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
<img src="https://cdn4.telesco.pe/file/Kx_TaKd4zrJt0i3Bomq0jeDAPV4aTL2dUUOs68iCJIJssZIquVcs6tUTbxxbOgHAD7L5GVLA7EG3XEZkjQZcb6UQxzmU681f2O2QvZ0nVPmYXYFRonebjHnHu3xLo7_EviWb8R4ANjcB-sj1K9_iikEnaDQdk-kifLIbtHJA9T_5ufRY99J3Xml7M5dexcUK3IKmva8aofAs1ADC8iP-p30xRO_m0negZHH6Ep33Xa3Mae2q6LLwEhp5MqOAj5P3yrnDaseinO4Bbji8ldEyyjeh3b1jcKeFBts9APGF9zcaIObFsQtNOiUME3Qyzr3aQG2cyaItXE8NqvSuvWTNGw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 445K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 23:36:34</div>
<hr>

<div class="tg-post" id="msg-20502">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">رسانه های عراقی طرفدار رژیم :
شنیده شدن صدای مهیب انفجار از سمت ایران در منطقه شلمچه در نزدیکی مرز آبادان
@WarRoom</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/withyashar/20502" target="_blank">📅 23:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20501">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مارک لوین : دیکتاتور سعودی دوست نیست
@WarRoom</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/withyashar/20501" target="_blank">📅 22:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20500">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/049666fcb2.mp4?token=VENzFfhla2gWYvDWmxvrE2Q_IXhbwau97wSNgy2JLj5nMdokSzx6kbpxTp9Vt_o3ujQ2d67f_Om_Cp-4_lIhnGr27Mo9KOC2y1YhtrVz7T8Uy_42iyqgriy142jrj43wQUA2l_UKUvKdwZTrvo0rLmtBsvxHGAjrpGYZdb1el7e8Y-RANEltGSxTx3CzAPNfPF2dupAL7b9bBxac30mPTCcm2jEM5PKaReGZLLjGAHntFn99ZWyOVdD3En5GX4JMKAYoaSPKDs3PCL4UDEsNrO11UFqAa_SZpF8j5XZOh8l-TMxAtjubAlNCT2oQAUAX7-FXwUxVNlz1CAR9Kz2dPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/049666fcb2.mp4?token=VENzFfhla2gWYvDWmxvrE2Q_IXhbwau97wSNgy2JLj5nMdokSzx6kbpxTp9Vt_o3ujQ2d67f_Om_Cp-4_lIhnGr27Mo9KOC2y1YhtrVz7T8Uy_42iyqgriy142jrj43wQUA2l_UKUvKdwZTrvo0rLmtBsvxHGAjrpGYZdb1el7e8Y-RANEltGSxTx3CzAPNfPF2dupAL7b9bBxac30mPTCcm2jEM5PKaReGZLLjGAHntFn99ZWyOVdD3En5GX4JMKAYoaSPKDs3PCL4UDEsNrO11UFqAa_SZpF8j5XZOh8l-TMxAtjubAlNCT2oQAUAX7-FXwUxVNlz1CAR9Kz2dPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ عازم لس‌آنجلس و لاس‌وگاس شد
@WarRoom</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/withyashar/20500" target="_blank">📅 22:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20499">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سنتکام اعلام کرد که از ابتدای ازسرگیری محاصره دریایی اعمال شده علیه ایران تاکنون 45 کشتی را ملزم به تغییر مسیر کرده و دو کشتی را با هدف‌گرفتن آنها ازکار انداخته و دو کشتی دیگر را مورد بازرسی قرار داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/withyashar/20499" target="_blank">📅 22:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20498">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrkxahFiuoZyncwytOqtarkVZRAnJVxrgZt0KEZf7w16ZXSeP-Fw4LyeX9Qggb3hOcdHQa2g6EZSPEkPBHC4AZeaer04hzUFTvPAfYoKTfntBSkd88ABo3TkFlhztjn_oY8cZSbBmoRxHrYnyBk9pOsjRaokPZ0EBZCtsMQHkGpYC5x_mIULRrNRXLP3qjS7n-gf1bU8Lt4QtaCoBnrdq18uCCoQzGfZ-4Wi5H-N_xlusdoSWY_-rPWhhkEDA09Y5K8gn0hI6Pmpz1ozOWyx1EtHcQkglDopmgI6hdCTV3Dw54X8p_8C4ZVCIvrPLPjuHbP2IuUMcI_OCGSted0ySA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت ۷۹.۳۵$ شد و به زیر ۸۰ اومد
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/20498" target="_blank">📅 21:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20497">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وال استریت ژورنال: اگرچه واشنگتن تأکید دارد توافق ممکن است به‌زودی نهایی شود، اما ادامه حملات دریایی و اختلاف بر سر شرایط و هزینه‌های بازگشایی هرمز، همچنان مهم‌ترین موانع پیش روی مذاکرات هستند
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/20497" target="_blank">📅 21:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20496">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">نتانیاهو:
ترامپ و تیمش معتقدند می‌توانند حماس را وادار به خلع سلاح کنند و غزه را کاملاً غیرنظامی سازند. آن‌ها پیش‌نویس این طرح را برای ما فرستادند، اما ما با آن موافقت نکردیم. این پیش‌نویس، طرح ما نیست؛ ما اصلاحات و نظرات خود را برای آن ارسال کردیم. جالب اینکه این نظرات را پیش از آغاز جنجال و فضاسازی رسانه‌ای درباره این موضوع فرستاده بودیم. این موضع رسمی ماست و با درایت، قاطعیت و حفظ منافع خود، بر آن ایستاده‌ایم.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/20496" target="_blank">📅 21:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20495">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">فاکس نیوز:یک مقام ارشد دولت آمریکا فاش کرد که لغو جنگ توسط پرزیدنت ترامپ در واقع بخاطر لو رفتن زمان جنگ در رسانه ها بوده و ترامپ این جنگ را فقط به عقب انداخته و مشاورانش به او گفته اند می تواند در این بین و برای آخرین بار به جمهوری اسلامی فرصت مذاکره و توافق دهد و در غیر این صورت در تاریخی که از قبل معلوم کرده و این دفعه امیدوار است لو نرود، حمله بسیار گسترده به ایران را انجام دهد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20495" target="_blank">📅 20:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20494">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4509abf5f6.mp4?token=gpwABD42asBfpAkPBhw6DL0sVHxqVz7PlB-8PBjmG2Ywux-2atoRiXR4HK7RsywY0zNHz9swZqghNBWx5_O6WGkb2zJhhiY841mJCd9Sqln8FKPE-Mb_79frub4RrhwqKm6RDOtQb36LX4HckW5sGK7qW2V_cCcziE714Puw00s8Yz83aF0FMBf2bu4eUBcAnhaDKyz7U2MjxL2TN25C_B7ESmpZAG1LnTM1QA9Q9zPWSUsuj2U9ksF99vgJlAtYMcRGNheT-NSacUiFfu0NF-9sAKTKd86ntg1CdEqCDCRzyYMNI0xhp4fMIqVO2yzdx4elS5vvSAl-EZ0l9YVLag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4509abf5f6.mp4?token=gpwABD42asBfpAkPBhw6DL0sVHxqVz7PlB-8PBjmG2Ywux-2atoRiXR4HK7RsywY0zNHz9swZqghNBWx5_O6WGkb2zJhhiY841mJCd9Sqln8FKPE-Mb_79frub4RrhwqKm6RDOtQb36LX4HckW5sGK7qW2V_cCcziE714Puw00s8Yz83aF0FMBf2bu4eUBcAnhaDKyz7U2MjxL2TN25C_B7ESmpZAG1LnTM1QA9Q9zPWSUsuj2U9ksF99vgJlAtYMcRGNheT-NSacUiFfu0NF-9sAKTKd86ntg1CdEqCDCRzyYMNI0xhp4fMIqVO2yzdx4elS5vvSAl-EZ0l9YVLag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : جنگنده رادارگریز F-22 نیروی هوایی ایالات متحده در حال دریافت سوخت از یک KC-135 Stratotanker در آسمان خاورمیانه
@WarRoom
🚨
🚨
🚨
🚨
یاشار: اف۲۲ ها هم اومدن منطقه و آماده هستند</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20494" target="_blank">📅 20:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20493">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">تلویزیون ایران: اگه ترامپ خودش بزاره ما توافق میکنیم ولی دخالت میکنه نمیزاره
مذاکرات بین دو کشور ساحلی در حال انجام است و هیچ ارتباطی با ایالات متحده ندارد، اما ترامپ با دخالت‌های مکررش، تلاش می‌کند این تصور را ایجاد کند که بر روند این مذاکرات تأثیر می‌گذارد.
ایران در تلاش است تا به صورت مستقل از تهدیدهای آمریکا، به پیشبرد برنامه‌های خود در مورد تنگه هرمز ادامه دهد و تأکید می‌کند که تأثیر ایالات متحده بر این مذاکرات تنها منفی بوده است، و تهران منافع و اولویت‌های خود را بر اساس زمان‌بندی یا خواسته‌های ترامپ تعیین نمی‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20493" target="_blank">📅 19:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20492">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">یک کشتی کانتینربر متعلق به هند در دریای سرخ به وسیله یک قایق انتحاری، نزدیک بندر حدیده یمن، منفجر شد و در حال غرق شدن است!
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20492" target="_blank">📅 19:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20491">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPbnu0cyxF39Httw8BYVtjIcrI98TiEekiKmH-hDEjyekEPIYEehKB4aGw3B3mOibaBPI5shux35vJVWkUjt0v7FXDbU7kMjeWS8WlB1XrwgoeOAWEAPS1UOzroDiEknwDOU-SePaR5riEvXa0J1hbib5YtuV9-PYgY023X74jhrizmpQMgRgvB1yJvrLh5VS8NOaHCjHyUAwCW9Um-vTBYprSJTGs-PLw3WYxIV-VLIfqdBk9TKks-4ITPYIXgVOsYZkcqQfB6vA443jreIqQuc44MyYTWGJnHd-jrU2YPkwMO4bYiH7hDtWy9mxM2hanucMcdHQ5pOVWtYtZJ41w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستون دود اهواز ….
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20491" target="_blank">📅 19:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20490">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ادعای ‌اینترنشنال :بر اساس اطلاعاتی که به دستمون رسیده، ملاقات پزشکیان و مجتبی خامنه‌ای که تو اردیبهشت انجام شده، زمان خیلی کوتاهی داشته.این دیدار داخل پناهگاه نبوده و تو یه محل امن، داخل ماشین انجام شده.
ادعا شده پزشکیان و مجتبی خامنه‌ای روی صندلی عقب ماشین نشسته بودن، اما صورت همدیگه رو نمی‌دیدن و گفت‌وگو به همین شکل انجام شده.
همین موضوع باعث ناراحتی پزشکیان شده و گفته: «اصلاً معلوم نیست اون شخص مجتبی بوده یا نه؛ با این کار منو تحقیر کردن.»
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20490" target="_blank">📅 19:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20489">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nj2kcd3VjLeM5UiDmlm7nOytO2zuritJgWspwV5aYWBpb0mFxpVj1ZhmEZj_TkOKmOPQcrLaktYId0rPvGNvy06i2UQJYgLs2EYCH7aqUpSBN-yCXUUAD7SOMQsXIGewfMOQxhZVUjT5N87X4SNhBnZD3PSjnvuOijVvZm-XOCVEYZUCYC_GR41XTESOoJvhCQKKcqjolyPtg7BSYpyLqADIjk4tH6mentSrdgccS_Kc81opREogW-O1zpUnEYMrw1V6QtgaTtnOwHq1Fcy7u9LRLKVrAHsa9MqejLfAGelw65gJsklYDRJDE2jSccCBIfnsEOq0uzZyaLMC1gBzNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدای توافق اهواز همکنون …
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20489" target="_blank">📅 18:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20488">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSMpiH_zLItJbGQElCPSIIOjtKdX36mbwiQzpDUP2icI44AGcw2l0Im44CJLgz9Pklgd3U5RACYzPFmVvLhKZ3I1nTm863PwguerDdrjTnvujmC2__pv_p2I-aBug5kiFSXJEdkDx6yrdzuEJ419-POTk-2Wv-8lqbHX2U-npOkj0U7SjD-ZxYi7BGl2q4UL3ArajhXIISJqfudKw03pvcwIoJieFEvfZ6z_JeAMbiO1tBvJdCYWXlIGp4LSvVk6-_F2CNGd8z5tQOTrCl0fBTDNFbk0NXhObVNsFG-YrwH4TaJAykJQt9ZrLmjxzIyntkndwjgeBSfGOWWDmQY0Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «توافق قریب‌الوقوع است» همزمان با از سرگیری مذاکرات ایران در روز دوشنبه درباره خلع سلاح هسته‌ای
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20488" target="_blank">📅 18:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20487">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lfv-J9MZalTzQTfhV9_V-hJX4Qxhacr9k3QPHgY89vPXCJW-wN9W-ipA45FAq_EHDbDd48qzAui9QPk5232hdqsn2iYayPPSJboJQwng6QnJAlEz2tB3KBOEvLJhHGeLKfTq5-A2QWeF340dvLAmpRLst_4G6bzfXc5kvMeN9nYc45vq23cw4lABXyGXj0S3cN4fS030TQf7wlReBYAV5m3qruvXMYZ2w1miWwYyT_jtR3wuRvvjbfHm3CaArE7posxet0ojI8MTzd1JrQzCGN2tWwLU5lE7dNc_XgzVDEJArSe3PODhQHbfxM2c7oysz4FKK1tTmP8dH0CddhLKnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام ياشار همين الان پادگان سپاه بانه انفجار شديد
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20487" target="_blank">📅 18:00 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20486">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa412933a5.mp4?token=Ead4b91G-CecI70shpFryuaYMqjCpN4gaJwGDwru3U8_oVC0UmWP4xxQjkS9gYOkZpOwAILCYobBtAA3y5ZqMKWypXLnJLektkKVlpnDz_iSxSV3AfJUpUnSUzmjUEcWexSvGi2UJGSkQsvQYreX4RLPDbE7pbCrPVapOFJrFHsUj3o0lxyis-KWcymUcmk1HyW5vmHLxcgegA8iRZW8uEM39IiEqnhlEMyNa6rJHyPMgBuRSV5ruSRAKOnX3ac-WxuJaHL0yKZ83XCr0ERxRUuOsXWkVDPQ0MAChEwaMQyLTr1U03-aknQ05U4oqnLbM51tRavh77QcWEMbyMKVuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa412933a5.mp4?token=Ead4b91G-CecI70shpFryuaYMqjCpN4gaJwGDwru3U8_oVC0UmWP4xxQjkS9gYOkZpOwAILCYobBtAA3y5ZqMKWypXLnJLektkKVlpnDz_iSxSV3AfJUpUnSUzmjUEcWexSvGi2UJGSkQsvQYreX4RLPDbE7pbCrPVapOFJrFHsUj3o0lxyis-KWcymUcmk1HyW5vmHLxcgegA8iRZW8uEM39IiEqnhlEMyNa6rJHyPMgBuRSV5ruSRAKOnX3ac-WxuJaHL0yKZ83XCr0ERxRUuOsXWkVDPQ0MAChEwaMQyLTr1U03-aknQ05U4oqnLbM51tRavh77QcWEMbyMKVuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو درباره ایران
: در مذاکرات برای بازگشایی تنگه هرمز پیشرفت حاصل شده است، اما هنوز توافق نهایی به دست نیامده است. ما امیدواریم که توافقی خیلی زود نهایی شود
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20486" target="_blank">📅 17:57 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20485">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ادعای رسانه‌های کشورهای حاشیه خلیج فارس:
به‌زودی بیانیه‌ای درباره بازگشایی تنگه هرمز منتشر خواهد شد
،
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20485" target="_blank">📅 16:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20484">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCmrFmb9DZK-_c6mJeoLNrzLZFvfOq1GgUbYGvadorg8fAcqqfc0312fNAwJMdRYG-DAqPSv0buCrrtqhdAWHtF0lw-GCoFcpDVbG8RaDltYZT-iGWhE7jnppBzQT8YWnfLiswXacVKdsMKUr9cG7yoV5SMrxAke1uj8rF-mfJnzvXBQiv6qI_mlp54f2ZT4ZqZbvXlnwAYTio0TldJZVzV4T5RXz3L_ROnwH6b-Ln7jtuyMSEVj-a6MG1lvOiyoBEhHiEltip3NyBlABCElTOiriMS_ThbazTXtx8aZcvEAavCtcFekkwlhE4duVW9wZi-CSPH6W_tf2OrOF7Km0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا، در مصاحبه با CNBC، گفت: ممکن است فردا با ایران برای بازگشایی تنگه هرمز به توافق برسیم.
کاهش نفت و افزایش اونس طلا بعد از این مصاحبه
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20484" target="_blank">📅 15:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20483">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">«تبریزی»سخنگوی اورژانس تهران : ۱۸ مصدوم در حادثه انفجار در شهرک شمس‌آباد
متاسفانه پایگاه اورژانس هم در نزدیکی محل حادثه به دلیل موج انفجار تخریب شده است، علت انفجار در دست بررسی است.
@WarRoom
یاشار : دقت کردی ؟ موج انفجار ! علت هم هنوز مشخص نیست!  فقط بی بی میدونه</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20483" target="_blank">📅 15:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20482">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">بلومبرگ : ترامپ به ایران مهلت داده است تا سه‌شنبه با عمان در مورد تنگه هرمز به توافق برسد، در غیر این صورت با حملات هوایی ویرانگر به این کشور روبرو خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20482" target="_blank">📅 14:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20481">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">یک مقام ارشد پاکستان به گاردین:
مذاکرات میان جمهوری اسلامی و امریکا،
به بن بست رسیده است!
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20481" target="_blank">📅 14:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20480">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">قطر: متن اولیه برای یک توافق  آمریکا/ایران تدوین شده است
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20480" target="_blank">📅 14:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20479">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اتاق جنگ با یاشار :میگن کارخانه آلومینیوم کاران بوده بد نیست بدانید
آلومینیوم یکی از مواد پرکاربرد در ساخت پهپادها و موشک‌ها، از جمله پهپادهای شاهد-۱۳۶ و آرش، به شمار می‌رود. از آلیاژهای آلومینیوم در بخش‌هایی از سازه و قطعات داخلی استفاده می‌شود و هم‌زمان از کامپوزیت‌ها و فولاد نیز بهره می‌گیرند. این فلز همچنین در ساخت موشک‌های بالستیک، کروز و برخی موشک‌های سوخت جامد کاربرد گسترده‌ای دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20479" target="_blank">📅 14:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20478">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">وزارت خارجه قطر: تا کنون هیچ توافقی حاصل نشده است و در حال حاضر، مهم‌ترین مسئله بازگشت به مسیر دیپلماتیک است.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20478" target="_blank">📅 14:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20477">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b588c7cf3.mp4?token=QCeSFHQh0nGMxk8ejyg55-HlSZCJnQFBRxsNnOYKyi3nYH_du_nQy-11R_bc4UxKkZnA765Yi4ywlAdEJSOMCRbLK3Ju1pAWPJo6ZMjc1jTYN9PKgZ3Ap1rz1v1Sghu7fO_QUPJ_MXHy3D2J7tJqoQDp_0m3DKsfLeOMQpDrlGXrCMgPn8_YQUSWmYxBTv9sbRBumtCuHlT9QMt3-lDYn1HQNj5cJ8EbiuFGzl8G_LhUquok4kNqavK5sDlRXnTV7sS8Nv0iaaZYOH1Dz49jXoik3oSm1iaXowlgEMVBbmrG-C8xZS-T4E7qgO5y13SzmlsMwf-TppSwynqLR98gSp-IMzqQciwKHWX9QVw0Wa3g9ErEY6SQHfZI7o6nS8YNhJxq992CyBVwPu0Di_MMnxlbYmTwCo7BqLvumGWYIl_pz2wc-xqJ_1fbHjy7DAxGOeXPKMLK0jPjkX_EaZkDkEXJGaTXcyc78L8Q4AEbN4WLZlMWsEI0TZSR6MtoltFxPO7P0GRYqk1kOX6U4nVblAcAEaVFl2MyOHPqAZY45PjO08GW87Uv86XD2O4S6QXzyS1Rohl8togL6KEtDYg6SGrd0GJhcNI9lf4U8HsQHIHHTWtvp7thRu4HUg2PQI4EXXpMG1mz1A7WSa0tqpdy7AHtddjlMQ-uDJxxS0nkqmc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b588c7cf3.mp4?token=QCeSFHQh0nGMxk8ejyg55-HlSZCJnQFBRxsNnOYKyi3nYH_du_nQy-11R_bc4UxKkZnA765Yi4ywlAdEJSOMCRbLK3Ju1pAWPJo6ZMjc1jTYN9PKgZ3Ap1rz1v1Sghu7fO_QUPJ_MXHy3D2J7tJqoQDp_0m3DKsfLeOMQpDrlGXrCMgPn8_YQUSWmYxBTv9sbRBumtCuHlT9QMt3-lDYn1HQNj5cJ8EbiuFGzl8G_LhUquok4kNqavK5sDlRXnTV7sS8Nv0iaaZYOH1Dz49jXoik3oSm1iaXowlgEMVBbmrG-C8xZS-T4E7qgO5y13SzmlsMwf-TppSwynqLR98gSp-IMzqQciwKHWX9QVw0Wa3g9ErEY6SQHfZI7o6nS8YNhJxq992CyBVwPu0Di_MMnxlbYmTwCo7BqLvumGWYIl_pz2wc-xqJ_1fbHjy7DAxGOeXPKMLK0jPjkX_EaZkDkEXJGaTXcyc78L8Q4AEbN4WLZlMWsEI0TZSR6MtoltFxPO7P0GRYqk1kOX6U4nVblAcAEaVFl2MyOHPqAZY45PjO08GW87Uv86XD2O4S6QXzyS1Rohl8togL6KEtDYg6SGrd0GJhcNI9lf4U8HsQHIHHTWtvp7thRu4HUg2PQI4EXXpMG1mz1A7WSa0tqpdy7AHtddjlMQ-uDJxxS0nkqmc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شمس آباد یک انفجار یک سمت و بک انفجار سمت دیگر !
حالا عرزشی چی میگی ؟ گاز و گوزه ؟!
🤣
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20477" target="_blank">📅 14:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20476">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e0d135103.mp4?token=exA5uE8-lzo9-yRmJDmNFb4j_7QGmYAyW0l-5ItkVAv1syngW0WH0eGRLVPU9M-_3hx3Ll54Q4-4m72WTctMlkSeSSHi8guDBN6LbBlp9OqFK8Jf5cIE-0NF-KHROuqwDj6B3crqTMJoeaiDIXOKvgNk6ekOVa4-K2opz-6Yca-KU75E9lZgGLCEzrocs6tmmA4q9P8Hr7H3TtUWVpjp99ntzmw44N1ZCZ5-rsw8o0nrKRmNuD_e_0JO1HDtq77fHk-5mzbFcz9E_w-8U5dIROZFLdDnq4tpE9Ikx-FwVlhL1jtx-Rfmxmyntj3vtSnBHARIpbm3UgTl4LY8TNq1iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e0d135103.mp4?token=exA5uE8-lzo9-yRmJDmNFb4j_7QGmYAyW0l-5ItkVAv1syngW0WH0eGRLVPU9M-_3hx3Ll54Q4-4m72WTctMlkSeSSHi8guDBN6LbBlp9OqFK8Jf5cIE-0NF-KHROuqwDj6B3crqTMJoeaiDIXOKvgNk6ekOVa4-K2opz-6Yca-KU75E9lZgGLCEzrocs6tmmA4q9P8Hr7H3TtUWVpjp99ntzmw44N1ZCZ5-rsw8o0nrKRmNuD_e_0JO1HDtq77fHk-5mzbFcz9E_w-8U5dIROZFLdDnq4tpE9Ikx-FwVlhL1jtx-Rfmxmyntj3vtSnBHARIpbm3UgTl4LY8TNq1iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار اسلامشهر هم اکنون
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20476" target="_blank">📅 14:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20475">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6BhMAqyf0lWz-p9j17w57N4mce19QZ1bRWfxaZEcTDOLBgaXWLXRUyA-IncXkY4Ey6hrRMB7oYLy4mYFMh1k9W7pRoP3an9irnreQkbhGdKC0K252a1XjALdDVgYVyBtlp9fZrjK14fbOu5E8Xrvt0rV7OU3EWBi445IvBV7MKHIJNZB2mZjWlHkxJC7dzg3-kDLB9eceJAEd7kCtS_p2SS6MMgiN-7522WsFuyOZPK4PlAIlorLqlKzAKhCVievHufA0DrD_NgAS6VX-1HtvKwusVAcSeN9zQE-ZrLqdkBB3RbzeUV6TTAon-xQaqfceYrmWdp6MrqA_7kQHzgLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیئت مدیره شهرک صنعتی شمس آباد:
چند لحظه پیش یه مخزن گاز توی یه کارخونه منفجر شد و باعث صدای انفجار، دود و آتش سوزی شد.
اصلا حمله ای نشده مردم نگران نباشند
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20475" target="_blank">📅 14:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20474">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گروه تروریستی حوثی‌های یمن اعلام کرده‌اند که یک حمله دقیق با استفاده از پهپاد علیه یک "هدف حساس" در فرودگاه نجران در عربستان سعودی انجام داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20474" target="_blank">📅 13:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20472">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d96f29aa.mp4?token=DfyIgg99I_bCLZC0aeXk0ME2MDGzWHR19kvoLC2ENoN4ZI-JpGsVX0RSKgRktLKppYtzHxpdr_y-Vp0Olb4pTCAv0Vupch7xTTEi-dahDtRscS3FboN50CHxWGpnjIPqjhiCs1CXOqE67UFS6bwTBFAnusGvbnVkna08yjPZAEB00CW5_hcq9IMnmAXzrzw1wZDch26vGAl3SLBr2mkLqG0FO44rz1CdDFK4NMo5ohrk4aLNeb2TrPzWLiSPCNGg24rkJJwLpcmk_7CmAQdf87Gsi-12A8Vo6Vy0yhKZXyEJvYRD0qCXQ93s4Jx3QvRcZVeyb0nnqUvkAlQHzgehCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d96f29aa.mp4?token=DfyIgg99I_bCLZC0aeXk0ME2MDGzWHR19kvoLC2ENoN4ZI-JpGsVX0RSKgRktLKppYtzHxpdr_y-Vp0Olb4pTCAv0Vupch7xTTEi-dahDtRscS3FboN50CHxWGpnjIPqjhiCs1CXOqE67UFS6bwTBFAnusGvbnVkna08yjPZAEB00CW5_hcq9IMnmAXzrzw1wZDch26vGAl3SLBr2mkLqG0FO44rz1CdDFK4NMo5ohrk4aLNeb2TrPzWLiSPCNGg24rkJJwLpcmk_7CmAQdf87Gsi-12A8Vo6Vy0yhKZXyEJvYRD0qCXQ93s4Jx3QvRcZVeyb0nnqUvkAlQHzgehCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کشتی باری که امروز سپاه زد !
ایا این حملات جواب این حمله است ؟ یاشار : شک نکن!
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20472" target="_blank">📅 13:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20471">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SD6oEMCTWeo1WtyahdCn-1E3FdsEFugoUjTxgALeUglf4W8YBgzjPyrCNhKxernCwfpOmsPmUnzRlyFbJyZbRGvQGgi1rLwh_964o9awgqyBd0QwBKUz-L_zaMftBbnSmz5PcYlb4w6hru9asuWTFKQKyNvGE5Rcua6nQM2w_K6NlAF7voeR6jdX2RsA6c7ZypWa7BLptQdSXP6uA1YVExlK0ePPrMxDA2pyPzVWBemJy4HbALTZWE1KQAXCBS6BBFBOWYZb1uZsuIH1Nwvupfkcphlc3T4XH1oR0tpOkyW-Gkc4nC-IWxeJQNdmekh0luliOrWsGWRAoa99GIFkgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلاورجان اصفهان رو هم زدن
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20471" target="_blank">📅 13:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20468">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/538f54d0f8.mp4?token=CKTotsfd86zBV149WIcqPG9Y47uR8UqiwnDxGGxJngs4ox0uTr5T10rlh4wtWt8Aa-jJmvCV4EhoyVIlUXUs1Hn9YBdL5NoEgiE_L29b-2RKVzUXY4Mu9rQNeuaFahMzSuwQIoqSStjpBU4IlydCN__CSkVlsmz0GWPNHZgmMQGRFp1f3qhWf95RApHMGhRsgIRJPj6b41k1vmX3nxNFO6pgedZZ8-7EOnrDaVMit4MYBJuZLj1J_eFtSMWtlJaj75SFGDAmdcTFr3EQiK6gMHyIuESJEqSler45te2mgZYlK_mlD1Lokl1LOlUJ4NQPD5C0cwhY9KA_-SucBjDetQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/538f54d0f8.mp4?token=CKTotsfd86zBV149WIcqPG9Y47uR8UqiwnDxGGxJngs4ox0uTr5T10rlh4wtWt8Aa-jJmvCV4EhoyVIlUXUs1Hn9YBdL5NoEgiE_L29b-2RKVzUXY4Mu9rQNeuaFahMzSuwQIoqSStjpBU4IlydCN__CSkVlsmz0GWPNHZgmMQGRFp1f3qhWf95RApHMGhRsgIRJPj6b41k1vmX3nxNFO6pgedZZ8-7EOnrDaVMit4MYBJuZLj1J_eFtSMWtlJaj75SFGDAmdcTFr3EQiK6gMHyIuESJEqSler45te2mgZYlK_mlD1Lokl1LOlUJ4NQPD5C0cwhY9KA_-SucBjDetQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌اکنون فرودگاه بین‌المللی رامون اسرائیل دیگه هیچ جایی نداره و از سوخترسان های آمریکایی در حد انفجار رسیده ، مذاکرات بسیار خوب پیشم میره
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20468" target="_blank">📅 13:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20467">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اصفهان صدای جنگنده
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20467" target="_blank">📅 13:37 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20466">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0HHAeyukfMq6slW0L9_QwVpL2nlmHOnIjn_ZCKhoXGoGFGysUIpfD9rbw1b4AhxGOMbsldoDt6HnudL6__qfx0ocm_Wi2uxf8Qp1xKp8vkkEzCD8dccMneU6T0BS2MaXZcwWKMJGkuKAgoswILKjS3921d16YmXInMTbnqVaAXrBDtlAQORvHWS4CWapTbgVLRY62lff_3jRaM8WvMkT3BEGaRIWvJxsFgQuOBbBRzmFO-IVCUsiw9htuVDnSyVLd3SBljXeNEPoMo7vNXOfb5u8aCv9vyv82axi4pzU7FUPytkkwOGqPh634DpJmbJHwoAAEYWFeJoxy6P-GbnKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمایی دیگر از دو انفجار
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20466" target="_blank">📅 13:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20465">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85c3af8280.mp4?token=At6b6wKnHQKpAEzPV3Zr3uXGQnmzlsnDJlBVtwAcvkIAf7hXQX-_gj91EvfAG9g_l0imLcBeYx8MnyP144Fy6Hk6-EW_NlWRI2HUk-tOttWeFa3aTnrbZ1fqZWiOcfUxIMA1YtGU_CH9D2eptyzmS7S75WVlVSiafqhm35RAXKfxvByWs6StqVTOi-itCwT-T3fQ6koygUygDpqbBsOOFWi4CJKflHgltY_Xc_sNVrTtI_AYl2fgVdaWjQqFxww3ShjN5HCTGNUFqhsXJCmD-xiYsldgK6yCDWuiZr4b7uUG_gtyb5X37Dh5QMPs4x6aBJv8UnQUwFCTES2LHTYP3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85c3af8280.mp4?token=At6b6wKnHQKpAEzPV3Zr3uXGQnmzlsnDJlBVtwAcvkIAf7hXQX-_gj91EvfAG9g_l0imLcBeYx8MnyP144Fy6Hk6-EW_NlWRI2HUk-tOttWeFa3aTnrbZ1fqZWiOcfUxIMA1YtGU_CH9D2eptyzmS7S75WVlVSiafqhm35RAXKfxvByWs6StqVTOi-itCwT-T3fQ6koygUygDpqbBsOOFWi4CJKflHgltY_Xc_sNVrTtI_AYl2fgVdaWjQqFxww3ShjN5HCTGNUFqhsXJCmD-xiYsldgK6yCDWuiZr4b7uUG_gtyb5X37Dh5QMPs4x6aBJv8UnQUwFCTES2LHTYP3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش مردمی :
دوباره زدن
، صدای صوت موشک قشنگ شنیده میشد چند ثانیه قبل از انفجار و الان صدای جنگنده میاد
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20465" target="_blank">📅 13:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20464">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpN2YALnjOpCjOHvWJc3TtBdkeWZ7YtSYAhcJMD1hFo2k3bb_YqI7NKcSEDTGSE4J2vvU91vrGdOiptMmRgXL-63FHonICzhLEHJq9iJsgYJsD5GmzYXTXZcsW2f9E6tWwDkKmyei7pyMYF8YWan4wnDdECWGoDWW85-_O4k_ErUGkQIKIBr0QsFBnpX4pwuSXqTjMSwjtfe-XxG3N0n159D8vYIXOvUX-Lb9qbzlE-bGKWMwLxsGORV-3ySGLIdcLvWTDLGdwwDQf7v6nkwEXo_0TS-2vkgkSHk4FW61QR2OWmmaclgMoKVfzxpk5JQOXoYGyp9XMUTA1pLoPVSQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرک صنعتی شمس اباد فشافویه توی خیابون گلشن ترکید گزارش های مردمی تایید نشده : مورد ۱ :دو کارخانه منفجر شده مورد ۲ : کلانتری فشافویه رو زدن @WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20464" target="_blank">📅 13:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20463">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20463" target="_blank">📅 13:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20462">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20462" target="_blank">📅 13:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20461">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گزارش های بومی : زدن بدم زدن ! خودش نترکیده زدن ! ‌ کارخانه پهپاد سازی هم بوده ، ۲ تا کلانتری و کارخونه هم قبلا زده بودن همینجا (حسن آباد فشافویه) @WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20461" target="_blank">📅 13:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20460">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7200405da8.mp4?token=BIvrxl54lAzxpSR51qXr6CmIvQMJqooZWrGgl_ySffEF31BTLMOZW3AodV_gFXqMDPyPLwnfQRmoL3_k3hAXCFOswCK_CJQ9vpilzl9eCXQDJjWcyuV3QZmjY-NgJj-y_XNQi2HOTacSS7GV9hMtpvHv5zQIjS1NkDcYP-dxORGy1uYpfX-7RSKOgWWdELx98nzGOLTlhT3ROrJeEN99uMwsxSfF5S0ReyBaswkLwbPMVAy1Jir-2-5w7dgQEiLiGGxMqbN6GE_q0rPg12EVLrcHRGouha4tlkms6tpqIHT2Jx-bmAQqbx3sJre5OyICEu7ufRAn2-2cya2ocQc5eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7200405da8.mp4?token=BIvrxl54lAzxpSR51qXr6CmIvQMJqooZWrGgl_ySffEF31BTLMOZW3AodV_gFXqMDPyPLwnfQRmoL3_k3hAXCFOswCK_CJQ9vpilzl9eCXQDJjWcyuV3QZmjY-NgJj-y_XNQi2HOTacSS7GV9hMtpvHv5zQIjS1NkDcYP-dxORGy1uYpfX-7RSKOgWWdELx98nzGOLTlhT3ROrJeEN99uMwsxSfF5S0ReyBaswkLwbPMVAy1Jir-2-5w7dgQEiLiGGxMqbN6GE_q0rPg12EVLrcHRGouha4tlkms6tpqIHT2Jx-bmAQqbx3sJre5OyICEu7ufRAn2-2cya2ocQc5eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش های بومی : زدن بدم زدن ! خودش نترکیده زدن ! ‌ کارخانه پهپاد سازی هم بوده ، ۲ تا کلانتری و کارخونه هم قبلا زده بودن همینجا (حسن آباد فشافویه)
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20460" target="_blank">📅 13:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20459">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqctkpLUFjkLpH871AAtQ1SlIRSVZ2XRDSzNyjmOFoPEz6vIR-ud-BnLxv8xG2wuZmgAkJIJwdTm5M_6nC8mY97AU_-wqQvE6_vtH1kBKyIZEd2yIRat69jtOHIg4t3SCCs8DGChIeTG9tTRoz1FmFZkFD7Hr_Umop31tNaySLYDZJepeYo2uVYifxTUD5d5E9yCeLOcG65wa6rliV13S6gWeK43K0UzUztjrp6HbjI5WhgE-2jYMaJZVOGcG7qU2fWGQZsskUcRFSGhY923qqkRLKit_E50K8SrI_w47_VgpSO2330PGSNlSHGyKjpkmDLUrVXvtgp87kL6zMdPqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرک صنعتی شمس اباد فشافویه توی خیابون گلشن ترکید
گزارش های مردمی تایید نشده :
مورد ۱ :دو کارخانه منفجر شده
مورد ۲ : کلانتری فشافویه رو زدن
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20459" target="_blank">📅 13:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20458">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20458" target="_blank">📅 13:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20457">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">رویترز: یک کشتی باری در نزدیکی تنگه هرمز مورد اصابت پرتابه‌هایی قرار گرفت و یکی از ملوانان مفقود و باقی کشتی تخلیه کردند
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20457" target="_blank">📅 12:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20456">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">دور جدید مذاکرات بین لبنان و اسرائیل در رم آغاز شد.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20456" target="_blank">📅 12:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20455">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">کانال ۱۴ اسرائیل: رویکرد سخت‌گیرانه احمد وحیدی(فرمانده کل سپاه) به سیاست رسمی جمهوری اسلامی  تبدیل شده  و سید مجتبی خامنه‌ای تصمیم‌گیری درباره پرونده آمریکا را به او واگذار کرده است.
مذاکره رسمی بین تهران و واشنگتن در جریان نیست و تماس‌ها فقط از طریق پیام و میانجی‌ها ادامه دارد
@WarRoom
اتاق جنگ با یاشار : دقیقا در پست ۴ ماه پیش اتاق جنگ «نشانه» 10May به این موضوع اشاره کردم</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20455" target="_blank">📅 12:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20454">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">روزنامه روسی Izvestia : آمریکا می‌خواهد با سردر‌گم کردن تهران زمینه را برای یک حمله غافلگیرانه فراهم کند
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20454" target="_blank">📅 10:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20453">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQQztOkvts3wuI96OtvkLkrSYTXnhkUw_a4dk86ZOAaHWo3nxx74Dhjg-hQ5JfpR4LXaILmM5QXo2x7IHUntW2POA4RomDkw_bR7e9YMSTleAlOiGhr1EDMjb0HpmjKHx1KJzC0TZtWZRcQQM52vT8_-XyRWZ7-fSMsIr5JmS1aSpTam-GEFHvBFkxuDwJG2vj_a6Ylw3PdCt_rnn7P6vb8I1C2JxvASLUBPnK04c8NLgW3Aml7ElzDrvpQnmdaE9CxMtrfAT4n5uQ1XlCpO2GuP7yGKH8tKllTq9NYU63mYPLYtPZV0NKDVC2turyoleprbe__DzzDIKnyPJxL1bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غزه قبل و بعد از ۷ اکتبر ۲۰۲۳
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20453" target="_blank">📅 10:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20452">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">تلگرام از اپ‌استور اپل ناپدید شده است، اما تا این لحظه اپل یا تلگرام دلیل رسمی و حذف اعلام نکرده‌اند.      اپل قبلاً در سال ۲۰۱۸ هم تلگرام را موقتاً از App Store حذف کرده بود و دلیل اعلامی آن «محتوای نامناسب» بود؛ بعد از رفع مشکل، برنامه برگشت. @WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20452" target="_blank">📅 06:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20451">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">صدایی مهیب در پایتخت یمن، صنعا، شنیده شد، و هنوز علت آن مشخص نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20451" target="_blank">📅 06:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20450">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">تلگرام از اپ‌استور اپل ناپدید شده است
، اما تا این لحظه
اپل یا تلگرام دلیل رسمی و حذف اعلام نکرده‌اند
.
اپل قبلاً در سال ۲۰۱۸ هم تلگرام را موقتاً از App Store حذف کرده بود و دلیل اعلامی آن «محتوای نامناسب» بود؛ بعد از رفع مشکل، برنامه برگشت.
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20450" target="_blank">📅 05:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20449">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iowSTe78n6dc9TzhjDctF6Vj5Q2fWlsgOKFdbszuBsSESHepihWCmh7oXzu-tkm9fnifx8MQJTQVO5-E19fCE0gg33rvNBUOWKDc9xO8UB1dFovOZ7h0l-RRr4VQ89DIoG40E9iayfZZ3NtkWdljVoMvSwD_JHc0bdrncQC4mSfRV54TvYp7FXLWJCp81_ti_zd1cdlt7n9k3lW8Nkwd7kwwbWxZfsZ1GnOd9XSDARvDxh6SBas81dQoHusbJc-ONrspVF9LETrPIO-ZTJ5o-PaD3iTGJGSSr5KdxVTZ1dfZ_txVEuHI4EEAdLiP_ErnaQJKNpqYmp1e4naDZpr9ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مذاکرات دقیقه نودی به درخواست عربستان سعودی
@WarRoom
😁</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20449" target="_blank">📅 04:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20448">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7lfc-Wik3NwZSyHDRvUTn6j7e3PpIT07DgjDukSoyIN2CqdTbbeJPmXKafm-1HKEp9Kepyloz5ue8-4wfp9zWP9m4OctoHTexVQux3o5Krnd3dPiiGPvxWqJJhjWNuls_GGL3OKTMv0JceBZsvkC9z92JxNXllAyHsgyGPgdt9yvL4CRpQ3Y5oJhlLX1j75h3kbZWaPYmO6VdwPLU2mLl_x9pb0wHmfZM_Lek2vMVw6UxaKxjG1TGiBij5z5i6-P5r8a_C0hsuR2B2Z1OvYxVBzDjYOc-1fvRHY52NXrSkHqYg5rUjQ6azr0sUvHmpu702uFTtwoa1Y5GJ9MdlHtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان دریایی بریتانیا : گزارشی از حادثه‌ای در ۲۰ مایل دریایی شمال شرقی الخصب، عمان دریافت کرده است.
یک کشتی باری در VHF 16 اعلام کرد که مورد اصابت یک موشک/پهپاد قرار گرفته است.
مقامات در حال بررسی هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20448" target="_blank">📅 03:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20447">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkU8yXpFNyrCITWsF2Q7YhoykrocmXXDmsGdeLb13XX9AgKDBZuDRPj_ioSVpskM_y3LrZH8r7obJ746PJ0J9PH8ifv3PJR5mZdebSMHXLDymWszrHV6HiTteRHlimWIR6sWADQyOFgy6zPhnLNAZwhZYmgaEU8KD1nvtDQ2-HXfCUMDL6KIW8x8_xdOF3ZBTWUb2zufyDGsumh2XMsMSF4-BD3kiJa6K8AqmN9N-O5VTi8LgjEay6_NahO35x6hyrgSxDEaJ-UFmXiwc8HsLtX_7gUAt0I3wotSGxFswit6O9IVoH4-sc1CKdr5RLoTQGjdgttZSRSj_5AfdEalQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هفت هواپیمای ترابری نظامی C-17 گلوبمستر هم اکنون در مسیر آمدن به منطقه هستند!!!
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20447" target="_blank">📅 03:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20446">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">کانال ۱۴ :مسیرهای دیپلماتیک ایران عملاً از کار افتاده‌اند.
به گفته درور بالازاده، تحلیلگر کانال ۱۴، مجتبی خامنه‌ای،  رسماً اعتماد خود را از تیم‌های مذاکره‌کننده ایرانی و آمریکایی سلب کرده است. دکترین تندروانه و بدون امتیاز احمد وحیدی، فرمانده سپاه، اکنون سیاست رسمی آنها است.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20446" target="_blank">📅 03:00 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20445">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">لاکهید U2؛ شبح خاموش آسمان‌ها به پرواز در آمد
🚨
🚨
🚨
🚨
هواپیمایی افسانه‌ای که در ارتفاعی پرواز می‌کند که بیشتر جنگنده‌ها حتی به آن نزدیک هم نمی‌شوند. خلبان آن به‌دلیل پرواز در ارتفاع بسیار بالا، باید لباس مخصوص فشار بالا شبیه لباس فضانوردان بپوشد تا در صورت افت…</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20445" target="_blank">📅 02:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20444">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lenne-0gECfFR-hKwphCCFxXOGSxFhytLuisnifI-Uv-X7nEottTHAzovxYbuNAGDAb5LuoyebwbY27xxyY1PvC9nSU9nUNctWV_jbWmEnss3dLfiQ4eylas6J_jUTDiV5WTS52bvE7fyK29aswLm4RNJGtk35rR2ki_1tM4UHx1ciRleeBNlEgOifuYDnhYLHmdwEVL6P5ulIzGLLIg_uSb_DgCtbfAsptX864XBbrI9l-sd0odv1k2jwXhRjvbnx1C18pUN85bjlxXKhuOF32b2G-gJt95A_8SVdU3xQNt4qjqJsc4eq4HTSzcr37ZhZ9ddv2T_0WFo7qziLpa8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاکهید U2؛
شبح خاموش آسمان‌ها به پرواز در آمد
🚨
🚨
🚨
🚨
هواپیمایی افسانه‌ای که در ارتفاعی پرواز می‌کند که بیشتر جنگنده‌ها حتی به آن نزدیک هم نمی‌شوند. خلبان آن به‌دلیل پرواز در ارتفاع بسیار بالا، باید
لباس مخصوص فشار بالا شبیه لباس فضانوردان
بپوشد تا در صورت افت فشار کابین، جانش حفظ شود.
با دوربین‌ها و سامانه‌های شناسایی فوق‌پیشرفته، از صدها کیلومتر دورتر کوچک‌ترین تحرکات را زیر نظر می‌گیرد و ثبت می‌کند. با وجود گذشت بیش از هفت دهه از نخستین پروازش، یو-۲ هنوز هم یکی از ارزشمندترین چشم‌های اطلاعاتی آمریکا در مأموریت‌های فوق‌محرمانه به شمار می‌رود
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20444" target="_blank">📅 02:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20443">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خبرگزاری های رژیم : شنیده شدن صدای انفجار در کویت و صدای آن از بصره عراق هم شنیده شد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20443" target="_blank">📅 02:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20442">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گزارش پرتاب موشک از ایران
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20442" target="_blank">📅 02:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20441">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XH1hi3WCuIdSaYfBKLvy2BV6dB--zB8snIrkaNMFGkufIH_loSv2RE_F4EMgHN34_K-QTW3x4PUdqgkBZ_51LIMRH_ojhdsp3LGMEuGeUge4pQ-kbaNQFhDQJBMLpyl8KlJNA0vIWCrZVkbX6G6MRFfP0-tW5ZgtFyFc9LV00QgMhH4nm0gn9AIpYTSeyc_mJSP-1WPS5YNbaBLag5EfFe2igsmjCmA5-f23xeuDnfSwKmspyQ5PQRJ8BDmRFzQFmkInWNf0tfcsposRZj3cz_1Q4-Z5cpbEbuxVPALhkwjWIk8cSbPJlDqW2uiXpn1AYGjg_oi-AqGR39nAgmQG2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت یه کاربر خارجی : اگه نقشه ایران رو برعکس کنید؛ چهره ترامپ رو میبینید!
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20441" target="_blank">📅 02:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20440">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پاکستان ادعای ترامپ درباره آغاز مذاکرات با جمهوری اسلامی را رد کرد
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20440" target="_blank">📅 01:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20439">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APuoVSbR9K8YaDDiCooOTwvppTorPZ2gMsQIYCA1tGNJEDmB9jKMRcRtOHzp4DboU960CZqpp60jnFC0_QCv1qsSMT2cHCvqYLLcKgOlBrArC8TFRgGOMYTToCRstLkUlLMZJMUZchce7jyc983LBdXDlpLbwS5Xk84jeCSd6nfxxq-YfjBwsT40P-eRuL946j4iqGc8y0XHjtrhP8NFZSFb44S8fVnTAusDsVErmZCYCKNrYtxUpm4hbx_MdrNm--umGwh3IsBUAxqJpZeeEHldSVC1vAmNfYRbOBMMSOd1jUsexnooFwtiwd1mA0yTbLzQqmQ0EJ4CH5Rk0jL3zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد امروز روزنامه اسرائیلی (یدیعوت آحارونوت) : «تو ما را دیوانه کردی.»
‏ ترامپ: «من حمله خواهم کرد.» من حمله نخواهم کرد. من حمله خواهم کرد. من حمله نخواهم کرد.»
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20439" target="_blank">📅 01:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20438">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJBJEA1cC356Mx7BsNl50Wph4pGQeDTVpE86uiavpjTb2d2PhfS9aGXCh9MkqCFs77DxWqcQuMWNbLxBkPMieFxwq2XsaoqBMfluxcvkTPEH_X8lpeVl1JXpe_d_qGdOtcVDlHRk5ENkaE4Q_-Tg4CX_tk3apQgI4M5gigvpAhWOHWbwLAAVdAOXaSejmWlUmw53cZoE6anPxyqbup2XGODdP8GpmI09CRtf_lM-GWWIYDVEsHgoqbd_F2BUByrcPzHPmYENLCeka-4RaSZCSsEMjhpGueGlYBY2whBxcnj-P0FpFJ708vEiURO4t0TSZDtHWxA-WnBoP0U1hhY4NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون
یک پهپاد سپا، مقر یک گروه کرد را در منطقه خبات، واقع در استان اربیل غربی عراق، مورد حمله قرار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20438" target="_blank">📅 01:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20437">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : دلایل به تعویق افتادن حمله از طرف ترامپ اگه شما مورد دیگه ای‌میدونید بنویسید ، حتما تا آخر ببینید و کامنت لیک ریشیر فراموش نشه ( کارهای اداری )⁩ https://www.instagram.com/reel/Dbl_dAtIsre/?igsh=andsNWUxa2tqaHZs</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20437" target="_blank">📅 01:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20436">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVST-3EwsI-6SKL-RRQnEJJon4RVM1Rq1bPF0HQKXb14daGHCAccewcRh66fLDEtrU8QTevOgLHD6zHHPfSGyDxC8YNQ4B56uUMjB4tIv0Tog0VdKg1j0hLTu9b5rVKI-2_PT7DjzJhM6NaJ-snZzC3JZuHeg9nkXYdm56bPmLL4qnRiw-GNiKRgeFWVofTUICYJQjpa5b65UuVO8FT-jasaUMxH4BZDyaRSTGVEgw5a1wmwShjteeTkY3Zj-7Wi8k3uIMh_nwyAoeH_lu0g6joBSemT25Q5mgCMawp5hncU1XjaW4m5shU8bo9klI8GR5KyG4Hxy0UgBaFjIWrixw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : دلایل به تعویق افتادن حمله از طرف ترامپ
اگه شما مورد دیگه ای‌میدونید بنویسید ، حتما تا آخر ببینید و کامنت لیک ریشیر فراموش نشه ( کارهای اداری )⁩
https://www.instagram.com/reel/Dbl_dAtIsre/?igsh=andsNWUxa2tqaHZs</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20436" target="_blank">📅 01:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20434">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20434" target="_blank">📅 00:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20433">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20433" target="_blank">📅 00:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20432">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a075dbac8e.mp4?token=gxF8Q3AKQT4n75580kLW4wRz7ZdwkKUBLboUsGkAWw1HlmAoNVMsP9jsoExhmPaR6aI-UmDnxizoaMMESX535CIhUJilzHUKM1joy0J5svHHIzLUHWgmK8dPV5_fWWvkmxx9ASPB6G8ZIAzIcg6t8yl8ry9s8le7ae2-hqj57qO0tiNSy4oLPchTHuNZUdjKn4Eff9n2fgQBAS_fC2qA4Qn9pfD6Dk42kvbJfBr3lBREmqnyOXgBkC_GtAOAMFa4ki_xtG1iURZV_mN2T3HaoXtA9L1oe43ITlqIge7DCaEian8FN3KTM7PTS-o2Ar9xCTiQm2Hh9Sl0IKk0kpM1Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a075dbac8e.mp4?token=gxF8Q3AKQT4n75580kLW4wRz7ZdwkKUBLboUsGkAWw1HlmAoNVMsP9jsoExhmPaR6aI-UmDnxizoaMMESX535CIhUJilzHUKM1joy0J5svHHIzLUHWgmK8dPV5_fWWvkmxx9ASPB6G8ZIAzIcg6t8yl8ry9s8le7ae2-hqj57qO0tiNSy4oLPchTHuNZUdjKn4Eff9n2fgQBAS_fC2qA4Qn9pfD6Dk42kvbJfBr3lBREmqnyOXgBkC_GtAOAMFa4ki_xtG1iURZV_mN2T3HaoXtA9L1oe43ITlqIge7DCaEian8FN3KTM7PTS-o2Ar9xCTiQm2Hh9Sl0IKk0kpM1Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون ‏عراقچی در عراق
😂
(مراسم اربعین)
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20432" target="_blank">📅 23:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20431">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">کانال ۱۲ اسراییل : بانک اطلاعات اسراییل برای حذف سران نظام در حال تکمیل شدن است
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20431" target="_blank">📅 22:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20430">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دونالد ترامپ با «فاسد» خواندن کسانی که دست به افشای ابعاد بزرگ طرح او برای حمله به ایران زده‌اند، تأکید کرد این افراد باید زندانی شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20430" target="_blank">📅 22:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20429">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">گزارشگر شبکه 12 اسرائیل:
پس از 30 ساعت سکوت در نوار غزه: یک پهپاد متعلق به ارتش اسرائیل به یک خودرو در خیابان الرشید در شهر غزه حمله هدفمند کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20429" target="_blank">📅 22:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20428">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">محسن رضایی: اجازه نخواهیم داد هیچ مسیری غیر از مسیر ایران در تنگه هرمز باز شود. حتی اگر آمریکا یک ناو هواپیمابر را به مسیر غیرقانونی تنگه هرمز بیاورد، آن را هدف قرار خواهیم داد.
آماده بودیم اوکراین رو در سه نقطه بزنیم اما بعدش عذرخواهی کردن و پشیمون شدیم
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20428" target="_blank">📅 22:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20427">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ترامپ: ایران از طریق افشاگری‌ها از حمله مطلع شد.اما اگر این روند ادامه پیدا می‌کرد، بسیاری از افراد در ایران باقی نمی‌ماندند.
می‌خواهم به ایران یک فرصت آخر بدهم قبل از اینکه "اقدام قاطع" را اجرا کنیم. امیدوارم آن‌ها با عقلانیت عمل کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20427" target="_blank">📅 22:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20426">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامپ:فردا آخرین فرصت برای ایران خواهد بود.
گزارشگر: آیا ایران حاضر است به آزادی کامل تردد در این تنگه بازگردد؟
ترامپ: من اجازه نخواهم داد که آنها هزینه دریافت کنند. اگر کسی قرار است هزینه دریافت کند، ما این کار را خواهیم کرد. ما کنترل کامل را در دست داریم.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20426" target="_blank">📅 21:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20425">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d709d0023.mp4?token=WiIm0tFBvJSxFbfyeQ3lTCF8m4JFGb6ZHHKWQ3kqJM3HPLIq2mCLtNjj9EZbRRYB0z9KnETX-yyAi5neozZw0w9ylTDrBe0GcmU1V_vbfhFCYo-Twk5R_70jzO6PnOIfjFqAQCSB-aDoNZYZTOrF9Gj4cAiGPLmv0zAzzSW-Fifwn4vhrqRLcbbAwvvKDxk8NSHK-JktJxxxFZI8tjLRY7Pg-w3Sbe7DifUr851fJz3zjLmYlSAGK2IbSKMnykskhKNvPjOizR-3nPyT-uJOVvNoOxBbqNHPlQYtAZBVtByrz_yalejSDKmu-TXFzmI4FpMSLW0RWbU4FdwZrNqMMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d709d0023.mp4?token=WiIm0tFBvJSxFbfyeQ3lTCF8m4JFGb6ZHHKWQ3kqJM3HPLIq2mCLtNjj9EZbRRYB0z9KnETX-yyAi5neozZw0w9ylTDrBe0GcmU1V_vbfhFCYo-Twk5R_70jzO6PnOIfjFqAQCSB-aDoNZYZTOrF9Gj4cAiGPLmv0zAzzSW-Fifwn4vhrqRLcbbAwvvKDxk8NSHK-JktJxxxFZI8tjLRY7Pg-w3Sbe7DifUr851fJz3zjLmYlSAGK2IbSKMnykskhKNvPjOizR-3nPyT-uJOVvNoOxBbqNHPlQYtAZBVtByrz_yalejSDKmu-TXFzmI4FpMSLW0RWbU4FdwZrNqMMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: مذاکرات به سرعت، به یک شکل یا دیگری، پیش خواهند رفت. موضوع خیلی پیچیده نیست.
ما قرار است فردا، به طور کامل، تنگه هرمز را باز کنیم.
سپس، درباره توانمندی‌های هسته‌ای ایران صحبت خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20425" target="_blank">📅 21:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20424">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ درباره ایران:
"این آخرین فرصت آن‌ها برای امضای یک توافقنامه خوب است."
ما دیروز قرار بود آن‌ها را به شدت مورد ضرب و شتم قرار دهیم… با قدرت بسیار زیاد… قوی‌تر از هر حمله‌ای از زمان جنگ جهانی دوم.
اما ما اکنون در حال گفتگو هستیم، این گفتگو بنا به درخواست ایران و با حمایت عربستان سعودی، امارات متحده عربی، قطر و سایر کشورها انجام می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20424" target="_blank">📅 21:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20423">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f308e1bdbb.mp4?token=elp6v3CXGch3W2U9D9XHx3Lu_LSK2K276Fv__JwgaOG0zNMggP5ZH7pWmhE_8wx6XBODV7awIcsg7igtIii6LGxJtSk3qfjylyIqcGhmmVWcyZjdOffzYhcy1IsIZ3MfzqT_otwgFpJIc2zJJdE3DOZ1dOlmjm4pZpf60Q-VoIGxnKjbKZNlkG56PEbAc7v2Gc8mz_IQh4vyqLwblOPJieWdXWhidaAF0Z0jOwM8LyjQfKonxSXBFBdup0TW8RoWuP9zhdm8MtkviYwuHnrkgfxFmEFEFrMzde1qZwoGymJGN0KU3uuPvNBuEj_CGA0-RmVEciqyM5BkFT872QkKbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f308e1bdbb.mp4?token=elp6v3CXGch3W2U9D9XHx3Lu_LSK2K276Fv__JwgaOG0zNMggP5ZH7pWmhE_8wx6XBODV7awIcsg7igtIii6LGxJtSk3qfjylyIqcGhmmVWcyZjdOffzYhcy1IsIZ3MfzqT_otwgFpJIc2zJJdE3DOZ1dOlmjm4pZpf60Q-VoIGxnKjbKZNlkG56PEbAc7v2Gc8mz_IQh4vyqLwblOPJieWdXWhidaAF0Z0jOwM8LyjQfKonxSXBFBdup0TW8RoWuP9zhdm8MtkviYwuHnrkgfxFmEFEFrMzde1qZwoGymJGN0KU3uuPvNBuEj_CGA0-RmVEciqyM5BkFT872QkKbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: «از همه شما به خاطر حضورتان در اینجا متشکرم، چرا که ما گام جدید و بزرگی را برای حمایت از خانواده‌های فوق‌العاده نظامی های خود برمی‌داریم... امروز، من یک فرمان اجرایی برای ایجاد اولین کمیسیون همسران نظامی ها امضا می‌کنم.»
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20423" target="_blank">📅 21:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20422">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7eb6721586.mp4?token=Qqh7uH9XI4v3JvRItnl8lmgTiwP3UBjx21a0opF1n4MCMPIfV6Za1UACCUju7ZTYz3ynkilctgxCy_TNqAH0Jlp2q4jlGOxZBLzfeQiyR49mTGsGivygmZp4FkrDH1CBye9WGLyHdviP3YRhO7v8YXpBCm3lU7YxgXWr30Ls5LMGOQ3B0wgozyJBq5UqvkX-zdj74Yn7Yl6kCEgQNi002T0Kcf8PRUHqlm6PlZqNrsaQWANMh6ZuHeVFQ3af7WmRy-Zu_Ze39C8THKi10zmiWt_xDAYpPqTUCD2ZlE45OQzvK8Rp7VB2R--bgIKcncrT6npl9Tx8wctj48c18R4UzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7eb6721586.mp4?token=Qqh7uH9XI4v3JvRItnl8lmgTiwP3UBjx21a0opF1n4MCMPIfV6Za1UACCUju7ZTYz3ynkilctgxCy_TNqAH0Jlp2q4jlGOxZBLzfeQiyR49mTGsGivygmZp4FkrDH1CBye9WGLyHdviP3YRhO7v8YXpBCm3lU7YxgXWr30Ls5LMGOQ3B0wgozyJBq5UqvkX-zdj74Yn7Yl6kCEgQNi002T0Kcf8PRUHqlm6PlZqNrsaQWANMh6ZuHeVFQ3af7WmRy-Zu_Ze39C8THKi10zmiWt_xDAYpPqTUCD2ZlE45OQzvK8Rp7VB2R--bgIKcncrT6npl9Tx8wctj48c18R4UzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما اختلافاتی با ونزوئلا داشته‌ایم، و این مسائل به شکل بسیار خوبی به پایان رسیده‌اند.
و ما اختلافاتی با ایران داریم، و این اختلافات نیز به شکل بسیار خوبی، بسیار خوبی پیش می‌روند.
@WarRoom
یاشار : مثال قشنگی‌زد
🤣</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20422" target="_blank">📅 21:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20421">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af9742ced6.mp4?token=flq4fAOXclLtEVbOXsNrGGQt1bDWIsHiRauba1_Pu3kYc5Oou39z4YXLD0A8LgqJGAjdmTED0ITVJYccsfdy_iOSKrlLe_jmK0ma_WcVoS_tw1XQ9CF3IOx45m3_yFBxLj4xRG3vAT2Sr4VtTpKLKNfIBq6G1xEz2M2EtSycpkDqAN1WKscGVlOJ7VITeiCScaFiJUb9WJX71qqLKhD3fzOsQb8UuHlbsBxQunZMoMoy0AjluGRIuHwRjVcTI2gj-PVjQ-9bYTKUwqZqEHYWnIDtWCzj9qvhbj79IM876Wvk4F96X6JlQZLVduMog7erkcd4Ls5KmARr2fVAesRW_Lvt6wXLsfCIa1v3dDIMGwwaBo8xOU8thp1Kz-yc4Q_zNrbbio9KHfeDOMBM1vzidAj_32q-EbRtVzJGg6B3T9LIbtUbVP6F8QFcWjS7YJCTpzv9NM6aOk-ElUrQGrGFvrttTDVsM44bff0kttYL_GHg8ZMemikGDLXHSsDRE4MGw3j5ddypmK0LkxoGM5I5Lr5pwysI0vIvNRZdSs1ZXUdcPXKPCsI-lqxw-YXXGXWg0EjA4SO2eeP0mGMMelLOd3NHqijuBkRe9VDkPUWxIYwnFRcmXzjQBuhGqfnaz1YYEdhaMuCibgs1LRfnajGiRb4VEQszziGcd1JviOMO1Ik" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af9742ced6.mp4?token=flq4fAOXclLtEVbOXsNrGGQt1bDWIsHiRauba1_Pu3kYc5Oou39z4YXLD0A8LgqJGAjdmTED0ITVJYccsfdy_iOSKrlLe_jmK0ma_WcVoS_tw1XQ9CF3IOx45m3_yFBxLj4xRG3vAT2Sr4VtTpKLKNfIBq6G1xEz2M2EtSycpkDqAN1WKscGVlOJ7VITeiCScaFiJUb9WJX71qqLKhD3fzOsQb8UuHlbsBxQunZMoMoy0AjluGRIuHwRjVcTI2gj-PVjQ-9bYTKUwqZqEHYWnIDtWCzj9qvhbj79IM876Wvk4F96X6JlQZLVduMog7erkcd4Ls5KmARr2fVAesRW_Lvt6wXLsfCIa1v3dDIMGwwaBo8xOU8thp1Kz-yc4Q_zNrbbio9KHfeDOMBM1vzidAj_32q-EbRtVzJGg6B3T9LIbtUbVP6F8QFcWjS7YJCTpzv9NM6aOk-ElUrQGrGFvrttTDVsM44bff0kttYL_GHg8ZMemikGDLXHSsDRE4MGw3j5ddypmK0LkxoGM5I5Lr5pwysI0vIvNRZdSs1ZXUdcPXKPCsI-lqxw-YXXGXWg0EjA4SO2eeP0mGMMelLOd3NHqijuBkRe9VDkPUWxIYwnFRcmXzjQBuhGqfnaz1YYEdhaMuCibgs1LRfnajGiRb4VEQszziGcd1JviOMO1Ik" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : خاورمیانه دیگه اون خاورمیانه‌ی قدیم نیست، ایران هم تاحدودی هنوز قویه و ما دیدیم که تو درگیری‌های خلیج فارس چطور میجنگه.
ولی بنظرت چرا اونا تو یک ماه گذشته به ما حمله نکردن؟ چون میدونن که ما قوی‌تر جوابشونو میدیم.
الان یه محور شیعه‌ی تندرو هست و یه محور تندروی سُنی هم داره شکل میگیره، ولی ما با کشورهای مسلمانی متحد میشیم که اینارو قبول ندارن.
درحال حاضر اکثر ایرانی‌ها، به اسرائیل احترام میذارن.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20421" target="_blank">📅 20:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20420">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">کانال ۱۲ اسرائیل: نتانیاهو در حال برگزاری یک جلسه امنیتی با حضور وزیر جنگ و رئیس ستاد مشترک نیروهای مسلح است.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20420" target="_blank">📅 20:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20419">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38c66da50c.mp4?token=jwWJpBVbJ7T9wGyhh7AeBBpl-RG5VDeB3NJuoUptgI51WWNj_m-Vw8LKzPIHp6cqr_X-77kZFYKDRGTHMwP0VgMwM-FDSOUkm-cCq9VqYFmdTkX2HdQRALzCZH2XCewkUo_JPNln-_1bDv-CpEvZGNyXALLuXEW25DtJWmvathl43jAzPmBKN0XachhCfflaDfgn_3SEZGkfTtIbVu08Mq269POy6zgdE1jIzmjaI1hOyFpXcL89xRvTeKnWiykb2kgnBsQ-D7IbDOepKBgmPu7An8mUJrKp6w65VPdnTmhkOMgd97yKGdL6YlksvJUPw05v0L8oU0TgphaPAezzdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38c66da50c.mp4?token=jwWJpBVbJ7T9wGyhh7AeBBpl-RG5VDeB3NJuoUptgI51WWNj_m-Vw8LKzPIHp6cqr_X-77kZFYKDRGTHMwP0VgMwM-FDSOUkm-cCq9VqYFmdTkX2HdQRALzCZH2XCewkUo_JPNln-_1bDv-CpEvZGNyXALLuXEW25DtJWmvathl43jAzPmBKN0XachhCfflaDfgn_3SEZGkfTtIbVu08Mq269POy6zgdE1jIzmjaI1hOyFpXcL89xRvTeKnWiykb2kgnBsQ-D7IbDOepKBgmPu7An8mUJrKp6w65VPdnTmhkOMgd97yKGdL6YlksvJUPw05v0L8oU0TgphaPAezzdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : نیروهای آمریکایی همچنان به اجرای دقیق محاصره اقتصادی ایران ادامه می‌دهند. تا تاریخ ۳ آگوست، سنتکام ۴۴ کشتی تجاری را تغییر مسیر داده، ۲ کشتی را از کار انداخته و ۲ کشتی را توقیف کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20419" target="_blank">📅 20:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20418">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQwLob_7VAXAbIXXxgv-oTuyU259HZNTLNtO5v8y3XdZg94IeblnNU-uqH_UPNWr5287Fl6ro6kwPInACLc4iSmbCmKR_yuQ3XXrp3xYI3ecod5RrI0JZVFlbKx4ktqNa9r9kCaMdt6OYNFL0XYBr1Cpixy1hAOSNHYgW70URumvXhmLQADlLznNaOXDcYjpsCg9k8YCIZNDp3L2_M9o1C2Ds8HKry4tVzbyQAHUGno2ZTAjkcBla3I9GB7yCXfbIng8WjuE8sXsiTEihiuyRhp7L0E48L5_B5sy9hEgOjHwYQylAs_iEpsmlXvZ8fBMXUNH0Iudj-EPTioBMB_7DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : یک چترباز ارتش ایالات متحده در حین اعزام به خاورمیانه، آموزش سلاح‌های سبک را انجام می‌دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20418" target="_blank">📅 20:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20417">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مارک لوین :
من از اسرائیل حمایت می‌کنم
من از اوکراین حمایت می‌کنم
من از تایوان حمایت می‌کنم
من از مردم ایران حمایت می‌کنم
@WarRolm</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20417" target="_blank">📅 20:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20416">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">خبرگزاری سی بی ای : مقامی آمریکایی اعلام کرد علی رغم ادعاهای ترامپ هیچگونه برنامه ریزی برای مذاکره با مقامات ایرانی وجود نداره
تماس ها صرفا از طریق واسطه ها جریان داره
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20416" target="_blank">📅 20:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20415">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20415" target="_blank">📅 20:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20414">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03f509353.mp4?token=H-V09Y5F6yX2OgCzTZtVUxTwJE8VFzvhjoqH-W4hc3TM3ZqlVgS3eEotMbNCh1ku7kgY_bopeAfx5kn8OF96BmSobWKKdoA_KmKkJoPIWiYmyXP6u7eC1Lp0P-1oYK64Pbb9UGlB40KT1yMAJ3jv4Q3SRJtIprUAO4YZzVVGNiwMGX1QHitaSuBYTMPiPevt2hdNOeyozTCyInRvR7DtJseoZnS4UTj6sBwM1D3yxXk20hN-yNSyui7ScgqRJpDENvVLN4Kx0vzaxZ6W4cA3_xwvqjdvbMI-GBxE0uZ3n0roMRUjSPS0o3KC77JESG0G2fiOC8MhsoW4XFduoGb0Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03f509353.mp4?token=H-V09Y5F6yX2OgCzTZtVUxTwJE8VFzvhjoqH-W4hc3TM3ZqlVgS3eEotMbNCh1ku7kgY_bopeAfx5kn8OF96BmSobWKKdoA_KmKkJoPIWiYmyXP6u7eC1Lp0P-1oYK64Pbb9UGlB40KT1yMAJ3jv4Q3SRJtIprUAO4YZzVVGNiwMGX1QHitaSuBYTMPiPevt2hdNOeyozTCyInRvR7DtJseoZnS4UTj6sBwM1D3yxXk20hN-yNSyui7ScgqRJpDENvVLN4Kx0vzaxZ6W4cA3_xwvqjdvbMI-GBxE0uZ3n0roMRUjSPS0o3KC77JESG0G2fiOC8MhsoW4XFduoGb0Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20414" target="_blank">📅 20:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20413">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CjjQ9frJxMkGDQ-Hu6mU00lUVSGODCYHsfvs7NbyM3hvv6rq4kbIfe4K3FR_3TiuNMvW30fntR4ZLuUJnmImPjRuWbigRAPPdvBlrUtT0HtolFE48LLhBdaptxSoN1elmW0IgMY_9_miQQ9qHXgwQEqwPz4Cnh28iC51Y5rx4V-ZI9O_Z9wNkkVNOKnBQEPqXqbE3PAF5JYjkJ2_hgCC1kf7Qn_bKyYTomoK-SsR9C23T19ZKUvhWqlPHbJG2UqKHCiLD0eYKD88TkuITsAxfkMhMur7byx9Ex96ZhwWRxPJ5W4Fz1txPTBCo_k9lq53i80uuhv9fs3Ct_5R1QgNKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث :
رهبری ایران به شکلی باورنکردنی دورو و فریبکار است!
آن‌ها درخواست برگزاری جلسه می‌کنند؛ بعضی‌ها حتی می‌گویند «التماس» می‌کنند. گفت‌وگوها آغاز می‌شود و قرار است در آیندهٔ بسیار نزدیک جلسات بیشتری هم برگزار شود، اما هم‌زمان آشکارا و با افتخار ادعا می‌کنند که هیچ مذاکره‌ای در جریان نیست، هیچ موضوعی در حال بررسی نیست و فقط با «عمان» در ارتباط هستند.
@WarRoom
بعد هم طبق معمول شروع به رجزخوانی می‌کنند و می‌گویند تنگه هرمز را با قدرت در اختیار و مدیریت خود دارند؛ در حالی که این تنگه هم‌اکنون به‌طور کامل تحت کنترل نیروی دریایی ایالات متحده و «محاصره دریایی» ما قرار دارد؛ چیزی که برخی از آن با عنوان
«دیوار فولادین ایالات متحده»
یاد می‌کنند.
هیچ چیز بدون اینکه ما بخواهیم وارد ایران نمی‌شود و هیچ چیز هم وارد نخواهد شد، مگر اینکه یا
توافقی
حاصل شود یا
تسلیم کامل
صورت بگیرد.
چه ایران بخواهد این واقعیت را بپذیرد یا نه، ما در حال مذاکره برای یافتن راه‌حلی برای مشکلی هستیم که خود این کشور طی دهه‌ها به وجود آورده است.
موضوع بسیار ساده است:
ایران هرگز به سلاح هسته‌ای دست نخواهد یافت
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20413" target="_blank">📅 20:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20412">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">یک منبع ایرانی گفت که تهران پیشنهاد اخیر ایالات متحده را رد کرد و تأکید کرد که تنگه هرمز تا پایان جنگ به طور کامل بازگشایی نخواهد شد.
این منبع همچنین ادعا کرد که واشنگتن بسته شدن مسیر کشتیرانی جنوبی را پذیرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20412" target="_blank">📅 16:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20411">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20411" target="_blank">📅 16:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20410">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">لحظه نشستنش رو استورررری کردم
instagram.com/yashar</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20410" target="_blank">📅 16:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20409">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c929d388fd.mp4?token=m5ogrsO_RpM6QmZEaVqpdcsfkXnm65BgE6cDGoMqopbuQZDFMbbKIS9J1ip_jXKqM_JnQoZkAUW86MpsczqiHY0_kdd0A1Tke6t6wA1cO1becDiTaOiPFAUegxK1NahQH7b7VmHHmHRXSx_zaMuOJgZ5b0yhJh2ec_e9NbKJw1aWitj3zD001S7Jy-JF66K6WBRuyo6-wGD2MfmZ_7gyBpw-v79WZAaV98_KJ3PVBfHDPVpCe1bYXo8C_9AI64g8sO_8b7GwkYyWyk7oZpFbg2y-ulj4siiddyeKM_4k3jtjUZu87qNgd3UKSyOmwDNFxqJ8eKbEIcVHY4N6fwVKVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c929d388fd.mp4?token=m5ogrsO_RpM6QmZEaVqpdcsfkXnm65BgE6cDGoMqopbuQZDFMbbKIS9J1ip_jXKqM_JnQoZkAUW86MpsczqiHY0_kdd0A1Tke6t6wA1cO1becDiTaOiPFAUegxK1NahQH7b7VmHHmHRXSx_zaMuOJgZ5b0yhJh2ec_e9NbKJw1aWitj3zD001S7Jy-JF66K6WBRuyo6-wGD2MfmZ_7gyBpw-v79WZAaV98_KJ3PVBfHDPVpCe1bYXo8C_9AI64g8sO_8b7GwkYyWyk7oZpFbg2y-ulj4siiddyeKM_4k3jtjUZu87qNgd3UKSyOmwDNFxqJ8eKbEIcVHY4N6fwVKVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20409" target="_blank">📅 16:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20408">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اتاق جنگ بایاشار ، رو سفید تاریخ : ویدئوی اتاق جنگ مربوط به ۴ روز قبل از شروع جنگ ۴۰ روزه(۵اسفند)، هواپیمای ریوت جوینت از همین مبدایی که امروز پرید، یعنی میلدنهال انگلستان، و به همین مبدأ که امروز میرود یعنی جزیره خانیا در یونان، پرواز کرده بود و من به شما گفته بودم
🙌🏾
@WarRoom
I TOLD YOU
🫵</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20408" target="_blank">📅 16:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20407">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">صدای ری اکشن هاااااا نمیادددددد</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20407" target="_blank">📅 16:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20406">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پیج اینستاگرام رو باز پروندن ! و بازم برگردوندم !
😂
پیج دوم رو داشته باشید حتما
instagram.com/yasharmotors</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20406" target="_blank">📅 15:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20404">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd1c503433.mp4?token=SA8pwGXinTYMZzhG7ac8U206-V701LbS9l7nqwdf09EFXVXcQW6gVtZISZNXyghiyyP7CX0TJGAxuzanMDnxvrzC0CHWM3rORZKd6_fj1tdIMmtmvFe00XodQAqdgpYfqUsma1R4PgDDshVBBn6rz9Q5Y0jeyzzYd0l3LqnzQEB4OpoRM6IBp8OKCMays2dM33BIrjzUFIR65lCJIbWXeNA3UIesqfVph2hs4-5rTIB_TivQhBmfBfooczw3m6BzHe3avrtX4PjzMkLyaPL94abeS9PyGQQyFeQFniqvVSVrxSbLHXfEAIZEbNdDYe6N2xWPvRN7Jm7_6YwvUDsWC1aLb_LaC0Bvt82pGpz-CuRQHQ1ctvlNzWb3WwgRDJTpt7r0Tl-lWjQmGJYMOrdtCSviqXXVZdkDnnoZn5--DTcwvQgz92npc36C2eS7vqw4CKr_-UCPok4wV8HVmN2JIoCzMk_OHImuL9plgDn6O_gfJlJWoorLmaJk-n2RKoD31xTQz9qXacAh_CQoNknOGg19h8mMiWdCfhRZx_F517KBB2FT2sXVuvzsvu020KMepDgSZC87sgLxhhQAXnIaOXhAofqkuV5R3gUvLb7oJi1MHXEX8-Ti2khkF7HgudMwB8qNtT8XGf25wZLz2P74p1vw9rHPqkrR0KmpkrCOX00" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd1c503433.mp4?token=SA8pwGXinTYMZzhG7ac8U206-V701LbS9l7nqwdf09EFXVXcQW6gVtZISZNXyghiyyP7CX0TJGAxuzanMDnxvrzC0CHWM3rORZKd6_fj1tdIMmtmvFe00XodQAqdgpYfqUsma1R4PgDDshVBBn6rz9Q5Y0jeyzzYd0l3LqnzQEB4OpoRM6IBp8OKCMays2dM33BIrjzUFIR65lCJIbWXeNA3UIesqfVph2hs4-5rTIB_TivQhBmfBfooczw3m6BzHe3avrtX4PjzMkLyaPL94abeS9PyGQQyFeQFniqvVSVrxSbLHXfEAIZEbNdDYe6N2xWPvRN7Jm7_6YwvUDsWC1aLb_LaC0Bvt82pGpz-CuRQHQ1ctvlNzWb3WwgRDJTpt7r0Tl-lWjQmGJYMOrdtCSviqXXVZdkDnnoZn5--DTcwvQgz92npc36C2eS7vqw4CKr_-UCPok4wV8HVmN2JIoCzMk_OHImuL9plgDn6O_gfJlJWoorLmaJk-n2RKoD31xTQz9qXacAh_CQoNknOGg19h8mMiWdCfhRZx_F517KBB2FT2sXVuvzsvu020KMepDgSZC87sgLxhhQAXnIaOXhAofqkuV5R3gUvLb7oJi1MHXEX8-Ti2khkF7HgudMwB8qNtT8XGf25wZLz2P74p1vw9rHPqkrR0KmpkrCOX00" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : خودش بمبی نمیندازه ولی همه بمب ها پشت سرش می آیند !
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20404" target="_blank">📅 14:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20403">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اتاق جنگ با یاشار:جیمز باند.
قدرتمندترین هواپیمای جاسوسی تاریخ، ریوت جوینت، در حال ورود به منطقه است.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20403" target="_blank">📅 14:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20402">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20402" target="_blank">📅 14:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20401">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9e4766f60.mp4?token=HajCDrR3yyz7jTpkgDh6heXZPbfcDt5AgZrt6DgbFiag6inOJM8_sGfAatnJHm2srrf5L0rLx6ABbOOswZDn22i6bwqN_IpZP4BLFbR_3_uk3sKIcde0wFfJTPj4aVFNJ_Rn45cbT07j77Pg1l9NjScEd7jykqIHi2wn47FWPArFbLKqEkWkqwKIItSfqqNhzBttuT1_DPQtGFkmSSnlhYGxBDyysov5RHxH6y2TOSN6NCPcJGkjm_1aKm_QFpOCZYTsvfVNpc3wywQUNBm2Q_4KxPz2iSND12BtapILCy-8WLkkHO_-QR-c8KRhLg9ZDvwJ15dGk0K-_wzdWjj7DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9e4766f60.mp4?token=HajCDrR3yyz7jTpkgDh6heXZPbfcDt5AgZrt6DgbFiag6inOJM8_sGfAatnJHm2srrf5L0rLx6ABbOOswZDn22i6bwqN_IpZP4BLFbR_3_uk3sKIcde0wFfJTPj4aVFNJ_Rn45cbT07j77Pg1l9NjScEd7jykqIHi2wn47FWPArFbLKqEkWkqwKIItSfqqNhzBttuT1_DPQtGFkmSSnlhYGxBDyysov5RHxH6y2TOSN6NCPcJGkjm_1aKm_QFpOCZYTsvfVNpc3wywQUNBm2Q_4KxPz2iSND12BtapILCy-8WLkkHO_-QR-c8KRhLg9ZDvwJ15dGk0K-_wzdWjj7DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهده دود بزرگ و غلیظ از سمت ساوه دید از قم
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20401" target="_blank">📅 13:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20400">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">رسانه های رژیم : یک فروند پهپاد MQ9 توسط آتش سامانه نوین پدافند پیشرفته نیروی هوافضای سپاه بر فراز آسمان تنگه هرمز رهگیری و مورد اصابت قرار گرفت.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20400" target="_blank">📅 12:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20399">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">بقایی: ‌در وضعیت تنگه هرمز تغییری خاصی تا زمانی که آمریکا آتش بس و تفاهم نامه را نقض می کند تغییری رخ نخواهد داد @WarRoom عراقچی هم امروز به کربلا میره و مملکت تعطیله</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20399" target="_blank">📅 11:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20398">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">بقایی: ‌در وضعیت تنگه هرمز تغییری خاصی تا زمانی که آمریکا آتش بس و تفاهم نامه را نقض می کند تغییری رخ نخواهد داد
@WarRoom
عراقچی هم امروز به کربلا میره و مملکت تعطیله</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20398" target="_blank">📅 11:32 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
