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
<img src="https://cdn4.telesco.pe/file/RYVg_D7F-GDBpBN6IFQk2FyJlSbjNmnaTwtU-Fdwn-DN-vGkBRMxecM1sqCwH8bWl04Tc3S-1nnxYtY933MrVGo1HslxVx8FMB9DeXNC9uZyzDHEBztt0JsLEav2mTxmOZ_Zh6FvQfAzxQpndZyNn66yVAZxbYkIgocm91fIQue0klg5baEttwf235kTItZfZovngFfhkq3UJ_Uuv4D8P7BRPsZ6cBdYgDz9Y-nPT6M0LMokUKYSl6EBTA_FuSEh3PfXv52mc6uscqPceypki8lS8NMSYXqDk2UwQqOU4ZxbMw_WMBRoKQdXAan9cSmBJ0ePf-txkEzEMoaYzPj2Xg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 22:44:31</div>
<hr>

<div class="tg-post" id="msg-134361">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❌
این همه اصرار واسه برگزاری این تورنمنت واسه چی بود؟این چه تیمیه آقای اوسمار .چادر ملو چهارماه هیچ تمرینی نداشته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 519 · <a href="https://t.me/SorkhTimes/134361" target="_blank">📅 22:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134360">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❗️
❗️
بازی همون یک بر یک تمام شد ...کسی نمیدونه می‌ره وقت اضافه یا می‌ره پنالتی ....خود شبکه سه هم از دو قاب خسته شد ....معلوم نیست ادامه بازی و کجا نشون میده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 851 · <a href="https://t.me/SorkhTimes/134360" target="_blank">📅 22:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134359">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❗️
❗️
بازی همون یک بر یک تمام شد ...کسی نمیدونه می‌ره وقت اضافه یا می‌ره پنالتی ....خود شبکه سه هم از دو قاب خسته شد ....معلوم نیست ادامه بازی و کجا نشون میده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 975 · <a href="https://t.me/SorkhTimes/134359" target="_blank">📅 22:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134358">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
شکاری و خدابنده لو میان داخل ..سرلک و بیفوما اومدن بیرون ...بازی و باید تو نود دقیقه تموم کنیم .وگرنه ضربات پنالتی همیشه بد بودیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/SorkhTimes/134358" target="_blank">📅 22:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134357">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
🔴
تیمی که پنج ماهه تمرین نکرده به ما گل زد و بازی مساوی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/SorkhTimes/134357" target="_blank">📅 21:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134356">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
پایان نیمه اول  پرسپولیس 1 چادرملو 0
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/SorkhTimes/134356" target="_blank">📅 21:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134355">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
ویژه‌ برنامه اختصاصی این مسابقه با حضور دکتر پیمان حدادی، مدیرعامل باشگاه پرسپولیس و حامد کاویانپور، پیشکسوت پرسپولیس، از ساعت ۱۹:۳۰ به صورت زنده از طریق صفحات رسمی باشگاه در اینستاگرام و روبیکا آغاز خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/SorkhTimes/134355" target="_blank">📅 21:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134354">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❗️
تا این لحظه با توجه به انصراف گلگهر از حضور در تورنمت آسیایی برنده دیدار پرسپولیس و چادرملو به سطح دوم لیگ قهرمانان آسیا راه پیدا میکند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/SorkhTimes/134354" target="_blank">📅 21:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134353">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✅
پایان نیمه اول  پرسپولیس 1 چادرملو 0
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/SorkhTimes/134353" target="_blank">📅 21:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134352">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‼️
گل اول پرسپولیس به چادرملو توسط محمدامین کاظمیان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/SorkhTimes/134352" target="_blank">📅 21:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134351">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✅
والیبال هم به باخت عادت کردیم ...دیشب به فرانسه ..امشب هم به آمریکا باختیم ..برد والیبال شده آرزو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/SorkhTimes/134351" target="_blank">📅 21:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134350">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c5878d1c1.mp4?token=g0YQzutPR81vBNT5RPRpwHYAcMmgX6SuGYGv72ro4iAFzNUp5brRfWSYFc2-xz-BVDWsw8NUlGZGVPt-q-_NUdmWi22qzY4BGYPAcn4FKqlco7jmhgbJ75nXjs4NeTaTiYigcdg-gaqnQinImdP0Kqswdgo4CVdBBNCs88-KglHQRSWo7tp8JCRXAlrlImTvW3oAAq-zin3WjTuzAZBAxVNQGHnn9xKCxAc4Gynk_I1vj2fqt15r1y69hJxgJaHyARsA9lGuMciMG2WIcU-GMzpBB3XjS4--XXeXUmHozW6NrVy5R9Zp4YFeQGrDZZe31F1PLcEwEfeQj682MJYdgw45ALkPLmIEa8wsw5WVNluEFulJxJRBA1HX1zj7akjN6h5MUWQLYa0G-kk2D7WMqpDu92qJM_Hy2WtKkKd0YYSy38vvcas87RLGhRGhQ1nalqhIq9Qe7nfsNODcUCGNqnHwF42ac_3ko-joqYm9TM0SSxOEwn-q7wjFws_7Yxaa0e1n7HyRe6X0qVSJEYOd-GMnwgvt7FfbbcOAuxje8ABPvYMe3bmp8i22lY4Qxc5H0uVviDvrN2iENzvdY7SqeQNl27p9ZXdXGFAnyLRrcDiApBA1catYUKEd9o0CaokmSjSLD-WWzhTFb4Rthoq02zZZ82xzTvJa15IzYC8gz30" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c5878d1c1.mp4?token=g0YQzutPR81vBNT5RPRpwHYAcMmgX6SuGYGv72ro4iAFzNUp5brRfWSYFc2-xz-BVDWsw8NUlGZGVPt-q-_NUdmWi22qzY4BGYPAcn4FKqlco7jmhgbJ75nXjs4NeTaTiYigcdg-gaqnQinImdP0Kqswdgo4CVdBBNCs88-KglHQRSWo7tp8JCRXAlrlImTvW3oAAq-zin3WjTuzAZBAxVNQGHnn9xKCxAc4Gynk_I1vj2fqt15r1y69hJxgJaHyARsA9lGuMciMG2WIcU-GMzpBB3XjS4--XXeXUmHozW6NrVy5R9Zp4YFeQGrDZZe31F1PLcEwEfeQj682MJYdgw45ALkPLmIEa8wsw5WVNluEFulJxJRBA1HX1zj7akjN6h5MUWQLYa0G-kk2D7WMqpDu92qJM_Hy2WtKkKd0YYSy38vvcas87RLGhRGhQ1nalqhIq9Qe7nfsNODcUCGNqnHwF42ac_3ko-joqYm9TM0SSxOEwn-q7wjFws_7Yxaa0e1n7HyRe6X0qVSJEYOd-GMnwgvt7FfbbcOAuxje8ABPvYMe3bmp8i22lY4Qxc5H0uVviDvrN2iENzvdY7SqeQNl27p9ZXdXGFAnyLRrcDiApBA1catYUKEd9o0CaokmSjSLD-WWzhTFb4Rthoq02zZZ82xzTvJa15IzYC8gz30" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گل اول پرسپولیس به چادرملو توسط محمدامین کاظمیان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SorkhTimes/134350" target="_blank">📅 21:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134349">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
این شبکه ورزش و برا چی راه انداختین پس یا والیبالو پخش کنید یا فوتبال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/SorkhTimes/134349" target="_blank">📅 20:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134348">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
نمایی از تمرینات پرسپولیس در حضور وحید امیری و با اضافه شدن تیوی بیفوما، محمدحسین صادقی و فرزین معامله‌گری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/SorkhTimes/134348" target="_blank">📅 20:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134347">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✅
✅
دو قاب شد .بریم برای بازی مهم پرسپولیس بعد از مدت ها .الهی به امید تو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/SorkhTimes/134347" target="_blank">📅 20:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134346">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❗️
والیبال طول کشیده .شبکه سه نمیدونه قطع کنه بره فوتبال یا نه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SorkhTimes/134346" target="_blank">📅 20:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134345">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
❌
پنج دقیقه تا بازی چادرملو و پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SorkhTimes/134345" target="_blank">📅 20:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134344">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✅
مرتضی پورعلی‌گنجی کاپیتان امروز پرسپولیس در دیدار مقابل چادرملو میباشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SorkhTimes/134344" target="_blank">📅 20:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134343">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">💢
گرم کردن عالیشاه و دیگر بازیکنان پرسپولیس قبل از مسابقه با چادرملو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SorkhTimes/134343" target="_blank">📅 20:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134342">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0c0f66cfd.mp4?token=K9hxUkzWJOMgbK65ImKmK0TIROw4qBevKo24mztr0KmcuTTTIN1zqDQ--GAsLuEz0fkTmQBPuRkX41KHeZGtcsz1rEIfJ943zYCR6vgHw_Zikkl48AoYhF-uF7_vsnNQK3NjaE7a5Inkl0Qgv-Czpoo0Sd86aZ6j986_aVYwJy-Kol7rXnWZwXRe1e3I9_CXcMRshahPEiRQdZEz6RhZXIvvNPf1aoqvl4Qk90zNd3kHLsDAfRiViyPEhY73VNhGNZ5xfOrA2STsdGKD1PQgJGyh0ruxRiz8_FhSdMbsPUt6Er9Ru1N6a3B4DhUwo_cEtzAX399Lp7FwiyeRBfVTYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0c0f66cfd.mp4?token=K9hxUkzWJOMgbK65ImKmK0TIROw4qBevKo24mztr0KmcuTTTIN1zqDQ--GAsLuEz0fkTmQBPuRkX41KHeZGtcsz1rEIfJ943zYCR6vgHw_Zikkl48AoYhF-uF7_vsnNQK3NjaE7a5Inkl0Qgv-Czpoo0Sd86aZ6j986_aVYwJy-Kol7rXnWZwXRe1e3I9_CXcMRshahPEiRQdZEz6RhZXIvvNPf1aoqvl4Qk90zNd3kHLsDAfRiViyPEhY73VNhGNZ5xfOrA2STsdGKD1PQgJGyh0ruxRiz8_FhSdMbsPUt6Er9Ru1N6a3B4DhUwo_cEtzAX399Lp7FwiyeRBfVTYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
گرم کردن عالیشاه و دیگر بازیکنان پرسپولیس قبل از مسابقه با چادرملو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SorkhTimes/134342" target="_blank">📅 20:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134341">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
ترکیب پرسپولیس در دیدار امروز برابر چادرملو
🛜
سیستم پایه:۴۴۲
❤️
امیر رضا دفیعی
❤️
حسین ابرقویی
❤️
مرتضی پورعلی‌گنجی
❤️
فرزین معامله‌گری
❤️
دنیل گرا
❤️
میلاد سرلک
❤️
مارکو باکیچ
❤️
تیوی بیفوما
❤️
محمد عمری
❤️
یاسین سلمانی
❤️
محمد امین کاظمیان
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SorkhTimes/134341" target="_blank">📅 20:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134340">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/215ef22d08.mp4?token=ddODNhr8MK7UB1wfpRSxa19o3htHdPyU-nTXP4B833zpdfWVVNJMtJJAN17BLLSUfpyWUXMUk5_MYY62ZYpL3y7Mx5cnRtFugZ_OcrEnPr-huXRwVunv2p_GIaJLZwuOnhGIR8lH4Oi21zzaRt9XuOY8l7lN8ldDQfBG0Tunr1kuFU2PBfHUeuOGyi5fHJV8qz6KddAzarVudzch5gsmEl_YnwokZCQEXe6h7f5GSU5Plps9G7do5zCYi49GIi325CdDs3RT8e2Ul6CaaCJ7buZQCZcMUP3YgtL4Umt45dJQJdUugPjKb1yoHXwZXah9PCEbRL3YxLyl9gwrbiajWoFmC4vBCowPurX7KAicZPxRaPXcuZ124wy9XeV0V6ZKUwViopPM-w9wUJsTgNJyaaOw_1rzrM-9ZFyD4U0cUQeUI071zPqdDnOp7n3cmCNsiHRE1pTdw2WxTBZvJWy0qfnhvULC1po6Exw4xPOcYjChQRABbZonkPMPR8ffpNre3UgsptnhhPdG_c6hBgdBS-DPHHeUqQC3gEattc8iy0-p9L_lS52no7C69BrFJQaB5arB4YMH_QTIsamw5PrUJr3TXyEHzw9_b1ELbnrAVb2CQmCNJ1XxoI6NOgZXg7I-6kqfG2RpOAkzbIaE8B0hVQPgjiWSBwsWJcxwz8rwxnU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/215ef22d08.mp4?token=ddODNhr8MK7UB1wfpRSxa19o3htHdPyU-nTXP4B833zpdfWVVNJMtJJAN17BLLSUfpyWUXMUk5_MYY62ZYpL3y7Mx5cnRtFugZ_OcrEnPr-huXRwVunv2p_GIaJLZwuOnhGIR8lH4Oi21zzaRt9XuOY8l7lN8ldDQfBG0Tunr1kuFU2PBfHUeuOGyi5fHJV8qz6KddAzarVudzch5gsmEl_YnwokZCQEXe6h7f5GSU5Plps9G7do5zCYi49GIi325CdDs3RT8e2Ul6CaaCJ7buZQCZcMUP3YgtL4Umt45dJQJdUugPjKb1yoHXwZXah9PCEbRL3YxLyl9gwrbiajWoFmC4vBCowPurX7KAicZPxRaPXcuZ124wy9XeV0V6ZKUwViopPM-w9wUJsTgNJyaaOw_1rzrM-9ZFyD4U0cUQeUI071zPqdDnOp7n3cmCNsiHRE1pTdw2WxTBZvJWy0qfnhvULC1po6Exw4xPOcYjChQRABbZonkPMPR8ffpNre3UgsptnhhPdG_c6hBgdBS-DPHHeUqQC3gEattc8iy0-p9L_lS52no7C69BrFJQaB5arB4YMH_QTIsamw5PrUJr3TXyEHzw9_b1ELbnrAVb2CQmCNJ1XxoI6NOgZXg7I-6kqfG2RpOAkzbIaE8B0hVQPgjiWSBwsWJcxwz8rwxnU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
میرشاد ماجدی: پرسپولیس و چادرملو برای انجام مسابقات ٣ جانبه موافقت کرده‌اند اما نمی‌دانم تکلیف گل‌گهر چه خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/SorkhTimes/134340" target="_blank">📅 20:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134339">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvI2D2pUENKWo54OLW3BUy3kaHWmrKZBT8Jh3G5_w5oaZaoLnLr79nPUBvlT3RG6vwZaBtDiGvMHeYDMPpfh5UCRm7m-Yazbl5RwinUkUL6FlMCEcPVxoN5Onqpx7wOLt4brzACePvk6Z07B8dGpRqZUhDQXOStNM1dyc5YyEVm0-OJVJu5hMQB0ab2-02t1uFbScA6W6gVHknRapGmUzICJiy5YLyIIs1qFcYRHPa1ZvLGmaZH6HTVcWZNRbrQhHbDz48oJCBWE8RFbX6TCZcfoI9cP5izygLeIWSDJegktTTDl_HiFIaksukMOErhh8G0SVE4GgqDlKnCMEbXaOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
⚽️
گروه G جام‌جهانی ۲۰۲۶
[
مصر
🇪🇬
🆚
🇮🇷
ایران
]
⏰
بامداد جمعه ساعت ۰۶:۳۰
🏟
استادیوم
لومن فیلد سیاتل
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
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/SorkhTimes/134339" target="_blank">📅 20:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134338">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇮🇷
🇪🇬
🏆
دیدار بین ایران و مصر در سیاتل از سوی کمیته محلی برگزاری این دیدار از جام جهانی بعنوان"مسابقه افتخار"(Pride Match)برای همجنس‌گرایان نامیده شد!
‼️
‼️
پ.ن:طارمی و صلاح باید بازوبندی رنگین کمون(همجنس گرایی)ببندن.
🫣
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SorkhTimes/134338" target="_blank">📅 19:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134337">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❗️
ترکیب چادرملو مقابل پرسپولیس اعلام شد.
❌
امیر حسین آسیابان پور؛سعید محمدی فرد؛سید محمدرضا حسینی؛سیروس صادقیان؛محمد حسین فلاح؛مبین قوچی؛علیرضا صفری؛محمد حسین خسروی؛ایلیا نگهداری؛امیر رضا اسلام طلب و رضا میرزایی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SorkhTimes/134337" target="_blank">📅 19:57 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134336">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
ترکیب پرسپولیس در دیدار امروز برابر چادرملو
🛜
سیستم پایه:۴۴۲
❤️
امیر رضا دفیعی
❤️
حسین ابرقویی
❤️
مرتضی پورعلی‌گنجی
❤️
فرزین معامله‌گری
❤️
دنیل گرا
❤️
میلاد سرلک
❤️
مارکو باکیچ
❤️
تیوی بیفوما
❤️
محمد عمری
❤️
یاسین سلمانی
❤️
محمد امین کاظمیان
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SorkhTimes/134336" target="_blank">📅 19:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134335">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
ترکیب پرسپولیس در دیدار امروز برابر چادرملو
🛜
سیستم پایه:۴۴۲
❤️
امیر رضا دفیعی
❤️
حسین ابرقویی
❤️
مرتضی پورعلی‌گنجی
❤️
فرزین معامله‌گری
❤️
دنیل گرا
❤️
میلاد سرلک
❤️
مارکو باکیچ
❤️
تیوی بیفوما
❤️
محمد عمری
❤️
یاسین سلمانی
❤️
محمد امین کاظمیان
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/SorkhTimes/134335" target="_blank">📅 19:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134334">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✅
حدادی ساعت ۱۷.۴۵ مهمون شبکه تلویزیونی پرسپولیسه و احتمالا تکلیف مربی مشخص بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/134334" target="_blank">📅 18:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134333">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
خلاصه آخرین تقابل پرسپولیس و چادرملو که با تک گل امیرحسین محمودی به نفع سرخپوشان به پایان رسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/134333" target="_blank">📅 17:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134332">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
شنیده ها: یاسین سلمانی در ترکیب رسمی تیم جایگزین عالیشاه میشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/134332" target="_blank">📅 16:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134331">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
دراگان اسکوچیچ پس از دو بازی تورنمنت آسیایی رسما و شرعا سرمربی پرسپولیس میشه/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/134331" target="_blank">📅 16:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134330">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
❌
با اعلام رسمی سازمان لیگ، به دلیل درخواست شبکه سه سیما برای پخش مسابقه تیم ملی والیبال کشورمان مقابل ژاپن، ساعت بازی دو تیم چادرملو اردکان و‌ پرسپولیس تغییر کرد.
🔴
🔴
به این ترتیب مسابقه دو تیم چادرملو اردکان و پرسپولیس امروز ۵ تیر به جای ساعت ۱۸:۴۵ در ساعت…</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/134330" target="_blank">📅 16:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134329">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
پرسپولیس با ارسال پیشنهادی به ملوان خواهان جذب فرهان جعفری 20 ساله شد
🔴
این بازیکن 2 پیشنهاد از خارج کشور و سپاهان و تراکتور هم داره
🔴
جعفری با امار 5 دریبل و 3 پاس کلیدی در هربازی بهترین هافبک هجومی لیگ برتر شناخته شده
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/134329" target="_blank">📅 15:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134328">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❗️
فردا 6/30 صبح بازی حساس ایران آغاز میشه .کیا بیدار میشن که ببینن ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/134328" target="_blank">📅 15:57 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134327">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❗️
امید عالیشاه سه روز پیش مصدوم شده و تمرینات اختصاصی رو انجام میده و گفته میشه امروز از رو سکو‌ها کار رو دنبال میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/134327" target="_blank">📅 15:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134326">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✅
۴ ماه از آخرین بازی رسمی پرسپولیس می‌گذره و امروز قراره دلتنگی مون به پایان برسه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/134326" target="_blank">📅 15:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134324">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOPvwKtdAQ43qdBXjOYlHRUXPn4OQF6rretoziIYZY3JQBD6PDvVOXoOEIi9zOMhVFFXut1tH7Vx34jRaVjxD_cknk4XIMRlDX3F4dCTC_FsXh6e5pWCdTx6349hMZB9buHSCRa5_HBYLYU_y8f75a-RuO_1l7mraAUTeeX03w1TIqQ-xBUKdroTNfpiwlP5vUgj5gJUyCzxgfv217q4kCOHA-UGYet-Vgq9-8L9WRUp7j_ZFIFjKDfwk6hl5J3zUL-uhmqMRFIX9Nq8uE-xIaEJv3_u0cp5puGFexdUwaCl5bbYc4ACXfa19lWVD34STL6FgxL_Sw8VqL5VWgirjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
⚽️
گروه I جام‌جهانی ۲۰۲۶
[
نروژ
🇳🇴
🆚
🇫🇷
فرانسه
]
⏰
پنجشنبه ساعت ۲۲:۳۰
🏟
استادیوم
ژیلت بوستون
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
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/134324" target="_blank">📅 15:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134323">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjeKb2DA7ElSHA1f6Y6n1XTUFVwNJKn44Dw3BfgwdYEvXaeea7upzutHrHiWg7kbsadrA1Pa9mXDJBUWCzM354PG0LqOAXmnR_4QaxryuFiQBvaQfoKlxHas7C2rz_ZqE-b0PlVIXYopqDesOuBh1J8BzeaGEDuZYr-QN-eD1IGgwxiOt_3CMie33J6mJ7u7Zx2EZ24j5rmLg6E399Ze-xp42ligycVG-K_0DARn4QIQPXWtIWdLVUxI1yCIHM8sUfa-0mfIfDdwcTG6ZD-c2jAJhErWS-7Ndqi2EM2w9L6qKhITbELxKcF4CzIfQZxpyfDeHvamkhfHDdKf47zXEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شنیده ها: یاسین سلمانی در ترکیب رسمی تیم جایگزین عالیشاه میشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/134323" target="_blank">📅 14:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134322">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✅
برنامه بازی‌های بامداد شنبه، جام جهانی 2026
✅
شنبه ۶ تیر :
🕖
3:30 بامداد |
🇨🇻
کیپ ورد
🆚
🇸🇦
عربستان
🕖
3:30 بامداد |
🇺🇾
اروگوئه
🆚
🇪🇸
اسپانیا
🕖
6:30 بامداد |
🇧🇪
بلژیک
🆚
🇦🇺
نیوزلند
🕖
6:30 بامداد |
🇮🇷
ایران
🆚
🇪🇬
مصر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/134322" target="_blank">📅 14:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134321">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
فدراسیون فوتبال: فیفا به ما و فدراسیون مصر قول داده هیچ مراسمی پیش از بازی یا حین بازی در ورزشگاه سیاتل برای حمایت از همجنسگرایان انجام نخواهد داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/134321" target="_blank">📅 14:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134320">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
اوریه از پرسپولیس شکایت کرده و حالا حدادی گفته باشگاه دفاعیه‌ی محکمی ارائه بده و تاکید کنن که بیماریش رو پنهان کرده بود و غیبت غیرموجه در تمرینات داشته/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/134320" target="_blank">📅 14:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134319">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAn-qGpMWGm9FfUwBvjT8Cy2SHGZPNToFew-2OPixhn79kiOsGvjmR4k73xBU6pW9MgTJRVOz_tQ-17mTYlckKPyGgHvarBL6E_Lkn3kjN2Z3xVrakxrDNEDj4hyCE5jbqSKwXJEDpkgG3l0dG7P7XSac_HF14FkhbTRWpVLs2G1cYReJldgpnUd13ygZRvvk2ZhA6azHEuEmifKemlAYhGgGK6J5vUSrds55ArznxtymvLmcyXz8wD-dAI3kVe4Z41U4xFxEf0biKDDgmmfUbLmc2LVgKTQCMX8SyM9vmYRTR6fUmRH0xRwr5jWE-su-H0hsPKOPwc5cq4LUWxKeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
۴ ماه از آخرین بازی رسمی پرسپولیس می‌گذره و امروز قراره دلتنگی مون به پایان برسه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/134319" target="_blank">📅 14:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134318">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
❌
با اعلام رسمی سازمان لیگ، به دلیل درخواست شبکه سه سیما برای پخش مسابقه تیم ملی والیبال کشورمان مقابل ژاپن، ساعت بازی دو تیم چادرملو اردکان و‌ پرسپولیس تغییر کرد.
🔴
🔴
به این ترتیب مسابقه دو تیم چادرملو اردکان و پرسپولیس امروز ۵ تیر به جای ساعت ۱۸:۴۵ در ساعت…</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/134318" target="_blank">📅 14:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134317">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✅
ساعت ۱۸:۴۵ بازی پرسپولیس و چادرملو از شبکه ۳ پخش میشه.و والیبال ایران و ژاپن ساعت 18/30 رفت شبکه ورزش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/134317" target="_blank">📅 13:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134316">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✅
ساعت ۱۸:۴۵ بازی پرسپولیس و چادرملو از شبکه ۳ پخش میشه.و والیبال ایران و ژاپن ساعت 18/30 رفت شبکه ورزش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/134316" target="_blank">📅 13:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134315">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
فدراسیون فوتبال: فیفا به ما و فدراسیون مصر قول داده هیچ مراسمی پیش از بازی یا حین بازی در ورزشگاه سیاتل برای حمایت از همجنسگرایان انجام نخواهد داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/134315" target="_blank">📅 13:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134314">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMYsoCYWDQAUgD2loV_FW05tRRC-kHK4TlRscpd8_zlAi8lImzS3k-DbSKCC3_GI_VKVmsDo_DddVRMRLISXjwQ48UonnhQTa99wTdseU_7SMWL9HQHvKApn1EoLSNZu50RLxJak2lofjBhPMCCMAgBChasFglf3gYDMWwIafCx79W3x-LyjmYXMVBjOzdbfpkp3F9z1okm3Gv10VepwpphNPoAw6OdQBORC9O_MYIHZY8JXag_NTHrnBK3yAKPMzoLFoYN-FBbtusEerlTvJdZ_WC5HF3C3CEJF4UndpL7AHhkFxpySQevABhPTjpzE5XeNxeKW-mGZtQ377tcxQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
فدراسیون فوتبال
: فیفا به ما و فدراسیون مصر قول داده هیچ مراسمی پیش از بازی یا حین بازی در ورزشگاه سیاتل برای حمایت از همجنسگرایان انجام نخواهد داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/134314" target="_blank">📅 13:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134313">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
لیست تیم پرسپولیس برای بازی با چادرملو اردکان
⏺
1_امیررضا رفیعی
⏺
2_محمد گندمی
⏺
3_ حسین ابرقویی
⏺
4_ مرتضی پورعلی‌گنجی
⏺
5_امیرمحمد بخشی
⏺
6_سهیل صحرایی
⏺
7_فرزین معامله‌گری
⏺
8_علیرضا همایی‌فر
⏺
9_دنیل گرا
⏺
10_میلاد سرلک
⏺
11_محمدخدابنده‌لو
⏺
12_مارکو باکیچ
⏺
13_علیرضا…</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/134313" target="_blank">📅 12:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134312">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✅
ساعت ۱۸:۴۵ بازی پرسپولیس و چادرملو از شبکه ۳ پخش میشه.و والیبال ایران و ژاپن ساعت 18/30 رفت شبکه ورزش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/134312" target="_blank">📅 12:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134311">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
لیست تیم پرسپولیس برای بازی با چادرملو اردکان
⏺
1_امیررضا رفیعی
⏺
2_محمد گندمی
⏺
3_ حسین ابرقویی
⏺
4_ مرتضی پورعلی‌گنجی
⏺
5_امیرمحمد بخشی
⏺
6_سهیل صحرایی
⏺
7_فرزین معامله‌گری
⏺
8_علیرضا همایی‌فر
⏺
9_دنیل گرا
⏺
10_میلاد سرلک
⏺
11_محمدخدابنده‌لو
⏺
12_مارکو باکیچ
⏺
13_علیرضا…</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/134311" target="_blank">📅 09:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134310">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❗️
امروز محسن خلیلی به عنوان سرپرست روی نیمکت میشینه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/134310" target="_blank">📅 09:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134309">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❗️
بازی پرسپولیس و چادرملو درصورتی که مساوی به اتمام برسد مستقیم به ضربات پنالتی خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/134309" target="_blank">📅 09:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134308">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
به این ترتیب، حالا احتمالات برخورد تیم‌ها در مرحله یک‌شانزدهم نهایی کمتر شده است و حدس زدن حریفان بعضی از تیم‌ها در صورت صعود به مرحله بعد، آسان‌تر شده است.
🔴
در این میان وضعیت تیم ملی ایران هم در صورت صعود به مرحله بعد، نسبت به قبل از شروع جام، روشن‌تر شده…</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/134308" target="_blank">📅 09:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134307">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
کامل شدن جدول 6 گروه اول جام جهانی، حالا حدس زدن حریف احتمالی تیم ملی آسان‌تر از قبل شده است.
🔴
🔴
به گزارش فوتبالی، با مشخص شدن جدول چند گروه از گروه‌های 12گانه جام جهانی 2026، به تدریج ابهامات موجود در برنامه و رقابت‌های مرحله یک‌شانزدهم نهایی شفاف‌تر می‌‎شود.…</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/134307" target="_blank">📅 09:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134306">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🗒
جدول بهترین تیم‌های سوم تا به اینجای مسابقات جام جهانی
🔴
هشت تیم برتر سوم به یک‌شانزدهم نهایی صعود می‌کنند
⚽️
#جام_جهانی_۲۰۲۶
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/134306" target="_blank">📅 09:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134305">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjA6CG5DMNL3MmKpevWAd-1D-GppN2l5o409EcBuvvLS8snPqUCdzg4wSvdLZhoazPsD4kfKVMjaO5xLoonc5SzT_KNdctTAwivcw9jWnDA7i0dyh5XTHmleV6j_UqV7OaDVfwZGj857yoXM0ETWj4J84v8cqvtHLMEd1xVoYmoqBlscW1qYCPe5U8sLcTNRCdWCg_wr-xr2BvJTF9u2SIADhfqDLCsfEfZIo4g4oWRDgP8eCzzSb2_kD_0amnhAsURgGNxotTMIVZVo8Igu-q3Me-4Bwnpc1BCGzotUUdkRKKcpoCezHfQs8aGm9ZSmkGiMuKqbPwlwszkUpNBnrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗒
جدول بهترین تیم‌های سوم تا به اینجای مسابقات جام جهانی
🔴
هشت تیم برتر سوم به یک‌شانزدهم نهایی صعود می‌کنند
⚽️
#جام_جهانی_۲۰۲۶
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/134305" target="_blank">📅 09:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134304">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/134304" target="_blank">📅 09:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134303">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pb0WN3H8yoIvoAdrIYAD9Qlg4t8a5rR121ZPi-sQhDfp6A34GncmOUvss99lAswRVQ4a85rNaJ1F-bOOvGKXp1PkA5cCjKe-OrIkUFydjV9eY8ltaz157rOeyp3pvIHZVHdiW80DpzlzI0lpgS8ruxQSKz9yQAlE0UTMecSROBXlElb03aoG9CiUjG2UsUswzO1CFb2LD_xbijNve8f9xQ1LwZIbV5htvO6pmVtExnpjhYcpBgE_L0XFLKJTmX3OnxUrUNczOZXqX0vuHI5HNXz7zCEcoNCGkodXiLm0AvR4BUVhzqtG32JrRBgF1EkplVSJvENzNe5tLgdxdzt4rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/134303" target="_blank">📅 09:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134301">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✅
جدول گروه D جام جهانی در پایان مرحله گروهی
🇺🇸
صعود آمریکا به عنوان صدرنشین
🇳🇿
استرالیا دوم شد و صعود کرد
🇵🇾
پاراگوئه منتظر سایر نتایج برای صعود
🇹🇷
❌
ترکیه حذف شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/134301" target="_blank">📅 09:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134300">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oemG2LcexR3Q4ylFmuWHsJQ_Y91pKLzb58Ko9ZWdL2Wod4ihT7VlDgWX9hlcgZ90yHyrY1vDMBipn2YyAyCisWW9yZr2T5tyrP2PbtdNErNIf48QbVF_8okeItPODCnAhss4sVy9qmuqmgFQtb90xIt8mJU6gSeydYaPC5TDl5a29vDDIeElEXI4c-YPeR9eZ19odj9iKFecSnRUiK0ySlGMa8W03RozBEEiB-atGgQFs4Y7mQQe5_ctLWIw65dZPQmOwSDXMXiscvy-Pt1JBDAYkKBuCOX8ht2VvkB5ztvSBbzXnDgMOdlG7k8iotYV9EdV_ijgEZPjQM7jZX1cQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جدول نهایی گروه c جام جهانی
👀
صعود قطعی برزیل و مراکش به دور بعدی رقابت ها ؛ اسکاتلندی ها باید فعلا منتظر بماند
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SorkhTimes/134300" target="_blank">📅 09:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134298">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❗️
بازی پرسپولیس و چادرملو درصورتی که مساوی به اتمام برسد مستقیم به ضربات پنالتی خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/134298" target="_blank">📅 09:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134297">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kaBjxE9GmcgYfWQIp06hs6OCb-UFaL8O__oIFnu1CRYpBSnteNVpYgwbiWAlO1CQh-QxlmP9m2vak0XBsWvsJFIJE6Fs9QbsFABDwIhNQIHNkT6oklTnvJfqJF2RETiq0EbeoyeSgasyq-d1twhyzepszpGVSzqeH3lIvQS6EwcX69mqlNPlQxyIc-LGEiNNa5X9YPpVuBrDNM3CK8u8rIOi1-J9czR0TleoT9dRt6va48zWxnTh-3DZMKhJ8nCq1XBThCvdcjdn6ELdwc3gitDZViFdiMBem_Vrs4y4I4hbxtoIg_1iJbW7cticEf3xowuSQopm5kYmj3yTqZbqeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
⚽️
گروه D جام‌جهانی ۲۰۲۶
[
آمریکا
🇺🇸
🆚
🇹🇷
ترکیه
]
⏰
بامداد پنجشنبه ساعت ۰۵:۳۰
🏟
استادیوم
سوفای
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
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/134297" target="_blank">📅 01:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134296">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEOZl0UoP2NWy85o0fG3dm6ESsaW2VH_eO0ZRvolYmQYSX2bbvWd0mMsme30C0OiXRQGcwWVyj1faShfA2Wi8LxVpBsgzFwwXrfVDkSJY1khhLj_OGT8Kwpzz6BIqL7vI6RndaVypSH1hPIFQrBO-s7pFt3ritBizwKMVceuxCknjqzu3DR9U3RMuSG2XSPSdZK7w0fwaPaT-OlaXp8mWNKLyTR7Ufxii8CdAcKbW8c7tk13_Fe7iZ-meJrCcGKcAHfjQxjae-uJeQnpwqCjRuwanU5r91JnwqoqZAicq525HWtygQP4zAr7i6b28yEHVUg-zDuJ5RRk79_CbZ9BPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پورعلی گنجی مشکلی برای بازی با چادرملو نداره و میخواد با دست بسته شده هم برای پرسپولیس بازی کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/134296" target="_blank">📅 00:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134295">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❗️
میساکی:
✅
جام جهانی رو میدادن به خودمون، بخدا بهتر از آمریکا برگزارش میکردیم.آمریکا نتونست میزبان خوبی باشه.
😆
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/134295" target="_blank">📅 00:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134294">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❗️
❗️
ترکیب احتمالی تیم از دید ورزش سه:
🔴
رفیعی
🔴
معامله گری، ابرقویی، پورعلی گنجی، گرا
🔴
عالیشاه،باکیچ، سرلک، عمری،
🔴
بیفوما، شکاری  نظرتون چیه
🤔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/134294" target="_blank">📅 23:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134293">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fafbef8e3.mp4?token=Jv-Lomx9Qug4g9qOWrQzoXuN4vVsC4lff782-Mz9U-UYHbc5VboyJ4KNArFaxmo2Xs5iAAQybKT_g0Pogjr2HCn1lCGVPci-FMzE0B_TvMruU4leCYGl8KYydw3CiQKENdhRjz2vXLHmT7CEBWvE1V1Setli0mb0-N3BWf-hmsuWYtYaJ3sjJnD4L4bZ9DyOlRFPXfN9mQecSSjukYevW3nEdMO0ZlgR8Ryp1TzebtVecu4g6DV8JE5lQgEkm4hOQgxgE6uy5t9Cjr3O-iIYNFG-mvrpDu409iIk6S7y0KAX2flwsBdgtl77AbeD-MNQ4sVUWmgjpOHvrdnoGaNP-oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fafbef8e3.mp4?token=Jv-Lomx9Qug4g9qOWrQzoXuN4vVsC4lff782-Mz9U-UYHbc5VboyJ4KNArFaxmo2Xs5iAAQybKT_g0Pogjr2HCn1lCGVPci-FMzE0B_TvMruU4leCYGl8KYydw3CiQKENdhRjz2vXLHmT7CEBWvE1V1Setli0mb0-N3BWf-hmsuWYtYaJ3sjJnD4L4bZ9DyOlRFPXfN9mQecSSjukYevW3nEdMO0ZlgR8Ryp1TzebtVecu4g6DV8JE5lQgEkm4hOQgxgE6uy5t9Cjr3O-iIYNFG-mvrpDu409iIk6S7y0KAX2flwsBdgtl77AbeD-MNQ4sVUWmgjpOHvrdnoGaNP-oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خداداد عزیزی: بنظرم ایران می‌تونه مساوی هم به راحتی از مصر بگیره و صعود کنه، با بازیی که جلو بلژیک کردیم بنظرم میتونیم سوییس رو شکست بدیم و صعود کنیم حتی به مرحله یک هشتم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/134293" target="_blank">📅 23:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134292">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✅
همون همیشگی
🔴
موعود بنیادی‌فر داور بازی پرسپولیس و چادرملو شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/134292" target="_blank">📅 23:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134291">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❗️
بازی پرسپولیس و چادرملو درصورتی که مساوی به اتمام برسد مستقیم به ضربات پنالتی خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/134291" target="_blank">📅 23:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134290">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✅
با اعلام سازمان لیگ دنیل گرا برای بازی فردا مشکلی نداره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/134290" target="_blank">📅 22:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134289">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✅
محمدحسین صادقی پس از چند روز عدم حضور در تمرینات پرسپولیس، اعلام کرد به دلیل مشکلات خانوادگی فعلاً به تهران نمی‌آید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/134289" target="_blank">📅 22:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134288">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
فوتبالی :برای بازی پرسپولیس و ذوب آهن دنیل گرا  مدافع راست خارجی پرسپولیس محروم بود و نمی‌توانست بازی کند اما بازی لغو شد
🔴
حالا باید دید آیا مدافع راست خارجی قرمزها می‌تواند تیمش را مقابل چادرملو همراهی کند یا محروم است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/134288" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134287">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPJ1_Q0nET1txoghZPvmB_bV8gVIsw-4AebdA1XUaNurxfT7uGwkr-XmspIlw6NUh1PvQBMiroD9YuyxIKGy6ai7QMZr9JksJcSjSvGtnBuKihNEPqrbX3lqTVqyHQu9rxD4PbShujJEYqk8JUlnzHtfosmE5s1BEL2xSrytCbBqUaVAWs65QcEpAkR9QjXHFowGcLyDCNBP9PzL4EJ2v0b0Rb67Zsi6uas8eHSWvYfnmuW14dQPBUcR4jNUeyXfBNMN_tpXYMRoHjGsFU5Fbl1Bjqe-Qtspa-llqxZt_eWeWy92_oermGy4s1Z8OiJ8s3WbsNuGpesADYaxIZhc5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
جدول خروجی‌های تراکتور در سایت ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/134287" target="_blank">📅 21:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134286">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❗️
بازی پرسپولیس و چادرملو درصورتی که مساوی به اتمام برسد مستقیم به ضربات پنالتی خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/134286" target="_blank">📅 21:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134285">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEqpZpkdqcjGIgnVNaQWpAFEtNCQcESZkIqJn2XlWGhdG3E90KH2Q6XhFMyFDFRGcGURwof6WhxsUuZ8C-TFdr8y3lhNO7Azuni3nxU6epjL6pWDqL4qi7YdIEnZpHg1zVyKGPthMgS2xwgRDlCdATkwoT5zd373OZTRn96YXa6GYgbyhRAPIModV7IFZI4wogTgxUm2cIUTYHc7T72Pez2hCC7sfN6ji-LTkReGMTm-ECPsZFZQkoj0x9sQKilhCM5yAcPip0ySpDUlrAypwODejHjXBZU73EdbAgCwhZMBO53JST_N-VuIHN_Q7sO0SRUFrU_B9q90oG3ASKicFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
بازی پرسپولیس و چادرملو درصورتی که مساوی به اتمام برسد مستقیم به ضربات پنالتی خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/134285" target="_blank">📅 21:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134284">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
او پیش از این، از تمایل به فسخ قرارداد بدون دریافت غرامت گفته بود اما اكنون خواهان دریافت غرامت شده است و خواهان مبلغی از قرارداد فصل آینده خود شده است.
🔴
البته او خواستار مبلغ بالایی نشده است اما به‌دلیل اینکه، او و دستیارانش ۴۰۰ هزار دلار طلب دارند و مبلغی…</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/134284" target="_blank">📅 21:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134283">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoR3jIN_ckbONURgQQBAK0pTBd96286JBb4nAeXLB2b_JT5ndH0pn7tY1WgNxg56Y9bUI7gcgTz9U_RrDti5zyBXdE7__i4J667HJ90lv8jAPJHBbM6-tyzRiyH15npDPr5-S4y4iVfO7FC2x6gHw8Tvm4lq939ii63uRX2yERdMkjCGgggIDcZpsPiuvYKSyHTiGtNU4MKMtM2_34FgfsoezAGrtYSqrEf3UFSGUKDcf1THkLwFsEzWANtaKxfLcmYTH9D1ABcgL_iaAZDC0-91bTMdrfWnDcOkSKeQfLJAYeRYEIFwMKIRYkfO4EF6iyP-UAJ9Jd5XbI3AJkVMJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
دیدارهای امشب و بامداد فردا جام‌جهانی رو در وینکوبت با بونوس ویژه پیش‌بینی کن!
⚫️
🔣
0⃣
2⃣
بونوس ویژه جام‌جهانی روی هر واریز برای تمامی کاربران!
🎁
تا پایان مرحله گروهی جام‌جهانی روی تمامی واریزها
🔣
0⃣
2⃣
بونوس بگیر و فقط با یک گردش روی حداقل ضریب ۱.۸ به موجودی خودت اضافه کن.
⏰
این بونوس ویژه فقط تا پایان مرحله گروهی جام‌جهانی فعال است.
📌
همین حالا وارد ربات وینکوبت شو و ازین بونوس ویژه استفاده کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/134283" target="_blank">📅 21:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134282">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hj26Vtq_WdCn-z_UnMDwf1inQ8UHSJhiPg8oHF5jxpR_1RjOA6h-Q38lGA2v7RKc4Jm0Az0BFGijsAIm4RT3RICsQgNLYnXNQbPwZOLuHyAQleGteexE-PrGMSbdlxjADXXjybjsJticBCmJ_pqMuMi_KfoerUBcCoHJMSf_cnu6Y3t8QEP561c6qMF00bET_8S2PjPjWvugSp8k_4XVMz2AjMkOlLx-M-_5yFU5fUsugjuLDnc5QrBlE1WbW-xRD0un1lG_FfxAmZPdUJD2kJgShl3cdLAJ_cirl9GpdIcqL0_G0vWvBfc8-k5eKozqE0zolXdfB5V1d3jHXVwj8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
شاگردان اوسمار امروز آخرین جلسه تمرینی خود را پیش از دیدار برابر چادرملو برگزار کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/134282" target="_blank">📅 20:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134281">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
❌
بازی سه جانبه
🔴
مسابقه پلی‌آف
📆
جمعه 5 تیر
🖥
چادرملو - پرسپولیس
⏰
ساعت 18:45
🏟
ورزشگاه پاس(تهران)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/134281" target="_blank">📅 20:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134280">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/134280" target="_blank">📅 20:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134279">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
🔴
🔴
#فوری
🔴
سرمربی پرسپولیس در فصل بیست و ششم لیگ برتر خارج از دو گزینه موجود نیست
🗣️
یا اوسمار ویه را بعد پایان پلی اف همچنان سرمربی پرسپولیس می ماند
🗣️
یا اسکوچیچ در صورت توافق رسمی و محترمانه با اوسمار، به عنوان سرمربی فصل پیش روی قرمزها فعالیت می کند./مهدی…</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/134279" target="_blank">📅 20:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134278">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
فوتبال جام جهانی و نشون ندادن به خاطر والیبال ..خود والیبال از ست دوم قطع شده و دیگه نتونستن از جایی دزدی کنن و پخش کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/134278" target="_blank">📅 20:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134277">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
🔴
ارتباط اوسمار و مدیریت پرسپولیس وارد چالش‌هایی شده است.
✅
به گزارش خبرنگار قرمزآنلاین، روابط باشگاه و اوسمار حسابی شکراب شده به گونه ای که ارتباط مدیران با این مربی قطع شده است.
❗️
البته خلیلی به عنوان سرپرست موقت و معاون ورزشی همه روزه اوسمار را در تمرینات…</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/134277" target="_blank">📅 19:59 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134276">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
باشگاه تمایلی به حفظ اوسمار ندارد و در صورتی که با اسکوچیچ به توافق نرسد، گزینه های دیگری دارد.
🔴
به گزارش خبرنگار قرمزآنلاین، باشگاه پرسپولیس به غیر از دراگان اسکوچیچ گزینه های دیگری را هم برای نیمکت تیم در نظر دارد و هنوز با این مربی کروات به تپافق قطعی…</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/134276" target="_blank">📅 19:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134275">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
❌
بازی سه جانبه
🔴
مسابقه پلی‌آف
📆
جمعه 5 تیر
🖥
چادرملو - پرسپولیس
⏰
ساعت 18:45
🏟
ورزشگاه پاس(تهران)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/134275" target="_blank">📅 19:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134274">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
باشگاه تمایلی به حفظ اوسمار ندارد و در صورتی که با اسکوچیچ به توافق نرسد، گزینه های دیگری دارد.
🔴
به گزارش خبرنگار قرمزآنلاین، باشگاه پرسپولیس به غیر از دراگان اسکوچیچ گزینه های دیگری را هم برای نیمکت تیم در نظر دارد و هنوز با این مربی کروات به تپافق قطعی…</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/134274" target="_blank">📅 19:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134273">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❗️
بازی تو نود دقیقه تموم بشه مستقیم می‌ره پنالتی و وقت اضافه نداره این بازیهای سه جانبه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/134273" target="_blank">📅 19:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134272">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
❌
بازی سه جانبه
🔴
مسابقه پلی‌آف
📆
جمعه 5 تیر
🖥
چادرملو - پرسپولیس
⏰
ساعت 18:45
🏟
ورزشگاه پاس(تهران)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/134272" target="_blank">📅 19:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134271">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
❌
بازی سه جانبه
🔴
مسابقه پلی‌آف
📆
جمعه 5 تیر
🖥
چادرملو - پرسپولیس
⏰
ساعت 18:45
🏟
ورزشگاه پاس(تهران)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/134271" target="_blank">📅 19:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134270">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇷
🤍
دنیس اکرت و جام‌جهانی سر نوشت ساز
‼️
💣
🚨
چند باشگاه مطرح لیگ برتری درحال بررسی شرایط برای جذب دنیس اکرت(درگاهی) هستند، البته پس از جام جهانی.
✔️
نکته مهم  این است که آنها صبر کرده‌اند و پس از جام جهانی و در صورت عملکرد قابل قبول برای جذب این بازیکن اقدام…</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/134270" target="_blank">📅 18:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134269">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✅
از آخرین بازی رسمی پرسپولیس ۱۲۷ روز می‌گذرد و پرسپولیسی‌ها فردا بعد از مدت‌ها به مصاف چادرملو می‌روند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/134269" target="_blank">📅 18:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134268">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
باشگاه تمایلی به حفظ اوسمار ندارد و در صورتی که با اسکوچیچ به توافق نرسد، گزینه های دیگری دارد.
🔴
به گزارش خبرنگار قرمزآنلاین، باشگاه پرسپولیس به غیر از دراگان اسکوچیچ گزینه های دیگری را هم برای نیمکت تیم در نظر دارد و هنوز با این مربی کروات به تپافق قطعی…</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/134268" target="_blank">📅 18:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134267">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✅
قدوسی ؛جدایی اوسمار قطعی شد و علاوه بر اسکوچیچ باشگاه یک گزینه دیگه هم داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/134267" target="_blank">📅 17:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134266">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❗️
امیرحسین محمودی: اگر فوتبالیست نمی‌شدم احتمالاً کشتی‌گیر می‌شدم. اول کشتی را شروع کرده بودم و دو سال کشتی گرفتم. در کشتی هم خوب بودم و استعداد داشتم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/134266" target="_blank">📅 16:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134265">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❗️
❗️
ادعای قدوسی: پرسپولیس غیر از اسکوچیچ گزینه دیگری هم دارد!
😐
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/134265" target="_blank">📅 16:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134264">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔽
🔽
مدیران باشگاه سایپا خبر خرید امتیاز سایپا توسط پرسپولیس تکذیب کردند؛ بحث اصلی فقط سر فروش زمین تمرین سایپاست، نه خودِ تیم.
✍️
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/134264" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134263">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
با اسکوچیچ هنوز چیزی روی کاغذ امضا نشده. ولی توافق درخصوص کلیات انجام شده.///خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/134263" target="_blank">📅 15:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134262">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✅
✅
درخواست ایران و مصر برای عدم برگزاری  مراسم ویژه همجنسگرایان توسط فیفا رد شد
🔴
فیفا: هواداران تو این بازی میتونن با پرچم‌های رنگین‌کمان وارد ورزشگاه بشن
😆
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/134262" target="_blank">📅 14:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134261">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
پرسپولیس با وجود غایبان پرتعداد در بازی فردا، چاره‌ای جز پیروزی ندارد و باید با ترکیبی متفاوت، نخستین مانع مسیر آسیایی شدن را از پیش‌رو بردارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/134261" target="_blank">📅 14:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134260">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✅
✅
درخواست ایران و مصر برای عدم برگزاری  مراسم ویژه همجنسگرایان توسط فیفا رد شد
🔴
فیفا: هواداران تو این بازی میتونن با پرچم‌های رنگین‌کمان وارد ورزشگاه بشن
😆
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/134260" target="_blank">📅 14:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134259">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇷
🇪🇬
🏆
دیدار بین ایران و مصر در سیاتل از سوی کمیته محلی برگزاری این دیدار از جام جهانی بعنوان"مسابقه افتخار"(Pride Match)برای همجنس‌گرایان نامیده شد!
‼️
‼️
پ.ن:طارمی و صلاح باید بازوبندی رنگین کمون(همجنس گرایی)ببندن.
🫣
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/134259" target="_blank">📅 14:11 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
