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
<img src="https://cdn4.telesco.pe/file/vz7bcqj_oJXVCfvEPmgQELfxh4t-5QdLg4VcQ4emrlDbWIfuZX4Guzy3wnoZ2_qBKCdoJ_XkaEaiElq4d-lSZxiitRSNIJEZ1tNz9CCCyQy_MNbii1XfO9q4UbABREeYT0TbIijW_iEU8MZx75RiSFutgPju_glLE-2p-tFaDrdYg6q2eDk4bcCpsqcDdi63u_jnEabHngR_SWm3zLbgTJKoXHxT1WPSdglSu3O8Xt9cJRgcN78bGLCSfwKdrFc8ZSFHHs1tDviZB3M0EZ9gwbx3sGACeHw3SNJZ8WWic8CG1hX89q_7lKZO4oNihxEASCFf33Qq9koXB4y1C8xjpw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 475K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaaa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 08:11:45</div>
<hr>

<div class="tg-post" id="msg-31474">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39e71f827d.mp4?token=Ib8UKInIw_Z_-RAkkKr7c2gn1_x44JeAeK4leF95m4XrQRzgHBjmpaFthMnTQJg698RM_IoVlCOhbEZivBOfma1D9Pw9J_cpKCqiDEdlZgcfxDDq7ryrugss8JuHtOxpBTbp7u5F6HR0rHDvSneV-GDXP3YdFDQTayB0aDwDIKczGspaSu4Tb4UhyIXsS4dUURAfO00T0_jtt2d0Ulw83IVasOuV_3hSyekAOyLGfoNds3VKTtOt27xeAgCLONwXF9l2gi0bbmQ_19U5-z_XZF46pJIT1JPr0rDahMHEywN-uBPQhiE-nClggY1prkYGL-_rwo9xxs8y-9Qzp6gFknW5kySECJz4URdwXUNB3DLQQ5TJplnPL7PVMocNbx652HIPgOTksOyzc82pt0t8K6tzfiVmnG0i6TpJ3PswafAAeJx5WW-E4FgxDnD0evakOizmNfwUUoAyhP8VPeGX5P2zdPEjCaSVcVAkGyRt3JVf5bJfuS6dE2kipmS2QIDa2dZP2-kG7U8z28L1_GsLvWDAdSrUm1YoC6e1WAsvnQXjT0LefWg0C4m6gNW77eiWsFGiPhDz8iUe0Jcnr74tAWwNE7bJOEVuoKDEf0vyb3OkhmcJ2UhmKqExtoyOy2m76NhmTlK_GnOL181K8-CpsdLJwU1TDU8SE9n3AQHcBxM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39e71f827d.mp4?token=Ib8UKInIw_Z_-RAkkKr7c2gn1_x44JeAeK4leF95m4XrQRzgHBjmpaFthMnTQJg698RM_IoVlCOhbEZivBOfma1D9Pw9J_cpKCqiDEdlZgcfxDDq7ryrugss8JuHtOxpBTbp7u5F6HR0rHDvSneV-GDXP3YdFDQTayB0aDwDIKczGspaSu4Tb4UhyIXsS4dUURAfO00T0_jtt2d0Ulw83IVasOuV_3hSyekAOyLGfoNds3VKTtOt27xeAgCLONwXF9l2gi0bbmQ_19U5-z_XZF46pJIT1JPr0rDahMHEywN-uBPQhiE-nClggY1prkYGL-_rwo9xxs8y-9Qzp6gFknW5kySECJz4URdwXUNB3DLQQ5TJplnPL7PVMocNbx652HIPgOTksOyzc82pt0t8K6tzfiVmnG0i6TpJ3PswafAAeJx5WW-E4FgxDnD0evakOizmNfwUUoAyhP8VPeGX5P2zdPEjCaSVcVAkGyRt3JVf5bJfuS6dE2kipmS2QIDa2dZP2-kG7U8z28L1_GsLvWDAdSrUm1YoC6e1WAsvnQXjT0LefWg0C4m6gNW77eiWsFGiPhDz8iUe0Jcnr74tAWwNE7bJOEVuoKDEf0vyb3OkhmcJ2UhmKqExtoyOy2m76NhmTlK_GnOL181K8-CpsdLJwU1TDU8SE9n3AQHcBxM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔵
👤
با اعلام مدیر رسانه‌ای باشگاه استقلال؛ مصدومیت یاسرآسانی‌جدی‌نیست و او به دیدار هفته آینده با گلگهر سیرجان در هفته نهم لیگ برتر میرسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/persiana_Soccer/31474" target="_blank">📅 02:06 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31472">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDeT6wwEc4tDtOa5oMqXasnAVg8rItE7MazqKF_qMBxl1diA33wQzM0_J2Kr8OuRxc686E2oLlxLiyuA5bBC4wPR2I_HfF4br9rSzijBNZkTvwaus4SKsQEDB5ua2OavLGyg10TXt05HlnCj_WgPL1RbZH9D7z3naDhq46R5PDb6YGSlb_V0m9o9_kn4NyH4-17pnCAEpI6zwJJVZdc_pxb86Rt_B39qU8uTF1DsP8LqSTmLwKdMOn4vqBVjtssFNA7s-xUn4oL7FG3qbvS7zGznzdN-zMyJZ4HVfywPbS9zUE0sn4mcYgNK3kUqMOOq-GF55X54JT6dytKeNk1pnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ نخبگان آسیا؛ دومین پیروزی پیاپی شاگردان بختیای زاده در شب درخشش یاسر آسانی؛ آبی‌ها با پنجره بسته در صدر لیگ نخبگان.
🔸
الغرافه قطر
1️⃣
-
2️⃣
استقلال ایران
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/31472" target="_blank">📅 01:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31470">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5UEuy2wCLtSXzguO6T9o_C9IAs-LzuBdy2OaWT9b5KcOAZ4a-89OdKk1XwzMNCBqdzU_f3LOkQWdU5KFt7uS7pWY-Zl8eAhbYIt6bLgVVUTx4lHlzqO_1A48MNAjhJjBSlZd8goHGipuL3NfaDRB5X2ZheWO5hbiHTTGxBDUuP6y42Q08HEwJPKoKALuh3-GhFq7IViYCuH7qJqEaQ0WnlHX5Jm8fTu7-BOfgGeD8vPT5-RaT0ffc30tLLU2db6t7pZq9F716wT50Mb1_sx2IJLUzdgg1gK-r1cJPBHmubVxMMT3SeWVUMxycLQWhYk5CU2wrTOgX4w622TAl0Wlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز
؛ از دوئل تماشایی شیاطین سرخ با شاگردان سیمئونه تا نبرد بارسا و گالاتاسرای‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/31470" target="_blank">📅 01:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31469">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_5-EmrlnwQPFai0qH7MLt0ywoO8rWCgAQjOmQ2xxtzVF49gX9KyE9Bwe0fabvi-ggh1bx-k1FvHmM5WTaCCJ8mX9Po9imNhOa_RCtsclvYyUA3oLNq0OwEtHx11KYimTX6hX_DcARwlSwNs0bvPb-nNtma2LbtK05CzhBsqjZMNUSRCTlxayIoY0gKw68ScyxTVHriXex_R_exgLsxeOAv27vi3MK2j_qVuy3RVHKcWRbKUJNfd-CgmpchYtNJzAFgcQ4tZp2vBHol-nPAoXBFdPJuAvIby8T5pWw8B8MIEhQDgj7ifUe1hraZHhzqeTlWKSbcM1F0HuZJpotN5ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌دیروز؛
دومین برد پیاپی استقلالی‌ ها درلیگ‌نخبگان آسیا 2027 با سهراب بختیاری‌زاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/31469" target="_blank">📅 01:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31468">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cd2361427.mp4?token=cnGcICsuBWHAYLHYc4dOARmGZLxIcmbB_ZbROmgZT56J0qJjgNQV9zKhu_4C5cotwOHzIxi3pQXJJD6Fa9iU-uUl7VDQCZxTQs-dN3gKARiXukDHnAxJ2miNBZ8tCyoDK4tl-X1bbuariV35Az1izYJ7Y3IqS6NiUC6LXYbxVVQdua0MAqVap2cFJbtqyG0rdcKiX-DH76Zr-T9IgXt7-UscLnLSw8U2X-KemGO_tOeiV64-BIBfsC_LZXnwO2aV8AEXqEwJUBv0LZXE64ZBAowUi_jLAi9OH8UW_UZ4xNnD3XfG7aN-NXIulswdr8IFKop5cUlQ-JZvcDQrBpdGAouHdTVO7i7qfrzImsegnVk_Up_oSz_m5IdO-pDMOTXyN8u9RPTn-YtYNQhUwQnmX4ObyWdN7Y0yNtWoK16ehcYMYvEp4X0Js50pA_aYo_9lsQScavV6H1pGCc4L1BilVUpyxWaF34TiaG17nC9TGMYz4VbFFXizfRtVt_siMeO5ClBewXVeU4f9JaqNigchy7TUFgdFU7XqhZnRJhfya-A0QnPJ7xPh48RKAUOOGMk8Z0XRjBBirElIr8EsjO_4qFkv1w5sDCJklDtR4ljkE_cHrSmPld6YQrsTwBXkwdj0b0jtylUIAR4y4rEvCFCSpxhIfAhtZQmiX0ixEBcfjto" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cd2361427.mp4?token=cnGcICsuBWHAYLHYc4dOARmGZLxIcmbB_ZbROmgZT56J0qJjgNQV9zKhu_4C5cotwOHzIxi3pQXJJD6Fa9iU-uUl7VDQCZxTQs-dN3gKARiXukDHnAxJ2miNBZ8tCyoDK4tl-X1bbuariV35Az1izYJ7Y3IqS6NiUC6LXYbxVVQdua0MAqVap2cFJbtqyG0rdcKiX-DH76Zr-T9IgXt7-UscLnLSw8U2X-KemGO_tOeiV64-BIBfsC_LZXnwO2aV8AEXqEwJUBv0LZXE64ZBAowUi_jLAi9OH8UW_UZ4xNnD3XfG7aN-NXIulswdr8IFKop5cUlQ-JZvcDQrBpdGAouHdTVO7i7qfrzImsegnVk_Up_oSz_m5IdO-pDMOTXyN8u9RPTn-YtYNQhUwQnmX4ObyWdN7Y0yNtWoK16ehcYMYvEp4X0Js50pA_aYo_9lsQScavV6H1pGCc4L1BilVUpyxWaF34TiaG17nC9TGMYz4VbFFXizfRtVt_siMeO5ClBewXVeU4f9JaqNigchy7TUFgdFU7XqhZnRJhfya-A0QnPJ7xPh48RKAUOOGMk8Z0XRjBBirElIr8EsjO_4qFkv1w5sDCJklDtR4ljkE_cHrSmPld6YQrsTwBXkwdj0b0jtylUIAR4y4rEvCFCSpxhIfAhtZQmiX0ixEBcfjto" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تورنمنت پاییزی بری بت؛
5️⃣
🔣
1️⃣
میلیارد تومان جایزه!
💞
🃏
پاییز رو با یک رقابت داغ در
کازینوی
زنده
Creedroomz
شروع کن!
🎰
🎁
هر هفته
0️⃣
5️⃣
7️⃣
میلیون تومان جایزه نقدی
🧭
۱ تا ۱۵ اکتبر
🏆
جایزه برای
۵۰ نفر برتر
⭐️
هرچه
گردش مالی
بیشتر، امتیاز بیشتر!
💝
بازی کن، امتیاز بگیر و برای جایزه‌های پاییزی رقابت کن!
🎉
📱
ورود به سایت
👇
📱
https://ikruyxysd.shop/fa/affiliates/?btag=914641_l303106
📱
کانال رسمی ما در تلگرام
👇
🅰
20
📱
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/31468" target="_blank">📅 01:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31466">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fncymc6f0AMP8LavY84Dbxauup_dSwqWJcRzOqBU6XrURoXvEqU2L_qNWHh8gpzMInRBk8edU3J7hOC3AzZZrIBqhpFhxPg7LRwhcZqfcYn9fHlX9gX6n734cguuMFisAleGXKfr96DvazP2ynen5nvGRkVZxemZWuRLPItEGfWUG-F66l7gQL-V9i6-WmDuRd-b9b8TZKEpCRrqtlowbT3FAiC3b8b_jBcX8UF7KqZd6YOfbpiRa2EWE0zGHdU3untTlkfCz-XFXxwompq8FhN7ixJUnwdAnpjTr5kj3M8gZ3lPkHYd4R08OnaMGvrkqw_SI7OkzNbRI0W4Vz0P8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gqJ8Ni3dqLXMhgDAjdbdn0MoWjzWFikAmGRxE4rQG9x8j4NQK3YceNWfqdLVzkkjM06i5UCIgRja2GeR8X42KulU0VghFMryX2DTEmOo-8dCVuOHxPmnhxhB7mP8eaEH-mk7Rx2VOeBOV9ew3rnZOLvnDehih5iiGZ0G7heqn0gibotXLVZBs3Jd7f8HwKZwI9jg9W9PospK27ETLF-0QBAe1IPitIM3cprC3uJl_R-Hh6VV3qcInbyS8RRDs-ETdn1iNdZ5KVGKIKWIT6og97DvGUILmbBlhrOXYuIZ9ld6dqJyc1KN7FuiYsk_7IkFeguW6BvMeCdCuwp2AQFgbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌دوم‌لیگ نخبگان آسیا؛ دومین پیروزی پیاپی شاگردان بختیای زاده در شب درخشش یاسر آسانی؛ آبی‌ها با پنجره بسته در صدر لیگ نخبگان.
🔸
الغرافه قطر
1️⃣
-
2️⃣
استقلال ایران
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/31466" target="_blank">📅 00:57 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31465">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWPulRm84wbDl5fFXIU9peD5Kjkm_MZZmJ6z2y6Igy7GkPEYS2sP592Zm7WKuuJKifQQnS0p0bNHO0-4Jud-v_ATIbKkPe0lWGUWImOEsjCKitPeL_Sb7ltUOA2-pYAuRhR4Q09ni3x_ZEWaCGDFL5vlLfYAAvRp0rT_A0_6rnhmBI0uEUNuYt05Z3-KZ_zIqelXXIuWkdZjeI1Oh_hbZahpUszFpudIFx56dNvWThsecGcK4l6fn1uyBsy1HbXKoeIzcwfDZwukfBtQCmNE4CIRvbAA8sSGiuJCNh3_uJAStqyi4697P8H9UU72NJyURmsW0hgOPgtvjo1CQWpCcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
👤
با اعلام مدیر رسانه‌ای باشگاه استقلال؛ مصدومیت یاسرآسانی‌جدی‌نیست و او به دیدار هفته آینده با گلگهر سیرجان در هفته نهم لیگ برتر میرسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/31465" target="_blank">📅 00:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31463">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nejheCOXBSpOX5TYNZLObEfiQKmSzxeQxV1W49T0HQb7qQzNfDwGwoxKKLt1iez1oVJVCMq9D-kcwixE3u916ZFmnJAfKD4PZYMLldqUA2NimDPDGgcIfquG2FiK8KsU-C8nmMu8tF8u2VSbnOU-00NzFtTF5g0IaWekWzCPjw9M7Y8xT7Ium2zK4IuUYSXkk2q7h4hivGJWCyTgDsvs7HXVPTDP5a424LOwVrfD2TwSLKCZ7K8KwSPyMviDUgodS70ldXozwyi04KAy0oAyPdLBCm0FLZiP4zYUclkGG3aBZkvBwLhVZclEzGVIBseVLyu5yM1DbYxRMJ0vVbV9MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
#تکمیلی؛ یحیی گلمحمدی سرمربی دهوک عراقی توافقی قراردادش رو با این تیم عراقی فسخ کرد و به احتمال فراوان با عقد قراردادی چهار ساله سرمربی تیم امید خواهد شد. فدراسیون با افشین قطبی برای هدایت تیم ملی امید به توافق نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/31463" target="_blank">📅 00:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31462">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxJrW8rH_T50g0HC2UMva62j3GO4KU8kikQT6OAqwVsI8YnFpNYqsI8jr1927dVwrlYQRTo3vWv64nQXGXloXxhcuf9nRRyFhTGzhCKCvKsAzpa1e4-wrUNIoXNIKjSMbhCVNmJTP-BUyUjgXTDCRunYiJgZIJcgFU_0vHDlJFonXZRVvlIqE-d6s7LoI4LcGIY1CBKS3LLoqEshAzH3Enh16He0DOoBFMAWhTpWJ2tgKg0PRhpPIDrrVd8eA8Pyd_g8COx9wJuPrI4hwxFY-Zvt5XAUTIj8SCQbPlHh5aEI76tlYLpHRkyvn4HDigH0JGKz-pDR2DMkNuyFazy4cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگام این چه خبری که منتشر شد؛ آرجی میته، بازیگر نقش پسر والتر وایت در سریال بریکینگ بد، به‌دلیل خودکشی در سن ‌34 سالگی درگذشت.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/31462" target="_blank">📅 00:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31461">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e66d7fe407.mp4?token=qAieFIX2L1x1xdNvNOX3MDzwtpRIjO74AdFVIZWQlcGqdOU50887vkOYOVCzHZLUcYclMT0T0eJ3edZOnZXvnY12LKuQj-cKwk82wJcQY6T8F9GJGRYpFDdorddZwY8BvGe204eaeRssUT3JpY8x5MYjzASVdUaDQjp8t08367ktL0LzE2sLaVEyyHz6fPUn0bYtBisMouWXZKV9e_IBackkxfW9J6UehpJ4uzjq3ofRjQoDwajiHD96OvVo7aUeQotwGx231Mz2peJx8-1L31gx2wceztcuzoiIV3nK06L4KET3fm5K8R5vMIKp0TRhaLVHer_dvjjHLoXWbq_Sag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e66d7fe407.mp4?token=qAieFIX2L1x1xdNvNOX3MDzwtpRIjO74AdFVIZWQlcGqdOU50887vkOYOVCzHZLUcYclMT0T0eJ3edZOnZXvnY12LKuQj-cKwk82wJcQY6T8F9GJGRYpFDdorddZwY8BvGe204eaeRssUT3JpY8x5MYjzASVdUaDQjp8t08367ktL0LzE2sLaVEyyHz6fPUn0bYtBisMouWXZKV9e_IBackkxfW9J6UehpJ4uzjq3ofRjQoDwajiHD96OvVo7aUeQotwGx231Mz2peJx8-1L31gx2wceztcuzoiIV3nK06L4KET3fm5K8R5vMIKp0TRhaLVHer_dvjjHLoXWbq_Sag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
پیش از بازی با گالاسرای در UCL
؛ یکی از خبرنگاران درباره‌وضعیت‌فعلی رئال از هانسی فلیک سوال پرسید که اون‌هم‌عصبی‌شد و گفت امیدوارم بالاخره یه روزی یاد بگیری از این سوالات نپرسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/31461" target="_blank">📅 00:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31460">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5AHuwwzx13OZhLwWHxe2C1qSCD1eALalOp-LX1Pptff2KXQocvFOeblfb5WPMp78jPDlJy21Ox72_hYZeJkCVkvKc5-KOoZzRTwdGtVC7pfuW9gnE--Urka0DcvwOgRwDFFA2MqShmm6ZvC_VcDYccAINq7K8tZFkSCbeOjrijCHKz0D_QQb3NzqHmO6_8ZncgXXlbfGEydlzDQZpiQmQnGpVYlV_U8xa7CwVWIkEylZdnu9V-qndeZCdDuWwoV_CqQuuMIBo2uljGW73GY7vyhO1MsHwlW160Nkm-RUZBc5DIcpmybHI4Gpv9m3yW8r1I70eAJBEUGFTBEO4coew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ یاسر آسانی لنگان لنگان از بازی خارج شد و بجای او محمد حسین اسلامی وارد زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/31460" target="_blank">📅 00:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31459">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxpdQzf1dypF8aNLIVof7bpV052ZIQ3V7X0x1h0M12LVUytf0P9jZJwLpFqWhLB33dOX45vsW4azx-bInmUq-O06S2k7MJQz-Ru2cA3KUtKnXrMyr8kKnXeKqY--TfiLo1aVCBd62tMMktJcHQGZxgGWQWdBjHg23I_WB_0VvwilnVUTSyqFZ_vEXG7cJJUp1INjZ4bXWXPzhF43F0lsTUDpkInOOEgYg28V9IHsVdg3gk5eHhih9UvpdtmW8GOK77EcY4DLi-SUKlQLo-INISPPCZlrFwZAQUP-9hRADL5nzteo0-AeHzo8f0B0MaLPzunG0qvWazhq097jcdDexw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ نخبگان آسیا؛ دومین پیروزی پیاپی شاگردان بختیای زاده در شب درخشش یاسر آسانی؛ آبی‌ها با پنجره بسته در صدر لیگ نخبگان.
🔸
الغرافه قطر
1️⃣
-
2️⃣
استقلال ایران
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/31459" target="_blank">📅 23:51 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31458">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3N2PB7AtNPASFNzdFCSDj5gk92UZP0s_CyJDrahxOT_GHxU_kxxA8D58FY-3LtRdvKgmdSPGL4lgrSz4BeHGWYtSUD-5ZLAd0O22jKwsX2iMuqL2PrmUhDziag9SJpaDoVpFsvW_M3OChs1gKZ7uZoI7Hyjqx1ijA1Rs19cvWi-6azrE4gaLw5BypbKyfQ-T6MWM1L48XqjXV_HGyKjMQzFw-n4Y3MtKE2jRZuhqrRH_x8Q7vQBi8pZAQWqPCTD9OBGHWrvaqrm5BhC_tck74hupd724kvusPTlrPBGRHeusndL90S9B3DdQwtmUUHouJkyjJP0CIX3lWkrUSwJwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ یاسر آسانی لنگان لنگان از بازی خارج شد و بجای او محمد حسین اسلامی وارد زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/31458" target="_blank">📅 23:48 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31457">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57855f950d.mp4?token=O6O0PAXclniuYcfiZRb1zVqgWVkK_hbmNBJlmbZ5B3Yswaoci2JTbzwtcIFjoB-3F9uwhzevzRo5AE8-c6MKqtUPA3tsg18XrYm6nNViEtJo4CBdMUs1f3qQHjBgEAiZB_UC91S0ymch3lysFHTMYEMcDuE0QZthABUMkQla-JjsINNzi4TcszuboxfdibQUh44Ao9Lxs9Kbx-6Ene5btvjvHWqHz7Mjj2IQJO-HD6NPZ6LbZ282txy8bcqtiL6OyQscREWI5s1YBh8IlZrlpB56HE1gh3g5ucihmbsn71KHLSh0xAv9WOUwMy1DVPcDeq6y0cbe7uX8Sz8PnLPPcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57855f950d.mp4?token=O6O0PAXclniuYcfiZRb1zVqgWVkK_hbmNBJlmbZ5B3Yswaoci2JTbzwtcIFjoB-3F9uwhzevzRo5AE8-c6MKqtUPA3tsg18XrYm6nNViEtJo4CBdMUs1f3qQHjBgEAiZB_UC91S0ymch3lysFHTMYEMcDuE0QZthABUMkQla-JjsINNzi4TcszuboxfdibQUh44Ao9Lxs9Kbx-6Ene5btvjvHWqHz7Mjj2IQJO-HD6NPZ6LbZ282txy8bcqtiL6OyQscREWI5s1YBh8IlZrlpB56HE1gh3g5ucihmbsn71KHLSh0xAv9WOUwMy1DVPcDeq6y0cbe7uX8Sz8PnLPPcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بوسه کریس‌رونالدو روشمشیر و درخت نخل نماد عربستان سعودی و ناراحتیش از جنگ تو عربستان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/31457" target="_blank">📅 23:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31456">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SECyobBr9r6bbk3Ciyd7QWYWP3YRq48g8HU8aY_e9TIfFp7bBULlWS5v9U008ri8zlZHxZIlGK0nPSz3wcBgZ13wCvPxsvSmyofzLLsyZzlHRdEd2nA-3RxHj73deCBCCkOpFstJb0GS_mvMlifvSI8aq-MWTCT3rK3QdRwbNx2sUA8uFpPOn-4pOiyFoaWE-j1Msdi2ikEoEou6cinP2SLBuGN5H7BiK-l8kJS-_YvuardAGLHIVmrkGLCrh4EYlqLXbL9LQiH3BeLlt1lUYwd5WnI8HpL4_KJrEgFwvESDWncxA6aRtGLHGDkavq3KHfbHsvSVQIU64rjyI1a5Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ حوثی های یمن: بزودی تمومه ستاره های فوتبال از عربستان خارج میشن. کار میکنیم که عربستان نتونه هیچ‌فوتبالی‌رو درخاکش برگزار کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/31456" target="_blank">📅 23:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31455">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad69f494fa.mp4?token=O7CkHsygwXwdSAE-gh88o1Y76JQRkZBBF28zOuRdWV9K0d_BX95WiH8W__LhDlQ-cpKL78dw9S0Jsx23nxw4TgPWtoCrpN4i5Af7aFl6T7z3s7eM4cOEm6lKSzlJ2YLR7uSa9IWitIBapQ03eKDgMU9v9qroWHr5OY92PwzmkeJ4x_ovutgdS53mCsx0mlQdjzaJ69bJmZC8hOWTK0Gw5W74ywW58zrM0DeRRf7DsAME2DVsjipd7J_ScILH_SHnB2cOiJFJSYlos1__ulmH1gQUvVfpAl9lkwQ2dzhHCTzIFmPLmeZQIvUwYBcTrPwNcFd1WUG73erDNwL3zawTkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad69f494fa.mp4?token=O7CkHsygwXwdSAE-gh88o1Y76JQRkZBBF28zOuRdWV9K0d_BX95WiH8W__LhDlQ-cpKL78dw9S0Jsx23nxw4TgPWtoCrpN4i5Af7aFl6T7z3s7eM4cOEm6lKSzlJ2YLR7uSa9IWitIBapQ03eKDgMU9v9qroWHr5OY92PwzmkeJ4x_ovutgdS53mCsx0mlQdjzaJ69bJmZC8hOWTK0Gw5W74ywW58zrM0DeRRf7DsAME2DVsjipd7J_ScILH_SHnB2cOiJFJSYlos1__ulmH1gQUvVfpAl9lkwQ2dzhHCTzIFmPLmeZQIvUwYBcTrPwNcFd1WUG73erDNwL3zawTkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
قطری‌ها خیلی زود دومیم خوردند؛ گل دوم استقلال به الغرافه توسط گودرزی در دقیقه 60
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/31455" target="_blank">📅 23:21 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31454">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c059d16e2.mp4?token=UdHX3MdcRWlzV6wScK81jO1TAlxT_G1hGDpDW-hh6XDEESOMhpvt9ryaIE5pOI5qp6dApEK0qAf8raBQ04yMIQyuIUcargimtoTGp0YBmpfvG74MgLRZw6Ec1SMNCDqKl13WkNcUyo1wczs0A0Orgh-tn6cU2XxTmeWVCn-gm2Z3tV4iSY5s8H51_PTJofCFAIwZ8dgl9LGX5DLjuOJg-F0G39zMVbFYw9vuYL-WJAMdWDBR-gC7-FhSwz4GkwrCppuREWbEqW01kWBjFUSZcvzvMS82OWRm82eC2M4lmv1nZ7Ek6JDbMOGWhTA7NHZ7_gInBHaKQWy-WjEbsQ9N6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c059d16e2.mp4?token=UdHX3MdcRWlzV6wScK81jO1TAlxT_G1hGDpDW-hh6XDEESOMhpvt9ryaIE5pOI5qp6dApEK0qAf8raBQ04yMIQyuIUcargimtoTGp0YBmpfvG74MgLRZw6Ec1SMNCDqKl13WkNcUyo1wczs0A0Orgh-tn6cU2XxTmeWVCn-gm2Z3tV4iSY5s8H51_PTJofCFAIwZ8dgl9LGX5DLjuOJg-F0G39zMVbFYw9vuYL-WJAMdWDBR-gC7-FhSwz4GkwrCppuREWbEqW01kWBjFUSZcvzvMS82OWRm82eC2M4lmv1nZ7Ek6JDbMOGWhTA7NHZ7_gInBHaKQWy-WjEbsQ9N6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آبی‌ها گل مساوی رو از قطری‌ها دریافت کردند؛ گل اول‌الغرافه به استقلال توسط فرجانی ساسی 48
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/31454" target="_blank">📅 23:14 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31453">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1448a1396.mp4?token=fA4lDCqMvM_9unh_g6FLoSZtjDSBo-HgkMU1qfgLvxzrXo2Q4Jg86A-HdNJH7_l1a78j5bbwFLPhQu7wpsrbOwpEpnpITQnsdjKhl55PN_FhCVFNY2aPaS9pCLvXUhxpvLSbDOhoOSUhLTC9Wvv1gDKJ2IuMq0Xss3DaZnqbgmVh91-DZAPpCMX-w3f_wIzHdaqH8tYZxkby-EUki8jWnLRO_f6eH0jkXj33uSZH7-K65wXkyvP0STb19FmF3W5VzgHg0LeWJn2w3ap4LCAB_df9_RW9cFUtdvIq2G_tSavte7BySTAl2uQhbv4yy5sbVneS1barOsGjo6hHKsQrXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1448a1396.mp4?token=fA4lDCqMvM_9unh_g6FLoSZtjDSBo-HgkMU1qfgLvxzrXo2Q4Jg86A-HdNJH7_l1a78j5bbwFLPhQu7wpsrbOwpEpnpITQnsdjKhl55PN_FhCVFNY2aPaS9pCLvXUhxpvLSbDOhoOSUhLTC9Wvv1gDKJ2IuMq0Xss3DaZnqbgmVh91-DZAPpCMX-w3f_wIzHdaqH8tYZxkby-EUki8jWnLRO_f6eH0jkXj33uSZH7-K65wXkyvP0STb19FmF3W5VzgHg0LeWJn2w3ap4LCAB_df9_RW9cFUtdvIq2G_tSavte7BySTAl2uQhbv4yy5sbVneS1barOsGjo6hHKsQrXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
زوایای دیدنی از سوپرگل یاسر آسانی به الغرافه قطر؛ نانزد بهترین گل این فصل لیگ نخبگان آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/31453" target="_blank">📅 23:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31452">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJ-d9zhQz8HnrZgtp8Roi4fTEzu3lgfdsiIptenSSFjfqV46yEzoUxaKeMco_Di1DlM8TcHUGohFUcfJhB2-wEA9Qqg0TKtB3xH6MR3FfxRE8_KrfeuwKl1lopZiXnRUzb5OmRWa2NbwIJyg-RHVsNCP-50_Y2McvtXeRgR-2dm48csUA4rohB--GMXRzgR0MOKHDVWMxzn8NSE5nEUPcv09i_qsdFKIMCPfzA1eOnWyrnQNPGjq0VkBkcoBmXwXYzA5ka3iJc9DqlyegbAc1FEA6WAIW8BnedSXy6ZYaXwgii2MHVjGb1wyVFJKK89zaly8VibHuqCI86m2tRRdNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
زوایای دیدنی از سوپرگل یاسر آسانی به الغرافه قطر؛ نانزد بهترین گل این فصل لیگ نخبگان آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/31452" target="_blank">📅 22:48 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31451">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LiIwD9OJbcwaJxQmc84dWFZTXMOLpc04nSl_wU5Pud-QLXafClPLYqaRox_CMYmSlSwl51MnlcWkVnsUzpYgzAwgXB9FYtU8w9wRloW0WjCE5w-_3daz4TDqaoj1fp2SUAR7WL8ZTd9oUd-aW3LTLcIbchCX7OZw11d4pD4RmodMB3Xfztnq6CdUfQTYJbX5lMElcbUD2UHhyJTQFu695iCusXEtLkmvC6NVTV2jWVxm91Jvw0xav7WKAD8JVINtv-W6HRfs1BoZTVEWsVBhNmawVjyKdcNI23c2sTPds16-T4hPtrNK5tpqoFGO_hKjUJy0AhZ_crmfvNuE7qXW5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی‌امشب النصر درلیگ‌نخبگان‌بخاطر هشدار امنیتی و احتمال حمله‌حوثی‌های‌یمن‌تاخیر خورد. عربستان با این‌وضع 3 ماه‌دیگه‌میخواد جام ملتها رومیزبانی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/31451" target="_blank">📅 22:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31450">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔵
👤
سوپرگل پشم ریزون فوق ستاره آلبانیایی تیم استقلال بلافاصله بعد از اومدن به زمین بازی؛ گل اول استقلال به الغرافه توسط یاسر آسانی در دقیقه 38
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/31450" target="_blank">📅 22:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31449">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af2c2d01f.mp4?token=ewTXYljQe7WysujDQ-qPE6b-so91EppI6K35iETtYWefxRTuWgquDQFJTFBSSsuOvLXZ93R1qCru6X_JpnryOMcIuf3qrQ409IaZq-uyqEmtLtFC1W431znxjYXW4_rOdkKGu_4huljR2YgM5eZm5x7ziKa9BzO5zmbWijjO-y2Cbq5K9EK8qq2tEZYIKYcFw2RptpeZ5Hn_CHRengL7pCTo2kSShDuIRgNQC7C3Fq0Lr9CeKKmSgK27q9kLz96Bs0qjSOSalbMKB7jzaeorMNMxmv_S-qusPjj2pQP9Ds46pOhjeHIoX9XtWlMoUFTZakAYIjev5CE04utQOLaHiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af2c2d01f.mp4?token=ewTXYljQe7WysujDQ-qPE6b-so91EppI6K35iETtYWefxRTuWgquDQFJTFBSSsuOvLXZ93R1qCru6X_JpnryOMcIuf3qrQ409IaZq-uyqEmtLtFC1W431znxjYXW4_rOdkKGu_4huljR2YgM5eZm5x7ziKa9BzO5zmbWijjO-y2Cbq5K9EK8qq2tEZYIKYcFw2RptpeZ5Hn_CHRengL7pCTo2kSShDuIRgNQC7C3Fq0Lr9CeKKmSgK27q9kLz96Bs0qjSOSalbMKB7jzaeorMNMxmv_S-qusPjj2pQP9Ds46pOhjeHIoX9XtWlMoUFTZakAYIjev5CE04utQOLaHiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
شماتیک ترکیب استقلال برای دیدار حساس امشب مقابل الغرافه قطر در هفته دوم لیگ نخبگان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/31449" target="_blank">📅 22:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31448">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7a4d637ce.mp4?token=bvrYmCfwhVMZ3PgB2efMFMr7Gu6cR2L8YeU7SLuwI5njdfEgeglW9K5QXf9lIpPfko6Xx_6guAGK9BAqd50ONmGdnxPN5YL666w2xDOAixnd60ftSV_hVP9cSshd7Rq01cZbF1DYphmPsCt059rqki7ok-vg7nQFY-_KTugH185Lop8vAM10xsi9q9VapkMsHPzrr_cVEBivlvhv1_jUPOVoIVAjTRtvLmTX1zQ7KtCvXgTMjNad0Ac_38c10_KQLaD1rMhCye0yQMun0iOwxOpTO5gAbvaHRCZh11RuxafayhtaW-_evNAYYowqWZC3fO0v8HAp4-Yo705br26Ujg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7a4d637ce.mp4?token=bvrYmCfwhVMZ3PgB2efMFMr7Gu6cR2L8YeU7SLuwI5njdfEgeglW9K5QXf9lIpPfko6Xx_6guAGK9BAqd50ONmGdnxPN5YL666w2xDOAixnd60ftSV_hVP9cSshd7Rq01cZbF1DYphmPsCt059rqki7ok-vg7nQFY-_KTugH185Lop8vAM10xsi9q9VapkMsHPzrr_cVEBivlvhv1_jUPOVoIVAjTRtvLmTX1zQ7KtCvXgTMjNad0Ac_38c10_KQLaD1rMhCye0yQMun0iOwxOpTO5gAbvaHRCZh11RuxafayhtaW-_evNAYYowqWZC3fO0v8HAp4-Yo705br26Ujg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
به دلیل جنگ اخیر دو کشور عربستان و یمن و شلیک و برخورد چندموشک به‌فرودگاه های عربستان احتمال‌گرفتن‌میزبانی جام ملت های آسیا از عربستان وبرگزاری این مسابقه در یک کشور دیگه وجود داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/31448" target="_blank">📅 22:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31447">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30cb6e2f17.mp4?token=mL15NNlnHUpIo_rm4O6Th--CiOuGSDuHWTUyN54okMZbudG8QDCZK3W5wXgdh0IZOylcQ0gZB9gargzkCwh8YvaD_vPQqsJ7FuEeCDrfW9C3qoJ9-cTFrVY5QgJc8h8DohA-jLieApGWffq9W5i42dq0HWDwqOku9fSnURcNWE-lmC7_4hWT22z9BEYHAwvIOTGUDrSv-8WCL74f0q8nGLONr5GOn_aLty2Pg9HRJYz2MPZJIDWSK8BB2yiD255LxPPseC3Yyyvb1qVlLr1xMe0twoAlNkldMk2SL7Gn_ZfrWF_LY0oaQbZ3BzguHkjFYTV-XKJCI86aSRAEewTLrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30cb6e2f17.mp4?token=mL15NNlnHUpIo_rm4O6Th--CiOuGSDuHWTUyN54okMZbudG8QDCZK3W5wXgdh0IZOylcQ0gZB9gargzkCwh8YvaD_vPQqsJ7FuEeCDrfW9C3qoJ9-cTFrVY5QgJc8h8DohA-jLieApGWffq9W5i42dq0HWDwqOku9fSnURcNWE-lmC7_4hWT22z9BEYHAwvIOTGUDrSv-8WCL74f0q8nGLONr5GOn_aLty2Pg9HRJYz2MPZJIDWSK8BB2yiD255LxPPseC3Yyyvb1qVlLr1xMe0twoAlNkldMk2SL7Gn_ZfrWF_LY0oaQbZ3BzguHkjFYTV-XKJCI86aSRAEewTLrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی جالب از فوق ستاره‌های حال حاضر فوتبال اگه خانوم میبودند؛ نیمار خیلی بهش میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/31447" target="_blank">📅 21:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31446">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ji62PgxkfGtXb-K9xg76mzEc1uT_LywDInJe5hTmd3kOm8waOYT8uoUDSC4wejUsBm5_3dmPGGjR9HgXrUWvkyfFoYxxkx3-r9xf3MjGtd53PtNeZrRCYbIKO0AEGDkrZ0z0mkjSCCrpVPhkvrUAnFPIpysQLCxdQ-nXHk-DCfZ1K15U10eWYPzAGt0UQ8R2tQZ-1J8ynxCTYGEeKJ3-m1FLkJ02k1AcxkvpKPZfyi7c2b6Xyoxs_fs-rxb4CZaKiQv74135yXRhBZsZbT52B2eEVYcYSQEMpb3QcqujpvjPyYLdcLtBcEgl-doRmQ6FDPn3Ya5-C7l7dWGH4zBYgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ باگذشت‌‌بیش‌از 15 دقیقه از مسابقه بازی تراکتور و الشمال؛ شبکه‌ورزش موفق به دزدیدن تصاویر شد و بازی تراکتور الان داره پخش میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/31446" target="_blank">📅 21:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31445">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzNVk4XH6Nc-mAwpEBb52itE0iREjAiQFcHigi9ooOs964EB03_J3pQSSwGWccMYkSUkQrmfsHieJ7MoaK2TFH517zULdsHN7vYRv64QSINhgvX7i2S4q7DUfJYwsqVFg4rtb87LTa9-opoYcqTIIWgzewVfNef3gTPVwjRbCTi4jP-R_MX_QrrFlyhF2c9DfVuKU_NqOrUc1Ly2pwqI5At6ojV4xSi7joIvRkYcvOW3YTWyoiFEZssEFNFqRvIP6nI6oqCFEQorLMxYnXxpDM5xJccSqxEo6AWpWijxnRgEhED3fAi9hgB5sUWmClpclS2kNQezwJMOXjasU8NzOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز؛آغاز هفته‌دوم لیگ الیت با نبرد حساس شاگردان بختیاری‌زاده مقابل الغرافه   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/31445" target="_blank">📅 21:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31444">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swX-zFd8FcMdmkJYsks26P4SzDqJrzQvfr7aMR8FXrYXN2HsZB45-iHSnQUTwtQ75wEqWAQobxnERgv002-_yKl_VKTN9tDcCe_X1WpI_NKApnztX6QMafRxIzc2_cWy4wqGnPuXxy_xvdan_lNFZ1LN7hv_wOTfVxUT04SdSluUve58_G7BVXoHkMlRs6iKMmDgLtHZuDVDTSG4ZLkOXBPWa0yWg6ScZ-2Ukro9zDjYibaaoDgqmfmUXy67t35nQrYrHNlnMeMF_wtcVFDpw-gJTL7IhNuItO3xY6slJ-7HxSzZzuKm96BAdvoRracVjZF3SQxCPji5IgZ8gOx8Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگار باشگاه فنرباغچه و فن کریس رونالدو که در ورزشگاه بازی شب‌گذشته تیم ملی کشورش مقابل فرانسه درهفته‌اول لیگ ملت‌های اروپا حضور داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/31444" target="_blank">📅 20:49 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31443">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSQuRCgfOpfxfvYC6eKnZyDZwtU89S3p1Rcp1y4OoXgL90n_3MGnWq-Km3I8ytlZdr2iZVhGTclY-jhDaopU4B9WiujNddgrgUF52s_GlKpq8h8lrn-MicQYRkPvkTY7TuHXkAVZBrQO34GZvcEXGBRWS7pJbS4cSyVrwU8svJ3XSZy2ixydf5buSdHt2-evh9UjHJwsklY4s4Tgz-PAEW9jUFcNUAscwJ5FeyQQcqgFObgBJiMagw3dejTOZHDsC-UO-Ggs3qLa3ecW9L3XjBcHHZwx-DpgaJjcS0XjAgw9d9k65zG3AAByU438DTpV3SgzzuuVP7sd_pPLOqv0Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ‌نخبگان‌آسیا؛ ترکیب استقلال برای دیدار مقابل الغرافه قطر؛ ساعت 21:45 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/31443" target="_blank">📅 20:34 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31442">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKT3gDt7XMgM9PWaR7lQKva6g-EVspmJzivMY6z1SlxajfB8rXGw2NJbJVvc3O9BcDlgJBf8762tVefynJoWlSmUGl6DGJB1p66CZn1-dC8yKsGR4WlFI9-adE2ZZ80aYefoquhqeb90mbs2RSZ0oisCJ5lPVr6FXa3zsQcXyc6JRywCvwLanUEecgwsxQZQxyUe_3kjHunTeXTkdOtqDdfQg98g10CjTtXUdyLy9Y2plWVFSt0oeJv3rCO2diGR6CsALUoxK2H_U8zScezJ1sCuBqYQtytvhzQ0UZ-3K557PaVMfLlZlnx0O0bE3kv_Jad8MhzdUTugzd9QpJ8n2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیانا؛ یاسر آسانی ستاره آلبانیایی‌استقلال دیدار روزدوشنبه مقابل تیم الغرافه قطر رو از دست داد. این بازیکن ممکن‌ست با کاروان این تیم به قطر برود اما قطعا بازی نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/31442" target="_blank">📅 20:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31441">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9509bbb5ca.mp4?token=GUdh9KMgRupDYYm0NOm3mmveci69B8Yv3P3rwIQhNlAN6COAmWBVDDgpPpNFH1dBvuINYYZgifA4jolbvPVZZ7Ird1uj_f5Rc6EAYBaaClQ7KIBVRjrIjh3h2eAUiTnLbGofzA12SqDc2LdIZE53UetBjAA9oGO2OW9B0NM2stEp5ZFoOu4cLoAdsLU-YZVs5wk485qopYlIpbZdyFHzQczY-sJHhovXhKJp6bmk0e7vaUJTTTg5i5N_dAmbIq8zw3LzVQQkbDD90uaw9qYlSi7KNhQnF8eETmYdDytdSSMXakMUQs37SPTYpjLxaRs_YhwAPclQdOFFM6UvG-GrmIFCaw5UCT-G-ALGyZw3wnLG-OQ5073hiWdtZmNg5Ncee8mRXCXkgQrMCjMrFBDlWVTswSrZTOjYfpDDfaFAPWvUh1q5vP-tzCl0vT2EQpmAJmUlVv0fMhgkPUK378_CcGf_PmvD4lT8WWMLEt9JizK6rLWqu9R06EOBJKKYi7XGfMnVuUw-US0HGCrOOWw7pg-6SsEiZWwh31W9CSlQymoNIINasQS8OBfdiGnvr9ylcxv0meg0_WGFe2kLGMZrkOiHjmaPCXFitMzZn4VNWPtvXlbRF6RHcccTwUX5NUZU4jvkPwTvka5vEJbJX2uzaWXOP9DuST9KxXJmYMKCbuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9509bbb5ca.mp4?token=GUdh9KMgRupDYYm0NOm3mmveci69B8Yv3P3rwIQhNlAN6COAmWBVDDgpPpNFH1dBvuINYYZgifA4jolbvPVZZ7Ird1uj_f5Rc6EAYBaaClQ7KIBVRjrIjh3h2eAUiTnLbGofzA12SqDc2LdIZE53UetBjAA9oGO2OW9B0NM2stEp5ZFoOu4cLoAdsLU-YZVs5wk485qopYlIpbZdyFHzQczY-sJHhovXhKJp6bmk0e7vaUJTTTg5i5N_dAmbIq8zw3LzVQQkbDD90uaw9qYlSi7KNhQnF8eETmYdDytdSSMXakMUQs37SPTYpjLxaRs_YhwAPclQdOFFM6UvG-GrmIFCaw5UCT-G-ALGyZw3wnLG-OQ5073hiWdtZmNg5Ncee8mRXCXkgQrMCjMrFBDlWVTswSrZTOjYfpDDfaFAPWvUh1q5vP-tzCl0vT2EQpmAJmUlVv0fMhgkPUK378_CcGf_PmvD4lT8WWMLEt9JizK6rLWqu9R06EOBJKKYi7XGfMnVuUw-US0HGCrOOWw7pg-6SsEiZWwh31W9CSlQymoNIINasQS8OBfdiGnvr9ylcxv0meg0_WGFe2kLGMZrkOiHjmaPCXFitMzZn4VNWPtvXlbRF6RHcccTwUX5NUZU4jvkPwTvka5vEJbJX2uzaWXOP9DuST9KxXJmYMKCbuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ریا بوز، استعداد ۱۹ ساله انگلیسی، پس از حضور درآکادمی‌ های چلسی و برایتون و تجربه اسپورتینگ، حالا بازیکن وستهمه و بصورت قرضی برای ساندرلند بازی میکنه. به‌ایشون‌لقب آلیشا لمن جدید داده شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/31441" target="_blank">📅 20:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31439">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qu6rWytozL03MU7Ytxdi7PlJJJVjGU5_2l7FyFdrInm5fNp0AiaOfFx1EGxuliJs2UDYGiSiMdfNBthzzDP8D9s_6vS2Q6ngfnf7LmmykSYkVwdSXzfpFZE5LDmG3k4B9LZJRDj-2pSSUl2NOc-9rQqDlERZYBD6JJFUkqLfRnS6egJPuhvJ982cyJzPvdMMwkzbcFUDBHbGUCv6sbVDqoKpmetqD1l2QK51BVvd4Kbs8MoTZkjBm41qkOEW28TEVwD4MC2celKVUy--9bc-Nv57zMzy43fmx7XMVUU8KFh7ZVCjOQcA4y8PFzb9s66eclfvQ8r2oFz7fpFyyAHGLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
هفته دوم لیگ نخبگان آسیا؛ شماتیک ترکیب تراکتور برای دیدار با الشمال؛ ساعت 19:30؛ حبیبی نژاد بدلیل مصدومیت این بازی رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/31439" target="_blank">📅 19:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31438">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRo5Xx5xe57eeuEiGIMyVynZf_3EuYgwYoyP4iwebAWKJENEOHB4Jo9ZPN843f7GIL1n4nMtnkyyk76Vo-cxnjUVAyuNmitz49vLfFV2R5fH-Pyg6fi9b4DTSar1os-V8f8qJyfX152bGZ-LZuWhgzX52EUn2ehwYBwG77mO4W9LaHzi3ADpoa6kNhpwOnwdWtrm1RbtTHHpOwCf0z-5mggAZXAvPiucmkkqQurLkDNG8ISH5pdsIsbOcXZETNDaScP8HIlu5RFe-j7l2IRfkiEkk1EDLBIX2yYIhJEaRJTOYiT2_M0W0oyvK1nZq0imqgUzu5rlz3wp863Plw590Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مقایسه‌عملکرد مهدی‌تارتار
🆚
وحید هاشمیان دوسرمربی فعلی و سابق‌پرسپولیس بعد از هفت بازی ابتدایی‌سرخپوشان درلیگ برتر: مهدی تارتار: 5 برد، 1 مساوی،1 شکست، 16 امتیاز؛ وحید هاشمیان: 1 برد، پنج مساوی، 1 باخت و کسب تنها 8 امتیاز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/31438" target="_blank">📅 19:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31437">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_EvmqqMdFJotlZkrB9h-D4bunUdPFZ-9OZFDA_yB_WzR63-9QIcP64a2wXIcUQwdjSXuQJb7855RNvc5ArDSH83JSsXNjsbOark6GLzgUoQUotOQ8ptujDGqoycknaYtJ0DMKGF8cfn42VzaTWLuSJIPKWlVPVkLReo6r3mNkykmKsedQ112UI4iBkfTFka-19yNK_iJVZ0BdndGfjXibh8BoFnOqeuayZ1DegKvI7gkQHlbJ4yGHsibW85EDLkWnBZJoIyjsHkZVQMnyUlhnLli5xG_BpqqlO9EPWB5X3nJaIL7s719tJTYyCRM9Ua62noo7N7QC14AQRZE2sogg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام فدراسیون فوتبال اسپانیا؛ وینیسسوس جونیور ستاره برزیلی تیم رئال مادرید مسابقه سوم آبان‌ماه با بارسا رو بدلیل محرومیت از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/31437" target="_blank">📅 19:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31436">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HI-ZmQZYuvV5rp0ar1gmJKjHQdaOpGLYHHmtaVzzZh5APwWk_hxYfuH7Sc9zllFtWcsokq6Ii6C9BbwMjHgusqqWzlswmk41dKetzqVzMyC7CDv9SurDhwvARg798jSBX1S7JsFCNqDih4SKWtn3yfqsBnZnTd2MgWFpPEn8czSZjsj6oEn37toqpOqPEls0vQEpD8S47X1wNrjSd-Duc06uSL_7SopNCHs5VTSc8cBx3LjdImFSunP-oiPIYCOJ1WEAO68mUfMCvpFzmHb1yYYh7ehsOQPuIoccPLy0jYhVSjUTxDZEhciaTUMjr7zKYvjfXKpKV2_eS-QBUDFeDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
مقایسه از هزینه‌ای که باشگاه بارسلونا برای جذب پدری کرد بابقیه‌باشگاه‌هاکه برای جذب بازیکن هم پستی پدری هزینه‌کرده. پدری درحال‌حاضر یکی از بهترین و آماده ترین هافبک فوتبال جهانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/31436" target="_blank">📅 19:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31435">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvIMRJAJ2EcD58WILNHa83OpmQOv6kyBO4i49E3GLpNjVdFJ9nH99dtuHI8Jw0jMp315BMXMSWXP6u8enuqnkfSv6xHq51BAguwZ0a1NS2f50GghTFbRGO5HmOYJ_9jbJD2btXCbes2zG82YFsfQ5T_bvRx0uU1riVoTgimz_zaiMDW4oHSKWoRPbPIUABBhNSTg-GAsLdLTwbxHJCryMTs2GAyV4nH3yUKoc08GGJOHA91Px38jEk6yU_s7k8JYnJjPjBvC3G4moms7zaLqBda1bv1gpRiatzwPzTnBJxpDcFTLmcaZV-whZ73aQTcko4s5PESjr0aj6PWnqA2gbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G20
🅰
🛒
ورود به سایت
👇
✅
https://ikruyxysd.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/31435" target="_blank">📅 19:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31434">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGoqYELd2Vf3UwIT1VWX887ZK7Ex04gauMKDyOP-mpEqImUw0C6-SKL6kkOoRxA4gAZU4NQjDF2gXbvHpMZwXFsuzMpjieXX1Ey3lesXuWj2iwYNXNHvc-E77T3w8jFZ0OYqJqBIt7NhYpyW5tDdKEqlJbWPbnt04XqiRlQt9KQj_UR6oqnRiMDmlruCW5ZDJsibonaB2XY4NDiR945k99i-WcJps2mRT_PnqBzvlfSbGr3U_t39mcFnljgUPaC0Mo81w4yDFEEA7lu7Q9iQolkCCKtpyjKjzezurRTXMesUdroLjFDqr2aBq0aevmFComf_pvy7Ek8nwVqaLkNq7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇧🇪
باشگاه رئال‌مادرید بزودی قرارداد تیبو کورتوا رو تاپایان‌فصل2028 تمدید خواهدکرد. تمام توافقات بین دوطرف برسر جزئیات قرارداد انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/31434" target="_blank">📅 18:51 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31433">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d320f9626a.mp4?token=DGLY3gISK_Ak9_VnOMnnhvGHpGVLUdNF8iUWk4nxaTA1Y45RSqR2ufy7xZRdvv44AakGIzvNqWb96L4J4qGQgHxKtxbdFdP9BjQkMoHxya0O1BwkeNdPaWUxKNMjCt1T69_XMbbwwWyvjQey27wNifZNlRffvBMwbnnAkRFG90uCaMd6sAgoofc7U5A22_W8oLwp3XjLhntwifPATyD283Yey__i_fg721wy03V5hS8NpNEwTJMkH5i70ufmZ-86wmHIQtKYDDZoBVY0Idv4ckMiZo2BmryI_xtB98nX9sBBPHIAItTdPZJZ8xmBZC7JIXk85SNG0UCey3r2gLUO9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d320f9626a.mp4?token=DGLY3gISK_Ak9_VnOMnnhvGHpGVLUdNF8iUWk4nxaTA1Y45RSqR2ufy7xZRdvv44AakGIzvNqWb96L4J4qGQgHxKtxbdFdP9BjQkMoHxya0O1BwkeNdPaWUxKNMjCt1T69_XMbbwwWyvjQey27wNifZNlRffvBMwbnnAkRFG90uCaMd6sAgoofc7U5A22_W8oLwp3XjLhntwifPATyD283Yey__i_fg721wy03V5hS8NpNEwTJMkH5i70ufmZ-86wmHIQtKYDDZoBVY0Idv4ckMiZo2BmryI_xtB98nX9sBBPHIAItTdPZJZ8xmBZC7JIXk85SNG0UCey3r2gLUO9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادت بدش روترک‌نکرد!
جواد نکونام سرمربی تراکتور:
شرایط به‌گونه‌ای‌است که همه چیز به سود الشمال است. چالش امروز ما مقابل الشمال شرایط خیلی سختی است که برای ما به وجود آورده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/31433" target="_blank">📅 18:36 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31432">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjE3-8v4jLSSRj9p_UZDIv0BIBuFjDISOGJpBWO3vH_bxwutfQsRwrULgs6bvSe92p8NVQ1lubTOzdKOWdsS9Ml_D1tlyyQpWywAREj92qAIJilSxha5_R8rYoz8qTxGAV41yUm3YijeRhJBLWahVmyckuBeCWAvqWnHzP0gEejSxdAnVMfteHhI164dfl7nIn-7VArVz8QZdZeA--2nj4nl3NB1Hm52RigHJ-t80odHoR9aHEl_CriQjzFhT_oAfVMCqh2PfOM-6MS922BHPjbtJm9_VWQISiDgAtkxgRc4ZvY4HJPCHjOv5zIkF3YnhvBybIeKmoFitX3DIX8xiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
هفته دوم لیگ نخبگان آسیا؛ شماتیک ترکیب تراکتور برای دیدار با الشمال؛ ساعت 19:30؛ حبیبی نژاد بدلیل مصدومیت این بازی رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/31432" target="_blank">📅 18:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31431">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YF9LDJA_PwG0mLucvMMAY_PNM6zWsr5dCy-sx8tyDuhk3Ye4TVOSEik2mwAJ5RHEt-KlUg2ui5ja0t-IUbbAh1qjqKZPjKb64wCxbvA4fgeGMesvLQn_4Y3re1-8p4rZ9PV7gnxdJ46gAWvQQzQpFjdL0OINys7st8RpSTiezhN2uDsi-slxL4EhrkzGVoTK1qB6887IZ0XlGcA6mTS5ShZPi4a2GOTNSYQZF6UrUkki5TYjKZlv-33UgKPhgnDL0AKnDugNWK2HTAsVIcHYTjJ_bwebLivZqEdjxs_bBGGceYgixg9b5dnc0KQAu35x8LkB097u4qiU-jKRpsCtow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افزایش قد عجیب پسر رونالدو!
کریس جونیور درحالی‌که فقط ۱۶ سالشه، قدش به حدود ۱۹۰ سانتی‌ متر رسیده و حالا ازپدرش کریس‌رونالدو باقد حدود ۱۸۷ سانتی‌مترم بلندتره! جالب اینجاست که با توجه به‌سنش، هنوز صفحه رشد قدیش بسته نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/31431" target="_blank">📅 18:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31430">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlXSRqyHQY-5eiQQUmAxqWGxhR8u8LeCG2Z1QwvFOMbPsJQvAZ4GslUG8fcwvsr4do6a9JdY1P357qP8Ig8_KT79nGGsDBkRBQnSmSLz4DEv1aR4LDCPbAfwhDeTuxh3pc-Qc_yMOnkAEA7Iq_NBLh59ywlwlXfXAz_1I8w0kgjkiO80axtzm5LBTkLOq1_Njgm6-kAzDZI9sK5W3unnuVBA5qem3NuDGC6pUBMY-3zKeOT8mHn2t_23K2TGa63o2m-E7XojHVXgCX5lsMfND_xglkPL5HtiZPw1VTZqFUDajPMKnAuElFxebCpfaAF2O8Ah9Dqq-e_x9QlhZYJZdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریس‌رونالدو: اگه‌کسی‌مسی، پله یا مارادونا رو ترجیح می‌ده، این سلیقه شخصیشه. بهش احترام میذارم. اما این که بگید کریستیانو یک بازیکن کامل نیست، یک دروغه. من کامل‌ترین بازیکن تاریخم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/31430" target="_blank">📅 17:42 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31429">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l95OVfu00xEQKK0I1jcV85wR_6x3QcxGQlhPM7aXQRAWSqO7j0QDSmh378Y_uyAx1QJ3hkcVzAVF9GwrdHLbd60dOnpL8b2tAKA5VtbZNirxXq_bmn7AqlQ5N-w85yQ6HkAoQzXDeMuAzXcYhN_PSJBK0QjMF54w-tCrf76TzHkqFyKJf_iomxx9RI6hv5ObiSNzfzQJvYnwFi6y2K6vyKQHUy-7KL8cZFW0MaqQQFJjM2hBU7LgLT52Q3_9JC8aat4nAYjR2B6kor56OvOP_YQFC6fNtGnhYMQ40_bk38F2rLDh3m8XuswyIN8ggLY-WcR3NOxTElGkL9j9y45Nvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخواست‌پزشکی‌علیرضابیرانونددروازه‌بان سابق پرسپولیس و تراکتور ازسوی‌سازمان نظام وظیفه رد شد و از اول آبان ماه اعزام پادگان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/31429" target="_blank">📅 17:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31428">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SjmQQMi0X28dOYBvMqiTW7p8oBrtjVJfQ6sXihWvqaHVIuUF4TmozYjkt08nh6z30CSWlYwhGV0QIaBZNxXb4z6cx-gVCDVMJxVcm4I2s6tOFo5gktq-zCeRf_IwF5H03BOYqfptn0XNKewIPcTd86b_5hiww0Tnr13Q6YfRBXrTn11lt8rkHx9dASencUh9JmjBTRA00D6wByacI6EXVYYABFjVseLLrKriU5T9WzXJFCCsxpTJoenyuOmmgcasiYvaTFkIbniCnwvE4kPKvPbmFsljH80mB-YNLjNp03Hbpfer1vJS80oTI4Rz8iZrAuB3aVG11DRli-CyPQ0_uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ سهراب بختیاری زاده سرمربی تیم استقلال در تماس بامدیریت باشگاه درخواست جذب همزمان یوسف مزرعه و یادگار رستمی دو ستاره 21 ساله فولاد خوزستان و فجرسپاسی رو داشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/31428" target="_blank">📅 16:22 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31427">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tdma2PV5QLjwdVlFt1m6NuMsmX8JJOgwcyfbYBbTPkC39mFBPA-g9nagylLYStY3G0gCFsnWRgd5iXwccbXavd__vqnwExA2LwWN0vqflWuvcWt03YqC5RoJ5zjsH4kEiaJlyqaCQclEM9-F8JvK6438Krb4pPB_I5F2p_0e7_gHQDB2kImC7Ll-3gg-mam_qiPk6Lq-ckkl1FsCK9ocOPG3rypUqe0ZfZQ56QIseETNCK1UHuz-eGu6Q2EAdD394uXwrPdOqm0zyf8a-aCF7-q9wBCeao5Ebd9QdspSwj2tedrhmVPTdgCqXFGwFwYKrlsLcOPVAExX46-zdE7prg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
#تکمیلی؛ کازویوشی میورا ۵۹ ساله قراردادش را با باشگاه فوکوشیما تمدید کرد‌. میورا فوتبال حرفه ای خودش را ۴۱ سال قبل و از سال ۱۹۸۶ شروع کرده و در فوریه ۲۰۲۷ میورا ۶۰ ساله خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/31427" target="_blank">📅 15:12 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31426">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‼️
ویدیو کامل قسمت سوم فان 360 با امیر مهدی ژوله با بالاترین کیفیت؛ عالی بود حتما ببینید تا آخر.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/31426" target="_blank">📅 14:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31425">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcseGrpeM7RMC3ZVURV9CNNr-3VpJS62wXW4T6gwHO2Tf_7BThQVxkr8iGVaRamnyF01moFaxMRiwG7_4qfmzv7rgOQgkN7nk4wgK1aQC7p6viJEtOgb2h_RmlV6cAb9k8FS_L_CzDNg1w4GdT0Txau-AtgCMjtUa-eIc_5Vd72Om3xocCWYavS2v1CvKQnJBAO3k-g3He_HH58QXneKhpPQu6QA2I3Oyb5WiNe2_Nk4uvnIQ2GSOpSc3xtC6NcdPe3iv-TXC-AeytbZX1cpNbcIq8Ic-U-023fJ_DVUNmpWsZs2jpJpct5Hwc359UMEBztkuHnDAwc1F6FGhdiOhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به دلیل جنگ اخیر دو کشور عربستان و یمن و شلیک و برخورد چندموشک به‌فرودگاه های عربستان احتمال‌گرفتن‌میزبانی جام ملت های آسیا از عربستان وبرگزاری این مسابقه در یک کشور دیگه وجود داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/31425" target="_blank">📅 14:14 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31424">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVnJoiJyUQ2dRCe5QQhfIuqkrAHYoBLQNuaffhgGhZ-drsWSUjkL7O5-9NQRbajp0ZHA1dvKPlkbuwASgF00wPOhZxQluKAVDi2A5y5NdkmQBLyy3KOCXy19t0h9FggGgQ2HpPY4yuA6LNmA1y33lD26MR8LVoR8zbzEDMdNAzom5CF_VZr45TY3OAU2KEeCiTYALvQU6zZVvuORdGLcVpq2uMCLFl2sluePmQeMOPr-LJWaCVR3GLlEtEvAi5eGxOlzRfVHB5FoENuWEUsn-uvyzY1-UYbTnJ82y8rgcLj8b7zeKGKZISfY3NB511RxpWgNrVblsVgqQ7rf7ccxfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
مهدی طارمی مهاجم 34 ساله تیم الوصل در اقدامی خیر خواهانه 8 زندانی در تهران رو آزاد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/31424" target="_blank">📅 13:57 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31423">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bb0f80f69.mp4?token=OXOfMoGfRhh_l2KXIEbTbQdh-7GFi8GaMMmMk7m_wbiUMXhDzbK6OT5st5_hJHqHwgDTNFkDcqCFEGnwIFMRBavVYzr2-kii_XPe30qe_5Vyd_-50rDNCJbWez9aWi3NJUxHdlUBvFyTqLAgQQckEFw5TEir3AsMrPBtNzQe_dyiO6iaZJUICRCVguzVSw3JHlvGp_VQo-i3clX_b5yD0TTHSx0jdNYQNn5jidyanygPpX2lYlWluB1YV_svdT64OnWrIW_qzRaEaMnVBJsZPlosz1nlL7-XhSiNrjiGVSA3EdlUk8-EgY-PIEqCB7vBtquz7wYFWrqt8DoyyIGvBYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bb0f80f69.mp4?token=OXOfMoGfRhh_l2KXIEbTbQdh-7GFi8GaMMmMk7m_wbiUMXhDzbK6OT5st5_hJHqHwgDTNFkDcqCFEGnwIFMRBavVYzr2-kii_XPe30qe_5Vyd_-50rDNCJbWez9aWi3NJUxHdlUBvFyTqLAgQQckEFw5TEir3AsMrPBtNzQe_dyiO6iaZJUICRCVguzVSw3JHlvGp_VQo-i3clX_b5yD0TTHSx0jdNYQNn5jidyanygPpX2lYlWluB1YV_svdT64OnWrIW_qzRaEaMnVBJsZPlosz1nlL7-XhSiNrjiGVSA3EdlUk8-EgY-PIEqCB7vBtquz7wYFWrqt8DoyyIGvBYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعدادی از گل بخودی‌های تاریخ لیگ برتر؛ از گل بخودی‌های عجیب و غریب محسن ایران نژاد تا گل بخودی مدافع ذوبی‌ها در فصل جدید رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/31423" target="_blank">📅 13:43 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31422">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qv7uy529vG-vnrMaHGJ9uepNmb8eZORQaNif85tGWYXYEXM-AVOpEpWP81CsqGAngRnbJ9bV0_M_JnuH4ZjSs_VAO3lMlclNO8D8srcEVsD5zqWvGE8vwEaPe8SP21AeHfGGRcuYyiuv-HkLpJkHBP8-2h73-J4tVPECGaqJm3XRy7d0x5RAelwx1_zH7d4uUJlj2Ec2qMjePOXvkhklyvAsa_JAHdEb3qH1ksyWZRAv4OtL5_b6po_giIEfMGMfeJb548j9osv3B8tZOxG7lpFNeomfvp4Q4CKcKULD8KHb-hq7kuXA_OPTP2BMtNdGsmyaMvok1PkOZxIAd-MjAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#تکمیلی؛ عملکرد درخشان کریس رونالدو و لیونل مسی در بازی‌های این هفته تیم‌هاشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/31422" target="_blank">📅 13:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31421">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-UbhYjjzOBVzVOb9zFBphNMKICsOidTs8u7N5wkKb3GsNU_ASIjhWLXzfiW7o_i-xgrvCP_9Y6G8YzxPnWFYlIHNgWo6JFHap0MNf165cDpzEkcWzYtOpa-HKhq8QtF5k7xcdsHaMgaIb2qW608koT30WXT9CRiF5zzZYkNiudYcKqErD49dOScp10a79WkN2ImTC_rke572EymmmFb1Yn3sF-RIKOVs8NhfW1sZDIFKbWIvyMWNG6-xa1B44JgBYEznO3joW32aF0K2kRVXBJNrEDAF5DQPeh6PqjhCIgehsTquoE_m-9_xRvO1jsCN8wr4BadlYn4kz5UlD7jTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریس‌رونالدو: اگه‌کسی‌مسی، پله یا مارادونا رو ترجیح می‌ده، این سلیقه شخصیشه. بهش احترام میذارم. اما این که بگید کریستیانو یک بازیکن کامل نیست، یک دروغه. من کامل‌ترین بازیکن تاریخم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/31421" target="_blank">📅 13:11 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31420">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjMitMqdxwfJj-aJVnCnPYsyR-BsTdIm6i477_QPwrg7nsp-0tqKxulLO9jcsVQdl5svOS1Au8BOf5jd24gW3UqmHdOipwcU-BiDviHPPP6rZ30GUDP89LKpxJAbjuSfKULu5VVVcoVyKMscBFM54QYkmsjpDcmQ2BPrIjEgI5rp1XvUs86t6Q1XEw6WmZFN0XPw4v2bIn1u3vv4Y-rusoOBxPdcLyHFq9RQe_CETeBtxybyzfhj8LUh3JvOmXP1wE-WaiCDjOJDFR_f67TeoKa0nVsqm5VV3D9-LBziZX07den-TaBMxBWoFaMtXyft-vFiL844rjoZYjlzwbB9RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چهار افتخار بزرگ لیونل‌مسی که از سال 2021 استارت خورد. مسی حتی‌قبل‌ترشم از بازی‌های ملی خدافظی کرده بود اما به یک باره ورق برگشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/31420" target="_blank">📅 12:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31419">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUkuffn-qgY5zLADj0PYQTAoVbz-g9Vvchlg7o2BDBcmL3WkXhmbl_03x44P4lSs07tmsYia4GoSzBzD2o_oC7jcaVhxb45Ll--l22GwVxxoi0FxlrX5kP370jWu638FwTEUIJ4ySTMNcPxZLHzWohTbz474_1Cyq-WD0W7GovI0DbMD5zO7Een-vfBOOxCXlmBYR8Oxn7J6HY776uk2p8C74loe4LPNmqTGAbv43a9Gm-2yxxTEHVTq0tHApdHCJMe9v_DY-_rLm93G9UwjsEARc9EBVjIRJy_xoeNU8jmlv7PftYhx26IuGPpWF6mR_9Qi75FC-HGsGpyMYSt_wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌شنیده‌های‌رسانه‌های پرشیانا؛ علیرضا بیرانوند ساعتی‌دیگر باحضور درسازمان لیگ قراردادش رو با باشگاه تراکتور فسخ خواهد کرد و راهی سربازی خواهد شد. او از اول آبان سربازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/31419" target="_blank">📅 12:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31418">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D92YBmf111vFYl2xhzfmKne82vsHcgjHE3EQbOYJfEJTNRnPYKm6DfKXBqUA04L0oGQMY4_SEVf8npPfrxvj8DXySmhDh3TZm2PmbdPP5iJsRXvrJ1lLXeQA9xEcLn9238Jjcq3Y9NQm4zk5g_CDPFWi-wCmeR-ZdRY_8CQ1qq8YalmnxjtqdPQdxBqT3TBa9mMhCZTw_MChQ2DGSj-BZGvKoj3XpLgz69bPwoSiiJlt2wUPZetAkRucuWkVsx7IsvYpnWcdcHOyoBT5xC4bfvolU0SUbh_IPaDOhqJVWYlWlv9Fj_jVBSc8WkNqccQYu7wMb9pAgsmEH8ydWgqSdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ تا به‌امروز اوستون اورونوف، سید پیام نیازمند و محمد حسین کنعانی زادگان بازیکنانی هستند که موافقت‌خود را برای تمدید قرارداد خود با باشگاه پرسپولیس به مدت دو فصل اعلام کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/31418" target="_blank">📅 11:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31417">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6D8asgFCtZEUohY1_MElwR3KZ-9pR3_YHf-jtMskWak8ARW1fqZH4Okvuv-hQG6SfVFID_3UiJU-S21SH06p8j7KEpyi40XQDyPjhFA4LWA47E1Kni2wt5bwFoPH7lfbbn42iJX5a_iASV4f27a_IRHtavkMziczDM-usWMqMFEDdPxCuElv1V9H-dUzwc332XgQIPbxPxpIL48sFzoSRPdQfSLykeunkTcGAUOD9mpIKnJz5LmBfuwM9XCuEFgTCiBK2aly6ZYA0hUZopZ_mVaENVwFkSIb8vwbGmcqA-5JE8rmi28aUQj0A_L8RG9pfIOBlcq2w6ORX6qlVVJ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
علیرضابیرانوند خطاب به‌شجاع خلیل زاده: هیچ نیازی به فالوکردن بازیکنان‌تراکتور ندارم. من به تراکتور نمیومدم این‌تیم‌عمرا قهرمان لیگ برتر میشد. بعداز خدمت‌سربازی به تیمی خواهم‌رفت که قهرمان خواهد شد. ثابت میکنم هرجاباشم جام خواهم آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/31417" target="_blank">📅 10:42 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31416">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvKjkvU0-bzB26iJiU8k-S6zOYaZf9N9uJX5vwcIDcPwDTQIfMYCeix4tSvwkdiMHDPpBr9oORIrEMmE4FuBuH05qGmEkWGL1UuiI1XpxC92Ba6kVS-7Pqo1yGGP_fCQ49EyOcSlkz6aD4iFqav4yGCAwA2Kb6RaAuzujsbcnH0Pyj2lZUOh3cQkV_XSlGt9kC0a1LLToaQW1ys8SwSlKDZbK6PoZPBSDQwOADohfyJmCIg3dH3nK_v9zJnDrjjMngBW-sZbmSxGy5_t7Wyq-tpfAsNsr6OXXMHoGwD2_vIlIgXEo2kmGEbzidr4Q7BieA3rzX-Hu7Hs7JA59j-HkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌پرشیانا؛وکیل‌علیرضا بیرانوند که رابطه نزدیکی با علی‌تاجرنیا داره در تلاشه که قبل ازرفتن علیرضابیرانوند بخدمت سربازی تمام توافقات لازم رو برای پیوستن بیرو به جمع آبی‌ها انجام بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/31416" target="_blank">📅 10:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31415">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGRhyLiRpzBC2o3YBUSB6LgoKj_3ncTc3WgjFusVzd_SppQw5RG4AERhqBHLzig_xbpFIzsKUnS27LGWtvs-uy0-nQzIISZnhLwGjor_-qYoC76dEqO5tMYvOq6-NKVz6sSOZD8FfmJeFMPIVfl41uRwyo_COGcw_vevDZ94fOvVwS-PPpg45EwooNKxDZu6Kxeo-stgHinhpTAyKJtnl18se_rN-UJVtk6Zvo97kP97QwzgHUPJ1Sle4fTlz9wZQQdMqhuI9C2mDyIaHfZCBMFO9HqMzAz_MtKaDKThc9ubjBLUbcTOBLBHvd_Uiw3QDo3PclL5qYwmCPLZwQPflw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد فوق العاده جی‌جی گابریل ستاره 15 منچستریونایتد درفصل‌گذشته:23 مسابقه، 23 گل زده، 5 پاس گل، میانگین نمره 8.6 از فوتموب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/31415" target="_blank">📅 10:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31414">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aqj9E5PHMxRWaZ2kr1YtVItbIu4tKs720V3_wa5HZx67HP47cmC3Mz0BM0eshNXHjHzb1vxo4hGnwHPFV0jd6NpPgA4pmOxjGIqdOI_CB7yE4BNRm7LbjuabUZlOLelp6kEWcnuX1ot60edjgdWywNub_lZiiY7CWs0fEXTfjcFvrQGrO50KmUQkgEnyUhuEW8ta0jba71AjnpHHQ-avNuext1te2JbaSVrNVAhPVxOM_aUObaHUPRsoNwsfiYGAZkgxU0CCHjUHQvu3iG7XXT0k7lJ6pcpTmzi5UbAVskSxpSven2REXkOUp-PsoI0cW6V346UAjGLkQYLF0iHeHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
الغرافه  - استقلال
🌎
ساعت ۲۱:۴۵
⚽️
تراکتور  - الشمال
🌎
ساعت ۱۹:۳۰
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r20
🔗
https://ikruyxysd.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/31414" target="_blank">📅 10:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31413">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8f6d230ef.mp4?token=Ou5zaAACWohb7UgyMFEfamCf_JW7WT5jlLBXZ5GdcfvOFE_xSPVco-HwX3wtxnppsjOueSPYqhZ-Qb1GmPNZtjJtyz_TFWo6KI0ShStxMKr7gK_z11hXGYJZDzHuBd900fLUKvKoztOFXk7WJEzCFyQR5MyTCjFJ0ZixZyEziwWMHvUIUOz8KASVQsGKc74Mc5jNv-mF15XexQETjH28BMQ69Q1TRWLBbUrMoQkGuKEKbyniCWvhKKbh8QO_OfwjAo8_ZXMAwjBZarWg82Pyo4DSIY6Yk6tQ8yAYUqICnPtyDm7yngOIk63ket2CAKa_vFDgbMNH6_VE09gg26Qx1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8f6d230ef.mp4?token=Ou5zaAACWohb7UgyMFEfamCf_JW7WT5jlLBXZ5GdcfvOFE_xSPVco-HwX3wtxnppsjOueSPYqhZ-Qb1GmPNZtjJtyz_TFWo6KI0ShStxMKr7gK_z11hXGYJZDzHuBd900fLUKvKoztOFXk7WJEzCFyQR5MyTCjFJ0ZixZyEziwWMHvUIUOz8KASVQsGKc74Mc5jNv-mF15XexQETjH28BMQ69Q1TRWLBbUrMoQkGuKEKbyniCWvhKKbh8QO_OfwjAo8_ZXMAwjBZarWg82Pyo4DSIY6Yk6tQ8yAYUqICnPtyDm7yngOIk63ket2CAKa_vFDgbMNH6_VE09gg26Qx1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مجری‌جنجالی تلویزیون خودش از ایران رفت! زینب‌ابوطالبی‌مجری‌جنجالی«مملکت مال حزب‌اللهی‌ هاست هرکس نمیخواهد جمع کند از ایران برود»، از کشوررفت. ازفردامنتظر عکس‌های نودی ازاو باشید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/31413" target="_blank">📅 10:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31412">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5075dda3.mp4?token=h8_uiNwzAUwqq1F893u4y4TVOQrT19xL4GCB2AS31FAhtel9RSROfnppSp3leBzcBmkPEp1TQQ0UYEHsERfao3FdowSq1Y756EALq1lTwIezkeVosMcaxZ73f93dMiXMp5RSmnmmnTtzIRAXwNlJUa-5Y5ki-0xzYwG_9CRZ2kV7D18JS_nCWS2l8LwWHFT_98n6kGMbhG7dk6O_1b9h6OiQ9H3mAkEbgOIMVc-JYY35KMZn7Id3Pj0g3r9nv9f7ZCm4dlqPECfF0D_HClAZkJz2wd9se1Tj_5BTQSBVeHQFyBcHayHKxnOCaDCZ5tn_zl7o18pOO4W3gKQo713JHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5075dda3.mp4?token=h8_uiNwzAUwqq1F893u4y4TVOQrT19xL4GCB2AS31FAhtel9RSROfnppSp3leBzcBmkPEp1TQQ0UYEHsERfao3FdowSq1Y756EALq1lTwIezkeVosMcaxZ73f93dMiXMp5RSmnmmnTtzIRAXwNlJUa-5Y5ki-0xzYwG_9CRZ2kV7D18JS_nCWS2l8LwWHFT_98n6kGMbhG7dk6O_1b9h6OiQ9H3mAkEbgOIMVc-JYY35KMZn7Id3Pj0g3r9nv9f7ZCm4dlqPECfF0D_HClAZkJz2wd9se1Tj_5BTQSBVeHQFyBcHayHKxnOCaDCZ5tn_zl7o18pOO4W3gKQo713JHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نادر قاضی‌پور نماینده سابق مجلس:
تراکتور پر طرفدارترین‌تیم‌جهانه.بالاتراز رئال مادرید و بارسلونا. درترکیه، ترکمنستان و آلمان همه طرفدار تراکتورند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/31412" target="_blank">📅 09:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31410">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7024843df.mp4?token=OLjCo_w3vG6BpySG3jmHkevb0SqqNq4obbGo9WDJfsbL3Ag0r6wUw_bQHsV5WNYX_HEvQbWOG9OgLsrSv7U8qUgnsGfsVaqa4joyGzyJM6Vlj6H3_UV6z48XZYCmVQLLZwje73vPWxl_0vUTgccD-5eycdIbbwyd9KyssOmexxgbfd8x9nuB2WUHkoU-XK9UVOkPkmDHFl2a_0T4RN5iylL10HeFkBf4Z1BaFHjvEK01HsGtz4lvpzQIMheRKQbN--8WgQJzAkeSIJxsFz8mggkQJ4rD6dAtF8mFg8xLCs5_vXgnkUU-x5XiyvslzHd4u9E67hNWBDiQCDSPh_Sh5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7024843df.mp4?token=OLjCo_w3vG6BpySG3jmHkevb0SqqNq4obbGo9WDJfsbL3Ag0r6wUw_bQHsV5WNYX_HEvQbWOG9OgLsrSv7U8qUgnsGfsVaqa4joyGzyJM6Vlj6H3_UV6z48XZYCmVQLLZwje73vPWxl_0vUTgccD-5eycdIbbwyd9KyssOmexxgbfd8x9nuB2WUHkoU-XK9UVOkPkmDHFl2a_0T4RN5iylL10HeFkBf4Z1BaFHjvEK01HsGtz4lvpzQIMheRKQbN--8WgQJzAkeSIJxsFz8mggkQJ4rD6dAtF8mFg8xLCs5_vXgnkUU-x5XiyvslzHd4u9E67hNWBDiQCDSPh_Sh5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ذوق‌زدگی امیرحسین‌قیاسی از حضور رضا گلزار در «دور امیر»؛ پز دادن به دوستانش با حضور گلزار!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/31410" target="_blank">📅 08:53 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31409">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ip0TUchj7zMDDOLDUOW1xoCodtieKL22qtKxNGzLWi-pSgjdiXDLern58zbf0PsnvAUxzTh2JY7unFurDOmRdCMZBqZKzcTkuQ8WPcX-W09b8pkuG8mrEaLHT70RbzbbiAQLg-tHEDS-P1mX_Liu8_h5cFoSUQyTF41KfCSBm5K0ykjfrrBGQocyYsSrrhDSGZlG3oxFmcK9u9ih03Fq0PLDb26eVK5XqfYsOqe98Spwvcc3i8IEJsplFO1eAacEa2V1TXL9t3g-XC_tAmywBa1XG4DeyqoA6IJohGBVL6ndQD4F-hhVfruXvfqlCkaO87x87Xk5ZjJQJuz7prZEQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
گلشیفته فراهانی با جان سینا فیلم بازی کردهه؛ چه لبیم گرفت ازش. الان دارم میفهمم چرا حکومت داره تلاش میکنه گلشیفته رو به ایران برگردونده.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/31409" target="_blank">📅 08:37 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31407">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZShRDwIP2FCZOEk0FLB062BB3-UINKZCa-Fq2w2109RcaiTJ6RFhWEVXMPTbXM-2niThQp0sR-YYdtxP06Jm3l07sm-e5OjH2gKD6EhB70UiixBQRKUHGdHjAjTIokwQjkN29VR6MdzHBUfGu5Y_s3WtcYphtMTNINw-viRHiHyLRnbF5GoOAE1JBiDW8LmQHMVYZM89nirqmTMeRPsmlmQw0zXM4Q3m3_WeGD-uX_lvFiCi4i7q_GhWBocTD35Fj2iJZuIe5YJ37yKp_4pIIKVAsH-ukQiKd-VL7b3S3HNTXkZ6mnrqMM10ZLiTH9ypRWc5Kd5T7--cG8bqi2ESw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز
؛آغاز هفته‌دوم لیگ الیت با نبرد حساس شاگردان بختیاری‌زاده مقابل الغرافه
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/31407" target="_blank">📅 08:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31406">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSBFNpaUi_Qz2i1-RkStWubgzkY3qOLNCD2TgHpAV7nQ2Xb9O7GIC2bzPoFOctUoN0kgzLMUi4GXawOGwWMdwVdYupjo82L9Pe4_RGsOxTroj5YFOf44yDe6uyQ_qbUSstDsBQ_w8Xr4niKtaZnv0y-7LOrC-h47GpKUYtDdCOxZmYlTGiBd82pErBzR_KCWvN3FYlY7sGoK-ci8QAwIgMDFFhxG_GIWKSjqskB8hgY30TzRQQZ3Hmv-Qq4lTFASufJNyn5_w3uaZA3O9AjFk4_c49mLvjy8FzIOyr0pORCDZKW0yt2cmeJnutkNUnuVQWwJ6AtWGNlJfgJk6r1hfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌دیروز؛
از پیروزی بزرگ شاگردان مارسکا در آنفیلد تا توقف روسونری برابر ساسولو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/31406" target="_blank">📅 08:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31405">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">📹
هایلایتی از عملکرد درخشان محمد خدا بنده لو هافبک پرسپولیس در بازی این هفته با صنعت نفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/31405" target="_blank">📅 01:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31404">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromایران تحصیلات | irantahsilat</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrF8ApLaJg5-4CJBYlpdjG8rnTTZDSLggFBl2nyWbmPvs0gAKTwlafSHbm49z6ssee_SgUSEAgvkTxvKgF3qjPG8gztIMEJgo9vjzUBO3NVHGFbAlul2jDsEna_MkSiqa0kjBnOIfcj57yCk4SbNAXpoatUOBx2y-9jFhbis-RkYiMpqN4JzBeqvTtN4b7De1yqL2QLW6LTBAFl2RBTBXXQ3srDlHZAdvfDg9TJI8fm0X3GNnPm6gNKESaADJUuhmRM1hirDTtiwEdYX710cXRTCRHKC3lO40SFmS7gJrL7ZGXsMKb_oql0kmrcTzvBAE5cjJFvR2jqou5f7gdP4TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
مدارک رسمی «دیپلم تا دکتری» فقط در ۱۰ روز!
✅
قانونی، قابل استعلام، کاملاً غیرحضوری
✅
مناسب مهاجرت، استخدام، ارتقاء شغلی و ادامه تحصیل
✅
ترجمه رسمی و تأیید توسط تمامی نهادها
☎️
مشاوره تخصصی و رایگان
:
https://t.me/irantahsilat_support
📺
عضویت در کانال
:
https://t.me/+1I9Ex4YFtcZkOTY0
https://t.me/+1I9Ex4YFtcZkOTY0</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/31404" target="_blank">📅 01:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31403">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfDuWNWIGBw-UyXUtKMISLoHqemdzMuLe_5WIo6UKyEkiXkCQEmBT1D5R40K7xMNjAvLBET0JL3eTWQsXO5enXwDUH1YK8Qj7eVPx1jMREp8sLaq1Z5XFhJqgmW5w8XooWPCPGbrNNrscdXWZZ5ubjoGCf4qtU-Q4EVxUj4jP-7sdUGGUD7KUe_zlqaPEFgnnKe3c0OCdSCUrSeC9x40TD_0UHf_j_Wm5OGk_6EnJ82L5GxQAHrj9U4d9bYcEcCD482Y9LWayn72L3ziy9BOw7wfIYB_36QYpN74AFAm7mDSI59pQTiJ25RuOT6durjukn4DxPaSK6YAJm1bdaYzsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هوادار دوست داشتنی و ناناز باشگاه روبین کازان روسیه‌هستن‌که‌اخیرا گفته از بین بازیکنان ایرانی به سبک بازی سردار آزمون علاقمنده.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/31403" target="_blank">📅 00:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31402">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxnXPPOhpCQLb19F09r7f30Kh1SG6_inlCvr44XI12BVBL9PJBSsOSxJbMx4is-i6rK1XwolQhVkhlmzGhKoLT_YF17VAbQHt2ADbUYajA_4lxbGmN5rWwo_P7v_aPDsL4Wnf_kYrr04R6IFguKOzDPp-VPQ6-AygUVanUZKTl8_xt_OmtFhkJH0isSg3JjBUNUU6WfMDA27fm4jJAW5ez7X3DC18LNTNudOAs3tsmA9WDZiBtbMPmBNgO7q8nNR7XO13j6lAHfPt7LIjSpj8Vkew-EYvdSfrpLWLIjEwJY3IolpXkzulAKlaUmaCZutrlkAMIQ-2LBQRia2gp7RAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق اخبار جدید دریافتی رسانه پرشیانا؛ یاسر آسانی تنها دیدار با الغرافه رو از دست خواهد کرد و به دیدار هفته آینده مقابل گل گهر خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/31402" target="_blank">📅 00:21 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31401">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVeMbjY9YcxPt_XETLUcEOlNZe7eBB4i9DyxMaCpWSLq2q18KQA3eKPFq-DaAhywSlSWDzBZwzgXFNtpCHT2FFseQbMor225bMNz0Bh4TpUspMY850yX4mwynXZhU_ZBw8VKn_NOeIrVEtaMvOV698RA3miIjwv3ltHr5XQ2bMXkasTPbrQuQeLl9nVTA-2NEPIDYfYHkcTyliygj2EEN437ys93Sg8a6POTgWvaI74vqY1vEaVttgnyGUSJUjvl622f1PsVScVFEQQEXP_j98bb5TIaqHwYjTxE7hsPdvA2JbJIBSryGg-s-xAhoc7-4EjE-gCVVTxi-qqOri6NQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز؛ دوئل حساس لیورپول vs من‌سیتی در استادیوم آنفیلد بدون حضور پپ   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/31401" target="_blank">📅 00:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31400">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQRRNbLTm57ppW-_5mIs78Ro8FTmCE7N--Dg1kKBwxD6Jo7oOftRN63h50dfkEKob2IK8lRYqFWyTzY-SnLL6oQ72ghnB8l2GpeKrapGVF9PZeaJmHV32ZPwj3KRTdVfUZyMagztZKts558yvScTekYsUnf86GdWrsSkf5DM6Ibt-EJAH2EiI6oXLTAGIBm3GCwqsJsVHHwoIx5dEeA8L_3qbvjq7UCiRsrkgxGhYuaDK8yqz9kFXABppzoa4WTA3Qkmpp4xigxZ3Mv4uQhP1AimLSCtTZ6_iDFqnN6_mvP0_RYImjUP1GhnGSleESYrRv7jvfAXYh92bcBlRROzKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه تعداد جام‌ های لواندوفسکی
🆚
زلاتان ابراهیموویچ درکل دوران حرفه‌ایشون؛ زلاتان فوق ستاره‌ای‌که‌هیچوقت‌نتونست قهرمانی UCL بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/31400" target="_blank">📅 00:06 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31399">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIvNSQZHmYkZc82nH3XdFYgycjKu4EqMT9-UmlYJL-wKy0HCDZ92dof1YOw2czfUzURAt8yTfaGiky02JDCTwGHovP7AVta7UDlEIwrxuMfFBdNyYJKIdM6hO0N2qenxw2u4K6lyQMjDqejlO7ciMxiusgKbenygoWsqfA2ZeOGHUR2mDMj90ZaC16_hTrpU1Cg4dY7IodH8SJ9FLlqlJvF3lzB3MmTCSMBDMFmGUyHzLrKBEkQ6YYcN5zdiT0ML4KzoTIOwTs2bx4NrsIiV8-7SSpfVZHI1tEOjduwXVw25QcfQqDtmNOjA3MuIFi0hv64NJvIO_-j56ID7gD8OVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دستور واتساپی‌شجاع‌خلیل‌زاده کاپیتان تراکتور به‌بازیکنان‌تیم‌تراکتور:همتون علیرضا بیرانوند رو آنفالو کنید. او دیگر جایگاهی در تراکتور ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/31399" target="_blank">📅 23:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31398">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVbgBh0CXBlGBJhm5toeF7dlKHj4fW9PWKAa8dlFfmyRAFEjuCC-SMwfX4N5kAEJni8ZutuaHbVLOiqVjtTYX_akz7rAjFE-K1C3lnfovVs-cAB1OBU8_Vp6wnUv2X6xkPBCCxNURh7EeuZH1RLK0xjgi5ICFEYX9G7WZg33G5Er-qc1ys-6UDmRwv6EyzoMAnh0MBZ2fa7iONQ5qy5-h7FnG1y_f8-Ff8iB9v7y6s0X-MLScXtyjLIBaLg0o4uxWf5R_d_qi1j-htZ6VFxADm5QidJdHXLCa7XP0m0atIl-iiRwz0SOIhc4WOnG0RW-M_NwQbH__Ij5WLZ2YF3a4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
شباهت‌پشم‌ریزون گل دیدنی ارلینگ هالند در بازی امشب به لیورپول به گل تماشایی او به آرسنال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/31398" target="_blank">📅 23:42 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31397">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YN4G4XktZrIPEp1FIRQTPRw3mHczPsaEHJxgxCNn98GLT8INOAW8ksaMO7e2yEq8NCJYevBXtgb6cPcnyc1GKNX1Jh-NXUdSOc_KoBVbbikA1x8n6VeqVIsrBShVRRW8tcOyxCEElBPwAhRn-ZiazKWRCp79TViwzTapRJn0vYe2rCEagvLacdCu3piBW2uW8LNQ-amCE-ihXwwslNxR6UTjxMHoTbXbrVQcV9uZVS38c5J1ivMMUAqI_ndeNrGQ6a5qfvGVJL7b1U1joZTJFCuOIhlUHqSOf1xh4T-gdstw8Y5-As8KNXbzId6x1gpcKIzPqt69jHPmnX2JAoaUqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
افت‌شدید ستاره‌فصل‌گذشته تیم استقلال؛ علیرضا کوشکی وینگر 26 ساله آبی‌ها آخرین بار در تاریخ 9 آبان 1404 مقابل آلومینیوم اراک موفق به گلزنی شد. حالا درصورتیکه که علیرضا کوشکی تا 9 آبان ماه موفق به گلزنی نشود دیگه‌یک‌سال کامل از آخرین گل او با پیراهن استقلال…</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/31397" target="_blank">📅 23:27 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31396">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQRtQfKyRXW6M4rEZN2XfeW5G2SCqWhg5-_aoB7-xGb76iSF0FhJQCNMb_IhcZtFahgCBz5Z7O3gYDpwKcFpfFXKIDeU9b3MB7CB-fjrQOygx5-4u0_Cj9NHj62Ba1lUloqLbJsDVylrGKBZ8J3R7bl_NtRj_npl8LntI61FwL6b43t-d4bRuRDGFcc69nwm13TnFoh4eP33IaLe7MaVsdOG15bIkDjXBZd5xKR9sei8VUQrSc-Tgss42gT_T3azEdFufPhVOO9FS15Ikab2PzwOI3NP5tkS-MqedRLrnV0y5eV61GU--SPs-KCGD6LcUqfPDUrSble7bKpSjwnCqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد رونالدو
🆚
مسی با پیراهن دو تیم النصر عربستان
🆚
اینترمیامی در رقابت‌های باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/31396" target="_blank">📅 22:42 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31395">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/095e7b9659.mp4?token=VIPLxEm5VAvnBN03NzoYb2af-BuxdJdxm1JeceW3ai3-gMq8_hnAdTJaf7lHAgmdKiCFZQOFbWigrtiMIszv0FPpa742TJTHgFE6m-fXZ_aGIghzup8RnIJws5N3Xz-PtZBZRFxT6XrK2diekJeqqCdDmCuP9TSozxISJRnCFW5Zu_KLKvT-jk51Mtj2KA-tzaBfemtuQrBbVhgCOKi5E91Hz7IJnAk4OtUwHxl1mLCaqz5rTqINar2F_d-uSGUBf14Z_pVD20Vp3j310_cCAe_N8fMuRV1jgNKrXPGOC4V0SQUZkLhkTtYRNAJjBO3aG7Kcqi8t6LNqZMLT3a73UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/095e7b9659.mp4?token=VIPLxEm5VAvnBN03NzoYb2af-BuxdJdxm1JeceW3ai3-gMq8_hnAdTJaf7lHAgmdKiCFZQOFbWigrtiMIszv0FPpa742TJTHgFE6m-fXZ_aGIghzup8RnIJws5N3Xz-PtZBZRFxT6XrK2diekJeqqCdDmCuP9TSozxISJRnCFW5Zu_KLKvT-jk51Mtj2KA-tzaBfemtuQrBbVhgCOKi5E91Hz7IJnAk4OtUwHxl1mLCaqz5rTqINar2F_d-uSGUBf14Z_pVD20Vp3j310_cCAe_N8fMuRV1jgNKrXPGOC4V0SQUZkLhkTtYRNAJjBO3aG7Kcqi8t6LNqZMLT3a73UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برگاتون‌بریزه
؛ دانا جین وایلد ورزشکار ۶۱ ساله کانادایی، با ثبت یک رکورد جهانی در حرکت پلانک، نشان داد که سن مانعی برای دست یابی به قدرت و استقامت بالا نیست. او توانست حرکت پلانک را به مدت باورنکردنی ۵ ساعت حفظ‌کند و رکورد جهانی طولانی‌ترین پلانک زنان را به نام خود ثبت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/31395" target="_blank">📅 22:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31394">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-N8bNeNSSkJw2lnAROx--O4ObPLmwdJELk9gpiUfXsK5C7bEE3woA7pPsuddMLOLfCE9jAvUJA6mB717uhTrw0MzlVPhiPgVELq8DRgs0iCAbhm8oIcN2BF99VCBqixfUIsqZKxudirPg_X7dSRHL5HEKR6kCPZCy-FLJpe1tGZtR69OvmgwoYA8grP6co2nHgtK1QswL1FHWJ425XwK6fbB3_L0xXX7JFUdz9g6nC2rp5U7VY1DfkBZJSkPDIT-BRsFahlo7Ey1IyVWnZVOYCzV0ri375AmbJ1Oy287ftvn6WupAJgS9e-u9-SAV8h_zk1SKFVz0Zj_QiWGV-ZFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام رسانه‌های معتبر خارجی؛ وینیسیوس جونیور ستاره رئال مادرید بعداز چند ماه از دوست دخترش ویرجینیا جدا شد. بچسپ به فوتبالت مرد حسابی. پیر کردی رئالیارو از بس حرصشون دادی‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/31394" target="_blank">📅 22:02 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31393">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOIlQJa8nzWXz1y-9W5gA2k0aTy4kru4EVcoZNAzOpfdZXeG7REEbNQksLgRCTAZH84KmO3__3BS2VW5Xmj01ICQLccixBf1hDi3E5cBS1SO6t8-Hfcw8LEnwV3ysqY6JIZerQZHHDaJwpYJ5tAMg7kIG11CFHiHf_Mw98zOnbS2o9x37AwBfkb1EQrslNS6aopAZIqCHB_qjggsOijPMOGOa02-Zz0Bv1POBZ90-zcPpZ_uqdz9HOL_BV9RzWWtozlfLDtFHr8w5PhAGKBTcQMIPznoGTkPzPvOnvNsseuLi6VAbxETTYtO4RJnvft1G7xpqr2PRtVoAHV1bt9WcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مجری‌جنجالی تلویزیون خودش از ایران رفت!
زینب‌ابوطالبی‌مجری‌جنجالی«مملکت مال حزب‌اللهی‌ هاست هرکس نمیخواهد جمع کند از ایران برود»، از کشوررفت. ازفردامنتظر عکس‌های نودی ازاو باشید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/31393" target="_blank">📅 21:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31392">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6abb5815e.mp4?token=dWj2Z9xBpMWniFQ0AyrZjBNyE1oUPyXpPB4F-FUB8NHjwHXno5LvAQc0q14XKBrmCk0NsSnuaWYW5C3nlaiynsexbLUVmgCA3Ev8WMj3WGKTiDNbEHcc8L5oGiFgXz0jU78l00BjBVhAwq6j5cxLNlsk8ZBe9CK6Nc4G_Pl6cDmTv5YgHPiHF_aiTPoRdDVcAgy2rm7wPJYvtFsOswtSp0nsQ6sdvhaM4L-G1fP4BTGxQs2HesUTAnSnic6LvNIafw3LisV0cRlmbijM_ExRsUv_rKTrAy_eN8y_FhjktNVqlj0-yiAyIc0L6H7JFbY53oE1ItGsK-LP0QXmDKNZFDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6abb5815e.mp4?token=dWj2Z9xBpMWniFQ0AyrZjBNyE1oUPyXpPB4F-FUB8NHjwHXno5LvAQc0q14XKBrmCk0NsSnuaWYW5C3nlaiynsexbLUVmgCA3Ev8WMj3WGKTiDNbEHcc8L5oGiFgXz0jU78l00BjBVhAwq6j5cxLNlsk8ZBe9CK6Nc4G_Pl6cDmTv5YgHPiHF_aiTPoRdDVcAgy2rm7wPJYvtFsOswtSp0nsQ6sdvhaM4L-G1fP4BTGxQs2HesUTAnSnic6LvNIafw3LisV0cRlmbijM_ExRsUv_rKTrAy_eN8y_FhjktNVqlj0-yiAyIc0L6H7JFbY53oE1ItGsK-LP0QXmDKNZFDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
در هفته ششم لیگ جزیره؛ شاگردان مارسکا در منچسترسیتی درشب‌درخشش رایان چرکی و گلزنی ارلینگ هالند سه بر صفر از سد لیورپول گذشت و با شش پیروزی پیاپی در صدر جدول قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/31392" target="_blank">📅 21:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31391">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMflmTKbPrRvKvuh_D8SN1JoPCZvK4oze_bb7BJ1wTWhIhkeMWk1XMRExHC9D7wGtQx1A-NP5gOmBUrFedSrTYXKfMCOoMpSFtxUWZnKXqJG_c9PqXPwrvplpgoESIGKo5wOkfO82gZ27-32VH1gYQMPWZxVzS82iD3Jnl2olmo5rCjxjskwYrooJRYHLGpuPXtY2uVc12SQZLZwvx8IaxNO-a7XsnYm9T5jvqGUndKuOsGGwhWXRmzTzTHEw50gAw2jb7cQCsbBrl1ViYZ3OqqgUkmzaMImsWwWkLQuj5PaPrCkJ3wf_9gIzekEa3V8wqb3sfkHUU4T54nomaMp_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ جدایی محمد نوری از نفت آبادان؛ با اعلام باشگاه صنعت‌ نفت آبادان، محمد نوری پس از شکست مقابل تیم پرسپولیس از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/31391" target="_blank">📅 21:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31390">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uhb4ljosXWuvO2eol3-hbc-ZjMSjJHLtBupB-RMTYH5rPdLjPXeKY07maGtaXqaC4z0UBMVe7e_yqXzHmQfZMVLNKe_Ct4YCdIbBc-nGuUQ3MQmAzWI-HXNK_IDFa5A_xF6ur5ezp8bWPA7G5f-T9sS6Bo1geYv5BrwbydktCA_sLgUjcVyhVSRRMkELBzOkvc5gIxW4xkLYAMjy7UxjeNc-tmZ7rhiMluasBUFrDfZsA9E_BHnFu9P0f7T9tzRFp3NcJJmApjsjP4ICMNZgaM3s_x-9ZwU1Y6clv4Yv-OzeQBLTpo7apUkrrBJb1_pfL_DOPvISV41rBGM5Br_1Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
متاسفانه‌دوست‌داشتنی‌ترین‌زوج تاریخ فوتبالم از هم جدا شدن و خانوم ویرجینیا باید فعلا تنهایی سه تا بچه قد و نیم‌قدشو بزرگ کنه تو ۲۷ سالگی.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/31390" target="_blank">📅 21:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31389">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-xplFRa9chvcp-zB_2Ihrim4QHLzaGL6HEE9trTSGpZJuSAss3h2Z0W2cfrz7sFYKfQITyf8BlUqq843uH_W9YjdZEzPWH02Dj4CmYVrhDfJmNsqOKCnnqflAgwSjha7eQvrxT_PDgmfUdvHpgF3hrBVar-dSRyEFzOkLo_s8szkSNoTlivjgUqsO6kR2WSmWzf35h-1FdZXiGqwDokY_0lplL-n8BfNFTNHjEmXywhdq6SzCt32B3xWvh-ZnllT_VsjuMjDqx3yZK8IpigfF2_sXS-GguAft2gZz2KTr9JZ8CQkQam-QEepaWAG-93pllTnaF_wnxHZo_QWlWAgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
در هفته ششم لیگ جزیره؛ شاگردان مارسکا در منچسترسیتی درشب‌درخشش رایان چرکی و گلزنی ارلینگ هالند سه بر صفر از سد لیورپول گذشت و با شش پیروزی پیاپی در صدر جدول قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/31389" target="_blank">📅 21:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31388">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🟣
گل‌های دیدار امشب دو تیم منچستر یونایتد و تاتنهام در هفته ششم رقابت‌های لیگ‌جزیره انگلیس؛ مایکل‌کریک سرالکس‌جوان‌نشد و در آستانه اخراجه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/31388" target="_blank">📅 21:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31387">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LIbOI7r2x2hWPYeNfiN-60OpUzPtgm4E9M90OHfPrPsS_WSeUEZFIBgVhS4FhEqqJZ2CajkChmzBdApVmxrI6HXzko9dtfaZ_5WW2I_lRIDFyDXMevwyu6bfsvw9Wg4g5VGBMO1hkVVfQsHhP1x-5vL22IifcjdThiaZs321u_XgGaQM7CgIhcKjUVt6EbEWCutUUoOhsdP3EJAyS1VhJjdV1XS4z0srMO4C6s85IoP3YAFECpQXhL8CRAJl69QPULzW4VB-sUqJMgy_lt2YLlcDyrSTK1yLJ8oJzvd0mfRqX5akFEjIl4ZNHUXRPV2Tn86S7VSo7H9nu1NWU2_M-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌پرشیانا؛وکیل‌علیرضا بیرانوند که رابطه نزدیکی با علی‌تاجرنیا داره در تلاشه که قبل ازرفتن علیرضابیرانوند بخدمت سربازی تمام توافقات لازم رو برای پیوستن بیرو به جمع آبی‌ها انجام بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/31387" target="_blank">📅 20:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31386">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10ee700462.mp4?token=Fp-PE-eMbwGHFf57XOGsF3Pi6832YXddWtIPFPFPmPItJmuDWrAZ-pihwsc1sC7ZW0mqzXyNae06L2j_y3HmtCgxiJa9UQjGscYiz33cEEIVEbozr7SkXhHh3o4udjiSJDYnSjpzIZO1yqYZCI6PGPjGlcQqwiuYZnTdzEyTjHYYywz2fz1YA4BmOUqHL2DkrQI6lc99_23KcukeqSZd1MF-JusMPB3bra2wvogVqd6sWNPI4GjCH2scFOvJp2fH4HcyCgHQA_FYcpXILQHFX4rqmPk-bnYiGmAGAnKMqkBGB_793mRaSuGOfk_8PfTQYk44kj-I2l8Wxznmck7C078QDOOKYMhrQMATkdBTUj4Dtm7gH3G94u47oRNbESAJekKLUGQjX0GpmB9Z-uslwZzbsqBboqBRm1JC71Cdewd_ZTrFdnRvmXtVubIl6SQ0ep5CYzwcV7bQjeqyPAiZwutQfYOnDyaurJncOisgdlkcP5nUsWcUg7nAofNTUzoOBJRdQH7VvjbTFoSZu5wciC2KuZ4A0172c8fy9N3uJPJlozKYHUhkRUdtGu7V3k_aXHg_lM0_oxHeZMN8-gzwlAte-bvSnYPPK6SJeKE9T-FbDp7D6_X5OjKrk3TxxlPd2yTHDF3khUvFk2Ikbg6faCDhhh4hRmAUXYX8xUaa_x4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10ee700462.mp4?token=Fp-PE-eMbwGHFf57XOGsF3Pi6832YXddWtIPFPFPmPItJmuDWrAZ-pihwsc1sC7ZW0mqzXyNae06L2j_y3HmtCgxiJa9UQjGscYiz33cEEIVEbozr7SkXhHh3o4udjiSJDYnSjpzIZO1yqYZCI6PGPjGlcQqwiuYZnTdzEyTjHYYywz2fz1YA4BmOUqHL2DkrQI6lc99_23KcukeqSZd1MF-JusMPB3bra2wvogVqd6sWNPI4GjCH2scFOvJp2fH4HcyCgHQA_FYcpXILQHFX4rqmPk-bnYiGmAGAnKMqkBGB_793mRaSuGOfk_8PfTQYk44kj-I2l8Wxznmck7C078QDOOKYMhrQMATkdBTUj4Dtm7gH3G94u47oRNbESAJekKLUGQjX0GpmB9Z-uslwZzbsqBboqBRm1JC71Cdewd_ZTrFdnRvmXtVubIl6SQ0ep5CYzwcV7bQjeqyPAiZwutQfYOnDyaurJncOisgdlkcP5nUsWcUg7nAofNTUzoOBJRdQH7VvjbTFoSZu5wciC2KuZ4A0172c8fy9N3uJPJlozKYHUhkRUdtGu7V3k_aXHg_lM0_oxHeZMN8-gzwlAte-bvSnYPPK6SJeKE9T-FbDp7D6_X5OjKrk3TxxlPd2yTHDF3khUvFk2Ikbg6faCDhhh4hRmAUXYX8xUaa_x4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
ویدیویی از آنالیز عملکرد پرسپولیسِ مهدی تارتار در بازی این هفته سرخ‌ها مقابل صنعت نفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/31386" target="_blank">📅 20:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31385">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqmwHsu1AOaX0Dcah0oB9GkBszXcWsZ5P5zVXyUFct_rOPeW2NizKkD6mf_P0DgCq0XNYT2PWKX-_mJ2qlUx-E59P94HKVL09FHoytNAEEY88UWdaOtWWSOtrLZH-zUj0U6RGjL1aJzxCDm9gjMzIWdh6QSHe1LXmQN0c2C0M0y143idGGf129ovZnOWWcjDwbIpe9YtgoFwamRzNXKxTbi9F4mwQq9po0_SL_1yi545j3zb-vhByWMRVcOyueYCjJtogLGsUC8euSjPUYPmC90x_mnWN5dnP3aBJuthAaZri-Pc0wV93h-5-sj9URPedaj-DjZTQcTSUGLoymZS6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیکه سانسورشده از مصاحبه چند روزپیش رضا گلزار سوپر استار سینما و تلویریون با امیر قیاسی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/31385" target="_blank">📅 20:19 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31384">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5BV0aJ5fIqTz_KyYkk1RGmagqhmgQvqHxVDTExvaG_0jAJuh8-QewwagYy_GDxgPKsf09ChXUPh-YxVziUInx3NCw2Bww7vof3vH5W4cBCBaV-H6fSrcdeFQpSmJgsG5U-lDOaR6ZR9hU7gAnjUoFlKaoybQQxEZi5PF4ag7S_M5G1G_m4HlY0I3wT5R3xpGrP79L15HhRw9oO0VLiinr0Nyd22gogmsffRW64llnk-aMEx1_slvs28o2meJYH3986ya4vXp4nqjGWtAzXoLrQChusdsif-F1Z-OI83TsdMHRjkKiqJnPEWGd1n3Wz5CcVMSc9EaHohDeF8ChUuoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق اخبار جدید دریافتی رسانه پرشیانا؛ یاسر آسانی تنها دیدار با الغرافه رو از دست خواهد کرد و به دیدار هفته آینده مقابل گل گهر خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/31384" target="_blank">📅 20:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31383">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ui6-i4ct842hgJXiqCS6bvhAAP-kJj6xh9vYO-WHxTUiGXJz32ppom3Zg1J2IhDNGUyAPWlRXw3elj-Yja_TLN2231K6CD7NFWOmycPZp7j0ZA33ckOmbn1XFCIOSzsptSQFDkI7PVBlpjqrw_RhR04koL9_QqgvJUaB6DRcB_NZAkJ9bgu6ZurnSdpMLZTTfiyrrDByIkHNEk6qLSv99odZzIqPl0drx8tZuCO0qwcg2CuRfZX5NKURUhC0WHzlo7zPo8dXvl9ttWulJ57IQLBbVRmld-sJpZCO1ZIkVF3M8NG9vRugmm7SDkahh_-xe7t_WIB3uATjhi2UoH_TwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مقایسه‌عملکرد مهدی‌تارتار
🆚
وحید هاشمیان دوسرمربی فعلی و سابق‌پرسپولیس بعد از هفت بازی ابتدایی‌سرخپوشان درلیگ برتر: مهدی تارتار: 5 برد، 1 مساوی،1 شکست، 16 امتیاز؛ وحید هاشمیان: 1 برد، پنج مساوی، 1 باخت و کسب تنها 8 امتیاز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/31383" target="_blank">📅 20:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31381">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7n6obwXYAxUig40k1yQ5Az7L8mT_yA8ZJ7a6m_73tCGk7WW75q_MmhaEqchdp_fJt0PxpOwL9PudQeQp4qySMxEtxKJCLWzV3FJC8Yr4lssFw1l1JTbdJqYfTwMPph-1aWgqAVhk0B2Ri7nj2qn7HpFf89Ald_qF8J595EETh8MMhW7oDAnIGXACGFYI1bM4vVHUISpbphv-QSeXyNEejWiGuM0quIsszW5_diM8gyfx7AZgVcEk9kqGI4_72eLqY8CWBcpRns6iw2ucD4Hs1P9sFkUZ6XxETWniyhfZtB_Jo8rfdMBsxO2WkOlKJC3WOoRh7aamkADYYq2_FQ00A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ زهرا گونش ستاره تیم‌ والیبال واکیف‌ بانک ترکیه باز هم نامزد بهترین بازیکن ماه لیگ ترکیه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/31381" target="_blank">📅 19:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31380">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHeFviaeBsw1zI7X9GV2WvrwGDU2rSGaX84MDIZCQjyhjSif1c1vyQxmv5axj0jCcxd6cVzZQMc_r5aSjOs3iT-_pMhiSxARbrfVHGnN7jwl7aP8KLL1fuxVFhfQML9YPou_8ovJPR9CJ8DnGfKMRYYpbEMNMUu-o-5M1S_Kdl0CgvJ09Z2v9Anm9R4g737wyToFWetkJGd7SaqGZx0Ho4wVAH4tpRWoBihFkgGI9kg7rU-Mf3P9CMlBC_KgWhoDiLhIf1OYnKHbKYweMhjLLMUoQoVGJNVBb9s8A2PEp2jvQgFupcNKbF6r_tj5yK-VDnCbeYba1VZnuzd9L1cVkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
سریع‌ترین بازیکنان تاریخ فوتبال برای رسیدن به 100 گل در5لیگ‌معتبراروپا؛ CR7 همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/31380" target="_blank">📅 19:18 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31379">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDODz7zObAxDyBgycWD75iELy9cmsIyTcd2hcajzPTaevXYh9o_OvhIeNGHFrZ0_vxdvq_soaDKBGrAUDsFTP--nprlh1qHRaqGJqs8HKEylX5j3EOFxqChvrOKlUH6QZ-kVL2NWVuVAZ21_b77I7GAc_3DZ6NeJ3QPwmACHHfaaXWzVPL98esTsyE-DWfdeCHx3WqutRvt67qzvDBamZwfDK5ebJrYSIa2V72qT39VUGG0Q4MBnjU_OvesZlI63DpQnqljkV0kdQsiV2xOPg5iBIKtp0ZUnpa7AH9Cbvbzylpq-bduVJwmoX_XLnewvrW-VYkJBWI9B-9j0JhdSeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
خبرنگار تیم اینترمیلان هستن که افشاگری کرده وگفته مائورو ایکاردی زمانیکه در این تیم و با وندا در رابطه‌بود دوبار درخواست.رابطه جنسی با من داشته که هر دو بار دست رد به سینه او زدم.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/31379" target="_blank">📅 18:41 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31378">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JB8zC-P-vPNDql71g7sGgfvs4ZZYPef69UHcdkQXrkBuz4FymTW1k6sazbSGH3avyDKtuyfYgm9xcO4nfo2F2O1ft-KA75mgVnAkFMwVdRGb6pLTJVn_tSvRiR6qVQ-SnnJSKJDE2vJhBXwcj1xhETBWZbnmMPQQqLnv_BN420tYa-yhhcNqe6ywDXorwUyEnDjQt_AGrF8yKFs-is84yGqZgot_X7b1KT3_Maac_cs0qri1XamT54OsbXxPWpSMQHMRd14IcDOeAeQs9WDcbRrcsJ_l0okeD78Mpi4A73boj5bScoXDERl2VllBMmCy48nghESX-rZQf2kaQ9VU8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیپ‌واستایل‌تمام"بگی"عیسی الکثیر مهاجم سابق پرسپولیس که تا آستانه یاغی شدن هم پیش رفت در اکران فیلم سینمایی ما که اخیر ساخته شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/31378" target="_blank">📅 18:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31377">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHBKUcbWz2u2FJiPJm86se8FW8NCnFk7ydCzW9N2qYTsYFCHaqIwWcIX8kHatMUPDhGtds3Z2CWelpks7P3hu6_fZloD0eR6zwEoswptjNIzwUfDs7kwkrcBDKFEqMZqndMK2Qz3SHjvqvwIzX-f6ClXQPMswfU_IIKf1UuOXV2efeoguvO5FQMVwB8Aluc63q6g0O_mr3Zh8-cEpQOcCoub71ggYoI6ag5-lHzhQyR___JmrKZlz3nYKXX5FyzeSlqNsoUiY9Cu3W2QVnrdCWh3OsAObebHVz1OumYUBRFFVTC49b3LvonWxIf69ZjqNQiXzSiEanmILHzFrKNVEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درفوق‌العاده‌بودن رابرت لواندوفسکی همین بس که تعداد گل‌های ملی‌اش از تعداد گل های ملی کریم بنزما، لوئیزسوارز، نیمارجونیور و هری کین بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/31377" target="_blank">📅 18:09 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31376">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGdkUjG-_tGFIcvcTn4JIFwhXLoZJFYDD6wqlo-ev2IHZ8EOamyaifx0hXvbN54PtIDxQCkZYoVa6lQXM6r-lTK66AUErUHoxgx40u1xBNL1L8ei2Z5eO6rcZXhxUVyWoM58U6vjr08Y8OiAeoNRDDyH3Gg8Ik5SsCHfNA2WCv6Yd3IVxCeSZDmJXl50rIPn7PRaT5nFo_R8zkb_7007SGik5a0FEGVHkqkLPmXo8cx8-nVulRE8DZrDT83eB1mOUhboW6yIFgR1JcVLmYrRG5na62sTVbc6ygHJRwTJCFvI-GizEsNQVoiTR95I4HMA9l2jVVrnLt8bIseONFe-Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌استقلال بشکل‌‌رسمی با کلارنس سیدورف مدیر ورزشی این باشگاه قطع همکاری کرد. سیدورف برای تنها یک فصل 250 هزار دلار از آبی‌ها گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/31376" target="_blank">📅 17:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31375">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sotN7ZEZGUh3xLoz91lZ2hnH1_4tHRmp25WH2eKovWVHhObeLnJwfBBXrl8fq6rLt_-pL2bP_Xc1M71XuWiJFoJ-RpKEAaDqESCcC3hNfxsjlMWB4kQUeJ8bqyzPPWNjF97ZhaHr2w0hPkllatTJ_1MzU8IeaAm25R84sC5zocY0TmVCVVAu5ds8XwOmIjBc2gNuKFfZDAgfXk0RKvSqo7Wcnd4CaMj5n-lbg8BMM1Xd8v1h8N1tz6McLM4HlCfVpXMIZTa8-ONSLPxfJzrfQjyOEtsC17PzfGXBubeIzsOCE3LeFMJ_vGSzHwndCCNOsyiNGY6pk97UpYoQ1jpycQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب تیم منتخب هفته‌هشتم رقابت‌های لیگ از نگاه‌سایت‌متریکا براساس بیشترین نمره در هر پست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/31375" target="_blank">📅 17:19 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31374">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghNDs04wGvdUc5aYhMguoEiNo8PcdDHZ1NmoBv0iqqEdee21hftIt-uMvdnFnYGGY03vbaAk8mnC0tQ29zb4ej3RTnhF0Uy8j_yDqdST04avjF9V4bsnK8OseUfO7Ivj2EkJHxQkAEzC781wdW8-_nUjiuJ37YeuLEDOCoZw5VHgk9-awGNTcNM2fxBJSGaI4yfWZxaP95MQCQmgsjUdo2nPrbp7CTNXPkFm44fQUchLI-kl2TsdB-zajFqclPVj-lUIbqVjBjGqvJWRvs5bIRzxdbQrrep9FoNaLS1Bt8IHm8wgl_xmllf_pBpvcbPVn_CpZW0-UbXQ1ZhMU36sPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
در هفته ششم سری‌آ؛
تقابل شاگردان گاسپرینی و سسک فابرگاس در ایستگاه ششم برنده نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/31374" target="_blank">📅 16:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31373">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNZD9jTLjhqxT6i2H-8IPMWLCGdGiG6Ps66iIXazVdx8YBIa3CcihHmcCGLOn_xzCs3chHyb_s1xoLd8dntXyxSAKKoO_Hem8NlZRDq3FXNrZbgvP2rFto-xq6_mooWGOFZWrP5o5h6KPYiyBejuCJsSCXm4j4hduC2Fro51gAu_9D9HxJLwB76E-DfP55R-80kn5ucYjeUg5CYK33Fqp7aKDly3PU40oXhMeGHKsr5excGxibnePWLuypMdAyGIodInsfPXs1tW-qfhrSYj6m5gFO-klKN6aCBvM8MHtmkM17KuoAlXcif3dP8xOb8tF9S5bQgUORxtM41qPeK-dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سهراب بختیاری زاده پیشنهاد حضور در کادرفنی استقلال رو به پژمان‌منتظری کاپیتان‌سابق‌آبی‌ها داده. منتظری گفته بزودی جواب این پیشنهاد رو میده.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/31373" target="_blank">📅 15:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31372">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5469fLHJYZ1WhPYVpkGpgPgu3onsXGxlbbxWYWybSfQvCQd97HzEbiSh-R_At1LpCmDA5AnpbVp0cHFddTo3nshxxX5EPh2VeD8ijWPF0UDanyJaoqyfMwfB8MI9HkLpLig7ArxYefmbAD6IaUKTQqxBUQ4ipJsw2uwsObgX-JzNucpB0b6dav_yvbda15_UkEZTycQyiFOMXqSpJ0b6UYPRJjidfbDegNLLinTi9s7LG86INc5tpzPUMMrPwLsCtcqdR0e56_1dAJzI50LxZCOICmxWugLy5rlTDlFw6hd-CxqoxpK-hXes0rD69gtYTjilxjh8J5jiyA5sr46tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روایت مؤدب‌ترین و باشخصیت ترین مرد تاریخ فوتبال ایران ازسفر۱۸ساعته کاروان تراکتور از تبریز به عمان به دلیل محاصره هوایی ایران: پنج بار فقط سگ ما رو گشته. اینجا هم فک کنم صف روغنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/31372" target="_blank">📅 15:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31371">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxQ9PoM7hmmae7SN_AjOFkr1evpBH8thfp0BHCo0FjcBfZxAkkXUFwheEuSVgDjumY29SZEojy8MtUzSY4u3hIcRUJleQ0NkVhrI9NaTri_TbRyTWNf74uajSh-Vz3zka6Cgztji7AOUNAOlyTh3LKfP6qC44enTaA1rpvkqlXb0XRz8mGS1QvHkcsIli8VU7VQqvH9vLTzThOkBw3HNBSkctxX43G52RLKc5asOgQhSm90MlnEngWEFoEZ9CEukQ8d4P8xcdObCqMzPgXQtUnln2ReTz6DC4QkzPuXS7rnxeH9aXLwgjk-PQm8-YtqOpgOR1D1-8bZ6_LVnzmi85A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ ضربه بزرگ فیفادی به تارتار؛ علاوه بر دانیال ایری،محمدحسین کنعانی زادگان و علی علیپور دو کاپیتان‌اول و دوم پرسپولیس به دلیل مصدومیت به احتمال‌زیاد بازی با صنعت‌نفت‌رو از دست میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/31371" target="_blank">📅 14:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31370">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f85d440852.mp4?token=fhKcdrhNrgcVuKoaQ3j8o2nCWDaIkd0vLZfgRrctfNfHkFnC-VRVeSklB_zojnXIjVRbAglc7B6i8mc86Dy_wU5M8TfCheKlmF64f6ufAx44sg44n-YGEl9Tq8J2dkSQribNw56GjLLZX5M7cnQpFixzsPSDmcdxYpak4SZZRjsE7jbme51MDmRE9c8Nr0XxcvhtSvIT9fGhZuckq6KBiQp9UVI5ojDqLUIqftl3hTazY--CgvguwYNwYz-fl0ObydlA8tHGhekv0ATIPM6FdSZhi2TW13fGf3j4oGZRISD0zJrtmq2A-VV-TQhoiNekcgJlqdjIEideySMX_pYCBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f85d440852.mp4?token=fhKcdrhNrgcVuKoaQ3j8o2nCWDaIkd0vLZfgRrctfNfHkFnC-VRVeSklB_zojnXIjVRbAglc7B6i8mc86Dy_wU5M8TfCheKlmF64f6ufAx44sg44n-YGEl9Tq8J2dkSQribNw56GjLLZX5M7cnQpFixzsPSDmcdxYpak4SZZRjsE7jbme51MDmRE9c8Nr0XxcvhtSvIT9fGhZuckq6KBiQp9UVI5ojDqLUIqftl3hTazY--CgvguwYNwYz-fl0ObydlA8tHGhekv0ATIPM6FdSZhi2TW13fGf3j4oGZRISD0zJrtmq2A-VV-TQhoiNekcgJlqdjIEideySMX_pYCBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
ویدیویی از پاس‌ های تماشایی پل پوگبا در مستطیل‌سبزکه‌منجر به گلزنی هم‌تیمی هاش میشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/31370" target="_blank">📅 14:40 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31369">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MK5RuseOKoechjr4hjEC8C08x133Q_af30uMhTUkWmuMO-SCpscRB4Q-XIHORTUv4UTZiav_nbYTOf1AP95qpmNhhw_xWQdGLz0KqHC8k64DFkQDJcRwCfb_uBvnP0nGNFbJdShOlSU_-AEpF69D9sIpg4OCqK6gwy_JHyRUjr-eoJKmN5RxKQsjhaKfHO4nGcQW_l-9w5nEzyKNgKKU6ZPkl6qvF8DO8LN-iIpX6Ne6-61dKa1DDhvySOevXKoIWw0rRjfUasl4sdtfwEyakHtMc8ZZdkFmnk8h_wA3HLlQHVYmPoou7qpGI7TOPZoA117E_7S_1oQONbWfQLQDGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌پرشیانا؛وکیل‌علیرضا بیرانوند که رابطه نزدیکی با علی‌تاجرنیا داره در تلاشه که قبل ازرفتن علیرضابیرانوند بخدمت سربازی تمام توافقات لازم رو برای پیوستن بیرو به جمع آبی‌ها انجام بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/31369" target="_blank">📅 14:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31368">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ReEm7iaxiEEDxombjAYEOdbrOSXJIsfE0i4P8k08EX972zmjqIVyAUJmO_EM9ATxQ2bKFhqfxfxbgvuQKKgTPZ7DvRQA96qNNpMXy9Rdrg2Ec0wUPaI5DCW7llJAP4uOQ9ytCWGo9GHBOv9PiN4RKMJMUPjuLGZps7OSy5h7NhZnjVbdAuhvxb1ohO-CPGUf-W4aifqC9dmOpKktRTc8lsiFwIpkMrmO4dGMAiKYHD52PKfCrUEjKNJzL2MeImsIrO30GUL-xRNHvddoi27m7DPFs8r9E8P7zELCZXAslsOpnVIdBuL8XM0ZRoP8IU3CwFoR3ZBKvNP3ezi36puf6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگار شبکه DAZN ایتالیا و از طرفداران تیم آث میلان که گفته روسونری با روبن آموریم به جایی نخواهد رسید و باید او رو از این تیم کنار بزارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/31368" target="_blank">📅 14:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31367">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptAcXdvNPA7fJ23tqEw3i4S-yMZGZVfy8rCpB-Iy-vv4t7O4p5nV0OBW6_VK_6P2fOA5wyxjVW4rXnPtCY6mW8BAehRnP_JHwPrrZhxhP8lV-x-6GMe47MvjLAf0I6MxS3wN9qnshuQJgEVfVSkufAld8G_p-rNrrRsMDwhi4e9Ve9mVHMR6w9bTVhxaKAH6WZ34R5cTc4fCgIUdO542CGGZ84tXvaIooNkEavCKvIcAwcUvpDhwdsE9oKeG9_Bx7PFJEnfRoe7ICVuXFAW2alkA9NyMzsfjHTfaTvui7e2RX2jqcBm_I0wvg3ROIURnick9cSH-bh7CBaipakkyAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ساکت الهامی سرمربی پیکان قبل بازی با شمس آذر: من‌دیگه‌اون‌ادم‌سابق نیست و دیگه دست به زن ندارم. ساکت الهامی در بازی دیروز با شمس آذر:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/31367" target="_blank">📅 13:36 · 19 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
