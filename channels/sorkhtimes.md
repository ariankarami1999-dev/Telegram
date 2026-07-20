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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 14:49:00</div>
<hr>

<div class="tg-post" id="msg-136301">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 393 · <a href="https://t.me/SorkhTimes/136301" target="_blank">📅 14:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136300">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 453 · <a href="https://t.me/SorkhTimes/136300" target="_blank">📅 14:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136299">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
❌
تیم پرسپولیس که قصد داشت فردا برای اردوی اماده‌سازی راهی شهر ارزروم ترکیه شود، با یک هفته تاخیر اردوی خارجی خود را برگزار خواهد کرد.
🔴
🔴
پرسپولیس روز ۳۱ تیر ماه برای این اردو تهران را به مقصد ارزروم ترک خواهد کرد و احتمالا دو هفته‌ای در این اردوی خارجی حضور…</div>
<div class="tg-footer">👁️ 546 · <a href="https://t.me/SorkhTimes/136299" target="_blank">📅 14:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136298">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
❌
باشگاه تراکتور مذاکرات مثبتی با علی قلی‌زاده، ستاره ۲۹ ساله لهستانی، انجام داده. او قرار است ۷۰۰ هزار دلار به عنوان رضایت‌نامه به باشگاه لهستانی پرداخت کند و سپس به صورت رسمی به تراکتور بپیوندد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/SorkhTimes/136298" target="_blank">📅 13:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136297">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/136297" target="_blank">📅 11:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136296">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❗️
❗️
پرسپولیس در یک دیدار تدارکاتی روز سه شنبه هفته جاری به مصاف تیم خیبر خرم آباد خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/136296" target="_blank">📅 11:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136295">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5fqgZdw1TDGt9U457AQkFu38jib3cXOta2ehADreqN1BF4-NLZLf7DcOygT1bLXfaDhk91WoZg-oGlBL3boQzxpzQzFvil0T1h8e5ItFI1-rDNALM4VZ9ZcIgY5xNTVPZwKnjELQpUZPsSXN8JKDyA2X8UeCffCD5IG2RrDb4Ix0og5NpVWgbAYdDFMSEHLA5ywuaDA9VXYi3xQVPKhJQE-nhmkrZ7x9ayAOTb2x0jeYH54OvXBjAl8BGhsBxF6VxHrbPwqEkFa64MlfWKR5Lx4AR-y_BZNPSdPCPTkWWmjRPfeUVK86DEY0m1XmujbPyQc-ahMVEOKUTVKXhNVlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رامین رضاییان از ایران با دو گل و یک پاس گل به عنوان سی‌ و هفتمین بازیکن برتر جام جهانی انتخاب شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/136295" target="_blank">📅 11:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136294">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✅
گویا دوره حضور تمرینی وحید امیری در تمرینات پرسپولیس به سر آمد.
🔴
احتمالا از فردا دیگر به تمرینات تیم نمی آید//طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/136294" target="_blank">📅 11:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136293">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/136293" target="_blank">📅 11:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136292">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
❌
پرسپولیس دو پیشنهاد خارجی برای امیرحسین محمودی رو رد کرده و می‌خواد فعلاً نگهش داره. درخواست شماره ۱۰ هم با مخالفت تارتار روبه‌رو شده تا فشار کمتری روی این بازیکن جوون باشه.
🔴
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/136292" target="_blank">📅 09:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136291">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/136291" target="_blank">📅 09:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136290">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uns-T9Bopckmb4OdNh-eqw3UfKDLmWsgE0b-ElomGO4Q46uPJxW31S4gb0Hto2LWiGfTVO8oVhvDRUHGU3mm5MNZtv2gX0S4VV5s7YgyJrM9RrH5gDvpBARiSjen3psKWkDPpD0P2cRILyAjlo0Ovc-zTC_ZcD-o9l8VZALz8Z0w5n7uRcrsDoNfqeyE1uU9W9TX5In-GmoWKLQUKp7GWmzJLRMKxv1N6Hoc1BxhE5LaihGEsrA2pU0DS3NQNTMyiFR-Wr3lfigO5f9t4ko5lAL3L-ttiDp71265GxtOEQG62bdRhx5Yv2zAuR0eno-WnKmNMp6TaaGgxTsipc3dVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
چه قابی شد ...
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/136290" target="_blank">📅 09:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136289">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8t86gP8tIGoNbAx_Cg49-IYcq-0wldvPtHbfsCfhdzO2kKfWrOYPGy7_NuXGSINX4MUeEh-n7uqfCNOw5Q9UZFiBzy3aPe51GwtXmwTk4aULaryAWq3x8iXPLogwRmTjnWmeHi0QLZrBf6cRLHuxY6vkQqD7GPPz4QJunv3Oa82vJZ5jtIqWaxYY-p9haH6ceehI-k3RNj4MV5bH23-PQ5ModNPJLOK4jrYgE6zjDrSKkP_e86khWJGkirLcZ_n6Oa6we-J4GFuDBAKq_zou5WMNsjG1QptRLsGnznk4b-iDMfgJ1sXRff44Rr60UBbCvr2n3KPoEKZ3vmsmfthIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دو زلزله به بزرگی و شدید ۵.۷ و ۵.۲ در کورزان کرمانشاه به فاصله ۵ دقیقه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/136289" target="_blank">📅 09:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136288">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✅
گویا حملات بسیار بسیار شدیدی دیشب به تبریز شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/136288" target="_blank">📅 09:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136287">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
❌
فاکس نیوز: هروقت داور بازی سوت پایان بازی اسپانیا و ارژانتین رو به صدا در بیاره جنگ علیه ایران اغاز خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/136287" target="_blank">📅 09:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136286">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
❌
ورزش سه: محرم نویدکیا رسما خواهان جذب ابرقویی و کاظمیان شده در این بین گفته میشه احتمال معاوضه این دو بازیکن با آریا یوسفی در قبال مبلغی هم وجود داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/136286" target="_blank">📅 09:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136285">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇪🇸
🏆
بالا رفتن جام قهرمانی توسط اسپانیا
💢
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/136285" target="_blank">📅 09:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136284">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/136284" target="_blank">📅 08:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136283">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/136283" target="_blank">📅 02:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136282">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/136282" target="_blank">📅 02:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136281">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SY9BAmLqaXuEpdCcatd1vwoTGlj43uLrwyimW4ZOB0nLTqM3WiOKhnNWNBhQN-GLHclP4FNAgfFdYMRoXKN_hJB1GGktwuES0pi6yYymy5MKZXH1lxGEMmz62tMuGMfWRD4_sPKwv4-gr4uvCmEQ9aNyX6lDKQI_JIqySV4wEZq83sN41S2s0y1kSlMtdSes656CSqFQQU1SLduLbLz8zITAb4JdrBbIpg32p9ARjt0tPHF6Rz4pxmgclK950L81bj5jZj9wDtt2qU9SWh8132TsvVIQ5ujN5-R7D3-5C7NYLlmrHrZuzUm_-Cx97Y4Laf3R4ZypZPUcWcLqnPqgvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏆
بالا رفتن جام قهرمانی توسط اسپانیا
💢
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/136281" target="_blank">📅 02:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136280">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">⚽
فیروز کریمی: مسی الکی داره گریه می‌کنه چون دید رونالدو گریه کرد وایرال شد
👎
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/136280" target="_blank">📅 02:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136279">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/De67C_kXBR1WYL01xXROB-O__ThEJcYV2Zr1qKdMt_phQDvPt2W7rE7YjREz3ssTu_1_kLT_75cTObJyNRheCqy4UV-EEg06mKbXpfOK7TO28_YW-nzbB5dWdvCq1ygi-FPjG0zhWiAY2Pem_e6kDmfHpRlkrpPv5YGbLZ94x4WN-VTJevA3QUBF3va6T2p7gQksr8EY_onnSSwOZj2jwhZpBOmB2aiAS0qiExd4dDSOrT4ygufaR6FidR-k17qdKFZ0RQ6-mbFU1OFa7WlBLPBZuXuX2UQ6gb5CFDT5P4aYgMLg4bkNDplazlG0-zqZ2sCGklYvi-gUqfvetaTwIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
⚽️
سرخیو راموس با کاپ قهرمانی جهان اومد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/136279" target="_blank">📅 02:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136278">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ueypOWUnsGEgLXG3OZXh8xUlPt5sxWWrpyRZ3l4QvNDShBp4aEUneu3Uq4HGdRMNoj02BMx8nuKpU5X12qcY8ZIqqwmIQGKt6GWXzmTxd-zu9onR6IMshjyT11crSY_8KckGUK7mZKpDEciOkqiIGpr0V9-SOGSWwSk998Bv1M0Iziv1eF5vw2ubDCHUYl9orYDQoIxhxpSWeblH2GVlgDJKh2MESRMqhWdM5M_sW6b10Drpq7TMtYR6n7sLcjTFwmo7OhZ9f10m0OwPpGypQN03eXBgBN4NRlSCPlwl00JS_o4MOG988-N9DG6Zvk50waxglrzVx8XKn06Xgo1oiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
💀
گریه‌های مسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/136278" target="_blank">📅 02:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136277">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/136277" target="_blank">📅 02:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136276">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/136276" target="_blank">📅 01:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136275">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/136275" target="_blank">📅 01:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136274">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4lLlkjgWFA3eVRRlyUSnpLyj5ms4lOC0OfZNmVkQNxl9MUs0zjx03RQmvoeFZjN0S-wenbAOICiTlYDNLMFLXsYqdiEsIAgGfu-jNhMlspqMVfrt-8_v4xIbvzvHqi1HzIqm--plI1GgDPu6buF7pJiiC3cPrfqO5EsJM-jYBUfFGkzNEfwfJV8ccdDRmWEeaOvR6wPULh9kObmYGr-8ujG-5Dq0IcWyGZrqIGjeQEXpv_8I685jSXq9nd6w6vdTW_x1Iq7XH_T-gcJ-nUrIxLBJ8paZCEZPNfamjJ-qLVfPlVi7dG_a63U8IpE4Rz-iD7H2QOB3NQ1XD8NkiNDUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
عکسوووو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/136274" target="_blank">📅 01:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136273">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJ_M5zUZILfVCSZHsaVbmi6GlKh82I1YDnvke4XKswzft5n-eBpKvELwy0lJ6_m3rAptQa4wosjB7QihTzEjjlIZJeKhYpfYHf8_JwAJRKR_wrkqWMw0lYSdeVT3elUPO1-GponQiunML77E5GNGaKory4g4Kv59uBeL6MmxsScfIKOQHBKwG2pGJbXYOX-w4bnZMlNPYun7N-nfpOiIf2xLtR4cP_GBvnfpe8jkYnMiQxZ-5wjsNE7qTg84QGsXZdYGZtCfj2_AFT-8ql4PVW6qGDL1OXIX76JQ4mikeBHRaodS2M6cnergm97do4jh9QKhAAfGuMTS5WsOYeKOSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
‼️
کنایه سنگین تونی‌کروس ستاره سابق رئال به آرژانتیی‌ها:فوتبال برنده شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/136273" target="_blank">📅 01:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136272">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHnGi1uDBWHPLrR1hDG3SNxlDzi8JKvANqM9upSaPPJXtdKcZ952YIE-zFgHO6bmOelERFxuhc7UXk2eajKU0wboLwKio2KS6R9UVk7t6JF8Y0TJkTU7fXCEGdz7GwkoFFkqnspSE4FLOG_dO1WsGPTRxmRaueHIxcWKtkqGZWTRSTs4vr1AgOWoVFgSZagbWQbVpIv5N9_QWvIIKH_IY1q6Vnwn2y1D9CXmattaWSDB28Kj1Lig6JcXwzSXpzYbE77mqmYQ-qdBEpClOXYTVeF68DlHJftT-rCvdN3eQ9A19rA0xnH4M4M9bnx4ovwBYvMo8GMGnSVKyMaRUKwlSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
اسپانیا با شایستگی تمام قهرمان جام جهانی 2026 شد‌
🇪🇸
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/136272" target="_blank">📅 01:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136271">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWIQqpgdtgazhJZzloLFzQMoyuq_WLe29lVC70Scqc4kVUjoARTWwJZ_LiExKDK4W2nkk1lLbRCdrdlzVLI9xFA3YRFqUtw1PJFRhusyrg3gGMdrFYhkTtQ07ZMae-Jdb8MFKhhTaC5lprAJ8SyAqfD4MjmQw1P7sCQ2f0sJyHBc3JCXbmNN6dKercRjQtqQpcDdhPpo9PwaRvrr5EGJp25tzMplUZzQNQRvtrYC86QLY1terPGoOSJCa3cSn-zfX8BNWzfwIBcyfby39X3C7FC6kg61tKhbPLcRiFMo2nQ12c-NLcCPeHNuxQYqdv0whE0Pb-LQsT-5XN6w0sVKbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💋
پایان کار مسی با آرژانتین…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/136271" target="_blank">📅 01:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136270">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✅
این بازی فینال که چرت آور و خواب آور و کسل کننده بود با نتیجه مساوی تو نود دقیقه تموم شد و رفت برای وقت اضافه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/136270" target="_blank">📅 01:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136269">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
بازیکنی که کلا محو بوده و خواب بوده تو زمین فقط مسی بوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/136269" target="_blank">📅 00:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136268">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/136268" target="_blank">📅 00:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136267">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">⚽️
اسپورتی تی‌وی: کاپ جام جهانی 6.175 کیلوگرم وزن داره و ارزش مواد به کار رفته توش حدود $713,000 یعنی 140 میلیارد تومن برآورد شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/136267" target="_blank">📅 00:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136266">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❤️
🎥
ویدیویی از تمرین عصر روز گذشته تیم
🔴
از مرور نکات فنی تا اجرای برنامه‌های تمرینی؛ یک جلسه دیگر از آماده‌سازی سرخپوشان زیر نظر کادر فنی.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/136266" target="_blank">📅 00:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136265">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🏆
اجرای کامل مراسم بین دو نیمه فینال جام جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/136265" target="_blank">📅 00:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136264">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
❌
نیمه دوم هم چنگی به دل نمیزنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/136264" target="_blank">📅 00:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136263">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❗️
نیمه اول بازی .بی روح و خواب آور و کسل فینال با نتیجه صفر صفر تمام شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/136263" target="_blank">📅 23:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136262">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99bc7fc060.mp4?token=vnOhB86wO0K2XqGg_coviB89FAOzQdgASLk2xb1D7-gfIUmirPEXEXHodMOR1oFtovStP-6yCQSv8zST5xVYtT-PJKWzd8Hm0nYcjwmiDmjVx8mvSx8U77KsKt2S-luDcW59R7rrrnY7q7W3B5maORgXv1RAGNkUvZ_Q-V9UtI0nxUuyUI6RqgSvYkMElgtLYv_fIx8xtQHSFHCMmvIAUZzivEVXCACJPm0hTqRh_aZJm2D3l7fWPtq63pf2UNXZ5aPkAQVqm6444drb6rZZ8hYkmSepi05jQdTFl6yFTY_w7SUTIpJER932_XloEHckpY6IN1iefDeBRygnTYm20A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99bc7fc060.mp4?token=vnOhB86wO0K2XqGg_coviB89FAOzQdgASLk2xb1D7-gfIUmirPEXEXHodMOR1oFtovStP-6yCQSv8zST5xVYtT-PJKWzd8Hm0nYcjwmiDmjVx8mvSx8U77KsKt2S-luDcW59R7rrrnY7q7W3B5maORgXv1RAGNkUvZ_Q-V9UtI0nxUuyUI6RqgSvYkMElgtLYv_fIx8xtQHSFHCMmvIAUZzivEVXCACJPm0hTqRh_aZJm2D3l7fWPtq63pf2UNXZ5aPkAQVqm6444drb6rZZ8hYkmSepi05jQdTFl6yFTY_w7SUTIpJER932_XloEHckpY6IN1iefDeBRygnTYm20A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اجرای بیژن مرتضوی در کنار ارکستر فیلارمونیک بین نیمه بازی فینال جام جهانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/136262" target="_blank">📅 23:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136261">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✅
با یک چشم بهم زدن جام جهانی 2026 هم داره به اتمام میرسه ...بریم برای بازی فینال ..آرژانتین و اسپانیا ....
🔴
پیش بینی شما چیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/136261" target="_blank">📅 23:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136260">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvHMXdwidljl6rUg3L-94xHkAzcUPiTn7-itsZPxlGZTXr1iQ2MDnCGXyy3yjNsqHAtLPP4_DLiLdV6pebE4_LAyD30LFoOiFXrgoIDrLf7SbqJRFBcnusWrHjHdAiS0zdfU1txcxL0aoefodkEk3C2rbIBHcuEkHe82Zw5PEOSBBCC4fNIPWJftKjuzfZvSR1FQKQF4nceRfpbuhCRugB1QKP0UMOgtzetXnv5Y27DPdTlCFJLsnGWuUeaws7QRWjN5AnYohN-g4z9pd3BTE-yyEWKZhW94FJtZ3A6pCbXt8Q-pwrNN6DsEC2zYgq_b4pftzrATwCb_BnPohhYI2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یعقوب کافو هم به تمرینات برگشت
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/136260" target="_blank">📅 23:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136259">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
ترامپ از پشت شیشه ضدگلوله بازی امشب را تماشا می‌کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/136259" target="_blank">📅 23:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136258">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✅
✅
#تکمیلی | رویترز:
🔴
ترامپ دستور حمله قدرتمند به ایران را صادر کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/136258" target="_blank">📅 23:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136257">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✅
خیابانی: چرا در ایران کسی معذرت‌خواهی نمی‌کند؟
🔴
واکنش تند خداداد به صحبت‌های امروز امیر قلعه‌نویی
: واقعا خیلی از حرف‌هایش را نفهمیدم. ما لودگی می‌کنیم؟ چرا پس شما حذف شدید!؟ ناپلئون و هانیبال هم یک پلن داشتند نه ۷ پلن. آقای قلعه‌نویی چرا نباید کسی انتقاد کند؟  من انتقاد می‌کنم و نمی‌تونی تریبون را از من بگیری. مگر بزرگتر از علی دایی داریم که انتقاد نکند؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/136257" target="_blank">📅 23:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136256">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPiRVjwszMThXK1JkDIePFYTq79k46bdgMteTMZYKA6xSuaUjat5_c9Mkp1PWvSm-K8RB9vyUeJANKygoWNEDXxavgm4X0LAZwI27IFPEk23wf5ENS7f_aALXwftGG1lZ-gSDn6mxMmtjcoUVhFx0D1QdZJxLqIb6W1x-UHvWsHBdV25oMPQsTKwyIR6DcUXdO2E96x4gCeOAcWWvO0c9Psc1jbrAAyYX7xZhr3vazexTpxxDBfW7tSlviFcFwbvZlSvo1-SAqibQYllN3YACv12EH84Xq5VGji_N9zpzx4RtZds2L6A8c3oLrbwaszZA-jI0sCpaGlitRRCQ9iwiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اسپورتی تی‌وی: کاپ جام جهانی 6.175 کیلوگرم وزن داره و ارزش مواد به کار رفته توش حدود $713,000 یعنی 140 میلیارد تومن برآورد شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/136256" target="_blank">📅 23:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136255">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔖
تصاویری از احد میرزایی عضو هیأت‌مدیره پرسپولیس منتشر شده که داره توی ساختمون باشگاه یکی رو کتک می‌زنه…اقای احمدی همین فردا دکمه ایشون رو بزنید
❌
پرسپولیس چاله میدون نیست، ایشون ادم زنوزیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/136255" target="_blank">📅 22:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136254">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85518f3eb7.mp4?token=nd8kPuJoxkJcDkfk-3Vm27-l_-MSpCXK8444syg45jD6rP7o__SJHAMVmJJWIHWxbKxqz5lNhfYsIqnDrkZUSTY5lUH2E3FxibFKYS9sa8jBhkq7pm4nf1rDiamP_M5CgiOpa1gknYI6m1JTRzps7MAqPmFWpneGZxs3C82oDlcZmM1tcAcWBhme80wyrdvUIa-O_MRvTXvHftQL8QvEqQXaLMzVYu5OH06THBOgtySTPSuPR-Sz6wGaKO5KBrb84TK9wiR252tza0f7GWr-MY7-A0Cm8B2J4WyYLFp5Ah4-qzhOtmDzOV0B979PsNaysIgbvl9ZBbsmbtCBryRxHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85518f3eb7.mp4?token=nd8kPuJoxkJcDkfk-3Vm27-l_-MSpCXK8444syg45jD6rP7o__SJHAMVmJJWIHWxbKxqz5lNhfYsIqnDrkZUSTY5lUH2E3FxibFKYS9sa8jBhkq7pm4nf1rDiamP_M5CgiOpa1gknYI6m1JTRzps7MAqPmFWpneGZxs3C82oDlcZmM1tcAcWBhme80wyrdvUIa-O_MRvTXvHftQL8QvEqQXaLMzVYu5OH06THBOgtySTPSuPR-Sz6wGaKO5KBrb84TK9wiR252tza0f7GWr-MY7-A0Cm8B2J4WyYLFp5Ah4-qzhOtmDzOV0B979PsNaysIgbvl9ZBbsmbtCBryRxHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خداداد عزیزی: مردم نون ندارن بخورن آستینتو انداختی زیر ساعتت همه بفهمن ساعت 10 میلیاردی داری.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/136254" target="_blank">📅 22:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136253">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/136253" target="_blank">📅 22:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136252">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">جالب اینه تموم فرم ها رایگانه ، وقتش نرسیده که از فوتبال دیدن پول در بیارید؟
😉
✅
@FuckBet</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/136252" target="_blank">📅 22:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136251">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NQKDohXhnwwlxi5sQEpZt9WOaoHzcKzdJ9QV3cCKnhj0BHf_XgHfNPP9KVC5mdfl6viLPvtKIdLwq_qKX-C3IoREn3Mp1nqwY7c_4jA9J5SGw2QdFt2VxWb0-gt09chyMfy4ELUFqJvCZPT1Y0p3sW9YfQTdiwXyZvYQvYOAYkFZ7GY6ej8tM77KaL8fJVuC2X1m6BzHaDHKKCbFTq6XHwVyHK6NK5qNPOl_Uj1ry-m2c0NR21jSyWdp4NLMtoYHxiyFonr0UYvUAgtOMooVgjOBWC-ky0o53vw-mGXTA9pVmBi0oBybZcR9F3AKXxY3ojDUYn-L1QnoLoTjKYXkuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/136251" target="_blank">📅 22:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136250">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/136250" target="_blank">📅 22:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136249">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
فرهیختگان:
✅
وحید امیری 38 ساله به پرسپولیس پیوست و کاپیتان اول پرسپولیس شد!
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/136249" target="_blank">📅 22:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136248">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8pkiXamq9MCK5282r97VvPR8J1B83PY8rEfAdXJgihJF8tQZTNa9EwUte0uLvgjQlgeKfMvTyXatLI0Ig_u6rYDmSVL2KcfGkX1AhyNJPA-C2hKxhqw3Xc4o0zeRZ1MwyVpEI-7QbiSxxT6d49qVWgUF40E5yH7Jq8HWS0gJ9uYHQB_EdAhFtqO9UCSzCLaUFYSUHisUXwHCnwbxPtXfoQgIGytj4qcF6WQBcMbi0RRVmwddhgCqcQ7HpkvaCcKCAMeGjWDp55v_AJH06hnI3T8It5SIU2RKGRwXItun5lBM_YHMLQmajrjBZ_e7ia7TJnzcyqC3rXMG4Om9lHUSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/136248" target="_blank">📅 22:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136247">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3XbNJuAG3VnmFxv8b44pyMyw0UjTctpVLe3D0Riv1E4iqfKMozwRgno87oC0wlYA_BrbUNEyBCQp9d2_z0hMeDiwDvTkVaANrZE-Sq0gIBb8SpLmSAqGQOitjrXtXHti7wjc7PQCM2FssR9_qVbvhks4Ycli4CHi7VJiBEcVPUvPIVMAdlPrLdhN5cFSHGv54Y-syluQz4hF01pma75jxhi2BDL-BdIj7gqdfcJ6VDyEu3Xi7XJODi48OzRfYbour9Pi4w93_7ybQgFkCw3rloCs-IKD35DitxwGVh1QDkxMWRnbdw-GNQ38cld2ShwESlJWk7dt2te2aiEpl4qag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترامپ از پشت شیشه ضدگلوله بازی امشب را تماشا می‌کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/136247" target="_blank">📅 22:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136246">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❗️
امین کاظمیان در تمرین امروز پرسپولیس حضور پیدا نکرد و جدایی او طی روزهای آینده رسمی می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/136246" target="_blank">📅 22:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136245">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXYyVVxnXfCsWKQxVbCiyaAZ7OZBIOS4CpdQcKwT9eAg9CDpX4tTeln1TRtBOrW8uAr-l1-N9Ghl4EQPdT7YeuklkC2RgKLK0e2r8RGA2234eLadOPxhxA6NINxI2znvZB1M7oUM201XQAo6TvXcWza-RjmK0tfFFEtfh8JF3Rp0ULL780lrwJLk0jMFe8sYYSZC9x6V5FFbZBktM3SC88uOyAXey7TkR77GW2Yxhy5xxWD6pltbkZuDxvUUS2pnd5mDfXCff7gPJ4cAHRbupQnOnZuL35cju3hHRQNMpVPKOmLomuyERDKgHl4VQHNkolAM4TK4x_cl4fn2hAnCzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تصاویری از تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/136245" target="_blank">📅 22:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136244">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5b943d93e.mp4?token=JK2aXHNvCtXhA0VyxWBB_HG16DKAKzhk3XfCr4ItmJ_Xw9YhW5ydH7zgcItZWAwAxqUPPOhAaMkfJHirJnBk5zIy6cJVaPE1xK0jPT5TMmgfjiU8zk6GS9DNZaHwmVajw6xLb7KNPBElqmgp07TRo1cL6oIlqovsOmTmnliavYpymg132GeRLOY80xfU75dFRT6w3JYH9e20SEY9fKdIaCkCHMBpdzz6XXEbok_FKSKr9emvR5R141ZqQyjLJRXUeaPkqIhxNrSUgmauK1AeDFhr8tUGK_OgeT9gPISW0fBNHW_4H2wYS7Vd7azkNW25g3W8i9IgofOGXVlr1BKHRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5b943d93e.mp4?token=JK2aXHNvCtXhA0VyxWBB_HG16DKAKzhk3XfCr4ItmJ_Xw9YhW5ydH7zgcItZWAwAxqUPPOhAaMkfJHirJnBk5zIy6cJVaPE1xK0jPT5TMmgfjiU8zk6GS9DNZaHwmVajw6xLb7KNPBElqmgp07TRo1cL6oIlqovsOmTmnliavYpymg132GeRLOY80xfU75dFRT6w3JYH9e20SEY9fKdIaCkCHMBpdzz6XXEbok_FKSKr9emvR5R141ZqQyjLJRXUeaPkqIhxNrSUgmauK1AeDFhr8tUGK_OgeT9gPISW0fBNHW_4H2wYS7Vd7azkNW25g3W8i9IgofOGXVlr1BKHRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ برای تماشای فینال به ورزشگاه مت‌لایف نیوجرسی رسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/136244" target="_blank">📅 22:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136243">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
⚽️
🔥
مراسم اختتامیه جام‌جهانی آغاز شد  پ.ن فقط 45 دقیقه تا شروع بازی نهایی جام جهانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/136243" target="_blank">📅 21:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136242">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKWmvMBaKln3Xc_GPtK9PCj_LSIyjXJ5aRuWEr-KznVW_bDPZ84WTNt5KwYo399wsQlPi0akxeW7BQ1BeImh5jajByn9s_eYaA9ruGWvw2TSDNxEDMOXPbpnWG_ZFSTSZEOCA1kZGrLgYJo6Z9lADrLairC8ZNmg82Xnn6dvu2MJlk2tFuk1q4u4veJXBL69dRatdcN_slez7vpw-52ZlKhfSFU8Pk-tzDbeFG5FAngmYUMM76BcX5rfut0A2gd1zvCOxkyF4mqCm4f-8V1VJ2jPuGWlJ76x1BSASjXR6hGawFa3OzGn1JY-o1XGPJeSbyQF3JoRfU_f2Y5msA_45A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
🔥
مراسم اختتامیه جام‌جهانی آغاز شد
پ.ن فقط 45 دقیقه تا شروع بازی نهایی جام جهانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/136242" target="_blank">📅 21:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136241">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a92f2cfaf9.mp4?token=fUBCgxuFqpdzJvg__9nbU-Scd3K6Tbonv5ZHjRBSWlREPKuj6P_yr3_olJ2EI_uZbrbPfyUJXSmXPVDQY3kjxAqh3Y9sz-HjpcHpJ9SFHfu01Uyadx84G0CQWvyHkAKuCBb7QGVHlsRv9_Fy8UPLhAu_ODzD3wiCRDIDDrgWggQh-aNURpBzR81MHg6X4nDNDm8h2XbbEYajI7du0Ru_905i4ZZO-219xfmVV1vSgJdRH78MMto_g1chb6Kz0POVy0JjrM11f5KyiOgp0USGeuApy6QxVMml84wHty8v-1nBA3uykAPQDEoios83PZRjDNG9EcTAX7UkxGSBEbC-_XG1PPwDyzlQ2zGPccHChspmhhC3pC-RO66n-dpNxXsY13CqEiw4s3gD2GaGANxlqivLRD3ywfPQfebfHkZtsa1XSnDmiSVlntBduHlRCzqRzUD9CRP1R2iaWB3Ny-RwVOSO6509qEgCOWJJ7EuB06ohVj8s5bBBR8sgbg4kCXhWFhlKX-h6EWhFuSBIL4pLcSjJ6lx121GE7N8zIBtOg2u6x5wvGjrlWuZSeftJgWMZLeCenJQisPh9PBXPvtwqP7obweXibTqU4O2LylSkYagdQP4Fp8jw7F-iTUJ2cVlYc1HXnXNKjH06wCfgUcycNONRO3bem4beendTYWdRUVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a92f2cfaf9.mp4?token=fUBCgxuFqpdzJvg__9nbU-Scd3K6Tbonv5ZHjRBSWlREPKuj6P_yr3_olJ2EI_uZbrbPfyUJXSmXPVDQY3kjxAqh3Y9sz-HjpcHpJ9SFHfu01Uyadx84G0CQWvyHkAKuCBb7QGVHlsRv9_Fy8UPLhAu_ODzD3wiCRDIDDrgWggQh-aNURpBzR81MHg6X4nDNDm8h2XbbEYajI7du0Ru_905i4ZZO-219xfmVV1vSgJdRH78MMto_g1chb6Kz0POVy0JjrM11f5KyiOgp0USGeuApy6QxVMml84wHty8v-1nBA3uykAPQDEoios83PZRjDNG9EcTAX7UkxGSBEbC-_XG1PPwDyzlQ2zGPccHChspmhhC3pC-RO66n-dpNxXsY13CqEiw4s3gD2GaGANxlqivLRD3ywfPQfebfHkZtsa1XSnDmiSVlntBduHlRCzqRzUD9CRP1R2iaWB3Ny-RwVOSO6509qEgCOWJJ7EuB06ohVj8s5bBBR8sgbg4kCXhWFhlKX-h6EWhFuSBIL4pLcSjJ6lx121GE7N8zIBtOg2u6x5wvGjrlWuZSeftJgWMZLeCenJQisPh9PBXPvtwqP7obweXibTqU4O2LylSkYagdQP4Fp8jw7F-iTUJ2cVlYc1HXnXNKjH06wCfgUcycNONRO3bem4beendTYWdRUVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ادامه حملات عادل فردوسی‌پور به قلعه‌نویی: هرکه از "غار" حرف بزند، قابل توجیه است؛ به جز آن کسی که کل جنگ را در دبی و ویلای آلانیا گذرانده باشد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/136241" target="_blank">📅 21:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136240">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
پست خداحافظی رضا شکاری با چاشنی ناراحتی: خداحافظی همیشه تلخ است، خداحافظی از گوهر کمیابی مثل پرسپولیس تلخ‌تر...
📍
موفق باشی
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/136240" target="_blank">📅 21:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136239">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❗️
قدوسی: ابوالفضل رزاق‌پور گزینه اول جانشینی میلاد محمدی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/136239" target="_blank">📅 21:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136238">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✅
✅
عادل فردوسی پور :
🔴
آقای قلعه نویی من و تیمم چه جنگ دوازده روزه چه در این جنگ تماما داخل تهران بودیم و تکون نخوردیم ولی شمایی که یا تمام جنگ یا امارات بودی یا توی ویلای شخصیت داخل ترکیه حرف از غار بیرون اومدن نزن. من تماما کنار مردمم بودم ولی شما همش توی…</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/136238" target="_blank">📅 21:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136237">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❗️
واکنش قلعه نویی به تصویر ساعتش در جام جهانی که باعث حاشیه شد :
🔴
اگر یک سرمربی ساعت می بندد و لباس خوب می پوشد که اشکالی ندارد/ اگر من زنجیر طلا می انداختم و یقه پیراهنم را باز می گذاشتم آدم خوبی بودم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/136237" target="_blank">📅 21:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136235">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
افشاگری خداداد عزیزی از امکانات تیم ملی قبل از جام جهانی:
❗️
به من گفتند بهترین امکانات رو داشتن، شما اگر از امکانات آمریکا انتقاد دارید در کاخ سفید جلسه میگذاشتید والا، 15 روز قبل از مسابقات 400 میلیارد بودجه گرفتید، 1000 میلیارد از رئیس‌جمهور درخواست…</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/136235" target="_blank">📅 21:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136234">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9106b20ac9.mp4?token=SFNMEYiehZkvZncVWSyviPjemRos7MUfHUqGA0gfflrVv-JSMsBrTAAbdfVedaUv_MA250UpO_pE42R5bClqSZFIw1XV3gjWXtb1dHj5SbQVWUIwtgIoMvQn9PCWqN7C4nxJNt9wq3m_dCL42ZlCSjWOgfaO9n7nzrrltCTjeH-dnl9W-f-WH2orGPuoXU0zdSpCCvOnh2I2rgAoqP_Lmalu-P4hGTEtlEByo5YsIcxylIXDm-ohadB28heStfj5xmaBfy7uvhnPdyxkc0s9aZj1L_WRWVKD3DPemWZD2wyWsTaa35ip_4ltWSg7OW-9T2PTuljXnMwV4V4LJtbAw4_xOWrUSX0mp_MtLfqZ3ln8uC9BVb_Ac0yw-wKVwMs03_iHi2cixeHD3lfFdl1Hos34q2TQPrZSW0KdGLtTMNNL8VGdcYYPZGylUci1JDCRUft5-pU7FhHNOW1b_IGh2t_WysLW-3dHM4NIdDKs0aYVCwTMGgprmYmvxVQgZgyhTzgTHMrbDE3yEZurbIayVrDMbkFfGyfMLwe0ZQzEYJoTnDIqtp67NXzbnC7w-CTgvmXN4hqqeSlZURwgFKG3ZWRDO33Gdhdo3yN3V05TM5p8bRdKV9SccFHW2I5VHrGzTkQ9pFAjXIS6hWAuao29iJFsEWrGZbexacEobET9Ulk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9106b20ac9.mp4?token=SFNMEYiehZkvZncVWSyviPjemRos7MUfHUqGA0gfflrVv-JSMsBrTAAbdfVedaUv_MA250UpO_pE42R5bClqSZFIw1XV3gjWXtb1dHj5SbQVWUIwtgIoMvQn9PCWqN7C4nxJNt9wq3m_dCL42ZlCSjWOgfaO9n7nzrrltCTjeH-dnl9W-f-WH2orGPuoXU0zdSpCCvOnh2I2rgAoqP_Lmalu-P4hGTEtlEByo5YsIcxylIXDm-ohadB28heStfj5xmaBfy7uvhnPdyxkc0s9aZj1L_WRWVKD3DPemWZD2wyWsTaa35ip_4ltWSg7OW-9T2PTuljXnMwV4V4LJtbAw4_xOWrUSX0mp_MtLfqZ3ln8uC9BVb_Ac0yw-wKVwMs03_iHi2cixeHD3lfFdl1Hos34q2TQPrZSW0KdGLtTMNNL8VGdcYYPZGylUci1JDCRUft5-pU7FhHNOW1b_IGh2t_WysLW-3dHM4NIdDKs0aYVCwTMGgprmYmvxVQgZgyhTzgTHMrbDE3yEZurbIayVrDMbkFfGyfMLwe0ZQzEYJoTnDIqtp67NXzbnC7w-CTgvmXN4hqqeSlZURwgFKG3ZWRDO33Gdhdo3yN3V05TM5p8bRdKV9SccFHW2I5VHrGzTkQ9pFAjXIS6hWAuao29iJFsEWrGZbexacEobET9Ulk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
افشاگری خداداد عزیزی از امکانات تیم ملی قبل از جام جهانی:
❗️
به من گفتند بهترین امکانات رو داشتن، شما اگر از امکانات آمریکا انتقاد دارید در کاخ سفید جلسه میگذاشتید والا، 15 روز قبل از مسابقات 400 میلیارد بودجه گرفتید، 1000 میلیارد از رئیس‌جمهور درخواست پول کردین و چجوریه که فقط می‌نالید و ما رو سیبل می‌کنین؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/136234" target="_blank">📅 21:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136233">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cce783d5f.mp4?token=sMX8KmxRxSnXEy3mjyNEeIWuX5d49lqhB3FlY07Ouy25pCeyRVTq9Cj8iN-Ja2Ugd-VHtklzssot4-XgWQaUSQmEkYD5ttozAfZ9o_s5fXV8QeQXwkNaE7G0gGiIX0TFwaV3bgJ1ZQf9TTcQ9g2x5dJbC8DoJaCVgQSkdZz9b0D_XLwnDKWzr75qw8qAO2v2_p4aOXHy3OrdaWexg22GvYAfbkCjANzrHUZgUwKn1gEsCmBMo4bnDBhunFLlIQ91xGweL44kShHb-74qNv8vJMYb_oonCpPAcgqbaEPbwUDP2C9afPddBWTLUUsGvQtSHTUR0hqBwKFXcGwd7mCEGq33DFgG1lhTNOj35k2XxAj3WeZqsNfuzFI6QYpO8K5cNdWvN6y5uGiPeV-CBWV1_89Dha1ffWGon7vvIKYE1OFSqdXLkWrnJbi6OQLGZKa86owT4UsIW3gFO3DAUPD4wlo8EhQuFaCzhxhmruJCv3F8_rmSQ0kbEcix3nkOkH6Fd3Wou7GkZaF7Yh2po3C1j3JplZK9b7cW8gDy6gRT8S_M6JYIFsJCUtfshibhicQ6TeZhNN7kgdZsduY9Y0bymE8XhOl_xPzY_PpoVML2vtXppSQEuGyI4GRnu8mAT13VHSmdnZYjKz3bIflAqIbaxmT3iHGOPVzQs4ywRJznIKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cce783d5f.mp4?token=sMX8KmxRxSnXEy3mjyNEeIWuX5d49lqhB3FlY07Ouy25pCeyRVTq9Cj8iN-Ja2Ugd-VHtklzssot4-XgWQaUSQmEkYD5ttozAfZ9o_s5fXV8QeQXwkNaE7G0gGiIX0TFwaV3bgJ1ZQf9TTcQ9g2x5dJbC8DoJaCVgQSkdZz9b0D_XLwnDKWzr75qw8qAO2v2_p4aOXHy3OrdaWexg22GvYAfbkCjANzrHUZgUwKn1gEsCmBMo4bnDBhunFLlIQ91xGweL44kShHb-74qNv8vJMYb_oonCpPAcgqbaEPbwUDP2C9afPddBWTLUUsGvQtSHTUR0hqBwKFXcGwd7mCEGq33DFgG1lhTNOj35k2XxAj3WeZqsNfuzFI6QYpO8K5cNdWvN6y5uGiPeV-CBWV1_89Dha1ffWGon7vvIKYE1OFSqdXLkWrnJbi6OQLGZKa86owT4UsIW3gFO3DAUPD4wlo8EhQuFaCzhxhmruJCv3F8_rmSQ0kbEcix3nkOkH6Fd3Wou7GkZaF7Yh2po3C1j3JplZK9b7cW8gDy6gRT8S_M6JYIFsJCUtfshibhicQ6TeZhNN7kgdZsduY9Y0bymE8XhOl_xPzY_PpoVML2vtXppSQEuGyI4GRnu8mAT13VHSmdnZYjKz3bIflAqIbaxmT3iHGOPVzQs4ywRJznIKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
خداداد عزیزی: صداها را نمی‌توان خاموش کرد، مردم ایران غارنشین نیستند، آقای قلعه‌نویی ما جنگ رو دیدیم، بهترین کار این است اسم ببرید، شما نتیجه نگرفتی چرا میندازی گردن ما گردن رسانه؟ تنها جمله درست شما در مصاحبه عذرخواهی از مردم بود، دوباره در جام ملت‌ ها من طاقت عذرخواهی ندارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/136233" target="_blank">📅 21:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136232">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
🔴
🔴
فوری| وزارت خارجه قطر: پیشنهاد جدید آتش‌بس را برای ایران و آمریکا فرستادیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/136232" target="_blank">📅 21:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136231">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
🔴
🔴
فوری| وزارت خارجه قطر: پیشنهاد جدید آتش‌بس را برای ایران و آمریکا فرستادیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/136231" target="_blank">📅 20:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136230">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6549a463.mp4?token=RLJfdy1A7DtUuG0xQSYXxR1XcWUSu3II653Kqlok1K2bsqd2bGq7bscaSbQF5xI2CUYrVbsj_OqevypnPSVKdPHUF7sKKI4uYiBXPe_VHgwW21qcf5jvnmls1P12rCM4mlYAS3EBHMlUcWvIh_l44_dsbkV2GCE0pU4MKYoRcWtJbOrIGJv5nNOr7L-H_33CqqsBEw2KAvJfZCzQD40vPxwoMIDCFxC_OlcB0dnswFSUPTdY7GaYn4PBYg8oMbDnTZRQH-xiBIJJKjXDC4iQCtX6aBJAntfnlEdth1BBbnHMmbT9OuCIQ5V9FIuRWjr66clMDGqspIHfN2f3dIDasA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6549a463.mp4?token=RLJfdy1A7DtUuG0xQSYXxR1XcWUSu3II653Kqlok1K2bsqd2bGq7bscaSbQF5xI2CUYrVbsj_OqevypnPSVKdPHUF7sKKI4uYiBXPe_VHgwW21qcf5jvnmls1P12rCM4mlYAS3EBHMlUcWvIh_l44_dsbkV2GCE0pU4MKYoRcWtJbOrIGJv5nNOr7L-H_33CqqsBEw2KAvJfZCzQD40vPxwoMIDCFxC_OlcB0dnswFSUPTdY7GaYn4PBYg8oMbDnTZRQH-xiBIJJKjXDC4iQCtX6aBJAntfnlEdth1BBbnHMmbT9OuCIQ5V9FIuRWjr66clMDGqspIHfN2f3dIDasA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله شدید‌اللحن خداداد عزیزی به قلعه‌نویی: شما فرشته ما شیطان؛ شما خوب ما بد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/136230" target="_blank">📅 20:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136229">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❗️
❗️
فوووووووری/ارتش آمریکا در پاسخ به نقض آتش بس از سوی ایران، اهدافی را در جنوب ایران هدف قرار داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/136229" target="_blank">📅 20:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136228">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMAY5HFdt3GoHhwfbii1JAD0MfwBWvXDW0IPalpChop_1P-xbxgnRH1sWrriGUNxTy93Qy256B2LQNNVl-96NuZi8o59HejqqSiokt4KmsYzpVheq23V1wRcBhvZoknNYZ1V_1LjcKbwS7oHMIci0eCB9g9DyjFp5OzITksvrzpxOa4ZOU-rCUXAuiDK7CAzf7dwDiZ1h19OwTek7rJsrjI8jz2-AoAWKJfsKWJe-4rW1n3WrpPviV8PpcGvnk7MjkaMG2n82PtJaE3afNPG54DqlRJ9v1kpkWMXypg8rQOPa6Zq7-TdHjuEgaCC4pKNFcijVvL9RtAYUAlVnvYBqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔖
تصاویری از احد میرزایی عضو هیأت‌مدیره پرسپولیس منتشر شده که داره توی ساختمون باشگاه یکی رو کتک می‌زنه…اقای احمدی همین فردا دکمه ایشون رو بزنید
❌
پرسپولیس چاله میدون نیست، ایشون ادم زنوزیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/136228" target="_blank">📅 20:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136226">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
رقم قرارداد دانیال ایری،‌بالاست، ولی می تواند قرضی به پرسپولیس بیاید. او بند خرید دائمی در نیم فصل دارد و بنظر می آید نساجی مایل به فروش کسری طاهری است. ضمن اینکه جذب علی نعمتی و قریشی هم قبلاً کنسل شده بود
✍
قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/136226" target="_blank">📅 20:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136225">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
#تکمیلی؛ باشگاه‌تراکتورتمام‌توافقات لازم رو باخودِ علی ‌قلی‌زاده برای قراردادی سه ساله داشته و تنها رضایت نامه این بازیکن باقی مانده که مالک تیم تراکتور قول داده ظرف 48 ساعت آینده مبلغ توافق شده رو به حساب باشگاه لهستانی پرداخت کند.
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/136225" target="_blank">📅 20:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136224">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❌
❌
باشگاه تراکتور مذاکرات مثبتی با علی قلی‌زاده، ستاره ۲۹ ساله لهستانی، انجام داده. او قرار است ۷۰۰ هزار دلار به عنوان رضایت‌نامه به باشگاه لهستانی پرداخت کند و سپس به صورت رسمی به تراکتور بپیوندد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/136224" target="_blank">📅 20:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136221">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
❌
باشگاه تراکتور مذاکرات مثبتی با علی قلی‌زاده، ستاره ۲۹ ساله لهستانی، انجام داده. او قرار است ۷۰۰ هزار دلار به عنوان رضایت‌نامه به باشگاه لهستانی پرداخت کند و سپس به صورت رسمی به تراکتور بپیوندد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/136221" target="_blank">📅 20:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136220">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
❌
باشگاه تراکتور مذاکرات مثبتی با علی قلی‌زاده، ستاره ۲۹ ساله لهستانی، انجام داده. او قرار است ۷۰۰ هزار دلار به عنوان رضایت‌نامه به باشگاه لهستانی پرداخت کند و سپس به صورت رسمی به تراکتور بپیوندد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/136220" target="_blank">📅 20:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136218">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47bce486c0.mp4?token=qs7S18iJfMxgCWcJUrhDLnlHGU9sDTzeXV3jpsL9X05tMI6GhgJyYAyiiJSAoH-dnS1_12O69B-p8gnaAYffYt0JKDRrQmx8SaK-bvXbh1_4Ba8OvWpDHUtBu2K1bTQdW_ePu-iJeRd-otb8bNRLEOvlCxWSXi0kShGXad6CZ8yE6FcbyuvMPKOvJV7ipsin7mKexjax9NHKckk6fvpRX2K0od2-f8bBXehJ8wbMe0Awi5cIfjdz2e4od-mX_J9RqJxHFNRc-wD24tBlwc9h8vWkfs5O8Hg0Vc1RzZHSk8ybd9lHkamF22nTBztekQJO335h5GGYmamqAjEG6n7P4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47bce486c0.mp4?token=qs7S18iJfMxgCWcJUrhDLnlHGU9sDTzeXV3jpsL9X05tMI6GhgJyYAyiiJSAoH-dnS1_12O69B-p8gnaAYffYt0JKDRrQmx8SaK-bvXbh1_4Ba8OvWpDHUtBu2K1bTQdW_ePu-iJeRd-otb8bNRLEOvlCxWSXi0kShGXad6CZ8yE6FcbyuvMPKOvJV7ipsin7mKexjax9NHKckk6fvpRX2K0od2-f8bBXehJ8wbMe0Awi5cIfjdz2e4od-mX_J9RqJxHFNRc-wD24tBlwc9h8vWkfs5O8Hg0Vc1RzZHSk8ybd9lHkamF22nTBztekQJO335h5GGYmamqAjEG6n7P4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
واکنش قلعه نویی به تصویر ساعتش در جام جهانی که باعث حاشیه شد :
🔴
اگر یک سرمربی ساعت می بندد و لباس خوب می پوشد که اشکالی ندارد/ اگر من زنجیر طلا می انداختم و یقه پیراهنم را باز می گذاشتم آدم خوبی بودم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/136218" target="_blank">📅 20:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136217">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✅
تصویری از خانه دروازه بان کیپ ورد...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/136217" target="_blank">📅 19:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136216">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✅
شنیده ها :دو تا از بازیکنان ملی پوش و با تجربه پرسپولیس با سامان قدوس تماس گرفته و در تلاش هستند که او به پیشنهاد باشگاه پاسخ مثبت بدهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/136216" target="_blank">📅 19:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136215">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6SpArj_4X9XeqhMHSFdNtIRLTmBvrJ5jpfcp-x3gsJ8JEK1-fS24rbKyYn7jsuXFyfJaFcS7ZCH_nHK8kVyrmTanlWCp5Qc8_DyW9FVhFsPiwt5n_6W9_OYmNLcGQnQjn3citWCLjxLebPVt6j_7Sl1mw3wS6w1TunW2B79GdKgQwPCf6pObqxQp1Ofu3RNsLEei3FKWxzwCfGj5W4KyIe4XYkm3zM68c_oPbb0cQI8m_bfeciptKO0mXzvHLjWe3dKTyeIuTK8pGwAvKqmR-XI94F05EJHk6dA40Aya-LUkM6xVRR6wimFvsCYjRCGeFMkA1pfgDYvHSnUTuriQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
❗️
یه سری عکس منتشر شده که نشون میده احد میرزایی، عضو هیأت‌مدیره پرسپولیس، با یه نفر درگیر شده و باهاش گلاویز شده. ظاهراً این اتفاق مربوط به گذشته‌ست، ولی بازم خیلی‌ها معتقدن برای یه مدیر باشگاه پرسپولیس چنین رفتاری عجیب و قابل انتقاده.
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/136215" target="_blank">📅 19:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136214">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
مذاکرات پرسپولیس با احمد نور پیشرفت خوبی داشته و درحال حاضر تنها مورد رضایت نامه ۸۰۰ هزار دلاری این بازیکن است که باشگاه پرسپولیس تلاش داره کمش کنه /ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/136214" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136212">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
🔴
مذاکرات کوشکی با استقلال مثبت نبوده و پرسپولیس و یه باشگاه لهستانی مشتری او هستن/ورزش‌سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/136212" target="_blank">📅 19:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136211">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a174835238.mp4?token=I01F0cmQ3TOxPuQuI1p-7ZhpUVwJBByBMPasvzfMDG9NhCXRGg2wK8iZ1u058MNWJBUSu78dlMI28i2jTbl0p0vPn8BUNIZA4rLSQFBfDba5oiS5w5QbG_XkmEYpBlXfbbrVSuLgihfTl-f8BlQu_JOL4rhwS59YAWy1Ve_Gn-qZQk0QPX0LfNjA729TP1et9v1n6oacUgIbqnXIpx-yKtEt6Ym_EsES8idb73z0PT2-xR1VM7psRfx4NZ9fA83VQk0cHVuRO4RsUasES2rQycE-PoHlzyL-U3NWwIhaBK6h6eqt2yZuBOm8TcrqWe4oEviln92r6Z633MoMvzER7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a174835238.mp4?token=I01F0cmQ3TOxPuQuI1p-7ZhpUVwJBByBMPasvzfMDG9NhCXRGg2wK8iZ1u058MNWJBUSu78dlMI28i2jTbl0p0vPn8BUNIZA4rLSQFBfDba5oiS5w5QbG_XkmEYpBlXfbbrVSuLgihfTl-f8BlQu_JOL4rhwS59YAWy1Ve_Gn-qZQk0QPX0LfNjA729TP1et9v1n6oacUgIbqnXIpx-yKtEt6Ym_EsES8idb73z0PT2-xR1VM7psRfx4NZ9fA83VQk0cHVuRO4RsUasES2rQycE-PoHlzyL-U3NWwIhaBK6h6eqt2yZuBOm8TcrqWe4oEviln92r6Z633MoMvzER7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/136211" target="_blank">📅 19:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136210">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
❤️
🤩
طرفداری: احد میرزایی بزودی توسط مالک بانک شهر به سمت درب خروج هدایت خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/136210" target="_blank">📅 18:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136209">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eda321934.mp4?token=loCZzIyRY7xV1X7owQS1XRj4XF0AEO4tPT_F56hQa2ckzhy8i0aVVHvlwOhOpWsOPlZpA9LM6Rn2oIsZRqoGSvJv2jhbJkjNFrA4I2br1_qdl8EmTX7T0WDqcxK0IJisNdsz1jPg3GuXxHbB1Rjm0Eh82twHOfA7B5HfMGcjSYF2GiNK56SmOKuX9ePmQrW9TEQHq6NSKvJfQWVSWfPPWb41gUP7oO2MVzmM1MqCGo6SkhBQ9_7_NGyvRWwW-DPVQMKxWWKZxWpE6rWO8UFHBwKSuxL3y1qTyKtXVaLcnd7fzcOu2aGKX3EacNQdTwBHHNFed01T60nAb-DUt5fAVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eda321934.mp4?token=loCZzIyRY7xV1X7owQS1XRj4XF0AEO4tPT_F56hQa2ckzhy8i0aVVHvlwOhOpWsOPlZpA9LM6Rn2oIsZRqoGSvJv2jhbJkjNFrA4I2br1_qdl8EmTX7T0WDqcxK0IJisNdsz1jPg3GuXxHbB1Rjm0Eh82twHOfA7B5HfMGcjSYF2GiNK56SmOKuX9ePmQrW9TEQHq6NSKvJfQWVSWfPPWb41gUP7oO2MVzmM1MqCGo6SkhBQ9_7_NGyvRWwW-DPVQMKxWWKZxWpE6rWO8UFHBwKSuxL3y1qTyKtXVaLcnd7fzcOu2aGKX3EacNQdTwBHHNFed01T60nAb-DUt5fAVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">💢
کاظمیان + رفیعی میرن گل‌گهر پوریا لطیفی فر میاد پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/136208" target="_blank">📅 18:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136207">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
میلاد محمدی در یک غافلگیری با عقد قراردادی یک و نیم ساله به  مکس لاین ویتبسک بلاروس پیوست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/136207" target="_blank">📅 18:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136206">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❗️
قدوسی: ابوالفضل رزاق‌پور گزینه اول جانشینی میلاد محمدی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/136206" target="_blank">📅 18:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136205">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U2SpFK7e9Q8H_syardcORimmGIE74OvRRyGh2d0Axgf7JDXlyr7tkHaRiifGcNiWfMlnVKMSGe5qHlWoOr_sM6PMzjyQedc-WFjBFXlwwhRqaXc8EtVC8Al3AvNqSq0QqRVl7L55ZManIIAAz4KlNIsWoa_YXo8FuIlFrQrtmQfVf4F4nQfX78_1JgdJr86-zStZq8Q3Xosm7Iqx9SJeKFO9UTx9HTDPXozCBxV5TFb1WYOkKYs36lzKZVst9WJvRy0XOvAZ5fFnG5vswn5mopbPT5MfDf58CN-9nA8qMEyrfEHxbzzt6ecVbHvXy5HNA9KRysh1oxTNErTxZxg4zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
قدوسی: ابوالفضل رزاق‌پور گزینه اول جانشینی میلاد محمدی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/136205" target="_blank">📅 18:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136204">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
میلاد محمدی در یک غافلگیری با عقد قراردادی یک و نیم ساله به  مکس لاین ویتبسک بلاروس پیوست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/136204" target="_blank">📅 18:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136203">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rc52rwhzSJerB3-CxXj0inTjpkEgv25mAjSn5rY3wXMxfXQbzgYmyer-A3xlKkW5nwqwmUjW5RmrULw6Bf0YytHrjvGA3Td33qkk4-7F9Ytrm4JNPHwqOQzpEGipDI9VR6a8c4wbexW4QCNMZKeKyZDJdjkzG20uGPQZzbzabyQd-gwclQ-7rCE2GTL74BWIF6IIev-n9xE1Yiaail-r_PEXGf7MQijFRDuyg0ma4QMjAYQBBE6lufBFvdv82l7hmvPOXvH8W7fuVB71-earC3-90e_A7ECSEmyeu462zwG6BRMN-jQhpFkl_ltlPjvPAS3N5onriJ3y6X_524ZKKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
میلاد محمدی در یک غافلگیری با عقد قراردادی یک و نیم ساله به  مکس لاین ویتبسک بلاروس پیوست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/136203" target="_blank">📅 18:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136202">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🏅
خب میلاد محمدی هم ترجیح داد به جای پرسپولیس به لیگ بلاروس بره
❌
رسمی؛ میلاد محمدی مدافع سابق پرسپولیس با قراردادی یک و نیم ساله به  مکس لاین ویتبسک بلاروس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/136202" target="_blank">📅 18:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136201">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIzXgxXPW0BGn3DDRzN0s2SA3xFMJG8EOuvmPx9sCcEZcCFviLZ7qew0rQQd_4EXBMZWiw8INVo4giyJxvTFb3hW2ZmVYkHs-cIfNUDxLIRzmGGcmCubtjuHe4opo3tF59km-YIW0Zq5h_Mrw8jFmplItQ24frSQATFCaM14J-VVzQmMt-np1d5Yb1KyNWxGBFahq5qfrJFADW9rnClaco-MOP0w8h7w936mWH3lyX2555Q1bUpZ9EDomXUiL7v2AwV7EMdRMAZGJOhlpZaBnaQI-bRuBPYC5ml2a39iayrIDZ25xKdbKMjX7mqGNXsu4b4XJKB3Ho_AQlveEg9D2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
خب میلاد محمدی هم ترجیح داد به جای پرسپولیس به لیگ بلاروس بره
❌
رسمی؛ میلاد محمدی مدافع سابق پرسپولیس با قراردادی یک و نیم ساله به  مکس لاین ویتبسک بلاروس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/136201" target="_blank">📅 18:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136200">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
غیررسمی: محمدرضا اخباری با قراردادی 1+1 ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/136200" target="_blank">📅 17:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136199">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❗️
❗️
درصورت عقد قرارداد تیم پرسپولیس با آلن هلیلوویچ این بازیکنان جانشین سروش رفیعی در این تیم خواهد شد. پست اصلی هلیلوویچ هافبک تهاجمی - بازیساز است اما در پست وینگر و حتی مهاجم نیز بازی کرده. احتمال عقدقرارداد زیاده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/136199" target="_blank">📅 17:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136198">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✅
✅
از تمرینات پرسپولیس خبر رسیده دنیل گرا را در پست هافبک دفاعی و دفاع چپ در حال تست هستند اگه جواب داد بمونه!
🔴
گرا برای جدایی درخواست مبلغ ۵۰۰ هزار دلاری کرده مدیران پرسپولیس برای اینکه غرامت ندن فشار اوردن گرا بمونه اما تصمیم آخر مهدی تارتار میگیره
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/136198" target="_blank">📅 16:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136197">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❗️
آمار افتضاح تیم ملی والیبال در لیگ ملت های امسال :
🔴
12 بازی
🔴
3 برد
🔴
9 باخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/136197" target="_blank">📅 16:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136196">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jxjibh2hbbqrka89rTqVKyK3rLFOTnjuPf1DXFlv4KhrsnF5VfrzOlHotMdZGyP5EBTo2GKsDuCZtIrp4z9CEHLaLlXQ9U0YCHZa69C_1up1Se8wGCuc9wnsfhmTmiDSP5f7GSu8v8VOh1cQki7nEUmYXWobkqAX8JpgDOGoj5TSWQV8eUMg2Y63lkqNfXk2RnHIyR8epf5kI3wvYIDlS6wM09ABUPKvurjtNc8615mjynsinmyQOZP0vLhY8RjPYInfbbuI3bGirTNGL2c8yRA8AIrCJGQY_gcvAlDH0GqkzLlOq1p3l6Vlk9s529nJMUnhR4tNZp7ciVyIcLlt2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رقم قرارداد دانیال ایری،‌بالاست، ولی می تواند قرضی به پرسپولیس بیاید. او بند خرید دائمی در نیم فصل دارد و بنظر می آید نساجی مایل به فروش کسری طاهری است. ضمن اینکه جذب علی نعمتی و قریشی هم قبلاً کنسل شده بود
✍
قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/136196" target="_blank">📅 15:22 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
