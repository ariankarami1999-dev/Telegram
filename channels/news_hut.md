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
<img src="https://cdn4.telesco.pe/file/ZhlkQFHyBR2iTjyGzrG5ckF4J7tIZcQgI9Tr7ZN9jtNe4do8MRda41UhnuMrnSMJKUza8e2WfNt7IRje7y0-HIcsd31ni7HPAFcHDgHRU4qncsNOBfspv-DiedlJ-bTw6zArkLl8QtHb8bRzihmrIWwMgOKmeABsm2RNHqJGwg4mPIdgz_PWhk1Cq3amIwQosozRj6Tl6BrGeV6jNKRXpYTZFadOmfGOVnYfNeIXbiN108rtenfr5AZBidc652wqnEyddGEplDqr-q0kvwvBN0zfXlQW64s5cv07osk2S2kfpxDERXL_LTVNoU-iHGiAlPoxyF50275GrkM0mlPgFw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 104K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-20 04:57:01</div>
<hr>

<div class="tg-post" id="msg-73139">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73139" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/news_hut/73139" target="_blank">📅 01:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73138">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qaVyTyM5_QxpCcudLLy0GJc2sBamo-IuNdy5WjEdqNN0zyIJkxgR5TKZmOueJj91PeiBqij4sLVas_Tw1puuUV8fRoxZTAhLO_h8npWs0xL6mnQGf0ak9iGAeErN3VXtCfPc1hoG69qTagBlmsZLAnlyHEweRBCqEx-CZkccAlFnr-ElLuBlJMYVTRf6onT2CXCmx18INaeXBOzxN858h_RfSo7sED4XPReyKUJCBUHZv8z0rbD75FIddEt_uScaZPjVbSQqqK5O9g-YRcVcY52EL_-wcXHGLAi3QQ0R68mH1v5EoXCtDGq3gyUQ4tlR5IXZEWKMMWjzayhpsDxJBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
[
قوانین رو در سایت مطالعه کنید
]
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/news_hut/73138" target="_blank">📅 01:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73137">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fi9WKRvstiP1My3ojy8x3Pkk9swCs-1EGVqZ78adqPaYoSKs9-ff3H9CQzTlr0zIB2VoyFzSxWNhpXK9gIhX-AuiHO6KQVXB4iwVCMWcVHwaey7tiSP4IU9bMhi8DfJwltCV8_99QdEZehyPS6D6-L8_6eKymITiUvlKZXkotBvVx61LiwBZaNgONDJ5q6NjRCuWwBdG8V9Xya6WUwFUUaijrt-UcCg-0uwm6-4zBuvqggH-DarGhRc9SwpGhGsaTB-WBYvWdJ6AZTB0DRtdxVtCT0dDSNwZuQQm725ha5SHMpltyYl1U6DJF1LppXJDsSOTpozfZt-Ne262Xt3Nyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی:
«آمریکا با بعضی از شروط هفت‌گانه ایران موافقت کرده، اما از نظر ما پاسخ آمریکا کافی نیست.
دیپلماسی ایران تغییر کرده و دیگه اوضاع به شرایط قبل برنمی‌گرده.»
@News_Hut</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/news_hut/73137" target="_blank">📅 01:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73136">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ویدئوی لحظه اصابت موشک حوثی‌ها به فرودگاه ریاض
تصاویر دوربین‌های مداربسته، لحظه اصابت موشک بالستیک حوثی‌ها (انصارالله) به ترمینال ۳ فرودگاه بین‌المللی ملک خالد در ریاض، در روز گذشته رو نشون می‌ده.
بر اساس این گزارش، دست‌کم ۱۳ نفر کشته و بیش از ۳۰۰ نفر زخمی شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/news_hut/73136" target="_blank">📅 00:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73135">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c13d27cb81.mp4?token=SF9GZ7nxWQ7KWbM5nIbHyD9unfzuhxhluU6e3V4qxtJUpW6Vt4ZAOQ6g-aOD43DURcwCEpJOJi0LyQdS2lVC0l-1TrQGh8V7Y_OG-F5r_RKF0ENhCjL3VH5BbnxzfVnVsMaURQAVfCHeUiaJDVwitb0YMyrBs4qaUanINLiJt4SrgwPwfQnV5iyW6a2SaiTgpxTOs4tZjsqtTU4lXpmTq0IPX_O2H92DWCJCqX-NE1SbeAAcw7GAemTbtSKZyWRltmwIeUlAvyPEDqddpajsF863OqdKsMnvNebvHUrXeJNWlkwVABRmNz6GlpJa3trfX8G2gy8yOWt0JFkMNNoOjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c13d27cb81.mp4?token=SF9GZ7nxWQ7KWbM5nIbHyD9unfzuhxhluU6e3V4qxtJUpW6Vt4ZAOQ6g-aOD43DURcwCEpJOJi0LyQdS2lVC0l-1TrQGh8V7Y_OG-F5r_RKF0ENhCjL3VH5BbnxzfVnVsMaURQAVfCHeUiaJDVwitb0YMyrBs4qaUanINLiJt4SrgwPwfQnV5iyW6a2SaiTgpxTOs4tZjsqtTU4lXpmTq0IPX_O2H92DWCJCqX-NE1SbeAAcw7GAemTbtSKZyWRltmwIeUlAvyPEDqddpajsF863OqdKsMnvNebvHUrXeJNWlkwVABRmNz6GlpJa3trfX8G2gy8yOWt0JFkMNNoOjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از مدارس پسرونه، اسپایدرمن تبدیل به اسپایدرعن شد :
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/73135" target="_blank">📅 23:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73134">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cad58aeb38.mp4?token=K5dZ972oeY7oyZGaaPoDFSHJSB_3v7FJKN9VczOJOMC4KLL_J2e2ZU5lCnrZggo7uR4GQx2ftJJbJRIMLowQ4mzCJ2rqWPSViBCAQpTiW5EFO2rNSWK0aX2f606YB9_VGbPHvyxQJw8BcXy29B2koSF9OqfkWQHbce1z6rGFX8mFnpeP7B7lw9Ux-wOodNlCzEpiyk8N2FWVZN7cVGtnJkydHUDJg0vsGiBUIZDdH4FxMx_kY1ArkSj37gqt0AaM3yyoLYj-ZO8whcrzU8pkM2LmEQS5O7RqMlL_-M7i5sQZdfjzXUw_n2YK7T3GleH3iru1HKN7mXUOEyzQinBIpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cad58aeb38.mp4?token=K5dZ972oeY7oyZGaaPoDFSHJSB_3v7FJKN9VczOJOMC4KLL_J2e2ZU5lCnrZggo7uR4GQx2ftJJbJRIMLowQ4mzCJ2rqWPSViBCAQpTiW5EFO2rNSWK0aX2f606YB9_VGbPHvyxQJw8BcXy29B2koSF9OqfkWQHbce1z6rGFX8mFnpeP7B7lw9Ux-wOodNlCzEpiyk8N2FWVZN7cVGtnJkydHUDJg0vsGiBUIZDdH4FxMx_kY1ArkSj37gqt0AaM3yyoLYj-ZO8whcrzU8pkM2LmEQS5O7RqMlL_-M7i5sQZdfjzXUw_n2YK7T3GleH3iru1HKN7mXUOEyzQinBIpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان: اگر لازم باشد برق اتاق‌های دولت را خاموش می‌کنیم اما نمی‌گذاریم چرخ کارخانه و تولید متوقف شود. مردم همکاری کنند فشار دشمنان شکست خواهد خورد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/73134" target="_blank">📅 23:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73133">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67b9ee6a71.mp4?token=gE-S6nuK696uAH7Pkdqv0Od_vZCG1GjD6t5uwzORBgSa_PvJ5mAv-iYnYBRTJPG_wh72Pe0wxPimwfjhYqtVWZtbQsoCzRkp3lsmAHYX4e9q3JKbnjqxZM3LHNc-fQzT7VQiuRvY-FWT5DhBDpCNuUCF2c9QLFLPgzxAPYho9qPU5xhiiL3tay14IIVMN8L23ao54dtP39GzXAtuTKZkgGEz-FrvJKlSv4AAE0mIG4MBvlzCElYS4qjskESKL5jKeTWGbOnPSzkXmSouDpQ5G-J1CcJ4nq3Oho67inCWkSXbRuiv_YUHAnhPFq6K-uNkKTGgGEKXdOnGZd30BfASHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67b9ee6a71.mp4?token=gE-S6nuK696uAH7Pkdqv0Od_vZCG1GjD6t5uwzORBgSa_PvJ5mAv-iYnYBRTJPG_wh72Pe0wxPimwfjhYqtVWZtbQsoCzRkp3lsmAHYX4e9q3JKbnjqxZM3LHNc-fQzT7VQiuRvY-FWT5DhBDpCNuUCF2c9QLFLPgzxAPYho9qPU5xhiiL3tay14IIVMN8L23ao54dtP39GzXAtuTKZkgGEz-FrvJKlSv4AAE0mIG4MBvlzCElYS4qjskESKL5jKeTWGbOnPSzkXmSouDpQ5G-J1CcJ4nq3Oho67inCWkSXbRuiv_YUHAnhPFq6K-uNkKTGgGEKXdOnGZd30BfASHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این کلیپ مربوط به پشت‌صحنه یه تئاتره؛ جایی که همه با هم دست می‌دن و همدیگه رو بغل می‌کنن.
+ عرزشی‌ها هم از این صحنه به خشم اومدن و می‌گن باید این بساط جمع بشه؛ حالا هم افتادن به جون عوامل تئاتر!
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/73133" target="_blank">📅 22:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73132">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3915a2c4be.mp4?token=bryAnmdIHFW8ToqfKBPF4E19DKa27Y28at_c7m994YT4yudIW1Rm3EXuodKcfnhCTar0LbCTNKhVLrEozTT1Kk9rA6KxLwcM636dzScMDfjvtPxZ_vyUwHWZfeU2h0_BVjCye8j0k84MVoJ8lwNJC-r-W3ruFZRsQGLR4h0M1Md8tTvwY66wxuHZnVCxXb4yPo1fYdCmMI7Ppdfm_h7YhfIOGPc5X_tqIc6_e6r_DXPkfguMdsiQXuWgOotYInmD8TO2NogtNbJ6KO5Tddp5SyNybbEd13q-uXcRs3fG-thGniDKIS5JpGnDb_fBr2wttIW_Epo_5zhh-Iu0WLyDtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3915a2c4be.mp4?token=bryAnmdIHFW8ToqfKBPF4E19DKa27Y28at_c7m994YT4yudIW1Rm3EXuodKcfnhCTar0LbCTNKhVLrEozTT1Kk9rA6KxLwcM636dzScMDfjvtPxZ_vyUwHWZfeU2h0_BVjCye8j0k84MVoJ8lwNJC-r-W3ruFZRsQGLR4h0M1Md8tTvwY66wxuHZnVCxXb4yPo1fYdCmMI7Ppdfm_h7YhfIOGPc5X_tqIc6_e6r_DXPkfguMdsiQXuWgOotYInmD8TO2NogtNbJ6KO5Tddp5SyNybbEd13q-uXcRs3fG-thGniDKIS5JpGnDb_fBr2wttIW_Epo_5zhh-Iu0WLyDtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه مدعی شد سومین نفتکش از دیروز تاکنون در جنوب تنگه هرمز با مین دریایی برخورد کرده و دچار انفجار و آتش‌سوزی شده است.
سپاه هشدار داد با کشتی‌هایی که سامانه‌های ناوبری و شناسایی خود را خاموش کنند، به‌شدت برخورد خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/73132" target="_blank">📅 21:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73131">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11e4cb03a5.mp4?token=JTMYakcFcbVy4tCF-yWhDtch2DMt5LHJ4QYDdJZ1bOCc82qy1gL7SBmnYNSvm_LA9RGccmJn3lYbpI1GAQQXqochgOpHjCg_MaIPhTtUi07kceKVbImi8RAR2MLevo3HSp1VvqpwAoIzrfsQreygcOVzbgWaDAEA4Zc-rLnJOzBV8g3hieHZF8ZDC5Dt4dx7yzSsIrQS-yUU5EBXS9JJoxuF_li_mwC1JEVIG33ATU2poqSqV9hWF7X3c4ye48yJwV0aDLTetZN2ag4wKGlQfREOLV1gi4uSIMDfzxVGRTwZ7uDiW4qmgE-WYo03bCGuPVMA57VhQUZa0oZ5ghlbww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11e4cb03a5.mp4?token=JTMYakcFcbVy4tCF-yWhDtch2DMt5LHJ4QYDdJZ1bOCc82qy1gL7SBmnYNSvm_LA9RGccmJn3lYbpI1GAQQXqochgOpHjCg_MaIPhTtUi07kceKVbImi8RAR2MLevo3HSp1VvqpwAoIzrfsQreygcOVzbgWaDAEA4Zc-rLnJOzBV8g3hieHZF8ZDC5Dt4dx7yzSsIrQS-yUU5EBXS9JJoxuF_li_mwC1JEVIG33ATU2poqSqV9hWF7X3c4ye48yJwV0aDLTetZN2ag4wKGlQfREOLV1gi4uSIMDfzxVGRTwZ7uDiW4qmgE-WYo03bCGuPVMA57VhQUZa0oZ5ghlbww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم وایرال شده از جشنی که یه خونواده، برای اولین پریود دخترشون گرفتن:
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/73131" target="_blank">📅 21:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73130">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa77f7e16d.mp4?token=sQ0qIcA_JXq4gHOqOVKjTxRk1x5NTnbk5dtQX4Gx1hqyuzT1m36t_RO1XcTEf3in4XsmyD5qtkLu8QfkgYNZTwKuCwD905mGFLoDtY0Ey5TtB_AAh9wh4NRDJAyVtzNjPmrqJBOqNW7Vs8PB8BuUbVeiHUqvfmMKi-oIEtNwNtw7r55-G3zjEZ-wJC5FyusACrTzKQBa3NAjd5RQEL_nFPgXGI6NIEH0k7jIQ50IhPgMTqO7lpCh1WPipHktU2hMwpq5ka52tspYFe9oc4qIKuFCKm0Z3aSwGHmQnj95ReKtyF_JVy3HOhPhJNdv-3GoFbks5d6fQI_iEcR3uRxOBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa77f7e16d.mp4?token=sQ0qIcA_JXq4gHOqOVKjTxRk1x5NTnbk5dtQX4Gx1hqyuzT1m36t_RO1XcTEf3in4XsmyD5qtkLu8QfkgYNZTwKuCwD905mGFLoDtY0Ey5TtB_AAh9wh4NRDJAyVtzNjPmrqJBOqNW7Vs8PB8BuUbVeiHUqvfmMKi-oIEtNwNtw7r55-G3zjEZ-wJC5FyusACrTzKQBa3NAjd5RQEL_nFPgXGI6NIEH0k7jIQ50IhPgMTqO7lpCh1WPipHktU2hMwpq5ka52tspYFe9oc4qIKuFCKm0Z3aSwGHmQnj95ReKtyF_JVy3HOhPhJNdv-3GoFbks5d6fQI_iEcR3uRxOBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی سازمان انرژی اتمی: منافعمان را یا با دیپلماسی می‌گیریم یا با نبرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/73130" target="_blank">📅 21:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73126">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bf520c338.mp4?token=W-8GFaMV6gREUQs0D0BliJKyUW-31qf1EdfKTAQlZJ-VxQ5qH9ICNKf6m71qPK3S09Hi4Z1HNa3vIBmvRXgBjrvwgAzrpsW91Hqr_RsV5Cbrvp_F8bWysq2nkzQ1Fsqt_Q1ryiKXMlxR04_MlGIx2qMqN1S1cTcVN7j1xkXfHaioRrPz_Csjwo5-YclYISNprNXPVVb2b5pyNYXKXikHt2aQdLSeRDOzARO5sBNfTnNvQSeKBT1l525tPv4GLuXSiRYR1qbHqgDD5YOvbzenMFI8cFH1LymCtvPvqVCq7U8rgDZUHbPOc95_eADUwV6tR4oeVnzHVWbgwkv-RgfHfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bf520c338.mp4?token=W-8GFaMV6gREUQs0D0BliJKyUW-31qf1EdfKTAQlZJ-VxQ5qH9ICNKf6m71qPK3S09Hi4Z1HNa3vIBmvRXgBjrvwgAzrpsW91Hqr_RsV5Cbrvp_F8bWysq2nkzQ1Fsqt_Q1ryiKXMlxR04_MlGIx2qMqN1S1cTcVN7j1xkXfHaioRrPz_Csjwo5-YclYISNprNXPVVb2b5pyNYXKXikHt2aQdLSeRDOzARO5sBNfTnNvQSeKBT1l525tPv4GLuXSiRYR1qbHqgDD5YOvbzenMFI8cFH1LymCtvPvqVCq7U8rgDZUHbPOc95_eADUwV6tR4oeVnzHVWbgwkv-RgfHfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی امروز گسترده‌ترین رزمایش نظامی خود از ۲۸ فوریه تاکنون را با مشارکت سپاه و نیروی هوایی ارتش برگزار کرد. تصاویر منتشرشده، پرتاب پهپادهای انتحاری شاهد-۱۳۶ و موشک‌های بالستیک و پرواز جنگنده‌ها بر فراز تهران و شهرهای دیگر را نشان می‌دهد؛ تحرکاتی که می‌تواند نشانه آمادگی ایران برای دور تازه‌ای از درگیری باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/73126" target="_blank">📅 20:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73125">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">محسن رضایی:
«اگه جنگ دوباره شروع بشه، خیلی از کابل‌ها، دیتاسنترها، مراکز هوش مصنوعی و زیرساخت‌های دیگه تو منطقه نابود می‌شن.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/73125" target="_blank">📅 19:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73124">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fW-gJb0leROaxJ2RoSOurEkRYKve5D8zbZx8ehY0ja-d8CsipprPimOdGT4pJd4FdeGaROkO69yefkgNjpsYTNmoXQ8tNaHUfpYGm529msgCHa0c_MUaITdmUrPuv47sEZAbKaiju-mFHAlK_6rrAb3GU_0gff-txEAUjZxWEG-fZiP7lLpJPnqLYbN6Un1LUTqtkwtzXAgkhyXbfe5yAOjVpYULuGLr7e-XxEHHkyxeVlWuukVFS32PaISUTdFyqoBHi9m8xFo-E15qh1dUyenWt1kCwgQqXyO2BL14YEbK-QSZhsa5fEYZaNEeVt8vKZAhbkcG9T5rkl9hiMLVug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی:
«ترامپ به قاچاق روی آورده و با استخدام تعدادی مجرم که در آب‌های ساحلی عمان فعالیت می‌کنن، این کار رو پیش می‌بره.
اون هر روز ادعا می‌کنه تنگه هرمز بازه؛ اما من در پاسخ می‌گم شما مشغول قاچاق هستید، در حالی که تنگه هرمز تحت کنترل ایرانه و ما مدیریت اون رو در دست داریم.
طی چند ماه گذشته، هر شب پنج شناور مورد استفاده قاچاقچی‌ها رو در تنگه هرمز هدف قرار داده‌ایم.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/73124" target="_blank">📅 18:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73123">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee20290170.mp4?token=N8u0KRbKofWGMYEYqDwLZYt0AmyvatkQFTjaRAaCK9dC8UA-92HGNY76WvqdOansZ_-lAkukwjVkJ3ikov1zMp-nhecMkucv1zzHCYRGbbyPULsVXi8ESVqOLpoz1IUk3QjQiz1v6MPc1tKJWYRFtrsSm7uZ4NaC5mE9bCGUFD6Qx8ngLrQqd8wyNWRrTAmCB9FEoCtgflExNs-DqAuUckqf-N-pco3n_6eDkZOrE36F9lD6Z7kpwqmEHz_zZEgZfF6P1PCeLqhIteLmlKWzTdw5kR8hYiNiwHG0wHmJyZ_RD8KYgrB71LnD8aVBksvd97XiuOWJyFfucc_y7WoRhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee20290170.mp4?token=N8u0KRbKofWGMYEYqDwLZYt0AmyvatkQFTjaRAaCK9dC8UA-92HGNY76WvqdOansZ_-lAkukwjVkJ3ikov1zMp-nhecMkucv1zzHCYRGbbyPULsVXi8ESVqOLpoz1IUk3QjQiz1v6MPc1tKJWYRFtrsSm7uZ4NaC5mE9bCGUFD6Qx8ngLrQqd8wyNWRrTAmCB9FEoCtgflExNs-DqAuUckqf-N-pco3n_6eDkZOrE36F9lD6Z7kpwqmEHz_zZEgZfF6P1PCeLqhIteLmlKWzTdw5kR8hYiNiwHG0wHmJyZ_RD8KYgrB71LnD8aVBksvd97XiuOWJyFfucc_y7WoRhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق گزارشات رسانه‌های عربی حوثی ها مجددا به فرودگاه ریاض حمله کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/73123" target="_blank">📅 18:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73122">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">زلنسکی در گفت‌وگو با باراک راوید:
«اعلام آتش‌بس برای من هم خبر جدیدی بود. اما اگر روس‌ها با آتش‌بس در حوزه انرژی موافقت کنن، اوکراین هم موافقت خواهد کرد.
اگر رئیس‌جمهور ترامپ این توافق رو با پوتین مذاکره کرده، لطفاً به ما بگید آتش‌بس از چه زمانی شروع می‌شه. ما آماده‌ایم و این توافق رو می‌پذیریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/73122" target="_blank">📅 18:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73121">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTGXL2q9qwQk8BDeXEYd8MkuWOPGp4PRpGppS6FCnXP6RVJDBWgVMicqcwUQ-_kh8g66YIbIsSzh_TEFcD--0ciqRXQbif_U3VZoFL3J7PNzlOCK2FFUJD-wqdwVT4gIFVJFAdet9WdqfSVYbTDps4Lib_nYNs-hUDYvjRo-vfxwIcELKKAngSss0bifi_jdK2auR4IDkVAmCovKaltSphuToLLnGaq9FalAXYdK_0S5ti9-bjDscB0OicLtAclAkFBm0GRscuqJ5aUhxcI__hESpQIHS83C_XfLxs9CImKlPqD35jgCQyM_VWKHZ6gClwly67zqLkecPWK3trV0FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ از آتش‌بس انرژی بین روسیه و اوکراین خبر داد
«از همین لحظه، آتش‌بس در حوزه انرژی در جنگ روسیه و اوکراین برقرار می‌شه.
هر دو طرف با این توافق موافقت کردن. این آتش‌بس رو نقض نکنید!
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/73121" target="_blank">📅 18:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73120">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73120" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/73120" target="_blank">📅 18:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73119">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gz8-Fo5AB8jJbOZnMrxAOA8UxcofpxzwIkwTWFszJb05hwFNWf56iiQqFgNmSWjjM5U1wXdnAN2E7G1GpdvWXwQwgIzNYAoU3EE_Pgww7HLowwee90u9cRtw7gSg4fJQZhLjBpA_Lk7nRsFqKMbE2ojkAlc0H8Y68XM6l0XGCvARlUR6RdnaxnevqbBg8WulKxJVvtxZnlr9FILWYYAdej0ckzrnE8vs3V6QatAikuCe4_vuXomiPOZFKwnekfT-U6NVFhtFYCLsRmJ2JZpZbKuQ8cwCxyFHQD-Ebl0JYwGD6Nru7Pl_AeCY83ZOUtSXR_SiONFdNWKP0p0rTjZu2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز منچستر سیتی
🆚
لیورپول
را در
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
منچستر سیتی: ۵ برد و ۱۴ گل زده
لیورپول: ۴ برد، ۱ تساوی و ۸ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/73119" target="_blank">📅 18:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73118">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb6d17c940.mp4?token=bFWnSVR5EbGbS2t6aKruAtr15dKGRVtBN_yePede-N4Dax73elX1nCa-hiV9RrXPjSQ3cXBIRQZMZcx3845cJ1JrPItPbURdzsD_1gB_MdEyse_ZseBh9QKjUKVj9c9nJpg9NdePOyHhV0NWWUiGlIaA9BxlSbgasfF7PKx0SPA1uQ1-tDhKaTGiCQ_etAhcBdR6T2dr0MQsg8X3Mpz8IA9KOqvtEhr5lKK1gRpZ350Sc1ELek-4teQVkRZZjh5i4Y3rbM06B9iMf1d_YTmuzMLFzHVguk81yEY7TSEmWdOIOVnAdcYPL-ruOlip4GW4wttNnQ72ziKA6DIX3ImJqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb6d17c940.mp4?token=bFWnSVR5EbGbS2t6aKruAtr15dKGRVtBN_yePede-N4Dax73elX1nCa-hiV9RrXPjSQ3cXBIRQZMZcx3845cJ1JrPItPbURdzsD_1gB_MdEyse_ZseBh9QKjUKVj9c9nJpg9NdePOyHhV0NWWUiGlIaA9BxlSbgasfF7PKx0SPA1uQ1-tDhKaTGiCQ_etAhcBdR6T2dr0MQsg8X3Mpz8IA9KOqvtEhr5lKK1gRpZ350Sc1ELek-4teQVkRZZjh5i4Y3rbM06B9iMf1d_YTmuzMLFzHVguk81yEY7TSEmWdOIOVnAdcYPL-ruOlip4GW4wttNnQ72ziKA6DIX3ImJqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت درباره ایران:
«نمی‌دونم این ماجرا چطور تموم می‌شه؛ هیچ‌وقت نمی‌شه از قبل دونست پایانش چطوریه. دیوار برلین هم بالاخره یه روز، یهو فرو ریخت.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/73118" target="_blank">📅 17:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73117">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4be03fff7.mp4?token=nGXWvdaBHuMOp13va-2ti78aE-9q_DT_gvuIoLg0qEmUZIHosKYouQyjYp58vygqbnrNRze1k175a-af1TdbOPRNeqVvnjfjttfhO0SezERVDqzJCvWpKeq0DmmmqsDxIPalm6Bu8kWeQFrvZcPaHT9dwIxytBF6YXo8n8eyo3gOseIaQ3JR1h9zZsAb4Sr1L4UfXyKm2Jo6_6D_yMXn5AWqG9jEbOUsFgkmZ9_J6xeXmI1Ga-tqDnjFy_Vn8hzxaWHSyyI2CYtdInK5HBR14DsGeU5ozTrWWdgl9M9GKS8fVKlXqAqNh7tEjx88i0yjMNxgeSRRb_1qNUXgtdqe_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4be03fff7.mp4?token=nGXWvdaBHuMOp13va-2ti78aE-9q_DT_gvuIoLg0qEmUZIHosKYouQyjYp58vygqbnrNRze1k175a-af1TdbOPRNeqVvnjfjttfhO0SezERVDqzJCvWpKeq0DmmmqsDxIPalm6Bu8kWeQFrvZcPaHT9dwIxytBF6YXo8n8eyo3gOseIaQ3JR1h9zZsAb4Sr1L4UfXyKm2Jo6_6D_yMXn5AWqG9jEbOUsFgkmZ9_J6xeXmI1Ga-tqDnjFy_Vn8hzxaWHSyyI2CYtdInK5HBR14DsGeU5ozTrWWdgl9M9GKS8fVKlXqAqNh7tEjx88i0yjMNxgeSRRb_1qNUXgtdqe_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت درباره ایران:
«اگه این ایرانی‌ها کشورشون رو دوست دارن، خب تبریک می‌گم؛ می‌تونن همون‌جا بمونن!
این فشار مستقیماً به نخبگان و مقام‌های حکومتی ضربه می‌زنه؛ دیگه نمی‌تونن برن لندن و اقوامشون رو ببینن، تو پاریس به دیدن دوست‌دخترهاشون برن یا به پول‌هاشون در سوئیس دسترسی داشته باشن.
اونا از دنیا جدا شدن و ما به ادامه این فشارها ادامه می‌دیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/73117" target="_blank">📅 17:33 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73116">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cfeac3aa6.mp4?token=lr4jiKPRh0QITzI3PmvFfSOSytVGTxVNg7CV_uIus2RsUAS2AmLXaXoo8nCcitbqn64r46j2U7yODQxRmryQ9088JMTpM_kTJ1x3fwO7blPEBfucxjQSk47L9OMM85pRtxWQ1_wpy-bGYg9lmDTEjx-XLVpWr1zoYTLejVgcFpPESTgx_g4BtF1SaFCUkWRdVKxqbD9dgjVypyOszb7SYb7vkTAN4DgO9AomvMHz0pUAJ0u93YxvwyaOwxnFniauftnasm0EklT3y7jOoVJYK7NXoMmoWqymcdsEQuhBBRw6r6Y_DIK8fufOYNFB1fIK1u4JlxUO3SgHPCHJX1Z-7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cfeac3aa6.mp4?token=lr4jiKPRh0QITzI3PmvFfSOSytVGTxVNg7CV_uIus2RsUAS2AmLXaXoo8nCcitbqn64r46j2U7yODQxRmryQ9088JMTpM_kTJ1x3fwO7blPEBfucxjQSk47L9OMM85pRtxWQ1_wpy-bGYg9lmDTEjx-XLVpWr1zoYTLejVgcFpPESTgx_g4BtF1SaFCUkWRdVKxqbD9dgjVypyOszb7SYb7vkTAN4DgO9AomvMHz0pUAJ0u93YxvwyaOwxnFniauftnasm0EklT3y7jOoVJYK7NXoMmoWqymcdsEQuhBBRw6r6Y_DIK8fufOYNFB1fIK1u4JlxUO3SgHPCHJX1Z-7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت:
«بزرگ‌ترین بازنده در این ماجرا، حکومت ایرانه.
اونا سعی کردن با بستن تنگه هرمز، مسیر عبور و مرور رو تحت فشار قرار بدن؛ اما این کارشون جواب نداد.
بعد تلاش کردن با بالا بردن قیمت گازوئیل، فشار ایجاد کنن؛ اما این یکی هم دیگه جواب نمی‌ده.»
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/73116" target="_blank">📅 17:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73115">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d595a9a29.mp4?token=aQg01greQGQCT1fwPi_hAfa2N2oHJkChBhiB4Ort_VBGwqvdnMy95-cyCC0F8El9UtnFaUs4X4vrcOxxv1zm7uQFY5LK-boInxyfyAuLi4ep8i4pFUdTrpbtK8qyXO65i9Pdwc6zgc8zZcocxZMxI0pCGFZRF7ZbdKJZc7FqYglxslY6DV43cxIhf6TRRlah_sCpGa28XHb1w-KJq-vR5_YlbnJ-3q6w7nmOm-IN3c-nWQlZfWtN4_K2P9NdNjFJ8ogsvBY-rIEJ2C2nIeRAuqw8nQXU2qVBFBg8i2NchnL6F5Lw5c6XQS7nAh3YE0Ix1ujW2qOiHotkIVkc3ZNKVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d595a9a29.mp4?token=aQg01greQGQCT1fwPi_hAfa2N2oHJkChBhiB4Ort_VBGwqvdnMy95-cyCC0F8El9UtnFaUs4X4vrcOxxv1zm7uQFY5LK-boInxyfyAuLi4ep8i4pFUdTrpbtK8qyXO65i9Pdwc6zgc8zZcocxZMxI0pCGFZRF7ZbdKJZc7FqYglxslY6DV43cxIhf6TRRlah_sCpGa28XHb1w-KJq-vR5_YlbnJ-3q6w7nmOm-IN3c-nWQlZfWtN4_K2P9NdNjFJ8ogsvBY-rIEJ2C2nIeRAuqw8nQXU2qVBFBg8i2NchnL6F5Lw5c6XQS7nAh3YE0Ix1ujW2qOiHotkIVkc3ZNKVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت:
«کارگرها دیگه سر کار حاضر نمی‌شن.
ایران به بازار دلار دسترسی نداره، برای همین کاری که می‌کنه، چاپ کردن پول بیشتره.»
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/73115" target="_blank">📅 17:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73114">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cbe1e496c.mp4?token=PYA_ais5gtNGDHBOW54RrF-9w_ysZ74HCzcsgsrC3xJncpjcijobB_2oWoxsy7c9Vk9ziwTy_7EzSfv_7cZi7tz1uUk8z7kQDmx-esos8kkPMHLSA_VFXr-dtUb9zE6r4T1cjSpNyQ81-vJU2BI0ev8xepkZilqM94shWZFEbeJdQUnD1fqeA2WzscO6htvypG6achiH8FzMePtMOzUAUroAexsw74IMQhrWRmV2Lld9uX7U6xBR2GV6zRswMPNcQQ7uss95lgKqRRDopgBu2lN89OS8xdOJQRMEUxZquz0mJVKBHUa6XnPC9Oya3fxPy33tP68aWx1UvwklHLCgvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cbe1e496c.mp4?token=PYA_ais5gtNGDHBOW54RrF-9w_ysZ74HCzcsgsrC3xJncpjcijobB_2oWoxsy7c9Vk9ziwTy_7EzSfv_7cZi7tz1uUk8z7kQDmx-esos8kkPMHLSA_VFXr-dtUb9zE6r4T1cjSpNyQ81-vJU2BI0ev8xepkZilqM94shWZFEbeJdQUnD1fqeA2WzscO6htvypG6achiH8FzMePtMOzUAUroAexsw74IMQhrWRmV2Lld9uX7U6xBR2GV6zRswMPNcQQ7uss95lgKqRRDopgBu2lN89OS8xdOJQRMEUxZquz0mJVKBHUa6XnPC9Oya3fxPy33tP68aWx1UvwklHLCgvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت:
«ایران دیگه هیچ محموله نفتی‌ای در مسیر انتقال نداره. جریان نقدی‌شون منفی شده و ما راهشون رو بستیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/73114" target="_blank">📅 17:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73113">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aafe668bc.mp4?token=LFsm0i1vddM2-YFv8Qxj1qW6Kxb0zZakpxgpeeBxpQdemqoSpSp0pQurqQHxh3fLvc2TlPk5GINPAlnuQFz_sbB2vqNcq-bNYLmcQf5q8vRuDnxL0Tl8iYYVlWsP5yTFAH8oJrcU_bVvcN__E-p3py3BUViuPX15Len8FFbc53sQAvoE3NRGEvMCkaXw964MeCaI5eyncWy4WIb7AcMJqqJR-W7boZVtQJcqcjCCIEWdM9q76pwkQ6Xt7nJRayOOwUVE4-ScD8bF3_F-mB2lxKmeWlw_Hjpon1rKqAPmlmaOcKNxi6Igk0chLAUSBJEMk90Nnf7mFIWsCoYX8f6xUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aafe668bc.mp4?token=LFsm0i1vddM2-YFv8Qxj1qW6Kxb0zZakpxgpeeBxpQdemqoSpSp0pQurqQHxh3fLvc2TlPk5GINPAlnuQFz_sbB2vqNcq-bNYLmcQf5q8vRuDnxL0Tl8iYYVlWsP5yTFAH8oJrcU_bVvcN__E-p3py3BUViuPX15Len8FFbc53sQAvoE3NRGEvMCkaXw964MeCaI5eyncWy4WIb7AcMJqqJR-W7boZVtQJcqcjCCIEWdM9q76pwkQ6Xt7nJRayOOwUVE4-ScD8bF3_F-mB2lxKmeWlw_Hjpon1rKqAPmlmaOcKNxi6Igk0chLAUSBJEMk90Nnf7mFIWsCoYX8f6xUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛
اسکات بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
«همون‌طور که رئیس‌جمهور گفته، انتظار نداره درگیری نظامی تا قبل از انتخابات میان‌دوره‌ای اتفاق بیفته؛ دست‌کم نه تا بعد از اون.
نمی‌دونم معادل عبارت «تسلیم شدن و درخواست توقف» به فارسی چیه، اما ایرانی‌ها بالاخره به جایی می‌رسن که از آمریکا درخواست کنن دست از فشار برداره و تسلیم می‌شن.»
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/73113" target="_blank">📅 17:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73112">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1394e2d860.mp4?token=BtjzbG6vqbOgpoOj5xEeWXJLKqZOKsvm28uLHSvO0Pl_lK_KmXj5lKz3xTi1oGh8Rbl11NYpbV8KBrY8YKIYLKLZ_1aQJB0Xt2jYARTpF5wm_WgdfrbkhJZ5Vcp_6CLkEMci-VG5Ansl4xSkLCq6JvhM5yr1HfJfUXoASod_C8yPcKaVntkoNOwsDCjlRN3g00wtttPckosZOQQO0zDdJhodbaJWBCyvgxc8L7mPNXsaKnjtD3Sp-p6Hy_mq8nLeZ4xZGB1o4WJjTrl5LuiHAe4ArLsOMOjy0fRJ-TQX4xf_4CSd8UQPGDv7yJGT80YEV59ggzXMoVw6v3DY3zz51Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1394e2d860.mp4?token=BtjzbG6vqbOgpoOj5xEeWXJLKqZOKsvm28uLHSvO0Pl_lK_KmXj5lKz3xTi1oGh8Rbl11NYpbV8KBrY8YKIYLKLZ_1aQJB0Xt2jYARTpF5wm_WgdfrbkhJZ5Vcp_6CLkEMci-VG5Ansl4xSkLCq6JvhM5yr1HfJfUXoASod_C8yPcKaVntkoNOwsDCjlRN3g00wtttPckosZOQQO0zDdJhodbaJWBCyvgxc8L7mPNXsaKnjtD3Sp-p6Hy_mq8nLeZ4xZGB1o4WJjTrl5LuiHAe4ArLsOMOjy0fRJ-TQX4xf_4CSd8UQPGDv7yJGT80YEV59ggzXMoVw6v3DY3zz51Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی یک کشتی در مسیر جنوبی تنگهٔ هرمز بر اثر اصابت یک پرتابه:
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/73112" target="_blank">📅 16:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73111">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">صدای دو انفجار از طرف تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/73111" target="_blank">📅 16:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73110">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de2a7fa633.mp4?token=P4jTGY5SDRsiq4ZZ85OY-HDocgGnl2xn6IxcnBgQhLCTF4soLaZSlhtYFQRXGJw3hs5xf9MIzkMppFCmxnu0axaQIt3JJ4wPpcDKWseBamV8JqXw_VxSFWGaPYBNyRfWGdoXhRkefA_ELUK5fWDVAu7ZQXzvqIXjDW3EqiKOIN8S8IZFECCmT2zqMzEx5TzN9jzAQNJXK18CwRFeqt26r4JZWijTSu8_Ls8MeBJETGFQD-fS4xDETwYoTwWsC51Xcio-aJFKDJwCyw_06G7TEx6RstsAGiEDsSyyKpDv3oUXK2KZxqBMBsTB-UaaBAqZ6bkg4innyzvdVGR-ECxB6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de2a7fa633.mp4?token=P4jTGY5SDRsiq4ZZ85OY-HDocgGnl2xn6IxcnBgQhLCTF4soLaZSlhtYFQRXGJw3hs5xf9MIzkMppFCmxnu0axaQIt3JJ4wPpcDKWseBamV8JqXw_VxSFWGaPYBNyRfWGdoXhRkefA_ELUK5fWDVAu7ZQXzvqIXjDW3EqiKOIN8S8IZFECCmT2zqMzEx5TzN9jzAQNJXK18CwRFeqt26r4JZWijTSu8_Ls8MeBJETGFQD-fS4xDETwYoTwWsC51Xcio-aJFKDJwCyw_06G7TEx6RstsAGiEDsSyyKpDv3oUXK2KZxqBMBsTB-UaaBAqZ6bkg4innyzvdVGR-ECxB6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس سازمان مدیریت بحران کشور: احتمالاً در ۴ ماه پایانی سال کسری انرژی خواهیم داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/73110" target="_blank">📅 16:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73109">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4f3b1e9af.mp4?token=bEWblb9hdbsrJocGiSLkIDGUDf4Brps2c-_XDlqOKQ5SZHDGCUN2MMMgaPmrgoBX9sIKyBO_SJJYHPjXZlyh-YceT1O94i4bHht5zYVMDFkECNeVaK7MCkorsbB7ir9T5mOadrQmCihzlwDd8W8_Q5oPXZiA83_vs-5c3oUUu1Fx6sd-mOfZDWdaMVS3aVyIKwCZOawe9EJqNWqxPWdCQGO5T2YvzC6Y93WTHovThU5WWANh4WaOGzqFzV6BVikZgwGbaeg1IcrS6p2HkzxxZ7bPBuRZcwDlB_btVy1UIBToaiSMdjOY0RtOxeO2aa7wEYVxxCTgLExCGnLb8BH1ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4f3b1e9af.mp4?token=bEWblb9hdbsrJocGiSLkIDGUDf4Brps2c-_XDlqOKQ5SZHDGCUN2MMMgaPmrgoBX9sIKyBO_SJJYHPjXZlyh-YceT1O94i4bHht5zYVMDFkECNeVaK7MCkorsbB7ir9T5mOadrQmCihzlwDd8W8_Q5oPXZiA83_vs-5c3oUUu1Fx6sd-mOfZDWdaMVS3aVyIKwCZOawe9EJqNWqxPWdCQGO5T2YvzC6Y93WTHovThU5WWANh4WaOGzqFzV6BVikZgwGbaeg1IcrS6p2HkzxxZ7bPBuRZcwDlB_btVy1UIBToaiSMdjOY0RtOxeO2aa7wEYVxxCTgLExCGnLb8BH1ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یا بچه مچه با خودتون نبرید طلافروشی، یا اگه میبرید با طناب ببندینش به خودتون که همچین منظره‌ای خلق نکنه :
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/73109" target="_blank">📅 15:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73106">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18ce038cc.mp4?token=NA37AlFpnwBgdY0fr-S8wq7-qOWDSqpx5QvAmLIqiXW3R33bCXPfb1QNcHN_kG05iNPlobCSI8Sm_1SOC97c2riiHj4wNW-X_NJfuNCey7d5rwKig94kzDaQyLxT9y0pIRIe-1lM6Q0u3fH0_IrRgyt4hFbeFgUirlCCiv5cGgzlnRGTc88-Hqa7jo0hWXqIEnYPUoXS1lP5jv90y_enfx1TBCWvjPHV_9OL5ybPHbntgAUS86p46YXXM3erVW5s3yDQgwUBGD-cwQ90aca4dmHURs7iaD_BIPcGFwjJbnMt0_hWZ5obe3HcO-24CqTouMmh81a01Ax-Bs_yWjjSKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18ce038cc.mp4?token=NA37AlFpnwBgdY0fr-S8wq7-qOWDSqpx5QvAmLIqiXW3R33bCXPfb1QNcHN_kG05iNPlobCSI8Sm_1SOC97c2riiHj4wNW-X_NJfuNCey7d5rwKig94kzDaQyLxT9y0pIRIe-1lM6Q0u3fH0_IrRgyt4hFbeFgUirlCCiv5cGgzlnRGTc88-Hqa7jo0hWXqIEnYPUoXS1lP5jv90y_enfx1TBCWvjPHV_9OL5ybPHbntgAUS86p46YXXM3erVW5s3yDQgwUBGD-cwQ90aca4dmHURs7iaD_BIPcGFwjJbnMt0_hWZ5obe3HcO-24CqTouMmh81a01Ax-Bs_yWjjSKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت گرگان بعد از سیلاب ساعاتی پیش.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/73106" target="_blank">📅 15:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73105">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/35cfb05bea.mp4?token=OV8j1LNObGj5Lv-XWra6oqSfhwiQzMW1XHf6S4a0axjzVK7Xkrrd3mOt0a2F6USLyafCqAGhuMZv0QNxOH-fRKK9C48pEomE2yVDORR6uO4kxoTmgNM33rLLul70Rks0SMoCo1lOXPbO-bJooCTvuShPd3U0INs7oMjQOljZmM5sze72fyxC0x0OOEqz5dmtbgaBya4wjmq9kgz9-E_HAypldoXFyT0tyaEy2Zcj6GKQRg5TaLm6I6TDP9lsyvmGKUxVgUWy-3ZN_r4WMjeVU30VIwjVhuZgIBBlCP5vW9F9bTfdAo5gwaKz-sdN-MpHc1n11SH4Vmdfu3wP7paSDg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/35cfb05bea.mp4?token=OV8j1LNObGj5Lv-XWra6oqSfhwiQzMW1XHf6S4a0axjzVK7Xkrrd3mOt0a2F6USLyafCqAGhuMZv0QNxOH-fRKK9C48pEomE2yVDORR6uO4kxoTmgNM33rLLul70Rks0SMoCo1lOXPbO-bJooCTvuShPd3U0INs7oMjQOljZmM5sze72fyxC0x0OOEqz5dmtbgaBya4wjmq9kgz9-E_HAypldoXFyT0tyaEy2Zcj6GKQRg5TaLm6I6TDP9lsyvmGKUxVgUWy-3ZN_r4WMjeVU30VIwjVhuZgIBBlCP5vW9F9bTfdAo5gwaKz-sdN-MpHc1n11SH4Vmdfu3wP7paSDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف:
من به مسئولین گفتم، با برجامی که کونتون رو پاک میکنین، فردا باید دماغ‌تون پاک کنین!
ما کشورهای منطقه رو تهدید می‌بینیم، برای همین سفرای ما در منطقه جا بازرگان و دیپلمات، نماینده سپاه قدس هستن.
ما همه چیزو تهدید می بینیم، زن رو تهدید دیدیم، اینترنت رو تهدید دیدیم، کشورای منطقه رو تهدید دیدیم، ما حتی حجاب هم خاکریز می‌بینیم!
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/73105" target="_blank">📅 14:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73104">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ac45cb0ca.mp4?token=bC2D_xWNqdViYPodxB9eeW5obGQhAmd4T95dRtOXW68gIiAYYrrO0ZMHLgN7RqMgxmwy5kHvZtIo_OfERWH66toELEsm_diisCj19Zy2KDZLvR_SovqUsDE-0SQ8xODhNmE3wBlE16jATED-zQeDUZ6iVB3GfEb7ehRNjMSQ2e4Nlh1E9O5vkljDvQhNfZYvAH5l8ScI80rq1wVJqHEy3ExOWif-_UeljbZ5y_cAwVdjwoY2OH_yzgUYiMgMzNA1Y-zqG3pTm7P5pN0KCg6BxRcToKylpbpJ0wEAQPL2lLZ2MKrhsn0ZWrjzZCrSjk4M20QTuGMPqa-8xnPr97ylqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ac45cb0ca.mp4?token=bC2D_xWNqdViYPodxB9eeW5obGQhAmd4T95dRtOXW68gIiAYYrrO0ZMHLgN7RqMgxmwy5kHvZtIo_OfERWH66toELEsm_diisCj19Zy2KDZLvR_SovqUsDE-0SQ8xODhNmE3wBlE16jATED-zQeDUZ6iVB3GfEb7ehRNjMSQ2e4Nlh1E9O5vkljDvQhNfZYvAH5l8ScI80rq1wVJqHEy3ExOWif-_UeljbZ5y_cAwVdjwoY2OH_yzgUYiMgMzNA1Y-zqG3pTm7P5pN0KCg6BxRcToKylpbpJ0wEAQPL2lLZ2MKrhsn0ZWrjzZCrSjk4M20QTuGMPqa-8xnPr97ylqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری منتشر شده است که لحظه حمله حوثی‌ها به فرودگاه بین‌المللی ملک خالد در ریاض را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/73104" target="_blank">📅 13:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73103">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZw75WAcmSClKeP4qE6atOx-p445hWeN8r4x5ElOvEWXprbpRUldKIufCObpJh-s1g8ie-F-htQ_sqybVnNm5S16InXjlzJwn0riv251zKmw6FiMjSS9SerMr4hDfBrL8DWhlROjp6_cOohDv7Nfz_JejPEgl2xkPUD24U3jbBEHznsSa-YEMBtveXUbsEjEfd-juQg3Hj4Ym4nsRoUC1wlxj8OfmyIFaJMhKd6ZPTCm5mpNfh2RsEmiHwmrF2Vui5QK4J2gRCVSLXECl3sOyJHQf9UlyHFG16Po7xVi6XqEHC4oqErVZhFNzSQtkjfBOgSnXTF4Pf0DjKuMpFMs1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز جهانی دختر، بر دختران سربلند و آزاده‌ی ایران‌زمین فرخنده باد.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/73103" target="_blank">📅 12:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73102">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uiEkVWCyoJosWNVR_Hc3kqACpKt4yRpxTZ4Q1k5qLD3qguTNP-ySPumIzvwJHVh-1rh-5pyDYVA74pmlJZoowzatVVOSrCNocc0gRvHXRk2za7Z5IXbs0pgeFA3LtT96kOJaKpZb4NJKQRegd77bJXxRWUdrgX_C-QzoNlEJD_A2Efjn33Vh_ZHrsMzr-04B_we7E3lp8Stm1drCHo4xG7JQ_9JJZjjIhV7ByKg4ywBIMDGqyIJLUGJbRcmHXMQ4OCx-lYxzGQclQkOK6JrY3Dcsf3qe9cZQUnVvgIBpkbAKpURuyKuSxEMBHACv5XqMDvz59kPxqXABCMuLlT5ayA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تست موشکی از جنوب تهران
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/73102" target="_blank">📅 12:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73101">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47fbc83428.mp4?token=s2HJYle5Gj1rMuuckE4cCzf12Lz5vXhiTvYailyUMvKDaBLDFT-g0M43pEnlJ0QMgFDbiwx8MloMthyxJC6CF56SzTvU3VJ9e07QC4qRVJp62bQ5tDLzdVz2eSH0cVOE-NDIeknXaQ1cme4uURUoHXexIHALXcSGj1uMcMipy90-7jJGRUaZ429bCfAtu7ItpkT7nJM7_1xSJzjqO4L5EIWEMnMwXsMqhydpLPO2YSeMcSdc2GiNAoHw1h3jJ7H-aM2ZWqVinHvHrbwfRhE9OK0olU_1zha8K3a1EnQo7Sk9zraciPx-C53nzPby1EPPIwBv2YwRw_JaRmX4qT-4Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47fbc83428.mp4?token=s2HJYle5Gj1rMuuckE4cCzf12Lz5vXhiTvYailyUMvKDaBLDFT-g0M43pEnlJ0QMgFDbiwx8MloMthyxJC6CF56SzTvU3VJ9e07QC4qRVJp62bQ5tDLzdVz2eSH0cVOE-NDIeknXaQ1cme4uURUoHXexIHALXcSGj1uMcMipy90-7jJGRUaZ429bCfAtu7ItpkT7nJM7_1xSJzjqO4L5EIWEMnMwXsMqhydpLPO2YSeMcSdc2GiNAoHw1h3jJ7H-aM2ZWqVinHvHrbwfRhE9OK0olU_1zha8K3a1EnQo7Sk9zraciPx-C53nzPby1EPPIwBv2YwRw_JaRmX4qT-4Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: یک کشتی باری در دریای عمان هدف حمله آمریکا قرار گرفت
فرماندهی مرکزی آمریکا (سنتکام) اعلام کرد در ۱۰ اکتبر، یک کشتی باری با پرچم پاناما به نام Ocean Molica که پیش‌تر از یکی از بنادر ایران حرکت کرده بود، پس از بی‌توجهی به هشدارهای مکرر و تلاش برای عبور از محاصره دریایی، هدف مهمات دقیق یک جنگنده آمریکایی قرار گرفت.
به گفته سنتکام، این حمله پیشرانه کشتی را از کار انداخت و خدمه آسیبی ندیدند. همچنین، طی سه ماه اجرای محاصره دریایی، ۴ کشتی از کار انداخته و ۱۳۵ کشتی دیگر وادار به تغییر مسیر شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/73101" target="_blank">📅 12:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73099">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6da19cc3d2.mp4?token=Ycqf_8e-sDDsL9ZcS4FaCd-wpATp447wf9coVhIqBESgT8iwPCijo7au2RDs8wLrFZQRC5ooF0L-EwPnjARORmCR9xLuJO8DCS1h7G0EGjIrW6pB7iUzY4Y7q2D4i_J2BDTWxZbNEsXmlPPl1LV19JoI3aCeNrawsuCRttuMWEjlG4F7pX682nA5ZogzaPV3ZmA-IQFW4uaBsjzVZkc7rMM4qFp_9QjGNeWjfx5ehrKRdwplqWgvdtsjUkcluwB0ydzxkWTovrU5aOpUVPmNQgFc1vgnqsE9cIBTItp9M3iMLFO8HKDvIEMX0saOYnrzkuljnLyQyh-JgmlM8Uc77Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6da19cc3d2.mp4?token=Ycqf_8e-sDDsL9ZcS4FaCd-wpATp447wf9coVhIqBESgT8iwPCijo7au2RDs8wLrFZQRC5ooF0L-EwPnjARORmCR9xLuJO8DCS1h7G0EGjIrW6pB7iUzY4Y7q2D4i_J2BDTWxZbNEsXmlPPl1LV19JoI3aCeNrawsuCRttuMWEjlG4F7pX682nA5ZogzaPV3ZmA-IQFW4uaBsjzVZkc7rMM4qFp_9QjGNeWjfx5ehrKRdwplqWgvdtsjUkcluwB0ydzxkWTovrU5aOpUVPmNQgFc1vgnqsE9cIBTItp9M3iMLFO8HKDvIEMX0saOYnrzkuljnLyQyh-JgmlM8Uc77Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدی رفتن ویدیوی رپ هوش‌مصنوعیِ بی‌بی رو نشون خودش دادن، اونم به شوخی میگه از کجا میدونید شاید واقعی باشه:)
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/73099" target="_blank">📅 11:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73098">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">مقام‌های سعودی اعلام کردند در حمله روز شنبه به فرودگاه ملک خالد ریاض، ۱۲ نفر کشته و ۳۰۹ نفر زخمی شدند.
ملیت کشته‌شدگان:
عربستان سعودی: ۴ نفر
بنگلادش: ۲ نفر
آمریکا: ۱ نفر
مصر: ۱ نفر
اردن: ۱ نفر
سوریه: ۱ نفر
فلسطین: ۱ نفر
سودان: ۱ نفر
برخی مجروحان در وضعیت وخیم قرار دارند و حمله خساراتی به تأسیسات فرودگاه وارد کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/73098" target="_blank">📅 11:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73097">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f2ae9fdb8.mp4?token=bgSQXKir0xGI2uv6f8C5eD7vaSgl5EvlMls6jByzyuyV9S7noy1u2UnqMI9cHaVljRXvLbfjze9966bmHzAh8z25yjPS2rtaMyIHOUwA45Na4Lo1NgMZFZiqww7XRASNEw7pPX5AVt-S1zBev7MEcBQQmVL3l1jvrkn3fBvO9C4vWVLoKvS1uwmXdOEiRuQAY2lklQIzIgj3dEqxYtzLO7ZxLVJA0EVzx6LYfiDlRVjIBtxvc9YMN5oYFZx8v61B6yjUW-3iqxBYyTR3hN6VcJGRj0-_BX8db6FvFPaMlFB0OcYwY_LU8XygWI5Otv6P2-_IWbg8mkleFx5f-ouJdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f2ae9fdb8.mp4?token=bgSQXKir0xGI2uv6f8C5eD7vaSgl5EvlMls6jByzyuyV9S7noy1u2UnqMI9cHaVljRXvLbfjze9966bmHzAh8z25yjPS2rtaMyIHOUwA45Na4Lo1NgMZFZiqww7XRASNEw7pPX5AVt-S1zBev7MEcBQQmVL3l1jvrkn3fBvO9C4vWVLoKvS1uwmXdOEiRuQAY2lklQIzIgj3dEqxYtzLO7ZxLVJA0EVzx6LYfiDlRVjIBtxvc9YMN5oYFZx8v61B6yjUW-3iqxBYyTR3hN6VcJGRj0-_BX8db6FvFPaMlFB0OcYwY_LU8XygWI5Otv6P2-_IWbg8mkleFx5f-ouJdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: نظرتون درباره حمله حوثی‌ها به فرودگاه ریاض چیه؟
ترامپ: «به نظرم اتفاق وحشتناکیه.»
خبرنگار: آیا آمریکا هم وارد ماجرا می‌شه؟
ترامپ: «خب، خودتون متوجه خواهید شد. اما به نظرم اتفاق وحشتناکیه.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/73097" target="_blank">📅 10:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73096">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ درباره یمن:
«ما با حوثی‌ها در ارتباط هستیم و باید ببینیم چه اتفاقی می‌افته.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/73096" target="_blank">📅 10:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73095">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/174ee9d3ac.mp4?token=YvKqpEh0nAj0BoxudEwjFRk7zhX-NdqQxgCJrmFmFOfAVFE4XM0KJHeVK5zJ_g9gjHKHcHU5U9Dl1umvyYpCzjnGAifXhiTvSboTt5M7ViqV2aNpM2sjbgHtayQk-zFqlHang57PVyqHyLMtTUJJl27_2vm_lyeaBSXAWVhj9ydLy1edxWrmSTzXF7pMO4-3AxdsCBEBaPIG950Id_rGRwC5nzlWzTixWhTaRfP8E3PJKPWS_yHWIPz2Et3UCXcB3z8vnARhy855GSGW2wh71q_Vy8W4KEVLLuVnbfOshVsmZeGLJ4LOnkJlRD0JOw2SOSzslMlW6c1-YSdBHg4bZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/174ee9d3ac.mp4?token=YvKqpEh0nAj0BoxudEwjFRk7zhX-NdqQxgCJrmFmFOfAVFE4XM0KJHeVK5zJ_g9gjHKHcHU5U9Dl1umvyYpCzjnGAifXhiTvSboTt5M7ViqV2aNpM2sjbgHtayQk-zFqlHang57PVyqHyLMtTUJJl27_2vm_lyeaBSXAWVhj9ydLy1edxWrmSTzXF7pMO4-3AxdsCBEBaPIG950Id_rGRwC5nzlWzTixWhTaRfP8E3PJKPWS_yHWIPz2Et3UCXcB3z8vnARhy855GSGW2wh71q_Vy8W4KEVLLuVnbfOshVsmZeGLJ4LOnkJlRD0JOw2SOSzslMlW6c1-YSdBHg4bZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا سعودی‌ها بدون حضور نیروهای آمریکایی هم می‌تونن از خودشون دفاع کنن؟
ترامپ: «بله، توانایی دفاع از خودشون رو دارن. سعودی‌ها جنگجوهای خوبی هستن، اما به نظرم اون حمله اتفاق وحشتناکی بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/73095" target="_blank">📅 10:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73094">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73094" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/73094" target="_blank">📅 10:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73093">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElvFrXraSVC9BUdDias5ZQVsdAoipYsj3t06i0789cLBKB1fkj94SXnQLcp1HIDNyB35qgBAPKZJbKI4cxJXLMhKC_KrLd4uw2KvbvxwJXTk7e9XEecxBKI3B7lbeDIU7ZgpA4RS1Jki7wX58YDuB8TroacnkEOtBPU4vT93Ay_SDiilro-HAGP9D8PY6vPWwigcEKC7Xe29TI8AS8WCxtrtCpRHelDmxhQHM21UwF0h5H3soKcDTXY9plgNGzsIuiBDN8IlnhX1cAuAgRrcc02Xl7LC-MCwp9Hp49ufPjwuFeP0j-kJtivgqRaN4upT3mlMP788e2AjZtqpPa2A6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
ناتینگهام‌فارست
🆚
کریستال‌پالاس
اورتون
🆚
هال
منچسترسیتی
🆚
لیورپول
اوساسونا
🆚
راسینگ سانتاندر
رم
🆚
کومو
مونزا
🆚
لاتزیو
میلان
🆚
ساسولو
فروزینونه
🆚
ناپولی
یوونتوس
🆚
کالیاری
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/73093" target="_blank">📅 10:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73092">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71e6800693.mp4?token=WaaMzHZZrGgF6fq6vVE9OzuMqiJ_rgunfvz2_VP5WxQkI0deQgiFzQ4_HmG3b4Sa4CPYh7UQ77mdtdBzzLrQGvOiSx557UhBMfb76Nb7vcP-ZPUEdCDdgE78T34vNYswxrOc1dO3CjaFH83EHGcwfF7Be3B8QDtwjUyVd6AudEiziiUdt5ZyZ7Td4lFx7WV5x5dxz23pPeGJUH2-4Z9cHkTZO2d_U2HYJUe1dERM_ToGfiXyJqqlE54mGVosHDbQrxEV2v2YqKAxPwhb3BS5IgrXYF9US9rE1YGP-tQB_guC20LczUjdH0-aP7Nd-V12Ei77cZwc_FqFRJDUYptuOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71e6800693.mp4?token=WaaMzHZZrGgF6fq6vVE9OzuMqiJ_rgunfvz2_VP5WxQkI0deQgiFzQ4_HmG3b4Sa4CPYh7UQ77mdtdBzzLrQGvOiSx557UhBMfb76Nb7vcP-ZPUEdCDdgE78T34vNYswxrOc1dO3CjaFH83EHGcwfF7Be3B8QDtwjUyVd6AudEiziiUdt5ZyZ7Td4lFx7WV5x5dxz23pPeGJUH2-4Z9cHkTZO2d_U2HYJUe1dERM_ToGfiXyJqqlE54mGVosHDbQrxEV2v2YqKAxPwhb3BS5IgrXYF9US9rE1YGP-tQB_guC20LczUjdH0-aP7Nd-V12Ei77cZwc_FqFRJDUYptuOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امام جمعه تهران:
توقع مردم، تجدید نظر در دکترین هسته‌ای ایران است
از ان پی تی خارج شویم به غرب می‌گویم هسته‌ای ما به شما ربطی ندارد؛
غلط کردین؛ برید گم شید!
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/73092" target="_blank">📅 10:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73091">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce6a5528a8.mp4?token=sz4bj4oo5gr52AEpYIVp3aJpXwidV77p94mqx6uDMpHlGIbbLDyPhDlZPAbPI4oHM7Q-f6ZWxGZ3dAv10iCD26UPQDef33SnGEeRYzw8Cl8nuvuYH9a_TPrCjobocWoEMBgHqkALN6ljHTB8Cv0yGO8oXUJ3wxSIBwueO8gU0rxsxGP3Ta8jrpx3MYwsAQ5RQagLQv-htyIpCrsFfqJvoiyMo5iAhfiZxf1c0BVAG4bZP89IQI5f1B3XupcSNija-qe64AkuzxgmnP8DGlP00jFO-e5e9l9lWJee5h8kLvoIs04HDxTGmlN6tBCoSfS2KXYjSYLhrxtiSErlMJ4KUALcs5M-QuW6j20ydee3D3xduecmGCP04QjOGUllsCCCnaL0v4wlxX7Coa7U7APfArl6Fsk6UJpRIY1hGwNB_dJ-SZfD1hGNOIohuYXPezOkYH6kp_g-hGghGT16YUgOgoyU1OkRUmEDnHoCk-3kVbZvASVK9ZN2GS7NM-kW9CyE7yNU5GmbICk_8WvFoDI-VWB9UUrcOQHJUuBGuiW17DatQiiaf51GCIInkSP57NkWcypdu-hCGwm8-sco1JErQ9vzVS_k5q7iuMuhExAyVVle-phRXOpPs0gnxsZc4kNLFND3i5dJHx4yFH8Cv_WIh4i6jIdKyGvo6DtdmbwEz8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce6a5528a8.mp4?token=sz4bj4oo5gr52AEpYIVp3aJpXwidV77p94mqx6uDMpHlGIbbLDyPhDlZPAbPI4oHM7Q-f6ZWxGZ3dAv10iCD26UPQDef33SnGEeRYzw8Cl8nuvuYH9a_TPrCjobocWoEMBgHqkALN6ljHTB8Cv0yGO8oXUJ3wxSIBwueO8gU0rxsxGP3Ta8jrpx3MYwsAQ5RQagLQv-htyIpCrsFfqJvoiyMo5iAhfiZxf1c0BVAG4bZP89IQI5f1B3XupcSNija-qe64AkuzxgmnP8DGlP00jFO-e5e9l9lWJee5h8kLvoIs04HDxTGmlN6tBCoSfS2KXYjSYLhrxtiSErlMJ4KUALcs5M-QuW6j20ydee3D3xduecmGCP04QjOGUllsCCCnaL0v4wlxX7Coa7U7APfArl6Fsk6UJpRIY1hGwNB_dJ-SZfD1hGNOIohuYXPezOkYH6kp_g-hGghGT16YUgOgoyU1OkRUmEDnHoCk-3kVbZvASVK9ZN2GS7NM-kW9CyE7yNU5GmbICk_8WvFoDI-VWB9UUrcOQHJUuBGuiW17DatQiiaf51GCIInkSP57NkWcypdu-hCGwm8-sco1JErQ9vzVS_k5q7iuMuhExAyVVle-phRXOpPs0gnxsZc4kNLFND3i5dJHx4yFH8Cv_WIh4i6jIdKyGvo6DtdmbwEz8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبکه بریتانیایی ITN حدود ۴ ساعت از تصاویر وقایع سال ۱۹۸۹ میدان تیان‌آن‌من را منتشر کرده است؛ تصاویری که پیش‌تر محرمانه نگه داشته شده بودند و توسط تیمی ضبط شدند که موفق شد این نوارها را مخفیانه از چین خارج کند.
این مجموعه که حدود ۳۵ سال در آرشیو نگهداری می‌شد، شامل یک ویدئوی تدوین‌شده‌ی ۲ ساعته از سرکوب‌ها و همچنین ۹۰ دقیقه تصاویر خام و مخفیانه‌ای است که در روزهای پس از آن واقعه ضبط شده‌اند؛
تصاویری که کامیون‌های نظامی در خیابان‌های پکن، جمعیت مردم و پیامدهای آن رویداد را به نمایش می‌گذارند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/73091" target="_blank">📅 09:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73090">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e31f09431.mp4?token=COhoUUe-bgl-kclzUQGJ2r0M4J9Z8aA6cK2XTCFPPYkNn8mCuvKqXbjhc4b56IG5Y7B9qp9O0AuvNQwKxCMSp_IDYrq9wfMi7dG-Q7mVaWwiLRmrl_7Z2GOzIQIjlclgf9axFSXB1oFweWXtGZpsbhMqfc5e5oDVzgTZKVMLB3Kj7wQPf6Yjjd4kVppsMhc8Wjs1WN2Wy91sviSrFn8hR41w-SMbBBh1Bl2_oOQcqsIwBPC2x0o70Ww2bQX5KFyZTWMg4ncPCTCP3hu8_h9S97YMsklP9QJmwZsjczrCBlUQlBScHirLrsVIUx1Qjhsxiyzsj3EejCsHipMX5G4y3TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e31f09431.mp4?token=COhoUUe-bgl-kclzUQGJ2r0M4J9Z8aA6cK2XTCFPPYkNn8mCuvKqXbjhc4b56IG5Y7B9qp9O0AuvNQwKxCMSp_IDYrq9wfMi7dG-Q7mVaWwiLRmrl_7Z2GOzIQIjlclgf9axFSXB1oFweWXtGZpsbhMqfc5e5oDVzgTZKVMLB3Kj7wQPf6Yjjd4kVppsMhc8Wjs1WN2Wy91sviSrFn8hR41w-SMbBBh1Bl2_oOQcqsIwBPC2x0o70Ww2bQX5KFyZTWMg4ncPCTCP3hu8_h9S97YMsklP9QJmwZsjczrCBlUQlBScHirLrsVIUx1Qjhsxiyzsj3EejCsHipMX5G4y3TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میرسلیم:
فلسفه بازنشستگی در یک کشور اسلامی هیچ مفهومی ندارد و مسلمان واقعی باید تا آنجا که می‌تواند خدمت کند
حیف است که افراد ۸۰ و ۹۰ ساله را از خدمت کنار بگذاریم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/73090" target="_blank">📅 09:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73089">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/73089" target="_blank">📅 01:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73088">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/73088" target="_blank">📅 01:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73087">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1848b3d2ec.mp4?token=BeG-4ECSnnNj21qQKytgXqHf1XXlwx_O8ipiU5umYJM_xQrKv1ntHvEtxEFhiYGP9Tpuu6CbCobI7iwCcyzebqmRwj4x2nm_EimCtEdehIDLfInpOsL5ixIYpzrb6-71pe_LRaqvN2X8HCMhgjLwESBsgAsLqlD1mQsQHE2kYy9kbraTz3_NoA8sup2rer6Jh9vA3lOj65sMeOhQPJXSwt77vW4iNhvROwli46LsIEx7UElxeIr68LmIF_5e2N1P8KN6mbrhHoC4i7C7z9zY6-i7aHFwIgST2oNRER6lDeed2Fh3gLxKUi1SP3Jd-_ynaFHeqGpNrgV4MAy4qZfUTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1848b3d2ec.mp4?token=BeG-4ECSnnNj21qQKytgXqHf1XXlwx_O8ipiU5umYJM_xQrKv1ntHvEtxEFhiYGP9Tpuu6CbCobI7iwCcyzebqmRwj4x2nm_EimCtEdehIDLfInpOsL5ixIYpzrb6-71pe_LRaqvN2X8HCMhgjLwESBsgAsLqlD1mQsQHE2kYy9kbraTz3_NoA8sup2rer6Jh9vA3lOj65sMeOhQPJXSwt77vW4iNhvROwli46LsIEx7UElxeIr68LmIF_5e2N1P8KN6mbrhHoC4i7C7z9zY6-i7aHFwIgST2oNRER6lDeed2Fh3gLxKUi1SP3Jd-_ynaFHeqGpNrgV4MAy4qZfUTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«ایران کشور بسیار شروریه؛ بزرگ‌ترین حامی تروریسم در جهانه.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/73087" target="_blank">📅 01:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73086">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6a4893ab6.mp4?token=hEEv6mQUOLGoG6sQvPWU2q-HiAvnKXUSXb48XaFRWXx_Aw5_YDUt0SUYLiBmZhjEkMD_-TuPkz996kAdYT9Npl6ON577Z4uCxMolCpP6wjG5sbXSWkwC_mQgbFRA1PEMy_ZJy6dFVciMY89RlM1xH4-Pq3T4kxKp0bTAydL4QTVzefB2zrGKseakbx6gJ9ZPWLiPUM-JnsoqM1rm0bXBny72pQFhFY_lN1gFMOVeOUzgEo1ikUYcbAm-tHY-Mb5HNvZ2RleVHjp_5vpy18mNYeEagDgue95PEPqSHqQF4NLsazZzEvMD6c6JkmjbRmu-DRWCfvYTqR8Qd1KjGTtOUoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6a4893ab6.mp4?token=hEEv6mQUOLGoG6sQvPWU2q-HiAvnKXUSXb48XaFRWXx_Aw5_YDUt0SUYLiBmZhjEkMD_-TuPkz996kAdYT9Npl6ON577Z4uCxMolCpP6wjG5sbXSWkwC_mQgbFRA1PEMy_ZJy6dFVciMY89RlM1xH4-Pq3T4kxKp0bTAydL4QTVzefB2zrGKseakbx6gJ9ZPWLiPUM-JnsoqM1rm0bXBny72pQFhFY_lN1gFMOVeOUzgEo1ikUYcbAm-tHY-Mb5HNvZ2RleVHjp_5vpy18mNYeEagDgue95PEPqSHqQF4NLsazZzEvMD6c6JkmjbRmu-DRWCfvYTqR8Qd1KjGTtOUoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«اون جوان‌هایی که در جنگ علیه ایران از دست دادیم، بیهوده جونشون رو از دست ندادن.
نمی‌شه اجازه داد یه آدم کاملاً دیوونه به سلاح هسته‌ای دست پیدا کنه.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/73086" target="_blank">📅 01:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73084">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/595730e6c3.mp4?token=N7svXmUTaglfOKomh0R0qP6Zzgj2JjwHXx21POJFyF3KHyfdryJ0w1KXw03eN1j7sug43PigDivSZCsh9oUyXCYOLLfU8iu6VbR7jIKz7OescKTZiWYEuY9ezTz5mKbN6pVTtFUnqUDXj7SF6yHx4u5U2oWUxaWxpJ1HnYNMpHbIaQzAC1XsWqrFsUn4fN91NnqCnZUNxwmMh6yQ1avKzHHZrptiQUwmXQ3SYZLXhbk-y00_ORQJK_HhwJjMMOkDqLz3lRzbF8n0WE3b3tqhhRf4g5hSLEV2_oIzf0K_wPc7P27GCGd39zE5-ekqMLaZ9nQ3suODiGBiDrofbjV-Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/595730e6c3.mp4?token=N7svXmUTaglfOKomh0R0qP6Zzgj2JjwHXx21POJFyF3KHyfdryJ0w1KXw03eN1j7sug43PigDivSZCsh9oUyXCYOLLfU8iu6VbR7jIKz7OescKTZiWYEuY9ezTz5mKbN6pVTtFUnqUDXj7SF6yHx4u5U2oWUxaWxpJ1HnYNMpHbIaQzAC1XsWqrFsUn4fN91NnqCnZUNxwmMh6yQ1avKzHHZrptiQUwmXQ3SYZLXhbk-y00_ORQJK_HhwJjMMOkDqLz3lRzbF8n0WE3b3tqhhRf4g5hSLEV2_oIzf0K_wPc7P27GCGd39zE5-ekqMLaZ9nQ3suODiGBiDrofbjV-Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دلقک بازی املاکی
😐
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/73084" target="_blank">📅 00:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73083">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b6424edb4.mp4?token=FjBH4oqVtK7frDIQsguqmdcgR4xsJw9QFrNsre4hLmHriMizSdL0scjhUpEFM5RKa1NlgKu5nfnL1B5TEYbbTopxIPj32pngggE-fHBW8JxQKRHa9wWrwXpnnZWWycEtszajxZZGVzJ0XM_ZjOSZYICTlTFg5re3b0HnXVXkwxWF289d_C0cpl3Aar869zLagBCxdilpRJzXSVqPgT0zdpthCNY74xMQXoG_S-1tilXXJd3O87Xh0HRY2dB1rUngRA7SRJeHT_1eJNcjzgtP6JW8Nvvg9ZuF27YFcOgWVtkEA4pHY5_wuLETarjlALj9rE2ONkKzP-UUGCdX4_312g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b6424edb4.mp4?token=FjBH4oqVtK7frDIQsguqmdcgR4xsJw9QFrNsre4hLmHriMizSdL0scjhUpEFM5RKa1NlgKu5nfnL1B5TEYbbTopxIPj32pngggE-fHBW8JxQKRHa9wWrwXpnnZWWycEtszajxZZGVzJ0XM_ZjOSZYICTlTFg5re3b0HnXVXkwxWF289d_C0cpl3Aar869zLagBCxdilpRJzXSVqPgT0zdpthCNY74xMQXoG_S-1tilXXJd3O87Xh0HRY2dB1rUngRA7SRJeHT_1eJNcjzgtP6JW8Nvvg9ZuF27YFcOgWVtkEA4pHY5_wuLETarjlALj9rE2ONkKzP-UUGCdX4_312g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارسالی یکی از اعضا از گرگان:
بارندگی شدید امشب در گرگان باعث وقوع سیل و وارد شدن خسارت به اموال مردم شده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/73083" target="_blank">📅 00:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73082">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c88cca8dd.mp4?token=iCl6iwaQcuMOcYAUHFwWQ6-nZTBtGrfn7tcGbD_yW94VJoICI-Fk9Cf1TRLQ2dvcqJFB_vkcPJuPsjAW8vnrKjHrkdHDRnPadRVsWzHnisHR7s37xgfmm-giGnhfCd3G9lyDTxllOgc_tLRaKxQ8wgetRkQaihiMDdRjnCbUxgnSIUOoCZa97rP-fehgQzJwPKUVCZ6ZhHRcoAY0ik8zDQG6fKsxk6xSfpvlv0uumnx2K_DqcQbK3S9o8QMMoXZ7OaZRwrn9n0c13lKS4H9I_jSmT8J97YCmy2O7LuOzCC4XmC-Gpx45qOfibD3DW9CqlsNm72Dt1ehd3ak-esAYng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c88cca8dd.mp4?token=iCl6iwaQcuMOcYAUHFwWQ6-nZTBtGrfn7tcGbD_yW94VJoICI-Fk9Cf1TRLQ2dvcqJFB_vkcPJuPsjAW8vnrKjHrkdHDRnPadRVsWzHnisHR7s37xgfmm-giGnhfCd3G9lyDTxllOgc_tLRaKxQ8wgetRkQaihiMDdRjnCbUxgnSIUOoCZa97rP-fehgQzJwPKUVCZ6ZhHRcoAY0ik8zDQG6fKsxk6xSfpvlv0uumnx2K_DqcQbK3S9o8QMMoXZ7OaZRwrn9n0c13lKS4H9I_jSmT8J97YCmy2O7LuOzCC4XmC-Gpx45qOfibD3DW9CqlsNm72Dt1ehd3ak-esAYng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">املاکی درباره تنگه هرمز:
«داریم به این فکر می‌کنیم که اسم تنگه هرمز رو به تنگه ترامپ تغییر بدیم!»
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/73082" target="_blank">📅 00:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73081">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e93cc318ec.mp4?token=CPbOIqWpzhPnra59ffISL9-lSyaW1hPh6DX980J5Dd9pH5_vv_PkQLaMRuFf_Y5VjnBGnvt8_SkPoVY_GlsbnrlLEEqH3OTkNPRsq7zEOWoA3CRYK_UEmz3Ehv-9zxJAtqZXEGF5pq3dF24jy-GEq-ZLDsNfGDBk9Uq35-UZgJoJlD08G60Sn-Qd1iHz9-g_avKrG5u91M7FG08Iz6TXrO3vw-byBIcloYbUQTZOVNl3SzewsbU5cVx0kLThQiK4r4-5JJaQGwNJp_XZ0ldvInjfNT01YV0Y72mdy1_Iau7Ax7kOMPeick7Rv1dbgm-TzhxR_RKZ0_UNY6asLY5TxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e93cc318ec.mp4?token=CPbOIqWpzhPnra59ffISL9-lSyaW1hPh6DX980J5Dd9pH5_vv_PkQLaMRuFf_Y5VjnBGnvt8_SkPoVY_GlsbnrlLEEqH3OTkNPRsq7zEOWoA3CRYK_UEmz3Ehv-9zxJAtqZXEGF5pq3dF24jy-GEq-ZLDsNfGDBk9Uq35-UZgJoJlD08G60Sn-Qd1iHz9-g_avKrG5u91M7FG08Iz6TXrO3vw-byBIcloYbUQTZOVNl3SzewsbU5cVx0kLThQiK4r4-5JJaQGwNJp_XZ0ldvInjfNT01YV0Y72mdy1_Iau7Ax7kOMPeick7Rv1dbgm-TzhxR_RKZ0_UNY6asLY5TxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«می‌تونیم خیلی سریع به این ماجرا پایان بدیم. ایرانی‌ها نمی‌دونن که من تا حالا چقدر باهاشون مدارا کردم و چقدر باهاشون راه اومدم.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/73081" target="_blank">📅 00:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73080">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/988c9468b6.mp4?token=ZmXCEjBHNzzV22fHM1VTzIG-uBWOFbibD1jSipIzB3v2C51Uo1SshqlJun8ECyi9WvvDOJtsk5kKm36ObUuudCWPaFjYAlnyLvZhkz9sLXB_9ebijTo1HXMOkrvSNvDLBHg3X8dBe8PdLdC6rJBH-sn7PkHTmV93_HjgtesaOik13H-7xJWQa_eiCbddCP4o2MaJfAhGhtK73PjJtfnxztTOIFD3CmeG4pqGTn3QtL-scwQyc50EMWB2whbNq0-bnqpf1vJhX012HUnCyl35wtRaZScU_kAiLONS-PpKwfZqCM7NmUz8nhFt1BHJX28Qe6mVCvz9xur9B768m6mu_5M4366Cs8rCCiiqUi8R-_Zbs7NmWvLbNQm8CCLhb5G6IW0XE3dq9Jp0_cypYpgccthj5h2OfUeoJ2lfNV3xiBgWuUdR0DT7Ke2DtmWAJImkuMjIzuXoopWBTD_ChFofCRvkenZJJiNbsWguNt4pnJAJLhKNqCLQTWRPONXKdIISA2Q1T56Id_CzPTMx9kqES1EZWL6uH6ZOaqVfZwy5Eru0DPj0NiRmo4nf8twk_QCPRUHwMKIKHJg8LJGrIKmApx8blqwqLRjlcNJxpQjYKftTq4VG_htdgRvsoACiCB_pZr6G9WtdXxQkVg211ISDnR3ijkT61ZJySbNvdRSC4tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/988c9468b6.mp4?token=ZmXCEjBHNzzV22fHM1VTzIG-uBWOFbibD1jSipIzB3v2C51Uo1SshqlJun8ECyi9WvvDOJtsk5kKm36ObUuudCWPaFjYAlnyLvZhkz9sLXB_9ebijTo1HXMOkrvSNvDLBHg3X8dBe8PdLdC6rJBH-sn7PkHTmV93_HjgtesaOik13H-7xJWQa_eiCbddCP4o2MaJfAhGhtK73PjJtfnxztTOIFD3CmeG4pqGTn3QtL-scwQyc50EMWB2whbNq0-bnqpf1vJhX012HUnCyl35wtRaZScU_kAiLONS-PpKwfZqCM7NmUz8nhFt1BHJX28Qe6mVCvz9xur9B768m6mu_5M4366Cs8rCCiiqUi8R-_Zbs7NmWvLbNQm8CCLhb5G6IW0XE3dq9Jp0_cypYpgccthj5h2OfUeoJ2lfNV3xiBgWuUdR0DT7Ke2DtmWAJImkuMjIzuXoopWBTD_ChFofCRvkenZJJiNbsWguNt4pnJAJLhKNqCLQTWRPONXKdIISA2Q1T56Id_CzPTMx9kqES1EZWL6uH6ZOaqVfZwy5Eru0DPj0NiRmo4nf8twk_QCPRUHwMKIKHJg8LJGrIKmApx8blqwqLRjlcNJxpQjYKftTq4VG_htdgRvsoACiCB_pZr6G9WtdXxQkVg211ISDnR3ijkT61ZJySbNvdRSC4tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«ایرانی‌ها می‌گن: همه رو می‌کشیمممم! همه روووو!
همچنین می‌گن: الحمدلله! الحمدلله! الحمدلله!
منم بهشون می‌گم: بابا، شماها واقعاً دیوونه‌اید!»
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/73080" target="_blank">📅 00:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73079">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8279d9c497.mp4?token=j3K3kkovoIA0IkPL3C08CFndQFb8rLS772vLbD4RgGlEk3FwwUfa8UqDSe1m1mMEZqqdP_2HPubFPrXeJq5wEynnjfL6uMOTIpXGlnxTLkKkyzBPxsoYwABgbKVY_Uq9mlOWy1RrRsCDepeKv80gMP0XP-OroFSP1vMHLhO_xTn2163buPqdB_gXodUk4tgPmQvE92cwaHn3gBJJM_nSvBl4Xn24R9vFKb7QL86Ls0S2Vnxt1ttLIO0VNafNC75p_aNoHTka0V9MHu6smzflJi5aImMgQPks51XIERjRIzRdU3hf5ykD5UScT4aoiGesu3IZqk9JfEVPVt4RA7UURg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8279d9c497.mp4?token=j3K3kkovoIA0IkPL3C08CFndQFb8rLS772vLbD4RgGlEk3FwwUfa8UqDSe1m1mMEZqqdP_2HPubFPrXeJq5wEynnjfL6uMOTIpXGlnxTLkKkyzBPxsoYwABgbKVY_Uq9mlOWy1RrRsCDepeKv80gMP0XP-OroFSP1vMHLhO_xTn2163buPqdB_gXodUk4tgPmQvE92cwaHn3gBJJM_nSvBl4Xn24R9vFKb7QL86Ls0S2Vnxt1ttLIO0VNafNC75p_aNoHTka0V9MHu6smzflJi5aImMgQPks51XIERjRIzRdU3hf5ykD5UScT4aoiGesu3IZqk9JfEVPVt4RA7UURg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور گلشیفته فراهانی در فیلم Matchbox: The Movie 2026 و صحنه لب گرفتن او با جان‌سینا!
+ نکته جالب اینکه همسر جان‌سینا هم ایرانیه!
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/73079" target="_blank">📅 23:52 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73078">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be8b607f1d.mp4?token=DcFIx-ltpoEQwBkQnXtcIRfgpNFrskbL0UqXSDVH2opHp6HDa5xl75WwUSci9tUdel0ix4iOYM_92ubecgoFoCADcaCH2OBCdSObwE-eKHfGldnjwbKIm1lHeUWVZ3Rt1scXjbxz2S9hsnnVKhI5_zLosQE_1NkoverULyHxHQTb-lBVWWj4H7b4p99RuVgiAZoaXWgYBoLJ8CU6NLBGF3Q28FacmXJAb46zm1KTMTNjwuORI4Q5KLS78lsPzWdlYuK5mg7bO-jHgGXAio1IZd8kTTNFydNl52P_JE4ZSIlziHIh2AcHvPUYCZlaoSr3aKjtYf5Qf63UzT7TTBA5vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be8b607f1d.mp4?token=DcFIx-ltpoEQwBkQnXtcIRfgpNFrskbL0UqXSDVH2opHp6HDa5xl75WwUSci9tUdel0ix4iOYM_92ubecgoFoCADcaCH2OBCdSObwE-eKHfGldnjwbKIm1lHeUWVZ3Rt1scXjbxz2S9hsnnVKhI5_zLosQE_1NkoverULyHxHQTb-lBVWWj4H7b4p99RuVgiAZoaXWgYBoLJ8CU6NLBGF3Q28FacmXJAb46zm1KTMTNjwuORI4Q5KLS78lsPzWdlYuK5mg7bO-jHgGXAio1IZd8kTTNFydNl52P_JE4ZSIlziHIh2AcHvPUYCZlaoSr3aKjtYf5Qf63UzT7TTBA5vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک پلنگ حکومتی :هر روز صبح و شب اینجام که بگم ما فقط جنگ میخوایم  و مذاکره نمی کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/73078" target="_blank">📅 23:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73074">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52a72e1a5c.mp4?token=F0yyKS2OK7SdnagiRRS1mx3TFc6vRs0doT5uLEm94RwV-Hs6opLuN3XGXNojaqch8R9rSMQjJ05V-q9BzsNT5irF7OVrvXRe9MB9RDcTL6JbAZh5mNPQGGJVRdhrzx3qYFqqjwUDdcbq4wLUJke6NpHR8zIBxxhq3Mjxxig97tEhWkgG2lmKnV0DnL6Wf6KLp1KU29kui5Vjj-dme_u67a_SRkGZXj3tTfxdSGDZWnV2kk_wyvTD13iYqFryOsKRUzASkjWuhnpXrW_3foSZDE8tvag4cluHOVzbjPqL8nKtp0uuqBehUnkPbpRVNcuwV2c6MA5k0wMmDwNCDF5ZFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52a72e1a5c.mp4?token=F0yyKS2OK7SdnagiRRS1mx3TFc6vRs0doT5uLEm94RwV-Hs6opLuN3XGXNojaqch8R9rSMQjJ05V-q9BzsNT5irF7OVrvXRe9MB9RDcTL6JbAZh5mNPQGGJVRdhrzx3qYFqqjwUDdcbq4wLUJke6NpHR8zIBxxhq3Mjxxig97tEhWkgG2lmKnV0DnL6Wf6KLp1KU29kui5Vjj-dme_u67a_SRkGZXj3tTfxdSGDZWnV2kk_wyvTD13iYqFryOsKRUzASkjWuhnpXrW_3foSZDE8tvag4cluHOVzbjPqL8nKtp0uuqBehUnkPbpRVNcuwV2c6MA5k0wMmDwNCDF5ZFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هوایی اسرائیل به ساختمانی چندطبقه در غزه
دقایقی پیش، جنگنده‌های اسرائیلی یک ساختمان چندطبقه در شهر غزه رو هدف قرار دادن. پیش از حمله، دستور تخلیه ساختمان صادر شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/73074" target="_blank">📅 22:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73073">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6e7ebfe2.mp4?token=s-4Ic-By2SJrRyjluwVRXNTo_CJSrneICFvyOt6FBCFIMmSElyONno42TCsA-q63Y_HOe0zPTw5Wq_It5ERM9CyncPcFKr_aYXl-Nw_CupgdKmPU4tfrVsWTNELLe0gk41eF_AmF2SCAgdqezCFCIyQIb71qYfwV62wTLEImOvSh-GElDupg8Y5fW8bONyXFXye715LE-S5brOar7irOgbWTu6CdOisnHcTCmrQ_ySxerlik4ziwQG7PIuaedq4LQ2ViaSqJ5UFEbKnEuqF3vcCplxiCjNbyiLt8g8w6vjLwnw2d1DA2BQTAlRu6vILMXwWhRLr-SkdAGuWqbDPwiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6e7ebfe2.mp4?token=s-4Ic-By2SJrRyjluwVRXNTo_CJSrneICFvyOt6FBCFIMmSElyONno42TCsA-q63Y_HOe0zPTw5Wq_It5ERM9CyncPcFKr_aYXl-Nw_CupgdKmPU4tfrVsWTNELLe0gk41eF_AmF2SCAgdqezCFCIyQIb71qYfwV62wTLEImOvSh-GElDupg8Y5fW8bONyXFXye715LE-S5brOar7irOgbWTu6CdOisnHcTCmrQ_ySxerlik4ziwQG7PIuaedq4LQ2ViaSqJ5UFEbKnEuqF3vcCplxiCjNbyiLt8g8w6vjLwnw2d1DA2BQTAlRu6vILMXwWhRLr-SkdAGuWqbDPwiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضرغامی: پخش خطبه‌های نماز جمعه از اشتباهات من بود!
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/73073" target="_blank">📅 22:31 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73072">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/be565181a8.mp4?token=C1CC7l7ciP0tHW1up5oj2mklq41xcI7gos1B4YN6HaiYsXvHZ0Mx3DZsdg0ZA7jDsxvhk_PiFwQHlf2hqARpjkX2FSuKne5wXKpoeDOiZA_v8AIGRrMLkU1y_k8cIMAWf6RZD78fCp-lgTK2pTdQ8w5reBXXAuVn5tUs1IKan6efc4WsYd2-OqEgQd6eBAzz2h4GHGAsGgZ5S58i_wEPk3nir10DKKqkWM6fG5yEEnAXmZToOlop90H-Ry-wBu4e1KOUM90ahEskGITwYxZ-s-OP4wF1v3ENqAvGTwaj57k9c-EWCau7eSpyvZqumX-zy3_67VSulY9KT2b9qvUg0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/be565181a8.mp4?token=C1CC7l7ciP0tHW1up5oj2mklq41xcI7gos1B4YN6HaiYsXvHZ0Mx3DZsdg0ZA7jDsxvhk_PiFwQHlf2hqARpjkX2FSuKne5wXKpoeDOiZA_v8AIGRrMLkU1y_k8cIMAWf6RZD78fCp-lgTK2pTdQ8w5reBXXAuVn5tUs1IKan6efc4WsYd2-OqEgQd6eBAzz2h4GHGAsGgZ5S58i_wEPk3nir10DKKqkWM6fG5yEEnAXmZToOlop90H-Ry-wBu4e1KOUM90ahEskGITwYxZ-s-OP4wF1v3ENqAvGTwaj57k9c-EWCau7eSpyvZqumX-zy3_67VSulY9KT2b9qvUg0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند وقت پیش مصاحبه یه دختر 25 ساله منتشر شد که ماشین 50-60 میلیاردی سوار بود!
بهش گفتن چطوری این ماشین رو خریدی؟ گفت تلاش و استمرار!
رفتن امارش رو درآوردن، دیدن باباش حسابرس شهرداری تهرانه و دختره آقازاده‌اس!
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/73072" target="_blank">📅 21:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73071">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/118178a3fa.mp4?token=RDueuN7yilvlBhfcPkIvRo7QrbRSLLO-p93NA0ShDSHHbBorN2TPGmh2v8iTAruN5G9-fjSVzqaQ3XKVkpk4rvKU826_UTwJrjvMayFFgdXQTMjGRovXMCUvFU2CO_3aMhWByDOhMm7C15-s_M806G2k8bfbjQO5T6t8AqoLT2Fv4UE8UQwHQUwcv-yQkzQsQewRhnOZDsXEy6If3032R9baVie0AS-EvOv4ST0AeX6TYWe0Eo7MCsnJJXPVNU27TaDXlgUDlwN2kD9Om9BrrJwVDULnL1pex-I-rgDeE_Rmp5331El0RIhvDDAtQZpGmiyiUbIuRWcaA4TIo_quqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/118178a3fa.mp4?token=RDueuN7yilvlBhfcPkIvRo7QrbRSLLO-p93NA0ShDSHHbBorN2TPGmh2v8iTAruN5G9-fjSVzqaQ3XKVkpk4rvKU826_UTwJrjvMayFFgdXQTMjGRovXMCUvFU2CO_3aMhWByDOhMm7C15-s_M806G2k8bfbjQO5T6t8AqoLT2Fv4UE8UQwHQUwcv-yQkzQsQewRhnOZDsXEy6If3032R9baVie0AS-EvOv4ST0AeX6TYWe0Eo7MCsnJJXPVNU27TaDXlgUDlwN2kD9Om9BrrJwVDULnL1pex-I-rgDeE_Rmp5331El0RIhvDDAtQZpGmiyiUbIuRWcaA4TIo_quqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: زلنسکی گفته توافق نفتی شما با پوتین نشونه ضعف شماست.   ترامپ: کی اینو گفته؟  خبرنگار: زلنسکی.  ترامپ: باشه!  @News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/73071" target="_blank">📅 21:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73070">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2bf843dd2a.mp4?token=bzUMVszIR4xVL7tASq-tBI6MGVIfwD6NUmVERLfVVLcepzCq8LhVD6NiAoltnCIEpMthXNYizLFhHH_IyXcLizTfVfwvw-rtlZvJ6iDkHnmg1YAn9q6tdWyRl5kiCqeX0mM-lEJigubl3JvjpxZK_IQ5zBwy_MzEyuM28vMzgi0SuZ0KyTYMuy4WI8ugfqGkgtlXD_CEU5ZIeGY9uPovMsvnBRmLmb-fnrZ4stkbnDAHTvG2cGdPegRfgDzQ5d89BrpR_EXPWdd0ODlFiX8EugDDqQlImKsUeV9aHn6XXPXH8Mwk5YHqlM8-wW2mrg-HkvNaWKldZ2bCd9IGLn7ehg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2bf843dd2a.mp4?token=bzUMVszIR4xVL7tASq-tBI6MGVIfwD6NUmVERLfVVLcepzCq8LhVD6NiAoltnCIEpMthXNYizLFhHH_IyXcLizTfVfwvw-rtlZvJ6iDkHnmg1YAn9q6tdWyRl5kiCqeX0mM-lEJigubl3JvjpxZK_IQ5zBwy_MzEyuM28vMzgi0SuZ0KyTYMuy4WI8ugfqGkgtlXD_CEU5ZIeGY9uPovMsvnBRmLmb-fnrZ4stkbnDAHTvG2cGdPegRfgDzQ5d89BrpR_EXPWdd0ODlFiX8EugDDqQlImKsUeV9aHn6XXPXH8Mwk5YHqlM8-wW2mrg-HkvNaWKldZ2bCd9IGLn7ehg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه تصاویری از آتش‌سوزی گسترده و نشت نفت از یک نفتکش منتشر کرده که به گفته این نیرو، بر اثر برخورد با مین دریایی در تنگه هرمز آسیب دیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/73070" target="_blank">📅 21:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73069">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3875ef3f4f.mp4?token=AaQ_UNPuzCSQBZ-oviqVNO3OZcuX1M-6YSSsQglQocqXBIIcxnWG9DZxMaSUfgEA0l_BxmhaYcd0h_lb1ezYJp57ZTZ4CMmqoYBab1PqZgAIJYm7b9yh2jl92KuCk67d_04mEdi99rD9_y0iyyeTPWBoAY-Y34M_hRDfvX4oxFeUuqNugXEZLTex9Txw_t69nRLlQpCFiS8bX77ui-VKrWjhLlYkzR7qJGE3T0O1tQNCJHiwjDbAX513-C6oGrpP-rnJ5cQpGFcVapEN_l9SdyDZhP1JpN-1IJ8-n9VzbXGVGWztPj7BGxWZbIhgRVbaCJ20u6uwAx_Pa0kSrTg-5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3875ef3f4f.mp4?token=AaQ_UNPuzCSQBZ-oviqVNO3OZcuX1M-6YSSsQglQocqXBIIcxnWG9DZxMaSUfgEA0l_BxmhaYcd0h_lb1ezYJp57ZTZ4CMmqoYBab1PqZgAIJYm7b9yh2jl92KuCk67d_04mEdi99rD9_y0iyyeTPWBoAY-Y34M_hRDfvX4oxFeUuqNugXEZLTex9Txw_t69nRLlQpCFiS8bX77ui-VKrWjhLlYkzR7qJGE3T0O1tQNCJHiwjDbAX513-C6oGrpP-rnJ5cQpGFcVapEN_l9SdyDZhP1JpN-1IJ8-n9VzbXGVGWztPj7BGxWZbIhgRVbaCJ20u6uwAx_Pa0kSrTg-5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: شما گفته بودید تا بعد از انتخابات میان‌دوره‌ای به ایران حمله نمی‌کنید. حمله اخیر در عربستان باعث شده نظرتون عوض بشه؟
ترامپ: «بررسیش می‌کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/73069" target="_blank">📅 20:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73068">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba9c18ae3.mp4?token=fflgB3pZnsJx5kNv7kpkUiwtTDK5ats-IaDk0L7m8j4ZYHeyk57SxbAtDceeOh3vPDT2GsAFUPGO1lNWigqcYaZkByECnld3ffYmqMvn-9kzouXEy48pWX7lPr4eGWXyTGNvDRpN2FTsLXXsd34n5Xl7FqJ6yhLQjleuc7WJGJcXYT8p5UYsrE9JfYN9a9pm-9mnHk5OalOadEHLgCPP9MW46Y_GeoWE_c1AzDEqf34gc0N5V2_NZmJHt9W6hgYDmnIFOeuKCBeMx4Sk1_NWa81WRcB_i54aKqBYOlbk_0GYtoFR3aBerNc-TNeW1oDcvaJ1p9m8x8mZG5TcEKzuJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba9c18ae3.mp4?token=fflgB3pZnsJx5kNv7kpkUiwtTDK5ats-IaDk0L7m8j4ZYHeyk57SxbAtDceeOh3vPDT2GsAFUPGO1lNWigqcYaZkByECnld3ffYmqMvn-9kzouXEy48pWX7lPr4eGWXyTGNvDRpN2FTsLXXsd34n5Xl7FqJ6yhLQjleuc7WJGJcXYT8p5UYsrE9JfYN9a9pm-9mnHk5OalOadEHLgCPP9MW46Y_GeoWE_c1AzDEqf34gc0N5V2_NZmJHt9W6hgYDmnIFOeuKCBeMx4Sk1_NWa81WRcB_i54aKqBYOlbk_0GYtoFR3aBerNc-TNeW1oDcvaJ1p9m8x8mZG5TcEKzuJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در ویدیویی جدید که در تیک‌تاک منتشر کرده، در حال ورزش کردن در باشگاه دیده می‌شه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/73068" target="_blank">📅 20:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73067">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89266c981.mp4?token=MwvzbDB7S1VYnzUtyXgOkaor7oTb7oYRjRqZ6d2s9-QvWTmf5D_HLkWy6fCBFygT4OcNNQC2xOrlmOOKcTvsv6lajQ306i0iINKQ_KI1dBJkM1gu52NU7DAnmRDl1CwYaS_rF3GNLE_XGiG8PR7L16yfBg_bjrxiI3K7yGSrIwNwI0m_GkZad3h5QI6CT2YMfB5Isu0vcxH8JJdyCRUWyLKYk0OYU0DmMdUNlGVnuJBA86P0pKWjhQeZcjmx2gEDmJmENf_MwJBMfN1M36SAsIMq2qvXvu_5kPt3dHqwn05OBkbyunglyvIXQTtevmTUuZ9zbFZuclCbqLachhOEwoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89266c981.mp4?token=MwvzbDB7S1VYnzUtyXgOkaor7oTb7oYRjRqZ6d2s9-QvWTmf5D_HLkWy6fCBFygT4OcNNQC2xOrlmOOKcTvsv6lajQ306i0iINKQ_KI1dBJkM1gu52NU7DAnmRDl1CwYaS_rF3GNLE_XGiG8PR7L16yfBg_bjrxiI3K7yGSrIwNwI0m_GkZad3h5QI6CT2YMfB5Isu0vcxH8JJdyCRUWyLKYk0OYU0DmMdUNlGVnuJBA86P0pKWjhQeZcjmx2gEDmJmENf_MwJBMfN1M36SAsIMq2qvXvu_5kPt3dHqwn05OBkbyunglyvIXQTtevmTUuZ9zbFZuclCbqLachhOEwoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رائفی‌پور: آمریکا را پایین کشیدن کاری ندارد.روسیه باید پالایشگاه‌های آمریکا را هدف بگیرد تا حملات اوکراین متوقف شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/73067" target="_blank">📅 20:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73066">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vT7gKE1ZwJF_mxBGfNDEGPP12OI2WV5vtFxOgggd1wEqbNw3juQRDAOalwWmWaqZOQ_7baHV7SzczyW3FFAIDFmWPIsjzMn5EBCqpp2ktgEAGDb6xLxXnxwGvkL8v3F1pAWVZCwnwCm4AkoVExPvri2HRzl3dLWzEHSkjqs-fN5SGPwjClkTgsx2vZZ0tDfrxsSrxGBVbXKOAzWHUoUoEVVIFaa027owOCFAxKGMVXnXhTvvmMeQYyoNwHYmJPUd1BFi0SGgPZW-Ak7NYl7d388y_ldxF72-RTFmzBhWZ_AOhhKAP6jhdPrcuh3d1AOcYRQs38WSo4HvSbKM20YFTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین محموله گازوئیل روسیه به مقصد آمریکا حرکت کرد؛ قبل از اعلام توافق ترامپ!
اولین محموله گازوئیل روسیه که راهی آمریکاست، ۲۲ سپتامبر از بندر سن‌پترزبورگ حرکت کرده؛ یعنی دو هفته قبل از اینکه ترامپ توافق رو اعلام کنه.
این نفتکش یونانی با نام MINERVA ZEN حدود ۲۷۵ هزار بشکه گازوئیل حمل می‌کنه و پیش‌بینی می‌شه ۱۱ یا ۱۲ اکتبر به سواحل شرقی آمریکا برسه.
تحلیلگران می‌گن حجم این محموله‌ها در مقایسه با مصرف گازوئیل و سایر سوخت‌های تقطیری آمریکا، فقط برای چند روز کافیه. از طرفی، حملات اوکراین به پالایشگاه‌های روسیه هم باعث کاهش تولید گازوئیل این کشور شده.
@News_Hut
| Clash Report</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/73066" target="_blank">📅 19:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73065">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3e4a880ec.mp4?token=KFMl5cK1nFBjN5SHJpWF-9Cns345LAdDR99PoW6cq7zYn6O2afBNpY5B618LDpSGmzDJp7yx2GFtbjcQ8nePlua6tBXJFDkWuSQlHuCocj11kFMW_qmcOr6U_jpmiigLor4DSVEavauw11KA00zsiayg0bZpX8DDwevYp2JTvPo0FLMLDBgeQahRCoOJ0xcliqjKl1u0pbZOuSeirdgj0p0s5VCvJj936QCZZ8e53InGvqKXbUEFR_DjYhCKaM46CLjaW17qRY007eU23AAz3o62QYwx7g5FDJToifa8G3wmCFQ938CgiSZJgC9wbBLcWq8H2puL4cBa6MfwCl9UYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3e4a880ec.mp4?token=KFMl5cK1nFBjN5SHJpWF-9Cns345LAdDR99PoW6cq7zYn6O2afBNpY5B618LDpSGmzDJp7yx2GFtbjcQ8nePlua6tBXJFDkWuSQlHuCocj11kFMW_qmcOr6U_jpmiigLor4DSVEavauw11KA00zsiayg0bZpX8DDwevYp2JTvPo0FLMLDBgeQahRCoOJ0xcliqjKl1u0pbZOuSeirdgj0p0s5VCvJj936QCZZ8e53InGvqKXbUEFR_DjYhCKaM46CLjaW17qRY007eU23AAz3o62QYwx7g5FDJToifa8G3wmCFQ938CgiSZJgC9wbBLcWq8H2puL4cBa6MfwCl9UYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان اجرای ارکسترال «آرش» در سالن اسپیناس تهران، در شامگاه جمعه ۱۷ مهر، تماشاگران در واکنش به صحبت‌های اسماعیل بقایی، سخنگوی وزارت امور خارجه جمهوری اسلامی، او را هو کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/73065" target="_blank">📅 19:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73064">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">برآوردهای اولیه از تلفات حمله به فرودگاه ریاض:
بر اساس برآوردهای فعلی، در پی اصابت یک تا دو موشک بالستیک انصارالله به ترمینال ۳ فرودگاه بین‌المللی ملک خالد در ریاض:
مجروحان: حدود ۴۰ تا ۷۰ نفر
کشته‌شدگان: حدود ۳ تا ۵ نفر
این آمار در حد برآورد اولیه است و هنوز تأیید رسمی آن مشخص نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/73064" target="_blank">📅 18:26 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73062">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23f8abc61b.mp4?token=Sda8qQmXBIbUePpkzz2eN5d0KfMu1AFSEWX8OvPZ0WezihDRAE2_CPKvj2Q7z6M_Zx3_EyGRyhp7CVLofTlrD92HxoSHH6534Brjzv9NRosZjhmmFtiXzOjMaT0JW41vOJT1oeSfFv_95zBT_BLWhej9bh5wn0DBWM1oLmtew2Jzajan_sCHXP9TbE8pLVrGI5-pkwF8dxqXakbXhwYqaQZcnFVrcxqicXkz8yyEIIr1D0pO_XsKyamSyODXEAHK272KLUkimMMBhIVvDtbtwFIMZZN4OyTjLlWs4OBTYycjC9MNYfYx8UqYV4iInfcMJdI_nZSkVKA9Oyko-bcpGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23f8abc61b.mp4?token=Sda8qQmXBIbUePpkzz2eN5d0KfMu1AFSEWX8OvPZ0WezihDRAE2_CPKvj2Q7z6M_Zx3_EyGRyhp7CVLofTlrD92HxoSHH6534Brjzv9NRosZjhmmFtiXzOjMaT0JW41vOJT1oeSfFv_95zBT_BLWhej9bh5wn0DBWM1oLmtew2Jzajan_sCHXP9TbE8pLVrGI5-pkwF8dxqXakbXhwYqaQZcnFVrcxqicXkz8yyEIIr1D0pO_XsKyamSyODXEAHK272KLUkimMMBhIVvDtbtwFIMZZN4OyTjLlWs4OBTYycjC9MNYfYx8UqYV4iInfcMJdI_nZSkVKA9Oyko-bcpGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از فرودگاه بین‌المللی ملک خالد در ریاض پس از حمله منتسب به حوثی‌ها (انصارالله)
در این تصاویر، آثار خون روی زمین دیده می‌شه و نیروهای امدادی گسترده‌ای در محل حضور دارن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/73062" target="_blank">📅 18:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73061">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">گزارش‌ها از وقوع حادثه‌ای بزرگ در فرودگاه ریاض؛
گزارش‌ها حاکی از وقوع حادثه‌ای جدی در فرودگاه بین‌المللی ملک خالد در ریاضه. احتمال داده می‌شه یک موشک بالستیک حوثی‌ها (انصارالله) به این فرودگاه اصابت کرده باشه.
تعداد زیادی از نیروهای امدادی و اورژانسی به محل حادثه اعزام شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/73061" target="_blank">📅 18:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73060">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">#فوری
؛ خبرگزاری فرانسه (AFP):
خبرگزاری فرانسه به نقل از سه شاهد عینی گزارش داده که در حال تخلیه افراد از فرودگاه بین‌المللی ملک خالد در ریاض، پایتخت عربستان سعودی، هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/73060" target="_blank">📅 18:16 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73059">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc0bb8954.mp4?token=Ef_vdZM32WLV3F0anItSsSyYndkoki0LpdsjJVLDxG9qFpsdNJjiOQ_y_jXcNBYTBihW3m3fCD315UXcbIp2_s672C8zZTUSHFzNOCKVa4A-3Vc78HQwjlV-OiMj1dz3mqXZwBrzMf7iZtB9KEd6qUVkFx6FEpTiOdiD6B98bP_94KXqckuBvHe3hrFA5ulUmbBlNt5BpyMQkgWFrgg3SPcHFaDmTV-HLADQ5cJDpd4LFX-xMRWB6RTkBtZTZ7wPbU7gomQkzcMY3wtmxs8Wij5INfD1IgFzPlFO16chT7jBZxl0upMt2spQJgU3ZX2xM4tY6AwgHCKAwqH3U8TJSj-nIJ5XDjIsb5mH7cv3C9gpIpZHlOk-vgeiNHkMJM1oS4Wl0RBk9YhEic-rhnpZsS2G1zIo7srPeKHEsqyuPWdfiBvyz9UfNnVwxmHqobOWzMKk9Yl84B5KcqcCWfiHWsoMqjrLeD7KePjUzWSWSEA5jvv40MCPvBxamU17axVYUybXQE_WcLte3ewmF8JcJM902QoEXxeC-ShMsqzyYc2QrrYVVWz36tPaebekFlDUrzaGGi3R8UfBZDZ-5S_N4pNBCBc4Rvk84ENcR6l_6y8I2bc79Tni06MdIToRpMsHqVbmg0N5OD87dYAxijkeT6QYGtonksagn7lUF_jw06w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc0bb8954.mp4?token=Ef_vdZM32WLV3F0anItSsSyYndkoki0LpdsjJVLDxG9qFpsdNJjiOQ_y_jXcNBYTBihW3m3fCD315UXcbIp2_s672C8zZTUSHFzNOCKVa4A-3Vc78HQwjlV-OiMj1dz3mqXZwBrzMf7iZtB9KEd6qUVkFx6FEpTiOdiD6B98bP_94KXqckuBvHe3hrFA5ulUmbBlNt5BpyMQkgWFrgg3SPcHFaDmTV-HLADQ5cJDpd4LFX-xMRWB6RTkBtZTZ7wPbU7gomQkzcMY3wtmxs8Wij5INfD1IgFzPlFO16chT7jBZxl0upMt2spQJgU3ZX2xM4tY6AwgHCKAwqH3U8TJSj-nIJ5XDjIsb5mH7cv3C9gpIpZHlOk-vgeiNHkMJM1oS4Wl0RBk9YhEic-rhnpZsS2G1zIo7srPeKHEsqyuPWdfiBvyz9UfNnVwxmHqobOWzMKk9Yl84B5KcqcCWfiHWsoMqjrLeD7KePjUzWSWSEA5jvv40MCPvBxamU17axVYUybXQE_WcLte3ewmF8JcJM902QoEXxeC-ShMsqzyYc2QrrYVVWz36tPaebekFlDUrzaGGi3R8UfBZDZ-5S_N4pNBCBc4Rvk84ENcR6l_6y8I2bc79Tni06MdIToRpMsHqVbmg0N5OD87dYAxijkeT6QYGtonksagn7lUF_jw06w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ملکه تایلند برای نخستین بار به تنهایی هدایت یک جنگنده گریپن سوئدی رو بر عهده گرفت و پس از فرود موفق، از پادشاه مدال دریافت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/73059" target="_blank">📅 18:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73058">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73058" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/73058" target="_blank">📅 18:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73057">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SurcaJPvnYYmi9kbDDyoi_1xV2et6n2_zV29eSqMmulLpBeh1uO8BNREwIS5cJEfVA5b-GvnXn3qusGVhQFHxVyJweD3N_GSo1_PNo2-kGFxmO1o7RWXFesefUjAadB7_itU4RahLg5JM_xK7QRXOqAj1K7GcQ0LlUPu8482jwFtpXAjbAEvcsV6rLLOLrFdDjzXoEUtQjklZZewFH2FRLB3mCYIEWXSbhcqtif0UwB87MncCI7oZG1_uTAtZrGjAZytQIUHJzKIt8FAEJTy6-iBeIQvYOmlSDU5g_dR2eHsYinp32LpeWUT9daSCypyC2o0qQROyoTgssWb8H2wNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز ویارئال
🆚
رئال مادرید رو در
TrexBet
از دست نده!
📉
نگاهی به آمار ۲ تیم در ۵ رویارویی اخیر:
ویارئال: ۲ برد، ۳ شکست و ۱۱ گل زده
رئال مادرید: ۳ برد، ۲ شکست و ۱۰ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/73057" target="_blank">📅 18:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73056">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c52e5fb32c.mp4?token=Q6HeNdRA-H_-NOwIJxjyfI6qiiRshSs8hDsmRfzoND10Yy5KN1JkrLRFDDtTqxbhqwf6ZENadR5xgCQT3zOnZtvImRaTRy1lBXEfpYQPsIj9bMHht5BfdP-djqtyWaNwTQLyPA__Xsb9sQunFhL6U1M3aWFTeAAq6abIACM2237YPw7rZSmNDouBAPWnZINa9bDM4ZVCjyxMf8LiDBsqJIG2mO0ve0qBuZyjjiBxDsTFGJoaGq_J0CCwWINC_7Nzr_KOTptPL1bJ-vEv-fLlwcRjfdkRgzwSTzf1lekt9QXoP5clNW-GWZAFt0uo8upGNxAqmkGLxoIAnvbzuEQSgwFmDahOoIrrONoaJGgn7b3llLXCeDHWVaDCYZ8PpzkQZ2XQHxDpm69HsogbNG_s8io1-fPxRwHFFi8HEXQpS8b9-sIuc2BbDVvwTYeyI_tQLpW9aw0R70qroMjwQdJ8ynhB9V004Gc4AdfVORgZUsxe4xxHlSXmzFMolEu7-_eh_LwryyiqweUUxW-dPZ4OaxHVAQ10a7rcmB9GN8gsN-QFnYItnKJtMtcIwclQcLbEe6l-wMQucMkU_rMos_tNHP6wi-80zzDly0ykpQGMuGC46SA6xrYkG-f7XO6U0vj1BOUm4xxhKyATd5NGePo_ir5wwxJ9AwzZt1wOgwmyLgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c52e5fb32c.mp4?token=Q6HeNdRA-H_-NOwIJxjyfI6qiiRshSs8hDsmRfzoND10Yy5KN1JkrLRFDDtTqxbhqwf6ZENadR5xgCQT3zOnZtvImRaTRy1lBXEfpYQPsIj9bMHht5BfdP-djqtyWaNwTQLyPA__Xsb9sQunFhL6U1M3aWFTeAAq6abIACM2237YPw7rZSmNDouBAPWnZINa9bDM4ZVCjyxMf8LiDBsqJIG2mO0ve0qBuZyjjiBxDsTFGJoaGq_J0CCwWINC_7Nzr_KOTptPL1bJ-vEv-fLlwcRjfdkRgzwSTzf1lekt9QXoP5clNW-GWZAFt0uo8upGNxAqmkGLxoIAnvbzuEQSgwFmDahOoIrrONoaJGgn7b3llLXCeDHWVaDCYZ8PpzkQZ2XQHxDpm69HsogbNG_s8io1-fPxRwHFFi8HEXQpS8b9-sIuc2BbDVvwTYeyI_tQLpW9aw0R70qroMjwQdJ8ynhB9V004Gc4AdfVORgZUsxe4xxHlSXmzFMolEu7-_eh_LwryyiqweUUxW-dPZ4OaxHVAQ10a7rcmB9GN8gsN-QFnYItnKJtMtcIwclQcLbEe6l-wMQucMkU_rMos_tNHP6wi-80zzDly0ykpQGMuGC46SA6xrYkG-f7XO6U0vj1BOUm4xxhKyATd5NGePo_ir5wwxJ9AwzZt1wOgwmyLgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این دختر خانوم با این پسره تو رابطه اس و که علاوه بره پسره، سگ دوست پسرش هم عاشق دوست دختر پسره شده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/73056" target="_blank">📅 17:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73055">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/502e54151d.mp4?token=BsXCe-Ea3Emh6lyqCCXssK6C_cbAwVGpFiZ8sd2GBhGSiCsogFLOd9amWYTbRk6lMC8hsnwXDJXlbbqOnjYfzq4yWz2P5FvyhwPw_zKkscWva1RxyA4QuMoj1vTkXXV7LDKkVIuSxW-spxNlN-aMS9Zj1KhJnI4WdxK7R3Od4BuuxRLZTLhi2Yi-i0Fc_r5VLgRle6O555WG1-EjghvTKxN9NBrXOKUWg0BGpiloSVeN2NGPO9XJofYM_epIyc9_6pL7se9xTQaEbKocnnxTrDEtwUD33m1-jHlhvPW2faJqBq3gEI_JkbPefNqoo5Q1m7kpnMwLxLm-chcyHQyNuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/502e54151d.mp4?token=BsXCe-Ea3Emh6lyqCCXssK6C_cbAwVGpFiZ8sd2GBhGSiCsogFLOd9amWYTbRk6lMC8hsnwXDJXlbbqOnjYfzq4yWz2P5FvyhwPw_zKkscWva1RxyA4QuMoj1vTkXXV7LDKkVIuSxW-spxNlN-aMS9Zj1KhJnI4WdxK7R3Od4BuuxRLZTLhi2Yi-i0Fc_r5VLgRle6O555WG1-EjghvTKxN9NBrXOKUWg0BGpiloSVeN2NGPO9XJofYM_epIyc9_6pL7se9xTQaEbKocnnxTrDEtwUD33m1-jHlhvPW2faJqBq3gEI_JkbPefNqoo5Q1m7kpnMwLxLm-chcyHQyNuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از بمباران پادگان سپاه در خرم‌آباد، استان لرستان، در جریان جنگ ۴۰روزه:
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/73055" target="_blank">📅 17:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73054">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPSkiYknLoX92SS35tc--BRo9qr_viIcNDXyWHy0Q8O4EOAuFAtnGXLnk1AFmnf5Mv9kiSX3O75DHkVe2o6cSSxwdShjiQqmBapHsyujSIZtVMhqlxRwTRQ0D65JdPkD_d_A_FVylOY4gNRXb7870S5sN_tKchfcARNMf8Hupeamq8DmJTREgC1laRmMf3tL3me7l3pTrefxGKudRKjzxXN3--iFagtlmGMqBIbX-s0UIivaNkwcljHblL-UBCaU3EUXIxy1BFAg9hNXh8SaSXygTIkxz1_D30_RMFcVg_vsSPOdebST8dx0U6uq_Prg4KmufQTyxDijsT3OL83Zdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛
معاریو: آمریکا از اسرائیل خواسته به‌تنهایی به ایران حمله کنه!
طبق این گزارش، واشنگتن توی مذاکرات دو هفته اخیر از اسرائیل خواسته بود بدون مشارکت مستقیم آمریکا، حمله نظامی به ایران رو انجام بده.
هدف آمریکا این بوده که پیش از انتخابات میان‌دوره‌ای نوامبر، هزینه سیاسی حمله به ایران متوجه ترامپ نشه؛ درحالی‌که چنین حمله‌ای می‌تونست از نظر سیاسی به نفع نتانیاهو، پیش از انتخابات اسرائیل در ۲۷ اکتبر، تموم بشه.
ایال زامیر، رئیس ستاد ارتش اسرائیل، هشدار داده بود که ازسرگیری جنگ می‌تونه باعث تعویق انتخابات اسرائیل بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/73054" target="_blank">📅 16:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73053">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fca26fcca.mp4?token=g3RWNroiPXJ5xT0o-wULx5SSTGYoA086x7xmdIMN4SaHLZHJ1XVtpdUCbd9I7HK_zpZ6oTooFwLP52ZYfJSOvAahZrSlCFZfLWjjywNPY9CcWvVN8cTaft3n1mN4lWlvnXKG2eqZso3QRVzkQoKwkirBJkZruLIpANZzrbFDvrv6S7tXMAZlT2LMsqyEsedmgkQlAQ0TV-kLdFkgD4kftc_yVPf61PkeahUUYzRzWuwCY2oDzkzyE_TPRfJyE-08KTYtaAEVKV7KMet6FPOkxp-igv4-ZDM7kOGgqzxUaR6NQGOtXlLUAAUoZmj6xzn27cxJM_vvnW00l4wXXPiYzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fca26fcca.mp4?token=g3RWNroiPXJ5xT0o-wULx5SSTGYoA086x7xmdIMN4SaHLZHJ1XVtpdUCbd9I7HK_zpZ6oTooFwLP52ZYfJSOvAahZrSlCFZfLWjjywNPY9CcWvVN8cTaft3n1mN4lWlvnXKG2eqZso3QRVzkQoKwkirBJkZruLIpANZzrbFDvrv6S7tXMAZlT2LMsqyEsedmgkQlAQ0TV-kLdFkgD4kftc_yVPf61PkeahUUYzRzWuwCY2oDzkzyE_TPRfJyE-08KTYtaAEVKV7KMet6FPOkxp-igv4-ZDM7kOGgqzxUaR6NQGOtXlLUAAUoZmj6xzn27cxJM_vvnW00l4wXXPiYzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظاتی ترسناک و باورنکردنی که امواج عظیم زیر رعد و برق یک کشتی باری غول‌پیکر را ناچیز نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/73053" target="_blank">📅 16:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73052">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PEEs8onVjS2ikZ5jTlfjIwDkij7rdDml9_0FrEuX1ll_m2-Bge6UEFIIYhCLUutI0p7u-yRmHdpJE0X3YMm-zJB1HIdwb1bZhtZHRcJBQj8NScDXeM0pGzuhAIswKYwKzroiWPBVCLnOQgZ5_YPFEt66X3C8J1Gcmq7gCR_AmG8IIedXjy_Xw1pS6AhpPGBKIJ5zuj9Q9Sf3icM3fwqMGOrJE6ETdp064oGCoct87nfwdMGO9JF5C4Zv_9aaPAdlb3pEq02h7GG1AUzj7Z_NsEVB2xI7gK_3MO7mU7ttfRir1IdyMo2U9hE4dGQbibZLN5I0Tp1UflJE99j3BOzDlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:«من به ۸ جنگ پایان دادم و به پایان دادن یا حل‌وفصل ۲ جنگ دیگه هم نزدیکم.
همه گروگان‌های اسرائیلی، از جمله ۲۸ نفر آخر رو، چه زنده و چه کشته‌شده، برگردوندم.
صدها گروگان از کشورهای مختلف جهان رو آزاد کردم و به خونه‌هاشون برگردوندم.
در ونزوئلا در جنگ پیروز شدم و دیکتاتور خشنی رو که با بی‌رحمی اون کشور رو اداره می‌کرد، دستگیر کردم.
همچنین جلوی جمهوری اسلامی ایران، بزرگ‌ترین حامی دولتی تروریسم در جهان، رو گرفتم تا به سلاح هسته‌ای دست پیدا نکنه؛ و خیلی کارهای دیگه!
با وجود همه این کارها، نه من و نه ایالات متحده آمریکا جایزه صلح نوبل رو نگرفتیم. عجب!»
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/73052" target="_blank">📅 15:43 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73051">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f583eac4a.mp4?token=aRwJyBVe8g-Un2uVCZtyL-Ss8lO7RsUFC8YFxG_zbE8HKeSvThdJ1pzD2TzVvsUNTCez9fyja_qMGyaxegyE--ghWA3tLQx5UqRhdr7cyvFH2chlHcOLYgbjWf7VvgsecwbVtNE2CkDiF61XsD0ocMpgZa54aEL6Kh3TVGuZpyaq6EIhQCRDI7nD1M9nFWIYZS44l2hiLVp0jHmKZohiHgOb1yh6OmikE7M8pF-pZqpI2Oo7hFTWP-wPXoj83vzIM0yi__S3nLmz9RShhKcIttXpUAb2G6lc11YpQbBVbut8Qopl79wzxU9cgMeoUWRmMWwOQh5bTiW4Z83OGMzFeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f583eac4a.mp4?token=aRwJyBVe8g-Un2uVCZtyL-Ss8lO7RsUFC8YFxG_zbE8HKeSvThdJ1pzD2TzVvsUNTCez9fyja_qMGyaxegyE--ghWA3tLQx5UqRhdr7cyvFH2chlHcOLYgbjWf7VvgsecwbVtNE2CkDiF61XsD0ocMpgZa54aEL6Kh3TVGuZpyaq6EIhQCRDI7nD1M9nFWIYZS44l2hiLVp0jHmKZohiHgOb1yh6OmikE7M8pF-pZqpI2Oo7hFTWP-wPXoj83vzIM0yi__S3nLmz9RShhKcIttXpUAb2G6lc11YpQbBVbut8Qopl79wzxU9cgMeoUWRmMWwOQh5bTiW4Z83OGMzFeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهرداری خرمشهر دیده یه سرسره تو پارک شکسته، با خودشون گفتن چکارکنیم چکارنکنیم؟؟
که این نیمه شاهکار رو پیاده کردن :
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/73051" target="_blank">📅 15:32 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73050">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76ef585e24.mp4?token=snm40_qWySlnCRgrkm2NxAhOAmyEwu8V87zWtZ9pwdEltCEn3Osw-FVCZ5kWO0pIJBCw-OkScs4zL6zNlkB1K3nA0pTTK9tM72C4nHXOzDLuftlwGfK8S5n7mdva1xAI0LZpZPfoehMZpGQUItMedoNswgw2fSHkXfspEYy3PpY-ue4ZAlsmM6yPSQ11gAvSy8wUfcOXK19eh4CsLhq7VZSros3B0F5rrPxu8OwI8s_4X7MhsJxXy-Lfx4SH4cpzwOBRST-fL0QnBCFl3HIlbzotqB78zJ9CF8veprHWvmOkpMbp-nM9BmN-iOK9dUv4gigNoabBGWOMKCHeVpF5lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76ef585e24.mp4?token=snm40_qWySlnCRgrkm2NxAhOAmyEwu8V87zWtZ9pwdEltCEn3Osw-FVCZ5kWO0pIJBCw-OkScs4zL6zNlkB1K3nA0pTTK9tM72C4nHXOzDLuftlwGfK8S5n7mdva1xAI0LZpZPfoehMZpGQUItMedoNswgw2fSHkXfspEYy3PpY-ue4ZAlsmM6yPSQ11gAvSy8wUfcOXK19eh4CsLhq7VZSros3B0F5rrPxu8OwI8s_4X7MhsJxXy-Lfx4SH4cpzwOBRST-fL0QnBCFl3HIlbzotqB78zJ9CF8veprHWvmOkpMbp-nM9BmN-iOK9dUv4gigNoabBGWOMKCHeVpF5lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میرسلیم:
نفت ایران مال مردم نیست و متعلق به خدا و پیامبره
مردم  حکومتو انتخاب میکنن فقط و اون حکومته که تصمیم میگیره چطوری نفت استفاده بشه
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/73050" target="_blank">📅 15:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73049">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/520264f117.mp4?token=LB7fYZC_LRKOW1xFrlIdB7B7YrwKsdGRiVtNc8EnbOS0i1r8r3fD-5enNOSaGh7KJt7-DUJcl3VHHfx8Sl3Y-yAeAGg_Jk7ko0IkUqAZW6mqtvNPpSAlm_aFfpx_7ndQZygdKbSfE1quf5GrwoyHFk-PBrKDd-06V-fmjJy1qHenNCeJwO70JtU9GIwb222cBLJ0ykKGGeEtLvB94IGL9fnljRzASdqxGk1nFDvwg-PTeR-65wG7wmqMiJ6N4zwm-9TeQzLx3yFxr0kxlOpWv3CFSXZxaJFWydBHdugEXzJDf7B8miyOPUlZdImOF4VA5F-tOeySnKNYCfmO2L5OZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/520264f117.mp4?token=LB7fYZC_LRKOW1xFrlIdB7B7YrwKsdGRiVtNc8EnbOS0i1r8r3fD-5enNOSaGh7KJt7-DUJcl3VHHfx8Sl3Y-yAeAGg_Jk7ko0IkUqAZW6mqtvNPpSAlm_aFfpx_7ndQZygdKbSfE1quf5GrwoyHFk-PBrKDd-06V-fmjJy1qHenNCeJwO70JtU9GIwb222cBLJ0ykKGGeEtLvB94IGL9fnljRzASdqxGk1nFDvwg-PTeR-65wG7wmqMiJ6N4zwm-9TeQzLx3yFxr0kxlOpWv3CFSXZxaJFWydBHdugEXzJDf7B8miyOPUlZdImOF4VA5F-tOeySnKNYCfmO2L5OZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی وایرال شده از اجرای امیرمحمد، نوجوون ارومیه‌ای داخل برنامه Kaos Show ترکیه:
+ این برنامه، عقب‌افتاده‌هایی که تو فضای مجازی معروف شدن رو دعوت میکنه تا مردم بهشون بخندن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/73049" target="_blank">📅 14:32 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73048">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/983154ebcc.mp4?token=kKBt1fa1Y9xVQkHzbZMsEkSinMKps9Wp0jgoZa9e2p5Jfjcm5hqxuExx_OLKnOahXUbL_gqFXwjZWQ3ToP0BQC4tZyh67DM1uuoRpMeGz05HJi2y8Q0qHhhMMZbypy-HlUYaGGuxQ3HcbVtzMI8-xuAnkBsfWs7pxEYnWhVUfxtxLGQiL-SI6p2X8qafgXczHUBs6hMyUM0VKGU38VIrpKaF-frRgQqL1Cipqi53_wVkdxgt8YrnxG-PbpvifTRt25Mi3Ntr8KBG3oSup1hT1f2vnuCtApJXn5-c-8xr8YzoMY3yR8uvu0r8xpD7eVFe_jhqgbIfWvCjKZgPam4W1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/983154ebcc.mp4?token=kKBt1fa1Y9xVQkHzbZMsEkSinMKps9Wp0jgoZa9e2p5Jfjcm5hqxuExx_OLKnOahXUbL_gqFXwjZWQ3ToP0BQC4tZyh67DM1uuoRpMeGz05HJi2y8Q0qHhhMMZbypy-HlUYaGGuxQ3HcbVtzMI8-xuAnkBsfWs7pxEYnWhVUfxtxLGQiL-SI6p2X8qafgXczHUBs6hMyUM0VKGU38VIrpKaF-frRgQqL1Cipqi53_wVkdxgt8YrnxG-PbpvifTRt25Mi3Ntr8KBG3oSup1hT1f2vnuCtApJXn5-c-8xr8YzoMY3yR8uvu0r8xpD7eVFe_jhqgbIfWvCjKZgPam4W1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن نصرالله، رهبر کتلت شده حزب‌الله لبنان، ۲۷ خرداد ۱۳۸۸:
امروز در ایران چیزی به اسم تمدن پارسی وجود ندارد.
آن‌چه در ایران وجود دارد، دین محمدِ عرب است.
موسس جمهوری اسلامی هم عرب بود و عرب‌زاده. امام خامنه‌ای هم عرب است.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/73048" target="_blank">📅 13:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73046">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/97e3d7ab08.mov?token=htB8IezVQmD54uUQO4yRExCyJRG_CWEBmi3gz3iY76Xl650KveZxdxMz-CBRgNAB2MLpuB69uF7tmtaSv7zd0tvRon5FTmfrZsW8opKCraVg-s25dcKCgasxn24tpS6JpoM4cc2NO4LyzZ0FTbuQCtTM1SlKJtzo51YFIUx8BSEn3EZRjmo4lNU2wmDkNegLWhcPqn3LbmJjNb5U8ffNsL6XMszve_5hoZhgqOmYM6eCtW-YPsagzhbs2bsM8i0HRAruOhYbWA_H2hwf3v9qaojK5ipdMiJiqiEsMbIRAjJeuEhmUhxFhCv3Ufy7vHI8akuZeTqoxYUsuUSW6uMAaA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/97e3d7ab08.mov?token=htB8IezVQmD54uUQO4yRExCyJRG_CWEBmi3gz3iY76Xl650KveZxdxMz-CBRgNAB2MLpuB69uF7tmtaSv7zd0tvRon5FTmfrZsW8opKCraVg-s25dcKCgasxn24tpS6JpoM4cc2NO4LyzZ0FTbuQCtTM1SlKJtzo51YFIUx8BSEn3EZRjmo4lNU2wmDkNegLWhcPqn3LbmJjNb5U8ffNsL6XMszve_5hoZhgqOmYM6eCtW-YPsagzhbs2bsM8i0HRAruOhYbWA_H2hwf3v9qaojK5ipdMiJiqiEsMbIRAjJeuEhmUhxFhCv3Ufy7vHI8akuZeTqoxYUsuUSW6uMAaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب صدای این انفجارها توی شرق تهران شنیده شد که گویا تست پدافند بوده!
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/73046" target="_blank">📅 12:51 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73043">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/351194ef56.mp4?token=nAvLMtfDz5vkC-SEDQmsGOlryl94uJc36ljdaUqYJVR4mAsyAeGwHp9yb6aBCOBI9zzMXozs3mJktdH2r-ung4fqhkHJ5xhSo2b7rLZib0CWWegruY47BrmL8OrDmRA6IaxhmCU242Y6aBp-9tZdU6yyOAL463K0DkH2bNumsuvtbEwiPWwHrUnUDR8QDPLqY_GwV_jbSTMVlp1EeGiTBM8P8XWuqxnPqXnZ4tl3kYCUgNCQh9yBvQ20mVvFkiUEyqu-pSLewrWmdZ6oN5x_asPygAHSZj0vUninQRz6D-ruo0YbIrIMAELGCVairXTvhBqZ-hP6clkTa7xxx1rsvw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/351194ef56.mp4?token=nAvLMtfDz5vkC-SEDQmsGOlryl94uJc36ljdaUqYJVR4mAsyAeGwHp9yb6aBCOBI9zzMXozs3mJktdH2r-ung4fqhkHJ5xhSo2b7rLZib0CWWegruY47BrmL8OrDmRA6IaxhmCU242Y6aBp-9tZdU6yyOAL463K0DkH2bNumsuvtbEwiPWwHrUnUDR8QDPLqY_GwV_jbSTMVlp1EeGiTBM8P8XWuqxnPqXnZ4tl3kYCUgNCQh9yBvQ20mVvFkiUEyqu-pSLewrWmdZ6oN5x_asPygAHSZj0vUninQRz6D-ruo0YbIrIMAELGCVairXTvhBqZ-hP6clkTa7xxx1rsvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیشرو و هیچکس بعد از ۱۰ سال قهر و دعوا، دوباره باهم داداشی شدن و دیشب کنار هم روی استیج رفتن!
نکته جالب ماجرا این بود که سروش هیچکس فریاد «جاوید شاه» سر می‌داد و سالن رو به لرزه درآورده بود!
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/73043" target="_blank">📅 12:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73042">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73042" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/73042" target="_blank">📅 12:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73041">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyTbCyaNjhbNVYwEamvFEia87hJ9t3zm1H5DhOkP3rX0x_4GTsgI4jRnAp8_5XvT6UYBgZVoIKT3O9iSomMrAzI_Zq2s-VaGkA2kfDE-1fN40yNpidWULfCUO_P4uE8kygEjKJEBWjtN39VldMH5_UnZU5tXGkm2vRwpzZ2JvPeH3okCMtNkawKNI4zX7mFjWreHACzAXE8q7A_YHrCD2AuqwA4bzqoXNPaJbOvi_n-Vg9peBDN_F546z5h5Y7PP3394FKt45BIuS1WQfV-60kqJTNsvS3_C4IHQh-yd6Nej1hJHyyDD2wRrwbURHw5vsPjFIUqOzaDpIAM-EDOqXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
لیدز
🆚
آرسنال
بورنموث
🆚
چلسی
تاتنهام
🆚
منچستر یونایتد
ختافه
🆚
بارسلونا
ویارئال
🆚
رئال مادرید
بایرن مونیخ
🆚
آگزبورگ
پارما
🆚
اینتر
فروزینونه
🆚
ناپولی
لومان
🆚
پاریسن‌ژرمن
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/73041" target="_blank">📅 12:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73040">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e742ff38d.mp4?token=BNWCKhiZ6BKI9iDAg2j6Sn9Lm_wlK_u5bKcKrdyxiGGoV25-4MB4Ba_quPSsAQtLUQRarCpKV8rvrP5fH3XCCijKR2awwGE3sggpl1wL0rp75_va4GttccdfGNxCmF5oVokcdpnIfEQ5gGqBoV8kMrwxi5gWetE7lSc3DIxVfT7oeuH-83PY42ECwIB2SnytNUU7HnVCHwE_U4JuuzRKqRBeZ54XU14KZ0913Wsfd7YstLbseSr5E0DS9Xo7VXXwxm3tvJdQqsKYK1R_x7tsXoE18GqS7vIFW3mJ-rzds9qGqmZI56crcRvSYqBrqXQJrpb6xiHyQ9uhT_f1TLEtLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e742ff38d.mp4?token=BNWCKhiZ6BKI9iDAg2j6Sn9Lm_wlK_u5bKcKrdyxiGGoV25-4MB4Ba_quPSsAQtLUQRarCpKV8rvrP5fH3XCCijKR2awwGE3sggpl1wL0rp75_va4GttccdfGNxCmF5oVokcdpnIfEQ5gGqBoV8kMrwxi5gWetE7lSc3DIxVfT7oeuH-83PY42ECwIB2SnytNUU7HnVCHwE_U4JuuzRKqRBeZ54XU14KZ0913Wsfd7YstLbseSr5E0DS9Xo7VXXwxm3tvJdQqsKYK1R_x7tsXoE18GqS7vIFW3mJ-rzds9qGqmZI56crcRvSYqBrqXQJrpb6xiHyQ9uhT_f1TLEtLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میرسلیم:
مرگ مردم در تصادفات رانندگی به علت رانندگی بد آن‌ها است و ارتباطی به کیفیت خودروهای داخلی ندارد.
واردات خودرو خارجی باعث می‌شود کشور پیشرفت نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/73040" target="_blank">📅 11:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73039">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e55bfab16d.mp4?token=hMBulhwOp2fLk4n58ybR8irSKYS95caEcykEmUiqozsb_PZy1dM-IAM-s4f4HKqfflL2uVJtszQi5HLCE1iztdhRlie8TFM8QrL1haVH373FBUpSuupgnWj9Bt6dkCdQZWafv0bp_oqul6Fk3xUhEwjccktp91DGQ_GU66hsiy5iOb6oPLtlEuOq7OvfmB0Z4lg_XG1JassS0H0bRCOLiFMEEOpI9k4ifwAozfrlMtBArAn356mu_cnRgeI17xK8Z6ZUcUmSRjNRdETO9WDld9uwQzXXwjmIj6yJIaqW7SCsx6D7dztWrvAcDqTEhmVq3cdOMPM_sxspMWuCClKlqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e55bfab16d.mp4?token=hMBulhwOp2fLk4n58ybR8irSKYS95caEcykEmUiqozsb_PZy1dM-IAM-s4f4HKqfflL2uVJtszQi5HLCE1iztdhRlie8TFM8QrL1haVH373FBUpSuupgnWj9Bt6dkCdQZWafv0bp_oqul6Fk3xUhEwjccktp91DGQ_GU66hsiy5iOb6oPLtlEuOq7OvfmB0Z4lg_XG1JassS0H0bRCOLiFMEEOpI9k4ifwAozfrlMtBArAn356mu_cnRgeI17xK8Z6ZUcUmSRjNRdETO9WDld9uwQzXXwjmIj6yJIaqW7SCsx6D7dztWrvAcDqTEhmVq3cdOMPM_sxspMWuCClKlqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مایک تایسون، بوکسور افسانه‌ای:
«اگر رئیس‌جمهوری مثل دونالد ترامپ وجود نداشت، به‌هیچ‌وجه امکان نداشت امروز اینجا باشم. متشکرم.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/73039" target="_blank">📅 10:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73038">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d334669b16.mp4?token=X1cGO5Jyq7DPjbr13LjvXyHU9GkQ45FovYYDeTN9ZEdRm5wTQp-GdcKpkJRg1CtyV0PeCZAqc-Gg2ZrrPgo1RLG5nM3zeURgyOoboMBzRyUaubmupr2yVRGe2E3E8Xun2hwqhVDceLscE_OGGazw7mpQlc2X5zsWQFo6EM1yExlMFtUthEcAKdaAXXra-KEusDKnN-dWS6UKxBemXJtyFD_bzGgg8XqF85FYKAzz5Xjdvrx9-RqZeCiS1wqXPM0k1wXkkCzWBE0ZJS40-gctSPy-eBd7dvoA6C9fI43xhQSv9t0o4ywsj1g4SSIs8un34j1rqqdy_aJSjnrZWIVQUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d334669b16.mp4?token=X1cGO5Jyq7DPjbr13LjvXyHU9GkQ45FovYYDeTN9ZEdRm5wTQp-GdcKpkJRg1CtyV0PeCZAqc-Gg2ZrrPgo1RLG5nM3zeURgyOoboMBzRyUaubmupr2yVRGe2E3E8Xun2hwqhVDceLscE_OGGazw7mpQlc2X5zsWQFo6EM1yExlMFtUthEcAKdaAXXra-KEusDKnN-dWS6UKxBemXJtyFD_bzGgg8XqF85FYKAzz5Xjdvrx9-RqZeCiS1wqXPM0k1wXkkCzWBE0ZJS40-gctSPy-eBd7dvoA6C9fI43xhQSv9t0o4ywsj1g4SSIs8un34j1rqqdy_aJSjnrZWIVQUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛ پرزیدنت ترامپ:
«ایران یا همه‌چیز رو به ما می‌ده، یا دیگه وجود نخواهد داشت. خودشون اینو می‌دونن.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/73038" target="_blank">📅 10:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73037">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">میرسلیم:
تیبا با خودروهای خارجی ظرفیت رقابت داره
واردات خودرو باید یک در هزار بشه هموناییم که وارد میشن برای این باشه که ببینیم چطوری ساخته شدن
مجری:
الان چرا کشورای حوزه خلیج فارس همه بنز و ماشینای خارجی سوار میشن ولی ما سمند و تیبا و دنا با این قیمتای بالا سوار بشیم...؟
میرسلیم:
میل و انتخاب خودتونه دیگه
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/73037" target="_blank">📅 10:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73036">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سپاه  تصاویری از حملات پهپادهای «شاهد» و موشک‌های کروز به شناورها در تنگه هرمز منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/73036" target="_blank">📅 09:31 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73034">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ویدئو های وایرال شده از دعوای پشت پارک یه مدرسه دخترونه در تهرانپارس که دو تا اکیپ با دوس پسراشون رفتن داخل پارک بخاطر اینکه یکی از دخترا همزمان با 4 تا دوس پسرِ دوستاش داشته خیانت میکرده به رفیقاش و گرفتن چند نفری زدنش و دوستای دختره هم برای دفاع ازش اومدن!
نکته جالبم اینجاس که چرا دوس پسراشون ایستادن کنار نگاه میکننو نمیرن جلو جداشون کنن و گاهی تشویق هم میکنن که بیشتر بزن هم دیگه رو!
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/73034" target="_blank">📅 09:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73033">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/73033" target="_blank">📅 01:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73032">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pulw1EIX3DxtSwKGHdaSD1MmSy9BiCyWXS54XxtxPQTsiov-dvdJc93brQ6KrOMqkRWGwwZp74aGHXOxxNvi2ZyGnTSrDWdmK7w7t_3Ermp-axn7RC21ae6_F2kiiiV1pflaIJW8jQr7ErXdS5kY0DdOTNgLe4_XYwW3_QiOy7BUobWT4hvp9oXby0s4j2k35_1HzPBHGP6IHaGBYuN9OqlUIr2RYmw1bjSsOEIXP7CXb5LDqcthZnVD2a--jwy76_1wdXiQFBZ698Ekl0SmlWYUmF7bRcZhOdXT6Mf5PQ02zrBsU-gi-nk7Yrp6la2y4WtKUXihk3hoZBrfEW-1oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/73032" target="_blank">📅 01:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73031">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d4fabef22.mp4?token=RPfiBc5YOFdmLwpJJW5f2AKRE9oeytNhcq51XOs5TgxzQ9DbXQgKDBDZCVbp5Z9CtAexMGdmU8ROnvnB19Dq85p2yOUTvHue9KFUd3dDl2GijSDDwcnPeiuswICCWxiEwuLUUcinodfNkAKya24CkGSDEgiOPJjjeY6AbMK_UAvzRYJal0Yh2k-yxlGsORI8EeT_SRQ7Po7gTxIEmKPqcfkFhKft5lMbKHK_v0Wt-cHoqiH23NDnVb1IFlbHigTNmLdGErhRPzEOGO4eq4txMh4O60v7tKZq9QJsTl0rSB-GK3doFPHVwC6Oa4J_sFfkMLaL3odVlPZBSJprvTgJIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d4fabef22.mp4?token=RPfiBc5YOFdmLwpJJW5f2AKRE9oeytNhcq51XOs5TgxzQ9DbXQgKDBDZCVbp5Z9CtAexMGdmU8ROnvnB19Dq85p2yOUTvHue9KFUd3dDl2GijSDDwcnPeiuswICCWxiEwuLUUcinodfNkAKya24CkGSDEgiOPJjjeY6AbMK_UAvzRYJal0Yh2k-yxlGsORI8EeT_SRQ7Po7gTxIEmKPqcfkFhKft5lMbKHK_v0Wt-cHoqiH23NDnVb1IFlbHigTNmLdGErhRPzEOGO4eq4txMh4O60v7tKZq9QJsTl0rSB-GK3doFPHVwC6Oa4J_sFfkMLaL3odVlPZBSJprvTgJIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ما در هیچ زمانی پیش از انتخابات میان‌دوره‌ای آمریکا در ۳ نوامبر به ایران حمله نخواهیم کرد.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/73031" target="_blank">📅 01:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73030">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mS-qxaebT2f1ro-pUizUW8wQN1faX_uNAG5jjwcU6vs-M_VF9o9oo1N0oyME_F8nB-oyLMW-kFy4Rn_J14FzWRiCEanR237eRS6kgXSjUzjIvfwLAop5qg2aBc5GJGCqpbOeZpZHTopPQGWQyqdVs9Xxysy6lr4iYcXf-LMnWEHMJB4B9APlcEtHCP0w0Mk4gJB4wu0J63IctiOUl61TBhLDtxO0ULRlVL92ReXa6AbTzOOloZkB8kxoieX8zEAEAuk8JR4lj4QH4hJTJwdIrzEX2-SKhN68ouW_HPLf_ldaC7QSWlL5uW5J04fFfsJEsQ6MoPdwMo6DXz5ZFzi2Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛
هشدار امنیتیِ وزارت امور خارجه آمریکا:
به شهروندان آمریکایی هشدار می‌دیم که فورا ایران رو ترک کنن و به هیچ عنوان به این کشور سفر نکنن!
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/73030" target="_blank">📅 01:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73029">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">از سیریک چندین پهباد/موشک به سمت شناورها در تنگه هرمز شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/73029" target="_blank">📅 01:05 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73028">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0925073180.mp4?token=jDqyJKuuTggM-oYL0bTnatnRu5ydnXNkkp1fAdVcVdwSRJZnJVSYHx4hAVxTWv0VassKW_H99yphKDTLJusrMo42rbmPa1igQQ9ApK6_ZcgeqCJj_-Mec9WPlSRG02k9owhX5VS1G0lLendLDa0XiOx8gRUkr5hwS-ksWjNxYYoJEl0wuZv3TZgw_lXaAUAEDcd-ppha6F-joQYXB2aw8h8exQWHNaVICC4QGAx_UJn82oLrrQLAP3FhasTAV0uNEj67wv-9d8pWoqqYP3bSwWrDKhPN6qTkA_V4pcEAAQxcJTVGSatB8vEOuTBmaWRWGrkHV06QZ2gEiZpOFgT_mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0925073180.mp4?token=jDqyJKuuTggM-oYL0bTnatnRu5ydnXNkkp1fAdVcVdwSRJZnJVSYHx4hAVxTWv0VassKW_H99yphKDTLJusrMo42rbmPa1igQQ9ApK6_ZcgeqCJj_-Mec9WPlSRG02k9owhX5VS1G0lLendLDa0XiOx8gRUkr5hwS-ksWjNxYYoJEl0wuZv3TZgw_lXaAUAEDcd-ppha6F-joQYXB2aw8h8exQWHNaVICC4QGAx_UJn82oLrrQLAP3FhasTAV0uNEj67wv-9d8pWoqqYP3bSwWrDKhPN6qTkA_V4pcEAAQxcJTVGSatB8vEOuTBmaWRWGrkHV06QZ2gEiZpOFgT_mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: زلنسکی گفته توافق نفتی شما با پوتین نشونه ضعف شماست.
ترامپ: کی اینو گفته؟
خبرنگار: زلنسکی.
ترامپ: باشه!
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/73028" target="_blank">📅 00:52 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73027">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bebfa1213.mp4?token=hBu-gWv-TW9xFk0_ooz16yGLcax41L5hpEiilgsDtCd5TB5mjgQhAbttEdVWk791-wthS6Fz9pMoGjwPIYc487Fk3j8FK0i1GqRqNbjfwJL0OLyvDFXbkQDF7q2byW5UP9SOl0ZUGNnkvtPDy0eQaMaj9DT3RltzGAAhDpUVkv-9WtYv4XptVZPgAaTHFaKRuXJyk7faShP2CkdByP43bsrcV9zCNlN0RtYJ_nRBn_R5_bHsHvRwTuXyTjt0kJ0pVlPj2q1HeVT13_x5UnPw4bZYh0oFe7AhMtPinqFXacAj60pSm9SyJuxhpS88SKiP13VCNqrq4EkqiK4YgMj0g4c9HHsecj_ACK0pPV6s49jRIyH3iyYxUbuKDl3Ah4EoWAmqNfpNaUmJ_BinjE7bZKdEVIfVBP2nPCNFD0F1iB4LgSLXQp4Yjzyo72jv3vbGhGcDhFw90TQddScg6WPIaULJtQVEGZxRVWwEC1NaEJC307BssnHGx8qltiyeqBIia-DW7P6QYsR9k85sYgYvFAzKEN6FPrRHCQVTFE_72y-eE3JSiK_hs3ynA6VpdalVCT4GFsZXfGaFzx1rMA9WqsueTjP12L7uTbp7il2m45bCjENbHSqFMuJ3rqvn8min5hDcGksT9zg2PKfjyod3Y9PRoO-pfIQ5gb0KaWSv9hc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bebfa1213.mp4?token=hBu-gWv-TW9xFk0_ooz16yGLcax41L5hpEiilgsDtCd5TB5mjgQhAbttEdVWk791-wthS6Fz9pMoGjwPIYc487Fk3j8FK0i1GqRqNbjfwJL0OLyvDFXbkQDF7q2byW5UP9SOl0ZUGNnkvtPDy0eQaMaj9DT3RltzGAAhDpUVkv-9WtYv4XptVZPgAaTHFaKRuXJyk7faShP2CkdByP43bsrcV9zCNlN0RtYJ_nRBn_R5_bHsHvRwTuXyTjt0kJ0pVlPj2q1HeVT13_x5UnPw4bZYh0oFe7AhMtPinqFXacAj60pSm9SyJuxhpS88SKiP13VCNqrq4EkqiK4YgMj0g4c9HHsecj_ACK0pPV6s49jRIyH3iyYxUbuKDl3Ah4EoWAmqNfpNaUmJ_BinjE7bZKdEVIfVBP2nPCNFD0F1iB4LgSLXQp4Yjzyo72jv3vbGhGcDhFw90TQddScg6WPIaULJtQVEGZxRVWwEC1NaEJC307BssnHGx8qltiyeqBIia-DW7P6QYsR9k85sYgYvFAzKEN6FPrRHCQVTFE_72y-eE3JSiK_hs3ynA6VpdalVCT4GFsZXfGaFzx1rMA9WqsueTjP12L7uTbp7il2m45bCjENbHSqFMuJ3rqvn8min5hDcGksT9zg2PKfjyod3Y9PRoO-pfIQ5gb0KaWSv9hc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«توافق نفتی با روسیه خیلی مهمه؛ حجم عظیمی نفت وارد کشورمون می‌شه.
راستش رو بخواید، می‌خوام از رئیس‌جمهور پوتین تشکر کنم.
این نفت هم گازوئیله؛ همون چیزی که ما می‌خوایم. پس ازش تشکر می‌کنم.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/73027" target="_blank">📅 00:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73026">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffadaf48ae.mp4?token=nIxmkgD0aB-Wo9hYogcvjziewpF6GS2TWYsFaCWQiRoxbcqwu3GZ9XHzHrDDDf5zK09CH0l5Ss1XeqNNGyxPn2vlAAQb2aD-j-v6Nw2ANfWBMz_qa1YeyIf2SEd4vPONNRrUkZPc3aCXXBGzof6MSvR_z7Hm3GftnnMA87fOwWm9JSdaKB0bED8PGJ2vTj3MhXftZ-TBfmJbfwWT69ljWntIu9U1uli9qNr-3N7_UP5sNJuuyYFMBjC5x_2L5M-rJFWnAA_-4I3TK5DXYUiXc3IfrkHzaiVfqdtYSEvcZkCjdiOOdsJSTb-d7kgq3ikCDyibwSh-t8PlmVBjOe0Lr7KkjL6KeoQR4raSQOfBMDywdcdfI7b9nYhFz2g5Za1UgeYXTV7UO9UZxAfvThuWeZVtgZtm6x0i8DNOolZ_jfgEryoQcHZdKxgz_N8elHv7dNBeVuoTXhYfjFNO77txem6RAsxojjI1JVgbX-KJu76ge_MpgfBos1seGP9fTcTwnXR8U1Kz7Os6PIsoctfHOXk-3hk-rKbWRVvcsr2YH-ngjSxlAoPiLynx5UR-ucnaV4azHlmW4FeVUHI0bmpfCTpGUcZkzW3eJyl9zUL-IJsSeu7DmMZ7qykIifpaU02fseEYcymwf32cxcQgWLx3QJ1OdAm1nKY-t2GH4cxf24w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffadaf48ae.mp4?token=nIxmkgD0aB-Wo9hYogcvjziewpF6GS2TWYsFaCWQiRoxbcqwu3GZ9XHzHrDDDf5zK09CH0l5Ss1XeqNNGyxPn2vlAAQb2aD-j-v6Nw2ANfWBMz_qa1YeyIf2SEd4vPONNRrUkZPc3aCXXBGzof6MSvR_z7Hm3GftnnMA87fOwWm9JSdaKB0bED8PGJ2vTj3MhXftZ-TBfmJbfwWT69ljWntIu9U1uli9qNr-3N7_UP5sNJuuyYFMBjC5x_2L5M-rJFWnAA_-4I3TK5DXYUiXc3IfrkHzaiVfqdtYSEvcZkCjdiOOdsJSTb-d7kgq3ikCDyibwSh-t8PlmVBjOe0Lr7KkjL6KeoQR4raSQOfBMDywdcdfI7b9nYhFz2g5Za1UgeYXTV7UO9UZxAfvThuWeZVtgZtm6x0i8DNOolZ_jfgEryoQcHZdKxgz_N8elHv7dNBeVuoTXhYfjFNO77txem6RAsxojjI1JVgbX-KJu76ge_MpgfBos1seGP9fTcTwnXR8U1Kz7Os6PIsoctfHOXk-3hk-rKbWRVvcsr2YH-ngjSxlAoPiLynx5UR-ucnaV4azHlmW4FeVUHI0bmpfCTpGUcZkzW3eJyl9zUL-IJsSeu7DmMZ7qykIifpaU02fseEYcymwf32cxcQgWLx3QJ1OdAm1nKY-t2GH4cxf24w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در کنار مایک تایسون در کاخ سفید:
«امروز قرار نیست باهاش مبارزه کنم، اما مدت‌هاست که طرفدارشم. مدت‌هاست با هم دوستیم. هیچ‌کس مثل اون نیست.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/73026" target="_blank">📅 00:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73025">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_QwBoEquyxO5EBTunuYekS3kXKuwtI9TGr8EN2mmZizeimv89IDl5xLDCmlBXTmf6oBZaDHM1rfVAp12hWCNt4vig0X-g5zTbq1Ein7vx1LEsH22D8EBQaJqi4uFV72FAlEnazjhExAyBRf1Lfmx7QNHZxUvDoMkBKQUQdknVqzkg9UGFpDF9YhP7cdyLxiN71B6N0TUKFpB-OfLLZ4_LdPUgBjtVvtehWSNoLd4UF2LGfKrumUXYQo4FCj8bNSsCmux0AI9pzt-8yNBcgdMub8AFCtAlucM1tDruHSvkihzLdaZPM9EzOmDfeMDUJam9akVZT3TlFfuCGJiTcrJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛وزارت خزانه‌داری ایالات متحده انجام تراکنش‌های مربوط به فروش، تحویل، تخلیه و واردات سوخت دیزل با منشأ روسیه — از جمله واردات به ایالات متحده — را تا ۷ آوریل ۲۰۲۷ به‌طور موقت مجاز اعلام کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/73025" target="_blank">📅 00:25 · 18 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
