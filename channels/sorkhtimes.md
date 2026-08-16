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
<img src="https://cdn4.telesco.pe/file/GKNHqrY6mRDP-hVDlEvyak4BZsxiSb3wLsQ5zf2MfguD0kTp9CHT-Ga9Gi8iptHSOn99FKv7Gorr_ieXw73k5VywhBMj3O817_2kWFMyKKkEu_23uqOKHqbHgq4tRtYeHXAHpDkWFWzM3N0WE7U4cmJYo06JBx4_bgsxa_xAcwiZSOXyV4KLPAtc-cN3-IWcEG1D_qEOldV--jrn3akIg4FldIlk-mVURaPAK-wwR1sq-00CXGR5Te7xmGKFxiQhxbdk1iebSwJzUR_dn1SVPi1B6WyGELtcNbaaeQmLH4exlw-zkeWxC2_2LTpHr_pwSfvvvZxvjRK9fB88DQ_RSw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-25 18:15:34</div>
<hr>

<div class="tg-post" id="msg-138332">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
✅
✅
⏳
10 روز تا پایان پنجره نقل‌وانتقالات تابستانی فوتبال ایران باقی مانده است.
❌
❌
پس از بسته‌شدن پنجره، باشگاه‌ها تنها امکان جذب حداکثر 3 بازیکن آزاد را خواهند داشت. بنابراین روزهای پایانی می‌تواند برای تکمیل فهرست تیم‌ها بسیار تعیین‌کننده باشد.  «سرخ تایمز»…</div>
<div class="tg-footer">👁️ 272 · <a href="https://t.me/SorkhTimes/138332" target="_blank">📅 18:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138331">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
❌
❌
اسامی داوران هفته‌اول پریمیرلیگ ایران
😀
استقلال - مس‌شهربابک/موعود بنیادی‌فر
😀
سپاهان - چادرملو اردکان/امیر عرب‌براقی
🔴
پرسپولیس - شمس‌آذر/بیژن حیدری
😀
تراکتور - پیکان/کوپال ناظمی  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 793 · <a href="https://t.me/SorkhTimes/138331" target="_blank">📅 18:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138330">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🤝
🤝
🤝
قربانی رو بیار و بهترین پنجره تابستونی تاریخ رو به نام خودت ثبت کن دکتر پیمان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/SorkhTimes/138330" target="_blank">📅 17:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138329">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">💢
💢
💢
💢
مدیریت بانک شهر صبح امروز به وعده‌اش عمل‌کرد و 800 هزار دلار بودجه برای جذب محمد قربانی دراختیار مدیریت پرسپولیس قرار داد.
❗
❗
مدیربرنامه‌های‌محمدقربانی  به پیمان‌حدادی‌مدیرعامل پرسپولیس اعلام کرده باشگاه الوحده رو راضی میکنه که با همون 800 هزار دلار رضایت…</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/SorkhTimes/138329" target="_blank">📅 17:29 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138328">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
500 تا دیگه رفت رو رضایتنامه؛ گلزنی محمد قربانی برای الوحده که داغ دل تراکتوری ها و پرسپولیسی هارو تازه کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/SorkhTimes/138328" target="_blank">📅 17:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138327">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
✅
با اعلام تارتار دانیال ایری به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SorkhTimes/138327" target="_blank">📅 17:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138326">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
🚨
مبلغ رضایت نامه الوحده یک میلیون و دویست اعلام شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SorkhTimes/138326" target="_blank">📅 17:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138325">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
❌
با اعلام ایجنت محمد قربانی این بازیکن امروز با مدیران باشگاه الوحده برای تعیین تکلیف قراردادش جلسه دارد و رسما تکلیف بازگشت یا عدم بازگشت او به لیگ ایران مشخص خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SorkhTimes/138325" target="_blank">📅 17:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138324">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
با اعلام ایجنت محمد قربانی این بازیکن فردا با باشگاه الوحده برای تعیین تکلیف قراردادش جلسه داره و رسما مشخص میشه که میاد یا نمیاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SorkhTimes/138324" target="_blank">📅 17:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138323">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCTELWXZziXhyqFIj08HAptyMRYsyaAqXgjrxyPaObeiUcVTdZnHQ2UHZj5eq75v49eZmo-z9TNqseKm9gD2Nknl3p-HUeO0SFJbWmit648ehHLYgQ6DwEKYYXcDQ0aqV1dg4wlVNis3_Ek2U-jRg1GK6KhIC3DMFlabYQGJKHBOZNV_osR3e09s_rjB5uRF6TBlI3PAQuk-hdZ3qFtGuG_tMiBNpQPbf_svBf1sJx2XQYcjmyvV4ozO4l6YhcKw_YSlQptOIbsxnjkJ63QE0fjXJWakMN4rGL0-bydhq8KYli6PPO8aJa0DX2ZHHv9RguPNDgW2_YZhl7jKWR5GYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
افشاگری و پست اینستاگرامی محمد یوسفی: خلیلی، اینانلو و دهن‌گشاد دنبال برکناری حدادی هستند تا خودشون جای ایشون قرار بگیرند!
🔴
زیر پای افشین پیروانی رو خالی کردی تا خودت سرپرست شوی.
🔴
آمدید که از پول‌های کلان بانک، چیزی به جیب بزنید ولی کور خوندید!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/138323" target="_blank">📅 16:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138322">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">⛔️
سخنگوی بی‌درایت سرخود هفته پیش مصاحبه کرده که جذب دانیال ایری میتونه محرومیت برای تیم و باشگاه داشته باشه !!! درصورتی که پرونده ایری اصلا شبیه به کسری طاهری نیست.
⚠️
ایشون با ندانم کاری و رفتار زشتی که داشته، چالش بدی درست کرده در جذب بازیکن. شما وقتی دانش و اطلاعاتی در زمینه حقوقی و حتی فوتبال نداری بیخود میکنی چنین حرف نسنجیده‌ای میزنی.
‼️
اون از تیزر ساختنت که فقط سوتی میدی و باعث پاک شدن پست میشی. این هم از مصاحبه درمورد نقل و انتقالات!
❌
فشار بیارید تا هرچه زودتر این فرد بی‌سواد از باشگاه بره کنار. علنی دارن جلوی نقل و انتقالات رو میگیرن با صحبت‌های نسنجیده!/خرمی
#افتتاح‌مجدد
#کون_گشاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/138322" target="_blank">📅 16:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138321">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
با اعلام ایجنت محمد قربانی این بازیکن فردا با باشگاه الوحده برای تعیین تکلیف قراردادش جلسه داره و رسما مشخص میشه که میاد یا نمیاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SorkhTimes/138321" target="_blank">📅 16:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138320">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b867823a4.mp4?token=q_sV9R49nd-l5W1nzS28NkzHBvT6d-y1POHj0a3N-i3SAzl1zPcKZwrSYpN8Q9aZusr0nB3eCoeO5wik2v_83StIxTz5N4fdZbqWETVhA_5TcgNDXPbxQXkr8U6IKt9OevgiIpQzqNIYleHV-C_WgXvULTPDasVUoY9Z5reOrSexokydGbEtv0VgH5sA-2jjb2Zt4uXjD6qPvDAg-GdqW0et8EiTnzxpT7BDHGVm38cC_qv91-6PI5rCGsjz7qFLnOUyr8VGWqAFHjPPQbwZqX_M__PFpDLJUZ-gL8q49s1uOvMw1HFwHDBbyzJepJ5a4bLlLmsLUrkBhIVoueAr8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b867823a4.mp4?token=q_sV9R49nd-l5W1nzS28NkzHBvT6d-y1POHj0a3N-i3SAzl1zPcKZwrSYpN8Q9aZusr0nB3eCoeO5wik2v_83StIxTz5N4fdZbqWETVhA_5TcgNDXPbxQXkr8U6IKt9OevgiIpQzqNIYleHV-C_WgXvULTPDasVUoY9Z5reOrSexokydGbEtv0VgH5sA-2jjb2Zt4uXjD6qPvDAg-GdqW0et8EiTnzxpT7BDHGVm38cC_qv91-6PI5rCGsjz7qFLnOUyr8VGWqAFHjPPQbwZqX_M__PFpDLJUZ-gL8q49s1uOvMw1HFwHDBbyzJepJ5a4bLlLmsLUrkBhIVoueAr8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏟️
آخرین وضعیت سکوهای ورزشگاه آزادی و وضعیت زهکشی و زیرسازی چمن این ورزشگاه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SorkhTimes/138320" target="_blank">📅 16:01 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138319">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
یا الله بسم الله اسماعیل کارتال ...
🔥
❌
پ.ن چه تیمی داره حاج اسماعیل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/138319" target="_blank">📅 15:02 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138318">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✅
✅
رامین رضاییان یه ویدیو از مهران مدیری استوری کرده که در اون میگه آدمی که افشاگری میکنه، کثیف‌ترین موجود جهانه. مثل اینکه دختره راست می‌گفت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/138318" target="_blank">📅 14:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138317">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
🔴
مهرداد کفشگری: احمد نوراللهی از تراکتور مشکلاتی با قلعه نویی داشت/ احمد خیلی صبور است اما اگر صبرش لب‌ریز شود، قید همه چیز را می‌زند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/138317" target="_blank">📅 14:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138316">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✖️
مهدی تارتار:
😀
ایگور سرگیف مصدوم است و هنوز به شرایط آرمانی نرسیده است وگرنه او جزو مهاجمان اول ماست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/138316" target="_blank">📅 14:27 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138315">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🗣
🗣
🗣
بزودی باشگاه پرسپولیس جلسه‌ای توجیهی برای اوستون اورونوف ستاره ازبکی سرخ‌ ها برگزار خواهد کرد. اورونوف شب گذشته در پایان دیدار با شمس آذر درشادی بازیکنان این تیم شرکت نکرد که باعث دلخوری مهدی تارتار سرمربی این تیم شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/138315" target="_blank">📅 14:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138314">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lt5vtlcO5b_0bOsVzSbu6lSTZDQtEMZVmFHjVAdT1N1qSjcZKOS2VszweMobfqIUS0to97R_hhqOrTsKpC-VPpl1BamehPIBS2t5V8GLA0TA8I62olzAL6miCYRwIQP14axgCJ1c1l3TxgpelKfU0GAJdUf0qRai6H9CuE0JbGGAKDPZf4wkYtv8cwCG8zTZkUC35DsIWpf-8yPUrATJqIpHCVcFjpyz4xRZa5WtgOA1ER3tVJeZRKjLivbFwiOYli_0zrw26fVPt0rlBw_0kB9xa_9qSyrQVMqcBrChlBxF32sTpfrORJmFOQTRZ8H4KXH4SMrT8j9uBIvj_0lSnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🇫🇷
نبرد قهرمان اروپا در خانه لانس!
پاریسی‌ها برای شروعی قدرتمند پا به بولارت دلِلیس می‌گذارند؛ اما لانس آماده است امشب را برای پی‌اس‌جی تبدیل به کابوس کند!
🇫🇷
فینال
سوپرکاپ فرانسه
[
لانس
⚽️
🆚
⚽️
پاری‌سن‌ژرمن
]
⏰
یکشنبه ساعت ۲۲:۱۵
🏟
استادیوم بولارت دلِلیس
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/138314" target="_blank">📅 13:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138313">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
با اعلام ایجنت محمد قربانی این بازیکن فردا با باشگاه الوحده برای تعیین تکلیف قراردادش جلسه داره و رسما مشخص میشه که میاد یا نمیاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/138313" target="_blank">📅 12:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138312">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
اورونوف به‌دلیل اعتراض به نیمکت‌نشینی با تارتار به مشکل خورده و احتمال معرفی‌اش به کمیته انضباطی و غیبتش در بازی بعدی وجود دارد./هفت ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/138312" target="_blank">📅 12:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138311">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
محمد مهدی محبی، محمد عمری و پوریا پورعلی به‌ ترتیب با نمرات 8.4، 8.1 و 7.9 بهترین بازیکنان دیدار امشب دو تیم پرسپولیس - شمس آذر بودند.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/138311" target="_blank">📅 12:09 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138310">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
با درخواست کیسه به عنوان میزبان دربی ، دربی رفت به احتمال خیلی زیاد اصفهان و ورزشگاه نقش جهان باشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/138310" target="_blank">📅 12:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138309">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔄
🔄
🔄
فووووووری؛ سه گزینه باشگاه استقلال برای میزبانی دربی مشخص شد
❌
ورزشگاه‌ امام رضا مشهد
❌
ورزشگاه سهند تبریز
❌
ورزشگاه نقش جهان اصفهان  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/138309" target="_blank">📅 12:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138305">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XZ-35spyB2DkPHv7mjKv8pl4MdfBxEc7nfGbiCfKGeDDda9X7jvY_IEOYGJBKLdjlkfIikY8wMyGoT_1SiSOWXhJXmTFpNsDLg-36jo0kLWrSUg49nW86Nckfx6tfmIAW7Au-Yjqo8Cl5Y3tcd_XkWCkNYyuYYEJp5b3iQ8b9tQQB0dnMMUQ-1KwzwPpQA_9_Vz1hR8erRF8aqgJYL3nL7_c7LRodmJMgVgBK4aJNO9PmIuU5xNzYquR39VaY_7g3NJeRG5djPOtcEgbGEHDIQRr27Xjjr8wyYzNjWUOmm1Q372is_W5Ol4w2eJYtR8BlQZOANZIoI2K6gJyVt1q1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RsCgu_7Pys-Sd9Js1tmpqagzQcNyFBAP90p0bWiF4le6BdkFJkr1EqSkGu2maJCeviDg7PT6lPWodsDqU0nBDRdHnOf6P72b512bBN9s1UBMu_-FbAFIbjN7DKNJPsI3RtrnSw0x0SXUgceRLYqfpFl6VOIni59vxiidJLfYgFujPDVRJ0EsajLwIpSMR57bGMao7Rdne8-N9rrildmm6oHNNAPoR2Psx20ajVsmOvARXE2jGHYfhzXbVWVlAxgzY6mYM3Rg8_hmnQnSBP-Cua7hLT5bdfInpS--VD9O_oD6lofcGi-D5r1T5qd-Ptmf7N3qeapV5A7rpax_b1Ll9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NV9LHS7u2pdsUD289rdZMrBPzKL8L-z-Yl-DNexPfk3LfuiQ-dWTzNySmfzJh9F9A4Wnzu5IaAu66am8om9yd6kHUDCB4smsGCT6ueIj9SkY44FtKkk6w_ID2n_rOQY0qa8lDrdw2M2uUOtnc_1_Bgc1Fhr5-GSuDPBPyr0osPyONBklGHEu5uPCypkklDyWF-XBR2sEOU055s71aq-dcLEyWhxSWBNfqqPYX5c3QhkkMKfduQXU36luiRnXA6aWCuldc41zrlzigKhVcN3JCIf6_VPPszvIVgPlOS7S_6QUcaHQVRkbW0H4tONqfpmls-RFnBvpW08ZbrnGG1JpPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lJ5REdS0P8UN1Xpsd1IHujmDZMFNHPF0LCwXYZsETBTmUPtGAjgLJqWpk8j7PBvty0JpB3XkqqIqy-J8iqkwx_kfQjlDnNgReMIFOG7HV7CubkOjxO217BmTtRxg5S7R_jo15jdZijE8bN7dU7HwKmaaEYkdCFZa0VtwHUJxGOAzNM5hG-zIYgIueDB3CuMnkdd8xA2vouzYctggmQzhlMnKrddnsM9Ei6pLkfhhLW02giY8GSWBX2xYd9CIxeQVU6U9qN7OCOjYRr6k50lLPpjtaqaUHvA0UB44zydnrdtRxtmsGOBtdV0_tHlBNVrUmeGL9nvwXIAAHfquxISf2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
⚽
افشاگری‌های محمد یوسفی(هوادار متمول پرسپولیس) علیه محسن خلیلی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/138305" target="_blank">📅 11:53 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138304">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🇮🇷
🎙
واکنش تارتار به ناراحتی اورونوف: برای من دیسیپلین بازی و تیم بودن مهم هست.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/138304" target="_blank">📅 11:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138303">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
❌
کمیته انظباطی برای شفاف‌سازی وضعیت آسانی ، از سازمان لیگ و فیفا استعلام کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/138303" target="_blank">📅 11:49 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138302">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
فووووووووووووری
🚨
رسول باختر کارشناس حقوقی: یاسر آسانی بازیکن غیر مجاز است و دیدار استقلال و مس شهر بابک سه بر صفر خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/138302" target="_blank">📅 11:48 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138301">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
فرزین معامله گری دفاع چپ 22 ساله پرسپولیس برای انجام خدمت سربازی راهی ملوان شد
❌
❌
معامله گری تا تابستان 1407 با پرسپولیس قرارداد دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/138301" target="_blank">📅 10:24 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138300">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bg3L9-dk4dMbGwb5YCXWjv3pU0J0NiA_6LpR8zlhVr3C54YHjXoAQA5s02DSvgwZIQBXVHS-f6omSmC_QiwqO0IYkxk50b3S8KFpOnTDfkAqZcJwUk4tCIoluC-BHpPBO1VWsuTKKXQSIRLM9CCN-z9FXBQ1_X3aLAC02NmCikoEt5-hDmFwmV6t1bof7ws4apEGDblwbnXMphfoYEJGNFYObcSFCqK3B3JMj3dxjVqwwEdXHJkP9sU5ykDvqby2a4B_kzlzL0Z3YEFQQba_JESzfgfz5dldKn01Hm5xrB3HC5COMjYJgOTh1Fy4PDSwtLcmj4DA2GKl4vfq8NYJ3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
سه بازیکن برتر زمین در دیدار پرسپولیس _ شمس‌آذر از نگاه متریکا :
✔️
✔️
محمد عمری: 7.84
✅
✅
ابوالفضل جلالی: 7.81
✔️
✔️
محمدمهدی محبی : 7.61
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/138300" target="_blank">📅 10:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138299">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
❌
با تشکر از سهراب بختیاری زاده که ایشون رو مازاد کرد
❤️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/138299" target="_blank">📅 10:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138298">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jqc-bQNRJr1VDFoqJsfAmUad_0dTf8vcbfbOJ_m9M7aCOodB3l1okHen6RcFYB6IqpLx1fxcGcpAAH4OWoahM4rMtZfe8NNgsTtnKj3WP_BRBHewUOmAnlckj4fH45d2GXAFHMYZyVJKTuVG6qDv3y0uwaDcRMD4OlH_2Hhps_k3L6ppvlePBynOIPCKWGA2KpmBK6qbofIVQNNpyreDz71blEJC3cKberX1bK73_KASK3RRDUK3QSxNH1W7hNNuEh5sS6IoXG2D2F8qiZGDvDCv9bxXC1kvrP8CuwExBhEBbegx7SFpa-aIc0EJLfZwYhKAt1nBg_CrSQHuDiligQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
با تشکر از سهراب بختیاری زاده که ایشون رو مازاد کرد
❤️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/138298" target="_blank">📅 10:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138297">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
⚽️
بااعلام‌باشگاه پرسپولیس؛ مصدومیت ابوالفضل جلالی جدی نیست و این بازیکن مشکلی برای دیدار هفته آینده مقابل استقلال خوزستان ندارد. جلالی امروز بازی  درخشانی در ترکیب سرخ‌ها داشت.  سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/138297" target="_blank">📅 08:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138296">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✅
صبحی که تیم محبوبمون بازی و برده بخیر.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/138296" target="_blank">📅 08:53 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138295">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDjZe5ZGP7C5FguUjan5IxtxpFgAE5dG5ELvJQwF5IL8c0zwBLO5KMYFF6a59RPe2xl2m_1yoLTQPpY99tfeSlcpX-OnD8UNjdbQ-krJ3gK1JO0jRekeLAYjCQZAtRp6reKpF-fH-Ib7r4BR0iBRyHEQPBkwqBHyrX67EhXwZMTPDeRVB9q4yDfb2E_ty1rbaqPlxqrGsqxiKSB3y79sMuzCxD3zYVwBo0XoX0ByvsJoMXAB1nlOoFfCWe1Up8Y6tD8DtE8vkShl65PTEWE9SK9ZZJju1DnGbIfTEFvPyS2erIAC2lfOCMoVacbFqKOKuetsSUtInW8SyuoWPdUqMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نبرد غول‌ها برای اولین جام فصل؛ جایی برای اشتباه نیست!
آرسنال با فشار و پرس مقابل سیتیِ باتجربه؛ نبردی که جزئیات تاکتیکی می‌تواند برنده را تعیین کند.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
فینال
سوپرکاپ انگلیس
[
آرسنال
⚽️
🆚
⚽️
منچسترسیتی
]
⏰
یکشنبه ساعت ۱۷:۳۰
🏟
استادیوم پرینسیپالیتی
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/138295" target="_blank">📅 01:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138294">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
❌
فوووووووووووری
😀
انتقال محمد قربانی به پرسپولیس کنسل نشده و هنوز احتمال نهایی شدن این انتقال وجود دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/SorkhTimes/138294" target="_blank">📅 00:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138293">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
زارع هم تو دفاع خوب بود ...  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/SorkhTimes/138293" target="_blank">📅 00:38 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138292">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/SorkhTimes/138292" target="_blank">📅 00:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138291">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/138291" target="_blank">📅 00:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138290">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✅
✅
با اعلام تارتار دانیال ایری به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/SorkhTimes/138290" target="_blank">📅 00:29 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138289">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
❌
ترامپ به فاکس نیوز: به‌ایران از لحاظ اقتصادی ضربه شدید خواهیم زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/SorkhTimes/138289" target="_blank">📅 23:59 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138288">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✅
مهدی تارتار: یکی دو بازیکن دیگر میخواهم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/SorkhTimes/138288" target="_blank">📅 23:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138287">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔄
🔄
تارتار:
✅
شمس‌آذر نیمه دوم بهتر بود/ باید از بلندی چمن گلایه کنم چراکه باعث خستگی و مصدومیت بازیکنان ما شد  سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/SorkhTimes/138287" target="_blank">📅 23:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138286">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⚡️
حمید مطهری، سرمربی فولاد: رامین بازیکن مورد علاقه من است و می‌دانم چگونه از او بازی بگیرم‌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/138286" target="_blank">📅 23:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138285">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
فووووووووووووری
🚨
رسول باختر کارشناس حقوقی: یاسر آسانی بازیکن غیر مجاز است و دیدار استقلال و مس شهر بابک سه بر صفر خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/SorkhTimes/138285" target="_blank">📅 23:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138284">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووووووووری
🚨
زهره فلاح زاده خبرنگار حوزه استقلال: هنوز استعلام سازمان لیگ از فیفا نرسیده و مدیران باشگاه استقلال با بازی دادن آسانی در بازی دیشب ریسک بزرگی کردن و اگه جواب استعلام مثبت نباشه بازی دیشب استقلال و مس شهر بابک سه بر صفر میشه
😂
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/138284" target="_blank">📅 23:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138283">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWXgLsQksusLMVJbM01NSz8CB69mNRAQE7YAHGYaxFcjQZd-3fxmSmjWs5fahKYGboQwVEC58jRvM5dU5Vwu83n2Yqm85urUPJ22PbII4hVHj0N1nA3XwMeQWDusEY5A9lDwRoYb3ULqytpqTnCRoEvL7MRdZwLuh2wHFZBt4PONatK758len_L-BYTZJcgrZmTIptbQs5JPg3Wlz7IY-DqIt-BeoNu5qWpfM9QulV3q5TvNSMSwvLmvcelhHGXsj1LiTghiKeoQNZQbCgG2sNEq3ltR1hzMP-eMoAjIQpwYwFexCgwf2-MHUqxJAy4n7YS_Y1v7RTA6aO-Qu_GyLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚽️
بااعلام‌باشگاه پرسپولیس؛ مصدومیت ابوالفضل جلالی جدی نیست و این بازیکن مشکلی برای دیدار هفته آینده مقابل استقلال خوزستان ندارد. جلالی امروز بازی  درخشانی در ترکیب سرخ‌ها داشت.
سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/138283" target="_blank">📅 23:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138282">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔽
🔼
بازیکنی که امروز اصلا بازیش به چشمم نیومد عیدی بود، بنظرم باشگاه باید با جدیت سراغ رامین رضاییان بره…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/138282" target="_blank">📅 23:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138281">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
⚠️
امیر علی‌اکبری در مقابل علیخان واخایف از روسیه ناک اوت شد. واخایف با این پیروزی، کمربند قهرمانی سنگین وزن در سازمان روسی ACA را حفظ کرد.
سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/138281" target="_blank">📅 23:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138280">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d1929df98.mp4?token=XDe2a0j1QdBAcegQrxpct0qAcDTWFKeV45jP4xw_nMQPd2K53KpLYNiqxsRHtFhBFM5FewD9NqCNsFbL2b1z-PSMm7OWb8RO1km7J9vUY9XMl9FBHQ-4naR_6NLFz4Mhdf0I-9pNo-LDAN0w_xP1rs7XwHClwwHXYvw8ZUKBOZ8DZLiROIK7pgeKCv1spUcDnvObhGRbC3cKhRDZjNilZ4h1R6jGnfMb07-flH15FU2CGfElreFrStW4udVww4HtqyPKYe1IJGQF8OIcVL2bWxIqMIV-Tc5BcBncRFw2N-7gyos-OK4w0qcCtFTyjj5qzlKNfInJHVup8wpfnIiPRB8QDtRk8vtaQVlSlF6GDgfP3M0LBX0DqQAHnlNd5ZMMi43TrK2hu1ln_JsIWGWIEcWLdgsyRJSK-biKr_1vG4cgLKLiWyKzGbbE54i6CNhYxY6BkjxN1ngKv3wl2vuLjmt8x3I2v3uk-gdzYY76Bic5YikG34J9NhJUrQjTlgkWsHLjUEcA-aXHlxiBnefeSzlXnt2T24UBwpNb-FRRKM-YTzdgLw4-5BzwMUpCzGQu1DJMu1-SjaX97fFAvIqj5USOoVqF7ihWpClFvcaJW0ybTZbynabrZNZLrMYAd_7FuHn0LD-MKHAqAbv_BUcW4PwnL67fXsP2gER8qkIvqyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d1929df98.mp4?token=XDe2a0j1QdBAcegQrxpct0qAcDTWFKeV45jP4xw_nMQPd2K53KpLYNiqxsRHtFhBFM5FewD9NqCNsFbL2b1z-PSMm7OWb8RO1km7J9vUY9XMl9FBHQ-4naR_6NLFz4Mhdf0I-9pNo-LDAN0w_xP1rs7XwHClwwHXYvw8ZUKBOZ8DZLiROIK7pgeKCv1spUcDnvObhGRbC3cKhRDZjNilZ4h1R6jGnfMb07-flH15FU2CGfElreFrStW4udVww4HtqyPKYe1IJGQF8OIcVL2bWxIqMIV-Tc5BcBncRFw2N-7gyos-OK4w0qcCtFTyjj5qzlKNfInJHVup8wpfnIiPRB8QDtRk8vtaQVlSlF6GDgfP3M0LBX0DqQAHnlNd5ZMMi43TrK2hu1ln_JsIWGWIEcWLdgsyRJSK-biKr_1vG4cgLKLiWyKzGbbE54i6CNhYxY6BkjxN1ngKv3wl2vuLjmt8x3I2v3uk-gdzYY76Bic5YikG34J9NhJUrQjTlgkWsHLjUEcA-aXHlxiBnefeSzlXnt2T24UBwpNb-FRRKM-YTzdgLw4-5BzwMUpCzGQu1DJMu1-SjaX97fFAvIqj5USOoVqF7ihWpClFvcaJW0ybTZbynabrZNZLrMYAd_7FuHn0LD-MKHAqAbv_BUcW4PwnL67fXsP2gER8qkIvqyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
واکنش کنعانی زادگان به شایعه قهر اورونوف
⚡️
حسین کنعانی :
اوستون پایان‌بازی برای هواداران دست تکون داد و اصلا چنین چیزی در تیم  ما نیست که یک‌بازیکن بخواهد قیافه بگیرد یا بگوید حق من است که بازی کنم‌ در پرسپولیس بازیکن چه یک دقیقه بازی کند چه نود دقیقه از دل و جان مایه میگذارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/138280" target="_blank">📅 23:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138279">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔖
❤️
من از این تیم تمام قد حمایت میکنم،انتقاد سازنده باید باشه، حمایت باید باشه هوادار حق داره نظر بده و انتقاد کنه، ما باید روز به روز پیشرفت کنیم بازم خسته نباشید میگیم به تمام بازیکنان و کادرفنی آقای حدادی که واقعا زحمت کشیدن
❌
این تیم خیلی پتانسیل داره،جوان های خیلی خوبی جذب کردیم و تو آکادمی مون داریم، من خوشبینم امیدوارم بازی های زیبایی از این تیم ببینیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/138279" target="_blank">📅 23:09 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138278">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دلیلش تفکر مسخره مربی ایرانی که تا یه گل میزنن با ک و ن میرن تو دفاع و تعویض های اشتباه مربی وقتی بجای بیفوما ابرقویی میاد تو انتظار داری حمله کنیم؟؟؟ اصلا چه نیازی بود تغییر سیستم بدیم  به ۳۵۲؟؟؟ میتونست جای بیفوما ارونوف رو بیاره ببینم بازم دفاع شمس اذر…</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/138278" target="_blank">📅 23:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138277">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🔱 Hero 🔱</strong></div>
<div class="tg-text">دلیلش تفکر مسخره مربی ایرانی که تا یه گل میزنن با ک و ن میرن تو دفاع و تعویض های اشتباه مربی وقتی بجای بیفوما ابرقویی میاد تو انتظار داری حمله کنیم؟؟؟ اصلا چه نیازی بود تغییر سیستم بدیم  به ۳۵۲؟؟؟ میتونست جای بیفوما ارونوف رو بیاره ببینم بازم دفاع شمس اذر جرات داره بیاد جلو</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/138277" target="_blank">📅 23:04 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138276">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromF_baj</strong></div>
<div class="tg-text">مگه گل گهره دفاع کنه</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/138276" target="_blank">📅 23:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138275">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">میخواد با ۱۱ تا دفاعم بازی کنه فقط باید امتیاز بگیره</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/138275" target="_blank">📅 23:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138274">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاَمیر</strong></div>
<div class="tg-text">میخواد با ۱۱ تا دفاعم بازی کنه فقط باید امتیاز بگیره</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/138274" target="_blank">📅 23:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138273">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
تنها چیزی که درک نکردم این بود چرا نیمه دوم تا این حد عقب کشید تیم وقتی از همه لحاظ و مهره ای سوار بازی بودیم، درسته بازی اوله سه امتیاز مهمه و شمس آذر روی کناره ها خطرناکه اما اینکه شما توپو بدی به حریف بشینی عقب خیلی خطر گل خوردن بیشتره، شمس آذر نیمه اول…</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/138273" target="_blank">📅 23:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138272">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
تنها چیزی که درک نکردم این بود چرا نیمه دوم تا این حد عقب کشید تیم وقتی از همه لحاظ و مهره ای سوار بازی بودیم، درسته بازی اوله سه امتیاز مهمه و شمس آذر روی کناره ها خطرناکه اما اینکه شما توپو بدی به حریف بشینی عقب خیلی خطر گل خوردن بیشتره، شمس آذر نیمه اول به زور سه تا موقعیت داشت، نیمه دوم راحت تا جلو دروازه ما میومدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/138272" target="_blank">📅 22:58 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138271">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔽
🔼
بازیکنی که امروز اصلا بازیش به چشمم نیومد عیدی بود، بنظرم باشگاه باید با جدیت سراغ رامین رضاییان بره…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/138271" target="_blank">📅 22:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138270">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">➕
در کل باید از این تیم و مجموعه حمایت کرد، همدلی باشه هر غیر ممکنی هم ممکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/138270" target="_blank">📅 22:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138268">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">📊
تیم واقعا امروز شاداب بود، هفته اول بوده نمیشه هنوز با قاطعیت گفت ولی چشم پوشی هم نمیشه کرد امروز واقعا خوب بودیم،خیلی وقتا بازی هارو بردیم ولی اون پرسپولیسی که باید میبودیم نبودیم، این تیم اگر به همین روال ادامه بده و بازی که نیمه اول به نمایش گذاشت تو همه بازی ها به نمایش بزاره من امیدوارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/138268" target="_blank">📅 22:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138267">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🏅
این اولین بازی بود بعد از یک سال اندی که من کامل تماشا کردم، طی دو سال اخیر اکثرا خوابم میبرد پای تلویزیون…
😬
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/138267" target="_blank">📅 22:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138266">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">⭕
این تیم به عقیده من بوی قهرمانی میده،همه خرید هامون عملکرد واقعا خوبی از خودشون نشون دادن و بنظرم ارزشش رو داشتن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/138266" target="_blank">📅 22:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138265">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEjV2hVaz7UnZgZtnnoE3j6A0MrgFRAbjVTb0mEG72EwYtB44hjBFwBkSFWhD6Y2ptUFAnOmBehnxs4CiKXBbsNVoIv82sznT5gQ9Z4Eavuuea4rIjiFVShOd8b0oS9i6l-5BIuvwFoAHHVKl7RdhZPYMYAXnGFQ_yeyWjYSy4cO6X-TTIqvc0P4ckqU6iAebxMGO3Fw3X1oOtEkaIu-dEeBvBUw6mAaTBeG9B6FUGsfem5qkSjiWYtAUR_pd5u8SEE-TJRIm7KYsiISezDlqUDRB0NFHsgvYA_FngtVyeWifm1sD5EIY_i_zgdDW3mXFf77hhixJ8QETaZJF1GKVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
برنامه هفته دوم لیگ برتر
سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/138265" target="_blank">📅 22:46 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138264">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✅
✅
✅
مهدی تارتار، سرمربی تیم پرسپولیس: هیچ قولی برای قهرمانی نمی‌دهیم، اما هدفمان کاملاً مشخص است و برای رسیدن به قهرمانی تا آخرین روز تلاش خواهیم کرد. از هواداران می‌خواهم صبور باشند و از تیم حمایت کنند.
❌
هنوز کار ما در نقل‌وانتقالات به طور کامل تمام نشده…</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/138264" target="_blank">📅 22:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138263">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔄
🔄
تارتار:
✅
شمس‌آذر نیمه دوم بهتر بود/ باید از بلندی چمن گلایه کنم چراکه باعث خستگی و مصدومیت بازیکنان ما شد  سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/138263" target="_blank">📅 22:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138262">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔄
🔄
تارتار:
✅
شمس‌آذر نیمه دوم بهتر بود/ باید از بلندی چمن گلایه کنم چراکه باعث خستگی و مصدومیت بازیکنان ما شد  سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/138262" target="_blank">📅 22:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138261">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
تارتار: در نیمه اول پرسپولیسی بودیم که خودم دوست دارم؛ تهاجمی و جنگنده/ در نیمه دوم شمس‌آذر تیم بهتری بود  سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/138261" target="_blank">📅 22:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138260">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🇮🇷
🎙
واکنش تارتار به ناراحتی اورونوف: برای من دیسیپلین بازی و تیم بودن مهم هست.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/138260" target="_blank">📅 22:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138259">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3867654e00.mp4?token=c2erhICy94qDkBxk3pgbG23Bwi_End8MdtgeSr4ZUEHlnRIoDW7a3kZkRjr7wXvW7lLJWgwzy44xOS774iAHgUA9yXai3c-3TZ7wnntIwUHRLHPQE8dI6BoQV0EW5d0MBEkUzxE_5mbOtRhUXG3ddqsWAjzL4Syfu10xxGuD3DYrMUumd0-BI_-pAg48-4uzEg0RDcvNy2T0hsMXFZ05JkOt9U_sDPliveSzoinKPCgx051dKZIQFlTLGs4Zv8xh204ZUhqrzMe_pA2mHLAFiD90yzZcdDHX5yrTrbXCcik45oPAR3UE6-2Id5WHoGntPfOkjS8Ul1X7hhLCNvPr2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3867654e00.mp4?token=c2erhICy94qDkBxk3pgbG23Bwi_End8MdtgeSr4ZUEHlnRIoDW7a3kZkRjr7wXvW7lLJWgwzy44xOS774iAHgUA9yXai3c-3TZ7wnntIwUHRLHPQE8dI6BoQV0EW5d0MBEkUzxE_5mbOtRhUXG3ddqsWAjzL4Syfu10xxGuD3DYrMUumd0-BI_-pAg48-4uzEg0RDcvNy2T0hsMXFZ05JkOt9U_sDPliveSzoinKPCgx051dKZIQFlTLGs4Zv8xh204ZUhqrzMe_pA2mHLAFiD90yzZcdDHX5yrTrbXCcik45oPAR3UE6-2Id5WHoGntPfOkjS8Ul1X7hhLCNvPr2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🎙
واکنش تارتار به ناراحتی اورونوف: برای من دیسیپلین بازی و تیم بودن مهم هست.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/138259" target="_blank">📅 22:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138258">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
به نظر می رسد در فصل جدید گرا، باکیچ و سرگیف فرصت بازی کمی خواهند داشت. مراقب باشید سهمیه خارجی نسوزد.//بزرگ نیا   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/138258" target="_blank">📅 22:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138257">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f1930bdf6.mp4?token=K3I32x_0rKhF1iWzwSjIRFwNvmOhtdTpdxXKblKEo-HqzlaxlQooumNzyMxOCJpxy2xw_RHeNxDhXFPVgV_4q-K7uz4P9vc9cFstyW2J2uOdSj6hst1Kt_daScgi5sZuCXSF3--05sjVldJYLhdcHS7_htxE8m4asDrEOuBJM5lpGujxltyO5n5TpWlczpdWijxOAzt0dBetC0Y9gg_G_tFroXJe-DQ1bGdUfKVeB9qW8uOo6zkO_meCymsp9V5rz8dUmAjFWxF00xVfT1B-T3og7wpI6sclsXbRi86ZUyE_YM53Zln_tremDW3-R29GOxkv6eHk8ZMBnv0rWeTiqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f1930bdf6.mp4?token=K3I32x_0rKhF1iWzwSjIRFwNvmOhtdTpdxXKblKEo-HqzlaxlQooumNzyMxOCJpxy2xw_RHeNxDhXFPVgV_4q-K7uz4P9vc9cFstyW2J2uOdSj6hst1Kt_daScgi5sZuCXSF3--05sjVldJYLhdcHS7_htxE8m4asDrEOuBJM5lpGujxltyO5n5TpWlczpdWijxOAzt0dBetC0Y9gg_G_tFroXJe-DQ1bGdUfKVeB9qW8uOo6zkO_meCymsp9V5rz8dUmAjFWxF00xVfT1B-T3og7wpI6sclsXbRi86ZUyE_YM53Zln_tremDW3-R29GOxkv6eHk8ZMBnv0rWeTiqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
🔴
تشویق ایسلندی پرسپولیسی‌ها و هوادارانشان با رهبری محمدحسین کنعانی‌زادگان
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/138257" target="_blank">📅 22:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138256">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQcwNXffOiXPXJOxxU4fhtIzzGU_lnU-lKdmF_OKE9FjLRZ1QuMGDp4hDk8oD2zi8mIL3K72rln0AEenc2ZkW2C3MKH331feg0iVxgLLMPBeOHuRBPEdz35EnPPeVzmo4z2mL6ahOb7Jp5sCnSm3PxmSspNG3XO4XRq6JWjPDVGCw3dUEiBZXoHGO0KhESbMTqn4lPebk0ddwvXhwunKzCeHuuScrMLnYGRzQ2vJYFG6WmhdLbK-BuiDUDQlYmp72QaDBHAMp_UgKtKe2mIHgpuLHq0VDRA25tC5iznB7VvwHqDVEeFasMqfa-zfVn_-Z0SUVIxoTeJ8-P9EgL0_dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محمد مهدی محبی، محمد عمری و پوریا پورعلی به‌ ترتیب با نمرات 8.4، 8.1 و 7.9 بهترین بازیکنان دیدار امشب دو تیم پرسپولیس - شمس آذر بودند.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/138256" target="_blank">📅 21:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138255">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✖️
✖️
واقعا بازیکن بد نداشته امروز پرسپولیس   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/138255" target="_blank">📅 21:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138254">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
دکتر پیمان هنوز مونده تو استودیو فوتبال و تکون نخورده   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/138254" target="_blank">📅 21:48 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138253">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
دکتر پیمان هنوز مونده تو استودیو فوتبال و تکون نخورده   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/138253" target="_blank">📅 21:44 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138252">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✖️
✖️
واقعا بازیکن بد نداشته امروز پرسپولیس   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/138252" target="_blank">📅 21:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138251">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✖️
✖️
واقعا بازیکن بد نداشته امروز پرسپولیس   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/138251" target="_blank">📅 21:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138250">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‼️
بریم برای نیمه دوم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/138250" target="_blank">📅 21:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138249">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
❌
نیمه دوم هر کی بیاریم داخل..‌ بازی و در میاره راحت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/138249" target="_blank">📅 21:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138247">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fF4tgCNN6qAiW0oNr1NFWDkuZig4h0Kdr719K8NdqIRfL6wchIp82s1ENaI1uLTkwJMuO7jxi1yRx4lx0Rp08qanLWRJecY9srBmGs8jGHcrBepDUA_tqWiA2Yvi56YMUrCNqt3dvkilZLFKX1ErmmlCgpXPTF5zWC2UmQUneKsYe2ITnyedT0k5k_bERDdvGJPQbPnvclr0ruexY0uqlBYZQiAfvTPmYD83NWNFL4E2mfEkbBhr0YJlPq7Zr21lsmSVVouhd_fQPlDfVLMpNuTcddPluBb2qMha4xJoTHTQ5HcS5j0BaU7syxTzqgHQZ9JbFzha2lSeHm4K21g6Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پرسپولیس؛ آماده برای شکار شمس‌آذر!
🔴
Persepolis -
🟢
ShamsAzar
🔵
لیگ خلیج فارس
⏰
شنبه ساعت ۱۹:۳۰
🏟
استادیوم سردار آزادگان
📌
فقط تماشاگر نباش؛ همین حالا وارد مینی‌اپ وینکوبت شو و با اولین شارژ خود و دریافت ۱۰٪ بونوس ویژه این دیدار رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/138247" target="_blank">📅 20:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138246">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">هواداران اگه امسال قهرمانی می‌خوایم برین پست آخر پیج بانک شهر و پست آخر پیج پرسپولیس :
👈
جذب محمد قربانی
👈
اخراج اینانلو
👈
اخراج احد میرزایی  ( اینانلو و میرزایی ۲ مهره ضد پرسپولیسی هستند که مانع تقویت پرسپولیس می‌شوند و حضورشون سم مطلق است )</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/138246" target="_blank">📅 20:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138245">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
دکتر پیمان هنوز مونده تو استودیو فوتبال و تکون نخورده   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/138245" target="_blank">📅 20:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138244">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
❌
پیمان حدادی: در حال مذاکره برای جذب محمد قربانی هستیم و برای جذبش دغدغه مالی نداریم ولی بعید می‌دونم الوحده فروشنده باشه چون هنوز قیمت ندادن و شاید قربانی تمدید کنه!   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/138244" target="_blank">📅 20:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138243">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736ad661da.mp4?token=GVK1tHUlX_1ILO-0xXqlddJMMB0GfUDJA7r1_mAKP2TiB_wyV1sRNDK701KqphzDaVq_oYVIDn83qVq3vEwDDK5gXS9Ch-pTWvxsSGAxSR87RG094-Erzxaha9t-CkAvn4Z03Kri4ObswzDQix2IyOKWzSl3imVOTzdhdVgmKXDGxwl2kuHfUF_MSyQ35FRE0hCUS6XD_JtPo9CH2PWONzcDuTzTGKv-ukgmR8MTM30BNokfxChjlLQFEBnBwKkkYxIiBORbfUbhZsfmXgzOWMuD8KPsgh-ZIsfAroVrxNeymbbMNaSwem2LYu1dC8Shvaa8RxM5RrZiS12j8llJFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736ad661da.mp4?token=GVK1tHUlX_1ILO-0xXqlddJMMB0GfUDJA7r1_mAKP2TiB_wyV1sRNDK701KqphzDaVq_oYVIDn83qVq3vEwDDK5gXS9Ch-pTWvxsSGAxSR87RG094-Erzxaha9t-CkAvn4Z03Kri4ObswzDQix2IyOKWzSl3imVOTzdhdVgmKXDGxwl2kuHfUF_MSyQ35FRE0hCUS6XD_JtPo9CH2PWONzcDuTzTGKv-ukgmR8MTM30BNokfxChjlLQFEBnBwKkkYxIiBORbfUbhZsfmXgzOWMuD8KPsgh-ZIsfAroVrxNeymbbMNaSwem2LYu1dC8Shvaa8RxM5RrZiS12j8llJFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#
منهای_پرسپولیس
☑️
گل اول صنعت نفت آبادان به ملوان (اولین سوپر گل لیگ امسال
♦️
صنعت نفت آبادان  یک - صفر ملوان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/138243" target="_blank">📅 20:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138242">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✖️
✖️
یازده تای اون زمین کی هستن که اینا نیمکتن
😂
:
✔️
رفیعی
✔️
ابرقویی
✔️
تیکدری
✔️
اورونوف
✔️
شهرآبادی
✔️
سرگیف
✔️
باکیچ
✔️
لطیفی فر
✔️
محمودی
✔️
همایی فرد
✔️
سلمانی  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/138242" target="_blank">📅 20:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138241">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
❌
بهترین بازیکن نیمه اول از نظر شما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/138241" target="_blank">📅 20:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138240">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✅
خوشگل میشه به این تیم امید داشت و امیدوار بود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/138240" target="_blank">📅 20:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138239">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
❌
تیم سرحال نشون داده  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/138239" target="_blank">📅 20:12 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138238">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">⚡️
⚡️
شنیده میشه تیوی بیفوما در یک ماه اخیر برای ماندن در پرسپولیس زیر نظر پزشک تغذیه باشگاه 8 کیلو کاهش وزن داشته و علاوه بر اون زندگی حرفه ای شو سالم تر از قبل کرده و تمرکز اصلی شو روی فوتبال خودش گذاشته!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/138238" target="_blank">📅 20:07 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138237">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
❌
❌
✖️
جونم به این تیم ..چه تیم شادابی درست کرده تارتار  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/138237" target="_blank">📅 19:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138236">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✖️
✖️
دو گل تو بیست دقیقه   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/138236" target="_blank">📅 19:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138234">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
بریم برای اولین بازی فصل با تارتار .الهی به امید تو   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/138234" target="_blank">📅 19:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138233">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
بریم برای اولین بازی فصل با تارتار .الهی به امید تو   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/138233" target="_blank">📅 19:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138232">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
❌
شماتیک ترکیب پرسپولیس برابر شمس‌آذر  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/138232" target="_blank">📅 19:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138231">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
❌
در سیاست کاری ما نبود از یک سن بیشتر بازیکن جذب کنیم. عدد درخواستی او از پرسپولیس کمتر از سایر باشگاه‌ها بود ولی از سقف ما خیلی بالاتر بود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/138231" target="_blank">📅 19:19 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138230">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
واکنش حدادی به شایعه حضور محمد قربانی در پرسپولیس؛ حضور او به احتمال زیاد منتفی است و با الوحده تمدید می‌کند  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/138230" target="_blank">📅 19:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138229">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
❌
در سیاست کاری ما نبود از یک سن بیشتر بازیکن جذب کنیم. عدد درخواستی او از پرسپولیس کمتر از سایر باشگاه‌ها بود ولی از سقف ما خیلی بالاتر بود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/138229" target="_blank">📅 19:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138228">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
فووووری از پیمان حدادی: با رامین رضاییان مذاکره کردیم، تخفیف خوبی داده، انگیزه داره برگرده  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/138228" target="_blank">📅 19:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138227">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✔️
حدادی : رامین خیلی انگیزه داره بیاد پرسپولیس‌  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/138227" target="_blank">📅 19:12 · 24 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
