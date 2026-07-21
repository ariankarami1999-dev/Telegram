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
<img src="https://cdn4.telesco.pe/file/bh0qRwdD_nDH1McgSSbJvSm1KnDqrQcMRCmZ2LYLddco1f7Z2UbAX1wquEQqM0njX8R9thd37dvk_iN3LDgVNPgvIvYpKJ_O0XWSTlO2urt0gfIrpZJCO45CqWjzOOFC2BLcTPbe8Syk2PrhfNVeNpodhGtHDCSXiuGIyRK16m5bXa86e4RKYS08XcJTTKHQLjNz-5dwOt7PgI5Ig4VU96x5ImJurqjbVxW1EohErGwu8SmcQ281usxjU5-Cu784R23c6oxlGCl32TELXxfgyy23QjNuH7Ujp4CeisXcKtNSPKRcmlYwB4Wsb8Z0QgGvI9lHQhG0O1XpjsP-UzdVcQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 21:20:10</div>
<hr>

<div class="tg-post" id="msg-136434">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
#فوری | ترامپ:
🔻
ایرانی ها هنوز چیز زیادی از ما ندیده اند، ما تا کنون بسیار مودب بوده ایم.
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 727 · <a href="https://t.me/SorkhTimes/136434" target="_blank">📅 21:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136433">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
✅
حسین قدوسی: پرسپولیس درتلاش برای کاهش مبلغ رضایتنامه‌ی محمد مهدی محبی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/136433" target="_blank">📅 21:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136432">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
شنیده ها:توافقات با محبی صورت گرفته.. واریز رضایت نامه به باشگاه اماراتی انجام بشه رونمایی میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/SorkhTimes/136432" target="_blank">📅 20:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136431">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
#فوری | ترامپ:
❗️
بدون شک ما کوه کلنگ ایران را بمباران خواهیم کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SorkhTimes/136431" target="_blank">📅 20:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136430">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❗️
❗️
فوری/جرزوالم پست: ترامپ پیشنهاد قطر و پاکستان برای آتش بس ده روز با ایران را رد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/SorkhTimes/136430" target="_blank">📅 20:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136429">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">💥
امیررضا رفیعی با استناد به بند‌‌ در قراردادش عدم بازی در 10 درصد بازی ها عصر امروز به صورت یکطرفه قراردادش را فسخ کرد و بدون توافق با باشگاه در تمرین دیروز باشگاه هم حاضر نشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/SorkhTimes/136429" target="_blank">📅 20:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136428">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❗️
پرسپولیس با گل های تیکدری و سرگیف ۲-۰ جلوعه  پ.ن تیکدری فعلا تو هر دو بازی تارتار گل زده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/SorkhTimes/136428" target="_blank">📅 20:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136427">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ml6ntEkT5N6wmbVUpfZkb7XCgRqoJHPcrrgQUqYjq581ktizuOh8pyCj_Lc65IIS1Q-4FBbVwXSYsm8kIflJf8b4v2geBqMP374VIpH7cG8yGwV6lSTZ0voNAa5KKXlDHJwrXptng71Nify5-YYPra8e3glkpvdMisHZGlku0LIbfhXDnXQgRcOCBRoJFnxrRyOzt-RUyZo96QJVYHx8LTdo64K0RhPYuuB8zkngF_hKSRmd8JKpYEpRxIcbwVTDnMjd4-jJQaiI9UImCMzpwzrs5PrnIrzb159cK5Ky06i15To98IE8v82EASXaBoUDpaPLYhibWP8-N7xjn8aChg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شنیده ها؛ مهدی تارتار لیست بازیکنانی را به باشگاه داده و به آنها اعلام کرده مشکلی با معاوضه نفرات با بازیکنان مدنظر وجود ندارد
🔴
امیررضا رفیعی
🔴
حسین ابرقویی نژاد
🔴
مرتضی پورعلی گنجی
🔴
دنیل گرا
🔴
تیوی بیفوما
🔴
یاسین سلمانی
🔴
محمد امین کاظمیان
🔴
علیرضا عنایت زاده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SorkhTimes/136427" target="_blank">📅 20:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136426">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❗️
پرسپولیس با گل های تیکدری و سرگیف ۲-۰ جلوعه  پ.ن تیکدری فعلا تو هر دو بازی تارتار گل زده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SorkhTimes/136426" target="_blank">📅 20:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136425">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
فووووووووووووری از تسنیم
🚨
تراکتور در آستانه نهایی کردن قرارداد محمد قربانی قرار دارد و نماینده باشگاه تراکتور هم اکنون برای انجام این توافق در دبی حضور دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/136425" target="_blank">📅 18:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136424">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✅
✅
یه جریانی تو باشگاه هست که می‌خواد پورعلی‌گنجی بمونه و بدش نمیاد با رفتن ابرقویی، جا برای موندن این مدافع باز بشه.
🔴
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/136424" target="_blank">📅 18:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136423">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❗️
فوووووووووری از حسین قهار
🔴
حسین قهار: هدف از مازاد کردن ابرقویی ؛ بازگشت مرتضی پورعلی گنجی به پرسپولیس است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/136423" target="_blank">📅 18:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136422">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✅
پرسپولیس از دقایقی پیش تو یه بازی تدارکاتی به مصاف خیبر رفت
🔴
ترکیب پرسپولیس تو بازی:
🔴
پیام نیازمند،
🔴
عیدی،ابرقویی،کنعانی‌، جلالی
❌
خدابنده‌لو، باکیچ،
🔴
تیکدری، محمودی،  عمری،
🔴
ایگور سرگیف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/136422" target="_blank">📅 18:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136421">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
❌
باشگاه پرسپولیس برنامه دارد کسری طاهری را به صورت قرضی جذب کند و در نیم‌فصل با پرداخت رضایت‌نامه او را از نساجی دائمی جذب کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/136421" target="_blank">📅 17:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136420">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
فووووووری: دانیال ایری به پرسپولیس پیوست /فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/136420" target="_blank">📅 17:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136419">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✅
تارتار برای اینکه پرسپولیس از فرم مسابقه دور نشه، خواسته تیم هر هفته یک بازی تدارکاتی داشته باشه. بازی با خیبر خرم‌آباد اولین بازی این برنامه‌ست و باشگاه هم دنبال حریف‌های بعدی برای هفته‌های آینده‌ست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/136419" target="_blank">📅 17:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136418">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
دانیال ایری به پرسپولیس پیوست/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/136418" target="_blank">📅 17:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136417">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
پروژه جوونگرایی نساجی قدرتمند تر از همه تیم ها در حال اجرا؛ مجتبی حسینی سرمربی نساجی مازندران شد/ فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/136417" target="_blank">📅 16:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136416">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✅
✅
سیتنا : علت فیلترینگ سایت فوتبال ۳۶۰ چیست؟ پس از مجموعه‌ای از شکایت‌های صداوسیما علیه این رسانه و در پی افزایش فشارها پس از برخی برنامه‌ها و گفت‌وگوهای اخیر فردوسی‌پور، از جمله مصاحبه زنده با علیرضا فغانی، این تصمیم گرفته شده است
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/136416" target="_blank">📅 16:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136415">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
شنیده ها:پرسپولیس امروز 40 میلیارد تومن + رضایت نامه قطعی کاظمیان رو به فولاد برای جذب ابوالفضل رزاق پور پیشنهاد داده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/136415" target="_blank">📅 16:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136414">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❗️
❗️
به این ترتیب تارتار هر سه گزینه اصلی خود برای پست دفاع راست، یعنی رامین رضاییان، دانیال اسماعیلی‌فر و آریا یوسفی را از دست داد/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/136414" target="_blank">📅 15:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136413">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQSq1FwzkVjflV5XcYoIo671wYJ9t02SnF6S3hxL35bt2IlmBVihMwEU-f1FR7v4_n1d3O6Ztfq8TdLsq2Xt2XKJGHkKgVXyx__FMxIKqrGFSF-w22UIuO96-LSPoqDppyFqHyLiDj5LZVQRxTv1GfNe2h21eAliedcISy7GoSUTmyTYSgtYfefAR8AWMCHKESZyBYMj7iS4fO0tCHYikp2UQ7pV8b-bxAWLVlS5YDZHyxBUjJGzu3XEcAqSKoqARkax-JR2RalMV5VUQ01XfgKdFpO-9P9BmfZRTEFTZRQI4pzLV_4H_PK0mBEZijKZCAkuzCOLwNAsW-_BHw1Lyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علیرضا کوشکی پس از بازارگرمی و افزایش نرخ قرارداد با کیسه تمدید کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/136413" target="_blank">📅 15:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136412">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
محمد خلیفه عصر امروز با حضور در باشگاه استقلال قرارداد پنج ساله با این تیم امضا خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/136412" target="_blank">📅 15:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136411">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❗️
با پنجره بسته، دفاع چپ جوون هم گرفتن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/136411" target="_blank">📅 15:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136410">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✅
✅
جزئیات اولیه از پیشنهاد قطر برای برقراری آتش بس:
🔹
۱- پایان جنگ و برقراری آتش بس
🔹
۲- تنگه هرمز تحت کنترل ایران به مدت ۱۰ روز باز شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/136410" target="_blank">📅 15:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136409">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✅
✅
مهم ترین خرید های پرسپولیس دانیال ایری، محمد مهدی محبی و کسری طاهری خواهند بود/ خبرنگار فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/136409" target="_blank">📅 15:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136408">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">کانالی که همیشه در مسیر ورشکست کردن سایت های شرطبندی حرکت کرده!
😈
آمار ثابت 90 درصد برد
✅
فقط کافیه چند روز فرم هاش رو دنبال کنید...
JOIN JOIN JOIN
JOIN JOIN JOIN</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/136408" target="_blank">📅 15:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136407">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AlkMkNkbpPPmjPROcw0ZgKSXkM5dq2GjpxSYR_3U4hC3a04A9bMjwFdguUjZ1umBIUGnsD86P6HB8jn0LFILV3JIhQZHBhQYUw7N-DnaSH4PnIB3qIhkVAp68iohAZ64sYPgq1NHh8X4TIkvF9BtMNheOOMKhFmW5V6z6RvRwPUcDzESN6sN8KtrifyH5gHpYSH9nXuNzNP5Ri9vYOnYi10un8da9C3iCNvWcH1JroA5vnqG3rVvsLnUzOefrIXg3ZdmKM5B55AgqR1EHBx63CwpC6rbjH27L7FHhggCpzg9jGFhe0sW9FjExaW2nBO-CCkocx9djeSWNOSqDolvFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
➡️
JOIN
JOIN
JOIN
JOIN
➡️
JOIN
JOIN
JOIN
JOIN</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/136407" target="_blank">📅 15:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136406">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
💣
One Signature. One Earthquake
…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/136406" target="_blank">📅 14:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136405">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
سایت و اپلیکیشن فوتبال 360 ( برنامه عادل فردوسی پور ) چند دقیقه ای هستش که از دسترس خارج شده و خیلیا احتمال فیلتر شدنشو بخاطر حرفاش علیه قلعه نویی میدن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/136405" target="_blank">📅 14:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136404">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
🔴
شکاری با استقلال مذاکره کرده و با باز شدن پنجره احتمال جذبش بالاست و اگه الان باز نشه زمستون یاغی میشه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/136404" target="_blank">📅 14:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136403">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❗️
با پنجره بسته، دفاع چپ جوون هم گرفتن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/136403" target="_blank">📅 14:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136402">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✅
✅
طبق شنیده ها ما هم افتادیم دنبال اسمی عجیب به نام زکی پور ....
❌
گودرزی کجا و زکی پور کجا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/136402" target="_blank">📅 14:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136401">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">،
❗️
❗️
شنیده ها : دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها واریز کند.…</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/136401" target="_blank">📅 14:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136400">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyJe8ajo4Q_kjfEE0yeIrk2WBs16sjqZzHjeBIYUqxmhYm3BBAqk3nihENJeB0C8SgUhtB-UoGpzxyAwxh6x2cVqNdutxRynGcTfxFt8zJ6ncW4W5dqHuaVZc9JBMACyTziJEU8u25W9ArV5z8H6RWH4KJ2eQlMO7tfDiOJhgS69dISH0Q0DYn5xGffgFJdH21qQK7bEBVsoozD4AjzmA3zKBrXHeedKwjqZ4wdsBUODOESV9VzHmC6-i1f9hk2-qDPzihHPTl5tnztftrrNArSSyHKjHpvCqoMM_9Be8o22CeSjS4W_ahpgW_2MaCUYJNINLVZsRlyorKhC3qTB2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
با پنجره بسته، دفاع چپ جوون هم گرفتن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/136400" target="_blank">📅 12:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136399">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✅
بهرام گودرزی با قراردادی 5 ساله به استقلال پیوست!
🔴
پ.ن قابل توجه آقای حدادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/136399" target="_blank">📅 12:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136398">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
❌
❌
#فوووووری
✅
باشگاه پرسپولیس با بهرام گودرزی به توافق نهایی رسید در صورت عدم تمدید میلاد از این بازیکن رونمایی خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/136398" target="_blank">📅 11:58 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136397">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❗️
تیم ملی امید ایران در اردوی ترکیه مقابل تیم مانیسا این کشور دیدار کرد و 1 بر 0 برنده شد
🔴
تک گل ایران در این دیدار را فرزین معامله گری دفاع چپ پرسپولیس در دقیقه 17 به ثمر رساند، پاس گل را نیز پوریا شهرآبادی مهاجم سرخپوشان ارسال کرد
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/136397" target="_blank">📅 11:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136396">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
👎
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس برنامه ای برای جذب بازیکن خارجی وجود نداره،و حتی در صورت جدایی گرا و بیفوما!
💯
تارتار از شرایط باکیچ،اورونوف و سرگیف رضایت کامل دارد،و اگر گرا تخفیف نده احتمالا ماندنی بشه…</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/136396" target="_blank">📅 11:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136395">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
غیررسمی: محمدرضا اخباری با قراردادی 1+1 ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/136395" target="_blank">📅 10:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136394">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
شنیده ها:پرسپولیس امروز 40 میلیارد تومن + رضایت نامه قطعی کاظمیان رو به فولاد برای جذب ابوالفضل رزاق پور پیشنهاد داده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/136394" target="_blank">📅 10:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136393">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❗️
❗️
واکنش تند گداوند به صحبت‌های اسطوره علی دایی: تنها مربی که در آزادی به عربستان باخته، روی فراموشکاری ما حساب باز کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/136393" target="_blank">📅 10:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136392">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">⌛️
⌛️
فووووووووووووری
🚨
لیگ برتر به صورت رسمی از 23 مرداد آغاز خواهد شد.
🚨
همچنین جمعه 2 مرداد مراسم قرعه کشی لیگ برتر برگزار خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/136392" target="_blank">📅 10:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136391">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
بمب سرخپوشان/ پرسپولیس با محبی به توافق شخصی رسید
⌛️
⌛️
طبق شنیده ها مدیران باشگاه پرسپولیس امروز با مدیربرنامه‌های محمد محبی به توافق رسیدند
⚽
قرار است در خصوص دریافت‌ رضایت نامه‌ بازیکن مذاکرات فردا انجام شود
⚽
محبی مشتاق است در پرسپولیس بازی کند تا…</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/136391" target="_blank">📅 09:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136390">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
چرا هیچ خبری از این بنده خدا نمیاد؟
❗️
حتی باشگاه پوستر خداحافظیم نزد براش
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/136390" target="_blank">📅 09:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136388">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✅
✅
محسن خلیلی: مذاکرات‌مثبتی با محمدمهدی زارع و باشگاه روسی داشته‌ایم. فعلا قراردادی امضا نشده اما باتوجه به توافقاتی که صورت گرفته بزودی زارع به جمع ما میپیونده و قرارداد رسمی امضا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
…</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/136388" target="_blank">📅 09:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136387">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🎙
عادل فردوسی‌پور: افتخار می‌کنم دایی و باقری با یک تماس آمدند؛ یک ریال به هیچ میهمانی پول ندادیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/136387" target="_blank">📅 08:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136386">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVnfekoqyPMzc_n-YyUCZlSZwwuYw5WhBJAdWtF8Rz_XAOKEkugwiITBRcXNW0W9WZ13d8bFCroaT9n_QBCar8FzPVpr8suL8ggu_B0onjYUljGHm_zpKlL4useAph2gnqE_yIjbUHLE7Gub3YxkSNolFVSoaiMwS40aV_CIgpK03kSdZ8DEkhNluwbFLtvYhykQV4qtsPqHsHdKMmfGEn7DKZaZLM1twTEvTy9E7xfuqb3HFDKJhw7yALSEPQ7AsdcXchMp0U7dT9W8sXXHgekdV-3RBW6OWnurkqMiCsth6ONohs366JWYTUGLHSb4KEoE1lw1liO7rxCBHKZ29A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
فارس: محمدرضا اخباری به پرسپولیس پیوست و به زودی امضا می‌کنه و امروز و فردا رونمایی میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/136386" target="_blank">📅 08:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136385">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🎙
عادل فردوسی پور: همه امکانات در اختیار شماست یک رسانه را نمی‌توانید تحمل کنید؟
❗️
❗️
بعضی دشمنان پدر خودشان را درآوردند یک چیزی از من پیدا کنند، نگاه مردم را با هزار و چهارصد میلیارد هم عوض نمی‌کنم! من دیگه سنی ازم گذشته و همه چیز رو به دست آوردم تو زندگی…</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/136385" target="_blank">📅 08:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136384">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drQekdWkGekbYUrutYpV1ybFiQpCHBjscJqODo41A1oRQK0RGBlhpxQZHiu9x_0T3Y4y3_wp-PHS6Ubpn0BYp2kGYXI0kS9aIWEJhI-Sd3vemkeECVbUGqWxuGZgW3DBIGcQgdm4RpC0d0F4tCjobScHyUNq5dOnv0Gj0Gj9P7la56cL_tRTSh4QjzehUbtenWd-yKjyhErHZAxhd-sfu9bRx6uXv32wvG-h5QXNPqZTVvPT9ZQEa50ZFE2lddq4FlEKzqaiWUQyqS_67KUJZhEcnNnEYvwV_w6DoCo2ghxnStpyiDsTIarY7W15QxWeh0JNQ1Ab6XHBsMrd9ZgBUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
عادل فردوسی پور:
هر پلتفرمی برای حضور مهموناش چند میلیارد هزینه میکنه ولی من افتخار میکنم که سلاطین فوتبال ایران علی آقا دایی و کریم خان باقری فقط با یک تماس من به برنامم اومدند، به هیچ مهمانی حتی یک ریال ندادم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/136384" target="_blank">📅 08:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136383">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/636f7d426d.mp4?token=d3zpVwln_gfrY3Dq4W3rgv8s4AYcmL-TFLuhpyfrTgQMNtWJbL8KK05aH0lIZXd6shoj8G-wtc0vUm5zE_jqP-_U7-hLnWljpB97rRW6N7bZWYGhanWxDIhBRsq_NtxMmDSMtlbGCwlVY-rP81XCeShsyE7bIu5NHZe2e0BfjL_7l37gvZ7uAwnzckFIy0qTlYC-fLhjDtkWmDfD2xhnbmIrpPKgfZMF5qijEgXoE6s-ZKH85YV-A-uargQk7w6EU5GrYiCBl8J5fPgJf5QyfndkGchJOFV6_5dq6SqVq3bL_yRswTR8tj5D-urC19NmrVADUVTLgEb2EpXr38pwkx_6-WEwCsqptHRs6LZilb6Ui_9nNW2K6b8HnAjPPk9N0yvpwDnud4dsX3T8kUs451s4Io5-yz9oeZukRjNLIOauRDHyyc4GcWrhTewJ9XlvwN34Ofhuo4XClwQISMsN5VDG-Q1UYV4kz6XiarQaUxRtVL-CGuwPhX6sCzDLYkU2Y0sLUBAkuvq_jqqXWW0Cbt4WcRsGoqcgUM7yPJvh6WKyYluDzeLloanjMehbRswxrKVOTu8esL_cEtmM1j2zLApjITJZvnGQw9C0o750_Vhf0JhwKyuyt_973SJZsK4kDZJDw6pDaKozLN8ZxQfomoBwNxip3OlGSdO3fCzOogI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/636f7d426d.mp4?token=d3zpVwln_gfrY3Dq4W3rgv8s4AYcmL-TFLuhpyfrTgQMNtWJbL8KK05aH0lIZXd6shoj8G-wtc0vUm5zE_jqP-_U7-hLnWljpB97rRW6N7bZWYGhanWxDIhBRsq_NtxMmDSMtlbGCwlVY-rP81XCeShsyE7bIu5NHZe2e0BfjL_7l37gvZ7uAwnzckFIy0qTlYC-fLhjDtkWmDfD2xhnbmIrpPKgfZMF5qijEgXoE6s-ZKH85YV-A-uargQk7w6EU5GrYiCBl8J5fPgJf5QyfndkGchJOFV6_5dq6SqVq3bL_yRswTR8tj5D-urC19NmrVADUVTLgEb2EpXr38pwkx_6-WEwCsqptHRs6LZilb6Ui_9nNW2K6b8HnAjPPk9N0yvpwDnud4dsX3T8kUs451s4Io5-yz9oeZukRjNLIOauRDHyyc4GcWrhTewJ9XlvwN34Ofhuo4XClwQISMsN5VDG-Q1UYV4kz6XiarQaUxRtVL-CGuwPhX6sCzDLYkU2Y0sLUBAkuvq_jqqXWW0Cbt4WcRsGoqcgUM7yPJvh6WKyYluDzeLloanjMehbRswxrKVOTu8esL_cEtmM1j2zLApjITJZvnGQw9C0o750_Vhf0JhwKyuyt_973SJZsK4kDZJDw6pDaKozLN8ZxQfomoBwNxip3OlGSdO3fCzOogI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
عادل فردوسی پور: همه امکانات در اختیار شماست یک رسانه را نمی‌توانید تحمل کنید؟
❗️
❗️
بعضی دشمنان پدر خودشان را درآوردند یک چیزی از من پیدا کنند، نگاه مردم را با هزار و چهارصد میلیارد هم عوض نمی‌کنم! من دیگه سنی ازم گذشته و همه چیز رو به دست آوردم تو زندگی ولی نگران این 100 بچه نابغم که اینجا کار میکنند، واقعا چرا نمیذارید کار کنیم؟
🔴
🔴
برنامه 90 رو از من گرفتید خودم از صفر با بدبختی فوتبال 360 رو ساختم و اومدم بالا و اینم تحمل نمیکنید؟! اگر قرار باشه به حرف شما گوش بدم دیگر عادل فردوسی‌پور نیستم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/136383" target="_blank">📅 08:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136381">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✅
گریه های عادل بخاطر بستن ناعادلانه سایت و اپلیکیشن فوتبال ۳۶۰ تو لایو یوتیوب و اینستاش.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/136381" target="_blank">📅 07:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136380">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lb28pexTwRC5h5y2z3oYcV_1ZHqNgsE-TE6oFiSXyD66w6Ls0cf4VAK2hCBch_r4-6a5Ciq0rm1kJgQlpnyXrKGP3rejB3htBBVwtUjNdNppf8b-FqudBYqESbJU61z8MWuP_iyn2BmADuE4zlTlS4ZTzvofD7zdHTMPivoGO9xhtPphisQYXp6ACkF2swtAWpzlSoWb_1OY6N3z-VcebBKsyyKWbZ1cONsdyNS7G3-wjS1QEJ1H9V6SIcqpIWcpp5VwLVTTcd0UuHFFYRyxS4txiHIInqSxfwl99k2iD-6y9cFCMz-5YBDrZrDn1OXpKtySTQ8Pc8BrQwZol54rZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
گریه های عادل بخاطر بستن ناعادلانه سایت و اپلیکیشن فوتبال ۳۶۰ تو لایو یوتیوب و اینستاش.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/136380" target="_blank">📅 07:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136379">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
⏺
امیررضا رفیعی با حضور در سازمان لیگ قراردادش را با پرسپولیس به صورت یکطرفه فسخ کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/136379" target="_blank">📅 07:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136378">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✅
امیررضا رفیعی در تمرین امروز پرسپولیس حضور پیدا نکرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/136378" target="_blank">📅 07:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136377">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
پرسپولیس ممکنه زندگی نده، ولی
شادی میده
عشق میده
اینه داستان سرخ...
❤️
‌
سلام صبح بخیر پرسپولیسیها؛
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/136377" target="_blank">📅 07:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136376">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136376" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر دوشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
🔗
بدون نیاز ب فیلترشکن
🤩
آموزش کامل استفاده از اپ
🔜
💰
💰
💰
💰
💰
📱
Telegram Channel
👇
https://telegram.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/136376" target="_blank">📅 01:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136375">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AccqbkejODlZ1NxjSCqkhRqObQ2HQRCJKxmJpPYI5vF9qxQzvmue6rejQQTP-7kJ4-vnLe_g3nezv-9c9kKcu-MIOkQbf2sZx3aGZK2SwJQaqXynl5X5UppuUk79sc1iBniTbLd355P9LEW_pFrqL7KBNIsuFMHMu8xh0O41MJdQfHET2J4mO3R_NFPio8zRrBmHuiPan31vMMk2i27MRSsOzav01xb64YLCTD07ite8HvQCrmMmwNDPM0Svs1V8Ltm9LXDaD-NnpjJmmcc87gDzQyn1Xq3N_1N8a33QcOxsZVd-eIWFbgbLS7F0yeyxkZky1sVJtD7Wbdmx1_6XRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
به دنیای پیش‌بینی فوتبال و کازینو با LINEBET خوش آمدید
🌍
سایت بین‌المللی و معتبر LINEBET
⚽️
پیش‌بینی فوتبال
🎰
کازینو آنلاین
💳
واریز و برداشت ریالی
🎁
بونوس 100٪ اولین واریز
🎁
بونوس 100٪ هر دوشنبه
📞
پشتیبانی فارسی فعال
🎁
کد هدیه ثبت‌نام: L5670
🔗
دانلود اپلیکیشن اندروید
👉
🔗
لینک سایت
👉
✉️
https://telegram.me/+dukgrB6-zGsyNGM8
🌐
برای ورود به سایت از IP کشورهای آسیایی یا کانادا استفاده کنید.
🇹🇷
🇨🇦
🇮🇳
Ⓜ️
📚
آموزش کامل سایت
👉</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/136375" target="_blank">📅 01:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136374">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
تصاویری از تمرین امروز تیم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/136374" target="_blank">📅 01:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136373">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✔️
امیر قلعه نویی تو جدیدترین اظهاراتش از حکومت خواسته هر کسی از تیم ملی انتقاد کرد اونارو به عنوان وطن فروش سرکوب کنه
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/136373" target="_blank">📅 00:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136372">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
قلعه نویی: ما ۳تا دستاورد بسیار بزرگ داشتیم.
🔴
۱. مظلومیت ایران را به گوش دنیا رساندیم.
🔴
۲. دومین دستاورد ما این بود تمام مردم ایران در امریکا با هر نگرشی، متحد و حامی ما شدند. بازی با نیوزلند بچه‌ها یک ربع دور استادیوم چرخیدن.
🔴
۳.  فودبالی بازی کردیم که…</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/136372" target="_blank">📅 00:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136371">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37ac31eab.mp4?token=DEIQe93PPlbYHKAfZ6w7r1sjb-Mg3unMIgb80Q_yU1saXeqlTD6A7idlyGcJNtSuoc00Zw65G44su_Y70bCKhZLFlvhL3CNtGYYvEjVLkm1H7QpJucdG53pVIJBwHG4XE-9USZ5NKUGth2G9KUQDARdjieSsWpTn5QNevzpKAjKJwwMdHxtcxtmN5onqRdW7pW8lePu6EkynygFlL3l4-yAnBJNtGM9tNmpT6KC2pFsJ1jP43NjeujDQEx7J4GB4qwttyJV0BkZsuKyJsVBIFEtuUPN9AcVpMzj0XaRDEDLJDIyYf9UkwZ3dJefE1cHtV2QRR3_7qJv5waYYPlzwaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37ac31eab.mp4?token=DEIQe93PPlbYHKAfZ6w7r1sjb-Mg3unMIgb80Q_yU1saXeqlTD6A7idlyGcJNtSuoc00Zw65G44su_Y70bCKhZLFlvhL3CNtGYYvEjVLkm1H7QpJucdG53pVIJBwHG4XE-9USZ5NKUGth2G9KUQDARdjieSsWpTn5QNevzpKAjKJwwMdHxtcxtmN5onqRdW7pW8lePu6EkynygFlL3l4-yAnBJNtGM9tNmpT6KC2pFsJ1jP43NjeujDQEx7J4GB4qwttyJV0BkZsuKyJsVBIFEtuUPN9AcVpMzj0XaRDEDLJDIyYf9UkwZ3dJefE1cHtV2QRR3_7qJv5waYYPlzwaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
✅
🎙
عادل فردوسی‌پور: سایت و اپلیکیشن پلتفرم 360 بخاطر صحبت‌های امیر قلعه نویی بسته شد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/136371" target="_blank">📅 00:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136370">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
سایت و اپلیکیشن فوتبال 360 ( برنامه عادل فردوسی پور ) چند دقیقه ای هستش که از دسترس خارج شده و خیلیا احتمال فیلتر شدنشو بخاطر حرفاش علیه قلعه نویی میدن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/136370" target="_blank">📅 00:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136369">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
خریدهای لیگ‌برتری پرسپولیس تا به امروز: مهدی‌تیکدری‌نژاد، سیدمجید عیدی، پوریا شهرآبادی، ابوالفضل جلالی، پوریا پورعلی؛ هر باشگاهی هفت سهمیه لیگ برتری و سه سهمیه بازیکن آزاد داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/136369" target="_blank">📅 00:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136368">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✅
گویا پل فلزی بندرعباس رو هم زدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/136368" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136367">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
دانیال ایری به پرسپولیس پیوست/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/136367" target="_blank">📅 23:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136366">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
قلعه نویی: ما ۳تا دستاورد بسیار بزرگ داشتیم.
🔴
۱. مظلومیت ایران را به گوش دنیا رساندیم.
🔴
۲. دومین دستاورد ما این بود تمام مردم ایران در امریکا با هر نگرشی، متحد و حامی ما شدند. بازی با نیوزلند بچه‌ها یک ربع دور استادیوم چرخیدن.
🔴
۳.  فودبالی بازی کردیم که…</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/136366" target="_blank">📅 23:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136365">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kTV_cXCs_MwRv4bEoFujh5am8Lq3zGz1-wXJC0spVVqb8QQSGdifr5feePHBCkWQwBUaPNY9rVB18c6nXgkH-MNa0FKpkqjAJ6eGimFB-devGBpu-fLWHsoQbZ9hkqwIN_-Zi1sNUW-FpQrWax2BJqgSjZYlfUXYStSnsT9rKPe6yqbBRTIo9YAhpX4H-jA62ccWGK4UqKHxtQoXsBeGQPbihpYxbBENQ-yF1utczOpU-t6FX51w5jEg8HSesoOZ8gncwLB5RcuMx-kbO8YFpMmPZTZVMZKwrzKt6xQY6448rt9R5vbcSDp9R7x6mCy1kYGAYtfk73hVrQ_LnuihcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سنتکام:
🔴
حملاتمون شروع شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/136365" target="_blank">📅 23:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136364">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✔️
✔️
فووووری/سی بی اس:
📌
یک توافق موقت درحال شکل گیری است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/136364" target="_blank">📅 23:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136363">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
قلعه‌نویی: من می‌توانستم مساوی با بلژیک رو خیلی بزرگ کنم اما خودم اولین کسی بودم که از خودم انتقاد کردم. ولی یکسری بی‌وطن ِ ایران‌فروش فضا رو خراب کردند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/136363" target="_blank">📅 23:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136362">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✔️
قلعه نویی: در همه جای دنیا انتقاد از سرمربی تیم ملی وجود دارد اما آنجا حسادت و عقده گشایی ندارند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/136362" target="_blank">📅 23:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136361">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
فووووووووووری :
🚨
🚨
سرانجام و طبق شنیده ها پرسپولیس و نساجی به توافق رسیدن و ایری راهی پرسپولیس و ابرقویی راهی نساجی خواهد شد. به همراه مبلغی پول
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/136361" target="_blank">📅 23:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136360">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">⚡️
مهدی تارتار به باشگاه دستور داده که تیم رو تا پایان هفته باید تکمیل کنند تا با نفرات کامل به اردوی ارزروم ترکیه برن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/136360" target="_blank">📅 23:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136359">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
تارتار گفته خودش کاپیتان‌ها و شماره پیراهن‌ها رو تعیین می‌کنه تا این مسائل باعث اختلاف بین بازیکنا نشه.
🔴
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/136359" target="_blank">📅 23:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136358">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✔️
امیر قلعه نویی تو جدیدترین اظهاراتش از حکومت خواسته هر کسی از تیم ملی انتقاد کرد اونارو به عنوان وطن فروش سرکوب کنه
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/136358" target="_blank">📅 23:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136357">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❌
قندلی: هرکس از من انتقاد می‌کنه عقده ای هست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/136357" target="_blank">📅 23:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136356">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
❌
شروع شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/136356" target="_blank">📅 23:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136355">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NloOzyif8SCV2NATE6eLKKPq_hSNnn6CieMDq93NaJySDN5yI1_SiMlcTBpZjC_glH4OF7B5g0CerK_ZMCAvSktBoStqumm-bz1vRpwXGdQZD-R4iuK7X1ptQF71101vEaX6_nSu1UrJzfGt2gqwSJO70Gj0TuvfXpSmRGycOYrzysLI-ESmFU2f6MdVhq1qqZJ1oqqTGprhMDguGqgZ-bIqqwmRtS3vM8SGQMeNtjDG4PA5sJdVHeqkkBvwqeB2udNnsRbYrObPZbUoEsHdJShhGQhzM_wiKKYpH0tClKwj-1CjpESjtHZU66PdmqVTrYE2uRNX2o0_CV4CU3Nneg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
سید بندی لیگ نخبگان آسیا منطقه غرب
❌
استقلال در سید اول در کنار: الاهلی، العین، السد و ترتر تو سید سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/136355" target="_blank">📅 23:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136354">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❗️
❗️
#فوری | کانال 13 اسرائیلی:
🔴
ترامپ پیامی به کشورهای خلیج ارسال کرد:
🔴
اگر در این هفته به توافقی برای آتش‌بس دست نیابید، خود را برای یک تشدید جدی با ایران آماده کنید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/136354" target="_blank">📅 23:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136353">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✅
سپاهان برای جدایی آریا یوسفی، خواستار انتقال ایگور سرگیف و حسین ابرقویی به این تیم شده که با مخالف باشگاه پرسپولیس رو به رو شده / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/136353" target="_blank">📅 23:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136352">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
🔴
اخباری قراره بیاد تهران و با تارتار صحبت کنه و اگه همه چیز برای رقابتی بودن دروازه پرسپولیس اوکی بود قرارداد شو امضا کنه. احتمال اینکه اخباری پرسپولیسی بشه خیلی زیاده/ تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/136352" target="_blank">📅 23:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136351">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
گروهبان قندلی مهمان امشب برنامه میساکی در شبکه سه خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/136351" target="_blank">📅 23:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136350">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
ادامه حملات عادل فردوسی‌پور به قلعه‌نویی: هرکه از "غار" حرف بزند، قابل توجیه است؛ به جز آن کسی که کل جنگ را در دبی و ویلای آلانیا گذرانده باشد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/136350" target="_blank">📅 22:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136349">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
#فوری
🔴
یاسر آسانی ستاره آلبانیایی فصل قبل استقلال در آستانه پیوستن به تراکتور قرار دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/136349" target="_blank">📅 22:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136348">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❗️
❗️
#فوری | کانال 13 اسرائیلی:
🔴
ترامپ پیامی به کشورهای خلیج ارسال کرد:
🔴
اگر در این هفته به توافقی برای آتش‌بس دست نیابید، خود را برای یک تشدید جدی با ایران آماده کنید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/136348" target="_blank">📅 22:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136347">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
دانیال ایری به پرسپولیس پیوست/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/136347" target="_blank">📅 22:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136346">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/136346" target="_blank">📅 22:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136345">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/136345" target="_blank">📅 22:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136344">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
فیلمی که از تجهیزات نظامی ایرانی از خوزستان به سمت مرزهای کویت در حرکت است و در حال پخشه قدیمیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/136344" target="_blank">📅 22:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136342">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❗️
مجید عیدی خرید جدید پرسپولیس با شماره 2 که سالها بر تن امید عالیشاه بود برای پرسپولیس به میدان خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/136342" target="_blank">📅 22:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136341">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❗️
مجید عیدی خرید جدید پرسپولیس با شماره 2 که سالها بر تن امید عالیشاه بود برای پرسپولیس به میدان خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/136341" target="_blank">📅 22:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136339">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
خریدهای لیگ‌برتری پرسپولیس تا به امروز: مهدی‌تیکدری‌نژاد، سیدمجید عیدی، پوریا شهرآبادی، ابوالفضل جلالی، پوریا پورعلی؛ هر باشگاهی هفت سهمیه لیگ برتری و سه سهمیه بازیکن آزاد داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/136339" target="_blank">📅 22:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136336">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
🤝
پرسپولیس تا آخر هفته با چهار بازیکن جدید قرارداد امضا خواهد کرد / خبرنگار فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/136336" target="_blank">📅 22:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136335">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/136335" target="_blank">📅 22:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136334">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/136334" target="_blank">📅 22:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136333">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">جالب اینه تموم فرم ها رایگانه، حتما عضو شین و‌ چک کنید چقد راحت سود میشه کرد
😉
✅
JOIN JOIN JOIN
JOIN JOIN JOIN</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/136333" target="_blank">📅 21:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136332">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcWFSrlH9a6gmDb5GdrIVCD-13U7nlyP1nDsIvjc1E9hHe7fPj9rN6Lefk4TDzR5XeY_nt445y9PrJAKNv9_iaq4yCztrnLNQKFQs3AnSVw3GcHwM13KxbRtq8a-ySCHf8E1NZw7MVKYjdL-lCYOTTddqRFDENtMzs1H8icwbSDDESrBiNZFnWHum0GRhR3d_KEifLhh389fSTqaCyVbf_4dCM_MIwlwD6A2_dJzjK3P04xPH6yNwCGeLbPqV7pIExvyQddgm-NjOQaaO-zt0KkkyVfx1Xn2tjYZE8ZDYkHklm_YOpLnc-U2VMYc-lw4V_-BPXjwqemoloxMNTn34Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب حتی با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
میگی ن ؟ بیا تو چنلمون و ببین
🤷‍♂️
@PeakyBetBlinders
@PeakyBetBlinders
@PeakyBetBlinders</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/136332" target="_blank">📅 21:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136331">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXZqEBj6rz4qqbE15rfhiUln9KvsomVtdGLhoEPDtWi95jOroFYGvk_KgaQKC89oy8X9kgJS0dTA1KMYRI0DPon9MuAdjj07QubnAj7pEdjbBL7ISl402Wc6zxtmZA7g03f5-N7Vli3eZJNudZwQteaQ2AyQp2VQcmX1xsF6KI88Axp4uXUOAE0VTGs3bGQfzUNAHOERvgH7iQ8P3b-Agm-9SjWXnJPgvK2ij91-C7NVP5QSTSlfAcmKLSX0XyfEmlc-CZsZWUQaASLWuZU1GfMJMXTFSQyfOVe4D2NG-KHW2Zv6Chmb_BOpRe8Jryn47pm28lj2L0D1AnA0vWeOpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فووووووووووری :
🚨
🚨
سرانجام و طبق شنیده ها پرسپولیس و نساجی به توافق رسیدن و ایری راهی پرسپولیس و ابرقویی راهی نساجی خواهد شد. به همراه مبلغی پول
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/136331" target="_blank">📅 21:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136330">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7XLmxbHY62a2UJucZe79Kw8JqQEWQ1o5Z5HlkvIaDgYCtVd1zQ4y9NfLO8OMt7MtWAyVmF74S59eiL6JPvEsT3iMPZ-WgbtXxuKnsRhtTpe_7_B8UlVRuHEK9kxbfGqg8OsU7IcmR0fI2Gp3-lLYO989tQwH448LBBmLMSOAwO6DbgMdVtFSLr-s48G9TUg4OYFa1AN5eOJMoie4skAg7hjDNUqwHpMwB6eakqjUtij_N7Y3LL0h0ycCaV0W9mtl1Qmd8DjY1tE_NSJceAH-OLOpQxeCQ1D_9XqEmKiQ-zq9En5VV3LACRtv6S5Nq4ZOp2l-yCo2UiZcJZlqzjLxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تصاویری از تمرین امروز تیم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/136330" target="_blank">📅 21:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136329">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
شبکه "فاکس نیوز": نیروهای ویژه ارتش آمریکا سال‌هاست که برای ورود زمینی به ایران آموزش می‌بینند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/136329" target="_blank">📅 21:28 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
