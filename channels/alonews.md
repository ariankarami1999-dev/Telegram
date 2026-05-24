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
<img src="https://cdn4.telesco.pe/file/GF3qY5PHxQrJubVCVnqCBGxJVuDmbjZNpZDpQWCvz4v6KP8LR91hMGs76EOdmBEHKmQ_2dTU_673JQVt-OZ4X6yM88Fcjoi15jLKz0odBD0-LkMpW6L6w4ZjVOmV-w35U9xBVskEvkAg5Aaz--V0vghYMO0Wz4gI1qtyBp7r4dWTyEttM2ks_lpiJeNPQmbvwfMedrMWh9VjicJ_FZZuhtjyP2MwPvOELM_0yxjWcup1Lx2bVUsmFkT2igAzFJjoXqAMJwJqbISNB93xZxbEI5jrhCF5bbcKXGiLKBRw7gnBRg-rHEW6sJJ3X5O3xLuohUGt7smAjsvfU5LrM4XOfg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 938K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-03 11:48:48</div>
<hr>

<div class="tg-post" id="msg-122256">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
نخست‌وزیر بریتانیا: از پیشرفت به سمت توافق بین آمریکا و ایران استقبال می‌کنم
🔴
ما به توافقی نیاز داریم که به جنگ پایان دهد
🔴
ما با شرکای بین‌المللی خود برای غنیمت شمردن این فرصت و دستیابی به یک راه‌حل دیپلماتیک بلندمدت همکاری خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/alonews/122256" target="_blank">📅 11:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122255">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef4a57f0a5.mp4?token=KyKXG48aW5Ll9bzIdX6KZOa-UKZftQ6DbgtzViu3VI2OetNXaMwcJWstjne3Tz_rXNn4rdlID1QCswz3BbAw9R1MQpZ763U1YN6ecR-mxidlS0oArlaTG2ZKoxlSqqVy7xSJ_uWvsBumA329LThHKzChtjAeXobGMVfh99lxdouIFNASKWP4A5_39W7YQ_z2C9xiCFXv3JbP_W0O8tKZ11q2DugzOXifhIMvLFBfqqgXhmiNSicZKKEyxyU3WMzh91JW4fJXVnDELI_0uLB5eT7FGwA_8E3iOTgnDvlPOOIYlU0VozDndpb_BdZdYkYSg_9nSCA5Lorxy83ip_vFnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef4a57f0a5.mp4?token=KyKXG48aW5Ll9bzIdX6KZOa-UKZftQ6DbgtzViu3VI2OetNXaMwcJWstjne3Tz_rXNn4rdlID1QCswz3BbAw9R1MQpZ763U1YN6ecR-mxidlS0oArlaTG2ZKoxlSqqVy7xSJ_uWvsBumA329LThHKzChtjAeXobGMVfh99lxdouIFNASKWP4A5_39W7YQ_z2C9xiCFXv3JbP_W0O8tKZ11q2DugzOXifhIMvLFBfqqgXhmiNSicZKKEyxyU3WMzh91JW4fJXVnDELI_0uLB5eT7FGwA_8E3iOTgnDvlPOOIYlU0VozDndpb_BdZdYkYSg_9nSCA5Lorxy83ip_vFnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو: هیچ مسیر آبی بین‌المللی و هیچ فضای هوایی بین‌المللی نباید هرگز توسط هیچ کشوری در جهان ملی‌سازی شود. این نباید هرگز به عنوان یک هنجار جدید پذیرفته شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/alonews/122255" target="_blank">📅 11:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122254">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
منبع ارشد ایرانی به رویترز: تهران با تحویل ذخیره اورانیوم بسیار غنی شده خود موافقت نکرده است.مسئله هسته‌ای ایران بخشی از توافق اولیه نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/alonews/122254" target="_blank">📅 11:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122253">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
روبیو: پیشرفت بزرگی در مورد بحران با ایران حاصل شده است
🔴
این احتمال وجود دارد که جهان در ساعات آینده اخبار خوبی بشنود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/alonews/122253" target="_blank">📅 11:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122252">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
روبیو، وزیر خارجه آمریکا: پس از همکاری با کشورهای خلیج فارس، در مورد ایران پیشرفت کرده‌ایم
🔴
احتمالاً اخبار بیشتری درباره ایران امروز منتشر شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/122252" target="_blank">📅 11:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122251">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FboTZXU3bjHjB6C77bloxnFPgqMhJx1gOIhY583Qr37EgbRxz9Z2pPU7vtY3fasGk_xm0r-KvU0kIiL-pU5vTC0d6GsNIdin6-cphDIV9iPC-g4fSLRQiWKq1gZoFZrFJ0n5K16XwN9wtmUD9vmYS0i1Shfb73DttmKr-tPfpeLAV5_JsDciTHAO1T6YMUaBcL2Epj_JQL3hQtxU1s8eXK1nY5C3NFoIAN5rRGQ8UxJfR7GpIyXeIL6vfafZcuQUs_NbRtSJ3eTPPiNlQCm00U8azIEIU-pFGEYSlEYn2_Jx5oRCHF6u7hQ5rAkvPiCMn-aI9YaOjx-uskGJw11hpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ، سال ۲۰۲۰ میلادی: ایران هرگز جنگی را نبرده، اما هرگز مذاکره‌ای را هم نباخته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/alonews/122251" target="_blank">📅 11:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122250">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/122250" target="_blank">📅 11:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122249">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1mwfChq1eUrBKoaGbKglHOR-nSdCtry9THCQCnv5g2I9_ZGJxtxN9C_n9s-zy16V7iYxj__7LHyRhbHibolnLVPYXEqQhRoy9mf7ApIq9cr2v1Uiz044rMCFYJNwJXP4WiX6ihLYAWqMIwrayVn_p1-xpxhTBmCwyYAA7YfjU15LyXxGbEW4iur8dfy0LXbTJd-IHxVvekAAeyKH8pbot13MlmDN1nX-IMkYjKCfNpmhLqr_bmsb7LBtBdNiwFqaS8D6W-AwqOttaLwqQmSt-DojWMxjkeQdKjoxIjdcYmH4N4SEx9FKSz04gfLo0uoPMm8x15LKcR-R42OzA9Tdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
گیگی ۱۴۹ تومن
🔴
🔴
🔴
🔴
گیگی ۱۴۹ تومن
🔴
🔴
🔴
🔴
گیگی ۱۴۹ تومن
🔴
🔴
______________________
لینک سابسکریشن
✅
تست رایگان
✅
بدون محدودیت کاربر و زمان
✅
تضمین عودت وجه
✅
@darkoob_config1
@darkoob_config1
@darkoob_config1</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/alonews/122249" target="_blank">📅 11:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122248">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
پزشکیان: بنده نسبت به مشکلات اقتصادی و معیشتی مردم، به‌ویژه آسیب‌هایی که در پی شرایط جنگی تشدید شده، احساس مسئولیت جدی دارم و با تمام توان در حال تلاش برای کاهش فشارها بر مردم هستم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/alonews/122248" target="_blank">📅 11:03 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122247">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
پزشکیان: آنچه در مقاطع حساس، ضامن حفظ و ثبات کشور بوده، همبستگی و همدلی مردم و ارکان نظام است.
🔴
با وجود مسائل و مشکلات متعدد، از بیان بسیاری از مطالب صرف‌نظر می‌کنم تا مبادا زمینه تفرقه و اختلاف فراهم شود. امروز حفظ وحدت و انسجام ملی به‌مراتب مهم‌تر از مسائل نظامی و امنیتی است
🔴
همواره تلاش کرده‌ام سخنی بر خلاف نظر مقام معظم رهبری بیان نشود و یا موضعی اتخاذ نگردد که به اختلاف میان ارکان حاکمیت دامن بزند و دشمن از آن سوءاستفاده کند.
🔴
هر سخن، تحلیل یا موضعی که از هر تریبونی، به‌ویژه صدا و سیما، منجر به ایجاد شکاف و تفرقه در جامعه شود، در عمل آب ریختن به آسیاب دشمن است
🔴
گاهی برخی کارشناسان در رسانه ملی سخنانی مطرح می‌کنند که با واقعیت‌های جاری کشور و روندهای موجود فاصله جدی دارد، اما دولت به‌منظور جلوگیری از اختلاف و حفظ آرامش جامعه، از واکنش و موضع‌گیری پرهیز می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/alonews/122247" target="_blank">📅 10:53 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122246">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
‌فارس: بررسی متن نهایی‌شده توافق احتمالی، نشان می‌دهد
آمریکا و متحدانش متعهد می‌شوند که به هیچ وجه به ایران یا متحدانش حمله نکنند.
🔴
در مقابل، ایران نیز متعهد شده که خود و متحدانش به آمریکا و متحدان آن حملۀ نظامی پیش دستانه نداشته باشند.
🔴
طبق پیش‌نویس توافق، طرفین بر سر آزادسازی تمام یا بخشی از پول‌های مسدودشدهٔ ایران به منظور ورود به مذاکره توافق کرده‌اند
🔴
همچنین طبق این پیش‌نویس، امکان تردد در تنگهٔ هرمز به تعداد قبل از جنگ و با مدیریت ایران، همزمان با برداشتن محاصرهٔ دریایی فراهم می‌شود.
🔴
علاوه بر این، تحریم‌های نفت، گاز، پتروشیمی و مشتقات آن در دورهٔ مذاکره به‌طور موقت لغو می‌شود تا ایران بتواند آزادانه به فروش محصولات خود بپردازد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/alonews/122246" target="_blank">📅 10:48 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122245">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
خبرگزاری معتبر تسنیم: پیش نویس توافق با واشنگتن مقرر می‌کند که وضعیت حاکمیتی تنگه هرمز به شرایط پیش از جنگ باز نگردد و تنها تعداد کشتی‌های عبوری ظرف ۳۰ روز بازیابی شود، که همزمان با رفع کامل محاصره دریایی و اجرای تعهدات آمریکا است. تهران بر حفظ حق حاکمیتی خود بر این تنگه تأکید دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/alonews/122245" target="_blank">📅 10:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122244">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
العربی الجديد به نقل از منبع ایرانی:
پیش‌نویس توافق بین تهران و واشنگتن شامل پایان جنگ در تمام جبهه‌ها از جمله لبنان است
🔴
بخش بزرگی از دارایی‌های مسدود شده ایران در خارج آزاد خواهد شد و محاصره دریایی برداشته شده و تنگه هرمز بازگشایی می‌شود
🔴
وضعیت موجود در پرونده هسته‌ای و تحریم‌ها حفظ خواهد شد
🔴
تهران در دوره ۶۰ روزه از کاهش تحریم‌ها برای فروش نفت خود بهره‌مند خواهد شد
🔴
هنوز برخی اختلافات برای حل شدن قبل از اعلام توافق موقت باقی است و توپ در زمین آمریکاست
🔴
هیچ چیز را نمی‌توان تضمین شده یا نهایی دانست مگر اینکه همه جزئیات توافق شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/alonews/122244" target="_blank">📅 10:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122243">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
راضیه عالیشوندی، معاون امور بین‌الملل و حقوق بشردوستانه جمعیت هلال‌احمر: محموله‌های کمک‌های بشردوستانه کشورهای عراق، ازبکستان و قزاقستان وارد ایران شد.
🔴
این کمک‌ها شامل اقلام غذایی، دارویی و تجهیزات پزشکی است.
🔴
این کمک‌ها در راستای حمایت از عملیات امدادی و تامین نیازهای اقشار آسیب‌پذیر در اختیار جمعیت هلال‌احمر قرار گرفته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/122243" target="_blank">📅 10:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122242">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mN0KxK3VtSDuIc0JImIge2myR6d7Wmo3e73zkT7rsero9EG4iFiOWQyeLm_i3tv8EZ-RyjBfgaFo0qkgh86PXrmXz7LZdeAeI7eDGpheuHYvrYDYZzu9Rjz1dCASY9f7ZtLjUSTRmEpq7YiaL-fwb3iF_9Z7d87U43IXy5-oQ77qMS0hDNujoRk6rydO05Fsqfb3WYeoCcFsSSDKXawbGj0ly6p-w3PUuHiJ0766R60N8Wi2Czb0PG9M51ymuDw3RGsjre14CCKjvd8XqppuRKjzQjdmjJkFr_RILKIS-djb0PsEGUdCKho5e3IzMm03o6GKzQ_xvL8tBVDMyaZ9iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخست‌وزیر پاکستان، شہباز شریف: من به رئیس‌جمهور دونالد ترامپ بابت تلاش‌های فوق‌العاده‌اش برای پیگیری صلح و برگزاری یک تماس تلفنی بسیار مفید و سازنده در اوایل امروز با رهبران عربستان سعودی، قطر، ترکیه، مصر، امارات، اردن و پاکستان تبریک می‌گویم.
🔴
فیلد مارشال سید عاصم منیر نماینده پاکستان در این تماس تلفنی بود و من از تلاش‌های بی‌وقفه او در طول کل این فرایند بسیار قدردانی می‌کنم.
🔴
این گفتگوها فرصتی مفید برای تبادل نظر درباره وضعیت کنونی منطقه و چگونگی پیشبرد تلاش‌های جاری برای صلح به منظور آوردن صلح پایدار در منطقه فراهم کرد.
🔴
پاکستان تلاش‌های صلح خود را با نهایت صداقت ادامه خواهد داد و امیدواریم به زودی میزبان دور بعدی مذاکرات باشیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/alonews/122242" target="_blank">📅 10:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122241">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7-p5nDX6EHVXJB1mKPf86B8DvbS93tN35eEZcbUe60tpBDzgis41Bk4zL62HDI0jHYhk5iZWigngcC4cQMUXCGnPv7Rp-JdFk93kw1L6be61ayQvW5y64guiYVLSp3mu1TNgNL8fmwCMC5GEMpOpc60z1nC3zkPS4AUp-1atLibcf3d-VhWm4Enl4UyAWMJggBseWUWZFJgGTtPQJXj2tN-86994nzOXJ2fE15iw1PzuAyhKM95DQoFjDLi1XPiElyPzp7YkrOFONGgsEk4jVtnkcKwsaWljNvI2wLJ_7pIzQ_tIsdAhTKK49ONCLe-baToqMjQ4SnPD7jja0pN_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مونیکا ویت کیست؛ نظامی سابق آمریکایی که به جاسوسی برای ایران متهم شد و اف‌بی‌آی برای او جایزه تعیین کرد
🔴
اف‌بی‌آی به تازگی اعلام کرده است که برای دریافت اطلاعات منجر به بازداشت و محاکمه مونیکا ویت، عضو پیشین نیروهای مسلح و مامور سابق ضدجاسوسی آمریکا، ۲۰۰ هزار دلار جایزه تعیین کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/alonews/122241" target="_blank">📅 10:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122240">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
آزادسازی نیمی از دارایی‌های بلوکه‌شده ایران به ارزش ۱۲ میلیارد دلار نیز در این چارچوب این یادداشت تفاهم پیش‌بینی شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/alonews/122240" target="_blank">📅 10:18 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122239">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
کابینه جنگ اسرائیل امشب تشکیل جلسه میده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/122239" target="_blank">📅 10:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122238">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
تتر دوباره رفت بالا و الان 170,500
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/122238" target="_blank">📅 10:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122237">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
تشکر ترامپ از سرویس مخفی برای دستگیری تیرانداز دیشب: از سرویس مخفی و نیروی انتظامی عالی‌مون به خاطر اقدام سریع و حرفه‌ای که امشب علیه یک فرد مسلح در نزدیکی کاخ سفید، که سابقه خشونت‌آمیز و احتمالاً وسواس فکری نسبت به گرامی‌ترین بنای کشورمون داشت، انجام شد، سپاسگزاریم.
🔴
فرد مسلح بعد از درگیری با مأموران سرویس مخفی در نزدیکی دروازه‌های کاخ سفید کشته شد.
🔴
این اتفاق یک ماه بعد از تیراندازی در ضیافت شام خبرنگاران کاخ سفید رخ داد
برای همه روسای جمهور آینده مهمه که امن‌ترین و مطمئن‌ترین فضایی رو که تاالان در واشنگتن دی سی ساخته شده، داشته باشن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/alonews/122237" target="_blank">📅 10:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122236">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
خبرگزاری فرانسه: کشته شدن ده‌ها نفر در انفجاری که قطاری را در جنوب غرب پاکستان هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/122236" target="_blank">📅 10:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122235">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
تسنیم: اسقاط تحریم‌های نفتی ایران در طول دوره مذاکره از بندهای تفاهم احتمالی است
🔴
شنیده‌ها از جزئیات تفاهم اولیه «احتمالی»، میان ایران و آمریکا حاکی است که واشنگتن متعهد خواهد شد در طول دوره مذاکرات، تحریم‌های نفتی ایران را به حالت اسقاط (Waive) درآورد؛ اقدامی که به ایران امکان می‌دهد در این بازه زمانی، نفت خود را بدون محدودیت‌های ناشی از تحریم به فروش برساند.
🔴
بر اساس اطلاعات منتشرشده، در صورت تأیید مفاد تفاهم اولیه از سوی دو طرف، ابتدا یک تفاهم‌نامه (MOU) اعلام خواهد شد؛ تفاهمی که در آن پایان جنگ در تمامی جبهه‌ها، از جمله لبنان نیز مورد تأکید قرار می‌گیرد. اسرائیل نیز بر اساس این بند به عنوان متحد آمریکا باید جنگ در لبنان را پایان دهد.
🔴
پس از آن، یک بازه ۳۰ روزه برای اجرای اقدامات مرتبط با محاصره دریایی و تنگه هرمز در نظر گرفته شده و همزمان، دوره‌ای ۶۰ روزه برای مذاکرات درباره موضوع هسته‌ای تعریف خواهد شد.
🔴
ایران در مقطع کنونی هیچ اقدامی را در حوزه هسته‌ای نپذیرفته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/122235" target="_blank">📅 10:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122234">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
آخرین قیمت طلا و سکه
🔴
طلای ۱۸ عیار: ۱۷ میلیون و ۸۶۷ هزار تومان
🔴
سکه طرح جدید: ۱۸۶ میلیون و ۵۰۰ هزار تومان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/alonews/122234" target="_blank">📅 10:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122233">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
وزیر خارجه پاکستان: دیپلماسی و مذاکره باید بر درگیری غلبه کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/122233" target="_blank">📅 09:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122232">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
اردوغان: ترکیه آماده است در مرحله اجرای هرگونه توافق جمهوری اسلامی و آمریکا، همه حمایت‌های لازم را ارائه دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/122232" target="_blank">📅 09:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122231">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4bHXpnuVnaFjm5UoKp3VptkxF2CyObswtT-GCuAr-HlJQsVynUnN-j4kjLqMWX4ss6FXKJsqgzlBjwB6dI-HsS3IU0oFDLmA_P-52-Nu1e7SB4e3wJ72h8OUbAphZ87psW_W9pvXqFkUyZ54eozMNb6KqHTHPpZHuy69UA0dRf7qXDmYCZwvpYDVTFQ8iNYkdHU-QsniDu0U_7dTZWP8oHdYbjTuwJC36qHZNtf6YeeH41QHMwuJx2KmzqCpn0O_D2-uG7-nPAsoA89-WcgNDy-Qs0LyWy7N1URiDEGwEkeSXaeB7lbV9gfSEoqDnL3ZDaxCaFNGT9v2QQ2ZiwH0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر فرد مهاجم در نزدیکی کاخ‌سفید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/alonews/122231" target="_blank">📅 09:53 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122230">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQRfQILv4wGLomEaJdWqOW-PWuGOJVBcIsdebRqLWGIPytg8yFaEIvEA5y57UsI5jRhJciNHZOq9_cZQv9T6QxsbxWr0kVre0Z5e7QdKKKem8cL9pKRdh9GPZC4Iss8Gc-ZRiYVvwVAoVaZdKfl25a0-fOGX7k0M9OCJL9c34VyevORiO540GgX6lxibPGY8sVTCdiIn2z2p3Dmd0K4Z2LEEZWZzCd-rwKYb2U6390v814cIVmiNw8dDj5oId1y_iXARsVYTKkVrtzEKTyn6IR_lpsM7wJMtgrgJYir9VFO4fIc7jvFMUhq9gsFL2PmMcoOvQh73XYznbcc2gGdVAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس تهران در دقایق نخست آغاز فعالیت با رشد حدود ۶۳ هزار واحدی در آستانه ورود به کانال ۳ میلیون و ۹۰۰ هزار واحدی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/122230" target="_blank">📅 09:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122229">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
ممکن است ظرف چند روز توافقی بین آمریکا و ایران حاصل شود که انتظار می‌رود لبنان را نیز شامل شود و احتمالاً به پایان درگیری‌های اسرائیل با حزب‌الله منجر شود.
🔴
بر اساس جزئیات منتشر شده، ایران تنگه هرمز را بدون دریافت هزینه باز خواهد کرد در حالی که آمریکا پولی به تهران منتقل نخواهد کرد و به هر دو طرف مهلت ۶۰ روزه داده می‌شود تا مذاکرات هسته‌ای را ادامه دهند.
🔴
تحریم‌ها علیه ایران باقی خواهد ماند به جز تسهیلات محدودی در محدودیت‌های مرتبط با نفت، طبق گزارش کانال ۱۴ اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/122229" target="_blank">📅 09:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122228">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
روزنامه دولت: طیفی که از اساس منتقد مسیر مذاکره و در صف منتقدان قالیباف هستند، خواهان تمدید ریاست او بر مجلس نیستند
🔴
روزنامه ایران نوشت: گزینه اصلی برای ریاست مجلس در اجلاسیه سوم محمدباقر قالیباف است که ریاست «هیأت مذاکراتی میناب ۱۶۸» را بر عهده دارد؛ مشخص است طیفی که از اساس منتقد این مسیرند و در صف منتقدان قالیباف، خواهان تمدید ریاست او بر مجلس نباشند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/122228" target="_blank">📅 09:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122227">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
هم‌زمان با انتشار خبرهای مربوط به توافق ایران و آمریکا، "تتر" در مسیر کاهش قیمت قرار گرفت و به ۱۶۶ هزار تومان رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/122227" target="_blank">📅 09:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122226">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
خوش چشم، کارشناس صدا سیما: احتمال می‌دهم ظرف یک هفته آینده جنگ مجددا آغاز شود
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/122226" target="_blank">📅 09:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122222">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7c605c4ed.mp4?token=un_reTaXFtDBYrmugWF5ZsiiemcEdNDkTQGghEtSf4qQ82kcHkXMMZY5RcCy2IqZzQ9GMw7Ha2zIXpz5fajwdRITcQIyDK8I-lrn8FNFZskBWP9j-dsVj1fKjregt-qL7_LGze6OjXXykbrEAsi0DBiBearsfluuVAXJBG_ZaN3qGbEazpJhghU9IjkUbgHTTu6qZNGreWAcHCQTJCXuoHabwRzOZ5h37l5g7k2eEcmT4EnIT1Soq_0P0U_-tDKjDhWtyQeAPV5p1LLjCMVaJXXuK3sU38SC6WrviWQ1DYWocCMgOKMzWfxDE9CH-wN7cMdUVCRBoLkp7IAT1jiZkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7c605c4ed.mp4?token=un_reTaXFtDBYrmugWF5ZsiiemcEdNDkTQGghEtSf4qQ82kcHkXMMZY5RcCy2IqZzQ9GMw7Ha2zIXpz5fajwdRITcQIyDK8I-lrn8FNFZskBWP9j-dsVj1fKjregt-qL7_LGze6OjXXykbrEAsi0DBiBearsfluuVAXJBG_ZaN3qGbEazpJhghU9IjkUbgHTTu6qZNGreWAcHCQTJCXuoHabwRzOZ5h37l5g7k2eEcmT4EnIT1Soq_0P0U_-tDKjDhWtyQeAPV5p1LLjCMVaJXXuK3sU38SC6WrviWQ1DYWocCMgOKMzWfxDE9CH-wN7cMdUVCRBoLkp7IAT1jiZkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چندین آتش‌سوزی بزرگ در کی‌یف، اوکراین، پس از حمله موشکی گسترده روسیه مشاهده می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/122222" target="_blank">📅 09:34 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122221">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
رویترز به نقل از وزیر امور خارجه پاکستان: تماس تلفنی مهم رئیس جمهور ترامپ گامی اساسی در جهت دستیابی به صلح منطقه‌ای است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/122221" target="_blank">📅 09:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122220">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
سرویس مخفی اعلام کرده است که مظنون ۲۱ ساله تیراندازی نزدیک کاخ سفید در اثر آتش متقابل جان خود را از دست داده است.
🔴
مقامات اجرای قانون به سی‌ان‌ان گفته‌اند که تیرانداز مظنون نزدیک کاخ سفید قبلاً توسط سرویس مخفی شناخته شده بود و چندین بار تلاش کرده بود وارد محوطه کاخ سفید شود، اگرچه در آن حوادث قبلی نه مسلح بود و نه خشونت‌آمیز.
🔴
مظنون به عنوان فردی که ممکن است «دارای اختلالات عاطفی» باشد توصیف شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/122220" target="_blank">📅 09:28 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122219">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
مواضع رسانه‌های عبری نسبت به توافق احتمالی واشنگتن و تهران
🔴
کانال ۱۲:  ساعات آینده تعیین‌کننده است و جزئیات راه‌حل در حال شکل‌گیری میان ایران و ایالات متحده به نفع اسرائیل به نظر نمی‌رسد.
🔴
یدیعوت آحارونوت: نگرانی فزاینده در اسرائیل از تفاهمات در حال شکل‌گیری میان ایالات متحده و ایران شکل گرفته
🔴
معاریو:  پیروزی ایران نزدیک است و اسرائیل باید محاسبات خود را از سر بگیرد، جایگاه خود را در منطقه مشخص کند و ائتلاف‌های تازه‌ای شکل دهد.
🔴
برخی دیگر از رسانه‌های اسرائیلی «سکوت مطلق» نخست‌وزیر و دفتر او را نسبت به اخبار مربوط به نزدیکی امضای توافق میان ایران و ایالات متحده محکوم کرده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/122219" target="_blank">📅 09:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122218">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXSom5zG_OdaXC91HPDsE-dXcg3IldtPqX8eHCX7E5RotyOCYhoW95M0aaZX0zaDsvmqrr9ZNA8T-Z0hViY3Plzd9baC7fVwRMt_r8RWWa9lImxy_BRSrnIftDDk51ph1TEhFA5fJWFAw6K2ghyAQD1fs6-nQa0dvJmRuuYg1EiRdPiOKsOM6DNgljtLwrL25CrdIHhtIuSZscHN-Gg_L-syzQ043v9rFafv2WSco591LmsramAqN9RRW_2EgAtf7xk0WrhiyKm4DlooJ-htRGk6wfImlaokvODGX1gWA30NpnfW4ShGPJyMroO-E7lNEhi4cCWQjs_VNrfDhRaw3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی، از رهبران بولشویک‌ها:
هر توافق یا صحبتی بدون تایید مجلس فاقد اعتبار هست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/122218" target="_blank">📅 09:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122217">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
تنگه هرمز قراره باز بشه و هیچ گونه عوارضی هم گرفته نشه و ایران صرفا یک مدیریت نمایشی(نگاه کردن) داشته باشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/122217" target="_blank">📅 09:18 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122216">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayVwiGsfH9hmcMhpwxZLnsLIMkGTFpPONGJNUs4takQVrfn0SFyJwzjvei6mjoB1JESOO20PrYbPKMFqeGRMTcFzipvUPkyza--E-yEFNghK3CPssvDC2CjKT-dGVK9MmAj6eMf2HoBJrz1IrGQ2Qb-l4n9---x0udZSU5lSJFWi4q8PqQ489XllmP9snUQWc2ZfkeIEQKpFXVZkqgMlbx0TCQuPS-yudBUQBz0Nyqq4gtsEQpSgx5gx0TuSz5-cwy7iJ5YjicHtuc2czbIpnypqSG9_Z6Z0SyQ_CNo1m7hfrNggvAkRnOspB7zRuUwLQtrfEN9c4_8uzt8dF-e8Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله تند سخنگوی کاخ سفید به پمپئو: «دهان احمقانه‌ات را ببند»
🔴
استیون چونگ، مدیر ارتباطات کاخ سفید، بهشدت به مایک پمپئو، وزیر خارجه پیشین آمریکا، حمله کرد و گفت: «مایک پمپئو هیچ ایده ای از آنچه درباره آن حرف می زند، ندارد. او به اطلاعات جاری دسترسی ندارد، پس از کجا می داند؟ باید دهان احمقانه اش را ببندد و کار را به حرفه ای ها بسپارد.»
🔴
این تنش پس از آن رخ داد که پمپئو توافق احتمالی ترامپ با ایران را به شدت نقد کرد و آن را مشابه توافق هسته ای دولت اوباما خواند.
🔴
پمپئو در شبکه اجتماعی ایکس نوشت که ایالات متحده باید «تنگه هرمز را باز کند، دست ایران را از پول کوتاه کند و توانایی کافی از ایران بگیرد». در مقابل، ترامپ اعلام کرده که توافق با ایران «تا حد زیادی نهایی شده» و شامل باز شدن تنگه هرمز خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/122216" target="_blank">📅 09:17 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122215">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grOiLkH0TMDYtQNGD4ZwLMDXfO7ceiYm8re2Fj_e0JDEZ-iZhOn2RSdPh-IpGTe9ox0ke-6ORrrPRniLN4SJ5NByoK6MtTE7WN15Ul_lfUw2l5rzIeSp9WwQIfztbZ4SbXfZKlYh5Ncmx0Wj2RvVARPx-XWlBly7bCQG_A-AfXwiPAkYDBP-dXbkF9yec6GMKA-kIpiQXq5WMFLrQyV-Jt3LvJhwyMJnbSO62XdR781G23aHOoqZytgSF570ZR9_Xlb4WKf-mqzKQmy6Txjo3NHhkk55kIpWe3pFt_gajLvuBA0wTpJuqYHQ235_L4xyC6qNh5SrUI2z-ennGf6FZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مایک پمپئو، مدیر سابق سیا و وزیر امور خارجه: توافقی که با ایران مطرح شده به نظر می‌رسد مستقیماً از کتاب بازی وندی شرمن، رابرت مالی و بن رودز باشد: به سپاه پاسداران پول بدهید تا برنامه سلاح‌های کشتار جمعی بسازد و جهان را ترور کند.
🔴
این اصلاً اول آمریکا نیست. واضح است: تنگه لعنتی را باز کنید. دسترسی ایران به پول را قطع کنید. توانایی ایران را به اندازه‌ای کاهش دهید که نتواند به متحدان ما در منطقه تهدیدی ایجاد کند.
🔴
مدت‌هاست که باید انجام می‌شد. بزن بریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/122215" target="_blank">📅 09:17 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122214">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
وزیر خارجه پاکستان:  تماس مهم دونالد ترمپ، رئیس‌جمهور آمریکا، با رهبران پاکستان، عربستان، ترکیه، قطر، مصر، امارات و اردن، گامی اساسی به سوی تحقق صلح منطقه‌ای محسوب می‌شود.
🔴
آنچه مذاکرات به دست آورده، باعث خوشبینی نسبت به امکان دستیابی به نتیجه‌ای مثبت و پایدار است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/122214" target="_blank">📅 09:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122213">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
طبق آمار، میزان ازدواج‌ها نسبت به زمان مشابه پارسال 60% کاهش یافته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/122213" target="_blank">📅 09:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122212">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
جمعیت مجردهای کشور از مرز 13 میلیون نفر گذشت
🔴
بیش از 7.2 میلیون زن زیر 40 سال هرگز ازدواج نکرده‌اند.
🔴
بیش از 9.3 میلیون مرد زیر 40 سال هرگز ازدواج نکرده‌اند.
🔴
کاهش مستمر نرخ ازدواج در کنار روند صعودی طلاق است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/122212" target="_blank">📅 09:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122211">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXyOUe91M5xvmqKVAToY2Tph4rji3hnB4Yl7IrFDJ4vnALZk_b3ECLvRtM1MuxRaozlRuXwJGdF5yr-2r8iO1jAvhTEXOVnN_GCM_PL93IYJM0JxXnD0prxi1ImiSqR47pCEkaTghuizIpArUjxrh5emxBBIeezN_uXDFnXFCsLabHIFfWvj2mVuYfmxJFl2P14LAXK1LOW-U0g1B3Q09nRlto-7uDLUZYm2UPddPCaQ_sQuOHyntCbBBHlW9Apyn3RcNg9omlVluhUlI642lqzSPws6o_Iio0AIBc1k5-kbSGh_3IR9FDGOwye8N-SCLDFxBR4yUmTYD4T_BnqJ3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تک‌تیراندازهای سرویس مخفی روی سقف کاخ سفید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/122211" target="_blank">📅 09:02 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122210">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
اکسیوس، به نقل از یک مقام آمریکایی:
این توافق، بازگشایی تنگه هرمز را در طول دوره تمدید آتش‌بس ۶۰ روزه تصریح می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/122210" target="_blank">📅 08:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122209">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
روزنامه خراسان: اگر منظور از قطع اینترنت بین‌الملل مسائل امنیتی است، بدانید که کاربران با فیلترشکن به هر قیمتی به آن وصل می‌شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/alonews/122209" target="_blank">📅 08:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122208">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
وزیر دفاع پاکستان: به نتایج مثبت برای پایان جنگ خاورمیانه نزدیک می‌شویم
🔴
مسائل در شرف حل شدن است
🔴
همه طرف‌ها در تدارک یک فرجام شایسته برای اوضاع جاری هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/alonews/122208" target="_blank">📅 08:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122207">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4eba5d9ca6.mp4?token=Px9CM05Hmn3KFfVQKzVmBvMFAY9zC1ZSaCE9F3yCaHlypEAvJH574142GXgML-qkBjJySOJm_b7XsI6lcTlzXTFhztEcIS4kaGpImJLBEhbi-VHU_oNgCovfvgAxrzb23vnuWf7h2CsAobfmJRBbMH3x2eWd1l7F-adMI4BbsiAmy1uTM3HCKnoaIPIrSIueFkFYI9vOxshN_TqtH0mp_G4deM5RlT92aPW0IFwxZECE4I86rUhrvBgBYHR7DSX3J9O6ZoiEPbg0fOFnxqNzI53WY5FxdgoPZRUrD29NmtKdEMwFjHBzDGIAX7YVCQc1ZRED9xvNvO_TgNX7ds536A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4eba5d9ca6.mp4?token=Px9CM05Hmn3KFfVQKzVmBvMFAY9zC1ZSaCE9F3yCaHlypEAvJH574142GXgML-qkBjJySOJm_b7XsI6lcTlzXTFhztEcIS4kaGpImJLBEhbi-VHU_oNgCovfvgAxrzb23vnuWf7h2CsAobfmJRBbMH3x2eWd1l7F-adMI4BbsiAmy1uTM3HCKnoaIPIrSIueFkFYI9vOxshN_TqtH0mp_G4deM5RlT92aPW0IFwxZECE4I86rUhrvBgBYHR7DSX3J9O6ZoiEPbg0fOFnxqNzI53WY5FxdgoPZRUrD29NmtKdEMwFjHBzDGIAX7YVCQc1ZRED9xvNvO_TgNX7ds536A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه‌ای که صدای تیراندازی بیرون کاخ سفید به گوش رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/alonews/122207" target="_blank">📅 08:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122206">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
طبق گزارش NBC News، صدای تیراندازی در خارج از کاخ سفید شنیده شد، با حدود ۲۰ تا ۳۰ گلوله شلیک شده. سرویس مخفی به خبرنگاران دستور داده است که برای حفظ جانشان به داخل اتاق جلسه بروند
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/alonews/122206" target="_blank">📅 08:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122205">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
نیویورک تایمز: ایران موافقت کرده است که ذخیره اورانیوم غنی‌شده خود را به عنوان بخشی از توافق برای پایان دادن به جنگ واگذار کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/alonews/122205" target="_blank">📅 08:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122204">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTNWwZ9OEe2T26a-yilhM38GBcrPcauOO2zZDm4MMdZINt_kNzAs5gpNvqDh7Wp5Ye6kb3iZXd18sfLgwZgjJyBoKQGXZcgYVjcNUmK64BhnpFyhm--Ajnqu8dL0RvAvo94YaoynYzI9A3bmV2eZSkmBBhv0lq3hOIzYY8kSVUCbrzR4Cc66D1QF2yFdlGqmjW2-YD9g833Mp9aySToSvP-Poblp8MhzwV8vJ2DbX-7juhNpfxEnxgo8knjBy6WYWFtc9Zi829TTgnXYR-uZwGeGqTqlEUb3is6GOnAYs8Xz7vxX54yUUS7eN1SBfNp9baGISm1RSCStPSVr_Lu9Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: خرمشهر امروز ایران، خلیج‌فارس و تنگۀ هرمز است
🔴
ملت ما امروز هم‌چنان مردم رزم ندیده اما دلیر خرمشهرند که روزها در مقابل ارتش متجاوز ایستادند تا قدرت مردم ایران را به رخ جهانیان بکشند.
🔴
مقاومت، ایثار و دفع تجاوز، ریشه در فرهنگ این سرزمین دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/alonews/122204" target="_blank">📅 08:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122203">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
طبق گزارش NBC News، صدای تیراندازی در خارج از کاخ سفید شنیده شد، با حدود ۲۰ تا ۳۰ گلوله شلیک شده. سرویس مخفی به خبرنگاران دستور داده است که برای حفظ جانشان به داخل اتاق جلسه بروند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/122203" target="_blank">📅 01:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122202">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
وال استریت ژورنال: ترامپ به دستیارانش گفته است که در صورت عدم پایبندی ایران به چارچوب توافق، حق از سرگیری بمباران ایران را برای خود محفوظ می‌دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/alonews/122202" target="_blank">📅 01:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122201">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
نیویورک تایمز: ۲۵ میلیارد دلار از پولای بلوکه شده‌ی ایران قراره واسشون آزاد بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/alonews/122201" target="_blank">📅 01:30 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122199">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از 3 مقام ایرانی: توافق بر باز کردن تنگه هرمز و رفع محاصره دریایی آمریکا متمرکز است
🔴
با یادداشت تفاهمی به توافق رسیدیم که جنگ را متوقف کند و تنگه هرمز را بازگشایی کند
🔴
این توافق به جنگ در همه جبهه ها پایان می دهد
🔴
توافق پرونده هسته ای را به مرحله بعدی موکول می کند
🔴
در این توافقنامه آزادی کشتیرانی در تنگه هرمز بدون اعمال هزینه های ترانزیت قید شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/alonews/122199" target="_blank">📅 01:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122198">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
دلار 163000
🔽
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/alonews/122198" target="_blank">📅 01:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122197">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
منابع موثق به المیادین:
🔴
آنچه پیشنهاد می شود یک توافق نهایی نیست، بلکه یک یادداشت تفاهم است.
🔴
این یادداشت تفاهم شامل هیچ بند مرتبط با پرونده هسته ای ایران نمی شود.
🔴
این یادداشت بر پایان جنگ و ترتیبات آتش بس متمرکز است. این تفاهم نامه شامل تسهیل دریانوردی در تنگه هرمز است.
🔴
این تفاهم نامه شامل خروج ناوگان آمریکایی از مجاورت ایران است.
🔴
این تفاهم نامه شامل آزادسازی نیمی از وجوه مسدود شده ایران است که بالغ بر 12 میلیارد دلار است.
🔴
این یادداشت شامل پایان محاصره نظامی دریایی ایالات متحده است. مهلت 30 روزه برای دستیابی به توافق هسته ای پس از امضای چارچوب توافق داده شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/alonews/122197" target="_blank">📅 01:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122196">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
خبرگزاری معتبر فارس: تنگه هرمز تحت کنترل ایران باقی میمونه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/alonews/122196" target="_blank">📅 00:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122195">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
منبعی در وزارت خارجه پاکستان به «العربی الجدید»:
توافق موقت خواهد بود نه نهایی، و پیشنهاد شامل گشایش تنگه هرمز و رفع محاصره بنادر ایران است.
🔴
پیشنهاد شامل رفع محدودیت‌ها از دارایی‌های مسدود شده ایران است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/alonews/122195" target="_blank">📅 00:53 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122194">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">کانفیگ فروشا
👍</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/122194" target="_blank">📅 00:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122193">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-poll">
<h4>📊 تا اینجا کی برده؟</h4>
<ul>
<li>✓ جمهوری اسلامی</li>
<li>✓ ترامپ</li>
</ul>
</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/alonews/122193" target="_blank">📅 00:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122192">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
علی هاشم خبرنگار الجزیره: طبق گفته منابع من، پیش‌نویس پیشنهادی که قرار است نهایی شود شامل موارد زیر است:
🔴
پایان جنگ در همه جبهه‌ها از جمله لبنان
🔴
آزاد شدن میلیاردها دلار از دارایی‌های مسدود شده ایران
🔴
لغو محاصره دریایی آمریکا و گشایش تنگه هرمز
🔴
خروج نیروهای آمریکایی از مجاورت بلافصل ایران
🔴
پس از این، طرفین ۳۰ روز فرصت خواهند داشت تا درباره مسئله هسته‌ای به توافق برسند.
🔴
این ۳۰ روز با توافق طرفین قابل تمدید است.
🔴
در طول این سی روز، عبور و مرور از طریق تنگه تسهیل خواهد شد.
🔴
به گفته ایران، مدیریت تنگه هرمز موضوعی ایرانی-عمانی خواهد بود و در حال مذاکره با مسقط است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/alonews/122192" target="_blank">📅 00:43 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122191">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_Q1LC1N1ldeGob-ovp9fDkMUpnjfNoNmPX50VOoWT0RyeEyZ7gPnvVLMBjI4Hc7y8Ae4IoPMszNmsthQZi5F5y1F5gpMce4E4MuMukHZefYs5-ZrvW0msIKDF828LREnWHLUQzoyhHCVgGOJJBajvPcFzJbAnzy3HLHmFj6Qw41I3r0Vl-iQe0MBLepH-3u4VIawlQ23z51gGegZE9j2TlH0BXbpx2X6BG5txRZ9T7S33XCQfVCiIqktVBT7raK0ZW6mVzwo6XH-WClePjqyPGWboFTjUORrzXvxYS4teiQhRZ1blJ7W5FF0hFbu8Y9dinYTwOwtttOGkF6EvFiPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
معاون اول ترامپ، بعد جلسه درباره ایران کاخ سفید رو ترک کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/alonews/122191" target="_blank">📅 00:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122190">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">املاکی از تسلیم بی قید و شرط رسید به تنگه هرمز به زودی باز میشه
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/alonews/122190" target="_blank">📅 00:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122189">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39125570ad.mp4?token=SON1vYt_R1du4pC6Eh0DJMvwvIWKyw-V64CDnikoZGIK--_HTfgVmsFsXgQGUfYcZj1uBIkRn2yjGuS0iyvzGbmqJBb5WP0GxUgqqZwgDfNAuSBsHAXJ6SVqklX4QR3lO7uT9wq8XtGhyCovVU3k1MuvSdF4OSWYkE9_4SGh-58fxTX-84R_QudVb4McSy4L4B659Hb5Y8_LrsKxSWpDl-vePG8BxbAW0QCagycwmxp0lonDVGLu_wxBSv9nXUTCpB5eMXBe0BoccUhcnMhpdukMc5v5MQ8m6ql1pgn7UvNAMb0qPecQskqdChUSGgWjsWn-U9HUpZmUbEE3S8Ql8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39125570ad.mp4?token=SON1vYt_R1du4pC6Eh0DJMvwvIWKyw-V64CDnikoZGIK--_HTfgVmsFsXgQGUfYcZj1uBIkRn2yjGuS0iyvzGbmqJBb5WP0GxUgqqZwgDfNAuSBsHAXJ6SVqklX4QR3lO7uT9wq8XtGhyCovVU3k1MuvSdF4OSWYkE9_4SGh-58fxTX-84R_QudVb4McSy4L4B659Hb5Y8_LrsKxSWpDl-vePG8BxbAW0QCagycwmxp0lonDVGLu_wxBSv9nXUTCpB5eMXBe0BoccUhcnMhpdukMc5v5MQ8m6ql1pgn7UvNAMb0qPecQskqdChUSGgWjsWn-U9HUpZmUbEE3S8Ql8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چه احساسی دارید؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/alonews/122189" target="_blank">📅 00:27 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122188">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
مارک لوین:
«تاریخ نشون داده که بهترین زمان برای صلح، بعد از شکست یا تسلیم دشمنه.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/122188" target="_blank">📅 00:24 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122187">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YayGoaGvaCeAhiT1Qdy37BNCRSahHVVQHC7uaVXwQEpqQ8wyDlBJwepYR4WU6e3_wgZpdCZiGzi-I6gPSudWFOgA2p2xKI9XlLTAb9E3NUSQU_VjAa1bCAiO-JNY3PwunP-IdWsK1lmEHDbpzeT3q0I7ZZNmtelZwiSaicsXxbvoFW3x7fMxlMdvpAr7Qs_DLuKA7-BIsNpS4YE7zg_bBm2t0lYiU_KSq9Pty-FrVnFsV-RJdwFKbKx3Qf2wn0xtJ4KaqaJb4q4Ogn1B07YQoarOLOCrRw64s8BekzFk7wsApcYdJ4sJDWUJGsn22XEwUhYBpr36n70UT5z18KwMEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی
:
تنگه اگه باز بشه جواب اون مردمی که ۸۰روز اومدن تو خیابون رو کی میخواد بده؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/alonews/122187" target="_blank">📅 00:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122186">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
تتر هم اکنون به 169000تومان رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/alonews/122186" target="_blank">📅 00:18 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122185">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
هم اکنون ریزش شدید دلار و طلا
🔴
تتر 171000
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/alonews/122185" target="_blank">📅 00:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122184">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
طی اتفاقی جالب بازهم پمپ بنزین‌ها شلوغ شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/alonews/122184" target="_blank">📅 00:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122183">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ترامپ: رژیم ایران را کاملا عوض کردیم
پ.ن:
😂
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/alonews/122183" target="_blank">📅 00:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122182">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
بزودی ۳۰روز مذاکرات هسته‌ای با قابلیت تمدید تا ۶۰روز آغاز خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/122182" target="_blank">📅 00:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122181">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
فوری و رسمی/تنگه هرمز باز میشه و جنگ تمام شد
🔴
مذاکرات بر سر پرونده هسته‌ای و مسائل دیگر بزودی آغاز خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/alonews/122181" target="_blank">📅 00:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122180">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
فوووری/ ترامپ هم اکنون اعلام کرد که پیش‌نویس تفاهم‌نامه‌ای با ایران تا حد زیادی مذاکره شده، در حال نهایی شدن است و به زودی اعلام خواهد شد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/122180" target="_blank">📅 00:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122179">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqMhZWvM1-b8gF3mX-UJNLXbXUdiLPZvUrBaKJpEEuVwgNIIAZc6X7KbxRWqYQejZdC3urflNl51FqF21Jm8pMYrhBTlFlvmasqONDe2JpIDk1CwPvvGGEIK7k_4la5geMufvjPlTpI_S4xhjLZpKN9ImjdyLHwoazepKj_peOXexQ4MnSA9ZIhcUA5V_YwnfKbMCeBqhgwMWeR7WUMgUCNqJPSo63XhVxuyZpLyP_SDEPR1RvLetsBf4eXIBJYsR2oRyoiv7msObZvIBXvp4MCkOB5w7Ww9WEKeGfr1er3eH45O6jiWqJMRprEXFw0ENso6iPTDqEaoebqoYAK2Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوووری/ ترامپ هم اکنون اعلام کرد که پیش‌نویس تفاهم‌نامه‌ای با ایران تا حد زیادی مذاکره شده، در حال نهایی شدن است و به زودی اعلام خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/alonews/122179" target="_blank">📅 00:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122178">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
کنسول جمهوری آذربایجان در تبریز بر اثر تصادف در اتوبان جلفا-تبریز جان باخت.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/alonews/122178" target="_blank">📅 00:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122177">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">💢
فوری/پرواز جنگنده‌های آمریکایی در مرز ایران
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/122177" target="_blank">📅 00:03 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122176">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOGsliKj4QrR43LX-wIH_FIW4AI6bvESybaigeOBKF4xvnQQw6cvzGB8J7ZA2UrHQRQdOgch-Qy3qKnzKrQlDKvTFhrUyM1Ie7-WP229lv7FtSsB4bIo-Zna1ywtzaJ_UtLxptn_JQX7-4nDHmm7FjoDB49DMB3zEz4PuKHJzZw8sd8pCWZdN8u3HstL_uIZG3cCcsuNni_3cGrxPDNa_HA5x4rWJyirJCrcHXkCFMPPPmW53mh0O3k0uz3Ky42cIuTvfik-znuieF1LCI9ohXq4jItP2ZPIYRTYIdqsnHFv1unot8-rjoiIZ3LXBUW6pYwMqSbqUanOihmsmf6MYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت دوباره اتاق جنگ اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/122176" target="_blank">📅 00:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122175">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
پرزيدنت ترامپ از اردوغان تشکر کرد که او را رهبر جهان قرن‌ها منتظر خوانده است.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/alonews/122175" target="_blank">📅 23:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122174">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
یک منبع منطقه‌ای به Axios گفت که رهبران عرب و مسلمان شرکت‌کننده در تماس امروز با رئیس‌جمهور ترامپ به‌طور یک‌صدا از او خواستند که برای پایان دادن به جنگ و کاهش تنش‌ها در سراسر منطقه، به پیش برود.
🔴
«پیام همه این بود: لطفاً به خاطر منافع کل منطقه جنگ را متوقف کنید»، منبع گفت.
🔴
مذاکرات به‌طور مثبت پیش می‌رود و میانجی‌ها امیدوارند تا فردا یک توافق چارچوب یک‌صفحه‌ای را نهایی و اعلام کنند و سپس چند روز بعد مذاکرات درباره توافقی دقیق‌تر را آغاز کنند.
🔴
در حالی که پاکستان رهبری تلاش‌های میانجی‌گری را بر عهده داشته است، حمایت قطر در هفته گذشته همراه با فشار عربستان سعودی، مصر و ترکیه به کاهش اختلافات بین طرف‌ها کمک کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/122174" target="_blank">📅 23:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122173">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
فوری/باراک راوید از اکسیوس: امیدواریم فردا یک توافق چارچوبی بین ایران و آمریکا اعلام کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/122173" target="_blank">📅 23:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122172">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
فوری / هاآرتص به نقل از منابع اسرائیلی: رهبری سیاسی اسرائیل معتقد است ترامپ توافق را بر بازگشت به جنگ ترجیح می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/alonews/122172" target="_blank">📅 23:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122171">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ej7IyCbp8n85FSHntqJ8y-gaMFF2goqfw0ELqo3zGn2Ehn3GPg-NPdAEvhecCfA2pBgSBMag5a3F4H_omak5a8ojaGx9Z9sOyHFAScx6A7F--GaIAINv0RadFqkCNsjJza1FY81aycT7_ZbHUw5vwgg1DYH09p1b3d3jAvQzmFI_awJMEgh2sgHWdGkGFMId1q8mvLam8AhmFQfM9IslBJv4YyW0e9mvFMog9gnhN__1nm5znkZ7zoCor2i6u1adqhVYvy1nHISXjHUPrNarsqJzxueSLGjRukm1-WB1_RgVFLo8iwXUKx_kMllcMQ7hLZ6WNswxHPhzCMg_89PWsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فایننشال تایمز: آمریکا به ژاپن درباره تأخیرهای شدید در تحویل موشک‌های تاماهاوک به دلیل جنگ با ایران هشدار داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/alonews/122171" target="_blank">📅 23:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122170">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de621e16c4.mp4?token=HwaUBGLp3s6rWCgF69Z4Ugp_-_NjYggIo2C97wXJsV7d3eDf2N5T-BeHEf9tQNg_NqY5aS3LU2j9s-G9GmbfVNTR0DIrujqAlMBTjcTSYIjWSo6va9GjqYH9TQ5AUZ3NrjgRHm59ArcThV4upad3feQCK6Rm9e7l55XFPOarIIfEHs0qJaYVSApRuBgmgd8JQ7-aT3PrRN__o1LlALF9dxHcsYBEHFMYoZEpM8F6PEJciXSscekTEmkqqlNXz-vcPaOo6hHp6g47f4LVIA-9lqADrpp5-MHNGDWlBCk5iyFn3I3WrDopG4sl40REu3JWwqG6Nwt3qqAceiF28HXVcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de621e16c4.mp4?token=HwaUBGLp3s6rWCgF69Z4Ugp_-_NjYggIo2C97wXJsV7d3eDf2N5T-BeHEf9tQNg_NqY5aS3LU2j9s-G9GmbfVNTR0DIrujqAlMBTjcTSYIjWSo6va9GjqYH9TQ5AUZ3NrjgRHm59ArcThV4upad3feQCK6Rm9e7l55XFPOarIIfEHs0qJaYVSApRuBgmgd8JQ7-aT3PrRN__o1LlALF9dxHcsYBEHFMYoZEpM8F6PEJciXSscekTEmkqqlNXz-vcPaOo6hHp6g47f4LVIA-9lqADrpp5-MHNGDWlBCk5iyFn3I3WrDopG4sl40REu3JWwqG6Nwt3qqAceiF28HXVcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جلسه روزمرگی سران نظام
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/alonews/122170" target="_blank">📅 23:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122169">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از یک منبع اسرائیلی گزارش داد: نتانیاهو در تمام طول شب شنبه با مقامات آمریکایی در تماس بوده و انتظار می‌رود به زودی با ترامپ نیز صحبت کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/alonews/122169" target="_blank">📅 23:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122168">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
نیویورک تایمز: مقام‌های ایران و آمریکا از پیشرفت در مذاکرات خبر می‌دهند، در حالی که سرنوشت آتش‌بس همچنان در هاله‌ای از ابهام قرار دارد
🔴
در شرایطی که مردم سراسر خاورمیانه خود را برای احتمال ازسرگیری درگیری‌ها آماده می‌کنند، مقام‌های دو طرف اعلام کرده‌اند نشانه‌هایی از پیشرفت و حرکت به سوی یک توافق دیده می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/122168" target="_blank">📅 23:36 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122165">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f9b1335f6.mp4?token=hElE_yAUAMTgNFYpB85ChnP4mdQHsiQZm7n-w-AyhlStt_oX_E1vxrAJucNIJDnFc7eFECAtgInB0chQlpFML1ENgMDgMICshYicYRLfqw9Wi1_vmfLF8jYTIvrewnWgY2MXI8sdooigtTNTYRV1M3lBsh5SQGjzQU77biLIls-YS3UHSojzzIx4_vBIgXqocVtL2VkzmopryLD11LQceJcIZSEJjszeW1K0CiTCT4QkErUsuNvY8G2wcIVVwHKEWenIRkgHsPbdEH0HyDdIbx-t2-mkkbcuc0mXylzWnW_dB5JhEzqw1bL54e1Ygwj304naPcp_9pHJn7PKKWVe_30Uswe71d8NImxGsfaeucHDTs-DOFu7wCujoXjoa3Lvsl_6BHQ7IXLlkVOh978wVfe4HMar4U8AGsEbhdpsLZ74wqBZFDxSTjCPjTur-2xlTyaGpKtHDvMziNrfWjUX2pyYDMhL1vPp8SXM2QdFP43NcUzPgEr_LIsaGGRrJIxE6BFl6Ll0ngCyQT6O0tVaMlnS70g65IYs1FSJU9Hxj3agAoYNxf9gkeTCjdLQCEODClgom5n1kPdf39sD9ASY9vLdmdsLnDslAhoGOUcEMRrz4sAJa73vSEo_TtxLWlE63QHKvdyuSRobZzbiLc8HNWPVapj29fGODnRtqsmv2Yc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f9b1335f6.mp4?token=hElE_yAUAMTgNFYpB85ChnP4mdQHsiQZm7n-w-AyhlStt_oX_E1vxrAJucNIJDnFc7eFECAtgInB0chQlpFML1ENgMDgMICshYicYRLfqw9Wi1_vmfLF8jYTIvrewnWgY2MXI8sdooigtTNTYRV1M3lBsh5SQGjzQU77biLIls-YS3UHSojzzIx4_vBIgXqocVtL2VkzmopryLD11LQceJcIZSEJjszeW1K0CiTCT4QkErUsuNvY8G2wcIVVwHKEWenIRkgHsPbdEH0HyDdIbx-t2-mkkbcuc0mXylzWnW_dB5JhEzqw1bL54e1Ygwj304naPcp_9pHJn7PKKWVe_30Uswe71d8NImxGsfaeucHDTs-DOFu7wCujoXjoa3Lvsl_6BHQ7IXLlkVOh978wVfe4HMar4U8AGsEbhdpsLZ74wqBZFDxSTjCPjTur-2xlTyaGpKtHDvMziNrfWjUX2pyYDMhL1vPp8SXM2QdFP43NcUzPgEr_LIsaGGRrJIxE6BFl6Ll0ngCyQT6O0tVaMlnS70g65IYs1FSJU9Hxj3agAoYNxf9gkeTCjdLQCEODClgom5n1kPdf39sD9ASY9vLdmdsLnDslAhoGOUcEMRrz4sAJa73vSEo_TtxLWlE63QHKvdyuSRobZzbiLc8HNWPVapj29fGODnRtqsmv2Yc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپادهای FPV حزب‌الله به حملات خود به تجهیزات ارتش اسرائیل در جنوب لبنان ادامه می‌دهند: ویدئوی اول: یک پهپاد FPV به یک خودروی HEMTT ارتش اسرائیل در سایت خربت المناره واقع در مرز جنوبی لبنان حمله می‌کند (۵ مه)
🔴
ویدئوی دوم: یک پهپاد FPV به یک بیل مکانیکی ارتش اسرائیل در خیام حمله می‌کند (۱۵ مه)
🔴
ویدئوی سوم: یک پهپاد FPV به یک خودروی زرهی نامر ارتش اسرائیل در طیبه حمله می‌کند (۱۶ مه)
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/alonews/122165" target="_blank">📅 23:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122164">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
معاون رئیس‌جمهور جی‌دی ونس، وزیر جنگ هگست، رئیس ستاد مشترک کین و کل شورای امنیت ملی توسط رئیس‌جمهور ترامپ به اتاق وضعیت کاخ سفید برای گفتگو درباره ایران احضار شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/122164" target="_blank">📅 23:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122163">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNJpjZAvNul2YmcoEuIMW2kyhzInB02_xHI5ih_yWbxjED-FI0p7KfUCTuIF0F9GILKcaCwBoDh0OQzOF3f2ikAuKyxxMygbamy8a2iRmivMBmv6ZDXgdxmRexKkIIHJVoeRSva0SynQa24MrVXwErq7i_XGOAYS_XH7P64c__7IZ-qNicx1OshSKNVwe0VpiX_Ee0CdR2bSWWnff6aogp_Lo8BrkCiSGmODYOKnhtlBN6R5N7aPnI45fFcqtEAUjzH9xeDOHLwlEuot0ioN0OuFYYZr8nUiMagyMa48W9QUlF15mAjkZBsP9wU3abOv0PV4TiZtVGIuDdLFCWapaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استثنایی گیگی
9️⃣
8️⃣
1️⃣
تحویل زیر یک دقیقه
✅
دارای لینک سابسکریشن جهت دیدن حجم و کنترل مصرف
✅
بدون قطعی
✅
بدون محدودیت کاربر و زمان
✅
جمینایو چت جی بی تی و... کامل اوکیه با سرورامون
✅
🏪
پشتیبانی کامل
✅
شروع فعالیت از سال 2022
✅
پرداخت ریالی
✅
ضریب و این چیزا ندارن و تا آخرین مگابایت برای پشتیبانیش درختمتیم
🥂
💤
این تخفیف فقط تا ۱۲ شب فعاله
💤
⭐️
@Napsternetiran_bot
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🔶
@Napsternetvirani</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/122163" target="_blank">📅 23:19 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122162">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
کانال عبری کان: «ساعت‌های حساس: در اسرائیل منتظرند ببینند آیا تلاش‌های دیپلماتیک فشرده، به ویژه از سوی پاکستان و قطر، به امضای یادداشت تفاهم بین ایران و ایالات متحده منجر خواهد شد یا نه.
🔴
این در حالی است که نخست‌وزیر بنیامین نتانیاهو به سمت ازسرگیری جنگ و حملات علیه ایران فشار آورده است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/alonews/122162" target="_blank">📅 23:19 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122161">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJgNq2aEtUlSO6i0Y3PQ9Ely3eMCa5NMtrRjsKUPe30eU1Pd7uZqoGXLPUJ7ItqeBJVKKT0pv9Of3SWTkLJaUV5L4GHsc1zGN0ZWQZ1_xZcHD1J91Afk_ko5MF2QdwHmz_2opvDhHPAabx4PP7ZFpZTTtYhqk3ezFbgwpIeFtSXmQwFEEkFxg1joJPFwXxJ7L3VKFnJr2Z7MSOvUjIKoEvS7mfTi7e_0nYY5MIk24UIFAkkESr504MobWnoHsNgoiLQr8HFRXFsGqKDrHUyCsXjMKK0wvgggzNAJBdSbRdEDaUUyKHoXBzvaOnJPBS8G5ZFEQKCMyvap4ram6c5lxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فاکس نیوز:
«
شما نوک نیزه خواهید بود.»
🔴
ارتش اکنون چهار ماه زودتر از برنامه به هدف استخدامی خود در سال ۲۰۲۶ رسیده است، طبق گفته پیت هگست، وزیر جنگ.
🔴
هگستث در سخنرانی فارغ‌التحصیلی در وست پوینت اعلام کرد که ارتش چهار ماه زودتر به این نقطه عطف رسیده و گفت که این نیرو در حال آماده‌سازی برای جذب ۶۱,۵۰۰ سرباز جدید است.
🔴
این اعلامیه در حالی صورت می‌گیرد که پنتاگون با تنش‌های فزاینده جهانی و تمرکز مجدد بر آمادگی نظامی روبرو است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/alonews/122161" target="_blank">📅 23:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122160">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
کنسول جمهوری آذربایجان در تبریز بر اثر تصادف در اتوبان جلفا-تبریز جان باخت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/alonews/122160" target="_blank">📅 23:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122159">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
خبرنگار لبنانی در شبکه سه: حزب‌الله بر روی نابودکردن گنبد آهنین اسرائیل تمرکز کرده است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/alonews/122159" target="_blank">📅 23:06 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122158">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
ادعای رویترز درباره چارچوب سه مرحله‌ای برای مذاکرات آمریکا و ایران
🔴
پایان رسمی جنگ، حل و فصل بن‌بست تنگه هرمز و باز کردن پنجره مذاکره ۳۰ روزه برای توافقی گسترده‌تر. امکان تمدید نیز وجود دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/alonews/122158" target="_blank">📅 22:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122157">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/54163ee186.mp4?token=RWtB61MH9K9h8mc-r8p9j6TV7yZtN_i1cRZ20958lxYcldFFJxmPvy5-i0eaGpLnoIHzIegVUQriEOzfzAgw1uN4qvO7bT46s9HdDjPlwfucpIUDoNpdX9cm0wEXVIlMw_O2zOW2jc90c76gEre7ZUxqWHCtunM-nj7KdBVR91l0mjpc4CicwC-RSY9Bd0UcIpiGMls3EplRLUViujC8ExmEe9Gy-s-VD-eqpurhsfq5TeclP-TLvp9N5BLdhW_VzxldPq01aB4uozemuzkbX7Q7FkJJR0ApOq0NQejCqDoCfDqgxbp0IODrxLm89sN8H7WnHlF_eo5wgI6t24V3og" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/54163ee186.mp4?token=RWtB61MH9K9h8mc-r8p9j6TV7yZtN_i1cRZ20958lxYcldFFJxmPvy5-i0eaGpLnoIHzIegVUQriEOzfzAgw1uN4qvO7bT46s9HdDjPlwfucpIUDoNpdX9cm0wEXVIlMw_O2zOW2jc90c76gEre7ZUxqWHCtunM-nj7KdBVR91l0mjpc4CicwC-RSY9Bd0UcIpiGMls3EplRLUViujC8ExmEe9Gy-s-VD-eqpurhsfq5TeclP-TLvp9N5BLdhW_VzxldPq01aB4uozemuzkbX7Q7FkJJR0ApOq0NQejCqDoCfDqgxbp0IODrxLm89sN8H7WnHlF_eo5wgI6t24V3og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی از حمله پهپادی ایرانی به حزب آزادی کردستان (پاک) در استان اربیل، شمال عراق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/alonews/122157" target="_blank">📅 22:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122156">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc07220ddc.mp4?token=iDfY3gQry3E-QAkiUyyb5tD21CU5SYqv3GmynTqF6q4durMIKDUO4ujyINTFydkgmQCzSIxdCXQhSN2_I9S7a7aa2aiCv0ho6-oNbIsp_DSY7kGxZTYhAL_cedakN332CCEX1ACtf_W8YOGzqUxSQxaujHiH-OVYfm1w6En2SHIESxnkmx-LK5C09766Ou1Ga73xVAbqkGQAXGxcp8JMhVQABF4TuQAG_DMn1xyLlXB34sSGG2hOZ8Yj8cvHmcu2EPzuW39L3f_yTKCtbNBMTb0FYsZzXV-Nzo7TMektH8HxXOPrjl3EGtZIev8yKCp1LMTH1wUdCgUJW_JdqCLA3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc07220ddc.mp4?token=iDfY3gQry3E-QAkiUyyb5tD21CU5SYqv3GmynTqF6q4durMIKDUO4ujyINTFydkgmQCzSIxdCXQhSN2_I9S7a7aa2aiCv0ho6-oNbIsp_DSY7kGxZTYhAL_cedakN332CCEX1ACtf_W8YOGzqUxSQxaujHiH-OVYfm1w6En2SHIESxnkmx-LK5C09766Ou1Ga73xVAbqkGQAXGxcp8JMhVQABF4TuQAG_DMn1xyLlXB34sSGG2hOZ8Yj8cvHmcu2EPzuW39L3f_yTKCtbNBMTb0FYsZzXV-Nzo7TMektH8HxXOPrjl3EGtZIev8yKCp1LMTH1wUdCgUJW_JdqCLA3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپادهای ایران مواضع گروه های جدایی طلب در کردستان عراق را هدف قرار دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/122156" target="_blank">📅 22:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122155">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
مکرون در تماس با ترامپ و سران خلیج فارس، خواستار راهکار دیپلماتیک و توافق با ایران شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/alonews/122155" target="_blank">📅 22:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122154">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در اربیل عراق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/alonews/122154" target="_blank">📅 22:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122153">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4943cd2a90.mp4?token=PWr_BoxfMlmM6ypMNIaiDsnGH0dWWsXpikt_CmOSYQ5cx1YgVoxA8IsBZEBzC9v8-jav7QHMMbz_MXDhuJBE8c4Tsqv04A5HkzQIE5LFsnxQWaJfh82Sf5mx16ECFmI7QB9wEOL-ACaux0i_1T9WpnB8rF03YXYhgaW9e9uyEXgIV3LwpoVPgztmIWnlzU6i3dy0LUG2vTg-6u7bVLKDhl7Xmf6iUx8X1Ssm8OueRkhA1yjOEGUKS26pa1-29Z6oowQOEXkp88NJ5tjY4xZFs27zbu-f4aqz5T_dpdTXj2RtNqHfxq77O3bg1pIAG4czAUWYth03oAvCsWozZF86rT1usl-xtEF3YySe2AAMDbl46HIH3o3Okd5pBfjH-n96j-00pK5An0B7ttZ6BZNnKxT23GwVvaFJ5jO3aSEd_zNOffuBxI-7AfxKvplfd2F0Bu_kuhdGc8ZsLs6pPK9stjkr2nknSKT-SGipuaQl5l9YKMERKMMO0ZjbSctE-CIva6zJ1GMbiwdcbTdESh31iE2aq3fcKUPIHXeXYSVAIfLEdV9jbO8c6YWPDrbl_Ib7WSstVVRyIeqQ4WuaoTUoKo0LaSAFff69V-nRibSWsX8kflkJC232985CF6zorEirwpaf-V6PC0eby9rGFn3KAlm-e7WJUWiLBsqYlix1bkY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4943cd2a90.mp4?token=PWr_BoxfMlmM6ypMNIaiDsnGH0dWWsXpikt_CmOSYQ5cx1YgVoxA8IsBZEBzC9v8-jav7QHMMbz_MXDhuJBE8c4Tsqv04A5HkzQIE5LFsnxQWaJfh82Sf5mx16ECFmI7QB9wEOL-ACaux0i_1T9WpnB8rF03YXYhgaW9e9uyEXgIV3LwpoVPgztmIWnlzU6i3dy0LUG2vTg-6u7bVLKDhl7Xmf6iUx8X1Ssm8OueRkhA1yjOEGUKS26pa1-29Z6oowQOEXkp88NJ5tjY4xZFs27zbu-f4aqz5T_dpdTXj2RtNqHfxq77O3bg1pIAG4czAUWYth03oAvCsWozZF86rT1usl-xtEF3YySe2AAMDbl46HIH3o3Okd5pBfjH-n96j-00pK5An0B7ttZ6BZNnKxT23GwVvaFJ5jO3aSEd_zNOffuBxI-7AfxKvplfd2F0Bu_kuhdGc8ZsLs6pPK9stjkr2nknSKT-SGipuaQl5l9YKMERKMMO0ZjbSctE-CIva6zJ1GMbiwdcbTdESh31iE2aq3fcKUPIHXeXYSVAIfLEdV9jbO8c6YWPDrbl_Ib7WSstVVRyIeqQ4WuaoTUoKo0LaSAFff69V-nRibSWsX8kflkJC232985CF6zorEirwpaf-V6PC0eby9rGFn3KAlm-e7WJUWiLBsqYlix1bkY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خضریان، عضو کمیسیون امنیت ملی مجلس:
در هر توافقی ایران حتما باید غرامت جنگ را دریافت کند/ مطالبه ملت ایران است که از مدیریت تنگه هرمز عقب‌نشینی نشود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/alonews/122153" target="_blank">📅 22:34 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122152">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
یک دیپلمات منطقه‌ای به فاکس نیوز:
«تماس سران عرب و ترامپ بسیار مثبت بود. پیشرفت خوبی در حال انجام است. رهبران منطقه از این پیشرفت که ترامپ با مذاکرات به دست آورد، حمایت کردند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/122152" target="_blank">📅 22:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122151">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
فوری / هم اکنون جلسه اضطراری امنیت ملی دولت ترامپ در اتاق جنگ کاخ سفید در حال برگزاری است.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/alonews/122151" target="_blank">📅 22:30 · 02 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
