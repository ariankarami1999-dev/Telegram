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
<img src="https://cdn4.telesco.pe/file/qVHde0o13jMNt-Ec4OMzlsaB0Pc9rs22hFnG8PV42CkdxHKEt9E24yc8EjktIaGFtigglAwvqPWLK5LG5VQ-QsMxlnUd4KWPVKnqHcivASJ5Wt-Tm36WHpDlWh4A71DP_JBvNwA5T9yWULNcv9xlTwW1PbKhdpwh5hE8O4-3Qt0KxtyB81SLEVOBYCrLKAonv0hJ0TId8iKV4jJY7y7ZFv3tbK9M3nqlNBehXLVc6eJGVKXODcT49x3vsmtPu1-1gn3f2UlXx2M-UjHjE9A76Sg8ut4rkXSwNevcxPZGIfkCU_NSah-EP9yrSo_Nle4takE7v7hh2kKMqBgh62MQZw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 447K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 12:48:51</div>
<hr>

<div class="tg-post" id="msg-22171">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ارتش ایران اعلام کرد که امروز صبح، امارات و کویت را هدف قرار داده است:
ما "سیستم‌های ارتباطی هوایی"، "انبار تجهیزات" و "پناهگاه‌های هواپیماهای جنگی" متعلق به ارتش تروریستی آمریکا را در پایگاه احمد الجابر در کویت، با موشک و پهپاد هدف قرار دادیم.علاوه بر این، پایگاه‌های استقرار نیروها و "سیستم‌های رادار" متعلق به ارتش آمریکا در امارات نیز مورد هدف قرار گرفتند.
@WarRoom</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/withyashar/22171" target="_blank">📅 12:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22170">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نرخ دلار ۲۲۴،۰۰۰ تومان(سقف تاریخی)
دلار کف بازار :نامعلوم ! تونستی بخر!
تتر ۲۲۲،۰۰۰ تومان (سقف تاریخی)
بیتکوین ۷۷،۹۵۹ $
انس جهانی طلا ۴،۴۳۴ $
نفت برنت  ۹۵،۲۹$
@WarRoom
🚨
🚨
🚨
🚨
۱۲ ظهر تهران</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/withyashar/22170" target="_blank">📅 12:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22169">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f620a5c792.mp4?token=NV1_Q8pcqWw5rrIDx-bx9amBkBtf6hQN1sPo0aMozLXsuSNW_vvR_Xhem_Pfoay-urxCocTaCufJXKGSS-bY-ZSJyBvWVYa4QXLicJmsSWT0WoCYYewpiZnd88o_UQF8A759FIbb2ynO9GJrQoltnKf41oWPPuBXHRoEuMWWxz8r4FUTqND8T12pE_kBLHnJ2MXRgGk-weOMcszL-OnB_OiA9Z7MltDzLqOFVvyMrMcAKHalBhNPTLaCJcYI2J6NEkMYMg0tO5CfaWyX2pkLwtyN7Yuy6VFqR9mR05QeI7MWyNnJ0PlPHtS2yh-TZck2UPqOTQ5Yr_YjhjEzm24MfzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f620a5c792.mp4?token=NV1_Q8pcqWw5rrIDx-bx9amBkBtf6hQN1sPo0aMozLXsuSNW_vvR_Xhem_Pfoay-urxCocTaCufJXKGSS-bY-ZSJyBvWVYa4QXLicJmsSWT0WoCYYewpiZnd88o_UQF8A759FIbb2ynO9GJrQoltnKf41oWPPuBXHRoEuMWWxz8r4FUTqND8T12pE_kBLHnJ2MXRgGk-weOMcszL-OnB_OiA9Z7MltDzLqOFVvyMrMcAKHalBhNPTLaCJcYI2J6NEkMYMg0tO5CfaWyX2pkLwtyN7Yuy6VFqR9mR05QeI7MWyNnJ0PlPHtS2yh-TZck2UPqOTQ5Yr_YjhjEzm24MfzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ خطاب به هگ‌ست در مورد ایران: شما شب گذشته کار بسیار خوبی در مورد ایران انجام دادید. شما آن‌ها را به شدت شکست دادید. بسیار عالی.
ما در این زمینه، به هر حال، پیروز می‌شویم. ما باید این را بگوییم، زیرا رسانه‌ها از گفتن آن خودداری می‌کنند.
با این حال، حتی روزنامه نیویورک تایمز هم گفت که ایران اخیراً وضعیت خوبی ندارد. این یک خبر تکان‌دهنده بود وقتی آن‌ها این را گفتند.
آن‌ها هیچ هواپیمایی، هیچ چیز مربوط به هواپیما یا کشتی ندارند. همه آن‌ها در اعماق دریا یا در انتهای باند فرودگاه هستند
@WarRoom</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/withyashar/22169" target="_blank">📅 11:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22168">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">رویترز به نقل از منابع: ایران به آمریکا هشدار داده است در صورت حمله اسرائیل به ارتفاعات «علی‌الطاهر» در جنوب لبنان، تهران با قدرت پاسخ خواهد داد. بر اساس این گزارش، نیروهایی از سپاه پاسداران در کنار نیروهای حزب‌الله در این منطقه و شبکه تونل‌های زیرزمینی آن حضور دارند. ایران هشدار داده هرگونه عملیات همه‌جانبه اسرائیل برای تصرف این ارتفاعات می‌تواند با پاسخ مستقیم و گسترده تهران روبه‌رو شود.
@WarRoom</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/withyashar/22168" target="_blank">📅 11:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22167">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گزارش پرتاب ۴ پهپاد از سیریک
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/withyashar/22167" target="_blank">📅 11:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22166">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVGDfPmafGiWzhJXh8UMfIhULb2A7vNcgh9VhncQk6bjsLsqLfFrvdUt9F58ECCtGmtOOILRV4Hxt69BWf5Zow5H8D857SglIp4frMXj_xAQDNrL-o-UYA6LbsbWJ0bzIr11rsGQjDLlxYqGwc7F6oAUR1AU-07ZE_ieiwuok7crEadj_B7dxYzWyF-aoXTRFI_pig5dyPa_UQeHHfj8QoxwTjq1nsPOwumANOdwElUWr4jqgVaPzomqUvorqxyP6hh8hPZ9VD71PY5goixWHm3BV6vng93WiQlTB5wxowJeZ4HfgIlJyt3EJSX_wbLrOESf6JQ7HmxInSNTKZf51Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه جوون دهه هشتادی ۲۳ ساله کرمانی
زمین خودش به ارزش ۹ میلیارد رو وقف مسجد جمکران کرد تا اونجا رو بسازن و معارف اهل بیت رو گسترش بدن.
@WarRoom
دیگه کرمان هم جنس خوب نیست و همش صنعتیه</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/withyashar/22166" target="_blank">📅 11:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22165">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">وال‌استریت ژورنال: پیت هگست، وزیر دفاع آمریکا، مأموریت و استقرار شماری از نیروهای آمریکایی در منطقه را تا سال آینده (۲۰۲۷) تمدید کرده است؛ اقدامی که نشان می‌دهد واشنگتن خود را برای ادامه درگیری با ایران و حفظ گزینه‌های نظامی بیشتر آماده می‌کند. در حال حاضر…</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/withyashar/22165" target="_blank">📅 11:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22164">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">بر اساس گزارش رویترز، شماری از مقام‌های ارشد کاخ سفید در حال بررسی این احتمال هستند که پس از انتخابات میان‌دوره‌ای آمریکا در ۳ نوامبر، در صورت ادامه درگیری و شکست تلاش‌های دیپلماتیک، اقدام نظامی علیه ایران را تشدید کنند. با این حال، دولت ترامپ در حال حاضر…</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/withyashar/22164" target="_blank">📅 11:00 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22163">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">رویترز هک شد
مالک خبرگزاری رویترز در بیانیه‌ای مطبوعاتی اعلام کرد یکی از واحدهایش با حادثه امنیت سایبری مواجه شده است.cاین حادثه امنیت سایبری در پلتفرم مدیریت پرونده‌های قضایی C-Track که برای مدیریت دیجیتالی پرونده‌ها و اسناد دادگاهی استفاده می‌شود، رخ داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/withyashar/22163" target="_blank">📅 10:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22162">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c5b61e6d4.mp4?token=oVQMHv0Iuev6QcpDRirpkXj-fK-efn3qtQR1Kcpa99Yy3_WM0477bWlpChcnXFHnuAGAMiOuMib6lMhQTpT7fsGKoAilwW-JRd4ILkZUqXczps69rxhPyuwA8V0biiZEUXkfLuCYGgmuYI3dsEeTwZpITXVpTZxXvCeLADTci3Q69BfAxrLvh96oFVvHoRbh_EhD9rAsDFT_CR9b1EYbfw9E9lWMcyvVeKMm5N7_V1CJcQeMv02lnM3FM9lIZPemBhxsca4OyjoRZRE7ueRCaa-eybtZ2ILsPrikQe54jX4-jL-s8hPM783aGUE62qM39pDpx4MviA7z2oNXJOL8FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c5b61e6d4.mp4?token=oVQMHv0Iuev6QcpDRirpkXj-fK-efn3qtQR1Kcpa99Yy3_WM0477bWlpChcnXFHnuAGAMiOuMib6lMhQTpT7fsGKoAilwW-JRd4ILkZUqXczps69rxhPyuwA8V0biiZEUXkfLuCYGgmuYI3dsEeTwZpITXVpTZxXvCeLADTci3Q69BfAxrLvh96oFVvHoRbh_EhD9rAsDFT_CR9b1EYbfw9E9lWMcyvVeKMm5N7_V1CJcQeMv02lnM3FM9lIZPemBhxsca4OyjoRZRE7ueRCaa-eybtZ2ILsPrikQe54jX4-jL-s8hPM783aGUE62qM39pDpx4MviA7z2oNXJOL8FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استاد ممباقر : در زمان حمله هوایی چه باید کرد
@WarRoom</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/withyashar/22162" target="_blank">📅 10:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22161">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a7c97f4e9.mp4?token=Cajkv8Qj915rwErVy3OOfj26h_9yWGUmhwQM-R3fVLgQbDcRD8fKeM5KJwkKZTPR0Wj8AqAQD3y__HHVQILwpqBDNSrpOWZYi8KkIKOZF8ceJEYMDkVMCAp8y1VgUhs-6Jy-PJC97fWYcJo7cb5L7gqkJ7mtuuyA-31P_iBP8aV9tHPAOwKVkIxHl7ASovzzu-DVrnBKaOTuS_Vr5br3SOYXiPeViJegVxnxF_IeAjf-u9IEpcVy6PtjxtmdT_pahcXroM3P21ygYEhnqTzj_MiceUbEnkd1ul2PPqOf-Xvfp_xeyTz_Xz_Efcws5CfE0KpN_kFEt6FYPLk8D1ZQPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a7c97f4e9.mp4?token=Cajkv8Qj915rwErVy3OOfj26h_9yWGUmhwQM-R3fVLgQbDcRD8fKeM5KJwkKZTPR0Wj8AqAQD3y__HHVQILwpqBDNSrpOWZYi8KkIKOZF8ceJEYMDkVMCAp8y1VgUhs-6Jy-PJC97fWYcJo7cb5L7gqkJ7mtuuyA-31P_iBP8aV9tHPAOwKVkIxHl7ASovzzu-DVrnBKaOTuS_Vr5br3SOYXiPeViJegVxnxF_IeAjf-u9IEpcVy6PtjxtmdT_pahcXroM3P21ygYEhnqTzj_MiceUbEnkd1ul2PPqOf-Xvfp_xeyTz_Xz_Efcws5CfE0KpN_kFEt6FYPLk8D1ZQPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه چادری جلوی یه دختر موتورسوار رو گرفته، وببین چی میگه…
@WarRoom</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/withyashar/22161" target="_blank">📅 10:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22160">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">رویترز: تشدید جنگ ایران و آمریکا نگرانی‌ها درباره تلفات غیرنظامیان را افزایش داده است.
رویترز گزارش داده شدت گرفتن دوباره درگیری‌ها توجه‌ها را به شمار قربانیان غیرنظامی در ایران جلب کرده است.
تازه‌ترین حملات آمریکا، ۱۸ نفر کشته و ۱۰۸ نفر زخمی شده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/withyashar/22160" target="_blank">📅 10:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22159">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1eb4d6be4.mp4?token=qPLBxkZzDbD0rMMUBb5cKnmWtIRDWpG2nyxnNyjopUbsfgEYh5jthrU8j8RZPLXuDdu43qjuPkNsGWNuNgQdA3nBHOqXWxMlA5OJu7buBSW4T_HOiCNLGqkZ05Nwc45EFx8GIvatZ0-i0B7mJGZrUoiVkz4svhIyD45slhziZjFFDF1uGGiwflkuQaMJGqPiNIIYTVkxRkTFBQec161iAqIbz9tztQ6TVPtgSenpG1K-zEJ4Vlwullwx3e3QmcX3NwFNTlphbOCCBqPhD0xkj3q4IXgGoW1YwX-AMjxfXlJf97MxR8oRGXsgaYSJRmrClpPwYlFKNJXAGC5qt1eIjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1eb4d6be4.mp4?token=qPLBxkZzDbD0rMMUBb5cKnmWtIRDWpG2nyxnNyjopUbsfgEYh5jthrU8j8RZPLXuDdu43qjuPkNsGWNuNgQdA3nBHOqXWxMlA5OJu7buBSW4T_HOiCNLGqkZ05Nwc45EFx8GIvatZ0-i0B7mJGZrUoiVkz4svhIyD45slhziZjFFDF1uGGiwflkuQaMJGqPiNIIYTVkxRkTFBQec161iAqIbz9tztQ6TVPtgSenpG1K-zEJ4Vlwullwx3e3QmcX3NwFNTlphbOCCBqPhD0xkj3q4IXgGoW1YwX-AMjxfXlJf97MxR8oRGXsgaYSJRmrClpPwYlFKNJXAGC5qt1eIjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: اقتصاد آن‌ها بدترین اقتصاد در کل جهان است و پولشان بی‌ارزش است. بنابراین، فقط مسئله زمان است؛ فقط مسئله زمان
@WarRoom</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/withyashar/22159" target="_blank">📅 09:54 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22158">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a756d7f2d.mp4?token=sYkTuTHpCrK1nvid3nyYytn8KWtTs2CPii4fJoUvsZhGJcV2zP1cab1sh_OfGQfkgqbqS605CuB0P-fkUZaUvLGifQ_4Eo5a-ZJNvnZ9yxVfPI3dnX4soMYWLJWvVM3mj-3SPb495wlMBrnFMFjpw8b_seoqdnra3cpM5X9KcH1_RlWK72zyYaibiD-mwgvHIbFXICrN5SZHrZhCqvhGJekQfP8Nyh5P4qv-z8KBRAzvMgdnOEawyokqZqkuu7mgPUmWbTUxSP7V2kZvovPhaHw2RImzQ1E75gBRsEx-9-vsdmBCI0lO2a7QQ42kS9QTr-Hi7WPfyx0HEAj84DmELw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a756d7f2d.mp4?token=sYkTuTHpCrK1nvid3nyYytn8KWtTs2CPii4fJoUvsZhGJcV2zP1cab1sh_OfGQfkgqbqS605CuB0P-fkUZaUvLGifQ_4Eo5a-ZJNvnZ9yxVfPI3dnX4soMYWLJWvVM3mj-3SPb495wlMBrnFMFjpw8b_seoqdnra3cpM5X9KcH1_RlWK72zyYaibiD-mwgvHIbFXICrN5SZHrZhCqvhGJekQfP8Nyh5P4qv-z8KBRAzvMgdnOEawyokqZqkuu7mgPUmWbTUxSP7V2kZvovPhaHw2RImzQ1E75gBRsEx-9-vsdmBCI0lO2a7QQ42kS9QTr-Hi7WPfyx0HEAj84DmELw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کریس رایت، وزیر انرژی آمریکا: مسیرهای جایگزین برای انتقال نفت و گاز ایجاد خواهد شد و نمی‌توان همه تخم‌مرغ‌ها را در یک سبد گذاشت. شاید جهان پیش‌تر به تنگه هرمز وابسته بوده، اما ترامپ در حال تغییر این وضعیت است. خطوط لوله جدید ساخته و خطوط موجود گسترش داده خواهند شد تا وابستگی به تنگه هرمز و اهرم ایران برای استفاده از آن کاهش یابد. رایت همچنین گفت نیروی دریایی آمریکا در حال خنثی کردن تهدیدهای ایران است و انتقال نفت و گاز به بازارهای جهانی ادامه دارد
@WarRoom</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/withyashar/22158" target="_blank">📅 09:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22157">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">حکم صادق ساعدی‌نیا در دیوان عالی کشور تأیید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس و مصادره کلیه اموال
بر اساس اعلام مرکز رسانه قوه قضائیه، حکم پرونده صادق ساعدی‌نیا در دیوان عالی کشور تأیید شده است. او به اتهام «فعالیت رسانه‌ای و تبلیغی علیه امنیت کشور به نفع گروه‌های معاند» به
۱۲ سال و ۶ ماه و یک روز حبس تعزیری
و
مصادره کلیه اموال منقول و غیرمنقول به نفع دولت
محکوم شده است. همچنین به‌منظور جبران خسارت واردشده به اماکن و اموال عمومی در استان قم، ساعدی‌نیا به
دو سال منع اشتغال در شغل کافه‌داری پس از پایان حبس
محکوم شده است
@WarRoom</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/withyashar/22157" target="_blank">📅 09:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22156">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">وال‌استریت ژورنال:
پیت هگست، وزیر دفاع آمریکا، مأموریت و استقرار شماری از نیروهای آمریکایی در منطقه را تا سال آینده (۲۰۲۷) تمدید کرده است؛ اقدامی که نشان می‌دهد واشنگتن خود را برای
ادامه درگیری با ایران و حفظ گزینه‌های نظامی بیشتر
آماده می‌کند. در حال حاضر حدود
۵۰ هزار نیروی آمریکایی و ۱۹ ناو جنگی
در منطقه حضور دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/22156" target="_blank">📅 09:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22155">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">رویترز به نقل از منابع: دست‌کم سه پالایشگاه نفت هند و یک شرکت بزرگ بین‌المللی انرژی قصد دارند به‌دلیل نگرانی‌های امنیتی، استفاده از کشتی‌های قرارگرفته در فهرست سیاه جدید ایران را متوقف کنند.
این تصمیم پس از آن گرفته شده که ایران فهرستی اولیه شامل
۴۵ کشتی
را به‌دلیل نقض مقررات دریانوردی در تنگه هرمز ممنوع کرد؛ پالایشگاه‌ها همچنین قصد دارند از این کشتی‌ها در عملیات انتقال نفت از کشتی به کشتی (STS) استفاده نکنند
@WarRoom</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/22155" target="_blank">📅 09:37 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22154">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ در گفت‌وگویی تلفنی با شبکه «کان» اسرائیل، در واکنش به تشدید تنش‌ها با ایران گفت
اسرائیل نباید نگران باشد؛ چون من
رئیس‌جمهور هستم
و تأکید کرد که آمریکا از اسرائیل حمایت خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/withyashar/22154" target="_blank">📅 09:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22153">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اکسیوس به نقل از منابع: ویتکاف آخر هفته گذشته با طحنون بن زاید، مشاور امنیت ملی امارات، در ساردینیا دیدار کرد و درباره گام‌های بعدی در قبال ایران رایزنی کردند.
این دیدار در حالی انجام شد که دولت ترامپ فشار اقتصادی بر ایران را افزایش داده و کارزار «عملیات طرد اقتصادی» را دنبال می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/withyashar/22153" target="_blank">📅 09:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22152">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">آکسیوس: مارکو روبیو از سفارتخانه‌های آمریکا خواسته دولت‌های میزبان را برای قطع فوری و نظام‌مند تجارت با ایران تحت فشار قرار دهند.
در این دستور، از سفارتخانه‌ها خواسته شده فعالیت‌های تجاری غیرقانونی مرتبط با ایران را شناسایی و از دولت‌های میزبان بخواهند
شعب بانک‌های ملی ایران و صادرات ایران
را که واشنگتن آنها را مرتبط با سپاه پاسداران می‌داند، تعطیل کنند. سفارتخانه‌های آمریکا در
ابوظبی، مسقط، هنگ‌کنگ، دوحه، لندن، برلین و چند پایتخت آسیای مرکزی
نیز در این روند مأمور شده‌اند. واشنگتن هشدار داده کشورها و شرکت‌هایی که به تجارت با ایران ادامه دهند، ممکن است با تحریم و محدودیت دسترسی به نظام مالی و دلار آمریکا روبه‌رو شوند
@WarRoom</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/withyashar/22152" target="_blank">📅 09:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22151">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">بر اساس گزارش رویترز، شماری از مقام‌های ارشد کاخ سفید در حال بررسی این احتمال هستند که پس از انتخابات میان‌دوره‌ای آمریکا در
۳ نوامبر
، در صورت ادامه درگیری و شکست تلاش‌های دیپلماتیک، اقدام نظامی علیه ایران را تشدید کنند. با این حال، دولت ترامپ در حال حاضر تلاش دارد پیش از انتخابات از گسترش بیشتر جنگ جلوگیری کند؛ چراکه ادامه درگیری، افزایش قیمت سوخت و تلفات احتمالی می‌تواند به جمهوری‌خواهان در انتخابات آسیب بزند.
@WarRoom</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/withyashar/22151" target="_blank">📅 09:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22150">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گزارش پرتاب موشک از‌ تبریز
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/22150" target="_blank">📅 01:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22149">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">گزارش صدای انفجار از تنگه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/22149" target="_blank">📅 01:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22148">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">😍</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/22148" target="_blank">📅 00:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22147">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/22147" target="_blank">📅 00:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22146">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">واشنگتن پست: پنتاگون دسترسی نظامیان به اطلاعات محرمانه و حساس را کاهش می‌دهد، این در حالی است که نگرانی‌های فزاینده‌ای در داخل ارتش آمریکا در مورد پیامدهای احتمالی جنگ با ایران وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/22146" target="_blank">📅 00:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22145">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پدافند شرق تهران فعال شد
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/22145" target="_blank">📅 00:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22144">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">@WarRoom
Branding</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/22144" target="_blank">📅 00:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22143">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">السیسی، رئیس جمهور مصر، در جریان سفر شی جین پینگ به مصر، حمایت قاهره از موضع چین در قبال تایوان را مجدداً تأیید کرد و اظهار داشت که تایوان «بخشی جدایی‌ناپذیر» از چین است.
ترامپ : با شی حرف میزنم
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/22143" target="_blank">📅 00:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22142">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">@WarRoom
Khate man</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/22142" target="_blank">📅 00:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22141">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHamid Taheri</strong></div>
<div class="tg-text">یاشار جان مجدد درود دلیل اینکه ایران اینترنشنال این همه بر علیه ترامپ هست و سعی در خراب کردن ترامپ پیش مردم ایرانه چیه؟</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/22141" target="_blank">📅 23:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22140">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گزارش صدای انفجار یا پرتاب از سیریک
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/22140" target="_blank">📅 23:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22139">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">@WarRoom
سپر انسانی ۳</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/22139" target="_blank">📅 23:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22138">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">@WarRoom
سپر انسانی ۲</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/22138" target="_blank">📅 23:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22137">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">@WarRoom
سپر انسانی ۱</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/22137" target="_blank">📅 23:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22136">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ناو آبراهام لینکلن رسید پاتایا
🥴
😂
ناو هواپیمابر آبراهام لینکلن CVN72 پس از ۲۸۶ روز متوالی حضور در دریا و جنگ با ایران ، که یک رکورد مدرن برای نیروی دریایی ایالات متحده است، در تاریخ ۲ سپتامبر امروز به بندر لائم چابانگ تایلند رسید.انتظار می‌رود هزاران پرسنل…</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/22136" target="_blank">📅 23:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22135">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e37dc0a2d7.mp4?token=ENpJ0dPY569J0y6nbJRTQRwbg4qteqg8Sxcu-OOzKNbLHYUuyHRsma2tXUbr1kzdFPX62okw5PLTv1JnKekDESR6LHnj5JF_Kiocoh47_DGycmqIU2B8lZeMQ_fDTDYbtoMQePKNBn8QBIAkghylnZSPqFFSuuTreJPwdy7eDtXG-CHMx1mpmGhwxr-oH3BKlvbw5lWB9pZURIzLLB2mp9QkgV3krV394P6-ktSDfK_Gw8B88HVT68fmW9ypLjnRm6VdY6gwSW3Z8J0_9-laKfNLK4pwFp0OtNgpGQx_JtWMN9HlvpYa-gqILjwOzy6P6p9Pp2jrmz6QBEEuyKrEnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e37dc0a2d7.mp4?token=ENpJ0dPY569J0y6nbJRTQRwbg4qteqg8Sxcu-OOzKNbLHYUuyHRsma2tXUbr1kzdFPX62okw5PLTv1JnKekDESR6LHnj5JF_Kiocoh47_DGycmqIU2B8lZeMQ_fDTDYbtoMQePKNBn8QBIAkghylnZSPqFFSuuTreJPwdy7eDtXG-CHMx1mpmGhwxr-oH3BKlvbw5lWB9pZURIzLLB2mp9QkgV3krV394P6-ktSDfK_Gw8B88HVT68fmW9ypLjnRm6VdY6gwSW3Z8J0_9-laKfNLK4pwFp0OtNgpGQx_JtWMN9HlvpYa-gqILjwOzy6P6p9Pp2jrmz6QBEEuyKrEnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام می‌گوید نیروهای آمریکایی از زمان تشدید محاصره بنادر ایران، ۸۶ کشتی تجاری را تغییر مسیر داده‌اند، ۳ کشتی را از کار انداخته‌اند و ۲ کشتی را توقیف کرده‌اند تا از رعایت مقررات اطمینان حاصل کنند.
از زمان به‌روزرسانی دیروز، ۲ کشتی تغییر مسیر داده شده افزایش یافته است.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/22135" target="_blank">📅 23:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22134">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cee95e57f.mp4?token=VxrWTxGGYKEN69fb_7oT5GaIsovSWs-silvAno0zkb1SpDll6WntuCPcGxnOC9FMk9wbCo1pkx4Ltg39e6uArZq-MzfryzayPjBLm2h-3MNC2_BbylYByoqqkA7ZpMvcVoelbNdJAzYVva9Lb-t0Pm440iOrmbUXEA28p9sh9bhS4PBTst7FCA3u-1sOqAUzmLenXreDmJj_VIbfRenFbTYO36oCAKX_yHUd_VE9ZnYCsVLVc6_llxXFTaodGxKyBFpJIdHSDjT8BLFMjz8Zn7jgnFU8lqOUnD_HOJuHCH5Ux-Q0740t-E5Oy0fG4BMP79hKfAgSjNF-zVqLT4Gozw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cee95e57f.mp4?token=VxrWTxGGYKEN69fb_7oT5GaIsovSWs-silvAno0zkb1SpDll6WntuCPcGxnOC9FMk9wbCo1pkx4Ltg39e6uArZq-MzfryzayPjBLm2h-3MNC2_BbylYByoqqkA7ZpMvcVoelbNdJAzYVva9Lb-t0Pm440iOrmbUXEA28p9sh9bhS4PBTst7FCA3u-1sOqAUzmLenXreDmJj_VIbfRenFbTYO36oCAKX_yHUd_VE9ZnYCsVLVc6_llxXFTaodGxKyBFpJIdHSDjT8BLFMjz8Zn7jgnFU8lqOUnD_HOJuHCH5Ux-Q0740t-E5Oy0fG4BMP79hKfAgSjNF-zVqLT4Gozw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:به محض اینکه این [وضعیت] به پایان برسد، که فکر نمی‌کنم خیلی طول بکشد، نمی‌دانم آن‌ها چقدر دیگر می‌توانند مقاومت کنند.
من تحت تاثیر انتخابات قرار نمی‌گیرم. من نامزد نیستم. حزب من در انتخابات شرکت می‌کند و من به حزبم کمک خواهم کرد.به نظر من، حزب من به این واقعیت احترام می‌گذارد که ما اجازه نمی‌دهیم ایران سلاح هسته‌ای داشته باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/22134" target="_blank">📅 22:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22132">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e5dd427da.mp4?token=qrZNVeBRyoQR_PeMyWMQscG8TKJtzy1Z12HKd_fVmDa5cJdypiwikapKzyCgKymaT-2nxypRohRUPgHTcgTbMZ43DlXHBaQzoS28zFkYTRxqM87RU7F-xBECYs5BRtVE7dGFIeF4vtlHpKhvUNsUp3QH1lxp0qY0zH65Ex0dj1YSOSVoasSOBYEBjO3fenpsMrU994A5Co7BXHleGZrLe1yCk0WGyOu7kG3lm9lo0ybj5gthrNXylGNaja8HI8lMqLWeLveeRfLbFUgRbImgWalZ8XDVA818wP_U2L8FU_YIaY4URv3n-e8hteijDAokCyGD8N5VqkeBCFpxi1lU1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e5dd427da.mp4?token=qrZNVeBRyoQR_PeMyWMQscG8TKJtzy1Z12HKd_fVmDa5cJdypiwikapKzyCgKymaT-2nxypRohRUPgHTcgTbMZ43DlXHBaQzoS28zFkYTRxqM87RU7F-xBECYs5BRtVE7dGFIeF4vtlHpKhvUNsUp3QH1lxp0qY0zH65Ex0dj1YSOSVoasSOBYEBjO3fenpsMrU994A5Co7BXHleGZrLe1yCk0WGyOu7kG3lm9lo0ybj5gthrNXylGNaja8HI8lMqLWeLveeRfLbFUgRbImgWalZ8XDVA818wP_U2L8FU_YIaY4URv3n-e8hteijDAokCyGD8N5VqkeBCFpxi1lU1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران دیروز شب یک حمله بسیار سنگین بود و ما آماده‌ایم هر زمان که بخواهیم حمله دیگری را انجام دهیم.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/22132" target="_blank">📅 22:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22131">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">خبرنگار: آیا شما سازمان سیا را برای مسلح کردن ایرانیان اعزام خواهید کرد؟
ترامپ: من نمی‌خواهم این را به شما بگویم، مناسب نخواهد بود
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/22131" target="_blank">📅 22:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22130">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/22130" target="_blank">📅 22:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22129">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ درباره ایران: آماده حمله دیگری به ایران هستیم
ما تمام تجهیزات جدیدی را که آنها سعی در ساخت آنها در امتداد تنگه هرمز داشتند، برخی دفاعی و برخی تهاجمی، از بین بردیم.
آنها سعی می‌کردند کشتی‌ها را ببینند زیرا نمی‌توانند کشتی‌ها را ببینند.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/22129" target="_blank">📅 21:59 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22128">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cce539976.mp4?token=WRt6vKjqLWlVAraXMAB3cBXZ45kLm-BftmEYRraPF9M7efCoPi62Dt-Tx_BaPWJ1JVwUmUs26u8tvPBND-JtrXGNhYdVurl4BtWcNZg95gNucdTg8by5lbMaqiK5BwPQEr84G5mhMfY9jgjQIKpUf5XSS4uBCMraXEl41sjhby4FEpI-qTJD31R2MqPRxwiKckHgI5VjFOOGou3NG_yxuBxYl11vmQCSw52NProNs-Z6aE5a2c2AWc7GGiEX3OmZPZc-ak1ewqw4bfoP6TX5Oq-hfxRUFhwFa4g4Kk0oglt6w9Frd_IquzcOb_cWYMNrxw8fHtW-UKtluQM0k2VJZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cce539976.mp4?token=WRt6vKjqLWlVAraXMAB3cBXZ45kLm-BftmEYRraPF9M7efCoPi62Dt-Tx_BaPWJ1JVwUmUs26u8tvPBND-JtrXGNhYdVurl4BtWcNZg95gNucdTg8by5lbMaqiK5BwPQEr84G5mhMfY9jgjQIKpUf5XSS4uBCMraXEl41sjhby4FEpI-qTJD31R2MqPRxwiKckHgI5VjFOOGou3NG_yxuBxYl11vmQCSw52NProNs-Z6aE5a2c2AWc7GGiEX3OmZPZc-ak1ewqw4bfoP6TX5Oq-hfxRUFhwFa4g4Kk0oglt6w9Frd_IquzcOb_cWYMNrxw8fHtW-UKtluQM0k2VJZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران: ما هر کاری که آنها انجام می‌دهند را می‌بینیم.
آنها نمی‌توانند بدون اینکه ما ببینیم به دستشویی بروند.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22128" target="_blank">📅 21:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22127">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fdea0685f.mp4?token=lbOIipzD5moSdXmEpILtoUAl9V8OWRXUZTbuz7sAmDw__ZgZO3bzC02-OKVGZBArr3zHh9K_blOPgG_P8H0yKLMAyK-fEHuGgyhMiRscPQ1BEWfFdA558IXa4cXq_RMZ1cobB95fXbGKwZ64yZu30_lAMsfUqQlv_KM82jvEPNAvT5CB24BEDDUVPUAVX6FcL7aI1Jeu_oe0WiRFrI-5Dkx8CrgaobHT9I9hdjcEcdbJJiTZHyL7XIKr9k8WI-gRIvnTtB1pN_jg4MIXu7q5k3unVYrXjc4GvPqS-ldmGP8XXQmZCVPgGtc7_Z1UYyU2FxzugQgc5YWFRMaAQ6o1yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fdea0685f.mp4?token=lbOIipzD5moSdXmEpILtoUAl9V8OWRXUZTbuz7sAmDw__ZgZO3bzC02-OKVGZBArr3zHh9K_blOPgG_P8H0yKLMAyK-fEHuGgyhMiRscPQ1BEWfFdA558IXa4cXq_RMZ1cobB95fXbGKwZ64yZu30_lAMsfUqQlv_KM82jvEPNAvT5CB24BEDDUVPUAVX6FcL7aI1Jeu_oe0WiRFrI-5Dkx8CrgaobHT9I9hdjcEcdbJJiTZHyL7XIKr9k8WI-gRIvnTtB1pN_jg4MIXu7q5k3unVYrXjc4GvPqS-ldmGP8XXQmZCVPgGtc7_Z1UYyU2FxzugQgc5YWFRMaAQ6o1yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران : آن‌ها وقتی مردم برای اعتراض بیرون می‌آیند، آن‌ها را می‌کشند.
آن‌ها دقیقاً از بین چشم‌هایشان به آن‌ها شلیک می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22127" target="_blank">📅 21:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22126">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c3fbdc32.mp4?token=BnmgXmZjMaW2a73GURvF3BLrV-2Rv0DuLb9yx4WK0UJSXnxDPmoFP16Xf6rZCiKWSNXlpmvwvpv1paGCzZo_yKU7ppqrh7tTC-NVd0ko18Z9pWkfR5AjwJ0Pbs8ILlplxh6s94Wdo9h1S2j5pUV94GHtyCsfNs8f3chwq2Ykrc974VqYiVBAHaZMzNpzS8qzHcUsJVnzeVP1JGpU7zkga9LsDUDCHrzaD4I8ZuyIyMeWsiabCdGyWv6sRx19hk8vOYv8C1PHnl96gm42th-mmejausdJmRTPF61vmkT2hg5wdth3m-GAkbL2UFp-btVwvNuR8EohgtJVymeV6L1lTYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c3fbdc32.mp4?token=BnmgXmZjMaW2a73GURvF3BLrV-2Rv0DuLb9yx4WK0UJSXnxDPmoFP16Xf6rZCiKWSNXlpmvwvpv1paGCzZo_yKU7ppqrh7tTC-NVd0ko18Z9pWkfR5AjwJ0Pbs8ILlplxh6s94Wdo9h1S2j5pUV94GHtyCsfNs8f3chwq2Ykrc974VqYiVBAHaZMzNpzS8qzHcUsJVnzeVP1JGpU7zkga9LsDUDCHrzaD4I8ZuyIyMeWsiabCdGyWv6sRx19hk8vOYv8C1PHnl96gm42th-mmejausdJmRTPF61vmkT2hg5wdth3m-GAkbL2UFp-btVwvNuR8EohgtJVymeV6L1lTYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
تا سه ماه پیش، ۵۲,۰۰۰ معترض ایرانی کشته شده بودند. و حالا می‌شنوم که احتمالاً ۲۰ تا ۲۵ هزار نفر دیگر هم به این تعداد اضافه شده است.
تقریباً ۶۵,۰۰۰ معترض کشته شده‌اند. تنها پاسخ این است که به آن‌ها شلیک شده است.
رژیم هر روز ضعیف‌تر می‌شود و در نهایت به جایی خواهند رسید که دیگر نمی‌توانند به‌راحتی شلیک کنند، زیرا فکر می‌کنم مردم دیگر این موضوع را تحمل نخواهند کرد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22126" target="_blank">📅 21:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22125" target="_blank">📅 21:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">خبرگزاری i24 : در سایه تشدید تنش‌ها و بحران اقتصادی در ایران، سازمان اطلاعات سپاه پاسداران از احتمال وقوع دوباره اعتراضات هشدار می‌دهد. در همین حال، مقامات حکومت مدعی هستند: "آمریکا در تلاش است تا بی‌ثباتی داخلی ایجاد کند."
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22124" target="_blank">📅 21:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22123" target="_blank">📅 21:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22122" target="_blank">📅 21:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22121">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22121" target="_blank">📅 21:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22120">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">تقابل بختیاری زاده و تارتار برنده نداشت
پرسپولیس
1️⃣
-
1️⃣
استقلال
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22120" target="_blank">📅 21:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22119">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گزارش آژانس بین‌المللی انرژی اتمی:
از ماه فوریه، هیچ بازرسی از تاسیسات اعلام‌شده در ایران انجام نداده‌ایم، به جز تاسیسات بوشهر.
ما تأیید می‌کنیم که قادر به بررسی این موضوع نیستیم که آیا مواد هسته‌ای ایران به اهداف نظامی تغییر کاربری داده شده‌اند یا خیر.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/22119" target="_blank">📅 21:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22118">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا: یادداشت تفاهم با ایران منقضی شده است
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22118" target="_blank">📅 21:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22117">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گل اول استقلال به پرسپلیس
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22117" target="_blank">📅 20:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22116">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نتانیاهو
در گفت و گو با شبکه ۱۵ اسرائیل:
ایران را تسلیم خواهیم کرد و این رژیم سرنگون خواهد شد
و تمامی نهادهای ما برای تحقق این هدف تلاش می‌کنند.
وی اضافه کرد
ما می‌توانیم در هر لحظه به ایران حمله کنیم
و اگر آنها پاسخ دهند آخرین حمله آنها خواهد بود
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/22116" target="_blank">📅 20:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رویترز : مقام‌های آمریکایی می‌گن شرکت کشتیرانی دولتی چین، «کس کو»، روی کشتی‌هاش تجهیزات مخفی نصب کرده که می‌تونه ارتباطات نظامی رو رهگیری کنه و کشتی‌ها و هواپیماها رو در نزدیکی سواحل ردیابی کنه.
به گفته آمریکایی‌ها، این اطلاعات به پکن برای شناسایی و رصد نظامی، هشدار زودهنگام و اختلافات ارضی کمک می‌کنه.
چین این ادعاها رو رد کرده و گفته کاملاً بی‌اساسن.
﻿
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22115" target="_blank">📅 20:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">مسئولان در دستگاه‌های امنیتی اسرائیل:
ما هیچ اطلاعاتی در اختیار نداریم که نشان دهد ایران برنامه‌ای برای حمله به ما در تعطیلات یهودی دارد، همانطور که آقای کاتس گفته است
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22114" target="_blank">📅 20:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22113">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eabf8dc5a2.mp4?token=ILTdHeqonGEegkH9Mkp4Jo5J37Rz7Ymf55MkZ5ZPBVf1-74lgd2Zz61a5X25zUwqYQTn7MXKH3nNy4o9cM2gYtdOwPkFKOtWnpSrpR6ngEyt0w0MbtifwOWvLMBdjudxfnXvQi0u3Kz60au4H5eDggORxv7N58P8ETILcrGmQcygtBfh80-ZCoaqsnZeKTa3vf-tABfGQB7eUNT3y016nlMAREHD_44bmYqxMBR2BtD7p1K_nkCJxLmwyko1mp7y0hRZHZaKk5Uo54eaKW_ffm88ffuR0L51YNvVTd284TUcpdjG_9ycZ9mFJKDxz6xOUtI48xa4VYaKXvw-zmnIjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eabf8dc5a2.mp4?token=ILTdHeqonGEegkH9Mkp4Jo5J37Rz7Ymf55MkZ5ZPBVf1-74lgd2Zz61a5X25zUwqYQTn7MXKH3nNy4o9cM2gYtdOwPkFKOtWnpSrpR6ngEyt0w0MbtifwOWvLMBdjudxfnXvQi0u3Kz60au4H5eDggORxv7N58P8ETILcrGmQcygtBfh80-ZCoaqsnZeKTa3vf-tABfGQB7eUNT3y016nlMAREHD_44bmYqxMBR2BtD7p1K_nkCJxLmwyko1mp7y0hRZHZaKk5Uo54eaKW_ffm88ffuR0L51YNvVTd284TUcpdjG_9ycZ9mFJKDxz6xOUtI48xa4VYaKXvw-zmnIjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راننده جنسیسی که تجمعات مشهد رو زیر گرفت: خدا شاهده عمدی نبود، از تعادل خارج شدم و وقتی به یه نفر برخورد کردم دچار تشنج شدم و بجای اینکه ترمز بگیرم، گاز دادم و یه دفعه همه رو زیر گرفتم.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/22113" target="_blank">📅 19:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">مارکو روبیو درباره ایران: هیچ کشوری نباید به ایران در دور زدن تحریم‌ها کمک کند. هیچ کشوری نباید به آنها در ایجاد سازوکارهایی که بتوانند از طریق آنها درآمد کسب کنند و سپس از آنها برای حمایت از تروریسم و ​​تلاش برای ساخت سلاح هسته‌ای استفاده کنند، کمک کند. و…</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22112" target="_blank">📅 19:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1b1fd93ee.mp4?token=Po7b3V3-Ek1ymfNzM1QoBte26U8eo7KHdTP5CWeU9QhibMbUilBWZ0__mdvZ2-XmWt8NQvCGzjXwN9VyB863eCtP2iGnjWJkqkluOE2ApgRdVXOUvVDjFLkTnv91SC0Snldd6zYHYBbeBCQakuaklhwxY5LwKYVcUtxaDNtMTLdGvWaldSOPuo30ZvNidr9qGl9k95InEvo1HhQvdpodcc7_guJ2rqrd6dW6SGlQnm6vyHL6B-Nr4t-HqMv5E2L8IbD2WW2lygY7ScivfQgQQQDsz8Pt4xv1GUgVjRDpKw1s-ihHx5dRLhYZRCftvhkcx8ZaaezHiRFh16jwVgQ-6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1b1fd93ee.mp4?token=Po7b3V3-Ek1ymfNzM1QoBte26U8eo7KHdTP5CWeU9QhibMbUilBWZ0__mdvZ2-XmWt8NQvCGzjXwN9VyB863eCtP2iGnjWJkqkluOE2ApgRdVXOUvVDjFLkTnv91SC0Snldd6zYHYBbeBCQakuaklhwxY5LwKYVcUtxaDNtMTLdGvWaldSOPuo30ZvNidr9qGl9k95InEvo1HhQvdpodcc7_guJ2rqrd6dW6SGlQnm6vyHL6B-Nr4t-HqMv5E2L8IbD2WW2lygY7ScivfQgQQQDsz8Pt4xv1GUgVjRDpKw1s-ihHx5dRLhYZRCftvhkcx8ZaaezHiRFh16jwVgQ-6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو درباره ایران: هیچ کشوری نباید به ایران در دور زدن تحریم‌ها کمک کند. هیچ کشوری نباید به آنها در ایجاد سازوکارهایی که بتوانند از طریق آنها درآمد کسب کنند و سپس از آنها برای حمایت از تروریسم و ​​تلاش برای ساخت سلاح هسته‌ای استفاده کنند، کمک کند.
و اگر کشورها تصمیم به انجام این کار بگیرند، ما نیز باید آنها را تحریم کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22111" target="_blank">📅 19:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مسئول مرکز ایثارگران سپاه فجر فارس اعلام کرد:
حدود ساعت یک بامداد امروز، سه‌شنبه ۱۱ شهریور ، یک راننده بیل مکانیکی از نیروهای قرارگاه خاتم‌ و بسیجیان سه پا ناحیه فسا که در پروژه‌های عمرانی شهرستان جهرم مشغول فعالیت بود، در پی حمله آمریکا به این شهرستان کشته شد.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22110" target="_blank">📅 19:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCBa8y0tIwCQpgbI6ILN-zWWxyfRO6BYss0-tfsBaeVII1AOZe1rnpZQ-tFoUMJ59Pt537tiL1fskACsrADqSsmY2QynlIgdyuxuIDTixsplUBWhw-O2NdBGTowo9mbucgu4XK4otCrBy-pmiJeKX9vnO39vTYft9xJZycguvZigP8TQ6U6P6TyrwiVskgEQ9Z7iBscw3SpqFMxHHrIb_F_61Mvj0GUzRyrz4tjvn21k7UtTj0ICJvJAGZBkla790OlENALK_InFMojfjVzDnHlkDT0_cOID-14NL_AeH6zSlLKWQdw4g2qi6fNmgQj4aWOLzCHe3rj3746MlxZMoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
ترامپ در تروث :
اکنون که این منطقه تحت کنترل ایالات متحده قرار دارد، آیا باید نام تنگه هرمز را به «تنگه ترامپ» تغییر دهیم؟
درست مانند خود آمریکا، این منطقه از همیشه «داغ‌تر» خواهد بود!
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22109" target="_blank">📅 19:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a3b32fad2.mp4?token=MukLS1um51-tcuOH0jEA-JOZp-YMj17iL4SpLdhaxyF-qhv_vcF8oVvcg46cV7RFJSpnHRS1nR_2qgQ-X2vjXOrYu7Dvx6kRZL0iuvmsA_0xBdAnAW4wPXfhio-dOT59sqzoRQfZ5a7O0rUuyFs9g791lqE5aJ1cCedrnvZaPH0SOZivgOnn7fGUU1XAUQuYPDkSafZwNcLosajF8EuvnF3e0ZAqYnFfZq9ac9wD5ylapeCsEWtA7rh-Y80o9qSiBSiBYxav3LFNR_ASVMEHM0rQb-SQGhCSYPxgH5ZXgZfBqm2Op0TbM9RXJHIXlCQQfdpXqaT0KJvfgL_M_CcOag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a3b32fad2.mp4?token=MukLS1um51-tcuOH0jEA-JOZp-YMj17iL4SpLdhaxyF-qhv_vcF8oVvcg46cV7RFJSpnHRS1nR_2qgQ-X2vjXOrYu7Dvx6kRZL0iuvmsA_0xBdAnAW4wPXfhio-dOT59sqzoRQfZ5a7O0rUuyFs9g791lqE5aJ1cCedrnvZaPH0SOZivgOnn7fGUU1XAUQuYPDkSafZwNcLosajF8EuvnF3e0ZAqYnFfZq9ac9wD5ylapeCsEWtA7rh-Y80o9qSiBSiBYxav3LFNR_ASVMEHM0rQb-SQGhCSYPxgH5ZXgZfBqm2Op0TbM9RXJHIXlCQQfdpXqaT0KJvfgL_M_CcOag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ درباره ایران: ما الان کنترل تنگه هرمز رو در دست داریم. کنترلش می‌کنیم.
دیشب ۲۸ تا قایق، ۲۸ تا شناور رو از بین بردیم. ما تنگه رو تحت کنترل داریم؛ اونا دیگه چیزی گیرشون نمیاد و ما چندین شناور رو هم زدیم.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22108" target="_blank">📅 19:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3543df88e.mp4?token=NRt42UoTpSslzyI_j6qGmdB5pLustT-oHWA-FzYqxA7TdOIWQOplhKUkUyYa5E8YpwmE6skJgHSEuiymBPM03u6I_JR-4o-0cYUWk02m19ScLAXM7jwnVzzdNJTAT6eRJll-3z2ie5N7u7IkWdZWlzAHN8QSslm-Tx5kPnSeTPOcXeknvedxjZUEPlLVynIosXs1jfXPQfW2B9mFLu8m4PQ9iQTTBUm7jUO7RGaKoAz1tIneCRFnthCr2Yi55oW6dhNWJgJmOAUG4D2oS_EX7OSfv7Xfc2dHd57xzp6vyKUSYY7Lgz-sd--wl4GXJYSoPdO9Y6tZ_ly2LlKw5Erzaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3543df88e.mp4?token=NRt42UoTpSslzyI_j6qGmdB5pLustT-oHWA-FzYqxA7TdOIWQOplhKUkUyYa5E8YpwmE6skJgHSEuiymBPM03u6I_JR-4o-0cYUWk02m19ScLAXM7jwnVzzdNJTAT6eRJll-3z2ie5N7u7IkWdZWlzAHN8QSslm-Tx5kPnSeTPOcXeknvedxjZUEPlLVynIosXs1jfXPQfW2B9mFLu8m4PQ9iQTTBUm7jUO7RGaKoAz1tIneCRFnthCr2Yi55oW6dhNWJgJmOAUG4D2oS_EX7OSfv7Xfc2dHd57xzp6vyKUSYY7Lgz-sd--wl4GXJYSoPdO9Y6tZ_ly2LlKw5Erzaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ درباره ایران:
من به مردمم گفتم: "ما باید در جایی به نام ایران، جمهوری اسلامی ایران، متوقف شویم و باید آنها را از داشتن سلاح هسته‌ای بازداریم."
شما می‌خواهید مشکلی ببینید؟ بگذارید آنها سلاح هسته‌ای داشته باشند. شما نیمی از جهان را نابود خواهید کرد. آنها بیمار هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22107" target="_blank">📅 18:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">صدای انفجارهایی در کشور کویت شنیده شد که از استان بصره عراق نیز قابل شنیدن بوده
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22106" target="_blank">📅 18:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مارکو روبیو: ایالات متحده به هدف قرار دادن ایران در واکنش به حملات علیه کشتی‌ها ادامه خواهد داد
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22105" target="_blank">📅 18:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22104">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مقام اسرائیلی:تلاش برای دستیابی به توافق امنیتی با سوریه شکست خورد.
تمایل سوریه برای دستیابی به توافق با اسرائیل پس از لغو برخی تحریم‌ها علیه دمشق کاهش یافته است.
کانال‌های ارتباطی با دولت سوریه همچنان برقرار هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/22104" target="_blank">📅 18:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نرخ دلار ۲۲۱،۵۰۰ تومان(سقف تاریخی)
دلار کف بازار :۲۲۵-۲۲۷ هزار تومان!
تتر ۲۱۹،۰۵۲ تومان (سقف تاریخی)
بیتکوین ۷۷،۳۴۰ $
انس جهانی طلا ۴،۳۸۵ $
نفت برنت  ۹۴،۵۰$
@WarRoom
🚨
🚨
🚨
🚨
۶ عصر تهران</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/22103" target="_blank">📅 18:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">نیویورک تایمز: امشب می‌تواند بدتر از دیشب باشد فقط باید منتظر ماند!
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/22102" target="_blank">📅 17:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">خبر زنده فاکس نیوز:
ترامپ ممکن است امشب دستور حمله مجدد بدهد
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/22101" target="_blank">📅 17:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22100">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سه پا نبی اکرم کرمانشاه در بیانیه‌ای اعلام کرد:
شب گذشته 4 پرسنل نیروی هوافضای این استان در پی حمله ارتش آمریکا به لانچر موشک بالستیک کشته شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/22100" target="_blank">📅 16:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22099">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCjDr0anrOTzjYxTizJmP9a_lLTbAZiXu1yNyWYj5JBEzVX4HXH7S261CI6YnRhi-r2vKIjb3YzjTzJ3SRTOfEkiw0QtUJSylITgQquGBwgszRwX_K_V_RVc0aVoNXC0lxxLg6GyONCPxFIFK3NoAQJqw4Ij2ONnvGXeInBHntsr3oXOSU_hOT3N-gqD8HLgTDtrvtZV7oLNeb-kJnYgqnIkPR6eQbe3T97W8RDVGGz7szKNQ7Z1K5foPYM3Hg2OiVKLVziFOWCs3fcDs2LaKyPVxnWiUi21N9xC1qn3kHzqXuyADNhVzxfnVG-g9hU3TEOMUvf-q6QJhyC0xPGpHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیجیکالا داره تتر میفروشه چهارقسطه
16 هزار تومن بالاتر از قیمت 215 تومن.
تتر قسطی دیگه چیه ؟! جیانکارلو دواسینی میگن دو تا سکته رد کرد بعد دیدن این پست
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/22099" target="_blank">📅 16:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سازمان تجارت دریایی بریتانیا (UKMTO) از وقوع یک حادثه امنیتی مرتبط با یک نفتکش خبر داد که در پی آن دو نفر کشته یا زخمی شده‌اند و این حادثه در حال بررسی است. @WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22098" target="_blank">📅 16:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22097">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/542ffb7905.mp4?token=ACnQtKSNGSEbKeJXo04Jusb6e2aMoPZxjKx54FTkHJCPG2DcHeKZNKXRY0D2gTpZ5M1ThEfGjJjXPWGOp58UvRfzFG8_ps3t9MrWm7yGXNHyrneaerDfC1r-PWlKtJQxoXwC1vQMPeQ_scPkSquTkTnBYDScGg74uiIouS5BGruY_iYWz-OhKI0WZBrw6M4UiMrAF7ByYWvqoOcHFj3VjoUHXlywwuTK6F6g9VU63X4oULKnEmQyS9Oluwy-BNTj9t7L4ZU_jLSdRIbmwOlsIb5dOJ9aWa-jW7EYWX3rnDBKU9h_13Ndp1xheC6iGHwbCcbifdblSvJTyFzF56WAyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/542ffb7905.mp4?token=ACnQtKSNGSEbKeJXo04Jusb6e2aMoPZxjKx54FTkHJCPG2DcHeKZNKXRY0D2gTpZ5M1ThEfGjJjXPWGOp58UvRfzFG8_ps3t9MrWm7yGXNHyrneaerDfC1r-PWlKtJQxoXwC1vQMPeQ_scPkSquTkTnBYDScGg74uiIouS5BGruY_iYWz-OhKI0WZBrw6M4UiMrAF7ByYWvqoOcHFj3VjoUHXlywwuTK6F6g9VU63X4oULKnEmQyS9Oluwy-BNTj9t7L4ZU_jLSdRIbmwOlsIb5dOJ9aWa-jW7EYWX3rnDBKU9h_13Ndp1xheC6iGHwbCcbifdblSvJTyFzF56WAyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بسنت درباره ایران :
«ما اختیارات جدیدی برای وزارت خزانه‌داری ایجاد کرده‌ایم تا بتواند در حوزه‌های
هوانوردی، دریانوردی و دارایی‌های دیجیتال
تحریم‌هایی اعمال کند.»
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22097" target="_blank">📅 16:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22095">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfe871b13a.mp4?token=i6_O6KeMRTgYRfmnIQMfRHkUA4fuSzNB-m1njXm6EAbiW0c9DQCJJ7GJMerJ014TeekDrDs2VX6P2FtUCgU9F5OS9U4jC45B6AlAL5FwnnJ1Smrhfo6vbQ0hC38E9HufykqzT3mW48sout2hceY8NlVlHyjG7V7QmyTfqCQPc1Ska5ChlQ0Le3pfTgZIqBcChQ-Z7lyd-t8JabwKI6DxJXu9AB3hBMz2FYOycKwUs9AkmFI5PG26KL0Yq8pxrM2KoIs4xckLIN_gslGjMtycsAsrwIUOAQZI6N4ljRsEYGLO1WP-_5Aa_Y0Z03uys0OsKz8bTpa6Vw9-q-RePZWsLobMQLgqd2qfLaFqXthlgN9YNn8mkAmjq0auSVkG1wjZW1Dahw7EHNQdrx53RsoF9pv-bqZ-3fu-_6mTQ89YwsM4uxucbVioUqV9q_kIqATSGcJqadMhs9cp5hIS7IQPTpGEchvSe5OQYRzZ-Ujwo8DDn3s3XOeLA3VDMBLVUCZ0RbgnV6cRIwB-U0f_pYr3ze4YFDg0dOiyip8L8tBDfi5NYFyvV-Ur8Fb7oiLZSv21JqOMLX2i7kItAgVcSPvh7W99YSB_vLqVSxC_dDtP4ShGecuKC1VtxbaLNDif3Lg1m80_eX4zl-GT6KndPGTqmMxzunux4KOPKNuaF-S247Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfe871b13a.mp4?token=i6_O6KeMRTgYRfmnIQMfRHkUA4fuSzNB-m1njXm6EAbiW0c9DQCJJ7GJMerJ014TeekDrDs2VX6P2FtUCgU9F5OS9U4jC45B6AlAL5FwnnJ1Smrhfo6vbQ0hC38E9HufykqzT3mW48sout2hceY8NlVlHyjG7V7QmyTfqCQPc1Ska5ChlQ0Le3pfTgZIqBcChQ-Z7lyd-t8JabwKI6DxJXu9AB3hBMz2FYOycKwUs9AkmFI5PG26KL0Yq8pxrM2KoIs4xckLIN_gslGjMtycsAsrwIUOAQZI6N4ljRsEYGLO1WP-_5Aa_Y0Z03uys0OsKz8bTpa6Vw9-q-RePZWsLobMQLgqd2qfLaFqXthlgN9YNn8mkAmjq0auSVkG1wjZW1Dahw7EHNQdrx53RsoF9pv-bqZ-3fu-_6mTQ89YwsM4uxucbVioUqV9q_kIqATSGcJqadMhs9cp5hIS7IQPTpGEchvSe5OQYRzZ-Ujwo8DDn3s3XOeLA3VDMBLVUCZ0RbgnV6cRIwB-U0f_pYr3ze4YFDg0dOiyip8L8tBDfi5NYFyvV-Ur8Fb7oiLZSv21JqOMLX2i7kItAgVcSPvh7W99YSB_vLqVSxC_dDtP4ShGecuKC1VtxbaLNDif3Lg1m80_eX4zl-GT6KndPGTqmMxzunux4KOPKNuaF-S247Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری فاکس نیوز
:
پوتین عملاً به ایران گفت: «ما پشت شما هستیم.» پیام شما به روس‌ها چیست؟
بسنت
:
«پیام من به همه این است:
دور بمانید.
»
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22095" target="_blank">📅 16:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22094">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHWQkv6ObtiVJVVUG1fWcRFAjSnH7josMSuhjhAgRHSR9WjJEGnWvqHmGkzTMsPoFuwXUobnMtlDY_pnVzkx2rJwhQofMVioJszAd3IwMesR5ex9BroNZl5-n102J6Ex0kuSDRF7DIkO8r2o7oGlltnnrbIf5ZGdHF4WkpTdFduAYooHVweBWO4RikXru5o2Y1TenqoZU0xmberR5vKp_WAOL2GcXz8u1ipZA4vCsO-t_eA14TiJO3ibO99s-VpSqpZ1HweLg-8MfluTgyv3-x2cZSp4YgQI7HOtgtWQu_pV9v-_bAp5eD9Hh-mc8wdlzHBm_zWOnP7P22fEBTj23w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان تجارت دریایی بریتانیا (UKMTO) از وقوع یک حادثه امنیتی مرتبط با یک نفتکش خبر داد که در پی آن دو نفر کشته یا زخمی شده‌اند و این حادثه در حال بررسی است.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/22094" target="_blank">📅 15:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22093">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">هواپیمای پزشکیان گاز کش درحال بازگشت به کشور  @WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22093" target="_blank">📅 15:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22092">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ در تروث : من آن‌طور که ای‌بی‌سی نیوز جعلی گزارش کرده، تلاش نمی‌کنم ایران را به پای میز مذاکره بکشانم. برایم هیچ اهمیتی ندارد که آنها توافقی بی‌ارزش را امضا کنند؛ توافقی که برای خودشان هم بی‌ارزش است. من موضع کنونی‌مان را بسیار بیشتر می‌پسندم؛ با کنترل…</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/22092" target="_blank">📅 15:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22091">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گزارش صداوسیما: تنگۀ هرمز همچنان بسته است و کشتی‌های مختلف هدف قرار می‌گیرند
گزارش خبرنگار شبکه سه از جزیره لارک؛ جزیره‌ای که هدف حمله آمریکا قرار گرفت و در پی آن تعدادی از نیروهای نیروی دریایی سه پا کشته و زخمی‌شدن‌
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/22091" target="_blank">📅 14:56 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22090">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoh</strong></div>
<div class="tg-text">داداش ما بانكوك رسيديم تازه بريم واسه قدر دانى از بچه ها ابرام؟</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/22090" target="_blank">📅 14:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22089">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">مارک لوین : ترامپ  اکنون در حال خفه کردن دشمنه ( رژیم ایران )
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/22089" target="_blank">📅 14:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22088">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ناو آبراهام لینکلن رسید پاتایا
🥴
😂
ناو هواپیمابر آبراهام لینکلن CVN72 پس از ۲۸۶ روز متوالی حضور در دریا و جنگ با ایران ، که یک رکورد مدرن برای نیروی دریایی ایالات متحده است، در تاریخ ۲ سپتامبر امروز به بندر لائم چابانگ تایلند رسید.انتظار می‌رود هزاران پرسنل از پاتایا، شهری در نزدیکی این مکان، بازدید کنند
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/22088" target="_blank">📅 13:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22087">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نرخ دلار ۲۲۰،۰۰۰ تومان(سقف تاریخی)
دلار کف بازار :نامعلوم ! تونستی بخر!
تتر ۲۱۸،۰۰۰ تومان (سقف تاریخی)
بیتکوین ۷۷،۲۴۸ $
انس جهانی طلا ۴،۳۲۱ $
نفت برنت  ۹۴،۹۱$
@WarRoom
🚨
🚨
🚨
🚨
۱۲ ظهر تهران</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/22087" target="_blank">📅 12:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22086">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز، در مورد ایران:
احتمال حمله ایران به اسرائیل وجود دارد ! میگین چرا؟ برای فرار از منطقه!
بین محاصره و جنگ، آنها ممکن است دومی را ترجیح دهند.
ما برای این کار آماده‌ایم، به خصوص که در فصل تعطیلات هستیم.
آنها دوست دارند در تعطیلات یهودیان حمله کنند زیرا از یهودیان متنفرند.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/22086" target="_blank">📅 12:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22085">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iu0tP_frilVIBSTNVJjcwWCl0pYBRe9bfpbm-hVlh2zqwOiwo1k8wQIJ4S0vyAenlhx6UMlfgPzfdADk50xEKj6fUrD_HBQHUWTgAb2k9S514R93HuuaULTS00qkgD5C0FvZKCr-ZZXv3-4jM1UFfMD8QfXQgC2vMp6fixfb-H2ZgiM71yYew_d9F4VttU2d2uiuCg0ZMlaezCT0Pbi_XFLXxkSprm3qLfW6ij2Q23Luo00Z-d_DLbw5q4LkIvvkixj_qB5ses6c17-TXdQajumkOTdhHNBgthWcoUhUsQX00I_M64Ms0CXDfHd_p_wlwv2SqmSAomXzszhY_UJzeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاصله حدود ۱۳۶ متری بین دکل مخابراتی و محل عروسی در کوهستک سیریک
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/22085" target="_blank">📅 11:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22084">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">وزیر دفاع اسرائیل: با آمریکا برای دفاع و حمله هماهنگی کامل داریم.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/22084" target="_blank">📅 11:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22083">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdLnl_a0iCgC4Zy0h8fEggx2ZAALzxLmijHq9D7wlmKwULGZQD_y3Xtqbemtwo4xKKREQjydv0iGsOSkgyTxb_ro8VCVyccbgVZId-ckRvALDRTM1XNg4Ap9K2y6syA7YRiEH4yynXYQWFQW7cTmBUb7Z-6GIAH4_ioGfSNtaVdfCitZH9NjCD0RAmQvILe8r8Fsc41JIkBHhX20f9gYquLlWNwSYb59596WThTjbrgH_ohx8RCwurnRiCGR0QAi1neei--3Xt6S_AGoJ8AoUzPHdRefWvge_SUNY7HE3txYokgYSxbYN5562wcfSJuGijxQUtReoLh6RP6aOtsUhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون ستون دود ارومیه
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/22083" target="_blank">📅 10:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22082">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">۳ بسیجی شهرستان دیر درجزیره لاوان کشته
شدند
جانشین فرمانده سه پا سیدالشهدا شهرستان دیّر:در این تهاجم، «مهدی بحرانی»، «حسین صالح‌نژاد» و «حسن مؤمنی» کشته و تعدادی دیگر از نیروهای مدافع امنیت شهرستان دیّر نیز مجروح شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/22082" target="_blank">📅 10:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22081">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">رسانه های رژیم : سپاه کدام پایگاه‌های آمریکایی را هدف قرار داد؟
1⃣
کمپ تیتین در اردن
حمله سنگین موشکی؛ هدف‌گیری نیروها، تأسیسات و بالگردهای آمریکایی. تسنیم مدعی کشته‌شدن نیروها و انهدام تأسیسات و بالگردهاست.
2⃣
پایگاه پرنس حسن در اردن
حمله سنگین موشکی؛ هدف‌گیری پهپادهای RQ-4 و MQ-9 و زیرساخت‌های فنی. تسنیم مدعی انهدام پهپادها و آسیب به تأسیسات است.
3⃣
پایگاه‌های آمریکا در اربیل عراق
حمله ترکیبی موشکی و پهپادی؛ هدف‌گیری مراکز تعمیراتی، انبارها، سامانه بالن جاسوسی و مخازن سوخت. تسنیم مدعی انهدام و آتش‌سوزی و کشته‌شدن نیروهاست.
4⃣
پایگاه علی‌السالم در کویت
حمله ترکیبی موشکی و پهپادی؛ هدف‌گیری قرارگاه، آشیانه و محل استقرار پهپادها. تسنیم مدعی کشته‌شدن نیروها و انهدام پهپادها و تأسیسات است.
5⃣
پایگاه نیروی دریایی آمریکا در بحرین
حمله ترکیبی موشکی و پهپادی؛ جزئیات کامل درباره نتایج حمله هنوز اعلام نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/22081" target="_blank">📅 10:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22080">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lE8VNPUoz0U_XiWMGbn5vJ2NqDxd4CPQUJnu2c-PJIa_muAHsH7vxeRAqPc6yqyhGmJYQNbMxqFEvfr55igUoqhi4TY4a7pXOURtpra0BeMAIpeGoJjRrvQA5XN_vzUeMsw5XUcuz459qnjVx9uFdTmuURgjTFELwA7x3BOXInFz_k-Ll_RTYtv7_4nd9G82a-V_JJ8lm1OBCBRgD4-T8cBMjG_ojzCdBwhuxRXFvcYf4RrIY3WlFXcPsomc_ggkncD3bLZkprc4q2LV2cucorKBeLvL-PyeBOIy6Jf1l0AQXwbKziyjXmVv_pR4-jL9eg8cxYaeVuGOpHmC1piPtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مناطقی که سه پا ادعا میکنه در ۳ روز اخیر مورد هدف قرار داده.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/22080" target="_blank">📅 10:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22079">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سه پا:
نیروهای انقلاب اسلامی بامداد امروز، یک حمله موشکی و پهپادی را علیه پایگاه آمریکایی "علی السالم" در کویت انجام دادند. این اقدام در واکنش به بمباران یک منزل مسکونی در "سیریک" صورت گرفت که منجر به شهادت ۴ نفر و زخمی شدن حدود ۷۰ نفر دیگر شد. این حمله، مقر و محل اقامت فرمانده پایگاه را هدف قرار داد
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/22079" target="_blank">📅 09:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22078">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a6fc9a16f.mp4?token=KLKkmIzo3i7UAmP0ugdPTnNdxlzl7B50vwUid00KVwkuu5DqkypyOxnWQSQBRTrxkKUaKd6mHFaowJUfPhTjdIDwEAFaLuOJfY3ksw3V1toiddDju4ueBiTjVnTtGBeMgXe-MOtsBfa96uZAFW9l6RYfQXukcv921u7rZPbBseovnUmvN4Bf335zA7PgorohkqxnpfNkdp8qLWdFFigE4KUneWw1VwuGuYSFWaT_8KhvDyGqllBLCrHHVAqq1rWFtZ76sJdnERMBlVPBFUaXxQFR-jA_DSArN4uqjR32iadYARAUbEsbzRhcBUzyU5sBSa4ita77stUZj-K6MIk2ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a6fc9a16f.mp4?token=KLKkmIzo3i7UAmP0ugdPTnNdxlzl7B50vwUid00KVwkuu5DqkypyOxnWQSQBRTrxkKUaKd6mHFaowJUfPhTjdIDwEAFaLuOJfY3ksw3V1toiddDju4ueBiTjVnTtGBeMgXe-MOtsBfa96uZAFW9l6RYfQXukcv921u7rZPbBseovnUmvN4Bf335zA7PgorohkqxnpfNkdp8qLWdFFigE4KUneWw1VwuGuYSFWaT_8KhvDyGqllBLCrHHVAqq1rWFtZ76sJdnERMBlVPBFUaXxQFR-jA_DSArN4uqjR32iadYARAUbEsbzRhcBUzyU5sBSa4ita77stUZj-K6MIk2ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیلاخ چین به رژیم و ۴ شرط برای سفر قالیباف به پکن
حسین مرعشی، دبیرکل حزب کارگزاران:
چین سفر قالیباف به پکن و گسترش روابط تهران-پکن را مشروط به موارد زیر کرده است:
۱. باز کردن تنگه هرمز توسط ایران
۲. دریافت نکردن هیچ‌گونه عوارضی
۳. پایان دادن به اختلافات با عربستان
۴. پایان دادن به اختلافات با آمریکا
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/22078" target="_blank">📅 09:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22077">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">روابط عمومی استانداری هرمزگان:
«امیرعلی کریمی» چهار ساله، «محمد ملاحی» ۱۶ ساله، «کلثوم ملاحی نژندنیا» ۴۳ ساله و «زرخاتون طاهری» ۵۰ ساله، اسامی چهار شهید حمله دیشب به شهرستان سیریک می‌باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/22077" target="_blank">📅 09:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22076">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1WMnKdaxltK6IA4FB_vqQdB7TYq1hhYGCsCntt2bnsxts_q2IyIRQPiN2NBG3-qKH8FxSt976boVAA8GqrQSdaZQjwz8IMWyCXT-RCh4ASUmCFT3YTqs5Z95aIOmxWTlpM0L9BLKKJGvMgPneLYZIp_BiC3Ex3vtnOqUebM-3fza8sGyMgYCBfMbGa2BitT8FOp9OQPLmBQU3eitlwZjIRw2VEhCJGAmQ0GysKZ4-taYFOhDJh-WxQLXMDs0Sac1EpFFFhgzNT5YYrtxUnaZXBv6-cfSn-_40mUS3gawsFnufD3bhNfa5xblyZgML1TryujcgJ0EE7X4Ds-zBftiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : من آن‌طور که ای‌بی‌سی نیوز جعلی گزارش کرده، تلاش نمی‌کنم ایران را به پای میز مذاکره بکشانم. برایم هیچ اهمیتی ندارد که آنها توافقی بی‌ارزش را امضا کنند؛ توافقی که برای خودشان هم بی‌ارزش است. من موضع کنونی‌مان را بسیار بیشتر می‌پسندم؛ با کنترل تقریباً کامل بر تنگه هرمز و اقتصادی که در حال فروپاشی کامل است. آنها فقط دارند اجتناب‌ناپذیر را به تعویق می‌اندازند.
مردم ایران قرار است چه زمانی قیام کنند و بجنگند؟
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/22076" target="_blank">📅 09:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22075">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qg59jHIfHMVOgayg1FNbXkXh9a4ffVtNXDVai288H7SPix-o4N42ifrOOPBpWPpOQ_3wqqEXHEQXULhn786XDERU6aPUYcZPxlhVTysSnysOA479Odm3kwzxMM0A53E1-L5F7_C8Lz0SkqnHZG52JgDP9FfQe0PyLGVV5PtaiZqIGslUdd9EINsG5KXQR_uI_Alb97x_P4Pjbv6OG0r9k9UH_x95SaI3iLzW-KmLR7x-ve7bpRlUtTeZM_d9yAgTIAjiPEVrnculd-X9EQAX6hxgFxovzafqMMoYoFS11S9FWVAp4TGX1-2F8oC5vrxFT1Q7-oc8QCZnVCKywgAMMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکنون ۶ هواپیما تانکر سوخترسان در محدوده تنگه هرمز به جنگنده های آمریکایی در عملیات علیه ایران مانند پمپ بنزین های هوایی خدمات میدهند
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/22075" target="_blank">📅 09:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22074">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ : نمی‌خواهم ایران را به میز مذاکره بیاورم
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/22074" target="_blank">📅 09:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22073">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">آکسیوس: ترامپ دستور حمله به نفتکش‌های ایرانی را صادر کرده است
آکسیوس به نقل از مقام‌های آمریکایی گزارش داد ارتش آمریکا روز سه‌شنبه دو نفتکش ایرانی را در نزدیکی سواحل ایران، در شمال خط محاصره دریایی آمریکا، هدف قرار داده است. پهپادهای آمریکایی با شلیک موشک به موتورخانه این دو نفتکش حمله کردند؛ اقدامی که نخستین هدف قرار دادن مستقیم نفتکش‌های ایرانی از سوی واشنگتن در واکنش به حملات علیه کشتی‌های عبوری از تنگه هرمز محسوب می‌شود. این اقدام بخشی از سیاست جدید دولت ترامپ با عنوان «نفتکش در برابر نفتکش» برای افزایش فشار و بازدارندگی در برابر ایران است
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/22073" target="_blank">📅 08:59 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22072">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دیدبان اتاق جنگ : اهواز همین الان پهباد شاهد بالا سرمه @WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/22072" target="_blank">📅 03:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22071">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86022269b5.mp4?token=aHwV9kCzvdMxVl_8Ja9zK15bqiaAHMHiGEwY_Pp5VAIXLH-msk2hNGNOGlKtiBamO_jEPQlRMuKQcYqsl9NbKPmWO7TP0aM-44C8LyL7b0xfd6k_fPC8h-LCjiIJL0Qw2HNcTfF8hoK22KEFgg_o7bozdD3lpx-xNsFyQuzdy-W_3jVHcYCV0FIUrfClFbWUt89PJLsGL1vGwHMiZ9aQBwlcLWCJIv6hSK6T3NLdAvsEaWSZsc7wPYMnYHQ92CDVQAT1oPwIi8mSBq0KzuD0bKObkjuB5L9AgLwt3FtzamzB2UfjBRwAxFE0XopYwN9rr9WsgW8gjA_uSMjumKXtmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86022269b5.mp4?token=aHwV9kCzvdMxVl_8Ja9zK15bqiaAHMHiGEwY_Pp5VAIXLH-msk2hNGNOGlKtiBamO_jEPQlRMuKQcYqsl9NbKPmWO7TP0aM-44C8LyL7b0xfd6k_fPC8h-LCjiIJL0Qw2HNcTfF8hoK22KEFgg_o7bozdD3lpx-xNsFyQuzdy-W_3jVHcYCV0FIUrfClFbWUt89PJLsGL1vGwHMiZ9aQBwlcLWCJIv6hSK6T3NLdAvsEaWSZsc7wPYMnYHQ92CDVQAT1oPwIi8mSBq0KzuD0bKObkjuB5L9AgLwt3FtzamzB2UfjBRwAxFE0XopYwN9rr9WsgW8gjA_uSMjumKXtmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدبان اتاق جنگ : اهواز همین الان پهباد شاهد بالا سرمه
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/22071" target="_blank">📅 03:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22070">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ma66hCHxLHZiNXEN4XDzVIlr5xrOmU6ZmirkYuGyvEUh4D1Kl0OzUGJKpffZecagktZFYc_I5SiXxZq9psClpi85XeiOXtHY8XDuskhhT2LSxZ1zQb6OXvVOIFiCDTzmhTtBPprIuGpI-un0RYXO5Qoz1MJzAFdnA4llQfHTsOhmKRNFlEN3IRenPGVymAcjTr0oBWNQk0DFeCo17HrpAK8lNy9Aq2YPb1yLgItJnrFEpRt8k33bA0NuGwqSJ03--O4062oD169xqt5Cq1EOsrOLx8qPMmP6bxY3SrQo-RRjss8JQCrjM7BX1PQ1nsY-y9fkqC6jsyZA_MTJpCHCAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ : هم اکنون بیمارستان میناب
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/22070" target="_blank">📅 03:11 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
