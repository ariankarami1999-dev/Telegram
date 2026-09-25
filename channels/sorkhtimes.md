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
<img src="https://cdn4.telesco.pe/file/I3XoE5Jrmthih7A1pJL6jF6f3e2EDdLoYHytAIj4Ap9HOBFd33c5dMailTNCtk2kb5IQG3I5432mK7b5vevF6bjwMPgccvMZtMcXcmLDalrIWt4ynGrxTp-G89PDrb8QyQnLBscgV320KsO3ixzPU7U9euULkiNoeJ2TUF-BFB0TJz5oHcD1et2mg0gpSN96EzZjt_Tze81Du7Rxe9gEKC_LFEoRUR-Y9LvprpiI-4XtrdWLzfBgC3TPMxIop2NMkLR1Vt3BSvSR3UigLiYH9wi4brpHJfV6x8AQmHHKunPERBjCnM5EiDoMSKDzOoNGh26ySH0R-BPokiarVRw-4Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-03 20:53:33</div>
<hr>

<div class="tg-post" id="msg-140537">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
فوری از قدوسی: قربانی به شدت تمایل داره پرسپولیسی بشه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 969 · <a href="https://t.me/SorkhTimes/140537" target="_blank">📅 20:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140536">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✔️
✔️
غایبان پرسپولیس در دیدار دوستانه امروز
⏺
حسین کنعانی، علیپور، عمری، ابوالفضل جلالی و حسین ابرقویی، باکیچ، ارونوف، نیازمند، زارع، محبی، محمودی، ایری، لطیفی فر و شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/140536" target="_blank">📅 20:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140535">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsk4D9cYZ9Ce-26zH5V8yGI3AVv3qOe-SP8Z6egUxujjiEdfukpjs3f58QkyHIRVw1izT0YbdlddNCoM2PEVdFjsr3DkrpnHjqh0AZl_0Yf1E9TgsKxudFAlWgVHC8T9FcGlAeT8TRzvmG38njMsyrY3eHrSYgADnwdPz7ug4U1xCZdbpJT6V4PLCgrWmbb6LA0hGz8QLzrA6LbBOaUVKSPvZCUOs_9So75MOYBRgN5-o91GTu1UxelK9SMbg2DUFJipSE1PZxrgAUU8Lm74WzF0ziX8aX4umRS2lkZK-HADnaUMg_KbtgXP6C6HVp5H2JWyYgK16li7o6Gum5g4ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
ترکیه - فرانسه؛ جدال پرتنش در قلب استانبول!
[
ترکیه
🇹🇷
🆚
🇫🇷
فرانسه
]
⚽️
ترکیه در خانه با تکیه بر فشار و انتقال سریع می‌تواند فرانسه را تحت فشار بگذارد، اما غیبت چالهان‌اوغلو و ییلدیز روی تعادل تهاجمی میزبان اثر دارد. فرانسه با حضور امباپه، دمبله و اولیسه از نظر کیفیت فردی دست بالاتری دارد، هرچند اولین بازی زیدان و تغییرات ترکیب دفاعی می‌تواند هماهنگی را تحت تأثیر قرار دهد. باتوجه به فرم دو تیم، بازی می‌تواند نزدیک و پرموقعیت باشد.
سناریوی محتمل: گلزنی هر دو تیم و برتری نزدیک فرانسه.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/SorkhTimes/140535" target="_blank">📅 20:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140534">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f84e7380b8.mp4?token=i2tpzbKET_aiFwyfccCTDrz4QLf360OHpAGCSUiG-7nVepDOOGLdzRE9JujGhVjjmGDsrKpgy5cgOby6q2DoXriFNFiUoniPvm2yJUwRmqKfFLI_uTAWPULpDUmBuwNm_HkW-gpHgl08EqmltpZfxS4NuU0tR8DVbzahht5yv-aOy9MYNE_k6n9ONt8wNUAJpUf3nBphebNbO2I2wN0LceHO490QVlGe72CcgKimtCV7YaDxLqj3LrGaN0enW4qH9vZh7sHJzqc4HcvTAhqgePQMr6uJxlpLmfH_1zmUszZqac9AOUb-J6_REWmabHRNmkfMPqKsxpNcG3KKAylfM72bhP-94jCi4NQuPS0K4GvMwyxcGCsDFJ0fo7ZZy38Ijkd7Nc8puSrDCAVPec4kDqwlkElo0i4r9LUe6V9OKUC977wUG3zvaWiDn5i45gOO5W-G_1Qz5WRpZWh0sRMhWpTwlEaqYNyXSGgmFIu2WM_fP_WLkiT2L3KlAcCUMAu1cS1Fb9Lx3LlWzgcJUVvJbxBUYei635fRL4ZKPturu19cu3Kht7rMa_hU95D8YcbJ_Zk63kEJPAUaMXR_p27FtUhNs22c1urwv9PtMlXJoXz26NBJ1RFA0D_hvI_gtaZw2xQLlFt91H97t5TJoKFHbyu76GiT5AKg7Z98gRmDAvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f84e7380b8.mp4?token=i2tpzbKET_aiFwyfccCTDrz4QLf360OHpAGCSUiG-7nVepDOOGLdzRE9JujGhVjjmGDsrKpgy5cgOby6q2DoXriFNFiUoniPvm2yJUwRmqKfFLI_uTAWPULpDUmBuwNm_HkW-gpHgl08EqmltpZfxS4NuU0tR8DVbzahht5yv-aOy9MYNE_k6n9ONt8wNUAJpUf3nBphebNbO2I2wN0LceHO490QVlGe72CcgKimtCV7YaDxLqj3LrGaN0enW4qH9vZh7sHJzqc4HcvTAhqgePQMr6uJxlpLmfH_1zmUszZqac9AOUb-J6_REWmabHRNmkfMPqKsxpNcG3KKAylfM72bhP-94jCi4NQuPS0K4GvMwyxcGCsDFJ0fo7ZZy38Ijkd7Nc8puSrDCAVPec4kDqwlkElo0i4r9LUe6V9OKUC977wUG3zvaWiDn5i45gOO5W-G_1Qz5WRpZWh0sRMhWpTwlEaqYNyXSGgmFIu2WM_fP_WLkiT2L3KlAcCUMAu1cS1Fb9Lx3LlWzgcJUVvJbxBUYei635fRL4ZKPturu19cu3Kht7rMa_hU95D8YcbJ_Zk63kEJPAUaMXR_p27FtUhNs22c1urwv9PtMlXJoXz26NBJ1RFA0D_hvI_gtaZw2xQLlFt91H97t5TJoKFHbyu76GiT5AKg7Z98gRmDAvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
صحبت‌های کنایه‌آمیز توتونچی، مجری برنامه شب‌های فوتبالی به تیم‌ ملی فوتبال: دمتان گرم! در کمتر از 48 ساعت 7 گل از کره شمالی و ازبکستان خوردیم..!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/SorkhTimes/140534" target="_blank">📅 19:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140533">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
❌
❌
❌
شاگردان مهدی‌تارتار درپرسپولیس امروز عصر در دیداری دوستانه یک‌برصفربازی رو به چادرملو واگذار کرد. علیپور بدلیل مصدومیت دراین‌بازی غایب بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/SorkhTimes/140533" target="_blank">📅 19:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140532">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
❌
❌
❌
شاگردان مهدی‌تارتار درپرسپولیس امروز عصر در دیداری دوستانه یک‌برصفربازی رو به چادرملو واگذار کرد. علیپور بدلیل مصدومیت دراین‌بازی غایب بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/SorkhTimes/140532" target="_blank">📅 19:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140531">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18169032d.mp4?token=aQ-V_51O5Q5U87qkbXQaby-VhJkSKvdjRsjDCuUA4a1nsl8XOnMSZc4nX9Y_9YshbWB-RqRPHssCyy8fxiUtH7Jb8j7FHwJnjyPtKt7vYOEWmATDt0opXK_f986BAk89awvdDxqxKzoJf15RYtrGWP-QssSDKoOh-YKP_Prrx3s0DMsfvOWAzNmRaqJcCBsCOjJpvYQ5-hZwgn_s3wOUCoZXhDxPoHvnlraECmy9ndlFuIYTcQIdnTtTYTGYewmeYBPzNl_vBlqz_safBH-p5aJzgdbVdAyHvkdS9xh1cF3-sDBiNOhXLJvm8OC1CFywe37xJM3XYsanPJjyVYUQyTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18169032d.mp4?token=aQ-V_51O5Q5U87qkbXQaby-VhJkSKvdjRsjDCuUA4a1nsl8XOnMSZc4nX9Y_9YshbWB-RqRPHssCyy8fxiUtH7Jb8j7FHwJnjyPtKt7vYOEWmATDt0opXK_f986BAk89awvdDxqxKzoJf15RYtrGWP-QssSDKoOh-YKP_Prrx3s0DMsfvOWAzNmRaqJcCBsCOjJpvYQ5-hZwgn_s3wOUCoZXhDxPoHvnlraECmy9ndlFuIYTcQIdnTtTYTGYewmeYBPzNl_vBlqz_safBH-p5aJzgdbVdAyHvkdS9xh1cF3-sDBiNOhXLJvm8OC1CFywe37xJM3XYsanPJjyVYUQyTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
گل های بازی بانوان پرسپولیس چهار - صفر ملوان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/SorkhTimes/140531" target="_blank">📅 19:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140530">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
❌
پایان نیمه نخست  بازی دوستانه
✔️
پرسپولیس صفر ـ چادرملو صفر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/SorkhTimes/140530" target="_blank">📅 19:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140529">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🖼
عکس تیمی پرسپولیس پیش از دیدار تدارکاتی با چادرملو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/140529" target="_blank">📅 17:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140528">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMnY55FD0U6WJt3k5CkKUwRiQtwRI6zpn-xBQ2gTwm5r2ZoroY3x2gU-67pQcjyLKf53vzjyRYgoXlGM0pQ2kWBPAil7FV1-MRUleH_zOZHwbJEjwLHuHj7bISHTgXYlUSnqlz28mWbCqnnja5LvjSvIq8YNEfHKSyQPY9yoApItqkwdTEsP_ct42LPUHVO0zDvllUJ7_AhIeqim2dpVH5v6-T-32UukdjIoVz_JnClgV0x3egKQJt7TfI-VfeA-wlv7cyjSHJRSK2VXrKxqL1DDQ64M7PVzyNLWGt0uXR0T8a0Vgrj-DHb6V5txSPGIec8PZlIwGvcrDaxTpzXZTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
پیمان حدادی که بازی پرسپولیس و چادرملو را در ورزشگاه کاظمی تماشا می‌کرد همزمان بازی تیم فوتبال بانوان پرسپولیس با ملوان رو هم با گوشی دنبال می‌کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/140528" target="_blank">📅 17:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140527">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFo4YSaVPVD2ha48NuS_aMr71zzL7dRbsSUg3M-pt2LFHtwUo3VPmVF9qAtw44xyJehqNeWi6jYOGREhyDbTifRJJS_PMM19QYsKyAkmWZWJVat6sMarSmom82dNdvsF5umRgSfnMmpARgR8ejTuheLxHYyAPvRkzVA6_nWbr41r-_YNGxbsqmUmdJ6EYBcMy5N_eH3ms8QQRtDNYpbOrNF7L2wtsKc8tGehytZiZH3yyXQhcFdD5b72k3edSWDmFtw7hgqGDjXDf9FNkVeUcrKShBBNbSejN2HJYn99ikB51j2y9VFm5OHlR_KDZEkQjjqXmAN-kCPR1jyJ_JxARw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عکس تیمی پرسپولیس پیش از دیدار تدارکاتی با چادرملو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SorkhTimes/140527" target="_blank">📅 17:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140526">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
پرسپولیس فردا بعدازظهر در دیداری تدارکاتی به مصاف چادرملوی اردکان می‌رود. با تصمیم کادر فنی دو تیم این بازی پشت درهای بسته برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/140526" target="_blank">📅 17:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140525">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOYW4-o5Dboz_tQeDnDY-fcjultnPXVeqscSLZ7cD46t-try1DeweNH8XQYnge554l1hCTcm1QfKseys7CFssvEG7gG-oMWYOBdMaQkokReBfJD7H3sx29Ayh6fxfuFDjn4dNKDbrzLjlHNqp06poX93nJPNGtg0bVFimlIGoK4OcMVmrLBabOYwJ9dxHMxsmps5zaMUISrVbwPx3E4d-3_AzaXvtc5B4L3ZV8XzTojHLmQNcRhoz_xhSC1Q16hbPCTJYkHDezXHgYMJLkCkxFAliucowdKHgTQxmq_eY4BERHUrlRyrUSPaB9E9BG-5AW-rAO-RtqC3PnyrrIDdKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با توجه به حذف دیروز امیدها؛
❌
❌
میراثِ قهرمانی «برانکو» با تیم امید در بازی‌های آسیایی بوسان ۲۰۰۲ دست‌نخورده باقی ماند...
❌
❌
این آخرین قهرمانی امیدهای ایران بود و ۲۴ ساله هرگز دیگه هیچ مربی نتونسته تکرارش بکنه تا بزرگی کار برانکوِ کبیر بیشتر به چشم بیاد...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/140525" target="_blank">📅 15:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140524">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🇮🇷
🎙
جواد خیابانی: تا دلتون بخواد تیم ملی با قلعه‌نویی به ازبکستان باخته. سال به سال دریغ از پارسال. تیم از جام جهانی حذف شد، رفتن فرودگاه استقبال!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/140524" target="_blank">📅 15:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140523">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
🤩
فرهیختگان: بزودی قرارداد اوستون اورونوف با پرسپولیس با دستمزد 2.2 میلیون دلاری تمدید خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/140523" target="_blank">📅 14:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140522">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUMz-Onh-CnYNf6Qmc6vLICKwtC13UyLvxhNyCkPV-8RKWNNwB7_DtIN9_2vVLE7WdV82VuZ7jHZMD7hVH8NWGYJ1CSC6zDyn2U3OvuxvJc_fqAUMGxU7VJREBO6OUsJ8GRHIqf6-EwZCMCFb30By3UNTg11pvs2A-6O4t1VNUcDTPTuvwqdAPComgcQO4OjdOHvZEAwgJyIErQWyT_ALEf19BLjFqW0c5f7SYYz0LgfhxSbi5TwPnMLHxSC_HUw7gONAu6H_neTLHO-VC_b6_3Gwsk7sOsHxquhxk3qf9yU716Bm_O7UA96uGnCI9b7sxgtEJtPiWPLlFaO_PG_RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری؛ ترامپ: تمایل دارم با دکتر پزشکیان در سازمان ملل دیدار کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/140522" target="_blank">📅 14:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140521">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
حسین عبدی بعد از بازگشت تیم امید به ایران و در فرودگاه از سرمربیگری این تیم استعفا و اعلام کرد که دست فدراسیون فوتبال را برای انتخاب مربی باز می‌گذارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/140521" target="_blank">📅 14:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140520">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🤝
🤝
مدیربرنامه‌های فرهان جعفری: فرهان اوایل دی‌ سربازی‌‌اش به‌پایان‌ میرسه و میخوایم توافقی که هم منافع او حفظ شود هم منافع باشگاه خوب ملوان حفظ شود از این تیم جدا شیم.
❌
❌
فرهان از دو باشگاه پرسپولیس و استقلال آفر دریافت کرده و در پنجره نیم فصل راهی یکی از…</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/140520" target="_blank">📅 13:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140519">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e518e3928.mp4?token=IkJao9nsE5AETuvWqoOHKKqL5uohdfGkdEyxaMxUuSDbFx0ZWQpMRGpUgJ9EeHja3-ymTVZgw04M9yZ4f7oVt0iCLj9X-Mc5OAKDJmFHF11tLezdopG_aEyP29dzSsju0RXYkMhyUqtbg9ztX3lBvXCE6rt5IFz7Vif0aoPe6piekS7ivbaFQEZBfp6g76XxV1wwyiS_cgt5G_Lk0p4XEDF4oX2rZd39sa5wb6DqtNCNEMMc0UFE-A3cSX_8jLvXxoTrovhkvoNIDlFdDDDIxl-q9sLX_OP2Gmygm4Oq8SY4yM1uTr7UcprSDhMiuG7GpJu2fQInEatOykGKfdBjIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e518e3928.mp4?token=IkJao9nsE5AETuvWqoOHKKqL5uohdfGkdEyxaMxUuSDbFx0ZWQpMRGpUgJ9EeHja3-ymTVZgw04M9yZ4f7oVt0iCLj9X-Mc5OAKDJmFHF11tLezdopG_aEyP29dzSsju0RXYkMhyUqtbg9ztX3lBvXCE6rt5IFz7Vif0aoPe6piekS7ivbaFQEZBfp6g76XxV1wwyiS_cgt5G_Lk0p4XEDF4oX2rZd39sa5wb6DqtNCNEMMc0UFE-A3cSX_8jLvXxoTrovhkvoNIDlFdDDDIxl-q9sLX_OP2Gmygm4Oq8SY4yM1uTr7UcprSDhMiuG7GpJu2fQInEatOykGKfdBjIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🟥
بازیکن تیم‌ملی اسرائیل دیشب بخاطر این شادی بعد گل مقابل اتریش با کارت قرمز اخراج شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/140519" target="_blank">📅 13:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140518">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bk5AtxITBzRZKHoSK2Btuhqk8hx6SE1Q3My2aepaul58H38KhUytatgJvsTdza9a_Sgc8ey76W0b4Zseh0UM8z6_yEvCzI0flinfudFt3kmHlLbF6uK8mYxb2ihH0pzrrXmdyposY80V8Ce0jNS3rrV1T1gnxp7CAoSBmTS2bVLXVb6asyewKlHuR4RvVl7LcdW-lzx43xvbyZm7WHjV1t3eM11MwmqxMm-5CqrSefm7SmK1pZZQ6lvC1M9lJtWID4iUUrt0OyJJ_gISgFPhXhJhqb8PArSBWbYtGtj1XvHYP5e6zLctiwfzzu_FrsBbwLil3vyJbhWVysX0gnBYQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
🚨
✅
⭕️
⭕️
⭕️
با تصویب شهرداری نوشهر؛ امتیاز لیگ دویی این تیم به پرسپولیس تهران واگذار شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/140518" target="_blank">📅 13:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140517">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
❌
جواد نکونام؛ مهدی ترابی به دیدار حساس‌فردا باپرسپولیس رسید اما مهدی هاشم نژاد بدلیل مصدومیت این دیدار رو از دست داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/140517" target="_blank">📅 13:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140516">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQVco_iTzYhGquu7alOG02Lew4lV5_8FB9_zEL5M8A-eMOKn2LEhjMAPNv1SI9WKKmVI3KJ-DaD0g5n6OG3GVSNqTLbWfE0svDLKWr-KT6Iz7H_zsBwvl7ds19xv9CZMEEzz6mXgAs_-UBcaF6duPEo_qh9LPr4Y2JWizwrn_7L-VZU6ByHxc07VpFiX9vYXVw_e9zdBMo1XxSAAYddV20_spasTHBclDph9q0ssY7IassZrZom_ASD6mKjDoHJcklAJ0CPBbWj_T4f56yC3bEeX9zGt5l87UMmq9KDK4NGnHF185gOvH3GyDHzSiEvk1IV8U4Nr_6OyEyou3ky9Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
گاریدو یکی از گزینه‌های تیم‌ملی برای
جانشینی امیر قلعه‌نوعی هستش
😐
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/140516" target="_blank">📅 11:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140515">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">⭕️
⭕️
#فوری | ترامپ:
🔻
مقامات آمریکایی به مدت سه ساعت با یک هیئت ایرانی دیدار کردند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/140515" target="_blank">📅 11:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140514">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
✔️
✔️
محمدحسین صادقی، وینگر ۲۲ ساله پرسپولیس، در نیم‌فصل به‌صورت قرضی از این تیم جدا خواهد شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/140514" target="_blank">📅 11:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140513">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">⚪️
⚪️
⚪️
مهدی تیکدری در غم از دست  دادن دایی خود عزادار شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/140513" target="_blank">📅 11:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140512">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
تیکدری بازیکن پرسپولیس: مهدی تارتار یک مربی بی نظیر است  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/140512" target="_blank">📅 11:49 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140511">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDIIInCvG8WoAfkPKZJDD7ppffH3zEw1T9XK6L_hpfWF6fgL-SwGVKsWChiCUlhkhgjZEO1WNQMLf_rKmW_NITbI8PX2dXtgg3IqaRg-qS_5a7Q-flrHEGdZxmxGctH44Kg3wSg__K0w4-kRCDS1VQrNotItnbMQEv9Eib2F0uarnq2JuEETyjS2CSYMZueIMQJq2xRVPnqE5S-2UDuG0L3lwba6j3oXx1St1-XhOKcJ2qz8x8BGOI6uzgDgIZagORLQifbLqV12g71ek3-I-G8OlqkK__DP9JkE0c5b6HMOWzFyCUL1wOUoZL3L5rfCTiZsTZ9XYYBnKmcABqmECQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
پرسپولیس قید جذب اندونگ رو زد
🔻
باشگاه پرسپولیس به خاطر ریسک بالای این انتقال و دور بودن اندونگ از شرایط بازی، تصمیم گرفت بی‌خیال جذب این هافبک گابنی بشه
🔻
طبق شنیده‌ها، تا این لحظه تراکتور تنها تیمیه که همچنان دنبال جذب اندونگه و نکونام هم روی این انتقال اصرار داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/140511" target="_blank">📅 10:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140510">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZ9MpOB_nYei_tt5npUQ7VthhY1nXlES5CWoYqL7dmBCctb7mEDcWwoWA5h6Kc-pq85aClhs6sn6TdYqMdnB3zYt-je7M0QfMwwjEWn9Z9n8LPKDLP86wVlBcyzJYXOCqXn3aPahfxmWqW4JDyrn9oWbExri2BfYUPoe1mgUOjXg7kGrvIw7qaW1nCWHEXQGrAt1ZgI5d3XGzPO82rKx1x7XXcWyv_j7SMj-MUX05leHvAoxJqJQDtFNtxaBuGgQ4qGcUsEnORFrQhqIXfqoADoCvBEV9Yew7Ug6POJIzF2mbTy8rf9WBG6ZJcz7QdjV7r1KVYIZXrYpTBcEk5xS5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
علیپور و کنعانی‌زادگان ابتدای هفته آینده تست پزشکی می‌دهند
✔️
نتایج این تست‌ها وضعیت بازگشت دو بازیکن به تمرینات را مشخص می‌کند‌ و پرسپولیس امیدوار است هر دو به دیدار ۱۷ مهر مقابل صنعت نفت آبادان برسند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/140510" target="_blank">📅 10:49 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140509">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
حسین عبدی بعد از بازگشت تیم امید به ایران و در فرودگاه از سرمربیگری این تیم استعفا و اعلام کرد که دست فدراسیون فوتبال را برای انتخاب مربی باز می‌گذارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/140509" target="_blank">📅 10:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140508">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
❌
حسین عبدی: از مردم ایران عذرخواهی می‌کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/140508" target="_blank">📅 10:17 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140506">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tcqH7X7q6FRXf08HINIveDxqbepJ85QWiTK2SzzWp90u8odBBrlC0yCPXANnwHnXtEFHRsqCFSuHm2gkU9Tk0sSFSi22qZTDlkepASJt1xcYB5ja5iguYqN0rYxVh2e3xiUqWoAqoMhxbJRm1cCrfRQLl4YuQzH9kei0_sDnMDYVZcPVCcJ_hoJAbZvqVPnPwU_b5TgC2SFARMpItLfTZYfBeuylqm1wnWVm31KIcZLmP93nPFTBDgXX7q1Q5jd9MqBReJ9sj-Fi4B0me8iRX8nuF8RQlvuEQ7AFgEvZMsug41uhVZB51IpJ5r3QGnGXMc09evhO9DSgutL9rXubGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
ITALY -
❤️
BELGIUM
⏰
Tonight 22:15
🏟
Stadio Olimpico
🇪🇺
ایتالیا با بازگشت مانچینی و ترکیبی جوان‌تر، بازی را احتمالاً با مالکیت و فشار از کناره‌ها شروع می‌کند. بلژیک با حضور بازیکنانی مثل دی‌بروینه همچنان در انتقال سریع خطرناک است، اما غیبت تروسار، دوکو و کورتوا روی کیفیت ترکیب اثر دارد. آخرین تقابل رسمی دو تیم با برتری ۱–۰ ایتالیا تمام شد و تقابل قبل‌تر هم ۲–۲ بود؛ بنابراین بازی‌های اخیرشان نزدیک بوده است.
نقطه کلیدی بازی: عملکرد ایتالیا در پرس و کنترل دی‌بروینه مقابل ضدحملات بلژیک؛ احتمالاً جزئیات و توپ‌های دوم تعیین‌کننده خواهند بود.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/140506" target="_blank">📅 01:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140505">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">⭕️
⭕️
⭕️
فوتبالی: جام حذفی به‌دلیل فشردگی تقویم مسابقات و برنامه تیم ملی و امید برگزار نمی‌شود. سهمیه‌ آسیایی هم بر اساس جدول نهایی لیگ برتر تعیین خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/140505" target="_blank">📅 23:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140504">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMsuVcMbmlp3YRlN6SUCfBCDozicx3wcaaiL3Sd3yDdtKjFcS7jMpr3OLfpgTWc7vBiz0UIv57v0FMwDHXtxOQ1u_bZVvRf4Mop6qi3atenAvwpUJAYyN8HbKodZBMPOLmbLnLTxsaYhLtFSFpcKmQnmwJF4fkRbQUkwPJfF-ID1je2uWbOY6pqEsElU85H-4XemLIO0JtdGk5-OinApvlvcLo-7GYpM6PZT849NcDtPe4k4IFAZ0_U__vH2oZ90rJeS_KPt8fvsbw5kDLVGAdFq3biBemiXPDKiHbrHfpytVbJRpGJwo0psUa7BiEkcpkURRzR3ppMIG_GsGdp3BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎉
جشن تولد آقاکریم برا محمود خان و آقامهدی
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/140504" target="_blank">📅 23:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140503">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/199c169158.mp4?token=cUS1Na_gLoJUU4LardbGg6HfN8UGDvmXYkS6aok9RdxJIY46ddHBy3SuyekRBmDCNh38fgBnR6o7B5H8Ly9vV8WR6ciZqx5EybtTwCMdljtfj07OvJVreiANc2y-vNK9uVs_HFBc0jU71sIS8a7cXMLuAam9avIXxE6m24NccAcmgDsBIUDIGURxfE57q9nPUcVMYJAH6X3XMKnxB576gOGgfyhw-l_NsJoYV7XySv1WuAni_g59XY5NF_EYY46UMm36QRvw6BwYSSMDEAkMhbLJFvuhuhMLbvIYkbIIA8IethE6LmemmvJ46BljzaUeOtBjtkJbJbiL-uA5EH3P9nvj6EI15GyUADmdlqW2M8gO1l-5poU7Qf4nCYQRL151KMUhL4-d6HUDsT_V7fJa8cEbHGJhsFx5iFzlIKkkzcl93MyAkCwykqesZTErrpBuXWVR7fzcouGan8ZEKJvD1tZ9_6NFjoJNTcoEjz3fUrk_AuHrO4rhKcNs8d91f3914nmMJ-EV1SgDYhl1pAsCx7Vsi_zvngZQCfMBtQY2OsZpgsdtJFMa5IacRcPxHbWtXUHUQ7fVsGfCdkSKb_CwBOdJ3GXg_NPqrotPd5IVbH194Pt1iKfWzDJuWoyFezEcfPK-vSuGmWAznP1gZApsVda7r1xZO9DJ9gjSnfCeprI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/199c169158.mp4?token=cUS1Na_gLoJUU4LardbGg6HfN8UGDvmXYkS6aok9RdxJIY46ddHBy3SuyekRBmDCNh38fgBnR6o7B5H8Ly9vV8WR6ciZqx5EybtTwCMdljtfj07OvJVreiANc2y-vNK9uVs_HFBc0jU71sIS8a7cXMLuAam9avIXxE6m24NccAcmgDsBIUDIGURxfE57q9nPUcVMYJAH6X3XMKnxB576gOGgfyhw-l_NsJoYV7XySv1WuAni_g59XY5NF_EYY46UMm36QRvw6BwYSSMDEAkMhbLJFvuhuhMLbvIYkbIIA8IethE6LmemmvJ46BljzaUeOtBjtkJbJbiL-uA5EH3P9nvj6EI15GyUADmdlqW2M8gO1l-5poU7Qf4nCYQRL151KMUhL4-d6HUDsT_V7fJa8cEbHGJhsFx5iFzlIKkkzcl93MyAkCwykqesZTErrpBuXWVR7fzcouGan8ZEKJvD1tZ9_6NFjoJNTcoEjz3fUrk_AuHrO4rhKcNs8d91f3914nmMJ-EV1SgDYhl1pAsCx7Vsi_zvngZQCfMBtQY2OsZpgsdtJFMa5IacRcPxHbWtXUHUQ7fVsGfCdkSKb_CwBOdJ3GXg_NPqrotPd5IVbH194Pt1iKfWzDJuWoyFezEcfPK-vSuGmWAznP1gZApsVda7r1xZO9DJ9gjSnfCeprI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هر جا رفتیم اوت شدیم؛
🎙
درخشان: مشکل، ساختار فوتبال ماست
🟢
سال‌هاست فوتبال ما به قهقرا رفته است
🟢
آیا لژیونرها فوتبال ما را ارتقا داده‌اند؟
🟢
بی رو در بایستی ما فقر فرهنگی فوتبال داریم
🟢
ساختن 10 برابر نیرو، بیشتر از تخریب می‌خواهید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/140503" target="_blank">📅 22:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140502">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab25e53c97.mp4?token=vZPzJ0-t5n5fuh4c1pOFlqCfEjR2l-dFJ07hbOsrt4QXl8OrSgNmyE_lHIASClu2ezyKXkKUaiwLKvOT6UX41azNhVC5WCLBhHr61eTiBFwzu0EVJcqNsmguS403DdrueYR6Nyfa7dDnp6lv975txOU_jJNuV6trpODWEEcKRvOzzO6eiwjukhyOZGVs2LesoPnaqhZZssmVA8Xj8FzYVQNDCs8uBaWcseY69V2gKhYDWguQYcNPOT2B-SoQY_GI-4nD06U9Ub_90rx0h01W0GAuhOK9A_8ihmWASzlhREPjwes4TzqzI_-y2OGBTuwS2oyyAT845ery1396wRu9ZpzMV76RDaoMIo7dFGKZx3D4dSDiE_YrNW7WQn1B1OkNdItgF0s1o2079VZ8M_boE91HSgML8uLtGCZ9fLQ3jdTTq58reAIyUomkpUYlCG4xPqj9zQtccK5zK5S95aXGbelMEmAtbXPT7__ed-GQEmGQE63citqXtdv6pVukz3bQxWpukTSe97rY4_RopQ_LNyVbPxxCuIiFF3MSzEFgmRwXExogjEodGxX10KCwcaqr4quiMXYxESHPQUBer8VF3EL3Bk0X6QDBqpOM5wETpWzG-VaPiFeVBeTB5fry7KaxrXKCtNxjilLe9xuxTt6ct78uNWoy8DC2apwCGPPg-2c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab25e53c97.mp4?token=vZPzJ0-t5n5fuh4c1pOFlqCfEjR2l-dFJ07hbOsrt4QXl8OrSgNmyE_lHIASClu2ezyKXkKUaiwLKvOT6UX41azNhVC5WCLBhHr61eTiBFwzu0EVJcqNsmguS403DdrueYR6Nyfa7dDnp6lv975txOU_jJNuV6trpODWEEcKRvOzzO6eiwjukhyOZGVs2LesoPnaqhZZssmVA8Xj8FzYVQNDCs8uBaWcseY69V2gKhYDWguQYcNPOT2B-SoQY_GI-4nD06U9Ub_90rx0h01W0GAuhOK9A_8ihmWASzlhREPjwes4TzqzI_-y2OGBTuwS2oyyAT845ery1396wRu9ZpzMV76RDaoMIo7dFGKZx3D4dSDiE_YrNW7WQn1B1OkNdItgF0s1o2079VZ8M_boE91HSgML8uLtGCZ9fLQ3jdTTq58reAIyUomkpUYlCG4xPqj9zQtccK5zK5S95aXGbelMEmAtbXPT7__ed-GQEmGQE63citqXtdv6pVukz3bQxWpukTSe97rY4_RopQ_LNyVbPxxCuIiFF3MSzEFgmRwXExogjEodGxX10KCwcaqr4quiMXYxESHPQUBer8VF3EL3Bk0X6QDBqpOM5wETpWzG-VaPiFeVBeTB5fry7KaxrXKCtNxjilLe9xuxTt6ct78uNWoy8DC2apwCGPPg-2c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
نتانیاهو تقریبا برای یک سالن خالی سخنرانی کرد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140502" target="_blank">📅 22:43 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140501">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
❌
حین سخنرانی پزشکیان، نماینده‌های: ایالات متحده آمریکا ، بریتانیا ، آلمان ، فرانسه ، اسرائیل ، سوریه ، لبنان ، عربستان ، مصر ، امارات ، الجزایر ، لهستان ، سوئد ، دانمارک ، کانادا ، ژاپن ، جمهوری آذربایجان , مالزی ، نیوزیلند ، استرالیا ، جمهوری خلق کنگو ،…</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/140501" target="_blank">📅 22:43 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140500">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✅
✔️
✔️
✔️
✔️
تکرار تورنمنت سه‌جانبه؛ دو بازی دوستانه در برنامه پرسپولیس
❌
در جریان تعطیلات پیش روی مسابقات لیگ برتر، شاگردان مهدی تارتار تا پیش از ادامه مسابقات لیگ برتر، دو بازی دوستانه با چادرملو اردکان و گل گهر سیرجان برگزار می کنند.
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/140500" target="_blank">📅 22:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140499">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✔️
✔️
#فوروووووی
❌
با اعلام حدادی جام حذفی برگزار میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140499" target="_blank">📅 21:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140498">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6388e432cf.mp4?token=KDycu_eDt4NprUmtqv_tfawykdemmfS3gjzie9DmQ4Xj9RmML_IUwRcOeKwcUkNevnQFZNzJjRI4PxQECqc76tKyhvzqv98-37lYmgs_DX_6YvA64iqyK5WlmGukwgVRaPunr4nHH0dbtRsdCw42aIx0dor1_9ww-16s3-wzoFHBXR-ANop2ZKCsd7Q_mxxFVDY7nFUq3T-okXsBmK4ETeiE8UyhWs_hCqpmeRHwxgKfkuvrKi9W8XjVHActfuST7B-pOBmiP09lDF66xYZx80sDuX3O4tRBm2b3mfKO-48KfdRLVPFoK4fLVvIzQUAFxuBcI4KEsdiTiyWmetFlzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6388e432cf.mp4?token=KDycu_eDt4NprUmtqv_tfawykdemmfS3gjzie9DmQ4Xj9RmML_IUwRcOeKwcUkNevnQFZNzJjRI4PxQECqc76tKyhvzqv98-37lYmgs_DX_6YvA64iqyK5WlmGukwgVRaPunr4nHH0dbtRsdCw42aIx0dor1_9ww-16s3-wzoFHBXR-ANop2ZKCsd7Q_mxxFVDY7nFUq3T-okXsBmK4ETeiE8UyhWs_hCqpmeRHwxgKfkuvrKi9W8XjVHActfuST7B-pOBmiP09lDF66xYZx80sDuX3O4tRBm2b3mfKO-48KfdRLVPFoK4fLVvIzQUAFxuBcI4KEsdiTiyWmetFlzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مجید جلالی: میلیون‌ها دلار خرج مربی خارجی شده اما برای ایرانی‌ها هزینه نکرده‌ایم به همین دلیل است که می‌گویم قلعه‌نویی از مورینیو بهتر است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/140498" target="_blank">📅 20:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140497">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETvvAuZQAmbZyPcBQNGZJiK02M2alkbh7OfR7NqicBJEvMH-na_pfZ_XKGpFLuQk97mkX0tGDgSQNvVzty2on20HpzyZ56M32RvowSkuFp5OHBvk1cP7s8hg_Q96XdvVMJf2MlVidyb6pHKuin3orVwxX0uSAQhMKjGLcYltfcqDuxw5uUD_3LvgQW-Uhki82hwBKSzZByVsl4VYb9vQhuYBc1UZYmhMIHrJx0SyVU9QG_H-8f5d-1ii3KNTJ_rvVjvFQNURdLV2EZ1O_0CiiLBfMqwMEBiVgTaAOP6_JTxTP0FOUKDYuKRApXt-hZCh-OW1gPHy_6uQe3DWkCpKGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🎙
جواد خیابانی: تا دلتون بخواد تیم ملی با قلعه‌نویی به ازبکستان باخته. سال به سال دریغ از پارسال. تیم از جام جهانی حذف شد، رفتن فرودگاه استقبال!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/140497" target="_blank">📅 20:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140496">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc376d50be.mp4?token=jYPDlhOJBjD_hyOFAVdAnzhUrw38VJNzKQneWISBy5vLliOlUtTva8iDeAY-Y7lmH7wQpv5unlsnXegPpMaHmiTsRTS83CxwvssKDnDs7yguntJYFZI2UODhVY49Lg8Len_5fB_wgOQSYpb2ratKUrDp5h1JeMxsQo8qufyRSF0GlwD4wApFovL-RxwaTmYnDZXJPca71wo6fEt9hGJbR9DY1JvNi5e4pvarNVWVlXvhWaTNzhS6T3yeiIz7utLvo2PQsI2jIHS0l_63DyeoXiDKf1mXIeNK_BnMcTKZNwrkirjEbVKftNy5cVIyQJyv0ezfPY_Zp0nxGq33GnZw1RuPyN7nwcH2DcZ1LelM-hX_2qofEo59qkxczHxZACBSRaQTeWr3Qp-gzLyC-rCc3URVspKuVrqgu8Zxa1D89iTYN5MSnV5T2yBeJ9NfjfUbv5Ax7dvuIkks8wenEgaF89WVDQUAfPC0GsYh-4vKzsdHEh6mp2lY3IHFsqHP5K5sFGYMJyHGPPZppTCl8kiG32PCy81Q3rTQ8o5rsFemRXmjftVoAGJbYWmdicT7BgZzPeSugE8zZnQC-F6lQhsOdMm3qjvWnevtxXszmbP3XZVV0vD0s34YuXudk9iTTs7-1g6CoyrWDPeraf7RM-r3ToF2vO6hzGvpGMXvtgIvDMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc376d50be.mp4?token=jYPDlhOJBjD_hyOFAVdAnzhUrw38VJNzKQneWISBy5vLliOlUtTva8iDeAY-Y7lmH7wQpv5unlsnXegPpMaHmiTsRTS83CxwvssKDnDs7yguntJYFZI2UODhVY49Lg8Len_5fB_wgOQSYpb2ratKUrDp5h1JeMxsQo8qufyRSF0GlwD4wApFovL-RxwaTmYnDZXJPca71wo6fEt9hGJbR9DY1JvNi5e4pvarNVWVlXvhWaTNzhS6T3yeiIz7utLvo2PQsI2jIHS0l_63DyeoXiDKf1mXIeNK_BnMcTKZNwrkirjEbVKftNy5cVIyQJyv0ezfPY_Zp0nxGq33GnZw1RuPyN7nwcH2DcZ1LelM-hX_2qofEo59qkxczHxZACBSRaQTeWr3Qp-gzLyC-rCc3URVspKuVrqgu8Zxa1D89iTYN5MSnV5T2yBeJ9NfjfUbv5Ax7dvuIkks8wenEgaF89WVDQUAfPC0GsYh-4vKzsdHEh6mp2lY3IHFsqHP5K5sFGYMJyHGPPZppTCl8kiG32PCy81Q3rTQ8o5rsFemRXmjftVoAGJbYWmdicT7BgZzPeSugE8zZnQC-F6lQhsOdMm3qjvWnevtxXszmbP3XZVV0vD0s34YuXudk9iTTs7-1g6CoyrWDPeraf7RM-r3ToF2vO6hzGvpGMXvtgIvDMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🎙
جواد خیابانی: تا دلتون بخواد تیم ملی با قلعه‌نویی به ازبکستان باخته. سال به سال دریغ از پارسال. تیم از جام جهانی حذف شد، رفتن فرودگاه استقبال!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140496" target="_blank">📅 20:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140495">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cb36555e1.mp4?token=Rl8UYndYaM9Xid8H1q8S1y9GMgjE-M5EuYn4zj0Uq5yYK2nujsQ9aQEO819YToGeHu5xaCIzWjHrVtiY0fCH9-NNRMTZr5yLGu-TI5V8BFpmeqMH3Gib0O6_3Fxr1XrJ50ETqrtjyT5FO-Y3i4gtRoLYNGkyELADqyA5u3fFzb4CrjXE0q7sSxIQfHaRw5puEkSVxioz7zRrCtwaBCg0h-_3mtIYsmAUv3vkn92sHmHA2_LNiBzub_VvueKMbO0aC8uvhDAs_y-DsF3sHrR-E6URgoPZLAOb0-7ySVdHXDr-V1INNMqz2i3W7tkqAqoDLaXm9d67R9LRxt3eDcnmZRb8xpLfuSExIfNKgD3XB9htjyTCj1jQKW3Df4IFkiA12DbfxjvohFEwqj-brhaHZBIFciegymun8IXojf640VvuWEDnr0Kcg6KHSw7L-NvKv-8C01OdNOQ3gsAduoQHTYmk7fjYzbJt0laT39BrTFZP4kfzC93e8O9uqUxfW30k5Es6eweG62YyejQjNnQm3uc-Ud8bM64QCsg9rAsONwpPyvZ4WLPmNWk9sflNdHQO-tUaLrqQSXPl3plPsuNOLyhQJopsUMyCYAe3L4vVy3qwY0qNa20uny_A8n7sL8YDRdZoKEltXcTeXzW4WmhGnvcp4FxT0EjiFR32Du3NlVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cb36555e1.mp4?token=Rl8UYndYaM9Xid8H1q8S1y9GMgjE-M5EuYn4zj0Uq5yYK2nujsQ9aQEO819YToGeHu5xaCIzWjHrVtiY0fCH9-NNRMTZr5yLGu-TI5V8BFpmeqMH3Gib0O6_3Fxr1XrJ50ETqrtjyT5FO-Y3i4gtRoLYNGkyELADqyA5u3fFzb4CrjXE0q7sSxIQfHaRw5puEkSVxioz7zRrCtwaBCg0h-_3mtIYsmAUv3vkn92sHmHA2_LNiBzub_VvueKMbO0aC8uvhDAs_y-DsF3sHrR-E6URgoPZLAOb0-7ySVdHXDr-V1INNMqz2i3W7tkqAqoDLaXm9d67R9LRxt3eDcnmZRb8xpLfuSExIfNKgD3XB9htjyTCj1jQKW3Df4IFkiA12DbfxjvohFEwqj-brhaHZBIFciegymun8IXojf640VvuWEDnr0Kcg6KHSw7L-NvKv-8C01OdNOQ3gsAduoQHTYmk7fjYzbJt0laT39BrTFZP4kfzC93e8O9uqUxfW30k5Es6eweG62YyejQjNnQm3uc-Ud8bM64QCsg9rAsONwpPyvZ4WLPmNWk9sflNdHQO-tUaLrqQSXPl3plPsuNOLyhQJopsUMyCYAe3L4vVy3qwY0qNa20uny_A8n7sL8YDRdZoKEltXcTeXzW4WmhGnvcp4FxT0EjiFR32Du3NlVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💛
🎙
حمله جواد خیابانی به امیر قلعه‌نویی: باید چیکار کنیم که کادرفنی تیم ملی تغییر کنه؟ نتیجه افتضاحی بود. آقای قلعه‌نویی نمیتونی تیم رو جمع کنی.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/140495" target="_blank">📅 20:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140494">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89362fa6a8.mp4?token=jv6HKwNIfXPns-14bkIz7WJy4RPhUs4jXIKViVcCSt7dwHYqBpvZkv5VvK2FMmnKqncOeZjRskQBDY177VNBaxjY90U_x-dzv6pHOJY-Ogxihix-zqW_uzBL7kZT_ouj1g_QcYyDJVXDbfdzN6TpXTmKJHziyIReGVgnSohGXs4J6zXn017myqG8ySBlig0gKuQ9UzvBipuDrJqjhMzGeSWAK5a0Cgl78aaO9OkidMDh2J77iR04HIsWlWk-qxkgFfghpvFYBBiKKCBfS5h-6uwsFIoN6YVpus9WE1nXXWV1q4ucobwwc3twGt5icjiTeiyJf1fkUtHbEPWAYm7tnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89362fa6a8.mp4?token=jv6HKwNIfXPns-14bkIz7WJy4RPhUs4jXIKViVcCSt7dwHYqBpvZkv5VvK2FMmnKqncOeZjRskQBDY177VNBaxjY90U_x-dzv6pHOJY-Ogxihix-zqW_uzBL7kZT_ouj1g_QcYyDJVXDbfdzN6TpXTmKJHziyIReGVgnSohGXs4J6zXn017myqG8ySBlig0gKuQ9UzvBipuDrJqjhMzGeSWAK5a0Cgl78aaO9OkidMDh2J77iR04HIsWlWk-qxkgFfghpvFYBBiKKCBfS5h-6uwsFIoN6YVpus9WE1nXXWV1q4ucobwwc3twGt5icjiTeiyJf1fkUtHbEPWAYm7tnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
💚
حمله شدید خیابانی به تیم ملی امید و کنایه به قلعه‌نویی: بازیکنان کره‌شمالی نه مدل مو داشتن نه قیافه آنچنانی می‌گرفتن ولی اومدن مارو درب و داغون کردن، بازیکنان ما چی یکیشون 20 میلیارد میگیره یکیشون 800 میلیارد میگیره اما دوهزار بازی نمیکنند و تحقیر میشیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/140494" target="_blank">📅 20:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140493">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pp_qMzlkd85uah0lRHHr3fmSQf2CLj6d1X-cSmUfTS-HoC-u_VP6vy2PQhrun1-PbxqOdSOIEqKrafNYFqm5wWL6flt55KM-VSJplC_6lMRzqvVhJ2JFqGzuh4gInVwNYccR6LJcuEExmqTlua4tUcXKQ2Y94KzcUVQVc3PLYWmsLmZ0gKVVyPexmT9dlf0mCz4KrA36TQQmdL3S345I_CYgIn57raU0kdBJYt7p_OdyQnwR1XH9bxZpxqe5pOo62qH3qeJiN67pTHKXb6YNEgr1s1AwBIxRXcr-dwAUEV7GtMMjEIUNCvtw815EzHiRAK8EAtmKEtSs5r3N2gYquw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
Netherlands -
🇩🇪
Germany
⏰
Tonight 22:15
🏟
Johan Cruijff Arena
⚽️
آلمان و هلند در شروع لیگ ملت‌های ۲۰۲۶/۲۷؛ دیداری که از نظر آماری کاملاً نزدیک است. هلند در ۱۰ بازی اخیر میانگین ۲.۲ گل زده و ۱.۹ گل خورده داشته، در حالی‌که آلمان ۲.۴ گل زده و فقط ۱.۲ گل خورده است. در تقابل‌های اخیر هم آلمان دست بالاتر را داشته؛ ۳ برد و ۳ تساوی در ۷ رویارویی اخیر و آخرین بازی دو تیم با برتری ۱-۰ آلمان تمام شده است. از نظر روند گلزنی، هر دو تیم پتانسیل بالایی برای گل دارند؛ ضمن اینکه تغییر سرمربی در هر دو تیم، یعنی نخستین بازی رسمی یورگن کلوپ و ژاوی، می‌تواند بازی را از نظر تاکتیکی غیرقابل‌پیش‌بینی‌تر کند.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/140493" target="_blank">📅 20:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140492">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✅
✅
✅
سرگیف، اورونوف، آشورماتوف و ماشاریپوف از لیست ازبکستان خط خوردن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140492" target="_blank">📅 19:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140491">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
❌
دو گل خوردیم .اونم آقایون شجاع و بیرانوند تقدیم کردن و دوتنه تیم ملی و نابود کردن   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140491" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140490">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">⚡️
⚡️
⚡️
عالیشاه از دو سه سال قبل با خانومش هست، مثل کریس و جورجینا و حالا امشب عروسی میکنن، قرار نیست اتفاق خاصی بیفته، عروسی صرفا یه جشنه و قبلا با عقد رسمی شدن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/140490" target="_blank">📅 19:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140489">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
این بازی ساعت 17/30 انجام میشه و بلاخره روی ماه اقای درگاهی رو میبینیم ...ببینیم چه جور بازیکنی هست   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/140489" target="_blank">📅 18:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140488">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✅
✅
✅
با اعلام باشگاه دوا یونایتد بانتن اندونزی، اوسمار ویرا هدایت این تیم را برعده گرفت
❌
این تیم فصل گذشته در لیگ اندونزی هفتم شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/140488" target="_blank">📅 16:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140487">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
❌
❌
سعید الهویی : قائدی چون گفت بهترین مربی هایی که باهاشون کرده مجیدی و استراماچونی هستن دعوت نشده تیم ملی
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140487" target="_blank">📅 16:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140486">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
ترکیب ایران مقابل ازبکستان اعلام شد
⏺
علیرضا بیرانوند، سامان فلاح، علی نعمتی، صالح حردانی، احسان حاج‌صفی، سعید عزت‌اللهی، امید نورافکن، محمدمهدی محبی، آریا یوسفی، مهدی طارمی و دنیس درگاهی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/140486" target="_blank">📅 16:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140485">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✅
✅
ورزش سه : زارع امروز جلو ازبکستان فیکسه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/140485" target="_blank">📅 16:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140484">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✔️
مهدی ترابی بازیکن32ساله باشگاه تراکتور که دچارپارگی رباط‌صلیبی شد هفته آینده پای مصدومش رو به تیغ جراحان خواهد سپرد و تا اوایل اردیبهشت ماه سال بعد دور از میادین خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140484" target="_blank">📅 16:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140483">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✔️
✔️
فدراسیون به باشگاه گفته که مدرکتون برای یاسر آسانی کمه و اون مدرک اصلی و قوی که ما میخایم رو ندارید شما ، حالا باشگاه از طریق یکی از ایجنت های ایرانی یاسر آسانی یه مدرک فوق العاده قوی رو کرده که فسخ رسمی این بازیکن با استقلال رو نشون میده و فدراسیون هم…</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/140483" target="_blank">📅 16:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140482">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✅
✅
✅
فشار شدید امریکا علیه ایران
✔️
✔️
امارات، ترکمنستان و تاجیکستان ۳ کشور جدیدی هستند که حریم هوایی خودشون رو به روی هواپیماهای ایرانی تحریم کردند !
❌
مکزیک برزیل و بقیه کشور ها هم رسما تحریم کردند   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/140482" target="_blank">📅 16:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140481">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
❌
❌
گفته میشه عربستان و چند کشور منطقه دنبال فشار به فیفا برای تعلیق فوتبال ایران هستن؛ اتفاقی که می‌تونه باعث حذف تیم ملی از جام ملت‌های آسیا بشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/140481" target="_blank">📅 13:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140480">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qW8moKC9wpU2x-u5o4E2sKhRLAO5ajM3u_ZzaUmUGY6yo2bgrF2dxyX6V1wMh5MD-sVoiJs-E1sz8Dpy-bl9_0s6Sx7H4oiw-tfgmKhGA68NW2hsx6FjyCiVz4ML6nIxNYKqtQnomhzPjTizAT2I3HFgqu6CS7pHZul-2eHaTvVz3VKv4rXeSc1ZRLjfFpF50Ccvv-CJ8TIQruxdv8UQndpuooIVDpK0UDhctjM-X0aV_GrUkeAatQuE1zwEseoyDYQzlqIGxJyzBiYzm2GRBnTulJBe1HQHz3bInDkX8h0N34XuOzpvf1S-cH-ofFQSVncvoxZflqvKDOJIQHHhWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوری از قدوسی: قربانی به شدت تمایل داره پرسپولیسی بشه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/140480" target="_blank">📅 13:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140479">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdKZ47QL3hxea3K6VAmGPZLcdI80qgd11BxDeHw2C1EDElu5AUonXwFYjv3vitAo-FQIs1prVk8zsihyswUbjTaLj02Pzae9dDSyS4-raU-9gqsWeKnpe0rq2TWG0b2JVD_ElbYPP0EgDKckQof2TAI3dL0uY0bk0YzxA-dks9oM-nfuPzjz2KjCbssjToUln4qKebpMeVQyjMEQa0863MgzlYBS_9TyaYqFTt6h4bKRHvjXsS41shxnsbmf4z93iXOSAD03AT-TiZdjDD3QszLC3K-KDVa0VpU514kkj6jZfBPBSK7boDNhVCbnteztzSdoX3Pesponp9RsbTtAkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
از ریفوی ژاپن تا لیسبون؛ شبِ دوئل‌های حساس
ملی
🔥
⚽️
فوتبال امروز با دیدار ژاپن و اروگوئه شروع می‌شود و در ادامه، ایران وارد یکی از متعادل‌ترین بازی‌های روز مقابل ازبکستان خواهد شد.
هلند با آلمان و صربستان با یونان از دوئل‌هایی هستند که فاصله تیم‌ها در ضرایب هم کاملاً نزدیک است. در سوی دیگر، نروژ مقابل دانمارک و پرتغال مقابل ولز؛ جایی که پرتغال با ضریب ۱.۲۰ واضح‌ترین برتری این جدول را دارد. یک روز پر از بازی‌های نزدیک، ضریب‌های متنوع و چند تقابل که نتیجه‌شان می‌تواند جذاب باشد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی بازیای امشب همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140479" target="_blank">📅 12:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140478">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✔️
✔️
✔️
بیرانوند برای فرار از سربازی، این‌بار به بهانه خالکوبی، دست به دامن کمیسیون اعصاب و روان شده تا شاید با برچسب اختلال روحی، کارت معافیت بگیرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/140478" target="_blank">📅 12:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140477">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
❌
چمن شماره ۳ آزادی به مشکل خورد!
❌
❌
بعد از دو سال تمرین پرسپولیس در این زمین، چمن سفت و نامناسب شده و قراره به‌زودی زیر کشت بره. احتمالاً سرخ‌ها چند ماه آینده تمریناتشون رو در شهید کاظمی و زمین شماره ۲ آزادی برگزار می‌کنن.  «سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140477" target="_blank">📅 12:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140476">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✅
✅
ورزش سه : زارع امروز جلو ازبکستان فیکسه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140476" target="_blank">📅 12:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140475">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JrBlSRaYmtQu5TheD61gskwvc_9Q_0FXTg9WXkljmW8PAbiF2gA5B_D53cbQi4n8i1AflCwzJCtUTm7oFhhBnOJMcVzeXS_rgpJD9gmQa5_J-7_wzLBETH2TxUoxWgvmOegOMm8p83Z3CohYtLKm7MZGTOV3mZ2p6uZESa0y5W2Z4PJUbLi3ZNMzvrMtM7LhGFXWJiAboMN8vJvaE88POZO2EYV7Dj8qv4KoTpnjiS9kt1BbuojLF42MQ3fW8zAmwwwer2i8IBQtIsHXc9WUFuNQEbQELNXRCvLBOt__zPmcJW0vgOAABbKS8zMy59v_p9gmB0mxSggjNIIueMyZ1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
| طرفداری:
🔴
⏳
🔄
تارتار اصرار به جذب رزاق‌پور دارد و ولکن این بازیکن نیست
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/140475" target="_blank">📅 11:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140474">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
فووووووووری از قدوسی : کمیته انضباطی به باشگاه گفته مدارک شما برای محکوم کردن آسانی کمه و اون چیزی که ما نیاز داریم ندارید.. که یکدفعه باشگاه مدرک جدید و آس رو کرده و فدراسیون آچمز شده و هنگ کرده   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/140474" target="_blank">📅 10:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140473">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
❌
بازگشا، سخنگوی باشگاه پرسپولیس:
✔️
از فدراسیون خواستیم رسیدگی به پرونده آسانی با حضور وکلای ما و آنلاین باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/140473" target="_blank">📅 10:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140472">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
⚽
طرفداری: پرسپولیس در آستانه‌ی تیمداری در لیگ دو و شهر مشهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140472" target="_blank">📅 10:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140471">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🏅
🇮🇷
نیازمند، کنعانی، زارع، عیدی، جلالی، خدابنده‌لو، تیکدری، محبی و علیپور از پرسپولیس در فهرست تیم ملی حضور دارند.
✍️
طرفداری   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/140471" target="_blank">📅 09:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140470">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYbffdz68YkmoVSSC_VUvrilOEamY_g38qFb6bOT6pkUjU6I6E66lnupdpIilYTy081ZxTO8cb4W3pRIgzpQD-bSeWHg8WGYWFWXpUiwpO2g9zuBmu-lc6MKx83UXX-QV1yCD9j_69xId0F92JHKisVuwXS5uPsdPfejcgqBeqrqD-Fnb1atPm_U-5ZWk3BW2aH-4MP1YeyFxBScbVoUJ4DhE0oBSnVw1Vos8q8HYTcGJH7RWH6AeOiclHGHGHzhqQjpW0AJoqnOGBK-cn3laXi42ZbXtDyeIA4XAPfVnI85NKGuf5Vamy57feSf2q2xNpnvhdA_nYrelt6NOcg-HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140470" target="_blank">📅 09:12 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140469">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swoItZrqwDpvFXw8f8bQpJ_NEYJj-X26ZgXGjS2W3koT8uxleDLMAjV81-40ncMkI58bbq_Aj9HvLgVLiiXZzjP599L0HOVoPdeuJ9xbofKEL0kvZGUgJzpO5gRRDSp6Ee_xP12I6F9IVAE2gYQjzlJqzOhTaaLVdyLJx5wZOVry9YC8b8PTYW4Y-l6PE6w8Df3kVSfdTXlJ5H01dvLj7r9ckuAIkx9yc8pFNmn54Mlsnccr3UtvI-xHKx6Hvkkk_K_p5JzeqADJ9f5gNrwmuiht5rIMMoydVYiJIhOjqleUKvyBVhOOd4Nlk59zsjMbUWrwS4i7wAVUFFwaFN23Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ایران و ازبکستان؛ محک جدی در یک روز دوستانه!
[
ایران
🇮🇷
🆚
🇺🇿
ازبکستان
]
⚽️
ایران و ازبکستان فردا در یک دیدار  دوستانه به مصاف هم می‌روند؛ دیداری که بیشتر از نتیجه، برای محک ترکیب و هماهنگی بازیکنان اهمیت دارد. ایران معمولاً در بازی‌های مستقیم و انتقال سریع خطرناک‌تر است، در حالی که ازبکستان با مالکیت و بازی ترکیبی می‌تواند فشار ایجاد کند. با توجه به ماهیت دوستانه، احتمال چرخش ترکیب و افت‌وخیز ریتم بازی بالاست و آمار نیمه دوم می‌تواند متفاوت باشد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/140469" target="_blank">📅 01:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140468">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
🤩
فرهیختگان:
بزودی قرارداد اوستون اورونوف با پرسپولیس با دستمزد 2.2 میلیون دلاری تمدید خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/140468" target="_blank">📅 01:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140467">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXLsDV4_nuoa_GESHt5-x0mnOBw_uelDlD-9MW5F2kIruRbpEKLPHN3g19pLt2orAUYWhhGAZlhfFonNfa0qxOCZyA610re-RkOuFztqGNok0cE6CPzRyJOtbv55GWKpedCKW2vu3Hb9PfcKQYJjOsNrShl7X9wpe4oAcHSz-j59joCE9kiDmLVphMvdTnGY-sz5lJPPj8-AlwLMHEdbghTLUulZYkrM1BDnSxJPrpUEjz4WsYqGvyUGlridK_kVg-wEQlCKa3YFtVLWQUIi2tt2ZUTy60Li3xLePZSSGX1a-i9OYaxC3Oiqyep7yaQGHP824i79EeHB1I8FF-Lxcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
❤️
پرسپولیس در نامه‌ای خواستار برگزاری حضوری جلسات پرونده آسانی و ضبط کامل فرآیند رسیدگی شد
‌
📌
باشگاه پرسپولیس در دو مکاتبه رسمی خطاب به رئیس فدراسیون فوتبال و رئیس کمیته استیناف، خواستار برگزاری حضوری جلسات رسیدگی به پرونده شکایت این باشگاه از یاسر آسانی، حضور رسمی نماینده باشگاه و ضبط صوت و تصویر کامل جلسات شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/140467" target="_blank">📅 01:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140466">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🤩
👤
🔴
فوتبالی: تارتار بعد از دعوت نشدن کنعانی نگران وضعیت روحی اوست و قصد دارد جلسه‌ای با کاپیتان تیمش در این باره برگزار کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/140466" target="_blank">📅 01:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140465">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
⚽
طرفداری: پرسپولیس در آستانه‌ی تیمداری در لیگ دو و شهر مشهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/140465" target="_blank">📅 23:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140464">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZ4GX6vT-AOklWcDl1ABV9ea5MymZSDAFDc2qDlSHvCPElx1i2lgIky4GJmXpXk9xQYIOCeQYG9iSQTh82bdXmnGOJipQ6cL57MDI9AIHhPaLCcjwcOlv1hxXf6yxLao_tNRfaZf6u5CssqKSrKA1TLLBeCFdGw3-Mo85PkJVZ1HGpAeY0LAfvyazKOvGb-ATKz0lw2Mea_iW_f96TJT75mcwvW4UzOvPO69SQb_i3Ox7hsec4XNxJPMpI57Lhdfs6QRQmKRTHNBNJYvRw8NYx214GuCV0O1JGjNW7sNkjG9KTSWCZImLp1WXHZn4k4uwN_FhVzel1oMk_EUcBR_QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
🇮🇷
سه درخواست رسمی پرسپولیس در پرونده یاسر آسانی
🚫
باشگاه پرسپولیس پس از ثبت لایحه تجدیدنظرخواهی در پرونده یاسر آسانی، طی نامه‌ای رسمی خطاب به مهدی تاج و ارکان قضایی فدراسیون فوتبال، سه درخواست را مطرح کرد.
🚫
این درخواست‌ها شامل برگزاری جلسه استماع با حضور نمایندگان و وکلای باشگاه، ضبط کامل ویدئویی جلسه رسیدگی و فراهم کردن امکان پخش آنلاین آن با هدف افزایش شفافیت و اطلاع‌رسانی عمومی است.
🚫
باشگاه پرسپولیس ابراز امیدواری کرده است این درخواست‌ها با توجه به اهمیت پرونده، مورد توجه مسئولان فدراسیون و ارکان قضایی قرار گیرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/140464" target="_blank">📅 23:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140463">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NiSz_v2fPOpw1ZSZCLFM30ahQutOberoK8IiIBH3xZAfHDZ8Uq-nxFHCpwmMFw6wsx3oQ3vJC3WZPnejwInpFLHCqMrHGSARNswkFbuZaHCoteBins_QUCVRBS2XR8m8dP93LhhWJeNUVcOhjewZL7nXZc7SrE5kMevajbSIai085t_FQDvAxV1goawAobESl76JrDUdxI22i8Mj-MP0oClouXYWhv7PodxauuCzTcZTSzgSNNMk90GKDLFXNlNn9zpjYQNL4O0jai_b6Ar115LDCqWsX_Jk7MNC150GjkeOfKN8CRNfgUhNKFobx5Z_CW3Y_ryOcfasrGq5hH1X5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سعید آقایی: در پرسپولیس کم بازی کردم اما بیشترین لطف را از هواداران این تیم دیدم آنها را از صمیم قلب دوست دارم
❌
بعد از مصدومیتم در نساجی کلا فراموش شدم تنها دلخوشی‌ام در یک سال اخیر فقط هواداران پرسپولیس بودند که جویای حالم میشدن
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/140463" target="_blank">📅 22:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140461">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">⭕️
⭕️
⭕️
🚨
🚨
🚨
در پرونده‌ی آسانی، پرسپولیس در استیناف پیروز میشه/قدوسی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/140461" target="_blank">📅 22:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140460">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/le6ARVfdvISFlzosa5r_LhC-osiwNsAhwsDLM7rVrpM9Sy0y8iBtEDzB_ZLmOiRgAoixXg5Ys3IiPLQDn50uIaadH9HM8xCBYfRp5-d542_nz6shOtghMMsDMNLZhY3890ZiIJ5b2LMvUDylgw7TGL9yghbw54f1uowrpGJvyEjllc6nlSQfRLdaBnBDji-m5HG_-5LlPyt6hXb12GSoogR6PtYu9kqWtW24E0ycZAeIzSAHM5N5AQjoi8lPDoaS4T-Kldos96oyToeR6BX4wset1a8Gu6vJsSz05e1Iz-XCpGjMKMYezwVUUzVtOKVl49JhNj-9Fy1XGjU9Ayr-zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
✔️
حسین عبدی: مقصر اصلی شکست من هستم، اما بچه ها با توان فردی خودشان فاصله داشتند از مردم ایران عذرخواهی می‌کنم
✔️
✔️
باید به کره شمالی تبریک گفت؛ آنها خیلی خوب بازی کردند. باعث تأسف است که در این گروه سخت نتوانستیم پیروز شویم و به مرحله بعد صعود کنیم.ما…</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/140460" target="_blank">📅 22:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140459">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
ویدیوی‌کامل سخنرانی فوق العاده و طوفانی پزشکیان در سازمان‌ملل  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/140459" target="_blank">📅 22:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140458">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
❌
حسین عبدی: از مردم ایران عذرخواهی می‌کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/140458" target="_blank">📅 22:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140457">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🏅
🏅
پرسپولیس مدارک جدیدی رو به کمیته استیناف برای 3_0 شدن بازی دربی ارائه داده
⚪️
حتی اگه رای استیناف به سود آسانی باشه پرسپولیس تمام این مدارک رو به CAS میبره
✍️
همشهری  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/140457" target="_blank">📅 21:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140456">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUHzNCGIu_kUuwR3oNIuYv4uOD-CFCogbyQs3sZfcq40LbzDV63OMgYdKayu_zwOTj0cGppbsMEqyuvqyCyhehXxPod_zcggyPjxH5kDHA5fC3nrTSm8E2vATZZridBTAsNt0FNs2pcgfHPzizQTK-1uJvwHPqVylToYg4Wffc5p8MNo9BljpbzoKKZSV4Ybj5qrF8iunJG2LvSFrVa6sb178R_wEA6GqW4UlIcCLzXjsQw-0dp-FylqzxK72B38YDHpzhPriKMS4XPfavsX3h_v3T2a47ZptmsJPHh0M9nxl5OBKV4XOHD1yidF_htfG1Z9QYtlrwvosaNkzBy0Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ایتالیا مقابل فنلاند در یورو والی؛ جایی برای غافلگیری نیست!
🏐
ایتالیا در این مرحله با ۶ برد متوالی وارد یک‌چهارم نهایی شده و در مرحله قبل دانمارک را ۳-۰ شکست داده؛ فنلاند هم بعد از یک بازی سنگین ۳-۲ مقابل یونان صعود کرده است.
ایتالیا با سرویس، دفاع روی تور و تنوع حمله دست بالاتر را دارد و روند ۶ برد پیاپی هم نشان‌دهنده ثبات بالای تیم است. فنلاند در بازی با یونان توانست در لحظات حساس برگردد، اما فشار حملات ایتالیا آزمون سخت‌تری برای دریافت اول این تیم خواهد بود. با توجه به اختلاف کیفیت و فرم دو تیم، ایتالیا شانس بیشتری برای کنترل مسابقه و برد ۳-۰ یا ۳-۱ دارد.
🏐
اوج هیجان همراه با اسپورت‌نود، پنجشنبه ساعت ۲۲:۳۵ دوتیم ایتالیا
🇮🇹
-
🇫🇮
فنلاند به مصاف یکدیگر می‌روند.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/140456" target="_blank">📅 20:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140455">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
#تسنیم؛ بیرانوندیه پرونده تو کمیسیون پزشکی ایجاد کرده و گفته من چون خالکوبی زدم مشکل اعصاب و روان دارم و باید معاف شم
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/140455" target="_blank">📅 18:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140454">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JwRgi58sAUu2ylJjCUh9sldEvW0LyS6hSfx6I7EbzMusgxPXh2QDux38nz_1r_VbobfvnLtxzjGXe32Ff7E5OESCF105__cTFz0Oo09pQ4YKdnVY-m8qOxDYAk9XV_MoqESE0hidxEi4RKhQSFz8A88ndAU9NiGWFf8bVgZoP9PWpuDLdEd8W1VIoHygRopFicemZXYzDvAN_QIE53smU7YpuactFDBXsfujUKgFNYSxKVJ2N_yxsVgTjc-8TfFn3SVaUM25D_9ArACacXqUvKrUvFXwpZDNfu_RHhvwdWLQil_h6KpYwrZcUVhpm7UCrqqTguXY8OJyF-PwqmRrUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◀️
⚪️
رنگ پیراهن دو تیم ایران و ازبکستان برای دیدار دوستانه مشخص شد و ایران قرمز میپوشه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/140454" target="_blank">📅 18:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140453">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
ویدیوی‌کامل سخنرانی فوق العاده و طوفانی پزشکیان در سازمان‌ملل
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/140453" target="_blank">📅 18:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140452">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGcgdP_nSCQyJzvIoxvx7g-DLPbktAd9ZHgwqsuNib0QDZoeiI1ZSPjGX_4LSLitCabowu9WJE8DJGPsJli0AurNmYWcWudluPeWr3Tthvg0rIB06qkQCMf06XU0qMax3JLCNmxfKVF0l5n3Bn7Bc7OO42zpfTtHPjt4UXI3yw6j_a5B6b7U0H-vfa1OWTuNwOyWYsfO8X5KIfAslvdKBqOU_0BwvM_2KPJRJjrlpL-TEnHfEl4Ct2YFWkRrteg5X0mgVW4idWJLOaFKx018p6krfRNvogaRdWBrHRrvnGGuMWnRsrBsw0qjLM4myrnPX3ROZBtcZ1lSW2qStVybkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
ارزش تیم امید ایران: 13 میلیون دلار
🇰🇵
ارزش تیم امید کره شمالی: 2
میلیون دلار
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/140452" target="_blank">📅 15:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140451">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8gij7GoL76o0OGQfRoBCmy6ayTt6hV-4HkZqjrSohVeEjBlCfd9etwgBb8NM3k76GUFjrX_4gTwDMhaokiWQQKN_-x8AuvNe3MIEKHMet95kP3HBQA6RJFunPQMr7CLExx2Gs3eGmLvaLLSLTl6BH1lT4s3bb5Z7_gFnwtT10qMkg3CLjASvjIIgGAg7doa1FqabHpXcAMwq80veDsi0ZSb7PXYfPL5rYiS2O_S0ac50xu-WRT6h-iHMqCwByKdp7cn9XX06z7YnfyWQ16czgCscqeSwgqwRuUfmkHJ7o5reXb7C2EfqDpiSyzQrUluM-5tmJXLqP9xDgZ8NuQMRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
🏅
پرسپولیس مدارک جدیدی رو به کمیته استیناف برای 3_0 شدن بازی دربی ارائه داده
⚪️
حتی اگه رای استیناف به سود آسانی باشه پرسپولیس تمام این مدارک رو به CAS میبره
✍️
همشهری
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/140451" target="_blank">📅 15:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140450">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNg6lVpv5HuKrrTW-w-90BjDch2OC5Xn_5-J4K1uKO3e4lRVqBzw7IOYfKRZAEcIFHyzVn_jAbawk5aGWg482RwI3xr43nA7v4sGHGm1Nu1aRZlwo9B1J-6cYoyBylLNrdSOhaftWzZ4YpvPNKdDXzzftMsFuWNFyiUjtJj0qxirTgMwznWy42VldVWuiwNRzYo7QRq4aG8uIFZbHGKWOhDhAUzpAYFAJNXqbd5WoXMW-SvMu1CAqGvWBtXXmA-qXG8qBgBZepk73YjjAgwcKcW4WLvW4NLI8seQO9p_k4bxWkaNlK7l7O_OI4TbyMSBjCuK_2GL4jzp1sR_euNNWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
جام ملت‌های والیبال اروپا به اوج رسیده!
🇧🇪
Belgium -
🇸🇮
Slovenia
⏰
Tonight 17:30
🏐
بلژیک با فرم هجومی خوب و درخشش فره رگرز وارد بازی می‌شود؛ مقابل چک هم ۳ - ۱ پیروز شدند و ۱۵ امتیاز از دفاع روی تور گرفتند. اسلوونی اما بعد از برد قاطع ۳ - ۰ مقابل صربستان، اعتمادبه‌نفس بالایی دارد و موجیچ، پایِنک و کوزامرنیک می‌توانند فشار زیادی روی دفاع بلژیک ایجاد کنند. نبود تینه اورنات به‌دلیل مصدومیت، یک تغییر مهم برای اسلوونی است؛ بنابراین دریافت و عملکرد موجیچ اهمیت بیشتری پیدا می‌کند. بازی از آن مسابقه‌هایی است که احتمال کشیده‌شدن به ۴ یا ۵ ست در آن بالاست.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد سایت شو و دیدار هیجان‌انگیز امشب رو پیش‌بینی‌ کن:
👇
🟣
Wincobet.com
🟣
Wincobet.com
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/140450" target="_blank">📅 15:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140449">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✔️
به نقل از رسانه ها دنیل گرا بزودی با گرفتن ۲۵۰ هزار دلار از پرسپولیس جدا خواهد شد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/140449" target="_blank">📅 14:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140448">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
❌
❌
فووووووووری
🚨
محمد حسین کنعانی به علت مصدومیت دو دیدار بعدی پرسپولیس برابر صنعت نفت و خیبر را از دست خواهد داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/140448" target="_blank">📅 12:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140447">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‼️
🇮🇷
بهت و تعجب ملی‌پوشان امید بعد از حذف از بازی‌های آسیایی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/140447" target="_blank">📅 12:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140446">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c126edce8.mp4?token=Gb9xNpEfjHYkXRWij9sI30ig75h_xn_jLtYFXd4Gjg9IHnSw08Uqy10y5Y8jDDsqYo-Hz8guS9qoAc_PLDwCGNQsBRvX4bz76vQqW9iBt7tl70slfJJorylmYXP9o-mYxqpp3LVG-BxqyR4Pjf6oKwifaiw3qwBk9Oo654nuWxx1fGlMh33O-Gf-8o28ap2YmlwL19boC59TLi381xro5xqm6qhgm3Iq-5ThrMWWuGB1pKidA1SSSo_gnYkSAPZpUb8ZCkIUpjOT5_IHInOQHyl1u-dQ4NUMARCMJEe9wenabsYJ6yH15kdB4DDiKHc1oepFWWJ-RqGx0pr5o0JpRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c126edce8.mp4?token=Gb9xNpEfjHYkXRWij9sI30ig75h_xn_jLtYFXd4Gjg9IHnSw08Uqy10y5Y8jDDsqYo-Hz8guS9qoAc_PLDwCGNQsBRvX4bz76vQqW9iBt7tl70slfJJorylmYXP9o-mYxqpp3LVG-BxqyR4Pjf6oKwifaiw3qwBk9Oo654nuWxx1fGlMh33O-Gf-8o28ap2YmlwL19boC59TLi381xro5xqm6qhgm3Iq-5ThrMWWuGB1pKidA1SSSo_gnYkSAPZpUb8ZCkIUpjOT5_IHInOQHyl1u-dQ4NUMARCMJEe9wenabsYJ6yH15kdB4DDiKHc1oepFWWJ-RqGx0pr5o0JpRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
بهت و تعجب ملی‌پوشان امید بعد از حذف از بازی‌های آسیایی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/140446" target="_blank">📅 11:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140445">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmbecca5pyH5zOBAWo8fw5DKqXZCb3IVxNNWs9M0Vg_UNoiPpJ2mab_M9ef2tepnAQTcwv8RyV1C4x1GVISy60U49VC-9IWNXmqbjwe1PDhmAVqgSAQZcxK0rE50FDobJ7YEWmFj2_6_J-vJKdNaIuJoWRq2MbQuo6iPUudNJ5d6HjsFSN8qZcgnlsKEtHtwWJAyiJqaFE1ESTAN0mGVHFfEFvKFx-wW8qtnk1_IJ-IQWpMBkShoY6FCsR8LBew3aIWoP7iYOlSKpHgncF2JaJxcsODGr2iWtUUcoh7sID0rb2Xh56FPQruSF3LcKfDlpzHb5Oa7MNOz2eqsE2Y41Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
تیم ملی امید‌ با این کادر با دانش به کره شمالی باخت و حذف شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/140445" target="_blank">📅 11:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140444">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
آقای حسین عبدی ..بهترین تیم امید و ریدی توش و تیم و حذف کردی و از کره شمالی چهار گل خوردی ..
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/140444" target="_blank">📅 11:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140443">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
گل چهارم و ببین ...از وسط زمین طرف تک به تک شد ...این چه تیم امیدیه ..آقای عبدی چه گوهی خوردی با این همه جووون با استعداد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/140443" target="_blank">📅 10:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140442">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c29d58e82a.mp4?token=PsAD6mUs2nVNaieeYKbF3MRacwSGSkTEoX4laOvhQ3zadGn33MR9R3iysn3LNvmSLHiYOeOadd_7pflj5x-crPUUIUgp-aJ1s5a8WIaPM5_NqeoZUHM__NaRzx_FLtT8bk-0hWp2_Tfa6Z1pq8nivN3tpWyTFV3TDVhBUrtoV1sv5ApTuGLNutsZTTXvD1MDKq2s3-Nd01RcvCVpg8DUxJhsYXMBnzdk9DPKIthVDSvXUFC-fC6p44oP4_AQvI3vH8RnMucYQyjmsXnGSYArULgM3COjZAVL_CL6BpxkBZEHefZCoirOw4qGBU5vELYiwyN9X4dtXuedkBEegi7S2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c29d58e82a.mp4?token=PsAD6mUs2nVNaieeYKbF3MRacwSGSkTEoX4laOvhQ3zadGn33MR9R3iysn3LNvmSLHiYOeOadd_7pflj5x-crPUUIUgp-aJ1s5a8WIaPM5_NqeoZUHM__NaRzx_FLtT8bk-0hWp2_Tfa6Z1pq8nivN3tpWyTFV3TDVhBUrtoV1sv5ApTuGLNutsZTTXvD1MDKq2s3-Nd01RcvCVpg8DUxJhsYXMBnzdk9DPKIthVDSvXUFC-fC6p44oP4_AQvI3vH8RnMucYQyjmsXnGSYArULgM3COjZAVL_CL6BpxkBZEHefZCoirOw4qGBU5vELYiwyN9X4dtXuedkBEegi7S2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل چهارم و ببین ...از وسط زمین طرف تک به تک شد ...این چه تیم امیدیه ..آقای عبدی چه گوهی خوردی با این همه جووون با استعداد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/140442" target="_blank">📅 10:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140441">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
آقای حسین عبدی ..بهترین تیم امید و ریدی توش و تیم و حذف کردی و از کره شمالی چهار گل خوردی ..
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/140441" target="_blank">📅 10:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140440">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✔️
تیم ملی امید راهی ناگویا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/140440" target="_blank">📅 10:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140439">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✔️
✔️
چند روز پیش یکی از نزدیکان میلاد محمدی به ما گفت؛ این بازیکن بخاطر شرایط خانوادگی قصد بازگشت به ایران رو نداره///طاهرخانی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/140439" target="_blank">📅 08:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140438">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uht-bIlzKuYcYHO2E6BzhsgFYI3rmoyIBFLmODxPpZB1kYWD0lxg2VJYTwOUj9Sxw_hVepNwKV7VLxdChH8ROMHblGt2N2M-vvNS28Hg5t27mVlrD9P3_HN9WjsTcLr4NiywUJoNJ5WvN4x2Ewn2rsIBdol96Nqm8GMvfao-sZeoZI-1VMJMS9kcTQ6zrPkEqcYHTqM91y3SK74yS161Uxqljvqy4WelVz7Z2OrL_6xUp98WnSeazo8hCjhyCzNCAzh9SSkgGsQelpd8JXIt6AUOsIGYEkBzeeLBhe6vKgTRf-xsjm7nzfbu3GnPUvvo2YtCfhw04rK54GuJPT1GRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
♨️
🤩
خبرورزشی:
🔴
🔵
🇮🇷
پرسپولیس و استقلال در نیم‌فصل برای جذب محمد قربانی اقدام خواهند کرد
.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/140438" target="_blank">📅 08:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140437">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✔️
✔️
✔️
✔️
علی علیپور به دلیل مصدومیت زانو حدود سه هفته باید مراحل فیزیوتراپی و آماده‌سازی را پشت سر بگذارد و در لیست تیم ملی نیست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140437" target="_blank">📅 08:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140436">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
❌
ترکیب تیم امید ایران مقابل چین
✅
✅
محمد خلیفه، دانیال ایری، امین حزباوی، فرزین معامله‌گری، ابوالفضل کوهی، امیرمحمد رزاقی‌نیا، اسماعیل قلی‌زاده، عباس کهریزی، مبین دهقان، امیرحسین حسین‌زاده و پوریا شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/140436" target="_blank">📅 08:47 · 01 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
