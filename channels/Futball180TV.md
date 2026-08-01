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
<p>@Futball180TV • 👥 506K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 15:08:29</div>
<hr>

<div class="tg-post" id="msg-102506">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNV_2C3tgF_LuoRxOgQn10iOFHqp12-lpyu5sCj6zzoc1zg9m_Bu0ojkH8fnX0ADUaENZe0l1ODy8yT1vngAbApcXdR45I99FPmgCaMGyvPPt2WTJy3WykcJHps1OKGR2IpBfCHmW4VgBAJnwI5QL88svnJsZ6xBVXcw-wPPRDhPD-JusxJEX8vW1qsTHgJhz-rYbDl6Qwy_T4KOmCz4SOA0fsE32iNJ1BynKzeFwBOjYpfktn4x5lL1N_Dl2_ysb3pPAzRwllEkalouXAbpwKfUC9rZROq_8Ux1pg1-aO1ZIb9knThVZ5A_kAxcOCh-bM3tc6BbsCnpCoGj9EprsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
تام هالند:
بدترین تصمیم عمرم که خیلی ازش پشیمون هستم اینه که طرفدار تاتنهام شدم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/Futball180TV/102506" target="_blank">📅 15:07 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102504">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a1fTku8wXouns6Mo_HDXaJEzmQaxqI_1vWgkHxiITZRzBISgpPmErvuYolpHQlAJCaZvY18XE8btor6ZtH2ZjoB1NQOJAYy01m73cxXnO6qZmiiQGtWQi-CKtByFUKS60mARMXdJVog6Xjh5haUcBa8_oOL2Uu26rklt2AnL3rUYrhTQT1o6OtNHLHZMyyu3ZGvxt1Jj7zM1g1bIzq9rdZfqFEk0XRORq3fqLAvrYqSISJE3fIy-l73rZjUXnhpQQv5_tFU_WBHbwewvwloTsGh2oSYaNlxliFW2G-cCfESsSbUZEfYQP_cZ20918UAPey1VGDv97kzU9QdDPFloag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qj8j7tBO5Sq_0tcFdMILZ18nyQuT_3BGfrLdq55-EEZxmlTJyVwHBs11hGx6SzJTYUb5Bp6Oh_gtirIdFV-uLbEuLST6ZSNM8Ig0EYGere8PkRNLmo3_39rGiDY5FAG04xMoONnhCMbXsqNlUD3camme2jMM4MevtDj5EAK2oWGtchTzpMyZcnO4lhDPbeoHXHEbCaJQugRL_yx4hNro7UZZ3cJXlqZY_4Dz4OJzZC5anQKIRP2_tc1GUnE7XzAc974pqeo5hYnaZGcdA4KAJNbj5zkadBnYb0b9JE3ZSyG0MwnWCCvEivwSXsYxTeveugvCPjpxkZ0m1PRabYdZiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
یه پستچی رفته بسته‌ کوکوریارو تحویل بده که کوکوریا نه تنها باهاش عکس گرفته بلکه بدین شکل یه عکس هم با مدال جام جهانی ازش گرفته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/Futball180TV/102504" target="_blank">📅 14:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102502">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rySRZayF4adT-0-oh0JNzBjdI-FfAX0BlTBHthvJp9cQ-gFIqmwEKXX9hgkBKRMmZB4HIPTKGFBx_Li_95ZGmEaFg1u-EfuhpLnjDWq3LubQDz-KSyfKFnwa4Z_EiVs1FhbwT7m9IE6nKit8MkEIwpSM9QYzY5O-s2DJXD-x6vW2yTbfNmd2y5aGQ8JnmiLBO7_hCKZCorkIhXBnHddkhteMmB2lxvg5o0V8MJFE_OripxdOY6eNmAVqPxibxuanS1oTt-taDukTl7LvyQ1lRUdie_Y-EI6R7V12LGLJNtU4RArqb2YUFAlbJI3d2B8Q5_BoPDanFrzdSESHK6ol_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Du80yLNkx_Q7p_wgn-PwHpOhnBWTopFUGhaKxi59HValggMwMhz1eIu5cEcm5Jjr9ziGAjx_hUemx1_mpphuRMxtpbZ02bMdJKaQIcUC7Rr_xnNvDqu43f3UJC7lxfuNzIrBQaN6yaqPTTDW_AJ0rRiNfjvfFFvmaUHstColpHQFz6FXjmK1vAz9_St8DsC7eXEE8nRbtuJGyTU1H7lXXL20z_sruyifNWcQ5rBUH2x6fsPqlihW_dwUWXuKSf9VxTdzrhzuYWRIs_hY2ZYtfOAFfkBC7SzUJahtX0gAOrRsE99og_DuSI46v9f7N-jHBXHU-Vf0I1f_EwSIDnuINA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
⚪️
نقل و انتقالات بارسا و رئال تا به اینجا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/Futball180TV/102502" target="_blank">📅 13:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102501">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5_UNSbE9Qu_pK2H1HNcqfmW2R2dCCRogR-IZFVCOAfymIzGPfs1GPv_HXK1eP7nzMZvtinc82IvbFDKYWAQETBrgu-RYhIqjLirTEpNcC_71Vkb1hA-Ers9yE9BeH9fwZCG2TI8IWLIaYsxT0axQrkUp9BCDfPITOQGIEvn-B65wAA4MOXJhR8DochNeg0AcYZzxcavyAa_FwmrLR1lLeVWXGZ7L7M63zqjQuje5biHYelo_5fR13lg1fiCgFjQcYjgR7yYkZiF7XQtqA1JDRPk3XPZ13ne5UohziO1lG9cUr__qeb7jXn37BpNuyUL_ifgjGmZvxkjGNhZXLqLiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رامون آلوارز:
اطرافیان وینی هرگونه توافق بین این بازیکن و آرسنال رو تکذیب کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/102501" target="_blank">📅 13:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102500">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sf8w7pDq2_8_iBSSw5wv16uoA9yT5S6kXwFj3SzB9CIKis46zEBUWTe0Rjd2EM2lGWbuNV1RKl50NYMWH11UtJtshaLIZ719Wvtm6Rfi6C_y0Tf0eSu6qntsHQtS-2gpHVTLRFEremGlfyxKKTk7SUaHgNdQSaMH5AtOXR5GurqiezDJPR3RewaCCIZ_5YIxYlZTY4nvs90m_6-UIIRAXHpPeS1VbnhiDk7VzS5gcwFdoV3sRAol70mTciHq9nhsadnENZeFxGptaY6lZW9k8RqxTIP7c874gwhif5ZxbxRgQvahv_d_fq6BT8U0h8-cG08pChTizNuQUzwg7avobg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
• کریستیانو رونالدو به یک ویدیوی کوتاه در اینستاگرام که او را به عنوان مشهورترین ورزشکار تاریخ معرفی می‌کند، پاسخ داد:
"خیلی ساده."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/102500" target="_blank">📅 12:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102499">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/102499" target="_blank">📅 11:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102498">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/102498" target="_blank">📅 11:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102497">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwRvnMfsoc2UOnS7sJYlnX2akiSBMBc0dyqn0aG4vBr4tAfdpH5zs_nYESkqgn23gWdC9cqQrA3q76StUgtE7RU-kdrEYzIP7ebH-UyKCnae8IYOrxnU9oZyb-UglwpFLq7KcuccWIn4PpVBQgc1Y4Za-X4L6s47B0xN84AWaqzCyJDTtsPrmWheJ09Mcxuc9fMh31KqKfayqpPWcvvK9rQZRHMJzjZW74zO8YW7U6ewewxNtx4UqYrUj5NU5GJOVRRoxRYHFR4GqLgidM7lJyiggDTsvTSIDgnMsfvnkyuNZx_2g-oGcPIm4kp1Tj9vzF7ONQTPm0C4wFGjcYjvRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
اینفانتینو با انتشار بیانیه‌ای اعلام کرد که طرح فروش بخشی از سود جام جهانی به شرکت‌های سرمایه‌گذاری خصوصی، به طور کامل لغو شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/102497" target="_blank">📅 11:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102496">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/102496" target="_blank">📅 11:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102495">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👀
🔥
هشت سوپرپاس‌گل ثبت‌شده فصول اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/102495" target="_blank">📅 10:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102494">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LuDUKzJs5mE5KePnwIeMi_1iQ9AbhKM0KCULlVIXto517-6VTVbIIQ7QUsAJe9EMj5aQXrvlYEePC0PCAU1_GhBElQfz9LrfibsU1vw6y8s19JnUW_5BjUJg2Fy366aKzrkTfVRJ5Fn5rW0RkBpLt8IKGJRurQEF_bhjpxmHbxksR23HjTxhQvb9lQ6o9PBYyuPc2lWnbmbhHONDBxCAl6C3bCwHHAxtNTmPr3aSLQG1GstnubTJwqVy-FloBtnD5En1_N59tbJwAiU-hPBubG5H5cW0rL2kT56CKIB6BxF0Ss-p19ygQSPCyUm8HH98GIYLZRlPxdqf5Jg_KzsQTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه آمار مسی و هالند زیر نظر پپ‌گواردیولا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/102494" target="_blank">📅 10:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102493">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvfujV1Z40npbDQYKOnmQyKyWhpoGRO_5YZ6ts1LZuQCHpVjwCfDi2YFbhq-HSrVhFhiet9LKjwQo6Qijo19cCBF42ohyO-IRJ54e1qbSeoWyfQf_EKTHU7Logz87Nx7HaM1KA9_s6GWfpmvzYHy_Ga4IsYa1aCY5KoSSjciSvpHLaDnO_s2eUK7KBd_bkc0PwQDSn6r7LieHLPO7zmqs5La6bXPpah40y0-8_yXAkpbwWoOhKKLECW8IXxpBtoyRn4eXtyybgAEpqK_xvzmbdwaaHGb6CGAvbCmFu98pWeaipP1De8y2c1Dk74d_mBR4kv1PJKf38pcfIO0S6tAhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تمام قهرمانان ادوار مختلف پریمیرلیگ ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/102493" target="_blank">📅 10:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102492">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/102492" target="_blank">📅 09:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102491">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5RQ4eI3U8Fm-COxxW8lK1aodHNFLoJsLSt-zgbKJ9NA5SVkfnQJKSv0MthjWxovUGeEbjZZqEULNyV6719LQzuVPli2ZhCXyJzChLHuUVeSjhKF0jnippBB0D48ALHSyhJ8QbTl2CiGIHRK5Nib5vG7ZRRQkzKQHyQW96CtHBlBeNZMCcyIk0q_n3pXEbCxBH7r74iZo9b92z0RT_0eDMyTn5zSEw_KCRr9VcC22t2uTNbMC2eKfLMgHKszWErD9xKlKzti6_MF9ZxpL6sUcX_ObiFtI5-5ic-ijmtKfmQdYqXb1kHYOXcpoG0IfadL2vmVbd4KjeYskQUgdbnOXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
🇫🇷
فوریییییی از فابریزیو رومانو: پاریس بازم وینگر خرید! مگنس آکلیوش، وینگر راست ۲۴ ساله موناکو به پاریسن ژرمن پیوست. مبلغ انتقال ۵۰ میلیون‌یورو و تا سال ۲۰۳۱؛
هیر وی گو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/102491" target="_blank">📅 09:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102490">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/102490" target="_blank">📅 09:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102489">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">هایلایتی‌از بازی‌جذاب الکلاسیکو در فصل ۲۰۱۲/۱۳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/102489" target="_blank">📅 09:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102488">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7q3yDIgOI6aD9ghFxhJoTVh4n0mdf0EeF7cgAIfUN5UaLBoPodJQ7fABvyAn0A2_IgWzidZd3yq5DiHSmahw9bcm1nB38TQqsMUkKNQNcA_0MuuDDfNha7Knt32VAYGrrEZvbmKYsxg6MYEwnMuARJij9-XoaotDAR0ExOgGsUY5Rm6vwpUbbpXfu8NP-tLVuY5MYgB8Ihzi5rs2f4-K4q-49zAwKwT8Bt4a8htqvVmlWMMK2OvNvvPZt6ZuNJsZwb5iMZDPRK7Q1JLYmS4wbrzCgG-d21RNsksDExh0clfkcjk5TlfLY4LJWfazfydvawqu-mfCFJNPie0lGxpuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیکنای اون ترکیب لجندری بارسا چی میخوردن؟
مسی عالیه :)))))))))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102488" target="_blank">📅 05:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102486">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eF96ltloueL5yidqKhK4m68FdV-Hf77RpL3qW0DjoSWIKRQTDvTivyZmUlrR07YqjffZYq20j3BYGtIYQ8LDLxEXOb_vHcWYmGYtFv5mkywik77SJG4uy7KMpK0f4UpeGAlNnsUNhm30l8vsK1L-Z7WoHxBFfNTHYYTrXDWTQ5jr-oP-hUYLY-VLbBaMaOHkL7L_8cLTbYAc3186RQNUpqdOOBCYSjBGDGBnlfVdUqpSdwCDmr-BQOlK0ffwhemuA9I3UgZgkop8NQR6dvhE8r_w6dNF587G1dRss8f35KzuaMOiLsXTjyjVJ6sRO4xmLZ6Feifn0NBNwZYcjPLHnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
گوئدس ستاره باشگاه آژاکس با رقم ۵۰ میلیون یورو بزودی به psg ملحق خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102486" target="_blank">📅 02:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102485">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
🇮🇱
کانال ۱۲ اسرائیل: نتانیاهو در دیدار اخیر با ترامپ موفق به راضی کردن رئیس جمهور آمریکا برای بمباران زیرساخت‌های انرژی ایران کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102485" target="_blank">📅 01:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102484">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBDbcvg28_Hz6BEMr8Yg2JZMWZmlOCkl1LZl2eaF7rQZbBY_KItzWgN-U6b0Afcs4Sa2614MML0GZ_5Ccw_4blsgTgMC3auPs1bQuZ8QzMh6E5zdKZckeI1h6esVE74t2qF3d4WNxMC8Yc9BwYVuL3G8fwdiKJcsuM58QCn3fvyl_Trb72FeRRosojDwyNjyUoSZ8_M_qO_65AFhoE58J0M36kOL_TP6BSB7pHWAvLw1UaS4E00WPc3fjwkuLw9ce9Mjd1Rvvr08OqNNm_nERHwjzSvzr7uHiK8ufIXGXfWcw8dlZSQQrcRkOyg41m_tMtnb2Zo179uLcOsEVUTgpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب بروبچ محله تامی شلبی حسابی واسه جود سنگ تموم گذاشتن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102484" target="_blank">📅 01:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102483">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔝
وال استریت ژورنال در خبری فوری از صدور فرمان ترامپ برای آغاز یک حمله نظامی جدید آمریکا به ایران خبر داده که می‌تواند بزودی در این آخر هفته (شنبه و یکشنبه) آغاز شود و چند روز طول بکشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/102483" target="_blank">📅 01:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102482">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edBSh1GaeRuz_SnJxCe5heoOIidGWrOlkBi4pdNa_Ybi_mWeqsTS61lTv2C0PauZ9jUPilccCnod-EgQAlFJ6a63Y-FItjqTHRJTaBGqcl_PQPJ8BMT5vx3n9WJS2XIoRgKL2YpY6R6XYm5qT2q-wXY2osRlAT0jxsdnigDNibr5sVcfp4SINpnH3W4nmZEb7yEVzehx3nWVJ1LwsAcaRLnSv5WskzD0mi3SIRY37VRlYAY8s5QKyYaxwymBJNjeqmUma0HB62tBaTy-NU_if1q2Nin74ynFXTSoM4LnJ8tWZa_93tmBU-J3-dbTdRdvULplIIrpoJRq7y35TJTtKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔝
وال استریت ژورنال در خبری فوری از صدور فرمان ترامپ برای آغاز یک حمله نظامی جدید آمریکا به ایران خبر داده که می‌تواند بزودی در این آخر هفته (شنبه و یکشنبه) آغاز شود و چند روز طول بکشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/102482" target="_blank">📅 01:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102479">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y1lY4nX_NS_1lGl76WSpFtpCttQvzASce0ln1DlP_oDEJRzHqR35SfCbeLIGQft_dvHjRD78kE2boANSDaMPuUAnytaSs2ajyFz1dUnqgSBYFDQlFdUPmBrIxhNbWkKiNwTydXBXV9nr4y8pm7Eb5fng0BZIFpNzmCLykbYCmPIz_ViVBYbC_j-1Qq6aVOQckY6iwK57oFiWo2Bo4_kUW8XPFFOL__cE1ugKDAQB69KslFTRKYVkrDzLpYnruDPxpqcsSZ9kzod1yjt586HPLm8aCKhSz5LFQ1I-dwacSA8c3qVsSlhTBUSCk8prnu7qHS5JCHdbVQHPxkB2VRhMXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gBoC4qO03lwN-ZQ7eQbFbimIdBUhe5fB7qogfmvdVgHIKfK3cqKoDAXNmFtD3jkUHw0oma7DSwI1kIZVcHkxrwJLVGzs_nhUjmUyOIny2iaVjLt5isJWayHswnfR58JTMlY4E3DMnz68-KY06XQabH1z0m1cPMWaORi-UpbCLlHFFjzmyQb0ylwrGPrPdS69vgHyqm9GJzPK6e6VQwbqomMg5NFbD-9pnk8M-p5zRb5oWFwU4HbtrsBpXvS6qPQbzgvtNYN-fVNS5ypCJJzY85dNTKK_rM67EEwwr2SjYC1zpGyxeue6sGQO27XOIt30d1JDgdEBBfpOFRyxNF95Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j6deKlP5xYjwdAoUOsYZWyb2kHDXxua9_mr4Ds00_R3I7P-MnO48rYPvWKHBQS2XeHUiEt_XhdDbGmlL1o9UVEd-wc2zPXhaSdFxUyw2j1H4kNVJ_IhausjpfkPpfGG_leRxuIzdbcKOtvRlBAto4CigvJphR9QpkBjMNXIW5JoigvLLTn_3JvvyVlk0qDqr-hW47z1ndexKD_KvMb-Qp6nk6RYoD8p6_m4Koq6mxh-CFl7bYEcQAVmkJjdzzmjrkTA9Tusxm_Xh2xNXAbmNsuBZN5AAb7m-T_srYURCjqm3RgOjPWfCV_ZclsioqPyDjaKLccOJhdHXWV6CmBW9Qg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
باشگاه فوق العاده محبوب آگزبورگ از کیت خودش رونمایی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102479" target="_blank">📅 00:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102478">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkFlE-owQZT6m0ZKCQa5g38KYkXzgIpfd6OM4A5hDpEaVVwkPoGGrT8iC376XAFVAzcnugZT-UKq8zcN8gBQ5j95ruR2LE2XAM3pczwIOEIJqujBdREwdIAnOWZXSv4m_405EaTlXUKMI90l0prH6VvR7Eb8HQIK_mG4CfUBcoq5NG4lHXYM-B8yu2_w81kxbew9Pmvl4ne2UjpeLF3TIZh8gJCzeRlYIeWuCSoQDeKyw63sNwkHjchVDyYgzn22FETnDpA64eOuedVTCYbAhr1HaHGt3StsMQebAPUgKCQe-XlZpZhBcl9HEDj1bB1EOAQEYLpEDbeMw8eYbfg22w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
هندآف آرسنال رسانه نزدیک به آرسنال:
وینیسیوس شخصا با آرسنال به توافق رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102478" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102477">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی،…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102477" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102476">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=E4kNSYW74YbBRh9uZuc2Q-gcRM39iC1x7xr9XrAH-D6OZFIm3bjRd-GBQc_qgevcreR0qb12mPWU9FTDIH6xW3IQYqTUY1F8D7IAz6A1LePioXiuSSlqgqosEWKTcx1XVIqORf3iD96rsaBg9kxdH6X0V6RJWa07Y6UBstW-qdAuTek1dZhU3OPN0s7LK5oiaKMoegQpgNRkIG0_J7nKmYVfcwku_IPgar_SsK3M6P5oUYZC603qKRpUnLuHboPDe5CTdsOq16Si2yNIgBm3wQFFJXkDeZolxKW3DkmPnHks9IW3wWueKLNdUofCkRlhhd5Jx_gR0q86DngLsTlzfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=E4kNSYW74YbBRh9uZuc2Q-gcRM39iC1x7xr9XrAH-D6OZFIm3bjRd-GBQc_qgevcreR0qb12mPWU9FTDIH6xW3IQYqTUY1F8D7IAz6A1LePioXiuSSlqgqosEWKTcx1XVIqORf3iD96rsaBg9kxdH6X0V6RJWa07Y6UBstW-qdAuTek1dZhU3OPN0s7LK5oiaKMoegQpgNRkIG0_J7nKmYVfcwku_IPgar_SsK3M6P5oUYZC603qKRpUnLuHboPDe5CTdsOq16Si2yNIgBm3wQFFJXkDeZolxKW3DkmPnHks9IW3wWueKLNdUofCkRlhhd5Jx_gR0q86DngLsTlzfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102476" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102475">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufscc0n3k-edWpvmgTmFn5gDG0_6E3vk3iMJBom0gejWtqkz1zmMM6IS5ZoHavqoakVydSkL6Z1asXGb77O-nhxHa-nMsoKyCMVAT4bGY_DiBRmyZT63Hxv2RNrE__e3hr9cbptvjqvRHL-xnYBtuwbLeMWgFG-AdLf5Z8mfrcuFd90e4YJyqTJ6j33PAe4HZW94AABl3AV7J3bJftQf4eNu8dQAA7QjOLqIHTUvZqO5VJHURGy6vNZ9wI0-I7tWrGiuLwrNZmfpk167mWXM-xa6QLDfFwBCXAq4FLFH_VW_6NsFoEtNmM1V8-qu7WxFqb8Vw1fQ7naZPXHaG0yKDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
بارسلونا در یک بازی دوستانه مقابل بیرمینگام شکست خورد. بیرمینگام با نتیجه 3 بر 2 در ضربات پنالتی به پیروزی رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102475" target="_blank">📅 00:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102474">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXYUBviP_F-DI0hrJmL7C3rCJsAIe6tDz99aInz0SnxiJH9-Gu3Jt-TwqaaIJs12eJsLuNb7pKZb42xGIOBL_2-nyoPF87k_nVvRtiLblORrR-i-dBqaqc8B5tYLAPcfA9j53sUzf3aIwixyJYGSIMvv2_mnt3atXxXfLnnTquajLMfUplxLPl0kLqhaUW7b5VrzXpzenAhkgh-e9uQ5GROLm9SNyJqqBlzJeGO8sZKETGStQ58R5fSBDm4Gh46-rJ3jmniJ9IM0fZ1jNr1VUjfujVV2-mR8dBuZVBtSBWbiX0_olhrKbtz8UJtPlFlgqRBIL2ONcePTpRnkungNlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری دوست دختر یامال
😦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102474" target="_blank">📅 00:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102473">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EeBCvPYP8foREWiOVWvgEQgSUMOJ-OQ_M8T3JJDkGykfWSmULbiREGeOl_oy3xxjdcKAAHh9JjpGC12TmDykAmCsxW7p9Bmglstx2z9MdJts-6Kg_sUPvwGJ11o3ccppNvzobXLCnK-gb5fS3zBCAfsgXyWJto8huSkAbfSlffeuCx57d8i7acESOfybsT91QVeDArdjqCsS80P2bTByX_cVog0IladSd79rVY5hEPdC8jHG7uzS3lCBWm7LjmNrNo4aZtfHny4DhZbXFa3C7tBFOscFojnPiS_AGo1-RcyfWSJbtb7BjG5TFSCcce-3MAyAd7NbwaQmqaBRCQRDXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟥
🤩
خداحافظی امید عالیشاه با هواداران پس از 13 سال حضور در پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102473" target="_blank">📅 23:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102472">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MX2mcLp8zNDmpaVtUsJylilTgmR_-dbg2tF9B2jB4Ywxy1Gaw7GUIs24Fd5ZSABLISu1gGwCboXTZJBjjDOh-DygocMUp_DYk--PirBt9TweRWzvb17qreNkSQvrrSpeSyvIyGTP_0y6dZY3ge9-elO1tFZD835Dxx7Ra23fyyLBoYlNoZPeoX2DqP187fILsD9mGqTrNfRoCnGYvu7QtJL-heSlBQk7y0l4vqXaraikhy16ohu7mbCNTGTTgaR6gP2QjBEOlSHP2rwqft2YxNyY66CXBQSnVtYpCHDd5LsImgM7MobvTYZUKjaxJLZs1ZNKAkPdWEmsgu4xdOA64Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
مسی و کاسمیرو تو تمرینات اینترمیامی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102472" target="_blank">📅 23:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102471">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102471" target="_blank">📅 22:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102470">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzIl1I2GVhQKQk2F4JFtYlPiK9BJjgaSfF99JUQruJTt3xzo3u-rQoYGfPQC8Ys73qHm9PcxwwG2oaJTZiYAB4JqUYoZnifzoJ-yN6l8UxAik8UtN0ZnHTCyLhyR_qTSXOaGxtxbwZVg3szpuPg5dTQJiDjW36-mDvdSqvlrPM1tiKASzFQS8_cl7nr-gWzNMHv4GKdU3pCg-S9RfLvwkXH-oSwhdHhehqFFpp2y3dcMg1-9lCgUAIbL6C34WQonuvfFjwCKYP-zxrpq29bDXQcB2Ip5iwvKJTTukO-3Vd2AGZqn84gdHiVmGz2KjJNe-qDoe-ePfZleHn_wS3b0jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ار‌ام‌سی:
مندی تو وضعیت مالی بدی قرار گرفته در حدی‌ که مدال و کاپ جام جهانی خودشو 54 هزار یورو فروخته.
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102470" target="_blank">📅 22:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102469">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102469" target="_blank">📅 22:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102468">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCfxCbOQAWFXwRbrso7jNeATnTj-iHa0PE3lGTNU7dU0MibS4yCWXajffkPqG5B5MqD67j5pZyjChf6jT385KzgrF03UC5dq1fq4_xxGyryufDPMIeYEmsvG6JvVU2q4w15GKqP-qTZyWci95Kc2JXgVvAGpBYo63tQg3bDL71ND_o8rC5z8KoacwU_U9pdILJm3B42OwHfLcgKwxAha0SnU5LnGF38-OH_h1Rrc7pj2VMRQhPl2Y-RUJSip2Q-aN90cXps14_wJFAnb1GXc9b2vxnDV2dib8m01WTmrHeFxnM4ESsrOcJrgNu-5zQEfIXKqy6lkCB6bT_MBr0R5iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
💣
بمب لاپورتا ترکید:
جسی بیسیوو، وینگر بلژیکی کلوب بروژ،
به بارسلونا پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102468" target="_blank">📅 21:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102467">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZ8SvQlDPOtjZQgsMziWLg2y4nSQe9m2Ah3a9M6KSyWxBUmLPmwSCXd1EPoy0Camqv_pZplrxNJRzN4APhK4wHwn6OL_NquVA5-Y797A25IkkHGxW7-K2gU4-kusqXtnhEd2afqG47uviCO7ngcr2yF-b7C7HJNpUsi5ziXP7xP3uhO2ruwBvgSfasom4C_-S3RIn2rNUAlI5tA5e6KGwIHikv4u68txI0DFBmgu8Ghsf2iSD2EFH_JtGrUlbp0m1E06yuv2rpV7wnYNMJ5JTo7zuEMd2rMCIfR8JCLy_Yi0ls8ne8UjT-WKIyH5lGQk-yFKmEY4yw51qdJ3YnSKoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب امشب بارسلونا در بازی دوستانه مقابل بیرمنگام‌سیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102467" target="_blank">📅 21:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102466">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f4d6d3d7.mp4?token=Gzq4nJIRqjyrj19WHz78QNajHNo5hZ9q4nQ5LeIMeSYqel2eS2S362g1NOGs8Ic6x8f8AHyZnCiPysX0jAqAX4TadqQD2fCCSp_qXg6sju7ZQ4QN4OwcqWxvvXd5AbKyGsh61-VYuo_6_vH7to37UOocBesgk5is3UmEzwd3kxkq-vxuMuz6BI00MpjNoguVEYvIM2hTlvNsSkf9sgNUjgJSZT8Nl81zTKbgCrsIYWT6Ej70Inys_dBmTHSfLX_IlGA8TVF5EZszs0WaEETvSx2b21fOg2D8fGuuqohE1phGY2xMnKdfjTHmzfcqwbgembUcL9hmPFjPv8KNNIywuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f4d6d3d7.mp4?token=Gzq4nJIRqjyrj19WHz78QNajHNo5hZ9q4nQ5LeIMeSYqel2eS2S362g1NOGs8Ic6x8f8AHyZnCiPysX0jAqAX4TadqQD2fCCSp_qXg6sju7ZQ4QN4OwcqWxvvXd5AbKyGsh61-VYuo_6_vH7to37UOocBesgk5is3UmEzwd3kxkq-vxuMuz6BI00MpjNoguVEYvIM2hTlvNsSkf9sgNUjgJSZT8Nl81zTKbgCrsIYWT6Ej70Inys_dBmTHSfLX_IlGA8TVF5EZszs0WaEETvSx2b21fOg2D8fGuuqohE1phGY2xMnKdfjTHmzfcqwbgembUcL9hmPFjPv8KNNIywuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔹
وقتی منچسترسیتی حریف پیکان نشد! سال ۲۰۰۲ پیکان با سرمربی‌گری ذوالفقارنسب برای آمادگی در رقابت‌های لیگ برتر، یک اردو در انگلیس برگزار کرد که در بازی دوستانه مقابل منچسترسیتی موفق به توقف این تیم شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102466" target="_blank">📅 21:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102465">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bcb0e2d66.mp4?token=eYrUQXZE0YysRHuKgWoWs883S-fS8WP4cMkB_575iM3-GY4lCJQTDzGWc72zV1QkDUb_A-tG3yJxBtfNvf5_LLp9fLKzwOr95CMck3CkeHtB0lPDcpThcLLI5P45NDYXz5NucCLaKw9nUQdnt4X2JVVKt2_YuAbHmCcoatrzgLlPEEu-yXQvRpKEBk1fuRIQ90B2QgyGl73H9WBck9mse4hiC4HT3yDKDcidI42fkMIPBDG5wUtPJW0zf72S6kUAEYYLni77---NpuApzlaCiDRcgmT_XpImcBhWn767xYquKvAq_GdU6VqctwTOFZ28MlRJpebtIl33-s9xk5hkCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bcb0e2d66.mp4?token=eYrUQXZE0YysRHuKgWoWs883S-fS8WP4cMkB_575iM3-GY4lCJQTDzGWc72zV1QkDUb_A-tG3yJxBtfNvf5_LLp9fLKzwOr95CMck3CkeHtB0lPDcpThcLLI5P45NDYXz5NucCLaKw9nUQdnt4X2JVVKt2_YuAbHmCcoatrzgLlPEEu-yXQvRpKEBk1fuRIQ90B2QgyGl73H9WBck9mse4hiC4HT3yDKDcidI42fkMIPBDG5wUtPJW0zf72S6kUAEYYLni77---NpuApzlaCiDRcgmT_XpImcBhWn767xYquKvAq_GdU6VqctwTOFZ28MlRJpebtIl33-s9xk5hkCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⚪️
رونالدو چرا رئال رو ترک کرد؟ شرح ماجرای جدایی اسطوره فوتبال از زبان خودش.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102465" target="_blank">📅 21:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102464">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ed94c011.mp4?token=i851gHe8in3HE7V9rZ56N4fH3OG19SxY2ec_309X0TZT0ervA6G3fmFyJnfvb-mJYpoYL77KFyHhHXlwcdss2GDpFroW6KwKMSToC8rnttzcnWh5kyMJYFrrsu7RL0na1NEes-rsNyzNQQzU3Lh4FRjuEB5MYIzXkbYN5NuGQ5Rj2OddELjNGj1smEllzxNuqsZaiFrsD1yfy1pcBHswCnwEvi6Jf_pPDTqWHD8quDk5BkH7Iv46Mh8lZPO8CEQU5qcphMR04aDeYjdZnVacpw4gYvcnCE3Q89wPWxqQ169TLatlF29l845QN8sZWFO-9x4EBdiZI0Q2x27CPEw3FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ed94c011.mp4?token=i851gHe8in3HE7V9rZ56N4fH3OG19SxY2ec_309X0TZT0ervA6G3fmFyJnfvb-mJYpoYL77KFyHhHXlwcdss2GDpFroW6KwKMSToC8rnttzcnWh5kyMJYFrrsu7RL0na1NEes-rsNyzNQQzU3Lh4FRjuEB5MYIzXkbYN5NuGQ5Rj2OddELjNGj1smEllzxNuqsZaiFrsD1yfy1pcBHswCnwEvi6Jf_pPDTqWHD8quDk5BkH7Iv46Mh8lZPO8CEQU5qcphMR04aDeYjdZnVacpw4gYvcnCE3Q89wPWxqQ169TLatlF29l845QN8sZWFO-9x4EBdiZI0Q2x27CPEw3FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یک تازه داماد پرسپولیس را حذف کرد!
از ماه عسل برگشته بود و چهار ماه حتی توپ به پاهاش نخورده بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102464" target="_blank">📅 21:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102462">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🔵
🟠
استقلال در نیمه‌اول مقابل فولاد با تک‌گل ابوالفضل رزاق‌پور شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102462" target="_blank">📅 20:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102461">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f8b6948d3.mp4?token=oIebsJM1FNiErRkcRAH8DZGY7rTvOD_okOkaXNlP1ydTzRo-9OIjng0_-uDSNiFypayt__53mmUa4lCl3NkLczMDeiDDHywDcbOWbUHo0rwIWZSJ5kiqgymYJCdS48_saKuxp5hTVgtyQJHPbarq_aA_sGPdd-0aDUyz2soZVv5sTtyqBhDUmhF3i9MQBFIkrf1JQ-O-yu8Ars9v--veie7gHLNfS_WdAwJCcuJ3x97z8-6oen_VMqFz6FIWGLqT9Mf-st4Ce87PKmavIkJPz5Z7iCFk406A7upOcvi8jKlH8QUqMFj8MNuBk2lQchtSf1N_aVJSnL-0TK7BT-zLwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f8b6948d3.mp4?token=oIebsJM1FNiErRkcRAH8DZGY7rTvOD_okOkaXNlP1ydTzRo-9OIjng0_-uDSNiFypayt__53mmUa4lCl3NkLczMDeiDDHywDcbOWbUHo0rwIWZSJ5kiqgymYJCdS48_saKuxp5hTVgtyQJHPbarq_aA_sGPdd-0aDUyz2soZVv5sTtyqBhDUmhF3i9MQBFIkrf1JQ-O-yu8Ars9v--veie7gHLNfS_WdAwJCcuJ3x97z8-6oen_VMqFz6FIWGLqT9Mf-st4Ce87PKmavIkJPz5Z7iCFk406A7upOcvi8jKlH8QUqMFj8MNuBk2lQchtSf1N_aVJSnL-0TK7BT-zLwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شزنی جنس رسیده بهش و مشغول دلقک‌بازی تو تمرین بارساست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102461" target="_blank">📅 20:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102460">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102460" target="_blank">📅 20:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102459">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ly4Hpz_s3ANpgAFOfUL7Mrx_YbeeNTUuNX6M6xXVVFscFsdPWUxWAgRm6rPwkwq6t2YjzzaqptfTuIABiw6GMz_n5mD0Ar_-IvK5ezKLfv_nTyI1W2bU3OdWlphjaqc8UJ3LVJbGp-Gxyt6SaSbtEYbCqziLX7xC13SmuBeBRDwntPpKKOcpUVfeM6SFjyfEdFH_u5iQt0aqRdF-72gjmOvEpk-oHsXcPkp_5dlt49bLbeuywRk8EepaH7oHRP01AMUmF8n7JgG3CjJ_lRZQzhR1ju5V_IenkOIcipw_KUhDIcFNAslyYzXiYykNngiG1uzTQEDRerVWJOatENMBxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
دیوید گرافسون دبیرکل فیفا تصمیم گرفته که علیه اینفانتینو کودتا کند تا وی از سمتش برکنار شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102459" target="_blank">📅 20:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102458">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpZST19q7TdtKTVpjAsMwGPIvX-kVt8wdZ7XpIlY9J8WRJTwa9qCa8ZjC08MYtRDsxDW5QefSu7zgNyYkVrEzv7a3bRHpSqjXh3uxdum5O_BZCABqSyg-sJmI1cEEE_wcyHCTjdCwKPPVYjvpwfx_ahs3tQt0-P1tbR8o1SREqUt6CZmdvQdiqy0Wb1ddeK3-aWIfdyeNth1-mya4Rme35PeMvv0NnCh11OoR9KhlZXsdwdBL-GsRV2V7npMcj4izql76HPEzKiwQ8OaW6C5tTS-JNBtvExv3OK45k4A8TWYLRKKgZ3_HB6zFw8__VkvAVUXV-e71lOjzgNT2AAOMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102458" target="_blank">📅 20:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102457">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uucAmoOri_sEoMZ_i5Z-qdBHsPF4ldf_U_CNxMiyLM04Ikb3PkacfdBHByvKZ7r2GYZhkdDqCHO5UJpP04HLSCZ4CsKNBNQs7F1cuatbpkozcidhgL1iMdNQL6qu1ttvoBITTluwMyN36lQyzQNyDduIFsIt_4N8V1WyZhfUtMa1dmWSAv_lwAHoE56WuLsvPLHX_TsCRbosNNLUjeCkGkFX2G6gL2iD08YFggLV0GsxC7tubyQ90b1RjQPpmdIP5gXf-qi2ax8sazUNMLrmbjyKlz3VhRUS4NoYzlyMVJjBieOFnbuine-U-MBePS_hhMASlieHiAw4a7ZMmLU2PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
دیوید گرافسون دبیرکل فیفا تصمیم گرفته که علیه اینفانتینو کودتا کند تا وی از سمتش برکنار شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102457" target="_blank">📅 20:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102456">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🔵
🟠
استقلال در نیمه‌اول مقابل فولاد با تک‌گل ابوالفضل رزاق‌پور شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102456" target="_blank">📅 20:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102455">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZThHlB36VClm1bCNnUuGWVdTOG8H0IOKEtLwUXBRjMije1eNyBotrWJNMDU2LbeNHiesmuUaVU7kNV1_KqmGbnVLRX7l1cmicVPz6mvMyopQTjmE3fA44kFf-syW3SpOFFJenStnCENCYHQX1WzId8ZZHolOAB8M4WvkI0HpImDza-4t2OEo5X8vGBRwKsxcZfmKETRztPeiKCMNF3phS_Z193IK3laz3Fk01Ve3ShdR-fb-T-4niLpP26qXrWzAyWsrTlOKnES3GXuHO8r64tBkFs2p9-j5zGOhHshtJ7AESVokf5CA2r-0ho-vCRL-bo7LVsTkeJ7Taksq_jpdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟠
استقلال در نیمه‌اول مقابل فولاد با تک‌گل ابوالفضل رزاق‌پور شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102455" target="_blank">📅 19:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102454">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p33oiXzZtoDWxcdEv9gyLwUAWjRiCm0PSlLHdg_e31iazVKXTgkOtY0TvjYh5_6xjWZ1IR53Xpbc8C0nppY-Izwn5BBxEu8QU5qh3mQf_x6dvwa71_yHN4gFobwTqrCPpcT8HsgpLC99D9sMFMA-A3Vy_90xhzGZrNVJ9wYMFPU9KFpc6E3uT5YSa729mX3k6g7mxLC71bGjlogQpBINSXns6JSBdqSBRwlx4X6uCmXtUYyoiDxj-ELdjIhZaB4THW7TY5wQ4xMY4bfdEpMN39RluCrAi12ZNFPPQ0hvBjGE-ww5C5yu0Qp8_JFOqmw-nqihvEeXXIgI265ezYiNiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇯🇲
وینی و عشقش تو تعطیلات در جامائیکا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102454" target="_blank">📅 19:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102453">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
📹
🔵
🟠
پخش زنده بازی دوستانه استقلال و فولاد ساعت 17:30 از لینک زیر
👇
https://t.me/+E5pLb4kNVJZiOGI8</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102453" target="_blank">📅 19:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102452">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">کاسمیرو به همراه خونواده که دیروز به این شکل بعد از معارفه عکس دست‌جمعی گرفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102452" target="_blank">📅 19:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102451">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-iQ5_C96xzDkF7TqbNjuBFxGPiRC-gGlJEOq75VWZQdj-UDclpCQuGTjSXM5Os_rISez5iIKBsAA5do_Y6oXevpNDfjVxycqS1JX0xq_-pGEvyoHkzQsLSBZDNt10ubP0xSE5HcOWiwPauz_6IqeQg7euWSmwGtQ9rXrN-6TMTdChqepU6e8o_1PbOg_ytkuZbj3SNO-R4LQB82XaVhH5LCK7MEIu8e2qHlaDd1sG1faYJT6AM8KVFVjEFY7oDvDw-HKmtxRZINW0cp7XJkjW3N8o-JiHlfCQYirQ31PTCf4RylLRO69nZOgfw224oZQ97Kfyw87obkcOb4c7YQQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇪🇸
رسانه ESPN برزیل: رئال‌مادرید هیچگونه افزایش مبلغی در پیشنهاد تمدید قرارداد به وینیسیوس ارائه نمی‌دهد و پیشنهاد فعلی همان آخرین پیشنهاد تمدید قرارداد است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102451" target="_blank">📅 19:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102450">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGzBra9_vQ8Zir-MkTlmaPIu8fWuLxAioU4FU1g7BN7p8xcYcHDv_k9fRvcTxmNUUTfLKS1K7SFGlWXqclBKRYi08smnrg2i9mzPYOHhhGVN1aHslCBjGi_T_WSxdnpzSCLynoJl1gG-Y7BzPaCUmzTnoY-1uM2fRAvOl-Z8thwUUwD1sZ_yvL93_JWYUdWi5Jpne2KVNrlzhiV8fUz9YCiO4GnAgqwlZstE0Cy0MAzShgLLlPskxOzQhiNSI_zLYQAwk9jRLYtlXQD_gr6UYgwf6vRRCIzFKXmgq44yInnraWYeLGwXiFcGXnPdSLFuvTOSONvXGkC9e44OrxQCvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🏆
اینفانتینو: جام‌جهانی ۲۰۳۰ بهترین دوره از تاریخ این مسابقات خواهد بود چون در کشور زیبای مراکش برگزار می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102450" target="_blank">📅 19:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102449">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6gEIczP7X7mKR0UQJeUxFe2NStdRhtwTd3uYKQHsbuEXca00xR1e6CKQiVzde8XrfEfaaF8lqPbEUoucP6vYwhl3EjEtZVjdCKvq_QcCFoIpndPSDuLCWeC0SXUGwcotlqAnOTx5GpjUi4rwgRswuOk3AOV_mrrQN3dboIkTXt3vflLXfUBHWwe-xWY6UjQqHG2jP-Cl49TftroFziGSwNcxBbpBlF-MkauijTd4UvJ4jwoUTcwbsjrvH1Z4RY9MaVFOH2llbw6WVUTiC0tIFZfiozL8CXjWI42oTPBlA8V5UKmgvdpIt92-UTXxLlLa8O43l3HG4l4mpsDxygP1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوفیس تعدادی از بازیکنای فوتبال
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102449" target="_blank">📅 19:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102448">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgn4B7qcAsUJnjrvEsCbfTnXJh0woPeN7gXkkNLf4zh3bGrbmBeKA4x0GyFA-wfCvbMO28LSVnzGJZFfoP6uTV8pXvkY9hfYa6dWr5o_0DcX-SK9yUEN31a45UleJWlUySidDkvzoBATqLs2DVrJN5jzlwXZhEsY_MjfslSUHp2o9tn8ljyWV6y4EDDG52Na0lnOidMZAz0g-lX5J9gFeMU0L1NUVlyoW6bNOtCYJFWbD8_aBfCWZlf_jzVs2xfspkoWEIgg3DeN-3T6nuN9WLdSMxuRKlii1C97U4__I8_eQNaN704t7tZIhwVE2s-CiX5lqyMUnb8hbi_rj9riXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
اسپی:
انتقالم به مادرید خیلی یهویی اتفاق افتاد و همه چیز خیلی سریع انجام شد، رویایی بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102448" target="_blank">📅 19:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102444">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s6zBsfSkxJj8iIdmhFc1_mqV1xKQZjCa7qsbJ2HzDhJSJvzlRPcSKiqLf3dsBsm6X7hGjy9RLffLNl2etknea3lFTO2suZ6PCfVC1zoCPB4nBZEPVYtzuItQxecq6CgwusfS0Iwx6Y35XO3uYAMv15FDUqUZykLr5TV54eoKCiW6-eFGl7MGmxLf_9eM_-38OL13iwVrmOdE4gFb9YbqJh-06vf5te--o-5ZO_13BTtF4nf6DRkUQzTq_9AbiuE5KJ7vm9bjcA_oIl-OG9V_qkA-vZbiG5ZdbAjjzFDqhF2b2yK3MJ9q0qMhFpesDKSSEw2kPmBrEq337c605E69yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S_hRjeUyjZbAbt4OVSci0vxHhdPJw-1-rWyGMwADhoVgREl4-8Wb1Tx_ib6hZ968a84_l7u65Zqlzga9btDbLAofItyPSQGgsFhe8XYmNKk2ehSnnpnXMZciPqOItLyJT_Xecds4x5Ot7s9A7km_6_iiLf4ERVliJw_M4mAjP-J3pVyA_k693KHERSJWcFMvPetnl-86oE81OrjgN7jSs9cgG00qw7-_3io5gD7xDM_XunCfKyvF7f4wPs-IyB_OT7lbnwHFubd5a4jCWCEorDkByLroszWInKdqjtpGeGRMhkT6ktgibu15DqfFsicTYIyJnAMkv_-KdnuIDNCXRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ocuwf_6icW8vwvpAbIyAMkWx8gUq5Fmm4aLVfau1uYS0bxpfSZ9kSE0H3fSm84i7TiphHGWfjb9aC1hMJ-exZUQgD5LPHhvN1-RVnmKvxoBc5pil69fF7OPyk4CJ_lziXXr9PY7A5ICzCexh88mjOlSLyZrFlx5C_sKojsRJJvsOzLfGnU2XKQDhZxVhLPuz-_qil8KxFVrUIq5VPE1sjLgkg0pzt6yBaSFQQnJ2J5DO8HHMB2bYDEw8Bu2sXHVVIs3hHkYI5vMFux5WO_Kw5LKogi69hKX8dzu6UlJ6fMRKgKkjVHdOTEl3irO-m_WrNXLc0pOkwLocj-6FU7EGBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YbKV5Z95ogBZ6IDCQiOcH7BfXt_LsFF_tMPEN6qAwRQ0RuTM4GgB47kg5TfhlYmgdtxhjxhSpUIngmm4ygtfhT3uSOO-cuudOMiqquN-8g6qCx3TH4h_SaJeeNwyX8Z3acDWQ-lscZTIT9v4YqKz7Re59nt59ZBfKVsF8F2yv-_hYOkttTfZlaCh35OHkW050bJJQdZB5F1bhNUrpzaZiZkr7Sbu5i_UjF9fZQads5oFiciLUOFMWrikBxSH6R4k6qJPSqDqxFGPsP9abf1i8ubFKsC4bLQ5pR68eGM6ddIUsmV6Th11i2FuCx29lBvNbakOkjNuEkpsCjTOfxZzag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
عشق و حال لامین یامال با دوست دخترش اینس گارسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102444" target="_blank">📅 19:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102443">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDSPDTZzUy_Gp4dRvfXR4_cxtq_d-KO8qf3f_wLPQ9oEAXD4ZMGvrfIhpcyuFG-v0ui8m0G9li_bM6VLN8_bnt7Q_kEw2_sh0vnRetwrpFvOhPyZLhrvTpfKeS8D6sDt2H_9JNSlzBrDajS9UkfVzsglQmYwWSa98OmUn2chn6U3GqgLEqYunwGbUd0gtOsVheLXWUjESagakfp9flIxmvmvBmVoSo7UNFwd6PcEClUcfZMMXGq5oXkcI3gLWgEu6ldwxVIW-5a8X5WebD2VAHz-b5vgxXU8Pqnpr7Ea-_JaZ9yji41NmLAgKsTHVxgTY1GRhrJZoe87gCmYIEXAlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی دوستانه مقابل فولاد</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102443" target="_blank">📅 19:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102442">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAVCI7CBsyY1BEPw-ZXc8GXFdMlGa2-TH_VP4IHjqnj45564cjb_Jz4kdvWSk6YFJDaZ9hbPVxiMFKSUcEHOX0NCpNx6mij6GPxWQWR3E-JtI5wdTGPqubBwI9-yLV0Y4FMlmAmU2_qKOLnGZ0nyhPh5PN4mSXLjeaGyheGrkr_GGxK6D7QjJhpAMYizdMxAbDQnHd9rjioSpNNtiO6HESj0XpuZNCf5Oxn038jkXjOsGXQsl1MmpJ5M_cocsWyPKzPxhmQtmvNJGieO5BBa5yqrdadsnaTgLxLF4YAwo9wPEvay6f24eUyZqT1JNbgffgGnKtlhsZtrN7jtkNQp-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فوووووری محرومیت دوپینگ میخائیلو مودریک لغو شد و او به زودی به اردوی چلسی در هنگ کنگ ملحق میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102442" target="_blank">📅 18:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102440">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eEcAVUxrHqOWxkQifqpbgcr5-6sKIrKpb4SxPfJ2lkGJAfCjeWcb62XncKU-jsKPs_Qb0T9gnu7wnm3gDenuRyDrWRoz-2UKS3C6HRxwvPLTTrI3uBKhFH-EIQO-J2Fi1fsB8uk39dxsSkxFQwmXIdrnfIUoZ_7UQn3XOWM1Kke5TyskLiXebAxlFFFmCCZ336furN1-PlFpiUW6obPR_ZVR4EisOnozkWf2nxdF-HAuBDANjfoShVuI5_Bags5OzdaTmOLCt5ljISKzfqnV_dWxMDY9Mllbe6Ba074l7I1Jln9Lmh8SUy2TngI1H-h2Z5oghbjZxe_mF-F8RPJ9BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H4fG_GowMoDtX8wEDCSZaUqUQmz3jmMZL-iFO8fnGxkV4RZr40GpP_1St8shkCMAX5tZX_s3gbGIAQb-fAIRhiIpPJhlQrGpvX7OcaKxoO3Vx3cMQNvFd6GsCn-wg6p4mP40Z6pdzXNtUl7MUXCdI-8xttH-p-zSTOsw1g4JWUiIkuxDBewnFhP2t1LqQDnSMwvRnci15-21gL_pSUrUvPMJCJr5YRjxlHkJQcvTnECfs5lqh1r60HtM1-uNcWaUGbVL-60CccAfK_XXoR6Fij7xlgYawgcj2RusAMtPo6aDA0sNtgqOkChndfHvIX8RurKVSg-KyiiZE1IjHDbf9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیر شدیم و خودمون خبر نداریم..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102440" target="_blank">📅 18:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102439">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5d65b7222.mp4?token=NbVKRlzhM5cL6FPH10PQjjm6-vmj4sPuLLaTmGvUVPooVo7FrFT8aPMnqaWH4rb0aD1VjCT1bfiKsB4W4S-zgN1Wn3-h_tVlVlJ4FCh1U_pPEWKiha87LNRfl_WqQGWaHTJzZTriIN3YeX3jEgzSTBlauJ4aANzQA6BtvD4zo3cLdZlJmMm8ZtaRIWxASGT3EhxC2yPUinmnMf2XqSi30J-F_aqA_ybuh6sohScemmCQT437qCo3P6ZtRZk04rTuLNXSso1ERyQEUnSS2YoC5YIoTW-SO_kJN2SP6hFdS--PTbxJ7AQadkeLZ5YZL9ZXND8Aes0Ii-IvKm9rLlOrLrv6hcjcW2KDQZ9Pc6dDaB1ZF059wMHmNdnto8Nq1kKfiylrACNhW-A2juTyGX4dHKUJna-jRShPBlhX3SVpjcNgabF9s6QxYzKzJq2XcMNjKG3Qv9Q5AZAmyMimVCirXW7wvRlqmvkKdNDEgWi6iYDPoMbxjb1_fumFb5vYlpJP7ZAhTH0IQsC6slyWDX_yFnlnkw0YOIm1E5yyKYC6oCTuk5AuAsWeYNDBrAN2n1MI6sv9gAdx-rIT9c8hjJi5qLy-V4gc5ycIXxtk-IN7KZgh5Iahe6StLsc0KvSPiYWTd5SHonYS0oYWdO0a6nx5wyKhAl2bFp3xUiWr0tY_ryo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5d65b7222.mp4?token=NbVKRlzhM5cL6FPH10PQjjm6-vmj4sPuLLaTmGvUVPooVo7FrFT8aPMnqaWH4rb0aD1VjCT1bfiKsB4W4S-zgN1Wn3-h_tVlVlJ4FCh1U_pPEWKiha87LNRfl_WqQGWaHTJzZTriIN3YeX3jEgzSTBlauJ4aANzQA6BtvD4zo3cLdZlJmMm8ZtaRIWxASGT3EhxC2yPUinmnMf2XqSi30J-F_aqA_ybuh6sohScemmCQT437qCo3P6ZtRZk04rTuLNXSso1ERyQEUnSS2YoC5YIoTW-SO_kJN2SP6hFdS--PTbxJ7AQadkeLZ5YZL9ZXND8Aes0Ii-IvKm9rLlOrLrv6hcjcW2KDQZ9Pc6dDaB1ZF059wMHmNdnto8Nq1kKfiylrACNhW-A2juTyGX4dHKUJna-jRShPBlhX3SVpjcNgabF9s6QxYzKzJq2XcMNjKG3Qv9Q5AZAmyMimVCirXW7wvRlqmvkKdNDEgWi6iYDPoMbxjb1_fumFb5vYlpJP7ZAhTH0IQsC6slyWDX_yFnlnkw0YOIm1E5yyKYC6oCTuk5AuAsWeYNDBrAN2n1MI6sv9gAdx-rIT9c8hjJi5qLy-V4gc5ycIXxtk-IN7KZgh5Iahe6StLsc0KvSPiYWTd5SHonYS0oYWdO0a6nx5wyKhAl2bFp3xUiWr0tY_ryo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
چند تا از شوت های کارلوس رو ببینید، زمانی که فوتبال تا این حد راجب کسب و کار و پول نبود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102439" target="_blank">📅 18:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102438">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d5590fc67.mp4?token=WFmHNbzL_NmVXXg8SdyMY_g2R0IAYG4ByJ9BHCf-7F_13_UDb5Yg1i3uL60Yfkxu6-vQ1aFFxRSE6g9y4SAtVN1M9koKGYbxZ-b-SNTgxb3Zo1eh4lISdfEHihYbYk0hrOCAc6rJ36TiAO1IJP0ncaE6LRV-ctE1Q-tAEjR-CSBqEFwSQg8A_okkwtKT_N0kU3X2OQ9erl7I5SGe2hRBz6XqNpgoddmw2mdJNn8Rb7pyDmRQUCmxQNn5bBWUc_8dybLabGaB5Lg5_dR48Pi-40kMIo-Vm_eeGPNo5pD1N-W5JE5CG0T8CVgrDtCOtJ-B51RU3tLCMrUK9Wj8JfLP4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d5590fc67.mp4?token=WFmHNbzL_NmVXXg8SdyMY_g2R0IAYG4ByJ9BHCf-7F_13_UDb5Yg1i3uL60Yfkxu6-vQ1aFFxRSE6g9y4SAtVN1M9koKGYbxZ-b-SNTgxb3Zo1eh4lISdfEHihYbYk0hrOCAc6rJ36TiAO1IJP0ncaE6LRV-ctE1Q-tAEjR-CSBqEFwSQg8A_okkwtKT_N0kU3X2OQ9erl7I5SGe2hRBz6XqNpgoddmw2mdJNn8Rb7pyDmRQUCmxQNn5bBWUc_8dybLabGaB5Lg5_dR48Pi-40kMIo-Vm_eeGPNo5pD1N-W5JE5CG0T8CVgrDtCOtJ-B51RU3tLCMrUK9Wj8JfLP4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ویدیویی‌از وینیسیوس‌جونیور در سن ۱۶ سالگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102438" target="_blank">📅 18:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102436">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ST0QAb1qihFsi74Z109AtI7mVtTlNHwZ_NPQ0OI5a-_3o05fHEhygITyJg-qoxjPJnpk2TobtmN0q6hSRvJj9mr6kRi5DYc70aIhMi96qwaFXpghQsgZMzgef892RCCnzH9xMel4lgbDqvL06fNvmGQmebCemUxsRKJlDgR7QgfUp8I60nNA0kMUaMPtdP8is7quyoQrta-dUO9zQ1Ny07H6yK45LTyj3zbgn1q8NTx_27gOxkdjReG0_FyX4Dcd3oN19FP5JFC9OlMdYMthQRpBt7HDV7R1ndG2zRjK_V1iruBi7zYZ5dMKNsaKUby2m5iRL59zam2ml-cHUjRfOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gJCX0Z6iDCilSg2v6Ulf5nEzCMiRCvZM9XlWjSVKA3boDKU2pdtsVu3_W4x94Li_RG7q3oiqcWDOW46p6I1vHnrlhYMX_IQzt_G_2zQDlKfsJXQxFUnfgcVkjwv1kcrnBpwLT2sR_fWbDHl44fpjm0BtoUwGI1OWrDXX7TetlMCBHDLM2DZEDnUtSX2tpNO6irEwf7M_dL5RHlaNX3VTHmrb9-QA_GHl11fceuITMKQY4L4ENIY5lU4vVrAwjk6OrFusN2AJUD2K_F80By3DMYmF0zXJQppETnk4C_5cgl1OPgRBBqMjDe5uGFM6BE8SIe8g4kW4LdJGMn0gZiKvcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/102436" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102435">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68f9e38a71.mp4?token=T1Y5EQjv1SKrN55yPBrWmIHICGCKCZ7jcdVn1Gn-1b8LRWVMzzD-YlNT1ZJFCg07Jm8aOo8BzZZjyjqACg4Qh3Tmnck4dXGhRFAEt9pyDSNGqjo7Apm19FYKTVAFCyp7XPzqAqGtg_wLK9ApVkjMrlY6rpD1iPyc4pkX4CxTgljq5XMbfsVtymFcQXs0jKockie_wjdHmZj0wGz3X-29IjQjZQIN4f0L_R2oKY65LayAn2eaUvTmB28dKYpbO1t5gat7KrR7oHYpHhrYmIvBE9SUCmKQOBDBtFpJb2r1paCyP12S8j7nQOMaMtfXponJhBqgxos9FAHtt89dvGB_KB-1Ug43UJ67Sr8ZSfN-eqe9CnEow7Xx353Lf8vKGYqTKFQAb5w-QYVwOasrYGnoqLYbQ5uP0ctqSaya4S_aw9pED0qnA92M3gZ79rXAJlkmhFBHnkZFUztapqMLL2YIHi4mZQzZKOzVXbVl6nXFyt0trtGoHsRX5rVvtsuvCSJ59EiafkJj-7fzzyPRKL90g2dJ7oCGvc_TG-VoMtL_g6p810_fpieuISbDILdQmdYH9zs5lakxBJjZxrIWltAb6DkmArDXjdyU_LHTfv9r7xfYwWFmHp0dsoQc738CS8PGK9wV2OdIAfjLpkrXszZ5rWXv3SJWtxnPhvGAodvSr0Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68f9e38a71.mp4?token=T1Y5EQjv1SKrN55yPBrWmIHICGCKCZ7jcdVn1Gn-1b8LRWVMzzD-YlNT1ZJFCg07Jm8aOo8BzZZjyjqACg4Qh3Tmnck4dXGhRFAEt9pyDSNGqjo7Apm19FYKTVAFCyp7XPzqAqGtg_wLK9ApVkjMrlY6rpD1iPyc4pkX4CxTgljq5XMbfsVtymFcQXs0jKockie_wjdHmZj0wGz3X-29IjQjZQIN4f0L_R2oKY65LayAn2eaUvTmB28dKYpbO1t5gat7KrR7oHYpHhrYmIvBE9SUCmKQOBDBtFpJb2r1paCyP12S8j7nQOMaMtfXponJhBqgxos9FAHtt89dvGB_KB-1Ug43UJ67Sr8ZSfN-eqe9CnEow7Xx353Lf8vKGYqTKFQAb5w-QYVwOasrYGnoqLYbQ5uP0ctqSaya4S_aw9pED0qnA92M3gZ79rXAJlkmhFBHnkZFUztapqMLL2YIHi4mZQzZKOzVXbVl6nXFyt0trtGoHsRX5rVvtsuvCSJ59EiafkJj-7fzzyPRKL90g2dJ7oCGvc_TG-VoMtL_g6p810_fpieuISbDILdQmdYH9zs5lakxBJjZxrIWltAb6DkmArDXjdyU_LHTfv9r7xfYwWFmHp0dsoQc738CS8PGK9wV2OdIAfjLpkrXszZ5rWXv3SJWtxnPhvGAodvSr0Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
درگیری کورتیس‌جونز، سیمیکاس و سوبوسلای بر سر بازوبند کاپیتانی لیورپول در بازی دوستانه اخیر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/102435" target="_blank">📅 17:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102433">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CmqnMOGr1rT5jU6gf6nRjQIRP0gewbFvgVQeb_uLFovW7QgIS8ZtL5Zo1696MhJRoABY6dGXenbat0KInAlXpp2ekb3UdjxI4lYMTxG3I98xEyovc3F6wCk2Zk73ATulPwJNYiKRj9poKSCvUSnFEYGnGcZprB_Q6KOdeAx6HfQSoaBAmhmwq0F8DWtTH98iInzAg8YVGcDfETyMm96NyMw5kP9tYZP-vgjB7ziwk7zCWT8M1Uy3mTtPa2glt5l_zqDGXTKZxz9NXie6ohvp3-NHBDHSfr9j2327ISkRXw66tmY_NUJ5B4Pr_k8l8JkgQelVdqnRouGbPZY3sDD5Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p1sTKy8F8EJ4nswhcQbYQ_KFLjrf6OvkMrv2zCX8sDCsDu7zGBUoqcqyFPbkbr97SLP_EYzNJj8zdvVc74BiTKNUqBgWVVwOBMK8x-7lUjDSVVF-FjACpQjmSsvrmWlYhWW_2US0DUUBchhN67KwWj_SAukoNeV0qhG48uRUES4VYFg8Lt7vOfaRXO0Qefi4gJx1T5v257r8w67lsmMHtLMLXiAujIpzfjsmYJM0i3BReCOlBCZKqZEVky3BSpnkn8-gilKWD7TVMznMsLKQdDdeu-jStqqCL8g-KnNmb8152RiQJ3tLVtAHxmVx5EDeZQNoU7DMHhrOBXgx1KDjUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
ال اسپانیول:
پرتغال و اسپانیا اعلام کردن اگه اینفانتینو پیشنهاد خصوصی سازی جام جهانی رو پس نگیره از میزبانی جام جهانی 2030 کناره گیری خواهند کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/102433" target="_blank">📅 17:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102432">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96363baca3.mp4?token=dmCeorJHqtHznDi_e7A1q8qluCFZ9DbVvHyQJyH0lY1L2B7vhnRwJCb1YJvTAsEDSPpyI8X_nEgUNKD_22K4VMkueyP4risFP0t_ZoL4koniDrdwT5LQwSAESkyMPb8KgEGzF70leEK0iKsk8nRdUQMSbTNfIVGEPX4WR1MNemvEgWKQkmM_BA81sREg86eck-F7cTuyRq3YKteGDEVtFWo6zcH-o1eQsAGXcy9fDHNbRCDzWYYaYyLPDcM_8kov74KTd2Pm44LqhNe2rcA_Hcwnsw3Z0at9MMpk3CwEptJ_wJmttnFK60nq3NQpds6L-NVfkNpyaSoMBgbHWGWX8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96363baca3.mp4?token=dmCeorJHqtHznDi_e7A1q8qluCFZ9DbVvHyQJyH0lY1L2B7vhnRwJCb1YJvTAsEDSPpyI8X_nEgUNKD_22K4VMkueyP4risFP0t_ZoL4koniDrdwT5LQwSAESkyMPb8KgEGzF70leEK0iKsk8nRdUQMSbTNfIVGEPX4WR1MNemvEgWKQkmM_BA81sREg86eck-F7cTuyRq3YKteGDEVtFWo6zcH-o1eQsAGXcy9fDHNbRCDzWYYaYyLPDcM_8kov74KTd2Pm44LqhNe2rcA_Hcwnsw3Z0at9MMpk3CwEptJ_wJmttnFK60nq3NQpds6L-NVfkNpyaSoMBgbHWGWX8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/102432" target="_blank">📅 17:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102431">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">💥
🧐
رونالدو، پسرش و جورجینا درحال عشق و حال در گرمای تابستونی اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102431" target="_blank">📅 17:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102430">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e703311f9.mp4?token=NIlZQEH9WJ0H691BGl9fkEUapoQyhEpoXZ7j9pvhEP8ByXHLSIcexcsr2nPLu6kKnwE8poMF2aMm3Gmxc5JeZiWRa8lgk2WrxxA7_pHdwUxjR_0Gx4DyD6AnjPDOYmuTSdAAw0Zahan24DPl1kXuZO-wcp8wxRVznCUAC5kAT1AvpC2klHr23iD5vv2hqFS_dP3yk669njFoNHcEQsFdJCZjMeVxCqbwC-dI0zPGmH5oFn-166-jl6N2E84shFAngLbJrFh_-9wUCekd1JEBSEK7lsSgxn2bipFOkImH0TQQRhobP9SfJea2DWsF9BpI1xQNERotTEnBb8vqijEfzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e703311f9.mp4?token=NIlZQEH9WJ0H691BGl9fkEUapoQyhEpoXZ7j9pvhEP8ByXHLSIcexcsr2nPLu6kKnwE8poMF2aMm3Gmxc5JeZiWRa8lgk2WrxxA7_pHdwUxjR_0Gx4DyD6AnjPDOYmuTSdAAw0Zahan24DPl1kXuZO-wcp8wxRVznCUAC5kAT1AvpC2klHr23iD5vv2hqFS_dP3yk669njFoNHcEQsFdJCZjMeVxCqbwC-dI0zPGmH5oFn-166-jl6N2E84shFAngLbJrFh_-9wUCekd1JEBSEK7lsSgxn2bipFOkImH0TQQRhobP9SfJea2DWsF9BpI1xQNERotTEnBb8vqijEfzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
🎙
تمجید جالب کاسمیرو از لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102430" target="_blank">📅 17:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102429">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b472a6619e.mp4?token=byBqqj8-TcIoapD-QnEHv3XVCRktbTA7T0D9LCN6heOq3_IlKOPqlRGUzSKAjSQP6tVqEV7dCHNgvL2fXjL3UMXQfOWsu90rMukz901-bXiJzEPUcqIgpS_dlzY31CV2oiwZmLM8z40WP_zkuqIjvwirHnfmg1EKzUb-QSrQ6GwenXeCGTqd0hU-GFJa9xaQYZyPECVr2OGGxjcY7OrsXkWnzaCViR4acnxqA2Ft7V0Kz-qQmdr1SxKu3xjYSm4KvvzbGusAnGHh1FTqerJeNw2yGsPnEL3V-OR19jGfcJqFIEJm80fHy56-2g6O78Cl14gKLu4qV0hNsa-iAcMb5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b472a6619e.mp4?token=byBqqj8-TcIoapD-QnEHv3XVCRktbTA7T0D9LCN6heOq3_IlKOPqlRGUzSKAjSQP6tVqEV7dCHNgvL2fXjL3UMXQfOWsu90rMukz901-bXiJzEPUcqIgpS_dlzY31CV2oiwZmLM8z40WP_zkuqIjvwirHnfmg1EKzUb-QSrQ6GwenXeCGTqd0hU-GFJa9xaQYZyPECVr2OGGxjcY7OrsXkWnzaCViR4acnxqA2Ft7V0Kz-qQmdr1SxKu3xjYSm4KvvzbGusAnGHh1FTqerJeNw2yGsPnEL3V-OR19jGfcJqFIEJm80fHy56-2g6O78Cl14gKLu4qV0hNsa-iAcMb5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
یادی‌کنیم از بازی تاریخی ایران و قطر با گزارش جذاب عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/102429" target="_blank">📅 16:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102428">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfd29d0ef7.mp4?token=d8f-51qwf-Tw6ojjVhVj1626tnjXeNK5Srd2diN3u_vsUEdQ6ktAUc9jK5zrnSgQhtpSKcOahTfpNOrF0AE5xZjoPi1G58wsbknEH8sITGtALEyDUhhFzTC0ADP0yYgGC6P7_wuf__ehQBlEJ61lO1dUqALtHYnWOTDfiYGbiDT13fYIrAK_FHGJ9NiD0HwGZEQZN0Qm67NkuDCgsGJgQZpJYB4_ACnPpbshJm55eyRjDJclC4Z_UgbFXSVMV-FxIxB-eDLI3wY3xMdRD1rmcnZBQwusKEBq9VQxXy1CD9xoDxQ-kIG1UY5uD-P0Beu8u9eBPHCjojpAjAlP_76TJoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfd29d0ef7.mp4?token=d8f-51qwf-Tw6ojjVhVj1626tnjXeNK5Srd2diN3u_vsUEdQ6ktAUc9jK5zrnSgQhtpSKcOahTfpNOrF0AE5xZjoPi1G58wsbknEH8sITGtALEyDUhhFzTC0ADP0yYgGC6P7_wuf__ehQBlEJ61lO1dUqALtHYnWOTDfiYGbiDT13fYIrAK_FHGJ9NiD0HwGZEQZN0Qm67NkuDCgsGJgQZpJYB4_ACnPpbshJm55eyRjDJclC4Z_UgbFXSVMV-FxIxB-eDLI3wY3xMdRD1rmcnZBQwusKEBq9VQxXy1CD9xoDxQ-kIG1UY5uD-P0Beu8u9eBPHCjojpAjAlP_76TJoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیاز بود یه آیتم جدا برا لحظات تاریخی فیروز خان کریمی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102428" target="_blank">📅 16:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102427">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d17c8ef3f2.mp4?token=laMopU7VUnyZwcpL_Dx7lAcbuETzjmvJHb3iMxBXrj_qUsYiaU03U9Be7pnXys6iDy6JMJYHFIzbWJwD7_fGfHg1eu1pLls6LhEvwHS6y7UHoQ5dN82A2dKURDM1fedtnJRu6a87u1SD9ZgkMZIE3t6j_9SZtnrnzJ7HQ5vRnthKp8UMVjauiwWFrCBpXC8PBG4Zru9rZWiKZL6oWPGjLdRDtgD0dK_KXfbQvPVFIjFzumEaRlLF7qWLwlh-IOXx3yKXAhOgrIkER-H3lbZKunmjcmpVmAFYi-llPPPVo0ZAXwMTk4BW2NxbKyYNTRs1dU4_4yLD9iIOosDkWF1zxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d17c8ef3f2.mp4?token=laMopU7VUnyZwcpL_Dx7lAcbuETzjmvJHb3iMxBXrj_qUsYiaU03U9Be7pnXys6iDy6JMJYHFIzbWJwD7_fGfHg1eu1pLls6LhEvwHS6y7UHoQ5dN82A2dKURDM1fedtnJRu6a87u1SD9ZgkMZIE3t6j_9SZtnrnzJ7HQ5vRnthKp8UMVjauiwWFrCBpXC8PBG4Zru9rZWiKZL6oWPGjLdRDtgD0dK_KXfbQvPVFIjFzumEaRlLF7qWLwlh-IOXx3yKXAhOgrIkER-H3lbZKunmjcmpVmAFYi-llPPPVo0ZAXwMTk4BW2NxbKyYNTRs1dU4_4yLD9iIOosDkWF1zxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
▶️
رکورد پرش سه گام جاناتان ادواردز (۱۹۹۵) با ۱۸.۲۹ متر ثبت شد و ۳۰ سال پابرجاست. این دستاورد استثنایی در دو و میدانی تحسین شده است. ادواردز در مصاحبه اخیر بر تکنیک منحصر به فرد و هماهنگی قدرت و تکنیک تأکید کرد. او پیشرفت رشته را با شکستن رکورد توسط نسل جدید ورزشکاران مفید می‌داند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/102427" target="_blank">📅 16:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102426">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/543e2ce52d.mp4?token=FgndNXPgNh0A9Y8qrheHTmisPncJrSj5rx4ktziGrs35OKT5fVNHI075tsRggBstY_hA1-C3q0CHC2477pURy6utHOc4BmBRioKLOjHKDg_jZYu5kXthkONX7Xn7JAhxs1ZgTsx_jTjPEDgIBnJpMb-q47ekWIRaoHELoXLdKCcxGhz8EbmTzUpQ8BN-5ZQnHR_y5RGLKiI1OzcvmC1bufLqcRKiW0P2zQU36qi1Rt6il1e6GQkb1rU1rAew7ODCgaL833ry2M0TOJdUibfTnmwE9LS9soK1o0VCzvsjopvTtVm0rCZNDxCTUwcNyhYqnvjPWOcZP-psjkHQsisDfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/543e2ce52d.mp4?token=FgndNXPgNh0A9Y8qrheHTmisPncJrSj5rx4ktziGrs35OKT5fVNHI075tsRggBstY_hA1-C3q0CHC2477pURy6utHOc4BmBRioKLOjHKDg_jZYu5kXthkONX7Xn7JAhxs1ZgTsx_jTjPEDgIBnJpMb-q47ekWIRaoHELoXLdKCcxGhz8EbmTzUpQ8BN-5ZQnHR_y5RGLKiI1OzcvmC1bufLqcRKiW0P2zQU36qi1Rt6il1e6GQkb1rU1rAew7ODCgaL833ry2M0TOJdUibfTnmwE9LS9soK1o0VCzvsjopvTtVm0rCZNDxCTUwcNyhYqnvjPWOcZP-psjkHQsisDfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو کمتر دیده شده از مارادونا و فن‌پرسی
💘
💘
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102426" target="_blank">📅 15:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102425">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102425" target="_blank">📅 15:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102424">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/102424" target="_blank">📅 15:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102423">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102423" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102422">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kefrgUF4Z0KvjIWz6jNJg2PXSyw4B8xLX7ztYrZLatk5OgvXaWNMMJirdxhpP5Z1pzct7DskGiFcFOTozA8qb93CYflvtdUGLizv2pmZiI6ZaTHRB4izS7ThRJ0XHsyxt6gXGXoiQb5nbuTQ4-6nczdNGJ6DdrcUNn9io5adayv0mcsTJHqo3TnEom5Q9P1klg01L1N_Q_dfYOVEoxrGmkAKSul9pzi5dj6XrO0Zkid8mzroIluX9od_oF08HPQyygWpaF3jek3DcLaCLrW6xs53PjZjvytvc1ktCcEDf6g8hUzIAmQ3u_6NsW9iOM_MX_kX7h0REZWz78OrpzlJqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
لیست رئال‌مادرید برای بازی با فیورنتینا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102422" target="_blank">📅 14:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102421">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102421" target="_blank">📅 14:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102420">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/529b07ca6f.mp4?token=AmTFh99Nb7RmoutX-7fz_srsnVorFDUQhctuoGvEtXdhG-UvmIpwKhZoZaKPCkGiXDBdWRS8O1VlRcMzYKNe9biHbev3rY3K33Y5lJKvn6AMMwFrrVBI5TSOPRsHCO9i1pVNqt2XYn5ZsBzY0MV4kHCcvptZCTXpnOkKcQoQYAJopXwOfl1AtCHbcZHF0JnhmqqUGadFOecXnWHNvKmka99RZeH3WTPkkwYTmx65FXLU84I5tBMh9fsqF1_IS9UDo1dV3gjy7kgkLKXFbXOP75_E0OSZ0Xkj6wfxfkf9Wit6Pg0JsAd0jyIOBGvjxtreA17ZTu2p-gXNgkGfLdrjYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/529b07ca6f.mp4?token=AmTFh99Nb7RmoutX-7fz_srsnVorFDUQhctuoGvEtXdhG-UvmIpwKhZoZaKPCkGiXDBdWRS8O1VlRcMzYKNe9biHbev3rY3K33Y5lJKvn6AMMwFrrVBI5TSOPRsHCO9i1pVNqt2XYn5ZsBzY0MV4kHCcvptZCTXpnOkKcQoQYAJopXwOfl1AtCHbcZHF0JnhmqqUGadFOecXnWHNvKmka99RZeH3WTPkkwYTmx65FXLU84I5tBMh9fsqF1_IS9UDo1dV3gjy7kgkLKXFbXOP75_E0OSZ0Xkj6wfxfkf9Wit6Pg0JsAd0jyIOBGvjxtreA17ZTu2p-gXNgkGfLdrjYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
✅
یوسفی: زمین و تماشاگر که ندارید، لیگ را پلی استیشنی برگزار کنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102420" target="_blank">📅 14:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102419">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9889076a09.mp4?token=ucA_tVGk0b4DCoMEwAVWci05qHaDALx0B0xzZk2aFAz_0aIwjA9kERNwyneIsKWLWonnlapRrUw_iwPreT3PK5meWIEl8uSHGKlqofOWQo3Gl-IcfdHazp583bvbZbVzbgvmbq2AnVeEZf3og_i22OYUoryVaE2TS8DTvkm7WQ2gQQLLm_tshJMhp9yrkQhVnjXrh8FF_mFhS0O8hnXP9jixN4f_SllzviYNNl5N9j8hehqDwdKUDtXlL7nRwjZOTYAwV9SA81LTXy03fnkSR5y2uDIf2ylrGh9mXRBWHpRNzbCVZfIiukVxY-N7b-ien4VgCcVYJVdQ3yk111PESw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9889076a09.mp4?token=ucA_tVGk0b4DCoMEwAVWci05qHaDALx0B0xzZk2aFAz_0aIwjA9kERNwyneIsKWLWonnlapRrUw_iwPreT3PK5meWIEl8uSHGKlqofOWQo3Gl-IcfdHazp583bvbZbVzbgvmbq2AnVeEZf3og_i22OYUoryVaE2TS8DTvkm7WQ2gQQLLm_tshJMhp9yrkQhVnjXrh8FF_mFhS0O8hnXP9jixN4f_SllzviYNNl5N9j8hehqDwdKUDtXlL7nRwjZOTYAwV9SA81LTXy03fnkSR5y2uDIf2ylrGh9mXRBWHpRNzbCVZfIiukVxY-N7b-ien4VgCcVYJVdQ3yk111PESw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
💥
روزی که پیتر چک آماده ترین گلر آن دوران فوتبال میخکوب شد و این اثر هنری شاعر رو تماشا کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102419" target="_blank">📅 13:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102418">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjGJb-bU2_Qqu-07vheBXYReUyFMfu1HaE3ZI3EtkuMUrGUbForfXn5YkR6SURqzJn3RJj5HbxAcwVqBvnMplgU6XC-ZyvKMXx4lqGKVx1CVFAZeiAJ47f-NGvuZFVTUOZSNkvCAoedbuwC5a2Cbl3i7iOMNUlYA0mLwolAD6JB1_vVzaCcWBah3QSVVVLC3jmE30_pqZhzso_V-tDFvbVEOU_2pCIJ7PjSDuEwwiVla9S1-DwBElDAUPBKrR1HJj6pMcoBhnk1x7qJowqvT-hMLaQtlLi2aH84lRyReUZoVH2fKOec-BlhBr13k1Bm5f_gUO47PDsJc7KcKIyxCXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
کارلوس اسپی تو تمرینات رئال مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102418" target="_blank">📅 13:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102417">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BcXhSTDEyM6gKQCKAJpXsm6qO4qMcxkH-uFB5ONNIfysD_CSlAd_szaOR0A4zE1-fKIzBzzvV7FQwYRwiXd3cIYTf3lUZULSqBtq8FhBvJsvlB4QhCWd5a128WUYhhneQDcR4x9iNrWYmkOKj7MENgvF7NSKLsJDguK9HAMryvxM5_CQ9CxDY5QxnX4qMKPQe_un9z8BERMpB-3bsROUOYNTI0TfWYorU33vrdTQIifTo8wdC59TWtTa-bbdG-u5zN1Boavwm4QB9KzVPqlXOS-My49CuHUVR1N3i7rS6Uz3aFh3bXWdK04Unm1JeO21miTswjdDO3_T90an4ixetg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
روزنامه اسپورت: دو باشگاه آرسنال و تاتنهام به رقابت برای جذب فران‌تورس پیوستند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102417" target="_blank">📅 13:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102416">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4938ae1d8.mp4?token=JRtw8qNdxRaEeZENOVoHMhJoFo3Yp7kAhDDNXkLJihFoumY0eSssPHxl2DbXsreOUxhGQRCL9fUs-0iF1YAdpaTuwWw7n0DVf8mHalhouPBD66JcgKz3UylcKIunvd1fLHunDd-A2B7bkZ3_qOzqFQAvbxW8zJVcLiKBw5dGVk2ajRHFFguhYvBThoN3AQINHJ2KTm870PEn9HLTXTLbfPq1JvtOo9U-CC2cpt88s2dXCRLfyRoX6yTNwPc_6GOGGtzjHikMyEPRhLf7wjdhTBNUd58OOqtesMXU7JsHkFQXaisOefR_asejAUdLDGB0g-UlaECoNXTrMWLYDq-fRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4938ae1d8.mp4?token=JRtw8qNdxRaEeZENOVoHMhJoFo3Yp7kAhDDNXkLJihFoumY0eSssPHxl2DbXsreOUxhGQRCL9fUs-0iF1YAdpaTuwWw7n0DVf8mHalhouPBD66JcgKz3UylcKIunvd1fLHunDd-A2B7bkZ3_qOzqFQAvbxW8zJVcLiKBw5dGVk2ajRHFFguhYvBThoN3AQINHJ2KTm870PEn9HLTXTLbfPq1JvtOo9U-CC2cpt88s2dXCRLfyRoX6yTNwPc_6GOGGtzjHikMyEPRhLf7wjdhTBNUd58OOqtesMXU7JsHkFQXaisOefR_asejAUdLDGB0g-UlaECoNXTrMWLYDq-fRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های بامزه رونالدو از ارتباط صمیمی با پسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102416" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102415">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5029f55db8.mp4?token=lTjL4jn3mWiteBxz2hRV8g8RJqxNshuMA3vAjnHvH0m2sBB8eRuiDHRri9fR8gdDEs3puc04TEvPlWwzto54VKi5odrdVRwFEvqa8u7HXfe5VHm_LrVGotCio4wkXj3gJY9FkjbC2tz7wb7pPhOxO6U05ZmVRwB0-sUhhB_lkMrNX5Y2s6VJwF-Cw8amJ6WA2oYJINaHkPeiOpq2cHGSDceTiISA8Hwuxow2f5Tj7krZgN1DfPiTCi5uzns-k3GlfyeRznZHsVRhu26shqI-RSxkAv5HIcTIJBARbsVB8U-t5iOR6A7E6XTyFnA_Xgvhw3G64bpzM9J4dMHZNPYSQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5029f55db8.mp4?token=lTjL4jn3mWiteBxz2hRV8g8RJqxNshuMA3vAjnHvH0m2sBB8eRuiDHRri9fR8gdDEs3puc04TEvPlWwzto54VKi5odrdVRwFEvqa8u7HXfe5VHm_LrVGotCio4wkXj3gJY9FkjbC2tz7wb7pPhOxO6U05ZmVRwB0-sUhhB_lkMrNX5Y2s6VJwF-Cw8amJ6WA2oYJINaHkPeiOpq2cHGSDceTiISA8Hwuxow2f5Tj7krZgN1DfPiTCi5uzns-k3GlfyeRznZHsVRhu26shqI-RSxkAv5HIcTIJBARbsVB8U-t5iOR6A7E6XTyFnA_Xgvhw3G64bpzM9J4dMHZNPYSQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🔵
درخواست کودکان جنوبی کشور در وضعیت جنگی از رامین‌رضاییان بازیکن استقلال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102415" target="_blank">📅 13:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102414">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac78119da.mp4?token=NbQhA_Pl1kqZghTm5TYr31qDR5QpFtKlkC8k_hvDtd9flGc-b25N93L7T2HpgpfwvJuHBTme8t3_Bz7DY-Vp5F87zHbJGqu2riNxUj3Kvr-ym_Uv_GlCzcs7F7XCHpOmScYSZYJlAjbmexVZHyw1gXoihWKK8ZCzygocS2rL1sDoUKzP63LVMRbmyumBF_O4N0KS32Ue67LKi9EBu0yr5STmh-nkf0n1lL1GYRU6YvsusjL-KHPYl1e1WmNUVo3_FffR70Vs5ClOGStoeh87gf0KbpErUF6DPOQxSgV6YajPDPHC5auFDiRnWPcoFEROZhuFVTfAxDOL5qHLbD6zQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac78119da.mp4?token=NbQhA_Pl1kqZghTm5TYr31qDR5QpFtKlkC8k_hvDtd9flGc-b25N93L7T2HpgpfwvJuHBTme8t3_Bz7DY-Vp5F87zHbJGqu2riNxUj3Kvr-ym_Uv_GlCzcs7F7XCHpOmScYSZYJlAjbmexVZHyw1gXoihWKK8ZCzygocS2rL1sDoUKzP63LVMRbmyumBF_O4N0KS32Ue67LKi9EBu0yr5STmh-nkf0n1lL1GYRU6YvsusjL-KHPYl1e1WmNUVo3_FffR70Vs5ClOGStoeh87gf0KbpErUF6DPOQxSgV6YajPDPHC5auFDiRnWPcoFEROZhuFVTfAxDOL5qHLbD6zQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
نصیحت اسطوره‌رونالدو به امباپه
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102414" target="_blank">📅 12:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102413">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🤩
#فوووووری فابریزیو رومانو: آلن هالیلوویچ استعداد برباد رفته بارسلونا در آستانه امضای قرارداد با پرسپولیس قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102413" target="_blank">📅 12:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102412">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75b732a95e.mp4?token=u4sXo3wBeVbM_9GsCeom1JPctI7MeTV7sJQYLBPX7JcRcEvMtHQamp1k_19zfpKN0E30WXWCHW7NlDaJOHXbTPuVP4p2xFJds52HK2CW0hXqh8aAu_FeBj7ozTGiusRqKJ1NolC2HAZ7kv5vQ_GPRe_opVDyunEu5wKh9OhQPxiUSC5EUPjvVRbGCcaO5eZpsP_T1aqOA0uGIXU09AyON-BugkrbXaeulNUAhmSJc6o28dZM-zZMa0pAcVVYUJMuN7m1uK_iAiNYtShTPTNJZiXIQtKtmhoEQGYqHmUi21LPnWVR7sRBh6W2IMZFUzWkChCGeng6R1V39hCdDwvyNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75b732a95e.mp4?token=u4sXo3wBeVbM_9GsCeom1JPctI7MeTV7sJQYLBPX7JcRcEvMtHQamp1k_19zfpKN0E30WXWCHW7NlDaJOHXbTPuVP4p2xFJds52HK2CW0hXqh8aAu_FeBj7ozTGiusRqKJ1NolC2HAZ7kv5vQ_GPRe_opVDyunEu5wKh9OhQPxiUSC5EUPjvVRbGCcaO5eZpsP_T1aqOA0uGIXU09AyON-BugkrbXaeulNUAhmSJc6o28dZM-zZMa0pAcVVYUJMuN7m1uK_iAiNYtShTPTNJZiXIQtKtmhoEQGYqHmUi21LPnWVR7sRBh6W2IMZFUzWkChCGeng6R1V39hCdDwvyNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇧🇷
آنچلوتی: "در هایدریشن بریک نیمه دوم بازی جلو نروژ اشتباه کردم تیم رو تغییر دادم که باعث شد کنترل بازی از دستمون در بره و ببازیم..."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102412" target="_blank">📅 12:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102411">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2964e2f72d.mp4?token=MzuOC1HFuLhoYfNtdHA9JP0wQMGe5isaGxAUKFrzU2AOmQ16edbuj5cgW_qXgRbjnI0Ov9PVoBxkTepkHpHhyeaulOKTxcyEp_pYqponx7CGuikIGKr_p4AveEK9PeornZpyokYoor7m4HBPm1uGtN0Z0yK7jRqVtC4PDenT9gIhmXXISUhZ2VslhJTO__vhkP7wmjlb8JHtVinW-cVCurQiY3JJzw0I3h2oVIbImbGy4cWneQZiXGAarxcabI4K_4p9g0NDh2iNwqg-It3bVRSkLQ5Q_CMTfAhxSSgRVptotqLjp8N3jD3BxAgR3mf7Mu1w-4add-miLL3MMLvoDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2964e2f72d.mp4?token=MzuOC1HFuLhoYfNtdHA9JP0wQMGe5isaGxAUKFrzU2AOmQ16edbuj5cgW_qXgRbjnI0Ov9PVoBxkTepkHpHhyeaulOKTxcyEp_pYqponx7CGuikIGKr_p4AveEK9PeornZpyokYoor7m4HBPm1uGtN0Z0yK7jRqVtC4PDenT9gIhmXXISUhZ2VslhJTO__vhkP7wmjlb8JHtVinW-cVCurQiY3JJzw0I3h2oVIbImbGy4cWneQZiXGAarxcabI4K_4p9g0NDh2iNwqg-It3bVRSkLQ5Q_CMTfAhxSSgRVptotqLjp8N3jD3BxAgR3mf7Mu1w-4add-miLL3MMLvoDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102411" target="_blank">📅 12:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102410">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b5a4f433a.mp4?token=T0Tpe-v_ury_LzpFy-uZ9xuhkjUWcFr5jeApeEGliNl0srApNILF0kR8U5uszKN07BiwG0xpx-rb0X_5s51EgYyv8bSuXQ4PFh-JXbdWPy4L0UJSm_uHAtB53o9hVaRKAJmKMT1MC3qOJt7xwNH5yOOTuGk4x4IeNYke8w5fMDg1zvsB_Uah8VymJeLuAupq6_zYyDlSf1Y5ZJj4dQo2Q4LRtto3dscIrGTUyVSZy_QjqlxDadq3O0j64KgKjArd--IGxbzFuVJpULlZ7oyODw9jb7f8MW1zUsSqvOwLt-XiW85k1exCPqQvEaWr8oil_fe8StG1TBOEUEAvnJhnTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b5a4f433a.mp4?token=T0Tpe-v_ury_LzpFy-uZ9xuhkjUWcFr5jeApeEGliNl0srApNILF0kR8U5uszKN07BiwG0xpx-rb0X_5s51EgYyv8bSuXQ4PFh-JXbdWPy4L0UJSm_uHAtB53o9hVaRKAJmKMT1MC3qOJt7xwNH5yOOTuGk4x4IeNYke8w5fMDg1zvsB_Uah8VymJeLuAupq6_zYyDlSf1Y5ZJj4dQo2Q4LRtto3dscIrGTUyVSZy_QjqlxDadq3O0j64KgKjArd--IGxbzFuVJpULlZ7oyODw9jb7f8MW1zUsSqvOwLt-XiW85k1exCPqQvEaWr8oil_fe8StG1TBOEUEAvnJhnTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
🔴
‼️
علیرضا بابایی مدیرعامل چادرملو: تورنمنت سه جانبه به دلیل کمک به پرسپولیس برگزار شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102410" target="_blank">📅 12:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102409">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c746b16b5a.mp4?token=XKPr8GxENirk5NF29NjjxhOrU4JyoJK8fHH5Xxc5GxS6nKEd3F4hDDtCuosjzi-jKrMk53ZMFqkZzN2zt5yJeayCvkdE9ewdoJ_9CT2MrZWEieRW7krYnRBUyP9oi2N7pdNA2iIO7QRHPeVGpUfwN1BnQI6AiEECRt4YSEXeew1qAHajaLIkx6nHI1R_MBwQtVzpfT0TKKk20Dzm1tyDdP2t03wbHMy3C8vAVUSf-iR7rotp2SviaghUzuE8Ma_uhKd-F6sH-0PlhSZDHEz6B4lAt1ca-1yHpEj7Dp3NCZzlt3Iv7s1hD8ymcYfUtnr5JwGwqq3p8C2B9fbtPmZGERJIccWT0ehbzs19tIo1_yMtOMDJFA1JeECRx4GiYsYGqXrbytm3a1yqM7YP96BuItN0QmyILIO1CwcFI2SREicllPWj_-hA99bqGK-ELYavFamCrWT5lG-wPWVzcqMRIPfZIT3z1gBgzTdWdQparrY6kUpwedJnDJEy73H-HLvx3nIXxZsML-lDBQzGDzZeti1KKU_JjX0mYM4ouuJ759zylv_9L-9OW0RM5xQvujA4TOIj9JPMoYbfEMoX1yE2h238i14v7EKoDr5wnfv_PsCobttbbDoKd2Ri6Y1chcqFF9zYtxE6jQk65N2f5Gj7rA7A95MHyDGLaoIRjhzV5DM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c746b16b5a.mp4?token=XKPr8GxENirk5NF29NjjxhOrU4JyoJK8fHH5Xxc5GxS6nKEd3F4hDDtCuosjzi-jKrMk53ZMFqkZzN2zt5yJeayCvkdE9ewdoJ_9CT2MrZWEieRW7krYnRBUyP9oi2N7pdNA2iIO7QRHPeVGpUfwN1BnQI6AiEECRt4YSEXeew1qAHajaLIkx6nHI1R_MBwQtVzpfT0TKKk20Dzm1tyDdP2t03wbHMy3C8vAVUSf-iR7rotp2SviaghUzuE8Ma_uhKd-F6sH-0PlhSZDHEz6B4lAt1ca-1yHpEj7Dp3NCZzlt3Iv7s1hD8ymcYfUtnr5JwGwqq3p8C2B9fbtPmZGERJIccWT0ehbzs19tIo1_yMtOMDJFA1JeECRx4GiYsYGqXrbytm3a1yqM7YP96BuItN0QmyILIO1CwcFI2SREicllPWj_-hA99bqGK-ELYavFamCrWT5lG-wPWVzcqMRIPfZIT3z1gBgzTdWdQparrY6kUpwedJnDJEy73H-HLvx3nIXxZsML-lDBQzGDzZeti1KKU_JjX0mYM4ouuJ759zylv_9L-9OW0RM5xQvujA4TOIj9JPMoYbfEMoX1yE2h238i14v7EKoDr5wnfv_PsCobttbbDoKd2Ri6Y1chcqFF9zYtxE6jQk65N2f5Gj7rA7A95MHyDGLaoIRjhzV5DM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔵
علیرضا بابایی مدیرعامل چادرملو: بازیکنان را از پای دیگ نذری آوردیم و با خواست خدا پرسپولیس را شکست دادیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102409" target="_blank">📅 12:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102408">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1b81246b4.mp4?token=hTfDp_W3Qa--rmRTY5hUPsEqYi0632tXR0DNmRz4hEVZcH-BsPUMi5m0satUgTJu8agFfe_FjxYc2NxWLLXTbG7ddPg4TMwxMZ-OaTBtEdsUxoT884FQqfzwlRpZWMNZZmHmvXZUEpb9ykLb9Gu-N3IFiH-_5GfEdnQdPHXTUaoSO5OaHCbishizOMaT1oZ9_eCwrxJJLcoRhJ5pO-E_y5pNg0kJsAsX3VBDX6t9QRyPtN-jIULsx7SiFLB7LIw9LrGNm-JYe6YSLoQoz0FqmQrSYBvqhlpyxfJpeYYK5NQ5R822CtidJheFTBrzk6rDu-teCWjKukRgtKX5knvXvTHob-3vekaG7MvVhfhEOQkdpa1lWAov2dkJrS6tWDPaFcnT4pQmH_-N0JhQjm4yi0KEQ1jEWPpIG9cs3KkRb15IlO7FIq5MMJAaKpMCpi5bKofvZUH51VFoTyX--4sjIfA33KFItB4__vvvnZ2TlIjzcwkzLqmVa8mZ9iPGlFK8JyKKDWHII179Qal9LwL-wXlu-WXKUaQN1jGPt6YJKtY8QgpQ-UmQ9tUbh6TMeK2X_Cy-mDkqUmtprq33msnS5QC1tXfmg1oqgrV4s7wbKxN4jsDNGb2IdA4fBKYmma0hnuxmGIS0X6OqRhdwXA4KgExzEBg3QqZxOXQ8om4oVvE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1b81246b4.mp4?token=hTfDp_W3Qa--rmRTY5hUPsEqYi0632tXR0DNmRz4hEVZcH-BsPUMi5m0satUgTJu8agFfe_FjxYc2NxWLLXTbG7ddPg4TMwxMZ-OaTBtEdsUxoT884FQqfzwlRpZWMNZZmHmvXZUEpb9ykLb9Gu-N3IFiH-_5GfEdnQdPHXTUaoSO5OaHCbishizOMaT1oZ9_eCwrxJJLcoRhJ5pO-E_y5pNg0kJsAsX3VBDX6t9QRyPtN-jIULsx7SiFLB7LIw9LrGNm-JYe6YSLoQoz0FqmQrSYBvqhlpyxfJpeYYK5NQ5R822CtidJheFTBrzk6rDu-teCWjKukRgtKX5knvXvTHob-3vekaG7MvVhfhEOQkdpa1lWAov2dkJrS6tWDPaFcnT4pQmH_-N0JhQjm4yi0KEQ1jEWPpIG9cs3KkRb15IlO7FIq5MMJAaKpMCpi5bKofvZUH51VFoTyX--4sjIfA33KFItB4__vvvnZ2TlIjzcwkzLqmVa8mZ9iPGlFK8JyKKDWHII179Qal9LwL-wXlu-WXKUaQN1jGPt6YJKtY8QgpQ-UmQ9tUbh6TMeK2X_Cy-mDkqUmtprq33msnS5QC1tXfmg1oqgrV4s7wbKxN4jsDNGb2IdA4fBKYmma0hnuxmGIS0X6OqRhdwXA4KgExzEBg3QqZxOXQ8om4oVvE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇪🇸
مشکل ایمنی ورزشگاه‌ها به لالیگا هم رسیده‌ و تیم رایووایه‌کانو نمیتونه از استادیوم خانگی خودش در فصل‌آینده استفاده کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102408" target="_blank">📅 12:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102407">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47a01fbf75.mp4?token=LEoMwtBLVtstDRUlFSiP3Uh8kXPaaZa2zUGpV8mlJC1KpQ66LD03EaFvv4G8j7pu56v0pXVfh3LpVRYI_ScPrlMc3YoOfjrLUP7LJE1qCZrlzRDId4Vaol6apwrnMK9gIkdVTLv0vtVO0j_JUaq3ri9vCdQV0-bvNUWUeqNgsaP6APb4_uSIuDrsrZK6JbSlV4Ub-6Fc4Zr0sSDV4o8NFGc1pL2BR6i3dSHguf74nSevFn0WoMYiE1rbRuArWL3qSvWQTatmBjCtvm0e4XchSRF39N5p-5mxccKwJTgEpLNI4WIZQIeDUcyZfwHkA03iN76vp3DIorg8LEU3DH4htQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47a01fbf75.mp4?token=LEoMwtBLVtstDRUlFSiP3Uh8kXPaaZa2zUGpV8mlJC1KpQ66LD03EaFvv4G8j7pu56v0pXVfh3LpVRYI_ScPrlMc3YoOfjrLUP7LJE1qCZrlzRDId4Vaol6apwrnMK9gIkdVTLv0vtVO0j_JUaq3ri9vCdQV0-bvNUWUeqNgsaP6APb4_uSIuDrsrZK6JbSlV4Ub-6Fc4Zr0sSDV4o8NFGc1pL2BR6i3dSHguf74nSevFn0WoMYiE1rbRuArWL3qSvWQTatmBjCtvm0e4XchSRF39N5p-5mxccKwJTgEpLNI4WIZQIeDUcyZfwHkA03iN76vp3DIorg8LEU3DH4htQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ویدیو وایرال شده از صحبت‌های تلخ و بامزه یک ایرانی حین ورود به‌تونلی در بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102407" target="_blank">📅 11:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102406">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262957043c.mp4?token=Sl0fbfdxP09mtXhkanROteaIatoIeUuvS5PsQXLikg1VuV12YMVSpgSGHNrOR3dcnslq7Yp7m2FfUf-zg_Pr8gKTofpl9Kdpu_nqeTDVSXVQ_WC9gYJm2INGHrs0_ahqJsO-Og3-xg1S2p8pYNAXc62RqhFjmtpIDw8CzFdP1eS5mKvmvnCCS9NrXalXttYNauGdoRWvgPuIacx1lKoF4HoHVm9l54r4E-2tsVNaisevbPgwFB1dvtBdA-E0gOISSwL7x6pLT3AvlMME7mQbiCMeHT-xG-7cLWItD4vADc6ur08WQlgpf_Qc4FO0vyftqFTlcyDHF59RaKZhW57Tvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262957043c.mp4?token=Sl0fbfdxP09mtXhkanROteaIatoIeUuvS5PsQXLikg1VuV12YMVSpgSGHNrOR3dcnslq7Yp7m2FfUf-zg_Pr8gKTofpl9Kdpu_nqeTDVSXVQ_WC9gYJm2INGHrs0_ahqJsO-Og3-xg1S2p8pYNAXc62RqhFjmtpIDw8CzFdP1eS5mKvmvnCCS9NrXalXttYNauGdoRWvgPuIacx1lKoF4HoHVm9l54r4E-2tsVNaisevbPgwFB1dvtBdA-E0gOISSwL7x6pLT3AvlMME7mQbiCMeHT-xG-7cLWItD4vADc6ur08WQlgpf_Qc4FO0vyftqFTlcyDHF59RaKZhW57Tvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
سوپرایز خاص‌ ژابی‌آلونسو برای فصل‌آینده؛ رونمایی از ستاره ۱۷ ساله قزاقستانی چلسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102406" target="_blank">📅 11:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102405">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef2180d890.mp4?token=sYpU81NJajVcs0JHgYhrYRBeuPDl9LsBhys47QvcWCSRGA2r6-0EPmkeKa8x6AL7c5VrzVUZiPkv7GpMDo0bd2hv1684v9KxMjGrn90FMCoz50LTs1Gk1PKkP03eBC3iFG8tNsD9n25WQErpLPzJr0yLTOLNLCajGsapfZgjLalqNJ6nVI_SJKBq9OhPoj7W-I0vz_MYtRpFUttesaQ1PdNKHWMgVHxB-ndHaQTA-ADx44kQkINgnT_Fmnxw2eoVfI6QmXEdj4Jb9g-kq4XqQw5YLKyMgn7Qwww5wyhbpBDrLBxHdjNTqbcCtANGjoqvted5GQJzEH8PxKduXabNhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef2180d890.mp4?token=sYpU81NJajVcs0JHgYhrYRBeuPDl9LsBhys47QvcWCSRGA2r6-0EPmkeKa8x6AL7c5VrzVUZiPkv7GpMDo0bd2hv1684v9KxMjGrn90FMCoz50LTs1Gk1PKkP03eBC3iFG8tNsD9n25WQErpLPzJr0yLTOLNLCajGsapfZgjLalqNJ6nVI_SJKBq9OhPoj7W-I0vz_MYtRpFUttesaQ1PdNKHWMgVHxB-ndHaQTA-ADx44kQkINgnT_Fmnxw2eoVfI6QmXEdj4Jb9g-kq4XqQw5YLKyMgn7Qwww5wyhbpBDrLBxHdjNTqbcCtANGjoqvted5GQJzEH8PxKduXabNhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
آماده‌سازی استادیوم نیوکمپ برای فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102405" target="_blank">📅 11:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102404">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31c9897d6.mp4?token=L9zZdu2LS_lOTiJM2VZsD-zlpP4DZJtfK1dr2bg8yvB-xIE3EQY0A14_o6DlEJ0OxqTxFkuDkgCvUik_KPpMCINBuy7qiGLyLZ0r-3YpEdM0xC_EFVur__Y7b44-FvQ1vifDPiaFA82fNNqzPCcMb-fiduB3eTIGnK6aE3ToZJh_BNzA5lKn9uBKb9toh9fQky3xBftECY2QbO4InjAjhVPoSF02xvSZXjq_lABnB4FWArqzg4tDJV1JwGEe0DBpKkwm7a9sI9Sgc0r9SDMMsCxg97gF30xVGs_NRgrjxW3DYMqMdlurDdnsTzw5Pfn2ielnVxSFASfT4844zFpISw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31c9897d6.mp4?token=L9zZdu2LS_lOTiJM2VZsD-zlpP4DZJtfK1dr2bg8yvB-xIE3EQY0A14_o6DlEJ0OxqTxFkuDkgCvUik_KPpMCINBuy7qiGLyLZ0r-3YpEdM0xC_EFVur__Y7b44-FvQ1vifDPiaFA82fNNqzPCcMb-fiduB3eTIGnK6aE3ToZJh_BNzA5lKn9uBKb9toh9fQky3xBftECY2QbO4InjAjhVPoSF02xvSZXjq_lABnB4FWArqzg4tDJV1JwGEe0DBpKkwm7a9sI9Sgc0r9SDMMsCxg97gF30xVGs_NRgrjxW3DYMqMdlurDdnsTzw5Pfn2ielnVxSFASfT4844zFpISw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
پاسخ‌تند و کنایه‌آمیز مهدی‌رحمتی به صحبت اخیر معدی‌قایدی: بذارید تو‌ توهم خودش بمونه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102404" target="_blank">📅 10:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102403">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
✅
کیت‌دوم فصل‌آینده منچسترسیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102403" target="_blank">📅 10:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102402">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/869e38d1a5.mp4?token=AGvqhR9P485w6OEwFQGzg2WqOWOW3StcZJSFX6D28o9Mm0h_-3ZV8ysomCg6F2Ld-47mwzz4NMsJtp-jyNb7PtVZ9EccxnN_VAAkRN9BJ1BiyhA9aEbPLSeL90q5N41KPTGxXAYmuVQOOrTFibyZPvtMPM2J7vT4tJTEo68d9zMplFkv-357ToVJf5YeLwkrPDFp03oK_A-Hj0RceD10ywjuxS_FU9NzMQOkTb5GjIWzYYUjhm5n_nMzINF0e4UUE57ew204uX34AEdvqzxDQR-nWA3JfPZlNDYcMmeef5C_vzpNfcokJyO-cRCjoH0CTp7TSt1sMTd9YISlvZvzrzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/869e38d1a5.mp4?token=AGvqhR9P485w6OEwFQGzg2WqOWOW3StcZJSFX6D28o9Mm0h_-3ZV8ysomCg6F2Ld-47mwzz4NMsJtp-jyNb7PtVZ9EccxnN_VAAkRN9BJ1BiyhA9aEbPLSeL90q5N41KPTGxXAYmuVQOOrTFibyZPvtMPM2J7vT4tJTEo68d9zMplFkv-357ToVJf5YeLwkrPDFp03oK_A-Hj0RceD10ywjuxS_FU9NzMQOkTb5GjIWzYYUjhm5n_nMzINF0e4UUE57ew204uX34AEdvqzxDQR-nWA3JfPZlNDYcMmeef5C_vzpNfcokJyO-cRCjoH0CTp7TSt1sMTd9YISlvZvzrzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
درگیری شدید فیل‌فودن ستاره سیتی به همراه مادرش با چنتا از مردم در یکی از کلاب‌های شهر منچستر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102402" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102401">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f0266060c.mp4?token=gdYFGpOuizG6BBVJl2i7Ede6zT0kETkZURJBZKI3KkOcr-tTYzz5EnrLSb7Kmp2ZIxiZm5qSkJ9CBdx9O0IZK7AF7mXSkK-8MXqEhjOvn5tPngrQkS66z1GXlzgYEzoeWxv8MEndnE67-33IMIC_EXGgyYlNPuJCigQrKQgVTIgH3tQrnXJDY-_5w04KKUU7dxhzDA1FOYAZEhSPYgn1942V3uzznIg2KnzzEwJ65tvJGaAqrR1mO0nPjwxzfD5ADZ7TPfIaWFpmfE_Xz6OI3qNDORqNUcG4vPHDWzkB805Hb96HjgdgyJNNittHSsFR5VEbjKgLmUQJerYTdVv4XH6AfEfjj4rBGVDO2Mxw9FRXQUKFZh_s-ibhyhlFZvxBruYytW_dsWkCS0eCMOwMoB-POdb-zTyCp-GgYD069IkQd9yWl2RRlKqdg3RxTPjwxwyzQVGGwzHmJYyWw7VxtprKkPyiz-ZKa74ai9FnNw54jknAIYm_5nhUbjLI1jpfq4atDgoitbgtLNXLwQ4PLhnLZZmkTDgA9MhnZysIqx93nMcYH_rG2ucbxik1Z8yPb2DLr44HU0i1ZaDA1mXS9xrEYd_lADWQv4JCnoM5NkOHU41hY0srv2BTwJ7kJr_P_rLdLXuwaRDTxYAlzeMQ7pbuPkkwxBZ1pB5yIf7niBY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f0266060c.mp4?token=gdYFGpOuizG6BBVJl2i7Ede6zT0kETkZURJBZKI3KkOcr-tTYzz5EnrLSb7Kmp2ZIxiZm5qSkJ9CBdx9O0IZK7AF7mXSkK-8MXqEhjOvn5tPngrQkS66z1GXlzgYEzoeWxv8MEndnE67-33IMIC_EXGgyYlNPuJCigQrKQgVTIgH3tQrnXJDY-_5w04KKUU7dxhzDA1FOYAZEhSPYgn1942V3uzznIg2KnzzEwJ65tvJGaAqrR1mO0nPjwxzfD5ADZ7TPfIaWFpmfE_Xz6OI3qNDORqNUcG4vPHDWzkB805Hb96HjgdgyJNNittHSsFR5VEbjKgLmUQJerYTdVv4XH6AfEfjj4rBGVDO2Mxw9FRXQUKFZh_s-ibhyhlFZvxBruYytW_dsWkCS0eCMOwMoB-POdb-zTyCp-GgYD069IkQd9yWl2RRlKqdg3RxTPjwxwyzQVGGwzHmJYyWw7VxtprKkPyiz-ZKa74ai9FnNw54jknAIYm_5nhUbjLI1jpfq4atDgoitbgtLNXLwQ4PLhnLZZmkTDgA9MhnZysIqx93nMcYH_rG2ucbxik1Z8yPb2DLr44HU0i1ZaDA1mXS9xrEYd_lADWQv4JCnoM5NkOHU41hY0srv2BTwJ7kJr_P_rLdLXuwaRDTxYAlzeMQ7pbuPkkwxBZ1pB5yIf7niBY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁳󠁣󠁴󠁿
نظر سرالکس فرگوسن درباره‌مثلث جادویی بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102401" target="_blank">📅 10:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102400">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f864b5c9ce.mp4?token=VEb2XoZLjapW4v-qYEpBzK3fln3cRfFRiJS9yXC10yg8biIJIDtkKBnMyQ7PsbfykaW63VlxPQPAYUKVkhs8mfSL8uxNkAaIhxwt4b32oqhDYVli2-uBstnBjdjnIP81ATohca1UCr9EXePfVoyaXwWcrCM5Q_kuFkWTdUGYqT1vN1WnI_Q4z3ws7rpabmwmny9ITF06qO-XQHlyLn45P_eTMKfTLKD1sRe_AtEAHYsxDiQhNfmUuS7SX6vchEwlPRyRhOWtPZ1YZWM2yGPI4hyyJWzecYYwIVxmsCCts-HHWyKxJcWVvLP_PD9eW31bcNtBI0Emd86tarBBoRlKiEBH3n0o_V-Cpg6iMJNe1KJn7Q3fiAIZX--jpbFzsfQoo7A0uTaM1L-_4KdByhBIp0712kdnLFzRs7jUg8auCo_wjBNvjETLEJkP1y81UloGeC7JxJ_8iTU909-k3giyFa3wJPTYsfUJjkbD_AueibyiINTA9Z6YzaJporz8G4sQAIgug5CM1XtSztvoH83ue4qVcUMCLl7x01LAhTbDvehPazDHscxDemPi7KQWwayhyxIgRauLFAvHqSJeK4hmmCkYbhageUw7CbKUrHX0LfP48D_Nn8_lLBY6lWpVlEWBA93QyAWOXhP7FUmLM1k-O6f0Q3tJO1MBbcHg6mrgn8c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f864b5c9ce.mp4?token=VEb2XoZLjapW4v-qYEpBzK3fln3cRfFRiJS9yXC10yg8biIJIDtkKBnMyQ7PsbfykaW63VlxPQPAYUKVkhs8mfSL8uxNkAaIhxwt4b32oqhDYVli2-uBstnBjdjnIP81ATohca1UCr9EXePfVoyaXwWcrCM5Q_kuFkWTdUGYqT1vN1WnI_Q4z3ws7rpabmwmny9ITF06qO-XQHlyLn45P_eTMKfTLKD1sRe_AtEAHYsxDiQhNfmUuS7SX6vchEwlPRyRhOWtPZ1YZWM2yGPI4hyyJWzecYYwIVxmsCCts-HHWyKxJcWVvLP_PD9eW31bcNtBI0Emd86tarBBoRlKiEBH3n0o_V-Cpg6iMJNe1KJn7Q3fiAIZX--jpbFzsfQoo7A0uTaM1L-_4KdByhBIp0712kdnLFzRs7jUg8auCo_wjBNvjETLEJkP1y81UloGeC7JxJ_8iTU909-k3giyFa3wJPTYsfUJjkbD_AueibyiINTA9Z6YzaJporz8G4sQAIgug5CM1XtSztvoH83ue4qVcUMCLl7x01LAhTbDvehPazDHscxDemPi7KQWwayhyxIgRauLFAvHqSJeK4hmmCkYbhageUw7CbKUrHX0LfP48D_Nn8_lLBY6lWpVlEWBA93QyAWOXhP7FUmLM1k-O6f0Q3tJO1MBbcHg6mrgn8c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
شباهت حرکت‌های یامال و اولیسه
🔥
😮‍💨
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102400" target="_blank">📅 09:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102399">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5630cebcb5.mp4?token=BjjyH5byYJu7parSGbVxgEYPG96Rz6B8P2rOojU0bJN4w6BDsfKJbRil-93fHSqfF09fbh5UNJSV-nLDLjP8nS5RhtbM1Gpw-Ss-9JpnmzDZ19wl-XDquTncj2_G0oWLDaJBd-yMEUpFvZTadHMgZPnxDrfRSc6yAOrvy7hI4MZnB4hil_0V4cvKTIwDMsIhLwXDioBaHkWyZacB3pn57A3XhgYYSzKUMxTxOTHCPDdkQ_zoWm9iEO0mrEgHZgv2zXUVMR65SdRurhpG0FqJfnnzXGwhr_k4mdKvbxVn_1MfYdN_QQc0cLEJXetjkXqbj5pd754ge6Jzs2ZiFBicYZcx0kTsAfF7p0iWTK4C1lZG2K-38DS1B5szf_AL0wo6OFGZJNhGMEpghyz3hvaP33ZlkzBfK9y2sfZ3nWNv5NBmXEjsp8CQTX2ud1BibxMxFwa47ksdj1dK3hM1bzXl0U8nC4mA2mepNBslf8A_9D1xBQapyD6Ol3ToDAWu2t8qS08-ulHBclzMcNOb2dCO-kA2lFRexjl9oX7V99yAaUasM4M5xT4tHn13YaiwJzOEK1DTMc-gaA8kVO49HZtZCZ2G75Z_XBiD6IpYKlEuIvJwXxNSKCsReX_sr4RCMp53394bLeJvhdmuB0_dWVtMg523NNjxs1rDefHTeenNoDY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5630cebcb5.mp4?token=BjjyH5byYJu7parSGbVxgEYPG96Rz6B8P2rOojU0bJN4w6BDsfKJbRil-93fHSqfF09fbh5UNJSV-nLDLjP8nS5RhtbM1Gpw-Ss-9JpnmzDZ19wl-XDquTncj2_G0oWLDaJBd-yMEUpFvZTadHMgZPnxDrfRSc6yAOrvy7hI4MZnB4hil_0V4cvKTIwDMsIhLwXDioBaHkWyZacB3pn57A3XhgYYSzKUMxTxOTHCPDdkQ_zoWm9iEO0mrEgHZgv2zXUVMR65SdRurhpG0FqJfnnzXGwhr_k4mdKvbxVn_1MfYdN_QQc0cLEJXetjkXqbj5pd754ge6Jzs2ZiFBicYZcx0kTsAfF7p0iWTK4C1lZG2K-38DS1B5szf_AL0wo6OFGZJNhGMEpghyz3hvaP33ZlkzBfK9y2sfZ3nWNv5NBmXEjsp8CQTX2ud1BibxMxFwa47ksdj1dK3hM1bzXl0U8nC4mA2mepNBslf8A_9D1xBQapyD6Ol3ToDAWu2t8qS08-ulHBclzMcNOb2dCO-kA2lFRexjl9oX7V99yAaUasM4M5xT4tHn13YaiwJzOEK1DTMc-gaA8kVO49HZtZCZ2G75Z_XBiD6IpYKlEuIvJwXxNSKCsReX_sr4RCMp53394bLeJvhdmuB0_dWVtMg523NNjxs1rDefHTeenNoDY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
شیرجه زد، گرفتش، زد زمین، شوتش کرد!⁣ جوک خنده‌دار بیلی مک‌کالاک ماساژور سابق چلسی درباره‌ی پتر چک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102399" target="_blank">📅 09:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102398">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8sHUEyXcrKgOx80-jT2_SmjzCxnAUyCiBUy5dXCPykhCY10bcvK0zSo3f15x3Nm72gTvySEcWaXOMh7sB1SeKqZ1LT9gQyNjSKk7xOic__VmGYTCSuL0rzgOID651hrnSMdd5vGjKPmBarOP-1ggwoguiruJy9qmHhrY3R_xH0ksPFrZqgrXQ6DoMUhQPcFHSNsMOhUH-sAfE8xLaLEf1xou9yZUA7893aJDdye_FhMCRDQ6mUGLJQWEY7m5avO5GAXyFzHbtwJm_yY_8hU3q3zPainxX_Allq6wNDQH_g0Tf4ioOt88UjnQhdB6Mdi2R3zSfxZb20mnQCYxJiNrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
🇮🇹
لحظاتی پیش، فرانکو بارسی، اسطوره فوتبال ایتالیا، در سن ۶۶ سالگی درگذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102398" target="_blank">📅 09:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102397">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d54a6dc02d.mp4?token=rJ3mZDy-xh8ArfiY1IGTTtH_6bzAb0FRWYkyADZOpqmuwPgJ0lDVZpermG0WPjgPXyt8vCi1msEcxqHWZHQi83cDFq6SOpbye42zPFBk3jk3jRYMhwiMMiGchWvRq719xrD3FxRzSfZ89Xbp2r7PANuTxX_Dag3zW79DWyoSbV2uFTzonelq6C4qGdoylBsF0b0b6MgqSF_hMy1oCALPy08gJtNezMg_4flN9azfcn49ZFJxDXjHKgSSUvl6tdpNopboIVnXG-2NFWoboWtVKkbbzbQ1zMtyxql6ezAIJG_G9dWteRhtmc1q3goFnmVr4b-C9emd9DCt6lTDNo_gww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d54a6dc02d.mp4?token=rJ3mZDy-xh8ArfiY1IGTTtH_6bzAb0FRWYkyADZOpqmuwPgJ0lDVZpermG0WPjgPXyt8vCi1msEcxqHWZHQi83cDFq6SOpbye42zPFBk3jk3jRYMhwiMMiGchWvRq719xrD3FxRzSfZ89Xbp2r7PANuTxX_Dag3zW79DWyoSbV2uFTzonelq6C4qGdoylBsF0b0b6MgqSF_hMy1oCALPy08gJtNezMg_4flN9azfcn49ZFJxDXjHKgSSUvl6tdpNopboIVnXG-2NFWoboWtVKkbbzbQ1zMtyxql6ezAIJG_G9dWteRhtmc1q3goFnmVr4b-C9emd9DCt6lTDNo_gww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت فوتبالیا اوایل هر فصل
🤧
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/102397" target="_blank">📅 09:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102396">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e396ec62ed.mp4?token=K9Xu0tfGRLO527-WmIfmGnIlRdF-c-_fLfnTM0XObherdKjYpKRQ6nicYdkXtujkzIxIU5-CU6Jq1CNLa8oWBKX15NsJ7SsoBLU2iFZmpvsNEtWgoKdiL9IIBZpsP3h6zzZwtk8KZ661UaG9hRrF2FwOrclY2nmGERB3zaRXRHedGXLqSoG7EJSPj1X4E_hc8saftpCdD5_kcODynJmP78ah7fGcXsAP3qKSi_JXsimPEOtxyhhlA8P4dts2T_Cxp1wgIqz2eIZa4YFtp-XhLcj6HNmnf6-StbWwmpjTjmlegAWp_2epZjwoWJomqRYT1F_669aqOL0MNeWwamKt5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e396ec62ed.mp4?token=K9Xu0tfGRLO527-WmIfmGnIlRdF-c-_fLfnTM0XObherdKjYpKRQ6nicYdkXtujkzIxIU5-CU6Jq1CNLa8oWBKX15NsJ7SsoBLU2iFZmpvsNEtWgoKdiL9IIBZpsP3h6zzZwtk8KZ661UaG9hRrF2FwOrclY2nmGERB3zaRXRHedGXLqSoG7EJSPj1X4E_hc8saftpCdD5_kcODynJmP78ah7fGcXsAP3qKSi_JXsimPEOtxyhhlA8P4dts2T_Cxp1wgIqz2eIZa4YFtp-XhLcj6HNmnf6-StbWwmpjTjmlegAWp_2epZjwoWJomqRYT1F_669aqOL0MNeWwamKt5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
نظر پرز وقتی مورینیو میگه وینیسیوس رو بدیم به تیم‌های دیگه تو این پنجره نقل و انتقالاتی...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102396" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102395">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WH4LnzKuDrbl2nP67mCS3TcEXeWuMMXC9vp-fLWm04DgKnk0LxInFe15Hy-RpmXKFvy6c70h72EB5gau0Mfnkm2Yihe9QF4quMRrI4dTZnIybbHK0dNQ6win25DMKSbBGyYJ_lSuIRUoOP8wW2YNbi2B1HOh8RoMxMrJ1XzyT2SqKYuSSbHT-Va5y-z2NPRJaFtS_ipH4y5B0pxptFkO_z6STd9FATLvAJxEjgFq5SHitjCJ4orzM_R2JHK9nl61RRsh_-z2qVxjdfxnNTYjiZ2xrZh5YntnIsRzHtbiSyBAbvTRMiz0Z95AwucsDqj0Erjd4NWLolTj74SbuHNoPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🗞
رومانو: حاضرم قسم‌بخورم که دیومانده بازیکن رئال‌مادرید شده و فقط تا وقتی لایپزیگ بازیکن جدیدی نگیره قراره رونمایی رسمی انجام نشه. اگر این اتفاق نیفتاده باشه از حرفه‌ خبرنگاری خودم کنار میرم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/102395" target="_blank">📅 03:13 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
