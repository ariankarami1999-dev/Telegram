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
<img src="https://cdn4.telesco.pe/file/TKgGLUZ5cWweTx26MqzBJ81CHUO2j9dQk0lC9-sFCbOP1k8nBeOeJFKvKZdTw-UjaCnIj094281BbthINKuuGzxXsPe0kixKPBzcUBZgF0IY0B0gnLe9EYOscWjiPQieqy6V3GdxibxZn8cmPWe5TDEUF6_-cjWTzsOETdfYDyepAPXzBSzgMhn-hK09ubK0z6l35D8fnD4mbcyvyE2v7Q2vvHe8kVixFoDxZjb03MWcLSOC0FNHgNmrjIiymEnSL1yA32oGt8xa25tHOTNBOYly-yysBVdzfzkCC0qGdR_WIJAzqDjU6hi9aL4YotaFpbjAadY-aXK7BZaCNfI-Mw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 18:14:17</div>
<hr>

<div class="tg-post" id="msg-136667">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
✅
محمدامین کاظمیان بخشی از قرارداد توافق پرسپولیس با گلگهر برای جذب پوریا لطیفی فر می‌باشد
🔹
محمدامین کاظمیان + حدود ۸۰ میلیارد رضایت نامه = پوریا لطیفی فر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 215 · <a href="https://t.me/SorkhTimes/136667" target="_blank">📅 18:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136666">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
باشگاه استقلال پیشنهاد 5 میلیون دلاری آسانی رو قبول کرد و این بازیکن شنبه به ایران برمیگرده !!!
😕
😕
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 619 · <a href="https://t.me/SorkhTimes/136666" target="_blank">📅 18:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136665">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
در شرایطی که قرار بود امروز بازی پلی اف لیگ برتر بین مس رفسنجان و صنعت نفت برگزار بشه.. تیم مس تو زمین حاضر نشده و آبادانیا جشن صعود به لیگ برتر گرفتن
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SorkhTimes/136665" target="_blank">📅 16:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136664">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
❌
تارتار اسم یه مهاجم خارجی رو به باشگاه داده و درصورت جدایی بیفوما و گرا مدیریت برای جذبش اقدام میکنه/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SorkhTimes/136664" target="_blank">📅 16:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136663">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❗️
❗️
خطر رفع شد؛ به ادعای ورزش سه زکی‌پور ۲ ساله با تراکتور بست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/136663" target="_blank">📅 16:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136662">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
❌
دنیل گرا و تیوی بیفوما هم توی اردوی ترکیه کنار پرسپولیس هستن.
❗️
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/136662" target="_blank">📅 16:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136661">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
۳ خرید ناب در راه پرسپولیس
💥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/136661" target="_blank">📅 16:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136660">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">⚠️
⚠️
تیم فوتبال پرسپولیس در اردوی ترکیه با فنرباغچه که هدایت آن برعهده اسماعیل کارتال است، یک دوستانه بازی برگزار خواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/136660" target="_blank">📅 16:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136659">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
پناه بگیرید
✅
میلاد زکی‌پور رسما از سپاهان جدا شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/136659" target="_blank">📅 14:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136658">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔹
نگاهی بندازیم به هایلایت‌ پوریا لطیفی‌فر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/136658" target="_blank">📅 14:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136657">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❗️
میلاد زکی پور، مدافع چپ سپاهان پس از قرار گرفتن در لیست خروج محرم نویدکیا، به پرسپولیس معرفی شده تا جانشین میلاد محمدی شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/136657" target="_blank">📅 14:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136656">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LqCvkpaBblfU4DArPj0JKSp1rNU6ZbIqKRjTco2IhvVOMl3EO5omk4uB0SJn2eNMN6Bqd85PQNxct9UuAkqcw0w9kMajRBYaGZmiEI2h6HjE1o5Dx5PkW5-ju-2IsnMoI-tSiw6Jsxy6EbJY70-niykfyRAIikCzdA0ZCJNjV7yzRZ-fUx39mdAvE9WAPgK52bWZ9vOP6QB61gM003p1pwRZya9qo4FWKVaJ-twsmEz92-pxQc8klpx51ki-FbbWLAAEQ3ELHgG8B5QELaQscs24V-0HeBX6o5RZSzMDRL2bI6N1fb3IlRLOiL4JQts-KrIN_xWjZeBJwiwFOIR0AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽
لطیفی فر با عقد قراردادی چهار ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/136656" target="_blank">📅 14:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136655">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVfCwqWDUk-IhYF6btoL5q1kM_jsbWd-1hrbQeVZpseIPiOWkWYU9gyZCzS5_rymqVR6XWldo7AHp0tKonKEuV4Lsj_KgiiOqUhOumhKfCOPdepqvAUo5TgVnF5PyrkbOpCMwb0desAQ1aEdM-kSXTKI3XWSJXzbpKBz42mgOqJsk3ck4XjsPStu_Ny-_ZUiHliiSCcRZ_B-a4lGzB_ogwr9rrg-z403rt4Dec5mxMjV_QZIkZKRVSBcgicdS8buwg31RMqfq_ohQQmsREGsfMVczdh6Iul9oRmXrhmxdia3VooY3lpOnoJb3NxTIRep3fiqsIOO5ORTBM2fZGft_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
۳ خرید ناب در راه پرسپولیس
💥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/136655" target="_blank">📅 14:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136654">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogtWDqMYI87ZSirLxSbrtHHiGfedvc7CW-DBS6QkOdq6LF8lcVC-rSiKI-V8OUeGDbYCiXVznl7fmNdzV7yEcUhPgJrSycQjmwM5vclRWu_RsKGecXVKf_muNDLcGomDjqe9nmdHHSAK-dnn9MHEt4yxUnDXtLKjloo0WbTf42enC2dlDxUYqhZ2BrXSs4VAwvoYdMZv3qAKQq5v6KGl7RbcCOVRoBQQvyRz1FYwMiHUlySOwcZggedC2AQoiIMGOntB2WmAC60zbciM1WAYX43xY3B8vD1xr93-t3vkZAmeRNV4fGZnyVBX4ZZGjn-jnEyLfQs-Wzr8VYaQovd56A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مدیر رسانه‌ای جدید پرسپولیس انتخاب شد
❗️
❗️
فربد بقایی مدیر رسانه‌ای سابق چادرملو و ساپیا جانشین روزخوش شد.
🔴
🔴
بقایی حدود ۱۰ سال قبل در سایپا فعالیت داشته و فصل گذشته در باشگاه چادرملو مشغول به کار بود.
🔴
🔴
خبر انتصاب بقایی طی امروز یا فردا از رسانه باشگاه منتشر خواهد شد و بزودی او راهی اردوی ترکیه می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/136654" target="_blank">📅 14:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136653">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
پیروز قربانی: من نیوزلند رو با فجر سپاسی شیراز می‌بردم مطمئن باشید نیوزلند اگه تو لیگ 16 تیمی ما بود، جزو چهار تیم آخر میشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/136653" target="_blank">📅 13:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136652">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❗️
واکنش ابوالفضل رزاق‌پور به پیشنهاد پرسپولیس:
🔴
نامه رسمی به باشگاه فولاد آمده ولی من وظیفه دارم سر تمرین بیایم تا تکلیف مشخص شود. خودم با باشگاه هیچ حرفی نزدم و دو باشگاه باید باهم حرف بزنند.
🔴
🔴
حضورم در پرسپولیس برای دعوتم به تیم ملی تأثیر دارد ولی امیدوارم…</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/136652" target="_blank">📅 13:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136651">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❗️
مشکل سربازی فرهان جعفری حل بشه با قراردادی ۴ ساله پرسپولیسی میشه/طرفداری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/136651" target="_blank">📅 13:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136650">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">#تکمیلی
⚽
💥
حدادی منتظر پاسخ محمد مهدی محبی؛توافق با کلبا انجام شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/136650" target="_blank">📅 13:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136647">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
💣
One Signature. One Earthquake…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/136647" target="_blank">📅 13:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136646">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🤩
باشگاه پرسپولیس فردا در دیداری تدارکاتی به مصاف پیرامیدز مصر خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/136646" target="_blank">📅 13:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136645">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
⚽
لطیفی فر با عقد قراردادی چهار ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/136645" target="_blank">📅 13:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136644">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3UDQK0I6sTPVPUWm59XcMWoU68eI74VOKC0NibYSx_NC0rRE3_PT96c2gEbkeHdsnE4FuCmsBf4wYs9kvPDh0s0qEFOkC2y6HjCLA3Sb2TkFG8mA8cZ4Cn3t20wM1C4rkUd4U_UqHiPzpUP4bSingU64LSyVomct4DJeoY8J8vkmAFQhDLOSVFRxiNu1-f19iDryvNsJYtesdT85lFVTkHQWJEgcYq3QJtDmkMsqLMZNft27hfNwvqLO1sYl5qdd1281sQgjfpWUNEZI17To8syheIxPM6-KrxN0gfTs4vyqLup0Ll0huujfrtAtkcFiy02DFr26HvHm2wdpGYbAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽
لطیفی فر با عقد قراردادی چهار ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/136644" target="_blank">📅 13:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136642">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/136642" target="_blank">📅 12:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136641">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/136641" target="_blank">📅 12:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136640">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
❌
امروز تکلیف نهایی دانیال ایری و کسری طاهری برای پیوستن به پرسپولیس مشخص خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/136640" target="_blank">📅 11:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136639">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
❌
بعد از 13 شب .دیشب و بامداد امروز هیچ حمله ای به ایران و نقاط ایران از جمله جنوب نشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/136639" target="_blank">📅 11:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136638">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
🚨
باشگاه پرسپولیس قصد داره‌ تا ۲۴ ساعت آینده از چهار خرید جدید خودش رونمایی کنه ///فرهیختگان
🤝
محمدرضا اخباری
🤝
دانیال ایری
🤝
کسری طاهری
🤝
پوریا لطیفی فر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/136638" target="_blank">📅 11:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136637">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✅
برخلاف شایعات ؛ حضور براجعه در تصاویر اولین تمرین پرسپولیس در ترکیه
❌
در حالی برخی منابع از عدم حضور براجعه در اردوی ترکیه پرسپولیس خبر داده اند که این باریکن در تصاویر اولین تمرین سرخپوشان در ترکیه حضور دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/136637" target="_blank">📅 11:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136636">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❗️
🚨
🚨
باشگاه پرسپولیس با باشگاه اتحاد الکبا برای انتقال محمدمهدی محبی به توافق رسید  #قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/136636" target="_blank">📅 09:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136635">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNKHZz08Bep4bXLTJw-yr9t2l5ed2viWRmWA-jDQRaIlISDui5VO_JnzYVevPlFld70HIwI0VsIGiyE4f5g8lyaPfW1F49t8Rk-Xn8IFg0UwxmvhdMnTN2i74qsyw1F7P10Oi8B4lNcxIGqXcLY4259C9IsoP6pD0lIynad46DWsGDzwA8qAIOKfVxa1bej02a3EbqNQ9vKgjYodVj5glWrkFWw-yac6sZgEMW3CtT87FhcHnSs0GQhxKV3_VlQMqVjwYXwP-o2u8Zq5nPoQMsnAUPAYBQ9g209typiRPdD0kJI9UQRzW-jfpOEva2vteaM32amgwPlFJ0mV_13pkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف شایعات ؛ حضور براجعه در تصاویر اولین تمرین پرسپولیس در ترکیه
❌
در حالی برخی منابع از عدم حضور براجعه در اردوی ترکیه پرسپولیس خبر داده اند که این باریکن در تصاویر اولین تمرین سرخپوشان در ترکیه حضور دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/136635" target="_blank">📅 09:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136634">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❗️
🚨
🚨
باشگاه پرسپولیس با باشگاه اتحاد الکبا برای انتقال محمدمهدی محبی به توافق رسید  #قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/136634" target="_blank">📅 09:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136633">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✅
✅
محمد مهدی محبی تمایلی ندارد قرارداد یک میلیون و ۴۰۰ هزار دلاری خود با باشگاه کلبا را از دست بدهد. باشگاه کلبا نیز قصدی برای ادامه همکاری با او ندارد، اما خود بازیکن حاضر به کوتاه آمدن نیست. با این حال، پرسپولیس هنوز از جذب او ناامید نشده است.///قدوسی
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/136633" target="_blank">📅 09:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136632">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
🚨
باشگاه پرسپولیس قصد داره‌ تا ۲۴ ساعت آینده از چهار خرید جدید خودش رونمایی کنه ///فرهیختگان
🤝
محمدرضا اخباری
🤝
دانیال ایری
🤝
کسری طاهری
🤝
پوریا لطیفی فر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/136632" target="_blank">📅 08:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136631">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">⚠️
باشگاه پرسپولیس هنوز با مرتضی پورعلی گنجی برای فسخ قرارداد این بازیکن به توافق نرسیده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/136631" target="_blank">📅 08:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136630">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
❌
بعد از 13 شب .دیشب و بامداد امروز هیچ حمله ای به ایران و نقاط ایران از جمله جنوب نشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/136630" target="_blank">📅 08:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136629">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✅
✅
#تکمیلی | رویترز:
🔴
ترامپ دستور حمله قدرتمند به ایران را صادر کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/136629" target="_blank">📅 08:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136628">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSMyUS0ivU3xH4oYu5blknA5NvETQyqN9hR9gbx66C3U28XUMGJAJhBZLtZ_UE3jXpB6mCeFDbIxas17T5qkeMXLBBghzsvpu3GXlpJGiP4RXkpNrjn2ZnrBjrgboY2klW5g-Kkb245d7qtiOqHCQjva0SJx-yWgVaBu_Z1Job0p9tyF3sr7cEw7B2_Pl1lO0YfefBxgODpuuOwb_kmNY4_PscFWk8hBtADecBlZ2onxaEzxMB6XZ1Xt8jp5ra717mHyuTD8CM7_rBPax4P298hnqT7kaxsJL8_EJlNxARFJ_bMNPnD4XzSifBLnKAsJYyHK5OHG7cel4MetJf2LVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/136628" target="_blank">📅 08:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136627">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136627" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/136627" target="_blank">📅 01:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136626">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDBjT2D6jr8iBvlShpmLtdgg1wTQGvObzxd8cZMd9aX_bm_4SPmh8BWl_TMTOHHeEBCA1yLWGHK4qwnsRd5LDxk2DggAWrM-n0W3_gHhaI2VfytTQa22tpO_Im2CzBYKjbobFH7ByRxPnZlxdPFC_z37YJ2tI0hRx9cVHY_GzUnbXYMEHj5TEZ2hsSXg4C2vvmRdzkFbqh3VaAxWdohNyZkAKFGI5koH6L0H4jSdnBmBzUBwnfBtH0IKX1WETwGs4YWaMOz2tXUi6y0xFcDFApFJINvxXY8dQjykoF16U7nd2HpfsEnzlTrDSbuomaJrDA2xZ9Dl6TLoCbUXhAbGPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هر
چهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
Ⓜ️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/136626" target="_blank">📅 01:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136621">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9qbYR9wS1hIymTw-2eUMN1eQsRsMDeoAjzElIhuynu-gq2jv10OomF4ZIsgIMWeSD-qdwkrh0-B8GmgAJ0ioXFAHpN6sZN6t9k4OIZFbynV3GGqM15euLe_kk32KWIuLye4zqUQYjSw3bt96TKZwluMG8A-ceDZNlX4ujhR1EQkxhwUuL7kkWPrFPkkI74tvdvkZKE1SPY5B58ncWI2UUcqEPmdYP0794-ImFQJmviLfR98W6t1OJ8vZmdJURIPY88c4-PuEV2k-RqQpBUS-XeBoJn6k8U3yTuBkd9xUsHjCBq-GpPd75q3vnjVMHKdfGEo1N3r4LihJw7OJEmo3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوررررررییییی ؛
‼️
بمب نقل و انتقالات پرسپولیس از امارات می آید
🔴
بازگشت ستاره سابق پرسپولیس
⁉️
👀
✅
پیشنهاد رسمی پرسپولیس به ستاره خارجی تراکتور
📝
Deal Done
🤝
⏳
❌
برای مشاهده خبر کلیک کنید</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/136621" target="_blank">📅 00:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136620">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔹
دونالد ترامپ: با وجود اینکه درحال گفتگو با ایران هستیم اما باید بگویم که مهمات ما برای یک حمله وحشتناک به ایران تکمیل شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/136620" target="_blank">📅 23:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136619">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
❌
#فوری |ترامپ به شبکه 12 اسرائیل: من در حال بررسی امکان انجام حمله‌ای بزرگ‌تر از هر چیزی که در گذشته شاهد بوده‌ایم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/SorkhTimes/136619" target="_blank">📅 23:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136618">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✅
✅
تارتار دنبال جذب یک وینگر دیگه‌ست؛ بین گزینه‌ها فعلاً فقط با محمدمهدی محبی مذاکره می‌شه. برای همین هم بیفوما رو به اردوی ترکیه برده تا اگر وینگر جدیدی جذب نشد، ازش استفاده کنه.
❌
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/SorkhTimes/136618" target="_blank">📅 23:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136617">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
❌
تقویت پست وینگر و جذب محبی از کلبا تازه ترین هدف و تصمیم نقل و انتقالاتی تارتار است.
❌
محبی که مربی کلبا روی بازیکن خارجی دیگری به جای او حساب کرده نمی خواهد قرارداد یک میلیون و ۴۰۰ هزار دلاری اش را از دست دهد. باشگاه پرسپولیس امیدوار است محبی نرمش نشان…</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/SorkhTimes/136617" target="_blank">📅 23:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136616">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
فوری، حمید مطهری با جدایی ابوالفضل رزاق پور، مدافع چپ فولاد خوزستان و پیوستن این بازیکن به پرسپولیس مخالفت کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/SorkhTimes/136616" target="_blank">📅 22:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136615">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✅
معامله گری که سرباز شده و برای دفاع چپ فقط ی جلالی و داریم و خلاص که اونم مصدوم شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/136615" target="_blank">📅 22:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136614">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">💥
💥
شماره جدید بازیکنان پرسپولیس در فصل آینده مشخص شد
🔴
محمد مهدی زارع ؛ شماره 4
🔴
محمد عمری ؛ شماره 7
🔴
مهدی تیکدری ؛ شماره 8
🔴
ایگور سرگیف ؛ شماره 11
🔴
یعغوب براجعه ؛ شماره 13
🔴
پوریا شهرآبادی ؛ شماره 17
🔴
امیرحسین محمودی ؛ شماره 19
🔴
مجید عیدی ؛ شماره‌ 20
🔴
ابوالفضل…</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/136614" target="_blank">📅 22:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136613">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
پرسپولیسی‌ها عصر امروز تمرینات خود را در حالی پیگیری کردند که پیام نیازمند و محمدحسین کنعانی‌زادگان پس از حضور در جام جهانی ۲۰۲۶ به تمرینات تیم اضافه شدند و کریم باقری نیز در جمع اعضای کادر فنی حضور یافت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/136613" target="_blank">📅 22:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136612">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
باشگاه اتاق محمدرضا اخباری را در ترکیه رزور کرد و هم اتاقی کاپیتان تیم حسین کنعانی خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/136612" target="_blank">📅 22:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136611">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIRBYl5NiKOl9TXLojDd2FRw8s_3Q75gsPfrBWaMD_H-PTUNgrr0ALbq2q7cwpmiL1poaxXMgvQ_AYiZxu3rNTiR52foQiPhdw51lrfB7xbPLm1BQyLZZlJNgNxVNZu09EekDGczvlas9IQFUIDS7TurfT6-yv4cWPd-_bFVAPcDkhboJuUg5ielW-pjIMFcrhr-I8MEd8zQrVNiNyZeAW0-U9AjARulmE0fIHVwUnf6ASS4zWvuxUEy_z2NtR7Ofcq88LQHZcnHcVLH2PSYvQidmoT65xvdJOPVK9Fk87psku7Ws9Av8ZMO-P0_Eyum7TKebGWNp3Ws0VLOzlsTBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
حضور و اولین تمرین پوریا شهرآبادی و محمدمهدی زارع با لباس پرسپولیس.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/136611" target="_blank">📅 22:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136610">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
❌
مهدی تیکدری وارث شماره 8 پرسپولیس در فصل جدید خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/136610" target="_blank">📅 22:13 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136609">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvqNNMqn10wmuMG5QreL4-Dqpas0RtcCVPkumrmXTqisG4KppYNO-oDD0XyVSElnH0H2MVdf2HvFoZ0HZOCoDieJkNFxAGb3aiUV228ztwhKRBkQ3xo05x24ezK2LCe1fWQp0PBLJTWPemM8v_M7uwkTBeNnmz6wVDJgMjiFVXg-A7W3bAfiKQiyp2LXIIUjeS54lupiEwaMVAK6V1dfrJK3Zzx2jmRjhqM-zrKXLGSQ5FYpVeTkR6KbtEBfm2_aMy7EWQAq-PYiqeW9RbWguWT6gryeRkgkcwfBvjP3DdQhMlahipmqyMJBBSOBdb5-68cVZtR056Qh3XX3rPU-1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوری
؛متاسفانه‌خبررسید اکبرعبدی بازیگر سینما و تلویزیون دقایقی قبل در سن 66 سالگی درگذشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/136609" target="_blank">📅 21:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136608">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🌀
🌀
هیات‌مدیره پرسپولیس فردا درباره جذب کسری طاهری و دانیال ایری تصمیم می‌گیره؛ با توجه به استعلام‌های مثبت، احتمال نهایی شدن قرارداد این دو بازیکن زیاده.  قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/136608" target="_blank">📅 20:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136607">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✅
✅
فرهان جعفری در یک‌ قدمی‌ پرسپولیس/طرفداری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/136607" target="_blank">📅 20:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136606">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">⚠️
باشگاه پرسپولیس هنوز با مرتضی پورعلی گنجی برای فسخ قرارداد این بازیکن به توافق نرسیده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/136606" target="_blank">📅 20:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136605">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❗️
❗️
2 خرید جوونمون تو این پنجره :
🔴
پوریا شهرآبادی 20 ساله
☑️
🔴
محمدمهدی زارع 23 ساله
☑️
🔴
اهداف بعدی :
🔴
فرهان جعفری 20 ساله
🔴
پوریا لطیفی فر 22 ساله
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/136605" target="_blank">📅 20:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136604">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upx53kXmhTFOsQ_4GXhytgcoU-bffbQdtmpl2D8H9GeSqs3UYSSB6ZRefAbsOyBCLrj6I1YLwS88i7nsvtsaZC68TGmaHSjxq66IX8HiOsyCEkP1SXuygI95Hb4edurn_5VsyzZfHgF50eWdhNSGCMa3gTELOVM8gEj3InuXGa72f1x9l-2m70oJfe-9bPzDvq7cn4JLWxVrn8vnKm_kvmVT85qZcFDJjDfi-DvhP_Sqo4lxTJ7JER4L29W-DHqepGgnjeyreaQ7kKaX5FilA3978uNccHMGl1Y1Ty9Yvu6WnRhTZOV6YiNOs3PIrLKp_lgv7cs1L8C-X19kqlzSYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رسمی؛ رسول خطیبی سرمربی فجرسپاسی شیراز شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/136604" target="_blank">📅 20:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136603">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136603" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/136603" target="_blank">📅 20:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136602">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lblI0fXFd2kswNLLpRsTg1K8HCYm-h2LNEj5UCV5QK6LVX7_ILj39TPOPYfWQ2b__jaJ8NEYwgP6wHcXmcr_31VvybSZM-fAX8EpdAcA4wPdqSEnZWNM0PCbm57LimXZVmSasiJ3w-MZ8j4qYV05o5V0F2jrbQUytrgxhissBZRExgryvxbpXh0xmNjK9a3w-O4rV3q8X1cDyPTfLnOwaSrgOLTycXmMhQeqSlxMDUvAH9jrtJ3cNCZiM6xCVz-wSx7APpI9KXXeptY_tb7rHNmpZBSKXF03nwVtplwgIvZYi8m41127AUcCj6xydswY5Bt_HhULOQdY9TpsQxm12w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
بازی های دوستانه
امروز
فوتبال جهان
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
⚽️
🔥
💵
امکان شارژ با همه
ارزهای دیجیتال
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🇮🇷
پشتیبانی از زبان فارسی
↗️
حرفه ای، مطمئن و در کلاس جهانی پیش بینی کنید!
🔔
آموزش ثبت نام، واریز و برداشت
💛
لینک جدید و بدون فیلتر ملبت (فیلترشکن خاموش)
⬇️
🌐
www.Melbet.com
🌐
www.Melbet.com</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/136602" target="_blank">📅 20:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136601">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✅
✅
امیرحسین محمودی در فصل آینده با شماره 10 برای پرسپولیس به میدون خواهد رفت. شماره ای که سالها بر تن بزرگی همچون علی آقا دایی بوده
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/136601" target="_blank">📅 17:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136600">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LY8sIYxgJIJ_JTs4pfR8dKmyWc_zojc7STK6l7GBofK43CXFbIntUaIzYxG95nArMhOWbzQTKh_VTxFtBIR5LjB4R2EkCTXGvqiO3QN0c6ikH-dDUVSViEnyYTIsN0yGUhil7dGMDZjKobhV8Sw2_TRxgXn3oZxEd3AS-Otd9ZypAoXrBi1xvfayN6EDZumrdsFLyrHeyHAbPdorTvyz2l-hXxmqySRxRz5peF65-RwHZNi425W-H2HMoTYaGCo7jSaNJRxYGqarPi8iesvGF7CYiooGOAVL7b5rltFQo965Umpt64ra-VJkb14IqwTX6hRCuTmB9gA03pmeBEBOeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خواکین گیل دستیار سابق کالدرون در پرسپولیس قرار است به عضویت کادرفنی استقلال و به عنوان دستیار سهراب بختیاری‌زاده انتخاب شود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/136600" target="_blank">📅 17:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136599">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">⚠️
⚠️
تیم فوتبال پرسپولیس در اردوی ترکیه با فنرباغچه که هدایت آن برعهده اسماعیل کارتال است، یک دوستانه بازی برگزار خواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/136599" target="_blank">📅 17:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136598">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
تایم و رقبای سه دیدار دوستانه پرسپولیس در اردوی ترکیه مشخص شد.
❌
سرخپوشان در تایم های 8،4 و11 مرداد ماه با  تیم‌های «پیرامید»، «آنالیا اسپورت» و یک تیم دیگر به رقابت می‌پردازد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/136598" target="_blank">📅 17:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136597">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
فخر فوتبال ایران، چشم و چراغ باشگاه پرسپولیس؛ بازیکنی که همیشه پیام‌آور افتخار و موفقیت برای ایران در عرصه جهانی بود
❌
اسطوره محبوب و محترم پرسپولیس، تولدت مبارک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/136597" target="_blank">📅 17:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136596">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✅
✅
زارع و شهرآبادی دوباره در ترکیه؛ استراحت دو روزه برای سرخپوشان
⏺
مهدی تارتار امروز را به شاگردانش استراحت داده و فردا نیز سرخپوشان خود را برای سفر به ارزروم ترکیه آماده خواهند کرد. در واقع فردا عصر کاروان پرسپولیس عازم این سفر خواهد شد و 10 روزی را در آنجا…</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/136596" target="_blank">📅 17:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136595">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
فرهیختگان: محمد‌مهدی محبی در لیست مازاد اتحاد الکلبا قرار گرفته و باشگاه اماراتی پولی بابت رضایت نامه محبی نمیخواد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/136595" target="_blank">📅 17:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136594">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری از تسنیم
🔴
استعلام باشگاه پرسپولیس از فیفا رسید و هیچ مشکلی برای جذب دانیال ایری و کسری طاهری وجود نداره و این بازیکنان ظرف امروز و فردا قرارداد شون رو با پرسپولیس امضا خواهند کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/136594" target="_blank">📅 17:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136593">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">جالب اینه تموم فرم ها رایگانه، حتما عضو شین و‌ چک کنید چقد راحت سود میشه کرد
😉
✅
JOIN JOIN JOIN
JOIN JOIN JOIN</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/136593" target="_blank">📅 16:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136592">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2f7xBRNdQ961VYbJhd4eivWZ4Pvw_X1-gA-hFrT8PvX7FhLuaUrkBcQhXq0teK3jSnAVAfiu_c2C9WNMO8VW-rEasGICXJq4hp3GNE6xNaEUdCqCxo9GtuLUJFY68AlnpgRkcuDmyYInBg-B-30sjYvpcuZ4GP-p2vOQuIB5yvxonuFpVgVgXPK55hBIhoCQ9AIidjMz5waXqt2cwfK96zxxhb_WL6iI7ehtazGxU-0bSI3ts8KKcWTX84XTgblh5G_28a4NfLDrx6VINno1D3WJd61ZzN_S09XOdEi2DnVhJzMEI_fBpdGE1sedCVZHc9oidNpTPx6UBLByX96zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب حتی با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
میگی ن ؟ بیا تو چنلمون و ببین
🤷‍♂️
@PeakyBetBlinders
@PeakyBetBlinders
@PeakyBetBlinders</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/136592" target="_blank">📅 16:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136591">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
ایشونم از روستوف‌ روسیه جدا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/136591" target="_blank">📅 15:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136590">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bkwo6LwJj3lIGbCbgBk0zaWaC6gmjlgMrfNnhhPbssFpqInuT-tWw_uKd2MRUyUMFy6iVi6yx4BUlQlonzTBKLCNS8tSTumockmUWZrGWew5RdpQnAPJrE6PxPCYVtHQeD7NrBEPCGtJ-euTDQ4FGbjIHKgrZO4R_sYcldnnjuhZG3iBtF1a_x7B8Ij2VeCs481nll2EKS2WCESjgvhIj7tnLPzZ22qGpngahQE0tFqKsD97fci-Kq-elviqWAtQz9TDHKuk_Zycgsyzl-Q7_yQhiTV4hoMojev4yxkPNHt787yw_AZXueehV7t1xrSXzUhW6-G52JApEhCu60Y-Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ایشونم از روستوف‌ روسیه جدا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/SorkhTimes/136590" target="_blank">📅 15:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136589">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🔴
طبق قول و قرارهای انجام شده پوریا لطیفی‌فر، حدود ساعت 15امروز برای عقد قرارداد به باشگاه پرسپولیس خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/SorkhTimes/136589" target="_blank">📅 14:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136588">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❗️
❗️
درویشی وکیل ورزشی :از نظر حقوقی انتقال کسری و ایری از نساجی به پرسپولیس خطرناک و ریسک بالایی داره..
🤔
امیدوارم مدیران استعلامات کافی و گرفته باشن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/SorkhTimes/136588" target="_blank">📅 13:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136587">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
با اعلام ترانسفر مارکت رامین رضاییان بازیکن آزاد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/SorkhTimes/136587" target="_blank">📅 13:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136586">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✅
✅
پیام گلر یک پرسپولیس و ۹۹درصد گلر یک ایران در جام ملت‌ها است. برای چی باید اخباری جذب بشه که خودش رو در سطح گلر یک می‌دونه؟ که چی بشه؟
❌
❌
ضمن اینکه امیر رفیعی هم گلر مطمئنیه. چرا باید الکی چالش درست کنیم توی پستی که اصلا مشکل نداریم!!! به فرض جدایی رفیعی…</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/SorkhTimes/136586" target="_blank">📅 12:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136585">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❗️
پرسپولیسی‌ها نخستین جلسه تمرینی خود در اردوی ارزروم را در سالن وزنه‌ پیگیری کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/SorkhTimes/136585" target="_blank">📅 12:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136584">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✅
✅
محمدامین کاظمیان بخشی از قرارداد توافق پرسپولیس با گلگهر برای جذب پوریا لطیفی فر می‌باشد
🔹
محمدامین کاظمیان + حدود ۸۰ میلیارد رضایت نامه = پوریا لطیفی فر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/SorkhTimes/136584" target="_blank">📅 12:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136583">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
شنیده ها:قرار بود دیشب از پوریا لطیفی فر رونمایی بشه ولی به خاطر بازی تدارکاتی گل‌گهر، جلسه لغو شد و به امروز موکول شد
🔴
امروز به احتمال خیلی زیاد، پوریا لطیفی فر پرسپولیسی میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/SorkhTimes/136583" target="_blank">📅 12:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136582">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🌀
🌀
امیررضا رفیعی این امکان را داشت که قراردادش را به‌صورت یک‌طرفه با پرسپولیس فسخ کند، اما فعلاً این کار را انجام نداده و منتظر است تا باشگاه ابتدا گلر جدید جذب کند و سپس از جمع سرخ‌پوشان جدا شود.
⏱️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/SorkhTimes/136582" target="_blank">📅 11:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136581">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LT9xugnuK2P4-3VMi8yPFusSbTlRhL8W5j6kvlf1cXtQKggDpaQmLtkv76JDGE-bHvZ4jwy182pFE1JhNGcqienHktyn-HOLCWdJbCxyDn1EKIEZMwHsrX8fJREDxuLZFlPH2EHzLBp0Mt8GtwG0VL3SDgzg0FY5_JkzAv7WTZvaINJeoa0YUilIsB1TcVGopMTGgGtPCLxtjZvPW3m7NbPITGcB9K5GtTTBFIlvyNp0Wo6-4qHJiY0W9SRfynDkKBi_4sd1Nm5G1B2swx81hfLwLh91iPH0E0Qf5ic7Ywbn4bPmqZWUwnwngEHfgt4nfVPtghBptB1Yw284XuJXJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سؤال بزرگ؛ ثبات یا آزمون و خطا
✅
❌
🚨
درویش تو سه پنجره نقل و انتقالاتی آخرش ۱۷ خرید برای پرسپولیس انجام داده که ۱۱ نفر از اونا از پرسپولیس جدا و افرادی مثل بیفوما و کاظمیان هم در لیست خروج قرار دارند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/SorkhTimes/136581" target="_blank">📅 11:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136580">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/136580" target="_blank">📅 11:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136579">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❗️
❗️
هنوز قرارداد اخباری، ایری و طاهری امضا نشده/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/SorkhTimes/136579" target="_blank">📅 11:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136578">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/SorkhTimes/136578" target="_blank">📅 10:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136577">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/SorkhTimes/136577" target="_blank">📅 10:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136576">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUORmTS5YhmuUlk5AdKybF_Mfs25d6cAuO7d5adUn6ZRj_blcVnTszr0GRajwxxEWdN194CRKA3MDIXFQg9C2o18_raqaNL7tpnC-pd0jKgXtOPAJMSy55CQOlKzZnCv8ZMfd2SMgtCCEItmC3qgKVZ4_MFRnPszStfBW_R4U0EF_63cnnLkJExpok-iRk8ggRiJOnU-pb-6rjIHrY7z0b217jgUsf0ooOdcJV98Tp6IDJDhZxt53iFYwRqt_z-uQSt5tXyjRaq1bMw6JYPCG7RHhmZ-1G7fcgBPE9rzkQvdYDOKrZ1Js_SRuvZNDUc4GfBM9o2TV3JhggDmvmS48g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
با اعلام ترانسفر مارکت رامین رضاییان بازیکن آزاد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SorkhTimes/136576" target="_blank">📅 10:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136575">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✅
فورییییی از رسانه برزیلی UOL: جنگ بین آمریکا و ایران مستقیما تو این انتخاب نقش داشته و ترامپ در انتخاب داور فینال جام جهانی دخالت کرده
❗️
رابطه نزدیک اینفانتینو با ترامپ هم به عدم انتخاب فغانی کمک زیادی کرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/136575" target="_blank">📅 10:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136574">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kugHq946-Yr1_hzhoq0RS9_c9ILuR9lQYL7jcVB8K5fzteg5YTgr-HnQf01RWyRJwU1auxuwPz5b4T6T5wP2TzrXoT37GOLuhlA-Q4wWETppiGK6bzZrSa4PMCSnMJ4s39K0L2bDLWJ3rPHoEh9JrhqNcy7R6qHCLR0jZE71stJkQZ7D8AHJNMdBvmJxQ2M5U8KsMDtuYKaNElmkyHM4GrpoTmiIod3nZf0Zjbx6SDnDyFKOaq1V4juBGzbDfevcdql03bOpAO_og9A1MuWviof6HuELH_pXENVMxTpf0YsuIgWyHyVlH7aB8bxYBnG9KzHu7Dp_DsGymh9QokcMYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی‌تارتار در گفتگو با پیمان حدادی از وی خواسته که هیچ‌پیشنهاد خارجی را برای اورونوف بررسی نکند چون این بازیکن اصلا فروشی نیست و فصل‌آینده ستون اصلی ترکیب تارتار خواهد بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/136574" target="_blank">📅 10:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136573">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🫥
🫥
شایعات: محمد قربانی در لیست مازاد الوحده‌ امارات قرار گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/136573" target="_blank">📅 08:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136572">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فوووووووووووووری از هفت ورزشی
🚨
مذاکرات پرسپولیس با پوریا لطیفی فر، هافبک ۲۲ ساله فصل گذشته گل گهر مثبت پیش رفته و اگر اتفاق خاصی رخ ندهد، لطیفی فر هفته آینده بعد از امضای قرارداد با پرسپولیس راهی ترکیه خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/136572" target="_blank">📅 08:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136571">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/136571" target="_blank">📅 08:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136570">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136570" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/SorkhTimes/136570" target="_blank">📅 01:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136569">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSP2x-Xc0DqNp-aMSuGwBB5XVEdeXatiqSngFpaTbL1RyQjRGZYKoBrS-ShGeRH0Qmw_m1KJyDyqG3JQYhTEFhV-yFSu0uq2b6UyfSEroNQ88Q-z0Hanm7GadX6R3W8C1JyrVzKMCwUME9GhVMqStUl0PqdV-K_6KdNReWIXq0sqEGJFQft7aIoV0xTxf6PUs06sjSijTjpHpRijKbi91UNjO2irIf2tvy5rwDg1fYe0lW5hinrIiNgtzUkfBwbzMDSaF47X9sa-Gevxa_nuirIFVFejc18u2NxxY4qhlhyF4lpiOL0YRu2NOpmWMw_9WFtO7hne53eQnLXKPT55tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هر
چهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
Ⓜ️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/SorkhTimes/136569" target="_blank">📅 01:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136568">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
🔴
فووووری از تسنیم
✅
مشکل سربازی بیرانوند دیگ قابل حل نیست و امسال یا باید بره ملوان یا فجر سپاسی
😂
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/SorkhTimes/136568" target="_blank">📅 00:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136567">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/SorkhTimes/136567" target="_blank">📅 00:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136566">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">💢
کاظمیان + رفیعی میرن گل‌گهر پوریا لطیفی فر میاد پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/SorkhTimes/136566" target="_blank">📅 23:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136565">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
شوک به استقلال: آسانی فسخ کرد!
🔴
یاسر آسانی با ارسال نامه‌ای رسمی به باشگاه استقلال، به دلیل پرداخت نشدن مطالبات فصل گذشته و پیش‌پرداخت قرارداد فصل جدید، فسخ یک‌طرفه قرارداد خود را اعلام کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس …</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/SorkhTimes/136565" target="_blank">📅 23:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136564">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❗️
❗️
زارع به اردوی پرسپولیس اضافه شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/SorkhTimes/136564" target="_blank">📅 23:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136563">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMkVJjsa0W9yY_TVlAuB-xE-RePwLQkMwvleiLQK1Sl0BFiwyM5PUPTg24En1q2HiPsulDS6PgZYsQbwZNMrsAy7IbO4jknad-bWvpi_GZUG4SIEOSnDPby0T_9aedm6hAKsMNbuIxTzAfr7cZpUQf-WHQf0bv822iPd2QXac5vvw_y3CoJPJ1ncQw1pmZ2-DVd66jBHIkKwzOUT-Nq40ZS1zdsZQyJrwHAWC_tLzl37mPOwQVjC-TEyOyXvcuf3QVyUfUvO1F65tZs6iGyCcIhJaF3hurBwQkJWrrj2hupnyWB4360d88SC2tjN5JLnPCGHebI7OUrNvpGB9cBhdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
پرسپولیسی‌ها نخستین جلسه تمرینی خود در اردوی ارزروم را در سالن وزنه‌ پیگیری کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/SorkhTimes/136563" target="_blank">📅 23:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136562">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✅
کاروان پرسپولیس دقایقی قبل وارد ارزروم ترکیه شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/SorkhTimes/136562" target="_blank">📅 23:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136561">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✅
✅
رضایتنامه‌ی قربانی خیلی سنگینه و کنسله/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/SorkhTimes/136561" target="_blank">📅 23:15 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
