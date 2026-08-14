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
<img src="https://cdn4.telesco.pe/file/Vtct5wxYmIQrzi7qus3NG2rIQnYQ-ge9PcgR1DTO9Q98lShMqILHygY7232Jo7oYwOEr3pab3uWTVwvFt83WSxNUvSIBNcJSnuYIwJQUuuYafXQkIGOXqjX2m1MbqF6UN5knUU1SIH32h9FoTJWD6cMa8cAx2l_DZxxRFb7Ye_2ZaAfacDKPCzTrm0w74Q6Eo7JtbzDvkztrAVYb5t96hjfFc1v-roHzPXx5gAUIdM468jBMgGDfL9a8mlFOymx5zJ29jj_2aSzZxiNtNgB7W7rUkXl1ZLV_Yv1vEbOHldEVdJ0KejZy1fzhnwVeiNQyWDqAUC-IFWwXFWvprPCS5g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 966K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-23 11:37:16</div>
<hr>

<div class="tg-post" id="msg-141603">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
شهباز شریف، میانجی‌گر ایران و آمریکا: هند سر عقل بیاید وگرنه پاسخ مستقیم می‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/alonews/141603" target="_blank">📅 11:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141602">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/804aec2cf3.mp4?token=diAKQm9ZH0maoY36SBgvElQhX_dwtrEkb9QotXiwFHva0dxx76bzzXe-G5qib-FPUmfF5AswHciTKTowTcdFKAilg0-ClQm_Z7ojfBLiS6UcD6mmmAik6pfPmmlNUlk_N6cT9M6WgLZtJwu245cj8p-fsXac5eKD5Q5tBUkCdj34utqJ-KlcsnK96eb--IZ6pjD0E5dj2AlMw3-KwcL2WC_YTHbVvcG1cVLvGwLXJLeJMEoPMX0bHVCJ-rLU-mpKSg1Rkn4evyPWnR3PvNtyniNLw-fJxLefup7p5W123GkgVeLyXycngMLZjoq3pDmDTNkKiwJ1F4sGzb3klAh8Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/804aec2cf3.mp4?token=diAKQm9ZH0maoY36SBgvElQhX_dwtrEkb9QotXiwFHva0dxx76bzzXe-G5qib-FPUmfF5AswHciTKTowTcdFKAilg0-ClQm_Z7ojfBLiS6UcD6mmmAik6pfPmmlNUlk_N6cT9M6WgLZtJwu245cj8p-fsXac5eKD5Q5tBUkCdj34utqJ-KlcsnK96eb--IZ6pjD0E5dj2AlMw3-KwcL2WC_YTHbVvcG1cVLvGwLXJLeJMEoPMX0bHVCJ-rLU-mpKSg1Rkn4evyPWnR3PvNtyniNLw-fJxLefup7p5W123GkgVeLyXycngMLZjoq3pDmDTNkKiwJ1F4sGzb3klAh8Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چین برای نخستین بار تصاویری از بمب‌افکن استراتژیک H-6N مسلح به موشک بالستیک هواپرتاب JL-1 با قابلیت حمل کلاهک هسته‌ای منتشر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/141602" target="_blank">📅 11:17 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141601">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
شرکت ردیابی کشتیرانی کپلر:
ترافیک دریایی در تنگه هرمز در اواخر هفته از میانگین ماهانه خود کمتر شده است
🔴
روز پنج‌شنبه تنها ۹ فروند کشتی از تنگه عبور کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/141601" target="_blank">📅 11:01 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141600">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
وزارت دفاع امارات متحده عربی اعلام کرده است که به سربازان جدید برای پیوستن به نیروهای زمینی نیاز دارد.
🔴
رسانه‌های عربی علت این اقدام را فرار بخشی از سربازان بخاطر ترس از درگیری با ایران معرفی می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/141600" target="_blank">📅 10:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141599">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
رویترز: ایالات متحده با توقف مذاکرات، محاصره دریایی ایران را به‌طور نامحدود ادامه خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/141599" target="_blank">📅 10:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141598">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbc7dcbf49.mp4?token=N8HAnSI7KQH7RPAoV9a5711RErXArYrxTG18C5hMfnBJqss3WC6bGoj6pbgDFCY2YARJHuMPIMQWmkBhpYkb02WJapGVvF-83Q1HSBGJcHGwi3el59qVio8L54y54wn7xwfnJ-n1XF9GSmcgJM2EfYVU6kILHGAr3Zs_EzwUBOLQcFwqBzszUxuXgbIEvTuPBamrRCgLe_X08d0YbEA52n6JPPxPePzVyyj41MCQAR-4aSpzYEdDd1YPGbPi2ZuPuenAaoVUK2TcPLh7bzI17EKOvFBlW7THzI_mFk9ponq0zDPgezl5KKInRmtIwx75nnPXe4Mc5ULkeyoLyQiSRIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbc7dcbf49.mp4?token=N8HAnSI7KQH7RPAoV9a5711RErXArYrxTG18C5hMfnBJqss3WC6bGoj6pbgDFCY2YARJHuMPIMQWmkBhpYkb02WJapGVvF-83Q1HSBGJcHGwi3el59qVio8L54y54wn7xwfnJ-n1XF9GSmcgJM2EfYVU6kILHGAr3Zs_EzwUBOLQcFwqBzszUxuXgbIEvTuPBamrRCgLe_X08d0YbEA52n6JPPxPePzVyyj41MCQAR-4aSpzYEdDd1YPGbPi2ZuPuenAaoVUK2TcPLh7bzI17EKOvFBlW7THzI_mFk9ponq0zDPgezl5KKInRmtIwx75nnPXe4Mc5ULkeyoLyQiSRIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسرای حوثی که توسط ارتش یمن اسیر شده اند به عربستان سعودی درود می‌فرستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/141598" target="_blank">📅 10:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141597">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
شرکت دولتی نفت ابوظبی (ADNOC) اعلام کرد دو فروند از کشتی‌های این شرکت امروز هنگام عبور از تنگه هرمز هدف حمله قرار گرفته‌اند.
🔴
‏ بر اساس این گزارش، احتمالاً نفتکش‌های متعلق به ADNOC با موشک هدف قرار گرفته شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/141597" target="_blank">📅 10:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141596">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
وزارت جنگ آمریکا: در حال بازبینی استراتژی هسته‌ای خود هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/141596" target="_blank">📅 10:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141595">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgCQZ1Ruez45yZfMcBiuBYy8AvDn7cdsIcE4EDZNECBbJssVqSrsTOFYPvD7Do9w2XqCgb4IsQXOvi6SQn7r1O1GnZH5LOHcrrHeUNt68-LvonmziN6NNDirvF-gnq14kD4PrgC57cH-7Mr8n6wGTxP8QkF2RBXPj-Ph9dFyXlKjgybLu6eFkYCi8nZ_wkTIXfFbyXarBtUvW7Gn4KntoDbJMWkvhg43ttPXRLs19is1myyRIziKLiI4EtrJXcExZ_T4TGEUy4VygsiGtiFHk6I4YzLV_-7lVhTjMF8lQ5zb8ta92_NJM3J3oX9CYrjOJS1_fTz9zUQr8o5mAIJU9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشک دیک چینی، معاون پیشین رئیس‌جمهور آمریکا، نسبت به وضعیت جسمی ترامپ ابراز تردید کرد و گفت تورم پاهای او می‌تواند نشانه یک مشکل حاد باشد.
🔴
به گفته او، تشخیص «نارسایی مزمن وریدی» با گزارش پزشکی قبلی ترامپ که اشاره‌ای به تورم نداشت، همخوانی ندارد و همین تناقض احتمال بروز ناگهانی مشکل را تقویت می‌کند.
🔴
سلامت ترامپ حالا دوباره به یکی از موضوعات بحث‌برانگیز سیاست آمریکا تبدیل شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/141595" target="_blank">📅 09:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141594">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
دیدار محمد بن سلمان با فرمانده سنتکام
🔴
طبق گزارش خبرگزاری عربستان، در این دیدار درباره اوضاع منطقه‌ای و تلاش‌های صورت گرفته برای کاهش تشدید تنش و تقویت امنیت و ثبات در منطقه گفت‌وگو شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/141594" target="_blank">📅 09:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141593">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
رائفی پور: ماهم باید یه ارز دیجیتال مخصوص کشور های اسلامی بسازیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/141593" target="_blank">📅 09:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141592">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvixxSZFYSoD8zAVgLAGHcWXmZk_lCNMiaNYczLN0t0Pr9In2WDVNvycEyPU4H8C8xbVjtjAJvQhHUa1swuF3MVmZmnne8VAdVNBplRSjppBjBARZOBxsp_cBJ76UwND0WEiAZ166qZd-sRFu6FFr5e-peyrowgQfMFl6dTqkSNMS_VfmEyXyVjYzamigl5Jranr9V4wWiDoclHPjNJ8CFxxsaecA734i6NzYZoqrmo05g8H0vr--olWDipxjnJQfo2vo8jV-O7_n-jm1UsX8MEGXyGHHgo6aMnyLPGBXcqxJN_VgVOOKkTZYeRMCS3Q6YnjMMjXgWC3YvAshlZlOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تلگرام ۱۳ ساله شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/141592" target="_blank">📅 09:27 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141591">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4970a84a03.mp4?token=je5I7694mngec6BGiemkx2RNTS86nl8YFEtyMEOi8J1Fuw2Gzad6iuyqjLYPeCYBpFTOo5bY_jwxIrrn3PQCPsduXHvqD_zSdT5GJHapia6zud5oYxATlF1lp-vz4WjqrwGtuatIEoGQeO0U7snxTIXD5Wbo4Fs7wRFVHXqoyf8LmHPFbliZ5QMRMR9NkYkXrzVJ9CMLYniGIBkexyD1t9I13Jg8Jn-ougBadjiWwZoVsgV8urGT_QLwwo0ZYmMd8yJd4xix_Y79yX_mSk0m738dJlzEIOocFM_NQTC5xZ5FDqZ_6FKC6oLrizXIhvzYMjqtRfVHlEjjF0-XYuHqdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4970a84a03.mp4?token=je5I7694mngec6BGiemkx2RNTS86nl8YFEtyMEOi8J1Fuw2Gzad6iuyqjLYPeCYBpFTOo5bY_jwxIrrn3PQCPsduXHvqD_zSdT5GJHapia6zud5oYxATlF1lp-vz4WjqrwGtuatIEoGQeO0U7snxTIXD5Wbo4Fs7wRFVHXqoyf8LmHPFbliZ5QMRMR9NkYkXrzVJ9CMLYniGIBkexyD1t9I13Jg8Jn-ougBadjiWwZoVsgV8urGT_QLwwo0ZYmMd8yJd4xix_Y79yX_mSk0m738dJlzEIOocFM_NQTC5xZ5FDqZ_6FKC6oLrizXIhvzYMjqtRfVHlEjjF0-XYuHqdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهد هواپیماهای سوخت‌رسان آمریکا این هفته دوباره به پایگاه هوایی «الظفره» در امارات بازگشته‌اند.
🔴
بر اساس این تصاویر، از ۱۰ اوت دست‌کم چهار فروند هواپیمای سوخت‌رسان در این پایگاه مستقر بوده‌اند؛ تحرکی که می‌تواند نشانه افزایش دوباره ظرفیت پشتیبانی هوایی آمریکا در منطقه باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/141591" target="_blank">📅 09:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141588">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2b327ec33.mp4?token=eQb9c1KZ6VlyiNOZVkfBKNwDh8biE6I7cIfJN2kLOpL5WJh7WPReI9_lJIxf3uYQkc_kGvwNP67OuUoi4X_0HJbROtt_wL3B_nf0N1oBwQAUvO62R7ZA013KPrwyNgNar2FrE4odgzdHLVfeY5wmiGl4LDgk35usfPwr-2Zbx2YbopmkIicO3pK-C8P22iAZeXkmro6xXhdwVmuD0BydqjVi3GDpIOnkv8GZxiQpewoSlW-4CGPd2l6fWkLNBGDPDomt0hgfrUjMOA5mZJmvEoRCnn213ambHrcNvySH6UpKcT2MkxyryA9g89DEA795rWRENbb7GHau8M-yEv_WQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2b327ec33.mp4?token=eQb9c1KZ6VlyiNOZVkfBKNwDh8biE6I7cIfJN2kLOpL5WJh7WPReI9_lJIxf3uYQkc_kGvwNP67OuUoi4X_0HJbROtt_wL3B_nf0N1oBwQAUvO62R7ZA013KPrwyNgNar2FrE4odgzdHLVfeY5wmiGl4LDgk35usfPwr-2Zbx2YbopmkIicO3pK-C8P22iAZeXkmro6xXhdwVmuD0BydqjVi3GDpIOnkv8GZxiQpewoSlW-4CGPd2l6fWkLNBGDPDomt0hgfrUjMOA5mZJmvEoRCnn213ambHrcNvySH6UpKcT2MkxyryA9g89DEA795rWRENbb7GHau8M-yEv_WQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلم‌های اضافی دیشب از اربیل، کردستان عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/141588" target="_blank">📅 09:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141587">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
وزیر خزانه داری آمریکا: در هفته آینده منتظر اعلام خبرهای بیشتری درباره ایران باشید؛ ما اقداماتی را اعمال خواهیم کرد که در تاریخ انزوای اقتصادی یک کشور تاکنون سابقه نداشته
🔴
این اقدامات ترکیبی از انزوای اقتصادی در سطحی خواهد بود که جهان تاکنون مشابه آن را ندیده و همچنین محاصره دریایی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/141587" target="_blank">📅 09:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141586">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
سنتکام: ناو آبراهام لینکلن با وجود ۲۶۰ روز حضور در دریا، یکی از بالاترین نرخ‌های تمدید خدمت را دارد.
🔴
سنتکام اعلام کرد خدمه این ناو با ۸۴.۴ درصد تمدید خدمت، ۱۰ هزار سورتی پرواز و مصرف ۱.۵ میلیون پوند مهمات همچنان پایدار و مصمم هستند. هیچ نظامی روی این ناو جان نباخته و ملوانی که ۳ اوت به دریا افتاد، سریعاً نجات یافت. سنتکام گزارش‌های منتشرشده درباره شرایط ناو را «گزارش‌دهی نادرست گسترده» خواند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/141586" target="_blank">📅 09:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141585">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1fc5bfffff.mp4?token=n2wb2TY-c1B7UEKFBlCrHmpuvjoiG6WUogJ0o6acUdf6w1t0qOBElytEtyJXOU9Wu67ottuE4AvzrQuLTqRUJgP8w0MglUoK9R9uJ2_NTL0FVJ2wTLgcPGDkQmD2gskk0-ev9AI6F_AzaTkz8qEQrerVI6hHkVmPxiYVxdMJlTVoT_h0gy78DQVxRChK0xjz50KfpAeoPAWH4-ciKWOYHtXJFELuxZRLCl_lIt-fItYdgjgjHEH5iI5WP1q9lZKa7E-9aP6kiuKbbwjiiE8d-AXho7Nwq0wcPseh2uVjF8ca6q6FDhrek083NsdngAGkk8u7etN55nfriHEhaxJ9Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1fc5bfffff.mp4?token=n2wb2TY-c1B7UEKFBlCrHmpuvjoiG6WUogJ0o6acUdf6w1t0qOBElytEtyJXOU9Wu67ottuE4AvzrQuLTqRUJgP8w0MglUoK9R9uJ2_NTL0FVJ2wTLgcPGDkQmD2gskk0-ev9AI6F_AzaTkz8qEQrerVI6hHkVmPxiYVxdMJlTVoT_h0gy78DQVxRChK0xjz50KfpAeoPAWH4-ciKWOYHtXJFELuxZRLCl_lIt-fItYdgjgjHEH5iI5WP1q9lZKa7E-9aP6kiuKbbwjiiE8d-AXho7Nwq0wcPseh2uVjF8ca6q6FDhrek083NsdngAGkk8u7etN55nfriHEhaxJ9Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رهگیری پهپاد شاهد-۱۳۶ در اربیل، کردستان عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/141585" target="_blank">📅 09:01 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141584">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
الجزیره: در پی گزارش‌هایی از کمبود غذا، خرابی سیستم‌های لوله‌کشی و بحران‌های سلامت روان در میان کارکنان ناو آبراهام لینکلن، اعضای دموکرات کنگره آمریکا خواستار شفاف‌سازی در مورد وضعیت این ناو شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/141584" target="_blank">📅 08:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141583">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b62202eee.mp4?token=edQ7Q1MZLfFoNNXMULy4wgveYpEK9Q1puRJo-xnLtyCNIqJ3CjP5FWQ3iG2w_jICH_VgDhYvNn9_50FIJMcM0-uTXiYZAR116_8mItdS-_AutcZSsNB6M6PsTCg2ESzXWqVc8LWRrFMCdRhtkR21ACvHxfRMi7R82H1IGwfuOfrEAeai-WAiyU2ff4289HdT7YpFoDZdgLslqLIWixG1MASnMXRu2K7VPNmkqXCEKQkt7FVcK-J7rCJuLoAmfL6tBaA5Wx7yyaEbnGJ9i25qBkYah50R0FRGR4vroEqy6ceZko6Mti-RzoALAw7CLMfst2J0YuL8Wz6bnHTwqlWMkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b62202eee.mp4?token=edQ7Q1MZLfFoNNXMULy4wgveYpEK9Q1puRJo-xnLtyCNIqJ3CjP5FWQ3iG2w_jICH_VgDhYvNn9_50FIJMcM0-uTXiYZAR116_8mItdS-_AutcZSsNB6M6PsTCg2ESzXWqVc8LWRrFMCdRhtkR21ACvHxfRMi7R82H1IGwfuOfrEAeai-WAiyU2ff4289HdT7YpFoDZdgLslqLIWixG1MASnMXRu2K7VPNmkqXCEKQkt7FVcK-J7rCJuLoAmfL6tBaA5Wx7yyaEbnGJ9i25qBkYah50R0FRGR4vroEqy6ceZko6Mti-RzoALAw7CLMfst2J0YuL8Wz6bnHTwqlWMkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات پهپادی شب گذشته به مواضع گروه های کرد در سلیمانیه عراق!
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/141583" target="_blank">📅 08:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141582">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
خبرنگار روزنامه جروزالم پست:
تیم هاوکینز، سخنگوی سنتکام به من گفت که گزارش‌ها درباره اینکه برد کوپر [فرمانده سنتکام] در جریان سفرش به اسرائیل گفته است که برای از سرگیری حملات علیه ایران تلاش می‌کند، کاملاً ساختگی هستند و صحت ندارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/141582" target="_blank">📅 08:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141581">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d86cbc5f3.mp4?token=eCCAKJJRldK1hh6VPaHMWNmeWlMJSji4M0BUX4ehCevYKBsfNcsnK1XFj0sv9w_x69t2nj_XVz1BRL1LzZ-ZOLCDHa27bC4Q-MZdyjLTKa71wR8Zb4_jeS5lRCxC0lvpwBNYuef1W-QTgLQzYh6B0QHRQr_ZLyLOTPCOQ9gigRrW5SZcuvnpardmxKE4ZgniANEg7gtUglhdnnilcyhg8KZSnLmxyD3mBOfLYgbqH6wSbK87ZaR0cxe-__3LxeXm-cl6CYFrmAZuG3u2x-GCLjTBf30IK7bot-1EggTwtWHQFWEfJ7H9HYMCb-XIxB1CucZbujSVude8DtbTEPPMsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d86cbc5f3.mp4?token=eCCAKJJRldK1hh6VPaHMWNmeWlMJSji4M0BUX4ehCevYKBsfNcsnK1XFj0sv9w_x69t2nj_XVz1BRL1LzZ-ZOLCDHa27bC4Q-MZdyjLTKa71wR8Zb4_jeS5lRCxC0lvpwBNYuef1W-QTgLQzYh6B0QHRQr_ZLyLOTPCOQ9gigRrW5SZcuvnpardmxKE4ZgniANEg7gtUglhdnnilcyhg8KZSnLmxyD3mBOfLYgbqH6wSbK87ZaR0cxe-__3LxeXm-cl6CYFrmAZuG3u2x-GCLjTBf30IK7bot-1EggTwtWHQFWEfJ7H9HYMCb-XIxB1CucZbujSVude8DtbTEPPMsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هشدار عضو کنگره آمریکا: ذخایر موشکی به‌طور خطرناکی کاهش یافته است
🔴
راجا کریشنامورتی: گزارش‌ها می‌گویند ذخایر موشک‌های دوربرد ATACMS و همچنین موشک‌های تاماهاوک رو به اتمام است. از سوی دیگر، ذخایر رهگیرهای SM-3، پاتریوت و THAAD نیز به‌شدت کاهش یافته؛ سامانه‌هایی که برای مقابله با موشک‌های بالستیک حیاتی هستند.
🔴
در نتیجه، قدرت بازدارندگی آمریکا کاهش یافته و این وضعیت می‌تواند دشمنانی مانند چین و روسیه را به اقدامات تهاجمی‌تر ترغیب کند.
🔴
آنها میزان ذخایر مهمات آمریکا را زیر نظر دارند و کاهش خطرناک این ذخایر، آمریکا را در موقعیت آسیب‌پذیری قرار می‌دهد."
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/141581" target="_blank">📅 08:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141580">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAtMzluOZU6dvuLSTaPjGG_HeIfZYOeAigYUioQsrnlrkvJN0EX-kiJt6s7gMTM6rEpag07Oww530wnzil_hI0xRAXmp33k-M4NiJZN_710sX4x6fG_5Z3yQPqHI8IQbgUae43_JdXzpYsMjbm6xcsoRhqAyp-0dMM_ksno1ytqeDstyXvSSn9wK0H7sWPDt7uXOG76p8FJkbvWM0TSUAvRf4lkBfoBMGXb2hwZob1PQMZRh48PmqbuTTIEKENnxcG3snfps1EOHWHLdRrhDDERvxaRWh3TFbtLY9Mg1hahSHDWlVVOgqknqB9i2JJA1kKdJgYJHivr3nvXrrHISHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سوتی عجیب شبکه خبر
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/141580" target="_blank">📅 08:37 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141579">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bcc1ba8a9.mp4?token=qBe04Qgdr5HCqPpYy2Yd4S9qtr8swB_8iFUC7gqRWsAt-SLf2fwhFILv91fxF7kJWfsWF0uuLAkfepu_NPl1M8VmRdZxbyenMLflAUka3UORw3aclJdNoPCQal3bmmUwRpmjyaenmF2hqjQ_4JrcgMIjN9iHtBZmi6OH_WUbnpPmAa-q1fhp4pmZ4PfT3yrxZ5FifzrrUs5rNiUr69OcFIBzqGRmo8XZ3asO9iBoD3Vnx1JNcRdjL-MyAwty3AkaouoJLgzVyQ4g4aoZDgm3-vW4xQLkSwG-UEou3_f_5PCDyOPlBNrqtdFsE0hnXaf-bTIMoeVIXTEXKUt6JHGL_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bcc1ba8a9.mp4?token=qBe04Qgdr5HCqPpYy2Yd4S9qtr8swB_8iFUC7gqRWsAt-SLf2fwhFILv91fxF7kJWfsWF0uuLAkfepu_NPl1M8VmRdZxbyenMLflAUka3UORw3aclJdNoPCQal3bmmUwRpmjyaenmF2hqjQ_4JrcgMIjN9iHtBZmi6OH_WUbnpPmAa-q1fhp4pmZ4PfT3yrxZ5FifzrrUs5rNiUr69OcFIBzqGRmo8XZ3asO9iBoD3Vnx1JNcRdjL-MyAwty3AkaouoJLgzVyQ4g4aoZDgm3-vW4xQLkSwG-UEou3_f_5PCDyOPlBNrqtdFsE0hnXaf-bTIMoeVIXTEXKUt6JHGL_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سقوط پهپاد روسی در خیابان‌های کی‌یف پایتخت اوکراین
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/alonews/141579" target="_blank">📅 08:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141577">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f61ac0c79f.mp4?token=EmJBZnQma_hNkCnoe7Q4DZZ4rK_jTyCL4T8ZV2m5SFb5FmodFTzbRJD5TZ9o-eQNAAtU_yqGqrvQ333ux1Hsvgdx0YqvjvZ1qLJyNPvmRsHUxk2EQr5x-FEW_S9u8endVTNVaYhD3sxU04ItGXGCenqy5XLrE9-sHbBnvpc5bQ3grkgB7uwkv1--QVIrdm_u9v6yCe0VRGjRzZOp1d3-zHn9RZIFVedpSgtnTPW-fgW1pnfom5xKXgHP2X-qftTMoh7yA5tZ7c3JiB6x8ghrw9ul_L22n8w4kfoXC9TKj0bkyiLhBybKeGERrQLDWraqB9Q_2NjxqryzYpXnLeMzKA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f61ac0c79f.mp4?token=EmJBZnQma_hNkCnoe7Q4DZZ4rK_jTyCL4T8ZV2m5SFb5FmodFTzbRJD5TZ9o-eQNAAtU_yqGqrvQ333ux1Hsvgdx0YqvjvZ1qLJyNPvmRsHUxk2EQr5x-FEW_S9u8endVTNVaYhD3sxU04ItGXGCenqy5XLrE9-sHbBnvpc5bQ3grkgB7uwkv1--QVIrdm_u9v6yCe0VRGjRzZOp1d3-zHn9RZIFVedpSgtnTPW-fgW1pnfom5xKXgHP2X-qftTMoh7yA5tZ7c3JiB6x8ghrw9ul_L22n8w4kfoXC9TKj0bkyiLhBybKeGERrQLDWraqB9Q_2NjxqryzYpXnLeMzKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امشب تو صحن امام رضا مردم داشتن با چوب عزاداری میکردن
اما چند دقیقه بعد بین یه هیئت یزدی و تبریزی دعوا شد!
بعدشم شروع کردن با همون چوبا همدیگرو کتک میزدن و پرت میکردن تو سر و کله همدیگه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/141577" target="_blank">📅 02:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141575">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b7_B3HBVFNUUEWaUt8qAJa7SvLbxtpgqiBdVbUez9XCuw2qYOIcB3id2_bgB2mxXBUFCu0-vNEIhVvIx95zQm847gIW1dkVbLdXfsaSVcLRAJY-7QpmNVGcoanWbeFpHmnfwneleegU3b9mR_zqFyCj_vmf7DNgF3zjKIselKHeSnVEtFuwtPZqAOLjnGOHHz6IEfihyUzmjqSu81j7jj0jHeeF0sHbNb0sQtzUNWMkX1KgQRrM5RENqXy2TXII-LHr6ENT2rwim7whUlOn-1bjOOkYEChPmtL0OEpMI_eJFd7IpEddjSC994SEeCKAriA0y_BX2wwacUgQbp7nvFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KjH2ru6G3mNTDTawa-I8a75qLEAYeKdDn66mn27jLTZgPCvGmrEBm-QtmWkM3omjgcDt46bqLzLUDTE6Ytqf8m31G2g0Cj4yCMEkts8ZygZNC_lKpMpX9GCO_ZyZGr0r_91KqKu7IjoDzaweB1Hk5-2YyE0yPx6pgIYzekKQrWd_xRB1DG-vp_cEltVZTkL_uAlgJXlgOJIli-B0oua7Tb__2KHVWxyyZginn6VxAlDDr1zQKfQZPGT15WxYfBMGQNvWmJue1myzvSab30B_Xsx-7010PUnp6FJ9zFdUFuJKWcKziwtWFhAtsl7FTEF47LvYd8hC7EkvKMEpoUmYpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
صدا و سیما به دولت، خوارج گفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/141575" target="_blank">📅 02:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141574">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BAR0-nHaU_wKpIrQB_9V7JMOn84OMPdXw3zxSX_Q6fqdM4fqor-DNH_EATXzqa6bMM-G5E_cELSg40slR0ko-Y1chsjsqQFvklc7ykCYPcxvI2d1MZqsJCVBc9pRbAsfZ-TcIpUMncPnVNgiuZjE8aN4J-bbA5qejNy1BZenWhQPH5joSm-jiD7GCclBi6ovuZQ2bPrVp-oCeXuP_Wdx8Ccvv5BiG4G_-B1ObjPJFbD0poRPoEGuAzJjRfhLXcdRFpC2R_G8co37uqX5CQ-WXfpaqzElw501jI8N15sbFKmiAOpzw0pEbwlifBVFlTwrFa5COdoDJKSs7WGHW2OehA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
7پالایشگاه از 10پالایشگاه اصلی ایران قبل انقلاب ساخته شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/141574" target="_blank">📅 01:36 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141573">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
تو اندیمشک و دزفول زلزله اومد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/141573" target="_blank">📅 01:09 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141572">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82036588a4.mp4?token=S08FXNmz1rmrlEXTqzR4oQFJOpFi7LtycHEfSvx2yyTWUVydHpZfmiDU-KrDE7atKPPl4G0y3vt7Tg8D76jBCYCTtdH9ETkfb_Vc4fHrS6IhDI8-kPlpqlvpb-2-Lpf0dQQySeLGG1RmbHKDLf_4IU_cAWvijyutNvhhsvkz70McyOm_eCG-hgMeKAuWjT8hCiJdWetjhNFDs32hTrqg1jbShCg8zIms5Ixc-dXmqIjg5Neus0Fx2E1HkW1qNsjzRjJMixGnTefn-eHFinSfPLkHkTHzwmTKB6lmmv-A69pWCVx4kO5uf1qKPvfcAAFhz9svhP7Ub6ccpSI8zFsg6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82036588a4.mp4?token=S08FXNmz1rmrlEXTqzR4oQFJOpFi7LtycHEfSvx2yyTWUVydHpZfmiDU-KrDE7atKPPl4G0y3vt7Tg8D76jBCYCTtdH9ETkfb_Vc4fHrS6IhDI8-kPlpqlvpb-2-Lpf0dQQySeLGG1RmbHKDLf_4IU_cAWvijyutNvhhsvkz70McyOm_eCG-hgMeKAuWjT8hCiJdWetjhNFDs32hTrqg1jbShCg8zIms5Ixc-dXmqIjg5Neus0Fx2E1HkW1qNsjzRjJMixGnTefn-eHFinSfPLkHkTHzwmTKB6lmmv-A69pWCVx4kO5uf1qKPvfcAAFhz9svhP7Ub6ccpSI8zFsg6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیش بینی عجیب مرحوم روح الله زم
🔴
یه سناریو طراحی شده که آمریکا به ایران حمله کنه و ایران هم تو منطقه بزنه پدر آمریکا و عربا رو دربیاره و قدرت خودش تو منطقه تثبیت بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/alonews/141572" target="_blank">📅 00:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141571">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRKBIZOxQFkA7oc_KGCZM6QbqGHOz0m9KS8yFkFxK6uJur0ChnfoWUEcAavVa9l7St9bGf4Z36vS9Yrz3Z2SfpmA7viUiU1HQ5kLkZD2qX5NctAbTdvB25FUQ3IJg2fJpxT2LaDu7iWyk9BTg1_Anq6CQw_midgL3qFqwNafKKw9oWUwV0xzhGWYSifwZDqm108zGke8jG4ulHdh43zE8Nc4mGh-IwnkUyQ2FjtRiQfkIv7ueaz1IUAs8ragoXAqHaH3lsJgc6tt0sfjvVt9T8kRHESp7Duna6VG8-gLKmfL3lVX0Lc1lXDdRfVQt5y5R6BHQY5qxGf5DZO9geinSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: دو مرجع مهم تصمیم گیر در خصوص بنزین اختلاف نظر دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/141571" target="_blank">📅 00:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141570">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be651093e6.mp4?token=GHK29jHfPNGCjgt-IC09S063gevyHHI1BjAzuY6TTlTu1KB_IySPkJD2NFWF7ul4m4S3H-gzi4Ak_6ateibqc3zyAk3UNrJkvdXKEObsPHCPYUUiT1o8FWx8AN5RXZ4H4R2O5RZuS4XtwXT2cQXwHY97umfWtR59IMHjZFYpk6WUH_-fgO9Nbxq0QRwBEPt90uDjnHt0vzWsKAItVHMpwp8hwN3BY7a9M8LQ1b5HAanVprj34tfV1ISEhcEYOo1nA6IDJk3QMx_ihCjAzImIwTpk_9Q8_tY3niWJ1OlFM0x8Y7nIqDPcVcCOo3aZmI11qJX2_rwA3krB-ssy8sRAnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be651093e6.mp4?token=GHK29jHfPNGCjgt-IC09S063gevyHHI1BjAzuY6TTlTu1KB_IySPkJD2NFWF7ul4m4S3H-gzi4Ak_6ateibqc3zyAk3UNrJkvdXKEObsPHCPYUUiT1o8FWx8AN5RXZ4H4R2O5RZuS4XtwXT2cQXwHY97umfWtR59IMHjZFYpk6WUH_-fgO9Nbxq0QRwBEPt90uDjnHt0vzWsKAItVHMpwp8hwN3BY7a9M8LQ1b5HAanVprj34tfV1ISEhcEYOo1nA6IDJk3QMx_ihCjAzImIwTpk_9Q8_tY3niWJ1OlFM0x8Y7nIqDPcVcCOo3aZmI11qJX2_rwA3krB-ssy8sRAnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس در مورد ایران:
قیمت نفت امروز در مقایسه با روزهای اولیه درگیری به شدت کاهش یافته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/alonews/141570" target="_blank">📅 00:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141569">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
سی‌ان‌ان:
مشکلات ترامپ در رابطه با ایران در حال تشدید است و در بحبوحه پیچیدگی‌های فزاینده درباره جنگ و تحولات مرتبط با آن، وضعیت دشوارتر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/alonews/141569" target="_blank">📅 00:37 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141568">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFDLSZyXs4d1Hsfh6om0MGJyADZO4MxDoR5RrbaRjnC36_9zVrbTyNWo8IPxJZ8_41nOK4qvdqlazVSAertVsRzDeAp51BhbyMtiKPrCye4niZSaFmnkx6siUDg-0a_6v14Fp-OHvMZOu38S6SeMcQ9rsTf2DJLCGRvKaxJUDZz1BwUnmiNgGLBILNE__pFEVBv1HWcvEGi8CbekpHxc4iHuDJkpofi1j4tJeORP3MefzcP4og-uP41x8hzqIwkn2I3eWq1-xrqKp0f0z1pp_DTPj8mAu1bNyDJRRj8poOERlRjMlhYZeazYcSj3sD9VX-NiwoYOovadSqtXXrZh0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه رستوران توی کیش، تمام نوشیدنی هارو فقط برای خانما رایگان کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/141568" target="_blank">📅 00:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141567">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
معاون رئیس جمهور آمریکا: من کاملاً مطمئن هستم که این بحران با تقویت موضع آمریکا و جلوگیری از دستیابی ایران به سلاح هسته ای پایان خواهد یافت
🔴
بازگرداندن ثبات به تنگه هرمز، ثبات قیمت نفت و گاز را برای مردم آمریکا تضمین خواهد کرد.
🔴
مشکل این است که ایرانی‌ها وعده‌هایی می‌دهند که به آنها عمل نمی‌کنند و توافقاتی می‌کنند که بعداً از انجام آنها سر باز می‌زنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/141567" target="_blank">📅 23:56 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141566">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
جروزالم پست: مقامات دفاعی اسرائیل از سرعت بازیابی توان نظامی ایران پس از جنگ، شوکه شدند. ارتش اسرائیل اکنون شاهد تحولی سریع در قابلیت‌های تولید موشک‌های بالستیک ایران است.
🔴
بر اساس این گزارش، خسارت واردشده به صنایع دفاعی ایران به جای چند سال، تنها فعالیت این بخش را برای چند ماه عقب انداخته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/141566" target="_blank">📅 23:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141565">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d92209cf4a.mp4?token=ubZQFzu7QVl7ovb5_k-I4FtzEY0cxTW2t2OIAIoUXVLkc7Qo0UzMfD2c72IkhLI4S1XSL_uXz6ocv2QPTdXnAUDcEUaM8B1GwD65CkHE7t-mdDSi8d1wNGj7xgujSaXAl3rAYkqdY2iwXyEsArZPeYeIvtCn0f1VPgzCd04j6w8-3_0MiN4AtKosdUMmQ73yrPRgW8Raz3t1RzfTOmjQNQW7m27_69PSQUcrHiEZxZGMT7QljMV9M3x5AJXAcfvEhq4sWXxDuDuS2p7Rh-56y1ye7TWACCo8gQDOXOjax5HWfZQ4lJhNipTAbfWgF1E6KigKHa9o83qwDoPNgaGSJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d92209cf4a.mp4?token=ubZQFzu7QVl7ovb5_k-I4FtzEY0cxTW2t2OIAIoUXVLkc7Qo0UzMfD2c72IkhLI4S1XSL_uXz6ocv2QPTdXnAUDcEUaM8B1GwD65CkHE7t-mdDSi8d1wNGj7xgujSaXAl3rAYkqdY2iwXyEsArZPeYeIvtCn0f1VPgzCd04j6w8-3_0MiN4AtKosdUMmQ73yrPRgW8Raz3t1RzfTOmjQNQW7m27_69PSQUcrHiEZxZGMT7QljMV9M3x5AJXAcfvEhq4sWXxDuDuS2p7Rh-56y1ye7TWACCo8gQDOXOjax5HWfZQ4lJhNipTAbfWgF1E6KigKHa9o83qwDoPNgaGSJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماجرای خبر بنزین 87 هزارتومانی و سپس عقب نشینی دولت به زبان ساده از مهران مدیری در سریال هیولا
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/141565" target="_blank">📅 23:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141564">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
جهت رزرو تبلیغات در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/141564" target="_blank">📅 23:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141563">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f229500ca2.mp4?token=ikxxCXXAwZ507opukdCrAmoy1mwoc5IC6nTYiyNBw2av3CAJhjo6La4gO8pLRM3p0OHpHF9gwjkE2QAnahplX1exkKTO1nxCbtHEzQLlaE7fK6xcS5yWpiIss-ZLZgAqAA2UeIa7cPeBLX7EytCJJlL9mKogojtwDcUf4adhyND9XEnE_Tr8dasjzxLQV-u2arxeMeMrDYf9rov7t35YufocJt8hp9Xg9TSedeyqsHUKj4pHcEvwHT14OJ47rCsKcMXbupVnAp5QFF0v0IwqixXbEW_XufRWGg92-JoczembY8MsloOyulB3YIRjm-uvKupXdynVCgFaPgbFsKe6ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f229500ca2.mp4?token=ikxxCXXAwZ507opukdCrAmoy1mwoc5IC6nTYiyNBw2av3CAJhjo6La4gO8pLRM3p0OHpHF9gwjkE2QAnahplX1exkKTO1nxCbtHEzQLlaE7fK6xcS5yWpiIss-ZLZgAqAA2UeIa7cPeBLX7EytCJJlL9mKogojtwDcUf4adhyND9XEnE_Tr8dasjzxLQV-u2arxeMeMrDYf9rov7t35YufocJt8hp9Xg9TSedeyqsHUKj4pHcEvwHT14OJ47rCsKcMXbupVnAp5QFF0v0IwqixXbEW_XufRWGg92-JoczembY8MsloOyulB3YIRjm-uvKupXdynVCgFaPgbFsKe6ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجاری در مرکز خرید عربلا پلازا در شهر جدید قاهره، جان حداقل سه نفر را گرفته و چندین نفر دیگر زخمی شده‌اند.
🔴
وزارت کشور مصر اعلام کرد که یک سیلندر هلیوم در داخل یک مغازه فروش هدایا در طبقه همکف منفجر شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/alonews/141563" target="_blank">📅 23:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141562">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ان‌بی‌سی: خستگی جنگ با ایران به ارتش آمریکا رسیده است
🔴
ان‌بی‌سی گزارش داده فرماندهان ارتش آمریکا نگرانی خود را درباره کاهش روحیه و فرسودگی نیروهایی مطرح کرده‌اند که ماه‌ها برای پشتیبانی از جنگ با ایران در منطقه مستقر بوده‌اند.
🔴
این هشدارها به پنتاگون و کاخ سفید منتقل شده و نشان می‌دهد طولانی‌شدن مأموریت‌ها، علاوه بر فشار تسلیحاتی و لجستیکی، به مسئله نیروی انسانی و توان ادامه حضور نظامی آمریکا نیز تبدیل شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/141562" target="_blank">📅 23:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141561">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
رئیس سازمان بهینه‌سازی: مصرف روزانۀ بنزین ۱۳۵ میلیون لیتر است
🔴
تولید داخلی ما کمی بیشتر از ۱۲۰ میلیون لیتر است و میزان واردات تقریبا ۱۴ میلیون لیتر است. یکی از اهداف دولت این است که واردات صفر شود و پول آن به اولویت‌های بالاتر مثل دارو و کالاهای اساسی تخصیص داده شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/141561" target="_blank">📅 22:56 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141560">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k44aaIrtJSqJeubVRFOthOMEdkbZZIuetcR5P4A7TTw8t2a1OFtIl7Pv0-i7GdTaJoTA9-uQnuZ-8cJge2vPakVIvSUqsk5wHqTKFIJMhSJKmBcU0d5KVKeBdK3h34FNdB8TBYUmRLpT190rv-0H0tO9zsaUg3qscq9N2PYCBedLDj28MZNhJxxqZrLzMtUOO655vPphsXlBfJN6deGMX2DIXnDn-L3jTRERiKd_bvB2JIbIIARHg4AtUd5nwGHXyRFPxKm1vp_BRNDmvuVBa_K6LPNB2xk9k_LWwT7hFHUWxab3mtcr9A2VFiVD_Cbwjc7kQ69i5uTFpqo0K5KudA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه‌ اجتماعی اینستاگرام هویت بصری خود را تغییر داد و از قلم جدیدی رونمایی کرد که ترکیبی از حروف متصل و چاپی است.
🔴
این اقدام، نخستین تغییر در نشان‌واره‌ نوشتاری این پلتفرم در ۱۰ سال گذشته به‌شمار می‌رود
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/141560" target="_blank">📅 22:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141556">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J4DB-h4C3plvKYQJ8yKlKrO3n9HD04K_SU6Gw5LDnK8plUFibCwZXS3omgZDG7YBYB4ZJTeoWvR-jsr9VqdHz63msZtbswqNRK6oF07KNoCOyfwmEshhdc7JIyyTFxVG_SyyKGRS2xTIMNek1ZxmWMLrKTiw17_hvLKeBgGEh659Jkv9F2arGGpTVpA_Bx_MDXTENG1xN8e6yLJn4Vop-gFV8r6O6H01MnaMr3sm9xR1AYlmJAhEcSBQms-NhrgDtM3IZogd66-ZzyouZpHZTDTN7pO43vLD4jXTyd4G9D2XzxylzGzwmUkUyIdPNzvfEMyrmJe4ij3S8nqB4QWIqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dtxQiQcKXDg2TddQC9fmDvLsJ2HJJQUXj8A8CWBd5tfgDu0zZqGTevCWOprYPx7pXvC_AvajNt7B_4_gWTGqX5G2UtS6fma3nBVioq4q8N75KDdIzf9leYenFkOP9d1lOA_TDnyTsb5a-zedFthwYgpuO9t38CeLqh_aePf1rSRamUZaJm-FE2rTzH9xIufix3_WPsbJnpJoW11pLxaPvBdUUO55S2GgQ4ViCwR2I2nAiiTTrynZ78MyWy53q3WbwUGN4Z_ipu1Eb_8vUjuuwf1d4HTWMzuutE07Q08OJ5zmbQdX0S7-DjujSOm5TrvMxZ4fCkIusyPEH2UrkT9_pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VDFANl1iyj06Nwz8pE9SSde2XvVl0vlGNtTJLVW1OmTNf2mSAFtzxkqxKqNtm_CLal6yeB4s0Qebh6wz_axY5fWlJGol9eyYRInt0POWMOafqNLRH2GPayU5vC_pGw5Qe_v5hTuhYI7y0K0gVr2p2Co-1wSyLGCEetTxqJWxU4FGFwafKoI3nawJ0SpAYmcx4GFJ8PHcjhhHqh-rIK1ZpclHnB6fmJT3gGis3X-b7l-rbSY3rBTkfmbZ6MPRs7LItyJKLKw-Rm8AAjnqpx3Q77GOETKXTlxSrjPXoWBnmdjrBPFRs3dYV6wQeHJGYAUh-VA3Cj_IreUJ9cbXzPu7VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B4QOoxJxrVE-aURpJ6GzRod6MdNit5DSaoAjJtBEatWRqU0PeR6AQmb-E8mImgeNI6gkGb_--_TU6qjcpJpKOw6nQ6mMKfXB85U3R6yfI-ULnffGB-CYKBX-XmZxaWFn0nqoNFSQgC4w-fAyLRADEddciWuWgO0gqXN2VYhgvIqjpttAtRZoUN0n9NUpjWGLl2LWRQXF6MNyTHIGAxbjPM_PWPX-gLPIZp3BuB1iDlO5FAmikH5LzYQTunHzyPi6QzV9W7X7WWWdFhLeTdgJMVc7Z22ZqjyCzmPQ0vTADo4RDAPS4rO1hIFCtWawe3f_Dul2fizBOS7JW8InZ02Bjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
مشاهده کرم در غذای دانشجویان علوم پزشکی اصفهان/امروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/141556" target="_blank">📅 22:48 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141555">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5531921f69.mp4?token=MkEfZb2pTtSdH0alFVpHaGgiuWN7gQq_MtU-vICTc0OU3DegWfZWANU8-1yDS-eBeFSvhKUONXEgsX-V7XMOcmEwcuYLA7YHnLXepRRi44Hf6FGDoqzI_cLINS5HKAZSxpJ6nei-Y_FRnCi0PgF5N88b0BpCsy91UT0hIbRnOA8NeFhpyh97PmvxNfizHqK32HYXfP01js2upEGdwH8ZYcbtb5Xf-YC1bwtx1VA-t8E_vU5a7qIQ2nkB0Yp0P7T1kqTs7GuABR15mjgLjpLFlAycIkIVqj9xJKjL_YvJKNDWV0qOyk48atBzr8HTokzEdZomLQTOKSVzsQ3Ih6U1vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5531921f69.mp4?token=MkEfZb2pTtSdH0alFVpHaGgiuWN7gQq_MtU-vICTc0OU3DegWfZWANU8-1yDS-eBeFSvhKUONXEgsX-V7XMOcmEwcuYLA7YHnLXepRRi44Hf6FGDoqzI_cLINS5HKAZSxpJ6nei-Y_FRnCi0PgF5N88b0BpCsy91UT0hIbRnOA8NeFhpyh97PmvxNfizHqK32HYXfP01js2upEGdwH8ZYcbtb5Xf-YC1bwtx1VA-t8E_vU5a7qIQ2nkB0Yp0P7T1kqTs7GuABR15mjgLjpLFlAycIkIVqj9xJKjL_YvJKNDWV0qOyk48atBzr8HTokzEdZomLQTOKSVzsQ3Ih6U1vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سقاب اصفهانی
:
تغییر قیمت بنزین در کرمان به‌دلیل برخی بی‌تدبیری‌ها متوقف شد
🔴
رئیس‌جمهور تأکید کرد از اقداماتی که مردم را غافلگیر می‌کند پرهیز شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/141555" target="_blank">📅 22:35 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141554">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‏
👈
سقاب اصفهانی در شبکه خبر: به دلیل خسارات وارد شده در جنگ هم  دچار کمبود تولید در بنزین داریم هم در واردات بنزین دچار مشکل هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/141554" target="_blank">📅 22:31 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141553">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkPMab11iSH9Wnwis_rVvygi-Nd3JOhw6iTI4unn5JIchxenpQOHb9bs25R9gQP0RGh3tWlx9dM0aoeP4CB__W8UBjyjHroY7kCMTAgf1OsNsSMRF-FvH9BU-jQW9fr9ug1fRgbchNcFVZvVEU-QdgC_wfC1VZNOJUJhbhu8CZmbQhO5AfT6YgJV6_mvJQPJ75t71luhBvoRvCHccSJOWYGLyjWGRKYJSbbsJ6PcAAnR5NdNfC8ufdLHpQ7P08mtnSfLl13Cg77O4ShDuEqVUCKB0-ZztgZpaIFmp9XrRnDRhuwla-4ZRdfQ-KnQU-wI31rVuwQAmF_rLZn-cv_-OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مشاور قالیباف: با تصمیم سران قوا، گرانی بنزین منتفی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/141553" target="_blank">📅 22:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141552">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUt6RjSm_NF7ypjHnLaFpAMJTmSpwQPPQx7q6nsutUwduBuSRueKarZXfziod53VjwC9n5iazJQbBy0QUSH_Xwa0NW5mFa7t7txyfImRfNcD7_7e_jqRL7Rez57lWJAGORySDbB_oI_GKdQlLLlCrbJdvvNhN5GwwtY8Eerr3MAqx9IOBk1zftwbc0wqhfa3NUpJ6H7tjqtd_cfMB7pI_mBRW1DlZBgeNiKEIIiSg89422lkt3WnNI8GYGRBBkPJ1DRRO2JCabRBUY1GdLGz6Dsgkd9IQGEFAvNXtcyY7vaEr8O6sqXAp-ngjfphTkd4OnmhRMXsqKZ75i_9uiNkDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ، اعلام کرد که سیستم "de minimis" لغو شده است: امروز، پیروزی بزرگی در دادگاه تجارت بین‌المللی ایالات متحده به دست آوردیم، پیروزی‌ای در برابر یکی از ناجوانمردانه‌ترین معافیت‌ها در سیاست تجاری آمریکا، یعنی همان "de minimis" مشهور.
🔴
سال‌هاست که شرکت‌های حمل‌ونقل خارجی می‌توانستند بسته‌هایی به ارزش تا 800 دلار را بدون پرداخت عوارض و مالیات به کشور ما وارد کنند، و این امر، نظارت کمتری را به همراه داشت. این موضوع به یک راه فرار بزرگ برای فرار از پرداخت مالیات تبدیل شد و همچنین، کانالی بود که قاچاقچیان مواد مخدر، تولیدکنندگان کالاهای تقلبی و سایر جنایتکاران از آن برای وارد کردن محصولات خطرناک و غیرقانونی به آمریکا استفاده می‌کردند. آمارها بسیار تکان‌دهنده بودند.
🔴
تنها در سال 2024، سیستم "de minimis" حدود 10.8 میلیارد دلار از درآمد حاصل از مالیات بر واردات را از آمریکا سلب کرد، و بخش قابل توجهی از مواد مخدر و کالاهای تقلبی ضبط‌شده از طریق این کانال وارد شده بودند. بنابراین، ما آن را بستیم. با یک امضای قاطع - بدون استفاده از دستگاه امضا - این معافیت مضحک را لغو کردیم و باعث شد که کالاهای خارجی طبق قوانین عمل کنند. واردکنندگان شکایت کردند. امروز، آن‌ها شکست خوردند. دادگاه حکم کرد که رئیس‌جمهور اختیار قانونی برای لغو این "امتیاز" را داشته است.
🔴
اکنون، آمریکا امن‌تر است، کارگران ما بهتر محافظت می‌شوند، و میلیاردها دلار درآمد حاصل از مالیات بر واردات که قبلاً از این راه فرار می‌کرد، می‌تواند برای تأمین مالی ارتش بزرگ ما، کاهش مالیات، عدم مالیات بر انعام‌ها و عدم مالیات بر تأمین اجتماعی استفاده شود. سیاست تجاری "آمریکا اول" و اجرای قانون "آمریکا اول".
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/141552" target="_blank">📅 22:22 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141551">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3e60e3f4d.mp4?token=gpklsjwiWm8bXdybKC7ddYIqKIG9c5z8ZpmJuWh616ycRxuysvnZB1CCXxFgyvt7G-_tphK-f94N-xWQ1gSdqJDTNL4g7nkQ8KPfqVVA-4I--czW7414lEoTFbjZ506jE8yhyRtXduANZbgl2xj1LX-xi6V2BMtA_5d9F9I7qB-WGS0NLYn-FYxmUmIUsfd_ccFKlaAvOFHe7L7pwxyKNY68vzRDDQJugvCDrUaiIALZp092UJk8tvjzqV6P5eHj8fTdWT4FCMXS0SIV3gm_WRc7yBKWJ6ArNye8coin3qryU9JBS-6xukMkpvgMVV-wwXf6JQaOly74SDJWbr00_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3e60e3f4d.mp4?token=gpklsjwiWm8bXdybKC7ddYIqKIG9c5z8ZpmJuWh616ycRxuysvnZB1CCXxFgyvt7G-_tphK-f94N-xWQ1gSdqJDTNL4g7nkQ8KPfqVVA-4I--czW7414lEoTFbjZ506jE8yhyRtXduANZbgl2xj1LX-xi6V2BMtA_5d9F9I7qB-WGS0NLYn-FYxmUmIUsfd_ccFKlaAvOFHe7L7pwxyKNY68vzRDDQJugvCDrUaiIALZp092UJk8tvjzqV6P5eHj8fTdWT4FCMXS0SIV3gm_WRc7yBKWJ6ArNye8coin3qryU9JBS-6xukMkpvgMVV-wwXf6JQaOly74SDJWbr00_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خروج قطار از ریل در انگلیس
🔴
یک قطار مسافربری در حومه شهر «لویز» انگلیس از ریل خارج و واژگون شد.
🔴
به علت مسدود شدن درب‌های قطار حداقل ۴۰ مسافر درون قطار حبس شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/141551" target="_blank">📅 22:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141550">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNZgCnavOoQQV7agw2Eo38qOJ6_tC5TRLTv3GATqTWg9Ev_EglL36FXtatjtus1pyC2NL1EsDXsofHhvfgqToVEyUe6y1dn19HBb5qJYql2Ee2flJ4E5LFskmtr7SP2PjmBVpTVCg0EK4tAu-XqIrCWP79GGbWkYX5u_AHHkZs4eQMyYu8fX6JXamwSmqDHyLtNmq1WeIRXx03h9X-cPqf0fSNRECbieG6L7q42gvYAenbk7XXsG52Dj5qLlbwfpvrFYIgknDU0dtLEoxQL5454ckQmsjdoNkDF-Fvg0lgI3kbugU4rITwkT_7FX98u3c1PUkv8aJZGZyQs7m87jeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدار رئیس کمیسیون امنیت ملی به جولانی
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/141550" target="_blank">📅 22:13 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141549">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
ای ۲۴ نیوز: ترامپ و نتانیاهو از زمان دیدار در واشنگتن که به دو هفته قبل بازمی‌گردد، با یکدیگر صحبت نکرده‌اند
🔴
این قطع ارتباط در شرایطی رخ می‌دهد که ترامپ همچنان در حال بررسی گزینه‌های خود درباره ایران است
🔴
در عوض نتانیاهو تماس‌های مکرری با جرد کوشنر، داماد ترامپ داشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/141549" target="_blank">📅 22:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141548">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ed9c73d19.mp4?token=Alab6BBXCKCQcZyAvJftIrffGPh6ZEBbbeC8UYo1gcFMKYC58QVcBOyNVYGQHwBieONzcGgtyE8mBR3j2BfPhQ8cwg3V6wzDjulLCgtTWbRSwQoILkAU2s5ljnDhqLMzX59cUslAJA0aUDG26VHa1ioEJ0tooLAqQGf8rZ7mVIIYROsF3YqjZYRbpOvj0B3CJLpoFuOMxB9Aj02dOAv9Q-mi3Cg2-2Xx_bnTUl06QMUq_H7qlogZghxJtDlP8wjNJ1Br59i1nG_Lbv5MwkR2BYdCY3RcJUbeveqoc48fMB71VmgjaNesqZPFkK3OHh6JtFN7l3J4nIDB1hU7Q3pJ6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ed9c73d19.mp4?token=Alab6BBXCKCQcZyAvJftIrffGPh6ZEBbbeC8UYo1gcFMKYC58QVcBOyNVYGQHwBieONzcGgtyE8mBR3j2BfPhQ8cwg3V6wzDjulLCgtTWbRSwQoILkAU2s5ljnDhqLMzX59cUslAJA0aUDG26VHa1ioEJ0tooLAqQGf8rZ7mVIIYROsF3YqjZYRbpOvj0B3CJLpoFuOMxB9Aj02dOAv9Q-mi3Cg2-2Xx_bnTUl06QMUq_H7qlogZghxJtDlP8wjNJ1Br59i1nG_Lbv5MwkR2BYdCY3RcJUbeveqoc48fMB71VmgjaNesqZPFkK3OHh6JtFN7l3J4nIDB1hU7Q3pJ6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کیث کلوگ، نماینده سابق ترامپ در امور اوکراین: ترامپ عملکرد خیلی خوبی داشته است. مشکل اینجاست که از نظر ایران، این آنها هستند که دارند پیروز می‌شوند، نه ما، بلکه در ذهن خودشان، آنها دارند این کار را انجام می‌دهند.
🔴
و فکر می‌کنم از این به بعد، باید ترکیبی از فشار اقتصادی و فشار نظامی، به‌طور هم‌زمان اعمال شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/141548" target="_blank">📅 22:03 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141547">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3-P7zwX7Q4IbahzDzloI6WjMx6KbWilAMeO112oKgvfd1k-Kw0sYI8Mh28o-bAo9n8egbZq1njGy5WHh7OcwiL9Vo9w2sniAQCTC9oYAfuUNJUuk0VLOkmEL_iB6Y3jyWG2llnvRvQBWLaRfmL-eiwI3ETUoVVeZxFEhy_ap-wcd9evtFht3rdQFs1nHJ7jLvvGkJPoPneAy4XNOTyYyy_g852ZhbnmvmTloXl_U0ingaqIefCZh5QNdfLauiVJ1T0LAw5StoOThhvWG6h2enCiSenhxsOP4aOJRZR4XH4AnwXv-JJQk8n7bfPKCwZJc96szxGpEHkMz21Sy4uXKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی سعدوندی، اقتصاددان:‌ چطور‌ رویتان می شود وقتی خون مردم را در بازار خودرو در شیشه کرده‌اید، از مردم بخواهید افزایش قیمت بنزین را بپذیرند؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/141547" target="_blank">📅 21:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141546">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
کان نیوز: برد کوپر فرمانده سنتکام به اطلاع مقامات اسرائیل رسانده برای آغاز مجدد حملات به ایران فشار می‌آورد و از نظر او فشار نظامی بیشتر می‌تواند تهران را مجبور به تغییر موضع کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/141546" target="_blank">📅 21:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141545">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
وزارت دفاع ترکیه روز پنجشنبه اعلام کرد:  ترکیه، عربستان سعودی و پاکستان بر اساس پیمان نظامی‌ای که هفته گذشته میان این سه قدرت منطقه‌ای به امضا رسید، وزیران ارشد خود را در قالب یک گروه مشترک گرد هم خواهند آورد، رزمایش‌های مشترک برگزار خواهند کرد و همکاری‌های خود در حوزه صنایع دفاعی را گسترش خواهند داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/141545" target="_blank">📅 21:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141544">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L14AAxMzTTI6cuRxDKNJQqbBsXzEENZ9YraqHPEhLbHreB6ckMI3trBoECeVs6iSQ95EqiqN3jG3qhMCGjwsfI5KfpVy8EVP0tvErEXAfeoduCWXMv3PHtHQxigusFkpJH5KV_6_eEPhP9Wd255N1uFUgVEW1z_N6h1OO2NKGrcFMooIkgsnUkNuLBvFcXmkS3PpoVPFChT36EHQPbntVOrMfduaKEmM24X0OOlhxLFUFJYAiS_2xVhbL5fN8TgnFPaO1JNvuEGWEISlxeL1s3Ok8iZLTRhHlYgekOIUREDXoIO09PdnpyceU-ylzpCpD05Ukz2r1Tq0pnu1Vb5hmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی:
رهبرمون هرچی بگه همونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/141544" target="_blank">📅 21:46 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141543">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">حوصلم سر رفته بود رفتم تو این بازی جدید صراف شانسی این چنگک رو زدم، 3 دلار داد
😐
😂
گفتم لینکشو بذارم شما برید تست کنید ببینید چی میده بهتون
👇
https://B2n.ir/mn1122</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/141543" target="_blank">📅 21:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141542">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
پیت هگست گزارش‌های مربوط به تخریب شرایط در ناو هواپیمابر ابراهام لینکلن را رد کرد و آن‌ها را «کاملاً تحریف‌شده» خواند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/141542" target="_blank">📅 21:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141541">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/524d681ef1.mp4?token=Ds_wsfXw3q76PDXEOWiBj5IvhZY_DQwDdMZkEfHaxmH-duL4R32S-Lxsk-v0h0V8QUMKB-ryi1GQfjl2XheNyyjNz1H94OvLAXml3Vi9CSKHTApOOr3qrB4emy9uD7RtrGDsI8axTaH6a7qrJySYmndUIJMEJHNO-4pqzGxt-06uNu_H9bSo19KNPcqs6rrZfvr7xltxcjXKF7G1xeQCt3QoYQ-nv5dsdsPimO2gOLA_us9wmGSbfqJtySLolfGUDbMXiQqg3mGDTvDElpH2JmtUtdI_ntYMoDYWzdnTAdvAipN8g7k8_l7WlUJOgMO3t7DnSJNGDXh4fNJdWhtk_Qbau4z7A34MjazOU7NCJ7_nx3aWCLTYQRsFcR97TTBJZo7pK0n0n8f80VX3vY8NaZHUXWFJFhS2A6lYOJnNdwjXxOjuXL4GWd7_EgaebBLV29vVj5NK3wbhvY7N9SZB_jF56tU7eQDqn_qxVhtcG5lfiio2AP5lHdVBlhcXt3we3T7pxY7qLGPIzwr0vHJFyp-arubKPTKvp044ctWxHRV4WXicPuLJ93FGu96uK2CoOsmJ6QPiBLXzd56P7QaMe2l-483fBr4Ce2HN7dDVJCQQsfOPNQ4rVhznqSoImCFVIVJq77SoTDdocKUqjvWjJqzKhbRoP5gfpoKhiMD9hNE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/524d681ef1.mp4?token=Ds_wsfXw3q76PDXEOWiBj5IvhZY_DQwDdMZkEfHaxmH-duL4R32S-Lxsk-v0h0V8QUMKB-ryi1GQfjl2XheNyyjNz1H94OvLAXml3Vi9CSKHTApOOr3qrB4emy9uD7RtrGDsI8axTaH6a7qrJySYmndUIJMEJHNO-4pqzGxt-06uNu_H9bSo19KNPcqs6rrZfvr7xltxcjXKF7G1xeQCt3QoYQ-nv5dsdsPimO2gOLA_us9wmGSbfqJtySLolfGUDbMXiQqg3mGDTvDElpH2JmtUtdI_ntYMoDYWzdnTAdvAipN8g7k8_l7WlUJOgMO3t7DnSJNGDXh4fNJdWhtk_Qbau4z7A34MjazOU7NCJ7_nx3aWCLTYQRsFcR97TTBJZo7pK0n0n8f80VX3vY8NaZHUXWFJFhS2A6lYOJnNdwjXxOjuXL4GWd7_EgaebBLV29vVj5NK3wbhvY7N9SZB_jF56tU7eQDqn_qxVhtcG5lfiio2AP5lHdVBlhcXt3we3T7pxY7qLGPIzwr0vHJFyp-arubKPTKvp044ctWxHRV4WXicPuLJ93FGu96uK2CoOsmJ6QPiBLXzd56P7QaMe2l-483fBr4Ce2HN7dDVJCQQsfOPNQ4rVhznqSoImCFVIVJq77SoTDdocKUqjvWjJqzKhbRoP5gfpoKhiMD9hNE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
تصاویر جدیدی از آلودگی نفتی سواحل قشم که یک غواص ثبت کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/141541" target="_blank">📅 21:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141540">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6aa7b78e25.mp4?token=AVe6se-6bTwfc3iq8pfSfP0EPpYv-3FqGr5jjpzCvUueUf_ZxNkSJKturULNSVfUfIZpavKThb0kMEFln5e7uRwFQBGuvcGoGO8zGBBjCFaYSKKOXnmkGIy1EoQVywfxyBx_K3y4wWcMfGks5Zw0aa08AViz22O4KkTISpWQ1lumZ0NGtWsXmiMH--MW-TtnbFLfVrpVS5ErtIOSeSUdGPRfiK5wHvGORay0vmSk13jjKjf4ImKz23gMiUc-b16SdiYcFRClNCexXlfROsFbfIbG0Ja5QTjjUe_ugOZ35TI4_N-nrMgbTWviLJSBvQiIxdUxw2V_HHS9DUviX4dKT4m-ai2GrYPIA_P78jmnJtyElHB_TdtD_T87aTx4GQphmlIsq9i2nAOSRr_g4e_D0Uq-lQkX0S6gysqdC5U0N8yWcghzxudKoVRx8nLFbKxXv-PfIeVKHuxjEo--9ReFktvxZzm5KtGdY03BL_Z912vPmlxp97oHownAMh23W9ZvESvK2h1L5JS_L9uoJnEv3X8_NG9Fkqq2v-bygsxCHGZbUv5M5CjC5d02HZxKluuYs3WXotfIu2Vv9e4dS1dC5w4RdKB_GwmeAGojAixDOJjvzvt4r-kFXjqQnMxXYOcG-1sWkSJYP41MBwRUzgxQw_01pxDeUMaS0oauofBBgcM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6aa7b78e25.mp4?token=AVe6se-6bTwfc3iq8pfSfP0EPpYv-3FqGr5jjpzCvUueUf_ZxNkSJKturULNSVfUfIZpavKThb0kMEFln5e7uRwFQBGuvcGoGO8zGBBjCFaYSKKOXnmkGIy1EoQVywfxyBx_K3y4wWcMfGks5Zw0aa08AViz22O4KkTISpWQ1lumZ0NGtWsXmiMH--MW-TtnbFLfVrpVS5ErtIOSeSUdGPRfiK5wHvGORay0vmSk13jjKjf4ImKz23gMiUc-b16SdiYcFRClNCexXlfROsFbfIbG0Ja5QTjjUe_ugOZ35TI4_N-nrMgbTWviLJSBvQiIxdUxw2V_HHS9DUviX4dKT4m-ai2GrYPIA_P78jmnJtyElHB_TdtD_T87aTx4GQphmlIsq9i2nAOSRr_g4e_D0Uq-lQkX0S6gysqdC5U0N8yWcghzxudKoVRx8nLFbKxXv-PfIeVKHuxjEo--9ReFktvxZzm5KtGdY03BL_Z912vPmlxp97oHownAMh23W9ZvESvK2h1L5JS_L9uoJnEv3X8_NG9Fkqq2v-bygsxCHGZbUv5M5CjC5d02HZxKluuYs3WXotfIu2Vv9e4dS1dC5w4RdKB_GwmeAGojAixDOJjvzvt4r-kFXjqQnMxXYOcG-1sWkSJYP41MBwRUzgxQw_01pxDeUMaS0oauofBBgcM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیدان درباره پیوستن مصر به ائتلاف مکه : مصر شریک طبیعی ترکیه‌ست و امیدواریم به‌زودی به‌عنوان عضو رسمی به این ائتلاف بپیونده
🔴
فعلاً چند مسئله فنی در حال بررسیه و بعد از حل اون‌ها، مانعی برای عضویت مصر وجود نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/alonews/141540" target="_blank">📅 21:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141539">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89761a2149.mp4?token=OISCJAkutVgbtwPkfkaOHOt721qA24TOKLvh4m68n1s1q90nRCkXQfZooF8v-h8cJf-ty8RvmF4CmwFqfAli9C0OHtHI6EeDkSXiY-NcWHMvxd1npilRi2_3rySPNnInTugql7avCO7_DgNcm8dwyvd9CtsKq5ipdPrvojDAQxyISESzSQOBTdASrOI20Fr9ewzX_HBMuUfTISDxqhVGP88qcpeGTYnGtiVWdyivrrEjbxo2TOa-orcrwgOOJH_xvyTN6b8lwPgGueimOLDhaN-rpbHdsefN0_wvoBAJxtESlyZkUAiaDRn2EPVkefGCsS_RbxOKUyVy_0QrOmc9Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89761a2149.mp4?token=OISCJAkutVgbtwPkfkaOHOt721qA24TOKLvh4m68n1s1q90nRCkXQfZooF8v-h8cJf-ty8RvmF4CmwFqfAli9C0OHtHI6EeDkSXiY-NcWHMvxd1npilRi2_3rySPNnInTugql7avCO7_DgNcm8dwyvd9CtsKq5ipdPrvojDAQxyISESzSQOBTdASrOI20Fr9ewzX_HBMuUfTISDxqhVGP88qcpeGTYnGtiVWdyivrrEjbxo2TOa-orcrwgOOJH_xvyTN6b8lwPgGueimOLDhaN-rpbHdsefN0_wvoBAJxtESlyZkUAiaDRn2EPVkefGCsS_RbxOKUyVy_0QrOmc9Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هجوم بیش از ۱۰۰ هزار آفریقایی به اروپا !
🔴
راشاتودی از ستون عظیمی از مردان آفریقایی خبر داد که با اسکورت نظامی در حال عبور از صحرای شمال آفریقا به سمت اروپا هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/141539" target="_blank">📅 21:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141538">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEsDJCua_ENLlj_U52A89S1fRRcZAuvL2CD78dM6madeCFkG_GKyXOfzt6ZCnzC6edXrPZj9VWl4kPvLNeUBT3VVpZUflmfJvqGgRu0eRO-SxUqLgHfAEHvQfHVhnpsxP-LLvMWIFaPu_eQJbi82LGC3qheKMlmsdhlyakcE0b2bGsvUWWpkZFVSoIDeppogVMoq7EyfRrBUUPlT63qgj1S1wpxuEgjvCGbV-0AIgl-habinX89hIA7ChqVUGIUKpxilzBIiobQRoBO_hxB5toM7wZkvdLKnhgODk4zKQWueTc40C8SJq8Hs-tlFcU60SYiFU-q-3S59vCqY9eM3mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر امور خارجه ترکیه، فیدان، با وزیر امور خارجه مصر، بدر عبدالعاطی، در شهر العلمین دیدار کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/141538" target="_blank">📅 21:14 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141537">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
هگست: آمریکا بر خلاف بقیه، وارد هرجا میشه باعث رشد اون کشور میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/141537" target="_blank">📅 21:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141536">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل: برد کوپر، فرمانده سنتکام، به مقامات اسرائیلی گفته است که او برای حملات مجدد به داخل ایران تلاش می‌کند و معتقد است که از سرگیری جنگ می‌تواند موضع تهران را در مذاکرات تغییر دهد
.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/141536" target="_blank">📅 20:58 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141535">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
قانون‌گذاران دموکرات از پیت هگست، وزیر دفاع آمریکا، خواسته‌اند درباره کاهش گسترده نیرو و امکانات دفتر آزمایش تسلیحات پنتاگون توضیح دهد.
🔴
آنها همچنین خواستار بازگرداندن چند دهه ارزیابی غیرمحرمانه تسلیحات شده‌اند که از وب‌سایت عمومی حذف شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/141535" target="_blank">📅 20:37 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141534">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
وزارت دفاع ترکیه: بر اساس «توافق مکه»، رزمایش‌های نظامی مشترکی را با عربستان و پاکستان برگزار خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/141534" target="_blank">📅 20:14 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141533">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThGlhu2uQK6Y7AAVvDIc0-tCmsm_GfYPPKIaLtt0FZO89y2YKVZwT0LBf2kpQtUf6kCJ1n_VBd_poOYdEakmXGYDfieOijy2FFRrq4igjvOxbibcXPatKeysdE7ZjXqG4rpE0-64ykH5f7z8odV0fBe2lGfx5k_-AgzM0GtEfNRit5rmk5Uh7-SM1MxLKyW0i2QLRgXr6byqcVTQb9TKZ05Abyi1R9C-qxbnP8tF_5O4EK0QAIJoebED0JgrHz9ikA1fy-GQ2j1Mwe-WtYhFHejvS4m-6jPHt_Y0QX5rRaGqezqWMIqLbuvlwQJWYyEFUph7PbBMkkuBU1_uLCrUMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عبدالرحمن منصور، شهردار منصوب طالبان برای شهر فیض آباد، پایتخت استان بدخشان، توسط جبهه مقاومت ملی ضد طالبان (NRF) در یک کمین بمب‌گذاری شده (IED) ترور شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/141533" target="_blank">📅 20:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141532">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
مارک کارنی، نخست‌وزیر کانادا، تأکید کرده است که حاضر به پذیرش یک توافق تجاری نامطلوب با آمریکا نیست.
🔴
هم‌زمان، مذاکره‌کنندگان کانادایی در واشنگتن در تلاش‌اند به توافقی برای کاهش تعرفه‌های آمریکا دست یابند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/141532" target="_blank">📅 19:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141531">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZYQ5fAFvbzqmC1fd3f5QW8XpC-9nxVZDCY0_EYU9JEboeH17i-Guwg8o4U3OQSS2_Vpuvk_V5ooUArj3gQcWNA-RrwCYpALu99nsAAv2lmJCH64lD0cQmhTHje5xQJc3pxI5yINb1IQIRQxr4wBUtXKbuPahoEdiBgbhTi9aVybghfu8g1_0bpAEcNbHBMbZhGvCcq2fJA8bDWiVm3c6fKIVUmj6zqCAcBQa3U5EqP7gIG61KrCjJV2cKaSw7uDPFerGhWrIxhp_dtxyOcCFs40fPKOiqwMmo2GFu9WHwGQJdcUs7vepbS001ogsmJuzNqiAuKGF3v5w4Y5zJ7EBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
افزایش قیمت نفت برنت در ساعات اخیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/141531" target="_blank">📅 19:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141530">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
برخی منابع عربی: تهران دمشق را به هدف‌گیری ۱۰۰ نقطه، ازجمله کاخ ریاست‌جمهوری سوریه، درصورت مداخله در لبنان، تهدید کرده‌است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/141530" target="_blank">📅 19:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141529">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
نشریه WaPo  : آمریکا ۴۵ پهپاد ریپر از دست داده
🔴
آمریکا در جنگ با ایران حداقل ۴۵ فروند MQ-9 Reaper از دست داده؛ حدود ۲۵٪ کل ناوگان
🔴
ارزش این تلفات بیش از ۱.۳ میلیارد دلار برآورد شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/141529" target="_blank">📅 19:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141528">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
برخی منابع عربی: تهران دمشق را به هدف‌گیری ۱۰۰ نقطه، ازجمله کاخ ریاست‌جمهوری سوریه، درصورت مداخله در لبنان، تهدید کرده‌است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/141528" target="_blank">📅 19:25 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141527">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnS3isT2n9BRJfqNMt_azyGxgAbb44qXOeTKW5bd432iaATZK9-KZK41wK6EsjK2dlLTXBiCNElB0utUZA0vf_5KrYtzZRdj5ZIdG9aVaISHip3fgGuptyuklLxgMGjEZ9x4wgysY6A4-tW8Usq2WMx222E_PgIF6KoujU_ttov48gZH1hxDw5hsJBTp8hzW4ak4YrdQ0JbmDv1QcLUCAEx4GW_m3wFB33_OnBhFFaK1CJPClvw41mycPmD-XR2F3F0Cb8Er3idIeS5V-5oitnWQcmHfJMRPU9CtCw4qnNoawLkbRCEv6KftrRDquIHGCsPEu_RyNNFQcxJ7REECAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر بهداشت و سلامت آمریکا، رابرت اف کندی: تا جایی که ممکنه فست فود نمی خورم، مگر اینکه دونالد ترامپ مجبورم کنه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/141527" target="_blank">📅 19:21 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141526">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
دبیر سابق شورای عالی فضای مجازی ، فیروزآبادی: یکی از نهادها فشار آورد کلمه «هایده» و «لوزام آرایش زنانه» را از موتور جستجو حذف کنیم؛
🔴
چون ابتذال و تبرج را در جامعه ترویج می‌کند؛
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/141526" target="_blank">📅 19:16 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141525">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ناو هواپیمابر جرج اچ دبلیو بوش ظرف سه روز به خاورمیانه میرسه
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/141525" target="_blank">📅 19:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141524">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
وزیر دفاع آمریکا: ما قادریم تحریم‌های ایران را تا زمانی که لازم باشد ادامه دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/141524" target="_blank">📅 19:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141523">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFHIidye8VNQPmZdyt9s2HM-whqHAQSsHEXdU3pQfF2JWTrJjkhm796UbcOzcMxf2__c6rS5p7EOSzcawDgkPSlwFMxHxyFi6k3FayEU3inZ_89D2BDCLDp4U0dQLaK0-eUX-VV8d9SSjdpM1oRKDRkUwv3meQvY76I6k2giita7ja5xJAyqLjvEW4BnkLgViZunCaBMU6PmKf9YwxQ8qQv7jt_wb3j22s3XaIXP9-pTnrUsGDIpps6Zg2e3phsKiAvmDnBNiqYuiSw-UTqh_ZxVISXa-eXnyD-BC9nwuobd_RhrFEAikmMSwhbnfeUtkpRXgJHpX4BF4Aq3HhL74Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل رئیس پلیس غزه را هم ترور کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/141523" target="_blank">📅 18:51 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141522">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
تحلیل بنزین و تاثیرش روی تورم  شنیدید از قدیم میگن فلانی «هم چوب رو خورد هم پیاز رو»؟ الان داستان اقتصاد ما و قضیه بنزین، دقیقاً همینه!  بیاید خیلی ساده و خودمونی اقتصاد رو بررسی کنیم ببینیم ته این بازی چی میشه.   قضیه از این قراره که کفگیر دولت بدجوری به…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/141522" target="_blank">📅 18:46 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141521">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
به گزارش رویترز، شرکت هسته‌ای «نوکلرالکتریکا» رومانی روند خاموش کردن تنها راکتور هسته‌ای فعال این کشور را آغاز کرده است.
🔴
با توقف این راکتور، تولید برق هسته‌ای فعال رومانی به‌طور موقت متوقف خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/141521" target="_blank">📅 18:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141520">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
نیروهای مسلح یمن: ما ۳ قایق حوثی‌ها را که حامل مواد منفجره بودند در دریای سرخ منهدم کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/141520" target="_blank">📅 18:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141519">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
نیویورک تایمز: غول‌های نفتی خلیج فارس میلیارد‌ها دلار صرف ساخت مسیر‌های جایگزین تنگه هرمز می‌کنند
🔴
این پروژه‌ها میلیارد‌ها دلار هزینه و سال‌ها زمان برای تکمیل نیاز دارند، اما شرکت‌ها و دولت‌ها آن‌ها را ضروری می‌دانند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/141519" target="_blank">📅 18:37 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141518">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
فیروزآبادی، دبیر سابق شورای عالی فضای مجازی:  گروهی در ایران می‌خواهند اینترنت ایران را بالکانیزه کنند، این افراد طرفدار توسعه انسدادی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/141518" target="_blank">📅 18:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141517">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8563204fb3.mp4?token=WgY4NM7obaq94AQHmLS1bNOvD0LetrBHI5YCsBxgRc_BIJEc6dXSrkAJq-Jwq7AKFydw_dGj6TaIIa8yMPxR53_NlgVSAabBQa4YP3bZCUo8C3Tj2ejWW-zDhPxF9Y0VEoyMNOAvJN2CdqE-Q6_lhSVGRsH0ysg5FnY4vqXWth-VEaBADzld8QliZpd_C-0zS1t3e6tHrJzNCqY9vb1h03Kp0TwzeYZT0Lfyqo6ytc8gfNJMeT8zXFllSnlCE7nykYD8AtlW7_5ZRUYNXqvsfXmUG0TNxbXLXsVv1mVxNhtSms7kG9ERJO8eP1GiDpaxYvujfWLfBqlQzBUCHQXt0hZ0ycaCPNrpi-CjpAee-qjASyEu6MBQv9Tm_fLgsNbLbXoksTETBZ-rg_gjG5b0_MOulOACL2qfdTWDeLueQD5tY7SLU_XCvdl1ynvuel_A57Qeae4W3qnQVRpQWu8B-RFOKVz4NK50M9hLpI2UGBgls5qtYLzZvlh_opNnL_b1raFklEuH8nhbg97ZiMBKnK0lkm__z5XyNbeMM7OsYEhZK0PM017meM0EYbIAqn9JQbgBV_BJXKF0AuGkuO6bOFBFfVokjVuhL_VHAlB2bD7R6C-D5qttbscGiovPdlCCvKtrSmqPyDtRNwJzw-DrYMbP2zjiwwjxNBfiTXUExKY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8563204fb3.mp4?token=WgY4NM7obaq94AQHmLS1bNOvD0LetrBHI5YCsBxgRc_BIJEc6dXSrkAJq-Jwq7AKFydw_dGj6TaIIa8yMPxR53_NlgVSAabBQa4YP3bZCUo8C3Tj2ejWW-zDhPxF9Y0VEoyMNOAvJN2CdqE-Q6_lhSVGRsH0ysg5FnY4vqXWth-VEaBADzld8QliZpd_C-0zS1t3e6tHrJzNCqY9vb1h03Kp0TwzeYZT0Lfyqo6ytc8gfNJMeT8zXFllSnlCE7nykYD8AtlW7_5ZRUYNXqvsfXmUG0TNxbXLXsVv1mVxNhtSms7kG9ERJO8eP1GiDpaxYvujfWLfBqlQzBUCHQXt0hZ0ycaCPNrpi-CjpAee-qjASyEu6MBQv9Tm_fLgsNbLbXoksTETBZ-rg_gjG5b0_MOulOACL2qfdTWDeLueQD5tY7SLU_XCvdl1ynvuel_A57Qeae4W3qnQVRpQWu8B-RFOKVz4NK50M9hLpI2UGBgls5qtYLzZvlh_opNnL_b1raFklEuH8nhbg97ZiMBKnK0lkm__z5XyNbeMM7OsYEhZK0PM017meM0EYbIAqn9JQbgBV_BJXKF0AuGkuO6bOFBFfVokjVuhL_VHAlB2bD7R6C-D5qttbscGiovPdlCCvKtrSmqPyDtRNwJzw-DrYMbP2zjiwwjxNBfiTXUExKY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگستث، وزیر جنگ ایالات متحده آمریکا:
ما کارهای بدی به آدم‌های بد می‌کنیم.
برای مدت زیادی، آدم‌های بد کارهای بدی به آدم‌های خوب در داخل ایالات متحده آمریکا و در سراسر آمریکای مرکزی و جنوبی کردند.
ما قصد داریم به آمریکایی‌های بزرگ و شرکای بزرگ قدرت دهیم تا کارهای واقعاً خوبی انجام دهند و در اعمال خشونت علیه کارتل‌های مواد مخدر و سازمان‌های تروریستی تعیین‌شده بسیار توانمند باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/141517" target="_blank">📅 18:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141516">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5Be-xGy-VsjeUS-71FSAvdKIWu1Obij_FEGwK6owlR6n8T-zKyp_FhqrOuqGj_q3ULwC9tjDEbM8VIuWYw-JqfUueZVKxstJ82WwBPJc_R_47ioZtiz27TlpS19YD1qi0EHmpHMIoVlF211uD9ZYPr0eihkHxYT25e52rcOHUslgWf8THKAl9OQKUk78HLzWmB5fKsqkYX8piTGu9KptbnHt2MsywQN2bAPSP1nFJb0Ag_qvoNZgO12mQZXwx6KuQ5pD0JQAbgdn-mheUrAuPFIX-cYQE9fqBuGTbF23R8igAVGxx68E64_gXBAprmTIpiRwJ2z0Fze-Yro3HqiZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
الحدث: سفر اسماعیل قاآنی، فرمانده سپاه قدس در بغداد با هدف منصرف کردن گروه های حشدالشعبی از تحویل سلاح خود به عراق، به پایان رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/141516" target="_blank">📅 18:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141515">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfd4d419c2.mp4?token=dOFMTNj7XPn4ZfMuw5aKRVi6xvAQ8_LoQ20OvdXMu3exIOBnbxhBil8uvLcdGC8GG9ldKnRZ82M2dJ-_8XfPdgwRkqhszFD75NvAbViNe7Jl15RvPgK1SLkoa6DIYrQxlgEwaJZxsnCOWRNdKVLmnrfJrwAIIUS6UzZfnL9IxrkkJoK8VwdtsD1jNQOOeB3_jnvDQ9jAH3Gluz_jlaQKqfxLXY37TT17oQXfBOpUJULsAFHH2p78iThLkPECR7KXNeFWxRZxq4ehqDr_Ut3QWfJhUz8d374fd80BY-YifVHegbK-akgkI_GMh2HMYfcatGyDDu2HfFhGkGNF5HTDOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfd4d419c2.mp4?token=dOFMTNj7XPn4ZfMuw5aKRVi6xvAQ8_LoQ20OvdXMu3exIOBnbxhBil8uvLcdGC8GG9ldKnRZ82M2dJ-_8XfPdgwRkqhszFD75NvAbViNe7Jl15RvPgK1SLkoa6DIYrQxlgEwaJZxsnCOWRNdKVLmnrfJrwAIIUS6UzZfnL9IxrkkJoK8VwdtsD1jNQOOeB3_jnvDQ9jAH3Gluz_jlaQKqfxLXY37TT17oQXfBOpUJULsAFHH2p78iThLkPECR7KXNeFWxRZxq4ehqDr_Ut3QWfJhUz8d374fd80BY-YifVHegbK-akgkI_GMh2HMYfcatGyDDu2HfFhGkGNF5HTDOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه پَر کالباس 80هزار تومن
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/141515" target="_blank">📅 17:56 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141514">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/075e2967ac.mp4?token=KIcXMhIZOO1Ei7HURywI-1cotGzIrU1CDu0D8oOOe_Z6q-BCBghAW4OdsEMbIfo8wpfADRJbLzbNqqqsiQTAYyvvOIq9TiKVLyL_tjN_4s3xnc18ssxOtpZD3LMT2HNSA8iNgADPz5bkJsV6zNEJghuVKxExhHPM3Bx8-4QBMlIHzxdm03-Xn5hSP4_CzE7SXFmL31xFyp8R8MklguNIBB173sIzLzhzUFdZQkvoUdLa63Rd1PAyiH4gk5oNKwsISMPyGoB2FEQiy6_pBngfq4NfCSzFM7O_Xi2ae8tCPIr9w53hnBAs6ATy276Xdl_h66M2lTdIpPZZUKQcskFRgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/075e2967ac.mp4?token=KIcXMhIZOO1Ei7HURywI-1cotGzIrU1CDu0D8oOOe_Z6q-BCBghAW4OdsEMbIfo8wpfADRJbLzbNqqqsiQTAYyvvOIq9TiKVLyL_tjN_4s3xnc18ssxOtpZD3LMT2HNSA8iNgADPz5bkJsV6zNEJghuVKxExhHPM3Bx8-4QBMlIHzxdm03-Xn5hSP4_CzE7SXFmL31xFyp8R8MklguNIBB173sIzLzhzUFdZQkvoUdLa63Rd1PAyiH4gk5oNKwsISMPyGoB2FEQiy6_pBngfq4NfCSzFM7O_Xi2ae8tCPIr9w53hnBAs6ATy276Xdl_h66M2lTdIpPZZUKQcskFRgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه زنه بلند شده میگه من رهبر سوم جمهوری اسلامی هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/141514" target="_blank">📅 17:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141513">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6PYE_2a89R2hMCIyjvZXE2QHAu6NMEHWyKtkb7vAOKGN4BT1oOP4vC6WW7Lst3wRz1y6VZLqu3zW2L31jg2tZ3NtV_oZ_J2MOLJ5efFRUMiuF_I2pllm-Pz6ANPfTv91y4bv1oR6zc2df-3Mm_Ci98nlGI4oKzpEEIfSdmrXdQcQazYcrUenP67z7FCYfMUcqUtlF4JOt1LzDMQ3sHNop7sVEHR8Rk387qmkzdMgrV8U8V7_JwzC4I36kn8EDBzfCoSu9YgGksexpEUJqYO-Md1fMCs3QF-Vus5CY5JflRQLK2U-SQrOtserhcG2mf348vHApVE1a2G1uRR9bvQOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد مخبر:
راهبرد قطعی رهبری مبنی بر تهاجمی شدن جنگ در صورت تحقق نیافتن شرایط ایران، بدون شک معادلات قدرت را در جهان دگرگون می‌کند با اثبات ناتوانی آمریکا از محافظت متحدانش در خلیج فارس، پایدارترین‌ راهِ نظم جدید در منطقه، اجرای سازِکار‌ اقتصادی-امنیتی هرمز، مستقل از تضمین نظامی واشنگتن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/141513" target="_blank">📅 17:37 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141512">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
روسیه یه شرکت لجستیکی اوکراینی رو تو شهر پاولوگراد هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/141512" target="_blank">📅 17:07 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141509">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a179373787.mp4?token=Lxqj9M7UYyKZUkU_DRyEvXAbwEZz8d2tk-98_pVC_OKvlrfnJoUcGaWToZ07vxrgQTBcP430U7FWRLFQmEe9UzF_-Sq6eqIX8z_tZiY54ZWNOwT4AXURGkKArR2e8vHxZO2B9tNVpBtGG58KuyDg4YrgT7XQqSlX9ryr2NoX8ExdYQ8DOM_SeVioH3U7Ilxmdge3LkCrJ96TbxG5dT5qKaSHIylzgSrCE8n36pVXK1zqo0PsibOwDc1E_oRj3N5ACebVwN4zxDGFDpsv5OSshUPl1fECiJjzpZlasmBqIINh9FJG85viHi3ZMgYUrejYbrsONzvCJFlB_L9we0dTGzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a179373787.mp4?token=Lxqj9M7UYyKZUkU_DRyEvXAbwEZz8d2tk-98_pVC_OKvlrfnJoUcGaWToZ07vxrgQTBcP430U7FWRLFQmEe9UzF_-Sq6eqIX8z_tZiY54ZWNOwT4AXURGkKArR2e8vHxZO2B9tNVpBtGG58KuyDg4YrgT7XQqSlX9ryr2NoX8ExdYQ8DOM_SeVioH3U7Ilxmdge3LkCrJ96TbxG5dT5qKaSHIylzgSrCE8n36pVXK1zqo0PsibOwDc1E_oRj3N5ACebVwN4zxDGFDpsv5OSshUPl1fECiJjzpZlasmBqIINh9FJG85viHi3ZMgYUrejYbrsONzvCJFlB_L9we0dTGzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز، اعتراضات خشونت‌آمیزی در پایتخت سومالی، موگادیشو، رخ داد. این اعتراضات پس از تلاش دولت برای اخراج اجباری غیرنظامیان از خانه‌هایشان در منطقه وابری آغاز شد.
🔴
پلیس سومالی به معترضانی که در برابر اخراج مقاومت می‌کردند، حمله کرد که در نتیجه، یک زن مجروح شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/141509" target="_blank">📅 17:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141508">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vh1_wMTx1MUA77geAALj4MpcYaofKruEEhobjUYhlCT3E3appbpwxAVE-lEQwhObzwl45ePRhdd1uszmEoNBjPIGjejHJgEtQt3w0ZM3F0dfJeN4acy83_D1FRIapqi2xXSa7YFu_btm_IZUk7D2VJ9A8N77ljjebKGnV_y3XIzr8jTFpWUwKN0DUDkuaVUVMgNsQTCucyZQJGboN_UbNp4qr6axSwPwX4tcoLnigLM1Albar82TChXAnEdaFnIuCSiZz1EZ7livE_HgrFFK5O2CzGl_j7AZavvKfuAbEMJey-CKZLxjd2qw43Q8dObLmC4JsTGEyu2Bp2mR8m2otQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک پهپاد ارتش اسرائیل دقایقی پیش به یک خودرو در شهر غزه حمله کرد.
🔴
بر اساس گزارش‌های اولیه، حداقل یک نفر کشته و چندین نفر دیگر زخمی شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/141508" target="_blank">📅 16:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141507">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
حشیش و گل به عنوان پرمصرف ترین ماده مخدر در ایران اعلام شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/141507" target="_blank">📅 16:48 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141506">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aN0J1We5eA3BHY-qtFZFbYrvMxqGV5xlNRGOuQlsgANqy6r6j7BrpnGd59RgyRlNYivlf8K-HKMuRAlT1DbhGMdT2SC9jEH08WoSKQV5JutqteZ-JuRSj-nWC5r05wbkERYIA-AwlD2qvKNcrbhhAIk-572OaLgfYWNph2zWR4Y4E7f3LWJuE9To31WjASMidAMAWO50JHLlImby4JpvXzIuOeEI14VynUZPJmQgzUMLqP8fUq2ksOqgGZLYdLOhEIMTayqvqbvqaaLdWAa5fI3bGnU02HQeKVFPqAEp86ooJD8Fd50pRxGxP612vWiUJUiqFohwld2VQwzTr0F7NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
‏ ️
نامه عروس معصومه ابتکار به مردم آمریکا: عاشق آمریکا هستم نگذارید مرا اخراج کنند!
🔴
فرزندانم فارسی بلد نیستند، و مادرشوهرم در اشغال سفارت آمریکا فقط مترجم بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/141506" target="_blank">📅 16:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141504">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jHr7nGhwk5S29JmaTv498xJg41pLYYenOuAl9NbzsjOTl7ob_EvxFqUuazxKJInbMb3GqXc4wFb6och43OzzTxtw9b_muntD0WJ-q0gmlUdt8cNyaAdOVgopA3QyTj2QgRDYHWuSQVY9oNYVgJjqwWbkhhjUjP_Bwx6k-z2NqaUQkgIn8UyfXLphfRhkQOAcgb0tDI7PnlDjaSa_ffMmD1riCCNyH8SGUyw9wHLJeT3fLeQhLO9cwTeNlBlFuklgOVSQajWt3v5IwKCuoPtXAifrrHSNWcvaBQajdXUZ0_VLYmHVcwVKffoGqGUZEOrLPTywawDdPn1ASIc7xxah4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DSLXWzzW6CanWl9--WvhhIJDC9PTP_sEdMlghDEz3L-kHoNkSp6FfHG0pals5Auw1DTMWiav90r7XiPrPu6UFQXOuDX-Kh5_rXO3dNJbqikgrD-rDKW8yK7T4CTRQrLiyAO-XeIxCn2uk7VzbGJJfWWsrLDr2Hir5wKpSiNgSEpLz-vbM6pqpHF9gjv4t20MdW02sQvA9A-d9Ad_jsMwWXUXfTBw64ySt8FrJUdfMis2o0cnnjYLvyicKIqlT8x0j2w7aYMTubfV3Z_md4uiD_5x0PiAOlTwbp8aGQBEZzvpLwlSOdxq1jJiLK_XkwPZ2lk5-YRoN08RA_jvp3PZLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از عملیات تخریب نیروهای ارتش اسرائیل در شهر بنت جبیل، در داخل منطقه امنیتی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/141504" target="_blank">📅 16:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141503">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‏
👈
الجزیره:  ایران هدف خود را طولانی کردن جنگ قرار داده تا درد را برای ترامپ حادتر کند
‏
🔴
واشنگتن هیچ ابزاری در چنته ندارد تا تهران را وادار به انجام خواسته‌های خود کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/141503" target="_blank">📅 16:21 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141502">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل: خانه ها را در جنوب لبنان خراب می کنیم و با تمام قوا به شهرک سازی در کرانه باختری ادامه می دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/141502" target="_blank">📅 16:08 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141501">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8edd86b4e6.mp4?token=bsX0UklrQ2cWyPBYYRIgWJUaabtSWK_NwFnpnzzZSJJ5dW_QE767KpwqDn-Ez0hn0Y0qpfR6ByLaPzvjXKVMbjEAe4h_0rxIGNy8Z8jOAaLL5seRt6ebByKUtYfXOYdhmWP4ob290ScPvAaVx84q8pro9i4NxkldNQc0eNW8mHzvjP-Gg5DoW1wvh1fUcw4M4hsxdaJJIpsO20sD6wXxkxNrEPLmUObyc7Gu99a_FYf0JC_KGSweD1zcRQK6vcIZ0k32uBQmvO52bYEbeiChDfQsrbQZnM2USIj6bySJVa626_XWKo7dg6eUPU3g02gwJMtUKRZAm0IfWMRzzD40iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8edd86b4e6.mp4?token=bsX0UklrQ2cWyPBYYRIgWJUaabtSWK_NwFnpnzzZSJJ5dW_QE767KpwqDn-Ez0hn0Y0qpfR6ByLaPzvjXKVMbjEAe4h_0rxIGNy8Z8jOAaLL5seRt6ebByKUtYfXOYdhmWP4ob290ScPvAaVx84q8pro9i4NxkldNQc0eNW8mHzvjP-Gg5DoW1wvh1fUcw4M4hsxdaJJIpsO20sD6wXxkxNrEPLmUObyc7Gu99a_FYf0JC_KGSweD1zcRQK6vcIZ0k32uBQmvO52bYEbeiChDfQsrbQZnM2USIj6bySJVa626_XWKo7dg6eUPU3g02gwJMtUKRZAm0IfWMRzzD40iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی قرارگاه مرکزی خاتم‌الانبیا: هیچ کشتی بدون مجوز و نظارت ایران امکان تردد امن را از تنگه هرمز ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/141501" target="_blank">📅 15:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141500">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
خبرنگار العربیه: ارتش اسرائیل از آغاز یک عملیات نظامی سه‌روزه در شهرک قصره در کرانه باختری خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/141500" target="_blank">📅 15:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141499">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dska8IY-oFyT0I-pO8G_smBzu8P45E_s1s_9ysDNPUN3h9dVlxRTTN1x2CTb5bJS-nwzptmoIRik5pgyWle14wUDNTMGOt_jcACtYRDZ2EFdEoh-9lyOBtisgJMd_IG8EJMg29yaDgDBVCp8TaF0SDsrJqG_zo8f5PuYpGIEIkj3TeYHcZ5mSgwUxwuAKC-sfA649Y9Y5dS9iYESTk4w0wLAyO_O9nERB0gN5ZoNGruN5YGtMm893LPZt68gEcWHxuLLrPS1XXCVuw_ZlKW4PkP7HBKOxz82_RI_UMDV_Nw4Yq57bWCs1qx5D-Y5n0bPxjPFaaCRjWnqN2obKjYS9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ناو هواپیمابر آمریکایی "جورج واشنگتن" به همراه گروه جنگی خود، در حال حرکت به سمت ایران است، این در حالی است که مهلت آتش‌بس بین آمریکا و ایران رو به پایان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/141499" target="_blank">📅 15:31 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141498">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T14NxQ7FNO03Al0zyP7jL_mF2aFF_fxFQeq63iaRUPu3zLkzfPeBwrzuDr11L6QqdJlWYebL4dvpb_FQQ-MLJBKSlISCkro-vdDCKCpVk5oCUZHKeih1TgDEFap2riFOhF0XuRSplUoPxR4eSW_a9r1AXZ1xQFWIwMtgfHXy4iyc6E_W1-yhiCvlPj8aVCGX3PyQUXyz8YqEV5dwrEmaO372sLOEU1_rFl7IUr9S-68ZeJEIAz2eT3sgFi3KRDUkui1AUFDcN76CjOoqq1nqYes6bnPIyuEeXo-Ex4bxWqva5jtwWGhi3qzVZGbVNIPbbFM0GgogrZUiQvdlsYQ8UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۱۷ کشته و زخمی از نیروهای "درع الوطن" که به عربستان سعودی وفادار هستند، در پی حمله‌ای توسط نیروهای یمنی با استفاده از پهپادها به یک اردوگاه در منطقه "العبر" در استان حضرموت
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/141498" target="_blank">📅 15:25 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141497">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODKdwYV36itHd8vl_mT6mSGt1Z3eckwuoQvltLPOPC3GlP9hKiTxxBKrE9QYpbbTRhLATCIAcxhIEsR0GzqNhsPG0D7oxkSuceE1uMXP6FRTcSv36yQd3dmm4VMyNmH_VfghhjHJcOGzFXU7qTthBfCvc3Oq-BUzE5QDLMiu4jPbH6gwXFRVXIlotAvei9xvQH4t-fbqi2uYxhs7vZMMXPkkQh8Nk82XI_diCzjH7aJ9SfdnIC0EV5UcMAhp9ONVSlp1v_QgcKYl07n_EtNzqwLx5syrSE99rXFkbhQunToHx3jGfsPq3mvRkRDdc9963LKLi096tZ-sfcxxJAXy9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش یمن با استفاده از پهپادها، مواضع نیروهای وابسته به عربستان سعودی را در صحرای العبر مورد حمله قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/141497" target="_blank">📅 15:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141494">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WVfEFclfK5e-2f3DsDcBDg6Mdk4kkKt9cM2MlG5JvjVhWygr008-x7ijfxuuzl0zzoTmME9_tctYzqiFKPgQ6hetDyFE6rH_3mt1HsT4sS9LfGp4RdznErR3lUX-BdDQ3EM1eirbOX0qi9RLVvY-P-DnE5k1P3GegAW2vR_uZiVTasyqfAIQWdPue7qOKTW_arf6VeeaaNzPz5h5ZrzJTAEavyr8CQXrgqJ9tspc3eLpTjlocOT_YWAjHt6NAMKyWkQsJPrYpmTOdoppjBUK44oROGM_j7hCcsvMJzvHB51rtAdA93-S1q9CAaVn7CxCOK4_QvpNVXOBMsnmpDoKJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NotEXejBSb9vVlwHT5W6jL3Gt3X0GzGsvBrHRCzwbWw-kp7pMHwfbnyNVqPnvYnLbJLNugrxjY-fO-dcGh2Zgv-9OLovrGYh2ZNuBxPQffhFYB_JQZZcKw4F1UAqeKbTbJhK_tx20mPM6CBRY64IxY5ilQa4sIvZ9HbTBlrg75vqgEfMSeuWdeEO-OwYu3E99otxbIOXE9pvlD2xnPbXiqpRF4s25A7Eb2oRHkw5BosgLHJq1KOwdu4Y4mj2x36Ya9CGo2j6n17HAPT_2msOQJPFbgh1lQAppHyNxMdawNvOnRXiqijXA_S8-A7l56GbGQ--dSv7IFRneHPDmo9nXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sGi3KHn2TIufZD-xUOq3JlEKw3gymhu1NtqK12_EMGBpaAA2Pt6dhGnx2OCoDLPq8v0jXdHqMG5AUjFAgRHSUzTrgN-lEPoOGDbArfkl8ApaSe4QRy3ZB5DjTHKSPTcaSq-ryiZmerv7N9VRm7dIEMDG9z2b5n8vLKLZ2htOqW2UScA5yoH1X-gW0c5Y8_z_ILoVCA7uUpDaeCdWyJTsIRMrGaRUHARqNLCbguV31Q4kc1h5iSRFGwhq2-DMNU1SsHhGD3YLQof1vXqNRCreXN53_C-GxCgtBhIrk7mfDuWN_8GfTHsCNgxVDcXxQ9mF2TQ2sjqg3QD9MWej8lZAHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
وزارت دفاع اسرائیل : هزاران تن تجهیزات نظامی، و وسایل نقلیه جنگی از آمریکا به اسرائیل رسیدند. این خرید و حمل و نقل توسط وزارت دفاع و ارتش اسرائیل انجام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/141494" target="_blank">📅 15:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141493">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
پلیس هلند از کشته شدن یک نفر و مجروح شدن چندین تن در پی وقوع انفجار در بندر روتردام خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/141493" target="_blank">📅 15:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141492">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/244de8d332.mp4?token=LYoV_BibPsTvJpd-pwjOh9f1XUlln4eayXcRP80wVcf1PFCr-s55uBvn3mDfaUneYZED0lI3NkOwYFIy22l0SWPN1DyTSL31o3raJixjihYR4A_7AqYRzqRQ-k1KRKK0v5JhvY5TNTP_gCparOvU9RR1f7nkBJGXLPogNgxVhk0UOZ5Id6SCb4Itz5p-NaRNUyExr42oBthyX9FYtIpPGkUxUGf4vLb9z-BCBjdsoNgLj3dZlUIIrXAK9eaPGlnXTkeiWcYmfE3T4QfMxd8VP1Nk2nPAtrWztofkiA_ulvdfHQLBAjgHTnwEbJ5pKTl5ZDNobPWeddrqwIW3-AeApSAosgmGBg2B4dy3P0_9RdlUvBAJ_mRuCQ1Y-AjOKylx97giRi7smE8lF-1Bv98zkYsnG0_I9jDtQ1EwBjvDseMKNvvSPkF_-fFmM8vhoAuugJqY23fltnQbxw86SvZDfNSkIXgB1FUPNUTEC5Jy7p03XAFcBl1-n_Ixj4pEcn-XtSrQ-jXwTQnN8r7f6uRKtDH7Ho8Dta8TGyTJm78iuKZwIp9tTNUm4-pPTzFeNM6ovf37Nt5G3Kegfp90WtxFAYh2vWPpVO7Lpg2jWuBgVCThFv2ZticdCDY3QWuma4HBIRwRdszeF8iCA4mG3gfukU0SYCUutf-6WodLRXGpXMc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/244de8d332.mp4?token=LYoV_BibPsTvJpd-pwjOh9f1XUlln4eayXcRP80wVcf1PFCr-s55uBvn3mDfaUneYZED0lI3NkOwYFIy22l0SWPN1DyTSL31o3raJixjihYR4A_7AqYRzqRQ-k1KRKK0v5JhvY5TNTP_gCparOvU9RR1f7nkBJGXLPogNgxVhk0UOZ5Id6SCb4Itz5p-NaRNUyExr42oBthyX9FYtIpPGkUxUGf4vLb9z-BCBjdsoNgLj3dZlUIIrXAK9eaPGlnXTkeiWcYmfE3T4QfMxd8VP1Nk2nPAtrWztofkiA_ulvdfHQLBAjgHTnwEbJ5pKTl5ZDNobPWeddrqwIW3-AeApSAosgmGBg2B4dy3P0_9RdlUvBAJ_mRuCQ1Y-AjOKylx97giRi7smE8lF-1Bv98zkYsnG0_I9jDtQ1EwBjvDseMKNvvSPkF_-fFmM8vhoAuugJqY23fltnQbxw86SvZDfNSkIXgB1FUPNUTEC5Jy7p03XAFcBl1-n_Ixj4pEcn-XtSrQ-jXwTQnN8r7f6uRKtDH7Ho8Dta8TGyTJm78iuKZwIp9tTNUm4-pPTzFeNM6ovf37Nt5G3Kegfp90WtxFAYh2vWPpVO7Lpg2jWuBgVCThFv2ZticdCDY3QWuma4HBIRwRdszeF8iCA4mG3gfukU0SYCUutf-6WodLRXGpXMc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حاکم دبی در لندن مشاهده شد
🔴
محمد بن راشد آل مکتوم، حاکم دبی و نخست‌وزیر امارات، در منطقه چلسی لندن دیده شده است
🔴
تصاویر منتشرشده او را در حال قدم زدن در خیابان‌های این منطقه نشان می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/141492" target="_blank">📅 15:10 · 22 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
