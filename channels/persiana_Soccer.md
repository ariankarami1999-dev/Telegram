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
<img src="https://cdn4.telesco.pe/file/ptBShGFRi0UIXwwbdd_hUY48Ph30WOmpWBSHiu3f4jxbcQLMH4DlLtYZKbpejm1Sk-5I6ZqbtCQ23reWQwAl3NOdR642i3VnDTfYOVryr5PYP1E130DitS6x7PjZMdlou_ySGJ-2QYAa3AKJxy6OmhUvhBsrUzbufTk70umJ9uDf-zIop-HwsvOu6iFMQEFutmWHcHbHEZu5del1bl2DG8qcsWl5dQr0q0r0wgWK_2DEL0kbXPZaFYd0SaBwod5HC0laoOZxhbsVFD9nORZ-Z2xciPFvnZYUgF2uRtttjyk4ibjBhlep4Fc67pQNdVv2aL5jxDrxpgTshHx4aCMGLg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 527K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 23:00:44</div>
<hr>

<div class="tg-post" id="msg-29628">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8G7Qq5EhO_k3HE4pzsYikulMUivk39sS0T51vC0leg8N8kd-wqWyzdz_VcBOt4XFbUDoUE7Ro6fYAv7gUGrpWByaa6i9tx9Q7SUSm2EZX1G8d4UD9L23EJKgWIDsbzkT4AUeH8U5XKIwfFaOBvnYFj7b1MhOgH_iKxBNDO2C26a0fxqKeamzkBIZZ8O2_B25Nr3kkBfNiAis3NzlI9iofE1J-9PF2NrbGbDXSQ5_fSop_VlybCWlzSFQ49UDLif_91k0WV65FZOWQ7K0EFuY9sm2A4EpQzizBXoSlSDNE3hV6VW_hQPhmMAOLPCcs0mZMDWbzYNkbwsodmwB-U3Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌جدیدی‌ازبهترین‌برنامه‌های‌هوش مصنوعی برای تولیدمحتوای خفن در اینستاگرام؛ این پست رو یجایی ذخیره کنید به‌کارتون‌میاد و برای دوستانتون هم بفرستید که اونا هم ازش استفاده کنند. عالیه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/persiana_Soccer/29628" target="_blank">📅 22:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29627">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ownGveQDic45xZKjX5sXRoLq_5slhIQZ02dcApUTwrtjzSOjzgUEYeYkL-ejUqo5phIoco7szlBZo6zB5MJRxkjc7FaUOhsWHbAdShijKf0E4RzwERF1R8BxyNGzaNAI0n59pkVaCZTcif8_zZkotKcrAQnPKMid6BOBI7XpwOmuLPQg2c3iT7dMejGprmZ0JIygK3aXquohNEiF79XcQGLVU_elWvhdd9G4Fu896vBfy0RlQPB_toO9WzziW6Bd9llW4NToSh5W4FJ6z7S8W_ywWsSfy6vHRMak5Oirm2FixrY0u5hs8yxU77bFmuio5bo3Nf1tayHC6zHAV25Epg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخبار دریافتی پرشیانا؛ باشگاه پرسپولیس بزودی با پرداخت 250 هزار دلار به دنیل گرا مدافع راست 33 ساله این تیم توافقی قراردادش رو فسخ خواهد کرد و گرا از جمع سرخپوشان جدا میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/persiana_Soccer/29627" target="_blank">📅 22:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29626">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZpOdX51eVwFa5pIyZEQ5zNPVqqONHPil7qcRzXL7bENx4r7YE4cXADlrOIPUjjy5HZrhaXbGix0iijkX89FgOZda8JJYy5Qw0w84PVz_Fy5kTGBTMPdrgcZ-Td1nhi1P_9rVqc5tusDMcQsM9Ozw1ZyKPvW4ZxKj9rU2bVV4kaWyLg_lIrQO8uKDlYc9ogp1GmoTjKiZlh8S5dbtsghL2oqGfYeIAKAZzMCU4sXGWHgr6Ygm9lEsw282Kv-antcVb3CXRfCtpkCLObUzmmooNXcCUt6PxQAOkI_SVByhSbrRgaJaOLhBvXaS6Fx2ErnUHvCWzmjuEnnpbzUApMUkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔴
طبق شنیده‌ های رسانه پرشیانا؛ بشار رسن هافبک عراقی پاختاکور که‌اواخر آذر قراردادش با این تیم به پایان میرسه از طریق دوستانی نزدیک خود به باشگاه پرسپولیس اعلام کرده حاضرست نیم فصل به پرسپولیس برگردد. طبق‌پیگیری‌های پرشیانا؛ مدیریت باشگاه پرسپولیس اماده عقد…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/persiana_Soccer/29626" target="_blank">📅 22:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29625">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2989e9b119.mp4?token=DyKnrB2gPhAmHjb0cKA-mj5IFlBtlVwkIXNsxtOK-L9ML_NlC1UGTdlkE1u98jsDQkMcRj5JHjhh0lu4BZwyo_7AyMjgZ2zTgHSqQmqpViNAGJSRcJhKHFK8MTOYW_BCZRoV0iSu93n-6BOp7116ExljQ9nRdDZZi9VInZLUwtn7rEWQ3M1miGZPqx_npO45eALV7e4OZMwHZsT13QItJtBEqJB_1pbNT6m7J3GCOsuR-jaIUyiOdyl5JJkp09jC9GeA_UxgyJF59Tj7ra5MYRsK43c0h70VPof3KF94Igk47fKuiTiA05gImMECXd473EvImS5X6CKfsrtd_OWnLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2989e9b119.mp4?token=DyKnrB2gPhAmHjb0cKA-mj5IFlBtlVwkIXNsxtOK-L9ML_NlC1UGTdlkE1u98jsDQkMcRj5JHjhh0lu4BZwyo_7AyMjgZ2zTgHSqQmqpViNAGJSRcJhKHFK8MTOYW_BCZRoV0iSu93n-6BOp7116ExljQ9nRdDZZi9VInZLUwtn7rEWQ3M1miGZPqx_npO45eALV7e4OZMwHZsT13QItJtBEqJB_1pbNT6m7J3GCOsuR-jaIUyiOdyl5JJkp09jC9GeA_UxgyJF59Tj7ra5MYRsK43c0h70VPof3KF94Igk47fKuiTiA05gImMECXd473EvImS5X6CKfsrtd_OWnLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمد نوری استاد جملات قصار! شاهکار جدید ایشون درنشست‌خبری قبل از بازی فردا با سپاهان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/persiana_Soccer/29625" target="_blank">📅 22:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29624">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKn08gmiGcQ6LEN1bIgIkBt60YVa4j-qEIUkceWJcgq6nN8r53RsYbT4Q34lrRQ3SfG1frV3RcRknZGCMEo_GlkVIh3snj671a_z2tvM5e0jdPGy_wnuJHeJKaW74oeB_mXnK1bUyTnRKibxnVnICAEjnFiRKVrrauIsF23oykWWtQTVHaExuYLXaIuGUn6SvzlB-R3hfY13SlidaoA9afl8cUkQciarZmsdVYc7tCl-FrfMSx3D0n1iEkMG68pvjA1BwosXknMIFbbMzoJsPyBlVkPXlDaEQH8cNidWUiTXwAfQAefHbTrxKS41BYvD--FFw8dwoGTtAyxIenFuyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔴
طبق شنیده‌ های رسانه پرشیانا؛
بشار رسن هافبک عراقی پاختاکور که‌اواخر آذر قراردادش با این تیم به پایان میرسه از طریق دوستانی نزدیک خود به باشگاه پرسپولیس اعلام کرده حاضرست نیم فصل به پرسپولیس برگردد. طبق‌پیگیری‌های پرشیانا؛ مدیریت باشگاه پرسپولیس اماده عقد قرارداد با این ستاره 29 ساله تیم‌ملی‌عراقه و درصورت تاییدیه‌مهدی‌تارتار این هافبک تهاجمی خلاق به پرسپولیس باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/29624" target="_blank">📅 21:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29623">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRyOx2-SG3aCMBdt9mAr-9y0fud04g7cZgSJJgoU-NvjIdPESviSyXs47-WEhCaNau_dxnbhQnlTTKKQ-S9arEfNxsUDGHBGlOzrfPBwCu_iHIxqovBEMupSjDkCoS1KAas0eDX51FYx6uuNk-TgddnF-7rsWSP8wsT6B2t5gucxc-LfIXyTXCdejiLpEHUUHVcgYfl9QQK-muZC7s8XPKqaWVtntjsipMzMfGYOOXRwB3m62ZHklGpuznhkfXnhAK5cawH8JnarZLfHsc_3NqYIQk_3G3beEdEQ4OiSsCg-Jc_bEcZt4WCIXU6xRKuqb-XCbf7hAyDTSNsQHKEh0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
گواردیولاسرمربی‌سابق‌منچسترسیتی:
برای تموم تیم‌ ها در چمپیونزلیگ برنامه داشتم اما هرگز ندونستم چطور رئال رو مدیریت و کنترل کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/29623" target="_blank">📅 21:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29622">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
توهین به پزشکیان در پخش زنده صدا و سیما: شما خودتون لیاقت ندارید صدا و سیما ببینید
🆔
@Persiana_Newss</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/29622" target="_blank">📅 21:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29621">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfLSkqqO6vMhemse6qGacwrN1bnEvXhXBt1RUkpCOs9KhImG1-_HXwF9C485yatBmxf-Ja5AsEoH5rhQxHlh5fAm1nCzT2oWzpYUAcTUGWlej3wnxoc4HEiwVUtCpleNk68lb8YN3PlZF9RI9RHJmCM9sdps0dzbBW6I-XFGgVuIAO3QlWuYmCeGFPb5RQYt9ialQvzh5D_21pwWAR9yVbW4CNoyHz1ej6835NagwpSyuPlLQiUmPwkxb8pgHDHYQsxOZJhWWmVFH52sNDMA_aTBCXBxz5A9uP5ijkJV35-gyIqObEJjK_4WtUzM8ijNta4q8RcCWCsB4FdORDwwqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت‌امروز انواع پلی‌استیشن 5 با دلار امروز که حدود 223هزارتومان‌بود؛همین کنسول یه هفته پیش 190 200 میلیون تومان بود! قیمت‌ها عالیه واقعا:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/29621" target="_blank">📅 21:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29620">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzL-DnRkEooXNA4SGjrQE6Rc0mFx3jLGa3BF4IC8bymZ-1q8EvUQ67Y9OGemNZrA2fx1rOHT83-rnNfCjTYOejaA1HrIdI3FP4g0TqUh7l2oRP8dTBP9Dg5Oj7oaAmZfYLF75y3fEy9uIGIuofqKJC0ohRimfkXloG4X_m4alMaCGUFeEmr4i-OLMu2NaJG1D-sX_6A_jEQWN2wJ2_nGcPojAYNWuh7zl-narRiOUdNXpq-uuuSThVrz_mNkmACY5_qVc00cK8mg4vXWrHQ2IHpOMZRkSz4Lw_9-P4Lp2NVeDeh5_fdILS5AtZkfc89JpNeyFkaD6gc7_YiRe2Tbqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لالیگا
|شماتیک ترکیب رئال مادرید برای بازی با رایووایکانو؛ ساعت 22:30؛ آقای خاص بالاخره‌خرید140میلیون‌یورویی پرز رو فیکس کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/29620" target="_blank">📅 21:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29619">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHkN8c2jWx4QPEqtl-UBImkRRMmIScmEVq1GzB53WHzaSCKQ1wGpObfbsx2EnQDmEaX1m0IaCwa2C4T_g6aWdMgcTo0hXeqbTVEBIXD5OvO4fvgGrC5KNBRBjKLnjCTsKzG52VvgcXMek_nyaF_H473oOg8_VqrC4TeSgOwMTF580x2jL-S2natAeUznbQeOuwjKmBcLWdWH5L0xIcIAGk3U-yrCsxy6K4ydgPPiHEArG2ZEeztqkZZrug6sIj-rK8erqdD4YZjOCIruJkPmuy78l-ebHx7YGb3Fcv9zdJLKrOeW-nrkOWnDPxupYp_0AoMCni_QoIpuYS_zaSWJVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وقتی‌میگن‌فوتبال‌غیرقابل‌پیش‌بینیه یعنی این؛ الهلال اینزاگی امشب با تموم ستاره های گرانقیمتش همچون مارتینلی و واتکینز اونم در خونه دو بر صفر به‌تیم نئوم باخت. حتی نتونستن به‌این‌تیم گل بزنند. نئوم تا پایان هفته ششم  دومسابقه‌باخته‌بود و چهار گلم خورده بود…</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/29619" target="_blank">📅 21:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29617">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWWmC_7JEIHb1Q1OWTG5ocfn7_RKOixI8ecIgGqb7wxE3D5xoZbuEqQcrltB605MnTJh_6TFbWUCjtjMW-yQonze0STQvN0Vzm1s_tmNoujzuLFhaFjbuwvkfDyyi4IKAKJ_g4avp5RGceqXSUv_ZCyWxiL84Sh2fIUU8dsZ0kcwMDn7qRgYPB4oD53HGFCf10Toeswo43F1cDgPNvCsA-l8C0ZEWeu6LlVPN8GLKGq-K7Jvj0-wWj8GM0nIk-cU7uqmUnaXOemeYiLbU9AdtX71NxqoD4xhvWThbeSozWcxymLxu20dcUQwhz5tLkg0a5RM7Q6smnB1xpTdD5y7aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عملکرد مثلث هجومى السد حریف پس فرداشب استقلال درچهارهفته‌ابتدایی لیگ ستارگان قطر: اكرم عفيف: پنج گل، چهار پاس گل؛ روبرتو فيرمينو: چهار گل، دو پاس گل؛ کلودینیهو: سه گل یک پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/29617" target="_blank">📅 20:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29616">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuT2acNcIzHPgniOyVV6LtFjbPTn5U4Q6aNcfj0sJeKnCK855bdE5JEuQkw2CebGAUxMKXCwkA2KuNLYnL5-fZIzi6u0oR1fRIaal3YVFFkgtv__BfQPZalVOXrARUlGBrevPJ5k8VfDzL5S1s5ObushPNQnya1zCrlhQWGTkbosMPJDhcYlMe67qOT-ln4kR2hNlr4e_JPgOXetvLNrFxWyld3scMa881seVXZQEmypUQasz4y78x32EZnoaoX4SWlJtEM1s8SxtYyHXgdxPG-njmwu-TwK0e7THsfcZvHvvU_6svtA8hXNinmEnhavAbJgPWl7eig6QuJzPajWhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عملکرد مثلث هجومى السد حریف پس فرداشب استقلال درچهارهفته‌ابتدایی لیگ ستارگان قطر: اكرم عفيف: پنج گل، چهار پاس گل؛ روبرتو فيرمينو: چهار گل، دو پاس گل؛ کلودینیهو: سه گل یک پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/29616" target="_blank">📅 20:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29615">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6942e2257c.mp4?token=o_5ngxnpHMgxTiNddG-a1cwFVoXl2TXYgw_xvyk2JaE9ROBNgTrQNw_9nv78XbvQUqXvZPoI0-m8y9USrWMas7hOaiUjSoimqoeVZFQ_3Kb1IOJ003Ak3d47W0MqshPyyUF7KRN2W0qimkwX8ZdglWAuxymqqFXiz3pI9Lx_NR2UoUoP9uvoUOMmrPvUn0pNdm-7jv-MStG1zq_PutNg8MReyGfQ8csFXJ60SyqXz0QqrudfD85iHpHlhb6z3bI-t2YEXjAFtiEOOFEj3NwfGICkHkcPLNUWq8GVHTuYR-fOp4zTlNRT6na6w4-J9eGN7CTYLujOnRnInRNb38bzVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6942e2257c.mp4?token=o_5ngxnpHMgxTiNddG-a1cwFVoXl2TXYgw_xvyk2JaE9ROBNgTrQNw_9nv78XbvQUqXvZPoI0-m8y9USrWMas7hOaiUjSoimqoeVZFQ_3Kb1IOJ003Ak3d47W0MqshPyyUF7KRN2W0qimkwX8ZdglWAuxymqqFXiz3pI9Lx_NR2UoUoP9uvoUOMmrPvUn0pNdm-7jv-MStG1zq_PutNg8MReyGfQ8csFXJ60SyqXz0QqrudfD85iHpHlhb6z3bI-t2YEXjAFtiEOOFEj3NwfGICkHkcPLNUWq8GVHTuYR-fOp4zTlNRT6na6w4-J9eGN7CTYLujOnRnInRNb38bzVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
گردوخاک اللهیار دراروپا؛ گلزنی دوباره اللهیار صیادمنش ستاره 24 ساله لخ پوزنان در بازی امشب.  عملکرد فوق‌العاده صیادمنش در فصل جدید برای لخ پوزنان لهستان: 6 مسابقه، 5 گل زده، 2 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/29615" target="_blank">📅 20:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29613">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tT6havQfxjxr9tkuLTrmq2HtYjCAfSrHyPXYryhbDQqHmK9PENrI0QlEvkOTFgyJlDTXz_fqg0V8TMw0FnBe6Itq82EDrIY1FdKu6m57uW2kvR1lYqLZOEUmnloK591HPSCMyIgRQBeSiRr7XFyCnHhcIbF36TTwFSGRkpLemxPaGbWwnZQX59tJhj0lDoHNIvMU0Xe1E-82N2iuQNl2E9cWSbYvs5dwW_aWhz2AKvNUdJogGxO9tqhB6sZJo0bdLYanOIXRC6vOmMnk8uwXLNK-BEMKycyS0lMy58jxFSq-kxybaTuXX-WbcEoHvAR5uzbOoliy4_eqS41Rw96LKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mLfdCT0u4dI8H738pjEK1jp17JpzB5Fb7L_e1PPmWLOxr28haozbwfJI2CIMCPqyn_QJxe6Eq1zOR1dTitu_HdyEIvc9jAOvYjNVfx0J60rvadLEl9HbD3TM8bLHpxuHgkHEik4wutc9yZ6AkSHNfKOm_LYsn9YyLU_BFFOOPbz5wvF69K9nGrlLA5qWy1V7ho6JewprsjllgfDoIMZClCOPxjm7a4caFyD6Hs-k2DPJzfQ9rix99nq8RlPVDHIdXaMz2m3CGiz9QMap5PvljX7qkeMaW6qbzrN4BNlvVe4u_tBP0z8kDPI_dWfr6tWzYiqqDFKoG9O7xQ0DDqNwtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
عملکرد مثلث هجومى السد حریف پس فرداشب استقلال درچهارهفته‌ابتدایی لیگ ستارگان قطر: اكرم عفيف: پنج گل، چهار پاس گل؛ روبرتو فيرمينو: چهار گل، دو پاس گل؛ کلودینیهو: سه گل یک پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/29613" target="_blank">📅 19:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29612">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‼️
سرگئی‌جاکیروویچ بوسنیایی رویادتونه‌که 3 سال پیش دریکقدمی‌عقدقرارداد بااستقلال قرار گرفته بود این‌فصل سرمربی هال‌سیتی شد و این ماه نیز بعنوان بهترین سرمربی ماه لیگ برتر انگلیس انتخاب شد.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکرد هال سیتی در فصل جدید: سه مسابقه، دو پیروزی، 1 مساوی،…</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/29612" target="_blank">📅 19:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29611">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzI6MhehLPJJ2pvuJKhn98-WUM-7zrK_Ogr1hzJP5q1cb_NuXcqZRxrmi1mjGW5JqoOpUXeikq0rcT2GnAvhvX4TACeJZA_8Ja_wOi79K8pRv_bXoW8aoeLj2B9X87u3SSCf0ccF_AQmdC_sohvxyUFN2SWS7lRqLenR71N1XtSmDlhFU9XloaFFsBxgFdPTA_R1tW1M5H9TB2gFYOWYm3vYcTlUTa88J028Vb257mrwsWvbUOZdv6HEM9GOssPXER6UzYuvNPH7TxkOBGjNe4sLxomL2Qlg0c9CULb8SrUrYZkv81uvSGZpGhy52gns8qOowJPh3sdVxTLbatnVRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فرصت سوزی برگ ریزون لوئیس واسکز مهاجم بیرمنگام در بازی امروز این تیم در چمپیونشیب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/29611" target="_blank">📅 19:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29610">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgIuZJZDsmdTPi_sUJQgpzeULMw4lRdxDyVMlsyGWWqvVvGBbPA6sT4T0I7X1HJWwVdSyuA9a0mgFVBh5P3nMz0cz5llFLfUlFXSD_qAp-syuT3U1523nIO1okwR3e77RSLfuWjAZbu6pZxFnG5njfQqiY5gLv1U6JwQ6kRCOYBbo-FPESqkofmhX6VGpHz-1LS1Vnq9t5DC5m8bF_G8scGYoFCjcFy9KuITTAfPTAk57nD7rufbo1-BzNhOaxNZMJR2Vx9EmCxoGcP-PdB4yUk0JUxIej23v3nK7QzfhYbxeE8cY5Ul29A6IkIAwlZGsz9pshdcp1mvl-aDtvdUqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🏆
لالیگا اسپانیا
⚽️
رئال مادرید
🆚
رایو وایه کانو
⚽️
💥
باپین باهیس؛ برای تو، پیروزی یک سرنوشته
🌐
سایت پین باهیس بابیش از400اپشن برای پیش بینی
🛍
پیش بینی باضرایب بالا
💎
🤩
🤩
🤩
🤩
بونوس خوشامدگویی
💎
🤩
🤩
🤩
فریبت ارزی ودلاری
💎
🤩
🤩
🤩
کش بک روزانه
💎
🤩
🤩
🤩
فریبت درگاه های ریالی
🤖
دانلود اپلکیشن حرفه ای
💵
درپین باهیس دلار با آربیتاژ 30 هزارتومن بیشتر ازقیمت بازارمحاسبه میشود
🌐
لینک بدون فیلتر
👇
👇
👇
g21
www.pinbahis.com</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/29610" target="_blank">📅 19:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29609">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdC85qbWZMQG1pJhLaJKHfimzxGMNG6s5UR3GocSKiACeo0xoC3PLGyyj4VA5xTNP8jcHM33sFyzAL8-8KRpx724FxNOp7nM-9flZGpX9MEwKeMEAGDK0uAnkhTbU6d3AUvm5qKKtI5sZwjv1nW97OB7e5RUgYm-9h8mwxFm8-Ap-t41fqR4f8lQIWg1xtmeXhnTR6TmiT5FqjZFDjXhhsWBFOXiIlVE9iEyQaUXY-2tBOozMhFrx-TjLpcTFddrcXTDZiu89H_IbTUKeV73mTG3J8sKPMvP7xDugCvQuq2xpw6JEWgxhVOPGMJW5WbHWP93JLflD2b2OML1dnedug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
نگاهی به آمار خیره کننده مهدی طارمی ستاره 34 ساله الوصل امارات در دوران حضور در پورتو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/29609" target="_blank">📅 18:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29608">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFLD-2trte8EFScTgX6vWJaDfI2JBOEILWHIjpSCVZEfIDZ8YkSgBl03AqJqQjfxdY1mFfJ7z6UE9fpirC3L8paG2KpPOasyobA0kDtVbiva3ylcrLIbHV1bj9FT5U8q-qyFTNQkfcctLoXdG67ZT1PB4uaXH2V1FhiLKSeMdmbvqCey0Og4j1CNQJEWxiHoZTtkpF6PrLvLK0bA5iNTRrAH7YIn02mDdFSCow8eQJBD_6BkREpKl8-frXIoQYg2HTwHtBS41WuEmDljweQhNAlNsDpah14ZXoPLfaEyvUevx7IutY_HQI17DMqP6AfZ9dnfe58yKylK-tN3UVqreQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ AS: میکل‌آرتتا اگه تصمیم گرفته باشه در آینده‌راهی بارسابشه فلورنتینو پرز سسک فابرگاس رو راضی خواهد کرد تا به‌‌تیم رئال مادرید بپیوندد اما اولویت اصلی پرز اوردن آرتتا به سانتیاگو برنابئوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/29608" target="_blank">📅 18:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29607">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇦🇷
ویدیویی‌فوق‌العاده‌ازکاشته‌های لیونل مسی فوق ستاره سابق بارسلونا و تیم آرزانتین درمستطیل سبز
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/29607" target="_blank">📅 17:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29606">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1Gbneqv_VbXrcwh9B4O0ax4MH628kR4JSOwRLyURks8FlcAFPfqIB4lKFd-cL9NElnQsk4e5wQKO7E1dhQTnGGnFg0RcQWIAfFwuSg_h84CTfiaSpy5_lIdOzuHKyYNHktMF_FEQ1XljwW3PmVYzzAq5zLBWIU8hh0UVtj8EFs8xgIHsdMYUf3PwyYU8WHX-9V7bzLxXrA8B-mBKm5JaWCznh5DUOY_CSybXHq3XkwnCD6E26rDxnJTFRN7loe2rilIB6hHqIqmPTNtGPGQkZ-rEHK0utd8g-lDq452Kpa3OW2k9ejEEHHP_-IgE6dqC2QklX-Y1Tm9LmBPcPOptw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
پرواز تماشایی برای گل شماره 979؛ گلزنی دیدنی کریس رونالدو 41 ساله در بازی امشب النصر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/29606" target="_blank">📅 17:42 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29605">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckQ_i44Cseb8uHwThRoWRXsGhBJdzIPcb9YxRNqUxNTybxGKvLVFoiNsCwxpKXzEFW7cTMkfdo6aws4irdLqYMYOWBKynwn_vdUwTAOLpWDbFqU9kLQzaJTpbs3x6y_EglLm3_lRBFYRhrpmPgPA0al8zfhk5gl3DfgJVPrsld1qXmKKiCpnZZvCfZZi_rfENsXailOKxjsif0Iegd6rpNzhKmBIqygPEeiJRGgXA-4ehJLNmtCMAp07ovTZJwp04G3zu0MASZCIjuSU85CHYpk3UloYfgFKZwFCdGNc3vpGMb3zV5ghFKe6sVrEEdtchhDKWAzoRwx5bJFoDKFlRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔴
برگاتون بریزه؛ طبق آخرین اخبار دریافتی رسانه پرشیانا؛ مدیران باشگاه سپاهان امروز صبح به‌مدیریت تراکتور گفته برای صادرکردن رضایت نامه آرش رضاوند علاوه‌بر تومیسلاو اشترکالی 50 میلیارد تومان هم بایدپرداخت‌کنند تا رضاوند تراکتوری شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/29605" target="_blank">📅 17:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29604">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Js4tgGy7pd_lyN7VIq1c5T7iAfqZVZB3wobrc1Yl7mI_83Ohw4Hov9-R1i_b42JTG1PYT5hois4W2EdFRCD7ZTLHsXZLMzkaPc4Shz2q9FSKjdmKXwKXMDsgU7xIqItiYQyNmw0NM7l5Qi5SlGLnQFMI-8hznqknzSfErYuld6DDBhkDaWK-IMeFTJuCA-vqAwCkiR_UtYcqgQKaSm8alIRiP-JVMkXNi28VwPljpGa5jv6kMq6l9VkR-dd6r0hBNnLF7oWcSSma_zvTPCnHLIDyPetHYUDzpL8ZVY7ZQiVcdaPTjnF8qt1g0ELjihv7UdSfyuA2yVcAcDqPYzvd1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
با برطرف شدن موانع موجود، کاروان تیم فوتبال استقلال تاساعاتی‌دیگربرای دیدار فوق العاده حساس مقابل السد در لیگ نخبگان آسیا، به طور مستقیم از فرودگاه مهرآباد تهران عازم بصره خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/29604" target="_blank">📅 16:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29603">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pD67VcC34oZYj3UvqMeiTr_DW7PRWQeVahl25Z2CMjMoa-weTwAvO_sgcIH8U-e8YYeoFCFr9oHUh5woTVsdLqtOW8RdZtv8l-vlMQLnH5EMRQICtgGRPeHFxFLPHPvXbwZWYgb0p0zxzkq7lVA8AmzZwKat88VFm0ki8zN-6Qo4cc9RwQfytsOcbO6d0bLnko4G92hKbfMBmbUNdY90qVUdMBBEIT4wCjZJn_uF1TddT3hl0fZrmIGMRVXv-xxRuvMxvLftMsQlch9JXCFl617NGwn2fAxaiu2PRaynsYU6xVEqr1Lox6fFV_6A2UdVyAbGzHM_kc14D5e1IOT16A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه‌کامل‌ودقیق دو سری آیفون 17 پرومکس با آیفون 18 پرومکس که دیشب ازش رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/29603" target="_blank">📅 16:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29602">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abe26c296f.mp4?token=FDWrkKHd9-ht3VsmHeTFjGfAIUkyhsuGlFFr_EvpT9nmHIIw4xz82HRx-3QnHsQ6NZrOwrWlZ2ZCvBSKktG-4KpwBPtfSn_2xEZiAbQZx8Lu8NQyV0A5hNtk7fFLqlqX0yunh1vOf0LZYCQRxt36G0JB_INccYog_sXSKIUC88P1ezy-O6HC0xJ7Ed8yhW9nKh103BbL80x95TNZ_4NPnlCOOEWL412_Egj49ggJ29domeYx7nEc6H0ULOiDfqRKau9xBQ55nyeISMYckvO3YnXOzwiJcUxl7vF-4w1nZWt50pa1JH4dU-a_e7UMPrwpDjd3ylKHxTjayZqAHQ_ANA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abe26c296f.mp4?token=FDWrkKHd9-ht3VsmHeTFjGfAIUkyhsuGlFFr_EvpT9nmHIIw4xz82HRx-3QnHsQ6NZrOwrWlZ2ZCvBSKktG-4KpwBPtfSn_2xEZiAbQZx8Lu8NQyV0A5hNtk7fFLqlqX0yunh1vOf0LZYCQRxt36G0JB_INccYog_sXSKIUC88P1ezy-O6HC0xJ7Ed8yhW9nKh103BbL80x95TNZ_4NPnlCOOEWL412_Egj49ggJ29domeYx7nEc6H0ULOiDfqRKau9xBQ55nyeISMYckvO3YnXOzwiJcUxl7vF-4w1nZWt50pa1JH4dU-a_e7UMPrwpDjd3ylKHxTjayZqAHQ_ANA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ویدیویی‌از اولین‌پنالتی تاریخ فوتبال که کلا 0.2 ثانیه توپ تو دروازه‌بود. دربازی این هفته لیگ MLS به این شکل که مشاهده میکنید بدون اینکه توپ به تور، تیرک یا دروازه‌بان برخوردی کنه گل میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/29602" target="_blank">📅 16:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29601">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLFnfI9zvMwdyRfrEfjBP3rv4OzJt9wio0tYdmFXzBuoZxwtMHf4pNnGpw7UYuO6X_eGRh3smIbHx6Y1HcFdDuUsFhum6ZztLWJM0iImm4O1ZQlCy92FZR7hT2ynsrs4bHAqvPbfls_9dNyJ67gIZupU3qYiUIS2_pofFqBWIXEQza3c1DubJxjNtBiaKg5pqqeohLGVsAY2ns0isFARcoHb3g69PLFIqBJMqhC_jomHyCxjdmrt1zg8OZznK2eX7V2boR2gbmGSLDkVxtRLoYDcWk1joDj9zmuJNUqPuHKRAZd7sYCf-wyeHnEZ0ACx4XjMlBaeWqVJDzPmopPeSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یاسر آسانی ستاره‌آلبانیایی‌استقلال یک خونه 75 متری در غرب تهران برای تدارکاتچی آبی‌ها خرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/29601" target="_blank">📅 15:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29600">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2KAxxQgbk9MWZQTcR5223bi3kInzi_Ngl3LrcPengMZe-Y7KJDXo6tOHsH-mhgbXsJcMNEjewKBDVOchQ1-Tn5UNjGT6-jR8GtcLdzroM2WIGRxswDgfLvQS_r4xRRRxt06h5yQ_NCipoZ0unvXVxn1qU-vM6ew1arX-dFdCPoYm79d4shIBWLTk_yDoBD_H_7qjL_0EBIQS4KO-ltv5VBy6LCaybTLOjSpKYuV-3yk0Z_gEJkACLfZDrl3KgiCvT1ZdlrHSXY_0h54y9kDPJF7iyvME2UKV4y8qJj-9VKD_I7zSsrKNuIvEbtVMvhkPa_t5OXqv5XPPAc2em-WbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌ پرشیانا؛ باتاییدیه کادرفنی؛ سردار آزمون مهاجم 31 ساله شباب الاهلی برای جام ملت‌های آسیا 2027 که قراره در دیماه برگزاربشه بار دیگر به جمع شاگردان امیر قلعه نویی دعوت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/29600" target="_blank">📅 15:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29599">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epWHa-_4Q1w1w5YXSJCrrVqW60B7PVKvo7c3Argnj5ZRjsL_ef6Zsf6W9up1BBdHI0wEoOe9z38Zkd9ZyT08E8NwyBbVZX_VsH6PuVX5A17BEYexMcizellvzLsOsCgs-RSyNWIBguIb9uCzw-nlEeQTwKk5MbwGiYqa5yK0-87s64DDMBhZgKnPwgiGJsViumn2Wjv0j4Zp0vH0R7KNA5NyByO0qsMvv9M0K1d62VUlIqOgl0kET4dxWvF-Y60H9VhQp4i1bMEb3Ea3Lgnx-Sglv2jhB5Aq8t_ilLnC2opewq2NvVhJErzuCMlYzit7qHhbfIDSvL-ce8_bHN76WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ بارسا در لیگ قهرمانان اروپا؛ رافینیا و فرصت تبدیل شدن به بهترین گلزن تاریخ بارسا در چمپیونزلیگ، بعد از لئو مسی افسانه‌ای.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/29599" target="_blank">📅 15:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29597">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be2a23445f.mp4?token=tx_cpQBtTCV4RWYZZ3xKf9vT8Ar5As6FUKN5BGDCLfeIoyjUQ2ZbkU21HuzPTmo0mlfR6I_ZHGWUwOAPnxoLhpwttrcOpj5up7sknYjaFwi174fB6bFTdddji2X7585OrgLbCQcgIUmaAA9X9vECbvpABuUvfkZYuj2lngy2Cl9wJIuV6ceJKlJ9lCH-T39fU4v7wBxgYb5Akfx41lu-_Q2h73n9N2VbvHpNBS_CPMhJl-CDmJWb8F2DlKRy4Xp91TWu3lIumETxYVB0NcIAsnGKx3A7aP20XcvUUKk38qOmFiFYz-m_xNY_xt8mAky4VbGxGjG4tOqPc9OkADDeNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be2a23445f.mp4?token=tx_cpQBtTCV4RWYZZ3xKf9vT8Ar5As6FUKN5BGDCLfeIoyjUQ2ZbkU21HuzPTmo0mlfR6I_ZHGWUwOAPnxoLhpwttrcOpj5up7sknYjaFwi174fB6bFTdddji2X7585OrgLbCQcgIUmaAA9X9vECbvpABuUvfkZYuj2lngy2Cl9wJIuV6ceJKlJ9lCH-T39fU4v7wBxgYb5Akfx41lu-_Q2h73n9N2VbvHpNBS_CPMhJl-CDmJWb8F2DlKRy4Xp91TWu3lIumETxYVB0NcIAsnGKx3A7aP20XcvUUKk38qOmFiFYz-m_xNY_xt8mAky4VbGxGjG4tOqPc9OkADDeNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شاگردان پیاتزا بابرتری قاطع 3 بر 1 برابر استرالیا درنیمه‌نهایی جام ملت‌های آسیا به فینال این رقابت‌ها راه پیدا کرد و در فینال برای قهرمانی آسیا به مصاف برنده دیدار امروز ژاپن و کره جنوبی خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/29597" target="_blank">📅 15:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29596">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T55o4m2VPEQNYrUvLzFFfVMaZTpaK1-8bvgJOpsTLprY5a1GiVYmeUP-eNJW_WnqAEAMVl0pi6V8djBrDY_bZKnuUhgwPAKPs8AE_1r_g1RmhCBW56BaVEkWRewaSTYh8keHu-AEdaSdtz39WAReCJ6WLFHrOvtTJSuESZD1wKOAEtDlqIYrH8a411hwu-zOK6ViGCcbRILOTwLVnTvV2ZItBDqgwTfJO4289jGsJkkYnfO61EglBY3u-6JwsXBYHr1M181twOmlP-Q1IQ_jwjmAWwN-2KTHIXdwotEdMAaWBWiY6RVIs4X6_2uX2TBtSh9EnhKPeEW2Se0bT66XUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کاریوس دروازه‌بان سابق باشگاه لیورپول در کنار همسرش دیلتا لئوتا گزارشگر شبکه ایتالیایی DAZN
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/29596" target="_blank">📅 14:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29595">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wslx7AzbYttC3dSRHXvfdcnJ3MEMxHIzgcMdyA0utFHPS_T4EiG6J_jRrFJTFoOANjjVADS_xiTJYq9aq3RLiZnvGK8ko2eygSY1to6foiFE2ziy-c5gMPxJ4GsVjrr_CjIyDO4t3FehOOgcOpVH2f0sT5evy3uTg-wwkaGMYZr_03K4sJIEsG3mMoLLpXfHgxym8GCaQJepO7_MMr87qhiWVi8szMqcM8mmfopJjMZEht7jZgEznPix0VMsm4YqWchCNGEQBxrqFSaZWqZGR_TE0iAkzzza3Zi8CpvmFzTll80Eq8X4GEhtB8nd3N6B0kGP4FdGEFSCCW3F7jsYpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌ویدیواز اول تاآخرش‌سم بود از دست ندید؛  مهدی توتونچی تو برنامه‌شبکه‌ورزش نادر محمدی رو اورده بود رو آنتن زنده بهش میگه شنیدم میکل آرتتا دنبالته که تو روبرای آرسنال بگیره نادر هم کلا ویدیو کال رو قطع میکنه. بعد توتونچی میگه آخیش! پست ریپلای شده رو هم…</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/29595" target="_blank">📅 14:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29594">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozhCqX3sUhxnPBG20FYBiYuZ1ebUdK6nIsSgseC378L3CyEmTkPyIF8I4Qw3LXO7X3Tfzn6jVig5CUL6KopqFx5_-kyE-CSlA0MPGabCYJJUY44xajgpXAJDXTseptzRZb3-eyc7TiSXG5bY1ezI7bG46YuYEr3uNjoaPeSWh0K1efYrne85YmAW21IOUvYizp6TZ-pE575zlE93601jRRyubL0Io5okIZDKPP1ipdqZWj6BuPtSGUPElJ12hfTDyGgC1CLJRNNd2xUuPZB8kQ3WN4KCnHpRWszyzqh6vNmaoRxELxpXOCDMH0tSY-eibsA1vv24sSJKl21huzPanw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🟡
🇧🇷
طبق گفته رسانه‌های معتبر عربستانی؛ ریچارلیسون ستاره 29 ساله تیم ملی برزیل و سابق تاتنهام در دو راهی النصر و الاتحاد قرار گرفته و به احتمال‌زیاد راهی یکی‌از این‌دوتیم آسیایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/29594" target="_blank">📅 13:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29593">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ro9Ddol6i9_wtX_6TXdieVrYSOeb9TtIJzlCtE-IFc5Zcro2N_yvf9GV_0ti-8qCmOK71uApI1DsWaLl6xQZ5AE7u2t7xN1D1tNkLLbtdZYNUyt9yav0zecDe7L-LOa9ZI5-JrRBCmhJ-pDA8TiPDhZ0lCGQquloeNqUUwh8B-dC1IprmiAFreqL5rTwmUwHfgkjCogc3cdTzuitRdpU5dvQQarlvUscjAl2pOcivgx_3rK-cNCHH9lI0YCC88DAdFMvclSktvgVQTn7sGv4XWIZimn6n3jsRyHabI5c817gXBwb1rKXUZBDd7P_8BaLxcW8dVeLRU4auf2j9cLkug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ بااعلام‌پزشکان باشگاه تراکتور؛ پارگی رباط صلیبی مهدی ترابی تایید شد و این بازیکن 32 ساله رقابت‌های این فصل لیگ برتر رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/29593" target="_blank">📅 13:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29591">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇪🇸
لامین یامال ستاره جوان اسپانیا و دوست دخترش همراه با کاپ قهرمانی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/29591" target="_blank">📅 13:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29590">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tp6OZ-673UuICAPbrKiuyvp0hG_bSkjFTjdhMLI31fiSaIo4A0s96EIEssjzu4gurk6tdupFWqmdzl4qP-g7VeXOoqAdAnrLmlTMriG65Y-pP-gioWzqtOCqegBRg1dSidHmL2QSDo1lreuwHcMTJOt3bcMD2nRYfKWIsOr_6L1Y7kPv-9pfLA4MfRv0D-ylDWNmmvRoZZ-mExYASIv1nx9ThFYUJmck5iIknqVEkmToaXe6Og75QbRDkfwmJ03iQk5e_WjeejgpkU8Z0y99InduU1JGn7zUKJNm_dZ3bQNQ_wJLfPerrBpfvlJJUcvyUOhPwHn8XjhTrvd8VNYYEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
باشگاه پیکان از باشگاه استقلال به خاطر استفاده کردن از جلال الدین ماشاریپوف در تقابل اخیر دو تیم به کمیته انضباطی فدراسیون فوتبال شکایت کرد.
‼️
باشگاه‌پیکان‌مدعیه‌نام‌ماشاریپوف فصل گذشته از لیست استقلال‌خارج‌شده و با توجه بسته بودن پنجره نقل‌و‌انتقالاتی آبی‌پوشان،…</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/29590" target="_blank">📅 13:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29588">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZU4LJ3XxWVKRQs4DMGlWNRyQp6kN3BWG_dWNcMb2mps3_1YBP18x7pD373IQvwW6S7F_FpNq2My1XyEkg9wYin3CiXgYSMqeOLadT7St55zT0n8yF1bgeYJL-SGwdttafK4RmX_qa9MRXGmKWYONroum6dGkW5A4kMEU1ocLV3Rf1i_eeZECce0Cq5Opv_2d6mb7i95VqgizRBogoBINMRJ0GvVRlS2VYCYbnpNTzr32wFUA_hH6eK9Wdvyy2dTxAbiedhzE_GW-5kXxSTjK7-rwbqa5nQajOl4iOH39S6nVemJRoO1sjyB3igBOL-YteXm_XAyyeTnB6g6XLMlmgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
معیارهای رای‌دهی به توپ طلا؛ عملکرد فردی؛ نمایش بازیکن در طول فصل و لحظات مهم و تاثیر گذار؛ موفقیت‌های تیمی؛ جام‌هایی که تیم به دست آورده و میزان تاثیرگذاری بازیکن درکسب آنها؛ بازی جوانمردانه؛ رفتار،احترام‌وشخصیت‌بازیکن درزمین‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/29588" target="_blank">📅 12:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29587">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLWaTYQ_temNHsVC0XaxGGsnLgqeRlf9cKkJtLE1mNZXPya7WuRbEcolxtpaHmB_cNH1tUCcao0KYKUFz03xF0rkDHjCn5qaLd7mIRKx4klZCPKmI13aHofTR0a6Y-gUKu6DvYss1Ymg1lu-fV9MdshVirNY_Hfi4_8A510kMX-GpViUrGUZ45xWTcj4dAsv9uVfCCCE2qLnGnwaJ8dSJFILjnr7-dqomYlgh4MznoC7rTXcGgvvCZenUzNLmqUx788HvmouO7e7GdikGqrIjO0u7sQVk7IMTZgNQ-rI9wWSq1WJupAweFxKApjuAAiJZ9Ksl3LoIRiV1rgsZC-loA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
برگاتون بریزه؛ امیر قلعه نویی سرمربی تیم ملی که تاپایان جام‌ملت‌های‌آسیا در تیم ملی موندنی شد درخواست دستمزد ماهیانه 15 میلیارد تومان از فدراسیون‌فوتبال داشته و شرطش برای موندن روی نیمکت تیم ملی در جام ملت‌های آسیا این بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/29587" target="_blank">📅 12:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29586">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d3e03b999.mp4?token=CyGcEBUbhZ6VbY7GcAd4TQW8mHQMMcyBtvbccK5fsZFj9KGY3nz-oxEQKm_izEXJ_3xsVRhxDQM8LRQrwbxYPgXoLU_b7DHAZaWVTWQ67BAHlA5jYNoMaohQlZEQJjQfjJ_zvz6cXSAAo9TINBnm6wZcpXB8U3N8AK64LHvCmDMimnIkuXw9ffby7ATE7NI-LRU_zOSsdbc1Xj5ZAwNfHGrttoBpdDdeoh8EqL86TvfoLQs4aYRoFSWlEyzugANhOU6z3DFVJV4jqgsnJ_aYcJN0xZi4FAIQaHv0p1dq3EE0A5dpfBBnj83mfCCkLHnXIcAtYpTE6YzhB1NiyEO6sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d3e03b999.mp4?token=CyGcEBUbhZ6VbY7GcAd4TQW8mHQMMcyBtvbccK5fsZFj9KGY3nz-oxEQKm_izEXJ_3xsVRhxDQM8LRQrwbxYPgXoLU_b7DHAZaWVTWQ67BAHlA5jYNoMaohQlZEQJjQfjJ_zvz6cXSAAo9TINBnm6wZcpXB8U3N8AK64LHvCmDMimnIkuXw9ffby7ATE7NI-LRU_zOSsdbc1Xj5ZAwNfHGrttoBpdDdeoh8EqL86TvfoLQs4aYRoFSWlEyzugANhOU6z3DFVJV4jqgsnJ_aYcJN0xZi4FAIQaHv0p1dq3EE0A5dpfBBnj83mfCCkLHnXIcAtYpTE6YzhB1NiyEO6sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تقویم
؛26سال از این‌خوشحالی عجیب و غریب محسن رسولی ستاره 19 ساله سایپا گذشت که با یک حرکتش روی آنتن زنده شبکه سه فوتبالش نابود. بعد چقدر بازیش خوب بود این پسر. یه لحظه نتونست خودش رو کنترل کنه شورت ورزشی رو آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/29586" target="_blank">📅 12:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29585">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrQRO_gazYn-vkH540jSTgT6JiolnGh6d1q5XfJBQ4UuytgjskqsjkQwCOjzEY0KO4WA5zyv6E9Go2JgoO6tcPIeahH9yWyc_Y2xFSdYFjnM17h7TmamkbdYf8ij-VMCZkWK93VXMk_Vz_t6ipWLddw71uw8e4vJUcOaDWiXFYhxpAlMF-QPdUrhJF989DKGR6UZmtnjOkJ4ixZXYOELNX5NEUypOAN6T5x3f9bLjBnZ4kKUL-GcaGDgujMKsaSwZhvHZMqaZHGyq3IH8hOFVflk7Ci57VRAn7Y_YCPuYqiTO1ph-bc7QrhFgkq7ws_flvw7Jm6DNJ8sr0SzGayiiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در نیمه‌نهایی جام ملت‌های والیبال آسیا؛ فردا تیم ایران ساعت 10 صبح به‌مصاف استرالیا میره و ساعت 14 نیز ژاپن به‌مصاف کرهای‌ها خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/29585" target="_blank">📅 12:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29584">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkgeN6Tt0kVQbDGm2QjSgLP_63RwC7u26ce0yc72PzQwi5WeJwBcPOQQe91pA_tiJoLN94PlULhnUbJ2jh3x_zR_C-1hispNO_g8O2V32Dv7EcHZwHxFlGfrXQQBxivKLky8T9OxsAVNhH_L4JzTbkOi21X3M18sICKzzjxxa708Fi1eKLvd9FvqJtnXxUFTtTYhQa1NGkDk9y0xcNF9nYg1_D1QSid-ArhmLUF1nKGh3zICmrQVlKXFfjv68V-jpmBHfzeQZY0r6kT3yD8sUxNa8P3S9sblOLQaJI7i45tmgvHd7QMU73R9czvM2jdpvy0wy5YR2rZ9AVjQ6sdnXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
باشگاه السد قطر حریف‌هفته‌اول استقلال اعلام کرد برای تمرکز رو لیگ ستارگان قطر و لیگ نخبگان آسیا از رقابت‌های جام حذفی قطر انصراف داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/29584" target="_blank">📅 12:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29583">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GsSaVroKEIw1IRiaUpfA_SwEFbYhdygIfoocuT6K37AMa_LdBbJvMxjhDop_utRGvGtA3LBFbwInRzU5xDhc_yAchr_C9ikjDwSVgicYik32hbhTnKVqDka4e7zC9OhwOkCC7jLiFhV8v0KOqooiWoOhWYtpezlkMQdYt2f0sFzHueFJdHJB9WgUK5-PCDEWv2_LJ3lKfIY-pKQ4umZnbpA6CuSihJvc-CBO_NvYF2j6D9G5q2pe5yw8BR7mrhcX_NZ2vHJWVAKJihXgXeV4HKkegsnt_p2xKm8KmJ9EXnQmkabuvkPzxuJsyIgNTHEX8eK26EPjOkbIqA8YJ3g2iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔠
🔠
🔠
🔠
🔠
🔠
‼️
از تحلیل و آنالیز تا پیشبینی رایگان
از مسابقه و چالش  تا همفکری و گفتگو در مورد رقابت های ورزشی
❤️
🪂
هیجان ولذت پیشبینی در کنار بت بازهای باتجربه و تیم حرفه ای پین بت
❤️
🤝
همین حالا در کانال پین بت عضو شو تا در مسیر موفقیت کنار یک تیم آنالیز حرفه ای به سود و موفقیت برسی
❤️
🤩
آنالیز دقیق رقابت های ورزشی
👟
چالش های نقدی
📝
گروه همفکری
🧤
ارائه فرم های  رایگان روزانه
🔗
https://t.me/+IxmGEx4ep9A0MzQ6
🔗
https://t.me/+IxmGEx4ep9A0MzQ6
🔗
https://t.me/+IxmGEx4ep9A0MzQ6</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/29583" target="_blank">📅 12:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29582">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‼️
فرانکو ماستانتونو ستاره آرژانتینی رئال مادرید که مورینیو به پرز گفته بود اعتقادی به سبک بازیش نداره و قرضی اون رو به‌فیورنتینا دادند امشب برای تیمش درسری‌آ هتریک کرده و نمره خارق العاده 9.8 از سایت فوتموب دریافت کرده است. ماستانتونو در پایان فصل به جمع کهکشانی‌ها…</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/29582" target="_blank">📅 11:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29581">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJ5ElgYlWErQ-FtbrSuG1Y2ktAzI2F3wLwTBM4wrAZ9SpkTIcKgyAapxCut6I1RDTfk0qzSA_JlQJnpiyxplO9Q-zQ_GtAEp89lmC9DDRYbqwR3RRU41QPFFsTMJO3oMTDhkCkNAUrPSVk059HKLSWOvWf6KzuckmGybYr0xDK9aALyCtmECw7uyjDDyWyNdPAqMUV0d8H6xXHbUQlQpMDE8djbvWYm5a8_rao9T3nDQt0VgJNfhuNL-DC1QWjs8KF6Jx_DVAcPTjOcbfkSZWgH-G8CukQQjOhpIixT8MA11eO02yhCbtvL_NOaInLCy2jgzLsz1GfC7U6L486sHRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
47 سال‌پیش درچنین روزی؛
اریک آبیدال ستاره سابق بارسلونا به دنیااومد و با این تیم به دو قهرمانی ارزشمندچمپیونزلیگ رسید. آبیدال سال 2011 هم به بیماری صعب العلاج خود غلبه کرد و بزرگان بارسا در شب قهرمانی این‌تیم در UCL بازوبند رو به‌بازوی این بازیکن بستن و آبیدال جام قهرمانی رو بالای سر برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/29581" target="_blank">📅 11:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29579">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af01699be1.mp4?token=nQ0mDapzBzeXpD4EiN6CBC2-n11NJ8GO49F8XXMAXyXU8ONRDz8EmcNwi0_RUvKcWqho0jeyT2fORD9yO6b1MzqngTjcAjEhhCqn66gLUWlYCcIIGrrXEOSKttXE3SwA2-Gu-aH2s-s8mCs0mSxmgnTB9VqjUD3gadbwErp2wZ6nR_Z4BzI8DJKqjLQx3uKxCBU_kfS7iCqFicSUriN9vXlX-Dmu08e-edqB6EdEvv09MBVQ6zz-P21g8GOXjJbHuvOHVDHbJHK_XSNSDF6es1SvG9ewxlBVgO63PiBkQQxFzio2KY5cpquBKfy7AGQGh_F6IF3A3urXhHsS1zZvn3PdStG8Fxdkt_mkaN8-FVeCUSXHAkxyUvYLQ5s8nTBqS9Ew6_d10MP7Ve2sW2KJnWK91P0fNSjQ9elZSSwjvikFSYghSsbc-j5IpSjad2Xjz0lrA0FMFIZ4K-Jjpb97eIGr6ogjKiwhX4IAdJUM5e8eey7Y6IywuqI6pz7EMl0RHVfXpRs0cWtIKehBn8xJrVfxakuWxC5fboOJJA1G-aXmhQRe9LbaRO-FCx-i92qQpx1jbGI82VTzHU6Feanh7v81u8ldaR8wBur5WX65ybe_V9YrLjSilZxYXsDWHya0Mq2iO1bWKwo5tuZbg9SGqd5pKiFoPShyUGoOg3mCvtM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af01699be1.mp4?token=nQ0mDapzBzeXpD4EiN6CBC2-n11NJ8GO49F8XXMAXyXU8ONRDz8EmcNwi0_RUvKcWqho0jeyT2fORD9yO6b1MzqngTjcAjEhhCqn66gLUWlYCcIIGrrXEOSKttXE3SwA2-Gu-aH2s-s8mCs0mSxmgnTB9VqjUD3gadbwErp2wZ6nR_Z4BzI8DJKqjLQx3uKxCBU_kfS7iCqFicSUriN9vXlX-Dmu08e-edqB6EdEvv09MBVQ6zz-P21g8GOXjJbHuvOHVDHbJHK_XSNSDF6es1SvG9ewxlBVgO63PiBkQQxFzio2KY5cpquBKfy7AGQGh_F6IF3A3urXhHsS1zZvn3PdStG8Fxdkt_mkaN8-FVeCUSXHAkxyUvYLQ5s8nTBqS9Ew6_d10MP7Ve2sW2KJnWK91P0fNSjQ9elZSSwjvikFSYghSsbc-j5IpSjad2Xjz0lrA0FMFIZ4K-Jjpb97eIGr6ogjKiwhX4IAdJUM5e8eey7Y6IywuqI6pz7EMl0RHVfXpRs0cWtIKehBn8xJrVfxakuWxC5fboOJJA1G-aXmhQRe9LbaRO-FCx-i92qQpx1jbGI82VTzHU6Feanh7v81u8ldaR8wBur5WX65ybe_V9YrLjSilZxYXsDWHya0Mq2iO1bWKwo5tuZbg9SGqd5pKiFoPShyUGoOg3mCvtM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداوسیما روز به روز داره خفن تر میشه! شبکه دو یه کارشناس اورده داره از خاطره قدیم میگه میگه کارتون میذاشتن زیر کونشون فیلم رو میدیدن.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/29579" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29578">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRzSBBelcyInq5OiG7OxLv9nwaA8XNWaIPxjGEpFcCpOVChQcJNjP9vUU9-bfUHS0UhSo7xLr-45jpU0Wsj8GjkiyZ19-qMe25TJCbkxiT_doqpJ7JzkfBruRMljDMwkCDY0YAQhgcD63dpuH1NJYMWYyYAU9n_CYgySN2sPlr8VXeplkuGFicSooKldAM-T7H3xTEi48ZDJEp5KzI721e27VgKiGBPf77xFXfxtCblKGpNCTGNgRJjINjcdKbYx6HuqMEulwCgvIbpK4yBQ_JRWDa0rodRyb4l0NDz6emPT_nsD-MLwToSsxazW_xbQlJKMr78Txf48XdnoUlKcSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قلعه‌نویی‌قبل‌از دریافت‌پول‌های هنگفت
🆚
قلعه نویی بعد از دریافت پول‌های هنگفت از دولت! شاید شما فراموش‌کرده‌باشین ولی‌تاریخ که الزایمر نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29578" target="_blank">📅 10:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29577">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJl-Yx-w2lPAd4Qgl05V_2JzeMgwBcQ8TE2rXT2v1-s5lecKuLWWi8G7ROOBNo4VoDqA8vow-1rhX6BMeqUlLuWJY4noqNO-lqJG904u0GEvSoHWL15k2N0o2wCs2KHaNOZB1rdvBTbTCfb3TUoQ6cBhSqaNUKeRJdzJhXgDIK2UtLhq2KfT8ozejbSZqdghUL_nfbrLlBJw7XNUp33Qnx680dGsh9JoCvQhoPVeE9kiI3FPWkqxrx5zmefADrAk6v6nkehw8oHiMgnG_UdKw7JPJHUOrPejNIzRvxhWVgJ5GYgfFA_sBU4nJtjIdm8oBQq6857LK2KoOM7iVUA1AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
باشگاه پیکان از باشگاه استقلال به خاطر استفاده کردن از جلال الدین ماشاریپوف در تقابل اخیر دو تیم به کمیته انضباطی فدراسیون فوتبال شکایت کرد.
‼️
باشگاه‌پیکان‌مدعیه‌نام‌ماشاریپوف فصل گذشته از لیست استقلال‌خارج‌شده و با توجه بسته بودن پنجره نقل‌و‌انتقالاتی آبی‌پوشان، حضور مجدد این بازیکن در لیست بازی با این تیم غیر قانونی بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29577" target="_blank">📅 10:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29576">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6157fe5afb.mp4?token=TM7oyf3MnSBsQHpr6NyLdlEPC4jdW_W7RtR8EgoICjqwGjqZSqL3JAXFvtRsJgyqyO8keUGQyq7gReGb2EMBlKIIQ3bFt923CdnZt-xMFW73KJCTQUsAD0W6RPOAL8NtBHB-q1KfgLeypC7hfndbpqaxzrOGmAG1CX4k7R1gpzqmlYqxpP8VUvmSB9wtReTFnxlegMse8IA2eLj1b2EGADTTgBznYMb_LqCLIT-8o0g9GrUuq1zYHs-up52mAUiN3NeKh7rbJvgNiznMKm7WDBd1Jyn4vTZNWHvM6Tm9lREDyjfPNwtfAa9dFJZtxNLyioFcBCQnb4xbJNFyiArjgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6157fe5afb.mp4?token=TM7oyf3MnSBsQHpr6NyLdlEPC4jdW_W7RtR8EgoICjqwGjqZSqL3JAXFvtRsJgyqyO8keUGQyq7gReGb2EMBlKIIQ3bFt923CdnZt-xMFW73KJCTQUsAD0W6RPOAL8NtBHB-q1KfgLeypC7hfndbpqaxzrOGmAG1CX4k7R1gpzqmlYqxpP8VUvmSB9wtReTFnxlegMse8IA2eLj1b2EGADTTgBznYMb_LqCLIT-8o0g9GrUuq1zYHs-up52mAUiN3NeKh7rbJvgNiznMKm7WDBd1Jyn4vTZNWHvM6Tm9lREDyjfPNwtfAa9dFJZtxNLyioFcBCQnb4xbJNFyiArjgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
دوس‌دختراسپانیایی کیلیان‌امباپه ستاره رئال مادرید در فیلم جدیدش بنام "Drawn Together"
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/29576" target="_blank">📅 09:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29575">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2108b760c.mp4?token=M5OJaOGmbtw65_HthZpahDX85SNpvFCpf6Rpl36IFRIAKFoaK84AUVEyiKmNMUeUg_iVGzzInocW9ZF-u7J7r7jh81fwGotFmMNxYR6gJ0VtF7tKCzYH5sx7SA1Lp7tH3UGzA6O3I2mw4aX5mnHXNKpomsIAVKdky5cTLnb8eP9he7Uv9-ZCzlsdjHTLn41VzBC6BHOKE8jsyyW6fLVQ6z7eAlIGsmUEgsHMnmrhn02bm4fF8MtaFb8hgSMRD-i6N6FG0gx7QDQH5xLGdDPtJrgoFepyVpFPRofio9CPFj7TbXzRoixrhmgIL9_y2ukcjEraZiwHjouvmTTWwOLOORxwZ4ZHq5g11PmG9g-sbcc8c0CgdeNeN6G8gRcRsZhJAe0pjcbOYxIADet2AKDULBJdB5na3qDR3kJ7-cwKfw8tYm16I2-JEdyQvcUQ0aKdcYb6Al7tpwPU-XybyocwdoPjI3geZLcv_r3eKZH0EyQ5dJP0mPJmoY-ES1xfmxtZ5RPUxwd_i2_S3Sb4ASEfEyvPVsbXSI_iVgEJbERk4CsQihXmJwpAbnvXABQKJ-BbibFRvfQLVVkkkv5J1UAO9ep-Qe3lk8ubTphmqOmRJGcBkLDSISyxbJLCadZFyMXUa1iuGKBUjAvsQ6gOpWomFtA-rzr1eeIN_-OIYmqcxbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2108b760c.mp4?token=M5OJaOGmbtw65_HthZpahDX85SNpvFCpf6Rpl36IFRIAKFoaK84AUVEyiKmNMUeUg_iVGzzInocW9ZF-u7J7r7jh81fwGotFmMNxYR6gJ0VtF7tKCzYH5sx7SA1Lp7tH3UGzA6O3I2mw4aX5mnHXNKpomsIAVKdky5cTLnb8eP9he7Uv9-ZCzlsdjHTLn41VzBC6BHOKE8jsyyW6fLVQ6z7eAlIGsmUEgsHMnmrhn02bm4fF8MtaFb8hgSMRD-i6N6FG0gx7QDQH5xLGdDPtJrgoFepyVpFPRofio9CPFj7TbXzRoixrhmgIL9_y2ukcjEraZiwHjouvmTTWwOLOORxwZ4ZHq5g11PmG9g-sbcc8c0CgdeNeN6G8gRcRsZhJAe0pjcbOYxIADet2AKDULBJdB5na3qDR3kJ7-cwKfw8tYm16I2-JEdyQvcUQ0aKdcYb6Al7tpwPU-XybyocwdoPjI3geZLcv_r3eKZH0EyQ5dJP0mPJmoY-ES1xfmxtZ5RPUxwd_i2_S3Sb4ASEfEyvPVsbXSI_iVgEJbERk4CsQihXmJwpAbnvXABQKJ-BbibFRvfQLVVkkkv5J1UAO9ep-Qe3lk8ubTphmqOmRJGcBkLDSISyxbJLCadZFyMXUa1iuGKBUjAvsQ6gOpWomFtA-rzr1eeIN_-OIYmqcxbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
هایلایتی‌خاطره‌انگیز و دیدنی از عملکرد گرت بیل در تقابل با بارسا در فینال کوپا دل‌ری فصل 2014
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/29575" target="_blank">📅 09:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29574">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‼️
گئورگی گولسیانی مدافع میانی سابق پرسپولیس و سپاهان درسن 35 سالگی از دنیای فوتبال خدافظی کرد. او بزودی در لیگ برتر مربیگری میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/persiana_Soccer/29574" target="_blank">📅 01:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29573">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcHCj4Cwzo_8Z0HZjCFX8G0Spg3OpcyL6a6B3rTWRKHtv_tQuuaK74bT_Q-a9NKQd416a-lDKB1h3HYqOOTlYgW7rejLBLFCcG28iCb-doFUCUo-66R3KXGVA8QH4Rv-XtI8t1c6f03SIFqba8OSHNFMQxiCdJ1ofOazqEzjmA9PM1BalOptVBLNLz48aNpzU3pOJohgaYICsZrH7qY3yfDLfmKgB3bm83wlFOB2lWSpAxyt_MBAYdH8awtG1gp3_BEvYjadqE7Edg9Wkls3C8j0L18IZoN1fFDCWxpQEJ9ri_mR0E7BkAh4bqDMi2pl4240rfMD8MFPlwGI1PwsJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نادرمحمدی تو روسیه‌تبدیل‌به‌یک‌سوپراستار شده و هرکجا میبیننش دارن باهاس عکس میگیرند. همین روزاس رومانو بزنه: نادر جون به آرسنال هیر وی گو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/29573" target="_blank">📅 01:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29571">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsa8C0SR8Ank2MVE_C9J071HTTnGSA9ef9dgyLulpnix-bDGYMWWb36ErLrnyM05LGkH8eXINBUWcqhIrIGB7KWwNySSnvkEZTXdtd-4XAgF_rP-0ELxRUT6FbUJRayXuS3eJoQV5vuc3UxNz4bn9AkwB4R0-cCkLkXkGv1gqxDxOBnhZ6gYPMo0F6ot5fIHigEFWQ03e8wX3-3e6_MKEBVnjNQXZh2u5w9RCMagpiTRYe5irxbnCRuSWcD9NSLyOstiWCYiY72d2P7Nta5AP6flow4q0-oQ1LVYx5cFYfs6AfpALJJquzDnIQ-JTOPB726COJPZX6Y7FwYX1FIgYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین گلزنان ایرانی در تمامی مسابقات در سال 2026؛ سعید عزت‌اللهی با دوازده گل زده در صدر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/29571" target="_blank">📅 01:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29570">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHgf8qUkumeJMI9pXebB8BObkRo3Z_7Q81ghIaZN4HpDliBWPG9xCWt70fv7BaEnezHtja_4HJ8DKxbMeK-hjFzb7BNpS7rLJFpJtQ_58FWFCYjkHpif1zR0TNKt6DnXYL9hBFQoHo_WI4FUSdlQyXzhLapRh6W68XZn5GLdkVDqm68s0hRap7boy8p2nQ4ZMIA2jfBfFBg8_DOOsBQTBNcKkNHraKPCns3qtvmrX9z0TWLRFPF7Pf_yZDk5vnyu30dYUAAopeJNS_A0oOqmb9teZKwrP3ryhAeQ7HmBs6jAOIbHcAk7-MaWl2ah9GYHr11Hf56rwhecZwX2p31a3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ سهراب بختیاری زاده و نکونام سرمربیان استقلال و تراکتور به شدت علاقمند به جذب شهاب زاهدی در نیم فصل هستند و حتی صحبت‌هایی باخودِ این بازیکن داشته اند و به احتمال زیاد زاهدی در نیم فصل به لیگ برتر بازخواهد گشت و راهی یکی از…</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/29570" target="_blank">📅 01:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29568">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDSNfzZN7M-VlpNidi4Q4DOEaeH6_-cPLeigcwpIWLMqQIrSOoPXR2UFPfBvN9Y5SoCMAzj8KFxuzwF8D7bjHiSjIkBkUNdJHQ8eIJsqwJmrR1zS7aIxH7h6dGknjzxEyqhV4NpSkfsXPG3fJLyZ4t25ABxF5loLoWL_prEEbSQxTN8P--SwO-X53dsfZFeGYqQDDTbcehPgjeqOdM6lFgny8nYsS3tZhIygR-hRHJ7gkXr2HokxMrNe2MubZhfcjoX2I6qgNSB63PqDxX25s6gBU_pS-WokNiXyhQD0ti7QZN6hohe4psuatKmFXCEvglYzIH4C7gVjXklKiEvftA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ فرانکو ماستانتونو وینگر آرژانتینی ۱۸ ساله رئال مادرید، با قراردادی قرضی بدون بند خرید دائمی به تیم فوتبال فیورنتینا ایتالیا پیوست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/persiana_Soccer/29568" target="_blank">📅 00:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29567">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FhgD47ytaH28wKUxX7h-ZoEGGefOgWA_803FvJz-3rWAfa7PjAmPE17VI6nvH-arFlai2xAwpNSCO9GtuFQIEACKxfISUbG1Vl6pzHOiauF02KHU5T2GU__XDJpM6wBBuC5bBMtPhZVQQSq5usnIyS8kUbQcmFdFR8KHDtKJmaJzwIO8fQkYNre4oimCO_RLYHj8MAF6ifbJPig9WibNuaXWusi7eoKm5HeGvbW2E6mV2u9XuBzphZE4DN3Hf9CCVHxA5AdupEyocOcK-tip1dNuIXn-PFPt-nqmd_uPVn3oJzyhUPn1-5PSRu2phAHLbW6e0oN1YAaET_VDa2KnvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ اوستون اورونوف در جدید ترین پیغام خود به مدیریت باشگاه‌پرسپولیس گفته اگه کادرفنی به سبک بازی او اعتقاد داشته‌باشد حاضره به‌زودی با حضور درساختمان‌باشگاه قراردادش‌رو تاسال 2030 با سرخ‌ها تمدید کنه اما اگه تارتار علاقه‌ای به ماندن اورونوف نداشته باشند…</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/persiana_Soccer/29567" target="_blank">📅 00:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29566">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7a6b08f6a.mp4?token=jmNNwGYp01oGi7VB59r7FHo4qHbOnCbfJ_6Ymm6J2YocqBOt9V-qC9PIWKTqH0Mr01nL5oz_1sGrj0x_-Ocqa3Ix3hbRNxIv8A9ueCIPry9CRWQsNgBCzimLi9C9-lUhydf1LUq6f4eFWYAc_AhTe5yv82LMkFY0y2jiIGOhCPEJCrAJ-nxQf2-239VV36hes7j3QHqUJIN8KeV2oPfkzpRKHnbH7GGGraM3l2iwuqSroJfWFr4d_jzxK7-vmV6Lq6WWk8gGcOWqwQ9jHdO2qHqBHPG8rkqwYQBzLO9kXLS2QuHAolzBZkLpjKVQh5ymwn94Rf-Ef8JCmspwe9xbvYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7a6b08f6a.mp4?token=jmNNwGYp01oGi7VB59r7FHo4qHbOnCbfJ_6Ymm6J2YocqBOt9V-qC9PIWKTqH0Mr01nL5oz_1sGrj0x_-Ocqa3Ix3hbRNxIv8A9ueCIPry9CRWQsNgBCzimLi9C9-lUhydf1LUq6f4eFWYAc_AhTe5yv82LMkFY0y2jiIGOhCPEJCrAJ-nxQf2-239VV36hes7j3QHqUJIN8KeV2oPfkzpRKHnbH7GGGraM3l2iwuqSroJfWFr4d_jzxK7-vmV6Lq6WWk8gGcOWqwQ9jHdO2qHqBHPG8rkqwYQBzLO9kXLS2QuHAolzBZkLpjKVQh5ymwn94Rf-Ef8JCmspwe9xbvYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌مهران‌مدیری‌به‌گرفتن وام‌های‌کلان در قسمت دوم جدید سریال جدیدش بنام «مرد سه‌هزارچهره»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/persiana_Soccer/29566" target="_blank">📅 00:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29565">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGfpPcuCSOAutCEltR_gzl2t4E2l3dfTD3wQSu0sAgwZ9EDTzgW0LHaaczQ1DbV9mqGblPyg8hAoZtFgkZ4GZ8Qtbo3S6gTB2I9_3gxkHAljb9aWSrBJNkKMxGWh6md7zhOVKsf33Ocb6qJneyeefyydoawaSPz4u33F-iSFNTmbr9Jc31hqjcQKRAVTfHSwoXdVXzUyCVt23mlnV36Rq-eLzVvQ1wD-MVePYzLlW4vOktbDI4BO1ocS8Gm2oh-C11Oqo6cEHVFN4R1Zglc_UJkgREoDrlONnADrpE_Xc4rU_Mrq5QfwKO0bMo1cNoBleRKU_ufpsQYGhZ6BRJdgjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز
؛ از جدال توپچی‌ها با یاران گرانیت‌ژاکا تانبرد رئال‌مادرید با رایو وایکانو در خانه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/29565" target="_blank">📅 00:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29564">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvuzBPgvhf6ddBlYPhvlwUHqqDd_llo7XyzAvXxYcvyA4yHTXjtLkQYCccr5jRjSM9NdNK3KT-340YHSNDp9L2vbFbA6VbJWf8bTp6GUGmm0Zsnw8Y0XhurdTEfszqJEFmCxTRCHRCYFjXTz5MBZ2OlT7ZLIsyCTRW81OJuqb22yo4KorBCPKzgqf0RMazDrrCtDQ3hXfHsG8XXIzqojr9-G9isyKOgqvWgU9Ke4SsgeGX5A2QIpr3V8WlUkp7Zo87YUDlp_KwNXeYXmdqn2SQ0Lm85udB07VJHpG1w4yGoFTD4aovMo_e0h1Aw1VOmq2A8Y80i90xzzlO35Huq60A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
شکست شاگردان مورایس برابرالوحده‌وبرد اتحادکلبا با پاس‌گل سامان قدوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/29564" target="_blank">📅 00:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29563">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHevGKcTNgo92SPgVotS2zQbVJgET3R5b3hvaDMAH-49yZDFYeerZir4H4DwvPJ1JclDH6H5eA4kLcNTA04zSpcuEeNpssVu5RWSLrN9XPuaJXQ-7uNekRpGFTmWg8ItNCG8xQDlKgqiVdzf7s5-VGDFLNIGGZPbOdE3SznD-ZfkYVhw1HkdhuN24uST6hpZyoo2bANyYVL4bKZeN_qLiHgmpHyXSoRadgH9sOlLynodvVs0vbWGaxI3P6LTa_w7spbBC1wrxuGbZ183cDS9XrDpGewgXjjzLJaatQzHd-sbE_bxCnwsPVb-JNK3UrvU69zKdA4XX9SQox6jkP8yEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دروازه بیرانوند بالاخره باز شد؛ گل اول استقلال خوزستان به تراکتور توسط رستمی در دقیقه 54
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/29563" target="_blank">📅 23:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29562">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITLOfimVa90MPOQN5Z1qwdikfSRYLYXmkrddNxcoRtxTRaxfs2RR0F8XTAJ3-UG1b67G94mZsjaErOq4cygkS1Qyg1mz9F6yvjCwI_-jIZB9LCQrcULhuVRDv_-7sMWKcZDhQ369urgsWjicn1WX5e4eJZsiJfijkEZP3En337zk898iQYJ2-X0BaZvhseMNuouferv8gmK01EBCdhggBjZt132s4ItM3YQPGSSlUTd9_9VJVZprLo1Nb_Z0TSPRN6-63nLmB_yO9G5k0CV4dig2nVJId_P2xbn8ESqdYulZQt4g3L-6wU4s7ZfRHD2ZktLFtjcbXp_0tuNpyKLgSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ رقم دقیق قراردادی که نظری جویباری و محمود رضا بابایی با فابیو کاریله امضا کردند 1.2 میلیون دلار بود که بعدش یکطرفه فسخ کردند. حالا 40 روز فرصت دارند که با این سرمربی برزیلی برای پرداخت یه مبلغی توافق‌کنند درغیراینصورت کاریله به‌فیفا شکایت میکنه...…</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/29562" target="_blank">📅 23:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29561">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a5ms6kMe9vld3cQOCFzaKRVQ9Fcga2M0Bu86aXZ7wHcbGMnV6dQTqI2hnBEVhfNeHEXNvOCVKQnKBqQyDbGyqDhexv8SmiCbxCrIa-bmUzASrCA-XCG6dKE6G1lXkWYA5bR2ESx54q6tXzoKL_-W0TDHxwQNeR9z65TjOjiQPAGttfQEEC3laN2j_wtxVP5mhY3gXVJRek6owe9JdV6YRniV2tYZvG08zonsHNhq2RT6EXaSgqnLuWLQqKKKRhBF7Vbk237EDCPUKbuQt84gTWs5EWwMmErymoK9IPGbE3GIyBvI2tYNnklhiRwOGNX77N9Wsrt_UOi5c2IigmCnMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد فوق ستاره‌ های فوتبال جهان که اصلی ترین نامزدهای‌کسب‌جایزه‌ارزشمند توپ طلا 2026. امشب‌بایرن‌مونیخ بازی داره ببینیم کین چه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/29561" target="_blank">📅 23:11 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29560">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQsZfgkePYgSqrlxvApleD19AWA0PZ6GoWCto9GYrf--TKzaDz-v0QBnhweliCHu3nautS8AKcoYxkvrlnl88Y2d8nLo0KJ3KOEA2a39WwLTRIZ8kiHxQvXHMXoOuIMx2KWqXYfh5eBsY7maed-kazTz_P9lY_77MA61PReU_Jg_MWcTqUeFFnLZg7Zz1M-GOmF9QYsGcC3coygcpDVW2Iel5PWX1BKfIY2H1drnv7EhFlgl1Fv2tkoKqMw-JDpFarHT2LG9bVcovQg1NIxkg7364fsZh-A13D_AcOaButcJqlK4k477dm4FBK5Ii_g8yKGoLCVGhW6ynIVOUl-p4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌ های رسانه پرشیانا از نزدیکان اوستون اورونوف؛ برخلاف ادعای رسانه‌ های ازبکی باشگاه تراکتور تبریز هیچ گونه مذاکره‌ای با اوستون اورونوف ستاره‌ازبکستانی‌سرخپوشان نداشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/29560" target="_blank">📅 22:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29559">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzczJhdAJr7Ogamn1xniPc3mp0FAsuiiPR0uRL95a2ugqhTEU39bNZ9wj8R8cHdJ483Na98MAvyPPP8A1kgGMkW2kwXTc1lxyBadENivEyJV-1bJ1dQzGYJuTZV85Ed9IxVPrLKC8xifXlyS4pvDWbO_9G5T6jPoqUzxCwUjKM9VzHSSaMTSe-tQK6xd2Dq7-TzWsdn4nPpyx7JhUc6dfS81kGbnRFa4B08pKjFjsHdy7CkLkJ9fDPZ__-6td6MLJ-G3na_fDg6bBTJo2TN1DZR3HW-TLDIAup-UloQhooZIIhhbxVQzWgV4y13Z4pFj3NrqQJNmgdKr_-E8kWVCcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
طبق‌اخباردریافتی‌رسانه پرشیانا؛ در کنار جذب‌بازیکنان‌جوان‌لیگ‌برتری؛جذب محمدجواد حسین نژاد و مهدی‌قایدی دوهدف اصلی‌هلدینگ خلیج فارس درنقل‌وانتقالات نیم فصل لیگ برتر خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/29559" target="_blank">📅 22:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29558">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6e36c4c43.mp4?token=NSJSiD-JeVJRG_yJSFHu-X2RhVXCGcYoSqkdb-w6RliMyVNh0OSsB0J5FGmqeOBIu1CV8kde-98zD6-4nWFHIZQTtXyvPtbcDiktzW3r8dF8l5WHtIUQ_vpy4rIHNiuQT6Y1cmGiHDjD6m7tVB3UUYcXkc1obV9RvUG4zgNKZ8BvTnVE3kS_ZqRH2sRt3hGVltCDPFtd_WtSpyTaeCJLCzrHFsDX2g-rl68c9I1gPSv7rBHiulY-DvFAJSiYnjsVUnhWd4ybM_wJGKo_W-0y0No827HbXD5Ly-9mkLQsRLkIlNx2Zihj0QEqxMcJsLWxKc_JSYSq6O_s70sN8aRZ-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6e36c4c43.mp4?token=NSJSiD-JeVJRG_yJSFHu-X2RhVXCGcYoSqkdb-w6RliMyVNh0OSsB0J5FGmqeOBIu1CV8kde-98zD6-4nWFHIZQTtXyvPtbcDiktzW3r8dF8l5WHtIUQ_vpy4rIHNiuQT6Y1cmGiHDjD6m7tVB3UUYcXkc1obV9RvUG4zgNKZ8BvTnVE3kS_ZqRH2sRt3hGVltCDPFtd_WtSpyTaeCJLCzrHFsDX2g-rl68c9I1gPSv7rBHiulY-DvFAJSiYnjsVUnhWd4ybM_wJGKo_W-0y0No827HbXD5Ly-9mkLQsRLkIlNx2Zihj0QEqxMcJsLWxKc_JSYSq6O_s70sN8aRZ-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
صحبت‌های‌انگیزشی‌رونالدو دررختکن النصر دربازی این هفته این تیم؛ نمایش یک کاپیتان واقعی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/29558" target="_blank">📅 22:29 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29557">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpDIdtdM2wHnYllzLcmapCqkpD0dXFT99r790PqbnKubui9NWK1y9-UUZejFoaa_Z71Ew0nIZgw1Skr3l-94MVtsFUMyAQvfSCUqIk1Sxc7k9o0aaquwlZ1W4P5ca7azn2BoESgFOEcesbvKv5HpbyaC_OU-S8qVtjOCrlaTmONWKbA1__0OtGMhVSGkMp-9Pf5wxgjt24Xlg1AnEiR6Wr_hNNCpQ6INuZtL9ne0IsJqBpgnF4d1a1olU2SBvVNAehLbE91csyfMb4tWEFKHJ6_uBsyIg8_1r2FFgnBd2LyiNYeHPtSm4ka1QomnRJtDoM3OeQ1TD0CiQw-P9ghfjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هانده ارچل: من از بین تیم های اروپایی طرفدار منچستریونایتد هستم. علاقه من به یونایتد به زمانی برمیگرده که کریس رونالدو در آن حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/29557" target="_blank">📅 22:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29556">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSVepYkO9DFI7wV0QRGyJCM0UajwuGG9vxAib6RXiZdP9diEqmc5DPpQbzVN2vLLfh-mUthb63XgHLyjK1MfNBoYawauStdfFnYKu517glezqVAW7rzbGQIzdFsRYPAGYIiwkCjTLbGo07OAQydp_azFt3CuEXkaoRPZdLHO8UMBKDULBW5yzbgHsy79W4x-UoIWD8VLYFuARIPSOMrkjo3lCpdnRJVAdoSfCvigNq5q1QzBU7OMAC1Cq9yw9L7oDuEkec8Vc8iaVSmvKbdiSmO7Rzw7tdepD5QCbhzB9LJTLoRjKxD4VwQOAQxql3NILD63Xbfk_Pdm6rZbse8jxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌ های رسانه پرشیانا از نزدیکان اوستون اورونوف؛ برخلاف ادعای رسانه‌ های ازبکی باشگاه تراکتور تبریز هیچ گونه مذاکره‌ای با اوستون اورونوف ستاره‌ازبکستانی‌سرخپوشان نداشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/29556" target="_blank">📅 21:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29555">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IONScXsTiDtafldrta6aOz_IDhe9NdnOtf5KH4OHS8uGJHm0U-J5AkzUY_fAqj2IPvE0khvupwXLlG4wUnNdm48_gcwRPlDdoJEZl6I2YIRvpLyF5nYFaWIRQek4U1gpOoj62cgCh_oGsfvOD2sEsnNLQL5-NBbtty-O5tDsRStF0d2r-wjoEcfVm8o4__Q8eNT3XJPjQNkUch1mARkNkkBDs8uQR_vdtQuqMoVg2htBdBZn_MnDgoqupS_JE00HrvNvW3jWpniLRtVQ95BMfp7OB97EXnKB9iSnXF5Ufzk5if2gRVrzJqXHgdjPAhRP5sgx0FELyHjCtoPhb1Busg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص آخرین وضعیت اوستون اورونوف در پرسپولیس‌دیروزتوضیحات‌کامل رو دادیم. در این حد بمونید مهدی‌تارتارمیخواد اونقدر نیمکت‌نشینش بکنه که خودِ اوستون اورونوف درخواست جدایی بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/29555" target="_blank">📅 21:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29554">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e054a17dd3.mp4?token=YG5rpCMCCRTubl4bjqEtSd1RxLoK5ELMhM7YK-2QAmtKBo-iSOU9ifONT-b3sOlXi-8eTa5xjdIHlBE3Xg68OkcYG7hWL3jA-XQ1QCrVfG1njyDCIELltQ5-2EJEXp9y3j1i-poEsMS9if-0kbPcO7Ul921N5nr9G8Q3jYY5yI0MsYc9TpfJMBJ5atPMNSUYyXf3_KDzZK8k7drIF0rNnFgSaFyiD-bUri1Q5-pmRB4oeLdJK3oCuVxwq1B6pneZnl89HKPVKlc3zuMJjEXXG3bO3p2uYxdGb5RP4NUWmrtnyFxmG_uBpCh53IDxXQcAW5wqRxxcYB56eKxV_ZhEfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e054a17dd3.mp4?token=YG5rpCMCCRTubl4bjqEtSd1RxLoK5ELMhM7YK-2QAmtKBo-iSOU9ifONT-b3sOlXi-8eTa5xjdIHlBE3Xg68OkcYG7hWL3jA-XQ1QCrVfG1njyDCIELltQ5-2EJEXp9y3j1i-poEsMS9if-0kbPcO7Ul921N5nr9G8Q3jYY5yI0MsYc9TpfJMBJ5atPMNSUYyXf3_KDzZK8k7drIF0rNnFgSaFyiD-bUri1Q5-pmRB4oeLdJK3oCuVxwq1B6pneZnl89HKPVKlc3zuMJjEXXG3bO3p2uYxdGb5RP4NUWmrtnyFxmG_uBpCh53IDxXQcAW5wqRxxcYB56eKxV_ZhEfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمایت‌مجدد مورینیو از وینی با یک ضرب المثل جالب: "تو فقط به درخت‌هایی سنگ پرت می‌کنی که میوه دارن. به درختی که هیچی بهت نمیده که سنگ نمیزنی. به درختی سنگ میزنی که پر از میوه‌ست."
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/29554" target="_blank">📅 21:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29553">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aac2a8bd0b.mp4?token=uJeyR2avfxybZ_OkbGUBzKaV7BVxLMFo0jQmja1_0soEB7kW1df-pUyueLEwIEvrklLEwWB3-QbSkdBcMxzCG0hT9CqR-tY3f6yEz1CqmcUD20F3TJTWb6GczdEV4uOQTxLGuOhl6g5PPy-zY05ShYwjXKmiUgmP-T7DHmB5cMghYPg5cu22zA57ieEWiRxwXq7sOcsDI60sP4mr9ZiCOK6H4LheuZtmSLa91Z7az5whLQ0qkT9fM8exfXLjm-9uPehDVZPVh13KUhCfIyntIrZOvCn-vlt_XnI5g3FlDSRzf9E4Y7o0yJ4Y_i-lUzOhAgTH2I800aK2nBx38ismtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aac2a8bd0b.mp4?token=uJeyR2avfxybZ_OkbGUBzKaV7BVxLMFo0jQmja1_0soEB7kW1df-pUyueLEwIEvrklLEwWB3-QbSkdBcMxzCG0hT9CqR-tY3f6yEz1CqmcUD20F3TJTWb6GczdEV4uOQTxLGuOhl6g5PPy-zY05ShYwjXKmiUgmP-T7DHmB5cMghYPg5cu22zA57ieEWiRxwXq7sOcsDI60sP4mr9ZiCOK6H4LheuZtmSLa91Z7az5whLQ0qkT9fM8exfXLjm-9uPehDVZPVh13KUhCfIyntIrZOvCn-vlt_XnI5g3FlDSRzf9E4Y7o0yJ4Y_i-lUzOhAgTH2I800aK2nBx38ismtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌زیبا‌وتماشایی‌ازدفاع‌های‌جانانه مدافعان برای گل نخوردن تیم‌هاشون در مستطیل سبز
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29553" target="_blank">📅 21:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29551">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4uPfS9GFZbQlJZxA24oBeRReS0sSzdj9AwMq0ejEiZItzZneZmSqX6zOgkT-WdsM95W4Hqz78r-32Pzzwy4RFvee3pJfHKb7AXzcwX7-PJtG2jcT5OXkT0a_NSTmG9aXoBor4ifSe_ajTXC0l-oXtEMg1VE71LTbGLGWK8RQ8DBOXogp6c-WJ9Nkw1kLhQcfblTKcwSkK_XqVlO2Jbdm5-mNBSV4BnqNZqkHReMPSdz96UCX-_XXrsct1EseLQN-VOOkCxXuGLeY40k82bSG5aRBtN9YKGj99ihsVrv8wedXk9VqMYKAn1-gA0XCOacgJZ1r3cvl6O1Sb6bhi5-pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روشنک‌مسئول‌مسابقات‌لیگ‌برتر:
بعد از فیفادی و بازگشت تیم امید به ایران بین هفته هشتم و نهم بازی‌های معوقه هفته هفتم را برگزار خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/29551" target="_blank">📅 20:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29550">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‼️
کارشناسی داوری دیدار استقلال و پیکان و دیدار تراکتور و استقلال خوزستان با مارک کلاتنبرگ: بنظرم باید برای پیکان پنالتی اعلام میشد. هر دو گل تراکتور به درستی افساید گرفته شد و گل‌آبی‌ها هم سالم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29550" target="_blank">📅 20:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29549">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_fvkyBvXJK5PtTTc2nzyymbukzz0JO2EDoQKNofz3eMsyYWyTA4LB9bUv-ub9hrp5ywfQwZVxISNW_8kOip0XbTzj9jgnYpsEE1Ak0dyCyrOihRLvt0jX4r3i1ypt_5hA4OiEOOOlbjgwtmIyNqNp1Isg_CK_4_JuR-rUjd4lts2_gUNi_OrlpV9mS-7Cnl9RaQzn8mH3yWBMVg0XFJebYLeEJKLKJ_TYVot97nBMvbtgKxS-q3ohLyCdOEc0TeFiQk7xBYWKAE5ttRlWP8EBej8oIVe0x7pGZiOEjG_xs1ghVZeiY7ryjhFVSD3TVsUHnjkg1lNXNZFBvAFNKysg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
نشریه‌فوربس‌گفته کریس رونالدو هر پستی که تو اینستاگرام میزاره3.3میلیون‌یورو که با پول خودمون میشه حدود  910 میلیارد تومان پول میگیره. در بین تمام کابران و سلبریتی‌ها اون بیشترین درآمد رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/29549" target="_blank">📅 20:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29548">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hd11GCnrLkzAVVMkODTu6PQKLqdXa4eQRyJapGViUQu_vVW2iWbdZZIGNIty818hCutrZueTwM7GA88PbKRmrnLKwGDqQbZs2rqdywWQO9Ydi0iAVA_JvhzVVTzFSN7Hp2eUgcHCzHyKwNnJg6Ek9rwAPyAQQ_WyEGw0oIzt5Be_6h_WvLw8lGyunINsI5D0vL8yG92u2JvvGHDBh_VPQ8cmd6lBxz6QuQ4dBSwe5LYdGwn9lNyedhH6vfG2TVn3Hf-D26pILqJDua4mW9oYzTS--Ez8VO8iiY-Ql5n-ROVd7SF2z-9GuRPevubS9JRY-_t9ZWEghGA18B4Q_Si7uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔵
#فوری؛ فابیو کاریله سرمربی برزیلی به فیفا نامه زده و اعلام کرده من پیش نویس قراردادی باشگاه استقلال رو امضا کرده‌ام و درخواست غرامت میلیون دلاری کرده! گویا پرونده استراماچونی دو به وسیله جویباری و محمود بابایی راه افتاده شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/29548" target="_blank">📅 20:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29547">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGRhbaL4GePkJklt8zfKt6Qdp3sTXGyRkhcpP-vuhdn6Azqp8q5cTZuZ6PdW-r6JiQVk4u4Mntwsq1ugFC6HlSF18OUo7gAAsSFjqEq3ujTSEEAMDFUoG_b3z0n7hRhvwyFihmDE-nVi1ih7xa1Q4kZP5zMwPken1znyoiijCE-RRftvxDbEXituIuUubtcMR1KBIjM95QoL8RqPvwPCuukivi8siVoaZs25BiqouV3NPXbiq02UKVXi00eHd65NXlNOR23zLpIj7j2FqhQA8Sw3PjIQwdjTKh4tpFQyugwhD7eIgdAIW-Q--_NG8vwx1L3R7a7NYrVneLBhXarZ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
رافینیا دیاز فوق‌ستاره 29 ساله بارسلونا با به ثمر رساندن شش گل و یک پاس گل در چهار مسابقه بعنوان بهترین‌ بازیکن‌ماه رقابتای لالیگا اننخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/29547" target="_blank">📅 19:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29546">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNdb8KyAJTIYB2-yPwmuI_CTE9o1p-db6PG0hLm3TjppQS8y5U4JRfdES4XTgMppxDmR19uIFj9G-8K5694_ostZPEFZD5A6J106hk6YMlQwMovIAEJWNWwD-H-F2ebCzNO3gPqCZq-GFIkUfPNGluSOMpOZQtiQ52-KwoN65b-Qlr2a2GY8AIx8kPO16XmK8olBdfiWyCZr6a6WMEMPUcgXJlkNAVdh9_PsDSPdbNod3BPhLyR0-Crzu5e9OqN0TI8WJ94KEkaVVo-k16igFuwNsYEiO6hkC-2HVKU1sxwssmEmbVd3RfJLUuZA6_f3AzPRJABLW7Sh2C44fV8E_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
‼️
علی نظری جویباری مدیرعامل باشگاه استقلال: هیچ خطری باشگاه استقلال رو در پرونده کاریله تهدید نمیکنه، قراردادی که برای فابیو کاریله فرستادیم امضا نداشت و فقط سربرگ باشگاه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29546" target="_blank">📅 19:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29545">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9jmdL3nadJzYJ3qRa_3Pr7NcYbnhLmjQc0B3twqVfIv8bjOse7uXLvX_1ywxMjES4odMrLTL-CR-bwYXNSF27HmWHbkm-2u_U_sygeTpplJAsG1EOV_Udr-7mezbwp2IlKw43M4n7nHwNqOoshIGHYUygnPqr4KHhPClftgXVB7eNER-YnvhyFal9lhbhnmStwwg2Wvp0NGzkPsz1MD-zei9TpFqCbPpQ0U4nrxSK35s3JTQgHpjI-DbAeOr0_p6gsglIb9UPqBTjJ_RjM52D-QYspBQ60ugjoAWi4EHWyxNFoGlqk9lMYZfAQxjvEta6H3tbz0rRXtEgWg6sMP1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
گئورگی گولسیانی مدافع گرجستانی سپاهان بزودی قرار دادش رو با طلایی‌پوشان فسخ میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/29545" target="_blank">📅 19:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29544">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b50d9kgeYvQyyEaO4w4AKEy41UKG1PxH3mn72yH8mTYMRfFPCLdU1pgHD4pQDa1HsR1aHs-GjHcWedTm1r2PB3pK33Vz3sMhAIKb4zwaWNX47Pbgm5bO_ssn7gYIDIdjUsPq4vxlCpPJQsD60FuSlzVxaY1xsBenkmBvwL3bHRHtcbeKAivuPJQgvzFa2u3D9BfU-06yjIs-vjp7i5_8gu0KBSJBJBZWyJpdR0NOltq44nYT89nhlldz8s8q0Ogp7FzVRPBEHq6551oWLounQmhmF2Ja5aedPxaWDDj8UHU_3Fc44JDY0BHebd8Xd2KlRywOo2drNTXhl5zQ5oUtZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
نشریهESPN:سسک‌فابرگاس و میکل آرتتا دو گزینه‌نهایی‌فلورنتینو پرز برای‌فصل آینده رئال مادرید درصورت عدم قهرمانی در این فصل با مورینیو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29544" target="_blank">📅 19:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29542">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyIwYFqG2VIIM7FG-uH_oARyS6hN_rSzJSyuFLybwd4mDPQ7JO4AhR0bozQATXSTPe7DTSdQwm31j4N0_EC5P_WUBggP1rYPKwxs8AJwpVha1QVuf7I-WYAiv7960KGEoUfph2IDRlWewWbMColbXnwRLpJEK0cDj68vm1yyGt_3VDc6mbqjdRGFDANDBNCQiQjaavap-_OPUAiQl6ZwewLHQVeTZ7OENh6-Sxj7jZj_5aZDVhhGo_C-Q1u7tRF29JpxJckCKX0S1wtXmLQc4UWlUY-3sdQ5teLrM4MieaIhNwxG2cTYjhCYaVUhuGAx_jUGvRsoJR6kP0H5GWpcjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#فکت برگ ریزون؛ تیم فوتبال بایرن مونیخ  12 سال و 9 ماه‌ست که در مرحله گروهی دور رفت لیگ قهرمانان اروپا در خانه شکست نخورده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29542" target="_blank">📅 18:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29541">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6Mti1bHeLJihdTXc0DhI52siYC0StmqGNJnHJPeK3VmSEp_nGxjSAU3J3QeCeTFDLeGymKZVr2oSFoCvRSo2IIw27-s4AycIYTb16uGCol02DUB-Ns6wghRR5u1aGdTUbepQxgkXYDzvUWF7XWUVRrqAmUR3jaraAKKKEFdGcNYduh4Z_jt9Y9ta8vRnZtXC6FiX8pnVEhecPxQ7oTznDWv1Nu2aayaiw0x7iypC1evSFUdZer5pgMvffzxJdWL771Fx3tvajT0368b_FIIXKZfcelji2TFcpntZxnphO_I3cEScwO5CsAs2U0zmnjnHWwjYHq5febEm0I6ngYuQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
👤
#فکت؛ ازشروع‌فصل‌گذشته رقابت های لیگ قهرمانان اروپا تاکنون‌آرسنالِ‌مدل‌میکل آرتتا در وقت معمول "۹۰ دقیقه" متحمل شکست نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29541" target="_blank">📅 18:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29540">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPCv9KP_mWJrbaq3wu59gyvAri44MdB17ZtrYdAaRb8fRBmDZF4mJmZiltdUblYgwm6BkF0ZrGDPNe5Jijid0_KME9TlM_EhCrEOEpWi71U7-CBSEV0squfTiWz15Lrjt3tFALN_KlnmRq5NsoUqYIGHE9li5Mu-0B8Ty_C3g4pe0NzLgV4lM0HeSl1BJW2FSQ_WfQb9A1Lh_xYFYId6_xqb5bciDkMKbV-9Fwbu7Qb5dEOeJar5aK8e_GxOLU8UOOzIduzfxQ_D3A57JAPNzvaqR3PXElG2hS1AwpJHeYgigUbsvc4HPEQ3sqGv_l00XqhnGWKGDBDUNhepi30Qyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در نیمه‌نهایی جام ملت‌های والیبال آسیا؛
فردا تیم ایران ساعت 10 صبح به‌مصاف استرالیا میره و ساعت 14 نیز ژاپن به‌مصاف کرهای‌ها خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/29540" target="_blank">📅 18:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29539">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57bb43418d.mp4?token=Vq17-IQAO6mKEtbMDd6R_DjdZMem3IEFUEZRIaOgammzfnb6WmJ8JWrZI4raUlaCCkEY3KFn2l__Uy3vRTgBAHV5wVNNvgrBNb_LIW8J3X1Pv841w5_dD_LxFXiWPePaPH938Ju5gLVAEzutGVzDoaNH48NMqWfTHfT7A0ouEPVp-l_nsKHFdaWStzFJlxKAq-SKaBNNyOUsy8HsJScCZkpFK9Kiq49dU7z2vWEQUIVsIvlqPQL2j082xvECzMYQq3v3X2XpfpmeZ8RkJugFGH8WIx1r3JTgEHgAvf4h2mjON0yBSjZ6vd6yztN3tSernmbAle6N31pm7N3B4CNUyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57bb43418d.mp4?token=Vq17-IQAO6mKEtbMDd6R_DjdZMem3IEFUEZRIaOgammzfnb6WmJ8JWrZI4raUlaCCkEY3KFn2l__Uy3vRTgBAHV5wVNNvgrBNb_LIW8J3X1Pv841w5_dD_LxFXiWPePaPH938Ju5gLVAEzutGVzDoaNH48NMqWfTHfT7A0ouEPVp-l_nsKHFdaWStzFJlxKAq-SKaBNNyOUsy8HsJScCZkpFK9Kiq49dU7z2vWEQUIVsIvlqPQL2j082xvECzMYQq3v3X2XpfpmeZ8RkJugFGH8WIx1r3JTgEHgAvf4h2mjON0yBSjZ6vd6yztN3tSernmbAle6N31pm7N3B4CNUyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌زیبا‌وتماشایی‌ازدفاع‌های‌جانانه مدافعان برای گل نخوردن تیم‌هاشون در مستطیل سبز
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/29539" target="_blank">📅 17:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29538">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlZEh_Kn2T8MLqkXju1ovTgiwJukuTjAgECqOFSEZyvBKR-xEKBzUhPekMbzgAVMeJ1g0FslTvSnHk99WF-2XzoU-19YoVJf0ZLXEftTjSp-0Y5efSiiWPYpRoRAUv_VrZlN0WCOJLyn-UuQpdVlQbrBZdIHuGCV_v2h6knz5NK_wI10S-0B166DCtNk0HP-7eMG5IkgY0vz6G3BF68o1BdLylVrzwxkhquH43aE6djY5_F7nP76jy2pdEa_DkXt6nKRnphJFoocj64T8RI_GCN14FlFSiMTqYsEro4F1dQ9r0aP3ecclg_40Z-SnXTKeD6YE_t50dU_2-RIhAz2-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌مهره‌های‌هجومی‌استقلال
🆚
پرسپولیس؛ تیم مهدی تارتار تاپایان هفته‌ششم لیگ‌برتر با دوازده گل هجومی‌ترین تیم لیگ بوده اما استقلال سهراب بختیاری‌ زاده هم عناصر هجومی خوبی دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29538" target="_blank">📅 17:27 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29537">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8dddf4f36.mp4?token=hD3fdOy7d2h-DmV40SP2Qr8hayMiSizZl7M3nVAkDZQKipEE-OUV72ZmScKuHUcP_Rk2n6cxZ9r_zyBwxXEieAXGXDxXctIee03s3djrzNqqOlY6PgQEvmmqBMYbM-B3xEIb-mS5WZWaavEXu3KqLnov34yO5Uko9HVSTiltegis7okb6MVWxxJD-GieGSQVT4hWKtkbZABQU9StY-CucTAEZOgqFWCbc8EYc63hZL7bk1lv-S3VesLlFp55B0DiOc2iZ0UrVz0Husx8sQrWamZJNNjpFa9WfQ4-tcsPBy8VsUAeNCZeLLZFT_10gjlh6go_Ti8MoSulQ2lkGrqcfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8dddf4f36.mp4?token=hD3fdOy7d2h-DmV40SP2Qr8hayMiSizZl7M3nVAkDZQKipEE-OUV72ZmScKuHUcP_Rk2n6cxZ9r_zyBwxXEieAXGXDxXctIee03s3djrzNqqOlY6PgQEvmmqBMYbM-B3xEIb-mS5WZWaavEXu3KqLnov34yO5Uko9HVSTiltegis7okb6MVWxxJD-GieGSQVT4hWKtkbZABQU9StY-CucTAEZOgqFWCbc8EYc63hZL7bk1lv-S3VesLlFp55B0DiOc2iZ0UrVz0Husx8sQrWamZJNNjpFa9WfQ4-tcsPBy8VsUAeNCZeLLZFT_10gjlh6go_Ti8MoSulQ2lkGrqcfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گلزنی دوباره شهاب زاهدی در بازی امروز جوهر داراتعظیم دررقابت‌های‌لیگ‌برتر مالزی؛ این نهمین گل زاهدی در تمام مسابقات برای این تیم مالزیایی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29537" target="_blank">📅 17:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29536">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bp-WOd0FMzVM561AxoAJouTgYAhEI_gO3TYi3VNncKAMCGDz0gvelLy5j5Es4GM1k7FAFRqaHmZakbWWZtJqx9UgXNPXZXqnoF4CzA2wwvGE35h4XqejZiBts1gDNdXlovMy4ER5vgmXwjIce0jLim69SyXuhyrZNBwVifkmGukInpokaxkEjSuiGtsOM2tKLbTagzb4T1PDZLTLXyOmRmEYwlG0T-Ljy-oFAQ3giru8ZpcBwUEVzadIAHuRkF4VMMqUZxjKy5j5cxE29NIf1IUTWFojmi7vxVGysLKiIXeRsUtclllRHqWUBauuFMklJeUpuOfEHF5Iqjzxr4GXNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتیجه کامل دیدار‌های امشب هفته نخست لیگ قهرمانان اروپا؛ از آتش‌بازی آبی‌اناری‌ها در نیوکمپ تا پیروزی ارزشمند آرسنال در ایتالیا وبرتری لیورپول و پاری‌سن ژرمن مقابل رقبای خود درگام‌اول رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/29536" target="_blank">📅 16:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29535">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YeUjMqs-5Yon-adPjp4ZBYrVRwqKwpircvIz11ZN6xb_t45HdIK1m4k7yr3qvigUeW9xyuc1e3GIaTIIIZW-ckIXDU8UtR6-C7YBW2bpFFEgkNuBCdNJAsnB2-0a_MQS5KKjT2wzBcldc08O0iks392ENYp8cQ4MEbEbVUvg-nDupjw_Nbm_zOuj8PpAvQLg6gpKHyEY6BRZ2T13NUKvJBBmu5qikCmVd7v2fve4Zz9WZkQd3UtqgG3Zv36D-dkZcG59odrlw5vd814FZZ5yM-oqXUROJX49qecp_YTMWFnoOueA5hfNGLqFurobci-pRu9_hwYZahPCDFQZ19Xm8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کار انسان دوستانه یاسر آسانی با خرید یک خونه برای یکی از هواداران استقلال از زبان وریا غفوری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/29535" target="_blank">📅 16:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29534">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEunXtyPnqBbCQYO0d7zCEqOAh4t-PcjCXqwIF1Z4xW1KCnZtQIQD6DudOLuwnmcgMsJcSOgBCK9QOOpvjgGBkazZ0xyxNvFO4BNIiXeLJB8rEUAQkQ8ydPC6yGn8niz3U5B1UU5gttYPRQirucOBX0Cty-HDjjTVzaLL697ICDedmA4ypZuEAIR_-QfUkITYmNh7OFy5gX9NLH_bmT4q0Kwj1TSgDRSiC4F_IEWbogFbO_pEYUFSDuEcJkNC7ptIbKrGP0VQYH_0sC5NmanU4DO4sw902VNyKQIGlCaONxZt5ioxBqyqRBdxnQjJH731XObbpoBbtnoeg2Xc2JOHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به گفته کارشناسان؛ علت اینکه فوتبال محبوب ترین ورزش‌جهانه‌اینه که شبیه‌ترین ورزش به زندگیه و دیشب یکی‌ دیگه از این اتفاقات افتاد. دیکتاتورها وقتی سقوط‌میکنن که خیال میکنن دراوج قدرتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29534" target="_blank">📅 16:11 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29533">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAjTPazLoTJo1jAf5Zq9t-U6A6Yz4KhPdl2h-KeyGRkhh8Ynwd13-txbWKMN2zPumqvh3gEX3kAaepavn8OVCo-ouEl91oUmSqhsYk2tTY7OnDz6j_cqAWe-YmtfnIOIxDDVdE1fFHROsdV1V9f1Eq9MoEU_blgOwP9wxw5INHkYN1Eq0tB6vPSbB2xfc6OT4qntFLMula34Zv9mSfMnyKb0n0OFb6X7kQg3Cx8bCMz1Cwu0x3c6QmDWCW42Xh6WVQ83YkTrcZZjQYVj0c0aOrULNRRum8V6CKvCGHgKZVVXYuu87MHPJ_SYuZC23nbtQSyzDtdqVjO0hZzjtXal-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#تکمیلی؛ سران باشگاه بارسلونا به این نتیجه رسیده‌اند که میکل‌آرتتا سرمربی‌آرسنال مناسبت ترین گزینه جانشینی هانسی فلیک در سال‌های آینده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29533" target="_blank">📅 16:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29532">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trj2Y7etjZ4PyOmLx1jVQENuOLmV_zr7CyvF6r042cCI7GrorwP5_veW-9Ssr0MECOMajYB8iWE8hCe8KKQevX5kGCNmTHWXng1FwpT5qOCUP6V33Ru1c0EqCY6XEA9OigShbwne3j-xeKcq4Q5KBtSnDl8zT1MHm1G5YwFNqJsaeAHlzXu28V2pv-BmWd5zadlYRimrJsJJCnDBSDZZJWUhMYX5f7rBBrifO4L2fFxUSm2xF88Y8x3eQWROIi5nZ0XziQQVEmmpKTKiuUHFH5oh5VwssrQ12Nc2w33Txupd61FLkxiATgGxX1IQWtX0eQGZ4rOhfGFvlUABUCzwfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ بارسا در لیگ قهرمانان اروپا؛ رافینیا و فرصت تبدیل شدن به بهترین گلزن تاریخ بارسا در چمپیونزلیگ، بعد از لئو مسی افسانه‌ای.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/29532" target="_blank">📅 16:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29530">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oORQ7vET_48mACS8QPzmjG0MBvEgmnFrAzlmdpRuPJ3XFg-8rsVXPlOPhbNfn4geH6esQVFy7QWM_y2hqFFR3yiyCSjqMwYZAYBtd_QAKOTi__usN1PVRuoFqZcXAh7A2KNtddzbR2FEHKaMKj-8nBOVfmHCqoKxFhHUQiAgJIEjSgxhmVYvgxTsQj6hFL7V2FEQZXU8yQjfD3qdrqVfiBysSmel3AjcQ78_FxjcNYgMIDKkieSbpxt4j54OlG2uvJOh7Yboo0LSei9-krW8VBffIB0uPN_hJuyh0t6-toXhz2E3lzk2sD71ZgiPoDiGI9d5PtgiikMLs4xkH3u2SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛مهدی‌تارتار سر مربی پرسپولیس به کادر مدیریتی سرخ‌ها اعلام کرده درصورتی‌که محمد عمری تمایل به لژیونر شدن داشته باشه با جذب عباس کهریزی ستاره جوان و 20 ساله آلومینیوم مشکلی با جدایی عمری نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/29530" target="_blank">📅 15:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29529">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XkZ3U9SGOVyGGXHyGhwy2IWwd6W1R0VtKfla4uJ-7cp2B5awJzpUBGRbiwJi-NksjhJB_bjYQU0X9j0veVbaJoyDy5riatkpgeMy8294vRSg9KISfEx5BYJ_ybucAPsgKBR6E07ZlJVugZ-DBjmtRYlbxtWQtsjtddHjNW2j4yjqxsxc4MNR6cWG-_27h7tfueZEFlMcEKtMK3LeUliUgjyFUSk-e58BimnuXRMJL9wvVE-nVuSr9aMZuEk6m7QDt57tRnlx8ZSfyd-OmjBYzGU8ckA3j0xOoG_58JdOb5mkNggpntE85g6gFsMnuDL8dwDX5YzhspBJ3L6YBlFkKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیکه‌سانچزفلورس سرمربی کهنه‌کار تیم آلاوز به عنوان برترین سرمربی‌ماه‌لالیگاانتخاب‌شد. سانچز در دو سال گذشته بارهابااستقلال مذاکره کرد اما بر سر مفادقراردادبه‌توافق‌نهایی نرسید حالا با درخشش در آلاوز بالاتر ازفلیک و مورینیوشدبهترین‌سرمربی ماه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/29529" target="_blank">📅 15:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29528">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHE5wsQflD-SpO82Oe7oTfmYspK8MwrV44d8Vlq0HIRIDt0-ejXfx5N5wbRTK17wDuM8tdh88nv8Bd5MOEKcuVhwT456BoupLs6ILM2Q5XcevxeZMwp_p2PAgUJZ3GlixsyiOhxv0vUJGOVXcKgy_knejKYSRG6ckRwoF5EFFuik9QLCJkRkNY72Og7GFMlQhIZQU06fpc2Cn3Aq9NimENmJfYu_wtRFnhtCek50cMpVPGkXg87K-eaCG2IrKizv0wJbAsdK1toFawBHXcQMl3boBtMuknZ7gfFqrUiCt3rTU1OMNNniH22x-TSrqru5SclQR8wf93ckb3ZA-rxxYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌رسانه‌پرشیانا؛ صالح حردانی مدافع راست تیم استقلال بعد از دیدار با آلومینیوم به تمرینات آبی‌ها بازخواهدگشت و کنار گذاشتن او برای همیشه توسط کادر فنی آبی پوشان صحت ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/29528" target="_blank">📅 15:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29527">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iiiwewMHRd6VJ_7bre7qKEJn60GCcsS1nvOp0yDw8ldEem0e1jck0Z0JU26ML_1J-Kw20K1DFpeqGY0S0oSOAbAVKeyGtvWRfjtUKuj4HEO-Fjzeu07ZOT5iLK3I6Wnzz0w8QqCi3uk1QNqWSKKSzUPoE-oUvCZzhyE2XpVJApmRtVmrOmwnpU3LRZp8cwmxKWG2n8ibM5g81MQVhqjScyJ652JBj0mg3u5OfGdgeKfKpxSIEyE1TcGpOhKAnQYoILtVh93VyK6DGmwJpJw1de-sziBgdETbjl3hUSWhIMHgLz_byswm-WuKpw9hzvmJsl8flfIm8HQc-75x1HuLjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛مهدی‌تارتار سر مربی پرسپولیس به کادر مدیریتی سرخ‌ها اعلام کرده درصورتی‌که محمد عمری تمایل به لژیونر شدن داشته باشه با جذب عباس کهریزی ستاره جوان و 20 ساله آلومینیوم مشکلی با جدایی عمری نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29527" target="_blank">📅 15:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29525">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yz1ea4k93XMDIAhjqxeFcezbO2kylZV4-zEqUw0Kj8TKhJkk9V_8cFMUJYbw0c3iQDJSJBzKupqsJnutiA8cZouajrWvjHNBRzKJ4-b5QWmt-OAuR0L5GLY_F1ZymuCNHwJOVXeMAHOk4QPkLbprFcY0pK1cs31uP_PIGLk8RBwaB3AwwLUvQxQ0GAA8-uu7Tbg36Iz7VrBUtbkNhv3rS4FLeG3_yJiKalVc37i1O6wr-woYmTZ2NFdqkLQguwsGc2vI8dhEi8yGysBWZaIg2vO-7bMLh-NXs8NWrg7VuTnpV_vBXBqV8QyJCfBItVklrTS72Z4PEBnarI5U90BaaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
برخلاف شایعات؛ یاسر آسانی ستاره آلبانیایی استقلال مشکلی برای دیدار با السد نخواهد داشت.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29525" target="_blank">📅 14:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29524">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNMiDnoqPebyx6zkKOnejIuMBZZLn7POq_290TO9cVY2uYDEy0it2l1wUmw-E1d3YqbfIvblZLWCy3q9Iv1pqxKXQrb_-Gs7lKsq6fJSlQmyacU7xBtUJbX-RevG_nVSsh0rMOp_rrUcEseJ0B_30bDX4vL_YiEwQDBM5Pj6LovpxGCGdpYvVHBgfafFu6LH_-m2jsp27mNf_6esExcwAe1UttLOBrjBnJqJKod1u_waPxbcgZP9NS__KZprztBlRbi-dS9kaWw91dO11dtKvg8D1GLbl1gdJvF8l97yO2F6heDXHfVNEidBigK5M4RKntPM7AM9pCfJ067g4ub2iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رئیس‌باشگاه‌فنرباغچه:بااستعفای‌اسماعیل کارتال مخالفت‌کردیم و اجازه‌جدایی به او نمیدیم. حین بازی دیشب یکی‌ازهواداران یه‌بطری میزنه توسر کارتال که باعث ناراحتی او میشه و بعدبازی‌میگه استعفا میدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/29524" target="_blank">📅 14:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29523">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-c6yIjp9NMTvvTBYf9cvBl0IWrZD5mbqlsVSKZ1rRpZf2vqsZDTOkvkCfi9XByLEzoyqG_QXfw9ob80_FDHBFzPGQEv4yRuJoFJ0BaLwlS8GsfUzAMY_jbMJ1MxsMda3ETPX-YaeIbzmOJxBra9Hg0D8eEVC-MFvDgg5ZvvqaHA-UGV5HG7sH5epkiRbaMyaflAtPHauETuH_-3OCZi55Gf_TOgSoOU6x4_mAp5YC4K4utiRCiRbn-fP7uixHw0z9RPqbZ03ib57oWS-CFxU29fQxujIiCZxFdmmzQrlJsa0q3KY5sYBALTk4KzsS-ByFzjyJKZKLjLoYL0kRNMfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوستر رسمی باشگاه اتلتیکو ناسیونال کلمبیا برای خامس رودریگزخریدجدید این‌باشگاه. قرارداد خامس یکساله و به ارزش 1.4 میلیون دلار امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29523" target="_blank">📅 14:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29522">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZATBx0eO-bQTrteEKFN3dIa5Dkq4ryhpquFgv2SqI1z0fZe7nLb7bREtypjZwDcwJXw-fZaaAtD5XHd27qLxitnJ0MogDoMQN7I-Yas1qTLGUBbAuBZz4P697VS0FnraN1HUojHXUq1jes_l8Rt3Hd7iYlJf_pMNBsZx3D5SXWeFPoXQPYhGLw_v425ppOZdWP0joGrzAUUrPR6zj0-EA0TPXBRCIojg-_rTco_-Aev0E_3A7qQ_5X6UhMbXKLKrVqDBTxavj6TBEVBXlAfPtA7Nt2ccXdcvwwsBosYbCm86OxLX2uW8UuxP2KycEjXA8SvxsENZExkdrnsvD9P9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
🇧🇷
#تکمیلی؛ مدیران باشگاه بارسلونا بزودی مذاکرات خود را برای تمدید قرارداد رافینیا دیاز فوق ستاره برزیلی خود تا سال 2030 آغاز خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29522" target="_blank">📅 13:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29520">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R8go_zJF9e9SHPIq8tI8nJbIwtcLRp_JbjzQrAJuo_N0WGPITnjd1kY25tanE19WaqA0Se88a6jfzhPq1RzyblLE9Z7pzD4uP4LFULPOq2Q2XjkPW9nQiPmKUAoWpYub8svUBZnxOMMiJkgPffkKBGwfhoIiAVcyUXe3v7kwMBmtBXonoa4dBH4rIBSIeRJl51mCbyfuXmAx1TDTYi0g1CE9VlLkCgNZHmSEX1J5XYL36jlpJt6dmX3mHFBnoFtBIq-0tbgpRXtVOunFEK0-59d7vU90Ktm_5H3JfHHB0bOTCCNEOhDKJrZeFNr62B203y9aBlV13nsMKzeIRceUDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MO_DwijaNxKZN4viMngKfVces7zK_LEWqTsiw3RIhXo4dzm1nPKL2_1r5rmbB-Gwv_LvceDAbEC6gw7Iunqzh6aEtM-arDwP_FLg8z9GTSVWmePO-KR6KayaZ3B2gJe5y5AQysfpnjySpUmputp-eOwytK-KuNq7wlHDTQbTytiAUkLRbRdeNSBzQRfMayV-tFpvYOwlzEaCFKnzosLg-n1FEGX0yKbHzT-Et_uoNTE7PJ_oCyAmjIDbEbsM0s289cBE6X-Vu2hcYFF37Wo8O6qJOWbDjWHEMirSTUBX3Mz4lmmocNGwVSweczYfjkHhRLZtixuuL2c3bPRZ0Yo0bg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇺
دوخبرنگار شبکه TRT SPOR که پیش بینی کرده‌اند امسال بارسا قهرمان UCL میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29520" target="_blank">📅 13:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29519">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gltxY1TfVkhv-VsKCHlvY731449nTGlg-MwXfP7PvU8v0V-OwPph7H70ftd0Wg64ayDXNSpGeEU5TGYLRw2NaJRsyA1PC7w8fYFSkXTOutzmiXHVMtj-XuPDPL9gqbbRUy9oKgfHX9SA-oGpMQYH7lVodvQOQkVw96vGvhCK4RwqkQ6CHvStFjW4kK8AgxLCMhvvu1qq2qSXVFi3u7BXu2fUttfF2tOacaU5v2RmgqRuQJ6FP4iz7f3Mi11PqCeLJURhppbqLVfaRJLbZK-lsVHB8rF8iMY861m5d45yVxzUQJHilTVZqJv8O3gWE11uwBbDt3oo5-4J26A5lxuAqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇴
🇨🇴
خامس رودریگز کلمبیایی باعقد قراردادی یک ساله رسما به اتلتیکوناسیونال کلمبیا پیوست. دستمزد یک‌فصل خامس رودریگز 1.4 میلیون دلار امضا شده. خامس دیروز درآستانه‌حضور درسری B ایتالیا بود که دستمزد باشگاه کلمبیایی بیشتربود و پاسخ مثبت داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29519" target="_blank">📅 13:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29518">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyUuxTzcVcatI2xaD_ecq2VQW6ax6h4d_XTyB3iyUURQ3OD1bjwN355z5llr-CXyoqJtgYGJRz2VhyGPMmn-RCIM_z9nuwpZ1kdYHDYimOhFbk_xJguRQMUI1GQkaKLlRdyth1zLW8gR6Gt8OrFNBX3J_DrLgpQdja2pEF1Nzu9VKwndRhrBG9aAZ659t3MIhzrsv2lUFZlG-cocB9CuSaXowFaKmDH7FCDzTSxqPWXkWLk5UuTfpwEcpLuuPnh8dAYKVGiwT_CMfGLk_M9qWAYCKguKMiBZDxpECrJR4JNJNxmrmktXnEIUOgslIi1O27uCOOcPvuA-xgFXdzNVsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نهایی دیدار دیشب استقلال و پیکان از نگاه نشریه متریکا؛ یاسر آسانی بهترین بازیکن زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/29518" target="_blank">📅 12:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29517">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‼️
نجات دروازه‌ برگ ریزون آنتوان گریزمان در بازی این هفته تیم اورلاندو سیتی در لیگ MLS آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29517" target="_blank">📅 12:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29516">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRSgo6qZKvW6mAeaVwyfq2kjzWfiMxpbMgzPfWlj9zF2IpvmFJZ5qlqvE_KaqRJaxQsFFGq3f05DADU339GG6QtL9ovFgVFjtGrOQlnA3RjJNezMnMmEVYnEakORUBNy0e30VfDfEafFueWjGeHw263342-ZsfMSO1zEMPk2LRyedpHXJklKxB8F9ltJoqzqec1VuVQS3hk_A8akNiV_WZpnArt-NMmOfpqpJPHjlYxYXWiPbzJ7aVbvOncQlxvKebAaCRrzHSaRj1zNrMneyMl7VgsYJJ2b-raLD1HOiLjU7TQg-RvtKnUXwWV7hko-zZTIe6773Zi70usTyQOGtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
بعدازتساوی‌مقابل آاس رم؛ اسماعیل کارتال از هدایت تیم فنرباغچه استعفا داد و اعلام کرد دیگر هیچوقت به این باشگاه باز نخواهد گشت. کارتال هر بازیکنیکه میخواست رومدیریت‌براش جذب کرد اما نتایج ضعیفی در همین ابتدای فصل کسب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/29516" target="_blank">📅 12:12 · 20 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
