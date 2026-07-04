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
<img src="https://cdn4.telesco.pe/file/S3IdUroGKnTseHkP9ZLAZKAWQvGTbB9RI1irxMNz9_cnkg9iA97KLB-GBZGZwSj2vT6SUuQQV8T-tybNH2Cytf_LxZ0l8jqoJfJInd_Bf_ZWENIiYgntSi0jZEJBC9LPG-9hMIbpgMWnSzaRiUY5tZY0XuBH728vLdx4mvecXYNqgajYbt6YpXz08nW0y4IC071Hx1fXnMCwHOOD2O9peum64VA8s6UpMlNUlS8sFFouElzgLba0kpH7KnRFcAW25sPbGkMKS90dHZNDUtzb6h76FrwGAd8hjZ1EmSt_PsZNRtP7RaL2WC247Udx97RDiw_Bc7fYQpDfSw1999iRiA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 936K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 11:38:00</div>
<hr>

<div class="tg-post" id="msg-131710">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
محمدباقر قالیباف در دیدار با رئیس پارلمان عراق: درباره مدیریت تنگه هرمز موضوعات مهمی در تفاهم اخیر با آمریکا به امضا رسیده است و بر اساس قوانین بین‌المللی، اداره تنگه هرمز باید میان دو کشور ساحلی ایران و عمان انجام شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/alonews/131710" target="_blank">📅 11:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131709">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
انفجارهای کنترل شده برای امحای مهمات عمل نکرده، امروز در جنوب اصفهان (ارتفاعات صفه و بهارستان) انجام میشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/alonews/131709" target="_blank">📅 11:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131708">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0S1hKT_xPq7Sp82zVQd0CwynUuRvrxWAz7FhHLzaMsXNuD4GfCI5dGGJTvts5fGWS0cm_Miu2_i03gvE8i7O_9qZUwd4M6ZoiemquTq3_KIQ0fDk3cJHwaWYPTmYrMOrLyR93KrYgC8AdPnTu0_oofT9uLVepzlv9XBlBodS89gubjB-hB9CRP4vnrmFqN5gk_hvylNK5QA0BKdSHM-eMKxpZwC8IqRllIDTAxj-_AuzkXOOdAbUrRwoA1eN1Yuow87XE5jVPJ6m9RC1qMENXW5w7XXv3ZWHiAspcYAM9kDt1dQ2H-mjhfiUKOIRVcKyJZXUpvUW5sl-PPA6ioKPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر منتشر شده در رویترز از مراسم امروز در مصلای تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/alonews/131708" target="_blank">📅 11:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131707">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
مدودف: تنگه هرمز اکنون برای ایران به سلاحی تبدیل شده است که از نظر اهمیت دست‌کمی از سلاح‌های هسته‌ای ندارد؛ اما یک «سلاح هسته‌ایِ» دیگر نیز وجود دارد و آن تنگه باب‌المندب است.
🔴
روسیه، ایران، چین و دیگر کشورها می‌توانند درباره ایجاد یک پلتفرم مشترک برای کشورهای تحت تحریم به‌منظور مقابله با محدودیت‌ها و تحریم‌ها گفت‌وگو و رایزنی کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/131707" target="_blank">📅 11:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131706">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
ارتش اوکراین کنترل شهر کوستیانتینیفکا در شرق این کشور توسط روسیه را تکذیب کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/131706" target="_blank">📅 10:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131705">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
تعطیلی سراسر استان تهران در روز سه‌شنبه اعلام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/131705" target="_blank">📅 10:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131704">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
فرانس۲۴: عمان قصد دارد پای کشورهای‌اروپایی را به تنگه‌ی هرمز باز کند
🔴
از آنجا که‌ایران قرارداد تقسیم تنگه را با عمان به امضا رسانده دیگر حق قانونی برای جلوگیری از این موضود ندارد
🔴
در اولین قدم نیروی دریایی فرانسه قصد دارد در تنگه هرمز مستقر شود
﻿﻿﻿﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/alonews/131704" target="_blank">📅 10:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131703">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIYKnCFsitnicjchj1lmbm0XgEyMIagtr4VU6xuSiil0KzfvpabPK-pYii323d8dTBoLzadd2xO4SKyY8GirwU2Bq0MBTGEp3OEd1rmo1uq7JVjTxORDJq8Nk47qSNaL1_inG5EvIscs2WpLl4br2glGd49kO_u8cljGgsxh9uAfPw1k8krKN5Z_gdXabVlIJy6fF1cePOHPNpYhjre0LBJUwuRXxG8QMTG5ItCyRW_FKK2fvyI2rOAj_MjnHDKPLyelUAhTEXhGyE3ZjwskMwcJLl7RzrWHBY-q3bOTdDmbvZmB08ItWlHBkG2U0qPGSKqnm7s_Ap7l4Lmlk_Y97g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فعالیت سنگین نیروی هوایی آمریکا در خلیج فارس
🔴
نیروی هوایی آمریکا در حال اسکورت کشتی‌ها در آب‌های عمان و جمع‌آوری اطلاعات درباره جنوب ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/131703" target="_blank">📅 10:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131702">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
سی‌ان‌ان‌ به نقل از مقام‌های آمریکایی:
مقامات دولت ترامپ از نزدیک شبکه جاسوسی اسرائیل که در ماه‌های اخیر، فعالیت‌های اطلاعاتی و جاسوسی خود علیه ایران و آمریکا را افزایش داده، زیر نظر داشته‌اند
🔴
مسئولان آمریکایی تلاش کردند به ایران درباره این نگرانی که اسرائیل ممکن است قالیباف و عراقچی را ترور کند، هشدار دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/131702" target="_blank">📅 10:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131701">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxieX523kjDauR7BsGGOUVHRzQV09HVLzCYDcWIhjIwojRRCR35iLjJHojglfrV6MyxZzlUVF_4lZZotKnTYhH3t0Db1RORinu1R83-5y04re_3EjvLJekTN8TP2CLPQW7EusI6RfFsALoNgiti5fVTVkMabhC7SVVDKP-3Fh_contz3Z26Qkbrn1DWP-SXdmtfgUBTYr60EYh1r6vUskL9MWB1sU8qBbMnImvGUXa0ehVG4KRruLMYLwnrdjciRYPqK7jXYLHLYiwQwtIckX-_VWWuwAx-3dVvASaq9qwIWlYJoYBau_Aelz_63SAwC-gqQGzTJNijw8rvYeo79xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدار غریب آبادی نسبت به هر حرکت نظامی در تنگه هرمز
🔴
معاون وزیر امور خارجه در واکنش به بیانیه مشترک فرانسه و انگلیس: تنگه هرمز میدان نمایش نظامی قدرت‌های فرامنطقه‌ای نیست. ایران به‌عنوان قدرت مسئول و ضامن امنیت تنگه، نسبت به هر حرکت نظامی در این آبراه حساس هشدار می‌دهد.
🔴
امنیت هرمز با دولت‌های ساحلی است؛ بحران‌سازان مسئول پیامدهای ماجراجویی خود خواهند بود؛ این هشدار جدی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/131701" target="_blank">📅 09:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131700">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
گروسی: تاکنون نتوانسته‌ایم به تأسیسات هسته‌ای ایران دسترسی پیدا کنیم؛ این موضوع به مذاکرات جاری میان ایالات متحده و ایران بر سر تفاهم‌نامه گره خورده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/131700" target="_blank">📅 09:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131699">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
خبرنگار الجزیره تأکید کرد که تاکنون هیچ اظهارنظر رسمی از سوی واشنگتن منتشر نشده است، اما رسانه‌های آمریکایی به نقل از منابع آگاه از وجود «تفاهمی موقت» میان ایالات متحده و ایران برای کاهش تنش خبر می‌دهند؛ تفاهمی که امکان ازسرگیری روند مذاکرات را پس از پایان مراسم تشییع رهبر فقید ایران، فراهم می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/131699" target="_blank">📅 09:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131698">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
مکرون، رئیس‌جمهور فرانسه: دو شناور مین‌روب را به خاورمیانه اعزام کرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/131698" target="_blank">📅 09:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131697">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGJjwxtf7iYr2VbUTILjnG3fW8vbs29wkIjue4tSCMX2zjsNdRGpn4STzJJ3YJF2gstmli72EWTnClQPaSZz7_5GENyqf4PXYZz6o82OoMn-S2nMII8epdLRcLCg1gAgpW_jSgNZNvhGYIi6ry6_r-uvrwJdoJr8KS9ZymU1DXloY0b34tqlmseVIRtf6UVIOiqlsRa3z2TYvi1yWpDuJcXVjVzSwcqdH-NAtTwIZ-8PSiioUQOYkAnNZD35t__OGmEUjEcli066_sJZecP98H9xAtlj3tVKJZfz2d2eLm48n81AXq1tPOe2DnYt_FLlAq8RKSWhL-L22SJDEfOQ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عربستان سعودی از پهپاد انتحاری دوربرد «SKYWASP» رونمایی کرد
🔴
این پهپاد توسط شرکت SR2Vector توسعه یافته و برد عملیاتی آن حدود ۱,۵۰۰ کیلومتر (۹۳۲ مایل) اعلام شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/131697" target="_blank">📅 09:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131696">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
فرانسه و بریتانیا آمادگی خود را برای استقرار یک نیروی چندملیتی به بهانه حمایت از آزادی دریانوردی در تنگه هرمز و تضمین عبور ایمن از تنگه هرمز که یک موضوع با اهمیت جهانی است، اعلام کردند.
🔴
فرانسه و بریتانیا هر دو همچنین بر تعهد خود به ثبات منطقه‌ای و احترام به حاکمیت همه ملت‌ها تأکید کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/131696" target="_blank">📅 09:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131695">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lRZNcM57R9BtrxJCPDuxLVghPmEcZvoFdNFskEiaK7fpROzBpzN6QezYxSVcxqhysv1tTgGbmc-Ynx3MO1QGaujD_PAWKT8mR_P_KlpA_jxelC-HDImnW4vD0B1BYuR-xT9V3HPQzS5GMT_0x5kLrASs0Nq6Fl-vZU2E8UYsLqjuqdmGrbg-gEoQ2iU-VV1PEHix13aWewlYrt2bQeb0pLWFuWtNtf4GX6ggwkbvDq26btQdR2rWhG7DaQS9QFp9kIlR6r5lcDyxF9QrgPKkbyMjH7sTDDJKxwnZH6oDAT_5X7fgpqTjtGiNms2C3X5smGBzhGHvGfNrnMJbiv52Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله هوایی نیروی هوایی اسرائیل در نزدیکی تپه استراتژیک علی‌الطاهر، در جنوب شهر نابتيه، لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/131695" target="_blank">📅 08:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131694">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
متروی تهران از امروز ۲۴ ساعته شد
🔴
مدیرعامل متروی تهران: تا ساعت یک بامداد روز سه‌شنبه، ۱۶ تیر، خدمات مترو به‌صورت ۲۴ ساعته و رایگان ارائه می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/131694" target="_blank">📅 08:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131693">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
منابع محلی از حملات توپخانه‌ای اسرائیل به منطقه «ارنون» در جنوب لبنان خبر دادند. گزارش‌ها حاکی است اسرائیل این منطقه را هدف حملات سنگین قرار داده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/131693" target="_blank">📅 08:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131692">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeebf5f487.mp4?token=M5PeEn7qv9-Jvnzflazn47EP1zv0O4prOGaqMZUw0TYZkc_OLa78WFAfqPowrv8Gg7KoR4H2plFR3VHn-g4M9pkZMWBX8WWgKjJYDCYZiCMFYvZPLmGohxSwOgKCtlsEOKIpAmuTvcq-0Nqx4I2_6LNhHifPGjz7JDTEAZ5nuhTJSgtG56KXbrnRWKyKlIYpc0LuS0TGNHGikEYj-r3yfcAKcQatiWrqiKl6Ka35gq9nvJfcd7u4I0YAUSPn0ImHg0bReG25yZoxs--r4ahUivk1wviGLJXkObu4VVCnhY6Fi2vXNzUka6tI6r_TNmGDEQ43oklt1Qdhq5HQEV7VlVz19BrXpMEzAP4mrlvNZNmJTfcLYVhaKAb9UY92I_vdjm3WpI61BQjP4NbYrhoURq7wkjkxlpSiJINXlaOdgfZHRcwoIRdzOnanZqa4zh0LSoWlgxyU7ymPN-vKKTqunly3cllyB8p-OGeE06lLXH7kCgMOV7dT-0J1SaHjOko58Oho5w4xF8gaL487ccDlI1lfv-ipGsDNrBi0FKdvWyzT8vNokDktB3eGQTPnC_2sJa-SqpP4L0-YM2dzm40Eez5islWZ0nM-ORN-EbZowid1nl5K-bebAR8DxveDAalb3AU6lzFeWgrU3C_SdFTF6WPqWIEljzvjO6JfpRWn1q8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeebf5f487.mp4?token=M5PeEn7qv9-Jvnzflazn47EP1zv0O4prOGaqMZUw0TYZkc_OLa78WFAfqPowrv8Gg7KoR4H2plFR3VHn-g4M9pkZMWBX8WWgKjJYDCYZiCMFYvZPLmGohxSwOgKCtlsEOKIpAmuTvcq-0Nqx4I2_6LNhHifPGjz7JDTEAZ5nuhTJSgtG56KXbrnRWKyKlIYpc0LuS0TGNHGikEYj-r3yfcAKcQatiWrqiKl6Ka35gq9nvJfcd7u4I0YAUSPn0ImHg0bReG25yZoxs--r4ahUivk1wviGLJXkObu4VVCnhY6Fi2vXNzUka6tI6r_TNmGDEQ43oklt1Qdhq5HQEV7VlVz19BrXpMEzAP4mrlvNZNmJTfcLYVhaKAb9UY92I_vdjm3WpI61BQjP4NbYrhoURq7wkjkxlpSiJINXlaOdgfZHRcwoIRdzOnanZqa4zh0LSoWlgxyU7ymPN-vKKTqunly3cllyB8p-OGeE06lLXH7kCgMOV7dT-0J1SaHjOko58Oho5w4xF8gaL487ccDlI1lfv-ipGsDNrBi0FKdvWyzT8vNokDktB3eGQTPnC_2sJa-SqpP4L0-YM2dzm40Eez5islWZ0nM-ORN-EbZowid1nl5K-bebAR8DxveDAalb3AU6lzFeWgrU3C_SdFTF6WPqWIEljzvjO6JfpRWn1q8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: در آمریکا، ما به زبان انگلیسی صحبت می‌کنیم، زیرا این زبان، زبان بنیان‌گذاران ماست. و برای هزاران سال، این زبان، زبان آزادی بوده است
🔴
یک آمریکایی همیشه خواهان صلح و آرامش است، اما ما هرگز از خطر یا تهدید فرار نخواهیم کرد. ما همیشه خواهیم جنگید، جنگیدیم و خواهیم جنگید، و همیشه پیروز خواهیم شد، پیروز شدیم و خواهیم شد. ما باید این کار را انجام دهیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/131692" target="_blank">📅 08:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131691">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
ترامپ: شما می‌توانید به کارل مارکس وفادار باشید، یا به آمریکا.
🔴
شما می‌توانید یک کمونیست باشید، یا یک وطن‌پرست. اما نمی‌توانید هر دو باشید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/131691" target="_blank">📅 08:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131690">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fd5cf7670.mp4?token=f6lU_bd8BnYE4r4OHQipMUJHW7XgrbZRsMmBuGDGD3K6NzvqyUIY5wQ943s9vI4K56kGmJvPboGTAxarRaODpH6UbzzttsefsEF3EnV0u6_yy61PFDvvtX11pFmB5wF_tteVVw3Jgm72FRJhKc6wNyQb47FpcrFhut4MiRAMWFqvZDUrrV9D2FWqmJnDuAKRVPTzwSnulckErvdoJa5bOuID-_xBX774FaMrdkCrLxHC6WRiUCX7tNWC6rzHLh3W31xOC7fqr9DmKPbJ7WIYoC6N7Gp4jTJwi6jHVB6U7sP17ORZbpyaEHqMtAxwWmAYj9bftJsxELvlGvANT5uJDDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fd5cf7670.mp4?token=f6lU_bd8BnYE4r4OHQipMUJHW7XgrbZRsMmBuGDGD3K6NzvqyUIY5wQ943s9vI4K56kGmJvPboGTAxarRaODpH6UbzzttsefsEF3EnV0u6_yy61PFDvvtX11pFmB5wF_tteVVw3Jgm72FRJhKc6wNyQb47FpcrFhut4MiRAMWFqvZDUrrV9D2FWqmJnDuAKRVPTzwSnulckErvdoJa5bOuID-_xBX774FaMrdkCrLxHC6WRiUCX7tNWC6rzHLh3W31xOC7fqr9DmKPbJ7WIYoC6N7Gp4jTJwi6jHVB6U7sP17ORZbpyaEHqMtAxwWmAYj9bftJsxELvlGvANT5uJDDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما ضربه مهلکی به ایران زدیم. آن‌ها مشتاق به حل و فصل [مشکلات] هستند. آن‌ها واقعاً می‌خواهند این موضوع را به پایان برسانند.
🔴
ما به آن‌ها یک هفته فرصت دادیم تا مراسم تدفین برگزار کنند، زیرا ما مهربان هستیم. این حقیقت دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/131690" target="_blank">📅 08:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131689">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHk3sVp09VgcZk8h4q3YQgTJfEeF4S5KDoULPDIPVM7Oc_7xi-7r0VUAHHHxGBDx5i9Q005_wVUaqsiENW3t51BEwh3DOIRYJ_t9hmyMqEhOyeXTAa8AQWjrrbD8s79_Bizy1cyOxk9mEXxddMjouh8s23WebkVeFuwQaKR8Nc9tM7RyZMwDGuov8oPWhoYf8P2Ps4hUlF47EvIz3eTYWOE8tgK4EUSYpJnaIK2BmJf2jTIA7xAH8NfH-dSRuBTeHCgIGNdYvIXFtOkfSl6sAyCGryJBhNyt-bj6oqGFlqaa76FOrJQAo__Kdm5vtLrZZ3qE-7Fxn9lAybsnQX_-qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بزرگترین سایت کاریابی روسیه، برای دفاع از آسمان مسکو از دست پهپادای اوکراینی به دنبال استخدام داوطلبان اپراتور پهپاده!
🔴
وظایف این شغل شامل آماده‌سازی قبل از پرواز، شناسایی و جمع‌آوری داده‌ها در روز و شب است؛ تنها مهارت‌های فنی اولیه رو هم داشته باشید کافیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/alonews/131689" target="_blank">📅 08:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131686">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/prgNmX9H2Kr_Tj3vw9zhkbLcvRjDX1E98_vQm7-eFKNR4RnYZa-89JBCfKoS6JMvk4WAjFbeQQzGMapOdBeTnyhPzVQ-xYfLi1ICDIFkk_7PrwP6INwlbK4U35M6G2t9uIrmg1ACnUOSDUqjQs-EsVOSQQZ3-mjDNRQGmRMmnqR35m272pYB5ZWsTpYCqkLA4ekyfII5nseIVPd0CP5LBLJQOAYyzy71C65W4R51dGqfpk0Vl5eMuMDBRWoL23IXFJOODms1G-81sHtlv6c4KoFkOsZsRZ1nhy-THzX9nye_363X7iNdesFCC8ZQaE1U2aZdNsEWBeZDWr_zVZkgbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mk1eKhpx_A6YTa5gl89rretYos67CqV66s8Qp9UyOSeUS7njvbY1ANha_dgIVrTRMRz5BhfwujEMN7p3jpu7A2Dj72W83RZBgjeHCPtODbYm34kiBHJ4DGdHdyFutlcavwGSVJwFyitSeVZTOREmjsEsg-LvbSf2iInsj6ed9UaH8Z1gDz4sOc538qLP6inYGKGlkk2v8tv2dZq8MQnzGn70Y6aRTnckisCCEtKB3nQHZcF7tExlZc8sn1x15LK1l3oy9d9EJ9IJCRd9ZNTM4bv1GdaDjjkepRK7QGZHkY5J8yYS2LwYnO52Ns3LqwrMrW1DH_ZH8SJbkl8B_LJqQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L3HwToLVxFasxwAh44xLl3CS17vz1RHoMKsf0KjnFLRhZ2evvH3_qcF1OQbga8QOEpUSFf7tKxvdBhw9jp3phMUslPyQzz38VvzBdkBnnLhRB49GO6VVLvP08_srv5dwUl_cjbwjjpC-05U7GLXzHf379ZadtC5lSZu92qhIjhzFVB0HoIw_e_b3qJzhTTHtsJb26FmTW9neRca5yMszJkCPGCaCPiMiI8DLUqDmh6e--xyREWI3B8XVRwcc6eQABohvekBrVCE1InyRinea0t-e_iRAIbli2MOoqboN6QCUn-2Y0eeKPvbW-T9g8VecR4FjwNXEOjaAZ3Roh8ZJ6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
هم اکنون مصلی تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/131686" target="_blank">📅 05:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131685">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a79a851cf.mp4?token=KowiR8ryM0fUyiyUN_DCZttg9H_gmUuBgBnKDTGbPcxgxZQA-q5aXUZmcAx2x5LgmieiBxM2Dwfx6xJ35KjqghySdFaPzqchTvRdp5C9vh9UFhEu56NlQ14-Ps2kkVABx6M4Br7s47ATIKT_3O9P6UHuvrGHDBVBK5ed-Jx0JJ_gvYt7aJbOQdL1zVJRuMvUbFi8BG36C9MSoTXctWgevLbWwb3NYQV0Sm3sogv6x0Z0v5T1HJoP4o5TR-5IzgN1n32s-VdH4-yNSXY_eM1L5-_YdJjzu9x1f549psgyEEtMDNNWcu592D4afzehc8U0QCe5LnLMYQ9uba_R5iRXCoZCcnatS0e0qv8c-M1swIE-XffSHPzJLtglec0l-El_s_xAa5mlTanmGfH2VD5ldaey5WkKS2ZIycfZVr08W7tzbCFQGUt0Cu-_DpndbIuNh6wn7DZfrg5Uu5DxHWJCAnCq-E7Zl-E_UNIg4XUS2F4deoNi05WlEawtSpFAwm9Nma7NicQPuCp4oxvA3HlwqLcy0qqrxI2wxgKyVUta0sbkw-n9pabIOCbQ_E_nuOptMkSNkkEDGC9svpyerLTeeGeUHfffIto7XMw9MFXvHqTrYLBCUlF_Nls9EpB8EBw5cNtHMDlFYVR1fmOdMzsekUrDnyoK4pRrUTZdvNHCHhc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a79a851cf.mp4?token=KowiR8ryM0fUyiyUN_DCZttg9H_gmUuBgBnKDTGbPcxgxZQA-q5aXUZmcAx2x5LgmieiBxM2Dwfx6xJ35KjqghySdFaPzqchTvRdp5C9vh9UFhEu56NlQ14-Ps2kkVABx6M4Br7s47ATIKT_3O9P6UHuvrGHDBVBK5ed-Jx0JJ_gvYt7aJbOQdL1zVJRuMvUbFi8BG36C9MSoTXctWgevLbWwb3NYQV0Sm3sogv6x0Z0v5T1HJoP4o5TR-5IzgN1n32s-VdH4-yNSXY_eM1L5-_YdJjzu9x1f549psgyEEtMDNNWcu592D4afzehc8U0QCe5LnLMYQ9uba_R5iRXCoZCcnatS0e0qv8c-M1swIE-XffSHPzJLtglec0l-El_s_xAa5mlTanmGfH2VD5ldaey5WkKS2ZIycfZVr08W7tzbCFQGUt0Cu-_DpndbIuNh6wn7DZfrg5Uu5DxHWJCAnCq-E7Zl-E_UNIg4XUS2F4deoNi05WlEawtSpFAwm9Nma7NicQPuCp4oxvA3HlwqLcy0qqrxI2wxgKyVUta0sbkw-n9pabIOCbQ_E_nuOptMkSNkkEDGC9svpyerLTeeGeUHfffIto7XMw9MFXvHqTrYLBCUlF_Nls9EpB8EBw5cNtHMDlFYVR1fmOdMzsekUrDnyoK4pRrUTZdvNHCHhc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فارس :ساعت ۶ صبح بیاید مصلی تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/alonews/131685" target="_blank">📅 01:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131684">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/667106b64a.mp4?token=kz810Gvf8Mwf30Ra5_kvfIYAsJhiFxtjmbSQy3ZfBBxJQGT7nF98mPUcPTSzyMALefRjqaGEWaaK_5IH8fQ2yv0TEKc665Zz6nfKBSy_M5I0e6yRow8FY9-J7BmX9RZxKOnmYwW0tl9AsYJhGZknH_huWZdfActUyabzudRFp-pWUlMKNP6NrlPhoYhNr4I_aDzQXb8bvH9_q0FcXYlW5Bkh1WuDGumajeOBqxBBFXdRppfhlILC4Gn2Pp2u2rS0Ecni0_SS81uObl5OTaLQZscgJG0dqxFtD7_YzfF83x6HN0Kr4NnAX0OIYuvQixcj9SOOVK0EKp2YL4-hDwds-oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/667106b64a.mp4?token=kz810Gvf8Mwf30Ra5_kvfIYAsJhiFxtjmbSQy3ZfBBxJQGT7nF98mPUcPTSzyMALefRjqaGEWaaK_5IH8fQ2yv0TEKc665Zz6nfKBSy_M5I0e6yRow8FY9-J7BmX9RZxKOnmYwW0tl9AsYJhGZknH_huWZdfActUyabzudRFp-pWUlMKNP6NrlPhoYhNr4I_aDzQXb8bvH9_q0FcXYlW5Bkh1WuDGumajeOBqxBBFXdRppfhlILC4Gn2Pp2u2rS0Ecni0_SS81uObl5OTaLQZscgJG0dqxFtD7_YzfF83x6HN0Kr4NnAX0OIYuvQixcj9SOOVK0EKp2YL4-hDwds-oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موزیک ویدیو کامل آهنگ جدید توماج صالحی به اسم «تو چی؟» که تا تونسته به رضا پهلوی دیس داده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/alonews/131684" target="_blank">📅 01:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131683">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
توماج صالحی یه موزیک ویدیو به اسم  «تو چی» داده و رضا پهلوی رو دیس کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/alonews/131683" target="_blank">📅 00:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131682">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiNsjJ1iavbklIhh17lVhazii-izRmAG13PmIqfUhLeHA7TTggndo8hMaRkAa0npv-jdtWon8-PolzpdWxfF5UxYHmyhwziPZQNwB5cA0iE_2Ofuwtf30kjHlvDB1WA6Aklp5ZWtSmnFocIz4FE1y5lFoLBJRxRQVtHgtLRVshGvXAbeP3_iMRjmBQNT_wofMpvjpkxsKa7CRXCxaSm-MMDFLTMroGT0M0JelrG5MDzpIb0ZcgTi6tUdAp3yk5LWELElkCQVVj1xCEqyRiPwvJiFBgiT5QsYMgGeQ5Ou6vxmyfnvfAvMXfHwBwMiFSaoqn0zJFPHyCRvchrNWI7LVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ در تروث سوشال
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/alonews/131682" target="_blank">📅 00:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131681">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d68bfd54e.mp4?token=drwhBEDjuPy4H2IOYPXmhK4M1jvZ3HK89nuS9OArC2d3I3xz-U09Yfjhncj0BzWO9HDE6kFQPTYJfBeJwm4C_k_Auh4rldP0tpjMbUnIAWCA6DVy9EWXZdHSFnFq_ECIMWSWvb80EEfMGd7CFkwhOVaz04UeJE3pKVFoIC9HHAqJcaBZrRDuzO7JhxoC70U2fakt_h2o5DDjiv9K6itPbGNY5EJ8jGI32ej3bOeRZxFosurulf2qQtikLyje6FQVwDFXBCiEtYCPMcCUlZakuK_GdAg4e8ZGh-dxZNlR8xTzxBWxba9_KFtyJ6FHOhB0UB7OiswBPAmgz7kMm3CSYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d68bfd54e.mp4?token=drwhBEDjuPy4H2IOYPXmhK4M1jvZ3HK89nuS9OArC2d3I3xz-U09Yfjhncj0BzWO9HDE6kFQPTYJfBeJwm4C_k_Auh4rldP0tpjMbUnIAWCA6DVy9EWXZdHSFnFq_ECIMWSWvb80EEfMGd7CFkwhOVaz04UeJE3pKVFoIC9HHAqJcaBZrRDuzO7JhxoC70U2fakt_h2o5DDjiv9K6itPbGNY5EJ8jGI32ej3bOeRZxFosurulf2qQtikLyje6FQVwDFXBCiEtYCPMcCUlZakuK_GdAg4e8ZGh-dxZNlR8xTzxBWxba9_KFtyJ6FHOhB0UB7OiswBPAmgz7kMm3CSYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توماج صالحی یه موزیک ویدیو به اسم
«تو چی» داده و رضا پهلوی رو دیس کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/131681" target="_blank">📅 00:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131680">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
مکرون: ناو هواپیمابر شارل دوگل در پی امضای یادداشت تفاهم میان آمریکا و ایران به فرانسه بازخواهد گشت
🔴
پ.ن : تاثیر گذار بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/alonews/131680" target="_blank">📅 23:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131679">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIuVr87DN48mRkKzD-3lTLZrsNu89ecgxAHRaS73QpafudGMGb6x7TePo1Dvq7f20Fhdb7og5Z1X5DyBbUF7RppkUvQoLy5doKTyByOFvp5i_FL1kwXoQkCCLEv6egclqgqYacJHJd-w8ntckIRo2tb6QEvZpXadp-0YONTP31mI_5YtINdS1LZSgqo1QFm2XWizXkK6Ac3QLnpTnFphxmXMf_4s4uIZQkZrRIcFwQ7qQq48-2AiDYg_vyA7kz9Zs7J-hqqxZrqf1_lzyshijDgxJVQ2x8_oBib8kRojkrwLOaS66IjEFTAQQGM_aouLHInDpkCA8GcJv8sCSUR42g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخست وزیر پاکستان بعد از ایران به ترکیه رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/alonews/131679" target="_blank">📅 23:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131678">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
فوووووووووووووووووووری</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/alonews/131678" target="_blank">📅 23:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131677">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
فوووووووووووووووووووری</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/alonews/131677" target="_blank">📅 23:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131676">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brMBg6fgltoVq7NRa8ynlR4mSt2XX9UQnbrYkSbPsGoiGAz73MgVpRHjczbkV3NHc-5m8NAOexCrcugZhzgLqqc2m7PcAEPRtvJrQm90w3WZKCgCCUtoAJ9R507bLE6q2zLlIY1vN7e2WgCcBwmw5Sbvlgm0jbZYAAsz7AAdQrFRoq5D0fbGRL0wE11OReq_yjKNUoVk5PB8bpXwyQ3_HJa9_KuDtvTF3e7R1IbJ94hHNI8l_FaSbpRSI4SPQYe9pbUyBXA84Qh9ziVuk9p3MizjtGnQnJAv4lnbq2TfAGfx4OJXNGEUzDzbAcP_WC2bEFTQ1xeuu7dxVBw5KXW7zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل به فارسی: ابراهیم ذوالفقاری چون تو مراسم تشییع رهبر شرکت نکرد،پس صد در صد مطمئن شدیم هوش مصنوعیه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/alonews/131676" target="_blank">📅 23:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131675">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrvzamxIC3wOvA446rIRbiZ_bexqkNA7_iVBv8bdc7HSmXlufCIhyLNbQTThzofAArM1DKV9E-I-MPJQAmu35KPUuMdmrHDkAqXHuYM_aMkvr_R-w7euXEKqm4HonR78-Gf488zWB9mSMzdrhd22wGN91xtWzosrUJ4zyX3dugu4P6cQZNBZkQyJjiOZ-p5zakpTyQBLoY8zSS91oOvhuG0eancsYU87r11mzbfx6b8bykMY8fPUEIW_Q0XrKyKeSltQocMNQMUvbSDZiFWjkebLJDDyzTdiOPOS_fKGP4LX0hRFGe6QKAehyoUpqzagle9tCaePjEWARrQisbX3kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تصویر بسیار منشوری و زننده دیگری را همسر سپهر حیدری در اونلی فنز منتشر کرده!!! که به شدت وایرال شده
◀️
مشاهده بدون سانسور</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/131675" target="_blank">📅 23:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131674">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aff6ec588e.mov?token=b0W5o2yKFNszC8w0oHx3achW4XVcbjZsuVf_8cSjAZkmwqwOP0VjTUUezjdVhYy7le6eYwFpFI1Gpf15FA0M57-m_oK1zKFJBiafTzLuSKq_M-H6GYOhm7Cg-TODXhBPZ9T3fdF7nWZcLonYtupYKcP-sIYpv4kA1teNZ4wiReJWZC5Lrj-yFhLWqFogBZejYgSZuNIpFCN4rqMzacjAUz_EEauOttEq_SqYH2YTtC81VXMfC3Kz9SZZvs1SeUucBRas89ygqH1IkxZ3GpOkcyGmjrLrOPBvp26uxyvLdXY2sfx0XGQaHD-aGuqNZDeJkSJn7PtzxkxfKVoJ8Td1dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aff6ec588e.mov?token=b0W5o2yKFNszC8w0oHx3achW4XVcbjZsuVf_8cSjAZkmwqwOP0VjTUUezjdVhYy7le6eYwFpFI1Gpf15FA0M57-m_oK1zKFJBiafTzLuSKq_M-H6GYOhm7Cg-TODXhBPZ9T3fdF7nWZcLonYtupYKcP-sIYpv4kA1teNZ4wiReJWZC5Lrj-yFhLWqFogBZejYgSZuNIpFCN4rqMzacjAUz_EEauOttEq_SqYH2YTtC81VXMfC3Kz9SZZvs1SeUucBRas89ygqH1IkxZ3GpOkcyGmjrLrOPBvp26uxyvLdXY2sfx0XGQaHD-aGuqNZDeJkSJn7PtzxkxfKVoJ8Td1dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پوتین یبار دیگه با لباس نظامی ظاهر شد و گفت که نیروهای روسیه ابتکار عمل استراتژیک رو تو خطوط مقدم جنگ در دست دارن
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/131674" target="_blank">📅 23:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131673">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
سخنگوی کرملین دیمیتری پسکوف:
پوتین دستور داده تا به دقت تحلیل کند که کدام از متحدان کی‌یف در تحریک ادامه درگیری‌ها نقش دارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/alonews/131673" target="_blank">📅 23:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131672">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9r7cyrgy8w51x9MPpEpGXFvWDnJ1iE7kPK-n9mgvqU5qulnh4UZZgdJROVf-d1c0M4KSZImMoLCJcKAuMzwjqtkOhvDrJJ651Fxw1Tlo2cSuiiNPHun0GS7E01Eofvh-i9Xa5J4qBcnNVLA2Zlmj_9m0NTMKOJZv-hjSr48wC6JQYbKh08bO5RW9pvupIDHRAgFzdLgM_XUJeZhTiAC6dfekPQCmhlZ_11oHbItBeR5pxaNQNTX_k5C7l_sCMOfixpkPBlfoYSoyqY-41WS7V_WCtMxcSGA5vlCtjwLra4qdkEJcqVtLElzcgJwjrYVZy_LX03p8I1CjlvPE_SRTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال: افتخار بزرگ من این است که همین الان برای شش نفری که توسط دولت بایدن آزار دیده بودند و در زندان بودند یا به زندان فرستاده می‌شدند، به خاطر «تعمیر ماشینشان»، بخشش امضا کرده‌ام.
🔴
در حالی که می‌دانم این موضوع مسخره به نظر می‌رسد، با این حال یک واقعیت است و بخشی از تسلیح‌سازی و احمقانه‌ای است که کشور ما مجبور بود در طول چهار سال طولانی خواب‌آلود جو بایدن تحمل کند.
🔴
من همه آن‌ها را همین الان آزاد می‌کنم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/alonews/131672" target="_blank">📅 23:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131671">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6ccf94e0.mp4?token=ixas-OZBS06wVB0oHDOZhyhm85gDaSH7KxrNVfWFlSNrDOaFNbyd54sX7XgKmCLn3AuWuRZowKE67Akpd1_X5sDnO5loqybnfXzgcsT7Mb0F6CODDjlmxJ9Uq6F4h5tKhUb5XxscMyo9RxO1CQgh0OOO6gnJyuKeA-ZLPCGyqiWx7tmLlEimXFBXufvyZXGbQJEsZU7ougVPTft9feGn1gQgP0EPjyVAWeSACEpZt2mQMz9OKo4RPdyXlQOEpv5P6x4PDEgC_S0f6RFpW2Xt4TwvxP2E-DFnvR9jdgLYcO4MNfSdkz4uHswL4HenabJZolbEWvk-eiV1Qf0X0ulVgy4hOFUdfnsm-s-ni-nQgRTnHR8xrJRCG919NsVkraBRZNBG5cixACQWjpxawuxg33Th0_kftPDO9cv79ZAkh8M0_14esTCmmaWotuTFYNDZxpBg0cggyEh2eTpmR2MrrFbd255jtTtXsvJPDQwSR1bbKLVWXGkP143WJCnKRVNgU4a_P2SUmlXLZg_UkZHMZ-q2_is3BxbPBPpzkTRKrS1eKESRLSFHWp8sgviySGgJ6yzpB-k0JaWjRhXtYdAaGWGWcsOJ-YQJ5BvWnTG5rT5AWqgMyY9mHHEeS0iU6zJcVyCWPnqy0e19XR0zQKBNdvxyhvqlKOo5uI6UYSsIfN8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6ccf94e0.mp4?token=ixas-OZBS06wVB0oHDOZhyhm85gDaSH7KxrNVfWFlSNrDOaFNbyd54sX7XgKmCLn3AuWuRZowKE67Akpd1_X5sDnO5loqybnfXzgcsT7Mb0F6CODDjlmxJ9Uq6F4h5tKhUb5XxscMyo9RxO1CQgh0OOO6gnJyuKeA-ZLPCGyqiWx7tmLlEimXFBXufvyZXGbQJEsZU7ougVPTft9feGn1gQgP0EPjyVAWeSACEpZt2mQMz9OKo4RPdyXlQOEpv5P6x4PDEgC_S0f6RFpW2Xt4TwvxP2E-DFnvR9jdgLYcO4MNfSdkz4uHswL4HenabJZolbEWvk-eiV1Qf0X0ulVgy4hOFUdfnsm-s-ni-nQgRTnHR8xrJRCG919NsVkraBRZNBG5cixACQWjpxawuxg33Th0_kftPDO9cv79ZAkh8M0_14esTCmmaWotuTFYNDZxpBg0cggyEh2eTpmR2MrrFbd255jtTtXsvJPDQwSR1bbKLVWXGkP143WJCnKRVNgU4a_P2SUmlXLZg_UkZHMZ-q2_is3BxbPBPpzkTRKrS1eKESRLSFHWp8sgviySGgJ6yzpB-k0JaWjRhXtYdAaGWGWcsOJ-YQJ5BvWnTG5rT5AWqgMyY9mHHEeS0iU6zJcVyCWPnqy0e19XR0zQKBNdvxyhvqlKOo5uI6UYSsIfN8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار CNN که مجدداً به تهران آمده است، از جزئیات مراسم تشییع  می‌گوید
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/131671" target="_blank">📅 22:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131670">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
بر اساس گزارش شبکه NBC، حساب‌های سرمایه‌ گذاری دونالد ترامپ، رئیس‌جمهور آمریکا، در یک روز قبل از توقف تعرفه‌های بزرگ، 327 خرید سهام پنهان انجام داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/131670" target="_blank">📅 22:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131669">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
استاندار تهران: راس ساعت ۶ صبح فردا درهای مصلای تهران باز می‌شود؛ قبل از ۶ [خبری از بازگشایی] نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/alonews/131669" target="_blank">📅 22:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131665">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b6d85daac.mp4?token=tbHLTnfNKthFQA90M0J5Wrf74fGos5pK1kb_B0JQ5L3bi72NNDfHs9NEnHr0xog70VZcwG6wuvDtDkqPewlhDGI8eVWisEQO9hNEeaJXRsFP2Z23HHD0v9kJEWj0xL-6-Ql1flrNDd-kkXkFHoPZY_1zsfxq5paV1Mw3AWG4QSDfcawrej4WEfhIl-ganDJ3iavAmREAO-NWOQO_RoVsgi2WtLMkbDkyFUveGuq60PpNvyl_TO3rGl0zQ1GCEr_hGKnd2_FPXvwcWy537Ar5PIJ5Me4JrFrxvpQ8H-K1xXYJv5ve2UAxq7Yof9cAZkqRKLucB0mR10c8ElkVOe4Reg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b6d85daac.mp4?token=tbHLTnfNKthFQA90M0J5Wrf74fGos5pK1kb_B0JQ5L3bi72NNDfHs9NEnHr0xog70VZcwG6wuvDtDkqPewlhDGI8eVWisEQO9hNEeaJXRsFP2Z23HHD0v9kJEWj0xL-6-Ql1flrNDd-kkXkFHoPZY_1zsfxq5paV1Mw3AWG4QSDfcawrej4WEfhIl-ganDJ3iavAmREAO-NWOQO_RoVsgi2WtLMkbDkyFUveGuq60PpNvyl_TO3rGl0zQ1GCEr_hGKnd2_FPXvwcWy537Ar5PIJ5Me4JrFrxvpQ8H-K1xXYJv5ve2UAxq7Yof9cAZkqRKLucB0mR10c8ElkVOe4Reg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های آشپز برنامه "به خانه برمی‌گردیم" صداوسیما که تغییر جنسیت داده و دختر شده :
تو 5 سالگی، یکی از آشناهامون بهم تجاوز کرد!
من کلا تو خونه پوشش دخترونه داشتم و این عمل، تغییر جنسیت نبود، تطبیق جنسیت بود.
من حتی دفترچه خدمت هم پست کردم که شاید از این حس فرار کنم ولی نشد.
تا 25 سالگی به کسی چیزی نگفته بودم ، حتی اون زمانی که تلویزیون می‌رفتم هم از همه پنهون می‌کردم.
2 تا خودکشی ناموفق هم داشتم چون اون موقع حس خوبی با جسمم نداشتم...
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/131665" target="_blank">📅 22:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131664">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✨
یکی از با کیفیت ترین و پایدار ترین اشتراک های بازار با قیمت خیلی مناسب حتما یک بار تست کنید کاملا مورد
تایید
در هر صورت تمامی سرویس ها قابلیت مرجوعی دارن و هرموقع راضی نباشید میتونید مرجوع کنید
➕
با کد تخفیف زیر میتونید با ۵۰ درصد تخفیف خریدتونو انجام بدید(فقط100 نفر اول)
✅
🎁
کد تخفیف :
Express50
.
🤖
خرید سریع
:
🤖
@Team_express_bot
🤖
@vpn_express_sup_bot</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/131664" target="_blank">📅 22:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131663">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚀
سرویس VPN (V2Ray) تیم اکسپرس
✅
اتصال پایدار و پرسرعت
✅
پنل اختصاصی (مشاهده حجم و تاریخ انقضا)
✅
سازگار با تمام دستگاه‌ها و اینترنت‌ها
✅
مناسب استریم، بازی و استفاده روزمره
✅
تمدید و خرید مجدد بدون تغییر کانفیگ
✅
بدون محدودیت تغییر دستگاه و IP
🛠
پشتیبانی تا پایان اشتراک
💬
تعرفه‌ها
🔸
پلن‌های یک‌ماهه
▫️
۲۰ گیگابایت — 100,000 تومان
▫️
۴۰ گیگابایت — 190,000 تومان
▫️
۶۰ گیگابایت — 280,000 تومان
▫️
۸۰ گیگابایت — 370,000 تومان
▫️
۱۰۰ گیگابایت — 460,000 تومان
▫️
۱۵۰ گیگابایت — 680,000 تومان
▫️
۲۰۰ گیگابایت — 900,000 تومان
▫️
نامحدود (مصرف منصفانه ۳۰۰ گیگ) — 1,150,000 تومان
🔹
پلن‌های دوماهه
♦️
۳۰ گیگابایت — 190,000 تومان
♦️
۵۰ گیگابایت — 280,000 تومان
♦️
۷۰ گیگابایت — 370,000 تومان
♦️
۱۰۰ گیگابایت — 505,000 تومان
♦️
۱۵۰ گیگابایت — 730,000 تومان
♦️
۲۰۰ گیگابایت — 950,000 تومان
♦️
نامحدود (مصرف منصفانه ۴۰۰ گیگ) — 1,350,000 تومان
🔸
پلن‌های سه‌ماهه
▫️
۸۰ گیگابایت — 480,000 تومان
▫️
۱۰۰ گیگابایت — 555,000 تومان
▫️
۱۵۰ گیگابایت — 785,000 تومان
▫️
۲۰۰ گیگابایت — 1,010,000 تومان
▫️
۳۰۰ گیگابایت — 1,445,000 تومان
▫️
نامحدود (مصرف منصفانه ۵۰۰ گیگ) — 1,650,000 تومان
خرید:
🤖
@Team_express_bot
🤝
فروش عمده و پنل نمایندگی:
📩
@expressuport
📢
کانال اطلاع‌رسانی:
🌱
@vpn_express_sup</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/131663" target="_blank">📅 22:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131662">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fj1dqY_GfdkUUP0gn6DDDWKCHOAbHKvF_1hhjwOpH3qA_8A915ZjMF-_BfjuM6vHKRNW7-kt-SOE4MdiTmnyTNL3o7iIsgehX30fwDtn-_cfw534IyNAGXHHbO119Y0aUFEB8z2DqLheOQoQkVq7CWMa64bnK0f9VSkO1OxJy8votd_cuNUEac1hVuOiEFe8Tcg4LNPZdFxVtszgkBpWJYNbg0L36B_t83IcElZ2W0veSkO4M51awab7-0_2kXGjuPvol3K1wmPoEN0plRs_JJM2Ilnqfmp1HH6QmlOiLyfXmW7Uj6dYVEc6Azfkg6Y4cacSbKYIh0oAVOV6aY1R1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف به ترامپ: به فکر سوء تغذیه ۴۰ میلیون نفر در آمریکا باش، مشکلات خود را به دیگران نسبت نده.
🔴
ایران خودش درباره دارایی‌هایش تصمیم می‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/131662" target="_blank">📅 22:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131660">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
حسین یکتا: ترامپ که می‌خواست ‎۳ روزه کار ایران را تمام کند، هنوز خون‌خواهی ملت ایران را ندیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/131660" target="_blank">📅 21:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131659">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoThN3hchJWvN12i2xx-NdJv1k55QxX__Y8gZzkNdFvXoKoGz8fWk8NJnX_MKuMmd6AlF49Bq3bvg-r9Wa7iisIEyTNMcE0tiifmNVIxiYXVr5xdZWoBVxmRroE3vaBNNwaopKGKKHvFi06wtDw1B9Z7NoRjgUbptLaZyWNmFArgUxfKT_h2vZqLGGfYPdiPOmWGM5tgCmAup8GYiCqiHQhS4ShqbEhb7aJd9hNJUIuIMKgGGpIUXqSJ6-ViqvDLua2WtARjoay8KLrTnoPXjziHx1lXUELiJ6ZcZN5gTm1bZHVLxQoEalujUSJMc14-cmXHk_5siwYxyTTSdRxfPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سال قبل در همین روز، مجله تایم عکس سیدعلی خامنه‌ای را صفحه اول گذاشت و دقیقا بعد از یک سال روز تشییع جنازه علی خامنه‌ای شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/alonews/131659" target="_blank">📅 21:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131658">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
فرمانده قرارگاه خاتم: اولویت‌های دفاعی تعیین‌شده از سوی قائد شهید امت، دست نیرو‌های مسلح را برای پاسخ به دشمن باز کرد و پیروز شدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/131658" target="_blank">📅 21:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131657">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
المانیتور: مقام‌های اسرائیلی به‌طور غیرعلنی امیدوارند ایران مذاکرات شکننده را طولانی کند و آن‌قدر آمریکا را خسته کند که ترامپ دست‌کم محاصره دریایی کامل و تحریم‌ها را بازگرداند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/131657" target="_blank">📅 21:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131656">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
سی‌ان‌ان: رفت‌وآمد کشتی‌ها در تنگه هرمز در حال افزایش است
🔴
هفته گذشته ۳۳۵ شناور از تنگه هرمز عبور کردند و پیش‌بینی می‌شود این هفته نیز تعداد عبورها در همین حدود باشد؛ به‌طوری که تا پایان امروز، شمار عبور کشتی‌ها به حدود ۲۱۵ مورد برسد. این در حالی است که پیش از آغاز جنگ، به‌طور متوسط روزانه حدود ۱۰۰ کشتی تجاری از این تنگه عبور می‌کردند.
🔴
اگرچه روند کلی فعالیت‌ها در حال بهبود است، اما بازگشت کشتی‌های تجاری بین‌المللی احتمالاً با سرعتی کمتر از ترددهای محلی و منطقه‌ای انجام می‌شود؛ زیرا بسیاری از مالکان کشتی، اجاره‌کنندگان و شرکت‌های بیمه همچنان رویکردی محتاطانه در پیش گرفته‌اند.
🔴
ابهام درباره خطر گسترش درگیری‌ها همچنان پابرجاست، به‌ویژه پس از آنکه حمله ایران به یک کشتی در هفته گذشته، عملیات تخلیه دریانوردان گرفتار در منطقه را متوقف کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/131656" target="_blank">📅 21:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131655">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
باراک راوید: ترامپ امروز با نتانیاهو تلفنی صحبت کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/131655" target="_blank">📅 21:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131654">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/En7BOMnzLTvP48ajB25RqWND0O7hmoE2PTAD9tcRM4AeqqxlEqGLNUyj5CcQ1EtTE7yabt4XofNii-TUAHafmcmfUN_dUF7DPlIHoO9HqK2igbPi4fn_yJeB3wMJSjcwXF67dSdsx2PTplHFAUv1pxA9f5FxTeWlbLZl0CNMC_dtlOORz8-LIJOtNy7MFNf9TrjMmeUJqcFkjwZxcYOKngp8Rb2sDRhfPcsKsZJ_enrTmVEUY2iUIs42Ww9Ed1Y0r-a3opTCjA2fMJCrhIceomymsiItJc_ATEcu6azlwpc8FaeA4hawogrbziXIVH4Bgt2wV5ypHHGPdM7pLdYVNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇲🇽
با اعلام رسمی فیفا، علیرضا فغانی به عنوان داور بازی انگلیس و مکزیک انتخاب شد.
@AloSport</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/131654" target="_blank">📅 20:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131652">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5c6feb8e70.mp4?token=JZCUOqbs7Fgo6AhT0HPiqTEWY43u8CkkwV7uZZmczyOjk6XaPdMlcapqXyowBKMyyX2qQ0x7Qzk3LxT9rnee3zAZ4KUmnxqEPzJ-P_FB79-U9mnY0hU7B7HSCV7CDIkuJmE5bQoErzPhbcZvWEiJFzA0qU3QNZsS8ybWqKc1lJvkzQGCwz5GZ_xt1rwaEwT1QRWCQvUTcnUMPchyM_vhkrR7AOvmNsOexqpjz6POU3JtzS2JXdG7wnBndZ0aQHfTf1uuMeLXYFfJnbg4HppXrIUzSOItC-9Taw3qMjmlp-EZBbAUKweRrHnCo7jGb1m9LpTtScvdIo7NDsxwFW2A2jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5c6feb8e70.mp4?token=JZCUOqbs7Fgo6AhT0HPiqTEWY43u8CkkwV7uZZmczyOjk6XaPdMlcapqXyowBKMyyX2qQ0x7Qzk3LxT9rnee3zAZ4KUmnxqEPzJ-P_FB79-U9mnY0hU7B7HSCV7CDIkuJmE5bQoErzPhbcZvWEiJFzA0qU3QNZsS8ybWqKc1lJvkzQGCwz5GZ_xt1rwaEwT1QRWCQvUTcnUMPchyM_vhkrR7AOvmNsOexqpjz6POU3JtzS2JXdG7wnBndZ0aQHfTf1uuMeLXYFfJnbg4HppXrIUzSOItC-9Taw3qMjmlp-EZBbAUKweRrHnCo7jGb1m9LpTtScvdIo7NDsxwFW2A2jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تیم نمایش‌دهنده جت‌های جنگنده F-35C نیروی دریایی ایالات متحده در حال پرواز و معلق ماندن بر فراز نمایشگاه ایالتی بزرگ آمریکا به مناسبت روز ۴ جولای و ۲۵۰ سالگی آمریکا است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/131652" target="_blank">📅 20:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131651">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1445c04c7c.mp4?token=ga0sJUmFhy-uG6QOA957VC0NlFJTs6jsrrJ09iBCtaqAO9OfCf08FNEZ82OJIvtDk_5e9rHc6VZS_Sh01cDTlCvd6YsJ6-37nqX0eel2arB1JFySHYYDRGqr6ZaM28llj0PHjv0bULbW6YrQoag6fs0A65Ic_QEjbbAXxFqufhPeDl0J4Qz4IM03axs3Ovl-zOpaZAeH9BwjXqtxWDn-i5VGbr21r6vKhB3RdZLEljUpacsdFj04-i_pJJGN8D3AcOaUUbGO2ux6oNdb5KEeRIDkAOt20-8G-0p-NqWrnTpjxwJAkMUupVvsG_jXz34v5rBWrYWbydV9JO_x8JMKgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1445c04c7c.mp4?token=ga0sJUmFhy-uG6QOA957VC0NlFJTs6jsrrJ09iBCtaqAO9OfCf08FNEZ82OJIvtDk_5e9rHc6VZS_Sh01cDTlCvd6YsJ6-37nqX0eel2arB1JFySHYYDRGqr6ZaM28llj0PHjv0bULbW6YrQoag6fs0A65Ic_QEjbbAXxFqufhPeDl0J4Qz4IM03axs3Ovl-zOpaZAeH9BwjXqtxWDn-i5VGbr21r6vKhB3RdZLEljUpacsdFj04-i_pJJGN8D3AcOaUUbGO2ux6oNdb5KEeRIDkAOt20-8G-0p-NqWrnTpjxwJAkMUupVvsG_jXz34v5rBWrYWbydV9JO_x8JMKgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توکیو به مناسبت ۲۵۰ سالگی استقلال آمریکا آتیش‌بازی کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/131651" target="_blank">📅 20:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131650">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
فوری/آکسیوس: نتانیاهو به زودی در سفری ناگهانی و قریب الوقوع وارد آمریکا خواهد شد و با ترامپ درباره ایران دیدار خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/131650" target="_blank">📅 20:14 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131649">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPKqrUt4MDxIR_IFuZhTFa8yH47EvsJW3mLQOtoaeBrE_7_gdYzgUE76nMmGRk6NeGjirPlycZUc_pZxK-ubVVEZXTYLwW36rWPx5YOPWmXZ2ihTEOi2MyzdnwCpQELWaDkHUqurPVxSE0kmnpjdFt9-Am6yBrBf_m65nvnhbp5ch0g3DL6cU3o0Ltg7xJPmFp1onzP7C9kbfof80bQlVTL8P9bgTxh7NDFAnOvmx31B5hOku1EL7smoOvtub7hwPINBwmxevrm0RmJvBb6JTCTuSM7hpQnqkWGRG0dhLTtH5Uv2VpCUJwwNm4j5Q8TSLzuty8IiJcCa6mQUUAjq4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک پست: رئیس‌جمهور سوریه یک بازیگر زن محبوب تلویزیونی عرب را برای مجلس انتقالی جدید کشور برگزیده!
🔴
رزینا لازکانی، ۳۶ ساله، به‌عنوان یکی از ۷۰ نفر منصوب‌شده احمد الشرع در مجلسی با ۲۱۰ کرسی انتخاب شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/131649" target="_blank">📅 20:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131645">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3767bfbca0.mp4?token=FkAW3X1DQPeAqMFkFk2iIx6HeGCd8ZYXw9gWIU_yW1Fq_3yZHSAxDwEAh3TpgVDHaJXspyDfzL9IoaGSlPBMRycCCI8YH9th0p_BcHW731VJH9rEJAuEHOnFgTN5UeSFv3l2UmJwRwR334hjBfGRoW9bPBeBq04zRiS0UJok265ZPsR2pq6z8oMLMSjtBGY2sfYWtbCegPKWF82hAJUsNCM51I1I-PnDAKzJ62zQ4PmmKcLtIh_xLleM_XZlV5X6gRV4FVV1zVp6cuD8pXGzkotFgKvSnQ0CQDxDfJ6CFqgzAw_uKJKo2AIJDPHdBC47rWO6aHs5jZnd4WrqZ58VYx58Vfv3lKiX9gHh5faceaFb00WSjh364NvNonXV1aLob3NbYikIqZk0HTRkUxcbG4xqL0B3b5GOYbP3B3vbiVZIqOBXW3d-eUqirdukjbI-p4IH20sA1MAdEhU8hT-qDYNGIMnt0TPvx8MvsZPcoJ7HOvE-7hWncr5GOtFF-LEsoZ-fy0Lz7aK8EGmHfPKgrLkDdBOkbKf9kQFwxcVkf0Mr2lPvrZwtBuuxw2HP9c-0PVLG3t_acJwS-8HbynneoNG-_cEd8PKrcezpuz7ehW6Twiky0MkKIMHJYBZuIvlKL2Ap7tWmcEQKSje8yzhjB4k2_vvkeEDOymOWj4PQSg8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3767bfbca0.mp4?token=FkAW3X1DQPeAqMFkFk2iIx6HeGCd8ZYXw9gWIU_yW1Fq_3yZHSAxDwEAh3TpgVDHaJXspyDfzL9IoaGSlPBMRycCCI8YH9th0p_BcHW731VJH9rEJAuEHOnFgTN5UeSFv3l2UmJwRwR334hjBfGRoW9bPBeBq04zRiS0UJok265ZPsR2pq6z8oMLMSjtBGY2sfYWtbCegPKWF82hAJUsNCM51I1I-PnDAKzJ62zQ4PmmKcLtIh_xLleM_XZlV5X6gRV4FVV1zVp6cuD8pXGzkotFgKvSnQ0CQDxDfJ6CFqgzAw_uKJKo2AIJDPHdBC47rWO6aHs5jZnd4WrqZ58VYx58Vfv3lKiX9gHh5faceaFb00WSjh364NvNonXV1aLob3NbYikIqZk0HTRkUxcbG4xqL0B3b5GOYbP3B3vbiVZIqOBXW3d-eUqirdukjbI-p4IH20sA1MAdEhU8hT-qDYNGIMnt0TPvx8MvsZPcoJ7HOvE-7hWncr5GOtFF-LEsoZ-fy0Lz7aK8EGmHfPKgrLkDdBOkbKf9kQFwxcVkf0Mr2lPvrZwtBuuxw2HP9c-0PVLG3t_acJwS-8HbynneoNG-_cEd8PKrcezpuz7ehW6Twiky0MkKIMHJYBZuIvlKL2Ap7tWmcEQKSje8yzhjB4k2_vvkeEDOymOWj4PQSg8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چتربازان و هلیکوپترهای گروه "گلدن نایت" در حال پرواز بر فراز نمایشگاه بزرگ ایالتی آمریکا در واشنگتن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/131645" target="_blank">📅 19:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131644">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COifDbQuOexX8hJ4QSnR6-Kmp4EjxRMMRRPKjbCm10SY3Yi8ldFXF515AyP4wZSpcTbBiAIEd7bap2rlIOijQ94F9VvZ4ZfvN9F7-VQNJ6nbNtO6TgTOkGdfXPrZxx2nN5nf4bhOXHX-hIusLyWxTy0pTzvd7XiYbaZEV1hknt8_V3Bo7UawStdJeAI4Kaha3OBXYi8tUrsWusW_vtQ-IyyXXF_bB5P-87cv-cR5OWGDWcpe0pHE2wZGzweMEWTFeWvI_NpwnskOtnVwFNBOoD4W5WYUn1XAy1-eWBrPoPag23OgvRrPjBpiux2ddT9hBnn8R5LxwE55iTOvumcOTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار عاصم منیر با عراقچی
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/131644" target="_blank">📅 19:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131643">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
فردا از ساعت ۵:۳۰ صبح مترو تهران فعالیت خود را به صورت ۲۴ ساعته آغاز خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/131643" target="_blank">📅 19:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131642">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ترامپ: اهمیت نداره که چه DNA تو بدنته یا چه چیزی مصرف میکنی یا عمل میکنی، وقتی به عنوان یک مرد به دنیا بیای هرگز نمیتونی تبدیل به یک‌ زن یا جنس دیگر بشی
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/131642" target="_blank">📅 19:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131641">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
حوثی‌ها اعلام کردند که جنگنده‌های سعودی را از حریم هوایی یمن بیرون رانده‌اند، پس از اینکه این جنگنده‌ها تلاش کردند از فرود یک هواپیمای غیرنظامی ایرانی در صنعا جلوگیری کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/131641" target="_blank">📅 19:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131640">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eizXhXu9KW576QlhLPD5VVogKrNaARrr9ZQ6CrI2swJOJq-8jBMDs3EkwOT9E7bfvudMNXpvX5UZnKDosjTY4ZGEl4AlPTit_EuHRez8XLn4XxHV3Ile-NlnZa2DdhNnPDO7xAn21zIt8r08NfXixHTQsUOYCKtLi27N0WGBPWfQL8VMRkGEqe5sCnv52bWWGL4osR3xrGHE40xvXa1Se0sOoAwDudnUS6_lkP0XBPvlV5FFpiANefERx9jvVl9xajAIG8iyluz52srZUEF0skrP51m2MTQEmcb97gxjlL7LELxj5vaXV8Jsuz5FrYRN342-K2ucXwFx8hGTUUduvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دفتر نخست‌وزیر اسرائیل، گزارش نیویورک تایمز را که حاکی از آن بود مقامات آمریکایی معتقد بودند اسرائیل در حال توطئه‌ای برای ترور مذاکره‌کنندگان ایرانی در جریان مذاکرات با آمریکایی‌ها در بهار امسال بوده‌اند، رد کرد و آن را «یک تحریف کامل از واقعیت» خواند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/131640" target="_blank">📅 19:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131639">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
اسکات بسنت، وزیر خزانه‌داری ایالات متحده، در گفتگویی تاکید کرد که افشای درآمدهای میلیارد دلاری اخیر دونالد ترامپ، رئیس‌جمهوری آمریکا از حوزه رمزارزها هیچ‌گونه «شائبه یا تضاد منافعی» ایجاد نمی‌کند.
🔴
بر اساس گزارش‌های مالیاتی و افشای اطلاعات مالی که اوایل هفته جاری منتشر شد، دونالد ترامپ از زمان آغاز دور دوم ریاست‌جمهوری خود، حدود ۱.۴ میلیارد دلار از فعالیت‌های تجاری مرتبط با رمزارزها درآمد کسب کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/131639" target="_blank">📅 18:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131638">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/alonews/131638" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👈
ویس لو رفته از ابویسانی، مشاور وزیر آموزش و پرورش که دانش آموزا زنگ زدن میگن بخاطر مراسم تشییع خامنه‌ای باید امتحانات عقب بیفته و در
جواب میگه خامنه‌ای و مراسمش چه مسخره بازی ایه
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/131638" target="_blank">📅 18:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131637">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7zbgo2Ald-VxIgMwA4NjcZjE6E4sOoSI3XyF1Pc07RMlIeAXr4SNzN3Hkunp1-mpk2LltrOI7pYHAu9PpOCfWCvDS2xdt3tXognCQWYTxXZa1VEXzXxGpyKrw4ZqXNqAir7T0iLZkX71XPY2ibLWXXB887vQyL5qkQ_hyn90oPq0dRKSO6JKH2VgAmCCsKGYoEwUvZkNtFpB4jd5JQyQaJ0DS91H0J1oAXiWZjVSWwChkQmIaas3ff8lLNosdp6Tpbuh1BNPZKlqh9jC_gBPHjdacz9B4ILrqqNfsE0XUenOLG9rMvGZVyaGOcBvxfmnATIPomIgJfxCvru6Bz2Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نگاه و تعجب عراقچی از گریه قالیباف که مورد توجه فعالان فضای مجازی قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/131637" target="_blank">📅 18:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131636">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
دونالد ترامپ درباره باراک اوباما:
من نمی‌دانم که آیا او یک بازیکن بسکتبال خوب است یا نه. من شخصاً شک دارم.
🔴
در واقع، ورزش مورد علاقه او گلف است. اما او به زودی در مسابقات "ماسترز" شرکت نخواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/131636" target="_blank">📅 18:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131635">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
ترامپ: رئیس‌جمهور آبراهام لینکلن از سوارکاری با اسب لذت می‌برد. من هم دوست دارم سوار اسب شوم
🔴
اما وقتی از اسب می‌افتید، من شاهد اتفاقات ناخوشایندی زیادی بوده‌ام. افتادن از اسب اتفاق خوبی نیست.
🔴
بنابراین، ما یک اسب پیر و سالخورده خواهیم داشت که بسیار کند و تنبل است، و شاید من هم سوار آن شوم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/131635" target="_blank">📅 18:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131634">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a185ba29be.mp4?token=Vo2LD-B5Mut3Bbnv2AUcaCuBE4BE22xjSlSZnJjer4pSWGu_Mma_kWXspkvve_DpWkUzHjUzi_Bb_9YnwK78SuTBLZa67AWX6xwNimeC-hPFWoYGjf1KJa3qTKLsgVd1Jp21LQJG1SqF2ORtnT7k_nEzGzUdhYgMDdJd5ctwg5thxxlTgcI9f2CVpMal7AUdCqqte_EDaq7d2ihz2epgpkegMQohbexGR30sV4kHFH6l9sKC-rTgWu91XKTgmbYMRX5JCLsdDveEszG9Du2i64gzxDPhd-qhlSOFKWrlLLEi9JtTmlt7l7iaWWxSakcbgsiWD5q1u059zIpKSMAEcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a185ba29be.mp4?token=Vo2LD-B5Mut3Bbnv2AUcaCuBE4BE22xjSlSZnJjer4pSWGu_Mma_kWXspkvve_DpWkUzHjUzi_Bb_9YnwK78SuTBLZa67AWX6xwNimeC-hPFWoYGjf1KJa3qTKLsgVd1Jp21LQJG1SqF2ORtnT7k_nEzGzUdhYgMDdJd5ctwg5thxxlTgcI9f2CVpMal7AUdCqqte_EDaq7d2ihz2epgpkegMQohbexGR30sV4kHFH6l9sKC-rTgWu91XKTgmbYMRX5JCLsdDveEszG9Du2i64gzxDPhd-qhlSOFKWrlLLEi9JtTmlt7l7iaWWxSakcbgsiWD5q1u059zIpKSMAEcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره بیل کلینتون: او در واقع آدم خوبی بود. من بیل کلینتون را خیلی دوست دارم. هنوز هم همینطور است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/131634" target="_blank">📅 18:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131633">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8AxU8CTjObYIN6RLb1WVVwy7py7FqZgtltM0TWDZInPp2T7FiSZWM3Q2HnjCb6cKlHckb63fMCPJUNQ0L4iLExPc8oUC03vPe12kxjsDUhVyczCITqAbLazv22bY7j19tptbY2cVk3_ve-Bh16hWEwnx7rpcO2APFcjMmUeQAqcDB2x-YZ1FYZZZTKaFokfGvPjt85OkCW4-B0lkoAr-8N8LLOkD_vS5NLoLqVIRHu8eEjT7kRZ_590jRHJmKAx2UheautFxfeGHKSUDjsEXEcxC16cXJIh_b4cGXbpdpPBnI61AcCm6vHrT4yLhS6tBFZmLrvCf_BeB4s7kMiImQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: تو این چند روز اینترنت رو قطع کتید تا دشمن سواستفاده نکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/131633" target="_blank">📅 18:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131632">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYGS8nPezzPwbpynfIo85KMEgQ_kTCVRpw1dasKq0__TNQcWqW1l8Yya6F5WZm_KmuNUZgvxHvyvI3fwnHcWUDo_B9FtVIzBoFtP_d0RGHzFA8vRaAnY92ayXHuqWQ9wFc6Hn7HLk3isvDneXGhwNjyO0pMlVlZRNQnJeqTefxbpGFwBxPy9YDDlBQcpu2GZw6cRWTnPXIiFH8RsrXRXWyAXMUaPSEZY0grVHkhhbHyUFyLgPD5VWbpd9rH__jPzrs9P7eypu1Copd3qhZSt176KzSyS0twBdjy3d04WrTP7kQynuXa7jzlwQ9MBgnLsCEYGEfF_sbgFEVq6gbu--g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بر اساس برآوردهای کارشناسان، هزینه جنگ ایران برای آمریکا می‌تواند تا سه برابر رقم اولیه کاخ سفید باشد؛ هزینه‌هایی که شامل جابه‌جایی تجهیزات، خسارت‌های جنگی، استقرار ناوهای هواپیمابر و سامانه‌های پدافندی، استفاده از موشک‌ها و بمب‌ها و حملات بمب‌افکن‌های B-2 می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/131632" target="_blank">📅 18:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131631">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
آغاز مذاکرات ایران با شرکت‌های ژاپنی برای ازسرگیری صادرات نفت
🔴
به گزارش جروزالم‌پست، منابع آگاه می‌گویند ایران مذاکراتی را با شرکت‌های ژاپنی برای ازسرگیری صادرات نفت آغاز کرده است؛ مذاکراتی که در چارچوب معافیت موقت از تحریم‌های آمریکا دنبال می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/131631" target="_blank">📅 18:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131630">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2ac75c7af.mp4?token=GbpkUh2d2PAz1ORp7wKcTKv_SwA7huK8b9V16UZEF2JpD7b210AzceL03YrshTjjGgjb39wYe2s3i9zdY-6O_SDb3wltQTwlBaqd-9BWC-jFFRw39n2Rq7tPz5y9dRq9-alCh502m585tFOUEz14PIC8qk3kRK_WbTSP0ceFUka2hzf-8yeuHh8khyAQK3_kxPuFxuWQFj9Py6O3V6RbQpZi6BGVIJowa_mwWgev9unNY_r7b2sC_xzVR3tmuMoVerLURKGeRg_YXDe0Fv50pXgW5VXnC6RCMvvR2D0NPiBxgKU7ny8V-B2dMJbrEoV1L3xEj7gsCQoNUjFV4rn4jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2ac75c7af.mp4?token=GbpkUh2d2PAz1ORp7wKcTKv_SwA7huK8b9V16UZEF2JpD7b210AzceL03YrshTjjGgjb39wYe2s3i9zdY-6O_SDb3wltQTwlBaqd-9BWC-jFFRw39n2Rq7tPz5y9dRq9-alCh502m585tFOUEz14PIC8qk3kRK_WbTSP0ceFUka2hzf-8yeuHh8khyAQK3_kxPuFxuWQFj9Py6O3V6RbQpZi6BGVIJowa_mwWgev9unNY_r7b2sC_xzVR3tmuMoVerLURKGeRg_YXDe0Fv50pXgW5VXnC6RCMvvR2D0NPiBxgKU7ny8V-B2dMJbrEoV1L3xEj7gsCQoNUjFV4rn4jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نایا: تصاویری از حمله امریکا از خاک کویت به ایران، با موشک‌های هیمارس در زمان جنگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/131630" target="_blank">📅 18:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131629">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: ارتش باید در هر زمانی که لازم باشد، آماده انجام یک عملیات مستقل و اسرائیلی در ایران باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/131629" target="_blank">📅 18:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131628">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
الجزیره: ۵۰۰ میلیون دلار برای ترامپ، دسترسی برای پاکستان؛ چگونه شرط‌بندیِ کریپتویی - دیپلماتیک اسلام‌آباد جواب داد؟
🔴
وقتی این هفته جزئیات درآمدهای مالی دونالد ترامپ، رئیس‌جمهور آمریکا، در سال ۲۰۲۵ منتشر شد، یک رقم بیش از همه جلب توجه کرد: شرکت رمزارزی خانوادگی او، ورلد لیبرتی فایننشال (WLF)، فقط از محل فروش توکن‌ها در سال گذشته بیش از ۵۰۰ میلیون دلار برای او درآمد ایجاد کرده بود؛ بخشی از یک سود بادآوردۀ بسیار بزرگ‌تر از حوزهٔ رمزارز که در مجموع صدها میلیون دلار دیگر هم ارزش داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/131628" target="_blank">📅 17:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131627">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91f227c1ee.mp4?token=R7-s5HHFPDERxRrkhAaMi8k02Qw5atf4IuQRtWvCU155au2V3fpr1a8cAj8xv-0JAjp49Dp_HEuhDxJVES7j-prhPrm4gq5TjoqVT-MwvTnqxwcYZgEVSoqRk9SVaTY3KjGlvxsIFoXm5Age8OmPftsGYcwMh_CmoUBmIaBJyVVVROvtbh1mZpBfIOzbzypLQ6ogOsPebkP67b8AqnymE9sUJ6VYCWvlpGrNlNf2oGAUTEiTfckykOdaCMrcKxFtwpynzRNT1A-633_KqEFYZUPXxmNaijOik48YHfP2QP6-yy5ylJ2l7CpNSKEPF3cGEFYjxYuMKTFlpl0twbC0fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91f227c1ee.mp4?token=R7-s5HHFPDERxRrkhAaMi8k02Qw5atf4IuQRtWvCU155au2V3fpr1a8cAj8xv-0JAjp49Dp_HEuhDxJVES7j-prhPrm4gq5TjoqVT-MwvTnqxwcYZgEVSoqRk9SVaTY3KjGlvxsIFoXm5Age8OmPftsGYcwMh_CmoUBmIaBJyVVVROvtbh1mZpBfIOzbzypLQ6ogOsPebkP67b8AqnymE9sUJ6VYCWvlpGrNlNf2oGAUTEiTfckykOdaCMrcKxFtwpynzRNT1A-633_KqEFYZUPXxmNaijOik48YHfP2QP6-yy5ylJ2l7CpNSKEPF3cGEFYjxYuMKTFlpl0twbC0fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر وداع عاصم منیر و شهباز شریف
✅
@AloNews</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/131627" target="_blank">📅 17:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131626">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEaKfiCiaPq8bCt8nc1boc6pdP-sJ6k6Hey25l5N7rlXjT0U8CWNZwjKt-qyCXK8mDAyLuP1G3cEyqBBb-4S15A_Yn4HHNcSqPhNWUqoeXEJ7PhdLJvYH5q9ec1xbWzp37bWEKW-PVgtiBFbGZZDVMsNq5qfB20c80hLhFVsttAXX4tZ5F2aU6vY7Pi40AkqnB7hfAtHXoVczT635asij8U9802nD5KvVmOls_kaStONiOQGXIZBkC49_B12kDfVSTkS-6Bf_g7MZ5rKT_0DNFP79hLAWQhl6IKV29H1Z4zl8P76JCSEDObl6KM9-4250ytfmEWZ4FBbkO8FMaZeZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز
:
به سه منبع ایرانی و غربی استناد می‌کند، ایران مذاکراتی را برای فروش نفت به شرکت‌های ژاپنی آغاز کرده است، اما خریداران احتمالی به دنبال دریافت معافیت طولانی‌تری از تحریم‌های ایالات متحده و اطمینان از ایمنی تردد کشتی‌ها در خلیج فارس هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/131626" target="_blank">📅 17:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131625">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f37b08bded.mp4?token=XoOvTFn7f5CZmoQrF_NUmLFL5e8Qo9zxpf1VvTiMvQENKUY2IZy9eW6FNCHH8SOgX2d8VJsBzryhVSY9yH6X2R9KGpadAOnnkkkqETd0TircGKBXlCWeu35g9qhi4vHEskRJcFnFnt1Mo9WRARtjPk4womBw_XKvwEgKLGYh31I0cJJNR4Veow9AoFJ6k_xoPCfX2ITvU6lbSLNKcdlqRaq6kM0XztLJCLRofKx0z-Cg1AnBBinKcz5YHm-NYqecdKbpv_fdop_MyXt17TzTjqWW-ZD5VZHrbGaPRbH-xzGfd2bbZtd1OlF6MB8Sz9bEG2NXUFMoZBhrLqxkhgqwHg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f37b08bded.mp4?token=XoOvTFn7f5CZmoQrF_NUmLFL5e8Qo9zxpf1VvTiMvQENKUY2IZy9eW6FNCHH8SOgX2d8VJsBzryhVSY9yH6X2R9KGpadAOnnkkkqETd0TircGKBXlCWeu35g9qhi4vHEskRJcFnFnt1Mo9WRARtjPk4womBw_XKvwEgKLGYh31I0cJJNR4Veow9AoFJ6k_xoPCfX2ITvU6lbSLNKcdlqRaq6kM0XztLJCLRofKx0z-Cg1AnBBinKcz5YHm-NYqecdKbpv_fdop_MyXt17TzTjqWW-ZD5VZHrbGaPRbH-xzGfd2bbZtd1OlF6MB8Sz9bEG2NXUFMoZBhrLqxkhgqwHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ادای احترام دیمیتری مدودف، معاون رئیس شورای امنیت روسیه و فرستاده ویژه پوتین
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/131625" target="_blank">📅 17:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131624">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/63e838adce.mp4?token=t3QSfAq0vtEGTooqVsTQ9qt2yaGv6H_6QnJ25-EhwL0-iCs5q38vjs44lqhuIV9Rx0_xdbna4qAbaQhFhm6rhtosGhu9ANqpBTSTdNWRqcQLoNL42WFxOPXHgtNad_aM3Hc3pMhv1Qu1LjMMs0yDvqgm15cbRXFIrRSUjD3T7d18VdXmZYMV_tkS_jmC3GQP0m_X2Gl1et_Knfed6GDCMh7xPc5UMA5Q5QpizFaN8uOcXJXOoQwPh0Fx9aHSbJNxDzQL6_Zz1rqiUghoI0f0O_9XRSx-qJjcsfyTAk5xvSBDyGuERxmDXPfev0vwsV8JM__yUrQwwnWcWayxQszTyg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/63e838adce.mp4?token=t3QSfAq0vtEGTooqVsTQ9qt2yaGv6H_6QnJ25-EhwL0-iCs5q38vjs44lqhuIV9Rx0_xdbna4qAbaQhFhm6rhtosGhu9ANqpBTSTdNWRqcQLoNL42WFxOPXHgtNad_aM3Hc3pMhv1Qu1LjMMs0yDvqgm15cbRXFIrRSUjD3T7d18VdXmZYMV_tkS_jmC3GQP0m_X2Gl1et_Knfed6GDCMh7xPc5UMA5Q5QpizFaN8uOcXJXOoQwPh0Fx9aHSbJNxDzQL6_Zz1rqiUghoI0f0O_9XRSx-qJjcsfyTAk5xvSBDyGuERxmDXPfev0vwsV8JM__yUrQwwnWcWayxQszTyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ادای احترام وزیر آموزش عالی گوام
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/131624" target="_blank">📅 17:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131623">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
معاون اردوغان از سفر احتمالی رئیس جمهور ترکیه به ایران خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/131623" target="_blank">📅 17:06 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131622">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOqm82vCNVw-Kr6yWKGPNLQQKc2q0Yp9yDz9NEHy-nUUCvH649BS94UHBywNtq3cASXB52ZISd9yYUr3ZYdnBoplfi2E-cT7LkNUSv9Fqq7qlehiHYlE3u99wLG9qXQs7sIK0IuvVXZQIDEAcEqcJ1IjsjMXFarSmSUJpz8KScV22jaNMjxPvEI89I3_sW7wUoDFzoA7bbFpaWoESl5oGPzNKVKMHlMGdJCf5k2-FoO8MXFxt-AUOMNf129BHK3rNyMwSSyknsM80FNoGZ7n9wMq-q2pSMGWVocrP_2L2xAZ7rY-tHxGJH5HVj4URZoxWYp3lS20tkHpbXw_W_jEOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صبح امروز یک پرواز ماهان‌ایر جهت انتقال مقامات انصار الله به ایران وارد صنعا شده و پس از مدتی به سمت تهران بازگشت
🔴
این اولین پرواز مستقیم ایران-صنعا در حدود ۱۰ سال گذشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/131622" target="_blank">📅 16:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131621">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
رایزنی احتمالی OpenAI برای واگذاری ۵ درصد سهام به دولت آمریکا
🔴
به گزارش تایم، شرکت OpenAI، سازنده ChatGPT، reportedly در حال بررسی واگذاری ۵ درصد از سهام خود به دولت ایالات متحده است؛ موضوعی که می‌تواند ابعاد تازه‌ای به رابطه دولت آمریکا و صنعت هوش مصنوعی بدهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/131621" target="_blank">📅 16:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131619">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
رویترز: ایران گفتگوهایی را برای فروش نفت به شرکت‌های ژاپنی آغاز کرده است!
🔴
خریداران احتمالی خواهان تمدید طولانی‌تر معافیت از تحریم‌های نفتی آمریکا و همچنین دریافت اطمینان درباره امن‌ بودن شرایط کشتیرانی در خلیج فارس هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/131619" target="_blank">📅 16:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131618">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af94fcd247.mp4?token=LGBZtpuxdKEUPI8xP6q_FpEn6qC7-fyRPDkAccBH3yj5re57lgKzQGqypFNbGKDAH5QG8QFo7l1JZ_pKqH0apJsAc8v10LDGKXHM_4kowlcRDqE-lxvi5vkc3q-LHI29bQeQEF_wNoVq9gDiO0sOou2gpgR679DWeKcLrtVvLtRkYqtXrdgjfK_r9yjSnycVLzN2NG7_094O9tgK1UWVehw287Tmn8L-FkzvEE1PfigtQMIU0GZ9_OJFN9HUMVQ1OblIyrKibD8qDYvzt_TCWOoh09jjB79ocAd7Q2lEz0YYWC7YVkm8evQ56Zyi1UKsgKV3WraxWbRG48RoqqMi7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af94fcd247.mp4?token=LGBZtpuxdKEUPI8xP6q_FpEn6qC7-fyRPDkAccBH3yj5re57lgKzQGqypFNbGKDAH5QG8QFo7l1JZ_pKqH0apJsAc8v10LDGKXHM_4kowlcRDqE-lxvi5vkc3q-LHI29bQeQEF_wNoVq9gDiO0sOou2gpgR679DWeKcLrtVvLtRkYqtXrdgjfK_r9yjSnycVLzN2NG7_094O9tgK1UWVehw287Tmn8L-FkzvEE1PfigtQMIU0GZ9_OJFN9HUMVQ1OblIyrKibD8qDYvzt_TCWOoh09jjB79ocAd7Q2lEz0YYWC7YVkm8evQ56Zyi1UKsgKV3WraxWbRG48RoqqMi7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ادای احترام وزیر کابینۀ نامبیا
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/131618" target="_blank">📅 16:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131617">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1def7056a.mp4?token=oVyFOHeoQRQ3BpUhpSZxZGhwQ5GipLVw-fEJlT_GiAlQk3_sHc7XlF_Jaqzru2J9-Wx9tIn6VOWTKyNUmPtFQMlBuyavVIUEupgGiGDtarDPdgDrHnNv0zhQ1dggwgs9ayOCxm4LqqWCGKcbP75Rf0H9iE8s9AxPbiOhArvOGWnqFy1SxqiRb0fMxZXCJ9XvOSvdIsctM5DkdyQPjFkn12QBFQPTtp0AuxTkLl7tUkXKawE2YSNPuNk-nVBoOVNPfUUKDKqirl2S0tGJexGdpm38RwfKVaqTzTnZ_zcuXZKY9Ono-k3cKjy6offDpuu1klHBsE5z_cjxnYJ60A9xbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1def7056a.mp4?token=oVyFOHeoQRQ3BpUhpSZxZGhwQ5GipLVw-fEJlT_GiAlQk3_sHc7XlF_Jaqzru2J9-Wx9tIn6VOWTKyNUmPtFQMlBuyavVIUEupgGiGDtarDPdgDrHnNv0zhQ1dggwgs9ayOCxm4LqqWCGKcbP75Rf0H9iE8s9AxPbiOhArvOGWnqFy1SxqiRb0fMxZXCJ9XvOSvdIsctM5DkdyQPjFkn12QBFQPTtp0AuxTkLl7tUkXKawE2YSNPuNk-nVBoOVNPfUUKDKqirl2S0tGJexGdpm38RwfKVaqTzTnZ_zcuXZKY9Ono-k3cKjy6offDpuu1klHBsE5z_cjxnYJ60A9xbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیمیتری مدودف، فرستاده ویژه ولادیمیر پوتین وارد تهران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/131617" target="_blank">📅 16:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131616">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQkcp_DPH21YFbZ_vt3o4hueC59Ok-ofvRmmjMXWQMuVsv-7BLVsyrDFPbNCE_sl8j4P7P4EvU46-BgfqhZ2jFwJpW2QXirQPkjK70PUGSWGFOVbf8NrvG8jfw1PmLrUUpiJ8vnOowYTYtaP4kIoW2vyMKMNY-A11WESc8NJlQnI1LS_hcGpktdui9rxDPHGN2L_m2jllXaP6B7gyZVhVq289mK9d4-9NqH3wULXfCcwD_FXWVc1jBysRU6ZSmF4sP9jK4oVaRm_18tD8BuXucIn3azSlNpk5rqznmGrSq-nLrMNU-WLVR-NwvOBMxHyn6-GddPv1Z2iFREzNW1LdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ، درباره ناتو : برای آمریکا واقعاً مسخره‌ست که همین‌جوری توی یه رابطه یه‌طرفه بمونه
وقتی طرف مقابل هیچ متقابلی انجام نمی‌ده، اونا هیچ‌وقت موقع نیاز کنار ما نبودن!!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/131616" target="_blank">📅 16:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131615">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
از ساعاتی قبل تصاویری بسیار منشوری از آرام جوینده همسر سپهر حیدری، اسطوره پرسپولیس درحال پخش شدن است
◀️
مشاهده فوری و بدون سانسور</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/131615" target="_blank">📅 16:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131614">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
ارتش اسرائیل:
روز گذشته به زیرساخت‌های حزب‌الله در جنوب لبنان حمله کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/131614" target="_blank">📅 15:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131613">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJ9wSB00pXie3ps7IQ1Q4D5CFY-0Xi33HDvDiCaKcuZFtekhEgrPRtmzKnpH62fJ7MmE8hpawWHMbr45Gn0m3mY2z2QOBaz3cJ-nzQdc5pGf9Umg_X-K5KPYsAJUa4dUGQu5DTe-CTbs-8EOLzD1QDUjVmF2DVoXI-8eafg1KRZKvDe6ai6kQtCyh_9-3sz_NNN7G9XPe4vohkse3W9qkhS_0NspkOzs0Yt215rq1v6JGYuaLWaXRcl7ZpBDPtpVZtA-1NAN1E4zLHoLqsoQxi_x1-YZm3iTTxMquWSqCo6PjS3tH86Kp8swpWHA07UCwg62rgbKu9Hk7A0npd5pYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎤
میثاقی به اسنایدر:
ما بدون باخت و با سه مساوی از ادامه باز موندیم
🎙
اسنایدر: وقتی صعود نکنی سه تساوی با سه باخت فرقی نمیکنه
@AloSport</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/131613" target="_blank">📅 15:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131612">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dU7f_mlCK2AxZFBe805uRAM1oXFT1pw1mU8MUrIVNJETS8W0BXdWF_QbQPLUZzTMMdWgiRksOoh9OSTtHj1QI-FbEtrr00fi1fNeZvE_bPYBYN1-U5q9THImMIOmNYo8dNzZbqOhI59CfGSv7eJNkm2UH33XO0bMYxXGMAPS5_-aQhK8Yi4tinV63jU7qb3pEbhjt0cZrwx1ygUBsNRw7UGdwPP3cUwakAeiGlBv4MD7SaT7cJEWGeabm2ML7zVlJtYCpKETRFQMFqZyUYEfstj3S5VXzh7DhybdoeNRwNkkoki-B8YE3n1MNc3CFJiwAbOR1T3nEj1yI0l2OaVXUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کلش ریپورت: پنج فروند هواپیمای بوئینگ 777 که قبلاً متعلق به شرکت هواپیمایی سعودی بودند، علی‌رغم تحریم‌ها، به شرکت ماهان ایر ایران تحویل داده شدند.
🔴
دو فروند از این هواپیماها در فرودگاه مهرآباد تهران دیده شده اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/131612" target="_blank">📅 15:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131611">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkIGbqb8VmFualq_VejhPGOuaBcLbBlOgyxbuIzRuI6_905hfiu6Kvn0pLdhA57jXnSvdTQ02vt3_x5__zHEX_HSXt3vJKk6lBzhF3VerEqiiNLETAS8D2cd8GBpzKVDqf4kNZP31iHlE5Bz96pqnp8nQTs1OtLC0pdm3euGeZrZX0HuZ9_oQXSNbMdFbRIq48HqJIXP_561oAgf3cLxMFu8j6-4ugx7zgh9FmPhX6z5F8SwynWecaadMN7z3qbJHrIcRz6i4kyibgrj77QaKwtceOoCoSHG-82E2OQrVKcYygx2H5DP5eWKnbENg75NzhTj9SvFTtLzybwHdrDn0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش آشنا به نبویان: راست می‌گویی در حدی نیستی که از بالا تذکر بگیری
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/131611" target="_blank">📅 15:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131610">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e4987a0d8.mp4?token=o25DohLWmxfmjYprIWxDDUwhNLy8_u3zH25BX4RUUKnykuNAoKXjMnU7lnr4euCPDKJy_l_z2t2DznvSQGQvcyi5lBs86Bt6Hl0bgd2vi-0Mnbv4Vz96Wta-yE9GwTOim2XNpvEDALxu1QUaxnIQ0M4bOw9uqOSOFs5jactMoUJxT347gc-Hqo6RfuD4btD-rOeChPF2RR5wAgsX4fx2NII8ApcDp9zKoKGNDlDK64rWK3kkKXAAvN9Hu3PcKXiDzkymgm9qq2w-G95cu2Zmt2RyI7PIbN5BH25mKaPNwO1h9SR4IBDqPgT3PSoEPtAv9Bgwc66zbKSpq-lBCbIgXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e4987a0d8.mp4?token=o25DohLWmxfmjYprIWxDDUwhNLy8_u3zH25BX4RUUKnykuNAoKXjMnU7lnr4euCPDKJy_l_z2t2DznvSQGQvcyi5lBs86Bt6Hl0bgd2vi-0Mnbv4Vz96Wta-yE9GwTOim2XNpvEDALxu1QUaxnIQ0M4bOw9uqOSOFs5jactMoUJxT347gc-Hqo6RfuD4btD-rOeChPF2RR5wAgsX4fx2NII8ApcDp9zKoKGNDlDK64rWK3kkKXAAvN9Hu3PcKXiDzkymgm9qq2w-G95cu2Zmt2RyI7PIbN5BH25mKaPNwO1h9SR4IBDqPgT3PSoEPtAv9Bgwc66zbKSpq-lBCbIgXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عده ای از مردم هند در راه ایران برای شرکت در مراسم خاکسپاری سید علی خامنه ای
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/131610" target="_blank">📅 14:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131609">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GkrzpiMRNlzSXuZtHKYJr2aBydQOpGrIU1YRIjIGTkkFDJpXZ0ub-egAOM9Zk5o5VL6MJu7Q6pBS3X9cqLSNCj4aPBlZUHIxd5uQSViXoFltpgcFDbKDGf9u3uLsGImWUaje1Mo7rHWybZDb5AVHr2G9ZDHNYeP84mOaxP1jbO8m7mA8p9s_YMdfcjiA_jLzb0Q8BYj6YxXx6kV3Gs1t8nN9TwIo1nTUjps0-bXJNu40yY3GUUgAc_j--q_guIKvksQsEX_trHkY4BVnLSE2pWevTVlMghsDqCXR8pXYoHX7j_63kUKIIoZEsAJOHtI1CR1QlgjbCltZhm5Cmc6Fww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چهره خوشحال پزشکیان در استقبال از مقامات کشورها با انتقاد حامیان حکومت روبرو شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/131609" target="_blank">📅 14:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131608">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
احتمال گسترش بیماری‌های عفونی و آلودگی آب‌های زیرسطحی با برپایی تعداد زیادی توالت در سراسر تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/131608" target="_blank">📅 14:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131607">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
سرپرست وزارت دفاع: اگر حین مذاکره تخلفی و نقضی را از آمریکایی‌ها و افراد مذاکره کننده در طرف مقابل‌مان ببینیم، در میدان به آنها پاسخ خواهیم داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/131607" target="_blank">📅 14:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131606">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
واشنگتن پست: اختلاف اسرائیل و آمریکا با ترور لاریجانی آغاز شد
🔴
واشنگتن پست مدعی شد: مقام‌های آمریکایی اخیرا فاش کرده‌اند، واشنگتن طرح‌های از پیش‌تدوین‌شده اسرائیل برای ترور عباس عراقچی، وزیر خارجه ایران، و محمدباقر قالیباف، رئیس مجلس، را خنثی کرده است.
🔴
این اطلاعات همچنین اختلافات و شکاف آشکار واشنگتن و تل‌آویو درباره اهداف جنگ علیه ایران را برجسته ساخته و نشان داد که اسرائیل به دنبال سرنگونی نظام ایران و براندازی آن بوده است.
🔴
طبق گفته مقام‌های آمریکایی مطلع به روزنامه «واشنگتن پست» دولت آمریکا خیلی زود به این جمع‌بندی رسید که این هدف از طریق جنگ، قابل تحقق نیست و بنابراین تمرکز خود را بر هدف قرار دادن توانمندی‌های نظامی ایران و ناوگان دریایی این کشور گذاشت.
🔴
نقطه عطف، ترور لاریجانی بود؛ در حالی که واشنگتن به دنبال فردی در ایران بود که بتوان با او وارد تعامل شد و ناگهان چنین فردی دیگر وجود نداشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/131606" target="_blank">📅 14:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131605">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
فوری / آغاز درگیری ها در یمن!
🔴
گزارش ها از پرواز جت های جنگی عربستان بر فراز آسمان صنعا، پایتخت حوثی ها و بمباران مواضع حوثی ها در نقاطی از یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/131605" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131604">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
تحلیلگر عرب در حوزه ایران و پژوهشگر ارشد مرکز مطالعات الجزیره: آماده‌سازی‌ها برای آغاز نشست‌های سطح بالا میان ایران و تعدادی از کشور‌های شورای همکاری خلیج فارس و عراق
🔴
این نشست‌ها طی چند هفته آینده آغاز خواهد شد
🔴
هدف از این نشست‌ها ایجاد سازوکار‌های امنیتی و نظامی است که منافع مشترک را تضمین کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/131604" target="_blank">📅 14:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131603">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
خروج بیشتر نیروهای آمریکا از عملیات ضد داعش در نیجریه
🔴
به گزارش جروزالم‌پست، فرمانده فرماندهی آمریکا در آفریقا اعلام کرد که واشنگتن بیشتر نیروهای مستقرشده برای عملیات اخیر علیه داعش در نیجریه را خارج کرده و اکنون به درخواست ابوجا، پشتیبانی اطلاعاتی ارائه می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/131603" target="_blank">📅 14:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131601">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q5ZP2sY9dtqFGSZ8BFyViwEF5v4EcpNnOK1gpVPcJRsPbeIxJA8f3_GWrtC3YWq4PRoDooGDcBZXE532aNNq746IcU6dOs0uN3tgdV9eNL9zfdViDQMBsqOWBZwxp1Aw7SoOTq23fc4DlgMHcWr6XITM9THeCJdxQ1AA3IjzS5pxLka5DI65f9uPOvqm0xV26mcjMWLgV6USvvOcfjpmR_J7NYMzZC_bw7_mTJJMDF2ucDffEme11Ln2kqNdVVr7Oz-dAyqcf6GHtUku-Yt2-ZuYNNkj-HP_sTmklOOJFLlBFbviyvvqDzGlH3kuMtHNdiBc7yEQRalzI8I-nU5Veg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/otzNbRj8A2-_u15q2ReDPApYeuA8LAeolaNpZ8BZ2G-NYOoc1qIS93IIqk2NGXU2loAs92ITSh4zIz-YjnxvBHe6OOdMWI-QNQMU-Q5FEKpzNZd_fg-DWkCVE3zz9K4W9Am5qIGMPLx6Wp8AAycvZB7Q3Be-62hdxROfRBkGO2mdDKboRwdsg92A2oYil-HnUtlwp33npzh65-6TpQgkFIPoStdVIZcRTjYjp-3lVcleuKfgdzqnpivhVTV-VQxwG5LiJskqd2pvezFrX4WfSZJ0oAN1zosUlflADg53OyRE6Z3EhZM2a0IefISMEWb2jnrGH5KcoPjca2czg4dxlg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مجله اکونومیست حدود یک سال قبل یک تصویر داد بیرون که اتفاقات آینده رو پیش بینی کرده و دونه دونه داره پیش میاد
نکته اینه مجسمه دست خامنه‌ای هم تو مجله اومده بود
😐
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/131601" target="_blank">📅 14:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131599">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
صدا و سیما: تا کنون نمایندگانی از بیش از 100 کشور وارد تهران شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/131599" target="_blank">📅 14:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131598">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
صدا و سیما: تا کنون نمایندگانی از بیش از 100 کشور وارد تهران شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/131598" target="_blank">📅 14:08 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
