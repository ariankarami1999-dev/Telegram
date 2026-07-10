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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 10:29:07</div>
<hr>

<div class="tg-post" id="msg-25336">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_ya46_JdJ6ayzPSoFPO5rhjVwdsQIbW7atpx-hoe4M02WS9lAk47d-4g10CtCWsMyyKkT4oMH3j2uWBw5F9NpGICP9K_2pDss2pFkoYxqfuDNpTTdUIAuVbPYnInLOu4wCqxit8mXGrDLPw4jKT8o-z1BKcNetoa0LLgsZsQU0ZcWhlCFOcLxtPBLUwgZEGxeQC1ZD5IQn8hGSJS8Jt85DuKsyamen9SPsbxG-mwvnSjRXBIU-E1m7lQEhgVAnzMooi13ry8vEV5GV-Yn-3kjmc7UzLy_i9zFFrs5k2EE0VxX5zRgE_LuwzbG4KagWM_G8YxhTCokVZhtwaay1osQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ دوستان میگن امکان داره مشکل سربازی مهدی ترابی برطرف شود؟ باتوجه به عقاید او و همسویی‌اش‌بااین‌نظام بله یه تبصره‌ای همچون تمدید معافیت تحصیلی پیدا میشه و خدمت سربازی او تا یه مدتی به تعویق خواهد افتاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/persiana_Soccer/25336" target="_blank">📅 10:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25335">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjHsE8MRoYZpysf6D_wrv0pmjlLVqE1LzvhcR1dK-RJCBmU83FXVUDPGlL-P-2XjfDCQ8hiphZyyWkTzGzfd5m38uZAu_Rt-LCZ1PvS33sIkVGSw_Qlb5PcpLbTHCglljiSnfKBtIgEjC3bk-oS8XPrOy8-Ad2_vu0UqSWXSfkugbr-_8TTP_ncLxdh-7y2dwNvCuzlTH6mrZG1kJJeOU6qEbgxu6pzNvQNglpnewE6tilSHM5reDWH0R7yOkNz2ZS2fUMGZS8d7U8lxzG4ozasaohHURJAAza1eWoQpfl9qjrXYy0mYEYdovH__BamjEqjmIeX90dxn1JuSrHF_MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
ابوالفضل بابایی و سروش رفیعی دو بازیکن دیگری هستند که بااعلام‌رسمی مدیربرنامه‌هاشون در ترانسفر مارکت از جمع سرخپوشان جدا شده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/25335" target="_blank">📅 10:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25334">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EY8KdJ0FSTSuawUihfVbioeS13PmuQE9neiyOfSaOdZzh7Wp8eVLb7NLss8Q_PoLRnt9zFMfNwNrouWRacq5xsjjr7xXOyue2PWqsu0Q9RNcS9paL9VTAKGgIOv3UwuSUi_DV-VA6AUPiCOG6_xG99tK31QfZ1zNIr8kJt7-uFfgukumoMaE6Q8zXqkgZIWRnqS_lP0gp_2AZ1bM7hM7VTrJ7ID0Ue1744Ysm6Bn3c-RdqNW6vWJ9s-g_j1mzNfuIpZXmG5GwArYkg6HffD2bHZowgoYfUQ3kKTG6At3qGRm-Liy1oobw8Ls7EaKOtSBuMmQhwb4P1VBMLUpW_CQPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد..بااعلام‌مدیربرنامه‌های مرتضی پورعلی گنجی، امیدعالیشاه و میلادسرلک در ترانسفرمارکت؛ این 3 بازیکن رسما از باشگاه پرسپولیس جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/25334" target="_blank">📅 08:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25333">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekICyXWbcNqFGcoo2diI0U1cCR2ZTcsAwFuEsKr9YzIZvaaFEpBRUJL8iISzn2v1Usxitqm-94VAimWjHgaxVnzxhvS31Q0PJJ8iPkljhC5ZqNo6-hPpxbcRpnf7cJOH08Tgj9ZQ0FE5gj9qp61DQ-qR7ZxE4fOoDtfVP5eckcVcJWDn902KYh126po9c6mqazIWprWkZOYwxgdwuC-L9ZabqVEpvEnbvo5jfkx0gTo0AqfqDx-nN5sWgu_90X_ZqgWhqDLkgo2vox-mC41BlqUznYlN8GXIvIW5UCJyhHAaI4Kw5D_JmZrsuOLbJ63rE3OC3orwfE_KRZ5J0ewXow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امید ابراهیمی هافبک 39 ساله سابق استقلال با عقد قراردادی یک ساله به تیم لوسیل قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/25333" target="_blank">📅 08:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25331">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T0K-SWRQ3FBgfpjNUzSoEMiC1kmXop6KJ91FZzeb-cWa0HuA98GhfGL-_BIgr2x1XEjT5MLAsOdoTAMFKsqFUc3Mo4zEsXQ5cI-0iHJ8AuPMc5c0l_wzcKKktNFhNu_QhX2QhsYmJ8ytlAQ-BidGVXBXmE3Ci89ZxtqlzO8zal4-2FiEYbP_XgkS0hPW7i4FWuJaJeq3nINYjmHEhmjzDcQ9ZGvX_9iTetyYVo9wgYt1msH7u55n09PkTd4MhVa3oIn6ncRuvgAsLIWkYa5VO9zWjFOIl7mMupUZCnk3vYkdPKmg8kIUjXWZkdBetsrUhMNZB5tTmTIYTln3dyqIxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aQT-2r8dslh33peLPt4TwVquap-9Xs4NJ0VOq0BkS0BOlttKfwdl0poQBUPsPVuitjiAJ1-jRxb3wQnAIKSlqT_luVloak__uh6IsslFUddkOxrxIouw2_a8DIRQXytenKMBxAMwFSl2_kdHo1JUexGebBDmf34auxP4ISxi9t9EZYAEf9nU0ibqRdmYsoyTLALqK3OqFBY8HB7o3BWKKufNwQlc-2xf1nfoGI6BhPq2xg4SLJ8FI-GwupRySvarJ1dB64W891V8QptTV3s_weH7Rkw493Ey4EzFizQT2BoG56dJaQpi73UnALxDZg5umt9uWiAACh3rYjz1p008zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
#تقویم؛ 10 سال پیش درچنین شبی؛ تیم ملی پرتغال با کاپیتانی کریس رونالدو به اولین قهرمانی خود در رقابت‌های یورو 2016 شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/25331" target="_blank">📅 02:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25329">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ilI93RFLuURoToZnJ0884Is8QXSdn4ATsNoDfaRZzPR8QQZVBYqCcF06SuN1YJPTZ1i6x_6P8EqgCra3T9veCZiSKP1qWfKwRtRWwmjHtzHA9w_KCoSfIH863cbSWm_6OoUkAEY49eEvHNMPQhvFsgrp2y_gMTSXnC4nBbrmLb_K8XNCFODAmNyuVm_xUpJRMvWcXdHWfXXVEr6-9B6nEbLaxTiECsIl3uTgSxaz8PsUE0P3QDEEZAXaWguZCeijt4KGL8QQku6CPvPWpglHvv3hFUk6u2Ne6b7WmNOSG2Xm0mUHHO892WHv5NNosSpUbv4Jpkt2rkJRi_QCeQqI-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f0ejo86gQzXZE5bwLuENa71MEtX4GL_rIGewV2xBmROLmQh7pBiGzeoQhV39aH58Qp2xaCU-9z1guCquGiamjOUGvkgsZjfZy-KKW8Zxaeq2W_IRS9ILgKYSrjhk4R5B7jZpHIHR8I4TkwkGzPcMcWJ_VN1fIsgrONwa-C5iFskBA8wCERD-JEc1a9LquyuAOJqogJh6OJkAF0cstQWpv_18eEMqzqckCwD1uafCFm99KxncCatMEDRwBJzcaPzHBJduThGcruolB7XoyqK0SpN3Hk2FZtc0AdlttAqNiMou8oj22_oHxYSigg1nfJDDve3c7im22LSruGeLZcOpUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇵🇹
ویدیویی‌زیباوالبته تلخ در وصف کریستیانو رونالدو کاپیتان پرتغال بعد از حذف از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/25329" target="_blank">📅 02:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25328">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4hkucHWRJrGx3bxwF-pC8npo7pP8xklfHAZqIvlkJayJpVWIIQNFmZXpk6Ektw3SLl3pnepsICqCErrBXcCE1Ln2kjMZTsodLACL84qVanPF_SqsBuas8C6BvJUtERuLrQL2rSI4PsaRUUfwk4nE9auRl8IipS7lCrGsboec-chTvPT9U1fHbG-wCs8Jd4C4XT-sp7gOVlKqUwtAGDz1bPSvXaWfNZFnlKBQ5S6q41_FsfRK3wNX5pkt-B_p2VL7x1VbqXws0gXLzYGd2VCjfxIYF6pgOoKbuDSwCjsJCPgFBAmy-4_kqU0Est9BuxelI65VQrGgeVBz4bndT9KiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز خان کریمی برای کارشناسی مسابقه امشب مراکش - فرانسه رفته شبکه ماهواره‌ای جم اسپورت؛ خنده‌هاش رو ببینید دهن سرویس چه ذوقی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/25328" target="_blank">📅 02:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25327">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWLezMyytgoVThdEoRikhUWQrHzdCeImVMDgTsO2PA7D3Z-e9ozpdbaBhh6FCGfL_BxQ47EKk40DNtKgRqBEZrPaJ3N6CL6zl1Htu-Fn-tg3sTqgNqktcgl33BSfC04CvAysb7nLhsrIjurm9s0vVlRu7lRIJWzd356TnkvxqwYgt8tOHuH7m70-GUFH4htfZYZV7BQSTjD-2NVrSFtqpyyDcA51amhae5f2FApSaPV6NO4cOp_1ZNIBkkrnjPEiFD5cE34X70tpQNLYWDgoTSOYpx3TXARWf0pdlQgtcwtDIjOCYofzJC-PQyMuRRJI_zk6nSqrGPpL89ZhRL03SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی جدید استقلال از پژمان منتطری کاپیتان‌سابق آبی‌ها و مربی الشحانیه‌قطر خواسته که به کادرفنی‌اش اضافه شود. درصورتیکه پژمان منتظری به باشگاه استقلال برگرده وریا غفوری قطعا از کادرفنی آبی‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/25327" target="_blank">📅 02:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25326">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aROhzyBplmfJOKMVjZMRSfl_lsozUywVQiA8Ft-AjQWXZN1aHHcW-mEeb15aL8FnsasAG4pkfmiNs2974yz78c8QkiueI1vwGdggvl6u_zYr_s1cZCweYt-Ln5SYDJOcwtOFpcdqkuvBAfaD6qFK7oCocuLjuOCh75LPpJnWD28BxmDogYoikpdMFoJcVkhxEMGpH4Is3bvys8cFMx9C73nx2ZgZ3P3_kyJw1UbFvCXzSOkGwlQICDXmj4sx7ERRfPfrSNQ0rsAb4-li_akbJZ7uGcnI7kgiBFmEgj8C__-Bkvz-86MF4E9fzRVBjUGePZm3Cbo4hqVo5LaS09-xxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همان طور که دو ماه پیش نیز خبر دادیم؛ امید عالیشاه، مرتضی‌پورعلی‌گنجی، میلاد سرلک و سروش رفیعی درلیست مازاد مهدی تارتار قرار گرفته اند و به شکل قطعی از جمع سرخپوشان جدا خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/25326" target="_blank">📅 02:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25324">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/25324" target="_blank">📅 01:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25323">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPrQGkwJoghmnppGz73IBtsLsEYYYz4u0_BAM60AJd-gJcZlvmetHnrKj2F5ibf4CCs2y9WaCgeItSDvlzoX5ttGWGY1bdHmn8sNd4Ysb56xi1uf376rY3J0J4r5XvTcq0LTPcgFVsabjirh8Msd3KFnSah1Ey2ig-YU0BsO1UuhuzvsDGqIVRRzF4VvvdJvyBICBPgbQqxkWgGfcseJIBcq2XN2rOaEFcvWM57Kul_GH0qhgjFv55zwHgg5t29xr0xivajQFDC2AuRJDYAk_eMtDCmgW4c6JSW9BFahdtUVWo-9tn2prmHb_ducr_11P-Nvz5OOkF-LDamkgtS_pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌امروز؛
جدال‌اسپانیایی‌ها با یاران دی‌بروینه برای رسیدن به فرانسه در نیمه‌نهایی جام‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/25323" target="_blank">📅 01:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25322">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwECH4KUsUlMItlJxkL5ab1aYPWpdRgVwtJMJWcvxapS1MnM4k67wd0yPRzjC9KKOPwUjLSVtjdVgDoBrT2TI7L6QGlML9n6NsAvZIRqC8B5ZBYcXJJCOnnK04e0x0A5veIh0y4fZ_GcyOHKwbtjbGPUxezDxRkvPuHVG1U0FoB7azkmxbQub3PT2_q41nFDSDPOCjy-Iricp0DqQSZRG5VUTq1o9wOLs6ZiCrJdcE5Ev9CtgNTZdTBDOVs9GtveWVWFpKE4ktZcubxgu5fmO9d0SSoZtpX5pS0fCzDmbNdepGCGKSUP5AGd2c6Waf_9DK2pi6dPMZ7ttv6c0NruQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
برتری شاگردان دشان مقابل مراکش با درخشش همیشگی کیلیان امباپه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/25322" target="_blank">📅 01:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25321">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXeo5Us5VAMaorcYNjGdhx5NmPPod5uos1cEdGSJU14mujlyOd3xduqZ8OpuU3jKKmN8cl8_4zshmeX3j5qCBNi3ReQomuAC9XxNMzmypk96LYu5NUuuvxupQHb9vrSDw8zFcU5E5sy4EJYYuqTd3XlsGnXJNsB68Hb5Zd9Pe685nQHt_gUFRg9RG1zbDVpypoc_XgEY_6gRYHQUZ2LY4U_WBiCuJ2nzpFVcJpuX40zqo02kse-k0JQkjgLI4QfGjl5mGkQGxRGBZOz3dnb5zWfPV_MVXScAQeBSSr2-XJHGL9vE0Q6iyDhnX2wRj896Ja-X2e_e3Ki8IiGWs1yngw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی؛ مدیریت باشگاه پرسپولیس بعد از عقد قرارداد با ابوالفضل جلالی و پوریا شهر آبادی از آن‌ها خواسته هیچ مصاحب‌ای مبنی بر عقد قرارداد قطعی باسرخپوشان دررسانه‌ها نداشته باشند تا زمان انتشار پوسترشون‌توسط باشگاه؛ بخش رسانه ای هم پوستر رو اماده کرده و بزودی…</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/25321" target="_blank">📅 01:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25320">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBpxjyUfyj4m-a2yyjApRT0RRucd365eN3OWIZYijFG_GTDookNYfwAojOqz3w9drffbjQTwS6efRm694YdLk_x3Odxcxp57mMLyoiSuHjlF_MHp5D7z-HJ8H9JonPrE42QjmadVxpSvvOp1Wrz3_Jyw2Gez9IWV6UMOTsWOo63XKsw_DEV9rXO1I_-NO7f8L6Iw_MKYCv1_L2SZ1hUNAinFaSMqdZqTRE7z-3KiJCWWSHybuJ0riRP9ANr5aXh1xPtoISNy8Jfz6KagtEqxhaCQ0ZmskUJjju_3SbUyqy7hY_JvY3w8IdODcwVxFuCGRgK3Lug8mznN71sONJHUrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
دیکتاتور جبران کرد؛ سوپرگل دیدنی کیلیان امباپه دربازی‌امشب‌دوتیم‌فرانسه
🆚
مراکش؛ این 20 امین گل امباپه در تاریخ رقابت های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/25320" target="_blank">📅 01:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25319">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhjM4cu61bikvJpnzDFByalaSULkoQp5Ny7CikJG2g4QuA4rPUZuzq8QRYZKt7fpzdh5jNxTUcBxqiprjS6LCl7scwKF6jmENqDjIABSLTKWFxp2tF2k7IbhY869QMv82jrD3hpvAaTXicEUKrhWf7s80bAPHXUBAbm2W5D4KMthzBsQttSKTmSndi2xmd65py0u3rlo9uDr1WPNthgXsAhB9VAm5StYxnUykur91KCyFSk5iSnZ5UiJbZutrRSBEOsYt8AeDgvbEhMaQBX_iThDpwUtZWEuO_epCTKODI6ydlB55s3n_BeRnLueIo9NE5zQhUoZXC6D02efqdn7-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/25319" target="_blank">📅 01:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25318">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/25318" target="_blank">📅 01:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25316">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/25316" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25315">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/25315" target="_blank">📅 00:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25314">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6hHEn-0CgQlNFcP8vtzSkyzkOqi-CHe8ZUDb0T_J830JWsdxS7SZvX-vOSFmL6vRwzt3IqOzJBV-ju9pdr_fd3yoD_pzIAtiArBTWo71aAbm36z5pTAOwBkhz68pEJ-hK7umpnpI8c2Qj80RF7VLh8lvY2qDrsyTmGavs5BVRWif-0YphzvyphPHNXtOVPWVgbVOCDV2qoLcLXAa48Hn5-Bzp3FrSnpBoidASuRRoe4KEvkpb8K3-m4oof7pvyhUsc1L8CqO6BPm1YyN9QTVt4d4_X56fJYmVPRHP7LZCK0MOBgaZPI2qvIF7hucsEX7fDgGeKMVLs5eyzL5U6TpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇲🇦
🇫🇷
پنالتی‌از دست‌رفته کیلیان امباپه در بازی امشب مقابل‌مراکش؛ یاسین‌بونو بازهم پنالتی گرفت. ازهشت‌پنالتی‌اخیر که براش زده شده در جام جهانی تنها دوتاش گل شده. شش تاش رو به راحتی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/25314" target="_blank">📅 00:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25312">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwsQQdTyPzE-PN1-cnwCJjcFSIl1nBSZkfL2cJ1y82E2IYXH6e6Yma1C7M8C6H4KvNvw-AEhNCOvzjlR6ZSAP3gGGz_4ALA251vUegacMmkuWHjcjCi1MwtRvEBqSevhEwBkSVjiPMWDIXKe-6qT2V8ICU9VJcmJYroBE1rybe-nM1o9-mTIo3_LKVCLC7UBs6hccs9ZXm4EehskpAJVk8AP9T2mUr_166gtKJ-zoxI046UYmdWK1fS-cyujG1voGCDofaeievvLlvOJBpTivnngULGrhhgARIbrl_zciygnvXazCWhkN-HCYlbp69ZcCHiRBbecp1NAR7HlkrKyPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز خان کریمی برای کارشناسی مسابقه امشب مراکش - فرانسه رفته شبکه ماهواره‌ای جم اسپورت؛ خنده‌هاش رو ببینید دهن سرویس چه ذوقی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/25312" target="_blank">📅 00:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25311">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7769fa4e86.mp4?token=WakwM7_udoT5NkoGTweTia1z-VqYdXn6A0DBA2TT_CETwqVJK0vdzYvugoWuPzQmrM6HaGE04CS6I1xuzKnhbPcKpAkLV6hfpv_LsigeiD1YMk1lgA-h-iQpegyNZCxzKEJcSlxEcj4q05xPLpdRSPC2QBJKmujl69_TkWmYLeRPuYANMfEs4AzhtQpHOkx4gsKSjOZWWllHEqxFlkRnbxAi35eGaztH-H6bsC7268UF8CAlpLrMa3xIgQ6U66c57ilk_dH8Oe0WhvTccgCRAc5nFSpkmNGAYefd4D1eLeu5Gy8hnNC3Nw6z-I2qYzhM9uib07XCcQ7UupXgGcjexg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7769fa4e86.mp4?token=WakwM7_udoT5NkoGTweTia1z-VqYdXn6A0DBA2TT_CETwqVJK0vdzYvugoWuPzQmrM6HaGE04CS6I1xuzKnhbPcKpAkLV6hfpv_LsigeiD1YMk1lgA-h-iQpegyNZCxzKEJcSlxEcj4q05xPLpdRSPC2QBJKmujl69_TkWmYLeRPuYANMfEs4AzhtQpHOkx4gsKSjOZWWllHEqxFlkRnbxAi35eGaztH-H6bsC7268UF8CAlpLrMa3xIgQ6U66c57ilk_dH8Oe0WhvTccgCRAc5nFSpkmNGAYefd4D1eLeu5Gy8hnNC3Nw6z-I2qYzhM9uib07XCcQ7UupXgGcjexg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌هشتم نهایی‌جام‌جهانی 2026؛ شماتیک ترکیب دو تیم فرانسه - مراکش؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/25311" target="_blank">📅 00:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25310">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfMqrzUlUnOWUyCuwLXjrt5mGX3Lmgr_M2WpdKKA2AwVtRLlpr_ljRhd9SH05TWSb22jfxtQeyPVcDHr9vska6uoqi-st5t139oa5Y_8-wUXrHsmMyAvX8llsrDK2LOhwG_D0UixmJIGsqT8DMfpLmEMm6kKrHY9S27OBlWJGRw76MvYVi_-zQqJkuWzEsxfhdU4-kk_cfGM-szcPC2VVZDhQeCV4MzJH7R0UM9gjg-C3-DaE1q_zI5-SSVNC2nInyEhrEVbyNElpaw-jeV0OT4RxF9d02NlO8_IWSQKGDFbGzI0EDT77UQLOfCBSHuYVD4zVapg_4_vQdt4qee4TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌گلزنان‌تاریخ‌مقدماتی جام جهانی در آسیا. علی دایی با 35 گل زده در صدر و سردار آزمون با 29 گل و کریم باقری با 28 گل در رتبه دوم و سوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/25310" target="_blank">📅 23:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25309">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgi_taLkpriUMqDDYf3zuVOBDWngWb1DZEjZoP0w3NV7Dn-_1tx3_VPLnrAmw_gqkA3cg0-J0nYV0ReZdAiTlRZWY-yxX4lotaZU5v5mNjtoE_vt6yDseSIfNcW47VX1xmTKvw0UxI4b9gbLywWW8KzYHZhZ2ICUoVR1kvFlG8zpYWisEY1029YclCKqFwY_0g-eoYDHb3lctFLdeok1p3cad3btV6So_WxZp0lDKW_bdkKSi1QkNKyRqLW3glniOdj6820GfXrvRVAEXfV1eA-DGiMbjyA852SSNVXgNQMh5HHq4IBgFQyNonlCTWF5Fl1ykQ-Q3x8BPqu7QGquRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌ترانسفر مارکت؛ باشگاه پرسپولیس برای جذب پوریاشهرآبادی20ساله؛ سهیل صحرایی مدافع راست جوان‌خود + 500هزار دلار حدود 90 میلیارد تومان به باشگاه گل‌گهر سیرجان داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25309" target="_blank">📅 23:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25308">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfvRYUapIK-EtOwNKxl7PR31Te-cn_XWjtOiRx3UsCenW4Qp8U4iYPA8goUTvhHam_GhuQcundGMrgntkREWpHoMMUyV3MnoRv2jFpKS5_AitZf2-L0p-xaAMWPIhcCFRU5NpbK-0EfADQCu5tJvufEacXzJD4g0eujhLLQ6SOG-_kogJNRPCIUHBQx71QD8Yl8ghDj5UZ0fTQPPHQlHnBhkb5pt8CW1bLGY1IvkU1e8yxyOPRZqeane3t5TcV85uXS5zQzIhVxk0ZAHSR3WsU3_cjGxekbEDEXuBdKD9zW_oWwtb3A4VZLWBWOtvKWJwWrbBQxBi9gOCOhTA68RQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
این‌بخش صحبت های فیروز کریمی هم عالیه؛ میگن الهویی دستیار امیر قلعه‌نویی گفته ما هفت تا پلن داشتیم برای جام جهانی؟ مگه فیلم هندیه اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25308" target="_blank">📅 23:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25307">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LM2XjAEWdWSYvxKwmVcv12VFzJ2FMsTJX2EbQbpsgJxD6J_-KeL_Lb7ffAxCpkLKyydjkm31XJpf4K4GswVyqpsOpfbIGz-34JAqXnAcqxLuJpd-FkrteFkw2Y1RlcspBviVl73GeIT5tnnLg9XzQAqMVA_mfMMvaZv4_-Mmpqn7hYVLoY0EzEDhmZ4ej-eBm4f41hRogXyz-oFQ8cl1HSO_Oh6xGoxYPEnokwDHegvFW5L7K1BC2CjbRABsCxHLE0gO1h5kKNp10jGHqtdmy_REtM2a5brPhazoqQQVfzRZICyAFpmTbAtA-SgRPKgHGvI3BywXwDd6DlTKq0EYjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی دو روز پیش پرشیانا
🔴
پوریا شهرآبادی مهاجم جوان گل‌گهر با عقد قرار دادی چهار ساله رسما به‌باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25307" target="_blank">📅 22:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25306">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kf7t43B_v1eo1dC8emNT9s_p4eBuPjqUF-G9QJGLD2JGcR7DYZpOvUBCE5x_48ngqJFB87-bC13bpIHppsJOTHSIbuioytQvQWmQFaaIdqhFXxp4ofbHNlqcx24KuLc4CAwH9LJ0pgQBGcR2C0iEukbHgrwhojmWnptSWWB2xpSDJuJaguGzeXDhR8nb2tvb80JSekVl0s5Q4ME8qD3F2TI8PRq0bPHwXfJNXmsRZgD5Wvq-XklU0yL6JakGZSEjuoONPAhFGVhFVBq2IGJJdi4-Ao14HgR8pQ6y3H_EaGB4eoEF9UI4ddnp0iIeaSVog6tzgSsDVcOBujnLWj9bKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی‌پرشیانا؛ جلسه مدیر عامل پرسپولیس با مهدی ترابی در منزل این بازیکن برگزار شد و دقایقی‌قبل به اتمام رسید. مهدی ترابی برای عقد قرار داد 2+1 ساله با باشگاه پرسپولیس به توافق کامل رسید و به پیمان حدادی اعلام کرده درصورتیکه تا هفته آینده مشکل…</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25306" target="_blank">📅 22:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25304">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H7Q2uk7eof3W6bwm0tYOLmCb8IFzMvjB3lnz0QsELyDfaIv0OjD-ISwrjo25JWHvTKekp5hf4NLiATJ3npjCO5rIhc0eRP5QMPh6jTSCcIDlu9RIM6hDzFbDK2m1r6znRPEl6sIV3lVxvN1OjgdnlyWH2zO3yCEDlpblMk_EWBu-fbAydc48-j0nC-RQ41U-QXWVU8Eoi2aV5oZm_gJovUieTt-z-BTvj8Lx-l1PsUPmGCKiqKUDcxctRULI3sBC7k2ON239ywdkh-gyYXKwwbjKCG164tr3zj6gbiwqnLwBlmOSNJ7PcB4tdvOr5OLRDCCfFN59lM3PSqubq5wtNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iuI2Hlxx3hDGENh41canI5qjfloto6JGGLt31inbjyBZA9lOxh0uxwpY7SJ2jktTYXhriAwKC-r2h9J15us0jRssrOA4Uqso-g_QPHM68WdqMB9cOgqUk_eqvFzxmIgZfMCXg3XSEQ9nTzz90wNirQJtMhCSXXjz6TGxrnS4_RT5B4jPq2_zq41h25mbuCL_JrtQeGBS921WlHcoh7wBdRqNd8MM3FGCp9J_uvnBiePFv-atTmbtSCqa3cERl3LxAr2p5jh9PNpbIDw1xcQuapgcJvVQvROfwr1FwIXvTvxEYxpnhMrytIH1SUad8qV8VDSSBt3eEGMHHkoB5Xi1Zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
#تکمیلی؛ازترکیب دوتیم‌فرانسه-مراکش در جام جهانی 2022 فقط 9 بازیکن همچنان در این دو تیم باقی‌موندن. بقیه‌خداحافظی‌کرده‌اند از بازیهای ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/25304" target="_blank">📅 22:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25303">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZhgBdCXactXOdfscnB1qFYAGHB_vBxZ9DFsEQ8NV-h7795DcNkz_UQ0xNB4aBHhcus38zcagQwfqC3NMOiLNOTb8MN5aPPCp_EfsMJ8bWPQkjgSNMQhXqNVNuX-rICwY7u2fBHvr8y1dj-Lh3NwIhXJRPOOTg8x9Tn-PxE-w1y4y8q1i_XoyfxAHUnmtz6PeAfPLNRvoCd8kK9ib7mi-TIp72C7PI3ZYl1rgZWsInZWQ5dvhlZSRA6l795L_IqxD-e09rqzUbYRD7_dvwm-h8ikEQKDA7Wi3sKWI9iNVre6pq7zcRIeQvnZ0YqB1OdHF-Y6J823wadLVdeGNoIueg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی‌پرشیانا؛ جلسه مدیر عامل پرسپولیس با مهدی ترابی در منزل این بازیکن برگزار شد و دقایقی‌قبل به اتمام رسید. مهدی ترابی برای عقد قرار داد 2+1 ساله با باشگاه پرسپولیس به توافق کامل رسید و به پیمان حدادی اعلام کرده درصورتیکه تا هفته آینده مشکل…</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/persiana_Soccer/25303" target="_blank">📅 22:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25302">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZ68MQ2wKg8DENeDn6UiKkOLc6N2Vsdv0a9UkPRSH4R45u5Ngvc4BkIPvlm5s5Z1-RUBkmhHwS5jyMm9kWL1vOBNcneYuHOKBZKHw2o3u-qjJi5BoTDDTwmTo-HNQq9mqZ6LO2DgtObh45uPTFicXAN6KloApGut3xkRfmxdwoQSkbNCfhIAf2InJuY6PVuxjCNGMYV0ihVYUilcNaq2ldGStFBlmzHbEX7O29M4QLO2P5JYKF2AUYt4tMOpYP7tycoMEG9ghKbJ8snZjFGGNlgqU2AZ582JXAD3ftn20qdwhes4sbMFLA6xnhzdXxYp-GfrWHy_AAsburp72uuS0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جلسه‌مدیران باشگاه پرسپولیس با مهدی ترابی و نماینده اش شروع شده است. تا ساعات آینده تکلیف ترابی با مدیران باشگاه پرسپولیس مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/persiana_Soccer/25302" target="_blank">📅 22:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25301">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_1zl3TtXsIY_D5qKAGviAjmWow1e43r2brO8txvdKM9gNKpOQXc65cunLdp07-yMkMZrLVxHbk-926J5QMN8aAtkEj1JfzhTq4f9R4OtFn1lqEfyt7p1yZioUZRVjS8vdLqbmIsNU3hAcG9ExziaTK_KdyZsxBtZn1NtVAQsbWcYz0jIH1msAjotQbYfNnNNAoA2rl8b2LU2eKLsC2CxZ5yYW_qQmFsS-tkxQYuzSv7PN-tRTXakRncFJ7zhJjtLLKyRVP9Hw7SkRnptNtx7Bse0dxA3QYaeA4vuGJg9XswrdFquAN-TQyelsMqCXxjUjipGOFBg6oZb9fw9PC9Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دیدارامشب‌ دوتیم‌‌ ملی‌ مراکش
🆚
فرانسه در ¼ نهایی جام جهانی رو عادل در آپارات گزارش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/persiana_Soccer/25301" target="_blank">📅 22:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25300">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1lZ6yZ82moj_qgDc2tmwEsuv5xbaZSVAAWP-Jo_ppHlCwWEqypDFPA_6VAgeIiCKMydFjnEgs-K2BxNZI5lYd1uCzmL2dKN5DNpa33MESY6OR-8dE_2o3d_Ymrj-8qKkQrVnvoZkBvc1kUqQ5CADooHgl1tnUdh7bfPTHr0xG4tJI5D_7tks7ty4G29GQBEVMquhJurXKcbaOqJa_LEJGi9hGhm-M4jj0v6MT7EXOrt_PuCM6PgfKyaLW9sXyulFE3mltchUGAJDJ6StO5Ap95neI5WS7DGg_1uSVFjYaOaEXwHG0zPhhYF0IopanzyULd6FaowPxYvh98muoQigw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تقویم؛ بیست سال پیش همچین روزی ایتالیا با غلبه بر فرانسه در ضربات پنالتی قهرمان جهان شد. با این حال، این مسابقه همیشه به خاطر اشتباه فاحش زیدان و ضربه‌ سرش‌به‌ماتراتزی تو یادها باقی مونده.
‼️
زیدان: از همهٔ کودکانی که اون صحنه رو دیدند عذرخواهی میکنم. هیچ…</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25300" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25299">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCI9WmyhbMdRl-OCr1-AWD6qbHDPHx-KWCfUARo9MwbOGDgYbI_gXzOG_29bWs6wvd01zm0A4IR-YHc6Ar3POyqMUkpf_LkIOX2iZapkU4922A1UAizW30PFbYuTCpUtqo7ApIE5-SmqFSJQ8_SeMlwXCnqvtrA2UAj7E9AY_4vRX1V61nvx8felcEQaa3Fh7L_5vYj_RT5qBPP6H6FuEBGh81nHzjQRGKPfV58t4gzlpQe-Rm3nj6LfqJ5gfyfR1X6rXigMDlzM4KMjwrMwuVZ5ulMAXeWGTSxPeJkgTptoP8ZsYVscqAa0-lw357i9-zni3lAb23qVvQhfkg1xfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
باشگاه یوونتوس برای عقدقرارداد دو ساله با امیلیانو مارتینز دروازه‌بان تیم ملی آرژانتین به توافق کامل رسید و تنها توافق با آستون ویلا باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25299" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25298">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtBKOP8iJBM1ZXEKy0vghkGkgtNXNiDEcofIl-BTdcyU7Ok_jb1GaOR1j5p1POZnUJkzYi79l6JvCl_OBqiBYrrwZ-AWxcl2E9Wa-T_TKyTVIpTnJ5JG0obbS-ctWr1oOWvutG4qkAfVzaf9MfIf1DKFdOoL3GuK7wosU2_nob0usIqrLICB4wjRntYBrjpr2z_dXEUYPWuYljvlCynnankDQPz1dfkXUFPYD63sumyaKmLVEF-C5s4BmlZoQpP76qbPgFIvTdrze_evrCLgwHeLcm89unnykXmZjO3OMBeq3cAQ3rrdE-HsY-Hsp3qNoWeWT-B0U2jD5TBNusNyiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/25298" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25297">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbv51MAiudkelVvymkWu4z6_wLiUXimlzBWLCahQX6JfS05zEeM0fWqv7LdMS_SqbpvrEugWmYAJcmgNXaf2ANuWf06p50hSw2MPYI9YseQwpLaquYo1TT8dK5iyusIZuwGjw9JMOfAqhuX31DjOANXovE4g3xuWqlIT-uzw1q3h6yS4VikmcXQxRCjeLZ5ZKnk4NW2ochumgCWbhyiLNOaa3HlUY-YjJdT7AWhuXWeILZROowRqTHhg_vqTGjE8LbgsyZZn5YRHsDoGIwgIUlFnLrpwsv869KOWDJBCHAKOXxy1IKfAcjy5ALzw10f9gWFsLkax0fKBt8d-Gy0Mkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
طبق شنیده‌های رسانه پرشیانا؛ هفته آینده جلسه‌‌ای بین ایگور سرگیف و مدیریت باشگاه پرسپولیس برگزار خواهد شد تا مدیریت‌سرخ‌ها این بازیکن رو برای‌موندن دراین باشگاه برای فصل آینده متقاعد کنند. سرگیف بخاطر مسائل خانوادگی قصد داره فصل جدید رو در لیگ برتر ازبکستان…</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/25297" target="_blank">📅 21:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25296">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoAbs0bOJnPAvFgQfHq4dl7IjS72f9_Gf3WsrS7IwVFR2QC22LkhXy80GFLq7D3ghHfjKcGZ_FUj6Z2V2zBtAT2QpsAh4PeLDwH5aMO6oF9wBBFPDPq64dks8V4hpfGR5MdGL7UFhpF6vp-1XD_2ueSZMkHbhrhLSWNfLQSyajOk9j2nsbZLixxzEy3reFt8l-N5zNVhAuwf0wIgTyWuoAq-uV_fV_-5kaFmCjKj3-ru80tcQcgGi1akBLCwTXCvBFjVl5V58HEqjdf69YCH3aUMa1Z9Qs7mpFZ8omUmZYfJ7BmZ_e4HL9xJGJs4fjYg7nrlNyftgU9m4G0Cl7TOfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
بنیامین تانیاهو
: راستش‌روکه بخواین لیونل مسی 39 سالشه و اون قبلاً هر چیزی که میخواست توی فوتبال به دست بیاره رو به دست آورده و بارها شجاعت و بزرگی‌خودش‌رو ثابت کرده. ولی واضحه که هنوز حرف‌های زیادی برای گفتن داره. من در جام جهانی طرفدار آرژانتین هستم؛ حالا از فردا بازی های آرژانتین از صداوسیما پخش نشد تعجب نکنید:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25296" target="_blank">📅 20:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25295">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LF2Gh6niFX5tOc2X-0rHMMYZlePYTRHYELmAWRqPxZqopGtFue7yCf2fD4Z8bmLRdPQeRlSWiqs75sgIWmneKUZf-RESeBa14Zn60L390antuerez8zOgThwI2hCLO2Y0a1cJIKjD00i60TPkbfEAEyYcFxAFQabhsb9ki28sqPNgRf1AQbBIQVEfPh_QC2zrLaoDd6zC5b0yJp-4GhntogIAooM-wH5kMKNsEIjfbPxRmWV2Wz36c8HjwrvIit44KLzuS291deZfNpiCwispJKgDTpxCnMjrdP47rwmKenwB9n85UhF0ggxmBD9TkTdXNs6HDAxQmi3QiCWkZRKCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|داوید دخیا سنگربان اسپانیایی 35 ساله فصل‌گذشته فیورنتینا آمادگی خود را برای بازگشت‌به‌باشگاه منچستر یونایتد اعلام کرده‌. دخیا میخواد دو فصل در منچستر یونایتد بازی کنه و با پیراهن این تیم از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25295" target="_blank">📅 20:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25294">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxD1ZEpqsx09YVdb5DluC1J85sZ6pYiStbdQ5PT1YS8ntdsC5rRXUXagdempspiTwtDqkQHEAdpZWzcSd8ruT5CppWal6c_foVnV_cosvzLww6x7TCMTKmk-wiRp_9r-TN_FF9enWqT2wL6Ry99PBDiMaBeQvnSN2gcxDV_7BqEb8WEWy7F-5gT3YGJ84NYPWKpnIF4saYbjyTdtcL-HyvGbQeLCaqPWNMQD-eJz_72qNMHgdnFQXr01-5N6vdV_3Wlcr6PumakEqRGDBYLGu92XLYigBq3jmpXdr-Dq69hAJkVRRWJAF1hUBQnTSNqPXk07jh0sWNTIemlUFVlksw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ طبق اخبار دریافتی پرشیانا؛فرداشب‌حوالی‌ساعت 21:00 مدیر عامل باشگاه پرسپولیس در منزل مهدی ترابی جلسه مهم و سرنوشت‌سازی خواهد داشت و احتمال اینکه قرارداد 2+1 ساله امضا شود بسیار زیاد است.
‼️
پ.ن: دیگه داریم لحظه تمام اخبار داغ نقل…</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25294" target="_blank">📅 20:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25293">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hin6fmBxhcy-GQUcZxf7t14mefw_pnsFgbtyfSMFuN5UqhHGSBCeVozh6FSRbkifp02eGjrABoHyF82htpvYBtrfhPWQo0HOC168iOd4eV1Zp-tmrPhKyFaQ9DpixyhOEHSqT1Gf-OjuCLskkUfHJj6alN4eygxhzWETRh98QcDamsNF34wKx0tBHmV4aCVvbSjxhDv2kKoatLXxiy-xII_2U1Ev071V8UMJLmTmiviID1frL4xi1fSWe-Fg4Qmg9vheONXhdhK_BYrzAVawT40nQB06qzMLolvvkUncHCkkj2dMhd1P41ZNS5xCYFifkdo6QhSwyj1uVYSt7DPyAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امید ابراهیمی هافبک 39 ساله سابق استقلال با عقد قراردادی یک ساله به تیم لوسیل قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25293" target="_blank">📅 20:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25292">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lz-of-Vj5ZbzJ4rit88Kdhx9jzfXGxZ4WctsJ1oAHMPUH6JSTuHUgx6jY6HKbvEBnhxCZcJgVYNuswMCPd20ERIvQWrgfkYf4lJP3PoWRcHAWHRTYFVMaLExLXmM5PggvTR5h7z7JZtzAEdzpp13UfGayBUwPyBzFZjflh7OpDEHGP-LWKNP1QlfpZg36ptNa144sfeJZdgG0nPojoVZfHln4UJ3OJv9VjfUak6WvhwlBso6-WYsNFBJqCes1nFoeoL4pOXkMWsNqjL_2Kwrn5xjr8F1FzfSRuqMNZqzghuNz4Lu7DoIaGUZ1Fnk-Xm97jpmj0Nl8NLpoEmBtoL1yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هادی حبیبی نژاد قبل از اومدن تارتار مذاکرات مثبتی باسران‌پرسپولیس‌داشت امابعد اومدن تارتار و درخواست جذب مهدی‌ترابی دیگر قید این بازیکن رو زدند و او با قراردادی دو ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25292" target="_blank">📅 19:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25291">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjyAU05UnXiLQxx8-pmA7P6wH5wFEOl5ktfMt17yAAA3arBJ6iDTZzAaaZt6tRG0qo9zaM2DYdp4upa3hBizM_XUSa1UeJ7t8idN3YAWB-BcupV_ppBjwpvXF1PyqifwnO2Gt6wKApt5e8zK4VeSMtnQ4_DFYF_eQkur3gC8AqlxEc7H3S963ZZTfK7DOzXPEDEXSjKpmVEbWSTTvis3m2OIftIfwlEliCPaGjJMY_s7LM52XpoQhrm9pvZi4_gzHs2LN_6HjzxWdz8LnYAiLhiVVRqgy0Te2hPGxAM2Uh-AaIBS71b4qD0NnAoPYRkuJC_VLvBnejgexN7vdgXrHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیرورزشی باشگاه‌الوحده به محمد قربانی گفته هرباشگاه ایرانی دو میلیون دلار پرداخت کنه رضایت نامه ات رو براشون صادر میکنیم. همانطور که دیروز گفتیم باشگاه پرسپولیس گفته ما تا 1.5 میلیون دلار حاضریم بابت رضایت نامه پرداخت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25291" target="_blank">📅 19:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25290">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njkeF_AhNfe7S2ZwRUe4NPLM0gbKO_YbZrEf2bybPI75kJIYadXi6PXU4kztjdq_EuhV_zmxrb9M6RNDTmY-Vu_yBbZ0M5EW6skNkDVytagRyMKi7H7Lq_SEO3ON1xB35tgKI3OWa3VB7G215mTWtyWD75CDuiLxpxTLRAHkI4tI-wl3Hnl7ircWqL6xbzCszLVZcCAeXyEdJbSP9Fxyzv6-SY75XT7eLoYt3VuAxnaI2KP7ehjelgBMFwOqwtYbNASoauH0DVPN0hgLAfHwQ42mdvuwanL3GH36k9FTxKImKPN9xNFojHpUzyvcj4u_lupVnUow1Czy305NwJMNmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
تونی‌کروس اسطوره باشگاه رئال مادرید:
مردم همیشه دنبال‌بهانه‌اند. تکلیف‌فوتبال‌در ۹۰ دقیقه تعیین می‌شود، نه یک‌لحظه. مصر نیمه‌اول عالی بود اما بعد از اینکه ۲-۰ پیش‌افتاد کنترل‌را از دست‌داد و آرژانتین استفاده کرد. این تخصص تیم‌های نخبه است.
🔵
مردم مدام درمورد داور و VAR صحبت می‌کنند، اما دلیل‌بازگشت‌آرژانتینی‌ها کیفیت و ذهنیت‌شان بود. مصر نتوانست‌سطحی‌که ابتدا نشان داده بود را حفظ کند. اینکه مسابقه "دزدیده شده" یا به آرژانتین هدیه داده شده تئوری‌ توطئه است.
🔵
بخش‌سخت‌فوتبال پس از باخت، پذیرفتن اینه که حریف بهتربوده. آرژانتین‌شایسته تقدیره. مصر باید به عملکردش افتخارکند اما از اشتباهاتی که برایش گران تمام شد، درس بگیرد. فوتبال همین است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25290" target="_blank">📅 18:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25289">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQu9N7CAsntbIZgye8colJJ5tHhcQ1-j9INyOnjKfdhwr6tt63gRbcVRpf6tDeus8yrkibwyewOm7FaO0JYIw6TPd-X2gVfJxcy1Aacvs9OUweD9V05F7ETdz2q35coXU5ZWoTXwL-g262juH-bqNLTde5rfa_y5o1qF3E4frF6UvkUrY10SL5GIHsYzT8Ot103D2eVdl_Vb1f9o6tJF4pDaDHa6hFJMe4Zwqw-ndpSj83eQ7EQqkOxxpn1iEqdu8uBDxbvdRyBabHmA8dhQ5zood9CODjnvL1Iuo0IRMhAesRZOD2-JHaayDsb0fD8LqUNc5YXicVtS1FD73qWQFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25289" target="_blank">📅 18:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25288">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJJPotHt5WPAC3flGuVqbPj8aXZ6_MzAzMCynC5RV9nxeoAFs68518JGWgLd15wZtWkOroKQvjLzAwv0-Eui3SmusjjW3GHbAzDHjgemAVAq0KvEdeQIuRJLncaiU0Q4WBczV9IwLkcuQhDjdg8-D7MHZAiCDty1WA_xB2R3q_Z2wDg68KgVyq3jW9a_K4yrLK_2M99N_Ehw-xlZrmsqYrP3XTtw9ubHmBMN-4MdgKmH9_JVdbBUtOy5Q9FmGZOI8_WwP5UwOE-hS3PY7HmSZr91p-h59VAoo0eydbgFLsZy_vl81Oigawd8MOWs_aGihHhvvXAG1-NAd3vj343cyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تقویم
؛ بیست سال پیش همچین روزی ایتالیا با غلبه بر فرانسه در ضربات پنالتی قهرمان جهان شد. با این حال، این مسابقه همیشه به خاطر اشتباه فاحش زیدان و ضربه‌ سرش‌به‌ماتراتزی تو یادها باقی مونده.
‼️
زیدان: از همهٔ کودکانی که اون صحنه رو دیدند عذرخواهی میکنم. هیچ توجیهی برای اون کار ندارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25288" target="_blank">📅 18:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25287">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekago3uKa0jLJ6z5zRAbfS5gc4qW5AUAae1p_YQKiPxT_1q0XkJLUfFyWvjT8oKy72B8ZwmW81w7cTKhilAB-5zt26iFhkNpbE0Tj0IYEjPqpewUr7VoSdua2b-OKnVoS-g2hZXJEGgaxDAl61GzHHuCwCsV1w6r9j7Mtx8cXxVHaJsVG8t7-YjNUdv_Bi8M6U5o2-4zS6cODzA71vLeqOwE2nnHJdQ9hKZ75LSJeQ5fagtq8lM87yiTmGGBMZybBu3rZvl0wkOSmq2_b1suZy5D7oA_2MumHZ-ONJj67gRctMT7Xwgz2pYrFFq7BRSvoyAiO4IfAl7LkL7gPBm9RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ طبق‌شنیده‌های پرشیانا؛ مدیریت باشگاه سپاهان درتماس بامدبربرنامه های علی نعمتی خواستار جذب این‌مدافع ملی پوش شده و به نعمتی اعلام‌کرده‌حاضره‌برای دوفصل‌حضور دراین تیم رقم مدنظرش که 150میلیاردتومانه روبه‌او پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25287" target="_blank">📅 17:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25286">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXreE3QSMIaQBI_nkj5u2UkALZmaWAEv53DInTkw--ipj4bEQ9Pv4BXavRbrQ-9-xH8oMJsrt4iSwS0pBwLCRl7D_P7thFHCJGS2Fn1qTZvGGc4wIXcQOdFGEfUL45jFmC1OssyTkeddW4twcbogAhwP3PuSaVWVeh1N-6sz4CIyljzA8pZbZVBtKT0P3z1_I4_qSMqOYAQSdNauQnKQ2-M_T-_xOnaN4g6ZszZY9OMLCLP9G7WxkY7o4cFpiD1qy1NCOXz3BTR51jury9GLQKkHZJrPYhaFFLbftbD0N8klqgsc1sV5rUSnTB2qjoSfB2hiJucipncgz7wf0kT3Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
درخصوص اوستون اورونوف هم پنج روز پیش خبردادیم که چندپیشنهاد از جمله پیشنهاد الشمال رو‌ی‌میز مدیریت‌سرخ‌ها قرار داره و با توجه به‌ چراغ سبز مهدی تارتار برای فروش ستاره ازبکی درصورت پیشنهاد مالی مناسب؛ احتمال جدایی اوستون اورونوف از جمع سرخ ها وجود داره.…</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/25286" target="_blank">📅 17:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25285">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcGw8v7N0WD4Q42noX-PEgKvSop0cdJSMKF7O-7q_wlfl27Ou-25e_Cp1uO7ZDzCbyfb1JDShQW21qBfv4CDELeycM4aVouGXv4HWGW9-VT0GPDWrK5QKwjgL9rJHyoFjZyYjgHZU-ymEnKdj3hf_5chkJ2DhI-6bLI_e__-eRJ7LZaLSaitZOQG08kOjvgILNzc11FrTLSxrXDsulcnl4OBBIMZgoGRTVA3qvi6_ArD82KrSWKw3UyY6lqCve5y95pu-iTalQVQ1YjFDMeE6HyGkvs33_ExPO-8fDcmmKx93a3KFFVyMVHoP1H6FujR_8xxyuGC5JwetbWQ8sqUJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
ارلینگ هالند روزانه 6 وعده‌غذا میخوره و حدود 6000 کالری مصرف‌میکنه معادل 24 چیزبرگر. هالند عمدتاً به‌مرغ،پاستا، استیک، ماهی، سبزیجات و عسل علاقه داره و بیشتر آب مینوشه و ازتمام خوراکی‌‌های شکردار اجتناب می‌کنه. جاشوا کینگ هم تیمی سابق هالند گفت اون مثل یه خرس غذا می خوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25285" target="_blank">📅 17:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25283">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-PevOcgXyQZBR6hIKla4Sgpr1uQUCi57qMdaXx5VUpFz1K0xYHBqOYOE8RipiMz5-uk_17YDaKKD2YYeqI6wU-rtJQuL71ZftsKUz6OFZ6FPXHBm_kyYLhHwZrEMcwTSGuK6UeSDiCK0r3uNlEFbrH23Rz1DoIREDM0xp3A0XfR558OQtDwl6yPpUbXVdci8AN8skAlmJFGsS5fICuegnugkt69LGZxl5XXgOMWKkDL2_-O2cfmZUhXjSDmYk0RiUziPF24O5Vz8-LwyXd0Q4RbzRwmYXYQVC16uoqqGeR7g-2hP5P3LGttCNK9AlXtTr3nAAn-Dk7Wh5BKVk5Hwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
جواب‌ فوق‌ العاده رونالدو به‌ سوال خبرنگاری که گفته بود میتونی‌ اسپانیا رو ببری: من تموم تلاشم رو بکار میبرم تاوجدانم‌راحت باشه حالا هرچی شد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25283" target="_blank">📅 17:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25282">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkBvj_nc-IGfOxsOWK6H-_NR4GcohP_U5PA-v-K_fs6Tb2R2aF8k5ExsMhjyz58ZskjX_GXnWzMNpatQDGrDm05ZUNCmTMNBUAxl0MIKjkv5LCIEyiiFRgGBBSSszqr4C-KtCtKFhLhSCjU87otVDAE2AcM7araGEg-d_KzOiS6Xbk9VTVDMDPuNAtEE_R6-xOYWOSjAOxXD-jJcroH6jcn5TwL_zqr6gFQU52bTR5yyaqIjDsUn5N1rw-R3F8DCnqOA6VNmeKt56irFYIZcol7u7VuPdzS-gg7IohX4-XJS1R2gx-LkTcGLEl-RarVJX2k9JEsYJlRdMlNnfyZ8qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی دو روز پیش پرشیانا
🔴
پوریا شهرآبادی مهاجم جوان گل‌گهر با عقد قرار دادی چهار ساله رسما به‌باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25282" target="_blank">📅 16:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25281">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RO4Qjj24mVQg5VIPJISB9bI0GsYQU9yZkOxAe1TpHUs0zvErDXfUd1UhzdvcP4AwEZT9CpGegyv9r0qGaW3jVOV1tYniP_8tCJMxmONagYBPghwWavdOMdkJ2LxL0xs9HeDLgOKzHgm3R6GeHbdVJ04uVNBRsk4rKg8veb-IqZrYTu3uKy0BT-c670zN2VUnHXTk3uw_jFn4JRUG11zJyNmlRFC6uR5SjChzlFYX7dsK3qEabdAiamR55uPXeEL0HpCCwWw2CvZJ0Rf-SSqpacN13Mi9Wh9kOTeh7V9-F26aEJ63ScoZ59Cxl0LDTnRnMN-f7cQwzz2VEezb42tV0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ پیرو خبر روز گذشته پرشیانا؛ پوریا شهرآبادی مهاجم 20 ساله تیم گل گهر سیرجان دقایقی‌قبل درتماس با مهدی تارتار اعلام کرده که قید حضور در تیم استقلال رو زده و اماده عقد قرارداد با باشگاه پرسپولیسه. بدین ترتیب شهر آبادی ظرف 48 ساعت آینده با حضور درساختمان‌باشگاه…</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25281" target="_blank">📅 16:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25280">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‼️
رونمایی‌از تاکتیک‌اصلی تیم قلعه نویی در رقابت های جام جهانی 2026 که سه مساوی بدست آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25280" target="_blank">📅 16:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25279">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQXlOU48ebduB_xaaepNw9zLM8bEZ4MhmuUCp5jjg5_29p6fsAm0GjPz1wRad-_2KqnBhEK-YBT449KSDVzXh0IznRzdr9y2E1PDNBxOK4LoqtZcPlL64NPn-4rlW2ks0YOLq6x1CteIkz_2bhv4xnGyeXNTuPWvJUBIgG9Hi-eToY2fs7vSjiSlO40AzfTBMTgKzCNiLkntspHo5DRyVqQwJRdiDokVY9wVbl1ypQwCg289YA9NZpM4xJaPfEi-YYlv-x2xq478bs06jRRjW4-Pp33lMsu90hYijyVxZJpV5xoPSZVUrw0xDAWEgj8kITO6JT83Qm6lqQifCQd4OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدیو لو رفته از کلاس‌درس‌محرمانه امیر قلعه نویی برای سرمربیان آلمان، هلند، ژاپن و برزیل در خانه‌اش بعد از حذف این تیم‌ها از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25279" target="_blank">📅 15:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25278">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7J2GFTFgm8HKyOgMbUT3fHorhCzmnjVfrXOBAxxJJrBYvWQOpFSlgLMcVkYO_Pe3JfCYVlnVSQf0CyoCHCJtT-u8h82mLNaTg38PdgWbxCFrxxUBLa8aGh2KQrtUof0tdMlAScztCjVNl5T2rKSmya7IwTBYD9pzPZKSuIj-hGhe6tjuJVyajiVz0JQL9uy-LFwE1JQnAT2t9TUTF2groKjG-XE_tMLX6VV0jlk0WAC0qF9A4fl6oGvvzEsRq33b1nGWqEkxoFLEkc_It700bgjTZPUxdGWLkWP7wGz3hwJTPFLCisAN1onj4BlnpfKV34iRNwgPFMcXUERUITmgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛مدیریت‌باشگاه‌استقلال میخواد بعد از تمدیدقرارداد یاسر آسانی قرارداد رستم آشورماتف مدافع 28 ساله خود را نیز تا سال 2029 تمدید کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25278" target="_blank">📅 15:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25277">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUNDvFDE5kxFjFiE0l9uIeK9BbhiPYexL541d-6ei3cmLufWo_pyRClwRMeWIhcf1iU4497c_2hQv_RXjWP1kxo1bSo1myHetPaL6dcZl2qGJrDBRa1zoWpyf-7c5_iFygMhOQDl0HQRwnp2HwKIpWuYYjDDokxvJiHOqRpIV6-tjKW8XVPpOa1eKHIDXHAmSrI_uectk7qXmTWfeSa3yZ8eOM1m6VZ9RVEABbo5sZ8q2uWPBougozlMMbxmhNWq5enF2GW7qDwvzliUXPzwkWqusHTSVYNBwCPp1P72qOFF6zsp_UgaKrtXKRIO3xL7hKBrsezVAuCOc1N3tLhbdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
#تکمیلی؛ کریم آدیمی ستاره23ساله بورسیا دورتموند برای عقدقرارداد پنج‌ساله با سران بارسا به توافق نهایی رسیده و تنها توافق با مدیران دورتموند باقی مونده که باتوجه به علاقه آدیمی برای پیوستن به بارسا بزودی بند فسخ او رو فعال خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25277" target="_blank">📅 15:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25276">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9xDnfW3wQW1L55hBK2mdmTqvuoxyQwArAofDJyyj7SAeI-b7jo-LiDNibLlU7-SIlEywLq7wHdUJRFJHmQYhAKrCY4BkaPkVLj8Mw3ucuYPiOXX47NhZrZEJC-GxyNw-fpw9-hLQDHBm8UPfF_VHsf869ZYpRZUS5iPoT55gq6mnK3Sxf1k2srs1PEeXHDTLlEOH8C-ASiJTqO4vFQkZMB4MvBkMy88XgbSlA5WX6PBaGoYBvqQnT5tmd3iTOlPEBPC2bVNqczjBQju9ZK38YWqYWsW5P7E1uF6o-Qr6hVcLcSZxJyaSanIhUNuBxaAu7Rw06SYl-y9inaQ4UQPSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25276" target="_blank">📅 15:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25275">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IB0WkkjEwbY9RIIJfrQQTyvFTU7pyC618xiciUk1asw0mSzLP04v7qqmuci58_4iQLNgIZi3ddIOTB82_Dbq_TgEbf8UdDJ6JbG0QRF686g6vg4O6HXV04MPfnyFzIYBDxrz3M1tWvJOVkNss3LVVNhCtYiwEpTy2ktxc6TFxj9vILrYnqhh0FqLFV8MLdYL3c_ldLTJvUvLY3dyWQkFlp1jnumKiVjPZIYpR2D-7daQE0hPWh0fyHPtsXctUjjZGMOH-mgcIyGEGHsp34hF9T0MyNJLQSfmIc1CihONGV8dUfg6al31GW8bljV-Z4mWT54T-R6wW1uspNmsnGKcaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی؛ ایگور سرگیف مهاجم ازبکستانی تیم پرسپولیس‌نیز درگفتگوبارسانه‌های ازبکستانی اعلام کرد که به قراردادش با سرخ‌ها پایبند خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25275" target="_blank">📅 15:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25274">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbnuphnUzF3Qs6Sow6Uav4DQ_01jnX-SCmcWl4B1jnu3Gy9SZ0s_GyHHGzGIT6Lr0AqalDRketV25mw8KfudAv_wdydDA-fxehF087VmwxIhwvef2Giz3S_OSuN68drHV6ZrsFbpw8pI_cmzWQGDS2D7iTZ8rhDpSsdO-RO3oug3hQAgZo434v48SgpRfAwj7aLaXixO5ZHyeXYwhECSS8qrN04qWKIo29f52DqCsbINEBUM7-ciURr1JCtgc2HRZaUS_4IlnLmplT1_lOKmjY0X7eTJycL2xYQ-RFE7YL7zkwTsr4a0FPoAVlylunfl8gwajbibVyLti9BAyGkwzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
آمار فینیشینگ و ایجاد موقعیت بازیکنان جام جهانی؛
همه چیز خوبه تا زمانی که گوشه راست بالا رونگاه‌نکنید. رامین‌رضاییان هم تو این لیست هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25274" target="_blank">📅 14:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25273">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPadTJjMwlcx-kaMJuLd5heG6DP9y99W79b6gNhP-illJ0Fg8z8P6MRz-yekE7L0UgknlAy8os0Q97SXJ5ZDHqm77WH6qY2n9HPcM4_zW7aZUPijLblVjcV7f988lpnNJ96vfdtyBHdbWUMf6Pxu2hv4zFIdJWXEFnobQaSg89U6gj8axRAl72bK58VHQsY9ZwZGkbuj1dvqgbnBU1W0q58lem3HGEBRV8IFhMUDikRr33uUN8Nb0vvegbxBmbTSbSspdZElXMDyFG4haw97wq-AFp1KPebS1Y-rFxhN8-6xl7TBniCafAbXGZi1e0qnAjjDm6yiniH9SsANsemp7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25273" target="_blank">📅 14:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25272">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uc4JKxG_wqiMOgAAGQ8GeTmf75sjBiWCWIyNSlGhrPi_TKV65o-Z04hLjlrZAqyyNm4nI0jLJ9fbfZ1MlH20pOFUtH4a9zkrslEWfuNTrA1ExeYfyRToty-6YNq3sHmJUAPNdsH5nMBZ98f3jUisdvepo_DIu5iSROV9qI2wi-pqXaNmlKLXW1vFCT7z6B3yXjS7ff-YjH_KsMYHWqYIRBofqu8ZoMMw5o7RM8vq4Lkd_UkwqpAjDS0yEuS1eHv20YQ6LwHmuaMlzNGWUlv-dBbLfecY7Fj02GF4i7iCgM0xOEM4I5nQJAqeh2HP7diKKe9HlyexV933F7Io4OuG3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا؛ علیرضا کوشکی فصل آینده در استقلال خواهد بود. تمام‌توافقات برای تمدید قراردادش‌ انجام‌ شده و بزودی‌راهی ساختمان باشگاه خواهد شد تا قراردادش رو سه ساله تمدید کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25272" target="_blank">📅 13:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25271">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8VWBHxUZkgNNBOWc0T3GUZDT4jwKmsXIdHZpBevNVRbfwGOWJhyozurMQz0GH2bBTCsfsAWVnM57pcTJRf7ID6tGOZ4OO-emigWLWwaHTjrOcBe1-unqnUDQ3QptlqfqxGCTClFdaBaegTrEwX0iw05Bcu9Cz3mMcYAegq00VeSfyVBebvVmvS72m25dT8Xd1Xz-leSfbMP4VrvXWbZc09uzxQwLBvpypUnJXfbo_AZ-oc6gXQdvuym5P4_dla4YW9Q80dHx7CDLga8hAR4a5-386ElUrf2N-4TBHoBKw-E0a_f6efFniNWxGXCVi2nAsDFGfN3xz9U82lwskwWsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه استقلال باشخص امید نورافکن برای عقد قراردادی 3 ساله به توافق کامل رسیده و هافبک سابق استقلالی‌ ها برای بازگشت به این تیم منتطربازشدن پنجره آبی‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25271" target="_blank">📅 13:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25270">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a5P05M-5ZaqhxtavpmexaeoyTGbnMum6S5pSino9TVOrWcyYP5hdI_K8Sva-6NZscdyYknFMLck5JtIT8-8RKIZxCa7b4B_I2OlNNEcDTVuJHRTyOQ51JfXdyVJ5feXmrDgtxHOL23IKaf2gtFzgGOOOuoodWROx7ICim9adbJ7hbpHyx-jkswNJkkRPK_xQ3yItrFPnBgJHMSS7VWBnhJfMzvJY1dpAyYMS-JZwP56JDtcCk5q9p2iYb8aoPfFlTQh8PYHZfrGA9ggTiqHd9V2c07yDkiL4vnEfmFA5WfEQUVfty83WAZ694ggtFl-LhCo8L_7_5D89ywb95uZKHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
باشگاه یوونتوس برای عقدقرارداد دو ساله با امیلیانو مارتینز دروازه‌بان تیم ملی آرژانتین به توافق کامل رسید و تنها توافق با آستون ویلا باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25270" target="_blank">📅 13:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25269">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwSuHrSug6Dqc-Wsvtb4BAkUdbNsZcQZ3xZJI-zQF06LphhxXYpd7ovVx5QD6HSSXy6djzc0OJ8wXVtNptuAKGMIhv2gGvYS7Zc6w8xZaQU52QXdEXcl2t-yp8KtHz5AAHkwV_TCSy4R21T19NmiKYXCia-anR_60VYkwhXYZIMHVB57-krnRQOv6LT6nF6HHxLwcRNuN3bCI1XSIniUOwQRVSExgXHMglb2bBLJ9rqBKG_91qmj__wZetWTvEOMr6fJToL0s65Y8Ts0EmxmcY1L-b3w4bf_0W80-dTm24XhBCUzAzyDaRdvJgLZu5kMVFdPZ1wYyXMhOtCfZ85ZtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
کریم آدیمی‌درسال۲۰۲۱: بارسلونا یکی‌از بهترین باشگاه‌های جهان است و برای من مایه افتخار است که‌آن‌ها خواهان جذب من هستند. در خودم میبینم روزی به این باشگاه بزرگ بپیوندم و بدرخشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25269" target="_blank">📅 12:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25268">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdIRT3wJEZcOWF5sieXyWgLt2KnVpg9Lo5suqRmUl5JIduw2H49nb60KtT0qV5AEzRAa_Zl284oayiSoUQkVRdr1jM_ClAeSFcmutFEZ2cgvOu_yYUzdqCqS2-fenGkPb-bvDrlrjjRoX1840wgf1Kdjv_7iFgDLvMVwNy8oL1VBtRJ9cov7mx_fnFAZQzIH0R5ftaDpeqpGZfYIaekhl3BxJooa7Rl9DhA2GkKyRIxzlHj3ww_M4DJRavz8TFlFtlHL6Wbpdf_dlwQN9takBw_YKxzOZnO2skVa2MrC7u5xq6-BoVhk9lBcYbJ68F3uSRWM8gMsApwiSk-rGLq1kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آپدیت‌عملکردکلی لئو مسی فوق‌ستاره آرژانتینی 39 ساله فوتبال جهان در کل دوران حرفه ای خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25268" target="_blank">📅 12:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25267">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30af4fbd6d.mp4?token=ssx6WfHJHHF9s7F8PghDPZebTKqeewR-88L7HqVaYILFoQz7mRI_yawI2Qcz4dMc31PsdB4twoqs2SiTNfUYF3vaf9cF4OwS20laE3AHx2ofqc8rn-Eh_2CQgc6IVe1jOD7uDCukBEOoz4cyWVi7QODJGEMzGivE0hOxxdy6EFqQalQyZlMKzkJcYhLH2RuehWVFXN9vG2dR_63HfaJPG-F6FLBDSN5g4PyRQtAeD88cpD2Rx_crVZDyYC4U9nToocUvbdj3p1BDGSXxOaeFad4VbBUiS_fBS65TQsSo5E52hHDSrcfWVCNPoCmIhEgRltMrXv-p4JmGDKMfpxQc5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30af4fbd6d.mp4?token=ssx6WfHJHHF9s7F8PghDPZebTKqeewR-88L7HqVaYILFoQz7mRI_yawI2Qcz4dMc31PsdB4twoqs2SiTNfUYF3vaf9cF4OwS20laE3AHx2ofqc8rn-Eh_2CQgc6IVe1jOD7uDCukBEOoz4cyWVi7QODJGEMzGivE0hOxxdy6EFqQalQyZlMKzkJcYhLH2RuehWVFXN9vG2dR_63HfaJPG-F6FLBDSN5g4PyRQtAeD88cpD2Rx_crVZDyYC4U9nToocUvbdj3p1BDGSXxOaeFad4VbBUiS_fBS65TQsSo5E52hHDSrcfWVCNPoCmIhEgRltMrXv-p4JmGDKMfpxQc5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
جواب‌ فوق‌ العاده رونالدو به‌ سوال خبرنگاری که گفته بود میتونی‌ اسپانیا رو ببری: من تموم تلاشم رو بکار میبرم تاوجدانم‌راحت باشه حالا هرچی شد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25267" target="_blank">📅 12:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25266">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vF7SKCiEmubnTSvlYqueiELMHmiPbRSc10XQ2WxFjANPNPJXIt1j7_Czq6xAaEctV9qNcmGlDgXCSLOQgkVU9rYH_FcGY1FHYkUjMQiTqKNbOY2PycG21eT_uUOUnt1iPVPmw_kfhQxVp5hsp9nqSMP5mbS71Lsj8mm0H5N1R4CwOU9vHop265wVfmrmCIWl4eu8zp4MOauHX2JoZqcWYkEGZHBi2E7PYAOpXy4_rJRF6xUz5tksaJRdnUCkB4dNWXZMAPNsEwpp_87EmxmFf2mw7ff8X8CXs6Oy2HAf9G2FxAliSj1FqU0SANG2zqmExxZxbD3VQexoTWtrPDSwHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛آمادگی پرسپولیسی‌ها برای‌ پرداخت رضایت نامه قربانی ستاره الوحده.
🔴
باشگاه پرسپولیس ساعاتی‌قبل‌باارسال‌نامه ای به باشگاه الوحده امارات اعلام کرده تا 1.5 میلیون دلار حاضر است برای رضایت نامه محمد قربانی پرداخت کند. اماراتی‌ها 2 میلیون دلاربرای…</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25266" target="_blank">📅 11:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25265">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzeZCJeuy0d_pype-SrBA5tDXzD3pnw9zetPWsESMDMGjPNPDia62Ub7fYktlmvYRHTspK-ZXuYOlJjBikNCBB_H85k7I_LZDKqMRZI6p0jxY5tyv2lBOIFUWuI8_fp4dCvyIv9vCyQXhP-aHuAlCMv1oX5o3f7rKNJuolKBjbPmyMGw-Io34ZA3X0hQATLWQBYFToiGY23cbRoMlITk-oME3R1WdOJuqwKQv7rng1S2Bk-Ss8juy6K1TNz3U52oob53kqX7sz8HV_k-xbTY3MBL-btu2fvN6oNylr9HIQli837ataRUScvVck6ecqRe8-jtQ2gJluL7IlC5Nd2A9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇳🇴
پدر ارلینگ‌هالند ستاره‌نروژی منچسترسیتی: شاید روزی در آینده نچندان دور هالند رو در تیم رئال ببینیم. ممکن است اتفاقات هیجان انگیزی رخ بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25265" target="_blank">📅 11:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25264">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKkcvb4Eys83k94ozEqulJJuYiwKzGBGomad6vncO_9vR-_pbRfxzgcuNmISgn0mwV2Dt4DUmeEhpti-sS-5FhF-2KQw2bD2ikr8ewLqYH3gD_8Od_tjjE66jqlmYFyT83Q3p8mOAuZMsxC9vkSnNVgpbFM_tdM4smfheLXniso5w2u0AA3Vs6oJD3bC1eqp1Dodop8CClC0mIrh973HCvGg0jxn2F6s5UgjFnrUsMT_0mm6QWalb0rilkbM-0rFaHNm1Ao7k9clJ04E3xfzsnnDPj1q0HCu4qFpidWEf-SBX_eFZDtk-mA2-xrZnsmeAIbAM6fceAgoG36_AmK0rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی_پرشیانا #فوری؛ پیغام‌جدید محمد قربانی به پیمان‌حدادی مدیرعامل باشگاه پرسپولیس: پیشنهاد مالی شما رو پذیرفته‌ام، رضایت نامه ام رو بگیرید روز شنبه قراردادم رو امضا خواهد کرد.
‼️
پیشنهادمالی‌پرسپولیس: سه ساله بوده. سال اول 80، سال دوم 110 و سال سوم 150…</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25264" target="_blank">📅 10:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25263">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94e6448be0.mp4?token=ksfrx7YI3-3ArkfoaAxlCjI8ERfDxRXO0dH3T8Mk08svEctn-JYNdJiaEl4YZ0lSnhfES_y7ywJnzAb9VyFYKJdemWgYjhY2Uq3vf1Kyy50r1SLCEeYFyg-na9o4w0_vShYDuOg8CtfT70zd835J1czYaUlq4VO3CZd2KYTXMHzzelKCFpDrXgxbPvbGong3sbLmnPrQ-MNBZbADCtNoC0NyrkMJZAdggK_aNCuE5AcCddj0QvCrCulWGljBw0YZD-sSfUASDEfy0AN8M-rNEh2TXlybnXhvhy3bhea58TD8IS9zL6lJGMk-xDz90q0SP4WmepUQsHDezKCaXcJj_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94e6448be0.mp4?token=ksfrx7YI3-3ArkfoaAxlCjI8ERfDxRXO0dH3T8Mk08svEctn-JYNdJiaEl4YZ0lSnhfES_y7ywJnzAb9VyFYKJdemWgYjhY2Uq3vf1Kyy50r1SLCEeYFyg-na9o4w0_vShYDuOg8CtfT70zd835J1czYaUlq4VO3CZd2KYTXMHzzelKCFpDrXgxbPvbGong3sbLmnPrQ-MNBZbADCtNoC0NyrkMJZAdggK_aNCuE5AcCddj0QvCrCulWGljBw0YZD-sSfUASDEfy0AN8M-rNEh2TXlybnXhvhy3bhea58TD8IS9zL6lJGMk-xDz90q0SP4WmepUQsHDezKCaXcJj_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عکس‌خاص‌وعجیب‌وغریب از 18 سالگی جواد خیابانی؛ خیابانی به خداداد میگه تعجب کن ببینم چطوری میشی. زنوزی‌هم به خداداد گفته بعد جام جهانی اول باید یه ماه تو تیمارستان بستریت کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25263" target="_blank">📅 10:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25262">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d48Hl__8MQBlt3t7zIiWk0MjaFQnkW4pH6l9OgU7hI6uaULe66Sd1_12ZO9P8PddjAQe0kMeAk5m38uhTaomJZsFgwQxvMTop9PRMMgbOPug1SvnI5I7kU-nXSb5rEVozg7FB9sty8aT-74X3yeYaV2k4h6Req585d4mwSNWKJQHMSjXeb30z7h5TfNH4i2qsTEO9274i4LWTIe7nXge6hrKcFQrjinyDTpLBSp_TRkDl_ki35mZKKb8z7nqCE6HnJnJ93nuAsUvX8b3X44FtfJubJUl_Yoi9ThiYTJACy7Ovsk0BY4vkk6PHvlpbbfvNHzryG34ntpNBJ7BxBfZIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نوع‌حکومت در ۱۰ کشور برتر و ۱۰ کشور پایین جهان از نظر شادی و کیفیت زندگی؛ منبع: گزارش جهانی شادی ۲۰۲۴ و شاخص کیفیت زندگی ۲۰۲۴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25262" target="_blank">📅 10:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25261">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fN_gv5W9nQP0J5c7xMjDl1VsQR3EmDXa3XFSicvyNi-Qc2olYC5pcydvTpjrwbPjxYERAq0oeDkFMY0pp-OxSkDIQ6K8e-F5I05iCkXeZqmFEmnoRRCVfFE8hLGqcNRGeitE89tUNjeC0_4HB0eiEItKfe2l6KhL7DGAXVCt-VOqU5TjFFTDCBVDVHSc_a3eofbajRFxJKQ_jE36DwfGkEgVU8CqLgrLU5k_-hOnn-vnjqRhmUH9ZpXx7_P_QeETcjurep7LOiBKNrtaOYuANkeaLGQajJfdCChxGHXsSWqxTBD1TlWxJpLzYb7qlRrCqGTJVWKbI1TUe1LVNGopMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدیو لو رفته از کلاس‌درس‌محرمانه امیر قلعه نویی برای سرمربیان آلمان، هلند، ژاپن و برزیل در خانه‌اش بعد از حذف این تیم‌ها از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25261" target="_blank">📅 10:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25260">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktroNgGRrK5U1f9hrn2ODAhK47V03jaFvi0ERV7d35xEi_hjXrlM0h_O2TXunnP43hfArh4VOhnvOntE56956raJ70-Gcoi-FimsDnjgYZ4F8WGsAF8uTXWsu96QmT_B4a2A27u5fMyRjsl755YL8XZLAG2eesMIYGL1qrMhevdtnibPyfYASogR36RYQNgIHRsTuFwf-2xvuCN2HKcDORekImJlikr3bvO5sjew_yV55AcMEXTOM76DnAAFMi95xF_CkrPUISoS8jzd26GT-mvxpMWkdzM0M2X2mhMZXoDrGTfd3AvUS44gG0ZsfNdBSfEW3uybdYy-oOc3J5-07Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
تصویری دیدنی از لئو مسی هنگام زدن کرنر دربازی شب‌گذشته آرژانتین مقابل مصر؛ آلبی سلسته شب گذشته با جادوی اعجوبه آرژانتینی خود سه بر دو از سد یاران محمد صلاح در مصر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25260" target="_blank">📅 10:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25259">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-boGFRzrb0Q_SC-VBiWXLEuUyXe80prguwvVAebucvJD5a9YR9tBDqt0Oe-aHsW_lDqIHMF2ei0mW5McjEoQN_BeYLzPPbQHjV-3LbtJQ-YDCQUXX7tpoissOB-M1I6UY_zIUYRofW1AJYE1WGUQgDFHCVEKHdH75Iy5f4Jp1NExeAy0tp1H24XPX9JUujTnp9qExh63pTb3FY6x4ZOkud4jH0nXMp6Z7v6JMbHo01jkDSut2C8tnqaOlqYRUz7-QJJ7HXbCL4n91V_k1HIV9n_1b2uMOF2sKThTMUbcsWeGRVfUM-xatuqcQriF6yLjehaXhx-QtRM4fyTVRhDyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ علی نعمتی مدافع‌ ملی‌پوش سابق باشگاه فولاد برای عقد قراردادی دوساله‌باپرسپولیس خواستار دریافت مبلغ سالانه 75 میلیاردتومان‌‌شده‌است. درصورتی‌که بانک شهر با این رقم موافقت کند به زودی پوستر رونمایی از مدافع جدید سرخ‌ها…</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25259" target="_blank">📅 09:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25258">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2_6tI67O3s0I2Gv2aTQVNjYy3qQxtUNfJrfaqgKwKbHeseowcGOVXol5t4YcwnQ4A-t1bYxceRhIdad8_-lmR9QQOxOLj2pgiprDBcGWtfMWsb3drQfhdud8TmurL1VTWjlowAZyTiGMdxsop7h8dUGAagAyW3xC3B8MNdC2JPK9aPk5hCtoe1QC9JACHFnHV7CIPWoFyWNbvH0tElWIfF2OODJqWvpc4ZCGJVu6luUWB5Q8rfov3is_NeA7-DOguqrvcIOIcf5bpPxfqbYKBOreZax-wqRZiIEFSghAF-XvFzFc0G3YTlc1znpotUNZWYpbujFeu_7JfFmyN5nPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25258" target="_blank">📅 09:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25257">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzfGkTMnHVozBFugO77si-HAJTQuRKRlL7a4p-xa0wHVz9Qyt6_nY_GhP4cPbGyTioBhiDKwcXNyDxEeEMIMn_BwdgOdBOCBosvUk34UMlUdeVb0DHwdUitEme9XZYFBW3zZI8L6veSwms2leS5JrBpx1Po-0C3aVo_V3ON3sYLX99sUs9KeIR7kPgLjEVFMplzOozgV86Wc4qtmguTWQ-HHdiUCaXfVrClk8u6DDnDNTCbRpChTD0Z5zsY_OFvtX5aooA66PyEiE7AjXmR4XbgVNFJolLCIkpBdvOuQ9pdBhQA-FuM0jPDnZLUVR9-aG9SRhPi1MwA_UwCd_-IE3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ آنتونیو آدان،عارف‌غلامی،آرمین‌سهرابیان، محمد رضا آزادی چهار بازیکنی هستندکه سهراب بختیاری‌زاده به مدیریت باشگاه استقلال اعلام‌کرده درصورتیکه حتی پنجره نقل و انتقالاتی آبی‌ها باز نشود باز هم نیازی به حضور این‌ها ندارد.…</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25257" target="_blank">📅 09:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25256">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UENjkeMBhhKpIw8Nz2PzgvDXEzkZHwUCLepCLKraT2ah0U-jv2VEoHA56T4QnaxC99V0Yi48_ac5hJXjIY_4FqfVeEYcF0wWBd9K8srEv-Zr8Lfd3m3cPO4UWy7gqOKtz6Wjaf84U1xX94kD_gI4ziN7a3OJFVPNI3fxORotphwTN-InU7KHbgyss9OiLfYlwjXEw_sXCFX8dASjiQ1GsSzLKYbBseAUaoeGW5RyyJpBMj_2PzAuGvOKo9OmOPjwqSVndUi4aZcFSeidpamGU2soNReTQzh_dqDpZ03XR5SEmm7u1xpZNl0hi5azY595fby07o7onTwpKz2mResXaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛ باصلاحدید کادرفنی استقلال؛ آرمین سهرابیان دیگر مدافع میانی استقلال در لیست مازاد آبی‌ ها قرار گرفته و بزودی از جمع شاگردان سهراب بختیاری زاده جدا خواهد شد. پیش تر عارف غلامی نیز در لیست خروج استقلالی‌ها قرار گرفته بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25256" target="_blank">📅 09:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25255">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8869652ba6.mp4?token=gTbZKkgWVxwPUMf7h1MVa5zZki5K1-jkczx18P2l1kZq3STesoNpuRK97_KLJDyNKQMRGszn7v2ETGP3jqFPHJE4iFQBtlI8QzPhRXRR4LKbMVN8DpcuMf_pzxlpDiijctIJmwWvX-qpM-FoxRjX0lT3Rq1HpBYOexixVncmipQbcRS0K8cC_PIYQPZ7nyTbQYqKTO0cFuCHcBKuGrEBWUxCAaWjJVNZk5P8V5bZxXxaU89UgkXy6GTG1BMEzT77o1UNKCXClt7drBiSDFpacAnVGtjUnlhkOZvHpBw60iXEvtx-nc65op9HNlWD9mjheXnTeblvPuv-wPW4gPmt8TVvOEitRpW5K9m3cHDrsKp3LUonEJglf1Tf4eCuAdKLI9RVsS9lEK9fd95tAzVuJKTr4OFXijeftRRCQc5rIdET5VolyrLGw3zifwEJHwEO20aYdZH8sv11UFfvaqIM2XjHOKjtu_FFV2L-fncK7JpciQ0JrnmVYan1c7JNFlMK2Kpo7XINks1zl_apkYzyjHxYPlFszh1qh_IoDcWbqDksSOhw9pkXkKHhq-srxjvOk71R7d20bHVXy3-jw7Xldj0zIXgiEeVUM81Esn9xdGykHi913GnP3SSAKt4rSVBU4-n9if2DlQkHTNgNWeHybC0hDX055YS3mDhX1oTchoI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8869652ba6.mp4?token=gTbZKkgWVxwPUMf7h1MVa5zZki5K1-jkczx18P2l1kZq3STesoNpuRK97_KLJDyNKQMRGszn7v2ETGP3jqFPHJE4iFQBtlI8QzPhRXRR4LKbMVN8DpcuMf_pzxlpDiijctIJmwWvX-qpM-FoxRjX0lT3Rq1HpBYOexixVncmipQbcRS0K8cC_PIYQPZ7nyTbQYqKTO0cFuCHcBKuGrEBWUxCAaWjJVNZk5P8V5bZxXxaU89UgkXy6GTG1BMEzT77o1UNKCXClt7drBiSDFpacAnVGtjUnlhkOZvHpBw60iXEvtx-nc65op9HNlWD9mjheXnTeblvPuv-wPW4gPmt8TVvOEitRpW5K9m3cHDrsKp3LUonEJglf1Tf4eCuAdKLI9RVsS9lEK9fd95tAzVuJKTr4OFXijeftRRCQc5rIdET5VolyrLGw3zifwEJHwEO20aYdZH8sv11UFfvaqIM2XjHOKjtu_FFV2L-fncK7JpciQ0JrnmVYan1c7JNFlMK2Kpo7XINks1zl_apkYzyjHxYPlFszh1qh_IoDcWbqDksSOhw9pkXkKHhq-srxjvOk71R7d20bHVXy3-jw7Xldj0zIXgiEeVUM81Esn9xdGykHi913GnP3SSAKt4rSVBU4-n9if2DlQkHTNgNWeHybC0hDX055YS3mDhX1oTchoI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
علی رضا فغانی:
دوست داشتم هرجا داری کنم نماینده ایران باشم اماخودشون‌گفتن ما نمیخوایمت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25255" target="_blank">📅 08:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25253">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WK8MQzY9QyCDXr4PtuStw2OjX5WIE9Zza9SJbw-XVCGAo595bKE4rzI7sc8cy7q-boUfuk98FCynC7WALNPRDQH_G8bah9NWUd-iu-FNKbwsfwRzyqW3I3ipFuYUNngyclBM4Bl2FWJSBYUlHkksReBX3V0kwk-vNh_B8IdD6dxAXlCNY8E10PHO18MNTCPPiA6qk0sLupQd3qWSYW1LUf75GuqXJCkLzKg7ZbULHufUihWRazdUOr_srHCBLMS4LVcdpDNGxggMWZwMSJOviTSEt14urZPcpnjyrnXleqf47t_DNhyZqttWYkkjeJajqjaoImbldWoRpMA-9SO5IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امشب؛ آغاز مرحله حساس یک‌ چهارم نهایی بارویارویی‌مجدد فرانسه و مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25253" target="_blank">📅 08:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25252">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4Tn38OQsr9W03gxXlvC6bHqWsp9dgKuSMBm0rluA5AIAvcFnOtxBCvEvwLdHGAKhQhmzaKer0DnMycsqNQdxMyq59vpEGtWH85PF_wyREKKQyZ2dMB3-osKeb_vsxRg5F1OxFor7rnoXTf4YnXxhQrrb-_SdJpaVu49gB50qDy5dZBpkj8qO8xAPUUR7Mfl-QBHzZ6hQvobD3NjyVTBMr_K87BA9YQmmo8bxjPbtmkaecshHgM1llxEEfR5WsvNIRqJxl2oiJyOBm900vwWqe3ba4D1opG3TWd-keqGu4ed-JrIkb9gh-X5lYfcobiwHAnHgkWW9i524Eypop7RPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
جرارد رومرو: ممکنه‌ طی‌ روزهای آینده کریم آدیمی ستاره جوان دورتموند با عقد قراردادی 5 ساله به بارسلونا بپیوندد. مذاکرات مثبتی صورت کرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25252" target="_blank">📅 01:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25251">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnXAqpRyoJwmQUiUlzdohi5hHPbbA7eAjgxVzWmVSfzeXXRaDJOvLeT03IiwNs0Ta9BQ63tSYmjFbzATBalHhv7m8iPgXx7dZWTduhQZQeHFFPPMY7yrAxc6sPRgzB3gr9s9TA69MrqXe3jsAYU-JTcinkAZyhzlt6Dib3KRO5VN6dxE2KTGEJlbESN0doyoVa-U4w_i_4_4CoY_TBGkBn439uUHcPKAtmwCrXG4aHekyAnTTn1A4KEBAKI0q9re9tPQW-fQ2qu4DvXQ7ruOgUdUATnpN77m0RdKk1uzycrQ3mErv7h2DPZaaBOEoCd2X1nGCPV9afC4CjgpHkzHwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
نشریه‌بیلد: کریم آدیمی ستاره 23 ساله تیم دورتموند به مدیران این باشگاه اعلام کرده که قصد داره از این تیم جدا بشه. منچستریونایتد و بارسلونا به شدت دنبال این ستاره آلمانی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25251" target="_blank">📅 01:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25250">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6798637471.mp4?token=FIPR4RZZ8PXRoiWuYa4EDbJENdo7KQNxqPzFAd09SjGvnLtRcjt5_x_i7KD7d0xWMiAYn6yl4mKTV9HJAZDONXjt6vxNkaSp5xrymWClPJGEviKt9FMbaS_im6cCpkLLcBmMFOtTUyU8b5zOdmuyyyJ1TOfpXm_DSx2RCbsY1ZXgaD4RpFoyIIHtif2hFSxJWHYBcZF04YWW5W27pECALfX-bfO1Z2aQ4HVQDXupK7wgZH3ofRXI0AMViHs36btzYhBNiGhwjOBE4xVKTT4lDP85WBScRwu_vSQqaRefZ5pFBb1g4lRk7-MgJ1Q1F9byG0QiIaB9Bt958BAFqP-WVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6798637471.mp4?token=FIPR4RZZ8PXRoiWuYa4EDbJENdo7KQNxqPzFAd09SjGvnLtRcjt5_x_i7KD7d0xWMiAYn6yl4mKTV9HJAZDONXjt6vxNkaSp5xrymWClPJGEviKt9FMbaS_im6cCpkLLcBmMFOtTUyU8b5zOdmuyyyJ1TOfpXm_DSx2RCbsY1ZXgaD4RpFoyIIHtif2hFSxJWHYBcZF04YWW5W27pECALfX-bfO1Z2aQ4HVQDXupK7wgZH3ofRXI0AMViHs36btzYhBNiGhwjOBE4xVKTT4lDP85WBScRwu_vSQqaRefZ5pFBb1g4lRk7-MgJ1Q1F9byG0QiIaB9Bt958BAFqP-WVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جوادخیابانی‌ تو ویژه‌ برنامه‌امشب جمله معروف
"گشتم نبود نگرد نیست رو گفت" خداداد هنگ کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25250" target="_blank">📅 01:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25249">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ni_bKPppktNhUXAYdYQdIUjx3ffnJn0a5ErIXsWq3QhWIcGo5QvlkgBYdf7iWa5RptrgOtPYz7KGDtGQBdO0p2-ReJnJhjRsBBax2ZQBCPJKQ0Cs8oYT45yDS4wRXKIVLJ-Ho5tQqmgDQN8v-62PbOtlLUtKaqLYgMyO3zMFnodjq3Uf111JcemevR20pT7eG7rG5jTULJ0POt7xXUdRUFeKeXMklrj5GA1Npn_w44ROrxYadfM_uocSvrilyMisZ6Q3mY7iwJp2RElJBBnaVPCVHZLys_WCrZ9RciYju4K7lkCucfQslxIg42eSO--LHOi56vsRtJ-FzcsIvf5ijg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
خوزه‌فلیکس‌دیاز:باشگاه‌منچستریونایتد برای‌ جذب‌اورلین شوامنی هافبک26 ساله تیم ملی فرانسه به باشگاه‌رئال‌مادرید نامه زد. کهکشانی‌ها برای فروش شوامنی ملی پوش 100 میلیون یورو میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25249" target="_blank">📅 01:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25248">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtapj0bRdVhPv0BJIzZXU64L6BUIgq5xeKUfoMXczaR7g4rgKTH2G2D7hbgOh9Bp0bS2o9fGfysNbB1jzLhwZFG8kAYO8bGk2ibntzbJxgxripiDrym1n7HDUZ6q4kJgMnqYK2obuRuzYbJHqyoV0mKxQrimMolk27RoXLFc_lCyKOp40XQ1crESNTN5eNV1KpqUyTmHNlJ_AjzwPHq2DP2B5sSGtpiH8eNwM9iDDB6MKAiAUeISxwNGcJ8s-k1DBJ-wqX9u3gMAL3Bxks1q08hN-PFC7pG9r6YEuPvc9tsuNQ-cBUTewRREujKVrC56Bij6NH4MjaoUv4EmPuM0Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امشب؛
آغاز مرحله حساس یک‌ چهارم نهایی بارویارویی‌مجدد فرانسه و مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/25248" target="_blank">📅 00:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25247">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4CYLX5sPacGqGHE9pnSQucLU8e62QuJU-R2PLiunpYnqCqbcsqFDS_IdUrPMaMFwNEfbRlwNoFxCL-dF2nZwwGUhANfrP6nLfXjmQLX2dYVirE5Y-3NWP9J6pEp5swHLO2LxLxyBm1kHZZkkUhe67z6NW4KlfkiGYTQP3TVVTe9YJZvy6r1dLtfSKRDqqPDzH-5476L8zcOV69Ztcb75T6BkPq9EDUSd8Mc23xCiisCBDMSjfdy4spSxv4i7l4RAeVr-4sFDM-mQciZQjAvtg1EqOg1w1u0wZpWAcS_coXw8GO3mPgYAuVFHM0JpT0-jE0V8qweGdNa_tm9aKR6dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عکس‌هایی‌که از وضعيت امشب بوشهر داره دست به دست میشه: یکی به این ترامپ احمق بگه هنوزجام‌جهانی‌تموم‌نشده دهنت سرویس.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/25247" target="_blank">📅 00:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25246">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfQzKaXYqoEELkyzlEsUu7g_zNYhYUSr4AuLJ7USQIl6wfaTrlqqqiXzgHKetkHVALv0NuDj-lRsQgmFyYnuv9LIjMJN3JJzVECSO6TRY8Lu4McFVUa1rHrhrwIMumBr1NWVid73CEDXgd9CGZAp_0F_u3WznNvyjNbGGiRkrc-tShUPlLYjbYuxM1B-i2rcrEnKJV4YBE8G3W1GhAKf7s3Vb8Dbq-QlCEa2wcvhhD-dgAlaCTFE9asmAMoI25Ui8330b--yRoT7YXIVrHrN2UfiKOXWqZQrk_RfrIXrTDdwCPR6eV524Lc8ANBp258fvKnRxoacQxACXDGZe6exTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه دهوک عراق بعداز جذب سینا اسدبیگی؛ حالا محمدرضا سلیمانی مهاجم فصل گذشته فولاد خوزستان هم با قراردادی دو ساله جذب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/25246" target="_blank">📅 00:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25245">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOtk6EwEZxlPHD6sxbKuVcq8PLrzdPx_YJG0PwQ3H3WhtE52iV6i0zD9nPPp6n46-fI1u3N3p6KhzpAG7H7FpfvfMbUsrs7-twyay9MMfprH8hcP8QTyoJKdrxdHy-OxFHPDD4vvWrj_EEWdKUeSjmLSP-dcCNRh9TLVEpRY9L6TN5DQVl2MwwIazQkcDLufAAuii69r8mEaihnZm5aC3P4uZSTmInZgjPyoqQVXWIeBJNeLYkcezOwVIjeaNxrnfOMqzsssiTNecW0o4xFoWYre10UopQSG0m850kl6tgolwrKLL0tKJ9-ftNJJAm_VTm9M0YDcawKcKYdhh7osvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اگه نیمار جونیور روهم به عکس اضافه کنیم؛ چهار نفرازکسایی‌که فوتبال روبشدت برامون قشنگ تر کردن. کسایی که روزای قشنگی واسمون ساختن. کسایی‌که اسطورمون‌بودن رفتند، اونم برای همیشه؛ آقای‌مسی لطفاشما تا ته این مسیرو برو. بارها گفتیم که‌هم‌مسی‌هم رونالدو بشدت برامون…</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/25245" target="_blank">📅 23:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25244">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqYf0a0EBgPrCrDzlfX28KzD3WAzxiGbM3ptqOLKvv641txXSujzBj_uZDkaDlK7f2dPyqLl6EpzZNHnKvw8valVyw_xD9wETNlZrcjC2MuLtfndAAhXQGq2eV-6jwffch5s3qe5Z-ktjPLaTPaKXBOyuO62Vwyq92CzYQJhokkjyyhUEYE92AHGCokBJ_6rA0YpkY28WHcYQgkoDSsZIkT6PvFb2creNVuqipYnivCcBK1XvvYyMchyPnJUqhdL7FZ3BjJ-m62tfZ8uDxjdZdTyZDgGPlgdbR7z-1jERrcryHI6i-XCluqtTvTpZMWYjM9u_cH3bSfJYxyM64kN9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌برای‌جذب‌قطعی‌سامان تورانیان مدافع راست آبی‌ها به باشگاه استقلال نامه زده. با توجه به اینکه‌باشگاه‌استقلال‌تمایل به‌جذب امید نورافکن داره و مذاکرات‌مثبتی با او نیزصورت‌گرفته درصورت باز شدن‌پنجره آبی ها این معاوضه…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/25244" target="_blank">📅 23:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25243">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxJbr_kmXfXKHveYupcH-Fd3iXmz14-NG1n5Jb3i5IWFxUmKtXLiyFICIV2QHynkDYewwYPKRjUOsF1FJneftNPQy3hLdwbycqkWhIMryNiSi2DXhSrtn9qocoKvpWEwqCN3JpjPoG_kwMdnKxxwmm4kaBwfWbgS6Yipf75pzrYScAye2VEms-wFMYoI8uffNW5IHguHlt93Jm0028DohsrKVgmIKx6teUuSTlsR0LFYB3fnLzMyuy7W0klOvWvXEyU_Kzw89Pjdksb6EIrjgcVgq_XRrFdfA4ux63wFIHYQcBOc1P7m2IuD3PybXh-SWRVFhMEjcn4hfjEzVkEwcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
تصویری دیدنی از لئو مسی هنگام زدن کرنر دربازی شب‌گذشته آرژانتین مقابل مصر؛ آلبی سلسته شب گذشته با جادوی اعجوبه آرژانتینی خود سه بر دو از سد یاران محمد صلاح در مصر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/25243" target="_blank">📅 22:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25241">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hoxXENEXTseBk97EwdpHB7VCbQYS6SS5OYsAjIODlGrYRx6tfvvEFpFw6jA6b01aIEZmgHaGq2n5bPA1w4VeodM5Y3o5BnGi3Y213XfNU06KDxh5Vt9kS8lJ6ba-uIChwxV5Ik9g2c0493tdUQo_ShEyYLkoRtBGu04U5pKACL-xzW6Z1A6gfyWO9vGOwtFy-fH47A5grnE7wu97SVLr215kDSu1fZEOuYrNaRCjT3304ZqhXA2CR23GmRmr6KXMJjklo1nxJe9SXQ_39J0-bzgrpksBQhyd2Bc90eJhAxbKdRi0-6HkVpJHert-RtVvPZp6UUg460dYr8XMSfEUIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pzcIvuDtrQ_grKF_nkZ7O7uzRQ_q_1qYPdfyYJgzPVch3nVA4mqV7F5ram_ayLSKatgVkevUjtkHRve5QJYdZzYm0XiVH7CbAqlig8jH6w1n31RE_GJz5Q_JmjRlMVTtDsZ41tkvg3crQUU0MQNQmEtfdxdMGXrhMICI2gsje82mzupz8RKo5zlUYnqSrWbqAQ-JFBdlR-vntcvEshla4l72-zj4GNVxpeMjO9TiQhob_5vRRTvGcfhsJQW-KjsPqQAJ-Nn43iVPWzvTtjUA_TzYXoHtfhwXZ2Ata7_kqB7b4TYZN54FnqlPYQttYeVobzE_ya6nZuAkWCstLdWuzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🤩
مجری شبکه رسمی باشگاه رئال مادرید که مدعیه‌کار انتقال انزو فرناندز به این‌تیم تموم شده و بلافاصله بعدازاتمام‌جام‌جهانی2026 انزو کهکشانی میشود. گفته با انزو در ارتباطه و انزو گفته به زودی به رئال مادرید خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25241" target="_blank">📅 22:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25240">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d23ff97317.mp4?token=ln5Cmqb0TepPxKMjgCgmleHDvMb2vP0VsxgpSWMReLpfGCQIEYTjTgHaf6ynWpeQZK7gP_fOU0K7HYwDMLdrci3kv8C1LqxQw4CW7l6g4Td8wZfZRxNNqYVFQ6bUOXlc_PkNtbAHO77Kl7lFkUPbLA0NmUa_dkONF2cK69h8_FZcfnA2dkf6JelcHxLTq2KBoSccT7ne-xCXjdVDp8T2fvPnRAOpA5RRZDnT5eImsqXkMEFCxclusozEKA1VraJriG5H4kTDWYws1X9AY810yM_xL1btP1HDWnjadMc_zHHD1aic8_0YsJspeo16sDc5zaP7IpagyibFq_VP5AJtVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d23ff97317.mp4?token=ln5Cmqb0TepPxKMjgCgmleHDvMb2vP0VsxgpSWMReLpfGCQIEYTjTgHaf6ynWpeQZK7gP_fOU0K7HYwDMLdrci3kv8C1LqxQw4CW7l6g4Td8wZfZRxNNqYVFQ6bUOXlc_PkNtbAHO77Kl7lFkUPbLA0NmUa_dkONF2cK69h8_FZcfnA2dkf6JelcHxLTq2KBoSccT7ne-xCXjdVDp8T2fvPnRAOpA5RRZDnT5eImsqXkMEFCxclusozEKA1VraJriG5H4kTDWYws1X9AY810yM_xL1btP1HDWnjadMc_zHHD1aic8_0YsJspeo16sDc5zaP7IpagyibFq_VP5AJtVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
امیر قلعه نویی سرمربی تیم ایران: کاش قدرتی داشتم که بعداز گل شجاع زمان رو متوقف میکردم تا شادی واسه همیشه رو صورت مردم ایران بمونه. باور کنید این تیم شایسته به مرحله حذفی صعود بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/25240" target="_blank">📅 22:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25239">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUMcRkpypbT70S2SlxfZ8HicdHW9cZURC6fihj1R_v7cAA7cvIujlW_0geO8n9zssI3ICs5_p2SljG-QKpRyzWrkmpJJ8Q1yH9UA9ioRC2h8asK4jOEAnus7Q6_JEAnEYXZ2Jrmu808R8Y2HDup4C2fkjUbw9B0OWup-tbvpAuJY-3WWfCJyjn6YYVP8H9PhpWINkMt8NupQEriRRweZCNx0fmkuHyL3tq8VvABDVZjMBldL2ZA_s9F3flhKNVwKPMbhSqHHPM3FeDKgezM3ukD09u8_HbZGw9mOvLryi2l9P8MtzmTo0ohQQdjHuM0RWnbUatixHiO2H6Kqr_0QhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25239" target="_blank">📅 22:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25237">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWiBmyxJ6j9-krt5CdqaBC4X-XarSG6ukzmfCd46Dnw05KwYUvyLAgQ6YgiqTEOYfZU2x8VB2QaV74-1k3ep7OrYvQww7x-_vRhpLmgXa-6mMd4lAV7Y5cK4TOz99cbNoJ-u8-sS5JHNKbHJRSt8RpyqJup9Fo3QPEDbQAFi9ELtZ5_PHw1oQzP2x0-E7FXUhylivl3K1EWKOcjMUEHc9iARc35kLd7qXkL9x_2vvIWKEMQk-KUwjTtGJpLbGtsSv3DzoyXw5GxNYijG6QoKRqJ2PMuePnoBDGhS66ioZnTn-2Jwi7E2QVnpqd-skATALLbTjj1-gSTFV0RYtMO5wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ورزشکارانیکه درحمایت‌از مردم از تیم ملی کناره‌ گیری کردند: یخچالی‌بسکتبال، محمد امینی بسکتبال، زهرا علی زاده فوتبال، موسی اسماعیل‌پور فیتنس و محمدرضا اورعی هندبال؛ بزودی شاهد خداحافظی جندین ستاره تیم ملی فوتبال نیز خواهیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25237" target="_blank">📅 21:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25236">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Evhdt-MnPzFbMrw-LsicyUTh4ebV9la4X39UN2bykoVIhwIpvP9Fpaixd1ZbkbOGzwJ7dc_e_i9O0IRWVIoh2QUSo6WdAlym16W2fKm7TyAdHXI0P_X3EJmQWmV5-KoLfNCxdW_E_OGVk7xd8NQJTXHg8DY-H3AWtHfMZbhXkb-WNFO0P03-gu-tYkqfqIVSmj4i3E-BEeZ6u-QkeQuZ4-byV0UEqHEAqT0jtwYeZe5W_eSFpP4BS8VbHPzaH-RPWXzdKDrQYg7wUA1FSwRl1HwePz7vP7zBDwu6f3sxXaCI29KqSufYQcroWm7taPAFD1lxtM5Xs6W0sq_UT1Eweg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🟡
بااعلام مدیریت باشگاه سپاهان؛ گابریل پین دستیار ایتالیایی محرم نویدکیو از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/25236" target="_blank">📅 21:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25235">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_eF9NJinNiShVa6Bk31qBM9AHo6tesrPBpe0NeLbt94aJ2lwQ4Vs73ME9lelVS1y9o-aQjpcvszUfyVA75djQdJgmvr31JaLmnZtG5MAQVefTldLamU_qkaZgl7vJ2kU7a0688YWqdwQyT470sTpixjIAml4BAa1XGcmtwIKOkhGam3RIDCMsozS-XT-B4rWuuyeJXynk-9FgZLveIlbEAzxN7RCLZPzQ4jJ0NgWb4GJZiQtqpOGwGgJv-6CuBjaRpEwnAO5BP0O7Vy-GQKtBZEMuHm6Q-bbgbn5zNC72LafbLfIC6uVyZ5_XLLCbydRjjtyj6q4xxdDuRtrVBwrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌پرشیانا؛ مدیریت پرسپولیس پیش از انتخاب مهدی تارتار بعنوان سرمربی خود؛ با ایجنت هادی‌حبیبی‌نژاد مذاکرات‌مثبتی داشت و حالا درصورتیکه‌تارتار تاییدکنه هادی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25235" target="_blank">📅 21:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25234">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxhYfkY0-ok-DVkihTvKW4QR9z0GqTxZfvQEjCmVAWVLkc7CxhEMz3_wJx-KNaxWS1zLZ0JNC7gOzXtAJMvCrUGK2Kc8F6v_4ZBXeWhPKB4-EFyl2jD1W6EsFrocQ71LgFdeGoRyMDDu1rEIMqy7w_nu3nwLUxzlL8UPjduQOQAusnlFcYaHaN_PnRXpNfJfrAimrVcxPNErGgm-WiTv7EgYRK7b8J47JnnSJ4yQBGVF-0mk1QXUSLVOMjwhJdmO9J6hJOQb5kn7kU-keda1zdfDsV1tFDptav9RSpHMDkWF2dj54ZTiF7PiT1X3hyObYB8BOADkpBDLVHdv3h805Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امیر قلعه نویی سرمربی تیم ایران:
کاش قدرتی داشتم که بعداز گل شجاع زمان رو متوقف میکردم تا شادی واسه همیشه رو صورت مردم ایران بمونه. باور کنید این تیم شایسته به مرحله حذفی صعود بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/25234" target="_blank">📅 21:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25233">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zh2_EUiyp-wXnkNxWvVaDWKZ7mdpGHQE4Kutzv_jKn_A-5zXF1Z8lhYeltEiWPEeKJk-Vs_-t6YUeJ1ySlGLhnUjeKS62KLssVQw6TwXKso-JP6uBj02lKL8haOOkfJTtbWM6tJVC9QIylPBVqi_t_oItErk5NI1QKT-Z0H0ZWa9zvz2S-qAtnsKfdBw6jgzHAk8jDarJsTbjUwdIyInwIS_VFYyHyNYRLqkEc6kdSWbYdN5Kqb5MJEukZthZ0yD9Zyj8WasF6yho4Uvh5duZsNkw9al_7ytC7lQhAVUBBLMz6Cx9xHLMK1pNqqQkdY-F8v8eOkt0uiAAyNKfT5Nfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
غلامرضا ثابت ایمانی هافبک‌میانی‌سابق ملوان با عقد قراردادی سه ساله رسما به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25233" target="_blank">📅 20:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25232">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reiwjX_BLT8Lyn_UjcWoZfbkZ9TiV430PQxdyl8xjWQOWh1D6WleauzwhMGuYL2ti8692fzIRn4vDD5IsQcxVT9L_W-ivUxSVE95MgTuYMOPD5F6m5Qz3aEVajYDq0n3yRseTK968wuRHmCokgOfb4HtPvl0ARdMCOJ5ftQYfAekxgiIt81h3ZcG-VZo5T6dCXdvB3qKM5qNdFJwTqJZWME8_TorSXl5MY99YF9lUX_BU4l6qoPEQWZLsyys8OqSy6TqLIto-0Mk5qWf9zKjGfy31u7RgpyPqoGX0QVLJ2Dv32ezl112TWpYqiTPzOcuf7iFiYl9owOI83jWOUpRYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کنایه‌مربی‌مصربه‌مسی‌ولیگMLS؛ابراهیم حسن: فیفا میخواهد مسی توپ طلا را ببرد، در حالی که او درلیگی بازی میکندکه‌فقط 3 نفر آن را تماشا میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/25232" target="_blank">📅 20:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25231">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eck4bpbs3r6LXyy7y6hsykzlhIgTPXmmvmokTYCIFudJC-hhh6CPR2DOcolVMmgeGKnAHxgVBE4ntQO92x6FuKgfqBq6-KUlSfbXkZwPOF87cuwY2On4xoqd0gjVMiTRckpL0leYhN1uHMfIIbqoCAjuX-ojkzyO8lPXTt4osGG0tuLO8vEtxBdxutcxY5S1xFwvooCVSCdgDO8WkvzDow5M20vN4jnw0hRqPlBwsPXDCJwksnA-JCqhEcyY9WidR0frkUbusfFLTAAw16MFaMsbFouelU_Tp-0Q7oYpzMLsTXiLqJLQUk6zCuiKI0l2mCKNdvQCtvSX1Yj15Om6iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇦🇷
یکی‌اینطوری هم‌تیمیاش خوشحالن براش و بهس احترام میزارند. یکی‌بعدبازی از تیم رقیب میاد دلداری‌بده‌بهش. خلاصه که یارخوب تمام ماجراست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/25231" target="_blank">📅 20:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25230">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNlti25d3a7yUtBqeLWMkS_9EBr5a65y_dxhNAWz0Z-NjdGvd7fCH6TRTSOfpeK6qF9YcFmJOGNiPKsHoIm0eCTJbnqFHZZStaTJOgjIWut0ugBgVUBcsIrulXvJl-Tg93AemRZ5rHxDikyUOIvH5ftszOE95RFoPUCRe2fAFEtiArZXt5-cgdK3BpUKOhPIh-dus3pz3JysNwTWvPcd_2Vt-B65RyHQRdM360FZHrzhFdK_hAgK5eQoYhLX5mcrx_F-rjF-3J_NWMI94VuX3Xccsyjatd0lflj_UOa_JqfwA3qyb4beG3vsDGJTJq-loRM0n8NGX5vCqXuU9HYyVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/25230" target="_blank">📅 19:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25229">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAWPEKS607fLy_GQHDbqMpEj2KYOSNiy4uUVEyNUVHajbyqUKlrIdmVrJvo1psjFPuS5ogtQmH_iAWiLed6SzPSKhqvJ6if3P_W78byN2TQCTY9COVS8u9FlbB4xKyTWgu2GVSDgL9vLRi7eyxFC1KyVDwtTqPgW6gyC7sg5WeUQyoBo4NNsDQHaTQtrIEUxtF03-UySq0y-Xjuh9NwKpZLm2cUkb704B6hACrTAn52tCkME0XG5udefi79mLkpTJOUeY5W-UBiOrAAoEFq9C7RUveyrnWkko08_xxQ3sFyfmb9mmZ0TkFYumutN2sCoAPXL5Sk-Sf5QPm3F7KskBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7acbde92f2.mp4?token=Lzhpm6PaB474HKcvEj1jFR7OXpnKSg-yFOI9X1vZ8zbhwPGFoGRwFr_b9Xa-G0RwXghmQ-ECAYEGBR3Cj7lC2HRjsK5xGsqjZS4lZrRHVySQOoDEE85nj5XGpY6u2Ye7UetLmRgIQcZ06HqgIznOJxkwmVACrQTjpnXxztmRBLS2gIPQEER2NnTmC4mKTSw8piZRzsWBD4ID7Yp4iIuLTtByRctq_cGFUTW0zrD9Ix_6mEpv9iBckSAHmIGvz4UkZGicDtXXSQNKwZgM78yZNtHP4yy1yW1dUzDym0snJDJIXIUa1F2-MjwlHUwL3tDopATgyc-K5hYFbpXBgqSysg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7acbde92f2.mp4?token=Lzhpm6PaB474HKcvEj1jFR7OXpnKSg-yFOI9X1vZ8zbhwPGFoGRwFr_b9Xa-G0RwXghmQ-ECAYEGBR3Cj7lC2HRjsK5xGsqjZS4lZrRHVySQOoDEE85nj5XGpY6u2Ye7UetLmRgIQcZ06HqgIznOJxkwmVACrQTjpnXxztmRBLS2gIPQEER2NnTmC4mKTSw8piZRzsWBD4ID7Yp4iIuLTtByRctq_cGFUTW0zrD9Ix_6mEpv9iBckSAHmIGvz4UkZGicDtXXSQNKwZgM78yZNtHP4yy1yW1dUzDym0snJDJIXIUa1F2-MjwlHUwL3tDopATgyc-K5hYFbpXBgqSysg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsQkvkBNiVi5nzkDtsGX0SVwq1XDdImgQK40lWVekgZrzizk6KTkcnPybR_gYaS0peqWyeNRbOaVjw4aH9ljhtL6UrSEKgAurEX5I8is6kIr4K31WhwJhDmvIuD6KftukuHZirooc9rzp6068vS6OWcIkDF5Dh-0a9GBHTyNiiTY2J1Q0RAUQsM-8DGtJW1Ij0OK1m_XeBSs8ne-qIzHj1fV_q1-L4hq1u7TN96dneyroSoP2nQtfmQN_GjgSuP_N6ixH02TKbHAB21mbwUOLW5F4muexEi3gBrdhWv2eWGXqubmWyepTyuvl3cS01AHovs5hf5byyYtAJcPy-4msw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
تو این عکس لیونل مسی با نصفه بالایی صورتش داره گریه میکنه بانصفه‌پایینی داره میخنده، آلپاچینو نسخه عمودی‌این‌عکسوداره؛ لیونل مسی بعد از بازی: من گریه کردم، چون احساس کردم که هم تیمی‌هامو بخاطر پنالتی که خراب کردم ناامید کردم. اما خداوند برام سوپرایز داشت.…</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/25227" target="_blank">📅 18:21 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
