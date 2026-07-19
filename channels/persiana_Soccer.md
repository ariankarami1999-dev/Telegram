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
<img src="https://cdn4.telesco.pe/file/Sj_AD5fqWsUfV7kg6KEA1B7cVyu8TYJ1u2kzHAU9h8ok4dRLkLTBW05a0r5ogGRzP_aZpEpDGK74TpFvjoHxrUHwUulemIxpci3uQ-b7uIX_1VerRCoaeCw1C-m0FSby-sld5P8ugtBMSRygfovWr8oqNGcx2DGL66u_P0rUSUxN2CrK3Hu9OcYxocAeXVNXQiwpEP0b060Ri6RGLCDXFyKy-FZAufaGhygqcaJA7cbOGEjYFxzx3uJveC40SuqLctIiCsepB7CqKHOdPykp_-4ebG3QV6kaxr4PFQ0bKdj8DsWvpjF3IA5N1DW-2CRd5bKkyKQZ-q6OrIXKkdhEJg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 521K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 11:07:53</div>
<hr>

<div class="tg-post" id="msg-26046">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYNoVGU2_YBIlp7PBA8RLt8p1lE26kXSsLAcywSRjA0luwxfprcjuWNM_-oCkqHN5LHiIvFMYLHyPjuA_uuHYTL6NCYQXZ_B7WTTjX_m7TIDcrBDW2bgUfFaPpyg5rDN_JZEeb_E1UMzhbyKyWDh4rDMIIno2VTEM971aOpDf4fdC8VWGhbivZbZEFmltNtjMabfoWSXF_3vaRc6HYL-CFRLxqVRw5wbQd0jvE83LD_rcidsXytUFV0zamTarnPq9Gh6PXYZ7E2uF3RZPekS6NN7KFYBXX-4RbbZUH5sZH5lf5pcUbnwKYCK98FEF15yVemaBrWXt-z9O1MzcO9MkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇷
🔴
#تکمیلی؛ رومانو: آلن هلیلوویچ هافبک هجومی 30 ساله کروات در آستانه امضای قرارداد با پرسپولیس قرار دارد و مذاکرات این باشگاه با او در حال نهایی شدنه. هلیلوویچ طی 63 بازی در فورتونا سیتارد آخرین تیم او 6 گل به ثمر رسانده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/26046" target="_blank">📅 10:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26045">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgFaoQX9ImNhn9TSi1O-GFrLWQK5hSqwSbOjps3a_J5aVUIE4tyq9SMrWQtHFDKUOA8E-L7NNAf75AA2TMNRcJZtrEL5KJIiFot8zS8LUQnoHzLlMrC0E5B2ei8A_obUpsce-kbdzXpkzgoR2jehYyIpcivKMYjSkRRpGOijoufasTxZXn27w21oQdigqDQMKy1WyhRmJ0mtP20of1wXWwB_PFTt52cfAi57i0X6OtlU_2Me4JOCelWl16ip87-7aM0LQmLpTgtR6MxhZ9nRhMOO5fcBB-dpTOGAIaNyWHX2Bq7atXw2xNVT_EOPcsg8n0tStSWNpWi5EaeOJlB89g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه نساجی بعد از جلسه امروز با باشگاه پرسپولیس رقم رضایت‌نامه دانیال ایری مدافع تیم خود را از 190 به 150 میلیاردتومان‌کاهش داده و72ساعت به‌ مدیران پرسپولیس فرصت‌داده تااین‌رقم روپرداخت کنند در غیر این صورت توافقات طرفین بهم…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/26045" target="_blank">📅 10:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26044">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">📹
ویدیوجدیدوبرگ‌ریزون‌میلادکرمی بلاگر معروف و محبوب ایلامی و ببینید. رفته رو پل B1 کرج!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/26044" target="_blank">📅 10:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26043">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2k6inj52MHQE0E4qqpkQyDFXLTIMtc4Nb3AfM6YA2q1ztjgeLRQRcJ454zA7un74k_jAMULHpwDun6x-xmyVJg_4tMRl7EtWICnLF1vQxmmWwyAF7rESatGVIhI4vHBt5IX8Vu0uqKa2xX11faQSjbiAdxB_nCdoy2w8_0q-S7m0m8UXuLs8vwfQzOQjRogOJPI2ImILH61ni6Sx7Pr_A8pzZigaYdgRQHRzaP-eQt7OuUR5rRvd1omKp_iZ1Kjjb6ReowN9cgEul6k9gcP3DFy9gxRU0_NWruY7YlDb9lX7JcWkYIQUa47OnfjsKu91-ty1a5nw6ggKOLRAWs5Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
برای اولین بار در ایران ، فری بت
0️⃣
0️⃣
2️⃣
درصدی وینرو
🎁
💰
سوپر بونوس
وینرو
، پیشبینی بازی فینال جام جهانی با بیمه ی
200
درصدی
☄️
⚽️
اسپانیا
🇪🇸
✖️
🇦🇷
آرژانیتن
⏰
امشب ساعت 22:30
🚨
ورزشگاه مت لایف
🎲
با وینرو همیشه راهی برای برد پیدا میکنی
🔊
🎲
سایت وینرو
با بیش از 400 گزینه متنوع برای پیش‌بینی
📊
ضرایب ویژه و رقابتی
🎲
ثبت نام آسان و سریع کلیک  کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
🎰
پخش زنده‌ی تمام مسابقات
کلیک کنید
💰
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr28
📩
@winro_io</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/persiana_Soccer/26043" target="_blank">📅 10:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26042">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05254735f5.mp4?token=PVqA_9t-85aOVTFAk-YemeJBcGAWqIVpQYUZ17kKGAi5GP7aguVi6-U8Tz_-IwlzLnEQMn8ZdywgeKNYHm0qLUElWzPJiOwxDz0ff0-qArt8qLoi-l_cqj3CYIR9sjvMkgUGZh-Vxz9Gb9Mme2lYm12HjrAb8yB4pCEhzvhrW3t3HX0dSCXHmQuaBrbJdUYJnQ8FoUwTkntzYR7V4BBEqFdU2K44eL95hjSwDavRuLELEjV78xyU_rNMIsJE6zxukLstSZzUMbt9Al_aLeJMnJVUihMNGCELBtOHvgoq6wI710eQ45_Iy77XQDquTOgtARPEgoQkEX7_Ap4nyYtTqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05254735f5.mp4?token=PVqA_9t-85aOVTFAk-YemeJBcGAWqIVpQYUZ17kKGAi5GP7aguVi6-U8Tz_-IwlzLnEQMn8ZdywgeKNYHm0qLUElWzPJiOwxDz0ff0-qArt8qLoi-l_cqj3CYIR9sjvMkgUGZh-Vxz9Gb9Mme2lYm12HjrAb8yB4pCEhzvhrW3t3HX0dSCXHmQuaBrbJdUYJnQ8FoUwTkntzYR7V4BBEqFdU2K44eL95hjSwDavRuLELEjV78xyU_rNMIsJE6zxukLstSZzUMbt9Al_aLeJMnJVUihMNGCELBtOHvgoq6wI710eQ45_Iy77XQDquTOgtARPEgoQkEX7_Ap4nyYtTqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی امشب دربرنامه‌اش و در گفتگو باجوادکاظمیان ازجدایی‌اش از اکیپ عادل فردوسی پور خبر داد و گفت جدایی ما کاملا دوستانه بوده و ممکنه بزودی به اکیپ ایشون در پلتفرم ۳۶۰ برگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/26042" target="_blank">📅 09:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26041">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59f65ac5ad.mp4?token=IgC5NHGSeHMOUQ-Eco8tg2D-YKvAWus2NaZWdudhcvvp931Z_ZeruWpAfbyw5nfzgxfSeq8Z1nALAJUncUpTSz8WWNnoQH85WRvqU3Tk3yNffFsX75tKieYzeum8PYOJwQyyD2upEjFhZ2_XWZ8LrgwVyXiyc7e24keqR_bC61Hl-TPA1Vgrqv7HzWwLylKHt6ih6Qzo94hmpJFsY0DkY69iHHJeOLmXNd4PNPRUowWyKNT64UdHC8IeeaWspIjtUgwzN5FoRO0uo25cfUFwFONuOBMwkqaJ9-fiNbudoCjoQZa8XSyxgpkmp2rEeRE4HqyCaEtNHTEelMRAhDTJ2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59f65ac5ad.mp4?token=IgC5NHGSeHMOUQ-Eco8tg2D-YKvAWus2NaZWdudhcvvp931Z_ZeruWpAfbyw5nfzgxfSeq8Z1nALAJUncUpTSz8WWNnoQH85WRvqU3Tk3yNffFsX75tKieYzeum8PYOJwQyyD2upEjFhZ2_XWZ8LrgwVyXiyc7e24keqR_bC61Hl-TPA1Vgrqv7HzWwLylKHt6ih6Qzo94hmpJFsY0DkY69iHHJeOLmXNd4PNPRUowWyKNT64UdHC8IeeaWspIjtUgwzN5FoRO0uo25cfUFwFONuOBMwkqaJ9-fiNbudoCjoQZa8XSyxgpkmp2rEeRE4HqyCaEtNHTEelMRAhDTJ2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌های‌سنگین و پی‌درپی عادل فردوسی پور به امیر قلعه‌نویی سرمربی ایران در برنامه شب گذشته
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/26041" target="_blank">📅 09:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26040">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده و مهیج شب گذشته دو تیم انگلیس - فرانسه در رده‌بندی جام جهانی 2026
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/26040" target="_blank">📅 08:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26038">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XVxzpmbEY6mITACJAKa9qjIk_hVZVBmbbDMuxOTgVyugreOb8Fzrx6-wGQ7IrtwpR_kENLRbdg40JcNCLh6-tNyLtVgDUozGdVzKmHebP7wQ-HP3AtUcsT7QXDSO0l7lxpZuzns5Ilh6HhZSs67lZSakB9Jv_BUUuNJb1B-WIuAAzz8SZuCGiqa5iFu0gL3FShKHur7frnFPdHW34SLajFccUUO10jEv9l4wqhVvLdgwRxvIH2Ri3FuP5r_eAqFuFpCL1KlrRXne11tgiTkjVCOV7YHZHbcmtLdccIbkR1iyi8Ye3jAHkOk4CiTV2NKUGroVLDsm5U1_YtDSpcRDEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c3fGNcp_ivrtnTPGV2mH9qSVIhLCb6xho4xLDmmYju3O3lDBIc0-9KyJd5nejcwfpNg4uDksrpbAGAnV2zEr1mjcT-esXOO_3LMlSzfHEltrsPB2KpXWDWRmGGWK00P3RVuaTrBDRW10fBBakJyJI9jtbJeKBv6dxtk_UWxV8finwRlvwActZUSD_22uD5P9B8W4U_dGUDB-PGm_gJ3yOZKxb1LJdX647lNRMIoE3GW_J9GH8hflf2sNK3MgylsWZ_-F1JispIfKKzjP3Z28q7Cn8NxVtQD37tEEp3c4ss1z3xBkfckSo1SQWCmJJyqVyIVasLt3PqY-hXQhVQW92g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
تیم‌ملی‌انگلیس شب گذشته در دیدار فوق العاده تماشایی بانتیجه6بر4 از سد تیم ملی فرانسه گذشت و رتبه سوم رقابت‌های جام رو از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/26038" target="_blank">📅 08:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26037">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QcHflUBQBkS0ovX6xWDvoG59eNnbpxSEiV5916uIAHKkZSP0ScUjpDl4dv-5-N183t_5scp320xFPy_4p-GBCiDLbYBKSQZvFLLyy2A4413IUO_uPbfXPgsDOWJ8g0__6DOuA623ooAFofsJKkx6FWJ6Yv6Um7WadhnTEScprtsplRNA--E0UapT7ArhNuI1qzv11IpoynHtuLJQMwVC55YtQIwxPOd2sHM2LU6OZiiaVdgklbQPC5KOHOnXvImHEWP2qQ7COiGJI3Gt-JBh_vXkd1hPFPkh9zgKyvnqurvf_MRECvIP8MTJDqi0FRN0zpsPZa6cPSs-3zYuOpVCeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مسابقه‌رده‌بندی‌ جام‌جهانی 2026؛ شماتیک ترکیب دوتیم انگلیس
🆚
فرانسه؛ ساعت 00:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/26037" target="_blank">📅 07:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26036">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b8dc0f4db.mp4?token=nxkTjt3JSyAt2-9uJ_vGLOZUPfNIeAhs8PflaX9-CFn1wG84NDs8LrDlGF9LI_Vcl8RO5cPPFNuxiQkq4Alsgz6Kv2WlPMSSAafoPJG_6GmVKeQ1gCjbyRCa3hIazflTnqM8-sOAQ2TCUxeCCvThaDp66rQxaea79PTMHdUwTP4PDW1b3sgJMdOLR-ltjgjtDdaF0cENw_a9nx3tqm8_IytLNvsTKm1e358zH8rZxfbixLhwvGDdiK4q2LIqckx9bsshsbMpPah78ubVZZ7Au9k71yR7FmAitSBTwemrt_oHgxGzSvMBulXAnL0ksNSIIzUBszbWTQaz0qOmNURjbr1s8rhls5qFtju2RZq33TDhZTEK-CNxSPE5SS2y1iaV2Jn--xJDVbaxc1S9-9Ab65wXDHwrM5CX4gQehx5Eq1_y7BiiSzd3CcBBS0uKciknd_JY0S_Cy78P5Aqn591XG1_dGkiiZ04ElThGzb4wzveK_4PFoywGNpt7Cmp7OyM-TiQMcq2Rw9uIjwTyEIVL7l51XgaTYXoMVn4Vj3MAqdAanfRuhRZ6dJErpVVBRiLryQGs8GRVJ3njy_G3nAnhI96IudS8M8H5SpDPmTJQlaMhudPsLUqwL3D0LjYBe5neGR7PIzMlwYPEHhZtyxetVEgAmp0gBSRfBhx0EhhPBA0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b8dc0f4db.mp4?token=nxkTjt3JSyAt2-9uJ_vGLOZUPfNIeAhs8PflaX9-CFn1wG84NDs8LrDlGF9LI_Vcl8RO5cPPFNuxiQkq4Alsgz6Kv2WlPMSSAafoPJG_6GmVKeQ1gCjbyRCa3hIazflTnqM8-sOAQ2TCUxeCCvThaDp66rQxaea79PTMHdUwTP4PDW1b3sgJMdOLR-ltjgjtDdaF0cENw_a9nx3tqm8_IytLNvsTKm1e358zH8rZxfbixLhwvGDdiK4q2LIqckx9bsshsbMpPah78ubVZZ7Au9k71yR7FmAitSBTwemrt_oHgxGzSvMBulXAnL0ksNSIIzUBszbWTQaz0qOmNURjbr1s8rhls5qFtju2RZq33TDhZTEK-CNxSPE5SS2y1iaV2Jn--xJDVbaxc1S9-9Ab65wXDHwrM5CX4gQehx5Eq1_y7BiiSzd3CcBBS0uKciknd_JY0S_Cy78P5Aqn591XG1_dGkiiZ04ElThGzb4wzveK_4PFoywGNpt7Cmp7OyM-TiQMcq2Rw9uIjwTyEIVL7l51XgaTYXoMVn4Vj3MAqdAanfRuhRZ6dJErpVVBRiLryQGs8GRVJ3njy_G3nAnhI96IudS8M8H5SpDPmTJQlaMhudPsLUqwL3D0LjYBe5neGR7PIzMlwYPEHhZtyxetVEgAmp0gBSRfBhx0EhhPBA0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت عجیب‌وغریب میلاد کردمی بلاگر ایلامی از افتادنش از روی صخره بخاطر یک تبلیغ کلینیک.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/26036" target="_blank">📅 01:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26034">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf49687f0b.mp4?token=r95dhP_T6j6-e0Z2csynEm4Q9wlzge9DUBfWgStJruoFSXy-aLf5ke0dB8nY5QvjL_kGTQsZD4Xh-ulf7G3MopozgC5q4u3ghWSHqQ29YNm9H9qIZR1P4EKsGKtI0-_opA49W8na8T65Mu46u6ESXNcEKymhKWtmfmF6o2U7fFuDQaRNrIOeQsNQiOd-30V7c37ZNdddT-7azOwXUu614S86qjrrFrWTPejTOwIwQE0Q78OfDaYMj6hqH2F_13H9bHMkceC5LpcGWdkQHAtVsi7JWcJsXuTX96xeGgswdSOJq9n6CwqguAD1e8AAiG9WiNj20PT-mW9VeFT7hXl8Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf49687f0b.mp4?token=r95dhP_T6j6-e0Z2csynEm4Q9wlzge9DUBfWgStJruoFSXy-aLf5ke0dB8nY5QvjL_kGTQsZD4Xh-ulf7G3MopozgC5q4u3ghWSHqQ29YNm9H9qIZR1P4EKsGKtI0-_opA49W8na8T65Mu46u6ESXNcEKymhKWtmfmF6o2U7fFuDQaRNrIOeQsNQiOd-30V7c37ZNdddT-7azOwXUu614S86qjrrFrWTPejTOwIwQE0Q78OfDaYMj6hqH2F_13H9bHMkceC5LpcGWdkQHAtVsi7JWcJsXuTX96xeGgswdSOJq9n6CwqguAD1e8AAiG9WiNj20PT-mW9VeFT7hXl8Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🎙
علاقه‌ شدید‌ جواد کاظمیان به مونیکا بلوچی ایتالیایی در گفتگو با ابوطالب: خیلی دوسش دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/26034" target="_blank">📅 01:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26033">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b649a7091.mp4?token=sRyxfvaK1Ua-OABJsjTPHIrrMIpN6YbsCXNpbA_9AAx1aSkTAiKqXTSxIIddnTY9ad6ay4D7Yw3xNUsdwSRb5IL44s3gTNYHSmf74EpMJ53l5P_SgVJ2xEWLMZXPu6ic-YBiEFoQEkEU6y-LNLfIbFPEo1APysXUvZ-1qNwOwHqwie3Jio5RFtY3yan5MvxvYTb1l87hjPuUW4aU3oqoA2VIy3rhCXasDYyFJGW5CPx6LAD7YXV26ve2SJNILwLdHfOrjTnPMoChEnB6a0inwPG-sf6bOr9acsZbnYyZan3RU67byw7fR85WX5MKtTMr9CTF6DiXJR-_918BDL_D7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b649a7091.mp4?token=sRyxfvaK1Ua-OABJsjTPHIrrMIpN6YbsCXNpbA_9AAx1aSkTAiKqXTSxIIddnTY9ad6ay4D7Yw3xNUsdwSRb5IL44s3gTNYHSmf74EpMJ53l5P_SgVJ2xEWLMZXPu6ic-YBiEFoQEkEU6y-LNLfIbFPEo1APysXUvZ-1qNwOwHqwie3Jio5RFtY3yan5MvxvYTb1l87hjPuUW4aU3oqoA2VIy3rhCXasDYyFJGW5CPx6LAD7YXV26ve2SJNILwLdHfOrjTnPMoChEnB6a0inwPG-sf6bOr9acsZbnYyZan3RU67byw7fR85WX5MKtTMr9CTF6DiXJR-_918BDL_D7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی کنیم از دست دادن فرصت طلایی توسط گاوی؛
سه سال پیش شاهزاده اسپانیا لئونور ۱۷ ساله به بازیکن جوان‌تیم‌بارسلونا «گاوی» علاقه‌مند شد به طوری‌که همه عکس‌های گاوی رو داخل پیج اینستا و توییتر خودش پست‌کرد و ابراز علاقه نشون داد؛ بعد مدت‌ها به گاوی پیشنهادداد اما گاوی در کمال تعجب قبول نکرد و گفت تنها عشق فعلی من بازی فوتباله!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/26033" target="_blank">📅 01:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26031">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9WDrmxR69nacbZj4X_MX7oY7FMjR8OMYScy3ULJoLavYphkfeW_qPLPe2C7GLsJqgwLuV3VOPh56QY2qH6HaPu3LvIYQkH8b3PADKchLinLOk_DkOTVJK0Jngq12fC1Asrqi8oNNi0dvOzD5jnINGIoS4ybz_e0Tl3ft1MIoRwKI2jux1rr3HIhEvuREB2S7CB7MsYiclWRpPwRRQDnZVOSwR4AGCzV37Nm1wCmQSirIPTtrvFnsybQ7e9Tcei90hwhbAIKYC8EZ9TPBeMYL0mp1r_LzjtVcvfLP-GIoT6MHrwfa9kHCA6-hakmrNJDCi5gYOwPs1Cln-1vjFs5TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇷
🔴
#تکمیلی؛ رومانو: آلن هلیلوویچ هافبک هجومی 30 ساله کروات در آستانه امضای قرارداد با پرسپولیس قرار دارد و مذاکرات این باشگاه با او در حال نهایی شدنه. هلیلوویچ طی 63 بازی در فورتونا سیتارد آخرین تیم او 6 گل به ثمر رسانده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/26031" target="_blank">📅 00:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26029">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767b719cdd.mp4?token=LuEszKXjVCS-BTjDySMHr0D9Dp8V8NbxDbPm7ZBeVpRGOcbk1Vur84CTS1hX25V4QVW89TyCqGfo1pUDN0O7gi_1v498_XzbvSwJGQeOy4KHjitnBIcB5opZAuyD_zk9rfUrH8XzztiyUtz64XMAN_VUDGqJBAivjFo_J3UZo4KvEfMNZmzPpm8HeRfGx3oeTXdh7OLiEplXeFCMrq3ABUJWvt7YsDHVHC7MiGZaoxr6Qdm0qBBdyXFlFgoA4PRcK4ZJUJdbMG-qyLqUWJQjRhqlnvxNKGHrfDhl_JIiYV4CaxDj5OaJZqfwIeRa6oe-gtrzEznEjgHg6RE7B8K5wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767b719cdd.mp4?token=LuEszKXjVCS-BTjDySMHr0D9Dp8V8NbxDbPm7ZBeVpRGOcbk1Vur84CTS1hX25V4QVW89TyCqGfo1pUDN0O7gi_1v498_XzbvSwJGQeOy4KHjitnBIcB5opZAuyD_zk9rfUrH8XzztiyUtz64XMAN_VUDGqJBAivjFo_J3UZo4KvEfMNZmzPpm8HeRfGx3oeTXdh7OLiEplXeFCMrq3ABUJWvt7YsDHVHC7MiGZaoxr6Qdm0qBBdyXFlFgoA4PRcK4ZJUJdbMG-qyLqUWJQjRhqlnvxNKGHrfDhl_JIiYV4CaxDj5OaJZqfwIeRa6oe-gtrzEznEjgHg6RE7B8K5wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره علی کریمی هافبک ملی پوش سابق استقلال از اسپانیایی صحبت کردن میلاد محمدی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/26029" target="_blank">📅 00:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26028">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOlq5tuGWCWQABQA-YTDCxSeglP82PztkLFyhxfMOwbN59mmeSZaBBsJZeFU_reBeLH8Ma1vpnzP6ipXKch1vYlNmTV1FrbloFEU777zsQ4_E1apmxRqg-PkwLAQUt10IlHhakHejO4TExlzE3n8aoPQVc0E5udAxiAwf10s9pT4PtHGFBoDX8rHRTZMJDOQUEZ6nbNHM-lYl57YvBukxEK2eJiQNtNIZFdK8RYtnNF8MuOnLNHqb9Aq6abg9tTvCUF92IwzldQSAR_i2al5cqXJVrDDsryF-Ek2dt_d7Qv9yw09ITl3CnunZ_cnYiSbagLJtkzqkuOBxuPEtyOKRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌دیدارهای‌امروز؛
کمتر از 22 ساعت تا نبرد تمام‌ عیار آرژانیتن
🆚
اسپانیا در فینال جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/26028" target="_blank">📅 00:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26026">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rm6V6PychbIT_nDrSJR3xAbFfNP_JdjjdbevAvsGjrHb7WsptJnj1dchP7CLGid7WKqTpUx_1BlYjeDDygauidcwBj59b5hb-o2eG5ivhHmsbUOab5t8xgJU5grqGMWAjal4Aq9_8vURmwD1L8iH-dqAimdeBh4v3DGJvLsgZqr_5U2iUkWgbcGyOxovPnpQmnR-bQLGfgu6csFbJRowxA-6tI5sBgP7oz0Movt-bgm0ZKEXChwvdwRN6Ww6QXUR-cg6pL1Pq7-YaZwZBOSG4aBZlXnLhiVW8gn-UmkwKVl1m-SSRIXlL_agEotGqpBE51oSM_FR7hw8TnLiAxK58A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/26026" target="_blank">📅 00:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26025">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGjHEXzYez31LfZLWxXu5korvtDMCDNDM1fvMmu3ncvjHg_tjyKGAWkSX54zQtGizfN8-PHe3w5n6440zGAiE7bqYsedX32_7Tbl7UTUw1TOwwId4VtOdXP1VUihl6OEFMil1Lxqi7Oi7f_EaUXBNcGVMwOrq_INy-ya_StOmvf7VNt8R5GpeNvwS88pkvtzuFYZ-bUm8PyxQHXaQvGRmEn4rrGFTv1OBRnZ7QgT0-6GNeA8tf4zR0EMW9dnYRyZo-r0fXihQctJZmjayiPc7Zi2MMx4QDPmyDYNOwMRUztqp6TWn6lvUnJX3R-NDmP1dhPij7jYmyVyAimRbL3y_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/26025" target="_blank">📅 00:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26024">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ae80f717c.mp4?token=L6cejANz_3SrtkwikIleMLtHmkd-W0N-_pVN6KoK9PlGMfUk80y0qs7jbjN0APVHDLh0EjBai6k2RdQX-YuY_lMpNZO385HzQukN1ihfL26jZ7zlvqGjtZ8RX6WwRa_Z5pa81M1srU_7HcQCH5mgSF0AUji2sxZIoMpxGK1VnvNZElVg_mteihYHPS7rEpkEUQnCkZQAcvfhVzI3pY1Em1ve7La63f3mWkw9IKBvvuQADuVQt4cirHaaIhdacfSbqpiCqptZ5Fv4w9bCp8IV2sIPOfcOTRGngH7mKrIWyHYRBg_jwUotKhppDjGVjW962FutEO7YYAIdjc_7OzwImA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ae80f717c.mp4?token=L6cejANz_3SrtkwikIleMLtHmkd-W0N-_pVN6KoK9PlGMfUk80y0qs7jbjN0APVHDLh0EjBai6k2RdQX-YuY_lMpNZO385HzQukN1ihfL26jZ7zlvqGjtZ8RX6WwRa_Z5pa81M1srU_7HcQCH5mgSF0AUji2sxZIoMpxGK1VnvNZElVg_mteihYHPS7rEpkEUQnCkZQAcvfhVzI3pY1Em1ve7La63f3mWkw9IKBvvuQADuVQt4cirHaaIhdacfSbqpiCqptZ5Fv4w9bCp8IV2sIPOfcOTRGngH7mKrIWyHYRBg_jwUotKhppDjGVjW962FutEO7YYAIdjc_7OzwImA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی امشب دربرنامه‌اش و در گفتگو باجوادکاظمیان ازجدایی‌اش از اکیپ عادل فردوسی پور خبر داد و گفت جدایی ما کاملا دوستانه بوده و ممکنه بزودی به اکیپ ایشون در پلتفرم ۳۶۰ برگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/26024" target="_blank">📅 23:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26023">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69396b76bf.mp4?token=kmCwpu7bjjUZCTLtO5mmMkW8Su4hFX7u2rx420C-q2aDC8sSQKbfEfNOVEKAwMUf7brqO269DbcnXwel6Ie6AdjQe7aLNzXy7Mq4QbU-jE3z-cSfquwneB4KaIHC9zK2zReU9yjuh8BhzFWYbpT3LnGz-yEth5ScJEQBcy-ORuhi6fmNBCeu6q5n3q8PpZkriB_ylWpDnwB-oaOWwI14chDA2b-PnlvIlaaMD-u4VFsa37B44N2fZbXYouxCTUbyTeD0CjmR0rieecoTTv_c67hbqP8w587-OL7Gez6qG1Ex6oMAdYbK9vzQpJ-eZfANVibtdZ52Qbv5cp_eVQW-tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69396b76bf.mp4?token=kmCwpu7bjjUZCTLtO5mmMkW8Su4hFX7u2rx420C-q2aDC8sSQKbfEfNOVEKAwMUf7brqO269DbcnXwel6Ie6AdjQe7aLNzXy7Mq4QbU-jE3z-cSfquwneB4KaIHC9zK2zReU9yjuh8BhzFWYbpT3LnGz-yEth5ScJEQBcy-ORuhi6fmNBCeu6q5n3q8PpZkriB_ylWpDnwB-oaOWwI14chDA2b-PnlvIlaaMD-u4VFsa37B44N2fZbXYouxCTUbyTeD0CjmR0rieecoTTv_c67hbqP8w587-OL7Gez6qG1Ex6oMAdYbK9vzQpJ-eZfANVibtdZ52Qbv5cp_eVQW-tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب‌شروع‌شد؛ جواد کاظمیان با انتشار این استوری و تگ کردن مونیکا بلوچی تولد او رو تبریک گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/26023" target="_blank">📅 23:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26022">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBvQZHhpIs4uCpV0NG1aaYXoj34h1Oa2uR7odFjXJr6cbBAxMuXCP42hulwvwseEq1ONhaHYm66fOiJTiBylXmhbjbjmyXf9uOvbEQ50LuB43oIAId7cxumvNZpsazVuD28DP8439Q-2CoSXXSVllPb3weW4iz6ED2VfY5qxkkptpKeKqeKZs79xN4BWudPYrTCr2Ku4WVS1UBqd8bHGDXePwXTDkYaTZJslHblb-Ivg71fClno7lz6KynV9oSNACLnxK_1uqArR1oTp3CPqg3_I-QlnIn7nbajh29fb3_74rx2d-dHWft7TEBBzlMqGqal5kJnAOdYez-lUPK7gsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🏆
باشگاه اتلتیکومادریداسپانیا برای دومین بار متوالی بیشترین‌تعدادنماینده را در فینال جام جهانی دارد: فینال‌سال2018: 4 بازیکن؛ فینال سال 2022: 4 بازیکن؛ فینال سال 2026: 9 بازیکن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/26022" target="_blank">📅 23:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26020">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/inyKQZuEUhbu8l5OFxJhv4NMMs-iGCsuQwKveaai6G7ro6woVfnlKoN1xqBO0aC86ZUZBePdXrja-BxcfwiK89fm6MypHK3Aqr3DiFMprJ18qvG0zfkVj-vgmhyzkouk5-H8pCDmE2-3mftuPhoEnCmu9pacCRkBel-iMr_hXCma-psC-HN6tRGywRihe0tF6bZXukrHtR2zpJx0Yrsvn-b0Jq5dYc9KIiMMLhySLMFJObNeM_dQqTj7OnzfdpEpwn-q0TvUq3uBn-654LxIBZYQAr1nKg16gzvSDFz5laLSXL79X4XAI1xBynL45NX06px3N5n255yCp9AepRn7ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vPDoVepCH5D6raLO2t6xl-2iRabgrEizUGNAH57BXL_9J3m9HXzmh8C5uhVNkFb_Ve7rhlEvAv2zEIeeavb-MEiE8SrlrQMq8GA6jYaVNMcZak6_C04aUt4NDd5H5KQ1jBAp6d_3W6kXmQY8M0HKa1ZA55Y7YfwGpsEnMXq4kAyLgWbENqxdad1rrXoPHcLRyjta2XkZozUk_Kv2LqCQUlr_UBgE-VxoHnAcow_HtPIZIUmeJVYnzrE_4lxT7U68Eq7ObrkLxVuBXhIPYwhUtl0AVwVT2mVIqg0TpeZYi5kLcVetx7HC4IvCowR8-_bec13HBu6nwyR3-zcDuRWoKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
مسابقه‌رده‌بندی‌ جام‌جهانی 2026
؛ شماتیک ترکیب دوتیم انگلیس
🆚
فرانسه؛ ساعت 00:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/26020" target="_blank">📅 23:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26019">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOEF_WNIFgF6s1CCzrLPneHV5eI34gKV5h256svvTw51QCf-_xo7ABZ_tbLplMvoNVWq_4lK_wPSKzK8OLB78MYTo68BZqlNojxgJtP3lPC8u88XzEMWDxuAiblQ_5dfWPpDFb2FtSREHO5RS3_npIdWLjX0lGKs9Ps_ieQNOW5lSlCCTl7t1edc905hYoQ_CP3GYy4jC3OlO8Ct2_iOq5BMzYXh_dpwJ7VGqJwrP4wo012kaIyjMJeiBaBi4Vqt7swddGwN4xPEG3so5oN0s629skW_Jhz-z0sJQ0qx3cQFRXwowfxZRAp4liA9yHv8MFqUvQiH04PRNoxU-fJvsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/26019" target="_blank">📅 23:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26018">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHOx6IqdSvwFnqIgRbTzFU9pUYQce6kTrEYU4ICns6IcVMx_42blNdiBhi0rdgyhtnx9Ma2HUMgncvfQ_txfwj27ZUBnp9V37He9HnNZMC8txUZBqNAHWpEFX5schFD_BsRnJkS4XW7UnYdjrHK_EIMtdAE6zT355rr7AH76HiP2oRzY8bvOH50rmz_HWv3ocakOEDPBdhffBaPxGBah_fAUmYZq9vwHk5kJ1gPkRqAqeMucAfaqEyjrcIdjt7-eOpiC5dqR4CB93ouDiSZu6ENqTXG3NUaPpEKjul2EOopYrcg3Tj-sw-nVbgyvihc-DyyvZfYt6RPvnZuT2MTXvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇷
🔴
#تکمیلی؛ رومانو: آلن هلیلوویچ هافبک هجومی 30 ساله کروات در آستانه امضای قرارداد با پرسپولیس قرار دارد و مذاکرات این باشگاه با او در حال نهایی شدنه. هلیلوویچ طی 63 بازی در فورتونا سیتارد آخرین تیم او 6 گل به ثمر رسانده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/26018" target="_blank">📅 23:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26016">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇪🇸
🔴
هایلایتی‌از عمکرد آلن‌هلیلوویچ ستاره سابق بارسلونا که در آستانه عقد قرار داد با پرسپولیسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/26016" target="_blank">📅 22:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26015">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zej6_G8j_9ma7AypN3wRwd3Q839WHdOvjCoEeO-R3Yxs9bNKHjEjju_2QjA3iuII6jdECfKrIEoXsjc1lLcBzJeBWYB4jpXw-D-mZ21RSmuzlPO6gCWwjdUOMyCtLGVRdB__Ok35kwYgyE-XxSF8Q8WGDThtfhcE1hMUxLmv6LQIJy1c9LqSq7T9S4j1ORIY4bGm6zXEzMufwU_WN4obw3EljV227h7tCQTKIrD_zm5omEJL87sm6QJ_fDXDZpBcm_H7dihYnKZA8cpWy-mMURZMTVcKP5h8VvEw6yYssu5R_XIsQANjzvSlHnRULfdqkZQk6U0jOgG8LzagAVWbGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه‌پرسپولیس به‌درخواست شخص مهدی تارتار با یک‌مهاجم‌کرواسی که سابقه بازی در تیم‌های ملی پایه این کشور درکارنامه‌خود داره وارد مذاکره شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/26015" target="_blank">📅 22:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26014">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boZ6uFV8INrqZVFjW2xAYSuUed2dSGEnhH19YjBxGd_6QKQ677vmWzapDl82HKeVyrVB1x4cV1HfzYiqBzIMTeXhUpDw7L4YD5Gq8rupdEYYU22q2HLVnzQT9qXvyV3hFVgJHc8bwHUATWXKUEx2CKg7az6eo1zdqzL2oouwMSHoUtuAG8vpogUhBU7i_7wsxR4Hr1jshcBjVNi-5I0IebsZSg7ZEHkD952Nt-yAo6eYgabxjtmb_F_9iskxspw_RMlV69BICpwojL7lTsqavp4F1EiSoK3CEGhHBX8z-dfnBAa7j82c18b9pSlk35j2SfcoowYbexsRVUKSPnmj3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان تری اسطوره باشگاه چلسی انگلیس:
این سوال رو از من می‌پرسن که چطور می‌شه مسی رو متوقف‌کرد؟جوابش‌اینه:هیچجوره نمی‌شه! حتی اگه بخوای با بازی فیزیکی جلوش رو بگیری، فقط باعث بهتر شدن اون می‌شی. مسی فوق‌العاده قدرتمنده، از جنگیدن لذت می‌بره و واقعاً هر چی که فکرشو کنید داره. به نظر من که اون بهترین بازیکن تاریخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/26014" target="_blank">📅 22:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26013">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d9c8adea2.mp4?token=G15RIk4ganAoOdOcf2xDY-5co2Nfr61vg2EvO03ODhYJIvl8OCxt2-ryAFBs96dm_4jNcHB-4EjCMq8LfqG5tCuNPQjpbMlcp7YjLQnqOOLRZr4qfnNnowbdn0_NLLbU_OBvoH4mfEfuE6Fc_CKTDQC2LHiWXegSHQMT8G7qjm8Qw7Rp1gd4ozHuRCov7d77aLoM-C27j2z96nFlwhchNwGg8SsGoxhnmg1tpFrXiWYcv5rttiuizr7eAcVhtifBnF85hnJ3c3MjWfjPR2GsV1s60yITZ1Upq7YF1_lVZUbQv270vKgLezoKCk-sahmWSi7MZRG1QF8o-AOavQnJ_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d9c8adea2.mp4?token=G15RIk4ganAoOdOcf2xDY-5co2Nfr61vg2EvO03ODhYJIvl8OCxt2-ryAFBs96dm_4jNcHB-4EjCMq8LfqG5tCuNPQjpbMlcp7YjLQnqOOLRZr4qfnNnowbdn0_NLLbU_OBvoH4mfEfuE6Fc_CKTDQC2LHiWXegSHQMT8G7qjm8Qw7Rp1gd4ozHuRCov7d77aLoM-C27j2z96nFlwhchNwGg8SsGoxhnmg1tpFrXiWYcv5rttiuizr7eAcVhtifBnF85hnJ3c3MjWfjPR2GsV1s60yITZ1Upq7YF1_lVZUbQv270vKgLezoKCk-sahmWSi7MZRG1QF8o-AOavQnJ_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره علی کریمی هافبک ملی پوش سابق استقلال از اسپانیایی صحبت کردن میلاد محمدی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26013" target="_blank">📅 22:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26012">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNa-DZyhdu0zjaloaIhJVHNEkXK089UATrl5XA7xTLejZeLdB2lvpN6EH--EMB5_0sk4FVzLS1Qh2pUZfsUzlyEYe9yQrYiwpMWvcxXjyFLM4GxwtMOmkBY3YpE5D0limTeUYWQyQ7g3icPYJ-24CmRq4BhDyx3DIa11fy_C1S1n_1fvHtEOkZ638SnNvVScPjeDDvg88xL6H-zcP1WoRKdX8oOTsxcGz4TuYDFgwNf2M7alF59XRMz0Z2xTDcreMwS1qGviw1r_efgPaQVp7bkXjavT5gUp-6aZNSDhgbPV_xvLc-Bxj-usoEfO7WIT-P49yOA_TSYAQOLCesww3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعداز اورنشتاین؛ رومانو هم تایید کرد؛ مورگان راجرز ستاره آستون ویلا رسما به چلسی پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/26012" target="_blank">📅 22:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26011">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUsD5BhORhVAWqemHOgNJOxVnSpnQ8fsQ9Yca_leShzJx5elYMoY6_0W-s7WJdRnuXdDLPpK4NcGEwgd8oDYzZnlQt-4ohgLMj9-kcwbnYeGMKeRHxr3MlDbO3Tl8BNDoMRfGjnm5YWNDdmCvEb1FruhQjaf4BSWZLcFLcxL5i8RWn80TJG6x7YTRnp5En25DEesoRiH4kg1DnKHvdqqyy86rvyy09KfjXpebyDAaY8yUXs4Q0bNCWTKAgY03_cKJK4-K5NmQ-Kjy6dmWi7Wd6FoFbpMinaVAiSqoRAGHxZSJycNsTC14R4XL5ehGG4yH62Ur47I6EDh9zz-0aoC7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🟢
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌باارسال‌نامه‌ای به‌باشگاه اخمت گروژنی خواستارجذب عثمان اندونگ مدافع‌میانی26ساله این تیم شد. اندونگ دو فصل پیش عملکرد خیره کننده‌ای درگلگهر داشت و با 500k€ به روسی‌ها فروخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/26011" target="_blank">📅 21:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26010">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrbU4ft2RZkqOcAxqy64WMqvXMp77LOZ6hZRiOvhJLOwZYpdS5olLAZjXP2IAhYKoT6dDx5MNNyNQTKtSlJOReOvzzSGMuiVuctXawNqM82RfrZbfNt-WU5m-26laUgo1IOcNjPbi7gKseMTSCB3VlxrSg-UBmiD2QEzOZfGEPRLTCeoI2Z5uYE1Fblsl943QRf3PPHrgM3u-rwU8VeXYI0ElC1kkrqjjXth0-ccA6TN7OvV63DTC4Sk37NxhazSrXaNMuLy-m0YfdI7OuV6oZJz5W7cbFEv5ukwFg2qx1MbNPQuye1axSdzgNHly5ZHulk3hrEKELtzXTmtwpZxuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیوید اورنشتاین: آرسنال هایجک خورد؛ تیم چلسی با ارائه پیشنهادی 137 میلیون یورویی به آستون ویلا درآستانه عقدقرارداد پنج ساله با مورگان راجرز ستاره ملی پوش این باشگاه قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26010" target="_blank">📅 21:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26009">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qy4Ae5fCdtjH0GR8iW-pi_VD8T_DJ2jCW0xRvcXEWxHvu5th5YJCaemBRccr_rdLLwJ4S-Z05YyPMrsaQAhaftnBIikzx4wLezJ_LwrFpyeKWB-AuIoR50ADyegC6unuomJiGxh08vU9Bpqtk_eNxoYey12sAi__PVRU3HwWM-VkUJxt8aJUKVr1WMeCiZhOdEnJ5pYUh6IFR2PFFbMW9mUAWUCJqZOpsTfkgfuKwF2amNN83BjkiJjyBTBhYKigZQCzClwDqne8ZnHIfOoGFpIFx38arFFkLxURFNzUwZjVM8XuTFWJ5vblTdMsX2u8BKltDmOt0QnwRuvLPJtxNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام رومانو؛ کریستوس زولیس وینگر 24 ساله کلوب بروژ با عقدقراردادی چهار ساله به آرسنال پیوست. زولیس یونانی فصل‌گذشته‌در36 مسابقه 17 گل و 23 پاس گل به ثبت رساند. همچنین توپچی‌ ها بدنبال عقد قرارداد فوری با مورگان راجرز ستاره تیم ملی انگلیسه…</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26009" target="_blank">📅 21:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26008">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3acdc0e3a.mp4?token=nuFIf8QsmjePisUFiPJ0f5o8nyF2SRxhVc8jqSi33vTDJsNZ3-vGF5KNjmF8BoWXGEuzpHL38ud8OiLEf5zsMGp9r3Ve3GLEVXa5TrKtoFKMD4xXixX2qmmSftiIkfnFCQlyQH4vaiJDMihPcvhnCyFbF2xXHT9EXrcTGbqbByyprNXm3YKa6nEq5enBQorx6k0OiGxwSGiji3B6ge3kiZ2rg1S7dCSz_-F670SIzWs-j45Cg8ZVFdlcpYtMyZ7GLgWm6DOmW_ApuTUfJNNvvD96YRv2nlWEjEQRnr2wGc1rhvu1dGBeYEtG6_rhhCYyQFYAgydUxkNgNQGNPlHx_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3acdc0e3a.mp4?token=nuFIf8QsmjePisUFiPJ0f5o8nyF2SRxhVc8jqSi33vTDJsNZ3-vGF5KNjmF8BoWXGEuzpHL38ud8OiLEf5zsMGp9r3Ve3GLEVXa5TrKtoFKMD4xXixX2qmmSftiIkfnFCQlyQH4vaiJDMihPcvhnCyFbF2xXHT9EXrcTGbqbByyprNXm3YKa6nEq5enBQorx6k0OiGxwSGiji3B6ge3kiZ2rg1S7dCSz_-F670SIzWs-j45Cg8ZVFdlcpYtMyZ7GLgWm6DOmW_ApuTUfJNNvvD96YRv2nlWEjEQRnr2wGc1rhvu1dGBeYEtG6_rhhCYyQFYAgydUxkNgNQGNPlHx_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
تو زندگی همه باید مثل علیرضا فغانی باشیم که حتی اگه داور فینال جام جهانی هم نشدیم از تلاش کردن تو زندگی ناامید نشیم. امید کلید پیروزیه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26008" target="_blank">📅 20:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26007">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cV0bykgMIPge3TPs7ONxHCNsEW59pgU_WnGTk7UpVkf8LGoCPA6au6rQmB5prYXsjzXgREeAgLa3_mlTA18GXPkNwIlriN6JH5A572Id4MRzOSVSxqcIRgmj5BVY5HKvsiGRZ06g1bKEind6h6gyT4scIQjOX5Ux3nB8QPG0SQjr32ALXbEFbrmLfF1NkkwTo0J2-ftr8JeIA1W09zzyj6CoHdihdNDVDUBIxk9BJrWumIJrI-kdwHV6IM1SIyLtCJoyMfT4XYAKvd9CamaOAD7DQ04F4gd4cEq6qkp_m2z-iMxiYtBxUUJm7NAWvckL5FiB7MTzO1mZ-tFt4pu5Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه نساجی بعد از جلسه امروز با باشگاه پرسپولیس رقم رضایت‌نامه دانیال ایری مدافع تیم خود را از 190 به 150 میلیاردتومان‌کاهش داده و72ساعت به‌ مدیران پرسپولیس فرصت‌داده تااین‌رقم روپرداخت کنند در غیر این صورت توافقات طرفین بهم…</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26007" target="_blank">📅 20:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26006">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcMnVf1hDV7EOw8hBpUleVHFmZbYGh77HpPxXTOIjLGSuBNxf_EqQINrmiRsWV9HGwzytAkg3hnV1xCIoEJAnqFHRw6sDQ_AnE_QgZtbB30XzifOXCqh-qvpIavSweUrGhvP-c0_mlmL_pyR399BQlOUzoU0oO602fZoTfM9dIGuWr3OUpRGIXkNd711X5DpSW_BtR-6t47_vIjfi97AYL7IIi2FbJ9dHhT1l_rAYzgyu_wLLJx_4sp37mp3DryTQ1V5ih1UPuBwfzucejMJnsdYjCb5LGTFjiuFSNQz5eu0nOIbw_risM5dMFx1YAXXeCQgetr7QTfJxvZq7XnnnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
راجب خبر حسین نژاد هم‌پرسیدیم گفتن تا شب بهتون خبر میدیم که توافق استقلال با روسا صحت داره یا که خیر. وضعیت جلسه باشگاه پرسپولیس با نساجی برای جذب ایری و طاهری هم مشخص بشه قطعا تو کانال میزنیم. خبر رو بی سر و ته نمیزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26006" target="_blank">📅 20:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26005">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntVQhJnay-t_biNhDj-9PaycKdk6F8D7zLA9_xr529YRYZ6yf5M6hb3v8BRTyEGwYnMt2onqI3V1vGAUBM-egE-uRctI5iOm3r2TzrTWcLZL8fLvnlbWeDbnL05immLhCjHSjhyVfqcetQdBOhRZp8FUNfNNd_S7XQzyVVWn-5h30SzsfVjbHHcWzAXwbGpKkESl0A1aV2EDTQD6T54HQ9htSEn7__cxaLL498i-BpVxD_YozJCgl3FW4bpPhebUjM6lX88oLPNXwcJFmENf-kqFfRH8XHat5wPD-oquruKR9JqpYKBbBxR87mi1ZhDmtT2nlfLCRMH9SrTSJn1gcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
وزارت‌ارتباطات‌شایعه‌قطع‌اینترنت پس از جام جهانی را تکذیب کرد.
علیرضا عبداللهی‌نژاد»، رئیس مرکز روابط‌عمومی و اطلاع‌رسانی وزارت ارتباطات و فناوری اطلاعات، شایعات مطرح شده در شبکه‌های اجتماعی مبنی بر قطع اینترنت پس از مسابقات جام جهانی را کاملاًبی‌اساس‌دانست. واقعا اونایی همچین شایعاتی پخش میکنن مریضن. سه ماه مردم ما نت نداشتن بسه دیگه کم دهن مردم رو سرویس کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26005" target="_blank">📅 19:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26003">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNbS6FrDAXcvTuzmu8Tydtn4j5FiEyU7nLZUx-KYYNwcbxSJa0UboVHiBk8HnlINK-wBkJY5I8RdRMHrK2H2Vx14EAwCJyirJqU__9yzE4EEzWd7QK9QCLbyLFEbxCAFS7myOTbY6B0DonK2vq4mFF5TiV4HLh5Bg80lbmdsd7bgCTzQPYESo03QzbMshCt_FHHO_QMxLMuheVqfzeeSDY8HDl2jSama5-WTJGPOMG1VClPXlQxWmmEromiyrGOy2OZPPlrmOR0_9FAbyMzIVlzyJTTFpxZFNGGzido_yO973z5ck_hd-7EiICGXB7WvcGY08MQu-neTkqREr-gbhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
آدیداس‌ازاستوک‌های مسی برای فینال جام جهانی رونمایی کرد که روش‌عبارت "آخرین رقص" حک شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26003" target="_blank">📅 19:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26002">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e60998a9e.mp4?token=EAMbJqf3oQ8sMyud_PqagSI86atBqirxrWb-vuKuQ_yIxNyg-0X4x6mYsc6q-Rsf2Epy3HaYzEhJJA-wXZwDTO2BDG4tAEpHBqSkEuxf9NAoJhnEjq3TA7UF00wf6OWKylyZsKjaSKkkZ046L7a-tBnqmi2JehZPm4OGNtelnPyYHl5iwjOPAP_qwcS0Yw0VPOLBDzwu0lz0hHT6HayVO-_VsPfmYBV3AkXtJYTvS5MGAXJBgDNXDDiVlwUm2tw9pq7onUERMX5GHlEVhu4Xi5s18_T4t0n6RXKduLa6_eS8k3NhAE77mzhxF_E0wX4Dnd0RG07qQiDjPW5E3P1bqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e60998a9e.mp4?token=EAMbJqf3oQ8sMyud_PqagSI86atBqirxrWb-vuKuQ_yIxNyg-0X4x6mYsc6q-Rsf2Epy3HaYzEhJJA-wXZwDTO2BDG4tAEpHBqSkEuxf9NAoJhnEjq3TA7UF00wf6OWKylyZsKjaSKkkZ046L7a-tBnqmi2JehZPm4OGNtelnPyYHl5iwjOPAP_qwcS0Yw0VPOLBDzwu0lz0hHT6HayVO-_VsPfmYBV3AkXtJYTvS5MGAXJBgDNXDDiVlwUm2tw9pq7onUERMX5GHlEVhu4Xi5s18_T4t0n6RXKduLa6_eS8k3NhAE77mzhxF_E0wX4Dnd0RG07qQiDjPW5E3P1bqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ درباره مسی: من‌از ورزش‌سر درمیارم، یه چیزایی هم از فوتبال می‌دونم. داشتم بازی مسی رو نگاه می‌کردم، دیدم مدافع‌ها حسابی چسبیده بودن بهش. ولی یهو دیدم غیبش زد و سر از سمت راست زمین درآورد. میفهمید‌ من چی میگم؟ همین خودش توجهم رو جلب کرد. هیچ‌کس هم درباره‌اش حرف نزد، ولی من خودم متوجهش شدم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26002" target="_blank">📅 18:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26001">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuAfZjPtzJExFzxg-B2ntzgvj7NJcA82yPuQvYgroIb2VtPOPWirRdyIxlrvcl0z0Ye2rCc0E7t_pGlR3W10L0nbJZ4EbfIoFHZXbeve1e5ft8ragpB-e9hBn0uY7t7rFadV-0_0uJp9p0SX8Xl3rJ03bxpfJmZ-1THWfCs6fkExgxSMSTkynLD9_sRQBCPfWK1XxOZ7FiolPyrB9pUtAVMhAmk6UpS7tBH2W7n7MWzRrkzMwLqm1IpQhHIXvI7j8191WZ2ftM6z1JvZeZxDw3N_3Ufs-co0QKWmGDWmtuHB276qBy4kkzGxkNenXMSeQvvBYTP5JfX07sRMZcn0wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خوان‌کاپدویلا دفاع‌سابق‌اسپانیا باسابقه قهرمانی جهان دست‌زن و بچه رو گرفته و بره آمریکا فینال رو تماشا کنه بهش ویزا ندادند. حالا چرا؟ چون 10 سال پیش برای بازی خیریه به ایران سفر کرده بود .
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26001" target="_blank">📅 18:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26000">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqrzsWDt9uj5HDBnY0vh3EscernLFnmaN4rFkoC2E95QffbV91hqnJ6bZ_CtpiAzlmggcX7UWS4-mP-Kh9BrkXCW9tWU_e5iB2RcWZ7rPBLLx1PwXpP18PwaILzSeYIUNvbzj35URkbxm1rmktqfBVVFTS6Ehuo1jU2zybCwhRIQyvhPnOFgaJuTdgObEaqpbB9mFsFR6-DaUfczBX4gCigJ09pPCE-gPuibftwIro5UiLQScJZ1rDH1ihxOJORkpabCe5KVY4Z7oMrXRLZaMC2OzkxsIftjHKXiT4ui89M3V-YZGkkprJBfZgZM2nQXeymLvG6y1BH5F2A7GmDlig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🏆
باشگاه اتلتیکومادریداسپانیا برای دومین بار متوالی بیشترین‌تعدادنماینده را در فینال جام جهانی دارد: فینال‌سال2018: 4 بازیکن؛ فینال سال 2022: 4 بازیکن؛ فینال سال 2026: 9 بازیکن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26000" target="_blank">📅 18:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25998">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K76ITIPye2q7Zd2O3zdTKd8-lXKjBaEEy7jKT3kxn162JPHvy13snh-os-4eoDv3vUXyJ71soY2FkqWhJZjmuGFqW5lY1agvxMp4DblpCWYzFPruoefe5Q11ap0puxZ46UUDe93XGR8jgmArDmnJnwh9BtlPOgYKjadMT6C3sPmpN0CDHYTp_pYaHXO4O9yWtskhIs158coVy6WOMgXmhzAMANSnGigPQ8BrGxh1eVT-KaT_yS8gVvpXnqAMiRjyloTzpiByyds3CZvqQLYs_L3pkcYYZyLvOK3RKRm-t6KvYnSLa4Li6IcqjPmzcy4UifW0QbbarAwzOt0qxsOpGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این خانوم اومده با استفاده از تکنولوژی آفساید درجام‌جهانی2026 باسنشو مورد بررسی قرار داده؛ افساید مهدی طارمی هم تقریبا همچین چیزی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25998" target="_blank">📅 18:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25997">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQQwEkJlv71g1BV-WSIfFaGABErZ17w0RJnSYkqM3HzLf8FNmlNLipSRHRRPrlUr3p6gl75Gdpkm6R8ShYpBaHM9_1QJ1a3DhdGZQpuQbLBKgFtZEYJ3_JaECUgOGH1I96sYTdtRxYUM-GXmYKHePfjx2_yh8BFciYWRGIgZSNjZ5VsrbQOfY4qgLI_YL82FE7ye1PfxK71_22kg6x4k3EYn5L8h04b1zIGDwUyARkG3qc9RQfzAgAJ6pYdesoPElh-MQlqcD-WkhCO3Uip7xHdiKHKl1xGUzy1dTIm5K8yDFRxEG_uVI3Lj_NgbSSyB7v60rLnHuZ4IK-bCHy9uAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇵🇹
🤩
عملکرد استثنایی و محشر لیونل مسی و کریس رونالدو در کل دوران حرفه ایشون در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25997" target="_blank">📅 18:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25996">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyDZUAa_VtdKW_bNSgMy6PxNeoPM4ESVmIWGTAAGGaxzQpq3m3a2IICX2Qwcifa1Y_BpT6zvZ72D3yQV5p3VuOwIKLD0JI_vlcwjN5acyem4mHmVtdIE2r6wPLdvACxvcnU8C_zcn3qh9Dr7oaM2sZtKNUBQxhooGJXStDWW82tvin42d9-Xcci6eesyTwqrq2N0_k5G-5yoCB11hOVxwDldmeNfLVWjEQ96kXeM99FkWm4nfSYUuyTXDhCaBLynJ7gfSQ8nm1xgez-2nM37gIPgZOlof_8WB6lTU9NegOkoPLgPuFexJvv7ou2z5xH7mQ3zra23Sixm_mLJFtCnwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇵🇹
🤩
عملکرد استثنایی و محشر لیونل مسی و کریس رونالدو در کل دوران حرفه ایشون در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25996" target="_blank">📅 17:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25995">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf0ae4ecd3.mp4?token=NDK0ZX5okAPWrOWgmczl_vd68cikb5i2f0PB4QYL_ZcOSEm0q-pcSjZbS7TsM73PRR-S0S2X-_QHI13XMqJz-_o3TKD9AVEH7KmilS6CDagf0jpPkCp3pEQqbz4eVV-HJd8x6Y7sBA2XkhXZqr_kb0eF3cqnOUD0h7h0tpBQw6fbTHZaV3WVMaELr4jmUlnSR3bC5HGtlwTy_phyFfraQ8AMaJi94_G9iHDV2mUneheg-xn-liApsBYUmmyaqgeRBHDOGNiMFH--KSJojrEmKEspgjQ3EfW2xV-hgu22BvJbSqL0EDQ62f6m1zwfNCWlsQ46AWLYkoRgD7OW0GEHt3xXJ_Vl725FJVZ1IiKicgwsxF9yA7p0LvZQNPPQSzogXFMmY208G2vf9PreMO7msF8gfoI6vN379cSCx8lY94UhT4rHPKfwXfFquRg6PB2EkNejPM8-_iq-WhtDwD_gtFNWq_xxnM1gKXLHZnQAp93pRWaP9fdaeyzaX_elX1qleEi-BOmhIouUurrRWAWIXtOw93ry7laMmHp-9SAQ9w0ZjZK3CeJVQxAuqK3GV3qJQBN4uI8SR7ZTv4w9rRRPGnMH0rpujiENVYlgqzW9pU7cQ2ckSeDLNL3A2nLmgBNTRb8vtCKFGZU8eX5cCs2UsnvHHn8nwFuwifKWLJOzw5c" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf0ae4ecd3.mp4?token=NDK0ZX5okAPWrOWgmczl_vd68cikb5i2f0PB4QYL_ZcOSEm0q-pcSjZbS7TsM73PRR-S0S2X-_QHI13XMqJz-_o3TKD9AVEH7KmilS6CDagf0jpPkCp3pEQqbz4eVV-HJd8x6Y7sBA2XkhXZqr_kb0eF3cqnOUD0h7h0tpBQw6fbTHZaV3WVMaELr4jmUlnSR3bC5HGtlwTy_phyFfraQ8AMaJi94_G9iHDV2mUneheg-xn-liApsBYUmmyaqgeRBHDOGNiMFH--KSJojrEmKEspgjQ3EfW2xV-hgu22BvJbSqL0EDQ62f6m1zwfNCWlsQ46AWLYkoRgD7OW0GEHt3xXJ_Vl725FJVZ1IiKicgwsxF9yA7p0LvZQNPPQSzogXFMmY208G2vf9PreMO7msF8gfoI6vN379cSCx8lY94UhT4rHPKfwXfFquRg6PB2EkNejPM8-_iq-WhtDwD_gtFNWq_xxnM1gKXLHZnQAp93pRWaP9fdaeyzaX_elX1qleEi-BOmhIouUurrRWAWIXtOw93ry7laMmHp-9SAQ9w0ZjZK3CeJVQxAuqK3GV3qJQBN4uI8SR7ZTv4w9rRRPGnMH0rpujiENVYlgqzW9pU7cQ2ckSeDLNL3A2nLmgBNTRb8vtCKFGZU8eX5cCs2UsnvHHn8nwFuwifKWLJOzw5c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
ویدیو ساخته‌شده با هوش‌مصنوعیه که خود کریس هم لایکش کرده، انقدر قشنگ ساخته شده که قطعاًاحساسی‌ترین‌ویدیوییه‌که میتونید امروز ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25995" target="_blank">📅 17:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25994">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d46f404ea6.mp4?token=uGRACek6CZzol1z6-MBSxSr8vgFv2fEgGLsVKvdzEiO2WSZPnHjB4XXTpkNOqwjJkup3zEg-ZWI68a1VUq9Ni5_34py1a2bHsLhT7crB8BEevc_Xi5nKtrhEWB5aKRSGsK1XkD4vjIngII28qKxQXtnaK18LS4XlErJcgzAxcGxpJNQck0pgGjkMIu9CaigAGDVYiTFbfi2p75WHNpePT8jLsUmuG9rmQ3Mb_CPGm0baVHGVsCZMHGMWR_-6X8MuhrTKHzNZbcgZn-dc7o9oDRO-IVpDlDA1aNXgtsFEDn8Qjqw7D1xic7ver1hmQ4qDz_FBwwtoZ6noWhE0bPvL6mLqebpD1ztGv7_fXRrOSGQJrfirUguBfPk3t0xmy2BuONzfkye2WEzs5tT1AMIrkaiLS7k1pWbLahRjT_T4hZVPePXVt4xiVzjIBgKP-w1YAKhFWY226eUSMWoN608-Vwiw6tn52HUrJgYjgCyXtb2tWMTMecPMh2AJbhN8M0HAl3jHO2zt5nP0o4XLDlnKTdW4h-_TdQShIhH_UwGW4Sv5SOV-nJFBf_PO23phwan-JERBb1sn17iM_G1HE27Xi7sxT40p04CvWPH4pb48Ua9AZOYPpDIJ5DmY_EW35pIUROTCuDTJKTNbxzTxo6U4XBR97JThl4r3gyuROltR15U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d46f404ea6.mp4?token=uGRACek6CZzol1z6-MBSxSr8vgFv2fEgGLsVKvdzEiO2WSZPnHjB4XXTpkNOqwjJkup3zEg-ZWI68a1VUq9Ni5_34py1a2bHsLhT7crB8BEevc_Xi5nKtrhEWB5aKRSGsK1XkD4vjIngII28qKxQXtnaK18LS4XlErJcgzAxcGxpJNQck0pgGjkMIu9CaigAGDVYiTFbfi2p75WHNpePT8jLsUmuG9rmQ3Mb_CPGm0baVHGVsCZMHGMWR_-6X8MuhrTKHzNZbcgZn-dc7o9oDRO-IVpDlDA1aNXgtsFEDn8Qjqw7D1xic7ver1hmQ4qDz_FBwwtoZ6noWhE0bPvL6mLqebpD1ztGv7_fXRrOSGQJrfirUguBfPk3t0xmy2BuONzfkye2WEzs5tT1AMIrkaiLS7k1pWbLahRjT_T4hZVPePXVt4xiVzjIBgKP-w1YAKhFWY226eUSMWoN608-Vwiw6tn52HUrJgYjgCyXtb2tWMTMecPMh2AJbhN8M0HAl3jHO2zt5nP0o4XLDlnKTdW4h-_TdQShIhH_UwGW4Sv5SOV-nJFBf_PO23phwan-JERBb1sn17iM_G1HE27Xi7sxT40p04CvWPH4pb48Ua9AZOYPpDIJ5DmY_EW35pIUROTCuDTJKTNbxzTxo6U4XBR97JThl4r3gyuROltR15U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جالبه‌بدونید فدراسیون‌فوتبال‌اسپانیا به سر آشپز ایرانیه یک میلیون‌دلار داده که در آستانه دیدار فینال جام‌جهانی‌بهترین غذاها رو برای بازیکنان درست کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25994" target="_blank">📅 17:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25993">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfHEcZQIiHq-oYa48qM3xYnESBnUbmYyWpqq_xsbxjdIlHqLcBVkiUSrGlH4qC-ZYDhVCC5bi6-oDo4TPYMu6oqse_s5krLEKW_wuZk0rj5vPGTfmwfTyLeXPy_F1JDrf4KOdI1S6bR2uXjen__bxsAjkDk4BO0xKCUfzEVZv1vYB5xQu39hKJn1hBC-9nn68jOtoXyrcQMdtuGZseeMPwr449jqwhTZcyU6YUhTkjJiilMQy2K1ogzGSxczPaceCvS4JVRNAGCz683pYKjAmBY-RRhTLgl3jsQbtNrHKhfS0aheo3ABCQkSnil0h3gPZ0Q-WkldlpGKHsbabNc02w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز محمدامین کاظمیان؛ یاسین سلمانی وینگرجوان پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و از پرسپولیس جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/25993" target="_blank">📅 16:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25992">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fpxbr9jJmtSjs2SJEE5zULTliOoEc9PvRUDRvZmAFUr9Un_JUkB6NMRyysxbVYUW6VYT6hFXujwfKsXhUAdY97womn3kFOd3S0HB6HghFrsKdVf1TRcy1jHtko6ZoZHa5dvEA7zhzCU5BFslYOJwoateakkZF8wZHCkC9a4uchplIRyZR1N-myDUr2pmyr1hdM3J1SpGwRnXI1AbRB8ynoQWbSDx9_pb-Ui0h1sVSqdfx1UYR0yBegSU1KjrndqLQlX9A9iXK7o0Nm4aDJRtVrPKO2Ytp-6-1AGuP5mbSjc3mNl7OiETXB9ASpOAqmOv5DmNXOP5ScUAsanaQwYVxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی #اختصاصی_پرشیانا #فوری؛ محمدرضا اخباری گلرسابق‌سپاهان‌بعد از تماس مهدی تارتار دقایقی‌قبل موافقت خود را برای عقد قراردادی دو ساله با باشگاه پرسپولیس اعلام کرده و اگر اتفاق خاصی رخ ندهد اخباری بزودی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25992" target="_blank">📅 16:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25991">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWjLMQ_B1ubGfPIwrha36UKWIPdIut6OSwVMb9abrtfY3DjPcVZIrbO0bE4gf_t2FDkfRecLd6Nhh1vbPdNiWjIVasr66Od9EdjW9K-FXBmN-E1IWMVJqyEKeP8aWYAvaocGpl_sRG5xjNXWRdvneUa-jxumwH2k4GzbYZgyLC2Xbdo1Vzcw6UKB9YibCc-fF3oGhO45umxskuBufGSF9xCcwsiauJk6OBTaF2ZnOa3gQxk3HWjLfuuU8mwjv4-purr70K-ifhLho-B3d0CTxRwd3OSrLk-KwYXweChLLVgrrtWDUhReyVujJAhQBYHbma5YmY2Yna8ODR8vRVKQ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ از طریق نزدیکان خودِ محمد جواد حسین نژاد درحال‌پیگیری‌هستیم‌که ببینیم طبق گفته علی‌تاجرنیا باشگاه‌استقلال‌باباشگاه ماخاچ قلعه برای گرفتن‌رضایت‌نامه به توافق کامل رسیده یا که خیر!
🔵
تااینجاش روخبرداریم‌که استقلال با حسین نژاد به توافق شخصی رسیده…</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/25991" target="_blank">📅 16:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25990">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMC7lz8zOjEcu1YjVKXHR2lv4foUP8Zt0CtaT4clyPetU3TNbz7fRkJ5eDmfIfG7gUzcKePRmQ2DsT7NcQuNNTPWmuNd7R03UlKCRQUiOsFM6dLYbezcqQXXVlgKN_b52ydeMF_cZ2SMhbtKmVmvINmBbZlwwPGXR0zE4ssFM-hZOp_XGO1EQ81B_6V3CMPuq3oacC5dkPGZgrpXCGbgTdVQRszIbfrgLlJ87-dJGnb8iALsuW-v25H_5TaqlhJjkBJxHvUmfZ2qCBg8uKCtHZHQBH7Noo-JrHj3KrsB_Ht5rUBUg6L6I5PG5Ubl2aPCcbbiPAIQPQn-K_YTrIcUfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
رفقای گل دیروزهم گفتیم باشگاه پرسپولیس هیچ مذاکره‌ای با علیرضا کوشکی ستاره تیم استقلال انجام نداده و هیچ‌برنامه‌ای هم برای.جذب این بازیکن 26 ساله نداره. بعنوان اولین‌رسانه گفتیم مهدی ترابی 32 ساله بمب اصلی مدیران باشگاه پرسپولیس است و امشب هم جلسه بسیار…</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/25990" target="_blank">📅 15:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25989">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bi4gzXHJN_1j3cw4gMCwolOiZaP8N4-9eqQp7wb3eIuWsQAcL_zTK8QlDoyNh2OG9qXqCj3tjv-6j46eWiTWZGWwSKiibJE3d1074ZqIKsiCXfJRyWv0LFhnxJIsPRayLRXvcL0Sp4QKK1q4Ep9bZfOxk29VvH-RXL2NoduTMA5F97_ipwbN1_nKbKioD-ahA7PAGouwLRwkyKtfqgqUXaFc0rc6jSuvkGeNlznrI8M7FchweHLSFe0E9YBWvw2RkmPkO8OVViJ7YphJDsl79oz0KA2T76Rw7wsbhRuidqFpTgdS_bwT7BvrNurd1E-una63FS85I5aj-6f3jyFptA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/25989" target="_blank">📅 15:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25988">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPPlSrofad9kEmVu1ucNgvjcclnAmyvlehcCDl66S76O1kHWXwg4U_DT6w3fac_1MGf3RSwere2cbzSX3JPTWP5iQJUA1kaWho3bZ-9UoQDCKcCTWKfymBA9k3q5ie1dBaat5OHvQsiQbBR6XU3HQfstykE0-jQhQtUipUJQ1KVgBOIqFJLQbD-CEWExeftai4Et-V36ZPEmwAorOG6qKHXeFrmYDnGfYCRN8s5PrUSnIbGknnO7PDjGuIlVZOwiiZXs9SoayRv6uTj2tbg77uQ3mug7Jao-FuwZqbbd1_K2AjCITFPvGnjEQ7Bqciy9V1nkcCTOmaXsaFS5PFfPxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ یاسر آسانی برای فصل آینده حضور در استقلال 1.5 میلیون دلار خواسته و ازطریق‌مدیربرنامه‌خود به باشگاه استقلال گفته درصورتیکه بادرخواستش موافقت کنند حاضره قراردادش رو باآبی‌ها به‌مدت‌سه فصل تمدید کند اما در غیر این صورت ظرف 24…</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/25988" target="_blank">📅 15:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25987">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/letSSacSNE1zBj5x7PYPzZgL9qAVbMr9fyqNKmZRiNTz_1K4tLThRojlrULGNDr7PukkhsStCsIrI69N51g2FcmMiNcYfot0937WID_NIfi4AqzAStXQNQ6SVH_ZWFJ-As3nxPvtPgTEmnopdtCYMEegmXBaOWBLXrNm4YSE0QmrcHxmyvpOcr6cf53R6AVRv8YS4h-ooPBZpuCjW3xM7nlwaK6PuBzRyQ6LGwF9J0O80nQ_ep15LJlpScEX8XjyZ6rYPtWOGCrBDPOINl7YU-BuyWa3bxjoWdavVD9sw-FEtbGwOaZqH-PqZ3cCK8veEk_LYJ7zilc82wTQR5vqjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق جدید ترین شنیده‌های رسانه پرشیانا؛ باشگاه استقلال ظرف همین‌هفته‌از تمدیدی‌های خود یعنی روزبه چشمی، علیرضا کوشکی و محمد حسین اسلامی رونمایی‌خواهدکرد. همانطور پیش‌ترنیز خبر دادیم تمام توافقات با این 3 نفر انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/25987" target="_blank">📅 15:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25986">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYxb19mj_Ive4DUdSsZfjcOaqOoIhSO98PrqLsM471ECXC8uXehtSzBMamuQtTRRAc3F86isAV3skG6ZvAmEytcsqdqAt8Ru8GwVFZpk5XcQ6kpaBz6d8yfiMOmXesrNDa9iQ0dy23ByGOHOS-0BMfDwI3aEIRKOT-SYQtyF_uinaPppNFalge2tMizF1aWBatYjSlGZhDO47G1d5u2lVscpbBQ6utl_BKDSAZ-3rqUjnFWxcqmMnNaUdCweDTs32T9-qLXaDuIOhYWhg7fG3oFiPK6ivcCcPYAcaBWCtUoDqt-d3QIflfuLJagDa0YDWAuFsB0Sc7w-HsUMl-fTUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی؛ امروز حوالی ساعت پنج عصر جلسه مهم‌سرنوشت‌سازی‌بین‌مدیران دوتیم نساجی و پرسپولیس‌برای‌انتقال دانیال ایری و کسری طاهری به این تیم دارند. طبق شنیده‌های پرشیانا احتمال اینکه این دو انتقال انجام شود بسیار زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/persiana_Soccer/25986" target="_blank">📅 14:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25985">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuurfHa7UQwOKLBKtCEJg48uKVLm2Dx-2EIKxI1dpnuK9MzxKBWkkVLrzxs0ADg-JYemP5UvdfeETZphUgjR0kxzjKjTjAlK5kwx8dwZKJiDk9H61UgYUOjdHFKVEmoJ6XACeEBy9W1orUk7gQlus5srAR5C-UqVKy_ZQ_T18yxloHfxkso6l_DqPC7G8sOIxTw5nhxiZTs3iwrlyxrNJyhnxp2XUEXmDlu-jeiaoQoc57gv8AY161NqpRPKIljBPo8HpqM4e8u4WQ8hiBTlapDEGdRe8ohbxSpKWV5bhbd2p8tLtNouXc6HkexmlyKhO3wyl6ZbVl_i7keVqsKXBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور برای عقد قرارداد سه ساله به ارزش 150 میلیارد تومان با محمد مهدی محبی به توافق کامل‌رسیده و بادریافت رضایت‌نامه‌از خرید جدید خود برای فصل‌اینده رقابت‌ها رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/persiana_Soccer/25985" target="_blank">📅 14:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25984">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFab79s20IHbcdme0YcNP1wzFTGcQ3-4SNVFoxCovKDm8jDv04a1Z7Y9UsWUIBJ0Fw8Rih5JTyn53lS4Wja2vipheLNIPtkpE6nx2I4xz00xv-Dl53ieqoKWT5wXpjQwKr-4BVCz-vbLOsKd010gjpsC1OD_CP3LBGYKFlw2k9ifOtP806sAaZn3XsRbcvsoepMdolLD1VTxCRMbHgTr2pHhWsFD31Ie6Uffc3SiXFnsakl7QvhJjfTN7Ur0_EAgfalBYCnyOA0IY0QMPd-gqBb4qjEDS9u977g3KWmuJvK5Tc-83j2wDU4dwR7wIF_BjsYJXdnDMVZYMuorGQq9JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◽️
🔴
👤
طبق اخبار دریافتی پرسپولیس؛ کسری طاهری از مدیران‌تیم‌نساجی‌خواسته‌ که کمک کنند در همین پنجره‌باقراردادی‌قرضی همراه بابند خرید دائمی به پرسپولیس بپیوندد. زندی مدیرعامل نساجی قول داده که همکاری کند این انتقال بزودی انجام شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/persiana_Soccer/25984" target="_blank">📅 14:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25983">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAh7unE6AtwOzXxr_uNUYke_cAeKmjsCPZiP3Tm_WhCVqPN7nP1wppFD_aqQW606xitvJ_NdvLso8d9SBy_XMXEw0X9Rcr2BSqHmc1qGp938hr4G99rRWfZk0WXrMdMcR-pUtHeEc6n_FIpqxqDyAl1u4_ZQJqqwDENMhHNr2kWDt6b1oXMHUacOq0Lx9TaAUrSiasENrV_-Nfw2p3AR2bwtjUhQUrtmalDsJc1hhwWhJ0TRU_vTexSiGMz-u051d8GQ9E84SSxBzyet9mUCjd7MaSnIX9CecoYHwlZ1kKAXPtFWQWxUFdA2C3KmjyeG0iVaL0p8m2cwJxkm_3odDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ شهریار مغانلو به پیشنهاد مالی‌باشگاه‌تراکتور پاسخ مثبت داده و اگه اتفاق خاصی رخ ندهد شهریار مغانلو به زودی بعد از بازگشت به ایران قراردادش رو امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/persiana_Soccer/25983" target="_blank">📅 13:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25982">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NnXVUOkq41zQcQrK9I2dtOXlVR9ai7EyQ3y-KNcTJnDxW5TnyokoPncJ6iGQfLU776rRfUDeCbx3l69-3q_Vs_93X6PV0t8HzTwo8dXZfqf5Fes9DJVi36LFX9n5Yd-50jK7CKmq5LVlBYZ9d3DjtEqTftHeP2ozY51NoBjfCFkbdYeHEMMuft8KEUwkkfC71Lw5FxozJcIw5qe5JhX5cdgv-BCyhaWAnB1Lal-lrStADQhQuWYkgeklR9J_L5LpX8Q3tXHR9LDphNxEMrPmZpVxIXrWo9B0ZZOl4eh-DilTXLJKyC6vtjsL_xYHDUH-U9z7wysiApu4DjLVhaI_sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#فوری؛ تاجرنیا رئیس‌هیات‌مدیره استقلال: مابامحمدجواد حسین نژاد و باشگاه ماخاچ قلعه برای جذب این‌بازیکن به توافق کامل رسیده‌ایم و بزودی با حسین نژاد قراردادی چهار ساله امضا خواهیم کرد.
🔵
علی تاجرنیا نیز اعلام کرد که تکلیف نهایی پنجره نقل‌وانتقالاتی دوشنبه‌رسمامشخص…</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/persiana_Soccer/25982" target="_blank">📅 13:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25981">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byooo9WLllUMShqtDCUyHpl13gdFhkqvwnGqGMQRBBDwsQfnJIQMnBadcSzuLgmlgelrs2enIB-VBFKBE_nnZ7qeLFdhcu_uov-GpDNgmoDUHOmkbfdGPEoqmkEIMxXdLdEgeFyNuU4wqAqljGQ6JHWQFCLOkV92m3mq343I9hJ6fgFqz9qhHx70z8PWD5KNkS-9aNHcR9Xy33PWo0pguHSZps5Q8CiAJOov1CToU-K9xGDJBytl7LrWMtAtv9_3ovdofsmLmMibpbhBkzDrdnneVLW1Ga6neuMHIq6SBbaOR8l2iY5gmRXVQv3wZNipKvLh0kxp6vN8ik649LmQkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/persiana_Soccer/25981" target="_blank">📅 13:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25980">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/letT-HLheJPmO6dJT2QyET-XAvKU0vHIwJ_CJQsvTBnIO55c0ZV-38-vjHoyW70a01SwWlkr6jicu-ywu4UiqqP6_wm3QDrQme0EPPmYDg5yY2tDq4hoGqD972PVSmrWoyhPj18THu1aqXPrLpKk6-9dhxUCUGqG7RagXH4OA-C24h7mfyTtSprqB0WUnO9s8yPgL80IWJjXBCBrxN6S6NttYkBD_TtOsGCEtUpJO4YE40AgUYDMFLsjp2PzwG-wm7wmy-R1R8Pi7QqVUTLOLpNKm2ZpxT9qtqJSLCawHx5I3aOcY6i7vwUUEWoqOt6mUymrGgBxEaLA8Cn7DIAfNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/persiana_Soccer/25980" target="_blank">📅 13:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25979">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBm5AjKBEcY0jRYs60Hn7yr8-4oJ9UqV6ORSAp5_aMrWuluPz79-Rj6DCl5NqWTwvzdakdopx3O4HzF13IAjV08stxjTYSf5FA_3KshF8zgRetobFLX_40biuS0QlTtELG4QrXTSXFnV1BsuEx4wTumQsJCFXEsGVe_qwW1ExM5F-xzvwbwnHbslsoad1gzHcKa1eWkc4K8l73K-4Vd3nXo30QDQouxLjqFULqPGVFUnUpUSrjiU30heREz3G5YLUJQiLS43irsuv-BkgH7Uc7c-96Su36kXpZlbbK9VfPa6649FywvSnLR4w55PUGYUrKLn4yEZ0y0cR1S5yoAG2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ باشگاه تراکتور امروز پیشنهاد تمدید قرارداد سه ساله به مهدی هاشم نژاد ستاره جوان این‌تیم داده که رقم بسیار بالایی هم به او پیشنهادشده‌است. حالا دیگه‌باید صبر کرد و دید هاشم نژاد تمایل به ماندن دارد یا رفتن از تبریز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/persiana_Soccer/25979" target="_blank">📅 12:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25978">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLnaBoB_S-leghoEejC7G-MytQy58uKimHdFaP-eXdcFhP1uC9ejjqruCJZzKdKXfCUAdfeFcg9Tfzm5ShZfeXxWOd3QmYauXYB4VrAe-6aO-2D4sL3NJT0u52kektQGIpATkuIB5r8JxTau066bms56B40mxNQZgwwOhJJFm-OLvRneoXrpw7oSztHTmIBfc6uWOI3d42fc_RWeFbxxmIHcc_ReQ-zQPUMrULDu3w59qkNQBH0hf2PxQUIOJDtxIgGyd_wPLeQbFl4oq6kmRYFFj-qjE360cs82fkDNtmuyaKsLKYuYDc-5fUXBxPBSHBFEc0cqXIwNlWQpdkjyUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
#اختصاصی‌_پرشیانا #فوری؛ مدیریت اتحاد کلبا ساعتی قبل پاسخ‌ نامه باشگاه پرسپولیس روداد. این باشگاه‌اماراتی طی ایمیلی به سرخپوشان رقم‌ رضایت‌ نامه سامان قدوس هافبک‌ بازی ساز 32 ساله خود را تنها 500 هزار دلار تعیین کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/persiana_Soccer/25978" target="_blank">📅 12:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25977">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkHKGTq-F064grErIUgVk0IgfFOlYCZXeLJDY2fpi4imYuC-SQikd8fNa9pGRT5ruPoX9iWx3ST1XOpkd8Edv5X_jxV_6JTYEeH7YkrKU60eHrmhZEzwnOvw6u9HZQJJuEZkgpCmeIk7OtUi_I97phMHXcZ1K9bUKCxIjDgREEZi1bbjnOqvpiYk8qV2vpluCctNTX2M-aAfydVvD3PbG8oNJu_t2VjAbBxxLXx0AGV6QM-uK9X8h_YgQJWHgfLLSM0nWp8yZB2Zbo_ThkFes2tQUkOaw2WSL_9GANoc9_PPT6EdiR3CUI6r9VP2OT8nnPVmLaLYtE2YeCssgXJMZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق شنیده‌های رسانه پرشیانا؛ مهدی تارتار سرمربی پرسپولیس بامحمدرضا اخباری گلر 33 ساله سابق تیم‌ های گل‌گهر، تراکتور و سپاهان تماس گرفته و بهش گفته با پرسپولیس قرار داد امضا کنه. اخباری گفته میخوام درجایی باشم‌که فیکس بازی کنم. تارتار به اخباری گفته اگه‌شایستگی‌های…</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/persiana_Soccer/25977" target="_blank">📅 12:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25976">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmYUZRkdKVfn-gkEmdOGa1ASdT-rej5TE8UU_r8_lWZVniWcJ13J7Fr_GkPB8t1pUJuIMWE2flw9egnc4LKGnh3PHZXRSvYsMyQ7rIgGTqN8WSCGJqTBCPHAx_R5T-ZAkNuu0i0zp8gKUldIwKpdntFI61BEzCCikAeaqGd-yxG9ONuYu1o65AEWjZcUzP_RRATfq86cGutZT65TKhB_XnZc0ac6VHg3xAd5ygbOlnlegjDKhj42vT61uIB_9NUMz71grYFO3NV7LYtY_lPSZMr6rU9EK4fWB4cNkZW_dOqpWpdaIr4bT1GUfDWw_vuwa0KnVkCehGBWrMF7FoDKqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مدیربرنامه‌های یاسر آسانی ستاره فصل قبل استقلال برای جلسه با علی تاجرنیا دقایقی قبل وارد باشگاه استقلال شد. هلدینگ خلیج فارس به مدیران استقلال اعلام‌کرده‌اندکه به هر شکلی که شده آسانی رو برای فصل بعد نگه دارند. ایجنت آسانی نیز اعلام کرده آسانی هنوز نامه…</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/persiana_Soccer/25976" target="_blank">📅 12:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25975">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHB6CV7OCEJCuIzOVYxNvV0f0MVNlLDsQjYuvmxKnE-21F3kysTxjUtagxirhI8kwLoMq50niLt0xMNHeCdBvIiF8MueQFhjQX9jwSEbE3d7bHgup2I7WLV5HBpEp2prdEXaEYJRX6dA9g3oiUquVSmrAk1T-UhtDAndy0IOYTFOWkpRD1aspqGakinf9JW_QFf04-v5e4SraieIU_pPMjk_JRHf1ivKMZRHr7aHxCHEUWpEBC4iNeosYcmBMzbR12KoWZwnlhyb9LTd8bZpAaXHHWouxkCqEPt6XfxSWR6NdM6nTNgofJUE72e_mk0YmNpw6wLn3VfnGQRl6aUJkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری؛ شنیده‌میشود محمد عباس زاده مهاجم سابق پرسپولیس، فولاد، نساجی و تراکتور به دلیل مشکل قلبی از دنیای فوتبال خداحافظی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/persiana_Soccer/25975" target="_blank">📅 12:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25974">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWTR1hOOir9HktIosq5qHMHeHkJcWyialVposFztmGi-Q07IoPsZ8mmmtneqlPZw5CFfjCX-Qdxicqlocm87cnG2vrI-VWh0G_woN3JBtt4NnntQpSkoYL0CHPanLGg0keaXiJV6zd5OXzU6JDuTHDX2d7TzJ3NVDggqBq14Raate8G7SV-raOFpBVjFdokmX_SlTAJZuV8vRBmzsIiLBZ54JgB_W9exmTKGT9TIEewAB0Q9OTE22blVPQYyb7TAe_qnax_N9WiC8F_Gaz6kgkPnvoLb_ujvraFH_ll4oc9iRNEvGy1ezaCufBJN-kEzy85ZQbRb-sdRSBFNQHW0kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ آفر مالی‌سران‌پرسپولیس به آسانی برای فصل اول1.5میلیون‌دلار بوده و برای فصل دوم 1.8 میلیون دلار بوده. آسانی فعلا هییییچ پاسخ سر راستی به مدیران باشگاه پرسپولیس نداده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/25974" target="_blank">📅 11:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25973">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ceab272ed.mp4?token=s3MI15b7UhIqSKH_F-bE3tUwVHVuXnM59yYAApVMwQKBhNEDiQ6LuDoIZQwTX4_A0Qo8hFCupeePxyI39IRqk8m8pO5iJdIAAadPXJ3jZH56jUHC6ical1IvRFmTft509nc8ZCiavu7AsHHz_mhpKZmDuVNBM0TKFO4jPjKxqbHf-9f-IbcegpS8un6FZb9hAxbimOtsjsa46TSkIzcUWwRQY8-YbHPhd98c102vIicRtO30A9zIp9qi-jwqlxxoJR96U33y5IU2odMQRCEOukDsgRNaU1BdtXtBgE2zInDQ7994YKw9mivvlF3RcFb2zeM2uPbQTxBigQZO7PT59w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ceab272ed.mp4?token=s3MI15b7UhIqSKH_F-bE3tUwVHVuXnM59yYAApVMwQKBhNEDiQ6LuDoIZQwTX4_A0Qo8hFCupeePxyI39IRqk8m8pO5iJdIAAadPXJ3jZH56jUHC6ical1IvRFmTft509nc8ZCiavu7AsHHz_mhpKZmDuVNBM0TKFO4jPjKxqbHf-9f-IbcegpS8un6FZb9hAxbimOtsjsa46TSkIzcUWwRQY8-YbHPhd98c102vIicRtO30A9zIp9qi-jwqlxxoJR96U33y5IU2odMQRCEOukDsgRNaU1BdtXtBgE2zInDQ7994YKw9mivvlF3RcFb2zeM2uPbQTxBigQZO7PT59w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
🤩
انزو فرناندز ستاره تیم ملی آرژانتین:
بعضی‌وقت‌ها واقعا خودمون هم از خونسردی لیونل اسکالونی متعجب میشیم اما او میگه من یقین دارم که‌دوباره قهرمان میشیم. همدل شده‌ایم که قهرمان شیم و لیونل مسی هم نهمین توپ طلایش رو ببره. حقیقتا لیونل مسی رو بیشترازخودم دوست دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/25973" target="_blank">📅 11:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25971">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UPsTJXLBuO93bhu9_ntCeO8Jk9Tjv1HtvR9cv482vN7etKnqNYalqZVuxgOpoYzkk5rGiM4tLHH0_0hnczqw588UTdc3gqN-BbIZQIbuBn8A5C_6i7tR0iluI1iVFJ4LwJIiKyNwXj65_Hlij0GXggfhrJJqlJOSs5xQ67qKsCoDkZxa40hYnVtvO82J_7Vdr8-GRCs002L-KkYcTfGnSVavPuTxriZd8S2v56QKsHNgGBRwU5zo_hnIbEi5i3UH9ZONRqwI1HAzshN0Efo2EcDK_PbLCINNHtc1x3i7utOa6nvc0xkAk3uHqrBwX0oShkSQBsPwZFfZp9TzFwXSxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aFgPW__5QcPHtFOIHVVxi-AGentV8cypFoeKre7swwENIy1VotJj7ngfg2nC5j7D3gcdqtt8lyqrHy4UaWNj4c0dfPIsisOcAc_Sox9HjQMpd2kr7dKY_yijVUg9PU0eAXQwMv7qWsRxiaxnTxBpZFfwFdUo3eacRDiTJJDz3NhN5kP-G7q0QtQXPeTybU_H5KabWWHrtp7uRve4PG_HBGB-dPXBSYXbi4RJOk1uw3TLhP3dOEWSdl0xY1kfp2hhVPrnmuJ_YqnRLeL3Ub4sBoUV4r8icLspprCJsI-ybHm0gcZY5djl0zmRAjPsIOHSYtx8fkinRU0foetQdPvQww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
پیش‌بینی جدید پارتنر لامین یامال از نتیجه بازی نیمه‌نهایی: اسپانیا بانتیجه 3 بر 2 فرانسه رو شکست خواهدداد و راهی‌فینال‌جام‌جهانی 2026 خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/25971" target="_blank">📅 11:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25970">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HkBnOnUc1AM3NLeWRQQZg9iRNQ3GDqAjqXPZ41AGoLNkHBenljucYztX4L9_-LmRVIrldvr4EXwsYXQrFvMvxU-YVgPXd3CRp1G9C14gSmKSYTVZGg88gvEqJbPGZ2nBaQcak_l2UQKEZ7gZFmB3VPYgkAxgFcl3XiQ-QgP5_CeBbyoBEilnKUe9Q-FZTXXxTpcXzIEx1c2ql4scPCh1ZZKSDQXdvMIAJWBbsBtsWBF7WTLqeOMOYYKNXXUTnireK-fAB_ru9LrM1XW53Z4ZTBdzImAIAW6E1QMRCtiCNxkYCG25OGKNMGuZOYlGad1kSZ6qpuZCpWyw5ayQlx7Z1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
برترین گلر های فعلی فوتبال جهان که بیشترین فالور رو دراینستاگرام‌دارند؛وزینیا بادرخشش در تنها یک بازی‌مقابل‌اسپانیانزدیک 16 میلیون فالور گرفت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/persiana_Soccer/25970" target="_blank">📅 11:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25969">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rphijxu31DXSo1n6B91EZavCALQwlNpHw3AARAUed0Jfwhquc-LrS0GkDeN5RBBoL6-ykXcCzyYtpatWL-F8UH6HJAetocClSDzBmaIOoH9cibURwUBtbZX9mMNfDWqyim_2hgOl32ud-c_yu-bic-FD-TRdXgk-oReRzSvqQH7t0OI0j0mg-hVXJf_KlBVcWFere6SePnipCvJYY2xIbOGnM9H_uylbThzuFjhN12tTrB6DYbiXluEb10AcGmbJWmgkOO_r6h2P7DlC05s8gRSKXH8nhTuS0kq_mn8kDnBc02KhtIx_qhqe0XH_nUnYPidkoc2wKxy0FCvVJQX_Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇦🇷
#تکمیلی؛ نشریه لکیپ: فلورنتینو پرز قصد داره به محض اتمام جام جهانی پیشنهاد فوق سنگین خود 200 میلیون یورو برای جذب مایکل اولیسه به بایرن مونیخ ارائه بدهد. بعد از کارهای اولیسه پرز میخواد انزو هم به برنابئو بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25969" target="_blank">📅 10:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25968">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAbFKy_I3924UmZ4TL-DJAg4_esGAZ_6fhkMBeE4XgVlHvVv40kAnMiryICAqa_v7sirMxRhmNEU1-9YS6ZNq8alago7GnwPh_y57abd210yAIN5n1lbVkR-dS2MGb4g_6nHc2f370WSkenRsYtJVUd-1cEgLwee-XAL3LFH9zO2FrbydhzKbsWIg2ouMTcky5HCn2UnSZX-yLQlkUoRcAyRJkm8ssIioIThJdG1BJWi6cFuETp2x1-wi3B6nk1XIbM3rmbGqLGT9gNEsZvbZ4nrycQituXELghGszmrVoYy1UyoUkqnp5NHkxSUCQGwqmAAHZ35MXZFT_7KZnapAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی تارتار سرمربی تیم پرسپولیس درجدید ترین اقدام خود تیوی بیفوما و دنیل گرا رو درلیست مازاد سرخوشان قرار داده است و این دو بازیکن نیز بزودی از جمع سرخ‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25968" target="_blank">📅 10:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25967">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91fe4cb625.mp4?token=fZL28H-bFI21XquuVqm5SB5Wk9PSOZHTo2itmW50Y1oQc6etPmG-pPDajaMkrSGe5M8iGSb6l_SzJSDk2cHRRUFyb4k7YGWQXKyT5tpD8ELdZKhQrOCQYPDx-DgSBi_DewshxVNAUYqqDter2RTJeZSbiYd8dE5PONJ-M1_H_CwkwMpHwOrqx5v7bFW7069tYDeohdvu3JGHTZsCHYbx41qNSFTsE5vxO6zAhrmEKbPgk1X2B93aWuSaWcXg178BdI3_BUDkqEpwrFQYbOzMdPgw0HcTHwbBSz4PzB6tOKK83WMRHOcI7ehOCfWINLlkEcng1gHLm4KG29NOCr_p6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91fe4cb625.mp4?token=fZL28H-bFI21XquuVqm5SB5Wk9PSOZHTo2itmW50Y1oQc6etPmG-pPDajaMkrSGe5M8iGSb6l_SzJSDk2cHRRUFyb4k7YGWQXKyT5tpD8ELdZKhQrOCQYPDx-DgSBi_DewshxVNAUYqqDter2RTJeZSbiYd8dE5PONJ-M1_H_CwkwMpHwOrqx5v7bFW7069tYDeohdvu3JGHTZsCHYbx41qNSFTsE5vxO6zAhrmEKbPgk1X2B93aWuSaWcXg178BdI3_BUDkqEpwrFQYbOzMdPgw0HcTHwbBSz4PzB6tOKK83WMRHOcI7ehOCfWINLlkEcng1gHLm4KG29NOCr_p6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
استوری شدید الحن علیرضا بیرانوند علیه علی دایی اسطوره فوتبال ایران: من را با رانتی بازی به جایی نرسیدم که الان بخوام الکی جانب داری کنم. ترفند هات دیگه نرخ نما شده آقای علی دایی!!!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25967" target="_blank">📅 10:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25965">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9PTb3rkLZ3hhpajQrDn4o3OEVoj2DpA9q0KeJDK1UZkGO9LmiBvk59pm94smFmnNNSTRK3JBIa7CYtZcNwJ0tn7KiVEwd4WxBrdtaAj7Jtq9fKb7O7Ic9q6Sv0zMUKCEaf1FrQi2ZaHfi4tIBtuNPpZV55jPh18RJSZCamqX7JH-4oY6onchw1Y7fupht5jft8Iv8wT5UwotKcmGHOr2QvL0sN2ug4duLuq-lEjaAB7vx7Uy8693rP0zj-_RIP0XOq_wWuyuz1YI3ytHCDh48z6ObFDSQGrG46FyoziB6B-USm8HSEjC169JoBy-2dsKKJpe8hWIEqYk6rYYs3Pnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
🇪🇸
درفاصله‌کمتر از 48 ساعت تا فینال جام جهانی؛ لیونل مسی فوق ستاره تیم ملی آرژانتین به این شکل به‌تعریف‌وتمجید از لامین یامال پرداخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/25965" target="_blank">📅 10:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25964">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8KWARSx0F83j-bafEa0rd6l8WMjGq6cbHo0GiEyYAFL7r4AsVoSzs8suEnNHv5KZlI83Ap3DqPM7cho-GZFlulrc6yjLs02bA126iPL6WsNz3DKGpvvExLTGMee7xOlNntM_oNOxaD3ij7W2d0K8qeJh4QEORZ9Ppo866EHkvbvOhMk3C_qPCIwWUHf9CW9-GjYZJKjdpG6i5BM5kBwhe6eZykvfesLTYktW1kHRVbPVl6TahouLiSyGgQUx_RHvWstjyzAyR802vS0Aj_bipx_H_ITrEptGkoepTv_bt6_UjNjtD3h8jfpFIqCsiZJD5WSBRwGVqM9kDDvYQvG9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظات کل‌کل پریشب وینیسیوس و اوتامندی و به رخ کشیدن قهرمانی جهان توسط مدافع آرژانتین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25964" target="_blank">📅 10:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25963">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3687e3b81b.mp4?token=ilICWq_fez9gLROhhiQNVMWQ2wMfMhsz2RV4evuPsCNVNjTlQafybjzwUIHHWo1TlaXWE09_yldCrRP3mMAevy-RrJQMA6DMBuiRdWnzF-mWQSXZTOn1w4u0IEqTmbvf--uoit-Da-53oypUzOYowqn3fZOdu6BtOv0WStozOYGD7fSkoitm7all9VFXTCI6dyr6fSmDC1RRDbSi22wzg4EIZXteuJ7fDiOwrsU1gLajj8ptjB9Ndl-4YFri2JqIPq6LbYHLJPPE2rHBuLiUOlMW7VFeztnpUskPQVEt6v5YOQgiQfA3NtsFvhVv9KWF0uSM1WjKlfxrVfXKiY-4iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3687e3b81b.mp4?token=ilICWq_fez9gLROhhiQNVMWQ2wMfMhsz2RV4evuPsCNVNjTlQafybjzwUIHHWo1TlaXWE09_yldCrRP3mMAevy-RrJQMA6DMBuiRdWnzF-mWQSXZTOn1w4u0IEqTmbvf--uoit-Da-53oypUzOYowqn3fZOdu6BtOv0WStozOYGD7fSkoitm7all9VFXTCI6dyr6fSmDC1RRDbSi22wzg4EIZXteuJ7fDiOwrsU1gLajj8ptjB9Ndl-4YFri2JqIPq6LbYHLJPPE2rHBuLiUOlMW7VFeztnpUskPQVEt6v5YOQgiQfA3NtsFvhVv9KWF0uSM1WjKlfxrVfXKiY-4iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
🇪🇸
درفاصله‌کمتر از 48 ساعت تا فینال جام جهانی؛ لیونل مسی فوق ستاره تیم ملی آرژانتین به این شکل به‌تعریف‌وتمجید از لامین یامال پرداخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25963" target="_blank">📅 10:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25962">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ht3Y9UhJUNU7UfpUsQFZE6N6-kveJ98oUdDTIaIu1beY0qB9SuRQHy3h89njGComl7IN_x6gfSuL1QpMR19IJOYBpeSmhspUrUP38e68WHBVfP23_qk0GTo7_pFe1THFgvjHTb2JQyNBbqnYzSK7MlK4VqWUjpFCfN_4cmAfeIbDEz3LJnzHtuKH-wj64UABbvoTV3T24D9sQCiOalkBIkzQ3PQHs_ied-MapUWQ5OJRBcBe24ut2q4KL9GZKG2wymLc6Fix4Ucnq-jnEZyQKRTVrSVBl-t59A9TPQ5dWcIlTabEoVvCIPxfAed2V4IbYY_H9NTC6B_vNDPXt6RLJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ همانطور که در روزهای اخیر خبر داده بودیم؛ محمد جواد کاظمیان وینگر پرسپولیس در لیست مازاد سرخپوشان پایتخت قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25962" target="_blank">📅 09:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25961">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-iwlnbwwexAXhagYvU26v2kQQqaNnIJvLQWRPgBjplFBfzzSlqPszmD27GhvQB2a95mHq6rpomz0RhlQNWMtlEtCVb9mMwGufQ5fpxhaNiNLu1Esm_cacXPXYZJuEeZZbmy8xPkYGFR00GMOt7NDaF0WS33Oh4w1Lf-PT0erHP1DaNfS5ZBkSi3YvuS4KrO0-awYEWph_w9bYfgWUMDxK3k4lu53m5ugShYrQs0jo6N5n8ExAaZOtTEXBlQN98D6Pj39_d0NuJN0kBvKEGsLn3BzKZMsN8qHNm-OnG7bFxOuLkz3SalEgLFFC-DGjR6XN_NXX1krJRcG5Y_Xu1GEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◽️
🔴
با اعلام مدیرعامل باشگاه نساجی؛ باشگاه پرسپولیس درصورتیکه رقم‌مدنظر باشگاه نساجی رو پرداخت کنه این باشگاه دانیال ایری و کسری طاهری رو به سرخپوشان خواهدفروخت. زندی اعلام کرد که طاهری میتونه با قراردادی قرضی همراه با بند خرید دائمی راهی پرسپولیس شود. تنها…</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/25961" target="_blank">📅 09:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25959">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YALTxhNtlSwcjBjFHp-scmSzqKhFK6otxCR3NdCI9GaowoHE7JFWszZO5tA8x38ro_5Wmj-hmWAxqkFOGen9Qr81UpHkfEyjnYlAx3ewL1TT5KIM3u_aHRCQMQgGo0dJ0sDe9V-ohVeiFOgqiwdFIKbmNuHL_KGaguE0vSIvJQyt6FtOII2BTTn_NOW5o-q0QV-SvLAKgljQ0A7GMN7WXnO_I56cCVOWQbmX8ussXeLv2TXWHlzpt5M2EK4rAK9apuPrLIuNph-E2J_L93HGyx0TDD1d7aFrotLQxJOdOyg0EAbSAyBFxtcUU1NM9SpeAzmvYIEuZuILiF5BPm5AnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تنها مسابقه مهم بامداد فردا؛
رقابت فرانسه و انگلیس برای کسب مقام سومی جام جهانی 2026
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/25959" target="_blank">📅 01:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25958">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7T4_HHuyqJ9tsuEq0UtWYd2xBFSXEIrTWUsGZxAkRymPwTB8r-7JQncTKr-A7-wbbNy5NRBD3TkqbrFQQWuAhiprk_VcqeWiUaOsB_EXO52eyOazvFQ4DZm6_jwjcnNK_zmiqblXeZKnxJu4KeGLDP7aRjT0dXvTRWfbt8_GvFCxt9dmdQ9EbL_sIrVICo-fpuZ9MFprB52eIFqbpJYajRLdAlHQJwt-tdfFDVMy3XsTbiRuZP5ZkqLSi-i42etdzZAuMxTqFRVLN7hrjBHpP21vpy0sV7ZI_Y65dvjrC0y7iQoSdf04PYTr5fyGONtZYJ0AiMWQRW-GhCmQGGH2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تغذیه بدنسازی‌ویژه قبل و بعدِتمرین؛ چهار گزینه پیشنهادی عضله‌سازی عالی برای قبل و بعد از تمرین
‼️
بهترین‌تایم تغذیه قبلِ‌تمرین‌بین ۳۰ الی ۶۰ دقیقه قبل از شروع تمرین؛ بهترین تایم تغذیه بعد از تمرین بین ۲۰ تا ۱۲۰ دقیقه بعد از اتمام تمرین
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/25958" target="_blank">📅 01:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25957">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e06c4bd948.mp4?token=UwSrj79iBnLQhopLF3s_9ItCs1P9NDLiH2aQBEgW0zBbUSClsg67pj5mY-3gbE4tjNnAkJIKRhpS0q4q2utWklqZKRyyaQVhWjk6dzdR9Iet6QXTLevCMXibgFJhcU8P4KEddJT00CD4Bz_B6XioR4TIBbOTxi3qUWudg6rxOZ2BoYVjrE99MSXTQ6_omQDdrdWbZjLwG_fYpJzK6G2VSxOLzJmgwm-mJAfYXh2TlBunC-NmLdAoVd-2RMVwn4FIO6IzwXdWgFyxHU8wFBXxO9jp1JdwVhGy_zm6CC8gVzk0ivg2MtoVLtz3AvwgDDf0serJ7cWiMIws-IMvGF0ADw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e06c4bd948.mp4?token=UwSrj79iBnLQhopLF3s_9ItCs1P9NDLiH2aQBEgW0zBbUSClsg67pj5mY-3gbE4tjNnAkJIKRhpS0q4q2utWklqZKRyyaQVhWjk6dzdR9Iet6QXTLevCMXibgFJhcU8P4KEddJT00CD4Bz_B6XioR4TIBbOTxi3qUWudg6rxOZ2BoYVjrE99MSXTQ6_omQDdrdWbZjLwG_fYpJzK6G2VSxOLzJmgwm-mJAfYXh2TlBunC-NmLdAoVd-2RMVwn4FIO6IzwXdWgFyxHU8wFBXxO9jp1JdwVhGy_zm6CC8gVzk0ivg2MtoVLtz3AvwgDDf0serJ7cWiMIws-IMvGF0ADw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره‌جالب‌علیرضافغانی از علی آقا دایی: طبق قانون سه بارپنالتی علی آقا دایی رو تکرار دادم چون ابراهیم‌شکوری زودتر میومد تو محوطه جریمه من‌هم‌مجبورمیشدم تکرار بدم. علی اومد گفت بجون داداش تا صبم تکرار میدادی من باز گلش میکردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/25957" target="_blank">📅 01:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25956">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOGYQWzOXzy47BY7WUa3bV73GyyN2yaSuSO0AXY7Ayb6frW5k_Go7nE-lwY3OW6tM9UgPMszbVAfOVyP0dpgx67xVLy0WldeH8x3zJp7dKdggmJvCAIgzYq51fc6rbOXLTIXq285NfJy7L6TC3C5XNFHQwIunmNM23PhswF4cFFDsm6ZAQthu1c0VzjlXBrg23rrVse9GfdqxQRIT2byWNr-syVzk-r4TGSZyjPjJjqnoR8Lfzy5axfq2aPVTNOKtfFjOgxfEFBV3nNeiY3wM1JSfCRHBtblEjjp4EaBItmxPUdwkO5vm1cCwTCdp_dLem6jlp3wrSHVm5KK2Nn8xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/25956" target="_blank">📅 00:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25955">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRpy4NcVVCNSqZXW0tvBair1vKfysF077REFWxJeTmBbSx6MA7svOuWAn8keElwqs44xk3W2QqLSTFFWTyr6_9ueGU7MyKF6ZpLSQwr5CZPxHTzEx_VDHXK-x-TSQH_je9RJhwbJcn2QGZQKRvJo4tPdCl3npcct9aiun-qXMMOoBa-765k1pH-f0Rh4F9kutRlYO0QHezvwFWVjLaFy6wRwOUOo1OqfprqY-nYT1AdtcKwo8wf-1VCwKaHFO0JpcFpNfuQu2CTkt7Phr3snLEgJX5YtB4ipCvuUbCk8fIFJPP1Gk_KNq1dHRh7TNSl2HMuHm79KWPlKICKrpElj9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
👤
علی آقا دایی اسطوره بی بدلیل و تاریخی نه فوتبال ایران بلکه‌فوتبال‌دنیاست. اعتباری که علی آقا نزد مدیران‌ باشگاه‌های‌ بزرگ‌ اروپایی‌ نظیر بایرن داره بازیکنان پرادعای‌این دوره‌فوتبال‌ایران حتی از نزدیک هم استادیوم بایرن‌مونیخ رو به چشم ندیدند. زیاد به اون…</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/25955" target="_blank">📅 00:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25954">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cK6P475R3hJC07T3mozAiDaE7-5aKtb_Fys0eRiAalInbHvQstc4fra5kRou8OhuFAAp0IaPVaZTIljAw3ZYbQFpEbV65sVtEMDYqNIJI_1vl4Rao_Qv6KsONU7ZLFNiDd5h5gg3iltmMOCyJ67IXZk-ZhV-ywKLWsty7UE-Vy6z6zyBUuNQVy3opx92q9SOfaBVrKz9Lz1Ar7hmp4r93eXTB4y7N27M1JErE-wEYV482oAXO9r1qR4Qjmdiy3lEbY7la8X4mvt-QvuWYH-wlc9MqyEasSVdFKy8TX-y6BKjzmZiHBO2A2W1KeFJv1SkKY0iF87qxnlKTE-b8MQu5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استوری شدید الحن علیرضا بیرانوند علیه علی دایی اسطوره فوتبال ایران: من را با رانتی بازی به جایی نرسیدم که الان بخوام الکی جانب داری کنم. ترفند هات دیگه نرخ نما شده آقای علی دایی!!!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/25954" target="_blank">📅 00:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25953">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jy6i0tED_W5m7mTIA87Q_MWnApmKUqcegE0QMVMVtvJugmYf02zTX3QudQ3edI5GEgCWnVOGISBe5Iiv2dGLaXxPfgVIsNSytd8rgGPWN1YJs9LHmyVYX0YicGN6m70Pk9VM_pQiDxPU1_N176ccyenvL0PmN7jTljFCWIeVP2Wx4VD4ZKylgHZUk1bNd_MUIjy-GTmPIhA-1WhgSPM2c-CLGkaF2ZqpUh0L9xHPOeeTgSVHa7efCpjtyZPBUIo3_9fMMRt3qTVLw4LsUc6yQ8oqORF6B4m37idv18zPyV4As-O2qzcMalfblQOnmTgWPDHJeClZNaLN6_naxlhXdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
کانیه وست پیشنهاد ۲۰ میلیون دلاری سران فیفا برای یک اجرای ۵ دقیقه‌ای‌‌بین‌‌نیمه‌‌فینال‌ جام‌ جهانی رارد کرد. کانیه گفته آنقدر بزرگ است که اصلا نباید استیج را با افرادی چون شکیرا یا مدونا تقسیم کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/25953" target="_blank">📅 00:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25952">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d160628032.mp4?token=pcHd5owqRxrXHGe6rqWUNr2HTo63M7DxdCTkKevu9LBJZJuzDZlrA9-qULLawf729-H5Sj3ees0KdJCQfY2XAAgVoSft2TA6baxD5Hxx_H72vA4QK5-5DDJJjwq_lLqsNNnCIttl1DNoAPQawkFxK-vxlpkUjSSv6mFMU_6quKWbr7WPq1oupna6zjL-gmjM0jKRRpRK9ji2JOXiQjNShCB4CT4wdO9BxjRuMMRfDhp28p-lvK6f2l9ov9tCjgUCHUi3V3d969UDngN23WFe0LZVFgcnyY7Ivmtmh9BNykkVWXsjeuz5TEEi9BIB7Cwltmp5bf5lHVnIL9y7uMkxnkazqZVXjfqwk4XMCN8sfmq_jhmbE_zLP28_GWMmrAODSio89J8xGkygKJP7MjcxFpaItWj3ElQpV6L52SnF_JGtqhhnbIWM3f5AXEjWBZ2drLfxurLZzX18JYpWqlSa6cbMt6MMSgx7G5BXiin0JNR_mxwdcSYWJU8iYw71wtD6KLqTAJnJ_jbq_DeCSDwDXHhfTAWxzrhLmjpyQOdUUylDSWyMPOrJc5ElHzgteZRRa9BoBSKr9g7FBJNgHkbsSqbWlTmdkHC0KafFgkNj6pt2OVe6QWroUPGcb56_MkMxO3vasD-bj8vlR3_197EIvL28IqZkGL3-v5bdni4JUUc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d160628032.mp4?token=pcHd5owqRxrXHGe6rqWUNr2HTo63M7DxdCTkKevu9LBJZJuzDZlrA9-qULLawf729-H5Sj3ees0KdJCQfY2XAAgVoSft2TA6baxD5Hxx_H72vA4QK5-5DDJJjwq_lLqsNNnCIttl1DNoAPQawkFxK-vxlpkUjSSv6mFMU_6quKWbr7WPq1oupna6zjL-gmjM0jKRRpRK9ji2JOXiQjNShCB4CT4wdO9BxjRuMMRfDhp28p-lvK6f2l9ov9tCjgUCHUi3V3d969UDngN23WFe0LZVFgcnyY7Ivmtmh9BNykkVWXsjeuz5TEEi9BIB7Cwltmp5bf5lHVnIL9y7uMkxnkazqZVXjfqwk4XMCN8sfmq_jhmbE_zLP28_GWMmrAODSio89J8xGkygKJP7MjcxFpaItWj3ElQpV6L52SnF_JGtqhhnbIWM3f5AXEjWBZ2drLfxurLZzX18JYpWqlSa6cbMt6MMSgx7G5BXiin0JNR_mxwdcSYWJU8iYw71wtD6KLqTAJnJ_jbq_DeCSDwDXHhfTAWxzrhLmjpyQOdUUylDSWyMPOrJc5ElHzgteZRRa9BoBSKr9g7FBJNgHkbsSqbWlTmdkHC0KafFgkNj6pt2OVe6QWroUPGcb56_MkMxO3vasD-bj8vlR3_197EIvL28IqZkGL3-v5bdni4JUUc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ویدیویی نوستالژی و خاطره انگیز از تقابل جذاب نیمار نوجوان مقابل رونالدینیو در لیگ سری‌آ برزیل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25952" target="_blank">📅 23:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25951">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d33f152b80.mp4?token=IZi4E3JPTYStTEbepAXcvEP4lfrZmEZA8zfUcbJ4qadPvdbmmLsZn5ZrM9FeIE2gEBuuld6dXnYhLVSID4I-3ERQ22rsGuzokUdsBO5vqXz1ZqGGSF3hNBA7DUElTdBB5FT_Cy3xwaYgP3nTjeqoC2EfC4QySqsn2hIgKbxtHvpNN3o5nWUzGLCDs4YmNvl0M0XqwC2X8-xWP8HCcx3eugYTQwA8F73fDBxEqcwY7AGuuhe-k-ic1CEZiLq-6Pr83wLoQrFbvGmJQv1b58-hJnvBHIOL16DrO9DWYdfFHJahRk5tQjUnge0gTq5oIL_v71r-mqgh3Hu5F3Jq0EyVLzQh_xy7eEeyP16miu06a7I37KG_EvjbU-2y7OOYP1X0sg83j2CVcSRKJcdwJ5UAS9TOWJBYBWlt2uxiCUgatsAdmi7BG9vaccViZa9EGg_b_k9imoPP1yqmIerbI-YS2ExD-OnGplHDEjAl2OlSDawTtv45HrwA6GxgS3uEiZpzcocgLjtXPrsyFMfsrtPf3Mpr7q8bbvIHvjiUn41ew-411nP91kzVmapzGUfdDDvkkWKlIvTrVKtWA18j05JXsYKcV1XBcnqDt-UKE4WXRYcs2s5ZCbEHY6dtydHQokdO8WE5QuApz9Zy5BS9DvmULorAJEuqvI7g8buw0oWRD6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d33f152b80.mp4?token=IZi4E3JPTYStTEbepAXcvEP4lfrZmEZA8zfUcbJ4qadPvdbmmLsZn5ZrM9FeIE2gEBuuld6dXnYhLVSID4I-3ERQ22rsGuzokUdsBO5vqXz1ZqGGSF3hNBA7DUElTdBB5FT_Cy3xwaYgP3nTjeqoC2EfC4QySqsn2hIgKbxtHvpNN3o5nWUzGLCDs4YmNvl0M0XqwC2X8-xWP8HCcx3eugYTQwA8F73fDBxEqcwY7AGuuhe-k-ic1CEZiLq-6Pr83wLoQrFbvGmJQv1b58-hJnvBHIOL16DrO9DWYdfFHJahRk5tQjUnge0gTq5oIL_v71r-mqgh3Hu5F3Jq0EyVLzQh_xy7eEeyP16miu06a7I37KG_EvjbU-2y7OOYP1X0sg83j2CVcSRKJcdwJ5UAS9TOWJBYBWlt2uxiCUgatsAdmi7BG9vaccViZa9EGg_b_k9imoPP1yqmIerbI-YS2ExD-OnGplHDEjAl2OlSDawTtv45HrwA6GxgS3uEiZpzcocgLjtXPrsyFMfsrtPf3Mpr7q8bbvIHvjiUn41ew-411nP91kzVmapzGUfdDDvkkWKlIvTrVKtWA18j05JXsYKcV1XBcnqDt-UKE4WXRYcs2s5ZCbEHY6dtydHQokdO8WE5QuApz9Zy5BS9DvmULorAJEuqvI7g8buw0oWRD6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب حسینی تو برنامه امشب میلاد کریمی بلاگر معروف‌ و معروف ایلامی رو دعوت کرده این بخش ازگفتگوشون جالب و شنیدنیه ببینید. میگه  قبل از بلاگری نمیدونستم ده تومن چند تا صفر داره.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/25951" target="_blank">📅 23:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25950">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YP-3RVacUsbOqzUkI6Rp9e3Ghi9Si77Rc5Yfb2nf3LXY3SeEGPuEdt_lrYK8nVgho4rTdam8O6ixOQgPy1YsfSVkJ7fQFtmFI5LO6yxIqsYAYynNYg9ZR2VVm7CZGsnALW4p4xZX5fMDcONtDiFT0Kx0FLaxtMLJ2_kR_jEzCFc17DkHHqsWK5YRKDiBggtzsdWpHYAXsbKhd44A1WAZiAYOQ3TL6SyEqKnlttrjpxfIhHfwcJvGiJc3A26K4Z9Lt7zGd8Kx0cGVlCGn1XDA8E9sItysqT9mLcaxTQcNNU1-3SJNxHZNpk_bUHwWrzgnNG3EsxOr8jNeTAuxJv9fBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق شنیده‌های رسانه پرشیانا؛
مهدی تارتار سرمربی پرسپولیس بامحمدرضا اخباری گلر 33 ساله سابق تیم‌ های گل‌گهر، تراکتور و سپاهان تماس گرفته و بهش گفته با پرسپولیس قرار داد امضا کنه. اخباری گفته میخوام درجایی باشم‌که فیکس بازی کنم. تارتار به اخباری گفته اگه‌شایستگی‌های خود را در تمرینات نشون بدهد گلر اول تیم پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/25950" target="_blank">📅 23:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25949">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e604eb6c6a.mp4?token=JpDXicr4eYISYRkc0rZaW4yT1pvzmIL5Qgvz-yAZumK5JQcp3GCrugdlBCxs6Xom5gGB3bmx-hbncVm7DiFhv3Z7qKvlrzEwTxmHMWZHR1Ssls3vWUHBLmZz8gRCBm4T-O7OjRc8Vs09gvTVztLpkAg570FTzdwP4cb0Zd3PYEpWUiHwEn1Z0jicB2cWvgT4f4GZUYKY9NrhiI1aLAnsnm8RdlepA9HGzAqNBkqIvwtJhJQGbSpsFMGT2EweNrbIQGZZwkpeqjCwyP-YeXmj2rP0A2gCldm-gfLPnm2D6-_72GpOcpKJv8A1PAnNUMTLuj8EaXU_VUlkwUBwHbWAEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e604eb6c6a.mp4?token=JpDXicr4eYISYRkc0rZaW4yT1pvzmIL5Qgvz-yAZumK5JQcp3GCrugdlBCxs6Xom5gGB3bmx-hbncVm7DiFhv3Z7qKvlrzEwTxmHMWZHR1Ssls3vWUHBLmZz8gRCBm4T-O7OjRc8Vs09gvTVztLpkAg570FTzdwP4cb0Zd3PYEpWUiHwEn1Z0jicB2cWvgT4f4GZUYKY9NrhiI1aLAnsnm8RdlepA9HGzAqNBkqIvwtJhJQGbSpsFMGT2EweNrbIQGZZwkpeqjCwyP-YeXmj2rP0A2gCldm-gfLPnm2D6-_72GpOcpKJv8A1PAnNUMTLuj8EaXU_VUlkwUBwHbWAEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
علیرضافغانی داور 4 دوره جام‌جهانی: اگه توانی باشه در‌جام‌جهانی2030 نیز حضور پیدا خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/25949" target="_blank">📅 22:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25948">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXW_Prm92KtOD0nhHeA1da0MaHOD7_01AZYtGKJ3UYObgigucU8lfw142kxtT-3KzHLD2kYkAwVMuJysQ9IzSMrpOXEWqBDMFyr5I2CAep4EhcZC2E-kBR7-4qHROh2jSCPynxfNy4qyKPaOtErRughlWaWkXxdBOhCJqx1F39_uGwgAE3M1Up5peHC3YerDG7zJWsmejcgxlV-QHI-Eh8asn_RthF23fbiySlGyFjrddsMW4i8OKE7TQSwFsrWhzv3rTKnJgdgJTDfbu-1oND6YNhHB2-7YvwKfQJsAcFAu_rPAtP0c23mW3tUQs3v8T3x1P5MBmnsI7vXqOGAoBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیکه‌های سنگین کریم باقری: مسئولین سرشون شلوغه. علیرضا بیرانوند خودش یه مجسمه از قلعه نویی درست کنه بزاره خونشون لذت ببره. علی آقا دایی هم میگه نگو بیرانوند؛ بگو دکتر بیرانوند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/25948" target="_blank">📅 22:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25947">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/985ce0bab0.mp4?token=lF8hJfCC56XggJG_u_wslzH0Z-z7USrxiFp6cWTFl_H4kR8ddM2FJl6t8M5ud28TkOWSGk_XrHIDtjav7DnAWtaH04xJKnUAdREt5faBCx93r_4mA8hnb1tUGCWn-kK_DGL64OtsrwJ7fysPxLZCsMZcXcUBogfZngZtswPEtfbtIiU5aIw0PZp5V_Y51CX-L_tjT2sHQrVsPynNMf5xuJd6pemdbhJLJD-5IoDfZ4P0LDWRyRhtW30UVNYsq9ugEeEa79ShNZBHllxhY0haPX5UkoBMZJ4KBND_iczFn2DFj8KbmS7YjWQ36T44n8EsR6V3IHgAujphHJzC5r3q-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/985ce0bab0.mp4?token=lF8hJfCC56XggJG_u_wslzH0Z-z7USrxiFp6cWTFl_H4kR8ddM2FJl6t8M5ud28TkOWSGk_XrHIDtjav7DnAWtaH04xJKnUAdREt5faBCx93r_4mA8hnb1tUGCWn-kK_DGL64OtsrwJ7fysPxLZCsMZcXcUBogfZngZtswPEtfbtIiU5aIw0PZp5V_Y51CX-L_tjT2sHQrVsPynNMf5xuJd6pemdbhJLJD-5IoDfZ4P0LDWRyRhtW30UVNYsq9ugEeEa79ShNZBHllxhY0haPX5UkoBMZJ4KBND_iczFn2DFj8KbmS7YjWQ36T44n8EsR6V3IHgAujphHJzC5r3q-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
👤
#تکمیلی؛ رسانه‌های برزیلی: علیرضا فغانی داور استرالیایی علی رغم داشتن کفایت لازم، به به دلیل داشتن ریشه ایرانی از قضاوت در فینال جام جهانی محروم شد. گفته میشه دونالد ترامپ در این موضوع به دلیل درگیری با ایران نقش داشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/25947" target="_blank">📅 22:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25946">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/geyC-4NuhRauRtIrW_yj4fLivLeL1nFrX8LKd9P9mHCxQuJs0NUveMsWzisM3y-YO2wBY8DcAd67p6TfKtUKoBKrD8mZOCsJ0Tq77I1_39T0XYhmFQn-Kq-rbzBsLzErPAy_twVXntL6-LKZ3W7XaGKNm_C7v3M7yPRIDyrCwN8H8hjuqxgJD7Uh7LsKgMvm19QudxAUVF8dozc5eLzdXUt3YXDv4Vplfuxk6omwoSL69dkuQj9FZcTnPi-mEsT-poKeixq49F1FzNyb6NTsfvI0WoNOmUE_wOoO-5WYdSgtG3JfTlv9AnadnJJHk4xbP_BlKXMKKv2DmjMWS9jUaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛بعداز بالا بردن عجیب و غریب رقم رضایت‌نامه دانیال ایری از 100 میلیارد تومان به 190 میلیارد تومان توسط باشگاه نساجی؛ باشگاه پرسپولیس امروز مذاکرات جدی تر روبامدیران باشگاه خیبرخرم‌آباد برای جذب مسعود محبی مدافع میانی 22 ساله این تیم…</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/25946" target="_blank">📅 22:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25945">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UecxM1tft_Gm0y4nQ91d5q-neJZosYUZXMyKy6KrvpdWLMEV3J_OJCJqtrJikqDnMkwVkZ7-0uswOZAVydVkBqUleQpzRqrqfITzXy_SdtlBTBOr8AObsbZiRonYbXPnWRsZt1E7x7-IoZX0_Na7I6HRM3o5hH9lE1Zja5ZNyYdv3gmNBYX-07gCJOz8bLZ55pTHF7HaAaz9ae_BfeqQu6h7_E5UgOFWi08MWURrL_lU0W5RLOAisqNxtSvun-CCWFArJotHNcZ-57liUxA5l-bz9k85QfC38Aja92MJ4tHu_eni1TjMnyBnPd0V1Xqo8gmiqkj4cdTclmXA3cFG1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
خورخه ژسوس سرمربی‌جدید پرتغال: من هرگز کریس رونالدو رو ازتیم‌ملی کنار نخواهم گذاشت و تا هر زمانی که خودش بخواهد در این تیم خواهد ماند. قطعا تجربه او در یورو 2028 بکارمون خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/25945" target="_blank">📅 22:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25943">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96e7669a60.mp4?token=V9IYRWu9i-skDM-Tc-211upjvFHLTs3HCP1g8CPkAmwR07aQuq15Q3y-fyw8wNwYFbSC3QmTAjloQlHLw_mAOnU61_RdVvMVv2_XMHpKioAqROgh2PM8h-SYSErTZIZBnZeINLoAxqUyyybM72HWu7JrnJSr_rS9qGx22ZZSschKJ6UWzYbIJ-ZkKhqaweK0lY8jwjrTvKzkHV-16xEcMPgrQagpN0sseyz2JG_orwzao53N7YF5i9n0RKw7ZAKcXVrjkI4SLhxU2LR8BRVy0Oooblj2On9wRD2bhlyNmIFxascu2AugnDqC9TkVBPaNeSkRE0dBPKoyxvPgNgQuAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96e7669a60.mp4?token=V9IYRWu9i-skDM-Tc-211upjvFHLTs3HCP1g8CPkAmwR07aQuq15Q3y-fyw8wNwYFbSC3QmTAjloQlHLw_mAOnU61_RdVvMVv2_XMHpKioAqROgh2PM8h-SYSErTZIZBnZeINLoAxqUyyybM72HWu7JrnJSr_rS9qGx22ZZSschKJ6UWzYbIJ-ZkKhqaweK0lY8jwjrTvKzkHV-16xEcMPgrQagpN0sseyz2JG_orwzao53N7YF5i9n0RKw7ZAKcXVrjkI4SLhxU2LR8BRVy0Oooblj2On9wRD2bhlyNmIFxascu2AugnDqC9TkVBPaNeSkRE0dBPKoyxvPgNgQuAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
لئو مسی وقتی قبل شروع بازی آرژانتین - اسپانیا در فینال جام‌جهانی 2026 لامین یامال رو میبینه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25943" target="_blank">📅 22:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25942">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cfa86464a.mp4?token=oT03YsqVKVNdCP5rO7bF3IbXH1k7Um0mhbhbBoVdDsgh_g_KSpdmBNhiN8jrWxMFZIRrI326z8UTPGaRVKACH6_B-m6fnoyF8wRb7_Z-UWx-UKL4DxWKA9-pFVRCzaqdLKrsaNYgF17wuFOFFZnfkTHn1SHkYfq3ZBrY74dMlBdYzijiByuepFU9TZtkzSfFLWAPQ9nhfoBJw8NaO2zpTYPqSvh7J8LhQBFArOb1dw_U6r8ju9oCb9M206sNfGIBBaT2iCyKlgA2dYkKM0uXIXSD3cIFgT7_0dztraf5WNio-qLrLU76O1vUdRs9tMAfMu4Dh-IeUkB3JS_d1pk43w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cfa86464a.mp4?token=oT03YsqVKVNdCP5rO7bF3IbXH1k7Um0mhbhbBoVdDsgh_g_KSpdmBNhiN8jrWxMFZIRrI326z8UTPGaRVKACH6_B-m6fnoyF8wRb7_Z-UWx-UKL4DxWKA9-pFVRCzaqdLKrsaNYgF17wuFOFFZnfkTHn1SHkYfq3ZBrY74dMlBdYzijiByuepFU9TZtkzSfFLWAPQ9nhfoBJw8NaO2zpTYPqSvh7J8LhQBFArOb1dw_U6r8ju9oCb9M206sNfGIBBaT2iCyKlgA2dYkKM0uXIXSD3cIFgT7_0dztraf5WNio-qLrLU76O1vUdRs9tMAfMu4Dh-IeUkB3JS_d1pk43w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره‌جالب‌وشنیدنی خداداد عزیزی و جواد نکونام از اهمیت‌نماز درامارات درویژه برنامه امشب
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25942" target="_blank">📅 21:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25941">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsrQNGUzWAdLEV02OKUPBwLJz9RKNobq6_pU1XJiDB1ofy21ts8OtmIHbmQ0_aiRax8ggaTcjwWX0sv3TunJAAi3IvRTlRD8-n1MTW63tcyOQvxwSyIJmd7B-YEQQUg-jrBpTc7i2u-9q6rWT9sabCwFcO1oQIsZ7wSkFPkDMBNKLz9GhyD_VP8ZXDc9ghypXdDC42E4kYQxOCRmhfTh5z6J2f8Arxycc6FRpYsJohY-cspwZ2IgowB7dqdrPZ8Vc9awivAg7PslCm-kIXqZL1cHhvUkcng9nwSJoXX9qEd1LuQln36DpgZk4QqRBorYbyJWT0KsPmyebr3LiE6I2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛باشگاه‌پرسپولیس خطاب به مشتریان قطری اوستون اورونوف: چهار میلیون دلار بدهید رضایت نامه اوستون اورونوف رو صادر میکنیم.
‼️
این اخرین خبر دقیقی بود که ما درباره فروش احتمالی‌اورونوف‌ازباشگاه‌دریافت کردیم. با این پول به‌احتمال فراوان محمد قربانی جذب…</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25941" target="_blank">📅 21:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25940">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03df1d2600.mp4?token=lg9i3MZ2Jq1abcRWaeoTxTNv8UlCwvmdMsqaCM8Vrn0Ir8vP8XVqJzk-owPWpBPnvhiLHqmtaaskFu_dhv-rlccoq7ckyyVOVbcvx8BOR8TZ678E59WdCXVjX1VUEMFGS0oj7EeGJZH3kXcn4kN7uB1nFoErMauqfyJOwUUYWE-VTERd1gD4dL-sihATqu6tXm3fdZEy36W4P1gw-bL1AbkutAag2erMKNCtA9v2ZZ1lu3aFnI6Y6hv93BDu-QOikIm9uJAMQlzV6l6rHl1JMbwPZS0_bXt9G2YJ-PuTo-5GQN17IHWO87dGiJHTK40Qmd15f-APL7tlym6zImHiCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03df1d2600.mp4?token=lg9i3MZ2Jq1abcRWaeoTxTNv8UlCwvmdMsqaCM8Vrn0Ir8vP8XVqJzk-owPWpBPnvhiLHqmtaaskFu_dhv-rlccoq7ckyyVOVbcvx8BOR8TZ678E59WdCXVjX1VUEMFGS0oj7EeGJZH3kXcn4kN7uB1nFoErMauqfyJOwUUYWE-VTERd1gD4dL-sihATqu6tXm3fdZEy36W4P1gw-bL1AbkutAag2erMKNCtA9v2ZZ1lu3aFnI6Y6hv93BDu-QOikIm9uJAMQlzV6l6rHl1JMbwPZS0_bXt9G2YJ-PuTo-5GQN17IHWO87dGiJHTK40Qmd15f-APL7tlym6zImHiCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
علاقه‌ شدید پوریا پورسرخ به رئال مادرید
: رونالدو هرتیمی‌بره دنبالش‌میکنم و کلکسیون پیراهن رئال مادرید رو دارم. عجیب رونالدو رو دوست دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25940" target="_blank">📅 21:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25939">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqUt6hLg7CCBpVAYXLQTDVPfDChKQF7VvMzWu6WFHtgZZGM0eWeiMqcn5NAEGmOtqjvW69vQvWBfmcQNv-G4bgXCa7k7GcopEmBLmE0fOG_6nsd7IfcjGhlvlS_pe67nSwbndN2exsTLhBqTuh7xHDNZDX5VHNfABi4cYNxmq-1YccWMr7L2kiuEDP_WEmMKstVbvT-JMT8rnVwG1fj53DQcyk1u_bKzBSNeZugQRht_mK-VzRqD1VkY9srjaPr8EjKYNdXf8jRMw6qqLmhoFb9m8omRNjZu33YQGre5tLonnYlU8eaBKap6VvuIROH12BfvovLYNY_6qsbd5x0dQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ایکر کاسیاس اسطوره‌فوتبال اسپانیا:
ما اجازه نمی‌دیم آرژانتین‌چهارمین‌ ستاره‌ش‌رو روی پیراهنش بذاره ،اسپانیا ستاره دوم رو روی پیراهنش میذاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25939" target="_blank">📅 21:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25938">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A711na2Twn2t9-ICzjbhy5ux8NYbnxKNsbB5GtiQGMTO9Tlqzl6WSMN3N_G7emeppzK9JeqAz6638MWgBJb97Ew8aNrq6M9vRGoRWfZIUjoo6kCjR_b2FN0NsrjgV-3qLhrHyLWr2579O8U2Ib-cZvP3uYwsjc-TOkgA-P2q1eosYudTXB_cFXCynZZYK7Vf3b4yLJ4lnPBp2uXSJ6Qx8KEVKhxb7XxgcnJqAgmgdfFypinA29mmSsRPp0Ljlv9UqU3p5o4p4FjGQHvLQjyvKaTpu8xZqrhlTb32Ggcduqr4Dn5lLDi3lq7BAtA7gW-7T4RBzCLLKAHX7Z6anFwdlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
سانتی‌آئونا:
محمد صلاح ستاره‌مصری سابق تیم لیورپول برای‌عقدقراردادی یک‌ساله به ارزش 12 میلیون‌یورو بامدیران تیم بشیکتاش به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25938" target="_blank">📅 20:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25936">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYavPhgA88GwSlaqK5KzXZT4UG_bVqnlHRyxfGA68ZtNHo5VOP6fWZ9BBxWgFhV0zF2V_UVl355LzdGSr5ZenA_G8bXVtGeSSbZEQSiarhNXC4VTHNtE0TtW3P6S9U7PnpgzMSjcZ9FoEFTB3aKZZv0T-ZCO34vHKzGV5d7JvF-Jdr0eq_eZsTIhEhrMkoerLDJtcnNXa-ChF_5SK4dmUMX88jJwEln7eCl8QPN_GCFJ4NKa6_fiV-sZtvEscsEJWoNL1zonXcvqbxYObsIA1TpEyV6NukdcVEW1U4W0NvhnLCX1fQ9UcZyflAg2XCMOVvw8U3oaBvFldG9HhxltPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
فدراسیون‌فوتبال‌فرانسه؛ طی ساعات آینده زین الدین زیدان رو به عنوان سرمربی جدید خروس‌ها تا پایان رقابتای جام جهانی 2030 معرفی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25936" target="_blank">📅 19:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25935">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSn6xBSwmd7NSsmuS62zX0wxApxOaBg6IKMLPI8ZbquzI99tRgSrrqUC2lJ8FlE3ocMg_GnAZLnwQIg_9aeRA8zQAJYa-wNOP49rwAaxjyy8OnOD9Vj4PWeAA5upLBQhO-QiuctrUk3fD3L2am3Quh6Yh-AbUWtIVDuvMDtwwHyq9jBcB_0WPxd3WcoULFSgW_Y8qPJsSKim8zimpn3cOXuTaa7ZCpU6_eXW7U12YYcXXin5Xl8GJRqiSo8lr2PC3HtTDf7_g3s8VVlUHoMfQRdErpJsu2fG0ql7a9JaSdI4QPlKs-rM1FvHQCI6MPsOJFl0mhhnjMECQK0DFljt5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسلاوکو وینچیچ همون‌داوریه‌که امسال در بازی رئال - بایرن یه کارت زرد سخت‌ گیرانه به کاماوینگا داد و بعد فهمید کارت زرد دومشه و‌ اخراجش کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25935" target="_blank">📅 19:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25934">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sav_3MvTy_5_69VZnOEOyLHvFX2iC79DSDD_1jF50-AjQgIv3YkMSBo1qNq_E5I0zEDY_7HqNzvgVNggzxzARFKVrXrbCMR0v-aemd5efXTBjfIHY_KGLtvVVGCpY-KesP4IQ1gtQBhF_OwXuYeRkVfHf_NOBIiriE3w2J8M2__dJn69AkTjd-s4G4gqUeaFDx1Hzcr4dxmlv5s_sGdgKicmNf53b0_JEh965GyNyu93SwM15gqkMpMD8vkW-phyDIbnaPEjOUKPpJV6rkqq3FjSY9ujZVW0zmq3MQPCicrIlu8UOvpacGW6F5lppFb2B-fVIyOS9f2VB9PnZKAEoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
7نفر از11بازیکنی که درفینال‌ جام‌‌جهانی 2022 برای آرژانتین از ابتدا بازی کردند در دیدار نیمه‌نهایی جام جهانی با انگلیس هم در ترکیب حضور داشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/25934" target="_blank">📅 19:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25933">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Krvm0fEf6mJb0l_0816_hFgbhwSn15_t1yKfsLtG74TF-EmlqK02ToPEOvSr7cibDR4Mp6haEDBesoMbAzP2wn7JLOa6LtLOAUx0mSnHPqbH2wCChEqbmCAru5vrQeAz5lMV87zwtBsZOkcHakffPqM_9TcnK0evHuLHsdysfA2s6-1SFBOU8kD2viK24GnJYa67ai9Y8XFGJmm5Rl1X1jTJPrku08abRatZSoJoONib3d2GPPnQEnzkZKjWcb39Z1DPO-6rLB15OyHL7lNPvHrE0SJysVsGRBQ1Y8wviQaCxoBwy39VhCyxe3dWazVcOY8czs5TV_iQhvtD3vP01A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌اخرین‌شنیده‌های‌رسانه پرشیانا؛ مهدی تار تار سرمربی جدید تیم پرسپولیس یک فرصت به محمدجواد کاظمیان داده تاشایستگی‌های‌ خود را در تمرینات نشون‌بده در غیر این صورت او نیز همچون شکاری در لیست مازاد سرخ‌ها قرار خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25933" target="_blank">📅 19:06 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
