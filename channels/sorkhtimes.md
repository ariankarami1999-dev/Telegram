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
<img src="https://cdn4.telesco.pe/file/YlMl7NJGgf81KO7Gxkmu4srEhG4ZMdC1WAp5xHRpCXtWh-7klBbPicUVU1hqYbAIP9HJ5Cflb8XhqpwPbN_qvV4w0f8ASHQJsVa63zQHlz7M6RIdgsL3ouqmDH2IfWWAtodDXMvj3dRE6FUDUHNhF1tcjkdeyKsLTDV7HluYjCqpXgc8vk72NBO0W5jmH7m8Px_PAlAL9Cilq1URIrvXjM7i20J5xEhlKDEp8qeluSZZjI7PzBDRZN7l3iyT0O8AhttGoPihj88y-Z2QAwa9_BcEe5fahgoca3tqPpAFRgHA7xfIOkWf9NoeNiKy-loV49xPJALfIP5lqEqeV8KNdQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 18:23:08</div>
<hr>

<div class="tg-post" id="msg-135289">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4FqI4P8A2kUIZQAodQgxiozEe4b61OMPH_ms7N1qETem3dEua3KnEH34ZG4HWhb-8sBbSwDnzc98vi7vMAhsorengTcQE6BZZyNxe4Oh2FWjGwknLlx6QoRr6-41KcMLG8kgLUOx5T50nLLjnF5n3awByNcNiPJuQSpOufGMXTOI4FRQMHdnx-kT_DySkgHbduB5EPWaj0zLEKlf4gF6rztm76wUnpN2jOEBjOtIbballwoLsMY-BdE6PjD1t7SQ-sZTXcVRIbgUd22Vhlf-I0JlAkY30DMLZ5HYnRkU-ktE3fHbSjn6frMUXp9eZGsWjN2ZFZp7-aeeWon89wkqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصاویری از حضور بازیکنان تیم پرسپولیس برای انجام نخستین تمرین برای شروع فصل جدید
که چهره ها نشون از روحیه و شادابی بچه ها داره با کادر جدید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 550 · <a href="https://t.me/SorkhTimes/135289" target="_blank">📅 18:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135288">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
احتمالا باشگاه برای رونمایی لایو داره  وگرنه چه‌ اصراریه که تاخیر داشته باشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/SorkhTimes/135288" target="_blank">📅 17:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135287">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
✅
باشگاه ماهم عالیه
❗️
طاهری، شهرآبادی، جلالی بستن و عکس هم انداختن پوسترشونم امادست
❌
اما باشگاه میخاد یجوری رونمایی کنه که تبلیغات داشته باشه
😐
مثلاً لایو بزاره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/SorkhTimes/135287" target="_blank">📅 17:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135286">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
🇺🇸
ترامپ:
❗️
دیشب جزیره خارک رو زدیم ولی به نیروهامون گفتم نفت‌ش رو نزنید ممکنه بخوایم جزیره رو تصرف کنیم چون از دستشون کاری برنمیاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/SorkhTimes/135286" target="_blank">📅 17:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135285">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
باشگاه به خاطر فشار هوادارا فعلا پورعلی رو تو آب نمک خوابونده تا نتیجه مذاکرات با قربانی و نوراللهی رو پیگیری کنه و اگه اونا جذب نشن پورعلی رو نهایی می‌کنه/ فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/SorkhTimes/135285" target="_blank">📅 17:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135284">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
تایید خبر دیشب مون
🚨
🚨
🚨
🚨
تسنیم: ابوالفضل جلالی دو ساله به پرسپولیس پیوست.همچین پوریا شهرآبادی چهار ساله با پرسپولیس امضا کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/SorkhTimes/135284" target="_blank">📅 17:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135283">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
❌
احتمال افزایش نفرات لیست مازاد پرسپولیس؛
🔴
وضعیت نامشخص چند سرخ‌پوش
❗️
❗️
فرهیختگان: دور جدید تمرینات پرسپولیس در حالی از فردا چهارشنبه در زمین شماره سه ورزشگاه آزادی برگزار خواهد شد که هنوز تکلیف نهایی برخی از بازیکنان این تیم مشخص نیست.
✅
✅
اگرچه مهدی تارتار…</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SorkhTimes/135283" target="_blank">📅 17:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135282">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❗️
ترامپ: حملات امشب به ایران ممکنه خیلی بزرگ باشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SorkhTimes/135282" target="_blank">📅 17:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135281">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❗️
❗️
#فوووووری از ترامپ: آتش‌بس با ایران به پایان رسید و از این لحظه هر دستوری بخواهم برای زدن ضربه نهایی خواهم داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SorkhTimes/135281" target="_blank">📅 17:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135280">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✅
مطابق اعلام سایت ترانسفر مارکت؛ تا به این لحظه مهدی ترابی و مهدی هاشم نژاد قراردادی برای فصل آینده با باشگاه تراکتور ندارند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/135280" target="_blank">📅 16:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135279">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✅
🚨
🚨
⭕️
بازگشت خانبان به پرسپولیس: به‌زودی....!
⭕️
بر اساس شنیده ها، مدیران ارشد باشگاه پرسپولیس با توصیه خداداد عزیزی به دنبال بازگرداندن مهرداد خانبان آنالیزور سابق پرسپولیس به کادرفنی پرسپولیس است
🔸
آنطور که از باشگاه پرسپولیس خبر می‌رسد احتمالا باید برای…</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/135279" target="_blank">📅 16:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135278">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
💙
ابولفضل جلالی با قراردادی دو ساله رسما به پرسپولیس پیوست.
❓
نظرتون درباره جلالی چیه ؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/135278" target="_blank">📅 15:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135277">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
💙
ابولفضل جلالی با قراردادی دو ساله رسما به پرسپولیس پیوست.
❓
نظرتون درباره جلالی چیه ؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/135277" target="_blank">📅 15:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135276">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
❌
البته این خبر هنوز رسمی اعلام نشده و یکی از ادمین های ما در نشر آن عجله کرده. جلالی گفته امروز، فردا با رسانه باشگاه مصاحبه می کند که پالسی است به نشانه امضای قرارداد‌. این مدافع چپ جوان به تازگی تمام پست هایش با پیراهن استقلال را در اینستاگرامش پاک کرد.…</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/135276" target="_blank">📅 15:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135275">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
💙
ابولفضل جلالی با قراردادی دو ساله رسما به پرسپولیس پیوست.
❓
نظرتون درباره جلالی چیه ؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/135275" target="_blank">📅 14:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135274">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❗️
با تایید سهیل صحرایی این بازیکن به عنوان بخشی از مبلغ رضایت نامه گلگهر برای شهرآبادی، از پرسپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/135274" target="_blank">📅 14:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135273">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❗️
شنیده ها :گل‌گهر برای شهرآبادی 120 تا میخواسته
❌
ولی گویا صحرایی + 80 میلیارد توافق کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/135273" target="_blank">📅 14:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135272">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/295a60cd54.mp4?token=C5bMX2S7sv62w2cGsY3H43nb4lr47HqMP8uMH1_q6_6aNU1UX8J5Zi9fYkzoORhvOiU7jkvXHkv8J_67Z5rv_cWC9g3CMiqzY36OFEk6b4coS1i-bnXQ0LKylWDnjFlncQbi0FACu_6tHr0bchUqWNDFIZ0WpA6kTGRgHG9qQ7-3yVqRMaJq3lx6gdEsKeS0JT0otaz_jzyAEY3CRVpvGlaJVysdYz1GF8RdAAa6103fYMsXsip_pNJ96_qL3j9vsaqFctYunF8XtrIcfAluNqymFknF5B1cYkIxcXoRvaJnzqTsKj8dAl5o5vblmJzoxWAoSlcjnHhT2NHMS2okLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/295a60cd54.mp4?token=C5bMX2S7sv62w2cGsY3H43nb4lr47HqMP8uMH1_q6_6aNU1UX8J5Zi9fYkzoORhvOiU7jkvXHkv8J_67Z5rv_cWC9g3CMiqzY36OFEk6b4coS1i-bnXQ0LKylWDnjFlncQbi0FACu_6tHr0bchUqWNDFIZ0WpA6kTGRgHG9qQ7-3yVqRMaJq3lx6gdEsKeS0JT0otaz_jzyAEY3CRVpvGlaJVysdYz1GF8RdAAa6103fYMsXsip_pNJ96_qL3j9vsaqFctYunF8XtrIcfAluNqymFknF5B1cYkIxcXoRvaJnzqTsKj8dAl5o5vblmJzoxWAoSlcjnHhT2NHMS2okLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سهیل صحرایی هم وارد دفتر باشگاه شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/135272" target="_blank">📅 14:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135271">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135271" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✈️
اپلیکیشن MelBet
🥇
🎁
کد هدیه 100 دلاری:
Sport100
🔒
برای تعیین رمز ورود حداقل از 8 کاراکتر و حروف بزرگ و کوچک انگلیسی و اعداد انگلیسی استفاده کنید، مانند Hamid120
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/135271" target="_blank">📅 14:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135270">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">⚠️
خیلیا نمیدونن که اگه ثبت‌نامشون رو با لینک زیر انجام بدن...
⁉️
💥
بونوس خوش‌آمد گویی تا %220 بیشتر میگیرن!
فقط کافیه به لینک زیر مراجعه کنید و وارد ملبت بشید و به راحتی ثبتنام کنید!
👌
🌐
لینک بدون فیلتر سایت معتبر ملبت
👇
🌐
www.MelBet1.com
🎁
بعد از ثبتنام، وارد حسابت شو و توی بخش "بونوس‌ها" فعالش کن
🎚️
نکته:
فقط این هفته فعاله، پس از دستش نده
🙂
🎁
کد هدیه 100 دلاری فراموش نشه:
Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/135270" target="_blank">📅 14:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135269">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTwy7f9wMUs7Dri0w33b8ivSfqb9iWcG9axLXsc5lnLtPuLxd6zAJ5BXuT1Xw73pVszp3RbFbxbPJA-uaSA9Hqq0q987TEHbKVbEngy1AFPTbtRgpe6nZoLB7Hpbn39N3ie3Vb-vLBwccSqlICgzto-qwCS_OxwvFkKl8X1kHpmMeEiuDUv8T8pZLkJceXvE5LaEMBfcLUVN-GBH4gttviijhuwDqGb_8KODK9lV4MTK2UJnyYD2KXnIMzqpjZ9283ccwgpk4IXZPbqZQxrYKoVAq_e7mCXBU96KJvDSSTvDLkAGSA0snkhuQ08hYQtxOU5TepysBHShAxnTom_f3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💙
ابولفضل جلالی با قراردادی دو ساله رسما به پرسپولیس پیوست
.
❓
نظرتون درباره جلالی چیه ؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/135269" target="_blank">📅 14:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135268">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c56bb19ad7.mp4?token=uoI32EUzEZ-_Y-m7VZt7sgUOrHk8tEXYg0v49h3jBs0s8Zi8e1UvXFA5Bx2LkW0u8cRHpwJt755R18BHwmqdzlQ21mL95057UN9mzD_2MrY4QV_DIp6zJlWQtczuLkdmw27Mws9H8NiE6Zel2F7NtlhWpI80E2qXoQyJpuBAC7-2NA-V6YUNA5sQqHPlqkWGPpb3JwwPSnSdVU8js7c5p8Z7nConzy0K5aEdxsh7EGwfBiz581IFM4eUjk3fZO5BaIBWVIKfmdIgRyP1crX_73DQKci14rv36XDp6CW0YNb1FD5MfwXsbUpuO_hswyGhsKNIddw4HuOndJGNNc-dpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c56bb19ad7.mp4?token=uoI32EUzEZ-_Y-m7VZt7sgUOrHk8tEXYg0v49h3jBs0s8Zi8e1UvXFA5Bx2LkW0u8cRHpwJt755R18BHwmqdzlQ21mL95057UN9mzD_2MrY4QV_DIp6zJlWQtczuLkdmw27Mws9H8NiE6Zel2F7NtlhWpI80E2qXoQyJpuBAC7-2NA-V6YUNA5sQqHPlqkWGPpb3JwwPSnSdVU8js7c5p8Z7nConzy0K5aEdxsh7EGwfBiz581IFM4eUjk3fZO5BaIBWVIKfmdIgRyP1crX_73DQKci14rv36XDp6CW0YNb1FD5MfwXsbUpuO_hswyGhsKNIddw4HuOndJGNNc-dpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پوریا شهرآبادی هم بعد از جلسه با مدیران پرسپولیس، مثل جلالی بدون اینکه با خبرنگارا حرف بزنه، محل جلسه رو ترک کرد و رفت اردوی تیم امید.
✅
✅
خودش گفت باشگاه اجازه مصاحبه با رسانه‌ها رو بهش نداده...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/135268" target="_blank">📅 14:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135267">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e4a201f71.mp4?token=nYPb46qE6ietH6HTgeY-SZNCzgA6U0BEhCnuThWtHcAfBlBaGPQ5URBjsCnMulRPmLqgl8fgrFLHOjMcR7_uAxnWVDuQoOnmU2zvlpOdGZ5iqm2B531WajGv5UihYhrdMON4EshZvXi0n-Rcb7U5QEBs4abz04LMs1TYBCd1MYuqXWdyqxCUIosTy-OHOOAUMiXbueuCaouAuy8cJKX7DpNM3o_NL3CAPuEOJcf7ivbSjF_UtsyFhXyYnwgh1swROuF7yJctV0hkKd3oCiyTraxEOuinuhmlgdTIawDUCLWMGR1bejenksdmIzTNUwzRJ3Cz-xzC7NOv0n6Sf7vDrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e4a201f71.mp4?token=nYPb46qE6ietH6HTgeY-SZNCzgA6U0BEhCnuThWtHcAfBlBaGPQ5URBjsCnMulRPmLqgl8fgrFLHOjMcR7_uAxnWVDuQoOnmU2zvlpOdGZ5iqm2B531WajGv5UihYhrdMON4EshZvXi0n-Rcb7U5QEBs4abz04LMs1TYBCd1MYuqXWdyqxCUIosTy-OHOOAUMiXbueuCaouAuy8cJKX7DpNM3o_NL3CAPuEOJcf7ivbSjF_UtsyFhXyYnwgh1swROuF7yJctV0hkKd3oCiyTraxEOuinuhmlgdTIawDUCLWMGR1bejenksdmIzTNUwzRJ3Cz-xzC7NOv0n6Sf7vDrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🏅
جلالی هم اومد بیرون… به خبرنگار ها گفته با رسانه باشگاه مصاحبه کردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/135267" target="_blank">📅 14:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135266">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24a7269d75.mp4?token=qYTMq9IFjC89DgYxwj0r38vKG_XUZx_7U_0jNetF8KCd7IAt0NpC9uSnkm7ghbr2wZ2qbS3k6EuZAW8zKAwPVp9NK8SdrqZJfIA-3kSaXYg5LtdBnJGOw9UfDw4thQkKExBgOYaZxO3bdV4r5ik5FNmK1c0r3-sNwNgRa-T0viYW-ni5dt1YQIOggFJ3Rct4KZ4_z2V9RflTE3Cydztr-_9kcah-unWMrcu36M-r6018b4-tiYE5JnNP66iHtcfoTYRk5snU9CCt4ZqCQ8IIWWmhKS5m-vN1LE4w36NsylngHVCo8ZTsJnkiODhtSGK1wg0xJ-M1PU_oaQCpgwpAcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24a7269d75.mp4?token=qYTMq9IFjC89DgYxwj0r38vKG_XUZx_7U_0jNetF8KCd7IAt0NpC9uSnkm7ghbr2wZ2qbS3k6EuZAW8zKAwPVp9NK8SdrqZJfIA-3kSaXYg5LtdBnJGOw9UfDw4thQkKExBgOYaZxO3bdV4r5ik5FNmK1c0r3-sNwNgRa-T0viYW-ni5dt1YQIOggFJ3Rct4KZ4_z2V9RflTE3Cydztr-_9kcah-unWMrcu36M-r6018b4-tiYE5JnNP66iHtcfoTYRk5snU9CCt4ZqCQ8IIWWmhKS5m-vN1LE4w36NsylngHVCo8ZTsJnkiODhtSGK1wg0xJ-M1PU_oaQCpgwpAcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
محسن خلیلی برای عکس یادگاری با خرید های جدید وارد باشگاه شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/135266" target="_blank">📅 13:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135265">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwCK4NH-sGP63d3H5zDHOJj6pTx4H541FY2KWvYGbsZKu4H3DH8r_CnJaGt7OEtcA9Y92fX2QDna7ShZgVxfqt4XYP6BOfoh9jGSf6kD43TEOOZfaxLTffzeYmIGSsuHtoJ52hd4v0lS7BfrsGvo5vmf0UNme14WnwWNSCy_ODbulfAn9Eh92sFlAwiqt5RW3GqcI-Uqpo3_LLHPB-f7V2PVgUlhfs5ePw3dIxfmnsuP9J4oYd_ojpBUCLP1ugtyxdZJyibuLPKdD1oFWQlyulnPD77Onw-KRDyEvm7wUN4PpQ5hAo01TlpLHXxK2QsZaY-MLp1XKOLJAm_VVZxd4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
نظرتون در مورد ابوالفضل جلالی؟؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/135265" target="_blank">📅 13:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135264">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86ba7ad723.mp4?token=segAs-eZy37hCT-dcwYqnR0EJqsLSnc2P8JaEH6sfr3pWjyu-wZ9WSzskK-maP-Xgfm3P7ml7703vXNQAsOWZT3FygsucBMVG9Ut71WOs-oidFymVBEBFTU2a4xB7jRRFuhCeh_JfrLCwQ8PNDwJbdyLiA7qWA6pGPMo_q5FhItBeS589X-DJHxXDOd7IrZU-BsYopBjpTYXgx8Y4GlwIaBCmX08LRN2AoNxihJX_3bgVua2r5MF68jHtIvBwgPG_zxj-2EA-i-ogfsCTZ7C-bYOXNSPILMPzPBel3zrrQMfsCpxCG6eX0yyaOs_W616YAg3j7AqYZ7ghnpDEaY7Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86ba7ad723.mp4?token=segAs-eZy37hCT-dcwYqnR0EJqsLSnc2P8JaEH6sfr3pWjyu-wZ9WSzskK-maP-Xgfm3P7ml7703vXNQAsOWZT3FygsucBMVG9Ut71WOs-oidFymVBEBFTU2a4xB7jRRFuhCeh_JfrLCwQ8PNDwJbdyLiA7qWA6pGPMo_q5FhItBeS589X-DJHxXDOd7IrZU-BsYopBjpTYXgx8Y4GlwIaBCmX08LRN2AoNxihJX_3bgVua2r5MF68jHtIvBwgPG_zxj-2EA-i-ogfsCTZ7C-bYOXNSPILMPzPBel3zrrQMfsCpxCG6eX0yyaOs_W616YAg3j7AqYZ7ghnpDEaY7Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
گل پوریا شهرآبادی به استقلال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/135264" target="_blank">📅 13:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135263">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
پوریا شهرآبادی برای عقد قرارداد وارد ساختمان باشگاه پرسپولیس شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/135263" target="_blank">📅 13:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135262">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/838edcfe33.mp4?token=Zlg4x8esX8hlVV8D3gsrgGSOtzCSN5f1ONJ8T4Fp6DXPm2V_q53ZBvQ34wCC-Mdl0xFo-ejcB6EYnmgrFTihBzttkB0Sx3xKq2AUWLoDsNrG8mOQghiUTCRDidsLRzRNznXHjfmxl-ijXtrX3gTUKXggfFkEzQlwVCLORxDv-lDia7u6oqZPisB59-YRYycXoGvshOaA7buZTgd_2hp3TkQmUGMQS6RX5f2ir-Q-u8eDvcqF3HRWm6Fouq7YCRjH4aXC0G7FlVnYJFOAtdno_3Hbre7L7d10ZhralwDX4UuzfTAB5CaRewrIs6ezwpJvigcJtpjwbX_JkkRrojq8Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/838edcfe33.mp4?token=Zlg4x8esX8hlVV8D3gsrgGSOtzCSN5f1ONJ8T4Fp6DXPm2V_q53ZBvQ34wCC-Mdl0xFo-ejcB6EYnmgrFTihBzttkB0Sx3xKq2AUWLoDsNrG8mOQghiUTCRDidsLRzRNznXHjfmxl-ijXtrX3gTUKXggfFkEzQlwVCLORxDv-lDia7u6oqZPisB59-YRYycXoGvshOaA7buZTgd_2hp3TkQmUGMQS6RX5f2ir-Q-u8eDvcqF3HRWm6Fouq7YCRjH4aXC0G7FlVnYJFOAtdno_3Hbre7L7d10ZhralwDX4UuzfTAB5CaRewrIs6ezwpJvigcJtpjwbX_JkkRrojq8Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پوریا شهرآبادی برای عقد قرارداد وارد ساختمان باشگاه پرسپولیس شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/135262" target="_blank">📅 13:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135261">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔹
فوری؛ابوالفضل‌جلالی مدافع‌سابق استقلال برای عقد قرارداد با باشگاه پرسپولیس وارد ساختمان این باشگاه شد. قرارداد 2+1 ساله توافق شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/135261" target="_blank">📅 13:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135260">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
فرزین معامله گری خرید چهل میلیاردی خلیلی به خاطر تمدید محمدی و خرید جلالی در لیست مازاد تارتار قرار گرفت/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/135260" target="_blank">📅 13:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135258">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
ترامپ: ایران دروغگوعه و من از امروز به بعد دیگه نمی‌خوام هیچ ارتباطی باهاشون داشته باشم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/135258" target="_blank">📅 12:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135257">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
فوری/ ترامپ: به نظر من، توافق‌نامه با ایران به پایان رسیده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/135257" target="_blank">📅 12:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135256">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❗️
فیفا به درخواست ترامپ، کارت قرمزی که مهاجم آمریکا، داخل بازی قبل گرفته بود رو بخشید تا محرومیت بازیکن تو بازی بعد جام جهانی رفع بشه!!
❗️
پ.ن سیاست آوردن تو فوتبال و ترس از آمریکا و ترامپ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/135256" target="_blank">📅 12:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135255">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✅
اگر پرسپولیس همزمان مهدی زارع و مسعود محبی را جذب کند، پرونده انتقال علی نعمتی به‌طور کامل بسته خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/135255" target="_blank">📅 11:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135254">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
❌
هوشنگ‌ سعادتی به مدیر پرسپولیس قول داده امروز جلالی رو ببره ساختمان باشگاه پرسپولیس برای عقد قرارداد؛ اگه باشگاه استقلال تا ساعات آینده با جلالی برای تمدید تماس نگیره امروز ازیاغی جدید فوتبال ایران رونمایی خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/135254" target="_blank">📅 11:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135253">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✅
مصاحبه‌جدید دراگان‌اسکوچیچ: هرگز برای یک فصل حضور در پرسپولیس 3 میلیون دلار تقاضا نکرده بودم.
🔴
بایک‌ باشگاه‌ بزرگ در حال مذاکره هستم و ممکنه برای‌فصل‌جدید مجدد به لیگ برتر برگردم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/135253" target="_blank">📅 10:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135252">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
یاگو به عنوان مربی بدنساز فصل آینده پرسپولیس انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/135252" target="_blank">📅 10:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135251">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
❌
شوک بزرگ به استقلال؛ سایت آفریقایی Africafoot مراکش نوشت که مونیر الحدادی ستاره استقلال با باشگاه الاتحاد مراکش توافق کرده...
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/135251" target="_blank">📅 10:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135250">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">⚡️
⚡️
آسانی و منیر حدادی در آستانه ترک ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/135250" target="_blank">📅 10:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135249">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
برای تمرین امروز چهارشنبه به بازیکنان  پرسپولیس اطلاع‌رسانی شده و در این بین به ۳ بازیکن دارای قرارداد، گفته شده که تا مشخص شدن وضعیت‌شان، در تمرین شرکت نکنند.
✅
امید عالیشاه، مرتضی پورعلی گنجی و میلاد سرلک این سه بازیکن هستند.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/135249" target="_blank">📅 10:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135248">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❗️
امروز پرسپولیس روز شلوغی خواهد داشت...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/135248" target="_blank">📅 10:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135247">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❗️
اسکوچیچ: با پرسپولیس توافق کردم انواع و افسام انعطاف پذیری ها رو داشتم اما در آخر قراردادی که برای من فرستادن مبلغش خیلی کمتر از اون چیزی بود که توافق کرده بودیم و من از این موضوع بسیار ناراحت شدم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/135247" target="_blank">📅 09:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135246">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✅
❗️
باشگاه پرسپولیس خطاب به ابوالفضل جلالی: اگه قصدت بازار گرمی نیست بیا قرارداد باهات ببندیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/135246" target="_blank">📅 09:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135245">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❗️
فووووووووووووری
🚨
قدوسی: حضور علی نعمتی در پرسپولیس احتمالا منتفی است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/135245" target="_blank">📅 09:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135244">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
برای تمرین امروز چهارشنبه به بازیکنان  پرسپولیس اطلاع‌رسانی شده و در این بین به ۳ بازیکن دارای قرارداد، گفته شده که تا مشخص شدن وضعیت‌شان، در تمرین شرکت نکنند.
✅
امید عالیشاه، مرتضی پورعلی گنجی و میلاد سرلک این سه بازیکن هستند.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/135244" target="_blank">📅 09:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135243">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBCAKkZMdQSLUBQpOfI95ByBsSAZySHaQ1kQZF9hKnhg0K4m-auTcaOGi9zQBvZQ2t2BSxhkshjkx01Yvo927Zq8g1n978zsUJAM7k6qH13xeI6lassTjOA20_sNbKZEbUjppZZwrxShBnEdZvg3y5FX5_UUGNio8-QwLwmmXAwAyc-NA5RqsXFu0zGUidvgC6xgP8GGUcMTtST8XrZSJsScfaLsn5uXtCud0PXeylhPqRnt3rYqGDn8l797m6XDiCDqFFVlvJqKNOf_gSOiB1K_K4cp7l1eTZafTALpbbqF3nfD1GHYFjbROBs7I4Bx1Ne5UdYeJFROk2_WCOwbfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
برای تمرین امروز چهارشنبه به بازیکنان  پرسپولیس اطلاع‌رسانی شده و در این بین به ۳ بازیکن دارای قرارداد، گفته شده که تا مشخص شدن وضعیت‌شان، در تمرین شرکت نکنند
.
✅
امید عالیشاه، مرتضی پورعلی گنجی و میلاد سرلک این سه بازیکن هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/135243" target="_blank">📅 09:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135242">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✅
نمودار درختی دور یک چهارم؛
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/135242" target="_blank">📅 09:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135241">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135241" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر پنجشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
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
https://t.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/135241" target="_blank">📅 01:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135240">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4XX9HWAMfNdvdcIGqqt63PCen4X2UCD_OJQOF75vJ8w8EExP7htKe5I-XhKq5hUj86TKiZymKi_QImt6FSR1RRwm4Maz3kcnJY6tkd_EB_M58_Hhs64oHrSndBAdVeTJrO_8ZyfNuRfpaBTfm3e8gziRtbMMKWJ6OE1t6onPsQWgS2TO06WUbWrg447cX3AlAx8qcWDDg50NwT5gx561t2Z7ZxSeYJleG0KtceO7hnTnZljsqHuzbVfNiqTyi76mOHZdcD5l7nhgZeQllsL8ygIZLxf80Km_YAJfYKa9C5db0JBhKzCh2aLbUefPi9PnHWrtaL_m_PDjOI-MEIipA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اولین سایت جهانی برای کاربران ایران با واریز برداشت مستقیم
⬇️
🪙
سایت بین المللی و معتبر لاین
بت
❤️‍🔥
اسپانسر لیگ  فرانسه
💳
واریز و برداشت ریالی
👀
بازگشت باخت ب صورت هفتگی
📣
دارای پشتیبانی فارسی فعال
🎁
بونوس
💯
روز های دوشنبه
🎡
کدهدیه ثبت نام
➡️
L5670
🔗
《 لینک سایت برای کاربران ایرانی》
👍
《 دانلود اپلیکیشن اندروید》
❤️
https://t.me/+dukgrB6-zGsyNGM8
🔻
جهت استفاده از وبسایت از آی پی کشورهای آسیایی
🇷🇺
یا کانادا
🇨🇦
، استفاده کنید
Ⓜ️
✔️
آموزش کامل و جامع شرطبندی
👉</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/135240" target="_blank">📅 01:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135239">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❗️
فوووووووری/سنتکام: در پاسخ هم حملات ایران به کشتی‌های تجاری و نقض آتش بس، مناطقی در جنوب ایران را بمباران کردیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/135239" target="_blank">📅 01:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135238">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✅
✅
فوووووری؛ آغاز عملیات شبانه ارتش آمریکا در جزایر جنوبی ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/135238" target="_blank">📅 00:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135237">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❗️
❗️
فوووووووری/ارتش آمریکا در پاسخ به نقض آتش بس از سوی ایران، اهدافی را در جنوب ایران هدف قرار داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/135237" target="_blank">📅 00:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135236">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
❌
حسام حسن، سرمربی تیم ملی مصر پس از حذف در بازی با آرژانتین با ادبیاتی تند گفت:
🎙
هر عواقبی را می‌پذیرم اما می‌گویم که این مسابقه کاملاً مهندسی و تبانی‌شده بود و همه دنیا این را دیدند. اگر تا این حد اصرار دارند که آرژانتین قهرمان شود، چرا از بقیه تیم‌ها…</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/135236" target="_blank">📅 00:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135235">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
🔴
به امید عالیشاه، میلاد سرلک و مرتضی پورعلی‌گنجی اعلام شده در تمرینات حاضر نشوند و در لیست مازاد قرار گرفتند.
🔴
🔴
باشگاه همچنین به سروش رفیعی اطلاع داده قصد تمدید قراردادش را ندارد.
🔴
🔴
تارتار هم گفته هفته آینده درباره ادامه همکاری با بیفوما تصمیم نهایی…</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/135235" target="_blank">📅 00:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135233">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❗️
❗️
وای چیه این فوتبال ..از دقیقه 80 تا 90 آرژانتین سه گل زد و بازی سه بر دو جلو افتاد ..برگام ...جونم به این فوتبال جذاب ..مسی موند تو جام
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/135233" target="_blank">📅 00:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135232">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❗️
با جدایی اوسمار ویه را و حضور تارتار فرزین معامله گری در پرسپولیس ماندنی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/135232" target="_blank">📅 22:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135231">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✅
دراگان اسکوچیچ:
❌
چون اجازه دخالت در نقل‌ و انتقالات را به مدیریت ندادم حضورم در پرسپولیس منتفی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/135231" target="_blank">📅 22:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135230">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❗️
❗️
فرهیختگان: علی علیپور برای تمدید قرارداد با پرسپولیس کمی فرصت خواسته تا پیشنهادات حوزه خلیج فارس‌ اش را بررسی کند سپس پاسخ نهایی را به باشگاه بدهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/135230" target="_blank">📅 22:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135229">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✅
✅
محمد گندمی ؛ سهیل صحرایی، فرزین معامله گری ، علیرضا همایی فرد و کسری طاهری از پرسپولیس به تیم ملی امید دعوت شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/135229" target="_blank">📅 22:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135228">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
❌
قدوسی: مذاکرات با احمد نوراللهی در حال انجام است و مدیران باشگاه در تلاش هستند این بازیکن رو به پرسپولیس برگردونن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/135228" target="_blank">📅 22:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135227">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YI11M32-KDh_ftYoxyqMO7jkB15E4f2dWiiVq05zGVGerV_tntADbTyi7_caM2Vc07idRIL6eNIi1OtM8h5pJNaawY5Fer6iD8yjL8zX57T_yqzl1AAaxZFCxlOSvqkwShHa0q_oj6vSmzgYceAC-3FeUQzVnZjf9fiHGoabZLdcbTI736LIVzAxATpXS2n1B9RsetH2cghrmfx3Xe55LVjqircGfXXcdFHN3omaiQjOjwdkyG5rPIYK1Ne_1HQ9d2sA_Utf6a-XfQNKYVzQXvdAXHOLJfXoVv5ZHC9fcJcHuB13UBdyCYtIFQtPjWCg8Ln2IUwrPqGmfaU3JoIRMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
استوری یکی از بچه های گرافیک کار باشگاه
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/135227" target="_blank">📅 22:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135226">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
فووووووووووووری
🔹
قدوسی: باشگاه با احمد نوراللهی تماس گرفته و ازش خواسته برگرده!!!
🔹
پ.ن احمد نوراللهی در تمرینات پیش فصل اتحاد الکبا شرکت نکرده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/135226" target="_blank">📅 22:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135225">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
❌
محسن خلیلی: هر مربی ای باید افتخار کنه که سرمربی پرسپولیس بشه، اسکوچیچ نشون داد که چنین لیاقتی نداره.
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/135225" target="_blank">📅 22:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135224">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UL88Z_PBbQRGGcr4QOpaHCkecPD4DLhmuBwrjffsTI7pOBjPfLvh83iEqTUSZx-nGux4Ol5l16vZNG4Kfz0AJCV_bcvvwRpqk0o4yR9f0YdyCLyPAeMOFVdLvIq5IXNtKkDcgMFDxcsg4ujjPg_UP2apN1gJuSE7A3EDtcoyI53VXuf-nSoAFjUEaRhYZj1ajW38_dLTSiHSbu4j9TIZJ42umAB3rs7GEe99N8jUkMItgWXXFiynCEWvkzB-OQtTZoPZrkcgy89oF0zh3DNRkZcD4b8qi5TmuKp18I1bE-ep04Prvu81c75_jW9d3emZe0dnK2pQgKpMvWNN5hR3Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
واکنش مدیر رسانه ای پرسپولیس به یک شایعه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/135224" target="_blank">📅 21:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135223">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4b1NMpvTaAjyGSISkPu7Rm1WaVaZwyIDDV13bXsfOGLXvBx6SxiUiSZDl_CyScC10GLW9HdmZQko-5hpfi9ccWwq5mGEz2neQRdQnG58x2fc-gRqhVq9whnKgvkeA5LckZAdDOC2Xeb7-rHG7lLyWBu9fEwEe-sfRe43dTEq3cXTkf2uhYMDJel_3-M85G-LyBNp55yh_vpiIXQ5BtWsoaQHlFBH2apUFJ015lpEzcFyaA_rgv-Qb4GX3dOpOx4ldude57S2v_gWSCdfWBmMQOgFhPQpNwjgtfJfsfdi8jLu6q5U7Dk_mlYCXsThRQZ7nbEiRLurExh67Rz0Rz3eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اشک‌های زیبای سلطان که در جام موند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/135223" target="_blank">📅 21:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135222">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
🔴
وااای آرژانتین تو ده دقیقه جبران کرد و بازی کرد دو بر دو و فعلا مسی موندگار شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/135222" target="_blank">📅 21:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135221">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❗️
چه فوتبالی شده ی گل و جبران کرد آرژانتین و بازی شده دو بر یک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/135221" target="_blank">📅 21:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135220">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✅
برگام ...مصر گل دوم و زد و مسی هم مثل رونالدو بدون جام خداحافظی می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/135220" target="_blank">📅 21:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135219">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✅
خداحافظ مسی .خداحافظ رونالدو ...دو تیم گروه ایران رفتن جزو هشت تیم نهایی   پ.ن با این نتایج انگلیس تا فینال راحت میاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/135219" target="_blank">📅 21:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135218">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✅
برگام ...مصر گل دوم و زد و مسی هم مثل رونالدو بدون جام خداحافظی می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/135218" target="_blank">📅 21:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135217">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❗️
خدا کنه مصر نیاد بالا .وگرنه قلعه نوعی بیچارمون می‌کنه ‌..میگه دیدین با دو تیمی مساوی کردیم که هر دو تیم اومدن تو 8 تا تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/135217" target="_blank">📅 21:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135216">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
❌
اوه اوه مصر گل اول و زد ...آیا بعد از رونالدو مسی هم امشب هم خداحافظی می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/135216" target="_blank">📅 20:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135215">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
و همچنان مصر نمیخوره و داره آرژانتین و حذف می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/135215" target="_blank">📅 20:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135214">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
❌
اوه اوه مصر گل اول و زد ...آیا بعد از رونالدو مسی هم امشب هم خداحافظی می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/135214" target="_blank">📅 20:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135213">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❗️
ورزش سه :تارتار لیست مازادش را به باشگاه تحویل داد
❌
امید عالیشاه
❌
سروش رفیعی
❌
مرتضی پورعلی‌گنجی
❌
میلاد سرلک
✅
✅
مدیران باشگاه این تصمیم را به بازیکنان اطلاع داده‌اند و این چهار نفر اجازه حضور در تمرینات را ندارند.
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/135213" target="_blank">📅 20:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135212">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✅
✅
ورزش سه: باشگاه نساجی مازندران تا کنون برای جذب سه بازیکن جوان 115 میلیارد تومن هزینه کرده است!!!!!!   پ.ن امروز دانیال ایری با 70 میلیارد به نساجی پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/135212" target="_blank">📅 20:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135211">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
فووووووووووووری
🔴
🔴
ایجنت میلاد محمدی دقایقی پیش با حضور در باشگاه پرسپولیس قرارداد این بازیکن را به مدت دو فصل دیگر تمدید کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/135211" target="_blank">📅 20:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135210">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join
Join Join Join</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/135210" target="_blank">📅 20:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135209">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmZSAwIab5lgd76dPYESp58NHKh3SeW4xqXpJ1MwJ5IbUyker2ZuYt39pNmx1QE7N_AJVNTdtdE6B3AEnHQHZ-9r3lYvcA_gBgtoxzUVmoAqwaxFkmPz5pRB7wIvg_xYqjEsVbyQC2CGoE2Kn_tqChp9JV-r2GPQN1ONxIyJO_0cbtWz6kP5s0NLtAaDMRo-Hh4XxtRdub2GZAUnD4ln530eHSZpjMHsF9_wEYasH7SMEitIcCTA8A5xSQiNI5tC8Glbnl4cY-f5GK3sDD5TS0J112Hkhw81kwlGM6FM19W8Qgmtuuq7S03RRIZHQQkp14MuqrbAqrxAQf4MTEj6gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکس عالی برد شد
❤️
☑️
✔️
@HaJFixed</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/135209" target="_blank">📅 20:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135208">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
❌
تسنیم : میلاد محمدی و پرسپولیس برای تمدید قرارداد به مدت ۲ سال به توافق رسیدن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/135208" target="_blank">📅 20:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135207">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✔️
#تایید_خبراختصاصی | #اولین_رسانه
🏅
مجید عیدی با عقد قراردادی دو ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/135207" target="_blank">📅 20:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135206">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pybCZ5XKTyNJ2i97IK6PchleqxU_onV9rjoAK0I15UyBu6_4ukWDxiak1YYVXPN4VXiEBhkohjCOVvQ68714tWfFn6ozvXXKk2zaixSpOaxuGsc6vUdqAQf8SOUPxJ8JhVFT4iaDEVJ38IZmWYQRXmzid6l8MzC76u5U7h8ZLo7DlqfiVmkdF1W-DWiIcnSdKi28y9vEiK6nF3--L8rGAPxpDWdZWU-mG3UlT-H5ByreF4AoklwIHNqv3R_b2VJcch0FGVYbMkEmpdEVikwsVgpoYXPC35Hx3t3p5PSC9CxknI0R1bj8nG10tqUHMrQxeqaZ-TyDP1lBN916DVUxJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⌛️
پوریا شهرآبادی در آستانه پیوستن به پرسپولیس قرار دارد و در صورت نهایی شدن مذاکرات، به جمع شاگردان مهدی تارتار اضافه خواهد شد.
💬
خبرگزاری فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/135206" target="_blank">📅 20:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135205">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✅
✅
بازی آرژانتین و مصر ساعت 19/30 شروع میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/135205" target="_blank">📅 19:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135204">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✅
نمودار درختی دور یک چهارم؛
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/135204" target="_blank">📅 19:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135203">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
🔴
خبرگزاری فارس مدعی شده محسن خلیلی میخواد احسان محروقی مهاجم فولاد رو بجای علیپور بیاره پرسپولیس‌
😐
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/135203" target="_blank">📅 19:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135202">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❗️
فووووووووووووری
🚨
قدوسی: حضور علی نعمتی در پرسپولیس احتمالا منتفی است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/135202" target="_blank">📅 18:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135201">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❗️
فووووووووووووری
🚨
قدوسی: حضور علی نعمتی در پرسپولیس احتمالا منتفی است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/135201" target="_blank">📅 18:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135200">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✅
✅
امید عالیشاه برای رفتن از پرسپولیس تمام قرارداد 80 میلیاردی فصل آینده خود را طلب کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/135200" target="_blank">📅 18:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135199">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
فووووووووری از فوتبالی: ابوالفضل جلالی فردا ظهر جهت امضای قرارداد به باشگاه پرسپولیس خواهد رفت و قرارداد دوساله با پرسپولیس امضا خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/135199" target="_blank">📅 18:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135198">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❗️
پیشنهاد مالی بالایی به پرسپولیس داده، اینکه میگن پیشنهاد خارجی داره دروغه و فعلا باشگاهی خارج از ایران نمیخوادش//تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/135198" target="_blank">📅 18:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135197">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
❌
شنیده ها :سیدابوالفضل جلالی دقایقی قبل‌ازطریق مدیربرنامه‌هایش به پیمان‌ حدادی مدیرعامل پرسپولیس خبرداده که فردا صبح برای عقد قرارداد وارد ساختمان باشگاه خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/135197" target="_blank">📅 17:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135196">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
بخش‌رسانه‌ای‌باشگاه پرسپولیس طی ساعات آینده پوستر رونمایی‌از کسری‌طاهری خرید جدید این باشگاه را منتشر میکنه. قرارداد طاهری با پرسپولیس قرصی با بند خرید 1.2 میلیون دلاری خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/135196" target="_blank">📅 17:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135195">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">#تلنگر
⛔️
اوسمار زنا زا… رو رد کردید ایجنت کصکشش رو گذاشتید تیم ببنده ؟! دوتا رونمایی داشتید جفتش بازیکن های این جا
…
بودن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/135195" target="_blank">📅 17:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135194">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❗️
❗️
پیگیری کردم؛ میلاد محمدی هم به توافق قطعی با پرسپولیس رسید و طی ۲۴ ساعت آینده امضا می‌کنه.///خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/135194" target="_blank">📅 17:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135193">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
❌
تسنیم : میلاد محمدی و پرسپولیس برای تمدید قرارداد به مدت ۲ سال به توافق رسیدن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/135193" target="_blank">📅 17:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135192">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❗️
❗️
ابوالفضل جلالی با پرسپولیس به توافق نهایی رسیده و فقط یک امضا تا پرسپولیسی شدن ابوافضل جلالی باقی مونده.
🔴
سپهر خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/135192" target="_blank">📅 16:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135191">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❗️
❗️
ابوالفضل جلالی با پرسپولیس به توافق نهایی رسیده و فقط یک امضا تا پرسپولیسی شدن ابوافضل جلالی باقی مونده.
🔴
سپهر خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/135191" target="_blank">📅 16:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135190">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❗️
❗️
واکنش مدیرعامل نساجی به خبر پرسپولیسی شدن دانیال ایری: «ما چهارشنبه جلسه‌ای را مدیران پرسپولیس برگزار می‌کنیم اما با توجه به اینکه سیاست اصلی نساجی موفقیت در لیگ برتر است، ترجیح بر این داده می‌شود که رضایتنامه ایری صادر نشود و او در تیم باقی بماند.»
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/135190" target="_blank">📅 16:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135189">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✅
✅
ابوالفضل جلالی و میلاد محمدی سمت چپ
❗️
مهدی تیکدری و مجید عیدی سمت راست
✔️
پ.ن دو چپ و راست خوب داریم
🙂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/135189" target="_blank">📅 16:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135188">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
فوری؛ باشگاه پرسپولیس پس از کنسل شدن جذب ابوالفضل رزاق پور، با ابوالفضل جلالی، مدافع چپ استقلال به توافق رسید و او سرخپوش خواهد شد. /تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/135188" target="_blank">📅 16:08 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
