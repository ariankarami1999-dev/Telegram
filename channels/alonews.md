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
<img src="https://cdn4.telesco.pe/file/Q8DLS9piyvS5KkRcN0ZOwf2xfmJ7_WOrPC1rTkPuH6KNVj-ggMWwXuf2LEVVMKzJBhKDdNQer-4T--stbuTY7UkvSI5qCbxwkE-dUt5UpmQ28Tz58IbkuhiOf_Qb5fgdPVCDSgGqO15TlBCEz5jmNBLGCtadCkw2inUHc0IoFNrJTGkZW--bJCFJkHwQrF4dm7XBzD0J_ziE1kCY92XLHEb_jB3zObGkgRNXqSD3t8zLibLER-lGb174SItnOVq4vV8PiiEGIQMBj5Anos57bjYzpzXWMouGYfGMC9zBZXjpoGNjarDbHId3X1ZpncV7BTmBJ-Pq4tElkM31d1vYhg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 971K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 21:43:22</div>
<hr>

<div class="tg-post" id="msg-128542">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
فارس: برخی منابع نزدیک به تیم مذاکره‌کننده ایران، ادعاهای شبکه خبری العربیه در خصوص متن یادداشت تفاهم ایران و آمریکا را تکذیب کردند
🔴
العربیه پیش از این نیز گزارش‌های نادرستی در خصوص مسائل مرتبط با ایران منتشر کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/alonews/128542" target="_blank">📅 21:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128541">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
سازمان اطلاعات داخلی فرانسه، اداره کل امنیت داخلی، استفاده از پالانتیر را متوقف می‌کند، وزیر دفاع سباستین لکورنوی به نگرانی‌ها درباره وابستگی استراتژیک به آمریکا اشاره کرده است، گزارش خبرگزاری AFP
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/alonews/128541" target="_blank">📅 21:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128540">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
فرهیختگان: بیش از ۱۰ هزار پزشک زیر میزی می‌گیرند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/128540" target="_blank">📅 21:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128539">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
یک مقام آمریکایی و یک دیپلمات منطقه به تایمز اسرائیل گفتند که آمریکا خود را برای ارائه تسهیلات به ایران در قالب معافیتی که به ایران اجازه صادرات نفت می‌دهد، آماده می‌کند.
🔴
اعطای معافیت تحریمی پیش‌دستانه آمریکا در مورد فروش نفت ایران نشان می‌دهد که در واقع برای برداشتن برخی محدودیت‌های اقتصادی، نیازی به امتیازات بیشتر از سوی ایران نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/128539" target="_blank">📅 21:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128538">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
عبدالناصر همتی رئیس‌کل بانک مرکزی به خبرگزاری تسنیم: پس از امضا و آغاز اجرای یادداشت تفاهم، اقدامات فنی و بانکی لازم برای راستی‌آزمایی آزادسازی دارایی‌ها و امکان استفاده عملی از آنها انجام خواهد شد تا اطمینان کامل نسبت به دسترسی مؤثر به منابع فراهم شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/128538" target="_blank">📅 21:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128537">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
صدراعظم آلمان مرتس در مورد جمهوری اسلامی ایران: ما همیشه گفته‌ایم که آماده مشارکت هستیم. ما قبلاً اولین کشتی‌های مین‌روب و کشتی‌ها را به منطقه فرستاده‌ایم.
🔴
ما آماده هستیم، اما هنوز تصمیمی نگرفته‌ایم — نه در دولت فدرال و نه در پارلمان.
🔴
ما باید، البته، همچنین پایه حقوقی را روشن کنیم. این سوالی است که هنوز به طور قاطع حل نکرده‌ایم.
🔴
اما این واقعیت که ما اساساً آماده مشارکت در حفظ این صلح هستیم، برای هفته‌ها موضع مشترک دولت فدرال بوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/128537" target="_blank">📅 20:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128536">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
صدراعظم آلمان مرتس: همه چیزهایی که از ایران می‌شنویم نشان می‌دهد که ایران نیز این موضوع را می‌پذیرد، زیرا با توجه به برتری نظامی آمریکا، به سادگی هیچ انتخاب دیگری ندارد.
🔴
من دیروز عصر به رئیس‌جمهور ترامپ گفتم: می‌توانید از این مثال ببینید که قدرت نظامی شفاف نیز قادر به ایجاد راه‌حل‌های دیپلماتیک است
🔴
و همین موضوع در مورد اوکراین نیز صدق می‌کند، آنگاه ممکن است به صلح در دو مکان حیاتی جهان نزدیک‌تر شویم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/128536" target="_blank">📅 20:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128535">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
کانال ۱۴ عبری : نشست اضطراری تو دفتر نتانیاهو با موضوع ایران و لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/128535" target="_blank">📅 20:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128534">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
سی‌جی‌تی‌ان: یوری اوشاکوف، دستیار ولادیمیر پوتین، رئیس جمهور روسیه اعلام کرد که استیو ویتکاف و جرد کوشنر، نمایندگان آمریکا پس از امضای یادداشت تفاهم با ایران، احتمالا برای مذاکرات درباره اوکراین به مسکو سفر خواهند کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/128534" target="_blank">📅 20:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128533">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
اختلال اینترنت ‌بانک پاسارگاد برطرف شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/128533" target="_blank">📅 20:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128532">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e3d11339e.mp4?token=RPIVihF8idy23xII0h4RkXAr7brUyMZFBIpORvFB7QEYr42nWQCpSqEKDlfFpiGf9NXO-YzmxKlR3W42iEdGKQp2P4K6OsmpSFigcl17qQX3yUDIxOonS3STn2o_NhUjCntqBIeBvW9D4_iPzY8aH3P4cjKEh8qq6z7V62m1VqJiaDmt0UVQuC-S8Sb8ZdayGsFmSmEvrf69z5PiXUgj58zMRF7Ekxg7A1UXZgds34UV4tjaVMFTiiIqQdvhD9UnfAMXhsJXF9zCvYrPgpRBNd03h4nGhumGsAVUD3ZwIqQ4AYa1HMmi7eONnndzhikFZLWgMSQXqhapxJXMBjAPwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e3d11339e.mp4?token=RPIVihF8idy23xII0h4RkXAr7brUyMZFBIpORvFB7QEYr42nWQCpSqEKDlfFpiGf9NXO-YzmxKlR3W42iEdGKQp2P4K6OsmpSFigcl17qQX3yUDIxOonS3STn2o_NhUjCntqBIeBvW9D4_iPzY8aH3P4cjKEh8qq6z7V62m1VqJiaDmt0UVQuC-S8Sb8ZdayGsFmSmEvrf69z5PiXUgj58zMRF7Ekxg7A1UXZgds34UV4tjaVMFTiiIqQdvhD9UnfAMXhsJXF9zCvYrPgpRBNd03h4nGhumGsAVUD3ZwIqQ4AYa1HMmi7eONnndzhikFZLWgMSQXqhapxJXMBjAPwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صدراعظم آلمان، مرتس، در مورد توافق جمهوری اسلامی ایران و ایالات متحده:
من به رئیس‌جمهور ترامپ وعده دادم که می‌خواهیم سهم خود را برای موفقیت صلح انجام دهیم.
🔴
این شامل کمک با ابزارهای نظامی برای امکان‌پذیر کردن حمل‌ونقل آزاد از طریق تنگه هرمز به صورت دائمی نیز می‌شود، به محض برآورده شدن شرایط لازم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/128532" target="_blank">📅 20:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128531">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2668d0c29b.mp4?token=SKe8IdpkLqOmB3HRzlG59yfpgwY165nsWb9S2rf_BVLTlDcRakpujbo962B-_nWM3mVXj7oQckdALF87uWfkLTQ7bhV9KF4zyinpagpaLIIL0k4OLYqRKCDenfdoZeQAZ88f2du9155nBnrNp3X5-EDiRC7flFsmPwbx32gKnVFNOExds7c_lNcMcTLqsjMk6LGhGhFM1o7ku5JDRQItziaVqrd1ozHSNz3QtsAsdKd5Hkq8WaFqES7uWJYA6_fZVVU0XOPiyVpB1tuAG6ElALbGxqO9pOZCneb-1ipw2_0kDIA0zpOH-3EvbqBrr92_Y-q6cm-VEZ9l7X8vcgn_wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2668d0c29b.mp4?token=SKe8IdpkLqOmB3HRzlG59yfpgwY165nsWb9S2rf_BVLTlDcRakpujbo962B-_nWM3mVXj7oQckdALF87uWfkLTQ7bhV9KF4zyinpagpaLIIL0k4OLYqRKCDenfdoZeQAZ88f2du9155nBnrNp3X5-EDiRC7flFsmPwbx32gKnVFNOExds7c_lNcMcTLqsjMk6LGhGhFM1o7ku5JDRQItziaVqrd1ozHSNz3QtsAsdKd5Hkq8WaFqES7uWJYA6_fZVVU0XOPiyVpB1tuAG6ElALbGxqO9pOZCneb-1ipw2_0kDIA0zpOH-3EvbqBrr92_Y-q6cm-VEZ9l7X8vcgn_wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواپیمای نظامی اوکراینی، که به گفته منابع یک جنگنده میگ-۲۹ است، در منطقه خمیلنیتسکی اوکراین سقوط کرد.
🔴
جزئیاتی درباره علت حادثه و وضعیت خلبان هنوز تأیید نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/128531" target="_blank">📅 20:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128530">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utss_j5uclQgJDpZUkk-RSPDjETqgqsI9rDcI__FziIRm9gpSRQZWnpXaEQpYdbh52n-uYkRTpSAzUr3K34Htxp2zs-yNWcKiSf5VBgd-3ni0BzO90KfcFXqYJyI6jR7hmIUYnyDW2ZXkNHyiKz32h97rXRaIzJujuNvQCnsBDmkflB-gai1HZewh2a1sGc8h1XKLJqjg6cW39Wz-L5032arU77utH1lFBncw_IC9sRBeGT5IE1jvfMmckm7SnfH-kjZzbQOmi8MMd1Zey1j0y8vDWyghsPJh28Ik5CUhVdpDtN-W2v9Kqb8SIWqkcw9bCcaZV62Cqdw-jScvAsTAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش شبکه‌ی العربیه از پیش‌نویس توافق ۱۴ ماده‌ای میان تهران و واشینگتن، در متن این یادداشت تفاهم هیچ اشاره‌ای به اسرائیل نشده است.
🔴
این افشاگری در حالی صورت می‌گیرد که جزئیات این توافقِ کلیدی، توجه محافل دیپلماتیک را به خود جلب کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/128530" target="_blank">📅 20:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128529">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
قیمت هرگرم طلای ۱۸ عیار به ۱۵.۴۰۰.۰۰۰ هزارتومن رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/128529" target="_blank">📅 20:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128528">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/023d758892.mp4?token=rGtEHig_zZX3xj95hCC6Dj5PVhMuv1m7qkK6oRibYz05q-qPUD8mkc4cU1JXFXkz-oPxr_8q47fC3-kUooX_vZ41UnRvMU4zj2MNheHiIcHXGzoDOxuqFG090ExTRlhIEHcI9z9wwu0cbo_lgs_Zvvm0SVStPgcLdnsoL2cIWyTK2nfxEPkrBwYFsQ2IPMFoyY_v0j5AsBsRuK8q1kfu_ufIdVeVbt5Xgn93HgPnUPnibw7uMxYvI29gWtIa-rtwXlQCRmgXTJTixqD7vpFThYcVKRM-sFbTgSlwBmvT0adWaLOWQO22veqfqxSE1ITNGi6Z-TQ3NiZhD34jmTMVyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/023d758892.mp4?token=rGtEHig_zZX3xj95hCC6Dj5PVhMuv1m7qkK6oRibYz05q-qPUD8mkc4cU1JXFXkz-oPxr_8q47fC3-kUooX_vZ41UnRvMU4zj2MNheHiIcHXGzoDOxuqFG090ExTRlhIEHcI9z9wwu0cbo_lgs_Zvvm0SVStPgcLdnsoL2cIWyTK2nfxEPkrBwYFsQ2IPMFoyY_v0j5AsBsRuK8q1kfu_ufIdVeVbt5Xgn93HgPnUPnibw7uMxYvI29gWtIa-rtwXlQCRmgXTJTixqD7vpFThYcVKRM-sFbTgSlwBmvT0adWaLOWQO22veqfqxSE1ITNGi6Z-TQ3NiZhD34jmTMVyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات اسرائیل به لبنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/128528" target="_blank">📅 20:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128527">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
خبرگزاری سی‌ان‌ان: برآوردهای اطلاعاتی آمریکا نشان می‌دهد که ایران اکنون می‌تواند هر زمان که بخواهد تنگه هرمز را ببندد. یک منبع اطلاعاتی گفت: ما عملاً کنترل تنگه را به ایران داده‌ایم که سلاحی قوی‌تر از هر سلاح هسته‌ای است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/128527" target="_blank">📅 20:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128526">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
فیصل بن فرحان، وزیر امور خارجه عربستان سعودی از تفاهم میان آمریکا و جمهوری اسلامی ایران استقبال کرد و ابراز امیدواری کرد این تفاهم به بازگشت ثبات در منطقه کمک کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/128526" target="_blank">📅 20:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128525">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3RVmNAaYRI0Al_4_VI_qUEQpN6ADV8gVp1oG0wwHM2ahx8KAzXtVHKPQHsbnsUskEjumEFbl-E0U6CO1GoFlY_J25gIrJKz2gaxYDTa831BIpil_etHq4oQSOmuqMx-Qhd8chNC6OhmveGarTD-03bMZoFwCIMYBAN-IZgnmGhItl2UszIPva-rMY_RVJo_tQDqqW5cGhc9RcwJwyY4HlZqwh6iaqf7bhjD9Hr_Zbh0l8_R05_O7I4c7deqPEP-JnkhVAw6XS4eBHqFY99pZZyCV1nmJYr14m5sYXcSdDTyFyrT3B1CVTn48z7NDfZATPFM6VdAV8XH1SwMrWBlcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بر اساس نظرسنجی مؤسسه کانتار، میزان حمایت از دونالد ترامپ در اسرائیل طی فقط ۳ هفته به‌طور کامل معکوس شده و از مثبت ۲۳ به منفی ۲۳ رسیده؛ افتی ۴۶ واحدی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/128525" target="_blank">📅 20:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128524">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
هم اکنون پرواز پهپاد های اسرائیلی بر فراز لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/128524" target="_blank">📅 20:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128523">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
فوری / منبع به العربیه انگلیسی گفت که ایالات متحده، طبق این تفاهم‌نامه، متعهد به لغو «همه انواع تحریم‌ها» علیه ایران است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/128523" target="_blank">📅 20:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128522">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/164440dd96.mp4?token=JV5tPzVwsssSFFHYMNOoISArg_-LhsGXXbWp4Ey6_HCJD_jrFp29lEF8b_LC0fSD4CzWiSKgIPLXD9qgvqkMAHPgtUrQGHihiRMyBGk8HOm9TTzo2oLx1ckeKRoHC26hy2PEI4c2mSciusAoUW7MrdRVBfVwY90CPNCcHUthQLI33HFHBoCyxIuZZx1QQne7V5BFEDSYefMIjIDdw82chy6ORZkG8aN5nGmef9oBGqrel3EjbjG65tFFRWP6Sa6cdt_hpEj8j4NpkFjuRHnZOVPwaZjvovuxH91QeHL-NfIthzlM7yb0BoaqaogHiM7byZhtdKDZMtZTfqRccf3aOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/164440dd96.mp4?token=JV5tPzVwsssSFFHYMNOoISArg_-LhsGXXbWp4Ey6_HCJD_jrFp29lEF8b_LC0fSD4CzWiSKgIPLXD9qgvqkMAHPgtUrQGHihiRMyBGk8HOm9TTzo2oLx1ckeKRoHC26hy2PEI4c2mSciusAoUW7MrdRVBfVwY90CPNCcHUthQLI33HFHBoCyxIuZZx1QQne7V5BFEDSYefMIjIDdw82chy6ORZkG8aN5nGmef9oBGqrel3EjbjG65tFFRWP6Sa6cdt_hpEj8j4NpkFjuRHnZOVPwaZjvovuxH91QeHL-NfIthzlM7yb0BoaqaogHiM7byZhtdKDZMtZTfqRccf3aOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل: لانچر شلیک راکت تو جنوب لُبنان رو زدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/128522" target="_blank">📅 20:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128521">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
وزیر امور خارجه چین، در تماس تلفنی با محمد اسحاق دار، وزیر امور خارجه پاکستان:
چین معتقد است که در مذاکرات ایران و آمریکا، نباید به عقب برگشت، چه برسد به استفاده از زور.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/128521" target="_blank">📅 20:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128520">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
فوری / منبع به العربیه انگلیسی گفت که ایالات متحده، طبق این تفاهم‌نامه، متعهد به لغو «همه انواع تحریم‌ها» علیه ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/128520" target="_blank">📅 19:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128519">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF): پس از ارزیابی وضعیت، دستورالعمل‌های دفاعی فرماندهی جبهه داخلی بدون تغییر باقی می‌مانند و تا سه‌شنبه، ۱۷ ژوئن ۲۰۲۶، ساعت ۲۰:۰۰، در حال اجرا هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/128519" target="_blank">📅 19:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128518">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxWbGpje-YHywfQQp9jIk0kBIxl6glqsk3m0iRc708XGTg3lNd9T0cihjR6iB0Vjyryfjvt0aB7jf_ui_xquvmlG6WIXGsqfxcBBf5mfdPkkCPR4GnSdq2rgn0MfxHtS1WD8qREXqa9bC5O-6ibPTWFgGKvcDVrktFtu2l6WkHnupT6C9hfNZV8aJ2Jw7fZL9mq-meuWqFT6fvV8X_ZaXDx3QAgMNZ3pHCO91l9BNHhBh9E5C2lZu_SIG6l6zanDC-xLaSHkgXeCbWG42a_kkYjstxx4xcnHYnjwvlmuAv1mm_g3jS7Nc-hOsR9NAjutKOjT5SAIKjzj7lMH68F3EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بر اساس گزارش بلومبرگ، توافق صلح با ایران و بازگشایی تنگه هرمز در کانون توجه اجلاس سالانه گروه هفت قرار گرفته است.
🔴
اگرچه متن نهایی این توافق هنوز به‌طور رسمی منتشر نشده، اما سران کشورها بر سر امضای آن در روز جمعه به توافق رسیده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/128518" target="_blank">📅 19:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128517">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
رایزنی وزرای خارجه ایران و عمان درباره تنگه هرمز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/128517" target="_blank">📅 19:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128516">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
وال استریت ژورنال به نقل از یک منبع:
تفاهم اولیه آمریکا و ایران به تهران اجازه می‌دهد فوراً نفت بفروشد
🔴
واشینگتن به تهران اجازه خواهد داد تا طبق توافق پایان جنگ، فوراً فروش نفت و سوخت را آغاز کند
🔴
معافیت‌های ایران شامل خدماتی می‌شود که فروش نفت را تسهیل می‌کنند، از جمله بانکداری، حمل و نقل و بیمه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/128516" target="_blank">📅 19:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128515">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
اف‌بی‌آی یک طرح تروریستی عظیم و چند مرحله‌ای را که هدف آن رویداد یو‌اف‌سی فریدام 250 روز یکشنبه در چمنزار جنوبی کاخ سفید بود، خنثی کرد.
🔴
طبق گفته مقامات فدرال، این طرح ترسناک طوری طراحی شده بود که «حداکثر تلفات» را به همراه داشته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/128515" target="_blank">📅 19:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128514">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff6b516f19.mp4?token=nGQoaXJb0d3SDkYMufEfH6as9bWCL65qYwoixUI3qmIPMc2oRw3SCilBNof6zCSY2z8kmJAYqJMYh2e6JQoIGw5c8aB2Gyy3bfGHKHfqKOUJLrPceYF196VnRzXWxfJdcoWUWNAsSuheCeQ-u1LqcqGWyw6LjO0ZtEcXqFI5Yo_qFDuHDAQjuz26BOreoIea-ordj5OK33jLC1dyTG909Fj7XNrEJJc3jDVhcfVIeuZgyL3uRLPuMCCf4LFOA19Ce7Yruz204yMFw5ktLVYyyBJSD41Kl2nbWiuJ5BzjMSj3If7F6aSemdtGcbzOc2FmWh6o-FVHVl55SBI6ylIZ0iva1ddtRTwxpNhzRuFyv9PYWPUQ177e0AA-bkLqcUdsO-u93tP3ZFA1xmUsFK5x8xM8uZOZk1Z8b11fTEkoro5o50QJFyH9u-X7tqD2l4tBOZKAeRwpBEOSLjHrhkOxKcyKLUHy9eV18oj1BG-kos6UqAeNgO2hjwmQ9TXYDMF0P6CQmBmKtHOuakvYqAsVfCFP-t0u3k2JzKr7E3axehNZMUkHu7qP6_nC-ESimqm54zaMI-Wvfkf3aywNKkz9NzJlvimZ2n9XO8CRDkFI9Jeeu3851_k1e73IfM9zGQdX7jY2pZVmBOzB0MEM585GvF1HX7RefAiFmh7EBM1HhCY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff6b516f19.mp4?token=nGQoaXJb0d3SDkYMufEfH6as9bWCL65qYwoixUI3qmIPMc2oRw3SCilBNof6zCSY2z8kmJAYqJMYh2e6JQoIGw5c8aB2Gyy3bfGHKHfqKOUJLrPceYF196VnRzXWxfJdcoWUWNAsSuheCeQ-u1LqcqGWyw6LjO0ZtEcXqFI5Yo_qFDuHDAQjuz26BOreoIea-ordj5OK33jLC1dyTG909Fj7XNrEJJc3jDVhcfVIeuZgyL3uRLPuMCCf4LFOA19Ce7Yruz204yMFw5ktLVYyyBJSD41Kl2nbWiuJ5BzjMSj3If7F6aSemdtGcbzOc2FmWh6o-FVHVl55SBI6ylIZ0iva1ddtRTwxpNhzRuFyv9PYWPUQ177e0AA-bkLqcUdsO-u93tP3ZFA1xmUsFK5x8xM8uZOZk1Z8b11fTEkoro5o50QJFyH9u-X7tqD2l4tBOZKAeRwpBEOSLjHrhkOxKcyKLUHy9eV18oj1BG-kos6UqAeNgO2hjwmQ9TXYDMF0P6CQmBmKtHOuakvYqAsVfCFP-t0u3k2JzKr7E3axehNZMUkHu7qP6_nC-ESimqm54zaMI-Wvfkf3aywNKkz9NzJlvimZ2n9XO8CRDkFI9Jeeu3851_k1e73IfM9zGQdX7jY2pZVmBOzB0MEM585GvF1HX7RefAiFmh7EBM1HhCY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حزب‌الله یه خودرو نظامی ارتش اسرائیل رو با پهپاد «ابابیل» زد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/128514" target="_blank">📅 19:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128513">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4bpnfG8gqprJhKfQ2FOaB5MXH4gk7mxYzHCWV-d13cBlri12ciI9wDw1iGFLq7LiBGv9zjvh4Ov005_SHKRPapz0RXiLJE2p2jq1bbF8puwpvvM7N7BynKA-DVKEHVKfkS0-hZaRuUJ6Q8Gi6OqU_J8cYvpXDuYYo8H-tDP6oBlHu0m68Qn0rNQsqqSPtXvsaf6HzQoTRx620mTjrfAvc01YnV8d1YK0uJf3ZGkSBya1zmvjcHQ6WR7dNMSzx2OAsmT6HLpq2gBvRc0omCKFz5FQwIQMCkNoRFhvJsooSzjjg8tR5nujRuyymEUCFZzj3Ky0i9zGxMZpwIY82YHgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: ‏آنچه تفاهم شده، گامی مهم برای توقف جنگ و شروع مذاکره است
🔴
تمرکز دولت با یا بدون توافق خدمت صادقانه به مردم است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/128513" target="_blank">📅 19:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128512">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EnUfWzLF153LNAK4b-uJSLWUeze3SqI-rY0rrAQJ_oZQgXYZmRpTZoCkp9OBgOvT3kmfTu4ezWSe8JgrHmop0HYFXnFMTPKHu7xsYzjIBFoSB_BFlCimE3YhCOwk3_sLILn-ZC6uZomgTGaRpqW7byiCZpb2o_BDc8gyzo_vR7G-UfCTIg19f77BDG7HfyDdLCLyoH1Bzt7XCZKmEFuZ4GJG-GUjnbgcMFO3OIWR45VsdS5AE024iY8xgOTPcs2NGQrMt8QCu-HrF46fkoHvTxRsrztevVKP3c1BpzsCSqYqZtzCBfLhQvHRqvyobl2jXIcA1WHr-jQxV2uIs0pwMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تتر به ۱۵۵ هزار تومن رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/128512" target="_blank">📅 19:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128511">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
توپخانه ارتش اسرائیل (IDF) شهر مجدال زون و همچنین حومه المنصوری در جنوب لبنان را هدف قرار داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/128511" target="_blank">📅 18:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128510">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSSMco_ST_4CoDwLC3ELEYQJoj3MQ3Es3KBhnCI2BVjzA5rb6LTXVAGrHHqBPESdqfxT_8_Z9l379zjxDNZSoML0q7L4cTav9ql0yTdS7ltq_O_JkcGPa0Vihtahy8QO00-_OdteTwe5dVbkY_cc5T3Jo4zGRgdi-1jNmpKMnqSuYnFSBKiabjtVAgt8raKJ_QtvDGcPPXaAU9dJ7VJF4VwttW0HAEgOk-bTjFIdvzuVeYLuD4LQceQ_VPW1N1cW56H6iMw4Qxrd-EJaTXhWeuQ5hso7_pmYyQCrkLqInSBwhzD4nt-xuVFKDgbcOzyZS9OVqnxz98Lngk9a6dUgxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
ویتنی رایت پورن استار آمریکایی تصاویر جدیدی از حضورش در تهران منتشر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/128510" target="_blank">📅 18:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128509">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/023d758892.mp4?token=pJxErUXSIB9K5Pk-icFWvo-3UpVR83ZGRwmmd4HUP9GSTgldSqIu8T35d7iTDY8VY_w8WpxqfVpDuuQi6HqgMgimBknRA726qeYjQQr_cgzPLIVV1f-aDvjxuD8dBBPDXdNdowJ_heNka9NR95TW0X1yiKjAAM-dIaph-Z0thVXHqm1HWAwxKzAbQ1iGGOfEzU-9FCJerUTKm-kdQatxU_F-7iHtmXiNzUyIIgUmBadDULq2SuZ7EIxGVySwwRMW-KMsh0_2_lZ47rFcDryQ_o_WMLxzoe4LU5mqfzw6Ku-8662FiQKDcMUfQZuhhXSZxhxLdLihofNuthJnWb_5BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/023d758892.mp4?token=pJxErUXSIB9K5Pk-icFWvo-3UpVR83ZGRwmmd4HUP9GSTgldSqIu8T35d7iTDY8VY_w8WpxqfVpDuuQi6HqgMgimBknRA726qeYjQQr_cgzPLIVV1f-aDvjxuD8dBBPDXdNdowJ_heNka9NR95TW0X1yiKjAAM-dIaph-Z0thVXHqm1HWAwxKzAbQ1iGGOfEzU-9FCJerUTKm-kdQatxU_F-7iHtmXiNzUyIIgUmBadDULq2SuZ7EIxGVySwwRMW-KMsh0_2_lZ47rFcDryQ_o_WMLxzoe4LU5mqfzw6Ku-8662FiQKDcMUfQZuhhXSZxhxLdLihofNuthJnWb_5BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات اسرائیل به لبنان ادامه داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/alonews/128509" target="_blank">📅 18:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128508">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfsVcat32lukRwHhQ2JIMYkBgh_hK8mvzbChCjss-obgXWDysT2X3EfiZ6fDeC4e77LxZBzhvmfTnd_hB5pw-UOgfOjLjXSGexKCpQ_N0cRnu_saRl4d6piFFmXs9f36Y8ueIKUMMXnOhGoOHNyYrO6GFgEOrkQ2jMulMWau2pdZjAYf_LkfpcOJgQqgtOXqNeN15I2KiukB97FXxijU_B0z-fH8Pw7QlAwkdsGCrPbnoXCQ-1cmW03pAS2UqH04t9OeGbqHt_Rld5DPc65ENZYOAwzU6DgA0mNDR9WYswK8_Fh7OmZ7h8NjjNi24sQrWvuEIB7bbFlMEvXqVNp0PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خانعلی زاده مجری صدا و سیما در ونزوئلا قبل سقوط: اوضاع اینجا عالیه و همه چی اوکیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128508" target="_blank">📅 18:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128507">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34b13e4ca3.mp4?token=erjPsDIR8wzQ5_gFsh3Sy2UvwHXonQXd7JOQhwC9zsNxKH_pUO--EgWNymkd9QM3XQae3gxTsghrs786Bg6iCKgXCTPG_Ds7oRz4LyVNs96YB9Wlh5zBujYFn46-r2FjVCLS9n2ibI8t6UT3oP_rSyuQY-8mKKhPOZwVoP3-GSHn6VRbg5YI1CPC1G9Iyu52JDLuFha0cdzl935Pp9sa-NaWk38nVMFTKzSJuzz6tDgfY3erOa0AvcPGcBaaX1xngL-SiuF6GlpT6wA-QHGrwCB4XKcYVypqA0knU5WWbROLJsLzDOsu1oudowD_hoptdc4aLMCwO5G6e4ZpkXXFh5y4oX3vdJo7i1Vtp3q2a9vwLz7RczbEmPQXs0-PO1mUg9uQ3W0V5M2nKAq8uM6VM5OMGsRORjtl6OyKoaVUSaYTxmSw3O7YOudEgwRMj7W72pSOyalGx6kgcXK5HgeFg00aKIquTnIwXEgJwkkhNwvI70a8eEqFKATYGxRGDi5dWIPVIXXMc7gXe56QuBEP7dZt_elG6DyWydCz7Oe9YFQpN9GPStlwxTJypmSKaN1j4zXyEinw1WjNtxZur-_o-dE-x22ec8i9VzuMAP1Jk2FfZq_6JV68YZRGzb_YCcwVk7qYaPv0d1f-xqbUFDKdNQGx78ye8ACth769UdsPWmU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34b13e4ca3.mp4?token=erjPsDIR8wzQ5_gFsh3Sy2UvwHXonQXd7JOQhwC9zsNxKH_pUO--EgWNymkd9QM3XQae3gxTsghrs786Bg6iCKgXCTPG_Ds7oRz4LyVNs96YB9Wlh5zBujYFn46-r2FjVCLS9n2ibI8t6UT3oP_rSyuQY-8mKKhPOZwVoP3-GSHn6VRbg5YI1CPC1G9Iyu52JDLuFha0cdzl935Pp9sa-NaWk38nVMFTKzSJuzz6tDgfY3erOa0AvcPGcBaaX1xngL-SiuF6GlpT6wA-QHGrwCB4XKcYVypqA0knU5WWbROLJsLzDOsu1oudowD_hoptdc4aLMCwO5G6e4ZpkXXFh5y4oX3vdJo7i1Vtp3q2a9vwLz7RczbEmPQXs0-PO1mUg9uQ3W0V5M2nKAq8uM6VM5OMGsRORjtl6OyKoaVUSaYTxmSw3O7YOudEgwRMj7W72pSOyalGx6kgcXK5HgeFg00aKIquTnIwXEgJwkkhNwvI70a8eEqFKATYGxRGDi5dWIPVIXXMc7gXe56QuBEP7dZt_elG6DyWydCz7Oe9YFQpN9GPStlwxTJypmSKaN1j4zXyEinw1WjNtxZur-_o-dE-x22ec8i9VzuMAP1Jk2FfZq_6JV68YZRGzb_YCcwVk7qYaPv0d1f-xqbUFDKdNQGx78ye8ACth769UdsPWmU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تغییر رژیم به سریال‌ها هم رسیده
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/128507" target="_blank">📅 18:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128506">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7b5a68df5.mp4?token=UfYhzYns8deD8Dr_CdTOo___sk-TFtDNALJOE4C5_xZBIdyuZfYTTrKxActgQ4OazmgosfZbggzIFzlhCPikg4I1RuHGiH-URB52QiUU-LEsr9R41uNLcwv92MctHbeZ-OGPa2lmod20vX2vk5qrN10xbaMRRv8xw4jFXbHbbWvsxMDzmuU6vh-JmmJGn67kaRN71Di-2JOAS3JA96tPMx_IPzMH5rEE-OfiPYNZAjUk3GMZhN67u4murZAK2b8XpKpPx9gXpLKyonJvCrA4ihz8WbW2WYjhwGc4gjJrAJb3qb5OxJXzoeE_xbhyTIxhBddp_uAwG5n__MVbrG46Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7b5a68df5.mp4?token=UfYhzYns8deD8Dr_CdTOo___sk-TFtDNALJOE4C5_xZBIdyuZfYTTrKxActgQ4OazmgosfZbggzIFzlhCPikg4I1RuHGiH-URB52QiUU-LEsr9R41uNLcwv92MctHbeZ-OGPa2lmod20vX2vk5qrN10xbaMRRv8xw4jFXbHbbWvsxMDzmuU6vh-JmmJGn67kaRN71Di-2JOAS3JA96tPMx_IPzMH5rEE-OfiPYNZAjUk3GMZhN67u4murZAK2b8XpKpPx9gXpLKyonJvCrA4ihz8WbW2WYjhwGc4gjJrAJb3qb5OxJXzoeE_xbhyTIxhBddp_uAwG5n__MVbrG46Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس فاکس‌نیوز: زمانی هدف ترامپ تسلیم بی قید و شرط ایران بود
بریت هیوم:
🔴
اگر تمام چیزهایی که رئیس جمهور ترامپ ادعا می‌کند که در توافق هست، در توافق باشد و به آنها پایبند باشیم، احتمالاً یک پیروزی بزرگ خواهد بود.
🔴
اما او به دلیل حرف‌های گزافی که در مورد دستاوردهای اولیه ما زده، کمی در موقعیت نامساعد سیاسی قرار دارد. هدفی که او زمانی گفته بود تسلیم بی‌قید و شرط ایران بود.
🔴
ایران چیزهای زیادی از دست داده است، اما این تسلیم بی‌قید و شرط نیست، این چیزی است که وقتی مذاکره می‌کنید به دست می‌آورید. دولت به وضوح در اینجا کمی عقب‌نشینی کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/128506" target="_blank">📅 18:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128505">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veWXJgP7G32wt-8LO4D3xUdammsLug5UHSzOcr7DSdh5iL_VNTdh3nBbP4lTQuNqD5k6ZAkvsQk7XvYjdgD8pCSoS2Oedica9EMEDetJSdz-lFuTuNyEiLIWOZ47ZZx_wFRhve_uJByQb39Dd0kyoPSnaJeqfBZ3_1Y-PrP45QTNATVlmmN_sMkwaJhzKcGjKAmuFHx2QA1Keuv5mG0tDoe4wPPGXeg8VUTaoKx_7_TNqidqgxPyWwt6Km2ucjbKfCRV0cwu1LQZkdl2jw8Iomngp588d0ciGsBP5GTFSSgM25aRRUgOefF-5JrWYX8U4C8Z4FpaDTWqllfhkhtOkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عکس
یادگاری سران G7
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128505" target="_blank">📅 18:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128504">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a196a552c3.mp4?token=ImXj-NIeHwek3PWpWdmhI8nIpTb5tf9HsajM9fI0GVm3iecXz91qcBJrVGtQ3iMJXvzdNNrp4lv67ueekwXpElgavGR7pQYrCU-a7JqOgLwSJ5e2IXe2pH43InWqi5KPNcDh_5yWORCWOp9pmVDvEkXldHdIYrJHrFF1k15EsGcb9St8HmeXEH_biyCtAcfmcFI_XXbkid1UU0ysv6dZ0XWDX0fpcZ7oRq89FYh0xclivjVipHy71e9o_6skgQ3daViA-6Qb4HJLJMOWIem4pgDkLrX1tR5-RKj5vKQY2i6j8ejUDrI2pSqhO_0vMLtf6fzlxtLF0yVZcH3yF-wB0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a196a552c3.mp4?token=ImXj-NIeHwek3PWpWdmhI8nIpTb5tf9HsajM9fI0GVm3iecXz91qcBJrVGtQ3iMJXvzdNNrp4lv67ueekwXpElgavGR7pQYrCU-a7JqOgLwSJ5e2IXe2pH43InWqi5KPNcDh_5yWORCWOp9pmVDvEkXldHdIYrJHrFF1k15EsGcb9St8HmeXEH_biyCtAcfmcFI_XXbkid1UU0ysv6dZ0XWDX0fpcZ7oRq89FYh0xclivjVipHy71e9o_6skgQ3daViA-6Qb4HJLJMOWIem4pgDkLrX1tR5-RKj5vKQY2i6j8ejUDrI2pSqhO_0vMLtf6fzlxtLF0yVZcH3yF-wB0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون رئیس‌جمهور جِی‌دی ونس
:
اگر مردم ایران خواهان رفاه بیشتر هستند، رهبرانشان باید پیشقدم شوند و رفتار خود را تغییر دهند.
اگر این کار را بکنند، عالی است. اگر نکنند، ایالات متحده قبلاً چیزهای زیادی به دست آورده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/128504" target="_blank">📅 18:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128503">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
ونس به فاکس نیوز:
ما پیروز شدیم، چه ایران روش خود را تغییر دهد و چه تصمیم بگیرد به توافق پایبند نباشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128503" target="_blank">📅 18:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128502">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/c96ac20501.mp4?token=kpabYDiOM_RW3A86AkhbYUL5zWIrjgV2eojlJifMIeOiGUmKAw1aqC9uv3xZ4dExhmDBlIeFC3_1FEU8RzlUxHUZkesyF-RyB1sH5WvvQzpGJnM_plbhhQF7iJWasmrPSteFpGauVF0e-FKKDQP54JTe6ZyLjW2AWrIEIHM6YF4iEW0-A2wVTU_cgM_0PYNu8oT-Pbswi81w8qfcl0aZiLpd6iN_25ZJKrZzs4rlGVOWXMBU-bEXm8En6xDQDM0kKpuCTrRVxxBIeR1L_wHKZFqFcOPHpGad5gbA9fmoRkyxD4zwUby1-xsigpMw5TqoZMagyIjA-iM3Q-5cVeJkyg" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/c96ac20501.mp4?token=kpabYDiOM_RW3A86AkhbYUL5zWIrjgV2eojlJifMIeOiGUmKAw1aqC9uv3xZ4dExhmDBlIeFC3_1FEU8RzlUxHUZkesyF-RyB1sH5WvvQzpGJnM_plbhhQF7iJWasmrPSteFpGauVF0e-FKKDQP54JTe6ZyLjW2AWrIEIHM6YF4iEW0-A2wVTU_cgM_0PYNu8oT-Pbswi81w8qfcl0aZiLpd6iN_25ZJKrZzs4rlGVOWXMBU-bEXm8En6xDQDM0kKpuCTrRVxxBIeR1L_wHKZFqFcOPHpGad5gbA9fmoRkyxD4zwUby1-xsigpMw5TqoZMagyIjA-iM3Q-5cVeJkyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله پهبادی اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/128502" target="_blank">📅 18:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128501">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">پاسخ قاطع قالیباف به مخالفان توافق  [@AloTweet]</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128501" target="_blank">📅 17:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128500">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esp0ERUlLcatxbQBcEoMDAtxsGChIu_EF_AKz_LppRe41vj-JTg-8wCHCP2sjVLLASEhnxVg3j9C6q3QlMgxpkPCIXL2tViItP7MIPnikH5taaBzJ9C7PF6so6c_pT97k9QupMRqqB6j6UnTmZmL4vrN-DNCYUbRZaaj0b9i94apD5EWk7JfklXTN0jEANx0PuA9sJcCbT_3Q638wHggdvQKAk_glhPgGO1XCEFD2VXy3pdxPfVJWaxEvSN56J4z5tomi9LR3UkBNcTSBvYuF45QuyUIGKFLwCJWWfhkapyja3p_7ZMZ1qXpULtqmYYlRkU7vva22B3ZCtgVNdxNKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبویان :متن توافق منافع ملی(کاسبان تحریم) را تامین نمیکند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/128500" target="_blank">📅 17:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128499">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل:
نتانیاهو خواسته متن توافق با ایران رو ببینه ولی ترامپ اجازه نداده و گفته به تو مربوط نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/128499" target="_blank">📅 17:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128497">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aJGPGnlxvi955M74UMkYG3XZMOq2JEq7rIyeialDZSBYaA6V7iStXf2j86ykyRkxtDwXtkva2ES2RnQh5UaOOe9KguucGaoz5olnUhJvwWtNmvFQDBSkF-ngHvvITE3H9hoYIeWQrIwB3Ow6FoXYSNcas4qblTCh44qWB5XX190wCG1KS_u1Kid2e4SzPRXTouBqI2ytpGZQLzpJV1vuld6KETVxfusRrvRtYJ6q22Wg3lT1t7SFUpPeE_jE-kd0gL0-Y5KObSOAFyBm-cvBfPqLb8UqqiATfKFCHj6_lrDRgjhOYk4KzZnrp1bma5v6HQHuO_b96yc-a2nNplHT3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cb1zkUR48TqnVrJtZquyzFnPhD1xc1YPJDo3vNfxfNDDA2KGUCFe2x09N9tSRcTPY7UztyXpH34gdjZqxfyDRAHAzTca4aF8yBgUED3p7PrVAxcXE0-fEPDAxPfaFxde4vh69K1p32cCVVGUs0AvJWGnxoQOTehhKmDBqkHDKXSZ6iyBHhhH1cwnDUSA-f31HVgsXi1zXxg6cQ8-3rE4nVtxuHIfhIt7qdUlu8-0ISHHL-WGaJjQyRLfLu5G-JTGX3opduTXZh7VSajKkqjTogaAxIcR_3QfL-V1UQ5HwCJqlToTGDdvxHcC9aka_hcMSCruvZCxpr-mi-MGj2qsTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
واشنگتن پست بخشی از مکالمه کوشنر با قالیباف را منتشر کرد
در بخشی از گزارش واشنگتن پست آمده است:
🔴
طبق گفته یک مقام نزدیک به مذاکرات، وقتی «کوشنر» در ماه آوریل در اسلام‌آباد با «محمدباقر قالیباف»، رئیس مجلس ایران، دیدار کرد، صریحاً به او گفت: «ببین، اگر شما بهایی اندازه رولز رویس را می‌خواهید، ما هم محصولی همانند رولز رویس را می‌خواهیم.»
🔴
به عبارت دیگر، اگر ایران با باز نگه داشتن تنگه هرمز، توقف غنی‌سازی اورانیوم به مدت ۲۰ سال و متوقف کردن صدور انقلاب خود، به تعهداتش عمل کند، می‌تواند انتظار دریافت صدها میلیارد دلار منفعت را داشته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/128497" target="_blank">📅 17:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128496">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a6909ecd3.mp4?token=RQ7RJXuBSbMzgbyGs-gZd718n35jNiIlX1hwp-WhIWg8CwFtKzfkU3ZYB3i6opXcz5zzXjaVyY4lgVXpd75_37Y6oPYW_DzzFVAEJJSHyjgrXa4arWaOAH3h85f2OV90iVdMnuBiCA5Lmfhj-VZKO-3_Y6euEBhzh8ur3Z96R-8nKdZqElCH-bOvFYCqh9ywAzskFkaojbMhMomWK6mGpFDcQnVyN-r8PE5Qbk1E-QhkJOeTNOJctEboi5TSUNht5GWupV8ciwq9xFGFDcizuimmt1J_vL0TyObFnftxyL38ScLnFdpMTiU4iQzQMV-OuT6DK9K1DvbbyvA_tv9OTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a6909ecd3.mp4?token=RQ7RJXuBSbMzgbyGs-gZd718n35jNiIlX1hwp-WhIWg8CwFtKzfkU3ZYB3i6opXcz5zzXjaVyY4lgVXpd75_37Y6oPYW_DzzFVAEJJSHyjgrXa4arWaOAH3h85f2OV90iVdMnuBiCA5Lmfhj-VZKO-3_Y6euEBhzh8ur3Z96R-8nKdZqElCH-bOvFYCqh9ywAzskFkaojbMhMomWK6mGpFDcQnVyN-r8PE5Qbk1E-QhkJOeTNOJctEboi5TSUNht5GWupV8ciwq9xFGFDcizuimmt1J_vL0TyObFnftxyL38ScLnFdpMTiU4iQzQMV-OuT6DK9K1DvbbyvA_tv9OTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک روحانی تندرو: ترامپ راست میگه رژیم ایران تغییر کرده. اون صادقترین آدم روی زمینه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/128496" target="_blank">📅 17:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128495">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udRSq8HZ9qBYrFJI77ePxL4ZsGgXQeSRhh-E6aV3vA6PxLfAM5SkylaotLhL4dawfE12UwZey9xIiarRoaEE3BGtpQQGi0NcOgNwY-omxGOcvceQML86oJCaobBi3Mux4k_Xu2XzY4npw4nGrOLP1vIwR97ghhqDCP1P3YBJkBvW0KvxOJB-sbHpITWl3KuvBWjLFeMMmclnnhdSskQFErqXf5y3sLSYdKaU4E6JJJph56486sbP3M4lYhpdtxqM1rFPXjok47yyjENogTuC5mXXOUByKoq6RO5v9MBQiY_X7FA9BXoOlznnTXK8TCW5N3Lck3OlHowOoOIlQDskqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سوئیس محل امضای تفاهم میان ایران و آمریکا را مشخص کرد
🔴
وزارت امور خارجه سوئیس با صدور بیانیه‌ای رسمی تأیید کرد که مراسم امضای توافق‌نامه میان ایالات متحده و جمهوری اسلامی ایران روز جمعه برگزار خواهد شد.
🔴
این مراسم در مجتمع «بورگن‌اشتوک» (Bürgenstock) در سوئیس میزبانی می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128495" target="_blank">📅 17:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128494">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه قطر: قطر در دیدار آتی ژنو حضور خواهد داشت
🔴
توافق فعلی گامی نخست به سوی یک توافق منطقه‌ای گسترده‌تر است که ثبات منطقه را تضمین می‌کند.
🔴
ما در نزدیک کردن دیدگاه‌ها برای دستیابی به یک تسویه میان تهران و واشنگتن کمک کردیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/128494" target="_blank">📅 17:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128492">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHBZ2k7zZpuf5PdBThvRTVrGFZUrc4H0ecc5hy2yXSMP4QdYO5wp-72UhLBkKi7iPO7FvdRwGjGb8h45vP_siElv8WAumVKTM-bAZLbNTf0Yhy--HfpcOGhG7DETYtw4yJdzRcAAqGXGbXLDs1ISNdjGeCVEPNfnxc70WvFaYK5jl6gbj7OEXD86yzPKqxKXCOFVPRBRub1vtkFP0gBpkxQDJIyBPB8DT6GldZqRHkSAqropmUNLuIEk9dJv1tlGAWoAwaqOjtqo1ii2lCXzkFhSIL0W2Ss508-VHSJ47zJU6bU1FEeh6SPseFa9bMaD1_BTmrPhV4NprldBSjIEOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجید تخت‌روانچی، معاون سیاسی وزیر امور خارجه، روز سه‌شنبه ۲۶ خرداد، در حاشیه نشست با دیپلمات‌های خارجی در تهران، جزئیات جدیدی از گام‌های اجرایی تفاهم‌نامه اسلام‌آباد ارائه داد. او تایید کرد که محمدباقر قالیباف از سوی جمهوری اسلامی و جی‌دی ونس از طرف آمریکا برای آغاز مذاکرات و امضای توافق در سوئیس حاضر خواهند بود.
🔴
تخت‌روانچی با اشاره به اینکه بلافاصله پس از امضای تفاهم‌نامه، گفتگوها درباره توافق نهایی شروع می‌شود، افزود: «ما در این مرحله وارد جزئیات بحث‌های هسته‌ای از جمله غنی‌سازی، ذخایر و نیازهای ایران نشده‌ایم و این مباحث پس از رسمیت یافتن تفاهم‌نامه آغاز خواهد شد.»
🔴
معاون وزیر خارجه در پاسخ به پرسشی درباره نقض آتش‌بس از سوی اسرائیل تاکید کرد که در متن تفاهم‌نامه بر خاتمه عملیات نظامی در تمامی جبهه‌ها، از جمله لبنان، صراحت وجود دارد. او تصریح کرد از آنجا که آمریکا از طرف شرکای خود متعهد به پایان جنگ شده است، در صورت هرگونه نقض عهد از سوی اسرائیل، از مکانیزم‌های پیش‌بینی‌شده در یادداشت تفاهم استفاده خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/128492" target="_blank">📅 17:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128491">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y88DFpqMIctW-KzS0UxZaG5cetvee8cbhQCOyxxKAsiT5V9dzcWxO2eDPyiTtyhzfznVm_rgU0dQ17uW2sKMFnLtRa3zHoeUAZomS_IIjL58JTNfmMP9sO-VFW2xSvYg1n3_tn2r3506qpwLHxatDdWqVOq0gsuK0ZZjn4pm4t3vjrqJXdUqixmJ6pczbGIgvVjUpEWsRQjJVT39mxiOKN52fHJXEqPs013bO0mEmCvu1uLmlv7pv2K6lf32NuIrvYVIsCm32BoB8viRz8NzLOvHt0qDBFJzNqNlDi_0nfEnDvaRpU4mHyy9FG9EjfiAJdxlwIj8upjCrehTy-1Bsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس کمیسیون اروپا: من به ترامپ به خاطر توافق با ایران تبریک گفتم هر دو موافقیم که این توافق باید به معنای پایان قطعی برنامه هسته‌ای ایران باشد ،تنگه هرمز بازگشایی خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/128491" target="_blank">📅 17:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128490">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0zdEZseoT2beTWTZe6eVsUJhdmKIOJFclJWsrlChCdn6CXIZ6H5MH-R8WV9dHzZVb45R0kqQdwwqyVD2gkcbhM--8vws0qoT6mjuD9ssbL99CwHFz9bbuClMwtpXEAhLCVF8bt7lB1WNj6raaBFFRwsObjrMDTEYI9N1dSODoY1neTPWsca3x4ODZZpUAE4_jCV_lKShemOlplldojCysva7JfbH_prOo9EPZ4sAwzwStg4rh4k97ZYApsPYN-rrPfiKqoC4tlFzDcayuQnxzepSGwiKJxODFdprahtAvAucb6EmMFaS1AjxVmMxsUYCDyJPle9JC2NKqJ7Uk3HGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی ایران در رتبۀ چهارم؛ پرتماشاگرترین بازی‌های جام جهانی تا اینجا
@AloSport</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/128490" target="_blank">📅 17:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128489">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f469266c7.mp4?token=Lm-cRc3qxWSoFOalDHZWj7p4SGebt9EdpOSj-u2Ais--hYH9hku3AOaWc4bSwJjWw2ehTby_FLEQkBTVc96v-Po3Xg6m4dXZ-1bi-eauoX4mhWrVd5v_A-CCBmjbJo-dwrduKwqA10jhJKYHU6iEq9X7QM78f9Y6v8xgW2BEChJJs5CUwuEY0Q5VyhH3hGmVpxni4oVyWOuvYfeA5Wya9Um5hx1ZhnXujx6L0ez8IzPghv3JKo5LmXFLh95EjcFjZnN1X8m2mp0Kaep4-02-p6YOUz8WEY4Yc2uSHQE052qPhKNZIfVHeTOmvZsszIZAbdXdatYezf9anHJoqD9oAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f469266c7.mp4?token=Lm-cRc3qxWSoFOalDHZWj7p4SGebt9EdpOSj-u2Ais--hYH9hku3AOaWc4bSwJjWw2ehTby_FLEQkBTVc96v-Po3Xg6m4dXZ-1bi-eauoX4mhWrVd5v_A-CCBmjbJo-dwrduKwqA10jhJKYHU6iEq9X7QM78f9Y6v8xgW2BEChJJs5CUwuEY0Q5VyhH3hGmVpxni4oVyWOuvYfeA5Wya9Um5hx1ZhnXujx6L0ez8IzPghv3JKo5LmXFLh95EjcFjZnN1X8m2mp0Kaep4-02-p6YOUz8WEY4Yc2uSHQE052qPhKNZIfVHeTOmvZsszIZAbdXdatYezf9anHJoqD9oAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
دقیقا حرف ما هم همینه. میگیم چرا وقتی حکومتی که 47 ساله داره دروغ به خورد ملت ایران میده رو, باید حمایت کرد!
🔴
تا وقتی که به مردم نیاز دارن صحبت از وطن و ملی گرایی میکنن و وقتی نیازی نباشه بهشون به راحتی پشت پا میزنن.
🤔
حکومت دیگه چیکار باید بکنه تا عرزشی جماعت بفهمه که بازیچه یه مشت شیاده
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/128489" target="_blank">📅 17:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128488">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dd7a8dd9c.mp4?token=UpsP60xlqCzuOACic9FmijizfRRID5xngHg66dkoJl8fOpbdchorVGNiC7UtW2xsQlJN8c3JHtKaAQxu7HSPWjoW7jg5ZK4qpIo7L_jsaNTatFaawNlYEHFPtFrzRkhJP1Cwf1m_XVeGnlhjKq4UPCwHrwyca5vFonhh7E1DYNtyJEFNFxy4Q2wYlcnjvLMZElcIQPqMRXDBCKmLV09GoqAiQlRTlNHoldBirNEYvuj9aFPtQJI8Rx7AJtc8Prj0Cjb7D3kK6ay-6fKrI42CzxeShIRNkxdLsQnDZWI0O-WwxuZ6ZL_bo7ZIxM7DrcHl-TfsnYTybiHjqQZr4gojyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dd7a8dd9c.mp4?token=UpsP60xlqCzuOACic9FmijizfRRID5xngHg66dkoJl8fOpbdchorVGNiC7UtW2xsQlJN8c3JHtKaAQxu7HSPWjoW7jg5ZK4qpIo7L_jsaNTatFaawNlYEHFPtFrzRkhJP1Cwf1m_XVeGnlhjKq4UPCwHrwyca5vFonhh7E1DYNtyJEFNFxy4Q2wYlcnjvLMZElcIQPqMRXDBCKmLV09GoqAiQlRTlNHoldBirNEYvuj9aFPtQJI8Rx7AJtc8Prj0Cjb7D3kK6ay-6fKrI42CzxeShIRNkxdLsQnDZWI0O-WwxuZ6ZL_bo7ZIxM7DrcHl-TfsnYTybiHjqQZr4gojyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عضو تیم رسانه‌ای هیأت مذاکره‌کننده هسته‌ای ایران :
🔴
مدیریت تنگه هرمز دست ایرانه و تصمیمش رو هم به کشورهای منطقه اطلاع می‌دیم؛
🔴
برای این کار هم نیازی به تأیید یا اجازه کسی نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/128488" target="_blank">📅 17:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128487">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZSG5EjF9e4MIeZ7BMHh4zABJEa0zTCOKk_5TgCAGBJ3-oExE1YUe68b8oHRafS9O4PL0zTNEKJk73n7p2ClnMR71qu8meOvgjIMoiLwbzFfe6o0rpN9I5-jstQv8LYOZCRxWUUf4IHtNb-c1YCLTTi6FVWL49BxZ6pCas1ILW0o19GqRPQ9wNTlYZvKYAf8Qt6f1GExol70GZ6s1_xB3fWyJcAPtLf7dv5h_9adREdRTDhDunBUQieLRkhSUiLUFJ-vZuJ3NxjCgaQLfRCqSkAQ9Fq3i9h081r7qDBHIYbe4kPzffCIP16UeXp2G5X3QP3qupMagc41COjawOVjnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسانه های چینی تصاویری جدید از جنگنده پنهان کار J-35 را منتشر کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/128487" target="_blank">📅 17:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128486">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9727a3ae46.mp4?token=aQewZzN64hjCCIOqLc-avcG6nzd2uMV88VKUwgT1sMcZ2_zU1fmWe7hxG5giWmjQ59IEsLDhbv1pcDCIfIIWecKhLXbunm1DvUAq0Ia_4Ejv0iHHVCt-ZSLTlDozeatvS_iMi_jeCbW_4hI3h6kYTYCJz4xhHweJfPyZggAJdUxrd-VEO0zaCoMs0miUUl9L-hsrJwvSihrzOYd5N-BKrVNeDvR7VNRLhl34i9O5fItrQLFabZCqEe4qMq04PakDvxw1MTwgS-GqHHdtnAqmGyZjMJn_leOXLuEP7Y055Yi-f6G0eHhzyZGRTQhlcsbyDPwlyQ6EYaTZxaIiX-SKcnXqf6mTA3GIlo15IDmr8mfyqrC8_YYilco2-b2bKgOlENwPBDUg3bq1TtoZIIXU9Vy3nZ8P3D542v0tx27Q5LXo9ToqnTul3hoZLbwcBfHOOvaSaXUgyW7dZZmwBcY2Bv1SCRFM4lKlO2nBGozOOwRT_isHSvpvBOsMwIDpuQWfGk-ga3oNrJuA4rt5F7Pwp4ssH2RwnRODFJFTDsHJhL6WXxzrt6hD7jT5q0gHxJ0dgK3GNOsG0LYYCxEZntm1Ncmi6xDtScH8XEaxcUELH3XPKHT6JYyLS8D3f9m1BolzUgTDS29u5n7Da9Leb9Ub5GYGyyhtCUBwNKZPurMGN3Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9727a3ae46.mp4?token=aQewZzN64hjCCIOqLc-avcG6nzd2uMV88VKUwgT1sMcZ2_zU1fmWe7hxG5giWmjQ59IEsLDhbv1pcDCIfIIWecKhLXbunm1DvUAq0Ia_4Ejv0iHHVCt-ZSLTlDozeatvS_iMi_jeCbW_4hI3h6kYTYCJz4xhHweJfPyZggAJdUxrd-VEO0zaCoMs0miUUl9L-hsrJwvSihrzOYd5N-BKrVNeDvR7VNRLhl34i9O5fItrQLFabZCqEe4qMq04PakDvxw1MTwgS-GqHHdtnAqmGyZjMJn_leOXLuEP7Y055Yi-f6G0eHhzyZGRTQhlcsbyDPwlyQ6EYaTZxaIiX-SKcnXqf6mTA3GIlo15IDmr8mfyqrC8_YYilco2-b2bKgOlENwPBDUg3bq1TtoZIIXU9Vy3nZ8P3D542v0tx27Q5LXo9ToqnTul3hoZLbwcBfHOOvaSaXUgyW7dZZmwBcY2Bv1SCRFM4lKlO2nBGozOOwRT_isHSvpvBOsMwIDpuQWfGk-ga3oNrJuA4rt5F7Pwp4ssH2RwnRODFJFTDsHJhL6WXxzrt6hD7jT5q0gHxJ0dgK3GNOsG0LYYCxEZntm1Ncmi6xDtScH8XEaxcUELH3XPKHT6JYyLS8D3f9m1BolzUgTDS29u5n7Da9Leb9Ub5GYGyyhtCUBwNKZPurMGN3Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خوشحالی ایرانیان کانادا(با پرچم شیر و خورشید) بعد گل اول ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/128486" target="_blank">📅 17:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128485">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83e6d8a076.mp4?token=mzJRqJEBja2ihIg_mJVuwS607JIkNUUP3HPAUMhLjXT_jFD_MXDL0ue6gYIR8nSDzGXnbKFA8TU5rJbM8nd7bhWHoCe24pS11TgL4ONHD9S13eM57_CxgLREFwhbp1iXR59ejG_R5_9gzw7uoTYKb9ZU5gP5nKTNE6ItGDfkGpO2DLVZmtLBRjWfbg6khph2TH20jNsBeDM62YZZQ4Ntn-H64ZPCaOa5V8FHTtAXxg4qOgUTndjCJelWFkTTKUZaMaovmQAIu5Mq3_cEaCTbCqkdT-1t2Fjk7JRkZnKwHpEKAN521jDtDbG9shIsGswl4jcI5H_7lvpRQ_-2pitdJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83e6d8a076.mp4?token=mzJRqJEBja2ihIg_mJVuwS607JIkNUUP3HPAUMhLjXT_jFD_MXDL0ue6gYIR8nSDzGXnbKFA8TU5rJbM8nd7bhWHoCe24pS11TgL4ONHD9S13eM57_CxgLREFwhbp1iXR59ejG_R5_9gzw7uoTYKb9ZU5gP5nKTNE6ItGDfkGpO2DLVZmtLBRjWfbg6khph2TH20jNsBeDM62YZZQ4Ntn-H64ZPCaOa5V8FHTtAXxg4qOgUTndjCJelWFkTTKUZaMaovmQAIu5Mq3_cEaCTbCqkdT-1t2Fjk7JRkZnKwHpEKAN521jDtDbG9shIsGswl4jcI5H_7lvpRQ_-2pitdJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
‏در اوایل سال ۲۰۲۴ بازیکنان تیم ملی‌ کنگو در یک اکت اعتراضی و زیبا موقع سرود ملی کشورشون برای حمایت از مردم و جلب توجه افکار جامعه جهانی به کشتار هموطنانشون این حرکت رو انجام دادن.
🤔
با تیم ملی جمهوری اسلامی که خودشون رو ایرانی و وطن پرست میدونن مقایسه کنین. یه مشت شیاد خون شور
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/128485" target="_blank">📅 17:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128484">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a279890145.mp4?token=JhuSJAIxAVn7U9D-B7sTnSw4mZd3tgr6dVSsyz8bKwxoXm5C6Trgi9ATArpRxD_2Svzp-77GFuV_kFyxPVCU3c73Ee5NUww_FXAQIli1o7wzyKLgLduqeMngljY9RUnFpFoLLT51q5aseBzLWwASQn7sXYjCdPhiOJOGxw3iHMDCl3THw88xIvc3H06yIvUH7njEmuo4kbTh5cc1oS_NBpDBT1oezOmY_gxQrdw-r8G_dXblKDO1iUSQDDLqpYfpxl-7fpdeP52KgCh59g0K2PkhJr0-WnBPABkRTsI9Yv6Uu9NdZayLxBFmYJBwOBZS4UEjloFr4jYRSLxLQ6ouvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a279890145.mp4?token=JhuSJAIxAVn7U9D-B7sTnSw4mZd3tgr6dVSsyz8bKwxoXm5C6Trgi9ATArpRxD_2Svzp-77GFuV_kFyxPVCU3c73Ee5NUww_FXAQIli1o7wzyKLgLduqeMngljY9RUnFpFoLLT51q5aseBzLWwASQn7sXYjCdPhiOJOGxw3iHMDCl3THw88xIvc3H06yIvUH7njEmuo4kbTh5cc1oS_NBpDBT1oezOmY_gxQrdw-r8G_dXblKDO1iUSQDDLqpYfpxl-7fpdeP52KgCh59g0K2PkhJr0-WnBPABkRTsI9Yv6Uu9NdZayLxBFmYJBwOBZS4UEjloFr4jYRSLxLQ6ouvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: کلمه به کلمه متن توافق را برایتان می‌خوانم
🔴
من نه تنها آن را منتشر خواهم کرد. احتمالاً یک کنفرانس مطبوعاتی خواهم داشت و کلمه به کلمه آن را برای شما خواهم خواند تا مطبوعات آن را به طور دقیق پوشش دهند زیرا این یک سند بسیار مهم است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/128484" target="_blank">📅 17:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128483">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XkJDCNhr-Wjlg7OL5OJgM3twaHPIu_IZvDW0UkovASM-hR9eN2UVeXi-iNcn947YhJserelncIb78EJK43WCuiwCVZQ-gZwlQRR5HWCo2toXngYPGZAZs5fqB5ZijIezq5URLRR0ODYaz-8t-3r3xclOQDFXX4uFLWOL5JfvyNVeb3C4BoD5ewmwnzNn4QQ97UlArwCNnhkvgwjl7BM1hqJfCKUlljqw9DR-27uImyZW6IKEsnHLTyLHXr1YTFsndxWcvtUweQDtLkTOTjDKK4G_xLu_uKAmCKX8TlxZw-PIf29GNs9MKEDY6FOFFyBgt0vGjYDWZid8GdREDU-HNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش ایالات متحده قصد دارد یک انبار دائمی و آماده جنگ برای سلاح‌های نیروی دریایی در سواحل جنوب شرقی استرالیا، فراتر از برد بیشتر موشک‌های چینی، ایجاد کند، طبق اسناد مناقصه و اظهارات مقامات به خبرگزاری AFP.
🔴
حدود ۳۰ میلیون دلار در ساخت تأسیسات ذخیره‌سازی در مناطق روستایی ویکتوریا سرمایه‌گذاری خواهد شد تا سلاح‌های نظامی آمریکا در آنجا نگهداری شود، با هدف بهبود واکنش نیروهای آمریکایی در سراسر منطقه هند-آرام.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/128483" target="_blank">📅 16:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128482">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
یک منبع ارشد حزب‌الله به تلویزیون العربی گفت که ایران به این گروه اطمینان داده است که یادداشت تفاهم را امضا نخواهد کرد مگر اینکه شامل خروج اسرائیل از لبنان باشد
🔴
این منبع گفت تهران خروج را شرط لازم برای نهایی کردن توافق می‌داند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128482" target="_blank">📅 16:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128481">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7a9z-MXWiDUtS_uWALrl8o_p23BhNPQCUQZXSB-t6THWocmLu-EXP3MmGWejAVGg3cL3oSMPD0560vvGPIBDNwImA_VnqB2zGMvX0sFa7hNuPR0BKtzEr75F73bqOO52StAXL62mruQ2tY_IKraZzh24fHwL5yW0Orz4x8daSwD9uZtGkxyNoaLrhd3ql6Xby8xVN33WyKZokhGd4yAxnw3Z8hclPn70zkzfiQkEDEGUu9moVmK3Dijpf0xQQOHLsOlJ-1JGf6P2hj9WEEu2VD3IfjtzDVzesgA0CchPP3OBKKLnApPx3fIJ_0SZC1i1ZYezcQl2ddflvQs43_h5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شب گذشته ایلان ماسک ۱۶۵ میلیارد دلار سود کرد و ثروتش به ۱.۳ تریلیون دلار رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/128481" target="_blank">📅 16:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128480">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
اسرائیل درخواست دیدن یادداشت تفاهم بین آمریکا و ایران را داشت اما طبق گزارش کانال ۱۲ اسرائیل، این درخواست رد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/128480" target="_blank">📅 16:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128479">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ترامپ در مورد توافق هسته‌ای با ایران:
این توافق در مورد یک چیز است: ایران هرگز سلاح اتمی نخواهد داشت. هرگز.
🔴
بقیه آن، صادقانه بگویم، بی‌اهمیت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/128479" target="_blank">📅 16:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128477">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ترامپ: توافق با ایران را برای بررسی به کنگره خواهم فرستاد
🔴
ممکن است به زودی تحریم‌ها بر نفت روسیه را دوباره اعمال کنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/128477" target="_blank">📅 16:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128476">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70d2b0a36c.mp4?token=VJDlsFZscNNw4-T2vL03T6W2zUsH_GUn3tOAVYcr1vyrzOFtUBT71hNs1U7RiIw71GbE1FXhZr4KWTXdwnmezY5NnWWgJTMQzZ9Baoox92uWL9KFeQf0HytYDS78pr-FwD0gfvpzRQS2FS6Q30XzVSMDtFmBrvUxWkb45RRVmT3JJABNnTX-doVXsf-jhCcDwcgYzzk-c0oIIAFs3Hzs3m3ZMKmt5ixRYkA-ktrjznueqQhSf4WuY6xRZ8mWR-CA3WrB6ZnhbzOgt-2G8pWC8Le7yyOxfyfK42vlIqZtiXeH_sVQNQQtLUNFuaM55t4mVmA7WyuhaAhblui710jnfGr1SXbbdJiuM8OEiUuTbDW02lIxF46mXL8zy1s3EszKHuOTtHAZmpvPa0fxq4-Q115fAOJenUraxmTg0szx_gfgV2SmYCFJcKfddCGKviMBHVn-xlA2xNmofgF1ZxpQEYtqlaaBa1jSfsOy-oFkYuIja9FxK6ogvb8LJ-UhTGbpQiGTSn9nSMMFGcLZ5rNMtBW2-gXAy5-4pCJToUPL7K4qQC97XDO_RQXTb8hh6SeLd9fOWtMKV1fGcOmsuw5eQk-sl1h_nCX49lXJlOX_4Vyu55Dl-3h6bmYATlR9dq6ph09tE5zL5yrDP8wd-UEzVHpe_PfRxar8dTxTzppwRrc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70d2b0a36c.mp4?token=VJDlsFZscNNw4-T2vL03T6W2zUsH_GUn3tOAVYcr1vyrzOFtUBT71hNs1U7RiIw71GbE1FXhZr4KWTXdwnmezY5NnWWgJTMQzZ9Baoox92uWL9KFeQf0HytYDS78pr-FwD0gfvpzRQS2FS6Q30XzVSMDtFmBrvUxWkb45RRVmT3JJABNnTX-doVXsf-jhCcDwcgYzzk-c0oIIAFs3Hzs3m3ZMKmt5ixRYkA-ktrjznueqQhSf4WuY6xRZ8mWR-CA3WrB6ZnhbzOgt-2G8pWC8Le7yyOxfyfK42vlIqZtiXeH_sVQNQQtLUNFuaM55t4mVmA7WyuhaAhblui710jnfGr1SXbbdJiuM8OEiUuTbDW02lIxF46mXL8zy1s3EszKHuOTtHAZmpvPa0fxq4-Q115fAOJenUraxmTg0szx_gfgV2SmYCFJcKfddCGKviMBHVn-xlA2xNmofgF1ZxpQEYtqlaaBa1jSfsOy-oFkYuIja9FxK6ogvb8LJ-UhTGbpQiGTSn9nSMMFGcLZ5rNMtBW2-gXAy5-4pCJToUPL7K4qQC97XDO_RQXTb8hh6SeLd9fOWtMKV1fGcOmsuw5eQk-sl1h_nCX49lXJlOX_4Vyu55Dl-3h6bmYATlR9dq6ph09tE5zL5yrDP8wd-UEzVHpe_PfRxar8dTxTzppwRrc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره گرد و غبار هسته‌ای ایران:
ما عجله‌ای نداریم، اما آن را به دست خواهیم آورد و نابودش خواهیم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/128476" target="_blank">📅 16:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128475">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bf48e1e56.mp4?token=K4rdrTOeh6GJLdBLNg6HsCQLF26UN8HSlX9dojBq3gt1hv8qag9ouERLnAU7iIQe5TYni1zXDbGVSYeRS2x66FZBEtjgkbzqmCS1J9oJBb7_JK6btrkXn2i9nDsDzHLQ8XUuEYZuEQ9mFya7KpoG2fhln85-MDo24FrXqOqqjxVJsIZe8u8uwFpS9YLcszSvcw342M6uIiHh87sMesKnliUALMTdGndh_qJ3D6sXeHGpV9emhjwFxJGsTlwyCa4ZrZ3vYsJgWnXbHXqQGyzXJQUBy_Ob9HHbM3uZhgSb59tPLuVifTnEICT7EJKHM7RShTXRHvwM4ABE_T9QNJ-RQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bf48e1e56.mp4?token=K4rdrTOeh6GJLdBLNg6HsCQLF26UN8HSlX9dojBq3gt1hv8qag9ouERLnAU7iIQe5TYni1zXDbGVSYeRS2x66FZBEtjgkbzqmCS1J9oJBb7_JK6btrkXn2i9nDsDzHLQ8XUuEYZuEQ9mFya7KpoG2fhln85-MDo24FrXqOqqjxVJsIZe8u8uwFpS9YLcszSvcw342M6uIiHh87sMesKnliUALMTdGndh_qJ3D6sXeHGpV9emhjwFxJGsTlwyCa4ZrZ3vYsJgWnXbHXqQGyzXJQUBy_Ob9HHbM3uZhgSb59tPLuVifTnEICT7EJKHM7RShTXRHvwM4ABE_T9QNJ-RQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره یک خبرنگار اماراتی: چه آدم خوش‌قیافه‌ای. آیا او از کشور شماست؟
🔴
محمد بن زاید امارات: قطعاً.
🔴
ترامپ: او رفتاری بسیار دلنشین دارد. مردم من خیلی بدجنس هستند.
🔴
محمد بن زاید امارات با خبرنگار شوخی می‌کند: حواست باشد حالا.
🔴
ترامپ: می‌توانم همین الان او را در یک فیلم بازی دهم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/128475" target="_blank">📅 16:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128474">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18495babbd.mp4?token=DwLAeeEVc9s9D1NMskxd66GUG6AK4dBy-rvkmlbV29ueA4f2-9CzX6D3nTYBAYc7B8cS6fSm4nYvOt8LMfVP-kF-6xmIoGsPeVzBMmnO48NBlYtGGZEgB4BWkdd3oucbVXLiW-PkQPwRyPVCjG2jaszCW39BlvyQL0CsdgxmHDEt8aYFU9a-a9SSgeDJX-YCvKvgEwHi6DfQJ3VCE3Ib9v2_USMAcKsSNm4HPBCo-4-KaawcEdgLTs_DXWtvbstNhJVGIaH9FcbL1q4Fzr4kyLXNhlNd497V2RM3R9-JZ5jwEbZmePysjRlTO-mOwfpdAGE0vQrghX6ELEyQl93FiChACWJtEJAJqyNGBdMoc3S-zvoUuyDy2siG3kKekSsfh3yC26NjqSZFWMs-pTqcqbWjN5rD0lV5HcZPEVkiUlP5BnUkYGHYJUNa73eVKSYBmJ0xoOOlS6Xy8W3rP3bVdZjaVHWYhqlvH1iWQMdHvTNpFg7DcAC7WHDO8h8MX6E45D3Gjtyv_z1Ao8MTZu7lSW-8_iehFZtlZvtZM6-xrB2wA2bPRizzYrIxCF_439x7CMZd8Gx6Be3b96u537oaVMggDqUtTz-hISW9tOp4ho_fO5uevWiLOwLOROycITb9ftoL9p8urXyLKUzOuy8deELL7VxmdNYxCtE9N-qpbUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18495babbd.mp4?token=DwLAeeEVc9s9D1NMskxd66GUG6AK4dBy-rvkmlbV29ueA4f2-9CzX6D3nTYBAYc7B8cS6fSm4nYvOt8LMfVP-kF-6xmIoGsPeVzBMmnO48NBlYtGGZEgB4BWkdd3oucbVXLiW-PkQPwRyPVCjG2jaszCW39BlvyQL0CsdgxmHDEt8aYFU9a-a9SSgeDJX-YCvKvgEwHi6DfQJ3VCE3Ib9v2_USMAcKsSNm4HPBCo-4-KaawcEdgLTs_DXWtvbstNhJVGIaH9FcbL1q4Fzr4kyLXNhlNd497V2RM3R9-JZ5jwEbZmePysjRlTO-mOwfpdAGE0vQrghX6ELEyQl93FiChACWJtEJAJqyNGBdMoc3S-zvoUuyDy2siG3kKekSsfh3yC26NjqSZFWMs-pTqcqbWjN5rD0lV5HcZPEVkiUlP5BnUkYGHYJUNa73eVKSYBmJ0xoOOlS6Xy8W3rP3bVdZjaVHWYhqlvH1iWQMdHvTNpFg7DcAC7WHDO8h8MX6E45D3Gjtyv_z1Ao8MTZu7lSW-8_iehFZtlZvtZM6-xrB2wA2bPRizzYrIxCF_439x7CMZd8Gx6Be3b96u537oaVMggDqUtTz-hISW9tOp4ho_fO5uevWiLOwLOROycITb9ftoL9p8urXyLKUzOuy8deELL7VxmdNYxCtE9N-qpbUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: سناتور گراهام همچنین گفت که توافق نهایی با ایران باید برای بررسی به کنگره ارسال شود. آیا شما این کار را انجام می‌دهید؟
🔴
ترامپ: هرگز به آن فکر نکرده بودم، اما انجام می‌دهم. برایم مهم نیست. یعنی، می‌دانید، دموکرات‌ها — می‌دانید، ما به آن‌ها «دموکرات‌های احمق» می‌گوییم چون آدم‌های احمقی هستند.
🔴
خب، چیزی که دوست دارم انجام دهم این است که آن را به کنگره بفرستم و بگویم «نباید آن را تصویب کنید»، و من آن را تصویب خواهم کرد. هرچه من بگویم، آن‌ها می‌خواهند برعکسش را انجام دهند. به هر حال، برای او خیلی خوب پیش نمی‌رود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/128474" target="_blank">📅 16:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128473">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea5ead7bb.mp4?token=s2kMPQsq997gkf5BxXCzEDRLYewAE6vkQzhatQuFVi9zVd4xD9gWaY4gWDD_CRpoI7BKye_nXCzhfNR9KERfACs2EcMk5R059S8AnkTnWUa0O4oOMuGFFQRlBu2n2goME7c76IKxYErkb4GU32HzPSDh5JKdtG03RUxabY7xGAZWBib9GhZvWMLEJZRDvphivoiS4xBxOL3rWfcvvPGczQzoL8Yw2MQA613KSxVfBJOf9skpmHUBhTKu7bu1QLud2O1g4Qf13jCy2z8KZGNRrSI31cfLr5uEtxUpHcq2qxJAXgYTJ7xqUGriCjm6BtmTIqhoq_Iv_8phWFcCjM19sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea5ead7bb.mp4?token=s2kMPQsq997gkf5BxXCzEDRLYewAE6vkQzhatQuFVi9zVd4xD9gWaY4gWDD_CRpoI7BKye_nXCzhfNR9KERfACs2EcMk5R059S8AnkTnWUa0O4oOMuGFFQRlBu2n2goME7c76IKxYErkb4GU32HzPSDh5JKdtG03RUxabY7xGAZWBib9GhZvWMLEJZRDvphivoiS4xBxOL3rWfcvvPGczQzoL8Yw2MQA613KSxVfBJOf9skpmHUBhTKu7bu1QLud2O1g4Qf13jCy2z8KZGNRrSI31cfLr5uEtxUpHcq2qxJAXgYTJ7xqUGriCjm6BtmTIqhoq_Iv_8phWFcCjM19sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: تنگه هرمز باز خواهد بود و همیشه بدون عوارض خواهد ماند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128473" target="_blank">📅 16:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128472">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a17e9d5f.mp4?token=DvRioxnV0E7cEVDT1nN_eCuTqYEhMuyZfnoGYj4z6_NcBznoeCHLdskfF0B5J2yr8s_wxo5Siq4VQm0VwH274VQsN3d1hhy3ZbTgfu_2cOIeCsR-9AVU4T-diJtx7lsGBqKN_83P1qFXmQepwOcEmdTPe57g2z14u-RVlrzSYfXzEfLbaMtNgY7ljima7KZAwi4eG8KhhyIF3FJaKTe-3pqE2skWPraatJPBHAc-A5ZegSQplFYE_q0wmTX8Gm7QL7EPKdNgv2AZU69emgk1Rtu8a00xL62kgsBiP0nYR8Q3-SxnlEkuCsJItByywcbtN6px1_4ylHjDpI5Plq5QhoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a17e9d5f.mp4?token=DvRioxnV0E7cEVDT1nN_eCuTqYEhMuyZfnoGYj4z6_NcBznoeCHLdskfF0B5J2yr8s_wxo5Siq4VQm0VwH274VQsN3d1hhy3ZbTgfu_2cOIeCsR-9AVU4T-diJtx7lsGBqKN_83P1qFXmQepwOcEmdTPe57g2z14u-RVlrzSYfXzEfLbaMtNgY7ljima7KZAwi4eG8KhhyIF3FJaKTe-3pqE2skWPraatJPBHAc-A5ZegSQplFYE_q0wmTX8Gm7QL7EPKdNgv2AZU69emgk1Rtu8a00xL62kgsBiP0nYR8Q3-SxnlEkuCsJItByywcbtN6px1_4ylHjDpI5Plq5QhoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره توافق ایران: لیندسی گراهام شکاک است؟ باید با او صحبت کنم. او در دردسر بزرگی خواهد بود.
🔴
لیندسی خوب است. او مشکلی ندارد. او شکاک نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128472" target="_blank">📅 16:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128471">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d9dd03f8e.mp4?token=Dpobbjmi1x-zvWhvnqMJQpAEyNkraXQEVZuGoFPhRX4_aYSQORbQWj-pgRlNr6m6xuMOe9F919exSk0sS8htIpwVEHrdWlz4XlQsV1RbTKn2wU6mqBKrwrP0OUwg_wh8FbWd_LHPXh5RYi38llgm_kI8D2PxQlDSwCSPS5tZkKQTsGZxaHHtOQ6Bg3PL4HX_bGuolx7d5131-_lTqv0uYZm9Z1Bl4-u6cvnp4vpjf3iQVmMr8WWRyrfBkuOVMFq4C7x-XpI8IIX1X7UhCMBulvGYqCHVoQm4hhcXvLVcZjzSieb32rRDW6jXabMYoeuCQnk8H7EOsxJ0Qy_juqwKCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d9dd03f8e.mp4?token=Dpobbjmi1x-zvWhvnqMJQpAEyNkraXQEVZuGoFPhRX4_aYSQORbQWj-pgRlNr6m6xuMOe9F919exSk0sS8htIpwVEHrdWlz4XlQsV1RbTKn2wU6mqBKrwrP0OUwg_wh8FbWd_LHPXh5RYi38llgm_kI8D2PxQlDSwCSPS5tZkKQTsGZxaHHtOQ6Bg3PL4HX_bGuolx7d5131-_lTqv0uYZm9Z1Bl4-u6cvnp4vpjf3iQVmMr8WWRyrfBkuOVMFq4C7x-XpI8IIX1X7UhCMBulvGYqCHVoQm4hhcXvLVcZjzSieb32rRDW6jXabMYoeuCQnk8H7EOsxJ0Qy_juqwKCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: روابط اکنون عادی شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/128471" target="_blank">📅 16:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128470">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65e1926caa.mp4?token=dk8f2hG3eho1gem8cI-Qy6jsBrA3Pcd0tCLRfVyISHsxo4dqE0tJpjCTIAgmLp8gyi6OFELmWlH8UpVDf2lEM9SrdlF1_GwFblG2j-NY_MB9-hjwcvYJTOvKvSk_-kkuFFqWnd9iDWMs1AIc4u5PSayw7qa8jmTxn1cEZr6NZRaMBGUKZcz7kZjJi1fNS6lgbAFD2mDLmCxP2h7TL7dL4Dv_8JhNIGR3ZVblWRciL1TZtZOiMzchMdfIkb2aaEvyyjoz5SKtN3xKGx5VDPTKmwAvI1Iq9px_pnVLK4N12BKQ0YkAQLnpJfQVrSLRi3hz0b0YPy7ix95p6-W0nM1oBI2_6C5cg5sm-evgsy6Gunfd-x5qI-ShnmQdPF8THEhPtkUNjPFVxS3oljjq1Y8F1ZozQlnNr-zdOCLnYt3RViADbuRomUytF-Jus2mBq3TBvLXZ9Pw93HT-FQtmjqAzQa7C_FLgJeyjLf2d0krug5wS2iEDdypXmdaT_gCGP0gIHLE8WKXF8hVK4tPDIdQAXYZnAFFoOak1H-JDrBrVqBDSba0n5afAC2GXVEkldwCxMgwvoP0l8B2dxlc6rd6OtqJ7wl5OGizb_YXqOvA0ocATzXOpoMUKKOILN0JhhA4Nfj_lTbupaN7aJDNnfFcPSqV6OXXZuX10cwQGrQxWNFI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65e1926caa.mp4?token=dk8f2hG3eho1gem8cI-Qy6jsBrA3Pcd0tCLRfVyISHsxo4dqE0tJpjCTIAgmLp8gyi6OFELmWlH8UpVDf2lEM9SrdlF1_GwFblG2j-NY_MB9-hjwcvYJTOvKvSk_-kkuFFqWnd9iDWMs1AIc4u5PSayw7qa8jmTxn1cEZr6NZRaMBGUKZcz7kZjJi1fNS6lgbAFD2mDLmCxP2h7TL7dL4Dv_8JhNIGR3ZVblWRciL1TZtZOiMzchMdfIkb2aaEvyyjoz5SKtN3xKGx5VDPTKmwAvI1Iq9px_pnVLK4N12BKQ0YkAQLnpJfQVrSLRi3hz0b0YPy7ix95p6-W0nM1oBI2_6C5cg5sm-evgsy6Gunfd-x5qI-ShnmQdPF8THEhPtkUNjPFVxS3oljjq1Y8F1ZozQlnNr-zdOCLnYt3RViADbuRomUytF-Jus2mBq3TBvLXZ9Pw93HT-FQtmjqAzQa7C_FLgJeyjLf2d0krug5wS2iEDdypXmdaT_gCGP0gIHLE8WKXF8hVK4tPDIdQAXYZnAFFoOak1H-JDrBrVqBDSba0n5afAC2GXVEkldwCxMgwvoP0l8B2dxlc6rd6OtqJ7wl5OGizb_YXqOvA0ocATzXOpoMUKKOILN0JhhA4Nfj_lTbupaN7aJDNnfFcPSqV6OXXZuX10cwQGrQxWNFI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور امارات، محمد بن زاید، به ترامپ:باعث افتخار من است، آقای رئیس‌جمهور، که اینجا با شما هستم. و می‌خواهم بگویم که ما بسیار سپاسگزاریم که شما اینجا هستید و به عنوان رئیس‌جمهور ایالات متحده.
🔴
تشکر ویژه‌ای برای حمایت شما در طول جنگ شش هفته‌ای. این برای ما بسیار مهم است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128470" target="_blank">📅 16:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128469">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88bd31af11.mp4?token=UdUKZd5_CeZJ5Y1dPskmpTOF8Jvgin3M5cKhQiEGiCgnghI2Gg0vcGxf_yt2Zp-v7TNHLQBsGMkylXlIOXIHsTWppqtg4apkxxPubVgVgsFc2Rl6zaYG-8HmjCB5w3TJhmMtKOBUiIHvcSmC5YOMbEGk8xFZ-Lio6oc74Z6n8ZgPnvioIFWhwvUUjDkPdpGBvybohBc2swm4hnAtl8V42pziJATTCOmdMvYzWi0I2Fsl5x_g9AFgDqtbFJxtJjP9LrVgkwauFfcKH-SLXDboFF1DS2Cz1Oc2Xi-UAH2xMRI05bB3mSK9ogAND5fxA5RpjTwr_LJX7un1Af8G7EZH6ZJgWLiPKqoCGyGcPC3c6i0GKCrUee51jwhByw7r7mCDi4UaRkZzEDK5J2N-4PP2s2VEFl0lK7nYuaXd3vAW_YVYhsotmhUaMnXCD5mDJkNvCzIKWuwaTqnlwt19r4r97tnpQoLEolHT-ntmovtIy-mHKrDlTsQqEX7r7u5cSfttjbLeEYEYamWsXALZe_2pHIWThgUiMd4xPjJB3tacm4QQa1Jx5e_TBeAVLONo0apDpcGhDWyoZAr6_6R4Ufv0pLNH4W3_nVXOJOTn9eQ0fdkcVH8mEqGZOk6nzER2KH-98svk4-RQazqP7xS2ETv3EO0nPNiMWPaozaOd5s4Mw7I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88bd31af11.mp4?token=UdUKZd5_CeZJ5Y1dPskmpTOF8Jvgin3M5cKhQiEGiCgnghI2Gg0vcGxf_yt2Zp-v7TNHLQBsGMkylXlIOXIHsTWppqtg4apkxxPubVgVgsFc2Rl6zaYG-8HmjCB5w3TJhmMtKOBUiIHvcSmC5YOMbEGk8xFZ-Lio6oc74Z6n8ZgPnvioIFWhwvUUjDkPdpGBvybohBc2swm4hnAtl8V42pziJATTCOmdMvYzWi0I2Fsl5x_g9AFgDqtbFJxtJjP9LrVgkwauFfcKH-SLXDboFF1DS2Cz1Oc2Xi-UAH2xMRI05bB3mSK9ogAND5fxA5RpjTwr_LJX7un1Af8G7EZH6ZJgWLiPKqoCGyGcPC3c6i0GKCrUee51jwhByw7r7mCDi4UaRkZzEDK5J2N-4PP2s2VEFl0lK7nYuaXd3vAW_YVYhsotmhUaMnXCD5mDJkNvCzIKWuwaTqnlwt19r4r97tnpQoLEolHT-ntmovtIy-mHKrDlTsQqEX7r7u5cSfttjbLeEYEYamWsXALZe_2pHIWThgUiMd4xPjJB3tacm4QQa1Jx5e_TBeAVLONo0apDpcGhDWyoZAr6_6R4Ufv0pLNH4W3_nVXOJOTn9eQ0fdkcVH8mEqGZOk6nzER2KH-98svk4-RQazqP7xS2ETv3EO0nPNiMWPaozaOd5s4Mw7I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره رئیس‌جمهور امارات MbZ:
حضرت ایشان یک جنگجو است. او در آنجا می‌جنگید و آنچه باید انجام شود را انجام می‌دهد. و به خاطر همین شناخته شده است. او مردی شجاع است
🔴
او کشوری عالی دارد. کشوری فوق‌العاده است. و آنها مدت‌هاست که با ایالات متحده همراه بوده‌اند. اما من می‌گویم از زمانی که من به کار آمدم، خیلی بیشتر بوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/128469" target="_blank">📅 16:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128468">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
اسرائیل هیوم: دونالد ترامپ داره گزینه برکناری مقاماتی که با توافق ایران مخالفن رو بررسی میکنه!
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/128468" target="_blank">📅 16:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128467">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
سخنگوی ارتش: در جنگ، جلسه‌ای با حضور مسئولان عالی رتبه نظام در حال برگزاری بود که مشخص شد یک پهپاد دشمن بر فراز آن منطقه در حال پرواز است
🔴
از آن‌جا که پهپاد از نوع کم سرعت بود و جنگنده‌ها با سرعت بسیار بالاتری حرکت می‌کنند، پهپاد مورد اصابت قرار نمی‌گرفت
🔴
خلبانان ما با استفاده از برخورد فیزیکی، جنگنده را به پهپاد نزدیک کرده و با اصابت بال هواپیما به دم پهپاد، آن را منهدم کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/128467" target="_blank">📅 15:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128466">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
فون در لاین، عضو اتحادیه اروپا: من به ترامپ به خاطر توافق با ایران تبریک گفتم.
🔴
هر دو موافقیم که این توافق باید به معنای پایان قطعی برنامه هسته‌ای ایران باشد.
🔴
تنگه هرمز بازگشایی خواهد شد.
🔴
قیمت نفت در حال کاهش است.
و اینگونه است که دیپلماسی نتیجه می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/128466" target="_blank">📅 15:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128465">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
اکیپ: دونالد ترامپ دستور مستقیم ابطال ویزای برخی از اعضای ایران از جمله مهدی ترابی و مهدی طارمی رو صادر کرده و ویزای این بازیکنا ابطال شده!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/128465" target="_blank">📅 15:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128464">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b287c6a06a.mp4?token=c_mUQpd0UhSLDU7Mjy6r95BWaK7WRdXSqg_9hVBUwAMyYjuQYhE5PxCvt-OeOvOX8w87AgBgs96aJ1pjR4P8bmI7l10Czy6LQ0XEqu9wqVNVXrkS-H5L3Vs7mpRnBCPXxN3Sjf6-uCIBtVXXbOFOMwIozD0MK9h9L_T56aMbe2xxkT7RK-XXeyF3UIS5CZLXczDyuExyMSoskI8DhNcXGXmIkTQO_gzt2e4OhQoBOPEefd3LGdyVgUVBZ-LEJPsIJ3mTn2_1-jIVXz37R7nNNf280niTJgEqc2W3W9jcDco-QFr82zfjsPxGO-o-Kcir9fbA_RxIqwzE6u7bOOo_WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b287c6a06a.mp4?token=c_mUQpd0UhSLDU7Mjy6r95BWaK7WRdXSqg_9hVBUwAMyYjuQYhE5PxCvt-OeOvOX8w87AgBgs96aJ1pjR4P8bmI7l10Czy6LQ0XEqu9wqVNVXrkS-H5L3Vs7mpRnBCPXxN3Sjf6-uCIBtVXXbOFOMwIozD0MK9h9L_T56aMbe2xxkT7RK-XXeyF3UIS5CZLXczDyuExyMSoskI8DhNcXGXmIkTQO_gzt2e4OhQoBOPEefd3LGdyVgUVBZ-LEJPsIJ3mTn2_1-jIVXz37R7nNNf280niTJgEqc2W3W9jcDco-QFr82zfjsPxGO-o-Kcir9fbA_RxIqwzE6u7bOOo_WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادی ترین حرفایی که عرزشیا به قالیباف میگن
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/128464" target="_blank">📅 15:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128463">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
ترامپ: مرحله بعدی مذاکرات ایران «آسان‌تر» از دور اول خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/128463" target="_blank">📅 15:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128462">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXFCyXmNilwZm1GB_gUMzf9beuWcx6hr2_pkr8M_pK2gs5VZYexedpumHbQqQ_j00khsvYzQtmGue-1TpUN7UU0MYD08qJpPpOTyErYq5J84etIQU9xokyev5gtl0kUYx84PoJDut_Jk3MfXo89zddoep1144-4z3P1GCq5VOi8xDwVLI9j00EePrP7EMOmJHcwLzchsmd89ZwcNLEiuM6AxUO15i3rLkFCNw3Yof-RX6WlPCVtl-Q_c5bbfDaqKYJhpcfRb75VNS9Tvd9h3OCoZ0sodas9rGdDFHNPuFHWQ0eoatG8DslOKEAIr32fbiMp_sRIq7G7TuMf5EMHp-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضعف فاحش شجاع خلیل زاده در بازی امروز صبح مقابل نیوزلند
🫶
بازیکنی که صرفا با خایه مالی به تیم ملی راه پیدا کرد نه مسائل فنی  @AloSport</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/128462" target="_blank">📅 15:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128461">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
نخست‌وزیر بریتانیا: ما از توافقی که ترامپ با ایران منعقد کرد استقبال می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/128461" target="_blank">📅 15:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128460">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
قطر: تفاهم کنونی تهران و واشنگتن نخستین گام به‌سوی توافقی گسترده‌تر است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/128460" target="_blank">📅 15:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128459">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/293f42cae1.mp4?token=Kur9FGt3kNuUmp11WkHEb3ZLrgvtcvxVZlFCi6PPsc5PCspWk9p_PxNxSfc6V1caKFRjwWuqawP0fevL3Uy2rcs5j9ZtcMbv_Dmh8yta9K2nC3PJBR2qNH0gQQlwHCR5DPXi3xgrlMk-B2zbvxFLmmduj8pvOz9k73VPvgg52Nij2LJOz1k50_5bPLjokg3z1UMuZW594xBiTimXug63bmEEptv_GU88tJkE5Y-F0eBAZAaby9viAdEMVvRH94CF7uxZhep_pms3_RJSWqN68LxnLC_eYoegGF1RXQ9PCKxxmwGwDDkZw1jZQ0CURVAq9eohLdtlmxyuYZCcHlIhjZOT2z-qdiWpRcyC-_OrhyX6hFwJ6JGQjEyzBn-S6GFJQ5-u493phkG6zBVtKC62zln2uTRn_XUnMNHpOob7C6U76Ap5U--x-lLZnq8cDJw-pQT6hBZAWqu7IorRMqyxHLGRRtjfopZDBVSdcDYitFj7-ZAa-FUUsKZXoorWV4E5q74U8nS3zFbrZdCeZqbU3R-zmz0zzsSEmGIXmGvomUgSFyWgKK2sWhjxYay_crk3-OY4kOMwobUIlJMGBSxMogaFpDQc0oQUDseACus7VCvTqPP6dkmhxl_0ySQAjjuRzx9zrd3UZOi2MUxn4fKoMhB7LYskNobq-qQ7QwiAeBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/293f42cae1.mp4?token=Kur9FGt3kNuUmp11WkHEb3ZLrgvtcvxVZlFCi6PPsc5PCspWk9p_PxNxSfc6V1caKFRjwWuqawP0fevL3Uy2rcs5j9ZtcMbv_Dmh8yta9K2nC3PJBR2qNH0gQQlwHCR5DPXi3xgrlMk-B2zbvxFLmmduj8pvOz9k73VPvgg52Nij2LJOz1k50_5bPLjokg3z1UMuZW594xBiTimXug63bmEEptv_GU88tJkE5Y-F0eBAZAaby9viAdEMVvRH94CF7uxZhep_pms3_RJSWqN68LxnLC_eYoegGF1RXQ9PCKxxmwGwDDkZw1jZQ0CURVAq9eohLdtlmxyuYZCcHlIhjZOT2z-qdiWpRcyC-_OrhyX6hFwJ6JGQjEyzBn-S6GFJQ5-u493phkG6zBVtKC62zln2uTRn_XUnMNHpOob7C6U76Ap5U--x-lLZnq8cDJw-pQT6hBZAWqu7IorRMqyxHLGRRtjfopZDBVSdcDYitFj7-ZAa-FUUsKZXoorWV4E5q74U8nS3zFbrZdCeZqbU3R-zmz0zzsSEmGIXmGvomUgSFyWgKK2sWhjxYay_crk3-OY4kOMwobUIlJMGBSxMogaFpDQc0oQUDseACus7VCvTqPP6dkmhxl_0ySQAjjuRzx9zrd3UZOi2MUxn4fKoMhB7LYskNobq-qQ7QwiAeBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضعف فاحش شجاع خلیل زاده در بازی امروز صبح مقابل نیوزلند
🫶
بازیکنی که صرفا با خایه مالی به تیم ملی راه پیدا کرد نه مسائل فنی
@AloSport</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128459" target="_blank">📅 15:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128455">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OI5vd6DKpGIlqT96Itlqax2AIf-j5_JDMrEY0pxWBQ3tMaDkblel1Er-3-t__LuzFZMOg2A9QhUREPH5-mAJiXgOygRlBvaKZ6hv4fIzwbmVRZd-oCdxMNU3qcWq67-27RIWo1AdTuNcSmhqtRI-j3l1axOYm8Cq01R10dHFvzK1MtNCyUnVM7fPYaBrPYFmIGGNNabi9ml-Be-9MBzPbfQiULMmAViMrOcQewI0tIWXDqoBtMv1S5-ngTdFkk0Vqadfs18wfdmFBdi-L6Okw6NHb4-snrV8KO46xfwej_WxAEpD2rPysne5oQAJzPSOjGcYN8X7vCTBOTrj97Xllw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o3lgEkYycetYvStyY1LcLOuCL1Nu-V1Vn4L2m4ZT8mjGUaNJB3Etzb5ghm__zTwcZl8b97QQMGIkH4hGE98LU-v2wY_sochzXUYade2BAdyA0CTBlLDy7X1EY41FpzpnExZzMHZb6c3DfSuogjGBMu70JZXVU1OSDT1n9QMA5pawiXpF1kBaVH8jMI_LW3F6KoGhx27t3osnFPOkRXJUAC9djQT4laI4MkvHTZcFRbRiptxeikT7srS0aD8SPR_2Co9kLrFZE7-FjEI5pbib0A1PegZ-bpW-bkCVVQ2zsawvTirGz3x8C23RROuNX2lpBcMUAbxh_BSv6rX5W5yJQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UVmpuXj_zbQgtxrUhYX6Dfqrsq8RSZ6eq7cBFLdGJxn62AStlKsKaSdMllsmG1I1M-fcEgthVII3iC5xSiVU1lCiosaZLHQFjJ3VbEqqx9ppgHB0ZuILYJ4oqWG9-84-PFxYtVCGz5a9iKLP1DIR-VIjr-N27AaK04qHsJIYxOSsDaWcp1bZ3ZoK5gQNgyESbIKMAzehfJM20WKAUz2lS2_k9H2jW29MW520hrTqrlKGs_C12qFGGnYcB_Vh4-Zju8WhR1tXFYfHHkj6s-DHWthYHfRqquzNweTWQUe22Z246l1fkFUTeTjXz322yxUBtNhvyY3iqg7murNsJkuDmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f9q0uCuulOO2iU3y0CPBzvFy1Vl_btD1kH9bSlMmy6UtuLzuVHkx7SQHcENPFLfOGPSxVPONPsxaFPcyK2A5bGjlloMFeMKjVaHT5Agb2hugFdgrQ47euG2V_ITC3qs7y3EP-V7xN5IGDzJJh93H1Msx2o9riX-UiP4wfrmWDpnRbD-neMsp-jHM2jQQXuUi-2bfoVUFYlhmcvUC3acrR4Glmn3AC9I7_g9XLMjmtgPWXUJf7eNUJtVRbvyjdv9rho2GUZHUyIB1IOnCgzGQh5uhe46OHIlmpGQqCadyMJgQCulFUI1YBRqEFfYwOUTKHCja4aEHFLCywzbz8dYG3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
رئیس‌جمهور ترامپ و رئیس‌جمهور زلنسکی در اجلاس جی۷ به طور مختصر صحبت کردند.
🔴
آنها امروز بعداً در حاشیه اجلاس دیداری خواهند داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/128455" target="_blank">📅 15:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128454">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
اسرائیل هیوم: دونالد ترامپ داره گزینه برکناری مقاماتی که با توافق ایران مخالفن رو بررسی میکنه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/128454" target="_blank">📅 15:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128453">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
قطر: تفاهم کنونی تهران و واشنگتن نخستین گام به‌سوی توافقی گسترده‌تر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/128453" target="_blank">📅 15:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128452">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
فیدان : ترکیه همون‌طور که می‌دونید یه کشور مهم و قدرتمند تو منطقه‌ست ، برای همین هر موضعی که می‌گیره واقعاً می‌تونه اثرگذار باشه و فرق ایجاد کنه
🔴
سیاستی هم که رئیس‌جمهور ما با محوریت ثبات و اولویت دادن به صلح پیش گرفته، تو موضوع جنگ ایران تو منطقه هم خودش رو نشون داده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/128452" target="_blank">📅 15:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128451">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
فیدان : بعضیا به خاطر گذشته سکوت می‌کنن (اسرائیل)
🔴
بعضیا پشت پرده درگیر تجارت و توافق می‌شن یا حتی تو انتخابات با هم تعامل‌های پنهان دارن
🔴
نتیجه‌اش این می‌شه که این وضعیت ادامه پیدا می‌کنه و همه طرف‌ها در نهایت آسیب می‌بینن
🔴
برای همین هم تأکیدم اینه که کشورها باید جدی‌تر و هماهنگ‌تر عمل کنن، تا جلوی اقدام اسرائیل تو منطقه رو بگیرن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128451" target="_blank">📅 15:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128450">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
فیدان، وزیر امور خارجه ترکیه : اگه یه «درک و هماهنگی مشترک» بین کشورها شکل بگیره؛ و این به یک «اقدام دیپلماتیک جمعی» تبدیل بشه، اسرائیل عملاً دستش برای اقدام بسته می‌شه
🔴
به نظرم کشورها باید صریح و هماهنگ عمل کنن، اشتباهات رو هم سریع و مشترک پاسخ بدن
🔴
چون همین فشار و اجماع بین‌المللی می‌تونه جلوی اقدامات اسرائیل رو بگیره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/128450" target="_blank">📅 15:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128449">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
بری و قالیباف در تماسی تلفنی: واشنگتن باید اسرائیل را به پایان دادن جنگش علیه لبنان ملزم کند.
🔴
اسرائیل باید مجبور شود تخریب روستاهای لبنانی را متوقف کند و از سرزمین‌های اشغالی عقب‌نشینی نماید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/128449" target="_blank">📅 15:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128448">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
شورای هماهنگی بانک‌ها: سپرده‌ها و اطلاعات مالی مشتریان بانک‌های ملی، صادرات، تجارت و توسعه صادرات امن است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/128448" target="_blank">📅 15:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128447">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8d0fd899e.mp4?token=MFbXQ4xuUZEkalt1Mjgk3wGyLMVIAjGjBXhJfG6kkpmFzvOjlfak_-PtZ30uvXuMWWDMt21_YYbQzPSsNT19Q1b7kPqY6kaCGhZ5VmOV_CeuE6XrGOH6EtC1nj4jnWkZDOLYC4XLMbXD33qq0zzX_tTcKFyWkUpZp7C7CQLko3FTkO_obkmrGReshqZJFU63rQWREycmv5ksrSqVryFxIQbmwXUWt6c5JH1yJyVA7-bXDGPr-XPpLercRcP2TwVpG2mME5TGqoyN-ZkC0cd4efFQwPa0SYuMDowihGXL562Sm6Y_TV0yzSynfCBBtxfk_vJNS9jTbhhZPSh_HbSjOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8d0fd899e.mp4?token=MFbXQ4xuUZEkalt1Mjgk3wGyLMVIAjGjBXhJfG6kkpmFzvOjlfak_-PtZ30uvXuMWWDMt21_YYbQzPSsNT19Q1b7kPqY6kaCGhZ5VmOV_CeuE6XrGOH6EtC1nj4jnWkZDOLYC4XLMbXD33qq0zzX_tTcKFyWkUpZp7C7CQLko3FTkO_obkmrGReshqZJFU63rQWREycmv5ksrSqVryFxIQbmwXUWt6c5JH1yJyVA7-bXDGPr-XPpLercRcP2TwVpG2mME5TGqoyN-ZkC0cd4efFQwPa0SYuMDowihGXL562Sm6Y_TV0yzSynfCBBtxfk_vJNS9jTbhhZPSh_HbSjOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار صدا و سیما: عملیات رفع محاصره دریایی اجرایی شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/128447" target="_blank">📅 15:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128446">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">سایمون کوپر در کتاب «فوتبال علیه دشمن» اینجوری میگه فوتبال فقط یک بازی معمولی نیست. اگر یک تیم حمایت طرفداران و مردمِ خود را نداشته باشد، فرقی با یک مشت دلقک که بیهوده به دنبال یک توپ می‌دوند ندارند.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/128446" target="_blank">📅 15:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128445">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPl-1Amxu3CZap9ezS3HK04tLTHl0xQRzIGoHMjJDfjRodroobRzq_QEM13VYmsKu4_-nTT3AAB5wxR3UIUaFlD2W4dPnXtvljvxfUh0A6L5pFw43M-K_eYPi02Ve3xpAMG_lW5Xuaxw20ErJHX5GoopwkZUsBFJKKbcpWlBsTmDsSVLqwwHZCJMsbj7MHk7kNpPiCaY8z8CmsSfmzQ2leRMuscwqxn-1PUtLnCI7-4Bm3Yidbsrk9E58-ZHwoV-DZXIfkKKRCAGctQxhl3vCXx_J3I8IFcFcHBze6tRogGUDWNpDKi0m89PmFSwqhcz7a5VscvcgpTwUi8CdzeYPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دراپ سایت:
ایران برای تحلیل رفتار ترامپ، دوتا روانشناس به تیم مذاکره کننده اضافه کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128445" target="_blank">📅 15:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128444">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzluCiSxidiVaGtC-o2tKCk7DNqy98ygKIp516UwlTvzQhdIUhhwk-FwAqpA2logdxkNj_syUphw-02ThXEaasR93opM1hID0zwEx_XNTR0-sxj7ix2NaY99jNWAKj3EnxabzEGGZSLRpFgWJoIosKWx16O87A2hjj0IB9jJ4OmP8UunVPue6UOZZXcI4to2efU4VvAK6RLEnAib9dW_8M7BwXHP9f5pRXosKs8JiA4hPjILxGf7qRye3UbLWcPlGVOhb-OApl7QPcRtEL_zXp-irktCHvAD39ewYj00NS8tWE7D_t7gtPAfiuDH_n9HenxpubkZRStp03gu8YZ2Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاهش چشمگیر قیمت آیفون ۱۷ پرومکس در بازار ایران
🔴
یفون ۱۷ پرومکسِ بدون رجیستر که قیمت آن در بازار تا حدود ۲۵۰ میلیون تومان هم رسیده بود، حالا با کاهش بیش از ۳۰ میلیون تومانی به حدود ۲۱۶ میلیون تومان رسیده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/128444" target="_blank">📅 15:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128443">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
عرزشی ها میدونم اعتراض دارید به نوکری کردن برای آمریکا.
🔴
47 سال به آمریکا شعار مرگ فرستاد سر آخر زانو زدید.
😅
ولی اغتشاش راهش نیست. بازیچه حکومتی ها شدین.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/128443" target="_blank">📅 15:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128442">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
معاریو: نتانیاهو تقریباً تنها مانده و مشاوران نزدیک خود را از دست داده
🔴
نهاد‌های امنیتی درباره تغییرات ناگهانی مواضع ترامپ، به نتانیاهو هشدار داده بودند، ولی او جدی نگرفته بود که نشان دهنده ضعف در ارزیابی ریسک‌های سیاسی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128442" target="_blank">📅 15:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128441">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb659ad616.mp4?token=OQumEitDGQ0iK4SWyuAYI9qHnYkouPB07pE2aMuu1_QqdBcSIGESE1eGDBcYtSsX0niXh9u38s8SKZ-6xtUwDhnlh9J3YYWN3P7YbhdTEsgdHIbzszcyDNUDKoAYqUyDfes6V-wjfrBm26zih0zTYPAkCuehKHpamjE0KQS3mRY3K5wOtDQ2qCaDHCyRn0kp7qkPuh6_dkWv8HQPjllmlZQtaJ9exH1l6toUbJjyb9CmXpH2w8MmdigFHcR5gQA7S8a2NFKF_zQqHHuI9P-Mc2Z5Y3DaSnVmG_2mfo6iSq6RnuN5S0s_yBZXU0BU-ts0dyr_dEAK750FbQJjkUHTXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb659ad616.mp4?token=OQumEitDGQ0iK4SWyuAYI9qHnYkouPB07pE2aMuu1_QqdBcSIGESE1eGDBcYtSsX0niXh9u38s8SKZ-6xtUwDhnlh9J3YYWN3P7YbhdTEsgdHIbzszcyDNUDKoAYqUyDfes6V-wjfrBm26zih0zTYPAkCuehKHpamjE0KQS3mRY3K5wOtDQ2qCaDHCyRn0kp7qkPuh6_dkWv8HQPjllmlZQtaJ9exH1l6toUbJjyb9CmXpH2w8MmdigFHcR5gQA7S8a2NFKF_zQqHHuI9P-Mc2Z5Y3DaSnVmG_2mfo6iSq6RnuN5S0s_yBZXU0BU-ts0dyr_dEAK750FbQJjkUHTXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صدراعظم آلمان، فریدریش مرز، به رئیس‌جمهور ترامپ یک پیراهن سفارشی تیم ملی فوتبال آلمان با نام «TRUMP» با شماره ۴۷ هدیه داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/128441" target="_blank">📅 14:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128440">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1153104f58.mp4?token=a3v4x6aNi6i0hwijMufLAvfVa0n3aK1q5lMYOoyEBDKMhr-owQwaSYRTjzALQvaO3ZzdXE45j-b6BWM8h71PNPfkNL94gxKc0oiiCO26ehHhwJko6_VTz8J7CP6DVvcNzijA3_NZ189igo_4OY0bbrU_a-kE-DBN20scSfSpszgBca4mATPYSlZMUNItVX0yfTICJ-5UZZsC48FCIk7joi-i6fESjrG5AqrrLQPVPLZmpC-aihuAHk2o0yxV6zb-YjyuGYBxzxDu9i72JQuSMs5JYYlRHwxedimltc0pbwA4Kir7uhceUsJvXkgqyPYea-kA-xRZsmXKFoz6pLtfWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1153104f58.mp4?token=a3v4x6aNi6i0hwijMufLAvfVa0n3aK1q5lMYOoyEBDKMhr-owQwaSYRTjzALQvaO3ZzdXE45j-b6BWM8h71PNPfkNL94gxKc0oiiCO26ehHhwJko6_VTz8J7CP6DVvcNzijA3_NZ189igo_4OY0bbrU_a-kE-DBN20scSfSpszgBca4mATPYSlZMUNItVX0yfTICJ-5UZZsC48FCIk7joi-i6fESjrG5AqrrLQPVPLZmpC-aihuAHk2o0yxV6zb-YjyuGYBxzxDu9i72JQuSMs5JYYlRHwxedimltc0pbwA4Kir7uhceUsJvXkgqyPYea-kA-xRZsmXKFoz6pLtfWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی منتشر شده از آسیب و نابودی تعدادی از  هواپیما های ترابری مستقر در فرودگاه شیراز در جنگ 39 روزه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/128440" target="_blank">📅 14:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128439">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
خبرنگار الجزیره: محاصره دریایی آمریکا علیه ایران لغو شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/alonews/128439" target="_blank">📅 14:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128438">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAf6MuFu4eO421CqiyvEO04ZTQdGRL78CrXM4rXxHeiUSQR7YZLH12RTI6ubsuoI0cXFZoQz016MnILDSu3mnx7TZep5YFUgsIUsF2VQwpmPiIoLSWRai4pFcFOU3yzO8MvetaAT4WRizvStMIGegnCJQRHkkEOslwfkcJ4GdOYDEjffaTvpt05R6aF_q4gxh_0wECI_hQ9Tyxj6qz5XlgBFYlsBZBNzP1HRKfdfHurdiHdgppqbjWABWrkBLuujYcf-iA2cSgEI716j8lexf0dB9XaeGkciHHMH9kSI1dY4KLn848HpLFbW0dbFqKPSvpdZpKiq-L31NujMQhlL4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دراپ سایت: ایران برای تحلیل رفتار ترامپ، دوتا روانشناس به تیم مذاکره کننده اضافه کرده
!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/128438" target="_blank">📅 14:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128437">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ترامپ: اوباما به اوکراین سلاح‌هایی به ارزش ۳۵۰ میلیارد دلار داد.
🔴
او داد، که دیوانه‌کننده بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/128437" target="_blank">📅 14:38 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
