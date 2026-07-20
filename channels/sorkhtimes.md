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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 20:21:39</div>
<hr>

<div class="tg-post" id="msg-136324">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/SorkhTimes/136324" target="_blank">📅 20:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136323">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
❌
تمام تمرکز پرسپولیس روی جذب محبیه و خیلی هم بهش نزدیکن ولی  اگه اوکی نشه کاظمیان میمونه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/SorkhTimes/136323" target="_blank">📅 19:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136322">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
شنیده ها:پرسپولیس مقدمات لازم برای مذاکره با محبی رو شروع کرده و این مذاکرات در حال پیشرفته
🚨
جذب محبی نیاز به رضایتنامه باشگاه اماراتی داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/SorkhTimes/136322" target="_blank">📅 19:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136321">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/SorkhTimes/136321" target="_blank">📅 19:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136320">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❗️
سپاهان به پرسپولیس اعلام کرد هیچ‌جوره آریا یوسفی رو نمیفروشه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/SorkhTimes/136320" target="_blank">📅 19:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136319">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
محمدحسین میساکی: درحال حاضر کسرا طاهری رسماً بازیکن نساجی است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/SorkhTimes/136319" target="_blank">📅 19:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136318">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
فرهیختگان:
🔴
تارتار یه وینگر تکنیکی می‌خواست، اما بعد از مذاکرات با یوسفی، هاشم‌نژاد، لیموچی، کوشکی و چند گزینه دیگه، مدیران پرسپولیس به این نتیجه رسیدن که محمدامین کاظمیان رو حفظ کنن و روی خودش حساب باز کنن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SorkhTimes/136318" target="_blank">📅 18:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136317">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❗️
فوووووووووری از حسین قهار
🔴
حسین قهار: هدف از مازاد کردن ابرقویی ؛ بازگشت مرتضی پورعلی گنجی به پرسپولیس است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SorkhTimes/136317" target="_blank">📅 18:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136316">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
❌
تارتار از عملکرد حسین ابرقویی در تمرینات راضی نیست و به دنبال انتخاب جایگزین برای این بازیکن است‌...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SorkhTimes/136316" target="_blank">📅 18:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136315">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✅
✅
#فووووووووووری
🔴
تارتار علاوه بر پورعلی‌گنجی، برای حسین ابرقویی نیز اعلام عدم نیاز کرده و‌ معتقد است این بازیکن در ضد حملات حریف کند عمل می‌کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/136315" target="_blank">📅 17:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136314">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
❌
فوتبالی: مهدی تارتار به اخباری قول داده اگر توی تمرینات بهتر از پیام نیازمند باشه، فیکس پرسپولیس می‌شود. همین اعتماد به قول تارتار یکی از دلایل اصلی قبول پیشنهاد پرسپولیس بوده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SorkhTimes/136314" target="_blank">📅 17:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136313">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✅
شهریار مغانلو به تراکتور پیوست
🚩
خط حمله تراکتور برای فصل بعد ؛
🔖
هاشم نژاد
🔖
ترابی
🔖
حسین زاده
🔖
اشترکالی
🔖
مغانلو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/136313" target="_blank">📅 17:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136312">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/136312" target="_blank">📅 16:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136311">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
محمد عمری 3 ساله با پرسپولیس تمدید کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/136311" target="_blank">📅 16:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136310">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
شنیده ها:پرسپولیس امروز 40 میلیارد تومن + رضایت نامه قطعی کاظمیان رو به فولاد برای جذب ابوالفضل رزاق پور پیشنهاد داده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/136310" target="_blank">📅 16:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136309">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLh7MJB9g_PSjHpJX3dgNDr4gWs6TkeRJZWKjiQ_MKqSdpxvEeGC863oZY6bIyZe7XD88VGoNMAeC0AjCl0SBDaEWlj-x52vjazNpCsrluKR3GRZjC98GZ-xhIgGNHnGl7xn6J1Vb2taxg3Q35TYk0mZIOtNP-X7pytM6WIC4ZiueiSX7ane0auIme83eYAgrA4qqL7CDOUXspGa4fKAQHrzT7YJFP4b2Nr7jQEqFOKNMgmYoMiYwcLF-6-nWGZq1rfxyPo6shRVlwyl_04-TUdI7Leeyvt4Kz4Ir_gC4lAloz-tRKCKhtotj1x_WbzYFO7r2cr_ohwUUqOAd6-WxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محمد عمری 3 ساله با پرسپولیس تمدید کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/136309" target="_blank">📅 16:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136308">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❗️
❗️
پرسپولیس برای رزاق پور پیشنهاد پول به علاوه بازیکن به فولاد داده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/136308" target="_blank">📅 15:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136307">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
شنیده ها:پرسپولیس مقدمات لازم برای مذاکره با محبی رو شروع کرده و این مذاکرات در حال پیشرفته
🚨
جذب محبی نیاز به رضایتنامه باشگاه اماراتی داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/136307" target="_blank">📅 15:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136306">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
❌
فیفا ظرف72ساعت آینده استعلام باشگاه‌پرسپولیس‌ونساجی رومیدهد. اگه پاسخ مثبت باشه کسری طاهری بزودی با عقدقراردادی چهار ساله رسما به عضویت باشگاه پرسپولیس درخواهد آمد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/136306" target="_blank">📅 15:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136305">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❗️
❗️
دوره حضور وحید امیری در پرسپولیس برای همیشه به پایان رسید و او از جمع سرخپوشان جدا شد
🔴
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/136305" target="_blank">📅 15:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136304">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❗️
مذاکرات برای جذب محمدرضا اخباری وارد مراحل پایانی شده و باشگاه منتظر حضور این بازیکن در تهران برای عقد قرارداد است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/136304" target="_blank">📅 15:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136302">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/136302" target="_blank">📅 15:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136301">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/136301" target="_blank">📅 14:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136300">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/136300" target="_blank">📅 14:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136299">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
❌
تیم پرسپولیس که قصد داشت فردا برای اردوی اماده‌سازی راهی شهر ارزروم ترکیه شود، با یک هفته تاخیر اردوی خارجی خود را برگزار خواهد کرد.
🔴
🔴
پرسپولیس روز ۳۱ تیر ماه برای این اردو تهران را به مقصد ارزروم ترک خواهد کرد و احتمالا دو هفته‌ای در این اردوی خارجی حضور…</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/136299" target="_blank">📅 14:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136298">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
❌
باشگاه تراکتور مذاکرات مثبتی با علی قلی‌زاده، ستاره ۲۹ ساله لهستانی، انجام داده. او قرار است ۷۰۰ هزار دلار به عنوان رضایت‌نامه به باشگاه لهستانی پرداخت کند و سپس به صورت رسمی به تراکتور بپیوندد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/136298" target="_blank">📅 13:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136297">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrNJLoh0TWga3oeFR1NpLbZDi2jnmv2pjaVDD26sYaVK5yYNBAST-aJGmTyjCObBbmPKsnqzalOdoJ_aCDjDfTyqiLSWiCJVzuXFe7yyyw0mDrrzocGxS5X47PjdFTsQqSXOhN-V0G9Vo4t88p6bsXkGRqqbj5Bm8i9dfNZZYahEllSqPoxv3hNXhMlL7VgHpQwpII7nOQmh_KOPrx4qu6bGCBhLurV8gG7S-nYhgzQMt-0ZQ4giDAPVx4Y_eu6TIML-1uoSdvTiTJ002xvzcX2qyGrc-52G_kbDr5qJ2D9lRH9cylj9RE0vli8yNlYAAGqsE9Y3e-p3laHxSB6MFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/136297" target="_blank">📅 11:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136296">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❗️
❗️
پرسپولیس در یک دیدار تدارکاتی روز سه شنبه هفته جاری به مصاف تیم خیبر خرم آباد خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/136296" target="_blank">📅 11:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136295">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSOo0LKZGlEsplVOd-aB1yH5BUwxvrybX_nmAIQm6lHHszQvVnOv2l1iskdW4CbMQUsKb-900S-dmOkaYGdyTIoCN3zhl9FPOmVpmdVzH2DvabLxYU-sgO2x2SLHjpAO6-E8GjgLkkBthtI5Dqo1wZvq72wnGJChvoJjkZaH6haC-rv-JxMzhjty79shESHjPqbtN978-w7ZfStoUbzkTYaTTVuW1G_RJEJAY5xFktEMjSBDWL8cLrRshYoXNepR8QrGm-ZNFCt1QDDHCP6Hqr5C0bkYWmX06-q-njNT-wDt_NbZ_Hksr6V2xgAJUgISV5AdcoOZw0Bhs9yIVPHwQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رامین رضاییان از ایران با دو گل و یک پاس گل به عنوان سی‌ و هفتمین بازیکن برتر جام جهانی انتخاب شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/136295" target="_blank">📅 11:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136294">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✅
گویا دوره حضور تمرینی وحید امیری در تمرینات پرسپولیس به سر آمد.
🔴
احتمالا از فردا دیگر به تمرینات تیم نمی آید//طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/136294" target="_blank">📅 11:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136293">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/136293" target="_blank">📅 11:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136292">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
❌
پرسپولیس دو پیشنهاد خارجی برای امیرحسین محمودی رو رد کرده و می‌خواد فعلاً نگهش داره. درخواست شماره ۱۰ هم با مخالفت تارتار روبه‌رو شده تا فشار کمتری روی این بازیکن جوون باشه.
🔴
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/136292" target="_blank">📅 09:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136291">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mosUJmZYMGDJrxp7YaeoSbvqh5eCWlog2NIOJ7f7i-7_kO7xx8d8GxrXQ-29CHEnULx-F2AvyFD8BIAiprnNE9-aHUZwHdv9CAOyTcVtwS0WA_6s1-69m0rLDlSoJW5S5XyEHp3m7O5TB-WwVYy1ytSo6riAM4I7FJwLNKoRX03y5_5wnfgWJi1MOpjfsr6u9B5eD-xxhsNuMx_Y9_F71gJxVJFDWZhlQvtoe5lUqq93d2LhBIVGPznFHvCAyl_DAQN3RVIDdwA-4CEqJKTJNzN38fyBMReWVfoQFBZDIZJLYUjOs9GczJ6IcYMmQVbDQa-afDCMqp-kff_Q2LRd3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/136291" target="_blank">📅 09:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136290">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uns-T9Bopckmb4OdNh-eqw3UfKDLmWsgE0b-ElomGO4Q46uPJxW31S4gb0Hto2LWiGfTVO8oVhvDRUHGU3mm5MNZtv2gX0S4VV5s7YgyJrM9RrH5gDvpBARiSjen3psKWkDPpD0P2cRILyAjlo0Ovc-zTC_ZcD-o9l8VZALz8Z0w5n7uRcrsDoNfqeyE1uU9W9TX5In-GmoWKLQUKp7GWmzJLRMKxv1N6Hoc1BxhE5LaihGEsrA2pU0DS3NQNTMyiFR-Wr3lfigO5f9t4ko5lAL3L-ttiDp71265GxtOEQG62bdRhx5Yv2zAuR0eno-WnKmNMp6TaaGgxTsipc3dVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
چه قابی شد ...
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/136290" target="_blank">📅 09:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136289">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrR47sgCs2KxMsgALUBEgVDzBBR87IMm2MtjMvvhn6ulKUcCT-hB47RYt3E1jNvu2GOJ6vXQxjMZVOirai3AUyKD-a16_9lfgLO1BSQ0lfJ04Gv2vvDcpBQOh5r5aUWlRcxPcPZknHy79qRU5VZ4LW_aGAWTd7dYj7ti-5TdDdbDFjQd4i95-YZnenzwaL-_DeKtgH07Wel6Grl3utx5_D6jLnu4R1rzNfUj6mGtI6BbbzNxuA8j3PJ8mIha0Aro7xKLZea6wNl7IvXwQFd23ZfPPEyR_y5y7AX5J6HNPHSC3QwXrp6C0gsxlRdIV-PoDdltut0SsKGpwjX5AVMPUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دو زلزله به بزرگی و شدید ۵.۷ و ۵.۲ در کورزان کرمانشاه به فاصله ۵ دقیقه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/136289" target="_blank">📅 09:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136288">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✅
گویا حملات بسیار بسیار شدیدی دیشب به تبریز شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/136288" target="_blank">📅 09:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136287">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
❌
فاکس نیوز: هروقت داور بازی سوت پایان بازی اسپانیا و ارژانتین رو به صدا در بیاره جنگ علیه ایران اغاز خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/136287" target="_blank">📅 09:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136286">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
❌
ورزش سه: محرم نویدکیا رسما خواهان جذب ابرقویی و کاظمیان شده در این بین گفته میشه احتمال معاوضه این دو بازیکن با آریا یوسفی در قبال مبلغی هم وجود داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/136286" target="_blank">📅 09:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136285">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇪🇸
🏆
بالا رفتن جام قهرمانی توسط اسپانیا
💢
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/136285" target="_blank">📅 09:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136284">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/136284" target="_blank">📅 08:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136283">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/136283" target="_blank">📅 02:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136282">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/136282" target="_blank">📅 02:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136281">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWDRK_b3AkLcgf0-zhEpg3qZq3ZSzkxo5GqrJcO280WbiLNeBglyH7yI41fu6-awEzKs2gxOhbMdBPdaJ9CkbnwS_0d-FhJem1sYMzjb1VPyrjWhoHkmYlNS6k-58xhQRu_WnIFlGBFrrEBskRM2zxj_vSoEc7Ewys1Pk_dKO8IcnH0PmvUxSJKPWxxwCEN41HPulmA37qSyHZ0ngHF09mli65Ha3nQ_5LTGFKGZYQEqmbu-qmY5HcmYsy-sgtAngBAOBj1Ls7wVc_1mLAjMQLllE2IxTCUTQJMMcKWi8dN9qg87U2qBlA0r5rzU0MGWFXQa2KkuU2IltIJnOY0BGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏆
بالا رفتن جام قهرمانی توسط اسپانیا
💢
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/136281" target="_blank">📅 02:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136280">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⚽
فیروز کریمی: مسی الکی داره گریه می‌کنه چون دید رونالدو گریه کرد وایرال شد
👎
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/136280" target="_blank">📅 02:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136279">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTB6pw4EWUqnU4GEu9i2us8VLkIzMUYlnUd2mmihh8ZZqKMmOFQb7l_1xTP110SgsmjtvCa0O4P0WZ_ZBJxE2kb652GJ6ePwWD7YsBxXVZK2Cby-4j1ozDv8D8MurPfz-7uuGFmsI92i2F1uwkdsFfpvEdcxc1vvvAqpeK9PCsWdDRZxJEUZxTEpZ93kvvgWhvUxEhyfS_5EjhlQDp9_E5mR74P51wwh1Mw18zdIjkSx0BVSBkBp8EePJ6vDPKF-g3oMD70rImwknYLFqjQybajCiP3FYmw7sz7t3u_Fg6p5xqMSgyGCCp2Av0N3yZfEhzF6fS_QpdB6dSNzmYw_uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
⚽️
سرخیو راموس با کاپ قهرمانی جهان اومد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/136279" target="_blank">📅 02:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136278">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ueypOWUnsGEgLXG3OZXh8xUlPt5sxWWrpyRZ3l4QvNDShBp4aEUneu3Uq4HGdRMNoj02BMx8nuKpU5X12qcY8ZIqqwmIQGKt6GWXzmTxd-zu9onR6IMshjyT11crSY_8KckGUK7mZKpDEciOkqiIGpr0V9-SOGSWwSk998Bv1M0Iziv1eF5vw2ubDCHUYl9orYDQoIxhxpSWeblH2GVlgDJKh2MESRMqhWdM5M_sW6b10Drpq7TMtYR6n7sLcjTFwmo7OhZ9f10m0OwPpGypQN03eXBgBN4NRlSCPlwl00JS_o4MOG988-N9DG6Zvk50waxglrzVx8XKn06Xgo1oiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
💀
گریه‌های مسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/136278" target="_blank">📅 02:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136277">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/136277" target="_blank">📅 02:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136276">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/136276" target="_blank">📅 01:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136275">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/136275" target="_blank">📅 01:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136274">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4lLlkjgWFA3eVRRlyUSnpLyj5ms4lOC0OfZNmVkQNxl9MUs0zjx03RQmvoeFZjN0S-wenbAOICiTlYDNLMFLXsYqdiEsIAgGfu-jNhMlspqMVfrt-8_v4xIbvzvHqi1HzIqm--plI1GgDPu6buF7pJiiC3cPrfqO5EsJM-jYBUfFGkzNEfwfJV8ccdDRmWEeaOvR6wPULh9kObmYGr-8ujG-5Dq0IcWyGZrqIGjeQEXpv_8I685jSXq9nd6w6vdTW_x1Iq7XH_T-gcJ-nUrIxLBJ8paZCEZPNfamjJ-qLVfPlVi7dG_a63U8IpE4Rz-iD7H2QOB3NQ1XD8NkiNDUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
عکسوووو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/136274" target="_blank">📅 01:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136273">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJ_M5zUZILfVCSZHsaVbmi6GlKh82I1YDnvke4XKswzft5n-eBpKvELwy0lJ6_m3rAptQa4wosjB7QihTzEjjlIZJeKhYpfYHf8_JwAJRKR_wrkqWMw0lYSdeVT3elUPO1-GponQiunML77E5GNGaKory4g4Kv59uBeL6MmxsScfIKOQHBKwG2pGJbXYOX-w4bnZMlNPYun7N-nfpOiIf2xLtR4cP_GBvnfpe8jkYnMiQxZ-5wjsNE7qTg84QGsXZdYGZtCfj2_AFT-8ql4PVW6qGDL1OXIX76JQ4mikeBHRaodS2M6cnergm97do4jh9QKhAAfGuMTS5WsOYeKOSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
‼️
کنایه سنگین تونی‌کروس ستاره سابق رئال به آرژانتیی‌ها:فوتبال برنده شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/136273" target="_blank">📅 01:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136272">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHnGi1uDBWHPLrR1hDG3SNxlDzi8JKvANqM9upSaPPJXtdKcZ952YIE-zFgHO6bmOelERFxuhc7UXk2eajKU0wboLwKio2KS6R9UVk7t6JF8Y0TJkTU7fXCEGdz7GwkoFFkqnspSE4FLOG_dO1WsGPTRxmRaueHIxcWKtkqGZWTRSTs4vr1AgOWoVFgSZagbWQbVpIv5N9_QWvIIKH_IY1q6Vnwn2y1D9CXmattaWSDB28Kj1Lig6JcXwzSXpzYbE77mqmYQ-qdBEpClOXYTVeF68DlHJftT-rCvdN3eQ9A19rA0xnH4M4M9bnx4ovwBYvMo8GMGnSVKyMaRUKwlSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
اسپانیا با شایستگی تمام قهرمان جام جهانی 2026 شد‌
🇪🇸
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/136272" target="_blank">📅 01:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136271">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWIQqpgdtgazhJZzloLFzQMoyuq_WLe29lVC70Scqc4kVUjoARTWwJZ_LiExKDK4W2nkk1lLbRCdrdlzVLI9xFA3YRFqUtw1PJFRhusyrg3gGMdrFYhkTtQ07ZMae-Jdb8MFKhhTaC5lprAJ8SyAqfD4MjmQw1P7sCQ2f0sJyHBc3JCXbmNN6dKercRjQtqQpcDdhPpo9PwaRvrr5EGJp25tzMplUZzQNQRvtrYC86QLY1terPGoOSJCa3cSn-zfX8BNWzfwIBcyfby39X3C7FC6kg61tKhbPLcRiFMo2nQ12c-NLcCPeHNuxQYqdv0whE0Pb-LQsT-5XN6w0sVKbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💋
پایان کار مسی با آرژانتین…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/136271" target="_blank">📅 01:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136270">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✅
این بازی فینال که چرت آور و خواب آور و کسل کننده بود با نتیجه مساوی تو نود دقیقه تموم شد و رفت برای وقت اضافه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/136270" target="_blank">📅 01:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136269">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
بازیکنی که کلا محو بوده و خواب بوده تو زمین فقط مسی بوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/136269" target="_blank">📅 00:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136268">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/136268" target="_blank">📅 00:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136267">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">⚽️
اسپورتی تی‌وی: کاپ جام جهانی 6.175 کیلوگرم وزن داره و ارزش مواد به کار رفته توش حدود $713,000 یعنی 140 میلیارد تومن برآورد شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/136267" target="_blank">📅 00:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136266">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❤️
🎥
ویدیویی از تمرین عصر روز گذشته تیم
🔴
از مرور نکات فنی تا اجرای برنامه‌های تمرینی؛ یک جلسه دیگر از آماده‌سازی سرخپوشان زیر نظر کادر فنی.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/136266" target="_blank">📅 00:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136265">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🏆
اجرای کامل مراسم بین دو نیمه فینال جام جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/136265" target="_blank">📅 00:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136264">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
❌
نیمه دوم هم چنگی به دل نمیزنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/136264" target="_blank">📅 00:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136263">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❗️
نیمه اول بازی .بی روح و خواب آور و کسل فینال با نتیجه صفر صفر تمام شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/136263" target="_blank">📅 23:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136262">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99bc7fc060.mp4?token=IX12rdszLxu6VAMnSrnL46DjOIes_pqNUX9ZVulPsSDM9RQVtsQZ3R8DQY1CLoKqIl4H-7tiUXsowRsHa5fpR4V_bznk3UUQwR3w2ET4Rz6L7Q2u0pvWT7Yer6b90uJovnKwwrAfKeo2ZHbBFN9GAtvRFnmz6AxqbevRebi_-M4Lh5wznOBqVcQrz5rSnQDmBpzOylACCXLPvvJTgBVRk1sdClo4SBHti_0Fv-petoYtXfdziDh4n5ejJbNEHVUkEf02UA3AFO9QKrCYVqHuQUqtGz4yBzeoG29ofcrxqjX2AxzuhBDuobj2LWsnPauVp1JdZStxqkjhnKGUa0pVgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99bc7fc060.mp4?token=IX12rdszLxu6VAMnSrnL46DjOIes_pqNUX9ZVulPsSDM9RQVtsQZ3R8DQY1CLoKqIl4H-7tiUXsowRsHa5fpR4V_bznk3UUQwR3w2ET4Rz6L7Q2u0pvWT7Yer6b90uJovnKwwrAfKeo2ZHbBFN9GAtvRFnmz6AxqbevRebi_-M4Lh5wznOBqVcQrz5rSnQDmBpzOylACCXLPvvJTgBVRk1sdClo4SBHti_0Fv-petoYtXfdziDh4n5ejJbNEHVUkEf02UA3AFO9QKrCYVqHuQUqtGz4yBzeoG29ofcrxqjX2AxzuhBDuobj2LWsnPauVp1JdZStxqkjhnKGUa0pVgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اجرای بیژن مرتضوی در کنار ارکستر فیلارمونیک بین نیمه بازی فینال جام جهانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/136262" target="_blank">📅 23:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136261">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✅
با یک چشم بهم زدن جام جهانی 2026 هم داره به اتمام میرسه ...بریم برای بازی فینال ..آرژانتین و اسپانیا ....
🔴
پیش بینی شما چیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/136261" target="_blank">📅 23:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136260">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0tj7WSE_qU5UIqk79pfK9si08uOP-FQvF3zUfS7oGAdnwatO6PRQuj-JCciij3to9fMU6__ia1QFvOCfcuquRc7J5lG0PPsiuj7L7Ro7rain7DTvo4O0Smje4KW-rN2DVSCfhg5bWt1Uk07vM8k_Yx-FApdECTT4wI7Fe87XTg-ZrN5u-YcSruq26XWQ-fC0lOxlSgDu3Egl8Y0Jvy7J00SvkLfGlwo0aCFaDjYAZFXkzhL-k0KYr1U0xltOkBjvPtbc7WAxHWNo1FOCpqJJeMJZBN9aoWltgoDbPvdSfWyaEF8rMkni3wabmv9M8ZRAlXI_0_kTA5Fec4345NEMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یعقوب کافو هم به تمرینات برگشت
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/136260" target="_blank">📅 23:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136259">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
ترامپ از پشت شیشه ضدگلوله بازی امشب را تماشا می‌کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/136259" target="_blank">📅 23:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136258">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✅
✅
#تکمیلی | رویترز:
🔴
ترامپ دستور حمله قدرتمند به ایران را صادر کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/136258" target="_blank">📅 23:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136257">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✅
خیابانی: چرا در ایران کسی معذرت‌خواهی نمی‌کند؟
🔴
واکنش تند خداداد به صحبت‌های امروز امیر قلعه‌نویی
: واقعا خیلی از حرف‌هایش را نفهمیدم. ما لودگی می‌کنیم؟ چرا پس شما حذف شدید!؟ ناپلئون و هانیبال هم یک پلن داشتند نه ۷ پلن. آقای قلعه‌نویی چرا نباید کسی انتقاد کند؟  من انتقاد می‌کنم و نمی‌تونی تریبون را از من بگیری. مگر بزرگتر از علی دایی داریم که انتقاد نکند؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/136257" target="_blank">📅 23:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136256">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fH3LYSBNhrh5GNin4BMZW_LoS5SirSA3cYgjAtHCfp5wfpjr2Y1waSHD3KOKG0QPyognGWHIPhgOfyODL9KmcqTF7uXseakRXwpa2D4LHZktahFwKf-vVC1IUmjwtTLOHQGCp3yvsldtAWTtQgnjcnU6_yy8hmAAGVX7WONrdI2M-RTgueWRJiHLgrfalKOLnwI8d0J6j4wdRoCH4Uvad6vLGQLCq7UjAe7f_hVF9_eT7MuOx8JG1Ue1T9K4qYip0cu-vdTRXkrW9MMVYLpwcWBkAX7lU6t5cs-zdAzSmeOFBC2Wiaea_8aZfpVOJensWkaBsyNvZWaeVKe2eebtCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اسپورتی تی‌وی: کاپ جام جهانی 6.175 کیلوگرم وزن داره و ارزش مواد به کار رفته توش حدود $713,000 یعنی 140 میلیارد تومن برآورد شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/136256" target="_blank">📅 23:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136255">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔖
تصاویری از احد میرزایی عضو هیأت‌مدیره پرسپولیس منتشر شده که داره توی ساختمون باشگاه یکی رو کتک می‌زنه…اقای احمدی همین فردا دکمه ایشون رو بزنید
❌
پرسپولیس چاله میدون نیست، ایشون ادم زنوزیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/136255" target="_blank">📅 22:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136254">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85518f3eb7.mp4?token=CGiFRZNI6zC_OTa-nYXXttoOUBgc8v6qY-kb7JIae34H8QA3yM6M5kQM5dAQGtgOOTiNIWEbESuBUYhGi8eDkJCce6Pqk_yBTSbfqefBtQICU4jzcZW68hH0QM2B9NhQtq1TpKWT4pwBhv0vdY-ZKVkUMSttr6Y9sU0u1FvICZUQ-oBkEs-ZTPGCn-zdVMgote1tfSySx05x90k5vEJAlXtY_k-FLmCqEJet0ZEjDdqNodZF6TDwy3xMC3xVkZtGlGZHwEso6q_wtJ0XLBr2WNo5qMImhj24yKyKpdSz5rXlobrDk5xeDHaJXlPkVhh4o9fFZCaNYZUMsmq_6DKNWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85518f3eb7.mp4?token=CGiFRZNI6zC_OTa-nYXXttoOUBgc8v6qY-kb7JIae34H8QA3yM6M5kQM5dAQGtgOOTiNIWEbESuBUYhGi8eDkJCce6Pqk_yBTSbfqefBtQICU4jzcZW68hH0QM2B9NhQtq1TpKWT4pwBhv0vdY-ZKVkUMSttr6Y9sU0u1FvICZUQ-oBkEs-ZTPGCn-zdVMgote1tfSySx05x90k5vEJAlXtY_k-FLmCqEJet0ZEjDdqNodZF6TDwy3xMC3xVkZtGlGZHwEso6q_wtJ0XLBr2WNo5qMImhj24yKyKpdSz5rXlobrDk5xeDHaJXlPkVhh4o9fFZCaNYZUMsmq_6DKNWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خداداد عزیزی: مردم نون ندارن بخورن آستینتو انداختی زیر ساعتت همه بفهمن ساعت 10 میلیاردی داری.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/136254" target="_blank">📅 22:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136253">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/136253" target="_blank">📅 22:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136252">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">جالب اینه تموم فرم ها رایگانه ، وقتش نرسیده که از فوتبال دیدن پول در بیارید؟
😉
✅
@FuckBet</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/136252" target="_blank">📅 22:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136251">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ccLmtai2AnBHfoilcYw_rY-UbsaaaI8QX-TpHe0zyvkkUYT6MBN9vkGEXEypSjJeAGD5TMGiBix3DqXTTmQPlJgkANJ_g5PhdmOwldCenkR5wxY90EJFK1ZgYXeZP4yZSDnRvY0YzZfp7rYSusu26vwUya1GcTSfFjCmV6iWrHY4pOaKXAmbMfPeOAVSpYmy6f99lRNszBUB42cLm5YI4CPVfFRCKCyBB-dI0z7ch6zqaEG8nOOYaZ5Gzimyi_CMlTRW42SM52JyXFrURAmkNvqHGOxZOIka_TFmE_kFVA4HGgkVQtehVTspy7RmsLYfor_GU02MO5zFpyOm4SHYVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/136251" target="_blank">📅 22:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136250">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/136250" target="_blank">📅 22:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136249">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
فرهیختگان:
✅
وحید امیری 38 ساله به پرسپولیس پیوست و کاپیتان اول پرسپولیس شد!
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/136249" target="_blank">📅 22:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136248">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrWeHf1jK9Cyd09jUd3gNIOCC9Egt3URrsvc7lFmbb4_Uyt6TvqI7DxUxrbwT2MqV5jPOaM8S4WyJ2Yy7pEmEnSW3Qk6peJ41o6J_loMe8By9JnoKS63hdlLUZDiCqbAqgqDY8KjSkaKxyeSmsyJsWdiYonustV3OhwbcgO03UwufjFoJ6kofcRFEf28RzdUeGV_aYe_LqvMNdvcvXToFplzwN9pXxLyP6MJznFPn1pzIw_I_nFploNYJsewAjYy9X8MwnMmweoNiEdcXVFAZ2oBghLSIfhnmNovTR9ACteC65G4k2CjkmGEDoFXLiVbHwz9nF3eDnHz8-69C1YQzw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/136248" target="_blank">📅 22:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136247">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1DxnxapGDgRLvIZzM6TuMdK5mjS6zmsiSI1LLdXjWbPpZUIicPZOIWUZC8TcC7OEbXwHilnVHsC8qMsgLcgOG7_2oa7DAiw2mH3CyGXMUTyQoxTHHAEO-vNrB45E_P8G1ssoOGuemxbtxuaIe8dsHnPA6KU1CY-b1kHhhRHrCFdcHDotZr7GddbBcMRnItWyMuBOSzSK33jMNBMbl82hZDIenOJeveUzD91AfpAHgnbaBdDwRZ3s2HTy2pN1rSE2jMXW_6Nd0o3hrbcAQmV04j8E2LSmy_oSUMqzr8u-q3RR2cgOa_kPNkJRmjJySHE_Pm3PdaXI2Ze8bZY2kayLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترامپ از پشت شیشه ضدگلوله بازی امشب را تماشا می‌کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/136247" target="_blank">📅 22:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136246">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❗️
امین کاظمیان در تمرین امروز پرسپولیس حضور پیدا نکرد و جدایی او طی روزهای آینده رسمی می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/136246" target="_blank">📅 22:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136245">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZH-93uyxk0WVI6m6NopgfAlsR6jVt6xoP6EUINeVvYcx4_a2qXi7E9y2ZgJvrmylDpTrc5UQu1C95YHUuOvcypU1kRjIahyASenR9cDUv4kqNRdLgor8PDhGbAzahr_8JfxpYr3pFMZGPANLygzgR7RTHg9KLcMahODVE7YcmMnUt2wfrPwyTxiai7RbbmG3UYfhv-Q5lCyC9E--yaosqzSFFs4e2TMsMn1A3jrluA-057v_9ilBK194TsvC_DB4mSU-IfpnwRUpxxGwHvWo7-Jyy2GZ-3-fLBOcuIDHgxg223RZvDLsnqH1fKt7HGlNw0MEefQSvjbIo3pAbX9Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تصاویری از تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/136245" target="_blank">📅 22:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136244">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5b943d93e.mp4?token=K7jqzTm1wwKxV48zYUanOi3zAjXW87O6ZRSyO5hO95fSMx4jG9PvWK9UyhKMgto137SzM0AEnRCey_iaZiP3XPeXCd9f0kSvWAs9bC9s6ZwH9jUi-nLxz97KS1V-uCsasGBAhDbo5Qku3iYU5CdewAmzlGeZV_QODxulxmS8q_D6THnFzlHOafgP5YXvgjh9Q_2k8S_DaPYBjqtVTTrRfvo1Xig2Pjq0WeI_NIajfPr196EoL1MtoBmA9AD2RC8CItMX6ZTcFjBAMdlglyQ3tJwoNVlA05tS9wygESuzXED6GHxQGgbuRzTIE4blyeeCw2q1rRXxzDRiR5s4w0IdCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5b943d93e.mp4?token=K7jqzTm1wwKxV48zYUanOi3zAjXW87O6ZRSyO5hO95fSMx4jG9PvWK9UyhKMgto137SzM0AEnRCey_iaZiP3XPeXCd9f0kSvWAs9bC9s6ZwH9jUi-nLxz97KS1V-uCsasGBAhDbo5Qku3iYU5CdewAmzlGeZV_QODxulxmS8q_D6THnFzlHOafgP5YXvgjh9Q_2k8S_DaPYBjqtVTTrRfvo1Xig2Pjq0WeI_NIajfPr196EoL1MtoBmA9AD2RC8CItMX6ZTcFjBAMdlglyQ3tJwoNVlA05tS9wygESuzXED6GHxQGgbuRzTIE4blyeeCw2q1rRXxzDRiR5s4w0IdCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ برای تماشای فینال به ورزشگاه مت‌لایف نیوجرسی رسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/136244" target="_blank">📅 22:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136243">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
⚽️
🔥
مراسم اختتامیه جام‌جهانی آغاز شد  پ.ن فقط 45 دقیقه تا شروع بازی نهایی جام جهانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/136243" target="_blank">📅 21:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136242">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RaF1iifSPyX_3LvR_1NwvEWhft06BNVt_JnEGwp5WlfKWF-JLjJpSkSa4_-h7fUDdcSQWmJDlSNRP7_uitA9yxehaFqkDbVPO-UKd5r0eHomdZZduwtxeNRw1pj__l80UkAA3ma701zngI0tE9-XVfHzk7TXQABbj_VOCy7CINFCGsSegHUzo9tP445kaPaC7qGADfrEaO1hKz8qRVTOWZkfdkZKzmS96kbodmB_F8yRJzl1_gIbj_KLzkBdIfS2jb_WhoUsw2R_jFX_ovteC1FET3cNd7bNmikRNEv2GhZRvgsXDPVX3FdyytuG3zqPybKWBbfAbI6LOgr3AquBhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
🔥
مراسم اختتامیه جام‌جهانی آغاز شد
پ.ن فقط 45 دقیقه تا شروع بازی نهایی جام جهانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/136242" target="_blank">📅 21:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136241">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a92f2cfaf9.mp4?token=fUBCgxuFqpdzJvg__9nbU-Scd3K6Tbonv5ZHjRBSWlREPKuj6P_yr3_olJ2EI_uZbrbPfyUJXSmXPVDQY3kjxAqh3Y9sz-HjpcHpJ9SFHfu01Uyadx84G0CQWvyHkAKuCBb7QGVHlsRv9_Fy8UPLhAu_ODzD3wiCRDIDDrgWggQh-aNURpBzR81MHg6X4nDNDm8h2XbbEYajI7du0Ru_905i4ZZO-219xfmVV1vSgJdRH78MMto_g1chb6Kz0POVy0JjrM11f5KyiOgp0USGeuApy6QxVMml84wHty8v-1nBA3uykAPQDEoios83PZRjDNG9EcTAX7UkxGSBEbC-_WjTLYNQJE1dRiK10GADXVkfMqe8li7Ec5ZPuxlkKxMoeMPL7JDawjS8-vzUGMLMue9S7zjxl-CJ67AojkT_TRU5Gq_DX0f1e0JsyhrDQQcBrR8k9dQJB3iBal6ZElfISOWFJGXwP7lAPL-eBhsIZGkQmxRpP7znWVbBdRVjj_-kALd94xZUU0HnmH3nGZGRnXYl2w1RId6hMAmG_hp92aPac65_KwqOvQjQxuyEq3aCIeY2TOiziWMWGDVt3AHymUO1I3vPYJaN-uMlo1iz_4QftjPB2BH-8VPIU7iv24LmnLvMT1GvQK4BUV2hlbIgue_wmAqabk9VqMpkJBL7A14" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a92f2cfaf9.mp4?token=fUBCgxuFqpdzJvg__9nbU-Scd3K6Tbonv5ZHjRBSWlREPKuj6P_yr3_olJ2EI_uZbrbPfyUJXSmXPVDQY3kjxAqh3Y9sz-HjpcHpJ9SFHfu01Uyadx84G0CQWvyHkAKuCBb7QGVHlsRv9_Fy8UPLhAu_ODzD3wiCRDIDDrgWggQh-aNURpBzR81MHg6X4nDNDm8h2XbbEYajI7du0Ru_905i4ZZO-219xfmVV1vSgJdRH78MMto_g1chb6Kz0POVy0JjrM11f5KyiOgp0USGeuApy6QxVMml84wHty8v-1nBA3uykAPQDEoios83PZRjDNG9EcTAX7UkxGSBEbC-_WjTLYNQJE1dRiK10GADXVkfMqe8li7Ec5ZPuxlkKxMoeMPL7JDawjS8-vzUGMLMue9S7zjxl-CJ67AojkT_TRU5Gq_DX0f1e0JsyhrDQQcBrR8k9dQJB3iBal6ZElfISOWFJGXwP7lAPL-eBhsIZGkQmxRpP7znWVbBdRVjj_-kALd94xZUU0HnmH3nGZGRnXYl2w1RId6hMAmG_hp92aPac65_KwqOvQjQxuyEq3aCIeY2TOiziWMWGDVt3AHymUO1I3vPYJaN-uMlo1iz_4QftjPB2BH-8VPIU7iv24LmnLvMT1GvQK4BUV2hlbIgue_wmAqabk9VqMpkJBL7A14" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ادامه حملات عادل فردوسی‌پور به قلعه‌نویی: هرکه از "غار" حرف بزند، قابل توجیه است؛ به جز آن کسی که کل جنگ را در دبی و ویلای آلانیا گذرانده باشد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/136241" target="_blank">📅 21:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136240">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
پست خداحافظی رضا شکاری با چاشنی ناراحتی: خداحافظی همیشه تلخ است، خداحافظی از گوهر کمیابی مثل پرسپولیس تلخ‌تر...
📍
موفق باشی
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/136240" target="_blank">📅 21:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136239">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❗️
قدوسی: ابوالفضل رزاق‌پور گزینه اول جانشینی میلاد محمدی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/136239" target="_blank">📅 21:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136238">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✅
✅
عادل فردوسی پور :
🔴
آقای قلعه نویی من و تیمم چه جنگ دوازده روزه چه در این جنگ تماما داخل تهران بودیم و تکون نخوردیم ولی شمایی که یا تمام جنگ یا امارات بودی یا توی ویلای شخصیت داخل ترکیه حرف از غار بیرون اومدن نزن. من تماما کنار مردمم بودم ولی شما همش توی…</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/136238" target="_blank">📅 21:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136237">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❗️
واکنش قلعه نویی به تصویر ساعتش در جام جهانی که باعث حاشیه شد :
🔴
اگر یک سرمربی ساعت می بندد و لباس خوب می پوشد که اشکالی ندارد/ اگر من زنجیر طلا می انداختم و یقه پیراهنم را باز می گذاشتم آدم خوبی بودم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/136237" target="_blank">📅 21:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136235">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
افشاگری خداداد عزیزی از امکانات تیم ملی قبل از جام جهانی:
❗️
به من گفتند بهترین امکانات رو داشتن، شما اگر از امکانات آمریکا انتقاد دارید در کاخ سفید جلسه میگذاشتید والا، 15 روز قبل از مسابقات 400 میلیارد بودجه گرفتید، 1000 میلیارد از رئیس‌جمهور درخواست…</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/136235" target="_blank">📅 21:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136234">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9106b20ac9.mp4?token=rz_45l3abmQfC-SOxFkLppuzrFU1rqKiLf4NJr87ZT90fSBXtgm2hOq99sv0GpikfefL4651LM7oK40MMrUiajr6o9BbhLWT4Hn39NmbhbQFIkBuc6F_ayJIfI2oT-QvrMQROhGFICQ5BvOCOdSET7GqviBuW8uPYAa1PTJPEAxaDsWC_QivGKKOAeDzaqdf7ytHekbnkF0JW99lVMOrHMnsLwUto3aqctS2fDmIKLy-ONS_cBGYh3rJa_vweXPos47nJl_CUz1pZuyscZqlJLTtbGcTg48GMDL785zzDt9Ur0uTHHOdzhfAQ08MLZqjeRJaT-4s6_4ZEDRg4P3s8mL8lVC8QpuYjHQkGET-BdN4hnRU2a8qA4nuR0Wen5ESUM6DYqwrzVDgUH4ihoaDfN4srgfWlYaA5B4pkVyhbChOwqUv_eFvCQIAEJzF5GjgkXf6x4SRPJ7whO5czRew55oj-Q5v9eMMFQYu2AFoabFDGKVn8gNAEs0uuj4GQVqnn2NYIZAB43dKTjsarcMXf9MrR993YH29xBCdpH-KZ9ncn6ipRPOvoLliwOJw3RGS8gpf2LMjiKbl3ROGDHzz6pyzI05-h9fECfWMPpo201_XvNzNbIvHcF_Vp8NEveDW87IbH_sg3Ksy4qSn6aMMQMCJTZ5s21nnwvoJ1Fv-S_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9106b20ac9.mp4?token=rz_45l3abmQfC-SOxFkLppuzrFU1rqKiLf4NJr87ZT90fSBXtgm2hOq99sv0GpikfefL4651LM7oK40MMrUiajr6o9BbhLWT4Hn39NmbhbQFIkBuc6F_ayJIfI2oT-QvrMQROhGFICQ5BvOCOdSET7GqviBuW8uPYAa1PTJPEAxaDsWC_QivGKKOAeDzaqdf7ytHekbnkF0JW99lVMOrHMnsLwUto3aqctS2fDmIKLy-ONS_cBGYh3rJa_vweXPos47nJl_CUz1pZuyscZqlJLTtbGcTg48GMDL785zzDt9Ur0uTHHOdzhfAQ08MLZqjeRJaT-4s6_4ZEDRg4P3s8mL8lVC8QpuYjHQkGET-BdN4hnRU2a8qA4nuR0Wen5ESUM6DYqwrzVDgUH4ihoaDfN4srgfWlYaA5B4pkVyhbChOwqUv_eFvCQIAEJzF5GjgkXf6x4SRPJ7whO5czRew55oj-Q5v9eMMFQYu2AFoabFDGKVn8gNAEs0uuj4GQVqnn2NYIZAB43dKTjsarcMXf9MrR993YH29xBCdpH-KZ9ncn6ipRPOvoLliwOJw3RGS8gpf2LMjiKbl3ROGDHzz6pyzI05-h9fECfWMPpo201_XvNzNbIvHcF_Vp8NEveDW87IbH_sg3Ksy4qSn6aMMQMCJTZ5s21nnwvoJ1Fv-S_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
افشاگری خداداد عزیزی از امکانات تیم ملی قبل از جام جهانی:
❗️
به من گفتند بهترین امکانات رو داشتن، شما اگر از امکانات آمریکا انتقاد دارید در کاخ سفید جلسه میگذاشتید والا، 15 روز قبل از مسابقات 400 میلیارد بودجه گرفتید، 1000 میلیارد از رئیس‌جمهور درخواست پول کردین و چجوریه که فقط می‌نالید و ما رو سیبل می‌کنین؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/136234" target="_blank">📅 21:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136233">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cce783d5f.mp4?token=XKTnxfu1iVO3FXIuwlwIYvpMeCiODfOq0gfqsHioyYpZeA4VZ6Kvq443ivlk4MucH5oHianIqXd-VjtnNUdxxR574b0CiFuSx1ZWYtN3_r8KU1mTA96IhJ9N9pnngOMlKU1GJ_gxsc8GJgpzEgzsqsEtsKa_7jBK3xu0Y1QEjCbBnz_mb3y5MVGhztRU_yx3ixDu0guWLX1QaDbwJvh-0njsFLsTdkjX2L6c_Hs5zffzEL0FqLDuX8IicAtl61sDWHry2lyskTC3ExoyKZrhVZriiJcFlbagBI77V2ZN0-EnxhGFCYxMmaE4MsZ-QI9X9CSJvlD-ugjQRsyQQWeEznvC-x7ec5A1yu_F-oj-qPWsuGqvN4jkCfmwvp2uKppHva3Mrv8Mk8YxjoAWc3zyAkPDjSt7MtfKsgiV_4HAeGkTqI1TAWRlI84AF7vioqqr0oBLCHGtCkSTq2OhnTeiwskcaDxE43RQCqBBVWAxCckdRHcuoRFYu1m_FW-3uJQFIHj27JX-6RjCBfSwbtfxTa8o4rWWv_qRSqv8YLo_WPDBcd1D4OKY4c9_6xY-CSSkkViM_JWhyBc-ExQiADhMyvuWFWE4PicmxoH7KkV-EYT97mWBS7Fl3cZV7COX8PeczeMfFAoNDb9i0r3hfgiW381yi_AGy-0w3F-QBhm-wNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cce783d5f.mp4?token=XKTnxfu1iVO3FXIuwlwIYvpMeCiODfOq0gfqsHioyYpZeA4VZ6Kvq443ivlk4MucH5oHianIqXd-VjtnNUdxxR574b0CiFuSx1ZWYtN3_r8KU1mTA96IhJ9N9pnngOMlKU1GJ_gxsc8GJgpzEgzsqsEtsKa_7jBK3xu0Y1QEjCbBnz_mb3y5MVGhztRU_yx3ixDu0guWLX1QaDbwJvh-0njsFLsTdkjX2L6c_Hs5zffzEL0FqLDuX8IicAtl61sDWHry2lyskTC3ExoyKZrhVZriiJcFlbagBI77V2ZN0-EnxhGFCYxMmaE4MsZ-QI9X9CSJvlD-ugjQRsyQQWeEznvC-x7ec5A1yu_F-oj-qPWsuGqvN4jkCfmwvp2uKppHva3Mrv8Mk8YxjoAWc3zyAkPDjSt7MtfKsgiV_4HAeGkTqI1TAWRlI84AF7vioqqr0oBLCHGtCkSTq2OhnTeiwskcaDxE43RQCqBBVWAxCckdRHcuoRFYu1m_FW-3uJQFIHj27JX-6RjCBfSwbtfxTa8o4rWWv_qRSqv8YLo_WPDBcd1D4OKY4c9_6xY-CSSkkViM_JWhyBc-ExQiADhMyvuWFWE4PicmxoH7KkV-EYT97mWBS7Fl3cZV7COX8PeczeMfFAoNDb9i0r3hfgiW381yi_AGy-0w3F-QBhm-wNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
خداداد عزیزی: صداها را نمی‌توان خاموش کرد، مردم ایران غارنشین نیستند، آقای قلعه‌نویی ما جنگ رو دیدیم، بهترین کار این است اسم ببرید، شما نتیجه نگرفتی چرا میندازی گردن ما گردن رسانه؟ تنها جمله درست شما در مصاحبه عذرخواهی از مردم بود، دوباره در جام ملت‌ ها من طاقت عذرخواهی ندارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/136233" target="_blank">📅 21:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136232">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
🔴
🔴
فوری| وزارت خارجه قطر: پیشنهاد جدید آتش‌بس را برای ایران و آمریکا فرستادیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/136232" target="_blank">📅 21:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136231">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
🔴
🔴
فوری| وزارت خارجه قطر: پیشنهاد جدید آتش‌بس را برای ایران و آمریکا فرستادیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/136231" target="_blank">📅 20:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136230">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6549a463.mp4?token=UcC1anmu5MgBEO70uitCcIVRL2F46hK6pu9pGVHppj4q2OqyrwLku3QYvhpeo0ztVZpCZp-UX-4Y3JrWlaArhWu5MB-2T4w3sKfd1WTLbij1DRhS8KE6hc--z1V-xUGKOPjxvFRNmzAN9mmSpxJLizbp1hPMK9v_CGKUyRj5bg5FXyrOP5eRemVLFYqAN_-6_iP4tHKOdn9lIVhh76qByQVm6hZj0yqUolzp5UqX1Ddz79MKEsnpzpSOhE_987nox78Wo388m6EaICynqOf2RmIpdlatOK_AKDctbA4UQoG_JAXwW7BTUZK4-NXAzxgtCJMBEnNoFh2vRF4K-D3w_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6549a463.mp4?token=UcC1anmu5MgBEO70uitCcIVRL2F46hK6pu9pGVHppj4q2OqyrwLku3QYvhpeo0ztVZpCZp-UX-4Y3JrWlaArhWu5MB-2T4w3sKfd1WTLbij1DRhS8KE6hc--z1V-xUGKOPjxvFRNmzAN9mmSpxJLizbp1hPMK9v_CGKUyRj5bg5FXyrOP5eRemVLFYqAN_-6_iP4tHKOdn9lIVhh76qByQVm6hZj0yqUolzp5UqX1Ddz79MKEsnpzpSOhE_987nox78Wo388m6EaICynqOf2RmIpdlatOK_AKDctbA4UQoG_JAXwW7BTUZK4-NXAzxgtCJMBEnNoFh2vRF4K-D3w_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله شدید‌اللحن خداداد عزیزی به قلعه‌نویی: شما فرشته ما شیطان؛ شما خوب ما بد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/136230" target="_blank">📅 20:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136229">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❗️
❗️
فوووووووری/ارتش آمریکا در پاسخ به نقض آتش بس از سوی ایران، اهدافی را در جنوب ایران هدف قرار داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/136229" target="_blank">📅 20:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136228">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBnPFTFSdbvdgLyf1Ny-UrfdsBNuUyYc9GtVCpC1Vd6o3PvPsIHQ3BJc2nOY7cmntw41FHpkfGUWW_gcxE8pJ8Id2UZumllVaYebI6dMFzaoS9O1Cs-BipFdkxMd9YYg6hTtdSaJcdr0jzE2guzCyfBr_wWuFyjiFPCDRVZZzrXUMrq6NMOo0tScOYLTU6dEhYrsaOILQ9IDATzNp23RG3A2-TgdC7_LcGm7IKkIrJxdO6FjTx0StnOS7iKDmirKim3GjYpzb-Bd7swtMoGDS4iqoAh33Z4viRI1tofnS07OcaVJ-kfI3MgDtuL8XQkm1Cth-o68PvIiPsQVjkxfWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔖
تصاویری از احد میرزایی عضو هیأت‌مدیره پرسپولیس منتشر شده که داره توی ساختمون باشگاه یکی رو کتک می‌زنه…اقای احمدی همین فردا دکمه ایشون رو بزنید
❌
پرسپولیس چاله میدون نیست، ایشون ادم زنوزیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/136228" target="_blank">📅 20:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136226">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
رقم قرارداد دانیال ایری،‌بالاست، ولی می تواند قرضی به پرسپولیس بیاید. او بند خرید دائمی در نیم فصل دارد و بنظر می آید نساجی مایل به فروش کسری طاهری است. ضمن اینکه جذب علی نعمتی و قریشی هم قبلاً کنسل شده بود
✍
قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/136226" target="_blank">📅 20:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136225">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
#تکمیلی؛ باشگاه‌تراکتورتمام‌توافقات لازم رو باخودِ علی ‌قلی‌زاده برای قراردادی سه ساله داشته و تنها رضایت نامه این بازیکن باقی مانده که مالک تیم تراکتور قول داده ظرف 48 ساعت آینده مبلغ توافق شده رو به حساب باشگاه لهستانی پرداخت کند.
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/136225" target="_blank">📅 20:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136224">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
❌
باشگاه تراکتور مذاکرات مثبتی با علی قلی‌زاده، ستاره ۲۹ ساله لهستانی، انجام داده. او قرار است ۷۰۰ هزار دلار به عنوان رضایت‌نامه به باشگاه لهستانی پرداخت کند و سپس به صورت رسمی به تراکتور بپیوندد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/136224" target="_blank">📅 20:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136221">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
❌
باشگاه تراکتور مذاکرات مثبتی با علی قلی‌زاده، ستاره ۲۹ ساله لهستانی، انجام داده. او قرار است ۷۰۰ هزار دلار به عنوان رضایت‌نامه به باشگاه لهستانی پرداخت کند و سپس به صورت رسمی به تراکتور بپیوندد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/136221" target="_blank">📅 20:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136220">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
❌
باشگاه تراکتور مذاکرات مثبتی با علی قلی‌زاده، ستاره ۲۹ ساله لهستانی، انجام داده. او قرار است ۷۰۰ هزار دلار به عنوان رضایت‌نامه به باشگاه لهستانی پرداخت کند و سپس به صورت رسمی به تراکتور بپیوندد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/136220" target="_blank">📅 20:16 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
