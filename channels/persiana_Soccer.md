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
<img src="https://cdn4.telesco.pe/file/CiZGMBNWMltb52ip6FFVQ_MdPlrw446EJCS2fInK8He-cmh35qVVrv5qRFzT8dRUXgf4nxKz5EcQJ942ev-oQpn3Qd67Z9o__p7n5FUUHZ0J50uXGBiufluMo-bYUE1v1Y2DSghfpZIVXEiEU7reW0ukZzq09n34joeapxxJthATJPyvJ235-Wtia9gtDbFLgJhhnRBqsSygkCCFfExnmUtko5yh6YUtffsTQKQeB_UD34qlP_3qG-365qp924abFFBfp0xKrzcweyHx1Od-TEyVY8jDvdbVaVzKME6G4aFrjOkGj23KYzm_hfvWCbNXfSs154KaG3t7d7MC9PGnpg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 423K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 06:50:05</div>
<hr>

<div class="tg-post" id="msg-25331">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T0K-SWRQ3FBgfpjNUzSoEMiC1kmXop6KJ91FZzeb-cWa0HuA98GhfGL-_BIgr2x1XEjT5MLAsOdoTAMFKsqFUc3Mo4zEsXQ5cI-0iHJ8AuPMc5c0l_wzcKKktNFhNu_QhX2QhsYmJ8ytlAQ-BidGVXBXmE3Ci89ZxtqlzO8zal4-2FiEYbP_XgkS0hPW7i4FWuJaJeq3nINYjmHEhmjzDcQ9ZGvX_9iTetyYVo9wgYt1msH7u55n09PkTd4MhVa3oIn6ncRuvgAsLIWkYa5VO9zWjFOIl7mMupUZCnk3vYkdPKmg8kIUjXWZkdBetsrUhMNZB5tTmTIYTln3dyqIxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aQT-2r8dslh33peLPt4TwVquap-9Xs4NJ0VOq0BkS0BOlttKfwdl0poQBUPsPVuitjiAJ1-jRxb3wQnAIKSlqT_luVloak__uh6IsslFUddkOxrxIouw2_a8DIRQXytenKMBxAMwFSl2_kdHo1JUexGebBDmf34auxP4ISxi9t9EZYAEf9nU0ibqRdmYsoyTLALqK3OqFBY8HB7o3BWKKufNwQlc-2xf1nfoGI6BhPq2xg4SLJ8FI-GwupRySvarJ1dB64W891V8QptTV3s_weH7Rkw493Ey4EzFizQT2BoG56dJaQpi73UnALxDZg5umt9uWiAACh3rYjz1p008zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
#تقویم؛ 10 سال پیش درچنین شبی؛ تیم ملی پرتغال با کاپیتانی کریس رونالدو به اولین قهرمانی خود در رقابت‌های یورو 2016 شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/persiana_Soccer/25331" target="_blank">📅 02:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25329">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ilI93RFLuURoToZnJ0884Is8QXSdn4ATsNoDfaRZzPR8QQZVBYqCcF06SuN1YJPTZ1i6x_6P8EqgCra3T9veCZiSKP1qWfKwRtRWwmjHtzHA9w_KCoSfIH863cbSWm_6OoUkAEY49eEvHNMPQhvFsgrp2y_gMTSXnC4nBbrmLb_K8XNCFODAmNyuVm_xUpJRMvWcXdHWfXXVEr6-9B6nEbLaxTiECsIl3uTgSxaz8PsUE0P3QDEEZAXaWguZCeijt4KGL8QQku6CPvPWpglHvv3hFUk6u2Ne6b7WmNOSG2Xm0mUHHO892WHv5NNosSpUbv4Jpkt2rkJRi_QCeQqI-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f0ejo86gQzXZE5bwLuENa71MEtX4GL_rIGewV2xBmROLmQh7pBiGzeoQhV39aH58Qp2xaCU-9z1guCquGiamjOUGvkgsZjfZy-KKW8Zxaeq2W_IRS9ILgKYSrjhk4R5B7jZpHIHR8I4TkwkGzPcMcWJ_VN1fIsgrONwa-C5iFskBA8wCERD-JEc1a9LquyuAOJqogJh6OJkAF0cstQWpv_18eEMqzqckCwD1uafCFm99KxncCatMEDRwBJzcaPzHBJduThGcruolB7XoyqK0SpN3Hk2FZtc0AdlttAqNiMou8oj22_oHxYSigg1nfJDDve3c7im22LSruGeLZcOpUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇵🇹
ویدیویی‌زیباوالبته تلخ در وصف کریستیانو رونالدو کاپیتان پرتغال بعد از حذف از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/persiana_Soccer/25329" target="_blank">📅 02:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25328">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4hkucHWRJrGx3bxwF-pC8npo7pP8xklfHAZqIvlkJayJpVWIIQNFmZXpk6Ektw3SLl3pnepsICqCErrBXcCE1Ln2kjMZTsodLACL84qVanPF_SqsBuas8C6BvJUtERuLrQL2rSI4PsaRUUfwk4nE9auRl8IipS7lCrGsboec-chTvPT9U1fHbG-wCs8Jd4C4XT-sp7gOVlKqUwtAGDz1bPSvXaWfNZFnlKBQ5S6q41_FsfRK3wNX5pkt-B_p2VL7x1VbqXws0gXLzYGd2VCjfxIYF6pgOoKbuDSwCjsJCPgFBAmy-4_kqU0Est9BuxelI65VQrGgeVBz4bndT9KiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز خان کریمی برای کارشناسی مسابقه امشب مراکش - فرانسه رفته شبکه ماهواره‌ای جم اسپورت؛ خنده‌هاش رو ببینید دهن سرویس چه ذوقی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/persiana_Soccer/25328" target="_blank">📅 02:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25327">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWLezMyytgoVThdEoRikhUWQrHzdCeImVMDgTsO2PA7D3Z-e9ozpdbaBhh6FCGfL_BxQ47EKk40DNtKgRqBEZrPaJ3N6CL6zl1Htu-Fn-tg3sTqgNqktcgl33BSfC04CvAysb7nLhsrIjurm9s0vVlRu7lRIJWzd356TnkvxqwYgt8tOHuH7m70-GUFH4htfZYZV7BQSTjD-2NVrSFtqpyyDcA51amhae5f2FApSaPV6NO4cOp_1ZNIBkkrnjPEiFD5cE34X70tpQNLYWDgoTSOYpx3TXARWf0pdlQgtcwtDIjOCYofzJC-PQyMuRRJI_zk6nSqrGPpL89ZhRL03SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی جدید استقلال از پژمان منتطری کاپیتان‌سابق آبی‌ها و مربی الشحانیه‌قطر خواسته که به کادرفنی‌اش اضافه شود. درصورتیکه پژمان منتظری به باشگاه استقلال برگرده وریا غفوری قطعا از کادرفنی آبی‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/persiana_Soccer/25327" target="_blank">📅 02:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25326">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aROhzyBplmfJOKMVjZMRSfl_lsozUywVQiA8Ft-AjQWXZN1aHHcW-mEeb15aL8FnsasAG4pkfmiNs2974yz78c8QkiueI1vwGdggvl6u_zYr_s1cZCweYt-Ln5SYDJOcwtOFpcdqkuvBAfaD6qFK7oCocuLjuOCh75LPpJnWD28BxmDogYoikpdMFoJcVkhxEMGpH4Is3bvys8cFMx9C73nx2ZgZ3P3_kyJw1UbFvCXzSOkGwlQICDXmj4sx7ERRfPfrSNQ0rsAb4-li_akbJZ7uGcnI7kgiBFmEgj8C__-Bkvz-86MF4E9fzRVBjUGePZm3Cbo4hqVo5LaS09-xxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همان طور که دو ماه پیش نیز خبر دادیم؛ امید عالیشاه، مرتضی‌پورعلی‌گنجی، میلاد سرلک و سروش رفیعی درلیست مازاد مهدی تارتار قرار گرفته اند و به شکل قطعی از جمع سرخپوشان جدا خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/persiana_Soccer/25326" target="_blank">📅 02:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25324">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OIUWxwoNJa8y4r6z9MAPF7aF8IKkR_37Ua_ZcPs5g2zl4JX5rx8_y6VESce5q3EPsU9XfxjvupT9-qJIKTiN3Fk81Ln3jIqGObSiU--YCFkmQt8X3GT8ao82F5xkcyXRsPk1pjzH51xDiGFBMnpKxibWn8mM7B0dNb3nhBpktbPR-_PQlc7X3PS_ggRgxAgfpTjJ6yL4y_518DRQQHvdPnOYZ_fPY8N13ztCjGVC8jU4dQEznuVdyG4OTfxqkmC--B4gKvIvwEvlEFy5WaifXFTfmHkgbBJNcz8hDj8l20X57s6c2VMXrZ_HJkBzxCtyb1CkuY-aZkLX8OuUskT-Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ieUVRmX3L9Dfv0mlUuRJ9LrgLgveZVc4DGkvOwM4xAtfyNq9UJDFbAAa2nv9c9biYIbsLhyaskmQQgiT-crLmbKY2T5sfTl_oAIbWnQwFuZm61qPeplI1UwH-U2UwYKyp5Nz5p2ubHjnS_Nq-c4xhKLh0daQE82ywil3qPo8NTteHaothEV_2-1WaFjlZgqJA9fl4G9Zh7z_2JJhLxcXvRLdwHqZV8QoqXKlLXXPjnl1uBel4QOC2FtSF1iFIxzqyhv-cQVZydpDyb-3wlB8FSnHANA8UQZoAkS5-OAua4qcAPYpCQQybOpLEJ4W8eUPS1x9-IhFI1wmWjPJiXQ-Rw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌چهارم‌ نهایی رقابت‌های جام‌جهانی 2026؛ برد شیرین و ارزشمند خروس‌ها مقابل یاران اشرف حکیمی و صعود شیرین به مرحله نهایی رقابت‌ها. اسپانیا
🆚
بلژیک حریف خروس‌ها در نیمه‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/persiana_Soccer/25324" target="_blank">📅 01:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25323">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPrQGkwJoghmnppGz73IBtsLsEYYYz4u0_BAM60AJd-gJcZlvmetHnrKj2F5ibf4CCs2y9WaCgeItSDvlzoX5ttGWGY1bdHmn8sNd4Ysb56xi1uf376rY3J0J4r5XvTcq0LTPcgFVsabjirh8Msd3KFnSah1Ey2ig-YU0BsO1UuhuzvsDGqIVRRzF4VvvdJvyBICBPgbQqxkWgGfcseJIBcq2XN2rOaEFcvWM57Kul_GH0qhgjFv55zwHgg5t29xr0xivajQFDC2AuRJDYAk_eMtDCmgW4c6JSW9BFahdtUVWo-9tn2prmHb_ducr_11P-Nvz5OOkF-LDamkgtS_pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌امروز؛
جدال‌اسپانیایی‌ها با یاران دی‌بروینه برای رسیدن به فرانسه در نیمه‌نهایی جام‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/25323" target="_blank">📅 01:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25322">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwECH4KUsUlMItlJxkL5ab1aYPWpdRgVwtJMJWcvxapS1MnM4k67wd0yPRzjC9KKOPwUjLSVtjdVgDoBrT2TI7L6QGlML9n6NsAvZIRqC8B5ZBYcXJJCOnnK04e0x0A5veIh0y4fZ_GcyOHKwbtjbGPUxezDxRkvPuHVG1U0FoB7azkmxbQub3PT2_q41nFDSDPOCjy-Iricp0DqQSZRG5VUTq1o9wOLs6ZiCrJdcE5Ev9CtgNTZdTBDOVs9GtveWVWFpKE4ktZcubxgu5fmO9d0SSoZtpX5pS0fCzDmbNdepGCGKSUP5AGd2c6Waf_9DK2pi6dPMZ7ttv6c0NruQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
برتری شاگردان دشان مقابل مراکش با درخشش همیشگی کیلیان امباپه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/25322" target="_blank">📅 01:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25321">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXeo5Us5VAMaorcYNjGdhx5NmPPod5uos1cEdGSJU14mujlyOd3xduqZ8OpuU3jKKmN8cl8_4zshmeX3j5qCBNi3ReQomuAC9XxNMzmypk96LYu5NUuuvxupQHb9vrSDw8zFcU5E5sy4EJYYuqTd3XlsGnXJNsB68Hb5Zd9Pe685nQHt_gUFRg9RG1zbDVpypoc_XgEY_6gRYHQUZ2LY4U_WBiCuJ2nzpFVcJpuX40zqo02kse-k0JQkjgLI4QfGjl5mGkQGxRGBZOz3dnb5zWfPV_MVXScAQeBSSr2-XJHGL9vE0Q6iyDhnX2wRj896Ja-X2e_e3Ki8IiGWs1yngw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی؛ مدیریت باشگاه پرسپولیس بعد از عقد قرارداد با ابوالفضل جلالی و پوریا شهر آبادی از آن‌ها خواسته هیچ مصاحب‌ای مبنی بر عقد قرارداد قطعی باسرخپوشان دررسانه‌ها نداشته باشند تا زمان انتشار پوسترشون‌توسط باشگاه؛ بخش رسانه ای هم پوستر رو اماده کرده و بزودی…</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/25321" target="_blank">📅 01:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25320">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBpxjyUfyj4m-a2yyjApRT0RRucd365eN3OWIZYijFG_GTDookNYfwAojOqz3w9drffbjQTwS6efRm694YdLk_x3Odxcxp57mMLyoiSuHjlF_MHp5D7z-HJ8H9JonPrE42QjmadVxpSvvOp1Wrz3_Jyw2Gez9IWV6UMOTsWOo63XKsw_DEV9rXO1I_-NO7f8L6Iw_MKYCv1_L2SZ1hUNAinFaSMqdZqTRE7z-3KiJCWWSHybuJ0riRP9ANr5aXh1xPtoISNy8Jfz6KagtEqxhaCQ0ZmskUJjju_3SbUyqy7hY_JvY3w8IdODcwVxFuCGRgK3Lug8mznN71sONJHUrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
دیکتاتور جبران کرد؛ سوپرگل دیدنی کیلیان امباپه دربازی‌امشب‌دوتیم‌فرانسه
🆚
مراکش؛ این 20 امین گل امباپه در تاریخ رقابت های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/25320" target="_blank">📅 01:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25319">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhjM4cu61bikvJpnzDFByalaSULkoQp5Ny7CikJG2g4QuA4rPUZuzq8QRYZKt7fpzdh5jNxTUcBxqiprjS6LCl7scwKF6jmENqDjIABSLTKWFxp2tF2k7IbhY869QMv82jrD3hpvAaTXicEUKrhWf7s80bAPHXUBAbm2W5D4KMthzBsQttSKTmSndi2xmd65py0u3rlo9uDr1WPNthgXsAhB9VAm5StYxnUykur91KCyFSk5iSnZ5UiJbZutrRSBEOsYt8AeDgvbEhMaQBX_iThDpwUtZWEuO_epCTKODI6ydlB55s3n_BeRnLueIo9NE5zQhUoZXC6D02efqdn7-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/25319" target="_blank">📅 01:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25318">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2548666d77.mp4?token=HHZmx2qQ6P7IWhVYc0R--uJTS0BcvI9NtTW2qJTvC4oHtihEF6LxQ7vYYPhGvH0NrKCrDx3EJHNZB1fwTrrZWg4JmAuqUUHM7ZYmM-qT4TLu2hBtFAKg_Rye8NyDEzgoRu3NY_xuTdOx1BV0JLee6nZCXMB5Dsoau_lTwESjRO2a6XHC4hCCxscwW2CavIC7aRqH8YE6bk0CbsENw2HCGR6spEiZsAPJMiVZblhH93cBShbbsBXtAUO0L45Tn_XW3LGjmTAZCpE2sATfP_JzYIKAIt7y2n7cipgF4eBHY1JFy-vms4zPw-gatO_qySDYwlDTBKdIcKNKDa_yLae34Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2548666d77.mp4?token=HHZmx2qQ6P7IWhVYc0R--uJTS0BcvI9NtTW2qJTvC4oHtihEF6LxQ7vYYPhGvH0NrKCrDx3EJHNZB1fwTrrZWg4JmAuqUUHM7ZYmM-qT4TLu2hBtFAKg_Rye8NyDEzgoRu3NY_xuTdOx1BV0JLee6nZCXMB5Dsoau_lTwESjRO2a6XHC4hCCxscwW2CavIC7aRqH8YE6bk0CbsENw2HCGR6spEiZsAPJMiVZblhH93cBShbbsBXtAUO0L45Tn_XW3LGjmTAZCpE2sATfP_JzYIKAIt7y2n7cipgF4eBHY1JFy-vms4zPw-gatO_qySDYwlDTBKdIcKNKDa_yLae34Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
شما حتی خارج از زمین‌بازی‌هم لایق احترام هستی آقای کریس رونالدو؛ شخصیت بینظیر و قلب بزرگی که داری رو هرگز فراموش نخواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/25318" target="_blank">📅 01:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25317">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UeTn2y4FCeNArxqzwK5GajwTawPGg8jqiadF1iOhr28i9PAcphwSEgm3-HYPcsValwMqfzJBHxRIh_p9RNq3XPZhY9vCHrkw8j2yxI0htnjEVXaMdwxygj8ZZpMhytS_z5pZn1X3u8K87lxY-tppDRMZ8UXJbbUIz1AVhCiuvXQHjmnofL0LzGCfiTFkva3MBTalH0To_obOyHn_cxeYMRxGDE2MNDv1411E3MyGSoccNfICHXwIeg_Zpw15IdeqFyBXMCpUo1ju93soJRkfHqC1ll2Us-ej3PsDjoNY-OfMcaXchvE4wrzr-ZHaoN58k6jKvqZCsy31mqoM0458rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک‌کنم‌اگه‌هرشب‌با ۱۰۰ هزار تومن میومدین چنل بت ما شبی‌بالای ۲ میلیون‌سود‌کرده بودین‌مثل دیشب:)
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/25317" target="_blank">📅 01:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25316">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f822cfdb19.mp4?token=sAqwSgejvXdBvdUg9ara1W57uSfY8GSXLBpARAJ3NP6T84-McSbYYQDWo0R2o7BRs4n3xCRiMZ_IJY1zwXTgpO7szGU2-V69BCtcawkWO04fX2sFf9-u51DnQifsYNvc0Ji8lYDf_itNiNUiVCxDokGMq6m-x1pEMny3AxX4jQ5Oa7Nn4HuPhcUbHR_Z2mOgLIpw7mejZW_hZrw8G3kILX0IwvHcARc4mGg0RZoZVaLY5amExrv3AdFwO9eoSx5jR9_4EYvzmhOr-T2J-PeAXhane-GS70uvSJGY2CDnjQqqfHwgJXfpmAcwzzkiaNTmB7HnteV7W1TPhBzOvjv81g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f822cfdb19.mp4?token=sAqwSgejvXdBvdUg9ara1W57uSfY8GSXLBpARAJ3NP6T84-McSbYYQDWo0R2o7BRs4n3xCRiMZ_IJY1zwXTgpO7szGU2-V69BCtcawkWO04fX2sFf9-u51DnQifsYNvc0Ji8lYDf_itNiNUiVCxDokGMq6m-x1pEMny3AxX4jQ5Oa7Nn4HuPhcUbHR_Z2mOgLIpw7mejZW_hZrw8G3kILX0IwvHcARc4mGg0RZoZVaLY5amExrv3AdFwO9eoSx5jR9_4EYvzmhOr-T2J-PeAXhane-GS70uvSJGY2CDnjQqqfHwgJXfpmAcwzzkiaNTmB7HnteV7W1TPhBzOvjv81g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
دیکتاتور جبران کرد؛ سوپرگل دیدنی کیلیان امباپه دربازی‌امشب‌دوتیم‌فرانسه
🆚
مراکش؛ این 20 امین گل امباپه در تاریخ رقابت های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/25316" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25315">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43c42773d2.mp4?token=t8O9nEpLSKTDwkoSIhbWnim-ZQ1jZGJvB5VUcB6WpQ_wkrYphdRb_yt63-EpVIdJBsWP4J1NCv4TvFTxPLTrruBvZ_Tv3TXLeQuhIfID9Zx7LCjwOXqTanViiUQvvO7C6f1y0QO_HDC2Ea0BbB1bW_wxaxZc-aDAjklF_i_Y3UukLz2XLZcNly_6fl33y6ZjnYGS--dyvd54CB-gcS9skjtfaaMRxuZq7gg4Z7K-PQsTbwWf9kSw336Ci_BBXhmUG4kjw9ugit9c32QbvUUFJySYpPYDcS2AvFZz84UTjYbNMv6gh-LSMfWtAXwBJNb_5W8C0TOnlDbSmchmZ2pgWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43c42773d2.mp4?token=t8O9nEpLSKTDwkoSIhbWnim-ZQ1jZGJvB5VUcB6WpQ_wkrYphdRb_yt63-EpVIdJBsWP4J1NCv4TvFTxPLTrruBvZ_Tv3TXLeQuhIfID9Zx7LCjwOXqTanViiUQvvO7C6f1y0QO_HDC2Ea0BbB1bW_wxaxZc-aDAjklF_i_Y3UukLz2XLZcNly_6fl33y6ZjnYGS--dyvd54CB-gcS9skjtfaaMRxuZq7gg4Z7K-PQsTbwWf9kSw336Ci_BBXhmUG4kjw9ugit9c32QbvUUFJySYpPYDcS2AvFZz84UTjYbNMv6gh-LSMfWtAXwBJNb_5W8C0TOnlDbSmchmZ2pgWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇲🇦
🇫🇷
پنالتی‌از دست‌رفته کیلیان امباپه در بازی امشب مقابل‌مراکش؛ یاسین‌بونو بازهم پنالتی گرفت. ازهشت‌پنالتی‌اخیر که براش زده شده در جام جهانی تنها دوتاش گل شده. شش تاش رو به راحتی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/25315" target="_blank">📅 00:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25314">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6hHEn-0CgQlNFcP8vtzSkyzkOqi-CHe8ZUDb0T_J830JWsdxS7SZvX-vOSFmL6vRwzt3IqOzJBV-ju9pdr_fd3yoD_pzIAtiArBTWo71aAbm36z5pTAOwBkhz68pEJ-hK7umpnpI8c2Qj80RF7VLh8lvY2qDrsyTmGavs5BVRWif-0YphzvyphPHNXtOVPWVgbVOCDV2qoLcLXAa48Hn5-Bzp3FrSnpBoidASuRRoe4KEvkpb8K3-m4oof7pvyhUsc1L8CqO6BPm1YyN9QTVt4d4_X56fJYmVPRHP7LZCK0MOBgaZPI2qvIF7hucsEX7fDgGeKMVLs5eyzL5U6TpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇲🇦
🇫🇷
پنالتی‌از دست‌رفته کیلیان امباپه در بازی امشب مقابل‌مراکش؛ یاسین‌بونو بازهم پنالتی گرفت. ازهشت‌پنالتی‌اخیر که براش زده شده در جام جهانی تنها دوتاش گل شده. شش تاش رو به راحتی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/25314" target="_blank">📅 00:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25312">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwsQQdTyPzE-PN1-cnwCJjcFSIl1nBSZkfL2cJ1y82E2IYXH6e6Yma1C7M8C6H4KvNvw-AEhNCOvzjlR6ZSAP3gGGz_4ALA251vUegacMmkuWHjcjCi1MwtRvEBqSevhEwBkSVjiPMWDIXKe-6qT2V8ICU9VJcmJYroBE1rybe-nM1o9-mTIo3_LKVCLC7UBs6hccs9ZXm4EehskpAJVk8AP9T2mUr_166gtKJ-zoxI046UYmdWK1fS-cyujG1voGCDofaeievvLlvOJBpTivnngULGrhhgARIbrl_zciygnvXazCWhkN-HCYlbp69ZcCHiRBbecp1NAR7HlkrKyPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز خان کریمی برای کارشناسی مسابقه امشب مراکش - فرانسه رفته شبکه ماهواره‌ای جم اسپورت؛ خنده‌هاش رو ببینید دهن سرویس چه ذوقی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/25312" target="_blank">📅 00:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25311">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7769fa4e86.mp4?token=U7cUt8k2P3zUosnVn1t61AVBb4NVlXROcalbtXtWfFpOaiLzDfrvpk6SzPjCR37XJAIGg0Wwd4mnXch0dtN3Hbni3TQnCp86M12EcmBKcXvO5q6MQE4-j2NtIvDAw5JLqwFyBz6WKCnUqWtYW09ohWOZjMO5XAQhEDEPNmWLXpfKXCLFu4YtlKiMQZl6x9pHThBN9EBlYY3xBPughp12lZbpVaBT9pPhuRp4ns2uXyPM1qBS4jCquXSS6wtOqIRqECZu6-7boNbevyO_hvZp7qEwoWP8KPIhvdhECGRYpDDcM2NHTUorJrrVtTKcTiV0K7p8rrQRiC8XTENJpRdxqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7769fa4e86.mp4?token=U7cUt8k2P3zUosnVn1t61AVBb4NVlXROcalbtXtWfFpOaiLzDfrvpk6SzPjCR37XJAIGg0Wwd4mnXch0dtN3Hbni3TQnCp86M12EcmBKcXvO5q6MQE4-j2NtIvDAw5JLqwFyBz6WKCnUqWtYW09ohWOZjMO5XAQhEDEPNmWLXpfKXCLFu4YtlKiMQZl6x9pHThBN9EBlYY3xBPughp12lZbpVaBT9pPhuRp4ns2uXyPM1qBS4jCquXSS6wtOqIRqECZu6-7boNbevyO_hvZp7qEwoWP8KPIhvdhECGRYpDDcM2NHTUorJrrVtTKcTiV0K7p8rrQRiC8XTENJpRdxqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌هشتم نهایی‌جام‌جهانی 2026؛ شماتیک ترکیب دو تیم فرانسه - مراکش؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/25311" target="_blank">📅 00:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25310">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6Hn21ybijLjbJZk9Oi1tj4H5Cis1Qs8mnk7KuNKi2npNSJBvfRhOC-GQhBIYUjyOi7Q0qd0g_XUAoTeNAxUQKwnLKfglj6bfzPlpnY_AL_JooqfCJfIHOFnHNTJZKqP-ol1aPFQQdLFqfH-OVjaI2guwf8Az5Uoauo_8yCgumPKpgVgeZIvTWKfnnp9hsB-rl-eEHNyMoWjy4GmBzHxWBRhqlPDI8Rtedbm3-ILaigEnY4qN1625qOUxvwK0SUM7xnSSFIgS5u-gJFykYZssMC4fo6I8ua1zYoFaVTSSKC1sx3J8Lm_Oa0HbfUoWSv2sK8gG8Vsl4R13_66zNt1dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌گلزنان‌تاریخ‌مقدماتی جام جهانی در آسیا. علی دایی با 35 گل زده در صدر و سردار آزمون با 29 گل و کریم باقری با 28 گل در رتبه دوم و سوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/25310" target="_blank">📅 23:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25309">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJWN4WHzvvpTJ2RM72kMEU55xrjMMr26mXfxCOrCLSTW1cOvXCefK1xs6fDMXHyShcIR74BOeGucpLrRaJgy3lvMBfv8azgK1ctpoMxp-gF9T4bRAfKZPKsV8tnuxH8j8GRh4nZf9GWZBSNt5RHyQQeufUdTUEOdWvV161DDm2USvXXQv47xUR4WHhgV06p8fB0oKEVrGMCtUuwngfewS-wApfqamsE2nJYxggKt9W9ZKBe9jReXBxrOeQcNS6fiwotIyCoUSOQ-crmIXKz8ymwzqdiKoMR8z_MJJwg1YaXthBiR5J8QKHzG3KbRMndbYfe6y0_TRAq7_S5mL1utkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌ترانسفر مارکت؛ باشگاه پرسپولیس برای جذب پوریاشهرآبادی20ساله؛ سهیل صحرایی مدافع راست جوان‌خود + 500هزار دلار حدود 90 میلیارد تومان به باشگاه گل‌گهر سیرجان داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/25309" target="_blank">📅 23:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25308">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/de7wR_IrWchBMTkLJMj8QwG5_7NuUg3CL3CDwySq71eRAeoNxL4FqtV20vCWGxw_meIjxBwylZxRlA7avO4VC1eSeEWX9VrRqWZaeY5-WDmDXvG9-9O9nadZyjVWmVr8RDCnQxslvzDzvRQy9nOp2Rko7bPHppoKXX_IfQP_pzmFyiGhWH_RABwus664DjMX0Eml8m3i82NVgF6yCQJ-P2_z7RQTBQPRGUzBPARQ4fbtnyWQXPTJhHk2HYqao1EBEylY0MNb4zZxeATSGmxBbox0NtqBp11ekF4uUNB84TQ5rsmdf0YiQtebEeN9Q_F9E8quJtoSM544Abw1AqKXxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
این‌بخش صحبت های فیروز کریمی هم عالیه؛ میگن الهویی دستیار امیر قلعه‌نویی گفته ما هفت تا پلن داشتیم برای جام جهانی؟ مگه فیلم هندیه اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/25308" target="_blank">📅 23:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25307">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNfv7QzKRzban2yYHvKUatcDI1DjjXXrTS7WbtljXfVbWCAxj2I0874C-8FSzq2UP9SeC9YotqwcoBk3Dh9br125OEIHDwdpC8lJ0pvNDUZccA1T_clJXMsAFHD9TJpbZ3GtC75LzkCyS63pNsflOrKiLxX5kpTat_JntND77Axut9bJPuywSzEBOiga4Vi-GWqvqkSRe0NpOAnPvho_cIgqmVtlLqRDTGVtFmRzGXQYQzz3PX_K61F1YHBLizEjcNPv0jDkRi83eRliAu3yM7zi5F5Ne_brI1JIxkEkh2AaqCmNRM1ZrNbj0JkFxr_bQmDsytvBZDN8yvWoHbBQXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی دو روز پیش پرشیانا
🔴
پوریا شهرآبادی مهاجم جوان گل‌گهر با عقد قرار دادی چهار ساله رسما به‌باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/25307" target="_blank">📅 22:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25306">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FM9b3Nhk9xl7P1XE-IGdL1VoHNXBda1VcWgs2uVoV8-MjGdVoMtrkyn8hf5Mx8hxco0Uhuaz1LjPBb9P2n5Rb1FByYH1CTsvi8TwHu48k_OLJl8sJM6Wp8sfmR5tSgZ0rRacP82UVSp3gIsW4TUVMt8H0YY2ha91O6aiH2F_LcXQ9TUyyC9vckD3UdGIjHuFGR1H46GlADmyYOcNVEfElanH6Gzr6NWhaU2U_qINzsMkEEkF4v1_MMv3cbd_cuvT3AN9qvoDS38fyuwWX2GLn1vqYrIFXcMkon8oA5ofDODD3oFLy0fXXgRLeGEeWLpBlbjSKhTGKRF8ZnLierJlBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی‌پرشیانا؛ جلسه مدیر عامل پرسپولیس با مهدی ترابی در منزل این بازیکن برگزار شد و دقایقی‌قبل به اتمام رسید. مهدی ترابی برای عقد قرار داد 2+1 ساله با باشگاه پرسپولیس به توافق کامل رسید و به پیمان حدادی اعلام کرده درصورتیکه تا هفته آینده مشکل…</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25306" target="_blank">📅 22:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25304">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LeKkTxiQ5sIWuaXxsOD-4MmgVJ--kZKHPwP0OZwP8U4OJkHBBj_FFhX6do9G7QtAPmz_T9Xq30qXawyMFebV7je65nQ_0N_Ep_fzfwkCd7OINQQ5jO3RjM_514Q19c9L0N54PqJaPkCat9LseaLKRvzCfT_EYmQ4UfQX8Uzm97FwdGeRQxbjFd5IszEutvZ4PfakNEJ53Bqrm-HLMfvAWun0W8xK2inAlv8ddExsvPN4421f70XbvlVgmvJbzk5q2wxgV0vh1IFus7LYgfsts264AQoOfrfCPsqtslb7EMeVX0t2LVCsVc5oxwmLICVTUbeHTdhdtopabxsqXpxIug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kfWeZEDLvNFsVMItx_vTD7eqIUSb6dwRnoiIqVAcBIxDJ_i1rreo1MReJ0INp59qOTIFNqNFNq0rZ7MSEEfhvVLAntO1eF_hmh5SMNSDyR6VOoH_NfM0I7leyWZTkoG30LDGSUWW8XQZy9YFY5s64FDCGwGMzoTtzMfTB_0t5CIFYlOsj5WXwKk-fphc5pqDQIEWR6MYOuZyLfgFdo1aaytJzRSHPO1rrgb7G7GcJbxFybX-yI0mZOJOdd78uBm15709pQJpFvHhb-b_i2FxY-Qg44FO1tzQqbNoFKSZwtLZDFvfrVMFvjzvTdwVHgZo-tmkgX6-chXVJsUkjpCbBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
#تکمیلی؛ازترکیب دوتیم‌فرانسه-مراکش در جام جهانی 2022 فقط 9 بازیکن همچنان در این دو تیم باقی‌موندن. بقیه‌خداحافظی‌کرده‌اند از بازیهای ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25304" target="_blank">📅 22:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25303">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxfK14LyCWj9xZ0O0_yNeksymMnzVde7uZVENjG5uq1vROR4lk0poY7IzuqHz7UMLYJwlPHvO-lfo1DoyDSg7huHRepzPlVFI0qe3NFvBrlNShX5Jnh7b8tg97q7HCib51G24Dc3yxaKH9WQ4ntPXv7kIPAvVo2zueAzHuCf3x0R6ZnzmbYLzcT0UCV1e_IETJNPfNvenUQovVoS8kgG8MJyC7I9X3dPgBy341Eb_lQy0Olg53NjONObYARQhO3V_R7NdbxMKS_lWMUAlEfEpD_Gln5efa5VRtG22yeg_gjF5Udpc7O2f-iJ8W13BVBxw6kDBIgBtj5HJMhY1Ws2uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی‌پرشیانا؛ جلسه مدیر عامل پرسپولیس با مهدی ترابی در منزل این بازیکن برگزار شد و دقایقی‌قبل به اتمام رسید. مهدی ترابی برای عقد قرار داد 2+1 ساله با باشگاه پرسپولیس به توافق کامل رسید و به پیمان حدادی اعلام کرده درصورتیکه تا هفته آینده مشکل…</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/25303" target="_blank">📅 22:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25302">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZjg-bepTUOBdNybqIBPyh0r9CB07lBEpN7vO7mF4q0dv8daKIIcYlhrHXZ_GNy5GV3PkUPPWY_bsxjKlX-cG6cOU4KAspWBo0761VuwN6qPLjJ3DVPW-lfNVVBRCrSxu5fSotLTYSiZdbX4na06C23HmLaiAtpZYx79IRbwJSsqnb3ceE7ptcoSx4wJPa-kG3_yZ9MAVz6Bkf0A9UipWItdRCTO77IkaVjVQ0NHK20EhgCGdUIJ_WJmVsdJZ-MtrkVqgthWFZCbk9lU9YYOA3JwUa9po691I6dkTMGWqyRxZYbBes0pi1kF_4i5HzJeUHj9D67ddmcr4BPx6WDizQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جلسه‌مدیران باشگاه پرسپولیس با مهدی ترابی و نماینده اش شروع شده است. تا ساعات آینده تکلیف ترابی با مدیران باشگاه پرسپولیس مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/25302" target="_blank">📅 22:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25301">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJ6zhttKK9k0v2r6KUDd_HVDl0FbgEZ6ySjesXfUL2Njx2TL2GMMCP4TyWWdDUxxa1gawCoXYAhfSQ8m7LSQOQUf_zXvoORzAID6DqJ73Ne-EfdC1M16aG4aQRmNjPUfv84mAFjsrjLZ6WUeUb0B7_nYW5d8mK2KX97R58-TlPpS23LPiSm7L3x7mOt-ASIhv2JCIsirfX0e5-dtbKzViIdRxn-YKd8yShkUqwxU5UqR5DLEJdQKUCS-4d8HISugZDQvdE68HVpxwT8Jo1f-wehAzVwyo-x41igIYksNlYpbfyC5WddMtiyofuDR7Uw48bv1moHlRQZBOrl7A7nmzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دیدارامشب‌ دوتیم‌‌ ملی‌ مراکش
🆚
فرانسه در ¼ نهایی جام جهانی رو عادل در آپارات گزارش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/25301" target="_blank">📅 22:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25300">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxkjPg3ijis11g27MYenI-XglC70WSRUdRmvlDhX_MeOBCoxB3ASsYmCW7sdlhWpae9Y_arQ-K0hoc-uGsSuT2P1ERtd2pnCjyVLdaxldGa1ePWKkuB6Ovygi9U79Z9g41Q5CyMmSxbCJ4dcDJIkSXNHJYzLc9DMDGTHatDTAJE6WOx-K8-nZNhdHPbgna_Kfd0WGkRmS32ClchDo1OF7jxzcyBAQMbX6fUL25K-N7kEoqLRQgr02PuQBNzpL1irLSZJtdcoiGHooembfd60gswtMZ1_uLNbYByWZzRWAdpwmVyuxqy_kG6bKwNPrEkKcKJhiCwOTBw4BwRh9T216A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تقویم؛ بیست سال پیش همچین روزی ایتالیا با غلبه بر فرانسه در ضربات پنالتی قهرمان جهان شد. با این حال، این مسابقه همیشه به خاطر اشتباه فاحش زیدان و ضربه‌ سرش‌به‌ماتراتزی تو یادها باقی مونده.
‼️
زیدان: از همهٔ کودکانی که اون صحنه رو دیدند عذرخواهی میکنم. هیچ…</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25300" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25299">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bb2pG7iZEzqYAvzj-g_C0CSwGHBQ3aqueK8qO73k2M655S_ZtahGFSVgz4-96KJPmF5PW2TDta3oERZy5A6XDh9aZByujWMEVyvJRR6OnBcN3aZVpi1CNh9zQsD_AMXGshTSdgf-9CE2gU2V4KW_obGUezpoFAsfhPVA0lkfCP8Aahn289wbCmfapcf-Q_ZXmL2_5TUgO9xT495GCEq3PX9l3c6Tu1KgE-oOhXr_2kN7Po-f9qDTCYnCqRu5od8Sf72idM_XktgdXdt_OOhM0KesYrtqMN8hJ6W9A6YEDh5jTNl0YSmdLH-p34db0KKi0ddNN-O9guJJxJHlZRQMdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
باشگاه یوونتوس برای عقدقرارداد دو ساله با امیلیانو مارتینز دروازه‌بان تیم ملی آرژانتین به توافق کامل رسید و تنها توافق با آستون ویلا باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/25299" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25298">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKnKHpX-Ez0o1GJH3PyfAVOWTs5b16TFeyWS3AQ1oMGbtund922Fh_0TlN1QLv0PdXRUqf82NKFfigi516x8oxK1wT26O2ZM0k75JpMLXoLt-y1tkjuc_vNJwwe1UIN-tq3-bZPjVJoz9xaAiV2AMNzAa8XeD4BuC82oOOslXed3Z2mmXteBEZebch27dPejHRndzp8z5cytAPDbxkKkQKmwo5omseHsw3a0o8W4v7e9zJ4ldcaSnxY1LAP78zZkKbqy624BT9h_Yx4i99SBotm2V2aOdQtK9YiFDFcr3PIc8E9DZ8eIQaw8CrRU1vzZ940MoMtHA3DKTsZDPLVo1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
مراکش
🆚
🇫🇷
فرانسه
فکر می‌کنی کدوم تیم برنده می‌شه؟
👀
🎁
۵۰۰ دلار جایزه
بین تمام افرادی که نتیجه مسابقه را به‌درستی پیش‌بینی کنند، طبق قوانین سایت تقسیم می‌شود.
👇
همین حالا پیش‌بینی‌ات را ثبت کن:
https://t.me/betegram_bot?start=p4_r4EF37DCE
🎁
جایزه به‌صورت فری‌بت و مطابق قوانین سایت پرداخت می‌شود</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/25298" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25297">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYpcqdD6ByE2owceYe1wNzOxdzz444wBctYch08YV0HCGWUvRf8ThqzWaQ8kskHyIYiwTuMc4P978FaDP8GZxhtkHT2ZEyzNprm7A0SKsBfkGDbHyA_RHgxdWiXLQEfh6pWchlmEOCS7fXdpWuYOmowRFceLXo5AYznldtZogceyJCkOvewidk4DhoSZ5sP6ERQi7sSDeNgKiyUIvp5RZ5tcOaRRe_7g7ResM4GlpDVdIx6CtGxyvtquML4ZApQ8fTnpZOoI5CSvrLlWJozNXyh8hv-dAYu3c34uaTLn8xA5JFrzjB5ABGc9Qg5aYFHrg-39LDWDsFBI-jUCxYCNYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
طبق شنیده‌های رسانه پرشیانا؛ هفته آینده جلسه‌‌ای بین ایگور سرگیف و مدیریت باشگاه پرسپولیس برگزار خواهد شد تا مدیریت‌سرخ‌ها این بازیکن رو برای‌موندن دراین باشگاه برای فصل آینده متقاعد کنند. سرگیف بخاطر مسائل خانوادگی قصد داره فصل جدید رو در لیگ برتر ازبکستان…</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/25297" target="_blank">📅 21:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25296">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJ_ynT7dHsY1H_jPrZHJmTGp40vv7kJxXS94y2Rv3bA0N2hDGjvudy-TT3oPgbZf1HAKvXAsf_o0VzgwnJmcR9mpow1F-Os9DTxBGtJy-w69wMyXU2zhdbtMiUK05XULeweG0nUOKgh72mDZ9B4ZynTa4E9c9iEuZmwN2jwHIqeuJEPK-bQoUsQbosgcjWzAB20Oz9_B2y0TY0515idxU5A3n6w03q0mTrAWLOCT0KNstgZ4WgeA2LKly_P6BoHOjgGgJG5yFOFh45OBwxqRAFQxXIHkNPTX_dX2-R5oSXRUZu5bg5iyNPDXCx3gqTfz2-73Xse3rfb9uUcsWY6-iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
بنیامین تانیاهو
: راستش‌روکه بخواین لیونل مسی 39 سالشه و اون قبلاً هر چیزی که میخواست توی فوتبال به دست بیاره رو به دست آورده و بارها شجاعت و بزرگی‌خودش‌رو ثابت کرده. ولی واضحه که هنوز حرف‌های زیادی برای گفتن داره. من در جام جهانی طرفدار آرژانتین هستم؛ حالا از فردا بازی های آرژانتین از صداوسیما پخش نشد تعجب نکنید:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/25296" target="_blank">📅 20:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25295">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECd2-Pof3kcXpG-i23OY2bvcjPl3FbAQj0_5QxHpCep4qDI-Z_Kx-u8i9M3FA2ro33s5_oGNE53P60ORzjbz7Kio_wExNQjevN_ntnQssSMmfo-MIpNGCaYtegdiewnfj2ij0mBqgc2QCZ1molzjPgfMHnC3yFVJ1Pdd3wI3nXBCVYbsZ-RFdKJvh_wJQ5et1BE3t10MLQzNP6xHtFjGp274BQkpFX_BQVw6v4-5rJJoiK1mgdamm2qJ0ZlK46b6ZW9Efp6D0MxgeM6E9gniGlgy-WO7YRFGqzI63V6S7CavU4yufo0R5v2wlmXWJVisdm4mCjLONiCOklrsHtXojw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|داوید دخیا سنگربان اسپانیایی 35 ساله فصل‌گذشته فیورنتینا آمادگی خود را برای بازگشت‌به‌باشگاه منچستر یونایتد اعلام کرده‌. دخیا میخواد دو فصل در منچستر یونایتد بازی کنه و با پیراهن این تیم از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/25295" target="_blank">📅 20:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25294">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeR4EBglic-yaRXxYbZ8dvsCMLi5fGt36_XcYBTV-r6zoDMzIc47Ma8l03Fj31JqXu1ak_Vu3lOcVYCO-whAjiu0nIa0xo50FdTL2OdRkro_dcD8ZDkxoIVfuLmP-151Bkx-e_Quit0VlLmnRX6e7tcqdU4AgdQQZfFq3Wp2i6HdDgJgyBfNoJ4puH1gACJtwPetixUGFpIdgTKlqOt9U4sw0FqKAbD06FDGOKfIzsyKQgEaXBxl9fwUnwClJnjXxLIIJmVStmdklJvJTwvHnEDY03MQ2MoLhuYnHFVKtlFop1vSR8HWqO_UVrjmUvUgp4dcaHizNRscXhF6ZlSFrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ طبق اخبار دریافتی پرشیانا؛فرداشب‌حوالی‌ساعت 21:00 مدیر عامل باشگاه پرسپولیس در منزل مهدی ترابی جلسه مهم و سرنوشت‌سازی خواهد داشت و احتمال اینکه قرارداد 2+1 ساله امضا شود بسیار زیاد است.
‼️
پ.ن: دیگه داریم لحظه تمام اخبار داغ نقل…</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25294" target="_blank">📅 20:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25293">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ScvYfv3Yx6mnjabDVqa1eNDtyKS1gC29sUi3PMM44ATiiAWDq5YeudvqHvvILNnrKJ3YTgV2xvegCiHx3Si_3PSgGRNGFJ3-kZSasXUoIni59YjyXXL3aKJD8BFbVqUGTaVZOG4KJUfQFa1BpohCTu-6kXTvoKJ_Sibn7YcrLoC7FLCrbrAWVe7poFYynCjiLmSvwruEONVbsruUVkIQ5JC6702nI3tJ3IabJWxwwT8PIF6BqaryuR1QIoZWs_fczl8PjDBu9BxTuzdrW5cJt9pubSm-uRsAOh1Gtjd9BOUE6PhDRE0Chj88rpOPakZym2cL1rPqL_GX-l2wBXhphA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امید ابراهیمی هافبک 39 ساله سابق استقلال با عقد قراردادی یک ساله به تیم لوسیل قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/25293" target="_blank">📅 20:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25292">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFvXvokSLGOoMOQmFrta65oZGnSrEd6DpChpJotJBYtvskj1BpzS8NRuL0NBiVRDF49X25QG3n_AhFPy9nTCi6cVFgG-gE2Cz98hlrxaQReJR_kQ3M_TJ32kab35qRF5CEfkTXiXt226lmxepJ-tTB5cWt_0cAQfM2aNpE-VsIVA2SCBPtDB4ezzA8Bnq_gg45JUJbtpvgGrFkbVGbjS-umWjxOMy8h7SpJxnmBg71h4uudBvJ2oYj31li5-Ea3qEb0realGecUpmjVTk6B-6Dc97C2378Pzu63cCvkZZRDB_-w9OKLCSY4Qzq8FxRV9TcE2maS4iOLEsobTqvqd8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هادی حبیبی نژاد قبل از اومدن تارتار مذاکرات مثبتی باسران‌پرسپولیس‌داشت امابعد اومدن تارتار و درخواست جذب مهدی‌ترابی دیگر قید این بازیکن رو زدند و او با قراردادی دو ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/25292" target="_blank">📅 19:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25291">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHtOjfueuSWi1I9R12MDz-lc8RJMYOXZPvkxXsPS1QKaGJJeEFP_-v1zDjATQEFy5dcyzO3GvojvusSLbo_K4HTOkbkSlY1qJrcghg-tiFhbM4SsppJl1XkmKLf2Mpf1C__9CsrfFuXOAylBdJE-csHyiiaU3gLz3r2w4p--XB3iVVmgWwMdHN_hDqCKGgZPjIDrRKYLYSiKqpF9Pd48rQmP1qi3t13QvNw1Bhznz-Ydd71Ba7bcEu_VeK-6oDOzXPInGNSlIgMveVWYe_-6ibV9Hdm90w9c1a31x1amJfUh_f-9u4paXestd4j72rf_Xyst9VlYS9GkpTBL19i8hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیرورزشی باشگاه‌الوحده به محمد قربانی گفته هرباشگاه ایرانی دو میلیون دلار پرداخت کنه رضایت نامه ات رو براشون صادر میکنیم. همانطور که دیروز گفتیم باشگاه پرسپولیس گفته ما تا 1.5 میلیون دلار حاضریم بابت رضایت نامه پرداخت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25291" target="_blank">📅 19:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25290">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAlUVh6LW_fHUaYfonn3SkLEgkcdqkg0cuK8l5Yy3WzYxMjvyrXLvx6LS6Y3YObvQGMarAX2kNErcLgQQKrHCd6aGeJGYRQyHgeobPX-ofZeOZfH1KJiE2kFJeDAhR1C8NokgpI7hMVynFwalUN5Wts3cxVJH-ZMvGLEYGkjTF0vsnRRqf_pajUgfCjAEJaOv20CjNDwynjdWQULr15GuVZrUKXp9FLXDOUMZf2gccWx2S1AqoVcuj1OdqYzkeckL3uwM_u7tgDTTO0VelN53Q2_5ZsMamOruh6UuTIj34Bi803-H0cQs6UQkZ1HZDQ97GXpcDDkbivNUVf_LfODJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
تونی‌کروس اسطوره باشگاه رئال مادرید:
مردم همیشه دنبال‌بهانه‌اند. تکلیف‌فوتبال‌در ۹۰ دقیقه تعیین می‌شود، نه یک‌لحظه. مصر نیمه‌اول عالی بود اما بعد از اینکه ۲-۰ پیش‌افتاد کنترل‌را از دست‌داد و آرژانتین استفاده کرد. این تخصص تیم‌های نخبه است.
🔵
مردم مدام درمورد داور و VAR صحبت می‌کنند، اما دلیل‌بازگشت‌آرژانتینی‌ها کیفیت و ذهنیت‌شان بود. مصر نتوانست‌سطحی‌که ابتدا نشان داده بود را حفظ کند. اینکه مسابقه "دزدیده شده" یا به آرژانتین هدیه داده شده تئوری‌ توطئه است.
🔵
بخش‌سخت‌فوتبال پس از باخت، پذیرفتن اینه که حریف بهتربوده. آرژانتین‌شایسته تقدیره. مصر باید به عملکردش افتخارکند اما از اشتباهاتی که برایش گران تمام شد، درس بگیرد. فوتبال همین است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25290" target="_blank">📅 18:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25289">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1cjNnMDqGQN6jaDkV1KiyOqbkxa-bQiL_yMTqguFgNX0QY2gjjyNGplJCNlcOtLUmNuwk1Tk52pej-OTYawr80n8NwfstWjPB9HMGUVitiFGWbW28E0KZsiDanl1JL6UaHMQ_GNPC91AJYhOs4qZ80uK2JBgXXEKw_ezJqvV_yTRxFLSztuHtvtliistFWewrwIKqXOEGNv1Bi4mf3GSVKdiVtCP9wzC3dc-Cq7fgJlCoQ5ZUXS52OwMNe-8CM31Axfk8lMglt2b_3bSpyYBf0_EApWMn9I4TTm1lrgcnC3PLxz_z5VHseVgWFfBy38lVK0Cr2reQvF2fDCr8OXxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25289" target="_blank">📅 18:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25288">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLmSWz6LmaninzjHlO7Br80VIc3RQEp_QQ7DFTUZSMuCwXz_df_n1wTboWwVMWHtqCddebo30Gzpg3LoOqDrYyD3uD-qUrAlD0ON47H1a8dPCqcqrp8Eiopqtx_jssf9NZ0KJ0_t3NZGJBqUiFyRKhlLCreuY8ok1i6PFvdTI_EPCGvOd1TEr3HYT8_paAcgu8xOtWrRRVNmxWHXAQ2bDisvAtTXZUP69uEz2dlwnuNPU71tscGqPUZ3gvN4FqtmAI87q4E0Ns0035JgE-p9lttAQo3VYMLyuBhRPtv9XGGnchTruKAoiPDnwz7UpcJCxow4qrithLnqgpnn7346Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تقویم
؛ بیست سال پیش همچین روزی ایتالیا با غلبه بر فرانسه در ضربات پنالتی قهرمان جهان شد. با این حال، این مسابقه همیشه به خاطر اشتباه فاحش زیدان و ضربه‌ سرش‌به‌ماتراتزی تو یادها باقی مونده.
‼️
زیدان: از همهٔ کودکانی که اون صحنه رو دیدند عذرخواهی میکنم. هیچ توجیهی برای اون کار ندارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/25288" target="_blank">📅 18:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25287">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTdbAIaNw9r-p2W6mW_Igkmr6jzvmYPFamVM0g255S58GJ1sRUdW_O20Y2H-kIHEGznrtiUSCfAvuz22UYqZ1068-pmVlHo4eHrMkotyAzdSqNRoTtplH3kVKvcYNeCR5TEHFGGwCGXHvRerLcU8TzVFbOewzjNS9qKuKN1iU1TSzDF7jZ_8SYqyBAbOhvxtnnzrwO2UkV2G-7QPdmmE0kiV98I88lGuGbeyU7YRLORNyp0rtp7hLW3GsQU2V4irGR2shexXva2-WqPglU78YWanYnoEJK5q3omUAHWBJANxTDDcEDvuqJLhxK9OC8MK_n7fiEYNw6f2UK08y5MRsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ طبق‌شنیده‌های پرشیانا؛ مدیریت باشگاه سپاهان درتماس بامدبربرنامه های علی نعمتی خواستار جذب این‌مدافع ملی پوش شده و به نعمتی اعلام‌کرده‌حاضره‌برای دوفصل‌حضور دراین تیم رقم مدنظرش که 150میلیاردتومانه روبه‌او پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/25287" target="_blank">📅 17:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25286">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdPVG0L4uYYkQ1KResI9-9nKkwCanzg2bTdgXbs3p0XrFm6qiuHa7n9NascHGkTdEsWPNefGy6FurRyCnDAIFkXdfX1ZPUibcCRXwxa8ydfZjgFnHPUvwrx6fj3hj__7Rj7ezRU0KqxSdG8krdv1BF86i04tLMsZP4QUv2JuoPU77xy6gP_fYCscpdDtEIrtZLqJ9o4MyQM8w2vNmWCHYy_o5UZitKCsVCp17Qouis8ITN-gGYZU2mF4bw2HG5arz3HJuzzVL6E29uQBcRP65YzU-o8cl5Vz7Ttf9JQestBpwH7_82VkuA0YkrJZ1cE7bwJ_9Rad7I-j0uzkFokErw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
درخصوص اوستون اورونوف هم پنج روز پیش خبردادیم که چندپیشنهاد از جمله پیشنهاد الشمال رو‌ی‌میز مدیریت‌سرخ‌ها قرار داره و با توجه به‌ چراغ سبز مهدی تارتار برای فروش ستاره ازبکی درصورت پیشنهاد مالی مناسب؛ احتمال جدایی اوستون اورونوف از جمع سرخ ها وجود داره.…</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/25286" target="_blank">📅 17:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25285">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLqSS4bCHfl0JHmNNEYWwrZSkHWFvbUWWyLzb34ST5i3hQptmzjk5imn3ji6V304jJFaZH2Vj3gGHBSrCAX47oPXJYbVV07Z_VsqJWWri5sX-b-s37QyelVMFEg57ygMgXFexo0HyfFB0lGC9Enyaeb9Ev712bzyO9VzZi5VwlR2JdDL4gpayDsT6totAoVodz1kQk8-bASc9gkPd5OFURwmpzfLC1IYNCYTPVpHvgoAGnyVR7_vbt8ofSycEU70OsikEE99Rjh2AYAuHkf4FXAL2rEwaifxUfuS17PNndjvhwZH-w21s2d4e-R8VO7LGRyR2LnSJWvdD-TpTlWw_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
ارلینگ هالند روزانه 6 وعده‌غذا میخوره و حدود 6000 کالری مصرف‌میکنه معادل 24 چیزبرگر. هالند عمدتاً به‌مرغ،پاستا، استیک، ماهی، سبزیجات و عسل علاقه داره و بیشتر آب مینوشه و ازتمام خوراکی‌‌های شکردار اجتناب می‌کنه. جاشوا کینگ هم تیمی سابق هالند گفت اون مثل یه خرس غذا می خوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/25285" target="_blank">📅 17:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25284">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">💛
هنوز توی MelBet با این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
بعد میاید سوال میکنید کدوم سایت معتبره
❗️
👀
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
✔️
🎚️
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/25284" target="_blank">📅 17:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25283">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pe-AjBm7iTMPK54zOWjFi10VKKvC7nujqdyMEDHITywXtymBucn8bNX9JxrT4-5S1dMe3p5uBZSM78lzWRFGrx6pPYNc4rPxDGGtUrYaYV3oqY4_o1C19W87WqLHn7a3f1sVjS9IrmNpiVz5KR78n99uIvQw0LiwcSt8tcmPZUCzPhckaDXKSNXGksuCeoOFzNGN-yZSHSl0OCBw7jsM0B9GLdxYJMgw0EQJvH9mHMLg9XHLKb1q5LrrBMYatZubkMJ3F8-YF8SWp7HZL8luO7KaYUeYrBtPHRJeRS68D9z5aFBOMEitnVQGbugOQP-SDB9YG84PgONxCSkmGoOrSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
جواب‌ فوق‌ العاده رونالدو به‌ سوال خبرنگاری که گفته بود میتونی‌ اسپانیا رو ببری: من تموم تلاشم رو بکار میبرم تاوجدانم‌راحت باشه حالا هرچی شد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/25283" target="_blank">📅 17:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25282">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbvPi6O9SIFuTV0SSXUBRn92tH6EwX7ckRhSrUTiSUbIEsC_eH9w2jmxpAax3kJ2v1d3a5p1IfObmewhAacgDdnrMYR2mCnKtKbHWxcJVMOUdKm1UCLT508jQsjjcO2oicRxeUm5Uok9D7Sep-ERk--dCf9YMJmiCyQS8TRJ3D40hi1n9jr2F4eNfAlexcYp5nsGRrJ8rgk6_ugvn_KPpHJaS7acvH2HY7-OzYl9r6Soz-U0OVFlzlske_h1HKW1Cp9JLKrGjj2lOois-eQFe8YU35wLVYopZHjp2IKADGlsF0vnVMVyfHBzPELrLS2hat176gzjp8ZST2yLNAFvwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی دو روز پیش پرشیانا
🔴
پوریا شهرآبادی مهاجم جوان گل‌گهر با عقد قرار دادی چهار ساله رسما به‌باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25282" target="_blank">📅 16:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25281">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVIKb1HbMI43dGkKS4lYIjfOCbkpztzZqjvOw8oaJ9-m_WNRh_qXDqRCQ8fUGL7ga2StwSN2EUV6NiARW7oto6McuhudYxk4ztHpm3ZEHwexlC3Uy4lak7Toc5sVOh-IcTh-JQr11rROQkfyBWXbOdHQY7wfnx1or5BSuFxoFxYcGfLvoHnnms_aJ7l0UiQY603X4httnOzPTK3FeMtQSXbl46vvdztB3uxY44i1Bx0t2cap29iIsWka0ZXjAXRLfVzQ4Hmt9f9g-QSkA9rFUuPjRNPL9Pg08zWrQuFpvwqTQFL9u934xA9GfVQvS4dCryo4NFPWZSNnG_IXsGjIrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ پیرو خبر روز گذشته پرشیانا؛ پوریا شهرآبادی مهاجم 20 ساله تیم گل گهر سیرجان دقایقی‌قبل درتماس با مهدی تارتار اعلام کرده که قید حضور در تیم استقلال رو زده و اماده عقد قرارداد با باشگاه پرسپولیسه. بدین ترتیب شهر آبادی ظرف 48 ساعت آینده با حضور درساختمان‌باشگاه…</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25281" target="_blank">📅 16:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25280">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‼️
رونمایی‌از تاکتیک‌اصلی تیم قلعه نویی در رقابت های جام جهانی 2026 که سه مساوی بدست آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25280" target="_blank">📅 16:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25279">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BusTLhoQi49vkjPFwji7pimaUS6g2U-zFLxiqGRKYJ0ri_kOabDmJ9yiWuKn_ADDc0BzYOGwqtzoXWC2U8dnr5H8P4-4M8ttJg32jvNKMXhoUTTLCD6mfiQlNW3-kDhIJdnKgksu8pKvbczBSejznhQRorHS5h62c-R-AhgiiqpSoBFbyVjMoZP11oqYRRLcClhGYFaQLfAivRBtRLFSULCcU9tEDgVxZUImWjN1w9MNu_YP4I82nXSrZOyeoQBLRdVBS-GRR05f1rRs-0Y5uwLky7qy5c78a-G4iSM0D5gx63jq0o9ND9EvkV3PuVlkyvBm4ipv3swH0-NuMsoljQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدیو لو رفته از کلاس‌درس‌محرمانه امیر قلعه نویی برای سرمربیان آلمان، هلند، ژاپن و برزیل در خانه‌اش بعد از حذف این تیم‌ها از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25279" target="_blank">📅 15:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25278">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQeNcIE69DBOVfz5LeAsMIWpx8k8A2L5tBU2gxcp77dmgjU_PTUbsN5VgSg2LyFy1BRLWAxIAxIBKEnf_jyhcuERliBHa9aJkQwdyt1rERsgvNxFb6SnB8gchzKZmp3B-SjX8oeqmy51gMFVZZMwjCwNWeHFD116MUZnqbfJJHEZEPPDklLOISJMWcLHzMM0Q7QwLbQaTwDgtqIF-r-itySyeApcvRUiR-zar1kWfkMeYz5uy8pKNaRSmUd0o12Sg4a2X61waKjwmKXj25k-J5zyNYRtUhaPgdkTst8twDxfKd7-u1wOqjU3KuYfyMdQUioVw4pkpvH9gOa4gIVGQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛مدیریت‌باشگاه‌استقلال میخواد بعد از تمدیدقرارداد یاسر آسانی قرارداد رستم آشورماتف مدافع 28 ساله خود را نیز تا سال 2029 تمدید کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/25278" target="_blank">📅 15:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25277">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELwrg7mBcYqk1aFynzcwWeOhoXsTR7ToCdBFYDGng41Brg22PCrb-2-QC9P_7_Y6TGxhbBmZL_Z78WoSO77HZMI-a-H-u8G9AWXhYEfZwY5VlKAKreAiKcI6VN5ZV4WNt71UCBL12sVrRLrBJ7lBSQOCcc1kwnDRvgZfAQU2Q3Te_r8XB0awSJ1w-e3u8wvch1Gko2OdOkUOhoACFL6aANgrwgL1aXmbd-MynBB2f8JscFsbO9uRBrT-_62dEjZ7b0YF8RgxNTWfMaktuD6Ins3elS9XNFmMHz6zcjlQ-_csdVtPbP9yjHNJob-niQSVoN5VTDpegCK5cwXCPM6H1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
#تکمیلی؛ کریم آدیمی ستاره23ساله بورسیا دورتموند برای عقدقرارداد پنج‌ساله با سران بارسا به توافق نهایی رسیده و تنها توافق با مدیران دورتموند باقی مونده که باتوجه به علاقه آدیمی برای پیوستن به بارسا بزودی بند فسخ او رو فعال خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25277" target="_blank">📅 15:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25276">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIERGxK67a_glUorlrjSi-tHF8NfgCFRIR2o60Uu9RDYKiDftg2c34YCpzAM9NKjzbuLOHKfa7eykx3DU-ggaBYGuARCR6FuOqD9UnX4LeGZO1FTVRZpKqL2ABv2mjTVuvx7PA0wL3Napdvv7GF2QeFUu8Fg2P4LoedR3jZ0QJa5am0ApPk5_NKOPi1b1nN55KcPlwQemlhWFsS5EJFd8gxaUp3SdDOB51ZGKFw_PwGbMtFOZLnaDSgVPPFPQvEap9Fq0TBg-VrkuQ0sdS2xw138f22B4J-q6fy4hkC4t8rXiyc9EavYk-V7pOBebfuvnkKkOZUhcoPt5ZoIohPN8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25276" target="_blank">📅 15:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25275">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqLCM349DB4rgLqLPtSpYTG8QxS51Lj65tKeERZjVyQC_cMSy01W1oTZTXm_gTpbCZPn9W33YM23TY5RCGKTPx1k6QWBVwejuYom5eYwppcKE1S4_Ylb8427I8S0idg3antTaNur2U-JlO1ipav_xmgibPd-8VZDHg8FFkGkFc1ExNR4-XzLhoWlqzOGN7ZLQZZQuU-ozfZ3YsEVNJVUDgTluBzxH8KJSRdoUYJB2zVi7OTKIqHJBDJhAVrySN_BUzSqh5xRqDN1Zq-9-ANymxDzSrp7QhvHStq4v7NhLU4g__hdK7FY02AQ50-yvSpxzXPogFAuHwAJ5NbWL_vfRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی؛ ایگور سرگیف مهاجم ازبکستانی تیم پرسپولیس‌نیز درگفتگوبارسانه‌های ازبکستانی اعلام کرد که به قراردادش با سرخ‌ها پایبند خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25275" target="_blank">📅 15:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25274">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCnU7Aj4DE4yUeHTVQZ6n2VIXOpJQGMBhK8u58xm1W5QKGc3KXYpHuQgUYbh45-0fZbhGum-61PuA_56JFH0znbXKXbiY4Fxb_IYv1assaYU0lW9hO5v3lxzOfyKhXLzlJQzbSWn7PB7-7dqGg7W5cfoLqM-u7Bb6xhdDeCKC2Ndn3z8triFNIthDyFwspTMDvrhKcpEyc-M9v8YBj3uTjgfNPTcFs9pIT0tR-OMDQIR-ql8UiYlomJIdETlqpJ5BcyBfQtxQIa68S28bHIDSZIIQ_K_GQn-iuaMtg5Zc22TlzScY65FoI18Q5HPtOCMswUMhDAVRY82A-P5CWIv4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
آمار فینیشینگ و ایجاد موقعیت بازیکنان جام جهانی؛
همه چیز خوبه تا زمانی که گوشه راست بالا رونگاه‌نکنید. رامین‌رضاییان هم تو این لیست هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25274" target="_blank">📅 14:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25273">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MO-whJsIdREZfgVKMAOTXouB9o0xI8eznjShLeuNlUj855D3X7Jhpn5UvNr4f8_n2VDqshWjr77Eq-3pjSpVZsBGD7c-I1xeiNFVE8kbHhM7xpHLiLYY5MLActgDo17Q_yrmgss_e1iMKiiRbeoExn5Eq8lJCj13YwKbyGi-wI2I5ELuPNDQMWHhtAQtP6ScHNIcl_AAPNkjGkDicukUPUasldt339aWmfwaOEsW2XS7Fnwm1J3fZPZwzZG9ZCX98n70fT-EzPROcjepPK8wzw37xQh0L_HWPACqs_4kkxzs62L7ByX50czxLtxyHi6OL1pG_4TsG1qOitWPtbDqDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25273" target="_blank">📅 14:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25272">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWLZ74nBrCAfcajHB8gV75V1yx3WMmay9q7xVzhWqaZfH_gYcqW1l3-sIuPwKyiTR-4Hsk7zogOfjsQz5k1KOn0mUEaFRGQO9lTQ0NgOC9YSEjisrLz5dS3iBoVFzH5PROsEEn1u8YOqweB0GaKIcGBP-ifZW3J74cRy3IZygzort_um-uv_656Xi3DiTWJ3Hk_sM3BJIavaxxb_GPWKfknwATilGXRW9DjYUPuTEv4spD34b4U0Lvcmvmr0Kwi8oH_DJoDvtUNVPKszecvWIXPgOfReopdGuWgbvFz04K_B2Kv01ujbbUhKcbSgu_hbcmLsTAHHiGfegBvHgbptLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا؛ علیرضا کوشکی فصل آینده در استقلال خواهد بود. تمام‌توافقات برای تمدید قراردادش‌ انجام‌ شده و بزودی‌راهی ساختمان باشگاه خواهد شد تا قراردادش رو سه ساله تمدید کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25272" target="_blank">📅 13:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25271">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoLdsR9b-moEF9pD-SJgbpjL85AaQUTLcQkpO3hPJJn3urkbZY88FOVfGxtcz-FI81UZe0AF9mcA3rXC8e_3WNhImxJtVvA5jHi070e6yQm4agbhqT2JY6SCPBptfwi3WQH4EjojcyR1ql0HzWMkIQyWlw0aqnbO4M1_L2KTe73C4Dkx9za291XqsIYQvT6cEx77x4IftSMHBc474eFOL1WBOE4hh2jidwM88pomjO46uPu3DFLke9B5_7NtI2cLZXEkOWckqmm_QPXWM6YGMktS01CO_rO9EaYKJFWkwpHFoI9enbD51xDp4Se4ys6KW5EyZqH9MiyrOsWwpa4Tqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه استقلال باشخص امید نورافکن برای عقد قراردادی 3 ساله به توافق کامل رسیده و هافبک سابق استقلالی‌ ها برای بازگشت به این تیم منتطربازشدن پنجره آبی‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25271" target="_blank">📅 13:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25270">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwXAVNyWBLd012DIc8pBKPsVr8qppB4iaxNkUyo8qlb95T_DQliBfRiyGmDeDmypjKbDjrC0s9Nl41zEm6TjLzX4oHu7O3uP9KX6qorvBi6LqNMfeI8bSbLfXovcsucUxWgh2rEgOEknCKry43O_RRatL-UrqsJqbRehlD4QfM1do7D_djvsF04O8XIQUYJiWz-uth6twCayy6oRkaQBhnK_Z6CmrbxWRvjJDCSU6a3Hn4_ZHJ-iRpNex7yRUv_kLDEhzD22ap3J0mJCyz2xYOjD4hH8YUfZjezjabig6apIqfqDPMnsYMxUHFV3aebJuO4WuHT1yuOBDqur2reT8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
باشگاه یوونتوس برای عقدقرارداد دو ساله با امیلیانو مارتینز دروازه‌بان تیم ملی آرژانتین به توافق کامل رسید و تنها توافق با آستون ویلا باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25270" target="_blank">📅 13:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25269">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ug6LDG4XK5VUlaEFHJ-7MKX27T9c8vnUtjbmo0BnLjzSxPOSJ_Di7k_DFsY-5g9aVjNLpub7nP-CqyDxvN9yOWFXpcOCGkBcMgSxkx4WXZFhurXza9WBItyk6MScC33hPcTt0YLztYLkB-CzWPiM8kzA-yxutEOUrRZ2aUBIAfihq4Q5mmI_UvTsi5ozdKmPpSlvgMt0yajXmSUm4Gb4GgpknnOBkmbeGRt-G4IojvJEkEbtBsSMe0mmCzi-O2rVndKpA8bOem0uCDQjkhec8p02ns2J_Nk0U1beFJbIzbY3ENYIYGL1mjepHK3-7Cx-bjPT2y8P-_4nMCNOMLoAcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
کریم آدیمی‌درسال۲۰۲۱: بارسلونا یکی‌از بهترین باشگاه‌های جهان است و برای من مایه افتخار است که‌آن‌ها خواهان جذب من هستند. در خودم میبینم روزی به این باشگاه بزرگ بپیوندم و بدرخشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25269" target="_blank">📅 12:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25268">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttcBq5lWVVQZodwHPwaY1xxUNRnDvTTFreE4kBUTv_gNFdPgCWIZuKK5q0HRJio22haIstfM3vKXPSmVCnR0d7u00N0LWONuuGa96SsKFKaQJQwy39uyTBw5lVUViR0TXFqdqUxYhwZRbP48P5kG28bb6dR1jGzoXbP7bqoSTYt7F3xo1q6CJ1yvtLVo-YvqcNFN6A8WBlXeTPfvtMbLiV_LWfqHUtk0AzQfLbcT1PHk9WW_yMkmzPlmnirHl90tIYx5e1MB7nEnXt_KZ-TzefAjHLbaiWYCUDcCmw-t-b9mHSa7TbiwY1uEo6eclomsOndbNOtReZIE4lU75jR5Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آپدیت‌عملکردکلی لئو مسی فوق‌ستاره آرژانتینی 39 ساله فوتبال جهان در کل دوران حرفه ای خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25268" target="_blank">📅 12:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25267">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30af4fbd6d.mp4?token=bQffeR4u65TWzM1RscW2NpMBC1EvGFPzskC8nf2Fx4LSH0TWoPOYqCxOVgMkhcFKg8YJWwxhVF5H1zXrQdIUWHcu4LQl0W0i3-zG-oaPt7K32ZHvAt8xuh6fRI8Rk3oT5qgqUcF1PRc8D8Kx-975fpLw3bXaoW8nW9oezIr58jVqYc2neM9Qfwde9K2WyLPaQ7R4PzKe2xvcD0DRq6Ig_DOdF2762zQzNh99TREVXVqwNDa5fbSEAPkb7wDwK_MpXL4dIVxTvPIIiwsxB8qsBMRiz7XU5dgacjpT1Xkc0kzeI1jN7y902LsWXMSgwALjJbfp9X-UqRQU4YthHD7Upg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30af4fbd6d.mp4?token=bQffeR4u65TWzM1RscW2NpMBC1EvGFPzskC8nf2Fx4LSH0TWoPOYqCxOVgMkhcFKg8YJWwxhVF5H1zXrQdIUWHcu4LQl0W0i3-zG-oaPt7K32ZHvAt8xuh6fRI8Rk3oT5qgqUcF1PRc8D8Kx-975fpLw3bXaoW8nW9oezIr58jVqYc2neM9Qfwde9K2WyLPaQ7R4PzKe2xvcD0DRq6Ig_DOdF2762zQzNh99TREVXVqwNDa5fbSEAPkb7wDwK_MpXL4dIVxTvPIIiwsxB8qsBMRiz7XU5dgacjpT1Xkc0kzeI1jN7y902LsWXMSgwALjJbfp9X-UqRQU4YthHD7Upg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
جواب‌ فوق‌ العاده رونالدو به‌ سوال خبرنگاری که گفته بود میتونی‌ اسپانیا رو ببری: من تموم تلاشم رو بکار میبرم تاوجدانم‌راحت باشه حالا هرچی شد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25267" target="_blank">📅 12:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25266">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afyZtn1nGjIS-bLMvV8QlhwZvrCnnfQ4gJlOGVtlxInvXBjClSyP2Mh_oKLZ-a1j7u80JG8K2hmNcKmH-9Tf6Pzc5sorYdKpT8L43Uza9uVA_hqfWx3fptUGcAIFImkBOLN9lbkD8FYjSzuh-UN-lx1kivuzZzoPqRBiRLXscGDbpXSP9N8eCWUPRzRvvCHV3RekREdJRyWAaiu2ezYFOuzd9MZC2hbyxQVAmB2PFD8bsqzsZadbiEMx6YABKnjyAqUUWHHWK8mypJqkp3YgCiLcB8pA37714Xf3ibNMMPG4M1dXwi6fwEccchr-CpbhgoDtfvEDHbXKV8blozsMvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛آمادگی پرسپولیسی‌ها برای‌ پرداخت رضایت نامه قربانی ستاره الوحده.
🔴
باشگاه پرسپولیس ساعاتی‌قبل‌باارسال‌نامه ای به باشگاه الوحده امارات اعلام کرده تا 1.5 میلیون دلار حاضر است برای رضایت نامه محمد قربانی پرداخت کند. اماراتی‌ها 2 میلیون دلاربرای…</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25266" target="_blank">📅 11:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25265">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYPitKmrCLwXGMisI5Yo3gQDmJvAQoYF5ddHl4t_7YhgHuMOnVtpjMCX9ltrqiMBLIirBzkezCj6ljOFRAaGAE22WI_9t3dp_trzvBPyj2IWl6PwCak0DYkJZ4LYDCn6oOFb2uHBG84BgY_y_XvDJfIAOCh_BehCEm6kbn3cZWWw1panmwP9VhoNowpfDmqKUEDv_xmSNKovD60FKx_OUVq2ud7eet-DHwjSRX2IAA6AcG9k-ny4hZ7GXONMScQsJFDrAVi7GJ5L1QBAoryrR3B4oOQG3p-jHq9tH2OzcuecjHE6ZuuBldeqWSFkR8Z8jW5AHEryeUK0qF7FC7ofTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇳🇴
پدر ارلینگ‌هالند ستاره‌نروژی منچسترسیتی: شاید روزی در آینده نچندان دور هالند رو در تیم رئال ببینیم. ممکن است اتفاقات هیجان انگیزی رخ بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25265" target="_blank">📅 11:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25264">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egiN0xVFa40lGcGUN_rbW0-ZH77VsXDL2CoO4apBH-s915iRjSiH19aL8qcIwSaTiDxQEl34nanEL8IZUSSKazQIxlG4R74sHsAC7XVpYdxtguC7KkhdHY1tG66_gHsrN-Xii81ERV8vA5hCjQhQnWiuUX2QjL45RsMmxP87jDGJxDqwDxEhaXac41Ts4RImyVlbZdN0ObWKr1SJSOOUmyJjGvpl6wL6kee7i0Xv2aD5JJAt_CCGZMQLx54kI1Qwzyafzmu7P5VzbDgI8n5KgP3kkCeJHqZhsno8g_UTJZ0HcLUcR6e3W5EmJ5TcxJ-L3_T27QPZWQIOr7ScHmWRUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی_پرشیانا #فوری؛ پیغام‌جدید محمد قربانی به پیمان‌حدادی مدیرعامل باشگاه پرسپولیس: پیشنهاد مالی شما رو پذیرفته‌ام، رضایت نامه ام رو بگیرید روز شنبه قراردادم رو امضا خواهد کرد.
‼️
پیشنهادمالی‌پرسپولیس: سه ساله بوده. سال اول 80، سال دوم 110 و سال سوم 150…</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25264" target="_blank">📅 10:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25263">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94e6448be0.mp4?token=srv-zhpebiQIjKB0ws2ddcLUikHxzjOPUb4bl6w8eHQdBux0NLa6hO1pk0l9Hyc35JSYeJw99o87zdaSwfvo27WyjSKP1s-LeFYoiGVR2dBgqe6f1iHthi844IIODfHLOgxWJdTzwBHX8tQg4pepC42ymYtKbHrxecJh4XzTtWXwCN3Hc_mHukuvvde7IawEXRGa33t3lTc0Wa6q-aIoKVl91HggBf6T-HgudwJhXnp-lr05QoCluPmodTcg-QQN2hipiZtqb6mFu4A9QoyNknffqPCC3yCy_UpfUC3-nPo0YKIlnNiGvcYYo1tSEZxNoLgDUMPLXf4sFwiTZriR-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94e6448be0.mp4?token=srv-zhpebiQIjKB0ws2ddcLUikHxzjOPUb4bl6w8eHQdBux0NLa6hO1pk0l9Hyc35JSYeJw99o87zdaSwfvo27WyjSKP1s-LeFYoiGVR2dBgqe6f1iHthi844IIODfHLOgxWJdTzwBHX8tQg4pepC42ymYtKbHrxecJh4XzTtWXwCN3Hc_mHukuvvde7IawEXRGa33t3lTc0Wa6q-aIoKVl91HggBf6T-HgudwJhXnp-lr05QoCluPmodTcg-QQN2hipiZtqb6mFu4A9QoyNknffqPCC3yCy_UpfUC3-nPo0YKIlnNiGvcYYo1tSEZxNoLgDUMPLXf4sFwiTZriR-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عکس‌خاص‌وعجیب‌وغریب از 18 سالگی جواد خیابانی؛ خیابانی به خداداد میگه تعجب کن ببینم چطوری میشی. زنوزی‌هم به خداداد گفته بعد جام جهانی اول باید یه ماه تو تیمارستان بستریت کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25263" target="_blank">📅 10:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25262">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9U4PlqAZsTpqVnCcKuYsbsIeJyYYLk5-Uc1GNAU2Y_6HUYfUu2rFFUuhdH7L2Ox13_9pTXcoRIormR8TqZio4LCjRFq5fboh_B7F5o-H2zR_j4vWqG9qv59nHzorPbRlXLsxQJMqvdIhYgPeV3yCAzOGVBDO2ijcUom2j3VIq6KcQ1jm6zHV47LSXhLeFFe21G03nufTjEKN-EHNL-Jtgy43au_Y6ssh_2lPN_vSBdUUpTEORaUutjPs7gd3aUHOdmTx2Ulg1yAwOzmqaPkjbVGtqIgRvaMLagIpBW7hLCy6mrQSZ-fUUAxzi1b3IzYjUUmCbeCTEAb-u8jcSiVZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نوع‌حکومت در ۱۰ کشور برتر و ۱۰ کشور پایین جهان از نظر شادی و کیفیت زندگی؛ منبع: گزارش جهانی شادی ۲۰۲۴ و شاخص کیفیت زندگی ۲۰۲۴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25262" target="_blank">📅 10:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25261">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LoV0_GHSHb5eXW62q0UaiIB0NxeW_cbH2311tjpi_sy1F4E1udC6HfScdPvKLdX9dlCr6pH1N2_hCYxpKw2LJMI1SkKeFQI2csJl8qR3HykVR3WQ4D-YodpOm0evlb2d6IAJnCOHh9924ejsHyCCRYbaoCnkEYe8Mg7xby1ZqLtmGW9toPU0pVvegARRLr4RINUTOcWuSBrjhm2rrT4KfZYW9Y1mMVlla3ds5agbvsOJ_E9UjtHhn5JOqNZ4pviNl88sp2p8-XxcYA8C2cw4KINACq8L2V_3VmDitz4YrbWRXy6_rXeN4MuT0v2fciTVMtuy2UhafnQQba84782g8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدیو لو رفته از کلاس‌درس‌محرمانه امیر قلعه نویی برای سرمربیان آلمان، هلند، ژاپن و برزیل در خانه‌اش بعد از حذف این تیم‌ها از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25261" target="_blank">📅 10:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25260">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stEEqugB9DOR-FXdeFwEhowtV28ZkZqJFis5LPBpQJ7UcVypxk3zTv3J2kPfxOPsT5_a3bNfzvtOMqJVHYC98FH1BZqZlXwXffVekfmDEg2dRsrCTzjTSw5KLp3qLLuNeInqBElOjFjTlrz-KJ04b3zLMSqNWodBgRlp2v6PhpFTxWVD2IU3z7iOxZ8rmtUyMZsXsXaH_c1BAX8qtS4zV9y452CdXkQ8JZByGIh-yrAoT4U2FImdhuF5JWbdkiEVwrU-ytk0sbtaxjHIIGjP-eHNmBl3JjhNYlB1tkGy7ISuwShfeBeZTlieOBuHkFzomDpBTb_LQx9eh5Y1NzNMUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
تصویری دیدنی از لئو مسی هنگام زدن کرنر دربازی شب‌گذشته آرژانتین مقابل مصر؛ آلبی سلسته شب گذشته با جادوی اعجوبه آرژانتینی خود سه بر دو از سد یاران محمد صلاح در مصر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25260" target="_blank">📅 10:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25259">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktBClwOfEZjyIKVRz-E4bdiUGpKyVTYn5Hmh2gfrQViXXJlTNyKqXZqJ2itXtZyStC7jOTnFfGOqdMtZl3Xu6VyN4j0cQDgNXr5dk_xeHwht2ViTmped9QD6ooRLaaeTPLFUsc_Skv-uSUc53Cq0ABvp6lnpFcH7sPPGC3RLk0K99sdpbWj2jj-7CXMh_5JW0OCXgw5AqOr88uVuv1swcE5OyD8MYdyNiiEb8MioOIVio0GYzeAbvjntvhcL_cfoeyeVZcJ-MmDHRo7_3rcgCIBf-6zHytDAPd0YkgsYpdpvWJkw7J68NFgdrfotrcEYdyhWeqqzCa2i8hTsAi_hiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ علی نعمتی مدافع‌ ملی‌پوش سابق باشگاه فولاد برای عقد قراردادی دوساله‌باپرسپولیس خواستار دریافت مبلغ سالانه 75 میلیاردتومان‌‌شده‌است. درصورتی‌که بانک شهر با این رقم موافقت کند به زودی پوستر رونمایی از مدافع جدید سرخ‌ها…</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25259" target="_blank">📅 09:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25258">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efXDJHowv4rmxW1wxkDJL2jPEfXCOrPTnsP57cCNvMUhWkNbcCaZSqRasL_EmbzRxJItUmdtxCB4UjeWm0eFkfmvUHxWYchcgj7RcCBW-gzoVLxUuEDiUHM6n8IR0FBuoPN0uom5T86FE0KDh3fZAV3M1q-YSuxPuT7h5Y5SJVEVIqtNzuUEaUqIuLaPl0e0rJ4HVFcfTeYk1p63-Say3Nnl6SyZjQ8mMOpxyiqDIC1Eqe5JTZ9yewUPMB4fn6AzWizxNy83jQic0-SFAc7AgMQlmzrYM_zhAs5aOVIBb8VKPtXlNZBmRNE9JMabpjU1OgAQ6sqfeQDKNefwURCOkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25258" target="_blank">📅 09:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25257">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gf1HeaVU7hPayNafuU6MF3HdZgv908XmjQh5pY38c6ANz6UgLmrcIcuyP4tt9OEA9hbCkIzIX54DkJliVM4AjFXl15yDe9wVs1MenHAo82xLNVPXBsdwrmihpLQWBTREj3-zJVEvuuOIRXpDyIhBxgbK2rNc_AJrPtgqL0cHPAr6-tay0G0-LrhLoeBlBjs8BPEvDtC93Mf_5y--PGc3MLcHlj5Y-rCW4AiAV3XkztPcJYbDyZQCY_N-ycfqCGo37IkfaPJQ1S3UhWXJI7mxPOzLv-M9xxvCu1y85iKXs-PdbHRwDlJ_JujdSotVHPckv6GAUNE_WmUUrMobQ4HBVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ آنتونیو آدان،عارف‌غلامی،آرمین‌سهرابیان، محمد رضا آزادی چهار بازیکنی هستندکه سهراب بختیاری‌زاده به مدیریت باشگاه استقلال اعلام‌کرده درصورتیکه حتی پنجره نقل و انتقالاتی آبی‌ها باز نشود باز هم نیازی به حضور این‌ها ندارد.…</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25257" target="_blank">📅 09:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25256">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGN_QtZwCC6FjKJ64QdWELh56VS6g8f4qJvUyOmDf4qmqduG3cWGnbI0ZXafbk4aUYYgDGMkl2ImWutKWFmzQ8K_dIrzKTDk-WXiJvQMl7dt4Dfea5_NPlSRAZwopwIuj4mExnQMku0C7-stL0Kjqg-ycnl6uHeQvq_mdMaMEGZfNvvjo6wKfZ3MrOVjbFuV5ETw1VS0a5PPk8rivnmZ1da6eb7cfM9ORtMEx4Iz1uU8FNJywIow6sQYxAX3zdZc4FDaRDfm3CGsV-JaG5xjDbFisxxoVv3RyAIii2pAY-fJXt2mEf45cmFv1uugBq8TM_hQwdwg5VGie6xHSHdBIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛ باصلاحدید کادرفنی استقلال؛ آرمین سهرابیان دیگر مدافع میانی استقلال در لیست مازاد آبی‌ ها قرار گرفته و بزودی از جمع شاگردان سهراب بختیاری زاده جدا خواهد شد. پیش تر عارف غلامی نیز در لیست خروج استقلالی‌ها قرار گرفته بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25256" target="_blank">📅 09:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25255">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8869652ba6.mp4?token=nR011aGnys01op0ctfwaRDA4Kk_fVdeuHgAV700WSbvEu9LjytwGnZVB7f1aan-fS3kEiABhtaFlk6OlSwALim9GzP7fN4fmjg9xNtL0Lz8ZbtqtNgTI-0cxMB2tFpUpbdqlSerNJLHNU9bNxPt0LoNtG8pymqTFtRc1aibR-6dquZzqdlMOIm8embyBfYCy9GVmfxvccVA-e8nQrInO-xQtZ-8fXBhYfA2OlRgjuInriLzm91PLfHOOKdzEQLol7GcMThNYSWqR2956QEQ8YQ3Jj0FGg5ufU5QkZk-ySu1t2iXejj3K1WTkxkoi7X7_xsLV0Mchn2rM4xl294wSvjzJ4CVprxBRhXVvE_Zx0th8M50PiOjbNkRJrZy-jzfDupvSrJAyBBxECQlTCfuPExVArOyFpvMowo8r5EI8ITUO6wZB3vrHeHvMpzqCM00Rw4-KABUt3sfjqN_83ajJEzr-Y1pnHBwH9pN00HDkNWfLUFX2CvdAjzMqIBwOzZjXt1gBYy3bpvNKwZ230WonBVXmDw7ShAA_EGSkseVmvvqWDSiALU0JOa8WorbhIFMMIvhDYObYbX0m1aNqJXgGdt3Fkx6TQbIf7xj17QIUFTfiQMpD6VpYpPgustaISpA7m1GservbL9OzWw4z4AkIcXzRd0hSj1hRLbHPYWhKklw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8869652ba6.mp4?token=nR011aGnys01op0ctfwaRDA4Kk_fVdeuHgAV700WSbvEu9LjytwGnZVB7f1aan-fS3kEiABhtaFlk6OlSwALim9GzP7fN4fmjg9xNtL0Lz8ZbtqtNgTI-0cxMB2tFpUpbdqlSerNJLHNU9bNxPt0LoNtG8pymqTFtRc1aibR-6dquZzqdlMOIm8embyBfYCy9GVmfxvccVA-e8nQrInO-xQtZ-8fXBhYfA2OlRgjuInriLzm91PLfHOOKdzEQLol7GcMThNYSWqR2956QEQ8YQ3Jj0FGg5ufU5QkZk-ySu1t2iXejj3K1WTkxkoi7X7_xsLV0Mchn2rM4xl294wSvjzJ4CVprxBRhXVvE_Zx0th8M50PiOjbNkRJrZy-jzfDupvSrJAyBBxECQlTCfuPExVArOyFpvMowo8r5EI8ITUO6wZB3vrHeHvMpzqCM00Rw4-KABUt3sfjqN_83ajJEzr-Y1pnHBwH9pN00HDkNWfLUFX2CvdAjzMqIBwOzZjXt1gBYy3bpvNKwZ230WonBVXmDw7ShAA_EGSkseVmvvqWDSiALU0JOa8WorbhIFMMIvhDYObYbX0m1aNqJXgGdt3Fkx6TQbIf7xj17QIUFTfiQMpD6VpYpPgustaISpA7m1GservbL9OzWw4z4AkIcXzRd0hSj1hRLbHPYWhKklw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
علی رضا فغانی:
دوست داشتم هرجا داری کنم نماینده ایران باشم اماخودشون‌گفتن ما نمیخوایمت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25255" target="_blank">📅 08:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25253">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijFcvha4F_jaDvYm4XYbM-3CYKSdX9PnX3QQ-_2ebPmQWANWx4BMtyHJbrR0tCP_mqVtJEN9zKgs8PVyioL8adHVlr_2fZKTXox9uHsdsAgcQ186NeX2XsQ4jBE4T-Uu-5_TY6Ps1bvKuT2-IhskptV6kquQmaJKY3F6SaKkdAS1vsQAc-1-UhqlSGRHSN6JgGNCppjYOJ_zdbktnVErYAREGS4D97C_vcfsoQqznxZ15LFVYPvtem9l6100xac-mvW8arYOYNZCNk7T_8pkxIrEZC8gWylA4_1jRb2yRP9AVMmD_FFJBoD7d36gohJnHNfqxyhckoI_zQh1-1LoQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امشب؛ آغاز مرحله حساس یک‌ چهارم نهایی بارویارویی‌مجدد فرانسه و مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25253" target="_blank">📅 08:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25252">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B705ETLed1GysRLrKL8z46sQApn_iotcEcKVMUOH4FctIVqvJnRxLpKvp0M7Y9D43h0-m6qY7QQRmVxruO7bapQ5a6R6xfiOaj-4wQtahUcpHlZHFMviBQC3lb-4PRS9MLNtT_bKMnuyzKsLNcKQ719rZbl1hnI5EZENHVrmMZcI5mJnmLpvo0F-Mz0fdEnKdgtU6X43raTtzCJ7EdksKSYlt4P9B0hTTn7K_FL4xIh9H3rJ5Gtm6MUx-xhsOvVxIQyTXbU2m8NyZOThUao1J3UiUbA_9Tz-aYq5GrroYTDtsdPKJUx3_3cHB9IDnam9XOCxLlUsQRsxWzBDMdzjdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
جرارد رومرو: ممکنه‌ طی‌ روزهای آینده کریم آدیمی ستاره جوان دورتموند با عقد قراردادی 5 ساله به بارسلونا بپیوندد. مذاکرات مثبتی صورت کرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25252" target="_blank">📅 01:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25251">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srLkOyQldweLy0TwprP_RTaoX7oJg0e186td5sXibjdn4KuRFIv6Kppgtps0GcLU0L7I8vkp1ykKT2oRm9uPDxy3W-i60kY2fGAVsrXcR1F06vyQjW4Rh_l1DmMkJ694dW6RmWH0-IJLwkWlTXIV_K2ZtpNR558bmsx-GGZuPx6TGxpQ7BKNo5F1dG17RLiYUL0YyW9_-kNj-oFeJYvC2BgFqNjnv3O7YJQK4im7PPo1xCiUtGrU-Jl68rzt7UFWlkhylb5MjMx-9gELuYHHtPzLDFTM9scMZNBLiuNPlv8WLNkCB9fpiIZpeTm_tInUIwk19s8nR4Z1N1GIt8RxiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
نشریه‌بیلد: کریم آدیمی ستاره 23 ساله تیم دورتموند به مدیران این باشگاه اعلام کرده که قصد داره از این تیم جدا بشه. منچستریونایتد و بارسلونا به شدت دنبال این ستاره آلمانی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25251" target="_blank">📅 01:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25250">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6798637471.mp4?token=v6qWYpe8U3Boa4eoQn9kF7n5hQsEtjehktymvVxn1wQpSpbqpj7ygf6qQZSJZ6Fqe7KmD7AvsbwSrL3k9GiHsxKrILTqWO4xfUT9QYtsYOtLpyJxMlhr1bi0cX8ScXoADUMvpMNgmJQGViz6MCAJX3gdYyuxZaXqq3jaQvpS1Kcoe-cEUCe-hDmyP2aFmQ-oV9QS2G4HTYH9vMuc0Bh33rnC0q8AEsrTJ_xvxyeMfqj5ZLvK3AFf4PvPBrejqSax0X0WbVUmBACoraVJ7SvqePh6MK9EBqSM1DEJ7bv_IIfL7X1uwdxB8tB_2Xh6W0wncyeMJzzJ9C-iSC4BQwyWcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6798637471.mp4?token=v6qWYpe8U3Boa4eoQn9kF7n5hQsEtjehktymvVxn1wQpSpbqpj7ygf6qQZSJZ6Fqe7KmD7AvsbwSrL3k9GiHsxKrILTqWO4xfUT9QYtsYOtLpyJxMlhr1bi0cX8ScXoADUMvpMNgmJQGViz6MCAJX3gdYyuxZaXqq3jaQvpS1Kcoe-cEUCe-hDmyP2aFmQ-oV9QS2G4HTYH9vMuc0Bh33rnC0q8AEsrTJ_xvxyeMfqj5ZLvK3AFf4PvPBrejqSax0X0WbVUmBACoraVJ7SvqePh6MK9EBqSM1DEJ7bv_IIfL7X1uwdxB8tB_2Xh6W0wncyeMJzzJ9C-iSC4BQwyWcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جوادخیابانی‌ تو ویژه‌ برنامه‌امشب جمله معروف
"گشتم نبود نگرد نیست رو گفت" خداداد هنگ کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25250" target="_blank">📅 01:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25249">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DnFBdBL5nV6dvffInwL1FKVhNXqOrOybp2BTGwn1tDpGepJSd56hiwEzMT8mUjdDPxXAwB0zL_9dKapt6l8HVLS2_p262uX4TutYOcx2cyUwfe24YKNLMpq4w9MAL5orwa_yG70zLH884umX2_CoFGsSFKs4sSFfMrQ4SdxAfU7rQ5mShzc4wICOl7EQKyLiGsuwfWMGzzDPzpexmpjkPC9HobSqKYcu5sAricypJW0GPWqRkXL7p8g-5Y4H7HHCb3ePJd6HAbhOjQGNaHJ6wDujISPDczZKmkdR_7YXKNZoYi5VnJrrTEnTLvMu6XdZeYGY9pDbqkXKJ9izvLPwiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
خوزه‌فلیکس‌دیاز:باشگاه‌منچستریونایتد برای‌ جذب‌اورلین شوامنی هافبک26 ساله تیم ملی فرانسه به باشگاه‌رئال‌مادرید نامه زد. کهکشانی‌ها برای فروش شوامنی ملی پوش 100 میلیون یورو میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25249" target="_blank">📅 01:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25248">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cyM-oO54EsA8ure1YJErEaDfjfQS1wRiKGyeGNvxbSo8GhsDmYAT9H7CfRgoZqZuwOFzqUCVkWkDjpJO9imAv0lEGe6xRcS1Tl5fUxBM27kbrYK81A8_-lnfzw9xPiu-JOPog20YGLYYpcVgfRnm4kVN5SeaGXDuAPNbcjhmf6-0bDYIFounz7FB2h_5yqlcn8UhROSdvb2Ds3l7pme_tv8_OR9hRbJT3QleMoK703hDKvWh0dWj3yD0gkaLg2IjhxXHTo4eGqOfbWZjAmaQB4Ojo2zg0sK6CJnF742k4hHV1SajftYJ5ZtGrhQ0Ohjg2xDJbqjeae78NeD9bq5JWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امشب؛
آغاز مرحله حساس یک‌ چهارم نهایی بارویارویی‌مجدد فرانسه و مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/25248" target="_blank">📅 00:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25247">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltn0hy4IX7l62CMvd1RS6AR5ckydkGx2YpI0I48q_yt4AiKifKJRxPBG7MmvjmbQENX5Gkurszcdz_nPtSazgL6_UTWEtDCtHFmh6uISX_hZTBbbif_FNTXBoLudUKj9fYHCOh6t0ZWVj7HB6ENLegYTnii2UXJB5t0Q2EUd6skqqiKz9SxJV93ctbRECmyFfGwcYXzKj_vEW4p4L6qpvHapvtRmU1fQoYIBgwD1pDqu2SZFFLjOlOWv1vL_JtyPSDhG4zV5RkQyohLo_OM56zbOLlw7FNk0QP6nThR1Imd3yTbmzZ6-5uQLMWkJjhXMdlbpcIYbiuavyzBXB3Epkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عکس‌هایی‌که از وضعيت امشب بوشهر داره دست به دست میشه: یکی به این ترامپ احمق بگه هنوزجام‌جهانی‌تموم‌نشده دهنت سرویس.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25247" target="_blank">📅 00:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25246">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxov-A_4tb7-nwVbLr9BPZEm88-CYuAydw2znIsKRBwacoXQlWQ2bolvKscXDW0rOmh8BOSktByScfJVsV4lStKbRE9h9HXWh-13Xr6_DtaRY3PDA_EYG0qPS9qiMX-7wrbear2I6fe2de4Uj8RwkjsXN_6GG_JJ-FQnLYmfanLvp6srsyQLs3plgTv-J4qTZSDewwOppt2EIA3-xtLkybbKmUlGG8cfcJNfHrZbQQzrlq6WkNMjZyWZ7YMJ6IZQ4GD4ui3lsDhPhgZTZ1yKOhzPf4HwPLa0crApupXJGuXB7VCn-ogLZnQibGBDxCv8C7w1m8tcjfscHC16xg2i8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه دهوک عراق بعداز جذب سینا اسدبیگی؛ حالا محمدرضا سلیمانی مهاجم فصل گذشته فولاد خوزستان هم با قراردادی دو ساله جذب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/25246" target="_blank">📅 00:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25245">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cE-DJeMAw6d0PtWnfDppZPXgcwa7pbvpL9wHZ_dNPFoOVxYxwZmMHgAABGEHYyTma4dAyz4o5zQIQkIjQ9s0d-tu8vy_VbtJYEdYvxr2d2k-1XgLOaAx3bcPP72SDgn2NJ7h9xuOyh7A09rtyvP7T7UkP2ied-eiSvbmXhE6Vq-eTepoEyeuezgI_pWz3X7gw_U5JVxIjCgjn0J__DS6_944C6PpoImZ85xEwL1jTQDfL3OF8NT1axSHNtOYmvx7wvZE6T3SIZaczK21xlG5MSiXPDJDegk2Tx63oy7YwQhfyMniEo4Z5YAzSo5Ok9GwqS_7Wx7GUb3h5P8upD6qKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اگه نیمار جونیور روهم به عکس اضافه کنیم؛ چهار نفرازکسایی‌که فوتبال روبشدت برامون قشنگ تر کردن. کسایی که روزای قشنگی واسمون ساختن. کسایی‌که اسطورمون‌بودن رفتند، اونم برای همیشه؛ آقای‌مسی لطفاشما تا ته این مسیرو برو. بارها گفتیم که‌هم‌مسی‌هم رونالدو بشدت برامون…</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25245" target="_blank">📅 23:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25244">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saa4fFR1LgAUvKrRuzMzGzcbNc10cjW3g8EaIgJvvuyNixNB_S5EAXJGdTAOermeZtGtMpRT41g5TcLrAHWIN3E5VB97gJp9dExduYmHg7UVwOi7qJ5k5kInu7zHxFWgGRyKkJvomj1VwrKGRXWeVr7_DoASttbih_yolKBUnG1KVrv7fyuSE7WevhEUK-0BVRXOKzt73o8iWKQxuzd3Nl4EDWPdjU97PpL4yrwXOl0CFUVG0b87X_vqKjcIT1b0DLJdNzqARfDTysXWTAcwgKDehU1KZ_tsXke68XzmNyajZxMwgWJTwV6J2adChj4REoNLhvlsDd89JSt15QYnjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌برای‌جذب‌قطعی‌سامان تورانیان مدافع راست آبی‌ها به باشگاه استقلال نامه زده. با توجه به اینکه‌باشگاه‌استقلال‌تمایل به‌جذب امید نورافکن داره و مذاکرات‌مثبتی با او نیزصورت‌گرفته درصورت باز شدن‌پنجره آبی ها این معاوضه…</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/25244" target="_blank">📅 23:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25243">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9YjF3LNKnKKbC2sGRz2p8a1yWYr7-pViprJ1UCXZb8NL8uqCR-3VWfWH4zQ15Sk88jFHb8_OzzOSjFq_oKGmQFlEavVpM-UB0iq20g5lBN97JXxlyfcPl_fGhhv6c39irh-Nhy9QdJelhG-LKrdN5YxrIFOSOaoseCrIQ3nOHqFfWl4ebakQR2bPfRXevs7lA-vgnp8d3qX8x0e3AR9Ja6xHNFtN_epsLMLSJ1653JEFtwhSjzTeKUd8WejOysLuI772z_keHi90yAnPl25KV8KAu9aEBdo7Sl2fFo15m6WqFHJbrHX8GvhO772yEtF0YlOhjOuPyOwTy06mST4VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
تصویری دیدنی از لئو مسی هنگام زدن کرنر دربازی شب‌گذشته آرژانتین مقابل مصر؛ آلبی سلسته شب گذشته با جادوی اعجوبه آرژانتینی خود سه بر دو از سد یاران محمد صلاح در مصر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/25243" target="_blank">📅 22:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25241">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kw2UoLgP37xBH0O7jcHXZkHXpO9igEKkzTgCc4eAFQNSTOA4iNLRaNizCzS0MQmF-ui6l0GUIC00_Tz-IV3PXDVSCCNDQwj7tUNZsKOOBQya7qMhlqxCmdKowJWfaRi0vy17lOZkri17L2WWHnI1NDrcs7pAWvaJ4t0Xdue11wVVy6p8EIm72RbvEp1aHHqtq68jGvXsDyAfmimX_aOStA_YvZyf0XXmwO5ET8_f9JPX0CzO06dgW3xxTHPNoJ0WL05wUzcl4ZRQFnhqyFf15shKEZQbYdfU2YrksTWQ-YM8HX1xS8RW84Ha8e6o2ljAtQRM-tu4n8Oh7qtl5KYk1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GIvjpl-BvE4na0KGVBGMB4dhDSOz2epquuxTvdserDApoUK0mDx3HuViNe2FLv9RvsOEfEa4bgF-LRwsbEB-gkXUP67074xXhiFMR5ov_9iE5AOKBhD4BEov6vf3gXSfEXErV0uS7TNdaRxWF8wEUuKK5hp7kjTU0yBiWnkqLUMkTRH1gP9kie1ckoUtaUPj1rGl9H0SnqOMK-lss3NqOXTtboz3rjc0VS1eDZX0qkoeL5MPZPhXJlvrHkxoTHuSHNgcFE0GgIGr0dvZgzPladNEvR5qO9w7D17Ejxe2cJl4d5L2-FPKBpeEEuDnMfBF7_Qi2xF-Jz6LFRzUZ-uGCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🤩
مجری شبکه رسمی باشگاه رئال مادرید که مدعیه‌کار انتقال انزو فرناندز به این‌تیم تموم شده و بلافاصله بعدازاتمام‌جام‌جهانی2026 انزو کهکشانی میشود. گفته با انزو در ارتباطه و انزو گفته به زودی به رئال مادرید خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/25241" target="_blank">📅 22:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25240">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d23ff97317.mp4?token=O510OYRRjCoySs2bsq_tdcWchPKI_mwZ1pxwTlDjr9bZRzgTnmZ44h_qn_MlydXTuRkxRufhAGsVkitcB7wkIx505NHD-T87P4cnPu9U31_FQ4BrgYTgJo67ooj8EuMNeEsSuwNj2p_ixpYishHV0gsHe69t4dMi7neqk3Xl-EUeq4mR1AKiuFcg7Sat_t9Vmwf7wj1f0Kpw_5DRCMRMPFq3Cftqdnxn9k2lvU55-PoDqL67pUtAErgN10Nm3fNtivLQt6JncoXz5yNo57yngw3caYHC-EvmrAMqmOTTQPEwwlpn97z7cvl0lM6OjqZfK31dBnpUTCcP1UypvD_xVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d23ff97317.mp4?token=O510OYRRjCoySs2bsq_tdcWchPKI_mwZ1pxwTlDjr9bZRzgTnmZ44h_qn_MlydXTuRkxRufhAGsVkitcB7wkIx505NHD-T87P4cnPu9U31_FQ4BrgYTgJo67ooj8EuMNeEsSuwNj2p_ixpYishHV0gsHe69t4dMi7neqk3Xl-EUeq4mR1AKiuFcg7Sat_t9Vmwf7wj1f0Kpw_5DRCMRMPFq3Cftqdnxn9k2lvU55-PoDqL67pUtAErgN10Nm3fNtivLQt6JncoXz5yNo57yngw3caYHC-EvmrAMqmOTTQPEwwlpn97z7cvl0lM6OjqZfK31dBnpUTCcP1UypvD_xVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
امیر قلعه نویی سرمربی تیم ایران: کاش قدرتی داشتم که بعداز گل شجاع زمان رو متوقف میکردم تا شادی واسه همیشه رو صورت مردم ایران بمونه. باور کنید این تیم شایسته به مرحله حذفی صعود بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/25240" target="_blank">📅 22:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25239">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPoKJludbF4FRTMAKtu7uu94SX_Ze9pOB7IvaE4g5EGjQQPcwhbns6h7xY6y-zV8JQp-6zZSIBXXIFu96OsEH-pllKzLyl57C6Rp9uu4yI2hImEdwzcl_SprO2phfPgsT0IchUDekEk6i6U8Xvzq1r0MfwgsSx6sVJcuGQKxioydydAsmKaMz9_j6LS28f-EaaZSPbhnFgxT23yY6ZLclJqzq-d8Z-83Ceo-EmYJR3D0QDF6NI8hMRibjTVv2Qm_90w80STNKmYPeVY4DTgie8WJJhjj3cXAPrWE_dJlrkXOGgqYHlWu2RTPaeZTjL0mKWnabH0ViwShlucQpR-19g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25239" target="_blank">📅 22:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25237">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4ypJi6mRjsUEn3a8b3A9ZKtyviNtT71lLZ3EBmEV-55-XctgX7P4YEVpDEZtgtx-4QFzPQMF6cnZr6OCMgnSeii8AOlxWmKKEPCFkk0VcEI9jUgYvpFv5iV0R4Fsa4tVwnzhkX3R_ZvPnVIySaGALU2leH0FjmsYxSxJeSG5m6ix5m55so8zARfcT0znyKOTXGlSGQiwNNtWGE_P2m3ABjrP2rV-nmXMCQ_PEXo9UhiMsZFZBNH9j04TKR-2sByEoQzrqn0-FUiUbOgqYigEFctFzuoqkguUE6BdKSiIdE7JsUggatkeKJtaGxAsAEnrvM6kEkaeJWWO7Hzv_6H3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ورزشکارانیکه درحمایت‌از مردم از تیم ملی کناره‌ گیری کردند: یخچالی‌بسکتبال، محمد امینی بسکتبال، زهرا علی زاده فوتبال، موسی اسماعیل‌پور فیتنس و محمدرضا اورعی هندبال؛ بزودی شاهد خداحافظی جندین ستاره تیم ملی فوتبال نیز خواهیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25237" target="_blank">📅 21:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25236">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YeWxU6QJGmgz_hET2KM1yev3aB4uIrptypz849PokCYM6ALgxwCzguJyNmxbxiL5UYPYXrOZnyeQ_XWLe77r6PuhZXfbpsasZ07-zTotrZfSjEitiqOS64jAGhgOY2HuA7q84DWMK3guoyIQlAsfZBONsjU0dflA3nVTUzX7iygx45nyKkLirpoHZhJMUeqTP_OSulTYmRAuxtl32y-iEKYJb9YUjzgllHy5EB-IBnp0zjI6umqii_i1QApkTv-HPu5uS7EGZDTXThjfa8DuFVj63Ul8u9ZQ_kQfjyGX4LJpOQGfqY3hrawmm_nJKXRdPojkOcDg6NwwALyyVxRsuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🟡
بااعلام مدیریت باشگاه سپاهان؛ گابریل پین دستیار ایتالیایی محرم نویدکیو از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/25236" target="_blank">📅 21:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25235">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wcwk3ONM5ATrIlxwua58A8Cyr7FX3_ghj6zJ4aqB2jX5SmrErjqmYWqTeQd9HlAd1Ex3qeB6dxIhE-lfst-UVXj_FMGDRDuZF4Pdshj42SHoPtPEyphqxNe1KFYWRXdsDzB4tq8Rc96pC6tNTDvTVlv_IvoCOnngOuSlKmgoHLQpjcgZHHTGEGrKoVyr19Brra_ISxWEjmdqSw-PHVAFSCKIDZhkWPvAGdOfLeDuV76fRhHPMjCt2oTxxLF-Cv0qh7YQZwcy37VTfD6IYJKYWmK7qYfnNOKFzXnkmoMdmKsjakV2UPUrhra50E4I0bwXyLLZWNCfJzQTS9LztjA66w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌پرشیانا؛ مدیریت پرسپولیس پیش از انتخاب مهدی تارتار بعنوان سرمربی خود؛ با ایجنت هادی‌حبیبی‌نژاد مذاکرات‌مثبتی داشت و حالا درصورتیکه‌تارتار تاییدکنه هادی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25235" target="_blank">📅 21:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25234">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXBVG9gs6nuQAPYfPAstD7juy_vt7Oi_-fczUzRS4mF6LNikxCz7KrYY24D4kxyaai9gQbd6--Y3gKVbfM9QgJ4P7CTopWaO0f3rXAEt0k7b5fodrHD79icGO2OP-mFEdQEJTX5yWudw453t5I5eP9fVEr3joP7EBdajfV7TkUGd5IODVK9nrPWXQhLcSS91VD2ncn2q8-9fVJOaj9cu_vvDSoAy5bRCGaiHh0SA_c3CVyszZ4OIc7-LNwwlsWgtd6bCsVDmntRP8kNqWuTFFTeAHUe6u4Nnkua51vgvx7SOlyjDzBIbB34HoHpRkRkepXEDw2GJOvoEF-FJPQWmYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امیر قلعه نویی سرمربی تیم ایران:
کاش قدرتی داشتم که بعداز گل شجاع زمان رو متوقف میکردم تا شادی واسه همیشه رو صورت مردم ایران بمونه. باور کنید این تیم شایسته به مرحله حذفی صعود بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/25234" target="_blank">📅 21:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25233">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJlI4vx6f19nZMxlIXdCcnrPS1oZOsoSqN2serPcxKnPr7SRqx3jaf-1Dq3lykaT4bMe4ZNQ0_aFpsJoUfUh0Bx1L9skwgxlEHW9e5bSD-r5dWfDM9ZXCpRXyDXqO-HLyr-Xou7MKhbjlFwVcIKmIK90hFMO463mQNTs9cHD3scv17fEBDin8j_lx_SJzJFQtSiHd7NOIUp6H1M0yDDn2Puh2adVjPcNqMGx7ufjW0BjZsrwX_UBOTeqbEqd7U3QUiLFyCkjZqi3eiQuLQGcZ74RH15zeYBlBx_UnQFBdSP68I2B8jhqOZaVeGuUHA0Ywu_EWZw_psRO1n7x5TEkbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
غلامرضا ثابت ایمانی هافبک‌میانی‌سابق ملوان با عقد قراردادی سه ساله رسما به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25233" target="_blank">📅 20:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25232">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1hQ3aO8NGgZKNojRXfS0u-jo9Eg6T9dZ9v1rackVbHe_LKIILUaRohECfgAYWC1pXHMVDy1yxSP5IfEh5q5UZ9HzB9h2aHDATCE2MzDsrsZpl6cctAqY_2t729edXRUBHE_Pjs5pAzUHA4yDZB2qW12Gcyb343t7S3egOjPTTwcA5eHxHQlpCQw2ybqiMiYNVkHanPvGnsJWPIdpMc7yga4oRnb-3xYXBmgF0x6TEMbk9RARcIQ_pxKnvTArBJYBlE2mNOoI79X5fydf3Ug-1RYllS2PKYNnOoRrSHDapYYscFRI7ZCDm6CCIBJyvgEFs_WS1xtL_o1myZ7zl_g2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کنایه‌مربی‌مصربه‌مسی‌ولیگMLS؛ابراهیم حسن: فیفا میخواهد مسی توپ طلا را ببرد، در حالی که او درلیگی بازی میکندکه‌فقط 3 نفر آن را تماشا میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/25232" target="_blank">📅 20:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25231">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gH0M1Q9kQuYwerTbKlLrPDXYn6YznXyaFuUX1oPBuLq69l8zBtZIJzlJcxH_KubEEYMNBmK8NyFXlR2g7B8XpPkBLsmmswUhWG-42tW7sPMbB5Gd97S0jXdND1HNjwCNhB1Ox2AmuTF8EJEWKdjduSWPFEcicTZI-T2mwghuNVGbtiqmwCYdkBRtMQV5DwSUZjf8fd-KTlSCopLlXIXo0GdPFhqWOc6ICdCvtsdZdimNdr8jTlNMxiq6WdCVbeYdPFTTHGoXGPFMWDc-038LcjxPcFbsL_7cRQjGjWy67gH2FJctGt8WVw75nyO3IsaMJXWsDEzYBvhIW7jm4cVoyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇦🇷
یکی‌اینطوری هم‌تیمیاش خوشحالن براش و بهس احترام میزارند. یکی‌بعدبازی از تیم رقیب میاد دلداری‌بده‌بهش. خلاصه که یارخوب تمام ماجراست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/25231" target="_blank">📅 20:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25230">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvdzLkrXvvN_HnUWzaotVTz3xAECuc-HqTaTGEOr6q66jxToHE6yslScYNBWpYd2CYOUYykQxVc-AQlzY-Jde1wVC8kXQfMPawGO2mAFFhCtAWAI_isgIQeVkxcjrktDlAscptrBRnP-LRfwfMXFphB-rsZZfTlBE-ILP6RIzAnNUMpWR3am68K4A1FGIskNtvNRzuLHUY6k7sh3_Valciv3z0-OuZyNXAkRCyfSPI2PAjq-_KBqcvsYxG6D6hASRKsfUfCDfvhPt_U1dXr_TjazDpUw_JeAz10Wcd9H-IJLXDwg5lh5oaVATijYypxwzR3qe4xFMjAfLX94ZJd2Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/25230" target="_blank">📅 19:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25229">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_1upSPWaNWTOPfgIEEWjQV7IPAtm43S2h26lC4dM1DwRRlFij8ALsmyzdIRdlTlWgC8NiTgJfEFAO9SP0XeZ5VUy9GPqfZqrdkNiMElF23gis1XQHuIwPTBvUtjl8oUpK9sslDB1Y038P_8Jl6MMgzsMnf7wx8UROMQhSbxdFTm6ZPALSAAnHt0XI_4S2GB9h8uBAMfv4dKy69wGEmpRtByF3NruxvqEeVeYBwS1yv7FQlSBUungBm1lsAdIeQp3w7y-iQke6z0xjEwkLAzVhRA5Gqk2rvmIz99UIcUDxFD5_nEQSbmrkK9ZckztaGY895axcI-m0TTaj0y8KIjKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
#اختصاصی_پرشیانا
#فوری
؛
مدیریت باشگاه‌سپاهان‌برای‌جذب‌قطعی‌سامان تورانیان مدافع راست آبی‌ها به باشگاه استقلال نامه زده. با توجه به اینکه‌باشگاه‌استقلال‌تمایل به‌جذب امید نورافکن داره و مذاکرات‌مثبتی با او نیزصورت‌گرفته درصورت باز شدن‌پنجره آبی ها این معاوضه انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/25229" target="_blank">📅 19:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25228">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7acbde92f2.mp4?token=aPiM3PnILVHjFy9Dj2QXe41EVseENyySkCRs2vQHOwRiKaHv73wwzdGB_QcuOdMFeaLLukCd4i-ehBw7-Vh4dPv4GdDjdVz8Tk11s6vTI54pS4xBgcY9OBFWqYUdNrBi-zwuZxsQilBtlwu-ZI6tRrnELBnIPK1i_0onmRSAkcPXVDXEq8pcVjXTXWhghd7CZsAq7OA7WO30fhUr8YUJm7A5oHwykhSt3JK7YEqZklqxtZQnJKHYDeJRLOT36qpl_pjxs-otI7_PQr2L48npuEV0HJKBxlrF34wz6eD8iTntl8rQ2YXoatW9JRLABNCjzOZcKpO8rB_9GQy3iDKBcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7acbde92f2.mp4?token=aPiM3PnILVHjFy9Dj2QXe41EVseENyySkCRs2vQHOwRiKaHv73wwzdGB_QcuOdMFeaLLukCd4i-ehBw7-Vh4dPv4GdDjdVz8Tk11s6vTI54pS4xBgcY9OBFWqYUdNrBi-zwuZxsQilBtlwu-ZI6tRrnELBnIPK1i_0onmRSAkcPXVDXEq8pcVjXTXWhghd7CZsAq7OA7WO30fhUr8YUJm7A5oHwykhSt3JK7YEqZklqxtZQnJKHYDeJRLOT36qpl_pjxs-otI7_PQr2L48npuEV0HJKBxlrF34wz6eD8iTntl8rQ2YXoatW9JRLABNCjzOZcKpO8rB_9GQy3iDKBcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
👤
طبق پیگیری‌های پرشیانا از ایجنت منیر الحدادی؛ خبری‌که رسانه‌های‌آفریقایی مبنی بر توافق اوبا یک‌تیم‌مراکشی منتشر کردند کذب محض است. این بازیکن اواسط هفته آینده به تهران برمیگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/25228" target="_blank">📅 18:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25227">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDxyE8LbxhL9iCOXJI6_K60xupvJ1QLbjXwkwBvK8RKFfiGts52NFnC5yUvb1PHYP8aJzlZpdzgQunLoEdhuYzwlfIQrRpPR02KIKzKaj9gjoUjRi9QOhUkXO0gyFVahsZQFzJicdVQrVb5Tqr0ry8-graRfICPK34tHerjrHnREONqc6bgPOR3YDAMFZxo7iH-pcmovlbxNq618pw3PMasouiHYOCYcKNM2wknKNYVn-VuacEeKUihfl4HIKK81Vr8w9Ch4igJoCMmOKNKdPo57rmFjdNtMoHLPdShGEZPN2RxqmJvMNSQG7p73DwUFQtHt40F-dNtcM_qB2mT7_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
تو این عکس لیونل مسی با نصفه بالایی صورتش داره گریه میکنه بانصفه‌پایینی داره میخنده، آلپاچینو نسخه عمودی‌این‌عکسوداره؛ لیونل مسی بعد از بازی: من گریه کردم، چون احساس کردم که هم تیمی‌هامو بخاطر پنالتی که خراب کردم ناامید کردم. اما خداوند برام سوپرایز داشت.…</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/25227" target="_blank">📅 18:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25226">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALSQ68lLOkcA8d3qRlKD5z4VcEgtQkVFr9cztKPZ5rtL8SjcLs__DwsYAV7otHY3C4VCWk0Zmi-GN7MOe70Z9bko8cRwF8zSPIfG8IjzV06GEUXUeRJ3e6Dvt9HknZGbmFvK-OATHQxUKmtK9VtgCnbyLMdFV_S0Uqq9zOEv1ShWHG6P3Ey5Q_7eB2uU9rVZARQ8uVFDNRHpZFFWnABQiHvv-1yu9FG8wxxeu8U1S1TT4osSCIplfL_RBQwH1y_fkIhKqPRoKSzyCHCNBIErt4bOjLmwThUxUraeV7a1Wvm2nJcRLHHcsNPiT8-iWMlU-Uxe4cMoROEdOxZA7s0Qmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بمب اصلی پرسپولیس که امروز رسانه‌ها تازه دارند روش مانور میدهند سه روز پیش به عنوان اولین رسانه ازش‌ رونمایی‌ کردیم؛ بله مهدی ترابی بدنبال‌بازگشت‌به‌پرسپولیسه و صحبت‌هایی با مهدی تارتار سرمربی‌ سرخپوشان نیز انجام‌ داده. تارتار بعدِ اومدن به پرسپولیس‌بلافاصله‌نامه‌جذب…</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/25226" target="_blank">📅 17:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25224">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khPyQgCj2r1tjNv00ui0Xf4ZzDkZIn9tA8PmNTq1bnENKZVZJa3uKiC9B2qN05PwLfDCkVJc0nNtDA4o6Jmu4Q_hchxrLgl4RIEbzLfTlMNcH8zz3agaqmO-GE0Yrk54xBAH0Gpl8flvuL6tEjaPLYoDJPKG8vHqZFaS5wEuOW922J9HAS8xmq8nOWA-GKfP-4QG_57wvo6GoA9XYTaC5yODkrk_n7RdeMGP9uVV4gDO_7ocNTzupQ1E_8z1JOg6sHKqcUUcjT7IPCVt1EZ9SfWXcSJX6sI5C7GmuyfCJYGYF-dnK1rnD3irG7J9GXt7kh5bVSsgJ8s0Ql3O_iF2Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
در‌اقدامی‌عجیب‌ازسوی‌فدراسیون‌فوتبال؛ درحالی که روز گذشته چادر ملو با برتری مقابل گل گهر جواز حضور در سطح دوم آسیا رو بدست آورد اما مدیران فدراسیون پیش‌تر نام گل گهر سیرجان رد بعنوان نماینده ایران در سطح دو آسیا معرفی کرده اند.
‼️
همون موقع‌ای که AFC خودش…</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/25224" target="_blank">📅 17:36 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
