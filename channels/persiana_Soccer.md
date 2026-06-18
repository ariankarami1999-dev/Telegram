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
<img src="https://cdn4.telesco.pe/file/BfD5Scqb9-lcxgvvsVgL11eeyjZEiEPfFq6aJzYmBaHPtRZw8IkbdBZz9nPD2E6Ai4wgxOO7C6nbPu5uL73MravNhUYyR8-Rw7NyEn7V31dxihfY_Zea8qfiut3M9gMFXua-ZExgkVx1eWolWjAipX3N3r5Lg-t0uqYlm47eGpfPzufKhxa7Gmgsrnlhcyualh2tJWW7zH_i9NOwNQKUs96_Cp9lgSCNmQ2xEQMuT-AgfUewVV2bubCeyiJQDHC4b-5r8ExaCt-pVgFivzopkmcxbs8mH5UckaCYnpnMu_WEr-TOaOX_oQBayCGuK5EgqQPEl9JCRKdfcX61HxXpBw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 311K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 14:37:40</div>
<hr>

<div class="tg-post" id="msg-23757">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjqRjP8bhvByhu_5sC16df0m1a6Evy22QYJDyMEWVp38QPliPzRjDShnzYbIVI605GFW-kkGHtmXlP4jTZzdBhBSwOFI8M4w9MXhcQyR-676PM1rS7jPif59Rqvw1KlIAFfHgHfHu6Oz877ihyVJr_vp5q_Mn6A86q_LvRAA4YtzDuCsflQCcx0Gdp1M1w3cgdIDQqDO83dTcCb-5WWIXmn-edGmo2JtieA5tjYSDYTKFgEPhshHrdA7t7HsNYXVZCbWrZTXBdB-jIstz_4QnZboV9jDt2fyIItJZoXsgKTdwBU61fBFfJ57TnVmRoAQegaXZH5Tvu3O9tbxoMSZbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛ باشگاه چلسی آمادگی خود را با فروش انزو فرناندز به باشگاه‌رئال‌مادرید درپایان جام جهانی اعلام کرده: 120 میلیون یورو بدهید انزو رو ببرید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/persiana_Soccer/23757" target="_blank">📅 14:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23756">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xze51gKGFiwnpu9nZ9wCQyJYYAfm2pj7nAeKdt_hbUaasENIfJCCsOZ3v3LTtXLKNWg1a3QxSkeUKhLBqnZ4RYKkfw-A1wlLvOm0tC0rNGpKfYJlhwbs2OJRTEooMpith0B4yAIjp-DE330pl9gj5uWf7wnzPjTUGtGAgVgSrhmsdICsuL6sXCULNesIjJZfxjfUD5oG_TrB5VY7_4Y65yX5BcrBvcc346BCuaqKkj_2E3no6nufawsMItcmPVCTVFltqJbg87NSAg5xiyoTV38lsSfRZl8lBHQemqAi0t4imkit5nox7yFbrJEV4lttTF73B4JuxRK6zbzPrNd4Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل کارتال در گفتگو با TRT SPORT: آماده پذیرفتن هدایت فنرباغچه هستم. مذاکراتی با باشگاه داشته‌ام باید صبر کنیم ببینیم چه پیش خواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/persiana_Soccer/23756" target="_blank">📅 14:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23755">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JApLnfQnSWYdZnBRgt-iV72CD5Ry4e5z7ajhOeORylerm1rtV7NvQfSZcAUE4oVs9uxEoqal9oML9e62xK_uOf_lXa4FRXWDW_FZSLI-KMUEkdCJEqmER92MJzMZfXEEPPD5wImYIWJJtCMjtjBs_FVPW2294rd_ESM4QZUVi_5ZwmkHMmtJszVIcnxFnwIjBEMe-eJIaas77rv3WGYGwhQXHKvJLmowXfJ7RwJNlkjCmlvuchb4jaIUOhgUaaBmiCohAxFlOLWFYYou9vQyyWf7zwLJnxuvN0YdUjHcwU6xBvpvecfELwystZ2fgavv93s81pIk-xSxrOn20TTOsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای‌فسخ قرارداد توافقی با اوسمار ویرا برزیلی به توافق‌برسند سریعا با دراگان اسکوچیچ قراردادی دو ساله امضا خواهند کرد.
‼️
مدیریت تیم استقلال در ابتدا مذاکراتی با دراگان اسکوچیچ داشت اما عزم‌ علی‌تاجرنیا برای اوردن این سرمربی کروات صدرصدی…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/23755" target="_blank">📅 14:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23754">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThzOEO8dWWjAVmJBydYbNcpsuH9GPUJvEn8EkM-i1p_29qb8br_cbeE2joqTk5io6q_Hl09LOYo_ki_4NJS0SxxyE5hxgGRWaBfiky8AG88w1Qlk-pjiMClV3EQxa8IIgMUBfUa23QQpyDohnBCnC8VNV3ojW9dNpQa0LY13kfMqx5j27q0cs6ZzgC8B5JU6F6J0_ie_jmc-Wm6Jebbvvz4IlCvypPm_zNhaeXhVP8osg2MXztgec1gA77VN4GBRXg8G-vKc591xeTkcuG2GMpgCyIayXcuEFDi41280OBXjAETmuUdexFDynXqZb7VceO_xHVZ3Ef2yttZQJ78_4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
جالبه بدونید مثلث خط حمله بایرن مونیخ در فصل گذشته؛ هر سه تاشون عنوان بهترین بازیکن زمین هفته اول رقابت‌ها رو از آن خود کردند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/23754" target="_blank">📅 13:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23753">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQbe38C1b_JLnMcKmDx6bGVByeU-Fm5w3a4R3hHpR9xr9c6zjp8tSUxnAZx9qApPv44FROTZpq4EaGOi4jwAMOrAQIMJDuwKxetmFeVaD89_rZwKlmFVVl0zoyfCU5uWL3tD5ivModp18CdOxRKgs7d4Yl3sfS8CCvYRqzl8yRgMPPR0cilhltGZ03_NqP_FPacd1ObzIKF3dODtlh5Xxu_XEjthCntsFWhnJrL0ToVywSd0AEDIYhqh4sDCqMfL4Umu3JHhfTOtf7RyqvVwDe78Zza03vQOJdOEKnYNBDrSwfzOJ2TtxDyE2WvFgpv8ObmtXkYuNP9bSZLAwDlRtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بانک‌شهر برای دوفصل‌حضور در پرسپولیس آفر 2.2میلیون‌یورویی‌به‌‌دراگان‌ اسکوچیچ داده که مورد قبول سرمربی سابق تیم ملی و باشگاه تراکتور قرار گرفته. حالا تنها مانع راضی کردن اوسمار ویرا برای فسخ قراردادش با سرخپوشان پایتخت است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/persiana_Soccer/23753" target="_blank">📅 13:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23752">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-fKR9yms4t8ob8FxiTj_TXbJXgXR13Z1nIlbXj3_xbIY5H608e3SwrDqSAL2Qd72y2CgAXf6Sy23lTZz7mMwL9ViAvI23MFn0pQbbStFN8-fSxIhhE0M59L6aqD-LW1KIN4uxhlnpQyEmJ-l7CUxU1dT08LdJe8oZn1JX30dRCthZeUB4G2l5HI1dwS5eDLZJmmvbWCSYKMA9JbQONPLoW0bjsHg46Rc61OgeyTJ8IZzaRecTgwKu60L9GToRKCgJ-3n760-oybDUo_xrNc4UXy1-8YL1rq4EjNcADzkwVVr2JE2Hwn3fCNCDIfqgg6oMm5Exk08qGTUSXJJHF2DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
وضعیت عارف آیمن در جدیدترین آپدیت سایت ترانسفر مارکت؛ اعتبار قرار داد فعلی آیمن با باشگاه مالزیایی تاخردادماه سال‌آینده هست. بنظرم می‌ارزه این پنجره جذب‌بشه از فصل بعد ازش استفاده بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/persiana_Soccer/23752" target="_blank">📅 13:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23751">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10541c5fb4.mp4?token=lXJoSYd0R75XDdo6r-u86uSagQGWfKf0hRGm7dpCStV-MMpBFH25PotD_F0kANLHDNpXXTrAyNWAvsAIqgwBQjLucmhgwRvwXIWyxYRnio1ioaN_G59KHV3vLVkLYm3axxEFGnaaK_HPRB-lZDSrKORqiAXaZzkUN0HIDhFIuFyGnZIgDxPrC5gUeL5A7g70xLFYYnNtIYZkZbLRLzWq9BCR-f1WwQpGrnEExL5tx8tSRuIFTg5Zu4-psXCRxOBIzbYJ7ZEg_FPvXz7dFQfESWjGTnGQmW4pLMj7d9jGTFq7kKQfWSJPLGjWYWGtnphpgRDZaqH9FBIRxrgB_OPLMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10541c5fb4.mp4?token=lXJoSYd0R75XDdo6r-u86uSagQGWfKf0hRGm7dpCStV-MMpBFH25PotD_F0kANLHDNpXXTrAyNWAvsAIqgwBQjLucmhgwRvwXIWyxYRnio1ioaN_G59KHV3vLVkLYm3axxEFGnaaK_HPRB-lZDSrKORqiAXaZzkUN0HIDhFIuFyGnZIgDxPrC5gUeL5A7g70xLFYYnNtIYZkZbLRLzWq9BCR-f1WwQpGrnEExL5tx8tSRuIFTg5Zu4-psXCRxOBIzbYJ7ZEg_FPvXz7dFQfESWjGTnGQmW4pLMj7d9jGTFq7kKQfWSJPLGjWYWGtnphpgRDZaqH9FBIRxrgB_OPLMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
جذاب‌ترین‌بخش‌های‌گفتگواخیرامیرحسین قیاسی با مرتضی‌پورعلی‌گنجی‌وپیروزقربانی دو مدافع میانی فعلی و سابق پرسپولیس و استقلال؛ عالیه ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/persiana_Soccer/23751" target="_blank">📅 12:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23749">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J5gswZDb8_H40fpFGWC09U_vANcpA5_tArJX-FZ47Y02TcL_K58PhfANImWIe03E_M7CcB-_8BeTR5tKUMqNWAMum-agbo9_KagLnaD5a55uuRn4YrohwlFSGzxajK_kFdmUTFl4qbCTYp8xe6QBaERtubl_QB7QeIsmFFlPQTitX3yNfFcMxbo7ysNe6RpIElcF9ZLe_N1d-6EaqAF0KR72RyTSV1WJmo7qSBnA21YUg3goVWEHWq57goxFFIOIdGPXWdwCgSM826G93AQWyV0yK2iiXy4TuWI2yHRiQ9Bh_jf6lVQd-S8brCU6lVD9d0ctYRVD2lly7XBKViQILQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ajk-l9Nrkkc5GFAn2Sv_75ope-09mM4SxJ54oNyy8n5jeQ-k6uP4HE7o6VwgZJJohVjbuEySqpIYWY9FB3ouqSYnW_V0ipQrLif5zv2qq4CqlbpwdDtfX_SCOCBgxrvLEhDkqciOQeNmTjMM7cGLcKYQW2LyTk9ZuYh3O44_JjYaoIQem8mq0fLK57EjIX1r9qCKHWao4syEhOIgLRQkQV2Hv-F_xKSNsLmrXJYPdjjJ9sbBdn8d4prBs43nhwaqyfH3BqvoKtXnvxVDJFzlVFvdEZb0Dah0YmK9d0XYNN5z_UH1VBG-JtaHh0vHLg_4-cpEHymR_o026n7OcQ8brw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
📊
مقایسه عملکرد آنتونیو گوردون
🆚
مارکوس رشفورد درفصل‌گذشته رقابت‌ها؛ باشگاه بارسا بالایی رو جذب کرد اما پایینی رو پس داد به منچستر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/23749" target="_blank">📅 12:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23748">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WxFlmoVLukn3FPOfMT141oN6gGWMULnpdaDRiG0QkuRiD9aO8EU9ANEai0dScZ6WQdb9_mUNhjWJQ7oYDEiuojo-uD8X4dzL36LmH4jkLpiIasz2Q65kYa4FQ60ja4s8zjy0k4dxFBnrbiUXoLJksbVLVHFBav8WTeOEa0bjBwH08Yo_GHltBhTiU6pAtyVDcvrm3d0AcIU5ZM-GiOfS4gi5PoIshw5BKJo_THvSVNoOWDw0VCPypUwzDSYXvaFgkzUT27q3MVc6RnZVLAjDkgum2dqqt_HmMFGzMPfis2SR4_2ujYaVz4Xbo4AWXQyJimxz5F899IvxlmRZIRlVAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/persiana_Soccer/23748" target="_blank">📅 12:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23747">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e75ce8522.mp4?token=jPnpF0LEfC3rb2y_30LPtJDUmzpdmmcmSqP5yIrtpiQS7xsJQuzkTsdQChIpl6PNuGZ4R5XF9sCHqyLukTo_jQ78gKXBCOE6wcQcstpMfaOOyhIg8e6o5WT-h5HtVyLjFzY0-b1P7nLHml4Xkbx9pjqhVUx3bkTE3x_f94SMTEN2Kr6A0SECQhmhReUGi4RcVDzxdCWSMHxIfWx38MtvWapGQnWFuxSLsDuqFTt6qiTL69A0QZlUnt0tC0OCmCzReLEje74-Bw5gdGyOix54LFAScg0WnR7fRDyMEEwgKwArToTwqw_TgO9bRa7h8hVBinBjeud7-CoJ68i_gYWXzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e75ce8522.mp4?token=jPnpF0LEfC3rb2y_30LPtJDUmzpdmmcmSqP5yIrtpiQS7xsJQuzkTsdQChIpl6PNuGZ4R5XF9sCHqyLukTo_jQ78gKXBCOE6wcQcstpMfaOOyhIg8e6o5WT-h5HtVyLjFzY0-b1P7nLHml4Xkbx9pjqhVUx3bkTE3x_f94SMTEN2Kr6A0SECQhmhReUGi4RcVDzxdCWSMHxIfWx38MtvWapGQnWFuxSLsDuqFTt6qiTL69A0QZlUnt0tC0OCmCzReLEje74-Bw5gdGyOix54LFAScg0WnR7fRDyMEEwgKwArToTwqw_TgO9bRa7h8hVBinBjeud7-CoJ68i_gYWXzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
رونمایی از تنها سرمربی حال حاضر فوتبال جهان که در چند ساله اخیر تونسته ژاپن رو شکست بده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/23747" target="_blank">📅 12:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23746">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIhWv4Grfy2KLWOGPH33yvLFYDXiUYkL5T7zm2wAgj7EjM8rm_RxlTLbtBdAHBbKDoSz82fmnaufbMWJXIUFznp6HdlWW7bXY_VhjSwduppbNKVdgKduXxagekPXE5AhcnKyP1r_tsBIo1wi6wgLxjpyxSHEV8JDpInV5rvBFZO2W3oqxyzToOddQqqawgtrrWuGHCUojMvIqE8yobHG73iztKGGnXR9_xIILDduJCZmPBfzQEsJ4sladAVzpsadVyHd3TFSxmXeZNoU2woYUPIuweRnVi0tZcKgZV3FR_qzd4biVPjPUtXctzNWiEOJmLCG5gbdQliXpqhyMee2sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مسعود پزشکیان رئیس جمهور بعد از امضای توافق‌نامه با آمریکا: به مردم ایران قول میدهم بزودی وضعیت اقتصادی کشور بهتر شود و قیمت‌طلا،خونه و ماشین روز به روز خواهش یابد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/23746" target="_blank">📅 12:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23745">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgA39_mpZBJhqAsb0rcrTU5Zl5b3hGwHA7XS-q7xiulG0hBTZwEQ4zSsnlXGu05sVjZcXsVW7nEuS5LhslhQaCJZNAWlVJwW5R2etDOfCWXASgZh7O_hwvt3ZqKWPAACAIOGKXTNtPMP3qHgqMyOkKbvSA3MeNKZ2ai_CoisCHL7-UKZzoS1-6yNSKUD33UMpvLT93aZsy21pOLXmfyfuzfEXaYKUNHrDUpl9kxgSK_tNTqmzZ1sJW2j4KYIF1zfZuBpXm-Zgl55gRZeAjqkTL2nyhrvX0fy_yN-vLf7RCu4oDtIEBtFfe672yOXPhCXAwIvw579bP0eXVi9_hu4jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌رده‌بندی12گروه رقابت‌های جام جهانی در پایان هفته نخست؛ از امشب هفته دوم شروع میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/persiana_Soccer/23745" target="_blank">📅 11:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23744">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwCC13xiDJ5ANKx1u98nwYiT2uMZdiTuI0qL2n6f0GQIyDP29iOJCUTWUPnr7ICQcDhLqKtVOexW-1dygKO1bHhV8RoMXsqGQ8OwaSiaoatQBwnA7V_OYUmF0fhijdnmBy3WDjMWs0gqyh7yQpQ58ckgwF1QJ_gy_Wu0sPIz1Y8dXfrxpz4shPU5JNOPoen1tkHqf7qqhltJLHqDTh0SR_i23zNzAQ3gTRuhPy617ShVr2_WuFFrO1Y6MXcFjkUKFvEQ48TVpfuZN3J3AUZRf2CD35xeo-S4ACSHU9xdl0iGgnoaZIHUPhnDJ-hzfndiuTBVjr3S5wRl3nRQOZf-aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال با نیما اندرز مدافع راست 20 ساله لگانس واردمذاکره‌شده تا درصورت توافق نهایی قراردادی پنج ساله با این بازیکن آینده دار امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/23744" target="_blank">📅 11:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23743">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">▶️
قسمت‌‌‌هفتم‌ویژه‌برنامه‌‌فان‌‌جدید ابوطالب حسینی برای رقابت‌های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/persiana_Soccer/23743" target="_blank">📅 11:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23742">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9f495fa66.mp4?token=t7i1VclZ8sRLWRR_p301YNCDeomqasEFGCJhH95W1WH7iGTvguW6sPZo4cyh3Ef8b5PPsPXMhiAjFvUkyRQnLy8wPgyQij8WzoAvu1dW9sd7RTlo2W4UMjWVO6QvvDzwc_Fmqby3TGHPLX9eiGvNWVGo6qs-27fFnTSQOA-CGavHhkiU5mw-iShhtavzocYdXD2LKUZC9ROmIffFPAvC-tryVwV2Ue4Nr3kbkFkoa2pAFTduj3tMJ046ZK1XUlRQbsWvXpQCsGa2l5l1v4P2vINa9A5maKMyw4Qjyjqy3Q1YQfJ1ejq2Joi2HFQ4zcZe0KEBO4LziDthcD2D2u4N-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9f495fa66.mp4?token=t7i1VclZ8sRLWRR_p301YNCDeomqasEFGCJhH95W1WH7iGTvguW6sPZo4cyh3Ef8b5PPsPXMhiAjFvUkyRQnLy8wPgyQij8WzoAvu1dW9sd7RTlo2W4UMjWVO6QvvDzwc_Fmqby3TGHPLX9eiGvNWVGo6qs-27fFnTSQOA-CGavHhkiU5mw-iShhtavzocYdXD2LKUZC9ROmIffFPAvC-tryVwV2Ue4Nr3kbkFkoa2pAFTduj3tMJ046ZK1XUlRQbsWvXpQCsGa2l5l1v4P2vINa9A5maKMyw4Qjyjqy3Q1YQfJ1ejq2Joi2HFQ4zcZe0KEBO4LziDthcD2D2u4N-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
واکنش‌لیونل‌اسکالونی سرمربی تیم‌ملی آرژانتین به‌سوپرگل لیونل مسی در بازی مقابل الجزایری‌ها!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/23742" target="_blank">📅 10:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23741">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhMA3oGzf_fABv_x2unfpq3W_IEan2mbPd8VI_HUrMtUJOWDl9DqFHB4r8ypPRIBDV-Xl5mUNzXGTLloY51trAXk3TW-LIAUmtocfj0N5kLXGseMPXKYdB9xBBj1UHvADBfpA1_rge6k9zqeNTTAtNDvnqGJhvFUV57u4z0_T-Z1PI-mtkD-uN6mQLgo-y0UyXhtExVURCQ5ePErYBfz07ChKCnGy0Zdxm7wwfrCsac7W79UCRX0OvPOWQjKGen_RiUSSo2Yc0pRQaKD26b8JCg7nbRYtraR0sY4xCEx1icdfhwjO67kdnhN1rgIY28GG0FO6v0JhjE-m7pYtGqHTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی رسانه‌پرشیانا؛ فرهاد مجیدی سرمربی سابق استقلال پیشنهادی دو ساله از الغرافه قطر دریافت کرده و در حال برسی این آفره. احتمال اینکه گابریل پین به کادرش اضافه شود نیز زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/23741" target="_blank">📅 10:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23740">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-7iQzAvLC9FaONHj8uMzlNzCXJHI3z0D6LGqFe5x0OqXpV48C5ZA6pt9cop9QnMoOwjKphQ2P_Y1K_78RbcpE67PY9Rc5uyDkxA_6xGtk-KYv7_L_S6wIz1gLvRIaZ9w1W5uao0M3UJDlEw_0AxK11cc9SFf7ox1rZWscpaJJu0_0v7k_o6lB1MrkM1WQrspDtrhd9BMiw9BH22zyQfVqqRYO8FpCsJ5gCmnqujaUr_gA4TUI7j6xiZT_I9y1XNnvRR1mzkbxrXVUHDst5zhw9dLq5Fu7FHF4weQGvCM2RtmGA-Yy2D-NTHzClR4s7f2pzN6zfsytbPdppBYVc9Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لئو مسی در پنج بازی آخر خود در جام جهانی
🇦🇺
استرالیا؛ گل + جایزه بهترین بازیکن بازی.
🇱🇺
هلند؛ گل و پاس گل+جایزه بهترین بازیکن بازی.
🇭🇷
کرواسی؛ گل و پاس گل + جایزه بهترین بازیکن.
🇫🇷
فرانسه؛دوگل+قهرمانی+جایزه‌بهترین بازیکن‌جام
🇩🇿
الجزایر؛ هتتریک + جایزه بهترین…</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/23740" target="_blank">📅 10:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23739">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ca0nFq37Tzl7X9b3vjQ2nJp-dYMgKarOriHF-pQd9Qpdpe6qeaOBEXs1RnQL7vwTz3xyM4T61PtU8151wG4xocTPOnqsEMuz5CRDe2nnHtqFhKtRc17TDM3H5ZbzPi3BYujjVbw3Wd1Twygrmg3J8m8ausAISooKgMZ2pQBriHIWS2fxuSAXJQ2ImbzEIL8d2u0tCf8IcVBOSZT-ygjJOnaNJZvT4Q6UEFUj_tIwbMql29RhuQrbt0LcciS9fvNdCW4nolhBEVb8wfd8CdlOZiNOfUJj5e33HQjsGuLytuiUMnYIRGH5fQ8Y_jbfdOE-ktaZUHP6M0U74iCs3EyFbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
دیدار فوووق جذااااب
سوئیس
و
بوسنی
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه‌ای، مطمئن و درکلاس جهانی پیشبینی کنید!
برای ورود بسایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/23739" target="_blank">📅 10:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23738">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adMqRszGFEbWiRZQE10kcdY5VFkYRXvY8cPfv0TKjNW67Ao2MnClSWyhaAIZlkb6HA7qHLSrdqrd1oY4BN5FkIrOaJqNWFUYfOCyF--5Bu1kyoHO-Xlf56XR60KSBNHMwyYKEhTACpi_Cu7A5XXjT1ddVu8VwbCOBSR1y_A5Jp6a4LsEv_9bjRTA8Kqc8eqfrr-GBxRP0Ya9xqYda4Xd4k0WS48q-31R9Subt5QYzg3QknordDOvaz9FDk7kmuSQBTNtKZUzZA1LwbN5EWipC_KBo0W5lVyOINcQJKZh6HslzVICWJIVTevinPpKWW-gPUSjmLkld8yg0yVS0Ap1Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛مدیران‌بانک‌شهربرای‌عقدقرارداد دو ساله باایجنت‌اسکوچیچ‌به‌توافق‌اولیه‌رسیده‌اند و درصورتی که هرچه زودتر با اوسمار ویرا فسخ کنند اسکوچیچ برای انجام مذاکرات نهایی به ایران خواهد امد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/23738" target="_blank">📅 09:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23737">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc17874c.mp4?token=Ci6-FrGtU-PXgpWOWzJ4eXbxpjq6lvCGjD18N-Tlc5kUtrskjpEMl-Te7Kazq6suVZrsO84XTtAPv-DzUsYZMGRCvCjxlNzCVWKRiTj07wZ-IWd-HYhFmVWm1kFb7AXB2UuCAbAMKBAIqr-_jo0xIKLe6cFzNpu9gamm3GWptlMHXzeAxsmgah7jnEWImy1DSwv5-VYQFY3kNKk9bqANk9rDs8nprA4mgJcoEK7MPne9rs5JiUrL4Mxogi91ayZExJxNWTQ_Ps84qgYac6MRz3fpgAotgZxPx8Pjd_iZizuxVKk4kFKDPoYPE1TBivLVW3zsIi-DhiE56EwKOSvh2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc17874c.mp4?token=Ci6-FrGtU-PXgpWOWzJ4eXbxpjq6lvCGjD18N-Tlc5kUtrskjpEMl-Te7Kazq6suVZrsO84XTtAPv-DzUsYZMGRCvCjxlNzCVWKRiTj07wZ-IWd-HYhFmVWm1kFb7AXB2UuCAbAMKBAIqr-_jo0xIKLe6cFzNpu9gamm3GWptlMHXzeAxsmgah7jnEWImy1DSwv5-VYQFY3kNKk9bqANk9rDs8nprA4mgJcoEK7MPne9rs5JiUrL4Mxogi91ayZExJxNWTQ_Ps84qgYac6MRz3fpgAotgZxPx8Pjd_iZizuxVKk4kFKDPoYPE1TBivLVW3zsIi-DhiE56EwKOSvh2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌داغ‌وسنگین پیروز قربانی سرمربی فجر سپاسی خطاب به حسین میثاقی مجری صداسیما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/23737" target="_blank">📅 09:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23736">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6e6215526.mp4?token=O8d38wAJyqAhRWlaBzh2wE47ltrShuYHTL24kiGg-AJAq3w__vlBf-bwns6y08wFW5vTWPY7vTwkIt1mlCYS6-wipjHGBtK5g37BaV-ONVCWgZREXsN3GLYRfXfqlB7xhtjMDV7fXc3ow-2mmZk3tm3shcyrA19kfXlLdAI7A0zEnhvzoMzCLQx7YgpieYnBg4s54pwl4GVE0AFaPDlaxvjwkERGr7aWGMkD6r7V76yE61PFcxyEi6YNA8PkqsaUaosic6Pkn-lmqDI8TFGWbVkqHrDLexeh7FGc3cVZgX0nol76s_zd_2w6tb7UqlzzCEZod8Bei9m08HXUantVnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6e6215526.mp4?token=O8d38wAJyqAhRWlaBzh2wE47ltrShuYHTL24kiGg-AJAq3w__vlBf-bwns6y08wFW5vTWPY7vTwkIt1mlCYS6-wipjHGBtK5g37BaV-ONVCWgZREXsN3GLYRfXfqlB7xhtjMDV7fXc3ow-2mmZk3tm3shcyrA19kfXlLdAI7A0zEnhvzoMzCLQx7YgpieYnBg4s54pwl4GVE0AFaPDlaxvjwkERGr7aWGMkD6r7V76yE61PFcxyEi6YNA8PkqsaUaosic6Pkn-lmqDI8TFGWbVkqHrDLexeh7FGc3cVZgX0nol76s_zd_2w6tb7UqlzzCEZod8Bei9m08HXUantVnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دکتر انوشه باتریلی‌از روی ابوطالب رد شد؛
تو عمرش اینقدرسنگین‌دیس‌نشده‌بود. عالی بود ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/23736" target="_blank">📅 09:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23735">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7467784054.mp4?token=Rar9Hi6thFV0-I85gf0r4tvwgBU1GlSXO1HhvTCX-6_6Dah888Zp_FitnioCMuHyURNT6TJuThhE2E3tJ4-4CdqIa4tkxoaY6ns6fPcqtu7g-YPCJ8Z6-s0Ux7xxTlCQQlynvlCD3WzVfiWX7pxtNy9wuKC_ieL3v_YLFbktT7LN4g4TTFZ8VIbc0Aq1mcaOXRKKl2V8_VTTXHIAZsSlblaEZs1rKbKoEY-d3L3QHLy4l__mgjqVfUfnZWNBMP2GiLH6e9nqKzMAsUSb2G_ucKISikbaTYP86rUECa8eHVzmlqmf2uQiC0s0ssjED-IuELQO9lum1hZtHkP5JjIT9bB4PBq_CeuTabhfqRdopxUJPdVJjJfFTeOa6WmdXnWvM9DU9FlRhh0GcUDz0VNYE8rzlbgq94q6tb8awq6dUfbNkRbRmXKL6fL31tTcM6eFJV0IgBVTKIMpMZjpiFj-cazmiu0IhLWZjidjwuAGVsdxK3nP63P23lVCHZPpMEXL_ynyioUpYLXU_Z9UBy639nMIeIK7OC3fBrHOE7ymfLzygxwEvUF5FXC1nzow_BFXm2YANwLB-1-w5KXIklljdGhNcLcw7p8ydlhmrxP2VYk5YRrEz09uQyi0quUcp_wsEt8Z4LRHOq2GP67VBsX4YWN-br3wxVEU6ouf3irQNwk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7467784054.mp4?token=Rar9Hi6thFV0-I85gf0r4tvwgBU1GlSXO1HhvTCX-6_6Dah888Zp_FitnioCMuHyURNT6TJuThhE2E3tJ4-4CdqIa4tkxoaY6ns6fPcqtu7g-YPCJ8Z6-s0Ux7xxTlCQQlynvlCD3WzVfiWX7pxtNy9wuKC_ieL3v_YLFbktT7LN4g4TTFZ8VIbc0Aq1mcaOXRKKl2V8_VTTXHIAZsSlblaEZs1rKbKoEY-d3L3QHLy4l__mgjqVfUfnZWNBMP2GiLH6e9nqKzMAsUSb2G_ucKISikbaTYP86rUECa8eHVzmlqmf2uQiC0s0ssjED-IuELQO9lum1hZtHkP5JjIT9bB4PBq_CeuTabhfqRdopxUJPdVJjJfFTeOa6WmdXnWvM9DU9FlRhh0GcUDz0VNYE8rzlbgq94q6tb8awq6dUfbNkRbRmXKL6fL31tTcM6eFJV0IgBVTKIMpMZjpiFj-cazmiu0IhLWZjidjwuAGVsdxK3nP63P23lVCHZPpMEXL_ynyioUpYLXU_Z9UBy639nMIeIK7OC3fBrHOE7ymfLzygxwEvUF5FXC1nzow_BFXm2YANwLB-1-w5KXIklljdGhNcLcw7p8ydlhmrxP2VYk5YRrEz09uQyi0quUcp_wsEt8Z4LRHOq2GP67VBsX4YWN-br3wxVEU6ouf3irQNwk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
10 گل‌برتر هفته‌اول‌رقابت‌های‌جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/23735" target="_blank">📅 09:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23734">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام چهانی؛ پیروزی لحظه آخری شاگردان کارلوس کی روش با طعم کلین شیت و شکست شاگردان کاناوارو مقابل یاران خامس رودیگر و رفقا در کلمبیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/23734" target="_blank">📅 09:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23733">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8XhYfdKzyI0EpXhoy74ksE4GUjjIv5hc9VfyRNncp9dT0KUw4qsi19k-OsVMFX1w_GBmwpE6YZL3YqJPrE2BqntsvK_v0TVi0yoKsmX2t8wnETo0jWAcxg7dHHoGsXr7ZkAD1INyWEr-tPEip-Kjs6eQ3LMsun1YgtceR3pVT2RYPlmEBuleFJctKLihs07LJr_DaWlSxJ7-IS-hH2RV8yC86mBa44309NOaUn3y3fIjQ3G8CXvEeBWZRSZd8d-20i429UWiqxWETL8IcWywa5Sx6YDUaJZIXu0Exw7pb8mzYwuvgv8Z-YfCU7GoJHBC_6E601J-_8Yp8WtX3tQ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام چهانی؛ پیروزی لحظه آخری شاگردان کارلوس کی روش با طعم کلین شیت و شکست شاگردان کاناوارو مقابل یاران خامس رودیگر و رفقا در کلمبیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/23733" target="_blank">📅 08:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23732">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOAqdNHMJrp97NOkPD6MqfHtdU_Unx3esDEJjF2JVGt_65h6xruhY76Z4bSUfzMYSruvL610oJjM9DMRA1AEPRzM4DE37V7gy05aQglu14m8LachlVPf31QdH6j4mw7nZC4Kwpdo7O4lt3sB1olGRPKPsAl5VRqHI93jrRggB3ZHg4IOP7TbxgauCUTmunAiHxGERyVHruNP4_yDArEwSxVMePgBdfEWQmJBMHjir8vRVNUeyJTd2ZtwYDnVEdLM_zJPWa5otv1QPJ1AReiLUXaH7Ye8m6o-VxHPKXmg3rcPVq0j9Qr-4dTr8nwUdRrqeADcFZ2AAg0Ix_AZI010nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام چهانی؛ پیروزی لحظه آخری شاگردان کارلوس کی روش با طعم کلین شیت و شکست شاگردان کاناوارو مقابل یاران خامس رودیگر و رفقا در کلمبیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/23732" target="_blank">📅 08:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23730">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I_91c3oA8NFS9l8YbHC7_2pTJd7ok1AX8wJGfZlUIsRKM8tC6V9Cp3w4Jv6uVikQCZexuQUaLHwDDSPWRrDVqKSSwhIp894myEkj7hUF2t1JDJquse7xxU1SYMXLpM78-BbaEDLhJ7YPXB45CVo1sv4ad79dTnBEmx74k1nxS63X27bhb1obOatUoaDFzYjNVhBgq3bF2MS_UoUY8HeCDbrLHdUDZ4K-d5Jw00E6jZhRjPjw8ydjnd8UmvJur18SVX_EbeH-epy0h5KSgVMWxDRySaLYGvkR0ag_KqqGw548Gg0HZLUH3tRwOH3J7P-tEEjZtvRYOgn8-1o9yTFdNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o87eorJd4T_vOE0F-3GUSV808cdwEnIQbZPnWyg63wn153Srt7ti2fGD6JlojcxhK5UHzquXFCaT5WSsyPUR2R-UiiOAS-FyiIwRNKaQwi4yjRFPSQYYhaFM3Lx09t4Gnlxk31qaBM3EtXBaMPKAxcLm3n9dJDa6IXc_8XhbnXCWNZJSQiQWsgUCUt589TeT5PqQob1jIVhwivGl62mWyKflWJT8WTN1lGV3j_6I2RIjFutJUT-rknwtu4BIGFYw3XUc7625qi1vTM2oDaijaUhE4an18jJ3h8x-UfHtPdLoh_KXWwGgmyBScMTKqq8BdVVk3oiEUBYI_EtvhlGz4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ ازمصاف شاگردان کارلوس کی‌روش با پاناما تاجدال یاران خامس برابر ازبکستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/23730" target="_blank">📅 08:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23727">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F57_vOiFuejxY854qtGdQARNUgXSWysQHrSkJTeyXf88cmwstN5CKUJRS9cIoKtF9aaQagJkQXKgIPswF1u6oddZ6QL2Ue9kCbr9Yj-ZwD87MF5E6CwrRLzMX0iBye8vfNPWxXRO9C286QgSq970By2OQtH5q3UCrdPTEqx_d5VJfp7_IMPTKZCSY6ugj0IxlrWlkb_8zqgK7h7FlLBXqIt4J7opNSo1tqhHRFoZI6Tct8ztuTgECke13n_48B5bg7s-Csz1VzTLFPhHKCE1w05UnTxi2keNfa1nK8JOjnIR2fpRiwgO1W8FfPgfFniMhYRHYZ9fud1zQjS4sxFalg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛ نشریه مارکا: باشگاه رئال مادرید بزودی برای جذب انرو فرناندز به باشگاه چلسی آفر میفرسته. مورینیو برای پست هافبک اولویت اصلی‌ اش رو گذاشته برای ستاره آرژانتینی چلسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/23727" target="_blank">📅 02:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23726">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMUJHqfJMJBbKWvQPmB1XPy6R1HMhxfZoW0ORRWjdBZ4HnbzkdiY4Qb6mzNYgO61SWfDCW7X_ZNBu_mMqTAXKo7HH2p-KZv4O6MWmO0siYUQptAY74YE9RqKEYakmewpEV7X7HDXdzMRxLuqlRj7TcEQ-V9m_MjzYvLVe3fqvzSimeqJ1BhM6q1rLvS5k_wAiw653BItb4Uny84MYc1yVUBCjjWfwGGH6auV4xLEsSESvJ_vhqU6WbA9Q2WIWOZktv82Ls3rbuR7nwLNyGrGNANpQnOSho-RmK55zHkDLA98fgEmv4ymxNzHy0FIldzhQSN0UorAQ8tiptmE1seKGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#تکمیلی؛ محمد دانشگر به مدیریت باشگاه استقلال قول داده بزودی 18 میلیارد رو به حساب باشگاه واریزکنه و کار به‌شکایت و دادگاه نمیکشه.  قضیه از این‌قراره‌ویلایی‌که دانشگر خواسته بخره یه مبلغی روکم داشته که‌تکمیل‌بشه به مدیریت استقلال میگه کمکم کنید این رو بخرم…</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/23726" target="_blank">📅 02:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23724">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VsqLT4Wx1XdzE88i116rSWM-OZZ82wOxJIuHMPSSEnn1bKEs7kgsD3pxw1QaVOAN2eeSuZEW9GVsz9Gjmh_kFeB2hn4slVjFEkQhcgQtUnIN5N3ZLHbWvvByhTKnYN62f8ZnrspTEFunvwS0L6a2kUMMm6K7i36fAOIuevbm-WynwGRvznJI_M2jUkioKkI9xmumL63-Qz6vAC9PVy9puKHa6BFDbMIuzh3o8fJoPSOU5ZppU1TxhVqu5SFr-bawCWJmCZhayNhlDz0ZYuLXQmC740Yx-m9J9XWO6oc6Oswz-Z7s1_8j6CEPQwWd2IBHOzq5OKp6WZlXp7Ll4WdPqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
ازمصاف شاگردان کارلوس کی‌روش با پاناما تاجدال یاران خامس برابر ازبکستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/23724" target="_blank">📅 02:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23723">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/heBlrajXX2YG_pgtNPpwA24JHToLUb0mBpyMDXHyu_9bNOdqCMgKbVub0i2e56FjuBjNxGhKT-lfpGZZ2shDgapuMB-6KlD5rchHpQKPWcd-AqTK-Vm6ozgbz3pBR2wxJPU23fBef-PB-wQvPL5QSE1X-pyfPNadb_sfEcaaAI89tFZM1RoX-EwoFCvbtbVgE8Bojs5qGnpcd8L_SgftprkNLpryEuQNQGJityqa4H7f-7o4ovJ0H6Xs8wNHfBscfm5ldEbFwGaB8RqKcIRTQ10wwkDT-fGLRgkTDvDdHr1Cm4OJq8SIwmtPcdjzlHQuEnqIN6tznvLHhZXNKoJLdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌‌دیروز؛
از هتریک فوق‌العاده مسی درگام اول تانمایش‌درخشان‌سه‌شیرها مقابل کرواسی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/23723" target="_blank">📅 02:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23722">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b735dd21e2.mp4?token=P1pHkIyicjNbWaC5sv0JSs1_V_PRxwuP7CD4_fXMSf2GkWIdHeQv4FCAGCTcmPPVmZ-dKBXLAsKaKTis_Gtp6BKH-t00hRBEzlzYpeo0g8ss84TxNWS9p_wA305VxM5jBjEcDJbvGNH1FYsTCkC2yZYLkV8auHMUq0mGJjUn5AajxdxhMRTwSDxIGJ5O9EdVWmiNODnpodCWYi1ucQfGs-FndBb6KAjSODyHptR1OqzFuowLUbAHHuDFOtTnOalEZpwcs24cw86c5LFYTXkVPJaqP5ck8s6LdjZb1TpKiyqTDhoD1eOFP99MC--CVmr65dG6DMQJtnCdgfLImfRBSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b735dd21e2.mp4?token=P1pHkIyicjNbWaC5sv0JSs1_V_PRxwuP7CD4_fXMSf2GkWIdHeQv4FCAGCTcmPPVmZ-dKBXLAsKaKTis_Gtp6BKH-t00hRBEzlzYpeo0g8ss84TxNWS9p_wA305VxM5jBjEcDJbvGNH1FYsTCkC2yZYLkV8auHMUq0mGJjUn5AajxdxhMRTwSDxIGJ5O9EdVWmiNODnpodCWYi1ucQfGs-FndBb6KAjSODyHptR1OqzFuowLUbAHHuDFOtTnOalEZpwcs24cw86c5LFYTXkVPJaqP5ck8s6LdjZb1TpKiyqTDhoD1eOFP99MC--CVmr65dG6DMQJtnCdgfLImfRBSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیروزکریمی‌پیشکسوت‌فوتبال:
بیرانوند درتاریخ بی‌نظیر است ولی لطف کند کمی تنگ تر از این باشد. این چیزی که ما دیدیم خیلی هم تنگ نبود واقعا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/23722" target="_blank">📅 01:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23721">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e924ecdff.mp4?token=bmC6X15iPRQ5g11czCEo09g-AZ9OeslPi0BbghSJ0OzNFt_GxEv8U4lSVYOa2dyC_0g4_UoNiYSKvWONTOT-EKv1tuVq1aAkOauk7Ou81lpC5iq3xp59rO6qPdnG1DsU1G364m9_I-pcI1r1btXLIO4BN_ofvG8kMeRz4i2cETh19dZn-65QX7HVDw8sGLVbJRYs1twyT78PveX5tJUWPzGROYJwJy59JNe1dCBJsCm7ZT2xan7e6Dz2rS2qAc1RaP3ruof-cxi-zKXTf3hkI7fr2xT5R0LjLKmZf1dita6NnVWmJvhRx7mO-PTwYOWictm_Do_pYg-mVhYinwE6qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e924ecdff.mp4?token=bmC6X15iPRQ5g11czCEo09g-AZ9OeslPi0BbghSJ0OzNFt_GxEv8U4lSVYOa2dyC_0g4_UoNiYSKvWONTOT-EKv1tuVq1aAkOauk7Ou81lpC5iq3xp59rO6qPdnG1DsU1G364m9_I-pcI1r1btXLIO4BN_ofvG8kMeRz4i2cETh19dZn-65QX7HVDw8sGLVbJRYs1twyT78PveX5tJUWPzGROYJwJy59JNe1dCBJsCm7ZT2xan7e6Dz2rS2qAc1RaP3ruof-cxi-zKXTf3hkI7fr2xT5R0LjLKmZf1dita6NnVWmJvhRx7mO-PTwYOWictm_Do_pYg-mVhYinwE6qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی‌درگفتگو بادکتر انوشه در برنامه امشب: باورتون نمیشه ولی من دوست دختر ندارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/23721" target="_blank">📅 01:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23720">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLacYe9USnsabjs_cxiVocP1ZjNUTDF7WQJERm7zCs7evWkwYMFv01lkQWEBq3tPvJ8QkrT_TZMg3KxFtCJ12HnekOmaGWs6k0iC5R1I_qJg0fFE-28CF-KlAwchPkoddsSP5T33W6VYd5Ic6i7UN35bUeb8vmLbCP4ST0q5aTg6vpFN_GdgnwHGGUQXEDMr75AiL7kT-TwwIRvAFqBy8GJaLJ9reRYYE_5DTybyFHquXP1FjmVGLEXm-dE-YhpQvpWP6YdvVGKSWRO6kvxOWCF40N-dC3HiD1gfp-a1sMOAzCvKix78wT-iGidZhlq0oDkU-1W50a49YVbp1C8ksA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
میخوای از مسابقات جام جهانی پول دربیاری
؟
✅
کانال
ورسوس بت
کارش تحلیل و پیش بینی مسابقات جام جهانی به صورت حرفه ای
🍑
⚠️
توم‌میتونی‌از پیش بینی جام جهانی خیلی راحت پول دربیاری فقط کافیه با کانال ورسوس بت همراه شی
📣
🌐
ادرس عضویت کانالشون ea27:
👇
🔪
https://t.me/+vEPd1hF2Y38yMWI0
🔪
https://t.me/+vEPd1hF2Y38yMWI0</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/23720" target="_blank">📅 01:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23719">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/210b9e3441.mp4?token=GjbqG5rJZnUbIlHDG4tTmPzZOSEd-M9rkVT_P3NAACLoc-FLcpxyeg4aF-K1HTd4Y7u00SMIaN9HBDuoGrLQrerjnIvQNzXvaJLBChun6s7jKx9Yf0G7FZLXHEBEVWYzueh1BWe9UNkyXABUaKBq1ohnRefCqSW6x2aztpvIp1ceV8rBPOGGWtc2wuTlN-RP8mL4GamkqEkRM9PJQCpoWxFrEZfecIzfAJaUvkzIvg7MlZsBqK8m3RPt-U0KnRyfWzlUv24LgCpWOjpL75zFHo-aavlSbx8wpSd-KRPcXrl1s9Eh0RbOuH85E2U5JAowsAbRByXOwmCA4vJnax1rZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/210b9e3441.mp4?token=GjbqG5rJZnUbIlHDG4tTmPzZOSEd-M9rkVT_P3NAACLoc-FLcpxyeg4aF-K1HTd4Y7u00SMIaN9HBDuoGrLQrerjnIvQNzXvaJLBChun6s7jKx9Yf0G7FZLXHEBEVWYzueh1BWe9UNkyXABUaKBq1ohnRefCqSW6x2aztpvIp1ceV8rBPOGGWtc2wuTlN-RP8mL4GamkqEkRM9PJQCpoWxFrEZfecIzfAJaUvkzIvg7MlZsBqK8m3RPt-U0KnRyfWzlUv24LgCpWOjpL75zFHo-aavlSbx8wpSd-KRPcXrl1s9Eh0RbOuH85E2U5JAowsAbRByXOwmCA4vJnax1rZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
علی فتح‌الله‌زاده یا تام کروز در نقش ایتن هانت؟ وقتی علی فتح الله زاده در زمان سربازی فرمان آتش به جنگنده میگ 21 صادر کرد؛ فقط نگاه های پیمان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/23719" target="_blank">📅 01:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23718">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">⚽️
هفته‌اول جام جهانی 2026؛ پیروزی ارزشمند و شیرین‌شاگردان توخل مقابل کروات‌ها درگام نخست.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
4️⃣
-
2️⃣
کرواسی
🇭🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/23718" target="_blank">📅 01:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23717">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZLTiLWSVHXtXdqrK636iyg1vLxIKX_Bdr0UlKZRlvk-xzq251hYSCe4YAaeJjjLyB9T3-3krce8O-GESEpzK7LE-PVOZ-f5CENlqQExTf-uLGMirn1igzMtXbPU3wUBBC_4sm6tI4XxhNq5Z3X3sjpWNWxe3e8V-Go-tSddNP-3R2Ss4586wCW9xO725-hKjjY_9VeYNKADd1jjhEkMfwyFuiF9zFYcEQs9v9ColMBLwNHxyNpoi1HK-_pCuGS2Ij_xiYkN_iYyBweD5tNja53wX_rvEspi7rTS6CxJS_sfvFc4zxf7stLMeDbzAWDvCZfxd6ANxqfywKEXYN1odg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هواداران‌تیم‌انگلیس پیش از شروع بازی امشب؛ برای ترامپ شعر ساختن، فیفا هم اعلام کرده هرکی شعرو بخونه از استادیوم میندازیمش بیرون.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/23717" target="_blank">📅 01:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23716">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d2128a8f9.mp4?token=J4NFQYvbLuNqTlkVJIsGTLu_wuSEXITS260phPuuCb4MsscJObWcS8SW3IWfGATqyXUigb4kLUQWs3ql_9cC4Gxhu3S2TV3IojKzeYw4YPaXaopm63ejYk3Fu23aAssU047-i2B04VFd49lclr44yzFQUkel54rp3kLOnZDunmW-TmbrmgQamnC1HjGWZsuhtO6yG-5Ub995vRMDDNRZot-k4cfKCnvYl_EoXZs9P34g8upLt6H2DMD8AQRx3DF0SyOOJid2Yp_8HiaHcbN1srBUAoYwGT53XoY3ZD2z7uUi0_ipCvl0W6O2wy4bGaV9ryHmsZyhQXGdbqBWqyriBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d2128a8f9.mp4?token=J4NFQYvbLuNqTlkVJIsGTLu_wuSEXITS260phPuuCb4MsscJObWcS8SW3IWfGATqyXUigb4kLUQWs3ql_9cC4Gxhu3S2TV3IojKzeYw4YPaXaopm63ejYk3Fu23aAssU047-i2B04VFd49lclr44yzFQUkel54rp3kLOnZDunmW-TmbrmgQamnC1HjGWZsuhtO6yG-5Ub995vRMDDNRZot-k4cfKCnvYl_EoXZs9P34g8upLt6H2DMD8AQRx3DF0SyOOJid2Yp_8HiaHcbN1srBUAoYwGT53XoY3ZD2z7uUi0_ipCvl0W6O2wy4bGaV9ryHmsZyhQXGdbqBWqyriBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چه‌غمی‌داشت؛ یه‌روزی به‌خودت میایی می‌بینی دیگه پلی استیشن رو گذاشتی کنار و بازی نمی‌کنی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23716" target="_blank">📅 00:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23715">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_aSTZvUQHL7aU_E2vPifdNfeYFPJ6UeUVGUOPegk12KTMzaVda7b3wDxoEdiS_VS2EreG7fNl7ktusiOSBL95bLgPSJt_j9wt9QLCGDr7exSdCZRUzrYGYANq2-2pf6RL8uP_pke8COZbkJmdxMXAFpB6i-_3n93PaXajND0BIPCBuwfda_bgRU7TI_Cs8a3MiMSU0EgVLufWcgDM9f-J6yEg-JOS-v_esc3L-wEkLzzo3cNvtU-X4PAjmO2WR1ZtxLAChanhoU1jr3nfef5f5Y0rcuiMa_LPiGC3uSYKvS7dJCdwNSQhzmWi2xDTR11IreH0tURxd1xoMSrOE3mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی؛ شماتیک‌ترکیب دو تیم انگلیس - کرواسی برای دیدار فوق‌ العاده جذاب امشب؛ ساعت 23:30 ازشبکه پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23715" target="_blank">📅 23:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23714">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OruoAohvgNMc9RWfyZtGi8_iIpeLj2o6nrSgF_NLvq6jc-aiYeltGZG7bf1AcvrEvETg4Fck29Z2fykSS6mAgk4nTvkq_2xR070Blr0AEHsTO7VjPzOtbOYvys3mb_lVAKNZ0OXiU7mtWFOmUMBBP9s6sT-qirtEdXnp4QvoYaYPeQpesqpPx1L5JYxLSRiRw7huCWGt3dPBC6-30TmqoESWzm8NEWrvPJVuXqrkusD3L6M3aAlYYWg2v1N2UNL2E3kt2cJijNakUXReR8E-CFD7b66lDWNN8xorU1aGKbjGBF-Qq422tIzzBZLcFVr5FUWh2X58W-f2fO67Fc0itQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
با‌اعلام‌باشگاه‌سپاهان‌اصفهان
؛ آرش رضاوند و میلاد ذکی پور قراردادشون رو با این باشگاه تمدید کردند اما محمد دانشگر حاضر نشد به باشگاه تخفیف بده و جدا شد. رقم قرارداد دانشگر برای فصل جدید 170 میلیارد تومان ناقابل بود که کم نکرد ازش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23714" target="_blank">📅 22:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23713">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79c30d0c69.mp4?token=cLUtNF8rHTEuq_ks3Wdi-XD3_Ty4zKWgtXDX5TScdVps7THHRQmwKgZzn8eloGBIo0PaWnqTzFcr78hL5yi9jL0JVwOTUXD4J8dfah8Dp9F4nfPSPyLFZBs5fn7zOb49vU8QbdWam-s8FmRdyv1YoWL7GJunaScU2j3fa8tpD2njIClQlCpbmOOzD7A9kpwNfM8XtbzDFtB981Ljei5-FOcHnecCt08b_nvkfXsmBCsxnHUp91IrIKcJtwcUhU9kh4drTiRVzR-swt1amxXJ6b8ZGJPUs3UjCj8Soc5MSjm-1HClbdEvIxcSTa2vv5VoNK5Te493CRnClu80mfxNE7FR4u0GE4cmx4DsRfxIqivKetvxhAi2ESRY6WwGJ9MU0xwYsfpQZxj5mq3WsETYtGw9udqTtGYkqx_fZrl3gzBZqRLZgMoAHRmgyD_VCCyIYdmsU6P60oIAi_u7g-MKr6PSz2x3XJLnWtW1PoE8z5_kzpMK5o-HkgsbmUyM86J9nq7WJzeS_SkW3k0bqL593js6gWlxWikOxihm1L2ZOyyXkNLHqcq3IEpLl8QtUrW5LRXYSDGSvxoUkXkWQJizNHLeATOCQuTrWRTtSH0anCiTZqq7Dok-tJWHdA8VufY0SeTcYL-xpEz4kK5IbLqNBB-9ofKoa7LPSViCdySAMtY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79c30d0c69.mp4?token=cLUtNF8rHTEuq_ks3Wdi-XD3_Ty4zKWgtXDX5TScdVps7THHRQmwKgZzn8eloGBIo0PaWnqTzFcr78hL5yi9jL0JVwOTUXD4J8dfah8Dp9F4nfPSPyLFZBs5fn7zOb49vU8QbdWam-s8FmRdyv1YoWL7GJunaScU2j3fa8tpD2njIClQlCpbmOOzD7A9kpwNfM8XtbzDFtB981Ljei5-FOcHnecCt08b_nvkfXsmBCsxnHUp91IrIKcJtwcUhU9kh4drTiRVzR-swt1amxXJ6b8ZGJPUs3UjCj8Soc5MSjm-1HClbdEvIxcSTa2vv5VoNK5Te493CRnClu80mfxNE7FR4u0GE4cmx4DsRfxIqivKetvxhAi2ESRY6WwGJ9MU0xwYsfpQZxj5mq3WsETYtGw9udqTtGYkqx_fZrl3gzBZqRLZgMoAHRmgyD_VCCyIYdmsU6P60oIAi_u7g-MKr6PSz2x3XJLnWtW1PoE8z5_kzpMK5o-HkgsbmUyM86J9nq7WJzeS_SkW3k0bqL593js6gWlxWikOxihm1L2ZOyyXkNLHqcq3IEpLl8QtUrW5LRXYSDGSvxoUkXkWQJizNHLeATOCQuTrWRTtSH0anCiTZqq7Dok-tJWHdA8VufY0SeTcYL-xpEz4kK5IbLqNBB-9ofKoa7LPSViCdySAMtY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته اول جام جهانی؛ توقف نا امید کننده یاران کریس رونالدو درگام‌نخست مقابل یاران گائل کاکوتا.
🇨🇩
کنگو
1️⃣
-
1️⃣
پرتغال
🇵🇹
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23713" target="_blank">📅 22:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23712">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzFu2wVdQ23V2dpl9sWwlGYJR5ZJoC05i0MsbIJN8v2REvs2cIhq81Qdf0Xc8zxix2Qw9bqzK-OpwzrA0Lzeqrt4GnYRvAa_11ArH6HU-wWvM9bzhyb8rFztFMHDjlrQSrhjIrlfILNsiq_kfMqQQg3ovJE44_n7NJnDx1imcq0jGWhIbOsSHuhrI0x6EKSJtVFbp1cfhfKl3Ou3at2bEQKXNkRgcvqd2SKsCSjLKXnnDSk6naDS5QfptOUcAULltJ6pue6YLFE97vw9DkGJ0Pjry6VZV5GMWh84TdLDwrS2hYE8MtevdIMGTE3TZG91WbeNy_OemHGeTAwYLr9Iaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باگلزنی‌برابر پرتغال، یوان ویسا اولین گل تاریخ کنگو در جام جهانی را بثمر رساند. این نخستین بار از جام جهانی ۲۰۰۶ است‌که‌اولین‌گل تاریخ یک کشور در جام جهانی توسط بازیکنی از لیگ برتر به ثمر می‌رسد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23712" target="_blank">📅 22:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23710">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vzIN-2yyxdct1HxU9LeJsOjGQFmlwNvi6CC8mKLxTU-meW5g8wOb9InEh0XuE7_5Ia_HdytkeQX2SjcE97fLqzvjasSkaECiP21C7gBCI9nJr7DIfQr3lmZMnwI8kfCYHTMq05hDVRzXexT6BVIt_IeIRRyWxog5eu5q_3jVCJiligWUil6rTNqKU9wtcIOvAjuZwVftdKWhiqo9JpuuAYT1ihszJJJgHM3NgZbNqaVmqPBCv0h43dFm4EDmg_xrcXQFQJ9MBqPl9n38LP3gWtBqi1x76psg16iV5EutubRL3_dn3OGcOPBnn8B3lYyMPrKDIHvn9bd6jFr994NQDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/I9UC2zBCqyWsH2qGqe66b2EL_62g_UWzyPxHrg9OkwL9Sb7f7Ai4XI_Ky4Heqh23Tg3sz1zJKIB2yDMxPlOILm6GZpbTJUckv7kvlSClq1z8XFUxQmoci2Utccmfd5_MyIzIgKNvV0zbEUeO7_KsFP7PBHE2MJv0bxtrsjqiDWAaOqs29rlXDP1bp-1-7mE3_-syn88yZS4ECB2beU62HlvGh3vD2tvdGtrAq39DOXBCBb3ZOSVFsoEPWPLmV0LoEIkvam-OZ_8YsM5DZgw2NlaEROhShS83rQtZYe3mogYZsqyabBk28oHBbmSuw6WGfQhvbeacPPKRhQv2vs3y_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی
؛ شماتیک‌ترکیب دو تیم انگلیس - کرواسی برای دیدار فوق‌ العاده جذاب امشب؛ ساعت 23:30 ازشبکه پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23710" target="_blank">📅 22:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23709">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8Mb4JZksCo-9wRixBnJ6VJURPHh-OVL20_o53ekGmZnYhBwXyIEDYVP3NptgH7Kbb8Jid8ddFI4IZkZEIYH8zITklV-aBx1odZ5I25OKPHbFs3zWvK9Bu-Dysxp8O-VdsPN38rAvKcEuj0fo1ZXEVUdibs9Z13xFmxirMM5B0Lcs7Znfyfq-g2TTQ5nnntfxiEgLfqSJ0374qhCKx9Ts2-9I9UihwNNQddOvAIA5NX1KaoibEGgIAMMvbFhprA9hq_YmvALrnuUa1QCmAVbvCwcgrdariJIPHRiQjQzgCW3_jMvZR4pVd9kJw6gL_4ZfANERSYVxzZbZzJunNq9vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
رگی لوشکیا هافبک‌آلبانیایی‌ساعتی قبل با صدور رضایت‌ نامه توسط باشگاه مبدأ به تراکتور پیوست. ارزش او در مارکت 400 هزار دلاره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23709" target="_blank">📅 22:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23708">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xoh1EvP6Czu7LsH8e8cfab1z6hPEo7bAur1nU73208PalVi6V4qjC-eQYz3Q7KxXJ8O7D6uQi0xBEWVcMh3unF0O10M7p5t4jf-VR6ANzXbAUKaISeGm35HtOuBsETzJ2Dq8u8dK-zOo2Ck8ULIpAldyAiwHDrnpWarluvNuCdpa33mlF6qnIAu3bpouL34VsaBy79pbAtrPPTCc3I3xTFE93Mu24jy8ctXH66Qqk3xlo2o0ccL1fUiufYFMSh7qBGnAzRuNHvTh2jcX5pMk9nuTmt-Q4WbPjvpOAcP0gYKoMhRcOXUQ190i0Ps4sPj4Cg2qwol1Xf4CnFkzYNAnMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی 2026؛ شماتیک ترکیب دو تیم ملی پرتغال
🆚
کنگو؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23708" target="_blank">📅 21:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23707">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaRS39G5h3S1AvA867v5gCWGJurjInEqw93YyQbhd7kU2FE4K4pHvLSMSslsZBSNIrW18q-PsNDFB0wa2vzGyPeV7-t3Y2MLK1keiNncX3AnqLCtTH1BYSVDyUerjmlAiRTXSnhrzMZDvHqtY3RE3iXfPg5jkCfYu1e-30Eqsr_zSJa3edtFGCC9pkLPaFW_eNHpcRbf9WdLshs62nvmfvMluschPTjwuUE_mWeg9BQMJE4SYapS4wJXQ2uUKOoHgJGfhkSK1LBrNqvpU0waySN8v_7EvU6LxDkAd5tce-b4r-3AkqD0RLtXMY3-v0HUJSmidfHb15CO0XJT6-wA8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ آرشیو وار: خطای لیونل مسی روی بازیکن الجزایر یک کارت قرمز واضح داشت اما داور تصمیم گرفت این‌صحنه رونادیده‌بگیرد. شانس با لئو یار بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23707" target="_blank">📅 21:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23706">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbfaW6H7YWLHWeZQBNZsVo3WteF_IU_0ByEztxNSG5wc0Wc7OgKeo3m4hCB8cFKkC4Lnfyxl6EzqKj3n5VoBlRNlugEAF1JV4rxXppI8vrpXfSJqHSP1GexgHbOpWZNq6gTPDEwc7Vh29dqdTJyON1se24QC6zoK3c72OZl-Bv33ffAOIxMj34MhnGuDRbC_IN2g2_2gjhlXiBp10u_hWvEd2EAvovlmuixsaSa1HPPhqgwHdTHUJZtcZJu33nJ_4smcK4_b-rHIqmkwZeuSHgVzLJ-QAeJuw7-OmhB1z48hJEjSjObEaAYKAxMoVmmmjvC9zqdOs1uCTZnOW0dmFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه‌پرسپولیس‌مذاکراتی‌با اسکوچیج انجام داده تا درصورتیکه بنا به‌هر دلیلی با اوسمار ویرا قطع همکاری‌کردندسریعا با اسکوچیچ قرار داد امضا کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23706" target="_blank">📅 21:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23705">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkL2pzjVwyPMHRTTGnVXq7Q_OO4QnoX4SFit5k120NWErmPJKTDKhe8XmOyaiux2D0BRMz-LGUSK0kqquC7Wa_tCBMJjNjj_Jm0BJCGUJa--wwPfYzs-6DDLLOMbiEOGuke4fZNGuZ6Wqv76xneUSzu5gf-fEOInZnek1CezttRTP92PHAD3vfqqT-QW-bmRlUffTo-Fe6pTRTjWytv7NCShEBRamuST67vh6in9Z8gyu2cNgFvpvas7oYX6gxC515uLMQVFsea_344dPi8BIQJPYpsfh1nmGrtcsJwoE-KkZ6oocZ1I2508YhDyoIxra-jT0NruaETXBe8vXixmNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبرنگارESPNاز پارتنر ژائو نوس پرسیده رویای چی درسرداری؟ گفته‌کلا دوتا رویا دارم یکی قهرمانی نوس با پرتغال در جام جهانی فعلی و دومی پیوستن نوس به باشگاه رئال مادرید در این تابستونه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23705" target="_blank">📅 21:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23704">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U00YLHog8jy-xZ7c-QnSPiM7oDpPFANneWzqioKpfZ5VIFw6hMJ00rPK7wYhwzn6-ceEWXQP-JALBoeOiP8tX2HLFH5a8pSW7pP11ITRNnzr3bigl1O97PmxQys32b1rsJbDtl4BhfvTLEWR1eX5x50qPYvyMiCBgS5L1y2VKgjXzXZM_Y8L7dsp8JSZtC6drH8NuhnKO9M5xvNqsJ_OzVAuGblD-2N42ife_0tpl_N6q7JzCpp4iMdnPyblEuZCIjV3GZenk5XSE5ruHySb3AHxQMr9vVj5si5ZeKqPR1yGvs_X0NoO8wO7trv5qtlu4PgANGK9LOiTWrLHWa6vKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛ نشریه مارکا: باشگاه رئال مادرید بزودی برای جذب انرو فرناندز به باشگاه چلسی آفر میفرسته. مورینیو برای پست هافبک اولویت اصلی‌ اش رو گذاشته برای ستاره آرژانتینی چلسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23704" target="_blank">📅 20:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23703">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwSXe4L7NIVwcyb4x4-oof2ct5T2cglbSE4BIm0U2rZ8zbMsMrotd_JjdgaN2Jec5PDqE_Dsd5-f-LGBJiEAtGSfgj1outZOjhgW19akhcJBw1LVXGBifm9QGvvx1Dt0CxLOkONhkAGXlx5yHw3mqtdMs9AWcik2f3X9IstSFdZXQFDjWRCsH71DKKp1KLRJD4-6gFHzADVXulXlgkRECOVwhJxNaRH8WLj93aHJMbWz1D2-1ojC--jWjzJKrB5ujaIB3zKgq2DmU145R9Q3hYeCGA9IlbRlNZk-zcJTPkACoj9obiZ3pngNb26FehTppnoIBWYKRTeUP3O94QBzqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#فکت؛کریس‌رونالدو فقط 1 گل تاتبدیل شدن به بهترین‌گلزن پرتغال درتاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23703" target="_blank">📅 20:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23702">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_G0dJt6PHz3pNmsOY6mHQyKjsEGIF_i9in__j3PpJ0WiZfNb3m0NrgZ7JVXv4eCi1hr_VjqufHyhOAgVlFALi1DCmirS0k_q2j9Kq_XpHwttH2Bq76Frs6Rh65dI4U6yrYC7mn57029rTbLduZ1R05AGVT_M1YjhOgiV6JwFY4Ma-r_ceL1bHV0zoMhUG9UzdPnwCfXpLdIdIHQ0GBDky4ZMWWJq7DHqCA9eNWlhdWgwlrwCTkd1WJr2lDEsn1Fs9CPITxpi5NpSBf-h3OVac4uGtrVtYm1WJs9pW6_lOk1WV_6GfgHVE2IpUVvLmIxe-81PHzITbnkERxrSpmzHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان خطاب به نماینده محمد امین حزباوی: هر باشگاهی او رو میخواهد 70 میلیارد تومان واریز کند تا رضایت نامه صادر کنیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23702" target="_blank">📅 20:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23701">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aR-gimH9IYKuaKRXDxq61FIVOSJ_dmu_eGBxB2id6DIcZxjRJxYE6zGqVAFppwu1YETMpwSy4mE7bG-ekrgL40kC_IcbNGWQtVN57b8XY6ir6WOIMzMpXFw8t8bU8FL-3tdZw42f8Ko7Dr2wUhkaDuYodvttVo7vhLQPKmzCsTuKJWn1ZUS0z7FxjdQz13pDkVNkPd5ayrhyWI33bR6mHGAIXJRlb3GZpYfvTZgw7noJPMe16bGFfCqtK93USnvLlqR0hBUYrlh-7PGKwkP9VMH_GSPhVYVPvTIpzbsPQGiwqESNK7dUrhF6mmq0nDivdR-Xvqp6D4U4Ttpb9Ca1jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23701" target="_blank">📅 19:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23700">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLNFdnFxshq_5IfqgoXvcP186ZNvlbRu3pprXE8qznraqmYG6bOIFdkardeJg3_-nAyPRWz_tTKTOTX9gA4RCDTEfqEFonVXLi7wmXUkX_R8smQJoC_RxHQMlQ-5R2VnQdIIIO6SYl-yktTPNF2VMaVDvDpx0uXMil-OZ46cTskJkAMHlthF7AAsHgWdDwHI8IY0kVRLNk8rfeLKiSaY8r-AXcDYxm3wov6kh4JmSO2zAP99B5uJnQBI0RvxZRzS1lPQqWwS88XSl49VSiMC17VpE6YqCKCn_AaaSQqDgnQTjAt4F4iJfRaxn4B2oVwW3mpSDvso47HiQs_sjYLz8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23700" target="_blank">📅 19:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23699">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QuEaoSnvd04-BdmiLGK9nV0EIQAmr-j_jbnG-7SBrjpEXkfVOxYAxzLLMfBo0iAA8AOsdvIwtHLlRokH8Atc166R8rMixkfPsn2DXKUbU6NYzR2wO-Sv0q6FOwOk7jX4r1_hTgrTgcN3QjwbqLBIB3eX4hQEpO7kqlmZuWPhdcxqgfGwsx8BDJNX-HqblJC3hWgCN5yJVQ-jedovIXCP1bH0Ca8QP-CKSSPPuvp2iUnYDykqXHTW0kAW14mo1JbQQAzbKEFo-18BWi5Hw4cfuNhRgF9Zdv3--xQ7T0hLiEdTkyOHeBCE98oa0V7OylsYBBfzqVPCueV5ly4DDXgugw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23699" target="_blank">📅 19:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23697">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tmLmkD19EFTtG6zQDDOouOXNKJ_cetPz02LphXmsCdvMV96KGy3L99dDlJiXVUcywGRyvWNqavSCvDyr21tmOtNhYcpGFampl5YIzfXZuKAqRGHtIWcD7FkWOQqMvhsWrNFqt4quiFyqQ6nJHUEY5ScqesqzVJTchdKgi0r_drRoYhfXn-vfMxPvqoouXq7z3NHnnDaP-PrrWlNY4fuz6rQ2V6zMIo4azXB3q0FEhBJ9Fs-mvOSMeWICWOyVtaeEdPl2jgVUWf_aVExYOzJGlyMoiqXxbwhdyhDN03ENJ7-h4FGhpBNlR3fsEXO7utAKHkV7SXzaIC265SJiERzLbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WQF_2P97Kcdc7KrYkH0AsPLKHhJIVg8o_F17onpYe1dBQl-Zw2ByOpZCM3Qsi0mDUQUkPjA-Zl8_ytPz0us5Tcp4ZmI39KkUYM-EMuFqe2eE-b8npxrQy_gnyGykxbOs5FWZaPc_4Yhyp2rsFe-D0pA5VjjhoThYCDJJlOiTqGddDFFjvJDJrvTIbvKhm3QtNGXiG3KpLVT7gKobLxZ2PhCBoBIHNN9eOVkS93idMctcoPkTy0NlHcdyEtr9LZOKfb5WCvv01OYZWoKGE2WNdN-sDRZIRcs3PUQh99mnNsRkxRukRoc0lUVAKsw0-Ye-RbZuCzojZB5SaPyGnJRXMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی 2026
؛ شماتیک ترکیب دو تیم ملی پرتغال
🆚
کنگو؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23697" target="_blank">📅 19:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23696">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/laM9-TynuyVQr_IEnhQW9FsVcswfuhKDePUUQJCSpNiO2VR7-SkWI7YfWVHK-7xLNRqOzyIXIPXmDntBejD9Y8qBDLRrUK0fPfNmvnNwxhHpwcENzuiEq6wAnV3zLXYsQJ22SDuAOg3QG35ZrbawykHTOmSp6EKwC6j3R77F1kbiV9n5sChGJuGYJVhBhuoZKyF7EQjTHUx0rOiOUEfMk-IrwJ0weW10ogpJ8ABZ2tBfbNcviE9TMa2Yj8y7aPKyJlrtAbqvmXCNSyJc7DjC8ue8eD0PEEZ0cqQ_KSy1BJfFjkg8MaYzIm1V2lIjuUJ5oKwBvqkcejj0kMRrz5uPHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ ژوزه مورینیو سرمربی رئال مادرید از فلورنتینو پرز خواسته از بین ماتئوس فرناندز و انزو فرناندز دوستاره‌پرتغال و آرژانتین یکی‌رو جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23696" target="_blank">📅 18:52 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23695">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kikyCmlcmApVOiizq0S9jn8kOS6Zo9mo4YKQcLIr-Qf0aPkkwnAhycMYl7-5Zt8_p4em-fRFhfWGJnhihKKT-Jrc0R8qGoFwbtMyeSoqu5kcvNnXMFNgLf3BDo_PZGGZacEh5qcEuKQUMzQZyYtV29BMHljgaJySMyDwD4ZtI2Bed4MhCY0clHNyZ6roJ3FNzs3oOMUs9dMYmTOfnwmFVa2FNDS45IG1bqij6wJ0MSYehL5028jl1prRhzo7SDKJMjcB5y8cK1rZiMS8SvU2cGPifr2OGtkOY5O0nryHvYxLuSyI8rNICCgdD_36uslmX2Dj_pgrbjUWTSoPi3oUiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام جهانی؛ پیروزی پرگل آرژانتین و نروز مقابل رقبای خود بادرخشش‌خیره‌کننده لئو مسی و ارلینگ هالند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23695" target="_blank">📅 18:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23694">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7cvSsIdNB9gD4dCD3YXH9_6NhosD9UFWOJqe5YBrnOJnxXsaStLTScClrpHxah_LdpLyDYxwLC0gl4ZJOFyCgEMY7LT90C1H4h9woASKki0iFK95TOqSBiCjD-x57Q9HFZINT8YWrqF2YyNlO3t9QlVAxwLMkEe3khwG60xU3Cj0m5EDSVWWlJPw-DvO4U0vKbLLFKciklTZ5qTR4ZCDItg8G-hAwmjQ_qBeJmNEFrxr7pJVXzdxnbMRF7l_aXbTXWR7znV8TgLIfa9zIAVXxAmQoSAt5suHc3sLEjGIL7cAglP03HWBQrivT9orQiDBaIrJz09VZSXgiYQyEwYSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
با اعلام ژابی الونسو؛ دنی سبایوس در رئال موندنی‌شد و او این‌پنجره‌کهکشانی‌هارو ترک نخواهد کرد. همچنین رودریگو پس‌از کش‌وقوس‌های فراوان به این نتیجه رسید که در باشگاه رئال مادرید بموند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23694" target="_blank">📅 18:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23693">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9GuJYSn3frkdLc--Ecj1Maeh2yKAjCL-lbxFHDof9OZmzh9OoNengJ7cnghS8DJI1XBwe9mheRgQ6_7uidggCIKtRFhktJQQyMZOiBUznJRqtwNXeRZLiwHRyjS2xx0che0T62Yj_rhHri-BB2viaLiAWfvB9426Mx80xmR37-6Fb5sgYzvqjBL__3EYZMLaYim423y-GasSnh42RG4C0z2eStoQ1-qfeH4rlLA9C1Z8HFDGgJGlmYwUIGVL7cwB2_I9XAyHreLgpKmoW2neI2XHA-j1XTaVlayLQoDTKPCrY3dVxGgDeH-Ak5B0mIXTLk9w-mXInBvBxNDSnu_Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...بااعلام باشگاه خیبر خرم آباد؛ سید مهدی رحمتی سرمربی موفق‌فصل‌گذشته این‌باشگاه رسما از جمع لر تباران خرم آباد جدا شد. به احتمال فراوان فراز کمالوند سرمربی این تیم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23693" target="_blank">📅 18:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23692">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b816759b6.mp4?token=QNc5Z4MjLbcREMxCwe9dm-Qt0PVGro6gOrBtSYY0JcfGT2pXe2OMLm8tEMqkBdpEUfZVCGaIhDGZPE_n3uopRYT9h4ijtJoDB9MQAFQSywK4zU013C8ceqNanLFnzn8f04GzAOn5f8F5ocpO1v56IIMSFH9FsHF-Xlaz1WkFRE-DtHOhjochxrGCWY7ONO0KqB6HhoXW3COA7jmMqVQT_HU-J9ffZ4VaMoQ0EacGp2eU-zUzI1zVDfb4zs-d3R0NINSyzWfw8AfM9WVxKtN7vIeDkGIU3tvaWpDEmnQEi_RF7Ex66DNNweiYskuN43CKLnrn6iGXz1wdn7Neok51domgzhXknrqeKM8Sn1g-QH8mg9w6Am1iP95d5Gyce7qXd7ELdEyhGK3ZNu1pOCf_fL94NLyktAZW3M7p3WSvPSCCl5-y4tsbCXEpBYrG2xg3dlFHWWbFUYzDtuj2GKTI4Mkb6isKnImiO9-1_4cl5JVuGtS4CVpa49hE4AEm8hDdcApa2MBRb5iwn1dQ_8MyvuvPkFo4VXNQ83mVgw5agUGe9A6FIHKa046slRuTIfynu85wKSYafjkRT46zM7tcPnCROf5w0ImGWJzAagKsbwvSHwzAtCiW3XHuFtMMMYKgTjQacWmHpt96tag4zj5zAtvKSLNQh8aioT39-17IFuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b816759b6.mp4?token=QNc5Z4MjLbcREMxCwe9dm-Qt0PVGro6gOrBtSYY0JcfGT2pXe2OMLm8tEMqkBdpEUfZVCGaIhDGZPE_n3uopRYT9h4ijtJoDB9MQAFQSywK4zU013C8ceqNanLFnzn8f04GzAOn5f8F5ocpO1v56IIMSFH9FsHF-Xlaz1WkFRE-DtHOhjochxrGCWY7ONO0KqB6HhoXW3COA7jmMqVQT_HU-J9ffZ4VaMoQ0EacGp2eU-zUzI1zVDfb4zs-d3R0NINSyzWfw8AfM9WVxKtN7vIeDkGIU3tvaWpDEmnQEi_RF7Ex66DNNweiYskuN43CKLnrn6iGXz1wdn7Neok51domgzhXknrqeKM8Sn1g-QH8mg9w6Am1iP95d5Gyce7qXd7ELdEyhGK3ZNu1pOCf_fL94NLyktAZW3M7p3WSvPSCCl5-y4tsbCXEpBYrG2xg3dlFHWWbFUYzDtuj2GKTI4Mkb6isKnImiO9-1_4cl5JVuGtS4CVpa49hE4AEm8hDdcApa2MBRb5iwn1dQ_8MyvuvPkFo4VXNQ83mVgw5agUGe9A6FIHKa046slRuTIfynu85wKSYafjkRT46zM7tcPnCROf5w0ImGWJzAagKsbwvSHwzAtCiW3XHuFtMMMYKgTjQacWmHpt96tag4zj5zAtvKSLNQh8aioT39-17IFuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌سنگین‌پیروزقربانی به کادر فنی ایران:
من‌ نیوزیلند رو راحت با فجر سپاسی می‌بردم. نیوزیلند اگه درلیگ 16 تیمی ما بود جزو چهارتای آخر میشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23692" target="_blank">📅 17:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23690">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ic8vAPDHbYPCGYQ8nTVB9D0d3rb_Mob9VaNspNAtXDXkbGmaVzVdM9DJAju36xIB0W_claXI91Gbn8ynd0Yx5gdJ9ZYzC-EkiNM0JI7ZPuqrOBk0WquygsFTuUBQ39abqEClgvjvYwjgS2sCqQOY7j0thRaR7xuBEJt0-6r9E8cptgxbnrRQir69EswK-itSuJWcAWIE1AzuLs5WyB_Ptpqgyj-k-7Axak-8QcbOZwep0n-YwCvu8Kb3I0DzU9ZpvY_PGWCzcJbBKIkzRXah6LsZondggccIMYPmfr7yK1hMQ4wkGUsD1A8Gh7BC7r5GCisxYVIGNdHEqfy0G8KVZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OHtLtRRTJ0rc2Dl-0m0k3hjZf8dfmMmNHcVR0o409vlAh6uG66jC8cOwsUuaW38HPjBvyfBOd2UYHIczTH2hLJAJP9LiDG98gT3VbnXu_z5SHg7uJuY1ouI-lS5q1lDflLtVoVc4cAiWvt2ChJz3dV30b3cigXXWPrGZs34j5Wj03kMxcWExRLxeviorP2DF7TEMt6ICvoDCTnf5tmp5Rk_EMojTtHUWhx2C6_j_pNSJSDQoQGCjlGGEnD-ATyUUE6K2ojqqxnnnbnMSgHsqrZQmnRMNBhK8rHUm47i6RKA4HXJpPRTfjgMXbYWj59-vHEICkIOb4FPGd57NBuXO9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👤
#فکت؛کریس‌رونالدو فقط 1 گل تاتبدیل شدن به بهترین‌گلزن پرتغال درتاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23690" target="_blank">📅 17:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23687">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjA54eW8a1Jzha4BlSdAyVHgUrJxGA8VJnwXJedbsrCwujuN7vBJYtkcwe-I3Yzr3LTWMEc90DzdFfH4-mcHy5iUwDPwFh0AxlUoTvgpYFkeKtPkseIFcJFleUK6CZPxBDDqWJYLjWBYCk6dduWcTCKyIaoPgDlzcS1HSZhfmyF1w_lRI19c2yztiavfWj1TBF11RB9FQlCJS_n9pkcp4PA7BXz0lVzTMpADPUkr0wiZQipgm_54wTsRMdzbs9aGD3mTQFEcrhWx30Frb_zirJAr-S8l96yxEj9K_1h6E9Xj2yg_H34TDLdr40VjcpnlnKno30895MIaej4N9iM6FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لئو مسی در پنج بازی آخر خود در جام جهانی
🇦🇺
استرالیا؛ گل + جایزه بهترین بازیکن بازی.
🇱🇺
هلند؛ گل و پاس گل+جایزه بهترین بازیکن بازی.
🇭🇷
کرواسی؛ گل و پاس گل + جایزه بهترین بازیکن.
🇫🇷
فرانسه؛دوگل+قهرمانی+جایزه‌بهترین بازیکن‌جام
🇩🇿
الجزایر؛ هتتریک + جایزه بهترین…</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23687" target="_blank">📅 17:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23686">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/012fc50185.mp4?token=j_8-V5HANcfLDy2R52Wa28HnybFugbc4LnggrN9cPn8ieL7NiEShulVF2H4EtDWCjbSWicJ1I7yNLs7w2Sx1Mr2ByMnZb__myn_cROUo752WT68hypT4uqEPHO6ssNLs65oIrDYuIdig_JTZc6TLNr_gwF8PZWPUc9EWp6QZ7BbMM_ezN3ItU5_UogtdLJBIuWQElZKhK2xPcGoGp2ITb_kKayeuFGZynb094fBBorSa7tqWHrjMThEuBaPhLhx25sggKqqa3XfXzlda2C1JS-sBtBsxJnZihUigHVvS_ugOn2rJLLnkrd6B4mEoxO7s_6A2BB-a7BMbNlWfa_Y6IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/012fc50185.mp4?token=j_8-V5HANcfLDy2R52Wa28HnybFugbc4LnggrN9cPn8ieL7NiEShulVF2H4EtDWCjbSWicJ1I7yNLs7w2Sx1Mr2ByMnZb__myn_cROUo752WT68hypT4uqEPHO6ssNLs65oIrDYuIdig_JTZc6TLNr_gwF8PZWPUc9EWp6QZ7BbMM_ezN3ItU5_UogtdLJBIuWQElZKhK2xPcGoGp2ITb_kKayeuFGZynb094fBBorSa7tqWHrjMThEuBaPhLhx25sggKqqa3XfXzlda2C1JS-sBtBsxJnZihUigHVvS_ugOn2rJLLnkrd6B4mEoxO7s_6A2BB-a7BMbNlWfa_Y6IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خداداد عزیزی سرپرست‌جدید تیم پرسپولیس:
من اینجا روزی چندین‌بار از حرف های جواد خیابانی هنگ میکنم. بعضا وقتا اصلا نمیفهمم چی میگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23686" target="_blank">📅 16:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23685">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mynIvl3fbHXhPhJXF6KDd-xKcLAS2M0sjkvAYY0iz2DJp3xM20fKOqNtnF0faM_H6NbOflVZlHZuPB1Poxl5WXUf-JgWgiyOvI2e-tFHOMO_n0y3qvzLTFrbKRiPNuUZ_Jy7nERTv8o_z2cfSJ-WJtfYEnqs1KRQ90k148bScxfLDCFu3U71xKJlcDk3GpUb3zZxzoSwPW2BLcJHZMmtHPVSg2tAIN3KG4DfkU4UsIr5s8JxWfTiwHnjY3ktO4DqtnKXFOAE5SNuLQlw69YKBb_OYxBJHeyAVRSEwzr0QNZq9PoPpYBU2OfUFH9ESNZ6TGRyQNxqUDsWjSVJOoPEoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لئو مسی در پنج بازی آخر خود در جام جهانی
🇦🇺
استرالیا؛ گل + جایزه بهترین بازیکن بازی.
🇱🇺
هلند؛ گل و پاس گل+جایزه بهترین بازیکن بازی.
🇭🇷
کرواسی؛ گل و پاس گل + جایزه بهترین بازیکن.
🇫🇷
فرانسه؛دوگل+قهرمانی+جایزه‌بهترین بازیکن‌جام
🇩🇿
الجزایر؛ هتتریک + جایزه بهترین…</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23685" target="_blank">📅 16:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23684">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a3b4e42ac.mp4?token=bbJ6CjaZkIHbXKv0mW_8oyGN3RSzJ1A_nMsu7vnPjEmWVxz-1lA_Z4SQT9spVtPjwjM05sE4RHE-_Fmd2__n3RYN2cENVP57qZg4QX7FwlrZfTHFpQuk1NJXsFZ588146R0dGUAvfLG5XTWj-JpcJHEKkgOrI3wnhqcnW2LCGPPlh56kC121m48z6OumFdDrxNdsd2-e6qY-HsaFn_IxoxOfFeFHmvMN1g8HDb-NIJpgU0fOmumEm_dYjF6NYfmGH3H_7DWSMtOQWBP5hmvO4H_mqScFjPwssugFX3Qx7gCj8LdTBA6Rq_DnoGi1WUOVbTBSU-yR9Z1fncdF-8xIMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a3b4e42ac.mp4?token=bbJ6CjaZkIHbXKv0mW_8oyGN3RSzJ1A_nMsu7vnPjEmWVxz-1lA_Z4SQT9spVtPjwjM05sE4RHE-_Fmd2__n3RYN2cENVP57qZg4QX7FwlrZfTHFpQuk1NJXsFZ588146R0dGUAvfLG5XTWj-JpcJHEKkgOrI3wnhqcnW2LCGPPlh56kC121m48z6OumFdDrxNdsd2-e6qY-HsaFn_IxoxOfFeFHmvMN1g8HDb-NIJpgU0fOmumEm_dYjF6NYfmGH3H_7DWSMtOQWBP5hmvO4H_mqScFjPwssugFX3Qx7gCj8LdTBA6Rq_DnoGi1WUOVbTBSU-yR9Z1fncdF-8xIMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇶
#تکمیلی؛ آیمن حسین مهاجم تیم ملی عراق پس از ورود به‌آمریکا توسط‌پلیس دستگیر شد و بعدِ حدود هشت ساعت بازجویی آزاد شد. اتهاماتی مانند همکاری با حشدالشعبی باعث دستگیری او شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23684" target="_blank">📅 16:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23683">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c34750719a.mp4?token=fpxl-cA0_5XlqNrTN7fPJxKKnhcAiSrYv_IgGQ0w-gXVLoaEFQ-9kinZeJCpgcgC4GT6pYYs5SoNDp_DGJ1ZMKVwOpg_CEDdU98yZlU9qCpix1x6Ukmz2ZKxyKWw-eGWjqWcaWRWUxmDdkPREZUnxfWz_rklKb3oGZUmaOsHOANAl-Hh8L3dXDSwT9aTt7f9dCWKEv3ZqWcvxhAO2a4F1iB8SCBT2dFcJfypRtSd_tpAvzBtKEnsia-8lNyA8dJS-ivpKBx2swmBXr42-yZ1Ut0B6CiI8sGsNudR1F9J3iQA8lKM0I0yl_6emmoiuj3rA7pL-NiOQ8lNlArbXZf3Z1ufNohY4ZTTIyvlQFtmIr02nmrY-44jPIORBrddCBmYqeqBn4XBILYh2CdBy5DSEytz9aYwq-RbG3-Kk9pXaBXFyOrGI-jIEOYIQguX3Ch5gax_HjmGSZUZdDr5pc-lSn7fcP8k7pzLanqTIhNFj1Y4QGvHoZmg0sKoW8wmpyrxo6DlMIsgeGYIL2ONsWxj2bJvFEb8AMWoRJv644Yw7qxTF6kZCqdqRhKZAEFo2fkrN8P97EIV_iaxHOBMKnlAU1b-QJDsC8dOinClIVtAIPFM3o8-xkkA7bXx5vIOQD9cEYfI2TTV9ig8wyG5d9RRo5YGAxbVLuYTwS007GJ7gU4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c34750719a.mp4?token=fpxl-cA0_5XlqNrTN7fPJxKKnhcAiSrYv_IgGQ0w-gXVLoaEFQ-9kinZeJCpgcgC4GT6pYYs5SoNDp_DGJ1ZMKVwOpg_CEDdU98yZlU9qCpix1x6Ukmz2ZKxyKWw-eGWjqWcaWRWUxmDdkPREZUnxfWz_rklKb3oGZUmaOsHOANAl-Hh8L3dXDSwT9aTt7f9dCWKEv3ZqWcvxhAO2a4F1iB8SCBT2dFcJfypRtSd_tpAvzBtKEnsia-8lNyA8dJS-ivpKBx2swmBXr42-yZ1Ut0B6CiI8sGsNudR1F9J3iQA8lKM0I0yl_6emmoiuj3rA7pL-NiOQ8lNlArbXZf3Z1ufNohY4ZTTIyvlQFtmIr02nmrY-44jPIORBrddCBmYqeqBn4XBILYh2CdBy5DSEytz9aYwq-RbG3-Kk9pXaBXFyOrGI-jIEOYIQguX3Ch5gax_HjmGSZUZdDr5pc-lSn7fcP8k7pzLanqTIhNFj1Y4QGvHoZmg0sKoW8wmpyrxo6DlMIsgeGYIL2ONsWxj2bJvFEb8AMWoRJv644Yw7qxTF6kZCqdqRhKZAEFo2fkrN8P97EIV_iaxHOBMKnlAU1b-QJDsC8dOinClIVtAIPFM3o8-xkkA7bXx5vIOQD9cEYfI2TTV9ig8wyG5d9RRo5YGAxbVLuYTwS007GJ7gU4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
👤
ویدیویی زیبا از شاهکار فوق العاده علیرضا فغانی دربازی‌ شب‌گذشته فرانسه مقابل سنگالی‌ها؛ همین‌عملکرد درخشانش‌دربازی دیشب که دو تصمیم فوق العاده گرفته ممکنه باعث بشه که از همین حالا بعنوان داور فینال جام جهانی انتخاب شده باشه.
‼️
دو تصمیم مهم فغانی این بود:
که اول نظرش رو تغییرنداد و پنالتی‌نگرفت. دوم اینکه آوانتاژ داد و باعث شد کیلیان امباپه اون سوپرگل دیدنی رو بزنه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23683" target="_blank">📅 15:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23682">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/167bd8b41e.mp4?token=Xo2x6RCy7IOmemBNjwE56hHUxHtWz1I78dYQxOFBDcKNV1Wf5dDLJ5o2NlaRqxA68kdDFoko-oj2mrGIdKlV9hDj5_sUUvZF0rVmVyY5AZtCs97_tKGmusraXTER1qe8Ot_ET6PYMvNAaef7DIqsQL3hXMxFM2Kma1EdiQzbL3b0ojVIE99lNtpmkh6aOBW3YONm4qAcY3oqGLxdRFYZOhK97nh1MRY4KvKbWieyX-tmu0kSOqgOBACIYv27LTHGcuTjccBcMT40KH9mNjNz9yCPbhqyrg8fl8OzOESdlI9Y5EEX_V4YZAjJYwEo-lJq-zWVHKtmffs0LzsZitqx0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/167bd8b41e.mp4?token=Xo2x6RCy7IOmemBNjwE56hHUxHtWz1I78dYQxOFBDcKNV1Wf5dDLJ5o2NlaRqxA68kdDFoko-oj2mrGIdKlV9hDj5_sUUvZF0rVmVyY5AZtCs97_tKGmusraXTER1qe8Ot_ET6PYMvNAaef7DIqsQL3hXMxFM2Kma1EdiQzbL3b0ojVIE99lNtpmkh6aOBW3YONm4qAcY3oqGLxdRFYZOhK97nh1MRY4KvKbWieyX-tmu0kSOqgOBACIYv27LTHGcuTjccBcMT40KH9mNjNz9yCPbhqyrg8fl8OzOESdlI9Y5EEX_V4YZAjJYwEo-lJq-zWVHKtmffs0LzsZitqx0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🇧🇷
#فکت
؛ تعدادگل‌‌های دو شخص حاضر در این تصویر درتاریخ رقابت‌های جام جهانی رسما برابر شد و حتی ممکنه سمت‌چپیه از سمت راستیه جلو بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23682" target="_blank">📅 15:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23681">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbrjRJGLiMBdYftED2iW-4URTayPcjsMpkaE0DidF3wKBdsAahAZK9bP8dK7cvpsFFp4x53voTCN152Tq0BtVWUaqBiTiDjVH2oGZQdk3t2ebrdhW8xRyJJsJei7ZrUBjvhFF9feIELSHNxHCyO71kJaZKXGs-5-kjktEeYWjFzEKkWxBCSG33kIo-wQdws24WfPGFKL9GanzVqfOPgPPeagpuNJfaW9tcx1G9bvVMZwNHk7uy2f5cfZMf68l5FZlWU0EgTLRqQ7QgJ6v79Ky79LCIEhxF6P3o-sRQst2pCoBca6GcSqCOts-aVhKr33lsiRpXgWGSZXNv-M588rWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
تمام 120 گل لئو مسی باپیراهن‌آرزانتین در بازی‌ های ملی مقابل تیم‌های ملی چه کشورهایی بوده؟
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23681" target="_blank">📅 15:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23680">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cr92V2GRRQVaEQRC4K5FkUao6_wn_p3IDKtmd5hMdW_iPQoyNOlqczdoT4yHVkAZ6txF1uffts3Squy29M8Nr4HYLnuskpI7LDugzOGt_VKm38yTugSFQqRtdlsldHwK-xZkR7V3iq48RKSION2hwLUaK30f7byteK41MbXaT75mfn1T6aF-aJp2tYRUNFpDYAEDVyf1uJYQ09_OmGtk4ZQVtcm2BSSKL4JL9-dfhOcqxg7MPw6lAe3pWP3JAdQmkWe6dHggHfiVWXd02K3HctZ8fcYLWwGyI-kXdEiy2nSEIJwjz_LcxNzcA3vsQgwM0JtuYdkMhaoXlk_xkQBD2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گابریل پین قرارداد یک‌سالش با سپاهان به پایان رسید و رسما مربی آزاد شد. مدیریت استقلال او رو به سهراب‌بختیاری‌زاده‌پیشنهاد داده‌اند تا درصورتیکه سرمربی آبی‌هاپاسخ مثبت بدهد با او قرارداد ببندند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23680" target="_blank">📅 15:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23679">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mccbl7jN9UFVEJ4gjLJiZphWqNIIHclSA1_EDKfuhWjMClGPmcVNd5xIqy509gwxL1ECtO5yjJrtoiLXMw9klPdVMIu3E3d6BB1OuYuKNfodmvdONDuQr92JTqVHq1Y5snCmk1WuLw864OWp1wIcY_lse5mvzTJHBjbKjJqV9klaTZau3hf0IUxuAGGudbdUztyUX8xUnWXfCpwGHmm61N852kHonO1unLivw5ACzy0F6T2i-NbNb9CQt6zdWGchxL4etaB_xqzAchOQcdMMNvvjAhIgGoNti1KiIEcHMLsWmFJohu73yxoBt8r6zancTYm5qzu1e2WMTGXtZf_1mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خوشحالی بعد از گل بردلی بارکولا ستاره جوان تیم‌ملی فرانسه به سبک محمد محبی ستاره ایران.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23679" target="_blank">📅 14:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23678">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/np-2NK_cqVp44eHBSFrb1I9lhI5d7k5Re5fhldwHC1ALhlQ0ncmZ4RaG5pTMiSlpO_U52MVAlwouEh3x3xU5rmAh_t6N_Zvmi7fBUdwQg3zK5oaMb13vGfsiXdBsLT6aNUCSkPpZD0P4Q6irg90oqzWnIAZRr7C3uYAjQvPASXJ3kXxtrC65zcTTcpYXkc-0rgrzveQSfaBK0_baPhx4U8LIATauzGnILxiMZkzLIMXTpvwQaKLnzy9pYb1wfazqVZhzNPWAm_-7dGbtRBl40_WBQy1oaK4A74CzJGjZvKRxi-dl9yyg4tUWsxyBHzPFTT2JZGNryyHk9hzznFXdlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
#تکمیلی؛ عملکرد کلی لیونل مسی با پیراهن تیم ملی آرژانتین در تمام مسابقات + عملکرد لئو مسی در تاریخ ادوار رقابت‌های جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23678" target="_blank">📅 14:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23677">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0FxY5UWqriRVhCwqREVEZBTgvln-fdviVdfHMzkZgeK4fYNlC7aEFeFZzthBi0RS9GdruFAYyaDB_ec2XByML3m7igCtUQjFIUHqzbbguc1UXFIXl-cMtiMoR_9shup4dI6646oZPJ2CjiAZ5JyzIn5a5G2xOOSB8ChGJ_w3SZpwOWbVDQCtQzhht3Qfx3aAGjbVKJLqI4iOzL2u4iVIQpz6NYu_ib10lxTo_euV2_lg-dNeUjHwuLZ8AuBFo_hEyrVeChVpBMlL8K_7XoUqYT1T_61B9lRxYsNEiax65RrjbOzLdNiHu0UkXBYHf4YxDs8CVY89JKdbj3bdpkiQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه‌کامل‌هفته‌دوم‌رقابت‌های‌جام‌جهانی 2026؛ دیدارهای این هفته روز پنجشنبه استارت میخوره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23677" target="_blank">📅 14:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23676">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdjJ3KnWxBRHR6h03Ft6LdXu83gt_tPFFgETbPLjQk44ROWgeKRnSNuyKTKgnDFa8syiXKJAzv0rSpcnsyG1luCBgjXUhynuX2MwlKJ5_g4sZ92fcw70olw-CwGaVtbfhbAj6C8tm9FpQwjaKiD70yW2x5JoqR6uf7zeoQESx0AL0ypT4qXt1BPAvzgxkqwhVsCxBminUJoZLSFk12o73ebSpzpIM5txv_Zcdy42ghJm9VWtZJJtsdvzvpjEk_XV5s2OdijEMfJbugS3hnx4rukjeD24ZdSvERxaj6oJ9JTdaeiuOwGqOeQdYTLsHsIrfIEOfCyPiXrPBLUYxHpoXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبرنگارESPNاز پارتنر ژائو نوس پرسیده رویای چی درسرداری؟ گفته‌کلا دوتا رویا دارم یکی قهرمانی نوس با پرتغال در جام جهانی فعلی و دومی پیوستن نوس به باشگاه رئال مادرید در این تابستونه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23676" target="_blank">📅 13:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23675">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa85532cfb.mp4?token=CcQ6od-hcdthU36PQ_H9vm7z-2iu5B1xH_sMQfZzQuD9_LqRnPXg6yfKpmOe88hYD5VVkwxILf8TVO6upYi_L3B2GmxkaDdRljTUo2q-kvzd42ZVNLHpblR1eEfbomCR_TYErlktafG70mZh2WQmR4O9LjIKX2kCauAfgJ5oOpYF65gNAr-9yTgIP8q-HUzWQ0K3sqmiR1UngW8G7Hy21WKuLE22S6rNZNEoJHCiPjCSaP3fRjIjVr-dc_mcnJ7_RNPc9-YygNJ_q2OOcfZKkWQY3d49hiERMd7it-sT6dYL1jK9lROfW1aiF5JQouKMU-yZz9HsE8oFhPJ9cbfW_TFA9Xz-Q9lL_ZHZP5Y_8-2U1paOmfIk8rmYuPbKrxTTuwVoyj7UxNrsszn_qLfipRbfOhXVk2f17eO-WnvvRgAQWhIxzaiHmwydc53JeoKE7NfyC3vW8YBSKfoP9A_cU6AZ8q-SRFFuKypQrT2WO-rf2OTmGcRxJs4aMzLCB3w1XO5CTmlCkoTXAyoQfUHLiVMuPXjV65i1yP0nrgsS88WbMwhqD051s_QaH3nViRxya_WyFljFi2qWY9KMfSdwQeC1Ws-a7KVOOjGMSTeZG9RXikezP9lgDCSnTYG3BklIQBh8yckYjCBeTHsjX7htVuIYJnfE7CvgQXqPHkv-vwM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa85532cfb.mp4?token=CcQ6od-hcdthU36PQ_H9vm7z-2iu5B1xH_sMQfZzQuD9_LqRnPXg6yfKpmOe88hYD5VVkwxILf8TVO6upYi_L3B2GmxkaDdRljTUo2q-kvzd42ZVNLHpblR1eEfbomCR_TYErlktafG70mZh2WQmR4O9LjIKX2kCauAfgJ5oOpYF65gNAr-9yTgIP8q-HUzWQ0K3sqmiR1UngW8G7Hy21WKuLE22S6rNZNEoJHCiPjCSaP3fRjIjVr-dc_mcnJ7_RNPc9-YygNJ_q2OOcfZKkWQY3d49hiERMd7it-sT6dYL1jK9lROfW1aiF5JQouKMU-yZz9HsE8oFhPJ9cbfW_TFA9Xz-Q9lL_ZHZP5Y_8-2U1paOmfIk8rmYuPbKrxTTuwVoyj7UxNrsszn_qLfipRbfOhXVk2f17eO-WnvvRgAQWhIxzaiHmwydc53JeoKE7NfyC3vW8YBSKfoP9A_cU6AZ8q-SRFFuKypQrT2WO-rf2OTmGcRxJs4aMzLCB3w1XO5CTmlCkoTXAyoQfUHLiVMuPXjV65i1yP0nrgsS88WbMwhqD051s_QaH3nViRxya_WyFljFi2qWY9KMfSdwQeC1Ws-a7KVOOjGMSTeZG9RXikezP9lgDCSnTYG3BklIQBh8yckYjCBeTHsjX7htVuIYJnfE7CvgQXqPHkv-vwM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
عملکرد فوق‌العاده و سیو‌های محمد العویس گلر تیم ملی عربستان در بازی مقابل تیم ملی اروگوئه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23675" target="_blank">📅 13:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23674">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNb90rFO7d5fcPh7DZlFvp5Le3ViIhp4NVFOwRJCAuju8xiJerOC9VGubEqoqQK46TiNfNrI81jm8liNCgTcrKnK0gK-jEyvQBrEbq8bK0wttHjGjls-5xcmzZAw6GqjKBLBSNaXAe2yYTY9Byk_fHUvwEkw4MrEWA1LK4WOvYhfREVmeRKGpLyQZyIzPXS4d8DbgfTGHPVBFnN86B4kdRXCGO05U9KDkPwbNGUitqkWbpx1300l7E1j-IWHNO-X6uMkpe_O-CDlfJyKP7jT1Oq8WvVM0hsuaXKnmOLSy7Svgjys080rkWZZ4XHWSpPa4qbQ7uTbFU7gt-vmnWIjEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ آرشیو وار: خطای لیونل مسی روی بازیکن الجزایر یک کارت قرمز واضح داشت اما داور تصمیم گرفت این‌صحنه رونادیده‌بگیرد. شانس با لئو یار بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23674" target="_blank">📅 13:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23673">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyyE95JUFdjLX40hvCQv8vKlBZ4un3i7CDwpnIV3jXX-cdMc1Nfs5UPZ1ds12iMDHhf1NyeQ6HfA44BI4HLEIl9nKE9nadCcPliUCRSgdxcxDUmzggGrYSa-Ll7O1VpIDuI2eRc8MiI0Nceq_LuXv5DIA36ZT83IXp0brlhLCcKtKx34h7j6goe8wQuOCBWQnPayxeBmB7oDjusJ8dPE3s_1Z3TaKj3ftL6k6-nAUqn2jlPzyG1ssdkMNWIriACSIz2WWOi_mJfntbIWzek78mzEyQ_PSQ-WhyKVVWlxcPTlO0SWKgO6hNU0FQC2LgTWAh3vCGruagcTqlbkoS9EAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇪🇸
خوزه‌فلیکس‌دیاز:فلورنتینو پرز میدونه برای جذب مایکل اولیسه بایدرقمی بیشتر از 150 میلیون یورو به بایرن مونیخ بدهد تا راضی به فروش این بازیکن شوند و قصد داره همین کار رو نیز بکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23673" target="_blank">📅 12:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23672">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eiHwDQ4f9K_WLMNRHKh2SX_hL2FuDckaV7JWsUj_m7g-nDBWZ7BaWnf45z_FqLO5tAmVYE24fwL3RevlUEbRIpkXUyiNKBfr3rK2gQkvQNtO53gRtOG0ymYeQ8eNkVBdpf5iP-wn4XGPxFL2LG7s_yy8rpRgu6YFN-SkQZRO7c5883MM3XgytXe-lWhHmBuTFGnhT8jXfxrxMMTiACYHf6LNWpYAxQEnihLDANzARBFErU4Mgddnvunf0F9xT68JG9HHKQNJp0a9HTZGzs3aKThKe812C7LFkWTZG8m_HB7d9qzyJv593RK2oAXefUmKJ9jAIvXSCGJzIEAcsAsLig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛ برناردو سیلوا تست های پزشکی باشگاه رئال مادرید رو با موفقیت گذرونده و باشگاه بزودی پوسترجذبش رومنتشر میکنه. قرارداد ستاره پرتغال با رئال مادرید 2+1 ساله به ثبت رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23672" target="_blank">📅 12:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23671">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqfPWLKD7FdsL1xIiNVw2VNHJ51np0pWRRIG9Yi_yiYvSOWaI9LFVvVgIM3B9Eh0DabgCnej58-1XV4Uvy6fDADxlOiwyZAL_3Cnm0Hhjsf1v6TjFxjnnfPyAQt0cSZ8bw4XOPs3SDDQVkv2HcZwkoQNsvGvzKWoGQ_kMntFXP54B5biCLPtUkFdvSxLZW_HZrXAeaZUx9HV9qZEK9hCAmUkcmQxLUpSK8aPIUBGsB9i1W4bhRPIr6jIeMgoh-8F_7Wxp6x7U2GnDOc84v2oF1sV8uynC-OTOK23dAIpdM0iqM_ym38pY_h97hDupcap9Ph1GTiq2A0ykSCk3DWm2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌ پیگیری‌‌ های‌ پرشیانا؛ پرسپولیس پیگیر برگردوندن یکی از ستاره های سابق خود شده. امشب اخبار جذابی رو در کانال خواهیم گفت. ساعت 23
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23671" target="_blank">📅 12:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23670">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxcpfH8KwSbLlqfgCbZEOM2EC-5N84dY2zVyjseKJcIyVtqlKU4q62Z4IutGJFvM_MW_cjiJNkvTV9tvhc-dErBGeZ5keS_vpfrGI5M0EvpthKKd26io394Xxb_PCKy2u99ZZHTOZMWkXB-vY6Ar_CbXOfyC3UqvXw3KEUvLjWXijLa8eUgwSxBcXH7hq_oGBzdO75PWVlXy_uwLlB2WAII39MAYx4qH3BdjCEu2LRjN7QCipipM6FULx0QTbhmTFWa4BWQ7nhDmZtaGiIbQ86iSepYc0MKvOmdEeBKm6FqhOb9yGTgsx75tnO5LBnOQYOQWfRM-KFIcaoJirMhUyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
تمام رکوردهایی که لیونل مسی اسطوره کاپیتان تیم ملی آرژانتین در بازی برابر الجزایر جابجا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23670" target="_blank">📅 12:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23669">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfY9jPP5ImQRC0pnqZHrZ6bNoLF2bWpHH0leHUOoC9YZ8SuMtjurOBOHrb_67htvmq9lJGX4vyN5FZB38lm31zIBCn8Q2YIh0iItUxBNCWcYud3hAYe8GxODpFjplml_ba2T8Vc0dBqZptq_umhW2DaxUjNoFI2oNnboY7275cDkuWn3ZnDK2ku6ErKGUKVlbh5G9Dew0vZztmGH9wI12j2OLFzJi-pmGLH6uA9F9bhzrDWcNxRxQ8T71IG6UiuEOQRDGVM1lTqLhmRPUsj-1-D1l0Ra4W_EO3zgF6_td8RADRYHx18RiaEH2YZpqkztI3gabPEju4mdP9aBBdP0Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
محمد محبی و مهدی طارمی در پایان بازی صبح مقابل نیوزلندپیراهنشون‌رو به هوادارایی دادن که باپرچم شیر و خورشید در استادیوم بودند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23669" target="_blank">📅 12:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23668">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCUwZvANXI4pvFrEdPNunIXIWLaMLWAfb0LV__5RlLZE2qT5SdImj1thb8azCE2lIrnLy_BoiHMDqUuKziGVoO_9c56W66EGuBLITZihUKWuG9e6pbhpNVXD98tC26kpSeHq9QN3gIl-PLC5sHFEU-yKVe44K1FyQF788WUN1M0kN8UZlsRF4URrhdkouucwPptgIqAdllZoNM9MM_kUiu9XCoZUmaqJatI_Mca8oOf_Z8u-Wi4r5Hkn73Jzj1TjU1iWatns3Lr7CYENwwc-_gJQWPk2zycYPSB9cWfGjcbueq6vFQK9BBVxhMYHTsH6FFMQI9KPJd2NTVGIeAPc4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛باشگاه‌پرسپولیس بلافاصله بعد از پرداخت مبلغ  توافق شده به باشگاه روبین کازان از کسری طاهری خرید‌جدیدخود رونمایی خواهد کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23668" target="_blank">📅 11:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23667">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTbcSL-Bwgj4_yTe7UkPW_Z7qFOKXmIs0VWCy6IV5RQQn1oxtt2ixW3WI1AQkpqJSiQ63-VRUWiEwd_NUdYMCzyxhCPlNJ0zcLJxYWrzCL3lM5cUnQDXMXvbFjFYisIl3krq8E3_BEiyz_8AVqCsPfRlFHmL1vYkJQv6fKbyrNsMFEZY1Ngdj9eXJL9RFdjRFTR62iFSCpvb0wCVI3Ite5AfCdV14IOuk94lLTqK59fUkwtUTsHhA6nwLVCicE5uP09Zj98pt5KXeDbF8TDZr5B8EEFImeKljXAIdp04mLqFUWt41n1VYFTCQZ2G3wYZbYZ5Of4tiN8J3Xilj0owlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
تمام رکوردهایی که لیونل مسی اسطوره کاپیتان تیم ملی آرژانتین در بازی برابر الجزایر جابجا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23667" target="_blank">📅 11:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23666">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3k0hdi97baXkvCsXeKPWtutr_gHsc6fpQha7SiEvHeIBMXMaxyQYaZpoUd0oeQYIP_WikVTrXMyyyK605aBzDcPAEtHx3IFDdaPzwoGTwapvppg2QLvhVZh1RGLtZSnu4mozRAG3IWx-agtoHCbQ3OUj-IHkbLsUJ5bKDlspWdteNR6xtRmhXzR0bgXNi4D9hOSPCCeuAPDPECmrHgj-RFkp591YrDewokOtACIUeyoRNnOBORJ7UiOkBb3DXwFe275JTjEsV_MFAlKNIxArB25kU-SKipUINF1k4U3KeB9xHOlpFf7NOk3LbP2U88ak5_GJL61HUohRFjFknThVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تصاویری‌عاشقانه از زوجای‌ایرانی در حاشیه دیدار ایران
🆚
نیوزیلند در جام جهانی 2026.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23666" target="_blank">📅 11:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23665">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hr1DHKz1s4LoZHT4XAU_LZt7g2u0umMh_vl3HDQq3e3WzrvMGuWwhC68bYZWXBQ-ydjLuWfMowEjJooPPgPvWjj-ZyQPw8P7lrmCUnJ2ALDsrwJ8hO6POlbK1arvRQiazzhIspIhQ6KJ3fNQNqP2b8gAnTMoaN2V45--jJpHv4feeEwTcMA5ndyRWjcfKQ707aZaxqYi3anslSozmmIFMwb05F5tK55JGiWjkqLUzRYDOa9l5Yupkd3zd7pc0xkuVWweTO--hUKd5dEvdnuJqNwPRqWm1Hsy_p3t_mUdYs5zUjQL7U0v-CGf-b6ZTzxrTyjhoW_HSQ-5nvv8k3ki3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
آنتونلا و پسراش دراستادیوم بازی با الجزایر؛ آنتونلا در پایان بازی اعلام کرد که بزودی همسرش رو سورپرایز خواهد کرد؛ بچه چهارم تو راهه؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23665" target="_blank">📅 11:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23664">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkxDMCBVgS-_2ghQOIu6LrNuRW2UbFpfRaA9F23K0U6P7011rE3a7ELnXbhvX61G2EiYa7RE9uWJoyUAJGzoMQ6ZOHFfQKIBurQL-hTt8q2xqFSABZthYdBYJGoXzwucxiixy_gFDfR2IJZhlW-YTw0c_nYtLN83Z7EOjYp2SaTc_tnFZFFgavtgKlwFR_NTV_GEvzKUStaZNGfpZ6tgZvrfsDwW_oTlFLfMvHnEa80_LNa-M2EZ0pLlB06kwg6LhWflphbfXYn63lFy7d-HiT98HjLuGBL4pFzqe2dKLTNK57Jolhx5ZLZ5qeS3crAW0gIUn9wPQ5iYFzoT7GETww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سیدمهدی رحمتی سرمربی خیبر خرم آباد بعد از اختلاف با مالک این باشگاه از هدایت این تیم استعفا داد و به احتمال فراوان فراز کمالوند یکی از بهترین مربیان ایرانی‌هدایت‌خیبر رو برعهده خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23664" target="_blank">📅 10:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23663">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNsi7FMlrd10aO2zAso82m7CthnmQO10jzif2heXBVzgm2i2SyL_Gn9Dymta-AkOFPbMLoKak3G4RJ7O_K_ud0IjDrPm5wy0wv9Ki2hgMlNTPQ8e9LNwCiDsf0a9eq9vpNIr2DguAJUoJldW8KQ1Ekt8oKSPZjN7Bxp1r-wIzmM3_1pXXJzI9ZXQisqdUn1VLRBQkM0aIZT6MUZMjJHtp2rIyT0yOIwjH3bYvT51wjWquyHrGrhUK5gJo93dMayZJyifPTy1wgrFy7tK0IS53NfyDVkMFEB7PS_sG8ZrJlZBFZaU9rTYu1VL_L8f_klnkEPpZNdHK_BEbGX-hGrghg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
#فکت؛ لئو مسی با ۳۸ سال و ۳۵۷ روز مسن‌ ترین بازیکنی شد که در جام جهانی هت‌ تریک کرده. عبور از کریستیانو رونالدو با ۳۳ سال و ۱۳۰ روز.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23663" target="_blank">📅 10:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23661">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S4ner0WqqnOveAKLYGUDIKR1OokKZi7BNxrtZHXdLEeDqY7Kt7lrRofUd2R7LTBEwkFSEPsSuehstoMCp4CJYaAmLvCgLsiCMG9GpO1iNq72ermR6komEyuJJ6xUyo-me5BVDKl62c51pX8zDt6CWt93bFKNVvImwDMRVVYG2LY5m70ZaA2JdioAwoFLxQspodX9pXLl5g248W2o2DBMgVWvecNICEReDkD_hzX47RfIu1hOI6Whw0sGYSGHYuZTf5uLRPabGj5Tvm0nKEWDpkMjqY8sqmI-X4-omE1F4lYQO3CTzoYq_cLu0MhidIXtlf6paM2eoH9dbhSXJ6HPnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r9E4Q2x1HptFC1Zd10BUHJIMLODe351lbijwNVgw4eawfZKvvzpdJW5oFDyGtne1TsMVUjhlwLHYfHb5OOchXwdrk2ccHTvvYfi7Z3xsdukA6cQsDdGRp5m2G6wCgPw2Pa5MuvQaBMslyslmyi-2IMQ8Npu_Phfpf632296GgwKfu2fqlFy9mb-ofNVehiLRjnpldugVw5IePIhRp13wecbrzpFToA-7dkYPKkizIv_PNmR5CmFQT5trTeaAMcOTkiDZKUyMgoEVkh-0DQwl-gFFSPRT1dWVdIWRdHl70kXPAwpasy-fU1BxBrq8y2omJhEHUzQa_Aj55HKCkMUm4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
دو زوج ایرانی در حاشیه دیدار بامداد امروز دو تیم ملی ایران
🆚
نیوزیلند در جام جهانی که حسابی در فضای مجازی وایرال شده است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23661" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23660">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2ca500416.mp4?token=ugvi0IqeG18u6tUpyHI_X0uq5H1zPvFCvPEPWij8ZhQnUv_gLLLkfTH2wXcBDMVshDtGNHv9LajrEcXbR608Yu7CR7nFRxiroeAtc4Sp8uKxbxY9YgZj4MnqvZ2DeJj_VEx7nngDo2ffWOtEkF9RX8QzA3POHWybuOYBjuhAC0uZhLAtY7yAFbeXHrJ3e2dFUdTzhJctw5ELvisqxLbkyJSbh1guqC2Wn2xbL7qXeRtwv1p_3f1ng_6hOrUkW7b3gzb7zwSg_reMBMxO_z455bTTJ4Ba6ucTI_W2zJux3V7643KCTQv7ITaB_UDyEC3w9GqtLVQ99o74p6uGFbpX4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2ca500416.mp4?token=ugvi0IqeG18u6tUpyHI_X0uq5H1zPvFCvPEPWij8ZhQnUv_gLLLkfTH2wXcBDMVshDtGNHv9LajrEcXbR608Yu7CR7nFRxiroeAtc4Sp8uKxbxY9YgZj4MnqvZ2DeJj_VEx7nngDo2ffWOtEkF9RX8QzA3POHWybuOYBjuhAC0uZhLAtY7yAFbeXHrJ3e2dFUdTzhJctw5ELvisqxLbkyJSbh1guqC2Wn2xbL7qXeRtwv1p_3f1ng_6hOrUkW7b3gzb7zwSg_reMBMxO_z455bTTJ4Ba6ucTI_W2zJux3V7643KCTQv7ITaB_UDyEC3w9GqtLVQ99o74p6uGFbpX4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
«ووزینیا»ژوزه‌مارو اوورا دیاس؛سنگربان۴۰ ساله تیم ملی کیپ‌ورد نمونه‌ای الهام‌بخش از درخشش در سنین بالا است که پس از سال‌ها تلاش در سکوت در جام جهانی ۲۰۲۶ به ستاره‌ای جهانی تبدیل شد. او که کودکی سختی را در غیاب والدین و نزد پدر بزرگ و مادربزرگش گذرانده لقب‌خود را از واژه‌ای پرتغالی به معنای «مادربزرگ» گرفته؛ نامی که ریشه در شوخی‌ های دوران کودکی‌اش دارد چراکه در بازیای خیابانی هر زمان بمشکل میخورد به مادربزرگش پناه می‌برد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23660" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23658">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6xPmDM4l-gBgl9a_g6Ehhb50WPoXtu1BcUq7Vjr3yvg3JQ37tfDVidf6xBeN-eQi1Ys6NYVcLi1Lrb6oWT36Icm3tYnqIiDromzqUNRjzin9sH0OcjBE_YmFA1NreviNtbc-ZqIei9fBCoxUzyVq6OfRcs2Ndo_9ndt3l097pLqbMSS6sOAt-OHfJsI9MtyIxYP8rWuB2B5EljGGLo1LIfjXDclCo7M-xScLZ2iMrTj2MlA1SGTcgcst7lDSjl4n3H9yKRzN6QDUPrw189vGbeLMxU3cWl6AIx5OxZboWwZ3mdRR7hqwws5kgpgOZ6kQDtCi8ZJQyGmDYpEjjgzAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه گل‌گهر سیرجان پیشنهاد تمدید قرارداد دو ساله به ارزش‌سالانه 20 میلیارد تومان به مهدی تارتار داده و منتظر پاسخ نهایی این سرمربی کهنه کاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23658" target="_blank">📅 10:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23657">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8Cq5tXptEbnressu3-PtFk-MIRrsIlvN67lmUUeEkfNxOKQRVSD7AqjopiEGwgQCA4hozPFmvK2C05Tp-hO3PMD19da6auJ2Vb3umA__nypAnDR_NOTSZiM03YksQhYyj6D53-KlB5DGjKNpwt3JXOknbt9WVNskNUrvjEYfqdneIRNuqnoDy9LXmWsfHksHtWggO2dlzYo_2ZMzWBrJMDkmwGS4nXEUaONGKrEVk1fkNLsKrm7H8sIul5Px_uubWHgulatXp9x3w07ZiNetYKv4wPxs_bXbyvtmNCyIB-gN3W-TPtH6TnNL0Rf_oIM6KS5TfprBDO0g6m4aUdhPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
#تکمیلی؛ عملکرد کلی لیونل مسی با پیراهن تیم ملی آرژانتین در تمام مسابقات + عملکرد لئو مسی در تاریخ ادوار رقابت‌های جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23657" target="_blank">📅 10:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23656">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hid7cjNjDiFsFpBNOqao3xOFhhZFGPkuLMjwwUhKamHcRASnVMNkDpNM24gBxYgVnwDygQr5lFdOFuzwXc5JDkcyuvxKHOkVb0QhztN5PEPgwXXf9R_p04M290_oB4bRDfc_JUK6D3oqgrnukYhX1eJPyiwmV34JB-FlCFo61vz2NR4Xyu1GGQhZX_P12nvYU6mgYZ56jBzoNa6HXlkrFcSTaTyS7HarYS5dFEPamKZr7AZdwr2pjLe28x5K3Aqqz8lxe85i0sLnGIpLcCUrRSQ1mdsyu6A369gQqjWqcksC_AMeKO-9il23d4QnSSK3FDfoJYl7pl031vYBkP9Hcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ ایجنت محمد جواد حسین نژاد به باشگاه‌استقلال اعلام‌کرده‌مبلغ 1.5 الی 2 میلیون دلار برای رضایت‌نامه حسین‌نژاد کنار بگذارند. خودِ حسین نژاد موافقت خود را با عقد قرار داد سه ساله با آبی پوشان پایتخت در این تابستان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23656" target="_blank">📅 09:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23655">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">⚽️
خلاصه دیدار دیدنی‌وجذاب بامداد امروز دو تیم آرژانتین
🆚
الجزایر درهفته‌اول‌رقاب‌های جام جهانی برای دوستان‌گلی که این‌بازی فوفق‌العاده رو ندیدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23655" target="_blank">📅 09:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23654">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e7674afc.mp4?token=F0vvvQE_sIswa-uQ3E3xQozWyhSEGEaXa56FmdrAs6zr3U_79udB6ntMpi4qdnRIyzPnqoHo83bGSAdLznTDGPlDdwnGcW8cRMjzt6w4oXxcss6AoF6TSx4AIuFatACmQBeP9_VH2AEyKnFQRbpQ6AGy-s2yRjEUIgH-hP0Tg9Z4v-8mdKoAZQO0SRwr8Hz_HSNm1ttvZTPSDzQOZ62b7RpK2fRxcbs00OYXQRToj9V5OJTUARHCqMIvm1HELNi8yI6k0IhuTMrTl0Da3fuJ9ECUWGwRnQUIw_36R9X43g8C1cZW1KCPZ8FyAvzC9bxsPw_KpKQyB7214zFO3CEAUl0dcRzF_gVQHk3CMRlesu10I3xfANRQdPKojKlxOIVVJxQfWlddJW5RHRvrZkUw36haVa8gKT3UFDintVJaH9amTAzTrEphbrK9AriqOTXGsHD-pk_XE6XdZSih9ICDPFlx1jQm7jCa1ZAdrSnEzOFK9llELqvQH6GUlemXEja0EnDbeR5NViwtDg8ZY79s5KLVV6EAUczi_FiVNHDHBgDX5W95QUdiHPrQwtwJHDvw8ePMZamLlqHlTRNcGFwzRV93xY9SebEW7P5shoTjdtEbBQRHPhholhqVKVOMkIH12beN8z2y_Y4Ocf51UHE-wGh6T0LZSJHZfdR__XfcRUU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e7674afc.mp4?token=F0vvvQE_sIswa-uQ3E3xQozWyhSEGEaXa56FmdrAs6zr3U_79udB6ntMpi4qdnRIyzPnqoHo83bGSAdLznTDGPlDdwnGcW8cRMjzt6w4oXxcss6AoF6TSx4AIuFatACmQBeP9_VH2AEyKnFQRbpQ6AGy-s2yRjEUIgH-hP0Tg9Z4v-8mdKoAZQO0SRwr8Hz_HSNm1ttvZTPSDzQOZ62b7RpK2fRxcbs00OYXQRToj9V5OJTUARHCqMIvm1HELNi8yI6k0IhuTMrTl0Da3fuJ9ECUWGwRnQUIw_36R9X43g8C1cZW1KCPZ8FyAvzC9bxsPw_KpKQyB7214zFO3CEAUl0dcRzF_gVQHk3CMRlesu10I3xfANRQdPKojKlxOIVVJxQfWlddJW5RHRvrZkUw36haVa8gKT3UFDintVJaH9amTAzTrEphbrK9AriqOTXGsHD-pk_XE6XdZSih9ICDPFlx1jQm7jCa1ZAdrSnEzOFK9llELqvQH6GUlemXEja0EnDbeR5NViwtDg8ZY79s5KLVV6EAUczi_FiVNHDHBgDX5W95QUdiHPrQwtwJHDvw8ePMZamLlqHlTRNcGFwzRV93xY9SebEW7P5shoTjdtEbBQRHPhholhqVKVOMkIH12beN8z2y_Y4Ocf51UHE-wGh6T0LZSJHZfdR__XfcRUU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
صحبت‌های عادل فردوسی پور حین گزارش دو تیم فرانسه
🆚
سنگال‌درباره‌قضاوت علیرضا فغانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23654" target="_blank">📅 09:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23653">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">▶️
قسمت‌‌‌ششم‌ویژه‌برنامه‌‌فان‌‌جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23653" target="_blank">📅 09:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23652">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام جهانی؛ پیروزی پرگل آرژانتین و نروز مقابل رقبای خود بادرخشش‌خیره‌کننده لئو مسی و ارلینگ هالند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23652" target="_blank">📅 09:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23651">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
👤
باشگاه‌پرسپولیس‌مذاکراتی‌با اسکوچیج انجام داده تا درصورتیکه بنا به‌هر دلیلی با اوسمار ویرا قطع همکاری‌کردندسریعا با اسکوچیچ قرار داد امضا کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23651" target="_blank">📅 09:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23649">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q4xU7SYQmC7X-QtHSbPP2KD4iZeWfMIO3C4ZjN9WVokt0Jxp7KwoUVKSP_4ub-RRFtblK9sYF505648KDj79PYDB2DId0rmMONFdnwVyVzV-hyCp1H2zxFhRubUfkbAzDCzEwG0GFj3Rr_EYrYCrzbuwglqzCi6Xpti7seXBM_5uxc3viTdJXYa0_67kErLgrf9to5PaJl7RMPxCK86OgcoY7fCjoHc183eUYQYgWeVOQbfj9TExvPUfCtyBEPxQaLAcXk25ZqtL5D7lrz3zpgrQyU8jGN3NVz6PLJyDCK1spv67sL2yTBTzV7x7d6wArrqTx2Z1Xluyqh5FjAdEwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mr9CRqaBEKe4fN5ak8oE0JAE6UBsp_0w85wB6B4ClIKC6fcmbebIYzaEuZPJTY8IqcMK9bhBud7xlRbnJz1jnA6swZVPL4icHIHW-vqFWTJkFUZUQC7ycaGBtApDbmb88nmRXPHZpah4bDCKobPVizvyo71378ZY4m3_rh61vgJTX09rAxe5wWyfiDfiaxQWDClcjRpeoY2mTzyaTthuTUrIXzlUWKxZzilP9T8SWuz28hGWI1Yc-Bl9l5gdb6Z20U9-ZFaoiiUkUOSb9FgiOVbFCK7ESuSJQSl8YcDxqKQqXGGWtqTf1_ygX_k3z4xIeqA01y9rIo6m_5yEZdBG-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
هتریک فوق العاده لیونل مسی 38 ساله در بازی با الجزایر؛ حالا لیونل مسی با16گل با رکورد تاریخی میروسلاو کلوزه رسید و مشترکا با او بعنوان بهترین گلزن تاریخ رقابت های جام جهانی لقب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23649" target="_blank">📅 08:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23648">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LuJlb9ZMQScb4yXUXzAcBM5gLKL82Ly8Gye-dCiryn32yqVCUMuxQejATsx3Y7YdV2huPOTrLtBDWj-KwCSThM-lWrhtaAZlo8w92Har7kmbRgkF3BXALZZsW0DBgys9W21pnr1NZ0jcing9bd5Ad0v-00--vvMNXjeUp3gDihpVJJBp9ee88PJlEow4zAQUmULaS_bozxuOVkbH5oGWKPklUnN3_5N-5pXofKZ1xcTfjJ2pm5YXrWtJMNI-fIS5r_SDdrDIC2qqxPNlOKkno-Jtughl9YgL1V7Ndeq0KHeIFqHq_Ekfa71BX-oc2Djs0qBOzXO9c9sSL1gGqHthWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
هتریک فوق العاده لیونل مسی 38 ساله در بازی با الجزایر؛ حالا لیونل مسی با16گل با رکورد تاریخی میروسلاو کلوزه رسید و مشترکا با او بعنوان بهترین گلزن تاریخ رقابت های جام جهانی لقب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23648" target="_blank">📅 08:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23647">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام جهانی؛ پیروزی پرگل آرژانتین و نروز مقابل رقبای خود بادرخشش‌خیره‌کننده لئو مسی و ارلینگ هالند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/23647" target="_blank">📅 08:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23645">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aFS7obWLTTTd3iXfuFoTV1ReD8cRFPZ2vd-FMGMJ8f0Ns2OCz-VWyIkCW1EeAOU96ZWEPoOq49MLQzkOLfKweY4ijqGTtyl9FiERChZ7MovAF2rNlL4xERtF1cW3bE7I73v6pLoxjHWhZ-HO7Kv8zDNV0eN-ZfCosFtTJq4-whRdiXi88aHylzXGdl1uscyJ_1EOA-iqhUciy64ZXRphsvUM2J4oOLbaxPuKPXnQPIN61izpiblPRGUbzbv-erpzrGy5a-0YWv1F5rPGh4o8aFPsivw1oorJXq8TSGC99Z91_bXOAAPLZQ9sj7-_tk3zXMS2nExfFmG1_w4tZKP1VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hjkJjT9j82n6_bs6lGkKkzp_ONmIGViaFiagcUKvqXsiJZdvrhMpV4RMYf0BBKDvBhOjysU-Q_sC-MfAinr-363UePOAbHqM_AgB-t4ndybJ9JKxxhjpneKCE0GGElfQYUkyP1M84acyHewCNx8rq7MAX3DZsyIgN0zjYe4P9gXAGY-ESlWYdh3XwxIeff7BQ_9oXfn0JXfCB8G8hMIiV2K9v0rjo_1xmfBnNRjzianPgQK5bkVpwO-4ZTm7k9BiZn-W1RkH-b3LyyD9QgdQZJcysJAyMLaFhgDxkMR4xcvGbd8GSHOYJnLmYBhYIGzMuPEhu24IDHI9IvBFGzeb_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌‌دیدارهای‌‌امروز؛ازاولین‌بازی‌مسی‌و رونالدو درتورنمنت تا دوئل حساس انگلیس
🆚
کرواسی
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23645" target="_blank">📅 08:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23644">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f480511b29.mp4?token=cCgwwzclJI9cDxfa85nx-2fguHg9GK2qIqJyhl-rGnsCIeO3mibvDcauLJvyO2WNSopPxbtmqukqrm--R7yL0rZtlIZyn54yPQqCXrJib4OULF7NhokdGtKGMo3K0dv9f4N1W_SnYDFatUJcuHvewMdLYPthakLnvbODjtLQdtr7pNwI19NGEt9EK3Ao_GzAeJJof9zG5XD4c0tUsUB4-xM-7-lJa8USQmnvIk0QHvmspDYDx2QeWJl9biVkegqyZWrYg-mL_Jb1uKp46jNiDCNmr39jS196XfOU7ln9ujQfuqTL_AXkJiBmbFcmxRCMOzREC4ipmIwLT5bxW8RrJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f480511b29.mp4?token=cCgwwzclJI9cDxfa85nx-2fguHg9GK2qIqJyhl-rGnsCIeO3mibvDcauLJvyO2WNSopPxbtmqukqrm--R7yL0rZtlIZyn54yPQqCXrJib4OULF7NhokdGtKGMo3K0dv9f4N1W_SnYDFatUJcuHvewMdLYPthakLnvbODjtLQdtr7pNwI19NGEt9EK3Ao_GzAeJJof9zG5XD4c0tUsUB4-xM-7-lJa8USQmnvIk0QHvmspDYDx2QeWJl9biVkegqyZWrYg-mL_Jb1uKp46jNiDCNmr39jS196XfOU7ln9ujQfuqTL_AXkJiBmbFcmxRCMOzREC4ipmIwLT5bxW8RrJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
خوشحالی بعد از گل بردلی بارکولا ستاره جوان تیم‌ملی فرانسه به سبک محمد محبی ستاره ایران.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/23644" target="_blank">📅 01:32 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
