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
<img src="https://cdn4.telesco.pe/file/JrsEPndXhLSjgYLqJVYtMPs8BKmyyFw6I7YufMwrAmGr0ltk2v91X0R6QEfJP_UaeGn28zUvMlTG0FUF_mH5St4Y4_fYF5xAISMptj1K59NCaCBeUCYIObIal48mL2bcQGyHXLZ_1sJzera8WgmnXupcWYiHwXsoxntCvG2JyyeAIP4oURvC4rqelfBpsMBacRGGXHbuqFnpFfrbQPSEIKAFhtGdilZ8gAFX-EPz-jQUWrHzICM1lYnfobjsc-6_CW5WvkYHpqLqWU6o7R8VHwUJAIbNOtQUKPSjRdu67mw0tu53ahnVKrK2IO8_APifon-X93ujEtC7H1BBwdGFmw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 172K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 21:15:03</div>
<hr>

<div class="tg-post" id="msg-22952">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-aa02eBvqq28SPB36dYSmj8JZGpoNjsJYM7wLq-py0dUgm5sRHFjoSHBfW3ScrYziKJwSslblAyrfYvmK8-Wv8WZ6LQVhap8-5pnCkQBspBRxHgfxLviVf60TZgFU5lyZR5HBr9FCpNqmdYLPqYyWB_43poyQJlS1GxqAR8ok5XZqMah49D8h8POl4OmNwyiM0CFT3Xu7pHegH3G1A5kr5sJnvPBryOD5TehTiinusex6RMfsOO88gicBJMkSCcNxQ9KqRZY63cGS8YTml9IePaEKInEgMY1s3PCJvqGUtzeZ4py6m5JbTdrC_9v6OrcAcLYTuzThFw3Pe2FJFrAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
حواشی‌ دیدارآینده ایران
🆚
مصر در رقابت‌ های جام جهانی 2026 از نگاه هوش مصنوعی ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/persiana_Soccer/22952" target="_blank">📅 21:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22951">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c25ae3aa7.mp4?token=vjDBSYmEz7LiEP1hUlZhHJC0P4yfojf4dO9K_USq46sg6P0wNpVXVrVb4kB0w4c1MaEOXplQKK4XtS4VMQNCFIldZv8JV95jGVK4Qt5eLC8cIvjlutNraqlPUfUHm7Bf0HcCAYtPJ5okIsFIQg3EzgrN5Vm46drdeBriropnKhejPpULjnfNOyAZPMmM14o9u6DtyieitSXhu7GZ1ar6sBLwElsQfWj4TkRRIgO4-t3MErIjJ56RDJdhA0d0n2HS7dYTYLT4gL3fz_3UdbvNqh-uxgY4Ag9wie97K8H3Z9Vg3xGkhAilvG_feNl9CjuO3wSdWwE3LiT1whc6KXUWvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c25ae3aa7.mp4?token=vjDBSYmEz7LiEP1hUlZhHJC0P4yfojf4dO9K_USq46sg6P0wNpVXVrVb4kB0w4c1MaEOXplQKK4XtS4VMQNCFIldZv8JV95jGVK4Qt5eLC8cIvjlutNraqlPUfUHm7Bf0HcCAYtPJ5okIsFIQg3EzgrN5Vm46drdeBriropnKhejPpULjnfNOyAZPMmM14o9u6DtyieitSXhu7GZ1ar6sBLwElsQfWj4TkRRIgO4-t3MErIjJ56RDJdhA0d0n2HS7dYTYLT4gL3fz_3UdbvNqh-uxgY4Ag9wie97K8H3Z9Vg3xGkhAilvG_feNl9CjuO3wSdWwE3LiT1whc6KXUWvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
تیکه‌های سنگین ابوطالب حسینی به تاج رئیس فدراسیون فوتبال درباره عدم صادر شدن ویزاش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/persiana_Soccer/22951" target="_blank">📅 20:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22950">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_r2omQk9nt7Zps8EMMLifoiGAmIoUVnYyoVPuy8yJ6eW2V2XZTTIpHr-4TlbAryRqmZ4I2y_Aj4scHq7ZxYzoqVHgmjLOXi0DR39BCd2wxdF5MIaw8xiB_8dVCsmo6_hjiLLRcll-ppWp4KxEwsJ1k6x3LpReBuRFj0mY_vF89EZY2FGud6lBplKdElDum1gvTZfs3xhP7fd1_9UwHSTh1a_nT7QVfp66JBbtqLcsFYk1sQ50uJktfavONRHjqDrBbc95y4HL86qAzv22XwyntoGMopiy6BhauP4xBCvg1Q2UN3JUF4eNv7OGrfWpEZpwTaV7bCn_qb6_c47QcuEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ سهراب بختیاری‌زاده سرمربی‌فعلی‌آبی‌پوشان موافقت خود را با پذیزفتن دستیاری دراگان اسکوچیچ درصورت عقد قرارداد با استقلال به علی تاجرنیا اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22950" target="_blank">📅 20:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22949">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNqMziCv3v7dKNR9Rlq0zLxoASKMR7wUPTzc6gUHFKiSiS-nTBB2dwvG-vKvy133OZQuYCpwX1F3z2c00bzo4D5Ee3PRx1FvQKoavQP-pf7PTZ-iI7xMyRfONVJa6ehAK-ojIqpdaNRnig4wAoY6XbaK2QIz3e9YPosaThF_cRrieggFVkfy_nWlCsQb_am5ho6q1hy0U54vc4XIcu3Rftf8JEoX_GvRW2dKSR5wSCVIghG8s7AiKQ7bcHxgJjvtG6q7dELy-j8voDl1P9fe2lglEiOycGyWkbglVZDLWQCqPozpdlgsP96YvQyvFnyWk2_Msk52ui0J4POInQanqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#فکت؛ اگه کریس رونالدو در جام جهانی 2026 موفق به گلزنی شود؛ به مسن ترین بازیکن تاریخ این رقابت ها تبدیل خواهد شد که گلزنی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/persiana_Soccer/22949" target="_blank">📅 19:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22948">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QL8PzbXjWNhxaG9ojosFD_dHAvwFc95VqFuR-oZllT061v-mgsUXLDXLRm_QU28guRfBdTrGsthqiRgO3DdHzmwOIZHRp1qOdgS_6AleOkhQBpNAIYOqsQkGAQuVZmjT3gn-Qis7qQUqqYbzCe5q9G6oONldHWTkQQ4zU2drl9AlsndaHNqYklqFUXbBqFbzJ0FZ1KXIzMVr32lFjXWEMvREPlR1odC9OgpVbBb8hOWBEY7Iq4Xk444C4CpMxqVRTWk_TeIf1YUwGfoRqln9qxjk0Apxnt0yLHSxAGKKMTJ90mT0gJwEuCUPz4nGPbOFIRc1pdh2_DXv9EdDK8XDlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ باشگاه روبین‌کازان‌روسیه به مدیر برنامه‌های کسری طاهری اعلام کرده هر باشگاهی که کسری طاهری رومیخواهد باید مبلغ یک میلیون دلار بعنوان رضایت‌ نامه به‌ باشگاه ما پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/persiana_Soccer/22948" target="_blank">📅 19:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22947">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c78767e61.mp4?token=bwDwM3hh54NsAIpwkleiHjar4hFF9hWJqHUL03-apWvExh29eDY6QacCO-kVaGq3xzHqY0Vh6kYVXYPfQZHPSVicNLCH_yailZUUDBpbeoJ7Ya0kcKDIMtE-mexvZHoyj0V0zIaEuUvcU0EopL3KAljXxdgsgi3ht64tpitBCftaBFgtXLpFl6d3VUFTamK4ymWfmSqS4KMiYTrZsXk4cnT6loyRvlfsOUj9Sftk4guYeGcmJKQjheH_kgVn6q4SQwI_T3_E6JUif9Qd-iSn4nX6JIbDMN1_w8NlIKJuWThGyNFsXHbGns0a9CLD3WtCF1mSPUS5z7-8ekqhb7KmYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c78767e61.mp4?token=bwDwM3hh54NsAIpwkleiHjar4hFF9hWJqHUL03-apWvExh29eDY6QacCO-kVaGq3xzHqY0Vh6kYVXYPfQZHPSVicNLCH_yailZUUDBpbeoJ7Ya0kcKDIMtE-mexvZHoyj0V0zIaEuUvcU0EopL3KAljXxdgsgi3ht64tpitBCftaBFgtXLpFl6d3VUFTamK4ymWfmSqS4KMiYTrZsXk4cnT6loyRvlfsOUj9Sftk4guYeGcmJKQjheH_kgVn6q4SQwI_T3_E6JUif9Qd-iSn4nX6JIbDMN1_w8NlIKJuWThGyNFsXHbGns0a9CLD3WtCF1mSPUS5z7-8ekqhb7KmYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
آقای‌ممفیس‌دپای‌هستن مهاجم هلندی اسبق بارسا منچستر و اتلتیکو که داخل و بیرون زمین می‌نوازد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/persiana_Soccer/22947" target="_blank">📅 19:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22946">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYjKdyXsQ-8FYOBTQMNQ0AWVscdVN4-INYvRyTzAYA3XLh0zCzY8oE3I1X8Ng9A60Yyb6qNtT9H3EuyhTxcJTLRDM2b3fG4QXG4JKtaoK7PBjZCB_ykcY4on6Qpa6AkfjJa4ki-O3_wk6jK0dcSVbgJKsTZ2xqcLPwZdHWIniJphhusiPQLl2sDJJnnhZMrDfNZivVBJ2rt3jZJPyVW_N1NhEYc49X-LLM3vHcUUVltMor-WHNOACsiAkhHZEw4tCZz18XOljc_AQQ7xZj4CJTe1RFFHF3jLSudAuN89YM9Y8e9K8RnXJOQJFvLK9YeoHgQVax4AmaJAfPaM6e7QIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
در
#رومابت
با ارز دیجیتال حسابت رو شارژ کن
🅰️
🅰️
🅰️
شارژ اضافی بگیر
✅
🎁
20% بونوس برای شارژ با رمز ارز
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
همراه با درگاه‌
#ریالی
#RomaBet
📣
‌
#بدون_احراز_هویت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
16
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/22946" target="_blank">📅 19:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22945">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zjwh9ZsOS26doBb8Am6h5R-Qv9N5RjWyY8ejGS7QtDeO01QwwCbad2U5ltNSqg8adGb7YYPw_OQjpq98tSipOw1stGhQl9w1YX_lirDfW3NlBDnt6J0QAJXvw3N6-9nDPPl-_eYyblywKpyTgtaeHgpr2VA5blZ0DV1Q8ps1ULzlnlJ1GOF76B5nXLPte4ERFEFSJg6oe5oENQoPWdvLRynDK5YIBp-vGQSUUWZvpeQ3KyzsxOM7PqfDFKTqbpnDiT5lO_qzM5xF5eETmYpzeQlF71LmQ67uu5jfr6dppYtI331ghS6FkneN3RUCvu0lwvxEPzunw5nzMuYDs4vG9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ترکیب‌تیم‌منتخب مسن‌ترین بازیکنان رقابت های جام جهانی 2026 آمریکا؛ به احتمال‌زیاد این آخرین جام جهانی این یازده فوق ستاره خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/22945" target="_blank">📅 18:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22944">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZePzDdby3EhFWEOxF2K5f7TeI4XBeEFlN24sQW9iMawxPT2tchFxBMs4gik9YaNjNgED9XnOaBeTGQrrvaLyXTp9vyOhKUKN_fRlemHHI6CX9KDBfmv2y3fZlcJy1uRL29k-MHfe90UCnnwvjqb94HHpXwn8VFyHLyPn0MhwBFPwoKvpM2oZqvnTjQdTwQWAMyBFr6MzeRa5V8KyW7GD721dxk-NIhA5UYFkeNgAgtmeWaDfSjDttdffkPHlszGfYNGeEcVRHGb0De1lNq2oVBqsY2wQkdCeBPQoIWPNWwAw5Ocb_jIHANse7JHJOl1ZPxoL1kScx2xcBG-EYoijA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: منتظرحمله‌این هفته فلورنتینو پرز برای نهایی کردن قرار داد مایکل اولیسه از بایرن مونیخ باشید. پرز قصد داره به هر قیمتی که شده فوق‌ستاره‌فرانسوی باواریایی‌ها رو جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/persiana_Soccer/22944" target="_blank">📅 18:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22943">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHly0IILeiePF_qCHBD4SRbb9Rm3urhHobK0ors47cB9I8QQvBepAliO5wsyqpdUFzNFhltqt32zv1QIgBgV_yKtTpQQ1NwCgTJhOMnDyaqiXGu9X_TkqTpTflW5YhfVvnQzRVWhorzEnwfhMX4MgUnyJ2VLeZg6QX7dZMadjSiU2kR0lpm5zPJQRoRrcJ5ldkuxTOOYKm0lPEpw6KVmykMlI6l9ljLmolS-5l1SifyNnv95zp8KQOD9H9PPWnFgtXJL_eJvZgI2mMagS0bbeAFr79NL5pzjoTE0npFC3GiiciTRK2-VRLH8qeyvqefG25hTwehdCDKPQky0bp4aQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ انریکه ریکلمه از پس پرز برنیامد؛ فلورنتینو پرز بااختلاف‌آرای بعنوان رئیس‌باشگاه رئال مادرید به مدت چهار سال دیگر رسما انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/persiana_Soccer/22943" target="_blank">📅 18:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22942">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ebed3078.mp4?token=sicwJ6XRrYTPdKE3leVthno2oNtLtV64FifYGqduBnaRPq4a9FMjQ2t9OtF0ElI4gq9V1j6oExA518h0NQp9WV1PG5azfxGNRc3GUnF0TFV9I2-8CAQRhj6Qz2iz8i-z8dmlPri-zVIoiruPQG5qao6YD8RwO8uvgO_aMLNGdJVYVXOHAjmjeNqVlJZFZsTZtrM2aQb3KzT1Nbp51TWl0cUEQ-5kFPoMuKdqwe_sDQCPd2ZPP-aqS3iPOUwkO6lAtfYjBTrr0CUDcfOUzUHFKqxVXTH1XLbwqLcjz9BRmY5AYfxFBfIXPxhGG61aSx27eEzm79st77ouGvCQisUghQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ebed3078.mp4?token=sicwJ6XRrYTPdKE3leVthno2oNtLtV64FifYGqduBnaRPq4a9FMjQ2t9OtF0ElI4gq9V1j6oExA518h0NQp9WV1PG5azfxGNRc3GUnF0TFV9I2-8CAQRhj6Qz2iz8i-z8dmlPri-zVIoiruPQG5qao6YD8RwO8uvgO_aMLNGdJVYVXOHAjmjeNqVlJZFZsTZtrM2aQb3KzT1Nbp51TWl0cUEQ-5kFPoMuKdqwe_sDQCPd2ZPP-aqS3iPOUwkO6lAtfYjBTrr0CUDcfOUzUHFKqxVXTH1XLbwqLcjz9BRmY5AYfxFBfIXPxhGG61aSx27eEzm79st77ouGvCQisUghQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظاتی‌از مسابقه‌کاراته‌معلولین؛ این چه حرکتی بود تو زدی آخه؟ چرا از روی‌ویلچره انداختیش پایین؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/persiana_Soccer/22942" target="_blank">📅 17:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22941">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-n7wNNqUz2oQks3v0F5Zm0KybnB3haXJNlAHOqHBg1LaHHONGaCgQmcgGXSKpUHCdiA9FzRnAXLUc9fXRRHSEp0r8QPdBgjG-4YIrWsQYaG4XAroy05o3YkiAqvhSyGwQzsy0FfMS2fLWVWyCMCb3w2-ozDSBxu2XA6U24GOIl0MiAsNg8Si-j_we4bpSuyQcILHlSuFCiDb4gRmzlTn-TPPb_oKfBaFwwdrrOs4vAGrHXfrY7YGPQI9o5t2OGTfctK7qlJlwlt18Ak-TYOR7xG1QzZHk2oHCjHPSbbZtMLboyJdxp7Jghm_bGWNCRPsKqAi0djslyPbZrKhp3IWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکورد بیشترین بازی ملی برای بازیکنان حاضر در رقابت های جام جهانی؛ کریس رونالدو در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/22941" target="_blank">📅 17:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22940">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzkX9afF1JyUjP2XblqhnlzKxxp9MMvVj6JCXbqln0RJ-yAuOsgERa44Gmt5_3GOnVzu1Ibxh45nChvzLR_JkDFearF4A5QRlYCQIHYedNSl_IJ3THg1RCwQayo5JL9YeW0FjLdxI7RswAxB2bzY_GYJ_3riLmDUKjp6Xvf0KoHfRwe_CQOSO7sY2Mc11s1EUUN0IyeRac_DwHOt8kWdyxv28qArW1-9Uz2jFZBjVP5DnZlG5QEYfmn5DtYwyK6_4sFTlX7U8d0ZkcAm4YEJ09lF7UXdazMYN5-OHzs6r90L2-_NeZYmoBmsw8cc7IpLUcoBEexaz4TqoFhmnQRE7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ مدیریت باشگاه استقلال به دراگان اسکوچیچ پیشنهادداده‌که تنها دستیاری ایرانی‌اش در فصل آینده سهراب بختیاری‌زاده باشد که درصورتیکه جنگ پیش آمد و اسکوچیچ مجبور به ترک ایران شد بختیاری زاده سکان هدایت تیم رو بر عهده بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/22940" target="_blank">📅 17:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22939">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJpOnoB_70ioQ34EcOzw6XXvOhoGCoG_7ZOe4YmWioh4jMWADJV7jNdvMikhCNsxgXsaYMPayCiqrB7UiIIl4RVV01mPyVUHjAP7zi_lzPtopQPVqq7teAoiIXUw_totezaVqImcUKj-7ARgtTGE5sGfkWLCqpEtdyrU1Xi_qmy937ywJe9FB6CpQFjGk-_QUvlBkBMjSDcc8OvlTxDBd5YuJeQQadWEh3nKcJm5G9tSykuu6fW64N-e3xBLPt5tFQ3gMsOzc1TAulABdh578DNwNILlhab5n6BnSvXHIxa24-1PUzPOaXG6OSJAxEobRM5U_RHGQbEImacCjRjoUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق شنیده‌ های رسانه پرشیانا؛ باشگاه پرسپولیس در تلاشه که مجوز فعالیت افشین پیروانی در لیگ برتر رو از نهادهای ذیربط بگیره و در فصل جدید رقابت‌ها به نیمکت سرخپوشان برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/22939" target="_blank">📅 17:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22938">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOoqj4OYUryczkD-XGCOhBBAt3-iIJYwAG0Kzv4mTiZDu44CyfT9ImW2bVTHGkUfMecrM-fhEPbuABeFNeE7xn6E8aBeNdH300rsqBkREGc-cwGGhZ6s7Tlcimr7ng2zX27zNn8KRDrDpkmrxB0GEGSk0q_rgPDxMMQQpIUzFlZLc24zXJR719OEqaJucLwgWuFIlyKh8U9WBcA-G6j6XVzBibitPzAEhXU4xhiMktWUw-Znqz5hz5N9S-YjkAGaeTB4o1gFc_nu2-DyWTnNACr3BdGETWn2OGxADWE5RVV4cwSSIb_aZTMWZtlsbPXkpsleVvnnxvgkJG3lBYdQyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
تا این لحظه فلورنتینو پرز در شمارش آرا از انریکه ریکلمه جلوتره و به احتمال زیاد امشب او بار دیگر بمدت 4 سال رئیس‌باشگاه رئال مادرید خواهد شد و از مورینیو،کوناته و دامفریس رونمایی خواهد کرد و سپس روز سه شنبه آفر 150 میلیون یورویی خود را برای جذب مایکل اولیسه…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/persiana_Soccer/22938" target="_blank">📅 17:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22937">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca0d90aad.mp4?token=q_9e8d6dLF-tYBAGP9xMgFy8aIjdhF-yB-1cZEOgpFq_q6FOMzoC04Vh8FrIWEQlfwPoPhw2dw6J_koPVXmVhIOxv7HhPpU4e6SjMY8hylIW2umJrYEPvbFyoXOJ8PRtA0e71jbgW4E8rFfOyD-Lg9c6Fukmoj4e96X9sMlRyqcwW4ZxH8TUDEBN7QG11k7FrWeP0hLrQ3FZdjIDT-FhbfqgJhw6M45LcD2S3b5KX8uWZUH_ZKutq3xXsT44Kg61zpGfpfJegOLtznhxhk1IgDU3ypeDDK0m_MQ1W4kHmihH5-8TwKhKEkBGUVAiwn5q6eF1q6L6qpT1ELGYZ60a7buQpaLnH069WTdS3o1OPcm5mGVwoiAGfghO_qN5VQxcJUMIekf-gb1eunHBOhT9E49vJS3UiwuaWCyif5CmDLiaDCgGqWDNTn7iL6srnX1nPVMn238Zze9y98AwxcZJgxd20b4zEPPjqVT-CdP5zhRwUsnsqaQLm6RVBC9pnKAdhlgpu3QDxGkEMwKS0fZN7bIP46xCJerw_YIMX0avNlVmW_7rSYkE_CtB0EVHukOO_2xGwiNOKPvpYTwMCVacTTQWwfskQgIEuH-uk2NipmfFbbn1FWFJoWMaZq0jHBZHMhClOElvWT3jkYt3EclbluY2MjvUeRZ-34RgtXr9u9k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca0d90aad.mp4?token=q_9e8d6dLF-tYBAGP9xMgFy8aIjdhF-yB-1cZEOgpFq_q6FOMzoC04Vh8FrIWEQlfwPoPhw2dw6J_koPVXmVhIOxv7HhPpU4e6SjMY8hylIW2umJrYEPvbFyoXOJ8PRtA0e71jbgW4E8rFfOyD-Lg9c6Fukmoj4e96X9sMlRyqcwW4ZxH8TUDEBN7QG11k7FrWeP0hLrQ3FZdjIDT-FhbfqgJhw6M45LcD2S3b5KX8uWZUH_ZKutq3xXsT44Kg61zpGfpfJegOLtznhxhk1IgDU3ypeDDK0m_MQ1W4kHmihH5-8TwKhKEkBGUVAiwn5q6eF1q6L6qpT1ELGYZ60a7buQpaLnH069WTdS3o1OPcm5mGVwoiAGfghO_qN5VQxcJUMIekf-gb1eunHBOhT9E49vJS3UiwuaWCyif5CmDLiaDCgGqWDNTn7iL6srnX1nPVMn238Zze9y98AwxcZJgxd20b4zEPPjqVT-CdP5zhRwUsnsqaQLm6RVBC9pnKAdhlgpu3QDxGkEMwKS0fZN7bIP46xCJerw_YIMX0avNlVmW_7rSYkE_CtB0EVHukOO_2xGwiNOKPvpYTwMCVacTTQWwfskQgIEuH-uk2NipmfFbbn1FWFJoWMaZq0jHBZHMhClOElvWT3jkYt3EclbluY2MjvUeRZ-34RgtXr9u9k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اجرا چالش فوق العاده سخت ورزشکار روسی توسط یک ورزشکار ایرانی با رکورد زنی روسی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/22937" target="_blank">📅 16:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22936">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6gCaC4-YZtUZhvHU8FQ6AXoDXtYL_TvXcwTHvyMYnilnXHuuuXQhmfGkgNjokOFhcJkBd14ICrlavWg7mZiDz3vJVt2SMmwy-MXlImOcgJBuryZIiBSLBE1EyQkEHFvwuS6BIIbVfuc1L58XeQcZodeG_cx7lrvwSaju8drVhwxCruHjt4lpBEEJUkopBnP-Tr9knSZ7jB403xs8UyyXDS_VSvNVUxYa2Atn64z0HA6pELtA_NPsr5dbM6vRqA1SNBdNn-XOdSIbCPUj8ituD5Ki5o5VdnI2JDXvsIBid7O80V_TEhPrdFkIlF83tXmMcPQfg1uL0nEpF5eqr8cRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات|با اعلام رومانو؛ دوشان ولاهوویچ از باشگاه یوونتوس جدا شد و قراردادش تمدید نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/22936" target="_blank">📅 16:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22935">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lax9yhjKNL9vJ_rldEiGHvr5zW8Gq9qoZTiGGwjt0-BqE9KGiVEQIvh5wMpkvYPmjI77wipqWd5lCKHUh9fJsxhpEVfbV9uGgQWU24WmpqF0udAaHM7_NDRNZBQrNAWxXdzRHWWPDnXsycTjhJCMiskVQZ6vq2gwnSRVImDb1DX1GIWTfCWh4moLC7beDzlben6Y4hmakti5qd8yigLXiBKsILU_CHvHjI3oGkapZU-ISbsSDj_dfYUwCA9jE1pCApkwWTV_F3PDOqZMPKqAGzjaDavK3jeO7yjlYzxpHG9DbhiTLx6GDPuJ3k7IlFk8MBWhEtaRTvW1ymSGCaB54g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#نقل‌انتقالات|گستون‌ایدول‌ خبرنگار آرژانتینی: با جرأت بگم که آلوارز درنهایت از اتلتیکومادرید جدا میشه. مقصد بعدی آلوارز صدرصدر بارسلوناست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/22935" target="_blank">📅 16:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22934">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGb4bf1aCCyq8tuGJ5mvYk5fT2TvU2YIOv3PTNnLs_2-y_Z1atgivEOjM_MWkpPA3HQj-fGN5RgYrq0VXXKIEuFL0rkXHttGTH5pkqyqTQzdmEDVJ4NODfcCZltxY3HqhAHHYBdTu5N_glROUyDovTrL3QoAK5i-sgLTK9gURw6EeMIMGFY-aX1kwPhHHQaR-vybV9arduGsVX4eVwbWG5j-L1r12oU5LElUz0EXKWzMMEMXLtsMYwKyloxJ01OetbKSbKVAuYwDmhQ85x8HM2-90ImFWPJTsye5urEOXgIB9c_BZTmt0mERtma9sVuQVdGkshcXk5ogMXbAqF_FZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
تا این لحظه فلورنتینو پرز در شمارش آرا از انریکه ریکلمه جلوتره و به احتمال زیاد امشب او بار دیگر بمدت 4 سال رئیس‌باشگاه رئال مادرید خواهد شد و از مورینیو،کوناته و دامفریس رونمایی خواهد کرد و سپس روز سه شنبه آفر 150 میلیون یورویی خود را برای جذب مایکل اولیسه…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/22934" target="_blank">📅 16:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22933">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139c25f87f.mp4?token=XkARHvqKBgZkA05ewjraQ5MTp94QtQjnNjc1iI3JMkQ2cHMu-rsr9XOPBdOwisFiInSU_uF0oNoK7QhtyyBlAKOj8w23wLhcwr9jl5Q_eJGE-UwPBMmGBY_2fSouINCnk1WBsf_9DsrNQqFScNvMZ32BbOd8RkO0B9LrV8ZD0NZ_xeWmY2RtdsNH4CRL40BtxQEqZGGnLe2v2DQzzP4gucWqPvWHxwxjU-2sQQnEEzAPYWTqg2uC6VLE-8vphzv7pY2M5gcBy3qgbDc_nl48rMVIe3sXnlGgWZEC1vVezgHIKPGu7nLJRx-_9AGB49lx_BAAf-hIZM-I_jdK6Iz-Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139c25f87f.mp4?token=XkARHvqKBgZkA05ewjraQ5MTp94QtQjnNjc1iI3JMkQ2cHMu-rsr9XOPBdOwisFiInSU_uF0oNoK7QhtyyBlAKOj8w23wLhcwr9jl5Q_eJGE-UwPBMmGBY_2fSouINCnk1WBsf_9DsrNQqFScNvMZ32BbOd8RkO0B9LrV8ZD0NZ_xeWmY2RtdsNH4CRL40BtxQEqZGGnLe2v2DQzzP4gucWqPvWHxwxjU-2sQQnEEzAPYWTqg2uC6VLE-8vphzv7pY2M5gcBy3qgbDc_nl48rMVIe3sXnlGgWZEC1vVezgHIKPGu7nLJRx-_9AGB49lx_BAAf-hIZM-I_jdK6Iz-Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
آدریانا اولیوارس مدل مکزیکیم رو بدنش عکس تک تک بازیکنای جام‌جهانی رو چسبوند و از دخترای مکزیکی دیگم خواست این چالشو انجام بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/22933" target="_blank">📅 15:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22932">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icyxPyIMZLXOhBnszi35S8RatgFTuemTgjKWycB06ecJQF1CE7oE8D2uRfWfpGq8MPhhghIAOGgio9DV2rzWJ6FTB540MMUaqEGO2JEM_tIQof5YYfwZxdNP2LUysVdBz6_uZnKc5gKePympxw9b59Xfgon_4LHOh56rXpAdGv-X71IV_fOUQTaqOjmvtVwwBTe-wXCQThNIdBhoNQwRez4tEuin8y6_QaQM2CxdOdvzLrYsbx1uH-4Ssfn-X3D1cIaZfvGIXh_8Mr-dEsZG8o4G5FUqN0YKxB46OtkhpSA4aUvL_loQA3C-oglqH337dZAmcosOSOLc0HmTTQ_w9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
انتخابات‌ریاست‌باشگاه رئال‌مادرید از دقایقی قبل شروع شده و تاپایان امشب هم مشخص خواهد شد ریاست کهکشانی‌ها به کی خواهد رسید. شانس فلورنتینو پرز بسیار بیشتر از انریکه خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/22932" target="_blank">📅 15:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22931">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cu3cCPiB9biljzNroIHYzHyC89wbuPEBbARpbRLYq0Cm5gWvEqqkZeJgaq7ffeOaeEfH9mNTmxEczRW_zWx0HQs-8YvIYax3pjf5ISUkGWbpQywvM8yIo5k2EwzpKvK_-IllC1THLR9aCGvuHkpsixcGG3wKaQot2TsSSFyygcGDSOm3Xvn6BMz923GtXYWcr1Q4XwVKRkcV7OyIVS9srylj4oVSxs1oIse42mqBP-s-ktKnM5DgoztYdCYE3qhi7bGk9zvuYKT0zvpCjCfELURJ-uo07tt2J4dwGqrzqUmWhQuYgS-JTNpZzTNGzGDVekZMfRt0n1EPY3zTiYYMGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال خطاب به‌تیم‌های خارجی که خواهان به‌خدمت‌گرفتن امیر محمد رزاقی نیا هافبک 19 ساله این باشگاه هستند: 3 میلیون یورو پرداخت کنید رضایت نامه این بازیکن رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/22931" target="_blank">📅 15:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22930">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvhkRFYyRgNlK-o_v4rpmEogdBCaM5gcd_UpFF7oQKzr4yzAQiG2BGm10gp7bc2HdalE6he3RQps4PrRds9vH8yfH0rsux6Sw-H3SO_F3U0s0I7MdKFRAMKQT_9e-GRjW_Dw4jUxa7kVxwA8I35fj0BjhkAREoBPfsJ7zreTrz_j622H3aocOYow6UXGLBsHUi5PV6ZFWCG0vmyq0qXEVGlVCvmjRX3Ci9jAW14xKmdmx2JsG2-Xb6xkjSkYshK8j0XVACLubgK_DCz3h-2Ehslj0TRxqsV7qOp1A7mtXjiagi_9MCd0Pxbd1z6NmQeoBWYGAB0iMkUleN9aBU5u-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
معرفی دو تیم بلژیک و مصر برای رقابت‌های جام جهانی؛ جفت تیم‌ها حریفان تیم قلعه نویین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/22930" target="_blank">📅 14:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22929">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZl1mcDoI_JdnFB42XtXrYojR63BnVD3abjvllFIOeXuNhAFgQunmic6pVr0gK64ccnsf5_4FSr1ydBWXx84W6axrtVLpYdB9LBBH9f09pnwj7d46I3I7voEuSpPNRoG5jeEH81E--R0LoLVI9Z0cVg3XZCgGPwayf9SApwvGJINzcIXbuQltH3arXKpkkGclXCTsuejlzVeWmEL531IAuiopnl7e389Z1o9tLPQ2HGV6KRvG0WBV7pd69s0pyOy9esz8u1yWr-cwHopVPT05upQ78bYa7uhWTZmeMiJZqhv8u7ikLV36-XMa90qn-T4uVisARe8T_e3MQAeixzgXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکورد بیشترین بازی ملی برای بازیکنان حاضر در رقابت های جام جهانی؛ کریس رونالدو در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/22929" target="_blank">📅 14:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22927">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fq1YDIVfOjXgt2_yDpN6M-hVNnKckgY2c4cViBNErqKiXb5aRM9AjPyaiGGHJU-ME-ADEQ7OYm2jpQy1OUCGc1j7MJWliiQjnj_1fhM3IcmEPItjgmvLoisopdWOSaTISVMjFwayNhNJC_zMkFk9DtvwQu7NfalD-Wu0d9x5nL_oHjhhTdGAe7peTw1KPDKShMBsQgPwmUz07zq8GfJk63bSLkzXgP0ziPGZ7m4pTEAWhzHkNibcI_mQJ7GP72I2dqNe8vfhdSfWtFSPgr-d9HHOTX4iDWhKuhwT15MPuk-eXvrEGlcsj2hD71i9fk53ErSnZ-p-1bDQOsrkg1XJtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iGpnqHYCr0dQ_DyiXnVBayshFJ4LuhoXSzR_Jmq5XbtBGnpuNZS7j1bxhDoNQTlHh8KlEqVDEzEmk5eDE88VHmutflqJemHm7Zitez9Yf5WlTFz23jy8UvM32QsqgzHIJcejE0xg_ZFym2zoA8Y9-zeT3_I4KlDCURbGRzU5_8niK2P_uPNcliZ1U9-0TVsJdVuoxVYzi-ndLem9TzXeagOO_5L6VHmX-q7lTWZivqqqJ9eVAN4U1T42QaydtBmaKPWqGWL42XHYROHukcXmf0UdqSGqguyRueCUUCL4LxCh0VpUhP9TYJVjmkmKXIiDo6PkCSRjosidSPTBMa2XOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
معرفی دو تیم بلژیک و مصر برای رقابت‌های جام جهانی؛ جفت تیم‌ها حریفان تیم قلعه نویین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/22927" target="_blank">📅 14:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22926">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZRbNBgpsVD2311F6i1IL-lk3Lj8sYXnf0ZdZnM_1Ox0PBmhYOJ7cecOV46KNXdqTsoNjBkJXdw8y3GXCKk3Q5wNa_j6Ju08XGIyU_pFvmK4Z7qwgYeUm_URcCrzTcs1Xx15hZOZkOlW2xY9MkJ-BUt0lw-De13pVs4LMw40LZR0pegjeDF-dFSTXfEqRvM2rnXZcn7WIh7g-qr3l4sRqI2f52KrLWJrCmNp1y4X3uFf1G_VIVgQl5GopJSXoooJY6HyZ_tweCxB-Uhyx0ItutGmQVPIZsuMdUJS6xVFdMkPWOQgDa_APUAtFqwcdJya1eP-NKcXku2BrX77pI_low.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکورد بیشترین بازی ملی برای بازیکنان حاضر در رقابت های جام جهانی؛ کریس رونالدو در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22926" target="_blank">📅 13:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22925">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/moUtooTgecRiJfSZkBFiXpQEe9gpqP-n619GsI_RbrUGl4ZJuJ66PQ7uZMXBG5XALrjO7RelA1AIN4IDJbu3AKo6ijWnId5RA9o2Ns97yQKTny-huZMcZGf6hEgYg0W2J-lcAcj_vJHFI9wL-UEUdaB4JO5q32zAh4yxAIEuDJRPVETWBzQXZ1Y1ZhHzVUvM5kaWpG85VvO-PfiLJbR1xT8hyWkrW_jRsX1X4MmvsqhMOTGZJNEEaZlSTKzNuM3Wst1wNGg2DC8JhrD4_dyKkLnKOVMfv2p5_8Acxed2WUYd-Vd0FwWqWAGSQ5ruU1e4F0QRmNa_6NEglyAeH7uvhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادی‌کنیم از این ویویو بسیار قدیمی امیر تتلو درباره استقلالی و پرسپولیسی‌بودنش در زمان‌های مختلف
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22925" target="_blank">📅 12:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22924">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYFOij0AgEd0DxBV4rQUdrdAcRzSvtLbM9gaFcBQMcJ5mbeFgMfpmKd0-tXrnARchmxvWoaFoga4dLvyXmELkuaTZBl7GlvhJmS6lhQE2wCvdyBuBtyA9bfBVNG5SIq65mObeqFZzuHR9WHQdob19IFGfdoznqRiKDEgADVb5Jc9q3RFRinpbkh6kYC0kfz0BrHwta2zhGbWKlGSEiwNYgVZsmk7HH5BrMJAltrndrg1vGhRHpGEebupPTkm2OnG2R51T1ZKdhhUYWMOT6I8MRt-F38oF0eqwBKbQzyKt1niIn8Yym4DP4xLcLUmWeszpyxQIdr5ue0SQOcb900LZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
؛ هفت سال پیش در چنین روزی؛
ادن هازاد باعقدقراردادی به‌ارزش بیش از 100 میلیون یورو از چلسی به رئال مادرید پیوست. او در طول 4 فصل حضور در‌این‌تیم 76 بازی انجام داد و تنها تونست که 7 گل بثمربرسونه مابقیش مصدوم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/22924" target="_blank">📅 12:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22923">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a46a056081.mp4?token=JvFX29dfyr3k6eZoNzbbizD2pHcgYcYd9ObKJf6fvHB13GErjG5qDn9Sqq4OuAI9uJUEA1Rbt--SICKN-knnrdtWwgMhDodGpR-vVqnwfZNdU876nZ0Tg_bOoCMa6IzIOH0i5HTbECln6_nEyxurW0S53VZAKg-6h-BCJWHeafM3Ep8rg_QnrPTznprIHv832X4H7hX-Gv_h0QgxMBHl6YUaKVhxGDcKdM-atWTG9U7kqRNrVAdBmlHVe34BDy1aiIB1rt-6khjRGSuES_fVgL36QMidInK9Kf9WdBrGuykFBRIT7JDoDnVAw4nkgR4QIxE6fFlOxW4JZJhbKHYHWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a46a056081.mp4?token=JvFX29dfyr3k6eZoNzbbizD2pHcgYcYd9ObKJf6fvHB13GErjG5qDn9Sqq4OuAI9uJUEA1Rbt--SICKN-knnrdtWwgMhDodGpR-vVqnwfZNdU876nZ0Tg_bOoCMa6IzIOH0i5HTbECln6_nEyxurW0S53VZAKg-6h-BCJWHeafM3Ep8rg_QnrPTznprIHv832X4H7hX-Gv_h0QgxMBHl6YUaKVhxGDcKdM-atWTG9U7kqRNrVAdBmlHVe34BDy1aiIB1rt-6khjRGSuES_fVgL36QMidInK9Kf9WdBrGuykFBRIT7JDoDnVAw4nkgR4QIxE6fFlOxW4JZJhbKHYHWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
وضعیت‌‌آکادمی‌های‌ژاپن؛
قشنگ‌ مشخصه دارند برنامه میریزن که یه روزی قهرمان جام‌جهانی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/22923" target="_blank">📅 12:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22922">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKnxU1o3xGCGkeus0PDmo-Vm-nH9h0ktOfQnd1Wu7ujFzwI1BtMayhq98EAeE382smq_RaiHXnlcyWjfmlX5dBhMT9cN19xhtzglL6ktj5tWc766Zczz846iRA3Gk1KiSd8zHap8qi3rEi05LzMuXnCRQzU_7AFVP_13CQgSQcFDiQzLZpUbmVAEVqBkXBCOLvZe-lJeWDeZ1kBSwPViW30E6qh2zgztLko054Voxliv3fxInDZm6cs6D99i04NpFvelBsB4oyyIoCJwTnXRgLVXyghaqSouGHIMDwwsRIb9UgAq-vkG7gcj2XKz_sYozNT5NzXrouLPWbr47pkwqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ حدادی مدیر عامل باشگاه پرسپولیس هفته آینده جلسه‌ای با مدیربرنامه مارکو باکیچ برگزار خواهد کرد تا تکلیف نهایی موندن یا رفتن این ستاره مونته‌نگرویی مشخص‌شه. باکیچ علاقمند به موندنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/22922" target="_blank">📅 11:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22921">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad2a01aafa.mp4?token=n3OgRashE32iQ5Kt0TzVA-6iyCFhjq-z0wbAAUPrgMJH8ID95-YevPfbS6UUmMzWsDc54Nwq6pK2REdzeAoClbEhp6S9JFvOMPoG5Qfw1j8vENjOENjU-d6fGDa8Fe1ns6dtp2m7rSDivnpJYBEY1z3SkMazkd4yB4s4V3rj8-aTVf1T0KS3tspyruSNAR9gQ8-ZAd0SHbhU8BDHxH_ktgNPxrDwMbN1kMZUGdvAX5XzJCF3ptqsH-OF7xUE6_PYdrtEmDTyp23rYzCOlUI0XjualbVtrmHrEPc2zUd9BNLN6lJR95_6olhd5_Evh2bYPOC09wwFaCaTM9ITNSt8NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad2a01aafa.mp4?token=n3OgRashE32iQ5Kt0TzVA-6iyCFhjq-z0wbAAUPrgMJH8ID95-YevPfbS6UUmMzWsDc54Nwq6pK2REdzeAoClbEhp6S9JFvOMPoG5Qfw1j8vENjOENjU-d6fGDa8Fe1ns6dtp2m7rSDivnpJYBEY1z3SkMazkd4yB4s4V3rj8-aTVf1T0KS3tspyruSNAR9gQ8-ZAd0SHbhU8BDHxH_ktgNPxrDwMbN1kMZUGdvAX5XzJCF3ptqsH-OF7xUE6_PYdrtEmDTyp23rYzCOlUI0XjualbVtrmHrEPc2zUd9BNLN6lJR95_6olhd5_Evh2bYPOC09wwFaCaTM9ITNSt8NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیبروین یجوری به تیبو کورتوا پاس میده که انگار هنوز از دستش‌بابت دزدیدن دوست‌دخترش فشاریه و میخواد کاری کنه در تیم ملی سوتی بده:)
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22921" target="_blank">📅 11:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22920">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22920" target="_blank">📅 11:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22919">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okeDmGPSsnfqlz1TZJHa7O4wjFo_t4dttwoBH1LsumkFzCKGiffhsB76nIyI-FrV57MfqyHkKegCYw9QmQORBlt-b-GzixJbRC_5PtkHVwOTWVaFnEjJMbDBS55UDD6FEsEBQuSIVfYZOaWPqu2MXvmzErCNQ-NtR0bQ2pzBM1gOkEdC7D2h5prblUJ6lh_KOr3S6sHdDX4zLVsiAHnbp4ddDZE7Yd3gTEK800xrsnpCDIImcU91pPZu3LQtg3VrT7WCqu-zFdrF4VEd5ix5IDlxPagQUUK-fjAl8G6npUCfUTBCgUQqYXP0tU3Hh4ka7-Q6NKEM4p4fluZkmtaPMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: با توجه به شناختی که ازفلورنتینو پرز دارم به‌احتمال 99.99 درصد مایکل اولیسه این‌تابستان‌باهرمبلغی‌که شده به رئال مادرید خواهد پیوست. پرز این قول رو به مورینیو داده که با هر قیمتی اولیسه رو به برنابئو خواهد آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22919" target="_blank">📅 11:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22918">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t21qgX5LTokgLK3BRgE2cgPt70MYznGmEjk9d37uQ62KhmblNZmdbFyxdA5kyLhM0QFEFZAZqKdS8SMD7yduqxmhj-bvZH7nHvDTyUhtgNrNpi39TrUNhD9Lgg6-O1E6XeY3wN_-Xb2dIUByj045L5pvDt7FlOXqKP_0HrbpF_7Dm3T33bUD0KRuhe6vXLs3MwdPao98UwuaDHRpfAQvI0mUXRqDUS2OS1U2P443gMLrtEK176__cE6UHtLCc9k4hc8Y9GSg1Vbdh-nRq8JikDHQyhDjPlfBFsQymzUbkI4jOOEQucF_fVWH2unV98rIy8qS8cFVhL1SEpjmhNgYBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22918" target="_blank">📅 10:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22917">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d705d6a743.mp4?token=j_Gzgp3T-pK-Hd-aNx_gTryRYWXxA0k8sc50UjzXq8qsQjph0RrKwoSWigw0kQla3heN0Lh0VtjH90yK7XIpJBuNoaARjTIThT5fyU-iKSsjleSqh4TaTfe9TAFe0HdsRPy2w5xm9pttjsxC1tlTMrNELy1vTLu4gK_6MvKaM_IF7Mwao_hjFQAtdpeKTM1LPtJgAsHJ_SFxSKeNunr-YTBM8ETeCZTcoCzw_-0PcIWU6ebSEsqjm1vZQYBa-YGiv0kVE0h4l9YVFG0aZPRM4BEVRsCcE-e6Bt_W0Ez0k5ZIZxBbjebIa-l48JjLfIpodMVLTO8956oNVpPkb4itdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d705d6a743.mp4?token=j_Gzgp3T-pK-Hd-aNx_gTryRYWXxA0k8sc50UjzXq8qsQjph0RrKwoSWigw0kQla3heN0Lh0VtjH90yK7XIpJBuNoaARjTIThT5fyU-iKSsjleSqh4TaTfe9TAFe0HdsRPy2w5xm9pttjsxC1tlTMrNELy1vTLu4gK_6MvKaM_IF7Mwao_hjFQAtdpeKTM1LPtJgAsHJ_SFxSKeNunr-YTBM8ETeCZTcoCzw_-0PcIWU6ebSEsqjm1vZQYBa-YGiv0kVE0h4l9YVFG0aZPRM4BEVRsCcE-e6Bt_W0Ez0k5ZIZxBbjebIa-l48JjLfIpodMVLTO8956oNVpPkb4itdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جایگزین تشویق ایسلندی رونمایی شد، تشویق وایکینگی هوادارای نروژ؛ تو جام‌جهانی اینکارو بکنن ارلینگ هالند جوگیر میشه به هر تیم 5 6 گل میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22917" target="_blank">📅 09:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22916">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0rBoKmDsahUAsx6lmB7bdQCob-TLx_eFd7mgTDlgw2niOHugjpEy9Q9wYsZ8AHKMkW3ogL-umi9C5ETLhGnfWBRG-r7vLRkz0vrgoUlSEQpfZiHvzSo_5i9yp0JyXF4RHIgoTHFCrxmdLvW5rgmR8Z5EXFmLrZFr0GJHXG1CMPAZhqDmc8tEErKg5CHlbqD61FFUZzBvzB2ik4m2v9ltCzaSas-Cp5scyvpEOtYBQEpbrNzDW4HdtCMJ_nHmp7cF3q9mbUqYS_xiBGS51hgXHZPnwRN6q3xEkn---LtTtp20bIlqcNB6BUudYePCyFv0rXE5k0h5oD8GIeNe_1zPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مصاحبه تاریخیی کاکا:
برام مهم نیست که بچه‌ هام بدونن یه زمانی بهترین بازیکن دنیا بودم؛ فقط می‌خوام منو به‌عنوان بهترین پدر دنیا بشناسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22916" target="_blank">📅 09:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22914">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HtifistF-Suma4gY48jUyYxHe3YBZLs-BzZqosDKcP-RcmYiDRVWvcAxpbVnrNfC4TdNpfabINQO0Hpzw5-doPASvCBagQf9ckDzwzCgwbJCI4FjnwPIS5Y1LSKeaV9BIwSZj-OVoOMBgp5WA0_GrfPqdjfkhfwnVug88JnoEDli6MN8HhH_kb-rrrmkwV9Zm84lXL4BX6t3wvAr3YCqZSGJyv78ASlwRvzbzoWWkyGzfBUFEcxvv6fMxzKqsfPIvhYAAq2OvuFzWwRVTwihGhFBBlpjBym6y4UIUA0fWG5ycN-66ReUcKGfob9Br5YfrMn7idfyj_aOVetl7eQ4QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌دیدارهای‌‌‌امروز؛
تقابل شاگردان کارلتو با مصری‌ها و جدال یاران مسی برابر هندوراس
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/22914" target="_blank">📅 01:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22913">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRrktIR7x4WE2S3YS5KliW6K2Pf2e6F-DXuqhvdMcsxP6IsmbjukKTfOghBRHamUi6ArosSbL12R_Y95IUL3dM8JD2DT5IfABJNSbMtb6AJQwm3QMmELfxREyoaBLEAu2TCmdfnnRnT0bEEzS7-bgArO0KrcNdy4ZSfqm-CJ5095QgTLdRx_s8-kJiHCqK8-VAW6Fa_8gL09HctEqKQNvcWKYz0hwGUbq-Xwz8UKM2ueENVXdQwxGLdjoXhf7cj5RF_xJPjQWlmVH5WLckcJ-J0dqpcYNByWb62AKM2UmpkzFrANfsYR4SxnL8aXNLvoutH4wm3gOQ73DKAtzvX-HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌روزگذشته؛
از بردپرگل بلژیکی‌ها مقابل تونس تا برتری تیم ملی پرتغال برابر شیلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/22913" target="_blank">📅 01:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22912">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvLLkO536MxvJoQ7KU1-KR4WS0P02LRidK6-ZYsBtsgBCJhqzJftDuuasfmZFnYate8GFC39tMDkOkTe60w7SwT0iCZvgUizLVue9KWqMKvUy391C3xyLD-9mTqrZeVBYAU6PU_XhrlKbY5aIwTY4X9koGNvWketwRmYd6Dy_2WL9UH1mnmgrYQS6gWkl0ptu8KOrlnGgR1Hqh4PxDinbXnRFg9F3pXM2_7_B6xV-ur_9d748Bn7me6r0JoKr9Wsv043HX8wcztNsNtESJil_ZM7yT1WKRpqfIbr0-mVp9aP43Zser5cAtAQOE7IZyfYpt_CCB0RTleT9cSHwP5Xnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ طبق اطلاعات موثق به دست اومده پرشیانا؛ باشگاه استقلال افر سه‌ساله سالانه به ارزش 1.2 میلیون‌دلار به دراگان اسکوچیچ سرمربی کروات سابق‌تراکتور داده است. همانطور که در روزهای اخیر خبر دادیم تنها شرط اسکوچیچ امنیت منطقه است. گفته جنگ کامل تموم بشه دوباره…</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/22912" target="_blank">📅 00:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22911">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc9d6ea65a.mp4?token=HmdcgGZgFDqCly93n9t-wZxRJA3BQBfq2r6oPNhR672mDwGC-ABPAFzqXm2vP9P-uVavw1lTlTPptN2-hW5XV4qMMPDddg1J5VHkQk0q4BknoO5hVFsZtMbtN25oZNDoPQ6SRPpCnPLufei68L_iX1iOLLv24luelnk8QgtBHPpu03nHbOvHA714E44wmeGRFPa5RU5_oXUxrVHQydsc648E4a0qnJOIIeF-4fPfwmcoZEqNpZtlVauNJXgSBQ8vjod--OV5X9pnn4IFHynXGvPwYYb4fq6K3rpXX4uHNIwhBPf-P_mBs5kxeBy1qiAQzYBFfPbVQvYE15Ztz9_HAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc9d6ea65a.mp4?token=HmdcgGZgFDqCly93n9t-wZxRJA3BQBfq2r6oPNhR672mDwGC-ABPAFzqXm2vP9P-uVavw1lTlTPptN2-hW5XV4qMMPDddg1J5VHkQk0q4BknoO5hVFsZtMbtN25oZNDoPQ6SRPpCnPLufei68L_iX1iOLLv24luelnk8QgtBHPpu03nHbOvHA714E44wmeGRFPa5RU5_oXUxrVHQydsc648E4a0qnJOIIeF-4fPfwmcoZEqNpZtlVauNJXgSBQ8vjod--OV5X9pnn4IFHynXGvPwYYb4fq6K3rpXX4uHNIwhBPf-P_mBs5kxeBy1qiAQzYBFfPbVQvYE15Ztz9_HAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصدومیت شدید مهاجم صنعت نفت؛ ویدیویی که روزتونو میسازه؛ فقط کامنت‌ها رو بخونید
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/22911" target="_blank">📅 00:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22910">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7334e55a73.mp4?token=MJ5146J0BxurMCBThaFCnfx8MLoRcUXMgo9DOhfk_ZGtQcuz7zKHyKtwIukqNDzz_m_EprBSbQ0kZDS-OCpoQNJUrIBF849KuMtYoWeZ--LYoQppgFQoKXMS2S36CYu-waC1ySkskAtcPZI7fhRBXRB7Y4u4cuRKGUf1DFRe0F6ZDlIoWxk-TQPVjpSMQiiHZt3nqsfxXR0SAXCSXvyLvCTnrSk572Ethk9S41zG6gGEZYpwRicesUtGPoRvdM7jHWCkvmBV1s-LbQMVxv8q6F-ynD5Nfe1YV8Mw3B-VgfKC0SsqAMkDJcx8FjYjpOvnFvY9qAFrmdzwYH-7xodFLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7334e55a73.mp4?token=MJ5146J0BxurMCBThaFCnfx8MLoRcUXMgo9DOhfk_ZGtQcuz7zKHyKtwIukqNDzz_m_EprBSbQ0kZDS-OCpoQNJUrIBF849KuMtYoWeZ--LYoQppgFQoKXMS2S36CYu-waC1ySkskAtcPZI7fhRBXRB7Y4u4cuRKGUf1DFRe0F6ZDlIoWxk-TQPVjpSMQiiHZt3nqsfxXR0SAXCSXvyLvCTnrSk572Ethk9S41zG6gGEZYpwRicesUtGPoRvdM7jHWCkvmBV1s-LbQMVxv8q6F-ynD5Nfe1YV8Mw3B-VgfKC0SsqAMkDJcx8FjYjpOvnFvY9qAFrmdzwYH-7xodFLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
امباپه27سالش‌شده؛هالند 25، اولیسه امسال وارد 25 سالگی میشه. اینم لیونل مسیه در 25 سالگی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22910" target="_blank">📅 00:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22907">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c2e44c05.mp4?token=oDCTpYDoJrvPipyPLoYf14I2r4YjKbSyxedtWOfe5-eMfgA3L-jajBhXkFZk4qMzx-JJJj-dovjAnlyp_lMS11iKrOkCK55gW3KSZQgkzSrmPRIewaZ3AFM35LiThBtWgZIz0NBsKLL-7o4OWxV_5IP6ScOVrVbr0OD1ergW-ZWiD2an-fdGHriL-nveMbWf8sUmYvKFiEdHRKHokKbvGtDscA4vaN7NU6Wn1wtw0TWqE7Ky029aio7KiM989gi55HacGb987KnxTr-NOvG_zjm437yU4oPINxi8xQ53p7vZitBaT4ehH5lR1V8OkcAWUjdijJgHhcUTcOgQe3Sw5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c2e44c05.mp4?token=oDCTpYDoJrvPipyPLoYf14I2r4YjKbSyxedtWOfe5-eMfgA3L-jajBhXkFZk4qMzx-JJJj-dovjAnlyp_lMS11iKrOkCK55gW3KSZQgkzSrmPRIewaZ3AFM35LiThBtWgZIz0NBsKLL-7o4OWxV_5IP6ScOVrVbr0OD1ergW-ZWiD2an-fdGHriL-nveMbWf8sUmYvKFiEdHRKHokKbvGtDscA4vaN7NU6Wn1wtw0TWqE7Ky029aio7KiM989gi55HacGb987KnxTr-NOvG_zjm437yU4oPINxi8xQ53p7vZitBaT4ehH5lR1V8OkcAWUjdijJgHhcUTcOgQe3Sw5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
وقتی‌داماد مجلس خیلی فوتبالیه، کریس رونالدو فن هست و به‌هیچ‌وجه هم اضطراب اجتماعی نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22907" target="_blank">📅 00:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22906">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/762477e8bc.mp4?token=pNkFsbAtCSPYpsk2zRnAcgMgAd9kRxusgvC44WnqOZO0zXlY1pS_HT0lG1DdUcmPtMT5ayCM1tmwmjAr5WfTf79Zj-bGqxpUm3OWljv860WpPVEwxzd94hhHr9oBMoWL70pJ6qfxWKZqzey5L4FGB0G35ZlF05ufzRawl0KmfpNytLCOYGfKtgWCl058WgYipF5DeiVblIT5r395-pk1aQ107hKshwyxyXMTcC_njNSHyqhzNvmKrDCMU6J3j61xztHpeIsZtsHJHk7ViH2DdoXDR6Td56PpTEkPKf4yqRH8BCYeMjEUYhoblrGh3xLMg24tfTZ8KdTas1plrQI1vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/762477e8bc.mp4?token=pNkFsbAtCSPYpsk2zRnAcgMgAd9kRxusgvC44WnqOZO0zXlY1pS_HT0lG1DdUcmPtMT5ayCM1tmwmjAr5WfTf79Zj-bGqxpUm3OWljv860WpPVEwxzd94hhHr9oBMoWL70pJ6qfxWKZqzey5L4FGB0G35ZlF05ufzRawl0KmfpNytLCOYGfKtgWCl058WgYipF5DeiVblIT5r395-pk1aQ107hKshwyxyXMTcC_njNSHyqhzNvmKrDCMU6J3j61xztHpeIsZtsHJHk7ViH2DdoXDR6Td56PpTEkPKf4yqRH8BCYeMjEUYhoblrGh3xLMg24tfTZ8KdTas1plrQI1vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ژائو نوس ستاره‌تیم‌ملی‌پرتغال و باشگاه PSG که در 21 سالگی‌فوتبالیست‌حرفه‌ایه، 2 بار قهرمان UCL شده، میلیونره و با دختری که عاشقشه زندگی میکنه؛ برادر در داخل و بیرون زمین زندگی رو کاملا برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22906" target="_blank">📅 23:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22905">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqveG-8xxhnW6hsMDs-V78OyDQkQN9VNq9QHJboaT63gEs41e8nOoGERj-9X1VrhNdGX1iB-jxLnZZgU-hQblMldnQ5PM08E37pBuQFPd5NuWPZXG42mBQ0vmG3j8SGuI5CkwfJv5HwyP_Y6WTA6whbQVx8J540N0WSlsgKFCpiF387aYZPYYQId4Dg6bVU2ZdNB9ZJhKU5KFfKtcIt5wPueLrmmXNOodzz30wJr0qgPGf2ykM4sZOf4Hib2ObRne386tchO2txNS2SWSytKd5ghfj_a4pC5m85xBaRg-1Q9uepOghG9tUdzaOjvOV0vm8BcdK_x1z1Ldwurlk9rZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇪🇸
#تکمیلی؛خوزه‌فلیکس دیاز: مایکل اولیسه از طریق‌نماینده‌اش‌به‌مدیران بایرن مونیخ اعلام کرده که بعداز جام جهانی 2026 تمایلی به ماندن در آلیانز آرنا نداره و قصد داره راهی باشگاه رئال مادرید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22905" target="_blank">📅 23:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22904">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7O4ED3dK706BpzIKC5oRiik3YNibmNFsiqwCTfpfm5z1fuRmcLhdBdLHBD9cxlzgwqHm-mOU2X8vHL4ZZACgLjbLxbzu3e8_dSGYlf2NWZIDxP3xALUWuJ7picSkqDaFAYAEXtYTyhxSkEJFGUFB254lx0OpPXgYlkzly7xfIS2cV2IIpPntYSFnZsO36F2-pVXG8JbPu6fbo_vrtrrqDhODVPvK7V_z9iL2dUhnCYSULGYYdWUoGZHSsGsUISuw_F_D4_d93js7WYozU6375ZXTL15mDxpbVMxoS4QW2o1VW_xeLISisiwT1KQkCEckducJYIPj_nRNuC7Cxt0Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق گفته رسانه ها؛ یوتیوب بزودی طی روزهای آینده بطورکامل رفع فیلتر خواهد شد و همین الانشم روبعضی اپراتورها مثل مخابرات رفع فیلتر شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22904" target="_blank">📅 22:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22903">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNTFTE-kkveQarPzAUL5fkR6lOzJXHBbWC1N85669ZrWqS-Dt1xDHqp51eDv1mXoO53bJRN0P7ZAVWzkPrsDXFdvdbPOPUSJjqQg0x2MFtVfBZokNYVi0YRd-iEoDnghsQrxTsXR2wD28VZw61jIuH6-OAN2M-Q22LguEvJ-rMSCBefUSomDEA45EgFhFhkWlHnU0Ya1o2NE-PBMjbtrrLKZpShRqNUSjaWKRQSGk45GjZQomXHXqny12qY5aETZTMmmA5307URjjlfhTUfdvPCbVyGJQT0nzy4IzM9vSwHtSCgM7rOnIlj01lOwp2a5mzf7-WlsIubMCxIzxRzftQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌اخباردریافتی‌رسانه پرشیانا
؛ ریکاردو آلوز ستاره پرتغالی سپاهان که با شروع فصل جدید چهار ماه از همراهی طلایی پوشان محروم خواهد بود به مدیران این باشگاه اعلام کرده درصورتی که محرومیت او لغو نشود یا به حالت تعلیقی در نیاید قید حضور در فوتبال ایران رو خواهد زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22903" target="_blank">📅 22:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22902">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lA17G-M-5lIZlaCrGaMk6Z_hXhmCDMy2g0SYcee28kb-zCW1_C40SkYObqlTyBqGYClIMHdZ6cEqAsJdhmXVFM0NcW57WAQNDbKc9Zl8-3_20t9GtztigS5xXwcGQbFcbfJWHTIqWq7brFELSnawwXxlD12UcPQnOk31LFGcUO0dkvKMPIv1MaecxzgS09azlSSYX6KJU9hyLkgQiGlDGsK2WUMQHzSnA__IoSiV0a5CFmxlbgUusxbeLLmszAG-UjvrnrpBQe7YGxipsnw5GD2zddGtrlVhUDBxrXjptaiUsTHLdFVtHQeV2nj5W7dX0bbJWyTXB4als0lwTWrXcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ پنج مکمل‌ ضروری و مهم برای رفقایی که بدنسازی کارمیکنند. هرچند با این شرایط اسفناک اقتصادی مملکت خریدشون شاید سخت باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/22902" target="_blank">📅 21:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22900">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C3jtGBace6xwh73v44FZULLaow-d-jmFmbIrdM3cd-PkWnhFN0P7_CtZnwe_rWfO7Ujoe-h2EDMvDmT6hZuTuPQU5FwU36xBtF1bbZAC0eeaR0cIRhjsiyeBdbcjNQyD_J0OQUNkkr55EmsZaQAAkNREW1cY5AMneO2r6WMSU6pXZ_qsHmnyf7GPPUE3TAB2JgYkcR4wbSFkbRT98rP9yNtAaSWXImlR4wIpB-srl6ymbtvgee3SCkfHehOT_1YFYT2awJNKgnWo42Z3vefvOKgnz-fFIFxEJzzVuPjIreWEBBn-KmkKZhhZvq7K3NqPE9RnsjnXoQXgyMJVAJhM8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ajlhPeOwnEYZqPfORdwXkeIJbKrSrC-jUlBWPuZr-GrV6PWCuETHAApSzIkJH21sc587kBC6HegkfW4Xh4Fxwn0Ly47LoV70jCDWu3YatdfMwMmvlztcko9Wx3-FikMtO1vvgCz0Ez1K7HD3X34_LHXICvC56pKQm6EJRTAuI6m03dh5NXrF7YYW0M9uLThcYHDqSJSuCz-f4NJ6bRfNG5QFY99p2WggLcEXZSbusSn4l5ZlCZSCqCoPj6G4c3t1AeXexLgYfqsLG93ry_B8_iGyJwt_9PZbZJ0M4uvN-yGzZk4AJ3whHCu80jtwCjgWLIcNKqRgNwQy9BMKHRBlcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
بماند به یادگار
؛ یه ریاضی‌ دان آلمانی به نام Joachim Klement که قهرمان سه جام جهانی اخیر را با مدل خود درست پیش‌ بینی کرده، معتقده قهرمان جام جهانی ۲۰۲۶ هلنده.
مدل او که عواملی مانند تولید ناخالص داخلی، جمعیت، فرهنگ و رتبه‌بندی را در نظر می‌گیرد سناریوی نسبتا جالبی را پیش‌ بینی کرده: تیم ملی برزیل در مرحله یک‌شانزدهم نهایی توسط ژاپن حذف میشه، آرژانتین تنها نماینده آمریکای جنوبی در ¼ نهایی خواهد بود و در آن مرحله مقابل پرتغال‌میخوره و در نهایت‌ فینال بین هلند - پرتغال برگزار شده و تیم ملی هلند نیز قهرمان می‌شود. البته این فقط یک پیش‌بینی آماریه و تضمینی برای رخ دادن قطعی آن وجود ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22900" target="_blank">📅 21:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22899">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WntQz1Uz-UweXUa680amZGmWkvFNxPuJ_LOqxIdthySUBuQqL2jd1Zg2hPP-kDMzI1wX-FVxBHKwNzCTEPbTI25S8aHiqgUco_nfOGG4Ib9wsZEMQ-2e6mnMATHOD6lZMZz-x6E_igdh-Z3cUihfiD3eykrDDyG_QCvqIeLiWrt86PQmYSkB_edx-HVR1ll5458EnTuyheUUI5dWiu32pxbBCjRMhm_CcTXP48FzsRPL4wVtxgf1cIberNY1Afv8fVWw1Jr_XeqtElyiT923Ck0W-tADyHW8SeKbrBdXzcR3g0pRcxMvFghGhYxA-yheWE9maGprF3jXXVH39voH7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22899" target="_blank">📅 21:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22898">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xft0iZKqs-3Rb2V0x0bANgzNfKnc7XzYJquitTP5wsXLUOM0eAIU0KCK3pWFn1W8YyQnmQ5VWKk3UfwV5lwpPMdNnjE_9z-mHiTUk9vaUNeiyOf22VUmPZQ5i5T5CY4kU2glXjlOFiZdrpAMEJ16VUVZJUfjBuycNc5-Lyb4uhSun72eEE11k4HYXzfgfQamiEvJnPLEA9QBn9kwxAX20dv8X3ZsYAiE7P66LqIa85-sxJAD6kEKZECVnGs619gEx_VpoUM5BYlwhOTkCgTEytnFiiaWoof1fquvVl3qH18Qxsk2iH9n2C02WYctsfwLR1BCu8FG747irmWd4thcZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌استقلال با فروش جوئل کوجو به تیم نفتچی ازبکستان‌موافقت‌کرده و بزودی این انتقال‌ صورت میگیره و کوجو رسما از استقلال‌جدا میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22898" target="_blank">📅 20:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22897">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f73008adba.mp4?token=phuNvq5uPavJeaAUJMmrHuRVgtGfu3Nl1kC7Q3bWv7qluu5ymkW_KgXfFUqRQJVkd8fu35EJFG097Nq_WqRKLs3pz0-q6Bkgc84AJq7gvTzWmZxzls4p3STzLXaVxtY6Aud8YA5iQ-6wkNfdNh-ZliT6Z-XA0tG5R5ox91zPgG8i5_QdiVxBqPUXmkHiv3P9ir6BYTEfr3-fkrwfo2hphebJdjgPRRSzIpDuhWl3Dy-z6-v481HEgcWHbzsco6xGzHC2IVKsWsGICBTadXImEWTbNELoezA329vCp9O93uEf6i2RIWHp5zhsqK2LapEcJ5jQmC10Z4_Gv8aEErQp6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f73008adba.mp4?token=phuNvq5uPavJeaAUJMmrHuRVgtGfu3Nl1kC7Q3bWv7qluu5ymkW_KgXfFUqRQJVkd8fu35EJFG097Nq_WqRKLs3pz0-q6Bkgc84AJq7gvTzWmZxzls4p3STzLXaVxtY6Aud8YA5iQ-6wkNfdNh-ZliT6Z-XA0tG5R5ox91zPgG8i5_QdiVxBqPUXmkHiv3P9ir6BYTEfr3-fkrwfo2hphebJdjgPRRSzIpDuhWl3Dy-z6-v481HEgcWHbzsco6xGzHC2IVKsWsGICBTadXImEWTbNELoezA329vCp9O93uEf6i2RIWHp5zhsqK2LapEcJ5jQmC10Z4_Gv8aEErQp6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبیکه‌مسی شخصیت‌منفی بود؛
آرژانتین ـ هلند؛ یک چهارم نهایی‌جام‌جهانی 2022. درگیری بین بازیکنا به حدی زیاد بود که به نیمکت دو تیم کشیده شده بود و این موضوع باعث‌شد مسی به قدری عصبی‌شه که یه نسخه از خودشو نشون بده که کسی تاحالا ندیده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22897" target="_blank">📅 20:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22895">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYRRl0OydObEi3gkO355xYM1EvZnjbUuRM6PBE0jgb5nxNDx4MJiA5nJT-Gs7yWNuY3etodas5_Lz2gh8HBTn59fZG4HAu5bgwkJxW9QbAT5ScWy17KCyPI_yUNV2EPG1z0qzW4kXnMctfHB9caMrTQzL7aBTACNtffPn6pnO7Xnf-u3jd2caM1Funi3MhWbxkk_ZgKBLfqj2sHvzHco64zQ8vO6i4-4Ut6rj8Wa2cQG9_heF9HoztLzzTHhokvghG-CpUeFxrt-E5LAWutAT83KeBH5FwHpjIer4ueC-roCq8HPUr8hgKBnsqE7La8O_iPjnmbks7bM7Ps7uj7XGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22895" target="_blank">📅 20:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22894">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc1ec4c74.mp4?token=CENb6MadOGOH5DUhsA7IfzCLOwdRXRsX0L-CoOk73cmh2ZrRqdMXokh2FhBhq3AFgqPLO2JJzThsPn4UQYdwHn5LcYqeVTwQRSKH0waBf_7t7AkJhpgfOQNX8MnOIRslwKEoFMe8ViAJ5YfLpyhEk3bjNH0c52D8T4UWD4YlURGr2FxJFq_XgoXuIaezn0J27Lx24c_pceAurDM1YoK0Hvze4guDt6Hh22GrhDuz0n22M2cOX54MFIQY4D-T8ajTHaeb_c2RV-nEadShY88-Uj2M5eehKZiJ7Lbk4a-GJe_7kiq1MEwTJs2aZycIzxjebpdqvd9mmnb0DwS43kANjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc1ec4c74.mp4?token=CENb6MadOGOH5DUhsA7IfzCLOwdRXRsX0L-CoOk73cmh2ZrRqdMXokh2FhBhq3AFgqPLO2JJzThsPn4UQYdwHn5LcYqeVTwQRSKH0waBf_7t7AkJhpgfOQNX8MnOIRslwKEoFMe8ViAJ5YfLpyhEk3bjNH0c52D8T4UWD4YlURGr2FxJFq_XgoXuIaezn0J27Lx24c_pceAurDM1YoK0Hvze4guDt6Hh22GrhDuz0n22M2cOX54MFIQY4D-T8ajTHaeb_c2RV-nEadShY88-Uj2M5eehKZiJ7Lbk4a-GJe_7kiq1MEwTJs2aZycIzxjebpdqvd9mmnb0DwS43kANjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇨🇴
وقتی بازی‌های باشگاهی تموم شده و از بازی در کنار هری کین میرسی به بازی در کنار این:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22894" target="_blank">📅 20:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22893">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwULc7834uuuEpIsjBWNIXatW2SNbCw23U09myazIKfVCKBvFDLBSihJf5KKaQQ0BMSWdn1x-EEQIA4P_m8KMBr3Yv40bW0aUnTr6VkTqbO9VklsuqT95XyRT_Tmu-L3rnDBP6LdElsQIBadyCRo55-eW2QDAaVd_be3k0tDzM114SMDMiW5V2pUmEFSqRUfQ7hBpPfUA2_MUShj697Jvx0LSxDdm_RqluqqkLHoDDPpfLC3e4cWOZvR72GHGtGxmMCzulRXyly9Og175OVhKpLR6HMbBFh-8TdtBcbna31MW4M-rT_bO20i-mYI3HZ6icj1BtMxYcOVRcy-ZCg5_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: با توجه به شناختی که ازفلورنتینو پرز دارم به‌احتمال 99.99 درصد مایکل اولیسه این‌تابستان‌باهرمبلغی‌که شده به رئال مادرید خواهد پیوست. پرز این قول رو به مورینیو داده که با هر قیمتی اولیسه رو به برنابئو خواهد آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22893" target="_blank">📅 19:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22892">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKCjEEaGHQIUHEm8G4I1tM8fBVUZVQnPJMHnU7QH1ma6PLxNiyT5cyxJDBIs90j2HzDVovKvWVLlSUWsL98QqneT-JhWi9Xz5Qctybr6hTTlzLXE0quZc-pzN545RVUe4Nu-sEkY4IuKg4OtKUTj2tl2oZrZ7RX51hRV6bnTE_IGhO_EsCOt-7DaJJax94WhRUFjkDbLynLgwuMgjw7_OMqHZpO8DPZv1giQ8cwFY1k0xqGofDpF9ls1VVJ-EGQBwlrUHHhtWt-6LfVcRiIY5n9YGqVDPPYNNONNwI3vTaDhAnh8Ea1XsewXFsMDALlWEv-Ju2NCwY2kczLZUDJfRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
در تازه ترین رده بندی فیفا و آخرین رنکینگ اعلامی قبل‌ازجام‌جهانی 2026؛ شاگردان قلعه نویی با یک پله صعود در رنکینگ فیفا در جایگاه دوم آسیا و بیستم جهان قرار گرفت. ژاپن بام آسیا ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22892" target="_blank">📅 19:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22891">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf50298d76.mp4?token=OAcqXnbRf19y6Ye7ClRUcPO8m_FoRwprsUibiQ8nRjDzYzYmORGnj8eMts1JTJjJ-X75ysHCkMAE375FcBDuoZh8MQQ7Ulo9UQ7QZtA-_xTcTfe86VQVV8nxf-aSlI7hKWe9Kkl0Z6nCUeh204P0K95EyZrRRBlURiR3cnhqbZjpGLTDbVIpR1R9VKuwOZ_FwbLbwVJZhs3JEBY4NePWexDJ0PIwjw4RkJE1TBOHixeLxH28izI689uVhZ6rR2GqisdIgoe-jL5lX-DpO6lPc8_B2z844aDZYv-o6KILWzawjk7Eyqe1xxdoIEJQi4ykewWLo3wZvYoYhuNGUjNsWISZgOAYbN6IzjfiG55UlcPJw0SHWxh4GM8pVGNBuPxvMVVq5G6mmgPeZ-L5l2fgZ_yrAI8PBhQzk-6B5wPnQYBwoVtjq1pu1RARTtIpBdGrlo46Ita9Cj-eayRxDSFCuesycJvaBbCnrDo4Aofk7-94Tqag4BlZqStbgEc5pQiQ-brl-Mza3KTX_GohH4vGRplcQT0B7d9qonkjvCj7YQXGaUUH3uEx08YJxzrbIDoV_UYnkZ0DxmkmHudzp9dLOujehCEJweFcBlwrFeEYFlnVHkMCtSR5NRC7CfIy5C64Pxl6TYBQE60YDN5D3dQEWfX8DJI3kPdS36AddawyJls" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf50298d76.mp4?token=OAcqXnbRf19y6Ye7ClRUcPO8m_FoRwprsUibiQ8nRjDzYzYmORGnj8eMts1JTJjJ-X75ysHCkMAE375FcBDuoZh8MQQ7Ulo9UQ7QZtA-_xTcTfe86VQVV8nxf-aSlI7hKWe9Kkl0Z6nCUeh204P0K95EyZrRRBlURiR3cnhqbZjpGLTDbVIpR1R9VKuwOZ_FwbLbwVJZhs3JEBY4NePWexDJ0PIwjw4RkJE1TBOHixeLxH28izI689uVhZ6rR2GqisdIgoe-jL5lX-DpO6lPc8_B2z844aDZYv-o6KILWzawjk7Eyqe1xxdoIEJQi4ykewWLo3wZvYoYhuNGUjNsWISZgOAYbN6IzjfiG55UlcPJw0SHWxh4GM8pVGNBuPxvMVVq5G6mmgPeZ-L5l2fgZ_yrAI8PBhQzk-6B5wPnQYBwoVtjq1pu1RARTtIpBdGrlo46Ita9Cj-eayRxDSFCuesycJvaBbCnrDo4Aofk7-94Tqag4BlZqStbgEc5pQiQ-brl-Mza3KTX_GohH4vGRplcQT0B7d9qonkjvCj7YQXGaUUH3uEx08YJxzrbIDoV_UYnkZ0DxmkmHudzp9dLOujehCEJweFcBlwrFeEYFlnVHkMCtSR5NRC7CfIy5C64Pxl6TYBQE60YDN5D3dQEWfX8DJI3kPdS36AddawyJls" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شنیده‌های‌پرشیانا
؛ایجنت‌مطرح فوتبال ایران که ارتباط‌خوبی باستاره‌های‌خارجی‌داره؛ بار دیگر ارتباط خود را با خامس رودریگز ستاره 34 ساله سابق رئال مادرید و بایرن مونیخ برقرار کرده تا درصورت تمایل او رو برای فصل آینده به لیگ برتر ایران بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22891" target="_blank">📅 19:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22890">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06fdcd2c12.mp4?token=TZsIH4oQ-IhI0INOIIs1r2_nEzuyqxzT7sZ9x24zp9Kmz_yivVF4V_qxfQoZ-vjsQm0MrkDwy22ctghqxRn_yz2KuCXR5GBLKSEys621LL04NqptWULnQ-lH87wxL-VLIcgF5PXSJOfL7ZXeRNEpjApoZ71_SJH-LMLOr7e4LHW3thwDeChjRVUHu9eg3e8R5Mr04Isv0HmjXWV63j8LHWG0ZgAnnDqZe3dkMQdA16tlqrCeGVFHml6XdJu_QG682CtUFDx8i37uuypqfRLb0yjYAKk2z_ipK-jhvsKsuZa5JmoYzvWs3dyhgyRM3ROedA3i4d9IgJcWZehYjAxHbFYmKhRM-1OLe-wCVE5_5FumOI1Z4TASzhvCJAhfP8XztWJtVlRLCjhHDgqe_zxx2oBbA0iBtmzkHo784NeYQ4fYwQTFp0QcQAqs2aZjhPKbS2fpvOYMzwln51YHdr2kXHFisrqfgr5dAx0r2a02gXaBalwja_ZxnQl4MptOqt7G6AOmrSX6gIrQuGwdnizJt04HKFql2REf0EFXgT3Y2gZXmTvXu74x2oSgiShb9Xlm0il3T_Ca6sKNi-9aeXAt_LXXEVVbbUPtrz74pZKH3DOBVCk6NGatYITDjOQYJldGq0q6ffYG7jjx-02hTYQ5wlP-n6-tq7WNzam7LktapsM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06fdcd2c12.mp4?token=TZsIH4oQ-IhI0INOIIs1r2_nEzuyqxzT7sZ9x24zp9Kmz_yivVF4V_qxfQoZ-vjsQm0MrkDwy22ctghqxRn_yz2KuCXR5GBLKSEys621LL04NqptWULnQ-lH87wxL-VLIcgF5PXSJOfL7ZXeRNEpjApoZ71_SJH-LMLOr7e4LHW3thwDeChjRVUHu9eg3e8R5Mr04Isv0HmjXWV63j8LHWG0ZgAnnDqZe3dkMQdA16tlqrCeGVFHml6XdJu_QG682CtUFDx8i37uuypqfRLb0yjYAKk2z_ipK-jhvsKsuZa5JmoYzvWs3dyhgyRM3ROedA3i4d9IgJcWZehYjAxHbFYmKhRM-1OLe-wCVE5_5FumOI1Z4TASzhvCJAhfP8XztWJtVlRLCjhHDgqe_zxx2oBbA0iBtmzkHo784NeYQ4fYwQTFp0QcQAqs2aZjhPKbS2fpvOYMzwln51YHdr2kXHFisrqfgr5dAx0r2a02gXaBalwja_ZxnQl4MptOqt7G6AOmrSX6gIrQuGwdnizJt04HKFql2REf0EFXgT3Y2gZXmTvXu74x2oSgiShb9Xlm0il3T_Ca6sKNi-9aeXAt_LXXEVVbbUPtrz74pZKH3DOBVCk6NGatYITDjOQYJldGq0q6ffYG7jjx-02hTYQ5wlP-n6-tq7WNzam7LktapsM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
5 سوپرگل دیدنی‌از روی ضربات ایستگاهی؛
از بین این پنج تا کدومش رو بیشتر دوس داشتی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22890" target="_blank">📅 18:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22889">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgL7S0wVjSChEADw6cFOlRZLtMN2IfUESmnyeyhRnGMgRcZERqlt2s1Tqce5zxPomBSxGWU-9OzQR_Fv-rr09JZuYO6mTer3HrE-QSMfjm7IRY-6d11JhBtc8ZgtSLXWRCJFIg2A2jU132LHUrmXzzd_9sev3pp38ND0iZezQX_8NzHcuATSEF-rQQU3Zq7nzyykEWv_IIjqJnqR1hI4x2YiyAzI7k1o6JRtV3Vl8xsIiR6d6bY1eWbxIR50AV2lLRop9a_-2uBhlvljzuwuSgyoTr5VTdam6VcC97JEI4YomZFvgeDuS7CgYwQhuUPVOXIIhFfuxnnvMnivD7mb1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
در تازه ترین رده بندی فیفا و آخرین رنکینگ اعلامی قبل‌ازجام‌جهانی 2026؛ شاگردان قلعه نویی با یک پله صعود در رنکینگ فیفا در جایگاه دوم آسیا و بیستم جهان قرار گرفت. ژاپن بام آسیا ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22889" target="_blank">📅 18:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22888">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb97f5a2f.mp4?token=pgpqlPYYYGRnkYFR6mIyjMu9bUXtaEuZ7mzxpNGpOlu5aeUuNfa2sTBHfAp_wf0CHQFdidJmES6pWoCN-CYq2UHgZviuMs4OWr8nZiLxJh7RjuVR8lHvuAqYrefuCfNyYgrUSOF9R6MMPudZ4zA2098MSoD3dsfmKAyLbY76w0G70103zpNH4NpozXNaV3tcLWOcjE9lHSUitBANyFR0GdcElZYUOpvy3h3A9OfJbJMDv9py-7zgowrGUZRyAjV2tvRlhPX9tkLfo8LqDSXEnq31aetTWwQGkO9fbRqsK6HtSTQbyOboqHJIJMFkYwYEc4AhzM3oK2um972K7hjiTQ6bP5ZYdQH-9mH7TBK9MwkksGBXhDc8kna4SqII81Hyt7afG4tQ079w7osT1yoq9FBHlx9TT0M1gi6XPnSb1GeQd8dd9yzmCOG2koxx95Hf53lPdmnYAdcMh75Eg28kvQJtu-XkBjU_hMBJXgH637eYOMdgDnMNcpoe4dTk1Ud5K8uR2_ui7tBf-s_4mwygu8DFpScGSUKN_bkeP2wgE0r2k_DIohXFBQVS8RyXtWnyBGyP3SwGZ-cnxCVxZmmwBesL4aRBr6tqDkJMVXixaQdgnEf4xYCJA0ZEvDcfEiigynVA423jmYdI46yEhRPfttUtCUWEAbv5JJlBu8qD_N0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb97f5a2f.mp4?token=pgpqlPYYYGRnkYFR6mIyjMu9bUXtaEuZ7mzxpNGpOlu5aeUuNfa2sTBHfAp_wf0CHQFdidJmES6pWoCN-CYq2UHgZviuMs4OWr8nZiLxJh7RjuVR8lHvuAqYrefuCfNyYgrUSOF9R6MMPudZ4zA2098MSoD3dsfmKAyLbY76w0G70103zpNH4NpozXNaV3tcLWOcjE9lHSUitBANyFR0GdcElZYUOpvy3h3A9OfJbJMDv9py-7zgowrGUZRyAjV2tvRlhPX9tkLfo8LqDSXEnq31aetTWwQGkO9fbRqsK6HtSTQbyOboqHJIJMFkYwYEc4AhzM3oK2um972K7hjiTQ6bP5ZYdQH-9mH7TBK9MwkksGBXhDc8kna4SqII81Hyt7afG4tQ079w7osT1yoq9FBHlx9TT0M1gi6XPnSb1GeQd8dd9yzmCOG2koxx95Hf53lPdmnYAdcMh75Eg28kvQJtu-XkBjU_hMBJXgH637eYOMdgDnMNcpoe4dTk1Ud5K8uR2_ui7tBf-s_4mwygu8DFpScGSUKN_bkeP2wgE0r2k_DIohXFBQVS8RyXtWnyBGyP3SwGZ-cnxCVxZmmwBesL4aRBr6tqDkJMVXixaQdgnEf4xYCJA0ZEvDcfEiigynVA423jmYdI46yEhRPfttUtCUWEAbv5JJlBu8qD_N0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
انریکه بال؛
سبک بازی فوق‌العاده و تماشایی تیم پاری سن ژرمن که ۲ ساله هیچ رقیبی نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22888" target="_blank">📅 18:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22887">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHcnphNOL4UdXks7n1NXY6baKn_XHPjpYazoyFFB-YXae2_txJm9KWL1wgw4rnJWnCEJKJcF4ZhOUtNLO1pHQbLlwrfPwMet0YzZmYKT2MV0GfH70ABUyk3_Y8Q9cm9WbiNPImq9cObXf0Yc34XdFN8yHqz11Qrd7de748PBewH1xrvt11mxHRwDkW8DtOGL3Q7K2-PLQ3y5QW67ASgo0OKU2_77IPzz8c1WQx9VjEYvB1PiikEAH_-Ib7IQSholw8WGO6i3_JUxml6so6CovyYShGtkxAOANo58oQO8znIoPaHjAriOtBXjetPFeiOIT1VVnA773myvFdsCmfgHvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌ بندی لیگ برتر بعد از سه هیچ شدن بازی گل گهر - چادرملو بسودشاگردان مهدی تارتار؛ پرسپولیسِ اوسمار ویرا برتبه پنجم راه پیدا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22887" target="_blank">📅 16:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22886">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efa86e852f.mp4?token=t2-NpJpbiw4rFenzHRcl__FdDL1xNWjbFpRt7V3eI23Cw8yEILupBvlrYuf4BMB0bb38y0NHLNNms1vgz1UIpSCeLp6_q9qbIhv2b9WFmjJffNKeNmgJpVBchApCi2L_9qUOH3mubGCXncaVssWuCiBA7Mc9l0iW3O6ez3K7VhiGFK8T9b5XCl24tI_JDQhPwYumpFrcb2UhSzORfYo9YeFuCGFhflgLRMiTdTXhNrs3WDW693y6WGHyJ9-Ov5k-ezMuc3a2Y1NsN4sxIxYlDWAr8v5jTgC_8d4H2nn4tMQLRqdtIxMguxAJheP-8TxzHQ9Cqq4pfFufpQCVj8L8Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efa86e852f.mp4?token=t2-NpJpbiw4rFenzHRcl__FdDL1xNWjbFpRt7V3eI23Cw8yEILupBvlrYuf4BMB0bb38y0NHLNNms1vgz1UIpSCeLp6_q9qbIhv2b9WFmjJffNKeNmgJpVBchApCi2L_9qUOH3mubGCXncaVssWuCiBA7Mc9l0iW3O6ez3K7VhiGFK8T9b5XCl24tI_JDQhPwYumpFrcb2UhSzORfYo9YeFuCGFhflgLRMiTdTXhNrs3WDW693y6WGHyJ9-Ov5k-ezMuc3a2Y1NsN4sxIxYlDWAr8v5jTgC_8d4H2nn4tMQLRqdtIxMguxAJheP-8TxzHQ9Cqq4pfFufpQCVj8L8Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرد‌هاوقتی‌میبازن
🆚
وقتی‌میبرن؛ لبخند برای پنهان کردن درد و اشک برای رها شدن از سال‌ها جنگیدن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22886" target="_blank">📅 16:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22884">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KoZNprrITExPTkvqSNggII0Pc7y-J-U5FGgCrrFTSn0P64C5FMWxKz2RdVDSTxMSztwlV3k63x-Mo1dHIf1SspK6cR9F1w78ITI1yJaESTrat9ZypK1AUU0x4bvhaUtUhmvmg7ynyjsgrkDVCSvwsA1MTXzqFEG8bQA1H627EY5SuKRoGBD80IEGPGVdOKeB9cxmRbAH_lJOOsClM_jljo7phqq3bwvDcCM9dRmmIHYiCEF1WKGjvEx6bNpcNxkIA4qz8fX2n8ozF4I6-TNka7AzHCB4UaefTa7yL916MUGMOUFQocJPBiPgdC7g0h9rEwEOhF0cy91gRmNZ8Uznxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hPkfhsgu59sEvuBdrPCX-U2OEXCCJLm4tHsFVtEYttjF50-8Y6N9lz9kxDkfoMQ8yLEqXJBzhB4K4jg5L5HeTr-K0qNJQxBaFPVH2sOKRpaSWgIBGm_dD335LuthjPtnMg9N8t6pPtoc6qNMoxrTKd4BeDKLXeHK3XLbgcZykLT9fpkhsYP8ZiOHMFj5flCJTAZPjMCAiHdiLMNF_bdM5sGgBUlmY-8OWHJ8rtacWwQ3fBFUgruyRS-ap9SJWiTwFJ0N22fzf6yqsBTsbldjez7wa_-ecskjUcrZNpQyv93PVBvOdYFquw1yA3yBTEgg9I9Mphk6wg-M_N06EY6lgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🟡
🔴
#نقل‌انتقالات
|شنیده‌ میشود آتوسا یوسفی خواهر آریا یوسفی ستاره‌بانوان سپاهان مدنظر تیم بانوان‌پرسپولیس قرارگرفته. آریا هم مدنظر تیم آقایون پرسپولیس قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/22884" target="_blank">📅 16:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22883">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPTCE9UwHTKqpo_2FVqfziIAKfqdvKQJz_7__qhZdQ-l6qlSLFbKh_LGTBZ_39zT3oTVRQnwcS3TRuEC6cgsliWTK_TorfTSPgNkEMaVjoJAnM3BKzm7IE3hD1YZiHIBYB0PsLgKTFpoxEDoIhc3YcKuG6MkgObdOqYmZCpkHrHH4_AWWr9mdn6NaIs2nLxxi09xjiJ2mIYpqGgedRHsNSzRQIVw9suprqCaT_WhPui5P9sq9cch7__nRw-5i0_Vri3Q0ybdw3W80lsfPIqWFCyMxrn-vs6OiPkLszZbLC9-ppi_msLGWJcb4VJarSYZW6feV1Q_hPSJQzK33raB_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
#تکمیلی؛دولت‌آمریکا: به افرادی‌که حضورشون درجام جهانی ضروری‌بود ویزا دادیم. دلیلی نداره به تروریست های جمهوری اسلامی هم برای حضور در جام جهانی ویزا بدهیم. ما هرگز اجازه نخواهیم داد پای همچین افرادی به خاک آمریکا باز شود.
‼️
مهدی‌تاج:اصلا درخواست ویزا ندادم…</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/22883" target="_blank">📅 16:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22882">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITFomBnZLHIGJ9xMiqDpG184A0gU_eLORA0eYRvtfj2SSmLxGIzGtg71mzceEPYvjoi58M97eM_FXsMZCkSUDBE7FkCeGSYl9ZK5o_Zt7feiD4h_L5BGLFRaRfgXgsU3CT-mkTgwL5IVVzw5y8e5Omrlw2TzqOJJP2h8vXH6zD5-HjZkU06lC3l4X6Yn4bx6bc_kf8krDBvAWOk4riChT6pk0Ijw9XQ0PTUwsZ3OtznhWR5VFwTJPjgMSLYwU3vcBIkZj8HRcxamZP2NeX7kBNkQhvV20V0CeHZ9CzXRXI07hIpH38UU3j1_N_yQz7li8ewqrAo-WyxXh6b-liKTfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ باشگاه روبین‌کازان‌روسیه به مدیر برنامه‌های کسری طاهری اعلام کرده هر باشگاهی که کسری طاهری رومیخواهد باید مبلغ یک میلیون دلار بعنوان رضایت‌ نامه به‌ باشگاه ما پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22882" target="_blank">📅 16:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22881">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9TW72fkSEN6ZupJ-pUtka3veL9xpRiFJcNXNprZau59jRLmSGgD7n2USRb1nNVVKzzqtLkFw4pHQDsvt5bq7eOa9LF0kfURGAEhVGkAqV8tDXmAO34PWDAvyVF9xL69BW90CF1lugOm31PdIHQHGOFwzD1Pdl3ZAeoxMDMV7JFvxQosF9xT6Tw-W0WTZPvHhzLSR6dWBo1Np_27uNaVJTbc0v677QvzMinEk6IwtnGCNl0kTo9RdHOYgxzGrzbE-gOnMC3rRaWbc1eqRoUiD0ry7wDrRHBLsvfqSlZxr9S70O0hhjEbQPr8d82vL3-v69KOxD1t-Mc6ENLm2afagQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نیویورک‌تایمز: ویزای‌موقت بازیکنان ایرانی برای حضور در آمریکا صادر شد. ایالات متحده رسما اعلام کرده که اجازه‌نمیدهد که بازیکنان ایران مدت طولانی در خاکش بمانند و تیم مجبوره پس از هر بازی سریعا دو ساعت بعدبازی‌آمریکاراترک‌کند و برگردن مکزیک.
‼️
همچنین‌گفته‌میشه…</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/22881" target="_blank">📅 14:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22879">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LPEZDMYgYZx-XftfiROmKkp-p_Bl6H5r003tN6Zg5LleoA3ycZN82E0ihUUY5EhPcLsxCQ6mkCJVK8KLAIvOenNUmwvLiB1O335LsHRP4SIhbOrBTw97FL_dVD3Kq9MFpOYaUb44vFQPSO6knw1hs6bJ3DGiqTVwz473tKnWaPTk9CQr1iqEPdjg9Ft6faaKXcoGO04uPZrv_7TST5b1FjizpUK1SlK5ysWHr9Ua-pIWX-Cy8tyZk9dLKGlcYo_pWdWG8sna4-zCjhH30DlKu0ENS1CYAMMES9di3JpnNiKut3PQAbr_cHV9pxP9_R6UQpDvTYNb-swJGW5fa8DiOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nBwHCZg95U8hq7N8NfMpsdpwZK6gprWhzGKDm2r12AaHUiRnDfNmSOP1QiSO0q0sQ52vF9LhxkP-mvfFJpSmLvFoYRiijF_IUfKRm_ZjtjdOQSVJtBpF_xWzAmG5K2noa_d8EqxI_uh0wWLVNR5hZwqZcMQn0kYw3NVMUjKT048CSu3S3k9COzbtm3qk-bOqwtYzY3reCxXJeL_2vaDLEw7NaA_xjNLKoFwWRF7bAkmqEFhuSNB71cABIIzZS9RjPB0pQ_TXB5QdK-rTvs2z0Aov3RhQKHJHfSQp2P6kiJLgp1_MKvKw9AbUJ8Xqq3rxH4Bip4PYHH1NRl-u7fMmIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
خط حمله هشت تیم مدعی اصلی قهرمانی در رقبت‌های جام جهانی 2026 آمریکا
😍
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22879" target="_blank">📅 14:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22878">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJ10NoyT4j-kus1kpAQG93leVhIUFJA3mQp0Y8uPEkkHffw6rCkirld3JV3quL0I-2qjm7H4Gjf7CqXO41NQugm8xQqzQeNqbAtZVzbU-AL74zNGHJDWmSRi2nn9knOZZbZCTi7MgFUsoG1etFunpaE8uvC4ys6CJcb69b__J0GrYA5MJrkexuXTuP3sCraDSkyBQEZWdNCiuMa-p7MRHEgjGrMezPeNq0F49yypppjD0-6st2rB2wUEFKztLIMSbBgtGD7t3oVoHBnl6iX6wDz6bbquzMQj1b_yL7Ey1i-OqcpMiq8Cz8-Veov8LpOjzQ4He1ZYkAztKKpRvhNbgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22878" target="_blank">📅 14:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22876">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TynStxYgrEgKKQEmedYKNOr3r8maJPO6CdgFnHBW0FWAbN5Q4b4vXIn01pdW72WtSSAngdiByOW1uVkobQ6_4XSDVEGTMJO61W3Q62S2QR2PsUKUu5mLd5I7paKU_COiRxGBnjbg53XrNhMtPYGQQr0Ue3aRsJtfT-EpPkgbOslvjIcsaPYIZTR4PzMghn9_0OYsgV4wqwWc0BDh-yx8GZ7zwbPNIloqusRx1nbWN1FeC6Ge0mbGwiWIBlaCFdG7JD-15nzEQTbzUpBueam6mxLDEngngoKuy3JEoa1UuJ7WWFRVYPnrb4LxrXxoQ0tlo0D4gDondQmLbshr71H0oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه استقلال با مدیر برنامه‌های موسی جنپو برای فسخ توافقی‌ قرارداد این بازیکن‌به‌توافق کامل رسید‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/22876" target="_blank">📅 13:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22875">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=AftnWG5KJdhRSk1eRth655GAdlRj2-1981AEZQ_s_TWghQVuBmTulkHzbGEZSxWSmlQaJugU3kcIdlbub3JT6j4whSGh8HX6HeFD1rncadGdcR7m5y9FrvMqBLNE1PJuHy1MDfh-fk77dPydIyBMyCWDt_ryE-d8ikabUsP-fYFv6T6Zgh9cCMLi2ubRXE3JY41eTDrRMSK4_NDGNZ4zc8OB-t1Elm9ynjR-YW5K7mviXoclw01Hf3n_JGRP7b709gTay9I4dKezX2L6kRCU3aIlWe3ZMMc-GwYq_IsIM5zuGv_IU0zg9P0-erIb5ld10ajW1VNlr75YFLvyH2njOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=AftnWG5KJdhRSk1eRth655GAdlRj2-1981AEZQ_s_TWghQVuBmTulkHzbGEZSxWSmlQaJugU3kcIdlbub3JT6j4whSGh8HX6HeFD1rncadGdcR7m5y9FrvMqBLNE1PJuHy1MDfh-fk77dPydIyBMyCWDt_ryE-d8ikabUsP-fYFv6T6Zgh9cCMLi2ubRXE3JY41eTDrRMSK4_NDGNZ4zc8OB-t1Elm9ynjR-YW5K7mviXoclw01Hf3n_JGRP7b709gTay9I4dKezX2L6kRCU3aIlWe3ZMMc-GwYq_IsIM5zuGv_IU0zg9P0-erIb5ld10ajW1VNlr75YFLvyH2njOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
نیویورک‌تایمز: ویزای‌موقت بازیکنان ایرانی برای حضور در آمریکا صادر شد. ایالات متحده رسما اعلام کرده که اجازه‌نمیدهد که بازیکنان ایران مدت طولانی در خاکش بمانند و تیم مجبوره پس از هر بازی سریعا دو ساعت بعدبازی‌آمریکاراترک‌کند و برگردن مکزیک.
‼️
همچنین‌گفته‌میشه…</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/22875" target="_blank">📅 13:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22874">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GX4fLCNvmvb3lfQY9DgMYcgDMzWmDuEcLzgaDZHWIv8_l3KCOBk7RWIhkI0T3tz_-SaTYbi-2AwkT9UrAMaZ970OKwqMIb3ohntelEkSLVYQkZPW3uGCZEFa5__hzEjfxfUCZel-4qR0WosbLihpOy44dTdOOoOEaQUVtjDWICCGPHSxvmzJMmrYvy8TGKcHFze9UBxSc4ekIFaKridO1lQ-O0PDTEfcQp4nQnguLLC8uWRU_vzjNhTpc45rUpNAzHOVszpe3vG9PWJHbmpmOK7iFEQq-6Cdq6E3aOyDWh_qSFeP6jHU4HArtCjXBomlIDsrJwDGaCr9AEuFlZdagQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نیویورک‌تایمز: ویزای‌موقت بازیکنان ایرانی برای حضور در آمریکا صادر شد. ایالات متحده رسما اعلام کرده که اجازه‌نمیدهد که بازیکنان ایران مدت طولانی در خاکش بمانند و تیم مجبوره پس از هر بازی سریعا دو ساعت بعدبازی‌آمریکاراترک‌کند و برگردن مکزیک.
‼️
همچنین‌گفته‌میشه…</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/22874" target="_blank">📅 12:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22873">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5ZyZLJbX7i6350Xh5oPF0NDb8AGCDwVUrKrmaaK9PG9XltVCukY9xUsRpwnHT1ElCEIpdaTya61BfWr8OdG9eq5DDeFN4FmFDZ-69-cxDqefIF8vFPArLntNXok__Lk6pa-5wAcmot4Iwf0QWi6r13Befk4GcDT7R5EEXA9ox4mIF_ujV9Jo3qLOVMWS8jVXUxACFAH9P1uqprwgyGQYh_b3mIbtx-56oanr9pLlZSmCV_pMvtURIviF1xNzBcxeUb8vlV3xQy3Zo0ncBsKhsjicjGAbxP2rLFQXMBhuuXh2RuUAcJeW4Xs8_cVWGdvI_0jJ5FgtqoFoelurQzg5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟢
#تکمیلی؛باشگاه‌آلومینیوم‌اراک: در روزهای اخیر مذاکرات مثبتی با یکی از اعضای هیات مدیره باشگاه استقلال برای فروش محمد خلیفه و بهرام گودرزی دو ستاره جوان خود به آبی پوشان به توافق کامل رسیدیم و به احتمال فراوان این انتقال بزودی رسمی خواهد شد و پول خوبی به‌باشگاه…</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/22873" target="_blank">📅 12:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22872">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNLJyS1Lh6fk-4UF3b-2tsR_DSmYTetZzqQEpzrh1eSbUdPupHZ0JIPKw0Hg1Vd8yO-tkRJLn7aUMtCaBi4ka00zSO8TmTGiqFOpBBKtOEvyEsnW77KSUE8XO-WUbNrLOxBAgAyuHgQSjxsB9BIpfNlxzuhDf7zxEpjZxQb7NC9liCyM_ziI23xfx4Al0lzLZiXNq3bGciopadglRgCAAyQfKYfInDvupCCKxYJhhIflV_ynmQ5Vka5nSyRfsrejkQ42BnR9HBDTDM2bWipwNU05ZZYuB1d-ZHg0T_423DaNPF3irz749GS4AXaewdcCE8mp5_PsssurhXsmwrbh2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست‌کامل‌نفراتی که دولت آمریکا براشون ویزا صادر نکرده و گفته حق ورود به آمریکا رو ندارید.
‼️
مهدی‌تاج رئیس‌فدراسیون، مهدی محمدنبی مدیر تیم، هدایت‌ممبینی دبیرکل فدراسیون، محسن معتمد کیا مدیررسانه‌ای، مهدی‌خراطی مدیراجرایی، مسعود اردشیر افسر امنیتی، مهدی ملک…</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/22872" target="_blank">📅 11:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22871">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OM5IPrc9VpNkEJwTybn5SYnT2JfDCWs4zuG4Xu5ChrqSxXZT3CpBkKVojk0gEBDHJvyKNU8IgqUZtVFUQMkXr_qNTHSKXpF9Q_vG1YGhzJ2554dMyl4lacJUL7-WAXdf5JIrncizH7fVkLXZgUqZbWu-wwvb9ag5l4Tu7yj4OgQHT-qn_ritjFjCf02IOrDBH02RLuC9YxzFGvDCDK5sWB3FS5bZZEdLTkVHb7cHaw1jy3-6WSFXek0MrWOEWfwrsY4joipqBN22v6YMVc3IegJMWq6pzf7A2x2H1qIakGfFDW28jK147k9oStRaMtVnULygKP6zDykHwzbS8TgdZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ تمام رسانه‌های معتبر خارجی از غیب احتمالی چندبازیکن تیم‌ملی ایران در رقابت‌های جام جهانی 2026 به دلیل عدم صادر کردن ویزا از سوی دولت آمریکا به دلیل خدمت در سپاه خبر میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22871" target="_blank">📅 11:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22870">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35d2a48cbb.mp4?token=rK7HW38znZeduUGe77taNYXWL4iHmAc4pkot7dQLt1jLy8tEianX-vvQvC3t8eXfSsU9oP1oR5G80-1eIrtta8gQiPYBs1IEWBwU00B_FxjCoSBwdy1XEENoxphdsZ_Rk2eB4jCPcCRnvpwnSbYwi5oEVnE6TEnYb8z9cvDk9LjoDbuewSZqunBIeOdIw_78gKYwMaQDx8CPXY4I0AsGzCSM8gMoUpoUYo_ViLB8HW6o3o5z_FvfNo4Lm7G70YAEvy46qVssOE6eVrNIjKqy67NyGPCOdtRdTFiLq9bSazXkfI4HOIiqJiwUf_jUaj7mpx37rzt7PB7julkoOvkyZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35d2a48cbb.mp4?token=rK7HW38znZeduUGe77taNYXWL4iHmAc4pkot7dQLt1jLy8tEianX-vvQvC3t8eXfSsU9oP1oR5G80-1eIrtta8gQiPYBs1IEWBwU00B_FxjCoSBwdy1XEENoxphdsZ_Rk2eB4jCPcCRnvpwnSbYwi5oEVnE6TEnYb8z9cvDk9LjoDbuewSZqunBIeOdIw_78gKYwMaQDx8CPXY4I0AsGzCSM8gMoUpoUYo_ViLB8HW6o3o5z_FvfNo4Lm7G70YAEvy46qVssOE6eVrNIjKqy67NyGPCOdtRdTFiLq9bSazXkfI4HOIiqJiwUf_jUaj7mpx37rzt7PB7julkoOvkyZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
اجرا‌ها و موزیک‌ ویدیو‌های شکیرا برای جام‌های جهانی ازسال 2006 تا 2026؛ کدومشون بهتر بود؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22870" target="_blank">📅 11:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22868">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbfjwUL2zBv_OjSoeCc24LKRSKDKRCJS3bnT8rbLauckbT2B-c2MYTyL9N32wUfky0xW6MYlEhV0D26UQJvH0J0JT5jOGmmcUQRaAJcMJtayBFGS7LLfN6quQ82pupaUBmA9IcqqRWBc1RSxrsaSrHxVQhxwfMtjycerRiQFf-d9t8HR1bucp2YFhRGcZy_zKx5RQB_yjQPGP9vp7nq4089vwvfQUnw-K7dnywRi6NJFyqb7-B8GUyA-zmsOeEM-Ptb0tZ_2ANeHCLAfo55Dbe-9emsCozSCODc_-ZFUU1uFXfmerTne_1Zq-PesAuptLjku3TqUbgHvRgY3RchTCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ظرف 72 ساعت آینده از لیست اولیه اوسمار ویرا برای‌فصل‌بعد پرسپولیس رونمایی خواهیم کرد. منتظر جوان گرایی و عوض شدن شاکله سرخپوشان باشید‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/22868" target="_blank">📅 11:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22867">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLaPoVRimiLBuc3cLyWS4fvG9u_f5CwsIjT_hmV_DqoRQtO3mkcCj0VZVVXYwYfNLq6YUw-UyJNPdgEqDMoKz6CPfIHHC4Y1aVizpNY5dg6nk6fgKnMrpsmHRJBrmEeBCmBh_KrZgIG-p2apJIFbMIzKc9o0im3ltyKdsVSJuqQwxQfKfYELkiAvJqp-HNxFHGKT72-tCyzbj8yP2kRpRrBpNLmKQLV5BfvUZ5VzTs2ksl3lWeWHd7_uBvnMz5VLlmjKX97cOPEdNOyXI_rFg0ZMXj9wb-qCckypH28x84neIY8qyRx18ldaQHTvesP6QWYK3GZUkwAcBV9We6QPDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ محمد جواد حسین نژاد یکی از بمب‌های نقل‌وانتقالاتی تابستانی امسال فوتبال ایران خواهد بود. حسین نژاد به ایجنتش اعلام کرده قصد داره به لیگ برتر برگرده و راهی تیم محبوبش بشهه. بزودی جزئیات دقیق تری در این باره خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22867" target="_blank">📅 11:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22866">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47f6fd1b53.mp4?token=sbf70ExqtZ_pTfDrW9aCcAv1LbZMOQm9A0jb2AnS7xxZ13cmb-1ND48HwTaiR_MDyeCfGw3-4aveh6txhUHTzVr825Tm8pViz2R9vvVOEH08-UqeezJbdqtDgcoigtFNk80L6IY5KPkjiowKWv2pQvipiyIVilSMbFxQ0RPBLtJjr4-eZgit26riP-L2J9XRGP8exhjlkvwiOeNi2MsuJ6fQ2rurFaJqIRCLiBZZTpin4MiDHiFXXph2zgk2uCFIEErlGq-Vcn-nADVNL2LgB7A5LTfOhPeGHG18V2GqB8On4A9Kfw0O2Ucn_ObwzHT3hhpv8ZL2Sn1X3_r16J7Ysw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47f6fd1b53.mp4?token=sbf70ExqtZ_pTfDrW9aCcAv1LbZMOQm9A0jb2AnS7xxZ13cmb-1ND48HwTaiR_MDyeCfGw3-4aveh6txhUHTzVr825Tm8pViz2R9vvVOEH08-UqeezJbdqtDgcoigtFNk80L6IY5KPkjiowKWv2pQvipiyIVilSMbFxQ0RPBLtJjr4-eZgit26riP-L2J9XRGP8exhjlkvwiOeNi2MsuJ6fQ2rurFaJqIRCLiBZZTpin4MiDHiFXXph2zgk2uCFIEErlGq-Vcn-nADVNL2LgB7A5LTfOhPeGHG18V2GqB8On4A9Kfw0O2Ucn_ObwzHT3hhpv8ZL2Sn1X3_r16J7Ysw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تعدادی از هواداران پرسپولیس مقابل فدراسیون فوتبال جمع‌شده‌اند و شعارمیدهند که پرسپولیس رو به جای گل گهر سیرجان به لیگ دو آسیا بفرستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22866" target="_blank">📅 11:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22865">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">▶️
هایلایتی‌کوتاه‌ازعملکردخیره‌کننده مایکل اولیسه دربازی این فصل بایرن مونیخ مقابل پاری‌سن ژرمن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22865" target="_blank">📅 10:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22863">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9211e2c5d.mp4?token=PZPSMV_hMMjICpB6byOvy96IBPXaEkaYPctyAW6MsfgRZIlhl6LAv8SZ2Uc7MfcN7K_xsriT23x_sBJs2wGNP1xBNQnHxfzZQja5-sv8mZZKnWLmTIBaZggB41RQ9vdewM60USdamzUGnThGPAKoVMBHR4a6WFqu2Rch4jNEyNH-2uKVXmKtjvT8U900a8hT3_QggA88_8Pp_cbgk5TbepTMPKZy7PFHw8osRIB1s3elsMaF2T0A01Ye4ig4gZ8mHE1KNEoX-7L83TIdvfGKcDl5PxAzk0Vu6sqdaAtwLLTODtYZgZiyvEgIcZbejaFL_cAgQNM8nRLAQNQT44BjMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9211e2c5d.mp4?token=PZPSMV_hMMjICpB6byOvy96IBPXaEkaYPctyAW6MsfgRZIlhl6LAv8SZ2Uc7MfcN7K_xsriT23x_sBJs2wGNP1xBNQnHxfzZQja5-sv8mZZKnWLmTIBaZggB41RQ9vdewM60USdamzUGnThGPAKoVMBHR4a6WFqu2Rch4jNEyNH-2uKVXmKtjvT8U900a8hT3_QggA88_8Pp_cbgk5TbepTMPKZy7PFHw8osRIB1s3elsMaF2T0A01Ye4ig4gZ8mHE1KNEoX-7L83TIdvfGKcDl5PxAzk0Vu6sqdaAtwLLTODtYZgZiyvEgIcZbejaFL_cAgQNM8nRLAQNQT44BjMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کیلیان امباپه: همه فوتبالی‌ها قبول دارند که رئال مادرید بزرگ‌ترین باشگاه جهانه جز هواداران بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22863" target="_blank">📅 10:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22862">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSaDUtnTh-SfwMbD6Zjy3FqRofvdijUlz1jGUvw7k1PuvTDFH4rF8kyonpQBm2vFC-KuieiERS7tnFMHMM9SjOsiF0a5U_qNfHavNhSFKKl0zLR8tEirjNfbEvjpjSD7J5ISDA7ma9ENYK5rcbd1KO5rF6NjHF5_eEGmk5jmljKMvXlfzrtG3DVuVr_9yjHCgFrDWhArbHxMhD2BPaA43O43Y_Z4UP5NkzyUU72kv-iSnz7yeUZPgj2FVSSbEoGAcAXqdiEgY9i9VGNL-yxCj5dDUyGsEz9ZUu6L4LXXlx_EdRfXRdjh8sMW0DOs3XVcUXKfHiqB00DpKYI1TgLIxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیشترین‌سرچ‌های‌ایرانیان‌بعدِ88روزقطعی؛
بعدِ بازگشت اینترنت مردم اول دنبال چه چیزی گشتند؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/22862" target="_blank">📅 09:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22861">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f73764a80a.mp4?token=ozzb0Oduwz_lAALYRODsJhXADFuIPNKdM5eN0_ahE2UVZ0vE7g81W4JRgS512iAjucWwSJJLNszLTIAeHAqqbPWqabMlI-cV4Vdy8y2SH0Bjqiy9VZE5l2ce-yG4sZGyCB20OQV4570-JzTyQ-hDOkKpaxHER05MfB9JwnVpGRGbGKC0Zx0XUFJZEj_Ti_IhA_T6rhHAHmoxaz14b-jjadEMpswaxfy4yK528trzrXGxAWlTnlW_hS8IMB6PPm6jMHA2tdRe5ncOJ4XhtEiom0ZuJ47NydP20joym_AbNsehOp3afeYcUD8cTgV6zwyOOk1HO8znxMsmC6TNF5fEcJJufWNT6LNH5V-IQu3eIetz2M2BJy7vvkUgQlAJe5w4rYHKDWZOXa7kD5QZdFDlZQZa6IyBo3WSNgwxhyA7wiVJzdkXlsL3XajjdZds49xJc_3fx_C4WVij6slgpGhBEmr3RQ6eV_9HoBEAGIDX1YrDNJ_2Unqh_Zpxb9tViNvFNRa0IaQFYz9iD-bu_m6pCeETl7Q50CZtKmpOACnJtspMM1r96VIx8WH7FQNrIZwbQB81T0RHU_kxlipvSfgFQ3l_iS6-B4lFCjq5EwY8LsUqhPLNOGJspGUdegXfTeknI0E53Bj3fdie2VLtjt1Jw-OzN9NdVqUnvQIHjI_uWNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f73764a80a.mp4?token=ozzb0Oduwz_lAALYRODsJhXADFuIPNKdM5eN0_ahE2UVZ0vE7g81W4JRgS512iAjucWwSJJLNszLTIAeHAqqbPWqabMlI-cV4Vdy8y2SH0Bjqiy9VZE5l2ce-yG4sZGyCB20OQV4570-JzTyQ-hDOkKpaxHER05MfB9JwnVpGRGbGKC0Zx0XUFJZEj_Ti_IhA_T6rhHAHmoxaz14b-jjadEMpswaxfy4yK528trzrXGxAWlTnlW_hS8IMB6PPm6jMHA2tdRe5ncOJ4XhtEiom0ZuJ47NydP20joym_AbNsehOp3afeYcUD8cTgV6zwyOOk1HO8znxMsmC6TNF5fEcJJufWNT6LNH5V-IQu3eIetz2M2BJy7vvkUgQlAJe5w4rYHKDWZOXa7kD5QZdFDlZQZa6IyBo3WSNgwxhyA7wiVJzdkXlsL3XajjdZds49xJc_3fx_C4WVij6slgpGhBEmr3RQ6eV_9HoBEAGIDX1YrDNJ_2Unqh_Zpxb9tViNvFNRa0IaQFYz9iD-bu_m6pCeETl7Q50CZtKmpOACnJtspMM1r96VIx8WH7FQNrIZwbQB81T0RHU_kxlipvSfgFQ3l_iS6-B4lFCjq5EwY8LsUqhPLNOGJspGUdegXfTeknI0E53Bj3fdie2VLtjt1Jw-OzN9NdVqUnvQIHjI_uWNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
#تقویم؛ یازده سال پیش در چنین شبی؛ بارسلونا لوئیز انریکه با مثلث خوفناک MSN در فینال لیگ قهرمانان اروپا یوونتوس رو با نتیجه قاطعانه و پرگل سه بر یک شکست‌داد و قهرمان این رقابت‌ها شد. این آخرین قهرمانی آبی اناری ها تا به امروز در چمپیونزلیگ بوده است.
⚪️
…</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/22861" target="_blank">📅 01:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22859">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fItxdG1KBW5xiV4DtP_Z7O4nSlaQPufhHNnT9zWenGg2mXtvMHamuI_JCspolIo-bcYveNO-vILihKDGkNVsSYc_QNLeAy61RtBQ9OfvwTROm7uSZyQi3BsP1s2qRU9adfSffpm399ZomRYsXgCTCLKStJZ-Mbjvpc2r1xce3BPMXRPb7Q-8zYaU7PZ9HJKAt0dDfRh4ngFeAQuHrWVS7hTk6csL3flau4GlXU7DIEAy06qIGo8EpbsUXX6e7lx1aOFlSZdvxM3ERw5rzX6yxe2q5mk8TKKvqMkgrzSmldNBJz7q8Ui8Y_Qiy2rjWOG5WgcKFGvDq1Y504Lc1Hkwqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VgyDh6ZJ-HuCn748SDRj0x3enY71TUZOU196T3z6VciDvnbey_mvLBaKx_ia_tkAsLKbs4yuRhLXazyR87zVPKPygIBjwSHJIEJAElaO_Q2BBOffi49lx-fYyKrzaEdqfxUKa0VVyc2PykCFCfYXTpesr_zo9r0ZOut9HU6QSdrKaXyk2lxW0D33_2F666iPuKL3j2AyVybupMjSbUcgC9ZrO5go9k9YZSx1Cv1SViIRdbOXp49WYwj9JF3GXnmhKYl7FzDmiDcwAE08AR12cXh-cxzLoenqPKvLi-S3P-UhIQNrqoO-cWx4HMSazUfSDon-TxxEYgXbMCb1NptBIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
#تقویم
؛ یازده سال پیش در چنین شبی؛
بارسلونا لوئیز انریکه با مثلث خوفناک MSN در فینال لیگ قهرمانان اروپا یوونتوس رو با نتیجه قاطعانه و پرگل سه بر یک شکست‌داد و قهرمان این رقابت‌ها شد. این آخرین قهرمانی آبی اناری ها تا به امروز در چمپیونزلیگ بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/22859" target="_blank">📅 01:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22858">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mxq2VDcu9_Y5CPM2JVOMtpEv3s7l7lpZLDTuCeF45aM0ZwBR5Mm0M_a6JRFMTvOlTJ8p9nokBugyTUjtqCwT6SZcZx1OVkKhMFezTFSsitE34zp6evrjxZua6gL5_8GK4U-zNX756FCn5mWsRe3UBeQuCbJTKoDaAFatPUXNVM4rXXGTmVRgDHmiustceLmuZz0wgW9oCFvZAEFpV7DdgZ4Gxtl2w-ipoMlFYQ04vc3mfSANR7P2xwMb03hgJjo0AdKTaJf6mXp1Kre8waXtqaV1nlraUcUxTcq9Tv_1ri4XbiNus4qWITi0R7WFGe91GNvCAsvwHGsDFi-6T_s_Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌کامل‌دیدارهای‌‌‌امروز؛
ازجدال‌یاران رونالدو برابر شیلی تا تقابل آلمانی‌ ها با شاگردان پوچتینو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/22858" target="_blank">📅 01:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22857">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClZ9rblZOZQkCQ996YE0heceS9Yl34F1P-RE1YAijhOiigv3gBp3OUz17ftfw5Jy-YwL6P9WrKOh0JhGjxqkQ1z1Gv3oMc-gIo_SUnkAIH1RcGHPRBVTkMryiCbNsVuVXsZLlyyxmjABeiBsFncO8q_u9qylpMbqAaWz9wbMkiSjtRe_543o4Q3E2IxwhQlsHN0qfbmZET7m8BApGANPJP-PKskdsBkpc9NUGimchS8kdGKoe2aFf7i0hl1drAzq2hyUT_wiZ1RnECLttq2vHNpRnl-Lf9tpAKJFe6TpcvrloY5ECsXnhoIK-OosrgDFsFcRf9hXv9pZkc9daqEcKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌ روز گذشته؛
استقبال مکزیکی‌ها از جام‌جهانی 2026 با جشنواره گل برابر صربستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/22857" target="_blank">📅 01:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22856">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ma-jo0iZNDcB9w7yo41_DM-kPD7WiT8_XFIgFcTSheB_AEuWjvVfMu7nBZ8WafzzEW2-MZEGFU_iz2N-HNGYK6dTIgtvhnbkPTIzLb_0MTWDFDMJ-6koybgwvwgsC056uhCfC2fzmsumu0_K_WzNRi5U05vmKqz6oLqzTs2qga-4MAELzL9z5oflK8KGrnixbgdBEuZPaVvjwBMihYU2PY9DVj9car5qVl-eX6f0ElnLPfFNM0elW5pGORp-gV-7lvzNIANZLDxwYRJfsRVFWnbq0h4nXIAw6I_h2rCQrEYVK4eD2C0zHaMqEeayPncIT5sNxpUjlAUcJwZXlkKPTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شوک‌دراردوی‌ژرمن‌ها
؛ لنات‌کارل‌ستاره 18 ساله تیم‌ملی آلمان درتمرین امروز این تیم بشدت مصدوم شد و رقابت‌های‌ جام‌جهانی رو از دست داد. ناگلزمن سرمربی‌ژرمن‌ها بلافاصله آسان اودرائوگو ستاره 20 ساله لایپزیگ رو به اردوی تیم ملی آلمان دعوت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22856" target="_blank">📅 01:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22855">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z65grzLtF7VcLu08JEXr9Nu4CVUMwoeZVVlGpr6abPRAHWiFPmJOhH9LXwPJjFgb5UyNc6s_QuVpqMHLOBjL-zU3FRR5kVyL57SFHYOQXzrm_fzCwxy7WgtNq7rdlO8ml_IE4Fo-E4-jwgXwbe93uRED8UU21YNUXvOUmj8B51R73WyN7or_7LJugw2CB677zzDDxS_LT877BmDGNXi5b5Po2ec19nvBEAzFS5ZzyddbwDcuHQMoEqYU6pfZKpXolWTe5FVJB5-LcgvXK7CwSDoWX3dm4y623O2QbyuDXhhhPzIUTqC9ynecdG5PInRZhHVjesZ4TbKSmlFYAzei_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛طبق شنیده‌های رسانه پرشیانا؛ محمد جواد حسین نژاد ستاره ایرانی ماخاچ قلعه بزودی از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/22855" target="_blank">📅 00:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22854">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sj1Q9kQRRvwmWdH_YtyaVs9Zc6yIHCY6L_b2-nQ5w1fvjVqvw12W0J9gSacDiVt2ejrJEicU3IUgy9nCZVUXPiJ6f2EfRHPiXalU-mKja0QMrAScHkT2mGQfe9QKOmPlH0WHvmhdIwUFzDCSadzrFR4n9euQpropwRHbXwBR1Ru9zd9mxybvBoxuainDzNiJkU3szLiX9ZXWmfXJ48wTlmJ1gLxL9chbMCJQQQ2WGMyJzzuuvot8hlRH-_VZXOhSAkJ3KghiX25tliFvYOGG5-hDd6jonSshajNGXYzQCOL-CwJVXRw-G5UN9KYM6fpvBym1Bm5RL_yvFWAsSngsBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چت‌جی‌پی‌تی،دیپ‌سیک و گراک بدون فیلترشکن در دسترس قرار گرفت. همه برنامه ها دارن رفع فیلتر میشن جز تلگرام،اینستاگرام و توییتر؛ سه‌برنامه‌ای که بیشترین استفاده کاربردی رو دارند باید فیلتر بمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/22854" target="_blank">📅 00:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22853">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e00cf6e9a5.mp4?token=tsj5lYaiPB6yVYDQ8ZLHfLIawZFv-PLpRB1F2yU48mlZcNnAZCxG7-YKhCy-qtWkX0lF8RS1L-3KuycZ1IxpzLBBBG_451QhKSo1FvDvVss5E5JxInBpb9yVYU3hZ5AvUtQgjDqpwpPoLIBs7BCX5nOerefs2C3plZ4PJX_dYP25utEnyZsB7_i9Y8Ls9_x3OuPLDJSadeV1ECqANOCEGTsdX9MReOXzFvg8GZCROh6TQWWXVDO06_yE99mxQEsePbvOvS0p0B-TvaTOY-Yws8VnOx2OVrutsGLqUKDySTLdlqOzUVDniVCHu5t6kPEO2FuyU4srYBCbHOx_3Le85Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e00cf6e9a5.mp4?token=tsj5lYaiPB6yVYDQ8ZLHfLIawZFv-PLpRB1F2yU48mlZcNnAZCxG7-YKhCy-qtWkX0lF8RS1L-3KuycZ1IxpzLBBBG_451QhKSo1FvDvVss5E5JxInBpb9yVYU3hZ5AvUtQgjDqpwpPoLIBs7BCX5nOerefs2C3plZ4PJX_dYP25utEnyZsB7_i9Y8Ls9_x3OuPLDJSadeV1ECqANOCEGTsdX9MReOXzFvg8GZCROh6TQWWXVDO06_yE99mxQEsePbvOvS0p0B-TvaTOY-Yws8VnOx2OVrutsGLqUKDySTLdlqOzUVDniVCHu5t6kPEO2FuyU4srYBCbHOx_3Le85Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ابراهیم کوناته مدافع جدید باشگاه رئال مادرید هستن دربازی روزگذشته با ساحل عاج؛ واقعا مدافع قحطی بود که فلورنتینو پرز رفت این رو گرفت؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/22853" target="_blank">📅 00:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22851">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pm6Ab-E62BTk24fDzfILX8DZEPmd-wMrq3B9nykXRDcX6sciP2blYswM0Dvz97UuTBrJYSCK6Bu1Oq5BHlE4q2aIs6dG3oB5OqU4svns03BAL7WzXJBglsWa47dJdh7KHw4AxgOEyzxGh4-0FpIg5JGuvfn2zZGbFhud-1zMvEjERrQ1GrEts08gs0hVQE1XXmnRNzTlFM2MRecQw0-pDz1-HGknX9v08y3bJ6kGPCAHpcDq4UkRt97czE0Ple08Ac5V81Gs4JGAzNiDkG9nSSE_Y1dSTwm27lRZi8ND0SEGQAdBP761HrxPQ55V8YpQgo-Klfb7q0780m8D_zw44A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
علی‌‌تاجرنیا رئیس‌ هیات مدیره باشگاه استقلال: یک‌‌نفر از اعضای‌هیات‌مدیره تیم استقلال در طی روز های گذشته با مدیران باشگاه آلومینیوم اراک صحبت کرده‌ تا انتقال محمد خلیفه رو نهایی کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22851" target="_blank">📅 00:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22850">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2CNK2QnDvKGOoAc5HlGWmMK7ZMqyL4Lv7BXJQvFK4cx672bH0yxQLPaEOYJu9sywTrP5Ts31-mQC9RN23dT3DurATmRkvMpgbcpOSIPZpWnXi-GbBUARsNi_lLHjiKY2b-m_HjUhL0kUIPwpvMEypCOdpin6I5LQb5mR3tyt6445Vm2tZqSzt0y6-4_igGuLKO-Bht7hH2N36xpfh50Ql63HN4MSfxQnAt7ibwQImxPpE9Rcd0fpjZAZOr6jbaz_91GIwq3LSB3Ek8bpwyL7ZgTRIWZ7-So909ojVsudNule-cj8FPvecctG2M4Y-xg7zGr3UsyXaEopbHmz-TcCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22850" target="_blank">📅 23:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22849">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aedcb21ace.mp4?token=nuKMIBPtHOvUtzYSkijkLq5RhrEHcg7Yuo7eLQ72Bjs6fhyMEDCm6mLxOFrJ1sALwUopj9nm_F-RyN354yE0TL8X-AnmPdws4fgo_-CTGuaNyJWnGPFXDhvf2h6_z1rQoVpfEHEdEVicVC2c96fv-_GLmHGXULU-UJbMFgPATs9fbO8w3Pjc-wbx8u0Lqcisyu_WbKaPb0zXyKx1Av8vbKa_rUEJ49QbD1z-cNESqApyR9aUg-o-CeILi8FeISBd7rd4oUW8euMhVUbN3M1oB6tDYLcIAPpFT7CpoPrABlrgBWIDWICp455Cn4bjvSI1obFsZg9sLv8SSliXNQCmIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aedcb21ace.mp4?token=nuKMIBPtHOvUtzYSkijkLq5RhrEHcg7Yuo7eLQ72Bjs6fhyMEDCm6mLxOFrJ1sALwUopj9nm_F-RyN354yE0TL8X-AnmPdws4fgo_-CTGuaNyJWnGPFXDhvf2h6_z1rQoVpfEHEdEVicVC2c96fv-_GLmHGXULU-UJbMFgPATs9fbO8w3Pjc-wbx8u0Lqcisyu_WbKaPb0zXyKx1Av8vbKa_rUEJ49QbD1z-cNESqApyR9aUg-o-CeILi8FeISBd7rd4oUW8euMhVUbN3M1oB6tDYLcIAPpFT7CpoPrABlrgBWIDWICp455Cn4bjvSI1obFsZg9sLv8SSliXNQCmIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه پرشیانا؛ باشگاه آلومینیوم اراک اعلام کرده‌است‌که هر باشگاهی محمد خلیفه رو میخواهد باید 100 میلیارد تومان ناقابل تنها بعنوان رضایت نامه این بازیکن به ایرالکو پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/22849" target="_blank">📅 23:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22848">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e230120d7d.mp4?token=Td6IafPZynku15dAFkNWMXStEMxf8qrSNuduUeupeLwPJ4dqyDix3wlnzB29F13DG_k3DNjkPlUVhX6MtYF2ps5Zg3uIrXmd80sZ9tHh8s7PDvJWZxCgLvbTJVA1pB2UKBSYLDJE3ORJhfseYPRQdO496NC4hc5auTVcq99OpXiNneNhBZi04JbRrHlnpidMeVnO8fVNl2Wu9KNqB0M8xIewFf5xM2vR9yt0Ngfwr8p6l_Mm582ZR2R9hOi1HXfq0ERXuxImzXQSlYEChNWvOKYBABVPboBdmup2iKE7B6qjzfYxCZecT-KHkVsA-BJ2J5zybyCrwON5Ss9fLzRbrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e230120d7d.mp4?token=Td6IafPZynku15dAFkNWMXStEMxf8qrSNuduUeupeLwPJ4dqyDix3wlnzB29F13DG_k3DNjkPlUVhX6MtYF2ps5Zg3uIrXmd80sZ9tHh8s7PDvJWZxCgLvbTJVA1pB2UKBSYLDJE3ORJhfseYPRQdO496NC4hc5auTVcq99OpXiNneNhBZi04JbRrHlnpidMeVnO8fVNl2Wu9KNqB0M8xIewFf5xM2vR9yt0Ngfwr8p6l_Mm582ZR2R9hOi1HXfq0ERXuxImzXQSlYEChNWvOKYBABVPboBdmup2iKE7B6qjzfYxCZecT-KHkVsA-BJ2J5zybyCrwON5Ss9fLzRbrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تکمیلی؛ اینکه خبرمیزنن پنجره نقل و انتقالاتی باشگاه استقلال بازشد زمانی صحت داره که درسایت استعلام فیفازمانیکه‌نام باشگاه استقلال رو سرچ کنی بالا نیاره. شماهمین‌الان هم نام باشگاه استقلال دو در سایت استعلام پنجره فیفا سرچ کنید بالا میاره چون هنوز بسته است…</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22848" target="_blank">📅 23:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22847">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9eXoRKCoslvOWb9dIyHdbZC0qiNboFM1MFHqhddDQbLS_UlVcOOaDW7xlu8bQYmZRydpUrjX8KafcP4AhAjXbltCqh4ejx2Sc1wQFM0QWWwBcmybGju8f7vdfhVoyPaOR5oJFcTKSr1IHrHmgMmUiwRrqrn7pky4dWC99vdxp_afh0OTgwQ2vLx0S6XJv37aoP1tF5YJKDESyntDoC6icTyLQ1cycDFNCGWzv1coVmYjYdinNRLM5nEha3CmY1KiIdOJwvTF3ejTQJCip9uGlboFHYhTVS5rTznG8D8OkI_BDo7TYuxS_luCquiMNC2c4miz5rLSOpx3crlygWkIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کیلیان امباپه ستاره رئال مادرید: به پیوستن مایکل‌اولیسه به رئال‌مادرید بعداز چام جهانی بسیار خوش‌بین هستم و امیدوارم هرچه زودتر این انتقال دوسر برد برای ما رقم‌بخوره و اولیسه رو بزودی در تمرینات رئال ببینیم. او یک بازیکن فوق‌العادست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22847" target="_blank">📅 23:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22846">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">▶️
انتشار موزیک ویدیو جدید شیدا مقصودلو همسر ایرانی خوزه‌مورایس‌پرتغالی برای جام جهانی
🔥
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22846" target="_blank">📅 23:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22845">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa70e9e949.mp4?token=mL9A4pAP-v1ZWp6Y5mjy5ri4zL9krw3y5N9L4CkUTA-sVlrKM5LqP0lxGiCjshfUOR80azGfWGgLq4KrSBSfjXTQ8OAU1ydlRPI6J0pY8k-gD_uzTTsFrWAERisK_iTGiiD42gVkJwCosb-Swz_WQHhhwRJdrrl0_zyq5FD_McgsaZSehywFMCsG6cvtDlvcqylwFRFBUjgBSoSL1Gc4qXk3Ezqi2zCrRSdfWekOVgHUjblYolq7kDzF8E-byLe28eGS4xx5x0MCEt5FI1TLyC2y9qo_W3yLgRK1X1HxM9avWJgIh95qY1A2PRZsJN33B4FXvVncQxMNIWvMm57aBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa70e9e949.mp4?token=mL9A4pAP-v1ZWp6Y5mjy5ri4zL9krw3y5N9L4CkUTA-sVlrKM5LqP0lxGiCjshfUOR80azGfWGgLq4KrSBSfjXTQ8OAU1ydlRPI6J0pY8k-gD_uzTTsFrWAERisK_iTGiiD42gVkJwCosb-Swz_WQHhhwRJdrrl0_zyq5FD_McgsaZSehywFMCsG6cvtDlvcqylwFRFBUjgBSoSL1Gc4qXk3Ezqi2zCrRSdfWekOVgHUjblYolq7kDzF8E-byLe28eGS4xx5x0MCEt5FI1TLyC2y9qo_W3yLgRK1X1HxM9avWJgIh95qY1A2PRZsJN33B4FXvVncQxMNIWvMm57aBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/22845" target="_blank">📅 22:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22844">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/080305bcc8.mp4?token=CnHQZwRFFR8W55HbeO-JSGgf9IvQtBCyxMQmvLse5l9xbuo74K5Ceh6Zftw6o4gCFDqPTihQuNRN9PRf7n5TbB7L352G8Y5YPJTH_BqE-ixAhA3b5MtuN0vUiaGTP9Viap6_cY1nNuVNRDtA7i5q3FFoYZKOAgANcBrtoSx2sGZJDKncKIc7UhKYOoqWUjEPVYpSkXhB7_XTXEM_4xh3GWq6-Dpo2r5kferQZn802JhApHBfktRi5WsBf4AVQKqlsw27wW_umB86UIsy2GdYa5ypi2PhVZ5R6VUFIIe3KMJNL2ZAvMB17cnGUKApJ1gNH7PU3t8-9XBNUeRDN7coeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/080305bcc8.mp4?token=CnHQZwRFFR8W55HbeO-JSGgf9IvQtBCyxMQmvLse5l9xbuo74K5Ceh6Zftw6o4gCFDqPTihQuNRN9PRf7n5TbB7L352G8Y5YPJTH_BqE-ixAhA3b5MtuN0vUiaGTP9Viap6_cY1nNuVNRDtA7i5q3FFoYZKOAgANcBrtoSx2sGZJDKncKIc7UhKYOoqWUjEPVYpSkXhB7_XTXEM_4xh3GWq6-Dpo2r5kferQZn802JhApHBfktRi5WsBf4AVQKqlsw27wW_umB86UIsy2GdYa5ypi2PhVZ5R6VUFIIe3KMJNL2ZAvMB17cnGUKApJ1gNH7PU3t8-9XBNUeRDN7coeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
ویدیویی‌از قهرمانی تیم زهراگونش در سوپرلیگ ترکیه؛ زهرا گونش بهترین بازیکن فصل لقب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/22844" target="_blank">📅 22:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22843">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63cbb26f8b.mp4?token=NWVg_X-_rJ7-WDZeU9A8I3Jg6ECKI6p4K-1wtjHZY3UFbnLZ4ZEq7iqprk5Lu6YLjLMG4EPTfZftowSqX15lUj__SY-6NG501_6cq3C5zIVuii7CaX8l3fqrD__zRplctbSshy_p_FGfWfT8xGITHVtlv07h5HeZK8FOMjo5mYh6659srh4CE0-MUn4WA6rjnBbSInLxJjwec4N_Pl_7EH5uUWsyzjFrbRBnE-Nz6GWKSmwx_BfcgylGYuzz3WKksvW7LBqkPLU7Mw_QBBFGXFKrkh6Ob5PZuw2macuAcaXNhYXLgzjR-2dMkU4oNO69HTsf-Y9HG-mtlgd2JoSJf69n1MoObBkbRc7Fd0gybctIawFawR6vRPttLvKeKveVqMQu7ljXbtlTdrJRZLbo2ZRBaCnphr939ijzrwk3r5i90oDjDEJQkqZlbgzz01D8E4kzViXCkbixHZeXguzu9km_MEdbORRixZSBsOHnwbacItoeJ2HkZetSadzhhVudDbx0JcoHZkc2PYbF7zY1kpzULXrpDgtCf0azi2Ho6pwSDQbfrlSVrKdviGhmh7flObDYXGjXsALk75ZXtRqk0i_bBKILZrJ69EfjLEY971f5Z5mYfNzPdukdxRzMSswojsHRY8RNu5BXIJCJNJboR4Ss_EJHocEe-hDYlIPqnyU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63cbb26f8b.mp4?token=NWVg_X-_rJ7-WDZeU9A8I3Jg6ECKI6p4K-1wtjHZY3UFbnLZ4ZEq7iqprk5Lu6YLjLMG4EPTfZftowSqX15lUj__SY-6NG501_6cq3C5zIVuii7CaX8l3fqrD__zRplctbSshy_p_FGfWfT8xGITHVtlv07h5HeZK8FOMjo5mYh6659srh4CE0-MUn4WA6rjnBbSInLxJjwec4N_Pl_7EH5uUWsyzjFrbRBnE-Nz6GWKSmwx_BfcgylGYuzz3WKksvW7LBqkPLU7Mw_QBBFGXFKrkh6Ob5PZuw2macuAcaXNhYXLgzjR-2dMkU4oNO69HTsf-Y9HG-mtlgd2JoSJf69n1MoObBkbRc7Fd0gybctIawFawR6vRPttLvKeKveVqMQu7ljXbtlTdrJRZLbo2ZRBaCnphr939ijzrwk3r5i90oDjDEJQkqZlbgzz01D8E4kzViXCkbixHZeXguzu9km_MEdbORRixZSBsOHnwbacItoeJ2HkZetSadzhhVudDbx0JcoHZkc2PYbF7zY1kpzULXrpDgtCf0azi2Ho6pwSDQbfrlSVrKdviGhmh7flObDYXGjXsALk75ZXtRqk0i_bBKILZrJ69EfjLEY971f5Z5mYfNzPdukdxRzMSswojsHRY8RNu5BXIJCJNJboR4Ss_EJHocEe-hDYlIPqnyU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
کاشته‌های‌دیدنی رونالدو در تمرین امروز تیم ملی پرتغال در استانه شروع رقابت‌های جام جهانی‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/22843" target="_blank">📅 22:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22842">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMVgT8qplfrDCjbh0r0p6pDL5pf0es1sbwby33GT_iLJ7ITQOelLTqgmP6JBNZi2RGrSTgfHETu7ZGFrNqileEHnnLw7nuWuP7Y5lTPuwAg6VojfRL3T1eWRgwA1AuPf9Oe5mLFb05YQwpRxQsdVGP1AjVB3e_9orl3ngL_uTY_3UNZsb-_1CpqHKsMzmtg4B0v0LKsZcFptQKH3gVsfWP1vCD9KjajJHR9alUXKHFz-AjXQdpHlQHpmDpETzcdkv8X7Z49EK_-WJKvvkOpHvMnS3-CozuQ2Kt6eOQi9Py4R51yc6b0-E1Hh1JrwlAD-nzsqkpWaKcfozJlScPvPaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛رسانه‌های‌فرانسوی: کیلیان امباپه، مایکل اولیسه رومتقاعدکرده تابافشار به سران بایرن مونیخ موافقت‌خود را باانتقال‌این ستاره 23 به رئال مادرید در پنجره نقل و انتقالات تابستاتی اعلام کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/22842" target="_blank">📅 21:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22841">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8JM_pXXLnfFZYbsZ2YmafVoumfY_Sbq1fYzqkBmjUSO89FaIjPg2eT7ZH05tPvRf1h_M-SAe1V6euX_CMDDiX7xrKExgsqH7bgd5E62nR0W0scvCC2WIleJgCaGxvE5sctQjnRSQU9DJRg2oOJQ5KWGDUZpqwXYX4fbv6EuYiugYjKWa0qisfrur8TvWCJ3QcNHW-YJ1lcGMYj_eQYbcPhD7bgFWQmz25PzYuGwE0fhoHshEYQE6Egi9nIuCSbHHEaVjYWQSH_x797Wk4oUkg09AmcoVPvLY7K1psF75i4pBl0uNn_iwcYL4jlW5Guz03rsH1nJl3W_0KgiZiuhIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ طبق اطلاعات موثق به دست اومده پرشیانا؛ باشگاه استقلال افر سه‌ساله سالانه به ارزش 1.2 میلیون‌دلار به دراگان اسکوچیچ سرمربی کروات سابق‌تراکتور داده است. همانطور که در روزهای اخیر خبر دادیم تنها شرط اسکوچیچ امنیت منطقه است. گفته جنگ کامل تموم بشه دوباره…</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/22841" target="_blank">📅 20:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22840">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c01b9049b.mp4?token=jjxVQChLlK3f2E3KKZIHPSoNCh83oXyJIAahW0XlPqW7gUvUU_fV4Htm9mGP1Qnv5OklxWKtI2m4HZOB_T3HaNx0LF8QAbxXVl_2ENAviJnFACnB3c6fPDdaTNzL0WGVuIy1UvPabAzY_uT5Y5I-hwslpkZiKm5-6zUV8nGHgh7Nw8HXnfBNP5AQcOMLY3x_boNMIBS0LNH7mLr_4Djd4pxqG91-WQetqL0rIbFCY7ZwaGnVCzb3nHDSQfZFFkvFkpB1o1n6_phP5UYrdQcmUZY_4LZHfFVcyZ6AonsiF4NSNCzVdVy0wffxCxPy3K9fKoL_BfqMwv0nWagxwZM4JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c01b9049b.mp4?token=jjxVQChLlK3f2E3KKZIHPSoNCh83oXyJIAahW0XlPqW7gUvUU_fV4Htm9mGP1Qnv5OklxWKtI2m4HZOB_T3HaNx0LF8QAbxXVl_2ENAviJnFACnB3c6fPDdaTNzL0WGVuIy1UvPabAzY_uT5Y5I-hwslpkZiKm5-6zUV8nGHgh7Nw8HXnfBNP5AQcOMLY3x_boNMIBS0LNH7mLr_4Djd4pxqG91-WQetqL0rIbFCY7ZwaGnVCzb3nHDSQfZFFkvFkpB1o1n6_phP5UYrdQcmUZY_4LZHfFVcyZ6AonsiF4NSNCzVdVy0wffxCxPy3K9fKoL_BfqMwv0nWagxwZM4JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
@Persiana_Soccer
| Out Of Context</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/22840" target="_blank">📅 20:53 · 15 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
