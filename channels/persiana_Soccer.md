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
<img src="https://cdn4.telesco.pe/file/BeLSskF5GDFEfoeftmQ0aCWSxrsQ31UgjHXCXaY0nEdiz6N_AHst36mPCFvflWGfT_sKxfd0M1SdUXMTwMOYxOG32_sCyBDEyM0DsnZe3ejmQaXDJ-XitrhcNCma3EddPN5CbKH3Xg4hM54nRn-bIw4wj6dHgAw32DZRNkeMgsIxJFDPWDzrIOCxINE7dVQkVWIi0oOo_2Ef2-CGobgzd8Pc3MfNDoBw7YHiu301sczTvW_fzSvilswaJ5WBKE4Tc0fYW8glcBG2s_-1h00Srg4Z4ULxm3VKKtdrJrJ_axQxZ5bgH_FzVdUnyu46SfELSRPyKGvDfE673w2k0-IJhA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 441K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 11:40:09</div>
<hr>

<div class="tg-post" id="msg-25577">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adLfmKCIWhqV8KNiQubEGBeuKgl5qEr9aW3TvXZqDux2dVStNCKwzM63zaxfbq_k1lB20jxQKxy2pvg21iFP8UEsPTda123b9QaXgQX87zpQwJ-kP7RP-vlTe1n16UuHepL3oV2Wpx171q3AvHrcrieUfD1E4bT-J_WfOP59waVoLuztaWdqCkklaEwkUoQLyvMt30_TLS1TQlQQB-k92EcC_WJPfaJiFiN7jijfJUACBuuOJVgUfhOeDaBY6XgsPEUSiBEkWqG-UMgdCzLYDRsssHbe8XAS4Zcvb1DWJXjFyeoC8ooAfHBtHt0poebpcHkk_3xhtAvoWRKLjlibMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اقدامات لازم برای زمانی که مبلغی را اشتباهی واریز کردید؛
این پست رو سیو کنید و بفرستید برای دوستانتون. ممکنه یه روزی یه جایی بکارشون بیاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/25577" target="_blank">📅 11:16 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25576">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Io7_0wthx4KFQ3SAEJee7896oXhJGA2hlPvFrscDR5EqkxlequrWMZ1BQnAbQ7qjS8voNX1m1lACf8NnEtqbypB4FmrEKuekvGbMgh4mZcUfG7obYupm6WwpC8DywC2VNh72X8RdY90PyV0iI6-fmbbf6Qnne-FdkWHRmgN8MQWVSXgTylOl5QWLcdauP-_1XnOpWQ1qm27K_nm1TVIZNCAb2DPfz4svTRX_qlHL50esqEnstVENxGXgfR3gE-xuX4zJ50iFiY0iJ8-p01aL0bGNGilDcFdI8Fgm-KfhsRIBTsnb-nPCawfNLBJH69l-XkEiP8wK6YKnuFmooTBk1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/25576" target="_blank">📅 11:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25575">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMEsq9fCfJdWmKrrv4rgscncz4dxe-lwcGiitrkHt6LEmenk6SObPg4FbVxlO1qWs71Ybt23YwZ6l7ALX_sGafNnnn3zSktS3O3DVTnibeTiwp92tDi1CwFUDmFaAUrsoeywiXK8f3WSXml_ksmLKUrgwGSKHHnha-VjsoJXiNUQYb0mGnHZNwxLv6be4BqER9RyFM7ncWvW6JlE7x7cHw2yb7rKltoJOvcWOfB8wgA3yA2ZUOFUuSCzjF6DYSGnMQeo4uYeXfOfaUp5k2wwzIq7zEyMSCieTDNExKCsSa_RYkNIao9wK54tyfTP_LAJCN8oF5VC30aXZ4-JE5YMDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسپید و این بلاگر آمریکاییه که میبینید در مرحله حذفی جام جهانی طرفداری از هر تیمی کردند بلافاصله از جام جهانی حذف شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/25575" target="_blank">📅 11:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25574">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYNVEJKifLMmDs7NToHaPOtaXkLwPcpcQguCwbx_rVmcKZo_D6xH37nPjwzI6xJlDpnS9F0IHO5RD9kxdAlNbDSvRUKgK-AMrhdCB_6jDIm_JJGlydtUqFiF5HeC0mvCySk7PqAfuCeMw6iPEy884L7eXyTiEOq9yM3mxmXNqM7iv09yy3yjbSpJR6Wq7TFxXo1N_IcWSlKxsW66kVnZhz8jBksEFlcN0uVXuPWr9lIrZxY-II4zhLaDQ1pC5HPnKtGo1adRdEnM-eWSfU56YmkokNm_jkbzVpZZkJp_m_MKT9xHQkt7MAMYXtg0MDALj1qIY0DB6quIy97flIIIog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
امار فوق العاده ی کانال ، کافیه هر روز با یک میلیون شروع کنی و اخر شب حداقل 15 میلیون داشته باشی
💵
اگه نمیدونی تواین‌روزها چطور بازی‌های فوتبال جام جهانی و والییال و تنیس رو پیش‌بینی کنی با مستر تیپستر همراه شو
😍
‼️
میتونی راحت حداقل 15 تا 50 میلیون تومان در روز سود کنی
💎
کسب درامد انلاین ینی زندگی راحت پس این کانال از دست نده
✅
لینک ورود به کانال :
👇
https://t.me/+HOIRMsG7xT4wMDM0</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/25574" target="_blank">📅 11:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25573">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c16c61fa5e.mp4?token=lGOY0WjGu7_2cIt0eU-o3ZwuhuHy1pHJ1njCHz-5B5r2I0gCASZqIfm45TNP_3TkNOovt6fpag7Kx_xPOt-8ueEYEAs7xCKzj8HflN5-Zfsv-9HPgyhhyjJug3UiufR-kBr6JgbisdvNPPujm4glaylluWe58KKhPEAxidfHkera2cQVs2MJsMlairaX8QKm3BLUfED6zcVlJIunBiko93R4W2V-BdJBlK-E0C9biLMxK5n95lapnubzgd3g9pbF1HgWUemCSuai50_Y8LGd4PboP6u_4nYDIT9DfsDaj8QtDh46cqHx0eCU2ge25j72eeRPXG7dEKWajkW1veF70A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c16c61fa5e.mp4?token=lGOY0WjGu7_2cIt0eU-o3ZwuhuHy1pHJ1njCHz-5B5r2I0gCASZqIfm45TNP_3TkNOovt6fpag7Kx_xPOt-8ueEYEAs7xCKzj8HflN5-Zfsv-9HPgyhhyjJug3UiufR-kBr6JgbisdvNPPujm4glaylluWe58KKhPEAxidfHkera2cQVs2MJsMlairaX8QKm3BLUfED6zcVlJIunBiko93R4W2V-BdJBlK-E0C9biLMxK5n95lapnubzgd3g9pbF1HgWUemCSuai50_Y8LGd4PboP6u_4nYDIT9DfsDaj8QtDh46cqHx0eCU2ge25j72eeRPXG7dEKWajkW1veF70A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
خاطره‌جالب‌وباحال فیروز کریمی سرمربی‌سابق دوتیم استقلال و تراکتور درباره یکی از شاگردانش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/25573" target="_blank">📅 10:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25572">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpyjoizA-j8tBK9nUIK7T4TjnQJvu6jMKsiC-Ze9XennvYQraGUCWNUH4ncHLoMTaW1FsLvoYIVgitFyFiT3YrWUhhHZOcAbq6xgG4MoMxf2DfPvW_q3IY6yQ0dv5cLHvzZ9M7-fV7iL0g6Ht9FFW57VrbyU_hYVBJf900bJlh6b6gAB8m-c3gpBtdARyroWJttX-1ZPO7uJUkRS2o1PBmjhWGoE51BKD_JdnhZ8hhxGsXYdBBAheQBXszdSCuNoc4hDvrr5UHkgf70N_iwMNzSxbp3mkR6dfCpapA2yGdIJEKrYFPH3uSyF4Zqod_U9DR7vZ6e3tFaq-pQeJRrbFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/25572" target="_blank">📅 10:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25571">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUcrzcI9cQRLaMVS9yoMKGMJsl2NiaWwHTzkONSb1uSnUX83jZ_bw_insSuv6xnp1zpdUwRKweKGwNV-tmEAy-MEwKL6vnM5zcicgmblx--qQMgl4Y1uRcwYJM0h6qrwB2QHcVrrUl5b3X0oWSrGnsb4tG1OG3I4swhWRDCV5bShbX4Em9FKE41iN5l3esoXvOd0_15INdTK8tk8vt7-WRIRnGRlYN1Pgfgw56PFMqrtQSa_ZSqnosNVkrxywYZIH-Jk01VAFRl1JJ4PMlE0SP1YYHOkSkQLJBQB_UslQMJSJ1PDpHKm_N4er4Di6hV6_9tAAVzN-oc60S3NBLOUqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/25571" target="_blank">📅 10:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25570">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2501cb2ee1.mp4?token=kCfu8gKR4_woIKJddEp7W_nugZLUj584ATf3xJW_2t4rSUFuc_bJhZir80Aou2uxoHfLkOF_GTMPsTuzHss8CgTX8Cut8APkDcKnLZ8pZdifOKAutBbind3O8a4pwiJHqMVCwQG2L4lgLmHdvlmB_2VJK6eij-xJzu9zlOkuSYREzydpw6vDRn0ULjMs6NGowHD0gKzLZVzQNw9MvCulAmVJ_x5ZTVr2Z1SpoCl-2OZKJtMbJepo6yaIq3g793DmkVisGK8BAnYzyZIJwYbNZyGQqPtCZK5MLnk_41wX-v-NRXQWpIMHL5sAUm8H2dZ1sdouHjM0-bGSkSwMSPc-Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2501cb2ee1.mp4?token=kCfu8gKR4_woIKJddEp7W_nugZLUj584ATf3xJW_2t4rSUFuc_bJhZir80Aou2uxoHfLkOF_GTMPsTuzHss8CgTX8Cut8APkDcKnLZ8pZdifOKAutBbind3O8a4pwiJHqMVCwQG2L4lgLmHdvlmB_2VJK6eij-xJzu9zlOkuSYREzydpw6vDRn0ULjMs6NGowHD0gKzLZVzQNw9MvCulAmVJ_x5ZTVr2Z1SpoCl-2OZKJtMbJepo6yaIq3g793DmkVisGK8BAnYzyZIJwYbNZyGQqPtCZK5MLnk_41wX-v-NRXQWpIMHL5sAUm8H2dZ1sdouHjM0-bGSkSwMSPc-Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای شدید و مجدد خیابانی و خداداد عزیزی که مجبور شدن پخش زنده برنامه رو قطع کنند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/25570" target="_blank">📅 09:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25569">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqvJCOoCQqm0t-Buu-WGl8SXcCrICcuPDXuU3LlDjDQkozlI37hQuDVexoZjwnTKBt2bYfWcPSweUmVKQnEbWqk_hMn1dYf5iVAJ7yUHQS_cNiept493CDSHXcKCd60qVo3iX-LtHkovQaX9EK0RnEFk5sz6GUQ1A64a4jCpSqafYzO9tRmPi-IihCLEd2BK4RXcB_CsxG3nihJyauEpf_Musql8LZrNGFFz5_ss_PO0BkxFs0_wimf72ZEujIyljVz4syTtWlFM2Q7lttbR6hDkUbN8DQjn1pJdeJzW183ai3HwvajzBgoYBOxL78HvJIQdpB6U3-wx3EmXX-xa8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بعداز پائولو دیبالا؛ دین‌هویسن دفاع رئال مادرید هم درویژه برنامه‌عادل‌فردوسی‌پور حضور پیدا کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/25569" target="_blank">📅 09:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25567">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iit51OLH6yRtsqADh795Jztamu1YIR48zNET5rPKlv64tNQB8thNjh0TEIuvrWRLNXMaaezBFkFuid-5D5yiKoTixpRJ6p_VslKUxinKnoidhui_xg6ff7I0BC_hgKFtYQEXNanwx7N-Wc_Hstc24EOnyO_M5hY6g4dwM32p_-H324T7Gr8UVk_8faj8AEIlY4AvoKBvJoxF0W0MQR6WwYuAkTnBub7gV3Du1pWqGblGfZBnmU3rx44HSRRc00dmO6a0TAllfyBcW3yXNXtySZHCoGIBsv-PG6T3ZbNBx7i7u0D4SI_UkH_IUdSUVcmBc4LDd-Gl9Tr-Zx38we3nOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V2AorHUgtGkpOX5aU9ShHba2rMzRhE_EHQ5rqV6P3HaapjNt-sgTC3yyfyCbRxC56CdNbBBMo8qyeN1i349gwtLGElhClm-vcmS4HQE5-I3TfcNVrmRDVul_bEtprufSqBNGa_KaHoGy3oaMgkqe0lkgJATC9R0HWl6873JZGJMKttZQloaSpfye7IGVdWAUmgxejWMrlrXWWmxcTgtMvMohOQ1wqhLwgkEtStU0nckHh09nclKrNOM0hMb0MnTpM_hgVoDopUEfD9AAep-hGfBPFmO1yRL1AqGiHLOrcILN1AYngCgdJBf7NZPmRCSV8rq1TXynEhyyPrXzcyzOOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
برنامه مرحله نیمه‌نهایی جام جهانی 2026
🗓
سه‌شنبه 23 تیرماه
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
⏰
ساعت 22:30
🗓
چهارشنبه 24 تیرماه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
آرژانتین
🇦🇷
⏰
ساعت 22:30
‼️
دیدار رده‌بندی‌ جام جهانی ساعت 30 دقیقه بامداد روز یکشنبه 28 تیرماه و دیدار فینال هم ساعت 22:30 همین روز برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/25567" target="_blank">📅 01:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25566">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nfa-oitmz525IyDyuTHT9vpUomW5S8oeumiu3-4De7AeadTNFiZ2UprMoWGPXFbpw2YYI9fVQ-vAjUoVhscx_T8R26qpDGLpO2CQco7DcVv86KAiU4FYj0DEkQD9ebR8YcCqCEYqHkDJgSwMuqoPDqLgIgj5Aj4Keb09SRrMxke0QRiZS6C_X5KawdyazkIoqR1D4GpksZzApcfrzQTa7B66KYlEJDlfeNcNOnDLzBfK5_xKJ-N6uyr8IUZ1W0IvtHpibXwTopTrHOuv-p-bDdzgrzvGlKx2srP6Gk4ga6J0yGfaLtN1Zr9r51Ctse1PC3gF-n08UKZ4xH3m7MqU5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری دختر علیرضا بیرانوند گلر تیم تراکتور دربرنامه‌امیرحسین‌قیاسی: بابام خودش استقلالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/25566" target="_blank">📅 01:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25565">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1294ecf8b.mp4?token=JYFGsyrU6qIWvvzJN7u6_-d9Vk2mjqozm7mghcOcirIagEPzYTl6a_qj4l6TlZXlXwVj4vYxr9yyG2KRdRINuFM41ngv9nWkoubaPurbl81cRhrVKOVu7AXk5NplcQXYxU6GA-IPOkvgLCrJonvZjY0sCwNO2C6WB98v8XIF1g-gzE8--17HyGVq8swddEKJgU3FTEqNOBSNbBBc_7fZ3dbn8sSCytXzP7iVHxuzmVom7rgwGLdF2KYsngrkqRUABOmZ-YQWJbaNFI3VQpLmk8GX8t6L3mxPqB7qqDtfnEUqD5BPeCAfu4NiKpBJhIUtfFGdMurSDaiw4pOu4QohDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1294ecf8b.mp4?token=JYFGsyrU6qIWvvzJN7u6_-d9Vk2mjqozm7mghcOcirIagEPzYTl6a_qj4l6TlZXlXwVj4vYxr9yyG2KRdRINuFM41ngv9nWkoubaPurbl81cRhrVKOVu7AXk5NplcQXYxU6GA-IPOkvgLCrJonvZjY0sCwNO2C6WB98v8XIF1g-gzE8--17HyGVq8swddEKJgU3FTEqNOBSNbBBc_7fZ3dbn8sSCytXzP7iVHxuzmVom7rgwGLdF2KYsngrkqRUABOmZ-YQWJbaNFI3VQpLmk8GX8t6L3mxPqB7qqDtfnEUqD5BPeCAfu4NiKpBJhIUtfFGdMurSDaiw4pOu4QohDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری دختر علیرضا بیرانوند گلر تیم تراکتور دربرنامه‌امیرحسین‌قیاسی: بابام خودش استقلالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/25565" target="_blank">📅 01:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25564">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd764fc92f.mp4?token=bCggAcMYdbTfTl8RoXs7_hQAYFzXgXnydjDRjWdKfi4KeJ9OBMBbuW9ElE5WIrL1fyaLUgjyJuZRPK3uHH3k6t5mH4L-8G6YtHrA4Mf8NPqPDOtsTNQrZKkjb5D-oyi3y2hBlHgdBQgL5b8CKdh179UI6Mis0mN-xqtuyRTYSoiYDuFoMnFASpzMnbh4YBev0_efa-ZVDXSy6AFih-iP_PZoVqtoFONf991rCbcQ6U-b80QzV6evhWGIWR-MOk1Y0WmUK1CpWKD1OWWtHTWxJEvf-xgaCucRc_kEttXAdlwrLv09Ep0WBoQ-gysCmOFOxppbEECgG1xVloTLru4M7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd764fc92f.mp4?token=bCggAcMYdbTfTl8RoXs7_hQAYFzXgXnydjDRjWdKfi4KeJ9OBMBbuW9ElE5WIrL1fyaLUgjyJuZRPK3uHH3k6t5mH4L-8G6YtHrA4Mf8NPqPDOtsTNQrZKkjb5D-oyi3y2hBlHgdBQgL5b8CKdh179UI6Mis0mN-xqtuyRTYSoiYDuFoMnFASpzMnbh4YBev0_efa-ZVDXSy6AFih-iP_PZoVqtoFONf991rCbcQ6U-b80QzV6evhWGIWR-MOk1Y0WmUK1CpWKD1OWWtHTWxJEvf-xgaCucRc_kEttXAdlwrLv09Ep0WBoQ-gysCmOFOxppbEECgG1xVloTLru4M7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#تکمیلی؛ علیرضامنصوریان سرمربی‌سابق‌نفت تهران از بیرانوند خواسته‌قبل‌از پیوستن به‌تیم استقلال این پستش‌رو از حالت‌ارشیو برداره و تو پیجش پین کنه!  علیرضا بیرانوند از چندپیشکسوت‌استقلال خواسته حمایتش کنند. منتظر استوری‌های حمایتی هاشمی نسب، منصوریان و مهدی…</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/25564" target="_blank">📅 01:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25563">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4ff28adc2.mp4?token=iZCDb6K1-6pu-lUZa1d1AwTdoB5wSMPaXTum2G2Y5_Vb2lMn6fqKyJ0pkcz95weGYcfg3hUcqYVyA0cvmye_ZRc103VXvc1IjB314yTjYplb9Fo-Z0DI_U49-ScjcO_64N-skZJVBOW89uUcWk65FHeLaJmwWA0kTAD5KSIQoakyo30jqsJ_H_eE06S2OJN608rOjlfk8zwXbIFp705RI407xbrSoJ09VTLStB-gbwFmjCq3VVwFhBS4_-zFGtvvT7bmZYcrC2vbo8hApDO29zl9G9AL8lO7WSuag4WNBjjC7J-RBIb5Gbzl9YUBSxI--_H8-fJAkbrXPiS0_R-Qng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4ff28adc2.mp4?token=iZCDb6K1-6pu-lUZa1d1AwTdoB5wSMPaXTum2G2Y5_Vb2lMn6fqKyJ0pkcz95weGYcfg3hUcqYVyA0cvmye_ZRc103VXvc1IjB314yTjYplb9Fo-Z0DI_U49-ScjcO_64N-skZJVBOW89uUcWk65FHeLaJmwWA0kTAD5KSIQoakyo30jqsJ_H_eE06S2OJN608rOjlfk8zwXbIFp705RI407xbrSoJ09VTLStB-gbwFmjCq3VVwFhBS4_-zFGtvvT7bmZYcrC2vbo8hApDO29zl9G9AL8lO7WSuag4WNBjjC7J-RBIb5Gbzl9YUBSxI--_H8-fJAkbrXPiS0_R-Qng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
خاطره‌جالب‌وباحال فیروز کریمی سرمربی‌سابق دوتیم استقلال و تراکتور درباره یکی از شاگردانش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/25563" target="_blank">📅 01:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25559">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIcOzAo93kW8ifsGHXXAp9PGkMKx1BqRdOq6bbprvB_WCyp_Q2eZpzLLcN0ZPoIeVxWmp1u_GUuGa7E1gDn6ukPYGgIxOYnOSbIKF_XYwTE6AYa_Ssk4bkOhi2TnBUWE2e3RrXwM3sW3w6tM0J8vYb35C49hLh6LRNkZnUTvXWiLYxdEcjbvzSQLYliKRCUidbwYqiBQtYFgTmXNAXjz3jghfSImCyktqsvG4SL7L8m4x1gGplyvy-4juuFRwIAMZxGX3Z3cg2xBgBvzii4F_7nLmML2HcedMSK62pjCkUDvfJEKPhB8O2I-TBy583VRgUn2HzhccY8HQj04aowTaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/25559" target="_blank">📅 00:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25558">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIJnXuks6_U-lN_uLyJNSdZUyisSDiY9LMeI8FhkHBNcIREgLVuQTorSumM4C4cI9eTehMZqUvqjxq8VcP3zA0YufQV_C2Wqy-tSKtuE-NhMEKmbz2q3kS1Ljtalq8Di-TFLnkjpImcluR8dvmiG_8TWhhQAxpda34ti83d1ydw66F3VvbV_XUXuwHHBNGLJDUdCBz7gm-8TsahoVTMFLGPGuWXXRIXbuDgaXNAzDt0qlRzXhCZaXHJBDG18WmZ4p8QZJN4Gb1QLkJ5VFfymAqAhbUMBUsMt1LO0zxx-_8quv5AA3zpEmfPvqedMhY94NCEpA5KWN5UECHExvs0rkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/25558" target="_blank">📅 00:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25557">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpJPnXdQ8MxpFGAtp5BPVEvC09GXYZ7MTFeJmInBe3LW8KfGMr53k6GUgFiW1hyJaML3ZLL3ZebA1lmxE4VJrtjyqzi_LG10Bg2lOoteli2cDRDRRYAmLOrzLKzSTsj7UhRNzoujaQdRjAA9YE7p-d4woABlVIUW-Wf3haLWF_zz63ZrYFT8aAHe_fyfft_uS_DQBm0f2TjSO-UcbGibmtudCzElGp1LPfYXp9cS_j4p6bbC-jlNjPUGlCJmCzBdNzhTYAdKhr4BQPb6G-og4NMglFuzMOovavDflxojewupm-v_55YlPY34h6EBsxk5plIB7Pbdn-vWrinGrTit0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کسری طاهری مهاجم جدید پرسپولیس: ظرف 24 ساعت‌اخیرکارهای‌رضایت‌نامه‌ام از باشگاه روبین کازان انجام شد و فردا باشگاه از من رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/25557" target="_blank">📅 00:16 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25556">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JynSYoJJOdg4vnG_LXmMQX08mHqtq2MpH3-7Y5AQSChdTcVRP3CXqvQ4TnQhk7GR31Ro7mJil-WnzkZTQgMhPbcY-1XMD0lfFtK3SJIhSyx1JhbfiQDBZQastgd5QlsQUgThcIewd7D37S9cB7_7V3etsfzPl2tYgmhQmEY6Ugu9aqm0XOFasI5xuwBT5lSsZjSGDM35p_z_stqQcp3SgOkzCrWaO6G5SfcaVtzhbLrpwqoQP0CgZdtVrTaTVc2X2bZDLar23wKS6M5tMdUfFOrIdRTWyeuD6b3vpTsozJmhkObgvbMzF7RSdb2YO-YbLy5jZKyaOyFG1Y_JKIRpnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصاحبه‌عجیب‌ زیکو بازیکن تیم‌ملی‌مصر:
لیونل مسی، بزرگترین بازیکن تاریخ فوتبال است، اما بعد از کریستیانو رونالدو و راستش را بخواهید، حتی حس نکردم که لیونل مسی در زمین حضور داشته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/25556" target="_blank">📅 23:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25555">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29a89f9e96.mp4?token=YHUyvdH1JoZimsC0rneIcmlo445oaGGO5yDDsdGcy3CnWMpVr2d5nEtjeDRUl4wMpErk2D5-Z4YedRpxoIVOsfJKSbKSzqGb6Ug60JO3GuiidErBX8QQih0eQrAfflPcYRBp94cjmmgaSkHMBLtm4G4NHOEf4k1N04LG6jjFvTrfbKRvargmTF0skSHczQ_RzvFlDMso7AU_kaRrHfEhoPwfM6TMR9y2AaBHuJcN5aPpQq6-x8yrjMyOzsEwV-2ilJ7MZyg8ei0RML0TLQvmVI8AEnf0rsa0ivuIPAi0Gypftm-tNxHYxLOO9fjKPlyR5KEWyZBSIpDGSFFITb7HPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29a89f9e96.mp4?token=YHUyvdH1JoZimsC0rneIcmlo445oaGGO5yDDsdGcy3CnWMpVr2d5nEtjeDRUl4wMpErk2D5-Z4YedRpxoIVOsfJKSbKSzqGb6Ug60JO3GuiidErBX8QQih0eQrAfflPcYRBp94cjmmgaSkHMBLtm4G4NHOEf4k1N04LG6jjFvTrfbKRvargmTF0skSHczQ_RzvFlDMso7AU_kaRrHfEhoPwfM6TMR9y2AaBHuJcN5aPpQq6-x8yrjMyOzsEwV-2ilJ7MZyg8ei0RML0TLQvmVI8AEnf0rsa0ivuIPAi0Gypftm-tNxHYxLOO9fjKPlyR5KEWyZBSIpDGSFFITb7HPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش جالب فیروز کریمی کارشناس شبکه جم اسپورت درباره صحبت‌های طارمی در رحتکن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/25555" target="_blank">📅 23:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25554">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDzh2d0ypJFhMq5CuyuyLhCQMe1LmZ2dprUioCnyhTQ9Bw_3gZIIsuXB1lRJ9mv3AbOhnGbefttGCj6RbmW_rYV-DjLTT4IxE_VAVDtk4X0LxNEx_pLBJhndaWA5liX1DJ2j09W_fnA9EXJYegfDBwtRMcwCG09s23KCkay3HpjmuYPdIVhJC0RVyva0rEVVNMCunc9n9mbjiD6wfcR_cl4MYgxsCwlYE8hgcfxy7xsymKa_DmAD4oOFFF2XAkOTIgQY6qYrtiwVE7KmUMheN5SjRuLnLpArKvoj9xSWK65sO_uxW6s-CNqW_oPRoPA3uxdxfvmJmHj6YTTdg4IGWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
رنکینگ‌شش‌تیمی‌که تیم‌ملی آرژانتین در این‌ دوره از رقابت‌های جام‌جهانی‌باهاشون بازی کرده؛ به هیچ‌عنوان‌نمیخوام‌ارزش تلاش و کاری که آرژانتینیا کردن رو پایین بیارم، اماازحق نگذریم آرژانتین اصلا مسیر سختی روطی‌نکرد و سخت‌ترین حریفش، تیم ۱۹ام رنکینگ فیفا بود!…</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/25554" target="_blank">📅 23:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25553">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQMammMSGbIEN0zu0eXYpe7mH7S0vEW6UMyjsJ0OUsxHDvNoOEjdtKa7VQkw7VABwUkpQoFJDYfnizh2IALb4a8gB-NBY6mjhG88bCab3Ijph7Tw7d98NpmGklarHVux-Mf-ejh6HVDAclM7nK3fLorfbEIgRWKYaZIqBujmTQGaiOm14CEGC--UQiMW4FsrSfuLPMXFkgHI4hrT3lS5vxpViIr6cR4-GTd1Sakc_2YYpNFvfT6FEeRCMAxzXf01cl0Pc4UUimzMDwftXEIUttmXTJIYHujSplwaIlTwU9NpRPWFX6eN9N7CuhP4rF2TpxDsBYVVaMwv5UAiEMDAwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
آرژانتین‌نخستین تیمی‌درتاریخ جام‌جهانی شد که بدون مواجهه با هیچ تیمی که در رتبه ده تیم برتر فیفا قرار داشته باشد، به نیمه‌نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/25553" target="_blank">📅 23:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25552">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcFgNrvzTPws02Iigu9fSoxh2CHi14cV2aZbNEV3SD_a2zSIoKIyMkJe0KY8UqyNzNANCGpC1atT64hd2agJEPNrmTWjyz5FOiErYcHmQYNMsA2iLfiwyHlD7unooqQ6Qf36I2uZuOIhesPnmvERJaA4IpDSvvUjOeqpwk8KbQ00u_nFvVuM8p0k_L7PXfmlNOXM02HTSAaeMTNb-Oc2qQAsJ7_DkVZwM2xwrRFA2hHF999ZMntBhTJ12-Xf3JVQQpWSm_2gXhsdK_zeT7I1pXItrcopaJFmyYqCpAv3n_iBg2y2ARiz2gjOQKxRvlQ7sPCbGD6iqFoY8qfsp8MMMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لقب جالب لوکاکو از زبان فیروز کریمی؛ جالبه بدونید که برای ایشان به‌خاطر شرکت تو برنامه جام جهانی شبکه جم‌ تی‌وی پرونده قضایی تشکیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/25552" target="_blank">📅 23:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25551">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">📊
🔵
عملکرد مهدی تیکدری ستاره جدید سرخ‌ها در باشگاه گل‌گهر سیرجان:  ۱۳۰ بازی، ۱۵ گل، ۷ پاس‌گل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25551" target="_blank">📅 22:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25550">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GP9VVbBkx-rFjbAwESiLHmm2PtNAl1UJrjYrFWWRyeFa_1SfluVsrAPEAuwwTxsqkLPcFtktRmjpI-aC6d0FuUwiGlKxnx19qQkkZVIrS9P2_yDkoqx5oxn3sqtgUAdA7-y9tP21IFXwvAH9dhQ4unhTv6ObWJypLkUtwFagBurdrFCeuL1y7xSFWNezL6Ymc9d9v5SpbRa2DEkyID1u9riUDUWniMpVZ3cu8KaMgpfUJYBsrLkObnhssmiK1MGpfFX02NLfQU3URAJ1G5v1LPsLx3XZTKhRGv2uIeri91jB10-tzG_t6L-0io5BEKaj_es_74bEaV29W-DMUyWPfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌_پرشیانا #فوری؛ برخلاف اخبارمنتشره‌رسانه‌ها؛ طبق‌پیگیری‌های رسانه پرشیانا از مدیربرنامه‌های یاسر آسانی؛ ستاره آلبانیایی آبی‌ها مشکلی برای ادامه حضور در این تیم نداره و فصل اینده با شماره 7 استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25550" target="_blank">📅 22:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25549">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fu5ai3V-NXiQ3DUxdCQDTPMi-B7QzA5GiO4nUGtYoOiJ7CwcBSWVMXLR3JlVKa-IZCMbfDalHWOYeim-EQP5zW_26v6n8YZdudJRXbWozB26mIScS2Jngo6rG5OzzyixoNu-ZjFYeVPD5XVzc5rQBxg8AuyYGUKHLuWFK6CjW6m1MGrWxBZroLkPk6N23QeNrapwIK3i6Y6rQBw_xB_t2YsAVoGLVjy3b2K5FsyVOEnvCW7oxwHEk_uTK6380j38nIyV9JGl6q99wBQ51jEEQKHUTJgpMEVN57ZZWyJllHPG4_IEHI09IUfEr5uHWL5n3G7z7jlu27vYVX5uXWiByw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس ساعتی‌ قبل با پرداخت 700 هزار دلار به باشگاه‌روبین‌کازان؛ کسری طاهری رو باعقد قراردادی یک‌ ساله قرضی همراه با بند خرید قطعی به ارزش 500هزار دلار دیگر به خدمت گرفت. بخش رسانه ای باشگاه بزودی پوستر طاهری رو منتشر…</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25549" target="_blank">📅 21:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25548">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfD-FvGdc7KuBykd-fFXj60v-5Ei7lttpgpdTHGrbDqhsqRtgtEJdqupnK0R0ahhMs6kt18EUiocnL8_XVm_dmfRltYXhUZoXEYrYsx3lrp0fV11Bf4zmIsFre47m5nr2ymWbEXwviUdGgy16-EgxtVcijsbzdFpbdT3gPRXVToN8S04tpcnyI9g-uyi13XeC_SOetEgxPOJA4IeBtYg7vvxjeMYhJuKCvCGyB_FOwJBUgyrxhtucMVeMOIPmkCK5fX_QNhGbd8wfHMptQLckZSYAGNk5ksuwUFp30MGLE0Tddux5x60Yt8VLlUEEGys9aBm99eSPJQACB_2Pmtiig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇱
فرانکی دی‌یونگ و همسرش که در تعطیلات بسر میبرند از چلسی پیشنهاد رسمی دریافت کرده. ژابی آلونسو درخواست جذب این بازیکن رو داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25548" target="_blank">📅 21:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25547">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuPrr1a2J6iMfGNtcBAKn1NbDVA8cyFrJqhfukAgFXWaBzfhCFRMsX7gqlvRfpOFR5XsQtQX1LSa6WILRWt-OrGjZ5gJBMS95Q8P81kULMenft8RZcj6-xMGcO5eOPc8bqN-hvjSB47V6_WERSTbudsVDD_nv6-HWZhm3a1cLXttmrGBshh6ufox5HXa6IS3rgTKrWLO_c4nzfypFKEEzlh2lafwuIV3oUOywmaSVf77RZrnEX1H5ddVXVkZigtl-L2ZT3zzKWghJ7sQDw9XFiH_p3mXnV9jc8LZbp2_LP-Dz1LAMnV8WcFlj8UWQvH5NvYuxM61R039ZX5ELGi1tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌جزئیات‌ عملکرد لئو مسی فوق‌ستاره تیم ملی آرژانتین در رقابت‌های 2 دوره اخیر جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25547" target="_blank">📅 21:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25546">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAi_lbH_0xZlUff8DVH1Z__-rr1VgWtNY2KbpO1T-pbcPF8Ff1p_GxY2ZLKbNE8lshICluRy8amvMsSBMABDXCw2vz-ZyqNaU7gIr_BpvEBGP0D9dNSJdRrNlEC4ZRwUwucOAoYM50Wsbk9rIpPymFrdCCkNLwBKeqLI2OP9XrupLKGVmb3g8LbxtJ0V_9f_cuEtB3owQ9mNVGZLdkUhWgPf0NQ-QiS-yIyyb6dRiycRBFfs6nhwHdlb7zGQnqImQR-jf88FMPWbQie0ZJ-31FVXPoKq7SCid_OdybM0ONUBjUYIDjD87hX_uhvSTbTIbcEbIRgH4RB_ysogk4oUrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اینفانتینو میخواد فشار بیاره تا جام جهانی ۲۰۳۰ با ۶۴ تیم برگزار شه. و ارژانتین و پاراگوئه و اروگوئه هم یک بازی به شکل افتخاری میزبان باشن. مشخص نیست فقط برای یک جام میخواد این کارو بکنه ولی ظاهرا عزم راسخی داره که این پروژه سنگین رو در سال ۲۰۳۰ انجام بده. جام‌جهانی ۲۰۳۰ با میزبانی سه کشور پرتغال اسپانیا و مراکش قراره برگزار شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/25546" target="_blank">📅 21:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25545">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HL1GuVf2qVgm9FKxyCQHa2OKmwT9b4jnfHwvDjRyRo-ugD-IEem496hyQt-6VwTfpBNVfXYkH0UswzBFRgwGO8BbK0PFA0S5P-Z0hJM650L-57BCI0etk_BTjR2izdjE7l0bZyGcal8VAXtqpP6jD7clf-cOjkvI28vm2tvB67prtTV5Qf3PePQsnI6TovyHpxDwOPlF9IJl1ZCCnJDncupiucso36tc3_wcgcUtm02u4feYo1EXP0eh2UWhMbDy9p1RYCCN0xq7othW_TOD1DI36TamS9dVETjYY-ffG8K7GK3_hVC0Bh2V5p0h95mAnckNgR6umLuoeeCXtL-p4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🆚
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
🆚
🇪🇸
🏅
تکرار فینال دوره قبل یا شگفتی در راه هست؟
🔥
🏆
اسپانیا و فرانسه از یک سمت و آرژانتین و انگلستان از سوی دیگری برای رسیدن به افتخار حضور در فینال جام جهانی ۲۰۲۶ با هم مبارزه میکنند.
👀
⚡️
آیا این بار هم یاران مسی و امباپه در فینال بهم میرسند یا مسیر فینال متفاوت خواهد بود؟
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/25545" target="_blank">📅 21:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25544">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9d86d8e16.mp4?token=n28Qa8kTg0I0NRMpLGUlgy9ao1xW6EaeIbKWiTH7joeC3rZ72GfOGhTdDjv65xfBjkaSnwGDC1hzpcoxMAMiUHwILU2dcoteCMJ8K49j0dyu5SLvoFtgCJ1loS95BaD1v_oTs2oSj3PhBdgrALm-b5oEhKAX2-cpxfr8zGQZp-KOkdnhcZHVsTt803d7qAM9JU9MKqPO7jwx-p4j1Je71KwK4xGQY-vKEcboQUUe_ayzPGcR7HMfHnvVcSonBtNa3zxzFhs1dJlc2BClndt-PuNVR_A8B32pfP5lRTd9qMybdMT5yFXcHIG898sG8ilZIG5N_U_AsCQ7zHq9cIVokw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9d86d8e16.mp4?token=n28Qa8kTg0I0NRMpLGUlgy9ao1xW6EaeIbKWiTH7joeC3rZ72GfOGhTdDjv65xfBjkaSnwGDC1hzpcoxMAMiUHwILU2dcoteCMJ8K49j0dyu5SLvoFtgCJ1loS95BaD1v_oTs2oSj3PhBdgrALm-b5oEhKAX2-cpxfr8zGQZp-KOkdnhcZHVsTt803d7qAM9JU9MKqPO7jwx-p4j1Je71KwK4xGQY-vKEcboQUUe_ayzPGcR7HMfHnvVcSonBtNa3zxzFhs1dJlc2BClndt-PuNVR_A8B32pfP5lRTd9qMybdMT5yFXcHIG898sG8ilZIG5N_U_AsCQ7zHq9cIVokw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌دیدارهای‌بامداد‌فردا؛از نبرد انگلیس مقابل وایکینگ‌ها تا جدال مسی و یارانش با سوئیس
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25544" target="_blank">📅 21:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25543">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C64uHj60h43Fgif9E_8gjnUTRfzxTVDAPCUZkzkItayogs9X3DDapHkDe4nxxoDPLSyRhk26yYeQmxL-dTMcdtXyUh9oNAdXmf6nJx10hSCY5Plq10uNYVaJPxkiL8lWGMXGcAUuX3egd0zOo8dsWFl_GtjqYtDl_nEMXy1EQ_XpGIylB_RDluRAfHAtTiIy0iA2ZOXU82zKJS2kvYhfxoAyewCAoKc8tp4B1XjBCXBGQmIikwcKVOlQ3NP9mZ7NS9mru6ZRWlWDpH4KuV4QKEpA9TYuUKd3cIpKr4vpXgCp97T0YngaOJk5lvjHBhfqGCM2k7MxrCITZC6Y-7tfFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طوری‌که سورلوث در بازی با انگلیس؛ نروژی‌ هارو به فنا داد؛ وایکینگ فن‌ها عکس رو میفهمن. برگ‌های هالند از خودخواهی سورلوث ریخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25543" target="_blank">📅 20:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25542">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOgZzV_ROxzmpKMcg6CCznSR3jvn1xu0LIqmgRHBJSqVPRd7ZsCPJHU-JC3aWt2W3z4TYB6jTb94N3tm9-UANThUwCnQvUeLvxGzycW6hfDHn6W-mIRKUNhE6tgoIWo5dCTHL3MuglPl3zDcMFECXh6N7T_u_sCa_UpmJ3nFfTCavP2Ul9pAdQMJdFIsZ6ixkVBmqcUwgF2HRsvXmjcP95l1eNN_nOFoTO0Ig7WkhWA4rZVRO6-xZGtJr2KxGmQ-mfJTFwjraGzqmUf1YxQiZebtEBJOl7h2lh3OyH5I6iaYBkwMNEaiT-Tcqn9RzVhBT7HhVIoG402LJdYbVcsorw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دو انتقال مهم امروز؛
آرسنال 20 میلیون یورو گرفت‌و لئاندرو تروسارد روبه‌بشیکتاش‌داد و مارکوس لئوناردو ستاره الهلال هم رفت آژاکس؛ هلندی‌ها بابت این انتقال 17.5 میلیون یورو به الهلالی‌ها دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/25542" target="_blank">📅 20:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25541">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/104d086276.mp4?token=bNrwy4b9T0BxKGeEAIvUV2l8lpXrRtJZzEpBPAmRoKPtdMO-Z5PE7qwuUbT_qNX82XrWujIRUsz5EzLOoIRVzgcxVmFXPK5yl8QmUnGbC8EQGh6H9tNHvSmKAUNrtzD7aEO479Hi5v8SsYrfLF_R4m-45NinAfPqTzfIuVu8SpMwHiTXdWB6Nm7nk-a-1oKy4bT6c0p-2hJjCxjposytAgxZBKftZbrIjIy_I3tPf-C8FORAvh6XvIZi6kRvWYJyW6bDBry4OV3CXo_B6hsLzSlNKM6Hq5us6HY3fqny5-4dDDuLzUu0UAqc3mCx5-XSQyeTiz8fwc5LhbiwXQ6RaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/104d086276.mp4?token=bNrwy4b9T0BxKGeEAIvUV2l8lpXrRtJZzEpBPAmRoKPtdMO-Z5PE7qwuUbT_qNX82XrWujIRUsz5EzLOoIRVzgcxVmFXPK5yl8QmUnGbC8EQGh6H9tNHvSmKAUNrtzD7aEO479Hi5v8SsYrfLF_R4m-45NinAfPqTzfIuVu8SpMwHiTXdWB6Nm7nk-a-1oKy4bT6c0p-2hJjCxjposytAgxZBKftZbrIjIy_I3tPf-C8FORAvh6XvIZi6kRvWYJyW6bDBry4OV3CXo_B6hsLzSlNKM6Hq5us6HY3fqny5-4dDDuLzUu0UAqc3mCx5-XSQyeTiz8fwc5LhbiwXQ6RaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کنایه جواد خیابانی به قلعه نویی و کادرفنی تیم ملی به‌دلیل‌عملکرد ضعیف در جام جهانی: فکر کردی منم عین مربیای تیم‌ملی‌ام که 180 میلیارد بگیرم؟
‼️
هومن‌افاضلی‌خیلی‌جدی‌داره میگه فکر میکردیم که میتونیم تا فینال جام جهانی 2026 پیش بریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25541" target="_blank">📅 20:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25539">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRhwfE4ddqxQdDRKrbJbSM6ER19WVGuKRtfSTI3KG3psBKyMjDkeoj9JrpuQ5RQE4fOAiE3GNMD_4ttkyFrkZZn4yPeFA-t3ND9QY7ul71VxfJPPPiIHYN_OPmPJChLPsGW2hOKtot_ebZ2Hdgp8np5tQ4R5Tpgblc4bvQlQyiL3mv3P95cmeNoOiSEwRpvs116F7dhVAxFofDCNyh1VPCDnhBM_ho7jul_371pJnqN9G6qYm41zgc3beFg_sCtsiXgO0xxVIju-46zVKjkza1888RhptA-G3S4lrbgN6yTx7hQS8eSt8VURwAMUznNGl5jZe8Va0nU0EL63bZkieA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25539" target="_blank">📅 19:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25538">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYfwvFbEIRWbjZ9hq-Br5JBayXwdRdNEVLhFIELQn4e3OLvZSb5M7ztw6QXankyY5_d4ia4ifKeeb90Hcs6PSikeQEzBBjM4S7vQQF_k1wvdCXjDPqqt0Jq19x5SvEa8fttntD7QzT9NUfDYpqyjiElOE62kreMkY3MoWWtnCHfWXYn4dLOoowVLbm4WHcPaLZsFiuLFvcH5RcajZRTa9aT46BiSB8ZJ2vaa0omAfin49kcGzR_lnZReAg1LosC47bo-xFHLutlB593_wQ5kS5hwGLYX4SMC5vdFJmLOaHPldZq4-Ef_9G3KyMuc2kwHIbm7-aoTd5Pt6SQ_Rcue1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسینی در سپاهان موندنی شد.</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25538" target="_blank">📅 19:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25537">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2_uEtj4f9_ZzLlzv9_yrWoOTqQOZCt8mSjzhfw-UaJfxGppcV3FKqEThP41IwsbKo6H18dXdIWS97NlzOS8pZIsH_3x1o7lutUwBimf5g-mLHEcmxjwwqHyF2cb27L2j4NTUp0HV1nxDUubkQa1NeHFJDQWAgRtLZhwrZbQt5mIZS9OgBWuIElYbQSV1cvqrDU6ElyzBHb3OVtVO6fiUGClfmS-iFa0hgDoklIH8bWX0B86mSzJfWIolWGuH52R16eGydx-hMm_A6FY8LA8oXyUrvRdLeIF_tgzoitU0Ix4UIxV6lsqINW70O-ipDM5F7v47GN6nOFESPJpmX2YCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ امیررضا رفیعی سنگربان24ساله‌پرسپولیس مذاکرات‌خود را با باشگاه تراکتور آغاز کرده تا درصورت توافق‌نهایی بین طرفین با عقد قراردادی سه ساله راهی این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25537" target="_blank">📅 19:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25536">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146af45fcc.mp4?token=mhSMV7YSijRBZ7gCpKpnmNZZbqlqsECxQGIBqCP8atSrxgTHjP4ozJxisf_y33K1FVYRgUfeo1ecEV6Uf-AaeUYL25xSQeN5hxChfBwet-Gsd6B0b_TNDAk89IzysdJmEhBS0DHLhaNUi6QBCzdQIrCnnIVpvF77ouRAxCPuI9vrSrOlIhvn0CZ5GG7CfMaFEv6582HqH7bGY-EDcwDJjEBck4hWPUEFYCkJR92YkItLhYT-1agdJA2Wlc4efOJ9zuODshorRDfyTN5WN5gqQji2h9NwWUiv0n5M8q1w1Nm2qhsTDYMDq1j_M_vQ3QBoa6gk70os9pdNtHPhD82d2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146af45fcc.mp4?token=mhSMV7YSijRBZ7gCpKpnmNZZbqlqsECxQGIBqCP8atSrxgTHjP4ozJxisf_y33K1FVYRgUfeo1ecEV6Uf-AaeUYL25xSQeN5hxChfBwet-Gsd6B0b_TNDAk89IzysdJmEhBS0DHLhaNUi6QBCzdQIrCnnIVpvF77ouRAxCPuI9vrSrOlIhvn0CZ5GG7CfMaFEv6582HqH7bGY-EDcwDJjEBck4hWPUEFYCkJR92YkItLhYT-1agdJA2Wlc4efOJ9zuODshorRDfyTN5WN5gqQji2h9NwWUiv0n5M8q1w1Nm2qhsTDYMDq1j_M_vQ3QBoa6gk70os9pdNtHPhD82d2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بلینگهام ستاره انگلیس در پایان دیدار با نروژ:
مادرم یه هفته‌کامل بهم میگفت مراقب زبونت باش، نه فحش بده، نه به‌داور گیر بده که کارت زرد نگیری. آخرش هم مثل همیشه حرف مادرم اجرا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25536" target="_blank">📅 19:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25534">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ad69fB-Dh0-xEl-cRFP6mjEIMV-_QH0Bf-Wy-LamwJ2ADQh71OlDecJN81wgAm5WPyMj8IqZS6QYZXM4sjA-5ykR-scj1AZFLFw64-OdXkW08PwUpQmOr6YJMhsk1dMRx6tkcl0eu8zfQUi4ZGGm0YmgstXsiWAFLtr4t78t1pAPsPdnE2co-8oxwIbNJunpmWBPIKfOPgp4Y3Ux6OX9ESdNB9-BtS012GoSVjKoFxMMWnK799ZOgI5bWuJmP4DwgS5gS0Oi43YL0aw9_Vv0HgE91HrHWXNCbLwbm6BLjdj9ZQ9c31yj6g_jhlKcSVL0C0Kr9l1SUlmUPcdHeQPeNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوسمار ویرا سرمربی‌سابق‌پرسپولیس در انتخابی عجیب با عقد قراردادی بعنوان سرمربی جدید به دوا یونایتدبنتن انتخاب‌شد. تیم‌یونایتد بنتن فصل گذشته درلیگ 18 تیمی اندونزی‌رتبه 7ام راکسب کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/25534" target="_blank">📅 19:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25533">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kU10yv_tHEhItHvoiXrHF5_FUI3BCq9IbjT9zaM18Rh-RMtQJe90N3V6-gPu5BDkK6jfqE6vcBUU5-lusD2CY5MGqbnUYQvYy-uQoWgHKCyxXL5E4tRwjsutEFj9AnzHov3RkecBg-t8UijPiqBh8jx0FWB2OiJM1-VRddK7OD6oOBsiqq-ZzJZErwVcrBrVaPmYBnfrN0AufjVvrK67vZXGCxPJItOS6L0-TNysy8-x_h5VWmrj9Pp8xFbiQ9EoecKxDfwQHxPzVHwjZAAXRu2HTvPSGRumEA4_r_ya2hRrpTtKBqNQqYXdImCrRpvxPc6W_j1RUTTQ0PwLMxLPng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
برترین گلر های فعلی فوتبال جهان که بیشترین فالور رو دراینستاگرام‌دارند؛وزینیا بادرخشش در تنها یک بازی‌مقابل‌اسپانیانزدیک 16 میلیون فالور گرفت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/25533" target="_blank">📅 18:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25531">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIU0dJXnX4Zxd1t94N_IKtflr92gjEpwcWmlhlkycG6ZYgU-GbOOkbPxrBIfhW1xTaLA63dFKVw6xwPZLzA9qcsa4qLsXJ5MiQCNNxEdSDGJlvh5hMA20q91JvtKE9LrCHy99ILdBqv8_kW8SLgzwzauI-iOvWV5Q6cp9MjzJiS4Y2hWynFP81kblc_d_DKYhC9hSMwR1r_hKJ9BdHh6oiCsKhpN2X-6kyrmh5y_s9i6ArOgoquzhk0qHKqmGspZbB1WhOVahHcDhlzw053KX7LFEb36ixLBmem2_L2c54H-H6YySMeihX7BXporztDn3zCReIGlA9ZhbwHHHc3j6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec951e804.mp4?token=QlL3PcFYHv_91UYwjKJ5-q_i52fmXLo92SBKlor3OE5CLebE-qQtKrOz89omE3Wi_Hg-5t4KhEvHwBx4jMQucL0SWpOTpTXjgD_PX64VeErs4bY4WsVGFWe-db-MJK-mqTF1IqZKWj90s8yQcEOL5CNsrETI9COD9eEA_7pC2foayddsvHwzBb__lCFFVNCbWUlYeL6tNwBfL7DwR43shzzfM-NzQfVfiwbXVWAweADvccTcwwJ3U7EwMXqUqRJbucU5-p4SP9Dx7FBlVUKGbQVuN8Xt6OU-hBNzadaRUF8EOKNnYyOLrOzJFHRT17Ypa-e4G1s-NV6jS-wMFGvPjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec951e804.mp4?token=QlL3PcFYHv_91UYwjKJ5-q_i52fmXLo92SBKlor3OE5CLebE-qQtKrOz89omE3Wi_Hg-5t4KhEvHwBx4jMQucL0SWpOTpTXjgD_PX64VeErs4bY4WsVGFWe-db-MJK-mqTF1IqZKWj90s8yQcEOL5CNsrETI9COD9eEA_7pC2foayddsvHwzBb__lCFFVNCbWUlYeL6tNwBfL7DwR43shzzfM-NzQfVfiwbXVWAweADvccTcwwJ3U7EwMXqUqRJbucU5-p4SP9Dx7FBlVUKGbQVuN8Xt6OU-hBNzadaRUF8EOKNnYyOLrOzJFHRT17Ypa-e4G1s-NV6jS-wMFGvPjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇦🇷
آرژانتین‌نخستین تیمی‌درتاریخ جام‌جهانی شد که بدون مواجهه با هیچ تیمی که در رتبه ده تیم برتر فیفا قرار داشته باشد، به نیمه‌نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25531" target="_blank">📅 18:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25530">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2121b6e4e.mp4?token=VoNjwDHeFy8cVBVkd20bo9oTWTeKT5thkDLw7PJ3DUE31XqGEzwcQ_G0OxKWcJvLeKkFrVAycgsZtAaxBUXRs0mzC_8_He8LL2ZUai0pPF358Ko2pXyktRQjb53-rTWHUITEddvQezPsLVLzuSAb4Nqqy1Shf_qSJJ7PD239i3Cc7SHpdGfIrB7bLo7r5hrKU0Zz8rKlvBfTI81XjauoC9aI51ado-Dv-PC0EMPoCCZN3-RFRilVG4ubooJOwoduTL-824JEcCsuRmW89d6o7h_1d5P19tGcaP1pWaKfrlS7pid192AfFp7jZGPG8_KOuDoWh4YzB8OmdyJu4yCfkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2121b6e4e.mp4?token=VoNjwDHeFy8cVBVkd20bo9oTWTeKT5thkDLw7PJ3DUE31XqGEzwcQ_G0OxKWcJvLeKkFrVAycgsZtAaxBUXRs0mzC_8_He8LL2ZUai0pPF358Ko2pXyktRQjb53-rTWHUITEddvQezPsLVLzuSAb4Nqqy1Shf_qSJJ7PD239i3Cc7SHpdGfIrB7bLo7r5hrKU0Zz8rKlvBfTI81XjauoC9aI51ado-Dv-PC0EMPoCCZN3-RFRilVG4ubooJOwoduTL-824JEcCsuRmW89d6o7h_1d5P19tGcaP1pWaKfrlS7pid192AfFp7jZGPG8_KOuDoWh4YzB8OmdyJu4yCfkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسی تو نیمه اول با پینیرو داور پرتغالی بحثش شد دیشب: بامن‌درست‌صحبت‌کن، بی احترامی نکن. من باتومحترمانه‌صحبت‌میکنم تو هم باید همینکارو بکنی. انگار نمیدونی‌چجوری باید بابقیه حرف بزنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25530" target="_blank">📅 18:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25529">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a0b0e1c0d.mp4?token=eteqPP43S1FUtvNsUbflkQ5OmtfKuJwQPO9DYGg5Q3e_wyUttvJ6eEGfIyku8GnIA0at0EzOiZIaRiWYPPNU0bKtTQzNoqQFsjahyOmEnn6gURBedKVGXl5oi3aJW0vstyHZG-PR5EVyqm91gHbamEgMaT8-RB52o8fRQFFAJd86PrOx4-SxelvUDA7fYyc2xm9fUvBGJUTGeJXJy_WXBKO_UAhzOLnIzdc-JvJOCk5bF5dgnI4eRC09740xXFEIvLY68xPGExlhIlfFoQU4KOQQLZnvvCmd05B4U38kXfyU4RM65XyV2jz2eBS6byXPiUkXA32qTdnkXwOgmwLhV4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a0b0e1c0d.mp4?token=eteqPP43S1FUtvNsUbflkQ5OmtfKuJwQPO9DYGg5Q3e_wyUttvJ6eEGfIyku8GnIA0at0EzOiZIaRiWYPPNU0bKtTQzNoqQFsjahyOmEnn6gURBedKVGXl5oi3aJW0vstyHZG-PR5EVyqm91gHbamEgMaT8-RB52o8fRQFFAJd86PrOx4-SxelvUDA7fYyc2xm9fUvBGJUTGeJXJy_WXBKO_UAhzOLnIzdc-JvJOCk5bF5dgnI4eRC09740xXFEIvLY68xPGExlhIlfFoQU4KOQQLZnvvCmd05B4U38kXfyU4RM65XyV2jz2eBS6byXPiUkXA32qTdnkXwOgmwLhV4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیوزیبا از لحظاتی فان و با مزه لامین یامال و داداش کوچیکش که این روزها سوژه رسانه‌‌ها شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25529" target="_blank">📅 18:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25528">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjzZez1RLRWWE3jz41OBKo1C9tPYQ7-dny2vjLuPckqxPA7f60WewNldiuXE9NpSJOqLqR_dP9BrdU1UrkkKaT_gr9DAzy6IgcHPMoISsVk9nM8evu8sZ7lyoBhdVVxXycNHaIR-wR4fjvqwiZZpleY2wx43buGWQBJoltBX8K5xAgilk-uPAlAn9OCJKYtMEDqs_usVTjRRB9RHHnCAL1yLEebQYSwftDf_zLqwfG8Oeil3RL0oyNL2_ohYXVAaBCNHSAFxHzWiGzwCUW-V2oUIPVQbMuOxSHSbJzN6ALc6K9zJSIz19TEX_AlSrbFVMCbEQd-mgDCDUICQZY2hsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
👤
طبق‌‌اخباردریافتی‌ پرشیانا از اصفهان؛
مدیریت‌ تیم سپاهان‌ با‌ حسین ابرقویی مدافع میانی 29 ساله باشگاه پرسپولیس مذاکرات مثبتی داشته و درصورتیکه حسین‌ابرقویی بتونه رضایت‌نامه اش رو از سرخپوشان بگیره راهی اصفهان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25528" target="_blank">📅 18:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25527">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‼️
تو یکی‌از خانوادهای‌عشایری یه دختر بچه حالش بد میشه، بعدمیبرنش‌بیمارستان تست میگیرن میبینن باردار شده؛ میپرسن کار کیه!؟ میگه پسرعموم، دعوا میشه بین خانوادهاشون؛ برادر دختره که بازم زیر سن قانونی بوده میزنه پسر عموش‌رو میکشه، میبرنشون دادگاه خانواده عموش…</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/25527" target="_blank">📅 17:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25526">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nlp3YYw38bJsqLwAXnzQfuedYFqUogVDHrt6v2C9haUg7lFST5n9-lXAa9ut-XduSnqLTTTOr2B0tCNo5yVkDVtjw_vOZPRosQNYNH4oVzpDYemKqsyXcQFezvAudL02EvnqnyGB6Ej8_idwWq3smAZLnbuWPFJnCGSFhZPx70aHYFDpdtOBVNhKj2pKzTIOlWeVsWCojtYO65bC1quvLxn4p53p4pq_72B5Jk2w3Lnbd46YI8ugvA6FdOPLUC2AJBNhCJ5ubbpcc2cy1D6CVSRoSMPyw-jrFXQz07IYYxMBjz5Y-CWHPeGnNs2OWJ0y2kTAlthjBrUGG9yqQVWC9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تقویم
؛ پنج‌سال‌پیش درچنین‌روزایی؛
مدیریت باشگاه استقلال تهران هفته‌ای یک الی دو بار از سجاد شهباززاده مهاجم جدید خود رونمایی میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25526" target="_blank">📅 17:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25525">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDiF55z3Vdqqb0AE3JFs_thGTIyrb5NU4vbWlWMQyHlAOVP0V1yRWcYyByFEF3_ZqIC0-Z5aNkdi8sIBLFFgiD_F1ezNapMLGiuWEo0UJq3MgCQItcbw7QC5hLPEReFlcy7QeJXbSEDCfQ3kmWvC47-1a3BvQGqYAZ7l3lqXtIYofQehFfghlNbqJ-xNJjiG_w7Mw1UmNqAIHCwKs4jew_nXli_Bie08w0Ijm0fGmiyvzKB0lT96TI-CDlEhlb2lIvOkEvDEMrOhJK5ZCM2DZub6pIAUvuvrfKjLWyIQLlHIakx85Z3LLPJewL6TGihwz9_PDN2jhZtixWmZRXSXpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
آرژانتین‌نخستین تیمی‌درتاریخ جام‌جهانی شد که بدون مواجهه با هیچ تیمی که در رتبه ده تیم برتر فیفا قرار داشته باشد، به نیمه‌نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25525" target="_blank">📅 17:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25524">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kadc3jrXNX8RhhoLLlb7BNRqr2YbaHi8TVpEzmtjTHkjn3srshXvRfixZlpXqGe3_SqbbU3VsbGS5RQiz1KK8BU02GHOvlExhyWRx0-wkIWKJ45P-boDdCP0CKugdgfk0KNioTalPln6dXae_AgD2UjRlqc9xTc6xQJrRRZvPyEwq1SdSINHtsqKZuoRqz_g2xm8Pw30a4MQ3KxT4sQVJVBWqtLBOX11UFyNFThC-YisQJ63LqNz-QbDTQspWiitUPtKrEUtff7IBHI1_51zjDbV98-ojSqYitAS7-XNzSOT4Rodbh6R4VmFKsygRVg-YSQnh9beIjLiUXOn86xxsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
عارف حاجی‌عیدی هافبک‌جنگنده سپاهان که مدنطر مهدی‌تارتار و پرسپولیس بود بامخالفت شدید محرم نوید کیا در جمع طلایی پوشان ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25524" target="_blank">📅 17:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25523">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df9c9cac2a.mp4?token=vV2HYXGObD1ya5V1mqN3tiJBYwsiVj8pubVy3rtXrdab6a1_bY0fofeqLCtVxyqsnA9W5_mjAO6fTHgh-L6m0pMDAlD6nVMwuHrPPA2rQyuZnMxf4KdEJI3rY71K0QsvYfDF53Nn0Ty84WFNpUDm9v_Om2u4ReyMLYVAoVL8ZD4S6qyHxYicU7HQPBK-R-2O8Y0ts9_Fug7HU059a30dQgJBdifBapeheB_DdUVBSDOKUpmNoxtKodYmqu3vgJhSbpZqfwbMfzG258m43ydcQH-8_dAUls0-sj8jhvoD4VaLYtWmPw-CewEoC_UpKB3VhRW_NsHqKgK6DzHkfz1xLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df9c9cac2a.mp4?token=vV2HYXGObD1ya5V1mqN3tiJBYwsiVj8pubVy3rtXrdab6a1_bY0fofeqLCtVxyqsnA9W5_mjAO6fTHgh-L6m0pMDAlD6nVMwuHrPPA2rQyuZnMxf4KdEJI3rY71K0QsvYfDF53Nn0Ty84WFNpUDm9v_Om2u4ReyMLYVAoVL8ZD4S6qyHxYicU7HQPBK-R-2O8Y0ts9_Fug7HU059a30dQgJBdifBapeheB_DdUVBSDOKUpmNoxtKodYmqu3vgJhSbpZqfwbMfzG258m43ydcQH-8_dAUls0-sj8jhvoD4VaLYtWmPw-CewEoC_UpKB3VhRW_NsHqKgK6DzHkfz1xLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هومن‌افاضلی‌از کادرفنی تیم قلعه‌نویی:
شجاع پاهاش پرانتز برعکسه اگه پرانتزی بود پاهاش اون گل‌هم افساید نمیشد ما میرفتیم مرحله بعد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25523" target="_blank">📅 17:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25522">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5608c7ac3c.mp4?token=lQeHbI-z1qznxljYg9K0ZrJXoBzpa18MU9cn0McWb-deiUm4stcLONwT2A_SVLv058wwmoi4isx3fKj5ZD2KYYCNcn9eXOVRxRdnOT1I_QxLa1npWav-U7jtv9P-FnncilminrqRna3az96h5vOplLnifE7ZP3SndjMSrxYdBrJg6XYojq0CjDh42BsEZoRBJaMw1Gi-hTxe6k_wmHvUhroLnSKoA45mRW5lVrKe8fQKCdkgGVyRT5SICoUXwsr-XwyYak5vFnZjTRjs0PCfo3-carOmB1llgb_uF4wa4mEqOpESl_qPdpWbEr_wxhji1gi-Akz0j8AHWDtIGs5Bxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5608c7ac3c.mp4?token=lQeHbI-z1qznxljYg9K0ZrJXoBzpa18MU9cn0McWb-deiUm4stcLONwT2A_SVLv058wwmoi4isx3fKj5ZD2KYYCNcn9eXOVRxRdnOT1I_QxLa1npWav-U7jtv9P-FnncilminrqRna3az96h5vOplLnifE7ZP3SndjMSrxYdBrJg6XYojq0CjDh42BsEZoRBJaMw1Gi-hTxe6k_wmHvUhroLnSKoA45mRW5lVrKe8fQKCdkgGVyRT5SICoUXwsr-XwyYak5vFnZjTRjs0PCfo3-carOmB1llgb_uF4wa4mEqOpESl_qPdpWbEr_wxhji1gi-Akz0j8AHWDtIGs5Bxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🎙
عادل فردوسی پور
: آقای اژدهایی، خبرنگار صداوسیما وقتی‌صدتا موشک‌خوردیم و صدنفر آدم کشته شده ‌میاد میگه که همه چیز عادی است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/25522" target="_blank">📅 17:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25520">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ef9dd527.mp4?token=Z-GuagDR3-GzlKW4cCM7JmV368aP1XLaEOvExkKvg_V3Yjq2mHk3iECUwp8lABMDHgDdrwRbVT3w-ivLoShwdTWaquQP4pj6ZlMKJvi7eK70XqCe3DhtjJ3MYXJY8o1BJy1kJ8WxXhqxJiDY-XhTGxCEEsvyAK0j8ZSIPFlH6d_oSHaRWTs2jQi7IdwKQTIjDMEhxjn6MBa_VfvHpxy0fsD-QEfbiJGBLKvnYozNRFvtopqIbpv2wJS0mpsZUpeihGmmj66a2JMEthTIeVyo3jkvU2gdWpOedqEtJwvcbAVP3nM5q_KWG80HVgtjeHVi3e9_i0ZM2sozaCtR2zPbqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ef9dd527.mp4?token=Z-GuagDR3-GzlKW4cCM7JmV368aP1XLaEOvExkKvg_V3Yjq2mHk3iECUwp8lABMDHgDdrwRbVT3w-ivLoShwdTWaquQP4pj6ZlMKJvi7eK70XqCe3DhtjJ3MYXJY8o1BJy1kJ8WxXhqxJiDY-XhTGxCEEsvyAK0j8ZSIPFlH6d_oSHaRWTs2jQi7IdwKQTIjDMEhxjn6MBa_VfvHpxy0fsD-QEfbiJGBLKvnYozNRFvtopqIbpv2wJS0mpsZUpeihGmmj66a2JMEthTIeVyo3jkvU2gdWpOedqEtJwvcbAVP3nM5q_KWG80HVgtjeHVi3e9_i0ZM2sozaCtR2zPbqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
شوخی‌جودبلینگهام‌ و ارلینگ‌هالند در حاشیه دیدار شب گذشته انگلیس
🆚
نروژ در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25520" target="_blank">📅 16:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25519">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ic3kMeDtyzmCf-EipkoRxfCMpI27Y8iCAjiSI-gcnjPw68xJGQkhf1t37IFufRY8nWdR5SyBW8fs9kebUYeMrCO2uEjH0x-XyGZNuYc-rPAms20ovclr9IZ4dXUFQBYX1egqMBaTzRpg1l3ZOoN6rSHgi71TpY9vqsNTt-vBPgwK9eFL_l88c86u00Pxhomw1F37O5hJoZUhIVwO_YjIRQoKlNaJgacoLGKYh5ubL2wOal4mcNutY3GnmbF0odZhBftycB-PuJmA5dXhn3P_mDvdrqIS1KRCu53KmT6_OyLaYjrzu7vR05sygI8e7mHFs64tkzu2XJBxF53UF2gOzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد کلی کریس رونالدو، لیونل مسی، کیلیان امباپه و هری کین در تاریخ رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25519" target="_blank">📅 16:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25518">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ct0bGzs24IOe0DvEzz1KkBs7FYsClnyCpfA_pBAW5tVBV73jGj9MufY2Q-ipSPAdyqDps_E3Fgq6GJ9dH1V-sFnagXDGYVW0sHDvppYyRTin93C2E0lYGPRHbBwwVTQXVDOAmz7X79DGNNeRwiNEISpB3vSvYUOODhvmbY7FgRXubJ2C3LE5B8e-wlFkwAuypxVpRYEHJoPjpaTvDwdJbLMAGWO37EkPoRtgacXZtAzW6YXFMN_mSeyk6zkHsJeRY2C1ljdb08YCFftCEn9AczzhCdTDbu4Y8Gl9eR_mnRdTfZzHgrRJ0QY3hagSt4bUWMdtnCgZE0k6cPuxAONLDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هایلایتی از دو تقابل جذاب بامداد امروز مرحله یک‌چهارم‌نهایی رقابت های جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25518" target="_blank">📅 15:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25517">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HR-Ya7jPtEVUDY_6o7KAptaCbjNhVifM2rkX__-HBGjI_sk2sAzjZxBapvG9_lKJdQYfaSaThkEh1_5RXInbifakPw10nx-yYCSCuEcBnQIX4phN5a61f-Yq2pCjQbJN6KsKGaoY8gvUW7k7aWteJkNhcgOr-LcpYRu8q8AecHr0ePN7w5Deu0W0lp8xNh0SBm3pzgCBnKDlx46E5DMhplmOnYuxaNWbwTZQ6VPyXPY8HFVHMDG2FmdSS_Z-zjSe58KYUuhx5cLdHDH39PauFpUZbDOH3dOPfanJOvEcTnkQ4SDSWBot8XDVwj9vhc-iayeD5HlwOJ1HrJgHFOXnGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محسن خلیلی معاون ورزشی پرسپولیس؛ بعنوان سرپرست مدیر فنی سرخپوشان انتخاب شد. نهادهای ذیربط مجوز افشین پیروانی رو صادر نکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25517" target="_blank">📅 15:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25515">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25515" target="_blank">📅 15:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25514">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GV3QVjOfCsMQ0MmS_hgEM0xFNmhcJdRVCEX1WVvANzTIsapJDO98t6TFyhmgs8-Sb3vExJYqvXEeGns1g5oEX2RWd1Btb05RJmMCGyOIZBzwelAjt0JBAFAW_BKp6KRWdSuX95KqHdpzbmdEfCjDloJulc5WCX-jLEuQP266Q7xtyoDvvsVvHxz4fvXJKmhVHU4xvcJOkGRGOMsWi8R4xG7WlvUWC_xnGiI-QHenRE6iF7gLQz9DCWyNdnqYtwwBWk1BvG7LyjmhQBY9XHxLyAOYkVGUlYD0RfRsq0o1xYv44KD2XrjwTFjp04NhJkKcxLPvinAQErmZAzeadqHklg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
#اختصاصی_پرشیانا
#فوری
؛
یکی از بازیکنان فصل قبل پرسپولیس از دست مدیریت این باشگاه بشدت دلخور است و به دوستان نزدیک خود گفته اگر پنجره استقلال باز میبود تا حالا قراردادش رو با آبی‌پوشان امضا کرده بود و یاغی شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25514" target="_blank">📅 14:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25513">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5IBFM6qEzxFCp-TiHv5LteCxF-Wele5wm_H3EiBq4SwKjf2KCJV5ygM8OhD0aoDaaFA9CZM5X5HdVSOiCJAkaNlrf59NExMethzh8Qfs5yJh6mN4yy7_ImkI_AQqZq8Ty4cm3bFGIi-hHnVthNPYDnZgqBPiv_MyBBVrr5iDjd9547Y1eIK3DI6NpzKazW5qgTSVqc2ZDSpW3s4PczENl55fahBkVPGl3fNARWwMHkDsfQjsSVAt7eDKP-Mk-hGFrD9c_oKANPc0NNHKcHAjpVeLNdSeqGHOaPDVUFmGmFfvnpf0YV2ogxWdqlIa75JBkDg0EekDtvhG5sIyuFksw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد کلی کریس رونالدو، لیونل مسی، کیلیان امباپه و هری کین در تاریخ رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25513" target="_blank">📅 14:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25512">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60fb9d0fb5.mp4?token=L0qoCuLQyawqVPrbZZB8jPi2oSszLfl2GT2KYBwbNhDl6ISpnE-9TqRuxOg0IY0jQRQertCh49qtTdN9Eym5lwkNk-Ox59y3R2ABq38jZeyrOGPGPVT6iGqgGQr5hmccy4bkKkexlLRTTZ0gXPFn9zJG3W8J-je279vdjyhnJNVaESuc3ut5W2WLh1V9wZ3ieteDrPrIbj1M4Kqek5CaOgcHBnAP4HH6lZgGN7DmYMzK-eHHjx1DC1xc1cVHLzRzSQesW8TVfBO9yfeaJN5c9in7ZLir32LVTHWGJjznltSq3GyWQWZpAnFs3JNcBE2iGKLA-qIHUJTqqo3cPK3ufJ8S8-3TKtX8bAb5PPBTQj21AKVyW2cXyVngaUYAFo_8WEZfzs2oMMRp9USCHLT8myaP-c-JzAdXznYy9B4SPRnA_1G8UxwGLmYPh22CXwz2xLVR0ldwSwxMRoI124Vzi96avb670EQX1LJo5CP8zb9OK6J_-gfsS6x1g5Wj7yk_hh83bV2ZUcFBM6UXUHCJOUQuzEH1FroYzN2D5aXpvVmiqyokifTdbTLm4l3oM1zl_FJ8cBVr4kmtrrC-OS-2vtgmX0UH43vAVAN1L7AkQi13j6v3ZtjIS3Vc1yPFh4R6Ch0iaJ6wShjBSs1WJAdJ-hkdfqtPrdoqGM-MdTkoGKE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60fb9d0fb5.mp4?token=L0qoCuLQyawqVPrbZZB8jPi2oSszLfl2GT2KYBwbNhDl6ISpnE-9TqRuxOg0IY0jQRQertCh49qtTdN9Eym5lwkNk-Ox59y3R2ABq38jZeyrOGPGPVT6iGqgGQr5hmccy4bkKkexlLRTTZ0gXPFn9zJG3W8J-je279vdjyhnJNVaESuc3ut5W2WLh1V9wZ3ieteDrPrIbj1M4Kqek5CaOgcHBnAP4HH6lZgGN7DmYMzK-eHHjx1DC1xc1cVHLzRzSQesW8TVfBO9yfeaJN5c9in7ZLir32LVTHWGJjznltSq3GyWQWZpAnFs3JNcBE2iGKLA-qIHUJTqqo3cPK3ufJ8S8-3TKtX8bAb5PPBTQj21AKVyW2cXyVngaUYAFo_8WEZfzs2oMMRp9USCHLT8myaP-c-JzAdXznYy9B4SPRnA_1G8UxwGLmYPh22CXwz2xLVR0ldwSwxMRoI124Vzi96avb670EQX1LJo5CP8zb9OK6J_-gfsS6x1g5Wj7yk_hh83bV2ZUcFBM6UXUHCJOUQuzEH1FroYzN2D5aXpvVmiqyokifTdbTLm4l3oM1zl_FJ8cBVr4kmtrrC-OS-2vtgmX0UH43vAVAN1L7AkQi13j6v3ZtjIS3Vc1yPFh4R6Ch0iaJ6wShjBSs1WJAdJ-hkdfqtPrdoqGM-MdTkoGKE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اگه ایران میزبان رقابت های جام جهانی 2026 بود؛ این مسابقات جذاب چطوری برگزار میشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/25512" target="_blank">📅 14:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25511">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l97P_N7-yZn6eoruqZ9jmlPk6a5OKVpl-lmHjOSbAvffwqaWEN81HqFo3znl0U_SM4do0KfnIWTgo02OKJKU4U3oAIBlOkrTTc1Ixq3UiXiknBgfbcmKgN1yT0Zv0K6gRVkbf03-5sTg1jA_dPO86uskhSmDh3dgSXHA1H40LzhkQERy2y6VxwIz5xqrbO2QToxL9ndhYf68qSpZCEjMJrl0OM78DC3fh-Uzsn6soUm33nlK1Ke4TpJs_3Biy_2S5lNq9KaeS0mEhoKa1OKs7IDfqIEYf-Lvu_5CvqoQNVOUTeFRJt3HGFXX7Df4FbokO34F8LDuwZaS7s3SPLC31A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مدیربرنامه‌های علی نعمتی؛ این مدافع ملی‌پوش باباشگاه‌لوسیل‌قطر درحال انجام مذاکرات نهایی است تادرصورت‌توافق با این باشگاه قراردادی دو ساله به ارزش 850 هزار دلار امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25511" target="_blank">📅 13:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25510">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFe0D73fwm4sXHT_kD-vEHalyXLgcSYoalvAyxd8V3Bu8MLd2L9Jtfg6Veee6g-TtxPrBTIxHHiX6aS-Q-9nFJlw7ZDei51ZzRQ9LL5V4-c4Bbq9JXjCz6zMAe2V178E5PFeRBxlnz5NHvSS-2BenZandkZDIaQ7s_jetrrAeB-Y7G_GmTpEPgqJvcIdZvTiEChvw9jaqw1wBdXanwgI_JDXxTUu0NmkowC1uWo6vE98Nw6kDaiTRGhx019VPPMvYE4ZS6hpV_WS-zChXiVqhWYg3hi_Bd03do9HNrypG3ph_iQr-td5burMTkPgY_glkwTHVwKZHofksiSTVbDKfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ آخرین پیغام منیر الحدادی به مدیران باشگاه استقلال: وضعیت منطقه آرام باشد این هفته به ایران باز خواهم گشت امادرغیر اینصورت باتوجه به شرایط خاص همسر و به‌دنیا اومدن فرزندم نمیتونم باهاتون کار کنم و ازای فسخ قراردادم مبلغی برای شما واریز…</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25510" target="_blank">📅 13:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25509">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akgcnjT6QE6AMd9UohffK6Ryr47uxcHnBFyPpWfYzIwvs-c4_gH98ckJJlOgKKgR_dxWGaL6lHHvfTUO3vClyLItQbOvvGYuXf2YETGdIo4VLIbC6UFE5B2PDSiwaOWEbrZqOZnEMUw6Z5Bm8upQUm0KSfMtpDNtWbCTMpef1TOSMw4CXAvrcUdd9Mx-sgi0WnFhxPAUPSia_UGu6Kg-SP6Z2uPvgcIoZTbIhf1RY_ryahm7zuPTPiJx04TaCHbFqjNly2_4tVtk1UWKyqy26-0v88EUjKcu5ashb9LdYt0UDtu2owlFIZ9Kv-smP3W73nMP14xNL_D54bUQINDh9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ مهدی تاررتار نام سه مهاجم خارجی رو به مدیریت پرسپولیس داده تا شرایط جذب یکی از آن‌ها رو فراهم کنند. بزودی اطلاعات دقیق‌تری درباره این سه مهاجم میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25509" target="_blank">📅 13:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25508">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOqbknAN6JskBmPtjac8JmudipZTL6CJY-Kj_kwmb9y42A1CW9CwNWbtk1uC96asBiBzxC5YqW6AYHB4MCNWH6PF6yWct-ULTr9VHOfZK3YZ0C0FbaN22kDDWAPj7DkqwkHU2yfMu0rf9koE3zVeE-CXT3AoBA3Usz75Oi1aElvCxNnQ0CzMHxqAH0j1cDEoLg56HzxkengaiTU3qdKKquI7WX7lVZbdlCjCNkvWDKiLdKqMTmacaXLbFOoCxpjrdUwfkFBOK06ZYFidQK-aw2j2H3LpA6FpXOPP7HxhaiuE4F7WaAXxflcSvmH5RpN7bpMeEr1fGD1egR2SBnkw9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25508" target="_blank">📅 12:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25507">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PloSGvSQTeH_u4muxEGcAW_Zf8bMY4-aXSsSpOCdTzXhRFYA-3ZYZgavicg2-n3Dy_n22aO0QIda0k9Ascc6LvVAXaZZRGKwvQH60g9PJ_mhc2kctvr4zKL4ddeqYRNLEuFHwfdObGryih0-RXihDgoofAxpocGs19dEDUfTwyCfQk7LPh4pFuiynOJPlj1TGu30yXiNbQfX5pBk48Ihx3A-6nRhNwqJEz1FMxCq8ntefbVB8hBVcvOW9TTHn3AM9nve1OUX9BYj_w0rrLLQame7MZJwVVYetI1IjH7Az1zFkNkwJP6868SHw3bli_TClL2jSSl0b4M2nEUCJedLww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
عادل خان فردوسی‌پور پیرو خبر دو روز پیش پرشیانا؛ مهدی ترابی برای عقد قراردادی دو ساله با مدیریت باشگاه پرسپولیس به توافق کامل رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25507" target="_blank">📅 12:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25506">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjfPGDAQ4Dw9FtdWh5QqSnXCDlGGJCZGzLlriYmja2w1DlIxd8CbNgkdIc5BF3lrRzj9rwLfeMMGULr6jnXA7AzA2GHwRS4SVfy7Y_Dhd86490dIABPcJezifoK9BPw-UGYkgTzKlZUE688LgfOQL4CMpBqbw3Vu8LnUzFI6gF37ThTmU1Z0OSDPvcTa3U6rQKdyG5RkrFvgocOYiRiiQfb8A_XnuZuLQlFSU26bbuc_mN_sZP-zZOPnMZyhQTm-_fahWtfTKB28xBRjXBjUkXI6da65ODrv6S9yn4c_KkFGD_dK5PqDc0gPgnMX1MLShH9v5FgZgRECekzb9i7fRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا
#فوری
؛
سهراب‌بختیاری زاده سرمربی‌تیم‌استقلال روی جلال‌الدین ماشاریپوف نظر مثبت‌داره و به مدیریت‌آبی‌ها اعلام کرده قرارداد این ستاره 30 ساله‌ازبکستانی رو دوساله تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25506" target="_blank">📅 11:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25505">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c5482437b.mp4?token=D62YFNn8jTgqWR3Xfepx4k5IzusO9rlCrLE03_OuNlhEJXJTW8Ifa1Avdfse0X2myPM8kEUTs2bDsV_S4o3pWUC75mFFVTViauxyCTp4oGHBTc8RdmjwuHS_80wX-fhLiuGjdQlU5crWohKMRBwaVAkVOmt-r-0PuumxPIRpx6Vi_Hm6yAZde1nt6UAW8kFygtYy8AEDHq9K98-uQbQ9t0Ixtk20Ocj5TTn1AzQkjU2j_0Jbi-RLZHTVgf4tg8qUUnvejiSBAA3ORInl8ooBNOG13MCvWc53BsF2Fz2jodhFyRSFgAmPiJE6vf60Vp9LBkn8jSSOoBXV3CWzcF77Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c5482437b.mp4?token=D62YFNn8jTgqWR3Xfepx4k5IzusO9rlCrLE03_OuNlhEJXJTW8Ifa1Avdfse0X2myPM8kEUTs2bDsV_S4o3pWUC75mFFVTViauxyCTp4oGHBTc8RdmjwuHS_80wX-fhLiuGjdQlU5crWohKMRBwaVAkVOmt-r-0PuumxPIRpx6Vi_Hm6yAZde1nt6UAW8kFygtYy8AEDHq9K98-uQbQ9t0Ixtk20Ocj5TTn1AzQkjU2j_0Jbi-RLZHTVgf4tg8qUUnvejiSBAA3ORInl8ooBNOG13MCvWc53BsF2Fz2jodhFyRSFgAmPiJE6vf60Vp9LBkn8jSSOoBXV3CWzcF77Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
تلفظ‌نام‌مدافع راست فرانسوی بارسا در بازی شب گذشته فرانسه مقابل مراکش توسط عادل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25505" target="_blank">📅 11:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25504">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcVEeV_dSezSoDQqaZfKZpj61nw41qgQ766t7X0Fqk-wHb3seZH0oYTGS6tnGVut895HKpsXUFgEOURutyMpLnuJzl3FfDVvNZeiGsM9fQrAgkkM4gQ4NGucO0vMghy_48g7ooPWaxqiEpzlrSXpFddsQcak4IvPeEeGrOaqhc78tF5u5tor_4gCNOrP1jiJgl2WN7OPgGlPij8-B6GKML0reokRV2Luv1pF0fTatunO3tI6YIyvBu-Xht7ItLVfJyhdXaQFSIBJx0FY_B-n0dZ0dzkI7Xgo0WnSbUKBcIIk-QMZ0kZwFDPjhoNmkfDZBsWUZlrY0aFwqa1UXP49Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی‌پرشیانا؛ جلسه مدیر عامل پرسپولیس با مهدی ترابی در منزل این بازیکن برگزار شد و دقایقی‌قبل به اتمام رسید. مهدی ترابی برای عقد قرار داد 2+1 ساله با باشگاه پرسپولیس به توافق کامل رسید و به پیمان حدادی اعلام کرده درصورتیکه تا هفته آینده مشکل…</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25504" target="_blank">📅 11:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25503">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6u8KDvySTSz7g9cC0OqaMBHkViKffK1wFprPImlkk9n_wv__AsYUqVcNhrpGsdEtEE4et47-2Fgx2IB6DdAwy90EvvGv4aYvPKeUO24O8BrLG148HnqY2aVkTRKWZ1Z3HXIlSnKlWldMkMrj83TFloV95KS6TaVHi_TsYBsX-VWzKjVZO_x0w1vMKdRCU7tAIsVcOx4IXYBNhdxEzss999LM_eAHJwStn4_CwjBF5KFrq2qerGbFHI-JrMHPgrv996qfcT5AgFY7rMVQK58bc17063msQtJo-ifQvDhDU6M8HGOlJs-6-gf6hILcYIdWR1oJr3geVl_t9JyOzf_sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امید ابراهیمی هافبک 39 ساله سابق استقلال با عقد قراردادی یک ساله به تیم لوسیل قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25503" target="_blank">📅 11:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25502">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a0f9a7afc.mp4?token=L-7q4s3PnQnKUXBawmh4e1Xi2zydtB40jlNlrxBYAWwJ7Y_OE5NPgPlveztz6bCfvp1wtTxuhUxMmY7SeyItbJNBwCEVFf3rgo3jONAuTbNgo6-AyEjGNl5jkccmQmmVuZWQU757mXEWDJ3G_-OOvO2JbFQRlzb8iEsi_ednHJW1wc4q-leWNiS4c6CYF9MuZukRXwKs9xQ8NM4KL_S8OgHCYXnROPIRCw5Rnl1WQUewjMPNCqdMLgIsk3c29rNgimBEUIXtX9EOGHLPb5JAhdyN871w0PG04DFbo3-Q2mEW10fpYFIe7qhawOvyYVPy-Y29ZI-Vy-0ByWQ082Exqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a0f9a7afc.mp4?token=L-7q4s3PnQnKUXBawmh4e1Xi2zydtB40jlNlrxBYAWwJ7Y_OE5NPgPlveztz6bCfvp1wtTxuhUxMmY7SeyItbJNBwCEVFf3rgo3jONAuTbNgo6-AyEjGNl5jkccmQmmVuZWQU757mXEWDJ3G_-OOvO2JbFQRlzb8iEsi_ednHJW1wc4q-leWNiS4c6CYF9MuZukRXwKs9xQ8NM4KL_S8OgHCYXnROPIRCw5Rnl1WQUewjMPNCqdMLgIsk3c29rNgimBEUIXtX9EOGHLPb5JAhdyN871w0PG04DFbo3-Q2mEW10fpYFIe7qhawOvyYVPy-Y29ZI-Vy-0ByWQ082Exqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
نروژفراموش‌نشدنی‌ترین‌تیم‌جام‌جهانی۲۰۲۶ بود. جسارت‌وجنگندگی‌کم‌نظیری‌داشتن و شدیدا دل‌همه فوتبال‌ دوستان رو بردن. به قول یه بنده‌ خدایی اگه ایتالیا مدل گتوزو تو اون گروه اول میشد جای اینا میومد احتمالا این مراحل رو به چشم نمیدید. من خودم بشدت فن ایتالیام ولی خب مدل اسپالتی و گتوزو افتضاح بود ولی مانچینی درستش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25502" target="_blank">📅 10:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25500">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfN_X-4rJPRR4UdsSnUxNaP8xIQSKR9n_L4uEsjX60gMF0QqVgZXCGXNL-l2NfbB5z76rJs7F8ftR6bYiFsdpOB4KYTGOHWG0xy49WiHUfuJ4Ly-cOXAPep9nNXgN0mHZl6CPJ4Zc9wCHDMETXRbV7fCtMLaaYHRcLn9YvKjzZ3S3WNBmbFWBEBQGulctlM0WBZWSrMcVvwAHK1fqYHLG_heG7WpYM1I0yqavrEiY4wR9RyKxM9Ukk13yB1AD0YdfK1fCx1obHuzC5a53Z1xDNqax0ZxY_dBq8pECiWLGOahEV2poX-HkG9RttAqsJm6z8gLn2IYA8dY2hjhh98cLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4928773d8.mp4?token=uwapzvFV7PgBU3Qg-mgWfQeaDGHIrdweTV65_SzRTeqrBuCH6lgoIzJG4j5ohPDrgBh5esZOk4WPLw2DTUbU_N0bW8IIzJOqsOjlz0W_eG2tiwsEdoIUoFk2BqprhglxX4G0W2CIx6ppNGGzUntVim5JXXgHgQ3aBEPEK09nkAkI4qlhsedf_JWpZRHEEKtVsF04b27otCRYJK_BJWX1271jqTExtx4wMB9_LEOKEyb-5ASBQVkNM7_1EkLlBlb0750tu9JOCI6ZoHbO2YSymEm7jQJY82vLkq0gwKqFV6SsAuv9zMCSMrLw9rVKUKecbzECkIMNUEgR0AfA4wQ_iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4928773d8.mp4?token=uwapzvFV7PgBU3Qg-mgWfQeaDGHIrdweTV65_SzRTeqrBuCH6lgoIzJG4j5ohPDrgBh5esZOk4WPLw2DTUbU_N0bW8IIzJOqsOjlz0W_eG2tiwsEdoIUoFk2BqprhglxX4G0W2CIx6ppNGGzUntVim5JXXgHgQ3aBEPEK09nkAkI4qlhsedf_JWpZRHEEKtVsF04b27otCRYJK_BJWX1271jqTExtx4wMB9_LEOKEyb-5ASBQVkNM7_1EkLlBlb0750tu9JOCI6ZoHbO2YSymEm7jQJY82vLkq0gwKqFV6SsAuv9zMCSMrLw9rVKUKecbzECkIMNUEgR0AfA4wQ_iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25500" target="_blank">📅 10:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25499">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfvHmlKHgYENkHazSYOIF5aGpoI6QtMBE4UlnYyEFVDyge5KoIW2rZbu2v9klAG4o6qX-gVCjHzdd8yaKifStKCk5-WdjNFhb8XCDyOCOQqttj3fx0K8PCfd72eRJtVuL7vHqj0U4b-AVNNyyIRjUyDBK4uupR6vpywcyywBeitJeJp-kiRmJAfRag3eFXeOWuJ6-VlnUSotjGVLKjT2eUW0ltZFXx3v68i72Ktxgqs9nTOLFn2mK0AN0Ov99tORAm0rlbgc9UF9HEo9_qQrNFfAvknj38N1H8nKtg62XUYHEVPB9UQsa03MwIzgwsCo88iT6aHYmS8bSVyOVcDlYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛ازوقتی‌توخل‌به‌‌یارانش‌اجازه‌داده بازیکنان انگلیس دراردوی تیم‌ملی‌میتونن با پارتنراشون رابطه داشته‌باشند جود‌بلینگهام یه تنه این‌تیم رو به مراحل بعدی جام برده. انگلیس دیشب با دبل بلینگهام برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25499" target="_blank">📅 10:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25498">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXIWQ6G0hDIPJRreqUuHcDGNMMlDWLuLn6L3s7F51EzXNSmTU7kRmVEsFo9YwureSqxeEBoBhgpfAueiBGjSDOa-3G9K9Up2eoYiy0WgXZcrlkeKzWy0OGJb-nJrof6S0QvwUKREZy4dgVrhxbzaHdVZmVvSqeKxLbgTzx3ciJHf9FX192W9TfXnv2tfSJTRRrc_upnkWHtrtDlRtGN0_JaAmZWrTajCYGROe6Z28-oEr1FUBU5NhyYGgTZJKnSMCBMKqKBelJpryb82trXGWZesErX3I_P-1mkctbHO1SJo1nZstIOy-J_RfwuHXhVECmDOSweXgi7dCTH7tmtzlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ جلسه مدیران دوتیم‌پرسپولیس‌ونساجی‌دقایقی‌قبل به اتمام رسید؛ نساجی‌رقم‌رضایت‌نامه رو550 هزار دلار اعلام کرده که حدادی‌امروز درجلسه‌به مدیرعامل‌باشگاه نساجی گفته تا400 هزار دلار حاضر است به باشگاه نساجی پرداخت کنه. قرار شده که ایری…</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25498" target="_blank">📅 10:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25497">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda5f52119.mp4?token=f-64qsjKGe6nLqkUjo5HHaESuoDA4ezPhp9J_6L0yDDnBwS0uwAxMP-9_5DO1yZLTOUN-0b3VqZ99vYykEA2iPGBIFy03pKgGnSMHOVZwWYsGZ89dkLgjeHVHO3tXMJBLXcSQMRX6grZtpcGJrwmqyuFpqpVET5_EyIZQXc9ttNT9KFrPUafHk3VwdrjKJ0Hdy4w85twTFeOx9MnB9vKGzP45xszaSnjn6hEfBCSfQ8bGwN0o9q4bfm5T9FZAaMSLtyIt3uDksd0Cx7UhAenr4omF0DPq22wxCZ5kSBijqk1vl4sL0UIXGxofW6v9pJOZCoH65JOG0xaRwx_pnE3XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda5f52119.mp4?token=f-64qsjKGe6nLqkUjo5HHaESuoDA4ezPhp9J_6L0yDDnBwS0uwAxMP-9_5DO1yZLTOUN-0b3VqZ99vYykEA2iPGBIFy03pKgGnSMHOVZwWYsGZ89dkLgjeHVHO3tXMJBLXcSQMRX6grZtpcGJrwmqyuFpqpVET5_EyIZQXc9ttNT9KFrPUafHk3VwdrjKJ0Hdy4w85twTFeOx9MnB9vKGzP45xszaSnjn6hEfBCSfQ8bGwN0o9q4bfm5T9FZAaMSLtyIt3uDksd0Cx7UhAenr4omF0DPq22wxCZ5kSBijqk1vl4sL0UIXGxofW6v9pJOZCoH65JOG0xaRwx_pnE3XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇧🇷
وینیسیوس‌جونیور ستاره‌برزیلی رئال مادرید امروز 26 ساله شد. او تا کنون موفق به زدن 128 گل برای کهکشانی‌ها شده و همچنین برای تمدید قرارداد بااین تیم با فلورنتینو پرز به توافق کامل رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25497" target="_blank">📅 10:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25495">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e63b6abc08.mp4?token=Vg9f6pbXD1rJulEBmI-gi85Nbg1hYKMDSLqhcTBkkgK5WJx8g9kgImpIMEVpgQ3FAPLIK-HYqwScGsEaQ5lDAGVlKXk_9-53yfVGMG1iNy85FDKBnZ-knZYu9flz9rBaHMWZL1x8gP4mAylMqI3tkBZycTl3oa0VdzAeGtt9QL16jTB8gqyx8AMeyxkJkacxIaAAh_jcY3wKEJJb-pWiZUntqoTvBPrN_Shwk4CC24xH1O9IWIjQvwFneduiYlLm1QJsy5A7A0s9UaSRIe3avP8HEYXMRdQSmStDaxkP9JFIzUppurA6hzvHcyyRCYiR7RG40QzT9_XrKDxMUpncMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e63b6abc08.mp4?token=Vg9f6pbXD1rJulEBmI-gi85Nbg1hYKMDSLqhcTBkkgK5WJx8g9kgImpIMEVpgQ3FAPLIK-HYqwScGsEaQ5lDAGVlKXk_9-53yfVGMG1iNy85FDKBnZ-knZYu9flz9rBaHMWZL1x8gP4mAylMqI3tkBZycTl3oa0VdzAeGtt9QL16jTB8gqyx8AMeyxkJkacxIaAAh_jcY3wKEJJb-pWiZUntqoTvBPrN_Shwk4CC24xH1O9IWIjQvwFneduiYlLm1QJsy5A7A0s9UaSRIe3avP8HEYXMRdQSmStDaxkP9JFIzUppurA6hzvHcyyRCYiR7RG40QzT9_XrKDxMUpncMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25495" target="_blank">📅 09:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25494">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hf1s0nZNQgJHMMAl5zOnCZWNw-WYV1C8Yezzk7bMCLGaQU__6VLpUc6zeBpXHLRe4P4rfngwX6clfqu4aTHf1w9pGPaqMPPbk88kQJSNE4Ef5nDRYYhAF1Ix_iVmrBrx-XvAW4DRSg16D26YuxIYrrTIlMcf9EhCmZnJIlQAWYGhiAtwr3RaSgDXx6pji7OqLnaOQseQTu7ABeE0HPgiLLscduKCBcYN60MBIabVyq2RDZZzt_WRQlyxk6qvrrDfwaRq0QRF-vi0LlNZQC0nEwt_qW252EvkpW_-QLFWK8EBTkgpX9lv9L3r08jVq6WrkKVXvFcT1TWS7MjUgIh0iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛ازوقتی‌توخل‌به‌‌یارانش‌اجازه‌داده بازیکنان انگلیس دراردوی تیم‌ملی‌میتونن با پارتنراشون رابطه داشته‌باشند جود‌بلینگهام یه تنه این‌تیم رو به مراحل بعدی جام برده. انگلیس دیشب با دبل بلینگهام برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25494" target="_blank">📅 09:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25493">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1QL_FuRAJ4JJVxXDuXDa_38fVwyb5sjjF90gsW40jr5kRl_q0FZZc45ARMLnSsE1V8nR9vGCSQg65LD2I0a5c6d7O9JbXl6KfudJ0P6EMCkTL-zrkiuEk-o7rbI-J2UAztKx8l-ALISG2cm9HAwC0iV6LkfV9ar7isgwniNhM9hw_OvxkGFb7nfZQLB6fFlTmXG2qxbDn1J1SlwZ43rixm7Ytn0vRcHb-EhTjkWnz7xoIQkyLFTH8r3SfMsEYzQJ53aKQOoq3NlSIoM8mzxBJT4Gxg_yB1q47qel8R_KPeuALjPLFR8gpRASQb3qNAuUTcgzjF8Idr76j5EyN5UkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی‌رسانه‌پرشیانا
؛ فرزین معامله گری مدافع چپ پرسپولیس بعد از تمدید قراردادش باسرخپوشان راهی سربازی شد و در فصل آینده در یکی از دو تیم فجر یا ملوان بازی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25493" target="_blank">📅 09:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25492">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0c6aec402.mp4?token=A974L18IlexK3dr4m37tivD5C1EHzLhQdH-gsrDFdZWghGF7ygHF7GS_NsS9CqFoc46cd390FHZqahivJFqeJn_v-FW-7XxKBPFr5kcwH4VK3uj0-FOOS85MJPSE0nBI_Es1g1I5bVvkWVbx6BqSUWjGqfpFs3ftu07UrCYiMrERzCcFjYGvb7V-lumlH0cl3kcHNu43tsx6UelNQvX68UDfhWwwslIPSQ0TjLSMeq5pbcSG7bLdMXJIGAh8ZOhvu58SkTFY6D4_4Ha3yU01SAMY9QyW2HJljkEQ8ISBC64X5idcEzAPR842-l6ZvGqQu8du1__YhJqbo4vkzsKa1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0c6aec402.mp4?token=A974L18IlexK3dr4m37tivD5C1EHzLhQdH-gsrDFdZWghGF7ygHF7GS_NsS9CqFoc46cd390FHZqahivJFqeJn_v-FW-7XxKBPFr5kcwH4VK3uj0-FOOS85MJPSE0nBI_Es1g1I5bVvkWVbx6BqSUWjGqfpFs3ftu07UrCYiMrERzCcFjYGvb7V-lumlH0cl3kcHNu43tsx6UelNQvX68UDfhWwwslIPSQ0TjLSMeq5pbcSG7bLdMXJIGAh8ZOhvu58SkTFY6D4_4Ha3yU01SAMY9QyW2HJljkEQ8ISBC64X5idcEzAPR842-l6ZvGqQu8du1__YhJqbo4vkzsKa1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25492" target="_blank">📅 07:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25490">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CiPkgfGO1uRhRUCV--pWGhsQeYFL3tPdAd_VfQOudn0tVL7SLP-NoXEL3Ol-6hA51xyoCycsb0KS0gfQWB2Txi1tmT239YUsE8KDFsMgVOTD3GurUM2uqWD4q0I5ovfEhbQ2IUD3e_mDU9vuIFTWi-Gy_MKv7kcJcwY2cDweq26gRZVWQHxqVy5g4t0NJBDlaw7rIjbpLfJVxTDyF06ydqhAheyi1lj6LdWP8EeH4BzamDVf_Re-Y8_bdd5nS1DGYdaiiKU93fU6iW3Nih3IfpscPNi1ZlL9SQpwd7gI_fRE4tOMHV7108E_gsIbSbQStMVcdbsxMro5_g3lK1-Rfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nTOiCfPLNuh4kkRGZM0Cv0D1pkrnJlzI23BFxcLst-bEJ8LwyOXqh3xpSn4rRCZg9lmcoADsRcEZ8a8nZeY5445piSECUrZOu5PIcT4FDVzQT1km6MzEZ0pInvyM8pUlCwtJODQX8GtEnR_MBof0SmvL2fqLq-5kG-CQPQ3pVM4rly8LJ7fPDA1eJZReA1UhlcxuU46tK_yp8VJi5EXvSh3s_H89TozeEkgXS9Unjtri9VbSt0wVIIC9e6pOxAkiswtyqodcCEtfeqvwrBRvdXv12TB8oD8gSHLDByzR6YpJEDmXHgmmN7iL3mZn8eZR5k_sXOZM4g1RWVQjSvcY4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25490" target="_blank">📅 07:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25489">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d869WS9aTFlbaR4ksLbZm-t_Y_OvQ6jCj4r6yQt54aHauWCoqv6X-2XV_0jl60n3Nppr7SXTY5BW6jrmSw5LkkKOUi4VxmBBScbOe26yX29WySrXl83gsStHV_3HFSFTmxivKsMsFGZdhyY0dOPGcE_wKtJ2f4zk-39Iet97GHhwLeLyWWdn1tGWNpxU9pPh_iTc1Xih_xOo3hJrJKVGWhyFUpQVHHA_31aYlvE6Qc0E6TS59NfqM5XpNDEXLIGo01HUFYNbqxB86l3aK6HWdl4iU5ZGmuqsRx3n9KstGWGqMWpbBLCQo2OwwEBbenagytNEOlK0FrKw3DTaI4AaMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25489" target="_blank">📅 07:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25488">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJNuyYbBTyDUkXnMoe1Ok9yiidEyTGN2-LU9eITYGZc6g767eJ7brSS3ze2nL_zsRXpK-A-ZVItMQTA4GpowYTTXClTmYI20AVH2a1Cp3UZvsTKggDY_Vv0Y4CQmiSvn2dpQZGiiLufW9OKZFrYZ5j3vnd6yGn9T2kwEQrkDQ6Df8ceXNESee6ib6Al3fwr5BC7LJkO6x0x8hFM_7Zgv47ldnusrn8QTzj-EtQy52ZYohpSQ1cft9XmUD2dLFxNa1uBKLiuJIWjG6jdJe7akgl7D0m2XQWPQZYXmdQ6jlvGk-GNYoKYMss7J3P9HxtXdLMf0YrdG7nZvlqIBhEJAPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوست‌دختر بلینگهام: امیدوارم‌امشب انگلیس با گلزنی جودبلینگهام نروژ روشکست دهد و راهی نیمه نهایی شود. بلینگهام رو بیشتر از خودم دوست دارم. هرزمان رابطه بخواهد با کمال میل همراهی میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/25488" target="_blank">📅 06:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25487">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvoNiMmAnWdyVBl8g2kom76deO_OozhyVuBxlTkg4DSVM9nCVj1t6iy3V7FFTkweq5Abh3hVHqiyERLl0UsNexU3nvH6_5It00Wm01OQsIzc8R_uSScuQ0jjsWH4ykxX_v31TH3RBpjDUaNL4SVBAtICBNFQGX3bRoZTD-ZfjKolOUet2SeeqmeFH1bh_ZvPjU7ffX4-WysLidY-oPqshfZadz9coGI_4D_yHmTa8E4_0QKg_rXsxqoDfoMo4dVmW8x1ZqKZMflZqAZ3U82xwLTHutqlcI2nplG6qh74yL9ieQMvkI6MiVM05nF8bpV32tqZFoLGvNPcwzEORofcuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوست‌دختر بلینگهام: امیدوارم‌امشب انگلیس با گلزنی جودبلینگهام نروژ روشکست دهد و راهی نیمه نهایی شود. بلینگهام رو بیشتر از خودم دوست دارم. هرزمان رابطه بخواهد با کمال میل همراهی میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25487" target="_blank">📅 06:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25486">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0TwCC0WcsjFrNShW87KQqVYLkY5765n11j89b2vIvhjFw7CVUJ_iOQtrwCnbs7WKIMsggHRgljKSOLtkvOt6RYQ46asZSlnN7tzFMwQqGQIMjE0tFsgbYMUwtx7-DKx-CgLEZ2HF92Rfo14skKVff00J9rC-CFOZXuxYV_vYpW4eeNRzxYscOLALujHwWyMDO0xEsI0k-J3o0Q5Oa0yuuxtQe4w9jwl4nQlkiOn1xEFX8Dto1jwH97eYVlMtumlE0VRJa6vxnl5lnt9V2q6h10dXrjUV_fD3sV9vbhD1pF5mUcN9lMx44pD4WeJ0B3XOGPCQSdGPOdkU7kFLR7t_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داش‌چیشد که به این روز افتادی؟
چیبگم اون شب جای‌درس‌خوندن‌نشستم‌بازی آرژانتین-سوییس دیدم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25486" target="_blank">📅 01:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25485">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67aef1f61d.mp4?token=iSioEy5-qJ2BO1BGDoUQSb18wEasPT8qpein8wnJLQegR98RWs23R6xb9QwrrdNtKsd7xlqxKCg7Mc60YuQ3mSwVK2v4r9D_P6xg0wk7nGRV4_2pDS6hqKpZApLNsDFXX5etSl8rS9XIqOPOqCuRh-k2ruhp8PqV9TjhmDFq6cz6a5qiCZAEdn02UHzDvOLmm0XntViXqQ1k23BElx9Co2h0b9JG2gNW-JjvhlFN-mS6Uda13vJlp5mUSmiYerfbw5-02RYIMTmPPT0HuCLxCZEO23Nd5SV5yQsLP2_v5RjBdU7bPEg39tdU1F6wGL3N-nRMGt9BtdovDtfqok-ryg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67aef1f61d.mp4?token=iSioEy5-qJ2BO1BGDoUQSb18wEasPT8qpein8wnJLQegR98RWs23R6xb9QwrrdNtKsd7xlqxKCg7Mc60YuQ3mSwVK2v4r9D_P6xg0wk7nGRV4_2pDS6hqKpZApLNsDFXX5etSl8rS9XIqOPOqCuRh-k2ruhp8PqV9TjhmDFq6cz6a5qiCZAEdn02UHzDvOLmm0XntViXqQ1k23BElx9Co2h0b9JG2gNW-JjvhlFN-mS6Uda13vJlp5mUSmiYerfbw5-02RYIMTmPPT0HuCLxCZEO23Nd5SV5yQsLP2_v5RjBdU7bPEg39tdU1F6wGL3N-nRMGt9BtdovDtfqok-ryg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
واکنش‌جالب ابوطالب‌حسینی از رابطه سرد بازیکنان تیم ملی پرتغال با کریس رونالدو در پایان دیدار مقابل اسپانیا و حذف از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/25485" target="_blank">📅 00:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25484">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wgfft4FFcO75suG8LxDXdVotnhvqA-wkXsopD4qH5cO2aDSkOVaFlboS092OLFP3fXqRWX2ygRS2eTLcJeVc_paKywgREGobhwyIyB1wiHqzKRGnm-QteVn1Puv_mLE9DICWv6DmVW-jhQWQOS3At6ZjmIj12Glst1d9qKf_XVRnDlpraJmErJHUdiLW9MsbUtiL1TdG1PmQ3tra0bCagDTz7LsRLVHlLIy_095Lt4en5aqIm2pSQLeW3brPjwjnBLmB9_WIwBRAHfXN3QNuGhcjZLv89YyM3IKXF4KQ_AfestFAsOXgKp_3VoU3XYegCShWJLGinPOSgZGts0kCrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه سان: درفاصله چند ساعت تا شروع دیدار انگلیس برابر نروژ دریک‌چهارم‌نهایی‌جام جهانی، جود بلینگهام دوس دخترش رو به اردوی تیم ملی آورده و باهاش رابطه برقرار کرده تا سرحال وارد زمین شود. توخل قبلا این اجازه رو به‌تمام‌شاگردانش داده بود و گفته بود نباید به…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/25484" target="_blank">📅 00:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25483">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OP6mQAYFnrG20xmoWiad4H84BJmXPg9BsxayDcZrTtZTveJ0lLEnUTCmn-pG5KSsqWf9yKmzTzW3xxyvXhrxzBOBoaMlEje-HelO1ZPtmXTTwCXxsIbfTNeWnj2VJ_k-hTPMHGcx8NlXosM0TwoRghXyMyf9-1UUPGeDoRyX5C0oleyZcJSDLYkNG_Cj8ZYSCFZarzTcC_iIK_QfoA06uy6cUwTVqT8BXcW0lla4oO7sTWq-ej235Z613-tJwS8FQdMsRkW-4BiRxBru33i4Gc5vlfkFD_PYRXUuPfYBmYxWLNyRP_l-K2zfMJNR6l3BgZ2GdtOvxWxKg_3YN1ezgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
دوست دختر کریم آدیمی هستن که به شدت طرفدار باشگاه بارساست و روی انتخاب آدیمی تاثیر گذاشته‌. ستاره‌جوان‌دورتموندی‌ها ساعاتی‌قبل با عقد قرار دادی پنج ساله رسما راهی باشگاه بارسلونا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25483" target="_blank">📅 00:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25482">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sA0wBxoopWOG4cxX3bvOgxnEOSJ8Jp4ORwW02HpzdeEqcIj4X5-Yh4eV5NzOpH4rzMwJ52OQRnOlSEx37_dKMvyChr_za5Oxv0o8WrxBEp2FnAhgdA1PGgwaNsxya7OKZp2lHrrcYDJRVUoglx07qN1TqBCp6rChs_yw8gv2dcnn3vQGFN50ByNnhnb6b-kc69vRcNS1iJqIaKbgqj0brCrAOhEtlVWcn3PzOKsL7d6nMC-5PGtZ55AokqbV4bToON0EefiRy_fZFEnJJatX2RqobxmyqVPuzLB4r5ys9pzSdDBvbiDuiylyo36gVdlUBhhNlKjlnY78CkRHN_-aig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25482" target="_blank">📅 00:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25481">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEKthfdvrfV2oF6hWJKo2uU7-FCqCbcKcEpodujEesAL8jiP0ugxsdwVc08H5DoI_BxQrB9RXlnbABBOhg7d-AoOHEEQx2MPrqxC2JyyMAz69qd7IqckGjT2H0P93XY55F-tkwMz-SaB87z3DMuulUb-Q8GUpnXmYeCQWaWubTASn-hE9dZF-EUJBkywvk0wx4__kzZNL4wDjxwg9xBPyAvfzk3sIhjPOZeC5SKXe5VI-v3j-m3avby288asvZ0sG7qOTKyR2thxvhmbWNyZDTUydbkxp_Ygudsm1NWvy6wPz-gCzGjs9YWYBnk-l6mgnsPw5XiB31m96yGRKn3aXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ آنتونیو آدان،عارف‌غلامی،آرمین‌سهرابیان، محمد رضا آزادی چهار بازیکنی هستندکه سهراب بختیاری‌زاده به مدیریت باشگاه استقلال اعلام‌کرده درصورتیکه حتی پنجره نقل و انتقالاتی آبی‌ها باز نشود باز هم نیازی به حضور این‌ها ندارد.…</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/25481" target="_blank">📅 23:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25479">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c84l2xvK7i6oC1frxzNCdKRM8RE_ndVgkYEvFzpxrfzZNXwO-NiUv1WaWsmdXwtQ5mIIwi4p8YVr3PSx-gGsKfMlPe61BWFLWhK1RtplvDJCtMw10W4V5614gL9N_utDraUdXeEnJvbA2YWjMlvstDLiTCDnzxDj6uE75wLnVU7407f2rAG6wToA7Olvk--Wh43Q4s5qNbmLKrVJXpvGqAee8QAbA3CFlRU5QWuGbg1YFrCY2iV2zpDYg6athLBKyo0DNqqvGJwgaczEklfMWTmSxotVNIK4F6TvZX14EDfaQ7cHAgJYlb5Jn1ZZOMQ_dgZSrVEuMnBCntUGywldag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BBPMhRrJX8S1Zd4o9keHqKL8optmJWjsO_WRwGmEmTIUfAYKGsFQ-mi2kYZ6Vumj6bAC1tYx9HLS-B1up_2V2bQNNiM07nyUtDGx6yGMSsDQ5k07Uson1tb0pD4ciJwr62MnwJVd59jc8RcM76VpUtotFBE2EQ6V6SSXc1-HbHxyiIZ9d0ZyLsJZol8tVXPLD7qwFPKLbkgm7yQFlanK-29062VgZvGr_uR3-mg3A0TNkfHAkRN8gHDJb4RYl49Wr4QcDyJxlDc3m5jVfG8FI_TupAcNCej822JMLHi-U7RtCglN6FScX5tD2O4IzTbnJLWW541arCBIZmx846DH2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
نشریه سان: درفاصله چند ساعت تا شروع دیدار انگلیس برابر نروژ دریک‌چهارم‌نهایی‌جام جهانی، جود بلینگهام دوس دخترش رو به اردوی تیم ملی آورده و باهاش رابطه برقرار کرده تا سرحال وارد زمین شود. توخل قبلا این اجازه رو به‌تمام‌شاگردانش داده بود و گفته بود نباید به…</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25479" target="_blank">📅 23:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25478">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXL8VFufEWr7BvyoF4EKePmEOF_oHCt1dQkNrZ0-OevncVUaW5Kc5ez3sU4fIKOPCdDWzGsN5k2xPMjOP9GX9a9YxIZnm3FgxuSzxTtnZmhjnEcLO-MQfF0NfqMKhtTz9s5KQogwIi63decGK63aMBMlgIsOxm1err_-PKlpLHcjrdEW10KA3ROR6mu780GgOt6lFcx-uB_M-ZU-DSu4XGDnkpVyoCE74NXNyEQqU-AZpqXzXYZvCJSN172Xm3sy2Dx5UfLbsLBBU0pm-l4zkBc1mg3odl_Qs34oug-6MOHSLk0tJdilSKWehnPHxsp8BCCWLlPSTcURPmGMjvBdkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
طبق اخبار دریافتی رسانه پرشیانا؛ میلاد سرلک در حال مذاکره با باشگاه فولاد خوزستان تا درصورت توافق مالی بین طرفین به این تیم اهوازی بپیوندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25478" target="_blank">📅 23:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25477">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ng0vqKK0uNqwtqk1e50InvF8cXFIIj7PcOuhdbtaZ2lkdo_bw4wNRoLmn9ZjLyxr5bYgviUTJAKg6_wUpZroTNMcwnGeuiR4mvWN3B4zSIBk1NTaxps7gW-Od9jgVAvr9e4l4ZS4aJ8d0DIUx3Ruw7XE1PAoW4WrfT0l9nB3Si0B1PTkARbs18jSjmkGxCfmlKeFXioBC5NBWWZwN2_qKtEJSMC41FhNNsuJSxypMaphFXF8GvkBISFuVyW7EiUG9DaT8cnGqLqSL_l0FYGjNT_YuQ0PafDOu90X4Q888G-RaCVgt-O9TguozdIjDBWPifxVfAa-WpIj3tZQuWgyhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
وحید امیری کاپیتان‌سابق‌تیم پرسپولیس به‌مدیریت.این‌باشگاه اعلام کرده‌که درصورت تاییدیه کادر فنی سرخ پوشان علاقمند است که یک فصل در پرسپولیس بازی کند و در پایان فصل از دنیای فوتبال خداحافظی کند و به کادر فنی سرخ ها اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25477" target="_blank">📅 22:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25476">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3degFqV5_0sTSLquzu2PlbtCUPyo9JILEaHNgEqpUEJKJlSc_MB9dx-f4_5gAQIIbjYXToZUE6dA6F6P8AGwA25R0WlucTC4NlXgPp4a40w1q6TcJRPby3ZZyFcJJt8UCTHalmBqR288raflqIkC7sr4IRTTX0wfx9RB-rwcfO2-MF1gYnKnbRMpabEQMLvMxgqzZSDR6k2rCEGkjzrrZ-j8DlOELIubu6WC20HHhFaFFHzgmZwF5j-MA_rIIJA9SWruvKjKtJCsbKanYYv8oFeoSfIK4GD1PUe7QW33p78F5dgJRixMxIWy61SNqLq8Ol514_R_uzy2n0ttSK-kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تکمیلی؛ روبرتو مانچینی برای‌عقدقرارداد چهار ساله با تیم ملی ایتالیا با فدراسیون فوتبال این کشور به‌توافق نهایی رسید و انتظار میره به زودی پوستر رونمایی از او نیز منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25476" target="_blank">📅 22:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25475">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d020345f8.mp4?token=rxIim2GuQaoUJF_llwVG7eCI1vx15l757NAbJwtQWbQHnM4fKbVqb9-6hNomOsyJ_XXUSqLJwrZ5P7i0gwJLZ91KoXnJaDmfzHKtdY8Wy1b8kTuoAtHfNB1x7kQK9TFUbKSRDjGYeYJIRsF4iWF7REiVcFbNb9mgaGbJ9dFJgrATSR5fT8rHB1J38dgx8odaYNDDZTK8288-p9CieYybiubo5DVczFQZLQwu2geVzAEnLU6xHy8s7IxhuMEO81lzomPkohPNll2UUTQ7bBZ88_nIuEzvdR9Q24iac3lRAUguxMCiBdpT0Wl0sKuGuTNIS-B6voswvIZAsaRquAY7gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d020345f8.mp4?token=rxIim2GuQaoUJF_llwVG7eCI1vx15l757NAbJwtQWbQHnM4fKbVqb9-6hNomOsyJ_XXUSqLJwrZ5P7i0gwJLZ91KoXnJaDmfzHKtdY8Wy1b8kTuoAtHfNB1x7kQK9TFUbKSRDjGYeYJIRsF4iWF7REiVcFbNb9mgaGbJ9dFJgrATSR5fT8rHB1J38dgx8odaYNDDZTK8288-p9CieYybiubo5DVczFQZLQwu2geVzAEnLU6xHy8s7IxhuMEO81lzomPkohPNll2UUTQ7bBZ88_nIuEzvdR9Q24iac3lRAUguxMCiBdpT0Wl0sKuGuTNIS-B6voswvIZAsaRquAY7gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
روزی‌فهمیدم مسی هیچوقت‌تسلیم نمیشه که بعد دعوت به این برنامه‌ازمجریای حشریش جون سالم به در برد. لعنتی‌ها ببینید چه گیری بهش داده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25475" target="_blank">📅 22:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25474">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sLjhKZYhiHdBobFc4lMICHPm_GoHZJDwLtKRnu8IWTSY_xJylXbYV5trQU_-HdGQKIaOHM79_fUMeeB9BSj88BgJcV9sixrogBx7oToUoGv2Z7m2inYd-BF0vUGg3S_Fe10f9tyJitY6Ngy-YUk9PBJEB2NJcBZmXFCJZKtWV0NBpmvA3YowqqEkTAx7yq2s5Iy0Azy1HIpyHXX4eOFkKHXZHM4SOuR8QHGsQV8_SBJpBvaT_Fkex6XvVeqmcpZbtTOFX7Oy19u6TOdq7Atuti1h2zsIN5qnKfJI0CyDE9GR6lZokw97gG1dsbDS4Kn-HCfnNpV4h8-fiGIel0jRBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی پرشیانا توسط پیمان حدادی مدیر عامل سرخ‌ها درباره وضعیت علیپور و محمدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25474" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25473">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec99dbc8ec.mp4?token=qBs3HTzVuocFrS_XxnjNLnsCwx976zDnvUhIlmjqxMYZw1xmxL4X0XB7BBEImWpwi9JbyW6B7ExRHmCcvgVBDmf7Fu76Oe4FUscggmD8Cn8bRog_uSqVE-ogDq3BCOGRRdPhePEiByqTUvFaCec3xlXTXAMhbXEsmAkOwuCee2l1KRmMY94WSGO5Yl_2uqpv11Yf6lZDLlehLOPB97DMIakBRwOdjFtoNTIHWLR7KrEWmNc120kDp8EkbBAOV3vsOYMtUTZM9z1RYH7cRI9OJNnLru-v-13Fiz4OITptM3ZghtbVrq6z5q9QiY4DoR5Z65BnSXzgR_eUyNd66kWq5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec99dbc8ec.mp4?token=qBs3HTzVuocFrS_XxnjNLnsCwx976zDnvUhIlmjqxMYZw1xmxL4X0XB7BBEImWpwi9JbyW6B7ExRHmCcvgVBDmf7Fu76Oe4FUscggmD8Cn8bRog_uSqVE-ogDq3BCOGRRdPhePEiByqTUvFaCec3xlXTXAMhbXEsmAkOwuCee2l1KRmMY94WSGO5Yl_2uqpv11Yf6lZDLlehLOPB97DMIakBRwOdjFtoNTIHWLR7KrEWmNc120kDp8EkbBAOV3vsOYMtUTZM9z1RYH7cRI9OJNnLru-v-13Fiz4OITptM3ZghtbVrq6z5q9QiY4DoR5Z65BnSXzgR_eUyNd66kWq5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
صحبت‌های‌ندیم‌امیری‌بازیکن‌افغانستانی تیم ملی آلمان در رقابت های جام جهانی 2026؛ این بازیکن از دو تیم آرسنال و چلسی آفر دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25473" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25472">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOLeV5bogCx0mD7v4DLj-rz5IL8WiCTHYbOMpYNyJfzt3mkrkm4pQQymmeW2vZ2z-SvMsJBiDBGoD8l8GtesEMoYNekUMuDurYUN-vOgL52udyyZ1xbzY2L8h7f8Bv-Q2kYViuFfIhSUXIjSibdYUY8IX37Mqqgi7q3JHGmT1tRFpdC-dVISWBhHwcOVwH1V9Z9WrQizx6NlcKX4Y4yuEJNz7tAgM1LfCeKCxRZMYe1-gXTX7_uShHApyAZdp4_IW2AyXkDtOLtEMyQ911UPk1U3rfiOo5aQhfS1PZPtS-JyiSvmntPO--QkEtXAWyK5x0QBiZcqsnk8GPnPitLMhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
قدرت پیش‌بینی‌ات رو ثابت کن!
⚽
🔥
دو مسابقه جذاب:
🇦🇷
آرژانتین
🆚
سوئیس
🇨🇭
🇳🇴
نروژ
🆚
انگلستان
🏴
🎁
500 دلار فری‌بت
بین تمام کاربرانی که نتایج را به‌درستی پیش‌بینی کنند،
مطابق قوانین سایت
تقسیم می‌شود.
🤖
پیش‌بینی خودت رو از طریق ربات تلگرام ثبت کن:
👉
https://t.me/betegram_bot?start=p6_r4EF37DCE
⏳
فقط تا قبل از شروع مسابقات فرصت داری!
موفق باشی!
🍀
⚽</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/25472" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25471">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-TSva6rzemFcNgbL5PDdHXKlC2feRbjd0rQdpTwbsB8wrRFi23zhq-tS5C0sQM_OEOo0Hx7h2cW4Gbqbvl6aNZw9TOJMCLym7OWi4pkkzeoXYZnSm72Uj1hxkZ6ow40kgyj8fA-EW9_XraNfoYgNj-Iq2bTtCS7b_th9m8s8TtAKc1vkQilAbjhxEGys_iP7HutJHImmcXzhoBP1XR8kHe19dU4GX9DQcVp5kDyZbB-mahfDazUFVM82R574xhMO0oDJuUd4bc0lZ321JaNW-0zyoK9Z2t0ng1yE3bbybpELIjXjY1FJS8xE8yWQdogJczvXCLBHInrRSZemGV-bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
#تکمیلی؛ اگه جدول رده بندی رقابت های لیگ آزادگان همینجوری‌پیش بره؛ نساجی و مس شهر بابک مستقیم راهی لیگ‌برتر خواهند شد و تیم صنعت نفت در یک دیدار پلی‌آف به مصاف مس رفسنجانه میره و برنده اون مسابقه نیز به لیگ برتر راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25471" target="_blank">📅 22:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25470">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IABLUzJOU-jUWurBy1C9118ufmKVQJvLWbXR0C8MeraHtYHG6TJS3o_5ezFe_Uqf1m-LmDtoGlWTAKiSHZmbRs4rXM_NlU5xQrapFKS07a7ptq-xhih2nVIX5GyjsfWbKIFHrhLBvat6ScZt1pDrgcFLk29uwa7NgrnMaZQY7kGhI3LkQU4ERG_WXDJ8nKI0a9IvNypv10xLNv_1J14Hix-7pxeJLEuaJhSNksXxLh02AvO7pu8ph2MQK0_W3U6SvRAe7FoCR3UbFF8c_W9fZM6ykllOZOU6AH0k3O-xGpK44fTkSKCWAcgyAWzw0SzCzKT8ksAIcJ8gOdOsqGmijA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جالبه بدونید بازی‌هایی که تو این جام به ضربات پنالتی کشیده شدن در نهایت تیمی که پنالتی دوم رو زده برده که این‌فکت هم درنوع خودش جالبه واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25470" target="_blank">📅 21:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25468">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fe85cec8f.mp4?token=dk7vYGB8hfFpp0vXB_a76VBwNcZiWSMYCYXZsGoggSQ3s5CXewBtLnRyHuED6lp2kAd1PJOEFB71sYrgHRld_mBpcz9cKtXjmGvAphZlyUSygJyfm9wTm-X9bmmzPde9iB3LS9ufJvOzETONuiQffMpsmMs6_DxB_MTP5aWgVUiS8fBzxNdnkBnwBYOJn36D5jMDbs_U57cOuHXtY84bY-JFkcHFucyBWoBmIT7i4er8G0ZfxRl613Wgs5WAGBI7CyEzixHqntRCfzaZoSs7I-VU5EBq0LQwUM0aWO_0coLFGSHe1zhTiq7RxebsNqx60F0sLNAk-umr4PCcEjkxSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fe85cec8f.mp4?token=dk7vYGB8hfFpp0vXB_a76VBwNcZiWSMYCYXZsGoggSQ3s5CXewBtLnRyHuED6lp2kAd1PJOEFB71sYrgHRld_mBpcz9cKtXjmGvAphZlyUSygJyfm9wTm-X9bmmzPde9iB3LS9ufJvOzETONuiQffMpsmMs6_DxB_MTP5aWgVUiS8fBzxNdnkBnwBYOJn36D5jMDbs_U57cOuHXtY84bY-JFkcHFucyBWoBmIT7i4er8G0ZfxRl613Wgs5WAGBI7CyEzixHqntRCfzaZoSs7I-VU5EBq0LQwUM0aWO_0coLFGSHe1zhTiq7RxebsNqx60F0sLNAk-umr4PCcEjkxSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه‌پرسپولیس که دوهفته پیش با ایجنت علی علیپور به توافق شفاهی رسیده بود حالا 72 ساعت به‌این‌مهاجم 30 ساله فرصت‌داده که برای تمدید قراردادش به ساختمان‌باشگاه برود در غیر این صورت قید او رو خواهند زد. درباره میلاد محمدی او تمام توافقات لازم رو…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25468" target="_blank">📅 21:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25467">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAil2GWqAlhVz_CzDOwg2A3sV4bJuaVIO1O5ek2dmHyhIigarRIXEgXf17nonXJZFgUsjZRmhVrsmRui3lY7lbS-sJdVPS7av18CQmmSM-rMqAVInSWLSTNm5t3klpdPPqJY_n6AeK-GB4AIb-GfeGeIUyg3OMze9DzLOxp0H-64xwzQpiKMdv8HkvCfCq-FBls8rPO78EgWdbFZ-ThEJgdhq0AoyB_LANv6OXP6eGM7JlhKSAokID2lgLYGCzQHjIG0oeqY_BSfm3XmqMAcCFl6rB7fD3z85oS7N4cQCYmqqXkuQxxR8pbqBCSjiYI4HtNVVJNRUHB6TO4366zIQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌_پرشیانا #فوری؛ برخلاف اخبارمنتشره‌رسانه‌ها؛ طبق‌پیگیری‌های رسانه پرشیانا از مدیربرنامه‌های یاسر آسانی؛ ستاره آلبانیایی آبی‌ها مشکلی برای ادامه حضور در این تیم نداره و فصل اینده با شماره 7 استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25467" target="_blank">📅 21:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25466">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NONe1ov6qhWDj2jqTsvAYidJJ6niqiaatAyQXhKQHy8YO7xVSGQ8HSK0ZLCFGXpGAQij9T0Qp1KkIKd5qCOTYC2J6MaaVBT3tEQQxv-onlzWJfnbfFbjhD7KbqY58Q-j_PDOToKd644ONL3558vUWqctDIkqpz0rllb8xJjsTHZ9UeGx08ePLHdjaWlJG8h7JBssKeXjblQeMvXx5yC5AYUgoG6Bb52raO3Hrtx5poA_rVScEs2cQyMK6TzJyhXf4EgoG7H2VeG4jYb7n60EcqE5bembobNbnGFgDEMYWC5OcZtveWYob6J4nyq7PyD5_Cjg0dvqdZSyQMZ3Q8UC9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
طبق پیگیری‌های پرشیانا از ایجنت منیر الحدادی؛ خبری‌که رسانه‌های‌آفریقایی مبنی بر توافق اوبا یک‌تیم‌مراکشی منتشر کردند کذب محض است. این بازیکن اواسط هفته آینده به تهران برمیگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25466" target="_blank">📅 21:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25465">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRkwcJ5REB0WG0s3f6K1f_elhfPCucGzhTV1jA20BFOhg47yuhSEGA5uW-mpsZFfqoJikFd9hvpDCyoMZYrOggz05GuXtrFtBPS67t1Rw9KYOxLohr-tm9TA5QXwh4nx9TwJacCqNQDdtHBbW9yLxitJOYd_0F_ie_3f-d719B0lWVAU7ubkZ_1gt9Z0knKSQ2FNtq4kuD3lN5MRmfyL0jtE-bNptFyjEgnxlCvEmfknKOebb-gx_Cr2zCwRdo9vruXxG4auORChoYKaiFemVIl7N05bxmXkQbuXn3PBq_LGWd2xxTMswSrrFbIwIM3_xFJCg25S_ajc-iM4CltLFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توماس توخل سرمربی تیم ملی انگلیس روش جالبی‌برای‌انگیزه‌دادن‌به‌بازیکنان تیمش در جام جهانی کشف‌کرده که چون یخورده 18+ عه تو کانال دوم‌راجبش‌گفتیم. حالا فهمیدم بلینگهام چرا یهو اوج گرفت. بعدجالبه بدونید 10 گل از 11 گل انگلیس در بازیای اخیر توسط هری…</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/25465" target="_blank">📅 20:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25464">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHULA5yz0YQ7mR7RmaavkAJEIQt59VUQy7nfB6F3KfrOGqFFzcpkDuvcTsJsmD-W-DmcUGHHl-9X61ax2wNxCjd4uL7JOzqfjdUL6fA2ptJDUE5zftdHwQVUtSSjLRfFSZcdwl3cTbw2d61pu0VTNhD-cLzs4b0gGk8OB3-0j0S60h5zTQRoDalHKYM6pKSW7FRtf0FT2JhOf33eax5hf8_kdwEmdUi84pd3UXxWto0csVSSQFWH3k7KzZfYlHtqUQXg2eiaUtinAryiSkPWfINHaees0cPCxKzozj_sBL0p6qQMbeUxZGX41m3IhRer8BrDctcMixp_sgtK0G87XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعداز موافقت مهدی‌تارتار سرمربی جدبد تیم پرسپولیس؛کریم‌باقری بزودی‌به کادرفنی سرخپوشان اضافه خواهد شد و قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25464" target="_blank">📅 20:32 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
