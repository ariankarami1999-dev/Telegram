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
<img src="https://cdn4.telesco.pe/file/nt0QD6r4PMY3f9C8KgJSoDVGyCNedM2O3oaS8GUg_FCunRK_2YTmprsmGLK-zY_Tpb4H9Z-KsQPaVua3X7aob48tq1AwA_YdlSPVHz1Dt11NNmJG4V2TwQMSGEvaM0cM_WKedHFwfh5_8gS6IHj6sJjxK5Sf0U1ws20mp2Uk-zjag_jF0cITtqLzFXhTyC2ciUjmKwQDf7Cs4FH9iYyGWgQkPZv1XkLYxN4J7OciVehMzDz1RnAi-zooXMLnlMz7aQfIskXozYiA6Tr_dysKM2DZOanfi0F_12wKH1Wy5hyOgAex_-PuHAKzdSOaC1_mjl_7YnhnQFsFz0RCAGEudA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-30 04:10:52</div>
<hr>

<div class="tg-post" id="msg-140341">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esRHlZMCdm8L_YB7RrcJWRURty8_xF7f4s7uG937Ejqc2nGjH3i-DI73iCgOFCg9TctxItP3orezFXmSlSVZY7XebAW_7zoMb-8RRIGZK0kI7TH7-UClspMxaxjGU4GxJwbndSmfPPgsafixhBDe1y0GlCFpViz1xeCLM3eR-hMyC7fjuH-T8zrBKFhkpZAK8mGMaIdjR4HhZiJAawRF_pOEu14pWSgarfTJJqyCSp0pzFpk3fkWXSSZAOmAMrjH2j9DuspKJadslN_bAxoMgrUzSJEmT7_6sQntcr7GIy_T60NhcJbUNF8DgnKi4K5ZgZIwKFQtdaM6M2lLUb1jWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
ربات وینکوبت در دسترس تمامی کاربران
🟢
بدون اینکه از تلگرام خارج بشید میتونید مستقیم وارد سایت و بخش بازی‌ها و کازینو بشید، پیش‌بینی ثبت کنید و براحتی واریز و برداشت انجام بدید.
📌
حالت Mini App داخل تلگرامه و خیلی سبک‌تر و سریع‌تر براتون باز میشه:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 585 · <a href="https://t.me/SorkhTimes/140341" target="_blank">📅 02:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140340">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✔️
✔️
تاج: بسته شدن مرز عراق مشکل جدی نیست و با AFC مکاتبه کردیم/ عده‌ای با کارشکنی و انجام اقداماتی به دنبال عدم خروج تیم‌های ایرانی از کشور هستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/SorkhTimes/140340" target="_blank">📅 00:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140339">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
✅
✅
سرگیف، اورونوف، آشورماتوف و ماشاریپوف از لیست ازبکستان خط خوردن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/SorkhTimes/140339" target="_blank">📅 00:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140338">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9814f0d7ba.mp4?token=gwo0jdT_xkIBHua4aszVOXu9yvya652x8rx2yy_yv2NGdOSbtCmlt5p4oKMoYly0B9gdBHIzsbgHBUnNVLlrlV_yJZg95f6yN2BE2smsLSA7id5XtHZD9VygaI0qE1sHwmOwVeoU2QbAZTZzoNli4NDHFH6VNo4TTaGgMh6EU0Kl_jWa-5VmRgwYuvn3AMT6FymJ8zkZyOCBkxizfu9BZxXm4IKkw2RTuB-bfShmfxdtwm64sVV2mez_vnwt_o7KJWteYb4IJACyyOrQlucybp_KhUYcTzzN7jloNmetG7SQfdvM4BFT4rVcZYyhcXBt_-7uhb-Rn8jeYLcgDjZA6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9814f0d7ba.mp4?token=gwo0jdT_xkIBHua4aszVOXu9yvya652x8rx2yy_yv2NGdOSbtCmlt5p4oKMoYly0B9gdBHIzsbgHBUnNVLlrlV_yJZg95f6yN2BE2smsLSA7id5XtHZD9VygaI0qE1sHwmOwVeoU2QbAZTZzoNli4NDHFH6VNo4TTaGgMh6EU0Kl_jWa-5VmRgwYuvn3AMT6FymJ8zkZyOCBkxizfu9BZxXm4IKkw2RTuB-bfShmfxdtwm64sVV2mez_vnwt_o7KJWteYb4IJACyyOrQlucybp_KhUYcTzzN7jloNmetG7SQfdvM4BFT4rVcZYyhcXBt_-7uhb-Rn8jeYLcgDjZA6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فووووووری و رسمی: وارد فیفادی شدیم و تا 3 هفته خبری از بازی‌های باشگاهی نیست...
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/SorkhTimes/140338" target="_blank">📅 00:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140337">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔄
✔️
✔️
✔️
🔄
سعید دقیقی بعنوان سرمربی جدید نساجی انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/SorkhTimes/140337" target="_blank">📅 00:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140336">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVUzd1rLV5m6XFOxqwv3hNNDs3J5whVjqeLQtx2G1dXGOL9f2MdjvC-vQRpeDRFKJuQVzoKaJMCX3R96IGvXN7cFuphg_CXZbUZDd-ncRAy1K6pjTCU1vMA5btbyHXlGz8xixKHOoYnGVauGyOGed_ZMdHcDDY2zzCE-V9UL4-i0ehNGouA8R_lYpyrpI2yCov4wyfLMW0dLCT6-uZlO7zAPs5waIGJmpPoJ1xW5EK_xqu6YlvWSyzW6aR5aSjirEXoAYwfPUodV6CbwLkvgVqQp_BZi7q4llBFnTwyOgxICuxe59TkRUOiEFPeENnJrI_AzmhwunG4rjWnOLH5aqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
💛
🔥
غوغا کردی امیر قلعه ؛ جوون‌گرایی نوین قلعه‌نویی: ( جمع سن نفرات تو عکس : ۱۰۹ سال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/SorkhTimes/140336" target="_blank">📅 00:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140335">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
فوری؛ ترامپ: تمایل دارم با دکتر پزشکیان در سازمان ملل دیدار کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/SorkhTimes/140335" target="_blank">📅 00:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140334">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔄
دیدار استقلال و تراکتور در هفته هشتم لیگ‌برتر روز پنجشنبه ۱۶ مهرماه در ورزشگاه تبریز برگزار می‌شود. بزودی برنامه هفته‌های آینده لیگ‌برتر اعلام خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/SorkhTimes/140334" target="_blank">📅 00:11 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140333">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s29SZCgY4XcHmMp7tcoSkpmjhuQgkL0c50ElvLZqhLulk_4POWAX3VQ-DabfsXhwcnJkemU0Z9IFegRi6BhnvpHbiU_DC17oq88bAS03z6X2ORnlEzCboDb-Umwfv2mh0DPAXVy_T19BLXqMArt_M_LhaYY1FEzH6FNwCrWX79oXX99vBc9WM4HuAruUAgADMBQ_LvjhiD9lFcl0q4GEW88kC2aXhY62QApCta9bes5308K5mV6oD7tTizyLobnyv_c4uKs8CIrhy-_3T5DtH7lkSZufGXMg1PTAQI9kqCkw8O5XAntrKTDnnFBvnFD5dk1JJqIE-XNqzzlC_qoyQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛎
پپه لوسادا مربی پیشین پرسپولیس به عنوان مربی بدنساز تیم ملی انتخاب شد.
🚨
خبرگزاری آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SorkhTimes/140333" target="_blank">📅 23:36 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140332">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJdxeteDII1kJv-u87poPWgFgfX1ArYD0JbkS7ssOmjTSYEe0krQsm94xhrgoEChzwaZ6cqlffM6WnxnUGX5-H8As0icnCN_bz9gI78j3LCngYEIbVNXqR4ExYrK_Z6ADVXAUkato-soOoXsNIZlCmkOH-_7Nh6sK-haPI4hAFlxFi5iWFKb1QHjrU_ZH9k47HkXmGNm2zTAOKt9wkD67V_GAEoI7usuOuVhpiqp_8yKpV6qEJlw3AzjmYc9uPtEA_gHXz3nW0B3xdNbOTlt2VvlOjI8ZVaMsqSOCI_uA63BIAgKIq6GRHWHetWAUaLNeGyXVqAGnQKejPaHv9aosQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
مهرداد خانبان به کادرفنی قلعه‌نویی اضافه شد
❌
❌
پس از پایان همکاری آندرانیک تیموریان با تیم ملی فوتبال ایران، کادر فنی این تیم با یک تغییر همراه شد و مهرداد خانبان به جمع دستیاران امیر قلعه‌نویی اضافه شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/140332" target="_blank">📅 23:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140331">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABez6zyR-YupFhK4txhvfTbvzyjDLhVXE_qTggChVPBHVhPM6stkwW0Cs-TTMdpen-_r4GZJWa0d3kqQXMFoAFEYOiGZGLVHhySlNH0CuY8waa0pGxaIZVMirKYhGflfiG_wEGEn0qapzOhUjNbmSDWIMWllGJ2S18q8k8ZC5NfF7ZPLhEBQvVDqNbhdC2Vq-yrb1A3yl8t-7hzUKc6WzY0205Ka7EwCDKfJzbm-Ngd78Lk9Y4SWM3s_kB7l2PwlFLoMyT77aL1bmJIwauJtdlciPIlxuvK5XC06_Y54QyiRklYd4v5F1Y7AUQVHbjzq6o9pQC0MNNLnjHZsEpNT0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووووووووری
🚨
خبرنگاران عربستانی: کریستیانو رونالدو نیم فصل در انتقال آزاد راهی فنرباغچه خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/140331" target="_blank">📅 22:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140330">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nauoFQd55XF7QSCgm6rSHz-6EswmODJofCLWXcZLTTu62VZ0risamVvxYdj0_TGRVt74ub6ao2hyzge9O4jBvzQIIaATWJLCuJ9XDWZnbJr7JbEpEdqHIsaxYRbCmqrzxf7ft-EuYdYNuwnVi-uu2LUDRyKM3Cy7QLc7h6M8yTz9espf3LsmG1Xd5es-s4a5xQuQHiB-OoIPSaw8PD4fD95l44jGHwUwM8LSbT6PxN-xASOdUnruvKNv8GtWNckRbrex4clNHJ_yYnrSxc27XyktMR9l_r9jSGcL2fZ9nHwzGnVEl0s-iT3NZ4Va7jR4hO9QNDO7RIuJ7CDHNGLLFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤍
🇮🇷
سردار آزمون با بخشش 5 درصد اموالش به کمیته امداد خمینی به تیم ملی برگشت:))
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/140330" target="_blank">📅 21:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140329">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
❌
فرهیختگان:
🔄
⌛
بشار و فرهان گزینه‌های روی میز تارتار در زمستان؛ پرسپولیس به‌دنبال پلی‌میکر
😀
درصورت تایید مهدی تارتار مذاکرات با بشار رسن آغاز خواهد شد و فرهان جعفری نیز گزینه‌ی دیگر سرخ‌هاست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس …</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/140329" target="_blank">📅 21:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140328">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
❌
رسانه‌ های عراقی: باشگاه پاختاکور ازبکستان با ارائه پیشنهادی جدید به بشار رسن قصد داره قرارداد این‌بازیکن 29 ساله روتمدیدکنه اما فعلا پاسخ مثبتی به‌این افر نداده. اولویت‌بشار بازگشت به پرسپولیسه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/140328" target="_blank">📅 21:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140326">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8hi8jOK_IvUkunsIeRcy766t5o0Km-kb7u-PM_MDzX_GM4Hhqip256UCHeSXKr1ux8W_FiReQ07BYJefWE6ABOMrzbuqUvnwGvjV3_f2gQIFn8AgAKK2r5pwRU4_WmmCoWjQJAIfcx0bQ04vTS0M6TIxACXQo8jMG_B2tGCNeHWN-P0UgVpaqM0epADGwtPSrZWoLNucebaQbNo5B7rXMhrwKQNcGe1deTqnO13lHxBwsdtrlWXVJcIIBic2bK1yA1-dI6QL8Ptejkdyu0YyEI2n0rKsPtCpQeZO8dKwwARuyZ9riYNK28Bk2U9dWmoUenffYfymsN9d2nQsTPThg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
Marseille -
🔵
PSG
⏰
Tonight 22:15
🏟
CEPAC Vélodrome
🔵
مارسی با شروع ضعیف فصل، در ۴ بازی فقط ۳ امتیاز گرفته و ۳ شکست داشته؛ پاریس هم با ۵ امتیاز هنوز در حد انتظار ظاهر نشده است. در ۵ تقابل اخیر، پاریس ۳ برد، مارسی ۱ برد و یک بازی هم مساوی شده؛ آخرین تقابل هم با برد سنگین ۵-۰ پاریس تمام شد. از نظر تولید موقعیت، پاریس میانگین ۱۸.۷۵ شوت و ۶.۵ شوت در چارچوب در هر بازی داشته؛ مارسی به‌ترتیب ۱۳.۵ و ۵ ثبت کرده است. با این حال، ولودروم و حساسیت «لو کلاسیک» می‌تواند بازی را نزدیک‌تر کند؛ انتظار یک بازی پرفشار با موقعیت‌های جدی دو طرف می‌رود.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد سایت شو و دیدارهای امشب لیگ اروپا رو پیش‌بینی‌ کن:
👇
🟣
Wincobet.com
🟣
Wincobet.com
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/140326" target="_blank">📅 21:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140325">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jd1-Iqw9QV36oSfmDw59MB9EbdV3qzDzNFG2-8Ps8UcC8ZXVB3iaJ6PnMo6unvZPihPzaHye4sZ3spT-YkmLcHXE4m1enq0ZWn08mV1piQ3Pk0qEj_kSyqVG5z-DYjd3WxS1RP8XLr-rTehR9_03Dhn6R3Pxo3ax6nznWakQ7-D85XpgaW4L3Wpmcd5RnlqBKVhOpGyrKsZQ9ystwY2W9CjA6sCADo_hZwsXS4X9nDdYrjtJxoS8SUADNAAetcYVrqCOTT0fBG7nTZNLS_yXfsLDlg138B2RamuEbTESQxXAfYXTeHOFzrMX6UHMHRJHebXTnfQBe3mNg25YdiZlew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏅
پیمان حدادی با حضور در ورزشگاه درفشی‌فر ضمن بررسی شرایط آکادمی، با بازیکنان و کادر فنی تیم‌های امید و جوانان دیدار کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/140325" target="_blank">📅 21:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140324">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✔️
✔️
✔️
✅
تصمیم پرسپولیس درباره اورونوف
✔️
✔️
پرسپولیس فعلاً هیچ برنامه‌ای برای جدایی اورونوف نداره و این بازیکن همچنان در برنامه‌های باشگاه و کادرفنی قرار داره.
✔️
✔️
شایعه انتقالش به تراکتور به‌خاطر نیمکت‌نشینی تأیید نشده و حتی اگر در آینده بحث فروشش مطرح بشه،…</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/140324" target="_blank">📅 20:29 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140323">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
❌
ادعای خبرورزشی :
❌
تراکتور به دنبال جذب قرضی اورونوف از پرسپولیس
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/140323" target="_blank">📅 20:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140322">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
❌
ادعای خبرورزشی :
❌
تراکتور به دنبال جذب قرضی اورونوف از پرسپولیس
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/140322" target="_blank">📅 19:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140321">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEtwTFdxdlxG3xym4XTJmz9jEMTRJGDmt43YM_MuGcRapLuOewLGtBUaMbwFvewhYxNj0ZS6ieb7i6KLOtCZ8BZDHi4-Je7PtOZu_TN21L2udVi1pQq1zP16nmtmxW_nKERHm7aPFKVffF1Q4iDyeN07cznGeTBxjUJFgJBbydWopjJQq3GOuGm4BZDqaJAc0FO8YyqnD4oDIwqMU-sSSe8CWXHrmbphf9X2_jOZC3rEo2e27Dflh7R-fxqLZ_xtRAfw2zuH3hyBxzSElqjvMJEz5ZMR4isC0VdKaTfjWLNZj_D3PEV7ihMPFJ_yVgUEzdlxANWwSNyR64IHVXIjFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
گزارش تصویری از تمرین امروز تیم ملی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/140321" target="_blank">📅 19:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140320">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbqgqlBu-wPP-wZyceEQYr3Hm_IWJH1_r-l0rgkc0Y5P4mmu3SjGx-in_Ptk9SOZwBhLGlyurrSU-ojxx6l9KsTiw5_271mcQkE49y4A04GnYRie5lObGxIqqupHE4qvB2MmJNWdfTrmA0I4ypOArXaUuEBV-2s7Ei-yYwBy3Z-d8mRyY2toCpOJtzh81Z6maEVF_vwSoEepgZSUlEvL7oRQYBq6uSKn9H5ow2wSEWDTxCioQg0ew2nXVCCF9yKulMbzIaRyGwpj0Mm1pj5bMh42Uqm8TW0H3hxjaYDBv9O7rW_yNq0GZjGOIOl-8MRHf1UuZ_PZT6epEZDWO9hGyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری؛ ترامپ: تمایل دارم با دکتر پزشکیان در سازمان ملل دیدار کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/140320" target="_blank">📅 18:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140319">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✖️
✖️
✖️
🇺🇸
ترامپ به فاکس‌نیوز:
❌
من می‌خوام با مقامات ایرانی
🇮🇷
مذاکره کنم، ولی چالشی که الان باهاش روبه‌رو هستم اینه که اونا مثل موش تو سوراخ‌هاشون قایم شدن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/140319" target="_blank">📅 18:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140318">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✔️
✔️
فوری ترامپ: آماده حمله دیگری به ایران هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/140318" target="_blank">📅 18:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140317">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
فووووووری ...شنیده ها
🔴
قرارداد استون اورونوف با پرسپولیس با دستمزدی ۲.۲ میلیون دلاری تمدید خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/140317" target="_blank">📅 18:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140316">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
❌
رسانه های مملکت گفتن آمریکا مجوز لازم رو از چند کشور منطقه برای شروع دوباره جنگ علیه ایران رو دریافت کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/140316" target="_blank">📅 17:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140315">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
اعزام علیرضا بیرانوند به خدمت برای یک مهر به دلیل بررسی پرونده کمیسیون پزشکی او، به تعویق افتاده و او میانه مهر به کمیسیون پزشکی می‌رود و در صورت رد شدن درخواست پزشکی، از ماه آبان راهی فجر سپاسی می‌شود.
❌
حالا خوبه این گفته بود سر تعظیم فرود میارم برای…</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/140315" target="_blank">📅 15:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140314">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
❌
❌
صداوسیما: حمله به ایران قطعی است و در وضعیت آماده‌باش هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140314" target="_blank">📅 15:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140313">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
❌
❌
⭕️
⭕️
فوری/کانال 13 اسرائیل گفته آمریکا و اسرائیل تو تدارک حمله سنگین به ایرانن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/140313" target="_blank">📅 15:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140312">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56fa29145b.mp4?token=DTF1gMgSVfRPpIrg6ZIwFKO0NxkJLyjxQY0Xx_Tv5jj-1xdLiKxeaxPbV8Y7yTeHtiVu4w2pDT6s8dZ_wPM86w70xTUnLyJoj6Iu4Bx2FqeUY_7lHAMRqFOSvrnpdbom3FclAV052HUy1skn0DcAzh0URiN7gl9GPxgxQXRyZ1l9CyMF1FlMp7hsw6XVXQlSkydtmvY6OY5mi90jwwFF5cFn3UxVj6MqQXoNzgVSEdw_24ytul8UNL4SBjDVOc1pbGRrSqe9fgMTU2HMbuAHupHisqmS1iJjOdr9Soko03WC9kGflJV7LLeeZQQR2I3jmGvhDavfd7SW2f7yMQUk8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56fa29145b.mp4?token=DTF1gMgSVfRPpIrg6ZIwFKO0NxkJLyjxQY0Xx_Tv5jj-1xdLiKxeaxPbV8Y7yTeHtiVu4w2pDT6s8dZ_wPM86w70xTUnLyJoj6Iu4Bx2FqeUY_7lHAMRqFOSvrnpdbom3FclAV052HUy1skn0DcAzh0URiN7gl9GPxgxQXRyZ1l9CyMF1FlMp7hsw6XVXQlSkydtmvY6OY5mi90jwwFF5cFn3UxVj6MqQXoNzgVSEdw_24ytul8UNL4SBjDVOc1pbGRrSqe9fgMTU2HMbuAHupHisqmS1iJjOdr9Soko03WC9kGflJV7LLeeZQQR2I3jmGvhDavfd7SW2f7yMQUk8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🤩
| فوری از برنا:
⚪️
❌
ظاهراً عباس کهریزی از ناحیه رباط صلیبی مصدوم شده
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/140312" target="_blank">📅 15:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140311">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✔️
✔️
ورزش سه:
🔄
🔄
علیپور و خدابنده لو به خاطر عملکرد خوبی که تو 6 هفته ابتدایی داشتن، در لیست قلعه نویی برای جام ملت های آسیا قرار دارن  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/140311" target="_blank">📅 14:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140310">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drmUpS-ARIcc0V4h3swJH9UiQNA6rTM3iYGCH68N68KVbhccgHClni6CspAe3sJ_JOiG0YlS41xjgj6669cicce5qbSjbVCa1UzuU6kdNImyCBUjwOM9P9y_I082lE_57NYpGY7YUtCH8GwgSBxq-r77ptmBxNwt7HKXyM688RWpOrf6BEtUoS6qeiIh-qIp9xyUjfIQDiwqg4itmMq2rwSWP05jH1KCSuqIoBU6sDIBDQO-y-heMtGyONmdtrqMhp1j7bFCADlKW-bWHArprcvFP2eXSixkXFQz_nrrw9BNcv8ULMYwkY4JRBSOnwRxO4FVIlEQRWuxIEZXc3hfsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مادرید در انتظار یک شب داغ؛ اتلتیکو یا رئال، کدام‌یک حرف آخر را می‌زند؟
[
اتلتیکومادرید
🔴
🆚
⚪️
رئال‌مادرید
]
⚽️
اتلتیکو با بازی فیزیکی و فشار در میانه میدان می‌تونه ریتم رئال رو مختل کنه. رئال اما در انتقال سریع و خلق موقعیت از کناره‌ها، تهدید جدی‌تری برای خط دفاعیه. دربی مادرید معمولاً پرتنشه و استفاده از کوچک‌ترین موقعیت‌ها می‌تونه سرنوشت بازی رو تغییر بده.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140310" target="_blank">📅 14:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140309">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✔️
اوستون اورونوف و ایگور سرگیف از پرسپولیس به اردوی تیم ملی فوتبال ازبکستان دعوت شدند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140309" target="_blank">📅 14:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140308">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✔️
✔️
✔️
#تکمیلی؛ فرهاد مجیدی سرمربی سابق استقلال ضمن تشکر از حدادیان‌مالک‌نساجی آفر این باشگاه رو کرده و اعلام کرده در ایران تنها حاضر است سرمربی استقلال و تیم ملی ایران شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140308" target="_blank">📅 14:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140307">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">😰
مدیران نساجی دارن با فرهاد مجیدی مذاکره میکنن تا این سرمربی جانشین مجتبی حسینی بشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/140307" target="_blank">📅 14:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140306">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSW7mXYWYiS0sObk4xIUL59vex95wa2mIiiCTXTxgzr80tCrLCcd8YJVwnyisaH2iBvdXI0XnJT9ofugVoJvkqWhEYoDkOIvjXITvUl-P4xNLOpPYSIHRE3LKK1L9b7HdGx4_dvlCJjl71NErcHMqhaKCGvqd7DBGaU8HVGJsePkeV1kQm_ZfxFwlvch4ashK8xGBLvFqZ7hPAPQfMY5cZlcraa2HeQIkepMhW_Zsh6JEBasgVJqPlmS_UX4U70X3FcJyD5Q7d-Q_ckn-NuDtp6YwQWGgWD8madqYtXkSXW6HNFBqIkT1IS-J7OCUQVJxbTFbbAYOehPqEgaINsuCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علیرضا جهانبخش قصد دارد در پرسپولیس به فوتبالش پایان بدهد
✍️
ورزش‌سه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/140306" target="_blank">📅 11:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140305">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJp7GRGEuo9xavHTNbgCKDkR0hgqk9XX3e1lGNCq5bo5XfUMNlAGBIJMsUxBsdBuRsO__UzvucDGurYHzuPZhMmkc0M3EFWuqFxaaxhCWnF4Kf-VZJP9gfJyr53vKnhdSvk5NICLFRttWV1okg1KXv5GtO8b7APR7os75ohiIHjiJK628a1BMym3j0zDiB9WquynFSevnvAWRcSZ4fPlW4viGKIBHfHAmTZfel79m8i3ikd84x2LZKTc9reZX_R3ls_4TuZKPABNVSWzVaoMYleK5KJAXpYnD9cLZTL_3IvuqENjsTz8r8AVGHoLEbnV_b4uf35NYZsgmfz2LW0p2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تیم‌ملی امید فوتبال ایران در دومین بازی از مرحله گروهی بازی‌های آسیایی برابر چین با تساوی بدون گل متوقف شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/140305" target="_blank">📅 11:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140304">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZCCa6YmageUjgQ11s9uKPYfRPCKq52xIJph_INt9SIJ3p9F3nFoO2z6X5ZKzQgeSlja1FJzB6kXLE_KMfdqpGF9zYsmFYbFsg0pF-XJ_i1Kyve6dhbTXXanUYB2_pTaeXU6ppVtllccK6-xGlUUUUIG0D5XsB0jNcxmQiiTSEspWdvwNx8cURbafEWxwBM_An06FDOwP4riDAOJ5A7LyoXKZE3sUoub9Sy6ZBeXc1zwSOU_DvfYis4QmnFsmhH3EUTUfoWWbZ2DSpNtoCxt-ZghJcdbGt2Wp15CE1ALsE7qu5qR2lHKn9hLXaUgXUjXHIj4iQ8XnCBb2ZDaUbyNhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
✅
امیرحسین محمودی بعد از اتمام فیفادی برای تمدید قراردادش به باشگاه میره
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140304" target="_blank">📅 11:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140303">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">⚪️
مهدی مهدوی کیا: مجاهد خذیراوی به حقش در این فوتبال نرسید/ حیف شد و واقعا سوخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/140303" target="_blank">📅 09:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140302">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
اعزام علیرضا بیرانوند به خدمت برای یک مهر به دلیل بررسی پرونده کمیسیون پزشکی او، به تعویق افتاده و او میانه مهر به کمیسیون پزشکی می‌رود و در صورت رد شدن درخواست پزشکی، از ماه آبان راهی فجر سپاسی می‌شود.
❌
حالا خوبه این گفته بود سر تعظیم فرود میارم برای…</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/140302" target="_blank">📅 09:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140301">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
❌
ترکیب تیم امید ایران مقابل چین
✅
✅
محمد خلیفه، دانیال ایری، امین حزباوی، فرزین معامله‌گری، ابوالفضل کوهی، امیرمحمد رزاقی‌نیا، اسماعیل قلی‌زاده، عباس کهریزی، مبین دهقان، امیرحسین حسین‌زاده و پوریا شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/140301" target="_blank">📅 09:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140300">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
تیم ملی امیدمون‌ امروز صبح ساعت 8:30 به مصاف چین خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/140300" target="_blank">📅 07:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140299">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">■
دنبال راه‌حلی برای ورود به سایت بدون دردسر میگردی؟!
🔵
اسپورت‌نود کار رو از طریق ربات مینی‌اپ ساده و راحت کرده، به‌راحتی میتونید پیش‌بینی مسابقات ورزشی و بازی‌های کازینو رو انجام بدید!
🔗
فرآیند ورود به سایت به شکلی طراحی شده که کاربران بدون درگیر شدن با لینک‌های متعدد یا مسیرهای غیرضروری، مستقیماً وارد محیط اصلی سایت شوند.
📌
این دسترسی از طریق ربات رسمی اسپورت‌نود انجام می‌شود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
به جای روش‌های قدیمی ورود، این ساختار یک مسیر واحد و ثابت ارائه می‌دهد که همیشه قابل استفاده است.
📌
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/140299" target="_blank">📅 01:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140298">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZzO1SxiUTzLsiN_uwr6MWle9PfPxAMHAkDgIAxgLhg_3_Qc0ka40rJWIL_82GwLcSz1IcCYL1yAkpWvZpQ9-AdZIEy1PISkDctD-kNmK6pUVNI2iMAwu068YaTJVwKWoxp5D-h2UqZwp87SJPFgF_mThANtj6eIReMOOmU4durzFyWCaVl2kj1nBvMBsp5XJ_p0LKpc9Orlf6pjxMJm4nlV79x5_0YtSVdZrOqTsvvXP0-2t4qnLOfKtSi3d5JS7II_xUY7PeayxSjyxqgFy9Xi_3fIrxF4CEU9CAJnsa1GgxQNaq2p15bwSonaqX7WLKe4miZU7lUyyNAwbQ9brw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تیم ملی امیدمون‌ امروز صبح ساعت 8:30 به مصاف چین خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140298" target="_blank">📅 00:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140297">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
❌
باشگاه نساجی مازندران کسری طاهری رو با 703 هزار دلار خریده و با 863 هزار دلار به سپاهان فروخته!
❌
❌
قطعااااا این انتقال پل محسوب میشه و باشگاه سپاهان تا نیم فصل حق استفاده از کسری طاهری رو نداره  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/140297" target="_blank">📅 00:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140296">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
❌
❌
دوگزارشگردیگر نیز با صداوسیما قطع همکاری کردند؛ نیما تاجیک و سعید زلفی دو گزارشگر مطرح، خوش صدا و با سابقه تلویزیون بعد از قطع همکاری باصداوسیما به پلتفرم نماوا اسپورت پیوستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/140296" target="_blank">📅 23:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140295">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✔️
✔️
رسانه هفت ورزشی:
✔️
پیشنهاد نخست لوسیل قطر که خوب هم بوده به محمد عمری ارائه شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/140295" target="_blank">📅 23:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140294">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
❌
❌
فووووووووری
❌
پیمان حدادی با درخواست مالی امیر حسین محمودی برای تمدید قرارداد با پرسپولیس در صورت گنجاندن بند 1.8 میلیون دلاری موافقت کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/140294" target="_blank">📅 23:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140293">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✔️
✔️
تیکدری‌ جای جلالی را گرفت!
🗣
🗣
مصدومیت ابوالفضل جلالی می‌توانست برای تارتار دردسرساز شود، اما مهدی تیکدری‌نژاد با عملکرد خوب در پست دفاع چپ حسابی جایش را پر کرده.
🗣
🗣
تیکدری در ۴ بازی اخیر فیکس بوده و پرسپولیس در ۲ بازی اخیر کلین‌شیت کرده. حالا با این عملکرد،…</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/140293" target="_blank">📅 23:08 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140292">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5ShprMU07RdZps7VtiDsUGnlbrDoat_R2640v8kAz1ZMw8jVEA4LZogdrcAKBTal9aNohXoR_EiES7O8vGcq2g8eSGaa7CD6Qxary_OBwo3Fd0xb7lhcqJJkp0c5bwnqQZOQ47Msb58DGspKw_4QBEURElPdN9I6OQ35o71XtXbWeMhZlDiBeRDxWQhZGWyP1NABeWpu8bOh-H3YH-FB-zI1r41ONjJwvNJ3mzHN-8b5DqeQYsWItMyvjP0ezJ6b5VknTXgkY3KutEqNrMBC2wdsjycuSPWwx8Yse-GOz3zsq93Nc_dr7fndwHdeaAfbs5EgiK_JwJshhTYsS6QHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گزینه جایگزینی یحیی در دهوک مشخص شد
❌
باشگاه دهوک به دنبال توافق با گل‌محمدی برای جدایی است و رسانه عراقی «روداو» این موضوع را تأیید کرده است. مسعود میرال، سرمربی سوئدی، گزینه اصلی دهوک برای جایگزینی یحیی گل‌محمدی معرفی شده است.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/140292" target="_blank">📅 22:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140291">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d7cf776d5.mp4?token=UF-Pusohn3UMl1Jc5UicbL_ZPoo8nrAEZyX5erR9-SPQKSP74uvkhy6JcvBUS9Yy84-fw56rdiR5yL48vf3KEWc1sJNPdZseS46WPltHAnxpZSc7WrFMe42ur9GHx_LaUP_sF62HJ4z7_OTxo5Vo_CpZUawRcpV9kUdxXZzRA5-FNobj7COaZN5mndC0QmUjUskuQNUh7tlHEq0jPSmoFtkRNnC6VOLDRQshD2UJoQOy-Lq3B-Fc27GQnhSVyoITSEhXeHGZpSEyZJvlpjpxCVlO5IJcHwVL8Gau3je2rPmXeyVKUrHoWVk3VBRlgpan-2QEgKe6yDM6eaUAbSBAUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d7cf776d5.mp4?token=UF-Pusohn3UMl1Jc5UicbL_ZPoo8nrAEZyX5erR9-SPQKSP74uvkhy6JcvBUS9Yy84-fw56rdiR5yL48vf3KEWc1sJNPdZseS46WPltHAnxpZSc7WrFMe42ur9GHx_LaUP_sF62HJ4z7_OTxo5Vo_CpZUawRcpV9kUdxXZzRA5-FNobj7COaZN5mndC0QmUjUskuQNUh7tlHEq0jPSmoFtkRNnC6VOLDRQshD2UJoQOy-Lq3B-Fc27GQnhSVyoITSEhXeHGZpSEyZJvlpjpxCVlO5IJcHwVL8Gau3je2rPmXeyVKUrHoWVk3VBRlgpan-2QEgKe6yDM6eaUAbSBAUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
مرتضی پورعلی‌گنجی تو بازی امروز تیمش دقیقه ۹ اینجوری ساق‌پا بازیکن حریف رو قلم کرد و خورد کرد و اخراج شد
❌
بعدش جالبه اعتراض میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/140291" target="_blank">📅 21:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140290">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgtUCyKDBGY3BmSBilKAHCxeUUHUzYNLjT31aBTgy9H430Kwo0lagdfxrn14Bv--SODl9YP4ZTy2RwkAcDUezXnnLDbsvVtJwXUVe_KPdNA-Gj6lhzJmX8keUj42TbwNMbU_75augBsmTOXQ83URQHouKgltrDMl4nQ5PCck5f8fjQBwJh4GnDPdGu14-wVInavA_5Nh59kPCBv6xiQuwHyJjZ1etnoAju_R83BeiQCqFYU6jQNVhtGLRmdCPkLpqRx2Tflrt4FiwE3wRdqlzSaeJU69hBun27WOISlR0VeVKXGiRnWgdgjpvtkScQdKDANIW5B2U5rHh8hVEgJ5jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
با معاینه پزشکی بیرانوند موافقت شده و اعزامش دو ماه عقب افتاد رسما میره تا نیم فصل
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/140290" target="_blank">📅 21:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140289">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
⚽️
⏳
۴ گزینه‌ی جانشینی مجتبی حسینی روی نیمکت نساجی
🔴
در صورت قطعی شدن جدایی مجتبی حسینی از نساجی، سعید دقیقی، سعید الهویی، محمود فکری و جلال امیدیان گزینه‌های جانشینی حسینی خواهند بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140289" target="_blank">📅 21:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140288">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔄
🔄
محمدرضا احمدی از صدا و سیما به طور کامل حذف شد و حافظ کاظم زاده مجری فوتبال برتر شد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/140288" target="_blank">📅 21:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140287">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
❌
بشار رسن پست مربوط به بازگشتش به پرسپولیس را لایک کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/140287" target="_blank">📅 21:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140286">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
❌
❌
❌
آخرین وضعیت سربازی بیرانوند از زبان مدیرعامل فجرسپاسی: معافیت بیرانوند تا پایان آذرماه است و این بازیکن در تراکتور می‌ماند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/140286" target="_blank">📅 20:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140285">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_DCKEFe6yCNZqdaoW18PxWK91xAfXCdXjUqRZ-mQE2Xff5ohHskgRcBk5z4oFoW5gvYOzb7_Ox3S6GS-VaIGduhqo8eMOlcxLQT6cRo9x04sxjAqF_8EiAiWx16QU-Zfxl39rw1cLdlBMlvIXhUwXEtOiQVeiGLBIaJ_0-uUjTlC4EWxCFPrScALdoqjugTvI5ABe7VIwJsW2ullQZFxG_raS7ljLAW8UsuKSR8UYsoYin97nFtAq47kJRGoPsKu7mkCGSaERFXUS_CscQfDJN8iZqb8Uli0oubpc2H59rWD_KAi0j46Zr-3A6lMd4LNzUoTja6gOANd7K5E2RKTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزگاری سیدجلال حسینی با وجود اختلاف قدی بیش از ۱۰ سانتی متری که با کیروش استنلی داشت با پرشی فوق العاده سرزنی کرد و رکورد فوق العاده ای از خود به جا گذاشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/140285" target="_blank">📅 20:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140284">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✅
✅
با معاینه پزشکی بیرانوند موافقت شده و اعزامش دو ماه عقب افتاد رسما میره تا نیم فصل
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/140284" target="_blank">📅 20:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140283">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8YEqK86n6ySx3Oo1Nk407dn7B9KYWkFyzETifAKog61j5PujEIwrzS2J7cPG2J64NZMKRfhl7ZPpYEYPcVuhyMcyBjSu7s4lrvF9EFpNbdPAf7VRdKcqURi8D6jeYiulxh_eKltArxJDDJXahTdugiqW733bZ43dpc-XGq03kcj6CAPl2NWXMj-12VBXDDFnzWSU8sFllAk0kgnJhADfw--9cCXX0qjPy6ARs6O6BXJ0KFt0QRqq-i48y-unwR6gxPbOtosVSwEvdbB5oVgcuG-I8BjLOu6IuZC6UC3FrJhQQF53OptnD1mcyT_C4sGQR-SYztpr3CbD7_JylpYSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نبرد آندلوس با کاتالان‌ها؛ سویا سد راه بارسا!
[
سویا
🔴
🆚
🔵
بارسلونا
]
⚽️
سویا با اتکا به بازی مستقیم و فضای هواداری، می‌تواند کار را برای بارسا سخت کند. بارسا از نظر مالکیت و کیفیت فنی دست بالاتر را دارد، اما مقابل فشار سویا باید کم‌اشتباه باشد. تقابل دو سبک متفاوت؛ جایی که مدیریت فضا و استفاده از موقعیت‌ها می‌تواند تعیین‌کننده شود.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/140283" target="_blank">📅 20:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140282">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-wKtwrLaHgJQ__I6E_xCgWitDS2RSUBUKIfcxAhGqCEjLzDqlLzkxuKa-lmGKb6UwctO5HPFBqe5uQ3v0fiuQavwZyL4QXvYpx08RI3xTXJtc87PpTzAL_LUWR2g5cbcjuM44tgOUSbCAHCtQx3bmNHXrVinfyY3UKyKySmNSvLAuNcNHU0xr89lfs_6xvXKwAeNRg3vQrDVDhoMZJcgHZYIu77Spe6LHMJs3_PzfvxRWCHvESjuoYRsq6enKH6DD1d5EZz99RmXJhlwWzcv7gSwdJ727SynW9RzsEzKGQv9D4WhB4B2jWrSd9DVD6xN4kXX_4fXmBPqR7GTxXXxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
تصاویری از تمرینات امروز تیم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/140282" target="_blank">📅 20:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140281">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGbqoQX1zSQKEzypz8N6eI2t2HyS5c5v8vo1q8POgUMUQM50HlX5GdB9CdjL4ivlAO7lom77fu1xnLxJqLgsBtWa7hWOv1VSxZcfkNszb3NzDImnAsO4U7NThtuErnVc3BlMbQoLJ0NbkWBpMwXsLqNvd8ZIctskwzdNI-UiEfl4jm80Wrz_UdHDSOise17hQBFkJ4A_rxBwk1bOsUSAykhF7JrU8FWrK4QvHSlmbGNwVOnA2EZdasEVvE-KXU1gO43THl4_X05JH8PQ1ZS3-Nsg5tWe53CH9V1COT7uisWYTkpUD5LXabUE2RmWI574UNC-N5fFGBIotkEq9EsH7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
⚽
بازگشت سرخ‌ها به تمرینات
⏺
تمرینات پرسپولیس پس از 5 روز استراحت امروز با حضور 15 بازیکن از سر گرفته شد.
🔻
ملی‌پوشان و بازیکنان خارجی تیم غایب تمرین بودند.همچنین حسین کنعانی؛علی علیپور؛محمد عمری؛حسین ابرقویی و امیرحسین طاهری به دلیل مصدومیت زیر نظر کادر پزشکی تمرین کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/140281" target="_blank">📅 20:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140280">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOvA6apLycblwwaN60QSHeG3BiY2wl56QxUh_VrQjso0CV_rNX4z7urvQ3aVNh5B6lxl42Qewn2HUr-YDa1ckUQcJU_0KubyRE5aUyA8fjzQdqfSp3ebuE-4lqkcaHEF2fvlfmQ7C77pdagVfrI2beQttFpmEtfikgCJexcWTLB7YCCc4lZ17VMWM-WSU9rU1nDbWjYlHLMJtFr4C1E0DSbBf9THtRNKToIKjeKxhXPxJsBAivYuVXGufwdi5ap5yFWdwFlgXtOyhcGdg795QHqx7I-1xzMShbnFpEw0rcsBqh_zauAfK1RbdnSv105hZ9tFQhXONuaA7FLtq93LIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوووووووری شایعات
🔴
🔁
🇮🇷
ایگور سرگیف پایان فصل از پرسپولیس جدا خواهد شد و مهدی طارمی به پرسپولیس باز خواهد گشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/140280" target="_blank">📅 20:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140279">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/227e813e97.mp4?token=cllqgNsDRYhW6cnFU71RkxhyF7tgC9KI1K7FO0xMJhGAtimNESmLEKO8rpN4Y_CGrah1alv865ozuTM5G-zZig3dEUv6oWjS7dzQWZJ62LT52iNn2wSVsfV9FsJkX2HWnXVXUSUTGGbekthowomE3PNNRyeqxKbLs1bdBOXT6yP_YNuFxje9-5QlvXfdJmWrBx6H0hBFNVya5KELdPeRc8RSTO45ncqHWHSvpSP_wqgLDCAdkbZTm08XdO2IVLeSLOnDEdNBtzklYKXDsW5R86yWGPF_Y5cYVdaCZ52VW9R8xu_RZo6SXzpwhx9IJu0fhTPPhrbFwep25gbxkOLuZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/227e813e97.mp4?token=cllqgNsDRYhW6cnFU71RkxhyF7tgC9KI1K7FO0xMJhGAtimNESmLEKO8rpN4Y_CGrah1alv865ozuTM5G-zZig3dEUv6oWjS7dzQWZJ62LT52iNn2wSVsfV9FsJkX2HWnXVXUSUTGGbekthowomE3PNNRyeqxKbLs1bdBOXT6yP_YNuFxje9-5QlvXfdJmWrBx6H0hBFNVya5KELdPeRc8RSTO45ncqHWHSvpSP_wqgLDCAdkbZTm08XdO2IVLeSLOnDEdNBtzklYKXDsW5R86yWGPF_Y5cYVdaCZ52VW9R8xu_RZo6SXzpwhx9IJu0fhTPPhrbFwep25gbxkOLuZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
گلزنی احمدنور در دیدار امشب کلبا مقابل خورفکان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/140279" target="_blank">📅 20:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140278">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjvZnwxreUt4vuUa7Ble03CzYmGRna_umpvyoQljD23Th1q8SjF6eIdS4q1CzCDqRdrMDHh1KNFgDiITc7WI2EAcLy8Oyh9a2qYlxysth-9B5SVrPVb8RzrBf43Q3xLUBRTMSPOvbCHsl0F1aSBHaHLL4yjR9k1Jf-wzg_H4Ak5llcY_O_XSxhqd3lTH5UdqFSvYxIlaYi4ZPQh4jEMowcg1XFfWXNzrYRwBn9m_O4armtaDX5ga9HpiN5Waraqe2f5fEgtyd4lCQ2YwZpAawKeztSlZbGrxFJObpun6ZXCvq-G-9usFo2FN3vc8O7OVoNuf4kO_1Cc_Mo7IDYIXqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
✔️
با درخواست علیرضا بیرانوند مبنی بر انجام معاینات پزشکی موافقت شده و او برای بررسی‌های بیشتر به بیمارستان معرفی شده است. این اقدام باعث تعویق موقت زمان اعزام او (که قرار بود اول مهر باشد) شده است. اکنون مشخص نیست که اگر او موفق به اخذ تاییدیه وضعیت پزشکی…</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/140278" target="_blank">📅 17:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140277">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
⚽️
⏳
۴ گزینه‌ی جانشینی مجتبی حسینی روی نیمکت نساجی
🔴
در صورت قطعی شدن جدایی مجتبی حسینی از نساجی، سعید دقیقی، سعید الهویی، محمود فکری و جلال امیدیان گزینه‌های جانشینی حسینی خواهند بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/140277" target="_blank">📅 17:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140276">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
بازیهای دوستانه ما تو فیفادی:
✅
پرسپولیس
🆚
گل‌گهر
❌
پرسپولیس
🆚
چادرملو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140276" target="_blank">📅 17:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140275">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
بازیهای دوستانه ما تو فیفادی:
✅
پرسپولیس
🆚
گل‌گهر
❌
پرسپولیس
🆚
چادرملو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/140275" target="_blank">📅 17:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140274">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✔️
✔️
پیام صادقیان خطاب به امیرحسین محمودی:
✅
بهش گفتم سرت تو فوتبال باشه و فقط به تمرین فکر کن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/140274" target="_blank">📅 17:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140273">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
❌
بیرانوند قصد دارد پیش از رفتن به فجر سپاسی، قراردادش را با تراکتور فسخ کند تا مشکلی بابت چند ماه باقی‌مانده قراردادش نداشته باشد. با توجه به بسته شدن پنجره نقل‌وانتقالات لیگ برتر، بیرانوند از ابتدای نیم فصل دوم می‌تواند برای فجر سپاسی شیراز به میدان برود.…</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/140273" target="_blank">📅 17:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140272">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jk_Y2VJzQ6t9PMEQzxH2afBwJtjWE0odxk2_mXuOJ20KqlnrXAwaBy08uUVR4SeD6OkHaM0T753KHQ2lApA02ZYUk5P_PpioCnRHNRaXmHdy4nCgXBnvPH8QO_mVQYvh41AkkqZcq2m-phhKQde-Q4cEcQgkhd4rfuu-vMbBIvxflOrIshHjC9SHw_P7ZaWLEW4FRYD5WuiQsmHJr3tf0xKHbea2nF4i-uQptDs3jtYnHzGr4Dj7GTCzveHbRXK1_FN0z_Oz5bR0AQy4HJYTqu2yWggFumvpFVlwZDKblHcPTOvezNzJVlyV5Sf-eequkRSDtwYHZeSherV5VbnofQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
ROMA -
🔵
INTER
⏰
Tonight 19:30
🏟
Stadio Olimpico
🔵
رم در خانه با تکیه بر مالکیت و فشار هواداران، دنبال کنترل ریتم بازی است؛ اما اینتر برای تغییر جریان مسابقه فقط به مالکیت نیاز ندارد. نبرد اصلی در میانه میدان و انتقال‌های سریع رقم می‌خورد؛ جایی که کوچک‌ترین اشتباه می‌تواند ورق را برگرداند. یک بازی نزدیک و تاکتیکی که احتمالاً تا لحظات پایانی، نتیجه‌اش باز بماند.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد سایت شو و دیدارهای امشب لیگ اروپا رو پیش‌بینی‌ کن:
👇
🟣
Wincobet.com
🟣
Wincobet.com
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/140272" target="_blank">📅 17:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140271">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc94830254.mp4?token=K6Nlv_Sg_UucwFJdlAlH2-s4KndECuNSlfslRLeYw13MNipatS3ICPgnaU2RXU9-9huxWzaJnRKLpVV_BVHEpVHJYFyU1c1khZSzw5HUji1d6I77WBNxrcdQMGVGAhHtf6LWWkFJ4gp0H56yI3b0v52LNWsEB2yD95lrQMUoLuNAKmku_7OjmSK7nfHrOzEb6MN9nf6zZGOlWcnC50LCz9HaCiVopROVyN94mBikt2cS-99ntN_WPEB82tEszoa-pf3QAyfRw9arQV3FS9z4O511BtEVWLsi9Qc6L898qjaxANGT66mKihe6GyjUIngx6c3OGRrBLxxg_5NlXokGIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc94830254.mp4?token=K6Nlv_Sg_UucwFJdlAlH2-s4KndECuNSlfslRLeYw13MNipatS3ICPgnaU2RXU9-9huxWzaJnRKLpVV_BVHEpVHJYFyU1c1khZSzw5HUji1d6I77WBNxrcdQMGVGAhHtf6LWWkFJ4gp0H56yI3b0v52LNWsEB2yD95lrQMUoLuNAKmku_7OjmSK7nfHrOzEb6MN9nf6zZGOlWcnC50LCz9HaCiVopROVyN94mBikt2cS-99ntN_WPEB82tEszoa-pf3QAyfRw9arQV3FS9z4O511BtEVWLsi9Qc6L898qjaxANGT66mKihe6GyjUIngx6c3OGRrBLxxg_5NlXokGIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
حمید مطهری سرمربی فولاد: پرسپولیس تا الان نتایج خوبی گرفته است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/140271" target="_blank">📅 16:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140270">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‼️
💢
💢
💢
باشگاه پرسپولیس میخواد در پایان جام ملت‌های آسیا برانکو ایوانکوویچ‌ سرمربی‌ سابق سرخپوشان رو بعنوان مدیر فنی این باشگاه به جمع سرخ پوشان برگردونه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140270" target="_blank">📅 16:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140269">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
💢
💢
✔️
✔️
مدیران باشگاه پرسپولیس هفته گذشته‌ مذاکرات برای تمدید قرارداد پنج ستاره آغاز کردند
❌
پیام نیازمند
❌
محمدحسین کنعانی زادگان
❌
تیوی بیفوما
❌
اوستن اورنوف
❌
ایگور سرگیف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/140269" target="_blank">📅 16:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140268">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
قراره در فاصله تعطیلی لیگ، برنامه آماده‌سازی پرسپولیس با برگزاری ۲ یا ۳ بازی دوستانه دنبال بشه تا سرخپوشان از شرایط مسابقه دور نشن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/140268" target="_blank">📅 16:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140267">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWaRBPKIHHYfBERnBP4oeXSVRk9gXDuIAYFc8Z4MmALLIMaSArkPl6V00P1sG0ALZyar_kBVlwQ1L1jmmgvV9qqPdRONmEpxjK-K7czUxdyQAtmcylGg_AlRDeejeuLwCJ_a1bs4DmeBPF8mb22C2OJu6lNTF3awIZiNgoBZsser1xeNfY5tWmPB3KeH30WT-2muhpx8R8_MEE3vyAuaYB5tzVF4_0_vgZZGcthLFOvWUybtZGyGrWUGy8D2AUdU2s1qeGS5sKBz-TDF2Z93uRw_rkFf_Mrhz2E3jwvFN6LPZk4P4V_3Io-ayS43X0e_yc-3eKP1slTPgoE00iOASg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تیتر روزنامه‌ گل درخصوص دعوت شجاع خلیل‌زاده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/140267" target="_blank">📅 15:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140266">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✔️
✔️
میلاد محمدی در آستانه دیپورت از لیگ بلاروس!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/140266" target="_blank">📅 15:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140265">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
فرهیختگان:
❌
مدیران پرسپولیس معتقدند که مدرک کافی برای پیگیری شکایت یاسر آسانی در CAS را دارند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140265" target="_blank">📅 14:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140264">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
❌
❌
فووووووووری
❌
پیمان حدادی با درخواست مالی امیر حسین محمودی برای تمدید قرارداد با پرسپولیس در صورت گنجاندن بند 1.8 میلیون دلاری موافقت کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140264" target="_blank">📅 13:56 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140263">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
❌
❌
🗞
فوتبال۳۶۰:  بشار برای برگشتن به پرسپولیس پالس مثبت نشون داده.تارتار تأیید بده برگشتش قطعیه
✔️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140263" target="_blank">📅 13:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140262">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
❌
آغاز تمرینات پرسپولیس از یکشنبه در تهران
✔️
✔️
تمرینات پرسپولیس پس از چند روز تعطیلی از روز یکشنبه ۲۹ شهریور در تهران از سر گرفته خواهد شد.
✔️
✔️
برخلاف برخی شایعات درباره احتمال برگزاری اردوی خارج از تهران، مهدی تارتار در شرایط فعلی برنامه‌ای برای برپایی…</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140262" target="_blank">📅 13:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140261">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/052167cdae.mp4?token=OxddthI_5_ne9hkPNIFqWf7aH6rgujd3e2zXE0lgurypEnlBu7BKdJsi_mGC6ZsSPIxIadBecdJsvVeFlC5TL33cJEQ-nJ95rQuPed5Zw_x9PyxW0CbxJ-UPupv1ey5UCVEoUFzyR7mZxrz48EcWvJ6J2S9T0oQxm9GLBTajvAvZsXO89a4DQOcYdNcxPwk1PG1BT9gvTEySMWnIwMsKL07lBos68KZtecGDFfyhWCdvbzGNbz1CsKYWYj-vYhHwLPwfGahs2ZZzlsx3w2H0ubhq84Uq4wDp0wv82B-ehlCPm7hG6GYjweh9mUzJeXhuNIcSbwrHbiopDXsNvtGX3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/052167cdae.mp4?token=OxddthI_5_ne9hkPNIFqWf7aH6rgujd3e2zXE0lgurypEnlBu7BKdJsi_mGC6ZsSPIxIadBecdJsvVeFlC5TL33cJEQ-nJ95rQuPed5Zw_x9PyxW0CbxJ-UPupv1ey5UCVEoUFzyR7mZxrz48EcWvJ6J2S9T0oQxm9GLBTajvAvZsXO89a4DQOcYdNcxPwk1PG1BT9gvTEySMWnIwMsKL07lBos68KZtecGDFfyhWCdvbzGNbz1CsKYWYj-vYhHwLPwfGahs2ZZzlsx3w2H0ubhq84Uq4wDp0wv82B-ehlCPm7hG6GYjweh9mUzJeXhuNIcSbwrHbiopDXsNvtGX3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
آغاز مراسم افتتاحیه بازی‌های آسیایی ۲۰۲۶ در ناگویا
❌
مراسم افتتاحیه بیستمین دوره بازی‌های آسیایی در ورزشگاه میزوهو شهر ناگویا ژاپن آغاز شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/140261" target="_blank">📅 13:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140260">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✔️
✔️
حدادی: محمد عمری پیشنهاد رسمی خارجی نداشته است
✔️
دو باشگاه بعثت کرمانشاه و فرد البرز پیشنهاد دادند که امتیازشان را به ما واگذار کنند اما چون زمان از دست رفته تلاش می‌کنیم در لیگ ۲ تیم داری کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/140260" target="_blank">📅 12:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140259">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjmJDjxQpib-C0Z67a1nYw4YWwufFCKZSbCmhU8M5kLeWwlhJhFUyMNQ8_R_RNBU8rTiRfCgrKZFmrPgK2ybqY-M-ksyO0OL9K40omeNUdqhsj2Bc0jw7nH3rHE0xgr4y8bGHZ56LNbfu1PXyWX7fVrQJGUghzDb2Q3MbU2QrzYSWI44R7RPD3Utkj41sjMMnychFx3qX__QVu7b9JrWpW6MYPsFC2JkJo5LgP-CqEuDh4N2BrZ8puoATunpIZ_DHaKWCV6p20MOFBJoNbhsmv9nlYhwVonVzBvRe5zhxF4gVp9kiNG1bH6kjbDR2Qv38K9RMqBgL2kV4Uz3aauJCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
⏳
۴ گزینه‌ی جانشینی مجتبی حسینی روی نیمکت نساجی
🔴
در صورت قطعی شدن جدایی مجتبی حسینی از نساجی، سعید دقیقی، سعید الهویی، محمود فکری و جلال امیدیان گزینه‌های جانشینی حسینی خواهند بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/140259" target="_blank">📅 11:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140258">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‼️
خبرگزاری تسنیم: علیرضا بیرانوند در پایان فصل به تیم کیسه خواهد پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/140258" target="_blank">📅 10:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140257">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
❌
باشگاه فولاد امروز بار دیگر تمام پیشنهادات پرسپولیس برای جذب رزاق پور را رد کرد و این بازیکن در فولاد ماندنی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/140257" target="_blank">📅 10:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140256">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iykxt5hS77bUPmcWpp-M1Uv32sma7Y_Bbt5-wrWRXU7OTp5XKl-i43B5OPxSYbK9H7FWDncqnqIT4SFvDM6gnNUDYchkquceZzyu5HRMuxV9noPviy8QIDhwc9gcfx-ULArQJ-Hud4UT0ewoZLI57Y8slxoD0czl314_mktUFlkBap7Wownr4f3XnG5KIi2xjxZo8QLj_EeW7ZKlpNL9J-YsAwngQgWusCJjCzNKv84fd5v_3AxCUFaCY6ps6-HbrWQ7Pe5iZlZzMK7Bus-Uh_ZUtMK42aU4DTYQEER5A4e5GO7ghx1Lr2RltayP5SAZnrQ4073pq-SHyXYQLDIDRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/140256" target="_blank">📅 09:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140255">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a058da26.mp4?token=vrzcuD3UkT4aaO4fBTzRBrY_IKxcjI0_bNeblunZ29BKfH6Kezv6LRbOX3erBkdbcczqVW5cgqGi09pY7qAHW-T2R-Dw9EqgFpO18BDnCBtsPaJo9N6MfS28yny7BpgOmNkU5xbpGeMcdexdHauQRNdDYin7WwJPW6twJ7HAO0lK9MIvBP-OTWZBVi8FOFN6PK7UC_sVmyeqwo1lPLnVqTMfp54sm4-422CCh8inO_KqQSf8AXlpOfEhPFFp4GAwR-TNGsqngd_SXxRHo1k3I1M8CTP--IN7i63TivOFNX9catNB627XrtIqJF8wjIuKq4UiZkXyhP5RxtmyMsBYFCrFOnczXxfcAneqcs1DoiZL7VWVeCnVrMEAzFg71F_LnZjQoWirSgM0ZGjFj_vDf63-0CeBwp8KqcqK960KX7DqREaW78rcCGLqk-f8Kln1I24IlFlgjUJuLRODb1KnOzoCuEVZaA5UWCpbaUL5zzoX7cALPllwMb5N1rYt3kmQRzP5MYZEFeOiay0YpHE9Q_pfIRWYWxN8Fh9CxWngoorftqvh24JqkmPSXvVrdHJdrgQbOXX1rkhga-TiXPUJA4zneyZb1dEcU4OufGlmxR7p-bHOr6a2Gfl-BG7Ss1OeWomxWS7cub66M2OylGxDxMHr1aQDucrFgKRF0lEVWCk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a058da26.mp4?token=vrzcuD3UkT4aaO4fBTzRBrY_IKxcjI0_bNeblunZ29BKfH6Kezv6LRbOX3erBkdbcczqVW5cgqGi09pY7qAHW-T2R-Dw9EqgFpO18BDnCBtsPaJo9N6MfS28yny7BpgOmNkU5xbpGeMcdexdHauQRNdDYin7WwJPW6twJ7HAO0lK9MIvBP-OTWZBVi8FOFN6PK7UC_sVmyeqwo1lPLnVqTMfp54sm4-422CCh8inO_KqQSf8AXlpOfEhPFFp4GAwR-TNGsqngd_SXxRHo1k3I1M8CTP--IN7i63TivOFNX9catNB627XrtIqJF8wjIuKq4UiZkXyhP5RxtmyMsBYFCrFOnczXxfcAneqcs1DoiZL7VWVeCnVrMEAzFg71F_LnZjQoWirSgM0ZGjFj_vDf63-0CeBwp8KqcqK960KX7DqREaW78rcCGLqk-f8Kln1I24IlFlgjUJuLRODb1KnOzoCuEVZaA5UWCpbaUL5zzoX7cALPllwMb5N1rYt3kmQRzP5MYZEFeOiay0YpHE9Q_pfIRWYWxN8Fh9CxWngoorftqvh24JqkmPSXvVrdHJdrgQbOXX1rkhga-TiXPUJA4zneyZb1dEcU4OufGlmxR7p-bHOr6a2Gfl-BG7Ss1OeWomxWS7cub66M2OylGxDxMHr1aQDucrFgKRF0lEVWCk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
تجربه‌ای متفاوت از هنر روپایی و تصمیم‌گیری با Crash Kick؛ جاییکه مهارت با هیجان گره می‌خورد!
⚽️
در کراش کیک، هر روپایی موفق ضریب برد را افزایش می‌دهد و هر لحظه وسوسه ادامه دادن بیشتر می‌شود. هنر اصلی بازی، انتخاب بهترین زمان برای برداشت جایزه قبل از پایان روند صعودی است. این بازی با ترکیب هیجان، تصمیم‌گیری لحظه‌ای و مدیریت ریسک، تجربه‌ای متفاوت و نفس‌گیر را برای علاقه‌مندان به بازی‌های سریع و پرهیجان رقم می‌زند.
✅
جسارت ادامه دادن یا هوشمندی در برداشت؟ تصمیم تو، سرنوشت جایزه را مشخص می‌کند.
📌
همین حالا وارد ربات وینکوبت شو و هیجان واقعی رو لمس کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/140255" target="_blank">📅 01:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140254">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✔️
✔️
میلاد محمدی که تو تیم جدیدش حسابی ریده گفته میخوام برگردم پرسپولیس  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/140254" target="_blank">📅 00:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140253">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
❌
❌
❌
پست خداحافظی میلاد محمدی از پرسپولیس
✔️
✔️
امروز با قلبی پر از احساس، از خانواده‌ای خداحافظی می‌کنم که همیشه بخشی از وجودم خواهد ماند. از هم‌ تیمی‌های عزیزم بابت تمام لحظه‌های فراموش‌نشدنی، و از هواداران پرشوری که در هر شرایطی کنارم بودند، از صمیم قلب سپاسگزارم.تا…</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/140253" target="_blank">📅 00:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140252">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✔️
✔️
تعطیلی ۲۵ روزۀ لیگ برتر
🗣
🗣
لیگ برتر حدود ۲۵ روز تعطیل خواهد بود. بخشی از این تعطیلی نسبتاً طولانی به دلیل همکاری باشگاه‌ها با تیم ملی امید است و بخش دیگر نیز مربوط به روزهای فیفاست که از ۳۰ شهریور تا ۱۴ مهر است.  «سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/140252" target="_blank">📅 00:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140251">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">⭕️
⭕️
پرسپولیس مهدی تارتار در این فصل ۴ برد ، یک مساوی و یک باخت داشته ؛ ۱۲ گل زده و ۳ گل دریافت کرده امید گل تیم تارتار ۱۲/۲۷ بوده که با این امید گل موفق شدیم ۱۲ گل بزنیم و امید گل مواجه شده ما ۳/۲۴ بوده و از ۳ گلی که دریافت کردیم دو گل روی اشتباهات فردی بوده…</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/140251" target="_blank">📅 00:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140250">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7629b3f4d1.mp4?token=HwQfwCSQDGruXD8a_WnHvgga_DgcX8M0eC89BEFzDMWlopSaki9_3aZZ60ws275qmPNKpuerhb8e6gsuOTpuxO7X79QgbOZ2U2oFPw88KV9VjGypsdqjZtgnKHJNCM7hUeyoI0FcS35L--SjBNw4SPo8jjwrFog5kxgVqUMb5oqo7odXc7z2KB7M41kWBmzjT3R3WzsweN62wWPsvwJ7HHzWfAuD58LDKjffoudXbbQEcZCrXetiiINH6u7rGXw486M1HlibeVghHTmLc0ZvvBNaa4htTrdPZkssMbzmP30gb8ixGmfQ3ixF9RBsJ67M_CdjH-CBuP0pUeKxi5vKcqo33xu53t4-x7J_Ud88MBMujhvZ5Sn215aRsZ7vVTiXkdxlNZ8LapPYiJvozzyjwlaeRSzYlZtoVmXuub7ifdU8jBLBxofrEmo_VCxYN98Gvkd33q79_S3n8cwMWWhZF_coiTsl-R9GVFBMv0hSB7xetbX1lfYh7duFj0H2hfohUEH4_3ZnP-NH4l_QpbZ_GV-ZRlaRnyehWk-IGr308P_FPYZepN7nt2-h-QPdAULsFuitI0Y7ZT4JVhMcUmmhHmBsO0fthXSjivLNj9aJ3vPGyA0XXA16WhiagQqErMCZVMScFFvQTxBmTUyPH8r5dQWR2-fGqJv47dL9htFdORU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7629b3f4d1.mp4?token=HwQfwCSQDGruXD8a_WnHvgga_DgcX8M0eC89BEFzDMWlopSaki9_3aZZ60ws275qmPNKpuerhb8e6gsuOTpuxO7X79QgbOZ2U2oFPw88KV9VjGypsdqjZtgnKHJNCM7hUeyoI0FcS35L--SjBNw4SPo8jjwrFog5kxgVqUMb5oqo7odXc7z2KB7M41kWBmzjT3R3WzsweN62wWPsvwJ7HHzWfAuD58LDKjffoudXbbQEcZCrXetiiINH6u7rGXw486M1HlibeVghHTmLc0ZvvBNaa4htTrdPZkssMbzmP30gb8ixGmfQ3ixF9RBsJ67M_CdjH-CBuP0pUeKxi5vKcqo33xu53t4-x7J_Ud88MBMujhvZ5Sn215aRsZ7vVTiXkdxlNZ8LapPYiJvozzyjwlaeRSzYlZtoVmXuub7ifdU8jBLBxofrEmo_VCxYN98Gvkd33q79_S3n8cwMWWhZF_coiTsl-R9GVFBMv0hSB7xetbX1lfYh7duFj0H2hfohUEH4_3ZnP-NH4l_QpbZ_GV-ZRlaRnyehWk-IGr308P_FPYZepN7nt2-h-QPdAULsFuitI0Y7ZT4JVhMcUmmhHmBsO0fthXSjivLNj9aJ3vPGyA0XXA16WhiagQqErMCZVMScFFvQTxBmTUyPH8r5dQWR2-fGqJv47dL9htFdORU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرشته کریمی، ستاره‌ی سال‌های اخیرِ فوتسال ایران، امروز اولین بازی خودشو در قامت فوتبالیست، برای تیم فوتبال پرسپولیس انجام داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/140250" target="_blank">📅 00:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140249">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇮🇷
🇮🇷
عکس یادگاری یحیی گل‌محمدی و علیرضا منصوریان در حاشیه دیدار دوستانه دهوک و الطلبه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/140249" target="_blank">📅 23:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140248">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
❌
تا 3 هفته دیگه قرار نیست این تیمو ببینیم
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/140248" target="_blank">📅 23:57 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140247">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1rMtqeT30O_WmI3o21C2ZwFirDyrRjvmxWIcO9Ivl1_qJIgVzlFM6IB0JTL-egFtPoL4AXVFRUDNPbiGepArUYjRcE03pl5MnS1LH42HSXqsEGxCaCI-GD0qbDM5wGV4YgoLO49y7tdhgeHhmLEcVTonDjN5fgUEtGUwaFXZQufB33ysNx3Nmub8mX3ZiGtdOTCkVF0GoxyJTDcyWlAdNQkuwJg6Ga4ziP_qvnX3ntq0BnhYAs_slHC3HPLYUYvEsU5OA4nZTFX9ACMSXTyQLtb0hKY-08q9alfGD5Kyb2VDaO5Ud7j_cPBOwRVdB2i9j8bxtv2fdzMoG21d9nWbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
اینم تو یه دنیای دیگه‌ست
😂
⚡️
آخه اسکول، تو این گرما این چه لباسیه؟!
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/140247" target="_blank">📅 23:51 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140246">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
❌
❌
اوستون اورونوف به مدیر برنامه ش گفته آینده ی فوتبالیش رو میخاد در پرسپولیس بمونه و با مدیران پرسپولیس برای تمدید قرارداد سازش کنه تا قراردادش مجددا تمدید بکنه
😀
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140246" target="_blank">📅 23:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140245">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
❌
❌
هوشنگ‌ نصیرزاده‌ کارشناس حقوقی فوتبال به پیمان‌ حدادی‌ مدیر عامل‌ تیم پرسپولیس اعلام کرده که قرار داد یاسر آسانی با استقلال قانونیه و 150 هزار دلار هزینه حق دادرسی به CAS پرداخت نکنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/140245" target="_blank">📅 21:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140244">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
❌
تا 3 هفته دیگه قرار نیست این تیمو ببینیم
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/140244" target="_blank">📅 21:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140243">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
❌
ترامپ :
❌
ممکن است مجبور شویم عملیات نظامی گسترده علیه ایران را از سر بگیریم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/140243" target="_blank">📅 21:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140242">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
❌
تا 3 هفته دیگه قرار نیست این تیمو ببینیم
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/140242" target="_blank">📅 21:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140241">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5tdLB49cS8eiDTFH119GhNuwoqzafyrZ7U14-mKOYEnvC9JUDR9rhaH5GnMLlqrBa0z3b6IhYTnd3qks8qa4Nyh6lD59_uCXkEO4zTQbeoXqBH05aOXdnm2GAYZPHpPjvtQuo2CrO46YRA2OesXJ3CiKuBSLkHWY9OSfVJaD7xf09Dxku8Ns2B93VFwpSr43cplYXZGeLlvcAvy_q3X6HhQ7qZ8AVoQ3bYYEwVHyXuq-pcsZZjW6py9KAotXmFsOwzzljbxBGno1eBUOs3DhZwosY2laV78u9xxF8XDBTRSPg25CbxmyucWfEBar7KnZRwStwm5wnnsHIY6QMyKiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
عکس تیمی بانوان‌ پرسپولیس در فصل جدید
♥️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/140241" target="_blank">📅 21:14 · 27 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
