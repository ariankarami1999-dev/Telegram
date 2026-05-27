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
<img src="https://cdn4.telesco.pe/file/uS6TEvX0AbxU5_4YZmbrIq7ZkWqdW4qxEZ5NeWkd99gmsj0ktVpBvCR8-CLPxXIeYF3jhPtBYaNBp4Z17n5W0Pv5sDi1M0Z-MrCjfg6-tUJpxaOgxILINeygu2W5ANrANIqkKhnvfwDCwg1jOL10pfJrYhAwX_WcoF94aKARMQAH3qzizQkHbN3JBsOCRu64qV3XhN6M7zJ_jSElJh1Y7D0u4CehuOcnIh9rHLTTFeuDm2gpyvaKrG3J-4jABfx--m1klgMVTEUBz4OBm027v9mOjU8Xi5T5unHeHYwcZnl4AwcAOpSdS-IY7TMT4dr1CfIhqp9kt2fHIE9he9IczA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 187K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 17:51:40</div>
<hr>

<div class="tg-post" id="msg-22349">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dt2JHXTTsDq61iTwnFHi43kK1g-p4jDmagEufJT7asW-Mi_qTGtHwjBl-tMKa2ERuEQQMKVvSto8lz2jAvsMwrovcTSQiiik2-1KLhEAg1XOvp271SNQ0uPMSMByiYoIaFIFQxdC2-Ba7gFbhA4blqGvw7H6boM9qEjyaplDOT3SaOieP7JODuMT88sHRBsclE9CLJTMpbmE_ez4z2yeFQWS7mfCu_Rn0ruVB0gbcMjU3LP0fVwUNwStsdXe3twLER5fHkfS_hQcOeJgfkSwd7w6YBpJEXoPOpgDeKxg-XDUw9cuTKZSC2XCkKyZ2gi9eeqg4SCa_g0hpJK-BTd7SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#اختصاصی_پرشیانا #فوری؛ یکی از مدیربرنامه‌های فوتبال ایران حکیم زیاش رو به دو باشگاه لیگ‌برتری که یکی‌از آن‌ها شهرستانی است پیشنهاد داده که میتواند با قراردادی دو ساله به ارزش 3 میلیون یورو به ایران بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/persiana_Soccer/22349" target="_blank">📅 17:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22348">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6d0b75c07.mp4?token=JoW2_AfTlFZOevBwXY_23Qhc-d_tkCYkPxrBGR7YNGSspKUmpLoaCt-YRdXi9f_jjRWzao9r1_PXYEeCt0mIj25i_r43wFRKdTkp-kGolKSlrO71-LjLjnr77vKETkdmE4jQn2tjhmZEI4PY4vB3e1dxnF4L60kEo3mWMgcVc9tYqxjNO5anB1ogG2G7ijMRIJIerksjgon85N9TYOdFK-x-tt_R_gC2XIQFydBLRuuo18OMfdiLRaZ1B80lQPq5IjRXbrEOi4RmKrrMI2RAL7OKtLRKciguQgYjGefKEUP7rQGMrDP-nGTIsRSaCx3x4bckLLKmsAg-EuXLIXhbKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6d0b75c07.mp4?token=JoW2_AfTlFZOevBwXY_23Qhc-d_tkCYkPxrBGR7YNGSspKUmpLoaCt-YRdXi9f_jjRWzao9r1_PXYEeCt0mIj25i_r43wFRKdTkp-kGolKSlrO71-LjLjnr77vKETkdmE4jQn2tjhmZEI4PY4vB3e1dxnF4L60kEo3mWMgcVc9tYqxjNO5anB1ogG2G7ijMRIJIerksjgon85N9TYOdFK-x-tt_R_gC2XIQFydBLRuuo18OMfdiLRaZ1B80lQPq5IjRXbrEOi4RmKrrMI2RAL7OKtLRKciguQgYjGefKEUP7rQGMrDP-nGTIsRSaCx3x4bckLLKmsAg-EuXLIXhbKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تنها 15 روز تاشروع رقابت‌های داغ جام جهانی 2026 آمریکا؛
بنظرت کدوم‌تیم قهرمان خواهد شد؟
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22348" target="_blank">📅 16:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22347">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxlhxWec4vikmYtDbIXItRHSiz_V0Z5cmEqaSJb-jaHg9UIglVJX5vUv-9eF9-PFVIBynzImyDAyespiOMyuw9czq21TCBlAvCijCoT6ATlV8GiL-NnXme0wbzS2sjQCY__7O1yD1fOG7rETUbFUic4Fe_PUHztzvEnDbVu7m6DJuWgtghAmR9y6qCFslhBU7xmAhG_GzRrhMakv7Bpi_tijKzwqqr5TdSizko7Xc6pLyTfBGHh_73-bC9ewLvkYDTyrGFBk1oBRz4hUjzfqiE5_xrgcVvkKW2DGQrrwkblCYyh8Ax6IMAvlEsg_Gx0ztwzZlP5VEvvQ4YgAQE6W9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نادیا خمز دختر خانوم پاکوخمز سرمربی سابق تراکتور: از طریق‌فالورهام و چندتا از دوستام متوجه شدم که مردم در ایران وضعیت خوبی ندارند و اخیرا جوانان‌زیادی در راه‌آزادی کشورشون کشته شدند. جا داره به مردم داغدار ایران تسلیت عرض کنم. مطمئن هستم که پیروزی نهایی از…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22347" target="_blank">📅 15:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22346">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFH1yJW0WXMeCWizC5LHbFHNVYyzYn3IZ-ED18r5lU4U10jzfAyEoIGgDnACogi72mgkNx5sV_y3_vTFQ25abGR7C-pVSfzo1RbYGlufvQHV-V1fiFM87pygqQywj2e9lgDAXUU6HpacFFxK7wcUGPH_I45h-mJWUssNNZBDVvbS1F4JEJk0Kd_o9iQFfs4Imn2Os_YGJD8vAj7leU94ZaEPleGlv5qF0Cp_ByvM6_IOh49nOCxDHqfTWpKVd1VdOCJFXGEH_oVdcZYJ4dXRE-XBY21uD7MXcLLbQT5_tyGTak1U-7M5R_agr4X3ONjYU4dLRKNX0VeNu1khcOlR1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لوکا مودریچ مهندس کروات و محبوب مستطیل سبز میخواد بعدِ جام جهانی 2026 از دنیای فوتبال خداحافظی کنه. این‌ستاره با کلکسیونی از افتخارات از جمله برنده توپ‌طلا و کسب شش عنوان قهرمانی درلیگ‌قهرمانان نام خود را به عنوان یکی از اسطوره‌ های ماندگار رئال مادرید و تیم ملی کرواسی در تالار افتخارات این ورزش برای همیشه ثبت کرده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/22346" target="_blank">📅 15:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22345">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWBmPe_d4xPyR9oYyMcTBQwdqmszxRcMuoDI-ZSh_YWb7xU4KoNgdEGxBhSakNjRhtEIhqGP0ouHb8bbkQIkgMD-Pq9HVggh5FqlR8bmv4nW4gpaHb5_HiAEfQEjudEOFehknNSHm5kpFjyRa2TClxVAuLjFoHMyRWJe7JM_DwaiCfIdG-vhatD_Su7d6Ysu8L70crwCYeA3BPg7eTqi7WeimMXrxxpnmWoWHb-J9J29jFE5hMeIFicPjkw_AqV9taqfmkdM1bRiv9ym66BC7bT7pPswOxbBE6mejfS2GHokCBDJihg1mVqS3Un787Y19WcNba9BD7osdKoij7DFew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی از دوست دختر جدید و 21 ساله لامین یامال ستاره جوان و اسپانیایی باشگاه بارسلونا  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/persiana_Soccer/22345" target="_blank">📅 15:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22344">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXCXlT7yrbtl8LURdqvUcMzlv_cmvmFZiiyBhVbRc0LfM1NPH8LKUKyZj8KcVGxOyPGRG1CcTIwWUB7EI95Zam0rEDXqvvRimCf7bXYNVXkUFExcscncuy7A8hKfOTSAIvYju1UTcO3u7QEu8jPgGUZUiOn6HAngp-D0Q4vtT7Ssq0zN7BCKnLKFr5QhFVQfJ-iVT0-fmPHeqERD03j_-1yxahO1LK410RhXPOvpym6aq1RVYjpQ-pPBnbspE-NyyinZhv4wskO6FcUGljeSRFgY2vPSsLUCNF3AyRfwz5vg88mCoZOv4MmwYV4rd1EZqOUWELIEYHG27FU3-qMyXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اکیپ:کریس‌رونالدو از نونو مندس خواسته برای انتخاب تیم جدیدش‌عجله‌نکنه و درصورت جدایی از پاری سن ژرمن راهی باشگاه رئال مادرید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/persiana_Soccer/22344" target="_blank">📅 14:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22343">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsFjPn8wZNPaVob0Ni1PoAaeCceN4Km00bGrGimnnFvpUFIJAMG5FknJD074vFFVBG5tdUYMVQakX6jOfmvtnHdhvpRIa6IFjppNOcArdoH6pyWn1AiO_5zL7U0ynnsJNNYwp4sq9d8Cw8bhcRnqnSwuFzL3I4xCgQKFsqu1Zbn3HKZNqYnM3dQYWcBg2wo-s3VXCQh2gFatKWKpFGhTFUZKH_naLMmF_f97Qy_5JmiKDciOkGHXSJ8RIHpt2WcPm2QBsiSJKAfqbwkIjrsFerNB7GAc0piAs6ofAxtChFZEbkJhooogiJ4gT9eL_8fLlXDoZm071zfqiqWFbg0kBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کنفدراسیون فوتبال آسیا؛ سه باشگاه استقلال، تراکتور و سپاهان سه نماینده اصلی ایران در فصل آینده رقابت‌های‌آسیایی خواهند بود. باشگاه پرسپولیس ازفدراسیون فوتبال به فیفا شکایت کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/persiana_Soccer/22343" target="_blank">📅 14:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22342">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5e8FPaiqfWko3OzqohdJi6xarX1ALmKk00RoN4NUoHmd1K3tTy4CCGVP8jiRl2TFTw8e1iiRzisTs8QfSy1TPTpxYG736XekY7COaYV5fvnd1sWPvlelORDrIGb9QaFZjsmkDHejsuDSo2-18L_RuY6ZQkG4s2keY-X9ZsjG52Y07Kc2e6XDq5ze8ybJux8tUjOIvduiTNKJ1Ra16qL86QArBVF8v864yXrxMr6KDG6MBdahXy3iVcRJM3Sc8aYiTCLHF2Rc6DeU6yVCGFNEUM6_N8xxIUoGAcyQQJeVVw4TazkLR5HziKAPQZvJLwlcaJ9QKhMLtQZ3spe3K_gjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ رسانه موندو: خولیان آلوارز تصمیم نهایی خود را برای پیوستن‌به‌ بارسلونا گرفته و درصورتیکه آبی اناری ها باتیم اتلتیکومادرید به توافق برسند این انتقال جذاب طی روزهای آینده انجام خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/persiana_Soccer/22342" target="_blank">📅 14:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22341">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SsBJEBq9kXYou_GdvGEokKh2cjeZWO14SqJ-zryTZxIDmJljE0-O1MwzTpHVe995mz_Xe4d7Il9YKW1sv8FOrEdbVN82M3S1vx6pEZyK5U2g5Isa8nQ5C-K5dXpUYbBDbC1iU6uRbuPkGuy6RYCcZqMafpBq7pPu-KE5UQyg3LZoqGLL_fmlOTgjBItpd_IXStkKfhsIFcC8UjDOWYKKjVU2FwdpzSTJR2jlCm3HQomQn7jl1_8AY1YHwmejZ2F1iOJ8ksSkPNkAK_o6qAqNbPGgubjyzhHCjFiIeA6y_oQuT6o9QiOEaKTa4G2nLa7f74ceUvAqTO3k1WMJT4EQKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انریکه ریکلمه نامزد انتخابات رئال مادرید: دو بازیکن کلاس جهانی جذب کردم و اگه رئیس رئال مادرید بشم باهاشون قرارداد میبندم. ممکنه تو همین چند روز اسم‌شون روهم‌بگم. ریکلمه‌درادامه پرز رو به مناظره دعوت کرد ال موندو نوشته پرز قبول نمیکنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/persiana_Soccer/22341" target="_blank">📅 12:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22340">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkT4RhI4x1O1Iq7KBrO6BJEjmqhFkPuZrRzKk5ekNGSHaJTXQ_kFgIRi92Qoma7al_RgoLVL4WfcMxE3PqUeXP4pUHDK1frNi3g-bmKiyyezyMzxrl8ulob6UDXdMXcjbxVEZe6sd_SaBC_XCCoQg22X6UQV9pn9-UVaksUjrTkatX9vecDLz5vBbRJoQY6xVX5QHwufJVJLiWanqp2caZqsRDGsvJgDPgbecDzVmRUhd1d-a2ScvXq0weLBT_MRB6eZ-FIRl4HLT_XqmX8NlbOKXH2aeJ0erejAKjPv5AvY-u_ag7WbCUmKcckYH-ab16WryjEtPwJBvMhoBP9yNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیران باشگاه بارسلونا قصد دارند که برای‌جذب خولیان‌ آلوارز 25 ساله؛ فران تورس همراه با 70 میلیون یورو به اتلتیکو پیشنهاد بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/persiana_Soccer/22340" target="_blank">📅 12:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22339">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljRElpNqKVtiH3LlhNdz4M2uGz_uGQQxXz_zV_FubXynIxhQ5NTmUoERJXyzocsmoaKGDcDUWgdpZA4kupcIHhnFJpEo7_8HEFKfffB0XTo1vjE21unOHX6pkMJjs-nTl6KbcGXlcMxlEt2ydX6Vt7gb0rw4LqxHVRg7UdhK3Pt6t3GlD_z8Tfj1nc4IhxhKRRNWf7qxeI-2ParPgvAcVs-Tzlp7LIeTX0tygOiESXlp61exoUJtgU2eUTuW5NCe6ZvkhJJm_QjZcpkBLZpftuppgnadqELuvl5l1KDnTY-wCzSZkirvYSniFT_mJ7NODxJtQvRIJr_jM5TleE2nGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
آنتونیو رودیگر مدافع میانی رئال مادرید به دلیل مصدومیت دراردوی تیم‌ملی‌آلمان در فیفادی از ناحیه ران پای چپ 3 ماه دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/22339" target="_blank">📅 10:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22338">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlvUWY96dGhwyxHUXyL7H95kmaBc8JGLjBiYm82swTjJDtk6c6l7gZWSdDd6sIHWAiKxHz7pkEGV-JF7jd75TMDAEyutRSr0xgVijKi3dSfwPTKs0sTpJ0hZnMPi-EQQiQtpNCXzF0BYanYXx7wOH6uGNj593nHC7XBQaWAyEM9TXbJ7hDvka28FeCyAVeQccd-tBE8p-NJSsUiRJpdAJegKyoEy6_yWduvsjhuSRWyxIxLdiNyAcJ6dzVdKvtTo_pEoLxEv6BN7aHIEp-QhqrTv9Ye7p3HU2pCeJb12Chk6pUfXsMuhBZf6vngy4wXZwcZP5TPXJXT1HbYQF4R_lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کادر پزشکی تیم ملی برزیل؛ مصدومیت نیمار جونیور کاپیتان سلسائو جزئی است و او قطعا به رقابت های جام جهانی 2026 خواهد رسید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/22338" target="_blank">📅 10:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22337">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4zedjt3e15udnZJXO4iVMyVmmTdhqiXGLF-FSmwvgCK0hGgqp3LZT-HelLjSTYB6FUd_0f_SBcWQZXInq1FCHzzM4bNw7LWzkF6kZB-tq5juYVsYaXmKeMK0f8egd-iVlAL0QA3PfPIqzuyws7J7eE7X6v7ueQi-hbO2xzB40BAJ6zqijVZHv196ltXYGPLKj0Ya3KR_P9dleu-nhhvWnubMdutQqt5vnY_m08RwDY0KnvHmYCdKfzGvQQkjFA-f6INIPbqk_gwvpZtM_kZU1gbEkQnYkEdbMsvQEi5oc6S5kVeQC_AezMgSvuyinPiQrTZx5dqXiOiutPyXA2ekg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا
#وینرو
بهت
🤩
🤩
🤩
هزارتومان‌جایزه‌بده نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r6
📱
@winro_io</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/persiana_Soccer/22337" target="_blank">📅 10:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22336">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/561656d5b3.mp4?token=Kbp9hojtQ3Q1FnPX-V1AYDVexIl2Mbs1pTr1ZwSqeo0FWDhnWD4diGI2ci2jDQbwzfsmxkhbMJ4iPn4en1TQqu_JwhA5tEBG_YRwBsOO9hku-9xNorHtG6WfAji8EwrAXqT2UdN9RYFxWbcpk0rWDT3_HEIGAhhMKQ49TSWqEgFm4ZdFY0f6g49n_xqbjvjMJNHJDCB5tR-E1K4TF-ZgtMf7eE5scn1BcMKI-rseR-wSzSMWa2vCfD9N8f_cM4XoC5uza7Wiplx-N5mni2V-eDLxkYW57W6r8A1keMEPH-5JqKnchzEGj7isvtC1cmL5TFXIHU_Xs0JJzJEep844pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/561656d5b3.mp4?token=Kbp9hojtQ3Q1FnPX-V1AYDVexIl2Mbs1pTr1ZwSqeo0FWDhnWD4diGI2ci2jDQbwzfsmxkhbMJ4iPn4en1TQqu_JwhA5tEBG_YRwBsOO9hku-9xNorHtG6WfAji8EwrAXqT2UdN9RYFxWbcpk0rWDT3_HEIGAhhMKQ49TSWqEgFm4ZdFY0f6g49n_xqbjvjMJNHJDCB5tR-E1K4TF-ZgtMf7eE5scn1BcMKI-rseR-wSzSMWa2vCfD9N8f_cM4XoC5uza7Wiplx-N5mni2V-eDLxkYW57W6r8A1keMEPH-5JqKnchzEGj7isvtC1cmL5TFXIHU_Xs0JJzJEep844pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌از فوق‌ستاره‌هایی که در پایان این فصل رقابت های باشگاهی اروپا از تیم‌هاشون جدا شدند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/22336" target="_blank">📅 10:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22334">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/quIpiXLjBbZLHTjMhKHwE15VA3yNkcqsM7KMkwHTxtzt61szQyxbt5Yq2w366HptHrPqKAtER6CJMbiIknK7Jgvc4N15qPjYn42-WCUYciD6JW0i1DZ2FTLSDxxGP5DBuo2YaGBfBH1mNbO2JwGS6uAHJsBVUjJO6BSiNj0VNcCFAbRbiVEsVh0Jt6Z6AKmq6hVtZiJbSHgyk1VSXN-lNRJcp4hAPndz5IoVfQpwM2E7VPIikq9aH92TsVhpsKDWvHSLXnBMgNCpMQIz97UBP08K9ICuGeNcAQiIypcKiw_bUbgqmX9ZvUueAu3XUgHzOhQkYCF7Jz-E4Uy1xBQUkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qVsK0VzXbXrtj-C_n18q_81z1CB-8peCKvlPxe92itfMHiblWwyP1HVKMdj2Uu4xO3QbF9LJFYXYG05R8BeYcKXBsA4GH0jTgFZ3F8cOS--dxsOnAbrZiLDgVM7jE9fCqjAx_P7J2bsGin4sV25XdzmfmewnWl1e-wmg1JhasL8W_2Eo7wQC-QB7cCf1M28GybB3u-kfD82iFWd9y7yP2_taENUGdtETRcCy3Gm3Pbn9kalOnivyXn7ObKisanL0EH_q-OLeN30ak3tracMhmGevab87VelB2jN7yftVkviF43XU8yyRGqjFoj2nS8xSbInpCZqmPGInMCcKDErrqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#تکمیلی؛تموم‌سرمربیان‌حال‌حاضر فوتبال جهان که روزی شاگرد پپ گواردیولا در مستطیل سبز بودند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/22334" target="_blank">📅 09:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22333">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePh49sNI9ozXd7EDAW2gy906hJDaYgLUtL72KATSAVsIbPYTZ5dIZbNmXMvwpS6XP775l70wg42nFbCOu_a9hpXUK7karyibpzBoNMNiZMhlERqke1s1rEsBfAXn50c9D6wzAlyvV7itvjDto_Ak47lQuTJz_OO__pDv42fLsmW3sFcRFvMhMT-9nE9oXIgmRCexXtGJttcmkrDgcpoj1sZh9YfbvjQJ-HRWZdKGs5yPCMVnGLbPPZ7ZD9Zh2_eqTAIZdoce4ZvpOH1ER-x_Ji80y1XGTDzAay00I-oYToZZskvprTtUHGUp6Pp44KN1EdYBdQPFgXUvinrPPqBuJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ نماینده محمد امین حزباوی امروزپیشنهادمالی‌مدنظر مدافع میانی سپاهان رو به مدیران باشگاه پرسپولیس ارائه کرده است. درصورت موافق با این پیشنهاد به احتمال فراوان حزباوی راهی پرسپولیس خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/persiana_Soccer/22333" target="_blank">📅 09:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22332">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wya04iMi3fDHwsikLbPkR8YnCX6PlohI-NJnFMdsPynAC58CzA4NBiPzg7WSsf0T_VJHv76B2AAceP3wK8nIsyBZyRdzMO0GVEU8rFzQsU5qLAstz2wCinbd4els-S60jSP93UQlgpWp9hKeilcaXo4ArEXVms4RMZy16nTvjfIwHaTEzx4d4yXfr15rplox0Ai-Jbj25XlV1w3g32rYOhws_d46bDPEGEZqjtyZSiyNHqa3uaQrUiR6kQh64ZdUXW44QgSurELGNdKBXo8zxqORoIodHHZMHdZJEuqTIUwtjUKinALNca1hiSNzyEtP9lTEM0wDFAiFH_cyO5OwBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ فوری از رسانه مارکا: خولیان آلوارز تمایل خود را برای جدایی از باشگاه اتلتیکو مادرید و پیوستن به بارسا نشون‌داده. اتلتیکو برای فروش ستاره آرژانتینی خود حدود 150M€ میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/persiana_Soccer/22332" target="_blank">📅 09:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22331">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-avINjLw_pNn_G0Ufw_TG_HP-zz-B1ct3yH-6RqGJMSllQuVV7uDH9zSlUlS5gESZclFgFdifyjqk06JTUhHrdODDlQwii-O6QDwLrC0o5XoS9Zq8lFxJgAuEBG45zvALb9rkHB-LKH9AeL9KrSmuTlkKfhONxCIGSRlgDlyYsjbiytwsA2FUzdQewXolD0dFcdNsGnfSdkj_mIxtgcaTJc13pPuUMq03WiIrcLcLKr-mW-Dq6uO_OYBHiMwiKP1015DTbHsPkDTiEpnQJvWAdPQqg1MpwpT95ylmkaAuYdncBtQVWVFJZbnLbXyRQNO3IMMEyB6EIaXsORtZyBFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین گلزنان تاریخ رقابت‌ های جام جهانی؛ میروسلاو کلوز با 16 گل‌زده‌همچنان درصدر جدول.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/persiana_Soccer/22331" target="_blank">📅 09:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22330">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vt4-wW8JaghtjHkTrQ-xTLLArB4-QBVK9GYok642ZAsbVxDfs7IijMq7UsXkjkRWCZMp1BJA6hOetI4NwO44bKJY3JXp6dCeU4aOt4VqU3d5dHDMYU4ZSUts2ztiCz2C1W2pFLMAM-iwE8RnzCnzkcVXY7j_nfxdBhlZicCiil-D_o4l4veXtnpvqJ7olG2vjOv2ne69nET0dkK6LWMfizfqmu2C33l6lBu17vAfj8junVmy2QYbgcc_4L70vTboxf8J1IO6mjc8EfbaeXbP0I2S14iT6z_Ma2U8VYgIn9anEyc5ZdeHztuWGhGBsvyeMkY_uOOob4HV-IkoL1mZDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌شنیده‌های‌پرشیاناازتبریز؛
مدیران تراکتور با علی نعمتی مدافع‌سابق‌فولاد و پرسپولیس برای عقد قراردادی دو ساله به توافق رسیده اند و بعد از جام جهانی قراردادش رو با پرشورها امضا خواهد کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/persiana_Soccer/22330" target="_blank">📅 02:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22329">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndFq-HjEsF5sIzzLrENNpiANQK2p8-04ngCErs4OkFkYfGCblu-iqmJETXt7DUkxU_x3po-jRIcJ83euvJ6SK91phIT15G79ca-uhgGk7fAacrMcHzdbDukY76zJ79Ip9gq8VSQzuSndMbUJYSnEWyDfowptbk8LqI8sXg-481t55D5eNAuh3kAlCgjyIsALfn_C-KOTrwBDsMlLKGhDTpyL3fgT8WNGk7JJBbEDKJxonqLF0Mz7eZO4v7pE8GwR-EeSbaobK0Iolhg2xTS2dXQw51gAhQZZAsfh-jJAgaJXgfwsJOeI9Bb49ZbPYKheDFAChWuCvr4V2m0vgxTC8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/22329" target="_blank">📅 02:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22328">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339ed28585.mp4?token=corzCcqP3mFwWMuW-54Io3jNfNo6tvXCpuHGOinYdDJCtytsecibTV_M92my0ravoBgvsLszmQZbAq1-0K60X_KXcnfLoUL0jP7OSSzzvS1VLuGeXkBdIe-dx2vSpfFPJDRPxk6XRA6s-c2vNB7PNyNmwDHObRe3P-H3kVABK6FuXaXdlA_Et4rg__WLTHnyOSEdXdPnj_gSCmZ6h7Ax3ug_G2IRh4odIDeWWvHy3WeVwHt8sdBfTVIKWeRl-Nz0r8UpwN600oxQMFh9xviyKy2ZEgC7uRbO-avsxl5N8NFzVnJ2V0BKAJmsclTZZSo2f-7kcOP9Tr0vcZgk-xNLmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339ed28585.mp4?token=corzCcqP3mFwWMuW-54Io3jNfNo6tvXCpuHGOinYdDJCtytsecibTV_M92my0ravoBgvsLszmQZbAq1-0K60X_KXcnfLoUL0jP7OSSzzvS1VLuGeXkBdIe-dx2vSpfFPJDRPxk6XRA6s-c2vNB7PNyNmwDHObRe3P-H3kVABK6FuXaXdlA_Et4rg__WLTHnyOSEdXdPnj_gSCmZ6h7Ax3ug_G2IRh4odIDeWWvHy3WeVwHt8sdBfTVIKWeRl-Nz0r8UpwN600oxQMFh9xviyKy2ZEgC7uRbO-avsxl5N8NFzVnJ2V0BKAJmsclTZZSo2f-7kcOP9Tr0vcZgk-xNLmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طولانیترین‌وعجیبترین‌قطعی‌اینترنت‌بین‌الملل تاریخ جهان بالاخره بعد از گذشت سه ماه به پایان رسید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/22328" target="_blank">📅 01:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22327">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/doZvDeKRq1HYJH3WmTIqrQGFyEEmmpajclCGbD6H44ZQ8M81D5RhwNRkiCP1v3k-tNjjbFnVuYQGIXaN2CZSkB9hNsgKDyuTCbAsYS_EF_dUpca42llWmUDOQVJu0bTTPQz2jHi7SAXmWymYwZgIW7sZiIbibpBKMhMNnApcanbv5ZcEj5CftQib4fHQpMF6jeyLdr9995Mrqb2ZH25Gr4K-rPfhnVhrAg2D4RO0iIorrkRbMB1VMFbvG2kzNb45_V0nQ7zX3kydOBuzqA3qHZfwtJBcoKy1FgcSIpxYWL3DYwwJQPXRgZLBMPVNDCoqzBIg0igsOBUXKI8cVTdH3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ سران‌باشگاه آث میلان قصد دارند که ژاوی هرناندز رو بعنوان سرمربی جدید روسونری انتخاب کنند و مذاکرات بین طرفین آغاز شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/persiana_Soccer/22327" target="_blank">📅 00:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22326">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_aT9-NHlli2deICAp1dseGPytwby--7gPHWk1Mi6-45i_UNMdhO_Xl_vfLIiFlBOaHCTToAyadGnCDJrFJ5tFkN9zof0zyt6IiA6sZjHhtru0xlDTZL0k4VHMDlMKmN50a1x7KC6XkGh5VP68g-4CDXU4oHmsWW-c6cNQeJhw7Oz-tNp9aEBYotWUDvyCVUF_Cbv0UZb4Fhy2UFIJIDxNZdzAn3rYVTeUaAzk1iijsJFvqBxqiQZE0aIgGhSCV1dx5Wd8HVB4OMvt756UI6p3RQGlpstZzcr9bXeP1bnBSHCPTGnAuozO4g5TSAsOIb-BS_S-NXPWfz_4FJZ0mUcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه استقلال از طریق یک وکیل ایتالیایی مکاتبات خود را با فیفا برای بازکردن قطعی‌پنجره نقل‌وانتقالاتی آبی‌ها در تابستون آغاز کرده است. برخلاف‌پنجره قبلی احتمال باز شدن پنجره آبی پوشان در تابستون بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/22326" target="_blank">📅 00:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22325">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/437e19a5b8.mp4?token=K8ufDeNRJg7n9UNm00oFyTi7SU1j72jMDt2wjs03nJdmoMAWT2TXUpCvdxe5xokza6vQtmorTruUvoElNyadjB-bJnabgg1-J_QemsUs6v9gkhwmzKJeqVkZ_RIE9mr8HbIAKPRDvGKrNSoaCAaQlcURvDgTSlcz8T4xcUJI-Ves9uwzTUDXY2cTNyd418cpQbUlOWar2W1OGyHADoVvmI8O4kWN9FBRxMQCzabrxMbzjNugkgZg1xDJxMK7ZDq9y1MK1jopjW39sxLCwJMTEoN1hZHl7zDrhL_C_xbUcSNs5Y8uI0uTYRc1162J_zFfvCp60e-zxt0UvbTqH_fDDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/437e19a5b8.mp4?token=K8ufDeNRJg7n9UNm00oFyTi7SU1j72jMDt2wjs03nJdmoMAWT2TXUpCvdxe5xokza6vQtmorTruUvoElNyadjB-bJnabgg1-J_QemsUs6v9gkhwmzKJeqVkZ_RIE9mr8HbIAKPRDvGKrNSoaCAaQlcURvDgTSlcz8T4xcUJI-Ves9uwzTUDXY2cTNyd418cpQbUlOWar2W1OGyHADoVvmI8O4kWN9FBRxMQCzabrxMbzjNugkgZg1xDJxMK7ZDq9y1MK1jopjW39sxLCwJMTEoN1hZHl7zDrhL_C_xbUcSNs5Y8uI0uTYRc1162J_zFfvCp60e-zxt0UvbTqH_fDDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گلزنی فوق العاده تماشایی و دیدنی پسر لیونل مسی از روی ضربه کاشته و یک خوشحالی خاص
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/22325" target="_blank">📅 00:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22324">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etHIygBC-8fBnduXAfDmC0bV5xuVqhLQwCmhUS4zgdCo4l0HYIIDg1VEmkX4etLOLI0UFyHOqrzT_LLGptjWS0yjMxuEfFAbVCulR96nudTcTiy6QOYPY28Ay7c2rVXo2D4p-l8OTgDvpdTEppsvBSLOlkQm9XDaMBU2AEQYiV_LAlzSLy6tPxJX2IXu1djeA8dhJ2MHBIxo4uWohvoC6fQxqFgeDIntffTrQlOEov4rz7qAhXCvxYzvI9mMlvSn1Tg90M8SOVUjgSS57ZzaK9aSNw7AKwpUeHzQa1TZ3gE9pUzhi2Hp0iDXRXsaeDJtcgf6XBGxD5Nxx5TnfuztOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باتاییدیه رئیس‌مجلس و رئیس جمهور؛ اینترنت بین الملل مردم ایران بعد از 80 روز تا پایان همین هفته رسما وصل خواهد شد و نت به روال قبل برمیگرده. ایشالا هرچی زودتر همه 70 80 هزار نفری که همشون‌جز خانواده‌واقعی‌خودم‌هستن آنلاین بشن اخبار نقل و انتقالاتی…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/persiana_Soccer/22324" target="_blank">📅 23:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22323">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ha3cqlhWMclppfjY4-H_u3N5m5Jml00bfb4YkxWc6O4mRxuncfP7ni3Z401bb9aMmjCcJxm33P1gJipY9VBm9fy0fEa2PpF2cWFVB105azUWurSTfpplOpdv_auoQAvNZq7VkQJU7205ztOk6ghihFPO0q1zRrl8xAD2Ybexldk-vEHCa0PerVdBNB_-kb1whH8YQlWC1Km_0wCOP8fBcMgdqf2WbW_awjQyWPzsZ__OdiwScdcE94ogvdX28BMeDOtjQL9YXN5IyOpp0VN_FpRBVPHKM2Y60HU72YfmVtx9IC9rvNIjJS6DAcXJf_yQIOxvNxwovcGMcHEfy6k4tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
معاون وزارت ارتباطات: در پی دستور پزشکیان برای‌بازگشایی‌اینترنت تادقایقی‌دیگر فرآیند بازگشایی اینترنت‌بین‌الملل‌رسما آغاز و تا نهایت24ساعت آینده دسترسی مردم به اینترنت به طور کامل آزاد میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/persiana_Soccer/22323" target="_blank">📅 19:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22322">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ie5TM9D00q83Ms7uvp_p37d7yBI81qHlECOJ3M40CfqPniwc4A5XtfTTB0yUxoP7cifK3-AdNpove8XunDw1d5SHa2xCyqV9yzN2QUP7SLDZH2bnLe_q8H0AWF4zbEp6LXwWI82Q2j5bJTv8YAMh-45wbdfhijP6rGiJJ9MDmBZYrzoPZtVh9wgLgoFnXlJ2OOKsvXApWeuhGIP2JN4qNkAxWs12YDzyCMLS8ag8-bN2ABFHuPScjuyBmIPCKEn99GknB-Gebo4jvCrufnrqHtRRmMrm4fpLInM7AVObWNE53_1b-93FaQaTiCUuK04Ecajj3miBZUae3RaL9Z7wqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
معاون وزارت ارتباطات: در پی دستور پزشکیان برای‌بازگشایی‌اینترنت تادقایقی‌دیگر فرآیند بازگشایی اینترنت‌بین‌الملل‌رسما آغاز و تا نهایت24ساعت آینده دسترسی مردم به اینترنت به طور کامل آزاد میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/persiana_Soccer/22322" target="_blank">📅 16:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22321">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EkogxGSQ5CS8xp913Qiql06Rr3t-N5pOCOOjb6I14ZnEfzNyZKqwWKtA1meXRPdGj3fBGdW0j-X7UPtTb7pjqSLbIueZqO758s5hwpgqOUjTNv5DaGErGrzXiCHK6sODXQv6EULco9iDhgvRPkYRLiLjWX9f0edwW79DsGH3-EMo1Myzafk7Bx2rZDlD278TZ8Q3adCEhmFEf1mrdeGSl-7H8tqJFBNw8mNFZn5hEqB_9jf0B9RQivMTbxULci2cN6OjpS2W6MP_I3qNll00AvkPRQMGcS5wqhbfbt-Hglajh3p1mINvVb7kxdKvHlDa0DMvyZv8YG9VGRBnGDf9PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ بعد از ناکامی تلخ در گرفتن سهمیه UCL؛ ماسیمیلیانو آلگری از هدایت باشگاه آث میلان برکنار شد. اولش خوب شروع کرد ولی بد تمومش کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/persiana_Soccer/22321" target="_blank">📅 16:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22320">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2231444b22.mp4?token=ldlXsWqdOf3P7xmto9Ma-7eGVNWQhKhI3RR9DtnOL4mS1mL4x01zVRyefOHkgFwMIW2pNeQDiGMbdqHIE-SBffToNuDlb7mEfF20YOzJEwDBUUd1GyDeYlOw69-nuhENU2ZIrCgoQqjtQ8hzfQbeyV8evLYNPQbv3Rj2XC5Cnek4lRwF1F93nKoGhey_h3n_8BMY1a6o6Ui8B57dF-P7bCUZb9TtLQx7AEVG6YQc7TnDfn2TWpVY-i29jbhcRN4uo42QC03e2RKFraGO89DOnUOOUqyYyDxyVAItImajwtbvxl-_Pyw0Y296vxFwdHqAclYXYTzjJkPrr16uQFxUbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2231444b22.mp4?token=ldlXsWqdOf3P7xmto9Ma-7eGVNWQhKhI3RR9DtnOL4mS1mL4x01zVRyefOHkgFwMIW2pNeQDiGMbdqHIE-SBffToNuDlb7mEfF20YOzJEwDBUUd1GyDeYlOw69-nuhENU2ZIrCgoQqjtQ8hzfQbeyV8evLYNPQbv3Rj2XC5Cnek4lRwF1F93nKoGhey_h3n_8BMY1a6o6Ui8B57dF-P7bCUZb9TtLQx7AEVG6YQc7TnDfn2TWpVY-i29jbhcRN4uo42QC03e2RKFraGO89DOnUOOUqyYyDxyVAItImajwtbvxl-_Pyw0Y296vxFwdHqAclYXYTzjJkPrr16uQFxUbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
#فکت؛ آرسنالِ آرتتا جاودانه شد‌. آرسنال در فصل 26-2025، اولین تیم تاریخ لیگ برتر انگلیس لقب گرفت که فصل را بدون دریافت کارت قرمز و دادن پنالتی به رقبای خود به پایان می‌رساند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/persiana_Soccer/22320" target="_blank">📅 15:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22319">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofPdtpzf4hHtk2vmspOQr4UcQ2x8fxdkCWvKtufORzzjWf9Cd0736Tdc1Uqb01BdoYI95f7quUtW0AXgF88esLR_Q5i55qBUPUR-LwDmWHvA24ehkzT4Sq8m-WoaQPBKTK-9Ghknl9OtCUmRVgAcOUG8GgElF3-6rcmw8K8blrs0aZuQcl6XxCzgi3Xb2VePloj3otKhrjHUzmJcSnB-ALFRNYTypqV4TypH0sfYKiH0SaCzbLVo-uSD0RWSOaUY2W7ICPpuLR4bVsWEaaf4IY-EX6RbqHO1EdvoqqiWM2hYV4_r63peuiNwCDKu2DJFvxbymmJNp95ZU-2TYNULZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/22319" target="_blank">📅 13:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22318">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqJ0UjxwpdJUbwZuKryyMmHy-XVYjhOmRaawp3rq1wxX6GQxbmqMfW29u9qGbYY_yH5-_4tsDS7s-8Omez7Vt0foh5CVqTMZMG0AbNJhqZP635RliuOUbSgYjNdR3yekME7TSo9CXMVe1Wk0n_f5TtusIa8Ex2YfuQSipsUhZ4LO11Gp6qCASYotOe_b4gZe7ipzu2yEf2U9C5lkkqJaNfB21ZPGTqdiyxryP8MRJJmqh0kcdKAmwlooan2hEird-OjVM0bsAJusNjJa8nkkVm3VQ55eLCgQmWIMVfZ8flD9tnpBkk3pIGzzQSVmf56KvDRwEhbqxUI48W-QBQKm4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛مصاحبه‌جدیدپزشکیان:اینترنت مردم ایران تا ساعت آینده به روال قبل خود باز خواهد گشت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/persiana_Soccer/22318" target="_blank">📅 13:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22317">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJBRFnAqp24BxPkqhCpNs47G2oWFvrdq4behYLsfNgm0pWwMJpcwZJP7D53izyqSZXplcLU6g8xWmAjmXdBVN9YvWvHxWtyE_Grg-1somTN1RjOId6sOcrphkRwpI0i_2uOyU3AgCe9peY2KgEfWZdV4aTnOcLRgeT9-RC34pF6CHH10uHU8-SI73dWpDKi-k_Wmcqgzhg8XYG7pSUQ_eGLlO2B8aeL_eL1reTVkUdk8CGCIKK0Q9uYutcSzAriFAO0SF3qhwsmqBROFIEqX0gBdjDGh8Z5xQtyaGVDN8gW8mj9Ausk9DF_14Wym_3U9LKk89HlCmuiGTvqJuTmIhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه کامل‌های مسابقات شاگردان روبرتو پیاتزا ایتالیایی در رقابت های لیگ ملت‌های والیبال.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/persiana_Soccer/22317" target="_blank">📅 13:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22316">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gogOwmLJXqmcJMsx7KuzM0P1CYheB6G7eZF5C0RceQrlrB695XVWFM5BcPtrOTnyV_WKWqTxqiUVd-XWEhANLBnRy9iZimtMCQ0I_6yJbqnMRNi4b_Z_VzRkqeVKQXEOQ160_QgU6BEMcxZ-_mDgmctf50tCxunLasMbiBQbCgZa-GXfb7vTlXFL7zBEL2SOQ7UijyBESXoy0IHPx5W9MPaBSNauFmY7LJcm7M5hrCzEnrp1h0YimzBLs4SYWvycvNbGxu0tKyEyRZ8vyRq_B7aSPzsTgQI7HkGyD14c9tHql30GVI5zLaQIXavnuEvyCKglvSlOfNZXzTesYVHEBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇯🇵
شهاب زاهدی که علاقه زیادی به بازگشت به پرسپولیس داشت بعد از عدم تمایل مدیریت سرخ ها به‌جذبش‌قراردادش روبا آویسپا فوکوئوکا تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/22316" target="_blank">📅 13:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22315">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5Ki-HJWLoA_3_mPjhYqs2u3O3tPlY2OdnFEmDbOwNPFGNYTDSxJYy9q558pWblk7U_O3IcLyW5iIuv9C-781YjEa-BI-07JRBJff_b3DYuJ79BQDc2PQNG4c88XTVvnk4LOVG5FZpkP3migQh4BVysQfTCQD65wkdj71HqmjJ9TlbUUPN4GfjV8d-1uojDjDxN0NCZpSHwPiTtuMpdqzAT9H-HXWXjjt5zd4xs9y8zAswUQ0zDMvtS66v0bMcrkruzPeHLkOVzVor36pnJprVpqPPrMd03bT_ZvsnilfptosgLrdmOaOqVwPFOnrYUe6Uso_-wckjqjC5fbQGADKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کادر پزشکی تیم ملی آرژانتین
؛ لئو مسی که درمسابقه‌اخیر اینترمیامی دچار مصدومیت جزئی شد مشکلی برای جام جهانی 2026 نخواهد داشت.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/persiana_Soccer/22315" target="_blank">📅 09:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22314">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bg6Oy08eptDYhqAS8b0ufjldZYi0bqSb8LJOMReU5tjZA5sqqRoVyDcmAM8l-A1jMDPeLoI8qBmD0nVCzEL7gLQdnWEEBLzerMRXOD6FZ6nbiQOdNt47yeZCUG4WYQEfv8gAoHUCEAfQNTFG_utc2GHhB3nuMAfEqGWvS6N_Dqkqj-XjBYrj5RJRAHG626zS0aP2IyaBKO4v1tmPdGQc4ZWNC4oySdeNM0O4Xsth8Kf0MyekUgw9tPwlK2L2BGwY1__n8C9Un_uxsGSlFkNxxVyje5LNDz_9wv9iEbxhg_g64WwJpcjPuUKjqg2QMqP_mljKbSWPGEdYJdDKPTNHpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛نماینده‌خولیان‌آلوارز: اگه باشگاه بارسا با اتلتیکو برسررقم آزادسازی خولیان آلوارز به توافق برسد این انتقال در تابستون پیش‌رو انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/22314" target="_blank">📅 01:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22313">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLvcuyMQSDyriJ4fRh2ImndFkFmfZ8RTbavbgwJBwVdtDBkqYN-bKTWKNFMTMJyxNPjjPwplqGo2bFeTAiApQGz8-MP0Y44bFf928rhjSClMdfNc4pu0iMsOk-W-zAYzKFs2CfgH6_yXc7VaeimFJmgcQc8RKpCHwTk6dZquKQu65N77nTLoh5e_ubzP8-FSsaA4u-qtiuZ4DHkDH05C4tBE0Zl2rwqOGZE3tMqGF4kxtExueSWCrCppfeoVrUuhYg2YFSS8jF3ZTJlpeu48OOwgEBJ6t_5iofoNCqZiUwhWgswcvQcGP1lLlY_UvzCz4kZ1rIpCyKObHXiKG8AtaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ طبق گفته رسانه‌های نزدیک به حکومت؛ اینترنت بین الملل مردم ایران تا ساعات آینده وصل خواهد شد. انشالله این آخرین باری خواهد بود که اینترنت مردم عزیز ایران قطع خواهد شد.
❤️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/persiana_Soccer/22313" target="_blank">📅 01:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22312">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-CbO2dsaWuXVZhivMfaYEGRe6OpWAjcbD2FQGTafrObIor0Cg94odVg_ssYDhwP5lWZ1nFOnBfSsNU4n0cUdRFngD-Q-OvdGcuif1BPR1PZPJK_vvQi7KUpBKpUwS0kBVHFgplhnYFCBNQ86elGAVP7zIcjnFD_px6lj1TzmFpoxeZl_eWPbDhFDI_WrWw639btDF5dBqhHg-kqkgZ7BNT7Re54HTp6vehNFO33knbnWj-74iHS77cbU201LL5IMauZ0JofMd7N3nPY9JMuPxLRE2PtDZT2NoOkCuZBd8T68_cDNq0gJwmfj1tqyOXeGOfQpTaQeob7L3cY1XeFLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی ؛ خبرنگاران نزدیک به باشگاه النصر عربستان:احتمال‌داره کریس‌رونالدو سورپرایز بزرگ ژوزه‌مورینیو پرتغالی‌برای هواداران‌رئال‌مادرید باشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/persiana_Soccer/22312" target="_blank">📅 00:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22311">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edSzR3zvCF2kYHJ2M-bJFXsmqG-zHY-87AF6v_6r_HZa1yjR2mfs8BtghPDsnQZZgD8YWq3ir_9TFWzkBWalOViY8u-gWEh0cpAJYBXR2I4zZ9mZ4r74pZEoNun1_JBzVMdDCFtm5xKJX96dL3_cPAz10Uy_k1WUBWzfo_fslgEoohDHjS2xGwMXgdXxHLRSALe-_9F7WZZiehz1So0ZEivZncBeeeLGwmdRYNYxTjyc_kM1VXoKyrWU6CYkzEZHdHLfdtsUPqrwhtQDocb6SrbPeer9F1N1Ldw6oZDdCApH24wwuL-GVtDFdOcuY6HZqB2Osq3FKVtzPyf9TdsR_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/persiana_Soccer/22311" target="_blank">📅 00:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22310">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHotOzDUy-Ur3Tl4N5j1rxqzupLJuSUG-E72FW08hz9MZZA5RaRV4QE_NNQAbe77ov9vXuXi1A4hHh1Cqs55CiWRv5Rg6HzTwhMFEtG5dxLOwe8RKHcDyprNPCFUbP5a_yEp5x3uzVXxvFYWMdbgr0VzZyxpsnSCtuWOmmff_Tgnu4ng-LC5qvHzLBmK9qL9LWjvNyvYIQAcfdwBG0UC_O9bVzsbZMZjw9moRtXKofnizjaQynGUFCqc4ecwSPBWUgGMZPGpwFcPioFgjEAZVSVwJMSbY_oDXTKB6UGsChmlMDVsOngauIRuvB3FBoab7MSNwSMo_URBMmv3sIo9GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان تااین‌لحظه نتونسته مجوز حرفه‌‌ای خود را از AFC دریافت‌کند و ممکن است درصورتیکه مجوزحرفه‌ای‌این‌باشگاه صادرنشود یکی از دو باشگاه گل‌گهرسیرجان یا پرسپولیس تهران جایگرین این تیم در سطح دو رقابت‌های لیگ قهرمانان آسیا شوند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/22310" target="_blank">📅 23:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22309">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ke26V3mvXLUVhKo9burlsrF5bXfZFHOVl2rKMUYCGpDEBmQbUmjONJbXJaQPrf26UVMf4YXQI1NKXabfMLpW7al7zPM-tASrOzQKeGPmZw9F9bQFbPgqxxE7xrtfChWPXquBvSPQzeNtiPpN0lB_LR-zQemJOBgmlyCUnCu9rTP3qjhzsipyuvljS2MgOfXyi_ILNne4D0ms9KnlC3kMal4PuHsxxbaH3csx5q3i6WToY1WZb3R1YfPi52mVVMjIUkqs0z1_WXUGqUYnrB5gFwRSeisZztMVcsYZ1FDZ1PnhTtD1k5u7mSmTJZ8O_UjmyjcIxQ5YxJeSUWlwgl9RBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌سری‌آ ایتالیا در پایان رقابت های این فصل؛ افعی‌ها با اقتدار قهرمان شد. آث میلان آلگری سهمیه UCL رو هم از دست داد. کومو با فابرگاس اسپانیایی راهی لیگ قهرمانان اروپا 2027 شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/persiana_Soccer/22309" target="_blank">📅 20:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22308">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPLio4yi2rexl8u5H5KUAabA2e64a6XwV1z5pFh8wqlBAoIQNgvdKHopSOmPZRs2a4JA-1RMSd1WCiGVTkctcxl-a0CJFLmF9_T7tN1l6QHU-_cX6FmuhLQ5RJGTIToHrqYDHc-C1me3lME7RGT7Zm_KDq9OhxAbMsbIhiLZiCn-fSjYY8aFaGFYV-paN4LfZsNzLFZiks8OzuMMF4hYQGShGGWHBODG02TXh5CVoxwFbqTFUrYLhrQbbJLIC6ftnLnq5HCUeZL3XRcSswywbpukQb5yeX5Nkx7ysGxbKmDXR37f84PMFSMjR88WwKRTsBvDlqYmd3GzYNsZljql_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...ایوان سانچز ستاره‌اسپانیایی سپاهان توافقی از جمع شاگردان محرم نوید کیا جدا شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/persiana_Soccer/22308" target="_blank">📅 17:32 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22306">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J6iawWL4Ev4xo5GVKHPb8A_icAfccD-UP-I8CC35dOm_L3RAlawLzNZ_GAiI96xP4ZxiBiH7dyTOVGF5PH0I8OzofbRTl5vR9usCSza3sP5_5QTxXkfBNwYF0VYu6O6r9ePV0Z2KMlF95aGkI26MNMGTe9KDhHOsL4-WHZ2f92GlUpBsySqTN1jSwKyYt9c935Vfz7KyKNOvP2kKnlBLnvdZt8K7bXL45SEJwwW4hUP10v9A9Qg-cmF3U4rBjYYxMyixbDjuLc1-nHjZSQ_SN8cfOQC5NJT0g4y0DeVoWQByKy9Yb6U8UOADkKaS4hli1d_lnqQ4JtQihrUWt4BDtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IJcrYDqrcB9H4zg6IpdevknbGABAXjctjcX94ASIo5WzYUgIsMDaBM-8l2f1MOl6aVsOfl-hBpapvI1l826KWB0SuOIN_UfpUbjFyhHbg15d_PeB2XpcuY2nmlf__ml9sSnZUHTXOKzlZdhXFS6nx2-pqa943lBW-Kytp1JiNYSNA2o4AfFfJtd7a89p1JKjGh_u27t8vSibGYILWQobrp6Qm1Xe3zSs2VEJdRFlMRg8hVAfwGW_vryzACGbo6NsCvoU5qkMJ1ist5C7DC4x_vVoAI4eEhZx5_gMDsKmdx5PFRHOO311nT_5XvGXJ48ZdXmiJFwkFGsp4-kjNuTz3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مائوریتسیو ساری سرمربی‌فصل‌قبل‌ لاتزیو راهی آتالانتا شد. جنارو گتوزو سرمربی‌ سابق تیم‌ ملی ایتالیا با عقد قراردادی سرمربی تیم لاتزیو شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/persiana_Soccer/22306" target="_blank">📅 17:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22305">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNDjzaaOCZEXQwdnrWQXKmDsCfvYuqTetzwr8sMqI9OnOslcAE3UlI3GXhucr8x8h7FhxidVLXZM3EzTGWbW2DzOC_31zdkpDqKXBLugS7MgxPn_2AaDz_eUy97igE1ClYnOPsNYuG6qhdgmG9mWzMXrMJMpvP5kHmANu-6a7aaNl1asaNboIlDz2FUjif1mqsAe_UFbqkqGIba47_Usq2rvA1c7uMCWYxCSQBYj9dema1l9crKZU3JlbvXiTXNjmtMFxGxr0SHDIHS2deFC1aCg4_di6tuJ2M_G-CHQcwHFUJzeM0sAncc9D-6K9tBzE3MxnVvmuJSSRmIjOT8-Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سردار آزمون ستاره سابق تیم ملی شب گذشته بین دوستان نزدیک خود: تا زمانی حکومت جمهوری اسلامی پا برجاباشد نه‌ برای این تیم بمیدان خواهم رفت و نه پام رو تو اون کشور خواهم گذاشت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/22305" target="_blank">📅 17:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22304">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRq5qy-M0Vn8sUa0kr2fC2epVo_urnAU2vFqAMtwGqAiQp7ikmn8BWWiJvUNclJNNOLUnzbDq4p2yM3StjQMzyyt5MEcIzPb58UQmgJyAN2ulbWxsXxvfE2HNiPT2YCd4ogAj8hOYnGW7g5fVEgvYbCh70RMmyCVFVdGBDA6iPqVXkuSR2aXDirnepcfDe8-itD5Qv5C0XGx0200Cppaastd7pRCA5Ca08OAidAdtm9d6Rt9BrlR7CDQ6acxrek0kDweLdvS_t3N0xrzrQfI2CATX4AgvN6SI9K7FOS9xn_CFg0rkV8LHMNX4CdOoLqMwND4dnIF24BQHdxAAB-vGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد... اوزجان بیزاتی مربی جدید استقلال و دستیار اول سهراب بختیاری‌زاده وارد ایران شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/persiana_Soccer/22304" target="_blank">📅 16:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22303">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hS96gYFM4r0ElKykgw01DryfGF-8DQlzBLKKvKF65VToArie4XIQXJj9SUSLE7ZGWS55yiHUJwcIhxMadhMGlkc8E6dGYptuZXWdUysuENZWObnX2Jt8zxa_DlCL3mLf_KZGsqHW2axM0c3kr8LD3bzTrJWtgr5HaOmjW-_ZZ4wpXU2mcczGewOkek4-xBADBGIxH6gqIgquX78Ox7btZUCM0rzibSmXseEYoLB5ezqZ2qUilYWcv38GQlVSvA5ceizqTITL8XCF7FIoRh_nThrY1-AcCT1sQCkNUzu45ZfCpxtsb3reA59ByBw4NLpPNPxnKY4m8Pl36hp32-JVVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باتاییدیه رئیس‌مجلس و رئیس جمهور؛ اینترنت بین الملل مردم ایران بعد از 80 روز تا پایان همین هفته رسما وصل خواهد شد و نت به روال قبل برمیگرده. ایشالا هرچی زودتر همه 70 80 هزار نفری که همشون‌جز خانواده‌واقعی‌خودم‌هستن آنلاین بشن اخبار نقل و انتقالاتی…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/22303" target="_blank">📅 16:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22302">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYD1luV0ynN2HSVGkkgaWBItenfoUmkge9uO4DJyrR6QfZan7thueTiZH_2ILjlNcFotuFkNRvCW79rOTRZR5jp4hwis44zgqAegKMXG1QcpGC82bxlWyq3IqEyxq179K7TeR4ZcqCzX9oIfv3Cz7XRCAfnTvLBGBiOiIowv5DIkwdpEN1sY8XAe2NF1wLlXAWMMaWVragoAGS-zC2m5PixewEgdt2RckB0fGrLKZj5hMRRFuKhlW1tVOmCRIsoGOEdE-EPKUrEv5x7sFNTQScoSRWFBcE1XKUvV37KTKE4cylIDWKEjqLZxp2hKn2UkOcAd0mcscrZOt4lUjUzx-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام‌لیست‌نهایی‌تیم‌ملی‌فوتبال اسپانیا برای جام جهانی 2026؛ رئال مادرید بدون هیچ نماینده‌‌ای!!!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/22302" target="_blank">📅 15:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22301">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTLAS5DfhOJcxyMkhztAs4DFcrd5bLSFo3A7Ba8sbGmtOE7Hg92jwRysenYDCcbnAqQIOQb08i7k_id0UP87zkAr4vxHZ3FxHt7JmpKH40_90mB_FLwvtF-5ADx4QiVC1fI6QLphXy9MollV1WRpq6RG_DDdLm-O6Yxt2ExXeY20faF6qpOSk9MUSsObjQr0Wuyik2tdvmEVCgLdFWVYK0h3P7mmHkbZTGRiJnqelfRNGrT4DH9rpJoSV-1BfBfhaytm-h3GCp_VvazYGdum-WoSXVFPMwUMUE9yR8xQWqDnxFrfVBV1HJaRyBjtRg0idTG8pEQ9ShycdihD7dGizg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/22301" target="_blank">📅 14:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22300">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSglAJYe6_XKY6q26KU35IdDZ44J_bJ_XmP0pPtLJ_e80vrOsME5orz8Zwg4kJE3CZaeup0Lu3FQ8TMMAH1_KMDxnL_RkNV5QZWW_mB2KpeRsyhWzwmZAYuRXX7pZM2dJDNtx8p4cOv820qlHOrI5CiBgELzuOdaIX8v0uPn5shd1LBMY2rW0cSXXjsHeyzHqb-GFY5SKfhAbQjuXPQ2ciwr3lC7tqEFx8oVIb029NqCqolXs7VJauNfBFsZ4uY64cdmEzXWt-fwG_6fBBUtwHWZB1unoC1NRQVCt-MgSocwmgcoSSRaOcNxbpML5lXhBudV854w7_V6PJMqscoZ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/persiana_Soccer/22300" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22299">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOzoygizBFjCZGhx9Ra0Ne57KE1v8BNge4549OK8DSe20Y9lb-pJ2KIIJ1SuNH17GhQjj6r55hI1rD85QUetR7SO3PRaxhj4BzBZ8vdQhDEZNm1-D5pff6GUd4aooi493dhYMyTp5gsy7Bi6jrU_L9uQaDwewk2ZcO5i1VnX8yrD9C-SO2RVeFgllGpD6s_-xoEhoMgu8FD3ykAqxTZ9dKoslc-UWfu3ZB_Bo0pqOUoPNu4OjfyCIISN_lSmyNPK662kheLU_2jDuePhnQSLN6Z5ADQokViWCMOsoJWalzWzbMhf_U91E-rGZqX-xUTnzgn6k2OccQP33qMEipJa0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام‌لیست‌نهایی‌تیم‌ملی‌فوتبال اسپانیا برای جام جهانی 2026؛ رئال مادرید بدون هیچ نماینده‌‌ای!!!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/persiana_Soccer/22299" target="_blank">📅 14:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22297">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFeyyY-YYnVwWvHTf-fs2QxpPHjTvWX7X1d9loEcev3z10jiBwJjMin6uDRwkA_Vv5PPnxllsvi0klrLfO6XOOLGHaBjQGJmNBj3s_ls1f5t3uKMGQSjWsKtaRutdgT7xDEVju1-cUgUC0X5ppUjSGSg-GSz8PRTsVayw8O9h-bMCNAnNPo8nbmeiCNPGU45RvBiWIVF5NGiJazBl72csEhON2RFbjXulYyhtnhYoH1x_R3vy9-fUfzzaRLt_kDtB94jDnYUitrt8EZXoDphyNa2VRebzpNyTmjpDlF9ctHKe21ZBX3zEAaagxFQSbgvFAAp5JRmNiREyAIz2rVr9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌سری‌آ ایتالیا در پایان رقابت های این فصل؛ افعی‌ها با اقتدار قهرمان شد. آث میلان آلگری سهمیه UCL رو هم از دست داد. کومو با فابرگاس اسپانیایی راهی لیگ قهرمانان اروپا 2027 شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/persiana_Soccer/22297" target="_blank">📅 14:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22295">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIPPzEUqEX0nm4bzKrMaJmH1CJ2sAyADWa0qTK8Qo89hYXYikcm_uuTl6RubR7Hohgy-5kzyAAtoQ-ej3hjq5AG6vgRR__sMaDypjgmWI8I7DUDO_X7jTt7Ri7hTe9BN-xdjDvnqyoG1dWXMbdGzqNPnsJ5NZpgF6ObNh1h1b6TKypFoxoLc01-SqgwIOCGZgqP-pdzi7DvdqMnEMoi4bZEG46btYSXKQJb6TNK-Uo_XkA9N6OCShZGUdrw5Qz9A6NcUQqcOHB5M07BOkV4PlLhInb0ga9YU54n7WC5wo2YWrgctTzj1LTB51vlUIyoejFTUovRSdjBCIunI1iK6ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رشیدی کوچی نماینده‌سابق‌مجلس نیز تایید کرد: اینترنت بین‌الملل‌مردم‌ایران این هفته به حالت قبل بر می‌گردد، یا ظرف 48 ساعت آینده یا تا پایان هفته!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/persiana_Soccer/22295" target="_blank">📅 13:06 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22294">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNjjVU2AHyTSXYblKzSAt-Rt__genpOKONOyaVswIzIUNbdu9ejIGxgHzfCIZn6fpABZ0Bcrut4xGOzjycpqnXcxBe8XJD-RJSHQQIjBwhLEx32gcJfvvb2I5FfE0IMeRHv0qbSeB7KwG5bzqvMkGNebqNwEoymZEAM22euAAG-bg-Hv-pp4yagb57QeEcjX9ZNnggy6CNe9CFelZIxGqVnKRPx946DIJ6DFlsxAVeK_LW-pGDuL8ZWg_AqLQilOLnGYUPv7iPZreCT-j3FXlN1ubpGuFGwnmO11dAtNQA5bTVojn-VTE6RGYT5sHIe7HfcgYxsdeXxk5MoujOECBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ بعد از باشگاه استقلال؛ مجوز رسمی دو باشگاه تراکتور و پرسپولیس نیز صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/persiana_Soccer/22294" target="_blank">📅 00:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22293">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtiaxXiLbGTXABukXd-9a4DJSvfRUgYWVPaq4xxcKohZndHlgafU3XvKqYzkjPw20DP5EKMjG-ZAWzGPbwqwmlR_qKoHgqEg251ClDQwtj5VrrHH6LWXrLCuyYp0IR_FDgCJ_ceBF4QUru8cfw6BMOphw0Jo3A5HpIj9dB484xGftM2fkrZEjnfOf4bAQp7q1baHDSfUIRKZG9eIfBQL3f_aXly2_3cqnaQUcaCp0HPft9LGekqAtMj5RgqvXrXE2kwtICLv30FCKWbGDv906b9hQiSd-LylcLgnjkgVxFRxfpuTuqjjL6ocdjiHWoYWp1fIkUSwbmMENlV6ZWhmpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بزرگ‌ ترین کشور های جهان براساس مساحت؛ روسیه با اختلاف در صدر، ایران در رتبه هفدهم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/persiana_Soccer/22293" target="_blank">📅 00:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22292">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t23jH3EyrkpgNEjLuV2vWuIjLvvetUcApVzZTiKOKjkvUiXmklzNJppRJabuAPeUSqeEN5IANgnMPOb4pECH-XVjBHBCBbuyGAVL8CaAPEblPjxz3H4H1feviIiaivskAPPBw6z28Yi14Lb4L3Kv52IzrwV8EHVd0Xrf-yh-STAeevJ4_iA8pxpHBUyrdemiMn08jCUE8pVxxwfylmFOEyHIj7AQYzs2s9KDvDLIB1tvSJoMGlGGz-c7y0lvpxQt9ngA1kJ70ljiRcwPJxq8OgxmxxxAFC1hy0ZBpwhiNUEjikIK17JgWowuccja3-68oogllwogouX8O7NC0PBkdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/persiana_Soccer/22292" target="_blank">📅 00:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22291">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8ZzmRsFztVx3623lzOlT8hhSGJ8vTRA-TTt7y2iLopSm3d-tV5liBHkU5xdVgchtqHvqFS75GtSRZyesGB8B8tk5BNq9Q2mE7whaqkTFgaPBZKocOut2kHUmDV7NDoqaoGSHcUIYLct99D-YQVIAWK43pBHRQQiJ2JBk4mubIZx_z_zlRm0BvQ-uQNwDNBbz_DoHBS1esXIVCm4Yq--H_awQga9doXoJsUXAB8KQogc9C8XuSLKP_cUA7gdpqfkKSoKPXXX0Ll4PAKXnjj8HleT3k52ydhJUmUuVq92KWxIWqaeg6PvAK6agMtROycLmgjWDhPR-FjgRgY2TbqgSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعدادی خبر نقل‌وانتقالاتی‌دستمون رسیده. انشالله نت همه وصل شه همه رو خواهیم گذاشت. باشگاه‌ها نقل و انتقالات خود را از اواسط خرداد آغاز خواهند کرد. همانطور که پیش تر گفتیم لیگ امسال ادامه نخواهد داشت و تیم‌ها آماده‌فصل‌جدیدرقابت‌ها خواهند شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/22291" target="_blank">📅 00:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22290">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nY0Ww3LX7zxVDgmoZFR0118RnL_oNGC_2DICi7BLGDebpscCrr9PWQ9BqxIWdXUhaS_yTIarh5P7AQUET6dAsPHlu6Wb2vP5Bdp5BRoab-T-ctiOPB2l632FbL8oi8FECvWgzYTwFVnlR3MFy93kyR6GSHTgCYshQFvHQcOeH-_T2xe3qyt_LT3m-Cd-aA13l-rktipemcYfTu4mw94x4ycGqEzRvHhu83hlCFf0ZA7UwKftQYcu0uUkSeEofEAfJXMHg2mSnCsi0UW6z_uJ4xzUcdCP-toypOt_MIgQvL0Ipd2ObBw3HpR9bLsJm9_DMIGYGAREu8nM7RmlXpOd1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|انزو فرناندز ستاره آرژانتینی باشگاه چلسی درپایان‌بازی امروز آبی‌ها با هواداران این تیم خداحافظی کرد و از جمع آبی ها جداشد. فرناندز از رئال مادرید و منچسترسیتی آفردریافت‌کرده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/persiana_Soccer/22290" target="_blank">📅 21:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22289">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_JZRYzz5dZkTqF3kcbiy6o3wCiQ4G4DoarSodsj3ZNQ_Ms9QZeNHX_b3GdbsyNmxsw0hzeETlp4dJnif-Lv6USu07lCHtrn3qcA7OBfi3GUQk2PX4-ZHcZZm9mkMtbiIgT6BIMv0mCWG6t6rgokfh4sSqjiOUd721ob7kEIJl4CapuJS12Uix8PTy9ZM2j5sqvgcG9psJBrsTZW2almDgHQrlPQmOPvIzxa51y4rq0SqwsHwvzupUfRPH8NNUGBf5BMvj2Tr95FxNXTjsDmtTTfuj73uiqqyp5rVbqSaUE2wAXT9jROy_YzrNaxZBa6Bo5RUg_0sfJPYZG-zfXY9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
باتوجه‌به‌توافق‌‌مدیران استقلال با ایجنت آنتونیو آدان برای‌فسخ‌قراردادش‌درنیم فصل؛ برای پر شدن 60 درصد بازی‌کردن او و سوخته نشدن سهمیه خارجی‌آبی‌ها به‌احتمال زیاد او درون‌دروازه استقلال مقابل فولاد قرارخواهدگرفت.البته‌اگه بازی لغو نشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/persiana_Soccer/22289" target="_blank">📅 21:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22288">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKZpLe3K358RceWqtU0kpHGF5CYFnnjcazgkISZzeh_VbipDrx9igS1EsuHHNOJqs6lpNwYhStCldreUth3ctTWNn3ctAgGqpg07sc2ruRTPYbng5WP4cYhiIqCMyDAsXNnMK4BcH4a6OWYLI8-gB9KohtuLsOWRT5grhzh1D6jCcFKaUP1YUSC_102dQ4gPD2pTv6n8GrDL_olsqJAJz9zLjqEJOseEanYGL5DSSw5_FB2a3zLtQplZiG-ZwOJxzMc1G7rfTXgJDZUL03o9YiRiTl8qOROHw6EyUPX0ZeIzr06uE9OGDHRnRFGnzCtHQP9AzHHgSzL18MprqLmaNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/22288" target="_blank">📅 21:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22286">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QB511pBTzkKC5D3yiKEwwrH5Hz9WrHLKAcmTrisgixAMNBqFeZoXZxCtbLZTsWBSU5pwy6KryETDAwFLjUa_swvfXt19FKMDcnEPzPLMh0Vx-XXuzdbDKhiTSmcTpTv9tpZ0XaeZxH5mr8ce2qWMtDpTcSOGakT14ituGS4A51mKmRmag-qqYvywLSWB72b9wY0JkJZIkejhH2_Maj9ehNy3JupPsvZgnG5T5tR2Px2EfR2CcqGnGsh2iRQxLwnYZFNouUopOyLi8J3vzbc0FRW8JVz4XgDGULyLXjY_4AQo4KYoDin3hR-JqUV5_TO-StCTP4izD_kgNHcu9OhBJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/persiana_Soccer/22286" target="_blank">📅 21:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22284">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dURAMVB_7JvbGFOrLcPyUp9v-267tgtHdzIjBN8a2AJ87iHcHCXdz_v9X83wmCHFlabrwjNjloN4SaGoWa73sjQeA_d5m_7Zxkn0QDtUA4usuEm89e3j-2zjsqQy0QRC3APNotvIpSSvMe0s-Rvt1MHKLlEfAPrRcVYj4FgRpJJwbr9qmE1Be46tgsh67ZwGrcaWgENApldAhc_ZOKW0-1TtO9pqjPrBedAg7ZEkYhJN5Bvg2ff56yYqi2r0iZyd2kn_V8jOHoZpZ2RjBKVnvN7CW9NTN7Nk1cnegCT8lIZpY-xRT6jGdZu4iCD51lRjnOXWHNWnP6vVfhqwudDENw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/igDoiSHb5wvvmdprAOVlbBtE8ml50Tz1ukIwdmaHDdt27avavDPU6nsOKFXGeJJ9fHTWL5fpQhQoGYghwj23A--04BlbLWp65cptltFV60nIK19_nDx0UzjmcvCTJ-ge3Hj2oxk2_Ft5uOY9DBdYs2nbN1fDdfawTiszqkAy1m2m9Dr1gKF0BjRjugRKczvNs6zPUEzTHjPAlCdT7X2ZLAWuEsDPvI0b2SEoLQNLSeD5hd5sqAGw8ui1SkNsWzS5fIPfMMdKgEY4epwyKn_qCQFADSzmlhYbC-lgVw6PEdT4_5YHgw8-jM6MG-Q9b_2E0h5F-emM6oeA4V_xtjGY_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/22284" target="_blank">📅 21:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22282">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fS9ETz9aFuWcGZCJMzIU4SXAre3IER0zORc6VxCfitawXTcuv8GsgZMZ5zI_pNEHIo-iVI8yNCltMzlB8AtfZilaXW_XFnWu7ru2HNAdLcg-Qvs37FOTEzhN45_F6bPVs5qyZbucGFbzTxIZIp0-VEDtTzR4Onf2bNsk-QeUodAipwb4IO-27_ziuGNNuj5ny3mQKVrXeMPQqp2OKL9hjDrN3Y9ZO6RD-JEQELMJkNyi9ZjbBSm8PzOckSk46U5i1cRbAPNDcG3cLXMKs2pLJuqZHUwCPCp9XlE3qEgFNMR7ildN9hXfIyiqcfUe6wppg-bFmPmsbFiLJ3TvjfgOfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KDQd_mxujfRJ0Oo9t94YA42T3estzbfPD0Nj5aPYqgKAbdKZBHLuTDYUrm8M58oSnscOfYHDoFdfsqSg0DZXhfdS09RpkWp3IxfDmyKq74jxQ34CmJ7sZb5jtOqLJwn4KJchdtKpGAipyNtIRiwiOl1HwWIguxPbjml3aQw0i0ri9maYkwE7FEW_bNYgfxfQlFwMqcuHfr4jygZ9oSXl21a9F1KyL-1_UHg6TIQtcaIHmrPLPT7PLPAt-QeyeC-blqcjZQsSA9ak95qXY-wxDvBTU2OegimHH3u3MuNS6DS8FicWNT64vg5IOq8ZmK_IhTzXBFV7VhbvfOLkuM18mA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/persiana_Soccer/22282" target="_blank">📅 20:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22281">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYvOfmrh1972gspZEbpznYQ2g5JTRE7qapBGFTf4CBt1Ex0ap9gRFWBRjGcW-TVGYWnU-CH6v8lxG3d0_1e6xw74QOio0ratM4_4mtvDPxOoMwwuCVKD4pHuJ5Ft1ahld1hzC00X3oAlDQUkH6Wi7CwmeL9CkI9mlA0BfOw0Ye7jFQBTAOcQ1LtM40j3EQTuJyeNNDJIgOGWIh8a6TF6Q2ILa31z4QZs0cl6aLRHipPYlFvynstI-T0YfkCZ3dU0yaYLkEndiy6T1YksQoKX1yXUu-i4ooj5CCFOcCBrH4BDWnHJpMrLez1eIsqoNwts76yGeZUQBRdXFMJc8WEvDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌لالیگا درپایان رقابت‌های این فصل؛ خیرونا که همین‌چندفصل‌پیش‌سهمیه اروپایی گرفته بود به لالیگا دو سقوط‌کرد. بارسلونا هم‌که چند هفته پیش قهرمانی‌اش قطعی شده‌بود نتونست به رکورد تاریخی 100 امتیاز در یک فصل لالیگا برسه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/persiana_Soccer/22281" target="_blank">📅 20:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22280">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxJWoBJExn5DTcZhS9_ABjFjZNAXBTksr_JGFbFvqACUwC-IjlbpTXeWpuRWLNYCv4lG6QVPvTq_ETJ2EKK2aV4FXqApyiaRBLIJVY2Z0rYo4hZmHkiG6i9wwpW7voLxYESG17JiLJhTZF3PMyTiy76_STIPVG8PAFyVTatYDGU7PQGTvzg4nx3CNqIV4VhUDhkKsrZVPKQZW5Qsj4txz5zLr1yWrQrbqytPO9-GQDKeRt_Uc6xW90Xoc-zsNW4xK5zMUrWeRZu4jOM_LlOevdLGa_4RBo-n5jUtuc3-TGLDe8SKN5jqqP6WI9GZ5eKfHDGei7dGgziptys12MSTTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ محمد امین حزباوی مدافع میانی 23 ساله باشگاه سپاهان قصد داره از این‌تیم جدا شه. حزباوی از باشگاه پرسپولیس آفر رسمی دریافت کرده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/persiana_Soccer/22280" target="_blank">📅 19:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22279">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImUpW_mYIcBIjvsGBygdoZ0Vls2d-FaOAwEaMx3KC4pS4KRFNMq1lEQKAxRkRCP9d6lFXRyg7QDFKJSGDkimFH8hdhsCznWG9jKw8T0u5KXOAZMv1Ti093KzScZ94Yq1CeuXwiulSjESPZFNPg_97zJecJ8ieJh9jqaW0jW7n3aAOyNTOB0KkFD58-bfnK2dLJje_VlPSzgbSfZDJDxf5v2LaIZX63tY6ep2amqxA5-oG-gytuX-oTl-1RpTFmpSOncR4ePLFdx6uH8DOoT03S2irgMzT63bAaFR_mGZf3Yau4zWimKtsjrkW65v0nXYe0PuTj7W_NFRQ8qoK9w2iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیتنا پایگاه‌تخصصی اخبار اینترنت: به احتمال زیاد تا هفته آینده اینترنت بین الملل متصل خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/persiana_Soccer/22279" target="_blank">📅 16:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22278">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUrCUfxy91vwOq2GWp4FpFsTdLKBsRDCbQlDcTrAsHQ8t3zbazv4c1Z-isFIloQ52IZPSQbsfNTF7Xz6A82F1XDU4NYaa7aubdq-BQqNQIND8iU6vvGwFresxtCcpNx739rTebMCZjGTKxJmRYrhz0x8y1wVdbsG0o02C47AO21q_sdHPECVSFeDttAOQnpOgdaTY78wdqEfHon6_z13y3qTXPH370Z2foPEt7nv7AxgSyJrSRfBUDREdc4goBAx6r5UHRZOlGvzjp_v83KS1z9Y8Pd3vPkkrp_eOqaTMyYmeAVoA1NLFtSSd1Ut8TP1gg1a25FOt-yLh8GFxAwIZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات
|ادرسون‌سیلوا هافبک 26 ساله برزیلی آتالانتا در آستانه عقد قرار داد چهار ساله با منچستر یونایتد برای جانشینی کاسمیرو قرار دارد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/persiana_Soccer/22278" target="_blank">📅 16:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22277">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvZu4xmq0iQqpE6qxTFDBG2omQjoskKc0P9Ck-k_Zx0ACnS-qhrFhlLau3JRh6UmUtAOUojOutY4NIozBzf0p-ZdWMJAJkgHzsfALPpbDBJF3PRmXzBrRz1LaS-Zqhi6Ph_gyBr4rwrp_NeTcT9HBWHlXgDL_f76XIGs-r6tL8shMLifPk_ECozi3eZ1zTEeFI3Z-LMjsnh7zyhmh1whyDcFJTDs7WOyhQM1ghyb_8TzsR-HXFetflI8L3EmunAPHGw6q38i0wzfQu4zTbsbmTLi1dq-uiiwD9ahb_sRtwsXbl1sDNVErIvArFtoiuy3foKCmPE8SPgCxFBIkBKGpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
هری کین بازیکنی فراتر از یک مهاجم؛ توپ‌گیری، حمل توپ و دریبل، پاس به موقع به هم‌تیمی و گل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/persiana_Soccer/22277" target="_blank">📅 15:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22276">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFuK4X64YaWmxgaP9T1qeVWN_7gy83G4xYehYAipQYG1oKjXOEDQU1D42_wuw0L8_7ze7DGZ3mQ0eFk3gWlMeNPDnOLnfGgez8pG6dc5LlkZ4dBnkb15f3keXMnxb_99fP7xr9NBDH9pKAK2-vYNo_VT3M2z12n_iUQIgLhYBSjIhjN2PndGqkLkE_SfShtxMA5SkV9mYzvWDox5A1B-Z2_9_TvaFqnb7xb3SOaMOLiV7ETJPQOF-BYKkZAkDtrigsRfCFbpZhpHHHr__368I4ZHx_7ezrHeKrq450ptHIolfGBVs0KubF_kwgsuW-OVSXZGZnGetbNuiNdjyJeb2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب منتخب فوق ستاره‌‌هایی که جام جهانی 2026 رو مفت و عین آب خوردن از دست دادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/22276" target="_blank">📅 15:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22274">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oD4G2obPsJoB3y9nrjpsSXPbed6HNzTp2LUvmjJ7YM3okPkVaBVCn-H1lh-0hb4NK7hXdQ4rT00LcE3-JAgDev7pNh2y0FKuf1tPCqhXw2HkIiJ9EbqGmj23tQMeonkEH6QbxQtV9kedcJzwfyaMeWme31NmxCV5304Zb7elozkhahC3iBQGsmcSALV4xC4KovBjqiIyWM0KLcnq-lTdWY52b42kb6rxvTgHv0MyxToT1j2ncW29NtCUphy6LyiLe64DPamQDWZ_jmrF8lIWsn6aRfYqNMRnGGaO8LdxqRrl0MGPRxl9rD2-EEhS0lAuO5vpe8H6VDkTS7UFqjbT7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌گفته‌‌روزنامه‌های‌ حکومتی: اینترنت بین الملل مردم ایران تااواسط خردادماه حدود 15 خرداد وصل میشه‌. حدود 2 هزار ساعته که اینترنت مردم قطعه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22274" target="_blank">📅 15:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22273">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONGgY4fgHmxzwv5SigWqC0OZZyb0xpQr1Z7Cmhahb5_eveH5O8CqrzEJiSgQutcfBfPn20G455cCm5h1aHzM_1L9PUyEGUOJBKchkhQfRaczWdB9GjndyCCBnSlT-t6CsmF3QhKH8xo0CLjTmq4-2BS6uu7irPxKwqKV2mbHkGnIFEYioXpHx7mB_qY0VzTEMrgYkc5mHa4c0W1fbdNIuJxNfEb-JV6ujNxa16yQiPRu5Hqa-4f51qx7L28FLqL757OwDzA_z8bFo0d3MOFQ0ZAE9NN6iVGSsSIyytcthJeluopwkM2NJz4kBNo5Z9l-PxqnPSEHNmAIU26ptwKNOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای سایت فوتی رنکینگ: سهمیه ایران در رقابت های لیگ نخبگان 2027/28 به سه رسید.
🔴
باشکست‌دیشب النصر در فینال لیگ قهرمانان ۲، حالا فوتبال‌ایران طبق ادعای شایت فوتی رنکینگ، برای دوفصل‌آینده‌بصورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود. در…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/22273" target="_blank">📅 15:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22272">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8nBuPSlnJRwDzdOChpXZcoysLjNL3a852gw9tnpvvbQ_61H8yw4WIptJs5dytjfjFmqxq1UjJmrNxz1-BjYIRiYhSdeMMENsvkIGFSw8SgA2mecmvBbZve_uSg3GIeNaN08LEFkwZpSNTrd5DQ8gQ11BWYGZH1fT-VobnfQOykYxFeTMv-PBzWLdP4fSySD-ZYyxXIn7R4BVVaFjBkRUewPDoG_sbEiyh59XwZfPy_S_pVBodMLKUbwpStOPBAgw2uDw0wpeM1AIgyAuZ-U5S6Y2IoOZIK3yRsiE9hJlPDQtfQS9Doo_QgfVC-1_tSuOXebYy7C6A-vxuc-6KbrOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
درحالیکه وب سایت ویکی پدیا از تیم های حاضر در لیگ نخبگان درفصل آینده رونمایی کرده و در بالای جدول هم اعلام‌کرده این جدول غیر رسمیه اما برخی به اشتباه اعلام کرده اند که AFC اسامی باشگاه‌ها را منتشر کرده و برمبنای آن اعلام کرده اند که نمایندگان ایران از سوی فدراسیون استقلال و تراکتور هستند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22272" target="_blank">📅 14:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22271">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb874305eb.mp4?token=WAggb8gsjIqlK0X6ceexx3sBKsHCPSYmbef_1RbIgKnaNO_Rj34oV8GPRilYoi0Jx30iAd2-hIPhNumrvGF5ECZoaHjvY-QSlp3ombRwAaWlsjd70e7WVlxQhxgH1xR2P6rzwemXAH5X2kbZsLknGk7pRrfudtYOIGJx0Ib4dLpidNARmsxCAhq_nKwSEKm2joYnWgZ0AVD_5zxQJM0fJdndWSHjID5cUupYmFYMabxgp-eNCkZWaQNfTyQ5NGntobiknQ0aZQgVLQhdkkjO225bjyKSx1AuBMZZHXfDTxNLy_m8p8uMxIj8jkKri1vOni0HdZjOY0EUTPGo1kL1_XTGhguzr1CCMDaw7O-wZdinK-ihhzzHt2NhaIa63Uzy4rxq5TENsIsw0QHXMwRpilFz_TzsbK8NmQ3b6nwcSN2YBSFkexBBj6_SWzPznm5bvcIBw__Jh7tOq6CcpKAeI6Uzh2O_dIVKJVNLSUfcKj5UjAaaxvRSHFmZjZetreyoc93gQ93HIguE0AJf41Yzv6hljbV0TJymRhqSiiPa7cYQqJZycrD8XBv2Q-v2WEMiZFwVT7kC0_0cbSGmeKooXr8814PqQJqtwqmF1CF4Z3ilYnDNYlM-FGpDZ0eQOYgfXRuCL-RyvzcRmdEP0XeiFJNsAHlYNB7ICV-xniUaLdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb874305eb.mp4?token=WAggb8gsjIqlK0X6ceexx3sBKsHCPSYmbef_1RbIgKnaNO_Rj34oV8GPRilYoi0Jx30iAd2-hIPhNumrvGF5ECZoaHjvY-QSlp3ombRwAaWlsjd70e7WVlxQhxgH1xR2P6rzwemXAH5X2kbZsLknGk7pRrfudtYOIGJx0Ib4dLpidNARmsxCAhq_nKwSEKm2joYnWgZ0AVD_5zxQJM0fJdndWSHjID5cUupYmFYMabxgp-eNCkZWaQNfTyQ5NGntobiknQ0aZQgVLQhdkkjO225bjyKSx1AuBMZZHXfDTxNLy_m8p8uMxIj8jkKri1vOni0HdZjOY0EUTPGo1kL1_XTGhguzr1CCMDaw7O-wZdinK-ihhzzHt2NhaIa63Uzy4rxq5TENsIsw0QHXMwRpilFz_TzsbK8NmQ3b6nwcSN2YBSFkexBBj6_SWzPznm5bvcIBw__Jh7tOq6CcpKAeI6Uzh2O_dIVKJVNLSUfcKj5UjAaaxvRSHFmZjZetreyoc93gQ93HIguE0AJf41Yzv6hljbV0TJymRhqSiiPa7cYQqJZycrD8XBv2Q-v2WEMiZFwVT7kC0_0cbSGmeKooXr8814PqQJqtwqmF1CF4Z3ilYnDNYlM-FGpDZ0eQOYgfXRuCL-RyvzcRmdEP0XeiFJNsAHlYNB7ICV-xniUaLdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوخی‌جالب‌روبرتو پیاتزا ایتالیایی با عرشیا به‌ نژاد: من 58 ساله‌هستم‌اما چربی‌خیلی‌کمتری از تو دارم!
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/persiana_Soccer/22271" target="_blank">📅 12:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22270">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c29GQAz3HO0BNKite-eBKUysetRQKnKTqb2x5p_RGA4L7tHE2-rviokvQjSYEzYljud96uZTvu8Hq0BvRl-l4N6DZx7fksb3J7vQeeNFH201T-2d8OkOUMOtwpyjM3mJpokkw0oUAjzw6hVw50M0da0eb3Zic3Xh3T8lpKVTRrkB9TRos4J9Ccy34rQ2r5GAGyAQ5uXa-3h3GvTfCk6dU3x8cCsZZPIpPLwib22g2-gpLgn2tuMuzZm726kLI-Dk20bVggrpuR83Ug6hNb4_sseN-yDvkxDPtg1i7PyazkxSL6ejwFmSImRj5P9HzEGtmLgxgq6D73506NbVLte_UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دنی کارواخال کاپیتان 34 ساله تیم رئال مادرید امشب آخرین بازی خود را برای کهکشانی‌ها انجام خواهد داد و رسما از این تیم جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/persiana_Soccer/22270" target="_blank">📅 12:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22269">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=mo8zVLWKK0X5nFxLD1AFjGXPs9PibBTRqKsOewL3Qc32XMKzbKPHvALZq_aNfFnQUwiqJRg0cq6zMbWWOBMZjkQJ8w19GxFn8xwBs8xYW6El8BPcfNYvwX2Gs0W2ZaF2MmccTIL6T6uk7bqITiccODlUNfjKo4mvxx6BCJCDZpNWVFbov2Sc_zlreH7DdU4YBkCxORl2_y61VzUKFZ1UcQQ87wgt9rdBiIb0lDvKgrkZwIaktZkNJAe0CuZT_SsLwBYXbpctQKeMhPrVanRw9vxYHQna9tBNGaYCVHZQOqBhZPnRKy5skAdGFgU-dmOZtxkB9yAryNXoa_ar8LuxuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=mo8zVLWKK0X5nFxLD1AFjGXPs9PibBTRqKsOewL3Qc32XMKzbKPHvALZq_aNfFnQUwiqJRg0cq6zMbWWOBMZjkQJ8w19GxFn8xwBs8xYW6El8BPcfNYvwX2Gs0W2ZaF2MmccTIL6T6uk7bqITiccODlUNfjKo4mvxx6BCJCDZpNWVFbov2Sc_zlreH7DdU4YBkCxORl2_y61VzUKFZ1UcQQ87wgt9rdBiIb0lDvKgrkZwIaktZkNJAe0CuZT_SsLwBYXbpctQKeMhPrVanRw9vxYHQna9tBNGaYCVHZQOqBhZPnRKy5skAdGFgU-dmOZtxkB9yAryNXoa_ar8LuxuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
روایت همسر ناصر حجازی از پادرمیانی برای برگشت فرهاد مجیدی به تمرینات تیم استقلال بدلیل تاخیر در حضور در تمرین بخاطر تفریح با دوست‌دخترش
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/persiana_Soccer/22269" target="_blank">📅 11:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22268">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7265d2cc05.mp4?token=PeeMqGk0hR9nyniq1t5o5EtLPKVcbAYtR33ZjujhTj30-5fH_qrPj2gxDqbAr0sC6XyShzmsTuVba1D-5rH0o89xQoyeYsSFlEbfmDoUt-pVjhv-IcbUs6sF_DwJ_FXx5zSyldRQ5oyEnTrHNcUn6bsikfP-snG7lgSuLBPmU3wgY7K7sb5kdGLN18WQZsQQT9kIFmV3RPe9xOStLe7pWizZOXO4FrDCAdj9Ye2Lw3N-pK8gQ23GWCZxqatPZd3nAl82UjpSjnZgWF6vbGIacR2t3_HnW4K3m-PDs5awUNZfPgKmgR6RwYmcXYKf7NO7UPcOkhwwv9SILzT1hiqQSTYndWj6K7fdavLmZq2Dd6pxv8KhyOgOOiEov3RUVp2Wa2fuHk5rgt97cWRLX472tSZp_5aNxg9dR-JNsIVM_23M6LaZvzpeSxBivXmaxqDJ1b0d3lbUHT05hftf-tDWMVcZU-YuK4F8pIN7Sgioh-WEJfNDXdGfXvYzvDzQ_IbiaZpzLKz9Dt9eZkaxNV8MpwifHXrnR73FziVMyArnmmXFHtbKo06P0RlgufQTh9J9Fc3xFArXywjiUYaUO4Tgh-gcg1wNga_JS0Ui19X-_VyG-JMQyTjqX4Vq-1DUUV9XiVFcK85mnQFbxBf5h7CA0xIrpTop46T20lTYueOtqnE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7265d2cc05.mp4?token=PeeMqGk0hR9nyniq1t5o5EtLPKVcbAYtR33ZjujhTj30-5fH_qrPj2gxDqbAr0sC6XyShzmsTuVba1D-5rH0o89xQoyeYsSFlEbfmDoUt-pVjhv-IcbUs6sF_DwJ_FXx5zSyldRQ5oyEnTrHNcUn6bsikfP-snG7lgSuLBPmU3wgY7K7sb5kdGLN18WQZsQQT9kIFmV3RPe9xOStLe7pWizZOXO4FrDCAdj9Ye2Lw3N-pK8gQ23GWCZxqatPZd3nAl82UjpSjnZgWF6vbGIacR2t3_HnW4K3m-PDs5awUNZfPgKmgR6RwYmcXYKf7NO7UPcOkhwwv9SILzT1hiqQSTYndWj6K7fdavLmZq2Dd6pxv8KhyOgOOiEov3RUVp2Wa2fuHk5rgt97cWRLX472tSZp_5aNxg9dR-JNsIVM_23M6LaZvzpeSxBivXmaxqDJ1b0d3lbUHT05hftf-tDWMVcZU-YuK4F8pIN7Sgioh-WEJfNDXdGfXvYzvDzQ_IbiaZpzLKz9Dt9eZkaxNV8MpwifHXrnR73FziVMyArnmmXFHtbKo06P0RlgufQTh9J9Fc3xFArXywjiUYaUO4Tgh-gcg1wNga_JS0Ui19X-_VyG-JMQyTjqX4Vq-1DUUV9XiVFcK85mnQFbxBf5h7CA0xIrpTop46T20lTYueOtqnE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌از تکنیک‌ ناب‌ودیدنی نیمار جونیور فوق ستاره برزیلی‌تاریخ‌فوتبال در دوران حضور در PSG
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/persiana_Soccer/22268" target="_blank">📅 19:58 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22267">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1fmBwpIyar1TGBTY_-8GpY5MiUiXB031lEWAVJ17fu3T1HVT9I9ClHY6ZdtzCCDRuTF2nLvyKpQza9yvgCLJU00YZHyFLEBZaVI-dches5ucd3btI76frc_on60w9gQcM8QDY-AtGFcD0DoxKFlSHwNVsZLhax-a4dy9rg7tIJ5SUbLa39YSVy3U-isJhltxPxTdy7Gy68h4GDfJ0F4OSSOKQxWQ7v75YWip-jEsyIcvwVR9MTlBmL_-1_hQhxv0S_AwaHm9kkZRcjS5dHxD0vMjLQLn9v8zSYCOPXPDMWLl5lFx6O24Q7IVw4LKzJJlCldrvUC4cb-GvGmKiF4Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعدادی خبر نقل‌وانتقالاتی‌دستمون رسیده. انشالله نت همه وصل شه همه رو خواهیم گذاشت. باشگاه‌ها نقل و انتقالات خود را از اواسط خرداد آغاز خواهند کرد. همانطور که پیش تر گفتیم لیگ امسال ادامه نخواهد داشت و تیم‌ها آماده‌فصل‌جدیدرقابت‌ها خواهند شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/persiana_Soccer/22267" target="_blank">📅 19:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22266">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUGCMxF2Tl_QXcuOj66GZzmPecy8XPmtoVsfLYAfe3lB_ZP1Tta8TNxkY3ai95D427FqrJYtzTtc-zSpISNjExpoR-j4fRvQycQCrtoPptgGUHkJK33rnWZ0RCgcvqgbTUf1gHegQShZHHYLjd18O1W6sMfIyjkbjyL18EecGbMf0q8I8MvAyuhEAF3xLLeP6vwsRv48fgWOwQ6is-VHxyapCCGFrro-IsTzrYS0ccbrn4tH4ZRtaxMAxJNAAYGRWT-lFypqKT4lAh1arg3faB_FX8AniHgPP4IBfWdlGKMi-D0iHcXWUZfV7drajZpxKuUj0Obxc0O3Jlw6zo3Log.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/22266" target="_blank">📅 19:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22265">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgraCYgUY2zlyHaF8ojpcy86920YwPoEnw8iWUdw73-E3Hc1US155ha98OGZN4pIQxTtWUIbzmUCUJhG2Bsk15zfIdglRbO1-a6FZg8DHGu4Mj4IYrMflx7s5UbMBh0aPAEvR1xL_S6_iLhAuBkisVRYVZX9S7wvljJrR6BUQ8NOHG8fdYbTGR8ZMNQPhB1T7T_Oyf10RhvGzPvtQYzIuWbYcTQ29dwDN9mKhhGkwgtZXqk1dn1cd6cmQe_0F5YBrzBAM2RwXbjbIePdeaJ_EN_DlZ12lcVatORE0gdKXsQ7skpblY03qDLDPKp0Egwvefu-0VuDXLfwvtiCAH-aNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رسمی: پایان راه آلابا در مادرید؛ با اعلام رئال مادرید، داوید آلابا، پس‌از پنج فصل، مادرید را ترک خواهد کرد و در تابستان، بازیکن آزاد خواهد بود.
‼️
داوید آلابای ۳۳ ساله، ۱۳۱ بار برای رئال به میدان رفت، ۵ گل و ۹ پاس‌گل ثبت کرد و ۲ بار فاتح لالیگا، لیگ قهرمانان…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/22265" target="_blank">📅 19:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22263">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEzVyH6iN3rXl56UDM2BU4pf9TK-UnSpMsLZTCoMnItyKd-Rt0Y_OSO9KRWho0J4nGpwqr7rPiAjS8h4zcVpUdmOFxzrnKy3scjdiUuLFQ9X_ioNg3Yu6Dj7Al-0OiNIsg1sBlv2uf9MuqEdvmJEJLNZigiGkd76bgjE6ZUIrOmJZqjxaWqneU0Wnz8tvkNCyrfspcrFmajd2ms7sYeyuAv4zlgt6o72KI2HANsiSqA735E_X-hKwaQYa1KFIvss-65bVviUPgNlsZDLrPvNY1qkU2uYDDgPDjpi7fD2digKfnNsE15fk2UQ-VkUDBKYLg7W5yVOlk7qYchSR-3A9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22263" target="_blank">📅 19:17 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22262">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TE7p2ITtobQdo6zMltKvn5C9CeSeltOsBvICH4M06qPDWHePd6vYyKT0QxQgpnSPA6zcq42mOnuhqzNhsy1JWMOAdmjoVdDRl0fmF8zjwePJmpCs1T7bCUN1NWFrrA8prM4St8iLcZAmXkOVo9eQ9SzQJfvsFeqgKBxGWFseRSalq0ViIHeA5WOtcPlTfK0XLAD2wKj7WZeSc76tw72BTiIEHucyVOg0cR9fN6f4365pv1NmsF-6HxvzUF5kZrBwvKz8_UXy1KpROjC-JBfXys_i2Gb4k6x6DjAh4OoXwtjrOaNBNKipJPytDio-eUkgROh7TMShMhEO5ErxkhpQrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌کامل‌مرحله گروهی رقابت‌های جام جهانی 2026 در یک قاب ؛ جام جهانی 2026 از تاریخ 21 خرداد ماه تا 28 تیرباحضور 48 تیم به میزبانی سه کشور آمریکا، کانادا و مکزیک برگزار خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/22262" target="_blank">📅 18:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22261">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sU9z1DPvbHOVMYli6skDIlP6LPSRPVQ3iuLeLcQwuekptZrbVMED4GHqjMosk4DhaLyZqo7yhoQICdIbsY4nCjnkE2l9i0urZrL-k7Ryx6q6l18l5NnujvusUF_TI6HRhy79Ahyj75NEqNf0Jsm_iXF9qHhs54nm_Mpxt9o47-XRVhx8d9vwxfp5g7DFjSlzw1Nu7QKIQArYdUzKLbZABIVFGPCt-t-sncVgOvP21n0pRtbXD4X1Fl9KDqZl3FTL6yTL6GU9xqhLUHGhnx_GQ0k1PCM-dogf6oY238Ws-2pY2oH2CrhtrlcXSDOWeNFADkHbxRiucq0V95H6utvKAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌کامل‌مرحله گروهی رقابت‌های جام جهانی 2026 در یک قاب ؛ جام جهانی 2026 از تاریخ 21 خرداد ماه تا 28 تیرباحضور 48 تیم به میزبانی سه کشور آمریکا، کانادا و مکزیک برگزار خواهد شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22261" target="_blank">📅 18:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22260">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQoa2OojRxgECTcQaz0dgEVYH10gu1RNbHyGq84NokQrcOXr4rYkWopP7ckvZveCo84-bnflgDSbzOOI0iaDRE3im7RPcnBQ1ZUYLcK9PeMl1WRIgpNycyHRroOUzB_Wz6rJG9uSy9L8fM2gfoUun074p-aq78qDG4t0y4fK0UHiKwjpCm99EAldHK__cVIrlCg42Ep5iuijBoIbduhO1DG3liuv1qpnmlJD1ttKTnOWCao1jIYfy5Rqc3SjpanYKyXawDWlyghb9Icp1nNB548xZC433w1cqHZbvnfGWYrCbQleF8ZjlwpRDlmVoGdd-Rp2axcaFqIZRK4Z0dI_bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛
باشگاه تراکتور قصد داره درصورت جدایی علیرضا بیرانوند در نقل و انتقالات‌تابستونی با محمد خلیفه گلر جوان آلومینیوم اراک قراردادی‌چهار ساله امضاکنه و حتی صحبت‌های اولیه با ایجنت این بازیکن نیز انجام شده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/22260" target="_blank">📅 15:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22259">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0NI8An5jqSpnClTyI44_FeAYhLfnvEg4ype3qvabjF_FaIJbRysMCJh-k080IIf0Khbi8s3aZoK3XhkxRPg14bcwXn-_gjiMt8cMy3i_wH_FprfBPOY_IS-FnOAReYY4D9h3fdxjtQF5BNWC0S42WWBh_Ch_8IUq2YP0KNvszSGchO2cdA8T-3nVAk1KJ2WztfgCaaM4VZEnH6rPaB2Z91lQ2EAVWNdgO9GyDojFVu3bCMVnOgomX9M-EGj-doewlIQA052YphseUBHhV30lNjxnDggh5zJOpIZoIKQIPSvQD2a2gm4-wWgQySMdpfMIWO9yH3nLta8Zs1Kfuo6Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب منتخب فوق ستاره‌‌هایی که جام جهانی 2026 رو مفت و عین آب خوردن از دست دادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/22259" target="_blank">📅 15:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22258">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8j9XyhxOKAb91RpD2rcONKiJAwSCI8UQ59BiEkTjbeIC8TDgNJvx1gW93OE8IpZ0nQonDNLRr9rwkK1yM37iMyMnUzTen0ek-sMa3Ykze38MF0ZjJUTCSgT7rCaQKdsVWEDTcqpIYJZdSdLAnx975--TPqQ2B4sfulv_9ieexM47HX_iBI0TNsCdhHD2txAuART_Aol1eibGnlkRUOl63KBiiOjcObvrV-zGHL9Frzu3UAO7hL5fLsa_lSnU3KPYu6aQ8lp6pMXl6fGYUqp8V-Jyl85H4J1SN4DOZpIej9zh_3REGHDh3X1OQ1oU_sOliXfQ2TRgRq8eGtoF8VVVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برونو فرناندز ستاره تیم منچستر یونایتد به عنوان بهترین بازیکن فصل ۲۰۲۵/۲۶ لیگ جزیره انتخاب شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22258" target="_blank">📅 13:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22257">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKHNUakIuqcBAajW5cbKqWYO5jojwEBhbWlJhOxWN5IuPwDiztTc3zQiR5iZ2RMVKeMrLeBqlyH-7DWn-Mbj427GaB19VU7UMbsZOuSfJ5c5G0BxMQ6646LNoGkDtFnb3sulLoVzA8DzLWuuGuLrIvzp5ODUlh1qazJbu7hZJ8BEUtSLyolA53osZPpTS_OwCKx1V306yKlOtssS8DcbWLaAXRsBNgTWeVuzIb-jv0KcpGgzoZNR2E1RqZOIshM7-jk-GEUj5F1qZ-hO6umTAQAFtq7ln-1xJIilElcfIZTC5ul5-j7Ds6aRQhPga08YK6noBnSBShF3k9arwF68qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاتر از رونالدو و سایر ستاره‌ها؛ ژائو فیلیکس ستاره پرتغالی النصر به عنوان بهترین بازیکن لیگ عربستان نیز انتخاب شد. ۳۳ مسابقه، ۲۰ گل و ۱۴ پاس گل  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22257" target="_blank">📅 13:36 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22256">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTAI0-ev3mBFTbYFPhi5hy6sUCaXK1GaIwnkQ5ZT0iu8h68-KHP92rhXAsj3PEuFJmsJVSNLjRahyIVZfvFqXPFZQSL7T5aZFhPg5C5Aj4DGbvdxZ50G0vfe1lFgO0lep2VgqbU7Z4eDnZ9C1k3om5sIdesktAa8Q_UR3UVH9QSW_pS6v_KRgvQ_5YKNYO4hvZVEaALokiPPZEr1hAQISAjZPuF5LV6OnDGbhOqAEVQWt8YRwl_Byj11UiFDWYu2YMi2lYtfN31OO9QXZPQwT4JOiOb4Ss759Jp8HKOR5TN638K80r8llMD-48Grnu93-EgH1i6xrnSh1xEFc4WHxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسعودپزشکیان‌رئیس‌جمهور: اینترنت بخش جدا نشدنی زندگی مردم شده. دستور دادم با نظر رهبری و در جهت رفاه مردم ایران بین المللی وصل شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22256" target="_blank">📅 13:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22255">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKJfr5SX-yJF8td67syYWkUc4r0kCFTG_hwM280J55-gIWrHlOoZ4Dh-AWN1Xj89lPdtMqlAcXmKmz12qPOthITKczrHdRh5kRtJ1JrVGd0rxHsJeHC62w0Vx8TqWKgkqVabLf90q3tYhBNtqNfF0xwVpqPgfDAcvQa_2Mvgzhg1U99cIAwHxaDMInQ3b-7arPDIs59DoNV0752vAqJzpl63eoCB6VOSLbyxeme0SvmRHwnO1aqoa_pOUCwKrpQQ4CaDYwvpZBT_1XBIYfgI0PENHa1843dtgjQIdVMdSMGeL3lwUZrdYn_IXh9g0wNVhWtuJlhbCRhWMwoSAgMhBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاتر از رونالدو و سایر ستاره‌ها؛ ژائو فیلیکس ستاره پرتغالی النصر به عنوان بهترین بازیکن لیگ عربستان نیز انتخاب شد. ۳۳ مسابقه، ۲۰ گل و ۱۴ پاس گل  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/22255" target="_blank">📅 13:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22253">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8dSNoIh-fzvj1v5G1B-Dc5W2kGKzOhrQiYhKfWN3YPv8BTl92uzDYuxeW85Aqv8GY6FIId1gPceS2rW3XbEk0J-kNSjqtxGUiLgyze2xTXaPkgUk22Fsj0miN8fdfyE6oy5hSPzlMHi80Lc3HNpk-5nA_PMI6Mc_etRXH-k0_ZFAAuILu-X7UjXK3ZsTQ7q2jE2FUekT4lk2U8E18IZZp5M2U-khbQEQvQtVV729aLRLpVZXBjPJQoh1f5AJAzS8BlAqJsVsK699dwOxY4hwaOfEgcDY4za1AQr6qFuoghdIoj-9liMdDumvhgYvR__jFq92NzHjb6D27_TfPHp0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فکت؛ کریس‌رونالدو به‌اولین‌بازیکن تاریخ فوتبال تبدیل شد که در چهار لیگ مختلف قهرمان شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/22253" target="_blank">📅 13:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22252">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7zdE0bB4D46QOpfIminskU3-kGGRZUK8-4gOoluke9Cr3H-P3BLqq9OjPvijt_blUarofOYgKjkQ_haL0SBFcOV8RVFqju0TAh7FeaS5vrgDoGxMyyMfYm0c04rA2fD1hhYT6kzq7g4SpjT_wZTmhciu_x-n6Awr3MCXqnYPuk-Qz480qzi377kN-FWNRxjHgDjSjYg1mOEK9b7M0HS9y0J0Y_pUZG7iUNncAVp_5UBCAnOXLresIxvrSOb1FTHp8cUcHse13xcyKzgnFzb2P02wt4im4bMC5hHRnV3G-1q1iMkST01sX_kafn0L-uUwuibJjmtU95oRgbJOsM-VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تیم منتخب فوق ستاره‌های توماس توخل برای جام جهانی به تیم‌ملی‌انگلیس دعوت نکرد؛ توخل در مقدماتی جام‌جهانی‌نتایج خیریه‌کننده ای با سه شیر ها گرفته بود اما درصورت عدم نتیجه گیری در جام جهانی قطعا مقصر اصلی این اتفاق خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/persiana_Soccer/22252" target="_blank">📅 00:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22251">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9DDJbHekplwECBMfOPTnA8JV-yofKn3kv6UP0HDZjCBgabqfObRxsLAlldedQMnKwOub9lQbst018DQsNBswGthGL0qEfLfsvu14eMlgApp4B2DI7oZkXiG9eOd2aMFQ_yBZ06AGF08L3fog3mkCu0OzyJ0MtvExKRzNBQjgaTNBaXJgznzKpN4XkcT22NK6M9FBNL0j8PoJWRGw_bRLg5UJS1rxhb2PgBxS2-5PQKvKyf_FUwtjJzvKJCKIUroWcHEchFx3JmKhJjWS8MqprggODPAGJBZWkxnoaj200w3ohDY2SsrxyFg5xwEzNEwjTQ0Ohk9UQhyNcstd7BtUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیران تمام باشگاه‌های لیگ برتری به غیر از باشگاه پرسپولیس تهران امروز صبح طی نامه‌ای رسمی به فدراسیون‌فوتبال اعلام کرده‌اند توان ادامه برگزاری مسابقات این فصل بعد از اتمام جام جهانی ندارند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/persiana_Soccer/22251" target="_blank">📅 00:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22250">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCY_zWXsr3fC_D_nJHxQbuv0cT_ry99gkIfguDNopPlfksvakvrP6zpHjdZupxt0AleqAdvBfitphMawlL_4z39ZNjZndQ5u6DfRuA7nnD2yrCPD6kRhNDF-tFvNgGruiT-fxsBxQ1aUIJm6GlTfzPHGxUBZOueoPYgXyEZ1dgve4bSraV86c0LO5grN3yWOUx7RpNY7T2ikv_S7CEf3A1J2RUGnUwSDfnJZ2uvnPaEQglFxfeklPxYTlNfbJP4mE67aOGGCUIjdiFlKJCw7QzZM-PEyDnkbGd2aqrqktTJvIDwngPDyAqjTHqwXEJLgKAAL4Kdc-F4QipfkJdWG9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیران تمام باشگاه‌های لیگ برتری به غیر از باشگاه پرسپولیس تهران امروز صبح طی نامه‌ای رسمی به فدراسیون‌فوتبال اعلام کرده‌اند توان ادامه برگزاری مسابقات این فصل بعد از اتمام جام جهانی ندارند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/22250" target="_blank">📅 21:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22249">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPIuQhRhAvuZ2Ae8h7TQ6yQRAxO0u6prtrm5oi1WJ3U4C8zd80BrPF8PHiNir7VJ4yKTI1wfB1uqxqSWHo-JdErgnCjqLn5cq0OSChMpB0F6UwwPK5DOjf33TQ_p8WVgZ-gUAVZFRLIQNAvWAXO-uncMw3JwC0nH9CFP2PlbMLDmTLb5oxWABbMvWnWWF2BVDkHiNG5DYBOmVFOlNRup9ePkAojvk2m_TBwrUG3tDHUPiEIdwGQoIv2uritbaD6DJlGAjOvwHCMgxE4jlBgjm8V4IdYdCfglTiu84_ZHtpTyzKMKQNo6L2_RxSngQBP_4qmA5Vwpc4J6zzivrsAG8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه اتلتیک: باشگاه رئال مادرید به داوید آلابا اعلام کرده که درپایان‌فصل‌قراردادش تمدید نمیشود و رسما در لیست مازاد کهکشانی ها قرار میگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/22249" target="_blank">📅 21:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22248">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WOQHctUX9cPtU9nrErxK0iPyBa-Ck_xgcU-vDjwPW1RIwFtFvgQFoV3AvqB_zauHkLkk8S9E38jcMRwYSH1CBu_rSzJkfbjzUyuE8tTX1lko-HafQbq0lEt_BSRLU7GQpe9dAV0TmP4KjZfY6lVlIGkyq7fevUfFprugv7LvDgSY2ZjQ87bZJ1Um17K2AMDYeVNYXJ8pDJmlBvCfM-py_akIZRuFTOX1qCw4cUN74JO3MOsJ0qT8CxPU6IgBl01n-YGwDRCUrVlKF1_fyYguUsPbhedMbhtVEA87r33Qvlx6rZFAh_sHYRHR3QkCE9eSrgIVmnqjaFO8hVr8kKwDdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست‌نهایی تیم‌ملی انگلیس برای جام‌جهانی؛ نفرات سرشناسی مثل کول‌پالمر، آرنولد و فودن از فهرست‌نهایی توماس‌توخل خط خوردند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/persiana_Soccer/22248" target="_blank">📅 20:22 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22247">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPFXd2asQS2CJTDqAFl0Ggm-BY6uPXPHa9_iBsYpotbeQ8XMrol90m0j3lPejI8y2GjhcWU9Hya-b-sv_qfbrTNJA3Ud5X6oDAMVKwhQLrP1dHoLhGA4vuccPMiedPbe94UrjL0ClPnG80ByHWh3nLWgtf2AkHFdq-EWdhxy9MAfCHmJvZx_sWIbDDetwc2FukWEyT4lpTR3PAadx72-rhm98-UUJsCrOBJsswqPx88kOUhSavpSrMc2BMhx6FNEf34sasJkUB1EcQkCDM5S3DtzyhSaCQR0kiaxQfgkcQohBHkaC8_k3vZgQTxhjYgJbdsdEFcwCm7sKnf2Ik2V6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه استقلال از طریق یک وکیل ایتالیایی مکاتبات خود را با فیفا برای بازکردن قطعی‌پنجره نقل‌وانتقالاتی آبی‌ها در تابستون آغاز کرده است. برخلاف‌پنجره قبلی احتمال باز شدن پنجره آبی پوشان در تابستون بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/persiana_Soccer/22247" target="_blank">📅 20:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22246">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MT9qYlDyEBLR8Bophen7xjPHDNwABwWzuE_KKRMuGvc7nJ4QnfE69KA1bChEoaePIMq2fskKUAWLHiNDlpDWjfIAX_E_av4yUmRpmT1iqUNRteBjtXbtobV1mZJ1y2HcbqsB-AFZvwrXSNE19cG7QT8IzdWZ9dy8GIdelT1v8T-eTFEVAlr4h_2Zh-BqRuSWIQWpLwG9HI39Wrcs5P8Bg1C9_3id-IVTA47PTt0MLwE_2Y13Wpn8bxwI_fozxbjko3POUjUTaEgfo-5uV9OgEAsytjgG882VkCGow6ccVOHYMrLe-wR0HMMnHt6bS7Sr1OHmC3HMRGrO-WeoSnP4nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
ایوان سانچز وینگر اسپانیایی سپاهان بعد از دیدار آسیایی این‌تیم به‌احتمال‌فراوان از جمع طلایی پوشان زاینده رود جداخواهدشد. سانچز از شرایطش در ایران بعد از کشتار مردم بی گناه راضی نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/22246" target="_blank">📅 17:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22245">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cdb0d3e03.mp4?token=hVWzoRItHyeWg2YIygxMTg8h4KSLhmQF3A-dyjoHKWHq8Orxb0QsiWh5bjTOJSCiUDfWyDWfYSlVUOtZo8M0jAuDImkYCISUTuMXqQrhv2DKqGZlG0nA6azBI3KOyhxic1y85ApJAntafgP2XeARLs4Qk65WbndAWp1sCqx3S2v4lTtQg5gbIfA1CqfJ77x6snVg15t53GA9IeqKhLqCI04CqiK1vYlJKAf0nNJekTuDw0gEmo0bV6YOZUYNKG8SS60y5S5juA2Hj0TFm64bSI7Z2Mbyu-RfcWpu9p96-Y05tVFFu0SCdPDKKNt3htjO0KbmA6w-hm0FlVRUy-Sq-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cdb0d3e03.mp4?token=hVWzoRItHyeWg2YIygxMTg8h4KSLhmQF3A-dyjoHKWHq8Orxb0QsiWh5bjTOJSCiUDfWyDWfYSlVUOtZo8M0jAuDImkYCISUTuMXqQrhv2DKqGZlG0nA6azBI3KOyhxic1y85ApJAntafgP2XeARLs4Qk65WbndAWp1sCqx3S2v4lTtQg5gbIfA1CqfJ77x6snVg15t53GA9IeqKhLqCI04CqiK1vYlJKAf0nNJekTuDw0gEmo0bV6YOZUYNKG8SS60y5S5juA2Hj0TFm64bSI7Z2Mbyu-RfcWpu9p96-Y05tVFFu0SCdPDKKNt3htjO0KbmA6w-hm0FlVRUy-Sq-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش‌بینی‌جذاب و جالب از فینال لیگ قهرمانان اروپا امسال؛سال‌رویایی و تاریخی آرسنال تکمیل میشود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/22245" target="_blank">📅 16:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22244">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gW22OB7XMX2xfzUa2glCY9bi486A5LGRfXGE114R9qXHjXIcWhUEDwu7N1bzhS3W4I-Z6An4E8GDF485O92ygxTdluRHaiA_384WA9FqmVPOoF8gPxfWIuzO51zZLPcVFl-WU-ZOuqLeCpzoGJZvLtX5Chtr-pqz7NqP7OSf51oGEXnXXQohWDH5khV1wH1lDvnjr_dFfBozCD5loaRbEkSTR6V97My_rLAioSbphJ4C185iJJRWBuG9KVgl7rHE36v3r7uHX2X8tiKuQC9UR7D6x9mBN6cVGLvDv89tXeiXZIndXuunpIsjVEFnszTCs9FFRPrRttmpnjtysQLWqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شانس قهرمانی تمام تیم‌های ملی در رقابت های جام‌جهانی2026همه‌تیم‌هاباصدر؛
اسپانیا در صدر.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/22244" target="_blank">📅 15:42 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22243">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2V8pKDqEZ-StEBdeL3opzbnLebe3Ij1YrAIubH5cZAHRLHdMry7JC4zVoOZb8Q-CXRSCSem9BJ6BojtUar_9IqFN92JvdgB1XP7XeDSDPYoCTRMe-57rkjS3I3nbQoY0p8dSXF7sbqsSY0c8PK_io2nV7SNkKU-uVl-E70Wf1Ret68EPCqHrkNG0YUVvx3Jay_H36ZNre9Qo0tljVvcXV3357XXzVHbt8UkOuNwlfLItJ3UJdfOGJ6q0XcgggGIba3joKWF7WlhOerpXgVFV8vAMk_yHEZyADzavRX3XUL4P8kV4hMQn65Q5Yd9aKLIu8SzMWxGg8gl6iZ91loblA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ علی تاجرنیا صحبت هایی با وکیل علیرضا بیرانوند انجام داده تا درصورتیکه پنجره آبی‌ها در تابستان باز شود بیرو پس‌از کش و قوس های فراوان آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/persiana_Soccer/22243" target="_blank">📅 15:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22242">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2vHTTB3bieDvYnGL_HaNq_GytFYXs1nzEKSI3nwLwTw_5NovCstkFpP5M6ePNxpFI0L6gxGHetnyC72meiYU4cd9MSwhOxXNb-DpDPiS4aVhwPMxNvKz3HRyl4kqAQWJa1vJOCcOUB59FDkE2ozynDBf9DYC3NI6Y_-qcUcxyK7xi8YF70uRK9FhO0-jJvtyPns8VZqpa7UU55dZTuFEAVa7Sb9DUdYpZ8WGjUr4VLJAcTwFz1x5z9OWMK-SRC-YoKLK2RBT2osdx7tsRyolPZLYevMPJAt2SykS7pp0AVqcGPzuhVoj_ihp-OkE5SMorzOt77OVWi_kEy66eFOXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان تااین‌لحظه نتونسته مجوز حرفه‌‌ای خود را از AFC دریافت‌کند و ممکن است درصورتیکه مجوزحرفه‌ای‌این‌باشگاه صادرنشود یکی از دو باشگاه گل‌گهرسیرجان یا پرسپولیس تهران جایگرین این تیم در سطح دو رقابت‌های لیگ قهرمانان آسیا شوند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/22242" target="_blank">📅 14:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22241">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRkCLooFaomWu7BVjufkTc4yhd2SowNMlJuRsW2rorG6gtGH5Nri8pt7q_iCitgDJUIGwyQK91ySL0JrWEzv-6WULSbEJDCnL_uiX1nKPT2XqLre3bIldOLq-4xCag0YblPHIPgX4q4HwuurX7D-D8woQIKDoUGvzOEkjemhy9loLwgsurX0sR9GsrJTgnaTyhCybw154hz_KB3UO5vwIlwWt7ui7hz4R7XDGpG58i6qXejF6aVCzDRLzd9JevJtFieQYSn9nXuS1Q0DYJwITY_gl35-L9qm6JLMga11oYu7TGz3LtXVHfbiz5hvJN16iRz4jj0qPszt73Ltutfz-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
با‌ اعلام رسمی باشگاه منچسترسیتی، پپ‌ گواردیولا پس از ۱۰ سال درخشش در قامت سرمربی این‌تیم از جمع‌ سیتیزن‌ها جدا شد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/22241" target="_blank">📅 14:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22240">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avgUzs5VC9f1jsV8Uutozox9hktykbTNKsKMDP3TKZk73rfEJFiOl0nP7Xk8QJav0mXOPZ4c8MgB8svocktemQnxwn4y6WCKWkF2wOPfHFo7sAQiLPHteHHFBywJunAVYc52KaUBQWhIdHOTfFbNqgH6HA93L8lSo50dgbT7RXTfYoKUhwDz86kPJhSv_LzTVTocEzDYwJhCTrgh4X4ZuZi-zqVc3eo0eJ8xisUzMxHPk3pjfFw75ZkMVHbe2gh-MLiob_tSaei1yacI6faJzTMJW0-Cf-Omopz8vZlgF2cZK8iQzh_opLGen7NlZfFXTlcgfopG04jUjyjQVYC93Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
مایکل‌کریک با عقد قراردادی تا سال 2028 رسما به عنوان سرمربی دائم منچستریونایتد منصوب شد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22240" target="_blank">📅 14:09 · 01 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
