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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 15:26:42</div>
<hr>

<div class="tg-post" id="msg-136659">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❌
پناه بگیرید
✅
میلاد زکی‌پور رسما از سپاهان جدا شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/SorkhTimes/136659" target="_blank">📅 14:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136658">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔹
نگاهی بندازیم به هایلایت‌ پوریا لطیفی‌فر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/SorkhTimes/136658" target="_blank">📅 14:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136657">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❗️
میلاد زکی پور، مدافع چپ سپاهان پس از قرار گرفتن در لیست خروج محرم نویدکیا، به پرسپولیس معرفی شده تا جانشین میلاد محمدی شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/SorkhTimes/136657" target="_blank">📅 14:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136656">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LqCvkpaBblfU4DArPj0JKSp1rNU6ZbIqKRjTco2IhvVOMl3EO5omk4uB0SJn2eNMN6Bqd85PQNxct9UuAkqcw0w9kMajRBYaGZmiEI2h6HjE1o5Dx5PkW5-ju-2IsnMoI-tSiw6Jsxy6EbJY70-niykfyRAIikCzdA0ZCJNjV7yzRZ-fUx39mdAvE9WAPgK52bWZ9vOP6QB61gM003p1pwRZya9qo4FWKVaJ-twsmEz92-pxQc8klpx51ki-FbbWLAAEQ3ELHgG8B5QELaQscs24V-0HeBX6o5RZSzMDRL2bI6N1fb3IlRLOiL4JQts-KrIN_xWjZeBJwiwFOIR0AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽
لطیفی فر با عقد قراردادی چهار ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/SorkhTimes/136656" target="_blank">📅 14:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136655">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVfCwqWDUk-IhYF6btoL5q1kM_jsbWd-1hrbQeVZpseIPiOWkWYU9gyZCzS5_rymqVR6XWldo7AHp0tKonKEuV4Lsj_KgiiOqUhOumhKfCOPdepqvAUo5TgVnF5PyrkbOpCMwb0desAQ1aEdM-kSXTKI3XWSJXzbpKBz42mgOqJsk3ck4XjsPStu_Ny-_ZUiHliiSCcRZ_B-a4lGzB_ogwr9rrg-z403rt4Dec5mxMjV_QZIkZKRVSBcgicdS8buwg31RMqfq_ohQQmsREGsfMVczdh6Iul9oRmXrhmxdia3VooY3lpOnoJb3NxTIRep3fiqsIOO5ORTBM2fZGft_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
۳ خرید ناب در راه پرسپولیس
💥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SorkhTimes/136655" target="_blank">📅 14:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136654">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SorkhTimes/136654" target="_blank">📅 14:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136653">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
پیروز قربانی: من نیوزلند رو با فجر سپاسی شیراز می‌بردم مطمئن باشید نیوزلند اگه تو لیگ 16 تیمی ما بود، جزو چهار تیم آخر میشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/136653" target="_blank">📅 13:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136652">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❗️
واکنش ابوالفضل رزاق‌پور به پیشنهاد پرسپولیس:
🔴
نامه رسمی به باشگاه فولاد آمده ولی من وظیفه دارم سر تمرین بیایم تا تکلیف مشخص شود. خودم با باشگاه هیچ حرفی نزدم و دو باشگاه باید باهم حرف بزنند.
🔴
🔴
حضورم در پرسپولیس برای دعوتم به تیم ملی تأثیر دارد ولی امیدوارم…</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/136652" target="_blank">📅 13:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136651">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❗️
مشکل سربازی فرهان جعفری حل بشه با قراردادی ۴ ساله پرسپولیسی میشه/طرفداری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/136651" target="_blank">📅 13:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136650">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">#تکمیلی
⚽
💥
حدادی منتظر پاسخ محمد مهدی محبی؛توافق با کلبا انجام شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/136650" target="_blank">📅 13:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136647">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
💣
One Signature. One Earthquake…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/136647" target="_blank">📅 13:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136646">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🤩
باشگاه پرسپولیس فردا در دیداری تدارکاتی به مصاف پیرامیدز مصر خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/136646" target="_blank">📅 13:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136645">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
⚽
لطیفی فر با عقد قراردادی چهار ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/136645" target="_blank">📅 13:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136644">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3UDQK0I6sTPVPUWm59XcMWoU68eI74VOKC0NibYSx_NC0rRE3_PT96c2gEbkeHdsnE4FuCmsBf4wYs9kvPDh0s0qEFOkC2y6HjCLA3Sb2TkFG8mA8cZ4Cn3t20wM1C4rkUd4U_UqHiPzpUP4bSingU64LSyVomct4DJeoY8J8vkmAFQhDLOSVFRxiNu1-f19iDryvNsJYtesdT85lFVTkHQWJEgcYq3QJtDmkMsqLMZNft27hfNwvqLO1sYl5qdd1281sQgjfpWUNEZI17To8syheIxPM6-KrxN0gfTs4vyqLup0Ll0huujfrtAtkcFiy02DFr26HvHm2wdpGYbAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽
لطیفی فر با عقد قراردادی چهار ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/136644" target="_blank">📅 13:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136642">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/136642" target="_blank">📅 12:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136641">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/136641" target="_blank">📅 12:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136640">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
❌
امروز تکلیف نهایی دانیال ایری و کسری طاهری برای پیوستن به پرسپولیس مشخص خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/136640" target="_blank">📅 11:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136639">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
❌
بعد از 13 شب .دیشب و بامداد امروز هیچ حمله ای به ایران و نقاط ایران از جمله جنوب نشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/136639" target="_blank">📅 11:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136638">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/136638" target="_blank">📅 11:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136637">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✅
برخلاف شایعات ؛ حضور براجعه در تصاویر اولین تمرین پرسپولیس در ترکیه
❌
در حالی برخی منابع از عدم حضور براجعه در اردوی ترکیه پرسپولیس خبر داده اند که این باریکن در تصاویر اولین تمرین سرخپوشان در ترکیه حضور دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/136637" target="_blank">📅 11:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136636">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❗️
🚨
🚨
باشگاه پرسپولیس با باشگاه اتحاد الکبا برای انتقال محمدمهدی محبی به توافق رسید  #قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/136636" target="_blank">📅 09:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136635">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3U2yueN1j97H25XvK0y0lwjSQk7kHh2MDbjWnRE6XDomhMawvqx_cQ6yB_XMiHph0dzs4dWAA3_9FztvSQ3T9481W-eiML_hTDAHKFoGH44Kb94CJV0Lq6_I6PlBj6A2S53a3RVL2n_iP7DbCG_-e72f1-8x50hF1J_BJ-O0v3leVRrr2RYYMzaW4HNy_sBxW_V_Uy8aU9z21G1SiTeG5WGCm6-sctLAq8pUHGHJkhWZ7xG_scWFve0fjzR9o7hk6upfpyFZ_iJyH0TkmB58_yKuxTcV966HTrzZ1GwQ0JXfEc1hZkWZYMzg_2ykeHmZzfo7p0ve_9JW2EpzPRhAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف شایعات ؛ حضور براجعه در تصاویر اولین تمرین پرسپولیس در ترکیه
❌
در حالی برخی منابع از عدم حضور براجعه در اردوی ترکیه پرسپولیس خبر داده اند که این باریکن در تصاویر اولین تمرین سرخپوشان در ترکیه حضور دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/136635" target="_blank">📅 09:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136634">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❗️
🚨
🚨
باشگاه پرسپولیس با باشگاه اتحاد الکبا برای انتقال محمدمهدی محبی به توافق رسید  #قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/136634" target="_blank">📅 09:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136633">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✅
✅
محمد مهدی محبی تمایلی ندارد قرارداد یک میلیون و ۴۰۰ هزار دلاری خود با باشگاه کلبا را از دست بدهد. باشگاه کلبا نیز قصدی برای ادامه همکاری با او ندارد، اما خود بازیکن حاضر به کوتاه آمدن نیست. با این حال، پرسپولیس هنوز از جذب او ناامید نشده است.///قدوسی
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/136633" target="_blank">📅 09:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136632">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/136632" target="_blank">📅 08:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136631">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">⚠️
باشگاه پرسپولیس هنوز با مرتضی پورعلی گنجی برای فسخ قرارداد این بازیکن به توافق نرسیده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/136631" target="_blank">📅 08:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136630">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
❌
بعد از 13 شب .دیشب و بامداد امروز هیچ حمله ای به ایران و نقاط ایران از جمله جنوب نشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/136630" target="_blank">📅 08:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136629">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✅
✅
#تکمیلی | رویترز:
🔴
ترامپ دستور حمله قدرتمند به ایران را صادر کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/136629" target="_blank">📅 08:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136628">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDcqw0plMIUXmiIKasEOGjxnYrHFKJ3Suni1bBVs7EhcOuKkv9x2It-EF5Zc03tloEbkD3rPaPDWuzc5sR0-iFTrSKBeZXqgvXWIKo4e6TRVOlMBTGZ6hgxK5laGKMBNH8yCIVSPLThwTx3SXbrnNARg3sS1fI9jt964fJFPmV7SakQJ1_XwmcHc7o_qYWRBEWd1zB7rYsg0M3Rz0TOWXF-hkacI2wFpqUvPV7OHwWNpDyNzjSYY33SOT48BHXLnn4TJjeIWzEq6jN5QT928YtanatmevHUkvXqE_XhVoIkocHOp_hgltiN6yl4GhhTw-nzS6r6onR837yHMVPQ4og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/136628" target="_blank">📅 08:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136627">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/136627" target="_blank">📅 01:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136626">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6J34le3UL1fl_Qi63AGY0D_-kI2llk3CWWo8JzQLwb8czdc5B-ABT-mSSRV6r56WuaDVf1bHvQw8efPA12DPtwdxmJNaJ5r7jXKjkBFXUd73IAiOPtfkU_NXL-RNqLucyrkcUy2Z-W1zNYu6lXRfwZRjn3RKw53_MAZ2Uv3MKFRCPtKIQUaM4Lc_mm3EpmwN6L016rkSKe4dGW1pMAlPKP60WnHmu_dhAf0JF1X-pxHQy_V8k2Dpmm_UFn_mZLJWI3yy51dNPsW94Rgi6gYcK1c9CHk3UWEY1wFLkgFgTpBLNHC79E9NMg5Mtx1oQ3vX6rEg1yRstVSj3fBt9crCQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/136626" target="_blank">📅 01:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136621">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCPZT03WPNB8C3UG_OvFh0oECRJ0BYL70R22s3R9PIqOxStyZygvJSd3XdBgZ1ykDC8YfoZGw_uWm1mzz-m9rKT5hBQ0k1u-L-_wfbReDg9b1wjfe1MsL1-PuhfBK1_hWe4OR58THF_G0os0DCw0TT3y-QK_U8tIqQx5D9-ZGqXiLX6E8dbCwU0O7RCtWpqOM1QFbll1glb7GEHc5ZJIaPs7VHdZ_wsEDsft2JrBnHQZnOgx6iShchc0b4OFHzW55hXkkEvnqe4-r497i_4qN7xCAYaVDo4Y-UIqrP_aU1SYDkkRdK8DuQ0uZ2bHTAH9lKfjK3ysD923LtJZP2EqpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/136621" target="_blank">📅 00:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136620">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔹
دونالد ترامپ: با وجود اینکه درحال گفتگو با ایران هستیم اما باید بگویم که مهمات ما برای یک حمله وحشتناک به ایران تکمیل شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/136620" target="_blank">📅 23:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136619">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
❌
#فوری |ترامپ به شبکه 12 اسرائیل: من در حال بررسی امکان انجام حمله‌ای بزرگ‌تر از هر چیزی که در گذشته شاهد بوده‌ایم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/136619" target="_blank">📅 23:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136618">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✅
✅
تارتار دنبال جذب یک وینگر دیگه‌ست؛ بین گزینه‌ها فعلاً فقط با محمدمهدی محبی مذاکره می‌شه. برای همین هم بیفوما رو به اردوی ترکیه برده تا اگر وینگر جدیدی جذب نشد، ازش استفاده کنه.
❌
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/136618" target="_blank">📅 23:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136617">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
❌
تقویت پست وینگر و جذب محبی از کلبا تازه ترین هدف و تصمیم نقل و انتقالاتی تارتار است.
❌
محبی که مربی کلبا روی بازیکن خارجی دیگری به جای او حساب کرده نمی خواهد قرارداد یک میلیون و ۴۰۰ هزار دلاری اش را از دست دهد. باشگاه پرسپولیس امیدوار است محبی نرمش نشان…</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/136617" target="_blank">📅 23:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136616">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
فوری، حمید مطهری با جدایی ابوالفضل رزاق پور، مدافع چپ فولاد خوزستان و پیوستن این بازیکن به پرسپولیس مخالفت کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/136616" target="_blank">📅 22:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136615">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✅
معامله گری که سرباز شده و برای دفاع چپ فقط ی جلالی و داریم و خلاص که اونم مصدوم شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/136615" target="_blank">📅 22:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136614">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/136614" target="_blank">📅 22:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136613">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
پرسپولیسی‌ها عصر امروز تمرینات خود را در حالی پیگیری کردند که پیام نیازمند و محمدحسین کنعانی‌زادگان پس از حضور در جام جهانی ۲۰۲۶ به تمرینات تیم اضافه شدند و کریم باقری نیز در جمع اعضای کادر فنی حضور یافت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/136613" target="_blank">📅 22:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136612">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
باشگاه اتاق محمدرضا اخباری را در ترکیه رزور کرد و هم اتاقی کاپیتان تیم حسین کنعانی خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/136612" target="_blank">📅 22:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136611">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XN6BMeePVclhSWd_EJ9UiHdlGvJ1iV6jfNmNgEqzyFL57BmouFWTHCImNLeWHsMtN58YEH5BT2wlcQJyYb5tSqbv4E7LdZuYGUd3YNDOvHQ8KkOOyL-jbnRdm-dJyEWVh0ftrwnj89-Y1tXvwHLvHatSBZ2azQ9goSL23NLmihVNRph35EROv06HiCnbF-9BoNQKFwNsaLTTvk1bjk1BZMZuebFLUhoVm9UlNAprI8DkjaoOd9Nd6p9f2mSCCx4c18_WdR4g50Vn_1gtpqAnk5FRRe-hu0vvrJkWDq3UkYx_OPv2p3iaKyUk9f_E69tGhJjpKSvQZC-Qwq3qCcUVTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
حضور و اولین تمرین پوریا شهرآبادی و محمدمهدی زارع با لباس پرسپولیس.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/136611" target="_blank">📅 22:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136610">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
❌
مهدی تیکدری وارث شماره 8 پرسپولیس در فصل جدید خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/136610" target="_blank">📅 22:13 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136609">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBEl5gJEMOebpUR0arQ3klhYiX_N84i0qHGZWXNCfQeQJSR5h5q8IiSek_0ce2KZjNZycMQRl5LA46niXuCRZtrnPcqGShUnKN_vkdR6Yw2U6ZtvP3ReYuTB6PDjwm3yRqdWCVog0C9kUisZNuZKwVjpR5o27vAHOBmwBsD660d943d8cXOpwQGCUP5ng59ayAPjLL6Wh1Fi6x5hAznJkHeFDdZce-R0Mk1ki5QouKkv4uOJQ_J9niIJVuCwsoVbrgiv2HY-NyCIuakajSJYqhw85bWNNiy4OGHMJkUv1BSK1teXVDvFkNfsOLbYZOrjWdNMKlnQ2kw4tOk6YNrkvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوری
؛متاسفانه‌خبررسید اکبرعبدی بازیگر سینما و تلویزیون دقایقی قبل در سن 66 سالگی درگذشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/136609" target="_blank">📅 21:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136608">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🌀
🌀
هیات‌مدیره پرسپولیس فردا درباره جذب کسری طاهری و دانیال ایری تصمیم می‌گیره؛ با توجه به استعلام‌های مثبت، احتمال نهایی شدن قرارداد این دو بازیکن زیاده.  قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/136608" target="_blank">📅 20:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136607">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✅
✅
فرهان جعفری در یک‌ قدمی‌ پرسپولیس/طرفداری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/136607" target="_blank">📅 20:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136606">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">⚠️
باشگاه پرسپولیس هنوز با مرتضی پورعلی گنجی برای فسخ قرارداد این بازیکن به توافق نرسیده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/136606" target="_blank">📅 20:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136605">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/136605" target="_blank">📅 20:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136604">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZA2nlPCKJ5JoHL3576NW4Nv3mHamU0LbHdkvpKrenRtdz3cav5Zv3_m0pQ3AAb9LPf-V_mX9aftHiYPL-JoIIEMB9pBXH39mAgZ78hMRPVE0m_I-T1xq3mWtODXgDUiWERaU8G5pDuhLS4wrs_wCjXvlctihRh5PbUfsQFX0fNtIDKnmDKF5mZb13DVvFBS8-zzfx3ojfNcoCU73skUribqiHGPolDBKM_rO4E5hlXbgYQp9unw878Qtnzg7T-uVche_IxSSU3D_oP75duVbhXeTo7ULrIvS3PWohtAO6jP3Fz3r4syKysWw-797VpaH96gEtJ8cYanH_X8eyRw7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رسمی؛ رسول خطیبی سرمربی فجرسپاسی شیراز شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/136604" target="_blank">📅 20:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136603">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/136603" target="_blank">📅 20:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136602">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqUoGygm_ShJEDgmgpEfcdMF3nYjGzQcEvVn0ThSSY_USKbuAABJUDgOwYZZoDDz0hf4EA9fge4otsroIswQWzL4r8yx5savsigjVXrWDUN5-aC9g9ByJCc_EFAJZNVlP8vDTajQdKbd5fPzjKrqsimIX8yWie2tgROzKWY70dgZADSvBtfKkiFKuZUY9GhbX704WUnQGIcgViDIaJVZGF9iTyWSvfA67FMdN2NxeMy0r_YknZ5-rfbo9dG1zuIeo9xuVJKnMBwjaJWSV52dRQFJx6ZE16iuZGLFA_x1mqOQfCiFNxB3XRt7wvg65w40CiMp_oYtwzA-H7N3HxsaQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/136602" target="_blank">📅 20:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136601">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✅
✅
امیرحسین محمودی در فصل آینده با شماره 10 برای پرسپولیس به میدون خواهد رفت. شماره ای که سالها بر تن بزرگی همچون علی آقا دایی بوده
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/136601" target="_blank">📅 17:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136600">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TB2dfTyDQn9CUP4oVcnocYjjAL_8OKp1oVZ7sW8S2dmJ0u37s_KwFX32ar8lz8mNvk67OAuWcYh5jd1cepkr35lZ_JJXyG92Zuhg0bUnKekVqRBX1wrQ4adS5zCjTc0u_X-XSv0ujl6RanjXccm-N53d5yYQzuZCc7NUEpi2dgqw82le-qhtNZtvZ4TmmZB7Qbc1JJFf6-jd8dU0p1pO5y5quE7q2WR0AKQpyDCA6GPNssJJ1cgBWfBqrbLzx4bHI_U36aR0rD6Ac_CK564Mn1T87nFULmOvnpxSqIWLRmziNPOsEZSyDAXQzWZn4lco7Zuv4xK7l_mROGIbJg79pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خواکین گیل دستیار سابق کالدرون در پرسپولیس قرار است به عضویت کادرفنی استقلال و به عنوان دستیار سهراب بختیاری‌زاده انتخاب شود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/136600" target="_blank">📅 17:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136599">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">⚠️
⚠️
تیم فوتبال پرسپولیس در اردوی ترکیه با فنرباغچه که هدایت آن برعهده اسماعیل کارتال است، یک دوستانه بازی برگزار خواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/136599" target="_blank">📅 17:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136598">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
تایم و رقبای سه دیدار دوستانه پرسپولیس در اردوی ترکیه مشخص شد.
❌
سرخپوشان در تایم های 8،4 و11 مرداد ماه با  تیم‌های «پیرامید»، «آنالیا اسپورت» و یک تیم دیگر به رقابت می‌پردازد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/136598" target="_blank">📅 17:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136597">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
فخر فوتبال ایران، چشم و چراغ باشگاه پرسپولیس؛ بازیکنی که همیشه پیام‌آور افتخار و موفقیت برای ایران در عرصه جهانی بود
❌
اسطوره محبوب و محترم پرسپولیس، تولدت مبارک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/136597" target="_blank">📅 17:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136596">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✅
✅
زارع و شهرآبادی دوباره در ترکیه؛ استراحت دو روزه برای سرخپوشان
⏺
مهدی تارتار امروز را به شاگردانش استراحت داده و فردا نیز سرخپوشان خود را برای سفر به ارزروم ترکیه آماده خواهند کرد. در واقع فردا عصر کاروان پرسپولیس عازم این سفر خواهد شد و 10 روزی را در آنجا…</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/136596" target="_blank">📅 17:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136595">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
فرهیختگان: محمد‌مهدی محبی در لیست مازاد اتحاد الکلبا قرار گرفته و باشگاه اماراتی پولی بابت رضایت نامه محبی نمیخواد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/136595" target="_blank">📅 17:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136594">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری از تسنیم
🔴
استعلام باشگاه پرسپولیس از فیفا رسید و هیچ مشکلی برای جذب دانیال ایری و کسری طاهری وجود نداره و این بازیکنان ظرف امروز و فردا قرارداد شون رو با پرسپولیس امضا خواهند کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/136594" target="_blank">📅 17:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136593">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">جالب اینه تموم فرم ها رایگانه، حتما عضو شین و‌ چک کنید چقد راحت سود میشه کرد
😉
✅
JOIN JOIN JOIN
JOIN JOIN JOIN</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/136593" target="_blank">📅 16:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136592">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcApaVKjmsfeNaF5JFzw0ytuFcgvTx-jq8MIeeXQellyZrdkwEUgZvU0ZRM-ikmLCnbvY9Enw_UlYfxnbwdTA5jkVoYLhYzuCyF0TIvGiv_LlDfBDMHkXHbwVXO1ARNAjaFBFdNNccfeTz3UeI7EkiHrlspq698A8QKJ0FDYEw84n8wH5Jvdk2OcOqKbx858QIadfZfEnqB6DGImfu7ZIV9oMLlGDIF1zVYmd0KGhyRqGnu7Kno9_UPRjhYpnHcttz_HGb5uzpr7jUaZYQPtlCA-IE_53Hj6m6-OlIFYEPfvTBiIwksjIRmKlGrDHYdcdizdLneJvqVR3JKDl9lYuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب حتی با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
میگی ن ؟ بیا تو چنلمون و ببین
🤷‍♂️
@PeakyBetBlinders
@PeakyBetBlinders
@PeakyBetBlinders</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/136592" target="_blank">📅 16:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136591">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
ایشونم از روستوف‌ روسیه جدا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/136591" target="_blank">📅 15:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136590">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMjvXd_aJa8eGtjp0sgASiGVDZoosq-OZETdOdzVlbW9LInAUXP33Jy8SlwUgjhAydidUML3ITMVPk8QaTrYdzzSNkJMWh00WgDe7Jvgvm6qhNmtiVZdWdRotfEQyol6C9TaZ9fQdlEC0HiuwPqPYnsdpha19ELQp9YFsYYUSXu2FRXN6cyUUu_hGMLfvxvYEjgVTst2rGSFRRte4kNQ370bgUYKr8ty4aac9rbM55EIYMmyzE7Ao_A53QSiMutYL00aG0PMgWmsgVlbYgbJz4-4jHhtt1SJUMF2YLpmipQKQgLG8rOPCw-sJE_Sa6DXG6rvVVNBcJT374IDEDnktg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ایشونم از روستوف‌ روسیه جدا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/SorkhTimes/136590" target="_blank">📅 15:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136589">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/SorkhTimes/136589" target="_blank">📅 14:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136588">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❗️
❗️
درویشی وکیل ورزشی :از نظر حقوقی انتقال کسری و ایری از نساجی به پرسپولیس خطرناک و ریسک بالایی داره..
🤔
امیدوارم مدیران استعلامات کافی و گرفته باشن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/SorkhTimes/136588" target="_blank">📅 13:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136587">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
با اعلام ترانسفر مارکت رامین رضاییان بازیکن آزاد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/SorkhTimes/136587" target="_blank">📅 13:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136586">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✅
✅
پیام گلر یک پرسپولیس و ۹۹درصد گلر یک ایران در جام ملت‌ها است. برای چی باید اخباری جذب بشه که خودش رو در سطح گلر یک می‌دونه؟ که چی بشه؟
❌
❌
ضمن اینکه امیر رفیعی هم گلر مطمئنیه. چرا باید الکی چالش درست کنیم توی پستی که اصلا مشکل نداریم!!! به فرض جدایی رفیعی…</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/SorkhTimes/136586" target="_blank">📅 12:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136585">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❗️
پرسپولیسی‌ها نخستین جلسه تمرینی خود در اردوی ارزروم را در سالن وزنه‌ پیگیری کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/SorkhTimes/136585" target="_blank">📅 12:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136584">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✅
✅
محمدامین کاظمیان بخشی از قرارداد توافق پرسپولیس با گلگهر برای جذب پوریا لطیفی فر می‌باشد
🔹
محمدامین کاظمیان + حدود ۸۰ میلیارد رضایت نامه = پوریا لطیفی فر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/SorkhTimes/136584" target="_blank">📅 12:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136583">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
شنیده ها:قرار بود دیشب از پوریا لطیفی فر رونمایی بشه ولی به خاطر بازی تدارکاتی گل‌گهر، جلسه لغو شد و به امروز موکول شد
🔴
امروز به احتمال خیلی زیاد، پوریا لطیفی فر پرسپولیسی میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/SorkhTimes/136583" target="_blank">📅 12:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136582">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🌀
🌀
امیررضا رفیعی این امکان را داشت که قراردادش را به‌صورت یک‌طرفه با پرسپولیس فسخ کند، اما فعلاً این کار را انجام نداده و منتظر است تا باشگاه ابتدا گلر جدید جذب کند و سپس از جمع سرخ‌پوشان جدا شود.
⏱️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/SorkhTimes/136582" target="_blank">📅 11:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136581">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxoufABejyVWvzLUNg4RFts2Sj3idZh0Bz2E43N2UKbJSTH_nuoAvyRwT4w-Z6UpzD1nFj7y_JD48R8r8iqA6J5MzjprjHs2xfk1ceh7S-VtbDIUPcIue9G5dWDk5FtbsOT1jmnx2b8KMaMZKu_Y38IQq1cMJ2Wzpur_KjRFQd0ubc_xVnSrhba1IMI8_ROckIQGXVcF-mbC10byReIap8ju8WxNoCjCF5LU0lS83SkXsOjgowjBPqYM6y_Xt-6SiiiKrVxZEfUu0VaTbFBfmUNkW7ZBMSlkKw0QIC4-oJABPrksNL-KFgmoVcBdGE4Buhv8CD4P57JcDSaJjcE3ZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❗️
❗️
هنوز قرارداد اخباری، ایری و طاهری امضا نشده/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/SorkhTimes/136579" target="_blank">📅 11:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136578">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/SorkhTimes/136578" target="_blank">📅 10:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136577">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qqc_WkK1Nwrajz_L9_VSmuYkLVitH1zj8yurmmtAZDI5z7tbxUFIPUDK5UscW4IiN6jguSJwZ5AfNF-BAdYBba3RRa-0W0w38Se8woP7ORS8_JtMjPLgpullhFOvngF1iFLe1A4uiIneqnXxk_bE4wrb3XwVLV7wpPvRhz_l895B1yPBTTx9CZuHPJ34yZwAkZXIvCGxoRoR3lb6vRHJstFQw82ifC9FQmSUl1L4sd6-NL52lEqJiCpZtTbuhbxDZwhoeYv4J79suEONNrRXzOCeRqqK5wOt7JYo0ckl6LRbjwpuecI3cJGpBv-3y8kmY0N7Tlp1kl21a5jpWBmm5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
با اعلام ترانسفر مارکت رامین رضاییان بازیکن آزاد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/136576" target="_blank">📅 10:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136575">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✅
فورییییی از رسانه برزیلی UOL: جنگ بین آمریکا و ایران مستقیما تو این انتخاب نقش داشته و ترامپ در انتخاب داور فینال جام جهانی دخالت کرده
❗️
رابطه نزدیک اینفانتینو با ترامپ هم به عدم انتخاب فغانی کمک زیادی کرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/136575" target="_blank">📅 10:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136574">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EE6VM9X0KJ8yk6Gc2NcATGoB_A63tsrMQK6f7VFBUOUEMiAMYNmqZDcR50XcK4xooaxBLvXhzjthqlBiESZOtZfjUVmpnmSukMkt8LzFVCFhSoDF5xv_cwsDKfeJwAQBOuEYHZPxNPAvWPc9BHVUFnh8HonJmNXhWJtk6pSOoYTf9wj5oEcDIVC8lXUAINbnK_AT7w56kP6qpVNhxDUTz4na4hqtSoR5hCsWGdYjrbnE7zwgJv-G7RAo4Z6xnzyfFgCILdHqOYbWP891efFQeiT1X3DYFDY31dwPDLzC6ZdEatTf_yignrCBAGWlmNrSKSRaRNXfEZg8K5qwi5oCkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی‌تارتار در گفتگو با پیمان حدادی از وی خواسته که هیچ‌پیشنهاد خارجی را برای اورونوف بررسی نکند چون این بازیکن اصلا فروشی نیست و فصل‌آینده ستون اصلی ترکیب تارتار خواهد بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/136574" target="_blank">📅 10:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136573">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🫥
🫥
شایعات: محمد قربانی در لیست مازاد الوحده‌ امارات قرار گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/136573" target="_blank">📅 08:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136572">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فوووووووووووووری از هفت ورزشی
🚨
مذاکرات پرسپولیس با پوریا لطیفی فر، هافبک ۲۲ ساله فصل گذشته گل گهر مثبت پیش رفته و اگر اتفاق خاصی رخ ندهد، لطیفی فر هفته آینده بعد از امضای قرارداد با پرسپولیس راهی ترکیه خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/136572" target="_blank">📅 08:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136571">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TuWtoiVBzXoQYL9VYUp4KLPS-jSCpnlISJ75VPD3lqmyp3fSyZT8kH36yV89JFQUhCPvJN3D76Fc_gS4VGyIlbJDU7JP4lNYDG1FXLYDsT5XSb5S3EYLav-eMMrvW5L3qmGp0tUZf0PYz0TLmGyJuvgcLbQ0BK-6iX0o76tmHyZhjM0QI4b7Wgy-iiBi0De2IhBspcKM9Q4Tu98_i40JAaPj9DTbyYxIIpUIt6_uAUFy1NiVuM5VjlLXfTgOvysG8-uU6s2v5y8gSXrOqcXeG8mW5z50DtAIrP0mt1xE9E_iq7DR6x0iXbwdJ7NmJM0g7mM0Gd63nO_yaMVLnjsOJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/SorkhTimes/136568" target="_blank">📅 00:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136567">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/SorkhTimes/136567" target="_blank">📅 00:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136566">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">💢
کاظمیان + رفیعی میرن گل‌گهر پوریا لطیفی فر میاد پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/SorkhTimes/136566" target="_blank">📅 23:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136565">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
شوک به استقلال: آسانی فسخ کرد!
🔴
یاسر آسانی با ارسال نامه‌ای رسمی به باشگاه استقلال، به دلیل پرداخت نشدن مطالبات فصل گذشته و پیش‌پرداخت قرارداد فصل جدید، فسخ یک‌طرفه قرارداد خود را اعلام کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس …</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/SorkhTimes/136565" target="_blank">📅 23:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136564">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❗️
❗️
زارع به اردوی پرسپولیس اضافه شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/SorkhTimes/136564" target="_blank">📅 23:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136563">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nI_v23IEsN-9V13wlwR5N-vJ7B5zvka7DBAW5cy6DrPdXODTJQZvg2G5GBODBuVviPB_Lswb3s7CKwXzZGtrvFnWZm3PPnBy105nSBVvy8zNFDyRmTy_s5qeP_WHB4Yygy6xxG6-uc7vAKzRwTHkmdn2EztdIVJguEbkHC1-F0rd7T1tDTxoTmrOQqy8DjagHyZa4uHrf5ZN5R765SD65O7ua7lAWV_f4ox2XP11cIN3BCe9UdJwNYDgxBDBa8-oSWdUANfqy6pSKh0CIYH_x0kwFJmMll-235aaNT8iwUqiJvPyy0gUJq_50aUGH41I7FvY9QnerpgJCeeL0ko8gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
پرسپولیسی‌ها نخستین جلسه تمرینی خود در اردوی ارزروم را در سالن وزنه‌ پیگیری کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/SorkhTimes/136563" target="_blank">📅 23:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136562">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✅
کاروان پرسپولیس دقایقی قبل وارد ارزروم ترکیه شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/SorkhTimes/136562" target="_blank">📅 23:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136561">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✅
✅
رضایتنامه‌ی قربانی خیلی سنگینه و کنسله/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/SorkhTimes/136561" target="_blank">📅 23:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136560">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
رفیعی خودش قراردادش رو با پرسپولیس فسخ کرده و حالا دستش بازه هر تیمی خواست بره. احتمالاً هم راهی گل‌گهر یا شمس‌آذر می‌شه و اخباری جاش به پرسپولیس میاد.
✅
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/SorkhTimes/136560" target="_blank">📅 22:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136559">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
❌
#فوری |ترامپ به شبکه 12 اسرائیل: من در حال بررسی امکان انجام حمله‌ای بزرگ‌تر از هر چیزی که در گذشته شاهد بوده‌ایم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/SorkhTimes/136559" target="_blank">📅 22:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136558">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
فوری از سپهر خرمی:
🚨
بعد از کنسل شدن تمام گزینه های پرسپولیس در پست هافبک دفاعی، مسئولان این تیم دوباره سراغ محمد قربانی رفته‌اند اما اینبار با پیشنهاد بهتر!
🚨
قربانی از تراکتور هم پیشنهاد خوبی دریافت کرده اما تمایل داره به پرسپولیس بیاد!
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/SorkhTimes/136558" target="_blank">📅 22:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136557">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/SorkhTimes/136557" target="_blank">📅 22:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136556">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fR-v-uNVyO1lq3_aQ3Zj3ln2MYpzbu8BAC0wTCId-mtA-bLuC3Y19dcQuAMYxQLpFdLUbuhW_kjoUExVvOA-9SvMuF3du_4jkd7WGLR4z0ocyWygI5fJ7NBikYHzPUmqZuvkvzzvxwvmZwlxYuERtZrjv5jcRw03ltg94Kd434zKx4Ez824mz7zYi0dfivIF--afyv29b0AR1qnk422Og194qEkiSYSmPAWpB8DYXT-DorwtFWxR6Hab1waTHhzcNofS-8c8wMjD7TQt_zJ291USkk_YBCj4IPgy6DLo0v7_tYjFGuMNMLIbaIiSydfzsdZk4YMvPwvw725omVtWcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کاروان پرسپولیس دقایقی قبل وارد ارزروم ترکیه شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/136556" target="_blank">📅 21:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136555">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❗️
قاب ماندگار بازی پرتغال - اسپانیا؛ دلجویی یامال از رونالدو پس از سوت پایان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/SorkhTimes/136555" target="_blank">📅 20:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136554">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
مرتضی و کاظمیان با تیم به ترکیه نرفتن و جداییشون تقریباً قطعیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/136554" target="_blank">📅 20:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136553">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/136553" target="_blank">📅 20:29 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
