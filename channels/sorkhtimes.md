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
<img src="https://cdn4.telesco.pe/file/UByV2a-t6w3YeXu1ZRlVUdIWFFjva2Thc-sFF3MjeiyhdqTe-CMg0k2OnAA0d0f7w7JF6L_f_447-LfZ7MwCkM7aL049ON4OKCnw_VtvvaaeipqCTW8HLJ6a7YFphPiNwD63wg7KOLwXrsargPEqsJ0rhkGRDM215YvYDacShNSqHnTOYl6ljTtLnhr0H4e7GAsHY7ZuBEO6O6tigv0ScqiZ3rXnoHeQqEtdCCY6rfj-tzT3a2hq5l9gMASwJpNzq8wIbPnrUU704gw3vGyPdhMgil5IHfQwEdwOVUw_4nuPJ88agp7s46tDf-ZZxvWDyOTIH0hy2WhtCYlLRsydPQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-08 06:08:05</div>
<hr>

<div class="tg-post" id="msg-139234">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clB09SFqqre6oQ2O7ifCYQxaCnzhU4pkbPpPHg9HVlWIp_-Ng4FGXYVlzt9cHOnI4fUBJjwnzGeWEE5Zy6UEz-UX1WPEaRz6fYny-kQLB8NC733Ut2cmh6zzXOGNqM_JcPZdIU_rbCWKZShCYqeMs1IGdl33aMgkLP8b5cr5WOgW_iA5-QS2cOMRYdquH-qj07kLLL7D7BkQrblODWtAt05UmmUc3aMT0lcKv5om556jyvlM5O3RoRIkwMGT15rt-4ZnAW2sf90dYO9-pcGPQ0QiUZT6IZFjNYuUne_32ZfSVUvCsxqMJupyg8Wu2B-GAAVLZ8a2K2Ro9ogQ6bWoYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ورود به اسپورت‌نود؛ ساده‌تر از همیشه!
🔗
دنبال یه راه سریع و بدون دردسر برای ورود به اسپورت‌نود هستی؟
🔵
با مینی‌اپ ربات رسمی اسپورت‌نود، مسیر دسترسی ساده و یکپارچه شده؛ بدون لینک‌های متعدد و مراحل اضافی، مستقیماً وارد محیط کاربری شو و از امکانات سایت استفاده کن.
🔗
ربات رسمی اسپورت‌نود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت‌نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/SorkhTimes/139234" target="_blank">📅 01:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139233">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
🔴
جدول رده‌بندی لیگ برتر پس از پایان هفته چهارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SorkhTimes/139233" target="_blank">📅 00:24 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139232">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✔️
✔️
مهدی تیکدری: بعد بازی قبل همقسم شدیم که این بازی رو ببریم/بزرگترای تیم خیلی بهمون کمک کردن/روی یه اتفاق به تراکتور باختیم/هجمه‌ها بعد از باخت طبیعیه/ترافیک در خط حمله زیاده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/SorkhTimes/139232" target="_blank">📅 00:23 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139231">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✔️
✔️
دانیال ایری امشب به عنوان بازیکن ذخیره وارد زمین خواهد شد تا اتفاقات دیدار با تراکتور را فراموش کند.
✍️
ورزش‌سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SorkhTimes/139231" target="_blank">📅 00:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139230">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
حسین کنعانی ، دانیال ایری ، مجید عیدی ، پویا پورعلی و محمد عمری پنج بازیکن تیم پرسپولیس که سابقه پوشیدن پیراهن تیم ملوان دارن
✔️
فرزین معامله‌گری هم که برای سربازی منتقل شده به ملوان تنها بازیکنی که سابقه پوشیدن لباس پرسپولیس داره
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/139230" target="_blank">📅 00:17 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139229">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🤩
✅
هفته‌پنجم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
طویله کیسه
🤩
🗓
تاریخ چهارشنبه ۱۱ شهریور
⏰
ساعت ۱۹:۳۰
🏟
میزبان نقش‌جهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/139229" target="_blank">📅 00:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139228">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrnBKoE40XQDXXJfQUI_qO3LZRza4EWzFovzk0W_o5E1BtQY9K_jMQNH2PP8aKimPU8WPt1ONKYq-Ib3i1w0SL7I5NSRO5_FcNAD-ESNzIGWEVP1sh5CtCWtBeiJQ083-Oer5plqrkeETdNKcNhF1JXsoSnKMQiWbQVtIxkHfyjYiW1RIBLXdlEQp8V-gk1ukgYnESCIWub-C25TSWo3V0RgZKKMMqy_UHxuiXgZSYUbTtGsfXdQEBHkm-QxUs5qSzaf2Pj7UlSJRWj3p2D5FrubPTvlQVusZw0KYhf98eE7GuuMx8l2hVSNQtd0yRciL6urmk5xR7Xs3UTAwn3DRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
✅
هفته‌پنجم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
طویله کیسه
🤩
🗓
تاریخ چهارشنبه ۱۱ شهریور
⏰
ساعت ۱۹:۳۰
🏟
میزبان نقش‌جهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/139228" target="_blank">📅 00:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139227">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✔️
✔️
مهدی تیکدری: بعد بازی قبل همقسم شدیم که این بازی رو ببریم/بزرگترای تیم خیلی بهمون کمک کردن/روی یه اتفاق به تراکتور باختیم/هجمه‌ها بعد از باخت طبیعیه/ترافیک در خط حمله زیاده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SorkhTimes/139227" target="_blank">📅 00:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139226">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
کریم باقری: پرسپولیس از هر بازیکنی بزرگتره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SorkhTimes/139226" target="_blank">📅 00:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139225">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✔️
✔️
کریم باقری: نگران نباشید. پرسپولیس بهتر میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/139225" target="_blank">📅 00:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139224">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
❌
باقری: کادرفنی زمان می‌خواهد که میان بازیکنان هماهنگی ایجاد کند
❌
تیم پرسپولیس به نفرات توجه نمی‌کند، همه بازیکنان جمع شدند زیر سقف پرسپولیس
❌
تماشاگران پرسپولیس را تشویق کنند، نفر را تشویق نکنند!
❌
اورونوف دیر به تمرینات اضافه شده و کادرفنی تلاش می‌کند…</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/139224" target="_blank">📅 00:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139223">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
آمار برگ ریزان بازی
🔴
۱۶ شوت
🔴
۶ شوت در چارچوب
🔴
امید گل ۴
🔴
گل ۳
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/139223" target="_blank">📅 23:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139222">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‼️
🔴
علیپور با ۲۵۷ بازی، از سید جلال حسینی با ۲۵۶ بازی عبور کرد و به رتبه دوم بیشترین تعداد دیدار رسمی با پیراهن پرسپولیس رسید.
🔴
علیپور در ۲۵۷ بازی خود با پیراهن پرسپولیس، ۹۰ گل زده و ۳۸ پاس گل ارسال کرده است. او با ۹۰ گل و پس از پیوس و پروین، سومین گلزن برتر…</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/139222" target="_blank">📅 23:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139221">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✔️
خلیلی: امروز فقط بهای جوانگرایی را دادیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/139221" target="_blank">📅 23:30 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139220">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7NFMb68WZAoxNv--p8ngFLovy81lbbPYxw2KpMrtFVUCFaQBtrTyANtJD03seSE5KzKLpU6dPM8dq5pmK478MZfYAXeCDOzDaDvyKDH_bG21Foh_Zj86jFkjyGZj_X4k1R-SbvdX6tPryazH_be7bWFMSwhbNOYgA8CQRctyoACkV6W5Y_gF5p4XPXAp-s78ejCd2K_x7xR4cFjzjPsMJAc9h6la2RICf-2y-U5Ix0ZOdGph3O2Ap-soM6ISVfddS6QUeL0S9SmMDdoAW4BZB0cSd53ZCnPXTHZPHGcnVtg-YQSc2tPG3w91fakFnOq02DFHReY4D5njzumUmBXPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
ستاره این روز های پرسپولیس تارتار
📊
عملکرد بیفوما تو این فصل
🔄
4 بازی 1 گل 1 پاس گل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/139220" target="_blank">📅 22:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139219">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✔️
✔️
براساس‌صحبت‌های‌مهدی‌تارتار؛ سرگیف از بازی فردا مقابل ملوان به ترکیب سرخ‌ها برمیگرده و تارتار میخواد زوج علیپور - سرگیف استفاده کنه اما اوستون اورونوف همچنان نیمکت نشین خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/139219" target="_blank">📅 22:34 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139218">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
❌
باقری: کادرفنی زمان می‌خواهد که میان بازیکنان هماهنگی ایجاد کند
❌
تیم پرسپولیس به نفرات توجه نمی‌کند، همه بازیکنان جمع شدند زیر سقف پرسپولیس
❌
تماشاگران پرسپولیس را تشویق کنند، نفر را تشویق نکنند!
❌
اورونوف دیر به تمرینات اضافه شده و کادرفنی تلاش می‌کند…</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/139218" target="_blank">📅 22:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139217">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
❌
باقری: کادرفنی زمان می‌خواهد که میان بازیکنان هماهنگی ایجاد کند
❌
تیم پرسپولیس به نفرات توجه نمی‌کند، همه بازیکنان جمع شدند زیر سقف پرسپولیس
❌
تماشاگران پرسپولیس را تشویق کنند، نفر را تشویق نکنند!
❌
اورونوف دیر به تمرینات اضافه شده و کادرفنی تلاش می‌کند…</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/139217" target="_blank">📅 22:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139216">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✔️
✔️
کریم باقری:
🔹
به زارع دوست عزیزم تبریک می‌گویم؛تیم خوبی دارد و ضد فوتبال بازی نکردند.
🔻
خداراشکر برنده شدیم و توانستیم با روحیه خوب به پیشواز دربی برویم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/139216" target="_blank">📅 22:29 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139215">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✔️
✔️
کریم باقری:
🔹
به زارع دوست عزیزم تبریک می‌گویم؛تیم خوبی دارد و ضد فوتبال بازی نکردند.
🔻
خداراشکر برنده شدیم و توانستیم با روحیه خوب به پیشواز دربی برویم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/139215" target="_blank">📅 22:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139214">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUR1_tqSGIPxuaXBbRYH7TPHI6GRXeZRnViXd-MGtjgfbXV47EBwFr-5SDaCaMUCDzvog8XJnKyqa2KMalkV10U4MsE4xdnyk26g50pj7nTuDSGr6mkEx51FyqGmin_MwNRtyDefZiolvxDqep36X8fnedEdy22hSRuEwEM8gCzl3aSGi2IOk5c8IZXVaIzdhEVbZPBPwf6At-t_-fB7VMt-l5jTzeih4s4SPsMQ5pEVxwhRghNVUORdlHmo5XSi5Xl6UAA4FgCQrGJEbaKQRNNGJZJAla7ytudggpMgNdt_4oyYcgsSS6MpzaW5_BdaP-6V-kqQGwruaGjIIe_iRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
🤩
پیمان حدادی بار دیگر این استوری رو گذاشت/ حسبی الله : خدا برایم کافیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/139214" target="_blank">📅 22:27 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139213">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✔️
✔️
مهدی تارتار به دلیل افت فشار در نشست خبری بعد از بازی شرکت نکرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/139213" target="_blank">📅 22:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139212">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✔️
✔️
گفته می‌شود فردا نیز مهدی تارتار برای دفاع چپ پرسپولیس از علیرضا همائی‌فر استفاده نخواهد کرد و مهدی تیکدری در پست غیر تخصصی بازی خواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/139212" target="_blank">📅 22:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139211">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
❌
🇮🇷
کنایه مازیار زارع به برنامه فوتبال برتر: دوست ندارم تصویر من را در برنامه تان پخش کنید. شما اینجا باشید من مصاحبه نمی کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/139211" target="_blank">📅 22:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139210">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d295e52c.mp4?token=Me5vOkXEeaE3nVliITQc9g3J0HKetMUnb3sSJMGHWQoOs5jfoxt4jtM7bLLOkNEYkfem0P2nVAkPEbBRhuDVNVumvLM6Y96ObuU5Opsu--VojIK8Mhuvs0RiZjNqt10uNCCwvehbhJFFDCjj9wYsdvhBQvCI_byNAI1bdUM-0uCgoiIH62hrXV2bBRfwfrSccPf012VBw1C1DBpJPPMM6E6HeFqd-O_ms-1y8cTzHqiRDFv8RSmufQnEZOeOeNsede4hcTZs2HVqESH5tnExf43HgwyByxaiDNedvqx55nZFozE9tKUDT4LPaYG2gvSbW_Mje-LxOX9hfhimdFmOSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d295e52c.mp4?token=Me5vOkXEeaE3nVliITQc9g3J0HKetMUnb3sSJMGHWQoOs5jfoxt4jtM7bLLOkNEYkfem0P2nVAkPEbBRhuDVNVumvLM6Y96ObuU5Opsu--VojIK8Mhuvs0RiZjNqt10uNCCwvehbhJFFDCjj9wYsdvhBQvCI_byNAI1bdUM-0uCgoiIH62hrXV2bBRfwfrSccPf012VBw1C1DBpJPPMM6E6HeFqd-O_ms-1y8cTzHqiRDFv8RSmufQnEZOeOeNsede4hcTZs2HVqESH5tnExf43HgwyByxaiDNedvqx55nZFozE9tKUDT4LPaYG2gvSbW_Mje-LxOX9hfhimdFmOSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
کنایه مازیار زارع به برنامه فوتبال برتر: دوست ندارم تصویر من را در برنامه تان پخش کنید. شما اینجا باشید من مصاحبه نمی کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/139210" target="_blank">📅 22:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139209">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e73d84229.mp4?token=AJ_-x5MGK1metZpvx0QphpIzOwI4RGmqaujdKlJfFA9T-po2Iw5et_dsfO9uFT8-Sj-9ib7uDCmhXZL5lI8y-Cxw9Fdwr2qMzTEooSCqxgp4syYqdzYmBRja1Y8xt3uePqQUGxIcrIwgYh81yfq1jtFIoUAzx-vy2WT4O1S6926_tm1DWftTuF5AuFUGf3-bPmhReL8e7vVC-8aaX2bSqrL0q-voeVttuJoMWFGXuKPC_xNmfEQReRwb88Ai8CNa_QQC2ql1UGB6hCqZmhagKQU4bC4XkrXBLXKVf-HFKeUMBOcBk2n_B3qhLMzUtiGYFwL-hKpXzJRR_xUjmPTncQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e73d84229.mp4?token=AJ_-x5MGK1metZpvx0QphpIzOwI4RGmqaujdKlJfFA9T-po2Iw5et_dsfO9uFT8-Sj-9ib7uDCmhXZL5lI8y-Cxw9Fdwr2qMzTEooSCqxgp4syYqdzYmBRja1Y8xt3uePqQUGxIcrIwgYh81yfq1jtFIoUAzx-vy2WT4O1S6926_tm1DWftTuF5AuFUGf3-bPmhReL8e7vVC-8aaX2bSqrL0q-voeVttuJoMWFGXuKPC_xNmfEQReRwb88Ai8CNa_QQC2ql1UGB6hCqZmhagKQU4bC4XkrXBLXKVf-HFKeUMBOcBk2n_B3qhLMzUtiGYFwL-hKpXzJRR_xUjmPTncQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
👤
🎙
ابوالفضل جلالی:‌
🔻
حضورم در دربی؟!هنوز هیچ چیز مشخص نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/139209" target="_blank">📅 21:57 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139208">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBRf5UdtjyaEZ1T2J9t_QTDt7r6qBrrEdgbCk0falRL8pfUVuTxqF28bgqMTahP_27bOU0n1TQloU-mUJEF_czhrWJe5mkQQ9ym0fkB2BrbQny9PF7bZb51naBnhAmUs0FtJY7sOE28k9gorZecZlYZ5Kaue_6CdZBRW1syyiwA2wSpchpvzL5mmo60J8MJBUlrEOwJ7YPYNU1PtoJZ4z9KASFuA5vYG6CE0QL1LC4fkB18PUAYGEzYqavMhPZCSfTBOaBYTOPHWQv1yB5RhCIkAU6EkMAqxxS0Vbtu3JQAUOHtcFFtjNEO8XW_QG2OEupi4Y7cEPnoTC2zjFsRdqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
هوادار همین سبکو میخواد آقا تارتار تیمی بدون ترس و سراسر هجومی تیمی که می‌تونست امشب خیلی راحت بالا 5 تا هم گل بزنه
⏺
خداشکر با روحیه بالا سراغ دربی رفتیم و امیدوارم تو دربی هم همینطور و همین سبک رو ارائه بدیم
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/139208" target="_blank">📅 21:52 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139207">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a052a7430c.mp4?token=MTX7P1x-z0QxMQNjyCenJJDgAder_epD8xXaMO9iJUHqdu668g-qWqbeBh8aypqGVMytABayqgvO8LbeTmsg4V-qMI1HzrJFzYV4XgakyHdBzuTWP2mtG4n9u4N7cobKpABBewA1XI0jZc4pfnzEZu-8G69hh8nQY7OT2UYuc7EoE4cjVquehjMW8QcWH0me4fv0i4VeZLFbmdzbbz3w5KuYOfD_mRr-W9iEYsHTWg4t4AFn2DUp6xhO9y6hE4gV9nGN3f1lehxXSrYbeXFtYtnUDcqIoLmb9dynErNeLI4u-FnGVf8IDKqo0ex6Zup0v8ReUK0oA35CIHVhnN83Yxbdjixcr49N4gA3v1n0bOeGVjhYMDthrzVqo0L8FrfHiHTwJ_8UTsSX-8n8v9AEr_o2ntWnQsd6lcoh3o8ydOemF6gSZPIwoGs5_8kwD6n40aPGTrS8h0uC3KldLe54vxCk71q_w0rRsaxZI5p87kJ_wlYCJUCCvbeL_A3DAYwZQzhcwCoYhli6HtlhWVKqNbLLAHKlkxh22qx6fkZ4AEdpdsQBkGRyD9jiEvgdQOSM5BYOHIhMQWpEmrxgn_RFmYwXybYUN7s0SSAIvrJpjlndwJUxRBz6v_ZlFjMjz3L_B4d3khSFnAAS5-lonedDuvd5KOHgFHNt3ibwIWgB33s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a052a7430c.mp4?token=MTX7P1x-z0QxMQNjyCenJJDgAder_epD8xXaMO9iJUHqdu668g-qWqbeBh8aypqGVMytABayqgvO8LbeTmsg4V-qMI1HzrJFzYV4XgakyHdBzuTWP2mtG4n9u4N7cobKpABBewA1XI0jZc4pfnzEZu-8G69hh8nQY7OT2UYuc7EoE4cjVquehjMW8QcWH0me4fv0i4VeZLFbmdzbbz3w5KuYOfD_mRr-W9iEYsHTWg4t4AFn2DUp6xhO9y6hE4gV9nGN3f1lehxXSrYbeXFtYtnUDcqIoLmb9dynErNeLI4u-FnGVf8IDKqo0ex6Zup0v8ReUK0oA35CIHVhnN83Yxbdjixcr49N4gA3v1n0bOeGVjhYMDthrzVqo0L8FrfHiHTwJ_8UTsSX-8n8v9AEr_o2ntWnQsd6lcoh3o8ydOemF6gSZPIwoGs5_8kwD6n40aPGTrS8h0uC3KldLe54vxCk71q_w0rRsaxZI5p87kJ_wlYCJUCCvbeL_A3DAYwZQzhcwCoYhli6HtlhWVKqNbLLAHKlkxh22qx6fkZ4AEdpdsQBkGRyD9jiEvgdQOSM5BYOHIhMQWpEmrxgn_RFmYwXybYUN7s0SSAIvrJpjlndwJUxRBz6v_ZlFjMjz3L_B4d3khSFnAAS5-lonedDuvd5KOHgFHNt3ibwIWgB33s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
⚽
دانیال ایری، بازیکن جوان پرسپولیس به سمت هواداران ملوان رفت و به هواداران تیم سابقش ادای احترام کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/139207" target="_blank">📅 21:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139206">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKEC3EirWSVN0tqvCPY9f3mHrEljrzcFCTn4Wey_IFeML78ovQiIczAjlEiLh65EemxtfggQZe9EFZFrS2lg7E7520u7d8_mR2M0K3slL58tHP8O0LwFYJL2taiDt4GEBCPitCX-w_thtfrFzvSsXbjp8bq830XskYGmBgCQekO7NoPOS1BBJcPHf3LZNV0vDalo-e9nz1hJ3OB8Ki2SA7c8wsfUJpVFkM70uLUJSU58CY0--P2g7jOwvjzB6oSrnwUaEH6TAEOlSxPaSgHOmzMcIOI5NT3PZE32HmjqYv_y_segp3YWTch_1PsoAi70NKkc4AtVmMwejcTb0rabEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
جدول رده‌بندی لیگ برتر پس از پایان هفته چهارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/139206" target="_blank">📅 21:38 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139205">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37d6965b1.mp4?token=IWT_4nojjS1MLMVskRDgXPfTW3mblr6c7qK6rDq5ZsJQNlx05RQiump8-Qftq_JDtndA0Qn_n9V0rH40oQhLXx2ieKrJ1iHRQ-e8AmP4NJlFYMD2bVGI404mYiIhzLIyReinzvIaACZIX09ajFc3ETRwRkUnYXWvtaKJDTAzRulwBF24XGAiCm4V93hAHQuFGvOlgffhpuvcu4T865z6no-XrxPRFMz-zMpI51rAEo5SNSa6dVw6Dd9WdPv4RhvMioKSDrftKMs3C0aKw8_PFEM9dn2fC7a80AhtBuB7WM7fUZwxLGjn17eLv0GzKEcgoKR2HiNXwbO1sfkQ2FJ87A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37d6965b1.mp4?token=IWT_4nojjS1MLMVskRDgXPfTW3mblr6c7qK6rDq5ZsJQNlx05RQiump8-Qftq_JDtndA0Qn_n9V0rH40oQhLXx2ieKrJ1iHRQ-e8AmP4NJlFYMD2bVGI404mYiIhzLIyReinzvIaACZIX09ajFc3ETRwRkUnYXWvtaKJDTAzRulwBF24XGAiCm4V93hAHQuFGvOlgffhpuvcu4T865z6no-XrxPRFMz-zMpI51rAEo5SNSa6dVw6Dd9WdPv4RhvMioKSDrftKMs3C0aKw8_PFEM9dn2fC7a80AhtBuB7WM7fUZwxLGjn17eLv0GzKEcgoKR2HiNXwbO1sfkQ2FJ87A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
تشکر اعضای پرسپولیس از هواداران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/139205" target="_blank">📅 21:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139204">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
🔴
💢
خلاصه بازی پرسپولیس ۳ - ملوان ۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/139204" target="_blank">📅 21:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139203">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
❌
به به چه فوتبالی .چه پرسپولیسی ...سه گل زدیم و شش گل نزدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/139203" target="_blank">📅 21:23 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139202">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
❌
تیم  دقیقه 98 هنوز تو حمله اس و تک به تک نمیزنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/139202" target="_blank">📅 21:21 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139201">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
❌
تیم سه گل زده هنوز سرتاسر حمله و تشنه گلزنیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/139201" target="_blank">📅 21:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139200">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
❌
اورونوف هم تا اومد تو زمین ی پاس سکسی داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/139200" target="_blank">📅 20:52 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139199">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✅
✅
بازیکن ملوان اومد تو زمین سلام کرد و بلافاصله اخراج شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/139199" target="_blank">📅 20:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139198">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">⚽
🤩
سیو تماشایی پیام نیازمند…
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/139198" target="_blank">📅 20:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139196">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6343db8016.mp4?token=dHamEvH6cZ5UyWDHOKsidyyK-EoyBFQLpGjqVDzR2QCDYT9Tg4q7JcRp_Q5NA4jH-DTn4cSnF6hSzr-fEP1P6VhXB9_lGRwTURch24RxSDTFarKI4MC2j9mTxIWogvGrb87-II9R7reK9Aw52cYQxx_g9VGutaO24baqp9Qgd4jCt5ISXBuk_GigiOtqCKHne-IByCxn9Hq5W6n3zy4t23y5lwsFfrvur9pSKDr3HRGb2DV1yDjermXl860QoGpOPfmH__0Oa1B_dynTKG8Wxg5M9-8SV3HSesUI45RErn4hjOUXFglJHXCiiy-ZIYK2k3Q11o6yPYtTNwxKx3W4pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6343db8016.mp4?token=dHamEvH6cZ5UyWDHOKsidyyK-EoyBFQLpGjqVDzR2QCDYT9Tg4q7JcRp_Q5NA4jH-DTn4cSnF6hSzr-fEP1P6VhXB9_lGRwTURch24RxSDTFarKI4MC2j9mTxIWogvGrb87-II9R7reK9Aw52cYQxx_g9VGutaO24baqp9Qgd4jCt5ISXBuk_GigiOtqCKHne-IByCxn9Hq5W6n3zy4t23y5lwsFfrvur9pSKDr3HRGb2DV1yDjermXl860QoGpOPfmH__0Oa1B_dynTKG8Wxg5M9-8SV3HSesUI45RErn4hjOUXFglJHXCiiy-ZIYK2k3Q11o6yPYtTNwxKx3W4pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
🤩
سیو تماشایی
پیام
نیازمند
…
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/139196" target="_blank">📅 20:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139194">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9df197fe84.mp4?token=QeDggdxCWqCTeoxdOClQjytCNf3xPBfjqGSYFiZ-LGgEBiZ1nR4XOkMJE2dxXOn2-jH67Gylv4GopZtFZifZF0XT38R14JjxADwvOAOT14mPa5m58dWA0XQkQKvqzfYcposd4X0awDHhACqIxHCBKBMzFBGk_ESCrz30tae_aA-193lkEWdu84UJdA5v7ed8YPt3qVdCgYdW88KJZJzyLHsRXtFu9kxiZ1dPaNdQWJ0hnafLCK4-WsuJ2sOzbEqzmx6TZcNZqAwcbbZq7NFT8Tl6_uZrcCBOHck-JgpKt3fsjjZDHRMTqU1ARQ7uPlcwNYFNAqiVX__35EL8VZpMjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9df197fe84.mp4?token=QeDggdxCWqCTeoxdOClQjytCNf3xPBfjqGSYFiZ-LGgEBiZ1nR4XOkMJE2dxXOn2-jH67Gylv4GopZtFZifZF0XT38R14JjxADwvOAOT14mPa5m58dWA0XQkQKvqzfYcposd4X0awDHhACqIxHCBKBMzFBGk_ESCrz30tae_aA-193lkEWdu84UJdA5v7ed8YPt3qVdCgYdW88KJZJzyLHsRXtFu9kxiZ1dPaNdQWJ0hnafLCK4-WsuJ2sOzbEqzmx6TZcNZqAwcbbZq7NFT8Tl6_uZrcCBOHck-JgpKt3fsjjZDHRMTqU1ARQ7uPlcwNYFNAqiVX__35EL8VZpMjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
🤩
گل سوم پرسپولیس توسط علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/139194" target="_blank">📅 20:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139193">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
❌
نیمه دوم نکشیم عقب پیروزی پرگلی قبل دربی خواهیم داشت‌.......
✔️
✔️
اقای تارتار یاد بگیر اینجور شجاعانه بازی کردن رو تو بازیا بزرگ نشون بدی
✔️
✔️
همینجوری جلو استقلال بازی کنیم بدون ترس پر گل میبریمشون
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/139193" target="_blank">📅 20:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139192">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
❌
بریم برای نیمه دوم ...بریم برای زدن گل های بیشتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/139192" target="_blank">📅 20:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139191">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a9742c8c7.mp4?token=kPH8PdmlwB9oBf5Jipsw5ObmSaOKHRA_5Jqe7HsQq8FU8B-QTvxcqei7KyaFpGp6Gvt3uD4sN65vRL3u1q9lksI466Nv33GsV1u6KegNVEIKBCTm1E9UzZlho1QLCwz9e3Rg5I_ydVrHiVERIHwa5JEZTBdB2X6SXIsmGovX4dyP8OtuXSp7OIS1ug6ExuzCvCJOVgloQazPNNwhZ0pSGOaa6g7MweVPlqEMu1pPEFd2YREgYqFY_Qf9qMQUGe26t_Dm5gsUd6M9p6K2ShGbv9SszJXrcJDqB4MTr-BKqwQSm3OfvFlhakeLl8r41bXzYAO7JFUO18wjTq6vjp-PnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a9742c8c7.mp4?token=kPH8PdmlwB9oBf5Jipsw5ObmSaOKHRA_5Jqe7HsQq8FU8B-QTvxcqei7KyaFpGp6Gvt3uD4sN65vRL3u1q9lksI466Nv33GsV1u6KegNVEIKBCTm1E9UzZlho1QLCwz9e3Rg5I_ydVrHiVERIHwa5JEZTBdB2X6SXIsmGovX4dyP8OtuXSp7OIS1ug6ExuzCvCJOVgloQazPNNwhZ0pSGOaa6g7MweVPlqEMu1pPEFd2YREgYqFY_Qf9qMQUGe26t_Dm5gsUd6M9p6K2ShGbv9SszJXrcJDqB4MTr-BKqwQSm3OfvFlhakeLl8r41bXzYAO7JFUO18wjTq6vjp-PnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
علی علیپور موقعیت خوب پرسپولیس رو به بیرون زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/139191" target="_blank">📅 20:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139190">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
❌
دیدی خوب بازی کنی نتیجشو میبینی؟
✔️
کاش جلو ترتر اینجوری بازی میکردی آقای تارتار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/139190" target="_blank">📅 20:23 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139189">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5adad84121.mp4?token=Vv1iiTJ1aJ4n9URmChqG_xfXNUbQBERxbdk_hrDj9w3KKp9LmHXGeJiLqkSiY1iIW0rpBVtPYQ9QP9wHyGRPt4KbShkOLmXwel6jeUDN3T0rCJ2qImNvgcLXxq1Q0C1l5pHWgtZwjXf9yozEuomncpNWlrmV05dmzv73XpKeMmngh06yhORuWTElAWw5GMv-_go3bCBoZ3nfS0DFa-pkkKFIJqaQvS9ZaRwdIhfpwa-FAuorlIg-_ILDd0QzfsVwoBlk_AEvGGv20gvI5fPTFr3LWUFXqvhhdvsj9vKyoa3Y66455N4fIkiM2ikYppvng3pbg_kXqDlBoxrYG2L9UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5adad84121.mp4?token=Vv1iiTJ1aJ4n9URmChqG_xfXNUbQBERxbdk_hrDj9w3KKp9LmHXGeJiLqkSiY1iIW0rpBVtPYQ9QP9wHyGRPt4KbShkOLmXwel6jeUDN3T0rCJ2qImNvgcLXxq1Q0C1l5pHWgtZwjXf9yozEuomncpNWlrmV05dmzv73XpKeMmngh06yhORuWTElAWw5GMv-_go3bCBoZ3nfS0DFa-pkkKFIJqaQvS9ZaRwdIhfpwa-FAuorlIg-_ILDd0QzfsVwoBlk_AEvGGv20gvI5fPTFr3LWUFXqvhhdvsj9vKyoa3Y66455N4fIkiM2ikYppvng3pbg_kXqDlBoxrYG2L9UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
در بین دو نیمه اورونوف از سوی طرفداران پرسپولیس به شدت تشویق شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/139189" target="_blank">📅 20:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139187">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">چرا باکیچ رو بازی نمیده حرومزاده کعیر تو گلگهر با بازیکناش</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/139187" target="_blank">📅 20:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139186">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پورعلی کلا وله بخدا باکیچ توانایی جمع کردن وسط زمینو دارت</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/139186" target="_blank">📅 20:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139185">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نظری ندارین که چرا از باکیچ بازی نمیگیره؟</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/139185" target="_blank">📅 20:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139184">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b85faf30c.mp4?token=ULeOB7stLdbsHzQ3OZAZht-Xpi2Z94YSYOuH8H_8uhZ8BpPMjJZGEd_90LGsAu9iQZ5wbBZnzx0lyesFm7HGs49T1WhEdFQYoJVTQ_m9BTHJelsW1VsLmFmAZZJx8_lijAteTW0KHP74L-YJooWowLUjQhgXrMLu_FTpALZKeZUbMjPTsmneGzkvRcWVRxZW5VcS0kQGNst1jmtORs5VdCxVw-BkQK7JmE4XsYDQafTrc1S--XNdbdpbpadSrUs8ILua6VFDwZhhWJgl-962c-EpVtwm5h5Od7aE8_32JBYphmxcox__Q0H-1ZERwud_NP8dnShUmXkK8CYZB5thvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b85faf30c.mp4?token=ULeOB7stLdbsHzQ3OZAZht-Xpi2Z94YSYOuH8H_8uhZ8BpPMjJZGEd_90LGsAu9iQZ5wbBZnzx0lyesFm7HGs49T1WhEdFQYoJVTQ_m9BTHJelsW1VsLmFmAZZJx8_lijAteTW0KHP74L-YJooWowLUjQhgXrMLu_FTpALZKeZUbMjPTsmneGzkvRcWVRxZW5VcS0kQGNst1jmtORs5VdCxVw-BkQK7JmE4XsYDQafTrc1S--XNdbdpbpadSrUs8ILua6VFDwZhhWJgl-962c-EpVtwm5h5Od7aE8_32JBYphmxcox__Q0H-1ZERwud_NP8dnShUmXkK8CYZB5thvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
مهدی تارتار و کریم باقری از گل انفرادی بیفوما به وجد آمدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SorkhTimes/139184" target="_blank">📅 20:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139183">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝙖𝙢𝙞𝙧</strong></div>
<div class="tg-text">چرا باکیچ رو بازی نمیده حرومزاده کعیر تو گلگهر با بازیکناش</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/139183" target="_blank">📅 20:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139182">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSana</strong></div>
<div class="tg-text">پورعلی کلا وله بخدا باکیچ توانایی جمع کردن وسط زمینو دارت</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SorkhTimes/139182" target="_blank">📅 20:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139181">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSahand</strong></div>
<div class="tg-text">نظری ندارین که چرا از باکیچ بازی نمیگیره؟</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/139181" target="_blank">📅 20:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139180">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">📌
وسط وله…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/139180" target="_blank">📅 20:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139179">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">📌
وسط وله…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/139179" target="_blank">📅 20:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139178">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
❌
دیدی خوب بازی کنی نتیجشو میبینی؟
✔️
کاش جلو ترتر اینجوری بازی میکردی آقای تارتار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/139178" target="_blank">📅 20:14 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139177">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRzFPhCzRLKZshgpFC6Z0Bm2NMFAUyVfE3txjIkben1qs5JHljgkPE1wCg_ao4j7ELSgKI-l-KbdwlPJQ6iBeM_Yb-O28M-D9CTkxjgySgf0vx0AMn3LTiRLSbfDoJ16YRp-eK8weMKWacc_ltkvOBOf-HX9IoPq0uD-wWj1COieIykVG_hKSMb3P3u8JmmxtsxM42x0RcIx0dPNpTBw4xS4tCfoFUMinQPIVe41d4v_K8aNdXsUh5IS4iZu9apl8j1P6gtkeVX9NYth011DmBTx0QgdYxO1mp147sQ9hFR6k5SJZ0QcFVQ-_O8DN4qOwcOEM_F3tglKf_rgKy86ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
دیدی خوب بازی کنی نتیجشو میبینی؟
✔️
کاش جلو ترتر اینجوری بازی میکردی آقای تارتار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/139177" target="_blank">📅 20:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139176">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skYmRazasRpDshuFTwOT3DXoasIX-7byvb7w4UqbV-HFkvuzwi22udEDL6FFXwr1TS7mci-56xyC5N6Rli0_zEWDTnPwBPyRfirWkhGV7v6GT03gO6DsBVtF4SRAnGznOU5gQupd-JqxTBABCVd1KWL1op_Vjrryc1b2ZWeHu5FAAcGMkFDEb6JShMYx2veaaNySBsyn8OF__YH1OPBoiwutfuHMPFZVAcVdCHqOZIdIjh8yn4vcWw7D3CNzpvaGYOf39K49XcuUC7q8bhatqRaQlstX4bMKcxZUHkjuix-4PmuMhQeTacPI0Ke4qLbPlktUfePbEy1qLb03S_J4_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
یووه در تورین دنبال دومین برد فصل؛ پارما هم برای جبران شکست هفته اول آمده!
برتری کیفیت و امتیاز میزبانی با یوونتوس است، اما غیبت ییلدیز می‌تواند کار را کمی سخت کند.
نبردی که بوی برد یووه می‌دهد؛ اما پارما می‌تواند برای مدعی دردسرساز شود
[
یوونتوس
⚽️
🆚
⚽️
پارما
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/139176" target="_blank">📅 20:12 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139175">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✔️
✔️
پایان بازی در نیمه نخست
⚪️
پرسپولیس دو - ملوان صفر
⚽️
گل‌ها: محمد پاپی(گل‌به‌خودی)، بیفوما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/139175" target="_blank">📅 20:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139174">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
❌
❌
خداییش دو تا زدیم سه تا نزدیم .عجب تیمی ..چه استارت هایی چه ضد حمله هایی ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/139174" target="_blank">📅 20:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139173">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✔️
✔️
همچنان معتقدم برای این تیم باید کلاه از روی سر برداشت و با این پرسپولیس باید با احترام حرف زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/139173" target="_blank">📅 20:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139172">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63de6c0cf7.mp4?token=j7kr711mUPvE-cJn5lLAsy0_NhZWao2rcZwgLiwXnC1zKfQQdmCp7K3n3490-qSmDLps-DCyyNs8ojHBRiDHFFhJhhryA_4zmpNVJNFBu8scQFNXJFnCR1qcmxm6ihS7uRC2PvnDo2KUrT3jCWLGFPNfqEL5ystt92_Dl-3i1tf3EaEvNhw3msU1w549acrwjV2NobwiPeWtwIy1CyX7lHRZM8_ksbhb5FvHiNAATVgKjiuSO3XgLwoZM0v94NXxmyrFA2ytg9GbU1FzQjmT6Gc5jhtDcLaFbGoh28JRkz20jZulc8h8iH7d9UeGqbC_GVFN2dnSr8VggINzpNa9do_vBHBwMt-72NY8ow9ar28Ea6G9xkIZUTCLjLURQ5PVRbko-7vaPZHSpzXVxO-AxXkPDycMCO07Zu1uqGxVSLcIFnDjyYgryH-enlyhBLgI61O0I4POxgE2grrByWqaWg6NzpPPHVhJajYJuY0guhgCwDqFiyX-ozP_MmJV-M7VAMZgODgmusZTZ1UpnSEwbqL9FT8UfYx4SEcMNF7D-fHZ2-mZygTLOjbFdDJyzcFsOcf7L-7VfC4A9yeUb_s2LnFEf2sGA8mDMBIYjy7xX2wlHb6ms64ZziTWOmaNMrj9ELULkCRRVlL3t4-cr0Jpj3pjyxboBcdZIsBpceQz01E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63de6c0cf7.mp4?token=j7kr711mUPvE-cJn5lLAsy0_NhZWao2rcZwgLiwXnC1zKfQQdmCp7K3n3490-qSmDLps-DCyyNs8ojHBRiDHFFhJhhryA_4zmpNVJNFBu8scQFNXJFnCR1qcmxm6ihS7uRC2PvnDo2KUrT3jCWLGFPNfqEL5ystt92_Dl-3i1tf3EaEvNhw3msU1w549acrwjV2NobwiPeWtwIy1CyX7lHRZM8_ksbhb5FvHiNAATVgKjiuSO3XgLwoZM0v94NXxmyrFA2ytg9GbU1FzQjmT6Gc5jhtDcLaFbGoh28JRkz20jZulc8h8iH7d9UeGqbC_GVFN2dnSr8VggINzpNa9do_vBHBwMt-72NY8ow9ar28Ea6G9xkIZUTCLjLURQ5PVRbko-7vaPZHSpzXVxO-AxXkPDycMCO07Zu1uqGxVSLcIFnDjyYgryH-enlyhBLgI61O0I4POxgE2grrByWqaWg6NzpPPHVhJajYJuY0guhgCwDqFiyX-ozP_MmJV-M7VAMZgODgmusZTZ1UpnSEwbqL9FT8UfYx4SEcMNF7D-fHZ2-mZygTLOjbFdDJyzcFsOcf7L-7VfC4A9yeUb_s2LnFEf2sGA8mDMBIYjy7xX2wlHb6ms64ZziTWOmaNMrj9ELULkCRRVlL3t4-cr0Jpj3pjyxboBcdZIsBpceQz01E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🎥
گل دوم پرسپولیس به ملوان ..استارت انفجاری و برق آسا از بیفوما
✔️
توسط بیفوما 33
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/139172" target="_blank">📅 19:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139171">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✔️
✔️
همچنان معتقدم برای این تیم باید کلاه از روی سر برداشت و با این پرسپولیس باید با احترام حرف زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/139171" target="_blank">📅 19:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139170">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
همگی باید کلاه از روی سر برداریم و ایستاده این تیم و تشویق کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/139170" target="_blank">📅 19:57 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139169">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIWcJz9M3lVuuxsc_z7DqPdkQ1H0sWwKNNvtZvD16Gs6idhGwhOyVyjHfPtc3lZrzQti3rr4l9FXlNTJvs20KiVoVlUomxgsaG2CXM_2wtdjlYPjQL-VhE4OBclxpvDyFfIyQFOu6o3X-WOK8WdAd8ocogvQnGycbuey86oBdBsAyfGhIr66CpoMPJ-xrdXPu0Nxp6qCVew3NgKVxMyJXg57gztbJTNWaao9Tr4sL4w0uR6o_GT_iI3gFyDRJTDMaYLEM9hKcd5q2pnJ6dqy7KxLxN_AxC8ANsq4xd0hmNN813YJaLIYZdvy-PlG6KPxQ4J_mdW86UP2PDF6xUv0_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟥
ورود کاروان پرسپولیس به ورزشگاه شهدای شهر قدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/139169" target="_blank">📅 18:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139168">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78df0f8e05.mp4?token=c6pa0PglvNA5iN0Dl-dskSH7JBZMvjd0hzkFxOML-Rqn_4vHP5fAfERdB6hACvziXkum4eXyc3jCZc6bijzh_LKnK11Envq4p2x-Auw7sIolMJ1LeNJpBtEjsVPdJyKGtNobY3GiwCxD2c7XYEjNW-Kb239KVGTejYsxAPJVL27FksVVUuZXHibOGAO9dY0KttZHHX-c-w6IPRqRaUJ5QGsGyyud53vZkVpDCMpr-6BocUv2Ro-tkVexbPK52pvHnwom1tjTcJBnPS8VCntbOCxCJiOq_tATenfk6filnICcefQXVDP6y9sUHjfD3NvEN5FCLHPD9xss816HqOYL_o2rY6A6sh7DMVsClcPa5HltYhrBN1OvuP2JBxiv2TozW553rh2sugfA1FTHP7X-G9Uk5Lh3P-mzPoWgbH2RUPqkEpm59L1fyLUiKg0ot6RlRsOsNEvUywkRcL8MSSXcJCbt7rZEXUb8DMr7PfEAtDE9my6Fvs4StSheBATB8rv87kYfazvF3RqnRxNr14pqS6DXqnVO0D-mOC39l5HrP26HWARkD2skgviaOlcXTZYb8DyHmErT0p4UaJrFuc3FUFUMpMLhUvmB2TwhwxozKUQAssZvxTpjB8CPE3IG1C0xjfLEgurIYAh7mtkzXb_MQY44YPOXzzFDYPPpNkwxsZM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78df0f8e05.mp4?token=c6pa0PglvNA5iN0Dl-dskSH7JBZMvjd0hzkFxOML-Rqn_4vHP5fAfERdB6hACvziXkum4eXyc3jCZc6bijzh_LKnK11Envq4p2x-Auw7sIolMJ1LeNJpBtEjsVPdJyKGtNobY3GiwCxD2c7XYEjNW-Kb239KVGTejYsxAPJVL27FksVVUuZXHibOGAO9dY0KttZHHX-c-w6IPRqRaUJ5QGsGyyud53vZkVpDCMpr-6BocUv2Ro-tkVexbPK52pvHnwom1tjTcJBnPS8VCntbOCxCJiOq_tATenfk6filnICcefQXVDP6y9sUHjfD3NvEN5FCLHPD9xss816HqOYL_o2rY6A6sh7DMVsClcPa5HltYhrBN1OvuP2JBxiv2TozW553rh2sugfA1FTHP7X-G9Uk5Lh3P-mzPoWgbH2RUPqkEpm59L1fyLUiKg0ot6RlRsOsNEvUywkRcL8MSSXcJCbt7rZEXUb8DMr7PfEAtDE9my6Fvs4StSheBATB8rv87kYfazvF3RqnRxNr14pqS6DXqnVO0D-mOC39l5HrP26HWARkD2skgviaOlcXTZYb8DyHmErT0p4UaJrFuc3FUFUMpMLhUvmB2TwhwxozKUQAssZvxTpjB8CPE3IG1C0xjfLEgurIYAh7mtkzXb_MQY44YPOXzzFDYPPpNkwxsZM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟥
ورود کاروان پرسپولیس به ورزشگاه شهدای شهر قدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/139168" target="_blank">📅 18:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139167">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/153ca3a7ea.mp4?token=RDNNkhHYSU39pvxOxvMVC-x40MVj6-FEZl2m6chsAAOCBxQV6KaF_wTI7jTC-P1Uw9WW5xSPk7I-Lgfx9vgqhpZX1q57Z2nj75LjZtxLW4J-Mc7USbQ_V6Cz7_NmRXZ2-BeGTp371su6ytb0Y-OTfoAhFvratVsv_y-Si_w56BfAsAgt45n3w0UOfjWZubICp0tKMqiVcI6Nfjffr7C_7Cujq3HjODNrnXx-bAH0T_Frs6JIRXHzZUGz5U_5IMZOaNO0zYjNgwQ9dxhSClVggoaZICWuohz7dmVZ2gyA2oAym170zTB4gDMPNSryzI3aEZ-dTH_DXuoOJ-YHgDQ-vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/153ca3a7ea.mp4?token=RDNNkhHYSU39pvxOxvMVC-x40MVj6-FEZl2m6chsAAOCBxQV6KaF_wTI7jTC-P1Uw9WW5xSPk7I-Lgfx9vgqhpZX1q57Z2nj75LjZtxLW4J-Mc7USbQ_V6Cz7_NmRXZ2-BeGTp371su6ytb0Y-OTfoAhFvratVsv_y-Si_w56BfAsAgt45n3w0UOfjWZubICp0tKMqiVcI6Nfjffr7C_7Cujq3HjODNrnXx-bAH0T_Frs6JIRXHzZUGz5U_5IMZOaNO0zYjNgwQ9dxhSClVggoaZICWuohz7dmVZ2gyA2oAym170zTB4gDMPNSryzI3aEZ-dTH_DXuoOJ-YHgDQ-vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کری سنگین هوادار پرسپولیس: آخرین باری که استقلال دربی رو برد دلار ٣۵٠٠ بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/139167" target="_blank">📅 18:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139166">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c76c3af39e.mp4?token=keBimFbnyno-9qJlPpUgq7g00xZVBjNIovzfHa3k3pGqPRONsyMKq5GzNr_yMfdtG5A5ONw7H_NcHnKYezHLlfPJb0Fku-GYP-XVpowMOuWYhHnyLdEJZG2v3G58UpXZ8xaYQSHC0odhjPIWdtVenR72OKEjbAq3HfKSUScpg6GKu61-c5Rn8Qb--51UpjLbLMqc2T7wvIK0tuQI4lz0rvue0B8MYz15b8Dx7nfKOlWkKqd_f49a_X-XLG2uOZs8EipZB92cpkoJ8Duy_2VGIDiAm87wRa4URY7UycJRUO4ymx7WuU0dHfyx9bQzennKLG6J-yedR8egBIQz3W7N1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c76c3af39e.mp4?token=keBimFbnyno-9qJlPpUgq7g00xZVBjNIovzfHa3k3pGqPRONsyMKq5GzNr_yMfdtG5A5ONw7H_NcHnKYezHLlfPJb0Fku-GYP-XVpowMOuWYhHnyLdEJZG2v3G58UpXZ8xaYQSHC0odhjPIWdtVenR72OKEjbAq3HfKSUScpg6GKu61-c5Rn8Qb--51UpjLbLMqc2T7wvIK0tuQI4lz0rvue0B8MYz15b8Dx7nfKOlWkKqd_f49a_X-XLG2uOZs8EipZB92cpkoJ8Duy_2VGIDiAm87wRa4URY7UycJRUO4ymx7WuU0dHfyx9bQzennKLG6J-yedR8egBIQz3W7N1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
⚽
ورود طرفداران پرسپولیس به استادیوم شهدای شهر قدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/139166" target="_blank">📅 18:07 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139165">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76152fe425.mp4?token=RX1RF1_Rf_rVW6Xs_MxzHRsTLuKUF9TOHJ2v9wABp0KoReChZUqmbMvomsMOJrd4Jzamoun4D1ZsgoUhdpGB76ZzkSyEL7dEXS66r3arNIFqvSJJvwjNxvCjEhWLJ18ZAMyBfK_RYWdJn55oQzukVuwvVRpZetK72I0U1nllBD0lGTD11p5bWdaCFhJCfelT_t5pJtB0-Ril1VEGHR58U33V2NCZ8LJjlEYMLz7263l6XvwNl6oF3Xsm86dK4LoVfPDD8G-kJ9o9EcPD471rAJXn92ATWAe_pIdQ5Oqispj4tl0bxMTg23OHFphgvJQQ2ZWFKwj2JxPVshPDAPsphA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76152fe425.mp4?token=RX1RF1_Rf_rVW6Xs_MxzHRsTLuKUF9TOHJ2v9wABp0KoReChZUqmbMvomsMOJrd4Jzamoun4D1ZsgoUhdpGB76ZzkSyEL7dEXS66r3arNIFqvSJJvwjNxvCjEhWLJ18ZAMyBfK_RYWdJn55oQzukVuwvVRpZetK72I0U1nllBD0lGTD11p5bWdaCFhJCfelT_t5pJtB0-Ril1VEGHR58U33V2NCZ8LJjlEYMLz7263l6XvwNl6oF3Xsm86dK4LoVfPDD8G-kJ9o9EcPD471rAJXn92ATWAe_pIdQ5Oqispj4tl0bxMTg23OHFphgvJQQ2ZWFKwj2JxPVshPDAPsphA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
روش جدید ورود هواداران به ورزشگاه شهرقدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/139165" target="_blank">📅 18:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139164">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d95e62021f.mp4?token=ly8eWQbJ-rfQ9UFnX0Yyi0BVOH1eVosS0yp7-AbRHl3Q-cU6P6I107GoJ6HEr2tvoDYqGq43C9_po6CoFj8gfiXRlmuyJhjq2Xu7qVD-oLDjItgKkf7j33pN5v-V3qfV6PJsTdw-xGRab1ZdJ0ICuqzs01RHuNzKisZU4bruK3i4O0rzxzPjaHDeC1WAw3mTlC1zWJxBmxsjpaNOSEehngqLydGtsLGnn5AeKGVJAR4T30Et9-yDPls3zOK9FoErMusvMa2WhjYfOnR-XlakU3QoQ2fS-nbFCxKzfmHcw_ixCKESXg69FpWhEv4uwVWzeFheSygnyASB9nwRx8kIgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d95e62021f.mp4?token=ly8eWQbJ-rfQ9UFnX0Yyi0BVOH1eVosS0yp7-AbRHl3Q-cU6P6I107GoJ6HEr2tvoDYqGq43C9_po6CoFj8gfiXRlmuyJhjq2Xu7qVD-oLDjItgKkf7j33pN5v-V3qfV6PJsTdw-xGRab1ZdJ0ICuqzs01RHuNzKisZU4bruK3i4O0rzxzPjaHDeC1WAw3mTlC1zWJxBmxsjpaNOSEehngqLydGtsLGnn5AeKGVJAR4T30Et9-yDPls3zOK9FoErMusvMa2WhjYfOnR-XlakU3QoQ2fS-nbFCxKzfmHcw_ixCKESXg69FpWhEv4uwVWzeFheSygnyASB9nwRx8kIgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
چمن ورزشگاه قلعه‌حسن‌خان کوتاه و آماده میزبانی از دیدار پرسپولیس و ملوان است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/139164" target="_blank">📅 17:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139163">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
❌
کلیپ باشگاه برای بازی امروز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/139163" target="_blank">📅 17:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139162">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✔️
🎙
روشنک مسئول مسابقات لیگ برتر:
✔️
✔️
شاید جام حذفی را امسال نتوانیم برگزار کنیم، هدفمان این نیست ولی شما ببنید چقدر امسال برنامه‌ها فشرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/139162" target="_blank">📅 16:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139161">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5fbb7cadc.mp4?token=dEKobV7vcNcy1piIeVuqjATnW61bhFwqgp67eI2DJEpqJ_MTDaehreBuijEHoYpMnb_v2NYXMVF-txU26LMdyDWEWrXJZQHsHBori1EKhhzn5MNEFpNb3xBYOpUJ66MVOiexbBaJMt4lyumDcZ2h17GeD_P33_b_rGCpOSsUzRkFyF3PS99EHao4Wca44iXprX3OdqSvubh1XgArHubPScP4CJQE73CwcYTyz33AdskbXJzEQ-5NlmkrReoRolPp3_VZRfHzH3-1DwlNC9DGDv68YKVlfLj56y2x7-XQVyCVlRR5rKH9iCGHQyknVT1tkML-13ciyCCs6DS0Lpg36g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5fbb7cadc.mp4?token=dEKobV7vcNcy1piIeVuqjATnW61bhFwqgp67eI2DJEpqJ_MTDaehreBuijEHoYpMnb_v2NYXMVF-txU26LMdyDWEWrXJZQHsHBori1EKhhzn5MNEFpNb3xBYOpUJ66MVOiexbBaJMt4lyumDcZ2h17GeD_P33_b_rGCpOSsUzRkFyF3PS99EHao4Wca44iXprX3OdqSvubh1XgArHubPScP4CJQE73CwcYTyz33AdskbXJzEQ-5NlmkrReoRolPp3_VZRfHzH3-1DwlNC9DGDv68YKVlfLj56y2x7-XQVyCVlRR5rKH9iCGHQyknVT1tkML-13ciyCCs6DS0Lpg36g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
▶️
این وسط یهو یاد برد ۳بر۰ پرسپولیس جلوی نسف قارشی ازبکستان افتادم، جهنم آزادی، پرسپولیس مخوف و گادوین منشا ‌بی‌رحم
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/139161" target="_blank">📅 15:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139160">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
❌
باشگاه فولاد امروز بار دیگر تمام پیشنهادات پرسپولیس برای جذب رزاق پور را رد کرد و این بازیکن در فولاد ماندنی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/139160" target="_blank">📅 15:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139159">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
خبرگزاری فارس: تارتار دلش می‌خواست سرکیف رو جلوی تراکتور بفرسته داخل ولی تو ذهنش یه تصمیم تاکتیکی گرفت و فکر می‌کرد شهرآبادی می‌تونه بازی رو دربیاره
🚨
تارتار همچنین علاقه‌مند به سبک بازی سرگیف هست اما تعدد بازیکن تو تیم‌ باعث شده به همه بازی نرسه
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/139159" target="_blank">📅 15:48 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139158">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5rhOwcnYBy03bzl0MrntAwf8xHb6oEy-Zd7zgfnD6JpUdz5CPZDsOBN96612lIJOqh5r641Ev2ExiK3R8s-KmZoCnm_h0TIA6gm0QRL_ttKoYbM34IEgnOhIzIQhQe-Sq8Gi7UQoq39cHdJ8Vlz3zp07PtoNvn6YOduY99CEUbJfgGQVdsfgpUayN2bzYrN38ZdLuCxPxHJ3i7Qdq7Gfe8ftp0Rp3yX1E8YQq4IUi_KukAFdcLredSjhGeLu-LDzATrNexZWwNrcBusSJ0pZlt1Bmg-x2byN4wauzbQx6ouois8UBc8Hp12B6W8DPAVn9r1SLygjAQE6IufESmDkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
جریمه 50 میلیون تومانی باشگاه پرسپولیس بدلیل توهین علیه مقام رسمی مسابقه توسط تماشاگران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/139158" target="_blank">📅 15:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139157">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5667f8b6b4.mp4?token=M585R_kNjx6OUtd-LWaRMXfLz8oPtHzMA7IWD2QBohVO0FlVIKn60hvTNleo8SAKtNUZ2FA8RZJ0hITVSDXJjyuQkKFFyz4YaOlePFUWO7nEe_vhfmiSZ4J0F4KG15z37uCMPggbVzeVwZpNm-1DuQ8l0BUuiE8IZsGyIkbS5gNDsT3N6PgRzrA_HVyD2hX9r3B3UBsCbxvKFlmfUvPdIhWw74rrhuYxCqAnwK_Tju183-uIh69peMU5HKQ_XWFvAQYaxyqlTyohwicLbhKGPG05uVcI5pJuDBiodEruiMQcrCBNAJsoZJJjsM72wF6hM_zQtZi8n3CMfH_hpsDuZQfMiGrcMxtqWVI8hP_HCzXQuEdNgW6786U2_gj1yVJ_mzvfpTTmfD7qpwfy7dsx830ZQGHxp6MImmcE7FtLt0LGb8Xf-qzhmvd7ugA7BkY4qf_Ee85XcEKdf53FSTK-6ceDT1XG7ATNno_VEh281IrdNAu4PKW6mvU1O1JOu2ZUyyDihrG46VvKu2dnkX3r5T-PprWOV1iEzSC82AAwRWWTKn2Js1zGZRo61vbss95hIPdN64wxd5S8r8BTvyzwFQ5aTSD2KfYdKp8jNT9-wT62sTeCXMon3m99LeQ2Cb6Fgt9VEnPoBpeOSddMBVxFgKwxyRYo5kCQPKzZizrtcUE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5667f8b6b4.mp4?token=M585R_kNjx6OUtd-LWaRMXfLz8oPtHzMA7IWD2QBohVO0FlVIKn60hvTNleo8SAKtNUZ2FA8RZJ0hITVSDXJjyuQkKFFyz4YaOlePFUWO7nEe_vhfmiSZ4J0F4KG15z37uCMPggbVzeVwZpNm-1DuQ8l0BUuiE8IZsGyIkbS5gNDsT3N6PgRzrA_HVyD2hX9r3B3UBsCbxvKFlmfUvPdIhWw74rrhuYxCqAnwK_Tju183-uIh69peMU5HKQ_XWFvAQYaxyqlTyohwicLbhKGPG05uVcI5pJuDBiodEruiMQcrCBNAJsoZJJjsM72wF6hM_zQtZi8n3CMfH_hpsDuZQfMiGrcMxtqWVI8hP_HCzXQuEdNgW6786U2_gj1yVJ_mzvfpTTmfD7qpwfy7dsx830ZQGHxp6MImmcE7FtLt0LGb8Xf-qzhmvd7ugA7BkY4qf_Ee85XcEKdf53FSTK-6ceDT1XG7ATNno_VEh281IrdNAu4PKW6mvU1O1JOu2ZUyyDihrG46VvKu2dnkX3r5T-PprWOV1iEzSC82AAwRWWTKn2Js1zGZRo61vbss95hIPdN64wxd5S8r8BTvyzwFQ5aTSD2KfYdKp8jNT9-wT62sTeCXMon3m99LeQ2Cb6Fgt9VEnPoBpeOSddMBVxFgKwxyRYo5kCQPKzZizrtcUE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
کلیپ باشگاه برای بازی امروز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/139157" target="_blank">📅 15:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139150">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WvZKV6vd7Aidtg89-OT2pFwCMy6dOHJuoFuMJz8XPcU51zStVpxCii73-KvTzt3KEXvBb2UQ58iwm3pIu6T_yIztsT5H2JFVCEd0nqk84RF03Kaa_-EBfz7AkSZ4JbFqi3f6BIR3Mh95IzAtSzdI695c2qA_qODV1ot0lHWkB1WICnKvFOAaMgM2rGE4Zw6XQ-K2H2f5qjRMP51rZjzR9szRTPbvxLhVT7GfUT8VjXEZhYW-y_hI97gVD_6wheb_yD8nvYUHn1HYeUCxTjmgdwvq822-ojpOCY7OcLvi3aFh-r1rHEv2XAO5KBTyib6XXFBHbv4AkgLQEWRkNs2Zjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TxR_nry9HAsoSKAS66KKgRsPQIxN6_t-3B6vpBeAtDlut9FiTGgKnYDIt-G-FNb_wZbvuvlRS3URrHSn37L79HNsVI35ICl3iAxGETNRqZyl7iCBdbJMyENA7jxaEaVYDOoDTu5MAou6NfVqSc3UJIC6lFZLItZ8NFr-_evp0Com-Fnv4oDdZo1AstzcqW12-sJOxw03YLoKz_US2LFGnPPhoHvDBh6IoAOpLpnNTpnYBWFHJhDdAwDrz9cMgnm7t8MaO3DOhUuVMQ-33RZBZk3iCatROK5NAmECraerXmtBK_8Y7kgg4POL5A_esk0WKcn0Vb6WHsjT9jNmrpDgfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K3uDSX8uacs-wc73En0RTc8Cj9ImkoN6ylqyr1jasLPct63L6VGpkAgRNLO0WqiUiGFmWu1R9UpX3NksSgLS70CJwV3wU3oJQq_6eMMIgVkqKKMIJ7XlYk7Rnybe4dMuXgMpHRIi7o-kXZv3Ar2AJY5GaOEAnm9UzXdRSpVsgzaf2oiw1JwpmAkdkSLwC8KoM5ACe0BQ3JbbZc61BCHNkuizGFaWh7o6VGQ80KyGsCCw7UrWR5KhG8ViD9ZouMzvpsQ7pG7obC-DXkwtB0KFw3xsZKj6yw2BMfRE_9iHHNX2Kb_ayVMXUm_j4VBJTSo9EkXi304WNSBK9ByLfDP-OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HyBLmrxCRFGKLsncmhD_Mr-dCvEhhthPC5CiK5-OLh27Bf-EasHWLFqwgX9auyCLndER3VW2AqzPO_ums_QmVxtiL68dRQeC_xxdtRW9O5VufHBMuReSzUuWFfrE4cGiO6he_IKBYFkmplUtqASqFfofeos3CXc0p7OBhSoGDuqP3M9C1xA0sD5R9VzldCPjZ26ztRZyzrlurOjVUT4z8XfTJLfazrRU_xu2w_6ezB9rsgUOqqO1ABzeCQc3JrG5MzSrCdvRPSFH99AtZXhHNTRSPEdTQJPEIKKin16nwTwbDkfxWNAWfbIjpiVsR8RSaFE0jFZVmhflhUna8z-EMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RfqwZp2YEDRpV4Dbo4BPeIqwcQrkHVYeHnYAc10Qzy5UXkhqHyeFJsTZGTuWhQJEu0hj7o5Xa8jveo2-NHyM93ueC93Nu0mhWbFcA0Bqnd0pjnMx-MAJanTUY0VNi4LyJeTNqqpBrh1pG01Ak00fVPu1opJRirrWUioQAfwuHaf_FZ1SyUsKMxITWxBjGF6VDP3FnLw5v_lDN5YXHi2UYp2OZtYC4HPGM3WMzbz6zgPZZF6QSbxwg3efoot6_w0Vsf_5H4Mrxmup0b_IzR0-t8EgycowxRqG15PTEvhYsczoWMFfkur2R3kyH4rGkwvS5vAAFb6OCYqATbr8wRHQOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g6A9UB8M-h7-iKK6DpNP3zWwyZ12ULKOalEDM0o0RGlvclAQXfL4rbmLk2OKmo7G3badyTR0t5fnDincYC8OFNmU4zPOkl3sgEYwVWSTSgLVwApv707RW6PHlsJIdz7S2vym_15caCtefDc3rPMQn8OwgeoAh9GtsQxRqcf-ctqbF8FjpDXpBbRijYXjAv4gLrKh3v9C3yR209WCMk2Orq4VNpwhUuYdgio00GJDlwetJ0h-bsKF4IFvvbim1kSGW_48rNoeFqN_o55az2QyB95qFlbKEKEGbJAce6iENlaBsrltz5i9iVl7NjETxFwkOBQRrdKKyaObCzHjxTvI8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lWvBJRyunAo5Xid8TiLKEVBHAe4WExhMvvR5M3TzW3OtOqfIXfd6ny--ejFAm6lZEcrqPsoaPtY8vaT3ZT9r_GNDbWyiQIogBZLAVWzITADo4ZUDdqz89Vc21QFsgrUl5MHJABICS2yKs5zSeUNpHZE7hVmoj6b5Au5wSb9OvNSgHbLkuW4q1V3fPsSyOtf1tRt9RbJa-PWAoVu4fGiEZY35Xp2SAH1dr40qU4gx9-dJ4f2DuXpCYTWXn_GtVDd5eSW2e0yCpYstMY1P7guhhLuR60YVBuw5OjEhpL6PgYSgQ0Rpzi7GkHcsND4w31wo9dV3SNM7Ji7lYkfhVFjhaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⭕️
⛔️
حواشی نا تمام هوادار متمول؛گادفادر متوهم ول کن نیست
‼️
🔽
رشته استوری هارا بخوانید…رامین پوکر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/139150" target="_blank">📅 15:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139149">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJ9y2Y6EaWW_36DOSpISK_fiimY05e0luWmn3WEuansnPFyKIQnl-dY_yyuLM0wLAOiSe171Q7nenFAS-Bp3A6UMHW772_nNNzdn1aH-HSTg_9E7NjhGhqj5Bu-BqhH2NmPURjk0No1BdSqjVllPaJOP_tdaGfun_4dykYjzgmrGlgU6X-rhMqLMYTvV98X-zS-EiVdftxV7ItHeyVRl5s19609mH3qtaJTF6Z5v_A5Gp6AP-T_9xBIfJlKlGjCZoiO9UyFCgky-REIOuzbbSCCSjPeqNttiHeYikcOa36EuuvYRsS4-bcAYBwTwUr6Fz1GQqZ_MmxFPc7Cs8rqJVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پایتخت آماده یک شب داغ!
🔥
پرسپولیس دنبال شکار ملوان؛ قویِ انزلی برای غافلگیری به‌میدان میاد!
امشب نوبت کدوم تیمه که حرف آخر رو بزنه؟
[
پرسپولیس
⚽
🆚
⚽
ملوان
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/139149" target="_blank">📅 14:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139148">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KxpzEfMOBAqcQbiH_7B1iTIp433tT_ol5KlhI7p9X_8gB4V0-awIQncdyE9ZZjTS95hWXODpRTquW6z-iCjERjRlzV4KaAZCcjI35iDxfvMlsnkFEDdD9O4_OlY6GE3dQcTeT1FiZnB43AX7A46rWC59MN-2p9sJ2xEh8QojmlGwatmq5hoeZwLTNqt6WIy_c3_el3O_0HT5kLyrzxe8nQ88driWlaemr8xCf6e79mg984PLFe1dAHrjf0ZN6lSUFm-WE0v8BszdbxQLI_dWPy4VcaoLzFFdxImcDazPY2nxDALixJiJvHt_2yV8PRgZl1X7alRtMpnjjKkzIWwxqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
🔻
رضاییان در توجیه رفتنش به استقلال میگفت هواداران استقلال جنتلمن و با فرهنگ هستند اما دیروز هرچی فحش توهین بود بارش کردند وسط بازی هم کلی بطری سنگ و ... سمتش پرتاپ شد !
🔻
🔻
بله آقای رضاییان اینا همون هواداران جنتلمن و بزرگ استقلال هستند که به مادربزرگ مرحوم جلالی هم رحم نکردن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/139148" target="_blank">📅 13:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139147">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✔️
✔️
✔️
حجت کریمی مدیرعامل تراکتورسازی: چون دلار شده ۲۰۰ هزار تومان کسی نباید در مورد بیرانوند صحبت کنه. مردم به فکر مشکلات اقتصادی باشند نه بیرانوند
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/139147" target="_blank">📅 13:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139146">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✔️
✔️
✔️
دنیل گرا مصدومیتش برطرف شده اما تارتار بهش اجازه شرکت در تمرینات رو نمی‌ده و باشگاه هم گرا رو نمی‌خواد ولی تا پایان قراردادش در پرسپولیس میمونه/ فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/139146" target="_blank">📅 13:12 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139145">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfPeeqvPGi2GDbCDBKAwEI69Fl9boNnhh1KhebchE7om8hkSn61vPooRfP9lHwIkKUuei2WBxhJBAQQS_NqfZJSUZ_1d6ivxCqWTZnVe0jBcz2x0zfo68z4xoTsaGS-7npOvLHsjTZkoJksLphsI6Rb2jX1fqi6JKLDoFClF_Xw1Sf3phiDBX8sFDsF6tiOPnlqLcsWiOzvV2QwayBBsIPq6YigGnGe7eX18pzxh7ucTkERwHss1ouBm39WkHkAXGQbER1EcIrHsVIngp2nKEYITMNdlj0vL5s17ntWfF7-tMdgetNGR0Ttuy83WnifVb199-ZKBAqk3XxaoXC3prg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
اتفاق عجیب در لیگ عربستان؛ از هوش رفتن ۵۰ تماشاگر!
🔻
در دیدار الهلال و الخلیج بیش از ۵۰ تماشاگر به دلیل گرما و رطوبت شدید هوا بیهوش شدند.‌ بسیاری از هواداران نیز پیش از پایان نیمه اول ورزشگاه را ترک کردند. الهلال این دیدار را با نتیجه ۵-۱ به سود خود به پایان رساند.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/139145" target="_blank">📅 13:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139144">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✔️
✔️
گفته میشه مدیران باشگاه گل گهر برای شکایت از باشگاه سپاهان بخاطر بازی دادن به کسری طاهری از تیم حقوقی پرسپولیس قبل از شروع مسابقه مشورت گرفتن!   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/139144" target="_blank">📅 11:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139143">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
فووووووووووری
❌
❌
یک سری شایعات پخش شده امسال بخاطر فشردگی تقویم لیگ خبری از جام حذفی نیست و قراره سهیمه آسیایی جام حذفی به چادرملو داده بشه
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139143" target="_blank">📅 09:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139142">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🌬
پایان بازی  نساجی
0⃣
-
2⃣
شمس آذر
🔴
👔
اولین حیا کن، رها کن فصل در قائمشهر؛ روزهای سخت در انتظار مجتبی حسینی!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/139142" target="_blank">📅 09:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139141">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✔️
✔️
✔️
حجت کریمی مدیرعامل تراکتورسازی: چون دلار شده ۲۰۰ هزار تومان کسی نباید در مورد بیرانوند صحبت کنه. مردم به فکر مشکلات اقتصادی باشند نه بیرانوند
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/139141" target="_blank">📅 08:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139140">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
صبحی که ی بازی سخت و حساسی  داریم بخیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139140" target="_blank">📅 08:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139139">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9pbSxfk8AgW_pWaPLpMmZJlIPDyHd7oekDZEwnIcF5xy_W6HrWxw0hxgZe6x-PhB7VvJx5Gc0rzQFViXXd_Vve9AzLQX0PXZYWfHjcSnC-dgI1RhiLExj35IgGmKUl33JpHd8uMlKKMCa7N4XUKpZS6blG6LN8iY_tZy_I9aCTL9w3LbJ5NmLF3ak3ALecH9oaw-6sl7CeUSSi67PerN47maN087Yr1W0rONI3XZObZ5Pz273RdgKr7ypCn0B-naanXa56X14PcQ2_qTlvPDb9V2DzcY-tHxxVfSr8d6Z97CiOhloRCkkBPyftahr_GNqX8ZA5mNyg_qsdiUHJehA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ورود به اسپورت‌نود؛ ساده‌تر از همیشه!
🔗
دنبال یه راه سریع و بدون دردسر برای ورود به اسپورت‌نود هستی؟
🔵
با مینی‌اپ ربات رسمی اسپورت‌نود، مسیر دسترسی ساده و یکپارچه شده؛ بدون لینک‌های متعدد و مراحل اضافی، مستقیماً وارد محیط کاربری شو و از امکانات سایت استفاده کن.
🔗
ربات رسمی اسپورت‌نود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت‌نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/139139" target="_blank">📅 02:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139138">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/241731bcb2.mp4?token=qmPsaYKMYhZ8jDHIkHfP-AWQYqM4vBBCZnnveEWOwmjfa0XSvSqK1OGy8p4ntxZOPJ9BFG9-ZzMi3zs4bGdUwvuMv2tj7tBaaombnivPJYZ01aaJYeAoBv8zkLwq4N-2VX2FdH3bjSOvgsl6alTe6mYRtmxtDuc3PZgWhOSZaba_Bo8DGutRhqydSRydGdYyrMvpwRktC25Z16cKJxPWwKIC-ZHmvhBKrEvrWVX4OJ3wXRLO3c4qckAt-zjpPmJHLLm3E4oZwjuEse16EEplwfk3gluq-XbbO4sNzbaRKfZnb0Rl7HvsTV23xWmNFjv7pPIfeuXNM7b-YW7LAAHnQKOJEi5qWSQ0Xp1ua4NEC4iubZnAONGw1t6MF-QFQ-hBjniXv8NPSMPMVoA2kYCHDds_hBN0ocJe5y-lfIBOCiTgVReB-LkoYGviKCHsFRT9Xm_3k9v3RYbqQz3u_IXMkkxfyGRERB4LocYqLhE7-HRXXynd_vqUfEgP3ipKp8gzcE87Bsynpoxk_GKn47rIFL4xskA8jvvKdXl78XQVl12lAP_8k4cgqHeFjDlY9nVkP_KEbo9bfDyZ1Ap3RcPIC9tYbhGQ7kC9Agc5BaOyMFhYLgdekfrZZduntiSXwB937sWRQqch3XlCOu6L5Ua71FaC_Dv-mFyQm0D73W95-s0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/241731bcb2.mp4?token=qmPsaYKMYhZ8jDHIkHfP-AWQYqM4vBBCZnnveEWOwmjfa0XSvSqK1OGy8p4ntxZOPJ9BFG9-ZzMi3zs4bGdUwvuMv2tj7tBaaombnivPJYZ01aaJYeAoBv8zkLwq4N-2VX2FdH3bjSOvgsl6alTe6mYRtmxtDuc3PZgWhOSZaba_Bo8DGutRhqydSRydGdYyrMvpwRktC25Z16cKJxPWwKIC-ZHmvhBKrEvrWVX4OJ3wXRLO3c4qckAt-zjpPmJHLLm3E4oZwjuEse16EEplwfk3gluq-XbbO4sNzbaRKfZnb0Rl7HvsTV23xWmNFjv7pPIfeuXNM7b-YW7LAAHnQKOJEi5qWSQ0Xp1ua4NEC4iubZnAONGw1t6MF-QFQ-hBjniXv8NPSMPMVoA2kYCHDds_hBN0ocJe5y-lfIBOCiTgVReB-LkoYGviKCHsFRT9Xm_3k9v3RYbqQz3u_IXMkkxfyGRERB4LocYqLhE7-HRXXynd_vqUfEgP3ipKp8gzcE87Bsynpoxk_GKn47rIFL4xskA8jvvKdXl78XQVl12lAP_8k4cgqHeFjDlY9nVkP_KEbo9bfDyZ1Ap3RcPIC9tYbhGQ7kC9Agc5BaOyMFhYLgdekfrZZduntiSXwB937sWRQqch3XlCOu6L5Ua71FaC_Dv-mFyQm0D73W95-s0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#منهای_پرسپولیس
👤
فراز فاطمی سرپرست چادرملو:
❌
آقای حیدری فکر کرده ما خریم. قشنگ بگید میخواید یه تیم ببازه دیگه اینجور قضاوت کردن بخاطر چیه. امیرحسین حسین‌زاده با تکلی که زد دوبار باید اخراج میشد ولی حتی صحنه به وار
هم نرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/139138" target="_blank">📅 01:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139137">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✔️
✔️
براساس‌صحبت‌های‌مهدی‌تارتار؛ سرگیف از بازی فردا مقابل ملوان به ترکیب سرخ‌ها برمیگرده و تارتار میخواد زوج علیپور - سرگیف استفاده کنه اما اوستون اورونوف همچنان نیمکت نشین خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/139137" target="_blank">📅 00:57 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139136">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
❌
استقلال فولاد مساوی تموم شد.کیسه خیلی خسته و کوفته شد و واسه دربی قانونا خسته میاد تیمش امیدوارم استفاده کنیم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/139136" target="_blank">📅 00:29 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139135">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
کشاله‌درد دوباره شجاع خلیل‌زاده در بازی امشب مقابل هواداران یزدی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/139135" target="_blank">📅 00:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139134">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
کشاله‌درد دوباره شجاع خلیل‌زاده در بازی امشب مقابل هواداران یزدی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/139134" target="_blank">📅 00:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139133">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32fe7cb793.mp4?token=VST0WhEmUeAddlklq9a7z7JLlxqp7xInc402BCHHycZYxU1d0mWZL7sSzy-738rnuuhLAg2mQ3Gvw4tv_ROBRcWnR-1Qlpv7AiyfEfqxvodasQ-QGdAMNJTxxnfumtf47Er5Xuq5XF1B2bPgfVNku50ZHFg7X80HTlzYdL65G1KwwwXjJXkiHrOkVkvLTn8rM2SuMASiZzRiSTVx5y9p1xGctlBWpczJTIWLvsyJ7hO24bFI0M3tSpjzSKxJ7-jsZutxMKvYphp6Ju_i0AB1r4qI_ZS7r7ROcsJuf1vaCPsvJM-AZOuoiei8PGwXbGqcejxcFkimAv4RZ4MmcJSdcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32fe7cb793.mp4?token=VST0WhEmUeAddlklq9a7z7JLlxqp7xInc402BCHHycZYxU1d0mWZL7sSzy-738rnuuhLAg2mQ3Gvw4tv_ROBRcWnR-1Qlpv7AiyfEfqxvodasQ-QGdAMNJTxxnfumtf47Er5Xuq5XF1B2bPgfVNku50ZHFg7X80HTlzYdL65G1KwwwXjJXkiHrOkVkvLTn8rM2SuMASiZzRiSTVx5y9p1xGctlBWpczJTIWLvsyJ7hO24bFI0M3tSpjzSKxJ7-jsZutxMKvYphp6Ju_i0AB1r4qI_ZS7r7ROcsJuf1vaCPsvJM-AZOuoiei8PGwXbGqcejxcFkimAv4RZ4MmcJSdcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
کشاله‌درد دوباره شجاع خلیل‌زاده در بازی امشب مقابل هواداران
یزدی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/139133" target="_blank">📅 00:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139132">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/867c2d8104.mp4?token=YT2W3kdDVbTARlzJdUMoEv0H27F7Tdz2vpPtmLiz_uIXzHsnuhMLD4HWvOeSldWIi7oWAd9eihYvyJ8fmoaqEwEYh73jT45dvDWmG23Exd65jlKMCEPJRPwB_xiYdpu_iN4CGkv3iOrFySM7ZwqMkyu6-r6w8GI9wj5IQEAAjDzuI-nmcSP88Cx9xGOxLK1lxQOUb4My1DCqYWkmzbty1rF177I0wBx2QRKQwT31t0J6OKeitH7ihScLrnggeuYNP0tWhg3rnSeTi0h7gNfYdL8Da5yhMKK2Jlacb7-paxs4w5z_ig_C9vwxCxFqzyXB3cUlM2FdCURfceq94BttIRX9z_vr04XkLul496vfdx648f5rFRFpYykMrNQ0pk-r5gwzQ8bOvJDyU2RpckAdoEcwveGyMXu3FeqYG2RaEJX5PM4JlcaEzAdvQnGXVbZgGUWAiFNk2Vvl0kRKprUBerFJAwBjWlSjRpRG3QKvGHHYZne1oL5MbnzR8oB6dZ3ECKkedkDAln15McbJmGIihRRi0oQBD3WeAGcRNwH9Y4sgff4pLPxcnJQ8wc4__2hYvn4ib7HYeFUGi2yzGVRibxsO4n_lenqaNXy7b7Pn6eodlv2m3l1xVIYGehcnQ8FoCsZk26iQJvoT-mfbo4h_nQJMhWGpzNWOkiNwauClmqs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/867c2d8104.mp4?token=YT2W3kdDVbTARlzJdUMoEv0H27F7Tdz2vpPtmLiz_uIXzHsnuhMLD4HWvOeSldWIi7oWAd9eihYvyJ8fmoaqEwEYh73jT45dvDWmG23Exd65jlKMCEPJRPwB_xiYdpu_iN4CGkv3iOrFySM7ZwqMkyu6-r6w8GI9wj5IQEAAjDzuI-nmcSP88Cx9xGOxLK1lxQOUb4My1DCqYWkmzbty1rF177I0wBx2QRKQwT31t0J6OKeitH7ihScLrnggeuYNP0tWhg3rnSeTi0h7gNfYdL8Da5yhMKK2Jlacb7-paxs4w5z_ig_C9vwxCxFqzyXB3cUlM2FdCURfceq94BttIRX9z_vr04XkLul496vfdx648f5rFRFpYykMrNQ0pk-r5gwzQ8bOvJDyU2RpckAdoEcwveGyMXu3FeqYG2RaEJX5PM4JlcaEzAdvQnGXVbZgGUWAiFNk2Vvl0kRKprUBerFJAwBjWlSjRpRG3QKvGHHYZne1oL5MbnzR8oB6dZ3ECKkedkDAln15McbJmGIihRRi0oQBD3WeAGcRNwH9Y4sgff4pLPxcnJQ8wc4__2hYvn4ib7HYeFUGi2yzGVRibxsO4n_lenqaNXy7b7Pn6eodlv2m3l1xVIYGehcnQ8FoCsZk26iQJvoT-mfbo4h_nQJMhWGpzNWOkiNwauClmqs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎤
بخش دوم صحبت های تند خداداد عزیزی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/139132" target="_blank">📅 23:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139131">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🎙
درگیری شدید خداداد با خبرنگاران یزدی
!
پ.ن باز شروع شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/139131" target="_blank">📅 23:58 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139130">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✔️
✔️
✔️
منهای ورزش :همراه اول تو جدیدترین شاهکارش، سقف مصرف بسته اینترنت ۷ روزه «نامحدود» شبانه رو از ۱۰۰ گیگ رسونده به ۲۰ گیگ!
✔️
اینترنت نامحدود تو ایران = ۲۰ گیگابایت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/139130" target="_blank">📅 23:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139129">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
سپاهان از استقلال شکایت می‌کند
❌
❌
باشگاه سپاهان به دلیل استفاده از یاسر آسانی در دیدار مقابل استقلال از آبی‌های تهران شکایت خواهد کرد.
❌
❌
این در حالی است که چند روز قبل سخنگوی سازمان لیگ استفاده استقلال از یاسر آسانی را قانونی دانسته بود.
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/139129" target="_blank">📅 23:39 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139128">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✔️
✔️
گل‌گهر از سپاهان به خاطر کسری شکایت کرد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/139128" target="_blank">📅 23:36 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139127">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">📷
جدول لیگ برتر پس از پایان روز اول از هفته چهارم  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/139127" target="_blank">📅 23:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139126">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XswXWersliIz9jToXUdCHxrVVYwl0KuHtZOfLjEJzo_uc6twP5EyPwf1BJh2ypTCRIr0A0kwXnoH0p-E2Rww0yR37d3UNgicyPwWFKb6Cv5FZFJ-aSomWTPgEGteeQ5uSZOnPeM2i3JtgtsT4OOW0YnZCYxSpjavLFa_hT8CXV4MkOrjai0egF_Si-vzMbxyM5TqhHJ0CScc4HjGVQoO2gNljxWmvSyIzvlC0teBHdo9kHE332pxhZ8hm-tiLQ9IAP8RJBFgbqzKKbvgRdzdZoB_-YTOJj1yMTkIbxnaZfBuF-pp8OYVKbCM1kp5z6kk82n6yVmkdd83uA44cG4ltA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
جدول لیگ برتر پس از پایان روز اول از هفته چهارم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/139126" target="_blank">📅 23:29 · 06 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
