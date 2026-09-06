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
<img src="https://cdn4.telesco.pe/file/bUxLiqYNY9FWnBSm-5mTiVe4_uNrypgL_JLB5ixY64XXOTAWwwrtEer0V5mqWce5Tud9nH2FMsHRRVWnbGOnGLO2JD5B-rEVkLQjfRNkVQHLeSZP9U-KPQFnDeJ46nTo9vUmgbZU2EaprMTLl5C5bWyFXSeYoVUM4R_DqA9mp5Y2YvrMLrGgYG8TRw_Yb1ab4xG4Mw3cRScsNzE5JqisvGmQeizDmxHLc_UW71-FiOINcMxiyVXGU3frgEbB6ppb00pF0fDix2k9GG-lUkdlJJWZH7yZZUVMBEV6COe4Z63Sn41dWhf5ZoIH_HEtc_wGkmKw_QMSlRhK6mwmVQIMfw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 936K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-15 12:33:46</div>
<hr>

<div class="tg-post" id="msg-145863">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
قالیباف: نوسانات شدید قیمت ارز، تورم، بیکاری و مدیریت بازار، چالش‌های اساسی هستند که به معیشتِ مردم فشار جدی وارد کرده و در سالی که توسط رهبر معظم انقلاب با عنوان «اقتصاد مقاومتی  در سایه‌ی  وحدت ملّی و امنیّت ملّی» نام گذاری شده،  باید با تکیه برتولید داخلی و استفاده ازظرفیتهای فناورانه‌ی نخبگان جوان، برای آن‌ها تدبیر  و راه‌حل کوتاه‌مدت و دائمی داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/alonews/145863" target="_blank">📅 12:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145862">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
قالیباف: آمریکایی‌ها حتماً فهمیده‌اند که دوران «پاسخ‌های متناسب» به پایان رسیده است/ هرگونه تجاوز به منافع و امنیت ایران، پاسخی «سریع‌تر،سنگین‌تر و دردناک‌تر» دریافت خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/alonews/145862" target="_blank">📅 12:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145861">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/630202ce50.mp4?token=NtiBiTqmKRDiZ3Do4SiqR3R7QMew9zjV6xl1zxoy26BpizDC5pTToXY-Ge-SyDNkg8yE1F7P9yQ_w2_8o5bLgNbZ56NLf3DZTOZLOL0g52QDc4jOqweLvcCnUPNxsm-oJyF_CH4tpGbjtcjJ-dSy1G6leimwDUbtdcZuD4ZvCoKbWlXGAPX8y6DEZgjXKXjWpu5pRI4Ihtn0VwC404n9rIEeRHfVenYis-8xuq_tnGiA5oncPj487Rgfxo9D89BhpWvhC8PbydGnHodpar9NShRTfMx2tMaxleCEwXvfX6dcL-iW9uFLs4ifAAOadd09kGBW3U0uiZyIEYPr6s9wBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/630202ce50.mp4?token=NtiBiTqmKRDiZ3Do4SiqR3R7QMew9zjV6xl1zxoy26BpizDC5pTToXY-Ge-SyDNkg8yE1F7P9yQ_w2_8o5bLgNbZ56NLf3DZTOZLOL0g52QDc4jOqweLvcCnUPNxsm-oJyF_CH4tpGbjtcjJ-dSy1G6leimwDUbtdcZuD4ZvCoKbWlXGAPX8y6DEZgjXKXjWpu5pRI4Ihtn0VwC404n9rIEeRHfVenYis-8xuq_tnGiA5oncPj487Rgfxo9D89BhpWvhC8PbydGnHodpar9NShRTfMx2tMaxleCEwXvfX6dcL-iW9uFLs4ifAAOadd09kGBW3U0uiZyIEYPr6s9wBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خوشحالی غیرقابل وصف یک آخوند از گرانی دلار و طلا در چهارراه ولیعصر تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/145861" target="_blank">📅 12:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145860">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frs3vC2AbGkfh1IbRVPnrDWob499rn83YvLCrnkmuLEPvCWqe7F9xUN4c7colfs41MG_keQbpTOm17XLVFYUZxHg8j2G67nSx8gHnvdaJDr4MwEb9oHPJ8xXq86YIJztFM1bW4SC7JNyqfJB5iMpp4hkXJHHVHz9E_kyZeFFDZRU16W4Cg2CwCtE2l-LGpgpHxpZtlpAqBE3OH1Wzog4jDCPNy1OQ2fNACh3fyKUYT4a2I8rM_cti5VulaiJjZCSHupSxOgnwRjzly2YtRARMW0r4e54Jw0mMhhTv6Fl6DO-jQ-yidU4uXongyVA-4JaVKGdU_4tu2leuNYGRggnJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع عربی: نفتکش «ولوس امبر» (Velos Amber) یک ماه پیش موفق شد بدون مجوز سپاه پاسداران وارد تنگه هرمز شود؛ هرچند در جریان این عبور هدف یک پرتابه نیز قرار گرفت.
🔴
این نفتکش اکنون در تنگه هرمز گرفتار شده و اجازه خروج به آن داده نمی‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/145860" target="_blank">📅 12:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145859">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
مشاور امنیتی نخست‌وزیر عراق در گفتگو با روداو اعلام کرد که ایالات متحده آمریکا تا پایان ماه سپتامبر، سامانه‌های دفاعی و نیروهای باقی‌مانده خود را از خاک عراق خارج می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/145859" target="_blank">📅 11:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145858">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-bDYxq0yAhGuCU4ikiw7jvF5_b0Vd5Zzp-ICiNS75O8Oik9hsZgPDyps2G10VoD1JZ_N8c-K8X2WoMjutr9ykZ2232VMThNTjbT8fC49walQdhg36ZDGc38VQO11BnKsRqRDlO-eG6Z0Rsb3mgO7BI6rc7yx5nPOdNYfWqvUiNYC3z50o_qUpclYCfFO9ZTR3mNZ-Xys2Gv4oeQGMyBtoVMUOVI464GQMEBH3bXZIYvWcELRUtRGx2AR-HupeQulWkeWrP4FjE_yXTsq5eiiTjnTH0Uau4Kk8YiHXISi4-LGBFLBBkEWT2O-tv9eoINtsGoZC6dyiKEb95VrKmcPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تجمع معلمان در اعتراض به وضعیت بد معیشتی
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/145858" target="_blank">📅 11:49 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145857">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
وزیر نیرو: تلاش می‌کنیم قطعی برق متوقف شود
🔴
با توجه به پایین‌ بودن میزان بارش‌ها از حد نرمال در برخی مناطق، مدیریت مصرف آب ضروری است.
🔴
شهر تهران تا حدودی با محدودیت منابع آب مواجه است.
🔴
امسال زمستان شرایط خاصی دارد.
🔴
در جریان جنگ آسیب‌هایی در حوزه سوخت، وارد شده که باید جبران شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/145857" target="_blank">📅 11:48 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145856">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
مدیر سابق سیا: آمریکا شاید نیمی از موشک‌های رهگیر خود را در جنگ علیه ایران استفاده کرده و اکنون خواستار تغییر به سمت پهپادهای ارزان قیمت شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/145856" target="_blank">📅 11:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145855">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uk05hlAtiV8e1uQ64Qh3g01cWOhidjOiv-l3dJIuye1nNLdTbgIKcQ-rmXt0atWk1J760Hr1PZmKukrot_l3T8maupjcJcAIOrkGMtMZI-Kr3cJdYO_D8PxnPKWKPMIsMNwn98V1Ub0G7VKqc1ofTI_vGLDme2ak31ifyhsTwy3-D2_xyFeGGOMJCoezgMWftFMWUVnT2CPNN2b4rj94RpXxZWLYxc_8yxMCm9BE7pFnZYMce08qWa8QLbi0rVmen5xT_RGxe3hD1hm0psJMhOk0g-fWVSb5YtoYQaVZuX3M5AJI6FFU9QpVFCL9SvaEk9Z4-oLZ67NpkKoPEYZjmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وقتی وزیر با وزارت هماهنگ نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/145855" target="_blank">📅 11:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145854">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
سخنگوی سپاه: هزینه محاصره اقتصادی برای آمریکا چندین برابر خسارتی است که به ایران وارد می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/145854" target="_blank">📅 11:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145853">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
هم تنگه هرمز تقریبا باز شده هم حزب الله ترکیده، فقط مردم بدبخت ایران زیر سیاست‌های علی الاصولی شما در حال نابودی هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/145853" target="_blank">📅 11:29 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145852">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل : تا زمان خلع سلاح حزب‌الله از منطقه امنیتی در لبنان خارج نخواهیم شد.
🔴
تسلط بر علی الطاهر به معنای تکمیل کنترل امنیتی بر جنوب لبنان است.
🔴
پیشروی نیروهای اسرائیلی به سمت «علی الطاهر» پس از دریافت اطلاعاتی مبنی‌بر وجود تونل‌های فرماندهی در این منطقه صورت گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/145852" target="_blank">📅 11:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145851">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8eeJnR8AXtOXzAGeGbag3G90V93vVyZlSLo8Rpr9SFsfC5O-MlAl5QcDYR_zGTZni2hWb6Bsrz-sWNyCnH0Rox3Imt_zJjBer2WVO7p8MwUVeabXpizaZKQQPL8rKf5qlCTfc5ZFikEuYBYgfzgj0O_vFKzXDtFGt5Alyga9li9n3KKIk61Iwn4qTh5yGIWGnitraTzyyCoRJZvYSlctm97VJGl2TL_4A_WKIz-QGFnHklh3XLKFsObqrCLAY32MQiFstSRlmKSXe-c1ZSnA6Rujsj-EvL8JfakPI1X8Lff4XPTboJWEDKYg1cr1IQy32Ll7MyIeZSx3JBG9urYjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاتس: تا خلع سلاح حزب‌الله از منطقه امنیتی لبنان خارج نمی‌شویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/145851" target="_blank">📅 11:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145850">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
مصر و پاکستان بر اهمیت بازگشت ایران و آمریکا به اجرای توافق موقتی که در ماه ژوئن گذشته میان مقامات این دو کشور امضا شد، تأکید کردند.
🔴
وزارت خارجه مصر امروز یکشنبه اعلام کرد بدر عبدالعاطی، وزیر خارجه مصر، و محمد اسحاق دار، وزیر خارجه پاکستان، در تماس تلفنی روز گذشته خود بر اهمیت بازگشت به اجرای توافق موقت برای پایان دادن به جنگی که ماه‌هاست در منطقه ادامه دارد، تأکید کردند.
🔴
دو وزیر همچنین درباره تلاش‌های انجام‌شده برای مهار تنش‌ها و بازگرداندن آرامش گفت‌وگو کردند و بر اهمیت ازسرگیری اجرای «تفاهم‌نامه اسلام‌آباد» که در 18 ژوئن گذشته میان آمریکا و ایران امضا شده بود، تأکید کردند. آنها همچنین بر ضرورت دستیابی به توافقی جامع و پایدار تأکید کردند؛ توافقی که امنیت و ثبات منطقه‌ای را تقویت کرده و مانع گسترش دامنه درگیری در منطقه شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/145850" target="_blank">📅 11:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145849">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
مدنی‌زاده، وزیر اقتصاد: ما اقتصاد ایران رو برای زندگی مردم اداره می‌کنیم، نه برای رضایت آمریکا
🔴
ملت ایران هزینه داده، اما هرگز تسلیم نمی‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/145849" target="_blank">📅 11:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145848">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
وزیر نفت عراق اعلام کرد که عراق ظرفیت صادرات نفت خود را به بیش از سه میلیون بشکه در روز افزایش داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/145848" target="_blank">📅 11:21 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145847">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPExhoD7dkEpdPaw0nc1e6az51OIxmFe0AOgRbVqf-mfMnMqs_vMM5siLOPRiCg27q2ks_v4MzdwvhNODwAOFo8nGbKszNWL6ChaYAUW9sJksF4DhX8ndKZPanRMd012sDolV9AeADq2kn97zTZ-2ArDLhSI4tnB5YJ97WPkzTk5tdyUb6ZMIf5aQoKHiZS7c9nDqM1hRuoCB2A79z8nhIXcu4kCh856ZP7VEy6O5Ls82H3ZM4PrGpwY-TqleqnDLrBWf9Q0qNdJQFfVor8yWfTvJ7NDNl4Z2U5GQ1gkiftTrwzh0EteKjVn-s9x3X2Kdv-mHIpyq3OsDyqewojsTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان : حادثه تلخ انفجار تانکر سوخت در محور سنندج- همدان و جان‌باختن شماری از هم‌وطنان عزیزمان موجب اندوه عمیق شد.
🔴
ضمن تسلیت به خانواده‌های داغدار و مردم کردستان، مسئولان مربوط باید رسیدگی فوری به مصدومان، حمایت از خانواده‌ها و بررسی دقیق علل حادثه را در اولویت قرار دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/145847" target="_blank">📅 11:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145846">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/500dcdb1b1.mp4?token=rvtkANNoKKRIXKeDCjeEGCOkNENV_X1mRJz9aeOKY_sAO-Yb8mH6dyqddsimto8nbw38mLNdWe0MjXUh9I-ZJidAVF3g74KCrIL3ap6MGMLGNVDxWA2_Kdx0vlatsnPInVz6B5REg-u9tclano4WzENg3fI7FhcAm_hC67_WZTm7-4nrrlXRvYQebaxb2CzoopqncWOotC7tsD4dsfp3ldMo07-5wTC00407d_jjMGeCkVulctogzzekm9CMXmNtApgGvF8Sre5NLyEKtcnhqHS6uGu8HquWR5Y-W9SmBKKA6ClZjYkJBslh_GAqDnaJV7oXt9MTm2qev9TzfVaHcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/500dcdb1b1.mp4?token=rvtkANNoKKRIXKeDCjeEGCOkNENV_X1mRJz9aeOKY_sAO-Yb8mH6dyqddsimto8nbw38mLNdWe0MjXUh9I-ZJidAVF3g74KCrIL3ap6MGMLGNVDxWA2_Kdx0vlatsnPInVz6B5REg-u9tclano4WzENg3fI7FhcAm_hC67_WZTm7-4nrrlXRvYQebaxb2CzoopqncWOotC7tsD4dsfp3ldMo07-5wTC00407d_jjMGeCkVulctogzzekm9CMXmNtApgGvF8Sre5NLyEKtcnhqHS6uGu8HquWR5Y-W9SmBKKA6ClZjYkJBslh_GAqDnaJV7oXt9MTm2qev9TzfVaHcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دبیر انجمن CNG تهران: مردم به فکر خودشان باشند، مسئولین در تأمین بنزین در شرایط بدی گیر کردن به نوعی بیچارگی...
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/145846" target="_blank">📅 11:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145845">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
شمار جان‌باختگان سیل نپال به ۱۳۴۴ نفر رسید؛ ۴۸۸۶ نفر نیز مفقود هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/145845" target="_blank">📅 10:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145844">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEYY64eOtv2aWP8TPQl11GmVckRHkDttIO9s76AiXC1B2HqE0nPhZCHkZyJ6kCwRkvekDvXAr86rL1exfrl59ppQ9kZWXV1gh91hUGnEtRob0nTyntvjLi20SQ9zTtMlu-wWSY7kyLtKR8LOj4VkBHAC5M5a77kJi2K1ur5fwpX_1y61dgpggIBxPrXEmWBD_ryvPrKB0uA2GZKTGGuMPljcXAGjSFYJUG3KhspSv48hZ-SO2nwoeLUGS9IDyvucSmRP2MwaA-mjEX5htcx9VuwYkp1R9K641__YhTB1lsDx1N73TVvZcRAx6I2aaB5Yt6OSyMtnqyW-NO_o3BZhaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بازداشت عوامل رژه موتوری مجاهدین خلق در کرج!
🔴
روز گذشته ویدئویی در فضای مجازی منتشر شد که در آن تعدادی از هواداران مجاهدین خلق در کرج اقدام به حرکت با موتورسیکلت و خودرو کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/145844" target="_blank">📅 10:45 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145843">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
حمله توپخانه‌ای اسرائیل به سوریه
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/145843" target="_blank">📅 10:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145842">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
بر اساس آمارهای تانکر ترکرز، صادرات نفت خاورمیانه در ماه اوت با کاهش ۳۹ درصدی مواجه شده است. این افت صادرات، منجر به ایجاد کسری روزانه ۷.۲ میلیون بشکه‌ای در بازار شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/145842" target="_blank">📅 10:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145841">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
افزایش موارد کرونا در ۳ هفته اخیر
🔴
رئیس مرکز مدیریت بیماری‌های واگیر وزارت بهداشت: از حدود سه هفته قبل شاهد افزایش موارد کووید-۱۹ در کشور بوده‌ایم.
🔴
سرفه و تب از علائم شایع بیماری هستند و در برخی افراد ممکن است علائم گوارشی نیز مشاهده شود.
🔴
میزان موارد آنفلوانزا نیز در هفته گذشته مقداری افزایش داشته است.
🔴
کووید-۱۹ مانند برخی از عفونت‌های تنفسی از جمله سرماخوردگی و آنفلوانزا به یک بیماری بومی تبدیل شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/145841" target="_blank">📅 10:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145840">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
ارتش اسرائیل یک تمرین سراسری غیرمنتظره با نام "طلوع سپیده دم 2.0" را آغاز کرده است تا آمادگی خود را برای یک حمله بزرگ و چندجانبه مورد آزمایش قرار دهد. این بسیج ناگهانی پس از ارزیابی‌های اطلاعاتی اخیر انجام شده توسط اسرائیل مدعی است که نشان می‌دهد ایران در حال برنامه‌ریزی برای یک حمله هماهنگ و همزمان به سبک هفتم اکتبر علیه اسرائیل، به همراه متحدان منطقه‌ای خود است
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/145840" target="_blank">📅 10:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145839">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOu1Y4uCxschoWmtsdnGdSHmkQS0w5pAuHoJtcAX1EXPeLEhoGpiQhxvvgpvwDEbBvunJuUtHov9-pIuGT6-tGW9F-261FjfcVz2zCSzaKQeLciLkNssKn3TI0OSRaeWtXVZds0TVyzLc44XEug1qTXqXd5R077cRNYqUgHJmrZOEuGpq1mlxbg4RIxbTX6rF6AXSzHXryUK7P_UCehhdBhljWwDVojiV9r5jJJ-LbQijLk1lt-OfIUqBzalF28QgeRiOczb2iCMg7GwbaRPWthwwKl1rUjhHQW-GZYdR4tJ38WK6xojRYBUbKygonZ7H_wsDFWVPgu97WC6AE8z3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان ملل سرانجام نقشه واقع‌بینانه جهان را که حاصل کار دانشمندان برجسته دنیا است به تصویب رساند.
🔴
بر اساس این گزارش، آمریکا با مخالفت دونالد ترامپ به این طرح رأی منفی داده و این نقشه را نپذیرفته است و ثبت نخواهد شد.
🔴
این تغییر به‌ویژه درباره نمایش واقعی‌تر وسعت آفریقا مورد توجه قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/145839" target="_blank">📅 10:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145838">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxD59tmzR778RM3yk4pPK3Iw-9wnEcnXvqgg4H8BOOBPbX0j2RGG1Roq2Hwxoc2qFvf2RNtoj9dT4mDubIGNuO7KyYDVwaooVgtk37L-D1ojA9o2MSFhWOSMdjQIsKpIk_xt9e2A8mvPG-Rf-juIZtAvKfp8rQ0ZnYcJyCvD419pBuRhb48N976HyhZlnIrPex4oAbjqY1G26cWhewxUMiZpZTLCmhpglBoBoYWDZRrPDh4wnz4hBVPhauHJx_7qc4RC25cwsc8kw_ARBuTxQL5yAOh76nIR8qVEFe90wJRSynj6P2eTYlOAtjKEzGjsJkIIXREsBGVBMtsK5YVGXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: ایران مجوز اقدام نظامی برای شکستن محاصره را دارد و حمله اخیر به ناوهای آمریکایی در همین راستاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/145838" target="_blank">📅 10:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145837">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73fa948c4f.mp4?token=ak94WfK1UFzstNHu0XI8SD_4c_ww5dlKiyFhRGEwGq65hsFpsvOWn5fh6LNSEf_JgLxy684iUSr0H3go-1Td1j3_V81gyA28Ii6NXgLfvM_mxwsNSQ-GtmSGMtJWIa2NqmMShIrCoueOtJXE3tQlThNcKsxpqjqYeqQ89SrvDg06u28oslZfMTmgZHGSYe-QvBXmojn2yu9esZMto_NnqTzkewLe1lccu39bbxPnYl-PFD4kkwjp6DBmiiXOmX_Qtbe66EdK1kuVPKavuS-itb9rMUxUswu7InFJ-UcGZP9yyIaY1I8SGUY6WxJH3DwAhf850QKwCA7NVtgAjRHY5UhVqj9SoRk6C1xQBUgjNjIWyD_HL1zkE6rmHXtaGXkOz2hG9egC9NvrCg9hjgyqHcHdDVbhXGlD0GohHcTlHHIi8igefSO0vYawixvgE5EZqfFdv5dFczk78TWhoQoxXHFB8mEszUk8p_-DuTSGgs8JnaU2FFBTKWwAh55qOlJgBCEibiNecekmGx34KuEbst6LI20o02MV5gvj6H4ks1ApDK0XQpSjsVsAOsuWTp6sxPSIpbhl41F34YAzydjLSNQAt5u1IqCbyEFZxlYwa1BwOSnjw7EV3FcEqRoCBZ6HoHfMmf2WvliLdIcjbXJUtNduhTaGvKoC98DwNDLOtmM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73fa948c4f.mp4?token=ak94WfK1UFzstNHu0XI8SD_4c_ww5dlKiyFhRGEwGq65hsFpsvOWn5fh6LNSEf_JgLxy684iUSr0H3go-1Td1j3_V81gyA28Ii6NXgLfvM_mxwsNSQ-GtmSGMtJWIa2NqmMShIrCoueOtJXE3tQlThNcKsxpqjqYeqQ89SrvDg06u28oslZfMTmgZHGSYe-QvBXmojn2yu9esZMto_NnqTzkewLe1lccu39bbxPnYl-PFD4kkwjp6DBmiiXOmX_Qtbe66EdK1kuVPKavuS-itb9rMUxUswu7InFJ-UcGZP9yyIaY1I8SGUY6WxJH3DwAhf850QKwCA7NVtgAjRHY5UhVqj9SoRk6C1xQBUgjNjIWyD_HL1zkE6rmHXtaGXkOz2hG9egC9NvrCg9hjgyqHcHdDVbhXGlD0GohHcTlHHIi8igefSO0vYawixvgE5EZqfFdv5dFczk78TWhoQoxXHFB8mEszUk8p_-DuTSGgs8JnaU2FFBTKWwAh55qOlJgBCEibiNecekmGx34KuEbst6LI20o02MV5gvj6H4ks1ApDK0XQpSjsVsAOsuWTp6sxPSIpbhl41F34YAzydjLSNQAt5u1IqCbyEFZxlYwa1BwOSnjw7EV3FcEqRoCBZ6HoHfMmf2WvliLdIcjbXJUtNduhTaGvKoC98DwNDLOtmM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کلش ریپورت: ناو هواپیمابر «آبراهام لینکلن» در تایلند پاکسازی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/145837" target="_blank">📅 09:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145836">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TA6OU3vMkwBDbHLjkB1o_K4ShI5oh49RdzyrQ-aJlAKX5vLl0uEMIb4v1YWdSGDmq5oqkOUeI2jvRFG2Lw7LV-1Ri0BipPtYxDKaudSflsg0cfrPLGVAcdDitKEWeDR5W1lFyCpZz6bslEbyG92YdntWaOZK-1Cfrn7HW135_ew47H-RFflnl6ox9qfkRGno0pOd1NYrDbgOz0LAe_sv2-g_gyAJtzoO7Yp-YpYuP2eiXCQw7-FAmTHQLVl0PgCNA-hh6QUCekMr5LZl34nRD338HO77bIZGIeUOa4Dlf5Hut-JMjXBIruDXP6_CKtiwNbGG3N6EiPiWyLkRpG73Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از حمله هوایی نیروی هوایی اسرائیل به ساختمان مورد تهدید در عرب‌سلیم، جنوب لبنان.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/145836" target="_blank">📅 09:45 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145835">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3d2e6a9ee1.mp4?token=N5-QpjUtQsLCGEcsuQLDtLk92Cm49MK6DPkSf3kyRV4MvcsgMuBSorlZ2wK_ehs_ID4BBFq729Yhy3QUViCAO0wJn0rV3UJEiGCWETCOdAKQ6A0DhwFqzpEyRM-U0ehOgOETMfN7IB9WEI-ZxW5qs9lz6hzfTPp6yIWD-RwYP8-vonNTb6uO_2WPXqP9UtcH_yNdJAUa-ntRzS_TX0SZoS6OEuLeQUoIUssTNYKqRFkjsupgUEGBZ43zYJY4C2oa1qDSLfi7lQHb973XLWoG0p0BfHVP-bgMc4SOpW2Xz5XqoVXPPL8Za-xQmetJsURffTs3V8zs0qe8tMiKh4jgdg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3d2e6a9ee1.mp4?token=N5-QpjUtQsLCGEcsuQLDtLk92Cm49MK6DPkSf3kyRV4MvcsgMuBSorlZ2wK_ehs_ID4BBFq729Yhy3QUViCAO0wJn0rV3UJEiGCWETCOdAKQ6A0DhwFqzpEyRM-U0ehOgOETMfN7IB9WEI-ZxW5qs9lz6hzfTPp6yIWD-RwYP8-vonNTb6uO_2WPXqP9UtcH_yNdJAUa-ntRzS_TX0SZoS6OEuLeQUoIUssTNYKqRFkjsupgUEGBZ43zYJY4C2oa1qDSLfi7lQHb973XLWoG0p0BfHVP-bgMc4SOpW2Xz5XqoVXPPL8Za-xQmetJsURffTs3V8zs0qe8tMiKh4jgdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی از پیامدهای حمله هوایی نیروی هوایی اسرائیل به عرب‌سلیم در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/145835" target="_blank">📅 09:42 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145833">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gQPqpwGYB4upJp2OL9ML7s0ZCMwNxv5erCPyq7BiUwzrcoKVNTiYpUxPPwo5MsUI-FfCV4OhZhMdhg3fWCYq9MqRFiDGWZADJqhUntJMwIE6PNyD9bBFNjTnw0RH0OxQdmTJfSnTxuGurN0fYU8RsN_XS35O4KmQ09-bvn_P--Ntb6MII8I2VcEYs0TJJDtu-1CSP8827FnmRo4mhQE765OYISzYqNdgHDih2CXGzbF9fQsN1FnKweonUybOV4rWB-DkDqXTuUtYbhRHYFner6-NmW6dbXRW1fkDhet-6t7-8R5UoKRbi5p8iWwNTQKPpah6fzM0fAsbhPtdlmgB1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WGZ2JqsP3sZ5mezb0aEBDJq0LGtDDfVjdaWhU1w4X9_ylR7cLN2H2Y3ceWukhehmtGloaExARCRPvMiL_VekzEI5RoKCldusegwblWo84-RMAWpn4ZYeEhlQSfbkEtGOPeqj0gwuJUb3HzyLSg7B3DtYESt-GkHbSwaGh3FW_zKNVdrdrqvePdsT7VkTumaGFxXbaXTmPHJ3j7DOB_1Urir2RAKq7gP2KXlaE7m96UdjZsr2n-gzPM2TUtX2G3IJXI655tYfONwrTXtI1fjOAcJBLb3yifHFsceviPEFu0C10LVvr-JDWFS7r2LLZNnfpRB-gKBH3el11-ZClc9WZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
چندین حمله هوایی اسرائیل
دقایقی پیش مناطقی در
نبطیه الفوقا
در جنوب لبنان را هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/145833" target="_blank">📅 09:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145832">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KioaUlX7sbgH9oZYvRhjMy72j11eKY9hwQbtg4kyG9yaBVuDzZ2e-omIiWkH2xpDqPCYPJioTRG_4-ocdMzQDTlSwbAPnQKqHwdns3IOPUk1fKuPBaECyKonSEcTzOCghR_REiP_9KaGpUmBY0DzPF_r6GW06hqKIpfxIkI3m4mz4eNksLO2hhLfsOehF-HIVtfwp_CBmXXVPGgdLNfCqx4esI0ICk1THEfn-vb-DpaWZ2h4JjkpQF9lFxrBmZF2K5tVwHRJ6agW6iGIhWDwvIYqGxobN3kYo3OcQjjVaKDi9o-8WLGQJhrAHvnICgyt7cHh0gVXnngAxTIkGc27OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیت هگست، وزیر جنگ آمریکا:
🔴
«جدید SOUTHCOM »
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/145832" target="_blank">📅 09:19 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145831">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7fRymhDFhYqCJNEGHoh-lfJt5dTAjWbXLXsXn_YkDrQGINnGLKMparbsM64SFHEARRL69se6tqOrwwoq_O61aCQRf5zLCqG2TatELoGzp3bQz4vZPgyOGssrYVQZBOqeC5ExRvc193iOWfeMYUhBio-pv12fsyyaTaXz2XzuMqCdnT_xaakuXWMuJW57a3g8Mku5C59g7XJzWp-m7g8mGiS-fNR-9NbVHj7QL8kclF4uA2WzlCU9sNSwlN4wY5qgN0ScXT4EjoQmlVIPH1XKN2BE-qk2QHdl_iXyv5otUsLDI6XsRuW6mepteKTPY73MYrd4UD2l3OmRFmJ6Erc2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ در شبکه Truth Social:
«بسیار تأسف‌بار است آنچه در اسپانیا در حال رخ دادن است؛ کشوری که
هیچ کنترلی بر مرزهای خود ندارد. واو!
»
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/145831" target="_blank">📅 09:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145830">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb0166bc5c.mp4?token=knPuNzY_TNhEKhHHekLl0KoZbXTPNJRbJ9XP68egj_MvCg1gByMO1Vkd6YtMUq9G1OdV1H1yQwvrpYvkF_g1okoTwXo9aGWXWipbNZqYKpvhvntXoJaB-R_AytNJyARYGIGE9Yom-dyxzAI4xpSlAzeS72XVRu9e6JQ2MvMd0zVTppwAgFUrkkN7vjzIJoYLxn47NlE5tbtP8Ii_h5ZBhBNM_pIv19US6CreH6IRwfY4IRPGdSFe1tcEUIBdqIcimumQCx1JCrvUeodCWzzPRTy9OqiGB0PTeC-Pfe0KmBu2eN-dpW_8n8ZbZvp0OHw0HdFHlh4qYY8v1fp_VEk3fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb0166bc5c.mp4?token=knPuNzY_TNhEKhHHekLl0KoZbXTPNJRbJ9XP68egj_MvCg1gByMO1Vkd6YtMUq9G1OdV1H1yQwvrpYvkF_g1okoTwXo9aGWXWipbNZqYKpvhvntXoJaB-R_AytNJyARYGIGE9Yom-dyxzAI4xpSlAzeS72XVRu9e6JQ2MvMd0zVTppwAgFUrkkN7vjzIJoYLxn47NlE5tbtP8Ii_h5ZBhBNM_pIv19US6CreH6IRwfY4IRPGdSFe1tcEUIBdqIcimumQCx1JCrvUeodCWzzPRTy9OqiGB0PTeC-Pfe0KmBu2eN-dpW_8n8ZbZvp0OHw0HdFHlh4qYY8v1fp_VEk3fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بسنت: محاصره و تحریم‌ها قدرتمندترین فشار اقتصادی تاریخ علیه ایران است
🔴
احتمالاً تنها حدود ۳۰ میلیون بشکه نفت خام ایران باقی مانده که چین هنوز آن را خریداری نکرده، این مقدار به زودی تمام می‌شود و دیگر نفتی نیست که چین بخواهد بخرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/145830" target="_blank">📅 09:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145829">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
گفتگوی تلفنی عراقچی با وزرای امور خارجه عربستان و ترکیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/145829" target="_blank">📅 08:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145828">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
هواشناسی: بعداز ظهر امروز و اوایل شب سامانۀ بارش‌زایی از شمال‌غرب وارد خواهد شد و در نیمۀ شمالی بارش‌ها آغاز می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/145828" target="_blank">📅 08:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145827">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c31c52246.mp4?token=VTZy9KZ4yKjas_UHMwogc38-PhTVD_4CVBEAgZNzw5lT1sqo1EWc2z0zOJlqdA3yPhZy7u8ELVUq4G0sv542fz6xo0oihbooJ6HYuZLpb5lY4-QDyDYWqmZJX_mBHwsw5-Ct2vsnqy4HxZbNnoKLiS0iL7ZZPdXQgQJMtpdwH23Kdxq-ulCTuVr5Gpf_Uj4UEJDCZzC23mBGyyCF31RAjkReA00fDYLNR_bxopjf7j3hzE-AGWPV-ABqk__YDHT02Or1P6gK81iu5h7WYxh77ekVvp_E49iyDzRfZeksgt7m7mezZgjXhYY6wVyNCA_xSN-_pbZD5nCtwD0rblH8hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c31c52246.mp4?token=VTZy9KZ4yKjas_UHMwogc38-PhTVD_4CVBEAgZNzw5lT1sqo1EWc2z0zOJlqdA3yPhZy7u8ELVUq4G0sv542fz6xo0oihbooJ6HYuZLpb5lY4-QDyDYWqmZJX_mBHwsw5-Ct2vsnqy4HxZbNnoKLiS0iL7ZZPdXQgQJMtpdwH23Kdxq-ulCTuVr5Gpf_Uj4UEJDCZzC23mBGyyCF31RAjkReA00fDYLNR_bxopjf7j3hzE-AGWPV-ABqk__YDHT02Or1P6gK81iu5h7WYxh77ekVvp_E49iyDzRfZeksgt7m7mezZgjXhYY6wVyNCA_xSN-_pbZD5nCtwD0rblH8hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله هوایی اسرائیل به جنوب لبنان
🔴
منابع محلی از حمله هوایی نیروی هوایی اسرائیل به منطقه عرب‌سلیم در جنوب لبنان خبر دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/145827" target="_blank">📅 08:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145826">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
معاون ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور: ممنوعیت استفاده از پیام‌رسان‌های غیربومی برای اطلاع‌رسانی رسمی دستگاه‌ها، با اجماع کامل همه اعضای ستاد ویژه ساماندهی و راهبری فضای مجازی برداشته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/145826" target="_blank">📅 08:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145825">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbWQUj3Gs7TqupzZrerCyWMAZ2kmEhAF-enaamS1ptWkfUgEYHtlpRxrDskA5PICuFAnTPjcpQZxP29k23Z_YtkaQkC5SfvLNIIcggvMkzead5IExDfojT3RdtG8_nbyjo-l3ahxMsKVUx78Xd6rfFIFsnRR2CTib0IrawQqmoDFM2y4tvivWr3ZYqOedsV5RF182OQFi2peZ6GTul8MaoBhY_Kx7_mVzStCcCRL-4Jkl1Pbcnc-xj3FpO_gFF3HRbEu-3oY_ld2NwybJHjyybLbETBLo_NuMKDohrnlZwB3UOJBrGnzxrf8Zm54zWvXao-pKS0bw-em3xolHblqhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استیو ویتکاف و جرد کوشنر، فرستادگان ایالات متحده، پس از نزدیک به سه ساعت مذاکره با ولادیمیر پوتین، رئیس جمهور روسیه، مسکو را به مقصد فرودگاه ونوکووا ترک کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/145825" target="_blank">📅 08:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145824">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34a71b14de.mp4?token=EyaWh7Nl-l0IMhzG5us4HVByz0TUHM_E7HSBIS0xJ3nAPLfoYPe9Gjl-DDKyASTr2zyjxtoMwsXrH9WOTiHDGzqH3qVRRLrCirxp71ixAvNI7JGC-BKXQEiusFqIefIAB1gAmF4fglpHAB6mA4Ghs2PQz7H5RWes6fEzuQw7UriwHf981yIlBDjqL2p8D8GjOoEahIzAmZc8ipnFWnwKStewlAH1l-Jg6Q-m-Xp78_XHxQsSEwtWFoySzTbI43munpHrZ3_jTSNGDhalFW2Es4ltSiBQLs_tTvVbidFOki1dIrYxbd3br9xp7j7o5_eD_CEcAJWaiqw80BMCvpUXsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34a71b14de.mp4?token=EyaWh7Nl-l0IMhzG5us4HVByz0TUHM_E7HSBIS0xJ3nAPLfoYPe9Gjl-DDKyASTr2zyjxtoMwsXrH9WOTiHDGzqH3qVRRLrCirxp71ixAvNI7JGC-BKXQEiusFqIefIAB1gAmF4fglpHAB6mA4Ghs2PQz7H5RWes6fEzuQw7UriwHf981yIlBDjqL2p8D8GjOoEahIzAmZc8ipnFWnwKStewlAH1l-Jg6Q-m-Xp78_XHxQsSEwtWFoySzTbI43munpHrZ3_jTSNGDhalFW2Es4ltSiBQLs_tTvVbidFOki1dIrYxbd3br9xp7j7o5_eD_CEcAJWaiqw80BMCvpUXsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سلبریتی معروف لبنانی : مجتبی خامنه ای می‌خوام به شما بگم
اینجا بیروت است نه تهران.
هویت ما عربیه نه فارسی
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/alonews/145824" target="_blank">📅 02:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145823">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YewPH_8UFxIDkS_I_lODIMF5cO4mc1DdBIFBbNV8DTOrUqAV7Vt8fI2HmPbpwD0KKOVJy6M6czQiwQVhyzR7TpkvtdlTJEeEN0qLGgb0ubxNks_4Pz3R_fbNeXM5KSD_0U3lCwqCU4pCBzBKgFFNPPfkYw9J9iclI6Io4L5bxq04MXmmXzaQz6jjigKz8MQI5vApfW-HvCvDkxHpJ8q5ytcqfY_PCliG3NRrqa1dAKWbKd1TF9tUu0IsMhoGUUkeAZspCpNJkMb6UZQ010MokNKVDsEsPv7lbMOJLXNMByUHbVn2vOMMon0LmzXowDXAp5fwMIk_iBbX4h3d9sKeSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیصر، خواننده که گفته بود جانفدا و عاشق نظام هستم بعد ۱ماهی که تو ایران بود دید نمیشه زندگی کرد و مجدد رفت خارج
✅
@AloNews</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/alonews/145823" target="_blank">📅 02:24 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145822">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
سپاه: با موشک ناو‌های آمریکا رو زدیم و اوناهم سریع فرار کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/alonews/145822" target="_blank">📅 02:07 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145821">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
رسانه‌های اسرائیلی: تعداد زیادی از نیروهای سپاه پاسداران در ارتفاعات علی الطاهر لبنان کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/alonews/145821" target="_blank">📅 02:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145820">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
ان‌بی‌سی نیوز، به نقل از مقامات کاخ سفید: ایران حق ندارد کشتی‌ها را در تنگه هرمز هدف قرار دهد و اگر این کار را انجام دهد، عواقبی در پی خواهد داشت.‌/الونیوز
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/alonews/145820" target="_blank">📅 01:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145819">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
اسرائیل: برای تحویل جسد اعضای حزب الله در تپه علی الطاهر، باید پول موشک های شلیک شده رو بدهند/الونیوز
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/alonews/145819" target="_blank">📅 01:46 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145818">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
گروه هکری عدل علی: رضا پهلوی رو میکشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/alonews/145818" target="_blank">📅 01:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145817">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ویس فحاشی خداداد</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/alonews/145817" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👈
فحاشی ناموسی خداداد عزیزی(یک جانفدا) به امید عالیشاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/alonews/145817" target="_blank">📅 01:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145816">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
‏جوری تنگه هرمز را بستین که:
‏
🔴
همه بنزین دارن ایران نداره
‏
🔴
ارزش پول ملی همه کشورها حفظ شده ، جز ایران
‏
🔴
تورم همه کشورها ثابت مونده جز ایران
‏
🔴
همه میتونن نفت بفروشن ، جز ایران
‏
🔴
همه میتونن دارو وارد کنن جز ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/alonews/145816" target="_blank">📅 00:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145815">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
فوری/شلیک موشک از سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/alonews/145815" target="_blank">📅 00:42 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145814">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
کارشناس صداوسیما: پیروزی‌های پی در پی ما علیه دشمن مدیون رهنمودهای آقا مجتبی هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/alonews/145814" target="_blank">📅 00:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145813">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‏
👈
هم اکنون حمله هوایی جنگنده‌های اسرائیلی به شهرک طلوسه و شهرک زوطر شرقی در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/alonews/145813" target="_blank">📅 00:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145812">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79dc7f9b24.mp4?token=Ze4_5Q0CTGxA4sQlsuWFSwDVNY9HsYG9wYdphvg3yNxFApRlWwpyI_a8vGnRN9gUVfDe54f7b1NZ6UPqU7mSQApv9fpByLW1QSaUhcnDDao7Qi2X4BngY1U5gSpzjYdX5sao4pKPf0nMl38_RHK93AWyEpE-njo41r9OTRpQuTW5yH0NwOoAGgWdbgLES-kAeMqgFCaigtYHDO_5SpKUqK_gvmHwEW_l9uVnaIDCqYNNTRfE0kb2OW3szXg7JBj4g3lYwaROaJglXg9fyoyrPPST-SJWu8P9gmy4IYzPjwdJ93n3rVxCTtuhgCy0sQQ6TAT8ekwlD-0YWZWMcV_d4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79dc7f9b24.mp4?token=Ze4_5Q0CTGxA4sQlsuWFSwDVNY9HsYG9wYdphvg3yNxFApRlWwpyI_a8vGnRN9gUVfDe54f7b1NZ6UPqU7mSQApv9fpByLW1QSaUhcnDDao7Qi2X4BngY1U5gSpzjYdX5sao4pKPf0nMl38_RHK93AWyEpE-njo41r9OTRpQuTW5yH0NwOoAGgWdbgLES-kAeMqgFCaigtYHDO_5SpKUqK_gvmHwEW_l9uVnaIDCqYNNTRfE0kb2OW3szXg7JBj4g3lYwaROaJglXg9fyoyrPPST-SJWu8P9gmy4IYzPjwdJ93n3rVxCTtuhgCy0sQQ6TAT8ekwlD-0YWZWMcV_d4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسرائیل این شکلی تونست تپه علی الطاهر توی جنوب لبنان رو از چنگ حزب الله در بیاره./الونیوز
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/alonews/145812" target="_blank">📅 00:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145811">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
کارشناس صداسیما: حزب الله تو قلب‌ها پیروزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/alonews/145811" target="_blank">📅 00:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145810">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
فارس: آمریکاییا تو تعطیلات آخر هفته با افزایش بی‌سابقه قیمت بنزین مواجه شدن
🔴
دولت آمریکا هم اهرم چندانی برای کاهش قیمت‌ها در اختیار نداره و موجودی بنزین پایین‌تر از حد معموله و بزودی قحطی و گرونی بنزین تو آمریکا رخ میده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/alonews/145810" target="_blank">📅 00:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145809">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89dfe86024.mp4?token=PABcsY1_Yp5aOVT2tvMrUMIXIylwppcSY1yQhWc6b__ikh4QHr-raLN_BH4yp2mU9O1088-ZvD3ioBa1GYTewuHRnwVzQaGRQkDhjWaaF-xipKHIr0ba3n9QpZtU368IaQskPerspqV8skV0QhbvHfc73vx0pGq5HkZRO61vrC-h-qmqUdJhKK8IQDQJXdzDNWSS-exTaFkh_Iz2qQnR1BvWjVXuxI7XaWV5_nuSVJAhPUY08Jbr622IkJg24UVroeH_x03aOJfnvDb1eUe8MoYeeXHSHTGij3Ha-XTApZ8_mBgYXc9C9hHy0T_1w_6ed_nFFr-30my8pryfbJ8dBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89dfe86024.mp4?token=PABcsY1_Yp5aOVT2tvMrUMIXIylwppcSY1yQhWc6b__ikh4QHr-raLN_BH4yp2mU9O1088-ZvD3ioBa1GYTewuHRnwVzQaGRQkDhjWaaF-xipKHIr0ba3n9QpZtU368IaQskPerspqV8skV0QhbvHfc73vx0pGq5HkZRO61vrC-h-qmqUdJhKK8IQDQJXdzDNWSS-exTaFkh_Iz2qQnR1BvWjVXuxI7XaWV5_nuSVJAhPUY08Jbr622IkJg24UVroeH_x03aOJfnvDb1eUe8MoYeeXHSHTGij3Ha-XTApZ8_mBgYXc9C9hHy0T_1w_6ed_nFFr-30my8pryfbJ8dBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ساده‌ترین گوشی شیائومی ۵۰ میلیون تومان!
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/alonews/145809" target="_blank">📅 23:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145808">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
برای حادثه انفجار تانکر سوخت پرونده قضایی تشکیل شد
🔴
رئیس کل دادگستری استان کردستان:
برای بررسی علل حادثه انفجار تانکر سوخت در محور سنندج ـ همدان پرونده قضایی تشکیل شده است
🔴
بررسی‌های اولیه نشان می‌دهد نقص فنی در ترمز تانکر سوخت از عوامل وقوع حادثه بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/alonews/145808" target="_blank">📅 23:44 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145807">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
معاون سیاسی نیروی دریایی سپاه: روزانه ۲ تا ۵ شناور در تنگۀ هرمز هدف قرار گرفته شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/alonews/145807" target="_blank">📅 23:36 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145804">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DUEsP8cY4n58zlqET3Qi_vMlZhUhUPwmaQFb2Qbo5hPOMu73DU0g6N519xNIY0W6ZoOndDRbDqG9DOou_rz_GPxUkRxiIxMXMpxXzLMB6zz-rnlOPGdiJK0oJo70P8Da04qptoPU52ygAxqAqIBvHYx9RaQIt1mbcKLD-9iNqfp70Sufy5WNVlX3U5R7V-FYEann_t_1dP3DhyxRDP71IkWhl2yw9ca-AJj9DN6X7vDpgMkQNwGAdI4XVC-rGQkxKStISxr_9bIrZCYkSMGot6WN4Zm7kfndw6PUfoTDlei44FeLPo10Jcd8da0RBswoRn648U3ydgSkqWEGD935Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F7AwsgBi6Iyb9YlFocue-aneFtAEEuKap6fJoJbEPkaAQ0x4n0W0WXqlxHCQUoCh8hA7jQ3Upi1VsUYTVM-YmnBcNme-2r4zavr0Qr8sJ_7rmpmfIYOOQ1Yo2m4kW_RjiA3Yj2Z9iKMf5oTVvGCEGOgPfU8LP2WlIKmXSF74MG-Q4gRvj_h7Qi3t1yP1yn-CNPRzQBHuOh9S2uBYs7fpK8AxqNFsz0MQ5sxqZlxvWUKreqt9NbyHbvgpO8f6EsK_UEimLDDNu88dp_BufvyBLsuDWW4vUnFQPAblH5KGZyfFjbHEjFKDCD9cOSGAssUOwCK2N7F_lKd2CKjMmFHJ3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kiejgepyU3ZgcHaRAn6E_pj1YzZq9506QfNqA1pRHiMk6kKqZdmd4Akipod1Ll7f9yUyhg_Hw-zBaYXoodPIhw6h-TaDqdTLX_QGweL2twnYV_BTynooHxncHLT54ZDIK_Yac6hGceZva277Ek0v5294nonkVHCxwI8GpEhWyjOQeYXTlRXy5a4ZUHrCNeVFboN3I0NSD55PiE9Wf_0pRUkj0_WDqEdiZ4yBlL_pretcgItrcjam9BYZ_3Gwc8UzpuV0VRe9kWhXn_RMXQg1s9zw6FyTcJOOmrN0NkEhPR4V9yDzYSJHpNcqEMV84JPHYtOJEcAoX4ZDVG_fIIKmLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ارتش بحرین، تجهیزات نظامی از جمله تانک‌ها و زره‌پوش‌ها را از جنوب غربی بحرین، نزدیک کاخ الصغیر، به شمال شرقی کشور، نزدیک پایگاه آمریکایی، منتقل می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/alonews/145804" target="_blank">📅 23:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145803">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
استاندار کردستان در پی انفجار تانکر سوخت ۲ روز عزای عمومی اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/alonews/145803" target="_blank">📅 23:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145802">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
نتانیاهو: ایران دوباره درحال تلاش برای ساخت سلاح هسته ایه
✅
@AloNews</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/alonews/145802" target="_blank">📅 23:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145801">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
شبکه تلویزیونی «المسیره» یمن گزارش داد که عربستان سعودی، مناطق مختلف در استان صعده یمن را هدف حملات توپخانه ای قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/alonews/145801" target="_blank">📅 23:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145800">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیلی : ارتش اسرائیل در ساعت گذشته، پس از مشاهده فعالیت‌های مشکوک در خاک سوریه نزدیک به مرزها در منطقه جولان، اقدام به شلیک گلوله‌های خمپاره‌ای کرد. از جمله مواردی که در حال بررسی است، این است که آیا افراد مسلح تلاش کرده‌اند تا یک بمب کارگذاشته یا به حصار نزدیک شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/145800" target="_blank">📅 23:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145799">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
زاکانی: وصیت نامه آقا با خودش تو بمبارون از بین رفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/alonews/145799" target="_blank">📅 22:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145798">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwII1o9OjV1ryT5bHUFPnjWxqphm_HHjJVFba7tkgJBKCByDBERCBdfBwg5IyKAfgvYrTR5vImYU7o_UUGKl4oxGGzuwsQ6gv8JszH6CWtOyBwu4xtomxl4hPfjzTV44RtlWtx0PiSzmnU9GtOszYEDiZfxGjwHKtU3QMkaZEiHvwuH4otYjp22CLg7s8zzYtQAb3IhYR1ENvjv8ekIXDoIhMP87DKtcNwwWXuG1X_I0k6Yb0TeQT8Nl2n5Louv6vZr2en9JH6Gp5_TUySB5LOcxvuk8281hABlM6qOaRFPYtwG5Xh6dAdDiePRyykdqXJ_vPsbogGDLQjnhrYYPDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آیت الله روحانی: صدا و سیما به شدت تخمی هست و کسی نگاش نمیکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/145798" target="_blank">📅 22:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145797">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3198e2b72d.mp4?token=g9OtHJiGRyb7HQzYlHgEyw9euIQxb9Sfw5Ks1OAtaz89Pe7Z33bE5vlkxuc7xBn0_ekiAtl_lT3-1zg6cGlb0vAKSWH46fX3l6ckFLA8YjHslHkx-VdVathciJ7x6Al9Un7gomwuEccNYQ3racMeGGJ-EfinwB_aUWL3FyrygaCFmQeL_9eXy4qRt7arnCHJBnU1cvmhIZ0OIuYNE3q7T2LesnDaHZX3WqGfRkDg0uU2IHh-owEKus02dUFNaxoqSMTmr2hmn2tMAFtmJuyHJySlvOgBJwVLd0m_U9euJ4yEbSrXtJKCWqTyuClZ4iQo7QTym2ZCm_gmbV-DxVW1r6cyj9vqZKpS8BX-NH-4_-U6X4TnMBtlkNr4M9Vj0HBH_o8VJwK9EkAM5YMdU649nFGyy5yCR_XlFvKm7td5pD2gc3yBTv85qwDLdgGJgb2OSnJhdozIKmPt3k991atNJxEhYGrkZ7L0c5ed-stZtutoTEBiwvvINNeLbSGOuQtbVKNNBbD6W5-1OMs9W-73tYXF95U6QsUeMVF8THtW5N5RdeWlPxxmdR2BWQZKUBfgTn0_nP45B5wECBQ9y2rSMRbXbQ-W4DyBNrEpBf2zsgYVKIN9Lj_KA-Ken95jyXhb-dBZ6lR34G_8WiLumLC5mddUtLBXWV3x3TfMAWmyp0E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3198e2b72d.mp4?token=g9OtHJiGRyb7HQzYlHgEyw9euIQxb9Sfw5Ks1OAtaz89Pe7Z33bE5vlkxuc7xBn0_ekiAtl_lT3-1zg6cGlb0vAKSWH46fX3l6ckFLA8YjHslHkx-VdVathciJ7x6Al9Un7gomwuEccNYQ3racMeGGJ-EfinwB_aUWL3FyrygaCFmQeL_9eXy4qRt7arnCHJBnU1cvmhIZ0OIuYNE3q7T2LesnDaHZX3WqGfRkDg0uU2IHh-owEKus02dUFNaxoqSMTmr2hmn2tMAFtmJuyHJySlvOgBJwVLd0m_U9euJ4yEbSrXtJKCWqTyuClZ4iQo7QTym2ZCm_gmbV-DxVW1r6cyj9vqZKpS8BX-NH-4_-U6X4TnMBtlkNr4M9Vj0HBH_o8VJwK9EkAM5YMdU649nFGyy5yCR_XlFvKm7td5pD2gc3yBTv85qwDLdgGJgb2OSnJhdozIKmPt3k991atNJxEhYGrkZ7L0c5ed-stZtutoTEBiwvvINNeLbSGOuQtbVKNNBbD6W5-1OMs9W-73tYXF95U6QsUeMVF8THtW5N5RdeWlPxxmdR2BWQZKUBfgTn0_nP45B5wECBQ9y2rSMRbXbQ-W4DyBNrEpBf2zsgYVKIN9Lj_KA-Ken95jyXhb-dBZ6lR34G_8WiLumLC5mddUtLBXWV3x3TfMAWmyp0E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
استیو ویتکاف خطاب به پوتین: «رئیس‌جمهور پوتین، بسیار ممنونیم که ما را پذیرفتید.
🔴
همین حالا بیرون نشسته بودیم؛ من، جرد، کیریل و یوری، و صحبت می‌کردیم که وقتی بازنشسته شویم، کلی داستان و خاطره باورنکردنی برای تعریف کردن خواهیم داشت و خاطرات مربوط به شما قطعاً در صدر همه آن‌ها خواهد بود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/145797" target="_blank">📅 22:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145796">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
به گزارش سی‌بی‌اس نیوز، استیو ویتکاف و جرد کوشنر، نمایندگان دونالد ترامپ، روز شنبه به روسیه سفر کردند.
🔴
رسانه‌های روسی گزارش داده‌اند این سفر در چارچوب تلاش‌ها برای ارائه یک پیشنهاد جدید با هدف پایان دادن به جنگ اوکراین انجام شده است
✅
@AloNewd</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/alonews/145796" target="_blank">📅 22:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145795">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/051a0fae8d.mp4?token=QqJ6MvqEht4pTwnxz-q2tM5VMgUBKCnfsoPUKhcLUIryjoM84LG0xCvt4YGBXbVDeaqwT1bZUcJ-OzOPg7fGdXynQa52fsvydiSfLyzeXIgmwsGmExPDa6xfFX_IbX2OnsQD-WJpJ_pZmoFtbUsJjy0vSnvB_5m2gpBNb2SWB7U83XAKqt8Sj1Pet4enSFX33EqrS1DTv16-U6ZIXWQhNXyaTfLPvd9jGsOpVsYN2mPcp4MR9P3j6kJbmNaC4F6szm8vgqTAx880LTEhziDaeyQeEGehIL9ekt8kc25Oeseh_rYZba3z8gIoHcUluqZzWtHuxR6WzdJQ-e7CNrDVYokm7uMnkarBtpQp6X7DZCDkS8KW4Ji76nIWu86P0yXNA0iwXvvkMG287EhbUjQGPuS8zOyhEdH8MxqSrbi_MbN6RN6-Dnvah4bI-tort3wKLyWn9H2EZoK7FIr-3Df5339sfJOGFJ177EUedwAIiQxL6-ZYt4jDmvYB9qhQeA6z7CFUhtkikEoitQCpN_uk1cZ4pW_YXCKxTbXCzNCbhl4uLLrejRiOI-IPya71Vi3GuAHKGFPx8ljPZ-2We2qadPfIAEDKPDjEUVwDd9IzbvMUD_4Y_0zLsBb-0htP0NNEIFFeWBOmeUk3qCp7QGPOBg92-dUqJitHlz6yb8Y0uOI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/051a0fae8d.mp4?token=QqJ6MvqEht4pTwnxz-q2tM5VMgUBKCnfsoPUKhcLUIryjoM84LG0xCvt4YGBXbVDeaqwT1bZUcJ-OzOPg7fGdXynQa52fsvydiSfLyzeXIgmwsGmExPDa6xfFX_IbX2OnsQD-WJpJ_pZmoFtbUsJjy0vSnvB_5m2gpBNb2SWB7U83XAKqt8Sj1Pet4enSFX33EqrS1DTv16-U6ZIXWQhNXyaTfLPvd9jGsOpVsYN2mPcp4MR9P3j6kJbmNaC4F6szm8vgqTAx880LTEhziDaeyQeEGehIL9ekt8kc25Oeseh_rYZba3z8gIoHcUluqZzWtHuxR6WzdJQ-e7CNrDVYokm7uMnkarBtpQp6X7DZCDkS8KW4Ji76nIWu86P0yXNA0iwXvvkMG287EhbUjQGPuS8zOyhEdH8MxqSrbi_MbN6RN6-Dnvah4bI-tort3wKLyWn9H2EZoK7FIr-3Df5339sfJOGFJ177EUedwAIiQxL6-ZYt4jDmvYB9qhQeA6z7CFUhtkikEoitQCpN_uk1cZ4pW_YXCKxTbXCzNCbhl4uLLrejRiOI-IPya71Vi3GuAHKGFPx8ljPZ-2We2qadPfIAEDKPDjEUVwDd9IzbvMUD_4Y_0zLsBb-0htP0NNEIFFeWBOmeUk3qCp7QGPOBg92-dUqJitHlz6yb8Y0uOI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
افشاگری وزیر کار دولت رییسی: برخی کارکنان موسسات نفتی و پتروشیمی بیش از ۲۵۰ میلیون حقوق می‌گرفتند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/alonews/145795" target="_blank">📅 22:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145794">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtRJUHG7AZr9QVMnCbSUkoZXlTYpNLyKkSd19kL5wHx5mXDPux5EDMjudJvv7jpjavk8VsLtrxFQ5kEp96_t2SGeuDINLc7WgssSqAbEWKRLhhz7pPG6dPvSH6ejmmHufU9K8s_Z4SMHy538sQYy7v7SNY7jueY5YUHQVxevUHikeyIzS9bQYOvB_fSN0prlk90r9vlkyCY5ZL4RZxs5NobeHiW5YzOud3M0utqKjIB-Ugl5jT4SUL3O9Kb8O0_PKHySbSwPltgk6UmLcsTZN_NSfTkre0PGmTob0BVZwzOWBJo-kh_fzxfzpReNlthdjIzCd6TKvkeDhnSVdI3N7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجری تلویزیون و سلبریتی مصری، ساره خلیفه، به همراه ۱۱ متهم دیگر توسط مقامات مصر به اعدام محکوم شد.
🔴
او سال گذشته در قاهره، به دلیل مشکوک بودن به رهبری یک سازمان تولید و قاچاق مواد مخدر، دستگیر شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/alonews/145794" target="_blank">📅 22:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145793">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
روحانی گفته بود هیچکس رو خدا انتخاب نکرده که حاکم باشه
🔴
انگار قشر اقلیت ارزشی باورشون شده بود که رهبر نظام رو خدا انتخاب کرده و این حرف روحانی رو توهین میدونن
🔴
اللهم اشفع کل المریض
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/145793" target="_blank">📅 22:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145792">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
عضو هیئت‌رئیسه مجلس: هم اکنون احتمال حمله به اسرائیل وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/alonews/145792" target="_blank">📅 22:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145791">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
آکسیوس درباره دیدار محرمانه ایران و امارات
🔴
آکسیوس مدعی شده است یک هیأت ایرانی در ۲۰ مرداد به‌صورت غیرعلنی به ابوظبی سفر کرده و با مقام‌های اماراتی درباره کاهش تنش و بهبود روابط گفت‌وگو کرده است.
🔴
بر اساس این گزارش، مقام‌های ایرانی همچنین خواستار کمک امارات برای تأمین اقلامی مانند غذا و دارو و عدم همراهی با تحریم‌های آمریکا شده‌اند؛ درخواستی که به گفته آکسیوس از سوی ابوظبی رد شده است.
🔴
این رسانه همچنین ادعا کرده چند روز بعد، پس از تشدید حملات به نفتکش‌های اماراتی در تنگه هرمز، روابط دو طرف با تنش بیشتری مواجه شد و امارات تصمیم به توقف روابط تجاری با ایران گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/alonews/145791" target="_blank">📅 22:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145782">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vXc9hPMVGpwn8PhSj4NTrhmTs4TJkPOUXZ0iHbOOzvqvP39hL0435MIISWsfjBfsvlf6fKeP16D3NgUOtTRTVxtQEEusLdItLY6CgJYmCfIMz7AX9h2V8vDqxnSsPTS7Jegr-yMV2cx2IjROZSy1xjXC_Yw4H9xOCVNSGamfaq_HB_SWw8n1i5rpGcuIw5cDhWg86zZwymWl9tMsatmvk-kDpmWjtuL5QM82jJ7lrobc8geBLdD2qU7No226n-QofJ4_F0CIx5wiVZmVrSz52BOv7dyhB7utjC5Ckyk3bHCwR1a4Kj1OzV1OMUWRlNz-McFTeMFe9fBD4kZeTIe52A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b3sopcyjkEiVlL6LFZzO2on4YRBa7QC1nHOBIoc3tIYw0cuhjfcQ-YNWeL6lVfr9pfoDAauY3DVdq61NWysGFtA1wfSRIsxwfyAxiutODy1bmSEoW2YnaNNkwiDoO90jhFGc-yE6mnNFoCbD5SUWoLp1eIlhf6JUpzao1OUvp3TIbyTOMnpvR3uQXrNYm8DhkWYQ2huvurHi5ePVi6SVW1aGIUbE6yftmqvJpaE-YFLZjoLbYZ1BfoStk8UW-AUf6qNpLHxbgvngFOmFwJHT_iFWUP7HdpNhltAoPjEkm7iEUjlw-QfZ5AUR6UvOFiU1F3sdO7MbfLWmRnXcdcwB4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z1dB_swIVaMTrnc383zpYUCktZWQXy9yMHg-IVqRD6lUvqk8-_Ng6jUhE0QdrKqEHVQxNXHVKJnatX-qp3b3oS7i6UIDapLUDjYYpp7c7emfTGRJWsAGA-fGi1poGutpZFx1-Hp33HL7vPxGQLKtiC01V5DWR-B2XVtsCMqBXfT2WeyNbfluJeFopwQ-DxZ6GwslqqTdeJEr2WVjbLFwxpSqmCs4ur5u99plbczkxRxhrVjvvM34EECqAAVRvWOXhATAk2N1pfZidYvh83SzVuqbhZ1t3CXE3JA9HhLj8Gy4ydc2aZH2mtiHkUMM2Q5Gxsje_NSEfFJXSsX4tMw1mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PYtRccX-CL-N-W_e66pPVrsmNo_7Z2P2FlWRwhKJECWgyW4Al1CDKqW8CXwkeUKU7cEGLSyr6uX7exYHRnbPUwBvrO9Wr8y8YrGpi69rplF7qbrABoEe3SIteJqN8i-WNqkNHJs34hSCRWwX-jxTDhDF0I5y0lMCiIoXuSGVBlvR6SSKzQUKxnDNYYXgIX4wOLPtDkaAvq0mPbtQRCvZIp9zdbTwl4Hgw8essfKFcBguXUvu9nkHsnQ7L-MKH5gpQKv7p3HHi9IOvWSX_bSC0cxrHVTSwuE89npEN8xduL4WqMm4NYcN_cJaml-e5YYEcP-xAGbvcCSJXp-F9JKdOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cFGUF5988kGGw2vrSzCjbcoA09r8v-lpbcqqp1ypzBMYTvFm01HpoJNGihRNsc1PxmtcqgqmVo-TJUBcZjqgdN_qWFAKMdc__byKYah_AXHC5pmex8zMnxav3GZNB8-YWhvJqERrg_IWy6SPmY4qaWG40GVqrSM_h4gB9er43zYOej2JUeTZZWd7XrPozuLtVMPFHLsefL-xUs7kOEwr_TWiutdsuXuzMHaY3m-ukarmfiNqBR-XEdlhu_mrEWi_9ygOn9shJwvWdyiQPBzNlB9jx5xsJ4nX1R_FjSLpLdeqVzDNry-4QZnFYhfyZMcjGoNF1vXHx91tx6hzLhxX7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W4NLHUi0m3tDqNHl4Y-CjJSbL74aJqXbyMfiAJPh4IWr23WD28PHUbppJRCVwQzzQg0l28CbaqJgeWs4Ku14xBbd6Ur22iWXO4T5n7DnlvnXY1a1IjJhOQwFX8aNxHDjpf5xjakHakNpIpaQRnj6tG9schnt1_qgy55oEl8jIAbkyQuObA73yKcQf11jl64ocUrqEoW5iraUHaTjXX1ml2W4SM8AIHAGL_ayebHG8W9jE7ptG2pDcGbop_iIaJyunntNnOmlw1iAEP9dKqmgSE4oA9EUmvOfoYaJMLU93-YPaoc7SY5OM39BVmSlCtcaYmT890vxlf0YZ_ikQOk0pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U9leU--UM-M1EFUQnqz1tz5grH9M7fmF5iVlBkfKJIDVveWQuhnJhH-uKbWMdSgG6VZtH0Cs7p60dddMDk8Urjal64PCAJdy2gFTa5zHHuuaGYEMMVKdzgM8OmfjHpY-fPl1GGBOaKe0itchxPl_EEFtTgSdpbwb9ZZJS-IlRmPosXSAvAzG7RWAp_cF8_k79Swj8K_f16LoGPqQlMkNXkGhVlRZS55b1V9_hqEudVZM92X6rxnGK_qyKqm0oCMVZ8w8hlxvRNMTosckRqEyy7fhuJyW2iHJKfMkSDBM2KY74PEUkfGTkDOYCDhyNMkAEpou1OIHiw5b5afMaj6SpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZpTCM9l_F8iKZGdN6GizPG08ll4ap1L02vKwCgvaCZz6BSx8QjJIcpgoF6cYrSXGYhqqmYpS8WYtg9mMS6AhYlYs9cusjg5c9-Lx4uitUXi7_CFFlFEYUa5B95F5s8qwc3mk_-xtkY2xfQI0r8dug9Jhs7_lEBMzxFBXa_Q8XtEiln233uS0bbcL4T4vZ42pxJXEObacs3AO-PwsJN0E2OGli4cAlpuGUCymG68xzQO47mRiiwZBtMdOD0x2rBgD6iIu1h6y7xw3Iy3dL3WdukVRh2nJomUKcemxmQhMnwdWID5m8t2S9fEyq57dd1BeAJOB1DVCLEh66giJi46GRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از انفجار تانکر سوخت در محور همدان- سنندج با ۱۱ کشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/alonews/145782" target="_blank">📅 22:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145781">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
وزارت خارجه ایران به سازمان ملل:
حمله آمریکا به نفتکش‌های ایرانی اقدامی غیرقانونی و تجاوزکارانه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/alonews/145781" target="_blank">📅 22:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145780">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
پوتین به کوشنر و ویتکاف: ما درخواست توقف حملات علیه کی‌یف را از طریق کانال‌های رسمی دریافت کردیم — از طریق سرویس‌های تخصصی و کانال‌های وزارت خارجه.
🔴
من دستور دادم، دستور مربوطه را، از نیمه‌شب امروز برای موقتاً متوقف کردن حملات.
🔴
حکومت اوکراین فراخوان خود را برای آتش‌بس گسترده‌تر به مدت سه روز منتشر کرد، اما این چیزی بود که ما با آن‌ها توافق نکرده بودیم.
🔴
ما تمام تلاش خود را خواهیم کرد تا از ایمنی مذاکرات و واسطه‌ها اطمینان حاصل کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/alonews/145780" target="_blank">📅 21:44 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145779">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
پوتین به کوشنر و ویتکاف: همکاران گرامی، خوش آمدید به مسکو.
🔴
وضعیتی که امروز سعی خواهیم کرد آن را مدیریت کنیم، آن‌قدرها هم آسان نیست
🔴
دوست دارم از شما بخواهم که بهترین آرزوها و کلمات سپاسگزاری صمیمانه مرا به رئیس‌جمهور ایالات متحده برسانید.
🔴
می‌دانم که او ممکن است وارد یک مسیر دشوار شود، اما با این حال، او تلاش خود را برای حل تعارض روسیه و اوکراین متوقف نخواهد کرد.
🔴
ما امروز تمام جنبه‌های آن را بحث خواهیم کرد و آماده‌ایم تا دیدگاه خود را درباره وضعیت موجود ارائه دهیم.
🔴
همان‌طور که قبلاً به ما اطلاع دادید، پس از این سفر به مسکو، قصد دارید به کییف بروید.
🔴
مهم نیست که بعداً چه اتفاقی بیفتد، این نوع تماس‌ها همیشه مفید هستند.
🔴
و در اینجا، البته، کیفیت میانجی‌گری بسیار مهم است، اعتماد به کسانی که این کار را انجام می‌دهند. می‌خواهم به شما بگویم که ما با شما به راحتی کار می‌کنیم و، البته، سطح اعتماد در طول این کار از سوی ما بهبود یافته است.
🔴
وقتی صحبت از این نوع واسطه‌گری می‌شود، آنچه اهمیت دارد اعتماد و راحتی با کسانی است که به عنوان واسطه عمل می‌کنند. شما از اعتماد کامل ما برخوردار بوده‌اید و کار با شما برای ما تا حد زیادی راحت بوده است.
🔴
برای ما افتخار است که شما را داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/alonews/145779" target="_blank">📅 21:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145778">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5974272d6c.mp4?token=fRaTxATbI9MZBDAoF3dHcKEBVmM0ZOqkey_k-bak2Hoq3APSGvCdJzYp4Yz52LUzeJLqgMoubRvE5xaLUYqYISY6RFWtiNhXc3HeojlCZB6-Vyx4djVtlI38agAo0szLw6CG4p5Kqxp5Z0mxp9WHjGA7BKw8TPfzpFU-Rfv7tDtCM4MRINU2KLsOvDKfRy6Eqb9zyYCBJMS7SAgVKqkhIN_Qb6UkchyGlWoOcicm03ePL-9mQPOjjyrNsD8EUu6_j8Mch4Zxej0OgPuJfiJ3zfaX252ZRsU1I5qTfUbD8kY-0zedfciBRDM7WwttlJALbcnwaW1P3aejt1zQpgelaS3HVcx04slHHpxj_kco349jsl4P8jlzofIh0rYphaAx485jmpCHhOia4ki0Od5ehiUTKtpmVKDS-juNQolX1J24XsfwqZF_EHA-kh-b2WN3brNRmMZ63xNozReX54Abg3ybwHBnMOoT2TTMF1UhWAtragyLgtQ1r7LyTwL8tGsxi1a0222xiaNMK4kx95R-v-rrDdz22YqNv5vn-hMrljfWeZGcVatusyxOGsFY7l65Uwx3XkPxXnE7Dndp5lVdjoFuMk5hTH1pKehcF3qExZdoQ0uwu6IxAzJNEs7fXFOIg-vTcJxYo4ZBTXHO_9VdwmKfF8qF85oa3cuDgoJL3oI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5974272d6c.mp4?token=fRaTxATbI9MZBDAoF3dHcKEBVmM0ZOqkey_k-bak2Hoq3APSGvCdJzYp4Yz52LUzeJLqgMoubRvE5xaLUYqYISY6RFWtiNhXc3HeojlCZB6-Vyx4djVtlI38agAo0szLw6CG4p5Kqxp5Z0mxp9WHjGA7BKw8TPfzpFU-Rfv7tDtCM4MRINU2KLsOvDKfRy6Eqb9zyYCBJMS7SAgVKqkhIN_Qb6UkchyGlWoOcicm03ePL-9mQPOjjyrNsD8EUu6_j8Mch4Zxej0OgPuJfiJ3zfaX252ZRsU1I5qTfUbD8kY-0zedfciBRDM7WwttlJALbcnwaW1P3aejt1zQpgelaS3HVcx04slHHpxj_kco349jsl4P8jlzofIh0rYphaAx485jmpCHhOia4ki0Od5ehiUTKtpmVKDS-juNQolX1J24XsfwqZF_EHA-kh-b2WN3brNRmMZ63xNozReX54Abg3ybwHBnMOoT2TTMF1UhWAtragyLgtQ1r7LyTwL8tGsxi1a0222xiaNMK4kx95R-v-rrDdz22YqNv5vn-hMrljfWeZGcVatusyxOGsFY7l65Uwx3XkPxXnE7Dndp5lVdjoFuMk5hTH1pKehcF3qExZdoQ0uwu6IxAzJNEs7fXFOIg-vTcJxYo4ZBTXHO_9VdwmKfF8qF85oa3cuDgoJL3oI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جان بولتون مشاور سابق ترامپ در حمله به پیت هگستث، وزیر جنگ: به نظر من او از ابتدا برای این شغل واجد شرایط نبود.
🔴
بر اساس گزارش‌ها، او برای سمت سخنگوی پنتاگون به ترامپ درخواست داده بود که با توجه به پیشینه‌اش، انتخابی کاملاً مناسب می‌بود.
🔴
او از پس این مسئولیت برنمی‌آید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/alonews/145778" target="_blank">📅 21:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145777">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIljK-dqynDUrrug5h5OjeEKSh3L8Dx4eqgwFWIvTjEkzkhIyBEjnRVfgC_R2Th51qlce_kEDeWkNCcklaDUlDxFmceC07oJwNfUb00iNvo6B8Q96etEv7BWyWQKYrEZb18TAZ88n79rtzI82p34KdCEfLoZzaCXIAuo-T28de_xlbk-FWj_lGGqP5IShphcR-LGmTZsdX-WlBDduiTR30D3cZCYUpHjhq55P44ym0v2yk-cL4JHxkQnLnygYfPCiG56JFgbTIc2FXsvJcdgNTUYmQj2C_ZUXJsQLFwCEk9HLvEtxT4O_6X5VVkRx6qxr15q8JNXrA92_qvHOLQY7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد مرندی: اکنون تمام کشتی‌های نیروی دریایی آمریکا هدف هستند. هرگونه حمله به کشتی‌های ایرانی با حملات متعدد به کشتی‌های مرتبط با کشورهای شرکت‌کننده در تجاوز ضد ایرانی مواجه خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/alonews/145777" target="_blank">📅 21:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145776">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
خبرنگار صداوسیما در جاسک و قشم: صداهای شنیده شده در این مناطق ناشی از تنبیه شناورهای متخلف در تنگه هرمز است و در این مناطق انفجاری رخ نداده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/alonews/145776" target="_blank">📅 21:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145775">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
گویا انفجارهایی که در جزیره قشم رخ داد، ناشی از شلیک موشک‌ها به سمت تنگه هرمز بوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/alonews/145775" target="_blank">📅 20:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145774">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
برخی منابع غیررسمی از شنیده شدن صدای انفجار در قشم و مناطق نزدیک به تنگه هرمز خبر می دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/alonews/145774" target="_blank">📅 20:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145773">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
پوتین، نشست خود را با ویتکوف، نماینده ویژه ایالات متحده، و جرد کوشنر آغاز کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/alonews/145773" target="_blank">📅 20:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145772">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66b1ca1096.mp4?token=aDmkl3YaJJSfDDwKmXUJBMR9ztP4rLF4RKOyZaoQSxlkGK0KT7qEMOV1xBt_bdY4o8bPNNpvKympHK9bPKBJTecsxsPq7pP5yRw9thynBwek1Ow-q5SBBIuZcJi587hl2e5lgR1ADijsgoxxlQbaFnKGqXURia6WoIj1PqhNyJxTi5H-JKPstJYoi54Jqu9UHeyxa4obRkB562ptyFmhNTuT_JYy-pkqJCRrDDBuv_jmqtgTwl8xqsDp3GEzyGWIuh60ucQCcapD25BVehVExEqU3bZB6gOJ04iRBO6jNtXOMFB_Z50WOd4fM5gdk1sbd7QZLtIrEZKSiRO4f4BqDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66b1ca1096.mp4?token=aDmkl3YaJJSfDDwKmXUJBMR9ztP4rLF4RKOyZaoQSxlkGK0KT7qEMOV1xBt_bdY4o8bPNNpvKympHK9bPKBJTecsxsPq7pP5yRw9thynBwek1Ow-q5SBBIuZcJi587hl2e5lgR1ADijsgoxxlQbaFnKGqXURia6WoIj1PqhNyJxTi5H-JKPstJYoi54Jqu9UHeyxa4obRkB562ptyFmhNTuT_JYy-pkqJCRrDDBuv_jmqtgTwl8xqsDp3GEzyGWIuh60ucQCcapD25BVehVExEqU3bZB6gOJ04iRBO6jNtXOMFB_Z50WOd4fM5gdk1sbd7QZLtIrEZKSiRO4f4BqDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ساعتی پیش تو مسیر پلیس‌راه همدان ـ سنندج، یه ماشین سنگین گویا ترمز می‌بره و مستقیم با یه دستگاه تانکر حامل سوخت برخورد می‌کنه و یه انفجار وحشتناک رخ میده!
🔴
متاسفانه تا الان 7 نفر زنده زنده سوختن و جونشون رو از دست دادن...
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/alonews/145772" target="_blank">📅 20:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145771">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
وزیر نیرو: قطعی های برق برنامه ریزی شده تموم شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/145771" target="_blank">📅 20:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145770">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
سفارت آمریکا در بحرین: از شهروندان آمریکایی که در حال حاضر در خاورمیانه حضور دارند، درخواست می‌شود که نهایت احتیاط را به خرج دهند و به احتمال لغو پروازها، بستن فضای هوایی و اختلالات سفر توجه داشته باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/alonews/145770" target="_blank">📅 20:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145769">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
آتش‌بس موقت که با میانجی‌گری آژانس بین‌المللی انرژی اتمی (IAEA) برقرار شده بود، صبح روز شنبه در اطراف نیروگاه هسته‌ای زاپوریژیا که تحت کنترل روسیه است، به منظور امکان‌پذیرسازی تعمیرات یک خط برق خارجی آسیب‌دیده، اجرایی شد.
🔴
این نیروگاه از بیستم ماه اوت از برق خارجی قطع شده و برای حفظ عملکرد سیستم‌های ایمنی حیاتی، به ژنراتورهای دیزلی اضطراری متکی بوده است.
🔴
فنی‌کاران اوکراینی انتظار می‌رود پس از پاکسازی منطقه اطراف از مین‌ها، خط برق آسیب‌دیده فروسپلاونا را تعمیر کنند.
🔴
آکسی لیکاتچف، رئیس شرکت روساتوم، گفت که انتظار می‌رود این آتش‌بس حدود یک هفته طول بکشد، اما هشدار داد که تعمیر این خط لزوماً تضمین‌کننده بازگرداندن برق خارجی به نیروگاه نخواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/alonews/145769" target="_blank">📅 20:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145768">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2950be1408.mp4?token=QLOXg_jO2K1lrX8MgHiIJrRt-VeUmorJzD_xmaS0XT1eZxv1Oai4dupjIIPWR5Pgx8OmNgRfNFy1__KyMXrHncGNYWHtE58-iQc25Ig9iwCYt335HqxvHDIHxTA5yqMeR9_6uHH9KHkubiwXnzmFcvTVw_X-kmfs5hK91e5YEOGQb8m-Hb3ZBuTXy9URkDSWUk_95FR5WcYkbc-ZPGamjsRnUTcpK3jqJ0yfnYE-vL9pgGJ5hq9Wg-3J5Nc4tfGMRj_pR5n2eNWjTQuuIs4K32ul4b6XneijK39dLdAIJnYxhR2wfhYXETXcreG23C9FOJ388kr0qlh0MhnikFlwhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2950be1408.mp4?token=QLOXg_jO2K1lrX8MgHiIJrRt-VeUmorJzD_xmaS0XT1eZxv1Oai4dupjIIPWR5Pgx8OmNgRfNFy1__KyMXrHncGNYWHtE58-iQc25Ig9iwCYt335HqxvHDIHxTA5yqMeR9_6uHH9KHkubiwXnzmFcvTVw_X-kmfs5hK91e5YEOGQb8m-Hb3ZBuTXy9URkDSWUk_95FR5WcYkbc-ZPGamjsRnUTcpK3jqJ0yfnYE-vL9pgGJ5hq9Wg-3J5Nc4tfGMRj_pR5n2eNWjTQuuIs4K32ul4b6XneijK39dLdAIJnYxhR2wfhYXETXcreG23C9FOJ388kr0qlh0MhnikFlwhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از هواپیما سوخت رسان KC-135 آمریکا با اسکورت ۲ فروند جنگنده برفراز کیش
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/145768" target="_blank">📅 20:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145767">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6588b2f6c1.mp4?token=WwLjOw7yh14XaA8oLXZCrSoF6ZwXRQqZTa-6KY2q8Dcx2XwKP9HSX_IiBLh6s29mcnXIjZ6k16EOjM_psYACqaWtZeFVTJGTHSQB8YYD3_8kByOY2hNl9E1aPsCCG0MrZxZN4xr8UI4WDT2tK-s0Po-P9b66KNcVKeyo_ysOkzR-bmKWomlO9LYMBv1rQhlnPo7Zv1ALSrJc-Pr_EhDY3bbbVUmha2TJ7V__ICh55m0kT10KyspshmkQ6XAwIzpXaE1gtd0cM1Ui1fyhjqhtVtOUN510162EebacA450TKtLyETde5-j-qYQfaq78cJ-c2yVG-PPc1oEtGZ4Pgu8aKxZvTATxhsU03B1Tt-pOoWxE3c7noGwFhLmXAlu_xdyYTyZzn2xxiJPoCUEIXJKzn_tqn72AncEC1SDMj88ra8e42sosPOMetk01oiflmly4wNem7OeUWqUtSWLX5t4GqS6Vg2VoLiGKwGeiwZBAmpArOvRh9R9w0OpWOoXfKkNYuiNu5mUExFS5jJllh9JpDR6mlcuusIw0XBKHMOESFflJGHHAVcaKqMLsBxikuZjChZkrDZY5CUhSTZBCkfUdKwnqjMeS974VnLmS1uiHkxiyQaaiFQciDFwMMqUMufJZKtzXkAi9_zNAL1RdeLpwo4CmeTKF0LlPdLk5DYKEzw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6588b2f6c1.mp4?token=WwLjOw7yh14XaA8oLXZCrSoF6ZwXRQqZTa-6KY2q8Dcx2XwKP9HSX_IiBLh6s29mcnXIjZ6k16EOjM_psYACqaWtZeFVTJGTHSQB8YYD3_8kByOY2hNl9E1aPsCCG0MrZxZN4xr8UI4WDT2tK-s0Po-P9b66KNcVKeyo_ysOkzR-bmKWomlO9LYMBv1rQhlnPo7Zv1ALSrJc-Pr_EhDY3bbbVUmha2TJ7V__ICh55m0kT10KyspshmkQ6XAwIzpXaE1gtd0cM1Ui1fyhjqhtVtOUN510162EebacA450TKtLyETde5-j-qYQfaq78cJ-c2yVG-PPc1oEtGZ4Pgu8aKxZvTATxhsU03B1Tt-pOoWxE3c7noGwFhLmXAlu_xdyYTyZzn2xxiJPoCUEIXJKzn_tqn72AncEC1SDMj88ra8e42sosPOMetk01oiflmly4wNem7OeUWqUtSWLX5t4GqS6Vg2VoLiGKwGeiwZBAmpArOvRh9R9w0OpWOoXfKkNYuiNu5mUExFS5jJllh9JpDR6mlcuusIw0XBKHMOESFflJGHHAVcaKqMLsBxikuZjChZkrDZY5CUhSTZBCkfUdKwnqjMeS974VnLmS1uiHkxiyQaaiFQciDFwMMqUMufJZKtzXkAi9_zNAL1RdeLpwo4CmeTKF0LlPdLk5DYKEzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کاروان ویژه نماینده آمریکا، ویتکوف، و جارد کوشنر به کاخ کرملین رسیده است، جایی که احتمالاً جلسه‌ای با رئیس‌جمهور روسیه، پوتین، برگزار خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/alonews/145767" target="_blank">📅 20:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145766">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
وزیر آموزش‌وپرورش:  در مدارس دولتی هیچ مدیری حق دریافت شهریه هنگام ثبت‌نام را ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/alonews/145766" target="_blank">📅 19:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145765">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
وزیر جنگ آمریکا: اگر ایران به کشتی‌های آمریکایی شلیک کند، آمریکا نفتکش‌های ایران را هدف قرار خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/alonews/145765" target="_blank">📅 19:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145764">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
فاکس نیوز: نیروهای آمریکایی پس از آنکه ایران به دو کشتی جنگی آمریکا موشک شلیک کرد، سه نفتکش ایرانی را هدف قرار دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/145764" target="_blank">📅 19:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145763">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNCTr3J6Jo-Ql5kor_JhzzRfOBdUhIlLNRHPZ1NHEdKchRp48zaaHiLwF9Xgr4Cwj-Gta_G_C1Q2OULDMi-idzujtH3oef3zYM28A7CsRp9LAb2Hfz06W3c4Kc5bZkcMTGbL8wByjPSZiTGRQYYrH4PMTqCOW-KijzNVOgiIC7hsMCPH5LyzxuA34CgKH6OXQbYFMbge3L06qCKuZ5ZcHlWPoiJ03yBUosUt_KeyjCOIgC5QZ-GITeXIty5orWpBZt79-uaQSKbjFslxwLzebYCFQ0exldgaaJ4WhoPZxYtrhZmozpw05-09T1vsqrFGD4WgKmpI6kX257DEltrPGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیده شده در تجمع جنگ طلبان:
علی الاصول یادت رفت
علی الطاهر هوا رفت
🔴
اما جالب اینجاست جنگ طلبان ذره‌ای به اقتصاد و زندگی مردم اهمیت نمیدهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/alonews/145763" target="_blank">📅 19:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145762">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
یک فروند هواپیمای جنگنده F-4 Phantom متعلق به نیروی هوایی یونان در پایگاه هوایی تاناگرا در حین برگزاری رویداد "هفته پرواز آتن" سقوط کرد.
🔴
هنوز هیچ اطلاعات رسمی در مورد وضعیت خدمه یا علت سانحه منتشر نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/145762" target="_blank">📅 19:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145761">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf5e996b2c.mp4?token=GdEE03HRBMa4g5W6pa3p_URkFSyyRgjtdAkjHvnta38zeAxfLksSEn-n4UeJktWMuR9hAZHJPmLbcs9cf8DUTcQOclZDmiy-YvKbLAkGpC4vbX_CzFxrbkjRyPGfuIB2TeiaP9DTA80pmrVzEI6cjHmt6TLrmYuwsT7BWdG9mVcFxOu-NKu4lEM2uq79wsR8d69kBpZBxgJY1cTw3HKjFsd6MtjAoe_DqVdUoM2oXuue1l7aAX6gVJz5PFMT26TXxSx9ImgUybkKsx_-rLpqDfJ7F4_y7r3xLdPKRQWpdsLaG-vHxFF8M5hwgwiBngVQKU0PxuI4nCA8o-y8o2mp83zh59bpZMpKkqngQknj4Ro_uz7qGb-CzteIc01Wfh2b6LPW3UCzpweLt6jEA5m3_Mmxmmk1UXGT_dpnQ2P5Gn9D5J0k8nAsoJJ0IySgm1heUTgcuCK8P8y1SAcNpZSWIiEIZ8UjnrLMTFu765cvfJAfVtiOMikNK1aODkOjQ_G3Edk98FynHkZV-we3H7TcPfwG2UI7slwxO1FxvKYh-2eEW5Y9Ndb9ExY9Lo_ivq4E8P9NlcLivpakRgzzqrgGXj2IvQzgHsD0hrjgv1bKAOFxSrPHDrRkpmMn1oexSrhvunrugT-xwDQOA3GKGkSVzA2s5vJqh1Yr555Joe1Fno8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf5e996b2c.mp4?token=GdEE03HRBMa4g5W6pa3p_URkFSyyRgjtdAkjHvnta38zeAxfLksSEn-n4UeJktWMuR9hAZHJPmLbcs9cf8DUTcQOclZDmiy-YvKbLAkGpC4vbX_CzFxrbkjRyPGfuIB2TeiaP9DTA80pmrVzEI6cjHmt6TLrmYuwsT7BWdG9mVcFxOu-NKu4lEM2uq79wsR8d69kBpZBxgJY1cTw3HKjFsd6MtjAoe_DqVdUoM2oXuue1l7aAX6gVJz5PFMT26TXxSx9ImgUybkKsx_-rLpqDfJ7F4_y7r3xLdPKRQWpdsLaG-vHxFF8M5hwgwiBngVQKU0PxuI4nCA8o-y8o2mp83zh59bpZMpKkqngQknj4Ro_uz7qGb-CzteIc01Wfh2b6LPW3UCzpweLt6jEA5m3_Mmxmmk1UXGT_dpnQ2P5Gn9D5J0k8nAsoJJ0IySgm1heUTgcuCK8P8y1SAcNpZSWIiEIZ8UjnrLMTFu765cvfJAfVtiOMikNK1aODkOjQ_G3Edk98FynHkZV-we3H7TcPfwG2UI7slwxO1FxvKYh-2eEW5Y9Ndb9ExY9Lo_ivq4E8P9NlcLivpakRgzzqrgGXj2IvQzgHsD0hrjgv1bKAOFxSrPHDrRkpmMn1oexSrhvunrugT-xwDQOA3GKGkSVzA2s5vJqh1Yr555Joe1Fno8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه هشدار تخلیه خدمه نفتکش های جمهوری اسلامی توسط خلبان جنگنده ارتش آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/145761" target="_blank">📅 19:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145760">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
وال استریت ژورنال: حمله به نفتکش‌های ایرانی یک استراتژی جدید برای مجازات ایران و محدود کردن توانایی آن در صادرات نفت است.
🔴
ترامپ درحال بررسی از بین بردن تمام ناوگان نفتکش های ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/alonews/145760" target="_blank">📅 19:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145759">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r40pBcFqETXQ8dfkU-ecEKXUAIE4Iqs8VVFz_ypH4nHRsQOnnwrS_90DDJcTZ2XLje8mdjS0enAdE0_W-7kflT3IkkEOcPaDt6cfrQX4sxbezImfC9xrNeWk2IBHrOBfeasyTysQAJ-_oxp4ThWgPHMzMOUCkRo6IeSVNlfA_hkFOOsgETO6bCuc2wSwgCVL6H-MlYIcqQCa0RrN0prNdA6vtXr_jVizy7A4_oKwwaNPJ1Y2-pMqYVCSakxQS-V-FEmoXZLXrAo1rdGce0MpOZgfTffkd8ao_zYvWisu1b7lupQBrbEz_N-WjjNwVN0pmUjJXyHOSrFIbDR6iGx7jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / گزارش تیراندازی به چند کشتی تجاری در خلیج فارس و دریای عمان
🔴
نهاد دریایی بریتانیا اعلام کرده گزارش‌هایی از تیراندازی به چند کشتی تجاری در شمال خلیج فارس و دریای عمان دریافت کرده است؛ اقداماتی که ظاهراً با هدف مختل کردن حرکت شناورها انجام شده‌اند.
🔴
این حوادث همزمان با ادامه فعالیت‌های نظامی در منطقه گزارش شده‌اند.
🔴
این نهاد هنوز وقوع تلفات یا خسارات زیست‌محیطی را تأیید نکرده و بررسی‌های رسمی درباره جزئیات حوادث ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/145759" target="_blank">📅 19:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145758">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
زلنسکی: آماده‌ایم تا ۳ روز از انجام حملات به مسکو خودداری کنیم؛ انتظار داریم روس‌ها نیز از حمله به کی‌یف خودداری کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/145758" target="_blank">📅 18:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145757">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29316aa283.mp4?token=AT18a2_peMpinG1c3vd52Nh79sZkFL_UUJ6twIHXaV2Oy93TXdT3NHIfBUS4W-X4WJKAEvY8p90qOGYeAjE3TA9AoVZs7bFnyisARmonBnYXurCvdwPkGd_MP2IeKMuaazEEwmT5TxWjwOmPyTM6jjXkMUb3vyEq5rjEO1_HTNIIuhGcB81agxuLNc3x3FgFl4g769Ckfgg7f-021UZqEfkWWI2QBvY2P3aEA84PPwYAKmBlro8X9iKGVLu9Y_QQV_X9ieCgjKh-uyLaV4Cuj--Wcx2IJe-UYVjonjXuXno8VjzZ_R9pri5PkjECzcmSDOpRu_GS81mhftW2UU-2Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29316aa283.mp4?token=AT18a2_peMpinG1c3vd52Nh79sZkFL_UUJ6twIHXaV2Oy93TXdT3NHIfBUS4W-X4WJKAEvY8p90qOGYeAjE3TA9AoVZs7bFnyisARmonBnYXurCvdwPkGd_MP2IeKMuaazEEwmT5TxWjwOmPyTM6jjXkMUb3vyEq5rjEO1_HTNIIuhGcB81agxuLNc3x3FgFl4g769Ckfgg7f-021UZqEfkWWI2QBvY2P3aEA84PPwYAKmBlro8X9iKGVLu9Y_QQV_X9ieCgjKh-uyLaV4Cuj--Wcx2IJe-UYVjonjXuXno8VjzZ_R9pri5PkjECzcmSDOpRu_GS81mhftW2UU-2Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار صداوسیما در لبنان:  اعضای سپاه در تپه‌های علی‌الطاهر توسط ارتش اسرائیل محاصره شدن و در شرایط عاشورایی قرار دارن
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/alonews/145757" target="_blank">📅 18:53 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145756">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
سفارت آمریکا در بحرین به آمریکایی‌ها نسبت به حملات احتمالی ایران هشدار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/145756" target="_blank">📅 18:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145755">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDCnYDX0oHgVS43fkMWarfdrWTLKD3WZzSlvtYhO0ZYlAz2CqCBFONkbDi-M_3oVaD03NUxbqGuxdxEo4z-rAlCnXmrv-y8f1KVXnRR0QXu52qAnv2Gk_4MmnDwAcJ4vClwfiFzovBTwZNaYrP4BxxJDeDt76QKWUByJzC-zF95sn30JPOykdFVmXoBCjIvmwV-lP_uoZGWC3moxHLAhciWzsHQMJFPWyAF9H5h1hH5S1jxikjJk2QuZR5BEGAr4LYvIWJ7o8Lin3hdp5bumBhPgpUN7NL90cS8BmjvHPkrT9A1T8tqdemjlQorej3lMcwDnj7-cvl6nun3KRTuiyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی سابق مجلس: پیش نویس قطعنامه جدید آژانس، کد رمز برای حمله مجدد به مراکز هسته ای ایران است. ترامپ اعلام کرد ممکن است خیلی زود به کوه کلنگ حمله کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/145755" target="_blank">📅 18:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145754">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
دادستان فومن: موتور سوار زن بدون گواهینامه ببینیم غیر قانونیه و میگیریمش
✅
@AloNews</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/145754" target="_blank">📅 18:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145753">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQo7qP7f6TUMNs7apmbgpyZxXXi5gxJGQadoNoZQVc_XXbMrxiCqlmangPrfYCe8yJ9-fVniv90ilY6_2Yg6RKe4HfkU1Gw4pCp8K_2A0-AQ5dW8BWvd0ygn1UDJ-Yz8NguLD3HwlbPfC_fUtfeeFkZRsLb4uL_F94BEsYAmO46nK279SIpoEilvlfJflPgqvJqYSXax0yG7KO-nIXIVm8VkT6Tk5uTobAp2Q_gA-TMdZ6p3QQn6o-_9XCoPUERenPzZhcA-7kG7hIZL-xIUCqzJcMSkMEAWq1-eiG064_g_u5NDElZdAgS1QF1pU6b6nR5OEiZKR0YKCwkB4FVr0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زاکانی:
مردم عزیزمون نگران نباشن، برنامه‌ها داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/145753" target="_blank">📅 18:15 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
