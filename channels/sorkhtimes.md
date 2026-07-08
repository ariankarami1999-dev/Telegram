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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 19:55:01</div>
<hr>

<div class="tg-post" id="msg-135295">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❌
یه هوادار تو دایرکت نوشته: امروز دم باشگاه بودم آقای خلیلی گفتن نه نوراللهی میاد نه محمد قربانی رضایت نامه هرکدوم دو میلیون و پانصد هزاره//قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/SorkhTimes/135295" target="_blank">📅 19:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135294">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
باشگاه به خاطر فشار هوادارا فعلا پورعلی رو تو آب نمک خوابونده تا نتیجه مذاکرات با قربانی و نوراللهی رو پیگیری کنه و اگه اونا جذب نشن پورعلی رو نهایی می‌کنه/ فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SorkhTimes/135294" target="_blank">📅 18:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135293">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❗️
❗️
شنیده ها : فوری؛ پیغام‌جدید محمد قربانی به پیمان‌حدادی مدیرعامل باشگاه پرسپولیس: پیشنهاد مالی شما رو پذیرفته‌ام، رضایت نامه ام رو بگیرید روز شنبه قراردادم رو امضا خواهد کرد.
❌
❌
پیشنهادمالی‌پرسپولیس: سه ساله بوده. سال اول 80، سال دوم 110 و سال سوم 150 میلیارد…</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SorkhTimes/135293" target="_blank">📅 18:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135292">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
#شایعات
🔴
علیرضا کوشکی در حال مذاکره با پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SorkhTimes/135292" target="_blank">📅 18:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135291">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
تصاویری از حضور بازیکنان تیم پرسپولیس برای انجام نخستین تمرین برای شروع فصل جدید که چهره ها نشون از روحیه و شادابی بچه ها داره با کادر جدید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SorkhTimes/135291" target="_blank">📅 18:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135290">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❗️
شهرابادی، طاهری، پورعلی و جلالی پوستر رونماییشون آمادست و فقط منتظر تأیید حدادی هستن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SorkhTimes/135290" target="_blank">📅 18:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135289">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4FqI4P8A2kUIZQAodQgxiozEe4b61OMPH_ms7N1qETem3dEua3KnEH34ZG4HWhb-8sBbSwDnzc98vi7vMAhsorengTcQE6BZZyNxe4Oh2FWjGwknLlx6QoRr6-41KcMLG8kgLUOx5T50nLLjnF5n3awByNcNiPJuQSpOufGMXTOI4FRQMHdnx-kT_DySkgHbduB5EPWaj0zLEKlf4gF6rztm76wUnpN2jOEBjOtIbballwoLsMY-BdE6PjD1t7SQ-sZTXcVRIbgUd22Vhlf-I0JlAkY30DMLZ5HYnRkU-ktE3fHbSjn6frMUXp9eZGsWjN2ZFZp7-aeeWon89wkqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصاویری از حضور بازیکنان تیم پرسپولیس برای انجام نخستین تمرین برای شروع فصل جدید
که چهره ها نشون از روحیه و شادابی بچه ها داره با کادر جدید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SorkhTimes/135289" target="_blank">📅 18:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135288">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
احتمالا باشگاه برای رونمایی لایو داره  وگرنه چه‌ اصراریه که تاخیر داشته باشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SorkhTimes/135288" target="_blank">📅 17:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135287">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/135287" target="_blank">📅 17:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135286">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✅
🇺🇸
ترامپ:
❗️
دیشب جزیره خارک رو زدیم ولی به نیروهامون گفتم نفت‌ش رو نزنید ممکنه بخوایم جزیره رو تصرف کنیم چون از دستشون کاری برنمیاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/135286" target="_blank">📅 17:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135285">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
باشگاه به خاطر فشار هوادارا فعلا پورعلی رو تو آب نمک خوابونده تا نتیجه مذاکرات با قربانی و نوراللهی رو پیگیری کنه و اگه اونا جذب نشن پورعلی رو نهایی می‌کنه/ فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/135285" target="_blank">📅 17:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135284">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/135284" target="_blank">📅 17:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135283">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/135283" target="_blank">📅 17:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135282">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❗️
ترامپ: حملات امشب به ایران ممکنه خیلی بزرگ باشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/135282" target="_blank">📅 17:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135281">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❗️
❗️
#فوووووری از ترامپ: آتش‌بس با ایران به پایان رسید و از این لحظه هر دستوری بخواهم برای زدن ضربه نهایی خواهم داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/135281" target="_blank">📅 17:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135280">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✅
مطابق اعلام سایت ترانسفر مارکت؛ تا به این لحظه مهدی ترابی و مهدی هاشم نژاد قراردادی برای فصل آینده با باشگاه تراکتور ندارند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/135280" target="_blank">📅 16:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135279">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✅
🚨
🚨
⭕️
بازگشت خانبان به پرسپولیس: به‌زودی....!
⭕️
بر اساس شنیده ها، مدیران ارشد باشگاه پرسپولیس با توصیه خداداد عزیزی به دنبال بازگرداندن مهرداد خانبان آنالیزور سابق پرسپولیس به کادرفنی پرسپولیس است
🔸
آنطور که از باشگاه پرسپولیس خبر می‌رسد احتمالا باید برای…</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/135279" target="_blank">📅 16:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135278">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
💙
ابولفضل جلالی با قراردادی دو ساله رسما به پرسپولیس پیوست.
❓
نظرتون درباره جلالی چیه ؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/135278" target="_blank">📅 15:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135277">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
💙
ابولفضل جلالی با قراردادی دو ساله رسما به پرسپولیس پیوست.
❓
نظرتون درباره جلالی چیه ؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/135277" target="_blank">📅 15:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135276">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
❌
البته این خبر هنوز رسمی اعلام نشده و یکی از ادمین های ما در نشر آن عجله کرده. جلالی گفته امروز، فردا با رسانه باشگاه مصاحبه می کند که پالسی است به نشانه امضای قرارداد‌. این مدافع چپ جوان به تازگی تمام پست هایش با پیراهن استقلال را در اینستاگرامش پاک کرد.…</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/135276" target="_blank">📅 15:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135275">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
💙
ابولفضل جلالی با قراردادی دو ساله رسما به پرسپولیس پیوست.
❓
نظرتون درباره جلالی چیه ؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/135275" target="_blank">📅 14:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135274">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❗️
با تایید سهیل صحرایی این بازیکن به عنوان بخشی از مبلغ رضایت نامه گلگهر برای شهرآبادی، از پرسپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/135274" target="_blank">📅 14:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135273">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❗️
شنیده ها :گل‌گهر برای شهرآبادی 120 تا میخواسته
❌
ولی گویا صحرایی + 80 میلیارد توافق کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/135273" target="_blank">📅 14:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135272">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/295a60cd54.mp4?token=hQjuUAr_9RxGvI2UF8j19bUuwyt_dAsJrv29cisnjJ_TCCfr99cXn49_pd8DahW9HSFWZY_dsAsSmoMCDdXUES3BBYG66B_mKMXMej6L3zH_jrSw-lEwDSz15kxNBs52-18Nhmsgt3JWecHbYFI3XLFL8HPhg135CGoSIePw1gdTRAG7lwVXmU8QF_FBMWjztrT1zE4b2ZTDXuwXkWf677fiu406ZmxbfZ1KVW1gFDqQkPhNGBlgYC2TjKCRqxzo0uSBV5rihnw-7Wuv0ZZMs5v3MqlcSbdVTpofIz5D6rW_i6TAtxFaPSCRKxuDl17zkwlENeHQ1lx1b6r9q3ELxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/295a60cd54.mp4?token=hQjuUAr_9RxGvI2UF8j19bUuwyt_dAsJrv29cisnjJ_TCCfr99cXn49_pd8DahW9HSFWZY_dsAsSmoMCDdXUES3BBYG66B_mKMXMej6L3zH_jrSw-lEwDSz15kxNBs52-18Nhmsgt3JWecHbYFI3XLFL8HPhg135CGoSIePw1gdTRAG7lwVXmU8QF_FBMWjztrT1zE4b2ZTDXuwXkWf677fiu406ZmxbfZ1KVW1gFDqQkPhNGBlgYC2TjKCRqxzo0uSBV5rihnw-7Wuv0ZZMs5v3MqlcSbdVTpofIz5D6rW_i6TAtxFaPSCRKxuDl17zkwlENeHQ1lx1b6r9q3ELxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سهیل صحرایی هم وارد دفتر باشگاه شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/135272" target="_blank">📅 14:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135271">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/135271" target="_blank">📅 14:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135270">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/135270" target="_blank">📅 14:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135269">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vK8n18JE6pSKtxIIXt6OtnYqWHOLMZs92MQacX01XUKeokiUpgN0nW6BGsLwbtDdD2CsxFM7z7EeSxqJzYE94QBmyOgKSDhBHOl30WQ2TJ2n4py5cSwR_D7_PC_rEuOlXOdzwPGnAqIFWa406S9KKlvBZsPIZq5YGTsIX_ujmcs5OFOcE0lk0MeWCx6qVsbmX6WpsFABJMGMR_HKI_EbFc9e0yj2ermxdcgw2C0ADNGlL8XKWCn_HD-0CVdEXDRNJT3ocvPswDldqVUVZj5kqLcq1Q8__hUrEyNCtd0TcOM-IHZN8RlWl2UsoxGExaDc-jTpXHkgE-RQxYTyy11IeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/135269" target="_blank">📅 14:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135268">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c56bb19ad7.mp4?token=cJ-NSP-JHBCJKtnHczGwURAfSNy552MyjRZuU7p2RnGDQsK3QbLxvRRoeigVA7CGXRJA4k8rH_aV3Av399YXdgBAArXLIfXJZdvL1Fk6FurAg7hIilJQarN2x2OWSMB3hAItq3maL4Ypo4PN_0rwgCoK5OTMZ5bxfMTAxxf7V2PBVu6-YPUKLg8I46-TU-vhd7Z9pEfUDcS8EthbNYSszLg-cOwWJCwQ2bt_oOkvopTMvC4dErdL-Zn_bp-t79dgGTRRFErv-uvWRkdS7ug6KiX291RLxVSmJwu9MHGtpMXQfL_1SOUkb7db2ZX39dX0z0CjrgkhEQPvReBzNF365w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c56bb19ad7.mp4?token=cJ-NSP-JHBCJKtnHczGwURAfSNy552MyjRZuU7p2RnGDQsK3QbLxvRRoeigVA7CGXRJA4k8rH_aV3Av399YXdgBAArXLIfXJZdvL1Fk6FurAg7hIilJQarN2x2OWSMB3hAItq3maL4Ypo4PN_0rwgCoK5OTMZ5bxfMTAxxf7V2PBVu6-YPUKLg8I46-TU-vhd7Z9pEfUDcS8EthbNYSszLg-cOwWJCwQ2bt_oOkvopTMvC4dErdL-Zn_bp-t79dgGTRRFErv-uvWRkdS7ug6KiX291RLxVSmJwu9MHGtpMXQfL_1SOUkb7db2ZX39dX0z0CjrgkhEQPvReBzNF365w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/135268" target="_blank">📅 14:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135267">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e4a201f71.mp4?token=FPRYIOVz34A6BuBknXtD5fvzh6XF-GHPI8WPsHg8eEpk-ZqZL3arkxdM5OTiyoHXg4ZRx8kFpV8X-Eyih9SDFj8qIlH-oSoug4NJC_bcko3OUNJCkIPWFiqMSrshxVzb2c1qIgbGbWSPCA6yUdK0jvL3Wunm_iW9_4L0r3a0dv4qtZOubNxlN7thIMdgpxoRm2CYJ3eQjMl2uieFCyBUWjn0upBAjnJcd_tQbgy3212kAiTu_vrOL2mRB8tRf53o99hnDTrLeCmEG9kFGAWtGrKu5JrhYOWHKydWLjSrqkYfu7nG_a5PmR-LMdRhQgp3ER8cOrwJTtyBydEGlCqKFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e4a201f71.mp4?token=FPRYIOVz34A6BuBknXtD5fvzh6XF-GHPI8WPsHg8eEpk-ZqZL3arkxdM5OTiyoHXg4ZRx8kFpV8X-Eyih9SDFj8qIlH-oSoug4NJC_bcko3OUNJCkIPWFiqMSrshxVzb2c1qIgbGbWSPCA6yUdK0jvL3Wunm_iW9_4L0r3a0dv4qtZOubNxlN7thIMdgpxoRm2CYJ3eQjMl2uieFCyBUWjn0upBAjnJcd_tQbgy3212kAiTu_vrOL2mRB8tRf53o99hnDTrLeCmEG9kFGAWtGrKu5JrhYOWHKydWLjSrqkYfu7nG_a5PmR-LMdRhQgp3ER8cOrwJTtyBydEGlCqKFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🏅
جلالی هم اومد بیرون… به خبرنگار ها گفته با رسانه باشگاه مصاحبه کردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/135267" target="_blank">📅 14:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135266">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24a7269d75.mp4?token=oiYc2jGP6CQM5GE5pa6Oskw0EM_GsPITAJMRrznKfwwm9HQA0FLQFdWQU1sOVwR6Wf76Lb45ZG5r3SGBZQCZx7G_xR5mnURHmvAXfCGsn6FxNupkWE5fFmMIPga_ldbRGIp1AaNYrVk4UIB5CC0BZKvlkhFUEW8_ZFjvcwpgv7Oc_SibgH-dknhWSz8p5QzTT01NlTD3xGRx_Uy7-Spkp2p49FKDsx6UyGgpjwq3GkBBHh5wl6UoqXiCLdNVVk4XACJEAl6hnDVOszw_w1xdTIYnb2K3A4BmGUJDU4xTECeILiSkqHqCS76435jR2Z9jqBAu1sng_SCa3Bb91YqEZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24a7269d75.mp4?token=oiYc2jGP6CQM5GE5pa6Oskw0EM_GsPITAJMRrznKfwwm9HQA0FLQFdWQU1sOVwR6Wf76Lb45ZG5r3SGBZQCZx7G_xR5mnURHmvAXfCGsn6FxNupkWE5fFmMIPga_ldbRGIp1AaNYrVk4UIB5CC0BZKvlkhFUEW8_ZFjvcwpgv7Oc_SibgH-dknhWSz8p5QzTT01NlTD3xGRx_Uy7-Spkp2p49FKDsx6UyGgpjwq3GkBBHh5wl6UoqXiCLdNVVk4XACJEAl6hnDVOszw_w1xdTIYnb2K3A4BmGUJDU4xTECeILiSkqHqCS76435jR2Z9jqBAu1sng_SCa3Bb91YqEZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
محسن خلیلی برای عکس یادگاری با خرید های جدید وارد باشگاه شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/135266" target="_blank">📅 13:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135265">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6Vi7gA-LiUTspwdhP80DOvQWw83W6GACS3aO5etw0J81seMlNr1C_wcuXOmeO4BkwPh-lwLke2WqU921etVLsTiPzkpcsfeRXGK4UtFMVmq6qKF19VCpSotkcI_Gd5zOuA_zq6uTOBDUTOqsZVR9HSNffdYHVAjJicM229RVXolo4D7jItBTsKpB-LUJd_-zO46U-Jawjb4z_OdvyLNfLRV1JR3kMS7U9jP4mP7I3l_1oh9DisiZF7EijyhfyMHVKG7PperIG6cU4u5hqFB-mlHyAOrwlR75n-LmZCwrqDOXWUIXxWYIWhx-11tnUZYq3Dxu6BCMUgowFQdGFc5Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
نظرتون در مورد ابوالفضل جلالی؟؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/135265" target="_blank">📅 13:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135264">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86ba7ad723.mp4?token=hJ1pY8tsk04i1eOYFSs1s0mKqSybPxcP3MjmuyzFnU6z2yd_1IQvgXWo-XfLaYCmUc6QcqUNkE2SHoJccWXM-Wg7VkOZrdh5RcZ1eB_BjFI3lkUB28ImJymE_vNKwsnv0rkJ-P6tAUwrCv5qSmXvC7vFIsq4L2QytcEzeiidSR1Jjl8fYK89bz7Lr2DmnrdbPQyn8L3rFT6pvU8yCxVXoOKiG3mImDin1-1G0T2XuH6KN4Gt33BmKLo_BwMMu37E2eGjPndBDhKEPGgf6mWLFLjf5h4WOYkOKNfCoK0Ek_Qn7wQgjcbnL-MAsWHMxpQyRyM7yMT266vVlHc8DYJeuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86ba7ad723.mp4?token=hJ1pY8tsk04i1eOYFSs1s0mKqSybPxcP3MjmuyzFnU6z2yd_1IQvgXWo-XfLaYCmUc6QcqUNkE2SHoJccWXM-Wg7VkOZrdh5RcZ1eB_BjFI3lkUB28ImJymE_vNKwsnv0rkJ-P6tAUwrCv5qSmXvC7vFIsq4L2QytcEzeiidSR1Jjl8fYK89bz7Lr2DmnrdbPQyn8L3rFT6pvU8yCxVXoOKiG3mImDin1-1G0T2XuH6KN4Gt33BmKLo_BwMMu37E2eGjPndBDhKEPGgf6mWLFLjf5h4WOYkOKNfCoK0Ek_Qn7wQgjcbnL-MAsWHMxpQyRyM7yMT266vVlHc8DYJeuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
گل پوریا شهرآبادی به استقلال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/135264" target="_blank">📅 13:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135263">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
پوریا شهرآبادی برای عقد قرارداد وارد ساختمان باشگاه پرسپولیس شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/135263" target="_blank">📅 13:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135262">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/838edcfe33.mp4?token=QOLSJV0qFGY5Csmycd7ydWb3V36fBzR7H7awfLIcQPkqHdsNCUre4bKjVPFo_O8RvaizfYqN5DIZCkHiYzTtDZ0-NaA223xqhsMmbeZd2KKu5ZTIpZVKf-o7DhryNDp8MMy6rBp8nd67WRhLm9XKEafdydazKYtSkHVkg1wKCGMghvkfHCXY0cm8i2wIziuSF-8i9OUwwvZgY7634yQtdarKeI_J3nCJPgKbsTrB7aupBj7RdDozPD6LQUbvV6MAFZlR3GqP-KNGNYgHWHzgS4IlxUw3cFfXrifABQKk5uwfdUzd1C3AJYLi2z1VlZ-SlwE7U9xu-oDSwxxR655EYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/838edcfe33.mp4?token=QOLSJV0qFGY5Csmycd7ydWb3V36fBzR7H7awfLIcQPkqHdsNCUre4bKjVPFo_O8RvaizfYqN5DIZCkHiYzTtDZ0-NaA223xqhsMmbeZd2KKu5ZTIpZVKf-o7DhryNDp8MMy6rBp8nd67WRhLm9XKEafdydazKYtSkHVkg1wKCGMghvkfHCXY0cm8i2wIziuSF-8i9OUwwvZgY7634yQtdarKeI_J3nCJPgKbsTrB7aupBj7RdDozPD6LQUbvV6MAFZlR3GqP-KNGNYgHWHzgS4IlxUw3cFfXrifABQKk5uwfdUzd1C3AJYLi2z1VlZ-SlwE7U9xu-oDSwxxR655EYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پوریا شهرآبادی برای عقد قرارداد وارد ساختمان باشگاه پرسپولیس شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/135262" target="_blank">📅 13:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135261">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔹
فوری؛ابوالفضل‌جلالی مدافع‌سابق استقلال برای عقد قرارداد با باشگاه پرسپولیس وارد ساختمان این باشگاه شد. قرارداد 2+1 ساله توافق شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/135261" target="_blank">📅 13:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135260">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
فرزین معامله گری خرید چهل میلیاردی خلیلی به خاطر تمدید محمدی و خرید جلالی در لیست مازاد تارتار قرار گرفت/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/135260" target="_blank">📅 13:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135258">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
ترامپ: ایران دروغگوعه و من از امروز به بعد دیگه نمی‌خوام هیچ ارتباطی باهاشون داشته باشم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/135258" target="_blank">📅 12:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135257">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
فوری/ ترامپ: به نظر من، توافق‌نامه با ایران به پایان رسیده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/135257" target="_blank">📅 12:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135256">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❗️
فیفا به درخواست ترامپ، کارت قرمزی که مهاجم آمریکا، داخل بازی قبل گرفته بود رو بخشید تا محرومیت بازیکن تو بازی بعد جام جهانی رفع بشه!!
❗️
پ.ن سیاست آوردن تو فوتبال و ترس از آمریکا و ترامپ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/135256" target="_blank">📅 12:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135255">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✅
اگر پرسپولیس همزمان مهدی زارع و مسعود محبی را جذب کند، پرونده انتقال علی نعمتی به‌طور کامل بسته خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/135255" target="_blank">📅 11:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135254">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
❌
هوشنگ‌ سعادتی به مدیر پرسپولیس قول داده امروز جلالی رو ببره ساختمان باشگاه پرسپولیس برای عقد قرارداد؛ اگه باشگاه استقلال تا ساعات آینده با جلالی برای تمدید تماس نگیره امروز ازیاغی جدید فوتبال ایران رونمایی خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/135254" target="_blank">📅 11:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135253">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✅
مصاحبه‌جدید دراگان‌اسکوچیچ: هرگز برای یک فصل حضور در پرسپولیس 3 میلیون دلار تقاضا نکرده بودم.
🔴
بایک‌ باشگاه‌ بزرگ در حال مذاکره هستم و ممکنه برای‌فصل‌جدید مجدد به لیگ برتر برگردم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/135253" target="_blank">📅 10:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135252">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
یاگو به عنوان مربی بدنساز فصل آینده پرسپولیس انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/135252" target="_blank">📅 10:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135251">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
❌
شوک بزرگ به استقلال؛ سایت آفریقایی Africafoot مراکش نوشت که مونیر الحدادی ستاره استقلال با باشگاه الاتحاد مراکش توافق کرده...
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/135251" target="_blank">📅 10:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135250">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">⚡️
⚡️
آسانی و منیر حدادی در آستانه ترک ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/135250" target="_blank">📅 10:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135249">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
برای تمرین امروز چهارشنبه به بازیکنان  پرسپولیس اطلاع‌رسانی شده و در این بین به ۳ بازیکن دارای قرارداد، گفته شده که تا مشخص شدن وضعیت‌شان، در تمرین شرکت نکنند.
✅
امید عالیشاه، مرتضی پورعلی گنجی و میلاد سرلک این سه بازیکن هستند.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/135249" target="_blank">📅 10:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135248">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❗️
امروز پرسپولیس روز شلوغی خواهد داشت...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/135248" target="_blank">📅 10:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135247">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❗️
اسکوچیچ: با پرسپولیس توافق کردم انواع و افسام انعطاف پذیری ها رو داشتم اما در آخر قراردادی که برای من فرستادن مبلغش خیلی کمتر از اون چیزی بود که توافق کرده بودیم و من از این موضوع بسیار ناراحت شدم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/135247" target="_blank">📅 09:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135246">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✅
❗️
باشگاه پرسپولیس خطاب به ابوالفضل جلالی: اگه قصدت بازار گرمی نیست بیا قرارداد باهات ببندیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/135246" target="_blank">📅 09:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135245">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❗️
فووووووووووووری
🚨
قدوسی: حضور علی نعمتی در پرسپولیس احتمالا منتفی است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/135245" target="_blank">📅 09:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135244">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
برای تمرین امروز چهارشنبه به بازیکنان  پرسپولیس اطلاع‌رسانی شده و در این بین به ۳ بازیکن دارای قرارداد، گفته شده که تا مشخص شدن وضعیت‌شان، در تمرین شرکت نکنند.
✅
امید عالیشاه، مرتضی پورعلی گنجی و میلاد سرلک این سه بازیکن هستند.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/135244" target="_blank">📅 09:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135243">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJ4WSyaGpO6IJQEjNOEEXVuQrcibdBDPQSpBKxMWM1sewu4qL06MfzEsY2NKu8BwBjR2suCXoyDWndrhnWwFazkwlbD41RhRVyzHcdA5L5VKUdgbRQZFsib2m6F5-8SyXUidRtrCoF957SHvuLkolkMoST8rooVSEpw1pYkccun3wfPUg4E2Fp0Pb3maZi8OVxk_5wHo5eZAQVsLWJxk3SMbxTltAGHR2qqsylGRzAD8EI5sF9ZTV4-D3gWQJ0k8TSREgiXdNDW2arqRv0LejoMD4Kqd7VBu73Zyzp8R1Ao3aS2KdDW5d7PsrltdqOAaKuq4v9hz1HjrF_ytCRQrrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
برای تمرین امروز چهارشنبه به بازیکنان  پرسپولیس اطلاع‌رسانی شده و در این بین به ۳ بازیکن دارای قرارداد، گفته شده که تا مشخص شدن وضعیت‌شان، در تمرین شرکت نکنند
.
✅
امید عالیشاه، مرتضی پورعلی گنجی و میلاد سرلک این سه بازیکن هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/135243" target="_blank">📅 09:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135242">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✅
نمودار درختی دور یک چهارم؛
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/135242" target="_blank">📅 09:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135241">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/135241" target="_blank">📅 01:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135240">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SoWD1BBZzN3xsbl92-jeie5iL0oAWbkvH1hs-uDFewHqrMVs6TceD9bpXwowDbKpaLteZn26GGy9yCP1byTv1x9cal4okkyrPewCJ3A695MyJPWbd_z8hLTo0qcUf1e6t4s7D59avbOK_4uVcMXs7q5NnWZhBwEcTZN7-CPFM_Ci3n2J9fuDAKNY-67kAPZ1O1rKHcm_dGHHkAGKliEMduMjTftCBsMQax8AFwApIWtLf_3vNFCNaPMIfkSoWxuDueRfZ1FZxBtYPiJmtD6PQBWY5DDSHwHlYI3Y0FouZpEiejngdUDjjbpUJB3jNwTi01a-_y4BujeEgVRgKHYj3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/135240" target="_blank">📅 01:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135239">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❗️
فوووووووری/سنتکام: در پاسخ هم حملات ایران به کشتی‌های تجاری و نقض آتش بس، مناطقی در جنوب ایران را بمباران کردیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/135239" target="_blank">📅 01:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135238">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✅
✅
فوووووری؛ آغاز عملیات شبانه ارتش آمریکا در جزایر جنوبی ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/135238" target="_blank">📅 00:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135237">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❗️
❗️
فوووووووری/ارتش آمریکا در پاسخ به نقض آتش بس از سوی ایران، اهدافی را در جنوب ایران هدف قرار داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/135237" target="_blank">📅 00:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135236">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
❌
حسام حسن، سرمربی تیم ملی مصر پس از حذف در بازی با آرژانتین با ادبیاتی تند گفت:
🎙
هر عواقبی را می‌پذیرم اما می‌گویم که این مسابقه کاملاً مهندسی و تبانی‌شده بود و همه دنیا این را دیدند. اگر تا این حد اصرار دارند که آرژانتین قهرمان شود، چرا از بقیه تیم‌ها…</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/135236" target="_blank">📅 00:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135235">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
🔴
به امید عالیشاه، میلاد سرلک و مرتضی پورعلی‌گنجی اعلام شده در تمرینات حاضر نشوند و در لیست مازاد قرار گرفتند.
🔴
🔴
باشگاه همچنین به سروش رفیعی اطلاع داده قصد تمدید قراردادش را ندارد.
🔴
🔴
تارتار هم گفته هفته آینده درباره ادامه همکاری با بیفوما تصمیم نهایی…</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/135235" target="_blank">📅 00:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135233">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❗️
❗️
وای چیه این فوتبال ..از دقیقه 80 تا 90 آرژانتین سه گل زد و بازی سه بر دو جلو افتاد ..برگام ...جونم به این فوتبال جذاب ..مسی موند تو جام
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/135233" target="_blank">📅 00:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135232">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❗️
با جدایی اوسمار ویه را و حضور تارتار فرزین معامله گری در پرسپولیس ماندنی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/135232" target="_blank">📅 22:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135231">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✅
دراگان اسکوچیچ:
❌
چون اجازه دخالت در نقل‌ و انتقالات را به مدیریت ندادم حضورم در پرسپولیس منتفی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/135231" target="_blank">📅 22:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135230">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❗️
❗️
فرهیختگان: علی علیپور برای تمدید قرارداد با پرسپولیس کمی فرصت خواسته تا پیشنهادات حوزه خلیج فارس‌ اش را بررسی کند سپس پاسخ نهایی را به باشگاه بدهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/135230" target="_blank">📅 22:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135229">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✅
✅
محمد گندمی ؛ سهیل صحرایی، فرزین معامله گری ، علیرضا همایی فرد و کسری طاهری از پرسپولیس به تیم ملی امید دعوت شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/135229" target="_blank">📅 22:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135228">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
❌
قدوسی: مذاکرات با احمد نوراللهی در حال انجام است و مدیران باشگاه در تلاش هستند این بازیکن رو به پرسپولیس برگردونن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/135228" target="_blank">📅 22:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135227">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6j1coAGZtoYAlyLGDqo_C6makvZiFazu_K5La4Zsbdd0tYKVgeWEHp093duH6oIUR2ewJsz0-rmxiNR4QFxENPKNSU2ZZY0vHw65QeVJhQIYJ-JQh8fZurePa0TAUH7We0lHZOdGHg8HTSGqEgBJvcyNDCD9o54WB-AZ70lO8iYZDZL5PWX0xcjgJuNoHyEa7v69J8Q8tq4IcJazIITFi4rmZlcUIFnnzvT5H-CUulEmJRDrGf-ytDj4h3DvZQh399hbiOZFSBaVBYMVODwFSPpFHKg3r3ctV_w4cIL-T_7mahmvIKHfpuR5LtXVIpsT7jGdU-50PYNF6mNc6r4wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
استوری یکی از بچه های گرافیک کار باشگاه
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/135227" target="_blank">📅 22:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135226">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/135226" target="_blank">📅 22:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135225">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
❌
محسن خلیلی: هر مربی ای باید افتخار کنه که سرمربی پرسپولیس بشه، اسکوچیچ نشون داد که چنین لیاقتی نداره.
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/135225" target="_blank">📅 22:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135224">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iP6AIXkfPF1s6_KyNkBapadsfmmQ8YJ90y-MME89EjJrgxwDfRXN7ZJKw_VvumB98vNegtXzo6rNEjodbnzWyhnZZNM0y46EaHqbdYkYcU0KLb6D8zgCWQ14Dxs2o8qdK8c9-rd8kFnLrLZy-0GDVNcSaqMlhgm7MuVfnx1vVvZVYl6JJdT4sZj3F4Cde-yO8XoVu8aOLeOPzCAr-Eke7mql9FROGbnvOwUQ0f3oHaxjTQ5DgE_YxuXXKNbsT7Ml3O590y3uV5Ns9mSQGN2yaSDtI7G4uHn0IK4HXeVT1SfxNH_95EFxrOSKjACzi3bRn9FXIUp2u-cPj0VU3W-4Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
واکنش مدیر رسانه ای پرسپولیس به یک شایعه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/135224" target="_blank">📅 21:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135223">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bk5B2SJ3Ht0kzJdC3GAJqnTwReSgtpL9AASI26yIJ-jowaYQ-M-4nykntCU5pxH6OkkrmbBUB3ptA_-q_NuH2r5k-Mw1w5OyGF2qe3yOrM0X3Ifbcs-6Iit1svBmTH-aXIbE8R5ZPgTkMatgs3GxbOm4EXHz-2lzAB4JCBu2wcrtiv-e2f78FijcbQAVhGlm50BETAZGc2FVVW_vtmxUkcMPjmfrC34ZxpKhutvDTz-AdxgoH9xKcI_V-BMazdrU_MHYWk9aOWZYEmdN7KUCb2qpImabE0JpKYEEywv0N_ZzQcxq9MUVdtG1tTckFXOPx3PdKDIknqpAiUIkLqIpwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اشک‌های زیبای سلطان که در جام موند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/135223" target="_blank">📅 21:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135222">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
🔴
وااای آرژانتین تو ده دقیقه جبران کرد و بازی کرد دو بر دو و فعلا مسی موندگار شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/135222" target="_blank">📅 21:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135221">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❗️
چه فوتبالی شده ی گل و جبران کرد آرژانتین و بازی شده دو بر یک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/135221" target="_blank">📅 21:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135220">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✅
برگام ...مصر گل دوم و زد و مسی هم مثل رونالدو بدون جام خداحافظی می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/135220" target="_blank">📅 21:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135219">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✅
خداحافظ مسی .خداحافظ رونالدو ...دو تیم گروه ایران رفتن جزو هشت تیم نهایی   پ.ن با این نتایج انگلیس تا فینال راحت میاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/135219" target="_blank">📅 21:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135218">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✅
برگام ...مصر گل دوم و زد و مسی هم مثل رونالدو بدون جام خداحافظی می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/135218" target="_blank">📅 21:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135217">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❗️
خدا کنه مصر نیاد بالا .وگرنه قلعه نوعی بیچارمون می‌کنه ‌..میگه دیدین با دو تیمی مساوی کردیم که هر دو تیم اومدن تو 8 تا تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/135217" target="_blank">📅 21:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135216">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
❌
اوه اوه مصر گل اول و زد ...آیا بعد از رونالدو مسی هم امشب هم خداحافظی می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/135216" target="_blank">📅 20:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135215">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
و همچنان مصر نمیخوره و داره آرژانتین و حذف می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/135215" target="_blank">📅 20:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135214">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
❌
اوه اوه مصر گل اول و زد ...آیا بعد از رونالدو مسی هم امشب هم خداحافظی می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/135214" target="_blank">📅 20:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135213">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✅
✅
ورزش سه: باشگاه نساجی مازندران تا کنون برای جذب سه بازیکن جوان 115 میلیارد تومن هزینه کرده است!!!!!!   پ.ن امروز دانیال ایری با 70 میلیارد به نساجی پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/135212" target="_blank">📅 20:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135211">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
فووووووووووووری
🔴
🔴
ایجنت میلاد محمدی دقایقی پیش با حضور در باشگاه پرسپولیس قرارداد این بازیکن را به مدت دو فصل دیگر تمدید کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/135211" target="_blank">📅 20:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135210">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABr5BAQthMODcMSKKN_WqWlefjp2YBcqADFlEcEVOCuqIKjf9NbI_hjuZv2DDhodlvu3aeUR1PQu2d_PQxhgGZ0Z6j7D3JWcUF7gEE-YUp8Y0_-X_biYz3_x8zfRWE-tV6D3FyPpOkQyldTaUase7ELoyRfjuAp4liQEgv1AkmLvBRPp6zSwsWTP7gq-WnpEpz3TbFxUMR2S80b4JvfqPeO_Uoq_00z85StAYHkQ_1T_2fxHwyhG5gvaTC40E3oFnAJJeVVMx8GpY9vBSIOMfu7NC10FMdoKb2WXPBx5J4cQYaxrMAya4fs5uRP_y6OgaoLnNe7uC8EtB5X27f_eVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکس عالی برد شد
❤️
☑️
✔️
@HaJFixed</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/135209" target="_blank">📅 20:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135208">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✔️
#تایید_خبراختصاصی | #اولین_رسانه
🏅
مجید عیدی با عقد قراردادی دو ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/135207" target="_blank">📅 20:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135206">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uuFsLol1xWwJFs904ih-PWyYCz1dDkkFEXatBE2CqYL8yRt6PfdgnMz8FvUhUYSUFQUjl0YTiIjfCRU_x3gtN02k8qEvpNrAAEUnxgs0LmcnRYRnsazuL3BdQ8_2v93uJewGdRlEvLFNmuAY7w5UmLhxK1ehCtpC0QiCMxgwrWQu2y89ZraT_HwfZ4Mv8E-p-lxz3OlPT9AJEZma5KV2EpJ1tzC-I--IVJg6ij_N3lhpgXycKSZuAwEJJONHDthP9xU5WBbpzBmRqmbkk73gNhgLvAgjBOgCyvOnN8HXfyZOb07ooc69UtgJQGfGzxgu-UcWHmP_Gv18YqFbtw5fYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✅
نمودار درختی دور یک چهارم؛
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/135204" target="_blank">📅 19:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135203">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/135203" target="_blank">📅 19:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135202">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❗️
فووووووووووووری
🚨
قدوسی: حضور علی نعمتی در پرسپولیس احتمالا منتفی است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/135202" target="_blank">📅 18:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135201">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
فووووووووری از فوتبالی: ابوالفضل جلالی فردا ظهر جهت امضای قرارداد به باشگاه پرسپولیس خواهد رفت و قرارداد دوساله با پرسپولیس امضا خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/135199" target="_blank">📅 18:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135198">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❗️
پیشنهاد مالی بالایی به پرسپولیس داده، اینکه میگن پیشنهاد خارجی داره دروغه و فعلا باشگاهی خارج از ایران نمیخوادش//تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/135198" target="_blank">📅 18:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135197">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
بخش‌رسانه‌ای‌باشگاه پرسپولیس طی ساعات آینده پوستر رونمایی‌از کسری‌طاهری خرید جدید این باشگاه را منتشر میکنه. قرارداد طاهری با پرسپولیس قرصی با بند خرید 1.2 میلیون دلاری خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/135196" target="_blank">📅 17:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135195">
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❗️
❗️
پیگیری کردم؛ میلاد محمدی هم به توافق قطعی با پرسپولیس رسید و طی ۲۴ ساعت آینده امضا می‌کنه.///خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/135194" target="_blank">📅 17:15 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
