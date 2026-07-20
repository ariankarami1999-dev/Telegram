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
<img src="https://cdn4.telesco.pe/file/VodC7mPs4FrQXNI7816SdJh8oz1GJxa1vr6Qo63Hy4sSZ0Drh5plf5xmY9lEj6aY4UCtQLNcQzbxB99TAXB2qf2Wa1ra4Ka5NdmZi5S6dAwKE6OjMOiWkJgtyi7UHglsutJ2uc3YQZRLQbM4yD6hI63HLxwO1Afrrm5VVrhxh0LqRU9O7NY4_v03619P7ozwcAzfz01Az9MuhN_dZ5Q3BLgOEgxCoPYwdBY9XP4zztZDBLTL5dLe7NaGjg4H6t5sZSKnkQ6BsSYVUgOSv0hUZoPwVKE_6JlW7nICtdbQh-Eg6NocZEycvj09DYEJl0MYoHN-p_qHIro2Rf1FQ1hAnA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 529K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 16:52:31</div>
<hr>

<div class="tg-post" id="msg-26148">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIoC6dgeHCxKfcGbldjQKzc1w7B8fnugWuFkXCPz8xQphTh6iHNrN3BSA5uNd8JYgFa0mJ2pIFWbhUIYmhVgAtT9CFIukecWcQnSNCbiu1GxSORUc4zwRgHdT8_BDM9ZuUcU_aB1zhcEdiyXhkBG5b2hPxDSLNfZzwzQHmhYqM1CGHPxlwwheibmKPxPGuG4pt6Jy7-no5J9d2n2GDCLhBQdKBaPiEsatFwRE59mLpdsM2OHSsiOiL6k8d8F8YSJ6QOrpBFOAMEiqNF11VdpA6IYkBhJBS-OSveMemvSKoQHdZEF923uBdQ-pyBVUCp4P78XYetlta4uX_cU95WuUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
تو نوزادی مسی با اون همه افتخار نشست کونش رو شست. تو دوره نوجوونی‌هم‌یه‌کلی جام با بارسلونا برد. تو 16 سالگی‌قهرمان‌یورو شد. تو 19 سالگی جام جهانی رو برد. این وسط هم بالای 10 تا دوست دختر داشت لاس خشکه میزد. این بشر دیگه از خدا چی میخواد؟ چی روش میشه اصلا…</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/persiana_Soccer/26148" target="_blank">📅 16:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26147">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qX7uFQo1ZBTrj0BJT8X5rvI-IgOdtoaV6Hr6P2Nyg5xiDF7oIVuuLrtclk7c2GHGHkz7lK2Uv-Qj9drKk2uymTpzX0hWW2sl6E_JeqBXYYRVoOy8HUof_9fFZBY4CtL0CnGFMXkawZ1zrawae_rvIlD9ylJ7mUvmmTDNHWv5XLyKWBbp79bDf01-FLicIs0dpFVjfUxBIo3vJa2smkpNfPJFMq2zken7lKJse_un8y-9imbKRlFZUNREWcF4zzZM1Z7vMtlunv_vykWck6yZuR7PHpRYRK9VOa7uVS0sb_SpgIzSFW7sLkWNB-soQWO1d1YlHJd7d7_kyGWDWf94Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آتزوری‌درحال‌شخصیت‌گرفتن؛بعدِانتخاب روبرتو مانچینی‌بعنوان‌سرمربی؛حالا پائولو مالدینی اسطوره میلانی‌ها بعنوان‌مدیرفنی تیم‌ملی‌ایتالیا انتخاب سد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/persiana_Soccer/26147" target="_blank">📅 16:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26146">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6eX1D63Yzj2NHWsx8PFDqO6diGPFkAYWzIwsm4XdYiKazjmth3sA9zW45lNOvRJmlRYWo6ZQNvOaCubxPHEQ-7tZyGRhXZ-s9a9SIuHTEVyyegTN2WkBlDLwgQGnqp61VhTkCA36uDElaPuAk8wfjnH9S0ShzVJDB9fBrI1hlmqJy722kZSNU2FCiz93zN36AuXHZSXb-lPFuPoFN4aYlXyiNYe3ok3Y1HKFHbSaj4WFPh6FTmZ-D1brM8fSruTscBJ_EBZH6RWSp1CvuUfwvX9LpyJRuZKdYb7mmY2R8lM4oVCADAL3z8C9FGygQHdkFvcw3K6OJ67T4iguK9sMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛بامخالفت‌تارتارسرمربی پرسپولیس جدایی محمد عمری وینگر سرخ ها از این‌ تیم منتفی شد. ضمن‌اینکه محمد عمری برای تمدید قراردادش با باشگاه به مدت سه فصل دیگر به توافق کامل رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/26146" target="_blank">📅 16:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26144">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ezu-ih1th5T3y83hWFqPSqrWD66PNyytjAzVDCDdLrgdRPbiHwhwF85nTbWFy-DDv_r_NROl5rWx98Gdgbi_1GUdJNZs5rWFX6fhashxL3AOA1yfQS_Pcwq2f4OSUZdFR9LIxWEMcox-94mf6egCTbo1ig7xLdTmyUf9AI7-_P2cBp85HVGMo9WsSDn-IatMOaOV77wzoc-MC8PQyCLl6VYzA9Df-pv-ozf4obJmkpJ-n_bxc6SbrojtjzcG730qsb1x95yaL8bdgEKn_qHP9aUdidAgbQpWjGFjW3YEF32aqpQmoiuWxmUVFgbA1DsZFyWag6BEy5U0I6-dwwZm7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iy3-TIyKME5fXq_N6s9V7-EgLXXJfLBv5RAJE97s0EPWMxlR8KGD6jSbTKHKFvXO1c1Fm9tLHoaHjkqoLjlFkfSv0hEsjM28B57Tfd_96dw70c6yWO3jYSp54sGX3XPpKnE-1kWhEExzAVmskOEDJA076YGjpSDtQCPMfPqh3kjijofYqHVtCfPhoOCRtBTcsHuL4qhvsaVZIBh_LHx8J7w4jT_fx5fFwIn1w5IJO0s8ZABZY_0ipz_Z4odtuXLwEUA3SyX4kf0Xx86nSL7oTYvLYpjyjzNeXibA1guR0xwvoYUg0NRwuJsBw8vLaQOKywhdSvMfMQDLDrxm3QKhXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
اسپید، یوتیوبر معروف که بشدت فن کریس رونالدو هست‌ شب‌گذشته حین اجرا در اختتامیه جام جهانی مقابل‌چشم‌ میلیاردها بیننده رو کُتش "فروهر" نماد ایران باستان و آیین زرتشتی داشت و به شدت مورد استقبال ایرانی‌ ها قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/26144" target="_blank">📅 16:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26143">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EfSWo4Pg6MXeq3DY-yHM1vuD8Gxu3mFAlqDm5fZl4exuv7cksv_jX1uxjY-Fs9UvVaD5RR6Bf7Ul78dY1nie6e0kHesWv4ztwuedvgZO67wz4KKP06quYQsqDL7zeoYr8zi3GLH8Ukfs2XR9kOLtY-GQRzzkkzYcL_v1spluZkQ0ex8rsM7aozpyaLkfUHKJpKbUdZV5UcFkM-9qzgKSyWjVH3Lc8WU4RhsE_181Wim3yCUxq1wp8-FyqFW1Mos2wOaARmlo7OhPnZDtw1JjJIoLi8lzKb3L5DpzV6I-C68bz15PkhQ_DzelfLozPs3XmenSokNpt0uRwxfuV8gfXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لئونور ملکه‌آینده‌اسپانیا: بی‌محلی به گاوی؟ من اصلا همچین ادمی رو تومراسم‌دیشب ندیدم. بچه‌ها فوق‌العاده‌بودند و یک‌شب‌استثتایی برای تموم مردم اسپانیا ساختند. نمیخوام راجب گذشته حرف بزنم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/persiana_Soccer/26143" target="_blank">📅 16:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26142">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afcXrHHHKPR9oRwkIbhzCQ0_KLkd3WOFsHg2sBfTyR-zz4ycSBHJec7saz25o92fgueme0oJ9bEFin7RO43OkS1y6M1u3X40EqddaICIJ9Rk9ZB2BJfYsfehWZPVdQP47i_8o_QeZ_mRbPCMu6P4KFZPrhUU6G1lMo0lfLQHEV9fa4yIZvOQJ0TSTf8sUfZ5mi5H4eT5YBuv7hLbwzELHiOEFUhdjMY5Jcl2_UVrisBfntnDLJQdG4RUF71KXZ2UhaMVZHbhcwqnXJosrVmV1D_WkI2sTrcG8BEMh2xGdVQ4Qm5C2BcT6buGGOQP2VWEOMPdWsGnLnAimNf0zNsR2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال ستاره جوان اسپانیا و دوست دخترش همراه با کاپ قهرمانی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/26142" target="_blank">📅 15:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26141">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-L-9sjgKp75l_Ww8yt-4Hxy1_N4euOVcPM79irh6-DIR5afaY4icpQqb_zKj1ZC8Q1PMME16KG0do6OcKeoxxFAyC7FxEGMNlhmpYMI2azitz-i1GKY4MLqrHVw-Hl-EpKdkXiIKbR6WG-IFGIUsC0OQ4Ox0qVShzxDwxfWetZMbfN5-k0Cslzxiz4HpmPzUu4yI0JWer5nCv6za2Z0vHzK1DHBeYSG6AG1hH4_VEVd00tb5yGh-q7MfUhe3QADh6zJ79PhEdwryDnMuSO3vVAa0hS0S2giyDLgiEuafOaR-YR0iHucYWtzLY4s_wbxvdND4WaoX8P19w_GuZ_hCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
وحید امیری کاپیتان‌سابق‌تیم پرسپولیس به‌مدیریت.این‌باشگاه اعلام کرده‌که درصورت تاییدیه کادر فنی سرخ پوشان علاقمند است که یک فصل در پرسپولیس بازی کند و در پایان فصل از دنیای فوتبال خداحافظی کند و به کادر فنی سرخ ها اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/26141" target="_blank">📅 15:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26140">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6473e7bf72.mp4?token=NhsRYvIW15wRsHeuunSp0QZxX4aox-X15zYxkzXe0GD6GLQg6lW4s6hJItFTzhV5Gpe2fKdv3DR_KV6zoRZ_INYo_1Isd9LpF6nGKPWRXca-EtXaZ76TPPZrT6wkC4gs4qLakfp7VSp5Wz2dKu2e3uManzarFrmf5PSPMNlLmK4au14uXJt4_QhEXnl_agHgvxQDhIKciCdlb9NqQTfx55Tovf4YialkIHCgUskxX3x3Lfmj_I73E5PPnrIcl_DRGqYEl_E62kj--kNfJq--YGUc4Wacj_HxFzPPt_qwj7MYr57XCmY3jEdjksRkkRp5ZAln958uVDr0PYr6j_E2Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6473e7bf72.mp4?token=NhsRYvIW15wRsHeuunSp0QZxX4aox-X15zYxkzXe0GD6GLQg6lW4s6hJItFTzhV5Gpe2fKdv3DR_KV6zoRZ_INYo_1Isd9LpF6nGKPWRXca-EtXaZ76TPPZrT6wkC4gs4qLakfp7VSp5Wz2dKu2e3uManzarFrmf5PSPMNlLmK4au14uXJt4_QhEXnl_agHgvxQDhIKciCdlb9NqQTfx55Tovf4YialkIHCgUskxX3x3Lfmj_I73E5PPnrIcl_DRGqYEl_E62kj--kNfJq--YGUc4Wacj_HxFzPPt_qwj7MYr57XCmY3jEdjksRkkRp5ZAln958uVDr0PYr6j_E2Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیس فوق سنگین روزبه حصاری بازیگر مطرح سینما به علیرضا بیرانوند
: اینجا ایرانه چاله میدون نیست. با کشتی گرفتن با بزرگ‌تر از خودمون بزرگ نمیشیم با احترام کردن به بزرگ تر، بزرگ میشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/persiana_Soccer/26140" target="_blank">📅 15:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26139">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHwY2KksjQODTyZ-JknPdBvspQRM1bX9QLZaNxaE4O6_4Sut92v4kdGIHitX4xk_85qmNi_liMiz27NN_U4xpOA9Qnkw_26jInkDjeM7hsHJqYylD1amPWpdPIpPbHHXGxYOlkc38eVJoT6byAYpulFfApHCEusPRBbKLixFV4PiXAm1g_MVNiQohXwsggQ923uCSsyBuevx7KFSF0um6803x9YUL0sTplVFaTNHFUKW6XO4U4lKJwPNKAcwnBwSBlCGzmsObcEoYgo3xmdpk0GuA7wQBJv8LIB5KuXL_0Gpb-HIAwK5u20X_-eLOkFi4UY5z3x9YwI_39N3J7GUDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استوری شدید الحن علیرضا بیرانوند علیه علی دایی اسطوره فوتبال ایران: من را با رانتی بازی به جایی نرسیدم که الان بخوام الکی جانب داری کنم. ترفند هات دیگه نرخ نما شده آقای علی دایی!!!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/26139" target="_blank">📅 15:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26138">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sftX0W9nj_Y6fQEZeT9GLtDijRZkt3w0pJcvWDYA7n4MiRJu3DAIwanVNKpgZhSGy0SZe7MD4BcCPaH_-8z2EWCFxWe-ufmRyIib_4Z2RjDgiKmbnf9LCWulFcwlutL7RbzTDO97jQoDXM1ILj-vKmuQTg2mVffB1Qu9yMP0Ort1WFVraQE6zBPsydpt_5tVtoAiVeOKPgTYORDi6Wy0iCW7_0y_drhHY_HkyVKx2mK_aQ0EpYvun6Ynzlbfzq1kuCpJIUPUNb3-x2pDdFXsbwc_ObV9zrzDRud9SgSMZ07ZALz0I5dZ8EcllQ4liD_0Y_IP86jmNnCa1tWdtIKBvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
آرمین سهرابیان مدافع میانی سابق تیم استقلال باعقدقراردادی دو ساله رسما به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/26138" target="_blank">📅 14:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26137">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gom1r_2UpwmMSlVfe6YTTN485mJj1PQ6o3XkrksXXPyM7A91GLVinAGSBvIDGpguBOToJvewj0rzgGLIPwksuXsFgRdBh_pDaeEMF3jUEBmilUsnr7IY1ueWS6FglkvdjODS2R1_0mYN4xH5aAuCJyb2ZjyyXTZObY4SFyvff3tdredsgpLjrXAvo9QN2ft0nf9fvxmqHFSnTRPIsPln35GRAxTRgTcwejEnskUhvO0DWid4zWz8-TMFj9ci8_M4rsVrSJDs7g0Nm-jfCAkMw-LqHIlP_H_2DWpULGYAKKjD45ur7OsFglzKpfVWPEpYzpT9LpJvAmg4C5WAFfA7bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...بااعلام مدیربرنامه‌های عارف غلامی و آرمین سهرابیان در ترانسفر مارکت؛ این دو مدافع میانی از جمع آبی پوشان پایتخت رسما جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/26137" target="_blank">📅 14:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26136">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه فینال جام جهانی 2026 شب گذشته عادل فردوسی پور؛ برنامه جذابی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/26136" target="_blank">📅 14:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26135">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbkR_UUOz2FCZYJGPFE3K33F0JZEWxm4zwT4COkbec6p0P5ZgR8XzmmA4p-vTsYJfYJwsHPiaK8t7xwzHsvNgU18NESrXLRAuUPc-GvGLj8Vl26aRVL0ZDP1pT_Wkvbis-oWXV-C4kJ18-TW-85OBgjoiYYRBtZeJzBxF5vEAvLafOflknCzQ7ThDtCgpym-1tJmmJEGi7BPnpPRYqmVf0etkV7wBbIlywJPi-bxgTvextONXrXykqoy-4EESCIoe5flN50gGUSZlmgXm1Bbh_NjgFBu9ugo8GphoVeBRTF6MjciMAffPi5vI2QRz2-5ttuYC40HLJYiuWe0wpudMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق شنیده‌های رسانه پرشیانا؛ مدیران هلدینگ خلیج فارس از عملکرد مدیریت‌فعلی باشگاه استقلال به هیچ‌عنوان رضایت ندارد و در هفته پیش تغییرات گسترده‌ای که مدیریت آبی پوشان رخ خواهد داد.
❌
علت نارضایتی هلدینگ بابت هزیته هنگفت برای جذب ستاره های خارجی استقلال در…</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/26135" target="_blank">📅 13:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26134">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzKcFse0x8u7b7o_Oon8PLXIiJC8GSAPmUhib-aRC0JJGtEPrQRMftZzlKwQYxlOi_nUYn4_PH2VAJ_fBE-3VdmIYTYJjRdH-g1ogCfQDBMkshiB24iBT2n37z1bRYRVi7FHkROoSWXROsE68gIYv3Axc-LSMapQtF0NYUPqoiSV92MbpG-n2qlLEJULCd-X3FZvdbCaxAuHJkvYj_3GuqRpRTjSVcag6sZjT1jA1ELH4ZiMfdXVrQAqFmnrqhfCpiSJAzhp3Iw6zBMIc1rcaw15WlVsJFNhkpRhRYIWLKB7GcnFXj1MF9uHUkxb_kktLoov0nHNplZEfoMOaAq9dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
🇪🇸
#فکت؛ مارک کوکوریا مدافع جدید تیم رئال مادرید درمرحله‌حذفی‌جام‌جهانی تا فینال حتی یک‌بار هم دریبل‌ نخورد. یکی از بهترین‌های این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/26134" target="_blank">📅 13:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26132">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHO7FXrO-66cWx8Dtp-Y5v-MoS4FcGGvmPIf3iFEGOeZT1vlXzwT-7fjcHoI2BNosNGVc4lWKeZ-Cvo6JWz-Uz6whF6vchhq1ewjXNNiRsvE93zmbRtNSG4cE6PCFuNLL65-G5fWr6Z7LVRVxhq3gDTNMZl8fkC2iTxa2BLLEoW_aTFPwcFXdTk5x1peNcPAFVuPVcdpZECmpf-YrVyEepYm4IZmM9VG1LuGYDsSb7IQGh8ubWip7spyJv_A2zWiR0V6ctDOzt9gtSjL-b4s9Irh44r6PftDhbQq6vviK87Hl5hlayP8UyWVuCyZIwE8kEqDMac5J1pB4dDY5TUllg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه نساجی بعد از جلسه امروز با باشگاه پرسپولیس رقم رضایت‌نامه دانیال ایری مدافع تیم خود را از 190 به 150 میلیاردتومان‌کاهش داده و72ساعت به‌ مدیران پرسپولیس فرصت‌داده تااین‌رقم روپرداخت کنند در غیر این صورت توافقات طرفین بهم…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/26132" target="_blank">📅 12:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26131">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxoSh4SnMnbyVWseKGQqRZDPiZdknzCoiqtExYh397A-PO7oXLRzXVWb2YR5nsCCAuNTlKT66p65oTK-mdzKBW22c-ZTAXiEiRzNcIjflZ9eTle765wKeRD8xeMK2fQ2D0m3vO-fMF1WWV4sWokI_X89oR9Yqx2t7jE6l_PV9375KofSvXYGemElvocfcMbF-cfmbMgRJM5ORg21eIVM7cffHN-CeY4AdSpDucjfVQNpIFs9WPSyL_EICLmsX6_iDJJvih9smZtp8S9T2ZiyHsHaaGVwQI86GebffEg2joBS9BzZBQ6zFXruHkMmrW9B6Q8Tmyolg1tDw5bXXxCU7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون بریزه؛ میثاقی روی آنتن زنده شبکه سه خیلی‌جدی‌گفته آه مردم غزه  ایران تیم ملی آرژانتین روگرفت و باعث شد که این تیم قهرمان جام جهانی نشه. بعد همین شخص اون شب در گفتگو با گلر تیم قلعه‌نویی‌میگفت این چه‌حرفیه‌که میگن کارما مردم باعث شد که تیم‌ملی‌ایران…</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/26131" target="_blank">📅 11:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26130">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFN-Uf3bdPoHILSJBUa2Yr8EO15msXCmj4Yju0cOSZv43NIfknYOy04cfsKt75s88RumZVOTVGSEPW58hnK6eycvxeQG3DEoFBs4zo41e3e2nw57HeYXWW0HCfb59-Er5A2uWbxT6c6dZvUMUT8BPT1PD4Udnfc-kYLmYF2dC-9wAJZx2gi4NV7WPyVA2thfoq0GSUrm9sjnY4LdGoqYBLAisFH2hw8DnJ7FCP75NfQzCs0Y5VYdtmMeiizhWx8AveLRxDKZ-gSYaMxJJ-95IvkVBrYGfX7tJbenBQh3oxKfelusvB98NPR2QoPd_YZmEuqxIGNipirFfBf6P-aJYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون بریزه؛ میثاقی روی آنتن زنده شبکه سه خیلی‌جدی‌گفته آه مردم غزه  ایران تیم ملی آرژانتین روگرفت و باعث شد که این تیم قهرمان جام جهانی نشه. بعد همین شخص اون شب در گفتگو با گلر تیم قلعه‌نویی‌میگفت این چه‌حرفیه‌که میگن کارما مردم باعث شد که تیم‌ملی‌ایران…</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/26130" target="_blank">📅 11:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26129">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyHFyxZcKWYlsa9iGMUDNG6cZ5kn_-dvv_rV33sZpJC0DcmhI_EAu6RhIq-ls7WZIt8XXqrK9CyQkOiKTI_DPIpF9ZPZMV-vbw2sSGLSzh0fmXPHCSxgpVCnvdh7Gn-yvJd0EasNrlkMcTm0ltn-j8oqu132_6RlnoRNYGNvOMVQGYkZ1KXAtwYFOaVUZ63tKEyvN4s6evTrp2Si87KTZ_ZXG4Y0562Bne7rtkvoSS5ZUHkyoVJZHs3h3GTb0IENm1SEEjOEgJBPSKkBejbnr6Tuad6ogBREbBX6x4mjVacJSevnFfIKcmx2H7GBIqBqaaksQc5Xr06AWbq1R_FpRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
#فوری؛ باشگاه پاری‌ سن ژرمن بزودی قرار دادی چهار ساله به فران تورس اسپانیایی تا تابستان 2030امضاخواهد‌کرد. تورس به مدیران‌بارسا اعلام کرده که‌دیگر‌علاقه‌ای به موندن دراین باشگاه ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/26129" target="_blank">📅 11:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26128">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/202f77d369.mp4?token=EzVPGDyzWBj599KTeFBF9zrqZeX6oDBsgLCWVd4soqMjpqCOXuds7KMqzJo0Jryay_AUxW7-pcjQy-qYXDF1dVJUmf7-WhcrrnPZC5wAXqeYVjqz99Xu_q00_sTDklVEA79sF7PBmYXruzEUm5tdLpxDax-u62N5s66UWJTaf50xYSiLOyFg7WF4gSvdgelQH0qWcAzYya5a-iQg5ot6DiP2YC1MYt-dWqDJSwi5ov6BVtfud6AHYBgYDGgBHLueNV3IJtXqGV5fq11-maZNjTJvzX8cVGrurdd1yCexj5d7t-ZGwW_UIzwF-F_6Rukvtw9x42K1lYKuwGOS764Si7fKE7DenOr7fzfUGXagk-onfzC1XxjofrkUPY5K9B49bXxR2HLTY1i2qz0KWX5ZqY5r4Wz3MGDkv0Aq_1ZuV8OpWz4XOu9-AzBIDi8VTAnu0zTPsml6MGcxj_l2xqwgAfuUGIqMAJOcxgkQ44Xxkv71DuZt2EvERQRhinE7-c-JMGJW6GzJr1R_FLoEcUNjiTb9pWY5Ewv9VE9mUkJqLLw-kf7mKfwclVXcx23RCdWW2jsIXHlzn0OHgafTYVtySc79hyujB4HfqE649axb8GhRbW1irU859L2cKxyfer2nqKCKYUe_9_4xOT1TStQpB0jvXZ39dMUWz-M66aOmvtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/202f77d369.mp4?token=EzVPGDyzWBj599KTeFBF9zrqZeX6oDBsgLCWVd4soqMjpqCOXuds7KMqzJo0Jryay_AUxW7-pcjQy-qYXDF1dVJUmf7-WhcrrnPZC5wAXqeYVjqz99Xu_q00_sTDklVEA79sF7PBmYXruzEUm5tdLpxDax-u62N5s66UWJTaf50xYSiLOyFg7WF4gSvdgelQH0qWcAzYya5a-iQg5ot6DiP2YC1MYt-dWqDJSwi5ov6BVtfud6AHYBgYDGgBHLueNV3IJtXqGV5fq11-maZNjTJvzX8cVGrurdd1yCexj5d7t-ZGwW_UIzwF-F_6Rukvtw9x42K1lYKuwGOS764Si7fKE7DenOr7fzfUGXagk-onfzC1XxjofrkUPY5K9B49bXxR2HLTY1i2qz0KWX5ZqY5r4Wz3MGDkv0Aq_1ZuV8OpWz4XOu9-AzBIDi8VTAnu0zTPsml6MGcxj_l2xqwgAfuUGIqMAJOcxgkQ44Xxkv71DuZt2EvERQRhinE7-c-JMGJW6GzJr1R_FLoEcUNjiTb9pWY5Ewv9VE9mUkJqLLw-kf7mKfwclVXcx23RCdWW2jsIXHlzn0OHgafTYVtySc79hyujB4HfqE649axb8GhRbW1irU859L2cKxyfer2nqKCKYUe_9_4xOT1TStQpB0jvXZ39dMUWz-M66aOmvtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
گاوی در جشن قهرمانی خواست لئونور دختر پادشاه اسپانیا روبغل‌کنه‌که لئونور پسش زد و نذاشت بهش نزدیک بشه تا به‌نوعی انتقام گرفته باشه. لئونور در عوضش با پدری برخورد خیلی گرمی داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/26128" target="_blank">📅 11:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26127">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcihDwsCoyDfqG3i8XhpAoytQlrCZSZvWX7lHI0tEMKQOvsA2fBYJ_aHU7NjASKSafbW_mkAH_-vgHne7zpYrT7TeqoqN_YUeAB3TYLVXo1dhSKPfjXZ9QmYw_gaSw8GMEhw-POyveROiD7l_BkaxrXXbAA0pSs-1RWVmB0TFFBzm2ZXRWcrHa1VfVgGRjeePadNGS3UwY8k2mHB9qx3WhVpBKZF4Vj4zo4nuV2YMGBW9jCo4Q1NyDBPIJNuSDlNsovRBPIrSIUIRAfwH8Oj_MNUeFSw3Z7BzB5hiQ5ddzPV5sDpC_lDXbRQ-1zih7aHOp_2NUGj6FmH1pyFDXWkvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
طبق اخبار دریافتی پرشیانا
؛ رضا شکاری وینگر فصل گذشته پرسپولیس دو پیشنهاد از لیگ ستارگان قطر و سوپرلیگ‌بلژیک‌دریافت کرده و به احتمال زیاد درصورت‌توافق‌راهی یکی از این دو لیگ خواهد شد.
‼️
پیش‌تر در روزهای‌اخیررسانه‌ها مدعی شده بودند که شکاری قصد داره به باشگاه استقلال بپیونده اما پیگیری‌ها نشان داد هیچ مذاکره‌ای انجام نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/26127" target="_blank">📅 10:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26126">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27dd0a5169.mp4?token=POsPw7obDXZSZdJA3mKo7IajoBmjrwvgCy0do82dFlOLxNwq7KtcX_KaWOj1ynuf6D-mlhm9VA1IystaLD__OX4o-ZhDL2udvPnt0gulvmc7TXjwPfrMyBXEeZc8hquqKLJ3m7dEVyamlKGzxH3yWcXv0akRTaA8RKpa3dvfHNd3cRN2Z2zjWhWvUrZLs5k6WRlh6og17F9W5xjH7K6ZBDN3KaI8CfMSzpczW2UhUex5qBgDQ1xw7-3JdadlYi0d6Lw092L9fnVxABhqZ41Z1JvE4Cxytd_FA4XpiihcT2iGypKwrTeS_-qu-RTId9OnlUi91_A18vG6xKwrAoXL6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27dd0a5169.mp4?token=POsPw7obDXZSZdJA3mKo7IajoBmjrwvgCy0do82dFlOLxNwq7KtcX_KaWOj1ynuf6D-mlhm9VA1IystaLD__OX4o-ZhDL2udvPnt0gulvmc7TXjwPfrMyBXEeZc8hquqKLJ3m7dEVyamlKGzxH3yWcXv0akRTaA8RKpa3dvfHNd3cRN2Z2zjWhWvUrZLs5k6WRlh6og17F9W5xjH7K6ZBDN3KaI8CfMSzpczW2UhUex5qBgDQ1xw7-3JdadlYi0d6Lw092L9fnVxABhqZ41Z1JvE4Cxytd_FA4XpiihcT2iGypKwrTeS_-qu-RTId9OnlUi91_A18vG6xKwrAoXL6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🩵
آپدیت جدید تلگرام دیشب اومد؛
چند تا قابلیت جدید بااستفاده‌از هوش‌مصنوعی اومده. چندتا عکس رو میتونید مثل اینستگرام پست کنید تو یک پست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/26126" target="_blank">📅 10:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26125">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6a101f8f4.mp4?token=k-oTW9uTi9w1VZ5CT3jdgWWs0zXRqriBZN2zwYoLCliZKPMD0q5HMcVZ1f1FQbW7twVvzdmRIP5F5bZ8n03ESs8agFI_hI2cNIhcrpORttuM2J9zKqYR5490X7oMlq0tLUmF7MpScjDuAhVFv1n4H8d5GYO5Y9eKSuc6nFgNzfVdk0fqbiavZL9A2OAardorjMRr48odUvzXU4oJ6VnxSRe3qg2IZAjCKH1JHpXBqQk45cDMgOfR-xPqPO2GrHsCDObxpbPACJxBB-X4Xbkex2x9MvDQGbfYK4b5Pr23I6V4-xQs9v8KUk7IcfdUy2mfAjMQOAfXRdrAAnex5ATlvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6a101f8f4.mp4?token=k-oTW9uTi9w1VZ5CT3jdgWWs0zXRqriBZN2zwYoLCliZKPMD0q5HMcVZ1f1FQbW7twVvzdmRIP5F5bZ8n03ESs8agFI_hI2cNIhcrpORttuM2J9zKqYR5490X7oMlq0tLUmF7MpScjDuAhVFv1n4H8d5GYO5Y9eKSuc6nFgNzfVdk0fqbiavZL9A2OAardorjMRr48odUvzXU4oJ6VnxSRe3qg2IZAjCKH1JHpXBqQk45cDMgOfR-xPqPO2GrHsCDObxpbPACJxBB-X4Xbkex2x9MvDQGbfYK4b5Pr23I6V4-xQs9v8KUk7IcfdUy2mfAjMQOAfXRdrAAnex5ATlvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
گاوی در جشن قهرمانی خواست لئونور دختر پادشاه اسپانیا روبغل‌کنه‌که لئونور پسش زد و نذاشت بهش نزدیک بشه تا به‌نوعی انتقام گرفته باشه. لئونور در عوضش با پدری برخورد خیلی گرمی داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/26125" target="_blank">📅 10:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26124">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1235d344e.mp4?token=FoS3q79XJZqJ9UecqStz5SvEMoyYLwmDBcfKnE3tm2tyMsJM16qXdxSel_lr3Iosyu9hOyBNbSrQcTk9qZ_eW_m2JHMLn8YqsVR_C_JTyoHble2pu-HYYUMdT0RAaqTURQCjZ7humZfWQD7nRegBhYJl_jbOUfjmdLfSIuaAstUryQTFfUoMwT8lT8qQ2Bov34Wx4HGTMyqDkc9ZeYZ-Yo5d4ZJBg1ujLUQiH6EP3VywJSrqWQUEXH_gxyBZSl12ovdmTz_0Ms0CQgYfpsx_WDktGVp5e8cvza7sSg9mvIUdn0s_u_GPhiLFZDrECxlqNrNQree0FsjjU_P2Hb9fOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1235d344e.mp4?token=FoS3q79XJZqJ9UecqStz5SvEMoyYLwmDBcfKnE3tm2tyMsJM16qXdxSel_lr3Iosyu9hOyBNbSrQcTk9qZ_eW_m2JHMLn8YqsVR_C_JTyoHble2pu-HYYUMdT0RAaqTURQCjZ7humZfWQD7nRegBhYJl_jbOUfjmdLfSIuaAstUryQTFfUoMwT8lT8qQ2Bov34Wx4HGTMyqDkc9ZeYZ-Yo5d4ZJBg1ujLUQiH6EP3VywJSrqWQUEXH_gxyBZSl12ovdmTz_0Ms0CQgYfpsx_WDktGVp5e8cvza7sSg9mvIUdn0s_u_GPhiLFZDrECxlqNrNQree0FsjjU_P2Hb9fOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دونالد ترامپ‌موقعی‌که‌کاپ‌رومیخواستن ببرن بالا ازپیش بازیکن‌هانمیرفت‌ بره‌ کنار؛ رئیسفیفا اینفانتینو دست ترامپ رو گرفت جدا شه از بازیکن‌ها، جدا نشد وایستاد تاکاپ ببرن بالا؛ فِش فِشه ها اتیش بازی بالای استادیوم چرا آبی بود. قرمزنبود! ازقبل بازی چرا آبی تدارک دیدن!؟ فکر میکردن تیم ملی آرژانتین میبره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/26124" target="_blank">📅 10:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26122">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rmSVF-_FTtoTJ6fRG7HYeX20Vlsw0wCdgsGW0SM-IeXJgHRlAB4B2__AICkWb7G-Fe9mLnEPBb54UzBrXwLYLDOuxbsV_wwua_cqUPCmMt2tPtmoSDKdtk2fBm-7Bm_pEwgrjalkDOtErT_X64HE1LCeLVNrW-0Y5YuBOd4uKZnj0yJ5PuAgA97BoD-UFmaHPw2CffMLgCG_Ioy8v4gu46cBW7UR3i1zmN3CIEDCFeShaSFYrJVS0pQm_LZba34THtXwiH7eczvYPq9kGmXXdGuLtNf2hHh7Kj1jHNA0TtzIVB_KA4HotwWN568aoP6l7f_0W3Jfp7aELrAPqEEl_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DDgzcDrhislvPaPBGvetnfulgEzLyONP2R2t99y8kV7gTZBJMrZ0v8uH4wYOIn4_zaAcJWZCKtp13D_wJPhQXJ8d5mbc3xuUb5SoSMOQ4TdbyscNe2gRmUAY0LGCKPsdoVsaN0excMFwEmB8P59WL8TQ8lMo9ZW7xkYvmkgJN2FA_cwA8eQoAliZPRaBHRses2X12OydiBHDeJacNtSfhSbJ1JrXEh2chAxZazrIWJFLzRaAGhQLxKrDCZ_hHyYEri60ng6F5B0YGzhlfJ3FzYujVXXiLs9tUtpNJb8EcJG2ki-rrUt4RPObHZcf9FmidMLTDg_723nSQ8nify9lrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
گاوی در جشن قهرمانی خواست لئونور دختر پادشاه اسپانیا روبغل‌کنه‌که لئونور پسش زد و نذاشت بهش نزدیک بشه تا به‌نوعی انتقام گرفته باشه. لئونور در عوضش با پدری برخورد خیلی گرمی داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/26122" target="_blank">📅 10:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26121">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c071bd0be.mp4?token=GFHJjkOywZ_n2MfR1X4s6vglL-YgZZHOhY2qFusdGyJhQ-1fkLraJydfkWgSwEibGyyA4XgWq12Tp5pbc9lX2pgrf1rlTjDcIZcDdRYVCQ0IVOfQSb-WnDJjL3zdKCrdhQj4jrpf0c-SV7lSyE7K_F9nkjFGdwY-VT6fgBzZiCG_oqyPWHxxnXL3MY3xreoTMBh_ZQ6HeRWGGj6MxwcPouDBuctTa3-AF3I13NrO6cvPQ4cmlB48YYKncD5aQwc57GMOoQFy-0ju7ONI20zeJrAvLSa8aPNfOVkaFGJJKyKEMpChBla93lbCWeMwRX9SSeKWponeEJjpAyd0rf-6yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c071bd0be.mp4?token=GFHJjkOywZ_n2MfR1X4s6vglL-YgZZHOhY2qFusdGyJhQ-1fkLraJydfkWgSwEibGyyA4XgWq12Tp5pbc9lX2pgrf1rlTjDcIZcDdRYVCQ0IVOfQSb-WnDJjL3zdKCrdhQj4jrpf0c-SV7lSyE7K_F9nkjFGdwY-VT6fgBzZiCG_oqyPWHxxnXL3MY3xreoTMBh_ZQ6HeRWGGj6MxwcPouDBuctTa3-AF3I13NrO6cvPQ4cmlB48YYKncD5aQwc57GMOoQFy-0ju7ONI20zeJrAvLSa8aPNfOVkaFGJJKyKEMpChBla93lbCWeMwRX9SSeKWponeEJjpAyd0rf-6yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حماسه‌جدید خیابانی دربرنامه زنده؛ خداحافظی اوس جواد با مسی و میراث مارادونا با شعر مدونا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/26121" target="_blank">📅 10:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26120">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec0657aa93.mp4?token=MH3lRB1Z2v6fMMpbJGHyWUHZZIN8K8ovtbV0dgZU4f--Ee6zoZZxjYitZkXe5a7e-fZo8fJhSrVQaiA45a4pIt5W_-FvKpEj229Gh7MYt_QfGZLnvVTRe8HtP6TZ3bVQHXznd4ongjlkVt-o0XmDx1zVKFPX3F2FMLV8uqhT9Z7xehLhKuftTeB5dH-qVERoIuz34mn0zRtL_oq6sGnGHzb34Qwiws_DCygfhnN8e5qrcyorXDPLMiFOvzo5JaJUbSD99iMuEYljIcaLaCQthnp6_9uecKguKNPXLocBixweO5OvYNSLp0ugOs2r-id7mHFlUxmHKA3gqFXpYqElkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec0657aa93.mp4?token=MH3lRB1Z2v6fMMpbJGHyWUHZZIN8K8ovtbV0dgZU4f--Ee6zoZZxjYitZkXe5a7e-fZo8fJhSrVQaiA45a4pIt5W_-FvKpEj229Gh7MYt_QfGZLnvVTRe8HtP6TZ3bVQHXznd4ongjlkVt-o0XmDx1zVKFPX3F2FMLV8uqhT9Z7xehLhKuftTeB5dH-qVERoIuz34mn0zRtL_oq6sGnGHzb34Qwiws_DCygfhnN8e5qrcyorXDPLMiFOvzo5JaJUbSD99iMuEYljIcaLaCQthnp6_9uecKguKNPXLocBixweO5OvYNSLp0ugOs2r-id7mHFlUxmHKA3gqFXpYqElkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
#تکمیلی؛ اینجا دیگه عادل آن‌فایر میشه و خطاب به قلعه نویی میگه من تو جنگ‌های این یک سال اخیر ازتهران‌تکون‌نخوردم ولی‌تویی‌که خودت هرسری فرار میکردی تو ویلات‌نیا ازاین‌حرفای‌عجیب‌وغریب بزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26120" target="_blank">📅 03:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26119">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa1c44954.mp4?token=MA8WmKcC1iba_rYFI2ZHwTiiSHspXibMSpJJnn0-m3woBx4pMyvW0jzYZRz-G2-su0F6s8gd3HfWUEH1IzWMWTVg44U0f5I9TrETsurBsvU70UzYHlCY5QTnKmm922svqD4qmaGO_fLvodtKAZSZpD6NIh8vttrqAJ5xn56lqk_83cYHyDx0B4N0vtiY83jiNulGVzKpXdH4sFrRN2H8Nrku-gz3xXYJw6PoVtkftqTXo0bjVJrZgV3ce4AuUoOwfyDyLylHut8NJQ-WDBWlzwH2Sev505NGo2JxPZKeSavAzKzT6KXLaK0GDxWKfjFhWegFj9kT4TppconbECCoFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa1c44954.mp4?token=MA8WmKcC1iba_rYFI2ZHwTiiSHspXibMSpJJnn0-m3woBx4pMyvW0jzYZRz-G2-su0F6s8gd3HfWUEH1IzWMWTVg44U0f5I9TrETsurBsvU70UzYHlCY5QTnKmm922svqD4qmaGO_fLvodtKAZSZpD6NIh8vttrqAJ5xn56lqk_83cYHyDx0B4N0vtiY83jiNulGVzKpXdH4sFrRN2H8Nrku-gz3xXYJw6PoVtkftqTXo0bjVJrZgV3ce4AuUoOwfyDyLylHut8NJQ-WDBWlzwH2Sev505NGo2JxPZKeSavAzKzT6KXLaK0GDxWKfjFhWegFj9kT4TppconbECCoFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
جملات‌زیبای عادل‌فردوسی‌پور برای لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌دنیا در پایان جام‌جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26119" target="_blank">📅 03:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26118">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55d171bce1.mp4?token=BWfG8P99Ah0sSNrgYaGPZFBlQpsDeUAc6klqKIYWyZaW6RPiGA9_dyZHXJhwouJhn370kYp3xLpO5x5M5MQ8kg10vis6JLNKK-C-9q06IP9FRV2VPqPj4_FSfVPz68TDAQlmYbzedWJHRtOhmcVXm-rr7vQyk-eg5mnNc5-UOUxprlk21N4m9Dmx-KR1J68QS-RekNvWM00DkCFIWUxMeWRwAGYcwvdnMH2LCQ-4yCGWCgaS3L14UcO1imED4kB3-txLeosRcFwU6a8zyjFYXHZPRsy8v-lTqwCeN67Ra7gVYbLkQ3peZbjEzQbp91hdJCFno-8F1vGqO33ZYjz5rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55d171bce1.mp4?token=BWfG8P99Ah0sSNrgYaGPZFBlQpsDeUAc6klqKIYWyZaW6RPiGA9_dyZHXJhwouJhn370kYp3xLpO5x5M5MQ8kg10vis6JLNKK-C-9q06IP9FRV2VPqPj4_FSfVPz68TDAQlmYbzedWJHRtOhmcVXm-rr7vQyk-eg5mnNc5-UOUxprlk21N4m9Dmx-KR1J68QS-RekNvWM00DkCFIWUxMeWRwAGYcwvdnMH2LCQ-4yCGWCgaS3L14UcO1imED4kB3-txLeosRcFwU6a8zyjFYXHZPRsy8v-lTqwCeN67Ra7gVYbLkQ3peZbjEzQbp91hdJCFno-8F1vGqO33ZYjz5rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
این هم برای هواداران لیونل‌مسی؛ مسیِ ۳۹ساله اگر نبود آرژانتین‌حتی‌از گروهشم صعود نمیکرد اما او یک‌تنه تیمش رو تافینال‌جهان برد و تهش به هم‌تیمیای خودش باخت. توخودت‌رو قبلا بارها ثابت کرده بودی لئو ممنونیم ازت که حتی در آخرین نمایشت هم درخشان بودی و مثل همیشه…</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/26118" target="_blank">📅 02:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26117">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b94e4b0c7b.mp4?token=CLn7rgYtwpNrUH1Tt7LIJw5_PEjf9nQsKPZP5pLSYVJG51CfPh-zyZRSilhwR74uiBQonUYz0sk57JiS6ihvRuQD8_6JcZcpRJVZGZMh_k_ifnH1oW32UYYbnlaJPFhfS2icuetqOJIJ0aniacLfWJi2IHjBbb6_4i8rbXhLg03B96ApMoZ6kJj00pjeCR7EOPJHvHEjSnvN3bel2-kpLW68QGSrY6WlaFfIrVgOOuOHnX5VsiRZ4BHAdNEMiGVDiWMvlrSRBTriAi1kWug_XokBGW_INlosmLCbu-83NUkoqrw3NlSnQd7tf7SzphJyrsHL8IMVHnM52h4cfj7wCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b94e4b0c7b.mp4?token=CLn7rgYtwpNrUH1Tt7LIJw5_PEjf9nQsKPZP5pLSYVJG51CfPh-zyZRSilhwR74uiBQonUYz0sk57JiS6ihvRuQD8_6JcZcpRJVZGZMh_k_ifnH1oW32UYYbnlaJPFhfS2icuetqOJIJ0aniacLfWJi2IHjBbb6_4i8rbXhLg03B96ApMoZ6kJj00pjeCR7EOPJHvHEjSnvN3bel2-kpLW68QGSrY6WlaFfIrVgOOuOHnX5VsiRZ4BHAdNEMiGVDiWMvlrSRBTriAi1kWug_XokBGW_INlosmLCbu-83NUkoqrw3NlSnQd7tf7SzphJyrsHL8IMVHnM52h4cfj7wCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نسل‌جدیدعلاقمندان‌به‌فوتبال:اینادقیقاکی بودن که بازی اسپانیا
🆚
آرژانتین روداشتن نگاه میکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/26117" target="_blank">📅 02:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26116">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e72188ac69.mp4?token=fcG0Bed8mQ7MfmMApnFCAhMfmrrUinD6qMqaZdEKK6fBcJeuW65mYNXVHiE-fGmmctZKPZlE_ZcLaR2S1Doi-LJULfH1QT19V5Rwqf7utZQa5OiScuJ7ZnnaQ7DXCCjo1BC_e2ePmFyoMFxqyXiDc2ztu-qba4mUT-SUQdihdQHENsaIjh0dJeB6fsm4v8Ubze9B_KyyUCiaU0ZGlMMQRa_egOsqeVxcHeqUH_CUcY1np86DZzL4PU6Qgs0uz5ovsqq8KmxWOmrYH8YXpLQ1rUXQvxmHo_VhyzqfeBTsVnHBFZ80xEEbkS-bIqckvIGb6zrKqJeXZtZXy5WjwSSKuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e72188ac69.mp4?token=fcG0Bed8mQ7MfmMApnFCAhMfmrrUinD6qMqaZdEKK6fBcJeuW65mYNXVHiE-fGmmctZKPZlE_ZcLaR2S1Doi-LJULfH1QT19V5Rwqf7utZQa5OiScuJ7ZnnaQ7DXCCjo1BC_e2ePmFyoMFxqyXiDc2ztu-qba4mUT-SUQdihdQHENsaIjh0dJeB6fsm4v8Ubze9B_KyyUCiaU0ZGlMMQRa_egOsqeVxcHeqUH_CUcY1np86DZzL4PU6Qgs0uz5ovsqq8KmxWOmrYH8YXpLQ1rUXQvxmHo_VhyzqfeBTsVnHBFZ80xEEbkS-bIqckvIGb6zrKqJeXZtZXy5WjwSSKuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نسل‌جدیدعلاقمندان‌به‌فوتبال:
اینادقیقاکی بودن که بازی اسپانیا
🆚
آرژانتین روداشتن نگاه میکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/26116" target="_blank">📅 02:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26114">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGEt4PNJrWnG4E4IRQ-1Nc0YaQnXplP_t_DuVVnRxBagupxZ6YqGH0sCIcHaeVGepzDqZbjiSdrdB1bz9qjN3coppFlNYN8ELABsbelZtOa7Ej6tkV8Z6sgWFSU3nAzBvLMCgBot_iFtg8u69viW23fzH8OVGOU2YmJvsLCOlJuKWDcOtSkLjRApai6M4Q6J5l4x4VT-HJ-eH2dHq2G3mvBwpb8zVh68tVScHfTJKQbS4BTbZFxqZk-omVkV2bBrme_UksZT0hMXLKrZ7ITG2oIuchZx8Lc6DZslklbRfkLvfvf0RvcUZ9mekRqzHoW9wGz1OmQaJVrHBcT_P6Y29Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یادی کنیم از دست دادن فرصت طلایی توسط گاوی؛ سه سال پیش شاهزاده اسپانیا لئونور ۱۷ ساله به بازیکن جوان‌تیم‌بارسلونا «گاوی» علاقه‌مند شد به طوری‌که همه عکس‌های گاوی رو داخل پیج اینستا و توییتر خودش پست‌کرد و ابراز علاقه نشون داد؛ بعد مدت‌ها به گاوی پیشنهادداد…</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26114" target="_blank">📅 02:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26113">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvsfMw_EE5d3H5B3Ycfv6iwRH7WGxTHMVZSmLl4UmwwLSgoK0sSepqya34P09X0QUaceNJMCd-tTqzTTLj1xVivJ_69xT0Up8nsqfyGIEGjWrIDEnmMAaITOqo1MU2-MOOehEwQKkIbKvz80SWFZRPhp4pS1EHj8gS5rlC_wYjlMfwucvj6vgnMm00jE4IaKWpLsUKp0WS3s0TgOkPhp8-arJYI0AwP-27mMa9mpb09OA0Czes2TqztgbJrbn3WcbF8GSrZ0U2DsIyHY9u2XI6-nDpv7mx_HAA1pNynKQrGiBACxRKsAsmjaoz3SAAI7oDwmPsA4ZPRwMG1hwlF3gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
این هم برای هواداران لیونل‌مسی؛ مسیِ ۳۹ساله اگر نبود آرژانتین‌حتی‌از گروهشم صعود نمیکرد اما او یک‌تنه تیمش رو تافینال‌جهان برد و تهش به هم‌تیمیای خودش باخت. توخودت‌رو قبلا بارها ثابت کرده بودی لئو ممنونیم ازت که حتی در آخرین نمایشت هم درخشان بودی و مثل همیشه…</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/26113" target="_blank">📅 02:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26112">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRrEBx2Vzr_UOVXL49_Y2ZMz9QI6YzG1BF2zfqu_0nnwkBcEEi5Qvj9qomy_jeNzrHONBg1nc_6yP9ZAH_40bHaO4SsSUgEh4PCVRCkHOwH9myPwIPHT9r3Sxw7EErHqm1QXuUXcxs1siP0JiredEVVE3m1n5_dv8MyhnMHTTwAQ4N3sDH2v5edZgc8IeX2ogtDirZMiTsJNa8paRFKCHRLFxZ_V6Cegoq8bXo1jIJQuMMisyg-qX-dN7b6jAXYbI0ejdczjnTADM9g8Tqw7ul-RVQHwoHCBCxZN_opxfe_a4Agr7ZvOqpnXOKyEK5fogRj4eK0zhir7HmWNm2Ag-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#فکت؛باحذف انگلیس،ایران، اسپانیا و آرژانتین تنها تیم‌های شکست‌ناپذیرجام‌جهانی هستند! اسپانیا و آرژانتین بدبخت باید تا آخرین نفس برای قهرمانی بجنگند، اما ایران؟! ایران یک مأموریت مهم‌تر دارد؛ حفظ رکورد شکست‌ ناپذیری! دو تیم برای بالا بردن جام‌جهانی میدوند…</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/26112" target="_blank">📅 02:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26111">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3LA0DMol48sR2Qd2ka6V-wRKgdr9wMo3Hp-4Dkx6P3r3g7Eq9HaxuwW3k0aLodN6wCgq3CvAYV7biMGfLxTkoKCv5NkW8sZltB0_9LnfyvP15Gr1TF3CLGBoUY7SfEaMy51PgwULnvQ83Y5QKghnYkILC4A9rEDR2weChnvuSarJYsmPODbngix4T-rxn3qQinAHeBmaZlsPPJZcupo3gTmDFPRKMg8TfBZ2Tea8MPTpn0FG2SjskR-YF6Hs7RKqzRrGWWbKlDxJeYAEETqA0GwgjUHbFENWGvZDdVZhvfiOcJlh-F9IqKaaDJc9TGMlQYx-jt3_iig4OZGZ-nLOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با عدم گلزنی لیونل مسی در فینال؛ کیلیان امباپه با 10 گل‌زده آقای گل‌ جام‌جهانی 2026 شد. همچنین امباپه با 22 گل‌زده‌لقب‌بهترین گلزن‌تاریخ رقابت های جام جهانی رو دوره بعدی مسابقات از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/26111" target="_blank">📅 02:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26110">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcJASsa7uI5fZyTskH00Q1LovdxilTQz6P-zaGz4FqgdmrktzAoc47wnGT73MHwJJRqMvMDUEyu3---VES6dQ31NHWPHy8pk-9ikcop8uIiAYvRPq1_2pkn2y82XlOnf3pDoO3wqECbQv7i9tLH0HEHgPeUgYYdYobODi9fIaBOtcyTOdLD0CvXF9s-O4tnCX0Zp8RPQBBCN6O5YAV4WANYQSEaq8c29V0nLKxIgq-GJvBGEviYdLWQI65_yLW1pbQeaNZktNXIk-jx48RlwplvLkj-c2NmzISVHkTSaFEDrWX6OgNgCxKEB_A8pw7yDqauqxTt0DX-VGPzrDShCng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
پایان جام‌جهانی 2026 باقهرمانی اسپانیایی‌ها و گل نجات‌بخش فران تورس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/26110" target="_blank">📅 01:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26109">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ykntq1Z-Df6zOg9yLeOIfwTe-Wd789YV32Tn9RTj9h_zwjenTtpf5730xAHSJmEvxr_Zl-04_TC-FB7y322GFHD1aHpkz6oml_DjhT-GXg-1UIMhZPWrS7FqGl6T3HPgq5lp-qsFkcc2aItnnE_f8saSLR2E7NGMmt0z3-L37YwmZvQja6kX-7NDrH2G6PLtEbve9btT22vutjIiRhg_yvEqhXbGqbAq118ADPyt1vB-n3HhK7UEoOmEMbdhGIPA-wKGB8hf_30kv42WNIw4NNheB4oYjAz7_kOkcs_i5wzZPq2tZB6SRbmGgEr2cHwW7TO0CSavhr_RZAJpEyH1zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرژانتین وقتی فینال رو به‌اسپانیایی‌ها باخت که دریک رپر کانادایی روبرد آرژانتین شرط بسته بود. او در این جام جهانی روی هم 10 میلیون دلار باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/26109" target="_blank">📅 01:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26108">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oT1HWjRiud9nCOZj73ivR7e1FjfL7x-2yaqTC50vpdPN9V9NGkpPhfAXoO4qytSDQ02zcpzubwahb9iM3uctChce_X5o7ql0nCo5UOaVhQr-W9F-tJxfywU8o_6WGSUKy4KTY49sO8JPJonPiNd35ETI4jMv7puMSo7GL1drY29BSCuGMvi7Uc2qcZsikD85oxlGFcUdvVSieIcBNlNn-wUGUc4qvo6RXI_NeBVAJELB6SkuovyJM6pKn5s8S233LPPu0v1FSwWW3tIZKtrwWk49mKFWKU8pSyvD71Hp3NOEoIrMmDjBliDl5BQwXSk1I8IPWde2LhkQD_GFtg4QBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید بلینگهام هم اومد:) فینال هم یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26108" target="_blank">📅 01:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26106">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsdPxhEQcmNoOH-1929zRknU3esblGoEtHSzk7bKXBVH6tLbXNUVKRSisunwtbWFifi7TEEhaX6L97mZ-G7OXczg7ejpc_3jXtuUuYweCYzY5k0SEyGxkF7BkgzHnhpjNkT2AqfgsEh7U_IVulaMt8Owq8urgBcKrQ_VOlu_JBp6EuhqdSv9arX4PL3cGACnwRx5ogjPOeZx6_jVQUgT-AZ4Z0IFm_Wf2L9TXzZg0KaV4o18jzjgGPPZD-o1-dAfSnEPyJUEtfPPb9hQdPN55MVkJNiN0bLbwwfcRZBhG35lvvvz61DeJbXALDJ5Gn0936H6lkR37Br44yUzHfR_5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ‌جام‌جهانی‌ و برترین گلزنان این دوره از رقابت ها؛ کار لیونل مسی برای آقای گل سخت تر شد. لئو اگه آقای گلی میخواد باید امشب در فینال برابر اسپانیا دو یا سه گل بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/26106" target="_blank">📅 01:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26105">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQ6AMryTJWBcbPZsSWLjPNKENjPT2nseFLfIRePeFsCiXHG-4BOZg2Jp_xqGfdBes5jVK7xt2Zb3dA4kq5ieq71lINrICHjF1b6KjJrxKTWOjw9HIdcHPAsExCEeJU0KOMt9dRWTFv-Mm-wh_Dm_CdLUL0e7ts0KndoEJml5EkErioSD0ZvNJL86Yk22Z-pFP2O5lj2uH44er7TVq8qrvGyea0YkPV_z_ebL71voo09X5OcPTxW_44qiHImApvks1B3D-ZM1J7qCP3htF5ip9FmvHgg3ZsN44kunja4TFesOujSboV3Z_4ThGsgTXXO6x54_vGMtA-7V9E4lb_U59g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دریک رپر آمریکایی اعلام کرد که؛ این بار روی قهرمانی آرژانتین 5 میلیون دلار شرط بسته. تا حالا هرچی شرط بسته‌بود برعکس در اومده حالا ببینیم این بار درست در میاد یا 5M$ بی زبون هدر میره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/26105" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26104">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bO95-Id03FHTNCDeXofjpn8EQ305XttURN4Dm7s4XKJjVhSpp3muyShJ1ytjOhS2TUO4GgH5V64DQRv4qpIU7N23iEJRa_90vTv3-ifIzpUgKnsng0vn09-aeMZBNSDOr0Fhq7o-Bfj4FTpGghWdQhR8MJxDuMb1VeM1k7X3zhhAkSUgaVsCScgVrRStbd6Ga3gMfsHUFTUXwU1CybPszYgMCw1SyFmgWj1zn9ruKYhSu-bt0eHr1hsLTEmt0GkbrZYaQ33g72boXEwMWJHqZhzgDU2P5AGXWfW_-7JNRvUC6S996yvP6sYg5s2lijSHmlyBxanzmPOfGfzBF1Hb7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
بعداز 12 سیو بالاخره‌مارتینز تسلیم‌شد؛ گل اول اسپانیا به آرژانتین توسط فران تورس در دقیقه 108
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/26104" target="_blank">📅 01:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26103">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b656d9cc6.mp4?token=Us60GAcr5c8KClVLZ1kS9xF6bxfgjOXvGYqqY6O1uQuub1W06_xQrYzwszgKt30GhcyCwHNmkAR8O460HdsfYuDQGjkquyFlWFK7VtaNL_FcvFPGRZXNE3wcdfIzKs3Hx_pe94koqRMXbCicI4N7dX7TysMv6mZnfLfpiS9PWvk9ITcP0Q2wePi24AGc3uC0hj1bXVmaheNhHUQw35109vE3N3tDGP_13Rq539_3yMLeRKSfFMpzlWuTuM0RV2dMGMrZhfxF2wluLzdmhcEHYMGdTMBPhWm5lxyZygvt97o6keHKSDiqBq4aj-hPyUcnzaoHXoIoSRClII23ltuNXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b656d9cc6.mp4?token=Us60GAcr5c8KClVLZ1kS9xF6bxfgjOXvGYqqY6O1uQuub1W06_xQrYzwszgKt30GhcyCwHNmkAR8O460HdsfYuDQGjkquyFlWFK7VtaNL_FcvFPGRZXNE3wcdfIzKs3Hx_pe94koqRMXbCicI4N7dX7TysMv6mZnfLfpiS9PWvk9ITcP0Q2wePi24AGc3uC0hj1bXVmaheNhHUQw35109vE3N3tDGP_13Rq539_3yMLeRKSfFMpzlWuTuM0RV2dMGMrZhfxF2wluLzdmhcEHYMGdTMBPhWm5lxyZygvt97o6keHKSDiqBq4aj-hPyUcnzaoHXoIoSRClII23ltuNXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
فینال جام جهانی 2026؛ شماتیک ترکیب دوتیم ملی اسپانیا
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/26103" target="_blank">📅 01:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26102">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIRyNlyW5jVoCZjlperteZ5vQtrKZeXlUgd4E89n5nGN1hy_14a6iIGARYmlpWm16Uc4Cd1lWeR0O2PLUad_-ZNI9a7UONeUD9vSV_QjVhlZ_J_M1kwGt2fv-cGOmZcNyzsevwFQIArmEU4p_RCSNr_iu1uRTkGsvLP7wLhr1-vlKtAM6o5itcnnLGfJMumHb3C4QL3FE5WT-CrxyUPOuD9b7W_fizlHm3S0cuZqEVL73lrlyqHQwzzHoIxsrXCy0qh44m5WrPK2Sj4XyuyH5ERS6TQrtCmefC5I6epxYrewGAnf4aXZVPr1lb6r1lFYCUU9YT1EhiwRIBLXTifsFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
ارزانترین بلیط برای فینال جام جهانی ۴۴۵۱ دلار و گرانترین آن ۱۸۸,۸۰۳ دلار قیمت خورده است. به‌عبارتی ارزانترین : ۸۴۱ میلیون تومان و گرانترین: ۳۵ میلیارد تومان و ۶۸۳ میلیون تومان ناقابل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/26102" target="_blank">📅 00:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26100">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FAPlaHAXf0uL8PYhJO5OI-OMP6e_C9RdUz_hwxAQJsl0TlchhmBOgeEEocoxAG_CILs9z4r55yo8vAadM0ubNsOVudsKcuQkcftQMtGGer2RnUHJ66EIvWqfiDpqZMsr3gmxw68jxLQVohKM7IEgFAb5jLab7INXli4SPeutbhAXo_1y93NHQ77F2tPqhCWZLNJ-uL1C1JPjuc5J-99vquXwFz58mzhhHjb22AFdGIQ41_hpZ9ugyeEwAvrOUzyDsaKouYu1IaWkqgIx9VAoGjsh3rG8eoV2GkQyNDZjve6om-OUxkvPQ3iC-u-PGGziPr5NZClppq_vU_dm5G7HCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qTVHfeQU91BBJ-hpb5UUcf4UGzK2U97FOHOxHGQIpyi2BoUNSAxiIKEdfPK2bKqqzg6FVHRF8rsPBhBhBGetbcEz3AWe-mW4xKkw8x9_EhutcWTWkaaZA9wIDeQfycha1m2wrzGBvrPGDlWFHmukpVgV6d6iz6_RA_LcnVegBLsZLsWG-77ypKYTJt0lQTe3xjtBFZ2thxYr2EudWvi3UpZiVwMknAxGegDK5QWfoPY0fYGCT64T7UGMgpX4Ep12Pb8z4bbQLqPQFpMQoQ3o1piuCzdc7q5ZPKvl-fDxk4atNfNDGq75wHAqiPo4plGzTcnnlamAjML82cFgyfgdUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
ملکهٔ آیندهٔ کشور اسپانیا به‌تازگی به‌ طور رسمی سه‌سال‌آموزش‌نظامی خود را به پایان رسانده است؛ ازش پرسیدن هنوزهم به گاوی فکر میکنی؟ خندیده گفته دیگه نمیخوام راجب این موضوع حرف بزنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/26100" target="_blank">📅 00:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26098">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/inbzWN10piw7cJhrSuzRaLqNykznoXnC04zs1byPHgU7VWiTYnRl_WIaHNj8uijE8LOBA1vhLSvZx1n93iyWFbaHNiSNvJclGz2z4sHBqiBYOfUJVj0ZpPj2hPKMire6AilIELP0mYPZkIoYWC6ORgQXHRK6sbkMGXsKxidaOvy7dTr9P6-DxJ1u6FtX5-8LQGRlxH5zFsYIzkOKk__vW6OZXD-iPrRjygA91X2whcvhZ-bJqYRMDyPRdQJXz0W7AcDTTd2pMVrM4NGj5vQx7ViHPPl2UhiHjDRKyTTfEyPVSZiMmYKp4QUgc-oWSG_iJT7keh-0QbGIgKWi4B9ipg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cz7pFz3l6DhYBS6e3oOVbP43fB-aTbC3m_MYjai3LrZLIBWx7fdIoG9K6h6a-3NzYhk5S6Ea_x54ObhRw5-fX0LyOPhfMD4lmm8noXfV7htblRmlrvMSxDqoNgiVRQrba6rD_XEbjZoLaCTqqjZ-mQa7yEGY5ZZ18cyc9W_GB8acYokbMIbwCqPqsliXOuW2q0g8jV0pj3Mbipd8cEFa3kqQJ28SNzxYg9WOy2AUtLDlx9St3M7prbbu5Jmnf4vdeHJdb-ohxRFAwOC4zS-bgZ8lRzDYDQ04uX3cnyHjqbnsVO_xNnSswOy7eA05zngdrMv3TghfVi6kl70xv5zMkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
ویدیو کامل اجرای بین دو نیم فینال جام جهانی با حضور شکیرا و بیژن مرتضوی؛ عالی بود ببینید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/26098" target="_blank">📅 00:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26097">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🏆
لحظاتی کوتاه و جذاب از اجرای امشب شکیرا خواننده کلمبیایی درمراسم بین‌دونیمه بازی فینال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/26097" target="_blank">📅 23:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26096">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6a67771f7.mp4?token=bAQNUQnjuLBVy6lV2aP0luPgvMNzJxE6QP-B42bnnAOf8o5eWHENFk4TCSLneADaxdC1CYQruha1QYvE5LypPXfyAWiHqLRyV5kqzv8efclYP6_j_48D4teaMkD2EKJqKcsig5yN326skkJRq0WFd0Y1TgNF0akuen-2ELtfZnEXDxVE9mv89sKMNkKFGvcg5KHa85h2IXybuwinr8-YQaDHIh9Q43t6nGUmP8NKQDp88sO0PkalWhHvaX3Kqdohc7cAd4luc8Qx5rJXPr2P8dhETOgOf4YEeHGSOUVaN0OphNaQWy9aXn-5rZOY09ZKwTVPEYbTkdR9x8ndbIhyrbg4mXuLNs0CI5y-5m9_Xv24z3WRkWa7AdFDwuVghWnPOyQYU0OwhCcMqu3O_JeMcTN6tn90ivzrmZ4g6724XUbsyFyecwCwfOT8ExWgwtZ3nDfH7iETC7fW4BB8DC9sh0eAlR9zNJrqIuH-ClHp4F55mf652Ex88maRE6UNgc4ZLvqsxQssfy0QCvLL1vMZ45AXIRcNtwCg3ESAt7FVd0fmb14rqzUAdXf2YnCvZ_3KkQ9FxkEg9F1uOnZce6Dzag6Vf3gRZw87E4QHtfua12anvQ1EDKGUrWxr32DYud5orDIKSx8oBrhvru9ufF8WOBNsqN8UGlvddmIcYTonVLk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6a67771f7.mp4?token=bAQNUQnjuLBVy6lV2aP0luPgvMNzJxE6QP-B42bnnAOf8o5eWHENFk4TCSLneADaxdC1CYQruha1QYvE5LypPXfyAWiHqLRyV5kqzv8efclYP6_j_48D4teaMkD2EKJqKcsig5yN326skkJRq0WFd0Y1TgNF0akuen-2ELtfZnEXDxVE9mv89sKMNkKFGvcg5KHa85h2IXybuwinr8-YQaDHIh9Q43t6nGUmP8NKQDp88sO0PkalWhHvaX3Kqdohc7cAd4luc8Qx5rJXPr2P8dhETOgOf4YEeHGSOUVaN0OphNaQWy9aXn-5rZOY09ZKwTVPEYbTkdR9x8ndbIhyrbg4mXuLNs0CI5y-5m9_Xv24z3WRkWa7AdFDwuVghWnPOyQYU0OwhCcMqu3O_JeMcTN6tn90ivzrmZ4g6724XUbsyFyecwCwfOT8ExWgwtZ3nDfH7iETC7fW4BB8DC9sh0eAlR9zNJrqIuH-ClHp4F55mf652Ex88maRE6UNgc4ZLvqsxQssfy0QCvLL1vMZ45AXIRcNtwCg3ESAt7FVd0fmb14rqzUAdXf2YnCvZ_3KkQ9FxkEg9F1uOnZce6Dzag6Vf3gRZw87E4QHtfua12anvQ1EDKGUrWxr32DYud5orDIKSx8oBrhvru9ufF8WOBNsqN8UGlvddmIcYTonVLk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
این هم ویدیو زیبا اجرای بیژن مرتضوی افتخار ایرانی ها در بین دو نیمه فینال جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/26096" target="_blank">📅 23:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26095">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb8fe73d8b.mp4?token=QlSBgiPtU92NCcVL90yzPDQ52GXCg-ttext8NylfmQF3vWdPER6HEJyYFL0IAZMfHcOdo_a4-rDbKRZ7bQS25ykeQCqe7rx6DGO0lAqAdppabYVoiwztQB7MpLqFygdh_ka4B5bjX6dft1Py9GyOJvVPOZ05KgQhFZQKPl6hv3tgn-NSQDKQl3X8VzesUgpFx4i83E0tvsoR029LLNNipXeO2G5Al6CNzSV59uNQnXOifctwwyVX3QjqcmK_7esFlmVn6ZJ-W-R495VDW0V08YkCaWdmgnKaDQh6MTCOPumdy7rgdftkSozwviNaAkbQEKb_qn__FywPGQRH73bWbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb8fe73d8b.mp4?token=QlSBgiPtU92NCcVL90yzPDQ52GXCg-ttext8NylfmQF3vWdPER6HEJyYFL0IAZMfHcOdo_a4-rDbKRZ7bQS25ykeQCqe7rx6DGO0lAqAdppabYVoiwztQB7MpLqFygdh_ka4B5bjX6dft1Py9GyOJvVPOZ05KgQhFZQKPl6hv3tgn-NSQDKQl3X8VzesUgpFx4i83E0tvsoR029LLNNipXeO2G5Al6CNzSV59uNQnXOifctwwyVX3QjqcmK_7esFlmVn6ZJ-W-R495VDW0V08YkCaWdmgnKaDQh6MTCOPumdy7rgdftkSozwviNaAkbQEKb_qn__FywPGQRH73bWbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اجرای شکیرا همین الان شروع شد؛ بزنید شبکه پرشیانا اسپورت نگاه کنید. ویدیو کامل مراسم براتون میزاریم که ببینید. نمیزاریم چیزی از دستتون بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/26095" target="_blank">📅 23:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26094">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzHD5oixVopHS8zyFwwsPlnEPIYdEk22jV5KIY90ZQGi-GySY53HJdqfonYKPltJwZcsBhq6kEaz784DgHJraXuw0-0w8T_1WaBmqEZ7myukX1vQ4NLoNLOHv6A3Of62kJwonSVrRFZpHPj2WZ-EGpsEdfEF0EsQ6feCqUQLKIVFcnj3uOdRa8hpUox64oRMv8Obe76OnLkuIcasMZdgIVpwLDXti_C9nG1gh-liOPJI4Tb3zRCBJWo_x56OYLYK-x-Su8-vkFCM2ekw6tZOB9_rDCHUbVQN7zV7abadxNvrEvPTZ0fGorlD5uJyinRwXz-A9CYD4h6MEO-NrGpupQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
خب‌تادقایقی‌دیگه؛عمو بیژن‌وشکیرا خانوم میان وسط برامون برنامه اجاره میکنند حدود نیم ساعت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/26094" target="_blank">📅 23:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26093">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2daebffff4.mp4?token=JCMbCTZRlqyTP8wArZVl_YbdRfferL4oLNRHRO6dAhQYMBmo6Adst9GD0mtCTkpmZnpKjW9llw2v7Cs_AQpbZ1B5_6m_tHOAaotKgNC1qN9SVhgNIwIvB0vzhf2lMnTS6Z30A_es-uq-5W7FkTAi43HhVQQC7E8Y0VeRG7zyy00dtevtLA50Soe7B6to61cRi1QEbXgd77HQ3ggXjimrnOgEtJsoNnAUr2VEF2NpY8FEFzgure41ZhTA_rq8MYdBYitF-ovubZYhCvNa--DFCk6KXqNX2hUvg1D9uzWi0LJXpBzbePeUEnBVhs_dtQUkwG6bA8Nm1Hd9rzRIhMNbHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2daebffff4.mp4?token=JCMbCTZRlqyTP8wArZVl_YbdRfferL4oLNRHRO6dAhQYMBmo6Adst9GD0mtCTkpmZnpKjW9llw2v7Cs_AQpbZ1B5_6m_tHOAaotKgNC1qN9SVhgNIwIvB0vzhf2lMnTS6Z30A_es-uq-5W7FkTAi43HhVQQC7E8Y0VeRG7zyy00dtevtLA50Soe7B6to61cRi1QEbXgd77HQ3ggXjimrnOgEtJsoNnAUr2VEF2NpY8FEFzgure41ZhTA_rq8MYdBYitF-ovubZYhCvNa--DFCk6KXqNX2hUvg1D9uzWi0LJXpBzbePeUEnBVhs_dtQUkwG6bA8Nm1Hd9rzRIhMNbHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
خب‌تادقایقی‌دیگه؛
عمو بیژن‌وشکیرا خانوم میان وسط برامون برنامه اجاره میکنند حدود نیم ساعت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26093" target="_blank">📅 23:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26092">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szPrOD0T8u_9aDgfagU83ncJ3PBBQrkSNjJaXdlCOgY4Q2TMCYklRbjGm_V7cmPw1rOWxUd-pHKrHB9fYy-mIZZF6WaHavqnne1KCd2Sd8Y0cf41r6v8cpeIys3SXiGCiMYjnysmdZ2rdPcz6gUBfs14GK7LU7VVqbVNKuDGg4kuI2y0j1Fkmr0kfQ3EV5Sj-EKgaHZ1kd2KdzxcdwSptY0w9IgkR7eRu_6nSiOarfoSnrIWEH8M--0cHOO-xLwZGPL9kpabUPex6R_BBAOW9qwc1r-3iVPPTzO1_HpYONtaFgigCWBTL0ePKA8t2YCKqiApFkegUtujP_qFW7Z3VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تقابل لئو مسی
🆚
لامین یامال بعد از 19 سال؛ لیونل مسی: چقدر بزرگ شدی بچه جون! انگار همین پارسال بود که داشتم تو حموم باسن‌تو میشستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/26092" target="_blank">📅 23:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26091">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPnmAQP3ciK7N7_0Q6cPBcyrSu_B3r0jVKjoF5H1-cltvI88zcvtxm_BiKFRCxX9qxWGJndIeKTuLUcX2uINk4uhMmNuEGY-Y0Me-t6CCQ-8z3ITMe9fud1-2j9LchQTHS5BkW1t3tQ0-ZyZjE8_rcWbUr5I_Lwcm-iy1KgTK7V60CBmpjJjOaLt2NJaJIeb4LalDnVDrTlggvO3QSKkH48ER0HfgnybuAiR9VInaFS7clILkHGGLXP-jWHgUDmx0uYOH3rZE_bripDh34QE5IQ7lUoaelDsmJsAGqMkOGi_Jcn-NbUz8WhBCUCLECS0QOjUn7CMb4bz5x0PJaUUKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
الان‌فهمیدم CR7 چرا انقدر بچه‌داره؛ جورجینا: من آرژانتینی هستم و تو کل زندگیم طرفدار تیم ملی کشورم بودم و امیدوارم‌امشب آرژانتین قهرمان بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/26091" target="_blank">📅 23:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26090">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🏆
روایت‌جالب فیروز کریمی در ویژه برنامه امشب جام‌جهانی‌از غش کردن معروفش کنار زمین مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/26090" target="_blank">📅 22:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26089">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de9d2fca55.mp4?token=Zitqd-A_1_SRuuICznJ36l2fFyY3snKaIBVIkw1PmT_FnMAYoTnAIuPP9SpDRyD29nDtE9gtjZATgwKfXZds-B2GX5OV9WeLWJkEgci-FebxHUfkgMEznljxq_xXutfiHx34xBpgUqVUquM_4aLxhLqfEkKCmZLJ5BAuQC6QrAKw2I7h8Qpj4MsZXvDQBKfpIXakj-od7U_NxvA6ZmE_yQh3t7ZnevE_q8TjmXNBCHL-8qsW9EYEQYzxf6kbXYj4keSB3gZu8J6yh8cem2J0Uyy-K0Ss34tfF0o_lBa1JyWGdBW2G6XVvcUAXdSBsAmyGEyoPsw6TS0bXkhWX7DZVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de9d2fca55.mp4?token=Zitqd-A_1_SRuuICznJ36l2fFyY3snKaIBVIkw1PmT_FnMAYoTnAIuPP9SpDRyD29nDtE9gtjZATgwKfXZds-B2GX5OV9WeLWJkEgci-FebxHUfkgMEznljxq_xXutfiHx34xBpgUqVUquM_4aLxhLqfEkKCmZLJ5BAuQC6QrAKw2I7h8Qpj4MsZXvDQBKfpIXakj-od7U_NxvA6ZmE_yQh3t7ZnevE_q8TjmXNBCHL-8qsW9EYEQYzxf6kbXYj4keSB3gZu8J6yh8cem2J0Uyy-K0Ss34tfF0o_lBa1JyWGdBW2G6XVvcUAXdSBsAmyGEyoPsw6TS0bXkhWX7DZVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو ویژه برنامه جام جهانی یه هدیه به ایمان صفا میدن که میگن این هدیه کوچیک برای شما! بعد صفا میگه این اصلا ک چیک نیس چرا اعتماد به نفس ما پسرا رومیاری‌پایین. جفت مجریان‌برگاشون میریزن میفهمن منظورصفا چی‌بودمیگه‌تموم‌کنین‌برنامه رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/26089" target="_blank">📅 22:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26088">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKJs-7r01KlvrAGxkSTOxmyX5DJr3SJ44J85FLeBv2h88RoW01y097dbtRgHuBtunNA2_QT4cPQWb7KcnpN0G-_OYNUl_z5ePkiPR5PWd9U5VClHneWMexEj8eRyTcNBQ4N6K4u3kdJ2NYlwyu83BA7kOc9YOZxKKGNhP4IX5PmbDUtfw4pChAceUVT4isBmfNvpaE1XmX0iUn697FMDCihvUrZI-b22tYTC2BT4vBHvWrYJFpdgbVHt9wYVsby4mxiGHXIjKR93HTdAdWUf05u79k0Vqm3IxVxx7zha5VrowEc9lXIPXIcns1RnGRHRftN0lOd2E5JReUQcI76vpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابوالفضل رزاپور درصورت جدایی میلاد محمدی.</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26088" target="_blank">📅 22:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26086">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68101d4663.mp4?token=La6mWio02BAwqG589YjMS_QQM2gQ7XOT2GCR7jYchUB5LFeYifCbHBDrK6T343PzP2E04YzlFCd3opOEF_AE3NU8xFzfi08GvpVG_an34I9FUqtcC7LQm__R_NZSlZ6vMc8G3diumD3vRP7FTeyz2bRhVo1ijZbJrLR2j4wmEaPAimXoq_q-8TWUk3WhMyNJLwPv5CnWqGfpzyfYSBY2LqxzCaK98xt1LJc_24i8utFHVmbUlZyz_rCZihRpxgHbMebnkC85BWXmx2aYGYyEpiWmtPTH1DLm-Yr-PsgcU99f4tzZ_-MQG2o1mOZ3YCFLs2f27W0p1lOrifD6RVHutw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68101d4663.mp4?token=La6mWio02BAwqG589YjMS_QQM2gQ7XOT2GCR7jYchUB5LFeYifCbHBDrK6T343PzP2E04YzlFCd3opOEF_AE3NU8xFzfi08GvpVG_an34I9FUqtcC7LQm__R_NZSlZ6vMc8G3diumD3vRP7FTeyz2bRhVo1ijZbJrLR2j4wmEaPAimXoq_q-8TWUk3WhMyNJLwPv5CnWqGfpzyfYSBY2LqxzCaK98xt1LJc_24i8utFHVmbUlZyz_rCZihRpxgHbMebnkC85BWXmx2aYGYyEpiWmtPTH1DLm-Yr-PsgcU99f4tzZ_-MQG2o1mOZ3YCFLs2f27W0p1lOrifD6RVHutw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
عادل‌فردوسی‌پور: سعی کردم تیم ملی رو خیلی منصفانه نقد کنم امااین‌حرف‌که هر کی نقد کنه وطن فروشه نمیره تو کتم هر کاری میخواین بکنید. وقتی اینترنت بین الملل نیست من چجوری میتونم برنامه بسازم. عادل از اوردن اسم قلعه نویی خوداری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26086" target="_blank">📅 21:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26085">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9df505731d.mp4?token=aEnJUnBFH761NXbXvkRqqqWdK4EWQQHs3v8r0cfHHKR5Q8CqJ3JBsT79wJSbo_L3Zpf4TKt0ftSMQBSSYpnmfupAMXgaQC2q1qI6LrB2GyoYF0Ipqj2mjSOGdTE-NVWT5A8pMlnmsElVMNx0shzs3nDmfQqAN1hXWGr52egZxaJBAFn4uiLh8xOM1kBUMRfMhoy6Tfj10fUequPuSbvmW0hpCXtkTZAhnMcSmmYKmrZhtNqTfDue7kmNOZw1Yghg1CeJE-gEymU0KIjDfqw9axe6P_QihxtOUwwFHsYQQ8XEo-GZoidYOrM55SfopXELBVN8g2SSEL0tJO0drL62bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9df505731d.mp4?token=aEnJUnBFH761NXbXvkRqqqWdK4EWQQHs3v8r0cfHHKR5Q8CqJ3JBsT79wJSbo_L3Zpf4TKt0ftSMQBSSYpnmfupAMXgaQC2q1qI6LrB2GyoYF0Ipqj2mjSOGdTE-NVWT5A8pMlnmsElVMNx0shzs3nDmfQqAN1hXWGr52egZxaJBAFn4uiLh8xOM1kBUMRfMhoy6Tfj10fUequPuSbvmW0hpCXtkTZAhnMcSmmYKmrZhtNqTfDue7kmNOZw1Yghg1CeJE-gEymU0KIjDfqw9axe6P_QihxtOUwwFHsYQQ8XEo-GZoidYOrM55SfopXELBVN8g2SSEL0tJO0drL62bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی تو این دو ویدیو به بد ترین شکل ممکن‌جواب‌صحبت‌های‌قلعه‌نویی رو داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/26085" target="_blank">📅 21:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26084">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtlGJ6sYbcwy2IZSlFP0_Sa3G14EW9M-TLz5KAY-VY8vUXhAni3wLy1Bzlcqbh9MlUzdBVwZbYDMtzftNhUzi3Z4mAomlwD8IMS9Q7gNsaB33BSg770ByGtPRMPLk-qxA16cqZOAgxOkmCigDLpTiWF-MalJ39whYYPKSXdDUXWTwBa8v6gmn-SVOOc0sWcQR9bDiwTj4NsgsBgDyj_FY-MUMp0kXT6OyEl8B-pijLWi22injVmhkhFCnrAZmc1EGBQGuRdDRERrZ7Sz2hwszLjJIeMchXaL197qXZQUW8yD1pdidfkHsTPIXv-9FFBAEmHW5xWxYnCxYZXaIDZTMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌بین دو‌نیمه فینال: بیژن ویالون بزنه شکیرا شیک، کی میخواد جلو این ترکیبو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/26084" target="_blank">📅 21:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26083">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60f87ee3ff.mp4?token=rhElHcLuxL7DhenV8A9x8UIwKR3Rmb_uQeC09_WaMyurxh0dkeKkvrR2sU1xy-niKz2tLlOIE9bID3KhHbBoRRRlth6qwdhI4DdF9Y8pDKXhqpCTO7KIdzCcbfCRE4FlkVDvaI2JASA61xv9Ecfq4t857w7m6Wp7afsbhT1PzJTnP5ivHQ2s_q-rOqngF3efqhAoOM5LxCP9FCcrlk4wnpP43e_X6c7WW40FVA5adK_nIgwdXVQ2kEjk_ad7XRBNVz0sTjk6kehXMA9j4zObWlrTlwIEezsIuIEQSdzGx8-G94YC_5HuTz03_-hDVKRIAfx4wweiVceL-EfD3vQByw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60f87ee3ff.mp4?token=rhElHcLuxL7DhenV8A9x8UIwKR3Rmb_uQeC09_WaMyurxh0dkeKkvrR2sU1xy-niKz2tLlOIE9bID3KhHbBoRRRlth6qwdhI4DdF9Y8pDKXhqpCTO7KIdzCcbfCRE4FlkVDvaI2JASA61xv9Ecfq4t857w7m6Wp7afsbhT1PzJTnP5ivHQ2s_q-rOqngF3efqhAoOM5LxCP9FCcrlk4wnpP43e_X6c7WW40FVA5adK_nIgwdXVQ2kEjk_ad7XRBNVz0sTjk6kehXMA9j4zObWlrTlwIEezsIuIEQSdzGx8-G94YC_5HuTz03_-hDVKRIAfx4wweiVceL-EfD3vQByw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو ویژه برنامه جام جهانی یه هدیه به ایمان صفا میدن که میگن این هدیه کوچیک برای شما! بعد صفا میگه این اصلا ک چیک نیس چرا اعتماد به نفس ما پسرا رومیاری‌پایین. جفت مجریان‌برگاشون میریزن میفهمن منظورصفا چی‌بودمیگه‌تموم‌کنین‌برنامه رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26083" target="_blank">📅 21:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26081">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
کنایه‌قلعه‌نویی‌به‌علی‌دایی: ساعت‌بستن و کت و شلوار پوشیدن نشانه شخصیت منه. اگر لباس یقه باز بپوشم و زنجیر طلا بیندازم میشوم مربی خوب؟!
‼️
همچنین قلعه نویی از مسئولان جمهوری اسلامی خواسته که مانع پخش برنامه عادل شود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26081" target="_blank">📅 20:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26079">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/raJj2Ybsgq4WXyzIgXdDmFtP-cxgDseucqv2vO7Sat7kXsLXecHuiiWjE89EVBupNtxOrqODPYMZUBRrCnZASmoejLVx4opOhrg7SP8pbCblvWH8eU3gRKxdLv0A6wtwhczV9axOCXHuthM8Hi5N9fSrVQLm614q6PzKzGTLotFXaxAiK-yEzo4cmqvpYuVLDKwDaghkPQJDRKsH1g8hsUyksm_Nv0IDlb-iftCpo7wUYYN_tii5FtXOpHa4KwGFcEOotPNy4RJ6trNnuGUL8fzKYWlH4kvzH6X6c8OVLTTafToXI-7LHs57ZALtzd1yIhwffI7m9l6qwR55-siyDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RxTbk5phgkKuEe5NfvQn8rTEcHoq_aOH63U-mBIKLKc5ASq_eG83Mg990HalaBpdQDPT9u2UfqO8VkLrpCvkAVxebxY2Y0jYfBsjyBsh2VLyRqNTqpqjkjIrPyJspr3oM9qJM_gYGJ0omJb5uJhqxWJ2gsvm2_WJRS51DgaURstCd4V8PNzKrssu9eW9n3cs11c1hM8Uq41BCTil0mVk85jMC9Uzi_LYGnQyPnq4C0sa_6BzDGHzZCQWi-Q0cJOEnLXre7jbiaiowNpeDFOFLNggX67tX63UY7nvigw8YsgURcAmy70nfN_7uiH-vG5eIFVkBuFxUZP_Woe5Ojer7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
فینال جام جهانی 2026
؛ شماتیک ترکیب دوتیم ملی اسپانیا
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26079" target="_blank">📅 20:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26078">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JD20SkSyJg2leXlwwJacCsMIQ1i99BC_rFITf4UPw4UI8MaquWe3ERWUG48EPf9WBcMuuodE3H4lhkzLUKaGLUpesLQFCnMXoDbS6im_sEBskY4hqqF4hN9POKRW1v6smIBBZvDN0p5kbUHL7O6sGFEVxumvL-bNY_6v5sEVNZdY2fdtOHDrh4ZHTfynUh_6F2QgPvC2l08tLSfrzqMC1YaxWeG4jwt3pFwXov7wbeWLlXeDA7ahOnvuIKNFuzdQzvPlyZcHI1IzGq1SdWhIWXADFjDuLduTphrvwK3KSU6YxqZNgW3zb5UbYHVRDsNYzDGwdaB40O4MV0BHEN2fTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/26078" target="_blank">📅 20:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26077">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bg7PEXX_ZrJaypCYoYCHP-lSfezEnHk3Bffrg4MS6EDxPIaujAwmCNwNWUpY_SgPZeV6xpjqxCx4Rs3jdQOPRQqhlFOoPqbn3AcydhTcIZVt1QbKsjFy0h-YOjESoaxHVlidnApmhZRJ4nC6DmF4sn71Hf0SwCPV_c1CSETPnT-AcTQzZbrIxgoOKbYeqRP3qInyBCmTLsXLqasZfTMsKqlA1IMBlWb38oAeSNGqdTmBsQ0pdLzb29VLKeRteG6M-25tyYv9Kd8n8GlNMcVju3Pi3iFQZ3ao_4Qq82ySQrWtMKhCFLbN1f0bUiViX2DMaJtwUR3g30wwttgmAakwvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/26077" target="_blank">📅 20:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26076">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POQm9QPfpbbS205KeGYaaWWWS1KthXTF1y6Hnn7CBK6bZaF_h8di-8YHlKwVk-e8KQkTgZVRIXwkp-5-S-MSR6WgI1xj0wu-BU6W5pR9RogOMFjjIxHFh0nEFTf6ypvTbSlOuAoeT37CRJiqKwiqv4XodEDbn9ETYFH7KXDjwY8CbrH8_NrEow1pVRlC6M2e33VmEWb3iAq8wLdHUEl8Lz25Ll-FnFnWDNX5QDfcHEWxg2nT0T0uxtb4Fo-Ul6p82qf7HzeES0Pu69EE5GTjHE8MAVOi2y8F-KEqg7vv7gTlZqlvNcUEACU9MIWAsqv-JF6YamUgPod85RWuG4JPKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
خداداد عزیزی سرپرست باشگاه تراکتور: تراکتور بزوی پنج خرید بسیار بزرگ خواهد داشت. 3 تا از این 5 بازیکن لژیونر هستند و سابق بازی در دوتیم‌ پرسپولیس و استقلال روکارنامه خود دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26076" target="_blank">📅 20:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26075">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgovSGY3DeSwudwmW4YbLwunmgrcMS-JLVxtiHTzdBhHiNjyWsKGW21sYAi_igN1CZjCTYFcIXNuze0ASxolNU_zjx8AVsfWY0dfMQoStn4IldGj3Ij3FDyed1J9Qgvj3WJHI7mLtmrhpPuRAB7foOmaacyvuIIX9SGQp0veCbtt2KvcnwW-QVHCBpr_9FVclpFk7WpaEYkKMcEFcoFOcW92lrIT3cJ3UGORrxHHRYrlzXlsuBUBSi28joje8K83biZZnR-yGdk6I9SPmk-fiXduQs9YCH5KTTGCtlhDVEhuOxpRrLv3u6CpnD8xzO0P9_Vk3dQ_6TY5q8LY6V5O8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یادی کنیم از دست دادن فرصت طلایی توسط گاوی؛ سه سال پیش شاهزاده اسپانیا لئونور ۱۷ ساله به بازیکن جوان‌تیم‌بارسلونا «گاوی» علاقه‌مند شد به طوری‌که همه عکس‌های گاوی رو داخل پیج اینستا و توییتر خودش پست‌کرد و ابراز علاقه نشون داد؛ بعد مدت‌ها به گاوی پیشنهادداد…</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/26075" target="_blank">📅 19:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26074">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JM4vDX8urKTW9K-Q2QEB6hlBwHuUNDkJds66FlSDptaBgcIVjTXIRBrCfvH2DKpMe2mkxGZxV7Ghw4olz7MEyMjib5JAuvaalNs5bQuJm8mzdflkMWw5gLdUSlrs10SZerA-iSfMZZRVc1eda-vkon-2G6SRW0W5W2rUeAmqLv6C89397wo7hA6ZV5TDhB0O5SVLLsozv5eiR0jLorDhMISr1uiuSWHLMKR5OAIRkcAbImWhR8k35OCfxqzFmyCQNr-jdurT1bxa3r05FkwI3LBCleMckcM_9OCyAv7QFVCtq6E7yCfssSBui006gZeoFx7o3f1yzX5c9yFdVlN1fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
علی دایی بهترین میانگین گل ملی در مقایسه با کریس‌رونالدو و لیونل‌مسی دو اسطوره فوتبال دنیا؛ بعضی رکوردها شکسته میشوند، اما بعضی از نام‌ها برای همیشه در تاریخ بشر به نیکی می‌مانند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/26074" target="_blank">📅 19:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26072">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzQsEDzodLz3oDATD794Slevp8cpG1jtJN4YKlvBafKLYXn-hJT9HSoB1wTlQTrOlNlt3gbENub4HghjSXF-8NkTwdS3P1pDX1j1Az8zhvMph5MUdT3QZFPjdoyl82VRbK2Jx_vmlFIBXmpmAvW7D_99anf0UMumkUkMt-_Nrpbk1XvwU6Q-xHsIu0GcUAuwgl4o5wtxnGcIieuk7oIN7-ntyXRtdrCb90s0VORSEKRjcszodo3zEi3Gy-iwtXe3n2yMUwL3Xz-SnqJLPwhVA55ruw8Pxxzk-1YnUxG7YqsQZcwKubFSXZW4a7cPmyj4EHcNrSGcyrekSm_3ZXwQxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مزدک میرزایی:
عوامل‌شبکه ایران اینترننشنال در سه مقطع پیشنهادمالی‌بسیار بالایی به عادل فردوسی پور داد که‌به‌این‌شبکه ملحق بشه اما او هر سه بار این پیشنهادات رو رد کرد و اعلام‌کرد هرگز خاک ایران رو به خاطر رفاه و منافع خودش ترک نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/26072" target="_blank">📅 19:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26071">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQHRPz9-8VOtKHIHadWYGst-4aCkOQEKWh6f732ObCo2r3Xlmhk7zlJsOtTlcqYxw4FdNi1nFNVHbzbIgr7C02plNfXa9TtQQnGAdy33NMtIFrSdx_pn5ZhITUTVtRkdOJdeIOo02k3AHVveZqbfdpUQaMo01XOOefiY9py0_d1qc2obmqdUPKy4KxlM1PnjPlIjwdtTMOYwvaMSMdwPKzCPLSjcYJ3QeSw8D-Ty8UT8m3LHWQrhDgZicR5W5hoKO87Qg5OxpLAeUy7U6viNHA30GrUEmm4UCAeF2bp7g9MJ6weCrC_xWlNzsAEHei3TU9jq2YoJB_OvlxoBpXDMGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام دیشب نیم ساعت دنبال دوست دخترش گشت پیدا نکرد مورگان راجرز یهو اومد گف اوناهاش اونجا نشسته؛ فقط ذوقش رو ببینیند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/26071" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26069">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a250b46c.mp4?token=aNPEHzLkF7x3UYwKBp72kfukd8Lq57QF5FwEf2ZO3PKFjyXtmj7zUgrqEqbzsR_NtBMN-aYyKyKYSwfvrcV6KF_blh1eWvvwVUMuiOu4gJjStGd4Ppfi3rRQcAqdOkqxdnGY3MNXVR1oW91W4rrKPd52X-gQD-XjuSIicRj431oe9uFGsqaE7bZ7n-XBNxQKVCXa-MY9x2QZiG0-nSbcttDtsKWZdiI8iVhKE4PaDZ5omjA5otmlWvy29BpQ1qLAflyXD-dJc0ioZIY_-VsZri9e47g80lcou8WdnFwx4rzKJdd_eYpartK1omDLxrjyQ0nHwt4HwXWvQpMlhOvSrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a250b46c.mp4?token=aNPEHzLkF7x3UYwKBp72kfukd8Lq57QF5FwEf2ZO3PKFjyXtmj7zUgrqEqbzsR_NtBMN-aYyKyKYSwfvrcV6KF_blh1eWvvwVUMuiOu4gJjStGd4Ppfi3rRQcAqdOkqxdnGY3MNXVR1oW91W4rrKPd52X-gQD-XjuSIicRj431oe9uFGsqaE7bZ7n-XBNxQKVCXa-MY9x2QZiG0-nSbcttDtsKWZdiI8iVhKE4PaDZ5omjA5otmlWvy29BpQ1qLAflyXD-dJc0ioZIY_-VsZri9e47g80lcou8WdnFwx4rzKJdd_eYpartK1omDLxrjyQ0nHwt4HwXWvQpMlhOvSrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام دیشب نیم ساعت دنبال دوست دخترش گشت پیدا نکرد مورگان راجرز یهو اومد گف اوناهاش اونجا نشسته؛ فقط ذوقش رو ببینیند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26069" target="_blank">📅 18:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26068">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAmW4IrC9j2qdYZjWgWTvWY4fFVl5mNVQFB7m3MWr3-Z1yrKoqQrFAl5p8wkvOHv4BI3Qklk0Sb2S-1uzewFF14UHws76F60TI1kqjnCT0NuwGHgyFZov_v9Aktn4MUcY4gpgfJMLm_DeB-g-TZi-Ai_hLMrNoZl3qMq8LX9Q2u2uJWeox658RB4k8glj1lf9dgKyqU80IX8pCvGZVmmgGkHHJLfAJYeAW8Msv1EQeRqXvH-K8OX2N_5MpQaO9PBTHneDJsGX-2Z_kOYU8Q7PYb9iIOIN-TTVY2ONIkiUgonwg8wR3YclcGfhYW3GC_-57hrlqRxZiI6GTK6jc6vpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در دو جام جهانی گذشته؛ تیمی که در مرحله حذفی با نتیجه ۲ - ۱ انگلیسی‌ها رو شکست داده در نهایت درفینال‌باخته. این اتفاق برای کرواسی ۲۰۱۸ و فرانسه (۲۰۲۲) افتاد. در این جام جهانی، آرژانتین در نیمه‌نهایی انگلیس رو با نتیجه ۲-۱ شکست داد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26068" target="_blank">📅 18:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26067">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSht_-_SKFb1vExV57wCh38SeSLS5duuhFel6TW89Oa4-TUg44nQYvO_Hhn55SBBBTtii4DD-Xb7J2hAHDK43J2MNE69dlNOI2SajSweB1hS8rQZRH5RVNnq166vv4dWVYsMrdIYbtR1NzMHSA8STX7caN12rd8aWrGNPgKrk8zQSMs53xnOivOqOBtrONxRgoccA_C0yo8-d0TpFBDfVZCP0knCYWa6BKWqTbEAtEU6P1hWR2fqAyedQBrTR63Hd2aI2n6CZM5YVaYl82F2JOU0VJXGTtwn_1YZ8MEGx8NbnWsS50hGGIIgXIdbcj-42ZQtY8dUU9BeIYBQsseu8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد محمدی مدافع‌چپ‌فصل‌گذشته پرسپولیس باعدم تمدیدقراردادش با سرخ‌ها با عقد قراردادی یک و نیم ساله به مکس لاین ویتبسک بلاروس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26067" target="_blank">📅 18:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26066">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZgrOjxj3sZXl0KQ6_YrT0KOXun0hVLbRFX_0W_b7xE_uL5QQYY3WhwGAvG_9yeK8YuIeu5toXcOO1WniTI5KfnXUU6gEdU_9Y58AJevbc5GKUHu3Sb87WKhBjq0d7kUytTkUfwzJLgAgZOe5WDRFHS8g_gr-w1WCPwduIALTbbblBSnkZ4r30lhTDRjDfDpi5qYEah9LuBB9P5j-BY_3s2LGsWY6vg5ATjvYo7Rw4VzINVuj7LvWxYn-HDae2E-ulNOCQjjXX7W2YAbIETw0RIldvU08jCs3RXnjXlBNUf8QBttUXl-h-pb5qIToyBvFmmW5WYPnFHMoGevgdDYcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
طبق‌شنیده‌های‌پرشیانا؛ مهدی‌تارتار سرمربی تیم پرسپولیس از وضعیت فنی سیدابوالفضل جلالی مدافع‌چپ‌جدیدسرخ‌ها راضی نیست و به او گفته اگه عملکرد فنی‌اش بهتر نشود مجبور به فسخ قراردادش خواهند شد. تارتار نیم نگاهی به جذب مدافع چپ نیز داره. جلالی سه‌فصل قبل آقای…</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26066" target="_blank">📅 18:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26065">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33544e2a7b.mp4?token=HHDN2nDCc07f3sv0Df8yd0ei4TWeETHwOakZoiFdycD1J53kDn6vQw9EtguQRsKhRyfDj7OlGOzfh4Qye8LRgnAF5Bpe43_jKKYSQNAPpAT1ctB880hZ7PWBI1ragrzZMqJDLjRvywO81msfc0o5dgvyHB0vxwXyTYaT_UIuhY1Lt3I-6MN3MUcr0V8PcDoEDOLDJ8r4LR49Oz3SOuljc83LnzyaqOFla5LtBrn5eOuCjjmPw7O10fZpgnxLTg9SPSTYzPmXAtN_nBtAN1v6fiML6vMIpAwGgemzggHaVctU-ZX0t3mRecg0e8vYeg2iQ2wmgO3AmQBOPM9ygKbEmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33544e2a7b.mp4?token=HHDN2nDCc07f3sv0Df8yd0ei4TWeETHwOakZoiFdycD1J53kDn6vQw9EtguQRsKhRyfDj7OlGOzfh4Qye8LRgnAF5Bpe43_jKKYSQNAPpAT1ctB880hZ7PWBI1ragrzZMqJDLjRvywO81msfc0o5dgvyHB0vxwXyTYaT_UIuhY1Lt3I-6MN3MUcr0V8PcDoEDOLDJ8r4LR49Oz3SOuljc83LnzyaqOFla5LtBrn5eOuCjjmPw7O10fZpgnxLTg9SPSTYzPmXAtN_nBtAN1v6fiML6vMIpAwGgemzggHaVctU-ZX0t3mRecg0e8vYeg2iQ2wmgO3AmQBOPM9ygKbEmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمام امتحانات نهایی پایه‌های یازدهم و دوازدهم چهار استان هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، تاآروم‌شدن شرایط لغو و به تعویق افتاد. وضعیت دانش آموزای  بقیه استان های ایران:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26065" target="_blank">📅 17:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26064">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUQDesiA_f9-ELm5Bk0QJyu-ywszZj1jtdTAege9pm2lHknc_WYJGaXomyINsQWMJlAVop9eWU4zRT7eSazymPG5i-Soc58PLLDjyxkPBJy7NkMrAkzgnUKae9XckIy5x2MCibf4B2JprIkJTOVcpf4JkO2QOWoTIy8nGgFsiav7_zumFenDTt3KHznHnf_qnvFq4OgrMRyNIMnMD1pTsHYcoCpZbHJz08pFQxeLFqn-xEGRbHpPTVmwytdl_0Wad-S0fNxbbnCuOev7FEQVEFVhIpOvpnZHrbnFqxcjgqF8V5b8VL0DEcCF_wgWzaXS7NhuIaTMGmrdY5ZlfnNQDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ ملت‌ های والیبال مردان 2026؛ فقط یک ست خوب و دیگرهیچ؛ پایان‌تورنمنت برای شاگردان روبرتو پیاتزا ایتالیایی با یک شکست ناامیدکننده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26064" target="_blank">📅 17:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26063">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3d2e6f73c.mp4?token=OMcdkpeWiHbuNucTue6oPlsSN23QJcJN_5TwJWiY7QPSX11KxmtzluYfCwct63EhGcEcIk-n-5BOynhug7ZEgj6fXT1PXZNGGMYykvVhYZYXuCUziZK9NR5fmPFoRW4dT1NZDpnuYxUNWfOLLBv6x1BMgOaP3xtnhSXUriLA3jTXGT8ak5GjIAlIWT8JvXdS1t7drX3JLiLsZGVjbXetcmHK2PrOeejap1TIC10Fxs8Mg2qwCU2OhlFPlh7yfsYxHIrM4u-WEQktOphs324koqvSMTWMdbIjNVK10i6DaEaBDylFKJRE4Y4YsyGws29l4DFUtheDj3BGgiGPM1HQlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3d2e6f73c.mp4?token=OMcdkpeWiHbuNucTue6oPlsSN23QJcJN_5TwJWiY7QPSX11KxmtzluYfCwct63EhGcEcIk-n-5BOynhug7ZEgj6fXT1PXZNGGMYykvVhYZYXuCUziZK9NR5fmPFoRW4dT1NZDpnuYxUNWfOLLBv6x1BMgOaP3xtnhSXUriLA3jTXGT8ak5GjIAlIWT8JvXdS1t7drX3JLiLsZGVjbXetcmHK2PrOeejap1TIC10Fxs8Mg2qwCU2OhlFPlh7yfsYxHIrM4u-WEQktOphs324koqvSMTWMdbIjNVK10i6DaEaBDylFKJRE4Y4YsyGws29l4DFUtheDj3BGgiGPM1HQlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
مسی و آنتونلا ازکودکی‌و‌ازسال ۱۹۹۲ در روزاریو باهم آشنا شدن. بارفتن‌مسی‌به‌بارسا ازهم دور شدند، اما سال‌ها بعد دوباره به هم رسیدند و در سال ۲۰۰۹ رابطه‌شان را رسمی کردند. آن‌ها ۲۰۱۷ ازدواج کردند و امروز همراه سه فرزندشان، یکی از ماندگارترین داستان‌های عاشقانه دنیای فوتبال را رقم زده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26063" target="_blank">📅 16:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26062">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Is8lKjqcAoSLtz9s9Xsl2xHjCUZEb3mGqFl9RgduyFhVzMkqyHYJ1Vtarn7HHYIwd92j2CvEZH96_HFu5mtkgsDy07_AvP0ZFzEx0T1LOjWQBtOURDWUYouoJ1Av0Dmi16flvW8uPMIlJPUn5_Dl2gD1ddkXCdrZa7ML-5oF32feWi-ExmpI93_AW4QLNaWi2tAC0sM39qbpN1fUurFxZTWVFRuxZsLbo1uM6Rd2fFYFGuZJnm0_5wzclvI6ZbVBp4IyrVZbJTzAIYyGUpikSBu3l6-hgA9p0k6f6jHQteDdy_CU3IKPFJiTNmUz0N5vI-GXJQugVbC3ClMK4MieOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ ملت‌ های والیبال مردان 2026
؛ فقط یک ست خوب و دیگرهیچ؛ پایان‌تورنمنت برای شاگردان روبرتو پیاتزا ایتالیایی با یک شکست ناامیدکننده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26062" target="_blank">📅 16:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26061">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3LnA0zkbWrQ4y9qkk97rtmcTvKXqm3RsH-dmnxrSuZKcykysxFCOx7aVJNGnYamTDvwS-F-DafrhbSZmIQSivam-JXc1ydLJ7LrRZJXXoank6LO8VOWHGnjdtQ5NvKE_RFGJHUR1A3ARBR16_aZWORcsglczwkaHo9ez7Ihois5_IJAwh9T26h4IEBRZfETq_-7hvpw-MW1uZnYYNolwf7Kyl4NgvJ1YJHT9UuPigCJLdjv0yLoaozYwHt-VB3lH4-Cp4s8_AwZnS1MIINb_LEf4RYgQFJCByoQoKe5Dp8S182PiSV-J1y1XdwTYlZrUY-rzrvAD6r0z0TVxqgH5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق‌ اخبار دریافتی رسانه پرشیانا؛
به درخواست مهدی‌تارتار؛ مدیریت باشگاه پرسپولیس با 3 مربی‌ایتالیایی،اسپانیایی و ترکیه ای در حال انجام مذاکرات نهایی است تا یکی رو به عنوان دستیار اول تارتار در فصل جدید رقابت‌ها حضور داشته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26061" target="_blank">📅 16:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26060">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vs6q4FKo351n6dghJPTfkuA2CTFxBvahq_UbNwgDWdv6r_Ihx6Gk7xtnbdpP6u4nw1stD9s_lgit0ZF9Yv9675qSwlqizDtifKdIumUwcj4JWEJxb_Kolo7_RKjia-phT7IVdfe7wK3FYMda5UjGkRUHnMq-OfhTTDBYgZtzYo_VnaYHEBjyi9r_ZyoFM0Xg8rD9p_nyhnPBVgV1iZBjzwd6D-E0A6erUJX9P4XLr21O8TYlyCX6-_4futnmgg9_UjrueYCSxvaK1QMAVGh1MOCNJXmivFgO2JiTw7s6_uFEJqQnX1Kiio26Rflt4VxXmtAHAO8ul_f3qSRm8h955Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: وینیسیوس جونیور تصمیم نهایی خود را گرفته و اعلام کرده بعد از جام جهانی قراردادش رو تا سال 2030 با رئال تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26060" target="_blank">📅 16:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26059">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=XA3WvxcgKfZwlmXttAuICgH07chje1Ufk0sEWIYVU_qhA0zZE46Vc9YrjXZ0Jewgb8borySCuwCMFOahO8a4_j3VA0I89DjfID-mAxxIUSrLsht2lGVKyxhQQgxYbNRQeYvBGJy4i7HPdGxgIKngFKO3Tg3FhZnrAZnj5YgHW5i8CgH_n_r_KZUwunmhsxiEwZyGvWd8Ccw1jaNO9a8uKWtuMtVEVIi6HIXJY85cGPrYj2Y7AKUxAom6S1DwnvCcbOdoCokJ_pBjTUgOZIy02DFGb00tqZCDIKpdq09fWC0oWFGLN5BE4RF6PDx4HTstpK7QaQwd7OO7cLf9udXaSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=XA3WvxcgKfZwlmXttAuICgH07chje1Ufk0sEWIYVU_qhA0zZE46Vc9YrjXZ0Jewgb8borySCuwCMFOahO8a4_j3VA0I89DjfID-mAxxIUSrLsht2lGVKyxhQQgxYbNRQeYvBGJy4i7HPdGxgIKngFKO3Tg3FhZnrAZnj5YgHW5i8CgH_n_r_KZUwunmhsxiEwZyGvWd8Ccw1jaNO9a8uKWtuMtVEVIi6HIXJY85cGPrYj2Y7AKUxAom6S1DwnvCcbOdoCokJ_pBjTUgOZIy02DFGb00tqZCDIKpdq09fWC0oWFGLN5BE4RF6PDx4HTstpK7QaQwd7OO7cLf9udXaSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔵
باشگاه‌استقلال‌اخیرابدون‌مجوزو مدرکی 80 هزار دلار دستمزد به اوزجان بیزاتی مربی ترکیه این تیم داده‌ و بیزاتی چند روز مرخصی گرفته بود و به ترکیه برگشته بود که بابت به همراه داشتن این پول بازداشت شده و باشگاه درتلاشه‌ مشکل رو حل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26059" target="_blank">📅 15:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26058">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ecirDVXYeCqmYh2_GZ86IBXEOjGM1UShQo6NMdOaucWRqFBEe09gf7bhOlk14a0_Q7VEy-TWiLVHzFwyk_4v8s-QLlkjLnVg-Huwcxm8swCC0RAROiUDXkiyDePi8W3XZjwMCn12vR9gxR_LwjB_oEPLUojTu4kXjI7FpYSAJMH3h__yV5ekm1aFZmgqPxQQvpTazCcqxMTNtXCXKOOT0atv4EC1FA_N5ABHKJ-0xE8ialvycS3Xsw7ay-QVgPGp0Z06SzxCbZPH9Wft8MOXA4ao1wul44OeC6Mv1_s1DbMhwqXuJv2uWjuDme1hDXKMFmlt0eIUvnOgrYDv9C2sHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
باشگاه‌استقلال‌اخیرابدون‌مجوزو مدرکی 80 هزار دلار دستمزد به اوزجان بیزاتی مربی ترکیه این تیم داده‌ و بیزاتی چند روز مرخصی گرفته بود و به ترکیه برگشته بود که بابت به همراه داشتن این پول بازداشت شده و باشگاه درتلاشه‌ مشکل رو حل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26058" target="_blank">📅 15:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26057">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwfDroyW3fv_M1tCfheVWXpJhRJAKJQkL-Am9Mfec_tidrS557iCN1TCQSL-FgQzU2ydIRJvifEYLeWCtn2NGzBX7BbsNA9qKB0CtcF_2lxVjPPFilTvVRIqO55f1WnQn_SvGqf5VN9ZkRGAIRkAH1JA_kK9olhNYiB6_gP4sMCAUi3xsALcFN-RDe3PPLVwhcM3BaJyJ7iODHrJlg0PXOzKurJYLrI6HkEfYgq6zP2EnUuupROuCX-RZVcdaMX_jut1k99Dm155IIpGpqsTvKOBdegxo4OaWqNb0gUGD0lDjTQ69llV1gfZ9SO42LyRK9_gDDM4ONdskbM_cqZX3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ اگر اتفاق خاصی رخ ندهد؛ محمدمهدی محبی با عقدقراردادی سه ساله به تراکتور خواهد پیوست‌. تمام توافقات با او و باشگاه اتحاد کلبا امارات انجام شده است و به محض پرداخت رضایت نامه از او رونمایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26057" target="_blank">📅 15:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26056">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd306e48a.mp4?token=A3rRVGCh3UmRl8WxuECp-xuFP88wXdmx1pmq-DEnQgJzDaoOeBcrF4uXPc3iAdMc11iz_jR7KmE9TfAVWJskoDvxd26YQJtXUiZTzVf4EUfob4LHigFKyIFFu04DnoiqFFyFRd2cfJsYrFEZlXev6XH6A6-hrVbOx9p-sEagECqflvWZilmWaBJSqIYnpCsZDMzAHALtZquUnohdyjfaNRFRSi_AMXgunmHmXwXkNdUw-GhJSmC2OJgSxpYBGTFGMJ_oxioeDUNj-szZEVitE_Y9sNhJhMlAa6LwcDLNlidC1G2JAhapQSuQEY3a__gY8t79D5pibeJ-0Dpx9ShrsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd306e48a.mp4?token=A3rRVGCh3UmRl8WxuECp-xuFP88wXdmx1pmq-DEnQgJzDaoOeBcrF4uXPc3iAdMc11iz_jR7KmE9TfAVWJskoDvxd26YQJtXUiZTzVf4EUfob4LHigFKyIFFu04DnoiqFFyFRd2cfJsYrFEZlXev6XH6A6-hrVbOx9p-sEagECqflvWZilmWaBJSqIYnpCsZDMzAHALtZquUnohdyjfaNRFRSi_AMXgunmHmXwXkNdUw-GhJSmC2OJgSxpYBGTFGMJ_oxioeDUNj-szZEVitE_Y9sNhJhMlAa6LwcDLNlidC1G2JAhapQSuQEY3a__gY8t79D5pibeJ-0Dpx9ShrsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏐
از تاثیرات جام جهانی فوتبال بر والیبالیست ها در لیگ‌ملت‌ها؛ دریافت‌جالب بازیکن‌تیم‌ملی آرژانیتن با پا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26056" target="_blank">📅 14:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26055">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e509ae8f31.mp4?token=GdMG5Py11nOgV1D3rLJNKcR6Gw-d2QU2Fxb3rcRFUrZ5DXi4E__Uo589hxN0MAmhimm9K-C17OpTcCenZMQMH0Y6upfzJVXaphfqAzB7ls2cwwYNu_e7ZYx1RL7YkNGSwrhiMCEePAAtqsCHSltRMinS8FzNKAfZd7DWsK96zwNzV0KKaJNVF7x64lZy_nhalxMDGOO257uYni8YUdU5bG6pCtOZv0bqFqy-PQIu6zp4ha480InRdyau_NzpqnawHzb5lwgl7qRToPog4N7FkuLNVrhfjJQh1XILxZqBQwOA01qEAUf-OqNe2zTcpq8tRmZv_gzwpdbo5gJ-wn5XNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e509ae8f31.mp4?token=GdMG5Py11nOgV1D3rLJNKcR6Gw-d2QU2Fxb3rcRFUrZ5DXi4E__Uo589hxN0MAmhimm9K-C17OpTcCenZMQMH0Y6upfzJVXaphfqAzB7ls2cwwYNu_e7ZYx1RL7YkNGSwrhiMCEePAAtqsCHSltRMinS8FzNKAfZd7DWsK96zwNzV0KKaJNVF7x64lZy_nhalxMDGOO257uYni8YUdU5bG6pCtOZv0bqFqy-PQIu6zp4ha480InRdyau_NzpqnawHzb5lwgl7qRToPog4N7FkuLNVrhfjJQh1XILxZqBQwOA01qEAUf-OqNe2zTcpq8tRmZv_gzwpdbo5gJ-wn5XNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پله همیشه می‌گفت زیباترین گل زندگیش رو در ۲ اوت ۱۹۵۹ مقابل تیم‌یوونتوس زده! اما از اون مسابقه هیچ گونه فیلمی وجود نداشت. حالا گوگل با همکاری خانواده پله و با استفاده از Google DeepMind، فیلم این گل رو ساخته. این ویدئو، فیلم واقعی اون گل‌نیست؛ بلکه‌بازسازی‌مبتنی برAI و اسناد تاریخیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26055" target="_blank">📅 14:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26054">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAeTcZQAXUdazBe_r_5p0LesJn3jr9_KKjaMiYZ5ls2wLUNzUMHm52S7tvyHVLlRE9y6UBp9DqUk-XDjBD5UohYnjMuWo8KRG32lN0H5_3zY0DoJ3nZoKhQATMgpRRs4QXsOhaTovNH9HVzUs1Pdw9X1QixWSPPcPcm1OQWb_vGrN-HNXjx82EUaSqUx5Yx3iQdsrDCfJoQwgBu-Tig3jZLPQJfSs-e0f43ffSnhuZupJ9WlpFUFXZnD6kjgy8xG3e2JCSiEHC_l4noUaJhd-Ow0qVR1uzn_Vs-CmAALFULAxfjFAJeDmeN3vX-zqESTwUE29kacnp7-G560Z4SFpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دریک رپر آمریکایی اعلام کرد که؛ این بار روی قهرمانی آرژانتین 5 میلیون دلار شرط بسته. تا حالا هرچی شرط بسته‌بود برعکس در اومده حالا ببینیم این بار درست در میاد یا 5M$ بی زبون هدر میره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26054" target="_blank">📅 14:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26053">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqYEdLBTGOkPy-Ez1eAn0ZqYH_n3vucpcMnqkW29x_Vl9M-BcadspjAOloxbzS_U85xlnRDrkM6mw_dSyjgTY37tyGvtXhvK_SRP2VAPzlc-gyZaM0ydDdA_HDTPB6fC7ed6Gu_RcYnRwfRaqwPOZcDeoTi-JuMp0mClLruzk-yHZh2Scf_Ooerh-caXStqt7OSWpyG_fcWbmOErXwB8B8Q7t2_V9mu7AjGdje4Dck4w7On57O2ezFabe2BTLhLG91c4WbqcuO_lEUecKkxT5d4Bsr-wFAy5Ph0Ihg17ORJKiiWctO9e3Yl0zpPV40bshQI2bUS9Wbou2n4GcdGvBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری #اختصاصی_پرشیانا؛ سیدابوالفضل جلالی دقایقی قبل‌ازطریق مدیربرنامه‌هایش به پیمان‌ حدادی مدیرعامل پرسپولیس خبرداده که فردا صبح برای عقد قرارداد وارد ساختمان باشگاه خواهد شد.
‼️
حالا بایستی‌صبرکرد و دید تاساعات اینده باشگاه استقلال برای تمدید قرارداد جلالی…</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26053" target="_blank">📅 14:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26052">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NiWbzI1IvuZkcKPiy3VtnNVXjTGi7SkrW96WGY5TKEfUGyQuE6LRLFEa790taeOfqlMKDHfy4YA8mC5TlNolRg9nQx2I4GIudLS9EDod_kDNZjV-lxYv_b6Yy24jvYlEH-t-HyHB8fFa7VJ1EmZub2DJfDavuA0aVSiMVa69XjfNyslXKsbAViAHZC1rGvleyKDm03l3z_11gYG2jsWkJj6nry3sYHnfSskxNsMsFDtSd3UPdyTmxAFXumC12CGFwahxJFGLnOLlbhpdJdEZQGqtM_w4Cmf3_G7nSRyGWmxeGBaTrhOsRTBSTSrBZvUBTF6sCCbDD3ymFjVFVe0fXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرط‌اصلی‌باشگاه پرسپولیس برای قرارداد با ستاره‌سابق‌بارسا؛مدیریت‌ پرسپولیس با آلن هلیلوویچ گفته که‌مامشکلی‌برای‌عقد قرارداد باهات نداریم منتها قبل‌قرارداد دراردوی ترکیه بیا چندجلسه با تیم تمرین کن و اگه کادر فنی تیم اوکی داد قرارداد میبندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26052" target="_blank">📅 14:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26051">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uobI9QxIEBQ8aLQy7PoxX7DdDTG250ASB7nmJnHRK7XUusRp2eRj7oZsqmbreNLM3PiMOE7fP06U65bgQ74HxEj9fbDIpzlr73rdPdlIV8HuAArAFfZoXz8goCqVL7y3_quukE2MZKQC8Wl3p5OYVP1aIpkka6MQSQNtCkrQ-vN_YFcsG60qvR-OEDxJxVeTbWXt6j9KVFWYKyPL-Rv43Vq5N8adIck2Tm7lkUgoIprmw6e5QMl_ZMv_IX30MVH5g2Xay6xkWBwYOC949sQbg-7BIV31EodkpXc23j170vHd450M0mPDcKSY0CDVLM0f9vacpsC_kfIMW0cH5RYagw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
طبق‌اخبار دریافتی‌پرشیانا؛ مدیربرنامه های رامین رضاییان شب گذشته به باشگاه استقلال اعلام کرده که این بازیکن مذاکرات مثبتی با باشگاه لگانس اسپانیا داشته‌است‌اما اگر رقم قراردادش رو افزایش بدهید ظرف 48 ساعت آینده رضاییان به ساختمان باشگاه خواهد امد و قراردادش…</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26051" target="_blank">📅 12:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26050">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNI5gJqpzBcwxaMjLrRhJN5AQEV3bHRm0W-McKDPPNeCNEGABsRJAQUjQtbvwvId_kNDgss201tMuzCClcdQiXEhpN3Q_DnpeSXvVSRvVlDDBitw0xGWX6NW-5vD98szw0_NNuFk7X0nwdk2XKb__mAik8GWjRPQoxI5YiEgt-nI0DRVaEYV_P0hnncIFig-VhxBEGLqOl14I_tN4hsUeIfW-Mu0EPM6S61Fapd-e3oz7g76rEnuVgKRsthSZ1GaE6qKrR2bgdLFq4jx90FcD8NgXwVU74AxjVnIFlsNWJ-zYPAV5zPFFkc9rw-enZmXD5M9nfZxbgB_ohsT-AsdSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇦🇷
#تکمیلی؛ نشریه لکیپ: فلورنتینو پرز قصد داره به محض اتمام جام جهانی پیشنهاد فوق سنگین خود 200 میلیون یورو برای جذب مایکل اولیسه به بایرن مونیخ ارائه بدهد. بعد از کارهای اولیسه پرز میخواد انزو هم به برنابئو بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26050" target="_blank">📅 12:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26049">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbaFgLDC0t_UIr3ZDJzXaD80gp8SbktVcZUbXIUKVN3CBBC2i_r2-JVC7qckhIHEJ7lXuU1al2mFPmQqjfRbjktUgrwQJuBx4yUCQaNO5DZsuuaYyDMve0_y2fof5F-a9vocPKE9e3rvmCNWXrYYbQnnT1N1b_ldvhDcYKcahrO6xleKUR3CzBe3BrGqqAc_T8Nl0IB_SVtptyWOaME_3qT8rQeEqRx0sO2K7kQUkg2xagZsna2TAi9H9wcGMPnfZ6vG0uBAPK2ku6mD_HLdlA2XRhuYCwq49kEvs4GH9KBNaIZ9aULnqW75bQrz0XiVwKFtbjiaLl7olYmFxVuOTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کلارنس سیدورف اسطوره‌باشگاه‌آث‌میلان و رئال مادرید درکنار همسر ایرانی خود؛ سیدورف فصل قبل بعنوان مشاورمدیرعامل آبی‌ها 250 هزار دلار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26049" target="_blank">📅 11:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26048">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fswGm7EWH-yxESVuAQ8cQnPuUvYVIwrgUpuHDoQQ4bP9TJrDNSsDpYxjdyGJ4FzpBUUHWF1uQzElo0ivxZEbCuSIU3W2d99VnLyfHhBw22qsacJia9jfR5YOnn2gw7Igh1qiLnEi3xLlM82zHr3Q0TvNvl1TYKep7lzKQjYw4w2q7IVzD7KFbLZeUFd6uFtBR-2tRIb1KE_yogBktCMhIjYHqLWOezdDAOpHG5zIdG3pmCMnjuwnjcL9kHtEmPuXNCFAhvvSQcXwFqB-Iu9_xFHzFGFJC6fRu3mIzdYm0cFRuxmE4iGz-T0mK6neiRU_XoL4DRUMkwFoeUOz87PdlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26048" target="_blank">📅 11:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26047">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqeLGhQZVPhOYfwscG1XSKSB_ARozbYgkuob7JdBsUeO0eLJgMW7ygkbijIWOLNjddO_pu6UJw-LeJSp42L-9t_umc25FqXr_ZaM3Y8bHxXXEdkqxcGN2xR10EGVpokgjkIBFUA45eu0xV_yWPyUniaN5F-xPtfgcRVfUeqP_F2K9wTUR0iuU39deYqovaw6lMNyWnAFcWhl6kqbmIBtp2rzmF5EU_9MXZnXa-lwK_VgNNC9Kinnk2a2jJwBNfAayz1wXID5i0oercFQ0N5CDgwFlbPODaqpYzYfWwvdhRMyunm1WV5qpi58Fb9Dg8EnW3sLimYkVVPXrC3m5dtvHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ‌جام‌جهانی‌ و برترین گلزنان این دوره از رقابت ها؛ کار لیونل مسی برای آقای گل سخت تر شد. لئو اگه آقای گلی میخواد باید امشب در فینال برابر اسپانیا دو یا سه گل بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26047" target="_blank">📅 11:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26046">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-VA2SM72-KFF4XTc1PPT2GS0QL8iDP6iPQLtHWGij9Hqgkz2ZUHvalHvGw-3_eeL8UAGiplRxTqwoPUA5J0EhvQROKNjYASj9ybmNs11QLMd-KCYBem79h7u0UGozvh6abN4JA7wW7x58fqnjm2Lpxl-WjRTFvctCkJtXgEjJsSY1-HKZLPw2_NoCGh91pUR5jxK83pca994XL94gHwrGF82ZxOwU5xcGtVrfDhx1yPcCsvyJh_7-CEdIRZWSNX0mv9_tyfqLyGHxh8YIWEcRUzu3EBoqn94h304O6A6gnxGJE4GyMdWJcGT8nQ2PcZbYsJOTBXAD8iSr6DRak0IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇷
🔴
#تکمیلی؛ رومانو: آلن هلیلوویچ هافبک هجومی 30 ساله کروات در آستانه امضای قرارداد با پرسپولیس قرار دارد و مذاکرات این باشگاه با او در حال نهایی شدنه. هلیلوویچ طی 63 بازی در فورتونا سیتارد آخرین تیم او 6 گل به ثمر رسانده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26046" target="_blank">📅 10:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26045">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfK9I9pFz4XI95aXMYnbZaXf846w-l_rEU5Fss9lBUm_-dKUQ5Bu6pbtNZf9GJv9XwfuTNJ5r--ZS_HqH5eE2KhLWuInQMwwx5fXt1SSaU_HvepJ3LfdwN8ucc5-ObtEMiubEgu_IjasyorU72dHdOuWBQrQ3KyEPS1TZOWZcwMi-bcJoYS25sbw1Ua9SEu9RnNuXMKUg8sYfiMZ82zT3Qogv_K0ZtENBxz0xl2qAxhNig9qdw29dt4y4ao3iTAUzY-BULN0y0o0G_coM_oJIr6HZdpaYCONtzA2SU-RXOmyhNI0lJw0PiQMEzNarpu9r8zdfhvZVZ1biILmMrSzxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه نساجی بعد از جلسه امروز با باشگاه پرسپولیس رقم رضایت‌نامه دانیال ایری مدافع تیم خود را از 190 به 150 میلیاردتومان‌کاهش داده و72ساعت به‌ مدیران پرسپولیس فرصت‌داده تااین‌رقم روپرداخت کنند در غیر این صورت توافقات طرفین بهم…</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26045" target="_blank">📅 10:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26044">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">📹
ویدیوجدیدوبرگ‌ریزون‌میلادکرمی بلاگر معروف و محبوب ایلامی و ببینید. رفته رو پل B1 کرج!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26044" target="_blank">📅 10:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26042">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05254735f5.mp4?token=qdjaNu2ecsLlo-SVVZ_5bwKVTZfoaVCeqOdoZAqWOEduUj9cpdds_I6HBbYbFshXPZqIT5SPmTep4jVyH3HMF7npi5xmVOeH8fHtrYIZ8_E85xhs_prqit69nF4gAqtc7rSVUUcWUYRg8rTRFtw50iLrBFFkrqHbvtWQP2AINz_VXwTuj-2reaXjfk7yGVFS20WYhbEosqJfT7IPnVowmUY1KqbOOB2DnNvY_VXhBzX5qUAsNT1CyR3qVMnkRxIevs29RwhYnBG7LoAEhxNAcYOtOsfqAfoX3ygVyUuDSwEdy78Kw8MK4kyZgaKmSD5TckGysLF6Ij5R6-Tkoo_oQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05254735f5.mp4?token=qdjaNu2ecsLlo-SVVZ_5bwKVTZfoaVCeqOdoZAqWOEduUj9cpdds_I6HBbYbFshXPZqIT5SPmTep4jVyH3HMF7npi5xmVOeH8fHtrYIZ8_E85xhs_prqit69nF4gAqtc7rSVUUcWUYRg8rTRFtw50iLrBFFkrqHbvtWQP2AINz_VXwTuj-2reaXjfk7yGVFS20WYhbEosqJfT7IPnVowmUY1KqbOOB2DnNvY_VXhBzX5qUAsNT1CyR3qVMnkRxIevs29RwhYnBG7LoAEhxNAcYOtOsfqAfoX3ygVyUuDSwEdy78Kw8MK4kyZgaKmSD5TckGysLF6Ij5R6-Tkoo_oQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی امشب دربرنامه‌اش و در گفتگو باجوادکاظمیان ازجدایی‌اش از اکیپ عادل فردوسی پور خبر داد و گفت جدایی ما کاملا دوستانه بوده و ممکنه بزودی به اکیپ ایشون در پلتفرم ۳۶۰ برگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26042" target="_blank">📅 09:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26041">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59f65ac5ad.mp4?token=VrApMFKiHCC-M-JECsSsb4JGSZHpTrnOIWrkm7SxqVDPC9XB6FJZ18IHLx8O0b8cBFaxQoi8zYc66BtaqXnNqZStcFcwK6ydomz3Sj3idjUoldLSJXuWoEqFqUstQ0h8FqJRINrWNS7nlx1zpyu_mzF01LTCRGN1CoSvytr3cZ48UTbkxgb2bNHS_vpvyEOSoiQcjmbSmRMxk5cv_zNp7Gp_6nDSGhcSnDw13u3qhI8Ex7klEyO9BBksD4ssJXbn88U8myPQaBslf10dPQiYOXfOwqlSkTHIjfJc8153fn7kteUHDyznx2Tsymt8lgZBi23rsJR_s3hz7lu115Ca4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59f65ac5ad.mp4?token=VrApMFKiHCC-M-JECsSsb4JGSZHpTrnOIWrkm7SxqVDPC9XB6FJZ18IHLx8O0b8cBFaxQoi8zYc66BtaqXnNqZStcFcwK6ydomz3Sj3idjUoldLSJXuWoEqFqUstQ0h8FqJRINrWNS7nlx1zpyu_mzF01LTCRGN1CoSvytr3cZ48UTbkxgb2bNHS_vpvyEOSoiQcjmbSmRMxk5cv_zNp7Gp_6nDSGhcSnDw13u3qhI8Ex7klEyO9BBksD4ssJXbn88U8myPQaBslf10dPQiYOXfOwqlSkTHIjfJc8153fn7kteUHDyznx2Tsymt8lgZBi23rsJR_s3hz7lu115Ca4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌های‌سنگین و پی‌درپی عادل فردوسی پور به امیر قلعه‌نویی سرمربی ایران در برنامه شب گذشته
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26041" target="_blank">📅 09:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26040">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده و مهیج شب گذشته دو تیم انگلیس - فرانسه در رده‌بندی جام جهانی 2026
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26040" target="_blank">📅 08:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26038">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tH63WIY4ZrDSsnHbsLgEuFVUeu6kGWfbDo6Zp4K_CIMWA0IQNofVGnqYTpNQSNwevwAPspr9mJ5wW4R2-zQcIOGlYg4qmR-Sh0618swuWIYmzQLQGAGzNgsTkHi2_MvTx69qLytvFIP8AKXgAXLoUHXg6_l1Ax1zsvtloSJEvcguXp1Axozh4xemJ9jypsKUWy0o5nmWIW3HPQEh9TOEkvY_a6EltZGBxvOgS93KSo5HCrZM0LpT4XgegH-tnGK3dyT_JCdEBK4-aS8TL30G7MEQXbltc-aVWVCkwNRS6M_gbgS9rhmchbAITiKdQci8rolY-HMqWqe0E2RdPXDCMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I9naexZj_e5R7VEzhHvHcqksAh_brcjF5ICC-5f8KI4H5OVndDTGgc-T7VZ_i6FXEOrX4neKVJe9ReuUAqBVRNaWpMUogAQOGgdqRn3dpuFvPkLTAHT2MR8X9aturHMGBiX0w_Xb4iXo2IoTMCFamy2vDfLTRxxya-G_Rjwh4FvVKd2kP-ritlTQSgV7D_dj-HLiop8JF3VUKMrVBzuWTaFX6YQUosjFN2ngx7rBTEPOOBzDepKD78BmBM9KN5kzLoRScGXlxxZRNhfyQ8HXILHrd1h-qehN4dzCUZ0h91kmgCFjl7aBCjdiEsQEtyWmrjtgh8R235ph7jp8X4IunA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
تیم‌ملی‌انگلیس شب گذشته در دیدار فوق العاده تماشایی بانتیجه6بر4 از سد تیم ملی فرانسه گذشت و رتبه سوم رقابت‌های جام رو از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26038" target="_blank">📅 08:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26037">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cv5sRfSlfaRzz_c3S55_fmaZVSYMjUzcQ5S4gtlwR7cZ8XmAIcJsF3qC4hTeGZvRugkcXG6EZcajDNEbwgXc9uBmua68FDKo6k7rB3iA2O1pXgzDLzEql7DPyLE7g6Rqkt0fQhcEMVu0PMiomsaroWfoweztiyvVfRO1UTTltLkDLOnDlOOm-6kVeGaePwfEzvtri4X8_XKJVdEwTjmgR4CJvecyUVmniTygweXcfk8rP1E62klpY1CjEfq9fG9cRP0EP0h3gGdYr_dEi5YBsPRyeA6AO6t3MwAiqV0rH_IkWqjXVgO244IcP4-FzR-3cEzYxd9v6cTtgfsET8dp_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مسابقه‌رده‌بندی‌ جام‌جهانی 2026؛ شماتیک ترکیب دوتیم انگلیس
🆚
فرانسه؛ ساعت 00:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26037" target="_blank">📅 07:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26036">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b8dc0f4db.mp4?token=TS2LePqNkVa6aCFNaAU1PbEmCQlt4IZMcD3vWvfnC41hDVhbZxT_bLU-uY1fMbs8-LD6LZuXGuWMulJwfMIDZqcYPmApYHP6Z3tBZEE1c3Qk6HhfdfqTfOkunwcaNMMlJpUAfjFI2Rru9Bi5xlTpAhPp7GUWKlKZcDywjeGRoNyV0K13HQGrah6dsPNniPlOyFtJB75pgqDGH__Sk-IeVzy9ZLKve7fg0A_K4CmgHBsEWUvZgvF4h_1Z27HhFaTHZVhBSNXNqm-LfrtwBL9PW8uXpNWMefhan8ZZHsOrcqUpqbxs3wTetGVyAGSN1SUs4fpo87ArrJJ2LP1EejMCZRJcb02Va9mMnXQ5i4masZgn2IKs2MvPvOjN9ZOh59DyNnsn9imWFlaT0ZLBNE4nPNmr-r5kWttE3r3Koj-_CTsG9UtLZYOY0oshrCxj0cGqayy4Q3dTYxLpOgvTnJi4V6mF_diJG61We0mb0SWbEGuCVRZ7goOWo7LFB2aNf50fBfciRCfH3EBI73VxSnLybD9tv77oii2cG6mzRrR5JO7M-X2_bB-AWTJVGd9TPLzJE0pIhfqBrgx9Q_p9um_hXJWfMhMt62Th_R6iGMER4MgUQx5tA2YPBpBhs0p8xB0k4MZJoRTippLhhjkRHvf4A1bgJH5XmqmyyR-QpjxfXJ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b8dc0f4db.mp4?token=TS2LePqNkVa6aCFNaAU1PbEmCQlt4IZMcD3vWvfnC41hDVhbZxT_bLU-uY1fMbs8-LD6LZuXGuWMulJwfMIDZqcYPmApYHP6Z3tBZEE1c3Qk6HhfdfqTfOkunwcaNMMlJpUAfjFI2Rru9Bi5xlTpAhPp7GUWKlKZcDywjeGRoNyV0K13HQGrah6dsPNniPlOyFtJB75pgqDGH__Sk-IeVzy9ZLKve7fg0A_K4CmgHBsEWUvZgvF4h_1Z27HhFaTHZVhBSNXNqm-LfrtwBL9PW8uXpNWMefhan8ZZHsOrcqUpqbxs3wTetGVyAGSN1SUs4fpo87ArrJJ2LP1EejMCZRJcb02Va9mMnXQ5i4masZgn2IKs2MvPvOjN9ZOh59DyNnsn9imWFlaT0ZLBNE4nPNmr-r5kWttE3r3Koj-_CTsG9UtLZYOY0oshrCxj0cGqayy4Q3dTYxLpOgvTnJi4V6mF_diJG61We0mb0SWbEGuCVRZ7goOWo7LFB2aNf50fBfciRCfH3EBI73VxSnLybD9tv77oii2cG6mzRrR5JO7M-X2_bB-AWTJVGd9TPLzJE0pIhfqBrgx9Q_p9um_hXJWfMhMt62Th_R6iGMER4MgUQx5tA2YPBpBhs0p8xB0k4MZJoRTippLhhjkRHvf4A1bgJH5XmqmyyR-QpjxfXJ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت عجیب‌وغریب میلاد کردمی بلاگر ایلامی از افتادنش از روی صخره بخاطر یک تبلیغ کلینیک.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26036" target="_blank">📅 01:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26034">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf49687f0b.mp4?token=ITZLc0cmS3038Y6I43tu3hH44Sedhe-GiKUhF764x3BfBS19YLfNumGrOFswQbK14mJ_sQwc9dmizooW1co6wATwv6of24mWrXcMLI5aplkJJ3Gdchrgn7CF-RpWIJg8AS3sKjpwa0JbG-UfiTRJFjFV9VqFbREmRxOi2nx2hFebG3gBAuqOPYgJdm7kKko7FYTtlj8Vnwbhqbt2rCPq-JGt7VMNJUpe1XZSaW-bE3tecYPUco8ap8v3q2GFE71hbUf2x0OtMBT3chwdoY2Qi8hmZUHOVo5azMTOOuSDudZ5muEtz7RQ0uMabKSfsbJoDI5_TZ78MEDVw_4U4W3whg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf49687f0b.mp4?token=ITZLc0cmS3038Y6I43tu3hH44Sedhe-GiKUhF764x3BfBS19YLfNumGrOFswQbK14mJ_sQwc9dmizooW1co6wATwv6of24mWrXcMLI5aplkJJ3Gdchrgn7CF-RpWIJg8AS3sKjpwa0JbG-UfiTRJFjFV9VqFbREmRxOi2nx2hFebG3gBAuqOPYgJdm7kKko7FYTtlj8Vnwbhqbt2rCPq-JGt7VMNJUpe1XZSaW-bE3tecYPUco8ap8v3q2GFE71hbUf2x0OtMBT3chwdoY2Qi8hmZUHOVo5azMTOOuSDudZ5muEtz7RQ0uMabKSfsbJoDI5_TZ78MEDVw_4U4W3whg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🎙
علاقه‌ شدید‌ جواد کاظمیان به مونیکا بلوچی ایتالیایی در گفتگو با ابوطالب: خیلی دوسش دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/26034" target="_blank">📅 01:28 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
