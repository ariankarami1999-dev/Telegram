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
<img src="https://cdn4.telesco.pe/file/seWo4KNzTNqOLr2RlujRDogO1mhYdUARB6CO1L05YV-_8mUW25AL4HV-r3NIYCujKXJLMihCaSWzhFOT544PywaIffKK2yV_LeBazTX29bClhVFTD5nJPUDx-Ly3Ei_FNy8Y20r6hd0cNHlQBnK_lfJp5iN3Zk7zpoq-pVV555DlrARwVqZcQZOQYM5yW0ud86DDSlfzbLvKfV8L9oybQRQ-lvEE3IcMTS1UyCPsSsQPlGuM9BnRT-tRiVJiYOdRSjsZdJ9DIUm7CI-gJyIf37ZadT3vGVy8qNZfhKXL6rl9hC5JbmYDF57Yw10at5Usl590tAnJvCXk7TjlxTwIgA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 488K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaaa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-14 17:18:01</div>
<hr>

<div class="tg-post" id="msg-31095">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd044daffb.mp4?token=OQkRV0KKP7YYoae5ATaNxv8OthKcRW05vpS1qropZsiNuSTEaSjCKcsYpsWgusM5IQi5LBSNhMeq4o-Ob5O1wdal9YsFz58WX2ZC8mIi3D6UOSCojVLSOP8oGHm81VzO_3IDXsIef4P3_0G47skNhKZJhcGv8liPcpPI0XwClT3KAPk6ssh4UVldeT2SpfvM5PE-iDOMFiaCCJdgNNNhUPCiN5WCN8GdZfWZ50LBNnjYyRnAlmlllluzDrBvPqGhFpaS837IQKEgWO-YVeCZX5vgJM5KBiYiU4anot9rwwltdQSDjx-b_3JVxaihJ9kOkcW7CYrijeDJ8F9jXQxc-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd044daffb.mp4?token=OQkRV0KKP7YYoae5ATaNxv8OthKcRW05vpS1qropZsiNuSTEaSjCKcsYpsWgusM5IQi5LBSNhMeq4o-Ob5O1wdal9YsFz58WX2ZC8mIi3D6UOSCojVLSOP8oGHm81VzO_3IDXsIef4P3_0G47skNhKZJhcGv8liPcpPI0XwClT3KAPk6ssh4UVldeT2SpfvM5PE-iDOMFiaCCJdgNNNhUPCiN5WCN8GdZfWZ50LBNnjYyRnAlmlllluzDrBvPqGhFpaS837IQKEgWO-YVeCZX5vgJM5KBiYiU4anot9rwwltdQSDjx-b_3JVxaihJ9kOkcW7CYrijeDJ8F9jXQxc-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
لئو مسی از سال 2005 تا 2026؛ تیم ملی آرژانتین راس ساعت 02:30 بامداد فردا در دیداری دوستانه به مصاف‌تیم‌ملی بنین خواهد رفت. دیداری که آخرین‌بازی لیونل‌مسی باپیراهن تیم ملی آرژانتین خواهد بود و این فوق‌ستاره آرژانتینی در پایان بازی برای همیشه از دنیای مسابقات…</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/persiana_Soccer/31095" target="_blank">📅 17:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31094">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFis50W0d5jx9PuJ8jcNXodJWMLo4bBdw3AW1fMKJmncWUcJj2qYFfUFOmJuNzYubRitYrG6lTKU-RIYfnZCG9_BN5ow8fuVBE4YobOMhXgUs-61VPyV5Coo4teUp60n_Qc44HChsXklwKrXsxX17KfPsJPSAOfR26XCM1RPMJzuLD4bFB2V7jX-kVhjHXsrmeS3dfYvHSFjij8K9nSWYJq9MOOzLrursDHGGTvWgLnHQXE7Cg9PWyCcMWKAqCLZ7b0xmPqpUgTHeHrKcdEJnfKM-2FX6Yccn1OTdH1HpHLT-1K6a_s3M9rATBBeT8sUU7gh8xwNT0HM2rOhPTMlGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
ادعای نشریه فوت مرکاتو:
نیمار زمانیکه در الهلال بوده به سران این باشگاه گفته جزیره میخوام اونام درجابراش‌خریدن. درامدنیمار درالهلال به حدی بالا بوده که درامد سیزده روزش رو به خرید جزیره اختصاص داده‌. نیمار در تیم الهلال به ازای هر لمس توپ، حدود ۱.۱ میلیون یورو دریافت می‌کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/31094" target="_blank">📅 16:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31093">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e1a596a3d.mp4?token=jeDEva2SHwFP8IBSBnqT6Aqt0BAOhTygPhNzk76YCvc6QYxouTuBNY8mxKS9O-UfDorPt210L4jcYRHQo4avKGF3Cz5P8LX61fAiXz3VMoJkjr5bROvMzcJNNO8Y-ZiyELD5ViYG32l8GndmSCdeWxqIsBWi9734eiuguWWeLDmSIUWVejWrHfTPLLKaRnrR8mf-39Ndgz7ni_Qdt9jElhsS3MzDLLdin7ZEv6KuW3OcVgYwFiF2UjutG4k-_SMMejkceTvYrQ5jKmp1x24yviRQV3tyRbW0y6GE3pXPhsRCoefOahALLR60pSgL0-BIA6oIk74NhkK3TgTbmhbeQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e1a596a3d.mp4?token=jeDEva2SHwFP8IBSBnqT6Aqt0BAOhTygPhNzk76YCvc6QYxouTuBNY8mxKS9O-UfDorPt210L4jcYRHQo4avKGF3Cz5P8LX61fAiXz3VMoJkjr5bROvMzcJNNO8Y-ZiyELD5ViYG32l8GndmSCdeWxqIsBWi9734eiuguWWeLDmSIUWVejWrHfTPLLKaRnrR8mf-39Ndgz7ni_Qdt9jElhsS3MzDLLdin7ZEv6KuW3OcVgYwFiF2UjutG4k-_SMMejkceTvYrQ5jKmp1x24yviRQV3tyRbW0y6GE3pXPhsRCoefOahALLR60pSgL0-BIA6oIk74NhkK3TgTbmhbeQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیدواژه‌های تکراری امیر قلعه‌نویی در چهار سالی که سرمربی‌تیم‌ملی‌بود؛ همه‌ی همه مقصرند جز ژنرال!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/31093" target="_blank">📅 16:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31092">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5T4TzUEEola_lVmH86tyKwmoDNptKuH3P5rz-l54W1qUJ8LA9-Hiw2mwMopF-BkYQpk5bWC2xw4xaCYwRnzbZtiu5okkC_eD1QA6JVyr0qY57Tr6135YxwOrrGAHtYQapp0PwS5fsZUBfyRfDwdf5ggQ7ILXF_086jEdvMK14gird36fR1QTa43SZ3BtVHbt2h7dhDKV_VrPg-soih9hx16rvlVBLCFhaZpYPnBK37aKF9a_b8VFcwTlrDipIYgnHkzBhv_5ITYnU2N1R0dq_x0H36Z1oZ5xXmgRfUgSV80mw_PEhnX_f8dNmUmry3o40Q9KCvq7em4_TdIgpXRlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
تصاویری جدید از دوست دختر کیلیان‌ امباپه ستاره فرانسوی تیم رئال مادرید در فیلم جدیدش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/31092" target="_blank">📅 15:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31091">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOU7E7-kMpf3QpDlD1cMgDR_kt-73HbiwUF7F2nIegHSrRTa_Nq2PI_4M-htHzE_BmDHq1c1tYQhw6qf7xAjizC6G1LW6IlSBFL3V4Yt-inaCp7adVqIJz3sE06yPt7LMuTyK4kzTfpCFRL__rKaBayOirSEHomYlE5qF92g1K20Hte00JdRN1vvU4B1_Bv0JYKJTDVmIHuZtmB6v-47zHtIfsHSZbmXO8XHXfLt7w_iDkO-7aSZxqZn3mw7RGKhosfgX_7neuZN0zSHT6vhBgxVS_KogRMN7IpNdRdvVVH5gRCcsvdQwdXSe7z770lNCY066R1Mt81M5Q_mRWBQUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یاسر آسانی و نامزدش بعداز چهار سال از همدیگه جدا شدن! یاسر گفته بخاطر استقلال میخوام برگردم ایران که نامزدش‌همچون‌همسر منیر الحدادی مخالف برگشتش بوده و آسانی سر همین ازش جدا شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/31091" target="_blank">📅 15:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31090">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1967f5895.mp4?token=KcIigSEASDUmkbujR4EcCAPDWVEr2sDBrWW6N902taaJ9d-Ex4TUHRwl8FHG5HL9vnMioi7XywmndQoKG0SD3b3EvTyOkoKLLuo4Mjq6xc3nNjdt-YcFEL49H-QcRhDhM73eMHLFMHeujXzPkXGGeyUflbJUj-ThO1ExmtQJzIHx8lyeXMMxxE_ske0LA7UjhPp3LittCf9vkpgQp_Abb1tHngd8mypeFz6ATHDZ_BB-rlbSdmChxUqR9lYGYTgEi0QFYb0Rtj2ui5hCc5BgslbEfnvV86NlWhavPTwquKe8w4tnI7Y580B0h9Yf_dTpIgq9mGyzA7YEa7j5G6Qwrmq91ZMDX9wJdgi-234xp8RXdWhTTVawn_-dZkhUSUQc_LwLNhRtKU0QqX1vJCud-vWGeS_Fw-kXHP991nEiYalTCOQ3X-ydFBSyAO2lSbgR362h0GyiiceZhVytvHgjInISwibdj9FFVpn1t70DOTWcOQsMRrRp1B3tp4pD4ikLzvH5c7EwtlGgjqxzbwgSzWR_hYA08q5AXQQVAEDuSRB12J_4t8VxD0xF7GWKqlq-WvnkY6nbr2InZvBdIIbpHD_f45V4UuYpkX9PsUpesOjB8XvWIuMK6vzjXr2ZF9i15XsBlibNeFi_eDQaUzUrEA7nqAmJFrzxPI8zqQJ7vEo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1967f5895.mp4?token=KcIigSEASDUmkbujR4EcCAPDWVEr2sDBrWW6N902taaJ9d-Ex4TUHRwl8FHG5HL9vnMioi7XywmndQoKG0SD3b3EvTyOkoKLLuo4Mjq6xc3nNjdt-YcFEL49H-QcRhDhM73eMHLFMHeujXzPkXGGeyUflbJUj-ThO1ExmtQJzIHx8lyeXMMxxE_ske0LA7UjhPp3LittCf9vkpgQp_Abb1tHngd8mypeFz6ATHDZ_BB-rlbSdmChxUqR9lYGYTgEi0QFYb0Rtj2ui5hCc5BgslbEfnvV86NlWhavPTwquKe8w4tnI7Y580B0h9Yf_dTpIgq9mGyzA7YEa7j5G6Qwrmq91ZMDX9wJdgi-234xp8RXdWhTTVawn_-dZkhUSUQc_LwLNhRtKU0QqX1vJCud-vWGeS_Fw-kXHP991nEiYalTCOQ3X-ydFBSyAO2lSbgR362h0GyiiceZhVytvHgjInISwibdj9FFVpn1t70DOTWcOQsMRrRp1B3tp4pD4ikLzvH5c7EwtlGgjqxzbwgSzWR_hYA08q5AXQQVAEDuSRB12J_4t8VxD0xF7GWKqlq-WvnkY6nbr2InZvBdIIbpHD_f45V4UuYpkX9PsUpesOjB8XvWIuMK6vzjXr2ZF9i15XsBlibNeFi_eDQaUzUrEA7nqAmJFrzxPI8zqQJ7vEo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این هم از ویدیو کامل قسمت سوم برنامه فان و جذاب با ابوطالب حسینی؛ عالی بود از دست ندید.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/31090" target="_blank">📅 14:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31088">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hVUZ1-Gpv7nLd_gDan9vzNPHr361-8jDn39Y3viIWro3vxfrOQ7v7ODwBnGVHcnOLqM08kUDcTbhgoYgr9_ITuLVxEGr2psiRZoG5N6VrZnaRjhb3qSCRrZhwr1CGfNzbZg5hkGXlHSkJ-Nu2ksH9zF_SL2-Q5EZElSUrFz3G76r0B-sJADXHcm-kOBcriUEg6BRDeT2rTqR43lJ7XrbjUEL_7Ju6F8_uQyCZjnhOB27fx9q9ZFw02L6gZq8qDrtLaLL0_UhWEoj7US2JQD-DClmXGH0t-O1Njr9wro9c35uVgZrKd79KkCvwb1ERShStyyGgeAL-cYeazLUJRk4rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e80_whgCKO_0bOqS5H3fL3Hns_E7iy4S78TtHpdLlvPVpeGUhZBNobJ4CbyvhM2fkRkApLP18IHPcPFUyAr0RrV0CIgmQG5GZWJ-dOakOaMCBpYc7BPIzkRkKTWsMORmr52yHfXmaLUcD7yFMwBLbKUtxgCmRDAkqyX-3KVhFLWgucUYpD1TWOsSDgTKHieHs5Yd9RDOZIsztj0rBgk7ytFiL_MhqwnyJgWJyrSnCZ7YuHss61v8a9B4ckIzrkHUqMNbZxo3SEZvqkeiHsQ3agoxC47rMQlPuez6ven0-Vl8YgAOFo05-tN9RGx8U4Q1xy7huYIY6_GLcbZgwrjrBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
پنج فوق ستاره برتر قرن بیست و یکم از نگاه هوش مصنوعی در دو قاره اروپا و آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/31088" target="_blank">📅 14:24 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31087">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKjJk-f2-kcVmzPPZI-DWu9REkm6-Eo2mdjyy28VsKR9MIza6qbfwF2NtPQF8EdyIB6rHIHsSBSMX9yxcGNBlFt-DjyaLPvm1RiY5i0JQFYvG3orOxB7mFew2Qnx4zjfoJBFNaEEXuqPq9RascvruQv-zWrenC8AOZ-kPlcG8YCJFAaakKyBlOoKCiWmLJw-AKdyDWdR6ELs8-tytv4N1sTc5Rd328Brrd7cN5_wF49JLsRBoMtfxfi-2mZMqwsI85yMINeBCumQVaJF0Gu113EtkqonPuhWw2lH_YQNkx9QLjsS4eSLWU3P2HHpTkjZcX95h0wd66Y0OAfYCEr-wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛
مصدومیت حبیب فرعباسی دروازه‌بان تیم استقلال کامل برطرف شده و او هییچ مشکلی برای دیدار با تراکتور نخواهد داشت و با صلاحدید کادرفنی این تیم میتونه برای آبی‌پوشان‌پایتخت به میدان برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/31087" target="_blank">📅 14:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31085">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CnzJSaolw0xIJRX8Ux99qD-pdcty9lDUEVHDktV-mJe9agzAstCmffsCCxuqrWRWE4sbkVOpOFCgkXyqh91XhOPZeA5cfIunVTbr86RzP-JQzGdkSHofqRG9FBDH5h23EM_cJtMqH2btwHmlxnOejSK15vkyYutA84hoqqWHkpWdFXl5KZNkTlkHJGa8OysNZxYxlBiRuvuBZwFl-37VTYRqRvieSTVh9l4VQWpJZdYhPBj70soXuUrRYtDEQJouwYm4hHZ-wBIJ9ShUUNSu4-bYTHar16Q-6nxMZMdrfrTT3yAOC8wX_dGogizqpEe72aXsvOKVA1fVpGl2QHt5lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RAsGcEIhGKnrxbch-WQ3fUYUoylpSzgdifQlccWZ7a_V_jHuNdhXTGlGi1YqIHxnwVTTYL9qJAW5v5wgff3evzv8PgPUDlO8ugMj8SjRn9MJ45dFENCWILGCwQDRpPQpm7I1Oz_ELsOoTiHr6yJPc04OWfISt7-K3EJ9dxFguCk9EJ7JEQ-VLVNoj3M3ooVmQp5Rw6LiuXn8h-i-vAnZK7lwLgHuXI5lGEyOKzUXbVw6bBA3ziwPPexAXbFCDfVXbSnmB8CxdHTAwb2MhUGG6ZJe5Xn08t_lz3xFTF5hSeamtm_l64RIMStBti0wP__k99jhEt3GZll6R-2OEMIZHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
پنج فوق ستاره برتر قرن بیست و یکم از نگاه هوش مصنوعی در دو قاره اروپا و آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/31085" target="_blank">📅 13:37 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31084">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJV1bgGhOB9uSsicBIzZ75AJt4lAnN9ij-WlP0qOtLMZnR7HKZvjDfJMBhO_tX-04_jQghuMMyA_W7fmjLSpel95JhwLhnBzR6iHDBAavh4OA7uQXZJN8wpg3HwWu6TnH7wT6q3PAZNyXjllcbDW6UvZuUeDflzQdHJrXS9nikWTo47VgaksuvNqIVBKHfg7BMcp4cB0jMEqP0l_JKnWgfCb_CrNc1_TrIq2mFzfrv5fRih4K72dAqZy2qf750nb5cNma3oFCfblZU-vsBlRYKE1oPUlsNPGOu1QvCBu7XfOGR9-iND5MaGkWkZGU546Ni-0z77dibg7UvKe2QEdEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام وکیل امیر تتلو؛ دادسرای تهران حکم به آزادی امیر تتلو صادرکرد و او بزودی آزاد خواهد شد.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/31084" target="_blank">📅 13:22 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31083">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYU5zEqKWITfO1oYrtxI_ojFPZkw8LPnp66Sxp_PQWFpBTJFbsag4qUA8B7xeZBSKoNcx4Ni-9A8FfJ_Db2bl_UVRRIKuDXmQ4QCayJJPEUVxe9gU1W9ockJBvcpFFGsRAkMwM7kiaW7SOANj3TGF8VefXthZ3ivBJy3tAVNXpBomrCxPP9Gq1JrdpDPw_Vs6krz9Tq5b9FM9B6sVEjzICzoXnuX2Pk-JhCvbo0L2unTVCyjKXyTQMIsJt7_msTPdTnFbRkxXF9vnM1kI5EFyDS92Q24v7iJ_7ZVOMeUbYdQFaXqZn0-Y0W6lOOZSZ8EEvW1hXCgQv2b4_vzZF3ruA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌امتیاز تیم‌لیگ‌دویی پادیاب خلخال روخرید و از این‌به‌بعد با نام پرسپولیس B در رقابت‌های لیگ دو کشور حاضر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/31083" target="_blank">📅 12:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31082">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GoXKBBAndpwsBpqaSgNFg6cpLgRsINfebTi5FgaXZhoZMACuFA2u5zKXLuoPumfxReRKoG9FuDQHR4nCwhhk1V1eoPoWEvLikZJc4FiKuxI8pThXnjFUL7iUiLMD3j9bifEr_NoNeJagfGnKKqBoyFKvNBPXoxasPUFa9ZcsFHmkTOAPaJsNoxX1djTutk8RO0oE8H5J-XZiduoQgtyI5W-g_-dd2iBSX68lxm5RsqEapgitQsSyWkgkztZNlXBD8VbncNqjXAcIyr4xwTS4e3ntgbGODfvZMbUfTjQ8ElZESC49ITPAexpQtb7Ab39tvpB5P0O5vqwwRwxPuhF0Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛ تمام‌خانواده لیونل‌مسی درمراسم خداحافظی او حضور خواهند داشت نه تنها همسر و فرزندانش‌بلکه‌برادران‌خواهر و مادر و اقوام‌ دیگرش نیز حضور خواهندداشت قراره‌این‌مراسم به یکی از بزرگترین خدافظی های تاریخ فوتبال تبدیل شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/31082" target="_blank">📅 12:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31081">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2ed844901.mp4?token=GI6aYwYoY162T3Gwn8C5Wmexuj1fEOhutIdP3yNpOPjmxZqQRYvXcBGupWdsuLzDDi1Dy3cMimyOcHa-wlosd-HstJlGIvZQ_5RVjqn3WGz_dMwh4-mpsO1rjRwWSLHdAgSx4gmQZIK_-DHPocNsXtpS79AlLwtVxdCvDpbWMyhUFSG5Su9aRRswL6BsUwsdxV3dY7Br9Yy_9bt47au5r3kGjTuI8Wx1WTN3Ew-PxFsQDVP5SnBWu_zVjVPPegrXdZAo2O7YkyUUf6cFtdNWyMSm9DXkj0idhRXv0VzprSXDVDKik9dFKjs7VlWENlSX1UIOTZsAgqmaqmh9LvJj8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2ed844901.mp4?token=GI6aYwYoY162T3Gwn8C5Wmexuj1fEOhutIdP3yNpOPjmxZqQRYvXcBGupWdsuLzDDi1Dy3cMimyOcHa-wlosd-HstJlGIvZQ_5RVjqn3WGz_dMwh4-mpsO1rjRwWSLHdAgSx4gmQZIK_-DHPocNsXtpS79AlLwtVxdCvDpbWMyhUFSG5Su9aRRswL6BsUwsdxV3dY7Br9Yy_9bt47au5r3kGjTuI8Wx1WTN3Ew-PxFsQDVP5SnBWu_zVjVPPegrXdZAo2O7YkyUUf6cFtdNWyMSm9DXkj0idhRXv0VzprSXDVDKik9dFKjs7VlWENlSX1UIOTZsAgqmaqmh9LvJj8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظاتی فوق رمانتیک و شبه هندی در شبکه سه؛ روبوسی های واعظ آشتیانی و علی خطیر در پخش زنده؛ قبلش داشتن هم دیگه رو پاره میکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/31081" target="_blank">📅 11:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31080">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuIc0svPpgmZxBZsgyCXpFXyiCqgvBu-KMst5-4uHCtWDvIRAvGUGBHU6RwpflHIC-Id8GSKZY4HzMsWC4snjHd83SCUcxDp7dq15aB2vJWpHHYpuAtH--d6-elxC0aHPBzfOHKVt8-2E-mtH4b7dlWM5nKIMYIq1CyQgWxUq2uZNn5wG-5yyjt2n7nKgPLGWh0m--aZjaFxyCAu3SHeXOhhVVwg5cLx52LKAGWeIn5Fk6zWe0CRgQqo2nTZxq-D9jO4KZfiaWhQJEZBJJQmCMXXENMv18LdMR7sI6xpNgf4BE0sO_EuF8GbXsGGlfJ62CaeCvnI8gSs1BSj1uHncQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/31080" target="_blank">📅 11:19 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31079">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e2faae04.mp4?token=nHGyeItDqT4tJXiTcGVQsFXXfkvB5gblESY9TcvMiBEk0vFTwcdcidkXl8DhdN8lE84U9gSZK6yRChZ31Vg0N9ZzIRSXf9qOBS9cXNzxw8cdNJ5R17BAn9K8sMF-SChkeso7EgazUkYnB4RG1bBPagNoWBufHZU3ZMQJz_B3NOBBgzaF6lLt2bzVTj1lBToD_0-3R1DYo1Vg6z6n_5uRYvnt4Ziw32inQj1y0-QmDuGp86VMeVcsb5KJr9AZD2YGdWiqyOhSZpXBQiPH16ixa3IJSsM1cT8pS70EqgNhLpRrc6s-72M44fvWCeZB8joII4EmaWzMxGbQENbq0bU5Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e2faae04.mp4?token=nHGyeItDqT4tJXiTcGVQsFXXfkvB5gblESY9TcvMiBEk0vFTwcdcidkXl8DhdN8lE84U9gSZK6yRChZ31Vg0N9ZzIRSXf9qOBS9cXNzxw8cdNJ5R17BAn9K8sMF-SChkeso7EgazUkYnB4RG1bBPagNoWBufHZU3ZMQJz_B3NOBBgzaF6lLt2bzVTj1lBToD_0-3R1DYo1Vg6z6n_5uRYvnt4Ziw32inQj1y0-QmDuGp86VMeVcsb5KJr9AZD2YGdWiqyOhSZpXBQiPH16ixa3IJSsM1cT8pS70EqgNhLpRrc6s-72M44fvWCeZB8joII4EmaWzMxGbQENbq0bU5Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
25 سال پیش در چنین روزی؛
دیوید بکهام با این کاشته‌ تماشایی در وقت‌های‌اضافی‌تیم‌ملی انگلیس رو با اون همه ستاره و اسکواد خفن به جام جهانی برد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/31079" target="_blank">📅 11:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31078">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8R5mQp5vl1ZyHRP00WfAooiqpune-TvuxKV0shJ0BGyIsrGMpqwX0ARvaxeBaeIAH5p3oK2qXCnTm12fyvmUVHV-EfGIof-34TNYSDskOniQjQ9vs0ZS_5qG5PS5jwpW7YLL9CxktxeQMqYgixHg5ulN_3c46X4y4QS-VsU7ZwNyBJNTbiWNhBCQ8WRtoLPHaon5Tzn9bm_-zx7iVEljCbDFqLojUDply5iUJm492ayYs9gsO5DHXEFUF05-A_t1fN7hHqvvhR6GPA8g0U-4nR8kBOE8AyplVilS3bZ-dlvhK_IXZhDQIdcQi_FUhEJN7JliVTnU_95BJrFZGzCiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسامی داوران هفته هشتم لیگ؛ وحید کاظمی داور مسابقه تراکتور
🆚
استقلال شد. احمد محمدی مسابقه پرسپولیس
🆚
صنعت نفت رو سوت میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/31078" target="_blank">📅 10:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31077">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb0144545d.mp4?token=fYQS7Vy-nbJ_jrg_O4z1rehEU0zrudhfYxbSCUSbc7SFEcZISt3y_BU9rBvL0XdqzFs47UqW5kM2kU_ud8YNAQa2BXF8enLsM5y680y8ONdUu3ipwBKoxx_cM7LbouGko-a0KBl9B43fPenURKjPkv24M9TR7SACoD7gE404Krph-VlZ2UJuI-hhlXLXeWCe2DBRY894VrOBo4mFUQIMmlXe86kawcyZw5XDzgUV2lN-6zmlSfMk0pXpnVxNf_Xxk38SZDZTKfzyeq9VJW5J0cR5xwzMQtXgGTu_9hfZteO30RUst3jtYcX7etKE3wQGJtxYrN-cmyZOyCKqe8xwNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb0144545d.mp4?token=fYQS7Vy-nbJ_jrg_O4z1rehEU0zrudhfYxbSCUSbc7SFEcZISt3y_BU9rBvL0XdqzFs47UqW5kM2kU_ud8YNAQa2BXF8enLsM5y680y8ONdUu3ipwBKoxx_cM7LbouGko-a0KBl9B43fPenURKjPkv24M9TR7SACoD7gE404Krph-VlZ2UJuI-hhlXLXeWCe2DBRY894VrOBo4mFUQIMmlXe86kawcyZw5XDzgUV2lN-6zmlSfMk0pXpnVxNf_Xxk38SZDZTKfzyeq9VJW5J0cR5xwzMQtXgGTu_9hfZteO30RUst3jtYcX7etKE3wQGJtxYrN-cmyZOyCKqe8xwNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک دقیقه از سوپر گل‌ های چیپ و تماشایی در مستطیل سبزروی هنرنمایی فوق ستاره‌های فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/31077" target="_blank">📅 10:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31076">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFIJ4Um9q6z7yrRbJg4RSHjK5xg5ZKCtW8BdrsSdZtze74AW99eZqZcNYjKf5gxZCSlwkRRfLIuJIrPWu5zL0ttOtNaelvOnOQ5kGC_dmLZcCpI5S3F6S5MzNf6xen5ig5-_iXTeBTQuzMdkB_DVaw8u-L_GdrFthHMiqGE4KRQWbwykVPSiJpc8sq0Eg88gg1Yfz5o4330dU_v-wU3lYj4YKE-8JFCaKTkV7Xm8skJJLWlSKP3o9RQwvaaR-MBK86qxDit6zMTMRm8jFyXnHY7DQ5s0LD-TBgDy2df_ep7QgiogBcGC3pSGssCyKN80fjYXNyqpwLdeJ7r1KMHJFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/31076" target="_blank">📅 10:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31075">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcjgQkIgxeLbmPty_3iYgstigKH7dj9NE4Enr9W3jOCOu9OsK5-WxXnrXdTGOyxXqVJXqtq1wYK0MnzBmow-7oywu5_KmzfshdStw8aedREpJRt1Di5OjiikIzDyUzXVmqBVxy4epfDbfIWjGPoWmI0Pk4RScd1Zu0XCBopdjD9SrAQK7nS88mL9ADMaqgVeQlVMgL5nNpSv4iuewbKEtFrd4ZdUg6bfq9972L5REAIWLXVzumtir-ZhY7Hm3pXsg_Lsr15_B4sd2UV-UvHOmN5SOHiFDjYICVML6I2MvRcBq7aPWeUJP-yg9e0tsFD0CZguxKGvL8QFoxhubl7Y3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
خبر خوش برای هواداران بارسلونا؛ با اعلام دکو مدیرورزشی‌آبی‌اناری‌ها؛ این‌باشگاه با رافینیا دیاز فوق‌ستاره‌برزیلی‌خود برای تمدید قراردادش به مدت چهار سال دیگه به توافق کامل و نهایی رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/31075" target="_blank">📅 10:21 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31074">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5V6VSFyNjiteZSQDDlD5ZUECJSmruL7H0tv289ESeAj5z5CFAXkTYegHPugZDus6WeiZn8kXzUBtkQ5nb7rn2jBpSw2hCiguioeGfkje8GqgiXGOxNYi33iyPrzffC-ul39hEnn0eX2iD5YyKbTtVfepa7jh4EZbr5Lrjg6Xo8cesU8E6xnvbAN-8DcwCkj3zleiPohzc_GG3FOHtOTd7AiLjNql_xTZcPWA4F1yT39DzIE-t8agKefKOyhoF9WWAomRlT6TDJA50NUCA94hW9jzL02WX3Lkll-Va7rpzbLbjks7xhAh1H6VJa-Vu84G0DGWYUy7gHUBk5leuoM8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسامی داوران هفته هشتم لیگ؛
وحید کاظمی داور مسابقه تراکتور
🆚
استقلال شد. احمد محمدی مسابقه پرسپولیس
🆚
صنعت نفت رو سوت میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/31074" target="_blank">📅 10:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31072">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LfHQ0yW-pUS3SQgZMJVf0f6M92QWZV_fHbTdVdXUYM2Q-yJeKgFOrp7fcPUZvQFyUzwGXboOI5gkSLyB_vLPNj19GmEuEylS9HcPmcol0HcIu3K2FCPMrRAJiAgmqgzx7WSESQPy3CCrKDpo0mJZq-RjQ0ExCMAtvVvMQWB1O-Yt8NDkZCWXh2tPL6QcIFMu4p75aZbztMsyBrWL7Hmsiur4es9ii6oTZK5TRgyhbPm_D1EzRBLA1XuWjCmBvGdmynRa5dk7pmzFav41KUL26MV-iX8uN-rT_pyvv1psq_PiOuxxTCBdYnXrjzv7gy2YRNEFBmzT6OPaDC5hItPERA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QNaLL8Md36YLVuF9_dKKK9iO7Me9NblORoeEbHQaZZtwubx0Z7nI4y-a5Yk_4XMMNZYEloLWuW_rYrEdK6Oo_lU5rhgnwxpnUI-I569K9bldhbq1wl0WCP7AuDssdCFanjgld2nqbU5ub8QPCRiK3jc1PIVCHYGp0q3dUV_q3jd7GqhU_kAuermIEEy6DO90zeCpjgIByT7qKcRnVcnakrBxzio16xLKx3S7wQYPWax_M_fbqpWmQ9kWIpo8aftYs47_cHn0jZ8PLFJDXG8tcyIujwwbhvXbuA9ecEfqEj6X6ZKmy9bh2STR0kUpnLLwUEwRfyTfkNfxi8zrggGgdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
👤
سنگ تموم پپ گواردیولا برای لیونل مسی: تنهاجایی که ۶ اکتبرخواهم‌بود آرژانتینه تا در مراسم خداحافظی مسی شرکت کنم. من به مسی مدیونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/31072" target="_blank">📅 10:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31071">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10ac8f2e13.mp4?token=T2-T64RHeYm3OBKMAAliZJJZ_RyRF2sSsPk2gJrQ_sOXX_4kzH3ZIyg2sTASuwNA2858c1h7oBLAICBCKQ70c0-v_8ch_iRLUcvfupC2s8n82F-KXvl_GTKVnuId8L8zNMpPhQMEpad0YToDXKhipYsGJ8kUee-3IkA0EbnSmF2vqHq72Z9E8lIvweyL4RyIv2hBJP1mmCOpksN73DrPavqj9dURd7LuqCw-a9174uXeezPd9i8zdtH6WMw-JyAo9MctudXQx__424l52SrD7iyYJLID9pLGWX1SBfZ0LZRco4ZosNXOKwYVoUSeNwbPD4q3rf17-OMzttqHvxKQug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10ac8f2e13.mp4?token=T2-T64RHeYm3OBKMAAliZJJZ_RyRF2sSsPk2gJrQ_sOXX_4kzH3ZIyg2sTASuwNA2858c1h7oBLAICBCKQ70c0-v_8ch_iRLUcvfupC2s8n82F-KXvl_GTKVnuId8L8zNMpPhQMEpad0YToDXKhipYsGJ8kUee-3IkA0EbnSmF2vqHq72Z9E8lIvweyL4RyIv2hBJP1mmCOpksN73DrPavqj9dURd7LuqCw-a9174uXeezPd9i8zdtH6WMw-JyAo9MctudXQx__424l52SrD7iyYJLID9pLGWX1SBfZ0LZRco4ZosNXOKwYVoUSeNwbPD4q3rf17-OMzttqHvxKQug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌ های‌ سنگین‌ و جنجالی ابوطالب‌ حسینی‌ به هادی چوپان
؛ هانی رامبد دیگه‌بهت برنامه تمرین نمیده؟ ایرادی نداره بیا خودم بهت برنامه بدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/31071" target="_blank">📅 09:49 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31069">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmRAPtS8F8u3YwECevmhtxF6GLNEB0sNmfcKaXHG55WQ2Or6kyivkHdzqnAj-3l_FJNmmLMDJxvo1fHYPAIinlEENwU1zrmJ095trn-abeBQ2neqLIFKNOfyTF_VTvR_3gXXeirLoUJHaIx_rxy_MON5mcVyYzbjzGygHMnksRF3gMDEiybGyEfg2RLZYtLFqUdeEe7DTkycXs-aFLRC_i3Y-MLx_OKw5NHLnVSk9tgGfj4vXhKOk7tKNQiF1J81OeuwUM-y3Bg-zFHXV-8N8aW2cBAJ7LsiTH9PybY35z9VtTeU7hXlaj8dBGKJwyr_b8ayRSQR3bjCwDthpwbn-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
جالبه‌بدونیدکه؛ سال 2013 تیم رئال مادرید میخواست تونی کروس رو از بایرن مونیخ بگیره که مخالفت شد اما سال بعدش این انتقال انجام شد.
‼️
سال 2020 کهکشانی‌ ها باز هم خواستن داوید آلابا رو از باواریایی‌هابگیرند که‌مخالفت شد اما سال بعدش قطعی شد. سال2026سران…</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/31069" target="_blank">📅 09:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31068">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rd4akD-u4047_r1GkfJKm90TPypFQW1sKamTeeXKkBZ-NErtyxOZZ5mla-9oYf2D9Zw-7rdflNY7UMSMOLvAsyAJUdmZ578tMoJw3sgwUvZbRxCNW2084ULS9bK17XqIHBCUOhfDQJc_irIrmPSzcfs204Vk6koPDgr69izKZ9jh1wJR4Xh9o7hcoNmI94ZJb_Q-aRe84deYCUC0as4eL_wSX03H1tfRSHsBXlDqIKnmsxZ76mox0pe3Hi80t8CRtn9tX_EZME5fpSDsW9qgCvnbrXv097qMy2PFnUbVEIAcKXIzS2CxVqPfBuDVnn6prtTeH0mkYeGcjjxVW2QzEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛نشریه‌بیلد: باشگاه بایرن مونیخ امادگی خود را برای‌ تمدیدقرارداد مایکل اولیسه همراه با بند فسخ200میلیون‌یورویی‌اعلام کرده. سران باواریایی‌ ها حاضر نیستند با رقم زیر 200 میلیون یورو فوق ستاره فرانسوی خود را بفروشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/31068" target="_blank">📅 09:19 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31066">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTYsxKJfBQolMiXH63X804GFoi2W4zcBze_tsaQmdCoBGWTX9tc33_gy_bdP-wKBYd9Dl4HJ0O3Bbl72JfFO9fTx5Bgh9fzddLQ400aazkKGqjZlE6uWSsxZ-NoTe5uPORKFAkT_kSWacD2af6VMunP8glh6dliaADHLYkwyYowmKRC_905jdDNd8dNIhnMDSbq2dKxo5ifXehKttFXIsOwu7dY4e4vMDLTFKWT36ji04OU5yoZZvkhrddA29Hta7SNl4MqxbiWYtjRApyiuLqB4kBcpi0t9kk-5DOm_TOox4kXhXMJpIhcj-SBK4LEFwG24qRgCL4gT_Ug4ewdEIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84daabae54.mp4?token=AeDeIsNnHcyfG_9RPhWUvOPXWGQ2C242-tjxEkPRYlEL74czysQkOJtp683Fv7ibyr58CPRfWih2XWISShyBop4OvWpM9cNPBJK2IqbY3efhPWYDHj1Kc5jdFDLTDaElS0v25ZhM_XHwUVirKC5EO_OTOTBloWfznPLuJvcrTRoCzeDHcZ4KLqtHD_zotPdE4cXPzQ6kx8TmdCn8wGE8YshxLPn3mtlaIU7xQzze_PkE5NSBEJtUY5EJ6MBYPhHz-A5NxZM914yCHxXaVyXYtb-EtY9CKLWzt2GE9UtYU6ajRe4sm87y7M-cHF4LY3eaBAkQxNVV1qyG_-6eW52PlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84daabae54.mp4?token=AeDeIsNnHcyfG_9RPhWUvOPXWGQ2C242-tjxEkPRYlEL74czysQkOJtp683Fv7ibyr58CPRfWih2XWISShyBop4OvWpM9cNPBJK2IqbY3efhPWYDHj1Kc5jdFDLTDaElS0v25ZhM_XHwUVirKC5EO_OTOTBloWfznPLuJvcrTRoCzeDHcZ4KLqtHD_zotPdE4cXPzQ6kx8TmdCn8wGE8YshxLPn3mtlaIU7xQzze_PkE5NSBEJtUY5EJ6MBYPhHz-A5NxZM914yCHxXaVyXYtb-EtY9CKLWzt2GE9UtYU6ajRe4sm87y7M-cHF4LY3eaBAkQxNVV1qyG_-6eW52PlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇺
گل‌های دیدار امشب دوتیم فرانسه
🆚
بلژیک و دیدار ایتالیا
🆚
ترکیه در لیگ ملت‌های اروپا
👤
شروع‌فوق‌العاده زین الدین زیدان با فرانسه: چهار مسابقه، سه پیروزی، 1 مساوی، 0 باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/31066" target="_blank">📅 09:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31064">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5ztf_MJ9-hTkYgayIf_adJlUbiUIY_XoreTBHDihsYryQ9I96-eHiZ-ARwj-1aSj9q-lIajj7snW0leUxQEIwZvKE-1t2EJo1iqN_8Zxkf2epJUyBmB97k4PO5OQIRIqob30Mvd960v8K7TIxRRbxHg41c_Ypv15y6vQ5bow3hZ1Qlh-AtUmZufdahSMODUP88kzvzSseN2ZKJbZHEYeJe3BUQQ1ZN_Ukhvu_TbwLMreZ7opG2zYPrNXklnmkWOv36kEc7rqE0rh9Yn8KmLiGJUe3tYubB3dLZYkyOBYHytgEItUYv0OnrB8BQdIYJod4NaWtiZJm1RxfeFLLPqVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌‌ دیروز؛
برد چهارگله خروس‌ها مقابل بلژیک و دومین برد ایتالیایی‌ها با مانچینی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/31064" target="_blank">📅 08:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31063">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPYTloHwVc5m4J2kXQfg_6eGeTVURCVvW1v6CC9KIXrDtIAcFskHP5Jv0OyWIM9iA-zfyqYuo7uox05Te57mhIhFEHFVGj8QZCSr2a6B8SKC2m_r7gw2YjMsLKTmnTZHgFhP7cjPK78AsHyAUpTbVrV4YWoxhB1G0PN56A9IVtJMcFjrRlZKCQpD_H28WjtmwqpOP5TmDVtYNJhm3JqiPXcmbB0og1uYMLrHrDuIYu-JpnosSecNe0qjijpJLKoE5JDJi0bRIurnuvBO4Zh_UOFQOT8gyEpFDFPUvak57WMmWYGju8ASfrrUVyAf7GNZW2kSFw2Eg6DpFkdjNeaeZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدار ها‌ی‌‌‌‌‌‌‌‌ امروز
؛ جدال خانگی کروات‌ها با اسپانیای دلافوئنته پس از تحقیر مقابل انگلیس
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/31063" target="_blank">📅 08:02 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31062">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e146e3bea.mp4?token=EI2WIb1COt7-PDaFpFeGguoqaEjXn4u-Xnw_96D4yI3KwCdMqdHH4rVew0FepL8aEsOxWd_LdFakKjtAQ2HW8YIplt27L-IYHkxkwUimqkZqGXQCcxjhAzpkWtfXzydH3OQRXxQVhFAZngCLjQOjIiYS-73FdkuXx4Xpy1nUfDPNoLrGjhH_WT4_v_sDzedYouCGvt5wT5Hzew8-nIdeTVTSlhhoSA8Uit6gJRjRAS7PWdSGW7UvNklYzj3wBP7kJg53Ze1MUKsRhv97MVwrGGGfzVZNcqQDIUPzu6pIUMSOfvaFzsJzNFd_14H27Cs0iqS0knt8oUeW6zwyCRtPwoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e146e3bea.mp4?token=EI2WIb1COt7-PDaFpFeGguoqaEjXn4u-Xnw_96D4yI3KwCdMqdHH4rVew0FepL8aEsOxWd_LdFakKjtAQ2HW8YIplt27L-IYHkxkwUimqkZqGXQCcxjhAzpkWtfXzydH3OQRXxQVhFAZngCLjQOjIiYS-73FdkuXx4Xpy1nUfDPNoLrGjhH_WT4_v_sDzedYouCGvt5wT5Hzew8-nIdeTVTSlhhoSA8Uit6gJRjRAS7PWdSGW7UvNklYzj3wBP7kJg53Ze1MUKsRhv97MVwrGGGfzVZNcqQDIUPzu6pIUMSOfvaFzsJzNFd_14H27Cs0iqS0knt8oUeW6zwyCRtPwoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
باشگاه‌استقلال‌خطاب‌به‌فدراسیون‌فوتبال: شما جام قهرمانی فصل‌گذشته لیگ‌برتر رو به ما بدهید ما خودمون نمادین اون روتقدیم شهدای میناب میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/31062" target="_blank">📅 02:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31061">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/612b743bd9.mp4?token=Zh436LkqIFIp3klEgG07-RXf5PhQUh_dTRtQRif-yVTHqq3tNo6gI7mfxFL6bU01dGm7zgl9M3mE1SkuDfVNr2Q5S6Y1GkbOrx6cnJ9tOcCx1Pek-OIrd61qtf40G2kloebi0vq-54JYuScMELCKSkUiRdqKB1jAUQCUgzhoIyjwVnZScWJR-NWGDYdVInc_QST2L3AiyFoI-pQoQosG5b_7_WX6rhshdLCAKmGhX_QrBnVMABs8asf8G6fiRBVCO03tUgTjrMuk79JcAxIZS1OA1mOf1uHgAiKGfYmEyg35oiKRXpVOB39d8hqnXaN0KPHJCSqPx2AE4f_ds1eFxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/612b743bd9.mp4?token=Zh436LkqIFIp3klEgG07-RXf5PhQUh_dTRtQRif-yVTHqq3tNo6gI7mfxFL6bU01dGm7zgl9M3mE1SkuDfVNr2Q5S6Y1GkbOrx6cnJ9tOcCx1Pek-OIrd61qtf40G2kloebi0vq-54JYuScMELCKSkUiRdqKB1jAUQCUgzhoIyjwVnZScWJR-NWGDYdVInc_QST2L3AiyFoI-pQoQosG5b_7_WX6rhshdLCAKmGhX_QrBnVMABs8asf8G6fiRBVCO03tUgTjrMuk79JcAxIZS1OA1mOf1uHgAiKGfYmEyg35oiKRXpVOB39d8hqnXaN0KPHJCSqPx2AE4f_ds1eFxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیو کامل برنامه امشب عادل فردوسی پور با برسی اتفاقات اخیر فوتبال ایران برای دوستانی که علاقمند هستند برنامه رو کامل تماشا کنند.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/31061" target="_blank">📅 02:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31059">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nat9nj69DnsJiE6NKRxPmteBxY7pBjnzr0naaZEIKl773arfJTLEw--OlwagK0Hkp_qUJEtXDbwte5TOlFwwTTAwch2yqiVtjXzcCTtRRZi686GgSjGPvQD5Vvvrqz7Br4FNwexagVjH16bg5vFzZwt2rJVE5QOoNm1SAlICaORXAmx347JvbeEm5BUIqAZAkMjHHWHd7w0DfHO6aH9N0QHQYVO_jwWN1x2Eo3Kdy1626ECpVVHDKOubiZKZxvrXKSvzBjiDg5smSu1YadyV_HQXMHD57iaBVvzVQrBfx-UJg2qoNLS-ykCkWKQkftAR4jbA9fkgNmhJODS_59_K1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روماریو:
امروزه مد شده به فوتبالیست‌ها میگن بهتره شبِ قبل بازی رابطه جنسی نداشته باشید ولی من باهاش‌موافق‌نیستم. من‌شب قبل بازی با همسرم میخوابیدم، صبح هم که بیدار میشدم دوباره باهاش میخوابیدم، آدم باید تو زمین احساس سبکی کنه. به بازیکنان توصیه میکنم این حرکت رو بزنند معجزهه میکنه. دو راند نیم ساعته قبل هر بازی توصیه منه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/31059" target="_blank">📅 01:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31058">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1edc763594.mp4?token=vY1gYACdMSiozovvq7Un7Pdo3NE7NOlm-Xr8DL6DT4hod-YyoRru6sUEx7Ak76FoN28fh-4ldMdIPrYt5yfkNwAxs0jkIDwDicWJ-Im8V9Rqo9emuJtMynmWuX3o_m7nLxY1XDHpdKZ7qS0iRSlkSu0b54aS9moEnuymFmhkPVce4nHjKIJnLH4zNKTrMLRP-KlQEAracScg4IkboJioztA3wkiqq6zo8RdJLyPogmv7Big7nSO-nmmSnsrSYfE4WXmfa-sSHMRW4tNvoYzZgWB2L3wVdQ09G61vL7p94DDQvw6SaSSxRHLfvf1yTXBtO-YSDcjb5uQ2AYnC-eBuuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1edc763594.mp4?token=vY1gYACdMSiozovvq7Un7Pdo3NE7NOlm-Xr8DL6DT4hod-YyoRru6sUEx7Ak76FoN28fh-4ldMdIPrYt5yfkNwAxs0jkIDwDicWJ-Im8V9Rqo9emuJtMynmWuX3o_m7nLxY1XDHpdKZ7qS0iRSlkSu0b54aS9moEnuymFmhkPVce4nHjKIJnLH4zNKTrMLRP-KlQEAracScg4IkboJioztA3wkiqq6zo8RdJLyPogmv7Big7nSO-nmmSnsrSYfE4WXmfa-sSHMRW4tNvoYzZgWB2L3wVdQ09G61vL7p94DDQvw6SaSSxRHLfvf1yTXBtO-YSDcjb5uQ2AYnC-eBuuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ تیکه های سنگین عادل فردوسی پور به مجریان صداوسیما: توکه‌حامی قلعه نویی بودی. رنگ عوض نکن. حق انتقاد ازش رو نداری دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/31058" target="_blank">📅 00:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31056">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇪🇺
درهفته‌چهارم لیگ ملت‌های اروپا؛ شاگردان زین الدین زیدان باطعم‌کامبک‌مقابل‌بلژیک آتش بازی به پا کردند. ایتالیا هم بادرخشش کالافیوری ترکیه رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/31056" target="_blank">📅 00:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31055">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXWl_wod6-MumUbUSE7-t42O7uuJKmoajIwi4U9WDO9RE31RbwKxD3hlcMkWZPOxp1poHZCRYZKeJoS-buAj-rTBmvTihd_7XxnTuFhlNyzCEpMa02G0e4mEPDVvtYrEeGpxyMTPra4HWpiIj9onzoDmmhpvrC12dl2cp2POgXbjc1sFTZS1UA78aiJ-77ajK3toB4XSA-vHo9zyYB2dRkf9y01PVD_1daSd72y4ffF0loSdq7HwHJKZglX17z3Yxqxbh6k9MEBbt7nPfbDMgbTwCZ-T-4zkOO0-4tye26B1y7muU2jnm-VT1bMqYppBIyaOlet3MHEOsQ-K_1Mbpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدار ها‌ی‌‌‌‌‌‌‌‌ امروز؛ مصاف خانگی شاگردان زیدان بابلژیکی‌ها و نبرد آتزوری برابر سرخ‌های ترکیه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/31055" target="_blank">📅 00:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31054">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0USmaD_HHxcxFiePukzhHyyoXvtEieoGcSWlk7IF_LvAbfWGZKAo2SQjvU6HrOur5A_GLv2TbLDZmR_GnjiT8m_MpL3ZTdsf45fZssV8zzpz_OkopJLamtDveWgIu91k4M0UjwOOvVTj3SPdsoKC4Eo8BA0bREuqEk0NOy8omDEkeXBUwh52Ab2MdnTTH0KrrQC4QNB05AYX_v9jfavHjy2I4p02mCL9DtdUmnxXfKQDC8OzH5hnnXqXX-WOuyEQcqiThW7vyDG_f7itSFpiOYmCllsEn4_kRxSbWT2WurcLJYpv9trpUYs0jbIffnvwIb4MH-2S0J_o_4fZh3KJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
از کیت عظیم و ۳۰ متری آرژانتین با عبارت «متشکرم ۱۰» در پشت آن به افتخار مسی در میدان شهرزادگاه لئو یعنی‌روساریو قبل‌از آخرین بازی ملی وی رونمایی شد. امشب مسی خدافظی میکنه.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/31054" target="_blank">📅 00:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31053">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9410553bb0.mp4?token=PZNvyPgOSp7W8PT6RF5udvCxyfw_P51wgzlEDa-O-W685tRGksYEJr3T99p0ZUMBmO2YgvaLmzp5_dJo8jJyDoUAdu6KTF9iPh3pxuGWIzMKCzRJk7QOcy8ceg7UZ2J42O-DdgFCgt7EL_TDJxUHLNHDJgAVkzoUsbkoQhwOvVABNOt7nIECc5hUejJlOEHsF3AJbN6R2ESqdvVZbRqfaEAmJfE5rJz8QzlkLGiYQGaaZbgApasGAf785zI5kvpjYo3eAMD8m0xkamGGCkQF-zE4Jks73R6_F3u6CnHCKW3FiaA9HB__lOpPTKLYUQWhFX3DVgmVm66MDeRPt2RLEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9410553bb0.mp4?token=PZNvyPgOSp7W8PT6RF5udvCxyfw_P51wgzlEDa-O-W685tRGksYEJr3T99p0ZUMBmO2YgvaLmzp5_dJo8jJyDoUAdu6KTF9iPh3pxuGWIzMKCzRJk7QOcy8ceg7UZ2J42O-DdgFCgt7EL_TDJxUHLNHDJgAVkzoUsbkoQhwOvVABNOt7nIECc5hUejJlOEHsF3AJbN6R2ESqdvVZbRqfaEAmJfE5rJz8QzlkLGiYQGaaZbgApasGAf785zI5kvpjYo3eAMD8m0xkamGGCkQF-zE4Jks73R6_F3u6CnHCKW3FiaA9HB__lOpPTKLYUQWhFX3DVgmVm66MDeRPt2RLEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ ادامه تیکه‌های سنگین امیر مهدی ژوله به فدراسیون‌فوتبال و کادرفنی تیم‌ملی درباره حاضر نشدن گینه بیسائو برای دیدار دوستانه با تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/31053" target="_blank">📅 00:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31052">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W38KerSxh49Apn3YOIRQVGT27n29s8TH05KdJZj8JUcLd48jDtHeip7JpaT4N8Dta9phLqciVTbB_xkmwg9r21E7SG0L4HjASNycA6s3kASVjyCdmuDsWbVKKHDrui49f1SBNwOPG7IkIDYzfP4xe98Qk66dABhrpZl2ZrLVQPysL_LcbM2jza4_1uazUnaDqo84SU81vtsllJNxV30G8dY-eb0PRrylhvGB4sHUtgw885V2uFQEAW58Eq-uRfc3JQ4GJCjmijbKYDWnnnnyfNVjNlQCIDvMPlja6nd7AypS8hca6K2jlVfpIdWlEWxUow_ojbCqRgJQB3oBk_oIkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خورخه ژسوس سرمربی‌تیم‌ملی‌پرتغال گفته چرا باید از کریس رونالدو عذر خواهی کنم؟ نه نیازی به عذر خواهی از او نیست!!! پس بشین تا برگرده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/31052" target="_blank">📅 23:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31051">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0HDJvz7wI9YlmEsKmxPVEQ7nMydYt-7G1_6Tlv44RDIxQ6Nent0C9aFyJU13DRTrpMmMLy5GXWJA42kBXElrleAMpz6S30tiVMHRpShm-1qmhK2fuFPiFwnhI5P6Q90TfxSek8dx5xBXM1C4kqExgrKpHYKYylo5V14Iebows-HUrI47oc--ldtEqSmiQFc15JVBsMPQr5kU0DRl4GPL8QAr8NGIxrsuedNVc_2watA07IWZszqkktdqTQ5sDQmwTERR8l2u--xcWv-XKrlpnBsQN5VFOIlfoJ7x22_AEbVaYyj8Y29eLLgcP4AktMMsNwtIZ33Ezx6K2_svATnjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رقم رضایت‌نامه‌سه‌فوق‌‌ستاره‌ایرانی ماخاچ قلعه، الوحده امارات‌والنصرامارات: مهدی‌قایدی: 2 الی 2.5 میلیون‌دلار،محمدجوادحسین‌نژاد: 1 الی 1.5 میلیون دلار و محمد قربانی؛ 1.2 الی 1.8 میلیون دلار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/31051" target="_blank">📅 23:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31050">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bbe125227.mp4?token=D8zSagYxyqUpJec5re8dhim173BtGUul3ObWe64WG5NqAk2lEgpcLveTZsaZAc4tIszaOZMbX9G1IQDAhg4F64UWB3q0BaaN949OWcNAZ8CfYS-tRwtrSO31q5lS_UsoKIM2dvy_qA79ODnhjRB_hf4T9W1mbsG22vSZnpv00mD9PX4qaLXzBcuzUI1m0FIOWAvYsmG0YOpD3prGGhQcTYlTxT4ht6sQ9rBaHyc2NFv9jIWL1FSmmcMOSPU5hmtiSAtXS6QZ7KMogpsoO5GemzkZ4Gix1HQSSJJDQY4hIAmClYdFsls4Uy2fDucSGhtxlX8_8Wqng7gkDuLBXWF1vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bbe125227.mp4?token=D8zSagYxyqUpJec5re8dhim173BtGUul3ObWe64WG5NqAk2lEgpcLveTZsaZAc4tIszaOZMbX9G1IQDAhg4F64UWB3q0BaaN949OWcNAZ8CfYS-tRwtrSO31q5lS_UsoKIM2dvy_qA79ODnhjRB_hf4T9W1mbsG22vSZnpv00mD9PX4qaLXzBcuzUI1m0FIOWAvYsmG0YOpD3prGGhQcTYlTxT4ht6sQ9rBaHyc2NFv9jIWL1FSmmcMOSPU5hmtiSAtXS6QZ7KMogpsoO5GemzkZ4Gix1HQSSJJDQY4hIAmClYdFsls4Uy2fDucSGhtxlX8_8Wqng7gkDuLBXWF1vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری جالب عادل فردوسی از تعویض عحیب تیم ملی در بازی دوستانه مقابل تیم ملی روسیه: قلعه نویی تو بازی با روسیه از عملکرد محبی راضی نبوده گفته خودت رو بزن به مصدومیت تا تعویضت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/31050" target="_blank">📅 23:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31049">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWGt7LHyBx8n6S3NYyzUFUZfkm6NbmSOHx7muzbybCACK78lATDJ14ZHFXuZ4y1rZH4SjbcfuiU85VbMUwQcK01ZwPylV_JQmmFF_t_QKXBquiUIwcV-B7MHIZWu0v2u7ST_BiMvZJSERM8Sly-0FXn1X6-bcB2c0LPWyY6udvnYGYvUHBwCLi_j0Pcy1cs8y3BUiC6ZDiEuJF_YkCEb5ZR6QZet-dH20NXP6ntlbFdoAQUQL0i40HJeyAu1aoz2npk8tO9xTaXSKPZkmfitq_TvOCH2oSLPUT1XV3TbevrwKonaXMyrkL2teJ4rDpKdqyVMF54v-MFagYlvrJNQDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سکانسی جنجالی و جنسی از فیلم جدید دوس دختر کیلیان امباپه که سروصدای زیادی به پا کرده. کانال دومم داشته باشید کاملش رو اونجا میزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/31049" target="_blank">📅 23:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31048">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39c5af2a82.mp4?token=Fastb1tFF0rdtI68uEdn53bKz9x47oG70PWzQKPzRXoRwNiE_ooMjcIfNODo5ygfxPaO-fSMOUAgz_PxR6fUD3OeJlvffy-2Xn2MzT5p9BGmLGLh2ZOE5l-b7UZrNwjdFiKG6Xps5imzkl4ye70aEuTglxpwv-AecxqbCz1KOuThQE2zKXlr_lOZoKADHvs0_Kx8yAXzfIfXrw3d9p57IpOV9KaOopgiPHzXEM7ypvzI38WQhBbMQ2sUJZ9Ud0WjtEnGZAp4XInemRH0IhVe9L17UcO-RjZvls_VehXMPIO6TFazoSWI8vNXZku0mgeI4wn-5m1J3bLqYLwOMkUEl0woeFTc8tgCzV_vJUxw0_YVmr_2paAoFqFT-nDGP4L7A5qP_dYl1r1PD1crw0-cZzfitFo3Ap8v2Kt9u6S7DCriysGbuTnfqqKJ_h6QLbUJPnc3C2HZMz6uM4nMkw5ArUtJnf7qNpt72fllgDzqQOlUA5iMYzr4J07Xozo1p7az3K1Yu876R9R9aBoAe2lR2AsrsFxmr1bcF-wpfMJ2fpm7BaFUej_JUnhWUDfo1MM2PZ3jlSXNfJKpNQmmyr1trHHJ1mdVE5MykoRD1hzcHAcBzP1dO5ypEJzBSsLbQc-oHHKIp9rpoWCgTHxk9HsoGjPt0k0ch2IfpudjZEQzDLo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39c5af2a82.mp4?token=Fastb1tFF0rdtI68uEdn53bKz9x47oG70PWzQKPzRXoRwNiE_ooMjcIfNODo5ygfxPaO-fSMOUAgz_PxR6fUD3OeJlvffy-2Xn2MzT5p9BGmLGLh2ZOE5l-b7UZrNwjdFiKG6Xps5imzkl4ye70aEuTglxpwv-AecxqbCz1KOuThQE2zKXlr_lOZoKADHvs0_Kx8yAXzfIfXrw3d9p57IpOV9KaOopgiPHzXEM7ypvzI38WQhBbMQ2sUJZ9Ud0WjtEnGZAp4XInemRH0IhVe9L17UcO-RjZvls_VehXMPIO6TFazoSWI8vNXZku0mgeI4wn-5m1J3bLqYLwOMkUEl0woeFTc8tgCzV_vJUxw0_YVmr_2paAoFqFT-nDGP4L7A5qP_dYl1r1PD1crw0-cZzfitFo3Ap8v2Kt9u6S7DCriysGbuTnfqqKJ_h6QLbUJPnc3C2HZMz6uM4nMkw5ArUtJnf7qNpt72fllgDzqQOlUA5iMYzr4J07Xozo1p7az3K1Yu876R9R9aBoAe2lR2AsrsFxmr1bcF-wpfMJ2fpm7BaFUej_JUnhWUDfo1MM2PZ3jlSXNfJKpNQmmyr1trHHJ1mdVE5MykoRD1hzcHAcBzP1dO5ypEJzBSsLbQc-oHHKIp9rpoWCgTHxk9HsoGjPt0k0ch2IfpudjZEQzDLo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های عادل در مورد بالا رفتن سرسام آور و تلخ قیمت دلار از آغاز هفته اول لیگ برتر تا به امروز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/31048" target="_blank">📅 22:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31047">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f9838cf82.mp4?token=MbBUbgMFXkKsshPgBkwMNwrNQjrrvIgSYJealMLUTHk6FBGzyiQP_MtOctFsZLYx5-3py-FAcJyOicL_1wsmi-g3b1D-6nOdE6eGeaAux1pcJ656qXFwJ6GsJeQsCSJ3xl8mJ0QLIg2jm-xZ3C03GU-PxNfmCbWRv12WvJI2IeWBj9mhL5ZNDeLIgX6P8oL2mUDzgsiZVJU9k5jshj_la8uCJXiDcwsyFvyR6HTSSKqX8ikLi8z1i2AwYuJN06sixR9luk2RC_EdsagDpYNbTWW0jpH-Nb5Rqq6ICvvH03sPc6EWRoHLXn-ZLX018t2vO5dyUeoH8kipc2GTRSNnvDUKz8f-fTKP41XzuEz9FIikMUE4cBlWS1duEYWe5lGKvh7IYuZbYg1Tm1NL9dYIe0UXW5j_I5qlazxiV9owp9qnH3dxz0MFcFZvRpKjphcvrY552srtVKqkO4llAnUkmJnofOEi9Jt0utoI9AeB6x3a9ygeDGbveaorly1J8eXBnCYUSG25eVh037SHDxW1mDWZkEgJ79u0VlYvs33TxNVqDx0gWwHv_-HE0eYE8E71L5TfuCNAPRN4R1HBRWT1XSN9QTx9duPHao23aBQzzBrSb9jFscTXBwiYPJJxVP7bWugZuMUhX9LUrF9QZy972ijxaa8v5ZtBC12tirX043s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f9838cf82.mp4?token=MbBUbgMFXkKsshPgBkwMNwrNQjrrvIgSYJealMLUTHk6FBGzyiQP_MtOctFsZLYx5-3py-FAcJyOicL_1wsmi-g3b1D-6nOdE6eGeaAux1pcJ656qXFwJ6GsJeQsCSJ3xl8mJ0QLIg2jm-xZ3C03GU-PxNfmCbWRv12WvJI2IeWBj9mhL5ZNDeLIgX6P8oL2mUDzgsiZVJU9k5jshj_la8uCJXiDcwsyFvyR6HTSSKqX8ikLi8z1i2AwYuJN06sixR9luk2RC_EdsagDpYNbTWW0jpH-Nb5Rqq6ICvvH03sPc6EWRoHLXn-ZLX018t2vO5dyUeoH8kipc2GTRSNnvDUKz8f-fTKP41XzuEz9FIikMUE4cBlWS1duEYWe5lGKvh7IYuZbYg1Tm1NL9dYIe0UXW5j_I5qlazxiV9owp9qnH3dxz0MFcFZvRpKjphcvrY552srtVKqkO4llAnUkmJnofOEi9Jt0utoI9AeB6x3a9ygeDGbveaorly1J8eXBnCYUSG25eVh037SHDxW1mDWZkEgJ79u0VlYvs33TxNVqDx0gWwHv_-HE0eYE8E71L5TfuCNAPRN4R1HBRWT1XSN9QTx9duPHao23aBQzzBrSb9jFscTXBwiYPJJxVP7bWugZuMUhX9LUrF9QZy972ijxaa8v5ZtBC12tirX043s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فلش بک بزنیم؛
به وقتی دوست‌دخترِ کالافیوری اونو درحال‌مصاحبه با یه زن دید احساس خطر کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/31047" target="_blank">📅 22:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31046">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-OGN90Oqq8bePH6RfAYs2no4ufdmxgokuOaInnw81M0sE_D32x32Cz4L3X8Sq9oNdCB6ZOYHEIUTmPItufvjN3Pcljo6QwsqtLKSrxWkOMbrngAFQoGp_hBRsQ5jepSPCj21NLGzR0Hj-Ii40fIqj76WNKmWvvrK5bRXVBRyR65fSCvF1v5XfZYxMYjSlJkSpVVodTjtbd294WaT7EaZQ7wqwK8Oy7kOcPgDERPrh8BdT1fpoNHbUJ3ViRNS6DgE13OA2VlkQASqyC-0yYrmeX6_inZOR_TP8pGnsJPoHVRMYLN_J_oVZIb0bW-f8-ZxPzRXS_dEC8kHoZxYUS2bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درحالیکه هفته‌اخیر سارقان تو اتوبان همت تهران تلفن همراه‌آیفون17پرومکس پیمان حدادی مدیرعامل پرسپولیس رو زده بودند. امروز همین اتفاق تو اتوبان تهران - کرج برای مهدی تارتار سرمربی سرخ‌ها اتفاق افتاد و گوشی جدید آیفون 18 پرومکس او مورد سرقت قرار گرفت. خداروشکر امنیت داریم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/31046" target="_blank">📅 21:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31045">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fe541534a.mp4?token=d-2j_HbgoAUX4LtqMDCFB5_vD_APHuYVINZFjsQ4Ik16HuiQudSTnGX6TCgPZUZqDgBaJaZuC_b-opKX0w7YaS22RyU9AmFgLXf9ypUy-XL2hPMe1QITbXVcPOUBdWoJiJYf7i7ohyU4-chXUwoYpbprAAOsslkaSd81UzbALRBXGLoZZZdTXjOmRqFbmsPrTJDNZZSuU5o8XV_9TbH159_b_VEwPEfOB2lEMCz4BYc4OIIYch4pt33zIP0j25QroUL3PTmQBf-bD_CWluVqplfHFNxR63zl6V5Dg5SGAgn97_I6vUPqnUfSpwydFdVubc3lbu9zj3YswIZWVTQJlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fe541534a.mp4?token=d-2j_HbgoAUX4LtqMDCFB5_vD_APHuYVINZFjsQ4Ik16HuiQudSTnGX6TCgPZUZqDgBaJaZuC_b-opKX0w7YaS22RyU9AmFgLXf9ypUy-XL2hPMe1QITbXVcPOUBdWoJiJYf7i7ohyU4-chXUwoYpbprAAOsslkaSd81UzbALRBXGLoZZZdTXjOmRqFbmsPrTJDNZZSuU5o8XV_9TbH159_b_VEwPEfOB2lEMCz4BYc4OIIYch4pt33zIP0j25QroUL3PTmQBf-bD_CWluVqplfHFNxR63zl6V5Dg5SGAgn97_I6vUPqnUfSpwydFdVubc3lbu9zj3YswIZWVTQJlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین ژوله به امیر قلعه‌نویی: من یکی دیگه فرصتی به تو نمیدم. در طول این چند سالی که سرمربی بودی میدونی چقدر خون‌ها ریخته شد؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/31045" target="_blank">📅 21:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31044">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RX-HSAy8DACTE-tXoitNwuPbdDFzIvcsPK2mkhMNsd13ppW83mklRAb2ue_8HduIEYrd5rM2H_3gQ4gh78s66SAr40CFhQnSiN2am9WaM38PwKg70lyxEPdgCiuZgPBJKThnf3arNkqM7KST82wuLvvoxe_mOB8VH_oRJaCMS1aO5on1y_Uz2ygZ_OidSsh-Uc2mqxAmNjc1apdSDvEjPiC3YuHY0ujoqoBJPWsFrmn-C7mbQkssOdgDWp3xqUPcjOcA1FGON3RxgNrIAIu_uySBoJJg7mCytqhnWwixPe2ltn9-Lct6EkFS7UWKXTdmRnOSNVLSpVviDuS4UBmSuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
مدیر ورزشی النصر عربستان: با کریستیانو رونالدو برای‌قطع‌همکاری‌به‌توافق رسیده‌ایم و ایشون درپنجره نیم فصل از تیم ما جدا خواهد شد. مقصد بعدی فوق ستاره پرتغال فوتبال اروپا خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/31044" target="_blank">📅 21:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31043">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">📹
ویدیو کامل قسمت دوم فان فصل جدید با امیر مهدی ژوله؛ عالی بود. از دست ندید و حتما ببینید.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/31043" target="_blank">📅 20:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31042">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLO-cEq7ydnNNffxjLr5-Ah5k0UIYdPDnCXKzM9rhXsPfvCIjk_T2jRsC57rNcyllyRsGQApTbEjBN0sI1dEg40fpuaUKRjDsvAXafrykWzxWRRT6nwLB3UUU_ioyF7BsKQXnFneDvOZkI1zuefo2ZGRVolzKfcIi6RpYUiiNxEV6I54-JcXilMYeS-vGIY9OwUNUr9b8ibMSSMvf8jx7zFr1nATOmj5BBVDfnIShfdJ5Ezwae90Jx3xwSPwVreVQCbmjDy6hboab17baRJWBy3-hd8bJSfrrcvFoLGLlShW9YzQu050VYcCdozi1ZjGssbtWvQ2tt83AQctlI-A6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین گلزنان پنج لیگ معتبر اروپایی تا این جای فصل؛ رافینیا دیاز فوق ستاره بارسا در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/31042" target="_blank">📅 20:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31041">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWEv3apbCnxsnM9AlCU4MR3wA7McRm57JOIs16Yez_0bc6d6pWAczrCxuvXCG1ts5JyAEKYdoGX_YjqQtm6n7FXJzB4U6KwHIVnbhUsdfBGB-TUEVW_A7LkVzJW2wnsT483hzp2XDi5n_b6f1DdMg0LOheBuZae2ZZbPQQwrx0mfUaiVhR1-s_eoV93K7WcsNN0S5Ag_7Libs2AlP_h8s_v-2OdDCBUQGSlULgedlhgqXc-gb-oPnTCB-qaNqQK37crJaoCNPFP6vKmKeoa2JX8-TqdTAxhSgT36i2TolUOBeGxBL-SM4HTRmfSfnURriqnJrl-d9sYtwSm1jxfV0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکردخیر‌ه‌کننده و درخشان جودبلینگهام ستاره 23 ساله انگلیس در سه بازی اخیرش برای این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/31041" target="_blank">📅 20:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31039">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7381a71b01.mp4?token=MDPVXkSNrsHDv3DYnatRvglJKh19EKephdZjbCKRwLQ4j3CWJhW-ejg_-iGwkJeV2SHHO6ETZOdFD9xMXCHPaxXO7DxwLNpKjnE5bzkKAXz7auC5Q56e577AoGFhyCzzRcyVPD_kX6PLvdxDFo746ZF8hhVKxgOF-Na-rnfePHUlOwBDZUxXB1J_qegrs0n3UJut9eaRz8lOhL5fku0ya3li2YMJVm-nprBkAcbqqZED5BOBFMx3QZ7hdeSD5DAslIde8-53PcRycTBrdsEsOkVBQjtkhvjMPRt74KFnxluhkXPi1tzw0EcbIG5KqSb0AYndo77QF3W4ksTOJnZy7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7381a71b01.mp4?token=MDPVXkSNrsHDv3DYnatRvglJKh19EKephdZjbCKRwLQ4j3CWJhW-ejg_-iGwkJeV2SHHO6ETZOdFD9xMXCHPaxXO7DxwLNpKjnE5bzkKAXz7auC5Q56e577AoGFhyCzzRcyVPD_kX6PLvdxDFo746ZF8hhVKxgOF-Na-rnfePHUlOwBDZUxXB1J_qegrs0n3UJut9eaRz8lOhL5fku0ya3li2YMJVm-nprBkAcbqqZED5BOBFMx3QZ7hdeSD5DAslIde8-53PcRycTBrdsEsOkVBQjtkhvjMPRt74KFnxluhkXPi1tzw0EcbIG5KqSb0AYndo77QF3W4ksTOJnZy7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیو کامل قسمت دوم فان فصل جدید با امیر مهدی ژوله؛ عالی بود. از دست ندید و حتما ببینید.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/31039" target="_blank">📅 20:24 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31038">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qN0LR9wS1XarA5ySb4Hd9_ww5E-IUlWEZUmUSvsmvDgyWgaGNp3Kv5TmPI7vq7m2tYGPGVWNGJt6iEATtDIN-6IL7V3-RQtpuc6H1YLvkiNBM7CTjkztvT-c1D6F4KIJeFqvXngF4BthvIBaXm34Oam7Ds-1aqTx8HpajxEkV7edS5p4w9f-FiHJ0f53B8N0sjMvarhA2wb31YvE3n3_1Bk1ItlGwSLZF6szGaRbCioiV-6VF32QkybZVKPkJZ-Vj3-iHYT51q5-2xPkTrtcmo6UKaW6axLWyHUqn4b4P7Wge9WrUjtVrbppq-kXfDG5d3bNIat036Ot8rFzdLO-LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇪🇸
🇧🇷
#تکمیلی؛ با تاییدیه کادرپزشکی باشگاه بارسلونا؛ مصدومیت جزئی رافینیا دیاز برطرف شده و او مشکلی برای همراهی آبی اناری‌ها در بازی مقابل ختافه در هفته هشتم رقابتای لالیگا نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/31038" target="_blank">📅 19:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31037">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWIWN1eMZQP-pEga8qpCe---3SFFkwmD8TlGgFPuu0meGpaZwtk4cwLjoQuJtZ5ie5isrLcdtzzFahkQXXaFEQNJUlGSfQ3jZbhtWBHZTQIwfAHtKMu3WHh2EzJVXqFB_bt3cG54yB45ctVZFeC8JwbBimLRsom3eXv6IOQu09bjP3GclyePbmkozaMQhQ4z5-WJWxc_hyOto68S12PzK8QgBqUMg2FosPm67jfsQYCfEqBcW3vAcJA-4jngyfQIuRDJ_1nrY1tB2IlkYQl1ahFh2e3nXjgIQqcgsKmc0Fva6E7jUaAm3TevTqjUuz2e72MHuoQkliMI84j5KQW9SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
مهدی طارمی مهاجم 34 ساله تیم الوصل در اقدامی خیر خواهانه 8 زندانی در تهران رو آزاد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/31037" target="_blank">📅 19:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31035">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfbtpGOIjBIMrpYG24GKkuS7q9fiOYuq_Uby1MNRu6AFjO6FFpn09O7xhTVFU_v0B37ZCb9DrNjpJMGK6XlNx7jJCslr3PrE4OK0KAXDYcYEp-SQU2MIA-zp2Otfx48jb9439TRUfyRec0hAW0dGLJixg4YjgU4Ah41UISghoh-N7wQaU3GA1P9peftHsUv-h46o9CkLk5qx6FxJAYbFcExm9UAPOxh80qlmsH2VuDLc_WRVKm1Mlbp0FfK-wmYrpnwmItfRLEiaS7qhHzwe71Amctonkl9mfyGDXvPrxOOxgS3R3hYwNYOboIPJ-JWTDrRNZGJO-QHGG7yst_RGTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
صحبت‌های‌جالب ساغر مرادی و فاطمه از هدایت یک میلیاردی سردار آزمون: این کادو برای ما خیلی با ارزشه. سردار همیشه به بانوان نگاه ویژه‌ای دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/31035" target="_blank">📅 19:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31034">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAy11nLgy8osEyi07Sa2d8geKqQA4scWmj67Pnkx6CLmLdwqB3u1tfZ-GPLVJ_SyCv-R_gAQaJWQHq2d3VlQyKyk9M3SetBN8YG76rNAV1MpxP-0eAh1HZPaSrCumwOL1IQgVHmHDN_BHXMELttz1auIiFJCrC2Ui5DHCRIm0geBd6oef79cC8HbOJTyuqjfZYKVscdNhCpXxmhreQvpbiOWzCeXXZelNbATZviuTa-Ow3p7TGkR_NeqGmOc8Tk7-Gp9yhCBWL4oCGDJGYQxQ4js3O83drF3RZpxME3hq0v4JgWXe6xqzWN6eLy5irDu_AOV6kGat-zLBL6n-RnraA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خوزلو مهاجم36ساله‌اسپانیایی سابق رئال مادرید و الغرافه باعقدقراردادی یک ساله به السیلیه پیوست. خوزه‌لو پارسال با الغرافه به قلعه حسن خان اومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/31034" target="_blank">📅 18:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31033">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOHQDv97l6UUmj_yPqP20HEOsIlx731dhBjtwEre0tM2_15GGn9kb2Vqsl9MfU3jqSjQ_aKM4l05GKp-kp3WgkJBicZo0jrjPAOjoQLEoO1sPriWi0r9uE8bxE0JYkgCaCSgSljdzmVhoCj_K17D3lF3x7ha--SUwPOlxGOJ5pwSUzGGoVAFvv_Dp4D2XLorBtvt6Kw8SKJn1c9wlCDLK1JZTPfzQGtqMRwsCjjJBjkK1tYi-aJePsdknXbBbVHWDz47xTbBPWtXmyj0omRPM99NZLXQwsYzxvnjLu_d49cjVKEsxVSYvIkJ0dGPXe1GE0aQAm6Q9MjVV7zqkpSDYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇧🇷
تیم‌ملی برزیل در سومین بازی دوستانه خود درفیفادی ساعتی قبل بانتیجه‌پرگل چهار بر صفر هند رو شکست داد. یه‌زمانی‌همه میگفتن که هند هم مگه فوتبال داره اما حالا فوق ستاره‌ها دنیا این تیم رو در فیفادی انتخاب میکنند. اینور هم حتی تیم گینه بی صحاب هم حاضر نیست…</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/31033" target="_blank">📅 18:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31032">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_cFKuF7hUYKOEjrBaN9AlaScjqjVDTVuYE5yhxXAhyiEEHEelPg3ARZOyn5kPThrPYy8_rAwyGTeFt3EY_L3vgUKxevbs7l6k_E3GUQzrbmuVuf_vYnROdGeouYXPkuOmSE0ZZJQ6G6FmylArus0kXtgAS36qZwHJRPCLTtytrg_diQSJEIimdInLwIQil0rKwaNuSpP5p0FW-GRsUV7ZwnKKfdOx8UzSEDUW35r48qWyuRgUXU8MoiP_gz5b3_ln_Nqr9S49wZOjxSk4H0uH3-cQuYfTEME7wRGiVGcZRw9Gukb-4HpnUAea_6qkcHcdlvf-S-Xvea23jQv5zwzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خوزلو مهاجم36ساله‌اسپانیایی سابق رئال مادرید و الغرافه باعقدقراردادی یک ساله به السیلیه پیوست. خوزه‌لو پارسال با الغرافه به قلعه حسن خان اومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/31032" target="_blank">📅 18:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31031">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKqD3cGpe91MWxObi40y2m81OMrKZGxc0wKftiqgFnrN002I8g3U78wpq8cuJK64pWiqd9xQpUDBtaonIc2LwlIw47ZxywbQvB5I2dPnly3o-qzq7ReJkvuonkEWKhh3CbNz10Mot3Zb5yl0Fu54ZBB3PQtmyomgUtq6B2sQMhQU3IlY-txh2_V32gZ1BwpFzrcr5pz8AhN9dh5aTSzihxyheVzoNH9-Cz9Sy5StDjSycyeNyXxvzluxhCEWMGYqi0-FboC3mkhwpxad9Lbg6oFMpndj3Ab0LCfSyRjLvcxLL9vp8VqChzUNa8o2zlHvP0KnDeHw93HGNJhaecVy_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گزارش ESPN از ایده جدید AFC برای جذاب شدن بازیای ملی:
کنفدراسیون فوتبال آسیا بزودی با الگوبرداری‌از اروپالیگ‌ملت‌های آسیا AFC Nations League رو راه‌اندازی می‌کنه. 8 تیم برتر سطح اول مسابقات به مرحله حذفی صعود می‌کنن و مرحله یک چهارم نهایی‌رفت‌وبرگشت‌برگزارمیشه و نیمه نهایی و فینالم بصورت متمرکز و تک بازی داخل یه کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/31031" target="_blank">📅 17:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31030">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uV67qHs0k1e_NAiXoB9G8GYJrbschP2B4zpJSUZ5H7p7eb6V5ukOvtT_tlyAsrrnuvZSFww9-KQbwKUc5gOS4VuYK6EIYYtQLGe6Wr5cKaDqF8sVlaDL0xVEcsOfqbxrs0geGqnfboxeofe_wl5nb2JrAnQS_CTBnRw-onY1ML-RtbG331aollViHxqplt2uIjD4LZ7IMGPqscMxF6bHD0_q6Hq4IxScgUf9bhJKlWccN6ugVCuW4LZwxwUNUi_54imdzaaFuQIfEfBXgRhahSxBnFztqTulY07f5RHcmAhmyS2LdXpQoY54zHlONdT1zPa0Cp3xQDSToKZgQWirJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
کلودیا پینا ستاره 25 تیم بانوان بارسا در بازی شب گذشته مقابل رئال مادرید موفق به ثبت پوکر شد اما فوتموب باز هم راضی نشد نمره 10 از 10 به‌این‌ستاره آبی اناری‌ها بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/31030" target="_blank">📅 17:48 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31029">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c89mrVCLr0Hc6_AfLY5qVSOPDu86w7C6401NWA1tUp36tR0psHaJy-cCFvVU26aicxM4s5CEEfsiMY9Vhox6WE2rxjjPyYWG9Xq034rWhq-Db_oEs4el7p_utXMIMZvgLH9Us25mldwVXmB-DzAGldTf6GDAvAo8KKvqqeHdeI9H2uvudwqYYylwETEdg4KcKxoT9XDkIJc1c8EC5gBVm0-h69ak9ltbC6iOFyNEBWc6V1RvgEJuXFCRHnXR4GJTa1-OXWen3xA2oQhKdjqYyfAIMEFnAG-wosv8Bv6RX429YwUU6J6rwV2YuFSV_5y2NZNrZIH91II0VFVU2nkzfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
تیم ملی ژاپن امروز در سومین بازی دوستانه‌ اش در فیفادی؛ دو بر یک نیوزیلند رو شکست داد. ژاپن در 16 مسابقه آخر خود در تمام مسابقات تنها متحمل دو شکشت‌شده‌بود که یکی از آن‌ها مقابل تیم ملی برزیل در رقابت های جام جهانی 2026 آمریکا بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/31029" target="_blank">📅 17:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31028">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24cf5abb84.mp4?token=M6bgfKxrPzRsXo3bYG1CXGuxhBZfGOSfNxqpe1ubqxQ4e_oF6_tLy48nuCyqIrKTm4Kf2ShzILXen28K-yvuuu0dvwhf5T1tos27tjGf5DzLoIu86atnBUO_2XPCNiaOmppIMcVMXhbVAZnjNUxGFMRWI81jNKaG2K-k6RV7HahHTk6qx2RcghXfB7XjI6s9oGL30hmE8itKLtj6Vrnp0lbf5x5vR2fFgHfHN9z-IkLBNo1c8R_TmcD53QZW9rBhL7Crp9VPeIzF2R3g0u1OfDrFkdlP9nwOR8RHO7ZXjD6PVqlsGWmF0OJV4409W6GTxEo39O_NnZh3fKMDyj_m8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24cf5abb84.mp4?token=M6bgfKxrPzRsXo3bYG1CXGuxhBZfGOSfNxqpe1ubqxQ4e_oF6_tLy48nuCyqIrKTm4Kf2ShzILXen28K-yvuuu0dvwhf5T1tos27tjGf5DzLoIu86atnBUO_2XPCNiaOmppIMcVMXhbVAZnjNUxGFMRWI81jNKaG2K-k6RV7HahHTk6qx2RcghXfB7XjI6s9oGL30hmE8itKLtj6Vrnp0lbf5x5vR2fFgHfHN9z-IkLBNo1c8R_TmcD53QZW9rBhL7Crp9VPeIzF2R3g0u1OfDrFkdlP9nwOR8RHO7ZXjD6PVqlsGWmF0OJV4409W6GTxEo39O_NnZh3fKMDyj_m8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ماجرای‌شجاع و حمال‌گفتنش به دانيال اسماعیلی‌ فر دربازی‌اخیر تراکتور؛ عادل: یه روز باید یه مصاحبه با شجاع بگیریم و قطعا اون روز دعوامون میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/31028" target="_blank">📅 17:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31027">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZyKca9p7jwxm9PfmeSrI1IwknD9tN8KgfSul75mHRrvK2Dfxhk5oElHHPpoF5-am5ipg-7LVnNvPJ9Nx1O9qq7TfCkoG2AgQ-qRIcS-CIBO-Ol22yNG1mBYiAddTxDydX-c2SVFr5soveXpO7s_Jgcky1ilVNLKuus2_ykdXVqap4fjQBRA_OFgd2xBb7HK9sGwOJ25CjdCtCNqT8bNA3gscQKexflxwKzyz5b29RwmfBTmJAFN7xMIrdfnWbeWhlfEUefS11vbtUnKTnOCDQ1OgVk9RzLURQTVhtPghCLt9T1r1reqJLBPKMfEOfnxfitGOSNvSvxBeS80WzYjZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
درهفته‌سوم‌لیگ‌ملت‌های اروپا؛ شاگردان توماس توخل درشب‌درخشش هری‌کین و جود بلینگهام آتش بازی به پا کردند و با گل کل یاران مودریچ رو بردند.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/31027" target="_blank">📅 16:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31026">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eadafe2e38.mp4?token=ilwrXbuZKa1Ob3O00zlJ_wACHXQnd7U9TBrlKZpOzsMWwErGixNlT0m6SDWzw5wydkyBfIpxd4618Ir8Xn5-K8i9GziGql9cs32xTR7_ua2wHO80_Pg903zFU-w66rXTrHJNmm4Ieq62xwEc3iwkXXpZRU7sOFvJxA7fFhs1Bw1ucChHHZZWM0Z7rVJDmC0nUKb1SrwGlBaFJ0Pu4eRZMh7YDDTI58VYIu-r0694MxhBC95Hk3XfmeqypMB77Gb_xLJJW02pyJTAHfLeh5NC8b9q5mmYfOM5LjEv9MpBBQgDNkWUA4sN15PWITslGprjsxrqLkTQC0OkA_XILZNaMBiuWuOxQRHL7ndmOCVBeaM2GVGAB-OeMHshap4awEV4NtRZG32ZIRyio-u9OwlMVdn3sanZMboz_DqKgU_4NMXou5NNTNNAX8xZ1WzVgMeIejLHlnmP-qPVoHnJlG3yLzzowvdw6UmOpBbJy--_ZVqf-gsGp1JEJZ073K7EHHVvWN-u5fnQZnLUFQixF4kK8XhUHuctWfZkbqDtOrajcwCtItZYFubDEJ0fZZgB2k7Bn47xPJ2zKOBLbvv62lqgGIdRSMjoIwLbCa4T-0JcBNyEhRpkZEaA9QxUzs4QDvpV2N28-j2zbjjzOS2Yq-kizYK_9F2jCqMIRdQm7BVWFAs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eadafe2e38.mp4?token=ilwrXbuZKa1Ob3O00zlJ_wACHXQnd7U9TBrlKZpOzsMWwErGixNlT0m6SDWzw5wydkyBfIpxd4618Ir8Xn5-K8i9GziGql9cs32xTR7_ua2wHO80_Pg903zFU-w66rXTrHJNmm4Ieq62xwEc3iwkXXpZRU7sOFvJxA7fFhs1Bw1ucChHHZZWM0Z7rVJDmC0nUKb1SrwGlBaFJ0Pu4eRZMh7YDDTI58VYIu-r0694MxhBC95Hk3XfmeqypMB77Gb_xLJJW02pyJTAHfLeh5NC8b9q5mmYfOM5LjEv9MpBBQgDNkWUA4sN15PWITslGprjsxrqLkTQC0OkA_XILZNaMBiuWuOxQRHL7ndmOCVBeaM2GVGAB-OeMHshap4awEV4NtRZG32ZIRyio-u9OwlMVdn3sanZMboz_DqKgU_4NMXou5NNTNNAX8xZ1WzVgMeIejLHlnmP-qPVoHnJlG3yLzzowvdw6UmOpBbJy--_ZVqf-gsGp1JEJZ073K7EHHVvWN-u5fnQZnLUFQixF4kK8XhUHuctWfZkbqDtOrajcwCtItZYFubDEJ0fZZgB2k7Bn47xPJ2zKOBLbvv62lqgGIdRSMjoIwLbCa4T-0JcBNyEhRpkZEaA9QxUzs4QDvpV2N28-j2zbjjzOS2Yq-kizYK_9F2jCqMIRdQm7BVWFAs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعداد سوپرگل پشم ریزون دومینیک سوبوسلای فوق‌ستاره‌مجارستانی لیورپول بااین پیراهن این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/31026" target="_blank">📅 16:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31025">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/476bc74d95.mp4?token=v_kFXaG6mK4mAzVw8VAEIbUqanvUOKuAj2OMf6kQiLcCobulPa2qq-dBN5cYOZjUlR5ZffN27bjLOeb14MElHZYkIGazmlaqmR8TtYZmsgUGLWXNB7un6Br2k2iDhcytTZ00Fqk27YG5L3d7xbymb2rkq_y1h2dhfVAgqDXrQ70CMeijDNLOpILbw2O9neviTqZLSk7I9tgrAAJe0FJEAskkCEUR4cWYMDf2VfWKPAFKZJoE4n3C7LaGSKcMqbt5dTtVONaGVo-VC5uheul3Bt2OnDpVCP--v4rtoa6wqVDrz5K42qZgy0z0HQBFE7rzDlRbnC13yKRdou_IspyOG09bsVEhgsa-xCNvmwUTlDQDCQO_DeOM4afcqGvWl7RzR43cpE1kux3qemqgnENzjG2VPxrykSuptuiVCTfDe7O0bSd25qJOyIvCg_bxWPUh57nKtmKPL0BrEEacjoxZSOzw_-4MbYHYQujrpHVuWVsaZN0_ceMW6hNQufXq7YMNMx0S1hxat0RvFncyGGbRXt43_nj5osk76c16sGLOot4KdKT8Fj94tHsg-rt1IUCZ4svKANs24reUUSktUBw2u4p4WmYUQ0kHNXIbkesVgcCNrs94hJ2HHzcdMXa5xlFu5vehe2mIXzfoLaxrKSqy0rXy8BtkMvSbY6MLWj1dtUI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/476bc74d95.mp4?token=v_kFXaG6mK4mAzVw8VAEIbUqanvUOKuAj2OMf6kQiLcCobulPa2qq-dBN5cYOZjUlR5ZffN27bjLOeb14MElHZYkIGazmlaqmR8TtYZmsgUGLWXNB7un6Br2k2iDhcytTZ00Fqk27YG5L3d7xbymb2rkq_y1h2dhfVAgqDXrQ70CMeijDNLOpILbw2O9neviTqZLSk7I9tgrAAJe0FJEAskkCEUR4cWYMDf2VfWKPAFKZJoE4n3C7LaGSKcMqbt5dTtVONaGVo-VC5uheul3Bt2OnDpVCP--v4rtoa6wqVDrz5K42qZgy0z0HQBFE7rzDlRbnC13yKRdou_IspyOG09bsVEhgsa-xCNvmwUTlDQDCQO_DeOM4afcqGvWl7RzR43cpE1kux3qemqgnENzjG2VPxrykSuptuiVCTfDe7O0bSd25qJOyIvCg_bxWPUh57nKtmKPL0BrEEacjoxZSOzw_-4MbYHYQujrpHVuWVsaZN0_ceMW6hNQufXq7YMNMx0S1hxat0RvFncyGGbRXt43_nj5osk76c16sGLOot4KdKT8Fj94tHsg-rt1IUCZ4svKANs24reUUSktUBw2u4p4WmYUQ0kHNXIbkesVgcCNrs94hJ2HHzcdMXa5xlFu5vehe2mIXzfoLaxrKSqy0rXy8BtkMvSbY6MLWj1dtUI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سردارآزمون به ساغرمرادی و فاطمه احمدی دو تکواندو کار ایرانب که در مسابقات بازی‌های آسیایی ناگویا به ترتیب مدال طلا و برنز کسب کردند، نفری یک‌میلیارد تومن هدیه نقدی با هزینه شخصی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/31025" target="_blank">📅 15:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31024">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6e4569c9e.mp4?token=GR6O92eIdqTKg9-vhob07tjgoieAXq-6fNks1DNT1Ya327jcmHFd85YxbqjBfmUslAs2nElh16RPRpt2cJ4C59sygRs6V5BjgC9E1NzhsB6aGMNlyV1TnUVZsMnI3UVcMMPSpCpbLunhIRlSuW_Y-4YhUKjdUb5x3MMj6eimNzdsAcWZL7CPOawcxnRjq1whBBiyVzFLdlVIryUq9NJ2rp7RuU21GN7kvGT5jw95NMZdcmsI9OT4kh8Me0GLcOuu5-h9pl3pSibJ1ykshFrdeJMW6tQT8WlnnjQhVoRJuMolXfFUx3c9uW5_XSWgTSYmzgsdXGYkB6kMoYY_s3xH-oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6e4569c9e.mp4?token=GR6O92eIdqTKg9-vhob07tjgoieAXq-6fNks1DNT1Ya327jcmHFd85YxbqjBfmUslAs2nElh16RPRpt2cJ4C59sygRs6V5BjgC9E1NzhsB6aGMNlyV1TnUVZsMnI3UVcMMPSpCpbLunhIRlSuW_Y-4YhUKjdUb5x3MMj6eimNzdsAcWZL7CPOawcxnRjq1whBBiyVzFLdlVIryUq9NJ2rp7RuU21GN7kvGT5jw95NMZdcmsI9OT4kh8Me0GLcOuu5-h9pl3pSibJ1ykshFrdeJMW6tQT8WlnnjQhVoRJuMolXfFUx3c9uW5_XSWgTSYmzgsdXGYkB6kMoYY_s3xH-oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صفحه رسمی جام ملت‌ های آسیا با ویدیویی از بازی ایران
🆚
ژاپن درجام ملت‌های آسیا نوشت: تنها 94 روز تا شروع رقابت‌های داغ جام ملت‌های آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/31024" target="_blank">📅 15:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31023">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0eqo96peL__f2OSNNzBiars-hic4NPe12m1NVLLSFL-cUkP0xprGNMmLKAc8VP96qaYMV_TZMqITuhG9QJ8YJAQ6wv-Bew0eQM8TB_Es_gEbY8ZGSK91wN-hDL6Tgfr9y5w6cpq7O85eIBgTgrMCwTTRswwd3sehg9XujqNsVxCon7HIhihxE9NPFJPiIVtLeW305-kUqegPVW-hogwyjnxN6gYuGbcTjt6d4OH7496-64XDU6Mi9pLvNx3dRTYbuLgfOZp6pGpi9H41d3Y-Z4QLwGoYQDBik0IsKlAC8uGUwoNluCLFcRM3Os_gMA1YQlMVvjwaNQPqJBB_bqoZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کمیته استیناف بعد از برسی کامل قرارداد یاسر آسانی با باشگاه استقلال؛ با انتشار بیانیه‌ ای شکایت سپاهان و مس شهربابک از ستاره آبی‌ها را رد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/31023" target="_blank">📅 15:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31022">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IW7Xan_-EwUCDOnaNLDdX3owtk7_pPNG-WiUCddsB9ONtJBDDqoA3oGSZmFJAa_p0Z7XOl9LqJpwHyrGeWsThn_QP0CTa0qMwNWpBGXHwOGCGnrdTnBqaCZ6pqmKYbxvX3wgqGaqIBOGJ46DTXrVe9xI0-xNuNPa6s2SJ_vwrL8GZSaxJM5HcJiWYBbDMWJMHLrGuwsCZVaV5yaA5zeXJOQ0_f1C2OETZeOlBYLqPQIoBIGYet0UQ6gxE9S3hrqdGz3liQC9pfajxcumUW9UHBZCHK6vuJqgcQop5ZcD9b2I0WGLXEED6gP1lEtt7z1yn34W19UR8WMRjctJpgbQOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛ خبر کوتاه است و دردناک: لیونل مسی آخرین بازی خودش رو با پیراهن آلبی سلسته از ساعت ۰۲:۳۰ روز بامداد چهارشنبه انجام میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/31022" target="_blank">📅 14:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31021">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLiI41AA7tXRgQh1z_dFSr9QliBGvk5U0-wm8xIzFd00lKhWxNovU9mFeNa0OId09_7GIVyrGYHuMJU9b7XFTcEoCTeOyZZDjqY_x-dyyRjItAj4HK5YcGgP6wFqFhihl_hxI1oq7dj7BxRL8c2LE1Y-iQLe6UQr58W0boR3tLmBf1W83WYkwxdmQn6km7Fii9IKP-j1whMrCnkngAK2sScH0T1udSnJtvAqc_i2wmHVn1jG_ieOiXra4GJ2OrzQBYli37e8JCRpRHTL-G_JELKlhQv9QVSSZxtcjtHPuthg5bZIZ2Z9F06jPxysIdhmj0jQJX_IMf0hJ5v9HQZC4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇦🇷
بیشترین تعداد گل زده برای دو تیم ملی آرژانتین
🆚
پرتغال در کل دوران حرفه‌ ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/31021" target="_blank">📅 13:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31019">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uDsA2uHF7_em6NxNPZ8-VhLFLhZpWkGV6q0yMAiPOiwkdYPEk_jdo5-zItaO6j8ml6FWa3guxGp3TwsdsNUFpnbndRlwLRHGjXEB6irpi64Oul7m3k8KcayDR_pqX1n_i3KiW18F0g_GTtzYKXQwd1QQJwUANyVzP-eAsCYPbKUC-Y7oVcuDJv73Lbo1dlCMYUrLL3uScQGaR0U2AF6gWqhf2mSl4gS9W5qoykdSriJDYNVe0rqpA4dfMG4yvVLl1u5eCBIJIjHEanP-gT8xwN-9ZXoRyAWDQX95bafP1ROkzIdgGpxYLd0gxrXIwDf2RrOMwJjB1DLxSWAdimufGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ObVhtvl0D5Vq32kTWoSgG-rYU7VTuk-Xmb7uMyBxAF8BNsMI6c0OOBXsR9QlOA3R9dI4SpfAl39N7HgjELyKZ87ggVdwzKIWZUel1zPzQRhlGl_QEvs-jI_MaPz7EF6qiu9Wb4WWWuEjoJjgWXYNvzMzoe-HWzGNVRaZr5FwDLwM8BdGTaL7PgXH57lhQn9xSTtW0l6zQF2oDMemgstrwAEe7cgJw3sljhW7mHfjlaa6wI0BnBFGtYShgN0rOSFf5rFZ2_Mu4fLwSxGev3idcC_E0UmQgYcj-12j3AzL4_-iSoBSqQGSD4a8pDEQnqz2ZNHrJNbErtgNFOhFClAg1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇦🇷
بیشترین تعداد گل زده برای دو تیم ملی آرژانتین
🆚
پرتغال در کل دوران حرفه‌ ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/31019" target="_blank">📅 13:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31018">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIa66O7ItjWB0eBdnNCq4wwm9ylWtPwPvPjxE2tgw3bO2Z8x66dAEPIPvfkFdkY8rgIiJZANOy9HbBG0LtlQDfYghz5SOQ-yzthWTrtXIC04lBqvuF8v65OXbSJN1a7UoUh6GXZYbkrE3DcYQuWlwttgI-byYNXZIlSZyf90II4jgaSiSMNJKgCB2H8rD-NW_kbhvNot8MVMON-HWBBcFWj884RkhQ7DXi0gPqdrXTezWuoDCGv-skqJN2Ruo2SgS_akEQsOorYR9IVbaoSciA8jFg1ud42WTtgVnEpFSVfV9hgcWOvM9L8vOFIivIrvZWL1J30X1yDvneRbsdIn5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خورخه ژسوس سرمربی‌تیم‌ملی‌پرتغال گفته چرا باید از کریس رونالدو عذر خواهی کنم؟ نه نیازی به عذر خواهی از او نیست!!! پس بشین تا برگرده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/31018" target="_blank">📅 13:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31017">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/034d1249e3.mp4?token=EeZG-LHiF2LPx-plGpVbwKHoNUW49ZRFtAN5wsyBGuyth8pCgLlCOWMVNQKHp25pPx5Ac7gCeMm0aZcx7unGhVt53XDUgnxF0gcsH1RBazElmJdJ0tNUTMCBW3j9cZDYnFCwmEuPolcZX1vpgwqJmnuirnLB3s4XzB0XVjKqCmsRBuI89ZpIKQEmmi7HSSx-nOaANk6Fuw9ts7xg7df90ZozSo_UsvvejWXwfw21ZZ-0NF9RTJebROHx_1peSCYE2cn9bfvdWPWB3PcQ2JqIEy6HS-lGjx5oXslBYGYtbDPCZ2x_l9JZEpXhA7CPZKQE_Av8lGSeIHTRuF9w0-Illg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/034d1249e3.mp4?token=EeZG-LHiF2LPx-plGpVbwKHoNUW49ZRFtAN5wsyBGuyth8pCgLlCOWMVNQKHp25pPx5Ac7gCeMm0aZcx7unGhVt53XDUgnxF0gcsH1RBazElmJdJ0tNUTMCBW3j9cZDYnFCwmEuPolcZX1vpgwqJmnuirnLB3s4XzB0XVjKqCmsRBuI89ZpIKQEmmi7HSSx-nOaANk6Fuw9ts7xg7df90ZozSo_UsvvejWXwfw21ZZ-0NF9RTJebROHx_1peSCYE2cn9bfvdWPWB3PcQ2JqIEy6HS-lGjx5oXslBYGYtbDPCZ2x_l9JZEpXhA7CPZKQE_Av8lGSeIHTRuF9w0-Illg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
چراغ سبز سرمربی تیم‌پرتغال برای بازگشت کریس رونالدو؛ خورخه‌ژسوس: پرتغال همیشه خونه کریستیانو رونالدو بوده و هست ولی‌اون خودش باید تصمیم نهایی رو بگیره. من هیییچ مشکلی با بازگشت او به تیم ملی ندارم. یه سوتفاهم پیش اومده بود که برطرف شد. همه ما منتظر بازگشت…</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/31017" target="_blank">📅 13:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31015">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p_-HG4o67nX_14SjEoBj6JutfavxsGoFjfUYacapKPLjIf2a-Q4_-L11TNVE8UdfTLI9K76-imUvU_6_0QRFwvFKvFWQiJCg2JZE15aXLPRnZ9Xf5nkZE1Fwle8waCKQgWGuOhYkecEmUG_r7qftjpp_1qryro2PigLRzLJu_cA8hRUtOulylgmQDQWm0NMdWiW58b3DB8DM8BvLbLKPQ1kbXvG-H3w7vHGrFJ5ijy7OVpQFVbF6JRbhfbu-XT6eZAgiakRnTgajl3YqYrEzn2PyDQhDNo-sAPXfjpHz2cc5uydHLlw6fjLmf2gXzSN4XDf-KZC9meLaBwKz-uCXGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uBvOeBvHSq9uRC6q_HxBMiwZ0BCybmWNOnReVs43aPs-eScKQOT1C72Qi2e4tEP3etVbcqwlxm8rqAsVHxMHam3K3j9SVX5-qOEb6ypX-puyBII0wC1wHitbIweJp-dkeT9FE82-5XF_O-PV6F7j-jl62BqPGhpaBP3uMO0cYrw7iSprOx6d0chnKoS5KM44HR6igQ031gt5GPdiRujdG1PXaYCoEWVDlv-sugVGdSGwmimy8wep8iXKtIc14pXMa0fkxBg97WaztghKwXQTyP7PVGZbKarY11-bR0AP1jaRT7nWvVQIXLKQS1SfypFdA_BYU82rv34aWzetJOqWhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
#تکمیلی؛ هفت‌گل‌تیم‌بانوان‌بارسا به رئال مادرید در بازی شب گذشته؛ وضعیت دفاع رئال مادرید رو ببینید. قشنگ میزارند بازیکنان بارسا هر کاری که دوست دارند در محوطه جریمه انجام بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/31015" target="_blank">📅 11:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31014">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwIb-GQFV8_xUgOgTDbiHE4-6SGsngMVn4jvh6BxYmWiuo0OkvJbA6NALsd_h12t0JpiMeB_pfnvJw22TOxHhKcZBuMSaMwD3biQgo2lEq5ALfnIGW92ymOmsYMNT7b94Yl2Fi5eshKHKNNFPS4YpzEVqC3cRl8NM59_5kWd36AvsI8nfKaewJgbMl-_XnIiX2f9KiUf_XFDZrBBFYL9-HysDdvvQaf2pNfvySdiLcYGFsyB45g1ZXYALtF9geN9WqLNhDLAoEjtnI-24e9k7xWVbGcRB7a_w5_lATB6KJqZXu4XcgSn2_9z-VHDAqxqKRPkWMa8Swjv7Vr8iTDLvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تتلو آزاد میشه! پست‌جدیدصفحه یوتیوب تتلو: امروز دادستان و رئیس کل دادگستری با تتلو صحبت کردن. درصورت‌ارائه‌گزارش‌مثبت‌تتلو فرداآزاد میشه!
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/31014" target="_blank">📅 10:48 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31013">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1QYQvR_WBb4s9Tn5TItbQT10evVQHwJlmMInGCDXNrg08Smd880CPzAjCS2N5CyK83z9Hb7q9E6SyPq6ieiEfl-e6qVfykMLrL0-MdHHAy7pbbvuxXK0sj8m0bMmXrixKecJ_x1t150RG89aXsPbKY-Vs9_V3KXdruAA5G-SHO5ZTYVLPuG8gBqI6R3uoHhvcPMUE1fTUCTUAIZxdom4GyQmJID97xVkLGwr_5wm_yMAgy6eSPIY8CWCc-gvuiM7F2BdaIdBkKDX1IeG3UFbS6nyIut7IvPKSA8EqwgcAYe2qZZoH2Sv5RRlrKAAZ4XGfg5aT6IXrxfhPtiCAHmTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق جدیدترین اخبار دریافتی رسانه پرشیانا؛ کمیته استیناف فدراسیون فوتبال بعد از برسی کامل پرونده یاسر آسانی به درخواست باشگاه پرسپولیس مبنی بر غیر قانونی بازی کردن یاسر آسانی آلبانیایی برای استقلال پاسخ منفی داده است و بزودی سایت فدراسیون دربیانیه‌ای این…</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/31013" target="_blank">📅 10:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31012">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGmhbZSezIPGK78jG2tw9Bj7ObtnKGlQxLBWDtRcn9aWXyi2KNfyvD-nU7qG9e7lXg1He5KmbT2_tq6DpkqSENz9LAyBZASgsLOK5AjxGHgFl8Cicd3SLfjrxy8-9hdO-MD0nIonXwEf9CkqIBBIpmVKiI-J_VIVcBnh6EdQ53VIjwfT6h6_-r0FgAUT2JT9klA5UxfVASSsXefvONTAJCmrzK3feM0mqlLJRMHHH6JeCZkDFqqNXFd6y3u3tBweUGPwZ2zW82XkYGr8EHGFFtZBswJJqAFqkGtMrEnawomsdpGcD0_M7QJRtFVk0ekOK24UkWoBn7bKc9Jz0Mst6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یاسر آسانی و نامزدش بعداز چهار سال از همدیگه جدا شدن! یاسر گفته بخاطر استقلال میخوام برگردم ایران که نامزدش‌همچون‌همسر منیر الحدادی مخالف برگشتش بوده و آسانی سر همین ازش جدا شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/31012" target="_blank">📅 09:51 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31011">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ska31mc17eWcvbTWJEYJ77hZH5mimBY1mce_R4JWWGO762tVwumpDr2iClILtn4Scqiauo91-69_5hlcunKhvMgeQE2AebJiJSW7joYSXbXve4u05Y9iIaehzmxD2R3oBywCpCuRoOr3isBKJbnlpFuqec3VnMoRVivuqOSMBrmxyYWOYNZEXP77VD_CSdU7-Y18EhlEaz95FPIhcTM3RualCHnYorZQGF2fvCdgoWMpxDy9tCSatPTYcNjKnSO6PksMmelZZ5JLP7W4nty8EwzlokvtsEw19gSIQzVrvof87Ysi8t6BRrsaezUIIfW-tTijrxxbOPCjFkT80hLGgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزنامه آاس:
بعد از فیفادی رئال مادرید قراره از وینیسیوس‌جونیورتستDNA بگیره و نتیجه‌ش رو با هوادارا به اشتراک بذاره تا بشایعات و تئوری‌هایی که توی شبکه‌های اجتماعی مطرح شده پایان بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/31011" target="_blank">📅 09:47 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31010">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2e1347c85.mp4?token=iYzDyun-n3mcct3XPaeH4JaSmnnL5aC43BiOlSiDGkhZ8_B5Zc2hlqNMOIdqAoOL6HmMUfJ-fMJdiyuWCqy0045Gcynz9BXILvALDTJPshdkYNFq7S6dP6oXNs1IUSKOeAS5BUp7G8rFo9Yyu1i91pI-f_Yzvac3m6liqecIIfkseTgWFJMOODITrtIcdQmcR4cyjHkecyEkUNf6wCUHQ6NkWAZzIVVWKneTv7dsPpJ_9N1I_Zg_fktDXprkp6KLplzPROFYDalEsjvPSmGnjs-nzvLYxKORNCMRTuSFyYQuU0Ib7bpjYZObrSHKWwjAoVXNBY06gGl07vBYhVbNuIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2e1347c85.mp4?token=iYzDyun-n3mcct3XPaeH4JaSmnnL5aC43BiOlSiDGkhZ8_B5Zc2hlqNMOIdqAoOL6HmMUfJ-fMJdiyuWCqy0045Gcynz9BXILvALDTJPshdkYNFq7S6dP6oXNs1IUSKOeAS5BUp7G8rFo9Yyu1i91pI-f_Yzvac3m6liqecIIfkseTgWFJMOODITrtIcdQmcR4cyjHkecyEkUNf6wCUHQ6NkWAZzIVVWKneTv7dsPpJ_9N1I_Zg_fktDXprkp6KLplzPROFYDalEsjvPSmGnjs-nzvLYxKORNCMRTuSFyYQuU0Ib7bpjYZObrSHKWwjAoVXNBY06gGl07vBYhVbNuIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
تیم بانوان بارسا در هفته ششم لالیگا؛ با هفت‌گل رئال‌مادرید رو درهم کوبید و با شش پیروزی پیاپی در صدر جدول رقابت‌ها قرار گرفت. تیم رئال مادرید هم با 13 امتیاز در رتبه سوم قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/31010" target="_blank">📅 09:47 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31008">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfuHcCO7L99XcM8TIfjBGIacA8UzQH5IpD5EVpBWcEHh9ciSHvuN0wU1rokZGCMV00Na6bp6DoVYWQeqViMzdCb6OKMIX-lflHrf07q8NuDqQpOO3UCIxJGk0ngiOml0B2hvEkQIsn9ThyvAewLToOd73WhaMHABzHH_xxbHHI4a_8lTohWWnfXVatte-2AftPcmgqJRptb0WKU1bjfZzMnhzmvd2tU6fOZsC-f5K5r2wIt2p88MWu_YaXABu41um6jdwmQ2T193la8ZI_InRuhtYsG7mrVvs45sYMR75Q8RqkopTCwa55R3CsA1gmqdrhRk5APz1jnw_UiPzJY3NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتایج‌دیدارهای‌امشب لیگ‌ملت‌های‌اروپا؛ لاله‌های نارنجی تحت‌هدایت ژاوی هرناندر صربستان رو بردند؛ ژرمن‌ها متوقف شدند. یونان همچنان نمیبازد. پرتغالم با درخشش راموس دو بر یک نروژ رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/31008" target="_blank">📅 09:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31007">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYfxsHYJW6R1F1jVmcxMDVeSb6-g_8a_YCz_XjclUEVaKHg_nHmAb7xUgTNu1b98be3UnEToiC-woW3K_7iVQpVnCdqT1Ohk3YRBO9xbHcnRI9K3e7r6g1-qUHFh-qLoheD98j_1j9CRSY2V8R1diqXjHRg19Pq_POwMjdWu3WwhhKB0UAqWBdWLBCbYX0DkeI2IFuc4_w3XBHa_EPJLFfcuM-_sc9yv0Mn_NzjEtKFfKo_RCHZZ5SjgFylSYk8k_xHo5n6BZd_0oUHt8skYXp1LnPAUV0DVUdWKD2zl9Dp2n1EN9kMteduD_9BeJLqIzuese3ndnvefUItB9Y8ysQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از نگاه بیشتر بنگاه‌های شرط‌بندی؛ لامین یامال فوق‌ستاره‌اسپانیایی بارسلونا بالاتر از هری کین و لئو مسی بیشترین شانس گرفتن توپ طلا رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/31007" target="_blank">📅 09:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31006">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d013eebfa.mp4?token=g-YdBHUnon7IFgUQN8LRDCJQoCSkDBMitvJivXLhnV3gtGreT3ExnWwkjY5fmMiPy5tNh_pnTp2G699Tgy0RD3JSt-4xRRkio3eEL9DePbB1p-UsmPcMJzz-k2Fb4zUM-kg-1CvNwdgsdAHLmDGHFrnCjBhpN3EwPCX6-kEG8u0ijAkD_bRMW5AtzgiRjFsS5URqNEb7Ec8MfUckGu6cdi2ExzY24BaWzvZN9r4gxU_aqqtiY5vyekBnLygn66V-jiOI_F1_2UYW6fL18kXiUiIUSseEVuC3o6JiEjOZ6P3wo_eqWHrk-z7moeH5QdaXef-Pi7s2aIYeGkmE7RYl5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d013eebfa.mp4?token=g-YdBHUnon7IFgUQN8LRDCJQoCSkDBMitvJivXLhnV3gtGreT3ExnWwkjY5fmMiPy5tNh_pnTp2G699Tgy0RD3JSt-4xRRkio3eEL9DePbB1p-UsmPcMJzz-k2Fb4zUM-kg-1CvNwdgsdAHLmDGHFrnCjBhpN3EwPCX6-kEG8u0ijAkD_bRMW5AtzgiRjFsS5URqNEb7Ec8MfUckGu6cdi2ExzY24BaWzvZN9r4gxU_aqqtiY5vyekBnLygn66V-jiOI_F1_2UYW6fL18kXiUiIUSseEVuC3o6JiEjOZ6P3wo_eqWHrk-z7moeH5QdaXef-Pi7s2aIYeGkmE7RYl5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
لئو مسی اسطوره‌آرژانتینی تاریخ برای انجام آخرین بازی خود با پیراهن تیم ملی کشورش دقایقی قبل به اردوی تیم ملی فوتبال آرژانتین اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/31006" target="_blank">📅 08:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31004">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sm87tq2kLEIo9ZAjWNZc5xtePOXhfX1lbHzHaLVtnEea4WFXiij04fs9uGeSK-jAR1oLzDvGgqsFR8-JR9w-x6v8EcarMeqiQOONqcH02AnCtnHpNLjeL70kr0N1xgTNMAl6ofr-uMqeUS2pwxyRwoQtZBQAm2oYFx-Op_sEZVxA_T_QmuhnBlTyGr4z5p3Y4OAuQbDfRBdhOtIPYII9fxnZ14_BPSWi4GFw6QMZ4-r86hmBvUmXEYfB0iD1WiurJ0hoOCI4P5sFzYsqdGKS7SUwIlQQjUR4iDuwRII3vfm8vpiUwU3Y45fA4YgYY8J8yUWt2nsg4Ke273u4u3fA6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدار ها‌ی‌‌‌‌‌‌‌‌ امروز
؛ مصاف خانگی شاگردان زیدان بابلژیکی‌ها و نبرد آتزوری برابر سرخ‌های ترکیه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/31004" target="_blank">📅 01:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31003">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MU9GyCCh0cxTTZ5btMzfcLCO-JOSDy0nmXkai_1ErwbLhgCLoTCw9LaKav2V6_T1vjKbHED8VNqdRsCcUiKuyJTJbCJBxq4Pjom0zfCQfSXlIuvCDfSrGCXvUI_xpIKqdn_ENnvUCc5S5FqSK8593BP0BYu54DTSAy2KfdoavSgmPeVCZBVGBMXtrmJsvjNd38Q-lEV1bQdZxzvvS7HTG-s7sLAMBsbkuWHMbBrdB1HbIczyVNSmh_6SoyYx5jyfktFZK3TRUQE8NH5cJb_eLhvtELnTfRwcdTlYrwggo27gaNcAgSqTrvYTGmBw-7H_QVviIMUcG93tm4j6hKGiQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدار های‌‌‌ دیروز؛
چهار برد از 4 بازی برای شاگردان ژسوس و تساوی بدون گل ژرمن‌ها در یونان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/31003" target="_blank">📅 01:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31001">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdRAeAdb3Nt1RpEJxohTElvGIi-A0jgVhMGiLFwxEj1ktx_SWc03L9m-all8-K508CBMSZEmncOoUk2BGK_VaJwj6Jqp2VVnshYTISH24zgXJu9MaA7iL5l6FElCRkFgvrzyk10d9AHZ9r2WKsPAQKye6rlXmOe6mJCCYKjfVYqu2jM5TK-RATToOwjGFIwjVjDS7ywTHf78UtJgU5aSgaPcmVv4e2L_0HPrj-rDrH_EIaVVMRhkRuEeHmvTOoLmuWDetbjsYTj266eUjrEPuwMlGrahaLC4A7w2EJFpowKVOsnd3Rio1LlLTRN5ZrcCOs-hGhM6s5m2_xhBD_yu2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
فابریزیو رومانو: تکلیف‌کریس رونالدو امشب مشخص میشه. رونالدو توقع داره که بعدِ بازی امشب پرتغال با نروژ در لیگ ملت‌های اروپا؛ خورخه ژسوس سرمربی پرتغال درباره برخورد زشتی که با او داشته توضیحاتی‌بده و احتمال‌بازگشت CR7 به تیم پرتغال در صورت دلجویی سرمربی…</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/31001" target="_blank">📅 01:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31000">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGsizVNiT1uZbPGMo9x0QXWBE1QTBnXEkNgDII5aynMj0VCs-frvS6BE4JSAO1z7F_PwwcwqJIaBGGiHu7AljKr8TQ6D-EddV26L-B-glHAWO6XP6hjiXOV2NUYlWRqN81j-jqsSDLTBZUXXbBNX1D55h_0jrWEU1K0DtGt2dYFystjyr4ez9GZM-B64xSFokOaVoRO1ND1j3NuGSa66mf-HzipjJQWFpafTysxsxdJELpQo-OdA-hwvIJCNORsv0m2Ky8micX4qHwXcbz6AJe-Yn8zejfFx6z5gk9g6LpPIMN_KC_bcWKRMGstgjSUDQg4wiXP1uaB3OSMqtr21AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛دولت‌آرژانتین دراقدامی قابل توجه روز 14 مهر رو دراین‌کشور تعطیل رسمی اعلام کرده تاهمه‌ بتونن‌ آخرین بازی لئو مسی با پیراهن آرژانتین رو ببینند. حالا اینجا یادی‌کنیم از پاس گل تاریخی او درجام‌جهانی‌که هشت بازیکن انگلیس محو کرد. پاس جوری بود که انگار…</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/31000" target="_blank">📅 00:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30999">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇵🇹
چهار مسابقه چهار پیروزی؛ تیم ملی پرتغال به عنوان اولین تیم رقابت‌ها به مرحله یک‌چهارم نهایی مسابقات جام ملت‌های اروپا 2026 صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30999" target="_blank">📅 00:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30998">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwU7NYvQCwpW9xyol0dVDqO9fD8X8BcixQSgxH1DJyoazkM0lIGLrEEr3q7uV645THN8YZuPwlU_S4ZGsAjXa1DHmX-M-NLKablA9pNJNbuCUFywtyaJ_CQ2-AJuFUrItflzcEpSKo3DxP8_VSp-pkx2Oms0H7iRgOvdL16-_A3PfiTKdZASPxhbB41_gy7XJ5nCh4z2nOb4iQBLiAKtxXlTt0heMNq4xEK35QsZBEJHVL7Gs8l43Kq8y_meigBInL5RtWV7JX4tMkLVVAKbTHo3o3cD9m40v0myH_1fh0KWZXTnnEG2i2v-8aRBfxtko53EVTuRjblqRh7Ip-KdMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتایج‌دیدارهای‌امشب لیگ‌ملت‌های‌اروپا؛ لاله‌های نارنجی تحت‌هدایت ژاوی هرناندر صربستان رو بردند؛ ژرمن‌ها متوقف شدند. یونان همچنان نمیبازد. پرتغالم با درخشش راموس دو بر یک نروژ رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30998" target="_blank">📅 00:18 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30997">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGPcn1UFeGsX7Ibo5jxrZCTWH9X0EdGDeBqJIwIJt1oT_1yBkXGZa6Ven4YIMorGfK9jdg5wBHeeRQEA4pM0i3iaCqOivoHoVvGO5qcIY5EFaZFPw32lgKvADx0yvltkiMR1a3CIozSBEIDvK64Yul-9nV7mp79qlj_WZDpJHCaqVhzBZ48Nyx_b3NRxTsBEf6kWDjNcUsOtEOmzxlwFZFAx2TgOX6kWYKRLbz_e_CyQMByCY-xv3_TCikYr_g1gdHVRDPvVhb8GmmVTKNrAMYaJmOP3SuTkKkittLJyvjKa2j7zGhcqzqTElaD8gPgXX3tc1R4DG2S2eP0Rkbs0Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌امروز؛ هفته چهارم لیگ ملت‌های اروپا باتقابل‌مجدد پرتغال vs نروژ در غیاب رونالدو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30997" target="_blank">📅 00:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30996">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rywvI3x3DyBxdyQnSyTLNVFy6WxL2zt1l6NK9u990Ka05xsmRfzXah_iVMLSEiVYVTrZliSzm6XZ5w83GZvwChUVzq05ojAjv1uOvYjxkeHHjMgh0hMvv_f1NNVswvFVf_-obT6FBtQtShpvj99oMnzZQxmXgTOyQb2v5V9c11lbkBuMWceO8aFvCpBkxvivcpdIw5xe-DEtYxw26WVHEBe9lBfj3udw3eJROy1FePk2kbBHPm3HkLz2t5crzSTLkxS4lY1xBBtfluTDaA_qr-2Y1hio53w5p-GVouZxhRj6-oV1Ec2lmLvyNmKuTfPiLVuCTTicUcU7xg6vOu_8PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
فابریزیو رومانو: تکلیف‌کریس رونالدو امشب مشخص میشه. رونالدو توقع داره که بعدِ بازی امشب پرتغال با نروژ در لیگ ملت‌های اروپا؛ خورخه ژسوس سرمربی پرتغال درباره برخورد زشتی که با او داشته توضیحاتی‌بده و احتمال‌بازگشت CR7 به تیم پرتغال در صورت دلجویی سرمربی…</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/30996" target="_blank">📅 23:47 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30994">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9256e00306.mp4?token=iUF0uw2mPhwl2u00HyqKWkG9jRgfO5jrk3x2TAgHXYrV5chj-7o517mThk7ycd613qWwUn3z0-ZQXJFEIMzlFsf66-Kk7J7xCxYvXWETsSXsax17vnqzuIoWQfEUMAHEBum7rrsYAniS7z_8vDwNloBAFMqbMMfgJ_hnFD1oYioI02zAMztL1NykiYUX6BLloZPtxd7HRPSzPJ5Sl3RaB8H9iuQf6ke5pagQHCHiqvhqXWQ_bRBXudubBH5yl1X2rV9GsbJa_hPjmYP5RD8COLAmCi-Dte-pQ__M5QuGBhSkVJOlNrH_iocrWcleDffX0GYDdx0JlxxI-SZ4U31wBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9256e00306.mp4?token=iUF0uw2mPhwl2u00HyqKWkG9jRgfO5jrk3x2TAgHXYrV5chj-7o517mThk7ycd613qWwUn3z0-ZQXJFEIMzlFsf66-Kk7J7xCxYvXWETsSXsax17vnqzuIoWQfEUMAHEBum7rrsYAniS7z_8vDwNloBAFMqbMMfgJ_hnFD1oYioI02zAMztL1NykiYUX6BLloZPtxd7HRPSzPJ5Sl3RaB8H9iuQf6ke5pagQHCHiqvhqXWQ_bRBXudubBH5yl1X2rV9GsbJa_hPjmYP5RD8COLAmCi-Dte-pQ__M5QuGBhSkVJOlNrH_iocrWcleDffX0GYDdx0JlxxI-SZ4U31wBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شکیرا همسرسابق‌جرارد پیکه: برای‌اولین باره که این‌موضوع‌روبیان‌میکنم‌ وقتی‌از پیکه جدا شدم. یکی از هم تیمی‌های سابق او که اتفاقا رفیق صمیمی پیکه هم بود به من‌ گفت که بهت‌علاقمندم و در این سال‌ها علاقه‌ام روپنهان‌کردم و الان بسیار خوشحالم که جدا شدی. یه لحظه…</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/30994" target="_blank">📅 23:21 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30993">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPgRDTcUDO07_xoFfqS1c6gHdn0uo-_3RRFA6lD_VkrhIzIniYI31U7IF2rfuon4xoNJteXgWXvZnuWEXTFw7LX78E-LA0CLBe-64U4FLYLDMoThacX3wh8CJ3eGsuPHbMDSyRbhIbVHdslkeLlDQla7FRFq1_TmtgFgZeW7GhKdJfSHmhTmvOqVrMkb2qNEL4Ay9T2a5XrKpbCXYzOdBTkSqVBj1swKPBOIenkPUMT4DQDCp75hNImQrycYSiVMCh4dQoEByT1UPUV80eQyesDocYXPeYDKKU7NwEVu98KCHYUb_MxRgGwXRyilNh4fAHDJWMIns4ZCW_usvBDUow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇹🇷
باشگاه رئال مادرید برای تمدید قرارداد آردا گولر ستاره ترکیه‌ای‌خود تاسال2032 به توافق کامل رسیدند و فوق ستاره به زودی قرار دادش رو تمدید میکنه. پرز دستمزد آردا رو حسابی بالا برده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30993" target="_blank">📅 23:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30992">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f8925e4e.mp4?token=GDt7nfrkGG737rutb7GJ96-ITqCy2pDg44zKLhhGLSENhoQKctXfrIv2JbaMf1xXKGYHnZwMLiWTHs7h-KMecO6Uf3Wxwh6fGx5hHPA9kRqTFmUChbH9C1r6ukB7akvOODqTQLe3AMD1nLrXM6yM3cvgCVi3WSU0DeCdkvXJTD2wmxIvJWkmYUDepycmetRqWTmNHfcmIUvbLaBa2gDfAKnJYTSVX5WwlMrw00-v-ktqERB7pUXawV_sxw11mOON-ujTXOjVdJ4nlj5qv9Rgwh4_09kGEd1m8rbScGZKhYQ9Uf-bOLG5qniS5WNbcANptxyib6ZEEW5HvY4b-egXsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f8925e4e.mp4?token=GDt7nfrkGG737rutb7GJ96-ITqCy2pDg44zKLhhGLSENhoQKctXfrIv2JbaMf1xXKGYHnZwMLiWTHs7h-KMecO6Uf3Wxwh6fGx5hHPA9kRqTFmUChbH9C1r6ukB7akvOODqTQLe3AMD1nLrXM6yM3cvgCVi3WSU0DeCdkvXJTD2wmxIvJWkmYUDepycmetRqWTmNHfcmIUvbLaBa2gDfAKnJYTSVX5WwlMrw00-v-ktqERB7pUXawV_sxw11mOON-ujTXOjVdJ4nlj5qv9Rgwh4_09kGEd1m8rbScGZKhYQ9Uf-bOLG5qniS5WNbcANptxyib6ZEEW5HvY4b-egXsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
صحبت‌های پیمان حدادی مدیرعامل باشگاه پرسپولیس درباره شکایت از یاسر آسانی: مدارکی از ستاره‌آلبانیایی‌استقلال داریم که به کمیته انضباطی ندادیم و اون رو به دادگاه عالی ورزش داده ایم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/30992" target="_blank">📅 22:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30991">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9pT35KlNp1unRWU4QtZiQPJ_2jeqieA7N2zoQNrRRl4GiA4cUmFxC6tsGdJkX_nlFFE49iTFUbnshiaClCBLbV0VJH5DHynbNNQAc-gifgkEI-9tITSB2ZbDhunAY5pzcBQyl-SJprbs6XtHYUTTtjvnTRAHvDbIjCZYTkFom1s-Z9b0oVCuER5IpB1wg09cDcPWT72h3LsJbh70NaDIzY6xLE18ktQJqeKhN6OV8y9D3r2aaNuxp0riF9xm-9Fvn2WO0QSz2h8ahq0Q0_Qo701tGVNal1dA4ovxEmx41dig6mt97GVhMf2so6I_79iw_G_4zazESPMJVIufbc_1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
ادعای میگل پریرا خبرنگار پرتغالی: کریس رونالدو مصممه که هزارمین گل دوران بازی خود را با پیراهن تیم ملی پرتغال به ثمر برساند بنابراین احتمالا درسال2027 به میادین‌بازی‌های‌ملی بازخواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/30991" target="_blank">📅 22:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30990">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhqfgZjDjEQo6JZZnFYJOR5zFbrbTddUELXK1zPVbwNF6-Poc3Nu5Jb6kbC3DoWDntcGenuBSH-szFOqZuGlCIL7Wx58WSujKIDO7JCtqabvpRznwmcUkftVpqjyHhQT4o0yaNylJTTHnF4bwFc00tNjSxVwGlmezlgKoncm1ND_pHBEiBOo-ZXHWLIOwZuKyuO40-7p14tksyMBgYZuo1FcOGjVOL1bkdH-cMic5TOqI5pvrckMTkwxFuUGSEGRQiZwrmZ1nO8B-rwz17UQCL9so-3vDZlLEEJzxGbGMNnXcWZh5IP9NYHfFxSgmiE35yPKmYBdRopMwxz9eU2O_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درمسابقه‌ امشب الکلاسیکو زنان؛ بانوان بارسلونا تاپایان نیمه اول چهار بر صفر از رئال جلو افتاده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/30990" target="_blank">📅 22:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30989">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XspWEJF1V8BDdlFtGuTEIgGd6jZK9c-lBZAiKtXWcqgKi_Pl-V_s1hSB73afhrxuO6BfXkQE8sYqITXOEUnSPT3_bcElzvDFGKSJcfGEwLuQd4Re6slQrUaHllpXLQdOTKH0F5ZDheKAzdIGXwkb4a7dE6Ig9iozrxiMigz3UgSl5hQ4HWeXV3um2yG1NPin5yRHHwlivzGmM6q17MvlDN-5fKBVmtql_sWkdjokAumai5HbQkt3xHzcpoPsi9H9OCWI10tEI7icIgLyFMp6RV55ZeAfeicE6am2AH5E8cceqEtCXFx5yFESX6qtWxTGcpc-6_vcrnWHz9l5KUaFyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یاسر آسانی و نامزدش بعداز چهار سال از همدیگه جدا شدن! یاسر گفته بخاطر استقلال میخوام برگردم ایران که نامزدش‌همچون‌همسر منیر الحدادی مخالف برگشتش بوده و آسانی سر همین ازش جدا شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/30989" target="_blank">📅 22:07 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30987">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhgWZm5LgN6XPLeWkxzjYnm-hbcWKB3lDsplz1a5DhDEiWJNuG-A2xMsKtiAZCzQI6mzIDNw8UAukXaF90-N0dJi0y0MaNbVtwufKw8TMDu6ngZiR34c6iWRoD12ulqNl2Djctc79M0DiEXaUrNWbZkYb9P5z6qyTgivzWOF5ro8VOvhSJtRQDqhe-OK8xvIhm5rMJ7Ke3EWHSA8myIZRAAdTzQY4c25eNrC0PNqipDLzgMj4mhmezWNetbt21jvPc9H7ruCoW8keKWzSdOndWJeW_Egh97ff3pfzqjcmSiF7OeZkO8vtUyofFflFtzWjxlhPUu42yaLh9r_QMUIXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3028cac52.mp4?token=STgZkwTdxVVgIaopkqy4o85WbmbK67GvA8w15mPM5MRSkfFvyBbPCgKt1G7mhlUuzBkvFim31ueuEbGzxBk86WPG763PbBxrq0PxKpMud5g8lO_RmbdyCiQndnKGE6hBMY83TqQ5dvsJw2fjuERrxNEob-Ay8pP3HSsh29xUsD5EQF-ySCJ40emC3Ev4gVUigp0JGNDHHk41m0Onhn3DYPQofgr7FRE-iojvr7QJGmzBsOawVDg6HF02zY2TD3tWnAUXIH2bGUd2Bfqn94-37vKfqKux_2jJlsvS9ujOEO4jcvW4rj4pUoJWLdv6TqwYEF6dkKK9-LyYp4ZmtfryMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3028cac52.mp4?token=STgZkwTdxVVgIaopkqy4o85WbmbK67GvA8w15mPM5MRSkfFvyBbPCgKt1G7mhlUuzBkvFim31ueuEbGzxBk86WPG763PbBxrq0PxKpMud5g8lO_RmbdyCiQndnKGE6hBMY83TqQ5dvsJw2fjuERrxNEob-Ay8pP3HSsh29xUsD5EQF-ySCJ40emC3Ev4gVUigp0JGNDHHk41m0Onhn3DYPQofgr7FRE-iojvr7QJGmzBsOawVDg6HF02zY2TD3tWnAUXIH2bGUd2Bfqn94-37vKfqKux_2jJlsvS9ujOEO4jcvW4rj4pUoJWLdv6TqwYEF6dkKK9-LyYp4ZmtfryMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ ویدیوکامبک‌تاریخی‌پرسپولیسِ برانکو ایوانکوویچ درورزشگاه‌مملو از تماشاگر آزادی با گزار مزدک میرزایی؛ اون دوران الدحیل تو 51 بازی فقط یه‌باخت داشت که اونم جلو پرسپولیس برانکو بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/30987" target="_blank">📅 22:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30986">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgIzBTbvn1PYdQ7PKs6_-3QKZJ6WYYYAR0z5MI5-InKIY-qwbW7E1HndWHqjXOpqkDLP9wkAIidS6lPtYsDzDvn1tRnaG9XVAzlzamPYNigXRT8McGYvPdjDPl_dz83NGjxjeZ5OhEM-z0HjYCoE3WWYOBxcTgkFH4y-n0mwHNEWCZb--2Y-1c5QMWED5jF5aqQ_9So2Wh2zr34nyeBCY393wwl-K1z7H5wfVmQACtIcLIDwcmm_MCOjGh0kOoToyXf3ij_mniDgpIUVJubzZczOgQRZJ93uCH3Y0rLnkCtIh4eijTWkwQdWChzG1hWixgGlg-UxIAdB0OeQslEgVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خرید جدید تیم بانوان تراکتور برای فصل جدید هستند؛ نازنین دواتگر مدافع میانی که سرخابی های پایتخت نیز بدنبال جذب او بودند در نهایت با عقد قراردادی یک ساله به تیم بانوان تراکتور پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/30986" target="_blank">📅 21:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30985">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18eb463e8a.mp4?token=NED5o1KE9oJCUDJeABwq9yCmycZpk5jmOXn7ZXGnSAox5IbSYMHWEG3CXNok0BK-Xr-BZ9PwlXrC8pzS1fgWQkoYecHVbMjPuO6M90jJ5t7wTYVdz040enHRLc9Fi5MsYsJ3nU8x8FLisPuSVfhEaGNb9F2OoOhpVvgX8L8jM5lHSQqWLNiy7alyTAkbW_QJHHXZPnNIg4UKmlukmuKqAPhMivt-jSQ2zpFriFy4Pzf2_Se_PmkaJCV9JJsHCNHDpktcy72qxfBA58esBipxY2RvjiGjjW0GQjbeAKuJ666dbTjqNIXmnbwlNRs_lD1Ws3Em-k9-Y4KjcioJPVw-Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18eb463e8a.mp4?token=NED5o1KE9oJCUDJeABwq9yCmycZpk5jmOXn7ZXGnSAox5IbSYMHWEG3CXNok0BK-Xr-BZ9PwlXrC8pzS1fgWQkoYecHVbMjPuO6M90jJ5t7wTYVdz040enHRLc9Fi5MsYsJ3nU8x8FLisPuSVfhEaGNb9F2OoOhpVvgX8L8jM5lHSQqWLNiy7alyTAkbW_QJHHXZPnNIg4UKmlukmuKqAPhMivt-jSQ2zpFriFy4Pzf2_Se_PmkaJCV9JJsHCNHDpktcy72qxfBA58esBipxY2RvjiGjjW0GQjbeAKuJ666dbTjqNIXmnbwlNRs_lD1Ws3Em-k9-Y4KjcioJPVw-Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ تا به‌امروز اوستون اورونوف، سید پیام نیازمند و محمد حسین کنعانی زادگان بازیکنانی هستند که موافقت‌خود را برای تمدید قرارداد خود با باشگاه پرسپولیس به مدت دو فصل اعلام کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/30985" target="_blank">📅 21:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30984">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQukYUDA8FUsZgjHUGkb4_ep5ZSpjgNYmsNhQXVGeeVKB-F80ipxoDXihmXzbZsen-SH_qHocsOD3elm4-s1YtwjqAIZTK9UnDy9yXAQGzxaALD4D08ieWb9eiCufGICVifWwR9VWPAKQDfh6JiEnnBU_2tsLVnamgtumD-pE6Ukg7cGPI2v-dAHry1OOIacbIsexzIfdAWFbgX84QINnf1gyStcJikMR7FpZemfED1o8VlwCFY2l9TGc8-nV0AsqXa0vZNYrJMOTeSIbU3gbUiX0xc7Vzx4kza8YbFgKzDgxfzFkOFeEZle9RTc5V0yv30t57TXWRxJT6Hugl1eNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد کریس رونالدو و لیونل مسی زیر نظر کارلو آنجلوتی و پپ گواردیولا در تمام رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/30984" target="_blank">📅 21:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30983">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0nMLCp6oT_cb-Rl5_wJQc1-ShLn14haj7kr9oA6oItH9dQCGoTzkJu7IyM4jSxBDIiSqcYMXo6s-8U-tmNNsGw1PoV7eQRXQ4Iuz5-eIHsNFT6Yjq4otVzJO2DvWuQycmKtVAEi6LYo6NgiCASM6eDO_ygWW4SyouRbAbSiDGm3tiUZ1rku8TDNxH_qJ7FU-hzJ0_LlFh8nwHiOtt3VFV9umfj2yhA_s1LAZ7rpPAW-7aFfaYNJBj_2d1NMIg7EXnfaEAYnh-FaJK0a8KPF3sjDuq5kU09hiLn0Lu4xnZB2eWdtl2M0okHCpE1LkVOcLdpDkXLGUQMdslGjyhFWyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیژن مرتضوی و زنش درتهران: متاسفیم برای فضای مجازی. مردم در واقعیت خیلی به ما لطف و محبت‌دارن و هرجامیریم یه ساعت باهامون عکس‌میگیرن. مردم‌ایران خوشحالن!
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/30983" target="_blank">📅 21:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30981">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2561d16fdc.mp4?token=CfWFbNfkvAK_5NMi94otG1MolQ-rdUm5UJmTuBt-GzvlL2yKbASGt-1U7Gp-sL34bGB8BMskegyl5AC5nVhdzhaJvOGvNgI9gGMveGxERSiZCzpCmcAJI6zJn05j7fPUmWjDGhzyZYvTc4r1sxZolD_s_JiSsaLAtFX1_tl0NvSk-WfErU1hDVaOI_qys2GcqQalQbuHJSyWQAAPinN4V2rlImCZN5RHDxM9zpwVU9Kd3W7JBkWyW9VNg1lmQaqGBvrrxZnFPZfccQUGAVOigPXfZZO6Saivezmv7iK4kgHS-Rui8PcxdBE_j1eWlJ47JXxgUaGM0DoiIhT4QZIndw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2561d16fdc.mp4?token=CfWFbNfkvAK_5NMi94otG1MolQ-rdUm5UJmTuBt-GzvlL2yKbASGt-1U7Gp-sL34bGB8BMskegyl5AC5nVhdzhaJvOGvNgI9gGMveGxERSiZCzpCmcAJI6zJn05j7fPUmWjDGhzyZYvTc4r1sxZolD_s_JiSsaLAtFX1_tl0NvSk-WfErU1hDVaOI_qys2GcqQalQbuHJSyWQAAPinN4V2rlImCZN5RHDxM9zpwVU9Kd3W7JBkWyW9VNg1lmQaqGBvrrxZnFPZfccQUGAVOigPXfZZO6Saivezmv7iK4kgHS-Rui8PcxdBE_j1eWlJ47JXxgUaGM0DoiIhT4QZIndw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توییت یکی از طرفدار رونالدو: تو امتحان امروز به سوال شماره7جواب ندادم تا به رونالدو و میراثش احترام بزارم؛ رافائل لیائو لعنت بهت تو چجوری دلت اومد اخه شماره کریستیانو رونالدو رو بر تن کنی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/30981" target="_blank">📅 21:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30980">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjCgAM729uFrTnAoIIsGgu4McaXXhJbbK7QTNv9O3xZYI97JD1iw8coWckx6IBPDbymc7UDFx4OvYJoJ7ghQ5jiKT5TKusJDQnDEAA2sl2EFf4OMg2uhAlQ9uNohKBHFixawKJNwM3QXm8JTaSDI-O-huYdcCFZjcU0UCLjvlWID5UnLy3aEeyqh6kb3Li2jSF63oCgmf46nrEFwAW4T2MWQ0BpeKrH1rhL8XBnfeXI7bGNj_xImYBNXGcztqu5GnZqs7Z6j7vNXwhfX5jWKEJLlEtmRtKfZeRtLehRWMXGFP8k1GN1BR3cdt973QVT9OnZ9w9EW8RFS6Pqw4Ws_Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درفوق‌العاده‌بودن رابرت لواندوفسکی همین بس که تعداد گل‌های ملی‌اش از تعداد گل های ملی کریم بنزما، لوئیزسوارز، نیمارجونیور و هری کین بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/30980" target="_blank">📅 20:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30979">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYCgjQty9WYyvyoqfXL36qV6KbrE01N23daJbj86y2jBHEI05JaZw4U55Icd2j5QH4g5hkqFXg1vdDiE1KhRiy78vjkiHjIYPX51Y2eM4-Aw0ZgfqFzpnaE7KdV7WxaQxN_pdyPuHP-oD9G_fj2XmiTyg4B35ErsM_xAoyytxKPU-oBA80CmSllzt3mVYhiFMqbHTHckar06insCsi4yTQ7AYpiiXOUC3eSHUqshCQCLy0GEoYcsNLVzC5piPuBxViWP9kkAUcWxoO1S2XF83zPTyC05cbRTFocZNZ0aJoHZ7KpoJghTBHdHrhi9FzlEtDvuseeu9t2IqJyW4UNDag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌آخرین‌اخباردریافتی پرشیانا؛ مدیریت باشگاه پرسپولیس میخواد تا اوایل آبان ماه قرارداد سید پیام نیازمند دروازه‌بان 31 ساله خود را بمدت دوفصل تمدید کنه. همان طور در پست ریپلای شده خبر دادیم تمام توافقات‌لازم برای تمدیدقرارداد این بازیکن با باشگاه…</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/30979" target="_blank">📅 20:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30978">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9V-yfofLWEslQ0bTfaA-jDvmbDNSeeuTAqiMWiVq_wFhuFNGbGZgnKt4Vd_cntJtw-6371HtcXF0ypHsztIZy8SILyuvg058ZunZ1MMB2mYBHDCCH_9Tl8JZwMBB-in6kNTH2DJx7nSjMmi5gVneJBRSMOyPd7rqW8JYAGZ9Po5-ns52qFKB2LfWX3JRQcVZO7tzl-q8ieOpTBXvpfUa3HP-VMD1YSvl7otUM3G64QTUmek3hURjoNt3ahmraAI2aRihkjAQday0vJt5reeNT5tt4SZ7yNSsUc6OXjMcfnfFp2IX9ek5-PSPZe51g3qPSgr6rHaODggQ5N9_pNQ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده‌های رسانه پرشیانا؛ باشگاه پرسپولیس با مدیربرنامه های سید پیام نیازمند برای تمدید قرارداد این‌بازیکن 31 ساله به مدت 2+1 سال به توافق‌کامل‌رسیده‌است و باشگاه قصد داره بزودی قرارداد دروازه بان ملی پوش خود را تمدید کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/30978" target="_blank">📅 19:41 · 12 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
