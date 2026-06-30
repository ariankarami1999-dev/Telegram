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
<img src="https://cdn4.telesco.pe/file/FkoP_aIeIL4_-_inYPZro2KkX3opEAg21gfjMIaaHHMqWBonI0wH0NP7B1zMp9_tXARGNQLpQBLhpn8-vBOAwLZ1aGwwmFjStYdT7Ojt1pJias0tSQmw3qUZHuM6ax2iPaGj01C9cAX-3EdnCWYbkSH3AAoyKdgWRKdxJca61ijaFJtRyCvS83xET_e0hk0Jt_s4HmLIW99JH6RzpIrlJoF5KQM6TdfnzHjoUX5u7GqxpP8_E_ifu9k_w-Zv66zlX49xblAQJnVD_BxIABhHXMaUAvSxqSs77j0CHIjzii52kUIcOBZvE002_HJgdbEh8RIlT-NkM6M5WcmYOWfjEQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 217K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 22:44:58</div>
<hr>

<div class="tg-post" id="msg-67108">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/205ddcc2be.mp4?token=POOQ-JMitB0WQORcxnHRvJIoevGIC58A9lwpzjwBMkck2wfaHOdaJJKblThRT95XbzBnT3lOpGMmKyxVfW8aiVQrPsU-C3shkNrEtQENkGWS1q3VTKy9eEmh1H7tu9TLXtgdvpzvMrf7feE9JskuCSO8cuVczizkZ6xzH9gQ-OuJHQzHUJN0OJft2yqOWQPr17Ji-1CNfIaeJKbgMKTE-ZLHUg9huVSnhHxVV5Shg9SVaggVHVR4bsZ1-6mVUrcN3JDejhM4ownEITFTFDwJ4jn3Q-2AcImMAebonpNlk3wCFrqcVNcs5dWWi_r_j9bZPJxIBW_GL79HyGrOW43o1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/205ddcc2be.mp4?token=POOQ-JMitB0WQORcxnHRvJIoevGIC58A9lwpzjwBMkck2wfaHOdaJJKblThRT95XbzBnT3lOpGMmKyxVfW8aiVQrPsU-C3shkNrEtQENkGWS1q3VTKy9eEmh1H7tu9TLXtgdvpzvMrf7feE9JskuCSO8cuVczizkZ6xzH9gQ-OuJHQzHUJN0OJft2yqOWQPr17Ji-1CNfIaeJKbgMKTE-ZLHUg9huVSnhHxVV5Shg9SVaggVHVR4bsZ1-6mVUrcN3JDejhM4ownEITFTFDwJ4jn3Q-2AcImMAebonpNlk3wCFrqcVNcs5dWWi_r_j9bZPJxIBW_GL79HyGrOW43o1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
اگر نخواهند در گفت‌وگو به تعهدات خود عمل کنند، آماده جنگ هستیم.
🔴
اتفاقات شب‌های اخیر خلیج‌فارس را نقض آتش بس می‌دانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/news_hut/67108" target="_blank">📅 22:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67107">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745f2de194.mp4?token=I2lrf2HwvEO3LL3tH-nqYcVFkWA7maaw5dVxP_6vLeWeXz2rhtrY9IOQ9hYtQ7zGpfjf-7jH7gBL3abENelJrQAxDa3JbzN1axXtxKb2u0tLSigI2crmcQor5uMs4Jm8fQZoKWybUKdq3_CT9HgFmZUxA5N04pJOWkBkWBx1dI4ySt4wDNpeI2NmZ-70Aek7zCDos04lkT9UsgMJxsrvPVN4NjaFNfEsy9y9tu07cw59ghbKnupoJBezZKrPsaKYG_NeMWOFW36BQ_iQucqC7Kpn-kocBc4Ng1ld4xVD3-t2VbkNfPlg1wDZdbni8DlraAmY8frH2yWeM_fVU2HJNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745f2de194.mp4?token=I2lrf2HwvEO3LL3tH-nqYcVFkWA7maaw5dVxP_6vLeWeXz2rhtrY9IOQ9hYtQ7zGpfjf-7jH7gBL3abENelJrQAxDa3JbzN1axXtxKb2u0tLSigI2crmcQor5uMs4Jm8fQZoKWybUKdq3_CT9HgFmZUxA5N04pJOWkBkWBx1dI4ySt4wDNpeI2NmZ-70Aek7zCDos04lkT9UsgMJxsrvPVN4NjaFNfEsy9y9tu07cw59ghbKnupoJBezZKrPsaKYG_NeMWOFW36BQ_iQucqC7Kpn-kocBc4Ng1ld4xVD3-t2VbkNfPlg1wDZdbni8DlraAmY8frH2yWeM_fVU2HJNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
دو اقدامی که پس از امضای تفاهم‌نامه، در شامگاه ۲۴ خرداد رخ داد، اعلام پایان جنگ از سوی نخست‌وزیر پاکستان و توییت ترامپ درباره برداشته شدن محاصره دریایی بود که از اتفاقات مهم تفاهم‌نامه به شمار می‌رود.
ما در حال دنبال کردن دوران گفت‌وگو برای تحقق ماده ۱۳ تفاهم‌نامه هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/news_hut/67107" target="_blank">📅 22:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67105">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gw8No68lp9wWVHExlGYMWIzRJ7U-Pmp38-lKUJagida2Ot8jJwTKr8IuxewJ38ehjCASkJfo1-q0gyKAxZPyXxidUpi-NYUAl1WdT7481L5KW-TYNbEi38kYeSnfgIFu3Bmfa5z29njpCXFRuOMCowInGA5kciSmfZjjfXcGW_LTUIAMGxLy9DweQWwZi6G24eMIX1qPsdCtGTzi2vb6wb2GYCjSvQhmvFqAmMXl-oSJNMDDz1C5XTh6ZNS5-05fdgDsugi1LX843keu64Okc504aMMC7ezFjmkJjhZON0R8zEYmPB_GRzV-o08FzlzuPA0Wkl-XYRk35ZAtKesKzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D4_JVxkOlUfZEp32xhM3-wRs-fAtZ-cUabDYhytdUWY1zIlxzUQadG1CFrt5IzWOfiy9kRkiystB_tAp8mHvUDpP0wQt-DTDypXB7dc3Tc0X1Xl-kUb62Z8pYJHNgfJ6m8mQXT1UA5v-AtZJrqoGfxvhZvWPeEuGqs6BxrxdFv0oWlo5Z7zsQQbVf2X0_267dAKjdy8IicDGqKK4paclgxuT5YAoPhuVKYjNxbcWJ11zsFQYHvuvZhlYcAqtnLUzEf6kW-mjTB2U76ZGWMCd5Bo1H31h-SCDcUBBsyEqSkJNsjjFsF9r6eTdQpNazkjhOxDQXzn-OdgGD6DUTQt3Pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
صفحه اسرائیل به فارسی:
چرا هر کجا این تصاویر به دیوار است، دزدی و فساد هم هست؟
@News_Hut</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/news_hut/67105" target="_blank">📅 22:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67104">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDQsQxCBpCK6B-b4dFVzg2sEdHj7sffq4PtiYSy3y4kNASK_m7_9XPsmQe7whKL5HYbORklMjHJ4u-fHFtysX1SZ7lbLt1a06o5o8cgdAuLtUIrgygNMNSPoV2mSk_Im71_Ymc4UxuPbQiQJ7s_KLrmNpNdCPi70cOcmhETtj_179Ddw2f_4Efh-AbnqYcHNHf1hWEDpHzq7d4gvNypYCUuzjSh-Wsej2sYeyGs6zMqE9_aexDAjGkHRDmnlSdsAroM9EjlCSoQ3VFoCldzqp3dK_QwMw34CJNPd9byekNLsOSrNW2QsyYthq7CPg8PvuTfYaYRVgG04LrhD1s6ylQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وال استریت ژورنال:
اختلاف نظر میان میانه‌روها و تندروهای ایران بر سر اهدافشان در مذاکرات با آمریکا، پیشرفت آنها را کند کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/news_hut/67104" target="_blank">📅 21:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67101">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hn0HRuSnra2IoQNIKzDtnSh3pvSc-yK427wN5uHy9QSzriHWe4tyY-RgIw2RsA2VysVdawrxwvmIbRNN6fLtqGYTs2zP_45jaWD9U0TQodHSlPpiSNPDQBlqAikw0DtLN1Jt5RdWkanYhsVwgY6ZIn98K7D1MiThRxNtsKewO6iljnDr89SlEEuMU42ePkPha8rUYMI18Bj5bJx0Dcu7JHD5XeEPtcj7KTRRPjtzbF2dr2mQ9R18FICTDb0X6iv2y4cBFwxV3W5cIYaPqdttdgqKl4PfmW8OZfFf1tXLff4F81qwY7x-G2frI271NpXCLLD2F3xhwSK_NOiwaQxJ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FE_Q6vbfr0ZwC8vOptYr03-M0qz9SCjp20l7BVespeY5sYbyxOYDKCZG9TRV075kPxl-2Urhmy8bhBJR3PR5kieT2KWj0R7Bf-LD0lrFwm2CjS9cGlFvV-0fJvFax3ED7368UknwXIF_LDvP5Yc-OFTW12uAWTBfko-i6RBBpr_rEYAAPqa1CGmobg2b-5ZY0zYsf26Ii4VMfbUYcV7o3RWZU-6ZNbI5i645GdUcBJmtNfSC2mSUGWnxBYmphhq4PEZcNSlTBiFlV7GpJcTkjx-caT-SUCmSYm9f6J3lk6GknqTyA9xWseayPkwQ5SgpoanxoR8paAECABhQ6qu9ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bzvNKrYOm9f3NbUw7shrZtFR34D5dkYKHM3Mg8gn2k-a2K0lNZLcrjZOx2yNiZXEZWytAsLCSMjZDSn3csK-03mGgvXvTznZyq_HqqC6N7U9FABKxM7slUif0BOJFjtULg73Ns5ODo84tuHOkOa9FZjuJcBYfWrK6jN6xTRxE9c2dnBSbmb_yClG7D-ep-zceVdAAnWx8pP_xKa38kDp61Po_303WLAN9iIiz9-OiUD_3uhqBl_zaasmbJULSOTaL6AKBW-yrn1JbM6n2UovnAKCLbRvhTrQLBSqXLB6bd2K7ukn57RJVAVhalGM-Sr-kymKiF48BmyRF4blLNryeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
سنتکام تصاویری از آموزش شبانه تفنگداران دریایی ایالات متحده در جایی در خاورمیانه منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/news_hut/67101" target="_blank">📅 21:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67100">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d3efb7db7.mp4?token=Jf71KIbGugXtlVk2Y6YKtb5HiveMEM9H7lR_ADYwwW4TIRFbe0V6jZOmhWw4Hb5zbxJH3pXKk-M8TnQ0EZIwUauYka3EmYCJIUfFfZBDYmv_Tv3CJ6Oo35OdoaKOy7ZiYpGHOWJDcUXhJVh4nGR-S_l27QVRlv9fhscPd5K-5aqdzO5CqPVSf_pPqO7yZF-cEr0zqHC6o0WK_Yw9-YFYPOR4uTn31BlzBSVxPSwQaqxUgdnpwmninipI-9-ER26cR2NNOa4S3GtJRSSSZRgKe7X0-nTWWsFwr2hK-S1D0XWy6X1hpYaHomtfFJ12aq3KjZEJxiiYJwVzpT6ZeLlZOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d3efb7db7.mp4?token=Jf71KIbGugXtlVk2Y6YKtb5HiveMEM9H7lR_ADYwwW4TIRFbe0V6jZOmhWw4Hb5zbxJH3pXKk-M8TnQ0EZIwUauYka3EmYCJIUfFfZBDYmv_Tv3CJ6Oo35OdoaKOy7ZiYpGHOWJDcUXhJVh4nGR-S_l27QVRlv9fhscPd5K-5aqdzO5CqPVSf_pPqO7yZF-cEr0zqHC6o0WK_Yw9-YFYPOR4uTn31BlzBSVxPSwQaqxUgdnpwmninipI-9-ER26cR2NNOa4S3GtJRSSSZRgKe7X0-nTWWsFwr2hK-S1D0XWy6X1hpYaHomtfFJ12aq3KjZEJxiiYJwVzpT6ZeLlZOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصاحبه با مدیر داخلی بهشت
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/67100" target="_blank">📅 20:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67099">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c1232f504.mp4?token=OHDGa1HQv6JcSYxWgOuLpI9xGy0FvC4kEOj_xf-lpa2V-IIjbHK1OoEFoV7HSY09IAWYD0rZg3Xk9zdY89RY5b-EiOfEA7nFquSu11DsHcFvF4RWqYUd2MaB4-RAkbGGREjnsizbtysMiA-ntecEQ8Sgd-51TJqgVlCpyCt15W9gO49U0Wj3XLsdameYLsHDvjq3uuqkFZi8Dlza4XXdJjXmCZuZZW7osvRMIxJVM3UTgrbkZ1HZJlpuJJ_JA6Q7hXgJXBoC560Rc6PA1r74UY409ZJXp2k6Mcm11dwXMi22pK5miMYpLq0Y2iCS_KdHWziHG6HzpmqP6rMKQO6uSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c1232f504.mp4?token=OHDGa1HQv6JcSYxWgOuLpI9xGy0FvC4kEOj_xf-lpa2V-IIjbHK1OoEFoV7HSY09IAWYD0rZg3Xk9zdY89RY5b-EiOfEA7nFquSu11DsHcFvF4RWqYUd2MaB4-RAkbGGREjnsizbtysMiA-ntecEQ8Sgd-51TJqgVlCpyCt15W9gO49U0Wj3XLsdameYLsHDvjq3uuqkFZi8Dlza4XXdJjXmCZuZZW7osvRMIxJVM3UTgrbkZ1HZJlpuJJ_JA6Q7hXgJXBoC560Rc6PA1r74UY409ZJXp2k6Mcm11dwXMi22pK5miMYpLq0Y2iCS_KdHWziHG6HzpmqP6rMKQO6uSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏در فضای مجازی این ویدیو به عنوان لحظه‌ی ترور خالد خالدی نیروی جمهوری اسلامی در پاوه منتشر شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/67099" target="_blank">📅 20:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67098">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaoHAWLGnm-SsJHyNFl1K0_Jqc1hb3oHqoJvYY8wF7SmxWVca1Oy9Rayl43kp8q90pJJ0vhJ5C0Uzub6b7-Vy-LlrSONLHf7qWjCWvDkkfwjNlrKdtofdVT9P7Cv2bDaC1F8qJbtt1-RQsk8kiLEYAO6s3C9CNN8AGbhVqA9koxnOFU0MpSAPnTLeMUm07v3kpq3VHTTVhw7se-AEDpc0QK8AqTR8Q1boD6TPbqlhIOzYOEaFB-iFWxrd-I4i-WRoWxt6k_i7CGnsxzisVppDYKcp-7b5klSKGqIfkOcvGPAoC5NJYeaHau3hQWumEpHT4t4zXTWV4dvNuz7i1XPPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
علی حسین قاضی زاده تحلیلگر اینترنشنال:
‏ایران اینترنشنال نسخه‌ای از دستورالعمل محرمانه شورای عالی امنیت ملی را مشاهده کرده است که از مدیران رسانه‌ها می‌خواهد طی ۴۸ ساعت منتهی به آغاز مراسم تشییع جنازه علی خامنه‌ای اخبار مرتبط با مذاکرات و توافق را از اولویت پوشش خارج کنند و بر پوشش مراسم متمرکز شوند.
ساده اینکه از بازماندگان نظام می‌خواهد که چند روز تکه‌تکه‌ کردن یکدیگر برای تصاحب حکومت را رها کنند و به چال کردن رهبر ملعون‌شان مشغول شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/67098" target="_blank">📅 19:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67097">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfG9YDIHFfvl-S_btL325FsNuwgg-TWsCjRt1pjTPW8BqZ_wkhMHgvq6Ga8MkchVsjZGJOM86UK3V5S37ts5wrt5ToRdvuDIyqiwe22MH9R4NhRJ9PekzC10Yg83YO4bv5w2uKb7RhUvggFB2X4xoaDPDx2prqSqhcVAo6AWn0plkxDGnUK6vz2AGP-oLWoT4aRKo4t625QgIUcEkohLjp0FwkhZIYPkrqkx9nNfFfgzts0hOrfEu9-Jj3ZcnbbwRv2gpWiCLiwrN_zthAPCUAKVrX0MTmmozx1NZk070MwMTfgW_tKiliqc16rY7Vzf1i-UmqYeEspgxbb6GYlf-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
ناو آبی خاکی «یو‌اس‌اس باکسر» آمریکا در حال نزدیک شدن به منطقه
🔴
بر اساس گزارش‌های منتشرشده، ناو آبی خاکی «یو‌اس‌اس باکسر» نیروی دریایی آمریکا در حال نزدیک شدن به منطقه خلیج فارس و آب‌های پیرامون رژیم جمهوری اسلامی است. تاکنون مقام‌های آمریکایی جزئیات بیشتری درباره ماموریت یا مقصد نهایی این شناور نظامی منتشر نکرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/67097" target="_blank">📅 19:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67096">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aeafe2956.mp4?token=mMVbJz35GVTuJbx2T3Jj-dPsg3MEwz5fmBpX_Yfms5GoTOE-Z2oABNV2jrH98UiexHHrihBlnxp7TMKihniUOjg9CG3TMCmz5lpsB2deoHA0S2EOwpbh_Opv4l_z5vZ6gEHvi3v4oT2BTe7i9yACoOulaMKeJZoyxKsqJ0PmAF28NpT49xzdJKvO_Vc98ICCFGIKQPr9fMpuotFaVevKL8sgTU0P-AFUAdBtbdXm54Er1syOHXVKuKsdHuOVIEpDfcnZhmQk_HbV-HkPQy7D5BPXaqynsJS4oGt8LMKRnC8ZzcmI2TacOlxodekyiJJXy4E7myNQHRF84eLQdE7O3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aeafe2956.mp4?token=mMVbJz35GVTuJbx2T3Jj-dPsg3MEwz5fmBpX_Yfms5GoTOE-Z2oABNV2jrH98UiexHHrihBlnxp7TMKihniUOjg9CG3TMCmz5lpsB2deoHA0S2EOwpbh_Opv4l_z5vZ6gEHvi3v4oT2BTe7i9yACoOulaMKeJZoyxKsqJ0PmAF28NpT49xzdJKvO_Vc98ICCFGIKQPr9fMpuotFaVevKL8sgTU0P-AFUAdBtbdXm54Er1syOHXVKuKsdHuOVIEpDfcnZhmQk_HbV-HkPQy7D5BPXaqynsJS4oGt8LMKRnC8ZzcmI2TacOlxodekyiJJXy4E7myNQHRF84eLQdE7O3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇺🇸
مارکو روبیو:
تفاوت اصلی این تفاهم‌نامه با برجام اینه که برجام یک توافق واقعی با تعهدات و چارچوب مشخص بود،
اما این یکی عملاً چیزی جز یک کاغذ امضاشده نیست؛
متنی که فقط می‌گه طرفین قرار است درباره ادامه گفت‌وگوها، باز هم گفت‌وگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/67096" target="_blank">📅 18:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67095">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eb209b62d.mp4?token=PEK4GQjUPIcAIxLOhC4kjjCDRkw4GV8H8HuQLWn5s91bA3sRAG5jMgPG0GzFIL6sYilfc5XAdbAH0ytRlNCLkPN7fhAqbXT5B8qG-VWCbPieWdQJqjf8LNqp_fdwApRDK1ZNzfuMykoqcxxgKNi_0c6vPTxvGuU-9wr0dj4KYhpiQoFbF4pkMY-BWpGdClPgoCGMNOgCl-taCZZUIX5KjhXNBDw9mMZ3UTEPK2SMYk-6rQ54Pf5VXOxk_FoN5zwRPUU993SGHhV9IBmUIVQardapJO2M3iOfknSKmYX9QZ7PBZS6-ksUArUhrPH3PLB6_ByjnkFg3hbB8IMYVmndoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eb209b62d.mp4?token=PEK4GQjUPIcAIxLOhC4kjjCDRkw4GV8H8HuQLWn5s91bA3sRAG5jMgPG0GzFIL6sYilfc5XAdbAH0ytRlNCLkPN7fhAqbXT5B8qG-VWCbPieWdQJqjf8LNqp_fdwApRDK1ZNzfuMykoqcxxgKNi_0c6vPTxvGuU-9wr0dj4KYhpiQoFbF4pkMY-BWpGdClPgoCGMNOgCl-taCZZUIX5KjhXNBDw9mMZ3UTEPK2SMYk-6rQ54Pf5VXOxk_FoN5zwRPUU993SGHhV9IBmUIVQardapJO2M3iOfknSKmYX9QZ7PBZS6-ksUArUhrPH3PLB6_ByjnkFg3hbB8IMYVmndoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله پهپادی روسیه در زاپوروژیه اوکراین، صبح امروز
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/67095" target="_blank">📅 18:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67094">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d3e8bdc85.mp4?token=D8a5GLdpUfOkdMG_3FRp7W92p_JRPV7vE23uGUnXcRBazmJzVvEInpitTIm5GFENIRiwBc8FHWEf6-SZnpU7KdqPypscIdqDcQLVudSQzeVrUA5slanDv4rTVyKS_6UVne60cXz_1xMS6iCglUTTGMze_SHeh-fTgGfOAqThpsijvglCh8UPXcwqRi3l5RtADQSrT7watIon-pD9CY39_L7-ClrK4l_RVBpsKTOsBivLy9dnkzL-rwSLHXQ5iDhOzq72hQBPbv0GBs_FcPsZL_AFH7serlPKMkTyWuDws8L5-p2Fa8CMeSQQHw7X6dK5ziWKDNYEPpr5KRRGdg0vOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d3e8bdc85.mp4?token=D8a5GLdpUfOkdMG_3FRp7W92p_JRPV7vE23uGUnXcRBazmJzVvEInpitTIm5GFENIRiwBc8FHWEf6-SZnpU7KdqPypscIdqDcQLVudSQzeVrUA5slanDv4rTVyKS_6UVne60cXz_1xMS6iCglUTTGMze_SHeh-fTgGfOAqThpsijvglCh8UPXcwqRi3l5RtADQSrT7watIon-pD9CY39_L7-ClrK4l_RVBpsKTOsBivLy9dnkzL-rwSLHXQ5iDhOzq72hQBPbv0GBs_FcPsZL_AFH7serlPKMkTyWuDws8L5-p2Fa8CMeSQQHw7X6dK5ziWKDNYEPpr5KRRGdg0vOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
پلیسا شوهر طرفو دستگیر میکنن زنه یهو میرسه به پلیسا میگه وایستید لطفا میخوام باهاش حرف بزنم یهو بعدش...
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/67094" target="_blank">📅 17:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67093">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">⏸
🇺🇸
نوه‌ترامپ رفته کاخ‌سفید گردی و با این ویدیو مکان‌های مختلف استقرار بابا بزرگش رو نشون مردم داده
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/67093" target="_blank">📅 17:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67092">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c791837da.mp4?token=q3m84EgSAQOWHjzxNyGotj8wmkPoIZoaDCgJiP6xa8G48j-urCUIx2njk7pf7FTG1IR--PN8GI4QJy_8PUIlKtEsYI4AH_pzkUzayrLz51D3vhYRnC8JIxGPNRhq4JqEM0q9kSQhx-dRE1XSg6431gyhjTTKckvpMRsNxeAMzsZHZkcmB6zX7GExr6Sp9qPdDw-pSYMKgPI0bdZuAH8pJPsttlDoXZ7caTVfwBb0pHN3oqMsL5ASgsmUAAnD-Q1cAh5rVur0mlk61zfJp55cI3diFfh0YFsaJk0q8cKPdiivG2e9-3ta85OQ-1d30QAgjpDGT09ucQ9ftdlDschKQbcJjTOV_pkhjLPH4uq23erXoRfPK0IgQvfLrxlHFkMxYydxEcEOXwNxUFPR5nOo63_Foy1ZvorcZd6mbnLNe-hEomDbQirjr5wKNuP_mwsmyBO9zsoLXtLohoz5DzKBxNgEueQqGpUfi7n0zu9MeduFELjARiamdhBVFqGr-O3QNNXS6yo5d5G0X7IuX7HH1hTj6MSfSQt5pDDkqSB0fmf_vYJXwofnEKmXUf7szC1Es6gF1IqLD-cTjqp_PYjJEDteW-9dz6OnsTT9uHpeYfBHgaFBDGZUEp9Jgg8qf-G8Rc6KaY-O1fAmi3sKfjQTi5E2MJ4-gVEGVbGZcwiTtbM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c791837da.mp4?token=q3m84EgSAQOWHjzxNyGotj8wmkPoIZoaDCgJiP6xa8G48j-urCUIx2njk7pf7FTG1IR--PN8GI4QJy_8PUIlKtEsYI4AH_pzkUzayrLz51D3vhYRnC8JIxGPNRhq4JqEM0q9kSQhx-dRE1XSg6431gyhjTTKckvpMRsNxeAMzsZHZkcmB6zX7GExr6Sp9qPdDw-pSYMKgPI0bdZuAH8pJPsttlDoXZ7caTVfwBb0pHN3oqMsL5ASgsmUAAnD-Q1cAh5rVur0mlk61zfJp55cI3diFfh0YFsaJk0q8cKPdiivG2e9-3ta85OQ-1d30QAgjpDGT09ucQ9ftdlDschKQbcJjTOV_pkhjLPH4uq23erXoRfPK0IgQvfLrxlHFkMxYydxEcEOXwNxUFPR5nOo63_Foy1ZvorcZd6mbnLNe-hEomDbQirjr5wKNuP_mwsmyBO9zsoLXtLohoz5DzKBxNgEueQqGpUfi7n0zu9MeduFELjARiamdhBVFqGr-O3QNNXS6yo5d5G0X7IuX7HH1hTj6MSfSQt5pDDkqSB0fmf_vYJXwofnEKmXUf7szC1Es6gF1IqLD-cTjqp_PYjJEDteW-9dz6OnsTT9uHpeYfBHgaFBDGZUEp9Jgg8qf-G8Rc6KaY-O1fAmi3sKfjQTi5E2MJ4-gVEGVbGZcwiTtbM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
قمه کشی ارازل اوباش میان مردم در شب عاشورا رودبند دزفول که با دخالت پلیس خاتمه یافت
😐
😂
تاریخ ویدیو 1405/3/4 امامزاده رودبند
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/67092" target="_blank">📅 17:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67091">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d685f955fc.mp4?token=ip_FjGyw30ZZ6dZifOfteYW2x0V3JHSxccnuDy8OXS6SYDMIL1YQw-O71lRipJrzjPLIyEwUD2b6heQNYIRvmaPltKClRDl_8SvIgMDCD8qfxsrLt2fAVGbEJsM5LP5dWt9LTTFMllMWSqe3qI5xVbXORCgZ_gZFMh_OlXnInlzzd_6lQnV6eQ8o5akSRUCQg3fhe8w7rOti3TZHi2BAz_3_8BapWPRA268uQIv9UQtXf_7yNRCvdrn-ULYXWo_AkeYsqIvldTwo3PY4AsK6yLL5LMPsb7VmPqD09Y7RzijCL4y7A8GJPUP5jko24pdiCIiSU6x7AjC6vrVjd2sLQyUnF_GYYc_1DA0awiO9KMdpNqfmGrpNDg7w25Zg29LNl7CqSTJLyB7tS2Ch1FXmMiC4htYKXAqC2reOK5ZiCHc_6MCGmm3bWkfg5Z0H6mEg7jLM3kQMiqN7BqRJrY_dYpGO8t0sd1e9XsWbX_5bSwqQ85buPcN0y9iflmKGDRr5iGI5lcCYmk2CH6gQi-ImftE-bs7MsTPU4P6Ua5PBO1jj4hVWP3o4Ls8cUUyJ6UMnrXIhUs_VVUGIGsMywyqU5aC3hATYbcCtw54fi-_JxRYOJq-V16-9FZ1NhmTaP3wugPTo3DMEdSnx_e7NrU18FTVDrd1yOMGwaw8NSwnoaBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d685f955fc.mp4?token=ip_FjGyw30ZZ6dZifOfteYW2x0V3JHSxccnuDy8OXS6SYDMIL1YQw-O71lRipJrzjPLIyEwUD2b6heQNYIRvmaPltKClRDl_8SvIgMDCD8qfxsrLt2fAVGbEJsM5LP5dWt9LTTFMllMWSqe3qI5xVbXORCgZ_gZFMh_OlXnInlzzd_6lQnV6eQ8o5akSRUCQg3fhe8w7rOti3TZHi2BAz_3_8BapWPRA268uQIv9UQtXf_7yNRCvdrn-ULYXWo_AkeYsqIvldTwo3PY4AsK6yLL5LMPsb7VmPqD09Y7RzijCL4y7A8GJPUP5jko24pdiCIiSU6x7AjC6vrVjd2sLQyUnF_GYYc_1DA0awiO9KMdpNqfmGrpNDg7w25Zg29LNl7CqSTJLyB7tS2Ch1FXmMiC4htYKXAqC2reOK5ZiCHc_6MCGmm3bWkfg5Z0H6mEg7jLM3kQMiqN7BqRJrY_dYpGO8t0sd1e9XsWbX_5bSwqQ85buPcN0y9iflmKGDRr5iGI5lcCYmk2CH6gQi-ImftE-bs7MsTPU4P6Ua5PBO1jj4hVWP3o4Ls8cUUyJ6UMnrXIhUs_VVUGIGsMywyqU5aC3hATYbcCtw54fi-_JxRYOJq-V16-9FZ1NhmTaP3wugPTo3DMEdSnx_e7NrU18FTVDrd1yOMGwaw8NSwnoaBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
😳
عاشورا برا این اراذل هرچه نداشته باشه یه خوبی داره و اونم اینه که تا سال‌ها سوژه میتونن دست مردم برا خنده بدن
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/67091" target="_blank">📅 16:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67090">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a57a9722.mp4?token=Rdbh5jp9WuVybQaKnTOF5dODVUpCntUjztyFQSemHyYcmk39uFcZ5AFDeOmMgrkIdpY1-09g20AtAJvc4o4czFhJvOI1YFoQlQyugCHxSS6pWkDRz9YSLy7nbxNDcs1jOkMsI1Wv3TI94lpZngcfmaGh63CK0hYxbWkRX_6HKDo9z3qMmxo1bh8Eo7iYpeywnJGNyXBg8szvajZjS2UlS9aGsI1xdfIrQAl1DoRR6E3cpCDc_m06t0XCMjqAC6lXQMwcXvIKSVRO1L5s7O1nEytT0WxKyKEC1qIB4sKP8p7ObB3bpoXq1Eq4Mu0s4qYumza0oeYI9J940ngI6DrJeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a57a9722.mp4?token=Rdbh5jp9WuVybQaKnTOF5dODVUpCntUjztyFQSemHyYcmk39uFcZ5AFDeOmMgrkIdpY1-09g20AtAJvc4o4czFhJvOI1YFoQlQyugCHxSS6pWkDRz9YSLy7nbxNDcs1jOkMsI1Wv3TI94lpZngcfmaGh63CK0hYxbWkRX_6HKDo9z3qMmxo1bh8Eo7iYpeywnJGNyXBg8szvajZjS2UlS9aGsI1xdfIrQAl1DoRR6E3cpCDc_m06t0XCMjqAC6lXQMwcXvIKSVRO1L5s7O1nEytT0WxKyKEC1qIB4sKP8p7ObB3bpoXq1Eq4Mu0s4qYumza0oeYI9J940ngI6DrJeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سخنگوی وزارت خارجه: اساساً برنامه‌ای برای دیدار با آمریکایی‌ها در هیچ سطحی نداشته‌ایم که بخواهیم از آن منصرف بشویم
🔴
گفت‌وگوهای دوحه دربارهٔ اجرای بندهایی از یادداشت تفاهم است و با هیئت قطری انجام خواهد شد.
🔴
اجرای بند آزادسازی دارایی‌های ایران در حال انجام است و امیدواریم کار به نتیجهٔ مطلوب برسد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/67090" target="_blank">📅 16:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67089">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dahKW0wXjoBzb7IUGSl6dho8B8EINbXZ5cqTiluKu-RgEMCJgh4OtjX7EZnpfCjLPZVCrZkXjtbu6stT9hk70iQ-tLP07ME7ddplPCgkjCgekGydbLUSNzW2yv-rtRZ5LHPK13z9FwZVVT4XxVolhzWJ7pDct8Vx9IDSFuTiWDFM-e-JKYT1BxuYz0TL10vLyyGsWx76yedFUsmMV8i_IAxDjmykqGRzFUtvaDy_-vabsa6aj-4T0tQpL1pjhdPUo2Tu4cgtloCVDxyPboFHxc1Q7sBq0iyKV3fm-TtMgkZ1DfR0xFsMBofnlvI_e0fg10GcswhJxPg0zm_SZkmhNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه:
مذاکرات غیرمستقیم میان هیئت‌های آمریکا و ایران فردا با حضور میانجی‌ها در قطر برگزار می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/67089" target="_blank">📅 15:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67088">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XhdfZn1vh58UHrLm8lfZkD-_V63xgH9zFbwZcNC0IT3WwiMAY-AIJyX2Y1XjhYJiroY0hzg_ntpHK1FTJtZ91F4TlAV8ZGtTJEfeWRtuEbMKVa3LD_-TUgNWR3ZWb92l583-5eyQiCGxzAgLxhFbXhOD5Eg691yQBOd7PmA1Y0l-iUXJB4UPPVEon3AH83c5Ow9-bejISwD2ksN5yOTc1Y5TLtzt-pbm-xKeZlSm0mucpaAvVC9TuZNeCoyubLxQsEmqCEQqnyGLprpwq1bd_VEINLAhBBqfHL0gcG46ldTmNlkYn4OiptaqRUJ0QuYl-Mk3OBVoJ8x3uu59RG9Uew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه همشهری با این تیتر ترامپ رو تهدید کرد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/67088" target="_blank">📅 15:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67087">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6f84963cf.mp4?token=JDAf80GfVsqBGPCHQvvkoBPMrsQM2vVANTTcl5anBnyar9EW40HPCdd59eg6j7K4QTC3AQ5n5P2RsivFEgr0H5umkNy6TRLekCPfo1N69iB5tTxbwLNCa75W9AD4L__1Lws5_3UBzfnwQlFRJmH4Sx94k_RskQt2uC2709HyKRyEtHQwwRNA0rIas0eiWo9VcSukTP7awb7rnZY2CYWbT9iB8i55lf0YAI6HAOQ4xOKMzkjNECnwjgheQUiLWH-mxm78cftV5px0xCMllBZAOtAlWqKSkf6MYyLMZxt33f0BJhEu-f-8t21zsIE8IaCuqNcPxZ4z9UBdCkQn4TVt1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6f84963cf.mp4?token=JDAf80GfVsqBGPCHQvvkoBPMrsQM2vVANTTcl5anBnyar9EW40HPCdd59eg6j7K4QTC3AQ5n5P2RsivFEgr0H5umkNy6TRLekCPfo1N69iB5tTxbwLNCa75W9AD4L__1Lws5_3UBzfnwQlFRJmH4Sx94k_RskQt2uC2709HyKRyEtHQwwRNA0rIas0eiWo9VcSukTP7awb7rnZY2CYWbT9iB8i55lf0YAI6HAOQ4xOKMzkjNECnwjgheQUiLWH-mxm78cftV5px0xCMllBZAOtAlWqKSkf6MYyLMZxt33f0BJhEu-f-8t21zsIE8IaCuqNcPxZ4z9UBdCkQn4TVt1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
ویدیوهای جدید از زلزله ۷.۸ ریشتری که در ۸ ژوئن ونزوئلا را لرزاند، در ساعات اخیر به سرعت در فضای مجازی پخش شده‌اند و لحظات پرتنشی را که در طول این لرزش قدرتمند تجربه شده است، نشان می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/67087" target="_blank">📅 14:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67083">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P0ogAm1VWZYxX8epuOvnSY3NOWIypcelOK-NJmhP_u0O7bEl7Wm1U5UWx5SnXR18g0jKUJMUu5NakQH8_sX2rVC26crNb3YjCUoqjRPz1QucG0bBSjFBtd5LBQhXUCcxcTTS6Dmt11vUAXY8x9vw9Yon6428QHN7GWsMRfPF8daBseiogJNJ7Q2zet8wReyLNin1-1DIvlayfTlcfZfAGq7ajW6Linn2SoCzPz4EVCTxx8qpBk4hMZbgTClTBJUTrGga3kjKwndpNj8mpFyI7AJbdc3UPjV2vWf1lBLIWYNT1IXVfz8O8rnQcKNGrCeSu8lNt0HqMSzDeTGZ94q-ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PGjz_08JDImxL9NPtQQFdK44ksvR0v-G8W8I86TsP9zqZvNpJ3jYnm9ywi6MyeQQ3wftUjrBwnEaplhHDjDkepmS-SkFDIM8iB0-dZ8lvsVRjH4WNHLLrYWVUVwCwPzQG5A-tNX_UpBv1j76fZ6r2RWiSsG18_X5517l5NQYvDnc7fx9vp2aDgYl6n-Ya94w5BAZA9s68jshdrETwLCU58jAeyxsbL1WwPG67d2URLD-yrw19vM6Ax1jrlXmFoG9JBp4FdCGMKmWGnox1CZDGj7xhT4wFJvrpVfOWDCL2-XEZjNUzkqcN0ufQnCKcuZkge21QyyJz89WkE6vtZfMqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qfPZl_UIVpAaQwEYJwNw6-LzNC7GQT0JpRXMbRyEZl9d0Ivfwvo-iZrT06Cf26w-2eD0Fo1eZJKin2n31DO0jVyGZ3jRf8tk5Y-3d1nG6vy1V7r2udzCEUX_MUDfZoP8tX9Wz0oExpylTN4iB8H2UTNT_lTeFyMOvVQm3LFXmGlksTHyEIzdkFIOA8WRZBFdKaxjJmQm7yBgN6Ej6Ps0I_usympFlihZkS6Hx5UwTQ-U14NgCsygdIhQd83lPUNjalrZdl_fgDgtowD3do-FkKRYvMdcu-CbBsOjj1h2rgSYGguuT1Pxx2qn3dF8PeaP5sJ1QmQ0xRvK9tgPekTrFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iQ33eMYPhGn7V2fuWMMMiNHHEi2Mvf17pCsqmpS-JrVq3YhhP_FnjvMdKncYXdR_79Zh3GMbKxlRbLoDxPuSDsnRQ1ZtNby0gmRQyWNmujc8aOZhZRLWvFrzUkR1IgeKmDKZIIMRIn-mawufUAT-jPsDYIKLkuqfiEqAyX4YSWxKb5--4vihMcCwndeRO84dkfC5oZwatpapIZRmjqHPMgHAnExdJRoGzIN1zzwxTYqi4dQeyG72GTGwtr7KhsvKTlTI7xbOVCYTA7Nf-ewjiEazOTvl4FhvEGXkTfRa2UzFnfZJV0tPDt5G-cAhBaw69Co5tTDu2gGUMs8Hs2hicw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😂
یه پسر 19ساله به اسم آقا سامیار، اومده چندتا عکس از تولد خودش به همراه دوستاش تواینستاگرام پست کرده؛
حالا به دلایلی نامعلوم، این پست تولد آقا سامیار تو اینستاگرام فارسی به شدت وایرال شده و بیش از چندمیلیون بازدید گرفته:
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67083" target="_blank">📅 14:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67082">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
⚠️
قالیباف: سوپرانقلابی هایی که هیچ غلطی برای این انقلاب نکردند، ازهمه طلبکار هستند
این ویدیو از قالیباف مربوط به سال ۱۴۰۱ است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67082" target="_blank">📅 14:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67081">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی وزارت خارجه قطر :
هیئت ایرانی از اومدن به دوحه منصرف شدن و مذاکرات لغو شد.
۶ میلیارد دلار از دارایی‌های مسدود شده ایران هنوز به تهران منتقل نشده است
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/67081" target="_blank">📅 14:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67080">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
‏سخنگوی وزارت خارجه قطر:
جرد کوشنر و استیو ویتکاف، فرستادگان آمریکا، در دوحه حضور دارند
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/67080" target="_blank">📅 14:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67079">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
‏سخنگوی وزارت خارجه قطر:
هیچ نشستی در سطح عالی میان آمریکا و ایران برنامه‌ریزی نشده است
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/67079" target="_blank">📅 14:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67078">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EQOova1yluilZtP9JY-O4NIQ72SJek6f4QopdbXFLcHKl7vTeCNo5R_yKWQHytgGDEPjhnWj3MYlBPcZgyB-J0z6Oto5Yl4IKa0kEnONUkebDfJiPpX1_wipnf_ytad3Swo8RZTAG-NM36QI8NbS1lRu7mNIRPSiA-zw_IJrM8JwAW0UT01BSoaiUMaCt3BMW1fXnhuf25ApzJg5s69yXJsLVlnBUKmRY2Zv69ubnV626UoxCgcO6mL580T5TStS8Egk4CurMnTuW-08vJmIy5HyJh24v3VC-0lt8sHTM-pIeF8u7aY-a9Eph_9Kc3yLluzy6qmWQpUPSKAxcjqzmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افت رتبه همه دانشگاه‌ های ایران در رتبه‌بندی کیواس ۲۰۲۶.
این فقط یک خبر آموزشی نیست؛ گزارشی از هزینه انزوای علمی کشور است.
رشد دانشگاه‌ها را با قطع اینترنت ، فیلترینگ، دیوارکشی دیجیتال و انزوای دانشجویان متوقف کردید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67078" target="_blank">📅 13:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67077">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiGRBBzBK43KX1Ytak6FtAob-trdzuCyUSYJAHYtlsd4UiyqDgresr-9pCRJPVWvqi7nBDUpZQs-s2wyoSCH75Lhnax8pZ841uN8dSVAMG64HlDQ4WTpd_7dJ5ZCx5ZI0uH-lYeq5ifd0tE_fuo8QL589IOVjxbp3qDDpfv3lfkEs7hn2jHj9vRXWYy2ikv1rQW2G50hYPyj27AS3GHv-2q0Za4nzFhfMpl3_rtMfmA0cNAHkSBuJwjOak9kKKo6Vdvhwmt_DOfaKXcMOMdfkjfX9AmoByJJ_iXh7k40I95E0fis7alFRmnTNbi5a7QmPS-6ENJY2OjoGTfTzb3oxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
💢
فرماندهی حمله جهانی نیروی هوایی ایالات متحده برای اولین بار تایید کرد که یک بمب‌افکن پنهان‌کار B-2 یک موشک ضد کشتی برد بلند (LRASM) را بر فراز اقیانوس آرام شلیک کرده است. ادغام جدیدترین موشک ضد کشتی آمریکا در این بمب‌افکن تاکنون برای عموم ناشناخته بوده است.
💢
نیروی هوایی ایالات متحده اکنون توانایی انجام حملات اشباعی ضد کشتی را مستقیماً از قاره اصلی ایالات متحده دارد، در حالی که پروفایل پنهان‌کاری خود را حفظ می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67077" target="_blank">📅 13:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67074">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYwtTzmTHeoj3CtnporjUXqGaD-Mc0TBxB-tnXnA7fKIVHpr17dFGkVTgYGh5R4T3KsJPSSbBuSovkbZkh2xN6nxmvdCbxvfdP4VB2P0ck_ekEzeDt4rYgdQXx9ree_JMZSSiTgJY3NWjtwYSXXTqEPlzppL3UsQFqlrs5Ch0CCdYsZqKNidAhn8_qxDH7uy2jAzaKzasKobxCkxIg_r5oG1rKZWrcb7ZFtkYUTAwpfRpfev-LSY3vnpCoUrWWFhz2nf_mbdDK76dJufuCNbmsTobz2f47r-lqN6H55RYaAdRbd8gZinUm-EDStZrcjGvYj9rhXZTDIxUglaO6Yj4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚠️
🇺🇸
مولین، وزیر امنیت داخلی آمریکا: خیلی خوشحال شدم ایران از جام جهانی حذف شد. انقدر خوشحال شدم که رقصیدم. نصف اعضای تیمشون سپاهی بودن و هربار برای ورود و خروجشون کلی اذیت میشدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67074" target="_blank">📅 12:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67071">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VVRVgKvxcuO3FhcLa8e53Tx5i3-HZbq1D4zLPGYs7Cxdj2tB1gA7rUKNzGXgT6QcoP15C4bj6jj_GT433IacwojSFePg3W9tWlvKAhDRFBmXN640wkwYF0YjcylNkRQ1JEUpMSLC_P7YrXYR8WG8U821wlE0Cni4SO5iEsdPuVMy4lHdkjBPi13ep3k8_qlcCIHJZI-MEPDH_kOBn1V8_x0GHsKYLQUll1ECHMV18eGgBtLbxVbQAut_mnUdt7CLqtt7mio63eYB2O9BWRwbp0LeIgTL7HY9pwKGN934LAGQgnsIPNXjnsRO0060ejPJkYHPtSGNXWvpfoAPMtrvuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/am8X2v6AcCUgJc3dhrHxNT6VowXt7EJuTC0-hsJAjqPu-aPrwXfuo5R0Xf6leXUKynfAW1HFyMhAV1JTbnphDvMkaAVHo8f37usIcguA3oneq4-k00wJ_pnqGHQuUnE_g1BTfd1XrA16zE40masZZfHTPAZp0r4ok9zh1Zl0W1UKehRiAJi6Y9WnMBBDT_ka-_nSeWU5HdU5LxKPjxks7DmT0--0w3Gvtgn9rdnFBA4Uq0zMfEe2Q1ciAj2RSLXmjd1DF2hfXZqc0989_2qkRqTqNosrFbD85imq076dWWcM_gUsvID1nCAePkApwp-oj0RaQ-qlMSrut9leVe_X_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cv2xhAq9NJ2L6IT3fx3HwaVGwFLk_RwfTSd8VtgoUGf_HdfyM4WOBqbm76wDqQjJfpDo4K9bPPzc2Hy2kPx5bidPjvEp-V3fapFvmGKm2xdSIWOraWoShIkU6tOVsd_JpSl-iDqqyXnsmVSFhtac_r1rjnk7g5KqAVMk1spnSSNdJulXpjxF4sd0UBq2AIJ3XcXRyumcYqYIeA9fAeZCwrhoLnsLmhRQV83xOeBV-MdW0SW_6JIkdgD1ABqxNS_cEPzeJ4KEpQb29YXWJLTnecKiXRBzkc4FSOL9u1T3rx2dPE8UXQ8c_eRK9uqVRdoBBkpZZAdnXqx2X38hUBy7JA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
اشتباه نکنید، این زیرزمین خونه والتر وایت نیست، این بخشی از دلارها و طلاهای کشف‌شده در منزل یکی از نمایندگان پارلمان عراقه. حالا شما به این فکر کن توی جمهوری اسلامی از دون‌پایه‌ترین عضو  تا کله‌گنده‌ترین فرد چه اموال و میراثی از مملکت رو چپاول کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67071" target="_blank">📅 11:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67070">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFwPcP-aaPkJEnVcQsRkmpmH_QL4ezE2Fg6BZwZjG9yQuv2UuLZs6eNo9y1YIqKcRO0eOY-m8UCxUDhsaX0pEVhtP12wtOYqEYK74bwE-UZxHp7tiFu5L1aVBY_Y_wG7L1aU6qj0hkN22QMnSnoCpvrDZR3pOsKe1US_Dbx1_sUM2qkqNqCpBY-hF0LecZaFrFvwFpA_-jHzVePy4TAY9EXX3hIwElfLxkpjySnoItQn2haMzb1OxZV3RollFH09aVSn1XxEwRIbzVaMui3NI2Al865-8lcokQ4C-sjsks9n3wSqBojazwwkHUj3CcdiMEIQJoZIZbUSrixSN5-PJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
اموال کشف شده تو خونه یکی از نماینده های مجلس عراق
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67070" target="_blank">📅 10:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67069">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f285f9f0de.mp4?token=Pma0-SnGg0MA7KzQFwvHWmCg1bMWI0NjZHlIqSK0OG6AUuWA3f8eGA4Wau2C3ajsXrT8m4lYKLkAWaSPoudIsCWtWI5CYlbPWPOJdE9GNM01zC-1HiPof-g4b44BCsBfDFLTFkusj0x-BsbsDZCwg8QvAiNsfJeIIfAyPm-ynYul5P2xmA26g97YmrKo2M5DxDvv3f-s5dqOvtfx_DR01KuknTpFNFhzK35kqeJbvg4Jul4Hy2i28sS2IexSy8jRUpnGW-zpia6ESjPPCAMQeXQQ6emwTk1bgxmVUTJraySec6FKQUJDQgi0yXMboEEzEafNF7K7tweYp55B35zvoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f285f9f0de.mp4?token=Pma0-SnGg0MA7KzQFwvHWmCg1bMWI0NjZHlIqSK0OG6AUuWA3f8eGA4Wau2C3ajsXrT8m4lYKLkAWaSPoudIsCWtWI5CYlbPWPOJdE9GNM01zC-1HiPof-g4b44BCsBfDFLTFkusj0x-BsbsDZCwg8QvAiNsfJeIIfAyPm-ynYul5P2xmA26g97YmrKo2M5DxDvv3f-s5dqOvtfx_DR01KuknTpFNFhzK35kqeJbvg4Jul4Hy2i28sS2IexSy8jRUpnGW-zpia6ESjPPCAMQeXQQ6emwTk1bgxmVUTJraySec6FKQUJDQgi0yXMboEEzEafNF7K7tweYp55B35zvoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک مداح:
رو هلیکوپترشون غیرت داشتن بهتون حمله کردن و علی خامنه‌ای رو هنوز دفن نکردید.
۱۰۰ میلیارد دلار پولتون دست اوناست، و میخوان ۶ میلیاردشو بهتون سویا و ذرت بدن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67069" target="_blank">📅 10:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67068">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad39cf71f2.mp4?token=Dilis2ReDz4czNzNk0PoUa6Lu2EvF6_5ZP9AZsxty4CZgElD6RcLFt-S_zvapRt3ITh4XzaG7k2vSeBbmgaS85EhhYszXKp2Z-3SnET3wQPHjha--epNSzjgbDDI-vasPEwWe4x8MUgAJ70NiQRVdmMWzcSKlp_ztslS3LaCSLcjmi1plPzOf7yI0dHEW967KVKsisfc6R6S0zDdBb8K9ewHsnD4cv34Catf_Oe35YsdjZZjQnbrXSfzHZ3aDaBV3txQ6_a33FcPWJtEBw69cbpSbsECQvU9HJUlUTtNkFFZZUWPtGG71Nmw6hz36hiO6tmxVGRud-SLT95Cf4ajtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad39cf71f2.mp4?token=Dilis2ReDz4czNzNk0PoUa6Lu2EvF6_5ZP9AZsxty4CZgElD6RcLFt-S_zvapRt3ITh4XzaG7k2vSeBbmgaS85EhhYszXKp2Z-3SnET3wQPHjha--epNSzjgbDDI-vasPEwWe4x8MUgAJ70NiQRVdmMWzcSKlp_ztslS3LaCSLcjmi1plPzOf7yI0dHEW967KVKsisfc6R6S0zDdBb8K9ewHsnD4cv34Catf_Oe35YsdjZZjQnbrXSfzHZ3aDaBV3txQ6_a33FcPWJtEBw69cbpSbsECQvU9HJUlUTtNkFFZZUWPtGG71Nmw6hz36hiO6tmxVGRud-SLT95Cf4ajtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از سخنگوی‌زن‌قرارگاه خاتم‌الانبیا هم‌رونمایی‌شد
😢
😢
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67068" target="_blank">📅 10:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67067">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=ViMfH6vZicHum5qBRqiWqY-AyEt2udaeqAkVEY63uQ7ai16QaaHdM5W3qO2OnqXarPCLiGVAn1UsZIa5qYAk2tqHjCpzsAgFay3erc4TrClYcXX9alopmNHnQLL0_Um5_WFSKGEF79DcP0dmKIjTlF7YrAZV_GDzA5QXcZpDTPkGhzWKvE2xyKmpdizBApFPnsiBmFmB_iYAVE5EmviJhAr4MiQ0L_vp8KhhyTxcsfkmpWObltswfg9rkvl4A8FXOseCaCFJeGWIhXx21YJrf-YHCB1OIGqcn81Sw3_WosKGyJReMF-JIEE2ukhV-RDqyuscpu6W6fdfVZuQSoknWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=ViMfH6vZicHum5qBRqiWqY-AyEt2udaeqAkVEY63uQ7ai16QaaHdM5W3qO2OnqXarPCLiGVAn1UsZIa5qYAk2tqHjCpzsAgFay3erc4TrClYcXX9alopmNHnQLL0_Um5_WFSKGEF79DcP0dmKIjTlF7YrAZV_GDzA5QXcZpDTPkGhzWKvE2xyKmpdizBApFPnsiBmFmB_iYAVE5EmviJhAr4MiQ0L_vp8KhhyTxcsfkmpWObltswfg9rkvl4A8FXOseCaCFJeGWIhXx21YJrf-YHCB1OIGqcn81Sw3_WosKGyJReMF-JIEE2ukhV-RDqyuscpu6W6fdfVZuQSoknWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس تلویزیون:
جنگ تمام نشده در وقت استراحت بین دو نیمه هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67067" target="_blank">📅 09:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67066">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81a3f09336.mp4?token=M5voTNuoh3GjCMxvu_2vQhVP29BhuhMA3Z0KY6xYVFnJmylid4r-onjP8PgOi2AHwwdq-j1F2CwK5Br0ncY9fQLqaiSEcOOcqHHFGLZdYv-tVvSUXKUVv67kPlYKKR25ZHICWHqlMBVn5hZdwVCC25h-IX2s7H3UmvPtu5ffjwE5-iUM2R4PtaRnGnPPfplmkclcMtXX8Q-VNLCyWWWQ80qN-aQ2x0EdHhC_tcnEhxytWm9u6rol_UYV1yNQwcbGOl-ZHxkWqZ-X5DOK7azOR2iW2OBp-0VfuFC38SsPEhTu0H0OxJOR-BeQ31BCb4tPnG1VOtoJ7WMAwbu17mn8aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81a3f09336.mp4?token=M5voTNuoh3GjCMxvu_2vQhVP29BhuhMA3Z0KY6xYVFnJmylid4r-onjP8PgOi2AHwwdq-j1F2CwK5Br0ncY9fQLqaiSEcOOcqHHFGLZdYv-tVvSUXKUVv67kPlYKKR25ZHICWHqlMBVn5hZdwVCC25h-IX2s7H3UmvPtu5ffjwE5-iUM2R4PtaRnGnPPfplmkclcMtXX8Q-VNLCyWWWQ80qN-aQ2x0EdHhC_tcnEhxytWm9u6rol_UYV1yNQwcbGOl-ZHxkWqZ-X5DOK7azOR2iW2OBp-0VfuFC38SsPEhTu0H0OxJOR-BeQ31BCb4tPnG1VOtoJ7WMAwbu17mn8aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسعود پزشکیان در جریان مناظره‌های انتخابات ریاست‌جمهوری ۱۴۰۳ با مقایسه وضعیت امروز و دوران قبل از انقلاب گفت:
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67066" target="_blank">📅 09:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67065">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67065" target="_blank">📅 03:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67064">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cv2O7ECPlL3NYo_FeVb7SJtLdLGlsOvGIsy_92QSF2U35lyccKguKisr2z_dqEgux8xtWuyY1hyzKgVHDkwqt7BFTbwDYr-rvZPDuzo2yaqcrkzN1mUiitTD25SrnpWBa22WvFEGRliiFU7h76Ur6IEl-CzsSBZZOr0RBlPQIngWwgKtFMgACPTdMjNrobZQQ8TeCqfD2_m-LQntZwC1XWeMt2haqjgsqBmRtpiREe5MmBe7uF9ggzcFvu8mEdpmL_jcRg93X_HJxdB7gDuCIceLnvBbku15gu3NBGzXZyUD18iQ0y9H3Z2QZc-uGN6xIG-Quq9mdPmfSx1peJE64Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67064" target="_blank">📅 03:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67063">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
یسرائیل کاتز، وزیر جنگ اسرائیل:
احتمال دارد جنگ مجدد با ایران طی دو روز رخ دهد.
وی اعلام کرد که نیروهای دفاعی اسرائیل آماده عملیات و هدف قراردادن ایران در صورت استفاده ایران از موشک‌های بالستیک خود در راستای دفاع از لبنان هستند.
او از آماده‌باش کامل نیروهای اسرائیل خبر داد  اما خاطرنشان کرد در مذاکره و اقدامات آمریکا در راستای ایرانی‌ها دخالت نخواهند کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67063" target="_blank">📅 02:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67061">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e68HHlxxFHrA74y2HVwQPvt5sHA4LXpZx68W1ViCgTuXjd60QyiUP-vjzjhsUIIX05u_UEziSy2S-fNFainNnMlqe5tUF3mYx6j0xd-Od-djWryOBratvNTz7DpyJoZUKLCUb24yuKOZ9bwOjdSpNBR5cB5yPbdgQ3gryFcxTMuwaSncOO9kkmdReyVeIH9aqtdbf_GPrt32Itp4zVo-2YrN3ZoeElatJ4-RZiP8KhsytbdjeGlSCfOAoYCAyj15I28GuZhNHlSNwGm7TT4qAfw013BjMwncuDR3SDneD9krGipAZv4f8imP_sYKGA7JtA3Qyy39DETFS12Iij-wsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تصویری از بیمارستان پاوه و هجوم خانواده های نیرو های امنیتی به این بیمارستان،به نظر تلفات و زخمی ها بالاست.
«کشته شدن سه پاسدار تا کنون تایید شده است.
سیروس درویشی،خالد خالدی،برهان کریسانی»
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67061" target="_blank">📅 01:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67060">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
گزارش‌ها از درگیری و حادثه امنیتی بین نیروهای کرد و نیروهای نظامی در شهر پاوه ارسال شده
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67060" target="_blank">📅 01:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67059">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uByUD_dVyCZrmFc1jPH92id4BNWqgu_WQ6J1AHJuZRvJebnGzYOB3ArAo9TkdT3KE-Y-KYQoj05SoPPaUEa5Wj1fvz9BfUObffn4x4GcaooKTyFejcfSYMbwn3yHpbp41L8mcq8tHyowCrem1j-25kGRiCAYI3vbufUw2DUkTUtmcLFM0Ke_kGgr7FYQxYO1u_eLCpxLE-p-xltYqM7w2qzB5A-MgnbWPGOaWRH0Rb_FELdkKXtZb3tNtqGLnZChgUdj-e8RlkdNYSeYeDErbARpwhrv2yymuQRnWvLvOpH_wUglwkahGHvvDp6tBHzCeMXxPUiM2gs01Vv55oxdUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
تفاهم امری طرفینی است. اگر طرف آمریکایی به تفاهم نامه پایبند باشد ما هم به تعهداتمان عمل می‌کنیم.
رویکرد ما در مقابل رجزخوانی‌های نامعقول و تهدیدهای بی‌پشتوانه، تکیه بر عقلانیت و کرامت انسانی در تصمیم‌گیری‌ها و دفاع قاطع و بی‌پروا به هنگام عمل است.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67059" target="_blank">📅 01:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67058">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
این نشست در دوحه شاید مهم باشد، شاید هم نه.
خواهیم دید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67058" target="_blank">📅 01:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67057">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15a452960e.mp4?token=FXhn0qocL8UuTQR-H74SmGaeExiYhdRyuR3lYJncGVNtqJatRxPswT3swJFcQrEcOXotazDULmcQIF-urrrIe4dTnaJAIJ1KWkxN0TfUcGS33BnoOSPr0LQA0dMaqM1YM6bVJTAENBvAA9C0vbvRqPH0tk0d4fIcBK9iDaW5aQGYKjij0zsw5KpKT-kl3FSZVIOJj72_P3wFKpX0Wu6RVFb_7kULBPFcbmvTLt-_JERo6qrD74FqV4the8TXMcqaChserVLu13dLcKzWXIJJEPOFezLiVQjh74P7RieEwfLrQgoDLZjcK2WqwQ-sCXHkefqQTMCc-ARf06J-HgXRBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15a452960e.mp4?token=FXhn0qocL8UuTQR-H74SmGaeExiYhdRyuR3lYJncGVNtqJatRxPswT3swJFcQrEcOXotazDULmcQIF-urrrIe4dTnaJAIJ1KWkxN0TfUcGS33BnoOSPr0LQA0dMaqM1YM6bVJTAENBvAA9C0vbvRqPH0tk0d4fIcBK9iDaW5aQGYKjij0zsw5KpKT-kl3FSZVIOJj72_P3wFKpX0Wu6RVFb_7kULBPFcbmvTLt-_JERo6qrD74FqV4the8TXMcqaChserVLu13dLcKzWXIJJEPOFezLiVQjh74P7RieEwfLrQgoDLZjcK2WqwQ-sCXHkefqQTMCc-ARf06J-HgXRBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ درباره کمونیسم:
این سوسیالیسم نیست؛ در واقع کمونیسم است. آن‌ها از واژه “سوسیال دموکرات” استفاده می‌کنند چون خیلی خوش‌آهنگ به نظر می‌رسد، اما در واقع درباره کمونیسم صحبت می‌کنید.
من فکر می‌کنم این بزرگ‌ترین تهدید برای کشور ماست، شاید از زمان تأسیس آن. این شامل جنگ جهانی اول، جنگ جهانی دوم، حملات ۱۱ سپتامبر و حمله پرل هاربر هم می‌شود.
من فکر می‌کنم این بزرگ‌ترین تهدید برای کشور ماست. بعضی‌ها وقتی این را می‌گویم می‌خندند، اما افراد آگاه خواهند گفت: “می‌دانید، احتمالاً حق با اوست.”
این در واقع وارد کردن کمونیسم به ایالات متحده آمریکا است. هیچ‌چیز تا این حد خطرناک نبوده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67057" target="_blank">📅 01:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67056">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMiP1N80fctsGHrCpoxI2eYuqXXKdkJzjKOw-r9prKLO59EdTk7RiG9IObiSkCS_j-2w2Ba8P1dnGspf-2F6bCLtmZxe1qIre9DlMzRT-MNLhxKfFSQUX5SU2byi62SxRZsiyurh7hrY06ZnEeAN8ESx7RKrLUJ4YjgwZSXvXJuaKXDt0esHtVXZN_CeMzoapojfRL6g6KoT5fzdQshmFdSRdDViQtSbpPZcMSlL0-I_ILkqNqN1CHnKUm4pFb32QL11Mw1xH9fB2pzo04-d-Qi5i8kpw_Rm7AhoMWRcejJ5ruSLxty-oEs03ba5P7-8g8j-AOhULrT-Hlw4Zxd0Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67056" target="_blank">📅 01:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67055">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c7afb034.mp4?token=XsLakP1Z629WpDYEjJGO7VmsQTXxY19aaS9KFdHYAe5rGkoXUdD6bzB3R6TAZ1hjscQi_GBc8egpIjBAXXNrvRPRfLYppZLXXtYw26htYiG19LsXH60w3ShGOxIi7aE3RqX5ZhptiiZa1EMEabSdZR_0bFCbRW2y3mT1DGM4DXFIDJGYSl9ZF7EurjfLeVy4cgj7-J6-K4uhvSA9ToPdT5ENnn6ZxhdutpGYVzQSQvtZGl6_lbHl75pXm18alUsWFYZ3xmdTQyqWtTIjSeGOUJP_T-uxjr02jM8iSnpkH0MliNijlNmm72LlHf3Z-5HTtvC2UfKPvxnxLjFisdHkKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c7afb034.mp4?token=XsLakP1Z629WpDYEjJGO7VmsQTXxY19aaS9KFdHYAe5rGkoXUdD6bzB3R6TAZ1hjscQi_GBc8egpIjBAXXNrvRPRfLYppZLXXtYw26htYiG19LsXH60w3ShGOxIi7aE3RqX5ZhptiiZa1EMEabSdZR_0bFCbRW2y3mT1DGM4DXFIDJGYSl9ZF7EurjfLeVy4cgj7-J6-K4uhvSA9ToPdT5ENnn6ZxhdutpGYVzQSQvtZGl6_lbHl75pXm18alUsWFYZ3xmdTQyqWtTIjSeGOUJP_T-uxjr02jM8iSnpkH0MliNijlNmm72LlHf3Z-5HTtvC2UfKPvxnxLjFisdHkKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67055" target="_blank">📅 00:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67054">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1336110317.mp4?token=iU7yHWIamzzau9zaoxCoYaam-FVrx6arE623sel49MLEgIv1TMriU7MXEBRLZyTMTmD8oR28GdVqcpQki3AQ33X2C6F2Pc8xLLacS3rTUJ7Hak3N7GiaTyhotmDvU-tPvclrjvvZ6gk1VJc_0ptIrEtOzSsXxVeW2AMaNDBnahpXMWIZbk9CcalCTD6BcMK45ZsKGM5J6g2zc6flKNR6gv7FqufXN1NqUoHqjVd_Aw9rHNGVuXtGQHB4GabQRvcu09Fl4YPHcUL_X5PrNJje_4HL31MmVdZd_BdF7JkGwylL53VmAre9x1vpu2TjIhqL16WjqshjL6CXc6swpcr3Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1336110317.mp4?token=iU7yHWIamzzau9zaoxCoYaam-FVrx6arE623sel49MLEgIv1TMriU7MXEBRLZyTMTmD8oR28GdVqcpQki3AQ33X2C6F2Pc8xLLacS3rTUJ7Hak3N7GiaTyhotmDvU-tPvclrjvvZ6gk1VJc_0ptIrEtOzSsXxVeW2AMaNDBnahpXMWIZbk9CcalCTD6BcMK45ZsKGM5J6g2zc6flKNR6gv7FqufXN1NqUoHqjVd_Aw9rHNGVuXtGQHB4GabQRvcu09Fl4YPHcUL_X5PrNJje_4HL31MmVdZd_BdF7JkGwylL53VmAre9x1vpu2TjIhqL16WjqshjL6CXc6swpcr3Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دادگاه محاکمه ترامپ و نتانیاهو
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67054" target="_blank">📅 23:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67053">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e959102c72.mp4?token=HJnzMG1fN97fhP13eN7cef6Je5Yqv7Dzs-NFW_BreZTFHlUxxocGqLwn73y3Oyg76FpwdFDzNmB4wA0KEY3CVb9QR36ZTjMxEC0vmYoW3qxqX6ZT_pHLtLrQFnSaAMxArppesIXUyOuCMU-dF3Qp9fjnOXXcrYuOu6nBQEn8-szOPGXf68cUUwrrsH5BZWodjzsTfjbNaepxPR4zFvnDS4sqvZnL2B6fmAkyW4wpWRGGTrTYXKKOGE6iSQV-iFI1DioxNSuZVdcyPM_bc0hZS-JZVr-8qil9DaNhchlXY5NcM8LU5kpg1gjXR9WfY3m2FtUeH12IvehgD5cVDchB0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e959102c72.mp4?token=HJnzMG1fN97fhP13eN7cef6Je5Yqv7Dzs-NFW_BreZTFHlUxxocGqLwn73y3Oyg76FpwdFDzNmB4wA0KEY3CVb9QR36ZTjMxEC0vmYoW3qxqX6ZT_pHLtLrQFnSaAMxArppesIXUyOuCMU-dF3Qp9fjnOXXcrYuOu6nBQEn8-szOPGXf68cUUwrrsH5BZWodjzsTfjbNaepxPR4zFvnDS4sqvZnL2B6fmAkyW4wpWRGGTrTYXKKOGE6iSQV-iFI1DioxNSuZVdcyPM_bc0hZS-JZVr-8qil9DaNhchlXY5NcM8LU5kpg1gjXR9WfY3m2FtUeH12IvehgD5cVDchB0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
عزاداری پدر جاوید‌نام داوود عباسی بر سر مزار فرزندش.
جاوید‌نام داوود عباسی یکی دیگر از کشته شدگان اعتراضات ۱۸و۱۹ دی ماه ۱۴۰۴ ایران بود.
داوود عباسی روحت شاد
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67053" target="_blank">📅 23:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67052">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWagIwpKtv0H--moLBmfeW3Ld5jcdnR074UAHczVyJTuNt1VTbFesXPxQCWE4eKHJXziHqbPRlBSQUFAHjVeHh-g2nODJSsEKYrooIrTMGWSczDJcVKpBCVNUUoL09PYqg9vekAWUaisTKzFtGBbyhp_YJ7Hq9qMr5xeBwPiMzU-OfyG6deIa4uOBKbnLRTBQW9gggasJkztWhAIrUUg7hYKhamnUP4rfJjrqXiqfeJkjHAQ039plYlqsWPWrrCeUGcgCKwdpR5cGvBHMq_EVjP7qwyuWTtKpLmxYR-XiaY8r_JkUMLKsjwFGXTBKA_QohOKtAl1h-Vb-ogiJskFbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری فارس
:
معاون سیاسی نیروی دریایی سپاه طی سانحه کشته شد
.
دریادار دوم محمد اکبرزاده، معاون سیاسی دفتر نمایندگی ولی فقیه در نیروی دریایی سپاه، ساعاتی پیش در یک سانحۀ رانندگی بر اثر واژگونی خودرو در یکی از جاده‌های استان کرمان کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67052" target="_blank">📅 22:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67051">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‼️
اسماعیل بقائی: هیئت کارشناسی ایران برای پیگیری اجرای تفاهمات عازم دوحه می‌شود.
​
🔴
بقائی در پاسخ به سوالی راجع به وضعیت اجرای بندهای مختلف یادداشت تفاهم از جمله در رابطه با موضوع فروش نفت و دسترسی آزاد به دارائی‌های مسدودشده ایران گفت: در رابطه با تعهد آمریکا طبق بند ۱۰ (فروش نفت) مجوزهای لازم از سوی آمریکا صادر شده و پیگیر روند اجرای آن هستیم. در رابطه با بند ۱۱ (آزادشدن دارایی‌های مسدودشده ایران) نیز فرآیند اجرایی شدن آن در حال پیگیری است. در این چارچوب، همین هفته هیاتی کارشناسی از جمهوری اسلامی ایران به دوحه اعزام می‌شود.
​
🔴
بقائی در پاسخ به سوالی راجع به شروع مذاکرات برای توافق نهایی در چارچوب گروه‌های کاری تعیین شده، گفت: هنوز وارد مرحله مذاکره برای توافق نهایی نشده‌ایم؛ طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات توافق نهایی، منوط به شروع اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ و تداوم اجرای آنها است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67051" target="_blank">📅 21:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67050">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‼️
بقائی سخنگوی وزارت خارجه: هیچ‌گونه مذاکره‌ای با طرف آمریکایی طی روزهای آینده در دستور کار نیست
🔴
طی روزهای آتی هیچ نشست مذاکراتی در هیچ سطحی با طرف آمریکایی نداریم و اینکه نمایندگان آمریکا به قطر سفر می‌کنند، ارتباطی با سفر هیات ایرانی که برای پیگیری اجرای مفاد یادداشت تفاهم از جمله بند ۱۱ انجام می‌شود ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67050" target="_blank">📅 21:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67049">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5249169d4b.mp4?token=IqUxTD9MT7jYXbZAHRZStWnRKC7enXZsEfV6qGfAdiUMeUMhL0AycXQaG4-6IrT24c_wHE-ujXk2jz2zSJByVfcAOdHcCxA70oqM63jbdtl6wSCz2SfZAhst9k6O5SvNup3j1scqGdUYqK0JDY8f2HeTcRY9jV6zYDuRsugdiEepHh84VUTHi5iVaV0xOeY7FmXmGIeGf_w9XHKYPB9uOX730zCq1xBXwRmOulMQPiPeQGOT7uHjgXTLF6TTBhWTG3c6QD--mVNlJA327GWeMoIGANEM1c2hG2TOEeVv33XVlOwH0AdN7FztJ6vFVOcSokguX6Bk6LfSuThjSWAH2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5249169d4b.mp4?token=IqUxTD9MT7jYXbZAHRZStWnRKC7enXZsEfV6qGfAdiUMeUMhL0AycXQaG4-6IrT24c_wHE-ujXk2jz2zSJByVfcAOdHcCxA70oqM63jbdtl6wSCz2SfZAhst9k6O5SvNup3j1scqGdUYqK0JDY8f2HeTcRY9jV6zYDuRsugdiEepHh84VUTHi5iVaV0xOeY7FmXmGIeGf_w9XHKYPB9uOX730zCq1xBXwRmOulMQPiPeQGOT7uHjgXTLF6TTBhWTG3c6QD--mVNlJA327GWeMoIGANEM1c2hG2TOEeVv33XVlOwH0AdN7FztJ6vFVOcSokguX6Bk6LfSuThjSWAH2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ناو آبراهام لینکن امریکا توسط سپاه غرق شد
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67049" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67048">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15026d52cf.mp4?token=dLu2Nwnq9w8qZHtcrDfccQxzogXHiNCD5NDvSixZCGBOZQY5aaHSrfmUbUoP8sNIr-Xhby8sNWI1D_BPTFNsqZV_PAMAKavfwKIC4l2eeRIJ-QJI30Clih0nbSZhh8Odthyo7Wb5pDuwN9NmftS8sjo7PYU5nr9AhQQxns_8ViH1_xFC1Be-YgJGbT1id_Lg4X-nnILwokKRkHyEroIH-_uIaLlffjy8QCKX6ZCIkFUwjQfwOHqwxIGEo2W8TXi8exqnYRef-LTY4VcH8UiA4yqLRzVk3cZz1dKxM21CBxfdWqusyEPVtOTn_U31PrniD9vKRVTo6XN3V6cCO1o-kKSmUdYPdLJmhKS1xeB83hGPB9MJuVRoFu7TfhdojnwWVO05Zhn2_jv6J9qsEXbTEtZ09NXZnOHT_iKK6JpTVVKeRXGh44XN8YY1EMzOGtb3T0ngq2rVnBip1GZ7x87abbjYbKubLMqE-deb3iqJXG2Trg8f5KM7Co7AT8YSkKnOzQnyBIu4skO6wAYReEiSYZyQoJ5YmTozv2J1Bpt8goDYwA4Ezp0q1H9ew5HyflwOClCEfXEfpLrHqLiEocwAXR2gT7rWd0ip2_D0rdOASFs8u8C-jaWKsmxlaS0yx6DRZNDg6FwKOSMy2rQGgO4pELKh4Ffva-596yGEfwKH8Us" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15026d52cf.mp4?token=dLu2Nwnq9w8qZHtcrDfccQxzogXHiNCD5NDvSixZCGBOZQY5aaHSrfmUbUoP8sNIr-Xhby8sNWI1D_BPTFNsqZV_PAMAKavfwKIC4l2eeRIJ-QJI30Clih0nbSZhh8Odthyo7Wb5pDuwN9NmftS8sjo7PYU5nr9AhQQxns_8ViH1_xFC1Be-YgJGbT1id_Lg4X-nnILwokKRkHyEroIH-_uIaLlffjy8QCKX6ZCIkFUwjQfwOHqwxIGEo2W8TXi8exqnYRef-LTY4VcH8UiA4yqLRzVk3cZz1dKxM21CBxfdWqusyEPVtOTn_U31PrniD9vKRVTo6XN3V6cCO1o-kKSmUdYPdLJmhKS1xeB83hGPB9MJuVRoFu7TfhdojnwWVO05Zhn2_jv6J9qsEXbTEtZ09NXZnOHT_iKK6JpTVVKeRXGh44XN8YY1EMzOGtb3T0ngq2rVnBip1GZ7x87abbjYbKubLMqE-deb3iqJXG2Trg8f5KM7Co7AT8YSkKnOzQnyBIu4skO6wAYReEiSYZyQoJ5YmTozv2J1Bpt8goDYwA4Ezp0q1H9ew5HyflwOClCEfXEfpLrHqLiEocwAXR2gT7rWd0ip2_D0rdOASFs8u8C-jaWKsmxlaS0yx6DRZNDg6FwKOSMy2rQGgO4pELKh4Ffva-596yGEfwKH8Us" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی کارشناس برنامه خط انرژی به غیرقابل شکست بودن ناوهای آمریکایی اعتراف میکند:
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67048" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67047">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rwuy2mPniU66y3uhrzz-XsRBcZQ1gbfdwl4_dNfhXA_8AqP8wNeA6x2KhK2I9EuamlnB01S7kDD1YtSY5O_sz8yqzcf9C0t6SQtVyanN9I9ashIMCbeEzDgF2docXeSyP1edVJU_JxcKANCbhdsJ71JF5b4rS4xZJvJG-RO-IuEh8mBk_jDgdIxlNTMC05X_YxWupoCaW6CY5KzuxRT7koS-2nqPscW6jg2mZVV2BhBMxtpgTr6twncGunKEth3j3hPJCxk4aoHZZkkjwPyaJKowxg6MJwbgpVv5wofQrODd1EbZzmrj6-H5rVSRhMUdMyC7vA3Rd3wmY6CKhk0R4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
رفقا
توجه توجه
✅
درآمد تضمینی روزانه 35 میلیون در منزل
🌟
تمامی ضرر هایی که این چند وقت بخاطر جنگ دادی  رو جبران کن
✔️
🚨
⚡
⚡
⚡
⚡
⚡
⚡
https://t.me/+ArmBt6ZWMF84ZDlk
https://t.me/+ArmBt6ZWMF84ZDlk</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67047" target="_blank">📅 20:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67046">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
نیویورک پست به نقل از یک مقام آمریکایی:
ما به ایران روشن کردیم که تا زمانی که پیشرفتی در پرونده هسته‌ای حاصل نشود، دارایی‌های مسدود شده این کشور را آزاد نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67046" target="_blank">📅 20:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67045">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a60a7af63.mp4?token=IFmjjJTrSbuJvA8_tXEZgaLCMgcB69dyzY4hypFIbfdIJbO0a6QGKiQhBe0OlyUy2hv6lzXgWV8NlPOU_CnC-LY67Dx9edVwit9OkDFSzYpBWuZ960P1bi8kJ2j6Xl8rub5ThvYCHSUwsaCS5PhlwtpH3REchTRSj8wNYAXQtmlb6O8MZXxnkydetpaGDV5Zu0e2TRWA3GEurVTxxo1Z5L83SgQSweVlcVh0c-EmF-utEHlL_7a2ECMStmLUsUFgojAqPbG5P8w_kIuHeu-XEj8sfaxm3YUWUgJ1rx5lSPzq3hetlJSnp5eqAhakf0y9U3hf8P6TwjWB3COZ_rP95A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a60a7af63.mp4?token=IFmjjJTrSbuJvA8_tXEZgaLCMgcB69dyzY4hypFIbfdIJbO0a6QGKiQhBe0OlyUy2hv6lzXgWV8NlPOU_CnC-LY67Dx9edVwit9OkDFSzYpBWuZ960P1bi8kJ2j6Xl8rub5ThvYCHSUwsaCS5PhlwtpH3REchTRSj8wNYAXQtmlb6O8MZXxnkydetpaGDV5Zu0e2TRWA3GEurVTxxo1Z5L83SgQSweVlcVh0c-EmF-utEHlL_7a2ECMStmLUsUFgojAqPbG5P8w_kIuHeu-XEj8sfaxm3YUWUgJ1rx5lSPzq3hetlJSnp5eqAhakf0y9U3hf8P6TwjWB3COZ_rP95A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان این تحلیل رو سال ۱۳۹۸ مطرح کرده بود؛ تحلیلی که از سال‌ها مطالعه و شناختش از روابط بین‌الملل میومد. حالا بعد از گذشت حدود ۷ سال،
با دیدن اتفاقات امروز حرف‌هایی که اون زمان میزد، داره عیناً جلوی چشممون اتفاق میفته.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67045" target="_blank">📅 20:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67044">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdI9ZfyzVWZvJGiQ6lzh3amtnfkG__F8j6RWdIakk8QNt33Td5vgm6gDDV81Vly20LboOo3qknoTIqkqS6dJDCu5LKu2FvvC-9b6SGVVHPuz6zCDYRlZTPMJA48bmBPL2h1LnFb7N_Hw4oKSQ1sWaKJqQXSTRRqPE9z1yIBCpVrBhe0Na1oUZ1T1SAQbGd1msxWMc7vq4OqMzhJbfzxEqri6J51mZfOOEbeqoM47eLtr0H6RbEzSfpYZHytXWkWRDTHKvglDm_G9At_baJsyqlXKdE6z0OqEZfmLcb9lVgD0Eeew-Pd6beU_ZzpwlCkaNlEp630Caa1yNcBdFmgxaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
حمله ارتش اسرائیل به دیر میماس در استان نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67044" target="_blank">📅 19:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67043">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🇮🇱
یسرائیل کاتز:
اگر ترامپ تصمیم بگیرد که مذاکرات به نتیجه نرسیده است یا اگر ایران به اسرائیل حمله کند، جنگ با ایران می‌تواند دوباره آغاز شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67043" target="_blank">📅 19:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67042">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea6a79f9a8.mp4?token=dNXrrS2jhAh73F2I6h9Ute9rI-O_tAKoM4QsrUUtwrMhYvIvTlni8Hu-5NCkW5wnRkKfG8kgcLXykm7CbeP294DXfTnR8ytyooMg2Dx2VKELlrBpkqrlzD8d5XWfXwh6TIiYfk1_F1eRHY9TUv_wDZW7BVjEdpTAU00ByuK2Pqzem2UDDDoGhBEnCLdPkR6BIFQDkqvKBGyd5E2pEC09uoGZIk41Lhy7bIx_fJJChQxF3wlK6LhlVIwAuLgrTYkche2ebYakKeAmCQIbRXOJ_AUGGXy9Tg4gE49neCjCEjorfUaSTVMspwgnnPJj87KNqBSHgmRYhxHJQVlKCYfEAYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea6a79f9a8.mp4?token=dNXrrS2jhAh73F2I6h9Ute9rI-O_tAKoM4QsrUUtwrMhYvIvTlni8Hu-5NCkW5wnRkKfG8kgcLXykm7CbeP294DXfTnR8ytyooMg2Dx2VKELlrBpkqrlzD8d5XWfXwh6TIiYfk1_F1eRHY9TUv_wDZW7BVjEdpTAU00ByuK2Pqzem2UDDDoGhBEnCLdPkR6BIFQDkqvKBGyd5E2pEC09uoGZIk41Lhy7bIx_fJJChQxF3wlK6LhlVIwAuLgrTYkche2ebYakKeAmCQIbRXOJ_AUGGXy9Tg4gE49neCjCEjorfUaSTVMspwgnnPJj87KNqBSHgmRYhxHJQVlKCYfEAYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تردد در تنگه هرمز در دو روز اخیر
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67042" target="_blank">📅 19:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67041">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9b7cb450.mp4?token=NzD_4v5d5J9Zxjm9pOmulzx-WgCSugnieCp55RyidTQnZpvv8-33WpfjvR8EyanH0C2Di2x0jqUiQkelMJErB2Hl6wA4hjywW-0GcNSWqOgY5FY7G_U3CTU9KdN3LVBm565N-ij_TR4E74UuwDIn4k6JcIoii4WNlEVWUkkKub7UnsZ1lITZIC7ZjlRshavw1pXGzJpdIz70OIHlRq9GXYsafuvew3Y2uCdg-G7IdspKVDkTZz7VMcE32DTIuDxiCn96JmGtgusAiJWsfUMyzOWCjZWEZtQiZPVq6US_aRxkFdpf5dzHn_ENnhTtGLbYxvoUrZDfKXuv9kRcppm_Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9b7cb450.mp4?token=NzD_4v5d5J9Zxjm9pOmulzx-WgCSugnieCp55RyidTQnZpvv8-33WpfjvR8EyanH0C2Di2x0jqUiQkelMJErB2Hl6wA4hjywW-0GcNSWqOgY5FY7G_U3CTU9KdN3LVBm565N-ij_TR4E74UuwDIn4k6JcIoii4WNlEVWUkkKub7UnsZ1lITZIC7ZjlRshavw1pXGzJpdIz70OIHlRq9GXYsafuvew3Y2uCdg-G7IdspKVDkTZz7VMcE32DTIuDxiCn96JmGtgusAiJWsfUMyzOWCjZWEZtQiZPVq6US_aRxkFdpf5dzHn_ENnhTtGLbYxvoUrZDfKXuv9kRcppm_Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وزیر امور خارجه قطر:
ایران یک کشور همسایه است. باید بین ما و آن تفاهم وجود داشته باشد.
آنچه اتفاق افتاد غیرقابل قبول است - هم علیه ما و هم علیه بقیه برادران ما در کشورهای خلیج فارس.
اما در نهایت، همه ما بخشی از یک منطقه هستیم و راه حل باید دیپلماتیک باشد.
ما می‌خواهیم یک منطقه مرفه ببینیم.
ما می‌خواهیم یک خلیج مرفه و یک ایران مرفه ببینیم که به طور سازنده با کشورهای خلیج فارس، با سطح بالایی از اعتماد و همکاری - به جای آنچه این جنگ‌ها به جا گذاشته‌اند - همکاری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67041" target="_blank">📅 18:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67040">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4f066d85d.mp4?token=iloqN2Fe3_U7GiFZoC3zqrj_yZiSTXhQmL9TfLiqr8oDYEXbeKnQpZjhvEwKPKHpwO68AdvyHRVfUVTnG5hhxrR12IdCSD_n3F0Ro2GsLio403RHGGqdqZBteSjgd9vcztI0D6EgCpL-gnuwF6mA15f5fowu8ex6TpnzI62kWp7IXYukuMjcIZdxW9VWfmVxbIUn8ARJmr-cMIOW1u8FlkfHZ7EHdWrCNqkzXODI7Tzth83Qd--DOLD9wAUtdiVdn0lypf1frvYfLjdH4HJlC0PNVooTxpprvEGSMp64SGletXukympORvA-N_M759CKhASbdhYSSOuNUaxFiX84Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4f066d85d.mp4?token=iloqN2Fe3_U7GiFZoC3zqrj_yZiSTXhQmL9TfLiqr8oDYEXbeKnQpZjhvEwKPKHpwO68AdvyHRVfUVTnG5hhxrR12IdCSD_n3F0Ro2GsLio403RHGGqdqZBteSjgd9vcztI0D6EgCpL-gnuwF6mA15f5fowu8ex6TpnzI62kWp7IXYukuMjcIZdxW9VWfmVxbIUn8ARJmr-cMIOW1u8FlkfHZ7EHdWrCNqkzXODI7Tzth83Qd--DOLD9wAUtdiVdn0lypf1frvYfLjdH4HJlC0PNVooTxpprvEGSMp64SGletXukympORvA-N_M759CKhASbdhYSSOuNUaxFiX84Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جزئیات اسکان و تغذیه در استان تهران در مراسم تشییع رهبر شهید
اطلاع‌رسانی رسمی جزئیات مراسم تشییع در کانال پرچمدار
👇🏼
t.me/Parchamdar_tv</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67040" target="_blank">📅 17:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67039">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78917b25d9.mp4?token=eNJDTDL3Cr47kGKEuglOSlE6mSQ8z5YJH4PH29cThcc-oXvPTKHywK-QY0GMo_pzpIV3TgBJZfr--KFggsQcJH4oIjnu5nj8zs-63KFk1RjN8o-VVQFic4cSq0D46cWIfI3GG8XbkhOFHXWZHpH05TXhD2iussKtOeDB2IYelsfKNb3os6hJqWkRdXnlJ61jE7vrwum8jLqOOTmknOjIvDHulsieBIiKDVkG1IuSwGlFkGh4C-_XO34wGkIdHhesHE7v0PVdPscL64ZQ2bG0Nfo2GrQ2k1PuHBhLVCUiHrh730EiPWAlB2OmMhDWOY8_zYTLrXJuPX5zVAXCO7DR6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78917b25d9.mp4?token=eNJDTDL3Cr47kGKEuglOSlE6mSQ8z5YJH4PH29cThcc-oXvPTKHywK-QY0GMo_pzpIV3TgBJZfr--KFggsQcJH4oIjnu5nj8zs-63KFk1RjN8o-VVQFic4cSq0D46cWIfI3GG8XbkhOFHXWZHpH05TXhD2iussKtOeDB2IYelsfKNb3os6hJqWkRdXnlJ61jE7vrwum8jLqOOTmknOjIvDHulsieBIiKDVkG1IuSwGlFkGh4C-_XO34wGkIdHhesHE7v0PVdPscL64ZQ2bG0Nfo2GrQ2k1PuHBhLVCUiHrh730EiPWAlB2OmMhDWOY8_zYTLrXJuPX5zVAXCO7DR6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه داماد، وسط مراسم عروسی تازه متوجه میشه عروس 11 نفر از دوستای پسرش رو هم به جشن عروسی دعوت کرده؛
گفته میشه داماد اول فکر می‌کرد اونایی که دور عروس حلقه زدن، فامیلش هستن؛ اما بعد از پرس‌وجو می‌فهمه همشون دوستای صمیمی عروسن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67039" target="_blank">📅 17:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67038">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de1b4e3a38.mp4?token=OncwUPTJYJbfxSQTEfBftLAEDicITxYeE4t3_ddTy7DQ0TYTEidTDNcnnVEJVvHaTpE2MFuvPrBVenMIs4c4CBmwOSaeK_Jhbhgfv2rpn5DlwmOsHtKFLFcGuLwJ99dNW_lJOowkq-2ScymL_2fKkH-IPFVRqMTAEX8O_TpNq4rT1EELloE7ozCIjb_Urj5ezmu0cDXNSIdN0H7pvVTciNQwwEWWQ5mlCA5DwvQPILed7gT7tUm-zWh9q1UmzauVm0z-kbsbSWKT-VhJ_5MaNr41UbX7TboFAp8dLfS6CdtfZvyKVhIg_b7zsVHW-63oC3DpxoFddzANW7hy1zcVeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de1b4e3a38.mp4?token=OncwUPTJYJbfxSQTEfBftLAEDicITxYeE4t3_ddTy7DQ0TYTEidTDNcnnVEJVvHaTpE2MFuvPrBVenMIs4c4CBmwOSaeK_Jhbhgfv2rpn5DlwmOsHtKFLFcGuLwJ99dNW_lJOowkq-2ScymL_2fKkH-IPFVRqMTAEX8O_TpNq4rT1EELloE7ozCIjb_Urj5ezmu0cDXNSIdN0H7pvVTciNQwwEWWQ5mlCA5DwvQPILed7gT7tUm-zWh9q1UmzauVm0z-kbsbSWKT-VhJ_5MaNr41UbX7TboFAp8dLfS6CdtfZvyKVhIg_b7zsVHW-63oC3DpxoFddzANW7hy1zcVeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جان کری، وزیر امور خارجه پیشین آمریکا، درباره ایران:
اوباما تحت فشار و اصرار نتانیاهو قرار گرفت تا در بمباران ایران مشارکت کند.
و از اوباما درخواست شد که اجازه (چراغ سبز) بدهد تا این اقدام انجام شود.
اما اوباما گفت نه و از مشارکت در آن خودداری کرد، و آن را یک اشتباه بسیار بزرگ می‌دانست.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67038" target="_blank">📅 17:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67037">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12f6a02f29.mp4?token=YfzeWHc1SCik1seaVstO2PYzSMMgY6hMyPpYgiP8fvGT8thoGD3yy4RrCcTQmWHvsFRDm0bNCsaY3s9CtRE52bn5xTN8KFPhTKwXkgdOGLuVEs5jm-19_8iFQeqJFyhuDBRqq1k1LElclRT9XpNcz-3AeP2E4zhRuqoq4BMudPwGEFU1PhrNxkkkFPKzTZTur2j0N8NW3HyiOKsCrUqR09fptHGDWX7U9pldsZcmN_ltxqbSoEARDDPGXHcpb7rr1aPCAOT7ApRF98Z6TCue7S7KCEvhmye9Aba2YTAbiONrn9Tz6FhijhWoeNa1ArnFdm17tZGZbBA004A3kr-_qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12f6a02f29.mp4?token=YfzeWHc1SCik1seaVstO2PYzSMMgY6hMyPpYgiP8fvGT8thoGD3yy4RrCcTQmWHvsFRDm0bNCsaY3s9CtRE52bn5xTN8KFPhTKwXkgdOGLuVEs5jm-19_8iFQeqJFyhuDBRqq1k1LElclRT9XpNcz-3AeP2E4zhRuqoq4BMudPwGEFU1PhrNxkkkFPKzTZTur2j0N8NW3HyiOKsCrUqR09fptHGDWX7U9pldsZcmN_ltxqbSoEARDDPGXHcpb7rr1aPCAOT7ApRF98Z6TCue7S7KCEvhmye9Aba2YTAbiONrn9Tz6FhijhWoeNa1ArnFdm17tZGZbBA004A3kr-_qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیو ای دردناک از لحظه وقوع زلزله در ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67037" target="_blank">📅 16:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67036">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e63aa7bc7.mp4?token=USoDiWTJMFrI69uJb2-O0PNxjOESnJ1GuBhpW4RUfdE-noefPFo5s3l3T3nmkmS6ITaj0GLyPyQ-6q8vbFBWwVfbkUxjbe1Z92_WVE2tWqXPYr0De7hY5KqhQPmFm34jqmlAj4QAse7YBRHN7Pygdkhv1j26_iEtZwPW1Ur9y_OiNh_VpBYaaBGUlYSKw6r6odWWs8Hd3O_Q9BPVdBbnhoDcBFl3SZz2rXrpi9RyHoBFlX6ZiVBPLi_37vrxinvrQCgFF5b2V9KQzI3GmlBXNP_IIYPJ15aN3U38wiInokgf3WbPS6Jac6xHDz2F4phfIIoXAinC0ch5FFYmQ-Ytew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e63aa7bc7.mp4?token=USoDiWTJMFrI69uJb2-O0PNxjOESnJ1GuBhpW4RUfdE-noefPFo5s3l3T3nmkmS6ITaj0GLyPyQ-6q8vbFBWwVfbkUxjbe1Z92_WVE2tWqXPYr0De7hY5KqhQPmFm34jqmlAj4QAse7YBRHN7Pygdkhv1j26_iEtZwPW1Ur9y_OiNh_VpBYaaBGUlYSKw6r6odWWs8Hd3O_Q9BPVdBbnhoDcBFl3SZz2rXrpi9RyHoBFlX6ZiVBPLi_37vrxinvrQCgFF5b2V9KQzI3GmlBXNP_IIYPJ15aN3U38wiInokgf3WbPS6Jac6xHDz2F4phfIIoXAinC0ch5FFYmQ-Ytew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حصیر آباد اهواز؛لحظه ساییدن سیم‌های برق شهری با «برج میلاد»:
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67036" target="_blank">📅 16:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67035">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
سخنگوی کاخ سفید:
استیو ویتکاف و جرد کوشنر، در نشست روز سه‌شنبه در دوحه با جمهوری اسلامی شرکت خواهند کرد.
همزمان با نشست‌های مقام‌های ارشد، گفت‌وگوهای فنی نیز برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67035" target="_blank">📅 15:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67034">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZ2PdIgC4Axe7MiaUjnMjrVg2ALtvwyyceVb18m_ErS9DMAJoc7Ppdp2YP9LMdMyd81cOa8oNj3meRIcjshevc2HslBqbUfvDQHb7ba9XS40uiGX2Kmov0EitbL7ICA8Yt8dC2Hc1fEiHYhpe2sYXZVQyv4B1y-hw2pBcD2nqnjTVWO6EEN0Q9o37MZvjMk6V_botTfYi5kLAxCuJmFpZjiJHxrnXm4C027TOXAZW3_3vIxluVxQiUM77vXjD1eMTQQlv7LA_TjUE6wGVWDpQyqMwJq-nzDylcv2f75tgNXotNmpLn0ErtBl1sKk_GxEHfHdUwNZOPKbrNGR-Bvgrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایران درخواست ملاقات داده است. این دیدار فردا در دوحه برگزار خواهد شد!
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67034" target="_blank">📅 15:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67032">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4zMAXrPHcMbEs_QnvX_XSHuFlUaPF4rMs4sY-7evIYJXFhS7rqlPPz8wKTTiGYs5fnn6RevypFHS76iDkRqhIbj6a1XFbKQr9RyhSUqMJim0aqgSNAnOlWRLvr3livt2ty8JS_j4yhfk0fYxNqb-YbFxJNZ2brFcgMGZtLbF_anNa4x5G3vuYnEGwRTCNXCXMixCESaG3bbgC7VJikaxkXvgi_K2lbd__5w_PFiPDAwwc1wJpZRcEI7RwlRt8da2oBudjkJ9VOSk15ouVvh5YcFie7aC3aJuS_aDUdYLEPFL3T_Q_LV_MQiWo3xfwpfj5xRrG1w2mWvnrOoQig46w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ در تروث سوشال:
محبوبیتم تو نظرسنجی‌ها از همیشه بالاتره
حتی از روز انتخابات ۵ نوامبر هم بیشتره؛ با این حال ایران نباید سلاح هسته‌ای داشته باشه
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67032" target="_blank">📅 14:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67031">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmZlXhypkMeFV1U5KwIwx_3nzncagAM8a1H8q7RQ5DcFMTsDbAql_o6aORS1PyvHk2TonQclo9Nx1FIqObz5mZbz8OugRtfVbqqFFHBVow0kGWnhI09VSjomRJJPoCl6t495_XVf4WoYk75_G8uPwnf0qcFfbGiCHdzoEGNk3U4S1rumzZVbRyZNhjKDKDXs3sK2-vBOenCUNNgBOZlKZSHRCq5JZ2-fWfgiCq346nXR7GSOQUCu1cNTlmfY-XeWECZuOZSnHlGObnkmdV6Rb7fHwVgyncZH54SXMgsPhi_Tkt2NtOudZuR-0qeEf1sJ6CMuGMTsQpfZtVwQs5KG6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حسین شریعتمداری (کیهان) :
گام اول تحقق خواسته‌های رهبری در مذاکرات، تاکید بر تحویل ترامپ به جمهوری اسلامی برای محاکمه در مراجع قضایی ج ا است
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67031" target="_blank">📅 14:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67030">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311b818b7b.mp4?token=kGz-oYI4YLfOQAVeJcwYYZeWfXhH_N3IYhDPx-wv-LAvThitzNCubjqKDUfqUJxvb9sHL_rLGmjuYB1ule8U4xM0VQu9LRvLju4r43B4-aiPKE1sABmTVlU0391BaZvRWrg56tMPlm0S81-_M4AF0gM_51ygJntmclOxFIFunRtWOGiNBiLR-J5xVTMUEmYEnefpQEy7-2CZITHQHgZy0JPJsAkCsBBmPsr8gcUuckJQ6u-LNiEWbF1vBPClt0hKWdyNjjF1SCsmZbE-8avOXBrB2GSUwzv9fW8eGX5j3TH5vZ0nd-rZ8T8Rh_qF0aoxuiNekqD-nsqlZAMiOfqH0GYoXRp_jS4nFD34irhlsY7oOSnDsX9aronVr9dGCSVJmltAQXVjJHOX-vZSWjlTsg00_7GHj8kw1yKTkFY4fCxh_syOC6zLZs1HrIxK34X0tDLMKclJLVCsPalxZ6FKgzj5NLQ8ggLbDbXJ-PqohoWX1WIPxujaaJKaGxYU3xE3hdac3MEHVDD1MVu6Pvpe2kUQCqk_PXjEsiMYlGA40uqoPGi_ENHiN-v3iTQAXTd9SLAFq_Hv752R6FnuS-SZm90OIVw5_zXtQik4bMiSq7ZwCx5_DT3791x-xLxv9Hihslb-hRFUR3xTVtCoD5q8rG8munu-LeZHZMQfylf_XQs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311b818b7b.mp4?token=kGz-oYI4YLfOQAVeJcwYYZeWfXhH_N3IYhDPx-wv-LAvThitzNCubjqKDUfqUJxvb9sHL_rLGmjuYB1ule8U4xM0VQu9LRvLju4r43B4-aiPKE1sABmTVlU0391BaZvRWrg56tMPlm0S81-_M4AF0gM_51ygJntmclOxFIFunRtWOGiNBiLR-J5xVTMUEmYEnefpQEy7-2CZITHQHgZy0JPJsAkCsBBmPsr8gcUuckJQ6u-LNiEWbF1vBPClt0hKWdyNjjF1SCsmZbE-8avOXBrB2GSUwzv9fW8eGX5j3TH5vZ0nd-rZ8T8Rh_qF0aoxuiNekqD-nsqlZAMiOfqH0GYoXRp_jS4nFD34irhlsY7oOSnDsX9aronVr9dGCSVJmltAQXVjJHOX-vZSWjlTsg00_7GHj8kw1yKTkFY4fCxh_syOC6zLZs1HrIxK34X0tDLMKclJLVCsPalxZ6FKgzj5NLQ8ggLbDbXJ-PqohoWX1WIPxujaaJKaGxYU3xE3hdac3MEHVDD1MVu6Pvpe2kUQCqk_PXjEsiMYlGA40uqoPGi_ENHiN-v3iTQAXTd9SLAFq_Hv752R6FnuS-SZm90OIVw5_zXtQik4bMiSq7ZwCx5_DT3791x-xLxv9Hihslb-hRFUR3xTVtCoD5q8rG8munu-LeZHZMQfylf_XQs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش چشم کارشناس صداوسیما:
آمریکا فقط به دنبال باز نگه داشتن تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67030" target="_blank">📅 13:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67029">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNneDmeNzluBPN-jqwOUcZu_0ipLO4CRQ0peB2DEIyj4DCJRgL6NVJ41tie-7DbbJmzIaWDhBHaWHMcMC-knZD1ENrUnxcgQcY3KlrrayUmF_Ml8aob0zoOHgumkyGFfWpv0Gn1HTidL7cKvxATariDFgUo5JedGCweQL5CgnGiGC9UCAjiMC_FfQNSzNk93OLP1CRCsRgcmHLY2y9JX-D48Gzr4YOQh9JxnCSIMi3RxcCGFTLzSnbL4PLhFUkgENilIJoUCtRzXKt8mlTj8_4jq7KWs8lhmx91gEDSLLbKYbUMankDjKIiQAafF8Wu7hi09oJ5mCx52nVvUAs52ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرزشی : قالیباف ٬ عراقچی پس خون رهبرم چی؟!
واکنش صادقانه ممباقر و عباس اقا:
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67029" target="_blank">📅 12:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67028">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/706d335e17.mp4?token=oz_NZIIBk9GW_N5jPpnfPC0QaalgOgAxYfehxlTpZ0bb3oqopFXBu0hyn-w-0--7slzi9u2l-tLiOb7UxN_g4VGtitBHjCb5wh0HL0X7OTAgUMpELFhCtl4wJs0M2jq4PCiiKihyJpBM-xdmS7Zssh46-cb0lCU8iQ0qQ-S1AcpVSbLEihnF0NQtAD6aJfaUZT2OsqyqKoBG57GSjgfICH3D_4kOuWvgNEfgyILkmnUj5thlTUnjx0atMv12fCtCPmLfUvInYT8GwCKRT8b4DoKyqx8kzAD8SOVc6q7DnDgMfMpa8KrMRegkOjqM_zXW5_zXN2NyvPmrJ8aaMWu1gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/706d335e17.mp4?token=oz_NZIIBk9GW_N5jPpnfPC0QaalgOgAxYfehxlTpZ0bb3oqopFXBu0hyn-w-0--7slzi9u2l-tLiOb7UxN_g4VGtitBHjCb5wh0HL0X7OTAgUMpELFhCtl4wJs0M2jq4PCiiKihyJpBM-xdmS7Zssh46-cb0lCU8iQ0qQ-S1AcpVSbLEihnF0NQtAD6aJfaUZT2OsqyqKoBG57GSjgfICH3D_4kOuWvgNEfgyILkmnUj5thlTUnjx0atMv12fCtCPmLfUvInYT8GwCKRT8b4DoKyqx8kzAD8SOVc6q7DnDgMfMpa8KrMRegkOjqM_zXW5_zXN2NyvPmrJ8aaMWu1gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
آتش‌سوزی گسترده در پالایشگاه اسلاویانسک روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67028" target="_blank">📅 12:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67027">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
پزشکیان:
بر اساس برنامه‌ریزی‌های انجام‌شده، شش میلیارد دلار از مجموع ۱۲ میلیارد دلار منابع در قطر، آزاد و به کشور بازگردانده خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67027" target="_blank">📅 11:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67026">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23c44657f9.mp4?token=TEyrH_5RH_up94PhTtKf1nOmpeA-Rgi4HXFGr8nTukbdRx0u7nTmclZnrvdKcJIdVJ9pnxClV0SWxVGspyaJAtpOxh3UvOp781NqePaTmV0SRA9qKbRkFYRX4GpVc9Mghua99VzllttgR7H1936mSZI8c3BAqgV_XO63nMgJ1l7bTc9c-Fcs6wE6jsRllLKJpdHPtAW1f6CxkfOCoKzCoWUXExs-QULPRkFVeiB1Cd0wtsnIY1iP1FnUvqo4oJVkVrsDlYy_jSyPscepR3EGBeSmjntEbXLCZM3_Waoku3YNnD84CROM_QVBhfAW_ASIswCvgdQLQWHxUEyfVX2rqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23c44657f9.mp4?token=TEyrH_5RH_up94PhTtKf1nOmpeA-Rgi4HXFGr8nTukbdRx0u7nTmclZnrvdKcJIdVJ9pnxClV0SWxVGspyaJAtpOxh3UvOp781NqePaTmV0SRA9qKbRkFYRX4GpVc9Mghua99VzllttgR7H1936mSZI8c3BAqgV_XO63nMgJ1l7bTc9c-Fcs6wE6jsRllLKJpdHPtAW1f6CxkfOCoKzCoWUXExs-QULPRkFVeiB1Cd0wtsnIY1iP1FnUvqo4oJVkVrsDlYy_jSyPscepR3EGBeSmjntEbXLCZM3_Waoku3YNnD84CROM_QVBhfAW_ASIswCvgdQLQWHxUEyfVX2rqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حملات سنگین به جنوب کشور در جنگ اخیر
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67026" target="_blank">📅 11:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67025">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">این کلیپ داره مثل بمب وایرال میشه، الجزایر گل سوم رو زده اتریشیا دعوا کردن که چرا طبق توافق پیش نرفتین‌...اونوقت بازیکن الجزایر اینجور با دست نشون داده که مساوی میشه نگران نباشید و ارومشون کرده  @sammfoott | پروکسی متصل</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67025" target="_blank">📅 11:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67024">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a1a05c8c.mp4?token=MCZ_4RE7QC5zkYmvrVq7-yRgp-f2JhasRfIqsyekmJftqvX-QL38IpSukc37x5ErHhdt6mqZcSNChR36To_h6JuTvKCJXkDRphPcReWIsNIWabRsstZ8M8uwH2lUOlbf-MiDWS7vVCKWxKxYtFGecFOZ-5l2tdLfF8_2FP5oS9frd0pPF5iA4CBQoTmclZU-85EMRykXLXm4JD9XLyfVrn9u_uOjAfR2NCuBK1WLhnt4OUBtSOkTLWax8rGXCi6nKW1Eb9uir-caI6zjpSlaqerzVkTv4iYsTI18hCj7bqStojYbzViT4S_WbAL_l8ddwTKXpJxN8jcL_4MhYyWr3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a1a05c8c.mp4?token=MCZ_4RE7QC5zkYmvrVq7-yRgp-f2JhasRfIqsyekmJftqvX-QL38IpSukc37x5ErHhdt6mqZcSNChR36To_h6JuTvKCJXkDRphPcReWIsNIWabRsstZ8M8uwH2lUOlbf-MiDWS7vVCKWxKxYtFGecFOZ-5l2tdLfF8_2FP5oS9frd0pPF5iA4CBQoTmclZU-85EMRykXLXm4JD9XLyfVrn9u_uOjAfR2NCuBK1WLhnt4OUBtSOkTLWax8rGXCi6nKW1Eb9uir-caI6zjpSlaqerzVkTv4iYsTI18hCj7bqStojYbzViT4S_WbAL_l8ddwTKXpJxN8jcL_4MhYyWr3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67024" target="_blank">📅 10:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67023">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91138929a8.mp4?token=fzsn4m45UDEZOn-Ah97Cnth_c8ul8HZUuj-KZcqwf9HTbAhLP0dvFmpHXlPdDCgAcH9YPzL9JD3AdzCLDOIlZiDry4Tih0sudR4CkBHZjUvYeXCXGCKAod24aJ_osf7VVy3lsB-QX-DvW1LRe63YOKX1oSEuZrZxIrolOhA8Wv1zqrjHEw452i6317tvM0RZrY_OWZNfEWwvC7innrd8rWhE3uePv8gZVzmFWMkfVXAejVCGTG_Tj08R0qZaeDXJOb3GqYaz7CRAtSDttB8U7X67SWXDERRbzfFhAxsNufzdNprmWkshsaXZ0OiXcdWYlTvj32VlGOdChSIkO-u_M4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91138929a8.mp4?token=fzsn4m45UDEZOn-Ah97Cnth_c8ul8HZUuj-KZcqwf9HTbAhLP0dvFmpHXlPdDCgAcH9YPzL9JD3AdzCLDOIlZiDry4Tih0sudR4CkBHZjUvYeXCXGCKAod24aJ_osf7VVy3lsB-QX-DvW1LRe63YOKX1oSEuZrZxIrolOhA8Wv1zqrjHEw452i6317tvM0RZrY_OWZNfEWwvC7innrd8rWhE3uePv8gZVzmFWMkfVXAejVCGTG_Tj08R0qZaeDXJOb3GqYaz7CRAtSDttB8U7X67SWXDERRbzfFhAxsNufzdNprmWkshsaXZ0OiXcdWYlTvj32VlGOdChSIkO-u_M4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
🇮🇱
بنیامین نتانیاهو، و یسرائیل کاتس، وزیر دفاع اسرائیل با انتشار بیانیه‌ای مشترک از کشف و انهدام یک شبکه زیرزمینی در منطقه «مجدل زون» واقع در جنوب لبنان خبر دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67023" target="_blank">📅 10:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67022">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sb8IsJ9VVPvQpUVABQiSTPOC9IrQOY1Tce96oOdf6lAnACDp2c6StIM5oyQQmcsFKZePUIKD3YZ9oY5FvHOMJutFbz1DbV-HTuRKnAPHcn9MVZ31xMVeA_1rRD60ZeMeOQSDfmDRn5mqY0me0AKLZw5EMKC_QSJjX53P8ZDF1SyuYAS4ixq-W92Gft0MSfGHrCiUdYHHQ4dXk2Y5yN68g8MqZy4snPb6TsxjbV4jFgd-odvcODXUBpRo0nQ1XAR6YfPjBhYvaUZVBpnXBmtEv_4qZ8Yqk2N9hQrXuVGy1Sz9eCw6MrtWHqxiJHzGWsq4fcxJb8H3vKAMUSCO93-8lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شاهزاده رضا پهلوی:
🔴
‏از ۴ تا ۹ ژوئیه (١٣ تا ١٨ تیر)، هم‌زمان با برنامه‌های تبلیغاتی و فریبکارانه رژیم برای دفن بقایای جنایاتکار اعظم، علی خامنه‌ای، و در ششمین ماه خیزش ملی شجاعانه ۱۸ و ۱۹ دی، ایرانیان مهین‌پرست و آزادیخواه در قالب هفته جهانی اقدام برای آزادی ایران، به خیابان‌های سراسر جهان می‌آیند، تا واقعیت ایران را به گوش جهانیان برسانند، و هم‌زمان یاد جاویدنامان انقلاب شیروخورشید ایران را در ششمین ماه کشتارشان گرامی بدارند.
🔴
این کارزار ملی با گردهمایی‌های روز ۴ ژوئیه (۱۳ تیر) در برابر سفارتخانه‌های ایالات متحده در پایتخت‌های جهان آغاز خواهد شد.
🔴
پیام ما به ملت و دولت آمریکا در سالروز استقلال این کشور مشخص است: با تروریست‌ها معامله نکنید! مردم ایران را انتخاب کنید.
🔴
۲۵۰ سال پیش، آمریکا آزادی را برگزید. امروز نیز مردم ایران برای آزادی مبارزه می‌کنند.
🔴
معامله با رژیم جنایتکار جمهوری اسلامی در تضاد با آرمان‌ها و ارزش‌های ایالات متحده و جهان آزاد است.
🔴
هم‌میهنان در داخل کشور نیز می‌توانند با حفظ امنیت و پنهان نگه داشتن هویت خود، از طریق ضبط ویدئو بر مزار جاویدنامان، دیوارنویسی و دیگر روش‌های خلاقانه، پیام‌های مشابهی را خطاب به ملت و دولت آمریکا منتشر کنند.
🔴
برنامه‌های دیگر هفته جهانی اقدام برای آزادی ایران به مرور به اطلاع خواهد رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67022" target="_blank">📅 09:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67021">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‼️
آتش زدن متن تفاهم‌نامه توسط یک مداح تندرو
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67021" target="_blank">📅 09:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67020">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67020" target="_blank">📅 04:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67018">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qqoUY2WN1AAzJshogABtJOue9BSQXy2WBxP7n1OjmZ4KaZSzvkwNthfsFKctZlKM_ITxi55VpzhhEq2ZN6Vkjpsotqp255SRs4WaHWQTcfHrD-mJdc28mMRj-xdN2F0JZhWnPE7R3a8DuEAVqc2ixCpYoV9lewi-Kycw5wYVgjy5gl7ILVx7xrV_M82ue_qrWrhJwiPIre7ZVt8JGm_VymdXiSS40LVQS1vdw5R2BKVTlPi8JHMN7wZCcX1Ro1zzbE_vew_ETMd9hXOpzb93rXQULBj6SXGuGrp-WYzA0Ca1-FyDw8BmP50EXwODQd5wGuC2WpK7ii4cqBzAqa4r2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67018" target="_blank">📅 02:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67017">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b55b34728.mp4?token=chwx3zQ1tNsJswgLLh-FiQNHrayW8as2_X4qYELviKN_cXnwhPealF126tZsqjPQQfD01aIYzFawzgIiaDaHhSbwbnqtAsQa-c4EdTWg4pugqwvCjmYwgGGE9KIq6fTXo7bITYlVlnr2ae0lDplNmQeQH2jQApSqFA2Tu8EXn6586GDMfai-e0UOMPrtotuDZ5RC52p7XiXxi2cGTrnbw31xws8xU1kW-7vpn7XSmd52axKbI5LAJDnT7X8bvDRQBhdOZO8XL71fRMd312sa01uKBj0SrAoEDKSuR-WSXUq7mxNY6KidBqv3Xr9ohMgFiHHcHcumsSyrWnK4C5ZbNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b55b34728.mp4?token=chwx3zQ1tNsJswgLLh-FiQNHrayW8as2_X4qYELviKN_cXnwhPealF126tZsqjPQQfD01aIYzFawzgIiaDaHhSbwbnqtAsQa-c4EdTWg4pugqwvCjmYwgGGE9KIq6fTXo7bITYlVlnr2ae0lDplNmQeQH2jQApSqFA2Tu8EXn6586GDMfai-e0UOMPrtotuDZ5RC52p7XiXxi2cGTrnbw31xws8xU1kW-7vpn7XSmd52axKbI5LAJDnT7X8bvDRQBhdOZO8XL71fRMd312sa01uKBj0SrAoEDKSuR-WSXUq7mxNY6KidBqv3Xr9ohMgFiHHcHcumsSyrWnK4C5ZbNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات هوایی پاکستان به ۳ نقطه در خاک افغانستان
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67017" target="_blank">📅 01:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67016">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18d3b4a51.mp4?token=nzZ6RKdvcjgC-J7OD2qJI8V1fdmNwfPumxD1zk_f0ntmMlMLqATwa8cJoSTT6k3H-_Wm6Qkn3igcWRFT6Ra2NUW1L52rovMqXvSAfd4gf3W4a6Cvcn_NgO5Oqje3kSB2LwC-ZegWZw-PC3b7HeLzrenZKfHbFt59n6HD9sxvIDeyDuorMQ67wLlXxkg8N_S_p2dNihK1Of-JTEsBwhg7tInFS4EtyGSQen3gSTp_WVxAoSKdTVe86uTR5Hhd25R3TRFfdizrMGxzDcHjZt81d_ssPAG7qbiPtJEwoNxh3xQfNKi2Cbkb3qY6n0PtWyfH_89SCTa3CgZlT2FCEpuJhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18d3b4a51.mp4?token=nzZ6RKdvcjgC-J7OD2qJI8V1fdmNwfPumxD1zk_f0ntmMlMLqATwa8cJoSTT6k3H-_Wm6Qkn3igcWRFT6Ra2NUW1L52rovMqXvSAfd4gf3W4a6Cvcn_NgO5Oqje3kSB2LwC-ZegWZw-PC3b7HeLzrenZKfHbFt59n6HD9sxvIDeyDuorMQ67wLlXxkg8N_S_p2dNihK1Of-JTEsBwhg7tInFS4EtyGSQen3gSTp_WVxAoSKdTVe86uTR5Hhd25R3TRFfdizrMGxzDcHjZt81d_ssPAG7qbiPtJEwoNxh3xQfNKi2Cbkb3qY6n0PtWyfH_89SCTa3CgZlT2FCEpuJhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
فعالیت ۲۴ساعته و سنگین ترابری هوایی آمریکا طی ۷ روز اخیر در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67016" target="_blank">📅 00:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67015">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vO1w8cj62-ZEAnfWZJQ3HiJgJFz1gjPr9G_BG0-5yH0HdP0oSnpJj82oSscMaM6Pmv_ti_qLGKAiKznuHgclg3vroGBcTKrwkx6zM35d5GgVqV-jeXi26qunXHoJPexhExKjAxAWk2wk4JtX5i8WpzHw0bP7Ph88XlBaIwBReYp1pAVIRu8OkQLE6y9CoDu-KQT-z05o2uhiGoQm0F3qJAZIcDGk-jjOKCQhDc5NMW0IjtM2JYu_4e3SkOVUPGnBS3ptZP-8hqIxhYrVKAdLxLIafAaveKwl-M7O4PYII2_S8qk5ODPF9bcdhyewdXoRFy54FepufEd5N4XUsFRhDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آکسیوس:
به گفته یک مقام ارشد آمریکایی، ایالات متحده و ایران توافق کردند که حمله به یکدیگر را متوقف کنند، در حالی که دو طرف قصد دارند روز سه‌شنبه در پایتخت قطر برای حل اختلاف خود بر سر تنگه هرمز دیدار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67015" target="_blank">📅 00:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67014">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e66d65d2e0.mp4?token=oxk1_45m-BjtZfkFnn72au0cBvQJ5H700ETZqVj88RkebxwHWElN96kSv5-zF7-EDE7FqWsVqAGdOdpcb8O0Lr51_pDkLdvkI2lJmKf0GUbfj39ATyktSxAMSTAlOd1NLf5yftVFusip--ygqaZ3KghXtvqwmCmSy-cELW3mt7TxwC8UZIOGIdqomVdoNjodd7cKu2PlHxWUNfFX1RxtsHZM8jFuKB4f2BvJYUPNpiSM6ozZ1sJBduPh9pcbaUBH_2Lgf42qX3R2wiqBvKP-0Q5e1jt-W6yNElpKJPJ2Dvh3pK-jdv09y1s5UtPFYMWnseag4S9XKW6jv9EuHw_rrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e66d65d2e0.mp4?token=oxk1_45m-BjtZfkFnn72au0cBvQJ5H700ETZqVj88RkebxwHWElN96kSv5-zF7-EDE7FqWsVqAGdOdpcb8O0Lr51_pDkLdvkI2lJmKf0GUbfj39ATyktSxAMSTAlOd1NLf5yftVFusip--ygqaZ3KghXtvqwmCmSy-cELW3mt7TxwC8UZIOGIdqomVdoNjodd7cKu2PlHxWUNfFX1RxtsHZM8jFuKB4f2BvJYUPNpiSM6ozZ1sJBduPh9pcbaUBH_2Lgf42qX3R2wiqBvKP-0Q5e1jt-W6yNElpKJPJ2Dvh3pK-jdv09y1s5UtPFYMWnseag4S9XKW6jv9EuHw_rrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
دختره رفته پیش دکتر، یه تیکه نبات تو واژنش گیر کرده! دکتره میگه این چیه؟؟
میگه ما یه رسمی داریم، بعدِ عقد نبات میذاریم داخل واژن‌مون، بعدش میندازیم تو چایی که داماد بخوره. چون با اینکار زندگی شیرین میشه!
😢
😢
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67014" target="_blank">📅 00:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67013">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8a95a6c6.mp4?token=uxwUs562kS6S-MYnRXOHr_S6NHc1FMrFpKtcCC6GWf0fq_D7vP5XI8ZF7d2kFYiUXMOSk20rdVESMMP3pvJoMyqfgDhSUiSMy6sDQIn1cNLuI98zIDTMM4cbQoJBfSA6N8MoLtqLeZ3RIdIpJaa2AocmmuZxD1gJ9lpwzwQSoSSbY7cCL7MVrMMq8qRQe831aq5qvs3t47hvKoAhHPF1iH7OszpEQbJCn43LApMxplQKMMCTIZlLJtE54hMbubcpHzJ7wEoIJ1etrAWYcgk4yZmb-WJR6jYRJ9yq68JKdvKA5WVAERrMtrtEMVIcSF2brBjS-fUer2Q0I-WENGTQKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8a95a6c6.mp4?token=uxwUs562kS6S-MYnRXOHr_S6NHc1FMrFpKtcCC6GWf0fq_D7vP5XI8ZF7d2kFYiUXMOSk20rdVESMMP3pvJoMyqfgDhSUiSMy6sDQIn1cNLuI98zIDTMM4cbQoJBfSA6N8MoLtqLeZ3RIdIpJaa2AocmmuZxD1gJ9lpwzwQSoSSbY7cCL7MVrMMq8qRQe831aq5qvs3t47hvKoAhHPF1iH7OszpEQbJCn43LApMxplQKMMCTIZlLJtE54hMbubcpHzJ7wEoIJ1etrAWYcgk4yZmb-WJR6jYRJ9yq68JKdvKA5WVAERrMtrtEMVIcSF2brBjS-fUer2Q0I-WENGTQKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله آخرالزمانی اوکراین به پالایشگاه نفت اسلاویانسک روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67013" target="_blank">📅 23:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67012">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivLDSjIR391rkSQKSiYHDVqo3G_hxik9cZOZpuz6ooSCCXQugPQeFoq__dv_CagrWoX9dMz0W62VnYxs2F8vh0xpgt9ViC5kChODDgtCQcnSQa2Scd4x4E-xhZyfxS91dS_3NeKVjYPmf3tLno1b_n3EUj5ZYLGmZCWnmLbHbJI5wmpl27PPFnxo8EmniNY9VbH44ywvNEDGEb0t_zLXzvyizQJTxRAAZrmvO-uqlj1Wlmah3SWc_7DrYuY9W63K1Rci9f-RCcpQt4qAK5AkXFaZvsxp5GyhkDxEnqyZgxLAFCwwcy-AueKiNceuduwIR24CGdERmMiHYO9Pi8GzoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسرائیل به شهرک‌های مفدون و نبطیه الفوقاء در جنوب لبنان حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67012" target="_blank">📅 23:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67011">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3Hm9v_UH6Pfhzq47wP6NmS5UO7FrDfR0n2lJHhyGNriPsaqRKTfP1cv-3--mhOziASD9-Wb3mhnn60Iksef6SeBG7-p0jMp35QdnbsoRn8E2Ml-3qyQQajqxP5FH3LgNqgYQORsS9MsuBNvJ8OlYR3u2IwDgztLgrnr10rq4gxHzruwecTzHpzdsvkFwar08Iltj4P6WCv2N--fgr-wZ30pfdGOkBoI0VlJ9bPNUOGpk-HCQTlUtAJGwZirjvozJStbbh-h7zOyGE9vEMlxmP_VkQO-mYa-BMKBW9rCcQ8ZE-d9flYZXOT1KV3k8UGWTdtgyJMvRGC2yzlak0rTPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67011" target="_blank">📅 22:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67009">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tLcbJ-rK0jpplPVpsymczV_FGx1-MTQSJjxfBMM5VzPG_5JFWR1ohS28KmF1SYGZL4ZhCx52aXRMH0Cv8ijswNDPEbKj8h5ZkX3tt1Bz14TPaAMT4MjeFHtknA3fVWiznRaIOFsjC3oWaXWd2IXDK-D9_uLGfARAYmfiVHZyUrtx9LRKWXevtnKAuKWb_Jjm_3L5OjT0ae5C3OPpZdkiwhMUsm9TlBxCWATNNI0025ADLvnXA2vEKaF9M2EQdYOYLaF1zf8Q95SbXvw-bWmgF0e8OekjekJWSWfWAR_ThB52up_ahCfwx1Xg4MhHOPV2_tvEN525t7vLR7VZwOGYAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7d35ea35af.mp4?token=aNFCV8EawDpR2wMS3EduiuJDPdMbsbk3Zo4ius-YPFDUElSmirKi5raxvwk0EFwqRuq953axEv_lfyBjjK0-9xT7gOUV-HVAMBe4FW4W76-DhHLRl5sGxrZnLCuj8JUpmACrU36eQQGoryWp1IYtfAdQ5kL_dpCXQ_O5o9aUEDJHyKpNLU_5u1n8YWmGTEbPInE3ZMpdlNgJ67n5Q-L_NKKPq8NbADyJBxpYKZmk3srUuLLCcHTxVOXHgz6QSWIzdk97x-HgzqTsuhQ10rHWPIbdzGPpiO3V4NkK-l9KKLE5GjUWLfKBoOJLf6l8qKAQezBuJB4XNA6nUa5uQPdFyw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7d35ea35af.mp4?token=aNFCV8EawDpR2wMS3EduiuJDPdMbsbk3Zo4ius-YPFDUElSmirKi5raxvwk0EFwqRuq953axEv_lfyBjjK0-9xT7gOUV-HVAMBe4FW4W76-DhHLRl5sGxrZnLCuj8JUpmACrU36eQQGoryWp1IYtfAdQ5kL_dpCXQ_O5o9aUEDJHyKpNLU_5u1n8YWmGTEbPInE3ZMpdlNgJ67n5Q-L_NKKPq8NbADyJBxpYKZmk3srUuLLCcHTxVOXHgz6QSWIzdk97x-HgzqTsuhQ10rHWPIbdzGPpiO3V4NkK-l9KKLE5GjUWLfKBoOJLf6l8qKAQezBuJB4XNA6nUa5uQPdFyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاری ندارم که حیوون خونگی این آقا مار کبراست! مشتی چطوری مار کبرارو قانع کردی چایی بخوره؟!
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67009" target="_blank">📅 22:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67008">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🇺🇸
یک مقام امریکایی:
هر شب رژیم ایران حداقل ۶ پهپاد را به سمت کشتی‌ها در تنگه هرمز شلیک می‌کند که برخی از آنها توسط ارتش ایالات متحده رهگیری می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67008" target="_blank">📅 21:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67007">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUWwMik75oftkumPYwQ3arJcoJQSUIkF__ptbZXLJQMZyh1Iz3qE9rLRCiQXJfPqlPPEWdifL1pVuqDyCO3PNKYqiAGg_UnkUdnyJ-44CELRosaTYgsu0jr3MBWmigZ54zTAvxoF6ba4I--kz2EX8vV1gLME7-BtGRgiWDqninmrpLKvNWI_0UEnj0JP3Mmnl0xLK3u3bk9eeD5P2Vya4SmOYyu9ZKl5arA07BKQTRQN1CDYaYvbr1Panc6XLYRMD-lI3MsEk1QJFHBssMYZCrJO8XxjQHUSwoRR38l4TmOnHQXYt751OU04i-uNaNWoZ7HCLDqllEIS4lNMawQkxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇱
نتانیاهو درباره ترکیه:
تقریباً هیچ روزی نمی‌گذرد که اردوغان خواستار نابودی دولت اسرائیل نشود.
ما این سخنان را بسیار جدی می‌گیریم، زیرا اگر یک چیز را از تاریخ مردم خود آموخته باشیم این است که وقتی کسی می‌گوید قصد نابودی شما را دارد، باید او را جدی گرفت.
ما این اظهارات را جدی می‌گیریم و آن‌ها را به اطلاع دوستان آمریکایی خود نیز خواهیم رساند. ما آن‌ها را نادیده نمی‌گیریم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67007" target="_blank">📅 20:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67006">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GSrsL2lts2MMzNlcM0emWF2MG2-Pcx3iLwh05G6W8AJlezge9Mi0whfRUY_oxXKjY-dBnqQpHH2fp_IwosgL8T8EYaZ_sRna-E65fZAJBO0-pgMJqYDG8uQyT-xnU9xRxjNsm6NCa_Cw_q0bBEXRmxiz6zy8Go53B7j4KmYpg-6t_DCQ7laTyPLrWoXG83oyIg8NnpDVEinmIcXf6zprw7HlbQyY2-v4_12mYrhVGclFeTP-9vFQx7w4rSqGFsTo2jOQZddvGcNmCzD8drebedC8DFgLwUv_R5sccqiaHdK3HSLMfsoj0UEqgvKbIDymCPg9M_10WVRPdq-voAlGZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:
آتش بس ایران و آمریکا در شکننده ترین حالت خودش. چون مذاکرات به شدت ضعیف شده و برگزاری دوربعدی بعید بنظر میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67006" target="_blank">📅 20:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67005">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
وال استریت ژورنال به نقل از منابع:
مذاکرات برنامه‌ریزی شده برای این هفته بین واشنگتن و تهران در سوئیس به دلیل تشدید درگیری‌ها متوقف شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67005" target="_blank">📅 20:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67004">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b64ee519f2.mp4?token=TQvFZeviHxAgEbow9zOWDfJ5-K30xlN6Wr5DDPqhkKelK0la0GjzU-_gOMFdRYrc1I09Za5bT8g3T8FeQd5L0E-fvdc3p2EubLxUtMxqzX2sywLA1qBYXosB08VvWG1ehlDJ7IXBug2XC7wJkR7LzLbk0puqBr2GPSVzTKPGEZBMVaEc0P89kkDa00VSJxyHjppgJG0TBDJKK3VothE-P3D2epI0FX-fKyzL4rpnQwXvMO7pVu7-QYIPvvU4zC7K42Lh-k1jBa79RZigOBSj2hjAo0ftf7wDDGMfCsmKgBPhJlwHdxZwMrdASsX4Ou6cuD09wCEqcrOYWDbxFUO2Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b64ee519f2.mp4?token=TQvFZeviHxAgEbow9zOWDfJ5-K30xlN6Wr5DDPqhkKelK0la0GjzU-_gOMFdRYrc1I09Za5bT8g3T8FeQd5L0E-fvdc3p2EubLxUtMxqzX2sywLA1qBYXosB08VvWG1ehlDJ7IXBug2XC7wJkR7LzLbk0puqBr2GPSVzTKPGEZBMVaEc0P89kkDa00VSJxyHjppgJG0TBDJKK3VothE-P3D2epI0FX-fKyzL4rpnQwXvMO7pVu7-QYIPvvU4zC7K42Lh-k1jBa79RZigOBSj2hjAo0ftf7wDDGMfCsmKgBPhJlwHdxZwMrdASsX4Ou6cuD09wCEqcrOYWDbxFUO2Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو سپاه از حمله موشکی دیشب
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67004" target="_blank">📅 19:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67003">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72a36c0ade.mp4?token=U1dUu22iluwpvhTRtc5VCFh8Bm_jN5dfUinxgdzjF1fTAKkxMl9Xl7NZikjFuFwy3ZrIW9D_dPTspxL189cJ46l-9NYN4l-9YKJ4DAu_LGkIUwdseZvorMcP7QJtzM5fXJDaJBuDaAsqYJOZ6nBp1Y_Lag-zvWs8Xkre0HFOtUWAe719x2l5AmzIgIG-Xq0Y5eG-OLOIGeFuKBW36yV9GhcnxrI0fMJzEpCaXa8K-aCzO2Bh5LVs3cc3dcpHNZjVC1zOAczWsQAqIeSk35bvEx_kRa0GNDIwhpWY4BO4n3UwKLmsF7ltvjNoSBeb4byDeThuQ-Gy70QIRRvsij_CEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72a36c0ade.mp4?token=U1dUu22iluwpvhTRtc5VCFh8Bm_jN5dfUinxgdzjF1fTAKkxMl9Xl7NZikjFuFwy3ZrIW9D_dPTspxL189cJ46l-9NYN4l-9YKJ4DAu_LGkIUwdseZvorMcP7QJtzM5fXJDaJBuDaAsqYJOZ6nBp1Y_Lag-zvWs8Xkre0HFOtUWAe719x2l5AmzIgIG-Xq0Y5eG-OLOIGeFuKBW36yV9GhcnxrI0fMJzEpCaXa8K-aCzO2Bh5LVs3cc3dcpHNZjVC1zOAczWsQAqIeSk35bvEx_kRa0GNDIwhpWY4BO4n3UwKLmsF7ltvjNoSBeb4byDeThuQ-Gy70QIRRvsij_CEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سنتکام:
ملوانان آمریکایی سوار بر ناو هواپیمابر یواس‌اس جورج اچ. دبلیو. بوش در حال انجام عملیات پروازی در حین عبور از دریای عرب هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67003" target="_blank">📅 19:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67002">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dcd7fa042.mp4?token=NoMo3mVJC5dfo_QUezlBcq4vrIw9JMX9tht-yQNtPpb1clGFtnSvgXATXWqrIA-kXA0_dGW1Hmt2vfgt7BwvsRfLjt0LlYyf3vVwvnrziuyPGsCsN-rWLn6B5O2A0kC5sbIy6CrxSt0_tCfX5fn4S-AKoGhEyGwummfTmfCHyEtUwqbWQMK63LyAZgTrbZNdArljVZgZZlKtT-A-ASDNrKYHwaED4A5oWhrOhGdNdfnkvzIlqKhaylJ7--u4mbbdtPWWZLicpvhbyYaCYNIND-scXDAVhayzBiCW_wAQ8v9IiRL_AdO3RBUtLvjOlCM6zyqkJzbUgXJ23sjf4uo3xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dcd7fa042.mp4?token=NoMo3mVJC5dfo_QUezlBcq4vrIw9JMX9tht-yQNtPpb1clGFtnSvgXATXWqrIA-kXA0_dGW1Hmt2vfgt7BwvsRfLjt0LlYyf3vVwvnrziuyPGsCsN-rWLn6B5O2A0kC5sbIy6CrxSt0_tCfX5fn4S-AKoGhEyGwummfTmfCHyEtUwqbWQMK63LyAZgTrbZNdArljVZgZZlKtT-A-ASDNrKYHwaED4A5oWhrOhGdNdfnkvzIlqKhaylJ7--u4mbbdtPWWZLicpvhbyYaCYNIND-scXDAVhayzBiCW_wAQ8v9IiRL_AdO3RBUtLvjOlCM6zyqkJzbUgXJ23sjf4uo3xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67002" target="_blank">📅 18:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67001">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6bc1a83a1.mp4?token=qHjzEl82MmYio766yQonHyGJiNtNsU7Nz2oPRosK079o9w-9v2WsMoUZdt1yzFJo4eTuUomCxAOUEs-VjcXtLSbr0T4uNQnWv2AMpcUrOZSDcKzrnYtfDO3Ezgr90LpFzUQjiqyizSwZVQuNVps-t5Y6B88wk4aBG1cpVq94J42IHeYSyfeB-eMfZo5w16iUq0zQonf-qVFeuIV31GtjRdopxK3vyWkc42EY6M09HTWfj_FhJHlZ5F9qwvLI5Ip7mSUq1AfWXAE6nM4PvNGB2y3uYjdcqaTEeiV96h20SUyDE7_s0U7lpxGNzrSeZNnHEg6kJg5JNcj_yZFfHNadNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6bc1a83a1.mp4?token=qHjzEl82MmYio766yQonHyGJiNtNsU7Nz2oPRosK079o9w-9v2WsMoUZdt1yzFJo4eTuUomCxAOUEs-VjcXtLSbr0T4uNQnWv2AMpcUrOZSDcKzrnYtfDO3Ezgr90LpFzUQjiqyizSwZVQuNVps-t5Y6B88wk4aBG1cpVq94J42IHeYSyfeB-eMfZo5w16iUq0zQonf-qVFeuIV31GtjRdopxK3vyWkc42EY6M09HTWfj_FhJHlZ5F9qwvLI5Ip7mSUq1AfWXAE6nM4PvNGB2y3uYjdcqaTEeiV96h20SUyDE7_s0U7lpxGNzrSeZNnHEg6kJg5JNcj_yZFfHNadNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67001" target="_blank">📅 18:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67000">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndJN5Def4Ux7l7VUdAxO1YAQZ420yh3Qq6-SfKEhL7jT6bgS9gE7lPOpByaPbj28vEofl65GzQoy8u8fog3bhLO0axhe2ic3ukL5JRegwiA-MmSuJeTd5xGLLIV3bbLv8jtLsv0ZZyy73wMrzYWM-am7d-iuncYgAyH8D4ZcRFCDT7Y-4NiJGFBRRJcr2lRrzlDYWr4Pb5UKQUovZbIPoM0_-Wq5VvtqgJRM1ltlthtrg_lj-EEIGP-R7ISMkxFzi_e3zCB1PkYQYl7JnbBrQs0u6dZ_46JQ3kIvD5_xNS5h7G5ayRGE1ug-hs4Gxg_th9idk7_RQiBE4TY3R9kCwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سخنگوی کمیسیون امنیت ملی مجلس:
پول‌های مسدودشده مردم در بانک‌های داخلی را آزاد کنید، خارجی پیشکش.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67000" target="_blank">📅 17:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66999">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c972b464a.mp4?token=Bqscph1SDCRqmZBSOz9GUcGFSzQ6TuZn86SHDBQmGhCs3Bn27hVqYKa-GkDfS59kPEKnlkB3sci_XgVGZGsY7nNx_bsuWAhLMHz0O1aI-6CSEOc_wHs26PHgOatx48ZyrnTWp8nIpOF9eiEmo2DZxOJ8nEv5pXeBei4Xi0Ywfz8YTFA8rSRDEf7AJobY5RLIcfFYS5K7VSxpChWtHUhfRR3OfT305Iy2_b0TT7k8MGG13dmjKw5A_xn8h74xHTIa2QC8f2KEOz6E2ZzohsaMuQWQ-y5aPhdYaBKGr8GZhbd1GZ1zb5LMnJSKoiMr8aNEnbA4OSgpBk-cQMg1oL1v3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c972b464a.mp4?token=Bqscph1SDCRqmZBSOz9GUcGFSzQ6TuZn86SHDBQmGhCs3Bn27hVqYKa-GkDfS59kPEKnlkB3sci_XgVGZGsY7nNx_bsuWAhLMHz0O1aI-6CSEOc_wHs26PHgOatx48ZyrnTWp8nIpOF9eiEmo2DZxOJ8nEv5pXeBei4Xi0Ywfz8YTFA8rSRDEf7AJobY5RLIcfFYS5K7VSxpChWtHUhfRR3OfT305Iy2_b0TT7k8MGG13dmjKw5A_xn8h74xHTIa2QC8f2KEOz6E2ZzohsaMuQWQ-y5aPhdYaBKGr8GZhbd1GZ1zb5LMnJSKoiMr8aNEnbA4OSgpBk-cQMg1oL1v3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عراقچی:«بر اساس تفاهم‌نامه، تنگه هرمز ظرف ۳۰ روز و تحت سازوکار مدیریتی مورد تصویب ایران، پس از رفع موانع از سوی جمهوری اسلامی ایران، به ظرفیت عملیاتی پیش از جنگ بازخواهد گشت.
🔴
این ترتیبات هم‌اکنون در حال اجراست و مسئولیت کامل آن صرفاً بر عهده جمهوری اسلامی ایران است. هیچ نهاد یا کشور دیگری در این زمینه مسئولیتی ندارد.
🔴
مطابق تفاهم‌نامه امضاشده میان ایران و ایالات متحده، هرگونه مداخله در این موضوع یا هرگونه تلاش برای ایجاد سازوکارهای جدید یا جداگانه، غیر از ترتیباتی که اکنون از سوی جمهوری اسلامی ایران در حال اجراست، تنها موجب پیچیده‌تر شدن وضعیت، به تأخیر افتادن بازگشایی تنگه هرمز و افزایش تنش‌ها خواهد شد.
🔴
همان‌گونه که طی دو شب گذشته شاهد بودیم، رخدادهای تنگه هرمز از پیش به افزایش تنش‌ها و رویارویی‌ها دامن زده است.
🔴
از همه طرف‌ها می‌خواهم در مدیریت تنگه هرمز یا در ترتیباتی که جمهوری اسلامی ایران برای بازگشایی آن در حال اجرا دارد، مداخله نکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66999" target="_blank">📅 17:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66998">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96542aaa83.mp4?token=fm8rJUUTFcg985-BGCrmHDXW7Ul5pEOehzgs7y7aiUHUv-EVaPWJ5DOw5P3bt9R09SROe8awcQ5sNF2yFJt_IoUsg-uDTbkUAsYgT_v8iFrrXkba1NJ6tSeNGSo5sPVdqrGDVOSZCv_LeV0_0rKTo-iAQI-hSP62lFDYaFAtDXL_fVbbjD9ot8kQiTvQI_LdrSsx80Dbt5nVSLsz_uzyvzNJa1Evxkc-LZ1FL8PbkTGttXrti-YYu70BqoPKIlKjIEjNS2csTv-3ZTWEEPMuhZuW3iQ4BSyjnIbYDCSaE_YlDe9Q_8vxbLNqEMcRO7rTmPT66JrZd7_m2roAy74qQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96542aaa83.mp4?token=fm8rJUUTFcg985-BGCrmHDXW7Ul5pEOehzgs7y7aiUHUv-EVaPWJ5DOw5P3bt9R09SROe8awcQ5sNF2yFJt_IoUsg-uDTbkUAsYgT_v8iFrrXkba1NJ6tSeNGSo5sPVdqrGDVOSZCv_LeV0_0rKTo-iAQI-hSP62lFDYaFAtDXL_fVbbjD9ot8kQiTvQI_LdrSsx80Dbt5nVSLsz_uzyvzNJa1Evxkc-LZ1FL8PbkTGttXrti-YYu70BqoPKIlKjIEjNS2csTv-3ZTWEEPMuhZuW3iQ4BSyjnIbYDCSaE_YlDe9Q_8vxbLNqEMcRO7rTmPT66JrZd7_m2roAy74qQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
نتانیاهو:
می‌خواهم به شما یادآوری کنم که در لبنان چه بود. حزب‌الله ۱۵۰٬۰۰۰ موشک و راکت داشت. و ما حدود ۹۰٪ از این انبار عظیم را از بین بردیم.
ما آنها را با بیپرها شوکه کردیم، نصرالله را از بین بردیم، فرماندهان نیروی رضوان را کشتیم.
فقط در دو هفته گذشته بیش از ۲۰۰ تروریست را کشتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66998" target="_blank">📅 16:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66993">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c6c8KTz6OJ7LDBDCMzW0J7vu8lbmc8hwXg700sH-5TT0lM6_4U2z6B0ZNzR9AJDCNKljYPBbTZtgQYGBNOo8meIdgcOq89YhW8mNv-9_bCjvuJlu4bQSF-bOQ2lQb8hkH46bzZqpTT11L8PzXyGfn7t6YnXuJEoxbeVdd46yomVf9B1fw-aHyfUQV1094scEGk6zc49HMaVp3xZfuRC9_isB2GszQH_elCl8iZWcih1WPetfsmtmXvbeAig084fdxKJ9Iwv8MeU-GsT26XY8dwPzixtfqAaImyPXo8BDmrXQ2pZJH53pIeekBbVfQIJHUunwD13oTHUAAzENPdPZ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cxJEQLTs97wm-fOKUP460iId2Amkdf2ZoG_l2yDijRKSnh_nCywE0RkGQnWe8r8F5J8MqXZHWejg9hql2SpsnJFo5v3TrksixFkh2lW6uMLXABh5CLzLRTyjDc7vTPYSXAY3SmDlQ1PxDlZ12fM_uE6gQcJsoCDrH5Z7HAsnm8LLFYaMSwut26BVP0-NGzg8hHdPnJjDwzvO3TXvrvFNEO6EZj2xUZGtomWpNQSp-TTCEOJh13Ya8_a7wUV0Wu5OlARAmwz_047PjLFNtuypAi9rc53TeyCq2Bny3fpJ_ldDuRj7rB9fN9no5qQCQ9joEVwKHIUmzg_crW6tpsD5VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/STw4XZprvTMpG3ywfMQ9BZnZIhD3PYNETPioPRRs7G-8XcluCHp1lEYJqGOydGr_iiBVughHpWKmX9PrdwFVYz2k3EF-1ongNG3dUWmvh28qaUSvI7m-ZX0IB7wy5Ay8y8zsU0II-ydXW0G9IRXAkc6wnVQq0dFDlyhOW9wnXfxkYs21DMu7YWRCO88NMxwLPKwLQSmKQeWGlg85Av9Ff26cSbBd54FuOdWflup83cVIkM2JCLamjGgqS6gfcwqNovEBXY7Y_07RMmQqzKDSbs3NbP78STXm7oxOWuzhY2lwtTjyVUfz0fg4s1aTqfT6JLbnk8xdCLcZVw48Sp7mnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2d278e2c9.mp4?token=Y9ha03C8sEdkfQ58cLQSwlFA2BbKdlztbUL_QhyV9zG1bmL0sKfCEVvNOxT_errtIRDY8-bz_FFuve__GpppB3mveK4XOID_O7ixDFAzXHVTVa4dpWIEKfo9n4HkTqxceU_CtuZuHEcFKaIj0IMLuD-5dnDetNwE7QWc2kQoiDLUBhz6HwMZQWgxvvlurxipm5WQ0MUfspvhwgwOmPWjCNnjNADid5iTr6lL9rh_Gcz4tordZJ09TPlj7fVs2YqQsM7h3AVoTCYCq3hIPzXrhNVGiVxFSDmNMaFKYhSdlz0F1XyEuZIWTTcGui-7_5hZ9Dz4_RKQh3gQ86C9rbl-Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2d278e2c9.mp4?token=Y9ha03C8sEdkfQ58cLQSwlFA2BbKdlztbUL_QhyV9zG1bmL0sKfCEVvNOxT_errtIRDY8-bz_FFuve__GpppB3mveK4XOID_O7ixDFAzXHVTVa4dpWIEKfo9n4HkTqxceU_CtuZuHEcFKaIj0IMLuD-5dnDetNwE7QWc2kQoiDLUBhz6HwMZQWgxvvlurxipm5WQ0MUfspvhwgwOmPWjCNnjNADid5iTr6lL9rh_Gcz4tordZJ09TPlj7fVs2YqQsM7h3AVoTCYCq3hIPzXrhNVGiVxFSDmNMaFKYhSdlz0F1XyEuZIWTTcGui-7_5hZ9Dz4_RKQh3gQ86C9rbl-Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بیاین یه نگاهی بندازیم ببینیم چه بلایی سر تیم به‌ظاهر ملی اومد؛ قبلش بریم سراغ مصاحبه های بازیکنان این تیم تو تجمعات شبانه حکومتی‌ها:
شجاع خلیل زاده :
حسم نسبت به رهبر شهید ؟ افتخار ایران ؛ گل اگه زدم به رهبر و شهدا تقدیم میکنم
رهبر عزیزمون شهید شد همون چیزی که خودش میخواست بهش رسید
گل بزنم به  رهبر شهیدم تقدیم میکنم و ما فوتبالیست ها همه دوستش داشتیم ، افتخار نداشتم با رهبر دیدار داشته باشم و دوستش دارم
حسین کنعانی :
حسم نسبت به سید مجید نقطه زن ؟ بزن که خوب میزنی ،حسم نسبت به رهبر ؟ بزرگی
رامین رضاییان :
شهادت رهبر انقلاب رو تسلیت میگم تو تیم ملی به عنوان سرباز برای کشورم می جنگم
اتفاقات داخل ایران { دی ماه } به خودمون ربط داره و به خارجیا ربطی نداره
علیرضا بیرانوند:
چه بهتر که تو آمریکا بازی کنیم می‌تونیم تو اون کشور برای اولین بار در تاریخ فوتبال کشورمون به دور بعد جام  جهانی صعود کنیم
روزبه چشمی :
حسم به رهبر شهید ؟ بزرگ همه مردم ایران !
سعادت دیدار با رهبر عزیزمون نداشتیم ولی بزرگ همه مردم بودن و این راهی که مردم دارن میرن ادامه راه ایشونه
و بعد از این اظهار نظر ها بریم سراغ دیدن نتایج، تو بازی اول از ضعیف ترین تیم جام یعنی نیوزیلند دوبار عقب افتادن و در نهایت با سختی یک امتیاز کسب کردند، تو بازی دوم فقط چند سانتی‌متر از باسن مهدی طارمی تو آفساید بود و گلش مقابل بلژیک مردود شد، تو بازی سوم بازم همون طارمی پنالتی رو خراب کرد و در دقیقه ۹۳ شجاع خلیل‌زاده گل زد و خوشحالی‌ای کرد که در تمام جهان سوژه شد، ولی بعد از چند ثانیه کل دنیا روی سرش خراب شد چون فقط دستش ۵ سانتی‌متر تو آفساید بود، نکته جالب اینه که شجاع گفته بود گلم رو تقدیم به رهبر جمهوری اسلامی خواهم کرد
دقت کنید برای اولین بار در تاریخ این جام جهانی ۴۸ تیمی بود و ۳۲ تیم صعود می‌کنند، یعنی در واقع به اندازه‌ی همه‌ی تیم های حاضر در جام های جهانی قبلی، این بار تیم‌ها به دور بعد صعود می‌کردند (علاوه بر تیم های اول و دوم، هشت تیم سوم هم صعود می‌کنه) و بعد از مساوی با مصر، سه شرط برای صعود تیم به‌ظاهر ملی وجود داشت:
۱.بردغنا
۲.نباختن ازبکستان
۳.مساوی نشدن بازی الجزایر و اتریش
ولی در کمال تعجب یک معجزه رخ داد، غنا نبرد، ازبکستان باخت، و در دقیقه ۹۴ بازی الجزایر، ج.ا صعود کرد و در دقیقه ۹۵ با گل اتریش، ج.ا حذف شد، این واقعا یکی از بزرگترین تحقیر های تاریخ بود
...
می‌بینم یک سری افراد با توجیه های احمقانه می‌گن اینا مجبورن و فلان، نه عزیزان دارین اشباه می‌کنید، میانگین سنی این بازیکنا بالای سی ساله و عملا فوتبالشون تموم شده و رسیدن به آخر خط، اینا فقط دنبال باج حکومتی‌ان و حکومت به عنوان حق‌السکوت بهشون مجوز واردات خودروی لوکس می‌ده که می‌تونن ۱۰۰ میلیارد ازش سود کنن، یعنی عملا یک رانت ۵۷۰ هزار دلاری هر شخص بابت حق‌السکوت دریافت می‌کنه، جالبه که تیم های بزرگ جهان مثل آلمان و اسپانیا حتی اگه تیمشون قهرمان هم بشه مبلغ کمتری رو می‌دن به بازیکنا (۴۳۰ هزار دلار)، خلاصه که جام جهانی بزرگترین رویداد برای شنیدن صدای مردم مظلومه، همونطور که تو سال ۱۹۷۸ کاراسکوسا کاپیتان آرژانتین بخاطر جنایت های حکومتش از تیم ملی استعفا داد و...
ودرآخر، از اون ضربه‌ی تیر دقیقه ی ۱۲۰ جهانبخش تو جام ملت ها، تا پنالتی‌ای که طارمی خراب، تا پنج سانتی که شجاع تو آفساید بود، از پنج سانتی که بازیکن کنگو جلو ازبکستان تو آفساید نبود، از پرچم کرنر تو بازی الجزایر، از گل دقیقه ۹۴ الجزایر تا گل دقیقه ۹۵ اتریش، هیچکدوم اتفاقی نبود و همشون کارما بود، کارمای حرفایی که نباید می‌زدین و زدین، کارمای کارایی که نباید می‌کردین و کردین، اینا همه صداهای مردم و آه‌ناله هاشون تو گوشتونه، مردمی که دلشون باهاتون صاف نیست، حالا هی بیاین بگید تبانی بود، نه تبانی نبود، اون بالاسری خواست تا شما به عنوان بی‌غیرت ترین و بی‌شرف ترین نسل تاریخ ایران با حقارت‌آمیز ترین نحوه‌ی تاریخ از جام جهانی حذف بشید :)
#hjAly‌
@HutNewsPlus
|
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66993" target="_blank">📅 16:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66992">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVXfZtWWB47FSupw4Fxr5Ad3ZE-Nq6cUJO-cFn8TE077T9MlPTqt2NCtc0v4pCm-xsuDJwfSoP2gNiuAZp60x7Am-hinZgLmxlT9S5z-KQAsqAbfrXUhmPsx3puRRWMgzuDX_2fUlBZvW1m0e5XKyelonEKeaOCjfP8vcQ_gwyhNvZFmBT8faWoht9rcCXubWYspbJ7DRxPxeYxzaL4iiDGY-mxitbc9QCiZjaTVILD3aCDUpD9x8HDIj2gQHDxmgf2rhCNEEgTdiubO24Kmkp6YhUnxfPIVhWM74sX7iDOPbJdw0x8S_kHhHgAEPICO-2WFO0JGedF2FMlHjlK3ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواداران حزب‌الله دیشب تابلوهای «لبنان اول» را در جاده منتهی به فرودگاه بیروت به آتش کشیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66992" target="_blank">📅 16:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66991">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHossein ️</strong></div>
<div class="tg-text">🇨🇭
ایران - سوئیس
🇮🇷
مرحله حذفی یک شانزدهم جام جهانی
سشنبه ساعت ۲۰:۳۰
محل بازی : گیم نت محلمون در بازی اف سی۲۶</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66991" target="_blank">📅 15:31 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
