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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 03:28:18</div>
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
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/persiana_Soccer/25331" target="_blank">📅 02:59 · 19 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/persiana_Soccer/25329" target="_blank">📅 02:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25328">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4hkucHWRJrGx3bxwF-pC8npo7pP8xklfHAZqIvlkJayJpVWIIQNFmZXpk6Ektw3SLl3pnepsICqCErrBXcCE1Ln2kjMZTsodLACL84qVanPF_SqsBuas8C6BvJUtERuLrQL2rSI4PsaRUUfwk4nE9auRl8IipS7lCrGsboec-chTvPT9U1fHbG-wCs8Jd4C4XT-sp7gOVlKqUwtAGDz1bPSvXaWfNZFnlKBQ5S6q41_FsfRK3wNX5pkt-B_p2VL7x1VbqXws0gXLzYGd2VCjfxIYF6pgOoKbuDSwCjsJCPgFBAmy-4_kqU0Est9BuxelI65VQrGgeVBz4bndT9KiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز خان کریمی برای کارشناسی مسابقه امشب مراکش - فرانسه رفته شبکه ماهواره‌ای جم اسپورت؛ خنده‌هاش رو ببینید دهن سرویس چه ذوقی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/25328" target="_blank">📅 02:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25327">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWLezMyytgoVThdEoRikhUWQrHzdCeImVMDgTsO2PA7D3Z-e9ozpdbaBhh6FCGfL_BxQ47EKk40DNtKgRqBEZrPaJ3N6CL6zl1Htu-Fn-tg3sTqgNqktcgl33BSfC04CvAysb7nLhsrIjurm9s0vVlRu7lRIJWzd356TnkvxqwYgt8tOHuH7m70-GUFH4htfZYZV7BQSTjD-2NVrSFtqpyyDcA51amhae5f2FApSaPV6NO4cOp_1ZNIBkkrnjPEiFD5cE34X70tpQNLYWDgoTSOYpx3TXARWf0pdlQgtcwtDIjOCYofzJC-PQyMuRRJI_zk6nSqrGPpL89ZhRL03SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی جدید استقلال از پژمان منتطری کاپیتان‌سابق آبی‌ها و مربی الشحانیه‌قطر خواسته که به کادرفنی‌اش اضافه شود. درصورتیکه پژمان منتظری به باشگاه استقلال برگرده وریا غفوری قطعا از کادرفنی آبی‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/25327" target="_blank">📅 02:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25326">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aROhzyBplmfJOKMVjZMRSfl_lsozUywVQiA8Ft-AjQWXZN1aHHcW-mEeb15aL8FnsasAG4pkfmiNs2974yz78c8QkiueI1vwGdggvl6u_zYr_s1cZCweYt-Ln5SYDJOcwtOFpcdqkuvBAfaD6qFK7oCocuLjuOCh75LPpJnWD28BxmDogYoikpdMFoJcVkhxEMGpH4Is3bvys8cFMx9C73nx2ZgZ3P3_kyJw1UbFvCXzSOkGwlQICDXmj4sx7ERRfPfrSNQ0rsAb4-li_akbJZ7uGcnI7kgiBFmEgj8C__-Bkvz-86MF4E9fzRVBjUGePZm3Cbo4hqVo5LaS09-xxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همان طور که دو ماه پیش نیز خبر دادیم؛ امید عالیشاه، مرتضی‌پورعلی‌گنجی، میلاد سرلک و سروش رفیعی درلیست مازاد مهدی تارتار قرار گرفته اند و به شکل قطعی از جمع سرخپوشان جدا خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/persiana_Soccer/25326" target="_blank">📅 02:05 · 19 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/25324" target="_blank">📅 01:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25323">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPrQGkwJoghmnppGz73IBtsLsEYYYz4u0_BAM60AJd-gJcZlvmetHnrKj2F5ibf4CCs2y9WaCgeItSDvlzoX5ttGWGY1bdHmn8sNd4Ysb56xi1uf376rY3J0J4r5XvTcq0LTPcgFVsabjirh8Msd3KFnSah1Ey2ig-YU0BsO1UuhuzvsDGqIVRRzF4VvvdJvyBICBPgbQqxkWgGfcseJIBcq2XN2rOaEFcvWM57Kul_GH0qhgjFv55zwHgg5t29xr0xivajQFDC2AuRJDYAk_eMtDCmgW4c6JSW9BFahdtUVWo-9tn2prmHb_ducr_11P-Nvz5OOkF-LDamkgtS_pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌امروز؛
جدال‌اسپانیایی‌ها با یاران دی‌بروینه برای رسیدن به فرانسه در نیمه‌نهایی جام‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/persiana_Soccer/25323" target="_blank">📅 01:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25322">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwECH4KUsUlMItlJxkL5ab1aYPWpdRgVwtJMJWcvxapS1MnM4k67wd0yPRzjC9KKOPwUjLSVtjdVgDoBrT2TI7L6QGlML9n6NsAvZIRqC8B5ZBYcXJJCOnnK04e0x0A5veIh0y4fZ_GcyOHKwbtjbGPUxezDxRkvPuHVG1U0FoB7azkmxbQub3PT2_q41nFDSDPOCjy-Iricp0DqQSZRG5VUTq1o9wOLs6ZiCrJdcE5Ev9CtgNTZdTBDOVs9GtveWVWFpKE4ktZcubxgu5fmO9d0SSoZtpX5pS0fCzDmbNdepGCGKSUP5AGd2c6Waf_9DK2pi6dPMZ7ttv6c0NruQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
برتری شاگردان دشان مقابل مراکش با درخشش همیشگی کیلیان امباپه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/persiana_Soccer/25322" target="_blank">📅 01:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25321">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXeo5Us5VAMaorcYNjGdhx5NmPPod5uos1cEdGSJU14mujlyOd3xduqZ8OpuU3jKKmN8cl8_4zshmeX3j5qCBNi3ReQomuAC9XxNMzmypk96LYu5NUuuvxupQHb9vrSDw8zFcU5E5sy4EJYYuqTd3XlsGnXJNsB68Hb5Zd9Pe685nQHt_gUFRg9RG1zbDVpypoc_XgEY_6gRYHQUZ2LY4U_WBiCuJ2nzpFVcJpuX40zqo02kse-k0JQkjgLI4QfGjl5mGkQGxRGBZOz3dnb5zWfPV_MVXScAQeBSSr2-XJHGL9vE0Q6iyDhnX2wRj896Ja-X2e_e3Ki8IiGWs1yngw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی؛ مدیریت باشگاه پرسپولیس بعد از عقد قرارداد با ابوالفضل جلالی و پوریا شهر آبادی از آن‌ها خواسته هیچ مصاحب‌ای مبنی بر عقد قرارداد قطعی باسرخپوشان دررسانه‌ها نداشته باشند تا زمان انتشار پوسترشون‌توسط باشگاه؛ بخش رسانه ای هم پوستر رو اماده کرده و بزودی…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/25321" target="_blank">📅 01:40 · 19 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/25320" target="_blank">📅 01:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25319">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhjM4cu61bikvJpnzDFByalaSULkoQp5Ny7CikJG2g4QuA4rPUZuzq8QRYZKt7fpzdh5jNxTUcBxqiprjS6LCl7scwKF6jmENqDjIABSLTKWFxp2tF2k7IbhY869QMv82jrD3hpvAaTXicEUKrhWf7s80bAPHXUBAbm2W5D4KMthzBsQttSKTmSndi2xmd65py0u3rlo9uDr1WPNthgXsAhB9VAm5StYxnUykur91KCyFSk5iSnZ5UiJbZutrRSBEOsYt8AeDgvbEhMaQBX_iThDpwUtZWEuO_epCTKODI6ydlB55s3n_BeRnLueIo9NE5zQhUoZXC6D02efqdn7-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/persiana_Soccer/25319" target="_blank">📅 01:25 · 19 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/persiana_Soccer/25318" target="_blank">📅 01:25 · 19 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/persiana_Soccer/25317" target="_blank">📅 01:25 · 19 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/25316" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/25315" target="_blank">📅 00:59 · 19 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/25314" target="_blank">📅 00:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25312">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwsQQdTyPzE-PN1-cnwCJjcFSIl1nBSZkfL2cJ1y82E2IYXH6e6Yma1C7M8C6H4KvNvw-AEhNCOvzjlR6ZSAP3gGGz_4ALA251vUegacMmkuWHjcjCi1MwtRvEBqSevhEwBkSVjiPMWDIXKe-6qT2V8ICU9VJcmJYroBE1rybe-nM1o9-mTIo3_LKVCLC7UBs6hccs9ZXm4EehskpAJVk8AP9T2mUr_166gtKJ-zoxI046UYmdWK1fS-cyujG1voGCDofaeievvLlvOJBpTivnngULGrhhgARIbrl_zciygnvXazCWhkN-HCYlbp69ZcCHiRBbecp1NAR7HlkrKyPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز خان کریمی برای کارشناسی مسابقه امشب مراکش - فرانسه رفته شبکه ماهواره‌ای جم اسپورت؛ خنده‌هاش رو ببینید دهن سرویس چه ذوقی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/25312" target="_blank">📅 00:13 · 19 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/25311" target="_blank">📅 00:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25310">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6Hn21ybijLjbJZk9Oi1tj4H5Cis1Qs8mnk7KuNKi2npNSJBvfRhOC-GQhBIYUjyOi7Q0qd0g_XUAoTeNAxUQKwnLKfglj6bfzPlpnY_AL_JooqfCJfIHOFnHNTJZKqP-ol1aPFQQdLFqfH-OVjaI2guwf8Az5Uoauo_8yCgumPKpgVgeZIvTWKfnnp9hsB-rl-eEHNyMoWjy4GmBzHxWBRhqlPDI8Rtedbm3-ILaigEnY4qN1625qOUxvwK0SUM7xnSSFIgS5u-gJFykYZssMC4fo6I8ua1zYoFaVTSSKC1sx3J8Lm_Oa0HbfUoWSv2sK8gG8Vsl4R13_66zNt1dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌گلزنان‌تاریخ‌مقدماتی جام جهانی در آسیا. علی دایی با 35 گل زده در صدر و سردار آزمون با 29 گل و کریم باقری با 28 گل در رتبه دوم و سوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/25310" target="_blank">📅 23:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25309">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJWN4WHzvvpTJ2RM72kMEU55xrjMMr26mXfxCOrCLSTW1cOvXCefK1xs6fDMXHyShcIR74BOeGucpLrRaJgy3lvMBfv8azgK1ctpoMxp-gF9T4bRAfKZPKsV8tnuxH8j8GRh4nZf9GWZBSNt5RHyQQeufUdTUEOdWvV161DDm2USvXXQv47xUR4WHhgV06p8fB0oKEVrGMCtUuwngfewS-wApfqamsE2nJYxggKt9W9ZKBe9jReXBxrOeQcNS6fiwotIyCoUSOQ-crmIXKz8ymwzqdiKoMR8z_MJJwg1YaXthBiR5J8QKHzG3KbRMndbYfe6y0_TRAq7_S5mL1utkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌ترانسفر مارکت؛ باشگاه پرسپولیس برای جذب پوریاشهرآبادی20ساله؛ سهیل صحرایی مدافع راست جوان‌خود + 500هزار دلار حدود 90 میلیارد تومان به باشگاه گل‌گهر سیرجان داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/25309" target="_blank">📅 23:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25308">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/de7wR_IrWchBMTkLJMj8QwG5_7NuUg3CL3CDwySq71eRAeoNxL4FqtV20vCWGxw_meIjxBwylZxRlA7avO4VC1eSeEWX9VrRqWZaeY5-WDmDXvG9-9O9nadZyjVWmVr8RDCnQxslvzDzvRQy9nOp2Rko7bPHppoKXX_IfQP_pzmFyiGhWH_RABwus664DjMX0Eml8m3i82NVgF6yCQJ-P2_z7RQTBQPRGUzBPARQ4fbtnyWQXPTJhHk2HYqao1EBEylY0MNb4zZxeATSGmxBbox0NtqBp11ekF4uUNB84TQ5rsmdf0YiQtebEeN9Q_F9E8quJtoSM544Abw1AqKXxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
این‌بخش صحبت های فیروز کریمی هم عالیه؛ میگن الهویی دستیار امیر قلعه‌نویی گفته ما هفت تا پلن داشتیم برای جام جهانی؟ مگه فیلم هندیه اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/25308" target="_blank">📅 23:31 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/25307" target="_blank">📅 22:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25306">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6FHZbkjaVy9f-MP4dDAqpvWIZAO3gZFshi91RZ0EXdNxN_dVaMnhSJ0JlBbHhCF8kGY4YtHJkxxQ-7y3chUracNR74vrUyjFTUUzzqZHR-3KL8qtDkX_IV-1qTvBg5TItZHZtti--2IXfwl6gZG7a2bo6Djitv7x2cD3RtLr__sIc1F_txL3sRHaT_bMt-AYb24T-8wCdNo_KjRbexqxhKi3n0kSsbmRvqf76zrp1lYwzGDnt8qAUADV3RoYaau3Ks3EpVirmJ3m53Vu3q45-BjDvZqncCqKFHIlPvvIhZMk9mwVRVGo50tsVvyoiRJvOaU7bO-twL88aaAroeqQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی‌پرشیانا؛ جلسه مدیر عامل پرسپولیس با مهدی ترابی در منزل این بازیکن برگزار شد و دقایقی‌قبل به اتمام رسید. مهدی ترابی برای عقد قرار داد 2+1 ساله با باشگاه پرسپولیس به توافق کامل رسید و به پیمان حدادی اعلام کرده درصورتیکه تا هفته آینده مشکل…</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/25306" target="_blank">📅 22:47 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25304" target="_blank">📅 22:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25303">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxfK14LyCWj9xZ0O0_yNeksymMnzVde7uZVENjG5uq1vROR4lk0poY7IzuqHz7UMLYJwlPHvO-lfo1DoyDSg7huHRepzPlVFI0qe3NFvBrlNShX5Jnh7b8tg97q7HCib51G24Dc3yxaKH9WQ4ntPXv7kIPAvVo2zueAzHuCf3x0R6ZnzmbYLzcT0UCV1e_IETJNPfNvenUQovVoS8kgG8MJyC7I9X3dPgBy341Eb_lQy0Olg53NjONObYARQhO3V_R7NdbxMKS_lWMUAlEfEpD_Gln5efa5VRtG22yeg_gjF5Udpc7O2f-iJ8W13BVBxw6kDBIgBtj5HJMhY1Ws2uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی‌پرشیانا؛ جلسه مدیر عامل پرسپولیس با مهدی ترابی در منزل این بازیکن برگزار شد و دقایقی‌قبل به اتمام رسید. مهدی ترابی برای عقد قرار داد 2+1 ساله با باشگاه پرسپولیس به توافق کامل رسید و به پیمان حدادی اعلام کرده درصورتیکه تا هفته آینده مشکل…</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25303" target="_blank">📅 22:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25302">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZjg-bepTUOBdNybqIBPyh0r9CB07lBEpN7vO7mF4q0dv8daKIIcYlhrHXZ_GNy5GV3PkUPPWY_bsxjKlX-cG6cOU4KAspWBo0761VuwN6qPLjJ3DVPW-lfNVVBRCrSxu5fSotLTYSiZdbX4na06C23HmLaiAtpZYx79IRbwJSsqnb3ceE7ptcoSx4wJPa-kG3_yZ9MAVz6Bkf0A9UipWItdRCTO77IkaVjVQ0NHK20EhgCGdUIJ_WJmVsdJZ-MtrkVqgthWFZCbk9lU9YYOA3JwUa9po691I6dkTMGWqyRxZYbBes0pi1kF_4i5HzJeUHj9D67ddmcr4BPx6WDizQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جلسه‌مدیران باشگاه پرسپولیس با مهدی ترابی و نماینده اش شروع شده است. تا ساعات آینده تکلیف ترابی با مدیران باشگاه پرسپولیس مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/25302" target="_blank">📅 22:16 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/25301" target="_blank">📅 22:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25300">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxkjPg3ijis11g27MYenI-XglC70WSRUdRmvlDhX_MeOBCoxB3ASsYmCW7sdlhWpae9Y_arQ-K0hoc-uGsSuT2P1ERtd2pnCjyVLdaxldGa1ePWKkuB6Ovygi9U79Z9g41Q5CyMmSxbCJ4dcDJIkSXNHJYzLc9DMDGTHatDTAJE6WOx-K8-nZNhdHPbgna_Kfd0WGkRmS32ClchDo1OF7jxzcyBAQMbX6fUL25K-N7kEoqLRQgr02PuQBNzpL1irLSZJtdcoiGHooembfd60gswtMZ1_uLNbYByWZzRWAdpwmVyuxqy_kG6bKwNPrEkKcKJhiCwOTBw4BwRh9T216A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تقویم؛ بیست سال پیش همچین روزی ایتالیا با غلبه بر فرانسه در ضربات پنالتی قهرمان جهان شد. با این حال، این مسابقه همیشه به خاطر اشتباه فاحش زیدان و ضربه‌ سرش‌به‌ماتراتزی تو یادها باقی مونده.
‼️
زیدان: از همهٔ کودکانی که اون صحنه رو دیدند عذرخواهی میکنم. هیچ…</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/25300" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25299">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bb2pG7iZEzqYAvzj-g_C0CSwGHBQ3aqueK8qO73k2M655S_ZtahGFSVgz4-96KJPmF5PW2TDta3oERZy5A6XDh9aZByujWMEVyvJRR6OnBcN3aZVpi1CNh9zQsD_AMXGshTSdgf-9CE2gU2V4KW_obGUezpoFAsfhPVA0lkfCP8Aahn289wbCmfapcf-Q_ZXmL2_5TUgO9xT495GCEq3PX9l3c6Tu1KgE-oOhXr_2kN7Po-f9qDTCYnCqRu5od8Sf72idM_XktgdXdt_OOhM0KesYrtqMN8hJ6W9A6YEDh5jTNl0YSmdLH-p34db0KKi0ddNN-O9guJJxJHlZRQMdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
باشگاه یوونتوس برای عقدقرارداد دو ساله با امیلیانو مارتینز دروازه‌بان تیم ملی آرژانتین به توافق کامل رسید و تنها توافق با آستون ویلا باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/25299" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/25298" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25297">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYpcqdD6ByE2owceYe1wNzOxdzz444wBctYch08YV0HCGWUvRf8ThqzWaQ8kskHyIYiwTuMc4P978FaDP8GZxhtkHT2ZEyzNprm7A0SKsBfkGDbHyA_RHgxdWiXLQEfh6pWchlmEOCS7fXdpWuYOmowRFceLXo5AYznldtZogceyJCkOvewidk4DhoSZ5sP6ERQi7sSDeNgKiyUIvp5RZ5tcOaRRe_7g7ResM4GlpDVdIx6CtGxyvtquML4ZApQ8fTnpZOoI5CSvrLlWJozNXyh8hv-dAYu3c34uaTLn8xA5JFrzjB5ABGc9Qg5aYFHrg-39LDWDsFBI-jUCxYCNYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
طبق شنیده‌های رسانه پرشیانا؛ هفته آینده جلسه‌‌ای بین ایگور سرگیف و مدیریت باشگاه پرسپولیس برگزار خواهد شد تا مدیریت‌سرخ‌ها این بازیکن رو برای‌موندن دراین باشگاه برای فصل آینده متقاعد کنند. سرگیف بخاطر مسائل خانوادگی قصد داره فصل جدید رو در لیگ برتر ازبکستان…</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/25297" target="_blank">📅 21:30 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/25296" target="_blank">📅 20:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25295">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECd2-Pof3kcXpG-i23OY2bvcjPl3FbAQj0_5QxHpCep4qDI-Z_Kx-u8i9M3FA2ro33s5_oGNE53P60ORzjbz7Kio_wExNQjevN_ntnQssSMmfo-MIpNGCaYtegdiewnfj2ij0mBqgc2QCZ1molzjPgfMHnC3yFVJ1Pdd3wI3nXBCVYbsZ-RFdKJvh_wJQ5et1BE3t10MLQzNP6xHtFjGp274BQkpFX_BQVw6v4-5rJJoiK1mgdamm2qJ0ZlK46b6ZW9Efp6D0MxgeM6E9gniGlgy-WO7YRFGqzI63V6S7CavU4yufo0R5v2wlmXWJVisdm4mCjLONiCOklrsHtXojw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|داوید دخیا سنگربان اسپانیایی 35 ساله فصل‌گذشته فیورنتینا آمادگی خود را برای بازگشت‌به‌باشگاه منچستر یونایتد اعلام کرده‌. دخیا میخواد دو فصل در منچستر یونایتد بازی کنه و با پیراهن این تیم از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/25295" target="_blank">📅 20:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25294">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeR4EBglic-yaRXxYbZ8dvsCMLi5fGt36_XcYBTV-r6zoDMzIc47Ma8l03Fj31JqXu1ak_Vu3lOcVYCO-whAjiu0nIa0xo50FdTL2OdRkro_dcD8ZDkxoIVfuLmP-151Bkx-e_Quit0VlLmnRX6e7tcqdU4AgdQQZfFq3Wp2i6HdDgJgyBfNoJ4puH1gACJtwPetixUGFpIdgTKlqOt9U4sw0FqKAbD06FDGOKfIzsyKQgEaXBxl9fwUnwClJnjXxLIIJmVStmdklJvJTwvHnEDY03MQ2MoLhuYnHFVKtlFop1vSR8HWqO_UVrjmUvUgp4dcaHizNRscXhF6ZlSFrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ طبق اخبار دریافتی پرشیانا؛فرداشب‌حوالی‌ساعت 21:00 مدیر عامل باشگاه پرسپولیس در منزل مهدی ترابی جلسه مهم و سرنوشت‌سازی خواهد داشت و احتمال اینکه قرارداد 2+1 ساله امضا شود بسیار زیاد است.
‼️
پ.ن: دیگه داریم لحظه تمام اخبار داغ نقل…</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25294" target="_blank">📅 20:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25293">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ScvYfv3Yx6mnjabDVqa1eNDtyKS1gC29sUi3PMM44ATiiAWDq5YeudvqHvvILNnrKJ3YTgV2xvegCiHx3Si_3PSgGRNGFJ3-kZSasXUoIni59YjyXXL3aKJD8BFbVqUGTaVZOG4KJUfQFa1BpohCTu-6kXTvoKJ_Sibn7YcrLoC7FLCrbrAWVe7poFYynCjiLmSvwruEONVbsruUVkIQ5JC6702nI3tJ3IabJWxwwT8PIF6BqaryuR1QIoZWs_fczl8PjDBu9BxTuzdrW5cJt9pubSm-uRsAOh1Gtjd9BOUE6PhDRE0Chj88rpOPakZym2cL1rPqL_GX-l2wBXhphA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امید ابراهیمی هافبک 39 ساله سابق استقلال با عقد قراردادی یک ساله به تیم لوسیل قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/25293" target="_blank">📅 20:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25292">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFvXvokSLGOoMOQmFrta65oZGnSrEd6DpChpJotJBYtvskj1BpzS8NRuL0NBiVRDF49X25QG3n_AhFPy9nTCi6cVFgG-gE2Cz98hlrxaQReJR_kQ3M_TJ32kab35qRF5CEfkTXiXt226lmxepJ-tTB5cWt_0cAQfM2aNpE-VsIVA2SCBPtDB4ezzA8Bnq_gg45JUJbtpvgGrFkbVGbjS-umWjxOMy8h7SpJxnmBg71h4uudBvJ2oYj31li5-Ea3qEb0realGecUpmjVTk6B-6Dc97C2378Pzu63cCvkZZRDB_-w9OKLCSY4Qzq8FxRV9TcE2maS4iOLEsobTqvqd8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هادی حبیبی نژاد قبل از اومدن تارتار مذاکرات مثبتی باسران‌پرسپولیس‌داشت امابعد اومدن تارتار و درخواست جذب مهدی‌ترابی دیگر قید این بازیکن رو زدند و او با قراردادی دو ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/25292" target="_blank">📅 19:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25291">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtGw8sMoPUPH8ovB8C0blxZkTLd8zOkGPRG5pu-LyDLXjUKJusMf9dXDJlKJcJF95izKyVo0d6fuiLLPVpy65iXo2ZTejtzNIoxbRY3uhxgVb6xnjD_pneKIWCvOn7pDPI8k4ODpyIQTAqHQBrpGZCgGfnQMNCXADS1Bh-j7FqXtezCCNDHijJdFc_n4x-dssfKkMAinSYDk2Ei0M_HF_sZ4fUVvKyVa5XabtK5XvAq6rSHygjGERhWb2f3_vDQ_fZ_uXWdsLh_CqzdA6yEeBzb-yMyJ0W-h8W7JdRnTSfNh_ew2qqflPVXHAhqionQVcFf5CvH5ojMSfs4V8JrC4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیرورزشی باشگاه‌الوحده به محمد قربانی گفته هرباشگاه ایرانی دو میلیون دلار پرداخت کنه رضایت نامه ات رو براشون صادر میکنیم. همانطور که دیروز گفتیم باشگاه پرسپولیس گفته ما تا 1.5 میلیون دلار حاضریم بابت رضایت نامه پرداخت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/25291" target="_blank">📅 19:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25290">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KafTcXypQiSxtVeCuN9kcFx9aWrCfo8k8WW7fQsiUsaFj-ydcv88URyKPTeA_kafj6LxmKDWsjxNL5Ql4v7ahtnCmqel6P5IBmmkKy-bvZw0xweakzcEt_wG4DiG73Afd9mUcq_2X-rL8GBq0p_BKOOH5VbrGU9l0jL1H1aNuwVwi70g7JFclA0PT4al_m-CAb7JbOStqeYHc2zZzYo0NZE8MjbzJsBmpzB5HSgI_oD0QTsh-PhgWLZMav2jW9TUElAKssZbxowsd6k17LH1zBeRTllXTNWeeOTU5kbgNhHksnTmlLitjJyUNJRXHGSf7YIGMJ_EBJBPSp7__S-55g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
تونی‌کروس اسطوره باشگاه رئال مادرید:
مردم همیشه دنبال‌بهانه‌اند. تکلیف‌فوتبال‌در ۹۰ دقیقه تعیین می‌شود، نه یک‌لحظه. مصر نیمه‌اول عالی بود اما بعد از اینکه ۲-۰ پیش‌افتاد کنترل‌را از دست‌داد و آرژانتین استفاده کرد. این تخصص تیم‌های نخبه است.
🔵
مردم مدام درمورد داور و VAR صحبت می‌کنند، اما دلیل‌بازگشت‌آرژانتینی‌ها کیفیت و ذهنیت‌شان بود. مصر نتوانست‌سطحی‌که ابتدا نشان داده بود را حفظ کند. اینکه مسابقه "دزدیده شده" یا به آرژانتین هدیه داده شده تئوری‌ توطئه است.
🔵
بخش‌سخت‌فوتبال پس از باخت، پذیرفتن اینه که حریف بهتربوده. آرژانتین‌شایسته تقدیره. مصر باید به عملکردش افتخارکند اما از اشتباهاتی که برایش گران تمام شد، درس بگیرد. فوتبال همین است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25290" target="_blank">📅 18:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25289">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1cjNnMDqGQN6jaDkV1KiyOqbkxa-bQiL_yMTqguFgNX0QY2gjjyNGplJCNlcOtLUmNuwk1Tk52pej-OTYawr80n8NwfstWjPB9HMGUVitiFGWbW28E0KZsiDanl1JL6UaHMQ_GNPC91AJYhOs4qZ80uK2JBgXXEKw_ezJqvV_yTRxFLSztuHtvtliistFWewrwIKqXOEGNv1Bi4mf3GSVKdiVtCP9wzC3dc-Cq7fgJlCoQ5ZUXS52OwMNe-8CM31Axfk8lMglt2b_3bSpyYBf0_EApWMn9I4TTm1lrgcnC3PLxz_z5VHseVgWFfBy38lVK0Cr2reQvF2fDCr8OXxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25289" target="_blank">📅 18:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25288">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8P3GDpU2qDYTPoiChXkgOEa75GBAvbLJos33uzkHE4Cs8F4ukcjKiA9KOVFFJ3E2TTxL1TTE5STr9Dvp_KjvCdftQXW4aSsvbtqTYBKQuRGZXBJ-jTQyL7SkmrVm8_LdQ_SzLKYW1QYqYAxY9cvzobIprMmU04Zu2Pkyp18kHvdWWg6RPpOSmqUhAbgF9kIBKHQTVppApl1FeJBxikvUD3VplPgxfJRoLDTXl0rwET8GHWJDc1iw2YxZF6cAUoAObBgg94QiHUOWSEbu22JT7Jo01VuZndZoMub1Rqmgc8yBV8-ArGnRA6GxkWdcwhOjSrI5avXRRXE0E1TgjcTXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تقویم
؛ بیست سال پیش همچین روزی ایتالیا با غلبه بر فرانسه در ضربات پنالتی قهرمان جهان شد. با این حال، این مسابقه همیشه به خاطر اشتباه فاحش زیدان و ضربه‌ سرش‌به‌ماتراتزی تو یادها باقی مونده.
‼️
زیدان: از همهٔ کودکانی که اون صحنه رو دیدند عذرخواهی میکنم. هیچ توجیهی برای اون کار ندارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/25288" target="_blank">📅 18:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25287">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTdbAIaNw9r-p2W6mW_Igkmr6jzvmYPFamVM0g255S58GJ1sRUdW_O20Y2H-kIHEGznrtiUSCfAvuz22UYqZ1068-pmVlHo4eHrMkotyAzdSqNRoTtplH3kVKvcYNeCR5TEHFGGwCGXHvRerLcU8TzVFbOewzjNS9qKuKN1iU1TSzDF7jZ_8SYqyBAbOhvxtnnzrwO2UkV2G-7QPdmmE0kiV98I88lGuGbeyU7YRLORNyp0rtp7hLW3GsQU2V4irGR2shexXva2-WqPglU78YWanYnoEJK5q3omUAHWBJANxTDDcEDvuqJLhxK9OC8MK_n7fiEYNw6f2UK08y5MRsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ طبق‌شنیده‌های پرشیانا؛ مدیریت باشگاه سپاهان درتماس بامدبربرنامه های علی نعمتی خواستار جذب این‌مدافع ملی پوش شده و به نعمتی اعلام‌کرده‌حاضره‌برای دوفصل‌حضور دراین تیم رقم مدنظرش که 150میلیاردتومانه روبه‌او پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/25287" target="_blank">📅 17:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25286">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIIuUWvQUyI9bat_9q363M-EFu_LWPMmw3KXoVj4-HRiG3efYmssLzBYoRnwLK5XetdliIAdQZyyRjaT2KobytS4dR1USICBfiFa8eJuOj_rLicLcCAL8grW7AKd-wrhTQliTINoI4a66F6SDgKkax4ycSVpka_RrqGWO60xgcQDkFjbBBcN-mX3x1AOw0fwBzUlF3fU2ZIpwiD7T4EZkuF9L0izA0cZA70CD5oyAj2hH3dQXMdm7YkZUxafrGNNmhjkGUkMsMNm0Ybu0e7BRLvhNBA89uJX1FI65qrsyQ88a3Fv618do699izTtARnppQj-wOSJQ6udePe_Wgk-Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
درخصوص اوستون اورونوف هم پنج روز پیش خبردادیم که چندپیشنهاد از جمله پیشنهاد الشمال رو‌ی‌میز مدیریت‌سرخ‌ها قرار داره و با توجه به‌ چراغ سبز مهدی تارتار برای فروش ستاره ازبکی درصورت پیشنهاد مالی مناسب؛ احتمال جدایی اوستون اورونوف از جمع سرخ ها وجود داره.…</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/25286" target="_blank">📅 17:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25285">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLqSS4bCHfl0JHmNNEYWwrZSkHWFvbUWWyLzb34ST5i3hQptmzjk5imn3ji6V304jJFaZH2Vj3gGHBSrCAX47oPXJYbVV07Z_VsqJWWri5sX-b-s37QyelVMFEg57ygMgXFexo0HyfFB0lGC9Enyaeb9Ev712bzyO9VzZi5VwlR2JdDL4gpayDsT6totAoVodz1kQk8-bASc9gkPd5OFURwmpzfLC1IYNCYTPVpHvgoAGnyVR7_vbt8ofSycEU70OsikEE99Rjh2AYAuHkf4FXAL2rEwaifxUfuS17PNndjvhwZH-w21s2d4e-R8VO7LGRyR2LnSJWvdD-TpTlWw_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
ارلینگ هالند روزانه 6 وعده‌غذا میخوره و حدود 6000 کالری مصرف‌میکنه معادل 24 چیزبرگر. هالند عمدتاً به‌مرغ،پاستا، استیک، ماهی، سبزیجات و عسل علاقه داره و بیشتر آب مینوشه و ازتمام خوراکی‌‌های شکردار اجتناب می‌کنه. جاشوا کینگ هم تیمی سابق هالند گفت اون مثل یه خرس غذا می خوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/25285" target="_blank">📅 17:47 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/25284" target="_blank">📅 17:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25283">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KbJoVCuLeJG9azTkURJ0kOW5FP7AUbvyDQGZ2RKQTRGd6wnEJ6lKwDoKNUx0qXBiugExFEJ9-_Nn4Rs4BypKdTXcK2KPY5yHdluqgHxYM5djp1YtV5isJA2h3-aDHc30m9CuA9bzrVZxC2LuzDYGOw48XqrkGux_Oq6l8k3ubiKr7Sc3osACXs3RKj7An0dYqoFil-bFGkPMCS6JEbuXE_7yqu2F3mZePPWi-7qk2LL-1CA11TWZUE3eTU5fVB5e-Q8WxpjmrUPtUL2pavd3Xr5z8ibLbytof2_71rllo4P9mvj0DUCYwzIs7bBonOThH66XEasRT8pekgbCBfwlLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
جواب‌ فوق‌ العاده رونالدو به‌ سوال خبرنگاری که گفته بود میتونی‌ اسپانیا رو ببری: من تموم تلاشم رو بکار میبرم تاوجدانم‌راحت باشه حالا هرچی شد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/25283" target="_blank">📅 17:03 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/25282" target="_blank">📅 16:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25281">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVIKb1HbMI43dGkKS4lYIjfOCbkpztzZqjvOw8oaJ9-m_WNRh_qXDqRCQ8fUGL7ga2StwSN2EUV6NiARW7oto6McuhudYxk4ztHpm3ZEHwexlC3Uy4lak7Toc5sVOh-IcTh-JQr11rROQkfyBWXbOdHQY7wfnx1or5BSuFxoFxYcGfLvoHnnms_aJ7l0UiQY603X4httnOzPTK3FeMtQSXbl46vvdztB3uxY44i1Bx0t2cap29iIsWka0ZXjAXRLfVzQ4Hmt9f9g-QSkA9rFUuPjRNPL9Pg08zWrQuFpvwqTQFL9u934xA9GfVQvS4dCryo4NFPWZSNnG_IXsGjIrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ پیرو خبر روز گذشته پرشیانا؛ پوریا شهرآبادی مهاجم 20 ساله تیم گل گهر سیرجان دقایقی‌قبل درتماس با مهدی تارتار اعلام کرده که قید حضور در تیم استقلال رو زده و اماده عقد قرارداد با باشگاه پرسپولیسه. بدین ترتیب شهر آبادی ظرف 48 ساعت آینده با حضور درساختمان‌باشگاه…</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/25281" target="_blank">📅 16:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25280">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‼️
رونمایی‌از تاکتیک‌اصلی تیم قلعه نویی در رقابت های جام جهانی 2026 که سه مساوی بدست آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/25280" target="_blank">📅 16:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25279">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BusTLhoQi49vkjPFwji7pimaUS6g2U-zFLxiqGRKYJ0ri_kOabDmJ9yiWuKn_ADDc0BzYOGwqtzoXWC2U8dnr5H8P4-4M8ttJg32jvNKMXhoUTTLCD6mfiQlNW3-kDhIJdnKgksu8pKvbczBSejznhQRorHS5h62c-R-AhgiiqpSoBFbyVjMoZP11oqYRRLcClhGYFaQLfAivRBtRLFSULCcU9tEDgVxZUImWjN1w9MNu_YP4I82nXSrZOyeoQBLRdVBS-GRR05f1rRs-0Y5uwLky7qy5c78a-G4iSM0D5gx63jq0o9ND9EvkV3PuVlkyvBm4ipv3swH0-NuMsoljQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدیو لو رفته از کلاس‌درس‌محرمانه امیر قلعه نویی برای سرمربیان آلمان، هلند، ژاپن و برزیل در خانه‌اش بعد از حذف این تیم‌ها از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25279" target="_blank">📅 15:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25278">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulmn7oEJFZux1_s-hor4G_jl_EP0XZdg_1vEQMyLIwzj7aVWZv85frHfXunXKQ2bXwpBj95U721o0d-I2cYq-thTIWuU3db9HMkh7hVS-yFXOK78IRn3_woodud5ZObcniiCYY7R40-a50spET5nB8S2nWqUWTAQvKiThA60qvEqwTS2Oxu6KThfGD2RiY8_d1uy3bqMJEBZmqLReoUdPAF6Oc4oS7IZ74ofpKKvLTiGBrmXYCNQ8Xkfrny0gSyVYSL2x6LsA66OY9BUBuAWcvpAzzHGPXxDJad2VxjR9qLL8kYJkJn4FRWaPGCYgDtEJBeCiMvpKEJPHR6bEbUWtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛مدیریت‌باشگاه‌استقلال میخواد بعد از تمدیدقرارداد یاسر آسانی قرارداد رستم آشورماتف مدافع 28 ساله خود را نیز تا سال 2029 تمدید کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25278" target="_blank">📅 15:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25277">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrn0MPH7Q3I785rAlYRh6bXmEoriPndaB-1oWPrwyIbYCmp1fmGl__uicYvjZq44hwfdMcc8xJmlFIqFF236In9duQKSZM2fBTjFm7FcbvOAko6DXs-N7suG_c63PLN6EJboIq4S0HPflJIurYNqYJSeRxkJQFUWWGN2ygK2gtr4l5Dm_3iCq6xf6PYskHZL0iT5jWY9tnGVzW7h3u4dGO4eaUynusUy4XuIjEJ8xnTjrJRu1qsz1a2u9nE3ejQfp6ZEUlCnAVmHzAbJx6gCpKSkg3bw5I3pIMKBsuzSV6KfOWP4PnfB9_Wy37DcjAlgjIQu_rUvkfX4XjcCW26ElQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
#تکمیلی؛ کریم آدیمی ستاره23ساله بورسیا دورتموند برای عقدقرارداد پنج‌ساله با سران بارسا به توافق نهایی رسیده و تنها توافق با مدیران دورتموند باقی مونده که باتوجه به علاقه آدیمی برای پیوستن به بارسا بزودی بند فسخ او رو فعال خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/25277" target="_blank">📅 15:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25276">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ratPZP9YCVgGMrOSCLvvYNLXto88ZLJ6azYTlb1NhMhxe-xKWaniOZzIZoB98vXJJArX81lLQ2f1cLXpcvy9t0OyFBAm1494c6r4ozqEBtjno1y2T2ZmnM3xa09FqNfeTvSuPvfsQ8W64gDjHphrfELuN9YFkO7JdP5z7D8rXj0mbtS0LtSr4iyc45jGDdUk43d1uFGyLEKHI64AC-Ihip8FeADBCfLVpNRtrOEF949Sq14bX6HmfOPI3RsGBsD9Fj60RyUh-ybR6NCHAbayDZ1eLvcu3efbQxX5TJsBPivaLwNgQJZETLJwRJIF9elS44ThkZxqWZOsQTjid92btQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25276" target="_blank">📅 15:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25275">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqLCM349DB4rgLqLPtSpYTG8QxS51Lj65tKeERZjVyQC_cMSy01W1oTZTXm_gTpbCZPn9W33YM23TY5RCGKTPx1k6QWBVwejuYom5eYwppcKE1S4_Ylb8427I8S0idg3antTaNur2U-JlO1ipav_xmgibPd-8VZDHg8FFkGkFc1ExNR4-XzLhoWlqzOGN7ZLQZZQuU-ozfZ3YsEVNJVUDgTluBzxH8KJSRdoUYJB2zVi7OTKIqHJBDJhAVrySN_BUzSqh5xRqDN1Zq-9-ANymxDzSrp7QhvHStq4v7NhLU4g__hdK7FY02AQ50-yvSpxzXPogFAuHwAJ5NbWL_vfRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی؛ ایگور سرگیف مهاجم ازبکستانی تیم پرسپولیس‌نیز درگفتگوبارسانه‌های ازبکستانی اعلام کرد که به قراردادش با سرخ‌ها پایبند خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25275" target="_blank">📅 15:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25274">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZuuM1Qgh_pUx59eb-aZa9qOSUMtXcC8ReuhWTemUj-gA7Kxv9MMOLgGJ2w7Hm3RqOcu8kmSa-tuLvT7u5HJdf3jymj7iaSLf6Shtu8NO3zzM5giMX_bHa-OnVdXsadCpIUOXtBaLuJHVrraO6uxhERuBGNmLWONFLBkER_nPs5lNGC9T3SPrQ1pkdyIYrrFxI4ZAANbeNfd3SIYUHx30t554lx5jSFla1rT506W8AMnsGXuepE9JpUSqtRenc9-bDLsBu6xyrYH0c24mijCqvfJF7VScrref3XBP8TGcJe5kDFvPCxaNn8NJ2PTmXWmTpHQxCLq2txKrVE5MljVEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
آمار فینیشینگ و ایجاد موقعیت بازیکنان جام جهانی؛
همه چیز خوبه تا زمانی که گوشه راست بالا رونگاه‌نکنید. رامین‌رضاییان هم تو این لیست هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25274" target="_blank">📅 14:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25273">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fe2Dz-AGFNzo0d4_E3DhMQ1fmTyQYobLedARiQwdS08v8RVWoYQ4yHbLWlZutBKqwhCT6m0wXnfR3awYtZ5T2zy02DitplJRIUbh06F7gZyFIskhvPyo0HZrGq6v5oNsZaMaClN0-Ob95ETCmS5XSJnMXkgqoFtEVN0z6gl_sKrE2H2FvnxYKKdi-XJyJCABatd0Eu3kuZjzapu7X8tboxGMx0MC7MjDTsaTOKu6wyb-KIGyJGGzxgERzDDwXr_zOojcxn95sppPVBGHUUPcgz4RgFBxF67LS9yQyXgPkx6XvQIfAUFxk2A0_HvY14OeXvp_elQKSJO_9aGD5kCPDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25273" target="_blank">📅 14:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25272">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWLZ74nBrCAfcajHB8gV75V1yx3WMmay9q7xVzhWqaZfH_gYcqW1l3-sIuPwKyiTR-4Hsk7zogOfjsQz5k1KOn0mUEaFRGQO9lTQ0NgOC9YSEjisrLz5dS3iBoVFzH5PROsEEn1u8YOqweB0GaKIcGBP-ifZW3J74cRy3IZygzort_um-uv_656Xi3DiTWJ3Hk_sM3BJIavaxxb_GPWKfknwATilGXRW9DjYUPuTEv4spD34b4U0Lvcmvmr0Kwi8oH_DJoDvtUNVPKszecvWIXPgOfReopdGuWgbvFz04K_B2Kv01ujbbUhKcbSgu_hbcmLsTAHHiGfegBvHgbptLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا؛ علیرضا کوشکی فصل آینده در استقلال خواهد بود. تمام‌توافقات برای تمدید قراردادش‌ انجام‌ شده و بزودی‌راهی ساختمان باشگاه خواهد شد تا قراردادش رو سه ساله تمدید کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25272" target="_blank">📅 13:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25271">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxK4__F-Su1i-T6oPxMNEJEx5OwBeVZ2y1Mq0NHk19FT-HfRkI1PkMz5Qi3bWryg5YtOFQ3ypJUeBbvEaKkDsEbJMTZWO78oUyCaenfRNntZ0LQBWiZAKIrqdEwrytZbP6y291T8iMn-oH7ibV2iVWjcT_r1vfGdGmI5_Mr1KgSZQQfd3C0EV_jTgdUb6fBFjV7i1wUbByOA1kmI_RARFIcK7_KVVpaPRZtYpj9vEtmtkUm5eYeaPqzwJNla-C8d9162u2P3jiA010zYLimqduQMlc_05ssd5iBOGsOnOmDBaMg9nWqXzZBb1uhVlQoTys0qi-wNO3YlkvETf_fssQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه استقلال باشخص امید نورافکن برای عقد قراردادی 3 ساله به توافق کامل رسیده و هافبک سابق استقلالی‌ ها برای بازگشت به این تیم منتطربازشدن پنجره آبی‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25271" target="_blank">📅 13:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25270">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upTA-EsquG-xV9bRnRKCGLSkP6GZEgGNtd1coLVL_pIed0Gk24YrIcOgiiPp_tWkTstApTdin_GjUZxNDkqBGbjqYV4SPBEHb0nTKcTZV6zX0cKukxVrO4z9sqJI-DKjlttRnmKLEGXneXKEsx0yakG3P2zlLIbQ-ja7PuLzJ30HTaFMF5KuhwPrAJU3jxpwpfGJ-AvpuSVpMtDHjrgFPzDMbPV3hQN4PQlGulxi2tpc7CQDtxcVmOfVRV9hfYYT2PN8Q4OvuprM_oRdcGKEGDuJKH2h1uqayVAxs15T8mbF8TIN3bMR9SsSYkbTSGiYzYIGlMOY_OnkMLPljhLZmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
باشگاه یوونتوس برای عقدقرارداد دو ساله با امیلیانو مارتینز دروازه‌بان تیم ملی آرژانتین به توافق کامل رسید و تنها توافق با آستون ویلا باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25270" target="_blank">📅 13:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25269">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhtwJKhcP5LXPg4v--a4bsruoOCXdn0LpLEmlOW7gPckE8rY1nIfH8G-IU3XJsYDUK55I40BS_W-p_SrTDbM18sGkGHI9jCqICeXejzkdFaXVGhwGjHEKdl2J350QYBvG2iZnrqmALBTodH9-Ry5MKKjrzjfXDfFZKBmqHri-DKTqc6ZrcBFSjwbaWe4OqA2BmnhFOF2c4g5ORLq5WAJOXB-NZVCINAT4a006YffcAgMEWY_80P4MgjHoB9DWcLwba8T9bU3rBb3CRKEyETAq11HP38VZI9jm2wtFzyI3sk7bW3sj6hhuKd1QzriLFlEdcuw7dPBNikPf2Od60CGNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
کریم آدیمی‌درسال۲۰۲۱: بارسلونا یکی‌از بهترین باشگاه‌های جهان است و برای من مایه افتخار است که‌آن‌ها خواهان جذب من هستند. در خودم میبینم روزی به این باشگاه بزرگ بپیوندم و بدرخشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25269" target="_blank">📅 12:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25268">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v10fzzj6MOSXTLGCJtPH6iG1G0uDM5Vu13_zGKtYCcCy9J6ywAi0edzrxnVo_eH3pn0YKFvzK73HtrJazK0qLmkP__00TvrXTUsqeYEp5WNbmzDxXC7MhdOYHjwYGOgTpwhjCnv1PTJAeodwgHE_Lw9ap8N3o_PKquUJCmoK5pSLUMdjLCn58CjfcdMvCVvo_y2SXTuhJ9kY35q05DA3v92gMiD_8ueAySSUTTOwWyDxotUainkVDyMflLeBPaXKow-Nt09sBJi_52vHKBANHNKobL3nFeyj3bRMSPeA7nWoBLY6I7qYRSF4mHHo5PMCDh6FMYHyOdIxYpeMZLNHJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آپدیت‌عملکردکلی لئو مسی فوق‌ستاره آرژانتینی 39 ساله فوتبال جهان در کل دوران حرفه ای خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25268" target="_blank">📅 12:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25267">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30af4fbd6d.mp4?token=KcMfbxY8RjlHxX8HcnIRSVg8fEdsHz-MpZuUfQmOeKM1h1qP1GcBdypBTiflLSpUoD8X6TkeO-lokPks15AshUWDDZtiS5qsk3rD5L7hN03XrLJgMQp_AtI6dpT1PC6xPUJucnR8DrBkAjsi526Wn44WuwdsFyJCZrIRh8FP55ojLde-sniK76aL-5UbKo0IjzdJ2-NHt4HXChd_cMhSDVFJiIVtiM73HOBmmvys3hQi3z_Zvg5S0l-FSrsjK7pX5_4RlwnJuOHAxUc5iL8zS1IAeC_oA5C900EfVgICytCLjwHk5mhpZzaabhbj8AMDWrAXQAyLFoK9_C7Y9mF52w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30af4fbd6d.mp4?token=KcMfbxY8RjlHxX8HcnIRSVg8fEdsHz-MpZuUfQmOeKM1h1qP1GcBdypBTiflLSpUoD8X6TkeO-lokPks15AshUWDDZtiS5qsk3rD5L7hN03XrLJgMQp_AtI6dpT1PC6xPUJucnR8DrBkAjsi526Wn44WuwdsFyJCZrIRh8FP55ojLde-sniK76aL-5UbKo0IjzdJ2-NHt4HXChd_cMhSDVFJiIVtiM73HOBmmvys3hQi3z_Zvg5S0l-FSrsjK7pX5_4RlwnJuOHAxUc5iL8zS1IAeC_oA5C900EfVgICytCLjwHk5mhpZzaabhbj8AMDWrAXQAyLFoK9_C7Y9mF52w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
جواب‌ فوق‌ العاده رونالدو به‌ سوال خبرنگاری که گفته بود میتونی‌ اسپانیا رو ببری: من تموم تلاشم رو بکار میبرم تاوجدانم‌راحت باشه حالا هرچی شد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25267" target="_blank">📅 12:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25266">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qia3Y9NLcEiI0aVNVKYBAYTqHLHfbiFELk9Krh6-wC4Ht37is73qjRGmGHONGk8W0CWcyFHmajd80TrHSVrGfk97NDWWqvYQqpMvKJwsDU4rE6ZxDSdYUrm5GOAlKsNxB1GwAlArCI_TM5w9LDTGxac53i1ywQHVhIjxW3FmSbsUs34eCFj5j9JcNgoPh-adX18LxIlk9kv2CdVQIo4Yktkl9a30WlLdjPsXbIDWjt9bG7lr5aUV_1UmmL6ALDPcJR040S3DYC0LnmiLIeXIUfTYLlEGHuEiU6Tq3-3bVtqNlO2r_1eo4Aaccf9lS-GGs0_Ub2jtVLXPFdqbVm_lpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛آمادگی پرسپولیسی‌ها برای‌ پرداخت رضایت نامه قربانی ستاره الوحده.
🔴
باشگاه پرسپولیس ساعاتی‌قبل‌باارسال‌نامه ای به باشگاه الوحده امارات اعلام کرده تا 1.5 میلیون دلار حاضر است برای رضایت نامه محمد قربانی پرداخت کند. اماراتی‌ها 2 میلیون دلاربرای…</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25266" target="_blank">📅 11:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25265">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tK-qS2Xs8yFYTtINH0Ja7oqyawSwiZthNwLTzKHL4-wLlh7RyAuZ4Lre02Uu8lBe65ezMf8hb7VRYScF15gg9oxAV4ofODECtchuuvrnItsd6a-pVSvTjApz_Py4JmwCNOVmScZ69J8ctozEsnWXOzw3IC5eK4fYYbPimjKgzsrTpfV_4O9MzvLr4jW6UWTu4XmErx2UglLriecc94bXHHyI4-LPsU69EOqUplQxavXK3Ec05oN9Wv90QpO2rtcDWECcxVm2UQ_K6FkQ3KBNguY_rXEgEBHw_XE3Z49SyfN6QYUYg9ty7YVyuZHYc_16cqbIfKthPBh08yRNbhhqGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇳🇴
پدر ارلینگ‌هالند ستاره‌نروژی منچسترسیتی: شاید روزی در آینده نچندان دور هالند رو در تیم رئال ببینیم. ممکن است اتفاقات هیجان انگیزی رخ بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25265" target="_blank">📅 11:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25264">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5zavm0BvVJuyE-0gnr_1k7pppb10zHSF6KIQVeX-hYR6Zyu0XzzhThn8Mt6_wRTpdoaex_3zHwVftO5FjHISU1hGRiYBp4kLJtgXv8kgjux7-Tdpc0gLjIysBjiJbkq2ceata0yqDYT1cHD8ZqdG4gKRrYvkCZBvFACN0pjECS_oS2YybX2DogoE8kGPUSsJ0nHksApHrne8wuXy2xh3oMi6e3FMi5RsHDnUhGgQVR6MuHKsJmWNkGQyCtakvdFpJAp1nNOJFv7WLP4nnS9ZNwnCLzbSEiYKMol8B8QOA4LVbgQjJnmmQSXb71W7xrxXh2k4A_MeB3iwaOBwdbzrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی_پرشیانا #فوری؛ پیغام‌جدید محمد قربانی به پیمان‌حدادی مدیرعامل باشگاه پرسپولیس: پیشنهاد مالی شما رو پذیرفته‌ام، رضایت نامه ام رو بگیرید روز شنبه قراردادم رو امضا خواهد کرد.
‼️
پیشنهادمالی‌پرسپولیس: سه ساله بوده. سال اول 80، سال دوم 110 و سال سوم 150…</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25264" target="_blank">📅 10:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25263">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94e6448be0.mp4?token=BIZ9nLPDXFbBslGGNLN_RHwhC8TqQWrxCsEWTc-NIvDRGP4YXKhEIsrcLgURm51u6NSSNjd_np5JBwTZpRWF2u9OQ7UCmF3UPWybR40aCjpGZEQANMXN8GeJO9rSW9NAumYXO7p2wE2iiLu2JUHR_Sr6KpzrsznltgFrq02nS9ebJDXP65--psKOJpDbCHMBhXDx8ZhbJSnHikauXdTCKNrbPGvMi9G9q_1wNOd9NAe_l28WxrkeCYRYThKmHzYR0Fz0TMajIyVNGHaMseEBdwpUA-I__g9ewTMfH4sCG5Fz95qu5W9WV1NW3oTKgkCkfpY8RhnpxYNE4et3Jk-87Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94e6448be0.mp4?token=BIZ9nLPDXFbBslGGNLN_RHwhC8TqQWrxCsEWTc-NIvDRGP4YXKhEIsrcLgURm51u6NSSNjd_np5JBwTZpRWF2u9OQ7UCmF3UPWybR40aCjpGZEQANMXN8GeJO9rSW9NAumYXO7p2wE2iiLu2JUHR_Sr6KpzrsznltgFrq02nS9ebJDXP65--psKOJpDbCHMBhXDx8ZhbJSnHikauXdTCKNrbPGvMi9G9q_1wNOd9NAe_l28WxrkeCYRYThKmHzYR0Fz0TMajIyVNGHaMseEBdwpUA-I__g9ewTMfH4sCG5Fz95qu5W9WV1NW3oTKgkCkfpY8RhnpxYNE4et3Jk-87Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عکس‌خاص‌وعجیب‌وغریب از 18 سالگی جواد خیابانی؛ خیابانی به خداداد میگه تعجب کن ببینم چطوری میشی. زنوزی‌هم به خداداد گفته بعد جام جهانی اول باید یه ماه تو تیمارستان بستریت کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25263" target="_blank">📅 10:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25262">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZM8HbciKJ-8XIRwdpeVvmfjYTG3tj9kM5EmDTOZR4q6jVI_uQ6QiuoYQtf2jSRdNEk9wF9mz1zO9f7apLDRPfHo-TIs1Qbgnp1LXyGPe444FE1otYvejJXvR1_fT4E1HcDFyTZxD9xPr_PwscMJISynwxhyNE3aTuZqK713q7lpSlmdm26jEpVA4-3z3Udpt2gPDmZvBuAyiK2vw_M-19jeNViPFr7Rf1ORLIXvl93GRK9-Rmd7t0f_TanbE8StHPqdD6bgAAxae7jmEOmrs0HVwr97CRc3SEeVZq__iqR_6l_JHl8VsPDGRJOp8-1bpcs2VJX2mnFdloIpq0hzEHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نوع‌حکومت در ۱۰ کشور برتر و ۱۰ کشور پایین جهان از نظر شادی و کیفیت زندگی؛ منبع: گزارش جهانی شادی ۲۰۲۴ و شاخص کیفیت زندگی ۲۰۲۴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25262" target="_blank">📅 10:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25261">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WewXDXL-_uvZZ3nyEr9KyayZde8trCdOUm_XEOcT1XIdwrSy_CccL6XSsmq3EH574px0x2P7WP0lM6e2BBEM5zG7yU4jLDW7fmenU3d4HSxPs68ONltHQpev5xgCygYtTv3NCzeoT2YoNJE5EuV9CmYJDjQeyBG8HrfmD3wqFFzib0R7cOQLrBe01VaB8JvssEZ2JHE29rltIbwQkvubuF1jBLli4Ol2FpvTZ_jvBd75IIU6SQ0uCuaEC0eJxkTvtTKTOJcP_Lt2nOs9DhW0sP1Ax3pEJ9AiJP00OW604xgNCQ47qgcxC_hHRS7cWxhqkImlaZttWHGjiM5-rvQ_jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدیو لو رفته از کلاس‌درس‌محرمانه امیر قلعه نویی برای سرمربیان آلمان، هلند، ژاپن و برزیل در خانه‌اش بعد از حذف این تیم‌ها از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25261" target="_blank">📅 10:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25260">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEAk8cfytueRYriiUEDGSCqw_2PRepjlbMJie7BJzmWObMlSnIwhS_R2HTewBkfFEfJqibR7BHheh25RuiiyAIzhvwbaQAyXKCbXlJFMqhxE8yyvTRkq_DGl9HsuQPZV1cls3fda8XLSo6KQMJrtLIbOqk4HPsbEqityK-svltiXGlDxZ96d1L0m1fNfxVgIKq8LZ0K0zaEckKZV69n2AitB3WBsNZ4oxa_vUUQbVGQlisHqpqwypB5K60SUyFX2tKwpSrOS_tFo9FIvR1COc2GXhbI35wYPDI6H87ERXjJzxNEdKIBB13QGFAgjqseRaLAOUtMku6oT1pwI5Jcd9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
تصویری دیدنی از لئو مسی هنگام زدن کرنر دربازی شب‌گذشته آرژانتین مقابل مصر؛ آلبی سلسته شب گذشته با جادوی اعجوبه آرژانتینی خود سه بر دو از سد یاران محمد صلاح در مصر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25260" target="_blank">📅 10:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25259">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RH2MJnKFTKkT9m_bh_GHtTMyMeHy4V3bbM2W94RGIY1ukl8WCT2yPATJq15mFklqBB363rZEh1r5Zbs7olWqL-ryz7UPhhtxnbTdC6difZYyj59N6wDa-OaFqdcZym7Zm1pJIFh0a_0_R28sIdrdaArAZvsPOIe560IiILexEuPWVXzdx_Q5ZnY9Kampd7Glr6HMK1yyeg3ARH4oXabeF2c5Kf60cJ88uUw-RwJiWCQ8SYmok42qraV6S8RzUbgwds9XCkUf0ZjtmfWrzTsLz-f6ihm8xKtXD2ENaH90NTYW6VkfQ9wBOCwEwd_GDnTQWwxd8uDLYC0jooEpH3a1Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ علی نعمتی مدافع‌ ملی‌پوش سابق باشگاه فولاد برای عقد قراردادی دوساله‌باپرسپولیس خواستار دریافت مبلغ سالانه 75 میلیاردتومان‌‌شده‌است. درصورتی‌که بانک شهر با این رقم موافقت کند به زودی پوستر رونمایی از مدافع جدید سرخ‌ها…</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25259" target="_blank">📅 09:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25258">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BX4ZUk0HOAsAKEefkaaPOk2nA3L7wrfnSIK-SEA-qjZMFuEDN4zn2WcaATqPMaojSHXwctKjxb0Z67C80hkOwiCrcgTnKNDaqUx9jNCgsh66fQQYSs-bydQ_LGszG2rdAGEG9Uhjjhca7BCW8dfhRXPaRvEAvUAHjPYttINaVkf-IBox5_p6aPW4fy7rIpYfI_crHn4iw17qcVa5LqOuQcs1uYWjqffx7kuYyAd1XeQO6tNIy6fziQ4Zaieg_ru5x8r3OqYQvZ9Q6OZLz0SUfqk-0beatByIGvmt_t2KBE4Ym5NTqHdh6QGft2kOg-DJs1rH8L1zABaPtm76eQdoow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25258" target="_blank">📅 09:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25257">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chSHVQfBcxjVcIq60jbvdwRWA1B1NABOyiAcBSpGRflnK3gtKYFML2FXnmUhVblHZVSht4FBbov9jqXR90KO6O5G30xxFIqGamvUK96oLcgZoDI-o3wa1PCivhcbceAMavvwMdfSn8NFtijV4sP5JyA--_9mcXjkERErZL1QZl41JJrUPFs5dX6pSJdEs5YuHi1ACW1Eyo1e-LXZC1sYqMipZ-sf3InI_1bL_R5s4zCX97NS7PqxHgzRV2Quzq9Uieb01yVnMVn7Dk2mN0Py2yVjcki6Ldk6z6oa-ImXxX-utIo9ZQnQZRi4bq6pdh7pcc_5NSvRhz5V1-1THJWRsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ آنتونیو آدان،عارف‌غلامی،آرمین‌سهرابیان، محمد رضا آزادی چهار بازیکنی هستندکه سهراب بختیاری‌زاده به مدیریت باشگاه استقلال اعلام‌کرده درصورتیکه حتی پنجره نقل و انتقالاتی آبی‌ها باز نشود باز هم نیازی به حضور این‌ها ندارد.…</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25257" target="_blank">📅 09:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25256">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYTfQTgWOLsJql9tivudgNOvipS5giKq5CRdqAy33nc5S9rmUqrvVjIZ7gN1uk_lQDDmVDuyKKBjJbfXRSgf4RZwQwq49NE5HY8XUQOud-J_uQishxxQfyV5ZE-VH1MBQ_jo06xQiPzjPFKaETxz--8eHHLWEfY22yubIOciUEedaetzaJSus7x7Tmx505QJTuVogEAB-VH_DrNTGWY72zgPo8w_E4Q7Fwg-IjrlvLBMR-iWwTT-TNxEaAn1-uUftBZ6UOZT-HGDV2NAe6jMFPjCP1NuPr6_b_qoOiRZX-Qfh_H5IGLYaj9dpO7FcAggDuZt8cHNRI7IHdekRaUXDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛ باصلاحدید کادرفنی استقلال؛ آرمین سهرابیان دیگر مدافع میانی استقلال در لیست مازاد آبی‌ ها قرار گرفته و بزودی از جمع شاگردان سهراب بختیاری زاده جدا خواهد شد. پیش تر عارف غلامی نیز در لیست خروج استقلالی‌ها قرار گرفته بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25256" target="_blank">📅 09:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25255">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8869652ba6.mp4?token=Qg5cn39-0TtNn0tuGCyX1QXUd8ZczS6UDTKFeMBIF8U4dTmXTj0L8kJAUsHTZyu9S1NFFklTXxFkznspdne7aKPIAZI7VwA0dUPUqZzVrDZZ7ud1UvYRocLZ8vDnsiSOJreyI7uz97J-zeL9J-K0i9Lg0wjYTL8TkDR9skvdBYjXsD-zpa8ImSVNXQ9EfKErpyLMIH0tn9mQWavaRi_D3xJzGqkpZWoxvKQcqtlieH7XnHnEqxVVrVilM6KWSEjDz68AJJDwqvngmpuc5haFoupocMFYKiLiTjze1JcjkGgr4XjhmGtuCvXtVRaOtfYQHIVgY-DcTldK3_s3Mw1ph0gWBf5-krI-Eli3svx7c0gnP-rsnHN9rKGL_s5uVEP6OCoF0ZU8sCXY1V5LLq2EFNTo6uaNTcyhXfJdDt27wcyxoVHnVU9jjoWBTJYIHlexs4Fgn7lhn7JW6Bp9PBeX30dpffQ7AX2xflx9Sa0DeHUN9nwUsbjniD9mWcuscFkxxUAVVcWiat4Ss-BpBqyVJOdub_PK4Zynu5r8C0uT5dx3lh0VLXAEEkSNih4vfc2HsmL5w3OgYwFOgoF-S-xH4t9GT_7w8MGgxTVBU8lA630d6tJP4sO_em-MK21rM5fBz8RgT5-4TToxHGoIG1giFAqbPiPj57sc2fyIJLrAtHY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8869652ba6.mp4?token=Qg5cn39-0TtNn0tuGCyX1QXUd8ZczS6UDTKFeMBIF8U4dTmXTj0L8kJAUsHTZyu9S1NFFklTXxFkznspdne7aKPIAZI7VwA0dUPUqZzVrDZZ7ud1UvYRocLZ8vDnsiSOJreyI7uz97J-zeL9J-K0i9Lg0wjYTL8TkDR9skvdBYjXsD-zpa8ImSVNXQ9EfKErpyLMIH0tn9mQWavaRi_D3xJzGqkpZWoxvKQcqtlieH7XnHnEqxVVrVilM6KWSEjDz68AJJDwqvngmpuc5haFoupocMFYKiLiTjze1JcjkGgr4XjhmGtuCvXtVRaOtfYQHIVgY-DcTldK3_s3Mw1ph0gWBf5-krI-Eli3svx7c0gnP-rsnHN9rKGL_s5uVEP6OCoF0ZU8sCXY1V5LLq2EFNTo6uaNTcyhXfJdDt27wcyxoVHnVU9jjoWBTJYIHlexs4Fgn7lhn7JW6Bp9PBeX30dpffQ7AX2xflx9Sa0DeHUN9nwUsbjniD9mWcuscFkxxUAVVcWiat4Ss-BpBqyVJOdub_PK4Zynu5r8C0uT5dx3lh0VLXAEEkSNih4vfc2HsmL5w3OgYwFOgoF-S-xH4t9GT_7w8MGgxTVBU8lA630d6tJP4sO_em-MK21rM5fBz8RgT5-4TToxHGoIG1giFAqbPiPj57sc2fyIJLrAtHY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
علی رضا فغانی:
دوست داشتم هرجا داری کنم نماینده ایران باشم اماخودشون‌گفتن ما نمیخوایمت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25255" target="_blank">📅 08:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25253">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ykrnl9WLijiL20eT-uUaY-egYdpnKMF9bKC-78QxFLRBRoE8xI9mGewbaEYwxQLzw7ujqxsMYGgpe6wzI4FrZ0AEoQpVmLws-T04VND2CKrbIzl6F_ivAY5pOTWNzvwl4532zs9A6FRyvGaXNsPPV-rtBUFcXhSjby9Hk0vBonSxoPUzZJX3ujQ1fqh1_cIO3_y24jBuR8XiUc4a4t4EzJJOuMJb5v7zNXYCC8KuDfUy8mdcvbabd-6ZFr47vu2OcYnqX9KeZmnAa_cDN3--lNz3Twzfgyg3vWJO9imZYvwoUhJRtOkwddq7yJQ0ud75frakzQV6-Nff8Ej4u58g-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امشب؛ آغاز مرحله حساس یک‌ چهارم نهایی بارویارویی‌مجدد فرانسه و مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25253" target="_blank">📅 08:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25252">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrVrS_yGJhUxGBX6EEROZwoHw8-PPQCJE1IDWB4ifFa-uVZIK_K20WzIBQhvvAA5owaamZQjjHpNZLQwE5Ya7Bd1Dds--89JW3QVon9y9DmXxPSgDd_tEtq9K_M_cLFLIyDVGHAZyZjXVqHSkBCQCgUqwX2zcnJwKyk_AvCkFmFg7yT0a-tkVdtswRj22i4my6ix_il4iMKUvY75QAf1S2vYe72IKLoJRJk6iHUtOA9zD7lHa0e-7huFw9j7Xca7L-lYQfYF6d7qpG7oaHd95fn3L-IZx5SNQmr-79kH7_MqWyOBKzsZ06esnRFDF6_EjTkeErO3_mdFeqRMhM1BVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
جرارد رومرو: ممکنه‌ طی‌ روزهای آینده کریم آدیمی ستاره جوان دورتموند با عقد قراردادی 5 ساله به بارسلونا بپیوندد. مذاکرات مثبتی صورت کرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25252" target="_blank">📅 01:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25251">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4gHOcZXYL8vfSe3kx3UCYBxNQ_lrVvl-1ga38bMHm3QYgU89bt3lM_FwiPqyq8y8Qx3hnZcMYPWPnS7WaB5dKn5QUDtjxifDg7PI9L_1g5y8FVNG3fSzdrg46xSdNQQwB97dqn-O6kuYrcdEXa5zeYzcU88fZkpCIpvXCgL7UaCHzYaD4yabTaG4srCRnsWZyft-5zw7ECqzbXOd3za4P9RHZFsTAp5lzU05boAQGd-b7v_WRDJPc8WwsrfRI6SvytDJwjeRG6YG6yRXgApTVYz6cfDHGbqFDk5NGZplVWqQ1Z1zRLjxJWbrW8m4iJqtWfy_T9VY0unD--O6NCrGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
نشریه‌بیلد: کریم آدیمی ستاره 23 ساله تیم دورتموند به مدیران این باشگاه اعلام کرده که قصد داره از این تیم جدا بشه. منچستریونایتد و بارسلونا به شدت دنبال این ستاره آلمانی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25251" target="_blank">📅 01:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25250">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6798637471.mp4?token=TBLJ5G-rJHwrXbGjmIrB3E5k3yCfBHP9C8hSkS8KiQFzDzZpvutRIQ-nwo8ZGL38fGwD4bb9doDI_ChwYcUO3aTh6Aekl-ug8H-Lh470KHzLQM4n-hlDv6Gc86jq00ukC7cblB7rje3jqzs1-JV2OnGd6lCmZs5ebthu8z0XZaQ2GnO36237aDnw58Sdsn5CplvIvDhmDb5revc0Cn4hruSfvOaH-T14qtuawXLQuGSXqmhRRe16Oz8vB7xzC8R-LIjztxV7uWJbgxBceTs7sZ0Gl0yaFjaIo7zCcnk4vOfueudmnuhzvVLRoEKTImivYj6514Uu286j23oPjPuoMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6798637471.mp4?token=TBLJ5G-rJHwrXbGjmIrB3E5k3yCfBHP9C8hSkS8KiQFzDzZpvutRIQ-nwo8ZGL38fGwD4bb9doDI_ChwYcUO3aTh6Aekl-ug8H-Lh470KHzLQM4n-hlDv6Gc86jq00ukC7cblB7rje3jqzs1-JV2OnGd6lCmZs5ebthu8z0XZaQ2GnO36237aDnw58Sdsn5CplvIvDhmDb5revc0Cn4hruSfvOaH-T14qtuawXLQuGSXqmhRRe16Oz8vB7xzC8R-LIjztxV7uWJbgxBceTs7sZ0Gl0yaFjaIo7zCcnk4vOfueudmnuhzvVLRoEKTImivYj6514Uu286j23oPjPuoMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جوادخیابانی‌ تو ویژه‌ برنامه‌امشب جمله معروف
"گشتم نبود نگرد نیست رو گفت" خداداد هنگ کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25250" target="_blank">📅 01:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25249">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjT7Y4G3BBbWj_hLtkMApKH3RQ3u5CFovLCa_SD2Ms0H4o1MLHvZNx5HRTFv2QsWMSTLNM_ev95s30SkcoXs2ASvjOyzJoAtnihjfOa-yMvqUSddmwPzIIZaQ_z1PIMUddTDlCUwZCUIpHmuucjEhWI6C_mwpW2BCE9FVaoDIHfKIuIBuz1mgSKuBpTxShLC7YI7dS_nwxgfek5PQXzlAm_t957zACr_ng_Mb7_lWWm-nh1sJYHxgKJXg9VYldDSp5g2IrKFjmFN63OyNz9RJ3p41RGTNKGyNT5UAym8kphTeY7NTfbS-VG11C42wD1J6sYA2fSEK8MNWD-lE43jzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
خوزه‌فلیکس‌دیاز:باشگاه‌منچستریونایتد برای‌ جذب‌اورلین شوامنی هافبک26 ساله تیم ملی فرانسه به باشگاه‌رئال‌مادرید نامه زد. کهکشانی‌ها برای فروش شوامنی ملی پوش 100 میلیون یورو میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25249" target="_blank">📅 01:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25248">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7pbZCgwydL1QiwV2LnlXd6d2TLDO9pQ7_tZ3fErNc27Yuyj8pd09QR_q7FQcBlZDRWWG5W1_TxgyJBVLqQlTT7_FiSZRjQlHT_fVDfP1QMoZ-_QoPWPhqw09WuPKryICtuOoP3jbbp2l3JX0qjbdELSq4bDgd-do9IEi_-__S84FG6TzoVf25tOuVZT_Sb2M0bIAzCYmpZ-Xf6klniqMggcHWxcGCJeW8k7-ugtfTiFbpc5TdUx0po-k80U3nJqKINtVNwYobZU_hrTx37PQ60rT3WxhhDyIxJct1CUxIAX7ynvdA_H9qCjgBqYJ5v3Sb88XygoLsWLRE0dJZ7Kwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امشب؛
آغاز مرحله حساس یک‌ چهارم نهایی بارویارویی‌مجدد فرانسه و مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25248" target="_blank">📅 00:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25247">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApSS-AiUWCCsR2M79jE4X7HpjuXUEAcIODYLxCrcLcInahk2M40p4lQdLv7w41YUecpS8NBArq_7GnOLCQXPm3nXy96ksP36_S58DDjPVqJLfh81ZbyTiuDknw48te1bIuKnpnMtvTk-p7WQ4_ZInLwGYCzRphalRY2oGEVee95oPdek0kqeii_ryNVqPIMxrkT8BzfbLUo8OYqdxOiJ-mhhHMsmWkDHM7gc6OnEiaXZ8smbW_1foNk-b1ryYaUo8M2M6SKRIjzcwCYyb65-PibIwhF4hhTI5opaJ7Xb1RwdJfRahh5M2XuP6r3pcQJTDjC6VZ4ltFwaRwyxTR9Lyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عکس‌هایی‌که از وضعيت امشب بوشهر داره دست به دست میشه: یکی به این ترامپ احمق بگه هنوزجام‌جهانی‌تموم‌نشده دهنت سرویس.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/25247" target="_blank">📅 00:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25246">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBd4b4hkypWEuj8znwWFmOTPEa7OCOinbLWwBbZeg71kKqu0ISEPUom4zdqOQ8gXn09C9v1e1IL_1EyJCQwXbIMsrxrPBijtESXRb5I4nSKx4c7CJqS6ZdjAnMUO0DR5uZfxUy4CLLIUu1Jrx39hpzPMRlQpyMKzxikc5VwXJv4Fa-GOo6KlP7Lr7wgcXXZZLXI5irVdk9Z8HAjDC0ahz0zCf96UOYZ9z0wYCtK5WI2QEqK_p9i7DiR1_uX1qUGntMhSpflhkj_jSmmQfhMK_BM1QFONGGIKu26zUJYv7011EwibIqolcDx60TdhDMCXoDubcPE3YqW9jtXL7pydDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه دهوک عراق بعداز جذب سینا اسدبیگی؛ حالا محمدرضا سلیمانی مهاجم فصل گذشته فولاد خوزستان هم با قراردادی دو ساله جذب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25246" target="_blank">📅 00:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25245">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acg9ILpxrnFSINy_Qkh6VIEnG0-HhWL6G2Q1HGYeloxXx5lOIB7naeFprHkVxcWNQwsVwICczrew-0SYmw9OTQ_a3mw3DSAPsh_KSWKzLpPliGbRpEi7YT76pettypoJVyJzltcigD2MEgkrRY_N16PfuNx2E6yc0fLLPCQRvrxYw4C18nUhH5e3AUZcYzv89VXRt-gOHWZ0BeoxOoecygUk5pZUKo2d6hb-BkN2O4gxM6eatWfGaUS3mXhhRWeEB1JA9aIK9vgHpUtlcL3sdQdywq2u5MmgxqYEgR118R-5_qEBXNYXVZzgdl7ZoTERriOQKigh-Asiy43LPnZmTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اگه نیمار جونیور روهم به عکس اضافه کنیم؛ چهار نفرازکسایی‌که فوتبال روبشدت برامون قشنگ تر کردن. کسایی که روزای قشنگی واسمون ساختن. کسایی‌که اسطورمون‌بودن رفتند، اونم برای همیشه؛ آقای‌مسی لطفاشما تا ته این مسیرو برو. بارها گفتیم که‌هم‌مسی‌هم رونالدو بشدت برامون…</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/25245" target="_blank">📅 23:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25244">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5Cy56Lvm4YfhbxZJj5_HAmwZqIk1icitULZpPXzUE-PtzBugYO9i5eME7SgUVUvfaLFBDTJ_h8GM7-jOcznlnhghuGV8ctXo5-iCMaMyru0E_fXqprL3XJogyQI4j3PqUWk9fRVfAI1TWqgVOac2qoAazkWZb79p2399uE_Iw0ManHoHLBEe2gd9MDwE_MWh_yhI59GtpV2Pcwx7KFdMm-4iU_mtjNcrevqVRDaSn24MMIJGmw4SHKPUo4AO6-I12kvMNd1JxbopeR8TdZdWrxT_VNF_-uRPyI-7ozkfQ7kh7T_feDrKGMzyKKK0IXa851fBgtxkwFaubc3HNSjhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌برای‌جذب‌قطعی‌سامان تورانیان مدافع راست آبی‌ها به باشگاه استقلال نامه زده. با توجه به اینکه‌باشگاه‌استقلال‌تمایل به‌جذب امید نورافکن داره و مذاکرات‌مثبتی با او نیزصورت‌گرفته درصورت باز شدن‌پنجره آبی ها این معاوضه…</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/25244" target="_blank">📅 23:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25243">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtG4yW_NoWGtlDD6MF78tnTqc7KY4hPHCbevH-Vo9J9f5O_aF5QV7CfYxieLL_uFQuR9Kc3Cd8solI_k04AQN4T719btqL4GRmv95kQiN9dmQIW2tliMf4WTO9h5Y9J_cJfTOz9lYMlv4PHmU1wdtkRMCGy8N-b-2G4G3Ngkeoy8M8YgSaRQBo9CKjw7j1W3p0cf-SEY_G8DtiyoZDavCCH0E9LxVE6KK_huTf_HyQavtkxFPIIPA1v5gdG3Vsvccqq23NbTtJJCFnHtU_eDYbYcxocjMB-mb_Dk5ffazCN-l3Rdk9MnTHNneRgZpCamKapRUzrMt93h1EDrS573iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
تصویری دیدنی از لئو مسی هنگام زدن کرنر دربازی شب‌گذشته آرژانتین مقابل مصر؛ آلبی سلسته شب گذشته با جادوی اعجوبه آرژانتینی خود سه بر دو از سد یاران محمد صلاح در مصر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/25243" target="_blank">📅 22:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25241">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gktoSFR2NgZ7Hhebh7MD5YAvKGu0Pt1C3am6Jr7eldGkzUvFaZWY3EQh8McRlqhwjDKJfIxic8XOUmPjgPXhhve6rZRLteR6DR6fLu0pBKB9YnigIH2Jut-GxmpZgdqN1_62A9nrDvDGNqtzfcoBARlhG8sK44ocOrtfRgnG96ZikER1xJ1W3L7uAP0MD7W0MicO1tnXLNcKSBWtcaJXR_L5fSAhl2ALSQtGEC5SMcihOHdcI4sGt3z0kAiNFbNIWWs28xsUhbaEYZ0T8tIceYoKx1KF_FiDEwD8maj_iUqhEGvac3GDPXKG_zysZxg2aXJBc-LVHX5LD7aBPOdTjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JED8PFiHA_gGp16R5C12BZ-lR7M_DVoZOBTGpJY5ZqUlBS4q-Bh8GcO7si1Vous5KV015Kwnjb5cxSBNr8PxpSJ4K16Z3R1Ds03kk46VS7kwNLrLGdzn7G45yZSUg1G4nCDyxKnW8FeUQdm4WO-G-NX2V_4w1_i0EdPB-Aw93dbopzXSiGuhfeO_Ec-serJfGb1vqHicFNRbbugap6AcUvqd_aSbCjTsVUX6ZHse7qle7j_xJ_Mnvuu7T6Oz5eOY_P75mecTgv3yKAXoP9UxxbCIEo6FPCqsHZP8lFt2zIQ2uXZYo0I8xhL9vcfsHtXpO7XcaWCjsrRH4OZ_XGLxHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🤩
مجری شبکه رسمی باشگاه رئال مادرید که مدعیه‌کار انتقال انزو فرناندز به این‌تیم تموم شده و بلافاصله بعدازاتمام‌جام‌جهانی2026 انزو کهکشانی میشود. گفته با انزو در ارتباطه و انزو گفته به زودی به رئال مادرید خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25241" target="_blank">📅 22:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25240">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d23ff97317.mp4?token=F2BNndjMs-EZlNIsTleU70YeVB91xLSRzTo31w9nb0shShNl4MdEaRfwByqV9mLyY5Dj63WygfYmMUiQi_f_tFAkmb5AqcfYkIWlJxUpbeujKo_A5jh7XrHCHOscdomU-dJ0g9Wj4bJfW2O0RPDpO7wcEpHA9oDieM1qtTS5EP7pDyVKef8Ix5TB38TUT08AyZygXhFuiqFBZ4YO8Z1o6jKE4p97YzvFzUyrXnYKL93_2i_Cqc4TygGHZDdcBeUU5-5xpO0w79YXsKMM0sH1_tGcZNJU2DveyWxl6P8ul1uWAZ45zbfdnlp10BewcQs5Vb9wjXz8VqprSknSTHnqFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d23ff97317.mp4?token=F2BNndjMs-EZlNIsTleU70YeVB91xLSRzTo31w9nb0shShNl4MdEaRfwByqV9mLyY5Dj63WygfYmMUiQi_f_tFAkmb5AqcfYkIWlJxUpbeujKo_A5jh7XrHCHOscdomU-dJ0g9Wj4bJfW2O0RPDpO7wcEpHA9oDieM1qtTS5EP7pDyVKef8Ix5TB38TUT08AyZygXhFuiqFBZ4YO8Z1o6jKE4p97YzvFzUyrXnYKL93_2i_Cqc4TygGHZDdcBeUU5-5xpO0w79YXsKMM0sH1_tGcZNJU2DveyWxl6P8ul1uWAZ45zbfdnlp10BewcQs5Vb9wjXz8VqprSknSTHnqFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
امیر قلعه نویی سرمربی تیم ایران: کاش قدرتی داشتم که بعداز گل شجاع زمان رو متوقف میکردم تا شادی واسه همیشه رو صورت مردم ایران بمونه. باور کنید این تیم شایسته به مرحله حذفی صعود بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/25240" target="_blank">📅 22:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25239">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIQwwYRZgPgaXPUaav6c0_0kikbDyPSPMayRAYUbtwB3qMtW8MVocBmUdKkMt1J-1moc1Evm8P4hMBk43TvbcYGWWxnWf8PJn25OdtZ4fEiY8s4nDeduCFW2fbpB8FvwkDPBXjJlvGGfAKfz3qgklIPieao2Lbaq3XAryH2s1UZ8OZGW6q4hj73MwoMiB8YI-3FwndQbqUulzo1fy5cvmlW-qqMIbRwYvj-SGbtCP8gpARR-bxgmlw6J-aJsWenl6kG8AI_lCwIFpFUilsF7AZvKzKKNy4DR08BgjuUAjBWWRsepI8zRx3b_j5IdlD0KanCODglH4SSGnGn-7nRP2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25239" target="_blank">📅 22:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25237">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gR_hm6ziUEB3tkjLKXSiUp8mjQtsyzK7xlbG0wamh87pc1qW65w4FLRupWjkawGu1mg1fQpzVbQxjVo-PDxDUXAAIO0KMTmKz6mLdTo3GkydkKKExp6Xgp4cmUJMhS2sFa_39jXGOUnC78O901iwQROS19Fx5fxgU1tMlYERH4sMcG7VMblTkCkJ8O9WQ4zTOm3GBlpa3KWMjW62bjL967-8fvcrkgl6lbRddYbUSGpMZCcpnNuP2huMOWWUPhmYF4UDrw3wdoC2zuniu-L2XNXlKu-7CHwMnNyM3v9BnoAP0ZU3R8m3MzcD2t7Thh00fEUNdWftbt16KRGyEEZj0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ورزشکارانیکه درحمایت‌از مردم از تیم ملی کناره‌ گیری کردند: یخچالی‌بسکتبال، محمد امینی بسکتبال، زهرا علی زاده فوتبال، موسی اسماعیل‌پور فیتنس و محمدرضا اورعی هندبال؛ بزودی شاهد خداحافظی جندین ستاره تیم ملی فوتبال نیز خواهیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25237" target="_blank">📅 21:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25236">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M46gFQ44Qua-2i_lxV1psoqXSylW8pmZuoq5X7QyG6aLWDYp5dVGMkfZqbgyddYqVOTyCMAh7xFKPyWi_Uwf-a6i_P0G8gS6m0_3QKpKy6-JC-d8j1TeY-W0jwGA1wbAOu9gpfwQovv7cuO2OFTPjYQMW0aUNAUndp5bGsQapIEUjQhqpTI4ZnnHqkGj3JnQxTeH2anNQ6KFH9MF0U5gCFHtoroEgwXvb2M4UG_HvKVh_bezQRHcar_wOO7HBVqejmTDq1NCLElUx0TUpJmlrz0B-cpInskbbXvqLzrNjZJOo1xfKgtoS8tLOu3hLX6NYClTamExMKRAUrLtsbKUCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🟡
بااعلام مدیریت باشگاه سپاهان؛ گابریل پین دستیار ایتالیایی محرم نویدکیو از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25236" target="_blank">📅 21:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25235">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufJhwBL747nW4o-JzXyOTgLOhZ66t38ArRxAlBkcx2nPmCtcvKCW4xIkAmG84McRV-WC7hgKjm0tWsvWWDrZJDwq4zluW2ebw2YkiRRb5MIIjg4CIzJRl3epdcSEiKtfzIlvDrBTS0xpVuUM6Rl8D-NBHODsSDddgZlWaKjbKmQ91ooAt0pr27aTJadYoO8jCTn1UWUg_5LIDJPDfiwXAT7jvpk1WoRlPFSKadwiWOtfmG-yUNvAUDn6ZpWlaCto88yODsgQUqQx0uI9gbXFoI38VYxrNnZUY9PZBBIrWQ1ccVyeQFCsPo8bpP6lU2QF39raMFY5EZaXbxcvHCgIAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌پرشیانا؛ مدیریت پرسپولیس پیش از انتخاب مهدی تارتار بعنوان سرمربی خود؛ با ایجنت هادی‌حبیبی‌نژاد مذاکرات‌مثبتی داشت و حالا درصورتیکه‌تارتار تاییدکنه هادی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/25235" target="_blank">📅 21:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25234">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAMbaYLHIyh1iAjUir_a88xSc2QGyehfP0hnYUT_i0_imlfQREuwxdavFfCzk-C0OsfCmDAlN-IHXq3YfnkqEDiAJLfBAhXpoMkGkYaVBSHgarrAI4jrL22jB4sb7f-c0WW_uJn6OlFYyS5U9cAFtV8reLxFDBt8p5IIZ7bmUBDCRo6zh3SbttOyMYe0zKaI7CBoGrtguHFyoNV7a9NGzRq8i6ma0l1aSJu-jx9BIFocq4zqJY90ZGUwTyd2aveo1UR-oHFlai07S5tAKyXCvy4sxnztCLWr8gYN6PTcq28lAjRuEykvdfh9GMNgy_N2nBOVGhm3ttpipHgfOMGlvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امیر قلعه نویی سرمربی تیم ایران:
کاش قدرتی داشتم که بعداز گل شجاع زمان رو متوقف میکردم تا شادی واسه همیشه رو صورت مردم ایران بمونه. باور کنید این تیم شایسته به مرحله حذفی صعود بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25234" target="_blank">📅 21:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25233">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izgtfn23p71JstgK_lOL4tn8JXEcow9g3OVzdORx5yCk8EgJz3vUSff-X00EoIYHGU-w7Xk1UT03jX5RrinRkStN3QHIELy68octAFDh2g0t3UrffuwkyEyeAiVf7mOpYxlfT9irNwgF55CWHjgdBHjJo-yzQ3k2aT0jC72ymxsmoxaFsIHgNN4JmvQ3zCpZPmLd755jgw4W269NBcFbvYxilJDh_0InH2gGUD23xDrnfSSR8C6acEn_E22yPVblzf3LpkE6mgNWL7prw-sXCr-PDdlRhdjipgu3VvIXpb7VLfPlYRyo3RezEGUyWU-aTy5j5CUOvaGN0FFF9XPT3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
غلامرضا ثابت ایمانی هافبک‌میانی‌سابق ملوان با عقد قراردادی سه ساله رسما به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/25233" target="_blank">📅 20:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25232">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HujJca6gykgLKivsl1dDjbN6NsN9fXDcIpxdBX3oe_ZGWubodjD00ZXqpjKl53H0jnZ0YmVp6bu38bqybwhYjBsFeCZ3FzN6may6SLvysbTxJ0lq7EMRuC1Dnlu8bWhcTJkF8cEuvTQO0CpxtwhmafhTxybN4BIDtwj1vqZ1J4--nhkcvKW93TyJLvhOAFOOF3Z0C6sENv8cdgZ6vL7XuBQhrpFGZ1gq2_nQSWNRa012rKK9NC1PrHEE5xodcvBNliCcWUApiG05-VcWiandEj0I9UJMEVjYbCjBg822EhthXK_-QBUiy0LhoKZ2KLjVQLVmTF1SbBmmTw7jTbWoOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کنایه‌مربی‌مصربه‌مسی‌ولیگMLS؛ابراهیم حسن: فیفا میخواهد مسی توپ طلا را ببرد، در حالی که او درلیگی بازی میکندکه‌فقط 3 نفر آن را تماشا میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/25232" target="_blank">📅 20:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25231">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LajfXmDAJdseofeOE7E4nlZl7x_o6AIU_yizx2kjAWizGfdv3AQd40XnIlYGuBVY0fhGixMD_Z_0CVpPwW63-dwKnWnsbVrNtdUoZiBHX7QB435P6mNnfLI0A6DR-nEltE9EG9ckl6eqoR33zuythmem3KV0GlDSoduc0QC3wX6PJCwdFnIo09xs8ir3CeSIGq2UMhKRfTkNDbej9D1Xi4n8TMvxcs1CRZK--PDSenCtr97fIN5PGsER_myfeOInKFC74Ay4aYrG2-kIjvYlI42SrdP5nH6qPj3KfqesGF4-9M9NdLlZnUZgXE1ZZY3vkP8jeK4mdYPRts3yOgZP4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇦🇷
یکی‌اینطوری هم‌تیمیاش خوشحالن براش و بهس احترام میزارند. یکی‌بعدبازی از تیم رقیب میاد دلداری‌بده‌بهش. خلاصه که یارخوب تمام ماجراست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/25231" target="_blank">📅 20:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25230">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THcURUa3Fed_HrL_Zdchr8ZluDGv_prAqV4ztG4L0pzZ3UK-dzePDbWG1fUPsb1JqwdaNZHOwPx-DZ1H7HRSenpMUg9T63WY0F649_6CJLy7qPCETifH-Jo0EqDtIazd_oQVQ384a2GLZQfO18xRROvKx8JS17UqNE4ALOCU8aJVjsOZa9i99JF-GLBifRpKqx2DoD_6Gvt-QRRfXoJnuLe_jUmdCzmahsSYztExswzWFZDmPNc10GegfYQyDdRST9nZutbDn9mV81x5iaVEZPHVqaOLB-w59RnKS0Nair8PCXOZYzVObmJaCWKJMKkeTCuzCx2XsM0ZT1jj5Ev5OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/25230" target="_blank">📅 19:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25229">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gm8desonk5GFciJHtK7tWKknx6ZYSSo05FwKcatRvSwDE6edly-FD7RXtfUNSl0h5e-AEoP8BHpDPEHestDP9T8y1B4CzH6HLfkS3DckXhUymCG8_4w7MJyd87cPpYsuixL5ajbitzolXG-8qm2wmVqQshiGfiFihrm9QXhcohD_y9IHCh1pLkVZXGWDvhgJrh_6xRV-aus8YCinlKHOlpHDG0sNxNAsEu6A_jmZYZMeF2LAviem0ljuBzvgKF4-R7WZZBCreX9O42TxM-qoA16L-IBmoDQaBDs93UvIDEOtnWMxjmJbshQj0XficER4KHMVqnlPPyEf4SOCMvX8vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
#اختصاصی_پرشیانا
#فوری
؛
مدیریت باشگاه‌سپاهان‌برای‌جذب‌قطعی‌سامان تورانیان مدافع راست آبی‌ها به باشگاه استقلال نامه زده. با توجه به اینکه‌باشگاه‌استقلال‌تمایل به‌جذب امید نورافکن داره و مذاکرات‌مثبتی با او نیزصورت‌گرفته درصورت باز شدن‌پنجره آبی ها این معاوضه انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/25229" target="_blank">📅 19:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25228">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7acbde92f2.mp4?token=ZtUeTC6r25w_5Hqmm5UiFUbf5kV9gkK0raO4JSX9sBEGUBhIrKopzZEOJ03CQ-T2qH9EZTWmmUiHAibTjQqAnYwXLuCcHaqsQxvc-j3U7vI36p5wrVuaTX0j_AlA2GAp73_7NEmxz3z16tG6qw1b9Oy7zkn91dGLUY9TSvE4j1UEN7GK2rwAhN-qaDVhcJf5uPjTIUKy3xIzZIZhCyNzITJLdrcknRia90--fzX7WBk6BPHNxT-Qqw8BSCA7PBBmXBESyWBqaR0WbEQYkRerJKptQ_CzRIy-18D19yjaNG6hRLtNI44_gjMJgi0VU3bczhTTK3tFEIRGJvZxDQsvww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7acbde92f2.mp4?token=ZtUeTC6r25w_5Hqmm5UiFUbf5kV9gkK0raO4JSX9sBEGUBhIrKopzZEOJ03CQ-T2qH9EZTWmmUiHAibTjQqAnYwXLuCcHaqsQxvc-j3U7vI36p5wrVuaTX0j_AlA2GAp73_7NEmxz3z16tG6qw1b9Oy7zkn91dGLUY9TSvE4j1UEN7GK2rwAhN-qaDVhcJf5uPjTIUKy3xIzZIZhCyNzITJLdrcknRia90--fzX7WBk6BPHNxT-Qqw8BSCA7PBBmXBESyWBqaR0WbEQYkRerJKptQ_CzRIy-18D19yjaNG6hRLtNI44_gjMJgi0VU3bczhTTK3tFEIRGJvZxDQsvww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
👤
طبق پیگیری‌های پرشیانا از ایجنت منیر الحدادی؛ خبری‌که رسانه‌های‌آفریقایی مبنی بر توافق اوبا یک‌تیم‌مراکشی منتشر کردند کذب محض است. این بازیکن اواسط هفته آینده به تهران برمیگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/25228" target="_blank">📅 18:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25227">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOKIui5UiKJNfCsdegeL_3mvmCGoF50m1FzRPHCdsoIKlGjgqMi4JcpDu8lwjHAQuitz1YmO4jhc31nAH8HwMl0AOtM1jJ055_1pGlE0lM5m4KfZThmpFfFLMBkPPZRxHW9nq2TKNvDVCZGE5Oj0Xf0whW_SOSF6vrW9LBQbu0sl6J7ukbcqo9Ra9mFGpbTwob6p-z-qiFqlePnn6PMCf8zXrRHLWZXW9IsJmNNsmKHDEeiXmKUw-QGdUR5NVxgnpVMpH0goZXOv1gtm6B_2x46emoLOYh80vG9gKXTwqDVuKUU4dqitUmVuOLZ25_eyBWLc5wNzwAokCiWi3B07kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
تو این عکس لیونل مسی با نصفه بالایی صورتش داره گریه میکنه بانصفه‌پایینی داره میخنده، آلپاچینو نسخه عمودی‌این‌عکسوداره؛ لیونل مسی بعد از بازی: من گریه کردم، چون احساس کردم که هم تیمی‌هامو بخاطر پنالتی که خراب کردم ناامید کردم. اما خداوند برام سوپرایز داشت.…</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/25227" target="_blank">📅 18:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25226">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhOJQLA7RBxcVrLawmobd2OFJkxNGHnrj3GdruBOu5HLxlrpFugfnqozHmwv_Y4wtZsoX3OzW7TQ7D16wtl8ypV1aOHVRtz1NSTtRgOTVx89NIVH3ygS1Tqa1701etS5-EPkFboa9XbUqqnDdKdI6pol8RGb8ZYXrIdmBca_op6NywTap1_ocW0rkRA09SKS-J_FuNbluk-5fe_xUZePZYRWoBP7UdXZFKlBCrr9bUiYZoJOzp80gQn3Z3ePu3YYtKDyFErXSoptgn8HGPJkML8o_nKPSFWqslpChQLnsyudwsqMbKU5LHKY2qV8RUzQygFXtkJFAsnDMpbp0AeJDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بمب اصلی پرسپولیس که امروز رسانه‌ها تازه دارند روش مانور میدهند سه روز پیش به عنوان اولین رسانه ازش‌ رونمایی‌ کردیم؛ بله مهدی ترابی بدنبال‌بازگشت‌به‌پرسپولیسه و صحبت‌هایی با مهدی تارتار سرمربی‌ سرخپوشان نیز انجام‌ داده. تارتار بعدِ اومدن به پرسپولیس‌بلافاصله‌نامه‌جذب…</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/25226" target="_blank">📅 17:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25224">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rydZZgW11XuQAG_BP-GoBba0-sT-6i6l64yetfUysNmEZL1cCMkd4Dl-QBMCsQfd1R5o7WofYgGTkzd-yunmEtzHivtBNa3yJbVDZvJBGljfNSGgyzM39eYICWLyrN1mpH86sSuqqFa-nquoXHz1O_2B0Gy0-rNiAeBrB_aulbMnY2SjpLyjGF8ZKZhR-clIQVmPazo6gLxetwEKatsMEreRvEXf3nKoFM4cI0aqvAvjYxt8HrVpWqVq0hNFuNgSK1W-kTw3FQKuu7P97YgvCkQ4JbK8J31O6pkoZG7pRgw231j1LhiRtWGbeN9wtbQfzxdSycaLxcqtEJcGjiRv5g.jpg" alt="photo" loading="lazy"/></div>
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
