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
<img src="https://cdn4.telesco.pe/file/QEeGzf522rtUOstugUVlc4i8NUVbKDVXZ78kUk9N_W1hI6DcFIDi6ZJKtQ13yNAV1E0a_DW6qW07uMmk2RKucMjxAdbb-vb1NAiie8Q6v0l4Lz4sm7Y_X54IkvK8Ftrr90PWiq_rD0TrOM4_9cRPGGEX2SQ5-mRxrmnlfovG57yFP3IFBAlUSIltv2uGL_9VHUSEDqmWdNULz7qty95odWjOKOeUQN4l3L66Pq8Ng_n0uazcUIBwNqqEtiIhjIVbEmLYab-7YRoiNtib9QprdAc0kxmwL5Su5xdaaGIaZotv1apy6BqJhc9tIB2A8QIYKqjftVwB8z-robbU7zNOGQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 16:52:31</div>
<hr>

<div class="tg-post" id="msg-136312">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rj1f_iItYyqUUc59YyztrMQvUygCRMJUd3YAIQp9ZNXMmWLCkwFmvM0eP8x8IZ_TelLutUomZajWw-9ZD1LDTRo9jjjbOL1ezv9YxXbr-IBDo5U0j1m-daSXtv5xs31ABid5ETUtYsreqTwX--CyBxb6GjucxkILQgBSNTWIW02uLk9ahrMCxIEx4TfAi6IjwO6JvkPGxkOxDPbwnYCBedVd4R8gZmON38P9IM93uS8kc2XD3vEy4K8TiRVJ0-TkA68tpnV1pi2cNIV7Eejqe1viglUjQI4DIfE-3b8mSTHNJ7Diwt-awR8HoOz424glXIhArwbvxslZV2R_xsoP4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوووووووووری / آنا
🔴
جذب ایری توسط پرسپولیس منتفی شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/SorkhTimes/136312" target="_blank">📅 16:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136311">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
محمد عمری 3 ساله با پرسپولیس تمدید کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/SorkhTimes/136311" target="_blank">📅 16:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136310">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
شنیده ها:پرسپولیس امروز 40 میلیارد تومن + رضایت نامه قطعی کاظمیان رو به فولاد برای جذب ابوالفضل رزاق پور پیشنهاد داده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/SorkhTimes/136310" target="_blank">📅 16:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136309">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLh7MJB9g_PSjHpJX3dgNDr4gWs6TkeRJZWKjiQ_MKqSdpxvEeGC863oZY6bIyZe7XD88VGoNMAeC0AjCl0SBDaEWlj-x52vjazNpCsrluKR3GRZjC98GZ-xhIgGNHnGl7xn6J1Vb2taxg3Q35TYk0mZIOtNP-X7pytM6WIC4ZiueiSX7ane0auIme83eYAgrA4qqL7CDOUXspGa4fKAQHrzT7YJFP4b2Nr7jQEqFOKNMgmYoMiYwcLF-6-nWGZq1rfxyPo6shRVlwyl_04-TUdI7Leeyvt4Kz4Ir_gC4lAloz-tRKCKhtotj1x_WbzYFO7r2cr_ohwUUqOAd6-WxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محمد عمری 3 ساله با پرسپولیس تمدید کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/SorkhTimes/136309" target="_blank">📅 16:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136308">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❗️
❗️
پرسپولیس برای رزاق پور پیشنهاد پول به علاوه بازیکن به فولاد داده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SorkhTimes/136308" target="_blank">📅 15:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136307">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
شنیده ها:پرسپولیس مقدمات لازم برای مذاکره با محبی رو شروع کرده و این مذاکرات در حال پیشرفته
🚨
جذب محبی نیاز به رضایتنامه باشگاه اماراتی داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/SorkhTimes/136307" target="_blank">📅 15:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136306">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
❌
فیفا ظرف72ساعت آینده استعلام باشگاه‌پرسپولیس‌ونساجی رومیدهد. اگه پاسخ مثبت باشه کسری طاهری بزودی با عقدقراردادی چهار ساله رسما به عضویت باشگاه پرسپولیس درخواهد آمد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SorkhTimes/136306" target="_blank">📅 15:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136305">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❗️
❗️
دوره حضور وحید امیری در پرسپولیس برای همیشه به پایان رسید و او از جمع سرخپوشان جدا شد
🔴
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SorkhTimes/136305" target="_blank">📅 15:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136304">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❗️
مذاکرات برای جذب محمدرضا اخباری وارد مراحل پایانی شده و باشگاه منتظر حضور این بازیکن در تهران برای عقد قرارداد است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/SorkhTimes/136304" target="_blank">📅 15:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136302">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CK2KmXrQNpX6AOjkgtcdT-aFPd7wsN4PruIfCnlXcfgibo2maXoaJe3unSN1OOPn6Bj7fGoqQfvuhoNMb22oxzxYclDpkdKBWoUvwHYFjFEUehZoGL59spUPr-j4YrOqJti-lMZusI27QwvTKANfSBIBOKGUyvxohX0wfYp1TFkyqHMcwjsv6fOAAn-aEWkNTLMYjbU4_l33s7XsdhWi75gK1DMzO9LaW3OpjearKKPDbsZdCbSIv6RJ1PYlUuP0VnXqMhkJHgUKposmYhN9HglM0mgd7_yH52MYoRMn-Db3CbtPVk-uOlyUP6DAbjHAxq6j7qiE_88FrF52EJTXPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شنیده ها:
پرسپولیس مقدمات لازم برای مذاکره با محبی رو شروع کرده و این مذاکرات در حال پیشرفته
🚨
جذب محبی نیاز به رضایتنامه باشگاه اماراتی داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/SorkhTimes/136302" target="_blank">📅 15:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136301">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136301" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✈️
اپلیکیشن MelBet
🥇
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
آموزش ثبت نام و واریز
🔒
برای تعیین رمز ورود حداقل از 8 کاراکتر و حروف بزرگ و کوچک انگلیسی و اعداد انگلیسی استفاده کنید، مانند Hamid120
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/SorkhTimes/136301" target="_blank">📅 14:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136300">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔺
بانس‌های فوق خفن مل‌بت
🔺
🫴
100 درصد پاداش اولین واریز
😀
100 درصد بانس یکشنبه ها
🎁
100 درصد بانس چهارشنبه ها
🔹
هر روز 1 چرخش گردونه 1 یورویی
😀
3 درصد باز پرداخت نقدی
😀
بانس شرط رایگان 30 دلاری
🎩
10 درصد باز پرداخت نقدی کازینو
🎆
بانس هدیه روز تولد
💵
و چندین بانس دیگر از جمله بانس خوش‌آمد گویی، بانس شرطبندی طولانی مدت، بانس 1750 یورویی کازینو و...
💰
هنگام ثبت‌نام در Melbet با وارد کردن کد هدیه giftcodeir بانس 100 دلاری رایگان دریافت کنید!
🆕
معرفی سایت و اپلیکیشن مل‌بت
🆓
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/SorkhTimes/136300" target="_blank">📅 14:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136299">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
❌
تیم پرسپولیس که قصد داشت فردا برای اردوی اماده‌سازی راهی شهر ارزروم ترکیه شود، با یک هفته تاخیر اردوی خارجی خود را برگزار خواهد کرد.
🔴
🔴
پرسپولیس روز ۳۱ تیر ماه برای این اردو تهران را به مقصد ارزروم ترک خواهد کرد و احتمالا دو هفته‌ای در این اردوی خارجی حضور…</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SorkhTimes/136299" target="_blank">📅 14:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136298">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
❌
باشگاه تراکتور مذاکرات مثبتی با علی قلی‌زاده، ستاره ۲۹ ساله لهستانی، انجام داده. او قرار است ۷۰۰ هزار دلار به عنوان رضایت‌نامه به باشگاه لهستانی پرداخت کند و سپس به صورت رسمی به تراکتور بپیوندد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SorkhTimes/136298" target="_blank">📅 13:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136297">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJpkMwEQyzkABX2B2QEYTo-uldM3PEAqy79mm5m0tJomNbhkm60uaJ1B_tH-j_LAqVcmPlZ9uELLTyRIOLCkIxcdZ0MJn2XOMYS9kovFnPLtmimsAO1Ba-qiDeVkAJM0zdF-oUrKNz2sOTB5fcpWrP4TA8pp8LQdO5Pj3Aid9dmHxdTAjqdvZegOZMT0CU9f_Yn387P4rDITWOOl67kNA_V--8kVa1Alpilnnfo_IAqtkBjO4Ow9U4-21saAU_Z9qfobK5F6hVjV6pM3imghwIl7Zt4oLFt2R32FYEy14IQo72lmA8rq82L-afvkYLASKX9tTrFw4-vratgQhSAz_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
تارتار همچنان ولکن گل‌گهر نیست
✅
شایعات؛ باشگاه به دنبال امیر جعفری مدافع چپ گلگهر
!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/136297" target="_blank">📅 11:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136296">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❗️
❗️
پرسپولیس در یک دیدار تدارکاتی روز سه شنبه هفته جاری به مصاف تیم خیبر خرم آباد خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/136296" target="_blank">📅 11:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136295">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5fqgZdw1TDGt9U457AQkFu38jib3cXOta2ehADreqN1BF4-NLZLf7DcOygT1bLXfaDhk91WoZg-oGlBL3boQzxpzQzFvil0T1h8e5ItFI1-rDNALM4VZ9ZcIgY5xNTVPZwKnjELQpUZPsSXN8JKDyA2X8UeCffCD5IG2RrDb4Ix0og5NpVWgbAYdDFMSEHLA5ywuaDA9VXYi3xQVPKhJQE-nhmkrZ7x9ayAOTb2x0jeYH54OvXBjAl8BGhsBxF6VxHrbPwqEkFa64MlfWKR5Lx4AR-y_BZNPSdPCPTkWWmjRPfeUVK86DEY0m1XmujbPyQc-ahMVEOKUTVKXhNVlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رامین رضاییان از ایران با دو گل و یک پاس گل به عنوان سی‌ و هفتمین بازیکن برتر جام جهانی انتخاب شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/136295" target="_blank">📅 11:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136294">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✅
گویا دوره حضور تمرینی وحید امیری در تمرینات پرسپولیس به سر آمد.
🔴
احتمالا از فردا دیگر به تمرینات تیم نمی آید//طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/136294" target="_blank">📅 11:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136293">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40e01fd378.mp4?token=FsiC2LJOu18xDgodjMZhcxuVNZKZ4D3kMQSiZLzotwln73bS2K5dc_8zf5bBHKDpBoU0JRscsgIPX8vT1pQOzgyeS6haqK8kGu0JtEghsGAjP1xP57zPh8HTk8JIxMFhZmzK1PrzjjrXU9EdGr_yMUpDHHwO9TiWB5L9dPkgiizoEjYSAOclTWYznQzzmg35xAw_LdPLr4dN3n0lZ8gmCZNKpASCQVEicbairl54x6hueTY17YpEH2ALWCjs1Gq28UswpjL0wuTrpzCeMiCIO2A-trlnmWxxOajMfesSW-OErPtSZMqz176T250xTA43xajbG8EMfgTIbKXKfrQ2zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40e01fd378.mp4?token=FsiC2LJOu18xDgodjMZhcxuVNZKZ4D3kMQSiZLzotwln73bS2K5dc_8zf5bBHKDpBoU0JRscsgIPX8vT1pQOzgyeS6haqK8kGu0JtEghsGAjP1xP57zPh8HTk8JIxMFhZmzK1PrzjjrXU9EdGr_yMUpDHHwO9TiWB5L9dPkgiizoEjYSAOclTWYznQzzmg35xAw_LdPLr4dN3n0lZ8gmCZNKpASCQVEicbairl54x6hueTY17YpEH2ALWCjs1Gq28UswpjL0wuTrpzCeMiCIO2A-trlnmWxxOajMfesSW-OErPtSZMqz176T250xTA43xajbG8EMfgTIbKXKfrQ2zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇮🇷
بقایی: با مردم آرژانتین مشکلی نداریم ولی مردم جهان قلبا دوست داشتند که اسپانیا قهرمان شود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/136293" target="_blank">📅 11:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136292">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
❌
پرسپولیس دو پیشنهاد خارجی برای امیرحسین محمودی رو رد کرده و می‌خواد فعلاً نگهش داره. درخواست شماره ۱۰ هم با مخالفت تارتار روبه‌رو شده تا فشار کمتری روی این بازیکن جوون باشه.
🔴
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/136292" target="_blank">📅 09:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136291">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCY736WxEoXLzXnaTJpTGAS3agYi8etFUsurbHQy9Hhd1lN9-VVCuVZOxsvh-jrUtrP74-cxtFWmo72jKN5wCRjt3knoOjHRN9bs6EWH-ukuO8qvxxAQ2YgSiokpX5qw3FRIvwKtZfk0QgV6njybCKYoYHbrlI9s4CVdEWpOqhrOWAMcUT-FVlFh626TnjFMPau-_L13_wqKB5Tw5G6xclwJVmQsVHeXFiS_zmqibxuFFkxygzIHjyoGfwcB0ou5ot0qec2LAn5fhCgEjVHkup10Ne1dtc5uXYhAy6EP0fpbNtc-pvkIbIHzJNAA8w4QEp4FlGwqu4gIaH2NMwrd_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
کیلیان ام‌باپه به اولین بازیکن تاریخ تبدیل شد که در یک فصل هر ۳ عنوان زیر را کسب می‌کند:
🔴
کفش طلای لالیگا
🔴
کفش طلای لیگ قهرمانان اروپا
🔴
کفش طلای جام جهانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/136291" target="_blank">📅 09:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136290">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uns-T9Bopckmb4OdNh-eqw3UfKDLmWsgE0b-ElomGO4Q46uPJxW31S4gb0Hto2LWiGfTVO8oVhvDRUHGU3mm5MNZtv2gX0S4VV5s7YgyJrM9RrH5gDvpBARiSjen3psKWkDPpD0P2cRILyAjlo0Ovc-zTC_ZcD-o9l8VZALz8Z0w5n7uRcrsDoNfqeyE1uU9W9TX5In-GmoWKLQUKp7GWmzJLRMKxv1N6Hoc1BxhE5LaihGEsrA2pU0DS3NQNTMyiFR-Wr3lfigO5f9t4ko5lAL3L-ttiDp71265GxtOEQG62bdRhx5Yv2zAuR0eno-WnKmNMp6TaaGgxTsipc3dVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
چه قابی شد ...
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/136290" target="_blank">📅 09:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136289">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J73mtsPGq5heDYzCRJljlsGApgCVqPVa4AK5wNGQOvLcRRL13t97sZytrWgyiom0ehdDDwRvt1eNv5jWRtCtwrrjrJlpDdoBbpgDC-OEsgpxKUs5EjgZ3boDHC4r-rauxmlg3xY5_zpcE3tfe_jXk8p0iK5N1V0EU3U5dUIVXlYob9GJel2qENWM3mSPn_d4jCn14N9y2nHqAtZ1dcOakPIBnJ7V2hpoVC0-IcvC-qbUGCSPL4Fh62quUZ-GLcJj_K0fS_74U5yGojp5LRqsjY7oWtoPKphZMctYMVynR6mHiOwv1h5yAarHWbmvG1rwJKW7sfX9PrptyjYom8LgOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دو زلزله به بزرگی و شدید ۵.۷ و ۵.۲ در کورزان کرمانشاه به فاصله ۵ دقیقه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/136289" target="_blank">📅 09:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136288">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✅
گویا حملات بسیار بسیار شدیدی دیشب به تبریز شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/136288" target="_blank">📅 09:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136287">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
❌
فاکس نیوز: هروقت داور بازی سوت پایان بازی اسپانیا و ارژانتین رو به صدا در بیاره جنگ علیه ایران اغاز خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/136287" target="_blank">📅 09:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136286">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
❌
ورزش سه: محرم نویدکیا رسما خواهان جذب ابرقویی و کاظمیان شده در این بین گفته میشه احتمال معاوضه این دو بازیکن با آریا یوسفی در قبال مبلغی هم وجود داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/136286" target="_blank">📅 09:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136285">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇪🇸
🏆
بالا رفتن جام قهرمانی توسط اسپانیا
💢
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/136285" target="_blank">📅 09:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136284">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYb5LOOx1va26i5rbDIFPEehtmcePL967_ICu1B70NRt0VPyYvl-YUGDBdMIesyAaV3xqFlWPWRom6xlvXyDIDchuJAt7FEl4TJVy3qV89cgIesOzrpHGZla4eY7oKGEy8d31TI_gCZ-eVl0BfVV-lvKhYBaQUZ_JpZbveEwZG801QrBkONsLfvLkNd4iyQHVUsMTsKJxtda2HNZIx7KsIyHFkX3yUKbPIdSFmfZ049Hr3daxMkCyfL76_B_vcnivYg1uxFkCJ1rK5hEVr9S4vonRpdC7u3FI47LRDUGHUf-uS38F04Ha_Ztv3YM9u33MZRGPgUuuTsyCnWoxDZGPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/136284" target="_blank">📅 08:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136283">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136283" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/136283" target="_blank">📅 02:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136282">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z--7TvFK1bdekOT7vXDGVGp8ojSBTydcdxDm9O3_9uoLAaejgd3jPrtfBzp_ZY7vXuN42IR5TQ2_7Wqx3oNo6SdEKheKchdPiXROGR4wAtTt5sK1K7qqQm-lUuPjJF6xjWhbpuusqvQXLftxAsQiO0eRQItvjpGQWUTJ8aB684Z6HAWoy8yJb6IW9w6VPU61e4pmp9L8Cdwcc2hw-UmJ4XZ2u0sE2-HdW3Mkd-EnrVIaIB_IxV_z4N4gRfBdUtTQ-jYXg5dmWPQ5ad6z44qiFNztQcucr0tPfufPvD7CyzFtJ4i-0nfy5DUXETu6MIGJklwxfyu4EB-LNn2BKeMaJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/136282" target="_blank">📅 02:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136281">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-nPEHp8IO7x0mIbkizVNefUQoVa2EDHEFNfbZi5xfrq3c6x3aBl_l-P6EvFsdwqSTu91K6jAKMOyklItg8V-LxZ2-v8yZNaIMx30Y5N0r7vcJ7TLsgVq0SbadNLKQsYpiIoJxp_hCi4kipTGOnftIVRww3rww8TkHiEvh4jDty8vuoH4FWhwdGVMQlSsRMOl6vT35FhSwi0Juqlv_dFEYyFT25cD9xjo7gHxszfnZ80fYYbhkjh9d5x4K9PBI5NceK1TtI9zeRLkSzqdKCqt73xgzJBFG8sUY4M2SWc29-4-He5vKGsx_6BznWHQQhgIRtdn-SUCPPu3EfEkzlaXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏆
بالا رفتن جام قهرمانی توسط اسپانیا
💢
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/136281" target="_blank">📅 02:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136280">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">⚽
فیروز کریمی: مسی الکی داره گریه می‌کنه چون دید رونالدو گریه کرد وایرال شد
👎
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/136280" target="_blank">📅 02:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136279">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2lZUH_ccwhRSR_yfZA1qMOOV6Qr3E8LSVSC23cZzQnMnabU_59HTgXFytMVoTSst_wHBY8NEpgQP817y7ArArASwI_u9cPwrhy5TgEX8wT4RupiseYi-WJTSt2Ar31nUAJv9CeHEgmao5PmI7oMB0EP6CqCQGNqv-1HkkClt75tNgbMhSzzC3yIPIeeqU96UibC-Luft_aOh6_FnX4DcOs9Jx3qEVPv24yMtT8y7Ev43UZ5IXKsmfD4Gv2MA7Lm4kT1SvwWUwmZP0XWxuklik_qKGs31h49YSSSjZYXsSYA6SRG4lp1e3C6kIfudwHkU8JB-pwfnOi103PyjGZ1Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
⚽️
سرخیو راموس با کاپ قهرمانی جهان اومد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/136279" target="_blank">📅 02:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136278">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ueypOWUnsGEgLXG3OZXh8xUlPt5sxWWrpyRZ3l4QvNDShBp4aEUneu3Uq4HGdRMNoj02BMx8nuKpU5X12qcY8ZIqqwmIQGKt6GWXzmTxd-zu9onR6IMshjyT11crSY_8KckGUK7mZKpDEciOkqiIGpr0V9-SOGSWwSk998Bv1M0Iziv1eF5vw2ubDCHUYl9orYDQoIxhxpSWeblH2GVlgDJKh2MESRMqhWdM5M_sW6b10Drpq7TMtYR6n7sLcjTFwmo7OhZ9f10m0OwPpGypQN03eXBgBN4NRlSCPlwl00JS_o4MOG988-N9DG6Zvk50waxglrzVx8XKn06Xgo1oiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
💀
گریه‌های مسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/136278" target="_blank">📅 02:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136277">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇪🇸
قول و قرارهای عجیب ستاره‌های اسپانیا برای قهرمانی!
🇪🇸
یامال : ریش و سبیل میذارم.
🇪🇸
گاوی : موهامو صورتی می‌کنم.
🇪🇸
پدری : موهامو بلوند میکنم‌.
🇪🇸
فران تورس : سرم رو از ته میزنم.
🇪🇸
کوکوریا : چهره لوئیس دلا فوئنته رو دستم خالکوبی میکنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/136277" target="_blank">📅 02:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136276">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c877f07487.mp4?token=moW7EzgPrnCfcHmsnbilAGjaiTOEeqC3N7peOSy6NggHjkQZNzqr0XeaYrkyNYb-8CMtMVDmgrRylk_J5HaQJCRC7UCSpvrp2ljvbssHw9LZNWC_7FQsutmfOav7Ax3XrVtn0hxM0PI8vXWqp2x-ZsYOw_zqQ5ofInsW_IcfqldtaW0ebgAMjCVg-HSvXg9wRLsmK0-W-14A_VJiZZnVc9-Wo0ITXL69dpqX3A3kAo7jtbCXgXP2KwjGIXxOrWtGIFjQxKqQC1msII_3Kj2tax43EyYg7q95gqta3g3Gd4EDb1kxmNE5vQPzI7PmQIt76fx3qLcvzekG3zzH4NLkHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c877f07487.mp4?token=moW7EzgPrnCfcHmsnbilAGjaiTOEeqC3N7peOSy6NggHjkQZNzqr0XeaYrkyNYb-8CMtMVDmgrRylk_J5HaQJCRC7UCSpvrp2ljvbssHw9LZNWC_7FQsutmfOav7Ax3XrVtn0hxM0PI8vXWqp2x-ZsYOw_zqQ5ofInsW_IcfqldtaW0ebgAMjCVg-HSvXg9wRLsmK0-W-14A_VJiZZnVc9-Wo0ITXL69dpqX3A3kAo7jtbCXgXP2KwjGIXxOrWtGIFjQxKqQC1msII_3Kj2tax43EyYg7q95gqta3g3Gd4EDb1kxmNE5vQPzI7PmQIt76fx3qLcvzekG3zzH4NLkHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چخه سگگگگگ
🖕
🖕
🖕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/136276" target="_blank">📅 01:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136275">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">⚽️
اسپانیا با دلافوئنته:
🇪🇸
قهرمانی لیگ ملت های اروپا 2023
🇪🇸
قهرمانی یورو 2024
🇪🇸
نائب قهرمانی لیگ ملت های اروپا 2025
🇪🇸
قهرمانی جام جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/136275" target="_blank">📅 01:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136274">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4lLlkjgWFA3eVRRlyUSnpLyj5ms4lOC0OfZNmVkQNxl9MUs0zjx03RQmvoeFZjN0S-wenbAOICiTlYDNLMFLXsYqdiEsIAgGfu-jNhMlspqMVfrt-8_v4xIbvzvHqi1HzIqm--plI1GgDPu6buF7pJiiC3cPrfqO5EsJM-jYBUfFGkzNEfwfJV8ccdDRmWEeaOvR6wPULh9kObmYGr-8ujG-5Dq0IcWyGZrqIGjeQEXpv_8I685jSXq9nd6w6vdTW_x1Iq7XH_T-gcJ-nUrIxLBJ8paZCEZPNfamjJ-qLVfPlVi7dG_a63U8IpE4Rz-iD7H2QOB3NQ1XD8NkiNDUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
عکسوووو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/136274" target="_blank">📅 01:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136273">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJ_M5zUZILfVCSZHsaVbmi6GlKh82I1YDnvke4XKswzft5n-eBpKvELwy0lJ6_m3rAptQa4wosjB7QihTzEjjlIZJeKhYpfYHf8_JwAJRKR_wrkqWMw0lYSdeVT3elUPO1-GponQiunML77E5GNGaKory4g4Kv59uBeL6MmxsScfIKOQHBKwG2pGJbXYOX-w4bnZMlNPYun7N-nfpOiIf2xLtR4cP_GBvnfpe8jkYnMiQxZ-5wjsNE7qTg84QGsXZdYGZtCfj2_AFT-8ql4PVW6qGDL1OXIX76JQ4mikeBHRaodS2M6cnergm97do4jh9QKhAAfGuMTS5WsOYeKOSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
‼️
کنایه سنگین تونی‌کروس ستاره سابق رئال به آرژانتیی‌ها:فوتبال برنده شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/136273" target="_blank">📅 01:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136272">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHnGi1uDBWHPLrR1hDG3SNxlDzi8JKvANqM9upSaPPJXtdKcZ952YIE-zFgHO6bmOelERFxuhc7UXk2eajKU0wboLwKio2KS6R9UVk7t6JF8Y0TJkTU7fXCEGdz7GwkoFFkqnspSE4FLOG_dO1WsGPTRxmRaueHIxcWKtkqGZWTRSTs4vr1AgOWoVFgSZagbWQbVpIv5N9_QWvIIKH_IY1q6Vnwn2y1D9CXmattaWSDB28Kj1Lig6JcXwzSXpzYbE77mqmYQ-qdBEpClOXYTVeF68DlHJftT-rCvdN3eQ9A19rA0xnH4M4M9bnx4ovwBYvMo8GMGnSVKyMaRUKwlSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
اسپانیا با شایستگی تمام قهرمان جام جهانی 2026 شد‌
🇪🇸
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/136272" target="_blank">📅 01:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136271">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWIQqpgdtgazhJZzloLFzQMoyuq_WLe29lVC70Scqc4kVUjoARTWwJZ_LiExKDK4W2nkk1lLbRCdrdlzVLI9xFA3YRFqUtw1PJFRhusyrg3gGMdrFYhkTtQ07ZMae-Jdb8MFKhhTaC5lprAJ8SyAqfD4MjmQw1P7sCQ2f0sJyHBc3JCXbmNN6dKercRjQtqQpcDdhPpo9PwaRvrr5EGJp25tzMplUZzQNQRvtrYC86QLY1terPGoOSJCa3cSn-zfX8BNWzfwIBcyfby39X3C7FC6kg61tKhbPLcRiFMo2nQ12c-NLcCPeHNuxQYqdv0whE0Pb-LQsT-5XN6w0sVKbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💋
پایان کار مسی با آرژانتین…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/136271" target="_blank">📅 01:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136270">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✅
این بازی فینال که چرت آور و خواب آور و کسل کننده بود با نتیجه مساوی تو نود دقیقه تموم شد و رفت برای وقت اضافه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/136270" target="_blank">📅 01:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136269">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
بازیکنی که کلا محو بوده و خواب بوده تو زمین فقط مسی بوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/136269" target="_blank">📅 00:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136268">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✅
✅
🔴
ارزونترین بلیط فینال: ۹۵۹۶ دلار (۱ میلیارد و ۸۳۵ میلیون تومن)
🔴
🔴
گرونترین بلیط فینال: ۴۹۳۸۴ دلار (۹ میلیارد و ۴۴۷ میلیون تومن)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/136268" target="_blank">📅 00:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136267">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">⚽️
اسپورتی تی‌وی: کاپ جام جهانی 6.175 کیلوگرم وزن داره و ارزش مواد به کار رفته توش حدود $713,000 یعنی 140 میلیارد تومن برآورد شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/136267" target="_blank">📅 00:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136266">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❤️
🎥
ویدیویی از تمرین عصر روز گذشته تیم
🔴
از مرور نکات فنی تا اجرای برنامه‌های تمرینی؛ یک جلسه دیگر از آماده‌سازی سرخپوشان زیر نظر کادر فنی.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/136266" target="_blank">📅 00:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136265">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🏆
اجرای کامل مراسم بین دو نیمه فینال جام جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/136265" target="_blank">📅 00:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136264">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
❌
نیمه دوم هم چنگی به دل نمیزنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/136264" target="_blank">📅 00:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136263">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❗️
نیمه اول بازی .بی روح و خواب آور و کسل فینال با نتیجه صفر صفر تمام شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/136263" target="_blank">📅 23:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136262">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99bc7fc060.mp4?token=ruiLmU2EhO2XRO2p7sX0nZq14VCkEiz0fhD6IncdCOYQ1lZ7A6dfAt6rG-NSzRzBo_B01yTEpf0o25Lb9mWS2FvPieiyUhZoP6ykgdYifcsLtymUcUbmt_AqUPpwjgMhdln1E55m1U_LPlwfCiM_kct-78b_DVlLkfuIhnelEJiQxQiOVZ0JZrmb6PaF9FlEZNyyfkKggQ1-BO5tikxMLil22CS-5BkJaBHGZwje-4LFBivhGeRbS2Y6ZjU79mDfyrOqO5P0t_qrxp072LM6g02ZCGL7aWmT2wC9Sejt5yq0AFOiiL-5XLXAh-cMlk3wx4bHdjw8Mr8Iv8YpsqE96w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99bc7fc060.mp4?token=ruiLmU2EhO2XRO2p7sX0nZq14VCkEiz0fhD6IncdCOYQ1lZ7A6dfAt6rG-NSzRzBo_B01yTEpf0o25Lb9mWS2FvPieiyUhZoP6ykgdYifcsLtymUcUbmt_AqUPpwjgMhdln1E55m1U_LPlwfCiM_kct-78b_DVlLkfuIhnelEJiQxQiOVZ0JZrmb6PaF9FlEZNyyfkKggQ1-BO5tikxMLil22CS-5BkJaBHGZwje-4LFBivhGeRbS2Y6ZjU79mDfyrOqO5P0t_qrxp072LM6g02ZCGL7aWmT2wC9Sejt5yq0AFOiiL-5XLXAh-cMlk3wx4bHdjw8Mr8Iv8YpsqE96w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اجرای بیژن مرتضوی در کنار ارکستر فیلارمونیک بین نیمه بازی فینال جام جهانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/136262" target="_blank">📅 23:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136261">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✅
با یک چشم بهم زدن جام جهانی 2026 هم داره به اتمام میرسه ...بریم برای بازی فینال ..آرژانتین و اسپانیا ....
🔴
پیش بینی شما چیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/136261" target="_blank">📅 23:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136260">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdJBQDRf-yWgERGByz0qoe1ZS7bbLyc-oVWqtuS0os2sv8s62HJ2CDPRpBzAUNagQlEjuP8-dHgIYHozRe-R78zLKhVZClstoaZdHCccurnlAnkinmbyFIBIAmSflvJJyqODqNIc3rDr9mIGk7A6hWYVQm9d2A5r99o1XWyXOcLFVpwfYezE2zhhR4plL_57KjR0UK-s_YWx3GqF_fC7nLJVXrLYFcqvxeR5UyJ1Z7XN85sEzpk3C_eofTSEQ3lM9JV_TgBOKebOXlTVvnH8JV_DNxLs3iB8SCqdjWIGjJb3cKi5GGyjjJYFnxarTAsyij7NxKy_ittFuR2lfxjYRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یعقوب کافو هم به تمرینات برگشت
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/136260" target="_blank">📅 23:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136259">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
ترامپ از پشت شیشه ضدگلوله بازی امشب را تماشا می‌کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/136259" target="_blank">📅 23:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136258">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✅
✅
#تکمیلی | رویترز:
🔴
ترامپ دستور حمله قدرتمند به ایران را صادر کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/136258" target="_blank">📅 23:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136257">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✅
خیابانی: چرا در ایران کسی معذرت‌خواهی نمی‌کند؟
🔴
واکنش تند خداداد به صحبت‌های امروز امیر قلعه‌نویی
: واقعا خیلی از حرف‌هایش را نفهمیدم. ما لودگی می‌کنیم؟ چرا پس شما حذف شدید!؟ ناپلئون و هانیبال هم یک پلن داشتند نه ۷ پلن. آقای قلعه‌نویی چرا نباید کسی انتقاد کند؟  من انتقاد می‌کنم و نمی‌تونی تریبون را از من بگیری. مگر بزرگتر از علی دایی داریم که انتقاد نکند؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/136257" target="_blank">📅 23:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136256">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7_-ebd8DCn4xYrac3azrl9oBhbEgA185m9ZhVf2Lcki6DcVGr7e3dT4mKoztl9qX7vAA_9cuYx9nB_8Z9pwYe50XXh3rUAqRzBwiFll_HtfpfmG1wE9ADUFTfYkB5L1RlmCH8WTl6TarxGmOAXLSIgCFRNCY4PpMdDWPoEkde3zbcjcZ-wS3i28rM3IkUWFb30Bu8nU3Cdsj4KamReokELsvlAwUkPNJpbtAoukxHBBhyTBlnYEDCffOi1o0J0Azkvs-gwJ5KWlxy_5lKggKfpxZFablcRR62d2JWpBTFMwu2OfLiWybYZ8DkdSFP3MV3gdSJ1vrjkfua-7ZkbMKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اسپورتی تی‌وی: کاپ جام جهانی 6.175 کیلوگرم وزن داره و ارزش مواد به کار رفته توش حدود $713,000 یعنی 140 میلیارد تومن برآورد شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/136256" target="_blank">📅 23:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136255">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔖
تصاویری از احد میرزایی عضو هیأت‌مدیره پرسپولیس منتشر شده که داره توی ساختمون باشگاه یکی رو کتک می‌زنه…اقای احمدی همین فردا دکمه ایشون رو بزنید
❌
پرسپولیس چاله میدون نیست، ایشون ادم زنوزیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/136255" target="_blank">📅 22:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136254">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85518f3eb7.mp4?token=lHOswNq-mtrWqOn0NOTiVpmjHiKpGy5eBHGcOwDd6E3x3cgnxdFNu1bGBA6gIzS_sv7EanG9Gmc3J3ByTLBB3aF_MYdzuuj9H71c6tIvUbNnKQTiyek-TK7ZNV09LTEGstnvTZXP1kKwE4GqpOV_rxwGZ1WseHGC2plq86N4gZjzjx8rZ7GsfvVGQgRgXF1fcfKyCBnbKSdgpI878BfTbSH_bIvDEW-VXzfs7awqO7s7WiAHC0tw5fOxRdF0r014ENzh5rC3M3SjdG1tBN4LMeDzo3aekrC-FR_wy3tAtgsJqlCLJk69LKLhbJbncm8lnRJVNJ0yzljmE_6xYzTdtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85518f3eb7.mp4?token=lHOswNq-mtrWqOn0NOTiVpmjHiKpGy5eBHGcOwDd6E3x3cgnxdFNu1bGBA6gIzS_sv7EanG9Gmc3J3ByTLBB3aF_MYdzuuj9H71c6tIvUbNnKQTiyek-TK7ZNV09LTEGstnvTZXP1kKwE4GqpOV_rxwGZ1WseHGC2plq86N4gZjzjx8rZ7GsfvVGQgRgXF1fcfKyCBnbKSdgpI878BfTbSH_bIvDEW-VXzfs7awqO7s7WiAHC0tw5fOxRdF0r014ENzh5rC3M3SjdG1tBN4LMeDzo3aekrC-FR_wy3tAtgsJqlCLJk69LKLhbJbncm8lnRJVNJ0yzljmE_6xYzTdtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خداداد عزیزی: مردم نون ندارن بخورن آستینتو انداختی زیر ساعتت همه بفهمن ساعت 10 میلیاردی داری.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/136254" target="_blank">📅 22:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136253">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/136253" target="_blank">📅 22:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136252">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">جالب اینه تموم فرم ها رایگانه ، وقتش نرسیده که از فوتبال دیدن پول در بیارید؟
😉
✅
@FuckBet</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/136252" target="_blank">📅 22:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136251">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YiND4JWgBlO8e-ppVL9DEZhMrbEkyaYq6LsC4xPFItMZ_EyyRLfIevKMnNQC7DynUVT_S6tvYnAGc5eK1wLS9SpFM4Knk5jNFqv92PGcOY28A-mW0YYWwdhV0V2Eh5amk3Tk7pI6q3Sj4ORt7ezAHFbuTETVKF8UaWCysnjjtWqbaxclhuRZp0ZX0AO5maSthh-J2Fgizi3R5coCLxPFhG5A8hRnbVf-ESq89Nnu1q5k3bn9_QWt51MDQAxIPnFiW_6CzouXATR6VZ0US3mikUNaMZc4_XeWHoGzPP3gawTdvvYklHZUKJv9k_UP7CDVH5ERqw6xTxLhJgtPMJ5KkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
Ⓜ️
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/136251" target="_blank">📅 22:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136250">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
🔥
فوووووووووری ؛ از کاپ جام جهانی رونماااااایی شد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/136250" target="_blank">📅 22:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136249">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
فرهیختگان:
✅
وحید امیری 38 ساله به پرسپولیس پیوست و کاپیتان اول پرسپولیس شد!
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/136249" target="_blank">📅 22:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136248">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mF0fOUqM7pieGiPktNAHXoowcUaqVyv4GaxJmWWu1tpQodrpEb0Tel2zeaGEj4Mry_CIt7T-OoNfFejHjp-O3vYA1TdRBZJ2F31GKzns5kT9N0dIb_pBBGBwBjLQ-w49OibwHcVdcOHtctVjT1Ov2l1SYaJlxrxP-kkftddndexOXUcCcncKdDb0SlmezDkluT_Tg5p-zGNuG_Vjs6LnWGM3tHEtr6sg1xXDmj8V8XZctTyH6zNNBO5K0FRjVIyNVHZ_pEvd7sZFQA4q2t1Txv0VEs1IfJnofvP1y4gcsZiLDupQBOjP2sifYxJoa30UojjjTedNw7CLvJ5p40Q0Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔥
فوووووووووری ؛ از کاپ جام جهانی رونماااااایی شد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/136248" target="_blank">📅 22:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136247">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LckutBA6YTf-nBJS0Yk5B1X39KNmk7WL2nTY8zxH07LF1vQaN5KV4uDbjrWWwr28wLPuyn4EVaNyZPplB46NXYZ7oBF6M5M1_YlS_-b6PqjPa7v5fD-BLZu7uCHTgYaen31GygmOcDdZXnFXGWwdMD0fv7FKjB1yR5hBJCxBL2EOGA_FnAdNQ7LbQUYxnFCPqasUcafM2OGIR2l0jBrMxHJXHTHB9oql_jeyPHNi6a6G5lu38sDEcx7QmDFhSxX6FDBgn39DEkvPLt4ijBrM2lO2IPuZoIUzm3YE1hUVgzm-6jRpOy6DuivBGcDxcgz7clmlTn0PjpPveqRFykpX1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترامپ از پشت شیشه ضدگلوله بازی امشب را تماشا می‌کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/136247" target="_blank">📅 22:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136246">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❗️
امین کاظمیان در تمرین امروز پرسپولیس حضور پیدا نکرد و جدایی او طی روزهای آینده رسمی می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/136246" target="_blank">📅 22:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136245">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPE8KWTJSVl55iyVgGr59vdxvl8ZKxTWiGlnFHVz-n1Q53mAhKInNUFOacsqFiWNfuNmf_IcTuuTVlbJxRo_Pc74T4dbqw2KaflgqiU8bmIncdCXzOlp4FoeGSkJc0O_S9s7BPYQP2jUHdl685gSlGS3IPuDzHLimvT56a3bSVW24LSpMU9PV9xn4w7HH36G3ppyDPwD_HAhAOQ5eKteFw6du0_r8bzED2zFfrtCDEyHxTvgi4fA-p6VCPJ0SxfYJuil-1JynBnknFkcYvdlu81m2yhAs-l_OdCV9jhesb8qvJrxQGkG4uf9jcnm0Txmzl7ZB9NQfemWFqFi7ePO3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تصاویری از تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/136245" target="_blank">📅 22:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136244">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5b943d93e.mp4?token=e2QI5f6798vwdCwi0ABDx-P6nuHipzzhksU3nH3q4Ta-ANqrcu21abgogGDGYcI3zConm_imUiDhscEEIVj_-BjjJu1a-2GSvTesguF3QuliQ_Vjahklnc8wb38NgFIyCheVi8Vi_mj8wpROt_awDjAH6yAULogy6m2iErQAok1CBCcvCjxe7LOQHUvEnx5erCS581qZNHpzTjtNJDDmW_lnxJMvFlQCKq2VVYa5oCKReNOeO4bFIik4wET90dom_zx2cV21PJdksh4Z3mem8NGQ_LmqoRK-2aWn2fFSjilFOzII2TxuZQnXrM8PuawXrZCWYe6Ce2CzORs3FVsVUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5b943d93e.mp4?token=e2QI5f6798vwdCwi0ABDx-P6nuHipzzhksU3nH3q4Ta-ANqrcu21abgogGDGYcI3zConm_imUiDhscEEIVj_-BjjJu1a-2GSvTesguF3QuliQ_Vjahklnc8wb38NgFIyCheVi8Vi_mj8wpROt_awDjAH6yAULogy6m2iErQAok1CBCcvCjxe7LOQHUvEnx5erCS581qZNHpzTjtNJDDmW_lnxJMvFlQCKq2VVYa5oCKReNOeO4bFIik4wET90dom_zx2cV21PJdksh4Z3mem8NGQ_LmqoRK-2aWn2fFSjilFOzII2TxuZQnXrM8PuawXrZCWYe6Ce2CzORs3FVsVUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ برای تماشای فینال به ورزشگاه مت‌لایف نیوجرسی رسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/136244" target="_blank">📅 22:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136243">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
⚽️
🔥
مراسم اختتامیه جام‌جهانی آغاز شد  پ.ن فقط 45 دقیقه تا شروع بازی نهایی جام جهانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/136243" target="_blank">📅 21:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136242">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcN15ZJOnO2yyIz5o1VchEsuaFRiU56Y0-qyoIWTarfpKPrC4NL6y6KtHpFa6r36OvposrMGDRZqDFSXbzLfgu6yOOf-p52KsMXEFEIAnp_G_CdRIdQD6Jul37rOKj1G56MTSntFIhrnicoyzoXwu_XVfCdQW6bJ8exIvDEux6t-rq0xapVgu5AdGhkz015uNdMWA-UikzmTpzQiQbw5q0mLYSOytEX_kcn8GW0qlDzNr0_btFT8App_nyA4dohvZ2EJHyT5Ra0E3j24CYavT8i6UEcIFsilBq1Vyj4j3lS7d5ZVAesLI0gJ0zxGt9DcnPVhyOFFXePimf7woCUhOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
🔥
مراسم اختتامیه جام‌جهانی آغاز شد
پ.ن فقط 45 دقیقه تا شروع بازی نهایی جام جهانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/136242" target="_blank">📅 21:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136241">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a92f2cfaf9.mp4?token=fUBCgxuFqpdzJvg__9nbU-Scd3K6Tbonv5ZHjRBSWlREPKuj6P_yr3_olJ2EI_uZbrbPfyUJXSmXPVDQY3kjxAqh3Y9sz-HjpcHpJ9SFHfu01Uyadx84G0CQWvyHkAKuCBb7QGVHlsRv9_Fy8UPLhAu_ODzD3wiCRDIDDrgWggQh-aNURpBzR81MHg6X4nDNDm8h2XbbEYajI7du0Ru_905i4ZZO-219xfmVV1vSgJdRH78MMto_g1chb6Kz0POVy0JjrM11f5KyiOgp0USGeuApy6QxVMml84wHty8v-1nBA3uykAPQDEoios83PZRjDNG9EcTAX7UkxGSBEbC-_TYBS1jnRCa6qXDwqpGuBs1hRAtMj5I8W2Fo_X6uM1hCkRnIDVJAXK58_f65IA3-55ZgyydZeWDYlm9o6m7R85EMICatDiRuC-NdumgbeuGiqjJhS8JRVXqKk7szZ_n502lLlpNh1_72HdEVKyYKP8NaP1Sfk134FZCRT44qZ4htdH0skx5ai6mGYDBLvzvn7EAto5fsfALrMrpX1KjCJN2VXIdWft0cg2rPbFFyrh5ymSDw7uOYUuHXVy_NU0oqnyLHFB-VFyiV1DzJ1Bf_I9L3dWVIkLd7ppJjeUSJ_-lYACLhq_rsgO-ELU1y6NjOCTwfsIwODbaHslBykb4ecz4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a92f2cfaf9.mp4?token=fUBCgxuFqpdzJvg__9nbU-Scd3K6Tbonv5ZHjRBSWlREPKuj6P_yr3_olJ2EI_uZbrbPfyUJXSmXPVDQY3kjxAqh3Y9sz-HjpcHpJ9SFHfu01Uyadx84G0CQWvyHkAKuCBb7QGVHlsRv9_Fy8UPLhAu_ODzD3wiCRDIDDrgWggQh-aNURpBzR81MHg6X4nDNDm8h2XbbEYajI7du0Ru_905i4ZZO-219xfmVV1vSgJdRH78MMto_g1chb6Kz0POVy0JjrM11f5KyiOgp0USGeuApy6QxVMml84wHty8v-1nBA3uykAPQDEoios83PZRjDNG9EcTAX7UkxGSBEbC-_TYBS1jnRCa6qXDwqpGuBs1hRAtMj5I8W2Fo_X6uM1hCkRnIDVJAXK58_f65IA3-55ZgyydZeWDYlm9o6m7R85EMICatDiRuC-NdumgbeuGiqjJhS8JRVXqKk7szZ_n502lLlpNh1_72HdEVKyYKP8NaP1Sfk134FZCRT44qZ4htdH0skx5ai6mGYDBLvzvn7EAto5fsfALrMrpX1KjCJN2VXIdWft0cg2rPbFFyrh5ymSDw7uOYUuHXVy_NU0oqnyLHFB-VFyiV1DzJ1Bf_I9L3dWVIkLd7ppJjeUSJ_-lYACLhq_rsgO-ELU1y6NjOCTwfsIwODbaHslBykb4ecz4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ادامه حملات عادل فردوسی‌پور به قلعه‌نویی: هرکه از "غار" حرف بزند، قابل توجیه است؛ به جز آن کسی که کل جنگ را در دبی و ویلای آلانیا گذرانده باشد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/136241" target="_blank">📅 21:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136240">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
پست خداحافظی رضا شکاری با چاشنی ناراحتی: خداحافظی همیشه تلخ است، خداحافظی از گوهر کمیابی مثل پرسپولیس تلخ‌تر...
📍
موفق باشی
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/136240" target="_blank">📅 21:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136239">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❗️
قدوسی: ابوالفضل رزاق‌پور گزینه اول جانشینی میلاد محمدی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/136239" target="_blank">📅 21:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136238">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✅
✅
عادل فردوسی پور :
🔴
آقای قلعه نویی من و تیمم چه جنگ دوازده روزه چه در این جنگ تماما داخل تهران بودیم و تکون نخوردیم ولی شمایی که یا تمام جنگ یا امارات بودی یا توی ویلای شخصیت داخل ترکیه حرف از غار بیرون اومدن نزن. من تماما کنار مردمم بودم ولی شما همش توی…</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/136238" target="_blank">📅 21:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136237">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❗️
واکنش قلعه نویی به تصویر ساعتش در جام جهانی که باعث حاشیه شد :
🔴
اگر یک سرمربی ساعت می بندد و لباس خوب می پوشد که اشکالی ندارد/ اگر من زنجیر طلا می انداختم و یقه پیراهنم را باز می گذاشتم آدم خوبی بودم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/136237" target="_blank">📅 21:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136235">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
افشاگری خداداد عزیزی از امکانات تیم ملی قبل از جام جهانی:
❗️
به من گفتند بهترین امکانات رو داشتن، شما اگر از امکانات آمریکا انتقاد دارید در کاخ سفید جلسه میگذاشتید والا، 15 روز قبل از مسابقات 400 میلیارد بودجه گرفتید، 1000 میلیارد از رئیس‌جمهور درخواست…</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/136235" target="_blank">📅 21:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136234">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9106b20ac9.mp4?token=RUKHi0FoqgpeCcTh7V1-IeXPf_De7pbPh0hZr0UjNZtT0HJ76i6ydh71DMNsyxiHfEgPp8gxXgubIYbOD0oP72YINMl6Ba20Qqjm47pPQHFjNImwyks2YkNB6rAj6Mau1Mvmcy__z0UvnopUaAUoQmfAK3bq5NVeriGf6Z0fb0ED3DjUzLP3cKO5-_0wVSp657SDeHDrjhS9mHmy3th0lWwEjFp7d2M6Lgj_JXrV7QfXQmIudSX9N6ALJ3dlTufaJXz4lFIOlI9UchexiazwaqRBdFIdHNQ_9rpCaQUKy2vbiKdCdJJPZD-aK842V0yH9rA2ckRfkxMZfiqcfbAo3CY8BhMyVhTYDSlWXBsKo4TNaTo4hjO3fEyRdHvWaQPcv-2sEUZ9e_WnoYNS03zc1vsarBbCfrc-NmVHd_1uXNKs29WK0C3W6-QGB8qRGP3tFZfiZffbC7xnTSeL_i1Yl1skerTlegTY-y9EbmkevmUPciw_x_j_h0npR2vyaIQz5I76zCa12JkaZ8fR8YsW3CLP06gWUF7e0-iRAfLqc9WxU0kqG7iP6sgQFBEZmr4-BEUj47Q3t3ePVRT9fh5-1ONIkLQcukX4x6H8h8mqadDD173gbZfLpTaQ0EJDwFr0_FZJnH4IkRfkbxLykna48GFdHeXHwMMqP-OP-NH_2i8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9106b20ac9.mp4?token=RUKHi0FoqgpeCcTh7V1-IeXPf_De7pbPh0hZr0UjNZtT0HJ76i6ydh71DMNsyxiHfEgPp8gxXgubIYbOD0oP72YINMl6Ba20Qqjm47pPQHFjNImwyks2YkNB6rAj6Mau1Mvmcy__z0UvnopUaAUoQmfAK3bq5NVeriGf6Z0fb0ED3DjUzLP3cKO5-_0wVSp657SDeHDrjhS9mHmy3th0lWwEjFp7d2M6Lgj_JXrV7QfXQmIudSX9N6ALJ3dlTufaJXz4lFIOlI9UchexiazwaqRBdFIdHNQ_9rpCaQUKy2vbiKdCdJJPZD-aK842V0yH9rA2ckRfkxMZfiqcfbAo3CY8BhMyVhTYDSlWXBsKo4TNaTo4hjO3fEyRdHvWaQPcv-2sEUZ9e_WnoYNS03zc1vsarBbCfrc-NmVHd_1uXNKs29WK0C3W6-QGB8qRGP3tFZfiZffbC7xnTSeL_i1Yl1skerTlegTY-y9EbmkevmUPciw_x_j_h0npR2vyaIQz5I76zCa12JkaZ8fR8YsW3CLP06gWUF7e0-iRAfLqc9WxU0kqG7iP6sgQFBEZmr4-BEUj47Q3t3ePVRT9fh5-1ONIkLQcukX4x6H8h8mqadDD173gbZfLpTaQ0EJDwFr0_FZJnH4IkRfkbxLykna48GFdHeXHwMMqP-OP-NH_2i8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
افشاگری خداداد عزیزی از امکانات تیم ملی قبل از جام جهانی:
❗️
به من گفتند بهترین امکانات رو داشتن، شما اگر از امکانات آمریکا انتقاد دارید در کاخ سفید جلسه میگذاشتید والا، 15 روز قبل از مسابقات 400 میلیارد بودجه گرفتید، 1000 میلیارد از رئیس‌جمهور درخواست پول کردین و چجوریه که فقط می‌نالید و ما رو سیبل می‌کنین؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/136234" target="_blank">📅 21:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136233">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cce783d5f.mp4?token=YnktUPyg-qMqTNhzb4E5zLJC_hhqNxw3CcbzqeY4u5Fh3nd7R4U5fGk6PwULOXeaQ6YJgY45ruU4i_2BA90Rx-PJMBwuazh4x2DKqfBW_qeWL0ajhZ4AoZMdVsv_MywN-kLjf3OwS88EBdQgif8vReCDxy6xy0YH4FkUUC71G36iAFNNjuq2jA60SSK3S6wSdKXrgKxH0o90PcbCGiX9zA-9WzaO7yZknQf4gHNcm6nm-EFE_Gw7O_z3KgxKteLmXJ1XCkcimRRTQ0e6LcSSQOh1NHDWKJPLWavxmxbXjVNrP0yg5ttZ9YFlue0VRVlEi07m_INL7xaqoMdcUumUH3X5KrTXSbAxYch2aM07CnAjRO3HKl1OLlpNqtMdlD9nRHMtkZRAwqgMTLIq3MjMH9q-pyMJDsbPfZs3PSpw_h9e-JaCf5Hco8QqoeedN5tbOFljSb-PRNBTs1DE2MyB9GvaMg5JOxTjf0y3pJmD-UcmhDep2mTZRDHNr-BhIVkk00D-Rf_CaZ3kNJ4SSiA_MvxGbWmHNKGFAWBYGQuTckbqtUo9hfYnAafpV70ztp5ZjvTKba313HWdx7RjKRert1SQSA1WBJ9-zsjax7mAxEdo7-HhO3ASZmrQUVnDOSTq7dyVvMdpZ7KjQzEaClEPenaiqALGNaNiZZPHvgE5zRk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cce783d5f.mp4?token=YnktUPyg-qMqTNhzb4E5zLJC_hhqNxw3CcbzqeY4u5Fh3nd7R4U5fGk6PwULOXeaQ6YJgY45ruU4i_2BA90Rx-PJMBwuazh4x2DKqfBW_qeWL0ajhZ4AoZMdVsv_MywN-kLjf3OwS88EBdQgif8vReCDxy6xy0YH4FkUUC71G36iAFNNjuq2jA60SSK3S6wSdKXrgKxH0o90PcbCGiX9zA-9WzaO7yZknQf4gHNcm6nm-EFE_Gw7O_z3KgxKteLmXJ1XCkcimRRTQ0e6LcSSQOh1NHDWKJPLWavxmxbXjVNrP0yg5ttZ9YFlue0VRVlEi07m_INL7xaqoMdcUumUH3X5KrTXSbAxYch2aM07CnAjRO3HKl1OLlpNqtMdlD9nRHMtkZRAwqgMTLIq3MjMH9q-pyMJDsbPfZs3PSpw_h9e-JaCf5Hco8QqoeedN5tbOFljSb-PRNBTs1DE2MyB9GvaMg5JOxTjf0y3pJmD-UcmhDep2mTZRDHNr-BhIVkk00D-Rf_CaZ3kNJ4SSiA_MvxGbWmHNKGFAWBYGQuTckbqtUo9hfYnAafpV70ztp5ZjvTKba313HWdx7RjKRert1SQSA1WBJ9-zsjax7mAxEdo7-HhO3ASZmrQUVnDOSTq7dyVvMdpZ7KjQzEaClEPenaiqALGNaNiZZPHvgE5zRk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
خداداد عزیزی: صداها را نمی‌توان خاموش کرد، مردم ایران غارنشین نیستند، آقای قلعه‌نویی ما جنگ رو دیدیم، بهترین کار این است اسم ببرید، شما نتیجه نگرفتی چرا میندازی گردن ما گردن رسانه؟ تنها جمله درست شما در مصاحبه عذرخواهی از مردم بود، دوباره در جام ملت‌ ها من طاقت عذرخواهی ندارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/136233" target="_blank">📅 21:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136232">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
🔴
🔴
فوری| وزارت خارجه قطر: پیشنهاد جدید آتش‌بس را برای ایران و آمریکا فرستادیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/136232" target="_blank">📅 21:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136231">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
🔴
🔴
فوری| وزارت خارجه قطر: پیشنهاد جدید آتش‌بس را برای ایران و آمریکا فرستادیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/136231" target="_blank">📅 20:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136230">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6549a463.mp4?token=mDMLgKlAs4tgde3FlE-E4HugqLUek-T49wZy9YcNmk0BSiW0Q1uxRcOfTqVxDqWwFRPyJFC0vOOtNdX8SnrDI4oby4R1oASklrKGcphY3q7scm5qfvSVebc_xN3fv7mSw_BTmyXOIws5-5y2ESz5XmMrgSBxGO5sQIpqS8GUofB_gsTOB8bkXB8U_oH7sHvc-KVwKQUXuoLJR0OgF1gF3v-1y-p1z8epSo2_YzlumL5yQ_VlbwNctYza3YO2Kbptu0wm-eH15lfDiS-vGi3GIkGoLP46UIF9Udy1gGnrvq3YL82CrBWAV3zQlowuBIOv5bFpCaKQvBg-JEV8MIrmMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6549a463.mp4?token=mDMLgKlAs4tgde3FlE-E4HugqLUek-T49wZy9YcNmk0BSiW0Q1uxRcOfTqVxDqWwFRPyJFC0vOOtNdX8SnrDI4oby4R1oASklrKGcphY3q7scm5qfvSVebc_xN3fv7mSw_BTmyXOIws5-5y2ESz5XmMrgSBxGO5sQIpqS8GUofB_gsTOB8bkXB8U_oH7sHvc-KVwKQUXuoLJR0OgF1gF3v-1y-p1z8epSo2_YzlumL5yQ_VlbwNctYza3YO2Kbptu0wm-eH15lfDiS-vGi3GIkGoLP46UIF9Udy1gGnrvq3YL82CrBWAV3zQlowuBIOv5bFpCaKQvBg-JEV8MIrmMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله شدید‌اللحن خداداد عزیزی به قلعه‌نویی: شما فرشته ما شیطان؛ شما خوب ما بد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/136230" target="_blank">📅 20:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136229">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❗️
❗️
فوووووووری/ارتش آمریکا در پاسخ به نقض آتش بس از سوی ایران، اهدافی را در جنوب ایران هدف قرار داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/136229" target="_blank">📅 20:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136228">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8fJRELEfescmd24xtoz-ktCOmplURxFgP600K6sh4-AcPVUI5fXO1IpsuLKrO4OJR0P65DG5FTRBp23K8bbSSsB_lqlvy80ZvSN8JJao-B-ySqs0jGFgJFtYDulIKoDbX6awcthnqJjrTIbnMatqTDJbV0gAwThCvtSW_8mn0uTf6W3KneSA7STEsjY3grJ41rAH20i6_1IDHMA3ojhaBS8beCNyggqBevCRc7KYktvK8nPDNLg2buIPa4zfJKDq6thu_-FVWajknsSbSVeDijLmYxWk6W4HcSNZ1oxgMa-nc4Njeh0M8qcZudGd4o9bCmcEUMQjQtaFnAcN3Zyhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔖
تصاویری از احد میرزایی عضو هیأت‌مدیره پرسپولیس منتشر شده که داره توی ساختمون باشگاه یکی رو کتک می‌زنه…اقای احمدی همین فردا دکمه ایشون رو بزنید
❌
پرسپولیس چاله میدون نیست، ایشون ادم زنوزیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/136228" target="_blank">📅 20:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136226">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
رقم قرارداد دانیال ایری،‌بالاست، ولی می تواند قرضی به پرسپولیس بیاید. او بند خرید دائمی در نیم فصل دارد و بنظر می آید نساجی مایل به فروش کسری طاهری است. ضمن اینکه جذب علی نعمتی و قریشی هم قبلاً کنسل شده بود
✍
قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/136226" target="_blank">📅 20:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136225">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
#تکمیلی؛ باشگاه‌تراکتورتمام‌توافقات لازم رو باخودِ علی ‌قلی‌زاده برای قراردادی سه ساله داشته و تنها رضایت نامه این بازیکن باقی مانده که مالک تیم تراکتور قول داده ظرف 48 ساعت آینده مبلغ توافق شده رو به حساب باشگاه لهستانی پرداخت کند.
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/136225" target="_blank">📅 20:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136224">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
❌
باشگاه تراکتور مذاکرات مثبتی با علی قلی‌زاده، ستاره ۲۹ ساله لهستانی، انجام داده. او قرار است ۷۰۰ هزار دلار به عنوان رضایت‌نامه به باشگاه لهستانی پرداخت کند و سپس به صورت رسمی به تراکتور بپیوندد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/136224" target="_blank">📅 20:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136221">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
❌
باشگاه تراکتور مذاکرات مثبتی با علی قلی‌زاده، ستاره ۲۹ ساله لهستانی، انجام داده. او قرار است ۷۰۰ هزار دلار به عنوان رضایت‌نامه به باشگاه لهستانی پرداخت کند و سپس به صورت رسمی به تراکتور بپیوندد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/136221" target="_blank">📅 20:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136220">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
❌
باشگاه تراکتور مذاکرات مثبتی با علی قلی‌زاده، ستاره ۲۹ ساله لهستانی، انجام داده. او قرار است ۷۰۰ هزار دلار به عنوان رضایت‌نامه به باشگاه لهستانی پرداخت کند و سپس به صورت رسمی به تراکتور بپیوندد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/136220" target="_blank">📅 20:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136218">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47bce486c0.mp4?token=eegFPo4bUz8Ado3WCfqvmDUPBzfSyXktil4KIe7xPkmkAVJvuF5-rdnOGEljo58TcPAVIe333X82deEX6Z2d8hAl-hr-Ka5zX2iCVIh-XNkE_dTqebDLld6pJOouY_B4Rz-xnoXa_QB2XXXnnOd64M67siScxq9n4AkIAHk8K0x-fjaokw7BOIPrRKLLor893LphHQOBg5GLTah7e1m7E36A60VgYVIayGu0NnL7-caq_AXvj9sfUtWpAbAAgW0B-LHuYftuQdyaIwPUwYtV7slKg_XAOBTZZF8xR3DNvTLzaWMlbKB7903BdcCKlYCdk37Mqdb_YCt332dpr2cwMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47bce486c0.mp4?token=eegFPo4bUz8Ado3WCfqvmDUPBzfSyXktil4KIe7xPkmkAVJvuF5-rdnOGEljo58TcPAVIe333X82deEX6Z2d8hAl-hr-Ka5zX2iCVIh-XNkE_dTqebDLld6pJOouY_B4Rz-xnoXa_QB2XXXnnOd64M67siScxq9n4AkIAHk8K0x-fjaokw7BOIPrRKLLor893LphHQOBg5GLTah7e1m7E36A60VgYVIayGu0NnL7-caq_AXvj9sfUtWpAbAAgW0B-LHuYftuQdyaIwPUwYtV7slKg_XAOBTZZF8xR3DNvTLzaWMlbKB7903BdcCKlYCdk37Mqdb_YCt332dpr2cwMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
واکنش قلعه نویی به تصویر ساعتش در جام جهانی که باعث حاشیه شد :
🔴
اگر یک سرمربی ساعت می بندد و لباس خوب می پوشد که اشکالی ندارد/ اگر من زنجیر طلا می انداختم و یقه پیراهنم را باز می گذاشتم آدم خوبی بودم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/136218" target="_blank">📅 20:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136217">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✅
تصویری از خانه دروازه بان کیپ ورد...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/136217" target="_blank">📅 19:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136216">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✅
شنیده ها :دو تا از بازیکنان ملی پوش و با تجربه پرسپولیس با سامان قدوس تماس گرفته و در تلاش هستند که او به پیشنهاد باشگاه پاسخ مثبت بدهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/136216" target="_blank">📅 19:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136215">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0UtvnVXx_GmQvnhn384MIzprw3_LjwgBXEk7DvvosU1z8PWWYCxWK-FtJ2kxlId0Y95Bxe1axvkr1qEfm_preH8pEp26kzDWMB7ZZW6HM13WYlx-UCQt8QmoL0K7uLbeMRuA2uFraJ4tG1NLGKm-FqqA5G663c4MzaiAZpSk1BlHG8mIYx4mt_PuEmbjWRdx3XU9SycL8uQgXW2VXLiztiZdZKdyOTMQjcxpuuuVCVq55LYUOts0hSYOnszXCS2BGmDgrPl3euOucvwcl_bwG7Z2zNRZkGSCHE7jc9Ame3Q8kRUv_YIQlFPsO8JkqH029yfYSfqqqoVJFm0KgbM1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
❗️
یه سری عکس منتشر شده که نشون میده احد میرزایی، عضو هیأت‌مدیره پرسپولیس، با یه نفر درگیر شده و باهاش گلاویز شده. ظاهراً این اتفاق مربوط به گذشته‌ست، ولی بازم خیلی‌ها معتقدن برای یه مدیر باشگاه پرسپولیس چنین رفتاری عجیب و قابل انتقاده.
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/136215" target="_blank">📅 19:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136214">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
مذاکرات پرسپولیس با احمد نور پیشرفت خوبی داشته و درحال حاضر تنها مورد رضایت نامه ۸۰۰ هزار دلاری این بازیکن است که باشگاه پرسپولیس تلاش داره کمش کنه /ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/136214" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136212">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
🔴
مذاکرات کوشکی با استقلال مثبت نبوده و پرسپولیس و یه باشگاه لهستانی مشتری او هستن/ورزش‌سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/136212" target="_blank">📅 19:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136211">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a174835238.mp4?token=RXnw5GbvdLRRydRkQMmt-YF40aBgjf8iVnVn311ghr3MjERAG3hUMRJrHyfLlYpq7zG_qogx-zTAGHVXYHDAf1LnfBhRTpXDsgAEL7O26D6R14yK2iUr6rTXZdNiolNVGE8Zsc_if1G0nBAsuBCXuFuEKcU2jxgZRdR31YySTMoAJXT8ZuITrJ2OLrgnioV2q5UlQY-oIOB3CGhNRR47gSRd71jxGbznf-y83aECxIO-UuEQfAaz-0Odlx6PxReS-FlKCfmvZd4l-kAfrbmQ-pdMFSEzUw8lYDpscGDzfwZxNjkb-pghJyoAeYgBL09dozii3-jG82nZpFToR6RWXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a174835238.mp4?token=RXnw5GbvdLRRydRkQMmt-YF40aBgjf8iVnVn311ghr3MjERAG3hUMRJrHyfLlYpq7zG_qogx-zTAGHVXYHDAf1LnfBhRTpXDsgAEL7O26D6R14yK2iUr6rTXZdNiolNVGE8Zsc_if1G0nBAsuBCXuFuEKcU2jxgZRdR31YySTMoAJXT8ZuITrJ2OLrgnioV2q5UlQY-oIOB3CGhNRR47gSRd71jxGbznf-y83aECxIO-UuEQfAaz-0Odlx6PxReS-FlKCfmvZd4l-kAfrbmQ-pdMFSEzUw8lYDpscGDzfwZxNjkb-pghJyoAeYgBL09dozii3-jG82nZpFToR6RWXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
فوووووووووووووری
⏺
سپاه پاسداران به یکی از نیروگاه های بزرگ برق کویت حمله کرد
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/136211" target="_blank">📅 19:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136210">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
❤️
🤩
طرفداری: احد میرزایی بزودی توسط مالک بانک شهر به سمت درب خروج هدایت خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/136210" target="_blank">📅 18:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136209">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eda321934.mp4?token=LzEXsJnTTgJAcudx4bOUVpBcdphN46-BDzGLgRlmFww4K2jr-anF-8JnEwHnhfBLUXwvqG-C0Ty7QslcBB6WgqFaIna1tW1OB8nAiJX_E8DQpecWwqZZWjatEkmil4DUi86GvlpP0Yta6GdnWmDUdK5uPVWpWpWPEi1ruMZAKIqRN6ql3gkghyDsmBnJ2zKOooZz6sk3eczQReBMr-Ao8WhLF1SAiSbcq11cMaXhjyWsrUE8jF0wZA3wF-6LLVHErfYt6C8vDJneq4M-a5637zfueeLUoEA1g3NhdnMBdwW2TGNpirAD2tDe0_IUOHEyH0SPn-XIEfxSow_OW5UpKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eda321934.mp4?token=LzEXsJnTTgJAcudx4bOUVpBcdphN46-BDzGLgRlmFww4K2jr-anF-8JnEwHnhfBLUXwvqG-C0Ty7QslcBB6WgqFaIna1tW1OB8nAiJX_E8DQpecWwqZZWjatEkmil4DUi86GvlpP0Yta6GdnWmDUdK5uPVWpWpWPEi1ruMZAKIqRN6ql3gkghyDsmBnJ2zKOooZz6sk3eczQReBMr-Ao8WhLF1SAiSbcq11cMaXhjyWsrUE8jF0wZA3wF-6LLVHErfYt6C8vDJneq4M-a5637zfueeLUoEA1g3NhdnMBdwW2TGNpirAD2tDe0_IUOHEyH0SPn-XIEfxSow_OW5UpKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
رسانه های استقلالی: روزبه چشمی در مذاکرتش برای تمدید قرارداد با باشگاه استقلال به مدیران این تیم اعلام کرده است که از پرسپولیس پیشنهاد دارم تا رقم قراردادش را بالاتر ببرند
😆
😆
😆
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/136209" target="_blank">📅 18:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136208">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">💢
کاظمیان + رفیعی میرن گل‌گهر پوریا لطیفی فر میاد پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/136208" target="_blank">📅 18:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136207">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
میلاد محمدی در یک غافلگیری با عقد قراردادی یک و نیم ساله به  مکس لاین ویتبسک بلاروس پیوست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/136207" target="_blank">📅 18:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136206">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❗️
قدوسی: ابوالفضل رزاق‌پور گزینه اول جانشینی میلاد محمدی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/136206" target="_blank">📅 18:26 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
