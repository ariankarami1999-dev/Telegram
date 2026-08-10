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
<img src="https://cdn4.telesco.pe/file/iIZgDxNvE0QYsCsbx9tvvJPpU8TjLLmiPtTHZWVOwkTatOxDce8exvwbEUWYnDi-q-idtG-4i5sDIT2j-zg1zMqEYv0WTvUPD2s354qdK22Rl1whXjBpSkHHirSmOvEuCicjlFTMMYuMbR1ENXK9KlSxN45IApbJelZx18fCPE1zIiwOPnxDKoo5s7IndSVvRUh5kNNfVU46e74ustR9rqBDBGGEq7DrfU4VxyIWjSZH9DE5ukwW8j56zehYYsRMM1Yzr6Ml3sdfi5jK1rHOfw5YTv2X7tJzDCzPjLHqRsowcb8mDTs1kh-YsfeD0b2xZmlfw1HjyyaOheq_8jSd1A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 631K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-19 17:44:11</div>
<hr>

<div class="tg-post" id="msg-27467">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Az1aHsLwF8T13YKKXs1vjKJpvMibUz_bVsorM91QlefTlfLeBQI_7wEfLxnsHkuZ3UwEjQ9WgdbiHCfRlnhLAif1pMSQepZUuzSTa6sWJ8OjMoWp22ry5-aQeitSZ3F-uRo305TiyHxAmgDRso4HDminmRd1ZO0o9MF6MhYddE3StWbNGefyW_Agk8LZZjnZ3eJZA6bWk1jTiqX5-ErxuE3AVPR1tMYtJWQkv_gpSMryNC5FGH-EKWfJLqWmitcME4J-OzQ6bpP5g-p_kMHmrhXZ4SGLo228u6DJFl2psRXvWVjtO6Fs7QmYHDc4SFGFTiGi2WOPKBGfV1Kft99p1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇳🇱
بااعلام‌باشگاه‌بارسلونا؛ فرانکی دی‌یونگ کاپیتان هلندی آبی اناری ها رباط صلیبی پاره کرده و حدود 6 الی 9 ماه دوباره دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/persiana_Soccer/27467" target="_blank">📅 17:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27466">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESoL7HBkK3H4ApKyfy3Y1_1Dp7OLaKd0WVRScSvFPrDEEW7_dwXzuMnKVh5WTu4zG12cTgmM7MgN1r_0D0VXYcpc2yQqZIxJsTFkpEVA0cSkQihMnI3Vht9b3sKwNMdXUHZm10dFw_yXZhWPuR-DeSFX3LIhcXRSHo8lMP7mbvlQ5uXImFZmDELDW-LG0kQn12E3xg9xyTnM0bX3fO9cny_wfOKUetbZLUP0Wjq5pL4xQvhOePEew2J-rovihSWY4ahi0p-cA_0sxgXVmXRw0tfYHbiKIc6r-p9aFHxPhRcV2aaa5bcDLa5wbbqiTeuEHXWo-8I_PfRVWRY5C1sejg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه‌دیدارهای هفته‌اول رقابت‌های فصل جدید لیگ برتر؛ تنها چهار روز تا آغاز دوره جدید رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/persiana_Soccer/27466" target="_blank">📅 17:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27465">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1ObXm_BNL25YPWwiSEg4hLYmpN4BpT3oib6veFiYaypQ8qTshW_FySJY9l2vG61VQdj-PoN-yHjYenm0m81Yc2FpIA-4zGS6-NnvMclU54hZXE1ivowcPX_aJ67ZQHEpbH3GRuSvoRAQStKoZilMFgIWtVrnvuifhmy4JSLMNNrdSdkhzCuM0Xh6xCHD7DXjCwAom1KLcUcFDMJpV--MWRiguaLyJDiwQJ7aA_FJ85fHkBrxqJEWH3UF8KRj4GSpbWcNeHP3YU7k6aiewtHqcnoS_FZDgubfDB0ao5Xrjp3qOUk-YENMafI7dfk_uPw2Q4iSgq6E9G2pXJblWwiUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا جهانبخش کاپیتان 33 ساله تیم‌ملی بازم قید حضور در لیگ برتر رو زد و با قراردادی یک ساله به ارزش 400 هزار دلار به اکسلسیور هلند پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/27465" target="_blank">📅 17:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27464">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c1c733196.mp4?token=nlBF8xyEYw6tGXyKwfPHM0r9iRq2FRlJamK5-HYurchSHJF4xf8GBEBFLjUg-7P9ZpZ5hHHLyund2OjXvMSpyAn6kCP5Yh7evOkCfv2UQOciyCZa76liEnkLQhxDQAPJ5VANoapmGnmg14UMWImKr9hy6xvn0v_ER854xnEXicnsrDcXSD7pRiIQ-eci4dquXgVD_pVpZPyo0q6me76WTV67aPrf7cIEHyo5Hx8VXB93pUNTKp4Y7TTULsv7CJe5trEIboJf4aUPbej2LcUUsBfJLDSEGtdYotBbDVpZE3M2nHdXFYNlWrDRMgDtONCDLn9wnU7STbFQS6IxCd62ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c1c733196.mp4?token=nlBF8xyEYw6tGXyKwfPHM0r9iRq2FRlJamK5-HYurchSHJF4xf8GBEBFLjUg-7P9ZpZ5hHHLyund2OjXvMSpyAn6kCP5Yh7evOkCfv2UQOciyCZa76liEnkLQhxDQAPJ5VANoapmGnmg14UMWImKr9hy6xvn0v_ER854xnEXicnsrDcXSD7pRiIQ-eci4dquXgVD_pVpZPyo0q6me76WTV67aPrf7cIEHyo5Hx8VXB93pUNTKp4Y7TTULsv7CJe5trEIboJf4aUPbej2LcUUsBfJLDSEGtdYotBbDVpZE3M2nHdXFYNlWrDRMgDtONCDLn9wnU7STbFQS6IxCd62ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
توضیحاتی درباره کودتا شبانه بزرگان تراکتور که منجر به برکناری محمد ربیعی و آوردن نکونام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/27464" target="_blank">📅 16:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27463">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyJvf0jsbhMiskk-ZsVc7Jzuml-X1wONcS-_6rCm_IwSAgL-M_TTXO1CHGX3JoLtbSmEM3ZskmP4tJkugAgqyoSp2DtYRuzsBuPNQu0nPzda8Dg3VEFZ-MWy9Z5qbmZqswDK2HqUnoz92mw83ENIPKV2ihMB_iMauJm_s-PH4OtGYhpit69GPKhmC5yuvaaaaOTChkKHxJvuZJLz6qBvJg8j6pe1mKAQNBVICNnuHQkSd6FfwgrwqxXsKUtZ2ksdIDiixTlGsp6w6DBuzp7L738IAzcpyNLkL4_g5Kw3LaETfL6PvWE3P5YOJi8fphpg2ol3piYIfr6dZY5gG0T49A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پاسخ علیرضا جهانبخش به سوال قیاسی به اینکه در آینده به کدوم تیم استقلال یا پرسپولیس میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/27463" target="_blank">📅 16:28 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27462">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LV0eFiJ2bxBi-ntJD168JpscDvxebI4lIPcPnHwhF4QW_VCybyfDXzF8idRjTJQmViR_GWLySHyyIK75rCHY4TfdOwtn2OOA1hFOAWpRe4Dzw9luXl181sXwugE7EvcElLTDgiePtPrm4de6-zeA_wOnhiQb_XAfRpYqzffINibqv0JS5xkfp1wHA2Wc8W90eu0-gWIM2gmYOh4t74Q3Qc-C_ICvbdlbXyiDXm8i-HmynO4j3waQlTyCFlGs2ouukYwYK8LW-lVKLQnuNS3lmPrkpu-Wloc4PFGYh2ln56ZJxTtRmC3M1f3pUTyz1Rjo-_z7SKNd3UmtwuxnPdyegA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب احتمالی بارسلونا برای فصل جدید رقابت ها در صورت جذب قطعی رودری و خولیان آلوارز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/27462" target="_blank">📅 16:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27461">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0q_lRkXAUmIOlq2aXon-r-TbSZWOiTOtY6AA0q7c5MARqWPmIZpJ96MlC7kjkQxaUzzEgTFvJZwDiNrI-kSdixunxWNGR_unyHgvjkjjQci3c81biDFkIF5RnRraSR5yIdehGpj5fewZbM9tx6Xbr_fFFBXSZEEinQm3ClybSHBnil5enBaM7dVHJSjnrwsQ5XdC_DGgJroP6cdSFR3IiSvBdLzXn2ON-IkIMWBkX0G4M2n5hB9voxdJzy438UQLSCiMMvwcZPDhsFX3FFJLav2TAJVo6ytx0n-ITD67iE0dSO4y_papMZG0c-UAX2TwcerUia4iLrqzpu9BAIopQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
باتاییدیه مایکل کریک؛ مارکوس رشفورد در تیم منچستریونایتد ماندنی‌شد و شماره 14 شیاطین سرخ درفصل آینده رقایت‌ها نیز برتن خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/27461" target="_blank">📅 15:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27460">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QA5UWy5DQokMQUhLpkRvIIIO1EnR4eW-N2EhK7NktqjPCjgeDHLaBjPQ7dTCVS3KLdzUh0C4HJI7HVz2mPwuzg1llrA07vhbo9-rbGW0iKdYRqTk_qoUJYuoiWQHfNWD_S7u26yuB_KjR3WSRjxF9J3ky-jrRGqLQBVBwpNLHJGFfaki9gzD4bb8RVXO4EtIJBAHurj_YGPCz7G3HGO3PXVgE2TGvdbKSY-mI2rBiHt-freys-7ZP6sG38E1TBNR9rjv-Qu5Nm_kPqboZn70XCaZ4KcnNIi0M6N00M2Jk4L71HoufcVf5_ffizsLfGNGDEUwIWEo2zU5ia5dGmBufQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
خواکین گیل مربی اسپانیایی جدید تیم استقلال فرداظهر برای‌ عقدقرارداد و رونمایی باپیراهن آبی‌ها وارد تهران‌خواهدشد. خواکین‌اسپانیایی دستیار دوم بختیاری‌زاده و مربی تمرین‌دهنده آبی‌ها خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/27460" target="_blank">📅 15:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27459">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOaq6jnTJD8syukBk0vCLddJYYqIcOf6HpSr7_BYvf13NPmTpkmFG9epiEtMz3ftrvGqmbP5kkKFmIhJKTv3MSISTcoR5v3NHzPIKeyuYQcZHB9K9IP-bWcxfKi5d4vae_DGCX6-OLQUSFRfaVUqqYy0QRpATnejEAQHmmHRu4y9JR6Wl1Aahz6hb9_sRWuMG_AxaWnNng4nHDWLqbpeIe_iZ9NerhrK5S0ow5s2uGYYNSTorp1P4z3M_0mSVWtmieaG69qZL9e8qTyWVyRQ3BY9KRzhgezjVvfzPmBkIxMQQMHMuNIWVvoUscZx9WDwxH6IM5sxHhkAHC2hUCw-AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇹
اقدام ایرانی طور فدراسیون ایتالیا؛ از پپ گواردیولا، کارلو آنجلوتی و روبرتو مانچینی رسید به آندره‌آ پیرلو! پیرلو با عقدقراردادی‌تاپایان جام جهانی 2030 به‌عنوان سرمربی تیم ملی ایتالیا انتخاب شد. البته در صورت ناکامی در یورو برکنار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/27459" target="_blank">📅 15:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27458">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/643163ded4.mp4?token=QZFDzwDWaVqVXkO9wfAgdgxm75YY5WD1Yz6kgxr0yTNNElZE5Ci7pf-bq7ZHBDX0prsgWwNtJxwxZqehMcqdXcUxWyDQYtI5R4N0RqkvqzNx8crhjX6xy7d3OIuGoOx0IGFdJLv4K5Xr8sSDy2HQG4QZq114hq4ea4rOL0jDGvyLwK-94FsZmB8wcGfyzXIXCSisO8NKBPKjA7B2Nzn5aZBcOBtgeGABjcD4d8GUpBmAuzqwhEEkYakhHx5iUVUA5KUMfJ5eInlYHKgfTlaIdVtynHm0X7taPC3ugd3KExBWlPV0Xt520AOAqGE0tBbHj-KVXRUXxmXpsh6-Thl2Zxa9gjjqrvfTHsFh60UfbhL2GHZKmV7j1ghXkVYkUT1II_-dr6jQc9POMndNzHp6ntMz1rEu6C1gyhUqpaFlyTGIwHyEzaKHlC9RtxFx8VZbCaKmwNN_BGmbShAWucwpM6UG-1mOQE_UP3Ml-2Q7cyY3MPwSVNFZwRXXr-cPAfhd_PkJ19N53LBvFqDgr0jaIBiVWWUa7KVtUKRihjyoMp00n_vJstILHrIZkDqx3A9XA-tDDnVi93OMa3zW-JXoe7H3NKfWQcCl4enjA5ZEBL4hFkDBdltKwzAT2ZLKkqt5caqMzyPhLj9hWgtOGYam8zqaNrEpqPe-SzV-rEISIWM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/643163ded4.mp4?token=QZFDzwDWaVqVXkO9wfAgdgxm75YY5WD1Yz6kgxr0yTNNElZE5Ci7pf-bq7ZHBDX0prsgWwNtJxwxZqehMcqdXcUxWyDQYtI5R4N0RqkvqzNx8crhjX6xy7d3OIuGoOx0IGFdJLv4K5Xr8sSDy2HQG4QZq114hq4ea4rOL0jDGvyLwK-94FsZmB8wcGfyzXIXCSisO8NKBPKjA7B2Nzn5aZBcOBtgeGABjcD4d8GUpBmAuzqwhEEkYakhHx5iUVUA5KUMfJ5eInlYHKgfTlaIdVtynHm0X7taPC3ugd3KExBWlPV0Xt520AOAqGE0tBbHj-KVXRUXxmXpsh6-Thl2Zxa9gjjqrvfTHsFh60UfbhL2GHZKmV7j1ghXkVYkUT1II_-dr6jQc9POMndNzHp6ntMz1rEu6C1gyhUqpaFlyTGIwHyEzaKHlC9RtxFx8VZbCaKmwNN_BGmbShAWucwpM6UG-1mOQE_UP3Ml-2Q7cyY3MPwSVNFZwRXXr-cPAfhd_PkJ19N53LBvFqDgr0jaIBiVWWUa7KVtUKRihjyoMp00n_vJstILHrIZkDqx3A9XA-tDDnVi93OMa3zW-JXoe7H3NKfWQcCl4enjA5ZEBL4hFkDBdltKwzAT2ZLKkqt5caqMzyPhLj9hWgtOGYam8zqaNrEpqPe-SzV-rEISIWM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دریک در یک برنامه دوست‌یابی با حضور ۲۰ دختر شرکت کرد؛ اون در نهایت از بین این ۲۰ نفر، یک‌دخترروانتخاب‌کرد و حسابی ازش خوشش اومد و حتی براش واق واق کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/27458" target="_blank">📅 14:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27457">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e350019bc.mp4?token=e2N6DF_z25esoIM4r-h5DiWwdEtdw4GvsUrQFrj6goI9KrTeREWBgEv-lzpUUtaOTFFAGP2F9l8tvfLjMLFT9eKj7J3yaMqiyOI02RMu4pbiJnMhQN2szk8nsZyBF93rSfOQLyDhrofhUm83orMTPo71NdWRZzDi5vYh4ON4CVd0eM12Qq-940DyIThVTEXYK3J2fOrdWSwyLZeUY8FczUNMcmXAZxr_54w92wZSxH58b4GOdneIJmUm3UaIJexCMkfXSybsdUwhNBwu0jJMct2HFIUviJu1rE4GClY9Tdw0Q_U3SemQoIHYZcS3-tfiQf0suAJsdSYk6BbShS4vdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e350019bc.mp4?token=e2N6DF_z25esoIM4r-h5DiWwdEtdw4GvsUrQFrj6goI9KrTeREWBgEv-lzpUUtaOTFFAGP2F9l8tvfLjMLFT9eKj7J3yaMqiyOI02RMu4pbiJnMhQN2szk8nsZyBF93rSfOQLyDhrofhUm83orMTPo71NdWRZzDi5vYh4ON4CVd0eM12Qq-940DyIThVTEXYK3J2fOrdWSwyLZeUY8FczUNMcmXAZxr_54w92wZSxH58b4GOdneIJmUm3UaIJexCMkfXSybsdUwhNBwu0jJMct2HFIUviJu1rE4GClY9Tdw0Q_U3SemQoIHYZcS3-tfiQf0suAJsdSYk6BbShS4vdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
«رودریگو دی‌پائول»ستاره‌آرژانتینی در بازی بامداد امروز اینترمیامی‌روی‌یک‌شوت تماشایی موفق به باز کردن دروازه حریف‌شد و به این شکل گلش رو به لیونل مسی و پدر از دست رفته او تقدیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/27457" target="_blank">📅 14:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27456">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Az_fLstgPO2TkkkgkWHY-t5QCudt83dLioKPhgzX-kY7J-9iHAX845AT2JQDwiltmIFdaBfmlw7_ncqgoKMoaX9hMw6jL3i_-Yq1dK1Fut0PP74SZlayCNVAX0nwaMREDSubN1sq5oraVfiT2Nuu4e4Ipd1bfZLawFPe_YQK0Mes0Mk2GBJJMxREFllkO2neeUm2VELYu5oyrN60cse2o64PnCGRO487DF1z0REfq0ejQFoujzqRFYokEtHxyz2eXy2jDxTX1XPUZ_wCRqHL4gJVywmZM9u_Vk_zep1CFU0LVNlQCMYsjlsEbEBsUGmk5E1vGw0vgRbHZVeIoX0W8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
کار انتقال فران تورس به باشگاه پاری سن ژرمن نهایی شده و این باشگاه بزودی با فعال کردن بندفسخ قراردادش از او رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/27456" target="_blank">📅 14:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27455">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FC15hdUvlbD3iRvfoh_goMFaIYmfdP2s4X6NQ5dg4R2ly0hA6Uydu15jgGfaSceIcY4S18ltMuCKHQCbtk4e6hj5pJEC9SMH7w6X2GstnNLZq6zGZD6R8XkvQl1g0HMASYVBJsf_5EHfqk0MG4dBqv3h_2dLPnpovtwR2tdbAlMXpaI7_zlTq809V2dOeXrl_3xG7g-4PI_LLU2DB2zUvzZt6CFblVq3csvrYC3_pybL03cYKUkpOjk3h715jcNzyJ9WRBGs2Z5MlA9UDdRRNqznJjIikyKY36KwslKGUv2BAe-hgHJPB1HwtIl4PjDBsKFLdIVs3WIZ22QuKH12Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🟡
#تکمیلی #اختصاصی_پرشیانا؛ فردا جلسه‌ای مهم بین مدیران دوباشگاه تراکتور و سپاهان بر سر انتقال آرش رضاوند به‌جمع پرشورها و پیوستن تومیسلاو اشتراکال به سپاهان برگزارخواهدشد. طبق شنیده های پرشیانا این انتقال فردا نهایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/27455" target="_blank">📅 14:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27454">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e058bdf5.mp4?token=XPjg2XprJaMARnEAiloYelj531_PNJd8LjNFM6PvkExls7W9VYIjepXqeIZwkvnQZdjX4Qhfoa9drCV5N0qYU4Mp1-iwb7ZSIMHlKojhMnilaMSMek1oO0SIMa0FEBLD1BHgUPIBHl3NAW1mFEpA-zRSFybxqxquwhviXZga6vqSgC_XOF_kKIrrl1k4D9UjYEV6CFl-Br1ULvVA_ceIQQpmebul6dOnhDkjJFgqTg0INmx5-jQbf8_iIxto4LN4gtHZWqkf7MN7zTdEOf9EWwXG5Ms-DPPbJkGo_GQ5A8dshGRT7k7X1oQzfhQM6L1jPMfsPWRMJ7JOt82NlmSN7aQl-8F8Qo_hMb1MRA8P-58c60v07kktpBCytJq8-N_9zpl45_ODHV3cHOrX4JFoQaglZrABoVB7d8V5V4MnO6L4tOqJzO1NTdlElEpiArV74dJAyMQrWg38CWYTAtsxS_su0HrzYN7CfjZQ1PpozpQ2fSMrB2T4bcpx6xhKrth2wFt1zRWnI_zUZ2FbV7eCJfaeBxBEm8_MZ9cF7HhoTiY3axMSVuom4xjkjlUyBZxGTYyNxD56zleKXFCVna1z99fmHGyB-mXosrJlNyNFOPFSbPvnWytdorPMbw-GLce_2DN6dOaTPGcKkLSB4rrDLHIcxGPyDGfF8_Gknkdyl6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e058bdf5.mp4?token=XPjg2XprJaMARnEAiloYelj531_PNJd8LjNFM6PvkExls7W9VYIjepXqeIZwkvnQZdjX4Qhfoa9drCV5N0qYU4Mp1-iwb7ZSIMHlKojhMnilaMSMek1oO0SIMa0FEBLD1BHgUPIBHl3NAW1mFEpA-zRSFybxqxquwhviXZga6vqSgC_XOF_kKIrrl1k4D9UjYEV6CFl-Br1ULvVA_ceIQQpmebul6dOnhDkjJFgqTg0INmx5-jQbf8_iIxto4LN4gtHZWqkf7MN7zTdEOf9EWwXG5Ms-DPPbJkGo_GQ5A8dshGRT7k7X1oQzfhQM6L1jPMfsPWRMJ7JOt82NlmSN7aQl-8F8Qo_hMb1MRA8P-58c60v07kktpBCytJq8-N_9zpl45_ODHV3cHOrX4JFoQaglZrABoVB7d8V5V4MnO6L4tOqJzO1NTdlElEpiArV74dJAyMQrWg38CWYTAtsxS_su0HrzYN7CfjZQ1PpozpQ2fSMrB2T4bcpx6xhKrth2wFt1zRWnI_zUZ2FbV7eCJfaeBxBEm8_MZ9cF7HhoTiY3axMSVuom4xjkjlUyBZxGTYyNxD56zleKXFCVna1z99fmHGyB-mXosrJlNyNFOPFSbPvnWytdorPMbw-GLce_2DN6dOaTPGcKkLSB4rrDLHIcxGPyDGfF8_Gknkdyl6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
ایرانی بس کن؛ یه بار دیگه ثابت شد که تو مسخره بازی رتبه ۱ دنیا هستیم بااختلاف کهکشانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/27454" target="_blank">📅 14:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27453">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/454a762bef.mp4?token=e459AldqJpAKmgEYYh9lVf488sfOnjlkULhvmkbbWjlGakK2i7QFYDY5nDWsb0rtDIraEUrWUJpOPrB872B8_E0O-hGhs7ly4mEpAaKpbNh151AVlsnNmCueLShygu9koBOn0nbEn_7rj1dteoDi0cN3KY0xzm9JwLUfJFLBc1E76EjGfHSG1wW2GvqiogVYGdMjRgXlSW9bkkycZGM16KnbXmHSmSuw57edjdf1AgFtAmiTezo2jrMaaKkcD2_GpmyVOeiswBNch78j0TqiW5GXkH3o8780qqIOVJXm-zsLlRs2BIL7GAwPVSN3oG_0vsuYo95KjKOy4BpGF0BmTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/454a762bef.mp4?token=e459AldqJpAKmgEYYh9lVf488sfOnjlkULhvmkbbWjlGakK2i7QFYDY5nDWsb0rtDIraEUrWUJpOPrB872B8_E0O-hGhs7ly4mEpAaKpbNh151AVlsnNmCueLShygu9koBOn0nbEn_7rj1dteoDi0cN3KY0xzm9JwLUfJFLBc1E76EjGfHSG1wW2GvqiogVYGdMjRgXlSW9bkkycZGM16KnbXmHSmSuw57edjdf1AgFtAmiTezo2jrMaaKkcD2_GpmyVOeiswBNch78j0TqiW5GXkH3o8780qqIOVJXm-zsLlRs2BIL7GAwPVSN3oG_0vsuYo95KjKOy4BpGF0BmTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی نوستالژی از درخشش فوق العاده ایسکو ستاره تیم ملی اسپانیا در فصل 2012/13 با پیراهن مالاگا که باعث شد رئال مادرید او رو بخره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/27453" target="_blank">📅 14:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27452">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TERHCM33Oi5l8tR5IiKXFOY_9eE0SQU3QV4wcNQeuk7ZwbRR2453bNA9n-Nn5RRGRYgEtNqFG1e5xSZMc9JflFhQM_uwlEddvD2ZZOO3TwtGITOp1pvT0UQWZh7Ku8OeRaIMfKK2BSCACwIdFY7T7Ch14xRY5YFAIgoiGyVLgp51gnoFgXYZlYWlwEPhS0vpNbQcrwGtrGo2daweHQvPPApPE1xqD6yjgNYWPQ_G2FrfbJPXaf4FhAf8LbcBuj1mo1EZXvTtoB3CS1naiWNlA5Gt0GSp4cE98mumicf1j04ahEv_XlVqS6IM60_Lwwu0lfhN_e-P9KTAsW56xqboww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
همین حالا موجودیتو
🤩
برابر کن
❌
☑️
۲/۵ میلیون شارژ کن ۱۰ میلیون شارژ شو
✅
برای اولین واریز تا 15 شهریور ،
0️⃣
0️⃣
3️⃣
درصد بیشتر در وینرو شارژ شو
🎁
✅
به ازای 3  واریز اول در وینرو به ترتیب 300 ، 150 ، 75 درصد بیشتر شارژ شوید
.
🔊
با شارژ اضافی بدون ریسک بازی کن سرمایتو چند برابر کن
⚡️
🎲
ثبت نام آسان و سریع کلیک کنید
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا
🌟
sr19
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/27452" target="_blank">📅 14:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27451">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I17-XYkUn7DdML-EYt9GHvtdzPWtztLV6qX5K-sfLI5tVbFzwnvXxpcWIdamJ5ONDKjoZ54mTld4Jd1d17Kw-Dp_2XPX6NnfeoBiVTskYvFUNVwVlVanTggT1_DcVvUVhCkM4rS2idflA2IKKl8mTzpwwDIxbBvMpXQn9n18AQSTpTfk0oDBq736yMjFhhdpsx9bS4765AdNmVMnsSkw7yaGwPrh-LcQXQCqxc7uyRzMsmNhiKiay_FwG9YGKItA13r2L_pm49PAn_bYRWrJkEb8E8P6ItERA5u6Dc9HaTMWatGwWDyUM4wlL7lxXvDuwC_18PhZKuHqgp8T75veiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ تنهامانع بازگشت مونیر الحدادی به تیم استقلال مخالفت همسرش‌بابت‌جنگ اخیر هست. منیر الحدادی تا حالا سه پیشنهاد رو بدلیل پایین بودن رقم قرارداد رد کرده. در حال حاضر دو پیشنهاد داره یکی از تیم‌های ترکیه‌ای یکی هم بازگشت به استقلال.
🔵
طبق‌صحبتی‌که باایجنت…</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/27451" target="_blank">📅 13:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27450">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSdxeWhB56o5nOp6ytxO3gi-RMQ3HuAJc74crR-pbC9cSdmZ5VEkUuObf8hcBrYWkKhjPOZkyrRmEe5768OKyLzuQtWhjN1jbMACW4jo7UCw5zHBTD2833jXpyeR_qq1CbUBvw1R_Xo_Ftp-5LIcavoI-rpnhGEO9Oeyq23AvaW6sSLwMKEURr1sVfqvW7ht713awR-LuGvXX5tmTZnBBkGXeaM1-tnn4V_ElddD5f1vehJmoDa2pwwYIrnoL2Xo_AY7XlsPcmXG_XmIJXSVuELd2MXQ7i5BgwqOhXWWYKObuR033Lh2Tq04XQr_mtFfY-3zGZLFaOqCBYXL9eZmsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
تنها دو روز تا فینال سوپرجام اروپا بین دو تیم پاری سن ژرمن قهرمان لیگ‌قهرمانان‌اروپا
🆚
آستون ویلا قهرمان لیگ اروپا؛ چهارشنبه؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/27450" target="_blank">📅 13:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27449">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxilFinKChk0ea6j81iVqImI-NI3ZQEVPxA0OIrP8hNIn9AqShPfQTt4n265kut4I3_eDs8JTNhihRGSjbI1IHzVLLtAX0M75mIIm-HYWByO8A5DVhVXLNmikxi8-xPfTQRJf3F-fuNK9gAHVA_TbNsqhubbaYkAOVZYsFTfjts2YvcfOK3_CRz49TaQfSeny_YOufEbxXoN77hK5RTAyH_bFQNB6bvMOCJn_VsswPzy2Z2Fp0cfUrnwqfGLPOLYje9N8JgCYZ24VuELqcpN4KZ7ePowu9QyYvc0GY-2oZwWFESgHbrv_5frlmIW0Jw4dkc9LFO4q3DQwsTkr-jNpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
عکس های جدید از مراسم ازدواج مرتضی پورعلی‌گنجی؛ مدافع باتجربه سابق پرسپولیس وارد فصل جدیدی از زندگی‌ اش شد و با برگزاری مراسم ازدواج، «بله» را به‌عشق گفت. همسر پورعلی گنجی اصالتا کرمانشاهی است و گویا پزشک هم هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/27449" target="_blank">📅 12:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27447">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pN22ZNVFqwoaJ8yyQWkDLazCumaZADBPn0623Pgt1hKcWYez-mzQrEuEktJljRb_uZ2ubhUy44UBxrZMtgnvKU8R9y8pb3itTtzTbEy7XS_q4WMg-B8imfWPASKnP8RXm7hra1bFGdHkyY8lulLL-TM3NH7SDGglRHazweCbioihkKcXq4SEHi2b9li8RkbzrJ2is4mfAVVyGC2JPO5cnMB6DpyfSI_b5f5hnr4l5326sQzlSxixG_JI5elx0tPehblEk-UfVgn0YUluW9TMWyJSCq5DKMUX40hIbEFJJJyPAkB4pSyaVG0JL3qV92ciY0ucZM7dNHeyIWGg7fP4eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j2FlCSsJHNlK3RMqM4RW5GjXAz8Ju4IK65fXflpzmq1IKgzFLxrufvQOtw-CQfO2d2BMjotq5CTfCYxRACzx85KcHFs34n08Ds8wmKZ-3OAIj0dT_IIjtNrdMbdpwgcJ3JAVAaRR8-U3VuTN8HXyBhbys-F5ErY-Op13xl0vZBWPJnad2WQvZoLA1NB3mIGndgGm0hYdlcI1TXEJFX806dP9CAsFC897VKfC2A8guGO9dm_uFK6_oEh0VJy4kUfjeOPOCGzUNYIWV6PYJ6f1f_aHpxE0XyHnAY_qdX8bKq_XVnW1jg2BlvHlDbtxkpsp9XJH_N5H407rzyKyM59lQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
لوئیس همیلتون در کنار دوس دخترش؛ حالا مشخص‌شدکه همیلتون چجوری به اوج برگشته.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/27447" target="_blank">📅 11:52 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27446">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzcTxbUJlWgboq3rNUhhTOx16EW_m7u5wNSzIsIrsQRClte3n8K2IP2fAHx371oqqiDyan9tP9z__9PetxZwJjswiPcYD6WUOaE5QlePmtxuUiF6zc-E-nn13_wMDwF-t4g9dkqFDO9oRpZJ2AtO5YtVFxPtN8aVDj0J-0UO1piQd-E7j0lj4jqMovYgKtmZTJiJsOLPJ_KH8ujuVGTZMoHU7FezZIJiu1gy4L5gIM5OZ7lr1BvAg81CGHbtLpD1DrBmucgQ4t9KMt3JKb77ayni2jfedgn15M3qSfoDa9L4pn7fxuH8nbojBZQSQMo9EcD2e19evFG3XhY620TkWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛جرارد رومرو خبرنگارنزدیک بارسا و از مامورهای FBI: الان ده‌ها دوربین در سطح شهر مادرید رو زیرنظرگرفتم تا بفهمم خولیان آلوارز دقیقا کجاست. یکی از اعضای تیمم هم با استفاده از هوش مصنوعی درحال‌بررسی پلاک‌خودرو جولیان آلوارزه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/27446" target="_blank">📅 11:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27445">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIlN5dM_jkzcKCetKKHW77KMRE9hRrkMKYMIE9JR9uIXLXMUpGDLaVDMOnRlPIAsh_vEFa65swBuHnOUsvQdwcX5qetNRlFUYGUx8VyEI_imR0KaPXTNCjewXwou-otX4quTUO0R3ZgkbAf7-b-KjbJVLTe1IP0zNXEtr4TkGrNALEsyRMO1t8VMrtdZqIH4xh4PwfwTg8AexF9oWSJRvnXqRBTSzAE9dMlupytfx7OzI7VvqTGp-BtACXgVyFHXo2_fkrvFPurRf1imvoLHjU2Io5_PU9KurcdOSs45j3DSuvk7McetEfGQqqpaCWpykDZ5YlGeX3uwR1FazRvDzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
دوباشگاه‌پرسپولیس‌وتراکتور توافق کردند که محمدقربانی راهی تراکتور شود و محمد مهدی محبی نیزپرسپولیسی‌شود. حالا باشگاه تراکتور هم بزودی از محمد قربانی خرید جدید خود رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/27445" target="_blank">📅 11:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27444">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EG4eo_bKfYvaHKjEM0UkTcSfEQ3OBc7jorwjBE9LAXsAJZCU--uGMkWowFNFu61WjOtm1FCYrp9aAHH5U08sCFnrCORKzpHrqpk-xnDK0lmhAgwUdLijMJpW0w7ZP7kdgEOTmdguPXRcrXonlVUkftYeRd2FpU-5RBXmyFmCs2IqMZSCoBaVGBuwdZevynlz6oDgo5LgTPSqPYp6VdmrXjMWkRqOG279XBN1vXX7RC1oO_KMW_N6345fh2LJF-rEeOC6xgj_0ZZJsqKeAionw6wcAeiUaR23CGuW3Vg1YySFyKZ4cB6PCmncVf-ZhwnyEp4hZlnKTBchLGFO8tScog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇪🇸
🤩
#تکمیلی؛ خولیان آلوارز امروز بار دیگر به مدیریت اتلتیکو گفته هییچ علاقه ای به ماندن در این تیم نداره و از آن‌هاخواهش‌کرده تا با انتقالش به بارسلونا موافقت‌کنند‌. سران بارسا بعد از رونمایی از رودری سراغ نهایی کردن انتقال آلورز خواهند رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/27444" target="_blank">📅 11:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27443">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMbBxijYkq0oJIHGwIXKj3tfFG0lTrMlIh8qtXXptrX8OgdGwzMF8PGip4dk9GCBVDBSs9c7q8QUD1XI-KcN0RB_4nOisygx43Hy6f_Fzx6kegj6Q1YmH1HN9WpkNpuHb7NHm6SE-eE2xLrL9U3CtiYDFbBEff7EFYn76Rs3UTBg7KbNORHYjzCCyEj5XbxPAfEczdZQrGPOLqPGL0w0X334d-9CAxGuk6u-myFxStpXiDu3PmLvwxhXmwa9YNLyyYZnYu8tYlIBPrXtLjWUolTpAMxvVj2ZzLCYJo0S2k9OyvSnGBiAtk23g6YCsa79j3Xux0REIr4ZforUQGzUUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترابزون‌اسپورقراره‌دستمزد ۱۷ میلیون یورویی به محمد صلاح توی این‌سن و سال بده. صلاح این سالها پیشنهادهای زیادی از سعودی داشت. الاتحاد تابستون ۲۰۲۳ بهش حقوق‌هفتگی عجیب و غریب ۲.۴۵ میلیون پوند پیشنهاد داده بود. سال‌گذشته هم یکی دو تا تیم عربستانی دیگه بهش مبالغ…</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/27443" target="_blank">📅 10:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27442">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WuiW5i_tJ7L98z0kYKidNY9XbtansARQBIhznCxHuW2geo_PM1-NRiM54dv3qS06k44xm9GWw9XtkB13P30lW9RJZ632_83q0tSaKtcuPd2GYidM00gQWSzUIqUZ-EyL65FeVOZWLvlbXTwDIccPBTuBDmV2DRNuezuVQqpzA7csfO3YePsiH-gTMBfFZxvmVd1AB6QtymtThgnHjCnPBcwU6MX_WwppYRICoWfD56libmRk5EU9QISv_8FuqJX5nt4LAXfsvh5hxheg7s7ibsQM2w9th31B1WYxmDXqvGAgwy31XNnm8TQtx3kDxWH3A8C9NaFIw_ac4jipvVTO2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست بازیکنان المپیاکوس برای دیدار با نایمخن هلند درپلی‌آف UCL؛ مهدی طارمی بازم خط خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/27442" target="_blank">📅 10:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27441">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e83727b1e8.mp4?token=ehJ5JUek43qAfZqvKJ6zEFmoFP1r8mS4we2UHTyAzY1yCoVLqh0IaMccWGUSaQVS_msm7Pf8opFeZSLySDlbnVjElVHLENXWoeT87NwGicmEMZMQvB8NhrNF8ywDjD4Nyzb16g08GHtXgDF-Z_K4ZyXH2CAK639uKfBGpNcuc8xQ7CTDfjQcx97EIW_7C8dJWAn8Z6mTYOXdkh2WrMcQlvLlq91qd_R4rwppimfuOH_c3Hq4Q-xNQ6L6EH4zUmfiMUxvWk2zCdkL8PP15nOqGSqNFK4K3laYxj48ZgUnTYSAGbtM889zpBm0-_Dfk7V-2QGzCim1CQlqQtG7nDYFqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e83727b1e8.mp4?token=ehJ5JUek43qAfZqvKJ6zEFmoFP1r8mS4we2UHTyAzY1yCoVLqh0IaMccWGUSaQVS_msm7Pf8opFeZSLySDlbnVjElVHLENXWoeT87NwGicmEMZMQvB8NhrNF8ywDjD4Nyzb16g08GHtXgDF-Z_K4ZyXH2CAK639uKfBGpNcuc8xQ7CTDfjQcx97EIW_7C8dJWAn8Z6mTYOXdkh2WrMcQlvLlq91qd_R4rwppimfuOH_c3Hq4Q-xNQ6L6EH4zUmfiMUxvWk2zCdkL8PP15nOqGSqNFK4K3laYxj48ZgUnTYSAGbtM889zpBm0-_Dfk7V-2QGzCim1CQlqQtG7nDYFqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ علت اینکه یه عده میان فحش میدن و گارد میگیرن نمیدونم‌واقعا. تو خبر گفتیم بانک شهر و باشگاه‌پرسپولیس گفته ماحاضریم این دومیلیون دلار رو بدیم. همین. هرباشگاهی‌حق داره به هربازیکنی که دوست داره آفربده. دیگه‌بایدمنتظر پاسخ حسین نژاد باشیم ولی میدونیم…</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/27441" target="_blank">📅 10:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27440">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65599dd5ce.mp4?token=rF_BarisIulqOA139rBHsm1Md8izNl5FFPpykiNIMF-Oi59lbPf__7eJhl2B4BE5Od7lPaBnj-GXSD2XbZKmfTwI0SSlb48lHMyehRY4FenUA64VrtqWqSYPnYjh8GpRuIknhsNvuFnFxf4L0ltgLTDKzvhvcWgJIXS4SJ0Up0gvDQAkwjfuyD95mr5_vSuH21XFJoPT_uCnivcQB443YbJVKGRxBM4eYspePSLj_0u72chtBtAEB_I99jrAY3so4LxuBd77IIOvAkfe9YFgOSrlvgManofTNBqWU5gv3hANh7QitXQtELgrrLQ457U9zfw7oyBTf01UWGW7djUGVLEl9yIYL2wEMFFzbMwczXMqt1eIKs6tiF-Jp0W0ILEMnw6QAJan5K7ZCGNTTpSdyzyv4CzKL4WQL3C95ZRDTsz7w42XDwXczYAx4QLpk-lorf9OdxAKGqDr28wOO_PN3mliSqQnXVyjRxViC2z-Y8wDXK5D7VOKGv9BqTACWFvftX5Lj_5GgENKyeOzWLhJtrSOgRnLrL-47Z5c1hz2TXja9wTNJ3cT7aAiZacU-6S8O7Riqk262j8WeK4Sd11vxEw2FlvryroIXE3dhUuwM-oPAdHCSMmzkQXd21A31pfpkdcfh-Llb6Yw3Zgeo8TMolb6-AsANlZSxjo63Nm6too" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65599dd5ce.mp4?token=rF_BarisIulqOA139rBHsm1Md8izNl5FFPpykiNIMF-Oi59lbPf__7eJhl2B4BE5Od7lPaBnj-GXSD2XbZKmfTwI0SSlb48lHMyehRY4FenUA64VrtqWqSYPnYjh8GpRuIknhsNvuFnFxf4L0ltgLTDKzvhvcWgJIXS4SJ0Up0gvDQAkwjfuyD95mr5_vSuH21XFJoPT_uCnivcQB443YbJVKGRxBM4eYspePSLj_0u72chtBtAEB_I99jrAY3so4LxuBd77IIOvAkfe9YFgOSrlvgManofTNBqWU5gv3hANh7QitXQtELgrrLQ457U9zfw7oyBTf01UWGW7djUGVLEl9yIYL2wEMFFzbMwczXMqt1eIKs6tiF-Jp0W0ILEMnw6QAJan5K7ZCGNTTpSdyzyv4CzKL4WQL3C95ZRDTsz7w42XDwXczYAx4QLpk-lorf9OdxAKGqDr28wOO_PN3mliSqQnXVyjRxViC2z-Y8wDXK5D7VOKGv9BqTACWFvftX5Lj_5GgENKyeOzWLhJtrSOgRnLrL-47Z5c1hz2TXja9wTNJ3cT7aAiZacU-6S8O7Riqk262j8WeK4Sd11vxEw2FlvryroIXE3dhUuwM-oPAdHCSMmzkQXd21A31pfpkdcfh-Llb6Yw3Zgeo8TMolb6-AsANlZSxjo63Nm6too" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
تموم رسانه ها؛ خبر از رونمایی باشگاه بارسلونا از رودری ظرف 72 ساعت آینده میدهند.
‼️
تموم توافقات بین سه‌طرف انجام شده و انتشار خبر پیوستن رودری به بارسلونا باقی مونده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/27440" target="_blank">📅 09:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27439">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_fwq18DEOAgVQsC1S-4s5CcpXA-bod6hqOuwnftMJAfRHXTV0T5LNsLFMpj778NYt4pWMV0TSr-83GfmPijCYaxdWL1XEHKgWZZPNwMz1kOZIVmeLMQLw8lPhyiEHPk0BsDOTLynhf57MjZZC80deqs7rmst_proKz76eGXwM8qtoQ3PrVfidL5zOIAThztA6hzSvYsRSFSCjUHaxUtmdRbBv9iIgogAi4lRew9hAzO_9fAlwhVEilwnc_4OZ0rcFjcRLc_1S8i7t_sOfCrpiQ99czw316LK6uGa0_NRyTHAfM_oVI1F-gS0CH8U_JlTs8wBpoJYOoDVjJZ9pihHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
شنیده‌ میشه باشگاه سپاهان در روزهای اخیر مذاکراتی‌ باخوزه‌مورایس‌ سرمربی‌پرتغالی سابق خود داشته که بامخالفت‌همسر ایرانی‌‌اش برای بازگشت به اصفهان این مذاکرات بی نتیجه ماند. مورایس بعد از جدایی‌سپاهان نتایج‌خیره‌کننده‌ای با الوحده درلیگ و آسیا داشت که با…</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/27439" target="_blank">📅 09:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27438">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFZAw-m-xqulJ4YFucPPOKT5gcDUR4qzkRGZT5SR8bmiASIKxR1VV2o3hKBcDJOuVUv7DXJP8HxQ7qlDyuL6oAfDGToz2JdQqHwT2oPIvCARMCJ_Wl69xVchvjYIsWonsg7uGSPpt42utAZS8ucLJh59ajYgJsFEQTQrUqIYWR1JoCcvBPdaAS_eX6XBMrWFsVFYYS4t2RFN-SwVWeWztxCXorOZLwjBvX6yE97X8drgOpaWe3PyUz1_rAxIuHxkJA2LdUy35R9_Lh3VjxEstIcppZ9B7g0YXcCuU3k1_JBVgNaSVAkNQ9fKz6gLIMHqYYmgouGoXgR4p04P5SRspw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
آنخل
دی‌ماریا:
اولین چیزی که من با حقوقم خریدم 206 بود، اون‌آرزوی اونموقع من بود و بخاطر همین باتلاشی که کردم بهش رسیدم، شاید میتونستم ماشین بهتر هم بخرم ولی قبلش میخواستم اون رو تجربه کنم و بعدش برم سراغ ماشین‌های بهتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/27438" target="_blank">📅 09:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27437">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3qQ7ihHAPLKMCO88rR4A73sILzHoAtoasraatQHNkzk-1UglKpz5PXcI2Q6KEkpLdXABMUdHGChosjbCAACdbUago5eVsy9HWt6Uyi67vmq3It6nn9NpLhYzQn5XcDzzMBnyXb7gyLeMm8_Zu63Lyknfa36X4BuI-dMolZgaWayH69JNBoRUhJNxUhuseqQSrunTA_h9AzC3Yhn0Tt1W9GpV2sXtbLcty6ez_o0aogzI9OKdSV_3Y6CLCl9EfqfzSSgkjcsc20uBNVYypRwWWocMJGoTiVrP4xqEvCIbewk2mn8E1wz4HRJTy86rh-OpCQMJzX8BxVFGMu8we9uPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فنرباغچه به درخواست اسماعیل کارتال سریعا میسون گرینوود وینگر سابق‌ باشگاه منچستریونایتد رو به خدمت گرفت. از فرشاد احمد زاده به میسون گرینوود رسیدن اگه پیشرفت نیست پس چیه؟!:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/27437" target="_blank">📅 01:21 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27436">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-VhBPkjDghCOPC56bvHqhHnOU1g3uujKBMi6WQWKtuBuOS84dWSg6OeD3ERxhzui2um2uKgL4h1qTyjnWcuvAGqMx-s3J3T10yoU8IvIjP9dxLyMn6L4cKn8QbcoqRWr92DMlkLjYryAFSv2zQZoKsV_ZTaL1I26-rPPX2QTakZtJVbAKNwI0wTy9Nk78GUFQveQILzBnnquJdTI3jhzFyvh8c-fNyDWn8zfp5wfZs9YSex0NjAAYdlPMrxzMlbMwSuei24HlkHW4eCxsux9XMnVCLGU3JxR4eF_1oaXpSqxZNXpasbAC8qMRO0KukDo5dSnxrUnQjjOTqMkcBcgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همسر ایرانی خوزه‌مورایس‌پرتغالی اعلام کرد که بزودی‌ موزیک‌ جدید او منتشر خواهد شد. یه‌ بخشی ازویدیوش رو درکانال دوم گذاشتیم! دوست داشتین اونجا هم‌داشته‌باشید محتوای جذابی توش میزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/27436" target="_blank">📅 00:47 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27435">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8da4d4aa52.mp4?token=IXohWIPasMWkqvDWXV1-uP9yrCnC9AGryqJnZYH6IYEVaWggvB-v23zK4MGk6rV4FdaYS7IvGxJdnkV9TQ0wLNbfRxBn06zhZt4qB0mzT9jnGKQDEk8a5voGflhWB93s9eteFV1OwMqszwJAFnAMXr-vs4nauqM2_DbeTvGOUK5Pc4wTzwg_szpiaen3jD7RKGQr6ViOKldWeEfknybRgujj0eTFbD00qKevDapLzGA73cxWbwPMjPz1bn-SrIFxE7yzezq-YYCl6V86EUswWLziK6Y7B3K0_5MqpStn4xf1soFecnArdQogJzznAHOBah7-75dCsHabT40hYGDbnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8da4d4aa52.mp4?token=IXohWIPasMWkqvDWXV1-uP9yrCnC9AGryqJnZYH6IYEVaWggvB-v23zK4MGk6rV4FdaYS7IvGxJdnkV9TQ0wLNbfRxBn06zhZt4qB0mzT9jnGKQDEk8a5voGflhWB93s9eteFV1OwMqszwJAFnAMXr-vs4nauqM2_DbeTvGOUK5Pc4wTzwg_szpiaen3jD7RKGQr6ViOKldWeEfknybRgujj0eTFbD00qKevDapLzGA73cxWbwPMjPz1bn-SrIFxE7yzezq-YYCl6V86EUswWLziK6Y7B3K0_5MqpStn4xf1soFecnArdQogJzznAHOBah7-75dCsHabT40hYGDbnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نادر محمدی که اخیرا به لیگ دو روسیه رفت تو بازی این هفته‌تیمش به این شکل با پرتاب دست توپ رو گذاشت رو سر هم‌تیمی‌اش تا دروازه رو باز کنه‌. خنده های گزارشگر رو ببینید که برگاش ریخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27435" target="_blank">📅 00:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27434">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIVtgXE7LDSohqT4Oa0Jce0MrHvsVvqi5MxJwPBj5itqPlEf0R4Va0K1zALmleLLHqwAXJVLsI2YZccmzeZm1TdFQEWY6qXdlFBzsPL90Ddz1q6MDH8ThUTV3NyflqBdSgqzVfy4RTE9ijTcV0eAhBzJKZL8XBLiNeo77oceL1Ra1xuDe-Tkn5ku8BQatmvjEFQ3fIw-YjYYqGUKgymZusijbwrbZXP_gM6MOD3Vqx62nlsdNPWzqmas5FuMDNpGeJbUbHF2ikEm2LDuWAjt-R9y2-2S7dVjhMgMjN8bTlsQ1X7oPfI18F2uWU4e18VgIHazFj4XDzINBGh8Dcb9wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
‌از باخت عجیب آرسنالی‌ها در امارات‌ کاپ تا گلزنی اللهیار بعنوان یار تعویضی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/27434" target="_blank">📅 00:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27433">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLACvW6vbSDCxHe9UtV0VdJdNeH1NF-RfId9iFlBWfuFNYYC6D6g6Cg60q84bir5DdCfHEW3cFhYgj0GpR8RwUlbxVVDl4Ac5Rn6rkmxaClKIhFTr-vfQ21TKvNXYx_uBq3CWKhaFNMthKueZlZevL0hrmKzXihcUxku0cumD-iOcQ7ZMP2L1Pp2hCer48kOlufml1WPgdY-wCHxquMorl4hsgQTiK-2-1OvXT507UY7CxsEwdP9yAYm3aMy0s1WZ8qU_mjP5NnBGF3o4VCsRFCLwh15nrD25k0WaQ8rpNt2wr2fkjZ6NhQDMwu5IFe3PHZLg1rStISEb-ukc-GWSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
وینی‌به‌رکوردرونالدو رسید؛وینیسیوس جونیور درفصل‌جدید نهمین سال‌حضورش در رئال مادرید را آغاز خواهدکرد و از این نظر با رونالدو برابری میکند. رونالدو ازسال ۲۰۰۹ تا ۲۰۱۸، ۹ فصل برای رئال مادرید بازی کرد. وینیسیوس که‌ازسال ۲۰۱۸ به رئال پیوست، حالا وارد نهمین‌فصل‌حضورش‌دراین…</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/27433" target="_blank">📅 00:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27431">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIWEZ7S5ZVRGT8h7apY9dlGhWYEMWZECrwPWXKxYoghUVFOnVaNeQov_HmctgumPEqVsbRrN5YpAgDUSF1_K23zP0OTQ3Q_LWqKvM4FNKYVcX6T2oQbeB6G-Vvx7dVPcUwqJSCl6GQPzgZ-BxH-ciPoqNmHz27O1-6bAqVdaFipm4tI6miC327CD5BzEuscV3w4TXv42Ljr08y_KQIcISWJrJpYmSFi4g4Gc4vgVYDmmqcr_oG6w3HLeYpzVMmtISVRK5X-nNaWhKcsP_iGvmGRtvTBzQ9o7P5pNCJP2vAvmj66BG2EBBRcqmjMcBBFcnFOGoSVZnycCjMrKELUDFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
گاستون آیدول منبع معتبر: بارسا میخواد آفرش برای آلوارز به‌120میلیون‌یورو برساند. بازیکن هیچ علاقه‌ای برای بازی دوباره در تیم اتلتیکومادرید ندارد.  هنوزشانس‌خوبی برای این انتقال وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/27431" target="_blank">📅 00:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27430">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiV5fZlfCpRvMVxSBDs8SqHHvhivGpgX74k7frcqtl39F6dJzUYdqcBlp1eqRWMXgBzgViUQflc69PK4v2GLRiSVwQOSnigITVNC4_3AKtHeuvwlXoRBPzMKc7KMVaz3mONTbKKqqZtrC_zEvpXkIVZKGF3Z9AjWA03zBoPECIkuW9hB0b7o64hQiSoAg0ea7wX_ilD7wieSQXD5C3T55ewNKWJk1xcqEPSmLqeXRImRt82e8i1We9FSae-DxImoD8dVcSQZPVt6NLb7avgXYGGpzY00wdb1i4Zg80C85EFOVLI1MlSzCsikLjF_fJbJ4xWDuZzNrLKvnBejMr1z9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کاپیتان‌ های پرسپولیس در فصل جدید: حسین کنعانی زادگان، علی علیپور و اوستون اورونوف.
🔵
کاپیتان‌های‌استقلال‌درفصل‌جدید:روزبه چشمی، صالح حردانی و امیر محمد رزاقی نیا. البته درصورت تمدید قرارداد رسمی رامین رضاییان با آبی‌ها، رامین کاپیتان دوم آبی‌پوشان در فصل…</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/27430" target="_blank">📅 00:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27429">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0GYS-eG6NlhBuJmamw71SqIDgY3wi1gX5nhtkBJNoPY7W6cI9q_RhPyPvG8sUHOr6XKfLhtAh-9sUbCJ8vtfntBSz2FkF-_lL8YNOBHlMk6F9O5rrYOo8Bd5y5G9PMzpDOEQn86hbY2PHatgBOP4b39UoEUF9gxkHwY-bMgINzT8G7H_ORfx703TFJrUX5y1PQZgwln5MBp-OpIQyTNeuDZzq19XntL-TSoKWIlFjnktHgtIzG7o6uOkg0jzyLzqFjjltnmQQFW4VVooHKDkVVz3GTOi4O-7rHZ7w4fiYT9szkMNbp0IiZjIAu1fvYZHofb9D9ePuH6aoCjv42FWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آاس:
براساس‌اسناد داخلی‌پلیس، لیونل مسی در جریان جام‌جهانی ۲۰۲۶ باچند تهدید جدی مواجه شد؛ دریکی‌از خطرناک‌ترین موارد، فردی تهدید کرده بود با مواد منفجره وارد ورزشگاه‌شود و به مسی حمله کند. این تهدید به حدی جدی گرفته شد که نیروهای خنثی‌ سازی بمب و سگ‌ های پلیس برای بازرسی ورزشگاه اعزام شدند که خوشبختانه اتفاقی بدی هم نیفتاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/27429" target="_blank">📅 23:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27428">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJ5YofukaXLyqKFpOdikw3UnovgcCNLE0DNisDunVPN5SRMLPQfmBQWTtdPSHax6MhUrY2WgjNs8BHG9LyZOtUZYOz_MWmUf9ojcR-U_v-13UuHXv8TIdlk-rZbcbUuMnqTxlU_IvB3DQsWURl7Owo3W0N7q1ekNKHN4Mqnm9iOllJoTt9VhKaNjzINJPCuT76uWm4_9YawN8H6uQSdyoyGZ_7-xzTUVr3UldW68lr5sueEnuPSEIC8FGecnoKwkEC4lLsEin-h6knqXq5Os396oxJxo0jydm7_eSxpErMM3iJ2dq2MlyDt17YiMYkhy2jYdv-wpTlbULSwynaqflA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ باشگاه سپاهان ظرف روزهای آینده از بین‌ حسین‌ابرقویی و یاسین جرجانی دومدافع میانی فصل گذشته پرسپولیس و آلومینیوم یکی رو جذب خواهد کرد. یک مهاجم هدف نیز جذب خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/27428" target="_blank">📅 23:42 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27427">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d19eee8d27.mp4?token=BTbc_G3KV1yjetC1-f5hTjMlRspfhJAp-yi-90nDlg8D2LAc-5zLkPxIGmHFxTrw8F44Bsde47t1LstD-BiTRZ6IjVTHMIfL28ihYBpGktnWzW_FtI53e0Cv44d6B1O4_vw4pnJ5xD4vsaw3Dgr67eLyPWNSPhVoluC4DgJdwj9o-85vSftTcZlfpYXYVfDqe9odIEXjn5Y8GOR5tKXpKkS4JXBv2AgqXUm1uyIeW2bDy12n7iG2Gxxp3_in00DSbRnNfJi4LWp6ZB81CQ1yE3IBV1UlKHuxIlXZonBhjAaD8CRxfa4mymUWE5wgHq1_EFSXzPrz1P7IFM11vrS1lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d19eee8d27.mp4?token=BTbc_G3KV1yjetC1-f5hTjMlRspfhJAp-yi-90nDlg8D2LAc-5zLkPxIGmHFxTrw8F44Bsde47t1LstD-BiTRZ6IjVTHMIfL28ihYBpGktnWzW_FtI53e0Cv44d6B1O4_vw4pnJ5xD4vsaw3Dgr67eLyPWNSPhVoluC4DgJdwj9o-85vSftTcZlfpYXYVfDqe9odIEXjn5Y8GOR5tKXpKkS4JXBv2AgqXUm1uyIeW2bDy12n7iG2Gxxp3_in00DSbRnNfJi4LWp6ZB81CQ1yE3IBV1UlKHuxIlXZonBhjAaD8CRxfa4mymUWE5wgHq1_EFSXzPrz1P7IFM11vrS1lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شایعه‌امروزازدواج‌رونالدو و جورجینا باعث شد هزاران نفر مقابل یک مراسم‌عروسی در پرتغال جمع شوند، اماباورود عروس و داماد مشخص‌شد مراسم برای یک‌زوج‌معمولی است! کریستیانو رونالدو هم با انتشار استیکر خنده به این ماجرا واکنش نشان داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/27427" target="_blank">📅 23:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27426">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1bEIvSesDfcEtp_mEpK8UamGFNnx0MlLn1hCTmBjq3Tak9RXh-5fjjYRmdM5rq4fqprTKAQMAIUKhvVatU3nSBa5QBt4-srpVBNJdxnzvtSqm_prirP1vJK3tizo6lBaXHaoFWc4VORnFxV3LVk4_CeYsuMH8_MdmlgSiCkaP8DgI8-VYqc9xwgx77l_T3kxLB2Y2Lh8l8lTExaPgPrYEuUsN9JDw78RkOOhQzNbZnzInrp3I8xXZwjtBWKvE7iUbli5HWIQeahtRPMl3bijHGZ6g3PorMx4f_g7j001HKQoe4dazt6r5F48GLgiTSdJPykavH679QBvbBATOa-Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بعدازجذب دنی ولبک؛ چلسی ساعتی قبل جردن هندرسون کاپیتان36ساله‌سابق لیورپول رو به خدمت گرفت. حالاجالبه‌بدونیدکه هدف ژابی آلونسو از خرید ولبک و هندرسون‌بحث‌فنی نیست فقط‌وفقط میخواد تجربه تیمش رو بالا ببره چیزی که توی تیم خیلی کم وجود داره و رختکن تیمش یه رهبر…</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/27426" target="_blank">📅 23:21 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27425">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5Y8nIu-PcqF4LEg_VqMOEOr0ZlenLTrVtMIrtzJt2cJvtSD8F9IbjvsPgpu3oJ9OznZkiNogbPIv0OEzTbWS9JwSuRWTiuN1jsuw4CLldPhcEym7OCUu0nccxjhPG6Sjv7aUXsTriAeQeeIz_GGnjFDtqKtZ-zXVQA4exaSJFkWe5sAm_jVtQGgBBFJRzJm5kKBHUW4edzG3ZWvQAYPHgRtIWzntfyjUdD70Xb59yPpafB_JvyxdU4qSH3ITJXlqHKlxMWaL9jlCgX-DeiyKtN2SnxtDWj39vySI8Wpb-Q4uY2yvqrc-PI9O_Yesv-N0rROhuzQ1Jjl905VC8mR0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی پرشیانا؛ احسان پهلوان هافبک تهاجمی33ساله‌سابق پرسپولیس، ذوب آهن و فولادخوزستان‌مذاکراتی‌باباشگاه فجرسپاسی داشته تا درصورت توافق نهایی شاگرد رسول خطیبی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/27425" target="_blank">📅 23:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27424">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gv-MrJUSYrMc98K4fdkqBolWsnKoOFIe9IYt_TzWwiYLHlBPwT0NrwXm4SSAt0yBnmWPhLyRvHPm1FVDU4wTblEAA1du_ucvHqnNBwp82KxwqWL3pU_vBIdUxPoGZnCUyHkghexaYdnQmjlWkwVRiP2HOn7GMlwRu_kdsOLjZZ0qrAXXROtYFI7M5yCk1mIArO9YXFkbzL22d_YzlPjSfEk1X4AYSawIuc9HfBmLvIsNnX95dQiU1IHbsVhQUSLh234UrYrX_ZSy-buNFLuTP2aK-NJaEsWDyYA9J3XJr-yLZSCvwtPIpqTiBRwp8tGqymOQuRKZeNxRnFzd26e-_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری از موندو: سران دو باشگاه منچستر سیتی و بارسلونا بر سر انتقال رودری به نیوکمپ به توافق رسیده اند و این انتقال بزودی نهایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/27424" target="_blank">📅 22:43 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27423">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUmIgqRbz4Ma6Cgo4ysMo7Ls9-A4Zq-wo-mLeVxUcFPVxjcc_c6sVvbidksRcO73vqTOaPENI7woJL_Y085YnuULheXnQAEORP3UJx5Genevpl_b8sDU14JiVpnTAE0AV_PZFXArNIogpV32LSWp3pN3mbDarZgBUnr15qxbhBr5N6spymrZ_BS0ZRP9ZRM_jnNKwfSirfyMfz8_MtKaZV395Zhm_VNGmO8BB4sl1S8EuT5ww23q8IbngOYGH_W0BRj_wr4hqLxCTZt3MZg-mpRxPzdyIMoGWEjwtVzf8Wxy0x9fX6cf83aIK-yQbl6m7bh6Iddu3CpbfKtFnCZH5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔵
اسکای اسپورت: باشگاه بارسلونا بزودی 55 میلیون‌یورو به‌باشگاه‌منچسترسیتی پرداخت‌میکنه و انتقال رودری به‌جمع‌شاگردان فلیک رو نهایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/27423" target="_blank">📅 22:16 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27421">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f508d354c2.mp4?token=WGD7dMKsCEr5_hwgdqjk5mt8cZ64okrsTL34TBJstUNddhNfX_Sru5fosIjt6cHli5ams8z5fqOmHZn0u_b7E98n7TtxO0CRBkXws_anZN685qkPWF5Eh-__dGf8te9XIhzynFZXEYlWnddXXsgmQ1GVFKQ7ut5QFhcFobCk94eVk8rgoqH9C-CVM5YdZDZyUzOBHQMPBjpbulSb6W2ivleEN7A3ccCdwCDD8ScFn3taX7w3X7iUjz0D-arZOHtJGxzoYMbqdlD3K0gitMwmXIyXb9NLQW_WBY9VpyO0XluxIMYq5ftM9C7I6e-1gAVf8remk6DciSL8ceLdQpBJpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f508d354c2.mp4?token=WGD7dMKsCEr5_hwgdqjk5mt8cZ64okrsTL34TBJstUNddhNfX_Sru5fosIjt6cHli5ams8z5fqOmHZn0u_b7E98n7TtxO0CRBkXws_anZN685qkPWF5Eh-__dGf8te9XIhzynFZXEYlWnddXXsgmQ1GVFKQ7ut5QFhcFobCk94eVk8rgoqH9C-CVM5YdZDZyUzOBHQMPBjpbulSb6W2ivleEN7A3ccCdwCDD8ScFn3taX7w3X7iUjz0D-arZOHtJGxzoYMbqdlD3K0gitMwmXIyXb9NLQW_WBY9VpyO0XluxIMYq5ftM9C7I6e-1gAVf8remk6DciSL8ceLdQpBJpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌امشب دربرنامه تلویزیونی خود از کوروش اژدها کش و امیرحسین طاهری دو خرید جدید سرخپوشان رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/27421" target="_blank">📅 22:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27420">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec041c42ba.mp4?token=DeMSXi5E6OKe1547JFO7ugm6JQtjdntGLzZUtwpr67-DPn9_TTV6JvollYeylJom0e_dBog20ovACJg-1ZrEtQLjp31RsLIXdTIrFVsXDtcGglwRHlhvvHKcc1PN3erjzk339QjSNKNsEpbmS9FF3rhgoolZozRmsRc7hyTVy5LSKw-sthdDLISmYEumbN0BI7B7raIDcofTV3DjGEDhgBDB7em3yUGum_mZ9e0bDSzGfvL35vt10qzrb6D5q-rstMqYghDfcVgA2L-EJgjm8giK0I1NAzTnMEuZiMtAKiL6mlqq4ml7YMjB41od_HCZlq6wgqaD8gBIUspYiOK73w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec041c42ba.mp4?token=DeMSXi5E6OKe1547JFO7ugm6JQtjdntGLzZUtwpr67-DPn9_TTV6JvollYeylJom0e_dBog20ovACJg-1ZrEtQLjp31RsLIXdTIrFVsXDtcGglwRHlhvvHKcc1PN3erjzk339QjSNKNsEpbmS9FF3rhgoolZozRmsRc7hyTVy5LSKw-sthdDLISmYEumbN0BI7B7raIDcofTV3DjGEDhgBDB7em3yUGum_mZ9e0bDSzGfvL35vt10qzrb6D5q-rstMqYghDfcVgA2L-EJgjm8giK0I1NAzTnMEuZiMtAKiL6mlqq4ml7YMjB41od_HCZlq6wgqaD8gBIUspYiOK73w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
مرتضی پورعلی گنجی مدافع سابق پرسپولیس هم به این شکل مراسم عروسی‌اش رو برگزار کرد. همسر مرتضی کرمانشاهی و پزشک هست.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27420" target="_blank">📅 21:45 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27419">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2458f36d9a.mp4?token=XoumrurUggW4GzJ9wkICHlvOTWh_gVPScAeC6gUA6FKvHS4hVmwWTqlGl3EerBHJb9cYT7RduIJlZb38J2Eky7frE4aHa6ScP9D3K6tjmBf6OHIAUQF4qEB2wSY8L4DSgMVI_qUQnq-4F5QqzH0OcxSW4GuHh6JHJIn8fR7wfe5r3Vv5gCwkmg45UPkiESyJufh4tyCztYDAiigZ05ot3H4FgVnlNIAFHsVj9xbRT0pCLe8Q9nUiXtwD7Pn-3RQrF6ODl-pHuVFZ-qRLMm4T3m4tVHCWCEPU8juf1KaJ1iOYtPzmmis7TsaaQVsFoRG1qHubia-SnuXU80TTYagLizzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2458f36d9a.mp4?token=XoumrurUggW4GzJ9wkICHlvOTWh_gVPScAeC6gUA6FKvHS4hVmwWTqlGl3EerBHJb9cYT7RduIJlZb38J2Eky7frE4aHa6ScP9D3K6tjmBf6OHIAUQF4qEB2wSY8L4DSgMVI_qUQnq-4F5QqzH0OcxSW4GuHh6JHJIn8fR7wfe5r3Vv5gCwkmg45UPkiESyJufh4tyCztYDAiigZ05ot3H4FgVnlNIAFHsVj9xbRT0pCLe8Q9nUiXtwD7Pn-3RQrF6ODl-pHuVFZ-qRLMm4T3m4tVHCWCEPU8juf1KaJ1iOYtPzmmis7TsaaQVsFoRG1qHubia-SnuXU80TTYagLizzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
سوپرگل برگ ریزون و فوق العاده تماشایی اللهیار صیادمنش در بازی امشب لخ پوزنان در لیگ لهستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/27419" target="_blank">📅 21:26 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27418">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDgsUTis2Om4z1BTPKbu7bYZteXoWWfEugMePwaKrc6vLO1JWhk7rHfRWaOQruKK8H0o6EzGJH-To1S-iaPztkrtDUZeISmd0bmSGdcP8ELgqj9mSB_H-pbpf9uimyS8-4b__Gs72hlx0cKMfZQmiKtk2gu9ShOjhZE_xhrJ5IjtNltQCeFMTq6gmaGLJ44SSy-bj36AqCVbNAH4dl63N_2jXW0U1NrLQBEbwDb3Lojk3JZimZnqKYipr6pwn1j3g8PxbFr3EeIb24JAfXtxw1fLYIy91aykyrCkBO-aDNjUxFslrvGXBMlN3oUpzoCCVjachV6Z0dPj--wGduIPwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تیم پرسپولیس درآخرین دیدار دوستانه خود پیش از شروع فصل با یازده گل تیم منتخب کرج رو شکست داد. پوریا شهرآبادی مهاجم جدید سرخ‌ها در این دیدار به تنهایی موفق به ثبت زدن شش گل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/27418" target="_blank">📅 21:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27416">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bOE01qAQOvVwYLkObewLvpBQ5m1AuEV_vLA97oKUcu6yQCHXRT_c3Op00QwDTPeYq5onk7T2RYH3sVvh9UEQMVOYQFclOFc3PEXpxuP4AAVIis712WH1K3r6RLSD9r7t31akIYerypWRcmy9K-XOnAoNhV053m6f8gP7VA-kGGw_lcjVUhE9EFjaZJQ45dDCV6mnJuXHpizR5hN1NcId3jVwHbS8A36drR1t6JUApbihYG1GZc7HcCBp8X67cRVIWosZVBE3yaiPiizjHPVCTJ-qM9zPWZBmcGnPeLRFKen_OrmQCxqbSfPs-CW9oy9J1eYHzgSAxRCFfHduPF32Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ojScIx5sg_IlJsvhDkPEjaBHT_d_G6Acy0ujEF9N3_aaVBuWaJnk7FpQ1ZbPcAX0ZQ2D_My9sQ83V2Rn8csSGjImx60zjg2vaOENcJ7MHTwS3XrNfqVf5vFkESrQZP1QfdFkDVfxFr3QBMfiaBQF--rm1T9UEYHBJlJR0L0u-lC45mJeBSJKjcDZX_Crm5vIL-KNR_TmjALW7kxI3jDfAy6EUIOTGSxhB_hPxh9BctODy0jnjkgqZnsWFrThTRbu5-DqpEnJaGPDpc53TqUplsZvgc1ziNqZO_znTVTbWau7PDLUOJokS5wTMJIMvPythETb0Lrm4qtfmsjh-mGrRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
برترین‌گلزنان ۲۴ فصل‌گذشته لیگ برتر؛
در ۱٠ فصل اخیر، سجادشهباززاده با ۲۰ گل، بهترین آمار گلزنی یک آقای گل را به ثبت رسانده است. اما رکورد تاریخ لیگ برترمون همچنان در اختیار رضا نوروزی از فولاد است؛ ۲۴ گل در یک فصل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/27416" target="_blank">📅 20:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27415">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srxfIUNdI_rfd1puxFs6sHTPv_zX2KX1_FyC2wzEE43c3_Jj_JuqtKqbcSYNodPiiDKuBYPWH9-5qsttLzUe3npz0zAVhKLA6crQeVYj7HOZ-SA5vCNSPEtmCboLLq6vTBvAxtxOBd-DkmfWccgn01Jj7VHzQfpUVGRg1Dykw8syLiNnN54Xugn9hu9mNokrWTgOuhyzupCGkbgakI-hoXi0VvvJJ3d-Wf9oenoUGSOjSrrVMMVJra-xyH20xzUkE1dY2zAzycFoEy4JguKZDATIPGYc_SlFepWFlR5-vBOzSNdjkS3gXDLWkYfaGeNAT2qR-riAzpyKMsi_lE5gOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ جواد نکونام سرمربی تراکتور خواستارجذب آرش رضاوند هافبک تهاجمی باشگاه سپاهان اصفهان شد. احتمال اینکه با اشتراکال مهاجم تراکتور معاوضه شود وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/27415" target="_blank">📅 20:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27414">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58a8a9a5f5.mp4?token=WkSBLRb-eJHcuHdxbV17Bfanih6fzjIzkXJCvKO3KWQdWYZfE7d0fnlC15piEiyi2C31mMfBWLJvLg6t4rGc8It6QqJRSCStBfgrxdFqzHrG1tkfaVKBNNoVgeElrvLcPQ7afHb29U--kRsEq7y8uiNxH8huSmWbm-kk2NeqXnduObNsmyx2zTB9Ap0afOEcT5z0k8mCY-bd_SIkOCxgWktIDMYdnAUIEZj_9RSu08MIrUHP0xFxUaiA-3HRv1uV3Hlg_eEYTKR0ZFlzz6w9FI-Nz9xGgaqojRytiOtshEawroix4zTuJUAY2p_J_rr_Sfzw6rDFV4N9j06DHkGivg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58a8a9a5f5.mp4?token=WkSBLRb-eJHcuHdxbV17Bfanih6fzjIzkXJCvKO3KWQdWYZfE7d0fnlC15piEiyi2C31mMfBWLJvLg6t4rGc8It6QqJRSCStBfgrxdFqzHrG1tkfaVKBNNoVgeElrvLcPQ7afHb29U--kRsEq7y8uiNxH8huSmWbm-kk2NeqXnduObNsmyx2zTB9Ap0afOEcT5z0k8mCY-bd_SIkOCxgWktIDMYdnAUIEZj_9RSu08MIrUHP0xFxUaiA-3HRv1uV3Hlg_eEYTKR0ZFlzz6w9FI-Nz9xGgaqojRytiOtshEawroix4zTuJUAY2p_J_rr_Sfzw6rDFV4N9j06DHkGivg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
رودریگو دی پائول: یه بار لئومسی دیر به تمرین آرژانتین اومد و من‌بعدش به‌لیونل اسکالونی التماس کردم که مارو بخاطر زود اومدن به تمرین تنبیه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27414" target="_blank">📅 20:19 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27413">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f5820aa32.mp4?token=W4PJ6zr19c2quIYOfA2KuZ2bzprPjfnG7cEwCXTPo7n6nmlH8Uspg-7m1dq6S7ak8QFDfpqR9WnCJhtKVUedVo_QO-mWvRbl8OhcEkCGemcLSVypK9ctOEZXEsEdrsvPiwhzPqNK4Y3gTv0YrI1ei1YLfbWz5SUXjQzM5H6lpkVCJVOirRhpsRpWi9T9Ix-2jx5-19FTKMcEhaI3sYPIwyLrnr1hv_V8ppHlKvN49F2-izZXRZK1ysYqKKLU2wBciMkwK65WNu8U7Rd0cPvNA0wWCnEzyC9en0chicXddTlA0Phm8j1RxCyuFFiyQdhD648sx_lEffOeRhx7t8h1C61XCyKBVVto6WwkTHpNRzU-SPwvv27c1q2Q7U56_ZzhDDMo5E0PILrY8KiIMJ65vURKV6ogNVJzqBAiUOIRWiNQO4DeiS2i6hKldoly8MfIgmSpXcoH2mcy1pQSWSkAIYFG5BP2uMY39f1L2w44rL9qwYGpCC4DIaWLu56wXHSpDb79iGkKzrkOcWCya1_PVnisNu6SRrM0yyeaa7QPcFYIltllRCoAnhl4Gq02LtRDL4ig4N64bvxpH5l4hyVtdYETZZ6cjjFoAAVb7k2RzU-ff-bjQ1qlmZ2GYms5XT_vWCHeh9iuTLCKH4KnIeWddQ8XBOv8w5XrDjErh7Sj9Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f5820aa32.mp4?token=W4PJ6zr19c2quIYOfA2KuZ2bzprPjfnG7cEwCXTPo7n6nmlH8Uspg-7m1dq6S7ak8QFDfpqR9WnCJhtKVUedVo_QO-mWvRbl8OhcEkCGemcLSVypK9ctOEZXEsEdrsvPiwhzPqNK4Y3gTv0YrI1ei1YLfbWz5SUXjQzM5H6lpkVCJVOirRhpsRpWi9T9Ix-2jx5-19FTKMcEhaI3sYPIwyLrnr1hv_V8ppHlKvN49F2-izZXRZK1ysYqKKLU2wBciMkwK65WNu8U7Rd0cPvNA0wWCnEzyC9en0chicXddTlA0Phm8j1RxCyuFFiyQdhD648sx_lEffOeRhx7t8h1C61XCyKBVVto6WwkTHpNRzU-SPwvv27c1q2Q7U56_ZzhDDMo5E0PILrY8KiIMJ65vURKV6ogNVJzqBAiUOIRWiNQO4DeiS2i6hKldoly8MfIgmSpXcoH2mcy1pQSWSkAIYFG5BP2uMY39f1L2w44rL9qwYGpCC4DIaWLu56wXHSpDb79iGkKzrkOcWCya1_PVnisNu6SRrM0yyeaa7QPcFYIltllRCoAnhl4Gq02LtRDL4ig4N64bvxpH5l4hyVtdYETZZ6cjjFoAAVb7k2RzU-ff-bjQ1qlmZ2GYms5XT_vWCHeh9iuTLCKH4KnIeWddQ8XBOv8w5XrDjErh7Sj9Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
باصلاحدید سهراب بختیاری‌زاده سرمربی تیم استقلال؛عماد زارعی وینگرچپ 18ساله‌آکادمی آبی‌ها به تیم بزرگسالان پیوست و در فصل جدید با شماره 99 برای تیم استقلال به میدان خواهد رفت.‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/27413" target="_blank">📅 20:06 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27412">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIYD6Mf_OIlpAP7B0aNdarrUEpElvcZkR3EjTKfoOcj7FX-x9vsaLaV1uVUny_4FN1fGn9qksupQmaot_BZm9n0xvqbI3FB1Vv5SiPBdgpEY-44jROs-m8NCRqW_pASXkNB1GghwGLJfIjfeb-2nmRjZRh1gGjQ2IveDXgDFE54kAhn4qLNCGcPa2pW4-_XbghhzZ1v_WF5a_AcRf4T5SznKWwzeRX_sNRdD2gDU9y_kQwBGGshlf3z4SuJGgBN-pykpIPJgDT-G3ltgfQBd6pTzih6lOl9uo7UsrIsyCo5O9f92XpGXJZ0PjdfdseyCJ8MAg_HtIhiOt0p9jz8EXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باصلاحدید سهراب بختیاری‌زاده سرمربی تیم استقلال؛عماد زارعی وینگرچپ 18ساله‌آکادمی آبی‌ها به تیم بزرگسالان پیوست و در فصل جدید با شماره 99 برای تیم استقلال به میدان خواهد رفت.‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27412" target="_blank">📅 19:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27411">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3h8_rYPWBsk0Qts-2Mslye1T9eUJmjUBrSeJpnTgAwBxDljqwXP2n4vGXYgIGc32Ut4SEe4P9Z2yXxML8ojFxNzrjshC-oYd64I27-YfwyX0rgbmRYcwJwpDg7_4Ug_tmvDS4cWiUYucXxxDpSTju-wtQn9JfxP-wZC2cHp7ynCmQ21vE9mFJ0k345iP88KDMZN05T1D7ZtK4lPaKiPHznjmEzcblpm05AOMefwDPhTrFpiB2L8RR7x2T2rDrKew_waVcUgDqJWLPrRtLAXR5Cy3LqtZuk52h8ql-tRdF6Mp2bTK5K16vOnrfnRhuzuMRboaQdRj9Bow-U35VkicA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تفاوت دستمزد ماهانه موسی جنپو در استقلال و تیم جدیدش؛ درپانتولیکوس ماهانه 20 هزار یورو میگیره در استقلال ماهانه 140 هزار یورو میگرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27411" target="_blank">📅 19:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27410">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbO4pP2oQDXFsPuw531fTgNOTJS84p03iu_fuG5WsGVIx7MIRbUwEp5RuZ5tVx0O1aiViHqQ0g9wLTLt5jqzbrWfn4mAAT9qj8huJhGWsOq69vcemtY3DugXGI5gMfU42HZp4DoSOHSkvKBauqE-ajJtWpl9u-kAV05vnmMfmP6R6uASlMpl-mHnr7AlSS2s_m44b4LlZdSB1pj52W4dh2f-pkdSW0xTwENFAD5khz9-hTDhOAEycowvEF0tjeGWGVvwBLAV2yBpM7rETJaIoEGS7akBAIqNTu_O1xpXDRPRBC4c5sG2wYvMEA-iPY7FSbkWIRtJMw93kX8806XaYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تیم پرسپولیس درآخرین دیدار دوستانه خود پیش از شروع فصل با یازده گل تیم منتخب کرج رو شکست داد. پوریا شهرآبادی مهاجم جدید سرخ‌ها در این دیدار به تنهایی موفق به ثبت زدن شش گل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/27410" target="_blank">📅 19:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27409">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ej8Y0RGtvsZlHAFAUffMxQ2dRyZrM1EglGjpHIFQD38URfXxtf5bwzy2nCsgqNijv3XjtHbB8YVeRBnlvyBAwLj4w5un4--RrbhyTGx5UOcDcIjVqIbUgaHf9Kk43HQ7g8IWydUfN0c3slqfARN23s5TyhofqyfAwji3q7s0544NWsX4XvGkMywTRm7r6i0BVesYC7l1nj54pCdHp9TCA9X4kGHTwElcqYqK1-PJh13n8GH9CGZMXrEPAtZHbBV4gioOWh7nT1fr41iDRfRgEkE2lfD-6hbglsqXYuvP0VB5r6PmK5XZeyBe5IeUBX7-oYngVsQiShamvlSvByS47Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌‌امروز؛از دوئل شاگردان مارسکا و سیمئونه تاتقابل توپچی‌ها با دورتموند در امارات‌کاپ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27409" target="_blank">📅 19:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27408">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzpnQvVN71bT0NLfW9keWas0goFC3I4K9nSHbnGN_xEczU-JWK2oKk8vZiIuHhsvAXByS3kli6GhQtkZ4pEx0GNuOmJoJ3B1FOtNFNnOZ50juYJabfR2RXn3_6W2-9cPmuaL6a1QqqV6myQgK2X5xNUTJ--k2fAPGhMljLwhL2Khw_beRo82jxZFw45OE6KG9ExFUHhEi41JQnsqWdv7bnZnK-NU5V0gKheQ5Z1-JbPdwC_sQP62Ohv8ibBTVh3jEZkY89VaISDvtgqOy435HggqHeHYaCo2THH_CG0xelRqnmJdo2BcPojn7iZ2ZvQlwIQj-xP8lGuoqozlXH318w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ در صورت تاییدیه مایکل کریک؛ مارکوس رشفورد قراردادش رو با منچستر یونایتد تا سال2032 رسماتمدید خواهد کرد و درجمع شیاطین سرخ برای فصل آینده رقابت‌ها باقی خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/27408" target="_blank">📅 18:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27407">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/faz1PoZ1hZsEBBIshlZbr6b2Mpthw7Wr0IRE8P5V0PeKuCkDPHpVMXAbiFD5-VNQCty34-_g9tPMljmBHfWB0_BA5CogjHWPi_YJDSSCw7Na4TflUJY3er9-Aegf8QBe95uB27m3946xUbWzpj6_X1p0YtjtScAx8xWOJ5Z7KAtTvZna3jJP1D0TfZECyvZT9i5OOI1SNhaJFREir59SZnHukSlhY7cyIFBVi18CA0-zEFunl0-T0PtEUtTZRL_YMigRtmowySxiJZuQn_i95C4QMySyQqz536ags00rwJ_eoXE435tmKQZRx4DhS6Y_MQO2gPAPxAASyXnTASFDWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فصلی فاجعه در انتظار روسونری؛ آث میلان در اولین بازیش تحت‌نظر آقای روبن‌آموریم این فاجعه رو بار آورد. حدود یک ماه که با تیم تمرین میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/27407" target="_blank">📅 18:19 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27406">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9154dc0f9c.mp4?token=ARQUYkx6QmXv2l2GMWH6Uc3s4Vy6PPE2irhvRD92m3jMjVD2-Zf9kGv_QMkMqGwKtxKTEHeXCASvYQkyozdZPKIHxK6c2KTREhgy-qramdXyq5jkJDGiE0qAQrpu0F9g-SlxDz99omhKTJ_5Y5ypbJHDLC2g5tmdg3pt7jU347wQcJc-8IWyqxHN3dSL7MEl6CntslQtlBZwvu8FPj4RHR42oH4gla34gmyPFUGQrY2LG_AxRVQjAZ80ssAU_tfKU_KjbFDyNSjzRhO89xp-gsZR8RNB3-harOu1ItmhRgDe-RvKmuRtRA8lFtzrMMijOnY8B5fnJahAuDRJMnf4Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9154dc0f9c.mp4?token=ARQUYkx6QmXv2l2GMWH6Uc3s4Vy6PPE2irhvRD92m3jMjVD2-Zf9kGv_QMkMqGwKtxKTEHeXCASvYQkyozdZPKIHxK6c2KTREhgy-qramdXyq5jkJDGiE0qAQrpu0F9g-SlxDz99omhKTJ_5Y5ypbJHDLC2g5tmdg3pt7jU347wQcJc-8IWyqxHN3dSL7MEl6CntslQtlBZwvu8FPj4RHR42oH4gla34gmyPFUGQrY2LG_AxRVQjAZ80ssAU_tfKU_KjbFDyNSjzRhO89xp-gsZR8RNB3-harOu1ItmhRgDe-RvKmuRtRA8lFtzrMMijOnY8B5fnJahAuDRJMnf4Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرصت سوزی عجیب شهاب زاهدی در موقعیت تک‌به‌تک با گلر چلسی؛ تو یه لحظه هم رگ غیرتش باد کرد یهویی با پنج شش بازیکن چلسی درگیر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/27406" target="_blank">📅 18:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27405">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6sS3wYCUvjoeMMXij6Tq7116HNysGKTDwK55G9PAQ0ihyiWqQxk9sq6BYzyA9x5Wv7llwICZANVhLXPGkeh4xJiQG1uLzqmKWiPUQHlS6J43V2ooZW6dbea82yfVMbkvvaB0GaP_zSoVznHe9lptlGb-cdIFy21uQt_NwI1D3AOj8GkCrimkzwSiJWSDvOvxH2dI0E8wjZ9zUayD7awNpgl2y8HlbmmfQB2tctL8s8yMsj5yjULSrGOb_ezTfoUvpeR93qbHpq5iAR5AwTyQf29NWsMgkRAYXF26JD6rosYftd8IFrHwI973NZpWqyLKlcis5jWoHEnhMacaYMilg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پیرو خبرریپلای شده؛ ماخاچ‌قلعه‌روسیه‌امروز تو لیگشون‌بازی‌ داره و حسین نژاد طبق معمول بازی‌های قبل روی نیمکته چون کادر فنی جدید این تیم تمایلی بهش نداره و به باشگاه گفته این بازیکن رو بفروشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/27405" target="_blank">📅 17:45 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27404">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsdcSX8yrtYA3uDLhxIr5M17dfA-T1zVLoB7D4RUICgOS4vdprW3ehCvPNMpTKT6DxXfORQIloX2GubVgTsPVpXcnndKldOeOxwwC0uaq7NoyWYt94VlEGboHloLwHyVVnDvIBk_uGuYw-9ZfHho7lfdchtLuPBZ4KgGvfgBvERsbwsfTgLA1MYY8P4anATWQqOOqlce48GGSOP1Z8DuaXJtAvjIxxtNgTh5Wd--TA7aN6Hh53JJinqUb2TdJ-OueMY0N0gjNbvIT7yCeWoVOlmjME5dl7kmoj_PIqpjWM7a836RZPUHOojJ7ypYlivep2WzAZuL3fLTBhLeZffudg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
ایرانی بس کن؛ یه بار دیگه ثابت شد که تو مسخره بازی رتبه ۱ دنیا هستیم بااختلاف کهکشانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/27404" target="_blank">📅 17:24 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27403">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8dde9dbf8.mp4?token=dTcTZNvgcBlE0f_JpcPd3IgcmW2aPXEb9JylVKXzgDp8j9tEWbNflWIalanzRGac9UFkblzwdU_aU-2DQvts2MeWDqR-PCmctSj6BZys5JpRoSXVqpZzHU-0hijSHjy4Yq388fCOgmrD0eyLS9JPGDYV63QrARfs1P0jvge9uQN-PGuDdC0Kx-d9j81cWu4aXnx0aW_i5JniMI5yB_tOL-LVxmwjf06-YQ3J0tXe0eoCnpGsuDlRIqYRmIeeBSywfEJhs1mvwlX7yDufcZa6GMldMjbgSViJAt5NoX6Si6b2kQyQLGsvhOreT6HNFip33Ccnyrl3LrrlTvouGBwKJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8dde9dbf8.mp4?token=dTcTZNvgcBlE0f_JpcPd3IgcmW2aPXEb9JylVKXzgDp8j9tEWbNflWIalanzRGac9UFkblzwdU_aU-2DQvts2MeWDqR-PCmctSj6BZys5JpRoSXVqpZzHU-0hijSHjy4Yq388fCOgmrD0eyLS9JPGDYV63QrARfs1P0jvge9uQN-PGuDdC0Kx-d9j81cWu4aXnx0aW_i5JniMI5yB_tOL-LVxmwjf06-YQ3J0tXe0eoCnpGsuDlRIqYRmIeeBSywfEJhs1mvwlX7yDufcZa6GMldMjbgSViJAt5NoX6Si6b2kQyQLGsvhOreT6HNFip33Ccnyrl3LrrlTvouGBwKJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
طبق‌شنیده‌های‌پرشیانا؛ درصورت موافقت مهدی هاشمی نسب، مربی سابق استقلال به کادر فنی جواد نکونام درتراکتور اضافه خواهد شد تا مثلث خطرناک‌ جواد نکونام، خداداد و هاشمی‌نسب تشکیل شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/27403" target="_blank">📅 17:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27402">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7pFtBV4XhkhC6fSvD0ji3gqVDWE7iraSCOmnNULBDI2YsUYXZ7BihdF-_NsG3DqG95DQpUSKSdF90sHTJ8uA-UrwHl4qvo2kbw0-DbRUvtL1lq-bKIvX_VMw1PNVc-sJUz5-KdDOHdWundmjL9VB9aQGr4OYB4XzJWdyvByg4RFMmUwHQCGDiBLplofIRQrYyu2HEEY9S9mpTsj9UOE7MHuNuGVpA99Nc7gbqtmfCr5oPv7LepCSQPwHiy6G0jwwyHXSWuT7ZVJaeixxUOelAG60SfpwvILDdNWjbjj-3iEzUQ7VY7GjyYerpGyECL0LYPgUPTRKFCDAZmrULObWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
🔥
فقط و فقط ۱۱ روز تا شروع بهترین لیگ دنیا و رقابت‌جذاب تارتتا و سهرابیولا مونده؛ برنامه دیدارهای هفته اول رقابتای لیگ برتر خلیج فارس!
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/27402" target="_blank">📅 17:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27400">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47b7307f5c.mp4?token=Il_sJb8U7uyVKbNm7n62GBg78ykvN_Imcr0n1Gy2ME5vqbwH6vdF8vrGZOW4leb-wNMyo84-i6PDg-euuGsIT785nhFFuk9jZjGLrQwP_r8uSyv2ht9eBlITVco6BgJtGQ7W_r-41jc-jtrExcHwpDqy-aH7PTcdQNvUCBWgMypoU0MtKJen5ZzyzlycLWXPOnRhEDSfBezBmTiWUf8JsXfDA0ekRBWFBDag0oN83flbB48-cadz0H8llDy64c1dAWdS4IC8DWcM3x43tfKWgJFZRR_Zex3qVTrF9RJnGccjPZ6-2Nyewdo7TwtoHrUjOAFwLGikTvojnxGcYgS0pgF5Cn1mZn88y4N58hu08faJmIIGMVCjAsTKUqz7KeyUX4WIN_6SClRlE4WOZi-aAIsKJ3wbRBFxwz3DUow9HfGCKEWyo9QjhUqSjY2BfNVZJcUBjMdARdF0NNRN2yuoyRdKTeBjZciyC3wI__HAkBtAy8r4iXAAsizVv3RQ1VG2gj14g4N8VBP2C8n5JaCRmPlr8XHrhfbq03BRV4EYJ4VTfVvykj2Ik-hdnxzLjTVOJvaHKQBvw1Hce9MqynkGW711pWGZOuflMM5n9vUvVLB60X-xxQsrFuHolNwtwRGQ6hVpCK-jni7_pJxQqG7YFfvIIWXQEGsgGHjsQ0UK8aU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47b7307f5c.mp4?token=Il_sJb8U7uyVKbNm7n62GBg78ykvN_Imcr0n1Gy2ME5vqbwH6vdF8vrGZOW4leb-wNMyo84-i6PDg-euuGsIT785nhFFuk9jZjGLrQwP_r8uSyv2ht9eBlITVco6BgJtGQ7W_r-41jc-jtrExcHwpDqy-aH7PTcdQNvUCBWgMypoU0MtKJen5ZzyzlycLWXPOnRhEDSfBezBmTiWUf8JsXfDA0ekRBWFBDag0oN83flbB48-cadz0H8llDy64c1dAWdS4IC8DWcM3x43tfKWgJFZRR_Zex3qVTrF9RJnGccjPZ6-2Nyewdo7TwtoHrUjOAFwLGikTvojnxGcYgS0pgF5Cn1mZn88y4N58hu08faJmIIGMVCjAsTKUqz7KeyUX4WIN_6SClRlE4WOZi-aAIsKJ3wbRBFxwz3DUow9HfGCKEWyo9QjhUqSjY2BfNVZJcUBjMdARdF0NNRN2yuoyRdKTeBjZciyC3wI__HAkBtAy8r4iXAAsizVv3RQ1VG2gj14g4N8VBP2C8n5JaCRmPlr8XHrhfbq03BRV4EYJ4VTfVvykj2Ik-hdnxzLjTVOJvaHKQBvw1Hce9MqynkGW711pWGZOuflMM5n9vUvVLB60X-xxQsrFuHolNwtwRGQ6hVpCK-jni7_pJxQqG7YFfvIIWXQEGsgGHjsQ0UK8aU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گلزنی عارف آیمن ستاره 25 ساله مالزیایی جور دارالتعظیم در بازی دوستانه امروز مقابل چلسی بعد از دوری شش ماه او از میادین به دلیل پارگی رباط.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/27400" target="_blank">📅 16:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27399">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2QR51GhQQpUCHvGWZT3Odcdo6XFriMp6aZkDkqcOFYPDTwFEji2GcUnJtI3uLBguZmb9WgjFFwUX_dTrRzHV1wfw9EAkHIJikM6CNMGuNwJKxCAufrSiOPbURzqpOEH1_PqM2FXhp8wn3YLLcPW5458M5ZbM1XTnv_NvlaUXmUgfVg6Oj8NIiroEIhfC5bEE2BxWI1y88wy6EezspElwEfRvYoKggh7umL8Dvwe8pkCi6WOoao9zTzd3tzsLDAG6nguEVVZ9aY6hGDyUDmLPiWHLcRU41B1ngKDXq9oz6ZuW0OQmDVUKJJA-IwsMOlP88pYBo1Kldii8faxB5Vjog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🇮🇷
#تکمیلی #اختصاصی_پرشیانا؛ منصور عظیمی تا ساعات آینده راهی امارات خواهد شد تا رضایت نامه این بازیکن رو به الوحده پرداخت کنه. انتقال محمد قربانی به تراکتور نهایی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/27399" target="_blank">📅 16:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27398">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIMWlELnx-JODK0hgk8BWov2Sp6f5qC73KKokpRLQAsJcgZ7VnB-HcMyJuTr8SMOCXKNZaI86i0oI-_fDXr2UfUh7LYy4Fi_p2cTnnu0cnLisJIkmVbm-uwVFFzbh60D5YcH6Awwd1YetxfAjRL4LauLpu33wSdaWBQbXDLIE2J1fhx76DiIPm0B26B2B65merParLYuVmqkpC9RKiPG42unPXvlKiQMtFBC6tVUiGOorGxiUgFH2Q8Ji9drMjxaYYKb2TiWO9socWllgp-kS3zyjqpVNO-FuJqjL_l0XGQpq0CW-5GZzKeTcMiEMRjm1c59aeDqqJwKiUQdkE4KlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
جوادنکونام‌سرمربی‌جدیدتراکتور: تیم خیلی خوبی دادیم. چهار بازیکن تاپ فوتبال ایران مدنظرمه که نامشون‌رو به‌مدیریت محترم باشگاه تراکتور دادم تا اقدامات لازم رو برای جذبشون انجام بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/27398" target="_blank">📅 16:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27397">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c0eb7a5bc.mp4?token=nGwbw86eTXyoOGw0aWjQNKPQTDo3kZd0DhAoEHU_6TLTAR4VhLdj6OhL_6zgyzNL3wtxqCdKUWYzWeCacUFL0cDG0Hh5l4ndIX03mmoywfPNW7PvQVWeUaFCUzpUpGHluakvNl-0xtSK2iZCtrMKpIj9NfZyWtdZlAv-xwmAHZZojoSHAk1R_gyCzZNkfbGrKsoJyWXb7i_OlbbENvQr9Guw4JrjYS4Jj2ghgQ1FUEAfRbsmoWYK4xxTs0mK36eKmC5fLwNwvmapuxLM5LfZc2hhsmtl8AVXTpUHgR7nd1XSh95U5dXEX-JmvBq1G9lLtDEuUNgtgxRNCjwZ6-cSUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c0eb7a5bc.mp4?token=nGwbw86eTXyoOGw0aWjQNKPQTDo3kZd0DhAoEHU_6TLTAR4VhLdj6OhL_6zgyzNL3wtxqCdKUWYzWeCacUFL0cDG0Hh5l4ndIX03mmoywfPNW7PvQVWeUaFCUzpUpGHluakvNl-0xtSK2iZCtrMKpIj9NfZyWtdZlAv-xwmAHZZojoSHAk1R_gyCzZNkfbGrKsoJyWXb7i_OlbbENvQr9Guw4JrjYS4Jj2ghgQ1FUEAfRbsmoWYK4xxTs0mK36eKmC5fLwNwvmapuxLM5LfZc2hhsmtl8AVXTpUHgR7nd1XSh95U5dXEX-JmvBq1G9lLtDEuUNgtgxRNCjwZ6-cSUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
ایرانی بس کن؛
یه بار دیگه ثابت شد که تو مسخره بازی رتبه ۱ دنیا هستیم بااختلاف کهکشانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/27397" target="_blank">📅 15:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27396">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ca826d21.mp4?token=hEP5T49n4wL3GDi02yKm9cPjFvwweoJ-1-JuVL2JAfjdtrSXaoaVXC_HjaAbyH4rPcJpbPmZVboLT6lPAHYV41LM7AO6W7DU9C_po4ax_WgSKm4vWy8b_b34Jkq4H2ispOhqgCYqtECk-tRhTUhXw2csMIbZnP_zKJtDR5zFTaaRW4XEDaOB8z9AaLWiAExZtZpQYkNJHu4NGi4UOL1BxeGNWGppKRnePpn6I9WG-QSDiMRQbt-p8NakxQQ02EOt_1Rn0UL6RoDwBMOoE5eJa_Zjj4iPOc3cexy5od4Ki2RNsPwp3b14Z1hWta8l-78bZgsN1eEWBx6PVHJP63Gbnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ca826d21.mp4?token=hEP5T49n4wL3GDi02yKm9cPjFvwweoJ-1-JuVL2JAfjdtrSXaoaVXC_HjaAbyH4rPcJpbPmZVboLT6lPAHYV41LM7AO6W7DU9C_po4ax_WgSKm4vWy8b_b34Jkq4H2ispOhqgCYqtECk-tRhTUhXw2csMIbZnP_zKJtDR5zFTaaRW4XEDaOB8z9AaLWiAExZtZpQYkNJHu4NGi4UOL1BxeGNWGppKRnePpn6I9WG-QSDiMRQbt-p8NakxQQ02EOt_1Rn0UL6RoDwBMOoE5eJa_Zjj4iPOc3cexy5od4Ki2RNsPwp3b14Z1hWta8l-78bZgsN1eEWBx6PVHJP63Gbnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قرارداد عارف آیمن ستاره24ساله‌مالزیایی جوهر دارالتعظیم به‌پایان‌رسید و باتوجه به اینکه اون هفت ماه پیش دچار مصدومیت شدید شد مدیران این تیم هنوز برای تمدید قرارداد این بازیکن اقدام نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/27396" target="_blank">📅 15:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27395">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0574804636.mp4?token=wAdoSkeSMEXK_qkSM-K08PNiq25C4YDpucNf5BVLoEMVmR-BwuzHpqiItOvu520H40cUHHhyZv8NOEACeEC-kipE7NgUdl4kLJjCfysMMLQpPlLUpfr6j6ZBNoJnw8g-lmMNnaxcrjhp1RkBShfEFwaJiG-GK9VJbHLn7e9DhooGB7d9pKCy1IpNAUKSJJcKmRXa9-gUAVvFIeS9DIE2qF17vPplOBKi9u6JbhMZk2KW4SYFtv4CpI3npcteqRr2FSTc8R3CHGn8iMLW-Bg3bl4kjNtgkk31TSV4WPg1mJbKOU18c1mIQ-7zzVv7rkuoTjBFdzonwmcHl_6aAHyDfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0574804636.mp4?token=wAdoSkeSMEXK_qkSM-K08PNiq25C4YDpucNf5BVLoEMVmR-BwuzHpqiItOvu520H40cUHHhyZv8NOEACeEC-kipE7NgUdl4kLJjCfysMMLQpPlLUpfr6j6ZBNoJnw8g-lmMNnaxcrjhp1RkBShfEFwaJiG-GK9VJbHLn7e9DhooGB7d9pKCy1IpNAUKSJJcKmRXa9-gUAVvFIeS9DIE2qF17vPplOBKi9u6JbhMZk2KW4SYFtv4CpI3npcteqRr2FSTc8R3CHGn8iMLW-Bg3bl4kjNtgkk31TSV4WPg1mJbKOU18c1mIQ-7zzVv7rkuoTjBFdzonwmcHl_6aAHyDfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دی‌جونای‌کارینگتون فوق‌‌ستاره سیاه پوست لیگ‌ زنان NAB پس‌از اخراج‌بدلیل خطای شدیدی که روی سوفی کانینگهام انجام داد، در توییتی این اخراج رو‌ «امتیاز ویژه برای سفیدپوستان» دانست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/27395" target="_blank">📅 15:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27394">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-xXyERwcAXVvGdEnliWIpdXcbyK4tqHujuBlY9-Ixex-uxjCSLhMmg0JxxOXgHOcvTD_93jww0YdEpqFK70xgSHt4gcjjf1s5YSRC2ofec2CTY_UZPGfZT4JTWiFiEg282v7eEXjhYUsmoqf-hCNLnbdHlp7LnlknC2XeFACnCyfCMiZBWZjUPcO0D79vqsjWrw2PoCWI4U3drEhgHi5-NHEMTAg1xSijq6eXLgDznFLrRYP9mUqmaQScLt63_ZBoul29IHwzWXeEIEnJ4hLhvJGyThp_mex91PgB-lUTmAatHg58L8-9ZANdDVz7mqKqqKfC425n4jtw1JjYyVEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ حسین ابرقویی مدافع پرسپولیس: از باشگاه‌سپاهان‌پیشنهاد دارم و مذاکراتی‌هم بین دوتیم انجام شده. ظرف‌چند روزآینده‌تکلیفم مشخص میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/27394" target="_blank">📅 15:26 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27393">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q79S3xHAHa-3rnJ0aRhUc2iG6QI93cGajsPCZtmWbCCmapHMs1DoUdKuk-PthMm5xMdaQfvddnhJdVhOw28NvSzPjvDEVdyiX1LeXnt6RWMUJBQonogOhzS8d3DoUUpRz92wrJZELjctD_nPt4WsKOUlzae0amV_y-9TI0iNyHeI7_h6OSrXS7AV2QiJ3MDLh1ETtL6hV-KtYIatY8PsfvUF0N0-eiI4SdNfr0dvfwwFS1T5fuiO7FpK3BPQPls5ODe7SSE39uv0AnIbKzPvVTZhXNU1esFOpAoFFH0MBlxjUg14vnCno_rdJQgn-e35Wx6RfIsH5W0X4ZnDT4J17g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اینکه‌گفته‌میشه؛ باشگاه ماخاچ‌قلعه رقم رضایت نامه محمدجواد حسین‌نژاد رو 4 میلیون دلار تعیین کرده کذب محضه. بار ها این باشگاه به مدیر برنامه این ستاره اعلام کرده هر تیم ایرانی دو میلیون دلار پرداخت کند و خودِ حسین نژاد هم راضی باشد این انتقال انجام خواهد…</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/27393" target="_blank">📅 15:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27392">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfwCq7S2RPF5k1vDkM69ujI3WUuj-tI3_VSokKg6Oh5Qmi8tqRB0XVP7UkAwqMX2Y5KtS1Eb0d1tKfHTCs1N4TiyNDLlm7W8HEuTd9X6cYGKSfLhmWQRS-HlQ-pYB-qWiYbJdlA0c_RClLXiwJyKwOTPuctFKlRTpntLPzySU5FzIF2LL1SyFuIBeL9mJb4hm0eTzGMK0mJHMerPREZMsi3uFx_7HjROuLZ7FJCSmgxN2gtugR7POFv6qWCfPIjbtWT52BrswzOyD-BcCVSSjdexID1td76KefkfFTwRL3NrjfJSZOUs7-Hsi92BA6lOnecZETAq54ecDdZmefB4aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
جوادنکونام‌سرمربی‌جدیدتراکتور: تیم خیلی خوبی دادیم. چهار بازیکن تاپ فوتبال ایران مدنظرمه که نامشون‌رو به‌مدیریت محترم باشگاه تراکتور دادم تا اقدامات لازم رو برای جذبشون انجام بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27392" target="_blank">📅 14:43 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27391">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3c4Oo_JenML7-asVbjQ3cYGHS2DiuS_0EdIm_GsFRHoGcEzOnZXI-g7_m6-OcBZuzHabSr823mH_3y5dxQBNDqwcn-xVYaZyzcCzCScyv1YFp3YrB9okMqRE3lm2c3oii7tNeA8dDtebxKlwvD9GQ4XwNZAosm3dUgk4yz5y8i1Gi1NDC1HKi1Gc_DXyS9IQQzMx-8qdLqMAWn9Taz54XOFxZ-dcw5SIrhnSpe8qcDpSYDdSi0mE-4jO2beqjTjQdv4bcZZH285zfjY6QpqtXWTdiZZKeagwQ--73acIvDfe8OV_ZXhhoZXcO6xMS4OwwFdkDko2_FXV3sT1b3lVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ احتمال داره جواد نکونام از بین صادق محرمی و مهدی‌شیری‌یکی‌رو درلیست خروج تراکتور قرار بدهد و درخواست جذب رامین رضاییان بدهد. محرمی رو مهدی تارتار برای پرسپولیس میخواد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27391" target="_blank">📅 14:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27390">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BubWOj4krFBBZ1BCj7KIwas-d9iK9Rwm8cRIXkLYtiDy2BsBsOyybn7axSYHcCzxBgoYFwIcEfqZWgPfe5MUUrx_gBPWpwrCn_o0D8tdVpL3RBB3q1RkD9cTaA-19BESyyd4eX0VcjVkSUKU1Dgfv2cTNL1V96IiKHU8CbhR6DzjJIArnxVsHz6qkIHw0MRsdaK68sDvKUilEdmIlTubGSwbVhqQtv_q1V3yMPBqt92wOfUiqOzwK7ujxKqurh7BT_RFGyiSQjZNmah5jOasbh1Jbx7GUzuojli53jn2lvfaWJHr0T_OBoOXJ0f5M8dZ5Wq947n42L8Pj0fiuJO4Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ باشگاه تراکتور رقم‌رضایت‌نامه‌صادق‌محرمی مدافع‌راست30 ساله این‌تیم روبرای رفتن به پرسپولیس 100 میلیارد اعلام کرده و از طریق مدیر برنامه های محرمی این موضوع رو به مدیریت سرخ ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/27390" target="_blank">📅 13:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27389">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxCwlWAz_GmjU3HlMyHYsUxeRed24CyzYZh4UgnNwf8-5VUi9_wXReMWkxI2ZVfrRbVqolNfX6rCxzmIgSiVdupkwG2MKZ2ms-GUjjkFtAyyxlO_G0OISUAzJphW4xUQZYc2Mf4JVbd1_WJiV3pwl6WR5o0BbvwyLiMTMTxnMyLvZYHqIopQIr5biMmuTvYyhQg27OAs07oOuRPgM4KpSgbS660h6Qq5wlpLsMOYhoMH6RpkVhR0wTbA8gaCIE0bBJt_lz6hqchtjQQ6nICGqE5jGuZt3l8_w9y3leOaVNY_oLyBvu0ssETbLXdUVbzVGVi-HwSfXYIZyAJcxtcB9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🤩
با اعلام جرارد رومرو؛ دکو مدیرورزشی بارسلونا هم‌اکنون‌درمادرید بسر میبره و قصد داره که فردا بامدیربرنامه‌های‌ خولیان‌آلوارز جلسه مهمی بزاره تاراهی‌برای پیوستن‌این‌بازیکن به بارسا پیدا کنند. چند روز پیش مدیران باشگاه اتلتیکو گفتن آلوارز خودش رو هم بکشه…</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27389" target="_blank">📅 13:27 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27388">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-waFUP0ew2uWAirOrjQvuCrPLC0DywYF3JCrNjJygAYR5qJkYuGQ-bc3Mw4ksGBClKEj2IErJdJSLKINp1sRE-LvipdCNdHn7ESqfyrczaHejnBt6G_Kryo0Gq223xcBtUfEXQCDGWGnQCUWTMj6CsG4F_n0WktvAHTsf0_lmjvLWZBZKyEsgmnh5R6OOECpNo4Z4ksxO0iyYW7wyWF52yNubYrMRy1A1fpt0XYLTG6PyC46kcvwRCL_XzhtKBrLDGJei5cbYADlcK3gsPcql1LqLF2urxSlo-uAxzaKFD2O1kh9HZNc-4dS1uEtoD_vyg7bfWtstmSyISotymj3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی 28 روز پیش پرشیانا
🔴
شهریار مغانلو مهاجم سابق‌تیم اتحادکلبا با عقد قرار دادی به مدت 2+2 سال به تراکتور پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/27388" target="_blank">📅 12:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27387">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/222f7c35af.mp4?token=GBilFZ5rgy6en7S0uMzt7uY0hZPJn1kjqiOCRNr3Ai9TFCoBSz_KXNvc0kmqfb6UlZpL0UAkVHyp0gbBCHGHdmOhdMtSXb5MaXPjCObsiLIZVQCxx9lECl3uficxwORrs1BQTuFmfCBQtykZVgzBoc7UYyY0z1M8sfuqOrSmDCfJdp5ubVuaNWx-mBTRpH5X187v1mPg05Fjhrh7GdRISaHenckOImpTtmL_keEsEV45cnD4GYkYuwDnx_gsDRPJhdusgMSn0vo1eZHRGOCBLTbR_Upo7zLXam8UqD7b4fxdtOt1AqMqrrZbh2nNWCKeFW5_HSpBh6L3MmuLR_mPKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/222f7c35af.mp4?token=GBilFZ5rgy6en7S0uMzt7uY0hZPJn1kjqiOCRNr3Ai9TFCoBSz_KXNvc0kmqfb6UlZpL0UAkVHyp0gbBCHGHdmOhdMtSXb5MaXPjCObsiLIZVQCxx9lECl3uficxwORrs1BQTuFmfCBQtykZVgzBoc7UYyY0z1M8sfuqOrSmDCfJdp5ubVuaNWx-mBTRpH5X187v1mPg05Fjhrh7GdRISaHenckOImpTtmL_keEsEV45cnD4GYkYuwDnx_gsDRPJhdusgMSn0vo1eZHRGOCBLTbR_Upo7zLXam8UqD7b4fxdtOt1AqMqrrZbh2nNWCKeFW5_HSpBh6L3MmuLR_mPKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برگ‌های‌ریخته‌شده گزارشگر بازی امشب سپاهان و ذوب‌آهن‌ازپرتاب‌های‌بلند نادر محمدی؛ واقعا قابلیت خوبیه بشرطیکه‌درست ازش استفاده بشه نه اینکه از هرکجای‌زمین توپ رو بهش بدن بی هدف پرتاب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/27387" target="_blank">📅 12:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27386">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeZooYH0A8XgHlXGciMg4uqIk9z9f_r8ZNgpXgDXOxGmwFtlfTQTYRWOv5MQnm8v_McTFPTQutXoNPA_-rITM6MJNAXj_pOgQdFNq3y9IxcHG6l0OhHt1RWlER_k2UuQvaEAA1HZNSwMu8vqbfH6GfgJmvWh3JZj2k0BuuTW9ZvMseSL1KQIzXiYIwNOUZzwrt7VT5GCGvS23-OZZhqK8Bqcc0SRtATAdCoBnGrcnwHgWq0YQbTOeoduLdkZKix7_imr1n1A8XxeBnF52nD3bdw8UpHG0vZ1Kvs0kJGHT7Ju0puTNawXUcU2V70iEcDPIwbfTF8iFFTJQvQ2_NdRGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
👤
طبق‌‌اخباردریافتی‌ پرشیانا از اصفهان؛ مدیریت‌ تیم سپاهان‌ با‌ حسین ابرقویی مدافع میانی 29 ساله باشگاه پرسپولیس مذاکرات مثبتی داشته و درصورتیکه حسین‌ابرقویی بتونه رضایت‌نامه اش رو از سرخپوشان بگیره راهی اصفهان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27386" target="_blank">📅 12:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27385">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJpr4PlzgHuHZoprrBOWxRHmWkPxi_QTzJ2Ic6Qg-mTKZyMPy9VWGLfkbl4gKsvmjqigjBAhwhsiqpITEnnodgWO5SiZaHFlqSJgd3E2xWW2Ct4axRevuWf7hrilf7DxgydJY3h4xZKdq_BBcgxHa6cv_OPvqaOBuctbqvQ5yskx6L6qYtwrYT0SSp5UtHPSaMOtU-yRd4TMB0gSDs-qv3E8kBF5tbjdOl4Chr4TrB7rOnPWEAvoMm2vco7RIlusXAW1240D5OGTjj3jTUzCjZ1ZPrqABUYvjyBqNAAekQVJmf1kBWPK8sAuzkJJTnBdyVKI7nGgpbvhFtDdcq2xYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ بزودی فابریزیو رومانو خبر پیوستن قطعی رودری به‌بارسلونا رومنتشر خواهد کرد. تمام توافقات شخصی صورت گرفته و توافقات بین دو باشگاه نیز در مراحل پایانی خود قرار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/27385" target="_blank">📅 11:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27384">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFaYHqnafekjzNSTRfA9ohLote40uYQVWAytzxlxejvFWvFQ1OLemTbZwPOfPBgGNUBFbEhVJGyWeStNDx3aik4o74OyIuaCRFBnkkdBnV7MlrJq-VO8l6pzvIs_rWjfjPlFDEc5AsW2kUL0sOv0gC8Mq8suVKEu48oLZn-bEYM5zand_hII-FjZ8mJERinWosR93M8_Ij9NE8vTX1c_qxRv8v-XsXf5fOTnIr8aOUh8ylhGN4HGprQL14pIEDxsHXkz6TeRpe7cV0VaOaX1Bywb76RI5qZyT-R90clztx9iTh0HFT564GHepRenaKmYcPD8lo0WT73l8yvmW4EQFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ عجیب‌اما واقعی؛ رامین رضاییان تنها باپرداخت 100 میلیون‌تومان قراردادش رو با باشگاه استقلال فسخ کرده است. در واقعا زمانیکه نیم فصل باشگاه استقلال قرارداد رضاییان رو تمدید میکنه بند فسخ 100 میلیون‌تومانی‌درقرارداد رضاییان میزاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/27384" target="_blank">📅 11:41 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27383">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5uJogCbcOa-kjKssPL-JQXaL870VHS70teTBUFsGI3760EZ5Yuc9bb2ozf0PuHMGg1YBbg82ITZzbGJDbLStZ38XPQmmvfHI4g-mTHgRdKlBVpmbUtOx4_tWAxTAKgXobO7a9lkRzmu_86n9twYrZ8wCkoqvdRQSw7TOmwPp-2mCorFZ4yq3tXy7TtxG5rver0i_kaq4XB53OTvZY6OxOrMfIeV0swj8pcXi_L5PJ6IOUCqvqlb7qUlMUqOaO_wp_aqIBErlXHklX-ig9oLCY2YUpNeVO6sFbFITGiKn9oeuP6an6JxuRuSyZWkuuesbCmSaQBJZsiycMpddVUmsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌رسمی‌باشگاه‌تراکتور؛ جواد نکونام با قراردادی سه ساله بعنوان سرمربی جدید این باشگاه انتخاب شد و جانشین محمد ربیعی شد. محمودرضا بابایی چندروزپیش گفته بود اگه بزارم جواد نکونام در لیگ برتر فعالیت کنه بی ناموس عالم هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/27383" target="_blank">📅 11:41 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27381">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkjW4yO_O84GqohjBgD7nbisX94lbmTPD8zZ7qZlr5t6URtOnlANSBRRQOj5aia-NfURcsCKVBjDgs5ngahBPlWZuNgV2gChw0eSwLOMpaQ0tpNuHir7ahFKGmv9LCeQtgA765BMIE43NRM8y1cDsQ1FVLwzSi5O5tBhgj5WcsuXJbvrzp3XCRdMwTH6ykaES8SLTzdOCfQspIzjyyssbjRZ_bjWSO4TtSoTMojlxb0hbY8pN28Y7_I9m_XRCfOOj8ojI_qoWsQuBDygziEOuLTaNrRrXR2whJ1YpWhGf_u--umjMqYxmogFVWOjTtgnTw3kKA0Ze64XM50C88y6Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌رسمی‌باشگاه‌تراکتور؛ جواد نکونام با قراردادی سه ساله بعنوان سرمربی جدید این باشگاه انتخاب شد و جانشین محمد ربیعی شد. محمودرضا بابایی چندروزپیش گفته بود اگه بزارم جواد نکونام در لیگ برتر فعالیت کنه بی ناموس عالم هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/27381" target="_blank">📅 11:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27380">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9jCg3UDrkvdzc0bjRWDXmQz-ZzAlY38NIY3hqGn6IzRln6GFYe5a1atILGMxX-KkLGiaMdFUkaWi4sT2YHYvNUAWYV0lPx1sOXzajeO6yzUk5is4y324zhKBjJ7pz13qTymFOn05V7ysqQJKgXlLNVySA-f4p3gLpE-rKPlPLjxxFQUB0rDZcGFVgRR8jGTiwPBQ1WtylQQGvRLAcJlt-GuFHNw_ZlaDVdoveRM-Jev-WrqIF1GCvPzUnS0k-6TPmT7aqdPqZTqACJ9K2y-St9hxfPV7ymP0mmFVrf5G-h7nEW0uBHSC3vlGCOqf3tVmG7dtNOnOBM04hEgAgMyJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#فوری؛ در آستانه شروع فصل جدید لیگ برتر؛ حجت کریمی مدیرعامل باشگاه تراکتور بعد از توافق‌کامل با جواد نکونام برای هدایت تراکتوری ها محمد ربیعی رو از سرمربیگری پرشورها برکنار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27380" target="_blank">📅 11:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27379">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwIvzdyH1VsWI9J_Qe_JsL0Vr9pUhONk_XIvK_2ecCNdEiCWUaxCzaYHzmrC6nHWtH5LjmTo2jeyZ45-5JoVdPmIa76Jm3kPykGYuSd3nYJKt4NoijMvXkNbrni8aFtoeL-VJbwurb7HgV9Tn0wDvVtPHHSe3hIDADl8JzZxNaIpMUxFb1yByFhHWbFyF94lwZ5KTru-3kgAjZk3AVCNXyNH_oO-PMUMBtVevEMVbPl9mWTbvn1d4BrUHJuwWyHBkZRm3csAvXAFeOhYqHvHyJZWSlfSHx-37fHjD6lE4tRbx8jX6QVolvjyQOLF_qN4k9jP8cMR8QZHEwM2U5ELXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛ امیرحسین‌طاهری‌مدافع 22 ساله نیرو زمینی باقراردادی پنج ساله به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/27379" target="_blank">📅 10:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27378">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ox_puldqYzy-u8yShFhuS7zMHI9_b2ACArT79Oki5hknxMFfl_qsny2ScWGpRtRFOTXdbzup24BOuxKYEhk-RMTiPF1OSvc51SBniQWjRRFlXF1fTRBTzzZkINOl0nz6ujkc73EhXUiIPHS2JIAgvPriQksKXeGpaRhfE9GdeSbqyoXykRp27s6LTwhmvunO1sZd0kKSHL7DatncjwyRQRQbbvewlEbAIVROnH8CYQ3-BrY6i4QiBQJyrXsMHHwDbgvufPgCY6JOKn2S23q1S4D2u2Vths_LY9fkJAkNdJTknL3G5WY5-rAuXt4MCl1mi6qrYqVZ8C_LQwfIi8Rt8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق اطلاعات ما؛ علی کریمی از تراکتور نیز آفر بالایی دریافت‌کرده</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27378" target="_blank">📅 10:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27377">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HV62cP_IAaQaX9rirmuFAnp27X2n9EvMg4SfY0IeWTLh4qaK_oBP_u1UlMPGflFB3BvDEumro5rsjp76I1HftzGkUDP6aS3tQyheEnLh3PVzUNin_WA-RtDmyfqaa6D3fOWZxmmsB6x4xhygQyuKtLObyLBbwzQUG9IvS8I4X7LE11QwjU6UESlNoLnzS_-TDwOIlmUReB9hPrMYP9ZfKVELlwT853qeliPI9u6qkRjK45W1AasHfx0NsnhDIOLe7vbH5UjBqyjrt-pw4xZOtQrV7B3AXyUjybt-MXPi00zrsUJighNIFYED9O6F9igp7n6TbQNpyhVb-PVcHHdzcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#فوری؛ در آستانه شروع فصل جدید لیگ برتر؛ حجت کریمی مدیرعامل باشگاه تراکتور بعد از توافق‌کامل با جواد نکونام برای هدایت تراکتوری ها محمد ربیعی رو از سرمربیگری پرشورها برکنار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/27377" target="_blank">📅 10:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27376">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzGg8pcOlSnyzJBncLtly67wsNaOqg4zGFCY08DPbjFiJi1DbTpj2apA2FgfhodWI94uA8iyatTNI89Qc4-Fk3uBUDwZskfFG2xRNmne8n60D6mDxC8eT_3rvvWFpPFaYkVV3rUSeEb2boHlw_uUayPT25jgOpa69taaP7fnupjbJvJL9zIwvkTgmjWtWuwepsXCYV1hCT_uYhJVrN3U9Jay0GexWkK7Fd-LiUdfbZ-ZhXFxXCTyKbyDmVCNUOa6sBWmJEhqFH4JdLj8SLYaxONTfcf9zioZp8qcRcTKCNM2EnGFYNoJnSYQJPsGYBIzT3nwi9eDn5D79E5LMPC1xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#فوری؛ در آستانه شروع فصل جدید لیگ برتر؛ حجت کریمی مدیرعامل باشگاه تراکتور بعد از توافق‌کامل با جواد نکونام برای هدایت تراکتوری ها محمد ربیعی رو از سرمربیگری پرشورها برکنار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/27376" target="_blank">📅 09:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27375">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKo9ukNbkPGacM0XL-K8df5wEYxPirZPBFcKZgmFWzI0NyAqxTFkwBclzjqBAyITGHGohQU9pyM2HOopZLN1q5FiDQRo8JntxuCwzGsexMiwYnLa35Ln_PAfNBD_BBeK_b-TzJAa40DrZ7ePol1GDgiYHutZwy1bPuLgD3AEL5Fo4aWwgVpE9AbUSiFLM8q_pCm99PH--P0rSrs1sBeGYXdPSza-_ykAaqFkHZWSm9NIxR2JFNgBuY1HDeJLDQYKMmuVnK0Huqxh9Ry_A3epoH1DuJHwfssH86ky7Xdzkfdo1sm5ONk9v4PGP9n7Ufo7dEwt6p1gdgKGCCXMpF1xAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#فوری
؛ در آستانه شروع فصل جدید لیگ برتر؛
حجت کریمی مدیرعامل باشگاه تراکتور بعد از توافق‌کامل با جواد نکونام برای هدایت تراکتوری ها محمد ربیعی رو از سرمربیگری پرشورها برکنار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/27375" target="_blank">📅 09:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27374">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZpYdTujstBmkXUArEoiohgLQ80g5cUzLvo30j7NfbaEq-5epmCDfYmUBNlUbMFyEbuaS-zzUwaouaKLHzu1o7AtiG8RKJsYas7emspaMSBbM0odGZ9qHO5ednoCkHGzAon4HPZhEyD-D_PYAudylfHjYj2nnGnn4p0PdmzeISOwzRsJLx1wmhSGB0FlN355fNZXnZ8qp2YiullZn4rfozyQNx6aA6GB8jBR24nUDtm_2UguBjQOBZmLWrEZ_kxCtuDO-LRKpW6GD8JYepNTjzJEdYFEOdg61mDR2fVZWBXYJ2yhzigI_WwxhClVxStp9uJaDUJhyPv8BYKULJRjqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به‌مناسبت‌شروع فصل جدید لیگ‌برتر؛ 10 رکورد تاریخی باشگاه‌ها در تاریخ لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/27374" target="_blank">📅 09:47 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27373">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXdA0sSzJt0GEV2aljWyMDEavuN91DNMM5XSzGa0sUYPPQrX-J1itzgHu3ON_3n3K4-NmQ2N2tZllvUB_5ZzaI_enjrTQpzC1RuKbNzVeR0bO7qq21wFQ4kvuV7fvPS9zH6lOGNCGxRaEHrkKRVbsb6p-ZFzT73l5V5JG44FRzLTpEf8wBO8ZDo9J8MpX4LNzQtfeN8r9EHOCF8_pGdqTDM5RpLitaPJmOZNnX6DOtSiNqrMhwByHjAtI3MfYyl_cn6FONK020d-oDcRlQFExvLLdjBy0rwN_XPmR1tB9QjUktmltYPqUVF4jKPME9Ci6yNUfmlgGoGAs8Qx8bOLWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خورخه‌فقط پدرمسی‌نبود؛ ایجنت، مشاور، رهبر خانواده و... هم بود. موقعی‌که مسی تو رده‌های پایه "نیوولز اولد بویز" بازی می‌کرد، دکترها متوجه شدن این بچه مشکل هورمونی داره و باید درمان بشه. خورخه‌که‌از پس هزینه‌هاش برنمیومد، این هزینه رو از نیوولز و ریور پلاته…</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/27373" target="_blank">📅 01:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27371">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_9_rrdWbvgrSEYqLzhFIl_HAv08o1jdGZcnJ7TE042ha6_ovRi4d2XkkkdxrAFw5Xt5T4CjOjgjGkmSkdvlbONlSpI8CAs7lsWeoL9I-xkmmb7PDT3U9UtR3-qO7qEnSwniEeiJb49dqjCvodiPcP3w2KKFcLbl2OERLv1t8arQzJKL3C_MtOB1GOIsG0H4moyjnj3iTamF96USGTrpibz5DJlemN8e7N72bdURaAwfPwJZg_l0v68M9H5FkbsA7I_3Jvs00ANbyECtjPAr82-69Dik1DIQjHKHPeQZipSVyBFLdRavAlo9cHyXWxFzyhUtDCy0bknoCz0dzWeRNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌‌امروز؛
از دوئل شاگردان مارسکا و سیمئونه تاتقابل توپچی‌ها با دورتموند در امارات‌کاپ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27371" target="_blank">📅 01:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27370">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFXRhNf0N8g15EjtllTD5_wpEcoK96jLtJfxiLYof_nS_nFpszPqPrtmZ_vtIzbjFosplbv0NEawT2RW3e0ENAYqek9LtiZsFKTmx2tHOUWi8_31WW8oZNHTYXLUsxiXTHcs7diMP_jTFDflBFyEx33lsAAaqz2AzUzBRcPh240cE06bEC0tlXn6s_xOssbeX7a3YnZVOshid11ZIEdnWQb-8xFHlTI-J6cn4RJmISNqT2KPeGL21Q1Q4fo4eLZ9AM9QIZ_BgDal5yNsBR6snkX6_ISl3RNszpVXRtSaDxSvmZ26yoZgDLjG_WdgFcn_2wEoWa268JyczNus9eU1kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای‌ دیروز؛
شکست شاگردان آموریم مقابل چلسی و تساوی در دوئل پاریس و یونایتد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/27370" target="_blank">📅 01:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27368">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLy4dHHfD9vrlD5MzTGJ_O6EaF_uwm6yrntl-I7Esx09VPpLD1SlWaJvYwjkJtzwFA8O2BlQ_fR9AcWLHCqYTJaF1wEoChvgwbG8h0os2lXRqvMJF6WXRQvHegkY171f8XUYm_LuPPHjUhX1gUXl0W28V8qHG7UU84fd6xcIrfklONVeMTgNkuC2TdAnWCAowzkl6VqgCvEPgstMSB4py8qzDr-TjdyXLXwbHqYBeW1RbqmgkCEvzLW3GXPKAqkQbvIpeXL3xmKIHfdvdd8EUCd0mkzs0dqlfNKsykpOFZ2XuVbBh4VxEf9PgMUTM-1ipAykQunNmu_uZ1RDkv8B4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری جدید خدابیامرز دیگو مارادونا افسانه‌ای برای درگذشت پدر لیونل مسی که آمادگی‌اش رو برای پذیرش مهمون جدید تو اون دنیا اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/27368" target="_blank">📅 00:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27367">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O-B_Z9ihbhH5OUhgxKhqA1OhbAGTooSadAL2w3x5fz3X3-lDzS4I46Us07IFyMpo5IgvP8MCqzT4j8BhIm1Yy0umLj-2EyC2vEm55DYScm3EUkyTRV4z7fcudZLU_Bj9Bn6WcETignatGfOLEz0pV9MZqK86CdS_njL2Ac-7qJEABxJcQ2PP5F8wEdBPoa-o3TkNET5GWwg6FiWGCKIcHyEWkwLrLleR1mEuW0sZjGWXsisNzvyPv7QwUhR4ESCQt8XnIAeQaB0-PD8O34fIsEIJJFHUyhIg1wl_hD9Or7lZYSKOhw5H9TSIbkLQW447UqX1FP1Xo3jC1k6880mLiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
از پنج قولی که پنج ستاره تیم ملی اسپانیا درجام‌جهانی 2026 دادند؛ دو تاش فعلا عملی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/27367" target="_blank">📅 00:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27366">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKr1lrEZGOE4mTdtk1389hDvdLyBLS0Z2dP892xq89DFNE_zGstEoIT5vrcFxp_PmuVUMAyIwcff8WW4UyXR7nKX2FxllAcwOa7UvjW2YBB4VhG_PoO5K395PG3bIGykvWNy_T0oj8k_PQJXtHERUrHH51ZXL1YbZGBzf1iT4DEmSe82t1BHCE4GTcbapXP6jcXx741sDGjFk00SMCDdVwkRppSnBZMk9jo8rv7MHkdcYusjrNCPb0MFPB7efxiK6sI0Y3-v1VG6XrSroUrHLMOtcufS-WLLZpDQHw3KE73MyXLjmC2krWnGgL95WdcoMMVwUaMNOm2-jgLvt2Nj1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا #فوری؛ درصورتی که محمدرضا آزادی مهاجم‌استقلال قراردادش رو با تیم استقلال فسخ کنه احتمال این که راهی سپاهان بشه وجود‌داره‌. ایجنتش با مدیریت‌سپاهان مذاکره کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27366" target="_blank">📅 00:26 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27365">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6sv5DQKcJx-WTXHvO0L8Y22rArtFYkBXk0Uojg3_bfmDvtvSb2cOpA5L4ss65H9T_tnwQaATvBA3b_4T7O6QW00YkNHPxKC7532DeIeHdOYcYRP8ntVq8RHqxFDoNuuQpGc8h6-_y2otO06VQAZgXqGpN-2-FeTJfkbwLEdHTCsuFWWfqW3oOT2WKN116bcnp2safcEHNgGbKCUwXLjYYAHpRa0i9PRukIyZwcvNOKHR42NlC1y1GWvqddqJOgULTj05pVToJD9kKX2weT5CwajtrZ5nNPuNZy1nk9LwwAPplIkP_SyrkpBHdmjL6udIVFDej-rObsg62SK0l4HRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟡
طبق شنیده‌ های رسانه پرشیانا؛ یاسین جرجانی مدافع‌میانی22ساله‌سابق آلومینیوم اراک که فصل‌درخشانی دراین‌تیم داشت با نساجی مازندران و سپاهان اصفهان مذاکراتی داشته و بزودی راهی یکی از این دو تیم خواهد شد. شانس نساجی بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27365" target="_blank">📅 00:18 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27364">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urXharjrTq0mp7c5VCIDzUFP5vcn0mV8bYdtl79HzqdnptKh4eJFFzfGnBUEcZiUbsHnY9t-p3LM1rnPoa09Iw9daD_Njge-MppRaRTjgSWT8DSgrWNY9qMzVzh8cf9px_AFYKSEtPtNZv26oJI03tqvmevFpBGqj0mIJTBzGX0ZD9qJaN3xtMHane51tFLL2nzOhbXyXIu4O-Z1n21nlZVzP2iR68w8N3D0Dhe48mxFS5fSyvedX9S2TpvPs9Jbknmdm0aLfzVaHFr_pG2bmIxAPWXIEvjHvWdnQB6RkptGde0AvUzTemzCAqQAsu1I-2srCh0Ri4QrsxnssVs0YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
مسابقه بین دوتیم استقلال
🆚
پرسپولیس در هفته پنجم رقابت‌های لیگ برتر برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/27364" target="_blank">📅 00:13 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27363">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbbE3FBXYyQDTc392t1ITrqN7ppWqCAMvkazgrqoxmH_s2jjmksEkUADajjKFhgQR1HIBFWZEwtqKrhiMLXTsnnhMGPcxCTr_TBPx68WphWfJq98MdnopY2f9L-SfTRfwRAG9kWXlLzWMmmPv4TrlHIVb_58yWevq_UwymYcSV--tbktWGOS8X_7YuLRh6_ux9pPSEvh51Wli_NuXXorHuCJE4BFU-DHF-cRYWqsgyieXeoLVcOMvpXE65Z_hiTECUuefIdBV9wVj8CJKG_BwSd9bfYMYO4gWFjsBtNSSVo4daX5Vtyhi4UqIHLr4D252Ql4yJQHQIVRpITB8VTzJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خورخه‌فقط پدرمسی‌نبود؛ ایجنت، مشاور، رهبر خانواده و... هم بود. موقعی‌که مسی تو رده‌های پایه "نیوولز اولد بویز" بازی می‌کرد، دکترها متوجه شدن این بچه مشکل هورمونی داره و باید درمان بشه. خورخه‌که‌از پس هزینه‌هاش برنمیومد، این هزینه رو از نیوولز و ریور پلاته…</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/27363" target="_blank">📅 23:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27362">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f50f562360.mp4?token=bHB7a0GeW3ho5ZD5NRj5B2aEoKalopEXTZhSmJVaQKzWf7oHTnxy3kD6ViQCXH5ohYyNtTgkhTdi5Yy7V9teow5uAT9FhPHBGwKuyh-SWJUX7OzIlWGtxuFG2bmacbZZ4PrbG8DvOjLBmrqS3x1rjUO556hU8JEmaxCsoXLsqKU0Kuw7P37kcjgQU4RbgReWTJTxe0vRRQf4JXir4vgd2e3DlwwtVCYU4PWN6uoCkZLw40IVCjXwM6v7Z9jG8xadyaYYXLkdD2zSGpAKEE9aOtDtUwzHK_5ahe38uyHz7TCEiByaZbenqkaxJRFsNvUfTZVKGw1MHaqiUPSlOohypw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f50f562360.mp4?token=bHB7a0GeW3ho5ZD5NRj5B2aEoKalopEXTZhSmJVaQKzWf7oHTnxy3kD6ViQCXH5ohYyNtTgkhTdi5Yy7V9teow5uAT9FhPHBGwKuyh-SWJUX7OzIlWGtxuFG2bmacbZZ4PrbG8DvOjLBmrqS3x1rjUO556hU8JEmaxCsoXLsqKU0Kuw7P37kcjgQU4RbgReWTJTxe0vRRQf4JXir4vgd2e3DlwwtVCYU4PWN6uoCkZLw40IVCjXwM6v7Z9jG8xadyaYYXLkdD2zSGpAKEE9aOtDtUwzHK_5ahe38uyHz7TCEiByaZbenqkaxJRFsNvUfTZVKGw1MHaqiUPSlOohypw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
هایلایتی کوتاه و خاطره انگیز از عملکرد خییره کننده الکسیس‌سانچزستاره‌شیلیایی در دوران حضور در آرسنال؛ یکی از بهترین وینگر های تاریخ و یکی از دست‌کم گرفته شده‌ترین بازیکن‌تاریخ فوتبال جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/27362" target="_blank">📅 23:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27361">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTMQBVuWeB4ZuWTz5izIfw2PAZMb19eMpMkni0M7-XjwUR-hk8c5zXw8_uryUfjr7sTfz7Ytr37HSQDkse5B2pYNh2Ewb9yrlJhthFD_Fv52laWanv4AIcPO8GRTggSfBzzkXyKOKtF2PMvhni11GT9NKxBBAmRjtKpdOyybdrpgMqfUEG37CAsazct6I-ZKfKZ6ADlf9a1nmgjk62tC2qD0E4-iGIxBBLP1O5mNIIfWAY8tKHNSi8q5iQ50PLrKj7bj1rWJuvPQxRxS25bkd_nvYEzVGSQPpnCne2-ZIaEGR07u2fwKIi6ZkQW_ZZFg8-W3_5HFSqX3M8wzoRjRPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه «عراق اکسترا» مدعی شده انتقال مرتضی پورعلی‌ گنجی، مدافع‌ ایرانی‌به‌باشگاه الطلبه عراق در آستانه منتفی‌شدن‌قرارگرفته است. این رسانه نوشت: دلیل اصلی این اتفاق مخالفت شدید خانواده مرتضی پورعلی‌ گنجی با اقامت و زندگی در عراق است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/27361" target="_blank">📅 23:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27359">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXlsNzSxTjhaR1D7EePzwnK1LuH4IhDQk87m4HFNwpZX7aUHFxpJQMhlSpZbe5cvo3BMSFXR8rKWMCUK-3NAnaWRPJJzfJ7V56QD1r1l3OhwscXG4l-1YBdPUql_KUCbphLFG21HhcGHGlMRHUWxLk99TiqoMYVBOcp9M5qqxdm8OAj3pwBPfIKW2U5OMI83__xpGPo9yG1mbaFTfpcoGNKm3yifkNqa7AFp6wCUg_fpUwdYbYuZFyXdQeeS4iSPiZbeM9PXfzxWD0oIMSqRIzJVGM70taZzFBc4QGutk9OgjGB4eS9dMkWpyzIgLT05YNyg7fH-WExxFWoFeX-MOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مهدی تارتار امشب‌باردیگر به پیمان حدادی اعلام کرده اولویت اصلی او برای پست دفاع میانی دانیال ایریه. باشگاه‌نساجی هم اعلام‌کردیم که منتظر است‌که‌باشگاه پرسپولیس 120 میلیارد تومان بابت رضایت‌نامه‌دانیال‌ایری پرداخت‌کند تا این انتقال نهایی شود. فردا…</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/27359" target="_blank">📅 23:13 · 17 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
