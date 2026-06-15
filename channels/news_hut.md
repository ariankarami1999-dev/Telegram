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
<img src="https://cdn4.telesco.pe/file/kSSYCMxRQ3ZabGWMtc8p1Rp023JJtPm5kAYcFjrM9zVT4SNACixkbA8cdT66mQUl8UzwYU3Yl_VqRYa4UOO-PDssssI3tJNoAA020W5ucMEWtF7GIpQreeoqVJgzfsqyYbuLF4ziGCfXo7xxBUN7Ff-xuuu1gGB5KFa_YP7K1pewm4WbRJCiCWRmKOeG0sxqGo9cqqPBVqCrLwEGfL_Mo5mT_0zYjj81ndUiW6M497nJmFq5O7h3G8NPhWB45e9xKj745-t3NUhMVSehJ-Y100deKGTZOIx5SB2hQVpToM23XjDeMNTyUrr1_EqDVjGzkSeM39Y7G9Wl038qciBeAw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 224K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 03:17:21</div>
<hr>

<div class="tg-post" id="msg-66237">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
صحبت‌های ایرانیان مقیم آمریکا قبل ورود به استادیوم
@News_Hut</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/news_hut/66237" target="_blank">📅 03:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66236">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKT7v87L_L3zQigWSxFwbDTaudfLpvEo3aI21H14PdkgMN2n33eC2Hj_MFWGTSWVLCgRe4p8VmeXgaMN9j0yTdLBOiq-B-eguSdAE8HCmJUJEdZIf9ClTfzA-2L57Bx6mx8Ts3ycDm-1GI2REP8AkqNJcRX118adSNR1jCFjDwIdu9woZUdaFeDbI9itx9JyV-jkGu1S9Hc_jj28wQSt4UulBwgnwVs4JBhzhjr2VT6m2mwvst9NM3Zq5kRAUgj_KXUAEobores4MTFn5h49yWU_T9_Nn3EJ_mFlu4RLvGVNg1SV_lIx8AexBnpC2SLm7gkiYKSX3jSqe2Ciyn5eGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی از اسمش مشخصه، باید برای ملت باشه، من نمی‌تونم رو این تیم، پسوند ملی بزارم، یه مشت آدم منفعت‌طلب جیر‌ه‌خورن که برای ۱۰ دلار بیشتر ناموسشونم در اختیار ج.ا می‌زارن همونطور که تو ۲۰۲۲ وقتی مردم داشتن کشته می‌شدن اینا دنبال حواله خودرو بودن.  آخرین باری…</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/news_hut/66236" target="_blank">📅 03:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66234">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c366b2c0bb.mp4?token=pqTeHLWevD4fPsAhIdg1HdckOBRsskZ4x3hPdqZSxbPEja8ua40VRExfRgbxnTePtq1BbfVBvh2yvzkKnEguQmT8GjMingpsKVFffycFSSWnxxm-EoYG-xqIPGOFJvuLszMC-uZIucaLWC-Q9OGstBkd1SLG_Fi_Yxy-f1_nUJKfK72IVfsznqemmSzIURYqXnFIsmsqY_NiG01gzhNihcSt8T7uecH0Y3bkyQUZq8JYL0blqJZyaa_lwFUHHqeWMwLmIIskkoFQP6q6XwazexnYw_0KEX8KHd2X3ZpZOO-cs5ASeIRE8QGH1cqEaigR7tDd52VNuBAq9DB48rJPuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c366b2c0bb.mp4?token=pqTeHLWevD4fPsAhIdg1HdckOBRsskZ4x3hPdqZSxbPEja8ua40VRExfRgbxnTePtq1BbfVBvh2yvzkKnEguQmT8GjMingpsKVFffycFSSWnxxm-EoYG-xqIPGOFJvuLszMC-uZIucaLWC-Q9OGstBkd1SLG_Fi_Yxy-f1_nUJKfK72IVfsznqemmSzIURYqXnFIsmsqY_NiG01gzhNihcSt8T7uecH0Y3bkyQUZq8JYL0blqJZyaa_lwFUHHqeWMwLmIIskkoFQP6q6XwazexnYw_0KEX8KHd2X3ZpZOO-cs5ASeIRE8QGH1cqEaigR7tDd52VNuBAq9DB48rJPuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
تجمع هموطنان خارج از کشور مقابل ورزشگاه محل بازی تیم جمهوری اسلامی:
@News_Hut</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/news_hut/66234" target="_blank">📅 02:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66232">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzDWZFqw_64tQ1OxvKsyOepW48DHJqCSoUwtAyVTG4VP3fbD82N30UFL-ekpjk9euYBkTi5ZtE7mpxZiJNeccUi8X7hB9BnJEdDEtbejcYK5-62wKx4ITYt6vU21-d-85Bz5wObKHUnJQQ5rud7B5hErss-dhaebZhgVB7XsYiPYAtlrTFiGUv-MoZDXN4zJ3XcxcvvGh5AUq5_4lHqJrbs5wWnVo1ZfpXLlEHIJfMSC_l0LhmtZTw4hBjx_R8L4kOysgBz9kvE6INX2Yb0scLNpy4wt5AnRjGt1w0Pb-sZY6MHbD1qbc-GiBwqnP7pXstkejOxsNx6-xoNXK4GVkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی از اسمش مشخصه، باید برای ملت باشه، من نمی‌تونم رو این تیم، پسوند ملی بزارم، یه مشت آدم منفعت‌طلب جیر‌ه‌خورن که برای ۱۰ دلار بیشتر ناموسشونم در اختیار ج.ا می‌زارن همونطور که تو ۲۰۲۲ وقتی مردم داشتن کشته می‌شدن اینا دنبال حواله خودرو بودن.  آخرین باری…</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/news_hut/66232" target="_blank">📅 02:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66231">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
#فوری
؛ترامپ:
ایران موافقت کرده که هرگز سلاح هسته ای نداشته باشد.
همچنین ادعایی مبنی بر اینکه واشنگتن مبلغ ۳۰۰میلیون دلار به ایران پرداخت میکند جعلی است و توسط دموکرات های احمق تبلیغ شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/news_hut/66231" target="_blank">📅 02:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66230">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
صف ایرانیان مقیم آمریکا برای دریافت تیشرت مخصوص ورود به استادیوم که تصاویر جاویدنامان انقلاب دی‌ماه روش حک شده  @News_Hut</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/news_hut/66230" target="_blank">📅 02:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66229">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d10adb291f.mp4?token=KHFr8hLxwvVeO8mzIncHSxobUlVxPsGOEZ-tbsdDq57oAjg_gy98M83hpoDXvrOhriCLlgGTdjaVqMfGl4bB_d3nXN4PJbKcL8SbrdFABMHKlu6d5cBlcAvaSMEAB4byAcii7wvuSzufUlGuZd0RudfN53HWB1LsZWUJI2C0hjSiS88SggaS-WA3i8VXbqfKaI1y7bmAhcGgmYGunNNWxyybNlzv7P2RsyyOlcgFwa3qN9VbGtcXPoG1xfi_zudEWtBY4-nJhBV86ac5FVfGaE1zZCShq63LF64zCEj_bT7T0JAs_Nfih5pkSkrvvP2fMz8syeEe807q3d7sQcHjYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d10adb291f.mp4?token=KHFr8hLxwvVeO8mzIncHSxobUlVxPsGOEZ-tbsdDq57oAjg_gy98M83hpoDXvrOhriCLlgGTdjaVqMfGl4bB_d3nXN4PJbKcL8SbrdFABMHKlu6d5cBlcAvaSMEAB4byAcii7wvuSzufUlGuZd0RudfN53HWB1LsZWUJI2C0hjSiS88SggaS-WA3i8VXbqfKaI1y7bmAhcGgmYGunNNWxyybNlzv7P2RsyyOlcgFwa3qN9VbGtcXPoG1xfi_zudEWtBY4-nJhBV86ac5FVfGaE1zZCShq63LF64zCEj_bT7T0JAs_Nfih5pkSkrvvP2fMz8syeEe807q3d7sQcHjYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
صف ایرانیان مقیم آمریکا برای دریافت تیشرت مخصوص ورود به استادیوم که تصاویر جاویدنامان انقلاب دی‌ماه روش حک شده
@News_Hut</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/news_hut/66229" target="_blank">📅 02:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66228">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mz-NZEHdMGYhN-6RNqZbSJZHteGwrki6RrCPFyfpkJbCOnyMCIQ-HVJwJe4XzvMQzUiBAT6SYUs4ERdk340QlGHehZ4dUGWI7KXBkXHgq1_VHLzS7mArmqx52h7r-NUrgL3ZrGbM6b-ZDW6ECnufPGAaNdz_KqF-4wprAZYEJtdCPzKaHDMCyvw6dYTxS4XXcxglJUSdchyn4U3BxU8_R_FqgI0OmbPCiwLSDgPxKlXLU2QrUcrnq8kHkN3Rn2ScYVl9geS-2VyK1gFhTrG-8CZHhNbVtIy9DyZKIIOG-Hn3F5OYLZsoHSlJI-Gc1f13Udcxe5w_A1PIXfdEbnb6dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
رتکلیف، مدیر سازمان سیا، به رئیس جمهور ترامپ و دیگر مقامات گفت که اطلاعات جمع‌آوری‌شده توسط ایالات متحده، تردیدهای جدی در مورد تمایل ایران به دادن امتیازات هسته‌ای مورد نظر ایالات متحده در هرگونه توافق نهایی ایجاد کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/news_hut/66228" target="_blank">📅 02:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66227">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIrx_RLAAWNdAL09Pwnu07XU5tQJQMKWJMkCv187gPpTBWnI9y1Ji_Jy-pX4KI08QCl5DGi8v-3uVu75hQ1jpInHmLIbGDMYfr5nUectBTBjjEv6XtFLjM5UsZoUCYl5SMKNAWwLEToE5ECl4hRrLO-3YuqxAHr6Wy90pWJgA-nGN5eq6GLylpGYntdjij6NIppenYCzncPFJ86A-cfNiHaCNnAL7cV8FIGuZGLnvj43xixss11HZGe1-DjkiPYtvbVh6M7i4ZDWCuK52MxDNTzXp0FXLfWQWvjVXIE5vtpCItBWCg9RHHmVCYnWgrsZ0YVxjyUjF1xXlzUS2EchLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فاکس نیوز:
نیروی هوایی ایالات متحده روز دوشنبه اعلام کرد که معتقد است هشت خدمه در پی سقوط یک بمب‌افکن B-52 اندکی پس از برخاستن در پایگاه نیروی هوایی ادواردز در کالیفرنیا کشته شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/news_hut/66227" target="_blank">📅 02:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66226">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‼️
ونس به سی‌ان‌ان:
یادداشت تفاهم با ایران حدود یک صفحه و نیم است و به همین دلیل یک سند عمومی محسوب می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/news_hut/66226" target="_blank">📅 01:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66225">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c31d4a9328.mp4?token=ueD3kX2QDPvGH6GPTcXtxx-L4KsTkgyFL8FdQ5j-tJOXyagtB0mrYgu_E3q7xYlzNtuPQaEvMxTTHZ1hVmGXffUofMzxVYtO05ArHgPhhmZZreMQoAah3hGn9Vh88-ByQtXfKhCXakd0xGjK3VarWZdSWVCbKEGJ0m3GsVKYXPdWLd1E6rwBORwPN8865bzOF6_mUdM1ho3amNxMM6yOLlqf5vz3XfDrrcw0aJEw_XjJvgzDp1wiSuRrZdaw60i7pxiFRs-qE2VciAv4MhcDLFQ0ecqa2s07p2Y1vtqZ2PDy-twWTUDKTbqP_e4EHlminkLTeGRmyX2DyWyxkykBlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c31d4a9328.mp4?token=ueD3kX2QDPvGH6GPTcXtxx-L4KsTkgyFL8FdQ5j-tJOXyagtB0mrYgu_E3q7xYlzNtuPQaEvMxTTHZ1hVmGXffUofMzxVYtO05ArHgPhhmZZreMQoAah3hGn9Vh88-ByQtXfKhCXakd0xGjK3VarWZdSWVCbKEGJ0m3GsVKYXPdWLd1E6rwBORwPN8865bzOF6_mUdM1ho3amNxMM6yOLlqf5vz3XfDrrcw0aJEw_XjJvgzDp1wiSuRrZdaw60i7pxiFRs-qE2VciAv4MhcDLFQ0ecqa2s07p2Y1vtqZ2PDy-twWTUDKTbqP_e4EHlminkLTeGRmyX2DyWyxkykBlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه ای خطاب به قالیباف و عراقچی
🤣
:
@News_Hut</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/news_hut/66225" target="_blank">📅 01:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66224">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b930a8766.mp4?token=E-jd5b7twkM8Zx4HDkWmYAzJBs-o6qKMC3RNXSlOfX1tltpBYzjl5AOs_8b-IWWuOaxSr5GOEkfu2-iHf3_eRqdMLkxQVH8ibnJh-dAbiYF4XJinYZElAWdV_8FIhIgM886tT8Uh4O_ONQRPOtmDsJvPhFHq5QsbpNzROGR8O5sUeCOeytiKLkc8McMq1vUWNEIu0dN_R6n_BPhRfq84ZOCADxssoRRSMh8QMk1pS36f7g7fIAJ5-oYzO6RTqDe9cbiZCME6nnbaeA_kM9lvwBX1lUNYSPX36SfHaQX6oI5EOpgcMxeMehhhItWe-_btk2rQA4HKTkhF718kEf5UcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b930a8766.mp4?token=E-jd5b7twkM8Zx4HDkWmYAzJBs-o6qKMC3RNXSlOfX1tltpBYzjl5AOs_8b-IWWuOaxSr5GOEkfu2-iHf3_eRqdMLkxQVH8ibnJh-dAbiYF4XJinYZElAWdV_8FIhIgM886tT8Uh4O_ONQRPOtmDsJvPhFHq5QsbpNzROGR8O5sUeCOeytiKLkc8McMq1vUWNEIu0dN_R6n_BPhRfq84ZOCADxssoRRSMh8QMk1pS36f7g7fIAJ5-oYzO6RTqDe9cbiZCME6nnbaeA_kM9lvwBX1lUNYSPX36SfHaQX6oI5EOpgcMxeMehhhItWe-_btk2rQA4HKTkhF718kEf5UcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حرف های متناقض اسماعیل قاآنی
😂
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/66224" target="_blank">📅 00:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66223">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/66223" target="_blank">📅 00:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66221">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromProxy MTProto | پروکسی(|•𝓗𝓸𝓼𝓼𝓮𝓲𝓷🥀•|)</strong></div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/news_hut/66221" target="_blank">📅 00:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66220">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‼️
قاآنی فرمانده نیروی قدس سپاه پاسداران:
هیچ کس نمی‌تواند در مقابل حزب‌الله در لبنان بایستد و هر آنچه از حزب‌الله در لبنان دیده‌اید، تنها نوک کوه یخ است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/66220" target="_blank">📅 00:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66219">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2752783b15.mp4?token=i7_E4logdc-FcDF9A_VlSSjmWvddgGExd0AxiWJga0mhyh4SX_2dpksXB99aczuG_o1OZJHmgxZkDprX1-UaK0PYcB523kEoUl_1Ptx7H3v2HzbuOEbS5iMXTz1b7p-xOcuUI81ps6CBskW7CaVFHtzSTj5KhrpapwTWVL69yq0VkaoFWFCmN61qHtIogsTTBlDsVwa5pDjjsnAuUr-X2xqnn50pDgnnbrnChc7nTWmvlslnulbxXwdSW_9eyjbpUMxj1UKwwbNjfzInMNLjyWLruq_yUu4KSsk-qMocB89FfIGGYiE5Ra8B0eLLdIXdJNw15LoSXgDMCsczNPT6jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2752783b15.mp4?token=i7_E4logdc-FcDF9A_VlSSjmWvddgGExd0AxiWJga0mhyh4SX_2dpksXB99aczuG_o1OZJHmgxZkDprX1-UaK0PYcB523kEoUl_1Ptx7H3v2HzbuOEbS5iMXTz1b7p-xOcuUI81ps6CBskW7CaVFHtzSTj5KhrpapwTWVL69yq0VkaoFWFCmN61qHtIogsTTBlDsVwa5pDjjsnAuUr-X2xqnn50pDgnnbrnChc7nTWmvlslnulbxXwdSW_9eyjbpUMxj1UKwwbNjfzInMNLjyWLruq_yUu4KSsk-qMocB89FfIGGYiE5Ra8B0eLLdIXdJNw15LoSXgDMCsczNPT6jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
شبیه سازی سیستم عوارضی تنگه هرمز:
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/66219" target="_blank">📅 00:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66218">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f287535d76.mp4?token=OnNR5opWUHZBrxNunIiqRiOAU1AHZl0NvS3bAtzwrH4Bn1jtZk2TPN-uMS2SIt6_ZznccGwYqf26AOYvp_qczbk7Koq-I-QdkvfUEmyjXMfYL_yN2j0R18PACqB6PJcSl7YGsEiU075X47K_NFeZWcV_1F3WwOdUdBkGBkZop6JcbaMylqDQkPI9f7v5a8uTw1KJ_GfmV2XNXRcgqQ2IQqlqbmG8cpNGay69Aw8T767psTqMeVJKyJ3TGhXvHOCqa7uXWfwzNQ-h3Srs7Hl_q-LNbueGAl6Ef0RD2SQmNE3YGQpmeulqPSQc4DSVlHyMG1a5m0UIYuHB49j8u979zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f287535d76.mp4?token=OnNR5opWUHZBrxNunIiqRiOAU1AHZl0NvS3bAtzwrH4Bn1jtZk2TPN-uMS2SIt6_ZznccGwYqf26AOYvp_qczbk7Koq-I-QdkvfUEmyjXMfYL_yN2j0R18PACqB6PJcSl7YGsEiU075X47K_NFeZWcV_1F3WwOdUdBkGBkZop6JcbaMylqDQkPI9f7v5a8uTw1KJ_GfmV2XNXRcgqQ2IQqlqbmG8cpNGay69Aw8T767psTqMeVJKyJ3TGhXvHOCqa7uXWfwzNQ-h3Srs7Hl_q-LNbueGAl6Ef0RD2SQmNE3YGQpmeulqPSQc4DSVlHyMG1a5m0UIYuHB49j8u979zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عراقچی:
جمعه در سوئیس تفاهم امضا می‌شود و پس از آن اولین دور مذاکرات بعدی را خواهیم داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/66218" target="_blank">📅 23:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66217">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">تو فاک بت یجوری وین میدن انگار بت زدن ساده ترین کار دنیاست
🔥
از جام جهانی تا تنیس های کصشر دنیا !  هیچ فوتبال و ورزشی و از دست گروه انالیز حرفه ای ما در فاک بت در نمیره !
💵
@FutballFuckBet
💵
@FutballFuckBet
💵
@FutballFuckBet</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/66217" target="_blank">📅 23:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66216">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYncUEsVXN98Z9dmhbrV5Fv7eNI-x6opyK4rGyylb2MwYmjQYhFF5at473KHQUXYRnP4C54coO8_-Wckev37sjYX_XOfLi42AB_peVEoCMAlrqccT-tpnNoKqdLV9Q20BrZV1cYeqrr84H8c_RbTt5qUNbsaz61qrSjWLLysD9jsFV-aUb4Fg5c2Sbiak8KD9vlcEiNoCR3l4z7bTIAoolhbRx9jdUHUsnHq3BiosHDUad2L7OCn0E4JwpFfGqaHhXrIKYBsATUqnh7kFcRrSMtLdVFMMFSZ6_466IH1TdtNSMFYD-OFvTPhWOT1xGfa49khibHWYKbjuqO433z7vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو فاک بت یجوری وین میدن انگار بت زدن ساده ترین کار دنیاست
🔥
از جام جهانی تا تنیس های کصشر دنیا !
هیچ فوتبال و ورزشی و از دست گروه انالیز حرفه ای ما در فاک بت در نمیره !
💵
@FutballFuckBet
💵
@FutballFuckBet
💵
@FutballFuckBet</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/66216" target="_blank">📅 23:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66213">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PA0Eyc_w-ODFVcjTKLqZlKLnpoZYaYxPzLd3jU4LmWsvElV_52fRdJKpcY4GzV2V2aJVrSVBwOFvYZN8L2NZvFytsZS5t1pOz0mai7B6xz8iwnqrd-M1QNCt5XQkbTlFB2Sfmmt-ek3FakWHd1MBYkl20myCWoy-vbju6H6kIY9A3qfHr7YzAsr0YsY-SDZ6DkhzVsQsCZb6uzfkgJ9PLpotLGdFDKotr0tj5XW-6BmulcOtVUikLAoE9PPXIVwc0d_ADu3uVlJUveLCCSQlLUpSwstSAcN5Z-NNJA20TjVcIbeuFRDJ3uhyT4LsWuDEGnbSDbjWauoCnXCeA6OJ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e2Tbkwx1mL37p63biNJJYlZ5LWlZXCEW5Obxd87vmbUtg7uGxIMQUJPRODAogAqNgPVXZzn0inEAQ7_Kh646vA8oLw5GVGobvmQZ-_5qWH1cHfljtf6DbJalMhfukZPM-y9ydJH61149Du1mm3_07imPkB6UzJ2g9Ma7dPmrbcG2HLPSy71nGVZuMlIae-oEDAa3CVmN-5tt78roEKGx_ABzswbyzcrpOu2pYjEAMuNrPZ0KocYeGfjV3X46ANw-y7-3AFtalkUKY87ypilLI34_10YetBPiA9ovdGna42nQTUXqzd3YPvpI0xtr5FBr9QZWSGsnyo1bxMQVAOvLjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df8fefe1cb.mp4?token=S_e2H4c9NxJ9aLZXUXujXdWIqt_OSI9brE1_dPAs1Z9S37YTAFkna--CKl6XByGeVmJdpJ2aGZeqnGZXQLO5a5gsYrfiSLyCGc__dgI3GGZv6qDYzSjjGSyIwqqBeKEeFgyFSEO46S7cDpWlENqyRBbKzW_qP0F5SUUUKgWcsLtRz63YR0xOUc4VnAvtoX7GR24Jg36ReFHb2serbC37lbHa3hCoX_93ZC5uvS3N8dKEDaZHo50xdNWAhwNzQUKgkqKYsDnHQLmpi_LUuoSAysq9uGcDcGTcEoqjbeiVaefk9KbwGpMVAUVVucPbuB3oz3HTDLvLUkEeJhyn7VN7xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df8fefe1cb.mp4?token=S_e2H4c9NxJ9aLZXUXujXdWIqt_OSI9brE1_dPAs1Z9S37YTAFkna--CKl6XByGeVmJdpJ2aGZeqnGZXQLO5a5gsYrfiSLyCGc__dgI3GGZv6qDYzSjjGSyIwqqBeKEeFgyFSEO46S7cDpWlENqyRBbKzW_qP0F5SUUUKgWcsLtRz63YR0xOUc4VnAvtoX7GR24Jg36ReFHb2serbC37lbHa3hCoX_93ZC5uvS3N8dKEDaZHo50xdNWAhwNzQUKgkqKYsDnHQLmpi_LUuoSAysq9uGcDcGTcEoqjbeiVaefk9KbwGpMVAUVVucPbuB3oz3HTDLvLUkEeJhyn7VN7xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گزارش‌ها از سقوط یک بمب‌افکن استراتژیک B-52 آمریکا در کالیفرنیا خبر میدن.
این بمب‌افکن دقایقی پس از برخاستن از پایگاه هوایی ادواردز دچار سانحه و سقوط شد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/66213" target="_blank">📅 23:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66212">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMain Online پشتیبانی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6_H1GloIOqtez2dFGZIDMzRX8fy45E5YVtCJ31aeyP4cJJcSBnshunbm56NQ0ytyCuoDXyFkkYxHpbf-rtvJeIZOe4_OBd1KfZkuMiZkBiudjtKixu4TbdLS1jLDtF5QepWw1-eAQdm25qKBRnYzEeq3C8A33S6lnsDxfkXv55rTjKhru9mYWR7DMS-fPSGdO-Qw0I2vMLzPvmfedHYEcNkyvTWmJNbezgq95ZGfHqjfYVQ3vkWUH4Lh8w43bzzJgx2X2vtdY6WFAPygRhCB7iviJz_3W7dXO8wTEQVEWXYYDn5azULryBdZKnPyG0TLrsFVvMiA7i9NTAIQOh6Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فیلترشکن فقط گیگی ۵ هزار تومان
✅
👥
| بدون محدودیت کاربر 999+ نفر
🔥
| بالاترین کیفیت یعنی تانل شده
🎁
| کد تخفیف : 50
▫️
5 گیگ 25 هزار تومان
▫️
10 گیگ 50 هزار تومان
▫️
15 گیگ 75 هزار تومان
▫️
20 گیگ 100 هزار تومان
▫️
30 گیگ 150 هزار تومان
▫️
40 گیگ 200 هزار تومان
▫️
50 گیگ 250 هزار تومان
⚠️
| تنها راه خرید مراجعه به ربات
🤖
| ربات :
@YOUPINGROBOT
⚡️
| ارزون ترین قیمت بالاترین کیفیت</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/66212" target="_blank">📅 23:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66211">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/007bf57d46.mp4?token=gUOHxxatcg_wy7AqQSTE4mPHCHxoPaU_Niw0eL_LpTc3z-ABzrLeYcXv56GXxPJk-HlifR51uT854_SsnzjCq5d029m2xhEJ2WG5nbTCDjBm-7dD3yNp90rrpnXvWkkCZ3h7QEio5w4DudJADGaV08La-2lD2R0gHdwhpuDJXg6hahebNmmiiHaar9CBBDoUCSrx9psgA1iBwi5FUUCyblNXch6juBk-4hexNtkqyLBio7SfU1I7qdtNIy35HSZAAEG4W8JNof9IjCRYUEM_fQeON4O_hVMBB9V-FMaWajlIkJImTDyPK-D7j9tBrMacn8w1oKZNLiYsRQwH6EKGmZR4B4mBY_BEfY1dwm-OdIwPyONPeWBrkJuLZsj6mEGYGaUpb-VfDiACUmTzveR8V35y28u_rz8S_tnUP501OQtHA0EOWNGgmGwlDW546nE2Pj-j9z3N_oqiWyw1iJOeySO-BoA_FyfeuYJkfQznfVRs1ZbgZ0QzTrOZ4eFcgj9rFZx_Rxx3LDYPkmrAoRfFz_1vh5_oSLo5TPooR-rVLIgHgJKkB1vr1j5qCmWfsKl5RQejXhqm8rtjjn1SzehqUEN-49XDbagKLLMQwWSy1oO48P7rVEdM51fpbzdYRQHncSusINbMI847DxtE78bjLKelqJzbNW1x3gwsH4vZi0Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/007bf57d46.mp4?token=gUOHxxatcg_wy7AqQSTE4mPHCHxoPaU_Niw0eL_LpTc3z-ABzrLeYcXv56GXxPJk-HlifR51uT854_SsnzjCq5d029m2xhEJ2WG5nbTCDjBm-7dD3yNp90rrpnXvWkkCZ3h7QEio5w4DudJADGaV08La-2lD2R0gHdwhpuDJXg6hahebNmmiiHaar9CBBDoUCSrx9psgA1iBwi5FUUCyblNXch6juBk-4hexNtkqyLBio7SfU1I7qdtNIy35HSZAAEG4W8JNof9IjCRYUEM_fQeON4O_hVMBB9V-FMaWajlIkJImTDyPK-D7j9tBrMacn8w1oKZNLiYsRQwH6EKGmZR4B4mBY_BEfY1dwm-OdIwPyONPeWBrkJuLZsj6mEGYGaUpb-VfDiACUmTzveR8V35y28u_rz8S_tnUP501OQtHA0EOWNGgmGwlDW546nE2Pj-j9z3N_oqiWyw1iJOeySO-BoA_FyfeuYJkfQznfVRs1ZbgZ0QzTrOZ4eFcgj9rFZx_Rxx3LDYPkmrAoRfFz_1vh5_oSLo5TPooR-rVLIgHgJKkB1vr1j5qCmWfsKl5RQejXhqm8rtjjn1SzehqUEN-49XDbagKLLMQwWSy1oO48P7rVEdM51fpbzdYRQHncSusINbMI847DxtE78bjLKelqJzbNW1x3gwsH4vZi0Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😔
مصاحبه با رکورددار عمل جراحی در ایران: بالای ده میلیارد خرج عمل کردم که همشو دوست پسرم میداد!
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/66211" target="_blank">📅 23:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66210">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64b5122b70.mp4?token=oBG19kfbsvrW_wZxdekFd8SLyJYUUKAW1NUuW2O8Q5zvEzzCK6lB6YHUu1yLRFelpT6gEHgViykb5s-PGhEkYXUd0OPcILwm73L5BP9Xaz4GXgXs3RSlh0aPf0Sk3VcsgIUFEXv9i51A0NtCPQd7N3jrHnwaG6IYbi0X85q37CDIl5nqI4zLgEGC8uxtBKFveccu1adMV0I9ueZA6My9PuigyEuP9d2Bdwhdaxbd4hoa1k1EXuB3vU2QKifgi52pUcXq8SNlNTCn5rSqwKeo8IcHd1g-l1xL7JYzc_NQdaXJENSPT7YxjudfyIpoEBlicKTtfZBVMrtLxpXgrWRmaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64b5122b70.mp4?token=oBG19kfbsvrW_wZxdekFd8SLyJYUUKAW1NUuW2O8Q5zvEzzCK6lB6YHUu1yLRFelpT6gEHgViykb5s-PGhEkYXUd0OPcILwm73L5BP9Xaz4GXgXs3RSlh0aPf0Sk3VcsgIUFEXv9i51A0NtCPQd7N3jrHnwaG6IYbi0X85q37CDIl5nqI4zLgEGC8uxtBKFveccu1adMV0I9ueZA6My9PuigyEuP9d2Bdwhdaxbd4hoa1k1EXuB3vU2QKifgi52pUcXq8SNlNTCn5rSqwKeo8IcHd1g-l1xL7JYzc_NQdaXJENSPT7YxjudfyIpoEBlicKTtfZBVMrtLxpXgrWRmaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ پای تلفن به دستیار نتانیاهو:
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/66210" target="_blank">📅 23:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66209">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">این BISS کد جدید شبکه سه و ورزش رو Starsat چیه شبای اول جام جهانی اوکی بود الان پریده! دایرکت بدین  #hjAly</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/66209" target="_blank">📅 22:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66208">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‏
🚨
🚨
نتانیاهو برای استقلال نظامی ارتش اسرائیل بودجه دیوانه کننده ۱۲۱ میلیارد دلاری اختصاص داد!
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/66208" target="_blank">📅 22:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66207">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">این BISS کد جدید شبکه سه و ورزش رو Starsat چیه شبای اول جام جهانی اوکی بود الان پریده! دایرکت بدین
#hjAly</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/66207" target="_blank">📅 22:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66206">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bb332cca2.mp4?token=ErNE6wkOdVnN79NlIbiZuq7XjH3cLR7OfeAYe8Xrx6ETneKAMni8nrg70zdLKMJf31hf8pw1s4DG9i0PEwc_PhrqLibDvkSj6Iruc1Fz5BeXrx_pbVvGPGyVguE-W7v1yIA_O6oTxRLsgQBkySqEkLvQy_yI3zt2NqrY9J11muQhIUwWg4iCeBQTbuevwYcG-Q0ecUtL6mPGo81nxE1z5bYxIHCDZQdrymklkXT2n3v34rgsMtDZfRpLP4xkAdSNVMODHL93bX-bJAJxqDxYd7GAAtQp1Jj-_udFtY13bskNXLzGs8SRDZdBgxmS5vQ4Pf1t2JhhvChz4MIWgwzHUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bb332cca2.mp4?token=ErNE6wkOdVnN79NlIbiZuq7XjH3cLR7OfeAYe8Xrx6ETneKAMni8nrg70zdLKMJf31hf8pw1s4DG9i0PEwc_PhrqLibDvkSj6Iruc1Fz5BeXrx_pbVvGPGyVguE-W7v1yIA_O6oTxRLsgQBkySqEkLvQy_yI3zt2NqrY9J11muQhIUwWg4iCeBQTbuevwYcG-Q0ecUtL6mPGo81nxE1z5bYxIHCDZQdrymklkXT2n3v34rgsMtDZfRpLP4xkAdSNVMODHL93bX-bJAJxqDxYd7GAAtQp1Jj-_udFtY13bskNXLzGs8SRDZdBgxmS5vQ4Pf1t2JhhvChz4MIWgwzHUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
خبرنگار: چرا ترامپ مانند بایدن عمل کرد و چنین توافقی را امضا کرد؟
نتانیاهو: من این مقایسه را نمی‌کنم.
ما هنوز نمی‌دانیم توافق چه خواهد بود.
همچنین نتانیاهو درباره انتخابات گفت که قصد دارم نامزد شوم و همچنین قصد پیروز شدن را دارم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66206" target="_blank">📅 22:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66205">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
نتانیاهو درباره توافق ایران ترامپ:
این توافق توسط ایالات متحده، توسط رئیس جمهور ایالات متحده، حاصل شده است و او معتقد است که می‌تواند هم به نظارت و هم به برچیدن برنامه هسته‌ای دست یابد.
گفتم: این تصمیم اوست. تکرار می‌کنم: این تصمیم اوست. او آن را رهبری می‌کند.
البته، من نظراتم را در گفتگوهای مختلف بیان کردم.
از سوی دیگر، گفتم که ما منافع خودمان را داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66205" target="_blank">📅 22:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66204">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
نتانیاهو:
ما ضیف، هنیه و بسیاری از رهبران حماس را کشتیم ، تقریباً همه آنها را.
فکر می‌کنم هنوز یک نفر باقی مانده است؛ او هم کشته خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66204" target="_blank">📅 22:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66203">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
نتانیاهو:
در ایالات متحده، می‌گویند که رئیس جمهور ترامپ هر کاری را که من بخواهم انجام می‌دهد، و در اسرائیل، برعکس می‌گویند که من هر کاری را که او بخواهد انجام می‌دهم. بنابراین این درست نیست، و این درست نیست.
این رابطه بین شرکایی است که مدت‌هاست یکدیگر را می‌شناسند.
بسیاری از اوقات ما موافقیم؛ گاهی اوقات نیز مخالفیم. این در بهترین خانواده‌ها اتفاق می‌افتد
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66203" target="_blank">📅 22:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66202">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
نتانیاهو:
من نگفتم هدف ما سرنگونی رژیم ایران است
بلکه گفتم که می‌خواهیم به ایرانی‌ها در انجام این کار کمک کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66202" target="_blank">📅 22:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66201">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
نتانیاهو رسما اعلام کرد که عقب نشینی نخواهد کرد؛ نتانیاهو، در پاسخ به یک سؤال:
«جمهوری اسلامی می‌خواست ما از جنوب لبنان عقب‌نشینی کنیم، اما من بسیار، بسیار، بسیار قاطعانه امتناع کردم—و ما این کار را نخواهیم کرد»
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66201" target="_blank">📅 22:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66200">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
نتانیاهو:
ترامپ توافق را با جمهوری اسلامی منعقد کرد و این تصمیم اوست و ما منافع خود را داریم
آمریکا به تصمیم ما در مورد منطقه حائل در لبنان احترام می‌گذارد.
روابط ما با ترامپ مبتنی بر مشارکت است و نه بر اساس تصمیمات تحمیلی
ترامپ رئیس جمهور آمریکا است، من نخست وزیر اسرائیل هستم - من از منافع خود دفاع می کنم.
مواردی وجود دارد که من و ترامپ با هم اختلاف نظر داریم.
مهم است که از منافع امنیتی اسرائیل به طور متفکرانه و مسئولانه دفاع کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/66200" target="_blank">📅 22:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66199">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/349807e03a.mp4?token=DEdy2cXzf288V5skbmWDY5QmOJQX76QCHzesEFeErw5d_yz_SNQdpBrb1jwBx8VtXIAFlvXWwMOmyvlGqGcr6iIbIexjIgZpDYxxwT-5VbRwCU0_nffRpqVYX8H8QxMV7wr0Cq3Uyeob7rZ4GRE5iNrWLhlz-ff2UEjuh5THbKK5yZcWZ2NDZocxuvWpRnVAaf0ewjUkIu2GkXsVLl1sy_R90RR69POONMtx2J4sTpGg9BReCODDknPDJRNFdI8EJoSFEyxty2pFS5AC3DdGq9JeL9g3zuZ4At7BsEX0E7FNruJmkdxPMp3Hp7Kcht0qPnxbsd6NMYnVCcL0e-uLbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/349807e03a.mp4?token=DEdy2cXzf288V5skbmWDY5QmOJQX76QCHzesEFeErw5d_yz_SNQdpBrb1jwBx8VtXIAFlvXWwMOmyvlGqGcr6iIbIexjIgZpDYxxwT-5VbRwCU0_nffRpqVYX8H8QxMV7wr0Cq3Uyeob7rZ4GRE5iNrWLhlz-ff2UEjuh5THbKK5yZcWZ2NDZocxuvWpRnVAaf0ewjUkIu2GkXsVLl1sy_R90RR69POONMtx2J4sTpGg9BReCODDknPDJRNFdI8EJoSFEyxty2pFS5AC3DdGq9JeL9g3zuZ4At7BsEX0E7FNruJmkdxPMp3Hp7Kcht0qPnxbsd6NMYnVCcL0e-uLbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏نتانیاهو:
ما تا زمانی که لازم باشد برای محافظت از کشور اسرائیل در «مناطق امنیتی» مختلفی که تصرف کرده‌ایم، باقی خواهیم ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/66199" target="_blank">📅 22:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66198">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e33dfcb5d1.mp4?token=nLBQelRDRhUCeqagUZb5KWL_EiNOZqgH1y9S77FbbQlBmElvMXP2HQTPZ1cyXeewPj_qgU7ap-CUdnrz5XfFFfPJyQ2rpUmokT1xDiBc3o5NhRs6eje9HthdfmuNmKQRVede2MVeX6mP5pd1j0tCikrxp09TWErrNTwg6pSQLx7i2jtAUqdwvy5KCUQEZXXhxbKio2xiaInQhaM4xgHV_YAoB37L_bttltlO4NzJ-ZdSyemGeEwJU0ctlF0f3Hzr_wFyV5vmsUppWczO_cziKIPJTotf3M-JAHJLSeJgm7JvSlHEt9GqudTya7ZTNTPS9xrg3fy_hJN3x_GRIHgEJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e33dfcb5d1.mp4?token=nLBQelRDRhUCeqagUZb5KWL_EiNOZqgH1y9S77FbbQlBmElvMXP2HQTPZ1cyXeewPj_qgU7ap-CUdnrz5XfFFfPJyQ2rpUmokT1xDiBc3o5NhRs6eje9HthdfmuNmKQRVede2MVeX6mP5pd1j0tCikrxp09TWErrNTwg6pSQLx7i2jtAUqdwvy5KCUQEZXXhxbKio2xiaInQhaM4xgHV_YAoB37L_bttltlO4NzJ-ZdSyemGeEwJU0ctlF0f3Hzr_wFyV5vmsUppWczO_cziKIPJTotf3M-JAHJLSeJgm7JvSlHEt9GqudTya7ZTNTPS9xrg3fy_hJN3x_GRIHgEJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
نتانیاهو:
ما آسیب عظیمی به اقتصاد ایران وارد کردیم؛ برخی این خسارت رو یک تریلیون دلار تخمین میزنند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/66198" target="_blank">📅 22:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66197">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3fc5d08d.mp4?token=AI1rqTFv1YkDW1gE0wFoqxebO_zBKcJtDvDL8RM_849zr7B9qVejlB5AuLsbAHWb0OKhYBm-9m3eVH2Hh-1Id3NK8xfpXdOfdEgU4YqTaYDDhR98qxgoycNsuU1uaqt-7NmSlnsj0WQ4X6_RQO9WXy8ELXygzVp9KfrW02hAKt1pHg3yp3mGufOu6uEun-TnZ9nfD2D5GRdpnQVToMRQAulbOlX5bk4GFD5nKR-Hq1nxveRi3tX-VVNvcv4rUSVy0AsmBZM5DqzSAHqvir5F6aHhtDVMwwn0JCSZ0vXV6-R94av2EIdwBrUgxCLGIY8mEb0rDHAQwKPPClLflrreTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3fc5d08d.mp4?token=AI1rqTFv1YkDW1gE0wFoqxebO_zBKcJtDvDL8RM_849zr7B9qVejlB5AuLsbAHWb0OKhYBm-9m3eVH2Hh-1Id3NK8xfpXdOfdEgU4YqTaYDDhR98qxgoycNsuU1uaqt-7NmSlnsj0WQ4X6_RQO9WXy8ELXygzVp9KfrW02hAKt1pHg3yp3mGufOu6uEun-TnZ9nfD2D5GRdpnQVToMRQAulbOlX5bk4GFD5nKR-Hq1nxveRi3tX-VVNvcv4rUSVy0AsmBZM5DqzSAHqvir5F6aHhtDVMwwn0JCSZ0vXV6-R94av2EIdwBrUgxCLGIY8mEb0rDHAQwKPPClLflrreTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
نتانیاهو:
هر زمان که لازم باشد اقدام خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66197" target="_blank">📅 21:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66196">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50e4d0c9fa.mp4?token=DlLXHVvek1KOy-zoe5zDnQ1z-OgrjWTHnwLMHEG79tRIYfhobp2c8azHoVCfexkS8mRWZ7Mes4F7IO73A_DPneJkPHxaYqP7sRq5tsfoZjYdAyHuxaBaUAAcMVmn_tODBKUdOJ2V668U-KWt-YpKoionkWdQg8NVDnCnMypIijw0zDsNQ6JBWGO9-4H578Rm2pMf7KmF26LvOMQLMMpUwD_PxCNIqrE08XeUm-KJNJ2RevQTTbeGhzyfDrIAcO0urMdn_c7kiEZMKluotNdtZ9DK3t3YmbRAmZRJdOd9YFlsB-LOhrzIInFB7egIb9Te9YfsAEQ7r9YeZm1gTDPDBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50e4d0c9fa.mp4?token=DlLXHVvek1KOy-zoe5zDnQ1z-OgrjWTHnwLMHEG79tRIYfhobp2c8azHoVCfexkS8mRWZ7Mes4F7IO73A_DPneJkPHxaYqP7sRq5tsfoZjYdAyHuxaBaUAAcMVmn_tODBKUdOJ2V668U-KWt-YpKoionkWdQg8NVDnCnMypIijw0zDsNQ6JBWGO9-4H578Rm2pMf7KmF26LvOMQLMMpUwD_PxCNIqrE08XeUm-KJNJ2RevQTTbeGhzyfDrIAcO0urMdn_c7kiEZMKluotNdtZ9DK3t3YmbRAmZRJdOd9YFlsB-LOhrzIInFB7egIb9Te9YfsAEQ7r9YeZm1gTDPDBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
نتانیاهو: ما در لبنان خواهیم ماند.
کار با ایران ممکن است همچنان تمام نشده باشد
ماموریت زندگی من مبارزه با برنامه هسته ای ایران است.
با توافق یا بدون توافق، ایران سلاح هسته ای نخواهد داشت.
اگر برای حمله به ایران عجله نکرده بودیم، به بمب هسته ای دست می یافت.
ما رهبران ایران را کشتیم، به سرویس‌های امنیتی آن آسیب شدیدی زدیم و اسرائیل را از تهدید هسته‌ای ایران نجات دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66196" target="_blank">📅 21:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66195">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
درگیری شدید طرفداران تیم ایران با مخالفان تیم قلعه‌نویی در لس‌آنجلس ساعاتی قبل بازی
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66195" target="_blank">📅 21:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66194">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0695d77536.mp4?token=GbBt819Ly5cmRSLuEz6ELuMvWHiRx22gICb1XV9q81ITAaInYVU_lhPJ-AgJWoYy1U7VBFDFa0F2R6RRLS_CsoEkylUxj7aBmUDKfWZgoS9zwbCli8y4_rCkvfAzPYwNk32YSoJYJVf2ss1CBIza-ltnMHTtolCc57bAIjkOzRBFRJwJirpEimx_s2-yi3t_8cOiuMvhLStzgxNflONPBOKqamYJah4Qc1wymKLVvk1ZM_cEnt0Jjw6WVIcYgsJ9zTdPE8yV15KCIDyUVYA7Fl9bFH2ZQ6qlkjzt-TUnRODS19L4EExztMGSmKGM-G3rtJ7cNS-3WHx6daCfTJIlbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0695d77536.mp4?token=GbBt819Ly5cmRSLuEz6ELuMvWHiRx22gICb1XV9q81ITAaInYVU_lhPJ-AgJWoYy1U7VBFDFa0F2R6RRLS_CsoEkylUxj7aBmUDKfWZgoS9zwbCli8y4_rCkvfAzPYwNk32YSoJYJVf2ss1CBIza-ltnMHTtolCc57bAIjkOzRBFRJwJirpEimx_s2-yi3t_8cOiuMvhLStzgxNflONPBOKqamYJah4Qc1wymKLVvk1ZM_cEnt0Jjw6WVIcYgsJ9zTdPE8yV15KCIDyUVYA7Fl9bFH2ZQ6qlkjzt-TUnRODS19L4EExztMGSmKGM-G3rtJ7cNS-3WHx6daCfTJIlbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نه جنگ خواهد شد نه مذاکره خواهیم کرد
😂
.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66194" target="_blank">📅 21:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66193">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8zPNpd888jJcWKyVa-BvyGJmEhmuNkGOs7IiwOBVwZXLWCC0pOi85bg26pCoZfScEJj4DYE8xieeaT1GQkbIPzSMkojoo3_z7uU8QfPTlFE5z79QBg96C84coAR-J9-0lU5WPxBpB2cJl25oHzBXweDBF65HPXtNyuHTq24qqhn1AbDDv3HH802wToRpe6cOPAdEGpKrPouGsxp8TF0CcIB4nd7u8N94iH0wqaxDpSrAiHd3Ba7IuNADIxpi5vGuS60lOR8piKkSPt_SozZfpTBprUBjCeNBQdg_RmOgn9uW6ILDW4gQfzENKPpnaGqoZErWRFBXRd6cmlSgPLYlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درآمد از تلگرام بدون نیاز به ممبر و تولید محتوا؟
سیستمی به اسم MTP وجود داره که باهاش میتونی وارد پروژه‌های واقعی بشی و درآمد کسب کنی.
✅
بدون نیاز به ممبر
✅
بدون نیاز به فالوور
✅
بدون نیاز به تولید محتوا
✅
شروع سریع
✅
آموزش کامل و پشتیبانی
🎁
فقط برای ۳۰ نفر اول:
سه پروژه اولیه بهت داده میشه
مبلغ هر پروژه ۲۵ میلیون تومنه
یعنی از همون ابتدا امکان رسیدن به درآمدهای بالا برات فراهمه
اگر میخوای جزو ۳۰ نفر اول باشی، وارد کانال شو و شمارت رو ارسال کن:
👇
👇
👇
https://t.me/+QpsFnjSfC382MGQ0</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66193" target="_blank">📅 21:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66192">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24683d102e.mp4?token=GbvLkpfyXuft6_xw2vvrhBi5Vp3ODSqhov-lgUP4j1d6IGcNnGMZwCyq39ALZ8sZuN7zYd1MrEpza2G_RnLCGDgimkS6isWMLfi-OWWTc11NKvmKW2RP3ocpnQEyiBHRjcMHYDPEnXDNENIQdCLK74_5-_KaIP5d6uwG6w866N2z8WUuULGQLDryaCqBNIYdtENhfGfWHAJ1vO2kTare13bJn4zr8XR4jsZJJH-eLz8mpzjkpmgwYwaqpFw2hInkCGaviNH2sM_gAKDn6ZgA0CzsyFy-LnmlpTgNYURON8X1ORgAmN7rlV4KRiYTYq89drXgsmtedTwpVc7d2ipf-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24683d102e.mp4?token=GbvLkpfyXuft6_xw2vvrhBi5Vp3ODSqhov-lgUP4j1d6IGcNnGMZwCyq39ALZ8sZuN7zYd1MrEpza2G_RnLCGDgimkS6isWMLfi-OWWTc11NKvmKW2RP3ocpnQEyiBHRjcMHYDPEnXDNENIQdCLK74_5-_KaIP5d6uwG6w866N2z8WUuULGQLDryaCqBNIYdtENhfGfWHAJ1vO2kTare13bJn4zr8XR4jsZJJH-eLz8mpzjkpmgwYwaqpFw2hInkCGaviNH2sM_gAKDn6ZgA0CzsyFy-LnmlpTgNYURON8X1ORgAmN7rlV4KRiYTYq89drXgsmtedTwpVc7d2ipf-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
آخرین مکالمه ترامپ و نتانیاهو بعد توافق:
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66192" target="_blank">📅 20:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66191">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a708e029d7.mp4?token=sspYWlQQuttdVPFj-AhQ2AUIqksIluIuY3qjMHGLbLIysiFLeR16MZmOVJWeUaOs3zpnip6xDMlu4kh9kk-Um6RmOq5cYikeX56vhfyj1okheOemNRa7CafDkxf3MUXCcmpYw16_tp9b5Tr-w3ZbFUDLC7tBeKsQ1ouDIlYhGTonNG_rlTt5xioLqLwYEUmG9Db5PF0wJDtHePLAiWNLt1FxjcObnsxlwRwpIOKgM13ucKD241ra-w5OgoKT5wegvhweCEv_6jSGdSG_3ilAi5RR31jQB5p5Mdfi8DbMfGRBBFs5ymVfyDeuimNnaKilPNmDOfSvD9acfIWpD-FLOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a708e029d7.mp4?token=sspYWlQQuttdVPFj-AhQ2AUIqksIluIuY3qjMHGLbLIysiFLeR16MZmOVJWeUaOs3zpnip6xDMlu4kh9kk-Um6RmOq5cYikeX56vhfyj1okheOemNRa7CafDkxf3MUXCcmpYw16_tp9b5Tr-w3ZbFUDLC7tBeKsQ1ouDIlYhGTonNG_rlTt5xioLqLwYEUmG9Db5PF0wJDtHePLAiWNLt1FxjcObnsxlwRwpIOKgM13ucKD241ra-w5OgoKT5wegvhweCEv_6jSGdSG_3ilAi5RR31jQB5p5Mdfi8DbMfGRBBFs5ymVfyDeuimNnaKilPNmDOfSvD9acfIWpD-FLOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ: توافق شامل هیچ‌گونه تسهیل زودهنگام تحریم‌ها برای رژیم تروریستی جمهوری اسلامی نمی‌شود.
ترامپ در پاسخ به پرسشی درباره احتمال کاهش یا تعلیق زودهنگام تحریم‌ها علیه رژیم تروریستی جمهوری اسلامی تأکید کرد چنین موضوعی در توافق وجود ندارد و افزود این مسئله در نهایت به رفتار رژیم تروریستی جمهوری اسلامی بستگی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66191" target="_blank">📅 20:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66190">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66190" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66190" target="_blank">📅 20:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66189">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUUani3EnjYN7oO7fGoXQh9rEKUk7ODbNIiHkvLSIPAZWptDNb3VEN3D_KHBKkNvGaAX3z-R__RgpPppobF-tUjTYsz2dEeErweBUaHmgHqg77uObPCU4Bq9LbVxgufaYcq3vPN2iso_-ei8_AmxsPqB7aHGhEEPk_rzHYxcYqk5K-GLVwP6_w_ezuz7xl_twuocdmJnonzhV60gRR46ScwGK_dDD9e_Z8ASIIRCTUtdS1Vqu3joeCzMwBtGRwvIO1H_UUCXTvKPJ9rmfqqqBNYOlQpYBnnLH_UYqakKfRim3KtU5AQvfaQ_amReRKZ7mLt_CcGeE9j6HfMsq5YG6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66189" target="_blank">📅 20:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66187">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27ad63d98d.mp4?token=eU9dwYb8RrEPUOiX2l83HynWFkl6kNd2jkzv_8-poxUIGs6XKVn4As4Ywh8beIyDPuU7ncnLgy_AYluMRu-G8voXkUf6JBKcctK6_AmZQkArrKoPe2t_irv1v95r_onjLhVT3QIRJ4qU_9z8jas90v-0MRKZpfOtP7IrwgvPm_S4Oka-TwKnUv9G5dFDYzTQfMirJLA5Qw8TjPNrXSZpCKsq1zv7WaypFSz49vZy3uOGXTP3d8HlFUyv9m4jdGLz9hLBhQWnPGNlKkMlu6AvEkwha3Dt46iLHJRKA1dmCWuv-yhfz5Fu80ExKwAfKBKyNykC0c9x8qPQ6oBRJkiHXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27ad63d98d.mp4?token=eU9dwYb8RrEPUOiX2l83HynWFkl6kNd2jkzv_8-poxUIGs6XKVn4As4Ywh8beIyDPuU7ncnLgy_AYluMRu-G8voXkUf6JBKcctK6_AmZQkArrKoPe2t_irv1v95r_onjLhVT3QIRJ4qU_9z8jas90v-0MRKZpfOtP7IrwgvPm_S4Oka-TwKnUv9G5dFDYzTQfMirJLA5Qw8TjPNrXSZpCKsq1zv7WaypFSz49vZy3uOGXTP3d8HlFUyv9m4jdGLz9hLBhQWnPGNlKkMlu6AvEkwha3Dt46iLHJRKA1dmCWuv-yhfz5Fu80ExKwAfKBKyNykC0c9x8qPQ6oBRJkiHXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
متن تفاهم‌نامه به زودی منتشر خواهد شد و سندی بسیار قدرتمند است
ترامپ در پاسخ به پرسشی درباره زمان انتشار متن تفاهم‌نامه گفت این سند احتمالاً خیلی زود منتشر می‌شود، زیرا مایل است افکار عمومی آن را مشاهده کنند. او همچنین تأکید کرد این تفاهم‌نامه سندی بسیار قدرتمند است و آن را با توافق دولت اوباما مقایسه کرد که به گفته او سندی بسیار بد بود. پرزیدنت ترامپ افزود انتشار متن احتمالاً در مقطعی پس از روز جمعه انجام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/66187" target="_blank">📅 20:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66186">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da891bd3ed.mp4?token=oIcpfTQ6_9_-2uwa44tgbNVETvW0ArK_67azmtdQtsj9jX9mzV3FFrIgQI68qiGN0AJZR_D5en7vGrUMzDg1nsN7tR1CJpODkLNL9rhs12o5QoYI6hYoJL40BfZA5TaVj3SK5_BxLR3jJNP-wQ3NUuk02KQbPUyL8a8sw9GWHsE4vIDgdcGM_SW6f7wmMTeQY_VpbdXPkf0uKa7o1byBNNhVIQJQv3_NFyXYHZ30Y5FM8bf5qEx1XWVqbDpP2VyrOTwnzyWFqNJfTnzRSh9tqTWVnUCTrGpgLyWEzxjsFk_Rv_Dl_GIuH8W-5XG8IRBaXgScJZUd3SA9eLWGJRbj2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da891bd3ed.mp4?token=oIcpfTQ6_9_-2uwa44tgbNVETvW0ArK_67azmtdQtsj9jX9mzV3FFrIgQI68qiGN0AJZR_D5en7vGrUMzDg1nsN7tR1CJpODkLNL9rhs12o5QoYI6hYoJL40BfZA5TaVj3SK5_BxLR3jJNP-wQ3NUuk02KQbPUyL8a8sw9GWHsE4vIDgdcGM_SW6f7wmMTeQY_VpbdXPkf0uKa7o1byBNNhVIQJQv3_NFyXYHZ30Y5FM8bf5qEx1XWVqbDpP2VyrOTwnzyWFqNJfTnzRSh9tqTWVnUCTrGpgLyWEzxjsFk_Rv_Dl_GIuH8W-5XG8IRBaXgScJZUd3SA9eLWGJRbj2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ: می‌خواهیم مسئله لبنان را حل کنیم.
آمریکا به دنبال آن است که ببیند آیا می‌تواند مسئله لبنان را سامان دهد، زیرا این بحران به نظر می‌رسد هرگز پایان نمی‌یابد. او افزود این موضوع در مقایسه با سایر پرونده‌ها نباید دشوار باشد و درباره گروه تروریستی حزب‌الله نیز گفت باید گفت‌وگوهایی در این خصوص انجام شود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/66186" target="_blank">📅 20:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66185">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46bc16471f.mp4?token=Fw779pdsyWexSNvQ3UqwjjMfqA4uZGSelXaZFy2bwCufNnbicApyhsOHI7eaJGfbSHyKSRrCY-jjgR1r5obM_569zltqtaqyw6WUbQ4DYTmcgk-ODgCFXQ9QhDIt4X_dpcXa0yBBiW7G2Gw1P8DMPdL3L9jQ8YHhTkF3iUibXIWv3rASdBnnVdY0AirzagfxJUvrseX1jK50dGryHTYHEKNkjjhoWBrT3h38YfFpHdNe_-su2OqiXGkcgfCUleFy9_EoAInr-rsCAKhhUKGBGT67l-ctf-wT4cxfCD2BqcJJFmc9bcxP8sU3OzapopdhDb8Rmvivgui2I4I7K-zrUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46bc16471f.mp4?token=Fw779pdsyWexSNvQ3UqwjjMfqA4uZGSelXaZFy2bwCufNnbicApyhsOHI7eaJGfbSHyKSRrCY-jjgR1r5obM_569zltqtaqyw6WUbQ4DYTmcgk-ODgCFXQ9QhDIt4X_dpcXa0yBBiW7G2Gw1P8DMPdL3L9jQ8YHhTkF3iUibXIWv3rASdBnnVdY0AirzagfxJUvrseX1jK50dGryHTYHEKNkjjhoWBrT3h38YfFpHdNe_-su2OqiXGkcgfCUleFy9_EoAInr-rsCAKhhUKGBGT67l-ctf-wT4cxfCD2BqcJJFmc9bcxP8sU3OzapopdhDb8Rmvivgui2I4I7K-zrUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
درباره باز بودن تنگه هرمز اختلاف‌نظرهایی وجود داشت، اما در نهایت عبور و مرور از این گذرگاه راهبردی بدون دریافت عوارض انجام خواهد شد. او افزود آمریکا احتمالاً به کمک زیادی نیاز نخواهد داشت، اما حضور یک یا دو کشتی از چند کشور دیگر می‌تواند مفید باشد و فرانسه نیز یکی از گزینه‌های مناسب برای مشارکت در این مأموریت است. پرزیدنت ترامپ همچنین تأکید کرد هیچ‌گاه نمی‌توان از تحولات آینده کاملاً مطمئن بود، اما به باور او تنگه هرمز باز خواهد ماند و رفت‌وآمد دریایی در آن آزادانه ادامه پیدا خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/66185" target="_blank">📅 20:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66184">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13b0fceee3.mp4?token=Dh7ROOuRN-GxbdC2QKe2yFprWF_iY0NpvliBuiid5X2h0Zph_ETmZDRpEdQsw0YVzsGQs-PAUZt5HWtTk_nEanyXR970zbhp_LE8iLUM5o__TDCkhOWfsezQVp7oNoQsFwjRY4I9kgx2TsMtvqVkVKVwlGTj72Y44PYtKYHm3xoFtpbDNl57DC-e4QofW-y7SGHkJAWLI7a_O4Bu1PD3lOs2L85ul_x-ERnobU0Re--5spceRIaA1G9qQYjUpHDobvVhT49wqWTuzDLae_v-HWcGGCdzaMyMpTT-AdFKL_GZ5DxLOMYIr_B5UWJzKJnU6vAnYzbQQjmm0mE9FlM0Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13b0fceee3.mp4?token=Dh7ROOuRN-GxbdC2QKe2yFprWF_iY0NpvliBuiid5X2h0Zph_ETmZDRpEdQsw0YVzsGQs-PAUZt5HWtTk_nEanyXR970zbhp_LE8iLUM5o__TDCkhOWfsezQVp7oNoQsFwjRY4I9kgx2TsMtvqVkVKVwlGTj72Y44PYtKYHm3xoFtpbDNl57DC-e4QofW-y7SGHkJAWLI7a_O4Bu1PD3lOs2L85ul_x-ERnobU0Re--5spceRIaA1G9qQYjUpHDobvVhT49wqWTuzDLae_v-HWcGGCdzaMyMpTT-AdFKL_GZ5DxLOMYIr_B5UWJzKJnU6vAnYzbQQjmm0mE9FlM0Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ درباره حضور در مراسم امضای روز جمعه:
پرزیدنت ترامپ در پاسخ به پرسشی درباره حضورش در مراسم امضای روز جمعه گفت این موضوع به شرایط بستگی دارد و در ابتدا قرار بود جی دی ونس این مسئولیت را بر عهده بگیرد. او افزود ممکن است تا آن زمان برنامه‌های دیگری داشته باشد، زیرا قرار است تا دیروقت مشغول باشد و هنوز تصمیم نهایی درباره حضورش گرفته نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/66184" target="_blank">📅 20:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66183">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/722077d2f4.mp4?token=I7n3cDq1fglB8rUOUw8aal-oG1imGeHqPGsA3lOCN7h8cP_Tnb0rtd2Wd1_FoyKNn7WTA-kASBv5o0lfsY0B0mGoM9NULacV2ohTp_8H37I2S_gVigZsxd_SOLHgJRS6izGQfZEWVdKW9pCaOLPr108KYWYNFGPdA9Y5RvZg7rGmZL7BoG4G4KrNEzyzeLhv0lwAR2HOwKrkhNtpja7RO_Ao5UlVx5jteme743AUFfGIHIJmgrFNXLQGISQGFsM7f7Exv69CFhwAGEBSi1NRTgEdpg69mEMrrO-JYyP6r2_wSGBgRh4SLMgORuA9ZFiE6mBq2XZAQ5omowCK8W7ITg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/722077d2f4.mp4?token=I7n3cDq1fglB8rUOUw8aal-oG1imGeHqPGsA3lOCN7h8cP_Tnb0rtd2Wd1_FoyKNn7WTA-kASBv5o0lfsY0B0mGoM9NULacV2ohTp_8H37I2S_gVigZsxd_SOLHgJRS6izGQfZEWVdKW9pCaOLPr108KYWYNFGPdA9Y5RvZg7rGmZL7BoG4G4KrNEzyzeLhv0lwAR2HOwKrkhNtpja7RO_Ao5UlVx5jteme743AUFfGIHIJmgrFNXLQGISQGFsM7f7Exv69CFhwAGEBSi1NRTgEdpg69mEMrrO-JYyP6r2_wSGBgRh4SLMgORuA9ZFiE6mBq2XZAQ5omowCK8W7ITg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
پرزیدنت ترامپ گفت آمریکا کار بزرگی انجام داده و امیدوار است روابط خوبی با رژیم تروریستی جمهوری اسلامی شکل بگیرد و دو طرف بتوانند با یکدیگر کنار بیایند. او افزود اگر این روند موفق نباشد، شرایط به نقطه شروع بازخواهد گشت، اما معتقد است نیازی به چنین سناریویی نخواهد بود. پرزیدنت ترامپ همچنین تأکید کرد توافق انجام‌شده با رژیم تروریستی جمهوری اسلامی می‌تواند دستاورد بزرگی برای جهان به همراه داشته باشد، زیرا برای مدتی جریان نفت در منطقه با محدودیت و اختلال مواجه شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/66183" target="_blank">📅 20:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66182">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hrr4tauXOM6GaBpMRyK_EDNB1qwQ3pNAE9nxXZW3htJlAOtq2sLYRH_wvoOOU2uUZ4Qx4Kh36yRwRqEU6BJaPK43-o1ZGnkXgqqyyvOWouORNRIXmx04RoHuop2rE_OK-JAafnveZhW8HAKWKzvrCDuStqr4BKagYlplxZkb-3duFOxRn_bV3WjWCATvdHhXIm1gJB-XVjHw22dbX8UaaIjQJLBwGkfhdiU9O-W2_zxfDjq8YhKymszyA3zS4AGdIw4PTSMB0hX3IxVLjSUD2TPqy0UYAOI3QD8C7H9mStsx4jf5jrs7L84uMw3bEH6wr9WtEF3wD8yz4gLbFiyVug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
ملت دوست‌داشتنی و سروقامت ایران! با مقاومت تاریخی شما و رشادت نیروهای مسلح دربرابر آنان که قصد جان این ملت و نابودی و تسلیم این مملکت را کرده بودند، ایران گامی بلند به سوی پیروزی نهایی برداشت. می‌خواستند و نتوانستند.
ایستاده‌ایم و در نهایت ‎
#ایران_ما
پیروز خواهد شد، به لطف خدا.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/66182" target="_blank">📅 19:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66181">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf026052c0.mp4?token=kj2u1enTqL_V9P0ioHmh1We4qWOyfFxsWQPG9D7NKAnxjWqtzqnQWxn3Ut6HzZE4JlgPh451QZ9G1WuF6k4V47sjsD4ofTRYhZG7mduDs4XsCkiN_Z105J_PRTmfmivik0EXIC-a4orOALNFZZfENraIRESisQBJ7r32Yg2gu96E-Gz7E3UpBY-Zvf9zxTrQ4QkcfkwNkA3bl2X3B-5d_aBNIVQy3y3TLJdu92Kc2wDVHwj3hucYP9DVKQzqf53Bs_2ZBrHH-b17UR-PAmshyKtE0KtRTmh_C4hMYNmMTQKB7l77W5egbEJ8yDwGg_QcTazj2T9QXC76RifeUjsPWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf026052c0.mp4?token=kj2u1enTqL_V9P0ioHmh1We4qWOyfFxsWQPG9D7NKAnxjWqtzqnQWxn3Ut6HzZE4JlgPh451QZ9G1WuF6k4V47sjsD4ofTRYhZG7mduDs4XsCkiN_Z105J_PRTmfmivik0EXIC-a4orOALNFZZfENraIRESisQBJ7r32Yg2gu96E-Gz7E3UpBY-Zvf9zxTrQ4QkcfkwNkA3bl2X3B-5d_aBNIVQy3y3TLJdu92Kc2wDVHwj3hucYP9DVKQzqf53Bs_2ZBrHH-b17UR-PAmshyKtE0KtRTmh_C4hMYNmMTQKB7l77W5egbEJ8yDwGg_QcTazj2T9QXC76RifeUjsPWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف بعد تعطیل کردن مجلس و انجام هر کاری که دلش میخواد
😂
:
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/66181" target="_blank">📅 19:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66180">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
ما هرکسیو تضمین نمیکنیم اما تیم کاویانی واقعا کارشون خوبه و دارن کل فیلترشکن ادمینای مارو ساپورت میکنن
❗️
پشتیبانی 24 ساعته
😈
همراه با تست رایگان
💵
تعرفه‌ها 10 گیگ — 170 تومان 20 گیگ — 340 تومان نامحدود — 450 تومان (ترکیه)  برای خرید بهشون پیام بدین
⬇️
…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/66180" target="_blank">📅 19:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66179">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
ما هرکسیو تضمین نمیکنیم اما تیم کاویانی واقعا کارشون خوبه و دارن کل فیلترشکن ادمینای مارو ساپورت میکنن
❗️
پشتیبانی 24 ساعته
😈
همراه با تست رایگان
💵
تعرفه‌ها
10 گیگ — 170 تومان
20 گیگ — 340 تومان
نامحدود — 450 تومان (ترکیه)
برای خرید بهشون پیام بدین
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66179" target="_blank">📅 19:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66174">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D6fIAksZz86UWQbY3VtCY6WfLXy8RdH6LGNOrIZadeWT26S-ejnw4zMaHeyMtI5Sr1RQPImyPzHTy3HdxLyiA6d9N_0eXiMfZLRGZ7Iy2Rj5oy_2bzAEq8RI6oV5syf5DBRecztsH1NI0KbdaEZGA315EOdbgHH3i_kwpiKo6tmWgF2s78qfy3pWvjBL-s0CZPImPXvjocg9kRxHpHxFGKPCNmNUg9noyBkv0kSINELhtfiy7XWDJroxrBvvHF8nK5w491q1q5CuhHijVL7ejo9NHY4xynV88AM_9FX_Br2boPQOvO2xgJKZjEr9RyqPN1N5b_vSwI5kJKVfE0vTXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DnH9YSvFSQ8M6ijebgLZwy5AA-v3aXDjsjWUybtYCgjwnb5N5WeMOKttVQ1NxNQ5fV_-TxjVWuHILU_e3ZqiyXNkxb41BHO9dqI0h6dx4cBmonJTq2Lu8AbepNpmBQcaEUVEf51-NmIEF_PueQ0Dvd1aLP6FE3OeKf0bwjMoWUik29m-m0UZc--JCRL54dlO0Andv0IJfGfmE1hhLtRx9vNV7MRIoDgyrAY8te-VNa_Sq_NS8x9SbGQc9vTifTlWdu4gWgJTfd0dDG_HVEG4clP7gU9756aBTVOX4YlLnJkfN9eTqp4X4AKR3-kQzQQde3FTqKPlPidTzP3WaVpwZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5cd54e998.mp4?token=kDcVGgK0u0dd7yt43LIyTsRksLLCWzlj7M_PZ07YG61S9mgZQBBbsn02UKthmbjMeP0zFzmLy9uXCzHHpDYLBr8r2T9kMGaAS0uGfNHIyYdHkUlynOUN2xeqIkLt_nkw9s8CVnA02a5X_zlVeERPE2bp3ZiyNdP9me1WrCVjOq_7JgWlSN6kI9EJB4GncubBvqP0IMrXkut1TPmj3XrHdQUh-Rkq_cc024AHV_Xcl686JQad2tOduiok_9PHXNBwrc-48SRwjMfH-7MayphzqXbteeqme6kx8noDRlZGIpCxfxLKl8OKlsFM3BM3YJR3H2qhgPDClJ9bXo1NQpN5JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5cd54e998.mp4?token=kDcVGgK0u0dd7yt43LIyTsRksLLCWzlj7M_PZ07YG61S9mgZQBBbsn02UKthmbjMeP0zFzmLy9uXCzHHpDYLBr8r2T9kMGaAS0uGfNHIyYdHkUlynOUN2xeqIkLt_nkw9s8CVnA02a5X_zlVeERPE2bp3ZiyNdP9me1WrCVjOq_7JgWlSN6kI9EJB4GncubBvqP0IMrXkut1TPmj3XrHdQUh-Rkq_cc024AHV_Xcl686JQad2tOduiok_9PHXNBwrc-48SRwjMfH-7MayphzqXbteeqme6kx8noDRlZGIpCxfxLKl8OKlsFM3BM3YJR3H2qhgPDClJ9bXo1NQpN5JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویری از آتش سوزی گسترده، میدان تجریش تهران
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66174" target="_blank">📅 19:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66173">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
نتانیاهو قراره تا چند ساعت دیگه سخنرانی کنه و این اولین واکنش اون نسبت به توافق هست.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66173" target="_blank">📅 18:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66172">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‼️
ونس درباره ایران:
ما کاملاً آماده‌ایم که کشورهای خلیج فارس در بازسازی ایران سرمایه‌گذاری هنگفتی کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66172" target="_blank">📅 18:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66171">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‼️
ونس درباره ایران:
ما دیروز به صورت دیجیتالی قرارداد را امضا کردیم و هیچ پولی آزاد نشده است. این موضوع تغییر نخواهد کرد،
این یک مسئله مبتنی بر عملکرد است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66171" target="_blank">📅 18:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66170">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cbb12962f.mp4?token=Lu_yAtEEugog42AlYDQjtkWIMOXJmZ5v04VSYRcS8TzrYC3IadPyLbyrb6yPLkmlWGDuaFMTmGxbewFJy04L3tfMDwPHTPnyJbDX_amVMF-47lkLUzqqKZeT91BlltQuQS1gc3fr4yWbgXwFYtafepr_isyccbSo4EPbwMoxolicCkMDj3q23Y2uq2nLOQoU1jEhlrPLiNqGWjQ35R_xDJKtHKcVL1fS3Z-vJoPbmVpHd9C6nfajlj6m6HaE4Ebzbl29koKp2ICf8XMdWlk2Ca1S6S2PJj1NhWLM2nxG81GOImyR6Yr7lByBbv_or-4XGQBez8nQHQ5Hm4FyMqskUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cbb12962f.mp4?token=Lu_yAtEEugog42AlYDQjtkWIMOXJmZ5v04VSYRcS8TzrYC3IadPyLbyrb6yPLkmlWGDuaFMTmGxbewFJy04L3tfMDwPHTPnyJbDX_amVMF-47lkLUzqqKZeT91BlltQuQS1gc3fr4yWbgXwFYtafepr_isyccbSo4EPbwMoxolicCkMDj3q23Y2uq2nLOQoU1jEhlrPLiNqGWjQ35R_xDJKtHKcVL1fS3Z-vJoPbmVpHd9C6nfajlj6m6HaE4Ebzbl29koKp2ICf8XMdWlk2Ca1S6S2PJj1NhWLM2nxG81GOImyR6Yr7lByBbv_or-4XGQBez8nQHQ5Hm4FyMqskUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ونس:
تمام ائتلاف کشورهای حاشیهٔ خلیج فارس از توافق هسته‌ای اوباما با ایران متنفر بودند، چون احساس می‌کردند این توافق به ایران قدرت می‌دهد که نقش یک بازیگر بد را ایفا کند
حالا ائتلاف خلیج فارس دربارهٔ توافق صلح ترامپ چه می‌گوید؟ آنها عاشق این توافق هستند، چون آن را فرصتی برای ساختن و آفریدن خاورمیانه‌ای جدید می‌بینند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66170" target="_blank">📅 18:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66169">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b420a810e3.mp4?token=kL7HvHxd-3nZDcnZQFef_Vul7rHmHAcMmwTCUQ6bbSvOEOPZwOaYH60OdjDu4bioOl7bnfJUqnsoCNo4zEvHU25wbCzSJQn2Jznnc1D9IZpgbVDa3s2Ff_aqpBBDaDWenJrHGyv3GHMUhMOARxGmpK7R_3XokU2sDxkFbjR4u86Mcx-hS843RfdqQPKUZKda8CPrxS8PYGNXYGyNbwpdsIaLJClIAvLY9YNqqQHHqXXYfn5sW4XxMhnSu-mXc032GOQxvmI6m2R8ogdf7Yqc8Xpw-g0tGd3O3l3ZjzqhcIbXHkqawo_fPXhbm4ho4sKTmWoNcLwht1T042Nwp29rew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b420a810e3.mp4?token=kL7HvHxd-3nZDcnZQFef_Vul7rHmHAcMmwTCUQ6bbSvOEOPZwOaYH60OdjDu4bioOl7bnfJUqnsoCNo4zEvHU25wbCzSJQn2Jznnc1D9IZpgbVDa3s2Ff_aqpBBDaDWenJrHGyv3GHMUhMOARxGmpK7R_3XokU2sDxkFbjR4u86Mcx-hS843RfdqQPKUZKda8CPrxS8PYGNXYGyNbwpdsIaLJClIAvLY9YNqqQHHqXXYfn5sW4XxMhnSu-mXc032GOQxvmI6m2R8ogdf7Yqc8Xpw-g0tGd3O3l3ZjzqhcIbXHkqawo_fPXhbm4ho4sKTmWoNcLwht1T042Nwp29rew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی‌دی ونس درباره ایران:
ما اکنون مستقیماً با نظام ایران صحبت می‌کنیم. روابط خوبی در آنجا داریم
دیگر پیام‌ها را از طریق کانال‌های پشتی منتقل نمی‌کنیم؛ در واقع با آن‌ها صحبت می‌کنیم.
وقتی با آن‌ها صحبت می‌کنید، متوجه می‌شوید چه چیزی واقعی است، چه چیزی جعلی است، درباره چه چیزی جدی هستند و درباره چه چیزی جدی نیستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66169" target="_blank">📅 18:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66168">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41a8610027.mp4?token=eRDA79guXG6-cKy5UZc9vNbyBL7cXIn4tHWPApdRu397ddmTVgAPjb_T1XVpt-HliqWnliph9KnZ2LMyF_pI1I8lKRa6gPyBc-ewism1H7N-KS-8ZAuG0rzel6clRV-FN1OK_Bvq4l5jjZ2xg2R9ttL9FyNmzmV0n-nKmpIcL3AxiOCYutoAAFCaw0dUFJoKRpSciklue8O9XQhugQH20mURl6CdSn8kpL1sqpORS_DWuuEywp5Vsny0lUpAjHYXD0h3FUz3ig5H8ioxWM_gJzmkymwCNbeUAMUOBEC7K3mi40JEDvqROymPqxPp_PJsgnL2Rdb837-BPzaq5Gys7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41a8610027.mp4?token=eRDA79guXG6-cKy5UZc9vNbyBL7cXIn4tHWPApdRu397ddmTVgAPjb_T1XVpt-HliqWnliph9KnZ2LMyF_pI1I8lKRa6gPyBc-ewism1H7N-KS-8ZAuG0rzel6clRV-FN1OK_Bvq4l5jjZ2xg2R9ttL9FyNmzmV0n-nKmpIcL3AxiOCYutoAAFCaw0dUFJoKRpSciklue8O9XQhugQH20mURl6CdSn8kpL1sqpORS_DWuuEywp5Vsny0lUpAjHYXD0h3FUz3ig5H8ioxWM_gJzmkymwCNbeUAMUOBEC7K3mi40JEDvqROymPqxPp_PJsgnL2Rdb837-BPzaq5Gys7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی دی ونس در مورد ایران:
ما دستمان را به سوی ایران دراز می‌کنیم. اگر آنها بخواهند رابطه‌شان را با ما تغییر دهند، ما هم رابطه‌مان را با ایران تغییر خواهیم داد.
این پیشنهاد ماست.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66168" target="_blank">📅 17:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66167">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/362abac9d7.mp4?token=lfbuu4TFJdWjXtlcjeBDreUfguwzsW9eVDxhUb6gEgxQrctkG3UBwmzDiX4jrX2bm2UaVl3BrfEc40uMPeMUOs76aVEkgOQUE3sbQat3Cpgbp_M0GEYsBa6HITe7RwrGgODMJQ5NBqmjN_-EwQCFv2TRbPNPMza8XKbfGNld6jY91tJdjSRPtCsbTSUn1Ew4vGvYuBboXRf1_eTTSd4zBbUHK68r_PYYEW__NsS5Mj3DoWMIL-Lh9G8i0Cn4mDkeAS7ry1FGcjWVhnYjVPgj4m7QIqGq2R09qXbxOuR1SmWY3bocLCtym8oWTGtkmp0Q8u34L1hmFwJlayo9QK24Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/362abac9d7.mp4?token=lfbuu4TFJdWjXtlcjeBDreUfguwzsW9eVDxhUb6gEgxQrctkG3UBwmzDiX4jrX2bm2UaVl3BrfEc40uMPeMUOs76aVEkgOQUE3sbQat3Cpgbp_M0GEYsBa6HITe7RwrGgODMJQ5NBqmjN_-EwQCFv2TRbPNPMza8XKbfGNld6jY91tJdjSRPtCsbTSUn1Ew4vGvYuBboXRf1_eTTSd4zBbUHK68r_PYYEW__NsS5Mj3DoWMIL-Lh9G8i0Cn4mDkeAS7ry1FGcjWVhnYjVPgj4m7QIqGq2R09qXbxOuR1SmWY3bocLCtym8oWTGtkmp0Q8u34L1hmFwJlayo9QK24Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش شده یک فروند بمب افکن Tu-22M3 نیروی هوایی در منطقه ایرکوتسک سقوط کرده و به گزارش وزارت دفاع روسیه تمام خدمه موفق شده اند با موفقیت اجکت کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66167" target="_blank">📅 17:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66166">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‼️
پرزیدنت پزشکیان:
فقط یک نفر از اعضای شورای عالی امنیت ملی مخالف توافق بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66166" target="_blank">📅 17:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66165">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SVkSjO3H7SGq7cGiXtiKycy8GEmJYwIj1i1NxJ4_uA9Q1wU1iJtLbVDnPCsCPNtnBMbZTVfIADiqendoPmByx1ei2-S1mnksp2UE8XACls7TUMJdBSDrWhJscTO-HteS6We4UtZgywUu8Ycxf17a4_9-GTEdwTdw98VXgOGNOdjmLmLHzwB-3xuLJ8VH9QZuuiF0RqLtH0I_rLSg0lL25VR_vUToDSqWAYitKtbRFj8cl0TewNu2GcPiMQISD8EJ0iFWHSXw0eYQdieKv8RC1heck4xImz7nx-lPHjGhI3WcSQ75UnjoQDLWZqVnBV73VYxQE54CX7q0ywdnmR9wCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبل شروع بازی اسپانیا و کیپ ورده فاک بت اومده لاین داده ضریب ۲.۲۰ الانم میخواد آنالیز بزاره از بازی های جام جهانی نمیخوای بیایی سود کنی؟
💵
@FutballFuckBet
💵
@FutballFuckBet</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66165" target="_blank">📅 17:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66164">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahOdgRD0W576hpQ76SpAAfoMrDYjW2QL9bjj0-yHg_5DpMd2TVASmpuQNAoYdzYcv7odKY3gU9KOMLgETd_1zkweadIEM2ZRqF1flWtWvdzv37Gg6AXdDTqeVgxTV-iMd9Cm-cYKg67VOpgIJ6nqtSqhM6MzQPk59mzCFsGkEwPKwq_x9wIeIv26-X2b_9ils5gIeFhGSXGRWBhGxbHagOSQEoSFvcuUxU9bSuFpZYaLjq1dfM7B00gaf8XCg3Apfa78n0U6LhaENg1JnPapfg5bkpsFvh_wM-fjAEqRqGwvqgkwLi0r8_JZKvSVoaLGJuPM90RtTgsa1V9l8mcjQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ در تروث سوشال :
پس از توافق تاریخی حاصل شده با ایران در آخر هفته، کشتی‌ها شروع به خروج از تنگه هرمز کرده‌اند، که بسیاری از آنها «پر از نفت» هستند
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66164" target="_blank">📅 17:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66163">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‼️
صداوسیما:
تنگه هرمز تا اطلاع ثانوی بسته است و سپاه بیش از ۹۶ساعت هستش که اجازه عبور به هیچ شناوری رو نداده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66163" target="_blank">📅 16:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66162">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9664d2e7.mp4?token=nN2jOWH7MrL0Ol9Mz0UmngVF5EyO3Ia9GBske2FvFgXCsc16KI8FUU8235_8Fb8o4IpByI7deSoCFvoPXKT1-aX55yYzx1SYmkx2-40OmCP4CokYMGkAmhnqxHls2MKb96AaHfWU9DvylGi17WsIi2M1_2mZT7VadrCH7KBpY-XAtvQU-iSD7D16L6KH3b05SUYahP3_ULS0BrF9vgLGjql_A4qeLMnAcORhEC43yFi8_z6ulBGx6WD6jMK1qXvg_bLzlJLA5SUt-lSlvn-NWMr3gqFLsSTurne0IrTCsFtZZk8F-J4vWNmfLwaECQDi4HMfl6oHJ9Q62ptkl8_xOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9664d2e7.mp4?token=nN2jOWH7MrL0Ol9Mz0UmngVF5EyO3Ia9GBske2FvFgXCsc16KI8FUU8235_8Fb8o4IpByI7deSoCFvoPXKT1-aX55yYzx1SYmkx2-40OmCP4CokYMGkAmhnqxHls2MKb96AaHfWU9DvylGi17WsIi2M1_2mZT7VadrCH7KBpY-XAtvQU-iSD7D16L6KH3b05SUYahP3_ULS0BrF9vgLGjql_A4qeLMnAcORhEC43yFi8_z6ulBGx6WD6jMK1qXvg_bLzlJLA5SUt-lSlvn-NWMr3gqFLsSTurne0IrTCsFtZZk8F-J4vWNmfLwaECQDi4HMfl6oHJ9Q62ptkl8_xOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ممدباقر۲۰بهمن۱۴۰۳:
با قاتلین قاسم سلیمانی مذاکره نمیکنیم.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66162" target="_blank">📅 16:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66161">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3b04717ec.mp4?token=p1byDDkYnePTYEqNrAlKA1WDehPhcjsDhOWTlEQtdZ_hSbmkVlHQrnz9t7mUDsbFryAQDF9tBIi4zg_ft6sLCeB8w5iVL8bTq_Cg9bugOSgQMb1JzxlePNLRYFGidYI0WPcOBlPn84aqvAFT4jIL8xkoMx3ty_TzRG9ZxSq--xHbIwoTaADeCFhTJq-3VtFcNdMxwyMrsZE3no8QWZIYqLEQrE2Wbw3XxvYBscH8U7Ylfrbz5PIX0-LcucMdkiKSVfR9bL4ZHTxSaOm2dN_xRWmfhTbxpvt1A7aaJBNxk06-F6lBtQ0iMB7Yp1k4Nzn4wdOmvBP9suZW8wq1jFgqSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3b04717ec.mp4?token=p1byDDkYnePTYEqNrAlKA1WDehPhcjsDhOWTlEQtdZ_hSbmkVlHQrnz9t7mUDsbFryAQDF9tBIi4zg_ft6sLCeB8w5iVL8bTq_Cg9bugOSgQMb1JzxlePNLRYFGidYI0WPcOBlPn84aqvAFT4jIL8xkoMx3ty_TzRG9ZxSq--xHbIwoTaADeCFhTJq-3VtFcNdMxwyMrsZE3no8QWZIYqLEQrE2Wbw3XxvYBscH8U7Ylfrbz5PIX0-LcucMdkiKSVfR9bL4ZHTxSaOm2dN_xRWmfhTbxpvt1A7aaJBNxk06-F6lBtQ0iMB7Yp1k4Nzn4wdOmvBP9suZW8wq1jFgqSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله پزشکیان به منتقدان و اراذل صداوسیما
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66161" target="_blank">📅 15:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66160">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDVLCS2onGIVjqMRE5SgPyMLN19Jyz01Md9Q6mQitZDpurpp28QXfE-mw-27rwr1HsCEtFvcIeu2arD-dROlYEcX-jPwH5i3cV0dfQWieksFJnV4f9bG6OUn_lLsJetLv0xrVtqT-Fy6d5oxy4ZRnV6gPRGZVpu2z4zWmywVG1xACpeE72Nmpdc7CycEgpQ2hhlp3ppo891lUc-Cw9XEvEbfkCDZq8J_BmjYGlVCAkw8S8qEngwVdwxV0HWokEX8Nd1MSKRLd7EqozWB70Tlp22QZ2kEUFfJUpPelJNHB8RH_v_NBezwH_jUPEYaTnHmFzeAJfqxH1QodvAOj0Uetw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ابوالفضل ابوترابی، نماینده مجلس:
استیضاح مسعود پزشکیان مطرح نیست، شاید خدا شهیدش کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66160" target="_blank">📅 15:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66159">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74d00f0f51.mp4?token=c_7DmwlHMPokEUbjxUqxVWINabvUY_0GPYNj8JDZXn4IUFRnrjaZKBK37GJwOABhxChG7rYPBKh7sYVDtm-D0biz_NluLmrLZnbQM_NdidinU1bWgSqjHsHdZK-jM0KT1mVk4UA7rgRGsq3t5gld0nG2pN26ZHsSUBsAJeecJc-zoKCZny5hbrp7K579cnYvvmoifXLzF5J4Qz41Bmyka38IBswma-bmalWkB0Ny-e6dIWRKCpHY2t7J4yImfDm1Ajq6LB_SsNcRMvRfLv8PGx5FqD6xlOjTfLW4Yf2C8Zh6qkpq-3gwize1cIvhsSXuhuOiLsUANJl9iCQh6FOFHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74d00f0f51.mp4?token=c_7DmwlHMPokEUbjxUqxVWINabvUY_0GPYNj8JDZXn4IUFRnrjaZKBK37GJwOABhxChG7rYPBKh7sYVDtm-D0biz_NluLmrLZnbQM_NdidinU1bWgSqjHsHdZK-jM0KT1mVk4UA7rgRGsq3t5gld0nG2pN26ZHsSUBsAJeecJc-zoKCZny5hbrp7K579cnYvvmoifXLzF5J4Qz41Bmyka38IBswma-bmalWkB0Ny-e6dIWRKCpHY2t7J4yImfDm1Ajq6LB_SsNcRMvRfLv8PGx5FqD6xlOjTfLW4Yf2C8Zh6qkpq-3gwize1cIvhsSXuhuOiLsUANJl9iCQh6FOFHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ برای شرکت در اجلاس گروه هفت به فرانسه سفر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66159" target="_blank">📅 14:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66158">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZ2t3cYImXsN9GAxQaY0ZmBg481IwFCtFIS20oTRB0iwQaJNjdedO3vZO-RdGpGt1b2g0yegFGnFL4V9QxllHBs_AIUv5HXQDfKbw2OFKiBsRI9zyQ-DOWEXV2VqkvvaxKO5w26h-WymvUrpX6xlFRoLzwb_OindcjZyo35JvanA7VxM-5Rkpn22boH3oMGbrs1jKp0ZFfRmMMqMIVYp8BnSDgkWqDUJI_9xPpxUsZpRipd4YE-I5LEpuyNl9ATHrp73HUX0612Nzo8QqqAkrXjJSbhb9G1CD1Nb32dSdN0XoqzMvtg6qLQGxikpKJREusN8GWJX-NzaRVb9Nu2ywA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید حساب اسرائیل به فارسی:
یک سال پیش در چنین روزی جمهوری اسلامی با ساقط کردن چند فروند F35خلبانان اسرائیلی را به اسارت گرفت و ما همچنان در انتظار پخش اعترافات آنها در صداوسیما هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/66158" target="_blank">📅 14:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66157">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2defa37b1.mp4?token=ksFlLNufGMBwEuVTJW5lUjpdtq0cPt2HPKsY_dKxPmt5n6FAAuvDlwIjT8xjP4u7MmWQ7KW07foHrHrv_lvzShnkYVrqPIruX0tvll4UpoZbbli4QvjcbV1zhyI-VLlC0rphU3y-9seVcBBq75tuEc65FIOinjQqZELeRoSQTurTFPRp8yb6RO7SDis_zch_IZf6Q7NfLIQp79PL-DbD7iN9Ox-yEbHBSNZQU1M5STrWFxJHJXZh8QMQweYhsZ-ptLjzeZ403VxkAf46nkYF0aJFM4j-UqJyMX8TNfGo9DtCjHHsve7f1vF_fD4_afI7bLCsZd_dF9-IZWsWBlvu2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2defa37b1.mp4?token=ksFlLNufGMBwEuVTJW5lUjpdtq0cPt2HPKsY_dKxPmt5n6FAAuvDlwIjT8xjP4u7MmWQ7KW07foHrHrv_lvzShnkYVrqPIruX0tvll4UpoZbbli4QvjcbV1zhyI-VLlC0rphU3y-9seVcBBq75tuEc65FIOinjQqZELeRoSQTurTFPRp8yb6RO7SDis_zch_IZf6Q7NfLIQp79PL-DbD7iN9Ox-yEbHBSNZQU1M5STrWFxJHJXZh8QMQweYhsZ-ptLjzeZ403VxkAf46nkYF0aJFM4j-UqJyMX8TNfGo9DtCjHHsve7f1vF_fD4_afI7bLCsZd_dF9-IZWsWBlvu2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت«
ال ریسیتاس
» بازیگر اسپانیایی از اتفاقات جنگ
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/66157" target="_blank">📅 13:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66156">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dca54ea3d.mp4?token=TA9KD9NyhFc-PxDPz9AZqT05baxUB6KHZJYRR2DRbwviUJ1sqTYcD11wNymyD6TkGu57XzH9woKU6LQZRve-iJxWHM3e_UCrLw8byliRy-GIYsPFAqyPAs1IXnKeXoB8U4_jzLIGwCwNrVTGcDnbJrhL-CLl56UcwV-XInqLolttSoCs7ymGUmVXAY-urDYbfew7ATNdWRZ8PektdogyRcQbgnbbi_gYzxw1N-exvzGx4_Dr6YHgRsq4zRh-yRBJ67YMECzePxy6q_4A13yRAtsP1W-RAMJI6jIy7nno6Kpy4NkKhsBvqq2zBAd8foVbGZryPUqbXSTE5zkLBTueSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dca54ea3d.mp4?token=TA9KD9NyhFc-PxDPz9AZqT05baxUB6KHZJYRR2DRbwviUJ1sqTYcD11wNymyD6TkGu57XzH9woKU6LQZRve-iJxWHM3e_UCrLw8byliRy-GIYsPFAqyPAs1IXnKeXoB8U4_jzLIGwCwNrVTGcDnbJrhL-CLl56UcwV-XInqLolttSoCs7ymGUmVXAY-urDYbfew7ATNdWRZ8PektdogyRcQbgnbbi_gYzxw1N-exvzGx4_Dr6YHgRsq4zRh-yRBJ67YMECzePxy6q_4A13yRAtsP1W-RAMJI6jIy7nno6Kpy4NkKhsBvqq2zBAd8foVbGZryPUqbXSTE5zkLBTueSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویری از حمله اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/66156" target="_blank">📅 13:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66155">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ef1hZBqkx12tyC2_cgtaR_MjRn4gllifWPVbFtLZ0kymwsaywPwBAmpIeFZRdhWUGHMAj4Q8GyLujMIwFJlj-b4qml0b-t89TbnI9Z7jaGA8ZyLJ8DUgg4JEoYGWuW4tzdsx8xioxaWA8WHCB1RsZEwcFlce-wkc6340ZEU-TUm_SfiPXSVH3LfNfqMV9iKRVP6WrCczGQjKHttNrL2mBlFfwaH9u3FKhD1L3X8nB0xnpNpw9349DEqOOXIFiZesVTgKAYamcphENb7Si_d5bEiOrQTGKgVwXRJzVWTRtMdgvZ8lRqg57k3mua-1V506sFkZTsWY_V3SYGBH4UR7oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دیس پزشکیان به تندروها:
متأسفم که به کسانی که دارن با مأموریت قانونی برای حفظ منافع و عزت کشور کار می‌کنن، برچسب خیانت و وطن‌فروشی می‌زنن. انتقاد کردن حق همه‌ست، ولی تخریب و له کردن این آدما کار مردونه و عادلانه‌ای نیست.
دولت باید از نیروهای خط مقدم که جونشون رو برای امنیت مردم کف دست گذاشتن کامل حمایت کنه. نمی‌شه ازشون انتظار فداکاری داشت ولی امکانات و نیازهاشون رو فراموش کرد.
ما جلوی هیچ قدرتی سر خم نمی‌کنیم، اما در برابر همهٔ مردم ایران و خواسته‌های درستشون پاسخگو و مسئول هستیم؛ نه فقط یه گروه خاص.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66155" target="_blank">📅 13:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66153">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RAZiXWqxWOzUs9W9Sb8jxCSyQQZX13kJGlKuKm0P2QldgfQSVv3dv3ADEN-4Y8bwYkQc1pM-XrOBgpj827ELiyOA378gKufqH_lFRsnuKVsbi2A1s1Htv1on6KbYSadGcKrpridMmcdoliIt4VQ9AU-A17CUMRXClXsufj313fq1EDJPU0pvD-AOpWrb3KajjWlRRMorO1ZmyX9r2tzmZfkjKJAgXAv8eYOSWftfcHbgHnaqpbYf7Q3QouadIH9xgGlHU0dug5F8xqYn3d2M0CZ-FH_VWTnxmdMf0kqrZ5p_33FgEd2w6sQW-tdYZ6pnENZr7aNTYCuyLqrt59_H0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/elwCJw1cVbi2i4b2d7yHrTimDTc0aL1vAtDowGClAShlU3exsVMAEnIVBG0GwFChgL0eomyTUFfda25VYuzb-EMbo4E_9jHeaRW0X0AM4VmFT4w15Av4ANwjCoC5_A5O9afBiW6zjPvMzFXLhN--llLumtmQuzcbhnhJ91poRvNU1bX9Y-LwcqVbr9kM38Bp4KlEurpI7XAuY79lzFMIx2Oh4DN-168cmHUve5o-2OI7O_1CDfCfh7dMf2r00y4Pww9ovCgYSaU-7GXL37drsp_Bu3zd8QfEY0ngYAVTjQgF0uz23ECty5Smzf4Pka4Lkbb2wqrGM7j6HAWJ5uJedg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
حمله هوایی ارتش اسرائیل به الخیام جنوب لبنان!
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66153" target="_blank">📅 12:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66152">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66152" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66152" target="_blank">📅 12:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66151">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5dZ8tp7Z2BnvEsqJrDlaOIPvlP5DqFeRIP5dum02_ZheScE6iV2VXlrbAcNutaYZJSdgzC_xXO3DUjFFwKgrG79IGL1IAPJ0SZHyIxIgBOHlbYg8n1VnB8gaaKoALkeZLwi18bxnWmn9WcpaNb7CTGzqVSFU6VMKHMXL2HXioIZy_lSQE6cnFdRHAE2lOZp8SKUisF4NMCcLtd3-tSvASerCyGjtwOkOgakazju8fiBe2ocQrlLqG5l5_IKlechUATXhMVR_oZoxI_SaI3INYn84wWSYeUwOjomb9yeuMxh95fAmB_T3Vk6IUwEX2vn_iBddEw_xlEhdix4VjRjwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66151" target="_blank">📅 12:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66150">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWnHklLKoP5f4kXHee0i8MnFdL51X2lf-7NM2MpnC0wnnTE1n-KHCljt2_UEI_bjUNGUe1zrJQb3CuMiEHj96xahiuLnTDuR_OAFWk8w20VifAl3-V4MRQXpoif2wxKgm-Dl9KAAp6hNf48o94Kg677L2LaOPOYsoMcIo0_hGrfLPqkV6OewxVaHP4rp1ZhBW1dXsL9f7IxZrrz-q3x2z4XZeXMMBW7blj01__RnHE2I5sAvgPVLUnxPvKlXHRX_FDnM5sl0GJILsb6Jpoul90M32g9_0b5pJ3Qo1zm8yjnXE5nzSE3jcm86JXF1FzZ7VWEcs5bo_X6shjCoRTtHHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیده شده در تجمعات
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/66150" target="_blank">📅 12:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66149">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyV-3NeicdZBVYQHbSLp8PSHOqxwoGnnHxBQMSRwsSg2R5nXFWsNrxD9fIa34soqW3hbQotlPaTTVWHTWOfbkx1tasqIMzXm7YCBgW4udXBs5xk3XfCEeOU_NjE4jHtAfmPdj4sy2U3njPnaN7lc2fIBLeagh1T3Xc7V2rjkMOX2bEjfeVpMGxzrt0E9YLsLmVP-HP3A33GZLPyummd5KW3JtEHHWtlwOl-PNgMjAUaSAVTwLL1HEME8SuwrQbpUCPbJjB1NOIc_JS7S5BBqvOByobJliQXoI7sxKpAvJXksMxZtzZAd80ALOXfTVyXGJaJ_ylmdRuGrVbf_9NCDsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وزیر دفاع اسرائیل, کاتز:
وزیر دفاع اسرائیل، با رد فشارهای بین‌المللی و هشدار به تهران مبنی بر اینکه هرگونه حمله‌ای به اسرائیل با نیرویی کوبنده مواجه خواهد شد، اعلام کرد که نیروهای دفاعی اسرائیل به طور نامحدود در مناطق امنیتی در سراسر غزه، لبنان و سوریه باقی خواهند ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66149" target="_blank">📅 11:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66148">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e24ffc7435.mp4?token=U14zMRP6xgtooegJYWPPHIorC4gvbXUzoRCQdO_A80XGMti0jasMe9Tg6Z04LZ_y4CfK56Mz5vLDlGrdH1A34HjYDIFfm548ws6ZjgtC-IzKZDuFNKoSp7gmjcKivE6jgHCKz3lZ6dqwL1qGhyxYjV8jJSw0vZTK1A3MWnjzumqn146EtCDiogBeI32zc81pCzpwlaREq0p3iFPqBWAvQLhQTtpF-6hFZnpdds8arMgkQ-z0qg75z1VU-hPlzobxD0LDVyjcBF4_2I9kVvBzoSzObCgcMd_vHL0lemEg5812VVPZcgyA7-ppVvwl_x_KgtpFJokcXxUgXy5x48HyDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e24ffc7435.mp4?token=U14zMRP6xgtooegJYWPPHIorC4gvbXUzoRCQdO_A80XGMti0jasMe9Tg6Z04LZ_y4CfK56Mz5vLDlGrdH1A34HjYDIFfm548ws6ZjgtC-IzKZDuFNKoSp7gmjcKivE6jgHCKz3lZ6dqwL1qGhyxYjV8jJSw0vZTK1A3MWnjzumqn146EtCDiogBeI32zc81pCzpwlaREq0p3iFPqBWAvQLhQTtpF-6hFZnpdds8arMgkQ-z0qg75z1VU-hPlzobxD0LDVyjcBF4_2I9kVvBzoSzObCgcMd_vHL0lemEg5812VVPZcgyA7-ppVvwl_x_KgtpFJokcXxUgXy5x48HyDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایرانیان مقیم آمریکا طبق درخواست قلعه‌نویی واسه حمایت از تیم ملی ریختن جلوی هتل
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/66148" target="_blank">📅 11:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66147">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJX32uFKBAJ_Ad7csCUm8rbdUmluidGHbkbzju1sqDZdypgVLXFHZddjGk5IpWj6b-5cHMSvgzGx1_EaqWztZ0pDfOypph0QZXU-_LKh8AmMM2F9wh876TDG91tLSCZcwcDDO4-wRnTH2J90rV0CAOZxmxFSPl0GRbwANwWWg2SrGNeZSJJLWCQxqEkP9uSYzdnWLHrNjFlB3fty91_7biEGA3wabsUUFvgGADN_dAh-fMeAWmM5EISlyuN2koC2fP_xpUFbXbSNOYtcGX-phjuGTox7MvDRoutqTvyc2hTodzlprdXZ781JawF_YwP4LF_LHBSKzanhI7ZoBCP-xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت عرزشیا هم اکنون:
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/66147" target="_blank">📅 10:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66146">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWpthapql7gzHmvxEMDtxtQmOgtN4XPZaDZIZVnf4vQAOZ58koEXroP552dRUq49FCFuWAoyKfBEt4r3pWGwbOj4wAus_t1tuj5raMDlg2BRAseBS_bs7CKWUsLifIMZXT5OEJ8xx0pm3VT1h-P6kewdXI90dOJMEBTO8V8JrLyVYaKUxwH0J8n7cfx69NNr8Nn192X24q_cQFl8WIf1HxCC9XPJWbGyok4unVZc9r88QOkf8BRtA64y6J3oeXJzArRbOmtd5VumBxQcNN8AaZw1fJ3n8Oo1xhE-TXDzMk5kDJvbe603cflsvOefOm8nPrvOe7UXEzGuqRjm3xHC8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عایشه قذافی دختر معمر قذافی در کتابش:
به پدرم گفتن موشک و برنامه هسته‌ای رو بذار کنار تا درهای رفاه و آسایش به روی لیبی باز بشه.
پدرم همین کارو کرد، اما ناتو شروع به بمباران لیبی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/66146" target="_blank">📅 10:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66145">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cccd116404.mp4?token=Ppt2wGvt8n2bQp2jlShnrQMzVJPwbkeXBPEOpUhxKfyvnGDZMwHRc7cXGmsUv-LetfoOECjInj8AO128QJVe3bIU18G9VXxWRVdjPkd-KitH6TjCfjcKI4mDae-lV2Jf7EbW3r8jLPsZlWainuuc1tXEGCXwWJ-xmtZ10GJXNqYnY7xhtZlh0P9iU3UO7aymo15RHSJOvz1LeDUex4ORRck-deUVVYR5HnMU--E3_IXw4iIW6k9Pwj_tmZzHA-U3rJLHigFJil2J2IZKSsVZU-tmD2P9JnmZGo_O2Tc5JGsFEXM6EgBLtRKJWMB4eASl_4XnKACRajgWimfMuDkCyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cccd116404.mp4?token=Ppt2wGvt8n2bQp2jlShnrQMzVJPwbkeXBPEOpUhxKfyvnGDZMwHRc7cXGmsUv-LetfoOECjInj8AO128QJVe3bIU18G9VXxWRVdjPkd-KitH6TjCfjcKI4mDae-lV2Jf7EbW3r8jLPsZlWainuuc1tXEGCXwWJ-xmtZ10GJXNqYnY7xhtZlh0P9iU3UO7aymo15RHSJOvz1LeDUex4ORRck-deUVVYR5HnMU--E3_IXw4iIW6k9Pwj_tmZzHA-U3rJLHigFJil2J2IZKSsVZU-tmD2P9JnmZGo_O2Tc5JGsFEXM6EgBLtRKJWMB4eASl_4XnKACRajgWimfMuDkCyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی دی ونس معاون ترامپ:
من قطعاً قصد دارم برای امضای توافق در سوئیس آنجا باشم، اما ممکن است خود رئیس جمهور ترامپ نیز آنجا باشد. ما این موضوع را حل خواهیم کرد.
فکر می‌کنم می‌توانیم با اطمینان بگوییم که ایران هرگز سلاح هسته‌ای نخواهد داشت.
ما کارهای زیادی برای انجام دادن داریم، اما امشب یک پیروزی بزرگ به دست آوردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/66145" target="_blank">📅 09:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66144">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e4991d46b.mp4?token=C0JLZgPP23e_cLI2lUUZDLLCPolAy-2aJ98o9NYRGExwOGCN2Q4UUovxg0-5o21v1FL19G2a47-E3qvpxfLzc8S_-kjZ1rP8dsBrUVUnT3N1ZcZ4E6r9OipRuwiqOJ4_GnVWsFJHmS9eMXjMWL_DoQoTnH76J2pjfbL9HbCn51omlouIXCkSLZEZ1-G5p32b9D8HB2dBuamT4934JmUo6UCOE_YVWqNUGMGlfC3I1Cx3gCrStJzXNVImu6YfL3xUFaIM53gLMDnko2vUoEQrqNy2ID0x-lCWphkxnK2QOkZWTyNvgon5fdaAE81_AC-4rTQpQHdFMIZDDZjSlcqz2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e4991d46b.mp4?token=C0JLZgPP23e_cLI2lUUZDLLCPolAy-2aJ98o9NYRGExwOGCN2Q4UUovxg0-5o21v1FL19G2a47-E3qvpxfLzc8S_-kjZ1rP8dsBrUVUnT3N1ZcZ4E6r9OipRuwiqOJ4_GnVWsFJHmS9eMXjMWL_DoQoTnH76J2pjfbL9HbCn51omlouIXCkSLZEZ1-G5p32b9D8HB2dBuamT4934JmUo6UCOE_YVWqNUGMGlfC3I1Cx3gCrStJzXNVImu6YfL3xUFaIM53gLMDnko2vUoEQrqNy2ID0x-lCWphkxnK2QOkZWTyNvgon5fdaAE81_AC-4rTQpQHdFMIZDDZjSlcqz2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی خطاب به بسیجی‌ها:
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/66144" target="_blank">📅 09:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66143">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
ترامپ به نیویورک تایمز :
اگر توافق هسته ای شکست بخورد، حملات نظامی را از سر خواهیم گرفت یا در ازای ۲۰٪ از درآمدهای منطقه، واشنگتن را به نگهبان منطقه تبدیل خواهم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/news_hut/66143" target="_blank">📅 03:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66142">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c39322d55.mp4?token=gDxbz7sAcgvOxSmgxxTkMYiiGtdDvxmgCytrBzrVSmOsfJs5iNDFQzf8S97U6ec40AOk7Ba5HE2h1_zJtkV3vJLewDmSQby6zxeatzEmxE41hg5QKFobnjZ20lN48dz3GaJSBUm8zgcDJ9R0PrAPZlxbNUeeNpCs9e7VzWyX-A6oXpFb80gqLIeqLnhK3KnsQXVdXWBvVS9DHRRC3FxoGPEXgeqW4yuAPfUrI79S0BKNtyZEuBSNKac9VSj__1GgsavtrpbH0CSU5ToYn4z_y0B3J_J7yEjHQtOlrLLNd7RV-zyFnLj0OGTxAfFPf9_Pngj_ssKtrFpYEborfo2xww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c39322d55.mp4?token=gDxbz7sAcgvOxSmgxxTkMYiiGtdDvxmgCytrBzrVSmOsfJs5iNDFQzf8S97U6ec40AOk7Ba5HE2h1_zJtkV3vJLewDmSQby6zxeatzEmxE41hg5QKFobnjZ20lN48dz3GaJSBUm8zgcDJ9R0PrAPZlxbNUeeNpCs9e7VzWyX-A6oXpFb80gqLIeqLnhK3KnsQXVdXWBvVS9DHRRC3FxoGPEXgeqW4yuAPfUrI79S0BKNtyZEuBSNKac9VSj__1GgsavtrpbH0CSU5ToYn4z_y0B3J_J7yEjHQtOlrLLNd7RV-zyFnLj0OGTxAfFPf9_Pngj_ssKtrFpYEborfo2xww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی مردم لبنان و نوچه‌های جمهوری اسلامی پس از اعلام توافق ایران و آمریکا
و عدم حملات از سوی اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/news_hut/66142" target="_blank">📅 02:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66141">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‼️
جزئیاتی از یادداشت تفاهم ایران و آمریکا:
در جزئیات یادداشت تفاهم ایران و آمریکا این گونه که پاکستان مدعی است بر لغو تحریم‌های ایران تاکید شده است.
طبق گفته پاکستان، آزادسازی بخشی از دارایی‌های مسدود شده ایران از ۲۸ میلیارد دلار، بین ۱۰ تا ۱۴ میلیارد دلار آزاد خواهد شد.
آتش‌بس کامل در تمام مناطق و خروج ارتش اسرائیل از جنوب لبنان اعلام شده است.
همچنین به پرونده اورانیوم غنی سازی شده اشاره و آمده است اورانیوم و همچنین تأسیسات هسته‌ای ایران در ایران باقی خواهد ماند.
طبق این جزئیات، یک صندوق غرامت ۳۰۰ میلیارد دلاری برای ایران تأسیس خواهد شد. تحریم‌های آمریکا علیه ایران لغو خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/66141" target="_blank">📅 02:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66140">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEOTbzGDUpYiiolCB0SpcEs32rxabp52QG90JTSVU5w6pcXfH6-o5LbxRxarx6hY9brWJTeiICXUVSc2Y038cLQ0B2S_KgY650RtX4qSwkD-8QB_3OzsCjKAADRfFh5YqIZmTqsxLH3b13gKewZkG8aZD8ZsCcXbv8Qyd8UWr1xe4MM2QbHvAHkm-9avh1TMdRDWUfmgDBpdPWLegpXoaZhbjyPwbpLdb085HVAnlWj0fvFkMqJBY2p0Y7wWCKKz2-HS5tvjzFnIfmZR4pegqbRs43kheq9zSiE4Ub2z1fFyPOuFn0BoEnoye1M_9AP4wsM_PgMSCMtukSUctbSELg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ:
این توافق بزرگ، صلح و امنیت را برای سراسر منطقه به ارمغان خواهد آورد. بسیاری از رؤسای‌جمهور تلاش کردند با ایران صلح کنند، اما همگی پیش از من شکست خوردند. رهبران منطقه برای نخستین بار، رئیس‌جمهوری را یافته‌اند که می‌تواند به آنان در دستیابی به صلحی واقعی کمک کند. با بازگشایی تنگه پس از امضای توافق در روز جمعه، به‌منظور رفع موانع مورد نظر من، نفت دوباره از هر دو سو برای منطقه و جهان جریان خواهد یافت!
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/66140" target="_blank">📅 02:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66139">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/66139" target="_blank">📅 02:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66138">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MIsvA4nO5a1cdszRPDaw51jD-OEM7i1G5y62APniLALPasc7sUbyr45PVPg74xPtx2A8MtCm0NC3-oS1HByHs7Ggi3frIshJpj17bjsLN1-uOWdxPH6uZ6TiOJhdOajHedl1O9H74uN72JDuzZE8caspsxUPwNyLW19ly10SB1UnTV79K8TIs_coPmX3g5Z25qOS8QyOsF4wgYMRgSTCfAQd6XuHcUa3bv-ZdVv-YYN58BzcfzMtiqsf2dYbbFiObbC5AfOE_F2pJN_uPGlcTa74hRXZyxDBY455NPqyDFy0llq7aXFjGyhjl-21797OtmGzKdpLHh3f7GgRtx_x5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/66138" target="_blank">📅 02:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66137">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9WP-9BCeepmkmDpIar5MPwUyQk6W0gCigx5HQ9sN6cN15G1fg7dmhgU2fiqnuzOCg8bhWMkW1W4_I4znCkuAo7sYZ2WJq03b_EiOmC3igHO7EBJNXVEkzKN4JsZsUoP0HpomTIPxaaZlunPurLWOYJo6q3uGFIkYJFbEFBG51AOEM0DLG4EytjP1-S2kC7eQ-hpqpWOJ9mXOo0OwWsXTPOPJ6CmJvdNRJKOi_bX_EpjNljR5247BDVIi9Ku66p6bVAtvj8ZE1UeQbP1YheIwlA9dg_OwmbTl_nNHOYT-FgQOC5uaOAEjFu4OBPuKirI5VdHvBaGJIGv3aw36AuHyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیتر شبکه خبر همراه با این تصویر
😂
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/66137" target="_blank">📅 01:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66136">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb0ba1bd70.mp4?token=OP0WiwQTztBkM04-1Ry8qGUefiP5NGE0OAgOXYvELVlsPMX_Hj5RCMToMvMCKA8cF0x-AJbhgRjDq97jdxkZ1AI573l6F5ZDfG6WPkBjJZw2OvnSJ5K21AxGD_ZvBrV_ZUisqVNlvCEKKh_2lBor-D2XH6AGbBZNX5RmhjnbMqiNL67vn1uFTI2TuOLTgavLGZlJIIQXkbcHA1z2bsuM7ITqPl7myjcLVnjsJdTeGPFQfmeoizm--61bNkE-b0m6ViV6SI5jUAHPsEuocUJQMkPmroaSNRU2wbp33OOLWGftTZS2gX4j653b0Xi4YbxPXNkDaki5n1ksFggwdYiyew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb0ba1bd70.mp4?token=OP0WiwQTztBkM04-1Ry8qGUefiP5NGE0OAgOXYvELVlsPMX_Hj5RCMToMvMCKA8cF0x-AJbhgRjDq97jdxkZ1AI573l6F5ZDfG6WPkBjJZw2OvnSJ5K21AxGD_ZvBrV_ZUisqVNlvCEKKh_2lBor-D2XH6AGbBZNX5RmhjnbMqiNL67vn1uFTI2TuOLTgavLGZlJIIQXkbcHA1z2bsuM7ITqPl7myjcLVnjsJdTeGPFQfmeoizm--61bNkE-b0m6ViV6SI5jUAHPsEuocUJQMkPmroaSNRU2wbp33OOLWGftTZS2gX4j653b0Xi4YbxPXNkDaki5n1ksFggwdYiyew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
علی‌خامنه‌ای یازده روز قبل از ترور:
امام حسین فرمود کسی مثل من با کسی مثل یزید بیعت نمیکنه: ملت ماهم بیعت نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/66136" target="_blank">📅 01:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66134">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/616572f1d7.mp4?token=J2wlPzUYoggHzmJwhW0guBhqKL5zLFul0i1jDjJQJfJW0_wJYw0Pci-sjpqUOjyAc3NG96xxQf0gdb8DsSxdOiPFE1sF7Ab7AktfhHN0Z-NUzytQTUVzgbpVJgWjFULj0vKCemSGfJeddirnXROl3ifwZGd1hKVRUa5fQL5HitoHIxbn7aY0MfdM0JsKKqbOc-wd3QkAhFLP4KpoUPEdNmGFdd53cue_CLLN6pwccpiWGA88-5V8yB8di78rEFKcH4Qb_A2MKop6tgdmtOcmaUmxjRqY6fRbQDxXKutyUwYrtQHzl8tH963IHKa3fz56fKYi7AAp8Rv775ufS_b1Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/616572f1d7.mp4?token=J2wlPzUYoggHzmJwhW0guBhqKL5zLFul0i1jDjJQJfJW0_wJYw0Pci-sjpqUOjyAc3NG96xxQf0gdb8DsSxdOiPFE1sF7Ab7AktfhHN0Z-NUzytQTUVzgbpVJgWjFULj0vKCemSGfJeddirnXROl3ifwZGd1hKVRUa5fQL5HitoHIxbn7aY0MfdM0JsKKqbOc-wd3QkAhFLP4KpoUPEdNmGFdd53cue_CLLN6pwccpiWGA88-5V8yB8di78rEFKcH4Qb_A2MKop6tgdmtOcmaUmxjRqY6fRbQDxXKutyUwYrtQHzl8tH963IHKa3fz56fKYi7AAp8Rv775ufS_b1Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اگر این توافق جمعه امضا بشه تازه میرسیم به شروع سناریو زنده یاد مانوک خدابخشیان.
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/66134" target="_blank">📅 01:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66133">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
‼️
دبیرخانه شورای عالی امنیت ملی جمهوری اسلامی
:
آماده حمله سهمگین به اسرائیل بودیم اما به درخواست ترامپ و پس از گرفتن امتیازات لازم، از انجام این کار منصرف شده و‌ توافق صلح را پذیرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/66133" target="_blank">📅 01:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66132">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44bd274791.mp4?token=LOqfNLVo4xqwguYjEg56ag_DS7gzgce--GL5qErENq4DvjVWmxkkE9dAH8u301gc3vgT7XN6VdK52ljelsigkPe1FKN6FDUwnC3QHATr4Sv1Ftd3SZTRWNwMippV8pD_-lMskFbkM5a5yQ3LmmfepBpkiYRyZD8gZ6sVlSgABYpbBn62TuyGCWXQHgZbakfuPSzRJkjWIlhRs6flaLWQLrvfSKRIcFQSZLavs1YSl8UCpCbX913k03uj___tW3vKgbVePG1DioGl246ehjW98sV2ynJ9DhwsCf9oTCyTVitogQlrRgpB8dAkjDwod8zpQ67XXbuFcbr_64YJjrPdoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44bd274791.mp4?token=LOqfNLVo4xqwguYjEg56ag_DS7gzgce--GL5qErENq4DvjVWmxkkE9dAH8u301gc3vgT7XN6VdK52ljelsigkPe1FKN6FDUwnC3QHATr4Sv1Ftd3SZTRWNwMippV8pD_-lMskFbkM5a5yQ3LmmfepBpkiYRyZD8gZ6sVlSgABYpbBn62TuyGCWXQHgZbakfuPSzRJkjWIlhRs6flaLWQLrvfSKRIcFQSZLavs1YSl8UCpCbX913k03uj___tW3vKgbVePG1DioGl246ehjW98sV2ynJ9DhwsCf9oTCyTVitogQlrRgpB8dAkjDwod8zpQ67XXbuFcbr_64YJjrPdoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
دود سفید در کاخ سفید. طبق سنت، این به معنای امضای توافق‌نامه صلح جدید است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/66132" target="_blank">📅 01:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66131">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
📰
تسنیم: تا دقایقی دیگر مسئولان ایرانی درباره خبرهای منتشره راجع به تفاهم صحبت خواهند کرد
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/66131" target="_blank">📅 01:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66130">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPspH66R-vdYQTGcvHmpYzfm6OeB42znjdQ2JyXV9Tpn_uhtoWhzgRjq8UIK6I_pLcTKLS5zhdDztpfO3qHqrzn6GDzKzsDb2SocRcITwfrtDO9C3Kgnwm3Eupw6PkAgeLIToj0WUEn95NKnnoVBDPIsSc0nR-um-R7e0D7xFn3Q03BxpmrDuSSs59BJiiXmljifAhVExZcnCo2K8K96DkHiLK5f9qpS7f1GsoKfs7w3YJsF-7fpQGws4jSCleR2QwRqEDmlNOTfoHP30X4-aLd55KetOtInd-ggJXlLo-2buKu4sIJX4CgPue6BL72LlYj2je1oS7wgJ5vCscOpZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🌟
یکی جلو صداوسیما رو بگیره. چند دقیقه دیگه تیتر میزنه آمریکا رو نابود کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/66130" target="_blank">📅 01:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66129">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWdZsvVijAHKukYq3YLz_Sl5ApNSJUMOELLv0UgypErDUdnznTEHqMGatjvrKpBgNUOkH7oj6TQWQt9pMePzE4Ctxdw24AqHZYkzs1RWCay58xxxXNPnNJ8Lp77vXCX8trvGKww8y1tYioUgHWRBdNBo0GHexRRKm_p2LdCzTPh60gM-6uky0P6F0WN0BsaqyjY5KQ2iMg-1uSRIUl3dPRKFY7QCZ6sg1iDZKs688EyTgZahiF5whlkKw0rPXrJO_oWRPvjU90EsHEwD8FDnHDhUgqMahoPrs6FUqZI8bsEjfLMidohHK4R-2fwut4HYxfRdkUfOq9Clhd_BRiQBAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب الان وقت چیه؟ آفرین حمله به ضاحیه بیروت
😁
#hjAly‌</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/66129" target="_blank">📅 01:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66128">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
#فوووری؛ ترامپ:
🔹
توافق با جمهوری اسلامی ایران نهایی شد. به همه تبریک می‌گویم! بدین‌وسیله من به طور کامل اجازه بازگشایی بدون عوارض تنگه هرمز را می‌دهم و همزمان اجازه رفع فوری محاصره دریایی ایالات متحده را صادر می‌کنم.
🔹
کشتی‌های صلح، موتورهای خود را…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/66128" target="_blank">📅 01:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66127">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EyKxW_P2tnrMJDJMM5r3xue1MyzK9EMFBhVeUF8gKbc91LUDB-mBNcgdetAvoNj7oWi676zmRJPifywJgGOYnJUC51AOdJspSwi9ceq8KkFIM97E3lPPkl2Jc-vwq4yBWG4ZjYsE6CZoBevHvAmzwukDyWL0E2SERoD3VaFcEvk9l-OJRh3TOPY_7T00Jyrg2Gqu4t9BTewo2STOM_HdmRIHy166qR0N1XA9QPCHJXlC56oNbPxh4CkF51jqNC1MDrKpNNTAkXQUuO9w6I_ZxP9HzquTB6ghs_pRysCZElh2YsnOxamzxi6CfCZH2N7RQ--YAjWbJMnP0IHDM7wbWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتقام خون رهبرتون گرفته شد برید خونه حالا
😂
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/66127" target="_blank">📅 01:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66126">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/960c47a55d.mp4?token=G62qlxjlr8raWUfiY_ByjsjdQkue7zMtE41nlAYK4QTYT_4Y3g4qc0kgTVVPjakk4-v5HrWVeXsBkpZM3asp6qU9_-yTgXbp7wWiMj7yoKJr5uUrXw9eZ1k8KtyVaXiLQavF1OgBOJYEkDQ-C9D50gfaFbpAvsa4QEC0rJCRW3x4yeY4_kfO6nRsbtwjTxw6-o5rZWlLzgK73dV5H192MZizY5a_uJcb6WRYqiR1JjqeElpcvA7vi_Lju9jSblVz8Qptk1fAZkgnzMc3fA_ThvhHbe2Z0UW_xTwgOCs_i86znGT4827SneLO9xDF9xdNrz7NNbaqLWzDR6fDYOHFGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/960c47a55d.mp4?token=G62qlxjlr8raWUfiY_ByjsjdQkue7zMtE41nlAYK4QTYT_4Y3g4qc0kgTVVPjakk4-v5HrWVeXsBkpZM3asp6qU9_-yTgXbp7wWiMj7yoKJr5uUrXw9eZ1k8KtyVaXiLQavF1OgBOJYEkDQ-C9D50gfaFbpAvsa4QEC0rJCRW3x4yeY4_kfO6nRsbtwjTxw6-o5rZWlLzgK73dV5H192MZizY5a_uJcb6WRYqiR1JjqeElpcvA7vi_Lju9jSblVz8Qptk1fAZkgnzMc3fA_ThvhHbe2Z0UW_xTwgOCs_i86znGT4827SneLO9xDF9xdNrz7NNbaqLWzDR6fDYOHFGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین واکنش مجری شبکه خبر به امضای توافق
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/66126" target="_blank">📅 01:08 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
