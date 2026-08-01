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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 19:05:43</div>
<hr>

<div class="tg-post" id="msg-102522">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFzJwqHhULAWRh4mjkvDg-mSh8MZ5CBQVM4ZuC7ZXAqMM4waIbq5heXz4ZCS5_yxzy1tjmqb8Hji9lM9yOVadbYZAltbD84z_7CeV--3EUDQ-jVUsiWGJXfxBVnnYVqtamQro03-r8ZAagzCRSxn2VAo91E1Kp-AedJlOkm5JsjWXtH4FJE1jPZayj5eWUESHEKEpmPQvvq-pDTMy4KI_ojeRtnDSchjZjRly9AU2vvfIWODFWF59xcHFufHFetmj7sg1lvmo7hdc8JUJNuaglaT1lGd0H3p0WWdiSoBbNdvcSMwk6OLt32Ll8HawAbMmmXuGZ1MWPOHiarodDleBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
🔺
انتقال های رئال مادرید به آرسنال.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/Futball180TV/102522" target="_blank">📅 18:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102521">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aK3mt4c64I8ukYlsSRD0ghwoS5vi2dQtRPTmeoA1x1sVuJHDbqezeR0bYsq72FXhMiIYcIqo4wJrzLg70ibny0xXo-QKdOntZHQzTuXKzvOPKecHn9q9WaJHva1DcMQc4VDHwctheG7s1tIKSjsSCuGZxHqJskIcZWi-ys_3__B750lS5k-l-a8z_HjpEScw6h7OByq40zVac8VH8EgMDh9yLiIGIcXCsmZTJUzSvIeGg46r8WWAB-bnGkjzMk9PvzWfW9YHWTKIh1IRzetJSaW-AeboA4no0Q-LeAVrKNxlAV99gUkh5E03CuS8AGpOIP7xrgjyqz2PWXdDFOWAag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
ترکیب رئال مقابل فیورنتینا در بازی دوستانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/Futball180TV/102521" target="_blank">📅 18:17 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102520">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHbGciny2o4HtLespz4FhB8Y5pJIrPAV9O2yhc5IF2YCe9oEobjcNcyiycmtPjAnjC9PQrRoTz8F88rT8EYdYCRpW_nu_0Fk2g9CwFLTOTcWrcz3Z6zYCyi9WqzeQRV0LGEedEZf1R7ikJ45bm9P1PR4_tFEWWlGGltMTGM24lN9vRvf3qjtUXxAKmeGdW_4HDYpCGaU83Vv2eGo5ssP-fZA0FkcdS2nSIB9t5YDzP-7dQP39ga2CzWJtRy3XvRSiyhVbwzFcm5MKMrTQwHt1O3WPIeIw_mYIGpn5dqDxHy3rdoPkAbO600l9fpTywF-I_rBFT081gOrY-Zyin3FfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوکاسل رسما لخت شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/Futball180TV/102520" target="_blank">📅 17:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102519">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDLtTZskk0arUtgRSQDD3Ged5rlHNDTgTowXMFpA_sdJuyhuEY0GYYXScMfnZitTqytHGpp5KHMjdtdKEOZJQFNAVaif4EzJjESvqy4yHGP72tLNQtrQmkXIuo62rF058KoATdrOyxsM429SkQfSwDfGDGyIvp_RzfLgspb3Y9phW9mTBuisehbLhUDMVGMhFC9xEO9JSHmsSxv94kyc3IB7V-hBLEA5P4S9Xc8_DrUnHHkzNAgftil8ta3UiTz4_LGAuizfAnx8BRMII6F3sp0Z9GMODKFrGDGi-yprhalo2c_h-S9h-5yxpeytpZsDi76yQQEvXDaymM-vFMajaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
چلسی پیشنهاد سه باشگاه اروپایی برای جذب ژائو پدرو را رد کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/Futball180TV/102519" target="_blank">📅 17:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102518">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSTe5GUpPpf36_5jQhP8745vJLVaF57zuojfzGkbXRmgI5YzLacmSCxsiR16b2PW3lLkVLvm6RgxL5s36Tqzk1lqEnRvlUo1eUwidvhMmSnEpanPd4diDL0Rx3Og6OdaJqabekdc2_rU7cb52qIUaT1ZeYHOXuC8aD0oB5NGoMvxusU8ofM-iIstOq6Hibxbi7WblZv810pSaCYGIMiVzmDf3-kIIoK1C0j4d0K2B37EM2BTZ233VmewSsXLIZQYswrENwwbDAdPh6ILJ5wiA3YRz5uUFatoI-qlEa4m6QIO08HPyN5dAJaIYjwh9ox1Yxg5XHR0OmTn-NxxIbx8XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس طاقچه بالا میزاره و ممکنه بره آرسنال؟!
من یک ایده دارم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/Futball180TV/102518" target="_blank">📅 17:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102517">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/102517" target="_blank">📅 17:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102513">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S9mPog6CqJWD24_nDW0t33EgqaNDkRe-MvIEKqSIqiOc0IFz8L1Z9zG1tLSwds4igbXmL33RpwsBm-d6iaR3J5id3QbsBmBeHartAqaZX5s_MlX0brRsCPadrmmPTW0CK5R7s4wfKDZqcFv3rV3jiifiTTE0Pjtau7SlgyX28w83iTRVW8OP5I54aHHPmHC7ghlHBCA9TBuHQDL5ezlUnfxCm411HBTvpKYl_QTPtbVtXwzH8Xgeq-bJV_ZoOkrARc9LhB4fyomXuvso7JxN2jUi5dFS7JTvgxWlMTk397Vc_GhyKba0TAWWqTian2by4uXew5LQpS3OfloyUFaI9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/et96n4ctRLLvGR_7CTPF97BW5lp2ZDUzRG-KaQANdhDWICDuvSrQJdW5bIE--bBD4wsU4iPKlkhtnT_155WvQXd-RQESbam2hvs2tAAfA00H4Cv1NDbAoT6U9HnMbyAK0aQkx7PYszDQSBu_K_ayFG1WVqhL5q-Wt9AV3gueQyHcGltHjeFAJTCvCLG_BPpjO-NBNktrlHQmDgUw6rpec3BlyHxvNQwEG3vqj7Mc06bNsQPREQLCUUOo88q64VylLKNooMBSULqxdkrF6UEEIVzsw0hb3tZn7aCqH117gAjx0abtWb24MibNYGjk_RKgW96DX5eRKFgY7ZDsK4XmOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z2zxW45bJ-6YE8gVkIj46lJZSheQOEY0WA3VtNyw2fDfTtrnI0QIEHZwTcDcndeLIVBLzcg8jL3ZdyDvgMjjZmEBXSyGgmku0_X2boZlqdIn0BPjdZI0i__Su42zsbb6IM-bjD0s_nWpxJHRCZ2ezEYfUJIjgVBPLn9ZsSz7lntTZNv-HtUljoT3YXouU5yEBzAzuYpPVDuV3dlVK46avhvMHOY_GwSBOgkcwtI476nqwbINrTB1CrOxvyqnV_syBjbTg9UhH0f09G56D3lA5BLxoi0wJKLnBsYwTbimDzt_gN8R-PkWEiYYyo_VJOLsYnWqWbZK-OiUXX-Jfw44Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l61Lkd8Uz-GcPmg-QHGLj23gRPH0XPKsYSTpMCe5_JK3nnMDswdc-3eRYccL_ibp2IQwkKIp0h5XbW1a1MN2jUH5vDm8OhHPPgJzYcVVLGka2MmDEYXeXLuq1RsDlOfPLxK8wPrfz6ob5BEq9g4DFyy1LFvQENqktkzyih8a78G5hEUI-4GTQ5wE7wyhJQUOdAwRpzMbULwO-ciW18rNy-UMGmCaQm_sfOjdAgVlRWN4uVOWfo8m3gd0AwHigP7QM1xC4J5i4ialRb71d9GXxWB6Kd2oGOLSYSbwyHxwukEDg_vca4odq5a1M_YjvcH4eEa9GMDa0Ornn6s5gotQDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پستای جدید جورجی جون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/Futball180TV/102513" target="_blank">📅 17:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102512">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LF0ozzzbzSoPRX8D-DFhceHe4U158gTJNqe1q0gEP8nimrbzEua6XoFu7kC1uBf-_5cjsyYwXrHJH5b9y7pZR2ZgaEdBRzwTNZaa8zWEDz1hOOxT0LVjfPQZgH4Xyc1mucCkI0TIuL3eugFV9lBOWvT43nuQKmBBsdXhhCUCexmEqhSxCVCd1VpOfcbCza6OlEMBNBRUN6_uAclh1IpHV7NBwa9IcshcNsliLBWTmWZdZWQHLpmoF-dsc-H6wpEiTq7OssVi9rCitF3AJvs6XTr9wtsZKrT0QdZ3HhJqcyi1PBjtMYuV8DDEZPQlGmtxgk_nDyHice2sEaH17BAijg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🔵
اینتر با نتیجه [3-1] در ضربات پنالتی مقابل منچسترسیتی پیروز شد. بازیکنای منچسترسیتی سه پنالتی رو خراب کردن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/102512" target="_blank">📅 17:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102511">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/102511" target="_blank">📅 17:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102510">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSPHTMdjVp57Nk9Y4d2imWkEOoybuewemssagTvBmMVFoJYO0gYkquJHDmivKivJ5V15vcmy3V7ypXX8AcrFaP8wUmcyLyP_XdK2iosDUANZASpqroi7WLNpSoOYuzTkfZRx5SLo3Sj129keRdIGTlUEIJn4CqlHZb2h2O20t_cfd0yLtNLzZb_dV8NN0PtV9wYhrOoaJ6gdiPJPHZe_mekyWUaflpZlTNFa7xvSwQGzaoMu0U_SMhW86TnZFny7SgSQ5ng7-xPYnIVzgcuk2g6mPzXPbhoXUp0xXLHlBEyEI2Cq9uaCHxUTGpuwqHPNxskfbuN3UzaMGM-l3OO_pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اورنشتین | اگر وینیسیوس با رئال مادرید به توافق نرسه حاضره همین فصل به آرسنال بره.
ماریو کورتگانا: آرسنال ماه‌هاست که برای جذب وینیسیوس به طور مخفیانه حرکت می‌کند. آندریا برتا، مدیر ورزشی، با اطرافیان وینیسیوس گفتگوهایی داشته است. چهره‌های کلیدی آرسنال نیز به نمایندگان او اعلام کرده‌اند که او مهره کلیدی یک پروژه مستحکم خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/102510" target="_blank">📅 16:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102509">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzcNNldFcRO37RtUz2tcIwp3nSSb9hLmeez-FoGIMHSEkWnDSm00A6LTb9kWagrmPvN8VHRUataONxhwZF2RXETRRQgyzBtNJ7Fs6Lz0ON9EIbReQfID1w3c84_Ix3vcxiecx0DW7N1s0OXE_auB1icgfP314sxuRgwpLikKNbmPd0gfyb4g4jUlFjDiS17fkUJtchKZSNKZoZawFX3dqZAycmIVqXmR-6Ucx5US4WaRoqSCCeM6RUokzWiBkOaXP2FJOLgBZzQ3mmv2f6r2Y4HmTLg_HoZfbOqG-ErmJG7BwWF-UAKXrORN96qi2jRTreEc0PGsBKutmNpFJZa-XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رودرا - ESPN:
طبق اطلاعاتی که به من رسیده، انتقال یان دیومانده به رئال مادرید با مبلغ ۱۲۲ میلیون یورو + ۱۰ میلیون یورو بند پاداش نهایی خواهد شد. همچنین انتقال رودری حدود ۶۵ میلیون یورو هزینه خواهد داشت و باشگاه در حال حاضر منتظر نهایی شدن انتقال بوعدی است.
⚽️
@Futball180TV
‌</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/102509" target="_blank">📅 16:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102508">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDK3XyaCOYOh_Nki8LUYkP-O_Tsa1meXZRuVmd-3dGDNztCiJrpJ1zDBGnauhPFySh1eey4UZKOEcyZqRLZXTL2nQ0fXQGDPxlG-86z3VXjzByz9zT6_TSNwlhQ0QBU-IzRACZ6eYA8xRNeDVVZ-Xclse_8mp-_gDO70FE6bu6pcDqimSMcFqlmuJvdrOHbPUrtRrIdWHT0HPv4sa6E35nAgGS7F8yJ7aTAfA7o1VaP3q_WlgjCmaKfgyBWGlYZHmPO2qLGSEXYxOCf5O1aBCzoVlOOpfLC-52cbrFqwMuXPwgDnbVdoN0wg67emi950zvK7q9tQhQhnWj9O02GpxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین شات از عشقتون وینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/102508" target="_blank">📅 16:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102507">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qC3NNI4nfvTJ3ScMGpePfWP_Slvtaj-3lwdfl-llb7agLlRBLfvh9q1xxhrTwcnpHT8ERkwqhEptynD598-_KzveJUjw0dRwLWPB36ROzQHr1KwSJZXZLtI-hbAi5cBLOdHbf2DLhFI23bhzDOu0U7iyybMiHgjRbtwtnlzt1BKy5LtNDGOzFBTcLvwkwemssK54ydRsz3ijCgjsm4Ca-OAklRSo9zfMGtO7VshmSeVUyhhdoTMZ66Mjm13S4VW5iOeRe-FF0ENWLhs6S8AMyxiJ08aijYarJz2_7Z1AX6xqf0AdUcHhfomRnZxNcpgs2z5TX2FGlkGg3ceQAHvNpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚪️
چلسی در یک دیدار تماشایی موفق شد به تاتنهام 10 نفره 2-1 ببازه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/102507" target="_blank">📅 15:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102506">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNV_2C3tgF_LuoRxOgQn10iOFHqp12-lpyu5sCj6zzoc1zg9m_Bu0ojkH8fnX0ADUaENZe0l1ODy8yT1vngAbApcXdR45I99FPmgCaMGyvPPt2WTJy3WykcJHps1OKGR2IpBfCHmW4VgBAJnwI5QL88svnJsZ6xBVXcw-wPPRDhPD-JusxJEX8vW1qsTHgJhz-rYbDl6Qwy_T4KOmCz4SOA0fsE32iNJ1BynKzeFwBOjYpfktn4x5lL1N_Dl2_ysb3pPAzRwllEkalouXAbpwKfUC9rZROq_8Ux1pg1-aO1ZIb9knThVZ5A_kAxcOCh-bM3tc6BbsCnpCoGj9EprsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
تام هالند:
بدترین تصمیم عمرم که خیلی ازش پشیمون هستم اینه که طرفدار تاتنهام شدم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/102506" target="_blank">📅 15:07 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102504">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a1fTku8wXouns6Mo_HDXaJEzmQaxqI_1vWgkHxiITZRzBISgpPmErvuYolpHQlAJCaZvY18XE8btor6ZtH2ZjoB1NQOJAYy01m73cxXnO6qZmiiQGtWQi-CKtByFUKS60mARMXdJVog6Xjh5haUcBa8_oOL2Uu26rklt2AnL3rUYrhTQT1o6OtNHLHZMyyu3ZGvxt1Jj7zM1g1bIzq9rdZfqFEk0XRORq3fqLAvrYqSISJE3fIy-l73rZjUXnhpQQv5_tFU_WBHbwewvwloTsGh2oSYaNlxliFW2G-cCfESsSbUZEfYQP_cZ20918UAPey1VGDv97kzU9QdDPFloag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qj8j7tBO5Sq_0tcFdMILZ18nyQuT_3BGfrLdq55-EEZxmlTJyVwHBs11hGx6SzJTYUb5Bp6Oh_gtirIdFV-uLbEuLST6ZSNM8Ig0EYGere8PkRNLmo3_39rGiDY5FAG04xMoONnhCMbXsqNlUD3camme2jMM4MevtDj5EAK2oWGtchTzpMyZcnO4lhDPbeoHXHEbCaJQugRL_yx4hNro7UZZ3cJXlqZY_4Dz4OJzZC5anQKIRP2_tc1GUnE7XzAc974pqeo5hYnaZGcdA4KAJNbj5zkadBnYb0b9JE3ZSyG0MwnWCCvEivwSXsYxTeveugvCPjpxkZ0m1PRabYdZiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
یه پستچی رفته بسته‌ کوکوریارو تحویل بده که کوکوریا نه تنها باهاش عکس گرفته بلکه بدین شکل یه عکس هم با مدال جام جهانی ازش گرفته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/102504" target="_blank">📅 14:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102502">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rySRZayF4adT-0-oh0JNzBjdI-FfAX0BlTBHthvJp9cQ-gFIqmwEKXX9hgkBKRMmZB4HIPTKGFBx_Li_95ZGmEaFg1u-EfuhpLnjDWq3LubQDz-KSyfKFnwa4Z_EiVs1FhbwT7m9IE6nKit8MkEIwpSM9QYzY5O-s2DJXD-x6vW2yTbfNmd2y5aGQ8JnmiLBO7_hCKZCorkIhXBnHddkhteMmB2lxvg5o0V8MJFE_OripxdOY6eNmAVqPxibxuanS1oTt-taDukTl7LvyQ1lRUdie_Y-EI6R7V12LGLJNtU4RArqb2YUFAlbJI3d2B8Q5_BoPDanFrzdSESHK6ol_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Du80yLNkx_Q7p_wgn-PwHpOhnBWTopFUGhaKxi59HValggMwMhz1eIu5cEcm5Jjr9ziGAjx_hUemx1_mpphuRMxtpbZ02bMdJKaQIcUC7Rr_xnNvDqu43f3UJC7lxfuNzIrBQaN6yaqPTTDW_AJ0rRiNfjvfFFvmaUHstColpHQFz6FXjmK1vAz9_St8DsC7eXEE8nRbtuJGyTU1H7lXXL20z_sruyifNWcQ5rBUH2x6fsPqlihW_dwUWXuKSf9VxTdzrhzuYWRIs_hY2ZYtfOAFfkBC7SzUJahtX0gAOrRsE99og_DuSI46v9f7N-jHBXHU-Vf0I1f_EwSIDnuINA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
⚪️
نقل و انتقالات بارسا و رئال تا به اینجا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102502" target="_blank">📅 13:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102501">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5_UNSbE9Qu_pK2H1HNcqfmW2R2dCCRogR-IZFVCOAfymIzGPfs1GPv_HXK1eP7nzMZvtinc82IvbFDKYWAQETBrgu-RYhIqjLirTEpNcC_71Vkb1hA-Ers9yE9BeH9fwZCG2TI8IWLIaYsxT0axQrkUp9BCDfPITOQGIEvn-B65wAA4MOXJhR8DochNeg0AcYZzxcavyAa_FwmrLR1lLeVWXGZ7L7M63zqjQuje5biHYelo_5fR13lg1fiCgFjQcYjgR7yYkZiF7XQtqA1JDRPk3XPZ13ne5UohziO1lG9cUr__qeb7jXn37BpNuyUL_ifgjGmZvxkjGNhZXLqLiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رامون آلوارز:
اطرافیان وینی هرگونه توافق بین این بازیکن و آرسنال رو تکذیب کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102501" target="_blank">📅 13:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102500">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sf8w7pDq2_8_iBSSw5wv16uoA9yT5S6kXwFj3SzB9CIKis46zEBUWTe0Rjd2EM2lGWbuNV1RKl50NYMWH11UtJtshaLIZ719Wvtm6Rfi6C_y0Tf0eSu6qntsHQtS-2gpHVTLRFEremGlfyxKKTk7SUaHgNdQSaMH5AtOXR5GurqiezDJPR3RewaCCIZ_5YIxYlZTY4nvs90m_6-UIIRAXHpPeS1VbnhiDk7VzS5gcwFdoV3sRAol70mTciHq9nhsadnENZeFxGptaY6lZW9k8RqxTIP7c874gwhif5ZxbxRgQvahv_d_fq6BT8U0h8-cG08pChTizNuQUzwg7avobg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
• کریستیانو رونالدو به یک ویدیوی کوتاه در اینستاگرام که او را به عنوان مشهورترین ورزشکار تاریخ معرفی می‌کند، پاسخ داد:
"خیلی ساده."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102500" target="_blank">📅 12:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102499">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102499" target="_blank">📅 11:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102498">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102498" target="_blank">📅 11:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102497">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwRvnMfsoc2UOnS7sJYlnX2akiSBMBc0dyqn0aG4vBr4tAfdpH5zs_nYESkqgn23gWdC9cqQrA3q76StUgtE7RU-kdrEYzIP7ebH-UyKCnae8IYOrxnU9oZyb-UglwpFLq7KcuccWIn4PpVBQgc1Y4Za-X4L6s47B0xN84AWaqzCyJDTtsPrmWheJ09Mcxuc9fMh31KqKfayqpPWcvvK9rQZRHMJzjZW74zO8YW7U6ewewxNtx4UqYrUj5NU5GJOVRRoxRYHFR4GqLgidM7lJyiggDTsvTSIDgnMsfvnkyuNZx_2g-oGcPIm4kp1Tj9vzF7ONQTPm0C4wFGjcYjvRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
اینفانتینو با انتشار بیانیه‌ای اعلام کرد که طرح فروش بخشی از سود جام جهانی به شرکت‌های سرمایه‌گذاری خصوصی، به طور کامل لغو شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/102497" target="_blank">📅 11:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102496">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/102496" target="_blank">📅 11:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102495">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👀
🔥
هشت سوپرپاس‌گل ثبت‌شده فصول اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102495" target="_blank">📅 10:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102494">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LuDUKzJs5mE5KePnwIeMi_1iQ9AbhKM0KCULlVIXto517-6VTVbIIQ7QUsAJe9EMj5aQXrvlYEePC0PCAU1_GhBElQfz9LrfibsU1vw6y8s19JnUW_5BjUJg2Fy366aKzrkTfVRJ5Fn5rW0RkBpLt8IKGJRurQEF_bhjpxmHbxksR23HjTxhQvb9lQ6o9PBYyuPc2lWnbmbhHONDBxCAl6C3bCwHHAxtNTmPr3aSLQG1GstnubTJwqVy-FloBtnD5En1_N59tbJwAiU-hPBubG5H5cW0rL2kT56CKIB6BxF0Ss-p19ygQSPCyUm8HH98GIYLZRlPxdqf5Jg_KzsQTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه آمار مسی و هالند زیر نظر پپ‌گواردیولا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102494" target="_blank">📅 10:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102493">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvfujV1Z40npbDQYKOnmQyKyWhpoGRO_5YZ6ts1LZuQCHpVjwCfDi2YFbhq-HSrVhFhiet9LKjwQo6Qijo19cCBF42ohyO-IRJ54e1qbSeoWyfQf_EKTHU7Logz87Nx7HaM1KA9_s6GWfpmvzYHy_Ga4IsYa1aCY5KoSSjciSvpHLaDnO_s2eUK7KBd_bkc0PwQDSn6r7LieHLPO7zmqs5La6bXPpah40y0-8_yXAkpbwWoOhKKLECW8IXxpBtoyRn4eXtyybgAEpqK_xvzmbdwaaHGb6CGAvbCmFu98pWeaipP1De8y2c1Dk74d_mBR4kv1PJKf38pcfIO0S6tAhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تمام قهرمانان ادوار مختلف پریمیرلیگ ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/102493" target="_blank">📅 10:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102492">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102492" target="_blank">📅 09:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102491">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5RQ4eI3U8Fm-COxxW8lK1aodHNFLoJsLSt-zgbKJ9NA5SVkfnQJKSv0MthjWxovUGeEbjZZqEULNyV6719LQzuVPli2ZhCXyJzChLHuUVeSjhKF0jnippBB0D48ALHSyhJ8QbTl2CiGIHRK5Nib5vG7ZRRQkzKQHyQW96CtHBlBeNZMCcyIk0q_n3pXEbCxBH7r74iZo9b92z0RT_0eDMyTn5zSEw_KCRr9VcC22t2uTNbMC2eKfLMgHKszWErD9xKlKzti6_MF9ZxpL6sUcX_ObiFtI5-5ic-ijmtKfmQdYqXb1kHYOXcpoG0IfadL2vmVbd4KjeYskQUgdbnOXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
🇫🇷
فوریییییی از فابریزیو رومانو: پاریس بازم وینگر خرید! مگنس آکلیوش، وینگر راست ۲۴ ساله موناکو به پاریسن ژرمن پیوست. مبلغ انتقال ۵۰ میلیون‌یورو و تا سال ۲۰۳۱؛
هیر وی گو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/102491" target="_blank">📅 09:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102490">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/102490" target="_blank">📅 09:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102489">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">هایلایتی‌از بازی‌جذاب الکلاسیکو در فصل ۲۰۱۲/۱۳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102489" target="_blank">📅 09:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102488">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7q3yDIgOI6aD9ghFxhJoTVh4n0mdf0EeF7cgAIfUN5UaLBoPodJQ7fABvyAn0A2_IgWzidZd3yq5DiHSmahw9bcm1nB38TQqsMUkKNQNcA_0MuuDDfNha7Knt32VAYGrrEZvbmKYsxg6MYEwnMuARJij9-XoaotDAR0ExOgGsUY5Rm6vwpUbbpXfu8NP-tLVuY5MYgB8Ihzi5rs2f4-K4q-49zAwKwT8Bt4a8htqvVmlWMMK2OvNvvPZt6ZuNJsZwb5iMZDPRK7Q1JLYmS4wbrzCgG-d21RNsksDExh0clfkcjk5TlfLY4LJWfazfydvawqu-mfCFJNPie0lGxpuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیکنای اون ترکیب لجندری بارسا چی میخوردن؟
مسی عالیه :)))))))))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102488" target="_blank">📅 05:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102486">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eF96ltloueL5yidqKhK4m68FdV-Hf77RpL3qW0DjoSWIKRQTDvTivyZmUlrR07YqjffZYq20j3BYGtIYQ8LDLxEXOb_vHcWYmGYtFv5mkywik77SJG4uy7KMpK0f4UpeGAlNnsUNhm30l8vsK1L-Z7WoHxBFfNTHYYTrXDWTQ5jr-oP-hUYLY-VLbBaMaOHkL7L_8cLTbYAc3186RQNUpqdOOBCYSjBGDGBnlfVdUqpSdwCDmr-BQOlK0ffwhemuA9I3UgZgkop8NQR6dvhE8r_w6dNF587G1dRss8f35KzuaMOiLsXTjyjVJ6sRO4xmLZ6Feifn0NBNwZYcjPLHnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
گوئدس ستاره باشگاه آژاکس با رقم ۵۰ میلیون یورو بزودی به psg ملحق خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/102486" target="_blank">📅 02:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102485">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
🇮🇱
کانال ۱۲ اسرائیل: نتانیاهو در دیدار اخیر با ترامپ موفق به راضی کردن رئیس جمهور آمریکا برای بمباران زیرساخت‌های انرژی ایران کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/102485" target="_blank">📅 01:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102484">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQDH7c-fhzdJn_b8zAOt5swZaDYJfIcJMTqAsxkuQ8OYO7uEDpeFijUjGIe3Wf02o1s5El7suNkzRnJ5bfMN0XCMvx-AC7LRU6u_YUB7r5U4P5GXQwEGWkm2UTumwkWBDyO_4yXeqZ9OFFeaFgfCL53suqctbf3rGe3l9uquMuHeY0VhNkUBdZ--yU13qFRw9xmd9dLKIenagc0tv7jzXW4S-qwXX_mjyvByBiHlpX2L8rXNFW_1RTpIxh0hYmHvU_f-Q1DyTg1Q-rWnjBvUxbzWFyE2pJSqbQ79cQXscepL2B2S_IGCMU4_wtkWR8pDpzYExDa0TMS0ejNYNFf8Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب بروبچ محله تامی شلبی حسابی واسه جود سنگ تموم گذاشتن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/102484" target="_blank">📅 01:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102483">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔝
وال استریت ژورنال در خبری فوری از صدور فرمان ترامپ برای آغاز یک حمله نظامی جدید آمریکا به ایران خبر داده که می‌تواند بزودی در این آخر هفته (شنبه و یکشنبه) آغاز شود و چند روز طول بکشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/102483" target="_blank">📅 01:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102482">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edBSh1GaeRuz_SnJxCe5heoOIidGWrOlkBi4pdNa_Ybi_mWeqsTS61lTv2C0PauZ9jUPilccCnod-EgQAlFJ6a63Y-FItjqTHRJTaBGqcl_PQPJ8BMT5vx3n9WJS2XIoRgKL2YpY6R6XYm5qT2q-wXY2osRlAT0jxsdnigDNibr5sVcfp4SINpnH3W4nmZEb7yEVzehx3nWVJ1LwsAcaRLnSv5WskzD0mi3SIRY37VRlYAY8s5QKyYaxwymBJNjeqmUma0HB62tBaTy-NU_if1q2Nin74ynFXTSoM4LnJ8tWZa_93tmBU-J3-dbTdRdvULplIIrpoJRq7y35TJTtKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔝
وال استریت ژورنال در خبری فوری از صدور فرمان ترامپ برای آغاز یک حمله نظامی جدید آمریکا به ایران خبر داده که می‌تواند بزودی در این آخر هفته (شنبه و یکشنبه) آغاز شود و چند روز طول بکشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/102482" target="_blank">📅 01:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102479">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y1lY4nX_NS_1lGl76WSpFtpCttQvzASce0ln1DlP_oDEJRzHqR35SfCbeLIGQft_dvHjRD78kE2boANSDaMPuUAnytaSs2ajyFz1dUnqgSBYFDQlFdUPmBrIxhNbWkKiNwTydXBXV9nr4y8pm7Eb5fng0BZIFpNzmCLykbYCmPIz_ViVBYbC_j-1Qq6aVOQckY6iwK57oFiWo2Bo4_kUW8XPFFOL__cE1ugKDAQB69KslFTRKYVkrDzLpYnruDPxpqcsSZ9kzod1yjt586HPLm8aCKhSz5LFQ1I-dwacSA8c3qVsSlhTBUSCk8prnu7qHS5JCHdbVQHPxkB2VRhMXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iim-C1yAFr6WptGSNUeEHDpMVnWjUe6A2XkpuaCVcsHBghnaoRT75hraA6xfJFJC0WguiuboBvmJafGwUE1GSKWsWMupVtj0k_QdEsBlgeRs_hW5uEfpBP_fFo5eFUlvqVN4OyYZN5iquAs-M1my36BYPES06dXTavWyTcwH-QY2WQXeF93covsRROnyAdJmRc7NJtqQCbmKAym2JEcQScUKxiONui8VKARdF5En7b-AYtAU4V06l801c5gWpZWWuwTDsgxILc0Ax3ZgjYr9KcW3G13L6ZfeblyDUUjA2tC7XeHN-iYQ23AdDcnvLvRtmIaeJEUk55iNVRrs5tdxjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j6deKlP5xYjwdAoUOsYZWyb2kHDXxua9_mr4Ds00_R3I7P-MnO48rYPvWKHBQS2XeHUiEt_XhdDbGmlL1o9UVEd-wc2zPXhaSdFxUyw2j1H4kNVJ_IhausjpfkPpfGG_leRxuIzdbcKOtvRlBAto4CigvJphR9QpkBjMNXIW5JoigvLLTn_3JvvyVlk0qDqr-hW47z1ndexKD_KvMb-Qp6nk6RYoD8p6_m4Koq6mxh-CFl7bYEcQAVmkJjdzzmjrkTA9Tusxm_Xh2xNXAbmNsuBZN5AAb7m-T_srYURCjqm3RgOjPWfCV_ZclsioqPyDjaKLccOJhdHXWV6CmBW9Qg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
باشگاه فوق العاده محبوب آگزبورگ از کیت خودش رونمایی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/102479" target="_blank">📅 00:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102478">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMbk9nkdUmhO27NX8_vb1-8LXza6dh4B6IQszK_1rNOZXKOUwJ5CWZkru4q7FNr6AOll6nUmhzr7tDdGP-to299oiLlDRaiGCLrZKpLwHo2yBF6OYGWhM5iPBUnMzKYj6a2MQF0RHN_nC7-4e4J1aG6b8f9ficd4XYnTBy9rf28eqRyYVfzBvmBWW7yHnDfuRTRE4qYA0IB7x1WL_ECuf5D1vdE2FXnq_J4cSuNnUCogdP5VaExonlnjo5nEBmmJqyQQmVDLBRY_lqQNcW9f2W5dXgjKPLnL9gJqRf6RHhmCbtZI-ZeH96LrCP8xZ32A4l_3J59ivW3YkjBpfx5HHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
هندآف آرسنال رسانه نزدیک به آرسنال:
وینیسیوس شخصا با آرسنال به توافق رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102478" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102477">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی،…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102477" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102476">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=g26w6OWgkxKQVKLpXGYBrFFBmXudvDXg0iNjtWypIte3Hs25_A0CO5aBQl4LBlcoBVlLkNhs-iQ5dpmVArzZilVG_TmA_avL_j6HinH-GLo97vdaEKiXzKVMDoXnXZ93EOPxwgo8eYWD0tgrSo4qls3xAVZh2Mf8_0Z6uWXPR6SwLYGDt3OidembsS0eT5gcIdrK2VvC74QkC-JIlk_fGhm5e4Ur0E_hRusT40Dbre2p8UMCJSSaZaN439boKcbEMQD3NjB_IUDlUgMfzjE86-NJDoPTESH8jIwRiga-vqwzByvcTJMgRAEMlvcv7EhMtlBiPajU4AIP8N1XG3hEcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=g26w6OWgkxKQVKLpXGYBrFFBmXudvDXg0iNjtWypIte3Hs25_A0CO5aBQl4LBlcoBVlLkNhs-iQ5dpmVArzZilVG_TmA_avL_j6HinH-GLo97vdaEKiXzKVMDoXnXZ93EOPxwgo8eYWD0tgrSo4qls3xAVZh2Mf8_0Z6uWXPR6SwLYGDt3OidembsS0eT5gcIdrK2VvC74QkC-JIlk_fGhm5e4Ur0E_hRusT40Dbre2p8UMCJSSaZaN439boKcbEMQD3NjB_IUDlUgMfzjE86-NJDoPTESH8jIwRiga-vqwzByvcTJMgRAEMlvcv7EhMtlBiPajU4AIP8N1XG3hEcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102476" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102475">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SvGtyAfGs1NH5lwG7rWO6z0UTD-Sf9zPiXanVxmD7cdgdTHi4xJBIkAjIHCOXoLw-c8DrAFzrXyoZcCmQU0EBt5X8SNfrDNgDERxCXBNP8nCDb4CQ9hhOwyJnIfX0PiYWX3tjJ1ZzU-vpXeHoOaginJ-hLOJZ9qXSRb5V1969WUOeUKPJnDiHyCc5zLs8rvHj8JFPaePHtH-2q6uqINmpQ_FZoCOwV1YLGBEKtAKK33J4PzN5L7uStESFoR8K5th9i2OU895hvyxuXNajQhBXOHEsJwF71XXZkgT3sV135aUV6RccinYVCvKCKzvDU-VJyCFtqIqBBPiyncsNwqWlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
بارسلونا در یک بازی دوستانه مقابل بیرمینگام شکست خورد. بیرمینگام با نتیجه 3 بر 2 در ضربات پنالتی به پیروزی رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102475" target="_blank">📅 00:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102474">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GaySU_x72ruMbOaULlzU2_-KZ2-jhB2nl-v4OaFPqkdTZsb1S737v01xy2SIfXzvcjVjA1Rk1oIabQ6EFEvDPFwRqj2mrvVrnuxWVEtG4dLU-kKc6YbP7XQJcavUM7NZg1nqDNli-XQfkpChaFxT5vjzGLmjsfrwV7qFEPA2TfLnanIx0YEY02C03k-sLyzY5BGBMd7UQWwlN16p0tfDWxpbcneG7mQ3tpd4LnQKUjvGy0UkMhTSmHek7HG2I0dMabz1tQObMf3Fl6S_QZqIJG4q3ZuJP_qLRsar2OS-UxDY_BuMYMefOXRruG0dlLK1aUG7db5xubqG6VIgs23HWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری دوست دختر یامال
😦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102474" target="_blank">📅 00:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102473">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDvcY2P7FCfLBUWcV9DpYOe8qcelfJ77TP1pRx1Jk-1D30ded8zcZHZm1-TdcXzXeERfDaDT_KKfAkjJXA5LIgSkkvNC6IcPZM_GD0tybTuuOhzHYjW3NULOITG-TjNeEG3qo8N0a2J1B_wW9mY39LB01zXimnnNDK2OpggJBQeakYcQ4zxNnWAgAAFaDACPyZythGgQBl9hn9wiP1T3w0A2NYpvcSqR2KOzqdS13-RGxGKqZHp_iIiwHaz1LAp5HVBt1mPuaeSbsQF6_j4J37B4M_TJyTeK5zCTwTe_f6YUbcWTB8x6w65h7yRpdvo5w84bJpBxP-FJUw5rkeACaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟥
🤩
خداحافظی امید عالیشاه با هواداران پس از 13 سال حضور در پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102473" target="_blank">📅 23:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102472">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WK3IL_rhtAEnGUisMLYm7VcUbjIjHG4cfDV_MFsu-7mvrB5aT5WgFmNkcvS5_lJcMLLcF3rDDmrRSyMyV3nySUy2xLufwD1cjP3tt2FJeBohj2hN1y7WQEhpzIy8VTIF0ngoMP32x4ACm1cSA2Fu0Kl0v6TPf-5rqxwZ4ub6We91R2omDHtoxfVoLjIJRL2Ff_wr9bbpkhlnhCx4jGoq6zLs6SlMRz5lFzmpOZ1XpEkMWC5NlahahRugAjC0a4aKr2PEprvWHeKWR91cS9BXW-SPw0BL977Tp1mpoVaAKQykun_X7Gl9Zhwuy2OEVN9oJ4H7EAmZUs2aWqMrC9KU4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
مسی و کاسمیرو تو تمرینات اینترمیامی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102472" target="_blank">📅 23:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102471">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26c665525c.mp4?token=emlA_8UBQn-dioXa2gCueytfFpv0o0ltK5s9mf56Yx1JxuAM2ZbsISaZqjjvRaq-ToYUWW4dZ29CNVC417EYEzQPYyWHqaTduXYgZyhDeETuGs0MTYkz7cWYuK4249QS2TV747417CNMajpcVQB6B4Pwf4tyUVMSqqMLrrzApnoHO3T_1P6tjeCUmOAigIAv8seury_Xm9izM3MKhRmhT1om_DCICiRqYdue7ZoBUp3CnzPfuEMunL9FchOPkI_YfUP7uF3rUhF35tE99EPSCIFFM5NVFvQAUptijQEFk9SOAhgUGNjOJ4vrPqnAsoIssHn7YEGDnLt6x2CP48nziQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26c665525c.mp4?token=emlA_8UBQn-dioXa2gCueytfFpv0o0ltK5s9mf56Yx1JxuAM2ZbsISaZqjjvRaq-ToYUWW4dZ29CNVC417EYEzQPYyWHqaTduXYgZyhDeETuGs0MTYkz7cWYuK4249QS2TV747417CNMajpcVQB6B4Pwf4tyUVMSqqMLrrzApnoHO3T_1P6tjeCUmOAigIAv8seury_Xm9izM3MKhRmhT1om_DCICiRqYdue7ZoBUp3CnzPfuEMunL9FchOPkI_YfUP7uF3rUhF35tE99EPSCIFFM5NVFvQAUptijQEFk9SOAhgUGNjOJ4vrPqnAsoIssHn7YEGDnLt6x2CP48nziQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین ووزینیا که تو جام‌جهانی تک تک تیما رو سرویس کرده بود، جلوی علی علیپور اینجوری فحش خورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102471" target="_blank">📅 22:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102470">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpeGs3nx96bvmOx8f9GFjcFC8y1JtVXkjfRmXIvWA56bPTPjYTJRBOslQf-VdoBrlY2WseCUIVNPh7Ius80WwyWihwimB2izgJX9K0hjw_jROPrrcaDinLMRFU5zIRnCNpUaoobyvOSP93OHEBn9FpHLwj35NjKqud2s14RWqgjqVGokH4pDSP0nN6jdsOzkWxRSqPubqGa8x6q6c9vce716axmT-UJ-MZp0cuUy0u6Wfx1ueX1qtu52FDiHDtBW-9xjMoteUt6LWs5RDwig_ysxxBphjYZJWI-2x9XurK4dZQ01Qj3ZZY8iIzkZoaInVmdBXSrxc8HBE3FYJEP_2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ار‌ام‌سی:
مندی تو وضعیت مالی بدی قرار گرفته در حدی‌ که مدال و کاپ جام جهانی خودشو 54 هزار یورو فروخته.
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102470" target="_blank">📅 22:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102469">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/261dc7eb19.mp4?token=DfqT5Ly_XxlFiNqpWGz83y3QHwaG1U1XlA-X3MwzJsTSP8N5TtYLsw2I5vhAFDscEVFCtQeFbK69RPh85c9Bp9ttif6Vq1zip3OnjDO0zFtpxzwB6PIGXjuxFNh-MgSLSQCt5J539PwIfaZ9_B3xgX8ce9zunzYKx7OnNKTi24fRf6qE3t2TnTuGnf2Hvcka_NBnKqxsHCQWYSkD2j7Hdb3hEwOtILyWnDUGXeUoGpnQQE1XV4gsc-VkpVLrp1DAfIcMHiyRn1uU7L6KEf2QsI5yNibHcnBGwJTo7rMGdZsqxAUEwZPb3S6UNwY3kEnmbzn1ownJIgwjiK7pLCVbXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/261dc7eb19.mp4?token=DfqT5Ly_XxlFiNqpWGz83y3QHwaG1U1XlA-X3MwzJsTSP8N5TtYLsw2I5vhAFDscEVFCtQeFbK69RPh85c9Bp9ttif6Vq1zip3OnjDO0zFtpxzwB6PIGXjuxFNh-MgSLSQCt5J539PwIfaZ9_B3xgX8ce9zunzYKx7OnNKTi24fRf6qE3t2TnTuGnf2Hvcka_NBnKqxsHCQWYSkD2j7Hdb3hEwOtILyWnDUGXeUoGpnQQE1XV4gsc-VkpVLrp1DAfIcMHiyRn1uU7L6KEf2QsI5yNibHcnBGwJTo7rMGdZsqxAUEwZPb3S6UNwY3kEnmbzn1ownJIgwjiK7pLCVbXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
تام هالند یک‌بار به ارلینگ هالند دایرکت داد و از او خواست به تاتنهام بیاید، اما ارلینگ اصلاً متوجه نشد فرستنده، بازیگر اسپایدرمن است. بعد از اینکه ماجرا جنجالی شد، هالند برای تام پیام فرستاد و توضیح داد هیچ قصدی برای بی‌احترامی نداشته و فقط او را نشناخته بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102469" target="_blank">📅 22:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102468">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I98inY2uLcFkcfxF3U4wXwJlEMVeaEk36NPJJVxi5tQ-hdU1zeuU0CkHm_UR5SmbvuBFQxU_rrDkyFItfuIvoX9oSnBdRtgVXbwRBnXIaRtAOGYDlbkbhVWPhY0JyImEwC8mjehtu8NstRjw8G0qf9qsiRAMXBGgzLLsOYE_BgXCgAJ82825o473VlCznRyoiD4hxNIoDUtFkzkGr6KPsXpdOxx1R4DcNKa-YA3YH_Q8ozgn7kWJr1cPsPnAfMhSGEB_jc0I6cP1N2qdN4JyFDk5Xna-ISwTSKxGcxSGM5HTnp4YAt7ItCIjKvkX9zSaecdq5hgCd-dwXycSxVlwew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
💣
بمب لاپورتا ترکید:
جسی بیسیوو، وینگر بلژیکی کلوب بروژ،
به بارسلونا پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102468" target="_blank">📅 21:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102467">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmEpY5B47V0ejfJCjiW7RLAGX2yY5e9nI4yCpOSijtnM0wY6StDiSvAmhAO3MsaQiAZGi6AXedqk_SlvgtCn1EbKBzF6-q0NS2xbr_x_digxWqtDrb567LuIPjAzWOUI1cYkoJPqHZ4G3QcWDLjgjzZsVZN-W_sV-aWxur3UKOwirPoYIZGsTpYrrJcgliXJOG7vBqvvpia5MtlyFSzFVs7e4mU63UM2lRa51Yxcsx9Iho1lJcvZmOs5eYsgoUKMJIkPCpSnvnwixMeEW0Nbl2jNXBOl8LqKlCWxfsNWnKfckHX6IQDd4N0lEiBnlRbBR1L54udxPMNN-YvztdSYxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب امشب بارسلونا در بازی دوستانه مقابل بیرمنگام‌سیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102467" target="_blank">📅 21:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102466">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f4d6d3d7.mp4?token=Bz3dXqmKzu4tFBtM3PM-bgkcNLS4EL6Faik-0vSss1CvqfwZQLSOjTd-l9tZYKW_K7KCF5flmHhN8GOYstUD4Z24pg0PgacN6rK3bFpVD6iLxa6Q-yC94FHuC5pIxQTQP7qcWUcypYPdLXstrTQ6RE0Y2tIzFHJTOs7n59_-wmSZoflmX1Zoj240un0AM-2Jg1pN2maceH7zLo7GPbzXfLTt7T0HR_h5aQ8qiEhr038FXwEljIFZioif0zhQnDc91KqmW_fAW5onof1J0r-dTH3ZewnkV7Dftw8wMAzwy9VRuWLphzpU6WcT7mcniLv7IAvWWIaNtB4fl7CnoL9RuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f4d6d3d7.mp4?token=Bz3dXqmKzu4tFBtM3PM-bgkcNLS4EL6Faik-0vSss1CvqfwZQLSOjTd-l9tZYKW_K7KCF5flmHhN8GOYstUD4Z24pg0PgacN6rK3bFpVD6iLxa6Q-yC94FHuC5pIxQTQP7qcWUcypYPdLXstrTQ6RE0Y2tIzFHJTOs7n59_-wmSZoflmX1Zoj240un0AM-2Jg1pN2maceH7zLo7GPbzXfLTt7T0HR_h5aQ8qiEhr038FXwEljIFZioif0zhQnDc91KqmW_fAW5onof1J0r-dTH3ZewnkV7Dftw8wMAzwy9VRuWLphzpU6WcT7mcniLv7IAvWWIaNtB4fl7CnoL9RuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔹
وقتی منچسترسیتی حریف پیکان نشد! سال ۲۰۰۲ پیکان با سرمربی‌گری ذوالفقارنسب برای آمادگی در رقابت‌های لیگ برتر، یک اردو در انگلیس برگزار کرد که در بازی دوستانه مقابل منچسترسیتی موفق به توقف این تیم شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102466" target="_blank">📅 21:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102465">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bcb0e2d66.mp4?token=Tsg9YmfXVh8mLlWHnu6FpvAZ3YCtZw8-jdF6JApIw2u7GU36pflELE49Iv3NpHPiyq8jpCe9SQoeFPOjA06l5Y9f3C7D6wCPbQOUFd7K-3gdQokn2_dxO4f_zW7HfS-4WcRu0a2GyP_tvVYUDDT7Oi2_KrCYl48xtAp4a0pcGRX304lNN5U9jzREZNUQzNQqj-tNXmv0xk772y8vIIGuP7QstIj3-doNH0tQPqifOJB0b1Ar0wl4na7jMO5_XR6vChSbBx9iXoMcFeuoDZrroK9pK9St18GfW2fI1CJBR1s_b4JZHtd1b6q90xuji-StB8p_V77HRsdneuyDuzrMbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bcb0e2d66.mp4?token=Tsg9YmfXVh8mLlWHnu6FpvAZ3YCtZw8-jdF6JApIw2u7GU36pflELE49Iv3NpHPiyq8jpCe9SQoeFPOjA06l5Y9f3C7D6wCPbQOUFd7K-3gdQokn2_dxO4f_zW7HfS-4WcRu0a2GyP_tvVYUDDT7Oi2_KrCYl48xtAp4a0pcGRX304lNN5U9jzREZNUQzNQqj-tNXmv0xk772y8vIIGuP7QstIj3-doNH0tQPqifOJB0b1Ar0wl4na7jMO5_XR6vChSbBx9iXoMcFeuoDZrroK9pK9St18GfW2fI1CJBR1s_b4JZHtd1b6q90xuji-StB8p_V77HRsdneuyDuzrMbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⚪️
رونالدو چرا رئال رو ترک کرد؟ شرح ماجرای جدایی اسطوره فوتبال از زبان خودش.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102465" target="_blank">📅 21:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102464">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ed94c011.mp4?token=Sgo7Whu0iO6gUguXojeP1zC784VMSoabn4ksLm9IlQDx3Q7kf_VSfp_GYm_AlLBpF4-k8Uy8FRaq-vjJNn4r0biCIkEQrfc5IXlAFar4L4YMcqVUvrd5PT0SDI5YzE0gqEb6Mj9zkhmMBXRQGIv9S_brnahEqItecITgKjgBwrP1AxHN6eQjkla_FMXm0QAr6TDnBoDPrnAKZw6fPdqpUKyUInUS4Pydn6MubbmR3EYCRUX-PBZzHmBLzPORy9U6uWYKsP079NI_8XJ_TYiPYIdKFENSCqOsIl5s9A0qFdFlzAnhvQUSU9I2HlWcuE8Ia8e5HQIXThruLCkLgRAeQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ed94c011.mp4?token=Sgo7Whu0iO6gUguXojeP1zC784VMSoabn4ksLm9IlQDx3Q7kf_VSfp_GYm_AlLBpF4-k8Uy8FRaq-vjJNn4r0biCIkEQrfc5IXlAFar4L4YMcqVUvrd5PT0SDI5YzE0gqEb6Mj9zkhmMBXRQGIv9S_brnahEqItecITgKjgBwrP1AxHN6eQjkla_FMXm0QAr6TDnBoDPrnAKZw6fPdqpUKyUInUS4Pydn6MubbmR3EYCRUX-PBZzHmBLzPORy9U6uWYKsP079NI_8XJ_TYiPYIdKFENSCqOsIl5s9A0qFdFlzAnhvQUSU9I2HlWcuE8Ia8e5HQIXThruLCkLgRAeQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یک تازه داماد پرسپولیس را حذف کرد!
از ماه عسل برگشته بود و چهار ماه حتی توپ به پاهاش نخورده بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102464" target="_blank">📅 21:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102462">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🔵
🟠
استقلال در نیمه‌اول مقابل فولاد با تک‌گل ابوالفضل رزاق‌پور شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102462" target="_blank">📅 20:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102461">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f8b6948d3.mp4?token=hPBugHqxB2fvF9C3IiM6f532Kt4-7z50uKlwRdH4tDoSaE-mFjisluOXjFfkostKrMJQv3XD5y2fTO55D85rpo7mJRw7SgK4x1EYgffzOzwOIgZJr70euBb8Bk8K__hPhs0rvx2Czm0qtGU2d_N3FO-eULq2z2MrPIFEh8mpjB6hB0jpu-ju_P8-UUcQYRHo7Qzh7ZfCMxwiAsol71UwpIXX-6oa6nxmEPiSH_rJjLLURyfRKwRZt1X6MvO06Mn8g2_6DoCZ2a7kjeYQNG3Z0lQszEzmcFhvkq-UPGn7wksjx2OsIvVsqF4t-xpb2q_SgE7uB4ZyimNf4y5xj5rMNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f8b6948d3.mp4?token=hPBugHqxB2fvF9C3IiM6f532Kt4-7z50uKlwRdH4tDoSaE-mFjisluOXjFfkostKrMJQv3XD5y2fTO55D85rpo7mJRw7SgK4x1EYgffzOzwOIgZJr70euBb8Bk8K__hPhs0rvx2Czm0qtGU2d_N3FO-eULq2z2MrPIFEh8mpjB6hB0jpu-ju_P8-UUcQYRHo7Qzh7ZfCMxwiAsol71UwpIXX-6oa6nxmEPiSH_rJjLLURyfRKwRZt1X6MvO06Mn8g2_6DoCZ2a7kjeYQNG3Z0lQszEzmcFhvkq-UPGn7wksjx2OsIvVsqF4t-xpb2q_SgE7uB4ZyimNf4y5xj5rMNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شزنی جنس رسیده بهش و مشغول دلقک‌بازی تو تمرین بارساست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102461" target="_blank">📅 20:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102460">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ace3163b65.mp4?token=NMNNKrSjhQiENG4TKqTz6FrAhq5muZ_7dcgWUz-ON-UuGPcW694vmRWRfmitLNYo98JJZG0_UxLv6T_pBQJRQneaGdmR6oYtwqNRsMTbmHfMMqNHABaSAl-93fHD2vKjRl4bxPqj6Y7KEeFx57mqE4eisl5fSI5aYQNSjzpVp-ctpnjUIxG7FU-lKaZROw-gfuBMeLleJ8qoXvoaDwZzTbf4LWmjAtgVTpLEYMMuvK3uk9CHEGXq46lo_n5uXB4cShziJCEM1HFAUPnNZHTWiG-2PDl4IwfkFWfhMpiPwz5Pq1PZ1_PEp0nLKqa_BfTCRZMgbSigMTuX5hmNqYcnFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ace3163b65.mp4?token=NMNNKrSjhQiENG4TKqTz6FrAhq5muZ_7dcgWUz-ON-UuGPcW694vmRWRfmitLNYo98JJZG0_UxLv6T_pBQJRQneaGdmR6oYtwqNRsMTbmHfMMqNHABaSAl-93fHD2vKjRl4bxPqj6Y7KEeFx57mqE4eisl5fSI5aYQNSjzpVp-ctpnjUIxG7FU-lKaZROw-gfuBMeLleJ8qoXvoaDwZzTbf4LWmjAtgVTpLEYMMuvK3uk9CHEGXq46lo_n5uXB4cShziJCEM1HFAUPnNZHTWiG-2PDl4IwfkFWfhMpiPwz5Pq1PZ1_PEp0nLKqa_BfTCRZMgbSigMTuX5hmNqYcnFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کول پالمر:
برای بازی مکزیک - انگلیس بیدار موندم، ولی بین دو نیمه خوابم برد!
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102460" target="_blank">📅 20:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102459">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCHsCZbTDc79FPYvVkejxX16K6Xg3-ecCF66DIoNQkJrEwF4g35B6AcdpegWEkZz2lKQDb7DPpwGpfiNCiw0s7by-J02sYgcm13NoBiDdy0tM40tKNkixWjtc0nAFKWYnhigGAvmKt3c1TotgrGA8p3iGkwvKzQig-Y5R5NKSENmJLxc0bHuB-ldKG8m6fGg4h28YXR3Rhwc_DvP47ZjwmSoNPhMpCa65M-xymt9Wn3kLyyL6rnH26pKVzjg1d60tIlILxzYbJcSeIUyZGGWFXfrgdD7MACY7pp4dt2HtfnkgLjsDzIbMFRlbm305yDZMtMqK_ezfm2vqxieF0e80g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
دیوید گرافسون دبیرکل فیفا تصمیم گرفته که علیه اینفانتینو کودتا کند تا وی از سمتش برکنار شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102459" target="_blank">📅 20:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102458">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISOxgrSwPxqf_5fGXSTC8PYd3lmYR0MVUghKy3-JIkryBMoYc7o_zP9jj48ctWThDCCCZI8gdZDzK40-1htvjjr8XtBfhJzehTtx93Jssc7rari28mpimKEio2PTdtagPtxlQBE0TV4rIeT4l89cjw6KtiHNbUaiJVC-SfVLP5ee61PbkTWmgh5kGrMOHVuUnjy3DI7MEDpW0HWkFvsBmxDU54VWfyQvkRHr2Ws0w4IAahCekCpR67g05Fqvyq47j-Le0GBwr6rpxEh-qYAqVJCi_wEIngh2uTTiO2ynwCRcEdAj4Eu-ESHYkgZx07RhQkvxV1nRU7NDZ91Zaa10EA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102458" target="_blank">📅 20:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102457">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZ71NPtxvqtPnaYSJ4EtyongE9Dt7Awx9svnNhQiJ_5FEJgD6KvIot_D_17iBvKr1OhaQ1ZJfOLlN0RKxzZV9wb3YF2n-3foqFY-R9yScLC4EtpACSX8yJV89FqQbYe_xxney6c8UTseb7fu7jLtmppuFIuX97N5QbmBTr3VoVyOoUU152iDNT46rfCeSJKwMhzfiAjN-kJ6PkODl28TxiozYXmgKqeCynWhU_wbvNfxMrXSGS9OZY_qjK8c0UegTsmW6lt-RsG4Pr5J2Us-PtGOhJBxJ0aDhlQQEOpTsfsBArINtNCzIXxy97pWJz8OwvPHMHQigZTLvmgpOiYZkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
دیوید گرافسون دبیرکل فیفا تصمیم گرفته که علیه اینفانتینو کودتا کند تا وی از سمتش برکنار شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102457" target="_blank">📅 20:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102456">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🔵
🟠
استقلال در نیمه‌اول مقابل فولاد با تک‌گل ابوالفضل رزاق‌پور شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102456" target="_blank">📅 20:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102455">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovPjdyFgZ6kc2WdORHvc90hCe1K4J3lubOsbQeuWB0N9LAZfvY31tKoMV3tsvkOktaDfo6HJux0tCkYgBcRITbvcEzKAtWO9GxROkcFdFAuPPiT_uphSJ8Cqe6r9Twa4jlsgC5M00zkuxmsff6TzCNDCsV4p8RFjanJ9jWD5Lw_F0hXt_UfOZW-wHpd17cloXxUsbAu0sTgVi0_5mXhR3x-yZwTFH2pqmNaxHZVkQRxPjxTgJKZgSS7pet1KVWg2epUxypOI_X8-iNszOxfurwHHo6iGR-ecb08M2zF_vqhLciwwNbIC_1b-AG6xvw80S6Zlc3G5dG_mpK5FzTf2wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟠
استقلال در نیمه‌اول مقابل فولاد با تک‌گل ابوالفضل رزاق‌پور شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102455" target="_blank">📅 19:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102454">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHZUjjA4SQwdccfq6GIZtc1SxP9IeAzhlPjWIp04NNcinYRACN3Q2OXKT8TdfqrOXlPZ_rYNUMsrukZWgX_3mzIMPc8b1ck8HrHHh5ZpwOObfGaWYWlhrjlRj-Hd1Qwvrfxn3q1gb4jCKcPhbP47gkO2M3kxSzncNadGupPYd4e6M_z5-nsklN7SS65VS0CsNUkdLAqE-UrS01arMD7esJbwhzkYhd-YPc2ikKcFmbgF3IrC2bnvxcqs7AffjLulGJ5Pa0X0OSoCcXfZrJxL3RS_Uq8aA2OW8uFIgjuKSlxjEA7w8U-ekHEllR2uhRJ0sZh51JGydbEk4Y0E4ybWRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇯🇲
وینی و عشقش تو تعطیلات در جامائیکا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102454" target="_blank">📅 19:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102453">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
📹
🔵
🟠
پخش زنده بازی دوستانه استقلال و فولاد ساعت 17:30 از لینک زیر
👇
https://t.me/+E5pLb4kNVJZiOGI8</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102453" target="_blank">📅 19:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102452">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">کاسمیرو به همراه خونواده که دیروز به این شکل بعد از معارفه عکس دست‌جمعی گرفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102452" target="_blank">📅 19:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102451">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guCMWSY3ZcT-RqGniKQUcuOgEyEbRj78kGUiGeRBhymuMLuw8wZgcih2lX5giV1v7fSsiV2Duelnn7LFlpEjnmmvKYbCWmuebqdCvRoSKI3btE38TJxluG2HJTLG_zI7ayxILCFk3ZyQ0zeGU20fhCeycEoN6Al1sFk2JFWzTAJyoydqiK_erOnru44Ot6NQH86P4OyrcOzP54yysKFQBe_c7h84Pss8FGaamR61VPWMTJOsXdUOom-fd1PI5vqhvaCOadAAzAKFaYINRBeV_dGXTvXkeSB_R73TzMHcJKC-bDU2XEbLAsmzS812wGOuhzb52BZ-Babh9rlOTG_4Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇪🇸
رسانه ESPN برزیل: رئال‌مادرید هیچگونه افزایش مبلغی در پیشنهاد تمدید قرارداد به وینیسیوس ارائه نمی‌دهد و پیشنهاد فعلی همان آخرین پیشنهاد تمدید قرارداد است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102451" target="_blank">📅 19:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102450">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUCL30HIm_2hDqaotSEywJepJ0i3g41iUaJQYeYh4zzrwetVa8N0Dba6hnCMZms9iFS6eE-9FhA1CaDeyTbpJsJslWZ_jHkJJGj5zelETRWzMKhVIMqljkcYtCx3eEUvVX-jC1MWtMcmI0qkI8gtRpEObuxzi8b-xdpfZ_KK2O-r7Hx_eau2HkKUHCG1Q6RaVayMoinphCuCKBcof1P9ECw71zZ9qIhs5nBMGeMAyH_jO4xMMLOUTGqWzlxM2eLNSl5K3zPkKdY5p7Sl8yIKsodzRy6E9PG8wuhrMJ2Yc2G4jLVkLYVddDX3bsx-lGBhNvYAMGiZqoJ998cpidQ0LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🏆
اینفانتینو: جام‌جهانی ۲۰۳۰ بهترین دوره از تاریخ این مسابقات خواهد بود چون در کشور زیبای مراکش برگزار می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102450" target="_blank">📅 19:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102449">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhnWJBzPmNjfG_u2osTyNCOZsr6Jx4UTrO9auLqTuhk0KHPnSI3mO8MRQPVood8_1RaeEcORXYn8g1Y3vHvFJi5Y89TusJph1Htx-CF-OlMXHHCnEp5RCEDG45zWpG4aghFL8adv8TeVZ2ysjwMW_2ZDOji9GhzNknh2D8F0epIpm_qYGRz9j_ZcCwg8liwImDPKEiW0Wg9Tj7xYIrbClzm4od8Fjvnxn_HqgvOjctBitB1S9lOvMV_927lEHr2sTpIJic_DUtY8fjykv_NQWpqO4s_JRXR-0pYe6mUCiXQ7Vu_4Nw9j13AMGQZJ6KAdW0QCn3rv744-Uz9foOA1Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوفیس تعدادی از بازیکنای فوتبال
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102449" target="_blank">📅 19:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102448">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzFR-6GIPsx17nrNvBlJ3zBm4BojGv_hESaMe9tF9KW1gj-Vb0hqoO-xXbkGoc6dG_2Nk93cTyVHVrGYIZmnvlbPnpxDwcg08BXHNN0bU_COmqkR1oy_69ONycQVRcAikKUXxhloKulsKuoh-LBjrCT8bl0QrWasQjrnYJ7cqEd4cs1tnbr3JSpYcO_iEU9aNRR-BMrQia7rmlkvb-CLF5957ovTw4BUTreK0o2nGrOQzF4NQbdXSx-DQouH5mWWIfQgyvEWoYZJX3XC9Oahg7a4-RoSMdGfEWQeFxEh7-TZ8KD-_kGKCO-T1ycrBMZmqr7i2N3APKNNyRMzTeNq5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
اسپی:
انتقالم به مادرید خیلی یهویی اتفاق افتاد و همه چیز خیلی سریع انجام شد، رویایی بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102448" target="_blank">📅 19:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102444">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TJ9KfkCVFAwOogOeX17NS80pJ1i2hhHqPZzm_vW6b0cGba56fyXAWBhgz4iqbkxq2GAe5tFsq1eSzVNUxI35b0sxIxTItHv3EpONy2UzkDHO9ib3QH_PBxgHf69Sc20ljgALrzcdFO-06ABTsZxAgl-7D9k9z4x7yUaTnYCUwwfXuAq4PmNO8xNJpgvSoWlarTJ5H6QZFX3DALOSieFBKykuxaB_HY6f-04F8NCB_n9A1zicwbLaK71vmS55kkVQ8g6LlpFgyvusr1x5IqQe3L1JI-evNiHDPNOjGKTH-VXd-mMe6soYbw7a59Q8UXR1Ef71TJ994gEy6OVuK7j3UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NMYuX20b3RPv8pJmm8_ZdZ18NbqJ7umlp89Sh22_sK4kBv3zYOalOkCMFeUoul4I3Z_ySwkj3rShSgIBcM7B5GDH8KIHDmsfrpfyEasLgroJ0O-xvkTEoxbE9oNFg3sZYSrGw2gig49Kf6qfJxakYcr7tYgpjNTdi6Rc37BIahu-TSrAOl8WFOjktyzxCP-Pkp614ThX7zMQyXhd-QWQ6p_sd5Gu-rWIPwwTey9zHYeBG2DOqLqPXfLcMrXhrEFl3vJNiv1jT4uO34n653j0ycLtCyIDRztRuljKKW-dXxQ-5dh2J14HSp1n1blOfyCZ5w6AZ1XzmQKLsR6Z2D3c9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e8RXvOsaBvSvXZS5lVjaTGy2dyrG45Qt2wuboF4_u-y8GM1GZmBHbMIXDkLC-vlOYnxtR9OKQL7qiq69g33nbmCLJCj0cKwHwbiWFKNz7Ff7qDc1L3ROrry94FXJzAAr1tbZkuUPWfX4f6PeihUWiAFuhzLd6tMQm23r4Rej7nggIpOb4s-IrbEIKcK8vSQ_klpwRdm7x4PBkeBxitRICF9TrvbxtArg9jkHvI4PG_Uq8owROA7LNW8BNzBpurepz04p20OO9EeZFljBRZ4B2qDaWT9al-ibyz8IHshyyyS-bbhTPFMT1olcOf4ElidVVI1o4WQLgAmJTySZbz96cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S81cRU72y2_bhH1i9PUUgBHmShUOxqcpR8ddlyt8sH4BAHJnAc6eIVYNKt3ywjDhsVNhttLb1dkC5NKoY6Q8L6hlmjwWsKaNehlJyDNzcAx-shfGORC1TsAohXrEY523F1VDaXNuuV9SGq0aiFlxo2jvEEvSSa9kS0SlNdfx1IA18KX9nzNnTPxxF6RI2r0Wf8xUZSXjro9Jk6w_euUMiNOTaLrHZLIiv1lndDCwxNRVjLo0mVyIn3UfuA0a2Wy0KTanD-9ohQGllm30OGtdRKMqyW2tXCrdd8ZArowjdTEvktqXBDjuqgsWHuKoF-ixH3pJE0gqP2U2VerQtKzwDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
عشق و حال لامین یامال با دوست دخترش اینس گارسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102444" target="_blank">📅 19:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102443">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JlR0r5ZFEeXgCBfjJYKJwPWYxx5lzIPRMlJK1l3FmT4SA0dI0BgD2phyVPhpH-OKvvEfkLEPoeAcf_85K-eRLycmPLoAzHHqMSLOk_fQxHZ4qdYY7mNXn5y-EJEDd4CHtW4zijwKVIBRUz-ekFRBMkEgpRskTSCL4EuQ3KSxd9Z_HT7X7CHVf2uIVN6zZSGSGfSpnZ3UNkc_6Ppgh3ybg8tBhecOg0RAH9cnzDNndMgBFgkhE35PZ0lsr1D2nvoq4XrBbVaKHD3b-CkAUmg7MchfOQbtMvc5W5U3EKDXaCxGwrWwIyVcyhqWmiFGaKKEsJJLJ1euP_RShvF16-nHRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی دوستانه مقابل فولاد</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102443" target="_blank">📅 19:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102442">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKUklcJObj6lypy45ipf_7F8X_Ci3iUpBWP1_6QHUlNmy_ms8iUAHLL9sWY_UfSe1DDnzF1xy_C88kLzuZCtD9mGuu7v8UCb2VStlZLSoI3nQKyJQ-WXsiU7anci8B9ZI5czQrlFYJ6MzqBdso3exUjk7niwvis4hdpBpcowmeAEOA6O6l-Jt9vxkwZFM_u_WwhJg74GN-n6J14y3lKbPUnmlKt4rXBzqFwsinnn0SDIVGQ0kh_s0FcVKJZx-E-iTz6yj4zEdJ3qVoi8BtMMxywbyYqw5LSeaIFUVFbqWQKpPAmNqnmXR8Ugjp4oKS9s0agb5CnMrdr6QzOZ6tT5xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فوووووری محرومیت دوپینگ میخائیلو مودریک لغو شد و او به زودی به اردوی چلسی در هنگ کنگ ملحق میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102442" target="_blank">📅 18:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102440">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZyNUJ7A4WX2i67W0XcHm2cNnSC7lmR3w5K4Qu5D2YJeR97j0TLZjSqmlxUsfOlAjSvWbgqMvRJpNMd2hYBTVOI80l5pkJwG2vWDK9O1R9I3ReSM_U-PxSH8Dc1nwFucaeCPKr7zVXmeP7q_s4U4B_UVH2ynenCWie2yj0g-sdQu1GPrj1sOCx2m_ZiLsdBZcCex78OqG9w4dOBTYrPahLYPmo5cpeaL4F2LzYlZnm4bh69C-bccz9ka8Uq7w-bXf_UT89eBKxptvnCGu7fGhRRdkjcrrA66qHHMRhFW_dOl3o_WzJh9pZz5c802kVWfBD-4E8-8f0Ca8ifKpmnHhbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/opPdQ5I8hDybo2wPsBwN0k4mER3mcn5tTQxjGZF2RGJ4nj0FQhmcMyU_XYuTHJt6Q17nSvz6CU_5SaR7AhzD-wvED5n-rh1cZUPtqEnKE5bXQmsIDVcmQvYp1Vwt_VF7aqGqQIJUW1fDkHEYmdwOP46mABNBOHY_juLShmsPHjJeI3fFR0DR7iUvrxHq7DTfDBYq8_ZOn8p_renntDW3gZ1rzVR7qzs9GtsGQXAUauUosZm8AN9UwgoPVXpbtjwMdV2SGu9OcrbPknfr9AgJWgYtKzzqdXrW1-eOCyMIF5mheXUF0VLLTcydIHlRaCi1mlT-ORa-sdQ03fjlcZGsSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیر شدیم و خودمون خبر نداریم..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/102440" target="_blank">📅 18:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102439">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5d65b7222.mp4?token=NL_bosH61kRC2OliQOKGXbnz_xk0GVXwl9yJ9NrbBPlhsmBQmC-hItNhSEYs2tuEbzADxJ1uBF12f0Ou7qJ2yjglFsKD64XkqBRABV6jgaY88yh8F_myjzaj2deIC9SoHp_qqT6eMvXNHXViVA-4pEA4EPaP300M5ypiykZVAkgxAuCkADlmWFRy9sQadwi0hNPIrpGTDCywg1p5YPjl8rdw3WAgauf1u7dj7MpR-tvaw74Zf8MrDrW0plLXtAPEupRDGdCtN1NqBvpGsXT3kakoiywEUKRq-KXFhH6FSxEieuUZhPJqLm8mxfeeXxk7OvzrGn__xn3nVPMLX1wyPrIyxqE4Mo6noazt4aJW6BKdN8qs9YiY1THC25MX780B24tUslDEBlHpiZPNDSVS-goUmYgKc1vRSAZUIQ0sQFySXBlri5IdkJtwrrBoTR3bh-g3WaT474YVoSC0l194ogyIvFRJ44fpvf-KxovmM7HTne_t7ZeVgCnLs3SGQHQ9AIrsWbwe466Qw2oqpYnBG35dj4z8LQT_cHStnZA2Mu4vqRR-9uoU86FwjxSprXiMPp9RJVFHS-GFR2p9cDsDNOfQKLJa7F3063c0s6VcfK5QcJG5hiPo7SQBtGhsuYwMWr2sDIVGOqySlGoIFFIEwDK_yqJ4TR6OndikFW5RGrM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5d65b7222.mp4?token=NL_bosH61kRC2OliQOKGXbnz_xk0GVXwl9yJ9NrbBPlhsmBQmC-hItNhSEYs2tuEbzADxJ1uBF12f0Ou7qJ2yjglFsKD64XkqBRABV6jgaY88yh8F_myjzaj2deIC9SoHp_qqT6eMvXNHXViVA-4pEA4EPaP300M5ypiykZVAkgxAuCkADlmWFRy9sQadwi0hNPIrpGTDCywg1p5YPjl8rdw3WAgauf1u7dj7MpR-tvaw74Zf8MrDrW0plLXtAPEupRDGdCtN1NqBvpGsXT3kakoiywEUKRq-KXFhH6FSxEieuUZhPJqLm8mxfeeXxk7OvzrGn__xn3nVPMLX1wyPrIyxqE4Mo6noazt4aJW6BKdN8qs9YiY1THC25MX780B24tUslDEBlHpiZPNDSVS-goUmYgKc1vRSAZUIQ0sQFySXBlri5IdkJtwrrBoTR3bh-g3WaT474YVoSC0l194ogyIvFRJ44fpvf-KxovmM7HTne_t7ZeVgCnLs3SGQHQ9AIrsWbwe466Qw2oqpYnBG35dj4z8LQT_cHStnZA2Mu4vqRR-9uoU86FwjxSprXiMPp9RJVFHS-GFR2p9cDsDNOfQKLJa7F3063c0s6VcfK5QcJG5hiPo7SQBtGhsuYwMWr2sDIVGOqySlGoIFFIEwDK_yqJ4TR6OndikFW5RGrM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
چند تا از شوت های کارلوس رو ببینید، زمانی که فوتبال تا این حد راجب کسب و کار و پول نبود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/102439" target="_blank">📅 18:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102438">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d5590fc67.mp4?token=Px90ILaEtmoZ4VEWN4E_h5MO36nkXP2bWx0PC-eisuHv9TJO6vJIbkSjTQr-NIFA8_lSZmHFz5-RVRP5oWILkzayo_Um51l1lEZwm0Ho0S3xLyEJ_8iDQ8PN4hMWVHetHXsPHSZbQBlRGaxSGCWHKKE1vcEbdZQMaV2w-xbyP8sfE0gPa5OpSsUookrUWd4B6KtI14kqlF22rxzGzeR_omLkoKTMx7wrJhJ4rZyNw8XrjVGCS5A0THEWOGQDJ51Itbi09x7Kr1foW47oS6p2urZqVumvkby5W1o_OewCcm6oyTKF4_AAo9o5YHnLSy7QavF7auKrUFRYbhLMF_s-8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d5590fc67.mp4?token=Px90ILaEtmoZ4VEWN4E_h5MO36nkXP2bWx0PC-eisuHv9TJO6vJIbkSjTQr-NIFA8_lSZmHFz5-RVRP5oWILkzayo_Um51l1lEZwm0Ho0S3xLyEJ_8iDQ8PN4hMWVHetHXsPHSZbQBlRGaxSGCWHKKE1vcEbdZQMaV2w-xbyP8sfE0gPa5OpSsUookrUWd4B6KtI14kqlF22rxzGzeR_omLkoKTMx7wrJhJ4rZyNw8XrjVGCS5A0THEWOGQDJ51Itbi09x7Kr1foW47oS6p2urZqVumvkby5W1o_OewCcm6oyTKF4_AAo9o5YHnLSy7QavF7auKrUFRYbhLMF_s-8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ویدیویی‌از وینیسیوس‌جونیور در سن ۱۶ سالگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102438" target="_blank">📅 18:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102436">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qn4SsdY9AQewL4uCZR1D8-vJnlkefTXeG1guOcdpfD8Wc9oC5Et50OitWM9n-Bo6n_uCeNdL25anKxX42sXNxujHPVTQB_v0z8XGvYHw_1HuDSMMXRjmuh3RSbSMsV3kZ3DEHWlJVq6eTICMLKPID2_Z75w1Ixrj8Gu-fD2VHQXBanakfXQe-cJlCzmTQuI_idkunXSr_-wI36Bz1fmauTDeUW3IcgsTE60ECVuHUfdgHqtjwP0EBys2tp0mpaou5W0YA4gMdN1QUJDrowSrn8E2GoN_BBQZaWEmZS14GgNvT_DNSueCzdH_jL4YD_1v8G7DvqQUPs5ev4ieYxfCIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hw1to2ZxkbQxTP3vg1s2h2Dv3PoBqlDqcK_mXIvL7f77QSueWULzLkgf9ABIuwDq6uVF1UMWIGYriwr816uy9-SujCN7E7LzgUTDxUket-6uR35SV8bDhpk9RqZc67CXRuL3lJ9Yk6rsUWOkfb0b-0aAcXDKE2-Lr4ZNrt-SIQLdY4ot6PfSKHpzrA8YUwrEE5Y3yfOYVQfIXibyXytldQUJkrIx6Pk5ggPFj82AlsAJ8GSFhLMmhxdmnT4xWlu3nvIFpzVmPctj2R4x5VSGxkc4w87ERGDK45Lkfjtyu7q-mllhxhHrndSoEvjOnioqigjPtP8MKeQN34eHAUnODg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102436" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102435">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68f9e38a71.mp4?token=tYvLQd_mVlOSopuL7Y-QA4U_-_xZQ5VDfdKXpYs8dkgFR2P-QGkVoE4FNHBHB2jjOl7VZAyoGmnhAgtp9OtcSk00PTGHXZ5ryCjO8sJxLP-1uHrwwOOcXmYlhiKdc3rnFuk81F-4tMim9oY9ErJVKD2SlW_XDRFf_j-0swebII0MNHq5lyx70crOnMSvZ5NVINlkjVwWAvXIipkdkkejCeKriTcPn8qgD0qha6106GelPYHRr2NWdaDjnGElcNpdJ0vhsjo_1WYv2iX24K6FhMrMgFBcrMXohKJkvAuzBMcGTkIQzmZq-GB3P4o54Vi4-OVYu7BAklGi4lnnMkQYVVTBIaLd-t2FTgePJzVM3Ao3ug-7BCMEBQdZ6HaBc2LmTSCem6OcRXxsxM3VZ8c2VfaSiepEyVi4Z9pRaigVLCDTcoWRDnu9lUM5LYiZNIHpnofKkXanUSsC-xbf65FDy5y-6WgI4yfUklTpkSxWfatA6bsMvS7aasQQVk7PKqaqTxVAIUZ2T4w9IkKiryBpmkmIOsQtVWbTtJRKjK0JXDQTvDAYZ4iRjylN9R4hI5TkKpzxNVdnX6D56dAkBmTDUYTEUozrTLrK-Z-IUs2UkINkgXYo1z7V3583v-DHjGJGLtZ-9OPyZFeqZDHYpaLsRACe-ajJlwebZS3npFLuzQM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68f9e38a71.mp4?token=tYvLQd_mVlOSopuL7Y-QA4U_-_xZQ5VDfdKXpYs8dkgFR2P-QGkVoE4FNHBHB2jjOl7VZAyoGmnhAgtp9OtcSk00PTGHXZ5ryCjO8sJxLP-1uHrwwOOcXmYlhiKdc3rnFuk81F-4tMim9oY9ErJVKD2SlW_XDRFf_j-0swebII0MNHq5lyx70crOnMSvZ5NVINlkjVwWAvXIipkdkkejCeKriTcPn8qgD0qha6106GelPYHRr2NWdaDjnGElcNpdJ0vhsjo_1WYv2iX24K6FhMrMgFBcrMXohKJkvAuzBMcGTkIQzmZq-GB3P4o54Vi4-OVYu7BAklGi4lnnMkQYVVTBIaLd-t2FTgePJzVM3Ao3ug-7BCMEBQdZ6HaBc2LmTSCem6OcRXxsxM3VZ8c2VfaSiepEyVi4Z9pRaigVLCDTcoWRDnu9lUM5LYiZNIHpnofKkXanUSsC-xbf65FDy5y-6WgI4yfUklTpkSxWfatA6bsMvS7aasQQVk7PKqaqTxVAIUZ2T4w9IkKiryBpmkmIOsQtVWbTtJRKjK0JXDQTvDAYZ4iRjylN9R4hI5TkKpzxNVdnX6D56dAkBmTDUYTEUozrTLrK-Z-IUs2UkINkgXYo1z7V3583v-DHjGJGLtZ-9OPyZFeqZDHYpaLsRACe-ajJlwebZS3npFLuzQM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
درگیری کورتیس‌جونز، سیمیکاس و سوبوسلای بر سر بازوبند کاپیتانی لیورپول در بازی دوستانه اخیر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102435" target="_blank">📅 17:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102433">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SHGFjlRM0k91qyj3jxkslIeALbsmHym5bw8u4BxJWTsVYsKbL-lSKnld29vpxG_CNCR6izmrFHhYwfE6oElavbxGdl-KZXVwIrbQDmV1woryCbQGRHu7n81IE1vtwTdl088-_wsxpbviuhg7GP-nzKTsWp-D0YPVmpQIjpO8vxpSboahOcxrB_z1ofjxX3yxLk8CxUO4WDpXEI_8z7Qk5xVxCg8oO6em8c2TSsoVlbBlyoDSpKBJJshzz3shIRWzGzj80SakrvL9tJxGdfnoli5eofiFaoXMmHGqGbysymPH6_4ohaEDPBihi-Ub62H6uO-PmQx7bkrtPLbrtfYilw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E5tpNYjC2DZr42CjrWHPArgsPWOu1205UMxbRj-y71m0ong_9wEZYACjP_MH5hsDJoVZ37REi_1DLkzUPZhpa0zRcfOf2NtGdubu8q6aL1_TASxqGCuVhrLXuo7gZ2GZv4pWurwMhOkeVo7_U-zNkR5OIy0znL4FnIUgUQ6aJnKqUcj1Ex5YAmrfnVp3VwAPi71Z9DmJa0ti-gH-ZXEClzkD1VrMNfQShdajWE6x50Htpi9F6KJhE6wzQ6nXWMr-duqmabjCAooezXO__IYEzuZSLhu2KROKeWgYh3wtxvAfVL-hm5tTJBpnabBlZwOc8HeW0am4TxSPvGsJjHNBWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
ال اسپانیول:
پرتغال و اسپانیا اعلام کردن اگه اینفانتینو پیشنهاد خصوصی سازی جام جهانی رو پس نگیره از میزبانی جام جهانی 2030 کناره گیری خواهند کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102433" target="_blank">📅 17:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102432">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96363baca3.mp4?token=jm0kovsUuqwCdyqTaehAV_plmKmJtbVopZHJa1Od0IVRLKaZt981NRNlgit_AI9n8ABeKzs40wgaL3VQoM901LkTvFstjEqD1qyxeqXcrU3w98c-5kcl-asysH0O3aN6VWbdDnp7LM0lXNuGXsWiFyzMT7cj5-NHdys6zJe0628WFsN9pzJk_hiQVUAUhP_sA8mGtaxuND_mq1l_9_5CjjMwAJmhPf2OUwpEuNi4xn0EHYjfdFaJ5PSK1WeEEfKNWSkdB5wBQ2KxeNQWp8T3RNtlA51dUHdx2V7-Y1oGNzURY3zR6oObDgtkG-0DpTYyaxiyAIrUcjsDIqgH5j3pbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96363baca3.mp4?token=jm0kovsUuqwCdyqTaehAV_plmKmJtbVopZHJa1Od0IVRLKaZt981NRNlgit_AI9n8ABeKzs40wgaL3VQoM901LkTvFstjEqD1qyxeqXcrU3w98c-5kcl-asysH0O3aN6VWbdDnp7LM0lXNuGXsWiFyzMT7cj5-NHdys6zJe0628WFsN9pzJk_hiQVUAUhP_sA8mGtaxuND_mq1l_9_5CjjMwAJmhPf2OUwpEuNi4xn0EHYjfdFaJ5PSK1WeEEfKNWSkdB5wBQ2KxeNQWp8T3RNtlA51dUHdx2V7-Y1oGNzURY3zR6oObDgtkG-0DpTYyaxiyAIrUcjsDIqgH5j3pbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/102432" target="_blank">📅 17:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102431">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">💥
🧐
رونالدو، پسرش و جورجینا درحال عشق و حال در گرمای تابستونی اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/102431" target="_blank">📅 17:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102430">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e703311f9.mp4?token=iOmrBThHOR6-YcUIYgfTvKLnrLmCwLlNiVExaCOECga4dS-y8Fga6QVQENqPQEqS3fZl3qxHkP-k5R7DUOPDSBiHEJUblhk8dq79mlkPy3uTMd_960RkVK7vGP-PJIG1ww9-6DVymJkbpauf3qh56kvnprGG3RExyxV46zDcvqXIE8mYhI0lLL-U6Z5zY8Jo_ZI-LWLRZcPUHFwGUPFfJ9FJlxFPlY3sF56ec6JeVchAACmz3cEqs-rMmbK1s_T5566LKoC6zy6kgBkTuKYhgAjL5Yek2GHCrUTMRYmShM5bhZnz-9QUO6Iyz_zky_bda7rn-0xH90x_Rb6rlbL3KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e703311f9.mp4?token=iOmrBThHOR6-YcUIYgfTvKLnrLmCwLlNiVExaCOECga4dS-y8Fga6QVQENqPQEqS3fZl3qxHkP-k5R7DUOPDSBiHEJUblhk8dq79mlkPy3uTMd_960RkVK7vGP-PJIG1ww9-6DVymJkbpauf3qh56kvnprGG3RExyxV46zDcvqXIE8mYhI0lLL-U6Z5zY8Jo_ZI-LWLRZcPUHFwGUPFfJ9FJlxFPlY3sF56ec6JeVchAACmz3cEqs-rMmbK1s_T5566LKoC6zy6kgBkTuKYhgAjL5Yek2GHCrUTMRYmShM5bhZnz-9QUO6Iyz_zky_bda7rn-0xH90x_Rb6rlbL3KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b472a6619e.mp4?token=uQb3j4LYlmL2h17VP_rn9INpXqKMuScPsNCOLDExGEtfEEu6iBUPPZLnxZd3b8Y3i78rRpL1ElkdPiiELW2f0_U5Bc6r32min9o2s_gPpVsvVEnm32slZqkNPGcRaGbccrZIgEaEoLg3qhgxkaVux6sXKcJO80R6ruPvoaG9HaY6sy3VV9ey-_roTZ8XkEJAZfbcD0xEJ7ajBpW-jLgHQazCyH2sSzzW47sbi-tzWezonFsCQ_y1z5yraESR5pZb9mXHS35ZTdq6ATLwcwoh81FKYobVy-jmNjLF9FgcHW4lff7CN5pxywJCrVPSy9AoNZSbwnemtj_IlpK_QpY3pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b472a6619e.mp4?token=uQb3j4LYlmL2h17VP_rn9INpXqKMuScPsNCOLDExGEtfEEu6iBUPPZLnxZd3b8Y3i78rRpL1ElkdPiiELW2f0_U5Bc6r32min9o2s_gPpVsvVEnm32slZqkNPGcRaGbccrZIgEaEoLg3qhgxkaVux6sXKcJO80R6ruPvoaG9HaY6sy3VV9ey-_roTZ8XkEJAZfbcD0xEJ7ajBpW-jLgHQazCyH2sSzzW47sbi-tzWezonFsCQ_y1z5yraESR5pZb9mXHS35ZTdq6ATLwcwoh81FKYobVy-jmNjLF9FgcHW4lff7CN5pxywJCrVPSy9AoNZSbwnemtj_IlpK_QpY3pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
یادی‌کنیم از بازی تاریخی ایران و قطر با گزارش جذاب عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102429" target="_blank">📅 16:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102428">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfd29d0ef7.mp4?token=RnEwDJr4JpZaIAMsLecMDrz4YKLBOUbvioTvwc903AWw3yrZDmNc9MPxa8SWVUz2yGkxKuodVnqdo5x2duq1QJDXZZOAz56OVrAXd_ocDvt1q15CuS74-BTrPWzRw73Fhnk01TauS3FCFkkY5w2jXgjhh756a_NFlXGhAWooHUCBMzlFBlLsqpGD-StxZzyG4VjxqxIUqYBubwtXID7fkCmTHZjTntYLEWHaaijI5phObLuS1u9W79HETE1oB5ulYFD8QxcOrA5jgktohbBC71hM_O03N0gZhV5Rmj9AINlZYb0hTPSrDKUkr6mPVmt9EB2MgrhHZUtXJuv6x13JBYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfd29d0ef7.mp4?token=RnEwDJr4JpZaIAMsLecMDrz4YKLBOUbvioTvwc903AWw3yrZDmNc9MPxa8SWVUz2yGkxKuodVnqdo5x2duq1QJDXZZOAz56OVrAXd_ocDvt1q15CuS74-BTrPWzRw73Fhnk01TauS3FCFkkY5w2jXgjhh756a_NFlXGhAWooHUCBMzlFBlLsqpGD-StxZzyG4VjxqxIUqYBubwtXID7fkCmTHZjTntYLEWHaaijI5phObLuS1u9W79HETE1oB5ulYFD8QxcOrA5jgktohbBC71hM_O03N0gZhV5Rmj9AINlZYb0hTPSrDKUkr6mPVmt9EB2MgrhHZUtXJuv6x13JBYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیاز بود یه آیتم جدا برا لحظات تاریخی فیروز خان کریمی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102428" target="_blank">📅 16:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102427">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d17c8ef3f2.mp4?token=nS9rWjGO0B0zxYVWnpBIRyLCcA5n7wI4V2Bq-utI2B2lDST7oyaFWdtItctRlF6SQvu6KO_fWdpq-qsTB7IcyayeIY_envsXXLRGyZOiwZAOpUyG_ejH5yZM5FR-VsxvSc133CJoAvRSawEJm_3vXOfbLiJORhuuaHiCLCcknujAG4eLtoqhOSsRoEqhTzWGuZ_WM0QV_EEnPaa6NQ7L9gStadRRNem_NqdXz3SY4s4G7ynsEJ6acpdegZ_Agl5rQvwyXPuvMrAQclIGwGoFwHqSf0RKW97F-AZ7PRXsVmMKg3KEj1TDhlWFV4Ltz6ku03L_boubNW-jn8q1gQlzYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d17c8ef3f2.mp4?token=nS9rWjGO0B0zxYVWnpBIRyLCcA5n7wI4V2Bq-utI2B2lDST7oyaFWdtItctRlF6SQvu6KO_fWdpq-qsTB7IcyayeIY_envsXXLRGyZOiwZAOpUyG_ejH5yZM5FR-VsxvSc133CJoAvRSawEJm_3vXOfbLiJORhuuaHiCLCcknujAG4eLtoqhOSsRoEqhTzWGuZ_WM0QV_EEnPaa6NQ7L9gStadRRNem_NqdXz3SY4s4G7ynsEJ6acpdegZ_Agl5rQvwyXPuvMrAQclIGwGoFwHqSf0RKW97F-AZ7PRXsVmMKg3KEj1TDhlWFV4Ltz6ku03L_boubNW-jn8q1gQlzYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
▶️
رکورد پرش سه گام جاناتان ادواردز (۱۹۹۵) با ۱۸.۲۹ متر ثبت شد و ۳۰ سال پابرجاست. این دستاورد استثنایی در دو و میدانی تحسین شده است. ادواردز در مصاحبه اخیر بر تکنیک منحصر به فرد و هماهنگی قدرت و تکنیک تأکید کرد. او پیشرفت رشته را با شکستن رکورد توسط نسل جدید ورزشکاران مفید می‌داند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102427" target="_blank">📅 16:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102426">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/543e2ce52d.mp4?token=X5dN-ZlHtboN07LIrO5ULwfhzgt5VZolIzOkYtP6R-tlXNvpIt_Gx7tkYjGUpyUcNQ0QkRVIlLKxQAmQTqzV6Rd6l3CJ8N7qy8Z2WLELYtAAdEK5TuX_GvEM2iJzmM8uVaVoAV0Yl5KUcYqJkI5oLqD23eG4yXjjFz28vRIwVaWvQ6wY-jbXhx0mvehlTyjmV7AkqW98ZDLbMUZL1ioKOb25EQO-FvXDeI3fbEwjVKiNNDATUZnwZjtDrQoWJdBTI6USRzyDi0wTsBSgwDWOZtPg0hiezH_IkNxkjIlgDvi2HqWnYl3jbfeY06gdtwp2IRFrrFI0uh3sd50jD3bd3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/543e2ce52d.mp4?token=X5dN-ZlHtboN07LIrO5ULwfhzgt5VZolIzOkYtP6R-tlXNvpIt_Gx7tkYjGUpyUcNQ0QkRVIlLKxQAmQTqzV6Rd6l3CJ8N7qy8Z2WLELYtAAdEK5TuX_GvEM2iJzmM8uVaVoAV0Yl5KUcYqJkI5oLqD23eG4yXjjFz28vRIwVaWvQ6wY-jbXhx0mvehlTyjmV7AkqW98ZDLbMUZL1ioKOb25EQO-FvXDeI3fbEwjVKiNNDATUZnwZjtDrQoWJdBTI6USRzyDi0wTsBSgwDWOZtPg0hiezH_IkNxkjIlgDvi2HqWnYl3jbfeY06gdtwp2IRFrrFI0uh3sd50jD3bd3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو کمتر دیده شده از مارادونا و فن‌پرسی
💘
💘
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102426" target="_blank">📅 15:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102425">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e43f315425.mp4?token=Py4TqFttW6Rby2RF2POndfIpn0R-5RpmNKXHrUp_MxC0iuH8pACRurlRu1qPiZBzo1wwQdJgPt0byKGMbmyxH4l8TjIWGgbHb_Mv1vOVjT4V-uqodVTPFgKvWCEGgl5MCTQN5sa0z_x38DlBgEOiD4F5bJPpQdix7XPm_CL1QtmdMm4PpKQmmY82riz-PnBPzpWqxHQIK3nBd8gF_h8HvHBPm4D_egnnuqKXOSAGiYZXANxP-qUfAKDK_JNjouKB3bbC-1IZMf7YZGSxgs98XZzYSey-2XEa7AMdUvcZG4BjFSVVmiA3elpNrhMh2mTKNXXBmKc6WPq8wFBNfui2aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e43f315425.mp4?token=Py4TqFttW6Rby2RF2POndfIpn0R-5RpmNKXHrUp_MxC0iuH8pACRurlRu1qPiZBzo1wwQdJgPt0byKGMbmyxH4l8TjIWGgbHb_Mv1vOVjT4V-uqodVTPFgKvWCEGgl5MCTQN5sa0z_x38DlBgEOiD4F5bJPpQdix7XPm_CL1QtmdMm4PpKQmmY82riz-PnBPzpWqxHQIK3nBd8gF_h8HvHBPm4D_egnnuqKXOSAGiYZXANxP-qUfAKDK_JNjouKB3bbC-1IZMf7YZGSxgs98XZzYSey-2XEa7AMdUvcZG4BjFSVVmiA3elpNrhMh2mTKNXXBmKc6WPq8wFBNfui2aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
⚠️
تجسمی از المپیک اگر تهران برگذار میشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102425" target="_blank">📅 15:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102424">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea1f4ae5ef.mp4?token=r1IHsPWJFEHraRIBXHOeZhfrpP3wiQOX_Cv8XuzwdO7QAvvAy1jjGBJ7B_-_ttxXlAxSBKz_8j_EL2g7XwctrGNLLfU3xfse6Yyg7NgEPwVPFMFQy1T5wfq9XqT-VA815_QCVlFkstJizasppXNM7D0HmTQ9toWXY0rG6xAd5zRfBmsA3BQwqrZCWKqky8zBvcxRY0YWjRHueNhAckrf3Yq48j68kR9SLD_b5pE0Wjt-QQCeoXLiyzJ69ff9EOsybSDjsTOVZOR_V5V89hfJzEwKXEnAjSw_Y7fTnCVGY3spVq2EIaRo1yH0BUrjSVwjFVv-mDXfhI6-GCOQKpSCGgX6uBzFouyvHO2tMfuh7DnlQUgPynRJZPAoh-nIqzfnF6xG57Tr7p_ECAJRQ3dxl6zhOQw7G2r1JhP1A-_U5_O2faBU7NQuxtNL8Buj5s11dX3ay9JnYhMkYMGLtT4zd5neGw0CABe43Ux2X8xqTa9A7cBOZ5-B8v0K9PSB5K2txlnhB2HTrVvh4Q8VDQmYnyE0pdd1oaGnZce4QvGiGZpnZLbVKSbp8bTD2MwnIX22TI18mwm-cUBgXtuDpBFlYi2Wggp_oSdpd4PZ9VCT9iymBck64OzulYfJrWev2xVqQZkIA_tghPgkcWs0xAaSZk9RHiF3FNdKrjSjwQ9Nk6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea1f4ae5ef.mp4?token=r1IHsPWJFEHraRIBXHOeZhfrpP3wiQOX_Cv8XuzwdO7QAvvAy1jjGBJ7B_-_ttxXlAxSBKz_8j_EL2g7XwctrGNLLfU3xfse6Yyg7NgEPwVPFMFQy1T5wfq9XqT-VA815_QCVlFkstJizasppXNM7D0HmTQ9toWXY0rG6xAd5zRfBmsA3BQwqrZCWKqky8zBvcxRY0YWjRHueNhAckrf3Yq48j68kR9SLD_b5pE0Wjt-QQCeoXLiyzJ69ff9EOsybSDjsTOVZOR_V5V89hfJzEwKXEnAjSw_Y7fTnCVGY3spVq2EIaRo1yH0BUrjSVwjFVv-mDXfhI6-GCOQKpSCGgX6uBzFouyvHO2tMfuh7DnlQUgPynRJZPAoh-nIqzfnF6xG57Tr7p_ECAJRQ3dxl6zhOQw7G2r1JhP1A-_U5_O2faBU7NQuxtNL8Buj5s11dX3ay9JnYhMkYMGLtT4zd5neGw0CABe43Ux2X8xqTa9A7cBOZ5-B8v0K9PSB5K2txlnhB2HTrVvh4Q8VDQmYnyE0pdd1oaGnZce4QvGiGZpnZLbVKSbp8bTD2MwnIX22TI18mwm-cUBgXtuDpBFlYi2Wggp_oSdpd4PZ9VCT9iymBck64OzulYfJrWev2xVqQZkIA_tghPgkcWs0xAaSZk9RHiF3FNdKrjSjwQ9Nk6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🔥
👀
۵ گل زیبا و برتر اولیویر ژیرو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102424" target="_blank">📅 15:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102423">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a3bfea056.mp4?token=UYV3zY8z2PflmyfppCI7ZF_ef88Vr1M9TiyrXNMRHXqa9X0bnEB9AUwsCMn8-lLcCKRcR4fLsdt6U0z8Su7bKq7jGnvA6eQFi-0xUTDt9LmwcpcCifRMmt4-KjUqPFMA1Eu55US0GFi6xueeu47VD8LMKQw6o3C5ne85nMErXLC3a4AmBJzZvu6Fqizrd6BVrtEC_2DQ_MFB_ri6HGfOZjxBROyeQW2vHQuggy5Mj0mIkE5GjnE6zy45InP36SHbrRN8zLNOlIF-7hOpHU9o8qMUoFuwQom2P1Lw23MCCKcY9_tHpd_9US6dwBaAw7MMwYWIRZdaO2l5Ir5LPkSQcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a3bfea056.mp4?token=UYV3zY8z2PflmyfppCI7ZF_ef88Vr1M9TiyrXNMRHXqa9X0bnEB9AUwsCMn8-lLcCKRcR4fLsdt6U0z8Su7bKq7jGnvA6eQFi-0xUTDt9LmwcpcCifRMmt4-KjUqPFMA1Eu55US0GFi6xueeu47VD8LMKQw6o3C5ne85nMErXLC3a4AmBJzZvu6Fqizrd6BVrtEC_2DQ_MFB_ri6HGfOZjxBROyeQW2vHQuggy5Mj0mIkE5GjnE6zy45InP36SHbrRN8zLNOlIF-7hOpHU9o8qMUoFuwQom2P1Lw23MCCKcY9_tHpd_9US6dwBaAw7MMwYWIRZdaO2l5Ir5LPkSQcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
سه دقیقه با لیونل مسی ورژن 2014/15
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102423" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102422">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIFS6SGbx7OC_h3DLRbl69ZbFUQqWasdihCL3-KIP3iGt0yzg51OzAbXnQBjVL2QF0Vd57dzK77RyEFFkOkD7mV8pYwKgt6ySK_iih_kd-by-jKaLoOnyJxWKUol-uhzEkYw-MJ0mvX8yTE8OT2slNSRK-icfSRWNLD1QOKHpe-8Y0xd-1f8AWGwiiatzBtELSydwwCTXjFXUdwwO6cxOegzLO6ynfNja_gHQM_aqwJ5C5doQZDA98rxSvlJ1KZ73MUTMNcebJ_P8bF9yYjWCLsp3Nao68d4n38VLhsyHJV0xRD-E8huB5UP9Oe6QAgvq8_Qch9Jtih1Y9W3H_aoog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
لیست رئال‌مادرید برای بازی با فیورنتینا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102422" target="_blank">📅 14:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102421">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOcyIdt2_T6q7dAwZjHw_woodlEExXrF8E4IDNuXDRmYQrND9QoezXDs42R-BW89haUPvRm5VhIilMOyDOe_rwtyyw_rN15MehCtAbZT3Ptd5RWQ3UwI2MHso9E65kF98Crzy5bbrFK5_gI4qho2NmIEyJjbOGA9QdO-O0K7a_OVo5Ba3A1r7qYD80iEg8g0s9SHouZBaWk8Q08fnOR0mPABOc3mrE8I5dMU7o_n8bBT48yBkSy1KzhZ5NxNjcZC83DNURrLCdj3ADrYOsyYFOf90P3cxnXwX8SJecD0V2cn8kUuSAgqpipdd5ieRvLzztdJ5-u4DXPYbN-jmXda5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
#فوووووری
از نشریه اکیپ فرانسه: آرسنال با نیوکاسل بر سر انتقال برونو گیمارش به مبلغ ۹۰ میلیون یورو به توافق‌نهایی دست یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102421" target="_blank">📅 14:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102420">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/529b07ca6f.mp4?token=XFfJqJ_klgkzM95ysEZmVIlsGhNiyssjjZAf2vOQDq2f3brObhZsYe5Zsd6_NT7rCRllrWH7HVJxy3qhBfky657uGQfDnx-4D0ZUHKgxw2w2axDdFmcFw3a-gVo2r7nAPqjiCZR2mxF6ZsCXxRQHxGhadvcd7fI4rgrDEGjPkmEgM1MpYwPWKwRW4jl1VaOImvwzx4NZFdHAKM2_XekXatZFCSlWxpTVDimOSgrKisT6I1Da0crFIzb4PxqbC3PEv7bHNW2_qSOv5HAp8nKtkIynzRokNFHHJ97WULC_hxFPakHMgZgwbvIacos5UGKSa0tMiEOr1zrhmYXsDSFZbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/529b07ca6f.mp4?token=XFfJqJ_klgkzM95ysEZmVIlsGhNiyssjjZAf2vOQDq2f3brObhZsYe5Zsd6_NT7rCRllrWH7HVJxy3qhBfky657uGQfDnx-4D0ZUHKgxw2w2axDdFmcFw3a-gVo2r7nAPqjiCZR2mxF6ZsCXxRQHxGhadvcd7fI4rgrDEGjPkmEgM1MpYwPWKwRW4jl1VaOImvwzx4NZFdHAKM2_XekXatZFCSlWxpTVDimOSgrKisT6I1Da0crFIzb4PxqbC3PEv7bHNW2_qSOv5HAp8nKtkIynzRokNFHHJ97WULC_hxFPakHMgZgwbvIacos5UGKSa0tMiEOr1zrhmYXsDSFZbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
✅
یوسفی: زمین و تماشاگر که ندارید، لیگ را پلی استیشنی برگزار کنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102420" target="_blank">📅 14:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102419">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9889076a09.mp4?token=FIp-egDBLdN2EreTefJreovVIrWV5P4njctL5FoSzkLOaSIfTAT3FiOatfiqT8QVo8bp_Cu3_yAbKxWEF_2BxTMbzAnJdB3OEMeN4fc63cATwuDICuXf0_rx5oihUAQpG2Qy05SRifzQzgE-fIFetFhMyztRyQIcovksUbQJolNz3rX5jHVoysn3WgCX1HW-UFCI3Jl5tqhGhUphTZW_OqZAwFv_0lwLXOduZ0dqkO10rpZ1F8Zd--XS6LSN2VVuGYO5kA82dJ-IVH8zB-JBvzgY93j6IDPjh5XFqYbzMt7HbQ_MVllP6SOyLFFg56ebvu1w9088DGC2MT4QUgzPqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9889076a09.mp4?token=FIp-egDBLdN2EreTefJreovVIrWV5P4njctL5FoSzkLOaSIfTAT3FiOatfiqT8QVo8bp_Cu3_yAbKxWEF_2BxTMbzAnJdB3OEMeN4fc63cATwuDICuXf0_rx5oihUAQpG2Qy05SRifzQzgE-fIFetFhMyztRyQIcovksUbQJolNz3rX5jHVoysn3WgCX1HW-UFCI3Jl5tqhGhUphTZW_OqZAwFv_0lwLXOduZ0dqkO10rpZ1F8Zd--XS6LSN2VVuGYO5kA82dJ-IVH8zB-JBvzgY93j6IDPjh5XFqYbzMt7HbQ_MVllP6SOyLFFg56ebvu1w9088DGC2MT4QUgzPqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
💥
روزی که پیتر چک آماده ترین گلر آن دوران فوتبال میخکوب شد و این اثر هنری شاعر رو تماشا کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102419" target="_blank">📅 13:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102418">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDTEkltd8moLj18MRymK9G6VQtUOk8pi-saPGeAkKfWAm1UM0isV45tjuLzBSqZMBk_CJ3zd5E1shF6yx308tR8jiuvepLvupH6P4_Oovc5QGvD7aYaxb0dtEOieyRk5wpU0MpoCO-z05_rF5pKX0xUxVHbORV5tg7Hj5SdAw6MBneeX4m8nqzXXjL9TIv3KfINGPiC3J7cG09yX9fqWFQT9eO0cejGhW3Vg_YQBJCRtqzkuN9iEJNfvFu0oXAXKmQWhclp7ODL0dG-1MmGkG-K1jJpWCmyIo_5UoyGJGE0AisvyvBXw71CdbF6XrlLaIXiwQ987-O2hNEKMPIIwdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
کارلوس اسپی تو تمرینات رئال مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102418" target="_blank">📅 13:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102417">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpz-gnjb0StKYmVMey1wo0nJf2WcV3SUejMxCUN3YzZHZeXrVqZ2SwNaFwdOXNAghke9sc5mBYjm1s3HVIRGdtYTcicvXPgtjOdg1UyMqy0r_JY60I8c42tHuxXHvfsMS0g3Tak92H8vYzIXevAvh6PxNDpVnk8lvXuuj4BdsX1DD1RYdsYkmNSi7HYTUwos-5qBZNHFEdrlKqE9Vwax_Yh208Vn0-_DRApLjOl4m46XBJ4naaAOR-c7ch8zodJgYBITFzFSrpGUvpfwwu5LWD40yRvQZiqrypT-VodNY6GrXxZEyE7unkPmzjhIcTm4rlFtgAb8WsecAK_-G1M5rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
روزنامه اسپورت: دو باشگاه آرسنال و تاتنهام به رقابت برای جذب فران‌تورس پیوستند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102417" target="_blank">📅 13:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102416">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4938ae1d8.mp4?token=d8XNz-4Uyg2JsPDgXGWUxKypgylEZDChqOg1K1m4N4De1KqzolxE_qD0Q3g_YXzh4_7OlDnpA17IyFehXZ3kfrSUePjCAAZDBbann6hlPTaLYc9gzJeTzXapUpiKOg32QEC9pV0cIOcc-Onh9BRgwnsBsyUzUjcUDi5_czUtBNs6A80S1M7YkN6k78Cnp1mYDy1RgKSXC2JD2_hR2XWr3IomeEC-Upbx7gYdJ6GNK8pfwQkcWFoO0loKdUuq4HHl9VJzj8z0U7h9VKeDc8_tlgI8WMej9_JUFulx1t9LBZ9b1DD4ozLnZiuh3jOa9ZVT8mJ9Fnw-Ezs3Etbc1Jd00Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4938ae1d8.mp4?token=d8XNz-4Uyg2JsPDgXGWUxKypgylEZDChqOg1K1m4N4De1KqzolxE_qD0Q3g_YXzh4_7OlDnpA17IyFehXZ3kfrSUePjCAAZDBbann6hlPTaLYc9gzJeTzXapUpiKOg32QEC9pV0cIOcc-Onh9BRgwnsBsyUzUjcUDi5_czUtBNs6A80S1M7YkN6k78Cnp1mYDy1RgKSXC2JD2_hR2XWr3IomeEC-Upbx7gYdJ6GNK8pfwQkcWFoO0loKdUuq4HHl9VJzj8z0U7h9VKeDc8_tlgI8WMej9_JUFulx1t9LBZ9b1DD4ozLnZiuh3jOa9ZVT8mJ9Fnw-Ezs3Etbc1Jd00Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های بامزه رونالدو از ارتباط صمیمی با پسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102416" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102415">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5029f55db8.mp4?token=m_5ilTu63ZcsZjR4T2PdDncmW9KTI3MiCrt8eMSEBv7tSy3yvfOdqILG9u5L0NrrewdHPOWwP8lEUT1yOjm3NzLESUnEQ8u0c-1OhQXhAakx1NnbrSLOuMGyJDgQttwTF0FoLfJa29UPCFHjBEYd7vp7DljDqinXf7WDHpuPrCNeuwmQ27QhCbOShJihsC4i3XVdFIOS5UKfq5NYPBzRrtk0UTpJv4wKgywmVuF0Prt8ZMDzC18OSDXs1LwwVr8gxmyWAIM8afDYpy0ji2c4yAyygxPjwWWZSMEK_e78XdG8mG2Ksu8EkcpU12Lr1b157IXGIviwHCTGYqDBjrgH_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5029f55db8.mp4?token=m_5ilTu63ZcsZjR4T2PdDncmW9KTI3MiCrt8eMSEBv7tSy3yvfOdqILG9u5L0NrrewdHPOWwP8lEUT1yOjm3NzLESUnEQ8u0c-1OhQXhAakx1NnbrSLOuMGyJDgQttwTF0FoLfJa29UPCFHjBEYd7vp7DljDqinXf7WDHpuPrCNeuwmQ27QhCbOShJihsC4i3XVdFIOS5UKfq5NYPBzRrtk0UTpJv4wKgywmVuF0Prt8ZMDzC18OSDXs1LwwVr8gxmyWAIM8afDYpy0ji2c4yAyygxPjwWWZSMEK_e78XdG8mG2Ksu8EkcpU12Lr1b157IXGIviwHCTGYqDBjrgH_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🔵
درخواست کودکان جنوبی کشور در وضعیت جنگی از رامین‌رضاییان بازیکن استقلال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102415" target="_blank">📅 13:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102414">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac78119da.mp4?token=svInd5gC167QVngV86PrEOeC-J8Ad6PihAG1WK6MzNP_RP5_SJmYnxzAWSdmlYPDAA5cnShZDQnIKeMflx0l_hxG5fxR6gBCaJvf_Lah-p74bDGsPASRYauOwScgI4F-ncjN4FeCTbFm_6Iq9fDw972UH1KHRDeRpFYmTnYICOyc3TcCT9SSgQW21b9j0l8A_ZE1hpgonyD0V2qD5tdJgt7p7hAwLwsCLvjDjbVt8kkEMgKwfevn81b-W5IXbUHZaCWpnr93emC5XwpGYP3i_h9fN-ulYRDXTGdCZmXSEeFMR67q5y7WeNJ9OwrlSbfH5ZmrneYRdTttR9vlFFlVxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac78119da.mp4?token=svInd5gC167QVngV86PrEOeC-J8Ad6PihAG1WK6MzNP_RP5_SJmYnxzAWSdmlYPDAA5cnShZDQnIKeMflx0l_hxG5fxR6gBCaJvf_Lah-p74bDGsPASRYauOwScgI4F-ncjN4FeCTbFm_6Iq9fDw972UH1KHRDeRpFYmTnYICOyc3TcCT9SSgQW21b9j0l8A_ZE1hpgonyD0V2qD5tdJgt7p7hAwLwsCLvjDjbVt8kkEMgKwfevn81b-W5IXbUHZaCWpnr93emC5XwpGYP3i_h9fN-ulYRDXTGdCZmXSEeFMR67q5y7WeNJ9OwrlSbfH5ZmrneYRdTttR9vlFFlVxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
نصیحت اسطوره‌رونالدو به امباپه
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102414" target="_blank">📅 12:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102413">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🤩
#فوووووری فابریزیو رومانو: آلن هالیلوویچ استعداد برباد رفته بارسلونا در آستانه امضای قرارداد با پرسپولیس قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102413" target="_blank">📅 12:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102412">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75b732a95e.mp4?token=WrQC1JhK1sVwSQkyb956apAChJRVItawyugsDkajvIMx2m7cgZNQGt28YWX2REjHAAhNYaRT5QUosr-MJn0a2a7hGKIXOvjZtEIvRCox7ZuS-3rYfDPIQg8TVYuBjMaGr7E98LkOSWhreXlO0ons6bl-StB2LDKAbc0Iu3M7HP_6y_6P83y1qPObJoToo6Pqtndhv-zeZu0khnDWfzx-SdxvfZntIqigaUWTq-Y8VmPtz9ls7917_Y-atJRSRMAmnBnOXE5l8u73a35TkG-2fRWI_ZdXLQaeY_kRVOj54Vvqo8fvRHP5xPsIA0XsOBeNoWOuf2wM1YAJqsBy51h3OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75b732a95e.mp4?token=WrQC1JhK1sVwSQkyb956apAChJRVItawyugsDkajvIMx2m7cgZNQGt28YWX2REjHAAhNYaRT5QUosr-MJn0a2a7hGKIXOvjZtEIvRCox7ZuS-3rYfDPIQg8TVYuBjMaGr7E98LkOSWhreXlO0ons6bl-StB2LDKAbc0Iu3M7HP_6y_6P83y1qPObJoToo6Pqtndhv-zeZu0khnDWfzx-SdxvfZntIqigaUWTq-Y8VmPtz9ls7917_Y-atJRSRMAmnBnOXE5l8u73a35TkG-2fRWI_ZdXLQaeY_kRVOj54Vvqo8fvRHP5xPsIA0XsOBeNoWOuf2wM1YAJqsBy51h3OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇧🇷
آنچلوتی: "در هایدریشن بریک نیمه دوم بازی جلو نروژ اشتباه کردم تیم رو تغییر دادم که باعث شد کنترل بازی از دستمون در بره و ببازیم..."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/102412" target="_blank">📅 12:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102411">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2964e2f72d.mp4?token=usl_jeCuAiZrr4fNto-UetMHtVW1V56G_bs9QOEchlNOB6vGC4w-Lh3VxHQlDtL1eTUvjnSOnVTdpekiKpGTlmQzDLJG6jAXIg3_tKFAF57U9BgSSptp2njj8fsctFLNg-7GHCkhZfkZnHu1Ttbm3TSi1b4pi4nPLptoO0Wv6YsOs7QDP37RCb-Y0bxwD9P-Ve7HsWfTpv5bv30fVObyq8OssXQhI05XmPakXStjCNdMaQcfQjdcZckZtYdSdqqA71o2J7npFxB35JRr-_l1Mg-vjIvOrwcpqKqP_ZYb7zAr2jpXfDvDYMnfFDtPBudrq40I3AH9ysBw15Ljj9rm5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2964e2f72d.mp4?token=usl_jeCuAiZrr4fNto-UetMHtVW1V56G_bs9QOEchlNOB6vGC4w-Lh3VxHQlDtL1eTUvjnSOnVTdpekiKpGTlmQzDLJG6jAXIg3_tKFAF57U9BgSSptp2njj8fsctFLNg-7GHCkhZfkZnHu1Ttbm3TSi1b4pi4nPLptoO0Wv6YsOs7QDP37RCb-Y0bxwD9P-Ve7HsWfTpv5bv30fVObyq8OssXQhI05XmPakXStjCNdMaQcfQjdcZckZtYdSdqqA71o2J7npFxB35JRr-_l1Mg-vjIvOrwcpqKqP_ZYb7zAr2jpXfDvDYMnfFDtPBudrq40I3AH9ysBw15Ljj9rm5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102411" target="_blank">📅 12:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102410">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b5a4f433a.mp4?token=ZX0XMJKj-5YBybZv6eS050Y6G4NktcJ7CzxWKSxTaywEKVKHWdJd0zZShR39oKTZLYq9p62v7nihkx7UJpKoUCw9bBvoZAShFIr-4RfJlBy9ZBY_XTM375SkgPuB8lU-Cs09s1L1CW7iI9Wt12JWQoYFPAmFUKLqqLvq1H7Znim_9I-YLuH8J199Pw8AsF0vKiBafShCj_G9LS5fDu0xIIgyOqap_2xH352GaFFu-E0643zAJpv42HUw-_IB-p2wXW4ErT2NmsJ1LU5b4_ALdQrcPaky-fa5dD79k_7TS9IktfycSjwK4QdyEvUUxRVCWLOpgEldAhvidJK_vYd4QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b5a4f433a.mp4?token=ZX0XMJKj-5YBybZv6eS050Y6G4NktcJ7CzxWKSxTaywEKVKHWdJd0zZShR39oKTZLYq9p62v7nihkx7UJpKoUCw9bBvoZAShFIr-4RfJlBy9ZBY_XTM375SkgPuB8lU-Cs09s1L1CW7iI9Wt12JWQoYFPAmFUKLqqLvq1H7Znim_9I-YLuH8J199Pw8AsF0vKiBafShCj_G9LS5fDu0xIIgyOqap_2xH352GaFFu-E0643zAJpv42HUw-_IB-p2wXW4ErT2NmsJ1LU5b4_ALdQrcPaky-fa5dD79k_7TS9IktfycSjwK4QdyEvUUxRVCWLOpgEldAhvidJK_vYd4QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
🔴
‼️
علیرضا بابایی مدیرعامل چادرملو: تورنمنت سه جانبه به دلیل کمک به پرسپولیس برگزار شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102410" target="_blank">📅 12:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102409">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c746b16b5a.mp4?token=RzCkqd1wndnwMQgUAB0b7tNjMm1N0Z-jLV6ij4NsvAWp4EKK3xcnLtHzj4iR6q80hxWwmbXKyXPux0We230jTzkej0muGtN0wenNU9T57Yns3vmcNWPbcWnfabHA2HSdWjeIYPE-x4XnawTfkgh8WQ9mtBejIBWa0UUb1KcLeQQfyTngoCqmrYzEo_uXquvDW7WmQjTDTDQHsfcwrei3TxjAyZ6GHEmpa3kXtYNMJjPUFv_EOThasMwhvPg52C1amhl95cfof7bbCEWYauRD0SQ8d71Y27Dt0Fg1Pu959gu-mOo80IusxhJ57-BYouEb_JVqTBs0eLoIsLmGze9dAJk8ICkdarIY2acxTF8ANvmnGD4Qm96w_qV2hc5YgB3YLRyvlVddeF1JHyNM6h4nNXpBDXdiJyL-yey2nVhD3Tea1Qa4E_gaS3rAyRuWYiwXLttyLjuYCWwmMfMO3vNkdJmNv7ZaV61IZVV5THXUmEpbyXxu4Tazzj0A6NFaIqRXOu7euuRBYdAKHhK_DcJKHH2XufFJANAZFl0vtlyktsANNIa53f7HWCrgipo-Ai3jhrvej2bSl3rakbV3buZrL8b8ai4nl2QAJzuEvmOJXSBWcUVtOfso3HlF1mZxKRZefRkutCIFTPuKbdAEG5Xx1x62ZBYNjtQHyZZRruYjHus" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c746b16b5a.mp4?token=RzCkqd1wndnwMQgUAB0b7tNjMm1N0Z-jLV6ij4NsvAWp4EKK3xcnLtHzj4iR6q80hxWwmbXKyXPux0We230jTzkej0muGtN0wenNU9T57Yns3vmcNWPbcWnfabHA2HSdWjeIYPE-x4XnawTfkgh8WQ9mtBejIBWa0UUb1KcLeQQfyTngoCqmrYzEo_uXquvDW7WmQjTDTDQHsfcwrei3TxjAyZ6GHEmpa3kXtYNMJjPUFv_EOThasMwhvPg52C1amhl95cfof7bbCEWYauRD0SQ8d71Y27Dt0Fg1Pu959gu-mOo80IusxhJ57-BYouEb_JVqTBs0eLoIsLmGze9dAJk8ICkdarIY2acxTF8ANvmnGD4Qm96w_qV2hc5YgB3YLRyvlVddeF1JHyNM6h4nNXpBDXdiJyL-yey2nVhD3Tea1Qa4E_gaS3rAyRuWYiwXLttyLjuYCWwmMfMO3vNkdJmNv7ZaV61IZVV5THXUmEpbyXxu4Tazzj0A6NFaIqRXOu7euuRBYdAKHhK_DcJKHH2XufFJANAZFl0vtlyktsANNIa53f7HWCrgipo-Ai3jhrvej2bSl3rakbV3buZrL8b8ai4nl2QAJzuEvmOJXSBWcUVtOfso3HlF1mZxKRZefRkutCIFTPuKbdAEG5Xx1x62ZBYNjtQHyZZRruYjHus" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔵
علیرضا بابایی مدیرعامل چادرملو: بازیکنان را از پای دیگ نذری آوردیم و با خواست خدا پرسپولیس را شکست دادیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102409" target="_blank">📅 12:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102408">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1b81246b4.mp4?token=hTfDp_W3Qa--rmRTY5hUPsEqYi0632tXR0DNmRz4hEVZcH-BsPUMi5m0satUgTJu8agFfe_FjxYc2NxWLLXTbG7ddPg4TMwxMZ-OaTBtEdsUxoT884FQqfzwlRpZWMNZZmHmvXZUEpb9ykLb9Gu-N3IFiH-_5GfEdnQdPHXTUaoSO5OaHCbishizOMaT1oZ9_eCwrxJJLcoRhJ5pO-E_y5pNg0kJsAsX3VBDX6t9QRyPtN-jIULsx7SiFLB7LIw9LrGNm-JYe6YSLoQoz0FqmQrSYBvqhlpyxfJpeYYK5NQ5R822CtidJheFTBrzk6rDu-teCWjKukRgtKX5knvXvaAZQhz-jwc2MCInvN2M7ozMk7hM9kipCe9S4JrkQc8eydsOQl_TbRgxxL1YPkPTG1HspqGvtz_aLJ0zittEjy2X-EMjXRK1-kUFVK3B_Kai2lKgx1OR-PJoUQd4bflVqnz60EXcgG0SyhEiqCNKOyxR5HGOeuqD3JT9okg-9BrTW1A9nFXLOA2eUtacTVlTrd0gvDNlI8QBKMwM2Xh5kP1hpyHede4dq4s1nNAykj-RC__SKPl9NSS-GlI0PvECrRBjzXFK6T4mg9nKqJtt7X84p5B5RYl7ZWi6TwUr3KwdESD484ITxreV08IYWEs49Xh0RBL_ejxYV4ORDdlarUU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1b81246b4.mp4?token=hTfDp_W3Qa--rmRTY5hUPsEqYi0632tXR0DNmRz4hEVZcH-BsPUMi5m0satUgTJu8agFfe_FjxYc2NxWLLXTbG7ddPg4TMwxMZ-OaTBtEdsUxoT884FQqfzwlRpZWMNZZmHmvXZUEpb9ykLb9Gu-N3IFiH-_5GfEdnQdPHXTUaoSO5OaHCbishizOMaT1oZ9_eCwrxJJLcoRhJ5pO-E_y5pNg0kJsAsX3VBDX6t9QRyPtN-jIULsx7SiFLB7LIw9LrGNm-JYe6YSLoQoz0FqmQrSYBvqhlpyxfJpeYYK5NQ5R822CtidJheFTBrzk6rDu-teCWjKukRgtKX5knvXvaAZQhz-jwc2MCInvN2M7ozMk7hM9kipCe9S4JrkQc8eydsOQl_TbRgxxL1YPkPTG1HspqGvtz_aLJ0zittEjy2X-EMjXRK1-kUFVK3B_Kai2lKgx1OR-PJoUQd4bflVqnz60EXcgG0SyhEiqCNKOyxR5HGOeuqD3JT9okg-9BrTW1A9nFXLOA2eUtacTVlTrd0gvDNlI8QBKMwM2Xh5kP1hpyHede4dq4s1nNAykj-RC__SKPl9NSS-GlI0PvECrRBjzXFK6T4mg9nKqJtt7X84p5B5RYl7ZWi6TwUr3KwdESD484ITxreV08IYWEs49Xh0RBL_ejxYV4ORDdlarUU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇪🇸
مشکل ایمنی ورزشگاه‌ها به لالیگا هم رسیده‌ و تیم رایووایه‌کانو نمیتونه از استادیوم خانگی خودش در فصل‌آینده استفاده کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102408" target="_blank">📅 12:02 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
