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
<img src="https://cdn4.telesco.pe/file/JIQpRkqx9NoEyOi5Jl0u1L23smQd2f63yAJjQOI7E2VEAQlxNTBHbyTEAfO1_IqwReJGL1NMDUTkq1tMsllVgxZWCrXLglrNa-4cG9gN3A4H9OnlbGo1pIkcZTYbOMkELZmD_GUW0_yd6Tw2GpTfLJ18TvwOTo3H1J3ROlCEE7jY0CszWmQQHEHUTQcY3qDTNvJqgWPUpk6uqIY-0WtLSbYkpdMg3KQg6V9ACp3UWmS7Nt9RV7MNLHdqsdL1kdXnEeKlkIU2qOWA30MwM_fBlzokPHDaWpPz2inAolF060B_SqzudOn5XJRIxsEH8NNLBzBxmUiKzYtZvyqu_DdNUA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 365K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 11:38:00</div>
<hr>

<div class="tg-post" id="msg-24922">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tM7CrLGjOfpd19CX-8TVKFDD1GGK3gb7MbwJ35qK_uTk9D7iAaMChZnddae2eqmbsOggjoD0bXcTOxZHdRqWS_jO9nXR5uWemacT00ntWTQftF5zZYQL2N3q5HGbR4PqKxqkcsFYHEBlmrTOZtvwU3SJxaSKFBAqJSj86QUr0WneUYjTDXzPtNlhcUAGfW1istM0gIM6rGs7BEeAKYnesk4CjhLYXi9UDHNB-3a7eSzXFfIynmTdlJMeeuIUIufM1wPgR3QJUIvFTj4lmVD1SOPaS_ZvNz4s196YSL-UKNkGKQzuB-wmAFXqM64Cz4EovoiKzVH4bFwjPWMBMvsITg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل مسابقات مرحله یک شانزدهم نهایی جام جهانی؛ پیروزی سخت و نفس گیر یاران لیونل مسی مقابل کیپ ورد و صعود به یک هشتم نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/persiana_Soccer/24922" target="_blank">📅 11:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24921">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STt2HdsJaZBdenhhPRLfcQKnP1ieiNQ-ROtwxg8JTXBlaxrJNHzheOaX3tx5YgsPwk2YXhQivsJNd4hA0zlPhogweYwUsLA-dC7zt2kx_SD6i9IT5lS5bNB-IGJ5iO1xhtXelNAbw7SevHUFpAWuUJ3z2HCOl77iaZrlAWBtKQ1xUrwvj-7pZOkrgGGrPNaLTGxl4ABRCIhs6Pktq7r_VBq8UMdVmXwCFM7nRSKyn5JbYalYsJLBoiZFEwSOAGnWR5R8hWZ1WkvKP6iQWtPOEy-_nTy6wazcCQW-lkxsdmXu3v2TCsSnSI3aWIkZT4WTTbmzrF27cXNpQeYvCOACeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
طبق شنیده‌های رسانه پرشیانا؛ آلومینیوم رضایت نامه محمد خلیفه رو به 70 میلیارد تومان کاهش داده اما باشگاه استقلال قصد داره با 55 میلیارد تومان این دروازه‌بان جوان رو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/persiana_Soccer/24921" target="_blank">📅 10:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24920">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWBRyahzwuLZ5PhJcikjtkfXs0lmicLLgz5-DsCxeo3iw-kRpkM3O_dQYTpxdGtuZJYKaTFNY1yjeTliBhpt13Kj1y8Mx31L8Z_GGv4oqhoYH1z2QjRPdzwcTOQ2px3MrvGqDyFnCu8rJ5qs81bnm5ot2yCs5dMDx0VSJ_feXj2ykIt1jFw44QoE-Lija1lB5VJxVmKCjJ5w-p6qPoXdPhDpVdZUkF2lR-qP6aIGV48FPS8ZePOy00yFpYybtoo2rBndCEGvCS-uoz4aWBRKGvALRVaUgD_BZ_OI37DZBdmPpn2D8QX5tQX1L2jCunfihD_Qr8YH21BtvIyNs-CYcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/24920" target="_blank">📅 10:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24918">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RITVlhu0cuuiRVMTwrB581tu6bsdOIM4wQXp2q3nusAg9qQT6t1PKKZfoJ3beuyuCnwCd4G-_1Xg1oYyfzssW-aqMkApw972lkYHn8Axsq6v3xSPK8yUxMqbXNW-MH0QbiE7Mv-Co7IB8IqjjU3mIKA2iCUixgj9BseUmF7iV_-XSpYTC3-dFXFCRvMomWc_Ze0-5oa3BcyAxUo3649zwM9u2cDvwPXja-aDlkGwQAhUqPy522pxbPIU52StWXQxyXoO5T1hk9-4NU4aXYSHhGJ5WKbaWEp1pFa3VooZBNvfkrzPjl7I8iCBkDhFEIQNP8gXZeFkuXkM-1Tm-pYtPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
8 سیو دیدنی وزینیا گلر کیپ ورد در بازی مقابل آرژانتین؛ پبجش از 18 میلیون به 20 میلیون رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/24918" target="_blank">📅 09:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24917">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef17610d75.mp4?token=QxL8UVnxM9-CJZZxQ-hT5rEsdqMaFMVaQBpBCHw8D9cNwRbYrPm1959gPx2Ht0U3SCVnuCQ1ss8FZR_mKwNdt4W1LrEu_-ZFCsPj-n8PX1w-KArOeHRYQy6z0Wdd6WFPvsx51NG3WZ--izA27AFzWPP-FmM1NsU3fRwmUe5pyZ26i__O8OPZs8ZWBXNFGOVrF0z0epC5sESxYcP5V_UQEH0KW9SLGyZ_6yDtxIJGggbgpdUKAFpzcDTCLHjm9V14hmMJhqM17-ijFhBlWZHCEsTCl_Xqydq2Oaov_Zut6Dt88QRbqGsfRgc93AuUTalecpCNBvmIjYCLT7jS0qSYZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef17610d75.mp4?token=QxL8UVnxM9-CJZZxQ-hT5rEsdqMaFMVaQBpBCHw8D9cNwRbYrPm1959gPx2Ht0U3SCVnuCQ1ss8FZR_mKwNdt4W1LrEu_-ZFCsPj-n8PX1w-KArOeHRYQy6z0Wdd6WFPvsx51NG3WZ--izA27AFzWPP-FmM1NsU3fRwmUe5pyZ26i__O8OPZs8ZWBXNFGOVrF0z0epC5sESxYcP5V_UQEH0KW9SLGyZ_6yDtxIJGggbgpdUKAFpzcDTCLHjm9V14hmMJhqM17-ijFhBlWZHCEsTCl_Xqydq2Oaov_Zut6Dt88QRbqGsfRgc93AuUTalecpCNBvmIjYCLT7jS0qSYZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/24917" target="_blank">📅 09:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24916">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3NZRm5eyRslINHkopFek0rx9W8nRLzJN7S79rtiMHOSP_S_UgsmNV73AAqr1rc8_bcCK8FvUPoJhGz5Chp9CqxLS3Cfi31JUMS4MJFwYPl0_38pwbrGoMK4n6eJWOfplx72C7n98E6cPUnbC-_D0PRujDNV9eNv0C8dd2it13Kb8gJJQa9GrXX62X_zkr5wwWf0-BnE5rPk6JSUXI7wSRtqNdYBcViUsxw60ztScLU28zCpIfT_0UQEgXESmx53R5RMj7fd1nzkmkKYVVl79ELdXxYDLjud_DW2pTrH-mOHtCimX0SqQWT_GaNNQ-MAWrKEt4AShLw-bektTIfptQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مسابقات ⅛ نهایی جام جهانی مشخص شدند؛ لیونل مسی و یارانش به صلاح خوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/24916" target="_blank">📅 09:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24915">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9IcGTPkLsrQfHu-FcXc8EJVeVDnRvzLvYRk73cw_oKistLNV_WgE8F0dEZg5NBOXX5VdLYAONARIL9fax_pPZp24XFSWLhsbSPeNwXwI-slhmbz_kdTsDf10ymkAjhMujW8uGrIwvMpYNKK3k6Z2qCmV7BYl0D0bEu5r8T4J4yN9OabScir7kcuL2DghqiECdTH2M64CmT6sFzxZMWJw7GyxLczsE3cLER3eIVGWsbdvHyLD57P4dZ64rdG_MTicb4OxDmkpYZA9K19v4xDwHIN4LbjEwFr6MIkqbndtniJYVODMoW3KZagxZStJFg-HE9Swlww6-VU5EBW7NnBbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ کارلوس کی‌ روش در بخش دیگه‌ ای که از مصاحبه‌ اش به تعریف و تمجید از مردم ایران پرداخته و گفته من حدود 12 سال اونجا بودم. اگه روزی ازباشگاه‌های‌ایران‌پیشنهاد رسمی‌ دریافت‌ کنم ممکن است به‌آن‌پاسخ‌مثبت بدهم. من برنامه‌ای برای بازنشستگی ندارم و علاقه…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/24915" target="_blank">📅 09:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24914">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/579197cdd6.mp4?token=Qa7-pBrMB0NcXbcQDBwGBrKkVNsXW9S7rUamf_v3ba95kjxpeEKm3xsSpbhVnTczSv7QsylRFcu77mqmNRGjvfDSr7zwSCQxaOtro336NBq40e9QuX5YPv8BodkynzcPTeEizGOwebtkP0CguqxM1SCcxUjFTKA0uKfAAK3f5mvcvzd9x18yClmLLjvagVFOsfz7sfZNenWBILtGjDAuqatLwtGLBD_juNgkkEI_nOk5sS9VJeJhJxc3U2lR6mUIDANbWlQB2ZyFnRAldy4vez1DelTMnmCcLPe0gyp_3TlieEWkngTL1diCKDgmpcqCt0FTTo2jwwdFf6lpYHSz3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/579197cdd6.mp4?token=Qa7-pBrMB0NcXbcQDBwGBrKkVNsXW9S7rUamf_v3ba95kjxpeEKm3xsSpbhVnTczSv7QsylRFcu77mqmNRGjvfDSr7zwSCQxaOtro336NBq40e9QuX5YPv8BodkynzcPTeEizGOwebtkP0CguqxM1SCcxUjFTKA0uKfAAK3f5mvcvzd9x18yClmLLjvagVFOsfz7sfZNenWBILtGjDAuqatLwtGLBD_juNgkkEI_nOk5sS9VJeJhJxc3U2lR6mUIDANbWlQB2ZyFnRAldy4vez1DelTMnmCcLPe0gyp_3TlieEWkngTL1diCKDgmpcqCt0FTTo2jwwdFf6lpYHSz3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌سنگین‌وداغ هادی‌حجازی‌فر سوپر استار سینما و تلویزیون به میثاقی مجری صداوسیما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/persiana_Soccer/24914" target="_blank">📅 08:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24913">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34a4a83cf.mp4?token=oliUuWK0lCX5I-DzFMJMggt4ISJGAXnnoJwX0LTa3TeG0F8Cpo8NMFYTG5NBMjxOiwDP4GIMBwtjV6Z762ZxIcU8vRElaX-fu_bldUeSqY9JMEcrKs9IKOhDvKig9a03fJ-dLyiWRQqfNF2phRCKkP0pLjoUeq1bCwZvZ5p1dlUYEnkPKqrhiekLUlaRZbHuqP-NK2h_YgiWgk5vscLb4wtEfB7fPCjjcyxUGoGboAOsdZZt6fGMBaG9m2pEi4FjsGuMtStKoO_d15nQJ5uZWHXW3LOA53MnE7X-ScLVKAPIP4BXHdRcHxgFN1nhxcG1WMk5SV3KRhuf3_vcRnKnZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34a4a83cf.mp4?token=oliUuWK0lCX5I-DzFMJMggt4ISJGAXnnoJwX0LTa3TeG0F8Cpo8NMFYTG5NBMjxOiwDP4GIMBwtjV6Z762ZxIcU8vRElaX-fu_bldUeSqY9JMEcrKs9IKOhDvKig9a03fJ-dLyiWRQqfNF2phRCKkP0pLjoUeq1bCwZvZ5p1dlUYEnkPKqrhiekLUlaRZbHuqP-NK2h_YgiWgk5vscLb4wtEfB7fPCjjcyxUGoGboAOsdZZt6fGMBaG9m2pEi4FjsGuMtStKoO_d15nQJ5uZWHXW3LOA53MnE7X-ScLVKAPIP4BXHdRcHxgFN1nhxcG1WMk5SV3KRhuf3_vcRnKnZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل‌های‌دیداردیدنی‌بامداد امروز دوتیم آرژانتین - کیپ ورد درجام‌جهانی؛درسته‌حرفای جادوگر درست درنیومد ولی‌کیپ‌ورد 120 دقیقه بدجور این تیم رو اذیت کردند تصورهمه قبل بازی این بود که آرژانتین همون 90 دقیقه کار حریف رو با 3 4 گل تموم کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/24913" target="_blank">📅 08:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24912">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
👤
خداداد عزیزی: بااسکوچیچ تفاهمنامه امضا کردند اما به یک باره همه چیز عوض شد و مدیران باشگاه پرسپولیس‌درخواست‌های جدیدی داشتند که درنهایت اسکوچیچ اعلام کرد با این شرایط نمی‌آیم.
‼️
دقیقا صبح گفتیم که باشگاه و بانک شهر بشدت دارند سنگ‌اندازی‌میتونن که اسکوچیچ…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/24912" target="_blank">📅 08:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24911">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLjllfsmuXfbcibNoi--GsrxTxLNpP9ioirNhlt_JV8JpBBvbHQr4WGbVzIEH9KhbOv_tOchEIblV9CNGqWI3KTvj_F_yLUHf1pg5sFGD0zpJSLBSwLx6UfVV4GhukRN1UPaxDiFjEbucj_-Z5n8GfpcG-1M9mSwWUw7ldEVS6P4e-jQMeqZEYWURN-tFxpd4TnvvzJJCaqJVYtK8Xg86c4WPWYE_Jyi8DG--t8XkA105Cxp1PrNEyQSl_WbM_jbj1uy5nxzveMFmoFkhPdPzk_7yXWWlewxZYUcdUC_ctLtr0-mTTwkeZtXNFPKXBKNf6TCxlsRXEGzhYaeY-e4zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دریک خواننده‌معروف‌کانادایی - آمریکا رفته پیش‌کریس‌رونالدو و بهش‌گفته‌روی‌قهرمانی این تیم در جام جهانی 5 میلیون یورو شرط بسته است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/24911" target="_blank">📅 07:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24909">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/24909" target="_blank">📅 07:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24908">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kj-qI4HKsGGxE-fA7yIEyrYqSpOCGWzMI7zYsrjJLFME_FPWRaVRepQrr6EBAptnAlCW9587T1_uTkAdsGItUOTQd7tS-o1zmQThOKVDbSCsBWAGTHmijX66Sh3wA-MH5fje_KAM7q36n-E6ASRR6jkj8zDViEZACOto2JZ0nivWVFmthPdUSfD3TVTVE8z_ErLf72pK8s2fgqH8GPTSyEZ35Ro_5FINHkC0JwQnoykl1RD0RoQElucZoHgo7xyLiWf2FbaQjoBE24WU1yICZN1tWfhCFsl9gyfYgxbARoMkwLRtzuVGXmPII0d1pUgmnOm6Jcl3r7t9MQv6pKrDZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل مسابقات مرحله یک شانزدهم نهایی جام جهانی؛ پیروزی سخت و نفس گیر یاران لیونل مسی مقابل کیپ ورد و صعود به یک هشتم نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/24908" target="_blank">📅 07:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24907">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GT5mubd8P7zF3mqZZZoRIKSxzoguTDfb3Y-dSxt9pmgAIzk3Xb7hRxSfuO7ZzHoEHaVkYYtJtQXc-gNwrhRLserWU1b5QR3nu8MzYJHvDKrIK3s3tviyWgTgLfCZ9FL5F3mPZLjiDGjz5HCPVxJ8IEyCWTGdtNPZGG272sidl7DMbKjyVepZOUZGLK2NRTdxgKwSeIIcwgARU9GIohh3U8QARkzScvUvRunQhgi9kat3FjGGWftS4CkgzEsqC3aAyBDv0pz-2vjg9x4KHzH1C3lRqa0FOcGG_inKn70GByx-4ddaUX9TLLEfqyZnNeGW4josBVGO_KqxrAhBsHEpow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/24907" target="_blank">📅 07:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24906">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmiVKSZd_Kf-a-DDbWxCXSMVeQYDxq_rsdTWR0TQPcK8Q8zTaOndnQ_YGg4W6VwlZASP5QmaEV3z183OinExzdBRsSYNh_sFjVTlbXVhU78w9pvs5p8u8YC72BRmsZix2QQwQfjnEZB7UYCn_AngxBSYPB7VLazTmH7Hv9NMowik_ZXKOY7BS-fCtVhIIzaFUZCpDrMExjJHU-xb7mNgtu29CQLwlJFlWGgnpolSUHdm_snSWejhAIGs7W_nE8OdWUf3PPtd5vZId7JWkXsLeq-i-Ng81YiEHeV0iqkUVc9ac-TsVrM3ZXsWmFzxAfPsvDxpcf85hTYkjGNfED2gRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی درگفتگو با ESPN گفته شک ندارم که آرژانتین باتموم‌ ستاره‌هاش مقابل کیپ ورد غافل‌گیرمیشه و خیلی‌زود از جام 2026 کنار میره!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/24906" target="_blank">📅 03:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24905">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXlMCQMZ3SS9P2bKTPwajWgxciKFgs1deA2POZVCvvNykoXQ1K2EoPINuhTDzJLKE_MBiZOPVrucAMom0x2onMp4VKcqUu9GNG51AR4RLjy3E57oEPc2yFoCAiMxBjrLqt94IVdLs6pAmO32gW7ZSVSBdFA_GZ7hxNOP3KZAUi7ew0gUI_8w7oUp5NSql689KPLEXlRnrljUlVYUuR2t-mFLy4Am6PNzzPMxXEAKW9m_sFUadDKFdlpbXzhkoaXTI40Z7LcUAB1xyN3CUotYTWrA_PnolaDs_J4SzccLfxSsiMIIFE8btJHf07vs9yKBqaHkKG7q7iF6jSAtV6zl7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
گلزنی‌لیونل‌مسی دربازی امشب آرژانتین
🆚
کیپ ورد در یک شانزدهم نهایی جام جهانی؛ این 20 امین گل لئو در تاریخ رقابت‌های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/24905" target="_blank">📅 02:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24904">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0965bbee9.mp4?token=Ufgi4GB9k4PjO2ohhy_4K72FFhE4ZfiBaMtTUatuEhQIn_BUdN6-SlRAx86q4-PhvBFRQP_syvEpA36sncAICpZz-vMKQLjBEegG7WxgjS2AqZskyoqIBPbIazpYdsmnK9CeD03AOX55sfiEqclU3sO4iVrKG9CG8SByC40RtPPY8rEvR8TQvX0RTv-LbroK7ICzF9h9mC6_BBfk2Wytfq7g_t7EEP7nboICXy6zW5O08aG1YJD33ODL7U8HshPoU5QV-yZ1-1-MyohOHbHIcC1LtHPV4kZhDpJ48EyJazmIiY1MbQD_ybupylK2G0yXNflLTK4AzfwP5LsgkYh4eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0965bbee9.mp4?token=Ufgi4GB9k4PjO2ohhy_4K72FFhE4ZfiBaMtTUatuEhQIn_BUdN6-SlRAx86q4-PhvBFRQP_syvEpA36sncAICpZz-vMKQLjBEegG7WxgjS2AqZskyoqIBPbIazpYdsmnK9CeD03AOX55sfiEqclU3sO4iVrKG9CG8SByC40RtPPY8rEvR8TQvX0RTv-LbroK7ICzF9h9mC6_BBfk2Wytfq7g_t7EEP7nboICXy6zW5O08aG1YJD33ODL7U8HshPoU5QV-yZ1-1-MyohOHbHIcC1LtHPV4kZhDpJ48EyJazmIiY1MbQD_ybupylK2G0yXNflLTK4AzfwP5LsgkYh4eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌ شانزدهم جام جهانی؛ شماتیک ترکیب دو تیم آرژانتین
🆚
کیپ ورد؛ ساعت 01:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/24904" target="_blank">📅 02:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24903">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBDsDFkUv-MEcmMZ_VzTas6SosvvyuxtIxp32VP0QIv-biCsq0pWXR9RW9RJWC5BP2WVFT7feLVB1CZwFTLaTvZX-XHdTkRMzegSSDiHLN09k4GO2ORt0G1c-yjEJk3clyyp5fzWo76qPrqGbpQxNodY42ZcL5QD4kYIQIBQkhPaJcQ-E9drSoYjj9A1_vIFW4i5OkJ3-T9wptZgR46srbya8i2PNpb-LL8KnpydY-N4fAV1yCsxZ0AibI35dvVoq1NZOYWGd7dv4Gz9i8XCmrmsk8fvGgoqvyJx_uWjEn43zYMFKoZzrRlruQQpSL8KV9E0HbFdlkoHJ-2GjwlWbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/24903" target="_blank">📅 01:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24901">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQ3m8EBCRxGPCPS_OV_Li5DZ96jrXENx9fSZIb7v1VrAk0DOxzoywRJWlmdHJe-NQVIYxqckDEHiriO4ImB1OzsngDclGuFJFVJg8Fkb7Jy34QTWXQMEAL2pwxxM-GohBMs115tOv8DWc1pSKkQk7dBgpsX3coeLwnfTuFdLzLnWg-RMEAaUX4QRnKPcc9JpsR1IXJxyMxsBc73WoAghu0bFXqGug2hv8KJ3CPJh_t8bxgVAPiWoaSbctFrSIQiW8jkZoSvAAwPhm2nd_K_oKYoJiS-AovFnm_pebempJP1Dnu8F2JJad6keNzk0ohIwBYNTSaUaF0cxQFieI18CyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/24901" target="_blank">📅 01:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24900">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUV4QWK8-GdRfRu2dzDVKXBX-4CpINwBBjWrgKFtVRbPTNTTJcdGmnLSjEgHa7WZhPOablTiey36HQB6Ns8rE9SS0LJtRFLHHMDyiKHHj_mHQJ9kYTg7DRSOj8Wr7n20HakWe5j_5YWUXhZDGqkZkdlWFCa4vmUxizbQPni3umksLzeKNn1hMSUG1RQZcyO_GBK9raXELbA5G4GQg0xSNlF7n2JpPtnN-Uv3pg30tZ7FcM3YabPaM-U4saFjeg9v5FNRQg3cHk51BBgmQQNC-LrLgU6Jo2dWRNuuE_fx0FxcZVfDfWeO8VLVNmoIxif8TSZD6rFqApjzfeHYD7BQKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت: کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/24900" target="_blank">📅 01:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24899">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5Hgf9fxLNhq0gF66M1clv5oN4ygh3PnPUj6fIHVRxr99ZHsi-O9XUmz6bkArDGVBaq6OlwP7_Brfqxo0_lSdPfFuXrwr5pgyuNSsAlKGZBKUud2DY176sM9xsxDWbEscG6JdlUywSePsuQWcscYyWp2XSJPb8Uae6a6-oTtPoC9Nn_8-WQvp_YI15uoReywQX3kVgbUYf09imd_YTQ_ieT4rE_ij1eLku2MH6z5bZ2dv-aCBkQnDMFIGoP__JMIOQN2hBkuo4Jl9iSz7pUOAvxwhjSjgBMh1mFNea-tMmkGmvrGfff-uMwosV_NeF5F3fv7JBcpErn2lB7nUomyxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌کامل دیدارها‌ی‌‌ امروز؛
جدال یاران لیونل مسی مقابل پدیده جام‌جهانی 2026 و بلافاصله آغاز بازی‌های حساس دور یک‌هشتم نهایی از امشب
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/24899" target="_blank">📅 01:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24898">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7XbEm1EMMQ08_opBMmiIEI-u27AnO88GTp6F7VhN7XAWF2ttqPa41KYomLUWDQEAs4XkVGDWp3HXVMwCLyAREdTDpSGevGlTMn7UrQHGG8AXhWP3Zal0HI6GhQBxfMVxz1VdyE9KftYMRvxeWC0pK47F7O3-kvtexiLnhyz6HAdsq3BvoIuULNcqF4h5_0Lq43XTnCzWcdycIRtDUuEz7HUMjEib9DgP7GBupTI4vHXB86vuxs9zN-jmP_pn3osUxYnct482NimCyqVxhK4_ZhnieKTvk_sGNx3vAKqVePnaujzmBdWpmP6n4SwkkfOOdUleps2P2GR_WSOCtPdog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از برد دراماتیک پرتغالی‌‌ها درجدال برابر کرواسی تا راهیابی یاران ژاکا و محمد صلاح به دور بعد رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/24898" target="_blank">📅 01:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24895">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktggsuQgkEiBQ-rJE9fUv5Kw_ZjsmNeujV1cZrRGdIh9_fTDSiBLcfTHD6Z0_WSZJkTBTWK4qqVcDNY2S1Ffh658naHXz8qV5-Vxca2WKGRasrKHwDzbB3WEDPA_skub7kLuD-nPlonCflSSDONa9dOpvgG49jSp22ooDuShE_OQKQ8jWAW46Xp68qaEOqF82pRM5uCC30ApW77lJ5lMCXPWcNULFYMiQIPf2DtuES79eBjaGCQ4iOn2Kz9NSYizNgrYYoyNNg_2Szq1p_DvMCcIHh0eD32j3OSWpdHCC_bIdhVwhNIraU4kaHYEsgzIYFYnZGUn8FyrChSqietp0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ دراگان اسکوچیچ حتی لیست ورودی و خروجی خود را آماده کرده و به نماینده و ایجنت ایرانی خود داده تا بلافاصله بعد از رونمایی بعنوان سرمربی فعالیت خود را در پرسپولیس اغاز کند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24895" target="_blank">📅 00:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24894">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c8ce51440.mp4?token=plX_JuxoxyDaHSe0MijBF37xbQ9YJkCbcktYlSieBkruu4scHajgpdhrReuwxF31EV5UnG0GvpIY7wt71tOmOO9UnChSEMHl2vuqzlapRj4Cj2Kg9_bssQHydd3z_1gzAqc4omEhCMlwSrZNtEUs8iCeeKR_WPhlGPeko3eV7ZazxahN6USuqKg7x9hzRi3SNHXXUGpu2wjKAE_htdz-2LIImpYoB97WNVyAAcHLgmNpNvUJGCdjbwUcuQXvJ6BpDTnuNxxmnWMUdbXlYG0_BKG4PxDNEvtSs9JTdBEbjoKl5FkTgOPT646F0jV9fNjUutvJFUniJUcyRFgNd_QuTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c8ce51440.mp4?token=plX_JuxoxyDaHSe0MijBF37xbQ9YJkCbcktYlSieBkruu4scHajgpdhrReuwxF31EV5UnG0GvpIY7wt71tOmOO9UnChSEMHl2vuqzlapRj4Cj2Kg9_bssQHydd3z_1gzAqc4omEhCMlwSrZNtEUs8iCeeKR_WPhlGPeko3eV7ZazxahN6USuqKg7x9hzRi3SNHXXUGpu2wjKAE_htdz-2LIImpYoB97WNVyAAcHLgmNpNvUJGCdjbwUcuQXvJ6BpDTnuNxxmnWMUdbXlYG0_BKG4PxDNEvtSs9JTdBEbjoKl5FkTgOPT646F0jV9fNjUutvJFUniJUcyRFgNd_QuTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تیم‌ملی مصر امشب با برتری سخت در ضربات پنالتی مقابل‌استرالیا؛
به‌یک‌هشتم نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24894" target="_blank">📅 00:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24892">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SxQ3FrKx2JJJivBogD1S4G8W7qYv4CwuY6A2IOt4TcLoYJa_Ut5eBtEBO3RxAhcgwYe7N8sr2-nHpQuS-lp3vBXGE9WLxJFB21-I5-CLA339BQzScYNu6lT9oaoL1Ha5OYP_dh2VKVztN_QtAN4_Yd6n2YJM4wZMomtcZe9ExcrSR8KA_0_vz8PtyZ1A5BtoS0DmFi8_5noROfI2hqstwEg2RJf0aaK-LJ9VXyO_b8AzR5H0EIe6r9pmXfAxFP_PUqvhaZgp3x_UCtpKXvIc6G66W_cfSeMXNkZ4KC3vDPFeeMp5g4RVAoMGS8Ugmci2BIYZMnFhdLadT09_BPygxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rIxl1cQP_yygWpZoM5XZ-z64Z2dqZKUWzCPD1MVQADkeezR4v_BuDOZ5BoyXy1YrRy4HqqXYqkCV3-MMgUGFspb1sxUabvHhiYfVTBTN58f78gnih406ipPQCCZpkI4wHirefmVqwnMMmGlP8jKa4zAWMMsGnvo_9r29G8rWQlhzWze4q5DCqJFzfkJfPRvBfXZXKLAOV6y5OF3MBj8tnQA2vjK4v4x48NPBiBmUcL-8GmLTN2wRQMp5pzF1fJp7vNbWELOKjFKsdYWHhWzgOj-1Gbocn2uretZVA-DlIhqHZE6ZGhUHMj309Gb-c2h-RagMqFj3cm-aV_8TifxqBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌ شانزدهم جام جهانی؛
شماتیک ترکیب دو تیم آرژانتین
🆚
کیپ ورد؛ ساعت 01:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/24892" target="_blank">📅 00:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24891">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2OZkRggAtQIXwnH1WaGccO6_G3AElwlq0Jf2zBzaxP0mBm9Q3ruAB2zyoNceM5IHkX67xx0snb9iJFpMXDFKbb1VPxOEcQUo7LyDZQTphJOmr7-TQnO2TJ5Ifg1nOCMVZFVCWwMHsl2hm3x5e6qhp4ms6SMy7skZ3qCnLJIGS4vWGuAuTc1sy6tGk6HyQTAWYGUttY9lR7ZcqCnUq8DrWIYuutsbcirZsYdQRHBowcrrvCZfRA_LXLK7qmVo8O3qCDXTW3ChH_g_RDGbhPQWyK8aUtzxqBjqpGCGImaPUTyVi4wbSigasTwntXeL-L81LL3AjyjLPmVeJ2GAU2LeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هواداد تیم اسپانیا در جام جهانی 2026؛ لاروخا در یک هشتم به مصاف یاران کریس رونالدو میره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24891" target="_blank">📅 00:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24890">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGaaE2O5eSUqc61cgNXsuyARlieWXVdUPfvKDETzhgebqZQzj2baLQTYe8gy1vCxWvEic56t64t_jRajmUR6xRnDzRV7AS-Rr0ofIlqaq-S44jtQqRlPJ_csw67IEM6eRnUg6dOXaYVKJh4tM0g01HSThD-K7HL0FxXqmnDAvBfzuvP0BLY__kO4SnLbgX4HPU3u2x9LgHXQldGOPyngOZgsdrsdQg72EA3EpFhAxN_9drEjv6Ba5rogeYgUkuiXAwmfKUkJWLrIuynDQUh8llqmG0c-t_W6M1nsbElpgkB2IDH9Z98T2pnSrkrB0n4WI2-pOI78qmpziG_HDireZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌استقلال بزودی خبر تمدید قرارداد علیرضا کوشکی بمدت سه فصل دیگر رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24890" target="_blank">📅 23:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24889">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsUElJ4kEmDTovOTQvhYxD41_rLQNv1wiGk_FKfWn59-urN8mi6mnHK7VnzkUHuu66hcbDvJMTpv13B-xOasbTzk19LrbQJ7KSGIIi7QnOxhqAhOL2EyiK0BIiCTj5jiqKQUPyUFdA69zdpwDEx9rNTUtCxs_EoIqarFlRFN0jweEmgSv9yflR8u4eW5DWmmdcIC1qU2BhfmPKoBjvIMBSU0VPlFMLojoWPhRqx14yFv4Azo7nJHxeneCY3cP4jIrAOWgEXwGEwT1mH4_nLgsAgu_J6cXtN45u5-rPXkrxxQerXBQUzOVKdBMeYcKKWXpmbFUeomPph18hJ9watvvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/24889" target="_blank">📅 23:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24888">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tO_8rJU3qwUeqycduwFJI1-4oF03sB1krJqGnDakoKHjIYf9OTNPAbaRbedzoo1YkUTls9Sy1SfWyqNhGXbAUEgkI3Mb_Cmblz73Nwnyd1CHgCB5l5Ov1kYI9boOOgA2BoXEs0fM6DdOWeOpc5twGJAfIrKdSgdlDY50Ey5MJkKHlSevXUvWRrmsP-wEdaaD0vQoY5ZyJdmY9_LYS5UWEMItH0y-VFmfj20CYfe2PaxwL8UDdfEzSqXGxOpRoeHFmEojU6dOAXDr99Ayby0Je80kxG3BBbsoeJ_hdaGATLQYqz5Gz_W_GwDNCnj2geWviE3A2D_lDhnOVpPaHyQ8Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور که در روزهای اخیر بارها گفتیم؛ دراگان اسکوچیچ سرمربی سابق تراکتور پیش نویس قرارداد خودرا باپرسپولیس‌امضا کرد اما اومدن او به ایران منوط به پیش پرداختی ازسوی بانک شهر است که بارها گفتیم یکی از اعضای هیات مدیره بانک شهر مخالف جذب اسکوچیچ بااون‌شروط…</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/24888" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24887">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r48c7rKX2P0D9KML4NLF4PeBd8Ykvxqkompp17-A5s9kmR2N4NM36RXFpaziQI4VU8AdCDaoG9tZT5gptKbpfZ3gETet51Vl8oY2F-VAQr07RYNT-av97h7t88q-1Xop2vLEbpoBQSrJnAgXMtXqHdI2aYtPcneaxd0-8LQ7V75vSBkABVQW7je-A__e_0HWlzn4fDlrjRBAToJH3koUx2JIIrCwj9fWqT2mc0z3PniJAmyYRGhMazc0mO29sRg9HLMID8Mz_csAMRNRUCQPrue4tUthc9X6PdIwU5FpWQ9lrtObKNRPgB5-y4z67Nh8-VbtgrBd9908UZuvbzQ9bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
تیم‌ملی‌اسپانیا بابرتری ارزشمند سه بر صفر اتریش رو شکست داد و به مرحله یک هشتم نهایی جام حذفی راه پید کرد؛ حریف بعدی لاروخا از بین یاران کریس رونالدو و یاران مودریچ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/24887" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24886">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHTwD5F0k3TC5lLObNGIGmLs4oF2SHrbBzmRkywxIsuw6Wq1_rESuGoUn-G46LWs8W2j-qZ_cqZNZDKE-ICrbA1OpTPpkTZmUDljX_UVFuqM0ghn0hPtDXohKg1ToC7GpeFDf097gUE0DWYckSw2eWZZJBZQKeyfKrQDvddzq77SX91Czib747bOrt5femvg3aHux3Tr8UWrq3JyJxBAbmVJhpOzvrryKHX7Qk24Z7tYPC6a51Zd5zK8btHYcqc8PDQHSdveh56jXXBAvCA9wr5vn8CCK-wIv-vcJ7xoNGx-YypTgMNi6Vy2_c6cTxh2h8-2qzKAoTNGS7N9kHKhIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیگه لازم نیست بین انتخاب‌های تصادفی یا تحلیل‌های زیاد سردرگم بشی…
🎖️
همه‌چیز برات به‌صورت پکیج‌های آماده با ریسک و سود متفاوت آماده شده.
🔝
فقط
پکیج مخصوص خودت
رو انتخاب کن و وارد همون بخش شو.
🏆
ویژه مسابقات جام جهانی فوتبال ۲۰۲۶ | ۱۲ تیر
⸻
🟢
CORE
📊
انتخاب‌های کم‌ریسک و مطمئن
🔗
ورود به پکیج:
https://betegram.com/share/betslip/ZKTRF62467
⸻
🟡
PRO
📊
پیش‌بینی‌های متعادل با سود بهتر
🔗
ورود به پکیج:
https://betegram.com/share/betslip/VGPXN72923
⸻
🔴
ELITE
📊
پیش‌بینی‌های ویژه با بیشترین پتانسیل سود
🔗
ورود به پکیج:
https://betegram.com/share/betslip/DACCB49184</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24886" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24885">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_-D9cQgTTkYv3kUsbiyAag7xF5uxj1ph2pU9D5seGWTqYM-6uO9y_B8rWPXb9lIjFElQyQU_RahdEJ34RW18V1HkuB-ooKLaoL55NASpfFEnYdiZyp6VHIN_LCl6fkww2ILO66UwoAujrWwwzYcrlB-eBAdqSg41ovtmD-X2WdgRFjLvMK-_x16SQF0gik5PUAbgX5TeEqtG_q4KNd8oUI41TGJBsGV0xil7aTYuDb40r24c8-yGntYZ_DHORK77UD-eetdwjH_2WzviOOdpM5QuFU9B2mqmrzk9fnd_aIQ1Oz7u-p2c5KDjONSGhh9Zz2bhGuhNEbgHQoKkT-wsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق آخرین اخبار دریافتی‌رسانه پرشیانا؛ وکیل ایتالیایی باشگاه استقلال عصرامروز با ارسال ایمیلی به باشگاه باردیگر اعلام کرده که ظرف دو هفته آینده پنجره آبی ها قطعاباز خواهد شد. وکیل آبی‌ها در این حد از بازشدن پنجره‌مطمئن‌است که به تاجرنیا اعلام کرده اگه پنجره‌بازنشود…</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24885" target="_blank">📅 22:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24884">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBWr_Tiw8MWnk1ZRGpCYIimhAm472eTGswDYhBWyv35b4OWBXCklfaivUvp944RjGcTSPP91hqAH31N4c4G0Z4ytQN2tWeJdkRCiMR5GMTdkMwZ2ytJZMNO6UBJgOkJRsMknS2JFqRflKhYOoNhBaJzH1iQQFmiaM9Lk1E7HGNxoWr2ptd8HgqJof51_50QPpeMmrvZKnCI39Cq8qZG7oieGHtxeBi5edwGE4z0-8z5u4x1hkigZSlPAt7ifWbGt06ulycyAjUBXJ7F-w25w89-2xwrUGweQI2AnleXfEekc4mxsH6iY_wgM_Wkvuq1JB9Pwv42U2u25CkzLwditMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24884" target="_blank">📅 22:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24883">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fee6a7d4a2.mp4?token=rN7n9BFrkI5Mcp05D_AcN09g4up1DA2drSSbT6eueeK7Jpq_d1i5q9Ffqwjt5Q6abGNTZV7t043Q2Xvzms-RjxTMdyxYEC1P6wFipr_AxG5B1hGVDzMLqferNy9g7h1p--F20A0Vgwr6TYe0yd_BTiKadCDvxTAN9w74ED0qGZRx4o0vFcUNCwXtTR_CjeFyKB4WY8Nn6loFZcv4zsuiFQfxqMMNJI6YzDXDlhK9NmauMwkb8g9eN9Y7X8q4MIsLRUvrZF8ZXFUQCEc97deq8v_IMGwQE1ozd-FcVhZVZAp7jj8cJ6q5o1F9y_jhfHAu4fdZLTVhYaU8KqnD2s8PeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fee6a7d4a2.mp4?token=rN7n9BFrkI5Mcp05D_AcN09g4up1DA2drSSbT6eueeK7Jpq_d1i5q9Ffqwjt5Q6abGNTZV7t043Q2Xvzms-RjxTMdyxYEC1P6wFipr_AxG5B1hGVDzMLqferNy9g7h1p--F20A0Vgwr6TYe0yd_BTiKadCDvxTAN9w74ED0qGZRx4o0vFcUNCwXtTR_CjeFyKB4WY8Nn6loFZcv4zsuiFQfxqMMNJI6YzDXDlhK9NmauMwkb8g9eN9Y7X8q4MIsLRUvrZF8ZXFUQCEc97deq8v_IMGwQE1ozd-FcVhZVZAp7jj8cJ6q5o1F9y_jhfHAu4fdZLTVhYaU8KqnD2s8PeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
بامدادامروز دربازی‌پرتغال-کرواسی‌شوت Cr7 به جایی برخوردکرد که شبکه 3 مجبور به سانسور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24883" target="_blank">📅 21:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24882">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFO5eClSUwA3-Eyvjq4pK3-Jjlfrt_M6pHcuzVhBgHSPEESQI9f5FKRCafWZoHDXRuzD_RqbOlJIvLRWj8B5rT5BFB8q3k1YzKdOVTOeTuQfqQXbtM706x7Wa8lhRz9m2OvtkRFRKSH3JnZdo9vKjz5NVI6i9-pwuuhVHAn4XWefz5qHnWgcYMnjf1pZYTyrpT3YrIslzB4lh6a0F4Ok69LAe49q6VEUc2tOuRcRSSbOgOL38tTc44vlRKYYRv_NPjdJpptAoXWyZolLmvvad4KBS-MITBwdAEPLBkrMwoqion7PA3QlRS92oQ8ALi_5rzZaiyXaoOIPy_Qbq6eIYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
رودریگو دی پائول:
یه بار لئومسی دیر به تمرین آرژانتین اومد و من‌بعدش به‌لیونل اسکالونی التماس کردم که مارو بخاطر زود اومدن به تمرین تنبیه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24882" target="_blank">📅 21:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24881">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfPi4YxYvfEC9SrGLjRyrx06jCWgJTHrjoxHerPd20QLMFdJvAkgpqMpH6WXOiJ0uyONMzQsiZBid60AwyEsFRF6KZ_58c1Ba5BGeO5HBuM7mLV5Ase_W7QgyI2mEmTmznLDlcrxXupba43aRGjglyoOckgQabMswOQJUboucg8xV_VGGBb3INcAyUWkSzEkQQDjDM81zQcIdOI4D_QpQCC-a9Xusk9xcX1JHj7nA8luR2wM5dBwEop-d2hFGVrsjM7FVbDZ2XtIEr1eRtm0klKt3k-T0Wb3Ch8G5EpZi0U4fnlHWBODGn-LVeDbD4_r7CYcL2TDuc-6I3JM8ZfbzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
علیرضا فغانی داور دیدار انگلیس و مکزیک شد. به‌امیدموفقیت آقاعلی عزیز در این مسابقه حساس. ایشالا خبر سوت زدن بازی فینال هم منتشر بشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24881" target="_blank">📅 20:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24880">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FW3DUoUvCITgEOfWTmZHsMUvGRgSvZlOOwgxI37Hk2PaiGPjRoXH97MPQXfFekyxjD7UO2q-hhewAxinYRAf_5XeHkHgoxhYmwPanaKP1dox_mCQ709zt_nDQaPPwKzhSBjPDihTiDfGidn6ucsAXuTukfDBSulf9-D2e01-S9tICd2542imY1Xp4U2HUwdK22d09dcenrjS1oBVCP-Ya3MfYsO0eVWvxPIgvHzZaEfghwUhnKLEZrBBuYTbscuZxSXB8qV1J_c1uRLGVXYaW5AJrnVkX32eUkobH5TOC2SGfggTgLekU52r7yJO14eELZK3hjwZVhuNVDlcwA8VoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سپهر حیدری رسما اعلام کرد از ملکه پاکدامنش جدا شده و دیگه رابطه ای بین این دو نفر نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/24880" target="_blank">📅 20:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24879">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9736fee745.mp4?token=twFo3qcPkTJuCG33snfr-B_5d-NsG7yQ8rdjTpbFSacusQuMeDaGvG8MIOnzWxgnDnSEVy-4X_lZhsr1GetdGBuJa3am1ihMZ-sLU-bHMuWiA4QkBwn2RfUUSYDKegE83Qk3NGq4StWajGSDfAwaPPwaBkjC__vl0c04FBUWrFPCBWgTCY1UATH0K4w53_hV8ObhmLawOSiu1qOVSwgcHfH3dLfiFwsKa6C3CkTw3F1xaHgB45zRn08IfWVKXRI0Xw0oY_ejGyCY9qig5vYdsoCgnw6BZCrlbmrRga1kjEvqTgk3HOc3mVib5EF9bSNuhC2roOWowLqm1jPo7W5PSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9736fee745.mp4?token=twFo3qcPkTJuCG33snfr-B_5d-NsG7yQ8rdjTpbFSacusQuMeDaGvG8MIOnzWxgnDnSEVy-4X_lZhsr1GetdGBuJa3am1ihMZ-sLU-bHMuWiA4QkBwn2RfUUSYDKegE83Qk3NGq4StWajGSDfAwaPPwaBkjC__vl0c04FBUWrFPCBWgTCY1UATH0K4w53_hV8ObhmLawOSiu1qOVSwgcHfH3dLfiFwsKa6C3CkTw3F1xaHgB45zRn08IfWVKXRI0Xw0oY_ejGyCY9qig5vYdsoCgnw6BZCrlbmrRga1kjEvqTgk3HOc3mVib5EF9bSNuhC2roOWowLqm1jPo7W5PSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
وقتی‌قانون‌برای همه حتی لیونل مسی فوق ستاره تیم آرژانتین هم یکسانه؛ فقط خنده‌هاشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24879" target="_blank">📅 20:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24878">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLL8i8LVVNPFKYZPCNlkS7cfbMdalgA1bx1lIMkHVLLNeHdW-tYdeYaNO3a4ToNVRpBqaW4nyJwq3KsvBjToReLZ8dFLibk__2iAbOACQP5T-WclXBaRR1hJYMPjdMXU3JAGOt7r6No5tv4ytkZ6T9a3fd3Epw4OwTHQNvEfDAPtu-OV_4BWsmwXCxW7n10bjKCDm3HVqcn1DfcKWIDLfvv9s68-DTjX4sQiDxf52wXFTh_Mbzt2uWCrcZYys75cjDfd0SNjKoW-ezT2xR1zqBuySaSIl4MfjLo9lLNABoTK1uXcDswOTYmNyufjg-yz_XKxwPD1ht5woJelauNjyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی پرشیانا
؛ کاوه رضایی ساعتی پیش با حضور در ساختمان باشگاه سپاهان قرارداد خود را به مدت یک فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24878" target="_blank">📅 19:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24877">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/459003d30a.mp4?token=qLMFYRY5tPIH8kbchTwEtJLXwezjQhuluroqu0f3wI_8i0Y-VaiqqTyc8ECfv2vaXIEppQLReA_DPXrTStlA9rkBD95ZVl9W8QrTBWuTE0tF4Zb2dM_CWQE22dDeu4eQx1c1Hz9cnhMAuBxTlEET9w97hik9WuBAEno8qN2YnG4hpVADrsrbLgrFHsX6BqLTWIO9g0Aty0Aru7Tp74V_FB0W-Ns-pMuTnNkqCMA1yRyIRECG_F2XwtcZmimH3VSQrgNdOzwAUuK2_lpqSKBKSKxNj8L82lZUmn5nNPWmIplSkEaASW3DkLtZBkKSIXNRZpCVRJhL2DOzQuVNQDdyEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/459003d30a.mp4?token=qLMFYRY5tPIH8kbchTwEtJLXwezjQhuluroqu0f3wI_8i0Y-VaiqqTyc8ECfv2vaXIEppQLReA_DPXrTStlA9rkBD95ZVl9W8QrTBWuTE0tF4Zb2dM_CWQE22dDeu4eQx1c1Hz9cnhMAuBxTlEET9w97hik9WuBAEno8qN2YnG4hpVADrsrbLgrFHsX6BqLTWIO9g0Aty0Aru7Tp74V_FB0W-Ns-pMuTnNkqCMA1yRyIRECG_F2XwtcZmimH3VSQrgNdOzwAUuK2_lpqSKBKSKxNj8L82lZUmn5nNPWmIplSkEaASW3DkLtZBkKSIXNRZpCVRJhL2DOzQuVNQDdyEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
طوری که‌‌ تیم‌های حاضر در مرحله 1/16 نهایی دارن بمرحله‌بعدی‌جام‌جهانی 2026 صعود میکنن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24877" target="_blank">📅 19:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24876">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kctFx9y6vq6jHuQ0F_cBjBd0ijgLbgcA_r51UNNsN3PvvwSK-c7KCD6Oksl_zrkxtujf-GC4ZkJ1hfVuddw9wqmKBtuZcjTWhPCPYXwcgMFp5MmUV0z0y6YjfbBjvsyJWMx10kKTnrW8TsaudWpMhQu8MrONDFVZwYE0gv_l-ccfywQWuQGJ5p-3Fd5Pd9dU-9_sfdTUC876iWcOsKHWq1jFelq-UDTxIy8yU9JVGvc-S6OQYPa2TNYLsrADqUiiBCLOSvVqwvs5sScCihCBJtdWYDirWEcYGssq6vbhWpt90Sw9ZUPYMsDxbOcb1kAkY-aur4KGBB_i8bTLctvl_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
👤
شیدا مقصودلو همسر29ساله خوزه مورایس سرمربی 60 ساله سابق سپاهان و الوحده امارات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24876" target="_blank">📅 18:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24875">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/376f8db7a5.mp4?token=SggQ17nQTYE1I7Spyzx9XkAeCRHU2gGteYf02-EpFbjMhU1BfKGKLZmLVc7nHUoVSPk_c61pf78bkcwGXliqwLVEDGc1DMsFVF_t_88IfmPyQw6oB1A7XE1vaXQi-HiscI_JoC6PjFsI_6Tfha3Jye0qRn15YcZS52AKT_5RpXafMaRRoMFLLAC93ixxTc-9vpNT7V5-nZOA56mnxVFn_ZB4pw28EG0TGfftIP48JJtpNKyoG86pXjB314AwkYko2vYrZQW4BlZPA00-whv3aQ-8Pss-mT_nC-3y9I9gIGdItFB2t2MHcXyzkD6PRsINh4LFOWot_WcdgQN_qkzlcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/376f8db7a5.mp4?token=SggQ17nQTYE1I7Spyzx9XkAeCRHU2gGteYf02-EpFbjMhU1BfKGKLZmLVc7nHUoVSPk_c61pf78bkcwGXliqwLVEDGc1DMsFVF_t_88IfmPyQw6oB1A7XE1vaXQi-HiscI_JoC6PjFsI_6Tfha3Jye0qRn15YcZS52AKT_5RpXafMaRRoMFLLAC93ixxTc-9vpNT7V5-nZOA56mnxVFn_ZB4pw28EG0TGfftIP48JJtpNKyoG86pXjB314AwkYko2vYrZQW4BlZPA00-whv3aQ-8Pss-mT_nC-3y9I9gIGdItFB2t2MHcXyzkD6PRsINh4LFOWot_WcdgQN_qkzlcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
​​
وقتی بعد دیدن بازی‌های‌تیم‌ملی نروژ و تشویقی وایکینگی‌شون‌میری‌باشگاه‌وحرکت قایقی رو میزنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/24875" target="_blank">📅 18:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24873">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97048a0557.mp4?token=DXaW0k50V4AWr5Q4y7rW-8gWFuQd3DJtgH_l8-2XpFWtccVtBIwsI-SlBrqnRfGnlutjbo3PPRDy3ncceSh39cYR4v--IGowh1e58Ms34m2mjIwoyylBwkV_2W0TH1sm3a9Q7jg-6htKsjLxQZzmJmMeeA3yMt8nwNHZ2DHeAEGcyDejyg0YJYk-zmIZ7RHe044q42v465D3jWjoe8LOHdO4WN5YBOMrqTBOGkonMWiEc0JLQkjV245i7OJYyROJu0zbpnmvNjphKwqOghLrd0V9H-GotivZ1DZQ-u1iPMKCnKZPqstu08n8QagFHLuZvdVsadSdyb783CCQkwaK1oH40_rYQUAkRJSTDe33oNyllvTh3o2sx--RKPJLq5_fcz7zbFWomr01kyM6oOpPqI56gW7zg2WCRXvcuj7Vxz6oY7-sPHliL-qPve1u12RKPr8pERIvPe9tkg4vTdPUVaM7z6MjT4bhYNIQ1FuN_5jNehakX_BvDKsHIwGOyW7Hu0AK8PzlRJIK1tbelSnYiGNxAqJ5EoyswKAFgCMzo4dOnTeIb6DCtb1yllpo0Kmy6d6FD-SM9LmBOPr6EjMKNZXKtP-IrAj-2sNyTZ1CnemqwrO1JyCn1IwJzaARedsEF6Y2xgp3H9tpV0roS9tdompILjSCJOckyCzLn82xThw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97048a0557.mp4?token=DXaW0k50V4AWr5Q4y7rW-8gWFuQd3DJtgH_l8-2XpFWtccVtBIwsI-SlBrqnRfGnlutjbo3PPRDy3ncceSh39cYR4v--IGowh1e58Ms34m2mjIwoyylBwkV_2W0TH1sm3a9Q7jg-6htKsjLxQZzmJmMeeA3yMt8nwNHZ2DHeAEGcyDejyg0YJYk-zmIZ7RHe044q42v465D3jWjoe8LOHdO4WN5YBOMrqTBOGkonMWiEc0JLQkjV245i7OJYyROJu0zbpnmvNjphKwqOghLrd0V9H-GotivZ1DZQ-u1iPMKCnKZPqstu08n8QagFHLuZvdVsadSdyb783CCQkwaK1oH40_rYQUAkRJSTDe33oNyllvTh3o2sx--RKPJLq5_fcz7zbFWomr01kyM6oOpPqI56gW7zg2WCRXvcuj7Vxz6oY7-sPHliL-qPve1u12RKPr8pERIvPe9tkg4vTdPUVaM7z6MjT4bhYNIQ1FuN_5jNehakX_BvDKsHIwGOyW7Hu0AK8PzlRJIK1tbelSnYiGNxAqJ5EoyswKAFgCMzo4dOnTeIb6DCtb1yllpo0Kmy6d6FD-SM9LmBOPr6EjMKNZXKtP-IrAj-2sNyTZ1CnemqwrO1JyCn1IwJzaARedsEF6Y2xgp3H9tpV0roS9tdompILjSCJOckyCzLn82xThw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
و بازم‌هواداران تیم مکزیک؛ اونقدر ویدیو‌ها زیاده که باید هایلایت‌کنیم بعضی‌هاشو بذاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24873" target="_blank">📅 17:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24872">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a06e45a5e8.mp4?token=JtyMMcQ_3HqP-xvF-AbNlbqrizvh2lF0pZv3swGi57N7B59jED7gsADx0MXGKjK2V4Xz6lox2OQ3-4mB5YrzZ_zXs_LO7w-BGehN97AuwKoQyxmZTAqrTrZ3-Na1fznuZsVxe8Mu_mNZ2oW2dpagYbSY2IpAIHghN-0qmMcGB5uK2fyFB_ggKlhVmeZIgSMXfZW7yrO8Q-g9NxWw5E45_1laoWOZ9N8Np0GIfWLQFZ3wQZiFwOfyom9odFNhtrxQbI1IJRIufCT3B0pl9Pr1MxiBYk5YN1ZfG2R_s4Rh2CJLw27_m5EFpk3Rty2RiGD5N8_cHIl_8aDSWtRZiD4NhZx-dkd6FMoIpJ87G9mpMMJAA-v-Oy5Tv_CfrpctKABWYnbckCqpl9m9A10PmnUpUsgumxuRKFVm_I6a5xV2vAv2SslD4w75W9BFDN8aY4UBJBGOEP1OjnaRvfq7JddyD8sXGrHcfCvp1q3nWMGyNgoNcQTGfMfiMI3H1ccddMmfWheTxCTOI_FKyzEbNJJIEglTMJcEPFbsDi00b_un6gL0SHLHddMpFhNtoRBotZaC1_HMwRyE45yM0iIseUS8IHtChxYd284tljKXeV_Zl2TLn1K2gj-PABcr6FDN3QoWfZqKPl74FrcYSz-cCTwjMImi3pv1bGl_neWdaaDXzeM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a06e45a5e8.mp4?token=JtyMMcQ_3HqP-xvF-AbNlbqrizvh2lF0pZv3swGi57N7B59jED7gsADx0MXGKjK2V4Xz6lox2OQ3-4mB5YrzZ_zXs_LO7w-BGehN97AuwKoQyxmZTAqrTrZ3-Na1fznuZsVxe8Mu_mNZ2oW2dpagYbSY2IpAIHghN-0qmMcGB5uK2fyFB_ggKlhVmeZIgSMXfZW7yrO8Q-g9NxWw5E45_1laoWOZ9N8Np0GIfWLQFZ3wQZiFwOfyom9odFNhtrxQbI1IJRIufCT3B0pl9Pr1MxiBYk5YN1ZfG2R_s4Rh2CJLw27_m5EFpk3Rty2RiGD5N8_cHIl_8aDSWtRZiD4NhZx-dkd6FMoIpJ87G9mpMMJAA-v-Oy5Tv_CfrpctKABWYnbckCqpl9m9A10PmnUpUsgumxuRKFVm_I6a5xV2vAv2SslD4w75W9BFDN8aY4UBJBGOEP1OjnaRvfq7JddyD8sXGrHcfCvp1q3nWMGyNgoNcQTGfMfiMI3H1ccddMmfWheTxCTOI_FKyzEbNJJIEglTMJcEPFbsDi00b_un6gL0SHLHddMpFhNtoRBotZaC1_HMwRyE45yM0iIseUS8IHtChxYd284tljKXeV_Zl2TLn1K2gj-PABcr6FDN3QoWfZqKPl74FrcYSz-cCTwjMImi3pv1bGl_neWdaaDXzeM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
گنگ‌ترین همکاری‌تاریخ سینما؛ حضور غیرمنتظره مسی درتیزرفیلمSpider-Man: Brand New Day
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/24872" target="_blank">📅 17:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24871">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oodpjJFj2oF3Ny-rBtz1dkwKSBkMj4JZGJ0a2mnBmBZQ_A3I2NKOo8f5qxgBAJ6HH6zyNWS1Rpja1L8-X8NXD2KImBEzrb_7rodM8JfDJ6vzoWmTeqz5LR3sJK90Vi_NX5iRG9ftWl6QCVIRPe9T4sWoRMa_zoM3_zKV_bx2xWw5kWH63GbsAzf0IkplIdBIqx29VjX9k0TY8I3pcOniYRCzdJxmsBYED_YlgeeDNztJOdGClLi_qGkX_fj4yZBFtq45R1ptHC15qwy2pJZrjTKBeEGZWM6uxUbyxaCl0bKyYxjfpdoR-7bFbnPxpgWXEi2acKaZJ2kSpgx-nzqYKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
🤩
رسانه اسپورت: دیگو سیمئونه سرمربی اتلتیکو به‌سران‌ باشگاه گفته بزور نمیشه یه بازیکن رو راضی‌به‌موندن‌کرد.150 میلیون‌یورو ازبارسا بگیرید و آلوارز رو بهشون بفروشید یه مهاجم بهتر پیدا میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24871" target="_blank">📅 17:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24870">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a0d41c219.mp4?token=Osqb9Ra6Os9wXshHOsZ_LOiKt2cYXTP5r4-64TEwNJhQVJ7nckd_-SIndUO57GU94TbbHnoYa-k0NakOEgN6KP_wL8HwC2nJhk1yWFMclxDu2lH7hY86GCZX9okfHcGcw6EACZSfi21LB9r0qpdAyroMz1AQiZSfg7Sk5uvL9WF2m9qe_Ptd4yfgLcycf2JT_G5mLern-jqOjZRIEDrGjAewwTwZD2OBAXE7FR_Q9C_QwCZ_JKIFSDSUp24xp1EChlcQ28kgVE89yvZ1UzqDk_s-5_6x5gvKJrnpdvhRJgOYEEFH8uTBfMxKRJK3sxabAxvwSqOTSpYE2dRQLtg3EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a0d41c219.mp4?token=Osqb9Ra6Os9wXshHOsZ_LOiKt2cYXTP5r4-64TEwNJhQVJ7nckd_-SIndUO57GU94TbbHnoYa-k0NakOEgN6KP_wL8HwC2nJhk1yWFMclxDu2lH7hY86GCZX9okfHcGcw6EACZSfi21LB9r0qpdAyroMz1AQiZSfg7Sk5uvL9WF2m9qe_Ptd4yfgLcycf2JT_G5mLern-jqOjZRIEDrGjAewwTwZD2OBAXE7FR_Q9C_QwCZ_JKIFSDSUp24xp1EChlcQ28kgVE89yvZ1UzqDk_s-5_6x5gvKJrnpdvhRJgOYEEFH8uTBfMxKRJK3sxabAxvwSqOTSpYE2dRQLtg3EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پدر آقای‌دسابره‌سرمربی‌تیم‌ملی‌کنگو در حین جام فوت شدن و به ایشون خبر ندادن، بعد یهو بعد باخت به‌‌تیم‌انگلیس وسط کنفرانس خبری یه خبرنگار بهش تسلیت میگه و این از همه جا بی‌خبر قفل میکنه که تسلیت چی؟ و با یه حالت شوکه تشکر میکنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24870" target="_blank">📅 16:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24869">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8337fefdb.mp4?token=OJgIJxFgbLBSIma_xot0inPvxLdvZnHrLEQ_hIG6mrG2WTzzwC4OgJ4h216Bg01NH4PbkaPU3r6bRB2jBEQ9IZbxfQc4o9b5zUF3vQg-1q-cimWm7VGbMsya1WCgtdwxp8ekohb9NL62SsxfSpX_jE8YO9M_cLt9ufA0bpuuLRKTG0WH7Rl5m--ukqNDRgdIKhZQKJk7idKnbuGtRsNeH_QTz9l0eMTUztnGUlXNafEhF4EzNTUQsqQblBndv7-dti0J_KbV93IfRw3Tjusnez4nFBzVurjzewo5bnvRhb6dly45xrFzGS7_M9J2y-DTHwZxGbVEwYgSUpeNWksG6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8337fefdb.mp4?token=OJgIJxFgbLBSIma_xot0inPvxLdvZnHrLEQ_hIG6mrG2WTzzwC4OgJ4h216Bg01NH4PbkaPU3r6bRB2jBEQ9IZbxfQc4o9b5zUF3vQg-1q-cimWm7VGbMsya1WCgtdwxp8ekohb9NL62SsxfSpX_jE8YO9M_cLt9ufA0bpuuLRKTG0WH7Rl5m--ukqNDRgdIKhZQKJk7idKnbuGtRsNeH_QTz9l0eMTUztnGUlXNafEhF4EzNTUQsqQblBndv7-dti0J_KbV93IfRw3Tjusnez4nFBzVurjzewo5bnvRhb6dly45xrFzGS7_M9J2y-DTHwZxGbVEwYgSUpeNWksG6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: خواهرم‌ گفته این‌آخر خطه و خداحافظی میکنم بعدجام؟ دیگه تصمیمای عجولانه و بی‌هدف نمیگیرم. بعداً تصمیم می‌گیرم، نه الآن.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24869" target="_blank">📅 16:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24866">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8659ae843a.mp4?token=WnOe5Nnp9h6k7ylJpMeh0_jnoq8YsXLFDU7XdtyYcrs57ycVQ4YIcsflHvr-p5T83Msv32hSPp7qv3NwDSDE47Fmw3m01C-VCSzF-ciqdpbnYTlZ319c7AWcSJAyq4d7APzpLwrIFxDrcf7EUGP5dg0KbTYfwZJIwDnDMYfsI9FplxcDd_jU414H9cHfc1335v-NFfVrRUT0DOx0pxP9KDjRHUQVcQ2Cmr7khA_tb4V-_jFnqAHKUkrzGl6yEpSIbJrARHP4d_1fIfadtmqnpAyYFfs-vzsah-U3W6gb2SJNVRWIXJviCG7CJxtxyFNh0ZP5wecxQLVxZDwefQcZ3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8659ae843a.mp4?token=WnOe5Nnp9h6k7ylJpMeh0_jnoq8YsXLFDU7XdtyYcrs57ycVQ4YIcsflHvr-p5T83Msv32hSPp7qv3NwDSDE47Fmw3m01C-VCSzF-ciqdpbnYTlZ319c7AWcSJAyq4d7APzpLwrIFxDrcf7EUGP5dg0KbTYfwZJIwDnDMYfsI9FplxcDd_jU414H9cHfc1335v-NFfVrRUT0DOx0pxP9KDjRHUQVcQ2Cmr7khA_tb4V-_jFnqAHKUkrzGl6yEpSIbJrARHP4d_1fIfadtmqnpAyYFfs-vzsah-U3W6gb2SJNVRWIXJviCG7CJxtxyFNh0ZP5wecxQLVxZDwefQcZ3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
ارلینگ‌ هالند ستاره 25 ساله نروژی باشگاه منچسترسیتی اگه درکشور‌های‌مختلف بدنیا میومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24866" target="_blank">📅 16:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24865">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/liF4h9fx6yY22dvHo_wPr5kj7lKdBPyhcav8hGuoF8crwATIvlb_8f7fUyQe2zWVJi5SmabMbeq1QCsXNIxqvKo0mwpwI0HI_teufEdQHN-Q_PCCnaWX74oXDbXyL4Hy98MHKIRxyQZjeFkQ2oYaoxC01pOs0hcszP9km2ZRfKt1sZZtHB69POY9bthucofipEnbIMGLqs7LpqyKSt9u_gpDJIk1pb-9sU2cBAO-RxOzuIZlUm-swkVBnTpons3iuo7LSRdiYb9Gosn9chQ0HD4PH85nacm3SEVfaLV4eBx5yDDIDrwDauMze_4Y0yn5ZR_oPeXfrIYBW4Jl5zCd9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: خواهرم‌ گفته این‌آخر خطه و خداحافظی میکنم بعدجام؟ دیگه تصمیمای عجولانه و بی‌هدف نمیگیرم. بعداً تصمیم می‌گیرم، نه الآن.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24865" target="_blank">📅 15:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24864">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKaG3wp4jIHgoNe8Z0mBdwfhgK1PcMxDBadN4L6nVCJDIC7Cm1ScDRzKJGLOwcZvQbJz1-k3idjSO5PscoOSMRkuIMfTkE0zQdfwBD3-0XjdlLUMMkUsLiWa5VQEjtD8EWTUf8Ds2SQ81rT9ChyF__UsGokf_CXTsM3X8eFPYH4tvZnmgP_dNOdclsiRu4nPT6zbaMfCK9YmCST6YInd2Z8hrvvVlwfpjzvm7H6s_IsyhTkVx526RTNnKKb0Lo56ymMdL_y_n1bZeHZn82vJ-lU1v3iSn3zBUdQlQ5ri9t04xUuiBVxKf7okeOYA1MJZOaDeYeJ_89Cw7vf84zJWRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
محمد خلیفه گلرآلومینیوم‌اراک: باشگاه استقلال باآلومینیوم به توافق نهایی نرسیده. الویتم حضور در لیگ برتره و دوس دارم که در تیم بزرگی بازی کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24864" target="_blank">📅 15:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24863">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqzCPF8aWY-03XNnh789xl1XcGRBfyD4AWpGvut8ztiR-ljeF6khyG4vz6USQzkAr5mcyW4k05mMfGmnuj9ukf9OOp1kDMlrov_QGJ36uGoDfgAm56zG_ehvPiLECmF2KsYPCwHn3T6b9yC-IIeus4KnM1JG9esVs_bpT686zScutpoEWPjkQt6F8npQO-llbJQ82xIh3FqwciRVIaLnneLXVRAFi5gzw9GGzxmELwf0X6Ve2lprqMjez1svXcuL9LDRsUAVlff5N_TM-oKqsJcrlRS_FBuy7M82TajxdxDejj-O9t7lhOB_hjh95IuZTLh2UeZ2UqNS1SWx41OvOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛باشگاه استقلال دراین‌پنجره نقل و انتقالاتی بین‌علیرضا بیرانوند و محمد خلیفه یکی رو قطعی جذب خواهد کرد. با توجه به توافقات صورت گرفته بین‌ابی‌ها و مدیران الومینیوم ممکنه که محمد خلیفه بزودی قراردادی پنج‌ساله با استقلال امضا کند اما یک فصل قرضی در…</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24863" target="_blank">📅 15:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24862">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHduZ07EsXMH3c_rzFibHXTYw585b3mgj8TUKEAYx1waD8gYr6Cyy8F6QeReSBLZprKcnl09Gx7T6pztj0m41K7FDFo-mYWZlJA6ECAFvc-6mdza9bW74eHxLSy4ch-jMLU05V1R2IIYqHs-sZzQCSINco6-YVD2PPpSUWTlacCdRVPf8xXCiKuCJQRYqtb5xMlqc3rp2U4KpNnbM-kSN2fLFW9ZxawYEEK14_Ki3AZl0IaJ3QCfoSwU_LasrPDW_d9niKPHb3DsUZXaYYACdsUnVBii4W03w8PQ1rdlNPBZ2AP7yXWqrE2Dr3MKM62o1c4tI5ieqVHzEJVM1x4_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دو تصویر متفاوت از کریستیانو رونالدو در دوسن 21 سالگی و 41 سالگی تعداد گل‌های CR7 در کل دوران حرفه‌‌ای خود به 976 رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24862" target="_blank">📅 14:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24861">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhvUGUReSA2Icn4DCwdAKCHRn2JsEe5B6NVuoO8tlLwRP-unpp1MGDivSHFtjDz0W7-9UF-aE5g_gDx7987CPuGHhs2tjJiIYUCutuNmBtzhPw5DU7CxZNxj-2HvmQX3QbDugmrnR4EHjhh1Z3BwTloy8RsxL2L9lmAkDCTLLtio9nrh0E6Finj9tupOsies2uHOfGaWOzqUr2tCDOpi0HBj9y6B0Sy9LHxwLIGhzHDeOl7d0YTrFIwdUvenqyz8wdaZRc8jSb3AuEA87rZO2aNXzmxMvEEgiK1JhkA9sFKdz1L363kGUOoOQT4Mxcz6B_5JqtIflafgvbpNKPR7nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
🇩🇪
#نقل‌وانتقالات
|
مارک آندره تراشتگن با عقد قراردادی‌قرضی‌تاسال ۲۰۲۷ راهی‌آژاکس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24861" target="_blank">📅 14:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24859">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGWhaHSOEHvMsH_pVifeLqjwOLKJVLbvH7nikxY7nzBPntfjXXWXuiIx9ndLROdjGvehs2NQjdK-H3tCqu-T5FdyKCJ5TYWfttXVxnnvGcdclLDwOrlWbrNJ8A09isqg8ivcKj7nWALB1hpDFAUG4k6Gb74eHYCOGmHu49IRVoI0exy-XT6tfe8AvrquAJIo6gh_-AdHIh9Tm4H0_wWUcSVs-dCRRWQ-hprCjOHbWDhr6xICVQj9VQhpflAjGrCrBHy6C8ff21koj5hHfhKCnyc76sLjn2gAtTbWT_tRiLzcD6nlBQekV8meMPGegMhPTlAm4ExrXYPuHWOOyt8WIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a322be112.mp4?token=Z2PtcxqEcOW_y8qDVLx4mcYQMjgHi5FZkGkKHRhOKKePQDEqhXp-Rx0Gs5mmvOY4PIchVw9oiceNkuTyyf_r_-N2Nk94lxpEZFIJU98S3aH-ZzBmZXtGcG49hittwP0G_nsSr3oeEo7p-6BqUiVedFENaz5Kl8-u3_fgFzPuNvt891rq6A30QeiUQU1js09HZJr0PggYEULiJ6Ul-oHaiFvtB64kwsKaIx9mzXRmgg8iQOiIpWWnyXmrK-WIOTi8344CqFWlxzSPn8qk2oYWc-LrCokycdnuBKOfUPpWAKxU6R-hCZdVZaocMZEp98oUUuaMWP_6Yp2da9u0zkt_FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a322be112.mp4?token=Z2PtcxqEcOW_y8qDVLx4mcYQMjgHi5FZkGkKHRhOKKePQDEqhXp-Rx0Gs5mmvOY4PIchVw9oiceNkuTyyf_r_-N2Nk94lxpEZFIJU98S3aH-ZzBmZXtGcG49hittwP0G_nsSr3oeEo7p-6BqUiVedFENaz5Kl8-u3_fgFzPuNvt891rq6A30QeiUQU1js09HZJr0PggYEULiJ6Ul-oHaiFvtB64kwsKaIx9mzXRmgg8iQOiIpWWnyXmrK-WIOTi8344CqFWlxzSPn8qk2oYWc-LrCokycdnuBKOfUPpWAKxU6R-hCZdVZaocMZEp98oUUuaMWP_6Yp2da9u0zkt_FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
دربین‌تماشاگران‌بازی‌ اسپانیا
🆚
اتریش؛ کلی ستاره بود؛ از فوتبالیست گرفته تا بازیگر سینما و خواننده، اون عکس هم خانم روزالیا هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24859" target="_blank">📅 14:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24858">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyPhh04NrqK59-ZJ-aQXZyVGwBvsn5bYG0-wrPrml8ZYTVMUNIzL6XL_Vnq69IBMoAR0YvOc_wOVE1QKGexI4fjcg1c2RyRM6SmAahnHPp0a-xMPoq6SM0HcKYcMHl2P8rG5IxiTUQlXnHEZLuMy-6ZwiCUuf1535cIva_I2_yQY8556sronOT1Eni0UpzM-DOMh57y90lAfJFgaKMvZiLIGqCU-1Cql3N546JMeWbRTPXLTw_pCPgz68PFUrgzMbuvImmOJPSVlJunFwhUTecXccrcSf2ajxO8Il-RcO_-ng7rIZvcutGwjIeKg0Gr1NKmbktooD1mEg1XHoFaw3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این هوادار مکزیک گفته اگه این تیم انگلیس رو شکست بده به50خانواده‌مکزیکی کمک مالی میکنه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/24858" target="_blank">📅 13:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24857">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5srLoi52ZDmHApl5Yt3kBq9WDJ5m5Y5E1tZjtkudEBWODTS-FGsDMzIP9K-d-buhrmBarpbbHZF3gQaL2OJiQw1vxn2_9Q-w85-L-FV73g-ev7SOQxfZGrmhOK5TVVU8ivUxS1SPknDp-hW4khZDqMLMa0kLF9kLhOi1zNbqlUANogqhlD2obq1snOS4wONuTegvpbDGpSn82h2-apKSTQRmgH6I6D3OcbBXJMGPGeH4S1w6KHmnTL2ZJu1QE1IXL7xPCIB6AWpcwWcI7cdBZ1-gdhk-CQ5qtRcn46SPgOXFp48aasmpT_ShWtVolPcgF4hZsyzJgFRHd6g7YNK5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور که در روزهای اخیر بارها گفتیم؛ دراگان اسکوچیچ سرمربی سابق تراکتور پیش نویس قرارداد خودرا باپرسپولیس‌امضا کرد اما اومدن او به ایران منوط به پیش پرداختی ازسوی بانک شهر است که بارها گفتیم یکی از اعضای هیات مدیره بانک شهر مخالف جذب اسکوچیچ بااون‌شروط…</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24857" target="_blank">📅 13:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24856">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8Em4uVUkIQUB79n0WFSbZqHDzJu1JOgQkzaWpA16IhL-O_Utvb1VnRZP5JSyn4qDAo51WJ0mUl2XeqA8di0zKiPxnsk4pk9aNVGNQPxcRoPzMeljnfvUJLLo0wlnVFf_NRe0Dl4iWEkwG6RPtx-FvzwygzMcUpgMYRQCSqs90Cv-s1IqD2VHPuwNQnEe-8K4F0JxW9dKsE1w-JZXhTd2ClcaJnuWHAyUnLokpNN7SfWamDhsUkGAQ1iHztGQoT6JDs3z3aizJmCBE5LBX63aTBP4zlMT4XMtqecKpZbxmN8Noxh9Gxta3eoo_AQe7hIp5EP3QZi4iTwXJbqhcIg5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق شنیده‌‌های پرشیانا؛ باشگاه تراکتور بامدیربرنامه‌های محمد دانشگر وارد مذاکره شده تا در صورت توافق مالی با این بازیکن قرار داد امضا کند. دانشگر در کنار مذاکرات باسایر باشگاه‌ها درتلاشه که با قراردادی خفن به استقلال برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24856" target="_blank">📅 12:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24855">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUNmVl9h-o-XOOqTyurO1dr9iJb5lEQNkN7POD7-zD85KjfDngjzRtGjllL-7-Pb4hdF3WyQdfe5p3vBNWyiEcTZo7DKhZI2x0EHKwKYP0dJJn4BWkJRbrdspW7U6BDD6LEp5G3MPBV6v4F1S3C0sQ49NRUHPE-oIRtAmu-vG9j_NAsbaOKZIy8FQLjI_Vxlw9H6P0n-iqNeJOp_kV2dQt53C5QD04N-lz1TjiC1f5fwjI_foIzTfh1IS2Si8ZZqPdJxJc2eeB1wVwBJE2D15qEy2d1k7h2aykB6aj5oBDGaIYQNU87lTKEg5hpDCP4MJMkJLVmrJ8GjqS8YnYhMQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ماسیمیلیانو آلگری سرمربی فصل گذشته تیم آث میلان با عقد قراردادی 2 ساله سرمربی ناپولی شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24855" target="_blank">📅 11:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24853">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VSY-MTXES_q3FBxXde040fkp8n-6sXrZCOy5egYltIgmh9IURZbraWPZtZYmQ2OSP-Nd0kx2-wrGtJ6ajq3WKgQjhF9ap-aW4QLosugI63aFqRzBV32x_M_h_nOXih0-JO_dXIph6Lc4Y5zxFd8jvqsNADXJrs3ittakybcVTwN10LWB-0x4X3L8ZOedj8QkALL_uFm7jnWTARk9mnCiQXrE7g8vCBc1XZxNfsswayVkJ_BGrozLuE9yD8ZNdT_QPlrdxoyzcGrl2qxpJmBy_wAELqTD-zkmBbqNph3-7VScV0y_Ua3qvkim-lbhmy2S5nKnAuJMK2g8RlZIX7086Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gjWifXIG6yAC8xDE9b9u8ywEpPZD0LcYbAxlB9rwz2bCNrE37L4vSa3SO1FURidbv2ZxUaGZs3ZfT4L-Dlueg7GajOfPcm5mpNsFbQsL0MEIqezKKXImCliXAh_SH2QQAN2BiK1WkGG8gVCyoB2Ryhfg8EcQl9-WHj99uFUmyFvai_e3L_su3JwH2G9SqwdkxzbWRHSEWsmtEWMHpn0KgWzUo_eyGLf_ilPBFSr5vce7IFUPZWNv7w6sC-bBcDzh7KPQCLY4PsBWqKIBe4l-1C4-yv_XQHzJ9k9uj4SikZ5k7Vt9xqULHd3czOl3GKTRHqeGIzen-12kEl1SuTFTwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇵🇹
به‌یـاد ژوتا عزیز؛ دیشب پرتغال درحالی که یک‌بر صفر از تیم‌ملی‌کرواسی عقب بود. کامبک زد و با گل های رونالدو و راموس تونست به مرحله بعدی بره. رونالدو هم به منظور سالگرد ژوتا  پیراهنش رو پوشید. تا خوشحالیش رو با اون شریک بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24853" target="_blank">📅 11:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24852">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f468b62e.mp4?token=Q6fBoMPoZ-J5ZCuHFA9WRvD3dzmKdMBN-fBSLp-EQ7CoeX9ranO8hXoRpu1-5I8Wt7j_hp-SLOr8K8h8uxmjL0XMAWtdVY2907jKtQuyowF3DXoY9u86UM79b-uU2X4brQvN236BEDr2Y21g4vy4KTsfczepXLO2Ggaz5oH6bPQNo2ko_jB_gCeWqX8jdFHNgvqgyAWIIXW7GAjXtDAQRYGdc9CfzUoWVbVO3T9egSFxM9M0Pp7NVSSy--m1LlGyD_IvV7hTcAGkdc-pUmtopFNY4xmwRD4spplMcByISBOwVpzFoobt-cB5yYXcEvALxppHCkum_Q-7FXeuFuNRlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f468b62e.mp4?token=Q6fBoMPoZ-J5ZCuHFA9WRvD3dzmKdMBN-fBSLp-EQ7CoeX9ranO8hXoRpu1-5I8Wt7j_hp-SLOr8K8h8uxmjL0XMAWtdVY2907jKtQuyowF3DXoY9u86UM79b-uU2X4brQvN236BEDr2Y21g4vy4KTsfczepXLO2Ggaz5oH6bPQNo2ko_jB_gCeWqX8jdFHNgvqgyAWIIXW7GAjXtDAQRYGdc9CfzUoWVbVO3T9egSFxM9M0Pp7NVSSy--m1LlGyD_IvV7hTcAGkdc-pUmtopFNY4xmwRD4spplMcByISBOwVpzFoobt-cB5yYXcEvALxppHCkum_Q-7FXeuFuNRlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
از دو شهروند بلژیکی پرسیدن که حاضر بودین به جای زندگی در بلژیک در ایران زندگی میکردین؛ خودتون پاسخشون رو ببینید‌. چقدر تلخ بود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/24852" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24851">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e81e75283.mp4?token=PRvpgODy6aJ59zpN8-wWfFhedFmAb6yyhFAfxoV8aZh0V525qzRWvk3F3A3yaEkc-6T7btF4BKTBwH1NB8dI0-EBzC2HnwPcRHvwkLNqmbKkY0p5eWoempYUkwhUBtfTRo_Wpt9dpYQlRqDQz0mesGzktZW6OZ0704QMvOi0SMo0iYEfXHowdGKyr2iVCKf67FnaUUu0sbEIpw1njHRhajixdPkI9BX6rdM47PXk545cSYDv3LWPcu4LRvGRAoe4HiJ_K-nTy5mA-KDDVhs-fSO2UzyI1X5DbjGN0OyQ7kKIJCr7FiZMmeMI33qfOknRPNNfoR5eM0ARx8g0YMt4RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e81e75283.mp4?token=PRvpgODy6aJ59zpN8-wWfFhedFmAb6yyhFAfxoV8aZh0V525qzRWvk3F3A3yaEkc-6T7btF4BKTBwH1NB8dI0-EBzC2HnwPcRHvwkLNqmbKkY0p5eWoempYUkwhUBtfTRo_Wpt9dpYQlRqDQz0mesGzktZW6OZ0704QMvOi0SMo0iYEfXHowdGKyr2iVCKf67FnaUUu0sbEIpw1njHRhajixdPkI9BX6rdM47PXk545cSYDv3LWPcu4LRvGRAoe4HiJ_K-nTy5mA-KDDVhs-fSO2UzyI1X5DbjGN0OyQ7kKIJCr7FiZMmeMI33qfOknRPNNfoR5eM0ARx8g0YMt4RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
به‌یـاد ژوتا عزیز؛ دیشب پرتغال درحالی که یک‌بر صفر از تیم‌ملی‌کرواسی عقب بود. کامبک زد و با گل های رونالدو و راموس تونست به مرحله بعدی بره. رونالدو هم به منظور سالگرد ژوتا  پیراهنش رو پوشید. تا خوشحالیش رو با اون شریک بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24851" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24849">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DswtgUXd72YShXdPS5UOVYdmwYimGGuM6rBQ_AXrqIqkuMKXy4VMUnKjnazjIlOLgjxD0HAqVfWcGxkw8FRHIWVQZ0yQ5iRk2hxelLvgu-KirFz3SJCQgLlCF--nw4I5j2hRnDI5Sh4OinniA24Uc4eXdqPRh9DXDSkQTgmQeYYsSz3N_iWTB8kPTeZst0jOZ9iP8rjAukbND00PNops1l2OfpBOcLoAtSipgn3_ozCTDbAgcCZgy1_T3fQofWBlejNvu-HVM88sW3KWyVN6ghrM0x06kpcFXnmV-HencwfhFtAZe_UuWjG9Sh893wUcsHpAFn2ReDiWBvjAmYYHyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اگه سنگ اندازی های عضو هیات مدیره بانک شهر تموم‌شه باشگاه‌پرسپولیس‌از اسکوچیچ رونمایی میکنه. پیش‌پرداختی باید پرداخت شود تا اسکوچیچ وارد ایران شود. امروز پرداخت شه فردا میاد. پیش نویس امضا شده اما شرطش واریز پیش پرداختیه‌.
‼️
دلیل مخالفت اون عضو اینه که…</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24849" target="_blank">📅 09:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24848">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a8e003dd.mp4?token=JhdJzj4UHrWThiEH_NHY8zT0Adp0LfeeWFk2YxgpH91wOpK_3u_qHaI4Bz1oRFA5BYcSwTamWJaNdnNkVroHoy8w1o9k51wIFX0Qsw3JwQk8vUlPLZMG2ee3_4c5mifIeICTv0-Vl0OV1m0oCraCvGNrAf-knJGM58FUAMRHZfNDqGBGly_F9i16n5XSgOcZVtYaGtyAB8RnbHH_YFK8OtzUJVu9i-u4-E4h1cLk5Xn_xdAHhUry7CAOobtSu-0KZuOTcMAEIdamzVjblfCrkc1RHGaZkyL3HeyfMMAJrW_CvAP5c6gOvOvPTkwbvWkntf47sbyoQepfFKSnbhKycQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a8e003dd.mp4?token=JhdJzj4UHrWThiEH_NHY8zT0Adp0LfeeWFk2YxgpH91wOpK_3u_qHaI4Bz1oRFA5BYcSwTamWJaNdnNkVroHoy8w1o9k51wIFX0Qsw3JwQk8vUlPLZMG2ee3_4c5mifIeICTv0-Vl0OV1m0oCraCvGNrAf-knJGM58FUAMRHZfNDqGBGly_F9i16n5XSgOcZVtYaGtyAB8RnbHH_YFK8OtzUJVu9i-u4-E4h1cLk5Xn_xdAHhUry7CAOobtSu-0KZuOTcMAEIdamzVjblfCrkc1RHGaZkyL3HeyfMMAJrW_CvAP5c6gOvOvPTkwbvWkntf47sbyoQepfFKSnbhKycQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
این‌بخش صحبت های فیروز کریمی هم عالیه؛
میگن الهویی دستیار امیر قلعه‌نویی گفته ما هفت تا پلن داشتیم برای جام جهانی؟ مگه فیلم هندیه اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24848" target="_blank">📅 09:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24847">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCs81Ur2tjqz0euffWbIybr1_I4qCeW8NSqQ_d8_AjBHYxRk9vNLvQ6to8L3wtsYHAEEqFXfqQ_fVueFI9sSqwIYTwVqvW2r9OgBaj8V2oYEK6L_k2lxO9bU9kTNTVPTCwrQSGC9FxowYsgIm-qqf5nb4aDNK23vpMg4Yt200JzBbz7TJm6iSSwQQ9GVdTj1wSmlDkplBXNxoFBiJqvHeAYv8VK-OLN8LimX246LQkK3jD56A-kTtHMe2BfGutchziGFFqNIf756Ha8mf4CNaF7BtmLossq1T-bnRCAJpFUnuVH2qqDINcADe2VljAcL2qk2QDo-VmG3dHl5xyypfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت: کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24847" target="_blank">📅 09:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24846">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzHbqZ8RLe6pYqq36Orq61rxJLcHX1a-fIcoFEsL2NRufzk1VFqFFuVJSD6mYCzNKrd1SowY8LoQXTutu5Ex3LnhYskMxum4Qjbgmy5zXFFosVLWvMkQr6HeRHJZkMGSD3xS2n3G8VMe1u1734LITdqxe5WfyXEuEROVEDAAjgl3BNXH2KY2Yj1Z9cqdc_53svxK8fSsM3XVzUrIP0pKZHmwnGvoRzWpFyVYRumSbHsmd1Gw2JcHCRpCHxoOHaN0t8d05KiVIsV39gbObRXiyrUhmWvqGIKbpM1IcEosUqSavETESlIvZ1PV0O9nUyI_Ypz-IMaukDqbY6DT6LNPDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇵🇹
گل‌های دیدار تماشایی و مهیج بامداد امروز دو تیم پرتغال
🆚
کرواسی در جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24846" target="_blank">📅 09:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24844">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F8OzUqX5uyk-M8_PGZs5yEERn201_RkJFBRrXOoJQXAFqf7xTgu5WvdIZ1IpQPlPf3nfXMWuSXFYQ0_BnxYlDj6uGMcmvj1v_x7WS1KZhYnq3xVt2_fRbSiMItf1DyGmgyJRHuEwn5XMjdoHRGCnBMuvcoIXeTaibDWdR5SCK1qzvAhfljUxrnTYV-zcB6Tl0toLCQUqGMW_7eXDE1OlTcU3RHOSO03NZoq8Ry4pVVYl2ij_LlDA0_1K3CqoX5nvdA4FsbkzKoppNR_b6rVlo6RQXXqwpuINBxD7-CIml-iV2BuApg0NZgfI-saa3Ex0tlwJdR9NwD3QUGJSBR7fBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RZzvjEyljSNFnZy472zKooAobHBjxUiqI5RWZ_Gk9uTtzbkbpT9iDkGsQ2nFozMf3w4WMnwkb1m7uUaKkAWd4HrLVTpe94m8d_aSkTfyoK37pA7Wq38fAsEzz9p0K9CaEuqX8GkRmBnEnaOkVKj3aQd7Y-AAfybZO0NM2utc2zTv80zsqjkLu2_0UkdSR-V_m5ZrN522YdVOO_P-CSdRZIvgUDiQY_nSLZSIwMf8pNa6ZdMJ4pGx2Z7OMZ3W-GELdfMoiRk_gT9EbU7iIVXKE_wKU85Y4dhyphHYBHywniA6qJ5Rs6vQHyO87OR5Ewf15VKNg1jvGEBLHEVeB0Er1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🇵🇹
گل‌های دیدار تماشایی و مهیج بامداد امروز دو تیم پرتغال
🆚
کرواسی در جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24844" target="_blank">📅 08:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24843">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1QhGMop9iJTRwnfPeZEQVc6UaX-EVkR8WrBwl-nYwzLwUgO7K9w1J2QGALeQPilB6SVV5NOOJbitmh4c1jYxDPFG1kTBKqcBjTgKnNuZ1KYnuxj4Bq6x7Vg-fQBt7oIcl6I48ytaFueftFE7vjhllBzAupIumyn0Yw7YPyL4ErC_yz0EYjuRuDB0emsK6xYTke17Cdxv_ScgI04WAnJeikKtF6vmhZmar_wlCcBWj4ULOtEJm0mOhSdHA7LszQZwhr0fn3pOmD8iiZZscXIhgnXuLnr0GLhXaAZs3i4dB4lC8VrUWh3Q3s16qt2kcKJFjL1TL-oap0aTBZpgv-F9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی؛ پیروزی شیرین و ارزشمند پرتغال‌مقابل یاران لوکا مودریچ با درخشش فوق ستاره پرتغالی فوتبال جهان؛ یاران رونالدو حریف اسپانیا در مرحله یک هشتم شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24843" target="_blank">📅 08:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24842">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3224dcb43c.mp4?token=PgTy1PR91JDNTIGH7jpwM4_aVrbI4fogBlabGGxqSiZEE_GuVPhZnp2EcPhEZG5H0h98aoSYc8mpFs6_IuAeawmr7B-2hFoKpxkFcpsTxu5IfTvEiJMV4zk7GvjNuytsVERhtkn--KOUIXOFMcFm-TCZVFr8Pxs_WgioUyoue_smPME49KRGESjjMmd3bd2Pkv8BUrMqI5VLl3Je0YNw4_F7QTMBszPFvWi1ClZdriCDXJa1jyWWphUrxXYVQKHlXDZ8xrS9sEPHqM7r5Y-KsTudKkinzzB67Q4o7XBd-OjJZYzSOTSYZtUGQBy0u-44-cZaro7gjeITBZefx-TLSImXPYKEnWOq-SOzpuzGXxfxphD_UVZ75vaeDw8LxHn-WRxfvtyyWEYI_hWs1W0Fekq3v98yvudzrzlFPfnqTspHGDKw3AdXZs9Wxo6feB-70M_TtB0yQAO6aoEfJ3wWiEmerVKyFwhVfooaz7zTg6EExhpDX16968nY-x0IdvF9OWNt4ZncC1J0w9F8nTWsDbUI_5bUPA9sSTm4nNU8JFDcQ9JF2oCAj758_VcuJxKU6Gggwplm-MekmZx33ZCRbstaHMCXlaxfTsIq5ui48guNS2_8M4XvEVnpdPU_3f5Bol5K8w3e3DbRYgWO8DCQyz7PymusKQq3dIQLYZJPdNo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3224dcb43c.mp4?token=PgTy1PR91JDNTIGH7jpwM4_aVrbI4fogBlabGGxqSiZEE_GuVPhZnp2EcPhEZG5H0h98aoSYc8mpFs6_IuAeawmr7B-2hFoKpxkFcpsTxu5IfTvEiJMV4zk7GvjNuytsVERhtkn--KOUIXOFMcFm-TCZVFr8Pxs_WgioUyoue_smPME49KRGESjjMmd3bd2Pkv8BUrMqI5VLl3Je0YNw4_F7QTMBszPFvWi1ClZdriCDXJa1jyWWphUrxXYVQKHlXDZ8xrS9sEPHqM7r5Y-KsTudKkinzzB67Q4o7XBd-OjJZYzSOTSYZtUGQBy0u-44-cZaro7gjeITBZefx-TLSImXPYKEnWOq-SOzpuzGXxfxphD_UVZ75vaeDw8LxHn-WRxfvtyyWEYI_hWs1W0Fekq3v98yvudzrzlFPfnqTspHGDKw3AdXZs9Wxo6feB-70M_TtB0yQAO6aoEfJ3wWiEmerVKyFwhVfooaz7zTg6EExhpDX16968nY-x0IdvF9OWNt4ZncC1J0w9F8nTWsDbUI_5bUPA9sSTm4nNU8JFDcQ9JF2oCAj758_VcuJxKU6Gggwplm-MekmZx33ZCRbstaHMCXlaxfTsIq5ui48guNS2_8M4XvEVnpdPU_3f5Bol5K8w3e3DbRYgWO8DCQyz7PymusKQq3dIQLYZJPdNo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی؛ پیروزی شیرین و ارزشمند پرتغال‌مقابل یاران لوکا مودریچ با درخشش فوق ستاره پرتغالی فوتبال جهان؛ یاران رونالدو حریف اسپانیا در مرحله یک هشتم شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24842" target="_blank">📅 08:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24841">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_cGaxnaXe0-0Xfml-8kvS1auhf44v6ETHwqZlbN7woDP-7484cW9Ocg87muUc60Y3MaHsj3ALKdDjKW2bESa6xmXXZBTZS0VxnxO-VFw4igL9zPFn0oEUUIeE38V5s0l-JOcvSEdtMSX7jec0xUsvAM2CCl5TURKkPu0BgGCVpvXFT1fwZtJ1tYYrhIhY4MrGmPu-bBeAdjS49J2e9NOoCaqIFtgyPE7nIs575XWtgkiwu83q880PDEPQxmZRLzRr_PfIel4euXrNnIwCEPrnQvaREAbFRou2MjhfQha-NnXvdIJkKKajkSqSuig38lr1LmIUykX7yoItOZd6NReA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
تیم‌ملی‌اسپانیا بابرتری ارزشمند سه بر صفر اتریش رو شکست داد و به مرحله یک هشتم نهایی جام حذفی راه پید کرد؛ حریف بعدی لاروخا از بین یاران کریس رونالدو و یاران مودریچ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24841" target="_blank">📅 08:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24839">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1jqii-fyixOecoI7OeyUHPe1PZK9YVTpxV50-PcedJoFHvzN2VKNDw-30O0tTLVXS24g1P4In5uZGE87H36X0scR92lR8PKDHoZunH8A4bOT2CH07G2xK0ytyW7_iC197gBeW0Xznu1cNkCd289v8pNs3uwuObdvXxmkxiCzk1jnN03_P9Fzszj0jArV5_qdF3mBC2_0T9QZ-YDJUCgfN46FpLI8khNyu3NCKVy33VI7Xe3H07_xFClDdcJ1uc32S6l2hQTLVJhzgPqkfJKBXw1OOkBOwyTEuFw2PwMoT9Q67ER_Tp6zt7nSiEc1EuZZtjye_-dYELaeeJAnkk7Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/24839" target="_blank">📅 01:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24837">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IpUlAiv9XKaEZrX6jWuU9IejgzgoAKry9EE1tIj245GbSe7iKBcFUJ8kM9i58o5r8DCzlcZ5XSAWKeoZgs1hVo9Ia8QJwqhDquFBydq6pHPRERLKpxSAUQRRa7uBdhbgjCRBR2DWxZ_dwL9BHJzzE1mA4NSXTo8xZ5CID-rk019U9fCclxeMN_2pnvEDZbdn2KDTvuziBfLZQYclqIJAkqDM0hwHlDptBTqIZr7dxyuCFt6wk-Ql6-RDMZW6qUK1rrPREGTSfbXPjio-h3KhOXdGP1BDH4Rv5EZRhFPKnH8wmLb1m0l7JkOFXg7tOkALJIPolVr5iOCKadGAKjebNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jeOvsZ6sj51s8EdSSXtKhD6Gk5rzBuf5IOW8SYWbpjq-Fo-vJLv6lQ_A3QDMMXtQuHKtkf5pRhR6Rv78mvAeZXmMoMfsbxLZyAzuk8zRaihTVxohduLQN9GBJsc8Qmy38DLOWo21X0MjLCTq46zQgd5eD5MbiN3S7jO75tb4PUmd5Q58e0dG4PJ5Af_P5ocNJ7l6ithCKK5iAXphDTu3agOIrH0CinedEZTA4yRp_CJfpPCa8Nis2H-wTM3zm4WUlc3E9b6QBzPUbmgT2M31VF8cd45A25Q8MqCg2751Hugksde05pJREEXiGyyYUIwEVbk6ULZzwl7WjIF3sOZXkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام
‌
جهانی
؛شماتیک ترکیب دو تیم ملی پرتغال
🆚
کرواسی؛ ساعت 02:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24837" target="_blank">📅 01:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24836">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7bjWLK--nmiyniNSuVVdnIXSMDZg2zp2d_zk600SHLXsEKTQTUWpoACHYYrclnzASw7LFN27rhBt6s6jlvDpq4yd7QMugXUQkjVOZAwc5F7TbH4EPXBMOp-qCUmBU2_ff6q3kgffZc_26HnWrG78TJ_aad1e5WWELPLCUYaumJKJGaSzcxnMs-jVngvMFjYmv8TOHpiqGRR2gJYCyYyUxNQyJmHvtBxBs01GvCBIZ3vO6y_BfH6DmAf12QBCvg1iHuAh9l1aCqDTQnQ1Ri6DliVdJxbJa2DH5FJpqtGy7sKo9ajSdGcYVQIWNFGsPdyO1WqraVcM7VtvtnZBVN6bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسول‌خطیبی درگفتگو باعادل: قلب محمدرضا زنوزی روتیغ‌بزنن روش‌نوشته رسول خطیبی
🙄
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/24836" target="_blank">📅 01:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24835">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwP5A0iIc9ZpiYb5_tO-1FYv49yFM0K3k6TVu1Lw3vSv8pDrDhRM941Ew9ie_Vz2gNMos6VqIIVg0-iS3-pmymXEI_fsWizkL-uQ7fSeGKlutkmcTT_-1AEqOdAW5RzLQLvpCBDitN5yLE54mvkqEEMG3fsIfNebFLEeg51DwqqEg0ya7NKoilpwdWeceEQ8TQWVk49l0jMST45YAUgb_LZkLPyNa__aUAmBfq3KynrzDM0nxmbrOBZMbAcmC59KYFW1SaeqVl0IYKByFRhQCgG0bTVWABEAxxPWBcG_4mv5fK22QGHS46mFSLI2p683s72zIIq8HuXqBLbOGXZs5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
نبرد فوق‌العاده حساس و تماشایی یاران رونالدو
🆚
مودریچ در تورنتو
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24835" target="_blank">📅 01:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24834">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6-lfwsfUQOtarF6kaPlGSn5Vi9bt-OaKlz6kFfdxkqX66xVHRuEWw-Qd7mjZkVik-_5AW2nXMK-ROv1XLJ2xhTicMqHLeG2m_WSNQvcO1cdSesCf7ex1PQnnSt3qUxLs70QU9ptXRY9Ra3J4kAcm-5LytW0YDxsEqaaXAyfjPtP71liOL5jL5pSjnTUxa78zYH0H6ZDyXEoyVeH9-VU6uKJFF5lcGUDUWmwL-dk-2a9yfofFcmBWpGRJp5rwHjAtxkZEUH5ILUw0x7UlW9Tp-8rwhzDgr8RsSSWsV3x3QnM3rUlrY-sbOi5VuFGHhAuoIYZIJ0zBxQYS-OsCcxfkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدارهای‌دیروز؛
صعودمورد انتظار آمریکا و اسپانیا به مرحله یک‌هشتم‌نهایی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24834" target="_blank">📅 01:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24831">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e6a78bfe1.mp4?token=iMan3cqhy-_QPuO9wv27sVKnY9TC7huOqhodSmEOgDxgAzQjxoYPVxjqjEeQR9SzTCvPwSXX89h27b6iNgqdpLL7hDILEMoWSaaHzPTdvuYL0EYivh3XBFgZRdcjaf8sq5xYN8tncoYYUY2MFTytNQVuD0SLLhRkQTehg9H3iJSOFNrIVS75AJvjPvyCF8TxNllhgY8LVIf8_dL060DXE7UbgE6Rt1Ptem8DThdefK-zxsIG1sAVBDBxb2jVNTv7HYYhW8ZkmR8LDkbjdvgCqD_a2ffNDjxg5Md_lk5ON-Maa63V0Q3Dbsp0XM360wnFmwp5hWCeT60_pb52A_J2Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e6a78bfe1.mp4?token=iMan3cqhy-_QPuO9wv27sVKnY9TC7huOqhodSmEOgDxgAzQjxoYPVxjqjEeQR9SzTCvPwSXX89h27b6iNgqdpLL7hDILEMoWSaaHzPTdvuYL0EYivh3XBFgZRdcjaf8sq5xYN8tncoYYUY2MFTytNQVuD0SLLhRkQTehg9H3iJSOFNrIVS75AJvjPvyCF8TxNllhgY8LVIf8_dL060DXE7UbgE6Rt1Ptem8DThdefK-zxsIG1sAVBDBxb2jVNTv7HYYhW8ZkmR8LDkbjdvgCqD_a2ffNDjxg5Md_lk5ON-Maa63V0Q3Dbsp0XM360wnFmwp5hWCeT60_pb52A_J2Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بااعلام‌باشگاه‌تراکتور؛خدادادعزیزی همچنان به فعالیت خود به‌عنوان مدیرتیم ادامه می‌دهد. عزیزی بعداز عدم‌آسیایی شدن پرسپولیس از حضور در این تیم خودداری کرد و قید توافق با سرخ ها رو زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24831" target="_blank">📅 00:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24830">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPGniX7oZTYyhqvNqn1r_3bOw3eXKgfnSEKrpevP-plcTTkb2by_Ccu1yPyCQPObIpVM3qhgTU5ydDweUno6a4OuQYMY8MNF8S6JYzMwnAx9fnnPPWqVMGAhGS97x2GS6YMX-Uyho9Ys3tFlavKYC_dtUhDM0AfIu_NKsA-2vwZapbyJ7QdHZK3tey5lZr77PknpgKAWzbBhS75-qvDELYynfHGKP6LHCDQB391uKbV8-8N8HOvNOkUVInD95n-pX7dHXVJtiPsoKsNcqd2_lnSEqHM-G-p4eVm67tLTajFG3S0bzhtb3jXleXIkpYVE995I3Lw3eEZYEJSUy6ul1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی رقابت‌های جام جهانی بعد از پیروزی سه گله اسپانیا مقابل اتریش. بین پرتغال و کرواسی یکیشون حریف بعدی لاروخاعه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24830" target="_blank">📅 00:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24829">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7rJohTQQtsnmcO8zxOfsKPiyGFV16g6YUpfp44ltB2a4_rBaqUPsgXGQOmjfKFfa05BC0EiM9VtngGbctd-NQkadK2PcPL3lumKzv8j5D2yk10JfmK5liEYWvLj4HItltC0xBYDiFWwvj5H9kbg-NNJI2g8tyOdQFR5bLK92tZngV7nOrDFwsYGnltZfkvayHNF0aH_c7JLwUH-yoqsThFoFuLbbUxxmDs170SjCdFoHqPmlpn81U_8RE-LywoKK4i_0dryudHH0SBQLoWSjQ6slvxmXUetsF8VdldLalBnmFvrqOurCvU_gmAdC37h2l6Lqt7czttuPNBoTu2Trg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درمراسم استقبال از کاروان تیم قلعه نویی؛ تو جمعیت و شلوغی گویا علی نعمتی یه لحظه غفلت کرده گوشی آیفون 17 پرومکسش رو دزدیدن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24829" target="_blank">📅 00:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24828">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rB3__EpjMWS_CkhjOZVfJrZg8GhHUfeIVDriidPtZQNqIiGp3itx8t8Wmpe5yXMR6C14iuieQL_aSdykI5Yw0bM-Gqw2U6GbKs7WIjJgreVXrMXShZO8SSEee67nR7SoSpKk62NexpUtK156hXNBvArtWeAEv_MCe-sEGEE09yhOarcIuTgAYejbeKmu_bUNfMNJKeRn44DP69uF2IsUQV93aVh9Kz3VYqCpB6LmE2p2lsyuLyvqxmZqIHjdojSO805hW63KZQe9zpNdoyHCW_DI5GBQgXeWOK1QgrDB76Vnkw10QG08eaUZc3gB0vGuSgXe0A5gH5SU4AodXwVAtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛طبق‌اخبار دریافتی پرشیانا؛ اگر اوضاع منطقه آرام باشد در جام ملت‌ های آسیا سرمربی خارجی روی نیمکت تیم ایران خواهد نشست. با امیر قلعه نویی قطع همکاری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24828" target="_blank">📅 00:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24827">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3237c767ed.mp4?token=avIfZHGG2Skq5WX22qVm3OaUoAbDxeSpLhK2ZXGIunZgwn47DGEcOdNVxBuij0h1yzxBWWaDQyDPtGQY8UqDX2U4hAKWmSiBk62SABfhyyeyjA9mmRXz5pTPqtwX6HMQgfYYp2O45aGm8zbBQGIyOYWaKVvskH7sJI2YHyJiao09XeSHa-1r3sCwhl7dSdKySNCERore58zyaODnejJNFD5fxgpjV_AJfBAw9Klv9YA0FX5aUB_OyR3TXh0yD59c0e80_4yXH1bMOSHDKBX2Bbk8t8pyugVcGxd2yppuMq1-TaCsQlULhj_Cf2TKbnpUvBZc-bYPt9-JBl3bq8o2YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3237c767ed.mp4?token=avIfZHGG2Skq5WX22qVm3OaUoAbDxeSpLhK2ZXGIunZgwn47DGEcOdNVxBuij0h1yzxBWWaDQyDPtGQY8UqDX2U4hAKWmSiBk62SABfhyyeyjA9mmRXz5pTPqtwX6HMQgfYYp2O45aGm8zbBQGIyOYWaKVvskH7sJI2YHyJiao09XeSHa-1r3sCwhl7dSdKySNCERore58zyaODnejJNFD5fxgpjV_AJfBAw9Klv9YA0FX5aUB_OyR3TXh0yD59c0e80_4yXH1bMOSHDKBX2Bbk8t8pyugVcGxd2yppuMq1-TaCsQlULhj_Cf2TKbnpUvBZc-bYPt9-JBl3bq8o2YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
رونمایی‌از قانونی‌جدید درمستطیل سبز بنام "قانون شجاع" که توسط ابوطالب تصویب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24827" target="_blank">📅 23:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24826">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_f7nORL0Qv14h3xQHOTz_2T4R0PbyngHGSpNQRgHMJwyqeyp_7DQXqhvaah4f_cvGz2DUPWltz9bFiAHCTTuPd_4CGnI07TeaIKwjo1G304_SITpY7A2beOr9DUwlfAKPRSjBWCr6qOou2GATjocFnFA_aHp0fDfmg3iEin1bciws6X_CemaCJWfyBVh4kFTTXWC42t-7FRDovnywjEIPSDrGVB2ThPDPTaEo24OX986aYztUOeg0YoZFrOtj8khBz4H9wuaIGYwYs53XgLdnMMW-fDr5iQ3DmMJ_d4UugPuHiOqwbY6wMaQcP8oLf2Bx2lZVDbdLl8IsowymJ3FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
رسانه Smashi Sports مصری خیلی جدی اومده گفته ژاوی روایران‌میخوادجایگزین ژنرال کنه‌.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24826" target="_blank">📅 23:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24825">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cffa11c70b.mp4?token=q3Y2AdUOwhrDPsT14nKVkn7ze0wCb67Jjam7ON1zN0ddZi196I5RyXz5zZP7qAy-dZf_A-nytecPsSBoNCdxNZWZoDlBqZX7AuKEhfnp9goROIsSZCJI1fug63_I1_ooMUzctoxxS8YIaoSP7_jL0YAnUElRi47MS5cy9rM0EzJm0kXiHA6OM-l3rSDvCjSU-6NYaxqfSmZii8VkSGBBhDB_aolIgWNors_mXoR5qmCSGBscvRrV6Gv-UgUgGxJjBtskKMSlTP6yl-pMIsMeFqCCejkUOXvhZR2N_PTYCtEeOt9BLfNu054IiZmtnDz33j97gFkGd4Bj0RQ-7EIpZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cffa11c70b.mp4?token=q3Y2AdUOwhrDPsT14nKVkn7ze0wCb67Jjam7ON1zN0ddZi196I5RyXz5zZP7qAy-dZf_A-nytecPsSBoNCdxNZWZoDlBqZX7AuKEhfnp9goROIsSZCJI1fug63_I1_ooMUzctoxxS8YIaoSP7_jL0YAnUElRi47MS5cy9rM0EzJm0kXiHA6OM-l3rSDvCjSU-6NYaxqfSmZii8VkSGBBhDB_aolIgWNors_mXoR5qmCSGBscvRrV6Gv-UgUgGxJjBtskKMSlTP6yl-pMIsMeFqCCejkUOXvhZR2N_PTYCtEeOt9BLfNu054IiZmtnDz33j97gFkGd4Bj0RQ-7EIpZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسطوره کریستیانو رونالدو در یورو 2016: از برد مقابل کرواسی خوشحالم، اما چون برادرم لوکا مودریچ گریه می‌کرد، نتوانستم جشن بگیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24825" target="_blank">📅 23:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24824">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ki8l7QLcC9tXXM3OA6UGVZJBQJOgrkTzuGooJDN08ZXon_UNdv732CR_8b-JO5ns2uvPT90PBaUP1zujX2AaUfkK2-LgZUtP9ICrcWNHHM59iP3H91cdtUHZzIgPFhdfMJwtEnqJPSJX_nU_oSS2IQnZRP6mtDEr6V4nDLe__DnBi9Stet5G23olFRVX52fPGmXBmoLHQuYg4wGMW0DJ7-dNu8UDl3G67E7Dv0K4VTCBLeopXN79hyJtY7biNMM1ihds9NMeRRIbnYr60Gz5ylX9Lhw1maO195L3QkHcYRQmEv0IrzRv12d32srgHJsrU1vtHn9rS_OTbIGkgw39xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24824" target="_blank">📅 22:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24823">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnza67Zvdr_f6pOBtBN2ru3tMp-r10t27MVa1UQyBZq2A-GU-yETi4RaSN1bt_sifk8J-BcFnqLoL4e8fpGvSihVHzEDGa8KGKw3K_wGf2qX6BQp3E3iR6w-xJuHlSrdVgwtyAD44iYXBcagAhZki_JmIlV6snp97XZiceSXRJYil_tO9eOqeRXGi8eGZIJKqw7abBqTKrwqObLUa1oLGpCQ4eN8kJcgz_3yGA8BvPTWBl5NIoxQvFX-5uF4p18Eyo8FQIAk-PF5vrY1ajnakMQEyBHOFeOevsxBnm8A5Co-4q6c03944DsiHfr_3wr3YnFXjhxqQ_1cJp6UQccTpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
مارکو یوهانسون دروازه27ساله سوئدی تراکتور برای فسخ‌قراردادش با این باشگاه به توافق رسید و بزودی از جمع پرشورها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24823" target="_blank">📅 22:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24822">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1pIeUEF0enxX1rt1nqI355HHpSJRIzVOTpxPOidZUxoLY1csc_L9GhY4lK71_XFFK7o-r8b-TPsqSB1pQ2zSYGf0JsHEFroXUIUB2EQNNDiSbjy9yTIht3npZC9ds2O0T0B9ZWra2e-QX3c4SjLkKUpUF1sT7aObtYpbz0LoZKbCQPidQeZ1BID4q8W1VFZYFFYDzt88wSCBh1XlUnN7jQpwKn8NfXW_pkY9UfWU7NzLgsoullLJLcEqi7nhi3YKMsdiM4X5Bg7MWvGMAaKkImwq-cforTQB_N9ZqB8ljOjm7ON56TkxNSJpM5FjBA0dfy0kadyD191CXswrBF2zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24822" target="_blank">📅 22:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24820">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyaYDiZJTmtq2rHSH_xJvH_mC0FIZAlbJaMf0dtL_oxdUOwBCeHeYyGmN5oFSjTNWFhSNlOG8_wvXyJGH5W_29_BjRrayiYjkW4-zyMi4LCPOqNbNifzSQrsU-6HQ04gU7BeEUJJhlQzu9O0R19WePJViML0jyFmiiUMCJXVAb3astvCMRccR9LPNttbOYDViXO82vMclqoxRm3PtdAZO4W4fWGvcPnz3EWnFx92m7aWQvDM_r-XxwpGPOsPyFExxC23X1tEBW_JvJbF3hN-eByYGHPJb7_I8L8yqWWbhi7Ub0RIyLKXA_R_t2Po4FQcqS4shmP6CQOtfWgfbO2bdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اوسمار ویرا 72 ساعت به‌باشگاه تراکتور فرصت داده تابه آفر مالی‌اوپاسخ بدهد. اگه‌پاسخ مثبت باشه ویرا بزودی بار دیگر به لیگ‌ایران بازخواهدگشت. همانطور که دیشب گفتیم قرارداد او با پرسپولیس فسخ شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24820" target="_blank">📅 22:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24819">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mhq67dpX3CzaM7_JesWn90yM9B4wRzldKVm4kG-LAcHoMIHFYNXaFSBboK0wF4EPg765J7shrobIHtclZSgPgDEufpVkbV03GCRJ0Y7CBXetTGXiF8VoAqMZxHqIxr4KyFbQ5vkXtf4Q1STrnZjtURO7w434Cru8-Hq8KbJHN8_rYnj_PmO7mkWqAL7KMP_Yj9bn4ZL0Tnsr03ii0d06CATqc8agW3J9dMpZR2FGVqMGVuHIcsHHVPzSE29ku3xYjuDGAQXwAOyijN1JXI-EZQ72MCovckpNUIN5cCLXPaozXFzJI_392uIXwUoS97thxSUpT_8r4DAUKxpdKa0NAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حجت کریمی مدیرعامل سابق استقلال امروز به عنوان مدیرعامل جدید باشگاه تراکتور منصوب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24819" target="_blank">📅 22:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24817">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNACSnL-LadAB_F7XYq9SUM8mrZaBX_8X7FQ2x7zZ6s9MwvxCVeu_OXXSEgwB8C5Cz0BzkQjPfWAsINQEUoVwkJCQ4h1Aj9c6-E2JvAmdjoiPmDR5E5mzo2GAPoTiun48HgHM9K7ycZDE8cFFwDFpErdZm-3WYriZGNDzlUewRLIDumHdPWGra2oetczpn1XdubA2-U5hpOkN-8Hjcpa_xfGo1OlIzNLIs2Hze3kibC0IacFHnG1nPaAKHsupd0iKE1fELqlBDUIJkNYMSOUf069bmjY7XEA8HT_IKDIq-BmNcoZAAQME-URLqOj9owrhLuLDTN93-K-fioJzk2lng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
امشب یکی از این دو نفر آخرین بازیش تو ادوار جام جهانی و احتمالا آخرین مسابقه ملیش رو انجام میده. شب سخت‌برای‌هواداران باشگاه رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24817" target="_blank">📅 21:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24816">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVS6VlS7xS2RL0fXGvRhWHNbZm999x5vT8-CA2U12etuxOvSP-D1rLr4AtA9lsc87nceZU4dAm8ixAjy8ZBR1vLu55U9Jfqt0MeylmNYSBnTWl2lY7pR0oe9ZDyejf8Vd-kugz8fFNfc1WIOKD2PXuTCZYyVJq7utbob3vKkjmf9UUiE1gXXjk0QZwv1sDmZTdNIoxPaXt5l0WnSa_9g-YwJFymh2gP2Nkci5i_Bt_Lq827S7uX9Vt2mAwiGHnFFsz_v2M13QQ7f58rlrnlRDMl8YDKMQeQmTMwSoubuOK2J5wDFEjPKGKbyCXZk5emWZQVXtZ37NKT8bYRcJuDbAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
یوفاقانون‌کارت‌قرمز برای بازیکنانی که دهانشون رو میپوشونن رو وارد UCL و لیگ اروپا نمیکنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24816" target="_blank">📅 21:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24815">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtSyxamjgceuZxWspcTQCMxBT28FPcsr6bfzzbocqvsJqw0mWOtmO2wvHiXAUlAEqKtDfPt-ckCMlET0P2NqHJ14KC7QNMUoFS6LNtnEG7jIt1VmAbBsHp6ZseFijsm98ZvJu6O6UEklaxGF0hrR9USA3Hp1gXsa4uQdJtt7-k9-3tASPXXUc38pGrAcpD_etMirIHNnhfKAvitbtaWXtzSax9lO-q2kEFhT9vbzBUsPX4sO11012qMilxQ097KC7jHg88g_qeYJVt6l3hQ5n6ewA8s5g-TIoZSMl18z8_Y_QpprOWKD8s83-N1W5pA7KmwB9vENIPC2JTJN9retCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24815" target="_blank">📅 20:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24814">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWsbaCYOTRXkpHOkQ-2yX0hGmRwuGlu10DrPnXVSHAXUDPTiKhiSIoWkju66dgh9tYr3WG329jI8GqXqqtEZMlkYl19hcdn0r7JkAcCv20XFMiUWYr2yAav4xFLKLLG5aXjdgZsKVyfeICIbqmyFSzSGH-0fMuJPiaACvGgbSQvyBRFsrpOhvwjlZqxO_ZDqEL67E5TU6tbKzbml03tm_JNglz9seCTNoNsX0J9g5ZtzlAt3QaBnQtnfrLRHRvajxzYb9oNtoKYb3JkCjQThDfywR3WGoMsFqFHnOJMLOWrYdeTy_Ea7XFzeEzjjLEiWeSxF49qYzW9O624HSpJ3fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی
؛ شماتیک ترکیب اسپانیا برای دیدار امشب با اتریش؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24814" target="_blank">📅 20:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24813">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBzm_CBQwO1ZZ1Q3vCnnm2AyuusMEMwo9Lo-IzpJsf6jYljSd-qC9CgDXn3fgP8Jq4FVomq-bzqLOIce61HJSp72PEIVTVPfCzeOPHFhn7BeUK6utjQeF0aUIBPzDD2-_s4Xg4mDpo4hSiBETyV5dsVU2yTE0A6s629CeU0exIeHSKClUWIs9Pt7cwiy1Lk6yYvvIaqIsqX7DT8H37xJjalk-R9NSLCQDZ8Z0Hcejq1pw5MxxBe3w2gWkcprRjx57ueI1X8qOCHu6-nLn0pw-RASfsnH4-05xz8kxRuWlZYmgh4MN8v44TkdurXNS7kKIACQ09ZMCdRcAMZKo61jVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
امید حامدی‌فر هافبک سابق استقلال با عقد قراردادی دو ساله به تیم فولاد پیوست و قرار داد حامد لک با فولادی‌ها نیز تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24813" target="_blank">📅 20:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24812">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucW37_-mOPC51lPp7kUx0dOm_RYXh3x7SWBjjU6BOx_7WSFa_SG6_JPwpD69kPoZwKgo0buJ5Hzwp1emUgVzMk9g7U-wFhj7N5XNgkmvYX1ea7uaWRiy61LmJiKRzhEzcYfodZC9jyLfx1fKgHZKRldSJFeDzBt3xtb5J0clPRSo-0LmqwtYsPcIk1nIR5alAkcUzaaG69lvIODiQx4DPVwMQnw-OO5jy3ly9KX2LOYJwKKmXDOwuB8qaTMAXrJD_jwB3KiGRinZYXCGM8eJDzoLHr791D7In3CaHyQ_mQNWBPt6X_v_HJnvRrcvLll9ilC14XlElZXcn-PYDkVJBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نتایح مسابقات‌جام‌جهانی 2026 تا اینجای کار تا قبل از شروع رقابت‌های امشب مرحله یک شانزدهم
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24812" target="_blank">📅 20:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24811">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-ptwoBvrCqfjYMJpWqEX5JBkMis3vsegzpDliH3e1pL-jGew2NH7P7qNGQ-yoEDgcZo9nLZk_iqDFxoyu6AkH1PJcm-MjAKwe2yb4BQ7LvvuZ4G7djchOzUVm3Zgoz8MjPe7ryK5jnYak1VkACh_qKGDnCqRx9tLU3GWSNBo1AXCz2J84WrIQK5WQzcxpXRgX8kid-FynRccT1860pZ4hfxMOY2fgVRuyZyifyHsWVQ8qZLVQu1T6lpwTdibnee4rMHv3q2T84my-IlyqVjEXuGzsw3ciSdTcAKYfBUpaVUlbgNc2TVGEDjMYw9aoidhc3Sj73SZb_ZvPt4Qef3RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز کریمی تو پخش زنده شبکه ورزش: تمام بچه‌ها زحمت کشیدن. آقای قلعه‌نویی گفت خدا سر سازگاری با ما نداشت و ما ۱، ۵ و ۱۰ سانت رو تحمل کردیم. حالا اگه به قول شما لپی بوده، مال ما لپی‌تر میشه؛ ۱ سانت، ۵ سانت،۱۰ سانت رو تحمل کرد، ولی ۳۰سانت رو دیگه قلعه‌نویی…</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24811" target="_blank">📅 19:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24810">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVqyhrVyWz8drwbVF5lSorEJJu4Emz6xJQ9sG9gn-BLhXSgOAm6zgnCebIo2psQiR6w_ezGJfSao3OAM6ZMqDA5tAfkatjfK4bGHa2-nLKHAHRamzfqw2hHSXWUWqt6__7oBIuJR9nGQyz_IwXg44WcP_2O_G9HXfXQhgOYROaT8mrrw0NUwUavOg2B3wRzFtcqSdTTwEGdNgF7bl8P9_9RitlrbGW8MUSBXn0MskcSv28eIy3O2BcWbENr-KGK-MhJ9pLSUm4tO7nlYe8vg2vlkn-CiA2_boKToragor5E89xD_hcZpWv9wwoSIO_9KLwniCYTXrhHLdql-D285AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخباردریافتی پرشیانا؛ باشگاه پرسپولیس تا پایان‌هفته‌از دراگان اسکوچیچ، مهدی تیکدری و کسری طاهری سه خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24810" target="_blank">📅 19:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24809">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tm6Sa22OYnNrc2POrakY4F9f21nt2U2bZxdfnB_-FcafoHMtUxgvipklfqLwW8rmnU0LjcKf4wlN7c8woKCiQB_z316xOMucLvWLE86ZagCxvtIENDEYEh_Go-I6yrSA5FW143Q63JBHpJcTOe6L90Jf_37NL9zaY0-VUEQMsEkfcNWrB2LVGHX5ZIKwG9UlCqxKBoWEZMS-wYVUcLkDDOEDlmFtLARKtERf4mof3KEKpzrNFEDHqhlqiQxo-hThKt7KsnX3qzLROSaD8vA0GVWBw4vzAcdOHx7P0rXgnSB4LstYFfuepKYa2MKQcA4-otvuUQQHGB6rplec_mIQ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛ نبرد آمریکا مقابل یاران ادین ژکو و جدال لاروخا مقابل شاگردان رانگنیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24809" target="_blank">📅 17:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24807">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gKZFtTZ1kD6mbi5l51aLXa-0Ika7yL2GbFtSF0O2tCbfPpz-zQGJRP5KQ7XIIvgC4vlkqtbpHIhAM-VmBHyvw8s8naW_szAmtK4anGH0YPAO-i0IDIcoT3vnlPdg9mVQiA2K20jMbzkEDzWV_jIawdAF4WUFUp12w1_x2Ub32zNFlp6VXYpjyfT6eF5Mb37-T2LvWEGk93hzeQiv4i1GyCrt_ctiNim3T6Gpx0zvCH1jsxNYK7TNH0yAyRZoyIgaELikxoqm_tQi9Cyq26cs7FhQr_sKj8-l-Zxh2eA938EAHZDPSsaGanj86ax_KVb1pFom_w3IcE3IqXxJSkpuVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/otmDgN7_Q2jo-Dw8MI7fLcJnhAPa4-qWiOBg9YMFDkq1C5vwLfuQV_30OufVO1MerOArhcWYnzTcLWvH00Tfo_BNUT22ZJBBByjat-Qggq7_PE-sw8Lys7QIeUG9X6AK2uQZW520FsgrzpiAG8hDz2zkwSkxpMbXTsZTAYQ2TfCXPA-LCLmBYqQd8IXSDeyQJ1bhIHq0z6wo1jmeDKpBAUFHx2C_SKl2tmyKfFKO1arP1j8yksY_mSeYsfblkz-zlsp2ogtJooSXFhRBdZ2CcbMp0pXx--4gCuSHsE04tL9xlaPZAmEvkRTcx0Csid12IT9efz9NDuMLBQXrIfi5XA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟠
امید حامدی‌فر هافبک سابق استقلال با عقد قراردادی دو ساله به تیم فولاد پیوست و قرار داد حامد لک با فولادی‌ها نیز تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/24807" target="_blank">📅 16:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24806">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c080f226.mp4?token=rUaeiO0IIrV9cpyIjhA-BdWGRcKBu0XGmv2QwupWYCbbfJh0kWlNK-eDqawRWUNL53JAxbsfavwEmSJaTT3XFQdWPXQ953BsasMEghJfp8f_WuLI7O4cMHoeRsCVkrwSVbyUna__NtqqQayJLOMKmq34ERsBQr4nfC7kDYxmSRBSr-jpygst_jYve-F-GEOWOhRJ6NF1vWho6X1b8G0KAAczH2A2TS6t9_TBrRfPOd7qhfr9gJKrxI3O99aofnFz_kaL1volLB-5_O5Hjag0a0vnE6nF2yjY7bSiTfOBoAXmEmGiWEVBHn-xkb3nTdRux26LA1DQpuH-1gXpAi6kmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c080f226.mp4?token=rUaeiO0IIrV9cpyIjhA-BdWGRcKBu0XGmv2QwupWYCbbfJh0kWlNK-eDqawRWUNL53JAxbsfavwEmSJaTT3XFQdWPXQ953BsasMEghJfp8f_WuLI7O4cMHoeRsCVkrwSVbyUna__NtqqQayJLOMKmq34ERsBQr4nfC7kDYxmSRBSr-jpygst_jYve-F-GEOWOhRJ6NF1vWho6X1b8G0KAAczH2A2TS6t9_TBrRfPOd7qhfr9gJKrxI3O99aofnFz_kaL1volLB-5_O5Hjag0a0vnE6nF2yjY7bSiTfOBoAXmEmGiWEVBHn-xkb3nTdRux26LA1DQpuH-1gXpAi6kmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لوکاس برگوال ستاره تاتنهام به سرعت داره به یکی از مطرح‌ترین ستاره‌های فوتبال تبدیل میشه. این هافبک سوئدی‌که ۲۰ سال سن داره نه تنها بخاطر ورزش حرفه‌ای تو جام جهانی ۲۰۲۶ آمریکا معروف شده بلکه به خاطر صورت زیباش هم وایرال شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/24806" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24805">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjKDYZHsnFTdCV2sKLk1e0JjUsuFjec-wOFZYhxetP6qgnQ-yZNbpdMj4porljt2mg63JB4my0vONR3UxiKVT6fzu5r69kcMB0btCOBwMldDDnkp5QUQ2OPZgH9j0wuDk7dnpQOK9RqkHdVxMH8QWiYRPCjOzcbe73Xo5cnk-48oAP4R9efE3abV2GFzd0KgbH9-vBe4lJ1-VmgoLEwbK_4QDorsjcBdvG1WwIt_vUlNly1ezaaluYwzmJ7Y1G57Nt229_bDGXZZTB797B9QoVFIZF1dLySUXdJ7XndYkhvAIZN6NYQRO_eysZSm2clBRgMmeDGFam1d9pu42jxMSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین گل در یک فصل در تاریخ فوتبال:
🇦🇷
لیونل مسی فصل 2011/12: 82 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هری کین فصل 2025/26: 72 گل
🇵🇹
کریستیانو رونالدو فصل 2011/12: 69 گل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/24805" target="_blank">📅 14:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24804">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f01ae4b17d.mp4?token=faSlFM852r1jsYzwI5V3qNfkB1vemcWYfYj8ejKJzCp8XjH9xbptGZVjZcwSSRB8qvAMjj9NEBuKqCX48DI-v6QIfHKFFUzJCB4hafITST_x96dJzYdpyI7sGl9C8maPj-4PVxX251WGCi167s0lRmuHW2jImKAs1oRKkcuOaut4DbY8j7R9xTH2zhX2V2sNzcnPEF48Ur1iuux3lZmsBc6lGLm2ZQk9V6Gq6svgZEWL97P9IZWsayjabB1cl6UjK_uZ149qnZlBCWlqqJ4Hvs5Fr3m4ZgTy9URrG9M2L1MGh-0_aEDeBMBWUme3Ax_22TbnhA09MMm0BVbxhWG63g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f01ae4b17d.mp4?token=faSlFM852r1jsYzwI5V3qNfkB1vemcWYfYj8ejKJzCp8XjH9xbptGZVjZcwSSRB8qvAMjj9NEBuKqCX48DI-v6QIfHKFFUzJCB4hafITST_x96dJzYdpyI7sGl9C8maPj-4PVxX251WGCi167s0lRmuHW2jImKAs1oRKkcuOaut4DbY8j7R9xTH2zhX2V2sNzcnPEF48Ur1iuux3lZmsBc6lGLm2ZQk9V6Gq6svgZEWL97P9IZWsayjabB1cl6UjK_uZ149qnZlBCWlqqJ4Hvs5Fr3m4ZgTy9URrG9M2L1MGh-0_aEDeBMBWUme3Ax_22TbnhA09MMm0BVbxhWG63g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/24804" target="_blank">📅 11:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24803">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ektMl6AlP7QMhoUKVeD-gnP3MRBdGYRpPV23dIp-1llyORV__HAwX3TktcO-2TwKgFrhpCVIlc1O3Ya8loKx7fri77UXkDgLWDUlJ-gUYXL-sOnAi-ar_xbCaXHlvFzO58vMTSZ1fgD9b8HhqCS9Yfj0YPP39GIcrBiBojPztxb3pRTG9eBLhnAhwzAzKFg7pIN0p2q8chjeCaXBw8iU2iHqm49qkR_rTV-AiT3msLTO58UE9Zp2HjSCdwYcfLXaWIzX3MUmSXRXjbV2ktWp4PX6vHsFOXT4ZTwWUSahq9SqpNw89cyPYo20RbsQfdgx5tPKB77rK3Ppc1KQ4jVI8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
ظرف‌چهار پنج روزگذشته بارها اعلام کار انتقال دراگان‌اسکوچیچ به‌باشگاه پرسپولیس نهایی و تمام شده و فقط‌پوستر رونمایی و اعلام‌خبررسمی آن توسط باشگاه باقی مونده اما یه عده تکذیب میکنند اماامروز خبرمیزنن‌که اسکوچیچ سرمربی پرسپولیس شد. زمستون هم بعنوان اولین…</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/24803" target="_blank">📅 09:46 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
