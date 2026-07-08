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
<img src="https://cdn1.telesco.pe/file/H0VksxhbMHXQMpAOO5cklaiF3fRUdiDpsO2yxvbqh9Btfol55AdLf9QlUT-rBo-CxD9q3y2BNiXPeYdqSY1t4d0vt2Qi9tHAXq74aBFt6ETSKpFUkRy7s_NKcHOwyhH3Y3uPQfrvY1vlD3vxPVxVDL9u-s6XzmhtezIwLZRsSiPzW5fLwK5jXZasVruwAVKV0Rv1Sfd6IXOPtJOMxdAEiRS3yFJ52UpN4m_s0BMDTf4ofYycJlk-iobqWCJivx7zz0mmcR_FecxjhfhjsTbg_5xjUJPpezAFzemnUKWEd68qdcUnUXU5bSMmN7QUe7gWSg4uWT4VDWTvcq1bB0dj6Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.35M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 21:26:16</div>
<hr>

<div class="tg-post" id="msg-76845">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eojGcYoar86uIP5smGfT6haun-HTm0KVgQiv5w3GAPW7EKW7oPYsz5Dy41FTrwfm0dsiFT537guyJDIg6nmjQuCUV5fPjjoDDq41Ax__QrvXmBSqt6mrYq8cbkYfmyFGbmLQLXUxDDoo6lXNlomNq0RDRgu5QQMaJokBdmgmThTTj1OFzzB3ezIHyrjT16P8iyyDvJmnZy4j0ywOFfsq4qNGsYWTN2lhe4xO4FE3rsbZoH6v8jRlEwpxybL6OfreIhbYMPs8BiI2J1qvqICzYm92rRKB8W0t-ZR3Tvqmy0eT0bRqR2pI5sDBKR4oxdJCZoVW7sN411tAi-d8gAxj0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی ارتش جمهوری اسلامی با انتشار بیانیه‌ای اعلام کرد که در پی حملات آمریکا به مناطقی در جنوب ایران، هشت تن از نیروهای هوایی و دریایی ارتش در بندرعباس و بوشهر کشته شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/VahidOnline/76845" target="_blank">📅 20:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76843">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HQNIf_VCUcNM-v6GfhjqF3AqwvzfGd-QaFZfTh1RyP0ndILy3IwxNBq8wE6a7B0jVapDcgIxOUA1RPUJ1kpADus2h7gBNPGHPeH4rslFcarUYTpSggrDTCXznx4UgkpSiR2RQgolZQ4U8jrY6z0qxCNI3jQjevMTPuzIfn83fr9yVWEk2B_rXNuCml2fqZLTkte0Vhvtv9ubmr9H2aIahLR5Qi6ngnmNeAEpG8HXeYi1779IpyJJvtNREjVZqwKh-fppi15-LttLDJ8HNi4MvVaLNq7TEC6rEBI5XLLcmZXmF0Hq7VOlgyllfkHt-ISRbJCLOhSbelnpBPUs54JQaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ffbf0a91d4.mp4?token=CgDxqEUQZfpd2yby8_1SXNqK8K--2fNvTZUXitIFJ4UdbcoW2q9cztvQD0JmDrxJHtGWIZ5fAUZ9zL31Xh68E-OIq0hc9_PHxNtd3l8BnVvlq5CtrTr_xORtJPZPigpAKUOQi84mWweQ2CFB4Vzl4F74giDiQXHCjr9Wa3KThl-qMwEy9a4ZslYH0VB_yJyqpNmVoX4TckkvwknjFqXuDaasXRo2Fg-SHk3vhgb_PrSVQZplhUElxarPTJwbTpLfTixQP_WMgSiGJ-fID5HBvLF54nSj1Z1fJXx2tQOSY6CdbLEidw7jpRCXx5MeDPfOOsD1e_miJV41H2QtlmrPfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ffbf0a91d4.mp4?token=CgDxqEUQZfpd2yby8_1SXNqK8K--2fNvTZUXitIFJ4UdbcoW2q9cztvQD0JmDrxJHtGWIZ5fAUZ9zL31Xh68E-OIq0hc9_PHxNtd3l8BnVvlq5CtrTr_xORtJPZPigpAKUOQi84mWweQ2CFB4Vzl4F74giDiQXHCjr9Wa3KThl-qMwEy9a4ZslYH0VB_yJyqpNmVoX4TckkvwknjFqXuDaasXRo2Fg-SHk3vhgb_PrSVQZplhUElxarPTJwbTpLfTixQP_WMgSiGJ-fID5HBvLF54nSj1Z1fJXx2tQOSY6CdbLEidw7jpRCXx5MeDPfOOsD1e_miJV41H2QtlmrPfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رییس‌جمهوری فرانسه، چهارشنبه در حاشیه نشست ناتو در پاسخ به خبرنگاران گفت حملات جمهوری اسلامی به پایگاه‌های آمریکا در خلیج فارس، توافق موقت را نقض کرده و تهران در انجام این حملات اشتباه کرده است.
امانوئل مکرون در عین حال گفت انتظار دارد نشست‌ها در چارچوب آتش‌بس ۶۰ روزه میان آمریکا و جمهوری اسلامی ادامه یابد.
@
VahidOOnLine
فریدریش مرتس، صدراعظم آلمان، نیز در حاشیه این نشست گفت: «ما به دونالد ترامپ گفته‌ایم که باید یک توافق پایدار با ایران حاصل شود، اما این ایران است که مسئول آخرین نقض توافق موقت آتش‌بس است.»
@
VahidOOnLine
دبیرکل ناتو، حملات تازه آمریکا به مواضع جمهوری اسلامی را «کاملاً ضروری» خواند.
مارک روته، پیش از نشست سران ناتو در آنکارا به خبرنگاران گفت وقتی آتش‌بس برقرار است و جمهوری اسلامی «عملاً آن را نقض می‌کند»، واکنش قاطع آمریکا اهمیت حیاتی دارد.
روته روز سه‌شنبه نیز گفته بود هرچند جمهوری اسلامی در حوزه موشکی و هسته‌ای تضعیف شده، ناتو همچنان باید نسبت به تهدیدهای آن هوشیار بماند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/VahidOnline/76843" target="_blank">📅 20:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76833">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Apc-suF6wfbgBVJAt2oHd47hvzBLkwXiFSDoD9uTbo_vMYQCQnlJ7OVFCAJ1x5quJmRi5iAvJ1myjlMcnFy7TdUjx6dztRjtPJfkAH6UnEtrtouup5wYd7BXInuazodu21XrZCSSKA-FcTPdt5F-zBY65uWfWb-9mayJeIiAaAWlxQsTTTM9Uv3cOpap1HDeA0ZGBwKbCVpdRvxUEM-5j1ijdZk92MCgZpAasJ6urcZCi9tfEq8TbAbbTFzhPOA_UwrqoB1FZ-LrLGX4nLn_tLitdPtyG_5HkiPAbfyQYkrZdkprf4YhnbA3HMKul37HILiMHLa56Jg8NwH8MWaKHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Orn_t-xqucoTt6uc0Loy-0udNF9mTgwaIcWv81D8r0x4zsoYMiO7uxaKhrsTN469HtioRHMxh4vM9rW6CmoZrTYwvLh2531QzAKVnBM8Iwr4mzNLOszLVY2IXbStPnpepKc1n5nuLR1PY7-ZOiFsb7ruFhNbWvbIXmDqPsR9SXjccRwC_fIt-ghze6NNukWe_GchXH06IlELXfMulWgt3qxFiUYQX06kFMOUy01-xKgQjv-XxpUhjrdqsG63QqXpFwk6F26Y9-TnOh4OY5zo47JesU_bYiOIcr3tXklUebahc-E0IqOBh8ak9ZGH0EObdCsDtCQHzB2EYj8NOPJ9bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SkHUnFfCOAdlPSkAjeSiBGHHRgKfWpcV9leTV2JRAd1BJsWo4FV9kx7YrgZ-FjAlkit7wmCmNNtFlgCQne_qHwnKI9D7EhFU_Rgu43alKKt-7srr9ZwWj7v4qyaLktcFWkHeWNQCpWj17OgKsRj1N5frQjGhscwehw7_7qOCeEY7sf_JH7fnK_ME1z1vLpvHDMBvvQLPuVYE8aIAgdWUTbHxyWkH-uvtFGbm2iy4_6WklxfQWw0gMZ5ZSNPbGR-Gr-cv1b5V-Td-6h-O-6lX3xaiVGdcZye65WkLD_L_78fUsRlaJIJUQdxn564BM67qUbZRxeBCVk2_oGwNGCZMig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uH7k6O1oZfe8VkI-9bKG0I-BUyuuvRAPY79IzlaPrRU4KdzBkojvik_6wdLuH0asDMta5uNuHr0SPFEyPYtT9JymBk5HEScl8WGXQTHvfMHBi-uIICEZvthXo1HQSJOneCJ_0jq1UE9oDeWPrGoTL0IjQBSgKADcQMDJ6EyVyC1BgOAo371OQ1BTarJdj2Kw0qYelbj2CKwlbtHezvsslZzuqm1NJc4BzXwq6adqZ1GncAN1egwcNWgKVDNmK9xBcaZsKW9pAc7j3R4jVSNCwMve5lIpMACcnF-8PaumySQg3kwP9cz3UIBH-dxvf7Q2pk8hqyf56ggVf9mHT7SVqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hZRKiWU0WlrM0gR7_RBV1wHRaGKYhY5lfmSo-1iWhcsSJ35w8w9II3j8Ud6LYi_oytJCQWmSvE9LlD9K6WdqOke-S_WD-QykxM_JcbHeIkiW_iOp3dGgNpAwqhkMDES5o9epPJ_FwmZiGMMB60seXdB0YetXSEcZPMNZkW7iApB8TGNSWxryP1Xg_P9RyLNxuyPtpjUeMzlG513b50OAFc1kHDrDmjwZHyaJDko4fruzwRG8bmp6Rg29iCe144_Q2DciFwpUSxjtOr_aErEsAQB_gVG2wnmfxOYu5-vZPWisXHxnImR6e5s3Vm20ynTYt6H9pfZ2vYtdiyG6IiKriw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e6cd91b041.mp4?token=gmfLuc62aGuVMDsOfuCUCMMl1DpESNyRFr7X2kI5IikFNumDBroSled2wx9t7qoOalbDvUVPxPlQcBqE6029es6x7TeCcEbbkrUMSaZeC-2pTPG9WcPRZpBhBnzHVoabLE9HHm4g4s0sMgEssRMbPrazFURQJjsqbkRT5m3abdMZXSMDTXUhR7-6KoEIFfDAL4ONMK5BkO4O60mmGuf3I_3VceiIo_MCFU8o8FVA1g-y1GcwL5oDDXcIO1Rk7ZmjHpx-_kki3Z67xskyo-0FI_xvoThQIEkKIP_rSLnmKiL1kWfZgjbCdBef4JmmzR0OH4CEdfH9CJhXsCe0uYw0pA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e6cd91b041.mp4?token=gmfLuc62aGuVMDsOfuCUCMMl1DpESNyRFr7X2kI5IikFNumDBroSled2wx9t7qoOalbDvUVPxPlQcBqE6029es6x7TeCcEbbkrUMSaZeC-2pTPG9WcPRZpBhBnzHVoabLE9HHm4g4s0sMgEssRMbPrazFURQJjsqbkRT5m3abdMZXSMDTXUhR7-6KoEIFfDAL4ONMK5BkO4O60mmGuf3I_3VceiIo_MCFU8o8FVA1g-y1GcwL5oDDXcIO1Rk7ZmjHpx-_kki3Z67xskyo-0FI_xvoThQIEkKIP_rSLnmKiL1kWfZgjbCdBef4JmmzR0OH4CEdfH9CJhXsCe0uYw0pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، گفت ارتش این کشور احتمالا امشب دور تازه‌ای از حملات علیه اهدافی در ایران انجام خواهد داد.
ترامپ پیش از دیدار با ولودیمیر زلنسکی، رییس‌جمهوری اوکراین، با اشاره به حملات جمهوری اسلامی به شناورها در تنگه هرمز گفت: «آن‌ها چند پهپاد و یک موشک به سمت شناورها شلیک کردند، در حالی که این شناورها حق داشتند در تنگه هرمز حضور داشته باشند. به همین دلیل دیشب بسیار سخت به آن‌ها حمله کردیم.»
او افزود: «احتمالا امشب هم بار دیگر حمله بسیار شدیدی انجام خواهیم داد. فقط کمی از قبل به آن‌ها هشدار می‌دهم.اما باید ببینیم در نهایت اوضاع چگونه پیش می‌رود.
@
VahidOOnLine
دونالد ترامپ، رییس‌جمهوری آمریکا، با تاکید بر نقض مداوم آتش‌بس از سوی جمهوری اسلامی، گفت: «آن‌ها هرگز تحت توافق ما به سلاح هسته‌ای دست نخواهند یافت. اما نمی‌دانم اصلا توافقی در کار خواهد بود یا نه؛ شاید این مسئله را بدون توافق حل کنیم.»
ترامپ گفت جمهوری اسلامی «هر روز» آتش‌بس با آمریکا را نقض می‌کند.
او افزود: «آن‌ها دروغ می‌گویند، تقلب می‌کنند و آدم می‌کشند.»
ترامپ بار دیگر از توافق هسته‌ای دوران ریاست‌جمهوری باراک اوباما انتقاد کرد و آن را «یکی از بدترین فاجعه‌ها» خواند.
او گفت: «توافق ما دیواری در برابر دستیابی به سلاح هسته‌ای است، اما توافق او [باراک اوباما] جاده‌ای به سوی سلاح هسته‌ای بود.»
@
VahidOOnLine
رئیس‌جمهور آمریکا با انتقاد شدید از مقام‌های جمهوری اسلامی آنها را «بیمار» خواند و گفت ما به آنها گفتیم بروید و مراسم تشییع جنازه خود را انجام دهید. آنها به جای آن، دیروز شروع به شلیک موشک به کشتی‌ها کردند.»
دونالد ترامپ که در کنار مارک روته، دبیرکل پیمان آتلانتیک شمالی، ناتو، در آنکارا با خبرنگاران صحبت می‌کرد با اشاره به حملات هوایی شب گذشته اضافه کرد: «ما هم دیشب ضربه سختی به آنها ضربه زدیم، خیلی سخت.»
@
VahidHeadline
ترامپ گفت: «آن‌ها درخواست یک وقفه کردند. می‌خواستند برای مراسم تشییع جنازه خامنه‌ای بروند. من گفتم این فرصت را به آن‌ها بدهید. و آن‌ها دو موشک شلیک کردند. منظورم این است که این دیوانه‌وارترین کار بود.»
رییس‌جمهوری آمریکا افزود: «ما می‌توانستیم آن‌ها را بکشیم؛ بنابراین فکر می‌کنم باید از این زاویه هم به موضوع نگاه کرد.»
او همچنین گفت جمهوری اسلامی درخواست کرده بود که آمریکا آن‌ها را نکشد و افزود: «ما گفتیم قرار نیست شما را بکشیم. هیچ کاری نکردیم. در واقع، ما امنیت آن‌ها را هم تامین کردیم.»
@
VahidOOnLine
ترامپ در جریان نشست خبری در آنکارا، جمهوری اسلامی ایران را به اشتباه جمهوری اسلامی «ژاپن» خواند. او بار دیگر اشاره کرد که در جریان جنگ، جمهوری اسلامی ۱۱۱ موشک به سمت ناوهای هواپیمابر آمریکایی مستقر در منطقه شلیک کرده است. فرماندهی مرکزی ارتش آمریکا، سنتکام، پیش از این اعلام کرده بود که این موشک‌ها رهیابی شده یا به هدف نرسیده‌اند.
@
VahidOOnLine
ترامپ گفت که حملات اخیر ایالات متحده به ایران «تاثیر فوق‌العاده‌ای» داشته است. او گفت که در این حملات، سامانه‌های راداری که تهران در حال بازسازی آن‌ها بود، منهدم شده است.
ترامپ هشدار داد که آمریکا می‌تواند تنش‌ها را بیش از پیش افزایش دهد. او گفت: «تاسیسات تولید برق، نیروگاه‌های برق... اگر مجبور شویم، آن‌ها را از کار می‌اندازیم» و افزود: «تاسیسات آب‌شیرین‌کن... اگر لازم باشد آن‌ها را هم هدف قرار می‌دهیم. دلم نمی‌خواهد این کار را انجام دهم.»
او همچنین اظهار داشت که ایالات متحده می‌تواند جزیره خارگ، جزیره‌ای با اهمیت استراتژیک در سواحل ایران را «تصرف» کند و گفت که در آن صورت، ایران «هیچ کاری» نمی‌تواند در برابر آن انجام دهد.
@
VahidOOnLine
ترامپ گفت جمهوری اسلامی «هر روز توافق را نقض می‌کند» و به همین دلیل آمریکا «چاره‌ای جز ادامه حملات» علیه ایران ندارد.
ترامپ با اشاره به توافق آتش‌بس، گفت: «آن‌ها هر روز توافق را نقض می‌کنند. دروغ می‌گویند. تقلب می‌کنند. مردم را می‌کشند.»
رئیس‌جمهوری آمریکا همچنین با انتقاد از دولت‌های پیشین ایالات متحده افزود: «در ۴۷ سال گذشته هیچ رئیس‌جمهوری کاری در برابر آن‌ها انجام نداد.»
@
VahidOOnLine
ترامپ بار دیگر تاکید کرد که ذخیره اورانیوم با غنای بالای ایران، تنها به‌وسیله تجهیزات آمریکایی قابل استخراج است. ترامپ با اشاره به حملات تابستان سال گذشته، یادآوری کرد که این مواد زیر آوار تاسیسات و زیر کوه باقی مانده است.
رئیس‌جمهوری آمریکا، با تاکید بر این‌که نیازی به اعزام نیروی زمینی به ایران نمی‌بیند، گفت: «وقتی که آن‌ها کاملا از بین رفته باشند یا توافقی حاصل شده باشد، برای خارج کردن مواد هسته‌ای می‌رویم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/VahidOnline/76833" target="_blank">📅 20:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76832">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v-USQ9zqrM_4HpDfcKrPyknm6cBYxSTBNDn_uRvUQw8qMXZV3Y7yZCVDCHeXl9oXT_zblLMDl-wsT8dxSv9_nhsCxMgPLMT60X7CN825C78xSNAF7FWeQcfYBZughwDyd5i4_CpY6Ceh4oalWYwSTu1jqNk5Ks61lQ5uIW4JdI62f1UBMYeOrcCCVnRTflYkquJEgCY52d1c1JQ4yiVb-MgOIXP8QusJ1iFxNdJe4XSAJmT3eO4KQsKpAkUyQKbGk8FE-s-to97qQUeLKjEvhx_mgsCyZyFehjNdmXDGCVybhF_g6pQdAj4FK23u1t_z9okPZZkMZZpMiYm-jjeVHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عفو بین‌الملل هم‌زمان با گذشت شش ماه از سرکوب خونین اعتراضات سراسری دی‌ماه ۱۴۰۴ در ایران اعلام کرد با توجه به این‌که در ایران «هیچ چشم‌اندازی برای تحقق عدالت وجود ندارد»، دادخواهی قربانیان این سرکوب باید از مسیرهای عدالت کیفری بین‌المللی «به‌عنوان اولویتی فوری و غیرقابل مذاکره» دنبال شود.
دیانا الطحاوی، معاون مدیر منطقه‌ای خاورمیانه و شمال آفریقای عفو بین‌الملل، در بیانیه‌ای که این سازمان روز چهارشنبه ۱۷ تیرمنتشر کرد، گفت: «با گذشت شش ماه از زمانی که نیروهای امنیتی ایران طی دو روز، هزاران زن، مرد و کودک را به‌طور غیرقانونی در سراسر کشور کشتند، ناتوانی جامعه جهانی در برداشتن گام‌های مؤثر برای پیگیری عدالت بین‌المللی غیرقابل توجیه است.»
الطحاوی افزود: «این بی‌عملی به تداوم چرخهٔ سرکوب مرگبار کمک می‌کند؛ چرخه‌ای که در آن بازماندگان و خانواده‌های قربانیان از عدالت محروم می‌شوند و زمینه برای وقوع جنایت‌های بیشتر فراهم می‌شود.»
این مقام عفو بین‌الملل همچنین بار دیگر هشدار داد که تلاش‌های دیپلماتیک برای دستیابی به توافقی میان آمریکا و ایران نباید باعث نادیده گرفتن نقض گستردهٔ حقوق بشر در ایران شود.
به‌گفتۀ الطحاوی، مقام‌های جمهوری اسلامی تاکنون هیچ هزینه‌ای بابت استفادهٔ گسترده و غیرقانونی از نیروی مرگبار علیه معترضان نپرداخته‌اند و همین مصونیت از مجازات، آن‌ها را در تهدید به سرکوب‌های خونین بیشتر جسورتر کرده است.
به‌گفتهٔ سازمان عفو بین‌الملل، «با توجه به این‌که در ایران، به‌دلیل بحران ساختاری مصونیت از مجازات، هیچ چشم‌اندازی برای تحقق عدالت وجود ندارد، باید مسیرهای عدالت کیفری بین‌المللی به‌عنوان اولویتی فوری و غیرقابل مذاکره دنبال شود».
سازمان عفو بین‌الملل در بیانیه‌اش بار دیگر از جامعه جهانی و کشورهای عضو سازمان ملل خواسته است بحران حقوق بشر و مصونیت از مجازات در ایران را در صدر دستور کار خود قرار دهند، از ایجاد یک سازوکار مستقل بین‌المللی برای تحقق عدالت در مورد ایران حمایت کنند و از شورای امنیت سازمان ملل بخواهند وضعیت ایران را به دیوان کیفری بین‌المللی ارجاع دهد.
ماه گذشته، رئیس سازمان عفو بین‌الملل نیز نسبت به تداوم سرکوب داخلی در ایران ابراز نگرانی کرده و هشدار داده بود توافقی که صرفاً به‌طور موقت جنگ را متوقف کند اما حقوق بشر را نادیده بگیرد، خطر آن را دارد که به پوششی برای تداوم مصونیت از مجازات، اشغالگری و سرکوب تبدیل شود.
عفو بین‌الملل می‌گوید توافق ایران و آمریکا، موسوم به «تفاهم‌نامهٔ اسلام‌آباد»، تنها در صورتی می‌تواند به صلحی پایدار منجر شود که حفاظت از حقوق بشر، پاسخگویی عاملان نقض حقوق بین‌الملل، جبران خسارت قربانیان و تضمین عدم تکرار این نقض‌ها نیز در کانون توجه قرار گیرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/VahidOnline/76832" target="_blank">📅 20:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76830">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jnlX9Iw2zeOKeTl0WecACeUFC-6I9tZfMT98E2rp2IDTX113woevjpVGWG0TGxoNzEotF5mkkQthFjlFhfwrDV-jpc6gvVL6yI3dyhigqq_mYTHfrPtkiB3hR0okRmHq_-6rUigvFYpxDNzqtzNKV2IIVE9t39tmSuice3Sf3OcBONwFNymKchOb5BrSl0NrNAsHLllyH4vZKPSSyNdUyldM5KqSldoR6Z3Cy9uTS-ydk0T7fLeQa-w-YXvEIGpYtYpuJXol9BxuQAsaDWkL1XX5vJkSiNsqMz_iFg42xIPsCjhUI9rHVvCXuMKbLfiMxvG1aojcgSov2hIEgQgK2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ow6gRuR5pHxAgWmIUGEL7AYm-hzGH52nNnRU-HjoDBZnIOE4GOgZLFfvxJfsTSuEtXO63cuX-XSajJzbClUgnJeJocU2-f4pYPyzqMfLSPzqYH9CR4b3D68DRVvwueM7v61dwGqnEgy8aF60Jxy2LgikTsRPZCanbxyzUeolIrRLnQKalJuGchjTgT-QQt7LxCogin68kQEDKq21fYj3Rp4CRf6YrjH83V2oMrxyoDXZuHtXsMZmZwP6qLrPhvvuL9gF6_e06bupJlabn-2h65YHQIEeUNAV6_r7qoYLpO6gr74Kqu2OEwZApChsNXPePzkKVwn6F4kcvXKbdYzZow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، با اشاره به مراسم دفن علی خامنه‌ای، گفت جمهوری اسلامی به جای حرکت به سمت کاهش تنش، حملات موشکی به شناورها را آغاز کرد و آمریکا نیز در پاسخ، حمله‌ای گسترده علیه جمهوری اسلامی انجام داد.
ترامپ که در دیدار با مارک روته، دبیرکل ناتو، در آنکارا سخن می‌گفت، اظهار داشت: «ما گفتیم بروید مراسم تشییع خود را برگزار کنید، اما آن‌ها به جای آن، دیروز شروع به شلیک موشک به سمت شناورها کردند. به همین دلیل، دیشب بسیار سخت به آن‌ها حمله کردیم.»
رییس‌جمهوری آمریکا همچنین جمهوری اسلامی را «بیمار» توصیف کرد و گفت: «آن‌ها بیمارند. یک مشکلی دارند.»
ترامپ افزود حملات آمریکا «۲۰ برابر شدیدتر» از حملات تلافی‌جویانه ایران بوده است و گفت: «باید سرطان را از بین برد.»
@
VahidOOnLine
مارک روته، دبیرکل ناتو، در نشست خبری مشترک با دونالد ترامپ، رییس‌جمهوری آمریکا، در آنکارا، از حملات شبانه آمریکا به جمهوری اسلامی حمایت کرد و گفت این حملات «کاملا ضروری» بوده است.
روته با اشاره به حملات آمریکا افزود: «این یک پاسخ بسیار قوی بود و من در این موضوع با شما هم‌نظر هستم.»
دبیرکل ناتو همچنین از مواضع کشورهای اروپایی از عملیات نظامی آمریکا علیه جمهوری اسلامی دفاع کرد. او این اظهارات را در واکنش به انتقادهای ترامپ از برخی اعضای ناتو، از جمله بریتانیا و اسپانیا، به دلیل محدود کردن همکاری نظامی با آمریکا مطرح کرد.
روته گفت: «می‌دانم که شما درباره ایران ناامید شده‌اید، اما به نظر من این‌ها مواردی استثنایی هستند.» او افزود: «پنج هزار هواپیما از فرودگاه‌های اروپا در حمایت از عملیات «اپیک فیوری» به پرواز درآمدند و اروپا به سکویی بزرگ برای نمایش و اعمال قدرت آمریکا تبدیل شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/76830" target="_blank">📅 12:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76829">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fc9ddafbb4.mp4?token=c-s_Zh50Ufp5m_vRt-DJHfQNxPZBBwgDGtDKo-x1RLfF68fqrllC5PCkPLreVVRUGv8vNK8qwQNPLAHdQLaa9AmASYBSPai6Hz_JTh-Uy2rjPabSN3W8JjQ9nQ5sEsL-Pa9612tUxVeeKE7Nw-IFExIYt486fKC_oWoc3wJeiaHXdyD6bAHRdJmDpVu9cahIjGcYtdUaOG3B5z_D_hApXeZOBD4VES9RPlKRB6z4TVyufVR8RgrCDaT6TKUbU2bPmHnYtMQO3oHZKkwuA_yr1kLky1L2L3BXLVji_q8ADuUMwM5KnjGDNjOuSa6xgdTuLp1LSrt409jyary3jrVJsA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fc9ddafbb4.mp4?token=c-s_Zh50Ufp5m_vRt-DJHfQNxPZBBwgDGtDKo-x1RLfF68fqrllC5PCkPLreVVRUGv8vNK8qwQNPLAHdQLaa9AmASYBSPai6Hz_JTh-Uy2rjPabSN3W8JjQ9nQ5sEsL-Pa9612tUxVeeKE7Nw-IFExIYt486fKC_oWoc3wJeiaHXdyD6bAHRdJmDpVu9cahIjGcYtdUaOG3B5z_D_hApXeZOBD4VES9RPlKRB6z4TVyufVR8RgrCDaT6TKUbU2bPmHnYtMQO3oHZKkwuA_yr1kLky1L2L3BXLVji_q8ADuUMwM5KnjGDNjOuSa6xgdTuLp1LSrt409jyary3jrVJsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره مقامات ج.ا: یک مشت آشغال هستند!
نقل زیرنویس، ترجمه ماشین:
سؤالی دارید؟
ـ آقای رئیس‌جمهور، آیا آتش‌بس تمام شده؟ آیا آتش‌بس پایان یافته؟ آیا تفاهم‌نامه مرده است؟
سؤال بسیار جالبی است.
از نظر من، فکر می‌کنم [تفاهم‌نامه و آتش‌بس] تمام شده. دیگر نمی‌خواهم با آنها سر و کار داشته باشم. آنها تفاله‌اند. می‌دانید تفاله یعنی چه؟ آنها تفاله‌اند. آنها آدم‌های مریضی هستند. رهبرانشان آدم‌های مریضی هستند و آدم‌هایی شرور و خشن‌اند.
دروغگو هستند؛ ما توافق می‌کنیم. و اگر من با او توافق کنم، یعنی توافق داریم. و او بیرون می‌رود، حرف می‌زند. ما توافق می‌کنیم. همه موافقت کرده‌اند: هیچ سلاح هسته‌ای. ما توافق می‌کنیم. آنها بیرون می‌روند و با رسانه‌ها حرف می‌زنند. می‌گویند ما حتی هرگز درباره‌اش حرف نزدیم. یک جای کارشان ایراد دارد. آنها دیوانه‌اند.
آنها دروغگو و متقلب‌اند؛ مریض‌اند. آنها به مردم خودشان آسیب زده‌اند. تا همین حالا ۵۴ هزار نفر از معترضان را کشته‌اند.
می‌دانید وقتی مردم می‌گویند چرا آنها حکومت را سرنگون نکرده‌اند، نمی‌توانند سرنگون کنند، چون مرده‌اند؛ آنها را کشته‌اند. کسی سرنگونشان نمی‌کند.
آنها اسلحه ندارند و طرف مقابل مسلسل دارد و آنها را می‌کشد. رسانه‌ها این را گزارش نکرده‌اند.
اما آنها آدم‌های بدی هستند؛ آدم‌های بدی هستند. و صادقانه بگویم، نمی‌خواهم وقتم را با آنها تلف کنم.
حالا می‌گذارم مذاکره‌کنندگان فوق‌العاده‌مان اگر بخواهند به گفت‌وگو ادامه دهند، اما من چنین چیزی نمی‌بینم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/76829" target="_blank">📅 12:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76828">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uZ0CAfJazpcU3dTxntUPCbxG02WYrgKgL1_f1e1HEL-YGUhRrlg50qPpDxSxenxxT4PUDdBxr5XDx3HofbI1auYYduw72HPIjlNX99HSO3Y9ch2OgoQIsHPblDnNqRHY0wzwpKJteALZzfx4UGtx_lCheVzsKsYIpgX5fatrJeZekDdFR8gT3uNXLav1PFaBM0oziGLMpJezmVWaURZ_qsHjnhuyRQYSW8ElZGmMfXn_su-zrjujV2YsSgaIgcN2R6ak0vGS-b3pEQ3pGjcD2J6z3mTHmreWEXaMm65uYqzWxNxhHlDwewRWGa6PVdMeJv4Ywzz9VsX4Hk7NgzoSxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست پزشکیان، ترجمه ماشین:
رفتار دولت آمریکا به‌عنوان میزبان جام جهانی همان سیاست خارجی آشنای آن را دنبال می‌کند: دستکاری قواعد، زورگویی به رقبا، مانع‌تراشی و تقلب. این همان دستور کار MAGA آنهاست. ایران چنین بازی‌هایی را رد می‌کند. ما قاطعانه پای حقوق خود ایستاده‌ایم.
drpezeshkian
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/76828" target="_blank">📅 11:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76827">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
‌
الان زد بوشهر رو ۱۰:۴۱
سلام وحید جان ساعت ۱۰۴۰ صدای انفجار شدید در بوشهر
سلام وحید همین الان ساعت ۱۰:۴۰ دقیقه صدای دوتا انفجار شدیدی توی بوشهر شنیدیم
سلام وحید الان بوشهر رو زدن فکر کنم پایگاه هوایی بود دوبار صدا اومد
بوشهر پنج تا شش تا صدای انفجار سمت پایگاه هوایی و دریایی ارتش
بوشهرو الان دوباره زدن
بوشهر یه بار حدود ۱۰:۳۰ دوبار زدن یه بار هم حدود ۱۰:۴۰، بار دوم نزدیک‌تر بود
ما پایگاه هوایی بوشهر هستیم
حدود ساعت ۱۰.۴۰   دو تا صدای انفجار اومد
دو سه دقیقه پیش هم دوبار
به نسبت انفجارهای روزهای جنگ معمولی تر بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/76827" target="_blank">📅 10:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76826">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K7sfRLD-SLB3loHTawE0L7L54zbtkVlJqa6rcUdIelsxQvP5khBld77RuXByT5T2DCNiyJZW_Ks93ELg7nwMERM8S0JVS2zkfhwBbL8yjrg5LRIYmkTuGj74PSc7FZ3pw_OWyHQmvaz_xbUrULjL30MPHyO9QnvZ1T_kdQvUc8HIQpAFLJEoGHL_DOnYTrJMhaTOpCrO0UasZpbxtzSM7B_0O0U5Owu0XjJt-8TLn_FkVjJQEMygjEw-dmGG2NsPjBHQlxuvSMsbDEc9w45WqCUbUrQ9gUH3iQRcMkGt0fOfmCy9RF32YhW1RZAPCkx3E0_ktK4fGxbffi9srFuzKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه: پاسخ دادیم
منابع حکومتی:
پاسخ اولیه به تجاوز آمریکا با هدف قرار دادن ۸۵ نقطه از تاسیسات مهم نظامی آمریکا
اطلاعیه روابط عمومی سپاه پاسداران انقلاب اسلامی:
بسم الله قاصم الجبارین
🔹
به دنبال حماسه سازی ملت بزرگ ایران در تشییع دشمن شکن و پرشکوه بی سابقه یگانه دوران و قائد شهید امت اسلام، رژیم متجاوز آمریکا که روز به روز ابعاد شکستش بیشتر آشکار می شود و بازتاب جهانی خیزش عظیم و میلیونی ملت سرافراز عراق در بدرقه تاریخ ساز رهبر مجاهد شهید را شکست بزرگتری برای خود میداند، بار دیگر عادت پیمان شکنی خود را تکرار کرد و وحشت‌زده برای تحت شعاع قرار دادن این رویداد تاریخی، ارتش کودک کش و تروریست آمریکا در ساعات اولیه بامداد امروز با تهاجم هوایی به تعدادی از پایگاه‌های ساحلی و ایستگاه‌های غیر نظامی در سواحل استان هرمزگان و ماهشهر به طور آشکار آتش بس را نقض کرد و تفاهم اسلام آباد را زیر پا گذاشت.
🔹
در پاسخ اولیه به این تجاوز نیروهای دریایی و هوافضای سپاه پاسداران انقلاب اسلامی طی عملیات مشترک موشکی و پهپادی، ۸۵ نقطه از تاسیسات مهم نظامی آمریکا در بندر سلمان، منطقه پنجم دریایی بحرین و پایگاه هوایی علی السالم کویت را در هم کوبیدند و یک پهپاد MQ9 دشمن که قصد دخالت در عملیات را داشت، سرنگون کردند.
و ما النصر الا من عندالله العزیز الحکیم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/76826" target="_blank">📅 07:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76825">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIukIwSq0lQnuBghGnoCICgqip5WoONu75I9tzH3KFn_waknW6t1HKDM_UBoIEuugXbjd0_HCf2JXHctq3xGvtk9r0x-s3d8dGMJcMp82_HSr1Nq1eiruX9AumnddBjMOWHsxO9cyHotjrpi1x3Iw1rMEovBhdttT6uXqqigzQ2We_EphIhwBkyyziXyYCOUVbTBaLOu7la1AgcomnBlqhqhhDQ-TfL44fe4JKO3eeTzpuoou9MMIPAGrT4CTPJ4fObjwKHa52jR3aHN3GF8Z9iT65HK-6gCQBNv2hnAQIE6oDWXmIKpLezcrv5HSZ_oGg2AqgAtzg1zABv1sBCj3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس شوری اسلامی پس از حمله‌های بامداد چهارشنبه آمریکا به اهدافی در جنوب ایران در واکنش به حمله‌های دو روز گذشته سپاه به سه کشتی در نزدیکی تنگه هرمز در پیامی به زبان انگلیسی در اکس نوشت: کلیدی‌ترین موارد نقض تفاهم‌نامه ۱۴ بندی توسط آمریکا:
۱ - نقض ترتیبات ایرانی در تنگه هرمز
۲- تهدیدهای مداوم به حملات نظامی بیشتر
۳- حمله به مناطق جنوبی ایران
۴- بازگرداندن تحریم‌های نفتی
۵- استمرار حمله‌های اسرائیل به لبنان
او در ادامه این پیام نوشت: «دوره قلدری و باج‌گیری تمام شده است، راه به جایی نمی‌برید، ما اهل کوتاه آمدن و عقب کشیدن نیستیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/76825" target="_blank">📅 06:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76824">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UPhJT2QdAApAwRxR0zRU4qz3k85wUGHcajZIbfLenBsn2pQgWsH5qXabMquLV5KZHnKqgIBC2i27QglwOZ3ncg10qzqZGuw2z7FSP4g1OrudzbpWTNhpZvAsFRlK5Q3N6ZAzO7xDGtatBj5UEYfrgD2nmXN0dgTUuy8RDXScQe47yg343D7LGGYMzSOOA-fQyLEyYXlvfuwRCtF_unxWz7rsVfNCbaiCSVoE1sfwRkByiL9hE1vSdW6qXNLHfnFaa7I5J_QkDL_LYSIBSj2FOtGAXskPis9vC1dm55JNYSvWgfgtmCbxhPvFE43NENH4tDJWgMdN3NLntQfA6TU2qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
همین الان ساعت ۶:۲۷ چهار تا موشک داراب شلیک شد وحید
موشک پرانی همین الان داراب فارس
+ کلی چندی پیام مشابه دیگر از داراب و هم‌زمان پیام دریافتی درباره آژیر در بحرین:
Sirens again in Bahrain for the 2nd time just now
آپدیت:
ارتش کویت: پدافند هوایی در حال مقابله با حملات موشکی و پهپادی است
ستاد کل نیروهای مسلح کویت بامداد چهارشنبه اعلام کرد سامانه‌های پدافند هوایی این کشور در حال مقابله با حملات موشکی و پهپادی دشمن هستند.
در بیانیه ستاد کل ارتش کویت آمده است: «اگر صدای انفجار شنیده شود، ناشی از رهگیری حملات دشمن توسط سامانه‌های پدافند هوایی است.»
ارتش کویت از شهروندان و ساکنان این کشور خواسته است دستورالعمل‌های امنیتی و ایمنی صادرشده از سوی نهادهای مسئول را رعایت کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/76824" target="_blank">📅 06:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76823">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e118ef7ca5.mp4?token=WbRVGNcSqQ-BTc-Pan5G5C55nU5ZSclIZ99_aNotLwaOsi-QxRQOgI80psHsA9UzsJcyeXfOZAFlVGJGKAJ2mjqaZHr_RdNNBwvMnMpnUVJM2Q_gyV2UmzDFx18Vo1S_7iyCIcdjxM5MS7VCfz0ry13LNovJ_rf3x4DPVQ2_L5J8h-W0B-lm23pJCR8SUs31yWpXRxVPfUtPIzhuvXiaMvSmKzJgm4WIul4i4e2KitQ4ssVej0HwwABgU4W6YIpM4Kn6SQ0Ml7bbNAFleABrli9HjWIX6JoEKbxI-n0NDE1rgkdKPBABxKxcuNR7Rp4qsw4vuhfYgSV1DI0BQ7xbhw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e118ef7ca5.mp4?token=WbRVGNcSqQ-BTc-Pan5G5C55nU5ZSclIZ99_aNotLwaOsi-QxRQOgI80psHsA9UzsJcyeXfOZAFlVGJGKAJ2mjqaZHr_RdNNBwvMnMpnUVJM2Q_gyV2UmzDFx18Vo1S_7iyCIcdjxM5MS7VCfz0ry13LNovJ_rf3x4DPVQ2_L5J8h-W0B-lm23pJCR8SUs31yWpXRxVPfUtPIzhuvXiaMvSmKzJgm4WIul4i4e2KitQ4ssVej0HwwABgU4W6YIpM4Kn6SQ0Ml7bbNAFleABrli9HjWIX6JoEKbxI-n0NDE1rgkdKPBABxKxcuNR7Rp4qsw4vuhfYgSV1DI0BQ7xbhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: بیش از ۸۰ هدف نظامی را با مهمات هدایت‌شونده هدف قرار دادیم
ترجمه ماشین:
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده آمریکا (CENTCOM) روز ۷ ژوئیه دور تازه‌ای از حملات تهاجمی علیه ایران را تکمیل کردند و در واکنشی فوری به تازه‌ترین حملات ایران به کشتی‌های تجاری در حال عبور از تنگه هرمز، بیش از ۸۰ هدف را با مهمات هدایت‌شونده دقیق هدف قرار دادند.
نیروهای آمریکا سامانه‌های پدافند هوایی ایران، شبکه‌های فرماندهی و کنترل، سایت‌های رادار ساحلی، توانمندی‌های موشکی ضدکشتی، و بیش از ۶۰ قایق کوچک سپاه پاسداران انقلاب اسلامی را در تنگه و اطراف آن هدف قرار دادند تا توانایی ایران برای ادامه حمله به تجارت بین‌المللی در این گذرگاه تجاری بین‌المللی را تضعیف کنند.
ایران اخیراً به سه کشتی تجاری در حال عبور از تنگه حمله کرده است؛ از جمله M/T Al Rekayyat با پرچم جزایر مارشال، M/T Wedyan با پرچم عربستان سعودی، و M/T Cyprus Prosperity با پرچم لیبریا. این تجاوز بی‌دلیل از سوی نیروهای ایرانی نقضی آشکار و خطرناک از آتش‌بس است و آزادی کشتیرانی را تضعیف می‌کند.
نیروهای سنتکام در موضع آمادگی باقی مانده‌اند و آماده‌اند هر زمان که توافق رعایت یا اجرا نشود، ایران را پاسخگو کنند.
CENTCOM
قرارگاه خاتم‌الانبیا: پاسخ کوبنده می‌دیم
خبرگزاری رسمی جمهوری اسلامی، ایرنا:
قرارگاه خاتم‌الانبیا: نیروهای مسلح جمهوری اسلامی ایران به تجاوز و اقدام تروریستی آمریکا پاسخ کوبنده‌ای می‌دهند
🔹
تحت هیچ شرایطی اجازه دخالت در امور تنگه هرمز و مدیریت آن را نخواهیم داد.
🔹
بی‌سابقه‌ترین رویداد و حضور مردمی در تشییع و بدرقه قائد شهید امت اسلامی، شکست خفت باری را بر استکبار جهانی و آمریکای جنایتکار وارد نمود.
🔹
ارتش تروریست آمریکا بدون هیچ گونه پایبندی بر تعهدات خود و در شرایطی که پیکر مطهر رهبر شهید مسلمانان و آزادگان جهان میهمان مسئولان و مردم سلحشور عراق می باشد در تجاوزی آشکار برخی از نقاط جنوب کشور عزیزمان ایران را مورد هدف قرار داد.
🔹
نیروهای مسلح جمهوری اسلامی ایران به تجاوز و اقدام تروریستی آمریکا پاسخ کوبنده‌ای می‌دهند و تحت هیچ شرایطی اجازه دخالت در امور تنگه هرمز و مدیریت آن را به آنها نخواهند داد.
🔹
مجددا اعلام می‌گردد تنها معبر ایمن برای عبور و مرور کشتی‌های تجاری و نفتکش در تنگه هرمز، مسیری است که جمهوری اسلامی ایران آن را تعیین کرده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/76823" target="_blank">📅 05:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76813">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QEVFu8U0952TleyuRU8yRkt3ztLLd16lPDnnp2A0k1i1_56-N17pL7BjZhN2ufZxV-m0EKIuqtJdmGcVDZE-sk6BOrotfT6e1NKTMxhEpcjwhk72UDjzylFHkYDJ9pFUX2GDR5hD26P4rZ1hM_va6R1zh7C_iriBkj7abrpZtqqQTnTaAw83-4uBbwjPbvYOV5-M7DHJpjTOqyZ9L_syhaw3eKqEx3mmTR_mi6_AqizKG1JKy5HPZo0rBTT3GfbNYQktWvQeHCPtTI4mP2XSEY2mj-xd2RhhUyekz7xyx8DTgRmdElQS-l5CmT9tOBQkZyzIM6gpxMwhA_xmx5U7GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FrzzxmV8uXBzDfTnNyINbOr7bZsJj62Uu3UIG_u26aaFRsG-ksumkQrfWXheskS36Fg8_Bwm6nAw5MqBphBkurXlqCAE7DN6gupf0Q52PXN7-3TR3RAwmQqn2Nzbj2dwlLX0uhvU1bLVT7SILBB3q31TxPt3h-cqjlevC6IlkBgVvuC6VBRLiYS6rzUtMuhWeKLwmG0q0HK-TzPhjCbauN78bHMLEsK0X0T3hgupwskaLs3XRPu2j6uDDOIc_tL-SNCJzNAoBMEb1eB8Rhe2DQzji6N5Eym2i6-60LVdx84MpQgsiqGf1RyGpUxjlne4ukD5J6nyv3GFZ7MQ0WqROQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Cj9h7RAxm_nk5VanNva0vcwwdPPsyzfLrLUERucCP0s4wlb1mb8qjjMf7qm9oKEOe-3QsrLYbtZbWsEDflE0JZzRZBdIQvwBBNs2DVYm7asBbYRUfdWFl7RAhBVylDAk9ahnvnO_DOljrp5NMdvjwedNEFqHcaDyWOccAElFzUfHOf87VE04g8_IkOXxqj3oy4ZPyUtjKdyhODn7H0nhP53QGbLhWObNlrA77MzNWc1IwcyOEvRSBp6sG1plgHBc1n7T1w216tmDM3arqg5RlKpEPdXkcNQWbQnBsAizC-ZJxZ5aE1j0sDIkZLkrVksVtxsmjOWUCg6-7Wx5cZFwRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IldpVn_M6RA_39c-MeDf6hD5l4BGtVeoClHD7xQrHUELhjOpqmnA7VxrFXz1WkD5SchlJ06j_lztSp6wK2rQdsEdmm-oFU0XO-wRh8XN1zdT-AF6wFcs1JQ51ckFhsxxVNoWj0ILCrmJa3eEXaa3nyxpr4tp0GDCsT3bUOXbn8aBcHfuPYgi79UQ4-QtZuXVhi2qmXR0kn7OG_Yf7KqFagulwvM9cb8_GT1XDzZoconE3MyNB6tXqBKwq5lloFKhPQIO_vmzwxNZTHkHMV9DQj4F4FoC8S-AcqNPA5EBXcE4-ZqtFFoJcVPZm83DgewTx_6kPlr2w5--ti6HqhJTEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vZQ9001npOlJr4Nj5fAyITQehQhJStvkGegmsPjAuj2ryUq1FHba2y2FXjg_2ytTZWhqUvV2_aucUwEDSWtxs65gujUR8J0A2M64CgKZLFCI-MwN19rbJPIeAvNqq8xYO6P_8UPhCCNyXY_JzA4qZLzDJKTbVZ7nT5aktMEihAR5CXL2Xz0AlafMBKYHge_ZSpriHt95ynas6lXKrfa31p92AYvs5F3Sfo5EczcACK3sAVsIWbu1R9wno2YHeZ7WDoJLK3hltgSNUGt6sbN7OqmHZLnSlSLJTmgUXOujn1i6zdLwT_uV4TQkp7dFjoMJUBGPR1OBU8Mx86KnYMEqWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/964f541742.mp4?token=H4VEkic7OOUTqK2XW451xlUyyF-B10thVAKdjYa7dLIFFG9MnDgNXdXkTxmf_IXqCRx18psJU8HD-lE90vh144tiPQV0dRDsel2Pe3g-WufHKF4kcAxtwB5EZc0SDn_D6DC2aEe3gJEbg1pRPia6i9_LjhPNOTebiPJhrpJPMVOv8Kolts3Nte068uWj_Tsn0Ccd6ANiDvdYKNX7vFmrtFXBC8cgHXbuqXSNTqgvzL0tuL1uGcK24f_UpTBNH8aIgfe02ITgkHAOSC3whMFEXhPsHVsraceqqylFenoU_45mfKQ9pMFGPzaFJB3yl0jqZqikVEJnsjmBHzEY6P23sg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/964f541742.mp4?token=H4VEkic7OOUTqK2XW451xlUyyF-B10thVAKdjYa7dLIFFG9MnDgNXdXkTxmf_IXqCRx18psJU8HD-lE90vh144tiPQV0dRDsel2Pe3g-WufHKF4kcAxtwB5EZc0SDn_D6DC2aEe3gJEbg1pRPia6i9_LjhPNOTebiPJhrpJPMVOv8Kolts3Nte068uWj_Tsn0Ccd6ANiDvdYKNX7vFmrtFXBC8cgHXbuqXSNTqgvzL0tuL1uGcK24f_UpTBNH8aIgfe02ITgkHAOSC3whMFEXhPsHVsraceqqylFenoU_45mfKQ9pMFGPzaFJB3yl0jqZqikVEJnsjmBHzEY6P23sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکان نیوز تصویری از یک انفجار بزرگ در بندرعباس و ویدیویی از انفجار در سیریک، در پی حمله هوایی آمریکا را منتشر کرد.
@
VahidOOnLine
+ تصاویر دیگری که با شرح امشب پخش شده‌اند و من از درستی همه‌شون مطمئن نیستم.
اسکان نیوز گزارش داد که ستون دود از سمت پایگاه هوایی بندرعباس مشاهده شده است.
منابع حکومتی:
مدیر بنادر و دریانوردی شهید باهنر و شرق هرمزگان: دود سیاه در پشت بازار ماهی‌فروشان بندرعباس ناشی از اصابت پرتابه‌های دشمن به اسکله صیادی بندرعباس و آتش گرفتن تعدادی از قایق‌های صیادی مردمی است.
🔄
آپدیت:
پرس تی‌وی، شبکه خبری انگلیسی جمهوری اسلامی، از شنیده شدن انفجارهای دوباره در جزیره قشم و نیز چندین انفجار در جزیره خارک خبر داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/76813" target="_blank">📅 01:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76812">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ke789N7kvYr1jweNfvgBiz5p4ZYSkHN1EAgaAzBTyas96e329cuocnGa62zst0D0nz-iq11-3ZCG8mIY_4taKZM3ds2VZn40VdXFqFwGx8bVedOGLOVSSeWi07aw4vxOaTn97nFmKsVIYf8y9gEvKZyG5yvwdFmG7u7IWjkQxDOcAQpUa34n4sFvsGw4NEp0t8MVomWepXpcU9GX8vywfVC02BItGy-z6e2LdBBTDO45ptVV45GuJOua9qjw9Oizo8jjRuy7u3Nmb43AAlx5h0AWmwaM4klenx3dx99C3ffB7vx-vHx8K7xIlB8JQ8UthRL3ZNB8UZeuvcXtMceGrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام آمریکایی به اکسیوس گفت اهداف حملات شامل سامانه‌های پدافند هوایی، سامانه‌های پایش ساحلی، موشک‌های زمین‌به‌هوا، پایگاه‌های موشک‌های کروز ضدکشتی، محل‌های پرتاب پهپاد و تأسیسات بندری ایران بوده است.
به گفته این مقام، حملات امشب از نظر گستره و قدرت، چهار تا پنج برابر بزرگ‌تر از حملات مشابه آمریکا در هرمز، ۱۰ روز پیش، بوده است.
رسانه‌های دولتی ایران نیز گزارش دادند که صدای چند انفجار در شهرهای بندری بندرعباس و سیریک و همچنین در جزیره قشم شنیده شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/76812" target="_blank">📅 01:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76811">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gKpaXn-yK3Xd2HKBDe1kQDC_hdcfZbKXxXzIY1Hplb-H-dDLhNBpxC0_dICQRQMdaw_aY9SL_wtYeUUS21Ghi53Ain_7_qRgh1Fc7IR-wHr8WYA_5W-VO-5Zy-sCoXGBSRfY_5XYw8ClqiGfx96Ll9aRrhu1JLmkhKAxRoz_QtGmZZ63GQAi1VNaOox7bnRbfHWUfH0ZM1tkW_EqNLTqFUCmI6tztcfLhsXj_1-ZlrzvFKgYBb9PJhF9ycan40OXX_BE_puq3ga9mjjVl5Tk8ynWwzWEyb91x-ykD-iiIUBsnH7e34-lELtNT2tEeaypKaTLCowe9o9to3jb4RUMDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه جمهوری اسلامی، در بیانیه‌ای، این که آمریکا اجازه نمی‌ده نفت بفروشند رو نقض تفاهم‌نامه خونده.
پیش‌تر امریکا هم
گفته بود
چون به کشتی‌ها حمله کردند، شایسته مجوز موقتی که صادر کرده بودیم نیستند تا رفتار مناسبی مطابق تفاهم‌نامه نشون بدن.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/76811" target="_blank">📅 01:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76810">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sho7ptQ-4aUbCrZcYk7Di0bkyat1uZ7aDzlQt5JT5BBSGIXbXQ-0cAhMBsIjAsCPHaSzL0wnKXGg3kpQZu6e8n1o4wBH_Hzsii7pnBrnPiBVVnE4UX-ItEIuoSPJjt69YRbbSgHK3D0aFjcSCpgxxuTSIhjxSZHqSJYny234yTO1g4Fix27Ae9TsgvLcXaE8IQiKaKGHJOO3RF0CTFoVf22GFWAL9I7XYQfVQNgGNytQHiGbSHKvaczRgxwTl-_M1BADM-V1cFqs0D1kCnYP-q21qBj911wkT7DZJGJRPATrkz_BKH2-b9gf_uMgNIIt8BwBpO1XUTVmbjKcgVLhvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
نیروهای فرماندهی مرکزی ایالات متحده آغاز به اجرای سلسله‌ای از حملات قدرتمند علیه ایران کرده‌اند تا به‌خاطر هدف قرار دادن و حمله به کشتی‌های تجاری با خدمه‌ای از غیرنظامیان بی‌گناه در یک آبراه بین‌المللی، هزینه‌های سنگینی تحمیل کنند. حملات آمریکا در پاسخ به حملات ایران به سه کشتی تجاری است که در حال عبور از تنگه هرمز بودند. تجاوز آشکار ایران بی‌دلیل، خطرناک و نقض روشن آتش‌بس بود.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/76810" target="_blank">📅 00:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76809">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پیام‌های دریافتی تاییدنشده:
سیریک، صدای چندین انفجار پیاپی.
جزیره هنگام الان صدای چندتا انفجار بزرگ اومد تعدادش ۱۰ تا بیشتر بود
صدای انفجار درگهان (جزیره قشم) میاد ولی صداش کمه انگار دوره به اینجا
سلام وحید جان بندرعباس صدای انفجار
قشم صدای چندین انفجار اومد
نفهمیدیم از کجاست
قبلش صدایی شبیه صدای هواپیما میومد
صدای دو انفجار ۱۲:۳۵ بندرعباس
سلام وحید جان
ساعت ۰۰:۳۲
ما روستای سوزا تو قشم هستیم
اول صدای جنگنده اومد
و بعدم صدای ۵-۶ تا انفجار اومد.
سلام ساعت 12:35 بندرعباس صدای انفجار اومد 4 تا.
سلام کشتی سازی بندرعباس خیلی صدا وحشتناک اومد
سلام بندرعباس ۴ تا صدای انفجار تا الان
آپدیت:
صدا و سیما:
شنیده شدن ۶ انفجار در روستایی حوالی شهرستان قشم
دقایقی پیش صدای ۷ انفجار در محدوده روستای طاهرویی شهرستان سیریک شنیده شد.
فارس:
دقایقی پیش مردم در حوالی سیریک و قشم صدای چند انفجار شنیدند.
هنوز محل دقیق و منشأ این انفجارها مشخص نیست.
🔄
آپدیت:
بندرعباس ۴ تا انفجار دیگه
دوباره ۴تا تا الان
شد ۸ تا ۹ تا ۱۰ تا
من مرکز شهرم خیلی بده
سلام وحید جان
ساعت 12.30 صدای 5 انفجار شدید ذوالفقار قشم شیب‌دراز  نزدیک جزیره هنگام
سمت پایگاه هوایی بندرعباس انفجار شدید همین الان
وحید جان سلام همین الان ساعت ۱۲:۴۷ بندرعباس چندین صدای انفجار پشت سر هم اومد لرزید
الان بندر عباس سه چهارتا انفجار بزرگ
درود بندرعباس ۱۲:۴۵ چندین انفجار پشت سر هم
همین الان کلی صدای انفجار اومد بندرعباس 00:48
سلام خوبی، همین الان بندرعباس صدای ۳ تا انفجار قوی اومد ساعت ۰:۴۵
بندرعباس چندین‌تا صدای انفجار پشت سر هم اومد
00/48 قشم پنج شش تا انفجار قوی
00.48 بندرعباس چند صدای انفجار پیاپی
🔄
صدای انفجار پشت سرهم بندرعباس 12:50
هنوز ادامه داره
یک سر دارن میزنن ۰۰:۵۰
مجموعا بالای ۱۵ انفجار
۰۰:۵۰ صدای ۹ انفجار دیگه هم با صدای شدید از سمت پایگاه هوایی داره میاد
بندرعباس ساعت.همین الان چند تا صدای انفجار پشت سرهم اومد۴۸دقیقه بامداد چهارشنبه۱۷تیر
سلام همین الان صدای انفجار پیاپی و نور نارنجی بندرعباس
بندرعباس رو همچنان دارن میزنن
👀
صدای انفجار و پدافند پی در پی بندرعباس همچنان ادامه داره
همین الان بندرعباس
صدای انفجارهای شدید، پنج تا شش انفجار
کشتی سازی بندرعباس، اطراف بستانو رو زدن
سلام صدای انفجار بندرعباس بیشتر سمت اسکله ساعت۱۲:۵۰چهار صدا سمت شرق اینجا صدا نمیاد سمت غرب بندر اینجا صدا میادسمت اسکله
🔄
ساعت 12:57 انفجار دوباره بندرعباس
بندرعباس ۱۲:۵۸ همین الان صدای خیلیییییی شدیدی اومد
خیلی تو شهر بود انگار
اقا وحید بندرعباس یجوری زد شهر لرزید
پیا پی اسکله باهنر داره میزنه پشت سر هم صدا میاد
ساعت 57 : 0 صدای شدید انفجار در بندرعباس
00:58 دو تا سنگین تر زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/76809" target="_blank">📅 00:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76808">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F8FZKJX6_47O6zwHPWQ2G2YLBzsnuFvXvqAmswyHqX9I6vI_0w1cO0FMJqLblHphl1qGNCTvpXxNqdeX654NiaWDaVJCDiQQ-QwbTThKwxy89b3fDs9oMYRjeLiv6J-IBOYumniwLxk65I7t5dcR6cPjk0kYguhtLSfS_EYJ_G84k1bHjAtzdtxo3fd-zoXUGOcNZERJeRSA8_QvQ9I0rUhoRWxCeMKvvS1EWMKU9oCe7ZyIsE9x5R1NYeiNYRC0hV0xOCbCg-ZOms-dpA2pfm1vjCqPM37mlPqwiEr9JDAjHVjqTGIT39XV4v5_6GkW7ViPSyghIjeF4qXv_bOoJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا معافیتی را که به‌طور موقت تحریم‌های نفتی علیه ایران را تعلیق کرده بود، لغو کرد و اقدامات جمهوری اسلامی ایران در تنگه هرمز را «کاملاً غیرقابل قبول» خواند.
یک مقام آمریکایی به خبرگزاری فرانسه گفت: «اقدامات ایران در تنگه هرمز برای ایالات متحده کاملا غیرقابل قبول بود و با عواقبی روبه‌رو خواهد شد.»
این مقام آمریکایی گفت تفاهم‌نامه واشنگتن و تهران «کاملا مبتنی بر عملکرد طرف‌ها است» و هشدار داد که ایران تنها در صورتی از مزایا برخوردار خواهد شد که «رفتار مناسبی» نشان دهد.
مجوز معافیت از تحریم‌ها که حدود سه هفته پیش اعلام شده بود، در ابتدا به جمهوری اسلامی ایران اجازه می‌داد به مدت دو ماه نفت خام و محصولات نفتی و پتروشیمی را صادر کند، تحویل مشتریان دهد و درآمد حاصل از آن را به صورت ارزی از راه بانک مرکزی وارد ایران کند.
اقدام آمریکا پس از آن صورت گرفت که بنا بر اعلام ناظران دریایی و دولت قطر و عربستان، در فاصله چند ساعت سه نفتکش، از جمله یک کشتی حمل گاز طبیعی مایع (ال‌ان‌جی) متعلق به قطر، در تنگه هرمز هدف حمله قرار گرفتند.
@
VahidHeadline
وزارت خزانه‌داری آمریکا مجوزی را که ۳۱ خرداد برای تولید، تحویل و فروش نفت خام، محصولات پتروشیمی و فرآورده‌های نفتی با منشا ایران صادر کرده بود، لغو و از روز سه‌شنبه مجوز عمومی جدیدی را جایگزین آن کرد.
وزارت خزانه‌داری آمریکا اعلام کرد مجوز عمومی X به طور کامل لغو شده و مجوز عمومی X1 جایگزین آن شده است.
بر اساس مجوز جدید، شرکت‌ها تا ۲۶ تیرماه فرصت دارند معاملات مجاز بر اساس معافیت ۳۱ خرداد را خاتمه دهند، اما
از ۱۶ تیر خرید جدید یا بارگیری نفت خام، محصولات پتروشیمی و فرآورده‌های نفتی با منشا ایران ممنوع است.
اوفک همچنین اعلام کرد هرگونه پرداخت به اشخاص یا نهادهای تحریم‌شده باید به حسابی مسدود و دارای سود در ایالات متحده واریز شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/76808" target="_blank">📅 22:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76807">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ga2W_Nt1OD6B8m-2C5Q9C_03RITn4Kh84mZ6Bj4Ewdb5e9gUEmUs3wfx-Wr-Io9d6oU6LfJwgf63uJLh1_S9C4U-tRwGViynvFOT8UZS9yeuTpfQG31gF2di8_F4NvidbNfSEiDwh0uDIK4g8fug_JIaoUAC_7PtYcxqUs6i2CEieclMz6rnFr8yegHlKiguxW-bzlMSx8zlV6ccA4JI2CHadHbgQDsvRDHFumdAeto2ZnoPzxHE38Xq_jnZBGTdbjF4qJxNCFfaCNDkawk-mNYdT6L61935fDV7M572o5-rX_Z2Bkp3goooLvuaSAebPL14OfimTzq04Nx3k_5bUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت قطر اعلام کرده است که در پی هدف قرار گرفتن نفتکش قطری در هنگام عبور از نزدیکی تنگه هرمز، کاردار ایران را به وزارت خارجه احضار کرده است.
در بیانیه وزارت خارجه قطر آمده است که این کشور حمله به کشتی خود را به‌شدت محکوم و آن را «نقض جدی ایمنی کشتیرانی بین‌المللی، تهدیدی مستقیم علیه امنیت عرضه جهانی انرژی و تخلف آشکار و صریح از قواعد حقوق بین‌الملل» می‌داند.
اعتراض قطر به ایران در قالب یادداشت اعتراض رسمی به محسن محمد قانع، کاردار سفارت ایران در دوحه و در محل وزارت خارجه قطر به او تحویل داده شده است.
وزارت خارجه قطر اعلام کرده که در این یادداشت از ایران خواسته است درباره این هدف‌گیری توضیحات فوری ارائه کند، اقدامات لازم برای جلوگیری از تکرار چنین حوادثی را بلافاصله انجام دهد و به‌طور کامل به قواعد مرتبط حقوق بین‌الملل پایبند باشد.
قطر همچنین اعلام کرد که این کشور تمامی حقوق خود را برای اتخاذ هرگونه تدبیر مناسب، مطابق با حقوق بین‌الملل، به‌منظور حفاظت از منافع و توانمندی‌های خود محفوظ می‌داند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/76807" target="_blank">📅 22:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76806">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTc7PTBk5DGCtWo2mOBE6NF0znaq0lRXjwF2PEBVmg-MLqHZ8orNSz7tyhdZQjUxmgssM7e12NmjnQJR2MTCChmC-b0qAwnjCA0CPm7B-Q2j8oKMvkj8j0rXv0jibOY81g7ldDuDLyVZgLn1rhPoTHR3aG5ByTAt9za9JiebfucZaCspzTiYF7hgmAvRx2jnvmxoazGXn2AyArfsK-yEFJaqM84gdRmi87ySddS0FsP7RMOo1TK01cUXBty7aJFww980q013K_tO9iMSC-GZGPa29pQcw4m3cNaG1jL-iXvmd6LkeeMDCBkEbYnDxYg5vhgAxrPHGmKW4RY0E9sNyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمید رسایی، نماینده مجلس جمهوری اسلامی، در شبکه اجتماعی «ویراستی» نوشت: حالا که دونالد ترامپ در تیررس ماست و برای اجلاس ناتو به ترکیه آمده است، رسما و بدون تعارف، محل استقرار او را در ترکیه با موشک هدف بگیریم.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/76806" target="_blank">📅 22:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76805">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UdYIwg71p4_jH9UY1a0fIT93YOaKHnZz5qSZ5IPy1pAyvZQ44jTzXiBjowTpLS6G3VtfCe7DtipXXgeHUojkvmeVgLjdzcIbT_s0DKkUMYJIejOKTtBylWcMe9GPVKvKjSrfO6UsllBb4pOBYaoaFfcTtlYlxv_Z-OiD228YlpLXz5MBgUYD0ncnl54iUV2z3ijWPik07DnQlrfY1ZXSjnxK37tv2hT5Epc_QgeY1Q_XeXn318Fa1mr-_nCevJ26x9uR7SpQVpUNRyXeOQnmPp14_KAm6Oy_plppdEHFGITrQu7s_SfHPcwfLvP0aa5uoOnudq5Xlx2WMVdxCwMBdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر اسرائیل روز سه‌شنبه ۱۶ تیرماه در گفت‌وگو با شبکه سی‌ان‌ان گفت که با وجود اختلاف‌نظرهای گاه‌به‌گاه با دونالد ترامپ، رئیس‌جمهور آمریکا، درباره ایران، آن‌ها در مسائل کلان مربوط به نحوهٔ برخورد با تهران «هم‌نظر» هستند.
بنیامین نتانیاهو افزود که هنوز زود است درباره آنچه پس از امضای یک توافق صلح موقت میان واشینگتن و تهران رخ خواهد داد، اظهار نظر کرد.
او اظهار داشت: «رئیس‌جمهور معتقد است که می‌تواند برنامه هسته‌ای ایران را متوقف کند»، اما افزود که در این باره تردیدهایی دارد.
نخست‌وزیر اسرائیل می‌گوید: «در مسائل بزرگ هم‌نظر هستیم و گاهی هم اختلاف داریم، اما متحدان واقعی هستیم».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/76805" target="_blank">📅 21:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76804">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gRHzdUnTBcWadkmoBS2wfqZi4Jd1duY-pXJbCB3GATQXbgKRKen24JlKgMqyqq6j5JH0l4hekWEgDOmlczPHlo0MwSRwKLCuXdr2LElmCj_RXwNhHuNLwwxwW3iZyFezJQvJ13OfeG48lCR3KMx6EAgbdD8ncQgnl3Z_i7Xq_ri2dEosBQ6IkZO2-X5VZb4d-ORMeQ2ffRoGn8yPkRl2YtcM4osfeQowWPLTq8SWBN5_5CrmaBeGDUGvaqauo-LscrOz0p9yvwNxP7HPlbhttdwckMxuct2GhtgodcbQFfqVxYRt099VCA0VShqIRFMv4FrND9xI3Vd0to234SBhIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام آمریکایی، روز سه‌شنبه ۱۶ تیرماه، به ان‌بی‌سی نیوز گفت حملات جمهوری اسلامی ایران در ۱۲ ساعت گذشته «تهاجمی» بوده و «نقض مستقیم یادداشت تفاهم» به شمار می‌رود.
به گفته این مقام، ارتش آمریکا امروز چندین پهپاد شلیک‌شده از سوی ایران را سرنگون کرده است. او همچنین با اشاره به حملات شب گذشته به دو نفتکش در محدوده تنگه هرمز، گفت که جمهوری اسلامی در این حملات از دو موشک کوتاه‌برد استفاده کرده است.
این مقام آمریکایی جزئیات بیشتری درباره محل وقوع این حملات یا میزان خسارت احتمالی بیان نکرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/76804" target="_blank">📅 20:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76802">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lCtACqczfIzAKf1Tb8ZVKJtfJRoCMVg5DWn-wUSyUnyUMhnY15vFYaTqpz1MrP2KY2-d2hrcXnmavqC-5upnX0Ge6VulNIDpL-S53QVtGmLYXoOVzM4nq-GIExMSGiC__a15fVPh8D41EZwK5TbGKZ-FvuHQdL0k3dGGDx_ppzbY7SH0CZirwl07834B-xwy6zluk63FgYDctS6m5uuYlt49ACLHSWVWpdaBLe7BrSAuYYdbdIjDD-pcadzcDKxtCuiEtgUB3-Vv_h3OMznM2h0mTNfPhauwoXUWt8BR02loSCJ4FAdjPN5s6M9dZ0HtCVwI6XgdG50G4CTWoi4zXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d3c7d37bab.mp4?token=AvHovjteevDy6dCyG-_XVoBonvutThZ7Ms3xK5vlqeeEMhfyVsQtcwoQq42dIwgjfUQH5FznpDKR7RAK_3vDpAGaDmDmV0kxHKq8aXbghIfkgPZ3O-nPkFVYUb8GOMwLsEVXoVwEd_ba9RfI-ZY6bqZ1qXbOcp6gc_iWoue9qCguVe5GNGtapxRru0rEeCwQFBM73Q2wecmmZK7tJEcA2k7ezMTTfumAxbfc8JRScEXxmdmRZW03H9HHIcXAX5aQVMyWk2TJXjtxAvjnsjBzaIxAzeHnoB7-oKUV_Mm-yjfwiU5CjQNvK6IRzIJYHKwQdtQiNI7izBDQOR_SXS-0xg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d3c7d37bab.mp4?token=AvHovjteevDy6dCyG-_XVoBonvutThZ7Ms3xK5vlqeeEMhfyVsQtcwoQq42dIwgjfUQH5FznpDKR7RAK_3vDpAGaDmDmV0kxHKq8aXbghIfkgPZ3O-nPkFVYUb8GOMwLsEVXoVwEd_ba9RfI-ZY6bqZ1qXbOcp6gc_iWoue9qCguVe5GNGtapxRru0rEeCwQFBM73Q2wecmmZK7tJEcA2k7ezMTTfumAxbfc8JRScEXxmdmRZW03H9HHIcXAX5aQVMyWk2TJXjtxAvjnsjBzaIxAzeHnoB7-oKUV_Mm-yjfwiU5CjQNvK6IRzIJYHKwQdtQiNI7izBDQOR_SXS-0xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز سه‌شنبه ۱۶ تیرماه در جریان سفر به آنکارا برای شرکت در نشست سالانه ناتو، در کنار رجب طیب اردوغان، رییس‌جمهوری ترکیه، بار دیگر از عملیات نظامی آمریکا و اسراییل علیه جمهوری اسلامی دفاع کرد و گفت این اقدام را نباید «جنگ» نامید، بلکه هدف آن «خلع سلاح هسته‌ای ایران» بود.
ترامپ با اشاره به نقش ترکیه در تحولات خاورمیانه گفت این کشور جمهوری اسلامی را «به‌خوبی می‌شناسد» و همراه با چند کشور دیگر، در تلاش‌ها برای پایان دادن به درگیری‌ها نقش مهمی ایفا کرده است.
او گفت اطمینان دارد رجب طیب اردوغان نیز خواهان دستیابی جمهوری اسلامی به سلاح هسته‌ای نیست.
رییس‌جمهوری آمریکا در ادامه با اشاره به روابط واشینگتن و آنکارا گفت: «این حتی جنگ هم نیست، یک عملیات نظامی است؛ خلع سلاح هسته‌ای ایران است.»
او همچنین با تمجید از توان نظامی ترکیه گفت این کشور می‌توانست وارد درگیری شود، اما چنین تصمیمی نگرفت.
ترامپ در بخش دیگری از سخنانش از عملکرد متحدان اروپایی آمریکا در ناتو انتقاد کرد و گفت از نبود حمایت آنها در جریان درگیری با جمهوری اسلامی «بسیار ناامید» شده است.
او اظهار داشت اگر نشست امسال ناتو در ترکیه برگزار نمی‌شد، شاید اصلا در آن شرکت نمی‌کرد و با اشاره به اردوغان، او را «دوست» و «رهبر بسیار قدرتمند» توصیف کرد.
رییس‌جمهوری آمریکا همچنین گفت ایالات متحده برای دفاع از اروپا در برابر روسیه هزینه‌های هنگفتی پرداخت کرده، اما در مقابل حمایت متقابلی دریافت نکرده است. به گفته او، در جریان تحولات اخیر عمدا واکنش متحدان را زیر نظر داشته تا مشخص شود آیا آنها نیز در مواقع لازم در کنار آمریکا خواهند ایستاد یا خیر.
ترامپ در این زمینه از بریتانیا، فرانسه، آلمان و ایتالیا نام برد و گفت مدت‌هاست این پرسش را مطرح می‌کند که آیا این کشورها نیز در صورت نیاز از آمریکا حمایت خواهند کرد یا نه.
@
VahidHeadline
رئیس‌جمهور آمریکا در عین حال تأکید کرد «ما به هیچ‌کس دیگری نیاز نداریم»، اما این پرسش را مطرح کرد که چرا آمریکا «تریلیون‌ها دلار در ناتو سرمایه‌گذاری کرده» تا از اروپا در برابر روسیه محافظت کند، بدون آن‌که چیزی در مقابل دریافت کند.
ترامپ گفت: «به نوعی داشتم دیگران را آزمایش می‌کردم تا ببینم آیا کنار ما خواهند بود یا نه، چون مدت‌هاست می‌گویم ما به آن‌ها کمک می‌کنیم، اما مطمئن نیستم آن‌ها برای ما چنین کنند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/76802" target="_blank">📅 18:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76801">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d41863b92e.mp4?token=Oz-NJTYyQMC_H5EuqKOwnMiOmlZgDx8Yf0zv9HbqUt8uKGulzP_O-CNwSezPCo4XqEscjjIwgCL2_gkM_BhU2brf4baExznBo1fcIRKCsqV4-MrsrRXF7E0-JSv9hkPD0jLaZIhHyvw6cF5-EuD-K4SJuD5qUS67IqW5_nHe6H4MJziiflKM2TA8xAgH1AA1zMTfi9zEDuff-DZ7KoSEfXeRgALTgzmTdirWMfUe7tra6Cd-WIe1pncNFzUg5Vy5fLj8GGDsvd4C_ZTmCorQMpBr_uK79KJfWVvsf2dIhOPGxM-m6bg2vMKiWY9wbwdgGitCKnZI0QPfvvZG6KFufQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d41863b92e.mp4?token=Oz-NJTYyQMC_H5EuqKOwnMiOmlZgDx8Yf0zv9HbqUt8uKGulzP_O-CNwSezPCo4XqEscjjIwgCL2_gkM_BhU2brf4baExznBo1fcIRKCsqV4-MrsrRXF7E0-JSv9hkPD0jLaZIhHyvw6cF5-EuD-K4SJuD5qUS67IqW5_nHe6H4MJziiflKM2TA8xAgH1AA1zMTfi9zEDuff-DZ7KoSEfXeRgALTgzmTdirWMfUe7tra6Cd-WIe1pncNFzUg5Vy5fLj8GGDsvd4C_ZTmCorQMpBr_uK79KJfWVvsf2dIhOPGxM-m6bg2vMKiWY9wbwdgGitCKnZI0QPfvvZG6KFufQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رجب طیب اردوغان، رئیس‌جمهوری ترکیه روز سه‌شنبه ۱۶ تیر، در نشست خبری مشترک با دونالد ترامپ، رئیس‌جمهوری آمریکا به مذاکرات جاری میان تهران و واشنگتن اشاره کرد و گفت که او و دولتش در تلاش‌اند که روابط آمریکا و ایران را به سطحی باثبات برسانند.
اردوغان در این نشست که در حاشیه اجلاس سران ناتو برگزار شد، تاکید کرد که این تلاش‌ها در راستای برقراری صلح جهانی خواهد بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/76801" target="_blank">📅 17:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76800">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHAFV3Sfwj-TkdAYjwi0QmqN2n0bUu-g5ffJylED8ZjW62ijOEV1Phub9c7YdRM6VzYHwll-SVRak17Pq-QJzoUVekgGy4xgPUy9lEu_RnvUpZcVn3nW3o1wWPOciSU3gCkpBx57KwkU8_IWeqWtO48EGqkRoPUoBmCq7iUzGbNfyKR6ACqMop8nSwadvkQvV8U7riweZKpZFMCVvZf6rcdzDYGa0n8j0UMJmr6yoTXrPo0uJHf5DLea9Uopljj4mCxOCK4YF5E-JrQiHDoUgi1x5HaRLSBN3NFWKVAJcfy2jHOehclxeLFceiiZ4e71Safp-K3auG7hUBlPfWJmJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا اعلام کرد یک نفتکش روز سه‌شنبه ۱۶ تیرماه هنگام عبور از تنگهٔ هرمز با یک پرتابهٔ ناشناس هدف حمله قرار گرفت.
این نهاد اعلام کرد نفتکش بر اثر این حمله دچار «آسیب سازه‌ای» شده، اما هیچ تلفات جانی یا آلودگی زیست‌محیطی گزارش نشده است.
این حادثه یک روز پس از حمله به دو نفتکش، یکی حامل نفت خام عربستان سعودی و دیگری حامل گاز طبیعی مایع قطر، رخ داده است.
خبرگزاری رویترز حمله به آن دو کشتی را تأیید کرده و وب‌سایت اکسیوس به نقل از دو مقام آمریکایی گزارش داده بود که سپاه پاسداران دست‌کم دو موشک به سوی آن‌ها شلیک کرده است؛ ادعایی که جمهوری اسلامی تاکنون به آن واکنشی نشان نداده است.
سخنگوی وزارت خارجه قطر روز سه‌شنبه اعلام کرد هدف قرار دادن نفتکش قطری «الرکیات» در نزدیکی تنگه هرمز، حمله‌ای غیرقابل قبول به امنیت کشتیرانی بین‌المللی و تأمین جهانی انرژی است و ایران را مسئول حمله به آن دانست.
هنوز هیچ گروه یا کشوری مسئولیت حملات تازه به نفتکش‌ها در تنگه هرمز را بر عهده نگرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/76800" target="_blank">📅 17:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76799">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c18721dbe0.mp4?token=NzOVaTBdur7eYo-ih8gqVn-dvjsWrTmZNTz9X_vZgodkzMyLioaAJm3gQpIhrRewF06nw1bF84YavKn_in_9WyyxEF9qs0wKeLAiTTADH2_ai7EnWmMUypH0qJkW7s40BIUL5s6Yeiv4svT6K9OsxhLF-_IoZM3ikhPhV7gFqZ9G9m97HJ1tBdsf-ME4srSEP_GHZoaxoa4BIPxBelYdhJtsI_3b-UBMkmJ0-T_52sGqgafjTH2_Q-nVw99hGG7MJ1o55qbiJ4dyugkDkH11qMJbnfeVR82FMEipH_7pfHsNC1dqkX-LAgXldPVY5gAzMyqrPWxr41NrPBj_0ZbAbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c18721dbe0.mp4?token=NzOVaTBdur7eYo-ih8gqVn-dvjsWrTmZNTz9X_vZgodkzMyLioaAJm3gQpIhrRewF06nw1bF84YavKn_in_9WyyxEF9qs0wKeLAiTTADH2_ai7EnWmMUypH0qJkW7s40BIUL5s6Yeiv4svT6K9OsxhLF-_IoZM3ikhPhV7gFqZ9G9m97HJ1tBdsf-ME4srSEP_GHZoaxoa4BIPxBelYdhJtsI_3b-UBMkmJ0-T_52sGqgafjTH2_Q-nVw99hGG7MJ1o55qbiJ4dyugkDkH11qMJbnfeVR82FMEipH_7pfHsNC1dqkX-LAgXldPVY5gAzMyqrPWxr41NrPBj_0ZbAbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری که در شبکه‌های اجتماعی منتشر شده گروهی از شرکت‌کنندگان در مراسم تشییع جنازۀ علی خامنه‌ای را نشان می‌دهد که به عباس عراقچی ، وزیر خارجۀ جمهوری اسلامی ایران، حمله کرده و او را «بی‌شرف» خطاب می‌کنند.
گروهی از هواداران نظام جمهوری اسلامی که با مذاکره و توافق با آمریکا مخالف هستند، اعضای تیم مذاکره‌کننده را به «سازشکاری» متهم می‌کنند. روز گذشته نیز تصاویری مشابه از حمله به مسعود پزشکیان در حاشیۀ تشییع جنازۀ علی خامنه‌ای منتشر شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/76799" target="_blank">📅 16:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76798">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqXaW5kdOKwJ_1OQV0k0uKvU5puNPL6Hh8A3m7nlKMlrgz3Xg8eUt3t794hdN6NhE5XO5hFd1veug3scG8XRZrKLf5pEuA032wbSSSwaPTtNFL6JcjJ9ak8Yf--oqMOvNbMcX6u62uyAodMyJwypCuwt55wCEXnULUydBs9fJIWXIFAiZSrhifxOXUI1LHqx0SSrQ1CB49_FOVJVA3aSAYEGp6F3oyZxoX-LFBpgLSXqXxj-_0KLGEWnW-to3EQgPzCuoGbKRLK6s4PLP4c_Zwu_meNQs_ZqleWdPCAqIWrZ2NAKiwYIg8f20ABxmmZCmVX1LLEUVHoCgUNkl6eEiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌زمان با نزدیک شدن زمان انتقال تابوت علی خامنه‌ای به عراق برای اجرای مرحله تازه‌ای از مراسم تشییع رهبر پیشین جمهوری اسلامی، محمدرضا سیستانی، فرزند ارشد علی سیستانی، مرجع عالی‌قدر شیعیان در نجف، به دفتر علی خامنه‌ای اطلاع داده است که پدرش بر تابوت او نماز نخواهد خواند.
در همین حال، جواد شهرستانی، داماد و نماینده علی سیستانی در ایران، نیز در مراسم تشییع و نماز میت علی خامنه‌ای در تهران حضور نداشت.
پیش‌تر محمدکاظم آل‌صادق، سفیر جمهوری اسلامی در عراق، اعلام کرده بود که مراسم استقبال رسمی از پیکر علی خامنه‌ای شامگاه سه‌شنبه در شهر نجف برگزار خواهد شد و آیین تشییع عمومی نیز از ساعت ۶ صبح روز چهارشنبه در شهرهای نجف و کربلا ادامه خواهد یافت.
خودداری علی سیستانی از اقامه نماز میت بر پیکر علی خامنه‌ای در حالی صورت می‌گیرد که جمهوری اسلامی از زمان کشته شدن رهبر دوم خود، مجموعه‌ای از مراسم تشییع و وداع را در چند شهر ایران برنامه‌ریزی کرده و اکنون نیز در تلاش است این آیین را با برگزاری مراسم در شهرهای مذهبی عراق ادامه دهد.
غیبت مهم‌ترین مرجع شیعیان عراق در این بخش از مراسم، یکی از مهم‌ترین حاشیه‌های مرحله عراقی تشییع علی خامنه‌ای به شمار می‌رود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/76798" target="_blank">📅 16:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76797">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H7u--PH87ixhTGdTG4YGd2HqKKuxMTEwdefXm06zFq_U9D_Lzr6In8AjlxcHTOhZUNGKXNNNZuGOK_aWuk8JST-ZO9bRLkUzF40QcxuMyHkBHvh1m_85ytTY8Yq0GJQy6QordjGbVNKxKKEAxczmi5l4vqfAjte6qbxgmkdI6bgVcVF-IRlg6n1Rwve8bpbhRpTDOsY6_Fa1TAZg0wMdIawuh0XNolRGFj-6y60Ad_8AV0UZxv0wmDeMGQlKITmvuKle-hndDbxzl7YQK3YqxK-7FcFUCxQop3j76ewBe2xigDtGKs82RL9VeiwYc6-JenXSQendZ53MfJdEFC523Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وب‌سایت اکسیوس به نقل از دو مقام آمریکایی گزارش داد که سپاه پاسداران روز دوشنبه دست‌کم دو موشک به سوی کشتی‌های تجاری در حال عبور از تنگه هرمز شلیک کرده است.
بر اساس این گزارش، دو کشتی در پی این حمله آسیب قابل توجهی دیده‌اند، اما هیچ تلفات جانی گزارش نشده است.
حمله گزارش‌شده پس از آن رخ می‌دهد که مهلت توافق یک‌هفته‌ای میان ایالات متحده و ایران برای توقف حملات در تنگه هرمز به پایان رسید.
اکسیوس می‌نویسد که ازسرگیری حملات ایران، تفاهم‌نامه‌ای را که کمتر از سه هفته پیش امضا شده بود، در معرض فروپاشی قرار داده است.
این منبع خبری می‌افزاید که
احتمال می‌رود ایالات متحده در واکنش، اهدافی در ایران را هدف حملات نظامی قرار دهد.
@
VahidHeadline
صداوسیمای جمهوری اسلامی به نقل از «برخی منابع» گزارش داد که «نفتکش الرقایات» متعلق به قطر، قصد داشت «با حمایت نیروی دریایی آمریکا» از مسیر عمانی تنگه هرمز عبور کند، اما «پس از بی‌توجهی به هشدارهای مکرر، هدف حمله قرار گرفته است.»
این گزارش تلویزیون حکومتی جمهوری اسلامی این‌گونه القا می‌کند که تهران این حمله را انجام داده است. با این حال، جمهوری اسلامی تاکنون به‌طور رسمی مسئولیت این حمله را بر عهده نگرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/76797" target="_blank">📅 16:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76796">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-V9B-Bvxi7uGzdDgStbQD7BLPMpalfNVsE90kslg-vDXzQzzlu3ptJsDKf2ACukn3Wu9U-XVY0l6vaCb7oyRNfY2s_hy4PuCUuNM4IwnZK_CX28cJipar6MVNi1rjdE_Vf4WnD_rpqTa8FvVb3zYhr9Jwwyu27to797pcFc-jeVmF6vxboFtTUywhygtfNG8ueaUionmAAIqAO9u2dIbORl-PKyX5CHfvr7JYQs9JUYHK3wSRF3tvAKaRlEbz80z9zgBMXfP7mo9z58B7Y1cj44zdYgZrT0GJ0LGiAtDF1-55VQdwC9bb6Z1adhEIOTDKpZrJENcKoKfgv5XVecZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO)، بامداد سه‌شنبه ۱۶ تیرماه، اعلام کرد یک نفتکش در حدود ۱۵ کیلومتری شرق لیما (Limah) در سواحل عمان، هنگام حرکت به سمت جنوب، از سمت چپ بدنه هدف یک پرتابه ناشناس قرار گرفت.
به گفته این سازمان، این حادثه باعث آتش‌سوزی در نفتکش شد، اما تاکنون هیچ تلفات جانی یا آلودگی زیست‌محیطی گزارش نشده است.
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد مقام‌های مسئول در حال بررسی این حادثه هستند و به همه شناورها توصیه کرد هنگام عبور از این منطقه با احتیاط تردد کرده و هرگونه فعالیت مشکوک را به این سازمان گزارش دهند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/76796" target="_blank">📅 03:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76795">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/418508ca7a.mp4?token=bH-uFVMBeJ75aWdAaAm-LD-TgcvoL5wvh5CouGkBzbX7W_vSRfR8fwIm0Ge3OpDPDIDKh6M17IL-Rp5n7Dlgdp43_-rLUDgdc8Kcm1zJof2pTojd26ipE8BJhMERGr3mIdP6Dc_C6pF67_0n5eWBlRg4HdOXsdfl_WYankH3aTrOCBFa2RpSj_Z2J2xx8AGOQXof14NORZPKBlWlnWwruZN8WPiPfD8zxlwlf6GOoC34SZj-dDxY43wHvCIWHkIbSGgMCQXkTOQY_65ZP4zHRTnnaBQwKIEhggDa0nKCsdDiuUEhodvEXhgABDq36GkYh6c8_tmnWXdjh5SLS8HPLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/418508ca7a.mp4?token=bH-uFVMBeJ75aWdAaAm-LD-TgcvoL5wvh5CouGkBzbX7W_vSRfR8fwIm0Ge3OpDPDIDKh6M17IL-Rp5n7Dlgdp43_-rLUDgdc8Kcm1zJof2pTojd26ipE8BJhMERGr3mIdP6Dc_C6pF67_0n5eWBlRg4HdOXsdfl_WYankH3aTrOCBFa2RpSj_Z2J2xx8AGOQXof14NORZPKBlWlnWwruZN8WPiPfD8zxlwlf6GOoC34SZj-dDxY43wHvCIWHkIbSGgMCQXkTOQY_65ZP4zHRTnnaBQwKIEhggDa0nKCsdDiuUEhodvEXhgABDq36GkYh6c8_tmnWXdjh5SLS8HPLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، گفت که از جانی اینفانتینو، رئیس فیفا، خواسته است اخراج فولارین بالوگون، مهاجم تیم ملی آمریکا، را بازبینی کند، زیرا به اعتقاد او خطایی که منجر به کارت قرمز شد، عادلانه نبوده است.
آقای ترامپ در جمع خبرنگاران در دفتر بیضی کاخ سفید گفت: «تنها کاری که کردم این بود که درخواست بازبینی دادم، چون فکر نمی‌کردم آن صحنه خطا باشد.»
او همچنین داوری را که این کارت قرمز را نشان داده بود، «افتضاح» توصیف کرد.
این اقدام بی‌سابقه، روند رسیدگی انضباطی فیفا را در کانون توجه جهانی قرار داده و با واکنش خشمگینانه بلژیک، رقیب آمریکا در دیدار روز دوشنبه برای کسب جواز حضور در مرحله یک‌چهارم نهایی، روبه‌رو شده است.
اتحادیه فوتبال اروپا، یوفا، هم به‌شدت از این تصمیم غیرمنتظره فیفا انتقاد کرده و آن را «بی‌سابقه، غیرقابل درک و توجیه» توصیف کرده است.
@
VahidHeadline
در ادامه واکنش‌های گسترده جهانی به رفع محرومت فولارین بالوگون، مهاجم تیم‌ ملی آمریکا، فدراسیون فوتبال بلژیک روز دوشنبه ۱۵ تیرماه اعلام کرد تصمیم فیفا برای صدور مجوز این بازیکن در رقابت مرحله یک‌هشتم نهایی جام جهانی را به چالش می‌کشد.
فدراسیون فوتبال بلژیک در بیانیه‌ای گفت از روند طی‌شده برای این تصمیم «عمیقا نگران» است و برای دفاع از «اصول بنیادین اخلاق، رقابت عادلانه و منافع فوتبال» به پیگیری این پرونده ادامه خواهد داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/76795" target="_blank">📅 22:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76794">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f07511960e.mp4?token=d24IArJYSxhUsJM9iBN8p5PmW3s0wTJVaBq4FYpbIJayZDwjD3thz0ygFGPVZgkEO5oKxPLnP4LplfpjyTtY5nCyKz7XY884FTEsO2FFFyAvfy-DJjo17b_I-0a5pJ9-NmV5Syj-Y78QrVHX3eky3WSL_I6GFrdkhNOB8iDvpv1LM3fY_lNqZ_Lp0KpwPiMk_azrxtvlVPwO2bPK7yIFBN1vD9reni0XbdUSfbzjSv6BwUrZiQ-f2FM7so-yxGXcVR_pX3cQS2RF9SxUAkWfWChPBtrg7-oip556WV3YN1sHeWvEP_aOULwqbtwwbslJgVoZjzwMg1Tlopem9nYz7A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f07511960e.mp4?token=d24IArJYSxhUsJM9iBN8p5PmW3s0wTJVaBq4FYpbIJayZDwjD3thz0ygFGPVZgkEO5oKxPLnP4LplfpjyTtY5nCyKz7XY884FTEsO2FFFyAvfy-DJjo17b_I-0a5pJ9-NmV5Syj-Y78QrVHX3eky3WSL_I6GFrdkhNOB8iDvpv1LM3fY_lNqZ_Lp0KpwPiMk_azrxtvlVPwO2bPK7yIFBN1vD9reni0XbdUSfbzjSv6BwUrZiQ-f2FM7so-yxGXcVR_pX3cQS2RF9SxUAkWfWChPBtrg7-oip556WV3YN1sHeWvEP_aOULwqbtwwbslJgVoZjzwMg1Tlopem9nYz7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه بار دیگر گفت: من به دنبال تغییر حکومت در ایران نیستم، هرچند این تغییر حکومت اتفاق افتاده است.
ترامپ افزود: حکومت اول از بین رفت، حکومت دوم از بین رفت. حکومت سوم معقول‌تر است. خواهیم فهمید.
@
VahidHeadline
دونالد ترامپ گفت آمریکا یا با ایران به توافق خواهد رسید یا «کار را تمام خواهد کرد.»
رئیس‌جمهور آمریکا در یک گفت‌وگوی تلویزیونی گفت قیمت نفت با وجود بسته شدن تنگه هرمز چندان بالا نرفت «آنقدر که ما نفت از آنها گرفتیم. مردم اصلا خبر نداشتند و همه اینها فقط در عرض یک ماه و نیم اتفاق افتاد.»
رئیس‌جمهور آمریکا بار دیگر تکرار کرد که کشتی‌های نیروی دریایی و تمام هواپیماهای نیروی هوایی ایران را از بین برده است: «در نهایت فهمیدند که دیگر رادار ندارند، چون سامانه‌های راداریشان نابود شده بود. بنابراین، آخر شب و در تاریکی آنها را هدف قرار دادیم.»
او همچنین گفت: «نیروی دریایی قدرتمند ما بزرگ‌ترین محاصره‌ای را که کسی ندیده اعمال کرد و در طول دو ماه حتی یک کشتی هم نتوانست از محاصره عبور کند. بعد نزدیک شدیم به اینکه شاید بتوانیم به توافقی برسیم پس محاصره را کاهش دادیم. نمی‌دانم، شاید هم به توافق برسیم.»
آقای ترامپ تاکید کرد که «به هر حال پیروز خواهیم شد. یا به توافق می‌رسیم، یا کار را تمام می‌کنیم.»
او گفت تمام کردن کار ایران کار آسانی است: «تمام کردن کار دشوار نخواهد بود. البته من ترجیح می‌دهم توافق شود، چون نمی‌خواهم ۹۱ میلیون نفر تحت تأثیر قرار بگیرند.»
«ما می‌توانیم ظرف یک ساعت پل‌هایشان را ویران کنیم. می‌توانیم شبکه تأمین انرژی را از کار بیندازیم. همه آن نیروگاه‌های بزرگ، زیبا و مدرنی را که ساخته‌اند. آنها پول زیادی داشتند اما حالا دیگر پولی ندارند. ما هیچ پولی به آنها نداده‌ایم اما می‌توانیم برق و نیروگاه‌های تولید برقشان را از کار بیندازیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/76794" target="_blank">📅 18:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76792">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e2iCryNpjIzngZ6O6HmULA-qWRUAB6syBoEhvtMMpwla6RxjqieUPWpjW6lbTq2bfWhYrBwlsqVrr08uPBGzDWAUx1CsZjvpwhzq1EzUuvJIbMG7WRE5db48xObMSHd7SQ29X14cW2_P5hazbCrEQYZ53BnFG6wv5aCb8oiZBT5w81fYnm4ZQhJdM6k1Ne3w_AVAySQbiqkmxMcL6xK87YIeaSGVnxbGHcyVJ0qtIdeT7m4rEbs0SoEUgDqWZqYbw4AV_mF_KbiCwQ7tidSZ_De7sJwgw7ZJtqTlFw8wGAuONM24EwkBHCRbg-j_GrPN3NujA4oH-13wP84Cw3iF5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/26366fc1dc.mp4?token=ZmTVgZi5kD-FmYdOz4GDGY41dRsFPsEYW15hmpxoVupkmCn53j8TJmWhUeJqI8mHSw_Xzh2g_LpRmVzorLNHDwqJ-DvOPkQ1Ton6ZFl97x7QNpvk8gBfz9lLa4g2UYOWhiUfbyQok1HZror1Llq-5mH4h8L6KH0U_6IhCqsQkCi1h9Q0rvO5X8D_8hq-WppdMCPds3V5Rn8L3naMeQ_j_EhMrko0cCp1vnlf0vofPAZ7MfrsDb19Td1neFxA829fSzILJhlTQVclDp2180FGXWtRYnC3dRniJ9kakGwUUBUH8yuWbfLccDphAdGMc4ZF55ifXOKt6WOYNY8-uNHBpw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/26366fc1dc.mp4?token=ZmTVgZi5kD-FmYdOz4GDGY41dRsFPsEYW15hmpxoVupkmCn53j8TJmWhUeJqI8mHSw_Xzh2g_LpRmVzorLNHDwqJ-DvOPkQ1Ton6ZFl97x7QNpvk8gBfz9lLa4g2UYOWhiUfbyQok1HZror1Llq-5mH4h8L6KH0U_6IhCqsQkCi1h9Q0rvO5X8D_8hq-WppdMCPds3V5Rn8L3naMeQ_j_EhMrko0cCp1vnlf0vofPAZ7MfrsDb19Td1neFxA829fSzILJhlTQVclDp2180FGXWtRYnC3dRniJ9kakGwUUBUH8yuWbfLccDphAdGMc4ZF55ifXOKt6WOYNY8-uNHBpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیمای جمهوری اسلامی روز دوشنبه ۱۵ تیرماه تصاویری از حضور احمد جنتی، دبیر شورای نگهبان در مراسم تشییع پیکر علی خامنه‌ای منتشر کرد.
رسانه‌ها روز دوشنبه همچنین تصویری از محمود احمدی‌نژاد را در مراسم مرگ رهبر سابق جمهوری اسلامی منتشر کردند.
خبرگزاری فرانسه روز دوشنبه گزارش داده بود در حالی که مقام‌های جمهوری اسلامی تلاش کرده‌اند تصویری از وحدت در صفوف حکومت ارائه دهند، تاکنون هیچ‌یک از روسای جمهوری پیشین جمهوری اسلامی، که روابطشان با خامنه‌ای دچار تنش بود، در این مراسم‌ها دیده نشده‌اند.
مراسم تشییع جنازه علی خامنه‌ای پس از دو روز قرار گرفتن پیکر او در مصلای تهران از ساعت شش صبح دوشنبه ۱۵ تیرماه آغاز شد.
روز ۹ اسفندماه ۱۴۰۴، در موج اول حملات اسرائیل به تهران بیت علی خامنه‌ای به‌شدت بمباران شد،‌ به شکلی که تمام ساختمان‌های محوطه بیت با خاک یکسان شده بود و همین احتمال سالم ماندن جسد رهبر سابق جمهوری اسلامی را بسیار کم می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 394K · <a href="https://t.me/VahidOnline/76792" target="_blank">📅 16:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76791">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgoxxczbMpqPYXVQk3piVj-M5U6AhMbvrgH5UkYCe-MB_KR0NCV2sxJd2U5ihdVOlTI-WTRGriYCn_8MxqM3QvHOimMgnWQoxwg2kI-EL66Bb6ajJaGmXw1SxLpsg-BYpDI5mW_xO5v7yjOasLbTHnWxMo4n7OLx4VJC8wGeot0QyUc3vPSAN1xxrI3_xkcFPUvNkcUutdkTZObZxmvZesjjYp3Z8VmNy-iDxg3uNb9VCsecpwxh4SO093haAA42ihZgHh0C2UhZcsI3sV1LI_aFQd_l5pisF2Q8cIlf6HB8hc5-xb84ie_VeFxGgGrgul-o9Od7ExVVmy8hxgcTGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شعبه ۱۵ دادگاه انقلاب تهران به ریاست قاضی ابوالقاسم صلواتی، آقای مهدی ناظر و خانم مهناز چاردولی، نامزد او، را به اعدام و ۱۰ سال حبس محکوم کرده است. همچنین خانم عاطفه ناظر، خواهر آقای مهدی ناظر، به ۱۰ سال حبس محکوم شده است. این سه نفر در تاریخ ۲۱ دی‌ماه ۱۴۰۴ در تهران بازداشت شدند.
@IranRights</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/76791" target="_blank">📅 16:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76790">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bZsYWsAsAyBghyHr23u1zvHV9o-42_K2_4RP2SMtJTnXCKwcw5W-kxZPItQpQFQF5pySUpLhKFjTssEBXsdZ5m32SO5sZR9bkslhrEYuf1INEYKqWmMEXH6ptc7-Nc0Y0pgL8AIAfhpOWcTOggqdCqQXyD_ipb85B8ljeXMglXBp0fhUCUQKyBdVu2jc9fEZCrCFC6Lu0o0B5WzFB-SYxEi1o6uLDpeK_GjC96M-NTpaxZvluI1Co64C5FUnHZSQ5dEfK5fjEj1YhXqGIDEq-YoEHv-wP87AyQWGAehRgX2Qb302a_G2Q-RYXqwjPTzG4zX72yJRb3fRYExKQaefeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه روز یکشنبه ۱۴ تیر متن حکمی را منتشر کرد که در آن مجتبی خامنه‌ای، رهبر جمهوری اسلامی، غلامحسین محسنی اژه‌ای را برای یک دوره جدید پنج ساله به عنوان رئیس قوه قضائیه ابقا کرده است.
محسنی اژه‌ای از دهم تیر سال ۱۴۰۰ با حکم علی خامنه‌ای به این سمت منصوب شده بود و مدت پنج سال ریاست او بر قوه قضائیه به پایان رسیده بود. حکم رهبر جدید جمهوری اسلامی با امضا در تاریخ ۱۳ تیر منتشر شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 438K · <a href="https://t.me/VahidOnline/76790" target="_blank">📅 19:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76788">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dQygc9rcqfDvMQGqYdbA1UCLLeffhmh7bQS4YDbDIhapwCS2TdxTLdVvZagW3xun56AJlTh173ni_qKHiEMXDnFtCqtEkDbCAFOE41W2M-dzqMyzWJt-VnNU1qcpuSsF_li8_d7Klby-0zj2aIUazuADBevFmCOVf7z9FKqXgXN6EdkXbOS8IL5VDFOtu_kvEa4SdFfVTipRQ3Tcy7zwFRd956J7vncGEzOOpp4WvJChGB_sNp3EPEEEL7B_AXFz5ecpjA3W8hPxoCVsREwNSppdXePeeptwwY9fES4EmSaItbQi1ReQQEYklrtiElmbeB-_oXqKPe8eEm9pILv8AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/15ac8211bb.mp4?token=IA8vwP16TqXxRH9wa4LjXqEtvPRUaP3me2FdFWcXV6BAEUcx-qX8t3PbAfMRgrOlotVrSsg65MC3XhFCN6RLsZpayhHD6iYC61UNXG54PT8QBRfCGhxqpazxcKH3i4lR6rQzheDW-DPshDW3IqeWJUgAvnpLq8pE2_I1nOcD8_zlvbBVmWHqzDF7L70SMa8M6GP7VZ16ty2xvDqWtFayPhbkUribO3btuCFS1aJ0S6fTKwAem4wGftLpRBv3ybhbYCES6sAkxdRzbqYD6AF05zsgodpI6Y8K45XRqQeJdwxnD1tk9WlnxguUQ-rfjgsBfxwa_U0qxRMsx2zMaCQLXA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/15ac8211bb.mp4?token=IA8vwP16TqXxRH9wa4LjXqEtvPRUaP3me2FdFWcXV6BAEUcx-qX8t3PbAfMRgrOlotVrSsg65MC3XhFCN6RLsZpayhHD6iYC61UNXG54PT8QBRfCGhxqpazxcKH3i4lR6rQzheDW-DPshDW3IqeWJUgAvnpLq8pE2_I1nOcD8_zlvbBVmWHqzDF7L70SMa8M6GP7VZ16ty2xvDqWtFayPhbkUribO3btuCFS1aJ0S6fTKwAem4wGftLpRBv3ybhbYCES6sAkxdRzbqYD6AF05zsgodpI6Y8K45XRqQeJdwxnD1tk9WlnxguUQ-rfjgsBfxwa_U0qxRMsx2zMaCQLXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماز میت بر جنازه علی خامنه‌ای، رهبر پیشین جمهوری اسلامی، روز یک‌شنبه، ۱۴ تیر رأس ساعت هشت صبح، توسط "آیت‌الله جعفر سبحانی" اقامه شد.
مراسم تشییع او بیش از چهار ماه پس از مرگش در حال برگزاری است.
اما نکته قابل توجه در این مراسم غیبت مجتبی خامنه‌ای است که از او به عنوان آیت‌الله یاد می‌شود و کمتر از ده روز پس از مرگ پدرش به عنوان رهبر تازه جمهوری اسلامی معرفی شد، اما در این مراسم حضور ندارد تا نماز میت را برای پدرش اقامه کند.
در این مدت طولانی از مجتبی خامنه‌ای نه فایلی صوتی منتشر شده و نه ویدئویی که نشان دهد او توانایی رهبری حکومت را دارد.
با این حال سه پسر دیگر علی خامنه‌ای، مصطفی و مسعود و میثم، که از روز ۹ اسفندماه سال گذشته یعنی آغاز جنگ تاکنون خبری از آنها نبود روز یک‌شنبه بر سر تابوت پدر خود حاضر شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 469K · <a href="https://t.me/VahidOnline/76788" target="_blank">📅 09:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76787">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyWOTESnLk5-LHfW2BKkPgjOBNXjM9j0j9g_Xm4NC3hLCuijQC1tnD_WQKEpqZi4wfyiIT08_-NMQl4SY8xjzhw8wZevj9GE2-9SXU1PqWA6_5t7iF5G49id_o-HxyUEJzPhspzVgKe1ZFVi5oTvyzUyYpjTAKVfUn2yoDSuJUSRKTJyAnOvaKvSVjbPMnMgPo7bcncli0EVme83wDp_mJNif6z5fjOgcuyVRWKLrPGtCQijotx0dCF-xTyr9bs28OCURy02UOzk4nlNH2p-NYsjz7xzTpJVDc78YOOjsViYBGBhXugYxgEeWTm6g3PjrEIW_CxL69i7yKCFUHvNzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا روز شنبه ۱۳ تیر، در گفتگو با وبسایت خبری آکسیوس، اشاره کرد که تصاویر مربوط به مراسم تشییع علی خامنه‌ای، رهبر پیشین جمهوری اسلامی را مشاهده کرده و از دیدن گریه افراد، متعجب شده است. او گفت:
از دیدن برخی ایرانیان که در مراسم تشییع گریه می‌کردند متعجب شدم چون گمان می‌کردم مردم از او متنفرند. شاید این اشک‌ها ساختگی باشد.
ترامپ پیش‌تر اعلام کرده بود که مذاکرات جاری میان تهران و واشنگتن، به‌دلیل برگزاری این مراسم یک هفته متوقف شده است. او در بخش دیگری از این گفتگو با اشاره به حضور اغلب چهره‌های سیاسی و نظامی جمهوری اسلامی در این مراسم گفت:
آن‌ها همه آن‌جا جمع شده‌اند. کار یک شلیک است! اما این کار را نمی‌کنم چون در آن صورت کسی برای مذاکره باقی نمی‌ماند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 467K · <a href="https://t.me/VahidOnline/76787" target="_blank">📅 23:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76786">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">این مجله ۹ ماه قبل از سرنگونی حکومت صدام‌حسین در عراق و سپس اعدام او نیز عکس صدام حسین را روی جلد برده بود. معمر قذافی نیز از دیگر رهبران منطقه بود که ۶ ماه قبل از کشته شدن به دست معترضان، عکس او روی جلد تایم رفت.</div>
<div class="tg-footer">👁️ 443K · <a href="https://t.me/VahidOnline/76786" target="_blank">📅 19:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76784">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8eed8d3ddd.mp4?token=MmPHVqqpNi5d_w3qmPdIfhuLPxZyAAVDPKbhgaFjYDiazxDPH1eFyvcPVTxtMf9OFc-X8bo7nO29rV_tA5Yg8mWMYtSFRdcn_oROP6j6N7UztC2WuZctdOZZrdUBU6NvJ2RtRg9OZO-o4Dnfx0PSwMKOBXY0YXBKnoeKnSx1z7ohd7rX6BE2A7RmiKZuswc_urcEjZA2EiNUk2AOOOJKndaw1ciPBNJbZYpgSSYH5nMlUnK9s9oiDWALLI62DLLDYEueqZ8sUtjJsh9ussgApv6jTgWtY0Cmmi_KWnlHm5Irb73KhvPJn3zZn9MyulDrlDQgyCncd7xLwfI3Iup2aA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8eed8d3ddd.mp4?token=MmPHVqqpNi5d_w3qmPdIfhuLPxZyAAVDPKbhgaFjYDiazxDPH1eFyvcPVTxtMf9OFc-X8bo7nO29rV_tA5Yg8mWMYtSFRdcn_oROP6j6N7UztC2WuZctdOZZrdUBU6NvJ2RtRg9OZO-o4Dnfx0PSwMKOBXY0YXBKnoeKnSx1z7ohd7rX6BE2A7RmiKZuswc_urcEjZA2EiNUk2AOOOJKndaw1ciPBNJbZYpgSSYH5nMlUnK9s9oiDWALLI62DLLDYEueqZ8sUtjJsh9ussgApv6jTgWtY0Cmmi_KWnlHm5Irb73KhvPJn3zZn9MyulDrlDQgyCncd7xLwfI3Iup2aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رحیم صفوی: این یک جنگ موجودیتی است و مطمئنم که اسرائیل از بین خواهد رفت
یحیی رحیم‌صفوی، از فرماندهان پیشین سپاه پاسداران و مشاور مجتبی خامنه‌ای در حاشیه مراسم تشییع علی خامنه‌ای، با اشاره به درگیری میان جمهوری اسلامی و اسرائیل، آن را یک «جنگ موجودیتی» خواند و گفت دو طرف در نبردی قرار دارند که تنها یکی از آن‌ها می‌تواند در منطقه باقی بماند. او افزود: «من مطمئن هستم آنچه باقی خواهد ماند ایران است و آنچه از بین خواهد رفت اسرائیل است.»
او همچنین با مقایسه کشته شدن علی خامنه‌ای با واقعه عاشورا، مدعی شد کشته شدن او، «حرارتی» در میان مردم ایران، شیعیان و جهان اسلام ایجاد خواهد کرد.
رحیم‌صفوی در بخش دیگری از سخنانش ابراز امیدواری کرد که مجتبی خامنه‌ای راه پدرش را در حفظ «ایران قوی»، دور نگه داشتن سایه جنگ از کشور و پیشبرد توسعه ادامه دهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 444K · <a href="https://t.me/VahidOnline/76784" target="_blank">📅 17:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76783">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhIgFLhbuh2jR0uOXfoSk6Lv4TXUz6HuERPMCVzBUqRPLhgDvvpOPMIKLzoSAYWEhugULQPX-QdpuqvL7-keT3Fq5E-g6Egq9hIw-5k5rTaSA3WAj3PAqIZGipEstNduHARHkZwwBv96_4tbGZ6FaLXAPzg-sbXZLdbXPE4g067v4hTnTP8S2CXHgCKDsLel4hKRmDGi2QtZQhORTd4pGvOU6vRCZH8CfkRyAdMIdiRRG7Tv8ujDOQeWNI6y6xjWgZLOFegRsyhx8WlgwsZQhxfZ40ogh7_dtcj0h4uYw_S0Pn4GRUHw4ABou0gULuetEB5Qsd84WiDqM5LFtQFbFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ اعلام کرد به‌دلیل مراسم تشییع جنازهٔ علی خامنه‌ای، رهبر کشته‌شدهٔ جمهوری اسلامی، «یک هفته» به مقامات تهران فرصت داده است.
رئیس‌جمهور آمریکا در سخنرانی خود در مراسم دویست‌وپنجاهمین سالگرد استقلال آمریکا که شامگاه جمعه ۱۲ تیر به وقت تهران برگزار شد، گفت: «ایران را به‌شدت در هم کوبیدیم. آن‌ها برای توافق بی‌تاب‌اند. به‌شدت می‌خواهند به توافق برسند. ما به‌خاطر مراسم تشییع، یک هفته به آنها فرصت دادیم، چون آدم‌های خوبی هستیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/76783" target="_blank">📅 17:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76782">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6cPaXLWlQ_LuqmfuFZt1Ufc6Bf_q5cVZkQKGZXpitkR5NbqbsMhvqjKINivjl__8DUlsKefsavvhitcZD60dtD-22eebkfIqoIoZFWqAk-UNr33Zt0iDoRlfsMrEWL_hjkuwWisqyzDHYuOXlhxCVA7EwTFmSQ8TRw84KztSzk4a_QITgfNEbQvt-1U61baMeuh8n2qX4NhK2o-UjfvlymD_13msn7bawjVE5BydKJJ1DLTv99BJkM3WFSFYV4Wlt6ytCuE_bMUoXN4_XYkiZgJqbeEtQN8kOtbnNOcV_v2lQ9aovylsdc_GBi_qgJnlNCZAe6z2Wgxb04jpnMHaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگین کیانی، عکاس مستند اجتماعی و مدرس عکاسی، از سوی دادگاه انقلاب بابل به یک سال حبس محکوم شد.
رسانه‌های حقوق بشری گزارش گزارش داده‌اند، شعبه اول دادگاه انقلاب بابل خانم کیانی را به اتهام «تبلیغ علیه نظام» به یک سال زندان محکوم کرده است. این حکم روز ششم تیرماه صادر و به او ابلاغ شده است.
نگین کیانی ۱۹ فروردین امسال در منزل پدری‌اش در بابل توسط نیروهای امنیتی بازداشت و یک روز بعد با قرار وثیقه آزاد شده بود.
این عکاس ۳۷ ساله پیشتر نیز به دلیل فعالیت‌های مدنی خود چندین بار احضار شده و با برخوردهای قضایی روبه‌رو بوده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/76782" target="_blank">📅 17:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76781">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wai0ELbU6dSew66Gj1IlIKN8y4o1mU8JVP2EW38DTpR5S5ilzE26kNcjop-QfOhCnNmtELDX0vh786anVDlswT5HxtDPvIzbqd4aRF8b2bseqfOBmVUWFHcmZBftAdXGHhTLWSL2T2KINXhDdJQRbX3lSisvPEH2Euk9YOKSadbCIPAGbeuScXxkSxX6IsAUmfdfGoQTJwaKZJ3NAykBD1RZysyef9saBlfuQSwzEDF3Gp2elQaVbhCaVyHJXYjG-J27Cwr7TRXJSBbWQlkF9YhSPQbq7LkMCPSIPWAz0kUFvk2pSSkf6wdc102YYtmzM2VTqczJFEJlV0BnshElrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرنوش پارسی‌پور، نویسنده، مترجم، تهیه‌کننده و فعال اجتماعی ایرانی، امروز در بیمارستانی در حومه سانفرانسیسکو درگذشت.
خانم پارسی‌پور که از دهه ۷۰ خورشیدی در شمال کالیفرنیا زندگی می‌کرد، از هفته گذشته به علت سکته قلبی در بیمارستان بستری شده بود.
او در سال ۱۳۲۴ در تهران به دنیا آمد و اوایل دهه ۵۰ خورشیدی از دانشکده علوم اجتماعی دانشگاه تهران فارغ‌التحصیل شد. نخستین داستان بلندش، «سگ و زمستان بلند»، را نیز در تهران منتشر کرد.
خانم پارسی‌پور در دهه ۵۰ برای مدتی در تلویزیون ملی ایران کار کرد و سپس برای ادامه تحصیل ایران را ترک کرد، اما در سال ۱۳۵۹ به ایران بازگشت.
او مدت کوتاهی پس از بازگشت به ایران بازداشت شد و چهار سال را در زندان گذراند. پس از آزادی به ترجمه و کتابفروشی پرداخت، اما فشارها ادامه یافت و سرانجام به آمریکا مهاجرت کرد.
خانم پارسی‌پور در سال‌های اقامت در آمریکا نیز چند داستان بلند و ترجمه منتشر کرد.
شناخته‌شده‌ترین آثار او در ایران «طوبا و معنای شب» و در خارج از ایران «زنان بدون مردان» است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 451K · <a href="https://t.me/VahidOnline/76781" target="_blank">📅 03:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76778">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Gh-39_gSKjueWsYKljmfe8EVeNDazF0noKzWa330LBy00WwyFkiHanhnm1672XawwmvkSLMqTKri6c0z3hkAPIT36s2ZMgb1a1AXD9j2iLWFQYNxLkcBE87vFVE5KvleZXQyr-BXiasyFlmQ69T1Fxmoss2OJKMMQ8a7TXquT_InWbaK1ZhrrAkyOgoUjJgfvNz8iEem8xaEPSkt6P2AH-Dm-ZvOZn7LanOBFsRDk3uq813EBZXSgh6y2PQT47YerZeM_dZ4ZH-Y9j4eee-C_lQMrQwaHJ9pl8QZy3L4zn_r2GeFX-GcUplddl625XSnMLgjA3DszLFBlmcNWswYvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CI3ivG5uO25OZukxEWVwTG8sKFQcm0j_9tTaIOZIwPq94AEzyDEWVQJJUcfMKQuNPJgL2sZ2zUIhBfjTnxs_9M6ptF1pzstlhLK0QfIE0lzPVX6vzP0Ly-Rx8xWOewNWG7UTSJmawH-jUvmQ4aj5CSD6RQtmubwOx28BbcxhUcJtC0KQB2qYNoai3WCtDn4Cx3u6cEwQEfP7dbQtpb_qR6kgURIhS0U-IlULznaYP3Sw78YgneSnjzNZ52fxiYZPopm_fuShQbK5U3Azf7wC79Wy4ah3D1V7hseXblmG9tUSCfzG9Q2roNK35sH1hdjMWrNKtSl1qiorwngDcQnkWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f3b6da11ae.mp4?token=Fi86H5jDBPlGPXAbMeVicnP5SzLbadgt7iWEHkcEBGf3Zr439X5syxI9X1LKX3MPaXb67uJUvdO9Oi8oTonqKAOQVnVz57NnY9zlOoYNtpO_N1YoRTn62oNT77NHztQE__rU0p9hpdyozavpVxBUCcEg22WLQf3eEU5atcKDwc77JHitMt-iIMvjfk-dsbLMkcfplBPl9JsCuWbPO3y4d9L37UN9j4gN22YNREUw_NLPShY7CuMaSPvDIP2W4x7E7ZGB8JFsjvt1QdUosRoU9Fa1JmCup_55eBX_7Kj_5HJA-eaIkx6f1aaytIs3uU3EvSCbmYqsV54REIJOuQ7I9w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f3b6da11ae.mp4?token=Fi86H5jDBPlGPXAbMeVicnP5SzLbadgt7iWEHkcEBGf3Zr439X5syxI9X1LKX3MPaXb67uJUvdO9Oi8oTonqKAOQVnVz57NnY9zlOoYNtpO_N1YoRTn62oNT77NHztQE__rU0p9hpdyozavpVxBUCcEg22WLQf3eEU5atcKDwc77JHitMt-iIMvjfk-dsbLMkcfplBPl9JsCuWbPO3y4d9L37UN9j4gN22YNREUw_NLPShY7CuMaSPvDIP2W4x7E7ZGB8JFsjvt1QdUosRoU9Fa1JmCup_55eBX_7Kj_5HJA-eaIkx6f1aaytIs3uU3EvSCbmYqsV54REIJOuQ7I9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📡
@VahidOnline</div>
<div class="tg-footer">👁️ 461K · <a href="https://t.me/VahidOnline/76778" target="_blank">📅 19:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76777">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/555882678d.mp4?token=WWJeR_JFG7oU3C2vsZk_U9YqKkN0crv62rmK2URWnzow3EiTkFE97tTlgJhoY3eTRZxNfKO69coAl1sEc0IoqfSpgmac_BDKwYDN8wxboRPjB-JVk3XPyxGSdNAfM8YTMxA_6_O2vnGqjj9ubuwbaAWvVn5wvaBEzSmw-xJ4HfvbEasf1DxIkFQ9EnhHo23OpZ8bFqnL9SFVIKeetIQjAxp48pGq-KxIQV6AUPoBsesqagzbWdVDig7pD9Ifnatg7Xd7xM8Rm2iTA7KF24XSnOKqQYH8IR2in66zE9Md2jdg_Pi2tVr2kxEwPrLx0eZonk0iRc08TX5tg6yXW8brOg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/555882678d.mp4?token=WWJeR_JFG7oU3C2vsZk_U9YqKkN0crv62rmK2URWnzow3EiTkFE97tTlgJhoY3eTRZxNfKO69coAl1sEc0IoqfSpgmac_BDKwYDN8wxboRPjB-JVk3XPyxGSdNAfM8YTMxA_6_O2vnGqjj9ubuwbaAWvVn5wvaBEzSmw-xJ4HfvbEasf1DxIkFQ9EnhHo23OpZ8bFqnL9SFVIKeetIQjAxp48pGq-KxIQV6AUPoBsesqagzbWdVDig7pD9Ifnatg7Xd7xM8Rm2iTA7KF24XSnOKqQYH8IR2in66zE9Md2jdg_Pi2tVr2kxEwPrLx0eZonk0iRc08TX5tg6yXW8brOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">[بنا بر تصاویر رسانه‌ها، مقام‌های مختلف در گروه‌های چند نفری در مقابل جعبه‌هایی که گفته می‌شود بقایای علی خامنه‌ای و تعدادی از اعضای خانواده‌اش در آن‌ها قرار دارند حاضر می‌شوند.]
رهبر ترکمنستان، روسای جمهور عراق، تاجیکستان، گرجستان، نخست وزیران پاکستان، ارمنستان، روسای مجلس جمهوری آذربایجان، عمان، قطر، عراق، ازبکستان، قرقیزستان، بنگلادش، مصر، وزراری خارجه نیکاراگوئه و کنگو و معاون رئیس شورای امنیت روسیه، رئیس اقلیم کردستان عراق، به همراه هیئتی از طالبان افغانستان و شبه‌نظامیان مورد حمایت ایران در عراق، یمن و لبنان و همچنین دبیرکل جهاد اسلامی فلسطین در مراسم ادای احترام شرکت کردند.
از نکات قابل توجه عدم حضور مقام بلندمرتبه‌ای از کشورهایی مانند چین، روسیه و ترکیه به عنوان حامیان جمهوری اسلامی ایران در این مراسم بود.
تاکنون تصویری از اعضای خانواده علی خامنه‌ای به جز هادی خامنه‌ای، یکی از برادرانش، در این مراسم منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 493K · <a href="https://t.me/VahidOnline/76777" target="_blank">📅 18:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76776">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q1KlnyaZcgxzDM-0K8B9V3z4lyfaXaIALN_PmCSswxM-eoRox25r2HqMaqRmYhnk-8CKK_H2q278MU-Lidu6FAdFW5T0FHpR_KmaUUdEO4f2Q_rYsOQOg2sHbyxD6EKOHnzNDmSkTkwaIJvn-7ocpPNywvgmrCYJvYGOkIga7ymUUGi8drSscAT2LtvtmiO6fBwG5AhnG_eCGFYgySzjwSI30m7KzroquD9RleFjHcORBjNy-ktLbeyEl7vmlljmPWIJ5jLVM751LKNUkf5kDSRioYCaNyFcP2jkOQBEzynI84IjFuldt8kxwTmpHmJL5RFatxMzCC6L0cBAISA1Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش سایت هرانا الهام زراعت‌پیشه، وکیل دادگستری، از سوی شعبه اول دادگاه انقلاب شیراز به شش سال حبس، دو سال ممنوعیت خروج از کشور و ابطال گذرنامه محکوم شده است.
بر اساس این گزارش، شعبه اول دادگاه انقلاب شیراز الهام زراعت‌پیشه را به اتهام «اجتماع و تبانی علیه امنیت ملی» به پنج سال حبس و به اتهام «تبلیغ علیه نظام» به یک سال حبس محکوم کرده است.
این دادگاه همچنین او را به مدت دو سال از خروج از کشور منع و گذرنامه‌اش را باطل کرده است.
الهام زراعت‌پیشه ۱۴ اردیبهشت ۱۴۰۵ در محدوده دادسرای اجرای احکام شیراز بازداشت شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 403K · <a href="https://t.me/VahidOnline/76776" target="_blank">📅 18:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76775">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHCSewXGk8MnFHEk2fva5m9xhLVTQeLlK3pSUmr8EiV-uwBpKGyQfjaOh2OA-IujCgJBHZ6_0CnVfo39OXsqAMWvfVBwhyEd90ofe3kAwCpUKl09pBKmdEBOrzLrVSPvq9k0qLxIuVr9pKZ6NboXg8pjBPMDpc_RI5MLhtQ9jYul0BxeRc9U3BXAyxrboRNfp3wqGqu-K5TiEAX1kZJfmebTFeGMRCGOz9R9Bg1QxmyhvsPqprgol4iHrF5h2z08dW1b1O68MIOe_Cm-P1xbza34Hfat_fejIpLRIzceu6miUF0oXhzndTvabcwOJXwGbzLJBgyuliApf90Reku1aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارغوان فلاحی، زندانی سیاسی ۲۴ ساله محبوس در زندان اوین، از سوی شعبه ۱۵ دادگاه انقلاب تهران به ریاست قاضی ابوالقاسم صلواتی، به اتهام «بغی» به اعدام محکوم شده است.
خبرگزاری هرانا، ارگان خبری مجموعه فعالان حقوق بشر در ایران، با اعلام این خبر نوشت حکم اعدام فلاحی بر اساس ماده ۲۸۷ قانون مجازات اسلامی و با استناد به اتهام «بغی از طریق عضویت در گروه‌های مخالف نظام و اقدام مسلحانه» صادر شده است.
ارغوان فلاحی در جریان پرونده‌ای بازداشت شد که چند متهم سیاسی دیگر نیز در آن حضور دارند. نهادهای امنیتی جمهوری اسلامی او را به عضویت در گروه‌های مخالف حکومت متهم کرده‌اند.
منابع حقوق بشری می‌گویند او این اتهام‌ها را رد کرده و روند رسیدگی به پرونده‌اش با محدودیت در دسترسی به وکیل و برگزاری جلسات غیرعلنی دادگاه همراه بوده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 429K · <a href="https://t.me/VahidOnline/76775" target="_blank">📅 17:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76774">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cFPhpG4QBhuuXuwr-_WoMvbZlJKk5TXlA5Cn1JmbQY8meD6Bv0R_WANajaQ_yAYapqoJBAMgVJc2rxGK5PnO4_h9XKuqjd0uY0b-SFylbgTduadj-Ho5oZG_m9Lxb0QWlXSVP4jCO3yBiGRbCsu7LDBU437IaX4biXV7Pflf4mtyqKC05ANDp-6QPuY6usUiOCRFwJwj-vKI5ycFwAWxKjqVSeRw-Aj5_c_LrdCE8DNLuUm_IZ0PqjDOAHX4yBZnVhVo_f-NhHKHGlNwXm3CzviSsuuciDrZ4wEyuBiz3T5KS5k-9OJykIUxJwUt_dycqvV57xm8S0DvbdagNAkM1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، بامداد جمعه ۱۲ تیرماه در گفتگو با شبکه سی‌ان‌بی‌سی گفت جمهوری اسلامی از نظر نظامی «کاملا شکست خورده» و مذاکرات میان تهران و واشینگتن ادامه دارد. او افزود: «فکر می‌کنم آن‌ها تقریبا با همه چیزهایی که ما نیاز داریم موافقت کرده‌اند» و ابراز امیدواری کرد این مذاکرات به نتیجه برسد.
ترامپ با مقایسه وضعیت کنونی با جنگ‌های گذشته آمریکا گفت برخلاف جنگ ویتنام، افغانستان و کره که سال‌ها ادامه داشتند، در چهار ماه نخست دولتش توانسته جمهوری اسلامی را از نظر نظامی شکست دهد. او گفت: «آن‌ها کاملا از نظر نظامی شکست خورده‌اند. هنوز چند موشک برایشان باقی مانده، اما اگر لازم باشد آن‌ها را هم از بین می‌بریم.»
رئیس‌جمهوری آمریکا همچنین گفت هفته گذشته پس از آنکه جمهوری اسلامی یک پهپاد را به سمت یک کشتی فرستاد، نیروهای آمریکایی سه بار مواضع آن را هدف قرار دادند و هفته پیش از آن نیز دو شب پیاپی حملات مشابهی انجام دادند. او افزود این عملیات‌ها هم‌زمان با ادامه مذاکرات انجام شده است.
ترامپ در بخش دیگری از سخنانش گفت آمریکا با استفاده از نیروی دریایی خود «دیوار فولادی» در اطراف ایران ایجاد کرده و «حتی یک کشتی هم نتوانست به ایران برسد.» او ادامه داد حکومت ایران با تورم ۳۰۰ درصدی، کاهش شدید درآمد و کمبود مواد غذایی روبه‌رو است و در صورت دستیابی به توافق، آمریکا می‌تواند گندم، ذرت و سویا را از طریق کشاورزان آمریکایی در اختیار ایران قرار دهد.
رئیس‌جمهوری آمریکا همچنین گفت «قدرت و جسارت» جمهوری اسلامی از بین رفته و با انتقاد از گزارشی در روزنامه نیویورک تایمز که نوشته بود ایران نسبت به چهار ماه قبل در موقعیت بهتری قرار دارد، افزود: «توان نظامی آن‌ها از بین رفته، رهبرانشان از میان برداشته شده‌اند، فرماندهان رده دوم و حتی برخی فرماندهان رده سوم از بین رفته‌اند، بنابراین نمی‌توان گفت امروز در وضعیت بهتری قرار دارند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 459K · <a href="https://t.me/VahidOnline/76774" target="_blank">📅 02:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76773">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M1DTeul076a7STLxIfPEDl2w8KV0Lj90hcikJahiIhaeATXCmihpAZEItdFJyVvgAfRDGvdCdwZVTgZLq_Tg2KkBcb3XdC6qFcfnDeS17AOFCXuqoOY1zDFXqZ-LCXUHpEacUs0Z8O25tLFPzsFpHeIuGrZ8aYNvN-q6WfAa1yuHof6lN8iGqeRjxHLH9OzfqAiOPJ1Iiz6bEVgM2Pzg93adSPVf6K9NghQECYLWrCldidys5dSt-NsMEcOsCTSh-tne6Yh-H8GguTjr_MkiW2zl_aJPeAAdgxFq2OGNzXT6F5racMimWpfryueckvyBJk1zal7wUMIvcwECBlWRtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"دارم خواب می‌بینم؟ سلام دنیای جدید!" ویدیو دریافتی از 'شادی جوانان شهر #گله‌دار در شهرستان مُهر استان فارس، یکشنبه ۱۰ اسفند' Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 433K · <a href="https://t.me/VahidOnline/76773" target="_blank">📅 16:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76772">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nn1Zg5EhemeWhmYxKqZnD_NOMAMJAABLcNOx8l7Ov4DUZ_lpzvqWUTTeOY0hxeQj8kBntMxv0zpsvx2Vrk17k3mt8NocFwt0OfyAo7acwiMIRvSRrwixucOnM1pmYn1-adMggALTTq_3fPXM0PltUHU5bSeBQkBGhagpqVrOfoBCaphryw4BDPGdh-DQlmmdIbvN69poFkAn8kdelX27nhlmQpb992tdDTgOtHwTH6fXPYJUOBp2UCFmKwqFsi2tENewz4MFsb8F3jo8ZnGDZvb-iSsJKvrZg4Y5UFNImQqp7c9CYP7wqLLDYzfPimdpwQtKj2r9pdKoZxw76Y5Trw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی کرابی (برسام) شامگاه ۲۱ دی‌ماه ۱۴۰۴ در منطقه سلسبیل تهران هدف شلیک مستقیم قرار گرفت و به کما رفت.
این جوان ۳۰ ساله که متولد سبزوار بود، بر اثر اصابت گلوله دچار مرگ مغزی شد و پس از یک هفته، در ۲۹ دی‌ماه ۱۴۰۴، در بیمارستان امام حسین تهران جان باخت.
پیکر او برای خاکسپاری به سبزوار منتقل شد.
ایران‌وایر مطلع شده است که به دلیل نقش بستن عنوان «جاویدنام» بر سنگ مزار او، مسئولان بنیاد شهید خانواده‌اش را تحت فشار قرار دادند تا این عنوان را به «شهید» تغییر دهند.
پس از آن‌که خانواده از پذیرش این خواسته خودداری کردند، سنگ مزار مجتبی کرابی (برسام) شکسته شد.
خانواده او نیز تصمیم گرفتند تا «روز آزادی» سنگی بر مزار این جوان کشته‌شده نگذارند.
مجتبی کرابی مربی بدنسازی، ورزشکار رشته فیتنس و داور رسمی پاورلیفتینگ بود.
یک منبع نزدیک به خانواده او به ایران‌وایر گفت: «مجتبی چند سال در کنار دایی‌اش، روح‌الله نصیری، از ورزشکاران نام‌آشنای خراسان رضوی، به‌صورت تجربی و آکادمیک آموزش دید و با تلاش و پشتکار توانست به‌عنوان مربی و داور رسمی پاورلیفتینگ، با مدرک معتبر، فعالیت حرفه‌ای خود را آغاز کند.»
او از هواداران تیم پرسپولیس بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/76772" target="_blank">📅 16:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76771">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c2c3ad4afb.mp4?token=j9vRU1fFdz4lh32iYHK5J0n0dGd_XxLfM3AYg4posJyXJCJuJq1Ix5gXkZf-PrHTtMPZD95E7unoLxPp6_jItQ5UdMURqdlj0I-0neNq_YIU_lDa4Mx3ESLrslruKsFq5uHW3bicC2gYalhk45Mz2j_lKOXSFh5iZ0PLvpjvzdks5UXupJiQf36fyC9DWYCCMt0So7t7QTwsHeLGS1au4OC0pnQjQgnC_zhsafyJdUfVz2NFgs-rSw_qoGntZBz86UMhr-P4LTYWCCxt71aqyvnHKoN0kX4wzxrX_brKEfmbfoUSNIkAZwHgR_8svZLtha-0BRB12aSdqcBRBuiMvg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c2c3ad4afb.mp4?token=j9vRU1fFdz4lh32iYHK5J0n0dGd_XxLfM3AYg4posJyXJCJuJq1Ix5gXkZf-PrHTtMPZD95E7unoLxPp6_jItQ5UdMURqdlj0I-0neNq_YIU_lDa4Mx3ESLrslruKsFq5uHW3bicC2gYalhk45Mz2j_lKOXSFh5iZ0PLvpjvzdks5UXupJiQf36fyC9DWYCCMt0So7t7QTwsHeLGS1au4OC0pnQjQgnC_zhsafyJdUfVz2NFgs-rSw_qoGntZBz86UMhr-P4LTYWCCxt71aqyvnHKoN0kX4wzxrX_brKEfmbfoUSNIkAZwHgR_8svZLtha-0BRB12aSdqcBRBuiMvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس مجلس شورای اسلامی می‌گوید گزارش‌های منتشره دربارۀ موافقت با دسترسی بازرسان آژانس بین‌المللی انرژی اتمی به سایت‌های هسته‌ای آسیب‌دیده «کذب است».
محمد باقر قالیباف در گفت‌وگویی تلویزیونی، که بخش دوم آن، شامگاه چهارشنبه ۱۰ تیر از تلویزیون رسمی جمهوری اسلامی پخش شد، با اشاره به قانون مصوب مجلس و مصوبۀ شورای عالی امنیت ملی جمهوری اسلامی، تأکید کرد که بر اساس قانون، «به هیچ عنوان دسترسی به سایت‌هایی که بمباران شده و آسیب دیده‌اند، داده نمی‌شود».
به گفتۀ مذاکره‌کنندۀ ارشد جمهوری اسلامی تعیین سطح دسترسی‌ها بر عهدۀ شورای عالی امنیت ملی‌ است و فراتر از آن، «هیچ امتیازی داده نخواهد شد».
محمدباقر قالیباف گفت بر اساس مصوبۀ شورای عالی امنیت ملی،‌ دسترسی بازرسان آژانس در حال حاضر به دو مورد نیروگاه هسته‌ای بوشهر و رآکتور تهران محدود است و به سایت دیگری دسترسی ندارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/76771" target="_blank">📅 16:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76769">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aMT14IFg1xk6gPmxXx4tTX_RPL8D5A4zK-3p0uHDIk8WVWTMhVGL-cDVo9gkmodL1pgGy14w9yOj1nrQp6osDXFEkMQBHlSgY2EQpQ01JPHb86buH9YrvAW8J43AJIohCX6N9psbQZJzrGYwdwg0qm_gN38y7iH3HbKfs6qhFC0g4zo8j3y30w6KnBW62f4EDrGNuhSH0Xq0dNFvH580c7GA0VhxhoXP5ENuMD9CE3qpFw0NnqIrbCZwsA5TqThYi7JADnhwdTQGa2N1yO5lQXSinuLI85evgx-boNCRg9JWXrsvJHk9p-K74Q04HyqZ0zaySlQ-T_pHfU_7kSVDoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/la-gznUXrlcKQm9iJMYQchooaZ17XUzh8EbPlt9h1RsdOZN1SPkQM6uxVGWv_6J1AvsGDbZXGWSP-CnS31Qo0GZOXjo4HWEvXU97w7KRlhs3LqeLVXwxcBUiOooRSoy8_dzEH2vW56FLWd-IDEAHBog-cSrASRs134geOk6rJOW_bz7iJZvDSkQRZMjI1JSmQXjtqzndJjT4soCijtaKAEy-RMoc-dSiW2TE59rI5PjlF4do6UNDNF48uXDnmqZOxO3zzbw7d-ohVktvY-uAL1Dhpu_JHGYO8uXhUzeTjBGeeZGfEVdkpRV2u30ektKztyd1NEjtFmFL5dJ7cTqLmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">منابع امنیتی عراق از وقوع یک حملۀ پهپادی به اردوگاه گروه‌های کرد مخالف جمهوری اسلامی در منطقۀ کوی‌سنجاق در شرق اربیل خبر می‌دهند.
هنوز جزئیاتی از این حادثه منتشر نشده، اما طی روزهای اخیر چند عضو سپاه پاسداران و نیروی انتظامی جمهوری اسلامی در استان‌های غربی ایران از جمله کردستان هدف حملاتی قرار گرفته و کشته یا زخمی شده بوده‌اند. یک گروه مسلح کرد هم مسئولیت برخی از این حملات را بر عهده گرفته بود.
مقام‌های امنیتی جمهوری اسلامی طی روزهای اخیر، بار دیگر از مقام‌های عراق و اقلیم کردستان خواسته بودند که به حضور گروه‌های کرد مسلح مخالف جمهوری اسلامی در خاک اقلیم کردستان پایان دهند.
سپاه پاسداران طی ماه‌های اخیر بارها با موشک و پهپاد به پایگاه‌های گروه‌های کرد در اقلیم کردستان و عمدتاً در اطراف اربیل حمله کرده است.
در همین حال خبرگزاری فارس به نقل از «منابع محلی» از وقوع چندین انفجار در اربیل و سلیمانیه، و از جمله هدف قرار گرفتن مقر «حزب آزادی» با موشک بالستیک خبر داده است.
@
VahidHeadline
درگیری‌های مسلحانه میان نیروهای سپاه پاسداران و گروه‌های مسلح مخالف جمهوری اسلامی در اطراف شهرهای سردشت و پیرانشهر، شامگاه چهارشنبه ۱۰ تیر و بامداد پنج‌شنبه ۱۱ تیر، ادامه یافت و به کشته شدن چندین نفر انجامید.
سازمان‌ حقوق بشری هانا اعلام کرد این درگیری‌ها در مناطق مرزی آذربایجان غربی رخ داده است.
رسانه‌های نزدیک به حزب دموکرات کردستان ایران نیز اعلام کردند در جریان درگیری عصر چهارشنبه در نزدیکی روستای «قزقاپان» در اطراف پیرانشهر، پنج عضو این حزب کشته شدند.
خبرگزاری فارس، نزدیک به سپاه پاسداران، بدون ارائه جزئیات اعلام کرد شش عضو حزب دموکرات کردستان ایران در این درگیری‌ها کشته شده‌اند.
کانال تلگرامی صابرین‌نیوز، نزدیک به نهادهای امنیتی جمهوری اسلامی، نیز مدعی شد در دو درگیری جداگانه، ۱۱ نفر از اعضای گروه‌های مسلح مخالف جمهوری اسلامی کشته شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/76769" target="_blank">📅 16:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76768">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p-8g7hkAVvUfLvO3z0Zznfqtlt-AWMlU0W7dgc6ksqAQZ13dtC3R63oY-9a1v-y_62wZzGgAmat_8Lxu7YdfkQyACQlI3LAIIgbwqc8ysbnMxNxY37pDCyXncgbwp4IIR2MWtISMt1SPm9EHuFgIzBZro_tKAKiNGmuor8Ha2ouOAvAOsKpH4qRsxHztv4OtOslvXf9LSx1xzEBcr30JxUM3gyh99uQc6VKeYRlldtV4f9gG78LuoX1f4162ZRNdsZft7sAgkWAQ4kkxtPfZHgWZ60rSwr9C3vLWZOkPKEG2pRkrZsDOPGr3cW0h2z03nzeCOwDyfH_VaCHL4yIxbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت کرمانی، وکیل دادگستری، از بازداشت دوبارهٔ سپیده کاشانی و هومن جوکار، دو فعال محیط زیست که پیشتر سال‌ها در زندان بودند، خبر داد.
آقای کرمانی به وب‌سایت «امتداد» گفت مأموران امنیتی عصر روز چهارشنبه دهم تیرماه با حضور در منزل این زوج، ضمن ضبط تمام وسایل الکترونیکی، آن‌ها را بازداشت کردند.
به گفته این وکیل دادگستری، نیروهای امنیتی همچنین سیما کاشانی، خواهر سپیده کاشانی را نیز بازداشت کرده‌اند.
او افزود تاکنون مشخص نیست این افراد توسط کدام نهاد امنیتی بازداشت شده‌اند و با توجه به تعطیلات پیش‌رو و بسته بودن مراکز قضایی، نگرانی خانواده‌های آن‌ها افزایش یافته است.
از دلایل بازداشت این زوج گزارشی منتشر نشده است.
سپیده کاشانی و هومن جوکار از اعضای مؤسسه «حیات وحش پارسیان» هستند که به همراه چند فعال دیگر محیط زیست زمستان سال ۱۳۹۶ توسط اطلاعات سپاه بازداشت شدند.
کاووس سیدامامی از بازداشت شدگان این پرونده که تابعیت کانادا را هم داشت، چند روز پس از بازداشت، به طرزی مشکوک در زندان اوین جان خود را از دست داد و مدتی بعد سازمان اطلاعات سپاه پاسداران دیگر فعالان محیط زیست بازداشت شده را به «جاسوسی» و «همکاری با دول متخاصم» متهم کرد.
سپیده کاشانی در طی سال‌های زندان در نامه‌هایی اعلام کرد که در دوره بازداشت تحت «شدیدترین شکنجه‌های روحی و روانی، تهدید به شکنجه فیزیکی و تهدیدهای جنسی» و «تهدید به مرگ» قرار گرفته‌اند.
او در نامه خود نوشته بود که بازجویان این پرونده «ویدئوی جسد» کاووس سید امامی را برای شکنجه به او نشان داده‌اند، و همسرش، هومن جوکار، را برای تهدید و شکنجه به پای چوبه دار ساختگی بردند.
سپیده کاشانی و هومن جوکار پس از سال‌ها زندان، در فروردین ۱۴۰۳ در پی عفو از زندان آزاد شده بودند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/76768" target="_blank">📅 16:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76767">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cccd78df1b.mp4?token=GKzU1yWZmdgTY90QKN_qlEyqbOv5XCN-uaIeDUVBsvfPp8-3cTMzb7nLsWzXcUmcHotZlMA-M9R0SuyNi_Qj3E9OF53r98noqhnbL3wV68vKFrfCJ8cCEaUhEgdKeFcK4qkTX7Zphy4N4bSQeRHpfObZL06G8-5wSFYjrxc0p0sGGdpzqXylYlj3tYPz8q7mSXaVKnybDqbRZTGhtilA9PVF0wpXV7X3lJiD8dLs_0SXhjzGpzDqs3tdxLUs45B1uqe2Hp2i5kdnaanHp2w_shujUhvkfgMjwreGsq2HV6zekHo3ipO1S931rg_ZxKYJp5RoK_OLCsW9GG8s0RSDVg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cccd78df1b.mp4?token=GKzU1yWZmdgTY90QKN_qlEyqbOv5XCN-uaIeDUVBsvfPp8-3cTMzb7nLsWzXcUmcHotZlMA-M9R0SuyNi_Qj3E9OF53r98noqhnbL3wV68vKFrfCJ8cCEaUhEgdKeFcK4qkTX7Zphy4N4bSQeRHpfObZL06G8-5wSFYjrxc0p0sGGdpzqXylYlj3tYPz8q7mSXaVKnybDqbRZTGhtilA9PVF0wpXV7X3lJiD8dLs_0SXhjzGpzDqs3tdxLUs45B1uqe2Hp2i5kdnaanHp2w_shujUhvkfgMjwreGsq2HV6zekHo3ipO1S931rg_ZxKYJp5RoK_OLCsW9GG8s0RSDVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غلامرضا نوری قزلجه،‌ ؛وزیر جهاد کشاورزی"، با تایید سخنان محمدباقر قالیباف دربارۀ خرید محصولات کشاورزی از شرکت‌های آمریکایی  در دوران ریاست‌جمهوری ابراهیم رئیسی گفت: برخی از قراردادهای کشاورزی از طریق منابع ارزی بلوکه شده ناشی از تحریم‌ها بود و آن‌ها نیز به شرکت‌های آمریکایی مجوز می‌دادند و از آن‌ها خرید می‌شد.
محمدباقر قالیباف شامگاه سه‌شنبه در یک گفت‌وگوی تلویزیونی به خرید محصولات کشاورزی از شرکت‌های آمریکایی در دولت ابراهیم رئیسی اشاره کرده بود. پخش سخنان مذاکره‌کننده ارشد جمهوری اسلامی در همین زمان از سوی تلویزیون حکومتی متوقف شد.
رئیس‌جمهور آمریکا روز دوشنبه اول تیرماه در گفت‌وگو با خبرنگاران در کاخ سفید در مورد آزادسازی دارایی‌های ایران که در تفاهمنامه جدید به آن اشاره شده، گفته بود:
پولی که آزاد می‌شود قرار است برای خرید مواد غذایی استفاده شود... آن هم صرفاً از طریق ایالات متحده و از کشاورزان ما.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/76767" target="_blank">📅 18:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76765">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FQzJjhExjnSXTBzEHMNF4VodEBrnRoFamuNrZqNJawqAagVAvfoicYuYkXYO74WeVrNaH5fuJOORPwVd8c_S4aZDPxSHoOu4K7HQuZQQqWiOv8QFndhei32UubyiUoTLH9sPqo1QM2NVzTEKYV7d5i52Nu59MlKe4E9gXefY-_D7rsxfKVQPLBd0-pe751i-m54KeCKZjehRlngKBihYSrgM2eyHT1fCcRWLxyI72WEFrQ1-so3Kc_vl9CozgWDpJRwFUAL688zH6uBh93izLmyKZVPDvZwQzMhPsC320DIuw7sPXEjjehds0xs4b0ghegOmw6oXzl_gXSn82lV-Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iGIaxlJM3E1ckB0a2dtdKljLFn5HmGddZogf_MTSoohffovQ0X1ujMVR1MXW1rRpqPj3g13xJcln4yz8YWfXY_v2_fQxcavbD7QnLcT66frzdW_L-E3nUvPTCgoi-kqnGUx8QtrxLLMuNhYzrCRSBzIRWTdSVH43y2tJ6H-UBIAB3HEpiGtfo8fo6Ilejkotp-aIVy1QWr9D-s3iaCdS7eyxftCM-kz9KOu8HsO-X1AMqbRhX5dC5thMwoB-tyEyvKpUvxXExrOrKChhSUGJZuhJZZaylucXbYPYroCNEWQkftiAZw9XUJded23SlHwsrYIZbeKSH4zw4oyPbdVvQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس‌جمهور آمریکا روز چهارشنبه ۱۰ تیرماه از روند مذاکرات ابراز رضایت کرد و گفت این روند «بسیار خوب» پیش می‌رود.
دونالد ترامپ که در واشینگتن با خبرنگاران صحبت می‌کرد، افزود که آمریکا چند روز پیش حملات شدیدی به ایران انجام داد، اما نشست‌های اخیر دو طرف در قطر به‌خوبی برگزار شده است.
او همچنین اعلام کرد: «روند خلع‌سلاح هسته‌ای ایران به‌خوبی در حال پیشرفت است».
ترامپ افزود: «آن‌ها نشست‌های بسیار خوبی داشته‌اند و باید ببینیم چه خواهد شد».
این اظهارنظر ساعاتی پس از آن بود که رسانه‌ها از برگزاری «مذاکرات فنی» غیرمستقیم ایران و آمریکا در روز چهارشنبه در دوحه، پایتخت قطر، خبر دادند.
این مذاکرات با میانجی‌گری پاکستان و قطر برای اجرای تفاهم‌نامهٔ اخیر میان ایران و آمریکا انجام می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/76765" target="_blank">📅 17:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76763">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PAme27JIyDAId6poWpuphbQtZwZdW6p5eJ6QwQUE674WtrCASVWT60qBkOGxOIQGlp7dP8uok0L7t-geeMryhXv4FiZzC3XL7uRwYl3IUV2wszg1ndSQu3C5RJaJ44l_SnovLjyc6fKUhlueSJOzEe3A7OapgWJRqHkdG9isiL2RBmCSeNhNjQoPeook-4-pRzjSN5Mx_Qc_rbo7kaMkq5wazTfCX0IBYtmwqmu1Jxy6Wc-AGMUefLYgQnZcRJcC1DNDDSBaS8ORUzY56mW5CiyDMpsq37dk2q4Mf6WYH7GvQWAJioTUzqByDvKd28cInk9fyp_wRwW8gufAWwDJSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sioKjFLtau9UcTahD7rMDTKnUJi0GyxiK4SIoUqVVjKCI5Wo6rwSJIG8mZJ8spwOEpmzb3SFXznpZDx76C2QFVnMbNoLo-VWQlNtMqYSF8RMltB_R4Y5LimGtxi0bzFMakqeNdOaHAXR4HHpd5L2suzDVzl6syvpzkZ7cYNUj7hysD_tTxvsLNXIzUP0QbGz9dyzCD-W7Gf0FzP1ckdMmNfz_rp9NCSV-n2vBrmkdymRxrtvB8e8rkgrEhMUStUDEL9cb4Tr82UP86ynTu1xm_Jtokpz5JGKjjSpHFxcXnQa0KB4ZPH8oNXZN-9Wk5_pIEQt2PJEVRzR2RAeKc8U0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معاون وزیر خارجه جمهوری اسلامی که برای شرکت در نشست‌های مرتبط با اجرای تفاهم‌نامه ایران و آمریکا به دوحه سفر کرده است، اعلام کرد کارگروه‌های پیگیری اجرای تفاهم‌نامه و نیز مذاکره برای دستیابی به توافق نهایی تشکیل شده‌ اما هنوز مذاکرات در این قالب آغاز نشده است.
کاظم غریب‌آبادی بعدازظهر چهارشنبه دهم تیرماه، پس از دیدار با شیخ محمد بن عبدالرحمن آل ثانی، نخست‌وزیر و وزیر خارجه قطر، به خبرنگاران گفت رایزنی‌ها برای تعیین زمان و محل آغاز مذاکرات از طریق میانجی‌‌ها ادامه دارد و در صورت فراهم شدن شرایط لازم، این گفت‌وگوها آغاز خواهد شد.
به گزارش خبرگزاری ایسنا، پس از این دیدار نیز نشست سه‌جانبهٔ مذاکره‌کنندگان ارشد ایران، قطر و پاکستان برای بررسی روند اجرای تفاهم‌نامه برگزار شد.
@
VahidHeadline
دیوان امیری قطر چهارشنبه در بیانیه‌ای اعلام کرد تمیم بن حمد آل ثانی، امیر قطر، در کاخ لوسیل با استیو ویتکاف و جرد کوشنر، فرستادگان آمریکا، دیدار کرد.
در این دیدار، آخرین تحولات منطقه، به‌ویژه روند مذاکرات میان آمریکا و جمهوری اسلامی در چارچوب یادداشت تفاهم دو طرف، و همچنین وضعیت لبنان بررسی شد. دو طرف بر اهمیت تثبیت آتش‌بس به‌گونه‌ای که وحدت، حاکمیت و ثبات لبنان حفظ شود، تاکید کردند.
در این بیانیه آمده است که امیر قطر بر ادامه تلاش‌های میانجی‌گرانه این کشور با مشارکت پاکستان و حمایت از همه مسیرهای گفت‌وگوهای ناشی از یادداشت تفاهم تا دستیابی به توافقی جامع و پایدار که امنیت منطقه و صلح بین‌المللی را تقویت کند، تاکید کرد.
دو فرستاده آمریکایی نیز از نقش قطر و پاکستان در پیشبرد مذاکرات و نزدیک کردن دیدگاه‌ها قدردانی کردند و بر تعهد آمریکا به ادامه روند مذاکرات و تلاش‌های دیپلماتیک برای دستیابی به توافقی جامع تاکید کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/76763" target="_blank">📅 17:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76762">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GTBj7g0jVlnLRt5Wk22R94KJ64zhVPaIqDrwMzFpb3oAzBQJ2RdV4kIgCoAUISl0Cbm9SxBlE6zWjp8YSaHHR0-BXy6CHBQgIR07jq5_ZN80REXlu1k4eDI1BxyFQm-vBRgvxhUMdn0kxvfvx998I7l8uCT-ljUXvuKMDT3B2rOtyruSqSBXlcB50cKN4xD5MXYjyYSaCrYBkHHoFmzMTZKxzLGsVfSYIW-_e63aLEozi3_YDXPyCylIKkOvOHgrzbk5ePPnS0s4MwIKTuuDMKai3PPyqVIuw50KuZ9wR_g6sZmqAWZMJCEY9dhwGH3sk7WsfJds_4uKnlE4njJ7tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌زمان با ادامه برخوردهای قضایی و امنیتی با فعالان صنفی فرهنگیان، سه معلم  با احکام زندان و مجازات‌های تکمیلی روبه‌رو شدند و یک فعال صنفی دیگر نیز در استان فارس بازداشت شد.
بر اساس گزارش شورای هماهنگی تشکل‌های صنفی فرهنگیان ایران، احمد علیزاده، معلم بازنشسته و فعال مدنی اهل آبدانان، از سوی دادگاه انقلاب ایلام به دو سال حبس تعزیری، یک سال ممنوعیت خروج از کشور، ابطال گذرنامه و یک‌هزار و ۸۰ ساعت خدمات عمومی رایگان محکوم شده است.
هم‌زمان، آزاده سالکی، معلم شاغل در شهرستان خواف و از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، به پنج سال حبس محکوم شده است. بر اساس خبر منتشر شده، حکم اولیه او ۱۰ سال زندان بود که در مرحله تجدیدنظر به پنج سال کاهش یافت.
آزاده سالکی پس از بازداشت در دی‌ماه ۱۴۰۴، حدود یک ماه در بازداشت به سر برد و سپس با تودیع وثیقه سه میلیارد تومانی به‌طور موقت آزاد شد. گزارش‌ها همچنین حاکی است اجرای این حکم می‌تواند به اخراج او از آموزش و پرورش منجر شود.
این معلم پیش‌تر نیز در سال ۱۴۰۱، زمانی که در شهرستان تربت حیدریه مشغول تدریس بود، به دلیل فعالیت‌های صنفی و اظهاراتش در کلاس درس، به مدت یک ماه از کار تعلیق و سپس به شهرستان خواف منتقل شده بود.
همچنین جان‌محمد احمدی، معلم بازنشسته و رییس انجمن صنفی معلمان نورآباد ممسنی، روز سه‌شنبه ۹ تیرماه توسط نیروهای امنیتی بازداشت شد. تاکنون اطلاعاتی درباره محل نگهداری، نهاد بازداشت‌کننده یا اتهام‌های منتسب به او منتشر نشده است.
آریا نورانی، معلم رسمی آموزش و پرورش در شهرستان مانه خراسان شمالی، نیز در ارتباط با اعتراضات دی‌ماه ۱۴۰۴ به ۱۴ ماه حبس محکوم شد.
شورای هماهنگی تشکل‌های صنفی فرهنگیان ایران با محکوم کردن این اقدامات، خواستار آزادی بازداشت‌شدگان، لغو احکام صادرشده و پایان دادن به برخوردهای قضایی و امنیتی با فعالان صنفی شده است.
در ماه‌های اخیر نیز روند برخورد با فعالان صنفی معلمان تشدید شده است. پیش‌تر شعبه سوم دادگاه انقلاب اهواز پنج فعال صنفی فرهنگی و کارگری خوزستان را به سه سال حبس تعلیقی و دو سال ممنوع‌الخروجی محکوم کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/76762" target="_blank">📅 17:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76761">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SyzG62dHwhesVTG5eFvVLWPtgOyBBflSat7Om3-sg7kY10Xdet8WEII83tsVOwwcQQ-Zh5U7HInoNjPiMyVVpKFqNagx1EXYHxx7VBALutbOW8L5JtmWo5kna6hmGqKo72DkOY78ifnAexuIcW0DIaqpRNYiEZMiMURL0U7pEo-fRX4kc2gWB3aNSiQ1oFQRM9jHuJsEZZqzCd-JZL5DjmghVJPKGxTmRKNmlERjDRygGpdHKFXlfYONT9DvKN42BrZgXPfT6rm517ew-fsRWS59OoiUFiPQnTsPHKqZOZfBG9VEBVs5s2gLNsrxaDHr8THh_QbWFv3H1NNLLHr3qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس، معاون رییس‌جمهور آمریکا با انتقاد از منتقدان که خواهان حملات بیشتر به جمهوری اسلامی هستند، در یک برنامه تلویزیونی گفت: «دیدگاه آن‌ها این است که فقط بمب بریزید، باز هم بمب بریزید؛ اما واقعا نمی‌توانند توضیح دهند که هدف نهایی از این کار چیست.»
او افزود: «اما چیزی که رییس‌جمهور [ترامپ] می‌گوید این است حاضرم دستور حملات هوایی بدهم، و به‌وضوح هم نشان داده که در صورت لزوم این کار را انجام می‌دهد، اما فقط زمانی که این اقدام در راستای دستیابی به یک هدف مشخص باشد.»
او در بخش دیگری از اظهاراتش گفت: «یکی از چیزهایی که درباره ایرانی‌ها برایم هم جالب و هم آزاردهنده است این است که می‌گویند نه، هیچ گفت‌وگوی صلحی در جریان نیست، اما در همان حال مذاکرات فنی میان واشینگتن و تهران درباره توافق صلح در حال انجام است. این یک تاکتیک مذاکره یا شگرد ایرانی است که من آن را درک نمی‌کنم.»
@
VahidOOnLine
جی‌دی ونس، معاون اول رئیس‌جمهور آمریکا در مصاحبه‌ای با شبکه خبری فاکس گفته است «ایالات متحده در رابطه با ایران در موقعیت بسیار خوبی قرار دارد.»
او گفت: «ایرانی‌ها در هفته‌های گذشته، هیچ نفت‌کشی را هدف قرار ندادند و جریان نفت در تنگه هرمز برقرار است؛ بخشی از آن به این دلیل که رئیس‌جمهور(ترامپ) تصریح کرد که اگر ایرانی‌ها به کشتی‌ها حمله کنند ما مقابله به مثل می‌کنیم.»
آقای ونس همچنین گفت: «اگر مذاکرات موفقیت‌آمیز باشد که ما می‌خواهیم موفقیت‌آمیز باشد، شما ایرانی را خواهید دید که بطور دائمی متحول شده؛ تروریسم منطقه‌ای و بی‌ثباتی را تامین مالی نمی‌کند و جاه‌طلبی‌های هسته‌ای را بطور دائمی کنار می‌گذارد و درنتیجه اقتصاد جهانی دوباره از آن استقبال می‌کند. این نتیجه خوبی برای مردم آمریکا و کل منطقه است.»
او همچنین گفت:«از سوی دیگر اگر آنها رفتار مناسبی نداشته باشند و امتیازاتی را که ما می‌خواهیم ببینیم ندهند، هنوز برنامه هسته‌ای آنها نابود شده، توان متعارف نظامی نابود شده و آمریکا در مقایسه با آنها در وضعیت قوی‌تریست.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/76761" target="_blank">📅 01:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76759">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/150c916f8f.mp4?token=h6E_UkioTuW2LhMXC0yxh8-OwOEBV8e32x8ONvUtwW7WriXqUD9ppD25KHu5zmRlVnyq58h9jew-5mxZ--oh6pdTpWRtJRYuCBhWVjvpa_FWIZW6tnNrkeqDYY2_icdMjLjGEV25XKikecu88_g1KiwZkIL8c13BbkKoreHGI7mSQozByabPKK2aNtewOkv3gDQQUqcqfk2XpBdgfn6nQ2JzeyVjVeGXt_NZV_eVv6NnKdD5JHLb7KoU1a2lP4IcPOt6v9IQqxPQlhaguepQk1NFtnXup6Z9BvbjInEnyqXxiZsTw5lIWGR8uRtlP2A_SeK2XWfx9TLqHtOG5o_kEg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/150c916f8f.mp4?token=h6E_UkioTuW2LhMXC0yxh8-OwOEBV8e32x8ONvUtwW7WriXqUD9ppD25KHu5zmRlVnyq58h9jew-5mxZ--oh6pdTpWRtJRYuCBhWVjvpa_FWIZW6tnNrkeqDYY2_icdMjLjGEV25XKikecu88_g1KiwZkIL8c13BbkKoreHGI7mSQozByabPKK2aNtewOkv3gDQQUqcqfk2XpBdgfn6nQ2JzeyVjVeGXt_NZV_eVv6NnKdD5JHLb7KoU1a2lP4IcPOt6v9IQqxPQlhaguepQk1NFtnXup6Z9BvbjInEnyqXxiZsTw5lIWGR8uRtlP2A_SeK2XWfx9TLqHtOG5o_kEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، مذاکره‌کننده ارشد جمهوری اسلامی، شامگاه سه‌شنبه اعلام کرد در حال حاضر «اصلا مذاکره‌ای با آمریکا نداریم».
او در گفت‌وگویی با تلویزیون حکومتی ایران محاصره دریایی آمریکا علیه بنادر ایران را که بعد از آتش‌بس و از فروردین‌ماه آغاز شد، «شدیدترین نوع جنگ» خواند که به گفته او «مردم و نان مردم» را محاصره کرده بود.
قالیباف افزود که برداشته شدن این محاصره «از موفقیت‌های بزرگ» تفاهم‌نامه امضا شده بین ایران و آمریکا بود.
او اعلام کرد که مذاکرات فقط تا زمان امضای یادداشت تفاهم ادامه داشت و سفر به سوئیس برای گفت‌وگو درباره «اجرای بندهای» همین تفاهم‌نامه بود که ۲۵ خرداد بین ایران و آمریکا امضا شد.
@
VahidHeadline
قالیباف با طرح ادعای تسلط ایران بر تنگه هرمز در پی جنگ ۴۰ روزه هشدار داد که «نباید تنگه را به ضد خودش تبدیل کنیم».
او افزود: «تنگه هرمز زمانی ارزشمند است که روز‌به‌روز تردد در آن بیشتر شود، نه کمتر.»
@
VahidHeadline
پس از  آن که مصاحبه تلویزیونی محمدباقر قالیباف درباره جنگ، تنگه هرمز و مذاکرات با آمریکا، در میانه آن به طور ناگهانی قطع شد، مرکز رسانه‌ای مجلس شورای اسلامی اطلاعیه‌ای به رسانه‌های داخل این کشور فرستاده و به این موضوع اعتراض کرده است.
در اطلاعیه مرکز رسانه‌ای مجلس آمده است: «به اطلاع هم‌وطنان عزیز می‌رساند در راستای اجرای امر رهبری معظم انقلاب مبنی بر پیگیری شروط مشخص شده در یادداشت تفاهم اسلام آباد، جناب آقای دکتر قالیباف، رئیس قوه مقننه و رئیس هیئت مذاکره‌کننده کشورمان برای ارائه گزارش به مردم، گفتگویی تبیینی را طبق هماهنگی با سازمان صداوسیما انجام دادند که این گفتگو بیش از ۲ ساعت قبل از زمان پخش به آن سازمان تحویل داده شد؛ اما متاسفانه پخش این گفتگو از میانه آن متوقف شد».
در ادامه این اطلاعیه امده است: «این در حالی است که این گفتگو به شکل ضبطی بوده و کمترین وظیفه مسئولین سازمان صداوسیما این بود که اگر خلاف رویه ها تصمیم به عدم پخش بخشی از گفتگو داشتند، آن را با این مرکز هماهنگ می کردند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/76759" target="_blank">📅 00:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76758">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6iB8ODVi2llMnlMbu5C7JBkphLDGgtW3NSUnCVDUfijk2a-HqnQtKrPzC5ItmxJhgbWOlc0qdOJhyRH7ZUEHZ8Ma44ok7vZ68GNTNy5cBquhVXXfyzmI0NDcIM0DSZ0FRQW2T6wC6zdWWzrII3fU02wIMptXeUtw6XeKA2J75HPBESah5pt_sQwAAxrjsyluPaGj4R4Uf4purFzfRdXvPrbOFRf17bd7VkQZkssQRdQnlIwvnXaFeoBMD6UnK_te9e4ACVayvolOr0DIF4IGPTSGFk33Xf1g3MzRcf3nP-wBam0DvcpAhBY4vX2cEkGc4XG1SZnb2zbrgnOpKEI6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌دیوان عالی آمریکا تلاش دونالد ترامپ، رئیس جمهور، برای لغو اعطای خودکار تابعیت به کودکانی که از والدین مهاجر فاقد مدارک قانونی در خاک آمریکا متولد می‌شوند را رد کرد.
آقای ترامپ و تیم حقوقی او تفسیری از قانون را درخصوص این اعطای تابعیت مطرح کرده بودند که تا همین اواخر هم در میان سیاست‌گذاران و کارشناسان حقوقی، حمایت چندانی نداشت وتوانستند آن را دیوان عالی آمریکا یعنی عالی‌ترین مرجع قضایی کشور برسانند.
با این حال، در نهایت اکثریت ۹ قاضی دیوان عالی حاضر نشدند سابقه قضایی ۱۵۰ ساله را کنار بگذارند و یا قوانین فدرال دیرینه و متن قانون اساسی آمریکا را به گونه‌ای جدید تفسیر کنند تا به نفع آقای ترامپ رأی صادر شود.
این شکست احتمالا برای آقای ترامپ ناامیدکننده خواهد بود و او را وادار می‌کند به دنبال راه‌های دیگری برای محدود کردن ورود مهاجران فاقد مدارک قانونی به آمریکا باشد؛ زیرا اگر این افراد هرگز به خاک آمریکا نرسند، موضوع اعطای تابعیت به فرزندانشان نیز اساسا مطرح نخواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/76758" target="_blank">📅 21:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76757">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSAjIjIkqDt0ereXvvG38ssDeMEZwW-NPaWcP3tx_XgA6vA3fMBZRoYV60MQvus2GMl-d2b4m1q-eESHKqfsEdchzGtn35JyvXBNT-hyGLIPPjircLnTwPErfPxZk06zEToGgkso5Xgv7IIUP0F49DQB-xMqxXzdkron9BfSboz11nEDGBhshh57YrCZyYq-dJZE9t-46HcsBkiV5ByN_uJXIvqnAmZppVIY-G91NqZdJh3Dgg1lPldu_iES0g6jTdpHKFPBwk-JBMWKofocC7QloTfdWY8qwj5QJQ2MPVO5qEEYYRcSevAu8ifttXHElqf8udRs3bUPq_bZvcI_0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه قطر، اعلام کرد استیو ویتکاف، فرستاده ویژه دونالد ترامپ در امور خاورمیانه، و جرد کوشنر، مشاور ارشد و داماد رییس‌جمهور آمریکا، روز سه‌شنبه برای گفت‌وگو با مقام‌ها و میانجی‌های قطری وارد دوحه شده‌اند.
ماجد الانصاری، سخنگوی وزارت خارجه قطر، گفت این دیدارها با هدف بررسی «تمامی مسائل منطقه‌ای» انجام می‌شود و موضوعاتی از جمله روند مذاکرات با ایران و همچنین لبنان را در بر می‌گیرد.
او با این حال تاکید کرد که ویتکاف و کوشنر برای مذاکره با هیات ایرانی به دوحه سفر نکرده‌اند و برنامه‌ای برای دیدار با نمایندگان تهران ندارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/76757" target="_blank">📅 19:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76756">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BajLqfC5_3_wnLdzzA8ogk6CpaA2A-bY9HxyLfHyX-sj0hU3WUOykfEpFAEjVRXPVPxytbRPC7TYW0dTvd_tDC8d5w_76PO2GEPbzbOtan7H9kSrexe2oSTMoWj6rKU7_fms2j_zClo0OkmG1uLMiIQfI2fptNi_Q_vn8M1PzrsHTcfh9qmLklM_JpiAuW2svrBD6dKKAiVufeaJx_Yr8JVWM0kS0RwBPMXkfF--ne4YAoyREdDIUd1thXkY0OSjHKf6xuZoCUFIuuWsmzOuxf5PhrTdzegkPFY6vqTvuhV8Uhm4fQnoIDuvM9MwfXu0A9NhDofzvp7JNi_rgH01dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العربیه به نقل از چند منبع گزارش داد جمهوری اسلامی تا پایان هفته ۳ میلیارد دلار از دارایی‌های مسدودشده خود را دریافت خواهد کرد.
پیش‌تر سخنگوی وزارت خارجه قطر گفت تاکنون ۶ میلیارد دلار از دارایی‌های مسدودشده جمهوری اسلامی به ایران منتقل نشده است.
محمدجعفر قائم‌پناه، معاون اجرایی مسعود پزشکیان، نیز با اشاره به متن تفاهم‌نامه با آمریکا، گفت که چند میلیارد دلار به حساب جمهوری اسلامی در یکی از کشورهای خلیج فارس نشسته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/76756" target="_blank">📅 19:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76754">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lUxsiBNNrBrEH_CmpZwrT54vg4akis-6eiJyXtjpf8tXEAbvhO3Lx4Zt1GfTwWMzSQJPSJy9ZsCNTkl96euPKGlB3I-P1tXFF8ndE_c6edTZKQViKA96djKQpL6YMpSmUa23DSLsSxdz2_dZkz7NMTT1hKNkojFwmKgSwrVqmJXTG7OLylaTrevWA9J59umxbx_dZuVrt_wysVokrfGmkiQOZFdPHcgGrFlw7UwOjqMROwdm_CDwLZakCOdr5PgaYQQJC-X8yQXzdi4hDZW3HLqIrj4yIMDzDy0B_Bv5eO1xxnWI3w1XF14Djg0H8ivjMJi0NLUpmMt0giuJ80t6qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jRXbFDrGwXr4ZL-_3h7Xs3f5sAOc5R8dgYf3baDf3nv0WXDeI2CHAAY8kXoDXNCeI7yIpMxSto8xnsQqHa6Vtek8BOXOKZcH-uGccezBkCxKFSzc_NgO8wPNGZjPNEI4gf6DGngziM_TUAXyA7sGacrLZHrc5fg7ton4eJB2Z5ELktmztyg9BHuJlThXI8pRlGgTz8nr9WiAyycl1UyZL9MnMP6BFzEHQRORJbMGNp736On2sV5I9E_s21maAYa3hWOlQVgR80kR8owZ358hlrDq5Q_9FZXkijK3EehKMygBfPIj9_8z2DsR3jPHPQePbS0rXSLFuL_QkSDEn_7RPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معاون اجرایی مسعود پزشکیان تأیید کرد که فرماندهان نظامی عضو شورای عالی امنیت ملی ایران و دو نمایندهٔ رهبر جمهوری اسلامی در این شورا نیز به تفاهم‌نامهٔ ایران و آمریکا رأی مثبت داده‌اند.
محمدجعفر قائم‌پناه روز سه‌شنبه نهم تیرماه اعلام کرد در جلسهٔ‌ شعام برای بررسی این تفاهم‌نامه، رئیس‌جمهور، رؤسای مجلس و قوه قضائیه، جانشین رئیس ستاد کل نیروهای مسلح، وزیر کشور، رئیس سازمان برنامه و بودجه، وزیر خارجه، فرمانده کل سپاه پاسداران، فرمانده ارتش، و دو نماینده رهبر جمهوری اسلامی در شورا،
یعنی سعید جلیلی و محمدباقر ذوالقدر، به این توافق رأی مثبت دادند.
او این را هم تأیید کرد که مجتبی خامنه‌ای، رهبر جمهوری اسلامی، دستور داده بود جلسهٔ شورای عالی امنیت ملی با حضور فرماندهان ارشد نظامی برگزار شود و در صورت رأی موافق سه‌چهارم اعضا تفاهم‌نامه پذیرفته شود.
اظهارات معاون اجرایی رئیس‌جمهور در حالی مطرح می‌شود که در روزهای گذشته، پس از انتشار پیام مکتوب مجتبی خامنه‌ای دربارهٔ تفاهم‌نامه، برخی چهره‌های مخالف مذاکرات از سعید جلیلی به‌عنوان «تنها مخالف» تفاهم‌نامه نام برده بودند.
@
VahidHeadline
به گفته معاون اجرایی رییس‌جمهوری، اعضای موافق این تفاهم عبارت بودند از: مسعود پزشکیان، رییس‌جمهوری، محمدباقر قالیباف، رییس مجلس، غلامحسین محسنی اژه‌ای، رییس قوه قضاییه، رییس ستاد کل نیروهای مسلح (که نام او پس از کشته شدن عبدالرحیم موسوی هنوز به‌طور رسمی اعلام نشده است)، اسکندر مومنی، وزیر کشور، حمید پورمحمدی، رییس سازمان برنامه و بودجه، عباس عراقچی، وزیر امور خارجه، فرمانده کل سپاه پاسداران (که نام او نیز تاکنون به‌طور رسمی اعلام نشده)، امیر حاتمی، فرمانده کل ارتش و دو نماینده رهبر جمهوری اسلامی در شورای عالی امنیت ملی.
قائم‌پناه همچنین از منتقدان داخلی تفاهم‌نامه انتقاد کرد و گفت کسانی که به این توافق رای مثبت داده‌اند، «کمتر از فرماندهان شهید نیستند» و نباید جایگاه یا صلاحیت آنان زیر سؤال برود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/76754" target="_blank">📅 16:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76753">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpGzxTWLGGifmPK5CiaGinrrv8ceW3Y3V3ymBWQxwB_B44m4BRto2ih41EAfcZZCDzqLarfmnTNr88OIriJYbDxKxE6E1CnV53_zrjTwwn7RaoupPme5gIOZGZBM1bryJpk1FwUHX_aggqxdskHODNpyrqaNVeEZ9ukEdxsmdTzBpU8y8PtC0xDHavODIYXU3N-rJV8Velp6fJDdlN4uuNmBVAIQgdXdt_2tzVsqG1sPp76GH4JSe9rJ_6axcQxDWX01LmnqkRoYd_8aDZQ32e89SCfAGDZDDAA7Avdw5g5W0SuAAJf_Z8zF04KcHDyeSRqjQzV080EpOoaWdAnRIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این تصویر، محمدرضا شاه پهلوی در جریان بازدید از بانک ملی ایران، با یوسف خوش‌کیش، رئیس وقت بانک ملی، گفت‌وگو می‌کند.
خوش‌کیش بعدها ریاست بانک مرکزی ایران را عهده‌دار شد و آخرین رئیس‌کل بانک مرکزی پیش از انقلاب ۱۳۵۷ بود.
پس از انقلاب، خوش کیش بازداشت شد و تنها طی سه روز محاکمه، با اتهاماتی از جمله «ثابت نگه داشتن ارزش ریال در برابر دلار آمریکا به مدت پنج سال»، به اعدام محکوم شد و بامداد ۲۴ مرداد ۱۳۵۹ تیرباران گردید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/76753" target="_blank">📅 16:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76752">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQuLWnwX_pX0MUt3huzvFTXsIao1XN920SwuB1C1IzPfLQlOhquKBelLoTYxvZwyxBsAivWvbVVUPi-MXk5Xx7Zqt8ut4obTgAFPFdIRSVfH1xmK8MCi-B1sT-EiZ7UXRinUou5BcuYhPhZIWnX6vWR1RENjfW0kUquGiWC9EiIk6w1hjYcbU66pxzozhsMiOkmeWO78Yc3B-dkrkVTeQ2Afn4XgSEeliR0nRx6xCK6X1UCZS9DZDs-sDxDWMt4LUfXsfqhEB4T3BE4vEyhh3fu-rq2CEBRuajXUvAcoU9gYIUQ6ajal2wbM8ZLKJDsKHN-QNYD_QRTzJW0t2rv3Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان مخالفان داخلی تفاهم‌نامهٔ ایران و آمریکا را به «همسویی با عملیات رسانه‌های معاند» متهم کرد و گفت «تمامی مراحل مذاکرات» با «هماهنگی کامل و مستمر» با رهبر جمهوری اسلامی انجام شده است.
رئیس‌جمهور ایران که روز سه‌شنبه ۹ تیر در دیدار با اعضای جامعه مدرسین حوزه علمیه قم همچنین گفت: «با وجود محدودیت‌ها و ملاحظات امنیتی موجود، متن نهایی توافق پس از بررسی‌های کارشناسی و امنیتی در مراجع ذی‌صلاح مورد ارزیابی قرار گرفت و در شورای عالی امنیت ملی نیز از حمایت قاطع اعضا برخوردار شد.»
این در حالی است که در روزهای اخیر مخالفت برخی طیف‌های سیاسی طرفدار حکومت با تفاهم‌نامه بالا گرفته و می‌گویند دولت، محمدباقر قالیباف، رئیس هیئت مذاکره‌کنندگان، و حتی برخی فرماندهان ارشد سپاه برخلاف نظر مجتبی خامنه‌ای این تفاهم‌نامه را تصویب کرده و پیش برده‌اند.
مسعود پزشکیان این دسته از مخالفان «جریان‌های همسو با عملیات روانی رسانه‌ّای معاند» خواند و گفت: «این‌ها تلاش می‌کنند با تخریب تیم مذاکره‌کننده و زیر سؤال بردن تصمیمات ملی، زمینهٔ تضعیف این دستاورد را فراهم کنند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/76752" target="_blank">📅 16:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76751">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/by4U2hgO4LApkxuFfs2o1hp3y8W_NQCcgcJ6NgpaXqLYkdChlBmOnF6iPErLyWGr2IGfXVNHc4A66bedVZrOHakOS41CkKSUosOE-FilsdBqt1ZhcVX67ALxglxN-gIlTst4cIPwqV2ma25MtfVwAxcFhpF3tCJmZeJM-ffS_GIrkKwTQyK3-Z-v5kp9bP8KM5RU9dOyjumhKo3yaCY4JYi4oSvwbdDNQe_-UzE0GHSY-9Qu6HL29pkowY2v1RBIDSENxdJT2wC_9HAdbI1-nHbNSAa6p5-Hrzr9k5d8RtkyPqQgJblZ4v1pR1NTQCp7FL3hg9MG57q_ojMkF09Qaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از ۱۴ روز از آغاز اختلال در شبکه خدمات برخی از بانک‌های کشور از جمله بانک‌های صادرات، تجارت، ملی و توسعه صادرات می‌گذرد؛ اختلالی که همچنان به‌طور کامل برطرف نشده و ارائه خدمات بانکی را با مشکل مواجه کرده است.
در این مدت، گزارش‌های مردمی از تداوم کندی، قطعی و ناپایداری سامانه‌های بانکی حکایت دارد؛ این در حالی است که مسئولان بانکی در روزهای گذشته بارها از رفع یا در آستانه رفع بودن مشکل خبر داده بودند.
ادامه این وضعیت موجب بروز اختلال در انجام تراکنش‌های روزمره از جمله انتقال وجه، دریافت حقوق و پرداخت اقساط برای بسیاری از شهروندان شده است.
هم‌زمان، کسب‌وکارهای خرد و متوسط نیز با مشکلاتی در دریافت مطالبات و انجام پرداخت‌ها مواجه شده‌اند؛ موضوعی که به گفته فعالان اقتصادی، بر روند فعالیت روزانه آن‌ها تأثیر گذاشته است.
در همین ارتباط، محمدرضا عارف، معاون اول رییس جمهوری، در جلسه‌ای با مدیران بانکی با اشاره به اختلال‌های اخیر گفت: «آنچه در بانک‌ها رخ داد نتیجه سهل‌انگاری در حوزه امنیت سایبری است و این موضوع قابل پیش‌بینی بود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/76751" target="_blank">📅 16:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76750">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FHLkjKY_W1wHxLI-bsqxOA7XRQgv0TcMx5pHBFZCDorgT0uZ2642kioYcNOpDCWGPUbRHngw1VWHKeXB7ll29oSTdYa81QhRmIwBasftJktlRhEMtN4BfUh1T1wuRvONXzd2lmEYITnAPwoYkVLHyFocI83Dks0Y4fhy0mmz9jsZfNous0mXrmMqPibqmQ6GFTWlxZDae2YxYmhZ3Dk8NZI3P0HDVomT7KZVyoNNiKNQ4rj2apSEiuupAX1T4jL-XV0_FOPXFRn1hQUStYz_eHcpAdW1LfIN1GtNe44B7zxRpLhbAf0tj7fRFZRg5Y4XjXF2aYYNpCIQ4YhzX5Qqfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضوانه احمدخان‌بیگی، فعال مدنی، جهت تحمل ادامه دوران محکومیت حبس، به همراه فرزند خردسال خود راهی زندان اوین شد.
براساس اطلاعات دریافتی هرانا، رضوانه احمدخان‌ بیگی، دوشنبه ۸ تیرماه، به همراه دختر خردسالش، مهفر لاله‌زاری که زیر دو سال سن دارد، برای تحمل ادامه دوران محکومیت حبس خود راهی زندان اوین شد.
این زندانی سیاسی در تاریخ ۲۸ شهریور ۱۴۰۳ جهت زایمان از زندان اوین به مرخصی اعزام شده بود.
رضوانه احمدخان بیگی و همسرش بهفر لاله زاری در دی ماه ۱۴۰۲ به اتهام اجتماع و تبانی علیه امنیت داخلی و تبلیغ علیه نظام به ۱۰ سال زندان محکوم شدند. این حکم در اسفندماه همان سال تأیید شد و بعد از پذیرش اعاده دادرسی و رسیدگی در شعبه هم عرض به ۲۱ ماه حبس کاهش یافت.
hra_news
فرحناز نیکخو، نیره بهنود، میترا برمچ و زهرا (هانا) غلامی، چهار زندانی سیاسی، پس از پایان دوران مرخصی خود به زندان اوین بازگشتند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/76750" target="_blank">📅 16:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76749">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LIza_iRWVnifstg_yjvx7n7EBnlBeAY6-SMQwF9RPSPCRY3ptrbsW56QKbTcYVhQZ61noZD3XRj1k5lMAEvgEP1fZ1YvGIe8PBKuRl4wl94n3mo6CtvVouC6CFWVVOYh3c9AA6TpXP2zV6r9MikNRCI9pA8GMCztLagTo5wJSFCHjyL-n5r2GVQAYaiiB2maZzYiEMCFE4rjVT36DPs9fZf2JT1XZSvd-rXnVh-OZWKJUg6v8t_1sv_5pWKkCgc8DjK58Pq4jQbJ0JdtL114RFMrtOz8WkRJmBVkSylX2frj4BMarn0LcdM0UR9pGTg1aAyj_AiQmb5SG6zV1bxbqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی سپاه استان کرمانشاه اعلام کرد دو تن از نیروهای بومی سپاه در شهرستان پاوه شامگاه دوشنبه در پی تیراندازی افراد مسلح «به درِ منزل‌هایشان» کشته و دو نفر دیگر زخمی شدند.
بر اساس گزارش خبرگزاری مهر به نقل از روابط عمومی سپاه استان کرمانشاه، این حمله مقابل منزل دو تن از نیروهای سپاه در پاوه رخ داده است. در این گزارش، عاملان حمله «افراد مسلح تروریست» معرفی شده‌اند.
منابع رسمی هویت دو عضو کشته‌شده سپاه را برهان کریسانی و خالد خالدی اعلام کرده‌اند.
همزمان، سازمان حقوق بشری هه‌نگاو گزارش داد که این حمله را گروهی تازه‌تأسیس به نام «خوری هیوا» (خورشید امید) بر عهده گرفته است. هه‌نگاو نیز نام دو کشته‌شده را خالد خالدی و برهان کریسانی اعلام کرده و نوشته است دو عضو دیگر سپاه در این حمله به‌شدت زخمی شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/76749" target="_blank">📅 08:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76748">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WiU40u20hA_k449w0GwCFx70i-l3XbT1zJERP7CRdY3680MZynyywCEY-tNvV2sbVchNFI8ZX71ye6VDSyT3aYrb5SkopIcaQxBWJ9eFI5MgfppUf19jq3sySDkrsjxw4hm2M6grCr_EJWNTw-L6S3TMLh1XYhhKyYGtgpxnm1VF9qabXgElUHAFdA4b9uaVWPeLWqhLN5z-D0YkT5ACyEZV9alxZOZKUlyuGZBTsLBM5eINDBTGBFyUI5p79FYfUzigEPkDeawQgHbGww5gxFKwIRAIWV5iRTClAHLHvs7uuQbRcmFn4Z2vRFUDtda42x09DBtNZrGxtYzbPmugnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقائی، سخنگوی وزارت امور خارجه جمهوری اسلامی، روز دوشنبه انجام مذاکره با آمریکا در دوحه را رد کرد و گفت در روزهای آینده هیچ مذاکره‌ای انجام نمی‌شود.
این در حالی است که دونالد ترامپ، رئیس‌جمهور آمریکا، از درخواست ایران برای انجام مذاکره در قطر در روز سه‌شنبه خبر داده و سخنگوی کاخ سفید اعلام کرده استیو ویتکاف و جرد کوشنر به عنوان نمایندگان ایالات متحده عازم قطر می‌شوند.
بقائی در این باره اعلام کرد: «طی روزهای آتی هیچ نشست مذاکراتی در هیچ سطحی با طرف آمریکایی نداریم و این‌که نمایندگان آمریکا به قطر سفر می‌کنند، ارتباطی با سفر هیات ایرانی که برای پیگیری اجرای مفاد یادداشت تفاهم از جمله بند ۱۱ انجام می‌شود ندارد.»
او در ادامه توضیح داد «هیئت کارشناسی» جمهوری اسلامی این هفته برای پیگیری آزادشدن دارایی‌های مسدودشده ایران بر اساس بند ۱۱ تفاهم‌نامه امضا شده میان ایران و آمریکا به قطر می‌‌رود.
ساعاتی پیش مسعود پزشکیان اعلام کرد که «شش میلیارد دلار از مجموع ۱۲ میلیارد دلار منابع ایران در قطر آزاد و به کشور بازگردانده خواهد شد»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/76748" target="_blank">📅 21:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76747">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rAm4QXb1Z_SVCUSnJKH8AenZgMTyYhd7yQaIDNdMp8_HH0THh6mE2rswhTcCkntjA8e8I3L8kZ4KGC3H6zNWD7BFJiEFSn-5s0lv0tnqNHmlAQf74e0L025t9Ols5J-PBoZAZHsDWQs3dvPKfBYSh7RDjWpuBLpfUUvuF_LpRpTxhwI_67ljaxVoZoSEipf4t7yhR_LP42znJh6J6r-LDAKHRy77Tv-vu-vmw-XygNernSXX-S8pLqujauepeG_GaXN4l2ucu2XNPikBhYHdGx3hKR9sV2JWVxVJqUsqlKXJBo30d4SvOUIMZwP1hMcN0nPaBfXSj8tVKF9c0bElRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، گزارش داد محمد اکبرزاده، معاون سیاسی نیروی دریایی سپاه پاسداران، در یک «سانحه رانندگی بر اثر واژگونی خودرو» در یکی از محورهای استان کرمان کشته شد.
فارس نوشت پس از وقوع حادثه، نیروهای پلیس و اورژانس در محل حاضر شدند و اکبرزاده به مرکز درمانی منتقل شد، اما به دلیل شدت جراحات جان باخت.
این رسانه وابسته به سپاه افزود بررسی علت و جزئیات این سانحه از سوی مراجع ذی‌ربط آغاز شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/76747" target="_blank">📅 21:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76746">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CA9J05XCvCCZPeWKtrnCBLS1ovx4xobSHQjEpUeDb1dJEwQf0CrPJVgu376VdnAZ7_TyyvUVe2426_nm3ir1XVwD8NJbktUMhpbz2z32ZI_PMwTnHEgsinp_b3K1Ji0rQC-wHtXi6EfVCUaes-fVAnZGbUjCrOCtLAfYQqOn9Rmw-HI1V79gufFEO2VWTZh2jCHC3v5B9LAVJf1uj_hrUagiiq5mlH023DthyzTUsWENprJ2LNa-aTMEArHROESdYMYm-YvKnbnc7FppXbTLq-8sXi3OwPfr5trJPBCgTGUEjYEebV864tz8ngTJXkHm-fgQEr-g9hcUGuSgLv-3vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوسف میری، ۱۷ ساله شب چهارشنبه سوری در خیابان حافظ اصفهان با اصابت گلوله بسیج به سرش کشته شد.
یوسف میری سه‌شنبه ۲۶ اسفند ۱۴۰۴ هنگامی که در راه بازگشت به خانه بود با مادرش تماس گرفت تا برایش غذا گرم کند اما پیش از آن که به خانه برسد با شلیک گلوله به پشت سرش کشته شد.
یکی از دوستان یوسف به ایران‌وایر می‌گوید: به مادرش گفتند به اشتباه به پسرت شلیک شده و اگر جنازه‌اش را می‌خواهی بهتر است سکوت کنی تا جنازه را تحویل بدهیم.
دوست یوسف همچنین توضیح می‌دهد: مادرش مرتب یک جمله را تکرار می‌کند که بچه‌ام گرسنه و تشنه بود می‌خواست بیاید خانه شام بخورد ولی آن بی‌رحم‌ها نگذاشتند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/76746" target="_blank">📅 17:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76745">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IVP48mqW8ka9VFyd33J3-Px-YpjgkUofcc27sETquz8kjJkB19HW8ZBnkeI-yO2_QJ8SRT4Xv_TMDY8bHegMWlAv8O1FAyBY9AtPHWXLByp1uDQRtEBLGWnrfhG5a3Ln4JGlBuYZClJKVg4GePHPMSxKIwEOzF4Ob5Hen9E4h6zmp4W8Ch-sf-ppSxd54qeS3XfU0IX82gLriCIXACvfgWW1qyAFpHno0ZpXNpIwo2fmoCTDu_bM9Elqkt7B_tTF1wSqV5vjv7Lv06p7T6GxcmAc6u2ZemPP4ITOm4QcRhG-EWI57jDjmVYcCcg_VLPUlZtYBo-5HGwjDsM6RXiHgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدر البوسعیدی، وزیر امور خارجه عمان، روز دوشنبه در گفتگو با رادیو مونته‌کارلو بین‌المللی اعلام کرد که این کشور به آزادی عبور و مرور در تنگه هرمز و اعمال نکردن هرگونه «عوارض تردد» متعهد است. او تاکید کرد که اعمال چنین هزینه‌هایی به‌طور بین‌المللی ممنوع است و عمان به این مقررات پایبند باقی می‌ماند.
این اظهارات در حالی مطرح می‌شود که ایران نیز از برگزاری جلساتی میان مقامات تهران و مسقط برای بحث در مورد مدیریت آینده این آبراه، طبق مفاد یادداشت تفاهم ایران و آمریکا خبر داده است. با این حال، گزارش‌ها حاکی از آن است که دو کشور تاکنون پیام‌های متناقضی در خصوص عوارض و مسیرهای تردد در این گذرگاه حیاتی ارسال کرده‌اند.
وزیر امور خارجه عمان همچنین تاکید کرد که مسئولیت اصلی تضمین امنیت تنگه هرمز و پاکسازی مسیرهای کشتیرانی بین‌المللی از هرگونه خطر مین‌گذاری، بر عهده جمهوری اسلامی ایران است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/76745" target="_blank">📅 17:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76743">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/q5xy0S2JlT3-c2t_34NqeGMkAIHKI6AfRPxYJCSP7Epwxo4yAxx7kYqYrRxDJGhzyRd9UtGtapjHk8k6FE-8dV1kRQHVsHE2J9SZrjqXoriidQn9QNg0_DLNaGEkfF6KO6XUGfuxkbfO26VARYf2_vQ8Jz3OMkEWO1WQVuhoVtl3dzE-QCYprrr7iw3YsJUEoia5CwVNVFq4UHdWA09d00Zfeq1ZVcR6-_-ltgci76ThTDlTvR_VA1mHJqJJDAJPsDQE7aYyVETNzyiKpAFCIA_qcFzUCgOrexNsjBXvtLyNxtrQK0WBtpdSRWYK7vQwmUJkgLgBMstwdLJk5bYh8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XRCbic8xVVigkD_sUwLkYzGV8FBE36Tnf5dGDJZh2A6P95elqdaNNfikoESCbHz8dGx5AYmUlX4PWWhH5SzQiqJrmJHiS5-_lgoKydnexJ0cJFndB8PU3XDA6_37KL1zaEP0i3s3x0SRvRUTgibxb55is2hX65imawfRJi6pirAzsZT2OE_X2-bRldIAEdWBjN3jwb9zMWp0Ug8f6XqJ1kXW6ZFAuGRIs7rkcOqnxkUyVm6ql1xr_dEZBJXCGboTAZaKFpoqe0cRPBRxMZhJVKywrWr07SQuaJAUCHXFmbnUAARmbgwFWq62Fl-Elf_OCZMimRnoaiCeFWHBQsDBag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست عراقچی با فوتبال، ترجمه ماشین: از زمین فوتبال تا میز مذاکره و تا میدان نبرد، هر گامی که ما ایرانیان برمی‌داریم، بخشی از مبارزه‌ای بزرگ‌تر است: دفاع از شرافت و کرامت مردم عزیزمان. araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/76743" target="_blank">📅 16:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76741">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/M5mDFcgIIZB1KAAYfpxQIkZhVB_Rxy6ODLkp0ewIiNRQnayUIx0vgmedwznFWtsgUVWCUJ7qXwz2egvgZfVQQg1E5HmI5RlfWmUo6Dt5uVc29s7sqfzsqJ8KS87UTvvJodr5g7io1CoNThlcsXI9RrvT76VosLYQ_rZW14H6-Eru9JZc9Z_CQ-57m6ThT8QnNCEm6UN6E15BgHEiGIVqisabQD7DwONISH6IVbXoZZfUNw8gqJsS1XKf1Sgein8OpKDebJQXDyso3qjweSDpKnGBdYrHGOFCNAioCGe2ZuNbFnsudA2ss42yek8G9N8CvReJnB3TC4K6DquIwMymqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Lw2f3xG8HkhLkJWQA1xyxBbPolKT8ONBN_bwoOXZ1fk4Ts_n2UKYeWVM6hjvXDja-3Ij88C9Ymaa-6Me_81ej-pGF5ET-Y1191tvbPF3EwWiF7lniw5YnpYSqFCpPJlDD_JxkaifugaSRyZ2614LJqENeeR9xuxIWjEWsfHrPutpFxF4rb0Ki0jfUtzqud9loMMngYgnsfxfiembUgajbz5hqdohKhU1AjbtuArZMfzy_qOlrUYIMV5_6saDXC925XI64xUl3Tz0aIilOzc5qm0uSfiTZAXWkp0wRq67kwJf5Hni468mfAM9ekpge-JUofcvD0djuwk4VoqbxDVSwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ در پستی نوشت: «ایران درخواست دیدار کرده است. (این دیدار) فردا در دوحه خواهد بود.»
پیشتر کاظم غریب‌آبادی، مسئول تیم فنی مذاکره‌کننده جمهوری اسلامی، گزارش برخی رسانه‌ها مبنی بر برنامه تهران و واشنگتن برای مذاکره در روز سه‌شنبه را تکذیب کرده بود.
کاظم غریب‌آبادی، مسئول تیم فنی مذاکره‌کننده ایران، امروز گفت: «هرچند رایزنی‌ها با قطر از جمله در خصوص پیگیری اجرای تعهدات طرف مقابل، طبق روال، در جریان است اما خبر برخی رسانه‌ها مبنی بر برگزاری گفتگوهای فنی کارگروه‌ها در دوحه تایید نمی‌شود.»
او در ادامه گفت که «اولین دور گفتگوهای فنی در چارچوب کارگروه‌های تعیین شده، با فراهم شدن شرایط و پس از توافق در خصوص تاریخ و محل آن، برگزار خواهد شد و رایزنی‌ها در این خصوص از طریق کشورهای میانجی ادامه دارد.»
@
VahidHeadline
«کارولین لیویت»، سخنگوی کاخ سفید اعلام کرد «استیو ویتکاف»، نماینده ویژه رییس‌جمهور آمریکا در امور خاورمیانه، و «جرد کوشنر»، مشاور ارشد پیشین کاخ سفید و مشاور غیررسمی «دونالد ترامپ» در امور خاورمیانه، روز سه‌شنبه در نشست دوحه با نمایندگان جمهوری اسلامی شرکت خواهند کرد.
@
VahidHeadline
ترامپ در پستی دیگر نوشت قیمت نفت خام وست‌تگزاس اینترمدیت به ۶۹ دلار رسیده و رو به کاهش است.
ترامپ در این پیام نوشت این قیمت از سطح پیش از آغاز «خلع سلاح هسته‌ای ایران» پایین‌تر آمده است.
@
VahidOOnLine
🔄
توییت خبرنگار اکسیوس:
به‌روزرسانی: یک مقام کاخ سفید می‌گوید فرستاده ویژه، ویتکاف، و جرد کوشنر امروز به دوحه سفر می‌کنند و روز سه‌شنبه با نخست‌وزیر قطر و دیگر مقام‌ها برای گفت‌وگو درباره توافق ایران دیدار خواهند کرد. روز چهارشنبه، تیم‌های فنی آمریکا و ایران به‌طور جداگانه با میانجی‌های قطری و پاکستانی دیدار خواهند کرد.
BarakRavid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/76741" target="_blank">📅 16:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76740">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdlSjDh_JnVFw2jTsmtNFtqJv23xGqezxeCA9sqCdgXyiDJmDWqXjNTCUmvEu0gCavLkNe1TRHia1Q4gX9D5Q203aJ5btg-0w5rPi5Coy2Zk2TAQoDKu2PBp15ra7Hh0i4o5tpuGWMt6ILQAEskpGJFensaYjhm257f1l8e9yJWV4T8EpJ-CReYdCU5WkpyquwJOys8fz_6nlXRgDWHc9yPzjtMxnhxZBT6A09vT6fb3v85dZ4tdH9iu9UzoKJ3JH7gK81idquPyKhvSOr82XBlC7VJd5FAWS284lgt8H9JgAV1LwjZ6rkd51llc34J_2crCgzv2LfORyS_zsbuO2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهوری اسلامی ایران روز دوشنبه هشتم تیرماه گفت: «براساس برنامه‌ریزی‌های انجام‌شده، شش میلیارد دلار از مجموع ۱۲ میلیارد دلار منابع ایران در قطر آزاد و به کشور بازگردانده خواهد شد».
مسعود پزشکیان در دیدار با شبیری زنجانی از مراجع تقلید شیعیان در قم گفت: «برای بازگشت بخش باقی‌مانده این منابع نیز پیگیری‌های لازم در حال انجام است».
او زمان مشخصی را برای آزادسازی این رقم اعلام نکرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/76740" target="_blank">📅 16:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76736">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NX713GOvt6HI5q5VXu3w3M_JNe6VptIyNBh7-rtAkLvIZ7JfeCVLo1SZMy8GthnNkb5yiAEoLVGIRYSgiWF-yr4GtsQK2ewbIh2j-CArNCIum9AKUDejR6uFE0hYEVUUa-UUy80a4QoQcMlHxnN1oXKTqBfvDXzPMPhzdvOi1E62M-P6DlXAgpYEujYJhx5_yXADVbeBF4ZlnrPrVbmsASeK8x4Nb8BqaunTDdPaaX-4uRgiuW7E9FZYVDtAd10rLWcf2ci_Gdpo8YFm8f-jdCD_MDUHzqX5S0-yoHHuCtbAePxU3qwPivsM3cdATCX6YY4ay3zb4pRDPM-b9ysknA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KEYdFdzu3JzV9vpiZif49BN89utFHSJ-NQFYvrZCnyKTcMRWlZJscthpNh_IShkldXEGaogv8Ks1EzohoszQCgUh0JW0djhLu1Tl7GTKdKdwSqpvJludHT4Q-WTgqPkdaZY9IdNy6pCIC0pgf1-hWVCWbRVdkX3o-6klEK_eNUEdQza7tavxHZFNwXMkdgabkBBXzPn_ZbqNv521X87EV9WeoSW5AcTDfu2oODRf2SN85BAFR_HBP1wS7Vzcn68J0wQy4dB3qPdIphfWjWSf6785hmdnPrswhFRMxhjPE_tGhZsaiaHLucprPDI3PGQ_E98Pc0yAWTTwzjNNyAFUDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h8pcr99PLKzTy7rHt2Nsuk4Ylw5bMWNLv0lz6fJnyfOx_-v3TnxKdKPj6Fe6zfbkM3L8RhrUqXe0O82JSQCLtOaJqTIhTOZX1R06uiSBir6mmdHGPTt5K-9Ndc40XNked5XS837ekt3hqgh0_2xWkzQv0ZdExDeenC9xeST5rblv04eF5pQLOOm-_pQr5JcH6k1hqq3_HdFaT2DK3M6TbeaMx3jniF8mdsvkAjSqM48XB-3VXGfS6whJU2Qmc2slyvoRBlNQLkmpzlrlGdYFX9_q_3u0mzOiMGdNJG_ANB_pzelBbdNfgotx0pTbRyn8qPVQxyyhLFslGboHhCT0rw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b61d44fd1.mp4?token=Q72q1dbuaqWgkuGrBQUm9sTZzUMLv1UW66koOKEFUBAWenVnDdAuqciiMGISHwBlFHmFM4vIWZE-sN8ynewnrQRy_ZZ9UHlrh7PcW6XI8-JQW_IhdnvfE1fro1iCM9Pc_GolwDOiL0lxApQ7NqqgMHKyofFKzuqA0o7XJiglix15U0NX-4n1gmeofCKWNsyOHpjE5xkqGzoGe6otiVhNPp3Mrix0XZRBryFrKU-nj5yFpkkh34yI73Z7RlGAOVVPAtbkGakAy7Q986ucIthF5GNcad2qGkV9nfhIfpkHgg7Q4jNGwqpdqNr34VLMwfuAcX3pBOWKUxdWEZXaQbZRq43v0-wxYBWKigDEHdoXGnYA1wC5s9FdRJKWzb63a1BoKPrKVhhj-amASiWX8HqVbUW3zQMTNmzF6r9iO6JwE2-hpOymZyD8lznciCxqsTJMoFQyJ0s_p1h4U0sSPPPegiLOf0wTowiLYlRE29qeOr6IEr9hNngLdGi7COjlkZxCjLJ7xb78Cpq1-7ecYkA4v34Zq-YAZCseMQ4LBK_lnCnmXXvvgNAGQy1J5DWKs08WclblK09ghPfPR5KhmqKK5fJ4XZZtru_Pi1HOJRSfhg3b463VTI5ChCdQfKEQ02KGq7LuKpbgYsX_igkkiyAO5lN55KXlOCAZRg87wiQdtKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b61d44fd1.mp4?token=Q72q1dbuaqWgkuGrBQUm9sTZzUMLv1UW66koOKEFUBAWenVnDdAuqciiMGISHwBlFHmFM4vIWZE-sN8ynewnrQRy_ZZ9UHlrh7PcW6XI8-JQW_IhdnvfE1fro1iCM9Pc_GolwDOiL0lxApQ7NqqgMHKyofFKzuqA0o7XJiglix15U0NX-4n1gmeofCKWNsyOHpjE5xkqGzoGe6otiVhNPp3Mrix0XZRBryFrKU-nj5yFpkkh34yI73Z7RlGAOVVPAtbkGakAy7Q986ucIthF5GNcad2qGkV9nfhIfpkHgg7Q4jNGwqpdqNr34VLMwfuAcX3pBOWKUxdWEZXaQbZRq43v0-wxYBWKigDEHdoXGnYA1wC5s9FdRJKWzb63a1BoKPrKVhhj-amASiWX8HqVbUW3zQMTNmzF6r9iO6JwE2-hpOymZyD8lznciCxqsTJMoFQyJ0s_p1h4U0sSPPPegiLOf0wTowiLYlRE29qeOr6IEr9hNngLdGi7COjlkZxCjLJ7xb78Cpq1-7ecYkA4v34Zq-YAZCseMQ4LBK_lnCnmXXvvgNAGQy1J5DWKs08WclblK09ghPfPR5KhmqKK5fJ4XZZtru_Pi1HOJRSfhg3b463VTI5ChCdQfKEQ02KGq7LuKpbgYsX_igkkiyAO5lN55KXlOCAZRg87wiQdtKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مبین یعقوب‌زاده یک سال بود که مادرش را از دست داده بود، زمانی که  تنها ۱۷ سال داشت، در ۱۷ دی ۱۴۰۴، در اعتراضات خشکبیجار رشت، با شلیک نیروهای امنیتی کشته شد.
🔸
سرگذشت کامل او را در یادبود امید بخوانید:
https://www.iranrights.org/fa/memorial/story/-9117/mobin-yaqubzadeh
@IranRights</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/76736" target="_blank">📅 16:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76735">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ac12c0761.mp4?token=lP5zTaYQ6pEJpi2i6gaOCbNc-uNgwZBXXyh9u62dlC5uDyeGwhMwZx41IBpZFjuqHHhouGhLaGCn2H497wdXWSfUw98UUWqMBMgCb_aQP6MBNHW9HPY2s2ob8-yzpZi3VUxQ2_uHUmeTliC86eafizvoEPJlvecbMHR5mER4_EyGyzuKoWyQcvZD6xS0bRvdzLK4M5LjOoWAmmNq4gPln0C84LChRfMAsJo-BkaIEVDr9MoR56ZanC74MnwNxmyn97DsMmhovxQFxJWGWn9Iq22i02LpfD1AKIXgdbUUpWihoWDBEAeoZHOs1OrmqCg8a3JY9edwV7kvDkh4xRuLvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ac12c0761.mp4?token=lP5zTaYQ6pEJpi2i6gaOCbNc-uNgwZBXXyh9u62dlC5uDyeGwhMwZx41IBpZFjuqHHhouGhLaGCn2H497wdXWSfUw98UUWqMBMgCb_aQP6MBNHW9HPY2s2ob8-yzpZi3VUxQ2_uHUmeTliC86eafizvoEPJlvecbMHR5mER4_EyGyzuKoWyQcvZD6xS0bRvdzLK4M5LjOoWAmmNq4gPln0C84LChRfMAsJo-BkaIEVDr9MoR56ZanC74MnwNxmyn97DsMmhovxQFxJWGWn9Iq22i02LpfD1AKIXgdbUUpWihoWDBEAeoZHOs1OrmqCg8a3JY9edwV7kvDkh4xRuLvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">(
⚠️
صدای بلند)
ویدیوی دریافتی با شرح کلی: "جنوب کشور، جنگ اخیر"
انفجارهای مهیبی در یک اسکله رو نشون میده.
از زمان و مکانش اطلاعات بیشتری ندارم، لینک یک صفحه اینستاگرام رو فرستادند که نسخه اصلی این ویدیو رو دیروز بعد از ظهر بدون هیچ توضیحی منتشر کرده و پست دیگری هم نداره.
Vahid
آپدیت:
در پیام‌ها میگن خرمشهره.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 419K · <a href="https://t.me/VahidOnline/76735" target="_blank">📅 04:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76734">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/spik40YZ6jX42WMNd2F3WUKMD4P_M75LnN8rAVSOu9bDlvTK3d9LgwotSjrN0h5MJu-ZHeHHtgcbK3fLBlpPpiZ--bqV5uG7EQu_w3S1oFdp3Ga_z7ULqF1R3Dpr33PEK5ZnKZHaynCR537v_OwMlEshEFcL1eP0PtcKvfWjEB9UdLZv-fCBEg6PzPbWaggn9CXSGtBXqhoK6_c7LVr5Zga6aW3NqvrTra0SPQs3QtFS8gIS1cvS-jd_kMxRIZ9Y65afqU4edqodaeGUa_BSZDTfoQOAHtI_SbkBTGAIvMVj3oVp829YihXj7Ib2xV1yKXyxHUgUo2Cs9ZEYo02hLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آکسیوس در نخستین ساعت بامداد دوشنبه هشتم تیرماه به وقت تهران (عصر یکشنبه به وقت آمریکا) به نقل از یک مقام ارشد آمریکایی گزارش کرد که ایالات متحده و ایران موافقت کرده‌اند که حملات علیه یکدیگر را متوقف کنند.
براساس این گزارش دو طرف قصد دارند روز سه‌شنبه در پایتخت قطر دیدار کنند تا به اختلافات خود در مورد تنگه هرمز رسیدگی کنند.
براساس گزارش باراک راوید یک مقام ارشد آمریکایی گفت: «ما تصمیم گرفتیم تمام فعالیت‌های «رزمی» (جنبشی/kinetic) را متوقف کنیم».
همزمان یک مقام دیگر آمریکایی هم به آکسیوس گفت که هر دو طرف «فعلا» عقب‌نشینی خواهند کرد و «شناورها می‌توانند آزادانه حرکت کنند» چرا که قرار است گفتگوهای فنی ادامه یابد.
هر دو مقام آمریکایی و یک منبع سوم آگاه، دیدار برنامه‌ریزی‌شده برای روز سه‌شنبه را تایید کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 425K · <a href="https://t.me/VahidOnline/76734" target="_blank">📅 00:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76733">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CeSENrnlgR3VuiZnjwgj2Q252uv_sakl8_5Gq9apZlCBV4vv3FbkStSAM_cem1r8JoowWxaNjXvHBT7Sv4rGiDcVTOoBcmb5zppDpgrTJPoOlLHWKd25zUZldi9bw27D-chO8L_tjv-YJiIfxdnnxkYgI5jWHKdhlUZYGixLveHLvdWm-sRMcLO7M_7oJRusoo9fABskXpvfjgJKzrT-xjPH7a_cARFuRQqUm_1jigC0Iww29ZMlTko8HL-lO722Siaeu1fcCQpWOV8w-ma5IyXFkLLqa9HVgYcEjUf7ZathYB5X8khtQ9nb7q79Ro4TNVkWZTXz-vyua6FOhdWQvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از آن که روز شنبه - ششم تیر - نزدیک به سه‌چهارم اعضای مجلس ۸۸ نفره خبرگان رهبری در ایران، در بیانیه‌ای شبیه «فتوا» خواستار گرفتن انتقام کشته شدن علی خامنه‌ای، رهبر پیشین جمهوری اسلامی از دونالد ترامپ،‌ رئیس‌جمهور آمریکا و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، شدند، دبیرخانه این مجلس روز یکشنبه - هفتم تیر - در اطلاعیه‌ای، این بیانیه را «نامرسوم» خواند و درباره آن توضیحاتی داد.
در بیانیه روز شنبه که ۶۳ عضو مجلس خبرگان آن را امضاء کرده‌اند، آمده بود که اگر «مسلمانان متدین» به این رهبران آمریکا و اسرائیل دسترسی پیدا کنند، کشتن آن‌ها «وظیفه شرعی» آنان است.
اما در اطلاعیه روز یکشنبه دبیرخانه مجلس خبرگان آمده که هیئت رئیسه این مجلس مفاد منتشرشده را «غیرمعمول و نامرسوم» توصیف کرده و اعلام کرده است که محتوای آن به بررسی و بحث بیشتر نیازمند است.
به نظر می‌رسد،‌ اطلاعیه دبیرخانه مجلس از اختلاف نظر و شکاف میان هیئت رئیسه و بخش مهمی از اعضای این مجلس حکایت دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 422K · <a href="https://t.me/VahidOnline/76733" target="_blank">📅 20:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76730">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BfH_4MxueZOD42X_3Em7NAPdKIo_s6FCT4rZi8ov0z357-VYjWFPWLAkihiGJIElnqfbyHkCfoIQJGn9HqEyU8uzdqfVJNR0o09AjP6yBVUyZRND60_e0gdxUVe-wcOoMUkYv9f2qgg4_kv8IY9m1HxAE6uhSJTSQlp1ldmAWhqAGFFwe2Q2F9x_ajtY_UwE-6omN0THF2aKhi_MYZ7N3c6gk7ydQ2IPYhkUAvaaHS3T31oPPGOC3O2nvvbRX5hqWTskYR5a7oEsyZoSDrJrbrAOtI3a1QFtM0iSkDP1rXPDJpvZPnn4MMEBJcYwR3riHYBzctQIeO7MWlQtUmkCRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AdLvw98aKfpMdpn-hAvncYZTJE3madpDD1zTXweoUzl3JBm-nT7W6_66EBLr6ci2ktQXWdy8N3N5s5JoXWnlZC6VuonrOMlxZIeg-Vr01fU3Jgh85goxh2hx0GEyDYQUWW_RL_vxO0OjW5yvHuECfS37N7E-3JYt11epsVaQ7lO_YXDCuedUqMtpa3Uych-BlBc2ac2pBlN4P-xnHoQApbQJ98SMHMuqKU_K8f-TyZFof6M7PGjQme20rSFnaEuoRrTPjU1RSf1DynMO4z14YAo5-y9sx1po7_20Zt5m2we-dd1uOXKOsxqzvMB82VgMmOBWY03iNnKQmHxB61iaAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bJkdfzHc8VWmT_97e9Fm7Ln1KwOsY1AzCMgdFqjRhAehTUD1p5IZ8Hi8k8tDjMww86kXuH0PdVxyzrR9_30iZ6HkJGAddT7BlahQMMsYAJ1Y5HjFW5G5M3TT_ZB2p9y6b_wlCHukW3N2S_YbIgh6tXMprgY3Og2D7S7iTBNO7fed94W21M0iDcEmGM_fs9B0MaAF9jR2jsuNZDMsggvrv0JejYta41Y62XIBGZEkFtsoffgQu4pvWInXeGRw7_pxENQYKuhbCDnu2qfQfdco3quyU8H-98aNmFLaKqXHR8eOO5VrvVNiXTSZhUKmIshd25t5GLsnuYMvkeuPV-f5Vw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بحرین گفت که یک ساختمان مسکونی در استان محرق هدف پهپاد ایران قرار گرفته است اما مجروح یا مصدومی گزارش نشده است.
تصاویری که دفتر رسانه‌ای پلیس بحرین منتشر کرده است خساراتی را به طبقه فوقانی یک مجتمع آپارتمانی نشان می‌دهد.
ایران بامداد یکشنبه اعلام کرد که به تلافی حملات آمریکا، پایگاه‌های آن کشور در بحرین و کویت را هدف قرار داده است.
بحرین و کویت این حملات را محکوم کردند.
بحرین همچنین خواستار جلسه فوری شورای امنیت برای پاسخگو کردن ایران شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/76730" target="_blank">📅 19:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76729">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UpcX50UPyYn_1fPDAS9xKyTKVds_xYntqoWBQO17fi7yyrRTEnWQzXbBmtO0Ay8rQ70onSvL4Ce3gVtawqY4XPPe4Hj8f4zNSOfhleeJbyxal0A3RkaNdxvKTyBYMpfIXf6rYpqHit2xrHog7E6e-FtAzSyeOgHtWOvJtGHF9UJdGUoNqeQiqBOI0M4Ussoqg7XykAxah68G0NCoEN5WtjQacvT7tYqzY6FMoXWGVxnAdU9g-pPLg1QH7HYkFCkGw8mbOfqumOmUbko9fhjrnIIhabzbrNjlEpSBLNbmVvuzqPW-oZZnQRwBa2X_630utG7mADSScg1nGCRM0dhH9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش قیمت دلار آمریکا و دیگر ارزهای خارجی در بازار آزاد روز یک‌شنبه، هفتم تیرماه، هم ادامه یافت.
روزنامه هم‌میهن خبر داد که قیمت دلار در بازار آزاد در روز یک‌شنبه به ۱۷۲ هزار تومان رسیده است.
این روزنامه قیمت یورو، واحد پول اتحادیه اروپا، را هم ۱۹۴ هزار و صد تومان ثبت کرد.
روز شنبه، ششم تیرماه، قیمت دلار آمریکا در بازار به ۱۶۶ هزار و ۷۰۰ تومان رسیده بود.
این افزایش قیمت بیش از پنج هزار تومانی در بازار دلار در حالی است که در پی امضای تفاهم‌نامه میان ایران و آمریکا، روز چهارشنبه ۲۷ خرداد قیمت هر دلار آمریکا به حدود ۱۵۳ هزار تومان هم کاهش پیدا کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/76729" target="_blank">📅 17:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76728">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5qT9gaPD8IVKJ1tH4vDt1ruR1usJLSOmpR2F81kfttRYBxS8KH_V8kdRUjlxIDM954-A17Va9BbDEZur3UJx82CduKlXQXPT2ELN6WZAGwwfM2t4u__40t2ljVyPNFuurXWB4YTyDP2G0QsEEDhOEEjOz3L36jAyMK3MNq4g8akwuatQMBCQZhtvGFhGkGQ6PNQLg2-xbdBqvlX9AS-uiRZYtOBbfWGbjFhB-57nA6LV1t8RIr0s1NLJEroqEXBe9MbUhizOCwT2iRxyfJi48iePFKsw2IqMYsyOFAeyyt1XfV9vKZuQ0WHOztTMjmpIp0kXzYEN0YM0Cyuk-G3aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای، سومین رهبر [اعلام شده] جمهوری اسلامی، در پیامی مکتوب به مناسبت هفته قوه قضاییه، از دستگاه قضایی خواست پرونده‌های مربوط به آنچه «جنایات آمریکا و اسرائیل» در جنگ‌های سال‌های ۱۴۰۴ و ۱۴۰۵ خواند را با جدیت در محاکم داخلی و بین‌المللی پیگیری کند.
او در این پیام که به مناسبت سالگرد هفتم تیر و هفته قوه قضاییه منتشر شد از قوه قضاییه خواست رسیدگی به پرونده‌های مربوط به جنگ را تا صدور و اجرای احکام ادامه دهد و مدعی شد چنین روندی می‌تواند از تکرار این‌گونه اقدامات جلوگیری کند.
مجتبی خامنه‌ای از زمان [اعلام] انتصاب به مقام رهبری جمهوری اسلامی تاکنون در هیچ مراسم عمومی، سخنرانی یا برنامه رسمی حاضر نشده [و صدا و تصویری هم از اون منتشر نشده] است. سایر مقام‌های حکومت تاکنون توضیحی درباره این موضوع ارائه نکرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/76728" target="_blank">📅 17:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76727">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dbba8d2b1d.mp4?token=Iy-hDbp9YwkJII-rI3tn4uYNKpYUn8vf0Rk_Ebkm-9eM8tDJiQ19WUo6A16xkqF3jD7wFlxcgytjCfCRR5FLTD15z483YD13NhmYh6ch65TL-gh3B9f9MpXM85EF-4RoGfNuE34mpuFflEMlRCdJFF3-KK0mvX0NCxN_9EbIyn6Hy49wI6PRO6dmyFHLURcuC2v1dny9dvIisqxvPPduVw3L_llFsScmzY8RSd1xT6S7tI8wbEwz4m_ZC5QD2QwABYuRI1_xrX3qdKKNmC8UaiIcfTzzYTi-OmG2-N6amF1YRrl6I-jne18P3SWFBeG-PeaL5bE7egaUsUBnogF2fA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dbba8d2b1d.mp4?token=Iy-hDbp9YwkJII-rI3tn4uYNKpYUn8vf0Rk_Ebkm-9eM8tDJiQ19WUo6A16xkqF3jD7wFlxcgytjCfCRR5FLTD15z483YD13NhmYh6ch65TL-gh3B9f9MpXM85EF-4RoGfNuE34mpuFflEMlRCdJFF3-KK0mvX0NCxN_9EbIyn6Hy49wI6PRO6dmyFHLURcuC2v1dny9dvIisqxvPPduVw3L_llFsScmzY8RSd1xT6S7tI8wbEwz4m_ZC5QD2QwABYuRI1_xrX3qdKKNmC8UaiIcfTzzYTi-OmG2-N6amF1YRrl6I-jne18P3SWFBeG-PeaL5bE7egaUsUBnogF2fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، روز یک‌شنبه هفتم تیر در کنار همتای عراقی خود به آمریکا هشدار داد که «ایجاد ترتیبات موازی» برای تنگه هرمز «صرفاً به پیچیدگی اوضاع، افزایش تنش‌ها و تأخیر در بازگشایی این آبراه حیاتی منجر خواهد شد».
در پی امضای تفاهم‌نامه میان تهران و واشینگتن، آمریکا هفته گذشته مسیر دوم را برای عبور کشتی‌ها از تنگه هرمز معرفی کرد، مسیری در نزدیکی سواحل عمان که از دسترس ایران به دور است و می‌تواند رقیبی برای انحضار ایران بر این آبراه باشد.
در واکنش به این اقدام آمریکا، سپاه در دو روز گذشته به دست‌کم دو کشتی حمله پهپادی کرده که بلافاصله پاسخ ارتش آمریکا را به دستور دونالد ترامپ به همراه داشته است.
در واکنش به این رخدادهای تازه در خلیج فارس،‌ عراقچی که برای دیدار با مقام‌های عالی‌رتبه عراق به بغداد سفر کرده روز یک‌شنبه در نشست خبری خود با فواد حسین، همتای عراقی‌اش، چنین گفت: «بر اساس این تفاهم‌نامه و پس از رفع موانع، تنگه هرمز ظرف مدت ۳۰ روز تحت مدیریت انحصاری ایران به ظرفیت پیش از جنگ باز خواهد گشت و مسئولیت اجرای این ترتیبات تنها بر عهده جمهوری اسلامی است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/76727" target="_blank">📅 17:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76726">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBwJHaAMfIcR_tvp5f0oxlJqDFas-x-DGXyLDTSR01WEwb8d92UAjgytRSvVGFu4KMzZSmKMvogFttpwoRRPT2nS-2z9ewiTCu5wg8q_wiWbPErv9KDxJR5YU84hxEnfsV6brRLzo9--n_8Y4jEQ_wmW4BmFab9Poea5fLYPxgemk6qWqeHxiJc3EUbE_G1WjGEyrzWXRaYc7sSgp7YQ8XFx37Kb0GBjuF6iOlhzPioY2pP0FOw0oC1DjlyCjNpSpjpUDUOBtNS4M3hXD9ZkB96HWCAH4b2LtIgrLgyrMEklYN-D3m8MROtj3vIM67oV1oUOSjkKx7pQEn_lDaz28Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«تقی چنگلوایی» فعال محیط‌زیست و داوطلب مردمی اهل بهبهان، در جریان مهار آتش‌سوزی گسترده در «کوه بدیل» زاگرس جان باخت.
تقی چنگلوایی هنگام مشارکت در عملیات مهار آتش‌سوزی، بر اثر شدت آتش و حرارت بالا و در پی انفجار دستگاه دمنده‌ای که به دلیل کمبود امکانات برای اطفای حریق از آن استفاده می‌شد دچار سوختگی شدید شد و جان خود را از دست داده است.
رییس اداره محیط زیست شهرستان بهبهان در گفت‌وگو با شرق نیز تایید کرده است که آتش‌سوزی در منطقه شکار ممنوع بدیل واقع در شمال بهبهان هم مرز با منطقه حفاظت شده خائیز هشت شب جمعه پنجم تیرماه شروع شده و هنوز هم ادامه دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/76726" target="_blank">📅 17:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76724">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">میثم پیرفلک، پدر کیان پیرفلک، که در جریان اعتراضات «زن،زندگی،آزادی» در ایذه کشته شد روز یکشنبه هفتم تیرماه پس از حذف ایران از جام جهانی در واکنش به حرفهای رامین رضائیان، نوشت: «خدا بخواد نمی‌شه که نمی‌شه آقای رضاییان.»
رامین رضاییان، پیشتر گفته بود: «اگر خدا بخواهد پیروز می‌شویم و دل مردم شاد می‌شود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/76724" target="_blank">📅 17:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76723">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F2QXpx_t7-l5beZQlVagZEkZg0Vop7701WAtodmnVN37X--VtXohDwSHaw0cVu8vSZJKPg-R0SXwCowh1vjAfWPSAnfFmHOJiUzs931gqOB5RUyY3eRBFr8xjeYVhvo3Gd0PR_0CwMZA5pbG0Wrr4kak2Xwak1YB6N9Kg9Lne2sEXz_eaw-MHX3MUqVdWz4OOZHOFxa85-QC8dNAC22U1jSOuJliByAnTvQuYFRKS7yT5MsKJ3XsDnC4eXoiMQX46TeuxGh77d-l7EFc3gUWrtg13j50_joRZmnIhgHLAGRBrWO9NeGjUWeTVNy1t2pB_K7iEpqnXbwFkkLLkA90-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار الجزایر و اتریش در مرحله گروهی جام جهانی فوتبال با تساوی سه بر سه پایان یافت؛
نتیجه‌ای که آخرین شانس تیم ایران برای صعود به مرحله حذفی را در آخرین ثانیه‌های مرحله گروهی جام از بین برد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 408K · <a href="https://t.me/VahidOnline/76723" target="_blank">📅 07:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76722">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jzPO3OlBVQQW67rLzHnJlN9zSDUJ1LRT2oClWe-q1mzMOmwHh_Zk2MWFav8z43-PpsR-i10L8KpPJJ2I5v_NbX0_-dCO6InQduIKJDQLdufNxxnMP3CdU9DxqoxhFvQs8MkCKuczs2jbmXLHVRz4H3GKP6lGt0aU7TuvLJBKu5VVrMZjIORnF8dsR_xWY4v46HGl2fppVT1FoSThVMl4rZKUQnX3-VOc30-ARv_M5tdSETklPe52fkvqeT0zM2hugW2TLqQJD3IO-cnOKZyaFP562w2r3LfC6E9pitZk2K22xDAhSprdJdtSl0j2HtugibC4Nvy_Okj9UWgfBGspqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی سپاه پاسداران، با انتشار بیانیه‌ای از حمله مشترک موشکی و پهپادی به مواضع ارتش ایالات متحده در منطقه خبر داد.
بر اساس این بیانیه، نیروهای دریایی و هوافضای سپاه در ساعت ۲ تا ۳ بامداد یکشنبه، ۷ تیرماه، هشت زیرساخت کلیدی ارتش آمریکا را در پایگاه «علی‌السالم» کویت و ناوگان پنجم دریایی در بندر «سلمان» بحرین هدف قرار داده‌اند.
سپاه این عملیات را «پاسخی قاطع» به حملات هوایی بامداد یکشنبه آمریکا به پنج پست ساحلی ایران در جنوب کشور دانسته و واشنگتن را به «نقض عهد» متهم کرده است.
در بخش دیگری از این بیانیه، با اشاره به اینکه کنترل ترتیبات عبور و مرور در تنگه هرمز بر اساس «تفاهم‌نامه اسلام‌آباد» بر عهده جمهوری اسلامی است، تاکید شده که از این پس با کشتی‌های متخلف قوی‌تر از گذشته برخورد خواهد شد.
سپاه پاسداران با هشدار به ایالات متحده اعلام کرده است که هرگونه تجاوز احتمالی بعدی، حتی اگر علیه اهداف کم‌اهمیت باشد، با پاسخی «خردکننده» مواجه می‌شود.
@
VahidOOnLine
متن خبر منابع حکومتی:
🔸
سپاه پاسداران خبر داد: عملیات قاطع موشکی و پهپادی در پاسخ به تجاوزهای آمریکا/ با کشتی های متخلف قوی‌تر از گذشته برخورد خواهد شد
🔹
روابط عمومی سپاه پاسداران انقلاب اسلامی بامداد یکشنبه با صدور بیانیه ای از پاسخ قاطع نیروهای دریایی و هوا فضای سپاه به تجاوزهای اخیر آمریکا خبر داد و تاکید کرد: من‌بعد با کشتی های متخلف قوی‌تر از گذشته برخورد خواهد شد و برخورد با تجاوز احتمالی دشمن به هر بهانه‌ای که باشد ولو مانند دیشب و امشب تجاوزها به اهداف کم اهمیت باشد، پاسخی خرد کننده خواهد داشت. دشمن بداند نقض آتش‌بس خلاف بند یکم تفاهم نامه اسلام آباد است و توقف کلی روندها را در پی خواهد داشت.
در ادامه این بیانیه خطاب به مردم عزیز و شرافتمند ایران اسلامی آمده است:
فرزندان غیرتمند شما در نیروهای دریایی و هوا فضای سپاه طی عملیات مشترک موشکی و پهپادی در ساعت ۲ الی ۳ بامداد امروز یکشنبه هفتم تیر ماه، با پرتاب موشک های بالستیک و پهپاد به سوی هشت زیرساخت مهم ارتش کودک‌کش آمریکا در پایگاه علی السالم کویت و ناوگان پنجم دریایی در بندر سلمان بحرین آنها را منهدم کردند و تجاوزهای اخیر آمریکا را با قاطعیت پاسخ دادند.
دشمن متجاوز که نقض عهد و پیمان شکنی در ذات او است، به بهانه مقابله نیروی دریایی سپاه با کشتی متخلف، اوایل بامداد امروز، به پنج پست ساحلی جمهوری اسلامی حمله کرده بود.
بر اساس تفاهم نامه اسلام آباد ترتیبات کنترل عبور و مرور در تنگه هرمز با جمهوری اسلامی است و من‌بعد با کشتی های متخلف قوی تر از گذشته برخورد خواهد شد و برخورد با تجاوز احتمالی دشمن به هر بهانه ای که باشد ولو مانند دیشب و امشب تجاوزها به اهداف کم اهمیت باشد، پاسخی خرد کننده خواهد داشت.
دشمن بداند نقض آتش بس خلاف بند یکم تفاهم نامه اسلام آباد است و توقف کلی روندها را در پی خواهد داشت.
🔹
و ما النصر الا من عند الله العزیز الحکیم
در خبری دیگر:
نیروی دریایی سپاه پاسداران بامداد یکشنبه هفتم تیرماه، با انتشار بیانیه‌ای در واکنش به حملات اخیر آمریکا اعلام کرد «شلیک‌های کور آمریکا به سیریک» معمای اشراف این نیرو بر تنگه هرمز را حل نخواهد کرد.
در این بیانیه آمده است شلیک به «متخلفان» راه عبور را به دیگر شناورها یادآوری می‌کند. همچنین با تهدید پایگاه‌های آمریکایی در منطقه تاکید شده است: «حساب پایگاه‌های آمریکایی منطقه جداست. جهنم را در این روزها تجربه خواهند کرد.»
@
VahidOOnLine
رویترز به نقل از یک مقام آمریکایی گزارش داد در پی حمله‌های موشکی و پهپادی جمهوری اسلامی به کویت و بحرین، هیچ گزارشی از تلفات نیروهای آمریکایی یا وارد آمدن خسارت یا آسیب عمده به تاسیسات آمریکا در خاورمیانه دریافت نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 408K · <a href="https://t.me/VahidOnline/76722" target="_blank">📅 04:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76721">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f7b676ffd6.mp4?token=Cl5w3a4ezcqipGCVwiqmlBoN92pFIXVEkdueMxlTPAH0vZ4JX-_0c2fdoQfkN3Wg5RhoIjlD-lYbOmWF1sELAReuw1Kkmqk_GSmD-jbuvXyTP8E5amxDQprsuQqsSgZRASEIVS3j0ixKGeXrHDUwJuc142iD_m4FJ4kNR2AIV0mJsqvfHKXjmYCMimfq_5qCTqm19pbqLaRD557GwndLCeuF10KEmLbuB4RuUtCpoy4dE-EVePZTisBfJitltZbusdB2hyUfuoWIVhg8h8uOcvh1FOrWyP99HrjYU-gANncu0spOt7OzHJvrEcKih40hkoC0uEJMgzriiW4quuQKxg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f7b676ffd6.mp4?token=Cl5w3a4ezcqipGCVwiqmlBoN92pFIXVEkdueMxlTPAH0vZ4JX-_0c2fdoQfkN3Wg5RhoIjlD-lYbOmWF1sELAReuw1Kkmqk_GSmD-jbuvXyTP8E5amxDQprsuQqsSgZRASEIVS3j0ixKGeXrHDUwJuc142iD_m4FJ4kNR2AIV0mJsqvfHKXjmYCMimfq_5qCTqm19pbqLaRD557GwndLCeuF10KEmLbuB4RuUtCpoy4dE-EVePZTisBfJitltZbusdB2hyUfuoWIVhg8h8uOcvh1FOrWyP99HrjYU-gANncu0spOt7OzHJvrEcKih40hkoC0uEJMgzriiW4quuQKxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
سلام آقا وحید از منطقه [...] بندرعباس چندتا موشک بلند شد به سمت دریا رفت
سلام ساعت ۳:۳۹ صدای انفجار بندرعباس
یک دقیقه بعد: الان یکی دیگه هم زدن
درود همین الان اطراف بندرعباس دوتا صدای انفجار
ساعت ۳:۳۶ دقیقه
صدای دوتا انفجار از راه دور تو [...] بندرعباس شنیده شد، فاصله دور بود اما موج انفجار تو [...] حس شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/76721" target="_blank">📅 03:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76719">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QVnZD7DdMsOUiTEjDG7kvvPET49Po7Zwt2RYT6leU_3CCg70yT_dgyAkKvVSpOfEcG3GM6F4XpGao4yfWv-NeYmJ1wjmTlTeDql70lTDJ0ai767rWftKwpw212svVHHttMls-hubRyaCuF6PW5NcZH3b7dw0i1Q6pku2Ov8sZwkJYUa64dxoupzmSDv3vLXxq6yjoVqIZoYt94lY9H2VLDySfCrRfpFfDz0gzUOUg1UjpzhqUzx0GafQn5XDbkq9Jp0Sw70jlOqIOb4BJd8XVftv8AT6YU8FoJF1ESmYQKlkXdBI1OEZMEOkfl6sRnjaQ54Al-sTX0opc55W9zZcGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/A3kJ-qJPRgsHt1CPnBkk-CpaojeoGxTkzAJKq-7hz1uP-_KQLa4umXAJ-yTikHP3VzpCq47v8Ekh5n7QF0Q6caXUZNZkcz_NqA-XyvWHL62Tb4nZWoJzt_TqsCCp9waL5JELcZts6MPOyaowaqDpo9gjKaSKu2VJq5RFE4f0-OFDWJCvHSlHLUhp89r8W-wTLyNIo2v7GpkjjOGFXwrwMGzO3YmngRihI4eGh6BC0iCODyirwzEpbecKAkubKrGLYtwawzEcIG6gcx09qv5QADtPaHOD0NOZQD_uANdysSlARIbwD-0GeogHczWzl7nyYtoytDpiw2RA18EFYn1dAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اعلام هشدار در کویت
تصاویر دریافتی
ارتش کویت دقایقی پیش اعلام کرد که پدافند هوایی این کشور در حال حاضر «با حملات موشکی و پهپادی خصمانه» مقابله می‌کند.
@
VahidHeadline
دقایقی پیش‌تر پیام مشابهی درباره بحرین دریافت کرده بودم. الان:
وزارت کشور بحرین، بامداد یکشنبه، با انتشار اطلاعیه‌ای از به صدا درآمدن آژیرهای هشدار خبر داد و از تمامی مردم و ساکنان این کشور خواست تا ضمن حفظ آرامش، فورا به نزدیک‌ترین مکان امن پناه ببرند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/76719" target="_blank">📅 03:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76718">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aLXMu5Ua8kA4scTEHwI1b_wQ9pgr32WU6W6r6bvwRZLAEFmlHgUDoamHEXpJOP7jVDyiWFaDXTn9E9FAj_rVIkpgXAPGuke6vgS9oEDlM7Oh4mIpyO25Q0yc0cGgEndLufXDUZVXnh79hduyyTuQ1018NYZjpAi0jHyTkLMVRMCct8m8gmKVZHp5yKTw-25Oz0xO604peBJchP77uT1vZq_kzFPlVNyXGUfVou7xizgeBAjVQZRQv6UhrjlwZLbP5wHHVsLR2dotaM8G2xZOXJpHTW2u3n6qzwnsAtBpRgly0d4Zh49ZtzSHolKfFCFX1IEqIYbWA6f7VjkDKr4cNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: در صورت ادامه نقض آتش‌بس، جمهوری اسلامی ایران دیگر وجود نخواهد داشت
ترجمه ماشین:
هواپیماهای ایالات متحده همین حالا محل‌های نگهداری موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادند، چون بار دیگر توافق آتش‌بس را نقض کردند!
بسیار محتمل است که آن‌ها هرگز درس نگیرند!
ممکن است زمانی برسد که دیگر نتوانیم منطقی رفتار کنیم، و مجبور شویم کاری را که با موفقیت بسیار آغاز کردیم، از نظر نظامی به پایان برسانیم.
اگر چنین شود، جمهوری اسلامی ایران دیگر وجود نخواهد داشت!
رئیس‌جمهور دونالد ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/76718" target="_blank">📅 02:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76717">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d134b6727d.mp4?token=iZ8-IcixE2ifHrVo_wsiokn_gEkbOghfD6LFcVK1i-LuusK4w2EPbOKUYkTk7LhpD1KCdY7nqBMkaAFRBX2VTXNmpvrvXyqktXu3K2lTvLCOQ-38mulXakFLGf6UE3XctWdlFkb-OcfEHlqpTU_Ov8_jTAKUwdAo7eoXwGfrpGQ3M6vBIK_5rlHV_oWEnN7dr9eDD3kq6oAksp-I_i-ujgehX7sHtAeTjtNp-TuUVBIcOxDlxqx-b5JKJ_JqWnTNCQf4V-qJC887Cc-hc1_leQAbV2khSDZHntD6eb8O6gCZxWnklMnqMKACAa-PUXoeeJTMkUjHqEfmJtWmN0TsOA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d134b6727d.mp4?token=iZ8-IcixE2ifHrVo_wsiokn_gEkbOghfD6LFcVK1i-LuusK4w2EPbOKUYkTk7LhpD1KCdY7nqBMkaAFRBX2VTXNmpvrvXyqktXu3K2lTvLCOQ-38mulXakFLGf6UE3XctWdlFkb-OcfEHlqpTU_Ov8_jTAKUwdAo7eoXwGfrpGQ3M6vBIK_5rlHV_oWEnN7dr9eDD3kq6oAksp-I_i-ujgehX7sHtAeTjtNp-TuUVBIcOxDlxqx-b5JKJ_JqWnTNCQf4V-qJC887Cc-hc1_leQAbV2khSDZHntD6eb8O6gCZxWnklMnqMKACAa-PUXoeeJTMkUjHqEfmJtWmN0TsOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یارو در «رسانه ملی» جمهوری اسلامی داره میگه چون کشتی‌ها قصد عبور از مسیر «ناایمن» رو داشتند سپاه اون‌ها رو هدف قرار داده بوده!
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/76717" target="_blank">📅 02:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76716">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fba5afa7ba.mp4?token=ms3nzu9b89YcFlOE2TIPcGQDy75D-PwU7S6v5MuPgUl6RFdWEMgpzwXIT2oHyVRP8eXQJg1m7_7XwP-sNzGfPtj7Jy8k0tzo8E9ch-q33Ehf0txIV0nc4pjFsjHDWWpPrR0e_P3nmhuq4yIN7KBDe-SSR1XyK-_T-CHFfRh43BlZqLWEg-9Soc31IwXHzongpaP1yjKLc7eB-eb8CsVoWJmyeKYXnyh9JO8BcU22BhQbzAKxY8E2AJgdni_xXJi0DZfj2JuwGgDvxm49z4WoGkUwJ73AX0b437aCCzyykiVkfu1Fq8OjLjFqp-Esr9VEVA1MszezYoLXxDnM8mqO0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fba5afa7ba.mp4?token=ms3nzu9b89YcFlOE2TIPcGQDy75D-PwU7S6v5MuPgUl6RFdWEMgpzwXIT2oHyVRP8eXQJg1m7_7XwP-sNzGfPtj7Jy8k0tzo8E9ch-q33Ehf0txIV0nc4pjFsjHDWWpPrR0e_P3nmhuq4yIN7KBDe-SSR1XyK-_T-CHFfRh43BlZqLWEg-9Soc31IwXHzongpaP1yjKLc7eB-eb8CsVoWJmyeKYXnyh9JO8BcU22BhQbzAKxY8E2AJgdni_xXJi0DZfj2JuwGgDvxm49z4WoGkUwJ73AX0b437aCCzyykiVkfu1Fq8OjLjFqp-Esr9VEVA1MszezYoLXxDnM8mqO0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
نیروهای آمریکا پس از تازه‌ترین حمله ایران به کشتی تجاری، حملات بیشتری انجام دادند
تامپا، فلوریدا — نیروهای فرماندهی مرکزی آمریکا (CENTCOM) به دستور فرمانده کل قوا، روز ۲۷ ژوئن حملات بیشتری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا در پاسخ به حمله ایران به کشتی M/V Ever Lovely،
به ایران فرصت داده شد تا به توافق آتش‌بس پایبند بماند، اما این کشور چنین نکرد
؛ زیرا نیروهایش یک پهپاد تهاجمی یک‌طرفه را شلیک کردند که صبح امروز ساعت ۴:۳۰ به وقت شرق آمریکا به نفتکش M/T Kiku برخورد کرد. این نفتکش با پرچم پاناما در نزدیکی تنگه هرمز در حال عبور بود و بیش از دو میلیون بشکه نفت خام حمل می‌کرد.
نیروهای سنتکام امروز در پاسخ مستقیم به ادامه تعرض ایران علیه کشتیرانی تجاری، حملاتی انجام دادند. هواپیماهای نظامی آمریکا زیرساخت‌های نظارت نظامی ایران، سامانه‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات نگهداری پهپاد، و توانمندی‌های مین‌گذاری را هدف قرار دادند.
عبور کشتی‌های تجاری از تنگه هرمز ادامه دارد. نیروهای آمریکا همچنان هوشیار، مرگبار و آماده هستند.
CENTCOM
آپدیت:
بعدا ویدیوی بالا رو درباره این حمله منتشر کردند
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/76716" target="_blank">📅 01:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76715">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n4MexarGViV9xfp2snaWzwM2ehdyZBBWL2KnDWRg9rK7kIWY-skvp-vb0dpTD-lJuC2vyuT-2VVtBsq3lFY0OcXhdqdHxlE4SHVA2JluU47PWBGqydZdRuOZTcLGBKCMkj7IBLXtHNex-h1nUBv0rqAv6o4lZtv85zMeYmJteuJWbM0PKENFrnaqPiAjJHs1esBdlZt495VBZqT-gpkRKLn7OBZaO1F3pNir8Vy90NX1YWUvNYWCy3ddBbH66kL8_r3cPEHttWqYC1SsAKhN2LuK4J3Cv7aXYevURXnhQhpjy6D_NXlfmvZb29wNfCsPSlzXYmvnXG50pM0Jkaupzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام رسمی ایالات متحده در گفتگو با خبرنگار آکسیوس تایید کرد که ارتش آمریکا، بامداد یکشنبه، هفتم تیرماه، در حال انجام حملات تلافی‌جویانه علیه اهدافی در منطقه تنگه هرمز است.
به گفته این مقام مسئول، این اقدام نظامی در پاسخ به حمله صبح شنبه به یک نفت‌کش تجاری در این آبراه حیاتی صورت گرفته است.
@
VahidOOnLine
پیش‌تر:
صدا و سیما: دقایقی پیش صدای چند انفجار در محدوده روستای طاهرویی سیریک شنیده شد
پیام‌هایی که من دریافت کرده بودم:
صدای چند انفجار.
طبق معمول انگار دوباره نیروی دریایی سپاه سیریک رو زدند.
سلام ساعت 12.41 صدای چند انفجار شدید بندرعباس
همین دو دقیقه قبل پایگاه دریایی سیریک هدف حمله موشکی
جوری زد که زمین لرزید
پایگاه دریایی طاهرویی سیریک رو هم زد
دوتا موشک صداش اومد رو دریابانی سیریک
دکل اسکله سپاه سیریک بعد چهار ماه موشک خوردن مداوم بلاخره امشب کج شد
قشم سمت سوزا صدای انفجار شنیده شد حدود ۱۲:۳۰
سلام وحید جان  تقریبا ساعت 00:45 صدای انفجار هرمزگان .قشم
تسنیم:
در اولین ساعات بامداد یکشنبه  صدای انفجارهایی در سیریک شنیده شده است.
برخی منابع مدعی شده‌اند که صدای انفجار در بندر طاهرویه بوده، اما هنوز هیچ منبع رسمی آن را تأیید نکرده است.
🔄
آپدیت ۱:۰۲
خبرنگار صداوسیما در سیریک به نقل از یک منبع آگاه نظامی: صدای انفجارهای شنیده شده مربوط به اصابت چند پرتابه به دکل مخابراتی در محدوده روستای طاهرویی سیریک است
💥
آپدیت ۱:۰۶
خبرنگار اکسیوس: یک مقام آمریکایی می‌گوید ارتش ایالات متحده در تلافی حمله ایران در صبح امروز به یک نفتکش تجاری، در حال انجام حملاتی علیه اهداف ایرانی در محدوده تنگه هرمز است.
آپدیت ۱:۱۲
خبرنگار صداوسیما در قشم به نقل از یک منبع آگاه: چند پرتابه در محدوده روستای مسن شهرستان قشم اصابت کرده است
آپدیت ۱:۱۷
صدا و سیما شنیده‌شدن دو صدای انفجار دیگر در شهرستان سیریک، منشاء صدا مشخص نیست.
آپدیت ۱:۴۱
صدا و سیما:
برخی منابع از شنیده شدن صدای چندین انفجار در بندرلنگه و بندر کنگ خبر می‌دهند
خبرگزاری صدا و سیما هنوز قادر به تایید قطعی این انفجارها نیست.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/76715" target="_blank">📅 00:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76713">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AUPPyjRmHMI-s45Cz8eBicbU7zxzp0KlvZSKEYU7jEbwA_JSB5wcNdHcwd5CWnyOW6WAK35GQvQr11rUaJZjw9CHrBUQaStTr2qajXTYNqbzExEq-h-6bgz7LSutl-KNsbH58zGl_tTBFC8DrGQYjZOdLzWoK32zgmrtpBbjpda0oK9C7pc0FcBlOWAQmmR_ibMQSxrT1ycYxtb8PkIJSQP0PHWht9uCWTf_ZTaB_mF6E4-bm1XFXzcmVq_eESItcm3PVSPdLBs69U3Lb8qcX1T8Pz3RAumiDjfEuUbwo47VDyRlmGprXTaOt3fxZeAHbtrFWxrHtNoG0Xu69vlCQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ps_yfN_1L8godp2mPNeLJ9O6bgk1ufeayulDyRY08VPAHuG2dRhxqnv3-_v_wzCznOjgN2zuPBe9e9h-VZsOlLPEA1o6FzuhlW8nd7Sri_hKwNqpOOIsKe_Mggc4ZC07l5j0foHm8bU4Eb4DwtaJQhfKlb8m1piBufsaw-k2b-73oXFo3_H7VZmI23Ton8lrXM2NJUD1P3a2yxxF-7iKvQQfMKzej0NoxxpIlA0-nHZXEtuxeTKbnkACnLg1Yqy_bOHy_hxYO6TAqAzFVaWtquLjKs1mBUcrI9HhO9hT4RiloEyLmsaNzMxu2tBCDCpB1ZmM05rFmmIg1pZzBXvU6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسانه‌های ایران بیانیه‌ای با امضای جمعی از اعضای مجلس خبرگان را منتشر کردند که در آن می‌گویند بازگشایی تنگه هرمز «خلاف تعهدات مسئولان است و خطایی راهبردی شمرده می‌شود».
بر اساس این بیانیه که خبرگزاری‌های تسنیم و فارس، نزدیک به سپاه، آن را منتشر کرده‌اند، ۶۳ نفر از اعضای مجلس خبرگان تداوم حملات اسرائیل در لبنان و «عدم عقب‌نشینی»‌ ارتش این کشور از مناطق جنوبی لبنان را «نقض آشکار» تفاهم‌نامه ایران و آمریکا خوانده و نوشته‌اند بر این اساس بازگشایی تنگه هرمز «خلاف تعهد مسئولان است».
در بخش دیگری از این بیانیه نیز آمده است «بر هر ملکفی» که به دونالد ترامپ، رئیس‌جمهور آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، «دسترسی پیدا کند، واجب است آن‌ها را به درک واصل کند».
این گروه از اعضای مجلس خبرگان همچنین «تثبیت مدیریت تنگه هرمز و دریافت غرامت خسارت‌ها و بازگشت اموال بلوکه شده و رفع تحریم‌ها و خروج امریکا از منطقه» را از مطالبات رهبر جمهوری اسلامی برشمرده و هشدار داده‌اند که «هرگونه سهل انگاری در این زمینه» با واکنش مواجه خواهد شد.
این بیانیه در حالی منتشر می‌شود که اختلاف‌ها در درون طیف‌های سیاسی طرفدار حکومت بر سر تفاهم‌نامه در روزهای اخیر بالا گرفته تا جایی که روز شنبه، نمایندهٔ رهبر جمهوری اسلامی در سپاه، از منتقدان این توافق خواست با «ایجاد اختلاف و لغزش» باعث «سوءاستفادهٔ دشمن» نشوند.
تفاهم‌نامه ایران و آمریکا به‌گفتهٔ مسعود پزشکیان، رئیس‌جمور ایران، با رأی «بیش از ۹۰ درصد» اعضای شورای عالی امنیت ملی کشور شامل شماری از فرماندهان ارشد سپاه پاسداران تأیید و تصویب شده و مذاکرات برای اجرای آن آغاز شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/76713" target="_blank">📅 23:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76712">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41aa678ed6.mp4?token=tyqYRQPUzsO9romAJ-C9i3IoczQJo5qQWzy9BMLuPhfA3v-4tzWMBs5bWowp0ln4pmEgyYlA6SUor3MK7VdkEUZ5BUe4uHOwoATsYPNnX89AJmEllDc7jInKRxk2tUHLtYAPt3oRHS5mVzHyhzAJCVFMoIwWnUjssojZYQSCZ99AdhSm9r-Og-lUj4St2zWQeUbbFRAMsRRrFtft3c9rpFl2IdDy0iUq1c6eSZjHoUK_pC0AgKO1I5SXXUNlHDuDiRDyHSE4af27J1cADTnh5bGuUCcAcmOOM44OGjErEzLB8NpKMLidkIzf3KRohcuDZHioJ9-ugowHIt_jMN_esQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41aa678ed6.mp4?token=tyqYRQPUzsO9romAJ-C9i3IoczQJo5qQWzy9BMLuPhfA3v-4tzWMBs5bWowp0ln4pmEgyYlA6SUor3MK7VdkEUZ5BUe4uHOwoATsYPNnX89AJmEllDc7jInKRxk2tUHLtYAPt3oRHS5mVzHyhzAJCVFMoIwWnUjssojZYQSCZ99AdhSm9r-Og-lUj4St2zWQeUbbFRAMsRRrFtft3c9rpFl2IdDy0iUq1c6eSZjHoUK_pC0AgKO1I5SXXUNlHDuDiRDyHSE4af27J1cADTnh5bGuUCcAcmOOM44OGjErEzLB8NpKMLidkIzf3KRohcuDZHioJ9-ugowHIt_jMN_esQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر اسرائیل در سخنرانی تلویزیونی خود ضمن اشاره به توافق اخیر با لبنان، آن را دستاوردی «بسیار بزرگ» توصیف کرد.
بنیامین نتانیاهو با تاکید بر اینکه اسرائیل در «منطقه امنیتی زرد» باقی می‌ماند و این مسئله ضامن امنیت این کشور است، خاطرنشان کرد که فشارهای مختلف برای خروج اسرائیل از این منطقه به نتیجه نرسیده است.
او با قدردانی از نقش دونالد ترامپ، رئیس‌جمهوری آمریکا و مارکو روبیو، وزیر امور خارجه این کشور، در تحقق این توافق، تصریح کرد که اسرائیل نه تنها "محور تروریسم ایرانی"، بلکه "محور سیاسی ایران" را نیز در هم شکسته است و افزود: «ما به دلیل ساده‌ای به چارچوب این تفاهمات رسیدیم: چون حزب‌الله را به شدت در هم کوبیدیم و حزب‌الله که منتظر کمک ایران بود، آن را دریافت نکرد».
بر اساس طرح پیشنهادی آمریکا که چارچوب توافق لبنان و اسرائیل بر آن بنا شده، نیروهای اسرائیل به‌صورت مرحله‌ای، کنترل مناطق مختلف را به ارتش لبنان واگذار می‌کنند و ارتش لبنان نیز مسئولیت جلوگیری از ورود اعضای مسلح حزب‌الله به این مناطق را برعهده می‌گیرد.
خواسته اولیه لبنان، خروج کامل نیروهای اسرائیل از مناطق جنوبی این کشور بود.
حزب‌الله لبنان، این توافق را «تحقیرآمیز» توصیف کرده و آن را فاقد اعتبار دانسته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/76712" target="_blank">📅 22:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76711">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OXKUuUZDYmMCqSj_azVuvsNksOyUqdhgRqaU8JApeIU1BjVy7DBuKqlSru3EW_-80Yz-SgUyndjE6M-n_K-pV-W2tV1jeLlURiWeThpjs4P4XAV4VxzYes1Dy3DVsqcS6rjdKWq4KE1qz6u0k8skQi_RZF6TI-G09uiytZ0Q-LlgNJ71VMhan2pOcPDSPqOmTHiApRoWfoxRRv_XzdB8OCWt0J91mxnXtYm4q-WnQsafxfs1d5UAMDVK1ZtqOixzJyysicUx_UDnISppUYMM57tuftwLbHAI66O2y4w9vCEg5pIOE1Kc6z2tvsfEWm1W3UPir8KWtH-crGDTculbMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی درباره قطع شدن برق در مناطق مختلف شرق تهران:
سلام وحید جان
به طور بی سابقه ای کل برق پیروزی و بلوار ابوذر رفته کلا خاموشه محله های این طرفا
توی قطعی برقیا هیچوقت اینجوری سابقه نداشته کل محله ها با هم بره کلا شرق خاموشه
سلام وحید
ما محله نیروی هوایی ، منطقه ۱۳ تهران هستیم. برقا رفته. و اینجور که از دوستان پرسیدم تا  خیلی جاها برق نداره، حتی برق  چراغ راهنمایی  رانندگی هم قطع شده.
مثل یه سری که توی جنگ برق ها قطع شد و حمله کرده بودن شده، چشم چشم رو نمیبینه
سلام وحید جان برق شرق تهران محدوده پیروزی کامل قطع شده
وحید برق  نارمک هم رفته
😐
😑
نارمکاز پشت بوم دیدم تا جایی که افق دید اجازه میده کلا شرق تو تاریکیه
برق سمت نظام آبادم کامل رفته همه جا تاریکه
داداش برق سبلان و نظام آباد و اینام رفته
سلام برق سبلان هم‌رفته
سلام، من میدون رسالت تهرانم، تا چشمم میبینه همه جا تاریکه
بجز مناطق خیلی دورتر
کل نارمک جنوبی بی برقیم
سلام ما نارمکیم ولی برق داریم
نارمک پایین هفت حوض برق هست
سمت رسالت و سرسبز رفته
سلام برق جنوب نارمک هم قطع شده فکر کنم پست دوشان تپه مشکل دار شده
وحیدجان ما نظام آبادیم ولی برق داریم
البته به بیمارستان امام حسین نزدیکیم
وحیدجان برق شهید کلاهدوز هم رفت همی الان
داداش ما کلاهدوزیم دو دقیقه پیش رفت
همه جا تاریکه
سلام وحید جان
محدوده شیخ بهایی تهران خیابان شیراز شمالی هم برق رفت
سلام وحید جان
تهرانپارس فلکه اول
ما برق داریم ولی دارم نگاه میکنم ی سریا ندارن!
برق خیایان شیخ بهایی شمالی رفت
انتهای تهران نو سمت اشتیانی و فلکه اطلاعات برق نداریم.
ما نیروهوایی هستیم برقا تا جایی که میبینیم قطعه
آقا برق وصله چرا الکی میگن شما هم میزارین مردم همه حالشون بده ترو خدا استرس بیخود ندین
برق خیابون مدنی،  نظام آباد همچنان قعطه
نارمک ۴۶ متری غربی برق رفته بود دو سه دقیقه هست که برگشته
نارمک جنوبی، حوالی میدان شقایق هم برق رفت.
سلامت میدان ۷۰ و سمنگان هم رفته بود.
الان بعد ۲۵ دقیقه اومد
وحید جان سبلان شمالی برق قطعه
سلام، زرکش وحیدیه برق قطعه
وحید جان سلام پیروزی چهارراه کوکاکولا برق داره اما کل خیابان نیروی هوایی برق رفته به طوری چشم چشم رو نمیبینه مردم با نور موبایل راه میرن
برق نظام‌آباد اومد
ندیدم مجیدیه رو بگند که برق رفته. اینجام نیست
منتها زنگ زدم و محله بقلی خواجه عبدالله برق هست.
سلام وحیدجان ما پیروزی سمت خیابون شیوا هستیم برق داریم
برق مجیدیه و خیابان کرمان از ۸.۲۰ دقیقه کامل قطع شده . تا چشم میبینه برق اطراف قطع شده
الان. نظام اباد محدوده شرقی امام علی خاموش بود همین الان اومد.
داداش برقا اومد فک کنم یه بانکی چیزی خالی کردن رفتن دیگه
🤣
وحید یرق پیروزی بلوارابوذر اومد
آپدیت: پیام‌هایی از وصل شدن برق در بعضی از مناطق داره میاد.
همز‌مان خبرگزاری فارس:
قطع برق تعدادی از مناطق تهران؛ دلیل مشخص شد
تعدادی از مناطق تهران از ساعاتی پیش با قطعی برق مواجه شدند.
پیگیری فارس از توانیر مشخص کرد، مشکل فنی در یکی از پست‌های ۲۳٠ شرق تهران علت قطعی برق است.
هم‌اکنون تیم‌های عملیاتی و فنی برای رفع مشکل در محل پست حاضر و درحال حل مسئله هستند.
آپدیت:
همچنان که خیلی‌ها پیام میدن که برق ما وصل نشده یک عده که برقشون وصل شده بود هم دارند پیام میدن که دوباره قطع شد. شاید به خاطر همون تعمیراته.
آپدیت ۰۰:۴۰ بامداد یکشنبه:
خبرگزاری تسنیم:
برق شرق تهران وصل شد
رجبی‌مشهدی، معاون وزیر نیرو از رفع خاموشی‌های شرق تهران خبر داد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/76711" target="_blank">📅 20:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76710">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckPmzw1XJicCEV4n0a6LA18vC28DA7k0E7qhJ4Sdh8kjxUn8Pbx_vWuN-fm615bVZRgmuC0s0jrx_pkZ-yHaC2rMBWWlqBLnW80LR2Py1F_4MicwhBqGA-zg6RNlpRkJF8N8TkjTDXAlnec7KhMgzt6gCKmaElZzmuH8GlrSUJw2Wucp1Mp7Q2H4QVNDfBt8FYh1MXJmqpMwxrs7scX7mNgD71OkKONfdEuqtiiwY_a_Iqnqt4cQqir_DIu5rTKgIWy9KgpZj_4plVFoSTfVzdrHlgWXtguLOpRZsixF8TVUv3-RMYa-rIgDawcnis8M2ie7jcELnFzV-n5-SWYjCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش رسانه‌های ایران ارائه خدمات بعضی از بانک‌ها از صبح امروز (شنبه، ۶ تیر ۱۴۰۵) دوباره مختل شده است؛ خبرگزاری ایسنا به بانک‌های ملی و صادرات در این زمینه اشاره کرده است.
شرکت خدمات انفورماتیک این اختلال را مرتبط با حمله سایبری دانسته است. در اطلاعیه این شرکت آمده است:
بررسی‌های فنی نشان می‌دهد این اختلال در امتداد آثار حمله سایبری پیشین بر زیرساخت‌های فنی و سامانه‌های متمرکز بانکی پدید آمده است.
هفته گذشته اعلام شد تمامی اختلال‌های پیش آمده در بانک‌های تجارت، ملی و صادرات برطرف شده است.
اختلال هفته پیش باعث شده بود که در بعضی موارد، حتی انجام عملیات خرید با کارت‌های بانکی هم امکان‌پذیر نباشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/76710" target="_blank">📅 17:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76709">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRX_M9LTivq2hwSxS5ZYCkwjocp8McE0a-BbMpI2iqAXMnhjJ6j9Lq6Kh_s9mB4otwdSXNWBCd09xPmWMsiZLYKJ9cF_sQ0oxwjJ6bmSX6xqv9i_aA5Z9PvljHD74HX8qX0l3mCTrVewJQ40MyMsrN_1PgzaxuXfZNa59WhwWychm-QCAZ7kDJVZL7AKifrH3YxVEaZs3ebdPxkeTj1Y87veJTKWXSsa2kYnYgs4_An9Ys8KwC19uMvQrnz8xF2JeXHCst6DuhD7lvq7lOTRMyPWev8ugpHyuAQa6_2_oEWnXBSBpcSYj5twHao6aC6fV2zoYs9z0t0eEM4pGd0y0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهنام گلخنی، پدر احمد گلخنی، از جان‌باختگان اعتراضات دی‌ماه ۱۴۰۴، روز چهارشنبه ۴ تیرماه در باغباد‌ران از توابع استان اصفهان بازداشت شده و با وجود وعده آزادی، همچنان در بازداشت به سر می‌برد.
کمیته پیگیری خبر داد آقای گلخنی پس از آن بازداشت شد که
در استوری اینستاگرام خود از مردم دعوت کرده بود تا ظهر عاشورا بر سر مزار جان‌باختگان اعتراضات حضور پیدا کنند.
بنابر این خبر قرار بود او روز شنبه ۶ تیرماه آزاد شود، اما با گذشت این موعد، همچنان در بازداشت است و اطلاعی از وضعیت پرونده یا اتهام‌های احتمالی او منتشر نشده است.
احمدرضا (احمد) گلخنی، شهروند ۳۷ تا ۳۹ ساله اهل باغبادران، در جریان اعتراضات دی‌ماه ۱۴۰۴ جان باخت. او مقابل کلانتری باغبادران هدف شلیک مستقیم قرار گرفته بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/76709" target="_blank">📅 17:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76708">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phi3GXqCRONjwK9IdLSTppob4cCCnRzSi_b7mqMNC4KhrwbKyn6tsF0000iaeyb5oJiymFtZ0oBc5QdA5WGeHW0Gfm2uR4Yd1qqG4atIFmOWaVAf6_WWkSlgX3kWiLspnx_7xh7YgaAwz4cUw6-TtCehZhkySM-YT-2t8FoUmzAHvJmj6Tbe3KLGo9xEes_luOXaTw6F7DqBDYhok9XrHMyIk6zedf_BLuqAAtfx3khjta5t32XsNIORdN4chIieOtCNERnkGz_2OESXPMjA-alXlbOO0eftPAfNcFhdSVznfAS5hSU6nrXJK8kxKBskqOXnC_13Evx-Cyk4ec8E0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل شرکت شهر فرودگاهی امام خمینی از برقراری دوباره پروازهای میان ایران و امارات تا پایان هفته جاری خبر داد و گفت: ایرلاین‌های داخلی مقدمات راه‌اندازی مجدد مسیر دوبی را فراهم کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/76708" target="_blank">📅 17:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76707">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cnIdSqJtyu8TNMUaZEIh0nM_IBx_GGfBrGr92fl8Onn2OL0YbhbNvQm18lTturszxrlajxE_gRV59vYkRhnMuccNp9wIamtHfwOmd3_zMoKMPCltZSFaQYyO3LVoXVLJSnBJ2GOVNHeQ6SsY5JCBqOdj4CqMNvc1E3x_tjTK4tztoVQDsMvbFbDQMkZmInn3D0vAjgXQSupgiI3OX2AESb_x0JYOvZDZ76sFqMVmFt67ycDJwWCS2aCWlzwMMC9deqz0BQpvt9z07U1-IYJjw78kIX2qkpGWSWzs5d_t97onwuCy4f2ojv-Ub2LsoL3EV36Zt_dx_fp6LqATjZwnEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه بحرین در بیانیه‌ای اعلام کرد جمهوری اسلامی بامداد شنبه با چند پهپاد به خاک این کشور حمله کرده است. این وزارتخانه با محکوم کردن این حمله، آن را نقض حاکمیت بحرین و تعهدات جمهوری اسلامی بر اساس تفاهم‌نامه اسلام‌آباد با آمریکا دانست.
در این بیانیه آمده است حمله پهپادی، نقض آشکار حاکمیت بحرین، تهدیدی علیه امنیت شهروندان و ساکنان این کشور و مغایر با قوانین و عرف‌های بین‌المللی است. وزارت خارجه بحرین همچنین اعلام کرد ادامه حملات جمهوری اسلامی، هم‌زمان با تلاش‌های منطقه‌ای و بین‌المللی برای کاهش تنش، روند صلح را تضعیف می‌کند و نشان‌دهنده رویکردی برای بی‌ثبات کردن منطقه است.
وزارت خارجه بحرین با اشاره به تفاهم‌نامه اسلام‌آباد افزود جمهوری اسلامی متعهد به توقف دائمی عملیات نظامی و احترام به حاکمیت کشورهای منطقه شده بود، اما حمله اخیر به گفته این وزارتخانه، نشان می‌دهد تهران به تعهدات خود و جامعه بین‌المللی پایبند نبوده است.
بحرین همچنین با تاکید بر حق خود برای دفاع از حاکمیت، امنیت و ثباتش، از شورای امنیت سازمان ملل خواست مسئولیت خود را در اجرای قطعنامه ۲۸۱۷ و پاسخگو کردن عامل این حمله بر عهده بگیرد.
@
VahidOOnLine
یک مقام آمریکایی که نخواست نامش فاش شود، به وال‌استریت ژورنال گفت حمله بامداد شنبه، ششم تیرماه ایران به بحرین شامل دو پهپاد انتحاری (یک‌طرفه) بوده است.
این مقام مسئول اظهار داشت که یکی از پهپادها توسط یک سامانه پدافند هوایی زمین‌پایه سرنگون شد و پهپاد دیگر بدون ایجاد هیچ‌گونه خسارت یا تلفاتی، در محوطه یک فرودگاه دورافتاده فرود آمد.
همچنین گزارش شده است که یک پهپاد انتحاری به نفتکشی حامل دو میلیون بشکه نفت خام اصابت کرده و نیروهای آمریکایی دو پهپاد دیگر را که کشتی‌های تجاری را هدف قرار داده بودند، سرنگون کرده‌اند.
@
VahidOOnLine
پس از اعلام دولت بحرین مبنی بر حمله پهپادی جمهوری اسلامی ایران به خاک این کشور در روز شنبه ششم تیرماه، کشورهای حوزه خلیج فارس این اقدام را به شدت محکوم کردند.
این حمله ساعاتی پس از آن رخ داد که سپاه پاسداران از هدف قرار دادن مواضع نظامی آمریکا در پاسخ به حملات سنتکام در بندر سیریک خبر داده بود.
وزارت امور خارجه امارات با صدور بیانیه‌ای، این حملات را «نقض فاحش» حاکمیت بحرین و تهدیدی برای امنیت منطقه توصیف کرد.
وزارت امور خارجه قطر نیز ضمن محکومیت این اقدام، بر لزوم پرهیز از پیامدهای این حملات «غیرموجه» و تداوم مسیر دیپلماسی برای حفظ دستاوردهای یادداشت تفاهم اخیر تأکید کرد.
در همین حال، وزارت امور خارجه کویت این تجاوزات را تضعیف‌کننده خطرناک تلاش‌ها برای صلح دانست و بر همبستگی کامل خود با بحرین تأکید کرد. جاسم محمد البدیوی، دبیرکل شورای همکاری خلیج فارس (GCC) نیز این حملات «خائنانه» را که به گفته وی زیرساخت‌های غیرنظامی را هدف قرار داده، به شدت محکوم کرد. این تنش‌ها در حالی اوج گرفته که از دو شب پیش و با حمله سپاه به یک کشتی باری سنگاپوری، فضای امنیتی در تنگه هرمز به‌شدت بحرانی شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/76707" target="_blank">📅 17:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76706">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LouBH08b_s8FdlEdCib6GTU3iNtOIIYsbv41gGrtfFrfQXfpnzwjNB6ura0UJ7jE4MzrqGMWE9yOlBln2-u51ILim6GU74U2jWt4Mjqjg28KheaKG7KqhDddskVAKXL4WtJ2hHs3nidkaapIiqgPkUA4TAsydvmik2Ien8IC_98BKPdu8x9YRPQLJ7YFBKRufJ_vuuoi1I5IxxZ-wS6NPtCmno8ixlvYQSwvXEpj4w_wCZNRftfz1FCi2qtW6GmpMdRKsdFvfMDX2Ns6fZRa-xo6vofQ2hkIatEFyK5F5li87pJ2SmTN1vtiQhgckHpnnCkL-r4sWUuCVcIhKVfKGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ می‌گوید بررسی‌های داخلی وزارت دفاع آمریکا نشان می‌دهد مجموعه‌ای از نقص‌ها در سامانه‌های اطلاعاتی و هدف‌گیری ارتش این کشور ممکن است در حملهٔ موشکی به مدرسه میناب نقش داشته باشد.
بر اساس گزارش بلومبرگ که روز جمعه ششم تیر منتشر شد، یک تحلیلگر اطلاعاتی متوجه شده بود ساختمانی که در پایگاه دادهٔ ارتش آمریکا به‌عنوان یک تأسیسات نظامی ثبت شده بود، در واقع به دبستان تبدیل شده است.
به‌نوشتهٔ بلومبرگ، منابع آگاه گفته‌اند این ارزیابی در سال ۲۰۱۹ در یک سامانهٔ دیجیتال ثبت شد، اما آن سامانه به پایگاه دادهٔ رسمی هدف‌گیری ارتش متصل نبود.
مقام‌های رسمی آمریکا تا کنون جزئیات این گزارش را تأیید یا رد نکرده‌اند.
بلومبرگ می‌نویسد تحقیقات پنتاگون همچنین بر ضعف‌های دیرینهٔ سامانه‌های اطلاعاتی ارتش آمریکا از جمله استفاده از پایگاه‌های دادهٔ قدیمی و نبودِ ارتباط کامل میان سامانه‌های مختلف متمرکز است. این گزارش می‌افزاید هنوز مشخص نیست فرماندهی مرکزی ارتش آمریکا، سنتکام، پیش از حمله از فرایند تکمیلی بازبینی اهداف استفاده کرده است یا نه.
وزارت دفاع آمریکا اعلام کرده است تحقیقات دربارهٔ این حمله همچنان ادامه دارد و جزئیات تازه‌ای ارائه نکرده است. دونالد ترامپ نیز گفته است ممکن است هرگز مشخص نشود چه کسی مقصر بوده و خود او هنوز مدرکی ندیده که قانعش کند آمریکا مقصر بوده است.
ایران می‌گوید در حملهٔ هوایی به مدرسهٔ میناب که ۹ اسفند پارسال در نخستین روز حملات آمریکا و اسرائیل به ایران صورت گرفت، دست‌کم ۱۷۵ نفر از جمله ۱۶۸ دانش‌آموز کشته شدند. شورای تشکل‌های صنفی فرهنگیان تأیید کرده که در این حمله بیش از ۱۰۸ دانش‌آموز کشته شده‌اند و گفته است معلمان هم در میان قربانیان این حمله بوده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/76706" target="_blank">📅 17:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76705">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WkZiCZNQsiYOns67y8CWgEO5bmlGFODm6IsaEYPpg4Bo0Gk66W1HA2z4-ar7JmYk7gf14Sa6l4VgCXW_x4c6THsTxnzvQAQ_Q8PW8zUYqRBnBR_lVrb9FTX6MFBOQKf0Urf79WHsqQCMkHnyh56iKCvjyije12ogj61nrKZJCAKUNmf4_UUzBN231KPZvd-LqQK4fH8Itz8oUh4rTuOniXif9ZL1Y3fE-nG_C8M0f8ceDDeE0-w8pwa-IkU8qdGAZkWdWi4FX5hFY4keR9sSI60FI0Dek3ZIKtKsFWq2KUX8xussIcTrJRk7bWe5-VzwqEAhE-F0kCBIUzwA37k7ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"یاسین محمودی، نوجوان ۱۶ ساله و اهل رفسنجان در استان کرمان، در جریان اعتراضات مردمی این شهر با شلیک مستقیم نیروهای حکومتی جان خود را از دست داده است.
بنابر اطلاع ایران‌وایر، یاسین محمودی روز جمعه ۱۹ دی‌ماه ۱۴۰۴ در خیابان طالقانی، ابتدای سه‌راه امیرکبیر رفسنجان، هدف شلیک مستقیم نیروهای حکومتی قرار گرفت.
گلوله به ناحیه شکم این نوجوان اصابت کرد و او بر اثر شدت جراحات جان باخت."
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/76705" target="_blank">📅 17:06 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
