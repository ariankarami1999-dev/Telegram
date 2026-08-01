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
<img src="https://cdn5.telesco.pe/file/FcIsEUqwHUiJMiI4h-c4KPWeEfQJidd04r6LyLlTyPFUmqCVNeNjl2O2piStDSqQ7s7Clk8rn6EE509w8Kh-LXW8ZZ9N7ezY4wzSN4B6X-kSBf3zKWZl0UsIH63SjdFuhq77asCF-0qhMSlwFrM44cL3QATVLz7hUFdrnvMrxUhjePK2khVGYq7x4jPPAfwGmedZ84uM4YquNKN0jbNuyUVmZg3CkvhjVdtfQRlLuKfa-mp6mL63x9PpEyMss0Eniy2EUhBSnv1SaLNrAR_KKziS_16b5QOXnXhhHaL8JZxSrI2gilfogjPKoEDcaWEz0jQrdkgei4HBlRV2TVk3Ug.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 505K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 17:57:25</div>
<hr>

<div class="tg-post" id="msg-102520">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHbGciny2o4HtLespz4FhB8Y5pJIrPAV9O2yhc5IF2YCe9oEobjcNcyiycmtPjAnjC9PQrRoTz8F88rT8EYdYCRpW_nu_0Fk2g9CwFLTOTcWrcz3Z6zYCyi9WqzeQRV0LGEedEZf1R7ikJ45bm9P1PR4_tFEWWlGGltMTGM24lN9vRvf3qjtUXxAKmeGdW_4HDYpCGaU83Vv2eGo5ssP-fZA0FkcdS2nSIB9t5YDzP-7dQP39ga2CzWJtRy3XvRSiyhVbwzFcm5MKMrTQwHt1O3WPIeIw_mYIGpn5dqDxHy3rdoPkAbO600l9fpTywF-I_rBFT081gOrY-Zyin3FfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوکاسل رسما لخت شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/Futball180TV/102520" target="_blank">📅 17:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102519">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDLtTZskk0arUtgRSQDD3Ged5rlHNDTgTowXMFpA_sdJuyhuEY0GYYXScMfnZitTqytHGpp5KHMjdtdKEOZJQFNAVaif4EzJjESvqy4yHGP72tLNQtrQmkXIuo62rF058KoATdrOyxsM429SkQfSwDfGDGyIvp_RzfLgspb3Y9phW9mTBuisehbLhUDMVGMhFC9xEO9JSHmsSxv94kyc3IB7V-hBLEA5P4S9Xc8_DrUnHHkzNAgftil8ta3UiTz4_LGAuizfAnx8BRMII6F3sp0Z9GMODKFrGDGi-yprhalo2c_h-S9h-5yxpeytpZsDi76yQQEvXDaymM-vFMajaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
چلسی پیشنهاد سه باشگاه اروپایی برای جذب ژائو پدرو را رد کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/Futball180TV/102519" target="_blank">📅 17:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102518">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSTe5GUpPpf36_5jQhP8745vJLVaF57zuojfzGkbXRmgI5YzLacmSCxsiR16b2PW3lLkVLvm6RgxL5s36Tqzk1lqEnRvlUo1eUwidvhMmSnEpanPd4diDL0Rx3Og6OdaJqabekdc2_rU7cb52qIUaT1ZeYHOXuC8aD0oB5NGoMvxusU8ofM-iIstOq6Hibxbi7WblZv810pSaCYGIMiVzmDf3-kIIoK1C0j4d0K2B37EM2BTZ233VmewSsXLIZQYswrENwwbDAdPh6ILJ5wiA3YRz5uUFatoI-qlEa4m6QIO08HPyN5dAJaIYjwh9ox1Yxg5XHR0OmTn-NxxIbx8XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس طاقچه بالا میزاره و ممکنه بره آرسنال؟!
من یک ایده دارم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/Futball180TV/102518" target="_blank">📅 17:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102517">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fb462e454.mp4?token=Jx5uPb2Nyl_48mk66BoRJeD7YsjMeNd3W9kDJp4_4glTi7Xzh9yPVrkr6MwF2oqgs_EBThO4KlrRQULCu-Y1oXPScnqpoJlNQll4dA7jSbt3L3Tunalef1Oo4cbmy3YL7GWCCTJC9H0dPznSMV7s-ukKlD3LfTEs6HF9Ay2tIH_7BmAqW7GB3GlenEmH9AgNrqcI0NTo_RRE4MB5LhwAylLslLu73UihjIQLZKM-XKPDRkR2bEXlXgdPEbp4sx0bVm3IB8sWXcg6_58YTU5TcXJio_qVQ-TTx5-pPCxHlnJXr-c1edIETTxivVprrIBsEkUPJavqVjJNeezOKO7VgyjT91wW6SSiC9v2PfrKyo7t2ywUe29hWjEfUCchfHhRkSna2gQhdLKZacEZOPu-qICnV_8ziebjPW89r6zzKJMXDm3BLqXW7f5sJ-O9Dp37dKrnJZNxUoSTzo2H1ZZsf_wryuitA8kQcP1e2Dt90C5eP1NAdXecDipDzZ2Nab-b4_lPU4Ic9gTVSwrA_mt0WnEnjCrUhwVklFUGMaVIIVZLfvSLazbtiO8fpRIQc_MXT91ZMs3KJZp_3BVWVyYlXjUBy0W8gliKhaBCGcTXSxCHyHPNSA6T1SUlpAlSwPHmKwz02eXL1bF5V38CfaRf8Q1jaDlsIB6B6McIcM7JmDk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fb462e454.mp4?token=Jx5uPb2Nyl_48mk66BoRJeD7YsjMeNd3W9kDJp4_4glTi7Xzh9yPVrkr6MwF2oqgs_EBThO4KlrRQULCu-Y1oXPScnqpoJlNQll4dA7jSbt3L3Tunalef1Oo4cbmy3YL7GWCCTJC9H0dPznSMV7s-ukKlD3LfTEs6HF9Ay2tIH_7BmAqW7GB3GlenEmH9AgNrqcI0NTo_RRE4MB5LhwAylLslLu73UihjIQLZKM-XKPDRkR2bEXlXgdPEbp4sx0bVm3IB8sWXcg6_58YTU5TcXJio_qVQ-TTx5-pPCxHlnJXr-c1edIETTxivVprrIBsEkUPJavqVjJNeezOKO7VgyjT91wW6SSiC9v2PfrKyo7t2ywUe29hWjEfUCchfHhRkSna2gQhdLKZacEZOPu-qICnV_8ziebjPW89r6zzKJMXDm3BLqXW7f5sJ-O9Dp37dKrnJZNxUoSTzo2H1ZZsf_wryuitA8kQcP1e2Dt90C5eP1NAdXecDipDzZ2Nab-b4_lPU4Ic9gTVSwrA_mt0WnEnjCrUhwVklFUGMaVIIVZLfvSLazbtiO8fpRIQc_MXT91ZMs3KJZp_3BVWVyYlXjUBy0W8gliKhaBCGcTXSxCHyHPNSA6T1SUlpAlSwPHmKwz02eXL1bF5V38CfaRf8Q1jaDlsIB6B6McIcM7JmDk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه چرخ تو اکسپلور میزنی میبینی پر شده از کلیپای عروسی ورژن ایرانی رونالدو و جورجینا
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/Futball180TV/102517" target="_blank">📅 17:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102513">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S9mPog6CqJWD24_nDW0t33EgqaNDkRe-MvIEKqSIqiOc0IFz8L1Z9zG1tLSwds4igbXmL33RpwsBm-d6iaR3J5id3QbsBmBeHartAqaZX5s_MlX0brRsCPadrmmPTW0CK5R7s4wfKDZqcFv3rV3jiifiTTE0Pjtau7SlgyX28w83iTRVW8OP5I54aHHPmHC7ghlHBCA9TBuHQDL5ezlUnfxCm411HBTvpKYl_QTPtbVtXwzH8Xgeq-bJV_ZoOkrARc9LhB4fyomXuvso7JxN2jUi5dFS7JTvgxWlMTk397Vc_GhyKba0TAWWqTian2by4uXew5LQpS3OfloyUFaI9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/et96n4ctRLLvGR_7CTPF97BW5lp2ZDUzRG-KaQANdhDWICDuvSrQJdW5bIE--bBD4wsU4iPKlkhtnT_155WvQXd-RQESbam2hvs2tAAfA00H4Cv1NDbAoT6U9HnMbyAK0aQkx7PYszDQSBu_K_ayFG1WVqhL5q-Wt9AV3gueQyHcGltHjeFAJTCvCLG_BPpjO-NBNktrlHQmDgUw6rpec3BlyHxvNQwEG3vqj7Mc06bNsQPREQLCUUOo88q64VylLKNooMBSULqxdkrF6UEEIVzsw0hb3tZn7aCqH117gAjx0abtWb24MibNYGjk_RKgW96DX5eRKFgY7ZDsK4XmOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z2zxW45bJ-6YE8gVkIj46lJZSheQOEY0WA3VtNyw2fDfTtrnI0QIEHZwTcDcndeLIVBLzcg8jL3ZdyDvgMjjZmEBXSyGgmku0_X2boZlqdIn0BPjdZI0i__Su42zsbb6IM-bjD0s_nWpxJHRCZ2ezEYfUJIjgVBPLn9ZsSz7lntTZNv-HtUljoT3YXouU5yEBzAzuYpPVDuV3dlVK46avhvMHOY_GwSBOgkcwtI476nqwbINrTB1CrOxvyqnV_syBjbTg9UhH0f09G56D3lA5BLxoi0wJKLnBsYwTbimDzt_gN8R-PkWEiYYyo_VJOLsYnWqWbZK-OiUXX-Jfw44Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l61Lkd8Uz-GcPmg-QHGLj23gRPH0XPKsYSTpMCe5_JK3nnMDswdc-3eRYccL_ibp2IQwkKIp0h5XbW1a1MN2jUH5vDm8OhHPPgJzYcVVLGka2MmDEYXeXLuq1RsDlOfPLxK8wPrfz6ob5BEq9g4DFyy1LFvQENqktkzyih8a78G5hEUI-4GTQ5wE7wyhJQUOdAwRpzMbULwO-ciW18rNy-UMGmCaQm_sfOjdAgVlRWN4uVOWfo8m3gd0AwHigP7QM1xC4J5i4ialRb71d9GXxWB6Kd2oGOLSYSbwyHxwukEDg_vca4odq5a1M_YjvcH4eEa9GMDa0Ornn6s5gotQDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پستای جدید جورجی جون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/Futball180TV/102513" target="_blank">📅 17:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102512">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LF0ozzzbzSoPRX8D-DFhceHe4U158gTJNqe1q0gEP8nimrbzEua6XoFu7kC1uBf-_5cjsyYwXrHJH5b9y7pZR2ZgaEdBRzwTNZaa8zWEDz1hOOxT0LVjfPQZgH4Xyc1mucCkI0TIuL3eugFV9lBOWvT43nuQKmBBsdXhhCUCexmEqhSxCVCd1VpOfcbCza6OlEMBNBRUN6_uAclh1IpHV7NBwa9IcshcNsliLBWTmWZdZWQHLpmoF-dsc-H6wpEiTq7OssVi9rCitF3AJvs6XTr9wtsZKrT0QdZ3HhJqcyi1PBjtMYuV8DDEZPQlGmtxgk_nDyHice2sEaH17BAijg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🔵
اینتر با نتیجه [3-1] در ضربات پنالتی مقابل منچسترسیتی پیروز شد. بازیکنای منچسترسیتی سه پنالتی رو خراب کردن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/Futball180TV/102512" target="_blank">📅 17:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102511">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f1ded84b.mp4?token=tkXtAGYnGK1D6sznvxmvNxz5sKAi_FPwkAeJgxtlfoQz4lcBIvUfmYJA2bj3xTQ8DROXI2hptQGan3jLKrkC0SfFyGbI00_OQoAVK_Kmge42-HUo1Fh9tIRHaAXc8uehQuHMMIWke80ADxDd8UREuVpnYl_qc2Kt2XUrpwKfyTd4x6LuXZQlV9O5Ce4S6TjTahgzinZiC6eASvmQqiGoJSH4dmJl9iqHJvNPFu8ZdauWopWkCmIs5waW12aAD6aLXIR2wgwOgnzcaqvtEje5-QgoVw8zdd9tarjplXfStyu2lREVPZD4_qE9_5nhlLggyPLx5D9AV4dlIRD9FdeQcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f1ded84b.mp4?token=tkXtAGYnGK1D6sznvxmvNxz5sKAi_FPwkAeJgxtlfoQz4lcBIvUfmYJA2bj3xTQ8DROXI2hptQGan3jLKrkC0SfFyGbI00_OQoAVK_Kmge42-HUo1Fh9tIRHaAXc8uehQuHMMIWke80ADxDd8UREuVpnYl_qc2Kt2XUrpwKfyTd4x6LuXZQlV9O5Ce4S6TjTahgzinZiC6eASvmQqiGoJSH4dmJl9iqHJvNPFu8ZdauWopWkCmIs5waW12aAD6aLXIR2wgwOgnzcaqvtEje5-QgoVw8zdd9tarjplXfStyu2lREVPZD4_qE9_5nhlLggyPLx5D9AV4dlIRD9FdeQcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
اگر پاس گل پوشکاش داشت، اوزیل بیشترین رو توی افتخارات‌ش میداشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/Futball180TV/102511" target="_blank">📅 17:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102510">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSPHTMdjVp57Nk9Y4d2imWkEOoybuewemssagTvBmMVFoJYO0gYkquJHDmivKivJ5V15vcmy3V7ypXX8AcrFaP8wUmcyLyP_XdK2iosDUANZASpqroi7WLNpSoOYuzTkfZRx5SLo3Sj129keRdIGTlUEIJn4CqlHZb2h2O20t_cfd0yLtNLzZb_dV8NN0PtV9wYhrOoaJ6gdiPJPHZe_mekyWUaflpZlTNFa7xvSwQGzaoMu0U_SMhW86TnZFny7SgSQ5ng7-xPYnIVzgcuk2g6mPzXPbhoXUp0xXLHlBEyEI2Cq9uaCHxUTGpuwqHPNxskfbuN3UzaMGM-l3OO_pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اورنشتین | اگر وینیسیوس با رئال مادرید به توافق نرسه حاضره همین فصل به آرسنال بره.
ماریو کورتگانا: آرسنال ماه‌هاست که برای جذب وینیسیوس به طور مخفیانه حرکت می‌کند. آندریا برتا، مدیر ورزشی، با اطرافیان وینیسیوس گفتگوهایی داشته است. چهره‌های کلیدی آرسنال نیز به نمایندگان او اعلام کرده‌اند که او مهره کلیدی یک پروژه مستحکم خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/102510" target="_blank">📅 16:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102509">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzcNNldFcRO37RtUz2tcIwp3nSSb9hLmeez-FoGIMHSEkWnDSm00A6LTb9kWagrmPvN8VHRUataONxhwZF2RXETRRQgyzBtNJ7Fs6Lz0ON9EIbReQfID1w3c84_Ix3vcxiecx0DW7N1s0OXE_auB1icgfP314sxuRgwpLikKNbmPd0gfyb4g4jUlFjDiS17fkUJtchKZSNKZoZawFX3dqZAycmIVqXmR-6Ucx5US4WaRoqSCCeM6RUokzWiBkOaXP2FJOLgBZzQ3mmv2f6r2Y4HmTLg_HoZfbOqG-ErmJG7BwWF-UAKXrORN96qi2jRTreEc0PGsBKutmNpFJZa-XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رودرا - ESPN:
طبق اطلاعاتی که به من رسیده، انتقال یان دیومانده به رئال مادرید با مبلغ ۱۲۲ میلیون یورو + ۱۰ میلیون یورو بند پاداش نهایی خواهد شد. همچنین انتقال رودری حدود ۶۵ میلیون یورو هزینه خواهد داشت و باشگاه در حال حاضر منتظر نهایی شدن انتقال بوعدی است.
⚽️
@Futball180TV
‌</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/102509" target="_blank">📅 16:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102508">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDK3XyaCOYOh_Nki8LUYkP-O_Tsa1meXZRuVmd-3dGDNztCiJrpJ1zDBGnauhPFySh1eey4UZKOEcyZqRLZXTL2nQ0fXQGDPxlG-86z3VXjzByz9zT6_TSNwlhQ0QBU-IzRACZ6eYA8xRNeDVVZ-Xclse_8mp-_gDO70FE6bu6pcDqimSMcFqlmuJvdrOHbPUrtRrIdWHT0HPv4sa6E35nAgGS7F8yJ7aTAfA7o1VaP3q_WlgjCmaKfgyBWGlYZHmPO2qLGSEXYxOCf5O1aBCzoVlOOpfLC-52cbrFqwMuXPwgDnbVdoN0wg67emi950zvK7q9tQhQhnWj9O02GpxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین شات از عشقتون وینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/102508" target="_blank">📅 16:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102507">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qC3NNI4nfvTJ3ScMGpePfWP_Slvtaj-3lwdfl-llb7agLlRBLfvh9q1xxhrTwcnpHT8ERkwqhEptynD598-_KzveJUjw0dRwLWPB36ROzQHr1KwSJZXZLtI-hbAi5cBLOdHbf2DLhFI23bhzDOu0U7iyybMiHgjRbtwtnlzt1BKy5LtNDGOzFBTcLvwkwemssK54ydRsz3ijCgjsm4Ca-OAklRSo9zfMGtO7VshmSeVUyhhdoTMZ66Mjm13S4VW5iOeRe-FF0ENWLhs6S8AMyxiJ08aijYarJz2_7Z1AX6xqf0AdUcHhfomRnZxNcpgs2z5TX2FGlkGg3ceQAHvNpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚪️
چلسی در یک دیدار تماشایی موفق شد به تاتنهام 10 نفره 2-1 ببازه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/102507" target="_blank">📅 15:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102506">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNV_2C3tgF_LuoRxOgQn10iOFHqp12-lpyu5sCj6zzoc1zg9m_Bu0ojkH8fnX0ADUaENZe0l1ODy8yT1vngAbApcXdR45I99FPmgCaMGyvPPt2WTJy3WykcJHps1OKGR2IpBfCHmW4VgBAJnwI5QL88svnJsZ6xBVXcw-wPPRDhPD-JusxJEX8vW1qsTHgJhz-rYbDl6Qwy_T4KOmCz4SOA0fsE32iNJ1BynKzeFwBOjYpfktn4x5lL1N_Dl2_ysb3pPAzRwllEkalouXAbpwKfUC9rZROq_8Ux1pg1-aO1ZIb9knThVZ5A_kAxcOCh-bM3tc6BbsCnpCoGj9EprsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
تام هالند:
بدترین تصمیم عمرم که خیلی ازش پشیمون هستم اینه که طرفدار تاتنهام شدم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/102506" target="_blank">📅 15:07 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102504">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a1fTku8wXouns6Mo_HDXaJEzmQaxqI_1vWgkHxiITZRzBISgpPmErvuYolpHQlAJCaZvY18XE8btor6ZtH2ZjoB1NQOJAYy01m73cxXnO6qZmiiQGtWQi-CKtByFUKS60mARMXdJVog6Xjh5haUcBa8_oOL2Uu26rklt2AnL3rUYrhTQT1o6OtNHLHZMyyu3ZGvxt1Jj7zM1g1bIzq9rdZfqFEk0XRORq3fqLAvrYqSISJE3fIy-l73rZjUXnhpQQv5_tFU_WBHbwewvwloTsGh2oSYaNlxliFW2G-cCfESsSbUZEfYQP_cZ20918UAPey1VGDv97kzU9QdDPFloag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qj8j7tBO5Sq_0tcFdMILZ18nyQuT_3BGfrLdq55-EEZxmlTJyVwHBs11hGx6SzJTYUb5Bp6Oh_gtirIdFV-uLbEuLST6ZSNM8Ig0EYGere8PkRNLmo3_39rGiDY5FAG04xMoONnhCMbXsqNlUD3camme2jMM4MevtDj5EAK2oWGtchTzpMyZcnO4lhDPbeoHXHEbCaJQugRL_yx4hNro7UZZ3cJXlqZY_4Dz4OJzZC5anQKIRP2_tc1GUnE7XzAc974pqeo5hYnaZGcdA4KAJNbj5zkadBnYb0b9JE3ZSyG0MwnWCCvEivwSXsYxTeveugvCPjpxkZ0m1PRabYdZiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
یه پستچی رفته بسته‌ کوکوریارو تحویل بده که کوکوریا نه تنها باهاش عکس گرفته بلکه بدین شکل یه عکس هم با مدال جام جهانی ازش گرفته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/102504" target="_blank">📅 14:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102502">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rySRZayF4adT-0-oh0JNzBjdI-FfAX0BlTBHthvJp9cQ-gFIqmwEKXX9hgkBKRMmZB4HIPTKGFBx_Li_95ZGmEaFg1u-EfuhpLnjDWq3LubQDz-KSyfKFnwa4Z_EiVs1FhbwT7m9IE6nKit8MkEIwpSM9QYzY5O-s2DJXD-x6vW2yTbfNmd2y5aGQ8JnmiLBO7_hCKZCorkIhXBnHddkhteMmB2lxvg5o0V8MJFE_OripxdOY6eNmAVqPxibxuanS1oTt-taDukTl7LvyQ1lRUdie_Y-EI6R7V12LGLJNtU4RArqb2YUFAlbJI3d2B8Q5_BoPDanFrzdSESHK6ol_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Du80yLNkx_Q7p_wgn-PwHpOhnBWTopFUGhaKxi59HValggMwMhz1eIu5cEcm5Jjr9ziGAjx_hUemx1_mpphuRMxtpbZ02bMdJKaQIcUC7Rr_xnNvDqu43f3UJC7lxfuNzIrBQaN6yaqPTTDW_AJ0rRiNfjvfFFvmaUHstColpHQFz6FXjmK1vAz9_St8DsC7eXEE8nRbtuJGyTU1H7lXXL20z_sruyifNWcQ5rBUH2x6fsPqlihW_dwUWXuKSf9VxTdzrhzuYWRIs_hY2ZYtfOAFfkBC7SzUJahtX0gAOrRsE99og_DuSI46v9f7N-jHBXHU-Vf0I1f_EwSIDnuINA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
⚪️
نقل و انتقالات بارسا و رئال تا به اینجا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/102502" target="_blank">📅 13:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102501">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5_UNSbE9Qu_pK2H1HNcqfmW2R2dCCRogR-IZFVCOAfymIzGPfs1GPv_HXK1eP7nzMZvtinc82IvbFDKYWAQETBrgu-RYhIqjLirTEpNcC_71Vkb1hA-Ers9yE9BeH9fwZCG2TI8IWLIaYsxT0axQrkUp9BCDfPITOQGIEvn-B65wAA4MOXJhR8DochNeg0AcYZzxcavyAa_FwmrLR1lLeVWXGZ7L7M63zqjQuje5biHYelo_5fR13lg1fiCgFjQcYjgR7yYkZiF7XQtqA1JDRPk3XPZ13ne5UohziO1lG9cUr__qeb7jXn37BpNuyUL_ifgjGmZvxkjGNhZXLqLiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رامون آلوارز:
اطرافیان وینی هرگونه توافق بین این بازیکن و آرسنال رو تکذیب کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102501" target="_blank">📅 13:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102500">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sf8w7pDq2_8_iBSSw5wv16uoA9yT5S6kXwFj3SzB9CIKis46zEBUWTe0Rjd2EM2lGWbuNV1RKl50NYMWH11UtJtshaLIZ719Wvtm6Rfi6C_y0Tf0eSu6qntsHQtS-2gpHVTLRFEremGlfyxKKTk7SUaHgNdQSaMH5AtOXR5GurqiezDJPR3RewaCCIZ_5YIxYlZTY4nvs90m_6-UIIRAXHpPeS1VbnhiDk7VzS5gcwFdoV3sRAol70mTciHq9nhsadnENZeFxGptaY6lZW9k8RqxTIP7c874gwhif5ZxbxRgQvahv_d_fq6BT8U0h8-cG08pChTizNuQUzwg7avobg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
• کریستیانو رونالدو به یک ویدیوی کوتاه در اینستاگرام که او را به عنوان مشهورترین ورزشکار تاریخ معرفی می‌کند، پاسخ داد:
"خیلی ساده."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102500" target="_blank">📅 12:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102499">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29d00a9ff8.mp4?token=EPU1o5fERphSWmF_tivMYhXKcppVtdQ1eLpFmfdbXJX2wExCLcwnQMchsOy4SvvvTSMwA-780dtZIlYPumG0ns-GlVZaESXYdYaZ5DE0q6YMzUUhNYadKxZwH3cm4u5J5KQ2HiDF450FXU_cpVe_kmBGjZRFSNCef5fc47Z4hTTZyNeU_ASHfsg5TTT2YP7NDjDVdXSzXa7uk0vbX1iMiSUBb2OtWkyCaX2mjDJslw8D8Iiq1mYFo_nLYDTO3kq5g1dmx6uQYOkfL_n2Uu_uFGTbhDrFzqgK1No9p6n6p6Dc9kO-IzcoRgpwBbpy86dEhdhW2OOt75SgMa_F2jpYq4JPRCJo5URfRwdCNT0QisLzn_EVknaQz3gU_uMsOsdtfUPSmn1Ocivzl7NacTSJORdyE3w8gqX-Xb3C5C4o7GO3GAFOEm1R5ATCWF2V6rMsld4MQzamYTGDbqxdvg1n8B47mvB3khayPe4rPRfmY4w7-cZyOpFLoZXwYAZY52_5WSiMc8YCCQWtQ8r9_sTkvIk50AIjngdKLdZv1mQat8rwZ8c9VEqt_uUh5jDK28HBwOxjZr29GTZI-_jhLLt-YCYocHtX7peTYREUJfHDewWhSRLO-A5oXFHv1OyBK7Fv0i17hRi9WPZ4vneJ5zquSX0VfMRDVrfZ24jLT1bW1G0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29d00a9ff8.mp4?token=EPU1o5fERphSWmF_tivMYhXKcppVtdQ1eLpFmfdbXJX2wExCLcwnQMchsOy4SvvvTSMwA-780dtZIlYPumG0ns-GlVZaESXYdYaZ5DE0q6YMzUUhNYadKxZwH3cm4u5J5KQ2HiDF450FXU_cpVe_kmBGjZRFSNCef5fc47Z4hTTZyNeU_ASHfsg5TTT2YP7NDjDVdXSzXa7uk0vbX1iMiSUBb2OtWkyCaX2mjDJslw8D8Iiq1mYFo_nLYDTO3kq5g1dmx6uQYOkfL_n2Uu_uFGTbhDrFzqgK1No9p6n6p6Dc9kO-IzcoRgpwBbpy86dEhdhW2OOt75SgMa_F2jpYq4JPRCJo5URfRwdCNT0QisLzn_EVknaQz3gU_uMsOsdtfUPSmn1Ocivzl7NacTSJORdyE3w8gqX-Xb3C5C4o7GO3GAFOEm1R5ATCWF2V6rMsld4MQzamYTGDbqxdvg1n8B47mvB3khayPe4rPRfmY4w7-cZyOpFLoZXwYAZY52_5WSiMc8YCCQWtQ8r9_sTkvIk50AIjngdKLdZv1mQat8rwZ8c9VEqt_uUh5jDK28HBwOxjZr29GTZI-_jhLLt-YCYocHtX7peTYREUJfHDewWhSRLO-A5oXFHv1OyBK7Fv0i17hRi9WPZ4vneJ5zquSX0VfMRDVrfZ24jLT1bW1G0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
ویدیو جالب و وایرال شده از رقص امین‌حیایی بازیگر محبوب سینمای مملکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102499" target="_blank">📅 11:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102498">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86343d5e54.mp4?token=iSdCK5DgGRK-jRv9EuYDoso7pbqnH8lEZF3zUS-aW-eORfw4AEZQfRhp3D121lXAYv7Lq8nHooNCzKXpfVidsoPpxeCsWJ4x32YJ_dgdXPRSzlSJK5cCuQ4MH2gZIxdBbhEHdYMDf26JKKRzxIPsAre9cs8MzFxXLWx-fPqEYL0BkYJ3S71IYSK8Jbi16XtcXuSaXPLlsR_Ro7Y8coM7wdZRfTpbv0QKszEMluNfBg_2hkZmoPeO88wAK6aO8gtqqJay5EQzzJ4KpbD3ticLMaca-rswEylW1gVVmaHFAvtl3doB40FY2m7ln7464F1TEIm0WBkM9T15A-X9vZYADjYSVS_HD0d4nKGQWItwOWCoYrjCf6lsJVxbpoHfJ58v3TLIOZvlkvM6rLi2AXnWSPKd1JNPXAjFpR-SCYVIsGi5A0Focj_l7SqYuLM2Z6jeeHoZDhK9DygrFxw6sZBV8cDKk2OQa5QCh9a4FDcwL1r9E_0a74oD-1ssieWuhPs837jD-MZJHkBNEtZ_uyV7G9Sf-C-vaKbYOt0MWabXui9uX_gjqPDlUgH3S1M2ZcbY8ER_1vMUJM9qFvMmKEzFFnUQMHBcS0Ry3_9caK5qh40sLyS3_pnJoQv-xgf3inQnRAZ7XHovu2iTO7zLTcgoP4ESBAKFwozNxg-IRKvkUS4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86343d5e54.mp4?token=iSdCK5DgGRK-jRv9EuYDoso7pbqnH8lEZF3zUS-aW-eORfw4AEZQfRhp3D121lXAYv7Lq8nHooNCzKXpfVidsoPpxeCsWJ4x32YJ_dgdXPRSzlSJK5cCuQ4MH2gZIxdBbhEHdYMDf26JKKRzxIPsAre9cs8MzFxXLWx-fPqEYL0BkYJ3S71IYSK8Jbi16XtcXuSaXPLlsR_Ro7Y8coM7wdZRfTpbv0QKszEMluNfBg_2hkZmoPeO88wAK6aO8gtqqJay5EQzzJ4KpbD3ticLMaca-rswEylW1gVVmaHFAvtl3doB40FY2m7ln7464F1TEIm0WBkM9T15A-X9vZYADjYSVS_HD0d4nKGQWItwOWCoYrjCf6lsJVxbpoHfJ58v3TLIOZvlkvM6rLi2AXnWSPKd1JNPXAjFpR-SCYVIsGi5A0Focj_l7SqYuLM2Z6jeeHoZDhK9DygrFxw6sZBV8cDKk2OQa5QCh9a4FDcwL1r9E_0a74oD-1ssieWuhPs837jD-MZJHkBNEtZ_uyV7G9Sf-C-vaKbYOt0MWabXui9uX_gjqPDlUgH3S1M2ZcbY8ER_1vMUJM9qFvMmKEzFFnUQMHBcS0Ry3_9caK5qh40sLyS3_pnJoQv-xgf3inQnRAZ7XHovu2iTO7zLTcgoP4ESBAKFwozNxg-IRKvkUS4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
پنج گل برتر فصل‌گذشته لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102498" target="_blank">📅 11:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102497">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwRvnMfsoc2UOnS7sJYlnX2akiSBMBc0dyqn0aG4vBr4tAfdpH5zs_nYESkqgn23gWdC9cqQrA3q76StUgtE7RU-kdrEYzIP7ebH-UyKCnae8IYOrxnU9oZyb-UglwpFLq7KcuccWIn4PpVBQgc1Y4Za-X4L6s47B0xN84AWaqzCyJDTtsPrmWheJ09Mcxuc9fMh31KqKfayqpPWcvvK9rQZRHMJzjZW74zO8YW7U6ewewxNtx4UqYrUj5NU5GJOVRRoxRYHFR4GqLgidM7lJyiggDTsvTSIDgnMsfvnkyuNZx_2g-oGcPIm4kp1Tj9vzF7ONQTPm0C4wFGjcYjvRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
اینفانتینو با انتشار بیانیه‌ای اعلام کرد که طرح فروش بخشی از سود جام جهانی به شرکت‌های سرمایه‌گذاری خصوصی، به طور کامل لغو شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/102497" target="_blank">📅 11:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102496">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e324940235.mp4?token=Bl5voWHdlRCMsZ-ZFpE1PTscJ5x4F9yWPvOCfx1on-oS829a8DktxJlcrOpFwlhvNrstCmVqipJ1HUlxMG35vrI0ulaIl00_GF1kS2lTlLuyF6AVyB-0o1J5rW-V-12L0-GwM-jUecW49JbAIwQVWOYrg9NdzraEtbue6c8C_ptAn5l0KOl3X4gNitRYw5DiVaJrWvIZCgdCH7AhqELVSSXsyLzPl9YpfvCU6XE3Nh1obV8NVd7fWu7s7xUAR5zDwXbAr-K-Naedt_-y3irYBeGRTNWMzRjJ2csrQ5nSFGOcjNb5WELPXNrkPuwWaAi33dy2gyNh9mu0P3JLyw39nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e324940235.mp4?token=Bl5voWHdlRCMsZ-ZFpE1PTscJ5x4F9yWPvOCfx1on-oS829a8DktxJlcrOpFwlhvNrstCmVqipJ1HUlxMG35vrI0ulaIl00_GF1kS2lTlLuyF6AVyB-0o1J5rW-V-12L0-GwM-jUecW49JbAIwQVWOYrg9NdzraEtbue6c8C_ptAn5l0KOl3X4gNitRYw5DiVaJrWvIZCgdCH7AhqELVSSXsyLzPl9YpfvCU6XE3Nh1obV8NVd7fWu7s7xUAR5zDwXbAr-K-Naedt_-y3irYBeGRTNWMzRjJ2csrQ5nSFGOcjNb5WELPXNrkPuwWaAi33dy2gyNh9mu0P3JLyw39nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
و بالاخره تحقق رویای دوران فوتبالی کاسمیرو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/102496" target="_blank">📅 11:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102495">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👀
🔥
هشت سوپرپاس‌گل ثبت‌شده فصول اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/102495" target="_blank">📅 10:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102494">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LuDUKzJs5mE5KePnwIeMi_1iQ9AbhKM0KCULlVIXto517-6VTVbIIQ7QUsAJe9EMj5aQXrvlYEePC0PCAU1_GhBElQfz9LrfibsU1vw6y8s19JnUW_5BjUJg2Fy366aKzrkTfVRJ5Fn5rW0RkBpLt8IKGJRurQEF_bhjpxmHbxksR23HjTxhQvb9lQ6o9PBYyuPc2lWnbmbhHONDBxCAl6C3bCwHHAxtNTmPr3aSLQG1GstnubTJwqVy-FloBtnD5En1_N59tbJwAiU-hPBubG5H5cW0rL2kT56CKIB6BxF0Ss-p19ygQSPCyUm8HH98GIYLZRlPxdqf5Jg_KzsQTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه آمار مسی و هالند زیر نظر پپ‌گواردیولا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/102494" target="_blank">📅 10:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102493">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvfujV1Z40npbDQYKOnmQyKyWhpoGRO_5YZ6ts1LZuQCHpVjwCfDi2YFbhq-HSrVhFhiet9LKjwQo6Qijo19cCBF42ohyO-IRJ54e1qbSeoWyfQf_EKTHU7Logz87Nx7HaM1KA9_s6GWfpmvzYHy_Ga4IsYa1aCY5KoSSjciSvpHLaDnO_s2eUK7KBd_bkc0PwQDSn6r7LieHLPO7zmqs5La6bXPpah40y0-8_yXAkpbwWoOhKKLECW8IXxpBtoyRn4eXtyybgAEpqK_xvzmbdwaaHGb6CGAvbCmFu98pWeaipP1De8y2c1Dk74d_mBR4kv1PJKf38pcfIO0S6tAhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تمام قهرمانان ادوار مختلف پریمیرلیگ ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/102493" target="_blank">📅 10:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102492">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AaQLh5h7nU1YDMZpCjMBwCrkhjDrRZItCfP-QHQ6YLfZi9ylXF7Xcs_YcwMnq8NqZ56cnYjvYIqG9fk7LsJkLrzmRUMwE1y3OhY_LWnIsjX4-hhSvpkPwXxzwjFPfIPavFjyNnAZmznq9ApFnINOTfcKCL4OELDe2hzJTb13ZAHQ6U5eddJsX8iIkdabzLkWDLTPiHpU7YuM4bBSGvtdR7dxaAUAOAfOBIagsR-FxnEcuNa0lVFFf-iz9RVbiOkHRXQh89jselOC9sPwrtPVx9Izbz7Lh5IF_IyZqf_lxXjmc8OWIaoTVTvZPsgZrBNyRV6YkVXslu7rMMe2ULDE8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
باورنکردنی است که برخی از زنان چه توانایی‌هایی دارند!
💪
ژوستین وانهائورمات، هافبک بلژیکی تیم زنان کریستال پالاس، در سه‌ماهه سوم بارداری خود همچنان در حال تمرین کردن است
❤️
او ۷ ماهه باردار است و همچنان با تمام توان به تلاش و فعالیت ادامه می‌دهد
👏
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/102492" target="_blank">📅 09:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102491">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5RQ4eI3U8Fm-COxxW8lK1aodHNFLoJsLSt-zgbKJ9NA5SVkfnQJKSv0MthjWxovUGeEbjZZqEULNyV6719LQzuVPli2ZhCXyJzChLHuUVeSjhKF0jnippBB0D48ALHSyhJ8QbTl2CiGIHRK5Nib5vG7ZRRQkzKQHyQW96CtHBlBeNZMCcyIk0q_n3pXEbCxBH7r74iZo9b92z0RT_0eDMyTn5zSEw_KCRr9VcC22t2uTNbMC2eKfLMgHKszWErD9xKlKzti6_MF9ZxpL6sUcX_ObiFtI5-5ic-ijmtKfmQdYqXb1kHYOXcpoG0IfadL2vmVbd4KjeYskQUgdbnOXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
🇫🇷
فوریییییی از فابریزیو رومانو: پاریس بازم وینگر خرید! مگنس آکلیوش، وینگر راست ۲۴ ساله موناکو به پاریسن ژرمن پیوست. مبلغ انتقال ۵۰ میلیون‌یورو و تا سال ۲۰۳۱؛
هیر وی گو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/102491" target="_blank">📅 09:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102490">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b17b2ecad4.mp4?token=bzBR6DKt9lRKeumx9HAdkUIxhjQg70eXGvLLwmJU6X-5JFMCTlECl9-c1TWTJYbjV5c1GQHOz0D2oD-1l0VTbHsWrKAqt1WqtoIX2kR62kcxFWp1x1S316KOY3Do-DpRBTOzqwIoCrzZ1sD9L3mgww5V4w9h-PtTL3uHDyFeccWSvOl9cy8nC5mepI2XgvDiK8hD2qmO3J8GAd7EGxMVT8j908AGnS0KyV0Mi5pdgBbR8Yo1J_7g4juMjlJqQPB7rv7IOM-SLGPzyLzIAj-rfwiLbWRdsFNKSJSQJs08__VPwTBBngwlbaS1fhx2byuIhYO1uXELzZtFZA63iSJnXpssTbXQOMTAcpziOsyDRr3kNIITDfoRXgLLMob9wK8ZE5fEUHS7M6zAzYTWoR4_0Eot5f37jGyj_rFElGcI4DmdN1Xfae__KFC1Jcwhbm8QOg0yMp7iUkWPpgvXVoaxxCcW2CCQ9y93ZGWBM8vForzuMb-YX1IJ5iKgL_B75mJi6e-frpvoUs614nlZ36DSOowM7zXmueHCvpKnbE4zvKCELYFgoXyLYwmFib-Th-FPR8RR1SfELHgsIl7axPSysI89HJ5YVHL8B_CVrIMQ-Foq25Ejn0Tagu-_VR470Nnn2ehMs5rJk-8VdQiQNAym1E8wvufJok9-vbDkj_50WVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b17b2ecad4.mp4?token=bzBR6DKt9lRKeumx9HAdkUIxhjQg70eXGvLLwmJU6X-5JFMCTlECl9-c1TWTJYbjV5c1GQHOz0D2oD-1l0VTbHsWrKAqt1WqtoIX2kR62kcxFWp1x1S316KOY3Do-DpRBTOzqwIoCrzZ1sD9L3mgww5V4w9h-PtTL3uHDyFeccWSvOl9cy8nC5mepI2XgvDiK8hD2qmO3J8GAd7EGxMVT8j908AGnS0KyV0Mi5pdgBbR8Yo1J_7g4juMjlJqQPB7rv7IOM-SLGPzyLzIAj-rfwiLbWRdsFNKSJSQJs08__VPwTBBngwlbaS1fhx2byuIhYO1uXELzZtFZA63iSJnXpssTbXQOMTAcpziOsyDRr3kNIITDfoRXgLLMob9wK8ZE5fEUHS7M6zAzYTWoR4_0Eot5f37jGyj_rFElGcI4DmdN1Xfae__KFC1Jcwhbm8QOg0yMp7iUkWPpgvXVoaxxCcW2CCQ9y93ZGWBM8vForzuMb-YX1IJ5iKgL_B75mJi6e-frpvoUs614nlZ36DSOowM7zXmueHCvpKnbE4zvKCELYFgoXyLYwmFib-Th-FPR8RR1SfELHgsIl7axPSysI89HJ5YVHL8B_CVrIMQ-Foq25Ejn0Tagu-_VR470Nnn2ehMs5rJk-8VdQiQNAym1E8wvufJok9-vbDkj_50WVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
بازی‌خاطره‌انگیزمیلان و یونایتد در UCL 2010
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102490" target="_blank">📅 09:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102489">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">هایلایتی‌از بازی‌جذاب الکلاسیکو در فصل ۲۰۱۲/۱۳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102489" target="_blank">📅 09:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102488">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7q3yDIgOI6aD9ghFxhJoTVh4n0mdf0EeF7cgAIfUN5UaLBoPodJQ7fABvyAn0A2_IgWzidZd3yq5DiHSmahw9bcm1nB38TQqsMUkKNQNcA_0MuuDDfNha7Knt32VAYGrrEZvbmKYsxg6MYEwnMuARJij9-XoaotDAR0ExOgGsUY5Rm6vwpUbbpXfu8NP-tLVuY5MYgB8Ihzi5rs2f4-K4q-49zAwKwT8Bt4a8htqvVmlWMMK2OvNvvPZt6ZuNJsZwb5iMZDPRK7Q1JLYmS4wbrzCgG-d21RNsksDExh0clfkcjk5TlfLY4LJWfazfydvawqu-mfCFJNPie0lGxpuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیکنای اون ترکیب لجندری بارسا چی میخوردن؟
مسی عالیه :)))))))))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102488" target="_blank">📅 05:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102486">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eF96ltloueL5yidqKhK4m68FdV-Hf77RpL3qW0DjoSWIKRQTDvTivyZmUlrR07YqjffZYq20j3BYGtIYQ8LDLxEXOb_vHcWYmGYtFv5mkywik77SJG4uy7KMpK0f4UpeGAlNnsUNhm30l8vsK1L-Z7WoHxBFfNTHYYTrXDWTQ5jr-oP-hUYLY-VLbBaMaOHkL7L_8cLTbYAc3186RQNUpqdOOBCYSjBGDGBnlfVdUqpSdwCDmr-BQOlK0ffwhemuA9I3UgZgkop8NQR6dvhE8r_w6dNF587G1dRss8f35KzuaMOiLsXTjyjVJ6sRO4xmLZ6Feifn0NBNwZYcjPLHnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
گوئدس ستاره باشگاه آژاکس با رقم ۵۰ میلیون یورو بزودی به psg ملحق خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102486" target="_blank">📅 02:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102485">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
🇮🇱
کانال ۱۲ اسرائیل: نتانیاهو در دیدار اخیر با ترامپ موفق به راضی کردن رئیس جمهور آمریکا برای بمباران زیرساخت‌های انرژی ایران کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/102485" target="_blank">📅 01:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102484">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQDH7c-fhzdJn_b8zAOt5swZaDYJfIcJMTqAsxkuQ8OYO7uEDpeFijUjGIe3Wf02o1s5El7suNkzRnJ5bfMN0XCMvx-AC7LRU6u_YUB7r5U4P5GXQwEGWkm2UTumwkWBDyO_4yXeqZ9OFFeaFgfCL53suqctbf3rGe3l9uquMuHeY0VhNkUBdZ--yU13qFRw9xmd9dLKIenagc0tv7jzXW4S-qwXX_mjyvByBiHlpX2L8rXNFW_1RTpIxh0hYmHvU_f-Q1DyTg1Q-rWnjBvUxbzWFyE2pJSqbQ79cQXscepL2B2S_IGCMU4_wtkWR8pDpzYExDa0TMS0ejNYNFf8Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب بروبچ محله تامی شلبی حسابی واسه جود سنگ تموم گذاشتن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/102484" target="_blank">📅 01:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102483">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔝
وال استریت ژورنال در خبری فوری از صدور فرمان ترامپ برای آغاز یک حمله نظامی جدید آمریکا به ایران خبر داده که می‌تواند بزودی در این آخر هفته (شنبه و یکشنبه) آغاز شود و چند روز طول بکشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/102483" target="_blank">📅 01:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102482">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edBSh1GaeRuz_SnJxCe5heoOIidGWrOlkBi4pdNa_Ybi_mWeqsTS61lTv2C0PauZ9jUPilccCnod-EgQAlFJ6a63Y-FItjqTHRJTaBGqcl_PQPJ8BMT5vx3n9WJS2XIoRgKL2YpY6R6XYm5qT2q-wXY2osRlAT0jxsdnigDNibr5sVcfp4SINpnH3W4nmZEb7yEVzehx3nWVJ1LwsAcaRLnSv5WskzD0mi3SIRY37VRlYAY8s5QKyYaxwymBJNjeqmUma0HB62tBaTy-NU_if1q2Nin74ynFXTSoM4LnJ8tWZa_93tmBU-J3-dbTdRdvULplIIrpoJRq7y35TJTtKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔝
وال استریت ژورنال در خبری فوری از صدور فرمان ترامپ برای آغاز یک حمله نظامی جدید آمریکا به ایران خبر داده که می‌تواند بزودی در این آخر هفته (شنبه و یکشنبه) آغاز شود و چند روز طول بکشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/102482" target="_blank">📅 01:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102479">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y1lY4nX_NS_1lGl76WSpFtpCttQvzASce0ln1DlP_oDEJRzHqR35SfCbeLIGQft_dvHjRD78kE2boANSDaMPuUAnytaSs2ajyFz1dUnqgSBYFDQlFdUPmBrIxhNbWkKiNwTydXBXV9nr4y8pm7Eb5fng0BZIFpNzmCLykbYCmPIz_ViVBYbC_j-1Qq6aVOQckY6iwK57oFiWo2Bo4_kUW8XPFFOL__cE1ugKDAQB69KslFTRKYVkrDzLpYnruDPxpqcsSZ9kzod1yjt586HPLm8aCKhSz5LFQ1I-dwacSA8c3qVsSlhTBUSCk8prnu7qHS5JCHdbVQHPxkB2VRhMXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iim-C1yAFr6WptGSNUeEHDpMVnWjUe6A2XkpuaCVcsHBghnaoRT75hraA6xfJFJC0WguiuboBvmJafGwUE1GSKWsWMupVtj0k_QdEsBlgeRs_hW5uEfpBP_fFo5eFUlvqVN4OyYZN5iquAs-M1my36BYPES06dXTavWyTcwH-QY2WQXeF93covsRROnyAdJmRc7NJtqQCbmKAym2JEcQScUKxiONui8VKARdF5En7b-AYtAU4V06l801c5gWpZWWuwTDsgxILc0Ax3ZgjYr9KcW3G13L6ZfeblyDUUjA2tC7XeHN-iYQ23AdDcnvLvRtmIaeJEUk55iNVRrs5tdxjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j6deKlP5xYjwdAoUOsYZWyb2kHDXxua9_mr4Ds00_R3I7P-MnO48rYPvWKHBQS2XeHUiEt_XhdDbGmlL1o9UVEd-wc2zPXhaSdFxUyw2j1H4kNVJ_IhausjpfkPpfGG_leRxuIzdbcKOtvRlBAto4CigvJphR9QpkBjMNXIW5JoigvLLTn_3JvvyVlk0qDqr-hW47z1ndexKD_KvMb-Qp6nk6RYoD8p6_m4Koq6mxh-CFl7bYEcQAVmkJjdzzmjrkTA9Tusxm_Xh2xNXAbmNsuBZN5AAb7m-T_srYURCjqm3RgOjPWfCV_ZclsioqPyDjaKLccOJhdHXWV6CmBW9Qg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
باشگاه فوق العاده محبوب آگزبورگ از کیت خودش رونمایی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/102479" target="_blank">📅 00:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102478">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkFlE-owQZT6m0ZKCQa5g38KYkXzgIpfd6OM4A5hDpEaVVwkPoGGrT8iC376XAFVAzcnugZT-UKq8zcN8gBQ5j95ruR2LE2XAM3pczwIOEIJqujBdREwdIAnOWZXSv4m_405EaTlXUKMI90l0prH6VvR7Eb8HQIK_mG4CfUBcoq5NG4lHXYM-B8yu2_w81kxbew9Pmvl4ne2UjpeLF3TIZh8gJCzeRlYIeWuCSoQDeKyw63sNwkHjchVDyYgzn22FETnDpA64eOuedVTCYbAhr1HaHGt3StsMQebAPUgKCQe-XlZpZhBcl9HEDj1bB1EOAQEYLpEDbeMw8eYbfg22w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
هندآف آرسنال رسانه نزدیک به آرسنال:
وینیسیوس شخصا با آرسنال به توافق رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102478" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102477">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی،…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102477" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102476">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=Qq-ui-Yuh3JyYkEL0zHAvWbffyVbr1ZpIYHzgNpKO_bWY_VNhSegorGBSrwkIvNjTE2jjhmg2DrCsaqReSjgIK7pmwA7s58qsMJOHxhUo0LMw0hai6uHfyUNPgrdbp68HxPQKiQrs1phdKbShlqlZzPNXaXliu81aDJMrT3m4lCp4_RYf3Jse2X28OQ9SJjY6BLP2HNjcbfCSk8Q7pwL1VMxIIG03e3GAhGsqa-J0aNTM9bKbcT-TgHKG_wK5k7C_SvuHfcj1nYzPlmnTMBGsTQqdO5G52-gWlKoLWuCVP2okYWsfEkXk7ppCBd9qVBmgvT5_aqwahLkxMfBBXA5dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=Qq-ui-Yuh3JyYkEL0zHAvWbffyVbr1ZpIYHzgNpKO_bWY_VNhSegorGBSrwkIvNjTE2jjhmg2DrCsaqReSjgIK7pmwA7s58qsMJOHxhUo0LMw0hai6uHfyUNPgrdbp68HxPQKiQrs1phdKbShlqlZzPNXaXliu81aDJMrT3m4lCp4_RYf3Jse2X28OQ9SJjY6BLP2HNjcbfCSk8Q7pwL1VMxIIG03e3GAhGsqa-J0aNTM9bKbcT-TgHKG_wK5k7C_SvuHfcj1nYzPlmnTMBGsTQqdO5G52-gWlKoLWuCVP2okYWsfEkXk7ppCBd9qVBmgvT5_aqwahLkxMfBBXA5dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی، باشگاهی و دوستانه)
🔹
پیشنهادهای دقیق گل بالا/پایین (Over/Under) و گلزنی هر دو تیم (BTTS)
🔹
بدون ادعای واهی ضریب ۱۰۰! فقط سود مستمر با مدیریت سرمایه.
آمار ما در ماه گذشته خودش گویای همه‌چیزه. فرم‌های امروز رو از دست نده
👇
🔗
[
ورود به کانال و دریافت فرم‌های رایگان امروز]</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102476" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102475">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufscc0n3k-edWpvmgTmFn5gDG0_6E3vk3iMJBom0gejWtqkz1zmMM6IS5ZoHavqoakVydSkL6Z1asXGb77O-nhxHa-nMsoKyCMVAT4bGY_DiBRmyZT63Hxv2RNrE__e3hr9cbptvjqvRHL-xnYBtuwbLeMWgFG-AdLf5Z8mfrcuFd90e4YJyqTJ6j33PAe4HZW94AABl3AV7J3bJftQf4eNu8dQAA7QjOLqIHTUvZqO5VJHURGy6vNZ9wI0-I7tWrGiuLwrNZmfpk167mWXM-xa6QLDfFwBCXAq4FLFH_VW_6NsFoEtNmM1V8-qu7WxFqb8Vw1fQ7naZPXHaG0yKDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
بارسلونا در یک بازی دوستانه مقابل بیرمینگام شکست خورد. بیرمینگام با نتیجه 3 بر 2 در ضربات پنالتی به پیروزی رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102475" target="_blank">📅 00:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102474">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3vLy8Ox9Lc46bnHEzCrsMGwBB-YQD6utbtqQYq0aRz50RJuNUJQ_LyRn13aTAL1DPMudx5D0NL49xdb4VRiFtknflczT_Gn6b_Ex1TC9aL6boNfYH0bqwLO4xY0ptQlV-Qgcuh30ejYG4ADBGmjsSIhFSE74_WoTd1znOWWCSb-GbAV0hZZQ7AA5YB_LYSZGxFMu29drYv9iLwvtZXkrO37wsC9UBVNvoT2s0tyqfq9kqokfTeDwoBOMISBqh2acy1ItFU0KPoTwbvwM63oy762_7j4aa3IRk6SCdh22CFiN-LhiSmPh_wzmAbUbOwvpGtq9hgJ86-h-v029xc39A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری دوست دختر یامال
😦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102474" target="_blank">📅 00:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102473">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EeBCvPYP8foREWiOVWvgEQgSUMOJ-OQ_M8T3JJDkGykfWSmULbiREGeOl_oy3xxjdcKAAHh9JjpGC12TmDykAmCsxW7p9Bmglstx2z9MdJts-6Kg_sUPvwGJ11o3ccppNvzobXLCnK-gb5fS3zBCAfsgXyWJto8huSkAbfSlffeuCx57d8i7acESOfybsT91QVeDArdjqCsS80P2bTByX_cVog0IladSd79rVY5hEPdC8jHG7uzS3lCBWm7LjmNrNo4aZtfHny4DhZbXFa3C7tBFOscFojnPiS_AGo1-RcyfWSJbtb7BjG5TFSCcce-3MAyAd7NbwaQmqaBRCQRDXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟥
🤩
خداحافظی امید عالیشاه با هواداران پس از 13 سال حضور در پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102473" target="_blank">📅 23:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102472">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MX2mcLp8zNDmpaVtUsJylilTgmR_-dbg2tF9B2jB4Ywxy1Gaw7GUIs24Fd5ZSABLISu1gGwCboXTZJBjjDOh-DygocMUp_DYk--PirBt9TweRWzvb17qreNkSQvrrSpeSyvIyGTP_0y6dZY3ge9-elO1tFZD835Dxx7Ra23fyyLBoYlNoZPeoX2DqP187fILsD9mGqTrNfRoCnGYvu7QtJL-heSlBQk7y0l4vqXaraikhy16ohu7mbCNTGTTgaR6gP2QjBEOlSHP2rwqft2YxNyY66CXBQSnVtYpCHDd5LsImgM7MobvTYZUKjaxJLZs1ZNKAkPdWEmsgu4xdOA64Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
مسی و کاسمیرو تو تمرینات اینترمیامی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102472" target="_blank">📅 23:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102471">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26c665525c.mp4?token=pjUb104t4htfAxAdieFhbZSrHWJfKjRZd_PRe9uohl1-UdLABg90hU5eUABcpyQWT3cRmTGWCGPaWsdYlOxheJaQtSbeJLgTgIHrjER93E2Pewvcgf2-6zFhTn0DwFgoHKE1F1puE2CQQVNZGLB-pQyG3w1XmN-h43rkY9q6UtsJ1Ie7TnzwhBhsjBHk8rE2p_1LFeyf8ezRoVVhsKSPyi5P1nnu9BJ5lInN_MzdSMd2L3tSuMc6jmP-eXX2AqJuqdGZvWAjZkTJUHlDQrHRr7gE8Kmv1nc75zMtO_c3On8CMg-ljZ_TamOb2j8iiZC5ju0a1kYTCdnYyjZ7gWaAfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26c665525c.mp4?token=pjUb104t4htfAxAdieFhbZSrHWJfKjRZd_PRe9uohl1-UdLABg90hU5eUABcpyQWT3cRmTGWCGPaWsdYlOxheJaQtSbeJLgTgIHrjER93E2Pewvcgf2-6zFhTn0DwFgoHKE1F1puE2CQQVNZGLB-pQyG3w1XmN-h43rkY9q6UtsJ1Ie7TnzwhBhsjBHk8rE2p_1LFeyf8ezRoVVhsKSPyi5P1nnu9BJ5lInN_MzdSMd2L3tSuMc6jmP-eXX2AqJuqdGZvWAjZkTJUHlDQrHRr7gE8Kmv1nc75zMtO_c3On8CMg-ljZ_TamOb2j8iiZC5ju0a1kYTCdnYyjZ7gWaAfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین ووزینیا که تو جام‌جهانی تک تک تیما رو سرویس کرده بود، جلوی علی علیپور اینجوری فحش خورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102471" target="_blank">📅 22:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102470">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzIl1I2GVhQKQk2F4JFtYlPiK9BJjgaSfF99JUQruJTt3xzo3u-rQoYGfPQC8Ys73qHm9PcxwwG2oaJTZiYAB4JqUYoZnifzoJ-yN6l8UxAik8UtN0ZnHTCyLhyR_qTSXOaGxtxbwZVg3szpuPg5dTQJiDjW36-mDvdSqvlrPM1tiKASzFQS8_cl7nr-gWzNMHv4GKdU3pCg-S9RfLvwkXH-oSwhdHhehqFFpp2y3dcMg1-9lCgUAIbL6C34WQonuvfFjwCKYP-zxrpq29bDXQcB2Ip5iwvKJTTukO-3Vd2AGZqn84gdHiVmGz2KjJNe-qDoe-ePfZleHn_wS3b0jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ار‌ام‌سی:
مندی تو وضعیت مالی بدی قرار گرفته در حدی‌ که مدال و کاپ جام جهانی خودشو 54 هزار یورو فروخته.
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102470" target="_blank">📅 22:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102469">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/261dc7eb19.mp4?token=viqih-vFLSsgXqi_E1JpP6bc002sGtB8FR04y7PvklprVr-ndHiuILTA03tl6mYDfaWNm1UwaPtLgl8RexwKZ8j7QUL0HNvu7H2MlOg6zuqz1dIC1U_avuOl96YV8mHt4zEj9ezxulKTDPGwju9vq7wIF4MRo14gZshbELp15lV3yMJDS79I65Nj1Wu_QaYecc8WXz-aq2lc3WLwob7KcbVnyK6JMZMEY3COCJ3ChQhPFL-s8xy2wXo1oVwX35yhnzEpMEsbCLktVGCRAZiqjnn4Sve0UhxBm8MXHEwM_01MsynesR_9DCLuYicE7o-lavAKdeH-3-0VeEKh2wieOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/261dc7eb19.mp4?token=viqih-vFLSsgXqi_E1JpP6bc002sGtB8FR04y7PvklprVr-ndHiuILTA03tl6mYDfaWNm1UwaPtLgl8RexwKZ8j7QUL0HNvu7H2MlOg6zuqz1dIC1U_avuOl96YV8mHt4zEj9ezxulKTDPGwju9vq7wIF4MRo14gZshbELp15lV3yMJDS79I65Nj1Wu_QaYecc8WXz-aq2lc3WLwob7KcbVnyK6JMZMEY3COCJ3ChQhPFL-s8xy2wXo1oVwX35yhnzEpMEsbCLktVGCRAZiqjnn4Sve0UhxBm8MXHEwM_01MsynesR_9DCLuYicE7o-lavAKdeH-3-0VeEKh2wieOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
تام هالند یک‌بار به ارلینگ هالند دایرکت داد و از او خواست به تاتنهام بیاید، اما ارلینگ اصلاً متوجه نشد فرستنده، بازیگر اسپایدرمن است. بعد از اینکه ماجرا جنجالی شد، هالند برای تام پیام فرستاد و توضیح داد هیچ قصدی برای بی‌احترامی نداشته و فقط او را نشناخته بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102469" target="_blank">📅 22:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102468">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCfxCbOQAWFXwRbrso7jNeATnTj-iHa0PE3lGTNU7dU0MibS4yCWXajffkPqG5B5MqD67j5pZyjChf6jT385KzgrF03UC5dq1fq4_xxGyryufDPMIeYEmsvG6JvVU2q4w15GKqP-qTZyWci95Kc2JXgVvAGpBYo63tQg3bDL71ND_o8rC5z8KoacwU_U9pdILJm3B42OwHfLcgKwxAha0SnU5LnGF38-OH_h1Rrc7pj2VMRQhPl2Y-RUJSip2Q-aN90cXps14_wJFAnb1GXc9b2vxnDV2dib8m01WTmrHeFxnM4ESsrOcJrgNu-5zQEfIXKqy6lkCB6bT_MBr0R5iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
💣
بمب لاپورتا ترکید:
جسی بیسیوو، وینگر بلژیکی کلوب بروژ،
به بارسلونا پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102468" target="_blank">📅 21:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102467">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bb_eXwbVenp62lec6e23xzR68GFoAdXwpd5M9NIJ9Q-TPntAlyzC3Dc053BHCJDHvlTkdsYZJP8CYH_twSN23DYqf0SLdPHX7OLp94iwTjOdn-XtsWNpX5JGidUMkh3L3FwO5KeVIwRYhET4A5W7BwQvwsl7QsxIo8oC08Q_K65w1yz-sz30LTCZe0q6_ofyDb7AmTCnIiXRC6sDIPELOB-X6OqyfxSMWSaIZ5YmQtFb2s4jBrxC_yhJvbSWXGVHDJELDgASFGslgGG3Jjf4Gz-BF1e3FWRUH3sn7vv0HZuDDcYG1asddpkZlpO7gRQ50vZlPUf5FWapxpLhyhN_eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب امشب بارسلونا در بازی دوستانه مقابل بیرمنگام‌سیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102467" target="_blank">📅 21:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102466">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f4d6d3d7.mp4?token=F9xjSwD8sH3fv81FWW9afwdkmt6OBkKCUgWxBD49StF7xQadQyNIOmINIitlYwfX5_xHONSzg9jDGeljlCSQkohpRJt7aWbKCgTwIZCoS6ASIkr6AB_ttIyGRCU5rKekc2XpBrzDnZG2kE9sylrFDio2uOVqoI0CP1tA1ti2dBfRHa_KdRg_s6_UCTe4lN4eNVQbmE2_NSLkyxyiuo2Px-zCMi59nFNHMJmuMAFi2yZz5dEEn-NFOEPwof1lE5Y81Yzz4qWEIqoDygXBZ8c7tsffgwMceXy2JWe48S_1X-xyXOhcLH7YQP7nghZKzwcfofmuUt0us4twM8YjGBg3pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f4d6d3d7.mp4?token=F9xjSwD8sH3fv81FWW9afwdkmt6OBkKCUgWxBD49StF7xQadQyNIOmINIitlYwfX5_xHONSzg9jDGeljlCSQkohpRJt7aWbKCgTwIZCoS6ASIkr6AB_ttIyGRCU5rKekc2XpBrzDnZG2kE9sylrFDio2uOVqoI0CP1tA1ti2dBfRHa_KdRg_s6_UCTe4lN4eNVQbmE2_NSLkyxyiuo2Px-zCMi59nFNHMJmuMAFi2yZz5dEEn-NFOEPwof1lE5Y81Yzz4qWEIqoDygXBZ8c7tsffgwMceXy2JWe48S_1X-xyXOhcLH7YQP7nghZKzwcfofmuUt0us4twM8YjGBg3pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔹
وقتی منچسترسیتی حریف پیکان نشد! سال ۲۰۰۲ پیکان با سرمربی‌گری ذوالفقارنسب برای آمادگی در رقابت‌های لیگ برتر، یک اردو در انگلیس برگزار کرد که در بازی دوستانه مقابل منچسترسیتی موفق به توقف این تیم شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102466" target="_blank">📅 21:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102465">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bcb0e2d66.mp4?token=muWJxKQgxqhT2-mn-XmPl46A-g9JwrpVlgHNJisulRgnrw-B34Av9OxR5WwooXDg1q3P2tM4F035WIIbnvqNPAlZUmIuckM3ZCWxNLbRZnTr0mnkjhPYjFsb7YG9CnOFpn9Nv2_Ll1jw2VT9VNaKKKQYinU1W86_ConTOYggbwClHCuagFCC5n1b2ey1609E0_GZCD9rsBT5XnLEpabNOXHeWRO72baBSjFhh4ea0EIAkuureBj40yTax_b6lAzF4J8XO2KVsPamrqOVseUbxBCSQuMqrREdolrMTNIEsBlM43yA1eFs6trpxHMJj7HvLzjKVPo4c-vBx2W76frmnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bcb0e2d66.mp4?token=muWJxKQgxqhT2-mn-XmPl46A-g9JwrpVlgHNJisulRgnrw-B34Av9OxR5WwooXDg1q3P2tM4F035WIIbnvqNPAlZUmIuckM3ZCWxNLbRZnTr0mnkjhPYjFsb7YG9CnOFpn9Nv2_Ll1jw2VT9VNaKKKQYinU1W86_ConTOYggbwClHCuagFCC5n1b2ey1609E0_GZCD9rsBT5XnLEpabNOXHeWRO72baBSjFhh4ea0EIAkuureBj40yTax_b6lAzF4J8XO2KVsPamrqOVseUbxBCSQuMqrREdolrMTNIEsBlM43yA1eFs6trpxHMJj7HvLzjKVPo4c-vBx2W76frmnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⚪️
رونالدو چرا رئال رو ترک کرد؟ شرح ماجرای جدایی اسطوره فوتبال از زبان خودش.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102465" target="_blank">📅 21:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102464">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ed94c011.mp4?token=Dkto4UJyQ_DyQlvDZ54vFfp8MYSgwEnb8n6jTRG2RoF3QREFfd1vfaeTskuXf_TqhEWs__8FXtKOVtBKjMWeAQy8eIeMa2ucW8xOHXo_6RYNzB455O5moNu0c2GsIu1iF2q8Dz-_k0x70kbQ7aUnvakR_hT4FX_puQLW5yJFxjlww187K_A5hQ0TaHW8wnQbgw0m4fKHZlmRJ2VfwKAj4UkaXmDqC5pZAdaGORbRIqPJAiQTyxIX7xHv1L_rkpmzb8xy4rNsa0bMg0H5JxkcWRsp5X_oOIaXjpj_rHlUgk2_UrVLeTDsc1khO78EJFZ5aWZDOrucd1T-WjT1jbcRAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ed94c011.mp4?token=Dkto4UJyQ_DyQlvDZ54vFfp8MYSgwEnb8n6jTRG2RoF3QREFfd1vfaeTskuXf_TqhEWs__8FXtKOVtBKjMWeAQy8eIeMa2ucW8xOHXo_6RYNzB455O5moNu0c2GsIu1iF2q8Dz-_k0x70kbQ7aUnvakR_hT4FX_puQLW5yJFxjlww187K_A5hQ0TaHW8wnQbgw0m4fKHZlmRJ2VfwKAj4UkaXmDqC5pZAdaGORbRIqPJAiQTyxIX7xHv1L_rkpmzb8xy4rNsa0bMg0H5JxkcWRsp5X_oOIaXjpj_rHlUgk2_UrVLeTDsc1khO78EJFZ5aWZDOrucd1T-WjT1jbcRAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یک تازه داماد پرسپولیس را حذف کرد!
از ماه عسل برگشته بود و چهار ماه حتی توپ به پاهاش نخورده بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102464" target="_blank">📅 21:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102462">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🔵
🟠
استقلال در نیمه‌اول مقابل فولاد با تک‌گل ابوالفضل رزاق‌پور شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102462" target="_blank">📅 20:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102461">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f8b6948d3.mp4?token=mMCJpxF7-mk3__WvVi1Xsfy8DYerodur4zjq6GWhx4mA6bhoRWckpvULlByaAvJm55KkH2NCU7WNzxFcTs6-bq1Dl687oiORXXbBVRZBnAc9eRQ1TRk55p9gEyDNZShdK5RXfuJHLSMIDDOOtuQA-C6I0n4f5EY1KkCEWAKIVOILOn5sHNgmLOjb7W7GMsABngxQnE2Hex3mgmB8RfBO7qHKiKYGEHrk1lrDdjvFs0ppDSNbiz6bs_Xmv5WL5gsVzj-ZroDd0M26PRFBP_L_gFTPuYAOSmV_9lF66-xmXKYhdG3YX7V72Z0qFT_3pva-MPs5EgCzq5s2njIb34OIlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f8b6948d3.mp4?token=mMCJpxF7-mk3__WvVi1Xsfy8DYerodur4zjq6GWhx4mA6bhoRWckpvULlByaAvJm55KkH2NCU7WNzxFcTs6-bq1Dl687oiORXXbBVRZBnAc9eRQ1TRk55p9gEyDNZShdK5RXfuJHLSMIDDOOtuQA-C6I0n4f5EY1KkCEWAKIVOILOn5sHNgmLOjb7W7GMsABngxQnE2Hex3mgmB8RfBO7qHKiKYGEHrk1lrDdjvFs0ppDSNbiz6bs_Xmv5WL5gsVzj-ZroDd0M26PRFBP_L_gFTPuYAOSmV_9lF66-xmXKYhdG3YX7V72Z0qFT_3pva-MPs5EgCzq5s2njIb34OIlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شزنی جنس رسیده بهش و مشغول دلقک‌بازی تو تمرین بارساست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102461" target="_blank">📅 20:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102460">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ace3163b65.mp4?token=V6UCWYjkHWLYFOB-DJ6K217OHxhNZt8rlrvOcaod_LCJrXF7qjMf1d6mSyf_OffBW3ev39bq-G5j_2ZcV7YWhjHZSGd6Oem27R430S5GmF03-aiSoHCHRndl5fi2lx24PfMdMiMFTViHvd3CIY1RSWawMZJRJlH5aNrEFHuJSUqM2zvSs1ApCAAMwQItxRQSCffsc2u4zbci-cXRltpAE_CplthY7z6qRhwoqhlTELpeU0OEJBqqkMnli1H_gFl_uKRnGCrdxlPW-nO0jprxRAyKM3JCIY9Z3yrw_9VAKpxk1xnQoj3RYrMtzJZMG8t0BjqFB4bMP1IDc64IlQc3QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ace3163b65.mp4?token=V6UCWYjkHWLYFOB-DJ6K217OHxhNZt8rlrvOcaod_LCJrXF7qjMf1d6mSyf_OffBW3ev39bq-G5j_2ZcV7YWhjHZSGd6Oem27R430S5GmF03-aiSoHCHRndl5fi2lx24PfMdMiMFTViHvd3CIY1RSWawMZJRJlH5aNrEFHuJSUqM2zvSs1ApCAAMwQItxRQSCffsc2u4zbci-cXRltpAE_CplthY7z6qRhwoqhlTELpeU0OEJBqqkMnli1H_gFl_uKRnGCrdxlPW-nO0jprxRAyKM3JCIY9Z3yrw_9VAKpxk1xnQoj3RYrMtzJZMG8t0BjqFB4bMP1IDc64IlQc3QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کول پالمر:
برای بازی مکزیک - انگلیس بیدار موندم، ولی بین دو نیمه خوابم برد!
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102460" target="_blank">📅 20:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102459">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6RVNOLkvr3SGNf0t4hMaWlABrGdoTvFxEU2boqRprgPBOtmwWrfuj2wd4gCu0TGfH6UJT34B-bJ18JPwQCL4cCoxbXQtVgJAG_El2BhbK90jIV5Z4DikwHMMu7z5Mly1tG20jp_r5XC0g2gnOLkwmlymXMyx8MxwuQkRQ-jed4BxNm1LshhPOfSAzcSPl0kcVzyfJFWmDpV4wffaujAnEBMyngbpaX5hUEddwNaC75hf9RkdG4qV0zrP55tEzvXPELvRXTZAJu8Wzj2wan0mlLklgIauX8WlgizuAOG7tnygJp7kBw4Fno3764j3IR0lvU1AEe3W2p3FtJ8HJNiyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
دیوید گرافسون دبیرکل فیفا تصمیم گرفته که علیه اینفانتینو کودتا کند تا وی از سمتش برکنار شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102459" target="_blank">📅 20:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102458">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgOGwlOUlUV2nNmRkTU5htprlgM_S4V2uadAgDAoyHJEykf8LJpvkgKaeX7mFWYwddt2FY57RkLaGu75ZMHksOf2oGMji4sRC9xLTXseSPd6hLUZsb0iO5dz40lNTylzcPbFHc7Y7o15TauyZIu2oSHBCy2J8Vz3o6-tEuXv2RbPk_whuDdObyPpF5-wtz8gF_Oi5-yejDz3V8LmEhPwyjlRtV2o51nTjV_nQw2JMjLIZxOzmJMWHFifsE4t_Lgys02QKEnIxzQ6ECpuF3MEuN4-3--y9vqBYlojmqVJUdE_05xZy8Hn1-MniuoFhtjxvTInw32SsTk0zZfEE18VtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
📊
فقط سه بازیکن توی ۱۰ فصل اخیر تونستن در ۵ لیگ معتبر اروپا هم بیش از ۲۰۰ گل بزنن و هم حداقل ۵۰ پاس گل ثبت کنن:
😀
محمد صلاح
🇫🇷
کیلیان امباپه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هری کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102458" target="_blank">📅 20:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102457">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqiJDhDhjwfRy952nKvl3rboZ5JrGt0FFiscRNWwiya4c6OBoFc8MCduM7KzqgjGESQ0WpwJOzKYlWesU6ivJH_7akr0TnKpFXCwttdwIA0xphXE3fPZJMMGDIzme34VWdIy20cwF4OiA6gc4VSrw2z2k1rrBHFAuewjPVBA_COLmLRmbA_c0xum-iH4EUmQCDW-TW89EUfHMi5HuGBSL8pLe1zz7VSA0xbCOIBHDiZRwW9I85L87fizy0OzvOjb4alWvFclFVs71gNwFwxQd_wbHonY_K3H1DzHDKv-ApwA60nHcL8F_uvvnqAxEVcqwLUTbm4hS6yUV7H9ZGjLuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
دیوید گرافسون دبیرکل فیفا تصمیم گرفته که علیه اینفانتینو کودتا کند تا وی از سمتش برکنار شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102457" target="_blank">📅 20:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102456">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🔵
🟠
استقلال در نیمه‌اول مقابل فولاد با تک‌گل ابوالفضل رزاق‌پور شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102456" target="_blank">📅 20:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102455">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kibTAquHRbL9iuHfPCoY6rmM6lQapRVearOf_6wHnrZ4lo0lrfsw7y0d9GhVyH6igxebb4wv3V_NcYHKrdYBg3o_W8CQKrQ1Fu8sUW8_FWE-64zWeYCSzmPjZiMK_ai3-U1h8gRetK6RbeLzuj1KUMAYMXSUxK1Guuzgnt0WaIVLexFMpcCZCC73CscvgvY-WpacoE6_o2S0HgyUYdQDP5AiE5TCRdOGTno-3YVOCwaepv14wC42Uz8G_CeTpDziXX7XrAICtSSIjtR6D3u8trBhBhHFNV_iQOwHNKblmak_-1Q01KUpnz63nhaLBFLYfoHWOG1GB15qENa6MRb9Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟠
استقلال در نیمه‌اول مقابل فولاد با تک‌گل ابوالفضل رزاق‌پور شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102455" target="_blank">📅 19:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102454">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLa8JN3K0lyuF5JBPmHVtg6P_287jjk44DRugzAldZzcVpRmpZOGK5zr6MDGQjoU-3kij_JIiUZfbkaj9uCTk8MqZjFFNkGuZNv_eOm1h0jS1aO8tiSXdK7V_RqwrSvgWiuIr_COZT6flfpVaIZMOTb3s-wnrrocrLVZ03Yl_Knzf_E1_6eU19xMI1-NXSgvwupunJrygoFG6Yja_j2kyPoElZXhGVg-rb-dumFbUcsmD9UTMcjdFtkJWMSykOK9ktaVrXEtYiqN-QHmdeqIzWdf84lmeKUWS8aYyJ3M-DAWP7lJ6DosHxQAR1mSCe53xS1uHlWtVtxPIfVu3cZSQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇯🇲
وینی و عشقش تو تعطیلات در جامائیکا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102454" target="_blank">📅 19:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102453">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
📹
🔵
🟠
پخش زنده بازی دوستانه استقلال و فولاد ساعت 17:30 از لینک زیر
👇
https://t.me/+E5pLb4kNVJZiOGI8</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102453" target="_blank">📅 19:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102452">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کاسمیرو به همراه خونواده که دیروز به این شکل بعد از معارفه عکس دست‌جمعی گرفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102452" target="_blank">📅 19:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102451">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_MRkOlfzSb_e_i0czt_iyS9_UzqDZTKf1ef2TU1aU2B_IZiuD28M-nYC33Um0je6w0t5OrjQ_6rsqVXMdJHhoQYOYWnt4h1xS5-3JxTq0xPyDHocNFBs3rd8Ynbxx--yIakvRQaQlU0h6010EVZ3MV_dYU06-Vbgsdm1R-vepPdDMe7-NlSmHpZHw__d3Jtnyl-pDuDvHeAbDv1tkQqY8Gyfv-leNTm764NA5o1FDr0eqHlaqRytsRO_WuIynlCBTppMPimUp9AbB1gO8xzSRg4mvLwkxsuCEvh7w6n3jNzYPlpM19ldShpLEJfu91zLkHUxcxCrR5BcC33ETNwoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇪🇸
رسانه ESPN برزیل: رئال‌مادرید هیچگونه افزایش مبلغی در پیشنهاد تمدید قرارداد به وینیسیوس ارائه نمی‌دهد و پیشنهاد فعلی همان آخرین پیشنهاد تمدید قرارداد است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102451" target="_blank">📅 19:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102450">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2Yy_ZVH6n-11NVRJSVHpnfqyq_Yt61Jpqkv97RITYyCj2stLcyk96I5nZq-1eUbm7_Sv-fjvE92Oi1caFogHXNwuLklJHMoRUqm9Ep4Ats1YOSF0farZbWY8hxXHpFI5sG3DGesxeTnvkwscMQaVk9xIAjj7NG6EjcM3Xgz3CvkO9QmNrR5K2Aq9w4EHIPYyCTViYXYo4Zkar9kuVIkUm0xEH0Tv4w-CEJIwsbO2-vJsmu8Uru8KCs99sjH3fopuiEM5JFunsP1aa0cfcqhNnXhHAC28uUgk5bcirvmOLPGCqFtq2ENIPwKJ3fIxml5ca7mVE1rsluUaM3FacfjIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🏆
اینفانتینو: جام‌جهانی ۲۰۳۰ بهترین دوره از تاریخ این مسابقات خواهد بود چون در کشور زیبای مراکش برگزار می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/102450" target="_blank">📅 19:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102449">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWG3aEXmEH8wBjStW851quEEfk2RhM7edA2HDtOF3Ejna_mXa29LUQqgLi6n2k0MG8hASQxq0PH1279eqAwfLzEKgeCFaRtjJOqH4LwpXMmSh_mXpa4e39q9grNayG7W-aIF55rlLndyjoEMJELKvykrfn27Hkdm5HpJ8Khco5b5L8lQN5LVQIouSnhMTh_tabbIxI3mskd9PIRXPuXFK2Ma017HBJBihEUwlzSdsAhpfxza8_hHVeKra5xgI9PJVkEbCpSoZwgNzfPaD-DX82BZvi8vtEaM46-hRJqyo8efGJY5m5UnEbNAELVIK6fmmHJc7czTAMvL1LFeUQPxeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوفیس تعدادی از بازیکنای فوتبال
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102449" target="_blank">📅 19:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102448">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1uQ0H4XcZdNgW0nWKtduWIf9XSO8PROQwSX9kLeA8kQswoVK9osF3Q8IzhNfD1m29bZbPEUh6mPXgjuQa1_Yh3S_69qIBd11r7eY6aGWTwNpFzSf1J0YVZQi54I74uLjIrH2996jPKSVgIviLUlkG7zss9FwbCx0pStSo5gE07q9BVtxxfQtHZJXS48dixaWmlTPM0xsEQQYiGo4ddXSg43X-v7wnCz-jdt-RSBpuEZxzCBXNKZvdcZ0QtiZpl8OtawZzVFcC2m-Q6dt7Y1AliheNJua5TPhnlMEFmdE99gGVN3NtC_HjV-0qt-9ca5iIF_p_Z_XQO2gs0czwCVJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
اسپی:
انتقالم به مادرید خیلی یهویی اتفاق افتاد و همه چیز خیلی سریع انجام شد، رویایی بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102448" target="_blank">📅 19:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102444">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SNnf1QLnYSvhpEnNZbp_aUVj3a9MERzzmJE41Q-jp6fXvgE601whzQUIySS5DIBttfoNERixcs_O9Ip_CFWtj_UXLWsW6R17rly847RbWRXdRQ0id_86YXVLfmu9s0QrjxyFmIVKq7QkHX3DrP4z1ehNAQLHxpa23yHHoxdrPB-Bjxl67NaiKVhFFZqErVlEExAvgoHv1ydr3sb67FkmjpCtvQLjG6u2fIlcOUxQAl6YAmhxyS5nMWnYLOg7rfI0h-sYBkshs_s3AGdWtX--L5Bt3_jx_rmOtGaHyIVIagbE2TtKlaDRDj1i-BOu_FML2y50sRReJ6_al6Ao43Mv5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FmwanV68YMpqV9Z9-HPyZsKvZVQs6ELHWJTpnE0NgZJSfKADfZYwjQJH5oQhhz9piHN2GfCuN8dmNZ0Ok7gxPHWQj4QBpGlEoDOAcsVkWg8Qz3n5Cm1SwO4SsEdfMhHTfFsNTZtCuB_GVwAi4HS_OfRgWt3YDwWDgkoqTRXRdC6UYlfG8ru_XaIfLGlyW3BtOasCCVUIzDjvTwL3SQJkkmQu1hD15pEHvqeCJdBulFHAg3tsNyHA4KS5ol_83e7eAFrVgk1XV1B4NS0a5770g_aJLAW0J_Juttyb5mRPvkK3rPZTMl7vVchK-pLFCOAmsSkUro8Wo31ZtDtcYltArw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AC1z58j0ePb5Rg4FaPrlizFrGJSV_pln49_FLD6UxgIdfEn9idWQavn5xWMdkvJ5wuU5vFPzO8AUSbCTfcI2V0sOicBb2Y3Z3sFKSbhf1aUczvM33pyAKQIhZwsdRso-fsJ9ZPbPS8LuqRajFLigRiEUBW9Lgg7q9glKTzhiAio9Wjy2MnU-Hao3RxiV0GJhpeYiC0JhgXHlCNh3dxxCJIBDWZZ_tAvz72wk5m_C3yUPaD2jgV3Q66SOQC-qDp6skeJ-Ym9cfUgkV0r7VtnsHSPmTJbLeO_WnZ81Tw1g66xXirjee5C3WB4ezXn-RC8H2qt7mNKTgzk_SmUDc7c1wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vY3Oe6CPIdqiMlEqeEKN6maHbWT70JTMSiuqmMrHuP71kZJd_Z6wmfwLgpzSy2ASI6dMlpCoNMJYw-SAEvKpgoj4A1dGcuokMFzzspeKpqFNv6Qr_Imd1UzqKGBFb2cMiQpRM1iVeBqhCEnv-lR9QsZL-wWCzjkSPgMqE6ImasrzohR3wvY7A-tGiNppxBKsVd2yKU4ggeXXsbNqvK2D3J_sT_XG0kVVMCIViC2FvCUfrpCd5bk4F1PTu6wjt_2KNGkZZsyL0dCIvAYaZVxbu3btqjnL0KzZLzcaBORyyaCLHcrugiHaZ7PzkEye9JKlathJwytvsX-5B6yHuCkRIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
عشق و حال لامین یامال با دوست دخترش اینس گارسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102444" target="_blank">📅 19:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102443">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4ucFx6pD9-gnu0l0ns-c2SqNEEWve6RAv9ahjBPMw75IAaiwg9zMpoh9kvXEsUud7Eb3JUFG0wwx5h7lfBGmvHOT9w_u43iQTroPMPCHoD4v64lvuXkE24vVDR6DIUBx2W8aA_JUWJB86l1Uv5spRYWuT83JEQzltYTumdv5poINA5RIvmBhr94CIWkRpa9kzf4_hJrBGJz_fuNCra7R-uvZ0CtD_s34e9W6SC98KsSNZ974T6e2BCCg67mBjIEVF6ABZM8rR52KeF01F-2B3Fh8TM0kN3x3fCxdibLQhXTX-En0oKDKIYbZsCWB-IU8k6YLC0-iidVviFy0u70iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی دوستانه مقابل فولاد</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102443" target="_blank">📅 19:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102442">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmpLb02cYcuaeGRZPFV6KEQCGrYSqkAaLzzUi2TjhU5lHrgni7dNMP1sc-po0qlianYDryI6huTK_bajMZEhWuSK1Yl4wocItHampiz9mNVY3KONyF9xRSSLslPVsWgsDJPOU3VlCVTuGeHor0n5s03KDg_eNl7CE-SWT3MqcZDv2kTR3DG7t0l-If0v0EbFwpdBtOXO3aMAlYboaLepmYkmHFREELRGLFegVrUVg6kRY5n5uQR9Rl4q51Cvzc_vuwvCXAMeUG63H8MS_FaruMHorrNOzle8qIWSK1NwaeyhnqtyQGM9q_disQgpcqej2AX0Q0TUMrNnAMyF_uEpSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فوووووری محرومیت دوپینگ میخائیلو مودریک لغو شد و او به زودی به اردوی چلسی در هنگ کنگ ملحق میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102442" target="_blank">📅 18:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102440">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tf_MBrvktTxkZeitRtoeT8qnEOWXOcTs6aOq6vjzGSwmc6pDIE3TEsWQvKhJYAcWNOzLQzVVyCysRn4ztj7yav-USDU1-RbHLfXBR8s4saMKd-olUQKY1AJ0bhE_sSD8oSfZe-UKg0_J4ik30lAYvnf5u3ZIasJKOphWabIf3Gf8rNXxn9PLR5eKmvTpdoJ2DGczUSTmA8CsC3GQhyxk08qfw3Yws7ljw_T3kj-RZGZrcxP0l4HbA4Y9BwLH01FOf9BcdIHPimgjv-hBjlK56qyr20Tq38g0I139HnrYgsHoK3uMZPF6iUXXHZZp-OTGt6M7of87S6WsEy8PKlYdvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WKVhTXX9NGeNGqj-ZVhEqgqAqbafIyy9A8WdtAobdPfJjKeDmtCb9Z3QyHJq7W1Ig5IiRCwW7Jn9MerKD4Rlgq-s33sBERlbuy8z08ALHSQx1ko0NOr22prXt_uCcmihKKNPV9QLWn1vJLwkQ7_h58WmF6LfV27CNddVFObymCdY9SiU7FdrWOS7oNw_bJ4xwpimmvJx8iJ2jLSAZiGpb0vWrr6qfk3eCYOFCHmWjyn5F5jsJLez5LfDrgReYhqpiBuRSiP1ssdn3zmeiwI1yazbUEwTUdv2FUE_3zHPnyZIMQP_-VfOdxyLdaESbSjufBbWeNLD14RFREDADhTiWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیر شدیم و خودمون خبر نداریم..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102440" target="_blank">📅 18:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102439">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5d65b7222.mp4?token=NbVKRlzhM5cL6FPH10PQjjm6-vmj4sPuLLaTmGvUVPooVo7FrFT8aPMnqaWH4rb0aD1VjCT1bfiKsB4W4S-zgN1Wn3-h_tVlVlJ4FCh1U_pPEWKiha87LNRfl_WqQGWaHTJzZTriIN3YeX3jEgzSTBlauJ4aANzQA6BtvD4zo3cLdZlJmMm8ZtaRIWxASGT3EhxC2yPUinmnMf2XqSi30J-F_aqA_ybuh6sohScemmCQT437qCo3P6ZtRZk04rTuLNXSso1ERyQEUnSS2YoC5YIoTW-SO_kJN2SP6hFdS--PTbxJ7AQadkeLZ5YZL9ZXND8Aes0Ii-IvKm9rLlOrLmdj5DGI-VTcrGggN1Msuns7VkQclMSp4WotBnh9GKuVzvd0jIRWx9YBtEOpQEPT5XkfOJzcnE6MfDwtVhypuAV6c_yYTEjmcuosVPSUj6LS5_kPNuK2H9uOZlAka8fKXHQk_2YmZUNxqjLHtxx2xChTsmLF6wdBCnpd903vcP9TVqauCec_4BsWo5U5uycRGwC5i8-GO4N5NjYndGQh_iK0dgGok1lmrQcAxVpCIB5a_qpMIzEiEtXXwCuDNZJQzDxkGBhnqxdMgsjks5bTlfqad1eTlYVtLxIgiP0KGIwQX4eAnkR0gObBdygIWO51Vfz6rsOGlh4_MJoyfHSHuQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5d65b7222.mp4?token=NbVKRlzhM5cL6FPH10PQjjm6-vmj4sPuLLaTmGvUVPooVo7FrFT8aPMnqaWH4rb0aD1VjCT1bfiKsB4W4S-zgN1Wn3-h_tVlVlJ4FCh1U_pPEWKiha87LNRfl_WqQGWaHTJzZTriIN3YeX3jEgzSTBlauJ4aANzQA6BtvD4zo3cLdZlJmMm8ZtaRIWxASGT3EhxC2yPUinmnMf2XqSi30J-F_aqA_ybuh6sohScemmCQT437qCo3P6ZtRZk04rTuLNXSso1ERyQEUnSS2YoC5YIoTW-SO_kJN2SP6hFdS--PTbxJ7AQadkeLZ5YZL9ZXND8Aes0Ii-IvKm9rLlOrLmdj5DGI-VTcrGggN1Msuns7VkQclMSp4WotBnh9GKuVzvd0jIRWx9YBtEOpQEPT5XkfOJzcnE6MfDwtVhypuAV6c_yYTEjmcuosVPSUj6LS5_kPNuK2H9uOZlAka8fKXHQk_2YmZUNxqjLHtxx2xChTsmLF6wdBCnpd903vcP9TVqauCec_4BsWo5U5uycRGwC5i8-GO4N5NjYndGQh_iK0dgGok1lmrQcAxVpCIB5a_qpMIzEiEtXXwCuDNZJQzDxkGBhnqxdMgsjks5bTlfqad1eTlYVtLxIgiP0KGIwQX4eAnkR0gObBdygIWO51Vfz6rsOGlh4_MJoyfHSHuQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
چند تا از شوت های کارلوس رو ببینید، زمانی که فوتبال تا این حد راجب کسب و کار و پول نبود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102439" target="_blank">📅 18:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102438">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d5590fc67.mp4?token=Cc0bY0SPx_YEnFVZIqpgjIx8gMUWuTSx-tZVDt_x-3rLNHMj44NKxFgE4h-B369P12mK--Oh6uEviHk9_0JO9Jc13jfEv155NPV4zHWCIROv02DkfmmDkofOAhBtn6lJmt4o8c8k4jIfG4MRyagJcGhCjCs1zqCow9rIU4GjwMI_LC0FAvLjRShItYQiI1yIEePhEWSwu0i0uMDmKoaghgC53iM940pE2-Z6Hryx80CP2v1DfgbvW2yP6xoRg7yGijvLVOZrT1L1GCP_szkfqQqQaqhRMiXTEtbI1polnzuWE3BJaF5mVRUAWSXFBEm4aOOVIP1bEaF_hCaTWadS_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d5590fc67.mp4?token=Cc0bY0SPx_YEnFVZIqpgjIx8gMUWuTSx-tZVDt_x-3rLNHMj44NKxFgE4h-B369P12mK--Oh6uEviHk9_0JO9Jc13jfEv155NPV4zHWCIROv02DkfmmDkofOAhBtn6lJmt4o8c8k4jIfG4MRyagJcGhCjCs1zqCow9rIU4GjwMI_LC0FAvLjRShItYQiI1yIEePhEWSwu0i0uMDmKoaghgC53iM940pE2-Z6Hryx80CP2v1DfgbvW2yP6xoRg7yGijvLVOZrT1L1GCP_szkfqQqQaqhRMiXTEtbI1polnzuWE3BJaF5mVRUAWSXFBEm4aOOVIP1bEaF_hCaTWadS_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ویدیویی‌از وینیسیوس‌جونیور در سن ۱۶ سالگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/102438" target="_blank">📅 18:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102436">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EY8UxYgUspqRIgKixH7GHrtk1FtRspSwc-gZ_R4UP1RkYdSZQ-AArkZvMiEEfHq7gEUeDX9ya7R0n1bxZVUHNNzWeQOvhT38VtX5iffH-sIDP6r1SqkQq29yoIUvfLiEapMQL6YSh1JyLjBH1PnMTcoTKs-VWHfG0dqPTNWHqvOEhej0nG3exXFUFHbsb9SGPgaVn2wfhvTOrlXjt60FA1XcEYgsjNMOXL6Sn4YWACCbrg2eVdsauStX03yBowqqpanyC4L9crNHylacRP2qutrQLoMrYY8O1RfqksYA50J5bZ8cafF2mWpXzdHWoZ4_ENEPY3ioKoXgal0e68FabA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aaw5KxIamEk39w0CS9OSLLLy2pXe9Lqh-CODVAUNGPL3ej2d36KLMWUupgjQB40o-6Tl6dDHH5JgjBMY8I9KMYo9eJ0ybxnT4R-ZDNFK0NvMmIG1LSnjjB99BN3lxkH0vC1_CRSZFPjgN9rpXJoHUK9ntUlBfZojj187EYHwp3on7t2LsK6RjfrPCTEAGO2H0jHchdSdBflDIS-I_MoN23hKVVRAn5tACWsY8NKx9327tk3v7V_lXc4qHL3nJxP59gXwAeHoMRsv1lyzd8IStShaajpdOevDQY0CNHVPuNh2rtuUee0CP1PFxu5fZHo07sXgUyu7pqmPaqPO8LsXEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔵
فوری، محرومیت سنگین چلسی:
🗣
باشگاه چلسی به مبلغ 10 میلیون پوند جریمه شد.
🗣
همچنین، به طور تعلیقی از ثبت بازیکن جدید در دو دوره نقل و انتقال محروم خواهد شد. به این معنی که اگر بار دیگر خطایی انجام دهد این بار پنجره قطعی بسته خواهد شد.
🗣
در ابتدا 6 امتیاز از مجموع امتیازات چلسی در فصل آینده کسر شد، اما باشگاه درخواست تجدیدنظر داد و این رأی باطل شد.
🗣
این رای بخاطر تخلفات نقل و انتقالاتی در دوره آبراموویچ مالک قبلی باشگاه صادر شده است. مالکان جدید این باشگاه خود این تخلفات را گزارش دادند که باعث تخفیف در حکم نهایی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102436" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102435">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68f9e38a71.mp4?token=lAeadRKJJe6SD5NmGr-z3azhVZJUmO5bFsBbjyJ-busOTcjhUj7HEZdAuIIGwiCxl9GLXyXAT3rMCiyKdeNOO0KfyD1CZ3n8Bxt9J-s83VfciP0ZcZ0h8PFEI5lJrzi-RcyfnDdtHnPTYyj6Ku0f1D950ZQFvdmSa97mRpXzGNjDDdzPM6vsuelx048F7ZDxmexAoC1PaY7Jgm1-eI82fUDfu6g-gWUyVsXhmou6KYyuqTmFIkLoIDkvcePVFNsAR2vo7bej-H89Xlmn9MStU-38skiEjyWfl1Kn3AYnSapePqU0ytWJJyy6H1vdS4diBfnnpSavbnHy4PbIeZFeI6T0QYC2roZMH3tZCemEeOu-h9Vdtpb0AY-KyiYCO0Vn_t8rRW9ExdPNl0KdKJe8hlK1ZV6t4mLZ5jaSEqZ09ZS9QY7UJV6wtJpolLNwhZQOx1zE_p2vQsHe434Ch1bc46lKXZoR1rm9VDdX2kIMHPE3oayqI9XzYPMvFO6A0oUHuMfx_AaBGWCnOmO08Ksz9VZ3HdiJyJ3Iizm3yRNyMKC3-_eJ9jRQiLwfQJLuonHRVJ-uHGHwTsi-7ZG-pkQPhf1MFWJxh3MAUIDGxp6jy39o9k3pQmcFonSRgDVe9IEJZLpt1-9gijM3N2NkW4ECs5X7Z9G8j5Mdx-Kc5MGRWXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68f9e38a71.mp4?token=lAeadRKJJe6SD5NmGr-z3azhVZJUmO5bFsBbjyJ-busOTcjhUj7HEZdAuIIGwiCxl9GLXyXAT3rMCiyKdeNOO0KfyD1CZ3n8Bxt9J-s83VfciP0ZcZ0h8PFEI5lJrzi-RcyfnDdtHnPTYyj6Ku0f1D950ZQFvdmSa97mRpXzGNjDDdzPM6vsuelx048F7ZDxmexAoC1PaY7Jgm1-eI82fUDfu6g-gWUyVsXhmou6KYyuqTmFIkLoIDkvcePVFNsAR2vo7bej-H89Xlmn9MStU-38skiEjyWfl1Kn3AYnSapePqU0ytWJJyy6H1vdS4diBfnnpSavbnHy4PbIeZFeI6T0QYC2roZMH3tZCemEeOu-h9Vdtpb0AY-KyiYCO0Vn_t8rRW9ExdPNl0KdKJe8hlK1ZV6t4mLZ5jaSEqZ09ZS9QY7UJV6wtJpolLNwhZQOx1zE_p2vQsHe434Ch1bc46lKXZoR1rm9VDdX2kIMHPE3oayqI9XzYPMvFO6A0oUHuMfx_AaBGWCnOmO08Ksz9VZ3HdiJyJ3Iizm3yRNyMKC3-_eJ9jRQiLwfQJLuonHRVJ-uHGHwTsi-7ZG-pkQPhf1MFWJxh3MAUIDGxp6jy39o9k3pQmcFonSRgDVe9IEJZLpt1-9gijM3N2NkW4ECs5X7Z9G8j5Mdx-Kc5MGRWXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
درگیری کورتیس‌جونز، سیمیکاس و سوبوسلای بر سر بازوبند کاپیتانی لیورپول در بازی دوستانه اخیر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102435" target="_blank">📅 17:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102433">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vVcGnraVnwF0umEP7n_Xu5_9SjKu5mQunHMhUyKxOH47I69E_t25-ffpHBnKHm0mAyjSoq7mQUCV2eW0kMCSimilh2IBfjJCt0LhvJ-v8BsxapczGCNG62PoGPhocN8nqcpEKhcEYOzeZMV9EXAVyk9uTUcHK605ws-Z4-r2agKbfLti8kqxocS5PT-mecvl1A7PXCqsnWrTt6KI0jcT31LUQFEX3uRQUf2Qm5DbodKIwkvF7UVgUxVzfbaEXTqX6PO6Opl_iUEBKiMQoOxiDzaXUm-gm4KldD9Bw2fqa85Nd2B4vhsMfQQSWi-4us_I1Uq5o4WEhuPZPlR33DiQWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DvCsbUu6KdxKC1voDDdXzm4fq1YIX79DkSOG423V5XGR41Y58QDHYH06zG_6B2l_tGWH4jqC-j8m3LeAfHSYoiZcBCQB8JJfNhMN6thCiylvf7UPr28Wwu68shnbu7fVhgq--wKDv-Ie48euzHxt3IYkLDu7WmjYwt5lIEemgO_H0cZuBt-nNqK62BCd2iPRBKmNTHNWkjypq-b-EmSCuhXjoYuc29Nr36zWMSC6-S4V9feO6QRr3-EoLPHlqZO5Z-l1BLrxSUhpL7tmAjH-0mLZmzctBxuXIWPI_yxMZl9mR3AGhCvS66abl86nZd-yYCA7gSf7biZB_FJWow4jTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
ال اسپانیول:
پرتغال و اسپانیا اعلام کردن اگه اینفانتینو پیشنهاد خصوصی سازی جام جهانی رو پس نگیره از میزبانی جام جهانی 2030 کناره گیری خواهند کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102433" target="_blank">📅 17:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102432">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96363baca3.mp4?token=LXXGl3GPKTcdojIYZ9DANEjRlk1LIZ7Q6BXg9qRcJWZf3yGetSgZ_IleAAGruezA7H9z7W2xkD5dXVGn_1ATAzn67CXnq21HbzU0KmYKKtf3ahFzLKywWm8b6tRICiejh5P3fbXk57_p2NMBdPKPm97oEVvS0eF8jIAvo33K6qZpc6AAFGFBQeDkG-6DAksrRFbAlZhOXupiykNDe07NQnvgYGBtTzBn7y8Wm5cOgUZ3NqyDBgof6u-UVBxFMLBmxKwpWUZ_VM7Bcf5COwoPVnxgSWF1bsR0UeTAHsqt4Vg_ZE6CU2f5ncziyihauhjlKvo5Yab0Im_7fMcSaYyKOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96363baca3.mp4?token=LXXGl3GPKTcdojIYZ9DANEjRlk1LIZ7Q6BXg9qRcJWZf3yGetSgZ_IleAAGruezA7H9z7W2xkD5dXVGn_1ATAzn67CXnq21HbzU0KmYKKtf3ahFzLKywWm8b6tRICiejh5P3fbXk57_p2NMBdPKPm97oEVvS0eF8jIAvo33K6qZpc6AAFGFBQeDkG-6DAksrRFbAlZhOXupiykNDe07NQnvgYGBtTzBn7y8Wm5cOgUZ3NqyDBgof6u-UVBxFMLBmxKwpWUZ_VM7Bcf5COwoPVnxgSWF1bsR0UeTAHsqt4Vg_ZE6CU2f5ncziyihauhjlKvo5Yab0Im_7fMcSaYyKOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
مرزها برای میزبانی از زائران اربعین آماده‌تر از همیشه
🔹
در آستانه اربعین حسینی، پروژه‌های عمرانی و زیرساختی در پایانه‌های مرزی کشور با هدف تسهیل تردد زائران اجرا شده است.
🔹
در مهران ظرفیت خدمات و زیرساخت‌های برق، آب و روشنایی تقویت شده، در شلمچه بازسازی و نوسازی بخش‌های مختلف پایانه انجام گرفته، چذابه با توسعه امکانات رفاهی تجهیز شده، باشماق به سامانه‌های هوشمند مدیریت تردد مجهز شده، تمرچین توسعه زیرساخت‌های خدماتی و ساماندهی محوطه را پشت سر گذاشته و در خسروی نیز سالن‌های مسافری، پارکینگ‌ها و فضاهای خدمت‌رسانی توسعه یافته‌اند.
🔹
همه این اقدامات با یک هدف انجام شده است؛ سفری ایمن‌تر، روان‌تر و آرام‌تر برای زائران اربعین
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/102432" target="_blank">📅 17:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102431">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">💥
🧐
رونالدو، پسرش و جورجینا درحال عشق و حال در گرمای تابستونی اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102431" target="_blank">📅 17:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102430">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e703311f9.mp4?token=uQ0-HLKJUbWGolnZFzgpwYJPccqLOj5TgI1rR0gPtFxPpQ7LcYh7Qt7-HhwT72Zy9CGq87aKsvMaOBxqyQXzE5AIgZpa_3wYvtLvLnlZvLPOuOEYOkPZLvTCynaQkcawo3kLSJtwZj6cUtDigobl8uFJ7Is5i2SEjqcVxr0PF1gr7jcnYpvP8G9H2obI25HO2IRE8T_iPkhJDw79oNubY_yhzOxx4kZxjAT92-RE7H0tVnbwA6WtvMgSK2zOQGzpKTBo9Ix14wfMA-6T7SRUmnCTfrBfi2jg7jzfk6WQuHHA8I9wTNhRQ9WRwNOK81mkqI8ej4AyVYivZ_TRnaS5Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e703311f9.mp4?token=uQ0-HLKJUbWGolnZFzgpwYJPccqLOj5TgI1rR0gPtFxPpQ7LcYh7Qt7-HhwT72Zy9CGq87aKsvMaOBxqyQXzE5AIgZpa_3wYvtLvLnlZvLPOuOEYOkPZLvTCynaQkcawo3kLSJtwZj6cUtDigobl8uFJ7Is5i2SEjqcVxr0PF1gr7jcnYpvP8G9H2obI25HO2IRE8T_iPkhJDw79oNubY_yhzOxx4kZxjAT92-RE7H0tVnbwA6WtvMgSK2zOQGzpKTBo9Ix14wfMA-6T7SRUmnCTfrBfi2jg7jzfk6WQuHHA8I9wTNhRQ9WRwNOK81mkqI8ej4AyVYivZ_TRnaS5Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
🎙
تمجید جالب کاسمیرو از لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102430" target="_blank">📅 17:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102429">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b472a6619e.mp4?token=Yi4MeK36DX8pLzcmQc58zhhsoPN_R356IFGCXeXuAaeAHaRrtRfG26QIiZDv5dXjf8aRNary0luri0PmnToG3lT0XNQYjomg-kP30Wyoc5Ap1AhOnHRFCsg9_IVBWxRQaIKtez5gHD_dwfQJ58wucS4oFD1VMpW2vUnvAVJtwsksCzjoDOwL46hriyQ1D6cOzjKQ2UhY0o_2waP4JfZYq6Ci3i_EmpnqtfNpZQLoo-0xDFzzqNODTL5hjn3KZ52d-M1BwbSpO75HxHjPyDx-I0duTQDxtgzB-x10mH_GJCnjUwIOp84-skoOPIvXpxDlqpg-LVx-G5NSfpu6d1ahPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b472a6619e.mp4?token=Yi4MeK36DX8pLzcmQc58zhhsoPN_R356IFGCXeXuAaeAHaRrtRfG26QIiZDv5dXjf8aRNary0luri0PmnToG3lT0XNQYjomg-kP30Wyoc5Ap1AhOnHRFCsg9_IVBWxRQaIKtez5gHD_dwfQJ58wucS4oFD1VMpW2vUnvAVJtwsksCzjoDOwL46hriyQ1D6cOzjKQ2UhY0o_2waP4JfZYq6Ci3i_EmpnqtfNpZQLoo-0xDFzzqNODTL5hjn3KZ52d-M1BwbSpO75HxHjPyDx-I0duTQDxtgzB-x10mH_GJCnjUwIOp84-skoOPIvXpxDlqpg-LVx-G5NSfpu6d1ahPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
یادی‌کنیم از بازی تاریخی ایران و قطر با گزارش جذاب عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102429" target="_blank">📅 16:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102428">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfd29d0ef7.mp4?token=CamqfwboKy63UfOcjbqGQQvSpb-I5nO2zXhqNaFB5KODOkb6OhCYSaXxfFycyxDH5e_ytwlP2LIs3E6uJxoAK_feS-YIsJLefEy1MeKWnKZd4cEQPJeE07JG5MuSFuyQlwquXrMCD4_vdy9EYacK2SvTySEqpGrhS6r4yMW48o_AuhRi8rIZmQpKWU5g9ueEmbqB0ZCiF6bk1pPnF7WFBtxh_9IJpSVO3MWIA_fdafQ5hqwEnAneQ2YyLbKLqcyQkMBOxqwQlnSy9MKaL50Pqa-sGWVQE-8J_KtCvW0EgjP55nN13MnQcgLL6QmaFVekyAx9tSjfO6dxKu2vjTlLKIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfd29d0ef7.mp4?token=CamqfwboKy63UfOcjbqGQQvSpb-I5nO2zXhqNaFB5KODOkb6OhCYSaXxfFycyxDH5e_ytwlP2LIs3E6uJxoAK_feS-YIsJLefEy1MeKWnKZd4cEQPJeE07JG5MuSFuyQlwquXrMCD4_vdy9EYacK2SvTySEqpGrhS6r4yMW48o_AuhRi8rIZmQpKWU5g9ueEmbqB0ZCiF6bk1pPnF7WFBtxh_9IJpSVO3MWIA_fdafQ5hqwEnAneQ2YyLbKLqcyQkMBOxqwQlnSy9MKaL50Pqa-sGWVQE-8J_KtCvW0EgjP55nN13MnQcgLL6QmaFVekyAx9tSjfO6dxKu2vjTlLKIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیاز بود یه آیتم جدا برا لحظات تاریخی فیروز خان کریمی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102428" target="_blank">📅 16:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102427">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d17c8ef3f2.mp4?token=hr5YrEe50cDDHiPpTYg_tKjguL786gRG84zUq8x8x8Z0hfdLAAzz1c-OZNklH0QIcGixCawlas01YO1Yak-NykkmPHJhXCbgF32uBC9QRGoZ1vVH_p3OEGxqagsD24-HeKL4Eb8cdT94DTb853wCuSj8B4aiUtZedzHSlg4GKI84jkqCaOv7Ny6xXzvLVIj6txE7ZaAkUBz3NvpV4s7zlVXdAA_SCSGQPyUqNDnWTdgilAKTFOmLP2SdKzCg3zo2LLQ4CTJBge_sEnxLAC96I4mA098RCKlhfsmtXk0Q5QRYnP7NIaP1ThAKvcWOk4aaPK3I0beWX-gOSWGnAXApPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d17c8ef3f2.mp4?token=hr5YrEe50cDDHiPpTYg_tKjguL786gRG84zUq8x8x8Z0hfdLAAzz1c-OZNklH0QIcGixCawlas01YO1Yak-NykkmPHJhXCbgF32uBC9QRGoZ1vVH_p3OEGxqagsD24-HeKL4Eb8cdT94DTb853wCuSj8B4aiUtZedzHSlg4GKI84jkqCaOv7Ny6xXzvLVIj6txE7ZaAkUBz3NvpV4s7zlVXdAA_SCSGQPyUqNDnWTdgilAKTFOmLP2SdKzCg3zo2LLQ4CTJBge_sEnxLAC96I4mA098RCKlhfsmtXk0Q5QRYnP7NIaP1ThAKvcWOk4aaPK3I0beWX-gOSWGnAXApPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
▶️
رکورد پرش سه گام جاناتان ادواردز (۱۹۹۵) با ۱۸.۲۹ متر ثبت شد و ۳۰ سال پابرجاست. این دستاورد استثنایی در دو و میدانی تحسین شده است. ادواردز در مصاحبه اخیر بر تکنیک منحصر به فرد و هماهنگی قدرت و تکنیک تأکید کرد. او پیشرفت رشته را با شکستن رکورد توسط نسل جدید ورزشکاران مفید می‌داند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/102427" target="_blank">📅 16:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102426">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/543e2ce52d.mp4?token=h49mXBuWgM_C8CRqDSp_zSiJ8gFuJENCRj5Cbq82LEMGVMWpkfdNriSTdS7JhFrFHAJJ1QFX3O9uu8A6cZcfvwPNS2uGKHu_ZRu-UPhrlClyQ8LFZNd6r75JkSnM6EAa7uXEYOfs3KdCXvUb5FgJvMwnFGJioXqQETQyuULRnGO-EoENPB7NARUo8bV3GNhIKlYwFU1UNYL5UuD-9Vvg38ekFGyOeAsubOh2bDU-jETQCcprITjAPkZRN43I7zOFrOvSPXYpsTp0p4WT0-Yy5rlFVZOkHJpuEO6IHuyaLJe96RI92sYX0kriPL09Kods4F-qGhmizOl6AfejgCN2Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/543e2ce52d.mp4?token=h49mXBuWgM_C8CRqDSp_zSiJ8gFuJENCRj5Cbq82LEMGVMWpkfdNriSTdS7JhFrFHAJJ1QFX3O9uu8A6cZcfvwPNS2uGKHu_ZRu-UPhrlClyQ8LFZNd6r75JkSnM6EAa7uXEYOfs3KdCXvUb5FgJvMwnFGJioXqQETQyuULRnGO-EoENPB7NARUo8bV3GNhIKlYwFU1UNYL5UuD-9Vvg38ekFGyOeAsubOh2bDU-jETQCcprITjAPkZRN43I7zOFrOvSPXYpsTp0p4WT0-Yy5rlFVZOkHJpuEO6IHuyaLJe96RI92sYX0kriPL09Kods4F-qGhmizOl6AfejgCN2Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو کمتر دیده شده از مارادونا و فن‌پرسی
💘
💘
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/102426" target="_blank">📅 15:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102425">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e43f315425.mp4?token=Is3xKOc-645VUkuANEOUbFbXAoWGS_lDxD2WC14bolQTKF6s_CM2mEvkqnvNYpSuZ-ePStYK1ynEcPsbBvjFdYqKy7t2To2pAtLI9qEtIF2o9bJEgUamnrFxDkTuGRKb6EiK3MbXsFJkgAjMnLy60dMgCOK5ErafldoKhnfTllalCXMw12o4tjfRWBjr99QqvmTEDLYiINWcxknWhmwf3nO3kp8BVkH-aC0wl0MdfH57NzZdR3nH10UWqLhrCsU1ZIEKxyMADp5v8zVIcrpBC00PovXXbZJIXWUHe4ZRkJz4-iW39VYTmFdi2-2Pl9s_tQVgKoNwG6xQjUE-JSNKrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e43f315425.mp4?token=Is3xKOc-645VUkuANEOUbFbXAoWGS_lDxD2WC14bolQTKF6s_CM2mEvkqnvNYpSuZ-ePStYK1ynEcPsbBvjFdYqKy7t2To2pAtLI9qEtIF2o9bJEgUamnrFxDkTuGRKb6EiK3MbXsFJkgAjMnLy60dMgCOK5ErafldoKhnfTllalCXMw12o4tjfRWBjr99QqvmTEDLYiINWcxknWhmwf3nO3kp8BVkH-aC0wl0MdfH57NzZdR3nH10UWqLhrCsU1ZIEKxyMADp5v8zVIcrpBC00PovXXbZJIXWUHe4ZRkJz4-iW39VYTmFdi2-2Pl9s_tQVgKoNwG6xQjUE-JSNKrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
⚠️
تجسمی از المپیک اگر تهران برگذار میشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102425" target="_blank">📅 15:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102424">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea1f4ae5ef.mp4?token=r1IHsPWJFEHraRIBXHOeZhfrpP3wiQOX_Cv8XuzwdO7QAvvAy1jjGBJ7B_-_ttxXlAxSBKz_8j_EL2g7XwctrGNLLfU3xfse6Yyg7NgEPwVPFMFQy1T5wfq9XqT-VA815_QCVlFkstJizasppXNM7D0HmTQ9toWXY0rG6xAd5zRfBmsA3BQwqrZCWKqky8zBvcxRY0YWjRHueNhAckrf3Yq48j68kR9SLD_b5pE0Wjt-QQCeoXLiyzJ69ff9EOsybSDjsTOVZOR_V5V89hfJzEwKXEnAjSw_Y7fTnCVGY3spVq2EIaRo1yH0BUrjSVwjFVv-mDXfhI6-GCOQKpSCGmK2zN8Pc1LI_3_ri8LiOU2wyVw_2ncqZxMe_wR-AkoXfTe7Uz0UJ12gh1ujtO2Qh55H2LsKPbmt2C0LCrFhgc0j6ieNcMHSURLcQEZT4jfgQO64TTWv8ornM5v8myEUwbqGcDtW4dwJ5aZyqWp8-wMKhRP9KkRJBJQdy2DlyGR8LcEkdYLFu5YsSEEMo7yDEtkgbofSGAy8FwMLo2sblZT9GsklKaY_21PH3T7U7Q4E3B9fjubRbQJj9jXDqpN1y6BgTAlxczse9YS3ffTaupV0ppoMYJQHKPOYID62JG_PwCmSM2I54LqCainlVGy_wzotUtJbKYNBlyq0WEHPwFU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea1f4ae5ef.mp4?token=r1IHsPWJFEHraRIBXHOeZhfrpP3wiQOX_Cv8XuzwdO7QAvvAy1jjGBJ7B_-_ttxXlAxSBKz_8j_EL2g7XwctrGNLLfU3xfse6Yyg7NgEPwVPFMFQy1T5wfq9XqT-VA815_QCVlFkstJizasppXNM7D0HmTQ9toWXY0rG6xAd5zRfBmsA3BQwqrZCWKqky8zBvcxRY0YWjRHueNhAckrf3Yq48j68kR9SLD_b5pE0Wjt-QQCeoXLiyzJ69ff9EOsybSDjsTOVZOR_V5V89hfJzEwKXEnAjSw_Y7fTnCVGY3spVq2EIaRo1yH0BUrjSVwjFVv-mDXfhI6-GCOQKpSCGmK2zN8Pc1LI_3_ri8LiOU2wyVw_2ncqZxMe_wR-AkoXfTe7Uz0UJ12gh1ujtO2Qh55H2LsKPbmt2C0LCrFhgc0j6ieNcMHSURLcQEZT4jfgQO64TTWv8ornM5v8myEUwbqGcDtW4dwJ5aZyqWp8-wMKhRP9KkRJBJQdy2DlyGR8LcEkdYLFu5YsSEEMo7yDEtkgbofSGAy8FwMLo2sblZT9GsklKaY_21PH3T7U7Q4E3B9fjubRbQJj9jXDqpN1y6BgTAlxczse9YS3ffTaupV0ppoMYJQHKPOYID62JG_PwCmSM2I54LqCainlVGy_wzotUtJbKYNBlyq0WEHPwFU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🔥
👀
۵ گل زیبا و برتر اولیویر ژیرو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102424" target="_blank">📅 15:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102423">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a3bfea056.mp4?token=fp9pOor35taP_bqn6ZZCTpdm_s1geMA_HKu54lF3F5VRwPzVW2WwSm_wVCywX-XXcuaIMHsKkNJ3tmZFQcO1L6g5_9XHePE8hTyUOhIvsO8dfWNrMgF4HjAKzfVWe5UfjkWMaOtqEbeEhqjWsz8IQ7DUsrHo7iCZFCsS7CHSu9XpnTyhsOVYCGQThNanRaBSvCFMAGWUy1NBnB-3GInX8iHr5f5NoW6FV6SbwHJ-rAmAjQ9plnkxlsRDRVN5wNF4_GTVLesqn4Q5sHKThYYApkGC3Mk7TIQKYpLvMtf8l9J7fypru6t4WgVUI3HaO6PGuQ0Exwo7XCGhKdbezyaoyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a3bfea056.mp4?token=fp9pOor35taP_bqn6ZZCTpdm_s1geMA_HKu54lF3F5VRwPzVW2WwSm_wVCywX-XXcuaIMHsKkNJ3tmZFQcO1L6g5_9XHePE8hTyUOhIvsO8dfWNrMgF4HjAKzfVWe5UfjkWMaOtqEbeEhqjWsz8IQ7DUsrHo7iCZFCsS7CHSu9XpnTyhsOVYCGQThNanRaBSvCFMAGWUy1NBnB-3GInX8iHr5f5NoW6FV6SbwHJ-rAmAjQ9plnkxlsRDRVN5wNF4_GTVLesqn4Q5sHKThYYApkGC3Mk7TIQKYpLvMtf8l9J7fypru6t4WgVUI3HaO6PGuQ0Exwo7XCGhKdbezyaoyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
سه دقیقه با لیونل مسی ورژن 2014/15
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102423" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102422">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kefrgUF4Z0KvjIWz6jNJg2PXSyw4B8xLX7ztYrZLatk5OgvXaWNMMJirdxhpP5Z1pzct7DskGiFcFOTozA8qb93CYflvtdUGLizv2pmZiI6ZaTHRB4izS7ThRJ0XHsyxt6gXGXoiQb5nbuTQ4-6nczdNGJ6DdrcUNn9io5adayv0mcsTJHqo3TnEom5Q9P1klg01L1N_Q_dfYOVEoxrGmkAKSul9pzi5dj6XrO0Zkid8mzroIluX9od_oF08HPQyygWpaF3jek3DcLaCLrW6xs53PjZjvytvc1ktCcEDf6g8hUzIAmQ3u_6NsW9iOM_MX_kX7h0REZWz78OrpzlJqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
لیست رئال‌مادرید برای بازی با فیورنتینا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102422" target="_blank">📅 14:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102421">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjVW_R3p647l85OdSlsGI6vHX6qbhqZopuzqBohfDF9TBAzrDvvAXCbl5Fd9-AFianzJ7AMMXXzLXKQVN-SPo81XGNLsQgQs5gCOAI2gaxbVXP5ZWD7jU_G0gP-NyQlGeQfB3aidk8AbR3ez9phHt8P6tmek8aiYUQJrNLtiXbokxeREZTRYdv9QQ43p14ofhjhS_cNEGIgQyjL_rSXwnokrpJXHBvTa4ViCLG7SUXkz7hfiaZiKd1Zyo9cKoHYD3l1SPozpmO2l7W-fW_9mmJa8GV5C2YZBqCT9eaI2wCbahro68zVfeZVNh72_ddbOEpV4EpwxcSXvC2UIM2Zxzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
#فوووووری
از نشریه اکیپ فرانسه: آرسنال با نیوکاسل بر سر انتقال برونو گیمارش به مبلغ ۹۰ میلیون یورو به توافق‌نهایی دست یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102421" target="_blank">📅 14:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102420">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/529b07ca6f.mp4?token=HV9_s2BOwzTV36NAQyXakf6J9I_gqjMFA46MG-8CMyaNPsZE65E55VPmvIOvT6NoNI4bI2o28evxTQGbeW31s37pfzGxxASc0VGBAL31wSxUeKrk1zrdA2TDLRQZTzpzZBrsIin2R9niWkcoR9CP2DMR-LNSZac-Vei7gS7B3k-PrTvKqfYDAGjrwvFMEFRtKbkTpgT7XSKfZfVP0DaNC33xp-xBGRrlZ_X7DygQKXz-O2vow0-tQytunZuyme1LUlmhKFn4iAOY6zGUNiXr1DWP6A_Abnls6eypbLv0FGEgv93gGnv7NewXF-ZNIjDqjm4VEVSw0Z1zJRuhDw60KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/529b07ca6f.mp4?token=HV9_s2BOwzTV36NAQyXakf6J9I_gqjMFA46MG-8CMyaNPsZE65E55VPmvIOvT6NoNI4bI2o28evxTQGbeW31s37pfzGxxASc0VGBAL31wSxUeKrk1zrdA2TDLRQZTzpzZBrsIin2R9niWkcoR9CP2DMR-LNSZac-Vei7gS7B3k-PrTvKqfYDAGjrwvFMEFRtKbkTpgT7XSKfZfVP0DaNC33xp-xBGRrlZ_X7DygQKXz-O2vow0-tQytunZuyme1LUlmhKFn4iAOY6zGUNiXr1DWP6A_Abnls6eypbLv0FGEgv93gGnv7NewXF-ZNIjDqjm4VEVSw0Z1zJRuhDw60KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
✅
یوسفی: زمین و تماشاگر که ندارید، لیگ را پلی استیشنی برگزار کنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102420" target="_blank">📅 14:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102419">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9889076a09.mp4?token=gnvG4P9KumwqNyMG0mwcwNRbtgxUX92EHGmHEnS_pfLyrCPTSgiqTPRLtF8vibzQfHuNKw5eMarnqTC9hz2dPAj2Fgc7Ny4AXYNHW4eHw41JIps3LmVyB8Kkjvww6jq_ujmGmmz9-VsKe4tDRRLtyuZaOmB4JLxTcqfwPeEuBB2_zrl1eNmUWUNMTHRL_ZQUQ6lDGqGncFn5sVmwFCSxQMAEC8iEJQ40hHblvxAK3CmWXK0xGqr73jCJtDzwW5d7kqsEVYW6Z0kJn0Uv14CmOvk0IEewtD-upNEwXbPIMByVOAR2gZSz9g0mV9yAcJmh8lxxfdtPMZqmiabsJ_NT_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9889076a09.mp4?token=gnvG4P9KumwqNyMG0mwcwNRbtgxUX92EHGmHEnS_pfLyrCPTSgiqTPRLtF8vibzQfHuNKw5eMarnqTC9hz2dPAj2Fgc7Ny4AXYNHW4eHw41JIps3LmVyB8Kkjvww6jq_ujmGmmz9-VsKe4tDRRLtyuZaOmB4JLxTcqfwPeEuBB2_zrl1eNmUWUNMTHRL_ZQUQ6lDGqGncFn5sVmwFCSxQMAEC8iEJQ40hHblvxAK3CmWXK0xGqr73jCJtDzwW5d7kqsEVYW6Z0kJn0Uv14CmOvk0IEewtD-upNEwXbPIMByVOAR2gZSz9g0mV9yAcJmh8lxxfdtPMZqmiabsJ_NT_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
💥
روزی که پیتر چک آماده ترین گلر آن دوران فوتبال میخکوب شد و این اثر هنری شاعر رو تماشا کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102419" target="_blank">📅 13:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102418">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROMON5viC0x17PwAUEjXtzK_QJ6t5zsVKyfM3LAe1FJJqnqPyvRocN6J56aRn0hb2Po-EBjJq9g2m3PgYiroT1QRefx2hzZityztNaquhBqmM8J-1Y2HKphsg6rOX1tsMTMt5HrF0ChzwcNrRYa4Vr3Cod4qABZVSZwTYYeagPzX7clfK9cpgPVCRsxtwN9W1KqUTyYEjX4XUN_SF6BAdCsdx7NkArdmzgbO8bYEZbBjGVPkiHNZnqi8JW1AijxxhqgCJsuE0vadY0-S5xShnwL-GMS4uwUFNiu8DvJ46SjeaH0bEU1JiqxDNYr_Z_YiHQiQJFGo-xbPiPqqPKKU0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
کارلوس اسپی تو تمرینات رئال مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102418" target="_blank">📅 13:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102417">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kl9N1WwU6NIziUHvFk_stCeShTAlEoCFSYgggAyWHJJnGqM5abhAEuyJNy8Iytcw4wmvzisfL2TrZeo8beIQ8ZFzcyC6SRUmPUr50ZnzNBD-Tw_MjjJ807hp3eVGjkyPhkjkJ4Y-t8bPLJ9CGgUYu6L9vzdr6mTwDJ6HTbYGMGCqnM8AHycmXpK9mNkr-kMv6l4OgfN1M0VZzO8GTLLser9IGpRRpNSLMMci7aPhXIWu6zXnIGStIBPnXzN5LnvyCL05XH1MLyDBrOpy1RgAf669eGKRRq_EKkqWpGswfLiMMG-LnDiQ-jqCNktIebS9KBrsR7l8zHKs2NC31wiLzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
روزنامه اسپورت: دو باشگاه آرسنال و تاتنهام به رقابت برای جذب فران‌تورس پیوستند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102417" target="_blank">📅 13:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102416">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4938ae1d8.mp4?token=trU6qUEkwDKndPrpe-I-dZuzNau9m6oChwUePos9uY8e2TtcMH-QaH0vOA6NsnX4TZag4sdfyEBfhFDaQdex2O8TKYQ0Ihs5wlr2u-6e5r9eZDSRJQ5-wsGH8aOCwq7VdUwrKVB8_zrDFhVTHJF4i021L69lYMpM2YxrZMpQGQyyVvNNSJeyq_1yw7PmVHFqD4eJlnwdvEJHfcKYNAjBihS2KnldHM2eacx6S0PoyoA_7A-p2guuHxzoHHwq4d58cmU_7zBreBAR8GN0dzNetiCjVTjUdRimlSg51hV854qb6h4R8VGV9uhud2Qi7Wxx3nfGsDTjrKUZXGVC9gCIIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4938ae1d8.mp4?token=trU6qUEkwDKndPrpe-I-dZuzNau9m6oChwUePos9uY8e2TtcMH-QaH0vOA6NsnX4TZag4sdfyEBfhFDaQdex2O8TKYQ0Ihs5wlr2u-6e5r9eZDSRJQ5-wsGH8aOCwq7VdUwrKVB8_zrDFhVTHJF4i021L69lYMpM2YxrZMpQGQyyVvNNSJeyq_1yw7PmVHFqD4eJlnwdvEJHfcKYNAjBihS2KnldHM2eacx6S0PoyoA_7A-p2guuHxzoHHwq4d58cmU_7zBreBAR8GN0dzNetiCjVTjUdRimlSg51hV854qb6h4R8VGV9uhud2Qi7Wxx3nfGsDTjrKUZXGVC9gCIIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های بامزه رونالدو از ارتباط صمیمی با پسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102416" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102415">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5029f55db8.mp4?token=Hp9lg_Wa7bIKjGRErhd_GKnrtZ00sWEZxtfnc_7dbeLzXyqbl5z9GQ7pIdp6CJXkkaANjo8Gvhxi15x90E0KuENjBv3ojYo9gB6s2PJ8uxVPmzjqokBgodfV9U_KnMmmxRUenoUFhvTxajDTLipRuWeNemBul3M9qzmNPT5xLKhhSuqo2J1pIEgqn_l_IiPi3QjmFXkZ6-WwCZ5K8yvyiDyIKZy70xDsSDR7sFpz-IGyMvqzVGFRAMXfT5pgkttCwri629KT1E97Mh3mm1p_tlWtF9QD2v3xjeoIG6oxCbTfgtDkk6KJi-IxQvFZDUuEaNNsZkHzeEQgi2kWaJEXFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5029f55db8.mp4?token=Hp9lg_Wa7bIKjGRErhd_GKnrtZ00sWEZxtfnc_7dbeLzXyqbl5z9GQ7pIdp6CJXkkaANjo8Gvhxi15x90E0KuENjBv3ojYo9gB6s2PJ8uxVPmzjqokBgodfV9U_KnMmmxRUenoUFhvTxajDTLipRuWeNemBul3M9qzmNPT5xLKhhSuqo2J1pIEgqn_l_IiPi3QjmFXkZ6-WwCZ5K8yvyiDyIKZy70xDsSDR7sFpz-IGyMvqzVGFRAMXfT5pgkttCwri629KT1E97Mh3mm1p_tlWtF9QD2v3xjeoIG6oxCbTfgtDkk6KJi-IxQvFZDUuEaNNsZkHzeEQgi2kWaJEXFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🔵
درخواست کودکان جنوبی کشور در وضعیت جنگی از رامین‌رضاییان بازیکن استقلال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102415" target="_blank">📅 13:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102414">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac78119da.mp4?token=t4kAO6ly5e-ZvUl3s_W98UZFjn4n5B4w5FRSjaL86EiHrOGnDm71WuykkWA0bMZmDFrYauU5oaNwitXrzdCEz_aCZnoDMEwdcIO6DVNFXz5j0JHrVwCcLxfoDE0wc8Lh_HO0HRzkB6HkOFXu3bzryPY1If-YPM5_FinksFjY0sCl461its6hCFSNea0qq9KlNyriixlYph0swoGwkTxBdh2UF1W_nolryZ6NZWbafH9RU3873RFIFk26WmGz_6YaaGpVXDDEB3Sh1VHvwoD4mY9upzkIv97pBqHkK-TCyyL19T3RpYUr_4jtGNZ8LXXtcFMWPTm_QPotHm4eYHtiRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac78119da.mp4?token=t4kAO6ly5e-ZvUl3s_W98UZFjn4n5B4w5FRSjaL86EiHrOGnDm71WuykkWA0bMZmDFrYauU5oaNwitXrzdCEz_aCZnoDMEwdcIO6DVNFXz5j0JHrVwCcLxfoDE0wc8Lh_HO0HRzkB6HkOFXu3bzryPY1If-YPM5_FinksFjY0sCl461its6hCFSNea0qq9KlNyriixlYph0swoGwkTxBdh2UF1W_nolryZ6NZWbafH9RU3873RFIFk26WmGz_6YaaGpVXDDEB3Sh1VHvwoD4mY9upzkIv97pBqHkK-TCyyL19T3RpYUr_4jtGNZ8LXXtcFMWPTm_QPotHm4eYHtiRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
نصیحت اسطوره‌رونالدو به امباپه
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102414" target="_blank">📅 12:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102413">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🤩
#فوووووری فابریزیو رومانو: آلن هالیلوویچ استعداد برباد رفته بارسلونا در آستانه امضای قرارداد با پرسپولیس قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102413" target="_blank">📅 12:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102412">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75b732a95e.mp4?token=Mv_E0dLcDLbvUXISs9rTcoUMx8wYSZkfjxCe-97MQ9WCW6tROh5sE6L2uvV-lm_LEP2xCJfOFmLSUlyg-RO8zhkym6gDplKv3veG0I4_TXlhGtDVLagdjXdLwVUHSv_954xyP-0C5XeZEg59WNtqzbXVMjEy1kuXYaM2pExEUr6hEE69NHLFSUhBbedCQoiXScfMhn3xnR7qgiNG1wUFfKZL1qTrd-IR27xI9jQw92C7x8ighsHg5Rp5DyZl5oatv5RpwnS2qM6P2HriDsGVF2k0YlAYaT6rXPVCtf2xoE7QmNupZMVG-QhjWELTh08G8Xyvb19pM-OKRF4cfSekbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75b732a95e.mp4?token=Mv_E0dLcDLbvUXISs9rTcoUMx8wYSZkfjxCe-97MQ9WCW6tROh5sE6L2uvV-lm_LEP2xCJfOFmLSUlyg-RO8zhkym6gDplKv3veG0I4_TXlhGtDVLagdjXdLwVUHSv_954xyP-0C5XeZEg59WNtqzbXVMjEy1kuXYaM2pExEUr6hEE69NHLFSUhBbedCQoiXScfMhn3xnR7qgiNG1wUFfKZL1qTrd-IR27xI9jQw92C7x8ighsHg5Rp5DyZl5oatv5RpwnS2qM6P2HriDsGVF2k0YlAYaT6rXPVCtf2xoE7QmNupZMVG-QhjWELTh08G8Xyvb19pM-OKRF4cfSekbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇧🇷
آنچلوتی: "در هایدریشن بریک نیمه دوم بازی جلو نروژ اشتباه کردم تیم رو تغییر دادم که باعث شد کنترل بازی از دستمون در بره و ببازیم..."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102412" target="_blank">📅 12:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102411">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2964e2f72d.mp4?token=pFNG2bAatYRkV6sWzy0bqMZ8s9HK_Eogk34d6aQdXt6dkyJdUub-0OJ4J0WahZ_pkVWE9NbGmFh4mrbauyI-Su8tsG5ZSwPMlOJ-DlWKdiMjB9XQtlXQk1NGN8rL_2TOeyFC3hT6oczNhLOeXqEfRufehZNs_HFaMdVVmD4p5GUsJzcEPWEa6W0zWluaK4tguW8Qh-UEh2vktrmu67BBsNr312V1dERYWfr8EWTdYj8Ll5c6hKCpFPQ9BBMBSb-dFrXAntD6BiXAj6xIMYm1uULOHRArasef0v-5aAyM0sNETTcrKzVNAX6j9FrdhSeOvU-wmjxs_2fDbtfitdDikQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2964e2f72d.mp4?token=pFNG2bAatYRkV6sWzy0bqMZ8s9HK_Eogk34d6aQdXt6dkyJdUub-0OJ4J0WahZ_pkVWE9NbGmFh4mrbauyI-Su8tsG5ZSwPMlOJ-DlWKdiMjB9XQtlXQk1NGN8rL_2TOeyFC3hT6oczNhLOeXqEfRufehZNs_HFaMdVVmD4p5GUsJzcEPWEa6W0zWluaK4tguW8Qh-UEh2vktrmu67BBsNr312V1dERYWfr8EWTdYj8Ll5c6hKCpFPQ9BBMBSb-dFrXAntD6BiXAj6xIMYm1uULOHRArasef0v-5aAyM0sNETTcrKzVNAX6j9FrdhSeOvU-wmjxs_2fDbtfitdDikQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
جواد موگویی که اخیرا در گفتگو با عراقچی یه سری اطلاعات حساس تهران رو داده بود، این سری اطلاعات مسکونی مقامات نظامی و ... هم افشا کرد
😳
😳
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102411" target="_blank">📅 12:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102410">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b5a4f433a.mp4?token=vAE2fLyiSHiJ_ph1SvDLHBhl7krCpXrAP1pv3ler8Y3DIUNM_cCpCyV2985vUPNr6cfSeR_7r1EN5vJDN650gx-hv2OM2-Y528o_cenuPDW3v_eSFVp7b0McPt1aDP4jJManEgyUDZE2sAsLNNZBhKQxAouc6LeZu9Xkf5CQlEYz28--wpRhQtbwDfQhibNpe2HC5W0T8cItgGJH-5o-m-9dGWf0VcFgaWP3SGasV6LPIizthIAukBEAb_o8tZAOZLUhL2PRuz9o0IqnG2fB86mx7PMZdUSn1Ih2hL0bbGTu-BDG3ljPZJ8OqELgB6maUyNRSDGiXLAP0OPapa5CYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b5a4f433a.mp4?token=vAE2fLyiSHiJ_ph1SvDLHBhl7krCpXrAP1pv3ler8Y3DIUNM_cCpCyV2985vUPNr6cfSeR_7r1EN5vJDN650gx-hv2OM2-Y528o_cenuPDW3v_eSFVp7b0McPt1aDP4jJManEgyUDZE2sAsLNNZBhKQxAouc6LeZu9Xkf5CQlEYz28--wpRhQtbwDfQhibNpe2HC5W0T8cItgGJH-5o-m-9dGWf0VcFgaWP3SGasV6LPIizthIAukBEAb_o8tZAOZLUhL2PRuz9o0IqnG2fB86mx7PMZdUSn1Ih2hL0bbGTu-BDG3ljPZJ8OqELgB6maUyNRSDGiXLAP0OPapa5CYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
🔴
‼️
علیرضا بابایی مدیرعامل چادرملو: تورنمنت سه جانبه به دلیل کمک به پرسپولیس برگزار شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102410" target="_blank">📅 12:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102409">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c746b16b5a.mp4?token=RzCkqd1wndnwMQgUAB0b7tNjMm1N0Z-jLV6ij4NsvAWp4EKK3xcnLtHzj4iR6q80hxWwmbXKyXPux0We230jTzkej0muGtN0wenNU9T57Yns3vmcNWPbcWnfabHA2HSdWjeIYPE-x4XnawTfkgh8WQ9mtBejIBWa0UUb1KcLeQQfyTngoCqmrYzEo_uXquvDW7WmQjTDTDQHsfcwrei3TxjAyZ6GHEmpa3kXtYNMJjPUFv_EOThasMwhvPg52C1amhl95cfof7bbCEWYauRD0SQ8d71Y27Dt0Fg1Pu959gu-mOo80IusxhJ57-BYouEb_JVqTBs0eLoIsLmGze9dALT0-qEZAR3r5zhaj77Sr2GEKe1o1JNVwPTsGPYEewXUU9iZeCziDQSKq78UsI9zj4Sye5piFS6BHIFVbJRvF-734L7zafWWyLyFRCJkYuOz2IMxuM52Ck5nkuJ23MMzy6WyeTRwTmhCfpD6cBW7lHmFYGDKKkPqd3v-rte6xjV3x3QaaVqgYCcNJ8iOCpmYPBvbJs-C1WAsyQhs2opxGoB_SqYUouk8xB_7Rv4N74-vHTYPl_hTf5OcLRSljR3maYrJCfki8lPylO803RfoUIJ3VaeFwl2mIkDC3Z6nkYNISkEv1U0CMfD9gljEE47p8KoehAlncugFk0g96nouiHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c746b16b5a.mp4?token=RzCkqd1wndnwMQgUAB0b7tNjMm1N0Z-jLV6ij4NsvAWp4EKK3xcnLtHzj4iR6q80hxWwmbXKyXPux0We230jTzkej0muGtN0wenNU9T57Yns3vmcNWPbcWnfabHA2HSdWjeIYPE-x4XnawTfkgh8WQ9mtBejIBWa0UUb1KcLeQQfyTngoCqmrYzEo_uXquvDW7WmQjTDTDQHsfcwrei3TxjAyZ6GHEmpa3kXtYNMJjPUFv_EOThasMwhvPg52C1amhl95cfof7bbCEWYauRD0SQ8d71Y27Dt0Fg1Pu959gu-mOo80IusxhJ57-BYouEb_JVqTBs0eLoIsLmGze9dALT0-qEZAR3r5zhaj77Sr2GEKe1o1JNVwPTsGPYEewXUU9iZeCziDQSKq78UsI9zj4Sye5piFS6BHIFVbJRvF-734L7zafWWyLyFRCJkYuOz2IMxuM52Ck5nkuJ23MMzy6WyeTRwTmhCfpD6cBW7lHmFYGDKKkPqd3v-rte6xjV3x3QaaVqgYCcNJ8iOCpmYPBvbJs-C1WAsyQhs2opxGoB_SqYUouk8xB_7Rv4N74-vHTYPl_hTf5OcLRSljR3maYrJCfki8lPylO803RfoUIJ3VaeFwl2mIkDC3Z6nkYNISkEv1U0CMfD9gljEE47p8KoehAlncugFk0g96nouiHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔵
علیرضا بابایی مدیرعامل چادرملو: بازیکنان را از پای دیگ نذری آوردیم و با خواست خدا پرسپولیس را شکست دادیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102409" target="_blank">📅 12:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102408">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1b81246b4.mp4?token=rvMqFiD5rA1_ZODoyY0iQBzXrC0qeu9u8cs1J1WkNl7wzR5KWui04UBHMis9Ns-O0YViaf3G5MIB6AdPxmtB3DOUZ_9YDTln5miHDVCrWeAxt0wGjt3PruoVWAxSTaMzcfxcq_MWMi8YGk53VedWcOPLuouDH-sZtIa_13-LtAMA0roOz0c9ITSL3l8OxSl684NZma2j9hpAv7l16bLqBPh4gPMf7bUcZLCJ3AtWsdWXXWDvN0vedvGslIZwmkEYM6mw3kkTfeiROj19SjdUtFlfXCekRmJ2a1s4Tn_OPM1knMSmS0yp2waVrW6zl1Y-PVYDcnrN9z8VKymjuk_B8Ug5Ij7Ye7UztdV08o7UN_dsz4InLrSb2pGF1-bX8sOqX2k7kBoWnxLAiNvy1lenQO46RWksQAUpXXtiqBFbdo5P3lpBoJfXxgDCmnrOZLnxy375Ioy5fhFDIBZ7vo1aLPJQ9z-vKn-IR7gJixUOZK5gVSncEFwFLZp0oG9GCVHi086WHQGmR5UOvGDj4YihFPH6Bo7AKvw43kRxdFqRzsi8bFKsTHf3ixhpNl1JyYvn3m-bHG2etTa7yNY1CYimcTtLUSErbm0DbNExenBnab17mzp9WPn_geFJmtp9RzM-bVoXpT_tl_W6YZ-xbdEKBcMK1jmlNK4Xif6cO0g89-I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1b81246b4.mp4?token=rvMqFiD5rA1_ZODoyY0iQBzXrC0qeu9u8cs1J1WkNl7wzR5KWui04UBHMis9Ns-O0YViaf3G5MIB6AdPxmtB3DOUZ_9YDTln5miHDVCrWeAxt0wGjt3PruoVWAxSTaMzcfxcq_MWMi8YGk53VedWcOPLuouDH-sZtIa_13-LtAMA0roOz0c9ITSL3l8OxSl684NZma2j9hpAv7l16bLqBPh4gPMf7bUcZLCJ3AtWsdWXXWDvN0vedvGslIZwmkEYM6mw3kkTfeiROj19SjdUtFlfXCekRmJ2a1s4Tn_OPM1knMSmS0yp2waVrW6zl1Y-PVYDcnrN9z8VKymjuk_B8Ug5Ij7Ye7UztdV08o7UN_dsz4InLrSb2pGF1-bX8sOqX2k7kBoWnxLAiNvy1lenQO46RWksQAUpXXtiqBFbdo5P3lpBoJfXxgDCmnrOZLnxy375Ioy5fhFDIBZ7vo1aLPJQ9z-vKn-IR7gJixUOZK5gVSncEFwFLZp0oG9GCVHi086WHQGmR5UOvGDj4YihFPH6Bo7AKvw43kRxdFqRzsi8bFKsTHf3ixhpNl1JyYvn3m-bHG2etTa7yNY1CYimcTtLUSErbm0DbNExenBnab17mzp9WPn_geFJmtp9RzM-bVoXpT_tl_W6YZ-xbdEKBcMK1jmlNK4Xif6cO0g89-I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇪🇸
مشکل ایمنی ورزشگاه‌ها به لالیگا هم رسیده‌ و تیم رایووایه‌کانو نمیتونه از استادیوم خانگی خودش در فصل‌آینده استفاده کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102408" target="_blank">📅 12:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102407">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47a01fbf75.mp4?token=e8H5B1tHqu_33SFTgtrcIJy2o3oAgRA5RwWU5X9bX9mRKkrHT-cIMhakwFZN1eFtlAL0Q9W_IiipT1MvHb-fWl8kzylJYljwRBLlMFZCb9JgI_q-UZrKr-xsGEwoBDkxVO2EawFJbWzmgwEpuqi6JWCFwXY0bHzZ7EzJP5k18u6bYIoTSiLE0o10oN8jF4Vm_EEAMIhkoM01ItdDQc7NjP54U6jaoOnaF-Ru1MuduPhLZpUQm1V318jmaJO9kOrUTqSJYMX7YB0mXhLpdsWKYcVQaN6ISKAp4eg58wfkG0xs-rE8gF-uBUDEK_ahD3ES2nmsbh8zEmWYcaptWhwNhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47a01fbf75.mp4?token=e8H5B1tHqu_33SFTgtrcIJy2o3oAgRA5RwWU5X9bX9mRKkrHT-cIMhakwFZN1eFtlAL0Q9W_IiipT1MvHb-fWl8kzylJYljwRBLlMFZCb9JgI_q-UZrKr-xsGEwoBDkxVO2EawFJbWzmgwEpuqi6JWCFwXY0bHzZ7EzJP5k18u6bYIoTSiLE0o10oN8jF4Vm_EEAMIhkoM01ItdDQc7NjP54U6jaoOnaF-Ru1MuduPhLZpUQm1V318jmaJO9kOrUTqSJYMX7YB0mXhLpdsWKYcVQaN6ISKAp4eg58wfkG0xs-rE8gF-uBUDEK_ahD3ES2nmsbh8zEmWYcaptWhwNhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ویدیو وایرال شده از صحبت‌های تلخ و بامزه یک ایرانی حین ورود به‌تونلی در بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102407" target="_blank">📅 11:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102406">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262957043c.mp4?token=siKfVexFrPJtw2110hiU4q7iUju04MlngDMlSqAM3mYcdf_tPqHz1TlBEmR7uabwtnibtIgm9ZbShw6voQQdGVlICw5tH16Siea4N6A0oYtoY8lAMCazGCt7L9G4IM_YHuCgleFxoqXbT9WbsbTZlCqY_bxJNnDjNwBvNF8Ey8DjyHJd5YGQ3UYETK1TU_2VoAkBJ8RBh0qz-5TjbNAXk3uLRFbmJv39XsKIh5JeHr6GajzSu4awr50KLZSyrQoh_d2yxIEy-u2ys1AycGZpb3vPkJ51z7d6-7OiC2qShpGHVLx0IE5PVzHhJMKfQQThuDFHok9lyABzQU8oVZaoNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262957043c.mp4?token=siKfVexFrPJtw2110hiU4q7iUju04MlngDMlSqAM3mYcdf_tPqHz1TlBEmR7uabwtnibtIgm9ZbShw6voQQdGVlICw5tH16Siea4N6A0oYtoY8lAMCazGCt7L9G4IM_YHuCgleFxoqXbT9WbsbTZlCqY_bxJNnDjNwBvNF8Ey8DjyHJd5YGQ3UYETK1TU_2VoAkBJ8RBh0qz-5TjbNAXk3uLRFbmJv39XsKIh5JeHr6GajzSu4awr50KLZSyrQoh_d2yxIEy-u2ys1AycGZpb3vPkJ51z7d6-7OiC2qShpGHVLx0IE5PVzHhJMKfQQThuDFHok9lyABzQU8oVZaoNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
سوپرایز خاص‌ ژابی‌آلونسو برای فصل‌آینده؛ رونمایی از ستاره ۱۷ ساله قزاقستانی چلسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102406" target="_blank">📅 11:20 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
