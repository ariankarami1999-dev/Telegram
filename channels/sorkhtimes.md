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
<img src="https://cdn4.telesco.pe/file/VjqPWb0F2LO6KW6EfzBdMRpcAoDWBIlpECFAIGYH0zrTYekiWGWQTodVeH7P6HD5F8f8dBAFbXoXtaHWCA-hQes-jHwtvkwql4QLxc6-LJ_BwDuV0C5o2FX5-stUnZPgaSddx1SNYrF-qAR0OmBihUgxqfRCY8xyHWJJjCE8cjAxvZql-KwY4XaNA9FcnNRv4Q3N8xdn9A-v4CXsqrexrx-k44upOWhanRsvXGlH1bs2uox1er76r1H-vZGlM0_C77GZwn8ulKPxbeSgQw74ubzn7ercw0CnUZ3hEUhKLfR0DeXjBIi2oxv1HXlebAifESf1c6MAC3YMffF83KVpAQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 15:31:30</div>
<hr>

<div class="tg-post" id="msg-134935">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
✅
شنیده ها: با وساطت سید جلال حسینی، مدیران باشگاه پرسپولیس امروز با مازیار زارع سرمربی ملوان بندر انزلی وارد مذاکره شدند و جلسه ای با این مربی برگزار کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/SorkhTimes/134935" target="_blank">📅 15:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134934">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❗️
❗️
شنیده ها: باشگاه داره با یک مربی فرانسوی صحبت میکنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 32 · <a href="https://t.me/SorkhTimes/134934" target="_blank">📅 15:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134933">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/134933" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SorkhTimes/134933" target="_blank">📅 14:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134932">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mDBAG8eNdxiULvpj7_U0SsnES5u9NlcmxJMMWZPpfi4YT0AuL4kBlWeUN65JLNZOUAr5JKyAvZ342FGu8OJs9TfmHT81N2sX7-CJaVvXcb313y7Rer1Yw7I7-5s84WwrjOY5yGK2MvIpi3MZLfc6q3vv_AaEmFDpQaqwLn4b6GyQoVO7Fv4TaD-qTcIjed3lo_lH0wvziM8m9oiN8ZfwfuXNx1poQNPzPB0rAwVlCUc41WVaP_YmGU4QSm7QHMzrTWBhYtbYXVJLsS-REqYsKRxbhinAsOZGDlV59wM-Qfza7bZ7TRtsoxPpNcNuvVt07Hc2OlmP0klq52I9B4b-pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
بازی فوووق جذااااب
کانادا
و
مراکش
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
🆕
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی جام جهانی
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه ای، مطمئن و در کلاس جهانی پیشبینی کنید!
برای ورود به سایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/SorkhTimes/134932" target="_blank">📅 14:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134931">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
❌
ابوالفضل جلالی که قراردادش با استقلال تموم شده، دوست داره به پرسپولیس بره. چون بازیکن آزاده، پرسپولیس شرایط جذبش رو بررسی می‌کنه، اما تصمیم نهایی رو سرمربی جدید تیم می‌گیره.
🔴
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/SorkhTimes/134931" target="_blank">📅 13:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134930">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
استوری دراگان اسکوچیچ :
🔴
تلاش‌ها برای جلوگیری از بازگشتم و پخش کردن دروغ درباره جدایی‌ام از ایران، مرا تضعیف نکرد؛ بلکه فقط ترس کسانی را که پشت پرده فعالیت می‌کنند آشکار کرد.
🔴
نحوه مدیریت مذاکرات توسط باشگاه، تنها نشان داد که این باشگاه در مذاکرات جدیت…</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SorkhTimes/134930" target="_blank">📅 13:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134929">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">#نظر_شخصی
🤩
من مقصر این وضعیت رو «فقط بانک» شهر نمیدونم این نظر منه
☑️
ببینید تیم هیچ دغدغه مالی نداره، هیچ بدهی ای نداره، حدادی بالغ بر ۵۰۰ میلیارد درآمدزایی داشته و بانک شهر کاملا ساپورت مالی کرده
📚
از دید من علت نتیجه نگرفتن پرسپولیس چندین علت داره،…</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SorkhTimes/134929" target="_blank">📅 13:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134928">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
استوری دراگان اسکوچیچ :
🔴
تلاش‌ها برای جلوگیری از بازگشتم و پخش کردن دروغ درباره جدایی‌ام از ایران، مرا تضعیف نکرد؛ بلکه فقط ترس کسانی را که پشت پرده فعالیت می‌کنند آشکار کرد.
🔴
نحوه مدیریت مذاکرات توسط باشگاه، تنها نشان داد که این باشگاه در مذاکرات جدیت…</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/SorkhTimes/134928" target="_blank">📅 13:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134927">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
شنیده ها: پاتریس کارترون گزینه پرسپولیس در صورت عدم توافق نهایی با اسکوچیچ!!!!!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SorkhTimes/134927" target="_blank">📅 13:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134926">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">#نظر_شخصی
🤩
من مقصر این وضعیت رو «فقط بانک» شهر نمیدونم این نظر منه
☑️
ببینید تیم هیچ دغدغه مالی نداره، هیچ بدهی ای نداره، حدادی بالغ بر ۵۰۰ میلیارد درآمدزایی داشته و بانک شهر کاملا ساپورت مالی کرده
📚
از دید من علت نتیجه نگرفتن پرسپولیس چندین علت داره،…</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SorkhTimes/134926" target="_blank">📅 13:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134925">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5fH9bE-jMLyip4_zzwDOdnKVAwrNThT3bRAxTjfbLCeNykpLArMbMMpr2AbrmD-Y4yQQM_U5pEpxtF-al58FY7SylkRBCNvGzVG7HR5lDHYeYKK0qgMzq5O0iliVXXtEcS-5ACUXvHoVgOAJT4tuG2pNUjbSHM1d8HTbV4Uutf-sthOan9k8atIFn9HYqryBCVdIs8IdeOBnLYq6ejvs6a0_-JFtTbSbhKsfxpvUk38lnL8i8c8ltXFsAHHmPNy8dptB0TOfTcMnv-IF89l3sp3l-oKUFMfMuieoHi3iFW9A6yrhJ2oeSBVlJ9MZ6bmfUrybM5Yo6mHc9kTy5xVsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
جام جهانی جای عجیبیه!
🔴
🔴
توی یک شب میتونی راه ۱۰۰ساله رو طی کنی و این معمولا برای دروازه بان ها میوفته
🔴
🔴
مثلا همین ووزینیا دروازه‌بان ۴۰ساله کیپ ورد که تا ۲۵سالگی زباله بازیافتی جمع آوری میکرده اما با یک شب درخشش شگفت انگیز از ۵۰ هزار فالوئر به نزدیک ۱۵میلیون…</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SorkhTimes/134925" target="_blank">📅 12:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134924">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
ابوالفضل جلالی که قراردادش با استقلال تموم شده، دوست داره به پرسپولیس بره. چون بازیکن آزاده، پرسپولیس شرایط جذبش رو بررسی می‌کنه، اما تصمیم نهایی رو سرمربی جدید تیم می‌گیره.
🔴
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/SorkhTimes/134924" target="_blank">📅 12:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134923">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❗️
خداداد عزیزی: پلن B پیشنهادی ما به پرسپولیس یحیی گل‌محمدی بود، با یحیی حرف زدم در قراردادش بند فسخ وجود دارد که از دهوک جدا شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SorkhTimes/134923" target="_blank">📅 12:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134922">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❗️
برنامه بازی‌های امشب مرحله یک هشتم نهایی که برای اولین‌بار ساعت‌هاش مثل آدمی زاده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SorkhTimes/134922" target="_blank">📅 12:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134921">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✅
سفیر آمریکا در سازمان ملل: صبر ترامپ نسبت به ایران در حال تمام شدن است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SorkhTimes/134921" target="_blank">📅 12:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134920">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GllKUuFZ0JS2hYf4HHOPA5RNImmjSI1kTevF50LKOYvqy88SYdlv416zPKKqO2CxhxZN-dabtMFcgB70ZiLdBuGN0PLDH7RVTlVbqB1mS9stxtikIDRPtwFwbhkxwXs-KhQMyWe8Qka45F_taeKVfYE6_fMuOPnL4GtDthmmGiiYLD25OK4rbvboiI2dfm43O16S8bu0YWTpCW0U6wCSCozOV-IqEyZvfUmK7ows1wwh0Wknms1TxBo2Bh7KZGcWxdCSqmZnbi4aW0PsffV_XAjJo_cEtZQcl_ezbt3LHWZEFZ_Nnz0Ewa07-rNlQh32TBKAKiNVBrV7TSwQJ6Qo-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نتایج بازی های بامداد امروز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SorkhTimes/134920" target="_blank">📅 12:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134919">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fb54955fa.mp4?token=rIS_t0y60a6GUV3HmT7I8TjSNUAzHEzciulmYU8UtVNJV45URS-EnENH4rNERkHjRGvyz0Jvcnpv_Wou5ZTkGkOW1D-654m0SRKpIOeG9K3jA_tqbMuVzG04JbeqMj7MIVF3ACDhJw6fXaW8b_w85cigXYGVKeXsD-VSVdBrnGreJMETdq_j4YSE9Myzhxhj0DyXl8l0_Ty-zosy_XPa0v_-ArFsoEtPM-7z_339xRj6G0SqLNKIxYAfdwFM9-_gnqq0wEK9fD2ZkDQxSewkGKGl8Of50xKAao2kKjtJ3ZIYq2KECYKPTPkqgFXXVp0japEqHIHsLpAVEx2-BLUXXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fb54955fa.mp4?token=rIS_t0y60a6GUV3HmT7I8TjSNUAzHEzciulmYU8UtVNJV45URS-EnENH4rNERkHjRGvyz0Jvcnpv_Wou5ZTkGkOW1D-654m0SRKpIOeG9K3jA_tqbMuVzG04JbeqMj7MIVF3ACDhJw6fXaW8b_w85cigXYGVKeXsD-VSVdBrnGreJMETdq_j4YSE9Myzhxhj0DyXl8l0_Ty-zosy_XPa0v_-ArFsoEtPM-7z_339xRj6G0SqLNKIxYAfdwFM9-_gnqq0wEK9fD2ZkDQxSewkGKGl8Of50xKAao2kKjtJ3ZIYq2KECYKPTPkqgFXXVp0japEqHIHsLpAVEx2-BLUXXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
از مدیرای بی غیرت خودمون که فعلا خبری نیست پلن B و C و G باشگاه رو از این افغانی پیگیری کنیم انگار زودتر به نتیجه میرسیم !!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SorkhTimes/134919" target="_blank">📅 12:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134918">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✅
شنیده ها : محسن خلیلی دیروز با مهدی تارتار جلسه داشته و این مربی اعلام کرده در قرارداد جدیدش با گل گهر بند فسخی داره که میتونه به پرسپولیس بیاد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/134918" target="_blank">📅 11:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134917">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❗️
❗️
قدوسی : جدی ترین تماسها از بین گزینه های داخلی با مهدی تارتار صورت گرفته و تارتار گفته میتونه از گلگهر جدا بشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/134917" target="_blank">📅 11:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134916">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
❌
#فارس‌؛ اسکوچیچ که کلا کنسل شد رفت، پنج تا مربی ایرانی تو گزینه های حدادی ان که یحیی و تارتار از همه پررنگ ترن و احتمالشون بالاست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/134916" target="_blank">📅 11:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134915">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❗️
❗️
تسنیم اعلام کرده گزینه‌های سرمربیگری پرسپولیس یحیی گل‌محمدی، مهدی تارتار و مجتبی حسینی هستن!
🔴
خجالت نکشید! حمید درخشان و بهروز رهبری فرد و پایان رأفت و حمید استیلی رو هم گزینه کنید!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SorkhTimes/134915" target="_blank">📅 11:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134914">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❗️
🇦🇷
🇨🇻
نانا کواکو بونسام:
🔴
من با نیروهای ماورایی و روح اجدادم مشورت کردم. به مسی فقط اجازه داده شده بود که در این جام جهانی 6 گل بزنه و اون همین حالا سهمیه‌اش رو پر کرده است. ارواح به من نشان دادن که در حساس‌ترین لحظه، مقابل یک تیم غیرمنتظره پنالتی‌اش رو…</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/134914" target="_blank">📅 11:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134913">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❗️
❗️
تسنیم اعلام کرده گزینه‌های سرمربیگری پرسپولیس یحیی گل‌محمدی، مهدی تارتار و مجتبی حسینی هستن!
🔴
خجالت نکشید! حمید درخشان و بهروز رهبری فرد و پایان رأفت و حمید استیلی رو هم گزینه کنید!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SorkhTimes/134913" target="_blank">📅 11:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134912">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
❌
حرف هوادار
✅
اقایون مدیر فکر آوردن امثال یحیی و تارتار و مجتبی حسینی رو به هیچ عنوان نکنید چون هوادار پرسپولیس اون ساختمون رو سرتون خراب میکنه حواستون باشه .
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/134912" target="_blank">📅 11:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134911">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✔️
مهدی تارتار
✔️
یحیی گلمحمدی
❗️
پ ن:هردوتا مربی بند فسخ دارن و هیچ مشکلی برای پیوستن به پرسپولیس ندارن (شانس تارتار بیشتره)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SorkhTimes/134911" target="_blank">📅 10:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134910">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✅
پرونده حضور اسکوچیچ در پرسپولیس به دلیل اختلاف مالی 1 میلیون دلاری و درخواست بند فسخ در صورت جنگ ، بسته شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/134910" target="_blank">📅 10:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134909">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✅
✅
ورزش سه: با کنسل شدن اسکوچیچ مدیران باشگاه پرسپولیس به سمت مذاکره با یک گزینه خارجی دیگر خواهند رفت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/134909" target="_blank">📅 09:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134907">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✅
پرونده حضور اسکوچیچ در پرسپولیس به دلیل اختلاف مالی 1 میلیون دلاری و درخواست بند فسخ در صورت جنگ ، بسته شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/134907" target="_blank">📅 09:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134906">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0nsCbmyCOGwlj7-8Khij8HgBTwIbnvwkizCZLXs8uykD7HK1ZjV3Te8-isS2bxNdUy8OJwMGyMgxeCN8KnPWSSYjOfyIjJNsnXebPU04WbZ0rvq9u3ysfNrp6AHsJ38RzTNqPsrqCBYLSM9LKWNUghWKXWj3_Ej0MVMrFYfvMtEykGKptH_kP7AqNzmtZGlCoMtpLjg6CMb4587-E0kVWdWe3ZpsVzAzpJkjC0P7bQI10BbuJ86X75m-VIU2nmiv5JA5KZ84QmlvsAGHZoadCnnXv8z_4fIG61DIGATbDeUbzfjrhr_IdYp8FWrKbiSraP56zcXdpYCw-GPzDSFHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نتایج بازی های بامداد امروز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/134906" target="_blank">📅 09:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134905">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❗️
خداداد عزیزی: پلن B پیشنهادی ما به پرسپولیس یحیی گل‌محمدی بود، با یحیی حرف زدم در قراردادش بند فسخ وجود دارد که از دهوک جدا شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SorkhTimes/134905" target="_blank">📅 09:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134904">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ii33FRg1KUiKp1qYk3gSLERoisV3sjBK9WOUMiv-w4hXfi65K8ziXt5EmIcMvWDpIXPNoUGINRl3LFzGnDb3BfogQMOne5b48anISwXpiDCOOkak16n7QRhpaO87jCIoVQPQSrwYv-25Q6i3vfeUbG4jp-GILOsKCxHfSg03ShIuEhLrEFg9Ne41rlDYyvGtOELaBkv1xMsqnOR4KHLrRbehEbVjYX37vzWAv_gO2f5Pxrd0Hn-MKk5RlolSR0X1ePVVMrJkjYa9TgOYJAUL9qvptGiQzONjGFsrcdBpIGVRHL-hRQWZfiAiBxCznmk2bsuflSLOVzXqx3S5vfaO8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
مصلی تهران؛ هم‌اکنون
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/134904" target="_blank">📅 09:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134903">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/134903" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/134903" target="_blank">📅 01:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134902">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pr2x4_3FVJiVbVbpQ5sRhVO-0RSzPJjE63w0Hu2i-cHwXidicR6HsY28Xs0KOB7cflTO-tliEfUu7F72upYa5Ugqn5eYp_VWy8UHgCzev_n0oT6v69J-7rfVFYS0AyCHxVH6MUBeYuCbgb_8hrlXz4_QROzO9lVMderFHFzx1j-3dqZ-tlyxlf5IMmXiJNrQ8hPLV5w6od3a58e5ICgb-x17gw0_L2vB2oE7yYa97MBt2j83kBeMr8Zm4DR71_n7KOLUmJxP80IHB5shraWRqQyoxEgIbfpayv2uX2NuR_pNR4EKeQhSY0iKF9TRsw5jqoyU2lk5sYEayeNv5s811w.jpg" alt="photo" loading="lazy"/></div>
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
🅰
✔️
آموزش کامل و جامع شرطبندی
👉</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/134902" target="_blank">📅 01:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134900">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">#نظر_شخصی
🤩
من مقصر این وضعیت رو «فقط بانک» شهر نمیدونم این نظر منه
☑️
ببینید تیم هیچ دغدغه مالی نداره، هیچ بدهی ای نداره، حدادی بالغ بر ۵۰۰ میلیارد درآمدزایی داشته و بانک شهر کاملا ساپورت مالی کرده
📚
از دید من علت نتیجه نگرفتن پرسپولیس چندین علت داره، ۱- دخالت بانک شهر تو امور نقل و انتقالات ۲- ناکار آمدی و فساد مدیران قبلی در فصل آخر کاری شون۳- تغییرات پی در پی سرمربی۴- نقل و انتقالات شلخته و بالانس نبودن تیم در دو فصل اخیر ۵-یک دل نبودن هوادار و جامعه هواداری ۶- فساد مدیران میانی و انفعال هئیت مدیره و سنگ اندازی هاشون که چشم طمع صندلی مدیرعاملی دارن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/134900" target="_blank">📅 01:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134899">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🫦
جدی فضای خیلی عجیب غریبی شده، قبلا ۲۰ تا مثلا کانال پرسپولیسی بود الان ۱۰۰ تا همه هم ماشالله ادعا دارن مطلع هستن
😅
🫦
هرکسی هم یه نسخه ای برای هوادار میپیچه یکی میگه باند عالیشا داره تیمو میگاد یکی میگه دست هاش پشت پرده یکی میگه خلیلی، یه زمانی میگفتن خانبان…</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/134899" target="_blank">📅 01:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134898">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🫦
جدی فضای خیلی عجیب غریبی شده، قبلا ۲۰ تا مثلا کانال پرسپولیسی بود الان ۱۰۰ تا همه هم ماشالله ادعا دارن مطلع هستن
😅
🫦
هرکسی هم یه نسخه ای برای هوادار میپیچه یکی میگه باند عالیشا داره تیمو میگاد یکی میگه دست هاش پشت پرده یکی میگه خلیلی، یه زمانی میگفتن خانبان
🫦
به من ثابت شد اینا همش مشکلات شخصی این پیج ها و کسایی که بهشون خط میده با اون فرده، وگرنه تو این دو سال کلی تغییرات انجام شده ولی روند موقعیت متوقف شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/134898" target="_blank">📅 01:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134895">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
هرکسی رو میخاید بیارید بیارید یحیی نباشه…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/134895" target="_blank">📅 01:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134894">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b80ddf04f1.webm?token=sl4bx1fkVBm24Kdd-XoVhVutdhoeb6evhUF0b0Qix3nUT4wcCVaXmtPiorq9pwG3hOZyK0zz7PpEnQ_7Mc4F565m09aHPpO-NcokTfdD9-DBLt7D3Wga7OL0Za5uESffh_ZCWevhKMG5rkXlE3zD_9UYhjtE4tWRmCxZ_Ifhdb8W25EN4gK0fhSJFm54iEPxEgmThPWH530VtezZoZm1nAlANU2SC5EeczpozMHYMUtNjLhQoDD_8H7xHQg7S2pzo4CwKi-7BhhjQ1uiuf0DYGAZP0-Tis1umWdlFRPDKiQLWfKVNJ930pud0tyjTQl3wNWSy2mhvVbGRJbU-JXmwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b80ddf04f1.webm?token=sl4bx1fkVBm24Kdd-XoVhVutdhoeb6evhUF0b0Qix3nUT4wcCVaXmtPiorq9pwG3hOZyK0zz7PpEnQ_7Mc4F565m09aHPpO-NcokTfdD9-DBLt7D3Wga7OL0Za5uESffh_ZCWevhKMG5rkXlE3zD_9UYhjtE4tWRmCxZ_Ifhdb8W25EN4gK0fhSJFm54iEPxEgmThPWH530VtezZoZm1nAlANU2SC5EeczpozMHYMUtNjLhQoDD_8H7xHQg7S2pzo4CwKi-7BhhjQ1uiuf0DYGAZP0-Tis1umWdlFRPDKiQLWfKVNJ930pud0tyjTQl3wNWSy2mhvVbGRJbU-JXmwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/134894" target="_blank">📅 01:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134893">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">💬
چه همزمان فیض بخش و خداداد عزیزی اعلام کردن اسکوچیچ کنسله
🤝
😵‍💫
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/134893" target="_blank">📅 01:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134892">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0fb9d756f.mp4?token=YnvJGexeS3l-NV2OGdYT_DwvKEzBf439cn7Mwc_v-1syUiO5Yc4b9u3sNdtst-ZeoLSqXNyUGZfHWGfitameKOiTUbcBGZ9g6HHbK5Clc5s7IJRfua1EGTn3sd3oLTqx7Ni94df3-hkp0UqXHpzIfn9NFVnAhxDrNBz2BQMm6ciJ1wFCeVMEg0oV7SNjO7NGVMnN0OwWSj9BYRFdrIkQ-M2DTnmLLWRaU8OmLuAsYBPqSOlsX0FhnRFfAEozCwmWxVtaPwNx9xQ9wDITyKw71TFgjpdKvswMxpuCblF6ZJhvgL0Bs03_vIgOjH7ozHsXv-GUmKDEGE5dzrrCjna8uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0fb9d756f.mp4?token=YnvJGexeS3l-NV2OGdYT_DwvKEzBf439cn7Mwc_v-1syUiO5Yc4b9u3sNdtst-ZeoLSqXNyUGZfHWGfitameKOiTUbcBGZ9g6HHbK5Clc5s7IJRfua1EGTn3sd3oLTqx7Ni94df3-hkp0UqXHpzIfn9NFVnAhxDrNBz2BQMm6ciJ1wFCeVMEg0oV7SNjO7NGVMnN0OwWSj9BYRFdrIkQ-M2DTnmLLWRaU8OmLuAsYBPqSOlsX0FhnRFfAEozCwmWxVtaPwNx9xQ9wDITyKw71TFgjpdKvswMxpuCblF6ZJhvgL0Bs03_vIgOjH7ozHsXv-GUmKDEGE5dzrrCjna8uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
خداداد عزیزی: پلن B پیشنهادی ما به پرسپولیس یحیی گل‌محمدی بود
، با یحیی حرف زدم در قراردادش بند فسخ وجود دارد که از دهوک جدا شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/134892" target="_blank">📅 01:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134891">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1c6fb008f.mp4?token=REgBAsnI_fEo2C0H-eanY7sCWJXoqv3seT5Pnz-_zcuPoGlVt1FiDLUewabs0H0jF-TY85u9RgQm-Reg1M95QQ06KLqVWvk5o1KFxjlQs-8uz_LLyRuo6kj2VxiZYWUhChRcnbTcpB6POFVWsPKbPrqv91ps45Fqjip525a7hhSw94Xxo_l3m9bJRbYbUnsGG6L1Oj5Dnc5FZMj7BficwrlLglTMzhc_7S0yPc9_oFgn72ghnPZjrocUOd5upa_ffxx3AWKyAD_6c2bJ-DTRkJXmCNPOUw-__7zLSyiz66TB5ilCk7UverKXkCEDHEFG4hZkhmvP7AjfuFQRsTxhmaqMn1BpHP9quMMCWVQCxgkBWBbsljWCepgltULBuTHLBih4pekyn-xAPRpHiCnup1vS0x28RMIlqFNvkGMuhePuQkN-f-OHhGYRO0M93f6DQ2Dc9C9trCr9aezuUjoI557NlBVCUrdYl4ZfrfNj9cDytvfDtR_WyzUUSb5rAO_iLTPVz2shcHbcQ2coZfgQ-FAWZ7lbJ1Z2drPzfEp_iwhNvGjoaZvFI237F_ZxhvC3boyifVSrpMchYEs0MjeHbsXos7dL7EKrRBK-4vG1tPHwnAR7Ul_C8vIPrnRTz-58PHTW6NWTqobcUw45-DhJt62Sg9i3w4IIId0y36EZrL8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1c6fb008f.mp4?token=REgBAsnI_fEo2C0H-eanY7sCWJXoqv3seT5Pnz-_zcuPoGlVt1FiDLUewabs0H0jF-TY85u9RgQm-Reg1M95QQ06KLqVWvk5o1KFxjlQs-8uz_LLyRuo6kj2VxiZYWUhChRcnbTcpB6POFVWsPKbPrqv91ps45Fqjip525a7hhSw94Xxo_l3m9bJRbYbUnsGG6L1Oj5Dnc5FZMj7BficwrlLglTMzhc_7S0yPc9_oFgn72ghnPZjrocUOd5upa_ffxx3AWKyAD_6c2bJ-DTRkJXmCNPOUw-__7zLSyiz66TB5ilCk7UverKXkCEDHEFG4hZkhmvP7AjfuFQRsTxhmaqMn1BpHP9quMMCWVQCxgkBWBbsljWCepgltULBuTHLBih4pekyn-xAPRpHiCnup1vS0x28RMIlqFNvkGMuhePuQkN-f-OHhGYRO0M93f6DQ2Dc9C9trCr9aezuUjoI557NlBVCUrdYl4ZfrfNj9cDytvfDtR_WyzUUSb5rAO_iLTPVz2shcHbcQ2coZfgQ-FAWZ7lbJ1Z2drPzfEp_iwhNvGjoaZvFI237F_ZxhvC3boyifVSrpMchYEs0MjeHbsXos7dL7EKrRBK-4vG1tPHwnAR7Ul_C8vIPrnRTz-58PHTW6NWTqobcUw45-DhJt62Sg9i3w4IIId0y36EZrL8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خداداد عزیزی : پرونده حضور اسکوچیچ در پرسپولیس بسته شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/134891" target="_blank">📅 01:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134890">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
با اعلام ایجنت اسکوچیچ حضور این مربی در پرسپولیس منتفی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/134890" target="_blank">📅 01:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134889">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✅
آقای حدادی .بانک شهر پاسخ گو باشید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/134889" target="_blank">📅 01:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134887">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eod6zoLYDJN4Hy51z7ExdeEqixLdedMKohtuX5A1NpISQJakwxQaTw46sgz2BWNYWJP0cw-DnGExqwXE8AnLWbWm1ERuo7FxQmUu_3cUoedQ8A5KdHSJ5-3--t5k0zxGpcFJBwHVk10x62My-8WntO15w97U4xxmmbEHZkVxn44i5Z4a-BaB2VB0P1BhLj_NshUElacrH6nTYKLViTvIoM8SKLFMR-gyBxe4zFTfsrxmPXCap4MDPYZpA8Cmc-D9IlSSEOEzEAhEc95A8GIY431-0dL1n2yh6W5Aoztjqvy8IiVoCrLLJRlG905ueY_ZguCg3hLXAMHdti6TmJOq8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
با اعلام ایجنت اسکوچیچ حضور این مربی در پرسپولیس منتفی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/134887" target="_blank">📅 01:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134885">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✅
✅
گویا همه مسیر ها داره مسدود میشه.یکی از نزدیکان و افراد ایرانی نزدیک به اسکوچیچ، بهم گفت؛ بعیده این انتقال صورت بگیره.
🔴
البته باید منتظر واکنش رسمی باشگاه موند . چون اعلام کردند ظرف چند روز آینده ، همه چیز مشخص میشه//طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/134885" target="_blank">📅 01:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134884">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❗️
❗️
امیررضا رفیعی طی روزای اخیر به مدیریت باشگاه گفته میخوام جدا بشم و به زودی این اتفاق رخ میده / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/134884" target="_blank">📅 01:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134883">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLwXnms0a1iDlqBjW20kre0XCCf6NY_guDGoDPcBXy6RRqV1G0I6HBdSWmNH7jCIvjwzqgvVgAhK4IY0uowQ434VBHmib9HEcFkGFlRYxePmpvDR-CRGrVarLC2wDYW0mB0vfwU18iFbUoGivEIn4RnSh52YMTf-7VHzJzMLKJk7OwfuTZxT4NZCb_gspGopwPE3loTkJ5el-3OY-6On8qEQ9TqsQtfm1KY9FHkWohvEbgfAIUgMvLFa3wFgslKxGPJUlw96v2Ad7c28BiYK9bXRotYbYtGMtECmXFG7mC3hrXipuWl6NpRn-6GU0oCJUUsk6sdl-RNX-wOcog6D_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
تیمای آسیایی تو جام جهانی
:
😆
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/134883" target="_blank">📅 01:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134882">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
❌
بازی های امشب
🇦🇺
استرالیا_مصر
🇪🇬
🔸
ساعت 21:30
🇦🇷
آرژانتین_کیپ ورد
🇨🇻
🔸
ساعت 01:30
🇨🇴
کلمبیا_غنا
🇬🇭
🔸
ساعت 05:00
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/134882" target="_blank">📅 00:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134880">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❗️
🇦🇷
🇨🇻
نانا کواکو بونسام:
🔴
من با نیروهای ماورایی و روح اجدادم مشورت کردم. به مسی فقط اجازه داده شده بود که در این جام جهانی 6 گل بزنه و اون همین حالا سهمیه‌اش رو پر کرده است. ارواح به من نشان دادن که در حساس‌ترین لحظه، مقابل یک تیم غیرمنتظره پنالتی‌اش رو…</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/134880" target="_blank">📅 00:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134879">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
❌
بازم تاکید میکنم اسکوچیچ مربی پرسپولیس در لیگ ۲۶ خواهد بود
🎙
طاهرخانی  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/134879" target="_blank">📅 00:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134878">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✔️
#تایید_خبراختصاصی
⚽️
🤩
رسمی؛اوسمار ویرا از پرسپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/134878" target="_blank">📅 00:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134877">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWpI1DdBhTwl1cbLbrFgxF-AalxWct3HR4i0_9ARk-3rEYSdT9pTAMwjXsBlzJb5PsRB0ZFFpWXAAm5DX4ewL8Fxwv013-CDpE1gRmE3LokiMdGcqsgxMAI5k2kE6Twpi91HvJ74G59iYqEuG__1zmYeeRSGV-fxnlNgO3uiz7IClqmmrkOkOdrdts-A3MZvW84hjBM-_Rmh48f3HL2-6BqoO6DEwE-PUGpt_6joRnXOBOuRAYkalBI5F9VXnku_t7-lDBOtbqQ1E7q5kWlQx3c2VWlZr9ycdWKlHpjD25hwJKby4hqPOfWj6WXI2IeGVEZwgVEEumU8-HCvrBmPRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اخرین نماینده اسیا هم حذف شد.
🇪🇬
مصر 1 (4)
🇦🇺
استرالیا 1 (2)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/134877" target="_blank">📅 00:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134876">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✅
✅
ادعای رسول خطیبی:
🔴
زنوزی مالک باشگاه تراکتور بچه بازه و همجنسگراست!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/134876" target="_blank">📅 23:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134875">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
❌
پرسپولیس حاضره تا ۲ برابر سقف قراردادش به احمد نوراللهی پیشنهاد بده/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/134875" target="_blank">📅 23:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134874">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9537d57a20.mp4?token=mOiCRNutIMpL6tk1tcaGhHYbDODWE4aNf6YuuNdni9pBrwLQB7fXeXJH7QF9olfPP9V5869YeaOQvSu5bI27ZPVaPZVnAS4xAPzQ7bXR2KHuWfuFqLGp7GJfCD0jm6PFHflVxIrKOmlI6xnAuI-Dh2jzlVVWLj2ZXLxgggbQvIU5uWP-tLaDrhoB75eKx3idVZnl-DOcaIJ4PjDamF9blpmDMFqgA3yRIYfrqvwbNIVS_AK-7e8_9hFRy2FCwf9zrqZCYkD4-Hox4LQRinkx_BBzI5468gaxM0VztZ0tknKJAgwdTZn_dJw4EzT6dORVxBduh4uOb06iXpVIskNwlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9537d57a20.mp4?token=mOiCRNutIMpL6tk1tcaGhHYbDODWE4aNf6YuuNdni9pBrwLQB7fXeXJH7QF9olfPP9V5869YeaOQvSu5bI27ZPVaPZVnAS4xAPzQ7bXR2KHuWfuFqLGp7GJfCD0jm6PFHflVxIrKOmlI6xnAuI-Dh2jzlVVWLj2ZXLxgggbQvIU5uWP-tLaDrhoB75eKx3idVZnl-DOcaIJ4PjDamF9blpmDMFqgA3yRIYfrqvwbNIVS_AK-7e8_9hFRy2FCwf9zrqZCYkD4-Hox4LQRinkx_BBzI5468gaxM0VztZ0tknKJAgwdTZn_dJw4EzT6dORVxBduh4uOb06iXpVIskNwlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
😐
میثاقی امشب به سیم آخر زد و شماره موبایل اصلی خودش رو به صورت کامل روی آنتن زنده اعلام کرد تا مردم بهش پیامک بزنن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/134874" target="_blank">📅 23:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134873">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
❌
اسکوچیچ برای خودش ۱۸۵۰ میخواهد به اضافه ۲۰٪ آپشن. همچنین برای دستیاراش ۴۰۰ تا میخواهد و گفته مالیات خودم و دستیارانم را باید باشگاه پرداخت کند
🚩
مجموع این ارقام ۳ میلیون دلار میشود.
✅
✅
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/134873" target="_blank">📅 22:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134872">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
پرسپولیس و اسکوچیچ به توافق رسیده اند و تنها بر سر مبلغ قرارداد اختلاف دارند.
🗣
🗣
سایر موانع و مشکلات جذب این مربی کروات، حل شده است. باشگاه از اسکوچیچ تخفیف می خواهد و او تخفیف هم داده است، اما باشگاه باز هم می گوید باید از قرارداد کاسته شود.
🔻
🔻
مسئولان…</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/134872" target="_blank">📅 22:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134871">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✔️
✔️
✔️
مدیران پرسپولیس پروژه فسخ بازیکنان را کلید زدند
❌
از عملکرد امید عالیشاه اصلا راضی نبودند ؛ ومرتضی پورعلی‌ گنجی، میلاد سرلک ، رضا شکاری ، تیوی بیفوما و  دنیل گرا  بازیکنانی هستند که نامشان در لیست سیاه باشگاه دیده می‌شود. مدیران پرسپولیس چند گزینه جوان…</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/134871" target="_blank">📅 22:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134870">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">#تکمیلی
🔴
💥
یحیی گل محمدی به محسن خلیلی گفته من تا شنبه میتونم صبر کنم از یکشنبه اگر منو بخایید باید ۳۰۰ هزار دلار به دهوک عراق پول بدید رضایت نامه منو بگیرید.
🫦
قابل توجه اون کصخول هایی که میگن نه یحیی نمیاد تیم داره با اسم امپرور بازی نکنید  #نه_به_مربی_ایرانی…</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/134870" target="_blank">📅 22:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134869">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
🚨
پرسپولیس 48 ساعت برای اسکوچیچ صبر میکنه، اگه پیش نویس قرارداد رو امضا کرد که هیچی کار تمومه، اگه امضا نکرد میرن سراغ گزینه بعدی / آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/134869" target="_blank">📅 21:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134868">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
پرسپولیس و اسکوچیچ به توافق رسیده اند و تنها بر سر مبلغ قرارداد اختلاف دارند.
🗣
🗣
سایر موانع و مشکلات جذب این مربی کروات، حل شده است. باشگاه از اسکوچیچ تخفیف می خواهد و او تخفیف هم داده است، اما باشگاه باز هم می گوید باید از قرارداد کاسته شود.
🔻
🔻
مسئولان…</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/134868" target="_blank">📅 21:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134867">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دوستان بهترین کانال آنالیز ایران رو از دست ندید
هر روز فقط یک گزینه مطمئن می‌ذاریم، بدون ریسک‌های الکی.
بازی امروز: کانادا – مراکش</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/134867" target="_blank">📅 21:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134866">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">⚽️
جام جهانی ۲۰۲۶؛ وقتی تحلیل درست، سود می‌سازد!
این‌بار نوبت جدال
کانادا
🇨🇦
– مراکش
🇲🇦
است؛ مسابقه‌ای که آمارش یک نکته مهم را نشان می‌دهد:
«مجموع گل بیشتر از ۱.۵» یک انتخاب کاملاً منطقی و ارزشمند است.
دلایل:
✅
کانادا مقابل تیم‌های سرعتی بازی بازتری ارائه می‌دهد.
✅
مراکش استاد ضدحملات سازمان‌یافته و استفاده از فضاهای پشت دفاع است.
✅
اگر یک گل زودهنگام ثبت شود، ریتم مسابقه کامل عوض می‌شود و راه برای گل دوم باز می‌شود.
ما فقط احساسات را تحلیل نمی‌کنیم؛
داده و روندها
حرف اول را می‌زنند.
❤️
برای دسترسی به دقیق‌ترین پیش‌بینی‌های جام جهانی، همین حالا عضو شوید:
👇
👇
👇
https://t.me/+iIi9FxzzcYBjNDg8
https://t.me/+iIi9FxzzcYBjNDg8</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/134866" target="_blank">📅 21:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134865">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
❌
بازی های امشب
🇦🇺
استرالیا_مصر
🇪🇬
🔸
ساعت 21:30
🇦🇷
آرژانتین_کیپ ورد
🇨🇻
🔸
ساعت 01:30
🇨🇴
کلمبیا_غنا
🇬🇭
🔸
ساعت 05:00
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/134865" target="_blank">📅 20:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134864">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✅
🏆
برنامه کامل بازی‌های ۱/۱۶ نهایی جام جهانی
🇿🇦
آفریقا جنوبی - کانادا
🇨🇦
🇧🇷
برزیل - ژاپن
🇯🇵
🇳🇱
هلند - مراکش
🇲🇦
🇺🇸
آمریکا - بوسنی
🇧🇦
🇳🇴
نروژ - ساحل عاج
🇮🇪
🇫🇷
فرانسه - سوئد
🇸🇪
🇩🇪
آلمان - پاراگوئه
🇵🇾
🇲🇽
مکزیک - اکوادور
🇪🇨
🇧🇪
بلژیک - سنگال
🇸🇳
🇪🇸
اسپانیا - اتریش…</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/134864" target="_blank">📅 20:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134863">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
❌
خبرگزاری تسنیم:
🔹
تنها مانع عقد قرارداد اسکوچیچ با پرسپولیس اختلاف مالیه که همچنان پابرجاست
🔹
مدیریت پرسپولیس خواستار تخفیف چند صدهزار دلاری شده
🔹
اگه توافق با او صورت نگیره احتمالا گزینه ایرانی مدنظر باشگاه خواهد بود  «سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/134863" target="_blank">📅 20:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134858">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
پیروز قربانی: من نیوزلند رو با فجر سپاسی شیراز می‌بردم مطمئن باشید نیوزلند اگه تو لیگ 16 تیمی ما بود، جزو چهار تیم آخر میشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/134858" target="_blank">📅 19:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134857">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
زنوزی، مالک باشگاه تراکتور به صورت شخصی با مرتضی پورعلی گنجی، مدافع پرسپولیس وارد مذاکره شده تا این بازیکن راهی تبریز شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/134857" target="_blank">📅 18:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134856">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇹🇳
یک اتفاق عجیب برای تونسی‌ها در جام جهانی؛
❌
دوپینگ ۸ بازیکن مثبت شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/134856" target="_blank">📅 18:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134855">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🏆
جدول نهایی گروه F جام جهانی ۲۰۲۶
🇳🇱
صعود هلند به عنوان تیم اول
🇯🇵
صعود ژاپن به عنوان تیم دوم
🇸🇪
صعود سوئد به عنوان تیم سوم
🇹🇳
حذف تونس به عنوان تیم چهارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/134855" target="_blank">📅 18:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134854">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
🎙
رسول خطیبی: محمدرضا زنوزی، پس از باخت ۴-۲ تراکتور مقابل استقلال در تبریز، جشن گرفته بود!
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/134854" target="_blank">📅 18:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134853">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
❌
ابوالفضل جلالی که قراردادش با استقلال تموم شده، دوست داره به پرسپولیس بره. چون بازیکن آزاده، پرسپولیس شرایط جذبش رو بررسی می‌کنه، اما تصمیم نهایی رو سرمربی جدید تیم می‌گیره.
🔴
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/134853" target="_blank">📅 18:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134852">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❗️
❗️
فوری؛ شنیده ها: ابواالفضل جلالی خودش رو به پرسپولیس لینک کرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/134852" target="_blank">📅 18:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134851">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✅
نساجی مازندران به لیگ برتر بازگشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/134851" target="_blank">📅 18:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134850">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✅
✅
🔴
باشگاه پرسپولیس: هیچکس از مدیران باشگاه به هیچ عنوان با خداداد عزیزی حتی یک تماس هم نگرفته و خداداد حتی گزینه هم نبوده و فقط از طریق لابی و رسانه ها خودش رو گزینه پرسپولیس کرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/134850" target="_blank">📅 18:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134849">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from"mehran"</strong></div>
<div class="tg-text">اگه برگردیم به دوران یحیی بدبخت میشیم
بزور امثال پاکدل و دهقان و ابراهیمی و نعمتی و صادقی و فرجی و عیسی و خیلیای دیگه رو بیرون کردیم
تازه هنوز ی سریاش تو تیم هستن مث سرلک کنه</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/134849" target="_blank">📅 17:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134848">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">یحیی بیاد که دوباره باندبازها توی تیم بموننن و دلالی باهمدیگه</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/134848" target="_blank">📅 17:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134847">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #افشاگری
⚠️
🔴
به گزارش رسانه «سرخ تایمز» محسن خلیلی معاونت ورزشی باشگاه پرسپولیس در ۲۴ ساعت گذشته سخت به تکاپو افتاده و دنبال آوردن یحیی گل محمدی به پرسپولیسه؛تنها شخصی که تو باشگاه خیلی سفت سخت داره تمام زورشو میزنه تا مربی ایرانی بیاد…</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/134847" target="_blank">📅 17:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134846">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
❌
خبرگزاری تسنیم:
🔹
تنها مانع عقد قرارداد اسکوچیچ با پرسپولیس اختلاف مالیه که همچنان پابرجاست
🔹
مدیریت پرسپولیس خواستار تخفیف چند صدهزار دلاری شده
🔹
اگه توافق با او صورت نگیره احتمالا گزینه ایرانی مدنظر باشگاه خواهد بود  «سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/134846" target="_blank">📅 17:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134845">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
|
#افشاگری
⚠️
🔴
به گزارش رسانه «سرخ تایمز» محسن خلیلی معاونت ورزشی باشگاه پرسپولیس در ۲۴ ساعت گذشته سخت به تکاپو افتاده و دنبال آوردن یحیی گل محمدی به پرسپولیسه؛تنها شخصی که تو باشگاه خیلی سفت سخت داره تمام زورشو میزنه تا مربی ایرانی بیاد علی الخصوص که اون شخص یحیی گل محمدی باشه همین آقای خلیلی هست!
#نه_به_مربی_ایرانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/134845" target="_blank">📅 17:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134844">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اسکوچیچ امضا کرده و الان رسما سرمربی پرسپولیسه/طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/134844" target="_blank">📅 16:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134843">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❗️
❗️
میثاقی: قرارداد پرسپولیس برای اسکوچیچ ارسال شده، روی مبلغ قرارداد یه چند صدهزار دلاری اختلاف دارن  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/134843" target="_blank">📅 16:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134842">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
❌
خبرگزاری تسنیم:
🔹
تنها مانع عقد قرارداد اسکوچیچ با پرسپولیس اختلاف مالیه که همچنان پابرجاست
🔹
مدیریت پرسپولیس خواستار تخفیف چند صدهزار دلاری شده
🔹
اگه توافق با او صورت نگیره احتمالا گزینه ایرانی مدنظر باشگاه خواهد بود  «سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/134842" target="_blank">📅 16:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134841">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❗️
فووووووووری؛ تکلیف نیمکت پرسپولیس تا هفته آینده مشخص میشه. باشگاه از اوسمار تخفیف خواسته اونم موافقت کرده ولی میزان تخفیف رو اعلام نکرده/ فارس   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/134841" target="_blank">📅 16:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134840">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
❌
خداداد عزیزی: ایرادات و مشکلاتی در پرسپولیس هست که این تیم را دچار بحران و حاشیه کرده است و تا حالا این مدل کار کردن رو ندیده بودم. در صورتی که در تراکتور همه چیز با یک زنگ به زنوزی حل میشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/134840" target="_blank">📅 15:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134839">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✅
✅
واکنش زنوزی به انتقال اسکوچیچ به پرسپولیس: اسکوچیچ مربی بزرگیه و تونست تراکتور رو قهرمان کنه اما او بدون ابزار قهرمانی نمیتونه در یک تیم معمولی دوباره قهرمان بشه!!!!!!
🔴
🔴
پ.ن آقای حدادی آقایون بانک شهر بهتون بربخورههههه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/134839" target="_blank">📅 15:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134838">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✅
✅
بازگشا سخنگوی پرسپولیس در مورد روند مذاکرات با اسکوچیچ :
❌
❌
تصمیم‌گیری، مذاکره، تفاهم، عقد قرارداد و امضای توافق با یک سرمربی در شأن باشگاه، نیازمند جلسات متعدد، بررسی‌های دقیق و رفت‌وبرگشت‌های فراوان است. اطلاع‌رسانی لحظه‌به‌لحظه درباره روند مذاکرات و چالش‌های…</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/134838" target="_blank">📅 15:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134837">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
بازگشا: به یه ضد پرسپولیسی داخل باشگاه اجازه موندن ندادیم. هوادار مالک باشگاهه، از هوادار سواستفاده نکنید که بمونید و کنار تیم دلالی کنید. آخرین اخطاره باج نمیدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/134837" target="_blank">📅 14:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134836">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/134836" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/134836" target="_blank">📅 14:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134835">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">💛
هنوز توی MelBet با این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
بعد میاید سوال میکنید کدوم سایت معتبره
❗️
👀
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
✔️
🎚️
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/134835" target="_blank">📅 14:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134834">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❗️
❗️
درحالیکه استقلال ، سپاهان و تراکتور تمرینات شون برای فصل جدید شروع کردن اما خبری از شروع تمرینات پرسپولیس نه تنها نیست بلکه حتی تکلیف نیمکت هم مشخص نیست!
🔴
🔴
حدادی داره کاری میکنه تا دلمون برای درویش تنگ بشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/134834" target="_blank">📅 12:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134833">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
🔴
فووووری؛ رضا شکاری از پرسپولیس جدا شد و به زودی‌ لژیونر میشه. تیم جدید شکاری در قاره آسیا خواهد بود/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/134833" target="_blank">📅 12:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134832">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✔️
✔️
✔️
مدیران پرسپولیس پروژه فسخ بازیکنان را کلید زدند
❌
از عملکرد امید عالیشاه اصلا راضی نبودند ؛ ومرتضی پورعلی‌ گنجی، میلاد سرلک ، رضا شکاری ، تیوی بیفوما و  دنیل گرا  بازیکنانی هستند که نامشان در لیست سیاه باشگاه دیده می‌شود. مدیران پرسپولیس چند گزینه جوان…</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/134832" target="_blank">📅 12:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134831">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
❌
خداداد عزیزی: ایرادات و مشکلاتی در پرسپولیس هست که این تیم را دچار بحران و حاشیه کرده است و تا حالا این مدل کار کردن رو ندیده بودم. در صورتی که در تراکتور همه چیز با یک زنگ به زنوزی حل میشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/134831" target="_blank">📅 12:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134830">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
🔴
خداداد عزیزی:علیرضا دبیر اصرار می‌کرد برم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/134830" target="_blank">📅 12:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134829">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
🔴
دلیل ناراحتی اسکوچیچ از پرسپولیس اینه که قرار بوده باشگاه بهش پیش‌پرداخت بده که تا الان این اتفاق نیوفتاده/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/134829" target="_blank">📅 12:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134828">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❗️
❗️
عصبانیت اسکوچیچ از باشگاه
🔴
🔴
پس از مذاکره اولیه و سپس حضوری در استانبول، اسکوچیچ در انتظار ارسال قرارداد بود که این موضوع از سوی باشگاه چند بار به تاخیر افتاد و باعث دلخوری اسکوچیچ شد. هنوز هم به شکلی عجیب و سوال برانگیز در ۲۴ ساعت گذشته این اتفاق رخ نداده…</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/134828" target="_blank">📅 12:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134827">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فووووووووووووری
🔻
احمد نوراللهی در آستانه بازگشت به پرسپولیس/خبرورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/134827" target="_blank">📅 12:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134826">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
❌
#فوری
🗣
حضور کسری طاهری در پرسپولیس منتفی شد / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/134826" target="_blank">📅 11:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134825">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✅
با اعلام ترانسفر مارکت محمد قربانی بازیکن آزاد اعلام‌ شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/134825" target="_blank">📅 11:17 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
