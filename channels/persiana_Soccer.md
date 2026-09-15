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
<img src="https://cdn4.telesco.pe/file/pMrgRbT3mgH68o5QK7N0rlCkGX5a4mxeDZgpZSTs5zhOn-cUoLRMrvPpUd9tNWuu6r_LgEF7J0yYGPo_8LZb7jbn9RztzGPE9P3LCFPzVzgHkIwxbxe3Dv5xlnHjT1p0gGWcoSPO-MaFd1KH4FqeM6j9usksFrIAKCn56KIBdMQTJAhJ-ddmfH78cBlrbjJSsbNVPBTZIo3UhRk5GUol17a9uI-NTX3-Ooi9UOZf2MZPPAeDm-4eyEJi-KVEhtOfrF2VoKqvvFsWgtW5grP26lwakyuRO5QD3D4Yi3HV_VOL4kYA2qWsdq_AbV5CPoPlsXSlaJ1MpvpI7rhj1pUsNQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 509K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-24 15:26:15</div>
<hr>

<div class="tg-post" id="msg-29807">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrUDIQUyXDRK3yVLrW73iIp0zjA_BAWQ1BFeCkRft2_viZHhf7Y4h1wm2YyMvWyM-GuUsRCMujZgbBaZZihTVDFi8OBI4ugGTHDc9kI7eHqDZR9AkjuGO7V_ogSngPP_RJMjAFnKI0pic6gCLa3qv4jA1gJiyl3s9tLL8ADKLA4Zl29Yl4BDMvzpkgTPCRai_wudYg9tdc-Ny0liylt9By5jTQTjH__JF0KhyuB6dwOXqhO97QX8hcJ_pwQ-FVJKwerskNREqm1TX9-R3QoZ1-cEPgvxbtcsXgUqyNFY2-u9xsCbdlQRm_TXWQ9Z5hlfPspyNMhvC6-gRAzvNzPM3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قابل‌توجه‌مفت خورایی که با گذشت حدود چهار سال هنوز نتونستن‌آزادی روبازسازی‌کنند؛ ورزشگاهی که دیشب‌استقلال دربصره‌عراق از السد میزبانی کرد ۶۵ هزارگنجایش‌داشت و ساخته‌شرکت‌های آمریکایی بین‌سال‌های۲۰۰۹ تا ۲۰۱۳ بوده. هزینه‌ساخت مجموعه به همراه استادیوم ۵۵۰ میلیون دلار گزارش شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/persiana_Soccer/29807" target="_blank">📅 15:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29806">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAZUuudk51XK-HZlQRPedNCk6zRDZItPQlAHrvIj02C9uv_eGG9lwb8ide3o1hijov556zIYQ4wIrnFw77M6BldG48tBBklEMRru1LDBAeVa2psFGQPehmY9IxGMzqT-68v7w0EFmx-utn6rEH9yh0PuRQhi4fkvF3LYtEGrjwvuwJDy9LhpvZ4lgFbQPJfiq0K87aby09eiIVpCi7jwePO7j-9hq0_Rr4qhFlKMPrW40VXmC3S4fOWN7kOREXDOXAiBGJu8Njclk-cAcaZv6pQ9OywklAvYMgIUaCqXwQbL1icT6YQPlEiUQalli-QqFpAjHQG9f6yrCxfJwZ2Aiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚫️
🔵
طبق شنیده‌های رسانه پرشیانا؛ مدیریت هلدینگ خلیج‌فارس پاداش 500 میلیون تومانی برای بازیکنان استقلال درصورت پیروزی امشب آبی‌پوشان مقابل السد قطر در هفته اول ACL تعیین کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/29806" target="_blank">📅 14:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29805">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdv7NG0fsc_QnztDr4SZkqPO9vW7cjBdFDYdN5T5-z5U_4C5oYQDAcwkJ8qbtyXto4EfVaqdKyqCj3beLB-WartrHygEryO2f8Yo-m7F8qcrnYCg7U4MiKAiNNhqfH2WKlNVHOlBprb4PhoHc2-F9JRwodtbJocqCYVx3HY_ciPj9bJ20U2w0loif32h7REl3eOGBt5a6pWrHdfwIbN6w2ux7iY4Xi9o4wLlykWazE9P8ZuKX7lMMZHeHK6q64WYha0xFiQL7VWu5XZt_tOy2fo2OBqt9g7DKn-GtuebQ63AfJQKpNFMQKDwR7tlkPPt8hcos6h553nqvUT-cB1MYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
امیرنوری‌بازیگرسینماچندروزپیش در مصاحبه‌‌ای گفته بود که خیلی پولدارم از هفت سالگی فیلم بازی کردم و اولین خونه ام رو تو پانزده سالگی خریدم.
‼️
خلاصه‌کلی از اتفاقات مثبت زندگیش گفت. بنده خدا فکر کنم چشم‌ خورد دیشب‌ تصادف شدید کرده الان بستریه. زندگی‌خودتون رو رسانه ای نکنید لطفا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/persiana_Soccer/29805" target="_blank">📅 14:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29804">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-Yd84dbHesu2I6mzpFGOzq8w_f_VKC_h1QuX9GOMsOLOVoqt5nemaElvhDO22Psjb3f05cmsmJwKKE9dAjyauQIg8timxbF4NX9DfhSFSVYGmGvN8oedlV64EuTcJ01ZsG8RVZY5fSU_0yrFq36YgmDnsTJfxKN_TTuf_VNO1LmBLfWuOnU0fAi6dbwayonUa6k9ZSV_A63UDVvCk_QX4pRcK10cQgBrZLf8tFINNFwPBadt_gBiEMeQA6Ss5K3kLwYnb7voQZoPMUKkY9w7mH42mPEJzzRsMWaSvhPb9BxXmX4I-Lffm_Tl9SkgfMSfR_Ym7CqxEFgBMwx4y-8tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همسر سسک‌فابرگاس سرمربی‌جوان‌وموفق کومو در گفتگو با گاتزتا گفته در وهله اول اولویت فابرگاس موفقیت کومو دراین‌ فصله اما اگه درپایان فصل رئال مادرید به او پیشنهاد بدهد باعث افتخار ماست که با باشگاه رئال مادرید کار کنیم و سسک به اونجا برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/persiana_Soccer/29804" target="_blank">📅 13:57 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29803">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZ1XqGhADuWfz7MwRMUPjwUBnlurCIKW4NjmJoypq8VVVijUcMASSVDR6MYk0-RQHvezKOmuoXv_7ddFToRoh9mrVwKvXEH6-N4k0nLGFCUcdK7gnN-3mNUlyeeJ4w8DhOHHl-WK0v0TBHV5CS-6ZVfQnKj358R_WHJmXCEz4Ty_NH6R7J5l5Me5riWpTUKXS7B7RovCgLRBx5pxTAJiTuE68W4J1q0gYba3HTVmsNHV9Ed8RncL81vXJOBijjZJWat-2uuKHckF91pgH1pT-uCQWs_Hy6te8AlF2POiRdfVETIUicvdoTfxcwLbCkgXU_MMArkBJg0-YMeXPav7qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌البانیایی‌تیم استقلال برای جلسه‌مهم با علی‌تاجرنیا رئیس هیات مدیره استقلال وارد ساختمان‌باشگاه‌شد. این جلسه مربوط به تمدید قرارداد این فوق ستاره آلبانیایی است و ممکن است همین امروز قرارداد آسانی سه ساله تمدید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/29803" target="_blank">📅 13:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29802">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TALA5qbb-8uPfnBNkPk2K-yUSIhhbpzoTDXYbSNZxWdazlrl1OH78GGVrOI4M0NPOdrmwk6JxPnsx37r6Vy5CRx7QRE6LOcz8WEjImEFBNXWImqyeJ3qeKH7iMZSoWZbW1PxAWpnGl-0h5iz4HoiPGxV8in29flMmv4ZrhZcvlI262DNcMuQ54uWI0tG_UCD6Db_1qAFIQXnOrobqSV9t3iMMPs3SBYbEFCrvivStKzxvQwjnDGUN4k5csSHgPNpJ9O21YbFdrh9Y6nZOX_hAGMRIntWr_VhKB4kfklAfIRTPfcrNOdbcpwPm-gr8YVhRyugCQkewvJqg74o_QcaDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
دراتفاقی‌جالب‌وبی‌نظیر؛
در هفته چهارم رقابت های لیگ جزیره؛ لیدز یونایتد تنها تیم میزبان بود که موفق به کسب سه امتیاز شیرین مسابقه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/29802" target="_blank">📅 13:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29801">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOhqP8Qs8F6yyAfRYnwD-YPTajypokUoVWVatCjAgvmOVhfIomNWlvAM1c_kWegM_c4BTbzsDS0rQXQHoKJglBmkBwzy6ICj_VGLmQac2PiaAGLG5JTMXnOfJljJzR8xl2-xhcBfMvBhJhvd9Uu1a5uwIrJkh9a_ia3el9nYTQQi0BSKrSKsCuQigN0LJa3ogHdq47Xsgttjwu-L5egGFY4pe5xY3yRuWriMvnP5JaydNbT1fsdwEAObbtB_JkpgUshNYZfqLkaks2oafBuV96m9qop47p3DVBmfIzAI9-wfzJZzHqEUbdoTTsGvNjnJqsYUoia3c4UL-RvmWoBiIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ورزشگاه 105 هزارنفری و مدرن نیوکمپ رسما به عنوان میزبان مسابقه فینال UCL 2029 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/29801" target="_blank">📅 13:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29800">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMH5IVhTzHGuAqreYxQWbS3sFvzbRUODjydhGfA4qFtZgZmz4Z5jOxpysxhdr7g7jy2Kj2WYWERw6zNf6ZBAoGHDq8NoWT5bSLQQ8_FzzOyNVnybQaCvtYRetEPW_I7d2rHaRDWFi8_pPt46UWdU_GZaQLDcBPqzWHd0QF0Gt4rvafnJ6DWiwG-OiPFU7IAHL4ThPHL6MdzWcr8w-bKo_U8ty7dGqpcGTkH08aP3b9AVKnnhdn96v7WgQwzA-c5BWevdmnIsL6YhSwo4GxOYEV5lZdbPqXltP2qLsNZ13te59RlCU9MS1eFAKDMD_1EMT6YU5xMCacz98X16_k5uEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مدیربرنامه‌های علی قلی‌زاده امشب به محسن خلیلی گفته درنیم فصل با پرداخت 700 هزار دلار به لخ‌پوزنان میتونه موافقت مدیریت این باشگاه رو برای صادر کردن رضایت‌نامه علی قلی زاده بگیرد. خلیلی قراره با حدادی و بانک شهر در میان بگذارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/29800" target="_blank">📅 12:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29799">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5gIcugYddcxhqc1oe45nuz7-fDKObA1S6H-9dNvhq8TPH_Gzr_1zpYfyQRDq0X_UkRYcLJK05wcLrbfSmJpQOKPW1jSu7McHqNd9fEBWW0YiAj0VPAkSKcGtWyg2vhddTDxwQsnKhxX9UQXoxGaDeDorti5awKpDn0GO3Zig54E11MiMHtJjJgDcxWlF8SigLc_ekMy_PuegLcuFJr5JJPfHQUmNDtgQJ7l-Qs8IYJ3nO6ZPPJusBPJ0bWPsKh31ixrJJ_tls9nJXWBjoUXMFvkt0hxKhvhFh8gL0b_wBlt6wSW_uNO5-NxF28aU6_l6zs4nOanOBAtG1V-l5dVtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
درخواست‌عجیب‌وغریب علیرضا بیرانوند از سازمان نظام‌وظیفه: مریض هستم یه ماه سربازی ام رو بندازین عقب که بتونم برای تراکتور بازی کنم!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/29799" target="_blank">📅 12:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29798">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O18BqiBz4P4EuFj0S-lgssmghXM3JQXDG_EiCzfwZxv6RK3D9bQFn-3ykKHFvtLaIRGM5wQlFkucbFRUenKv_do2Cey_7sLDCR2KR4tsJmYW29kyw1Pr4PJihpinn3YgL5y_d9m9w9WJDE8iy0xLjKEKdAFPSJO_qtvsKzhUpOimAFM28M_XAD2IunMs1Fc1N8rQtKS7whGyHbAOUsgbyFO0Smek4ExMPTprQ0ycLF6zU6dk89Eph1BsvbSzgtYyQFm57LowOsbHPNSfVVzRXB8UT1I1F4Mmvc00f2f0fm7Rsk9pPJvcgkL2vm0dz61LS2wtYZ8q71BkLg9_Yua7HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛ تنها خروجی استقلال در نقل و انتقالات نیم‌فصل محمدرضا آزادی مهاجم  27 ساله آبی‌ها خواهد بود. مدیریت استقلال درنیم‌فصل 7 خرید خواهند داشت که جذب قایدی و حسین نژاد اصلی‌ترین اهداف هلدینگ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/29798" target="_blank">📅 12:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29796">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vE5P8hWoGMM6pdQLiv8ntdhqsNyDpCxn5tD_ocIJjbBWZdO-977H9iUxNaFj-_wtaDQ3f0cs6fMMjEuslzCDs6KdS31uGd8r7YeQHv-tcLuAY96Jzr_qKJepiEIfuMtmj6jOx3UvLQXNbdN_NVTueV1Ju5eCBXROIL1PJHyaut1juQFaYYg29cpWUYP93-L8QeDjCe6jteLejO-NOmOtx87COqDHfIDT67EjLAEua_fdrDK4MkZ-CgEXDocMhKYhcWbG02bGtNvY0K6gS8rgUktaYJe_zQvMEzLtNpTWNFRRsiGaeKa4P4QB9CDQtzqi8d0ZB35DaVgGOhge81XjsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JQesQrGQU88TTfns74rO_bunfUFQvUS1d6o23JnuHNx7vZWvbe8sJH5mCFxUs2WWg7eB1ObW0dxHj2-JOs93HYJOsdNAV3ZRASAQoGSStSYo9rXypFFU2NouVl2gvaPoI6VhDt9172Gx5s13EaAO_FfKC2zeEZFdMnaMA8p4ANkSTvtUOhZUQJHyhNOhoCOLDlQjzvZQA8l4Oa9wd0oUZh1FSMCa6UQCbEJ8PvIJaepZ_Ew3x2JYxggoZ-q8QBxqhxU-ygy3DOSlqi3zwZsD_dcs9NdcsSm12LHZyTxVhM7mlkP8A3hh5zBu2WhP5eCm3wopyCPnTCd65Xp02pOXCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
تمام قهرمانان رقابت‌ های لیگ قهرمانان آسیا از ابتدا تاکنون؛ الهلال‌پرافتخارترین تیم قاره کهن. نکته جالب این که تیم الاهلی تا همین دو سال پیش هیچ افتخاری نداشت اما درست هزینه کرد و عین باقلوا دوتا قهرمانی شیرین در این مسابقات بدست آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/29796" target="_blank">📅 11:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29795">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPYWIzRZ0Qhckvu4yC9C6Ib3Yj87MjQ7jb4NoDC4Hjr7yw97a2fOoZg65y9N6lA580epZ414VFjue8zpEx4jI3zSQBTJlYSXuEQ4K9Wo6wAOs6UKnX5GH80yNRXrqUyJD_eAnmCUicDvK4_XHr7uvDjYPPt2ENKsX9Bz6biVwg_J0PdJPfckcsIQYFr5OYq-mi-5ggSrTd2sVyQDTazUhdfWoPepg4eNLrg_5_uk5P0dzTYvCLgTaSFHXogFZaGm9HKhH41KoVjy-0q5wrH2JoVfrxnCCPGPYBSh28nB_8H7dOsZz5Isyrf3wY78L5n4bhVWXw1rJtb_hXwRfoQtkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فابیو آبرئو تا پایان نیمه اول بازی امروز بیجینگ گوان درسوپرلیگ‌چین؛ موفق به به ثبت سه گل شده که‌یکی‌ش داور بازی مردود اعلام کرد. نمره آبرئو در این بازی تا پایان نیمه اول 9.1 ثبت شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/29795" target="_blank">📅 11:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29794">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/to9iD7gAK0t08Y1ZOSbvUUamWCLnxrPJUWzGGfUFb4ah4Esi_frhzkC8WUgvQ2alo5vwgnIssvEVoX3UZLCJm7kUHQFUJC5zPvrC8tB33TK_RzlaCJz5J75HSUsFlxca-NEyXEdjt9xTWLOMbvf_xR75o2_fE2Z_x2J9Zmv4V336Lz7ckIs3HzYOtzrdhJa7wktWtgTfUZ9fIuowDXtau8Tog3IOpPgq9q3Gdyw13JuLjQ57eQMa5IwQE2bn1olbEehIgD90uaJoWWKqhfVuCNy3fqdWIo__hREvCaRUiSZ1toJFFxua4j-BSsIsY2xwQFmnT7xum-MBzRTgWvlobQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ایجنت‌ایرانی‌نزدیک‌به مدیریت تیم استقلال به فابیو آبرئو اعلام‌کرده درصورتیکه باشگاه چینی بیجینگ گوان به او پیشنهاد تمدید قرارداد داد این پیشنهاد رو رد کنه. مشاور نقل‌وانتقالاتی تاجرنیا به‌آبرئو اعلام کرده که هیچ مشکلی در ایران برای او رخ‌نخواهد داد…</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/29794" target="_blank">📅 11:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29793">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gy-zOMB9SYABT9uqIhGjm8gjr2J68Zxsyg5UswF52wl4gmKHZCIN9o6dWXAWQibCCzDFdEbsnHx-m3UNe3jDUCfaLyzVdqBbUla_JQ7G9pwCK5Yc5GURYnrEBTe8AUe6-9Zk7Ut24MVWdBFvN0wk8TWiB8ey0A5OUHsi0N6IIrDPcOBjASmWmHhU6zU0-LispxydJWxFnRCHJwFMO8WYY2cTA5nUIVrWwCQH0ZgFW8TymM0nPEVlxOvUCVbL5LPBIEVrrgP2v9DAQ34aAUqg3PKanvwtizF9laCQul_qcoNgCGRb8_GZ1EVta0Fbn0W5vU0qz-Kq72r_oQ3ozc1bkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇧🇪
باشگاه رئال‌مادرید بزودی قرارداد تیبو کورتوا رو تاپایان‌فصل2028 تمدید خواهدکرد. تمام توافقات بین دوطرف برسر جزئیات قرارداد انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/29793" target="_blank">📅 11:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29792">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇹
کامبک‌پشم‌ریزون افعی‌ها در سری‌آ؛ اینترمیلان درشبی که دوبرصفر از اودینزه عقب بود در نهایت با نتیجه پرگل پنج‌برسه؛ سه امتیاز این مسابقه رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/29792" target="_blank">📅 11:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29791">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXUSWWwYAmRzz3phPiPJP9RYK9Lk8tLt43zXkXLSvhvAKaj8C9vEoGVJtggCfJ6GtuBRUs_6PLdwR0eO4LZFdgmIrFTk14Kb0mbRt4hsOWoUAXv6B0z4W-7qoHtPi0vdLPE0YAYmzYdNXHYmTgG7VrV7mAWZessOqfScnxq_A3xFK6z1XWSweYnNA9YIo3PgoOr_pfzutuf-IU40oJ7Bu2OLHEllFTpgdzLi9L_0MgQOJEl-SGkzZVW4qInFg0nS3LkldnfiV3AHSmRyN5umDhLqdAERZruptuHUdaCJ-_aJ_9XVkkp-8m_P81sH9i5WGJOLooVd39Wz8I2FK4GYgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🔔
از تحلیل و آنالیز تا پیشبینی رایگان
از مسابقه و چالش  تا همفکری و گفتگو در مورد رقابت های ورزشی
✔️
💥
هیجان ولذت پیشبینی در کنار بت بازهای باتجربه و تیم حرفه ای پین بت
✔️
🤝
همین حالا در کانال پین بت عضو شو تا در مسیر موفقیت کنار یک تیم آنالیز حرفه ای به سود و موفقیت برسی
✔️
🤩
آنالیز دقیق رقابت های ورزشی
🤩
چالش های نقدی
🤩
ارائه فرم های  رایگان روزانه
✈️
لینک عضویت
⬇️
r24
🌐
https://t.me/+IxmGEx4ep9A0MzQ6
🌐
https://t.me/+IxmGEx4ep9A0MzQ6
🌐
https://t.me/+IxmGEx4ep9A0MzQ6</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/29791" target="_blank">📅 11:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29790">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPLHQDHcs3plerZfi71pbg8pMFBZyHQ2ZdWIu8MWWt-O14ZSdTayQzFqC9tkf4tG1YpEcxLpD24ySocnsBxYAohwLnrLpJBEChK3QCB3QDZ3psjNJnJPu_Z-bMtWDJM3e9Kl9DgTnkZfZcdDP-i5rBjlOML0yH5o9ll9aDESKT1qSqlfy3-rcoBJd56Ks1nazO2I2nD-sOr-JQMT3HmpK0-V9BYlEoJIOyd7UijQy9qsVztbUYtrajMwf3OPC2gcX1WAIY9vqr7r0YXwX0Qs1t7YYQ0IdU7sDbYtycVykBnYGAHrqLy2dJy1saf3O-ek4QyXYR_tU_d8O6Kj4xtOgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/29790" target="_blank">📅 10:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29789">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3JS1FSa1KPlh0K2wMh1iY2gzteVX7rs6SYZOMOz8PTgCQOvBqDK6mcQ_GxjRZNmKDPvTFS7GjC0nBo-JrTVMl-l8sUmy-k43nu7I_LLvCdBIf8gxCMmuJNF69mED4YXv8XydWNhMochXi-QZgHlC6ucx0Q2-gmGiVMguYNMImxDSeNGA3w0pshcXR122lQhEskhMqP2ss_Ho8zzT_vh78GXcErnaEnh4tc2CyCTJE0vwEe8RxNZmZqDM-ZjUD7E2hMZNFOcJrm2U9LgupPzYqnclXq275FazOj-A9_d9sS1wTZ2RD0kvZyjdpbMBLrSJ1KZmy5cp16gy_hK9TduVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌کادرپزشکی‌تیم استقلال؛ مصدومیت یاسر آسانی جزئی بوده و او مشکلی‌برای همراهی‌آبی‌ها در بازی روز دوشنبه مقابل السد قطر نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/29789" target="_blank">📅 10:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29788">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntASYxpl_OA0YxDmKtKOZ1GhuS58uXzd6lwldS7n8IJGk9UYezNsW2u29dxGqNBW-0228OcLM9FZrYwiLp-34hdTz-8W1IRt2s75zu5EeBBd4G9mIze5pyldjGXdA0FXMmD-qa7hliTQQazk5vUkq0yVfa3KcYM4-Tul5a1r9vF1gB4mtlHW5hPBOKSiA_vY3aW0zbJdfDjFbO_1bv6vuglxSlJg47_n4fE04H8kg1C0xeNNs0oJRH-vO1RdB8dgc6L-wDP4oTEeRj8gnOx-bYILJipl1VzRM7u9h42U4VDdUFYksUzupRc-FFuEJpDt-bat0XjbTfT1XLFwtPWURw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
رودیگو گومز ستاره پرتغالی ولورهمپتون در کنار دوس‌دخترش؛ پارتنرش‌به‌حدی گومز رو دوست داره که تموم بازی‌ها برای حمایت از استادیوم میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/29788" target="_blank">📅 10:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29787">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a34b5427c1.mp4?token=LgqO-nE12SIpyLRE0Py-y7nRHzGuXFXHayaNVRnwX1IX7X2MSUbNZG0NpYf-y-0p7rR2y0D2kZm5y5kWPNc5Cd2JAZyf-L1Ii34o1zYirSUckWMRhQOpOh1QXM9kFhVjpa1qyfLjPsl34aK2P0ETXgxO3-d3FlpRYEZO5MVa_5DTNQaDbqhjNH6yk-VSkJTbY0UqV5i_ZFgX1Z7OvYleJQR5BNQHbxAjDi-AeKkQuzG-zs7AAbp1_qNT9dLIhsjGKsf1lrLdS6SDlr3Rq4ZIHVWsA39YevnxxEeC4MvKdUHB26MULtbaUWZYD0c_5hNpQV2-BJl4BCtRd4ak_8hhgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a34b5427c1.mp4?token=LgqO-nE12SIpyLRE0Py-y7nRHzGuXFXHayaNVRnwX1IX7X2MSUbNZG0NpYf-y-0p7rR2y0D2kZm5y5kWPNc5Cd2JAZyf-L1Ii34o1zYirSUckWMRhQOpOh1QXM9kFhVjpa1qyfLjPsl34aK2P0ETXgxO3-d3FlpRYEZO5MVa_5DTNQaDbqhjNH6yk-VSkJTbY0UqV5i_ZFgX1Z7OvYleJQR5BNQHbxAjDi-AeKkQuzG-zs7AAbp1_qNT9dLIhsjGKsf1lrLdS6SDlr3Rq4ZIHVWsA39YevnxxEeC4MvKdUHB26MULtbaUWZYD0c_5hNpQV2-BJl4BCtRd4ak_8hhgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
هواداران‌التعاون پیش از بازی شب گذشته این تیم مقابل النصر با هو کردن نام دیگو ژوتا ستاره فقید لیورپول حسابی روبن نوس ستاره الهلال و دوست صمیمی زوتا رو اذیت کردند.
‼️
در پایان مسابقه هم که مساوی شد این بار رفتن رو اعصاب کریس رونالدو که CR7 دیگه جوابشون رو…</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/29787" target="_blank">📅 10:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29786">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LB4nTy8pQrI4ENPSP_RHsyGZlrP82oYvTiTT4TvTN_iLNJG7Fo0QWefWEOFRT-0yNrIG4oPcNQKRrTHqkrcW1xtrw9deiEOekOB6uH9-F9NeX4EkpGypSI9odnZXQ61z6BTyHcDBjeCnj8UG50q3L6WfMXU9kjaW-1OPFHr-9KbkVIiw-T65LC_jDj9rM5oq7Wlf-o4tG4u4L7eS6I_zoSOnXDuoEB4990SqAJUP-oEepCt329rsaHJ1kwuHu5beLhzxG22-IWqm_SxIjmL0k24anO60UWFtZUNNdTM2oZlMtZZYv_RfE-ILPWQ49Gqv50CU7aUqHJ7nwho8keVmgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ بشار رسن از طریق‌مدیربرنامه‌خود به‌مدیران تیم پاختاکور گفته ابتدا میخواد تکلیف نهایی‌‌اش با مدیران باشگاه پرسپولیس مشخص شود. درصورتی‌که با این تیم به توافق نرسد قراردادش رو باتیم ازبکی تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/persiana_Soccer/29786" target="_blank">📅 02:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29784">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGxGgYbbtHbUoxqZp4w2LJWk9qstNZvhyPmqMPdvC9FFe-Cx0yEk7XoJz1pm1q_8_KcGD47hZ807eEssYTth7gDzWrT-X7wO3QgPiLTA5dRJ7WFLXTicZWFp3LYzrwDWpZOfpWcArA8XgJ85WJiqjpLytVRm1JZL2rv7UIuU3gwRKBLXj7yjBET6k0zxRntUyi4epfAaaSjD8ZAaQLB79MXJhwcaLehUb9l0tClcHjf3cjoLUTBjOdUCWriJYBzKOlyKFNjNaK1QTF6YimxerNGLgHBDMiOhDactBfUPzvV8sCfEJbps2Xd7ugY326pu0voaQ8Fh5VMVY1ztVqzXyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
#فکت؛ السد قطر تیم 78 میلیون یورویی آسیا امشب بعداز 22 مسابقه نتونست‌گلی به حریف بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/persiana_Soccer/29784" target="_blank">📅 01:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29783">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFXkCo8rF-56tR1HGJDK-OjliLgCrwLuPXaQUbIBho_GATbPqFQX1FpH4BBIGiVrOmKRMxT8u7-5cnuyWZbmgK0ofdkmMpKUKTNVDELHJAlOYJKdzdlTj62gB0QWyMjNscCNlDtOdmz6g2ofuOVxb8GzJn5O71FUwiyNB3mQ-cuRaRn8LS1oXKNCVqJs3H3xyUDLkZ6WIHcr5g7GQIzyWs9A93zCyyixyqpVi-1uhwIvWBnBBxOvVfDnqGJiwsqE4mZZ5CGCCgOQf_TR_ZgkMorpctDVzFm1CESlB2thRT15z3xwPFo_I5IPPcyq63L_xUNc7dsbJDMypXdqhMDWtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌پرشیانا؛ مهدی تارتار سرمربی پرسپولیس‌امروز درحاشیه‌دیدار دوستانه سرخپوشان جلسه‌ای‌کوتاه‌بااوستون اورونوف برگزار کرده و به او گفته که درادامه فصل‌بیشتر از قبل به‌او بازی خواهد داد و مشکلی با ماندن او در تیم پرسپولیس ندارد.
🔴
گفتنی‌ است‌ که علاقه…</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/29783" target="_blank">📅 01:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29782">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPmHYryae5YPJAjhAkfc9bXrffQB2-e3dDZwVW1go-suGRVCRElMsSjXgH_F41qH2mrGSDnxqaU5_Mwo6qX6CIpHSERZlMt9aWU3Hxowu4kMitKQNmQq9j252LlsLCDtFKxQIFq14SubeuSp_URKnFdy5t6BWCUp9WrTDuW4UIj6njhYB9BwBy9ZxnOObDbprq0yvO9Z7d8ANwQpdn5bVPPRXiQrg5z4owm66Snhzhk69E6E-efAiZFPI8U079oqS5lg2nl2iZcpcNYP1VKDMWbVzybJVUNRdoFJdCjBCstxk0LnSmtdm3x4Fa6cDvLMqS-kjw18jfvjQkqsBTSp3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌امروز
؛ تقابل‌لیورپولیها با شاگردان دی‌زربی در کارابائوکاپ و مصاف رئال مادرید با الچه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/29782" target="_blank">📅 01:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29781">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGtzqSgNRucyCyJCTGgYyBmm5GNRAb46cU6oW7t0updO-6V_PkmKp7AxEWW4TM_RH-IYenNqHLaYvgCaQOdYxSGuA97qYqalMF3gOpVwyR0Z5rmOCriQnJvCy4y8d9AmvKKuTJLltKuTjWTmtzgrW84tWIol2htt9_qluG32G1qKXeEgKktfeVgm0JtA96J7PW3Do-6_tbBHIZCMr29ZUA-5j-0rXGXHYRnG4IsnwNjCpMKUuV2t5a3rI6u6eWdJI9D4Top0MtefVU7YHSvTfTXWfaIQmM3bvxy1-vMgWioFp2mO2UtZ2TOPULqNAYSBEs9fIKuc_TwuJT9SPzuGzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
ازبرد شاهکار استقلال برابر قهرمان قطر تاصدرنشینی‌یاران دیبالا در سری‌آ ایتالیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/29781" target="_blank">📅 01:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29779">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCD8Gja4WEKuJqOfoU0eZ1zit-mzIqJgBkaIwsCERTKv2-HcTHj433xAI7XueS9sh4c-FyIrgxgP4m4dcxcIn6aiP3QLazKWujvd1J3BJxaQBhhlls9Hkk6MA_7NeS0GezYwpKIBqtxh0xK7U1oDVKyY0bRAzhrkzE4531vvtRSkdoJVlNgR07URThBGftPIQQ3qDyd7Ao-ComfZLcKd0v1E5NkR7M9hn23T25zcPff-x9eGKUI6GMWtaxgDKlq6OigxPcGZ3KH1yjujPAavDv3_HyLwjkZKklIjxRPprrbKdRvwNBRQ7U6ywQrIjtsXdMS16ANJGwmFALseS8H5oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛مدیربرنامه‌های علی قلی زاده که رفاقت نزدیکی که با محسن خلیلی داره با توجه به چراغ سبز علی قلی زاده به پیوستن به پرسپولیس قصد داره این بازیکن رو در نیم فصل به پرسپولیس بیاره و صحبت‌های اولیه شروع شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/persiana_Soccer/29779" target="_blank">📅 01:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29778">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aw9VGvKYg8-rjN78X5z77ufrySCF5XHH8yjfS3saGqrGEiOkQm1p_Dk5srpbTU7RD7h1_PigI0hWM6fbYTV4pNlwSmh7yvPjSuXJTH8qFiHnsGvB9YXyxyUckEX8CRuXOrRS8vfOmRp_sXVZtJ5dSsc3lhspzQevPoz7ikyg4uW4V__IaeTznki58Hf90UwirZ7Lw1P2ZrZmKqwVl49h3qaNDgFvPYL-cec--YvKi3GEx8mCfKYjVY-E1j67Ig9hNGEqp9YScfYZqUnMzuZKhvaVXvqsL5m7tPBoNoddcqSSMHVjTx0DjWOnayazstlSCXWNt92TGlscAfkZ4Q8d3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ بشار رسن از طریق‌مدیربرنامه‌خود به‌مدیران تیم پاختاکور گفته ابتدا میخواد تکلیف نهایی‌‌اش با مدیران باشگاه پرسپولیس مشخص شود. درصورتی‌که با این تیم به توافق نرسد قراردادش رو باتیم ازبکی تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/persiana_Soccer/29778" target="_blank">📅 01:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29777">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GRm7k_Ja4zp-GrxcT932aUnNIv6a9tadAVktqiWw8zGHLSRPCm1qU3nqiRbkJDnZK7-C1XQ_91uvVnkwTVwWfUWOvMx948MPvf3CO1HgXoisx5gAisC3d2Cb9LxrkUIILviPS3mnVqT-fJQaasFhyoF3EljkzgKPPisQ6gCnAzdGCuiCKZOMnrqNWNgQnIWj_grACLj6_Srb1iRM3C0y8SYuSmN4dUK5f0d68b8gSHqZsQYuyArqWVPr8ShO2YmGtaTPTB91UqpuzX4cICAxaOqIyi2HUV5Te73letxW6eSk7avrZ4-NRC2Jc1Q9hONrWDJ8EViwUF9SWZpq2vF-yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
کامبک‌پشم‌ریزون افعی‌ها در سری‌آ؛ اینترمیلان درشبی که دوبرصفر از اودینزه عقب بود در نهایت با نتیجه پرگل پنج‌برسه؛ سه امتیاز این مسابقه رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/persiana_Soccer/29777" target="_blank">📅 00:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29776">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGt6zNjh9q19f7XI1_oJbBRGiQ3r6OJSoT4pgIo8kQjAOMDWeVKWcnbQOoKB7ShvGrpXTiAiPgN_7bzjpp5AyoRfy9OCfQYccg4oeWeHi2KCKCxsaySr-v8_a_-My2d_MIPNVHjkTQGtzyAUFIpF6645pOwwceTxAcHhel1nvi36qpIz8Dcag5tHdPP_96uRO8NTExMqw2Z5_ilVzk69ATZ42BTxhDfrH_4-806JA7vt6lnC6_KoAIF0IWUsBXMlHSGOVXi58J8z7wCqE41ZVJ_63t6UTsheXA76HucEL0AJFq9B3KRwEwWVj4JOhwellD-6UkovnjcIjc5myXzGvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌استقلال‌ میخواد درروزهای آتی با پرداخت 800هزاردلار به‌فابیو کاریله پرونده او ببندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/persiana_Soccer/29776" target="_blank">📅 00:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29775">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgygiC0XvXeRpo-gEO63e3qA9d1ihGZeXbaMI2Rw9-98QjFHUdqPeyhhzAxzs-G5gcyNgxEdqviTi2g7QqRhd_brJheZZtAgUWpBy84tvn59MiVkaa2wiSVN9Meq7_pg330sDKksURU6OrEfLQ4Jmx_XpMMzqUenBw_4aMzkOG8PZnxdG01o9bQuJobLW0F88Kg0BQcw8UUqhRC2fEy-lioyTf9h-jBxpuYOhh6BJRGXrOcHVvsc06sraVPhDiha7wYYvEP7BFW4cbG2F3pb6XX6ac1bz3OZHKMplEgV6CIByraRayUg_HRisnIwgoJKRI2gZ9ReqJCz4LMR2AKzjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درهفته‌چهارم سری‌آ؛ آاس رم گاسپرینی با دو گل سه‌امتیازارزشمند رو از تورینوگرفت‌و با چهار پیروزی پیاپی درصدرجدول ایستاد. شاگردان سسک فابرگاس هم دو بر یک ازسد پارماگذشت و با10 امتیاز در رتبه دوم جدول رده بندی سری‌آ ایتالیا قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/29775" target="_blank">📅 00:13 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29774">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ti7834UbECJMTCCwM61PdRkG_e1sj7MCqFIJmSAI0dmsu31Qc57l9_y-ob_U_ElaWYTcaanNB2OJ8Bp_ChGH-ZBHf-5-tQPp2iSbX-Rq2DUg2MBiZpdZycKie3eLhTlNvixYXaMi-eJZEZOgk92ft9Td0vXjPBQCreOz4tsodv6OSpgZSmVn3fpBs6zOUVNGxq5xKcux24CAZJtTOJvPqti57GKu6WvLKf6a5E-fBauzMqVVhwknKVcucjszZRC7Z2QQBO2aiaKgtpTzOSVfViUJ_QuSuF7vo-pGU-RTtnQif9AF63ACqYlxN1nbFy1FY5htud-gnUxvWuwyyA6doQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ نخبگان|دشت سه امتیازی ارزشمند شاگردان بختیاری‌زاده درگام‌اول لیگ نخبگان در شب درخشش‌خیره‌کننده‌یاسر آسانی؛ السد قطر بعد از پنج مسابقه بالاخره طعم شکست رو چشید و تحقیر شد.
🔵
استقلال ایران
3️⃣
-
0️⃣
السد قطر
⚫️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/29774" target="_blank">📅 00:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29773">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lW3Oe03G21Y0VRFYLGIGtBNc4-KaR42s5Ut6KjWhnAuImjiP3FaDuQWwgW-517AXIDGv_KJnj2VlnA1tJO55kfcYL_lUo75dFWwdbEp-_6Yr0Da2VuY5Wn5FoghKDHtVDpoD331HgCwGO6o7rn0I-lEXtKC748MT7ljhElygEhQOS_9GcE4xKowvalkJyIEeSr-Vvspry5vwHtzLT5sx7vQnKBrgA1iB1H01PUnKccDcj7i54HU2t-f8dUtbm8Y7oy1JDonELqOMg3ktzoZJ6lhsvVjPPYBJXFivyARk8RkqjQ_ThFlvjnlnWUdsbP5phIVwAbMEtKNOvAdATH-b-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ نخبگان|دشت سه امتیازی ارزشمند شاگردان بختیاری‌زاده درگام‌اول لیگ نخبگان در شب درخشش‌خیره‌کننده‌یاسر آسانی؛ السد قطر بعد از پنج مسابقه بالاخره طعم شکست رو چشید و تحقیر شد.
🔵
استقلال ایران
3️⃣
-
0️⃣
السد قطر
⚫️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/29773" target="_blank">📅 23:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29772">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DP0BFgrqofL9qGuytSn4d0jjqfzmR9e-699toj1_KxQ9312GfZ7gnM1rxuYSHeYTVTgioIkhTan1nvF11ncOnxOKArH8j1BYz3JmZ-_njInlHA-bRnOdXCeITHzO1ja5KTR3tDsccO-nKL2qmkPqcT2KpRvr8wycSpTOchip5m47d4lrp44se1tzJDojeVmaxgULDM6OeC_u6wkVfW8f3YbGmhSdC46erxehwsnLeVdHbe24GNnR0T7E5hBIL9BAfVrVvTPe8fdoioJh0P0Vyz_OW0_1yGo_S3e27wBchkhXGWiIELyYeDCmqx0h5PFOZCLRUq6EM5Dp5Gh9WTNrJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ نخبگان|دشت سه امتیازی ارزشمند شاگردان بختیاری‌زاده درگام‌اول لیگ نخبگان در شب درخشش‌خیره‌کننده‌یاسر آسانی؛ السد قطر بعد از پنج مسابقه بالاخره طعم شکست رو چشید و تحقیر شد.
🔵
استقلال ایران
3️⃣
-
0️⃣
السد قطر
⚫️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/29772" target="_blank">📅 23:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29771">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXZXeQ_q5z6klJWf8NSDJs580jMYRkJ5y1QuMsua6mr8Vj0yFdpQnJBJEGKzYh6sp3tiCJUzKulc9_FaSbHFTKpuF2xb8666IzBY4P4N9KgHPSMI6-W9GxgNR8kCA4hKwo484DHr-_nmaLdxzxU1ee-zI6jB9qRMh38Xq6ewBqw7usxMuhVp69ZBTBP_iKPW72Dz9mZ0FRh3wZf8qcLdqy79RR0kLyM6x4Qz64xELZiER4NwOz5onLgvCDyFq7Rssw9-6ejXmdu_hr3HFGe2Ok96ARV5b5lqX6wn1w0K1qecP_IZqjbmSAgKJKpgf790AMDc1fK9HBFKH8GKHwc6CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گزارشگر بازی استقلال
🆚
السد: بله داور آفساید اعلام کرد، مشخص بود توپ به دست بازیکن خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/29771" target="_blank">📅 23:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29770">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e46b6c177.mp4?token=VPV_BDGy7EoqxUvq653RGN6GHeVXmc2sUtr0Mri5KS2jmVKfO2bFiYAY3xO2YkRVHDj9HPnn_jffbediUL7ErB2de2Sn84qEGW-VWVLjA947JpvdpyJqqm8qlYHUTyDsf3Gk3byau8WBtW88hzSgmyhNNp8wqHmQzet6oDSS499shaZggz2fxV_WMGOXk1Rv7rUqKA4LUkAjf5uLeOZwJ_-6emav44-mXpmd00uOlsix2xlpgI_-pm8BmoH06xoql0lJFE_2WG0T2M6uCosaDQpeBXtoE_XYp8c0kN-oGn4VWFji9R8iNFgQzmckubXo8j0SzqASQEKKFfWMS5sWPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e46b6c177.mp4?token=VPV_BDGy7EoqxUvq653RGN6GHeVXmc2sUtr0Mri5KS2jmVKfO2bFiYAY3xO2YkRVHDj9HPnn_jffbediUL7ErB2de2Sn84qEGW-VWVLjA947JpvdpyJqqm8qlYHUTyDsf3Gk3byau8WBtW88hzSgmyhNNp8wqHmQzet6oDSS499shaZggz2fxV_WMGOXk1Rv7rUqKA4LUkAjf5uLeOZwJ_-6emav44-mXpmd00uOlsix2xlpgI_-pm8BmoH06xoql0lJFE_2WG0T2M6uCosaDQpeBXtoE_XYp8c0kN-oGn4VWFji9R8iNFgQzmckubXo8j0SzqASQEKKFfWMS5sWPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گزارشگر بازی استقلال
🆚
السد: بله داور آفساید اعلام کرد، مشخص بود توپ به دست بازیکن خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/29770" target="_blank">📅 23:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29769">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOnaOU4BnDzRF4k7Z5kc2RPIvS4xiDTZWpqorgxVejMI_EL7Q39U-7Q9zqHGOkI-hrcEpeX_vtAZRujXPh0zvz6IiWPhHl5CI3J32C4tbHXqbS0G3fmD0cH8YlZtu3xmtB2uR8pxWehJ7Vh0fW2CzwYCqMfSeATkMTcAWTG1-jMNH3lDGnFShGNS-nVsqPGOuBDX8R2p1_QzDhXx0w8wQOMqpkmQ89auje6U8zoktI5LazPDibYKLyG7ej50JwRqV2AcWEzo9XBaUa7Z92aOA77E_L35FP7IOGLswi2qVKWRDy8GTPigVS3upBfemf74Xij8y-zFvI_cRJ3NAElZdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
اظهارات‌ جالب لامین یامال ستاره بارسلونا درباره توپ طلا: "فکر می‌کنم امسال من لیاقتش رو داشته باشم، بخاطر چیزهایی که بردم. چون از نظر من، من و امباپه دو تا از بهترین‌های دنیا هستیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/29769" target="_blank">📅 23:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29768">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a29f0c126c.mp4?token=tswycls5aKXK2TJKe_hzryFvL1ZcprVMRRhjIgDK_enS75jqfWjpcl2TpjdqUg1lF06xJeKKp9Hr2dN5Z8B9tEkBlRRVxMjXNj_b8H2kzukmlLvnRyRT9UUyprMt0g8_CcnB-_dldZA8B06XnGmOh2yF7l2prRI_riEk-364B3pS6eY2G59kJ67tUHPfdpyVLyNWzuOj6zJg8cBW1-n08bbNUCJ3pQKweUgGWMjlyi5o_DdzrZP-IGcGdttPzBk3Gpn_LweounuImrf1leYMrwGOnoUTXYuitSJ6-7iDZoUvQ1B05YMP3Yhsd0NA66OW6_sm_MaWF1nsKlbbSSPeUIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a29f0c126c.mp4?token=tswycls5aKXK2TJKe_hzryFvL1ZcprVMRRhjIgDK_enS75jqfWjpcl2TpjdqUg1lF06xJeKKp9Hr2dN5Z8B9tEkBlRRVxMjXNj_b8H2kzukmlLvnRyRT9UUyprMt0g8_CcnB-_dldZA8B06XnGmOh2yF7l2prRI_riEk-364B3pS6eY2G59kJ67tUHPfdpyVLyNWzuOj6zJg8cBW1-n08bbNUCJ3pQKweUgGWMjlyi5o_DdzrZP-IGcGdttPzBk3Gpn_LweounuImrf1leYMrwGOnoUTXYuitSJ6-7iDZoUvQ1B05YMP3Yhsd0NA66OW6_sm_MaWF1nsKlbbSSPeUIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
روی‌سماجت‌کاپیتان‌‌آبی‌ها؛گل‌دوم استقلال به السد توسط سحر خیزان روی پاس آسانی دقیقه 47
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/29768" target="_blank">📅 23:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29767">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eb15dcf87.mp4?token=HmTzrlGhBQYcv0m3BuZ7KgdZ-D87DPQiuukzrN7GigtSJxjYhNwKuBOlc6T0Bxpx7WDp7WHVty17uS5zvutnwwjXFaUFdaSCaethy0zlK4QwbingUSYR3GyjBh-ILpRzIkcKF0nwaWCz4ljZP93fvgboe9utvoCRFP_re4jqNPWpUVbxt-5ED_Ks33zcWJhB11tC1pekk3PKtWplk84q_4JxvwaiwOqx5TpuoOjX21flEKi3WsIM_BO43aBIeei7lk8vmsO81ia6jVTJTzfsCLB20eHqVsAPMkHFAov94Vt0mWLEictr_GiZeynfn8fZ0ZAln7V_Zn-bAuSvMJCVUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eb15dcf87.mp4?token=HmTzrlGhBQYcv0m3BuZ7KgdZ-D87DPQiuukzrN7GigtSJxjYhNwKuBOlc6T0Bxpx7WDp7WHVty17uS5zvutnwwjXFaUFdaSCaethy0zlK4QwbingUSYR3GyjBh-ILpRzIkcKF0nwaWCz4ljZP93fvgboe9utvoCRFP_re4jqNPWpUVbxt-5ED_Ks33zcWJhB11tC1pekk3PKtWplk84q_4JxvwaiwOqx5TpuoOjX21flEKi3WsIM_BO43aBIeei7lk8vmsO81ia6jVTJTzfsCLB20eHqVsAPMkHFAov94Vt0mWLEictr_GiZeynfn8fZ0ZAln7V_Zn-bAuSvMJCVUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
شلیک‌محکم‌ستاره‌آلبانیایی؛ گل اول استقلال به السد قطر توسط یاسر آسانی در دقیقه 9 مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/29767" target="_blank">📅 22:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29766">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0fauEESv5Xl6yIW_ngWkismbmAEwJIIpUONgd80OuCCMGq-ANO8qcrpNwwexovS2AYUalkjJRJ8L-pC6e5yq6AkYr6WzBmfg33bxX075adp1SwQTzL89jymLGf8PFs4cWwj1STGVhKgcZw9OHFDXAV7kT_V8CXkk-dlg4uibnTFHFcrv3h-CEzN6gVHBhfwvva_eNBv2X3j0rFAy7rVtImMfXHxaVnkzS72WA-a6WSwxwQ_tCufVpxwmgxjqflknl-eKGkkKRRzYvx6L9YLK3osdpTQPlbFxjZecAVRkzDWKGE_ZHYgg_3FxIKOjLtrsGYDDiDkyRU3r6nmynHWnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
شلیک‌محکم‌ستاره‌آلبانیایی؛ گل اول استقلال به السد قطر توسط یاسر آسانی در دقیقه 9 مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/29766" target="_blank">📅 22:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29765">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FmQm9Fwo2dEAPfxNivgxcgFfVfwjhp6cEXabAuOTs6DZHdDgF4MY6ftZkMv2rw482CblGzEeEKpM4AtbI9vf_164wj9kEj_D4cE2ynk09lrJN5-1HkL70AP5ECrHpnqQ64vdeLemcdnuXRCuM2QyzSDrstihXQRn-91RiIclJ9C71KGgsR9y5pkbvb2lC_OcpDHoYxSxB64DaAu-FX9ixXIEyRaHPGY1bzpVPUrHXXvFACpra3Eia8sGfU5V6_eiIrki5e3a_Mv5CJ4lr4GzBzmIw0wLkkYFrppahNi8itRidUy1RY42xgtAVu-RWV9hy5ID93qokgvXQquzTYbM4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در هفته سوم سری‌آ؛ رمِ گاسپرینی در دقیقه 90 کامبک زد و دو بر یک آتالانتا رو شکست داد. لاکرونیا هم بادرخشش‌خیره‌کننده اوبامیانگ سه‌بردو ویارئال رو برد. اوبا 37 ساله فوق العاده داره کار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/29765" target="_blank">📅 22:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29764">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea8d6d38b2.mp4?token=tsk9jrOKj6gsiwlSEVsOPlYX8KyqGBUjeGjDnkEtSMgbSfXp5U946mmWmLErE_8ObqW_Ey6bvLHviVLE7obvh7h-XJezCxt8aeVnDtnXKgydAcwhpyz5I1enuNcMxIbby4cSpNbZrbUDxVXgrFZf3mPOcRSx7sgNpk4nGEaUTYykb-no75_uLUHNKhTdFzwzy8PDy0OACl4qC5p387weg4r18qohqXCpkddeIvBJEaw2mrlM_CzqLAIISkth-rF_0aJ8wgxmc8enACRaaSh3V1kKH9io3l_WCtmknnGUqLrLyQUrRTwF4eRYC7nICa-4NM_knpZ_RU0LQ_1WxIf34w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea8d6d38b2.mp4?token=tsk9jrOKj6gsiwlSEVsOPlYX8KyqGBUjeGjDnkEtSMgbSfXp5U946mmWmLErE_8ObqW_Ey6bvLHviVLE7obvh7h-XJezCxt8aeVnDtnXKgydAcwhpyz5I1enuNcMxIbby4cSpNbZrbUDxVXgrFZf3mPOcRSx7sgNpk4nGEaUTYykb-no75_uLUHNKhTdFzwzy8PDy0OACl4qC5p387weg4r18qohqXCpkddeIvBJEaw2mrlM_CzqLAIISkth-rF_0aJ8wgxmc8enACRaaSh3V1kKH9io3l_WCtmknnGUqLrLyQUrRTwF4eRYC7nICa-4NM_knpZ_RU0LQ_1WxIf34w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
شماتیک‌ترکیب‌تیم استقلال برای دیدار امشب مقابل تیم السد قطر در هفته اول لیگ نخبگان اسیا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29764" target="_blank">📅 21:57 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29763">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUykeNKPVY-NM_ICHAJ9a-iYNr5h6NSpAyt3hHGCIRhnlrIlyM4IxnGIJlDKuDRqv4tHDZ-KvZNRavO0ZCvPXC08DJ4OgBpM-E70Aga5WEFxCCT07WTIaNW-sd9kWVOpj7DV0EUyw0ZZqonVI2z5ooLUJtgWJROUs1OlQe6Gf9t1gIJwnhUuXz8kr2eAcXI9Nek2SXt28qQQDRzHzzqtWLzIYTxrSjkd5guXcY2vbm0Amhfw-JFe27WPSRcHU5Cx93kEaLbV8Bu3ZOMhokesaV5hIpJpPYzRTkfrfap5FR1fTn3uKeuCtc8rA7ADuaTX5EWdcBqug7XG4lLOSHXb3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
گل اول شباب الاهلی به تراکتور توسط یوری سزار در دقیقه 22 روی پاس زیرکانه سردار آزمون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/29763" target="_blank">📅 21:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29762">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d18cb084.mp4?token=sJrexbOrBSoV1nZ1QmftBz5fOkxgCQGJpEIij3Jh8nknJ9b7EMt-gEzTZU6gt-j6lasojjupGDAFBxqKBqEABpnp3aD4LNANhmMc1NvdBP35BqGB1mKCdGlBwgvEQPHRTfPt6ULp4iXWYN6KjLOlhW103M3aZV7CRBpYU_CUqbIiuHna3avUtdGrE7cAGDrDMkj0u0hkqDEhRQ7VIbR_l9Bg_s8kiMcyk3cAFCXFVb0YPp_Dg7CKcSiN_uqBCalYAkiBzSkMZLC-7h7gGIhskJC7qO2tn4vV-aFgComuaoknRBulTulBe87hqgn3eSUn3ARlSJBymq55JwOujAvjhVXKvaDCrP7wDFzs-jxjdNBNbyWEL2LSttdWHHR4by8_BMI4Oi9r3xmqmMBCqXEBmxvsvG0spT_LoAoSKFciRnfgqtgk_tBV1rw4vqcOxtzYSZFOsZJc4a_4nV4uQHedHC2ayR_2TaQiLUkvXIPA6vxXGg2KCMi-FBW2BTejAV6d9kmSWzrAdFgWpXPH49jHTYvzqswcQp21__8Ruv-wLVnYlDPuGTAy2bQlH6Y6b2i-P5YkaCphLAR4tgWVShpX0jL5xXvWBDotAesEPMq312Ol-1laWECY8GK8vE_NyH_KUF29XCq5_hpXOTHwP0y7yyCDcTZzdwsK1eSbtsYv4Wk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d18cb084.mp4?token=sJrexbOrBSoV1nZ1QmftBz5fOkxgCQGJpEIij3Jh8nknJ9b7EMt-gEzTZU6gt-j6lasojjupGDAFBxqKBqEABpnp3aD4LNANhmMc1NvdBP35BqGB1mKCdGlBwgvEQPHRTfPt6ULp4iXWYN6KjLOlhW103M3aZV7CRBpYU_CUqbIiuHna3avUtdGrE7cAGDrDMkj0u0hkqDEhRQ7VIbR_l9Bg_s8kiMcyk3cAFCXFVb0YPp_Dg7CKcSiN_uqBCalYAkiBzSkMZLC-7h7gGIhskJC7qO2tn4vV-aFgComuaoknRBulTulBe87hqgn3eSUn3ARlSJBymq55JwOujAvjhVXKvaDCrP7wDFzs-jxjdNBNbyWEL2LSttdWHHR4by8_BMI4Oi9r3xmqmMBCqXEBmxvsvG0spT_LoAoSKFciRnfgqtgk_tBV1rw4vqcOxtzYSZFOsZJc4a_4nV4uQHedHC2ayR_2TaQiLUkvXIPA6vxXGg2KCMi-FBW2BTejAV6d9kmSWzrAdFgWpXPH49jHTYvzqswcQp21__8Ruv-wLVnYlDPuGTAy2bQlH6Y6b2i-P5YkaCphLAR4tgWVShpX0jL5xXvWBDotAesEPMq312Ol-1laWECY8GK8vE_NyH_KUF29XCq5_hpXOTHwP0y7yyCDcTZzdwsK1eSbtsYv4Wk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
باشگاه دورتموند با انتشار سوپرگل دیدنی و فوق العاده فیلکس کلو اِنمکا در بازی این هفته با پادربورن مدعی شده باید جایزه پوشکاش 2026 به او برسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29762" target="_blank">📅 21:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29761">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGTjkJt3K3tDj8v3zKKlxyxw6bUS9I2S5TY3RlTT0moH-rBtG_UPukZ_YKbimmGD7SQzWRfuk8kmnfk2GfUD_NYxBGQt5tTo9BO-jGQuEUZU2vrpFo1KgvZwsyYxWV_-wBniS6AvqmQ-aVe-lp5CR6RrAXV0yR7ggmJqQIIcaurO98jw3Gf0Sp8bdy7toCxqhssGKvvaCosZGnMvvMKLVLVQRdTWI_5-XDE-FqubgMWB3T8u1uDT9_L5lBTLTrPGpZ8nFFaULg8HUdxWL47VVp_ps_Lo0r4v8YHE0vEXXdDPiOx6ZiA1sS_XJx7aBwPqY_jyhVrhytAqatDwKp7xqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ‌نخبگان؛ ترکیب استقلال برای دیدار امشب مقابل السد؛ ساعت 21:45 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/29761" target="_blank">📅 20:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29760">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DThO_jjblIcLqFpGUnuTmU7P-6LdIGpTq_VQd0poPDugxck6AmdEvDbtuglUw4UUZTYJgw-GCM7iaZJUQGOcUHToVnY97285DAkpT3c9cuxP_3I2wSLvGYOH9WHP1lmw5WG4imudiH0kelL6BNGElyGnkzO8Dp2vWTr19w5y_Otr4uEBnLu2zipM6yzewB5Hdbw4ujIK90NUI7OMVbxg14jdI5VBr6D-ATCbWfsmZe7BwfSP_oScKaYfrL7qT7DOsiicZ_8fTIa2aVIDA5vNMfrSCeDTtZ-AMoLqKn62-6XMLecpx03wNyuDY7ZfmXR9rRvcZJzcrfWUNkRgN7OX0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ‌نخبگان؛ ترکیب استقلال برای دیدار امشب مقابل السد؛ ساعت 21:45 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/29760" target="_blank">📅 20:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29759">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Um3L011qlOvNmGj63uwkhw9LeYjuR6-6Ps1AsVZ4dRaDvGa3S3IDpwcdO30pqjCfkUF_G9kB6hB9CdjEYL-pQYh-qzLg5hSSGCWC9eJL_QvnNfdSTfo_XzbVj01IWfqzcrWQeHnyOHmQF7zHoeVhFXCzK_beguj08nAGVP5jP_6_DhTH4fm-eN-42VFJ2p4UWV83zVshQEIjQNzqz6oBlmCyzzpUHQUvhnZBtz2SjX3kmJe2W-XGUcyQKgWx-KQA7EH-bEhQyUmvKh1SErODdmLp493lkr4zAoq2_zHKd2hRlii7h7pa0HLakByhrJxIafDMnw6PMNKsfOgoRfxILg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
🔵
شماتیک ترکیب احتمالی استقلال برای دیدار امروز مقابل السد قطر؛ ساعت 21:45 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/29759" target="_blank">📅 20:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29758">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2LOXRxu6Za06iUUD3nwh46DubdwTRE9eBAs0QMvrqb8fWXMDuzNNDiljgQswYHGCF7wDN5dr4KAahMjoPeiK_eZI8ph47BHahMiF0K8V8Q6nq8u-7bK5R6HTrrC7tG6LVjhHaLrqs6Xd928OOVD--5aYwY_PMFZTb20paBxo-6pCdCgLovTssrJs1wUOGlpsDTbPcLXMHXF2v_wJx0P-mEyZFwohFS-Mm6Z7T0j0GwMTQS-E8ENUMkxPZyXfa33VQa1J_RftZwaPTomls7I0kxo6YLHtWKiFTkK0UVJjrdJVXlZgmTLjKZ8QicNXbha2w_EVmq6pAuyqPjawvLA4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سوال خبرنگار از بلینگهام:
هنوز هم گواهینامه رانندگی نداری‌نه؟ جود بلینگهام: نه ولی به کسی نگی ها. من هنوز راننده‌شخصی میگیرم، الانم کسیو ندارم باید ببینم همیلتون بعد فرمول یک چیکارست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/29758" target="_blank">📅 20:26 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29757">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2de12818fd.mp4?token=PjDI6NhP-k1-JGz9sRZ9no5cJIIBDrb1qojuDfRz6aFPrP7O8eYWxNbSWUqTDdYWNiEmYmEqQCsgtuEEkWOEHoY1ulFBp9Xw3M7nnbNohx-bFxoKHEFvsU4xqU4oenUC5GD6mBpVB2ns5_NBqjLeEfoR8JtABbxD5EU2yzWSUDh2pDQKPduaIfyhYZ389i25hz6yVAX8hhOSb73bmuPmYmDdCA_1KEiUAPdUg-y5XGoJUjEcxic2pd5MntlwQlwNhuNHeOQcQhFm92JpNwLgoiW-YDXe1lXqS0gAAmP7x6gyw0IRSo76smeLCGuV-0hdyf2w-P2dyClzQDWJkL6Ovg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2de12818fd.mp4?token=PjDI6NhP-k1-JGz9sRZ9no5cJIIBDrb1qojuDfRz6aFPrP7O8eYWxNbSWUqTDdYWNiEmYmEqQCsgtuEEkWOEHoY1ulFBp9Xw3M7nnbNohx-bFxoKHEFvsU4xqU4oenUC5GD6mBpVB2ns5_NBqjLeEfoR8JtABbxD5EU2yzWSUDh2pDQKPduaIfyhYZ389i25hz6yVAX8hhOSb73bmuPmYmDdCA_1KEiUAPdUg-y5XGoJUjEcxic2pd5MntlwQlwNhuNHeOQcQhFm92JpNwLgoiW-YDXe1lXqS0gAAmP7x6gyw0IRSo76smeLCGuV-0hdyf2w-P2dyClzQDWJkL6Ovg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ضربه‌سرمحکم‌سردار آزمون‌در دقیقه 7 مسابقه که وارد دروازه تراکتورشد اماآفساید بدرستی گرفته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/29757" target="_blank">📅 19:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29756">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90deefc883.mp4?token=QS7cn7aiF-aShvBO9T5dES9gUHLaSfWqNRQiY9oninxKKZpUj437ZlOB-Vo2IfqhGGYSbHsy26xMczo7ZIO5EWTisjsq-KvY2bA9CtHKA_-Qrdj5UuFaRNXRVsVfdUEvs2srt6GGoMGEyUkw5Vn-51Ub_PsTd2Gf-6-PbkebJ9sIn8tEK3Lg6qR-MqnggneplRgwDipi0Uf8siQndngLtSaYeklxsKPYzO1iZI4NBOSQHG-Ont9MyNrQs69lnKutqqNIK_DoRJlFr4yQdqxZHkiy9G0Qp797VdhNGO6275EOOFh0cGi7fhjq_vpJrHc_11PsKOAHY-A-M0fD6OChrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90deefc883.mp4?token=QS7cn7aiF-aShvBO9T5dES9gUHLaSfWqNRQiY9oninxKKZpUj437ZlOB-Vo2IfqhGGYSbHsy26xMczo7ZIO5EWTisjsq-KvY2bA9CtHKA_-Qrdj5UuFaRNXRVsVfdUEvs2srt6GGoMGEyUkw5Vn-51Ub_PsTd2Gf-6-PbkebJ9sIn8tEK3Lg6qR-MqnggneplRgwDipi0Uf8siQndngLtSaYeklxsKPYzO1iZI4NBOSQHG-Ont9MyNrQs69lnKutqqNIK_DoRJlFr4yQdqxZHkiy9G0Qp797VdhNGO6275EOOFh0cGi7fhjq_vpJrHc_11PsKOAHY-A-M0fD6OChrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
ایشون خبرنگار باشگاه شباب‌الاهلی هستن که پیش از مسابقه امروز با سردار مصاحبه کرده و بهش گفته مطمئن هستم امشب دو گل به تراکتور میزنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/29756" target="_blank">📅 19:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29755">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNOWpbzjl7eGVwPKInRUQqXzu1CA5MFaYGZfpAvji9LnzYO0EgyU_eUx7cMZtZKVLJwrI_u3Wzp1TwelUuxLZEJgmloDnymh0xpUql0iuxfwJZO_qk-lmfh8GFzZKmaGHciwUFxidq7NYfi7otc7PNCbiOatmLQPLqz6v0nOKahCD94MXe1X0bmNk8IEWmL1i29cENSh8NXZd94Nrwf_Qc58nBeEvr2ak5-xxgSO3IiqiTOS6q8xfH2xkFEACYqmVEzgMM0JvcwD6AQn7eLrvxbZjzlY95UdBI6qOhqrWQix5qXtqpKuj1Euc0Awb1x4rFNS4065AyFWjX8Wjl2TTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#فکت؛ اگر یک ستاره هر فصل به مدت 19 سال متوالی 50 گل بثمر برساند درمجموع 950 گل خواهدداشت. ولی‌کریستیانو رونالدو: 979 گل زده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/29755" target="_blank">📅 19:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29754">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADAis9OXteyjFFMCWyEEYX8NByxekTyWo4YOUmPSq_gfZ5uTLZcgH01Rpr7DpcVXsipVFe_y26eI_dGYR4XdVEez7HAbRPEz5Xs3Ba2LTKtcehvGrjXqeVf7quP3UEXubo7ug0EchipGLsZJnViFa__CV6Diyr-8duFyY2HyKLXRYx0Y4aLVIkNn5RZ6nwTNKe52RPh7iHwWWXu-MiZubRis8_qnaFI1CnV0ji9pjBiwc9U6QjuCcW_n5-xazcBn_5AYFr5Sd7ZuPwVVaqSk6RQCkpOzyVwggz2-joJuoD5wqZgmne6YhLoG6XZ26Of-TthbVXw-wYrRBz_rO_ec6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
فلیپ کوتینیو فوق‌ستاره‌برزیلی سابق لیورپول و بارسا با عقد قراردادی دو ساله به سانتوس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/29754" target="_blank">📅 19:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29753">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rtb8EVZbRFyEX1OB2jCZcu5m7J_Do9TtElfxyHF0PVXGWNjsU195LxdK4W2II649irszGX94ugr5Wk15mgPuByOMgXHy0SLf5Tx-wJkXB7iKXfFbkg9iL6w4QRo_f2ytcmUZwhtliZ_k_ta-fOXdp9-7hn0BvFU05hbpGaL5oBboivOWxYlU5vIB1-2OJnzKZ7SdZ0Ju9OWUJ7SCoKEQs0HZRf12QpvoNivI2KAYICIvkJLkM3FIFs8e148d3OELY3sgEQs9ZrpZ9RJnGHW8PCs0hbZg-qwEeN6TE8YYgTFrziCGkm8o7t5VbrUi--7rvlQ4SmXU-KE1cRtMqh0uDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚫️
🔵
طبق شنیده‌های رسانه پرشیانا؛
مدیریت هلدینگ خلیج‌فارس پاداش 500 میلیون تومانی برای بازیکنان استقلال درصورت پیروزی امشب آبی‌پوشان مقابل السد قطر در هفته اول ACL تعیین کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/29753" target="_blank">📅 19:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29752">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzgOxWYadNeKV3P9EEeLiYoL9BlZtfpQEkEB4kOPEPC2TSpPtlE0whq2KAiyWeD9jqQclFUf7UFBdZ1HcB6dfrZhCsYfAvVXg1a9fFbLDdmOTslhyY8y9ZXKyiBfMP9vFNmvq8eSisd_P5YZRXSpL1Y173_LkmVYpnXRI-L3HPKMK9k2GgmZ03foiQsxerqGHpz_bKKuhcNU0kWkqK-qCvxcMP0K1vOYRj65LEqbr0k3MOvzJoGqNEIVkxjLAow_zUyYF4wUCLfE5J1oFOvLYdsI3M-VrCsP_Y2uHbxI_B3Zw_IFfquPaQFj41KRAofK8Y9sZmPO5kPqX5zPgHtlFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
درهفته‌چهارم‌لیگ‌جزیره؛ منچستریونایتدِ مایکل کرک دراولترافورد مقابل‌منچسترسیتی ده‌نفره یک‌ بر صفر بازی رو واگذارکرد؛ تک‌ گل این دیدار رو ارلینگ هالند برای سیتیزن‌ ها به ثمر رساند. سوپر سیو پشم ریزون دوناروما در دقیقه 90+6 مسابقه رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/29752" target="_blank">📅 19:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29751">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGxqgBeGmWsIm-4p2y4o_RF45f8rAA_e-LaSkqdjxUFv2UyK7H4VQMHQZMd86VYXyE_KhIgjGPytFVnioZW-JMbW6ooD2V9qsf-r3CVdheQWw69JQ1VnE9aLwRtPWuNPxEeIIFF1Mfp7aYmCEzBnwbMkF1crtIpvCqDe78TOqdwRMOXXu-wCP06MbdH9dr43iVH2CuopWfFFbUMjJplj1iKuGdXoK92-83-CoJ_N_WEGEHA6mthyWZTH41_1-Cz8XLzxzH9vMMi6zV-pcwjvBJnZyuVFP2Syl5eUmVABUyUUuAC9hytLzDEJcGiNFVhM-LyMuzTsARQEkRwSZPJumg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🤝
دوستان خود را به پین باهیس دعوت کنید و
🤩
🤩
🤩
واریزی دوست دعوت شده پاداش بکیرید
🤩
برای دعوت دوستان خود در پین باهیس بعد از واریزی دوست دعوت شده به پشتیبانی وصل شوید و همزمان با دوست دعوت شده و برای  واریزی شخص دعوت شده پاداش  بکیرید
🤩
برای آزاد سازی فری بت دریافتی میباست یک بار فری بت را با ضریب 2 به بالا کردش دربیاورید و سود حاصل از فری بت را برداشت نمایید
💬
برای اطلاعات بیشتر با پشتیبانی زنده سایت در ارتباط باشید
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
g23
🔗
https://t.me/+FafS3mPlOZAyOTg0</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/29751" target="_blank">📅 19:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29750">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fF2BmzzcE0nYdmzGSqumurvHWywQc27sFfWWQBXzIt6lSAV39UaqHwgB5JytsO0-TjgFjdKDg1liCB1KhYZthmLhoH2LSYA7InpOamli0uTNddJ7oMXYXSX4zmZsad5GROQUbYyI2j1N2I9TeqClF-_xG2TpekDY07kxNKmF2gErowcJKjk-uxX3pqgVCAxgs1R7IBNJ8rUbU1OpHu5mNECGBLBctk3YSAuLuGAixVGI1XBdlXFbxFZdpbPci3MK5WljGPbaaZQP_1WEMamk4_Iw3ekUjwysQUQYbXmqZhiZ-_h_0qxvDFDBCJxe_dqe4aIwkCIxe6p0SrkWuXeTOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
هفته اول لیگ نخبگان آسیا؛ ترکیب دو تیم شباب الاهلی امارات
🆚
تراکتور؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/29750" target="_blank">📅 18:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29748">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H4EER9UnoPTS1GxdBpIn2Q6M4njetdFvwLEHujFr18ZHcDFpo3VhSHJY4m_4Aade1awgkGp8K3UTEr1znPqqbS-vZbUm-BnjUqodMW50-Q_VNNrHiMPaZiaujGh6r9pxF1N3xU8CFW9SpdzBS_OhFv_SEQfSUIP6BDEn5t0hr-JIML4mFZv5MglZZdeZVpNlSPz5iJDCJiQ-4GISYlym_hAs5HmQ4sI3IrHDIu1SUs3r9oFYQBwBHmCzi--Y6ugoX5QNRMZkFNifC6mvVBiSqZ2zecb2kEIv9ePtILjNbUxy3uNox4H775eAeM6j72Bmw379snF21wAsR4yYJXH9HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rkw74UVoxzVo9W-PvtHhz-TMpHWRodU0-pMcOYVxK1OcB667Fi3zPEaifipqdNxG-CKQ6QzGMeVF6OBjd76Bshn4a0MtKdZvJYDz0f--YMt_i5E5-U4I-tLx-LuC4lSyFYInf6YugQW86CKV2qX9c_mjkuIpdo9b6nkSDNXHghDonTVoUOZHenr0_iN9U04zNFrk75q6IpV0zf4P1GqEkOReTOB-YPrlSNNIzmmFyqMdFI4iwB-xhGQAPxVmTdxI99oCYBadiPN2m714VY2L6aVcU-4dpzZkVudofT9J8Ox7_XOnzGcdF_9eGmbYXAlqtBwT8Q1tKj8H6TNSQrDw6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
هفته اول لیگ نخبگان آسیا
؛ ترکیب دو تیم شباب الاهلی امارات
🆚
تراکتور؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/29748" target="_blank">📅 18:23 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29747">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQB2r5F-NstNUWfAxOoOwQ1e-UrooHXGOjZLdcGhFtL16gK2ZCqIMsKKv3LgRGtqM-DpEeDDxm3FOkKvv_yVVTNIDbkKPbY3_tLnnelqGGSH0_P7FcLDIYeDEuCj2WQ2e8jLtcJ4QcunUsOzXKI9j3KuJhuMHwy_f6PsjlQRSfDlDuqvhiqVp27b9CCm2irDpMUew3TMMm5jZ6NrJD2tMsMj7-M1K7YHzlxK7REs6SKxA8r41jbUPP7ciTPxLYymolkHUE-65ImVzeU27xXHT_d0El2v7k0HzvvZG9ncxfnRxx5GKGWj4sxVrqkhA8TXedOSpnQWVdW-MDeQN5bpTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یادی‌کنیم‌از زمانیکه
؛نامزد ویکتور بونیفیس قبل از مراسم عروسی‌وقتی‌‌فهمیدبازیکن تمام اموالش را به نام مادرش‌زده سریعا تصمیم به جدایی از بازیکن گرفت. دختره این امید رو داشت که بعداز ازدواج و باطلاق از او ۵۰ درصد از دارایی او رو صاحب شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/29747" target="_blank">📅 18:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29745">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adae707100.mp4?token=JLuUixgyDGNGiBiixOeYRZDKxE3Al_unhOwxJrb5QGiGWNGgjlFhFCRLCX7RIr8_47MIRMguz6iayleHf64L-qFIVJmQTKi9rTr476Uj9uOUylunuR_-KWuFBOlx-sctw_xe7DUgA4k5K6QdPl8jFfazQ8mWCOGgVyBvuKgzjYqDwQDeqP2mSdTl5vszrNDeEI5f9FW60cf47WYztt8n-25UF0SQSejpoRa9YrmdU9eL2SIEL3MBpukBjevJ2FpNWnzQEr02lrAba2skgH9RjjKiFTOcluVrMgqGy5gHhxm3XFLPFWKq45j5zEAjhloxrKRequnXnHXcRC-EWiMVdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adae707100.mp4?token=JLuUixgyDGNGiBiixOeYRZDKxE3Al_unhOwxJrb5QGiGWNGgjlFhFCRLCX7RIr8_47MIRMguz6iayleHf64L-qFIVJmQTKi9rTr476Uj9uOUylunuR_-KWuFBOlx-sctw_xe7DUgA4k5K6QdPl8jFfazQ8mWCOGgVyBvuKgzjYqDwQDeqP2mSdTl5vszrNDeEI5f9FW60cf47WYztt8n-25UF0SQSejpoRa9YrmdU9eL2SIEL3MBpukBjevJ2FpNWnzQEr02lrAba2skgH9RjjKiFTOcluVrMgqGy5gHhxm3XFLPFWKq45j5zEAjhloxrKRequnXnHXcRC-EWiMVdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله‌ تند و عجیب یک‌آخوند روی آنتن زنده صدا و سیمای‌ جمهوری‌ اسلامی خطاب به لاله مرزبان.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/29745" target="_blank">📅 17:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29744">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlUpIfrq-xSZ26w63_mh0_d2pizNpmnXquClch1N37cXlSXW9IBLQzml_Fw4olqgvvZ2hMOi3jkM1yd5hpFFH0oSZE4kTJhG6b2VqxDBhhfMi9vM5MFLifcInCXXNs7WTehThuXXkPvO7aVi7Nvp-be7tB0gfBbuc2BdwN5mRf0LBpRfmI95wx8eEgZgZeZGOBTTKvH6dWrMwu6yxxRPZzjAhR33i-fqjLLh7EA2-QT-fvmPEAEmmnzUl6ePWJOoB7L1Jg3UFJNdnPQuWs87OBQ5fj-Fm3eEMtBEvtemrIK2h-mNhnIkxZLHD3mwCEJI2Xr295cWSIFPhPYt_s_D6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ AS: میکل‌آرتتا اگه تصمیم گرفته باشه در آینده‌راهی بارسابشه فلورنتینو پرز سسک فابرگاس رو راضی خواهد کرد تا به‌‌تیم رئال مادرید بپیوندد اما اولویت اصلی پرز اوردن آرتتا به سانتیاگو برنابئوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/29744" target="_blank">📅 17:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29742">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihTRoBqsj1XQdXUM7HXH2DQIIkkUOhEcxh7d9vZxXsnh7OhneUyLqHm1FL0SwbhB6NMQp71mAijM2xY1gzh8O4Gg6R5hnyMuGBCrega4jCC7YSluTOplQTWCeqNs2EhGEGCLzTGGcD1w3GaV_-Re48th5sTvw3eyZVB0t4SKXJZGcZWKEe4dKmhVDpAO8FKwsibGCu9dVzI8QamyoK-a2qnnfdoJRrookNDGC6HoAz0gSrwB5MbtRi-U3LnmlFwXsDX3aSbFp666tPBwE5PEMLs0ynkABWI42Mncp_F7Tc5ca2Ftb4JasP7mThD-owLoiWfAqCr1mkrq70Hywb0kLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
خبرنگارباشگاه فنرباغچه هستن که معتقده کارتال باید درفنرباغچه‌بمونه و باید به او فرصت داد. باشگاه اون‌فردیکه بطری زده بود تو سر کارتال شناسایی کرد و از حضور در استادیوم در فصل جاری محروم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/29742" target="_blank">📅 17:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29741">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvOpIM2oTVa8VEZjT8CscUdVzb9WU06UhL2321XKNA7lCuaqHtCe7_T1nsE-mjwuIepN875Gaux2uOjr-Cxlad1iklpAsKtJoSsg4HBibJT2iOrJXnxhNPqOi_7q8JFmv8gs-VufjdqYbmqQfF8ZSIqknVAn6dAAa41JrwOcLWj0KWPy5llV7kZIPJmPq6Id2AjQN5ovve0RfzEufdxyfo4EdcQVYBF1Ugr9HPWshqhcvohGreJh4NhxOp3f8_b-05k5yDobPvEe7DfXNfenKa6vyNXiCS8m1Sg-o329oaJ91-mf5PMpf9bNAxpx9xzacZyoQlw_DesrRW-GiWUdRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔴
طبق شنیده‌ های رسانه پرشیانا؛ بشار رسن هافبک عراقی پاختاکور که‌اواخر آذر قراردادش با این تیم به پایان میرسه از طریق دوستانی نزدیک خود به باشگاه پرسپولیس اعلام کرده حاضرست نیم فصل به پرسپولیس برگردد. طبق‌پیگیری‌های پرشیانا؛ مدیریت باشگاه پرسپولیس اماده عقد…</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29741" target="_blank">📅 16:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29740">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-e88VinBTQzIRDcRLKUT74QF6l2wWvPv9suDLnMlwmfH-vvg32NzVxf-5NtDT12ZwqYfTAEmBhMEtxp0H6kikjpoiWziS3kCqPQ4VCnCrnKdtjmeFDKbSL3q_txsncCzAYvmkMFzGpa2UF4bgwUnVBpg0zkoMjXI8p28J8SF9cxn8Hs2xPJMk85kcD2uioUQJSCczSmMVVIuGveAeWCnD2td2wUtwyiv174jQjMGePo7m3bDt-A1I4C7CZ8IVh4iQnHxV4hM0AsyDI2xjL_72hPVcXvD1C0RdvEU7m2ZzArZYc6V8JFwsN_LW_mGlN2Thqc57IkijJ9TS65s486Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هفته‌هفتم‌لیگ‌عراق؛ امشب هم تیم علیمنصوریان دو بر صفر بازی دو واگذارکرد هم تیم دهوک که تحت هدایت یحیی گلمحمدی سه بر دو شکست خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29740" target="_blank">📅 16:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29739">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OL03hMdGd56k9T8ilwFH8Cl0k8XIIYz4hGX-1rGhBQB8Ql1g90xYW4mb1ah38qhNT2FPpA6AoteRkvsiVJvcUOwzjte8zQeHSHUAY3AQut_iQuJPIi4cMx5RFW32ygBzXZl5waGwJKf19dXXi42DxAmczSgVVHMHOFUeCRGVBjP1Vbhl1eMS8USwVFkR92wWVTn1J-VX8OWD2_bP732dZjLIlemv3QGh0EICpPIBtLhcx04PAnYOFkGbgjuCC5g2MwWepQ4EFfmNldmLiudufaRLbCqkB4c0Y0hepxd34w2bs3aXgXlz43Z6WnEncxJnUpNVFuX0B0CokStw0VU2IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
در هفته پنجم لالیگا؛ شاگردان فلیک در دیداری خارج از خانه به‌پیروزی‌مهم‌چهار بر دو مقابل لوانته رسید و باپنج‌پیروزی پیاپی در صدر جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/29739" target="_blank">📅 16:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29738">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsxqpUeSWqky48moLFrf11RBgG_ugaX0e4C-dllxM7hgFoQ22no7r2zc-5pjw4hSCcETfKgbshHJ3YVDv_MNtFZQHsIKDYR_1rVkD_H6HF5MogPK6qetO0YASGXvp9LVMBCozFFHE2fCoQMLATStstlmeAZvDA9BEDe0ukvOHimUxiGdKGqY8xcbnKZTOYlxuhpCfd6a8mEyWJhGhRa3ULGk_KBi76j0RUNSPU41HOjcVIvSaOusEKiY2-lTGtzfZah8pMuCxsAJASJEQwjTbqZpMKmKxh4-YIulFTYm3bvIsUd595Gq7_rh0zXuKCUTgwIOUeONgHDnlEqYPzL2ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌عملکردلامین‌یامال و رافینیادیاز باعملکرد کیلیان امباپه و وینیسوس جونیور در فصل جدید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/29738" target="_blank">📅 15:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29737">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2999a059e0.mp4?token=GkxwYbougls3VkBTzimI0kJ3xnTzWquvt9icr2YHOlpvCnzhv3JJUZzFIwkc0yaJtrai1xcyxBIN12X7Bt9CCiTayZtUrcgbh9NWgpOYDWFOOvvjQIH74ToZceOBUUOuPUN1wdNu-DkMMN788BwfgFS1gzlgooR7FiNmwF0VTHNVO6AQ-T5KE3ik87q4Q5vdt9Fk9oxjJxhg17BwNuoQsXwnuJFTvBESlRdzAsM8ztQsXIaGxTI6D_H85XKLwFCP1sUhD_4WLrvxPj1aWH-ulQnPS2mG_b4MWWdQeCEJ647BKy7L5Fgv98TxN56qLpkswEvmYNQg19DGGAzUhFIgaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2999a059e0.mp4?token=GkxwYbougls3VkBTzimI0kJ3xnTzWquvt9icr2YHOlpvCnzhv3JJUZzFIwkc0yaJtrai1xcyxBIN12X7Bt9CCiTayZtUrcgbh9NWgpOYDWFOOvvjQIH74ToZceOBUUOuPUN1wdNu-DkMMN788BwfgFS1gzlgooR7FiNmwF0VTHNVO6AQ-T5KE3ik87q4Q5vdt9Fk9oxjJxhg17BwNuoQsXwnuJFTvBESlRdzAsM8ztQsXIaGxTI6D_H85XKLwFCP1sUhD_4WLrvxPj1aWH-ulQnPS2mG_b4MWWdQeCEJ647BKy7L5Fgv98TxN56qLpkswEvmYNQg19DGGAzUhFIgaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇫🇷
عثمان‌دمبله درباره توپ‌طلا گفته که؛ تو کل دوران فوتبالیم یه‌بارهم‌درباره توپ طلا حرف نزدم و نمیزنم. فقط‌میخوام‌تلاش‌کنم و سخت‌کار کنم. دمبله درواقع‌به‌مصاحبه دیروز یامال تیکه انداخت که گفته بود من و امباپه با اختلاف بهترین بازیکن جهانیم.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/29737" target="_blank">📅 15:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29736">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTTW6_y-0zGwiRKGaqZzCZv4X0WsHLB3XDaiyfpBY9oEOuvQd3xpdqSmC0Am0LbdElsHKMeUp2ELgyanZqlta0lAPRC2Fua2DClXckBwtenE9INXmmBZmeuRWs7tWf6DyG0627nQkRyeuLRyifIbesRrM6S8Wu5fpurhpQtBkDYS5bmNyQvU90PqdkR7HLvnJDo_WRWiTgOt5FG7RK1hLWFmQ9Dv_PJ8Odb63VyDnTUmYnBXJ6_fiZIaQ75uVsaYpPLd3fUJ1MnJ_ZMgIRgdXQWvGgRF4XbyM-usiHy8eJGkEOacwrmBUys9u3KRU8EJ6M4xFLAIltiSmHGPg-bLUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تمام قهرمانان نیم فصل و قهرمانان فصل لیگ برتر خلیج‌فارس در 10 دوره گذشته این مسابقات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/29736" target="_blank">📅 14:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29735">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/liNXujwij1-Be1g5J-o4Lpaq1QZ03QXQuyktOeZjZnJGzK8UAnUE4VWbjcf934GsEmiSGv78us1Kl4CDEDbGiDk9WrU0ykqQb91KhJJglnKgyPYckJae68RNZ6FhNBs4l-HIkOwnhspQU3DMzzAfJUhcPNCspN9hf0BNp8HlsCwilx6qftu5LV0HEHQHjMuFE8QiEX6bdc_teMf-PoMKeT_JIH-HehtAiCHPjJHRQ4CaVf73J4JiFVWcfTkFTMI_1nlNPvUt3C5r5CNXkcYCMgX5ZEQH_qiO7QcktEPqzxm8aoeTYqgR-M5M-KHGDO9GEVedplS2XNKVq5hPwK7nDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یاسر آسانی ستاره‌آلبانیایی‌استقلال یک خونه 75 متری در غرب تهران برای تدارکاتچی آبی‌ها خرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/29735" target="_blank">📅 14:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29734">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3be0ab7dd.mp4?token=aBPTyaK8CjZ5-zE-WjV5ma4DLoKAK-y8ycAuSFCt9DRRFbRP5roXl4Cw8p9abL0EpBb43Oamo-ucQK0z3WN0yOHlq7y41MaPkw4KBv2Bmz9L0yeKvtm0fW-eJSuZB1NSQuwHGL4CaLXzq4cnjBLxVIjYO4MXyhs709FSWgvVV-P3G3y8_0D44dD51St5QZo6B_RszzwjwILbuRlyHA5nI0A83E8Fh2-3YAGlOQR8iEiGHJuV5eEC9DQdDcZXPxezCiZKADWvkXdCEofOSYDKJNnuXru5TvCxUEPAZLetf8FuQib1ikHNq4ROlav39INokoojZkMDBs7zyz-6is2b2XNqszDvDPnJOzlFUpOJo49Z10ruW_Q4tyPhr6wZSw_PJP5ZiSHQvqNJGxDQpzF0bNEdnG1-iM2RiIkgNylINRQAXg4t0ZES2O81OKVuhv34Ktvq_7LG_FIZ1mkp457Nl3Ein7kDdV8pW0S4W7kD__kB5B091YdIu3QqEc7f1bR1zA87TqZkR_pAg1p-1yHo_LxnOvOKgp_PIxf0-QNme5YTbn6BA0DYCw9gxeDx2VKxGxdgUjYAmhMytUBtIQ2eS1D4xfuVdtl7M4lEztxsIHyBGI9nXspPupv_iabvE08ptF-Db-xNh8sGtW0yRFuyxjJD-mw9lZhvR4VJemdbMVo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3be0ab7dd.mp4?token=aBPTyaK8CjZ5-zE-WjV5ma4DLoKAK-y8ycAuSFCt9DRRFbRP5roXl4Cw8p9abL0EpBb43Oamo-ucQK0z3WN0yOHlq7y41MaPkw4KBv2Bmz9L0yeKvtm0fW-eJSuZB1NSQuwHGL4CaLXzq4cnjBLxVIjYO4MXyhs709FSWgvVV-P3G3y8_0D44dD51St5QZo6B_RszzwjwILbuRlyHA5nI0A83E8Fh2-3YAGlOQR8iEiGHJuV5eEC9DQdDcZXPxezCiZKADWvkXdCEofOSYDKJNnuXru5TvCxUEPAZLetf8FuQib1ikHNq4ROlav39INokoojZkMDBs7zyz-6is2b2XNqszDvDPnJOzlFUpOJo49Z10ruW_Q4tyPhr6wZSw_PJP5ZiSHQvqNJGxDQpzF0bNEdnG1-iM2RiIkgNylINRQAXg4t0ZES2O81OKVuhv34Ktvq_7LG_FIZ1mkp457Nl3Ein7kDdV8pW0S4W7kD__kB5B091YdIu3QqEc7f1bR1zA87TqZkR_pAg1p-1yHo_LxnOvOKgp_PIxf0-QNme5YTbn6BA0DYCw9gxeDx2VKxGxdgUjYAmhMytUBtIQ2eS1D4xfuVdtl7M4lEztxsIHyBGI9nXspPupv_iabvE08ptF-Db-xNh8sGtW0yRFuyxjJD-mw9lZhvR4VJemdbMVo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایوان تونی مهاجم انگلیسی الاهلی عربستان:
من‌ عاشق این هستم که موقع پنالتی زدن دروازه‌بان حریف رو تحقیر کنم برای همینه اکثرا چیپ میزنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29734" target="_blank">📅 13:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29733">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvj775I_rBqulJtE8wNGDUqAMrsilfOSm7Sg8dEk0dD8O-RNDxAKXCaWOyRAHZsePcObE_8rCks5_wuAjU0pvvYdrxqEV-wbGNf9IigVqB1R5KZPnl5h9AppXdOabkYFvIqI7M_lgZuhUTt897fgumqt1prSOwModZto0hm9YIgA4gjRx6XvdtRraMzXv79pjDS-1nj1O_IpaKE6MPTarWvhnLYoVUse7xHFlpqdUEe_6vRiVqDldBU5IW-mx1oIgpyjwu1aVJ7S-97D_bV4iC9EYgdhUvj9n-lSUb4xs-lTT1Xtote_R9jFfyqrq52bY0K3q3mnZk2a8cb8cbDf6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
خوزه مورینیو خطاب به‌خبرنگاران در نشست خبری پیش‌از دیدار فرداشب با الچه: در فاصله 3 روز من باید 6  بار بیام جلوی شما بشینم، خدایی خودتون خسته‌نشدین؟ اصلا سوالی مونده ازم بپرسین؟ واقعا خسته‌کننده‌ست. بلند شیم همگی بریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/29733" target="_blank">📅 13:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29732">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGw3QAqu7aaxduKORxxhGWySxzVtZrgy5DXWbiFGLaO1Ru68UQetYsQSKY8Cd-j-4Iz5HJexlF3_xdz7Fw6VRr_mXWJBCgM-DYMkF6NoqNjwL0_H7FCGIcO5EcOOYGCJpoZR0LTnQYnQ2jSeqE2bmnMaSan3fRtmpUUpyIa0zOja8lsc1gh9gq3zB0Qk_J9aLuNtOKg7XW8jaeE6lafDae0olCjF2oEWFVBtZaXi7Kx5luLvAidlBIZre8E7NiAwQEyMj7Ls0FHZFmoN2ZvQYZ4hDhx4UYzZHkEdXOZCT9xwkT6KM1BanArQvit2_LnF4M8ECSiBERwkK_T6E0k8bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکردخیره‌کننده رافینیا و لامین یامال زیر نظر هانسی فلیک دربارسا؛ یادتون باشه قبل اومدن فلیک سران‌بارساداشتن‌رافینیا رو میفروختن‌که فلیک اومد و با رفتن رافینیا مخالفت‌کرد و گفت احیاش میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/29732" target="_blank">📅 13:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29731">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83d6c3c639.mp4?token=oVYhlg2z9fQBaJjhVpDUyLZ7vBM3bIfIi2u0CxYdr_cY2IK6SXGXcOtOvGDz0-EOTX9lYkvxD93kp__Q0ChGYiNvENph7690GCYx1AuTHCBr3N1YsEHYI_6iBubqx1KldgYkPJMFAJ_FyeJG-NNbTIuWs-sgwwfgSRWD9eff2zAMDf942x-152Jg5Y4WKIA7ktq-YIQvtEbc8K7x49cSpsymRoluJsNHWBridxt8GSqBkUAn5m0wSSl4cg5wIeVte4InaGUUDTHXrve2Rfx0L8R9_9h5AcRDSzhuje2X73fXR3HaXWs-6FhkKQp_6xZXejhdCIGglSvGGvGxpK6ak7nM7yUOkmeJb5zCceYKC-Y_Gfrf47VsLgehesD6ezXWuifueB7pnTfhvxbEJK2pS0GX3Eb0z_kb4bemO9syICVJ5ET9_KhyptuVsq_CWovk0EYa_CnBKrn-ktJLr940HkyQCKXT_w_pougmRtJQEdrtoZZzFyOHClIjGeSBgtt0Qh3hTZRt5XW2UYda3sgT1NQStVdbWBv6ql_ip8BiHcSYgkoKURRVh58cY_YRftLYV4MtEw5HkT76uzl8tGxjn8lZX3n839e5TjPwYy-BJeRRDg6DLVyF-XgchQlokA_b8MWrlacRtIu7oo_fXo0E4A18uSTSP0qxzy9oWCw3jp4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83d6c3c639.mp4?token=oVYhlg2z9fQBaJjhVpDUyLZ7vBM3bIfIi2u0CxYdr_cY2IK6SXGXcOtOvGDz0-EOTX9lYkvxD93kp__Q0ChGYiNvENph7690GCYx1AuTHCBr3N1YsEHYI_6iBubqx1KldgYkPJMFAJ_FyeJG-NNbTIuWs-sgwwfgSRWD9eff2zAMDf942x-152Jg5Y4WKIA7ktq-YIQvtEbc8K7x49cSpsymRoluJsNHWBridxt8GSqBkUAn5m0wSSl4cg5wIeVte4InaGUUDTHXrve2Rfx0L8R9_9h5AcRDSzhuje2X73fXR3HaXWs-6FhkKQp_6xZXejhdCIGglSvGGvGxpK6ak7nM7yUOkmeJb5zCceYKC-Y_Gfrf47VsLgehesD6ezXWuifueB7pnTfhvxbEJK2pS0GX3Eb0z_kb4bemO9syICVJ5ET9_KhyptuVsq_CWovk0EYa_CnBKrn-ktJLr940HkyQCKXT_w_pougmRtJQEdrtoZZzFyOHClIjGeSBgtt0Qh3hTZRt5XW2UYda3sgT1NQStVdbWBv6ql_ip8BiHcSYgkoKURRVh58cY_YRftLYV4MtEw5HkT76uzl8tGxjn8lZX3n839e5TjPwYy-BJeRRDg6DLVyF-XgchQlokA_b8MWrlacRtIu7oo_fXo0E4A18uSTSP0qxzy9oWCw3jp4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدشد؛ بااعلام‌مدیرعامل‌فجرسپاسی؛ علیرضا بیرانوند دروازه‌‌بان‌تراکتور درنیم‌فصل‌با عقد قراردادی تاپایان‌خدمت‌سربازی به این‌تیم خواهد پیوست. بدین ترتیب بیرو تا نیم‌فصل بدون تیم خواهندماند و راهی لیگ آزادگان نخواهدشد. بااین‌شرایط باید ببینیم بیرو درجام ملت…</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/29731" target="_blank">📅 12:44 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29730">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCd_aO75ir1p02fAS10EXm0TKoprWv30nZBHTZ905Ggmnvrs25gF_CgHYaBX4Qel0G2GrWC1ppyq_8w8JqFHtCZlzM8Gx5bNld8MZTh0nscLnoddCLQqqblCrZAUz3QSXQ6SlvU5KfsHJg9Jjv75XG5xUNtfRNBCcwQkUKBfnIiOrQBQG2TitcNLKbM_H04JfDf98KrMQOPe-umFQPe1_FeLmnFG0NuGyv2vpyajHTlOAhAWGlnIZyURLzL2MJTPyBflidCfTq_tEp-XY_zDnRjcV4naFkWINaIMrNEghyVhW2I9DwRikh5-EN44ICKS_1JGnEk01CztbWOAix-FMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عملکردخیره‌کننده یاسر آسانی ستاره آلبانیایی استقلال در لیگ‌قهرمانان آسیا: 10 مسابقه، 9 گل زده، 1 پاس گل، کسب میانگین نمره 9.1 از فوتموب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29730" target="_blank">📅 12:23 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29729">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b04b36d02.mp4?token=S3VdgrlQQKr7afv8mQn6INJ2wFFb78YmRDaAiPVEYzeDtqFeVhSTFVOs3rLlsFqqyMHYb1f7I0j7IK1gq0EQ7cF2h498KOMEFGSA0HI0faEdLmKDMO2fCcpi-i8goOlUS9DatFBCS-G2Sjw9XEueaOx0pNtiEcoJJqAsgk0X8Z9o9DoCQFtOeSxGPv9prrYeUBfvdM5Jd0z_P7X-xu54tjb_o2vnTeXiESVjxqPw3cEw9nz2q3IscQXGPLjlc1_7lax172qep7MJXgUMpTjYuoFjZ5Krjs9dBHbwNtuTGTK8zBETUIA4VEFX5h-bn0venp_LZi77loAoypR131q1KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b04b36d02.mp4?token=S3VdgrlQQKr7afv8mQn6INJ2wFFb78YmRDaAiPVEYzeDtqFeVhSTFVOs3rLlsFqqyMHYb1f7I0j7IK1gq0EQ7cF2h498KOMEFGSA0HI0faEdLmKDMO2fCcpi-i8goOlUS9DatFBCS-G2Sjw9XEueaOx0pNtiEcoJJqAsgk0X8Z9o9DoCQFtOeSxGPv9prrYeUBfvdM5Jd0z_P7X-xu54tjb_o2vnTeXiESVjxqPw3cEw9nz2q3IscQXGPLjlc1_7lax172qep7MJXgUMpTjYuoFjZ5Krjs9dBHbwNtuTGTK8zBETUIA4VEFX5h-bn0venp_LZi77loAoypR131q1KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇫🇷
عثمان‌دمبله درباره توپ‌طلا گفته که؛
تو کل دوران فوتبالیم یه‌بارهم‌درباره توپ طلا حرف نزدم و نمیزنم. فقط‌میخوام‌تلاش‌کنم و سخت‌کار کنم. دمبله درواقع‌به‌مصاحبه دیروز یامال تیکه انداخت که گفته بود من و امباپه با اختلاف بهترین بازیکن جهانیم.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29729" target="_blank">📅 12:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29728">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKIH-inYlBqTbQm-YnwXLhjloxDbH-9O50RB6KW6Ytxmeqft1-6yx6aYfxYG6cVoxABJbERy7g1K9FvqmZqmj4Zqt82nE1bJl8gMlAgq2w9LnhrIQa9lx1P4tBlGbYlLMfcTwuqER8qd9TGVEHTmFBN9AsiOdr8O93iG04dsNdWejy62GXeATbGDvV3GxrJtjfi7Dnqybj4s5p13G4iSaeQVNF3x1qODh23pHOjnVWyxm0gkE56HRuGpD9-37tjUco1wnpWjQSuDASifdN4n6wAGMtPNOdg0JwFTRTYL7PyZUH5kNBQIcsevnO3ScWLcN_I-895FApyKCNHklD8z-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه فجرسپاسی اقدامات لازم رو برای جذب علیرضابیرانوند انجام‌داده و قصد داره از اول مهر ماه این بازیکن رو به خدمت بگیره. بیرو هم درتلاشه که با پارتی‌بازی معافیت تحصیلی خود را به مدت دو سال تمدید کند و در تراکتور موندنی شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/29728" target="_blank">📅 11:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29727">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOnHl_576qJYJE9IlnLIAQCn7XKnZQg7As5atlpQWA_HkvmmGyEvY7jS-nAQzv9wfO8zaLhH7pCz8plyuSOUTh5stoXIkaYXER_aAKqP0YCEBV3JKLd97_5VWNLoFKXQwnPPZRNra6Wg2ui4hY_RZodIPj8ClBRJ3KJMh2jHrlKFJ0o3dOC09U1yRtN_BhiGqWVXyDUfKYzzbO_-svXWgtgtDPi--0wxGl2yLWDTyqR7mk7U1gxP8q4vOd-w-Wq8EHdpq8gMQxJgRyx77ojMTfiLrWldDxTik8u1JQGExlj7lc5qh5x5Pw451DiKoiTUODp931rfvhI4sQYd6PX23Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برنامه دیدارهای معوقه هفته هفتم لیگ مشخص شد؛ سه‌شنبه 21 مهرماه دربی‌اصفهان برگزار میشه و چهارشنبه 22 مهرماه راس ساعت 17:00 بازی خیبر خرم آباد و پرسپولیس تهران برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/29727" target="_blank">📅 11:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29726">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e641fb1ca5.mp4?token=GupRxr5ov5uS38Ixht22XTHN4hohh-McjFm7g8tVCF_ERa89dYbPuYN4ElkG9eQMMMf_WnQr29ulyiKs0tRI7DAM8ehNNBWc7ZSbndQEhoSa3Xp4Xl9wwh2qUTrUapDnHkKKW4dmQ9Dd6WSuAV3ZzILlhF5zChcfD7wQwt87OgxpMMzW53u79WEnQfZCbfphWwbTfQZhawmP4dY0DfTHQMyHMTF_OvPJNZf4oC2txsCMJzSFgj22zhFenF4sod6cMo58Dte4y5uS-uFAdjE09YtySRhPCLT8ndhVg0g-_J-KjcqQBWyReh2xpIE2FjwL3QieG1KnrsE1tv73qKeo6TbpUoWd-h8nOEdV3cCqcfHW7XlrdZN6UPk5Whd-Hnjx-jtDlTgS15b27Xfj2bTQdwci-wJI5fY0wNfn2SjtKWirZ7xHi0zN0kNTCYP0UhCZ17pr8Yy38kf5nGNcnqXYrHOKNzPvQH3A8lg4lRGVBbg_F9FwpRHMtZRfWbZGfAzpZvl1QusH52nyoRkXhxZTFyCw9mZZx1sNGt1Luq725KHw1RGq0C5kB1XW0uM5fzTG4VY27UGlagAlxrQYUfdgSlwQEnn3Yy5RdjXrkeWEYlDLICNWMOweJdB1p9YE6D2RAW_hmiN2xi2HKzauoZxQN3Q6rTN1HnhRcS2CHxa4vOM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e641fb1ca5.mp4?token=GupRxr5ov5uS38Ixht22XTHN4hohh-McjFm7g8tVCF_ERa89dYbPuYN4ElkG9eQMMMf_WnQr29ulyiKs0tRI7DAM8ehNNBWc7ZSbndQEhoSa3Xp4Xl9wwh2qUTrUapDnHkKKW4dmQ9Dd6WSuAV3ZzILlhF5zChcfD7wQwt87OgxpMMzW53u79WEnQfZCbfphWwbTfQZhawmP4dY0DfTHQMyHMTF_OvPJNZf4oC2txsCMJzSFgj22zhFenF4sod6cMo58Dte4y5uS-uFAdjE09YtySRhPCLT8ndhVg0g-_J-KjcqQBWyReh2xpIE2FjwL3QieG1KnrsE1tv73qKeo6TbpUoWd-h8nOEdV3cCqcfHW7XlrdZN6UPk5Whd-Hnjx-jtDlTgS15b27Xfj2bTQdwci-wJI5fY0wNfn2SjtKWirZ7xHi0zN0kNTCYP0UhCZ17pr8Yy38kf5nGNcnqXYrHOKNzPvQH3A8lg4lRGVBbg_F9FwpRHMtZRfWbZGfAzpZvl1QusH52nyoRkXhxZTFyCw9mZZx1sNGt1Luq725KHw1RGq0C5kB1XW0uM5fzTG4VY27UGlagAlxrQYUfdgSlwQEnn3Yy5RdjXrkeWEYlDLICNWMOweJdB1p9YE6D2RAW_hmiN2xi2HKzauoZxQN3Q6rTN1HnhRcS2CHxa4vOM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
در هفته‌چهارم لوشامپیونه؛ PSG با درخشش و گلزنی تورس اولین پیروزی فصلش رو بدست آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/29726" target="_blank">📅 11:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29724">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ecKKwDdDUIjZKaaj4zIqcBMzQlvAMOGwES-ENoVYQi0wVa8V6wJBWxDXVrQ4wpeA6pu3qtM4QGsConZUNK0Y1aJ2gJpv8lJl7KAiO0kps7cZKC9PkHno23QYY_gnnRo47qR6yqcwOeST4003MhZl0jxg910zLa_xzFPRa_paNRWESAd8JnIxx32x_k16Fx3h9gP7a0K653vCFx4Zf7aUkj2oI3Rk8sgagXgvpGGHfivekOEK-DSyxNkRy691eiNEEP9EXQVcJcWi7BmaSrClEHto6nCd1B_joWhAHoiiqvjJeZaGzrpDoMzJ68vph2xE4O7dMhE18N_HeIZwa7HyYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌رسمی سازمان لیگ چهار دیدار ذوب آهن با سپاهان، پرسپولیس با خیبر، ملوان با خیبر و فجر سپاسی با آلومینیوم درهفته هفتم لیگ‌برتر به تعویق افتاد. این درحالیه‌که باشگاه پرسپولیس دقایقی قبل اعلام کرد هیچ مشکلی برای دیدار با خیبر ندارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/29724" target="_blank">📅 11:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29723">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96cf41ef0f.mp4?token=SnyLw4HToZF4Ml31cA9zdMIPnWL-_IsbzkwSAXeOJ73BcXCO5zeBwE8SWxpO9vkMoObkF1GMgIDFs_k3tyPKcsBet8S7rIMT8A_tmF6eoPIUqBlCd3qh1tIUB3A5zzYl8fZ9Jj9_YVk9T_8PKpe3-AZ09dzmdjLu4jzJ6mt7taGkdEQpNPgCq93d_5Fpu87_rJhoHQcll89c8iblqIqUGAmNks4ZLSFN88G59NoqbyjFBbzcHUQbrRfaP0YVh1GBZNuVnsN0ahZp6pxtI28HMJDKhszEdINuXj78oYSsCN-aQfo0Y_MIsgNNL2ga3NUJ_c7EMPvwdGeM9SAC49-PVYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96cf41ef0f.mp4?token=SnyLw4HToZF4Ml31cA9zdMIPnWL-_IsbzkwSAXeOJ73BcXCO5zeBwE8SWxpO9vkMoObkF1GMgIDFs_k3tyPKcsBet8S7rIMT8A_tmF6eoPIUqBlCd3qh1tIUB3A5zzYl8fZ9Jj9_YVk9T_8PKpe3-AZ09dzmdjLu4jzJ6mt7taGkdEQpNPgCq93d_5Fpu87_rJhoHQcll89c8iblqIqUGAmNks4ZLSFN88G59NoqbyjFBbzcHUQbrRfaP0YVh1GBZNuVnsN0ahZp6pxtI28HMJDKhszEdINuXj78oYSsCN-aQfo0Y_MIsgNNL2ga3NUJ_c7EMPvwdGeM9SAC49-PVYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
کل‌کل‌های وحید هاشمیان سرمربی سابق تیم پرسپولیس با پیمان حدادی مدیر عاملی این باشگاه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/29723" target="_blank">📅 10:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29722">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VD1kIknvnyznAdWJ9okoDyXaxbnbVwpNFDkwS_eY7uhvw_5dItykFQr9IeWjqprFDhwb7LUcC1KOtpsQ1o2yX8Mge63YF1tW5dl0f447eMhGJUEj-r3wHlJj1YfpUtgoqomHVzbwCVYNxOTcVr4MjBhQp-H-GNEmjD88blLsrGZk4btvCmD5SJAVB8SZg9x-3OjTMM912EFt8r8NC2YXvLrbeUUXR_ZG8YHh6q4M_M5HGEy_JTUjDxpLH__8Uj7F-vcd_1TH5fcY7JC_xs3qCkR7J6-2b0JdlpQhspSmN8Y687H1wBKZbZ6-yPRCpw2kqyLpm1M1NW6zPDL2rU8J4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیرانوند دفترچه خدمت سربازی را ارسال کرد. دروازه بان تراکتور از اول آبان‌ماه ۱۴۰۵ دوران خدمت سربازی خود را به‌صورت رسمی آغاز خواهد کرد و به مدت ۱۸ ماه در یکی از تیم‌های نظامی خدمت میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29722" target="_blank">📅 10:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29721">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8UN400GsAciEWRs3F_bnIKrwnuonuVa_wWWH3b5oK84bApv9EICrTBBxgMLootOSYx94-KGQ-GJQHA1uW70DirsybqmMGWQ_ChIhqjqtrBufz2Fi-VX3k5hDa7-VzUqaw90iZWCNcmDAq8vMq7kpIwwJ2o55mFrPZKsVEOdF_XwnTaIxocZ-I305NuR7Ay6xDn_adWSrsX9XRymXwzZnHqz5S_tYhj63QdOCFxWUGHLWXTSC5KzGAyEnLODZzvxNCZWlw73ylIEpmV8lFKxn4_qgcXNKTql9mA59w3JKncDm7InLXB6AAe1zAdfEKoQueDXm58aAv5TaytIadYRGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
کمک‌ داور رقابت‌های این‌ فصل‌ سری‌آ هستن که در بازی اخیر فروزینونه
🆚
فیورنتینا حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/29721" target="_blank">📅 10:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29720">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aw4NhDCI0fOsXq8N5g6T2Psa74jovsxKY0J9RR6YdHf-N3jyUBK1-rNphJMxBuQahFDalfoY4LUOugJfyfk3OQgcJ9rDc7JpEzBbJQiEX1Jcodavu9FdotuxiBYcnGNaEEOfjapyhkDtH1YB1bVlSEgztzdQmTUC0bOmn5TzkMYnoLlu2M8zV8kvFHCqyEojidKDbMVJ2fqocsXP0B0S8Uir68ZXW7661BLdh93YvpCKBLPLvm9ddYtZRJjqnnnmQleh9Dhv15aVH0Pm7s1aRL-BZ-oU-qS2SrQ0LJzu_rfmq2gl7M2sJt0PQ7cxeO8vE7vWpQq7myWaDLwrZxr6Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
در هفته‌چهارم لوشامپیونه؛ PSG با درخشش و گلزنی تورس اولین پیروزی فصلش رو بدست آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/29720" target="_blank">📅 10:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29719">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcrtvLnugNaS2vaYqYlcmBGILMf2xi6f0NhOBn3lqrMCxJkZItfuncBEl18Z2ZtUDpmC7Wzgdhm51rjXmej7Npzm2rjxTBs4UbtUuIVCj923Hu2LrPOBAampCobvDTJ_uoALu1CXj4MF52ra3ULXQSdEywFkIrFbff-LYQ3_44yLY8cfn7N3KIdu_b6iFThrSU-UxqDKDtVsOsEHWmwPYq7MflLCPkY5kTc2nGJ8iNaEg-8OaLg6s0aO6n4uRdvL26newtpx_p9CEdrEsUZz0VesgvEzkII28VY_0c6QPwsPdyn1wsErn-R5GymhdGrj72cs1yepQLaemmROD6TuGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌لالیگا درپایان‌دیدارهای‌هفته‌پنجم؛ عملکرد خیره کننده بارسلونا هانسی فلیک درفصل جدید: پنج مسابقه، پنج پیروزی، 27 گل زده. 5 گل خورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/29719" target="_blank">📅 09:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29718">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXx0RybpTxwugLK_3vHJMJ6RVZg0NvePYwwku2Nnqm-HvX6fjAIfrAEFyb25T3wNLD6pTh_i99kAN7lJk605L1223WzufekIT-pCOnjczeDxvZw-rFzdpw7d12cPQcyAzakywz7Xe9Iz5U9Qv6Nb5psgxmbFpCxO_OxN5L_OdsKg7aAjTvtIXDlNX5HpKahFgD_5GpmoxeZZ3TQyvao2EC_EeuNxLJG-mQFoXbJVQxL-Q_MIjUnjo4iqLHW9lHsdYUAu3g5NPsNGdgMoiWNqM3kUV_AVIc0L64CMVGru9VBEzAFrfbyDqxx8ic8PKb9KmlIGBmk8VMGL7JI8x_6onA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
۱۰ سال‌از شبی که قلب پرسپولیس ایستاد، گذشت؛ واکنش امید عالیشاه به سال‌روز فوت هادی نوروزی کاپیتان‌ابدی‌ سرخ‌ها: از آن روز تاکنون هربار دقیقه ۲۴ نامت از سکوها بلند می‌شود، انگار دوباره برمی‌گردی به زمین، به قلب‌ها، به جان هوادار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/29718" target="_blank">📅 01:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29716">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bas8ovH7bylfeS-KA42RmErnu5vTNRj41LixzD7G4lde8Pfw_P6DAbzJvURqTmo93VRIJHqgThqPx-lVTmGISNnVci9WO9mU0RkUfyWohAWwyFQxb6Kj8SDuuWyys4SMvJ2xm40qkOMim3Jv2FlpbPAVPywGoiXErxSo0hdQraNLb7H1Pf-VORS8bAGvPgl08-Hd4GNuwHDH6SrHi7licQwBfxTm1RlDZff5MlYv7fzu0HgBTIsoNT3twSAI8Hx1zahFmU-wSFIk_zEHz88wYJd6Bdsgh2Gr-gvcdN4qOBwCexfiVNk6E7TVxWYILpOa0vzk0c3Ai4WvG-aXHazQ7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌امروز
؛ا ازآغاز فصل جدید رقابت های لیگ‌نخبگان‌آسیا با جدال مجدد یاران آزمون برابر تراکتور تا تقابل استقلال
🆚
السد قطر در عراق!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/29716" target="_blank">📅 01:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29715">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtNsO1j_QmkXY7_M-ImcBtr6Jatgo4O7YZsZa67H3p89Z1VoQgJdovSeyrXqg_WVudzgmEnWLmGTnOeqSN30TYseqAm-1tUsw9GgW0cbjTxJbE6J1eZfEzATEjjU2schhQONjjapIacY0Rae0Nh5yIM6fB8_G2FCtM7-9oUQwzICsGsIAMEmucK8GIQ4JDBKgtSCdS4AlghsXQ6_7fdfUqU_KfPqkljgyXf3d_Cl1m1GC1VWeA9PgBh6why5w6B-I1lVOW2jmKgDONtLX-5NUWwoL_G_FJPeqPgY-DJY86lN5rPZ2VNeXTnT4bmUF9z1uGEVOaj8MYtt1W4CImLvjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
ازبرتری‌سخت و پر حرف و حدیث سیتیزن‌ها در دربی شهر منچستر تا پیروزی بارسلونا در ادامه درخشش‌ های یامال و رافینیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/29715" target="_blank">📅 01:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29714">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmR3IlOpCO_SoSHqDsj00Y3pUw-Z1dkSRzLmhRa7q1RJczLtAQuWYkP9pPw23MKnUdBXQk_LQDw1tYEUxtS2Kw5CeoSEVWSgz-EF3xCoTfyOXQiWqAm5QyE2g9kQv1TDvAbcp6PanIqEMwUGxSXsbcckeB6Kp15iloxDSZ1RTcOsyH2oygE7WjsABvN9Qsz5_aQSUNBGFO9I9vDIK1K1EKc-IKDTl_OTUnw699FVI_kKDu5XYu0rG3tr_EPcSj85l3TEym2Qn3ImkdyBqkpAnjikPrR-VYlBgwR3MU8DvWyjZ9WXVQILNlqx8vTY_ADJnegJDMZ7tUMWPqQEbaQ6tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل تقابل‌های استقلال
🆚
السد در رقابت های آسیایی به‌مناسبت‌بازی‌فرداشب دو تیم در ACL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/29714" target="_blank">📅 01:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29713">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSnBFZhaCckhLrhEaYsnifEe4gX98PZLI8zeKMfv-2sS5QpfyvcwHYpGlKDqD8Op6Dq8PL5P5RqqvkYl1zirihoDFakrZGBlmDEEkKkKvIk6axQ3vvDD5vuZqbD2xXsmNYVZZeLme3Ad6QIdfLJ4nibZWwCTNW6O8bnunFVm7gv0CDnGMTvF9YNx0G65LNXcN-3lCX_4yquyMF3KkJcK2ZFUV5oaA7K3UD7lPvQxb1-lJnlMHs9E7kxP2DBgZZmw_7vI8xMMXuyya1IFlydbWqJji2EWvAN5-7G1y9hJt--LsMjPB4mI6JOBKrlUB46Gbgp_YggCpIL4G0gTf66vQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام مدیرسامانه هوشمند سوخت؛ خودروهای صفر "نو" بالای یه‌میلیاردتومان فقط میتونن از بنزین 10 هزارتومانی‌استفاده‌کنند و سهمیه بنزین 1500 و 3000 تومانی براشون حذف شده. حالا سوال اینجا ماشین صفر زیر یک تومن چی مونده اصلا؟!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/29713" target="_blank">📅 01:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29710">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZV1NVQBUH_FLY7IlIryODvSL_D8WIcVr7eNTOyKKSxX_9D-D_9NED-n4N7e0YP_v3WncpnhmvGW9FYSV3MEtgOJAsFp8KiziLKbu16XIlMbUfRfKWwH_8ElJm6Jg9PEUCIvj_rSxV2HO2xI81HRaM5qUlcf5ZqVPFzAq7D7KaFPswYoPJBwYNIEHSeoEybHeKRK3uwkikvshuoV-m7Wo3b0eVIrpNj6znhsFrQKtuaf3kPjAh1dAC3SI5c6Hv-yjm8uFzURqf4QVyy_4gCrOB8_bQwp7X6JsuS4GPM4qJHELciAE1ctPMIBehaeIg7CQ_liuJElnrju6xV3Q3VPl_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29710" target="_blank">📅 00:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29709">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TWrSizzzMa29cPEKrHmrVqOemqHOZpyfBoSZHLuFfl3F3U8WZ3fUKPzi3VYDUCVi7JZAbfovn3R62UKBDWLoGlCrKTsS1OgYUrWBHQsdr5r76t9A1RCMUcZh_K87TIbS5qyriJDA7zQTI0dhcucm_3jwoqS6GuYTsPYlOFaXhpSzu2bbZXNnKw1c8m1lDtDUTxI78WFgbQ-mUKj-79oJMqdce_xvbS08WVE_duspO2TSZT--70SQbXVsBiJ94CxqG9C9ufxtiI5yshtZI-zAGsS8DSAn4BeeWZ9N_AjINHRzjLPhik9JY8n7fdNV6mHoJr10nvJFRRRUmkKwkJ0F6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
تفاوت‌تجربه‌بازی‌درپاریسن‌ژرمن و بارسلونا از زبان فران تورس فوق ستاره اسپانیایی جدید PSG!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/29709" target="_blank">📅 00:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29708">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKjz-G8tkc6cDgC2KzOtgEhRAitJ3L8I5te6NioMDAVOHuBsK3GkDme62sxXvu-c6T7aqKW1b4kMjLSSkOPhNqw5TWLazpbE0muy_8PUv1bd8-3Lqtrj1Ov1CvZCWj3Icgt8BtxOUWQSEAiD9l_bP9NYQsfwCkD2vnZZqoNFmKrDpcVLv6qhrpzJtlzXZhFn96mQMoHiqp6UZfFTRFMgXXU9D8zdkZhpLEa8cwxHZYpph1AValIztnqTY8pQ0608bX7SmOqRD4g6KJl4AzMttg4q8CCrADuB4TYCveB_byilvK7C0ExsmVmfDlsz_D7iNoN-dQJJYz2X6zFKIUp9VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌تراکتور از اول‌مهرحق استفاده از علیرضا بیرانوند رو نداره اگه بنا به هر دلیلی بازی بده اون بازی سه بر صفر میشه و نکته بعدی اینکه باتوجه به‌اینکه پنجره نقل‌ و انتقالات لیگ برتر هم بسته شده بیرانوند نمیتونه با فجر و ملوان قرارداد ببنده و باید…</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/29708" target="_blank">📅 00:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29707">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dad7qP1hQ_A-TsIPe57SCa2ejKUjWVUMQZu3qSGqEAPH7DaUI9Xv6G66qWN2UCNKzM0yo8IBxrOdhUrKenx2MA01ny633j1lv90eLJ94SbThvDFyu4kWEsVdq92iT_rnNZ5Ibyw0eOonUh41RCCP23-0K6PMvQfslPhZrJXiP8HImHmemgwsPnu3oSMtGA0ybapneJ4uRq-QPORGvTAI2Rpl843SgmKTfTV2KKzVMMIiWBjpnwTuqziO7VTqF-4dMpI62qaqW3sWMotsUlFE-10QtFVTkkpI1UPbqnUWqVVwty4zoBDj9TCix6W6CW1FhKiIwWTueIU1QStY3a-XuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هفته‌هفتم‌لیگ‌عراق
؛ امشب هم تیم علیمنصوریان دو بر صفر بازی دو واگذارکرد هم تیم دهوک که تحت هدایت یحیی گلمحمدی سه بر دو شکست خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29707" target="_blank">📅 23:48 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29705">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uGjo-j8GN8ofMM4Ls3dXPH8IhSj992xdlhO8J_HJMtG2GeD5ZClFBOxCvitwX5wmSCOKoObXRUZuGL7knKYp9FdtsL_TnyXypPjYb_m9GM6b92nZhVtDwvIPOm-wprnPzSd6LDftADcuRjrJd7o0JuD4YGpcrKczs8G97XjMXJVCch9v6xdM9oEcCRXpN6kpnXYvkOq9imHWolq-LyfH9Gh-jhrn2JPWiC4MOf8zm7-asf1TK9pAX59lDheK5sPbMBUYMYW6P6uDpSwn0iY30XiJJhzHwJqdrCHA1A2N8G5i5VXg17b0QP5pZt0LJLJPdqhPac7JwpQE3ZhFixQNHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FdooLeJWduhqQjEXBEL6fms8013CbENAh6QG_JxZHWcC-lUOf1SbpkFDxx4IRwTnvFjCdgkwYKjCxGEyiI0JHxLdTjAjqMo0qqJB91ouUdTvN7zMdgchTj7lj8nY2uxdPn2JviQ-AbBP2rC1TjYMoSQjnSOvgNV7i6_b8wWUla-NKpAFFnqUqL7ybUqfi9Gzmnqgr0BNz6SOqM3-H7iAOIVBV0uVAczVuKiqUM2E2FYvcB72bh9f1sbMCCW6Q_y0bK2FZEFzz35n-kAdUKxkE9WhhR9OfoFhbTw2_gWu-ySJn20MZ7hIZKsthR0oAFQN0MUP-0zDi-l9oflcZdxpRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇦
خبرنگار معروف و محبوب شاختار دونتسک در کنار خانواده اش؛ جالبه شوهرش بازیکن تیم شاختاره اما اندازه خانومش محبوب نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29705" target="_blank">📅 23:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29704">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_ZRAJTTpX6IuIOc5WmKtugW_kqKn76eU0E21I0iXN7RtI6HGDD2FNaQmGDw14bYDpEjt-QB9I9GOUiRmU-5dJY86S0CdVVjRONDcDiRlte_Q6ZwwE3whEuhXq075w4DGiAy1mMyB18yfZH0zLozqZ0W5sYhQtn5QxNysUIzljeoYZyWSpqO29XpKQcSkU93E9R5wri-_XyuFCUYgEpfbj5FErfRmmOiFAgAciUliuMvGwZXFGtFGFJN8mepe49NdgkyvugIqAP1gXmw7ieoW5_coD5vm81JMeVffOyAniI7WrWlDOADyflgFT_XVqJuleeqL89VWeI741T2cgNPlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
درهفته‌ چهارم لیگ جزیزه؛ آرسنال میکل آرتتا با دوگل دیدنی گیمارش و ساکاساندرلند رو شکست داد و باچهارپیروزی‌پیاپی صدرنشینی‌اش رو تثبیت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/29704" target="_blank">📅 23:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29703">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_-urnANg3GY7ydKTxbfi962nyL-4kYNdy3XGqhtFWxAaT48hDV5JY-JvTTL-Xgpqe0ybiHdBqKsLClQeIk7k_wE-fME2Z8SsRzdF8CqzXYmHqHPnL_ej3SeWhvsXl7bzCKepgjAESROPEyFp100xPEjNUgS0ZmpNJ_DmLVtyfAt1ONrHr2E2lTyr-Vj9qM6y_ZtZ29-2yeye0hNdzWvt6p0rWAsy4vuzwAcHJojBXlP7pIbBpb76p3DyusbiQS4fJ1wvoPFj-xyeOzU_VigAQOyWQs6bFpmZfXy88w37l4birUBIMULRggD_1HPdnRA7pHdtmgvbq0j75QuKiGhIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌پرشیانا؛ مهدی تارتار سرمربی پرسپولیس‌امروز درحاشیه‌دیدار دوستانه سرخپوشان جلسه‌ای‌کوتاه‌بااوستون اورونوف برگزار کرده و به او گفته که درادامه فصل‌بیشتر از قبل به‌او بازی خواهد داد و مشکلی با ماندن او در تیم پرسپولیس ندارد.
🔴
گفتنی‌ است‌ که علاقه…</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29703" target="_blank">📅 23:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29702">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/780ec53923.mp4?token=P2l2DxiJK-wDBPoYnBsu_WDP8l8C--E3kO8X3YcItDplJb_1FhIPXql6aFTFoLmIlovkfvvPGPBfn7haj4YTdcVurZQbkwA8z3oiH9FUUZJBjXWj5QgW1MBOVf2XBnBjk85DH083yj0gXTOCmzKXl5S5GzTK7ZeARTR83uTBBd5nSq2SUxFHSdoRgviKchuz_DkMDAxtlg3k7w3W6DphUbmF5exLdmiLZ1Dy230lu1DP3TJWqJ3RuFHBOR27fQMr0K9V1FSTJ9wpuaeH-orjqxX6MJK-WNqnylN0mE-gK1F0cTEEK7T1uAlFDanJ_jCXnP14WE77WemCf0HKYZDAzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/780ec53923.mp4?token=P2l2DxiJK-wDBPoYnBsu_WDP8l8C--E3kO8X3YcItDplJb_1FhIPXql6aFTFoLmIlovkfvvPGPBfn7haj4YTdcVurZQbkwA8z3oiH9FUUZJBjXWj5QgW1MBOVf2XBnBjk85DH083yj0gXTOCmzKXl5S5GzTK7ZeARTR83uTBBd5nSq2SUxFHSdoRgviKchuz_DkMDAxtlg3k7w3W6DphUbmF5exLdmiLZ1Dy230lu1DP3TJWqJ3RuFHBOR27fQMr0K9V1FSTJ9wpuaeH-orjqxX6MJK-WNqnylN0mE-gK1F0cTEEK7T1uAlFDanJ_jCXnP14WE77WemCf0HKYZDAzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیر امریک اوبامیانگ ستاره37ساله‌سابق تیم‌های آرسنال، دورتموند و بارسا با عقد قرار دادی یک ساله به‌ل اکرونیا تیم تازه برگشته به لالیگا پیوست. جالبه بدونید دستمزد یک فصل اوبا تنها 600 هزار دلاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29702" target="_blank">📅 22:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29701">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rve9e0zN8kKArcGELt2BeA-Z2KBHEUwMwG3P8jXbcjoGoswE2p3D7KczxnPBDPLNu-AGGb-DxO3ZWYWF-9KUXOMJJXjNh02c6rcYAI9C_OEW1IdxH3uuh2XzJh0m39erKGbncZkXd4NMLLKY8s5Sbt5v5ttBOU0DevFC787uUh1tNcg9tDBVluVreTyNQ2zXvpBsyEEebGs-5dx_K_huPyCYvPwLLXFdjmBMq4Dq41ss6QMt3CHhiaWcDdK9GzSIRGGO7IH78P2-r4m-EeoMgLraLRk1dEbVa9EFDrmyCpSchx-Zwou4z4Ozn5Uxp5EkYfhh2FuK_6TjvgQ2qYUiqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امروز عکاس‌ها دوتا شات جنجالی از لئونور ملکه آینده کشور اسپانیا درکنار شش پسر منتشر کردند که جنجال‌زیادی دررسانه‌های اسپانیایی به‌پا کرده است. عکسا یخورده مثبت 18 بودن تو کانال دو گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29701" target="_blank">📅 22:18 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29700">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0eb0365ee.mp4?token=p3PcMzn7jfgUmvITI_Ddp2uPxZRInm0XDO2o3dMS-ZmPVycjRZj9Ejn-g_3IiWdxw1iQgtaiddYd9a4sDrUpoSjwtKnO_DLJX_sPBz3nJjRVaVm8mKr3fA1LfLemmtnwOB3IysRGEda54TlBazpoSoUdkJXFIJ5R_PlKLJ9CO0ereYi8XFvoJUdVuBR-iW5E8X9RfWWqhbAOs5VcynyzYpnHbUqkcX4DVFPlHbls2_YtZDzulm3wybwWGZBi1jNBU3EVGZfDDbQknA8_ctyqjwT4GnvH7txjxxao_kVKLnyqHPHbUcU_Mrioa-DDy5Vs9hm7-AdZf_B_0vvet6Z7Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0eb0365ee.mp4?token=p3PcMzn7jfgUmvITI_Ddp2uPxZRInm0XDO2o3dMS-ZmPVycjRZj9Ejn-g_3IiWdxw1iQgtaiddYd9a4sDrUpoSjwtKnO_DLJX_sPBz3nJjRVaVm8mKr3fA1LfLemmtnwOB3IysRGEda54TlBazpoSoUdkJXFIJ5R_PlKLJ9CO0ereYi8XFvoJUdVuBR-iW5E8X9RfWWqhbAOs5VcynyzYpnHbUqkcX4DVFPlHbls2_YtZDzulm3wybwWGZBi1jNBU3EVGZfDDbQknA8_ctyqjwT4GnvH7txjxxao_kVKLnyqHPHbUcU_Mrioa-DDy5Vs9hm7-AdZf_B_0vvet6Z7Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
درهفته‌چهارم‌لیگ‌جزیره؛ منچستریونایتدِ مایکل کرک دراولترافورد مقابل‌منچسترسیتی ده‌نفره یک‌ بر صفر بازی رو واگذارکرد؛ تک‌ گل این دیدار رو ارلینگ هالند برای سیتیزن‌ ها به ثمر رساند. سوپر سیو پشم ریزون دوناروما در دقیقه 90+6 مسابقه رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29700" target="_blank">📅 21:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29699">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmaaYGUVwtOCQhgrZnrlk3qqib50uc5N44i97h2-qtPrDU6IYWG_bUBJmv_3KUlxTdMED7VepwPsY4QBGZBHGZHpCFLnW_Rui8bnU3tr36wRdY_Q-t1xp3DjwS2GGj_l6O2r1ZqKVqB_GOyrJ-nEkuFnT507PYIaBj8qNIZCL-sRPlxwtsCFlwivqffjgx6gzh4DtltpxiMBbOM7yHVER4GhP-6RHAYhcpewusAaOGbzIbmBrlQCK5WTN8g64fbSCtGedIjrTuqQy8trwFqUHeu7__dY67_-REX4VFuJ12j9DWwVA6mC8zMbpL7y4kchTBiplkzZ6jhDh22bnG5D-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به‌مناسبت بازی فردا استقلال مقابل السد؛ نگاهی به تقابل‌های آبی‌های پایتخت مقابل نمایندگان قطر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/29699" target="_blank">📅 21:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29698">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c65CsxBCTmIAiftzUE09UEsIbUkH1HJPi7scHky-f4vDoUyvMAQ4J5-bXuf8WmnfX-MumwqWa_KxJBEH8yczImbaJyjxIicl_-QemA7apb29GgMlOkQ-EMnpl8HdRdyyM7AqQU1G7MPiMDJqCnaLXz0mG0tuEUIQy_Zk9n3Ej0CWrO6ZTMrk9ZFVYHYgsmiAH8vsW8upQ7ZzKTfmkCJXdwowbGFOHXW7mleJXun1KWUc8FRd_OKP7_Kd4UeNojCyi5HnSdGwNvuYZfjth9T1c7r11XPkx48r_Jm4MmtBv2OOJBA_zqx9vEjM8HR4nZ17OUYns2ZaTxhOtkoVeLay8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بایرن‌مونیخ‌امشب درهفته‌سوم بوندسلیگا با گلزنی هری‌کین فوق‌ستاره انگلیسی‌خود دو بر یک از سد الفرسبرگ گذشت. حالانکته‌جذاب‌این که در 100 پیروزی اخیر باواریایی‌ها در تمام مسابقات هری کین تو 97 مسابقه تاثیر گذاری مستقیم" گل یا پاس گل" داشته. امسال خیلی به توپ طلا نزدیک شده.
📊
عملکرد پشم ریزون هری کین در بایرن مونیخ:
98 مسابقه، 100 گل‌زده، 22 پاس گل، نمره 9.5.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/29698" target="_blank">📅 21:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29696">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fne21Tq2Ei2hEAnnijzp2cvytwwSZ52u2C7HKyKYEFS23AHE2QZWlbQqyMPRa-nNjz8JbBC4whmsRQlE07YvgQQ4B8_k3092rzK5EOyqN2nvRWfb-ZKUSZMNDNovfGHsfAJd1qFUEG5EhAxPn4cn47LUQy38H0DzgjzLeDN5vtN0dtcLSEXdietopmgqxvrbJcPCUj4r6QtOF04OlY3jBRYmpIXOGe4Cp9LMQy-tPcz-s40f_stg0dscvQ2UH9QeaqXF66KE__csur4DUm0LjspdCUQK6lK_V0rSK0zSfIctlkAt_juLwYVKGVGJeJcBo376SC7J3oBflVK2k1WaZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
درهفته‌چهارم‌لیگ‌جزیره؛ منچستریونایتدِ مایکل کرک دراولترافورد مقابل‌منچسترسیتی ده‌نفره یک‌ بر صفر بازی رو واگذارکرد؛ تک‌ گل این دیدار رو ارلینگ هالند برای سیتیزن‌ ها به ثمر رساند. سوپر سیو پشم ریزون دوناروما در دقیقه 90+6 مسابقه رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29696" target="_blank">📅 21:04 · 22 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
