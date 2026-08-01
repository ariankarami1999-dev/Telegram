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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 13:43:38</div>
<hr>

<div class="tg-post" id="msg-102501">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5_UNSbE9Qu_pK2H1HNcqfmW2R2dCCRogR-IZFVCOAfymIzGPfs1GPv_HXK1eP7nzMZvtinc82IvbFDKYWAQETBrgu-RYhIqjLirTEpNcC_71Vkb1hA-Ers9yE9BeH9fwZCG2TI8IWLIaYsxT0axQrkUp9BCDfPITOQGIEvn-B65wAA4MOXJhR8DochNeg0AcYZzxcavyAa_FwmrLR1lLeVWXGZ7L7M63zqjQuje5biHYelo_5fR13lg1fiCgFjQcYjgR7yYkZiF7XQtqA1JDRPk3XPZ13ne5UohziO1lG9cUr__qeb7jXn37BpNuyUL_ifgjGmZvxkjGNhZXLqLiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رامون آلوارز:
اطرافیان وینی هرگونه توافق بین این بازیکن و آرسنال رو تکذیب کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/Futball180TV/102501" target="_blank">📅 13:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102500">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sf8w7pDq2_8_iBSSw5wv16uoA9yT5S6kXwFj3SzB9CIKis46zEBUWTe0Rjd2EM2lGWbuNV1RKl50NYMWH11UtJtshaLIZ719Wvtm6Rfi6C_y0Tf0eSu6qntsHQtS-2gpHVTLRFEremGlfyxKKTk7SUaHgNdQSaMH5AtOXR5GurqiezDJPR3RewaCCIZ_5YIxYlZTY4nvs90m_6-UIIRAXHpPeS1VbnhiDk7VzS5gcwFdoV3sRAol70mTciHq9nhsadnENZeFxGptaY6lZW9k8RqxTIP7c874gwhif5ZxbxRgQvahv_d_fq6BT8U0h8-cG08pChTizNuQUzwg7avobg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
• کریستیانو رونالدو به یک ویدیوی کوتاه در اینستاگرام که او را به عنوان مشهورترین ورزشکار تاریخ معرفی می‌کند، پاسخ داد:
"خیلی ساده."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/Futball180TV/102500" target="_blank">📅 12:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102499">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/102499" target="_blank">📅 11:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102498">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/102498" target="_blank">📅 11:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102497">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwRvnMfsoc2UOnS7sJYlnX2akiSBMBc0dyqn0aG4vBr4tAfdpH5zs_nYESkqgn23gWdC9cqQrA3q76StUgtE7RU-kdrEYzIP7ebH-UyKCnae8IYOrxnU9oZyb-UglwpFLq7KcuccWIn4PpVBQgc1Y4Za-X4L6s47B0xN84AWaqzCyJDTtsPrmWheJ09Mcxuc9fMh31KqKfayqpPWcvvK9rQZRHMJzjZW74zO8YW7U6ewewxNtx4UqYrUj5NU5GJOVRRoxRYHFR4GqLgidM7lJyiggDTsvTSIDgnMsfvnkyuNZx_2g-oGcPIm4kp1Tj9vzF7ONQTPm0C4wFGjcYjvRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
اینفانتینو با انتشار بیانیه‌ای اعلام کرد که طرح فروش بخشی از سود جام جهانی به شرکت‌های سرمایه‌گذاری خصوصی، به طور کامل لغو شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/102497" target="_blank">📅 11:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102496">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/102496" target="_blank">📅 11:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102495">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👀
🔥
هشت سوپرپاس‌گل ثبت‌شده فصول اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/102495" target="_blank">📅 10:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102494">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LuDUKzJs5mE5KePnwIeMi_1iQ9AbhKM0KCULlVIXto517-6VTVbIIQ7QUsAJe9EMj5aQXrvlYEePC0PCAU1_GhBElQfz9LrfibsU1vw6y8s19JnUW_5BjUJg2Fy366aKzrkTfVRJ5Fn5rW0RkBpLt8IKGJRurQEF_bhjpxmHbxksR23HjTxhQvb9lQ6o9PBYyuPc2lWnbmbhHONDBxCAl6C3bCwHHAxtNTmPr3aSLQG1GstnubTJwqVy-FloBtnD5En1_N59tbJwAiU-hPBubG5H5cW0rL2kT56CKIB6BxF0Ss-p19ygQSPCyUm8HH98GIYLZRlPxdqf5Jg_KzsQTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه آمار مسی و هالند زیر نظر پپ‌گواردیولا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/102494" target="_blank">📅 10:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102493">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvfujV1Z40npbDQYKOnmQyKyWhpoGRO_5YZ6ts1LZuQCHpVjwCfDi2YFbhq-HSrVhFhiet9LKjwQo6Qijo19cCBF42ohyO-IRJ54e1qbSeoWyfQf_EKTHU7Logz87Nx7HaM1KA9_s6GWfpmvzYHy_Ga4IsYa1aCY5KoSSjciSvpHLaDnO_s2eUK7KBd_bkc0PwQDSn6r7LieHLPO7zmqs5La6bXPpah40y0-8_yXAkpbwWoOhKKLECW8IXxpBtoyRn4eXtyybgAEpqK_xvzmbdwaaHGb6CGAvbCmFu98pWeaipP1De8y2c1Dk74d_mBR4kv1PJKf38pcfIO0S6tAhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تمام قهرمانان ادوار مختلف پریمیرلیگ ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/102493" target="_blank">📅 10:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102492">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/102492" target="_blank">📅 09:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102491">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5RQ4eI3U8Fm-COxxW8lK1aodHNFLoJsLSt-zgbKJ9NA5SVkfnQJKSv0MthjWxovUGeEbjZZqEULNyV6719LQzuVPli2ZhCXyJzChLHuUVeSjhKF0jnippBB0D48ALHSyhJ8QbTl2CiGIHRK5Nib5vG7ZRRQkzKQHyQW96CtHBlBeNZMCcyIk0q_n3pXEbCxBH7r74iZo9b92z0RT_0eDMyTn5zSEw_KCRr9VcC22t2uTNbMC2eKfLMgHKszWErD9xKlKzti6_MF9ZxpL6sUcX_ObiFtI5-5ic-ijmtKfmQdYqXb1kHYOXcpoG0IfadL2vmVbd4KjeYskQUgdbnOXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
🇫🇷
فوریییییی از فابریزیو رومانو: پاریس بازم وینگر خرید! مگنس آکلیوش، وینگر راست ۲۴ ساله موناکو به پاریسن ژرمن پیوست. مبلغ انتقال ۵۰ میلیون‌یورو و تا سال ۲۰۳۱؛
هیر وی گو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/102491" target="_blank">📅 09:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102490">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/102490" target="_blank">📅 09:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102489">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">هایلایتی‌از بازی‌جذاب الکلاسیکو در فصل ۲۰۱۲/۱۳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/102489" target="_blank">📅 09:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102488">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7q3yDIgOI6aD9ghFxhJoTVh4n0mdf0EeF7cgAIfUN5UaLBoPodJQ7fABvyAn0A2_IgWzidZd3yq5DiHSmahw9bcm1nB38TQqsMUkKNQNcA_0MuuDDfNha7Knt32VAYGrrEZvbmKYsxg6MYEwnMuARJij9-XoaotDAR0ExOgGsUY5Rm6vwpUbbpXfu8NP-tLVuY5MYgB8Ihzi5rs2f4-K4q-49zAwKwT8Bt4a8htqvVmlWMMK2OvNvvPZt6ZuNJsZwb5iMZDPRK7Q1JLYmS4wbrzCgG-d21RNsksDExh0clfkcjk5TlfLY4LJWfazfydvawqu-mfCFJNPie0lGxpuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیکنای اون ترکیب لجندری بارسا چی میخوردن؟
مسی عالیه :)))))))))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102488" target="_blank">📅 05:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102486">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eF96ltloueL5yidqKhK4m68FdV-Hf77RpL3qW0DjoSWIKRQTDvTivyZmUlrR07YqjffZYq20j3BYGtIYQ8LDLxEXOb_vHcWYmGYtFv5mkywik77SJG4uy7KMpK0f4UpeGAlNnsUNhm30l8vsK1L-Z7WoHxBFfNTHYYTrXDWTQ5jr-oP-hUYLY-VLbBaMaOHkL7L_8cLTbYAc3186RQNUpqdOOBCYSjBGDGBnlfVdUqpSdwCDmr-BQOlK0ffwhemuA9I3UgZgkop8NQR6dvhE8r_w6dNF587G1dRss8f35KzuaMOiLsXTjyjVJ6sRO4xmLZ6Feifn0NBNwZYcjPLHnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
گوئدس ستاره باشگاه آژاکس با رقم ۵۰ میلیون یورو بزودی به psg ملحق خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102486" target="_blank">📅 02:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102485">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
🇮🇱
کانال ۱۲ اسرائیل: نتانیاهو در دیدار اخیر با ترامپ موفق به راضی کردن رئیس جمهور آمریکا برای بمباران زیرساخت‌های انرژی ایران کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102485" target="_blank">📅 01:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102484">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBDbcvg28_Hz6BEMr8Yg2JZMWZmlOCkl1LZl2eaF7rQZbBY_KItzWgN-U6b0Afcs4Sa2614MML0GZ_5Ccw_4blsgTgMC3auPs1bQuZ8QzMh6E5zdKZckeI1h6esVE74t2qF3d4WNxMC8Yc9BwYVuL3G8fwdiKJcsuM58QCn3fvyl_Trb72FeRRosojDwyNjyUoSZ8_M_qO_65AFhoE58J0M36kOL_TP6BSB7pHWAvLw1UaS4E00WPc3fjwkuLw9ce9Mjd1Rvvr08OqNNm_nERHwjzSvzr7uHiK8ufIXGXfWcw8dlZSQQrcRkOyg41m_tMtnb2Zo179uLcOsEVUTgpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب بروبچ محله تامی شلبی حسابی واسه جود سنگ تموم گذاشتن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102484" target="_blank">📅 01:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102483">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔝
وال استریت ژورنال در خبری فوری از صدور فرمان ترامپ برای آغاز یک حمله نظامی جدید آمریکا به ایران خبر داده که می‌تواند بزودی در این آخر هفته (شنبه و یکشنبه) آغاز شود و چند روز طول بکشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/102483" target="_blank">📅 01:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102482">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edBSh1GaeRuz_SnJxCe5heoOIidGWrOlkBi4pdNa_Ybi_mWeqsTS61lTv2C0PauZ9jUPilccCnod-EgQAlFJ6a63Y-FItjqTHRJTaBGqcl_PQPJ8BMT5vx3n9WJS2XIoRgKL2YpY6R6XYm5qT2q-wXY2osRlAT0jxsdnigDNibr5sVcfp4SINpnH3W4nmZEb7yEVzehx3nWVJ1LwsAcaRLnSv5WskzD0mi3SIRY37VRlYAY8s5QKyYaxwymBJNjeqmUma0HB62tBaTy-NU_if1q2Nin74ynFXTSoM4LnJ8tWZa_93tmBU-J3-dbTdRdvULplIIrpoJRq7y35TJTtKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔝
وال استریت ژورنال در خبری فوری از صدور فرمان ترامپ برای آغاز یک حمله نظامی جدید آمریکا به ایران خبر داده که می‌تواند بزودی در این آخر هفته (شنبه و یکشنبه) آغاز شود و چند روز طول بکشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102482" target="_blank">📅 01:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102479">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y1lY4nX_NS_1lGl76WSpFtpCttQvzASce0ln1DlP_oDEJRzHqR35SfCbeLIGQft_dvHjRD78kE2boANSDaMPuUAnytaSs2ajyFz1dUnqgSBYFDQlFdUPmBrIxhNbWkKiNwTydXBXV9nr4y8pm7Eb5fng0BZIFpNzmCLykbYCmPIz_ViVBYbC_j-1Qq6aVOQckY6iwK57oFiWo2Bo4_kUW8XPFFOL__cE1ugKDAQB69KslFTRKYVkrDzLpYnruDPxpqcsSZ9kzod1yjt586HPLm8aCKhSz5LFQ1I-dwacSA8c3qVsSlhTBUSCk8prnu7qHS5JCHdbVQHPxkB2VRhMXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gBoC4qO03lwN-ZQ7eQbFbimIdBUhe5fB7qogfmvdVgHIKfK3cqKoDAXNmFtD3jkUHw0oma7DSwI1kIZVcHkxrwJLVGzs_nhUjmUyOIny2iaVjLt5isJWayHswnfR58JTMlY4E3DMnz68-KY06XQabH1z0m1cPMWaORi-UpbCLlHFFjzmyQb0ylwrGPrPdS69vgHyqm9GJzPK6e6VQwbqomMg5NFbD-9pnk8M-p5zRb5oWFwU4HbtrsBpXvS6qPQbzgvtNYN-fVNS5ypCJJzY85dNTKK_rM67EEwwr2SjYC1zpGyxeue6sGQO27XOIt30d1JDgdEBBfpOFRyxNF95Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j6deKlP5xYjwdAoUOsYZWyb2kHDXxua9_mr4Ds00_R3I7P-MnO48rYPvWKHBQS2XeHUiEt_XhdDbGmlL1o9UVEd-wc2zPXhaSdFxUyw2j1H4kNVJ_IhausjpfkPpfGG_leRxuIzdbcKOtvRlBAto4CigvJphR9QpkBjMNXIW5JoigvLLTn_3JvvyVlk0qDqr-hW47z1ndexKD_KvMb-Qp6nk6RYoD8p6_m4Koq6mxh-CFl7bYEcQAVmkJjdzzmjrkTA9Tusxm_Xh2xNXAbmNsuBZN5AAb7m-T_srYURCjqm3RgOjPWfCV_ZclsioqPyDjaKLccOJhdHXWV6CmBW9Qg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
باشگاه فوق العاده محبوب آگزبورگ از کیت خودش رونمایی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102479" target="_blank">📅 00:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102478">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LG5ad1so2sO4mttE7gPjjNZVl9OVyqAwJEasYSKI2ibVSICOsHCbjh2ylvjdIWWmxYfG5M9zz_q0Ocnz03LD7y5kN4FZXGQRAzXSKGogfbPvtdQr18FML1aunBfra9juTQsVIjK_J50Uw1DO9NPb0-IX9antrnOb5S8r1MFyyZFcjF4ru_NU1w7VJFp0x1xkXJ3jKhANhZe9ZEKqfs97EaLGi_0qSZrlYX5VuT7L4clAy8lySvZGnEP_SxXJUTkOvho5YttB6fKREM3v9CdNghBZ-JuEJs2C1kqz-ybFfgNmWt5bYnppctt_cUN9BS3r7AMReZm0LJLaSh1uUQvv4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
هندآف آرسنال رسانه نزدیک به آرسنال:
وینیسیوس شخصا با آرسنال به توافق رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102478" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102477">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی،…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102477" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102476">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=aw47Xtb3HbB9GkYymDtnBBeJU-4rssR8FutAHmQVSG1paoF4qSyv-40aJ3z6HN59HggTxUgiPqToQ51JJSM_fB-1vHm063sgF3DP2ZhA50QH6-sQDusiOoLspzMJ5xTbvfYEyciZCbv_sTJFB9ahM1fktBlQl9hL-Q1CMc9VChnPBTXmX63DACr5eLyW9CLKdfeCfnhPbAFWXKleLbxfL8Y1SWIyVh8NvMDQJVEOs6gj87fp55UdiFc1Od_DwcQ1NNp1GxZhKIBLZE8m8jG2I3UXn0AHDjh9k0O8-x66VcVQ3eyJn7HuK1Xn0WSwvgI0TmfrhQjX35dcMPgHPZatpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=aw47Xtb3HbB9GkYymDtnBBeJU-4rssR8FutAHmQVSG1paoF4qSyv-40aJ3z6HN59HggTxUgiPqToQ51JJSM_fB-1vHm063sgF3DP2ZhA50QH6-sQDusiOoLspzMJ5xTbvfYEyciZCbv_sTJFB9ahM1fktBlQl9hL-Q1CMc9VChnPBTXmX63DACr5eLyW9CLKdfeCfnhPbAFWXKleLbxfL8Y1SWIyVh8NvMDQJVEOs6gj87fp55UdiFc1Od_DwcQ1NNp1GxZhKIBLZE8m8jG2I3UXn0AHDjh9k0O8-x66VcVQ3eyJn7HuK1Xn0WSwvgI0TmfrhQjX35dcMPgHPZatpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102476" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102475">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GM9WkHhC9DUmoawt2xycjRetnyrf-4yS2j-9667SYNNdO6q6bwsoGRpPyDaCM4Ap321fFOyGLIuK45gPo6lQHZcUw6dlpxkbUQTl-8Wm4mXkA3f0XEaWpYhOULujqjV--WXrS_-rPD2sB2HQyRvhYSedQjRjSbkeyoD1JXeY4ZKBTWD5c1QdqZZaus1UNCGpdzlwtNlMDEpZ_2XM-TRpL4nmbmY3BJ0E7f-72XZiRlBPYYRJLzwe87mb5nTpeRZ9sGZRpg3nit2Eh6tJznQwRNI8qHfFJyw9aWMsJBy7CK3s2B5vknk5-XkiWKW_SQzDOm3IRhiD5JRxjTtdJcpHRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
بارسلونا در یک بازی دوستانه مقابل بیرمینگام شکست خورد. بیرمینگام با نتیجه 3 بر 2 در ضربات پنالتی به پیروزی رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102475" target="_blank">📅 00:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102474">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_BkpDi_CrVjcD417jVQEzkBg7vqTa95cJWUbU--fuo4YQ_HMSn2M6q_Imp82UhpxfT4MoApdIY6HAzU2tSGHeAy_GsNi4l2bNNwcu35vOjFBWEDf1RaXR5hoX6_qHTjpvIjMvNbmLzq-E-pERXzzsKkCZi16vFGL8aJCHScW0dtihg4-7qQrly7OCHbBqlvGakBwxzQGV0fLim-LHtjFZIiXPzeTOwavIMiWcxihGcwWNuYqDDEQKskJDJDzEpAfjM2G9aWpA_dr58wS_b-ZdWdVZXCvi4jo-cDwqDOEer4F9Lees3a8P4rQ-3Lqt7gRlxp5dSLCkaoTbKS2e0jTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری دوست دختر یامال
😦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102474" target="_blank">📅 00:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102473">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZ8I_VRhIrXhqgmSMqD6cpn2C-fbM8FaBW6gxw3L5DPyuoZlxIUXht_MgJlYd8s2I5Rbu6Xx2rPQXYwPYf6M4_uOz-HReEZRaQGWEtRt08tO0Dare-mykYemrjc4--K6vKm3I5ude4UkXQxEoxnUpxaQNdEI7mCgayf5LpEtkSjXyXMPFIQQB-SxUXkVNpHHEM6tw86wfeaFMoUEZF1PvGwi8WBDDE4hwaFlRVhPj40PgLm2C8qIvYKfuuar9rQ2RhmnNX_syHkgvhay68AzJZ24LpRQhuo7G1NcYYfdp86gCX0y9DNy15zFG6rJvk9xNZJijIkRfzC7KHlruvyZdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟥
🤩
خداحافظی امید عالیشاه با هواداران پس از 13 سال حضور در پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102473" target="_blank">📅 23:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102472">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYMY_npcHC27ZR1mbnaIoDetbNK691Dni1nICiwb4QbGg-moErDachdvtdJV90vFMr3j_XjKRDOuYaZZJg9Strk8XqyY9xO4PWAlQ24BOXox8fAk7KATvL6NeSRmcLt1_iPTK6GNF_dxB8pFOEylCo2-1FEOtREdx4wTUWk5UYpf-dIksvc4PdcWo3fToLGIw9mxqV6RnnhDkUCMgBFbWzIClBMIsM7nO3MLpnu0ZNWkBJWWHiHSh4OpFFW7TWAKNjj_361zT5yVPleZcSueRVInDyz-TQq4ax67rrYdF8qYOFOJyQHFQ8SgONgRIT7fPKPKX-tsi1tpnLswLHiZpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
مسی و کاسمیرو تو تمرینات اینترمیامی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102472" target="_blank">📅 23:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102471">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26c665525c.mp4?token=BQsn3z5YJg5qOtHNPHWkpJgr40AlilwKMHnEXX6owxl0Wa4DjP1eKfaJ5VJaTMWDna-EYJ-iujms8cihJcKqZGcsf_XFBTwYBTWy4epDJI_Dbg_Zy6XsJf05IZSZUPZfPy3akvq8e8JXQQdFLzDk4VpjGqwHhaco75IoOHerwTgscxdHHV8siSCmpsZqwv9EihhSgfqGvWYJqIzHK_eJNjedOb_iQ1T2iwBVHIPDTkmjvFQJTwrN1tJ1Mf49z_smwP4vDOyLx5EptTEwDUEzwhoVGMN9TqHeFJY4NCK3V6WfPkUC5rooVoqjuFaqpTmRhNGzRktAVXIL7ohEOG0oQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26c665525c.mp4?token=BQsn3z5YJg5qOtHNPHWkpJgr40AlilwKMHnEXX6owxl0Wa4DjP1eKfaJ5VJaTMWDna-EYJ-iujms8cihJcKqZGcsf_XFBTwYBTWy4epDJI_Dbg_Zy6XsJf05IZSZUPZfPy3akvq8e8JXQQdFLzDk4VpjGqwHhaco75IoOHerwTgscxdHHV8siSCmpsZqwv9EihhSgfqGvWYJqIzHK_eJNjedOb_iQ1T2iwBVHIPDTkmjvFQJTwrN1tJ1Mf49z_smwP4vDOyLx5EptTEwDUEzwhoVGMN9TqHeFJY4NCK3V6WfPkUC5rooVoqjuFaqpTmRhNGzRktAVXIL7ohEOG0oQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین ووزینیا که تو جام‌جهانی تک تک تیما رو سرویس کرده بود، جلوی علی علیپور اینجوری فحش خورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102471" target="_blank">📅 22:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102470">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtvBjDgbRoJAy7FsvLzBqKBIRZABnggEdppkgmKFJFnbfNgu1hh0rVj2Bw84y2NGhoH4Lr_lqSi5_h-TaSvCD1eUHFzxZYAJOh3fvYqCkC1-cr9sOXrVukNAycoTNYoex8g38WXHt-F4uacldeB11Y9maNYaIhD53l4hzz1DZHN-PyvgYjEw4OuF41ckPx8-RFKvrG2SgVvwFnbQKfd2lnpJIr5A72hlcLXIgjQZxN_-XeZNY6K9IW254YFQ6K10Z1uvCaNXGYyhKfqldFIsd8fQhJ4CibwV7So11mdd76C6I0_hn_bj5XLnOOEeEDhkoNekVCwpE0cSRW7XjvnSIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ار‌ام‌سی:
مندی تو وضعیت مالی بدی قرار گرفته در حدی‌ که مدال و کاپ جام جهانی خودشو 54 هزار یورو فروخته.
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102470" target="_blank">📅 22:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102469">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/261dc7eb19.mp4?token=V-1n8XsL_AqY7QcFAa9pgA7wEXxSwsFYA23PrsdvLPucBVKDc7GxJlJaxKqkHoxL73-Dd_K38UZ0p73JFm6m2DL9XNOwOV9jVMaz4qmDe91zd9wDUhtV9maFrYGoCFkrIur-qWSyW7mCvLiCWVqZ6asFnLZ8EOTVu1i_JcuVjFnm4u5lsgD9_g2lAJuCbwo7smS2Por3LhRRwEG-82wk9bHJy_OE_eF_jE2wEh9hCNaYJEvpC7DFdY5ovD9zhpm3mRDaWm24tciRooD8_Nk3dy5kxgFLRQ59JPxJcfWbDME-g2SAGGryZRHaJt_lUqnOGxSRdNFwHUH3uXGXkhOv7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/261dc7eb19.mp4?token=V-1n8XsL_AqY7QcFAa9pgA7wEXxSwsFYA23PrsdvLPucBVKDc7GxJlJaxKqkHoxL73-Dd_K38UZ0p73JFm6m2DL9XNOwOV9jVMaz4qmDe91zd9wDUhtV9maFrYGoCFkrIur-qWSyW7mCvLiCWVqZ6asFnLZ8EOTVu1i_JcuVjFnm4u5lsgD9_g2lAJuCbwo7smS2Por3LhRRwEG-82wk9bHJy_OE_eF_jE2wEh9hCNaYJEvpC7DFdY5ovD9zhpm3mRDaWm24tciRooD8_Nk3dy5kxgFLRQ59JPxJcfWbDME-g2SAGGryZRHaJt_lUqnOGxSRdNFwHUH3uXGXkhOv7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
تام هالند یک‌بار به ارلینگ هالند دایرکت داد و از او خواست به تاتنهام بیاید، اما ارلینگ اصلاً متوجه نشد فرستنده، بازیگر اسپایدرمن است. بعد از اینکه ماجرا جنجالی شد، هالند برای تام پیام فرستاد و توضیح داد هیچ قصدی برای بی‌احترامی نداشته و فقط او را نشناخته بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102469" target="_blank">📅 22:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102468">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjJAhr05LZaBk5oKwHpp0bYN_dHbNaQyz8XmxlLVGX328HrqaglR5RPL-T0Ii1Fe5zDL2ajJmK0qiNbddeqGS1bAbb-2n0pFHhEAXp_8x0G9HnhSV_biaUkHZ_c0xk8NnXngSP8aIw715IEj13cboQhX6uc8F18n_pq6M8XfenGsVVJPOOuSj-Y8Z5prfIfIrGN9-KexbzefKLZ9QEBPq8cTmFr1xYJlSPLW_ecsjakNTe3mZ2smpiSS48QpojggfQ7Ep1niN3ERQuWm3mNXiJHJPFkXNpH7fqUlBe6hdMIhO6bYRdJLaHQGV5DrDOlVaLzPSfmazYDCsGaEkEpLpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
💣
بمب لاپورتا ترکید:
جسی بیسیوو، وینگر بلژیکی کلوب بروژ،
به بارسلونا پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102468" target="_blank">📅 21:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102467">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHDnfLXGtouDvPMFsCjcB483Dh98Iy9YhSyyZLR6KsbFU074sb-2tx_5hKqpcqnCubPnMOQaD_Q7ih2dx_tV_FXSLp7TpC497he3nOFEuvj9foTQMUuu2mxHFo_uj2yHlKF4tPFe5wCzi07qv99ggyyPM-C0f2BG2Tn66gAotAbKmGT2t2J5vKGh9G-nXc3_yRy23wjvdffnLBfAbaYx7js9MSuUDneeIath6sQHSYLpFV18oTP0gizAi16z-sVJgUoZxp6KMm6Y0UHRSPLZmvbWB2SissxoI_n3JetetoyUGRk3E61v8VcmFaIPNnyMkeRBA_ciZt4EQ6q_ZGszzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب امشب بارسلونا در بازی دوستانه مقابل بیرمنگام‌سیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102467" target="_blank">📅 21:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102466">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f4d6d3d7.mp4?token=NCXpSSyqmadvMi0cW2Q7WIuB3Y3iTUuks60nObNGlneMgUo96J575c8KoT91WBtmsIwk5c3WF6ex8JVXcCyOL40bvRVm0281L4wppOXSdBLAF1UXwsd-04kBvXMTHZds_-lxfDpRvHuGYxCRned5LtLRlHn1tITisQkMs8-8OucIjB-AmSTbuSd9frxSRZbgT2BeEfIGBCW5CVIgp6dkKGqXAfLRYuhyKrVC5-a6wYglNIL2NnlV2EcYC7zB7FsU7Vy3qHkdzkdOtWGfxJNd1kUu_E5bUbTf8OQqMiC7C0HdAJWbToz76GqepeP1Zpq6rCmYnaIzgSZ3L0yvoJ48ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f4d6d3d7.mp4?token=NCXpSSyqmadvMi0cW2Q7WIuB3Y3iTUuks60nObNGlneMgUo96J575c8KoT91WBtmsIwk5c3WF6ex8JVXcCyOL40bvRVm0281L4wppOXSdBLAF1UXwsd-04kBvXMTHZds_-lxfDpRvHuGYxCRned5LtLRlHn1tITisQkMs8-8OucIjB-AmSTbuSd9frxSRZbgT2BeEfIGBCW5CVIgp6dkKGqXAfLRYuhyKrVC5-a6wYglNIL2NnlV2EcYC7zB7FsU7Vy3qHkdzkdOtWGfxJNd1kUu_E5bUbTf8OQqMiC7C0HdAJWbToz76GqepeP1Zpq6rCmYnaIzgSZ3L0yvoJ48ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔹
وقتی منچسترسیتی حریف پیکان نشد! سال ۲۰۰۲ پیکان با سرمربی‌گری ذوالفقارنسب برای آمادگی در رقابت‌های لیگ برتر، یک اردو در انگلیس برگزار کرد که در بازی دوستانه مقابل منچسترسیتی موفق به توقف این تیم شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102466" target="_blank">📅 21:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102465">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bcb0e2d66.mp4?token=T32AzjsmXtIgJ8KmTfiibuVTZF756e8N-_zwYdNNsGLRGfZrw2o2xYXVhdZHukx6zEyMHEBFxOcXsdz8ceibqz-nex4ChunDT1pzkrQwafXcC9KAVrcGN7ncNzqJQGUq92tPIlZ9TFQZSvol72PIIsm7a-uS3anMPBraIJf2pxNJhM1V-0DEW2Uftzgr7CI9mQjl80gk6KFoDMgs_vs20BT76OIR74Chj-_7xLKaDSdBMDEeExgH0BkWnAbUH92V7nqmaDPzVYTwGoT-avEbKztHIeI-t1pO7mA34H4D1APtO7oQU_6W4UF0j9hjEyzlUEXEauR82PSXKznL8btHLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bcb0e2d66.mp4?token=T32AzjsmXtIgJ8KmTfiibuVTZF756e8N-_zwYdNNsGLRGfZrw2o2xYXVhdZHukx6zEyMHEBFxOcXsdz8ceibqz-nex4ChunDT1pzkrQwafXcC9KAVrcGN7ncNzqJQGUq92tPIlZ9TFQZSvol72PIIsm7a-uS3anMPBraIJf2pxNJhM1V-0DEW2Uftzgr7CI9mQjl80gk6KFoDMgs_vs20BT76OIR74Chj-_7xLKaDSdBMDEeExgH0BkWnAbUH92V7nqmaDPzVYTwGoT-avEbKztHIeI-t1pO7mA34H4D1APtO7oQU_6W4UF0j9hjEyzlUEXEauR82PSXKznL8btHLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⚪️
رونالدو چرا رئال رو ترک کرد؟ شرح ماجرای جدایی اسطوره فوتبال از زبان خودش.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102465" target="_blank">📅 21:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102464">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ed94c011.mp4?token=VaPLf3l2kT9NKdhjeu12yI3O5htzcTxua8H-qOCinTNanPl9F8_sDUp6uAo7KuC3-3VMwgUCg7Nr-tpeuIxu8h9IoBTFMyD7qqhjO64ma4I393jm2LHCgsT_VLRu0o6Jdv5bug1VXKCl7EXtfEqTimPRQ08uPXCS3z06c-YP7ZSULeG71eHi6ltJFHDV3IKTjbe_yIHJsAIlB3UUmRjaukJHrATYJpBsi75pdpb0G91qxAQ7gepUhQ9HItroSB5OIWKp9PaVynToL6VfLOxqSSYHDy6aoe83hwBrNZovIXzR0ftLNbKd2Rhc5q-2Ya9nH6uEtqOQgCw-1648Otb-qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ed94c011.mp4?token=VaPLf3l2kT9NKdhjeu12yI3O5htzcTxua8H-qOCinTNanPl9F8_sDUp6uAo7KuC3-3VMwgUCg7Nr-tpeuIxu8h9IoBTFMyD7qqhjO64ma4I393jm2LHCgsT_VLRu0o6Jdv5bug1VXKCl7EXtfEqTimPRQ08uPXCS3z06c-YP7ZSULeG71eHi6ltJFHDV3IKTjbe_yIHJsAIlB3UUmRjaukJHrATYJpBsi75pdpb0G91qxAQ7gepUhQ9HItroSB5OIWKp9PaVynToL6VfLOxqSSYHDy6aoe83hwBrNZovIXzR0ftLNbKd2Rhc5q-2Ya9nH6uEtqOQgCw-1648Otb-qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یک تازه داماد پرسپولیس را حذف کرد!
از ماه عسل برگشته بود و چهار ماه حتی توپ به پاهاش نخورده بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102464" target="_blank">📅 21:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102462">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🔵
🟠
استقلال در نیمه‌اول مقابل فولاد با تک‌گل ابوالفضل رزاق‌پور شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102462" target="_blank">📅 20:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102461">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f8b6948d3.mp4?token=FJjh-TZXDgnf3E5VYZbRvSXsl63DboUaVzRP6v6Wh75ES1Ff_8N88r7Aw9R8fZwwMUtOmwvwe6onb16eDZdNs70d_6mQQPzq2JXnTE5CX9DSWL1pgMFdTFN4lgZBSySOyetjXvCooZfviB1fSky02mUVV5rUzSTTQyVl02p3EzH_XrIxABhgCzI2uCQNLvf7pVKZdjwmZcpe6LixHIHuWkVIPPHG_wDDnjG3mew_-TGzxtrKEOkrYiYtyvMIYWkBP_vWv5W66GP2FTMVNTMqr_7V4cn9dlcjrNvU5g2sa6mb8Jsm8TsPAStlIroctrcTh8GpFU_HMeTC0bZLrma5GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f8b6948d3.mp4?token=FJjh-TZXDgnf3E5VYZbRvSXsl63DboUaVzRP6v6Wh75ES1Ff_8N88r7Aw9R8fZwwMUtOmwvwe6onb16eDZdNs70d_6mQQPzq2JXnTE5CX9DSWL1pgMFdTFN4lgZBSySOyetjXvCooZfviB1fSky02mUVV5rUzSTTQyVl02p3EzH_XrIxABhgCzI2uCQNLvf7pVKZdjwmZcpe6LixHIHuWkVIPPHG_wDDnjG3mew_-TGzxtrKEOkrYiYtyvMIYWkBP_vWv5W66GP2FTMVNTMqr_7V4cn9dlcjrNvU5g2sa6mb8Jsm8TsPAStlIroctrcTh8GpFU_HMeTC0bZLrma5GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شزنی جنس رسیده بهش و مشغول دلقک‌بازی تو تمرین بارساست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102461" target="_blank">📅 20:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102460">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ace3163b65.mp4?token=tgSDTrUn6R3D9BeGCHW1lFzyWUgh-hPKlwxh25tpNDXUho12_a5xhoUFAiFCT3TG4vprB-eNoiJeKsMeC2myToABXPpKS8RjrdiqyCrOgAizW3t7G7OxORK134_4UzCdp_3RE6629A2-jcS6Q3SzY02UEa0Bu3wq-53dAIJJuObhdxOhNZ_E0ffUgmcGIELUn3PRx4E2Gkp3U3l1O9JFF7yYR3TdpxhFtclbHd9K2KoyHxpEr1SfCZz3eqqH2d7z7Q5CbdWetz9-JA3Ho2coxWZb_9mdmK0pCAITgIeWB2PQ8gxRn-Xg69xqu8VFlXjn6FBdhtITDwXk_DOdYIRuYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ace3163b65.mp4?token=tgSDTrUn6R3D9BeGCHW1lFzyWUgh-hPKlwxh25tpNDXUho12_a5xhoUFAiFCT3TG4vprB-eNoiJeKsMeC2myToABXPpKS8RjrdiqyCrOgAizW3t7G7OxORK134_4UzCdp_3RE6629A2-jcS6Q3SzY02UEa0Bu3wq-53dAIJJuObhdxOhNZ_E0ffUgmcGIELUn3PRx4E2Gkp3U3l1O9JFF7yYR3TdpxhFtclbHd9K2KoyHxpEr1SfCZz3eqqH2d7z7Q5CbdWetz9-JA3Ho2coxWZb_9mdmK0pCAITgIeWB2PQ8gxRn-Xg69xqu8VFlXjn6FBdhtITDwXk_DOdYIRuYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کول پالمر:
برای بازی مکزیک - انگلیس بیدار موندم، ولی بین دو نیمه خوابم برد!
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102460" target="_blank">📅 20:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102459">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhtgBuSIVtECjWBENH7A2P_QF9ZTv2zzfC_ePoOR3zayZBlpak5o-kPqYxdYgMVp7_veupnruqgUugWyGBoWTXDJzgzIzKYJS6NqxdaSnghR8MTM7hN1vGRnZBgcYHKf5_d4Y8U3eXQWfo4OhilodFvs11p-vsyE3KphQA9zEYkA10hc-0D5kDeZfGFVHwiuFnunDrU-BoYcxaSmVDYir_kOmTESPxbLX2c3kBXqTBbFjruauuEGdtbOUV-F4F_QslPQKI4cSyDzOcnKg7C42iYwSw6LTmxL38RpagxcasSDKH3dWInrY6AmbLVB8nf0vVIv6YviSTVevCW4EU6jig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
دیوید گرافسون دبیرکل فیفا تصمیم گرفته که علیه اینفانتینو کودتا کند تا وی از سمتش برکنار شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102459" target="_blank">📅 20:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102458">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afLyq-BGO61-7BUz76uPpVlBmKaMv9KCehsGLHglvLJ_U9TcMbMyC1IKBnozmed87728spUhpp2zr3YDd_wSysyOdbjlSNKLOw_RPgFvA76MiUbW2fu0-CXFBIgg_23J_JXs_s9u_Z1aofB0P8VsaHnf4K-HKezCiYxEZmL8YY3F9qc3y7pRZLLmvTDrEmTKK01RfXx39VHVeDO5jqHlC38GTtlxKJzYeYp12KhCiEREj6e_2nCZALJJT0J7KSxcdGxARdg626KGs3EoVomYRv8jJtkHQy2KMCS85z4LjTKeKe2QwtgRgko6Ia6ncOtRXHE_loemPIrece4QoUmDVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102458" target="_blank">📅 20:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102457">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZgMeAoIwn41jNNeJ7LN6uFvSqUbjkhUQWQxA6aTmITJtXOrWf2-hODw-LIVo6ibJ6n38U-vWsRTZ1n-qZLZ-jFJW4yfsiXybsXWERuuwibMeHLu4qRiWkGyueViOFfGfitbGZqQ7ZwiTDJjH-PBTrWfsdRml-0gemZaQgHPANFspL25t7xfN23qY6LFyOpBULgJsE2oIfa6Q-dWBnWHzNwzW_7Uc0uliuUxSgLHKQlgwpYGaICkxzEPC4PhHyUh456AsjU0POMQAh1z9O4y2KWlfzE4gNt7QJ6u8nH7Q4raYuNztkNWUFA3yiCcAIMUO8qvIH6EtFxm-4aSAnOVHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
دیوید گرافسون دبیرکل فیفا تصمیم گرفته که علیه اینفانتینو کودتا کند تا وی از سمتش برکنار شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102457" target="_blank">📅 20:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102456">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🔵
🟠
استقلال در نیمه‌اول مقابل فولاد با تک‌گل ابوالفضل رزاق‌پور شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102456" target="_blank">📅 20:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102455">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dh_EBLlznQ6aw3ZMvaGI7IxvjKwY6r-C6f55oSnqyCeFk-qu0KteN0TDg8qg8krYs6p_J0H1KwGJU1ZpvcKP2gqfy59UBkPA89E2yhP1cbdf86guJLfvFRjdEe_hEu_c11dUnLhXHPHRgwIsVVNwtprF552evb1PqRnwa13RvdUQuQ74hzTpCT4vb4CreES4K6GYwMSxWyjU4uvmnsCFb-KKN3jEa60yJIJnnP8s1lL9tngHDZ1-epL3-rSp9Xa32fLHyoPtAlcUr07CAXEtlmp_1dFK10416OVN2YnhEwKbjePINuPbabax0OvA82J0ApAM__C2FfHaso3BUZOkjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟠
استقلال در نیمه‌اول مقابل فولاد با تک‌گل ابوالفضل رزاق‌پور شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102455" target="_blank">📅 19:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102454">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfYTJlk9X_rmUpQl6LYMnIeoWyadah5SArQlJOQdQoI2N2Hinu6Ebw-Sa0M9-YZAq1PeMiUbEisc5G-mGz_GOiv_3tKJ_sjh1wJuurFMPy18BK58sKzkJE6jCzsHh7YSVepdE7RDBoFpyyRP-Rh5WrbpvpztB-jiJY6ewM87XYCx-TWMxqJag46HY57_dmpRJE1W7dL7bB-hSiAAU17G1-wajZ8gxBi2PmCtO8pwCHomRC2gZn9fneAU8ATTRfCqyxH4ej3WmiGKmnhfvuhZqwwEBygBCgpjlWaAh8LgErUPMJI-HTit7RHPnS1xurgFXiBb8y8m-uODgdNUnDgtRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇯🇲
وینی و عشقش تو تعطیلات در جامائیکا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102454" target="_blank">📅 19:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102453">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
📹
🔵
🟠
پخش زنده بازی دوستانه استقلال و فولاد ساعت 17:30 از لینک زیر
👇
https://t.me/+E5pLb4kNVJZiOGI8</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102453" target="_blank">📅 19:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102452">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">کاسمیرو به همراه خونواده که دیروز به این شکل بعد از معارفه عکس دست‌جمعی گرفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102452" target="_blank">📅 19:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102451">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c6Va7HXzm_bV_NXxbO3qqI89Jwf4EbIDvtkiwBcP4W1k0Gg0gSnzy8p5K9wIwrTdaj6guVncZLXgaCoLXSKYZvibKbUVti2euo4TuEvD9PnKrPQbN0n9FxFn-TEMNBGzHM_IccoDdXud44Fhy9rouOeLqLCxcwRU_gxQ4BoO-VwFaR7s7cIvxZB_QQG25PbzSjvcorcmWQ016Du6bnyNBqbNqlaF6nxqBbZnjOWBoZIyB0w0VvOpiEO6opBA-3Y5zJBExOFq26kE0_V6HIYO-NY_08_d0GMS3QjsidTPH_1FntQ_l-DmMabgrbWhb8v2GRpdX-iHVDGXADY1amtyUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇪🇸
رسانه ESPN برزیل: رئال‌مادرید هیچگونه افزایش مبلغی در پیشنهاد تمدید قرارداد به وینیسیوس ارائه نمی‌دهد و پیشنهاد فعلی همان آخرین پیشنهاد تمدید قرارداد است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102451" target="_blank">📅 19:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102450">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IE3d2k1SdFgzAvxlP5QGlNVYOGpDFm5Bh5ER4_9ZU4ashWrxJH0m__9cS9MveAzlc7DOSewTRi-ZaVTdM2swJR259AWkfCCVY5YLmV8k1xpdPYkjN_phHcxgLDqNAuSLN-Cl1gWKNlvLq7-89ZRlHSZQIEcJD8wZi1eHWX9J2L2m2Mv2zBjidL_9lIeY8P6oW2yW8Y4sGuuOSwZDg7Bxc7ivdVsZ1FAIhoVWzwPMdiwqlf2kDgUWtc97s4N0nbJ39T6-NbObzi_NVa5eNJzkWHDxPQ3fRq_t_WZOkAcuPZlhZV7CbE2Y-V1AQ9MkS33Zv7OhIKrU0Xbs-1lwcLguQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🏆
اینفانتینو: جام‌جهانی ۲۰۳۰ بهترین دوره از تاریخ این مسابقات خواهد بود چون در کشور زیبای مراکش برگزار می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102450" target="_blank">📅 19:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102449">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-CD_0SZeGOqWDNtwZ70zXPC_WMZM0GEzScy2puP4KDektrgD8YVZXwni59t694EY2AB1WlWKk44bVsRdFmFp4_2ohIQduigpwIGtnMoVzHVha-Im02fidR4kT53pnuIYPO7AnxrJ64KKNZelJUQyTyJhAtfvl7pKZY76qqDr8umSNjPkjjkJVYojZAf_-gZx_eDL_CJH1dMnvEvGIvyCdHQKB_DR56PHTfdv1m7LnCcmTFqX2hMpW9ptH07PhEIdnW25Kx7qMIb1F2kx7R51Kv0zc597bMOIxGG6UcAa94WaPfsxy6WhK7kiPzI1v5KvrL1LTZuMkENBTHvOMCPHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوفیس تعدادی از بازیکنای فوتبال
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102449" target="_blank">📅 19:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102448">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXNrMeTBjiTHUCDewqcc2rench_kwu_dv_K9TcMxzJPKl-vf7KqcXardEOvcSWNnqu76aVm7a2HvgwGWmydbRkwP67f9VZfljLiT-mghafhUAZnkFQKteWFws5NS1faghcnSUEU3EzW9oujUXwlyrKUsi2QgzPXusxWVZjUmdh5B38jVUZBlezO9PQZ2Md_dNaLOUxQhqsjo--I9my3zyRuBlHS3EKbWt0kV8yNWvWYQyfLJEupltnHugFLGotBNCLEP1nT5EB8C5kJUKmOQVS-Eth3I-HPKfikgYbjoDBYmZ3vDxukEZrEykcHLb16YpdC9wHgaT5MbGIJSh34ikA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
اسپی:
انتقالم به مادرید خیلی یهویی اتفاق افتاد و همه چیز خیلی سریع انجام شد، رویایی بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/102448" target="_blank">📅 19:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102444">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GwQZZF58ZKWBO3D-k_989d4T3sI3nOTdqq9ZVYxA9DWzeIUgNUF1rmEqLuh_9Mp13S0x2ueGNnf-lZpQYZOKESMaMexDYC6fYwxxghq5EXQxX5E5XTxnEuE4haT5oi4cHFdRk-5y_eo4e9IQED3j_f2LqoSOJUdltFXEYdiGyLTWCt3zeEBZcvkS_9jcGnr8XrN5ztWge6yob-ynk0ZPqMhXtHbwWqEf05kr7e2Tl7ddS-1ISDGA-gVT48ONFpkOb8ggtJUF8K-9GFBHFu1ENLHULsMPp7d_v-OBH1Or3_eorAboxWW-h9Gs9gWI4y6kirSu_WI6ed1Xih_Bc-vyjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XgGA0lXNhjrZc17qAiYp1HTZHjgf2VSt71m60gt9Gkv28ln58X3-Q3KWiooydZnhm8sA-7YcKm7e7mmM-E8Au15ZHnX3RexuwQCM7fUJozAncQLG3moDPbsalHZ0F--Duhccs_i1vpCIvk6T8CLzzItnhLY1BnPYkElOrLxtP9bdlpIizOIRZtARz35VfM4f2219GSZJX1p1BLNU72i4HC-QIPMF5aNteblLvh6hZdSuIE3uKImWFrJUdo6WYVN_kEarw4mCCpF3hoa4sdmzd0nBhfSKyT5-Dx4ss2xDfWI8fiPxxSYsodTX9iI1MaY8i4OwwNGQXeGZ-cQdvGmkUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rwXKl-U0HBHVhqIkruwQy0u-2gl17Bfd2n474lFDW4B0xQqYcfuBiDUVunFWVoh7hcOueV7jR118ykYhgh04C0B_UFOiIc_3WT-z7mNigUxhFcteZcFV-c3Q51BSYnZ2YnMQewn5B8HZikyzO_X9zXpev2zYrcOBwrywIhzsra_xGbhXnMClGqDRYfFInqKgYwfT44Ot80eyKQe8D5unNV2w_gfhUAFDPiEdGTD3eh83WfwvJDJCFwTqwe-qUSFkBqBLeSmjqgG4Joe7tE4r3qMVc03pnKYYTfPWCCU8sskDPskftYFE6gDFY8UprhnUzVy3jp80s47H38GOYru-Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QoaRKja-ikRctJ2VXxC3ugLk2vrd4ONrtJroRXoyeO22rNcZ641oxtA4KjNn2pqF67jbqflk3csS-BhsC7JvYnbA1jqLZPzSoOCbgQaDUSVd86vmJIhrTsbBFRQO6GizhN6qX07CdvblmurJbw7Z2LdTWomAfylPk4DO4jH9t0eBYFA7x2yRFsMoEz4_TEx7X5XEMF96rrDg7aVaDuRr3XTwoaNBipjD2K9WETKNxaZsEzXHREDo6_f6tG9TZhUHaglSabzrQUSuJD1YlDmBXiwwCCaR2Fgae52eOz7uabaKp_8_DPj5OOUw0RRTWozl9uN-yNU3GHzGZamBiAcjCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
عشق و حال لامین یامال با دوست دخترش اینس گارسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102444" target="_blank">📅 19:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102443">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYXObKH-QCBOGKeXcjW_TbmZjrCGL54rE3lVur9BLM6LDw8BedFYCz2wGQlJiSUf1ZWsqrR8RlVvOnwq8Rf39fX4E1-fNMuAc1LhFc6WyA1G0OKGAzXb_tSfoFSG7wiFiU5LXRJ4CH0mZ5VtnnONPbwYSw8lSItufQjSkXcqH54EtZfq4ezm74ewK1tDhOzKyIq27guPUk_JsCT4BUr09VVd7Z_cXT4UsC6NKtOQ3D9AXmxj7kZGNFVjXAr2qQ0WbeE0HtEboIFIaBDUR8OiTl9dt08yh0lN9O-rKNJdmzlLLzNAo4Y6nv3bS4llUFbSg30ZIsuSycWSJ_05U89Aeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی دوستانه مقابل فولاد</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102443" target="_blank">📅 19:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102442">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PV-083iJ4ONX8xrne9uJxWGvqHBeEAW4hbyrKXeYgeJWnCfqcRdbr8nw3CAeeACNtMmMrHr3ZxqQmtbyahRpFSP0gJuHPgc2-rraJD7C7fqIA9lHOjGSuZbKvu_XhqtSf_HSd_1s14EdpXcTMfm1oScYtO37j7lVnxyJvPyJOCbgmfEaWrQbUXJrmo2yS4l8OKweQOPoMjT_nRfI5TQ7nGbMVulC_IW9FMau4pJFfHOYO8Xv3X9ac7WLOQoARyrrR5NH545LSkv7YzdzwcoVnlhJW4DuJOe-gmEqZUr-Xevbq_DHRLbMR-eagDz2QQ1I2lKOBgfxjoFCItvj8JZo6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فوووووری محرومیت دوپینگ میخائیلو مودریک لغو شد و او به زودی به اردوی چلسی در هنگ کنگ ملحق میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/102442" target="_blank">📅 18:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102440">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AIM3WRcPfLnZeVMKxgSanHLuVw1oBi_J1eVTtrq_sY8HtdsmujYEaCNUUp42IHyjeYOj8k0C3k5iXUVzzv6054AdVs3Fb8eInp_soAGanxqrGqeg1dh1wNcihRyWGGK01gMabEAbp2x4zCrnjbSwHeJlHNMa_2JuYmHJ2e4T45tAx0vREAW3WxHIAbOB5W2BwEFK_ynIewW11XkqEUA4WYU_nsk2h_LFRe-P_px7pbDmrKwYu13xjgnxUO3JiIQsKrApz6iBjS35_PPH5v7exjpr1Fs1HNp_TnWIUEnJXrZ4AN5ZlnziJ76IQjylVVBagf0Z-Ijwn1667lo6TwqgrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nPyfD4y_6WSyogsVwjwWfqhtN20hk_loMfV_VUNSkPB59K98AXTWN8JbZKYjRvum4xHpHNwZsGKwzqiaknwXiZeNzHz7Nqt2qewiNTt1aqEACKiVkRXmMXuXrGxmj5xEh2KCMU7V3snBnHPd1WXfppDtcXykjSGvA4zi0t5xzT26ezDDdOAmxRvfkrCUxzKOT8uR_EEOlXi4nMlN2c0NZLHeWZOD_GeQc1Meuy6rO4u9_YwuIY7mJrrKZoMZg4xWqHfBBF5aRs_afiIjYHzyD2XddLqSCGU8chaz-_pxBs_VOxXHNSY51H7u3cWgeLkv2DCnRbhDNMXkuuFr5JIPsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیر شدیم و خودمون خبر نداریم..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/102440" target="_blank">📅 18:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102439">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5d65b7222.mp4?token=NL_bosH61kRC2OliQOKGXbnz_xk0GVXwl9yJ9NrbBPlhsmBQmC-hItNhSEYs2tuEbzADxJ1uBF12f0Ou7qJ2yjglFsKD64XkqBRABV6jgaY88yh8F_myjzaj2deIC9SoHp_qqT6eMvXNHXViVA-4pEA4EPaP300M5ypiykZVAkgxAuCkADlmWFRy9sQadwi0hNPIrpGTDCywg1p5YPjl8rdw3WAgauf1u7dj7MpR-tvaw74Zf8MrDrW0plLXtAPEupRDGdCtN1NqBvpGsXT3kakoiywEUKRq-KXFhH6FSxEieuUZhPJqLm8mxfeeXxk7OvzrGn__xn3nVPMLX1wyPmRg1Ph6MkBQO_LGvrN2deqsJ3khM4Wwtfp4FI6L-nbyJXE1Oc9N-l4Ott3b37QBQodWWkuXqGTXQGlC8ixjSYPUvq6y2bs2aJsMWBcXCtgN0qieI7YHksY2_Rk1WSichTuWkcNPk216Q0J35V3n_B6Y-s-uDY05fC3qDXWeJoVqW1B0PF_GOlER_lyzU_TWmjjW7c83e3c1LZNEZYR-fPYV47GKvFKiGI8X5gzCDAdCiP7-83TcW64GpebnmUN266wB_eklDtsnVnpeIqGYKGq4R94KRytkNT-RIoHQrUvEAvcoexxE6uEUmvtMCWYnaFDCvYQRkoEJuAW1gCSWZ_M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5d65b7222.mp4?token=NL_bosH61kRC2OliQOKGXbnz_xk0GVXwl9yJ9NrbBPlhsmBQmC-hItNhSEYs2tuEbzADxJ1uBF12f0Ou7qJ2yjglFsKD64XkqBRABV6jgaY88yh8F_myjzaj2deIC9SoHp_qqT6eMvXNHXViVA-4pEA4EPaP300M5ypiykZVAkgxAuCkADlmWFRy9sQadwi0hNPIrpGTDCywg1p5YPjl8rdw3WAgauf1u7dj7MpR-tvaw74Zf8MrDrW0plLXtAPEupRDGdCtN1NqBvpGsXT3kakoiywEUKRq-KXFhH6FSxEieuUZhPJqLm8mxfeeXxk7OvzrGn__xn3nVPMLX1wyPmRg1Ph6MkBQO_LGvrN2deqsJ3khM4Wwtfp4FI6L-nbyJXE1Oc9N-l4Ott3b37QBQodWWkuXqGTXQGlC8ixjSYPUvq6y2bs2aJsMWBcXCtgN0qieI7YHksY2_Rk1WSichTuWkcNPk216Q0J35V3n_B6Y-s-uDY05fC3qDXWeJoVqW1B0PF_GOlER_lyzU_TWmjjW7c83e3c1LZNEZYR-fPYV47GKvFKiGI8X5gzCDAdCiP7-83TcW64GpebnmUN266wB_eklDtsnVnpeIqGYKGq4R94KRytkNT-RIoHQrUvEAvcoexxE6uEUmvtMCWYnaFDCvYQRkoEJuAW1gCSWZ_M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
چند تا از شوت های کارلوس رو ببینید، زمانی که فوتبال تا این حد راجب کسب و کار و پول نبود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102439" target="_blank">📅 18:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102438">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d5590fc67.mp4?token=k4vZtY7hEZscfCZhMw_f4MUWoGwGJr2_s4zsKbivnIe_GolAF-uVk9D3W2QfCBCo3psXB90zdUTMNj32SUC7tIAOevntDr7LB59P2ng1KGfCJ36LB79TCVY-ewjSVfNMfgIrNbULBQCenI3oOWYzUozUlo7a7BOrTR2hQ66cabKI4kBBpo5bh2pPc5CN4CzdACUBOxH911vc-yMtJg6pSOsTjZOmoc8ueBUqg7DejGVNGRItyJAh6USfhtMs_jRHqsussYKC15DX4m2BiH4_nG8AtNvdf5WmrVf-bFfFd6qq0Y2Otu_sQE1xNj3DlxtLtuhMrunqGgFMiCeLoCBtxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d5590fc67.mp4?token=k4vZtY7hEZscfCZhMw_f4MUWoGwGJr2_s4zsKbivnIe_GolAF-uVk9D3W2QfCBCo3psXB90zdUTMNj32SUC7tIAOevntDr7LB59P2ng1KGfCJ36LB79TCVY-ewjSVfNMfgIrNbULBQCenI3oOWYzUozUlo7a7BOrTR2hQ66cabKI4kBBpo5bh2pPc5CN4CzdACUBOxH911vc-yMtJg6pSOsTjZOmoc8ueBUqg7DejGVNGRItyJAh6USfhtMs_jRHqsussYKC15DX4m2BiH4_nG8AtNvdf5WmrVf-bFfFd6qq0Y2Otu_sQE1xNj3DlxtLtuhMrunqGgFMiCeLoCBtxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ویدیویی‌از وینیسیوس‌جونیور در سن ۱۶ سالگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102438" target="_blank">📅 18:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102436">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U0cNOgH8EYesdCSeSZ4AbOiMouSVBWILjaA31_2I4DeCSeE2aanmurRvmsCCN78ZAn_FoWplLnOO5w7USySVl3h7ffPnRBMtlHxLJBCkFq-FDWQqs49fAs8pXuaJwZQ8hMKl1LpviU0JxcsGa7EzEPg1Gz_ifU7c9F5Iux_NhsQJE85KhXTW4s0lV25rx3o5AWaKTpFPgFyWH1qfq37un8aVkq-kDITNyXj6_fs-g-5yWJT0cIld8xJVSg-ko8sAYC4CW82FBuvSPLyH_wsN7BXFqfzdA8YH15brEeF0tBllS6YQit3hcydxO-uSytm9vQEHpcYt6P3wkrg9UlsUHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N8mVhHk_qRfjmoDOlAIDwQNb7m0LUzBYiyXNH_42gCzqfaOsw44FfrXNGPZAhyiwH4lQ9gulSe3gE3QfhuqQup6P7q4ONAGtTfqdXfiRe7FvWd78YzbEw_IOnKKYmM_dBYWZe_9zBH4wPItJrwJpOL46QB-Mo4LYJ3clHjvn3vZo0KpPw10NJEm_Q_Kb1B8PCuEUb5nn_d_vkG10cOTPII-pVIejtCB_noBJV38g4YSRgiybJfsUOZLOmUPEC9YtTi7vts6Ga0HlCB--ZDmVsIGahPOrXVdptcncliJ_BMaMjwiDeB21IoLB6mntImiF0reLAbANlKGVypsUAE9mwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102436" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102435">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68f9e38a71.mp4?token=oiqiqyO3jutj7vIqDEqXLRWwMDjjwZL7Fbl6hClDDclSZeTIWK7Olx4pH4_hdLRMVxlFu9d9jiXTj6sr9tfOPpmB1PqSmogRtZd-O0gO54JK3XDd3l4fDVocsR8nMJtaYUP8Hi3hPuqEv6mYRcVtZdYbEU_kL85mYBbjaLh_efn_W7BWpZDltfTPyWlESdxY-GMuXdGELnIZAIVE-OP-DYCaVPxGO2O9gQJfqXRd2kFWmP6LDQ_zmPLf02fhfZiZG1G6Peg00b1fRGKlAQTD1nKlNizCbMfPIT5R2JDXM7uAKz_z8o5m6K0w6t-Pcv21-6ef6tX7cqgvU2i4TcVJuC7SZ4XABrO6JuSXVW00VCCuk1AoHfcT-_9sxbT3y6j-V9i233aLG-jbd39cAXPWNK2Gf5Wc3AHf9Z4Sq8giCkMiPQuBt5ZDWoKlMcPKZXdk_Fr9IATaIhjvJSm457p8BfiJih8BmqZ5jOS3ec9DS4y4AVEinfI1eAeO2Hh4PUOBXM0CK-H111aieNr9JUorWqyBgJfwBahqwbpMaGl2ncj9KEquzJIi2tjdD1CZFoB3H1idtcRl27MVhMb5Z25P0BHJx1EmCKLW_o6wCX2Q0xR6BgDFKjiDhOc1J6Z3lCVycro5pwM7rKhTnrJ_4bH8ZzBawA1S1uDxBPLhITaKxF4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68f9e38a71.mp4?token=oiqiqyO3jutj7vIqDEqXLRWwMDjjwZL7Fbl6hClDDclSZeTIWK7Olx4pH4_hdLRMVxlFu9d9jiXTj6sr9tfOPpmB1PqSmogRtZd-O0gO54JK3XDd3l4fDVocsR8nMJtaYUP8Hi3hPuqEv6mYRcVtZdYbEU_kL85mYBbjaLh_efn_W7BWpZDltfTPyWlESdxY-GMuXdGELnIZAIVE-OP-DYCaVPxGO2O9gQJfqXRd2kFWmP6LDQ_zmPLf02fhfZiZG1G6Peg00b1fRGKlAQTD1nKlNizCbMfPIT5R2JDXM7uAKz_z8o5m6K0w6t-Pcv21-6ef6tX7cqgvU2i4TcVJuC7SZ4XABrO6JuSXVW00VCCuk1AoHfcT-_9sxbT3y6j-V9i233aLG-jbd39cAXPWNK2Gf5Wc3AHf9Z4Sq8giCkMiPQuBt5ZDWoKlMcPKZXdk_Fr9IATaIhjvJSm457p8BfiJih8BmqZ5jOS3ec9DS4y4AVEinfI1eAeO2Hh4PUOBXM0CK-H111aieNr9JUorWqyBgJfwBahqwbpMaGl2ncj9KEquzJIi2tjdD1CZFoB3H1idtcRl27MVhMb5Z25P0BHJx1EmCKLW_o6wCX2Q0xR6BgDFKjiDhOc1J6Z3lCVycro5pwM7rKhTnrJ_4bH8ZzBawA1S1uDxBPLhITaKxF4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
درگیری کورتیس‌جونز، سیمیکاس و سوبوسلای بر سر بازوبند کاپیتانی لیورپول در بازی دوستانه اخیر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/102435" target="_blank">📅 17:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102433">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iWBa6GmcPJWvDK8Tu8LrXUHAge94eGjGU7-7gdC2HMMQpk4BCiaXISSx470N4Q-ShZo7H649vJX5wytbPpV0JmyR3Jhlzv-EL_hZor8Uold7YJwv3Dt2jUt5ABZxxxpVHD-dcE99dBm7EdoKouA3va7WpUo_JqWriIJZ5-R961Ief9u4lWLt0TzI1KmXITaRyUqtdwcywTIX8qvVbuudsH4XXfF-dOkSevVAMcdvCvCGtdn1L9Qt2Vm2beENTcpNHDIjAIzv1zwveNQZbWj0h1ZX1ntJp3Ih2mp967nirthEg_M3yLyLSCOmq5otcaxmojCcJkg-OwcKJ8ayjzvOnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BwsLvLPp3P33zOjUWyzGsyKDOj_wPJ80mOX6VtPVKz41uyO3IbcewkdmQ4fdUIrerqjXDC_IoGCirSI_39if6cBjAIaTAyyfWJP3VAw6gzRTyuKf--u0Jhx0J9TL4E-GHlyLX1A-Q23X7Tw0OhACDqQ-fEKge257qHoY7D-kbgrdPCh6zsK7u9_stF5MfkUCYzfLAEP87RybYKOiDjT6TAYOYQisU-ftVDoPV67H8DeCfzuIadVMo7kRARf8guW8z0jBP4pLgrbEW53Rsl5V1ADJ_jQBPF6ILJhhE1FCHm9_MbA6nphBXGeilzAycpiXnUrTcq27_KF3hnByECEExw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
ال اسپانیول:
پرتغال و اسپانیا اعلام کردن اگه اینفانتینو پیشنهاد خصوصی سازی جام جهانی رو پس نگیره از میزبانی جام جهانی 2030 کناره گیری خواهند کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/102433" target="_blank">📅 17:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102432">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96363baca3.mp4?token=n01fRga5zj1PausAm62ri_wQ-VdISIl3pdJ-mqgnT2FOxHsg8ZwDXGaNcDao2Vxy7O3IiH_paXixtVT4zBx3RGoKv2lpfqHyzXReezAH5nsK-4x19jBcPNNK0fcpXgF7CMH-i90dPyHRXrC10gBa9Sr7Eq-YlYIQanh3O6pwXNWYK-YgZZaSbso8SawUzsLNklAF5zCktA6hQ6mguP4BuW7iQXElMyEmLymR293JBgS8hfk8EQOykbRFvsJrDwlSiJZBwv-HiKpGuoaY0l9GUQ31GXYz4gWs97rK2PyuZZXuvxE8IXZS5P5ayt9SAPzEMViVnEm_D8v3bCWxmFD3rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96363baca3.mp4?token=n01fRga5zj1PausAm62ri_wQ-VdISIl3pdJ-mqgnT2FOxHsg8ZwDXGaNcDao2Vxy7O3IiH_paXixtVT4zBx3RGoKv2lpfqHyzXReezAH5nsK-4x19jBcPNNK0fcpXgF7CMH-i90dPyHRXrC10gBa9Sr7Eq-YlYIQanh3O6pwXNWYK-YgZZaSbso8SawUzsLNklAF5zCktA6hQ6mguP4BuW7iQXElMyEmLymR293JBgS8hfk8EQOykbRFvsJrDwlSiJZBwv-HiKpGuoaY0l9GUQ31GXYz4gWs97rK2PyuZZXuvxE8IXZS5P5ayt9SAPzEMViVnEm_D8v3bCWxmFD3rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/102432" target="_blank">📅 17:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102431">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">💥
🧐
رونالدو، پسرش و جورجینا درحال عشق و حال در گرمای تابستونی اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102431" target="_blank">📅 17:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102430">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e703311f9.mp4?token=mymhy6gwV29YCTqct9WVT5M2aZ2i5L7pWGktkfpPo66Rc0YQZI5iDdus8bTRSs4OdQA7A0M4R0qmjMusHdw5vhMg_qVix54i3BtmxMhYlNC8GHxkjVKHM_vtE69gR-QcMrjXbaEL1dCamqpYl2hhPN_-hKWNyXEbLuYyY81Xw1rdrrOpsAFfeZvGijHGCzcZI7uEAGm0nk-V0Ue_W6-JcrQAZoVe85IIR_c4e7DzjyTkDId6er3zzgR3r0edUym4eE5RXMg7QjFsRzsq4E0Da92mPBrfnUhhRmz1gsQX9BKKPHeesHmhWdtvlh0KR7LTgJxaaO3It7jb4Te_fKLfqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e703311f9.mp4?token=mymhy6gwV29YCTqct9WVT5M2aZ2i5L7pWGktkfpPo66Rc0YQZI5iDdus8bTRSs4OdQA7A0M4R0qmjMusHdw5vhMg_qVix54i3BtmxMhYlNC8GHxkjVKHM_vtE69gR-QcMrjXbaEL1dCamqpYl2hhPN_-hKWNyXEbLuYyY81Xw1rdrrOpsAFfeZvGijHGCzcZI7uEAGm0nk-V0Ue_W6-JcrQAZoVe85IIR_c4e7DzjyTkDId6er3zzgR3r0edUym4eE5RXMg7QjFsRzsq4E0Da92mPBrfnUhhRmz1gsQX9BKKPHeesHmhWdtvlh0KR7LTgJxaaO3It7jb4Te_fKLfqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
🎙
تمجید جالب کاسمیرو از لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/102430" target="_blank">📅 17:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102429">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b472a6619e.mp4?token=lAIUk3IDqfuXtrgVOnG35Q9ZM_sX8G3I-R226BPOQkN0qRzL7qYepJrTDBxQ65BS_f25PuuZWN_Ui2hbBQSI_7UUwcEv5f5KWEzlEh7R6kPdXFCYcVZJYieTA2O3DkOkf-rTAyxc_XjbS1MxW-twuzTxpNHrL2Bn60ViCFnzqURYbInMFdZi9s9ovyadJfO1CMMES0myuBlkH1yO8PR9RMOodMWMcwLV4Z2VCfAxYR-oZB1U_ocv86hp5MvGswBP3Z48J_rOaNwChLLt1RXB_s20QhRjuxbYPTO4I7ECJ11WjfEOJJmVYUlHklOa-1K9vWfaXTssVXUQEviHiX5o2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b472a6619e.mp4?token=lAIUk3IDqfuXtrgVOnG35Q9ZM_sX8G3I-R226BPOQkN0qRzL7qYepJrTDBxQ65BS_f25PuuZWN_Ui2hbBQSI_7UUwcEv5f5KWEzlEh7R6kPdXFCYcVZJYieTA2O3DkOkf-rTAyxc_XjbS1MxW-twuzTxpNHrL2Bn60ViCFnzqURYbInMFdZi9s9ovyadJfO1CMMES0myuBlkH1yO8PR9RMOodMWMcwLV4Z2VCfAxYR-oZB1U_ocv86hp5MvGswBP3Z48J_rOaNwChLLt1RXB_s20QhRjuxbYPTO4I7ECJ11WjfEOJJmVYUlHklOa-1K9vWfaXTssVXUQEviHiX5o2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
یادی‌کنیم از بازی تاریخی ایران و قطر با گزارش جذاب عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102429" target="_blank">📅 16:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102428">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfd29d0ef7.mp4?token=bZf2wGY9ukzLDjXvnAUWS_FY-p2SIk88R_yLO3-mxSI27gEzAnZ8MTHBfjcC36Y0lFCi8RRtWt-YNEEpsIkKydJTOB0i7LFz6F3NpcnjcOhKMQ621wnlHWPEDj72sJIOUVME_q2dn-H5hlHJ8bcQLzwShnHvDAPU-o380R1iW9hKcg1i6h4n0nOhEFW4W9UEJnbV3w3M5dEpYfGfJf0aw666LHelTVJt48ZjD19WJMasL8UhC9xbrLV5qpjIsxDnRRlYBrho7vZjnoTiSGNjWYC7_5LfkaeKGRMkUEREy8nG-jHCP53WUMPTTVLjiuQz2j9j1MbIVlEONilBkCtzsoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfd29d0ef7.mp4?token=bZf2wGY9ukzLDjXvnAUWS_FY-p2SIk88R_yLO3-mxSI27gEzAnZ8MTHBfjcC36Y0lFCi8RRtWt-YNEEpsIkKydJTOB0i7LFz6F3NpcnjcOhKMQ621wnlHWPEDj72sJIOUVME_q2dn-H5hlHJ8bcQLzwShnHvDAPU-o380R1iW9hKcg1i6h4n0nOhEFW4W9UEJnbV3w3M5dEpYfGfJf0aw666LHelTVJt48ZjD19WJMasL8UhC9xbrLV5qpjIsxDnRRlYBrho7vZjnoTiSGNjWYC7_5LfkaeKGRMkUEREy8nG-jHCP53WUMPTTVLjiuQz2j9j1MbIVlEONilBkCtzsoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیاز بود یه آیتم جدا برا لحظات تاریخی فیروز خان کریمی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/102428" target="_blank">📅 16:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102427">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d17c8ef3f2.mp4?token=sLIaqCUBIAFvw_D5xEEpOIiOsg4IIJv9UgjZF-ObbR19VkrQOL_VcFPYkeLeafnaZKWkKgN71qa0pxTXEvtlYm7R-7plPqsVtO6abwWJKrn2EJ9lUbBPL0WQFNop0UkVVXDzSiqoxgTZ5tta86xyCbDK8DNH4t1khohkcGgqaOhWLc8I0mEgFqBEgzIXg8Qc2EEyisfYyQ6RuZRAQUbBnf1DnRd-HKNzoQm2Qqaf9CxN6ebmya9UQs9b35iSBN1C2JNhETZXU9VQlJd6kdVxwagyj0abATu1hNT6XvZc09hRPNpEXWDvxtYIRAqcviG0vEzsF_b4tI4bqmqYXcrf4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d17c8ef3f2.mp4?token=sLIaqCUBIAFvw_D5xEEpOIiOsg4IIJv9UgjZF-ObbR19VkrQOL_VcFPYkeLeafnaZKWkKgN71qa0pxTXEvtlYm7R-7plPqsVtO6abwWJKrn2EJ9lUbBPL0WQFNop0UkVVXDzSiqoxgTZ5tta86xyCbDK8DNH4t1khohkcGgqaOhWLc8I0mEgFqBEgzIXg8Qc2EEyisfYyQ6RuZRAQUbBnf1DnRd-HKNzoQm2Qqaf9CxN6ebmya9UQs9b35iSBN1C2JNhETZXU9VQlJd6kdVxwagyj0abATu1hNT6XvZc09hRPNpEXWDvxtYIRAqcviG0vEzsF_b4tI4bqmqYXcrf4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
▶️
رکورد پرش سه گام جاناتان ادواردز (۱۹۹۵) با ۱۸.۲۹ متر ثبت شد و ۳۰ سال پابرجاست. این دستاورد استثنایی در دو و میدانی تحسین شده است. ادواردز در مصاحبه اخیر بر تکنیک منحصر به فرد و هماهنگی قدرت و تکنیک تأکید کرد. او پیشرفت رشته را با شکستن رکورد توسط نسل جدید ورزشکاران مفید می‌داند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102427" target="_blank">📅 16:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102426">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/543e2ce52d.mp4?token=LZzQxBlX3GN4VVPkeqYeF-fClwp5yhJB5yTIRz2vsfgEwuSiXduAFlTDbP34iIc2FDoRicqUdXXGx9vjqebDtpMfKFb4LmnHW4TRVw0LPoHBA69AA075T1BK6zOZX67nx16qvuDv-QpzDpsHBPwkIzsW0LbMGtu1kdZUVZ5y3SAXfAyDjJIXKSoz4FQyXawCjCBqFQykCp9R0QK0I3P_HwnHSXcvbe1nDfh_N6gdYm28SR0OtTNHFXwQ6eZZvzFawp1XB_dHAKlVhG0QmHRoTjYUASWB3lOAuZmVWMB6YuRIZk1ScCkRYrrfldo6GR9U3yP30-aOhNEFHb1ho4rhnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/543e2ce52d.mp4?token=LZzQxBlX3GN4VVPkeqYeF-fClwp5yhJB5yTIRz2vsfgEwuSiXduAFlTDbP34iIc2FDoRicqUdXXGx9vjqebDtpMfKFb4LmnHW4TRVw0LPoHBA69AA075T1BK6zOZX67nx16qvuDv-QpzDpsHBPwkIzsW0LbMGtu1kdZUVZ5y3SAXfAyDjJIXKSoz4FQyXawCjCBqFQykCp9R0QK0I3P_HwnHSXcvbe1nDfh_N6gdYm28SR0OtTNHFXwQ6eZZvzFawp1XB_dHAKlVhG0QmHRoTjYUASWB3lOAuZmVWMB6YuRIZk1ScCkRYrrfldo6GR9U3yP30-aOhNEFHb1ho4rhnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو کمتر دیده شده از مارادونا و فن‌پرسی
💘
💘
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102426" target="_blank">📅 15:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102425">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e43f315425.mp4?token=ZaRizN5-TT5BTUUB-xLhmBmRcfawKx9oyuAHgELPNXleLb3gka1WzE4UKzVRGWW8DeB_pSDejHQJUEjROsFgU4mSo0zciprZlpnD48sG-bev6xkSkAdrQUy3Dx29TNSzajdhEFRDhniqVGH2D0ZfxGD1kgGVnEayZejqx-uHDJhEGoN7ELjCeAkxHTtxyMbugB5pOd9B9-_pB7KNlf9g08XPPxEz8sq_lVH8mIlmeKDPwLwFAFw_WIYR9BQdIukgjCxLEMBGotMDv-SXZKWPt1w7qyu-IQmL5JxysxxutoO0ia0hmVkF8_H37Sitl_NC5ry4lybA06zV8QDIXMl8Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e43f315425.mp4?token=ZaRizN5-TT5BTUUB-xLhmBmRcfawKx9oyuAHgELPNXleLb3gka1WzE4UKzVRGWW8DeB_pSDejHQJUEjROsFgU4mSo0zciprZlpnD48sG-bev6xkSkAdrQUy3Dx29TNSzajdhEFRDhniqVGH2D0ZfxGD1kgGVnEayZejqx-uHDJhEGoN7ELjCeAkxHTtxyMbugB5pOd9B9-_pB7KNlf9g08XPPxEz8sq_lVH8mIlmeKDPwLwFAFw_WIYR9BQdIukgjCxLEMBGotMDv-SXZKWPt1w7qyu-IQmL5JxysxxutoO0ia0hmVkF8_H37Sitl_NC5ry4lybA06zV8QDIXMl8Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
⚠️
تجسمی از المپیک اگر تهران برگذار میشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102425" target="_blank">📅 15:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102424">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea1f4ae5ef.mp4?token=mFFKaHexWSmXotAAvrM-Agy41GQQqMmN90_LCwclwYdX1f7kxdpa2Ipx8NKcu6Zgd3f3R-_LkNMHkOm7f5-wiUQwu5r8VDN0Dh7rStLT-j4RLZF8hcEpfdR7G57nu8xy_pINbrQbwdd07WENc8vaJSTSULeniGWGHiP_18wKGrlqz44epo-g0bZcEaSSlWXozusMSSDlUvK9o9SKBGPkod5u3cIK0HjC5GrV0N7uzKcjzatzKnIUwpSW6CvwkTwmX26wE3ptWgwC_jopDu91bJ4asA-5FVpcKdwMLvZO0wGe8UKWdx1SsqIo63pGg6EGWi8R7rwrRXBdllPZkT2TUBy5Fe0yRJoyvzeTmtBEVXR0Rc5Y8vLT1Gt8NEmKtal89gtRwFtgRP7skQW5dFUd7PS_rM3eXdaQiu5MiRDIn8H5Jozjyq7WsC6dAbE1b6l7nX2FCfBduA_Cd36nG0dukwsAfeF1Iinind992uNWBVD_yjj-ykT0y83rzwxZTurzxlCYpywyrdj644qX4Xsd6EpV0lEITLWLrnxW70JpSMk3yLThvJECinKBztJWc2tJCbldGu_TZsTzP9JSbQG7oBSxojSmZraoS2phpD_HZGEdGORedYobsHbuYeMsWS8ZGKJdlzIXxC4C_6g_UNqJ2Tb74EKF4whdnT_aLdobwAs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea1f4ae5ef.mp4?token=mFFKaHexWSmXotAAvrM-Agy41GQQqMmN90_LCwclwYdX1f7kxdpa2Ipx8NKcu6Zgd3f3R-_LkNMHkOm7f5-wiUQwu5r8VDN0Dh7rStLT-j4RLZF8hcEpfdR7G57nu8xy_pINbrQbwdd07WENc8vaJSTSULeniGWGHiP_18wKGrlqz44epo-g0bZcEaSSlWXozusMSSDlUvK9o9SKBGPkod5u3cIK0HjC5GrV0N7uzKcjzatzKnIUwpSW6CvwkTwmX26wE3ptWgwC_jopDu91bJ4asA-5FVpcKdwMLvZO0wGe8UKWdx1SsqIo63pGg6EGWi8R7rwrRXBdllPZkT2TUBy5Fe0yRJoyvzeTmtBEVXR0Rc5Y8vLT1Gt8NEmKtal89gtRwFtgRP7skQW5dFUd7PS_rM3eXdaQiu5MiRDIn8H5Jozjyq7WsC6dAbE1b6l7nX2FCfBduA_Cd36nG0dukwsAfeF1Iinind992uNWBVD_yjj-ykT0y83rzwxZTurzxlCYpywyrdj644qX4Xsd6EpV0lEITLWLrnxW70JpSMk3yLThvJECinKBztJWc2tJCbldGu_TZsTzP9JSbQG7oBSxojSmZraoS2phpD_HZGEdGORedYobsHbuYeMsWS8ZGKJdlzIXxC4C_6g_UNqJ2Tb74EKF4whdnT_aLdobwAs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🔥
👀
۵ گل زیبا و برتر اولیویر ژیرو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102424" target="_blank">📅 15:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102423">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a3bfea056.mp4?token=EcnCgGYyDc1RfiSwg5iDYcJ1iVtWSn-Tlawyl7JiugdLca6DzaqTZ0ph_UfoU97Eo7GcG2n73XHM-qO9NXx1FbbgyxbcJmHIVPAZRO3BYdWrOBvWfYmmltIaxfb_u_7x8Y6iU6vgdnVrdtkWVDuXxwglZh9iFeNhTilyMnK-A3kIUEQ9WASKKzZJCdEQXIY83xR4eAsDfAbNR3pxKzy0Vq9VuY6S6xc6F9VwIazmM2d5MUsVykysulxu0swncNLkgczetNhdO-qNbjWtSv0VV7h-R_4PJC8ho_csH8lh6u6i3Ptx3oDPfDMVeYntL5TiFBHZJOdegn2Ijx8p9CA54w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a3bfea056.mp4?token=EcnCgGYyDc1RfiSwg5iDYcJ1iVtWSn-Tlawyl7JiugdLca6DzaqTZ0ph_UfoU97Eo7GcG2n73XHM-qO9NXx1FbbgyxbcJmHIVPAZRO3BYdWrOBvWfYmmltIaxfb_u_7x8Y6iU6vgdnVrdtkWVDuXxwglZh9iFeNhTilyMnK-A3kIUEQ9WASKKzZJCdEQXIY83xR4eAsDfAbNR3pxKzy0Vq9VuY6S6xc6F9VwIazmM2d5MUsVykysulxu0swncNLkgczetNhdO-qNbjWtSv0VV7h-R_4PJC8ho_csH8lh6u6i3Ptx3oDPfDMVeYntL5TiFBHZJOdegn2Ijx8p9CA54w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
سه دقیقه با لیونل مسی ورژن 2014/15
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102423" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102422">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dv6VUPsVMt8GTPib4dP7sWrRoNurHE9G0BQ1Ae8Cdzwk3fpvFlOsxICmrYQ4hFU-t3ZswGZoE93_ryeBga5qpdp2x4-ai4tPluwJYZ0jNPhDOI7D_52_BHKqhBTdfpFYkMEp5IJ-3OyCKTaDi6vjrA9anrq9kAPl2VIn0b-n9ncjV4gm9a4ybq1EyUvt56OklRymtd7eU8oTO_GYxci70i9ared7xemqYkLTRXr3CiDMBRBAD0fm46WibQzv7xSbaPOpU1evcMDBrTGRcIXE2klVZuSoIoO5XJovJqwe9oV70qAO-5dsgF0LLvD5aM6mqBuo-tXEPpBoLFzW8yZlVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
لیست رئال‌مادرید برای بازی با فیورنتینا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102422" target="_blank">📅 14:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102421">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCcNHAqP_E2A-88VwQqr9NBPtUatTAjcQJ9BXzE1lMuBtnOrgdhguZAgC3VZapPpetxSzfrGE-IuWc_MLLX-VTWKf5Mj9NboaBM14I7czlhFa8GHi9uEZmOfc8XU0nmnpdt32HmA29kmuf8BGuxAOiy7kXuHgFLbbsCXiPtW879MgMFL5y5wq8iC6NNt6exmle0oZY1LhY4xRBDLgFg-bqwfffZjsPzJ4LbM6Q2hDi5696eG-bPwuGalkxXW308A6YKXPDe456Ev1NvQGDsAtrId9ZY0SfDS_Xu6eX__IjDRlkwTRGzjXkBXHDtMHJEFVIEDOCLwv-NgfC0--PVFTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
#فوووووری
از نشریه اکیپ فرانسه: آرسنال با نیوکاسل بر سر انتقال برونو گیمارش به مبلغ ۹۰ میلیون یورو به توافق‌نهایی دست یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102421" target="_blank">📅 14:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102420">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/529b07ca6f.mp4?token=iPn3zpPQHGvHVr5gQ7qK0nvO0cW9kqeKOm_X0pMUDsiF73cHU9HZrZG512Bq1vcWNfFeFKjHME78vSH3gECCIl8TeN6amTv8vqDzWMHiAmrGWbwbr8pq3IJVZmMM3IjJ02RQ3rGD38beIP1N6ErvgATVrXc4WWjRCZAvOZ6R_1R75a2d_M5PJIKYDbDxJ9FLOJOzupZLLHHGtlKnVTvZcIC8bAkP27_yXpOoy8zD2F_qSczIIaB2zVsrHsg0yJPNeZpxxSNt_3oDtxy7aAHaw6bXDBb9vtmC2oOG_urN1uVNPadtdpIxH3k58K6PSDimAKUHUJWuXQJU13Z11LCZKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/529b07ca6f.mp4?token=iPn3zpPQHGvHVr5gQ7qK0nvO0cW9kqeKOm_X0pMUDsiF73cHU9HZrZG512Bq1vcWNfFeFKjHME78vSH3gECCIl8TeN6amTv8vqDzWMHiAmrGWbwbr8pq3IJVZmMM3IjJ02RQ3rGD38beIP1N6ErvgATVrXc4WWjRCZAvOZ6R_1R75a2d_M5PJIKYDbDxJ9FLOJOzupZLLHHGtlKnVTvZcIC8bAkP27_yXpOoy8zD2F_qSczIIaB2zVsrHsg0yJPNeZpxxSNt_3oDtxy7aAHaw6bXDBb9vtmC2oOG_urN1uVNPadtdpIxH3k58K6PSDimAKUHUJWuXQJU13Z11LCZKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9889076a09.mp4?token=ukBtSxoHPbLvNCADbxteBR3zSAUlupU14xI7_4XHCD_zxsi78uGniVYCaO0HPch1WN3O4t8PCdT6rJkvm22UyWfTRR0vcFFyGUx86Ww21c1J7qZY_Ts3SmtJJNfgykirTuvi0rKgGqfEO_XQzAFpXb3detGg5yl41AWrANKRoW5D4gUAnLN-pN9xGieeLh89cdYJXgmzLjdeDqxwHgHaf_2I8EaBwzAV3lF1fAttXcgbVkc3q0FwqTc8UrOC2krDmjfHS5ASZpMQ1OHCj91qPyDSn23vDUvwNX-8X62A2Ae_itWEXlQASLlWWBHFBjJveRbz0zPnEmmj75Qk--ADhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9889076a09.mp4?token=ukBtSxoHPbLvNCADbxteBR3zSAUlupU14xI7_4XHCD_zxsi78uGniVYCaO0HPch1WN3O4t8PCdT6rJkvm22UyWfTRR0vcFFyGUx86Ww21c1J7qZY_Ts3SmtJJNfgykirTuvi0rKgGqfEO_XQzAFpXb3detGg5yl41AWrANKRoW5D4gUAnLN-pN9xGieeLh89cdYJXgmzLjdeDqxwHgHaf_2I8EaBwzAV3lF1fAttXcgbVkc3q0FwqTc8UrOC2krDmjfHS5ASZpMQ1OHCj91qPyDSn23vDUvwNX-8X62A2Ae_itWEXlQASLlWWBHFBjJveRbz0zPnEmmj75Qk--ADhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
💥
روزی که پیتر چک آماده ترین گلر آن دوران فوتبال میخکوب شد و این اثر هنری شاعر رو تماشا کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102419" target="_blank">📅 13:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102418">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A416nyiUFQhB07xc0M0UMxn6fTv8COrdXZSPWpzuuNKKFHD3x0JhbpIw4VkiRRyr_wv6Jo-QV4FDRYixpvZipJ_TNKMhXchDAAa7CvJwryxnnBGJvDbcrhgVrby8j7ejbJ3GgC_MySqZZ6quTKSIYzQG7trr8oaqsJ6hxCtsQMtg97lQje7rq60mFcjol8iuHf0JxvJnW21OCLnFSzL3be3IhuJ6SqY5p8yJK0pfXS_C4lRp79ZsAungBEtARx9lTe-LVJRQsVTlC1myilUtqrQ9xbeFqhoG5a1n04RDJWEVjrlEyNZfW_W37cqK69yObzJOdU2N98pU6YdFLqelEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
کارلوس اسپی تو تمرینات رئال مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102418" target="_blank">📅 13:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102417">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4zqABClgQqsSp_aK7dGb3aBKqOfJM6iGYwVSC-pVqiA-6rcec9VsNB31nR5FGgMd9nYiKZO3jZOtdNw7-IR8lPgYnm2J52W03hKcsEVsAWCAn-MoKukY3Ktlx8p79gixbvyBu3BPoNqADpfTHxdblsgE7vhy44BiJDu_-BpqkhgZzHhupCMed-W5cC03zNNOu3LTWufmtFWchem7CcOAmYQ5jQAs6JNFkg64l2YkMeKzddPW-qhhtvBE-7PB_uZcPHnap2GdtA4B_ETO3ATVrhkkiT1nMEXjHaQ5T7u9IxnehAwXbYAjL67jdGb-ek-tbPNAkzHfUxnofUExs1_8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
روزنامه اسپورت: دو باشگاه آرسنال و تاتنهام به رقابت برای جذب فران‌تورس پیوستند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102417" target="_blank">📅 13:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102416">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4938ae1d8.mp4?token=aXZEIBD0arTaNAhYV9DlBmpLQQiSh90kNmSSs3n2SJktYkLRaFc44-09qAtRESfJwbVBWBfukqyV_0T5_7898yuDsrYGBTl9jwvInr0RvrYdLzOmQBzQuABy5EPyIfAGBHEe5nPA6k6RR93WC_5sDF5lb5kYLDOt8Oxbr24Ks-jL8yVzNdj0vKkShrse_gUsX2tUBj583GEP_85U-rsknwcDK6z1IjGoqPUxvZxgxPoMC3p5ngAYWG29KM5fHeNOg74QpwlCO84PxbGHXX7itDla5nJdYxstiosjaRAoQL3CBP9s4Y2Y-rYUcq7VVrbRJ8mVZQEOCJJKvMHNU0x_ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4938ae1d8.mp4?token=aXZEIBD0arTaNAhYV9DlBmpLQQiSh90kNmSSs3n2SJktYkLRaFc44-09qAtRESfJwbVBWBfukqyV_0T5_7898yuDsrYGBTl9jwvInr0RvrYdLzOmQBzQuABy5EPyIfAGBHEe5nPA6k6RR93WC_5sDF5lb5kYLDOt8Oxbr24Ks-jL8yVzNdj0vKkShrse_gUsX2tUBj583GEP_85U-rsknwcDK6z1IjGoqPUxvZxgxPoMC3p5ngAYWG29KM5fHeNOg74QpwlCO84PxbGHXX7itDla5nJdYxstiosjaRAoQL3CBP9s4Y2Y-rYUcq7VVrbRJ8mVZQEOCJJKvMHNU0x_ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های بامزه رونالدو از ارتباط صمیمی با پسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102416" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102415">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5029f55db8.mp4?token=dNl6cR0QFCMohLCL9xOXGw6BMzjYRzdQBJcEzykTIJG0Zm-1cxs2ceiTcEZJDpC5GcxxEoievndti-B6RbbNlyZpYNtMZ7qqdL1UisIuOqQVuPhhKa3LcXHdIB7UDcVQ7eIPo9ZlOnUT9t4u0M9I96xUI69Cn2sgqlzTvVIq5JxRZjYLtcOl65bLozmHWf_mprU2IE5eUDWGTTgOZ7KJqUqgty292TCtGeVUDbbTSOMzpV3mqmtHfTk-hikvy36tE99GlB9h4pvEyLh8x7Jv5BcJ4YOpWUVuDWkQ-L8-nlDSbUa2aNe-odOJWr4tPOP5JZ6VEAjI_VF63JLE5opl4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5029f55db8.mp4?token=dNl6cR0QFCMohLCL9xOXGw6BMzjYRzdQBJcEzykTIJG0Zm-1cxs2ceiTcEZJDpC5GcxxEoievndti-B6RbbNlyZpYNtMZ7qqdL1UisIuOqQVuPhhKa3LcXHdIB7UDcVQ7eIPo9ZlOnUT9t4u0M9I96xUI69Cn2sgqlzTvVIq5JxRZjYLtcOl65bLozmHWf_mprU2IE5eUDWGTTgOZ7KJqUqgty292TCtGeVUDbbTSOMzpV3mqmtHfTk-hikvy36tE99GlB9h4pvEyLh8x7Jv5BcJ4YOpWUVuDWkQ-L8-nlDSbUa2aNe-odOJWr4tPOP5JZ6VEAjI_VF63JLE5opl4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🔵
درخواست کودکان جنوبی کشور در وضعیت جنگی از رامین‌رضاییان بازیکن استقلال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102415" target="_blank">📅 13:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102414">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac78119da.mp4?token=XRb2SAFRFvT_70N28ykwNEQ03soc96rkwvo9bAJTx-mMq4i6ZZe4yP5QlG7IZ3AHXTj5VlYzgWc2mQ_407Y7oS1HPjrFGn2wKm3VnV5Du6uJAu8Q-ulDLQzxJtg_pVzEPfQXtYjQSarScMCsc5ARccCFc3MYS9bPGpd3msQQjwR3lkd06j0o0oAv9T3R0ToEml8P9QkpK1t1oXuzMQPageCMqeGbCRonSzYZzqYRMrIE4I-75MZRS6jCVbt34DiEznSjZOqoF2qu1V5933BOg7o2Jsz3T8jixMklsM07pG5xa6L7NvEKexSb32hkmpJ7_CfwFZ5S8IbcdGQ9YECYsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac78119da.mp4?token=XRb2SAFRFvT_70N28ykwNEQ03soc96rkwvo9bAJTx-mMq4i6ZZe4yP5QlG7IZ3AHXTj5VlYzgWc2mQ_407Y7oS1HPjrFGn2wKm3VnV5Du6uJAu8Q-ulDLQzxJtg_pVzEPfQXtYjQSarScMCsc5ARccCFc3MYS9bPGpd3msQQjwR3lkd06j0o0oAv9T3R0ToEml8P9QkpK1t1oXuzMQPageCMqeGbCRonSzYZzqYRMrIE4I-75MZRS6jCVbt34DiEznSjZOqoF2qu1V5933BOg7o2Jsz3T8jixMklsM07pG5xa6L7NvEKexSb32hkmpJ7_CfwFZ5S8IbcdGQ9YECYsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75b732a95e.mp4?token=HPq-BDpTui5c2S29DkDEXiodV8rVIjiRajlo33-M5C3thQAh6VbhArckQfz7Ia1jTOeRC-5IYTPcRC7-yLRAUDJzKUx2OMhuudu-DhJqNNv0zpIE5NiH8s4hUe-a4j3PhZfgLNwIq9zQCxEK73g-1O1TqCj0jMy-hWWPrJzcPQW8ghF_PbLlsPWAg6nn10PoiIKZSyaIOBYbxrunzXclRbkeGJXxcAeOHdCnUULEk5U6YnKnzAuGEPG3Z04Y3GZRVSVEX7JW9Ihhent7voDr-M-KVBTlo46z5StfbTP7CWdKpt8UsVM99Cqk-qxZXkmxh_Z-49jdt_F2cMXGAS971g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75b732a95e.mp4?token=HPq-BDpTui5c2S29DkDEXiodV8rVIjiRajlo33-M5C3thQAh6VbhArckQfz7Ia1jTOeRC-5IYTPcRC7-yLRAUDJzKUx2OMhuudu-DhJqNNv0zpIE5NiH8s4hUe-a4j3PhZfgLNwIq9zQCxEK73g-1O1TqCj0jMy-hWWPrJzcPQW8ghF_PbLlsPWAg6nn10PoiIKZSyaIOBYbxrunzXclRbkeGJXxcAeOHdCnUULEk5U6YnKnzAuGEPG3Z04Y3GZRVSVEX7JW9Ihhent7voDr-M-KVBTlo46z5StfbTP7CWdKpt8UsVM99Cqk-qxZXkmxh_Z-49jdt_F2cMXGAS971g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇧🇷
آنچلوتی: "در هایدریشن بریک نیمه دوم بازی جلو نروژ اشتباه کردم تیم رو تغییر دادم که باعث شد کنترل بازی از دستمون در بره و ببازیم..."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102412" target="_blank">📅 12:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102411">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2964e2f72d.mp4?token=PpiOLSQfYYEjMqniuNhewKIAF_HstHXyN14VwcSQ9ZA5D8wEfeA1INi4wLMIj3cq_FzJPK7ET6T7bxwxzTDLzhLG1VT6JUew0ZsX_yQN_jo-mzdlH6WhjsRWrlMkAiYecBgCCL1XeJ-HGkbbKw9vdM2MUGvTup9GM3gZoZZUgXfo6fqKGi9XhgTwsu8gwWnYSOCx0pthx0AcW9nMNnETqRGNaJVrqh_1z_G8m1NIWV7devZCwJU5MdNA-fSWeqVJqzP466XK50ZBGCJFH51b6PQtkyKmxg8GULzRgzqsaH-XodB-G1VwCVQXmOke-fo67J5aePDBKsZpeghV1p5u3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2964e2f72d.mp4?token=PpiOLSQfYYEjMqniuNhewKIAF_HstHXyN14VwcSQ9ZA5D8wEfeA1INi4wLMIj3cq_FzJPK7ET6T7bxwxzTDLzhLG1VT6JUew0ZsX_yQN_jo-mzdlH6WhjsRWrlMkAiYecBgCCL1XeJ-HGkbbKw9vdM2MUGvTup9GM3gZoZZUgXfo6fqKGi9XhgTwsu8gwWnYSOCx0pthx0AcW9nMNnETqRGNaJVrqh_1z_G8m1NIWV7devZCwJU5MdNA-fSWeqVJqzP466XK50ZBGCJFH51b6PQtkyKmxg8GULzRgzqsaH-XodB-G1VwCVQXmOke-fo67J5aePDBKsZpeghV1p5u3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102411" target="_blank">📅 12:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102410">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b5a4f433a.mp4?token=PlcbqqJu28L6ZJWixv1QIBJeeOvGFnJc7RuMcmUZ0_E8ue2yTmUvBfoNP9I2Nx-Kbw3-sxaqNJAFDFrpRJcGPS9kMcF-OXKQi3s9sS_-Zkp8ANzr2u1AIfyArbN9rC99Sf4C5SS-lKeQ8FXkIJINde_dyKpgNJEWdRw8-O41pWJjIxLF2EVAjz9U_k-w_Ebb4AfhaB_TbJNi9-pGUqdQ1EQ1pNC_g9YrQTUCBt98cNrL2uaow0X6Glj1PYszjmn8Fn2jFXr6B2AhVWkOenp4BTubal6-jqOKqzy-d8zUw4YFHkmKS2aUOpAKumHq35S-UcDuC9Kp9B6VxIwCj1pHPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b5a4f433a.mp4?token=PlcbqqJu28L6ZJWixv1QIBJeeOvGFnJc7RuMcmUZ0_E8ue2yTmUvBfoNP9I2Nx-Kbw3-sxaqNJAFDFrpRJcGPS9kMcF-OXKQi3s9sS_-Zkp8ANzr2u1AIfyArbN9rC99Sf4C5SS-lKeQ8FXkIJINde_dyKpgNJEWdRw8-O41pWJjIxLF2EVAjz9U_k-w_Ebb4AfhaB_TbJNi9-pGUqdQ1EQ1pNC_g9YrQTUCBt98cNrL2uaow0X6Glj1PYszjmn8Fn2jFXr6B2AhVWkOenp4BTubal6-jqOKqzy-d8zUw4YFHkmKS2aUOpAKumHq35S-UcDuC9Kp9B6VxIwCj1pHPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c746b16b5a.mp4?token=RzCkqd1wndnwMQgUAB0b7tNjMm1N0Z-jLV6ij4NsvAWp4EKK3xcnLtHzj4iR6q80hxWwmbXKyXPux0We230jTzkej0muGtN0wenNU9T57Yns3vmcNWPbcWnfabHA2HSdWjeIYPE-x4XnawTfkgh8WQ9mtBejIBWa0UUb1KcLeQQfyTngoCqmrYzEo_uXquvDW7WmQjTDTDQHsfcwrei3TxjAyZ6GHEmpa3kXtYNMJjPUFv_EOThasMwhvPg52C1amhl95cfof7bbCEWYauRD0SQ8d71Y27Dt0Fg1Pu959gu-mOo80IusxhJ57-BYouEb_JVqTBs0eLoIsLmGze9dABWCBrsCfa3LLxWm1hpi-uQRc3jhQ8voMUU9ayJGrk3JyNeSsq_IKRseqOVydIkg5GbNooDU6DEdOxHjo6ecsUbUZkNwT0nZG92RroVYgZWrX3uw1nZm1n5raKI15XkAOmPkF-spD2Hok87UKPzwL5W0Ju33dZV7yC_OPF1ptkO69TDKtodjLaRW0i5RA_g8vhWdPcVckEDdTLSh7AtX0z8FEb3Q1EHc3e5m1GU7scNFzg2Fd2NhD4ZqL94CBOOGw11_w48djry57WaGCnnbLVK-etSzYaa0wWB-G2myPpH6u636br77PMVwoa2Q5dc27d9M3n1hqrMPCu3eYeJVE-I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c746b16b5a.mp4?token=RzCkqd1wndnwMQgUAB0b7tNjMm1N0Z-jLV6ij4NsvAWp4EKK3xcnLtHzj4iR6q80hxWwmbXKyXPux0We230jTzkej0muGtN0wenNU9T57Yns3vmcNWPbcWnfabHA2HSdWjeIYPE-x4XnawTfkgh8WQ9mtBejIBWa0UUb1KcLeQQfyTngoCqmrYzEo_uXquvDW7WmQjTDTDQHsfcwrei3TxjAyZ6GHEmpa3kXtYNMJjPUFv_EOThasMwhvPg52C1amhl95cfof7bbCEWYauRD0SQ8d71Y27Dt0Fg1Pu959gu-mOo80IusxhJ57-BYouEb_JVqTBs0eLoIsLmGze9dABWCBrsCfa3LLxWm1hpi-uQRc3jhQ8voMUU9ayJGrk3JyNeSsq_IKRseqOVydIkg5GbNooDU6DEdOxHjo6ecsUbUZkNwT0nZG92RroVYgZWrX3uw1nZm1n5raKI15XkAOmPkF-spD2Hok87UKPzwL5W0Ju33dZV7yC_OPF1ptkO69TDKtodjLaRW0i5RA_g8vhWdPcVckEDdTLSh7AtX0z8FEb3Q1EHc3e5m1GU7scNFzg2Fd2NhD4ZqL94CBOOGw11_w48djry57WaGCnnbLVK-etSzYaa0wWB-G2myPpH6u636br77PMVwoa2Q5dc27d9M3n1hqrMPCu3eYeJVE-I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔵
علیرضا بابایی مدیرعامل چادرملو: بازیکنان را از پای دیگ نذری آوردیم و با خواست خدا پرسپولیس را شکست دادیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102409" target="_blank">📅 12:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102408">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1b81246b4.mp4?token=rTujyG71eBeXKptfod3xbKiJuDhimMexBJuQmuHhLS1o-Yx0lpjsOJJTrfWkmKgLeb_IhFlTq9iXJRNAs7WX5v-JlRWtRCwQ5yfMQcFkK45boIb3VNy6ANQlsjSodoZYNmd6npwyw-Mydeqx9s0KKZXXwfrxfV0rxN008Ur0HVYSs-7u_HIHjOBpSKBT0R2czdvXTtZW4SWzM0j-Agw4EdUe9Wr6KHjMPQ2zJxtLu767fywdk2H5yw0P4Z_GpC-JqQs6AqMmV_6kMVq8vLLYFTfKKC6w_Zybz_CX9ZfqlzK2VydbSXeKL5MEDO71puB6ianfeCCiE6mX76X9YDNerjosAF35iG9jBhb3dQBPcvZdN9KczaTos4lPMYWLhtMz9EQXXy_5MwhlWskm92PFaq_lZVjZByi6abom48Y-6L0vBq7H0KrdPPv_lggtdRvLwnvRguJgkGv3yfts4G63Esz0RUfSLGiMx-CeC1mYceW_wgZ3_uQTtsNjuxWggiKxdRdWHr8P12oNG_ZylFkLfLqJdeuGzPKuvleJNvFqzFZFxq2xdijZb70wa0n-_IZzZfJe4JPby_S8U4WRPxUwuRFp_UC8hhgEdVqsPLX71J1PKYu-yZyZ3TvHbXsvR-O0wq3FlR5xgK5VdtqF6Sgom2K34OhZj1aOlz38S2LfqfU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1b81246b4.mp4?token=rTujyG71eBeXKptfod3xbKiJuDhimMexBJuQmuHhLS1o-Yx0lpjsOJJTrfWkmKgLeb_IhFlTq9iXJRNAs7WX5v-JlRWtRCwQ5yfMQcFkK45boIb3VNy6ANQlsjSodoZYNmd6npwyw-Mydeqx9s0KKZXXwfrxfV0rxN008Ur0HVYSs-7u_HIHjOBpSKBT0R2czdvXTtZW4SWzM0j-Agw4EdUe9Wr6KHjMPQ2zJxtLu767fywdk2H5yw0P4Z_GpC-JqQs6AqMmV_6kMVq8vLLYFTfKKC6w_Zybz_CX9ZfqlzK2VydbSXeKL5MEDO71puB6ianfeCCiE6mX76X9YDNerjosAF35iG9jBhb3dQBPcvZdN9KczaTos4lPMYWLhtMz9EQXXy_5MwhlWskm92PFaq_lZVjZByi6abom48Y-6L0vBq7H0KrdPPv_lggtdRvLwnvRguJgkGv3yfts4G63Esz0RUfSLGiMx-CeC1mYceW_wgZ3_uQTtsNjuxWggiKxdRdWHr8P12oNG_ZylFkLfLqJdeuGzPKuvleJNvFqzFZFxq2xdijZb70wa0n-_IZzZfJe4JPby_S8U4WRPxUwuRFp_UC8hhgEdVqsPLX71J1PKYu-yZyZ3TvHbXsvR-O0wq3FlR5xgK5VdtqF6Sgom2K34OhZj1aOlz38S2LfqfU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇪🇸
مشکل ایمنی ورزشگاه‌ها به لالیگا هم رسیده‌ و تیم رایووایه‌کانو نمیتونه از استادیوم خانگی خودش در فصل‌آینده استفاده کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102408" target="_blank">📅 12:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102407">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47a01fbf75.mp4?token=r78IVBNreD_qkJGbdDnxDT-WqXehVJhfnjO1-bLu_Y54b0iGCjGeEwHFzd7RsCpKfhWY4DwAKI9buERgp5dlXBp_BEswyeY_-b0n1M2_5vjK6wi2HFauuRdh4KJKglMNaH1m0f7ds2GtSTyhzc7F7geNMFH5myRfkd_8stCU0GCHAae1rk8E29beVkUT1uutyBXmG5inRQ-eadnZeachoY0o0-u3cmuSBbUb-xBUDzbam2WXI-bO6l45h3AuF3a3iVBZIoxRRHI5kLxp-grg8dXwW4ZBkf5s62xHWb9HeR_QaxCR7TEjYSAteOVJKTwrv6LgRSWsGAb9jM3n9cduJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47a01fbf75.mp4?token=r78IVBNreD_qkJGbdDnxDT-WqXehVJhfnjO1-bLu_Y54b0iGCjGeEwHFzd7RsCpKfhWY4DwAKI9buERgp5dlXBp_BEswyeY_-b0n1M2_5vjK6wi2HFauuRdh4KJKglMNaH1m0f7ds2GtSTyhzc7F7geNMFH5myRfkd_8stCU0GCHAae1rk8E29beVkUT1uutyBXmG5inRQ-eadnZeachoY0o0-u3cmuSBbUb-xBUDzbam2WXI-bO6l45h3AuF3a3iVBZIoxRRHI5kLxp-grg8dXwW4ZBkf5s62xHWb9HeR_QaxCR7TEjYSAteOVJKTwrv6LgRSWsGAb9jM3n9cduJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ویدیو وایرال شده از صحبت‌های تلخ و بامزه یک ایرانی حین ورود به‌تونلی در بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102407" target="_blank">📅 11:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102406">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262957043c.mp4?token=XO-NfSYQHMm1N7owb53r9VL7GRFvNnJY9jCO4NrjngZn94fSkFh7M8GdRESObQN00X656fmS5ShMCx8QidIb0uB13inwpN3_TEtSakfLg86k2bOucqYbpHTm9jiFlTiakGx4O1kgTBNvYh7g9FrFvuniFF8S0O-Ox8zzWmhyGn-k31OC_vz8-7zUwjRifTmz0JtJxMrADXtEBruRkTHxEUtl7umZav5Ve-lzVZEz1UZ5Be0s-4V9i3lIwnUGRjkB5MqUB0kl35PFuzqH7WvWyaTFmt-1RV6cg7PvQ082SbroaMZCxUWxD0wGYF37j504BpiJgun0qq4mMZCjj0i15g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262957043c.mp4?token=XO-NfSYQHMm1N7owb53r9VL7GRFvNnJY9jCO4NrjngZn94fSkFh7M8GdRESObQN00X656fmS5ShMCx8QidIb0uB13inwpN3_TEtSakfLg86k2bOucqYbpHTm9jiFlTiakGx4O1kgTBNvYh7g9FrFvuniFF8S0O-Ox8zzWmhyGn-k31OC_vz8-7zUwjRifTmz0JtJxMrADXtEBruRkTHxEUtl7umZav5Ve-lzVZEz1UZ5Be0s-4V9i3lIwnUGRjkB5MqUB0kl35PFuzqH7WvWyaTFmt-1RV6cg7PvQ082SbroaMZCxUWxD0wGYF37j504BpiJgun0qq4mMZCjj0i15g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
سوپرایز خاص‌ ژابی‌آلونسو برای فصل‌آینده؛ رونمایی از ستاره ۱۷ ساله قزاقستانی چلسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102406" target="_blank">📅 11:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102405">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef2180d890.mp4?token=it44ZcTKq7C5CW8iOSxJe19DM3tDOx2xUckdp3fLhMPvh3IajvAnEqz29G0J1eBKxiDTlAzj8973cpuqvRvPNJUTSiLZt5B2yEnQJ-uakdKHsAA5fy4ZlkE8jW7l4u6MUHzMnkMEBoBKVb2_kKtbRw9X6nbFIdnHSmUVbN_yPYg_wCoWsqxnY19Ln6F2jXcIQWjgcKgL5l75p7tx3kxYPzzAR-pNNio0TpJIspYmNK6FQTFmCfxxAGUlmbPd8JSoiEZCYFiUppvXbuRHLMLibMaJC_xEWd-j8Pbb9s9DQCYXhbYYo18WiICusGTfz0tC_obaEgWu7OWhodjMUWWZxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef2180d890.mp4?token=it44ZcTKq7C5CW8iOSxJe19DM3tDOx2xUckdp3fLhMPvh3IajvAnEqz29G0J1eBKxiDTlAzj8973cpuqvRvPNJUTSiLZt5B2yEnQJ-uakdKHsAA5fy4ZlkE8jW7l4u6MUHzMnkMEBoBKVb2_kKtbRw9X6nbFIdnHSmUVbN_yPYg_wCoWsqxnY19Ln6F2jXcIQWjgcKgL5l75p7tx3kxYPzzAR-pNNio0TpJIspYmNK6FQTFmCfxxAGUlmbPd8JSoiEZCYFiUppvXbuRHLMLibMaJC_xEWd-j8Pbb9s9DQCYXhbYYo18WiICusGTfz0tC_obaEgWu7OWhodjMUWWZxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
آماده‌سازی استادیوم نیوکمپ برای فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102405" target="_blank">📅 11:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102404">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31c9897d6.mp4?token=tbAD--SJCvduqgb0Kj78qIm2hKsrDLM4XqHQxU7nEUYgqVGsz_cHI9WtMVx-oaDpXOvob0RA3RC2CAlUpZwb4tmZPbTBRmVGlp7neOJm_KipzKs7Gd1NDKpdUtEmHyI0XCgv0HcBkZfLnkcd6nzQ2iv5sLoEQO5G8b9RqrnPYUE9ICFfYfOJNf6URQ8DMDFXvQjZ1uK2AD5FvjlRGztYytdqapwMV7RerfAvXyJFtqfZ5_vILWLOfpqUVXsKEipfZx4qBQBPVD_mYr-BL8-UhUMRMgT-0txK2mgr9nl68mLgIsDrXanZ5VlCGuetSnJbPaBiKxL1SeBoKekd5Lcksw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31c9897d6.mp4?token=tbAD--SJCvduqgb0Kj78qIm2hKsrDLM4XqHQxU7nEUYgqVGsz_cHI9WtMVx-oaDpXOvob0RA3RC2CAlUpZwb4tmZPbTBRmVGlp7neOJm_KipzKs7Gd1NDKpdUtEmHyI0XCgv0HcBkZfLnkcd6nzQ2iv5sLoEQO5G8b9RqrnPYUE9ICFfYfOJNf6URQ8DMDFXvQjZ1uK2AD5FvjlRGztYytdqapwMV7RerfAvXyJFtqfZ5_vILWLOfpqUVXsKEipfZx4qBQBPVD_mYr-BL8-UhUMRMgT-0txK2mgr9nl68mLgIsDrXanZ5VlCGuetSnJbPaBiKxL1SeBoKekd5Lcksw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
پاسخ‌تند و کنایه‌آمیز مهدی‌رحمتی به صحبت اخیر معدی‌قایدی: بذارید تو‌ توهم خودش بمونه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102404" target="_blank">📅 10:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102403">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
✅
کیت‌دوم فصل‌آینده منچسترسیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102403" target="_blank">📅 10:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102402">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/869e38d1a5.mp4?token=eEtsHXVnYKHYnrMYpLnz_zqiES8os8gI5Wj2wOaAWOAAlTrGnwCMLiDVhmljFyfUqPdHyk6L89IvLbhN-q0JxoTDPhQb1VhcFk64znhaPHH1CcC2D4HZ4MG-MhXlWs0pXWq6M6Jxd98sEOa7Zda6QZFXZeq7EhPw1kEaQVLBy_AtZUvzDcGIpiLOQoBGqwVOnUOmxmYDnnitbaNXcW1WGm_CtgrAiM1s6byeKIoarGq7OnDzKm4BzaQQCbZe_JUpzKwD1ywH0Qu0zucwNdOiFoyJzmGQPzpTENCSMZ61mh3rLq-rO2FHKVllc4hQBUbnQgF58OZs7SxU-C7lRuoFAoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/869e38d1a5.mp4?token=eEtsHXVnYKHYnrMYpLnz_zqiES8os8gI5Wj2wOaAWOAAlTrGnwCMLiDVhmljFyfUqPdHyk6L89IvLbhN-q0JxoTDPhQb1VhcFk64znhaPHH1CcC2D4HZ4MG-MhXlWs0pXWq6M6Jxd98sEOa7Zda6QZFXZeq7EhPw1kEaQVLBy_AtZUvzDcGIpiLOQoBGqwVOnUOmxmYDnnitbaNXcW1WGm_CtgrAiM1s6byeKIoarGq7OnDzKm4BzaQQCbZe_JUpzKwD1ywH0Qu0zucwNdOiFoyJzmGQPzpTENCSMZ61mh3rLq-rO2FHKVllc4hQBUbnQgF58OZs7SxU-C7lRuoFAoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
درگیری شدید فیل‌فودن ستاره سیتی به همراه مادرش با چنتا از مردم در یکی از کلاب‌های شهر منچستر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102402" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102401">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f0266060c.mp4?token=gdYFGpOuizG6BBVJl2i7Ede6zT0kETkZURJBZKI3KkOcr-tTYzz5EnrLSb7Kmp2ZIxiZm5qSkJ9CBdx9O0IZK7AF7mXSkK-8MXqEhjOvn5tPngrQkS66z1GXlzgYEzoeWxv8MEndnE67-33IMIC_EXGgyYlNPuJCigQrKQgVTIgH3tQrnXJDY-_5w04KKUU7dxhzDA1FOYAZEhSPYgn1942V3uzznIg2KnzzEwJ65tvJGaAqrR1mO0nPjwxzfD5ADZ7TPfIaWFpmfE_Xz6OI3qNDORqNUcG4vPHDWzkB805Hb96HjgdgyJNNittHSsFR5VEbjKgLmUQJerYTdVv4XDHhGk4LsWoZKzc1e2VlhrAyAL8bYZbtb1OGs0x0t1aHLbeBSTHtWQWJ0clwyylMSpgewR8Dw9binfsSlBxDvRtuEx6_zSdu9Ss5sXjnsMxv8o93gLyKMxrj_c8NC4gbuto_PrHxDcz-Ftc0WQyrybB0MefBit6WKYCgF7BLUoAhAhe1oSFRLM1MXiVgAuhdqBl6opRZDZXleWf7_b_5U61chc1g_RaDq1wWOLw-U9hEXGY2GDnkWYOCvquapGjzieC6UtcaHkRqhuJ6KC5qbfng0aSsPlAiTU-o8he71WqYkZeL6fsBc6C_iU4fYmGECOQHxFeeuwcY7a4mi_wAM_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f0266060c.mp4?token=gdYFGpOuizG6BBVJl2i7Ede6zT0kETkZURJBZKI3KkOcr-tTYzz5EnrLSb7Kmp2ZIxiZm5qSkJ9CBdx9O0IZK7AF7mXSkK-8MXqEhjOvn5tPngrQkS66z1GXlzgYEzoeWxv8MEndnE67-33IMIC_EXGgyYlNPuJCigQrKQgVTIgH3tQrnXJDY-_5w04KKUU7dxhzDA1FOYAZEhSPYgn1942V3uzznIg2KnzzEwJ65tvJGaAqrR1mO0nPjwxzfD5ADZ7TPfIaWFpmfE_Xz6OI3qNDORqNUcG4vPHDWzkB805Hb96HjgdgyJNNittHSsFR5VEbjKgLmUQJerYTdVv4XDHhGk4LsWoZKzc1e2VlhrAyAL8bYZbtb1OGs0x0t1aHLbeBSTHtWQWJ0clwyylMSpgewR8Dw9binfsSlBxDvRtuEx6_zSdu9Ss5sXjnsMxv8o93gLyKMxrj_c8NC4gbuto_PrHxDcz-Ftc0WQyrybB0MefBit6WKYCgF7BLUoAhAhe1oSFRLM1MXiVgAuhdqBl6opRZDZXleWf7_b_5U61chc1g_RaDq1wWOLw-U9hEXGY2GDnkWYOCvquapGjzieC6UtcaHkRqhuJ6KC5qbfng0aSsPlAiTU-o8he71WqYkZeL6fsBc6C_iU4fYmGECOQHxFeeuwcY7a4mi_wAM_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁳󠁣󠁴󠁿
نظر سرالکس فرگوسن درباره‌مثلث جادویی بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102401" target="_blank">📅 10:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102400">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f864b5c9ce.mp4?token=LNgLtMa5o4GO3HT-BiqQh3ZDGdo9sLX2YtyvWIZUtZX72Ur8e3FALxEZO_mMfsPttnWgN_yDObz5D_m9cQzT0zMglGcFwDqqe9NOq8xkrKH_fHQN9B7ZYm2NPSjFsNP9hG7V9eE_3cITggzpCb-K9VspHGonbe_tpAJU3CRLMtVpJAqyHYJIsfsShOA0u3KPLiQ6W08UWmV_y4UzUVD8rUCBo-buObEs4tYZKLRYpxz4PmN_f_UjrxZV8TyW1HE12priui0HufNpMrmDwWWHN1--a7MUF89ukYSvy81-F6qdbsLTF4hgfdt08-BAci48sIGSeAVi4H0MilZ1v-XQoRCjQyP4Ay4ufjxNkLphknUKujNZH8GWG9pMGo8fbin3DGIvjE0Lle7IJIIBKmYr_bR-a4_LMTChaNjySTgA0T5w32TpEaF31YTv36BN-31QFURZnWEd1aCTgrvufeTz3jTZBB5P6BUs39KdLDJ9-8rAxT34Pp-GqNKzcmA14BivlH39QCrAdWmqyEORs-ZKZl5t-8rrxSUG21u6x76DAgKB4sbErRK72n69W5FBFoUV2ekxIR7JKlmXt8y7rCB15MnYzOhkRvBv6B_s3YO7ZVWcXlEl67fvDGFMQcb6P0Ycvu7XwTH6b84uEu6vghUk9RgfZw9IVZhLsXs9YPRS0BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f864b5c9ce.mp4?token=LNgLtMa5o4GO3HT-BiqQh3ZDGdo9sLX2YtyvWIZUtZX72Ur8e3FALxEZO_mMfsPttnWgN_yDObz5D_m9cQzT0zMglGcFwDqqe9NOq8xkrKH_fHQN9B7ZYm2NPSjFsNP9hG7V9eE_3cITggzpCb-K9VspHGonbe_tpAJU3CRLMtVpJAqyHYJIsfsShOA0u3KPLiQ6W08UWmV_y4UzUVD8rUCBo-buObEs4tYZKLRYpxz4PmN_f_UjrxZV8TyW1HE12priui0HufNpMrmDwWWHN1--a7MUF89ukYSvy81-F6qdbsLTF4hgfdt08-BAci48sIGSeAVi4H0MilZ1v-XQoRCjQyP4Ay4ufjxNkLphknUKujNZH8GWG9pMGo8fbin3DGIvjE0Lle7IJIIBKmYr_bR-a4_LMTChaNjySTgA0T5w32TpEaF31YTv36BN-31QFURZnWEd1aCTgrvufeTz3jTZBB5P6BUs39KdLDJ9-8rAxT34Pp-GqNKzcmA14BivlH39QCrAdWmqyEORs-ZKZl5t-8rrxSUG21u6x76DAgKB4sbErRK72n69W5FBFoUV2ekxIR7JKlmXt8y7rCB15MnYzOhkRvBv6B_s3YO7ZVWcXlEl67fvDGFMQcb6P0Ycvu7XwTH6b84uEu6vghUk9RgfZw9IVZhLsXs9YPRS0BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
شباهت حرکت‌های یامال و اولیسه
🔥
😮‍💨
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102400" target="_blank">📅 09:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102399">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5630cebcb5.mp4?token=BjjyH5byYJu7parSGbVxgEYPG96Rz6B8P2rOojU0bJN4w6BDsfKJbRil-93fHSqfF09fbh5UNJSV-nLDLjP8nS5RhtbM1Gpw-Ss-9JpnmzDZ19wl-XDquTncj2_G0oWLDaJBd-yMEUpFvZTadHMgZPnxDrfRSc6yAOrvy7hI4MZnB4hil_0V4cvKTIwDMsIhLwXDioBaHkWyZacB3pn57A3XhgYYSzKUMxTxOTHCPDdkQ_zoWm9iEO0mrEgHZgv2zXUVMR65SdRurhpG0FqJfnnzXGwhr_k4mdKvbxVn_1MfYdN_QQc0cLEJXetjkXqbj5pd754ge6Jzs2ZiFBicYXmUK-GTaasC7XtM8nzB2ZwRLfgFEc2izt63M-gJnH_e1A1V6lI_w0tzWUhEPHB901Fr2ngXHJtw9p_kLvkipYOzFbap_oC5GDLHU_njcv272Op5IQHothoTb7Cayo_AcIgdcr5J0OTgJwN7tJvy18hONgOrF0HZ-gKHHDvMa2X7z-J_xx0F_JVzNhtGoJgI2hAzm_1ZoU45q9iHM-1TwzMqjMaTBTHZoqCRwqrBrdQ_c3WIBgP0tUe9G33uUclGWksU7xd05izegDfrAfbeXU8hdwAedSl_imIsbsxHkm0lmUJKYhsaM774SAdGpJ4xvVxxwI-P9P2nBG2Ciw7qQ9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5630cebcb5.mp4?token=BjjyH5byYJu7parSGbVxgEYPG96Rz6B8P2rOojU0bJN4w6BDsfKJbRil-93fHSqfF09fbh5UNJSV-nLDLjP8nS5RhtbM1Gpw-Ss-9JpnmzDZ19wl-XDquTncj2_G0oWLDaJBd-yMEUpFvZTadHMgZPnxDrfRSc6yAOrvy7hI4MZnB4hil_0V4cvKTIwDMsIhLwXDioBaHkWyZacB3pn57A3XhgYYSzKUMxTxOTHCPDdkQ_zoWm9iEO0mrEgHZgv2zXUVMR65SdRurhpG0FqJfnnzXGwhr_k4mdKvbxVn_1MfYdN_QQc0cLEJXetjkXqbj5pd754ge6Jzs2ZiFBicYXmUK-GTaasC7XtM8nzB2ZwRLfgFEc2izt63M-gJnH_e1A1V6lI_w0tzWUhEPHB901Fr2ngXHJtw9p_kLvkipYOzFbap_oC5GDLHU_njcv272Op5IQHothoTb7Cayo_AcIgdcr5J0OTgJwN7tJvy18hONgOrF0HZ-gKHHDvMa2X7z-J_xx0F_JVzNhtGoJgI2hAzm_1ZoU45q9iHM-1TwzMqjMaTBTHZoqCRwqrBrdQ_c3WIBgP0tUe9G33uUclGWksU7xd05izegDfrAfbeXU8hdwAedSl_imIsbsxHkm0lmUJKYhsaM774SAdGpJ4xvVxxwI-P9P2nBG2Ciw7qQ9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
شیرجه زد، گرفتش، زد زمین، شوتش کرد!⁣ جوک خنده‌دار بیلی مک‌کالاک ماساژور سابق چلسی درباره‌ی پتر چک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102399" target="_blank">📅 09:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102398">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FT88AJGQ0rpf6jEBTsF6_Q-7wIhgo839RltL_SHilh6_VzND4EunwvKxn80EtKgEW9JlwBUFnlLjsu9MY8YvLTZdN7bFine3dA3RKpBVpwBDiWpVadjLfKKJIWHfR1NBec7Iz5Q310YJzCaXwZf7IKIGVYxTGeDKe5sKLqIAL2ddm1b5FCgrU31jWPbaKnh9c7h2BOuoEZCMuAQnfLxrg08LaGKb2cWic_bTdlv1QwSKicWf00sn8x_E1IV8S3nknvq7zmiqhtgRf2f1dwSqLVYll18NcEz16bG6ifVI0IoAbFC3Ltm1kKf-tk1PxkXhxjzbd4XZnZ0XKCwdhhKL1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
🇮🇹
لحظاتی پیش، فرانکو بارسی، اسطوره فوتبال ایتالیا، در سن ۶۶ سالگی درگذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102398" target="_blank">📅 09:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102397">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d54a6dc02d.mp4?token=nCg22zujR3j-op1il2qAnHI2zvMyTXr7a8yc6PYc7miDROkGzSEGCzN52hCdJTAgxv1FdumguFCS5aQ-1msxXOiroOTxFIKh85UH17qSOtwlPqiIeL7A4orJOC_AFAOHMzXOEGVZqODkrLXfT3AciFWi7XommR_hsrEcvmSiZ3Yq3XeNbxEh7lwje4W0jMvzrKOPb7XVk8nOy5TGVC68PVOikuOMEYYbwzkYwdjj5xhOZU5eBnjrRtU8VlN76284xbw7KiererUoREfPfC5A-hTimALbg8syKmi4k2njTgfD1xAI_iP3rTc0-W_EU5DQtPeN7vt3QpvzaCNHUWAOTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d54a6dc02d.mp4?token=nCg22zujR3j-op1il2qAnHI2zvMyTXr7a8yc6PYc7miDROkGzSEGCzN52hCdJTAgxv1FdumguFCS5aQ-1msxXOiroOTxFIKh85UH17qSOtwlPqiIeL7A4orJOC_AFAOHMzXOEGVZqODkrLXfT3AciFWi7XommR_hsrEcvmSiZ3Yq3XeNbxEh7lwje4W0jMvzrKOPb7XVk8nOy5TGVC68PVOikuOMEYYbwzkYwdjj5xhOZU5eBnjrRtU8VlN76284xbw7KiererUoREfPfC5A-hTimALbg8syKmi4k2njTgfD1xAI_iP3rTc0-W_EU5DQtPeN7vt3QpvzaCNHUWAOTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت فوتبالیا اوایل هر فصل
🤧
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102397" target="_blank">📅 09:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102396">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e396ec62ed.mp4?token=HXPz2pPF6pKrYb4GnEyr2WiNv8Rk4DmAWe6zWyNfzOGWN-nCQUt4P75PRryiMvNi6JFMtwQ4qOKYRofdvHmgL0gXwrpnhXZwtJvhxp0d41HEbGzLLk-BpD3wPV_kRBHCIOzkP3QFckL1lNX7u3JKrCeVc0ORIoOnv1-4rL2u_KwGmdDES2JszMdKJv6NQ4A0hUXDlPhAKZgLy9VzVoT-dYECkw8WfaegzyMTB4DvMD8K1LdMEsUkYefPRvm2kz-3MTk8LxXkfSDyRvSUai9U-7GxbGCUYCKtmMtAFBRLhMJ2dTiY_XKbQKbLxVefQuz-v9-UQcDuKKoV41bNEDQzxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e396ec62ed.mp4?token=HXPz2pPF6pKrYb4GnEyr2WiNv8Rk4DmAWe6zWyNfzOGWN-nCQUt4P75PRryiMvNi6JFMtwQ4qOKYRofdvHmgL0gXwrpnhXZwtJvhxp0d41HEbGzLLk-BpD3wPV_kRBHCIOzkP3QFckL1lNX7u3JKrCeVc0ORIoOnv1-4rL2u_KwGmdDES2JszMdKJv6NQ4A0hUXDlPhAKZgLy9VzVoT-dYECkw8WfaegzyMTB4DvMD8K1LdMEsUkYefPRvm2kz-3MTk8LxXkfSDyRvSUai9U-7GxbGCUYCKtmMtAFBRLhMJ2dTiY_XKbQKbLxVefQuz-v9-UQcDuKKoV41bNEDQzxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
نظر پرز وقتی مورینیو میگه وینیسیوس رو بدیم به تیم‌های دیگه تو این پنجره نقل و انتقالاتی...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102396" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102395">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usC3MjxTk7OLFtS1Eipez9e092FhoQ0KVbmykmPpILILZHFWOxqFApBwp5CnQjska2WnG4HBNHC4Y7k_fl0vvIM0s01vBf06JWPOFLz_y6bEPxwFE-FWWbWYbGv1dlNagkYQs3SzCgeVAn5ouZSPEeBTAQhzJMkTZGCS5RoBiw92yfOgO0ZrqTiuw3XYiClMFlDQwXxAAzvEkLe26mr3VtqX0Lik3q9JXCSC766PzYiWKccjC-buqls0k9D5NJZejkbub7W6mKpPPUjhRujIQ1nYD2YYwxFHLWJWs256mdeoQQNa6M9nS2Bn2CVrkwXyamoQyd4g58Rc1A_qziSNqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🗞
رومانو: حاضرم قسم‌بخورم که دیومانده بازیکن رئال‌مادرید شده و فقط تا وقتی لایپزیگ بازیکن جدیدی نگیره قراره رونمایی رسمی انجام نشه. اگر این اتفاق نیفتاده باشه از حرفه‌ خبرنگاری خودم کنار میرم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/102395" target="_blank">📅 03:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102394">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJ2RoSEKKOBRsqfO56aQ23j2Et8Y7G_6Yq-ul8e_MyQbp3P80LhhTf5bjZWYU9TF-mvGwJqOkx7VtoXvk-belZcCdDgU5bKGYVoBEm0xNuYfG30g3Zo0Y_KwWzOiHKs4QvtWJtiwyK8rsyBXj73bdYLKG_97KflDDshFlw4kESjKOKbCQCNO1yW3iD8uBnyy9esVSW5GXtpRBjO4ntvzyLHZjiDWNSyB-XWXy8XXJiLzY37XYa4os9e25jJ-2QoU5ko_Yta7U5DNZoLNyLfTJeHcex9VK0FHVJ5CQEtPfWNfyEVSbzr_sguphZ9nJ74QW7iXqsd0uWfIzZCVdlRKmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کاسمیرو:
خوشحالم که اینجا هستم و به لئو مسی کمک میکنم، او پادشاه فوتبال است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/102394" target="_blank">📅 03:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102390">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iW39Ry0CixmHeYo9vpPiVQPuY3o1OR7CSvkxwxzuWJ3MksrHATDgXfL7mlyzDo90icliic87uON2sHpOL0LxiTTLZm--o6GA4fS3f-0wp8hsJG8CszEGmsyBWQR2D6KeIpTA9G9xc80svwFTg59WRb1FECCkXcpud9mcdTHgjKouzmn2A5z1llJfZr04QOZ82qkHbEcmcXEmNPsVeEwu5OFv_9VonAwUAZlBafiCq1LBoPfnqq_rw-DUBTaHwW3FQ1r6tnnqsWMSEm3AqbGu1bokaYOHoQvCFugAKJ-evIBOShdb4zfhN4FQCJUDRD50yBe9BgOITQa53RFmXonzkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iHwT0tPkLBJx-a7IBLakgw6YDalWRLUNelf4QHH8nfy_ceu1RYPRE_sIimjbV1dGwxokTTQqjZevRaR80q8NLtKySuZk9od87cAccLbp9KSGjulpXrnOHjUfMaHoBLfxut4uBCBPLw39g2QqJP7ngcKr0mURgCU_QfnU4n3mPKqnUL0KNhOWRE2WLoQcN5g5uGcnkrwIcijdQiEcr1DzUdK4lqlZplThxRqKNf2JLxOxmGwa4wJqw6fX-C_UuWDYDcxjXZ04iWk4H3pR-4pq8R9i5iTOsnkbnpzWOnuem8y0G8NAfUEkKnJPEl5vDFL-RA1axnzUATJdQhW55Sw3Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RU8SezJje7Dos9o-nYRnO8GjNpC4-Jnw0noz_C9DsgsbLkkXOJQyJr8mpc1d-AH3QESTaj4cvJnti39GxdIcxL8vVoxACESi6S0gR86s-Kd1vst9Cl22sWYllwali6YdjzrL6bLVfLKLnfyf_lJiEVe5QcyDJMFtZvutIh6u8kSBnXiJdRVwpm8lwGtNwzwDEJcclmZtLzyLi0SREhUasPjRRRY7sbKfcbU9dtgI2DoJlr-agD5xENcUmYfMHJbJuGQKMmvIYumsQsCC1sBl587XOkxFRy7nxtM74OdCPGf1PxnY0SjlczVQ71SmdC6kqLy9vRP7gQDRJKqPJF-Hbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/COc7l9ymQxYcUCGS4NpnPHKTr0d4xCb3GaAVULhmDVpYlflVOZRtMME6zIyHuyMWMP34yhCbea1ie2x0sZh2bvK6u-KTlyd5LmVRnEZEE-s3T77ijoYBt9_qowcuGtVQ8G_75l4eZB3Z2LnylY2SBmLpfHGRy6IuAo19KZuTsg76uRB-K5oSWI9IhUcvjHdsvrxuM7lqgxe4y_C24g_lhnmyISSTO_vEmgLPs3igRgNsu44gWF1fozq73mQPGLsxcXmji_5Wg_wFQe0ProcFOwYK0aDY_S0rX6QIRLHI8NavHNUsscOWQiNINX8-bMoSjX5RwPOY1-oLtglNSjbh2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کریس و جونیور و جورجینا رفتن عشق و حال.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/102390" target="_blank">📅 00:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102389">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/511459b235.mp4?token=BpZGaIWpLHDTKRC6pQkzw_O81aPZlDfCTGwr1TaVS2pASv_DSsX0Q6DWoHo3qazV-VuPSGgcEziDYtw2EUuvsvBy_MCyj-_hxYM3A8TVUgYZJnP0L9x0jhBgnBtXlCqRyeoRkA2f8Zx0MyAwYG19wC8LQDUnvFtv09hDnv6VdBWgOtRuh-l4QCpUm_m1-8yCLwI0F3Qt3ZKKx1_0lOM8AExao3C_PBFwtd_3cfMQdS9kTm2wOoj5_niZd3Qt11W222YyzzMOMRphefMenOlaGdj66sO90CbRzLzz_mvtC0-JNkd1NHw3qvR9sOjG5XGbcxa2qSzkdLzWfXiqHhAdUCYDWg-MMyE9K7El4AzNPJHqUSTEt8g9h14GI_yJwnx8Xk4vZmCm6vkTOtwWi0-PUB0GeA_jM_qulvVnCd6CQgE3sRgx6oxFm2mRr70jQaeJrsgE1N_xWDSD66slsiaH4ThNbgLxMbOWUJYAnDvxH6DU1Ck4nGBx98JI59WAklXM2uMUy2Y2gqeAAU0FecSL7gPfNPQXAGbW6MqpB7xU9uEyQ47E1MVl2WcZ6h7Mz4UooGuoQLx8ApZEELIl4kDYGzdMzXH100MRhKGJ3DoSEhWbBGL2M-UednOvHNvXVXNca9wp6EzNlml6o-oV-HkIm26FiTjXyYakOOp_7U6nRW0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/511459b235.mp4?token=BpZGaIWpLHDTKRC6pQkzw_O81aPZlDfCTGwr1TaVS2pASv_DSsX0Q6DWoHo3qazV-VuPSGgcEziDYtw2EUuvsvBy_MCyj-_hxYM3A8TVUgYZJnP0L9x0jhBgnBtXlCqRyeoRkA2f8Zx0MyAwYG19wC8LQDUnvFtv09hDnv6VdBWgOtRuh-l4QCpUm_m1-8yCLwI0F3Qt3ZKKx1_0lOM8AExao3C_PBFwtd_3cfMQdS9kTm2wOoj5_niZd3Qt11W222YyzzMOMRphefMenOlaGdj66sO90CbRzLzz_mvtC0-JNkd1NHw3qvR9sOjG5XGbcxa2qSzkdLzWfXiqHhAdUCYDWg-MMyE9K7El4AzNPJHqUSTEt8g9h14GI_yJwnx8Xk4vZmCm6vkTOtwWi0-PUB0GeA_jM_qulvVnCd6CQgE3sRgx6oxFm2mRr70jQaeJrsgE1N_xWDSD66slsiaH4ThNbgLxMbOWUJYAnDvxH6DU1Ck4nGBx98JI59WAklXM2uMUy2Y2gqeAAU0FecSL7gPfNPQXAGbW6MqpB7xU9uEyQ47E1MVl2WcZ6h7Mz4UooGuoQLx8ApZEELIl4kDYGzdMzXH100MRhKGJ3DoSEhWbBGL2M-UednOvHNvXVXNca9wp6EzNlml6o-oV-HkIm26FiTjXyYakOOp_7U6nRW0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
عادل فردوسی‌پور بعد از کلیپ دست‌بوسی که ازش منتشر شد یه کلیپ گرفته و میگه ویدیوهایی از گذشته من رو گزینشی منتشر کردن. هجمه عجیبی علیه من اومده! من اگه قرار بود چاپلوسی کنم الان تو صداوسیما کار میکردم و نَود رو داشتم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/102389" target="_blank">📅 00:35 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
