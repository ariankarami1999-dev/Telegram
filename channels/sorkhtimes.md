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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 22:18:40</div>
<hr>

<div class="tg-post" id="msg-136339">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
خریدهای لیگ‌برتری پرسپولیس تا به امروز: مهدی‌تیکدری‌نژاد، سیدمجید عیدی، پوریا شهرآبادی، ابوالفضل جلالی، پوریا پورعلی؛ هر باشگاهی هفت سهمیه لیگ برتری و سه سهمیه بازیکن آزاد داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 908 · <a href="https://t.me/SorkhTimes/136339" target="_blank">📅 22:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136336">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
🤝
پرسپولیس تا آخر هفته با چهار بازیکن جدید قرارداد امضا خواهد کرد / خبرنگار فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/SorkhTimes/136336" target="_blank">📅 22:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136335">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/SorkhTimes/136335" target="_blank">📅 22:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136334">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/SorkhTimes/136334" target="_blank">📅 22:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136333">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">جالب اینه تموم فرم ها رایگانه، حتما عضو شین و‌ چک کنید چقد راحت سود میشه کرد
😉
✅
JOIN JOIN JOIN
JOIN JOIN JOIN</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/SorkhTimes/136333" target="_blank">📅 21:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136332">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfhOdHVKIRIAEP4XNiPwRfJ1NrxcH23BZ8M8XVulTzEr3jadP5XcWkxP39M-QK3KC_DYOtNXRbhFO21XL_TweT-dLsYqlpuY0S_tO8a5VsnuO05BDWF9NgU-P59qEmUSpWSoAe10tmzX-C4fzxJhqL7NMbAaUNiyVjVl_SrJe4j8oqOPi_D5pUMyicjpi3ZHn5ktsh0jtmnq671opap264eFe54sqQlJKNdFxS0-rqdaV-_qmSiTcCMSGjA9nlYJi2chG_6bQoN4VFvV6-cYdWZgamZQfarcmrQt_85kh-xtopLvW5RZYLDTmCcUiwxIJ6OPngehBXTyoAWXjJfsaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب حتی با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
میگی ن ؟ بیا تو چنلمون و ببین
🤷‍♂️
@PeakyBetBlinders
@PeakyBetBlinders
@PeakyBetBlinders</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SorkhTimes/136332" target="_blank">📅 21:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136331">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1NRNkzJyRUurrH9QNryxREdLdpeMRELUpqyuo5Ifu_faL-E-ekx8cLywlkT4AgLerg4MpoB8bRzDFS4cHU4vvAWp38N9Tbadx0L2lrX0s9yvu9WDszklwnP-sgFZdgMJT7Q1jxEYtR48CvCiK10MKsZKS9zQUSZk2F3JMzcURsCZvCqIBGJww__b2MU-bNW1dPoF6iXlRzLevOacdVpndjJHFn8C2xnIjW9pBqyUx0n-V5MNoJROT_70okctiicPde-DhUi2kh3a-ZA4ECUj9t6Cnj2-342h6pbsNIfStrbntdM4X3M-dx-bcOOElM3HocBvbezF5mecUuQ7DYvNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SorkhTimes/136331" target="_blank">📅 21:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136330">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8zeH6d8KORDSOuSxt6bEUps1zA1kUHdVavLXdcAF-BMDEB5GkFokJjVALqQ6OPTpGtDPEP80iq-aD8nEvg9QWvbJfWljSXKwEpjaBd-wt78jTJGIWT5X4ofORo-aYMt0LWSuyd4rWnAotS_s2msPoqKJrXc4gqym9QfGLF3hI3kfa2ELCeszwYgF_WA6s4yF9T2XWdEQ1yfeJi9wX878F6N7PFEyJ-9wEdE07tfe964pP8tqEx440ShZwx8IjOWwOQSqM-UM4t71rFIR1_LgEC6BXWL4cCYSgHiNSk4asY_9UEE6tVwTyICb7wzCObZJGbIPTia7WoGaRpT_NbojQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تصاویری از تمرین امروز تیم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SorkhTimes/136330" target="_blank">📅 21:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136329">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
شبکه "فاکس نیوز": نیروهای ویژه ارتش آمریکا سال‌هاست که برای ورود زمینی به ایران آموزش می‌بینند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SorkhTimes/136329" target="_blank">📅 21:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136328">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKRoRjZRmEJeAs-iB1rcj63XDo43dLunmpvlDrz9V9UbZyPSM93qGpPykcRWISfDBywhiNHmkzw2qbD-FiUyp6nIbEQUUdLiIrG70Qzjjm77dVvjwSto7tSVP4oX8BT8EUqt3GivZc0ys2CGdcTWTaCZrKZL4EBRibUK06o6LZRBy89pMAOQMHqwMYAftm6-W7cTrIoEfUZ-NRfgM0O21yukPDs7PaBEPvWjEdhz5JY376EFi0psPWr3O0-5KqXffpGgsNm-YdX0fbG9dw_h0jB7FXgbmppAtkHQnuVjDAvBR6WlisMyn5i2eN8rr9uX1RNaPHcO8cpsrhZudvqxuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جام‌جهانی 2030 به‌مناسبت صدساله شدن تورنومنت، با 64 تیم برگزار میشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/SorkhTimes/136328" target="_blank">📅 21:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136327">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✅
سپاهان برای جدایی آریا یوسفی، خواستار انتقال ایگور سرگیف و حسین ابرقویی به این تیم شده که با مخالف باشگاه پرسپولیس رو به رو شده / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/136327" target="_blank">📅 21:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136326">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری از فرهیختگان
🚨
🚨
کسری طاهری در آستانه عقد قرارداد با پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SorkhTimes/136326" target="_blank">📅 21:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136325">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❗️
باشگاه پرسپولیس برای جذب کسری طاهری از فیفا استعلام گرفته و منتظر جواب فیفا ست تا برای جذبش اقدام کنه/آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/136325" target="_blank">📅 20:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136324">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/136324" target="_blank">📅 20:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136323">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
❌
تمام تمرکز پرسپولیس روی جذب محبیه و خیلی هم بهش نزدیکن ولی  اگه اوکی نشه کاظمیان میمونه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/136323" target="_blank">📅 19:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136322">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
شنیده ها:پرسپولیس مقدمات لازم برای مذاکره با محبی رو شروع کرده و این مذاکرات در حال پیشرفته
🚨
جذب محبی نیاز به رضایتنامه باشگاه اماراتی داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/136322" target="_blank">📅 19:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136321">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/136321" target="_blank">📅 19:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136320">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❗️
سپاهان به پرسپولیس اعلام کرد هیچ‌جوره آریا یوسفی رو نمیفروشه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/136320" target="_blank">📅 19:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136319">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
محمدحسین میساکی: درحال حاضر کسرا طاهری رسماً بازیکن نساجی است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/136319" target="_blank">📅 19:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136318">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
فرهیختگان:
🔴
تارتار یه وینگر تکنیکی می‌خواست، اما بعد از مذاکرات با یوسفی، هاشم‌نژاد، لیموچی، کوشکی و چند گزینه دیگه، مدیران پرسپولیس به این نتیجه رسیدن که محمدامین کاظمیان رو حفظ کنن و روی خودش حساب باز کنن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/136318" target="_blank">📅 18:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136317">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❗️
فوووووووووری از حسین قهار
🔴
حسین قهار: هدف از مازاد کردن ابرقویی ؛ بازگشت مرتضی پورعلی گنجی به پرسپولیس است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/136317" target="_blank">📅 18:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136316">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
❌
تارتار از عملکرد حسین ابرقویی در تمرینات راضی نیست و به دنبال انتخاب جایگزین برای این بازیکن است‌...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/136316" target="_blank">📅 18:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136315">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✅
✅
#فووووووووووری
🔴
تارتار علاوه بر پورعلی‌گنجی، برای حسین ابرقویی نیز اعلام عدم نیاز کرده و‌ معتقد است این بازیکن در ضد حملات حریف کند عمل می‌کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/136315" target="_blank">📅 17:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136314">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
❌
فوتبالی: مهدی تارتار به اخباری قول داده اگر توی تمرینات بهتر از پیام نیازمند باشه، فیکس پرسپولیس می‌شود. همین اعتماد به قول تارتار یکی از دلایل اصلی قبول پیشنهاد پرسپولیس بوده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/136314" target="_blank">📅 17:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136313">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/136313" target="_blank">📅 17:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136312">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/136312" target="_blank">📅 16:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136311">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
محمد عمری 3 ساله با پرسپولیس تمدید کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/136311" target="_blank">📅 16:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136310">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
شنیده ها:پرسپولیس امروز 40 میلیارد تومن + رضایت نامه قطعی کاظمیان رو به فولاد برای جذب ابوالفضل رزاق پور پیشنهاد داده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/136310" target="_blank">📅 16:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136309">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLh7MJB9g_PSjHpJX3dgNDr4gWs6TkeRJZWKjiQ_MKqSdpxvEeGC863oZY6bIyZe7XD88VGoNMAeC0AjCl0SBDaEWlj-x52vjazNpCsrluKR3GRZjC98GZ-xhIgGNHnGl7xn6J1Vb2taxg3Q35TYk0mZIOtNP-X7pytM6WIC4ZiueiSX7ane0auIme83eYAgrA4qqL7CDOUXspGa4fKAQHrzT7YJFP4b2Nr7jQEqFOKNMgmYoMiYwcLF-6-nWGZq1rfxyPo6shRVlwyl_04-TUdI7Leeyvt4Kz4Ir_gC4lAloz-tRKCKhtotj1x_WbzYFO7r2cr_ohwUUqOAd6-WxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محمد عمری 3 ساله با پرسپولیس تمدید کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/136309" target="_blank">📅 16:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136308">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❗️
❗️
پرسپولیس برای رزاق پور پیشنهاد پول به علاوه بازیکن به فولاد داده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/136308" target="_blank">📅 15:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136307">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
شنیده ها:پرسپولیس مقدمات لازم برای مذاکره با محبی رو شروع کرده و این مذاکرات در حال پیشرفته
🚨
جذب محبی نیاز به رضایتنامه باشگاه اماراتی داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/136307" target="_blank">📅 15:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136306">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
❌
فیفا ظرف72ساعت آینده استعلام باشگاه‌پرسپولیس‌ونساجی رومیدهد. اگه پاسخ مثبت باشه کسری طاهری بزودی با عقدقراردادی چهار ساله رسما به عضویت باشگاه پرسپولیس درخواهد آمد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/136306" target="_blank">📅 15:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136305">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❗️
❗️
دوره حضور وحید امیری در پرسپولیس برای همیشه به پایان رسید و او از جمع سرخپوشان جدا شد
🔴
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/136305" target="_blank">📅 15:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136304">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❗️
مذاکرات برای جذب محمدرضا اخباری وارد مراحل پایانی شده و باشگاه منتظر حضور این بازیکن در تهران برای عقد قرارداد است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/136304" target="_blank">📅 15:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136302">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/136302" target="_blank">📅 15:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136301">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/136301" target="_blank">📅 14:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136300">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/136300" target="_blank">📅 14:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136299">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
❌
تیم پرسپولیس که قصد داشت فردا برای اردوی اماده‌سازی راهی شهر ارزروم ترکیه شود، با یک هفته تاخیر اردوی خارجی خود را برگزار خواهد کرد.
🔴
🔴
پرسپولیس روز ۳۱ تیر ماه برای این اردو تهران را به مقصد ارزروم ترک خواهد کرد و احتمالا دو هفته‌ای در این اردوی خارجی حضور…</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/136299" target="_blank">📅 14:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136298">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
❌
باشگاه تراکتور مذاکرات مثبتی با علی قلی‌زاده، ستاره ۲۹ ساله لهستانی، انجام داده. او قرار است ۷۰۰ هزار دلار به عنوان رضایت‌نامه به باشگاه لهستانی پرداخت کند و سپس به صورت رسمی به تراکتور بپیوندد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/136298" target="_blank">📅 13:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136297">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/136297" target="_blank">📅 11:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136296">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❗️
❗️
پرسپولیس در یک دیدار تدارکاتی روز سه شنبه هفته جاری به مصاف تیم خیبر خرم آباد خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/136296" target="_blank">📅 11:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136295">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSOo0LKZGlEsplVOd-aB1yH5BUwxvrybX_nmAIQm6lHHszQvVnOv2l1iskdW4CbMQUsKb-900S-dmOkaYGdyTIoCN3zhl9FPOmVpmdVzH2DvabLxYU-sgO2x2SLHjpAO6-E8GjgLkkBthtI5Dqo1wZvq72wnGJChvoJjkZaH6haC-rv-JxMzhjty79shESHjPqbtN978-w7ZfStoUbzkTYaTTVuW1G_RJEJAY5xFktEMjSBDWL8cLrRshYoXNepR8QrGm-ZNFCt1QDDHCP6Hqr5C0bkYWmX06-q-njNT-wDt_NbZ_Hksr6V2xgAJUgISV5AdcoOZw0Bhs9yIVPHwQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رامین رضاییان از ایران با دو گل و یک پاس گل به عنوان سی‌ و هفتمین بازیکن برتر جام جهانی انتخاب شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/136295" target="_blank">📅 11:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136294">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✅
گویا دوره حضور تمرینی وحید امیری در تمرینات پرسپولیس به سر آمد.
🔴
احتمالا از فردا دیگر به تمرینات تیم نمی آید//طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/136294" target="_blank">📅 11:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136293">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/136293" target="_blank">📅 11:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136292">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
❌
پرسپولیس دو پیشنهاد خارجی برای امیرحسین محمودی رو رد کرده و می‌خواد فعلاً نگهش داره. درخواست شماره ۱۰ هم با مخالفت تارتار روبه‌رو شده تا فشار کمتری روی این بازیکن جوون باشه.
🔴
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/136292" target="_blank">📅 09:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136291">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/136291" target="_blank">📅 09:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136290">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uns-T9Bopckmb4OdNh-eqw3UfKDLmWsgE0b-ElomGO4Q46uPJxW31S4gb0Hto2LWiGfTVO8oVhvDRUHGU3mm5MNZtv2gX0S4VV5s7YgyJrM9RrH5gDvpBARiSjen3psKWkDPpD0P2cRILyAjlo0Ovc-zTC_ZcD-o9l8VZALz8Z0w5n7uRcrsDoNfqeyE1uU9W9TX5In-GmoWKLQUKp7GWmzJLRMKxv1N6Hoc1BxhE5LaihGEsrA2pU0DS3NQNTMyiFR-Wr3lfigO5f9t4ko5lAL3L-ttiDp71265GxtOEQG62bdRhx5Yv2zAuR0eno-WnKmNMp6TaaGgxTsipc3dVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
چه قابی شد ...
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/136290" target="_blank">📅 09:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136289">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrR47sgCs2KxMsgALUBEgVDzBBR87IMm2MtjMvvhn6ulKUcCT-hB47RYt3E1jNvu2GOJ6vXQxjMZVOirai3AUyKD-a16_9lfgLO1BSQ0lfJ04Gv2vvDcpBQOh5r5aUWlRcxPcPZknHy79qRU5VZ4LW_aGAWTd7dYj7ti-5TdDdbDFjQd4i95-YZnenzwaL-_DeKtgH07Wel6Grl3utx5_D6jLnu4R1rzNfUj6mGtI6BbbzNxuA8j3PJ8mIha0Aro7xKLZea6wNl7IvXwQFd23ZfPPEyR_y5y7AX5J6HNPHSC3QwXrp6C0gsxlRdIV-PoDdltut0SsKGpwjX5AVMPUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دو زلزله به بزرگی و شدید ۵.۷ و ۵.۲ در کورزان کرمانشاه به فاصله ۵ دقیقه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/136289" target="_blank">📅 09:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136288">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✅
گویا حملات بسیار بسیار شدیدی دیشب به تبریز شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/136288" target="_blank">📅 09:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136287">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
❌
فاکس نیوز: هروقت داور بازی سوت پایان بازی اسپانیا و ارژانتین رو به صدا در بیاره جنگ علیه ایران اغاز خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/136287" target="_blank">📅 09:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136286">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
❌
ورزش سه: محرم نویدکیا رسما خواهان جذب ابرقویی و کاظمیان شده در این بین گفته میشه احتمال معاوضه این دو بازیکن با آریا یوسفی در قبال مبلغی هم وجود داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/136286" target="_blank">📅 09:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136285">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇪🇸
🏆
بالا رفتن جام قهرمانی توسط اسپانیا
💢
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/136285" target="_blank">📅 09:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136284">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/136284" target="_blank">📅 08:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136283">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/136283" target="_blank">📅 02:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136282">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/136282" target="_blank">📅 02:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136281">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWDRK_b3AkLcgf0-zhEpg3qZq3ZSzkxo5GqrJcO280WbiLNeBglyH7yI41fu6-awEzKs2gxOhbMdBPdaJ9CkbnwS_0d-FhJem1sYMzjb1VPyrjWhoHkmYlNS6k-58xhQRu_WnIFlGBFrrEBskRM2zxj_vSoEc7Ewys1Pk_dKO8IcnH0PmvUxSJKPWxxwCEN41HPulmA37qSyHZ0ngHF09mli65Ha3nQ_5LTGFKGZYQEqmbu-qmY5HcmYsy-sgtAngBAOBj1Ls7wVc_1mLAjMQLllE2IxTCUTQJMMcKWi8dN9qg87U2qBlA0r5rzU0MGWFXQa2KkuU2IltIJnOY0BGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏆
بالا رفتن جام قهرمانی توسط اسپانیا
💢
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/136281" target="_blank">📅 02:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136280">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">⚽
فیروز کریمی: مسی الکی داره گریه می‌کنه چون دید رونالدو گریه کرد وایرال شد
👎
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/136280" target="_blank">📅 02:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136279">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTB6pw4EWUqnU4GEu9i2us8VLkIzMUYlnUd2mmihh8ZZqKMmOFQb7l_1xTP110SgsmjtvCa0O4P0WZ_ZBJxE2kb652GJ6ePwWD7YsBxXVZK2Cby-4j1ozDv8D8MurPfz-7uuGFmsI92i2F1uwkdsFfpvEdcxc1vvvAqpeK9PCsWdDRZxJEUZxTEpZ93kvvgWhvUxEhyfS_5EjhlQDp9_E5mR74P51wwh1Mw18zdIjkSx0BVSBkBp8EePJ6vDPKF-g3oMD70rImwknYLFqjQybajCiP3FYmw7sz7t3u_Fg6p5xqMSgyGCCp2Av0N3yZfEhzF6fS_QpdB6dSNzmYw_uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
⚽️
سرخیو راموس با کاپ قهرمانی جهان اومد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/136279" target="_blank">📅 02:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136278">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ueypOWUnsGEgLXG3OZXh8xUlPt5sxWWrpyRZ3l4QvNDShBp4aEUneu3Uq4HGdRMNoj02BMx8nuKpU5X12qcY8ZIqqwmIQGKt6GWXzmTxd-zu9onR6IMshjyT11crSY_8KckGUK7mZKpDEciOkqiIGpr0V9-SOGSWwSk998Bv1M0Iziv1eF5vw2ubDCHUYl9orYDQoIxhxpSWeblH2GVlgDJKh2MESRMqhWdM5M_sW6b10Drpq7TMtYR6n7sLcjTFwmo7OhZ9f10m0OwPpGypQN03eXBgBN4NRlSCPlwl00JS_o4MOG988-N9DG6Zvk50waxglrzVx8XKn06Xgo1oiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
💀
گریه‌های مسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/136278" target="_blank">📅 02:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136277">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/136277" target="_blank">📅 02:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136276">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/136276" target="_blank">📅 01:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136275">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/136275" target="_blank">📅 01:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136274">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4lLlkjgWFA3eVRRlyUSnpLyj5ms4lOC0OfZNmVkQNxl9MUs0zjx03RQmvoeFZjN0S-wenbAOICiTlYDNLMFLXsYqdiEsIAgGfu-jNhMlspqMVfrt-8_v4xIbvzvHqi1HzIqm--plI1GgDPu6buF7pJiiC3cPrfqO5EsJM-jYBUfFGkzNEfwfJV8ccdDRmWEeaOvR6wPULh9kObmYGr-8ujG-5Dq0IcWyGZrqIGjeQEXpv_8I685jSXq9nd6w6vdTW_x1Iq7XH_T-gcJ-nUrIxLBJ8paZCEZPNfamjJ-qLVfPlVi7dG_a63U8IpE4Rz-iD7H2QOB3NQ1XD8NkiNDUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
عکسوووو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/136274" target="_blank">📅 01:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136273">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJ_M5zUZILfVCSZHsaVbmi6GlKh82I1YDnvke4XKswzft5n-eBpKvELwy0lJ6_m3rAptQa4wosjB7QihTzEjjlIZJeKhYpfYHf8_JwAJRKR_wrkqWMw0lYSdeVT3elUPO1-GponQiunML77E5GNGaKory4g4Kv59uBeL6MmxsScfIKOQHBKwG2pGJbXYOX-w4bnZMlNPYun7N-nfpOiIf2xLtR4cP_GBvnfpe8jkYnMiQxZ-5wjsNE7qTg84QGsXZdYGZtCfj2_AFT-8ql4PVW6qGDL1OXIX76JQ4mikeBHRaodS2M6cnergm97do4jh9QKhAAfGuMTS5WsOYeKOSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
‼️
کنایه سنگین تونی‌کروس ستاره سابق رئال به آرژانتیی‌ها:فوتبال برنده شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/136273" target="_blank">📅 01:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136272">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHnGi1uDBWHPLrR1hDG3SNxlDzi8JKvANqM9upSaPPJXtdKcZ952YIE-zFgHO6bmOelERFxuhc7UXk2eajKU0wboLwKio2KS6R9UVk7t6JF8Y0TJkTU7fXCEGdz7GwkoFFkqnspSE4FLOG_dO1WsGPTRxmRaueHIxcWKtkqGZWTRSTs4vr1AgOWoVFgSZagbWQbVpIv5N9_QWvIIKH_IY1q6Vnwn2y1D9CXmattaWSDB28Kj1Lig6JcXwzSXpzYbE77mqmYQ-qdBEpClOXYTVeF68DlHJftT-rCvdN3eQ9A19rA0xnH4M4M9bnx4ovwBYvMo8GMGnSVKyMaRUKwlSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
اسپانیا با شایستگی تمام قهرمان جام جهانی 2026 شد‌
🇪🇸
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/136272" target="_blank">📅 01:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136271">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWIQqpgdtgazhJZzloLFzQMoyuq_WLe29lVC70Scqc4kVUjoARTWwJZ_LiExKDK4W2nkk1lLbRCdrdlzVLI9xFA3YRFqUtw1PJFRhusyrg3gGMdrFYhkTtQ07ZMae-Jdb8MFKhhTaC5lprAJ8SyAqfD4MjmQw1P7sCQ2f0sJyHBc3JCXbmNN6dKercRjQtqQpcDdhPpo9PwaRvrr5EGJp25tzMplUZzQNQRvtrYC86QLY1terPGoOSJCa3cSn-zfX8BNWzfwIBcyfby39X3C7FC6kg61tKhbPLcRiFMo2nQ12c-NLcCPeHNuxQYqdv0whE0Pb-LQsT-5XN6w0sVKbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💋
پایان کار مسی با آرژانتین…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/136271" target="_blank">📅 01:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136270">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✅
این بازی فینال که چرت آور و خواب آور و کسل کننده بود با نتیجه مساوی تو نود دقیقه تموم شد و رفت برای وقت اضافه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/136270" target="_blank">📅 01:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136269">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
بازیکنی که کلا محو بوده و خواب بوده تو زمین فقط مسی بوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/136269" target="_blank">📅 00:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136268">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/136268" target="_blank">📅 00:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136267">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">⚽️
اسپورتی تی‌وی: کاپ جام جهانی 6.175 کیلوگرم وزن داره و ارزش مواد به کار رفته توش حدود $713,000 یعنی 140 میلیارد تومن برآورد شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/136267" target="_blank">📅 00:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136266">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❤️
🎥
ویدیویی از تمرین عصر روز گذشته تیم
🔴
از مرور نکات فنی تا اجرای برنامه‌های تمرینی؛ یک جلسه دیگر از آماده‌سازی سرخپوشان زیر نظر کادر فنی.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/136266" target="_blank">📅 00:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136265">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🏆
اجرای کامل مراسم بین دو نیمه فینال جام جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/136265" target="_blank">📅 00:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136264">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
❌
نیمه دوم هم چنگی به دل نمیزنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/136264" target="_blank">📅 00:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136263">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❗️
نیمه اول بازی .بی روح و خواب آور و کسل فینال با نتیجه صفر صفر تمام شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/136263" target="_blank">📅 23:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136262">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99bc7fc060.mp4?token=oQcGDnwGXhsR-ESb-ys4zcoCrqqBA74MRLXXDUjcKmLzibRjORx7cvTCSYsKLEr0OOHTu5SEQaJoQ0Y1NuNw6pUjaQyAdmuVWwsxApBHHPc1yCrMpXd8VxS__3axh0OUDQLBVYcuDrliGPYo3zJrBKEh6zEhz9D2SGvvsJ_mCmTiUt-GHMdn2-TIHsvfwSN6ZKSVhjc2HnEeek4RasMYyHn1BPy3Z6ztgqfM_71qMPHwzL-msF2wPRKe5hqogDEFJUco3MEshpXWNxah1Ua2vG6BRwUJ0-Cm8rSqdmKiKcZqh7rLl0a2mzH75lEJDBDBfryQfFJUGxXoCqwf5JHfkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99bc7fc060.mp4?token=oQcGDnwGXhsR-ESb-ys4zcoCrqqBA74MRLXXDUjcKmLzibRjORx7cvTCSYsKLEr0OOHTu5SEQaJoQ0Y1NuNw6pUjaQyAdmuVWwsxApBHHPc1yCrMpXd8VxS__3axh0OUDQLBVYcuDrliGPYo3zJrBKEh6zEhz9D2SGvvsJ_mCmTiUt-GHMdn2-TIHsvfwSN6ZKSVhjc2HnEeek4RasMYyHn1BPy3Z6ztgqfM_71qMPHwzL-msF2wPRKe5hqogDEFJUco3MEshpXWNxah1Ua2vG6BRwUJ0-Cm8rSqdmKiKcZqh7rLl0a2mzH75lEJDBDBfryQfFJUGxXoCqwf5JHfkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اجرای بیژن مرتضوی در کنار ارکستر فیلارمونیک بین نیمه بازی فینال جام جهانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/136262" target="_blank">📅 23:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136261">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✅
با یک چشم بهم زدن جام جهانی 2026 هم داره به اتمام میرسه ...بریم برای بازی فینال ..آرژانتین و اسپانیا ....
🔴
پیش بینی شما چیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/136261" target="_blank">📅 23:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136260">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6ASnuUvmrQiYaTRBaEMCYpB_G2pLJZUJaP9u75qd36PMjLXBjC36aAVYMHEw-3U9l5u2fnUY8NxOG6r7oEKI_3SnkOri6v9PmgtXex9I3y5pUAxXaZl2O5hVYS105tcadCqDxiXaUayi2t3YTGw1wqF3jnXgILVuKp3h4ZU73oC950cUK5roSqQKqkf5Zz_O4_X1ZLmuCF7atdrkEaBSIhYrEccD0C43VALRUTb4k_frqj1aW41y5i5pyrU5wFFWkld8WgDzCP_TqiNgKDtK6j-Yv7GPNN77Yn0gvte6qg29sq1z15BPD94zukHRTY1AVDGi0GrGvCFredvuA6JOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یعقوب کافو هم به تمرینات برگشت
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/136260" target="_blank">📅 23:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136259">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
ترامپ از پشت شیشه ضدگلوله بازی امشب را تماشا می‌کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/136259" target="_blank">📅 23:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136258">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✅
✅
#تکمیلی | رویترز:
🔴
ترامپ دستور حمله قدرتمند به ایران را صادر کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/136258" target="_blank">📅 23:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136257">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✅
خیابانی: چرا در ایران کسی معذرت‌خواهی نمی‌کند؟
🔴
واکنش تند خداداد به صحبت‌های امروز امیر قلعه‌نویی
: واقعا خیلی از حرف‌هایش را نفهمیدم. ما لودگی می‌کنیم؟ چرا پس شما حذف شدید!؟ ناپلئون و هانیبال هم یک پلن داشتند نه ۷ پلن. آقای قلعه‌نویی چرا نباید کسی انتقاد کند؟  من انتقاد می‌کنم و نمی‌تونی تریبون را از من بگیری. مگر بزرگتر از علی دایی داریم که انتقاد نکند؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/136257" target="_blank">📅 23:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136256">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eHWCP6OH8nPoKmEr4_CkgOEJtoT-JhgUIHCqXDMr9Yu53Sjbdq5P6yJ7KePaR5xWBcaGvVL1uhU5j22xr4BeryXiWBtvWMTioiOQM6FQ-ovGZus2Oka52I9_BiIYxEB9ifEn5OUH0IIukfafCVa50sgk3_bhiC-pjBT1b_Em-lSDh7b9eaeJuvsYgSvwweqLCSBJ53gyIgUxhbp9tH6wa6ZxetVsSJmw7F4R7d3nmwGDysMqWsTTUkN34P_rWUBh8j0HJSDfXEx--TCceksnyv8aXILX70NQ16rqQNxf62xsW4RhM4O_NgwiYVE9p_41OaZSi0UMTtAA4tbizkRGqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اسپورتی تی‌وی: کاپ جام جهانی 6.175 کیلوگرم وزن داره و ارزش مواد به کار رفته توش حدود $713,000 یعنی 140 میلیارد تومن برآورد شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/136256" target="_blank">📅 23:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136255">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔖
تصاویری از احد میرزایی عضو هیأت‌مدیره پرسپولیس منتشر شده که داره توی ساختمون باشگاه یکی رو کتک می‌زنه…اقای احمدی همین فردا دکمه ایشون رو بزنید
❌
پرسپولیس چاله میدون نیست، ایشون ادم زنوزیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/136255" target="_blank">📅 22:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136254">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85518f3eb7.mp4?token=eSQGFtAZNsD9Rol-enpr69-58Dtr0R9y-A8bM8ctUvFWYxshR2pnXgSBFuMl_UXlZSd7kUItnHQqdXAiZigjRIOdRBasZclqcp9LgUEN3uQUSP_mhrLF93JPgZYnrpHvKL_mAEV343mZgM75bbi4Bq8ooilS6N4KYlrpITFTz-hNp1ODAvV3ql9GlnEDfKTeDOi2g8mjWH8GTpM7D7XGw1sK2A-L8paPdi_lidLMi7TQ3rmh01IO92DE4qM-fp4333PtLsi1_AlWYpoRcTmk18LwQqhXievomhHBC_Ao1H0Wbovp3z6-k9Bh99yjJLznpG-_l95VVV5LnSGMKf3aoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85518f3eb7.mp4?token=eSQGFtAZNsD9Rol-enpr69-58Dtr0R9y-A8bM8ctUvFWYxshR2pnXgSBFuMl_UXlZSd7kUItnHQqdXAiZigjRIOdRBasZclqcp9LgUEN3uQUSP_mhrLF93JPgZYnrpHvKL_mAEV343mZgM75bbi4Bq8ooilS6N4KYlrpITFTz-hNp1ODAvV3ql9GlnEDfKTeDOi2g8mjWH8GTpM7D7XGw1sK2A-L8paPdi_lidLMi7TQ3rmh01IO92DE4qM-fp4333PtLsi1_AlWYpoRcTmk18LwQqhXievomhHBC_Ao1H0Wbovp3z6-k9Bh99yjJLznpG-_l95VVV5LnSGMKf3aoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خداداد عزیزی: مردم نون ندارن بخورن آستینتو انداختی زیر ساعتت همه بفهمن ساعت 10 میلیاردی داری.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/136254" target="_blank">📅 22:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136253">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/136253" target="_blank">📅 22:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136252">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">جالب اینه تموم فرم ها رایگانه ، وقتش نرسیده که از فوتبال دیدن پول در بیارید؟
😉
✅
@FuckBet</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/136252" target="_blank">📅 22:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136251">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HLfu7RZu7-OuZ_7k8oPpjmkD4Jl1wOy9p1Qvyfcdx5Cxg8M0zkGiK5R-mBciD0_WdeMMYciehtc3pwHZSeMr9H0MZX9zIZyUAzbiO6-FEIMakhFFpIUeVTR3w5wV2r-LHom9BilBGpw7BMSVDSo640ijt-S_UENL_EoyMj7t7haWPjyFmnCcIWGdqACrZ0VhKP6XcXUi1zCm0qigDBGYoAq36uhP6L9fSqwpTtNxQbM3JNM57Jyg5zR-0-K6JmCblXQxj9TiCd0brboOl1PEOYC4QTrVXuX5y7L0IJSccgcXTtKPj5RTu5SbIWWZjE8llKdMbSUW048wDZlYcxFPkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/136251" target="_blank">📅 22:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136250">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/136250" target="_blank">📅 22:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136249">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
فرهیختگان:
✅
وحید امیری 38 ساله به پرسپولیس پیوست و کاپیتان اول پرسپولیس شد!
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/136249" target="_blank">📅 22:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136248">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSQJRJ07irUYF33Wrr6t5VJdybtnUYoYu45kev0bEK5RFmrauFxqclCv1EIQ1tAlRGoCs_2-FNuveLJxcKACTuZNmXuumA2_xAnR4TcDMngg09gz6vu-HTuzAE-yR2orTy5UV-8gMRWnn2nFfpAYddtbeJnevvsG8rYZQEN79daSuOYvDOIlHjJza8ZY0vL3IRe8FGcjtLQyZIzAFIll7xmMtqDKg-1lh2tHiByZ-Sz5lCA8kOZTLOOLIIJzFST5-2xj-Ug56FDGCTfDMphmgeTqBUESJjP9JY_lwWhwet8l22i9piHpEFTgXOyQh6ms85zVB4SLySZ-T6TWbxXeiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/136248" target="_blank">📅 22:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136247">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjQ2NYQndwEMlpAL8riyGsdMxqom87uM6AnHV9YKxDShp4OU89LFQGIWbld2ofOORKLLxZEwwNj5tv5EJT7PZPZ6fnM6-T9ciUNKvquMnRAanU1yE0Q5B9VdPRxvPDgIXQTizq7CTQSf9wvqvuXykF6hJRvIxA7ZTzGyapPwgRUL8DL7CekakBpRktLJVQN-5FiV-O4hOIeekJ7VQtpFQQPmbalUnXF9_SXx087Q-H8dqfLAfKkHbOXHob0bvEOdluMgNELcRt8troem5jgizWXhJiUMe25UlJhWymPFuGvOBmLavNEFk0GqFibaies-Wc0sS3TI-LUYOPP6mj4w_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترامپ از پشت شیشه ضدگلوله بازی امشب را تماشا می‌کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/136247" target="_blank">📅 22:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136246">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❗️
امین کاظمیان در تمرین امروز پرسپولیس حضور پیدا نکرد و جدایی او طی روزهای آینده رسمی می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/136246" target="_blank">📅 22:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136245">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlWYk_gpkC5lFV68EXQjjXnFkUTb8gBLBWo4ICOOrTvXAQQfkl_DJnIuuYd2EtEmA3ZWk4DAXIYTV90BR7xgouMdV9dkgprfXsvEDCggWvhrJi7RtoLPWRaDXZoj3FeFVT3fo2_Up8QXuLR-10l9mXCqI_qHEiN_VYHdSOjRwcXQfRvLsL5D_uyqlhBPPkCJ5wuIMfQek1spS9zZvCbftFU-gRBstB10qlboVS-4UzH_i_RevwJ0Uyaq-QqkknK5HE-w49vsIutZbGM1GSjXfhjntyPxYQPQGh1vqNMsdAOX48jE-WIc5xXD-gvRqah22e1vWjNwXYLXS76PCuUzZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تصاویری از تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/136245" target="_blank">📅 22:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136244">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5b943d93e.mp4?token=s9vyVbbWo50GVnyG3R8gJUT6uJapP8dfBejW2vhk1FKMxnPL3lgqUh4w5cMJvKcqDinbYQsp6fLaf8BAk9dCVfqreHc9Q7KVT5tV_TvKDKvVDa7SsOFmjL7ASrWt5O46YZFCsUA1zkQcX-c8daVlPc5YOB_AuUcTBxFvgIDm05LUqbK7kZFWaHewHeNYf0ogJgQ4d9ejns5-VQKaqGysENJKaiwz5e4zS4h2V6WfCU1zcSAtYSrnVMNyBiVx6oeeXUs_c6zoE7WwCBXW7elUqGQUQXMiy11uEQGHK9fNZvl6b8mA7-B2Qn1iq-4AbYBAg3XERCdqcjpgmdmgVtVl_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5b943d93e.mp4?token=s9vyVbbWo50GVnyG3R8gJUT6uJapP8dfBejW2vhk1FKMxnPL3lgqUh4w5cMJvKcqDinbYQsp6fLaf8BAk9dCVfqreHc9Q7KVT5tV_TvKDKvVDa7SsOFmjL7ASrWt5O46YZFCsUA1zkQcX-c8daVlPc5YOB_AuUcTBxFvgIDm05LUqbK7kZFWaHewHeNYf0ogJgQ4d9ejns5-VQKaqGysENJKaiwz5e4zS4h2V6WfCU1zcSAtYSrnVMNyBiVx6oeeXUs_c6zoE7WwCBXW7elUqGQUQXMiy11uEQGHK9fNZvl6b8mA7-B2Qn1iq-4AbYBAg3XERCdqcjpgmdmgVtVl_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ برای تماشای فینال به ورزشگاه مت‌لایف نیوجرسی رسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/136244" target="_blank">📅 22:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136243">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
⚽️
🔥
مراسم اختتامیه جام‌جهانی آغاز شد  پ.ن فقط 45 دقیقه تا شروع بازی نهایی جام جهانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/136243" target="_blank">📅 21:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136242">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVdA4o4rvyfd741HdW6qpRUm97vG03C-T0iEbLCgJzn_bH8yHHoHHokaDG2YGiYMzWKTOhoBPv-9P8_jz8LQ96vvT2k8X4RGTnrg9Z5onmrRS67HFAF-RNPMgSIsm3Po74srwrSqr2J280XYzEcj4IbVlKHRP2YfOFwwo3cX_siUjqmoiRf7BcVRGcib47Qjr38bfnpAXiWFwBjPhe18hHWO7XJx_Nq67j4KneXSaMlkSTJiGH1XGyh8bnsof2Sl6ATASWu_xGzdlZE7Koey3AO1SJXSNpeUoZx62x_MIY9dXkCFyXq4Sn4B61shCPjtpYpyJr7ZfJCPCtybs-qvNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
🔥
مراسم اختتامیه جام‌جهانی آغاز شد
پ.ن فقط 45 دقیقه تا شروع بازی نهایی جام جهانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/136242" target="_blank">📅 21:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136241">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a92f2cfaf9.mp4?token=WGFORucrVD04pLZSqgI4-2a4iqijeEW8BqEFNq0Q782LHTAv2qDhlUKDyBtaKygthHuGwgKHT5eM-mDLirgDNVoWly3gw3fVkcT_-DrEDfc6WmtawqEcEiERh0TNzHjKTeRwhW3Ma50AH5FvBnJnRLXeHtN5Wrj2fJmAX-FE4if-pKKaFM0wKdYT29UNrpHW3473nTYd56V3Hzlcsft7mj1PJCbO8C7nSOOHcbyFkYqxybdJry27NLABOgrRzVmAXKbDzYQdsqV7nFWGW_e0cDO7i1cBAe1NXG1usuDxJAUW0he-D3NtJrGkFtyxF5DWdw19DfxMceQlqZ_DXE1QvnEbM1VcQMSim1XjGjyGPzjUA6_80JO-HhwY-GfPX9Rn88LsQun6EXKQUUfXxgfwIy_womwjXUOneGBOUbx0Jpbt2SJxuor31i1mXWvTD2tuq5XS0CSofIMvnbsQRawvrJZjmsow-BUzOBsutGdJXr7uGpgD8KT5Jj5lc8uSPUrizMWxVRc8cZgTCiNHXC9eaTBDRxrBHO_mV2JsBU_CKbcX6tyqJ7eQIK_sDHresOeiYtDLgyeVaw44mXzYl7SoFZbBJ1r9z8mlCKYzsgXctRo-a3oTgkd_2nk_7dLSfXp3edknEEOWK6Sj8r3KiLJwZFQzX889qMUV4gBQslmi-A0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a92f2cfaf9.mp4?token=WGFORucrVD04pLZSqgI4-2a4iqijeEW8BqEFNq0Q782LHTAv2qDhlUKDyBtaKygthHuGwgKHT5eM-mDLirgDNVoWly3gw3fVkcT_-DrEDfc6WmtawqEcEiERh0TNzHjKTeRwhW3Ma50AH5FvBnJnRLXeHtN5Wrj2fJmAX-FE4if-pKKaFM0wKdYT29UNrpHW3473nTYd56V3Hzlcsft7mj1PJCbO8C7nSOOHcbyFkYqxybdJry27NLABOgrRzVmAXKbDzYQdsqV7nFWGW_e0cDO7i1cBAe1NXG1usuDxJAUW0he-D3NtJrGkFtyxF5DWdw19DfxMceQlqZ_DXE1QvnEbM1VcQMSim1XjGjyGPzjUA6_80JO-HhwY-GfPX9Rn88LsQun6EXKQUUfXxgfwIy_womwjXUOneGBOUbx0Jpbt2SJxuor31i1mXWvTD2tuq5XS0CSofIMvnbsQRawvrJZjmsow-BUzOBsutGdJXr7uGpgD8KT5Jj5lc8uSPUrizMWxVRc8cZgTCiNHXC9eaTBDRxrBHO_mV2JsBU_CKbcX6tyqJ7eQIK_sDHresOeiYtDLgyeVaw44mXzYl7SoFZbBJ1r9z8mlCKYzsgXctRo-a3oTgkd_2nk_7dLSfXp3edknEEOWK6Sj8r3KiLJwZFQzX889qMUV4gBQslmi-A0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ادامه حملات عادل فردوسی‌پور به قلعه‌نویی: هرکه از "غار" حرف بزند، قابل توجیه است؛ به جز آن کسی که کل جنگ را در دبی و ویلای آلانیا گذرانده باشد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/136241" target="_blank">📅 21:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136240">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
پست خداحافظی رضا شکاری با چاشنی ناراحتی: خداحافظی همیشه تلخ است، خداحافظی از گوهر کمیابی مثل پرسپولیس تلخ‌تر...
📍
موفق باشی
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/136240" target="_blank">📅 21:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136239">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❗️
قدوسی: ابوالفضل رزاق‌پور گزینه اول جانشینی میلاد محمدی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/136239" target="_blank">📅 21:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136238">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✅
✅
عادل فردوسی پور :
🔴
آقای قلعه نویی من و تیمم چه جنگ دوازده روزه چه در این جنگ تماما داخل تهران بودیم و تکون نخوردیم ولی شمایی که یا تمام جنگ یا امارات بودی یا توی ویلای شخصیت داخل ترکیه حرف از غار بیرون اومدن نزن. من تماما کنار مردمم بودم ولی شما همش توی…</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/136238" target="_blank">📅 21:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136237">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❗️
واکنش قلعه نویی به تصویر ساعتش در جام جهانی که باعث حاشیه شد :
🔴
اگر یک سرمربی ساعت می بندد و لباس خوب می پوشد که اشکالی ندارد/ اگر من زنجیر طلا می انداختم و یقه پیراهنم را باز می گذاشتم آدم خوبی بودم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/136237" target="_blank">📅 21:18 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
