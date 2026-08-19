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
<img src="https://cdn4.telesco.pe/file/S5MCnZJDAdSMxyFbmzelaw5waxrF2xudSBw4Pp1sB0QWtjf56TqnhZIAeVnA0MVCsKNLOvSqbUy2rrPdn1jefQNXAETX8tv_82EbcGqqms2fcs7RyJJOkIn2ghhiSbfZDt9-tPhjJEgupO4UprXlsWcjaZnufXObGzklyJOQvQIVPPrzzmNlHgrK-ZrJf_cQYmte0sT_9jhKD7RX2wFKPwBtVYvVqSVmMR-3-KR1-ZQ6ELH_nJySxe4EWJm_IdZktWn4gUyNgD68mWzRtUN1jn3fDbsgqf3CgcN2mhSJ5ZxJrBAy7BswdDYIh220V_AU-21Li8wzMQmEqfH58dLeKQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-28 22:30:02</div>
<hr>

<div class="tg-post" id="msg-138620">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❌
❌
مهدی تارتار، سرمربی پرسپولیس:
✔️
✔️
هدف ما از اول این بوده همه بازی ها را ببریم. هواداران پرسپولیس این شکل بازی را دوست دارند. بر اساس فلسفه هوادار خواسته های خود را جلو می بریم.‌در یک پست باید تقویت شویم .از مدیریت باشگاه تشکر می کنم و از آنها می خواهم…</div>
<div class="tg-footer">👁️ 410 · <a href="https://t.me/SorkhTimes/138620" target="_blank">📅 22:29 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138619">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
❌
❌
بازگشا:
❌
بازی با تراکتور و درخواست تماشاگر؟ باید مجموعه مدیریتی باشگاه تصمیم بگیرد
✔️
اگر تضمین بدهند که بازی برگشت در آزادی 100 هزار نفر هوادار ما بیاید می توانیم تصمیم بگیریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 653 · <a href="https://t.me/SorkhTimes/138619" target="_blank">📅 22:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138618">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
❌
مهدی تارتار، سرمربی پرسپولیس:
❌
باید از هواداران تشکر کنم که در برد امروز سهیم هستند.از بازیکنانم کمال تشکر را دارم که از دقیقه یک فوق العاده بودند. نشان دادند امسال می توانند کارهای بزرگی کنند.استقلال خوزستان کادر و بازیکنان جوان و خوبی دارند
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 802 · <a href="https://t.me/SorkhTimes/138618" target="_blank">📅 22:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138617">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
❌
مهدی تارتار، سرمربی پرسپولیس:
❌
باید از هواداران تشکر کنم که در برد امروز سهیم هستند.از بازیکنانم کمال تشکر را دارم که از دقیقه یک فوق العاده بودند. نشان دادند امسال می توانند کارهای بزرگی کنند.استقلال خوزستان کادر و بازیکنان جوان و خوبی دارند
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 837 · <a href="https://t.me/SorkhTimes/138617" target="_blank">📅 22:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138616">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
❌
تشویق بی امانه تارتار در استادیوم ..همگی دارن از این تیم هجومی و جذاب لذت میبرن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 934 · <a href="https://t.me/SorkhTimes/138616" target="_blank">📅 22:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138615">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">📌
به عقیده من تیم با خرید یکی دو بازیکن دیگه ۱۰۰٪ تکمیل میشه
❌
یه دفاع چپ و هافبک دفاعی… بنظرم میشه به همایی فرد اعتماد کرد چون دفاع چپ ایرانی تو مارکت نیست و اگرم بخایم خارجی بگیریم باید با دو تا از خارجی ها فسخ کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/138615" target="_blank">📅 22:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138614">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔖
⚽
به باد این دوتا برد نباید بخوابیم،عیار تیم تو بازی های بزرگ مشخص میشه، با دو تیم نسبتا ضعیف بازی داشتیم اما عالی بودیم اما هنوز برخی ضعف های تاکتیکی هست که باید رفته رفته برطرف بشه ولی از همه جهات این دو بازی عالی بودیم تمام بازیکنان مون عملکرد خوبی به نمایش…</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/SorkhTimes/138614" target="_blank">📅 22:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138613">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔖
⚽
به باد این دوتا برد نباید بخوابیم،عیار تیم تو بازی های بزرگ مشخص میشه، با دو تیم نسبتا ضعیف بازی داشتیم اما عالی بودیم اما هنوز برخی ضعف های تاکتیکی هست که باید رفته رفته برطرف بشه ولی از همه جهات این دو بازی عالی بودیم تمام بازیکنان مون عملکرد خوبی به نمایش گذاشتن
◀️
و به لطف باشگاه تیم خوب و سرحالی بسته شده، همه باید از تارتار و حدادی حمایت کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/SorkhTimes/138613" target="_blank">📅 22:16 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138612">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
❌
حساس‌ترین بازی هفته سوم لیگ برتر پشت‌ درهای بسته باید برگزار شود؛در شرایطی که براساس رای فروردین 1404 کمیته انضباطی و تائید استیناف تمام دیدارهای تراکتور و پرسپولیس مقابل هم در مسابقات لیگ برتر جام حذفی و در دو فصل 1405_1404 و 1406_1405 باید بدون حضور تماشاگر…</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/SorkhTimes/138612" target="_blank">📅 22:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138611">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
رسمی؛ با اعلام سازمان لیگ دربی پایتخت برای اولین‌بار قرار است در اصفهان و ورزشگاه نقش جهان برگزار شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/SorkhTimes/138611" target="_blank">📅 22:08 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138610">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9bca5c905.mp4?token=maKqyPalGPreNJkvYe2jtKTZ5MuzKEBUUGIOQLu1MeSPqRNsioAAoPEDH6nVL9Br3taB7nxWmNbwMRUdXaZ6-2HrJPeo-h9SPaR-GGv2s77p9LKRPG6eU-v_k-7sZjyIrXWN0T-UYFUBKXVQOfEU1DBnKBtuxNs4nqwSCmg6pYEEytuVc4oybbhKqN8_cMBHdy-778MfGxmWnSnt9lv7S07XdOKNNncS55TQoEZQdn99lGqDHKz8xjlp0FX7fbGjNOvBf8_FromK_mc7XfWy2TXyo4GOhfftGDYb13NRPkQVpRiKHjoHw9rOtyXX3A9ulCeuuKhvyj6rVu1SpggKfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9bca5c905.mp4?token=maKqyPalGPreNJkvYe2jtKTZ5MuzKEBUUGIOQLu1MeSPqRNsioAAoPEDH6nVL9Br3taB7nxWmNbwMRUdXaZ6-2HrJPeo-h9SPaR-GGv2s77p9LKRPG6eU-v_k-7sZjyIrXWN0T-UYFUBKXVQOfEU1DBnKBtuxNs4nqwSCmg6pYEEytuVc4oybbhKqN8_cMBHdy-778MfGxmWnSnt9lv7S07XdOKNNncS55TQoEZQdn99lGqDHKz8xjlp0FX7fbGjNOvBf8_FromK_mc7XfWy2TXyo4GOhfftGDYb13NRPkQVpRiKHjoHw9rOtyXX3A9ulCeuuKhvyj6rVu1SpggKfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🎙
بهنام ابوالقاسمپور؛مدیرعامل استقلال خوزستان:‌
🔻
با حدادی در مورد بیفوما حرف زدم.
🔻
ما باید مبلغی به کمیته وضعیت می دادیم اما چون ندادیم نورشرق به نفع پرسپولیس رای داد.
🔻
الان پول رسیده و باشگاه پرسپولیس هم گفته مشکل را حل کنیم و دیگر کار به دادگاه عالی ورزش نرسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/SorkhTimes/138610" target="_blank">📅 22:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138609">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/154eade970.mp4?token=hjrY9bbkX3Evv5TVqY5Hpbl3OAvuX-bzUG-fyqn4EF2-W14UXuJxdvVFJLYAfpCEhNCqwkAqkeWFpKnHOk7bEHfpVrJ-Nism58piwxX6TjjeG7oYpPD-QP9L-t-9R5rBtJ8zRYS_bBowjFr7O7OIX259qRt2fnHrucQI5LcG82oUpQqW73mgcXqXoXnRAANtqVGEgpI8_9yQVZQ1FosOSUYJWlzpdo1p2t70OY9Vd2SULNqY9j1BxWKQnNeD0hrjp08aNo_zi1S3NP5ZLdPMxpdXVbg9tMEkDrOQoq7ncPXndFC3_fKx2ICRAcGdJC04LJTUwUWzcCaAuEIdBX3XDTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/154eade970.mp4?token=hjrY9bbkX3Evv5TVqY5Hpbl3OAvuX-bzUG-fyqn4EF2-W14UXuJxdvVFJLYAfpCEhNCqwkAqkeWFpKnHOk7bEHfpVrJ-Nism58piwxX6TjjeG7oYpPD-QP9L-t-9R5rBtJ8zRYS_bBowjFr7O7OIX259qRt2fnHrucQI5LcG82oUpQqW73mgcXqXoXnRAANtqVGEgpI8_9yQVZQ1FosOSUYJWlzpdo1p2t70OY9Vd2SULNqY9j1BxWKQnNeD0hrjp08aNo_zi1S3NP5ZLdPMxpdXVbg9tMEkDrOQoq7ncPXndFC3_fKx2ICRAcGdJC04LJTUwUWzcCaAuEIdBX3XDTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
شادی هواداران پرسپولیس و اعضای این تیم پس از سوت پایان بازی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/SorkhTimes/138609" target="_blank">📅 22:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138608">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c286dc680.mp4?token=QahQO88x35PmuYu-ibSWFzo-JrOD58xw6u1kSMwC6AuYIQMBZcW-cvNWxnZT_vTbO3_2lbbPv3mgiDgbCzy3e-KwBYBsFXrNmXMboNT_YU_z9PKv2GnQwyrAwKa5GUmGGoXdlGoKsPfGzbRykdsMNvUGqt-AFmJQGBjlC75P-OWXQKg6GShUZvNSuj7KrMPrUBdrRL4sD96O8VpBn6aks4S3r1DHunPxRkNKhJ_ZffrSovlxjEZC5gmMwU0Cd2hcO0AnCD0CREqccsBR7DL1bycG3zNRMENysJNaTiNW2kOFfUMwv-NfRHrZGRtjvP8b74aqgHza0wqy3vuJXONYmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c286dc680.mp4?token=QahQO88x35PmuYu-ibSWFzo-JrOD58xw6u1kSMwC6AuYIQMBZcW-cvNWxnZT_vTbO3_2lbbPv3mgiDgbCzy3e-KwBYBsFXrNmXMboNT_YU_z9PKv2GnQwyrAwKa5GUmGGoXdlGoKsPfGzbRykdsMNvUGqt-AFmJQGBjlC75P-OWXQKg6GShUZvNSuj7KrMPrUBdrRL4sD96O8VpBn6aks4S3r1DHunPxRkNKhJ_ZffrSovlxjEZC5gmMwU0Cd2hcO0AnCD0CREqccsBR7DL1bycG3zNRMENysJNaTiNW2kOFfUMwv-NfRHrZGRtjvP8b74aqgHza0wqy3vuJXONYmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
گل چهارم پرسپولیس به استقلال خوزستان توسط پوریا شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SorkhTimes/138608" target="_blank">📅 22:03 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138607">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34f62d7868.mp4?token=Qlz3yoE32BFe428jX2kwFJi2UOx76FmaNAmV061SH4JQVOK7OCWlha2Q4bqQAKxfCCTrLoCLAQIrzKHOnkDBkAxss4uI_8k-nQyYDIwMWVnzWleY9-OiT9pYckXkJ9_SZvTxl5nrvaoUPkuHnZn8AAa4R1eMBBrIebCiVo7dBMfSLRu9yMwQoiiBH_vN0equZLzsidfaVa0qRBuGHLc6qUnP4IEpy65F9lL6-Lov41Vxc0r-5nQNo4ar-n6TNbqG0mCoQNkRmY5nAvOkevoWcBTHmpcuilFuPos-QO5owZe_N5MNOsrYcEkpHVUTa_--lXKcNpO95tIftlZizlnbgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34f62d7868.mp4?token=Qlz3yoE32BFe428jX2kwFJi2UOx76FmaNAmV061SH4JQVOK7OCWlha2Q4bqQAKxfCCTrLoCLAQIrzKHOnkDBkAxss4uI_8k-nQyYDIwMWVnzWleY9-OiT9pYckXkJ9_SZvTxl5nrvaoUPkuHnZn8AAa4R1eMBBrIebCiVo7dBMfSLRu9yMwQoiiBH_vN0equZLzsidfaVa0qRBuGHLc6qUnP4IEpy65F9lL6-Lov41Vxc0r-5nQNo4ar-n6TNbqG0mCoQNkRmY5nAvOkevoWcBTHmpcuilFuPos-QO5owZe_N5MNOsrYcEkpHVUTa_--lXKcNpO95tIftlZizlnbgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
❤️
گل سوم پرسپولیس به استقلال خوزستان توسط ایگور سرگیف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/SorkhTimes/138607" target="_blank">📅 22:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138606">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6f4fb205d.mp4?token=Twl1YCNvu_T0IjS2Zjmg2M1l1itGs934fR46B5PEVke57-i3_px8A-QV1tLRB-cA-pMDA6vG50WkwW1yCM8bC3BhvQbqsN6V0oeeS8CcnjmiacdPwfVEFLMV6Ddkf2UB5kRapc8ol30KCp2BsBm_t-A-92DpnpM4VOwqVvTquY7zi7-TaL-q2rqu9f6t0tS49Ch_ObJa0cuP-tIpohJzyRlC3Zg_m30n5TJhLm9XxFFdFhdQWOMnf1qRYcXtfrcFpokJEfyDJEJ2N_P-jXGQf1wr98NrOZPqXOEqtkVA2pbzBw2l4Ls2yqVmWbvAPBSdoREU5q45ti4fQu51T3otQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6f4fb205d.mp4?token=Twl1YCNvu_T0IjS2Zjmg2M1l1itGs934fR46B5PEVke57-i3_px8A-QV1tLRB-cA-pMDA6vG50WkwW1yCM8bC3BhvQbqsN6V0oeeS8CcnjmiacdPwfVEFLMV6Ddkf2UB5kRapc8ol30KCp2BsBm_t-A-92DpnpM4VOwqVvTquY7zi7-TaL-q2rqu9f6t0tS49Ch_ObJa0cuP-tIpohJzyRlC3Zg_m30n5TJhLm9XxFFdFhdQWOMnf1qRYcXtfrcFpokJEfyDJEJ2N_P-jXGQf1wr98NrOZPqXOEqtkVA2pbzBw2l4Ls2yqVmWbvAPBSdoREU5q45ti4fQu51T3otQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
🤩
گل دوم پرسپولیس به استقلال خوزستان توسط علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/SorkhTimes/138606" target="_blank">📅 21:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138605">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fbb512d19.mp4?token=IUK-RyGJ1-WFAvDZMFwqCTfvnx1z9dmCxxjrpqzSl6UYUWlajwwyex58cB7NPZ4lDS0RJrIVTSa1LttThK_HmhfcGo1_OUdOZE2xSQXSQBLFpJmGnVtdT6MrZkC9Rz2wB3E-ZOWxtaHNmxE_MRUO1kH5ogtZJS1HYgjhOUoMeWizsN9cJF0D7XB8TDnMPn8e2Xn9UC95aaj6YZAUKol-OPeFR6K-rKXQkvyQMsDj9Vf90vSL1OFWYrs6O8qB9yLnzu2cIWdoOiN1HOo0-v3aEJ3oxWCtpKsJUkTlyWAF4SVkxYglEG_-6b_fyTT5OCr5iqP8loXEQvoy_9VZTcHN5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fbb512d19.mp4?token=IUK-RyGJ1-WFAvDZMFwqCTfvnx1z9dmCxxjrpqzSl6UYUWlajwwyex58cB7NPZ4lDS0RJrIVTSa1LttThK_HmhfcGo1_OUdOZE2xSQXSQBLFpJmGnVtdT6MrZkC9Rz2wB3E-ZOWxtaHNmxE_MRUO1kH5ogtZJS1HYgjhOUoMeWizsN9cJF0D7XB8TDnMPn8e2Xn9UC95aaj6YZAUKol-OPeFR6K-rKXQkvyQMsDj9Vf90vSL1OFWYrs6O8qB9yLnzu2cIWdoOiN1HOo0-v3aEJ3oxWCtpKsJUkTlyWAF4SVkxYglEG_-6b_fyTT5OCr5iqP8loXEQvoy_9VZTcHN5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
🤩
گل اول پرسپولیس به استقلال خوزستان توسط محمد خدابنده‌لو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SorkhTimes/138605" target="_blank">📅 21:57 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138604">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚫
خطا روی باکیچ و بیفوما نگرفت به هردو کارت زرد داد مادر به خطا
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/SorkhTimes/138604" target="_blank">📅 21:57 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138603">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❤️
👤
تعویض ها مهدی تارتار مقابل استقلال خوزستان
🔴
۱- همایی فرد: عملکرد قابل قبول
🔴
۲- بیفوما: یک پاس گل و عملکرد خوب در جریان بازی
🔴
۳- ارونوف: عملکرد خوب در جریان بازی
🔴
۴- شهرآبادی: یک گل و عملکرد در طول بازی قابل قبول
🔴
۵- باکیچ: اثر گذاری روی گل چهارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SorkhTimes/138603" target="_blank">📅 21:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138602">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTyv38dwZdzRJwxl-0OqUeYgHDnRX5Y_0IP-IRhOe3uGK0mbwVkXSRW6ayvy49yhRz33lxGqJtxYz6nuIdge9A9gcbTpBs68jPfzD0973JgtzPoyi51ACZ_BDqi15cGbdH01vW1exawCM2QC4gDgULrwnSzMyClfcQKV0HB4_J5ou3cg2AJgcM6QV8oWMt453OaqE4WCHI6w-aUGunQCQL3QaSLztszmYj1Y1bck75l_nWxUOouHds42-7nCRQxV5mS9mszXW6fjHv0V6pqh0uEWzzPmwyNIcFL7QSP_nGaEAubi_ltcHcY3WtBJR8NLyhigaS1sWC8kvW1LxsNd4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
علی علیپور، مجید عیدی و ایگور سرگیف با نمرات 8.8، 8.4 و 8.0 بهترین بازیکنان دیدار امشب دو تیم پرسپولیس
🆚
استقلال خوزستان بودند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/138602" target="_blank">📅 21:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138601">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">⚡️
⚡️
شنیده میشه تیوی بیفوما در یک ماه اخیر برای ماندن در پرسپولیس زیر نظر پزشک تغذیه باشگاه 8 کیلو کاهش وزن داشته و علاوه بر اون زندگی حرفه ای شو سالم تر از قبل کرده و تمرکز اصلی شو روی فوتبال خودش گذاشته!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/138601" target="_blank">📅 21:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138600">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0ArRvwo2X7QGmQE8LXgLxNeqv_4s4W7A1OFjn9gQdF6oBaI3N-xRrAX7ol9DxdRbrhAdCWZiWiCDTGFrrOeTxaRFD4vI-fX4k29PGOvjRCy9pdIrrj3VczRbCDdscWVsKeN30N8hIENNp9LeAJk7cxlkNOLOwZvUYw2Ezjzi-tZbONfi8S85WqeRUaQ5COdT_LK0wa0I21cqlBP9_3D2_KgD85WxfIh175JjiyqQ3HoFk9ijisPw6rhRTlKb-0ZboDdR7uO5ZnQh-kBtMhWdcjfdl4rslxC8XBSZ3cPY-PrqTPTK5xCtYpx7plpeajZCkOpav1Yz2Hy_pK-g2wUeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
صعود به صدر جدول با چاشنی گلزنی تمام مهاجمان/پای علیپور، سرگیف و شهرآبادی هم به گلزنی باز شد
❌
پرسپولیس 4
❌
استقلال خوزستان 1
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SorkhTimes/138600" target="_blank">📅 21:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138599">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✅
✅
مبارکه با چهار گل بردیم ..دو بازی شش گل زده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/138599" target="_blank">📅 21:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138598">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚫
داور حروم زاده ریدم پس کله پدر جاکشت اکرم حروم زاده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SorkhTimes/138598" target="_blank">📅 21:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138597">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
❌
گل چهارم هم زدیم توسط شهر آبادی 19 ساله و با زدن گل بالا رفتیم صدر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SorkhTimes/138597" target="_blank">📅 21:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138596">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚫
داور حروم زاده ریدم پس کله پدر جاکشت اکرم حروم زاده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/138596" target="_blank">📅 21:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138595">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
❌
پای جلالی خوب نشده بود و دوباره گرفت و تعویض شد و جاش همایی فرد جوون اومد داخل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/138595" target="_blank">📅 21:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138594">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
❌
گل چهارم هم زدیم توسط شهر آبادی 19 ساله و با زدن گل بالا رفتیم صدر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SorkhTimes/138594" target="_blank">📅 21:29 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138593">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
❌
تشویق بی امانه تارتار در استادیوم ..همگی دارن از این تیم هجومی و جذاب لذت میبرن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/138593" target="_blank">📅 21:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138592">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">⚡️
گل سوم هم زدیم ...بلند شید و این تیم و ایستاده تشویق کنید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/138592" target="_blank">📅 20:49 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138591">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
همگی باید کلاه از روی سر برداریم و ایستاده این تیم و تشویق کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/138591" target="_blank">📅 20:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138590">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✅
✅
نیمه دوم میتونیم شاهد ورود اورونوف و شهرآبادی و تیکدری به زمین باشیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/138590" target="_blank">📅 20:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138589">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_lgBu7cho_U6fihpQvU6zkJwH7AX0mWb27QEAmjZ0Vqknq1qX-cWjfBe1r7knCRHVskoediJXtW4xwV9gnrvujCStcgCpqDKU4tqJYX-JqEjkNu9MkUvVQVVuusJgkOunJsy63AFEsjQTZojWyQQ6MmuX25F4ecwdm2TpYxMJPJNpEqZNLqLFvxsjKZn9IGHFJElKPzpdrknYLJK8pmvPks2H4eEv6QUNhf8nBPKMDfH8IB8qiCjkt37V4rVRFXWMUOeQFNYHfr1qNu1XoFGxhHjRsKYbGDrBUWdK7DwBnlgETttTpY6JXDGdeizCkCrSFvilA7QQeU9dBElKP5Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
️ بونوس اختصاصی چرخش رایگان بازی Scarap Temple
💰
کاربران اسپورت نود می‌توانند از همین حالا، با هر بار شارژ حداقل ۱ میلیون تومان، متناسب با مبلغ شارژ خود ‌اسپین رایگان کازینو دریافت کنند.
💸
هرچه مبلغ شارژ بیشتر باشد، چرخش رایگان بیشتری دریافت خواهید کرد! با هر چرخش، شانس برنده شدن جوایز نقدی را دارید؛ جوایزی که بدون هیچ قید و شرطی مستقیماً به موجودی اصلی شما اضافه می‌شوند.
🔗
آدرس ورود به سایت اسپورت‌نود:
👇
🔵
نسخه جدید سایت:
Sportn5b2.com
🔵
نسخه قدیمی سایت:
Sport90.bet
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/138589" target="_blank">📅 20:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138588">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
❌
مثل نیمه اول با اختلاف زارع بهترین بازیکن زمین بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/138588" target="_blank">📅 20:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138587">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
❌
نیمه اول و با دو گل پیروز شدیم ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/138587" target="_blank">📅 20:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138586">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
❌
گل دوم هم علیپور زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/138586" target="_blank">📅 20:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138585">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
⚽️
بااعلام‌باشگاه پرسپولیس؛ مصدومیت ابوالفضل جلالی جدی نیست و این بازیکن مشکلی برای دیدار هفته آینده مقابل استقلال خوزستان ندارد. جلالی امروز بازی  درخشانی در ترکیب سرخ‌ها داشت.  سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/138585" target="_blank">📅 20:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138584">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
❌
باید برای این پرسپولیس تارتار ..تیم جذاب و هجومی با احترام حرف بزنیم ..چه تیمی درست کرده تارتار.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/138584" target="_blank">📅 19:53 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138583">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✅
✅
گل اول و خیلی زود توسط خدابنده لو زدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/138583" target="_blank">📅 19:52 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138582">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
❌
با اختلاف سه گل ببریم میریم صدر جدول..الهی به امید تو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/138582" target="_blank">📅 19:49 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138581">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">⚡️
⚡️
جمعیت خوبی هم رفته دم هوادار گرم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SorkhTimes/138581" target="_blank">📅 19:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138580">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
❌
با اختلاف سه گل ببریم میریم صدر جدول..الهی به امید تو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/138580" target="_blank">📅 19:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138579">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
❌
🔴
📸
شماتیک ترکیب پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/138579" target="_blank">📅 19:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138578">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
❌
🔴
📸
شماتیک ترکیب پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/138578" target="_blank">📅 18:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138577">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
نسبت به بازی اول فقط جای سرگیف و بیفوما تغییر کرده و همچنان اورونوف روی نیمکت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/138577" target="_blank">📅 18:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138576">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
❌
🔴
📸
شماتیک ترکیب پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/138576" target="_blank">📅 18:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138575">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5SkboM3RZN9xZSRAjKjx432V666TWfdLmoSPML7BCYHi0Qq_37PkyiPKe10-K6e7y6Vj2jKqpdDZtRqnk7lrxX35Y6aqNuABY2_9MjxiPkUVhtqSUhKizJ1Cb4eD6F7OVoq_1sudvbRlIbYfDW2A5P6M6Y72957wauMUgJRzzocbDtiBnJrBaacN238U87GjBeO9CpghYyfBpGNNv9s8R9oMMD3aJqjsg4MNCwBvioLB6t32puTdLmruhqAKWTJB1sFW31bxoAuht4qL3ceY9Jwfhj1NvPHzoBVKCE6YrhhjEPHq632w-_qBiIdR1QKyrmMLMw0LaBSpzbiinErCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
شماتیک ترکیب پرسپولیس برابر شمس‌آذر  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/138575" target="_blank">📅 18:30 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138574">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d137678386.mp4?token=RZqlqT4FPAmSdEcflafwbaVql0FKZOcjrBHgcfTUIi5-70YkLxTcnUiiYpM551KWb83WQry0ynpjNRV7fhTxHVN1axWSLSPqlNYbh8Vnz8lwCEq1hCXm0wUZzYMCDSfXJ-WI3Dd0SPVbajPDPJPj1SViD1IyjvxaGDlRhQELfZej2V9QoWS8GqIvhzP6QDBeTC8i3lvwzxfp5yxKHWbU5RpW41gMSbD9UtTRR3nWOEzo7zgqOIk9bq6_XtBpc7pNEUvu5aO4U-0_4-gKRnNBJdh6h16P9BF9vwEhYjs4EGfyYU8PCQeni1BEDiOsuUac-pfyqzARDtBD5-96REQHTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d137678386.mp4?token=RZqlqT4FPAmSdEcflafwbaVql0FKZOcjrBHgcfTUIi5-70YkLxTcnUiiYpM551KWb83WQry0ynpjNRV7fhTxHVN1axWSLSPqlNYbh8Vnz8lwCEq1hCXm0wUZzYMCDSfXJ-WI3Dd0SPVbajPDPJPj1SViD1IyjvxaGDlRhQELfZej2V9QoWS8GqIvhzP6QDBeTC8i3lvwzxfp5yxKHWbU5RpW41gMSbD9UtTRR3nWOEzo7zgqOIk9bq6_XtBpc7pNEUvu5aO4U-0_4-gKRnNBJdh6h16P9BF9vwEhYjs4EGfyYU8PCQeni1BEDiOsuUac-pfyqzARDtBD5-96REQHTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟥
‼️
هوادار پرسپولیس: تیمی که ۷ گل خورده و دسته سه رفته، به ما نمی‌خوره! فینال آسیا واقعی رو ما دیدیم. استقلال بره آسیا ۷ تا بخوره، خوشحال میشیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/138574" target="_blank">📅 18:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138573">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff8f1d1ef5.mp4?token=M0QMToN37a0nt1TxLTDV-YJgJZzolj8aWbuvf-sFmVTx3S45PFUDIw-Sncw0ol6oDkae0DtagJDswQNeVB_dOEEOnpEVq23cKmBNrTWoNz-oG-P8CprpZVbvJ4y4ZQfv9V2Q_nCIq3juRonKPnOz5XxlwBFMppxfR7f_l78kJTFfJJdVWfnPKFyZKcK__ciUHPz4NHrG6Rz3Au0hdakuN9XLjl_ssNTk-JVkd6e5h8p5w0aiCN3wValtXMQmesqN7crxCwkS56N1zfbTi4RUvkM8sBqpq5WhNecq3DGwucVVRByiKJro6239XtqAtajM67s7OC36L1aKOS6-PVH2Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff8f1d1ef5.mp4?token=M0QMToN37a0nt1TxLTDV-YJgJZzolj8aWbuvf-sFmVTx3S45PFUDIw-Sncw0ol6oDkae0DtagJDswQNeVB_dOEEOnpEVq23cKmBNrTWoNz-oG-P8CprpZVbvJ4y4ZQfv9V2Q_nCIq3juRonKPnOz5XxlwBFMppxfR7f_l78kJTFfJJdVWfnPKFyZKcK__ciUHPz4NHrG6Rz3Au0hdakuN9XLjl_ssNTk-JVkd6e5h8p5w0aiCN3wValtXMQmesqN7crxCwkS56N1zfbTi4RUvkM8sBqpq5WhNecq3DGwucVVRByiKJro6239XtqAtajM67s7OC36L1aKOS6-PVH2Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟥
🔴
هوادار پرسپولیس: از رنگ آبی و استقلال نفرت دارم! تارتار تیم خوبی ساخته و پرسپولیس همیشه قهرمانه. استقلال تیم نیست، عروس آسیا هست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/138573" target="_blank">📅 18:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138572">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a524ae095.mp4?token=PO7r9zb__K03ULbQRWLmEozbOV5KxwQvAzJHQKaaVopZ7UOw5IdUYDxqy2ZDyJWzJrPtGw9T26eaYCz88P5DiXb1BQdUkLBddrh6yCEJ-O-ei0k9jkCX19EgDm45qu1JIwFhi2RxXhsyrgIUPFn_g1jOn3aJI0fIULJJuI2JOVQE23u4YOQEUBe4wslbrJ4c7KecyySv9cw7UUuXuvK01KfRJLkDDLC4hBykQ6JbkugRH-AUX6KTVCJ9H2Q4OeEisLNBJvSDVSiQFyYxu4SdhreHeincx3xJ2gLLXg45C34R40cZCkUgvIS9p_8OMy7oEbyePbybeYuwTRTSkVXcBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a524ae095.mp4?token=PO7r9zb__K03ULbQRWLmEozbOV5KxwQvAzJHQKaaVopZ7UOw5IdUYDxqy2ZDyJWzJrPtGw9T26eaYCz88P5DiXb1BQdUkLBddrh6yCEJ-O-ei0k9jkCX19EgDm45qu1JIwFhi2RxXhsyrgIUPFn_g1jOn3aJI0fIULJJuI2JOVQE23u4YOQEUBe4wslbrJ4c7KecyySv9cw7UUuXuvK01KfRJLkDDLC4hBykQ6JbkugRH-AUX6KTVCJ9H2Q4OeEisLNBJvSDVSiQFyYxu4SdhreHeincx3xJ2gLLXg45C34R40cZCkUgvIS9p_8OMy7oEbyePbybeYuwTRTSkVXcBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏅
وضعیت ورزشگاه شهرقدس در فاصله یک ساعت و نیم تا شروع بازی پرسپولیس.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/138572" target="_blank">📅 18:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138571">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3a1e95c93.mp4?token=tOTlMSDd_HE6BzREFE0LvJ0PlxtX5mN5PpvPr8isrO8Ydin8NArE0c8V_DRzbQxRJ8uRa4qC9OsACLNBfP1hvclCKNMU4_BB68JyDJaTmmUXoTlWoow2xxblrccgnfEZpxAQ542W_WgzbhgvEQh1OYS1M5LyEccv2tqF2F0KNJ0pc6x5o11xkiXBDe3KXb4cGq01MkpOvnmzGy1X-PXu-_M5haIejCNX2LdCjNt3aKzZnHKgId75jVd5q-ew_q6vWVQH8ZW1Z2kSGTXaNA4axnUVPXHiD-V5ZmyUcCweuJFmn-mCqTbNyKj7YgVjAVWnfDNmML-qSSmGtwOi0BTSNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3a1e95c93.mp4?token=tOTlMSDd_HE6BzREFE0LvJ0PlxtX5mN5PpvPr8isrO8Ydin8NArE0c8V_DRzbQxRJ8uRa4qC9OsACLNBfP1hvclCKNMU4_BB68JyDJaTmmUXoTlWoow2xxblrccgnfEZpxAQ542W_WgzbhgvEQh1OYS1M5LyEccv2tqF2F0KNJ0pc6x5o11xkiXBDe3KXb4cGq01MkpOvnmzGy1X-PXu-_M5haIejCNX2LdCjNt3aKzZnHKgId75jVd5q-ew_q6vWVQH8ZW1Z2kSGTXaNA4axnUVPXHiD-V5ZmyUcCweuJFmn-mCqTbNyKj7YgVjAVWnfDNmML-qSSmGtwOi0BTSNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ورود اتوبوس تیم به ورزشگاه برای مصاف با استقلال خوزستان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/138571" target="_blank">📅 18:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138570">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">⚡️
مدیر برنامه آسانی: نامه فسخ دستکاری شده است
🔹
مدیر برنامه یاسر آسانی، هافبک استقلال، انتشار نامه فسخ قرارداد این بازیکن را تکذیب کرد و مدعی شد نامه منتشرشده با هوش مصنوعی دستکاری شده است.
🔹
رسانه‌های مختلف امروز نامه‌ای منتسب به فسخ قرارداد یاسر آسانی با…</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/138570" target="_blank">📅 16:49 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138569">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❌
دانیال ایری در لیست پرسپولیس برای دیدار با استقلال خوزستان قرار گرفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/138569" target="_blank">📅 16:44 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138568">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
❌
شوک بزرگ به طویله کیسه/ نامه مشاور حقوقی یاسر آسانی که اعلام کرده قرارداد رسما فسخ شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/138568" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138567">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gh8fRqQqG4Zx-5HAWUNF2h8N70bQ773WQvXFJzC36ttvReDQqt5qZUOB2ALDFEPr7_eE9uLKPQopltnRp9M_GHtKpGM1z3GA1rPX-kK4T7FD92QF-vG-pG5KV9qAM11PrwewuPUG9jdiSzd1gwmmEHZtpX-iX6oxCFSmmb5B0Ln_QlqlYCqdlQMhoYxCA0ecePPryamF9v-eXVO7ZSQiO8Oa1YJV3am50-kCTUrxNMaoO6ZFAGNhbD7_DGO_O78wSZLI70pV-FG_WHKBsdKik7vUJM07SXP2x8vYtoXDHFVZEtyJno1w_nTCchW6N5zHI4ASv1Sr1LDdhShEdI6Lug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رسمی؛ با اعلام سازمان لیگ دربی پایتخت برای اولین‌بار قرار است در اصفهان و ورزشگاه نقش جهان برگزار شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/138567" target="_blank">📅 16:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138566">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1Xt_d1hIS0PqqZvQP1yZmYLs0zFL9cIIMoXM2Uh81DwsPSFZ-StMhVmX1x9zLFwKieE1EZp_FgQtA5TzaJzyW9ccc0NgLVZNH18DpamRoTORCOpZ7cU2HrBFa58_3bC-DiiRUuLw17Nyjn-K3nVkTNuxqD7K7Gl0Ieh79YJBcZDO9WeqKunftB9iMt2m0LUsIlTLZ3aGCqH4nQCGVNxZGFnA1QRJxWL--YNeCS6RsUe3qRJEbTAmbRUezAlQYMnYNSuUu0ANhMBkEVD-ICN2apTTwlLklSxDHkylHmZN1Dl8qOP6SX8TSR14yvZQK2EOkkUSffH2xythc14VWz5uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
استوری وحیدقلیچ: رییس فدراسیون فوتبال روسیه دنبال منه
🤣
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/138566" target="_blank">📅 16:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138565">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">📊
🇮🇷
🇮🇷
نتایج ۵ بازی رودررو اخیر پرسپولیس و استقلال خوزستان:
🇮🇷
پرسپولیس ۳-۰ استقلال.خ
🫱🏻‍🫲🏻
پرسپولیس ۰-۰ استقلال.خ
🇮🇷
استقلال.خ ۱-۰ پرسپولیس
🇮🇷
پرسپولیس ۴-۳ استقلال.خ
🫱🏻‍🫲🏻
استقلال.خ ۲-۲ پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/138565" target="_blank">📅 16:08 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138564">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e06320f5f.mp4?token=gl0UF5OerE0_YFxoYDebJuFr2sqXbWQ3BpgnuUr0wvLHoY45b76kPzMokWID1TfWPdGLRxZWAj84WPAnI5VWQEAXGGabsB0GEXf3rdfPQ-UkbCi8bA2cHLCvs3B0Dh8cW0CU66TUPAKm7oZlSUkKjhHVJkC-jRJSR1ea7NsW7Ejd9ioKw7KMH7JYymCyAWiHJ4p4ewOS2WFNTzwEGrtXransNVuOXHIrZkjRkjxVux4QQlulzZi_6ID2Y4B1Vzywd3phoG-yEk3HztbJxddp4H3eyDBDP83Ya5z4bTOiQxYqGQHvjJif5OEcOXirIl7poqAx1TUvEsZMi8Z048RtNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e06320f5f.mp4?token=gl0UF5OerE0_YFxoYDebJuFr2sqXbWQ3BpgnuUr0wvLHoY45b76kPzMokWID1TfWPdGLRxZWAj84WPAnI5VWQEAXGGabsB0GEXf3rdfPQ-UkbCi8bA2cHLCvs3B0Dh8cW0CU66TUPAKm7oZlSUkKjhHVJkC-jRJSR1ea7NsW7Ejd9ioKw7KMH7JYymCyAWiHJ4p4ewOS2WFNTzwEGrtXransNVuOXHIrZkjRkjxVux4QQlulzZi_6ID2Y4B1Vzywd3phoG-yEk3HztbJxddp4H3eyDBDP83Ya5z4bTOiQxYqGQHvjJif5OEcOXirIl7poqAx1TUvEsZMi8Z048RtNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🏟
ثابت قدم مدیرعامل شرکت توسعه و تجهیز:
ورزشگاه آزادی اویل آذرماه آماده می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/138564" target="_blank">📅 16:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138563">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2698fac3f.mp4?token=bNUIiMQ7cIBrbemoZYJ8J2FOve7nOa5JE9VFj9PiIPIABq32BMftdsghaAzcl6mbSJWAgwZtclUr1KROjA3a38d9JXPl3VX6jSHJGB1LNoL1LxlRQ9n7jOqJ5sK1xhwSVaz2i0iTA24ag75xFyApP92IwA5UNS0a0QCHtGEJRXRhBVIeQ5KgFdITcmE_T-YKNRY9Ut3UB5Bnw69HU7dTCLXx_8-OwViu1oyWUCx6AqAUQpkRResJMLvcXlDB0BGGLAXnl2oSphZBpMbn5fKXAZN4d1tZ2QIlZxj-rLtvbgQ-R9LXpclhm5DXC8l0iOaX7Lx3mlRYkFulgrotcfnjYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2698fac3f.mp4?token=bNUIiMQ7cIBrbemoZYJ8J2FOve7nOa5JE9VFj9PiIPIABq32BMftdsghaAzcl6mbSJWAgwZtclUr1KROjA3a38d9JXPl3VX6jSHJGB1LNoL1LxlRQ9n7jOqJ5sK1xhwSVaz2i0iTA24ag75xFyApP92IwA5UNS0a0QCHtGEJRXRhBVIeQ5KgFdITcmE_T-YKNRY9Ut3UB5Bnw69HU7dTCLXx_8-OwViu1oyWUCx6AqAUQpkRResJMLvcXlDB0BGGLAXnl2oSphZBpMbn5fKXAZN4d1tZ2QIlZxj-rLtvbgQ-R9LXpclhm5DXC8l0iOaX7Lx3mlRYkFulgrotcfnjYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⛔️
آقای کمیته انضباطی اگر یکبار به صورت قاطع برخورد کرده بودید و درگیر رانت و فساد تلفن بازی نمیشدید،الان کشالش رو میکرد تو
کون
ناموسش به مردم توهین نمیکرد مسبب این بی قانونی و فساد اخلاقی رفتاری شما حضرات هستید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/138563" target="_blank">📅 16:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138562">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✅
✅
✅
کمیته انضباطی قصد دارد به صورت ویژه شادی گل جنجالی شب گذشته شجاع خلیل زاده را مورد بررسی قرار دهد و با توجه به سابقه او در انجام شادی های جنجالی، احتمال محرومیتش وجود دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/138562" target="_blank">📅 14:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138561">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
❌
❌
کشوری فرد دبیر سازمان لیگ برای بازدید از ورزشگاه نقش‌جهان در این ورزشگاه حضور یافت. بر این اساس، احتمال دارد دربی استقلال و پرسپولیس در هفته پنجم، روز 11 شهریور در نقش‌جهان اصفهان برگزار شود.
✔️
✔️
گزارشگر دیدار روز گذشته سپاهان و تراکتور نیز در جریان مسابقه…</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/138561" target="_blank">📅 14:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138560">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byAW3CJWweLTRhGawcWhaGQ2P9GB1wk4SPaDzJ2sPagsKCOlKn1nTFLaAaQY3sq71Ki8rQ_6h8r1veiJm2dpFlYGePjXqLPBm3ksY6xaDt-4KB_yl97LHU3lLTQh5JLXttSm1-VwkHGWGe9PkxyCTimojNcGBWmRfpbMe9mzlRvLHT1bf2vc-G09fe08skk9fbNboE_WQiHyFzLb7QbWx93LFwjs3I8TLX-uLdnikPBfnGeXVXF6cXvISNK38cQcJawiWABKBcfLigp0VAGfhaFYfH06X5HIE7BZc2ztM9dhovb6uT30i5cCumm0hgO7xs4nM0ctGAfEV08Jh7OOPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽
نبرد سرخ‌ها با آبی‌های خوزستان؛
پرسپولیس برای شروعی قدرتمند، استقلال خوزستان به‌دنبال غافلگیری!
⚽️
لیگ خلیج‌فارس ایران
[
پرسپولیس
⚽
🆚
🇮🇷
استقلال‌خوزستان
]
⏰
چهارشنبه ساعت ۱۹:۳۰
🏟
استادیوم شهرقدس
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
🌐
نسخه جدید سایت:
Sportn5b2.com
🌐
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/138560" target="_blank">📅 13:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138559">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
با درخواست کیسه به عنوان میزبان دربی ، دربی رفت به احتمال خیلی زیاد اصفهان و ورزشگاه نقش جهان باشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/138559" target="_blank">📅 12:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138558">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
فوری؛ باشگاه نساجی مازندران از باشگاه استقلال تهران شکایت کرد
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/138558" target="_blank">📅 12:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138557">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
محمد گندمی، یعقوب براجعه، دنیل گرا، امیرحسین طاهری، علیرضا عنایت زاده و کوروش اژدهاکش از لیست پرسپولیس برای بازی فردا خط خوردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/138557" target="_blank">📅 12:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138556">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❌
⚽
باز هم حرکت عجیب و منشوری شجاع خلیل‌زاده، بعد از خوشحالیِ گل!!!
❌
پ.ن و بازم کشاله ران بوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/138556" target="_blank">📅 12:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138555">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
❌
آسانی بازم فیکسه!
❌
مدیران نساجی ام گفته بودن مستندات جدیدی دارن، چه شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/138555" target="_blank">📅 12:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138554">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✔️
قدوسی: پرسپولیس و تراکتور میدونن که الوحده قربانی رو نمیده ولی از ترس اینکه اون یکی جذبش کنه پا پس نمیکشن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/138554" target="_blank">📅 10:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138553">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
❌
فوری: بازی تراکتور و پرسپولیس در هفته سوم بدون تماشاگر برگزار خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/138553" target="_blank">📅 10:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138552">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
⚽️
🧡
رامین رضاییان میان تشویق شدید هواداران فولاد با شعار « رامین، رامین، رامین ما دوست داریم » وارد خوزستان شد؛ فقط کلاه رامین رو ببینید
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/138552" target="_blank">📅 10:24 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138551">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❌
❌
مهدی تارتار قصد دارد از سیستم چرخشی در هفته های ابتدایی استفاده کند تا ضمن آمادگی تمامی بازیکنان فشار کمتری به تیم وارد شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/138551" target="_blank">📅 10:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138550">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
❌
جنجالی‌ترین بازی هفته سوم بدون تماشاگر
‼️
✔️
✔️
تراکتور و پرسپولیس هفته آینده باید در دیداری حساس پشت درهای بسته به مصاف هم بروند. تراکتوری‌ها حالا به دنبال تعلیق محرومیت هواداران هستند تا سکوهای تیم‌شان را پس بگیرند؛ تصمیمی که می‌تواند روی بازی برگشت در…</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/138550" target="_blank">📅 10:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138549">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQ_SGiuezat29CWI-oL1xowMmAUyuMWw71GEZIn1AGaFh-X6HtEvR5YiXHsQF1vU-4w9_WxWkIMy5mtf4CE54jmw97g9kX-5LeoE_v2m1Lfmv3L1vnSXb-hfkjc4DcnuG7t3viMuqF9bZ_DTyuDXrPQJNp8FN1wLk-CmB1VHbdmq7g8hw5zrRqYU7GpwtYT1dOX4C7toUeyfousos0FAcS4n_oFJMsDeWoEtude4dBzXA97NdoMQX3fpE2_0Te6G5mvlSR-j4aIFSTgf30RfIXhY8bJW61eqKHvuKB2ypFd_XYX9bu4mGligwh4rr_oiOfsG3NIqoPJAwvqKM36K-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
️ بونوس اختصاصی چرخش رایگان بازی Scarap Temple
💰
کاربران اسپورت نود می‌توانند از همین حالا، با هر بار شارژ حداقل ۱ میلیون تومان، متناسب با مبلغ شارژ خود ‌اسپین رایگان کازینو دریافت کنند.
💸
هرچه مبلغ شارژ بیشتر باشد، چرخش رایگان بیشتری دریافت خواهید کرد! با هر چرخش، شانس برنده شدن جوایز نقدی را دارید؛ جوایزی که بدون هیچ قید و شرطی مستقیماً به موجودی اصلی شما اضافه می‌شوند.
🔗
آدرس ورود به سایت اسپورت‌نود:
👇
🔵
نسخه جدید سایت:
Sportn5b2.com
🔵
نسخه قدیمی سایت:
Sport90.bet
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/138549" target="_blank">📅 01:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138548">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
❌
حسین زاده :بهمون گفتن بازی با پرسپولیس بدون تماشاگره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/138548" target="_blank">📅 01:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138547">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✔️
✔️
✔️
تارتار تو تمرین امروز چند تا ترکیب چیده و هر کدوم در یک رسانه قرار گرفته
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/138547" target="_blank">📅 01:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138546">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQarnTpWxH84On-2eYDbOLwwj_0IW_OdtzN2hP4SMZMgn_zZ9TlU30RfV7XhcjAYwZcgTUhDpC2f6rkVBQjaoWGX200-cVK3PlSJUV5YQ0YDi35N_ymHAxC00Q3QJO4jG5GEUWK7y9aWE0cfgGLSrDCjVRNwEDuHqKHLRa0c72wRxIRZK36ZFXi3be3qzYRP9Ft2vtw3WiHLTZuDSG27qYi3l4p-9u9lSlm4HwZH11WE1uWJvxM0F5zw9ix2LJwWSEb5vxuwc6vtV7r9dYx9aOH_eNHhkCJIBINFsiElFCRtfS3ZrKIwyr6ZY836Y4O34zNb2LnbOb0wBhZMVGhgxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
استقلال و سپاهان هفته سوم باهم بازی دارن
بعد اگه جفتشون از آسانی و طاهری استفاده کنن و بعدش بفهمن جفتشون غیر قانونی قراردادشون ثبت شده و تخلف بوده نتیجه بازی چی میشه
🙁
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/138546" target="_blank">📅 00:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138545">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❤️
گل اول تراکتور به سپاهان توسط امیرحسین حسین زاده 83
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/138545" target="_blank">📅 00:54 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138543">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
❌
❌
مهدی تارتار تصمیم داره دیگه حتی تو آخرین تمرین قبل از بازی هم ترکیب تیم رو اعلام نکنه تا ترکیب لو نره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/138543" target="_blank">📅 00:20 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138542">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🏟️
آخرین وضعیت سکوهای ورزشگاه آزادی و وضعیت زهکشی و زیرسازی چمن این ورزشگاه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/138542" target="_blank">📅 00:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138541">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
⚽
باز هم حرکت عجیب و منشوری شجاع خلیل‌زاده، بعد از خوشحالیِ گل!!!
❌
پ.ن و بازم کشاله ران بوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/138541" target="_blank">📅 00:14 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138540">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✔️
✔️
البته طبق حکم دایمی بازی لیگ دو تیم پرسپولیس و تراکتور بدون تماشاگره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/138540" target="_blank">📅 23:57 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138539">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
مس شهربابک از استقلال به خاطر استفاده از آسانی شکایت کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SorkhTimes/138539" target="_blank">📅 23:42 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138538">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
عینک‌زاده: فوتبال دعوا نباشد که لذت ندارد باید دعوا کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/138538" target="_blank">📅 23:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138537">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
⚽
باز هم حرکت عجیب و منشوری شجاع خلیل‌زاده، بعد از خوشحالیِ گل!!!
❌
پ.ن و بازم کشاله ران بوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/138537" target="_blank">📅 23:36 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138536">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a31203bb22.mp4?token=bv5iR_88PkYpof0_UD-AmFzett0o2q_AP4cx3ku5YutwD4UZsoQt7UR7sOGzsfZJW00p7UF95xMUXDB81M4XsG4r02-E1ChZCiKkebeYaLyMzCMb3JbP0Ht2Ir20ncQaemunBjZFJ2eFwRAi8osKVueCm8Jpz-wqhmQS5B3Dt0_m878CSODkkFKLAgREuuGnjS8jNtxlU3tjZf9ekzdxoaH0f62h-O1a4QZGcoZPGZOqf5o8VO4q3r-WNsfrCs3U98ZbrPByYwHwCiTon0fIOeOKgKoKQA-6sLgCaAlxu8nXFqOYa5Rm995bfLCIY03TFJeYzVW8WYj0QemeZc9w5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a31203bb22.mp4?token=bv5iR_88PkYpof0_UD-AmFzett0o2q_AP4cx3ku5YutwD4UZsoQt7UR7sOGzsfZJW00p7UF95xMUXDB81M4XsG4r02-E1ChZCiKkebeYaLyMzCMb3JbP0Ht2Ir20ncQaemunBjZFJ2eFwRAi8osKVueCm8Jpz-wqhmQS5B3Dt0_m878CSODkkFKLAgREuuGnjS8jNtxlU3tjZf9ekzdxoaH0f62h-O1a4QZGcoZPGZOqf5o8VO4q3r-WNsfrCs3U98ZbrPByYwHwCiTon0fIOeOKgKoKQA-6sLgCaAlxu8nXFqOYa5Rm995bfLCIY03TFJeYzVW8WYj0QemeZc9w5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚽
باز هم حرکت عجیب و منشوری شجاع خلیل‌زاده، بعد از خوشحالیِ گل!!!
❌
پ.ن و بازم کشاله ران بوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/138536" target="_blank">📅 23:19 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138535">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
|
#فوری
🤫
⚽
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس اخبار جذب مبین دهقان صحت ندارد و این بازیکن مدنظر باشگاه و کادرفنی نیست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/138535" target="_blank">📅 23:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138533">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
🆕
🏅
به گزارش رسانه «سرخ تایمز» و طبق گفته های عضو هیئت مدیره باشگاه پرسپولیس، باشگاه مصر هست تا محمد قربانی رو به خدمت بگیره و خود محمد قربانی هم علاقه منده تا به پرسپولیس بیاد اما مشکل اینجاست باشگاه الوحده داره بازی در میاره و تا الان…</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/SorkhTimes/138533" target="_blank">📅 23:06 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138532">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0VgKM0HTQo1jNhyQ6UgNNYRdzyLjbICusGvpaNfEyfxUYhXE1Fo23cr_GOi3oQjgktcxCtWMtuGOPRnQJCD4OknNasDgIPUFOyUzJ9u5d9BkM5Cwr6XAPhnxQqiVjkLgorofs7TWo-yRgEtZhAqYFiPIaFHq3oEIJBB9XthpVhYahgms7skwT1cYppeX2CaM0xav62EP6NPkOxY2Zpozxnmw-mohdaUpHrWrfByAz4E8wnFTxek-LHx7SwXOCONDZh-geGhoUenouWDHOhnRu4S_DEwpCPNn-z1E8n6EZu6TI0iP38hM0zoWSRf8tgHj5BHoBQpaajGIoSDZmrwZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استقلالِ سهراب اگه بخواد انتقام کاملی بگیره؛ باید 8 تا به الوصل و 7 تا به العین بزنه:))
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/138532" target="_blank">📅 22:55 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138531">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5b8d2e556.mp4?token=guGz5XZmwq4Zl8tjTHXc-7v-oEc78BE_ouwIb1q7DPdGa1lczwKSySVFjLE4fWZHK06nR-w9TsC_gL9--jSJv_MpkJ1wsPSco85Oc2PSgnCh8BeTHa0pZ9aUOGAuXvTH7jGqJrqYVIYGKz0QK7YvI8QMXiysFhSJi9EDih3dBC82Br1cV8Dka1KKO7N57NhKSTXv5w6meYv70Kx9PvPA2qKT29iWebrz6zQNYYEq2E7G2hbNYJNOANt3n01VfucHMNGKyt9dWVKe18QV6yWmhJB8xGQc2mPWrJKctKR0-_IpAedEUPo6bCO67jRXzWgAH6w_34aLY9faBFMZX6TOTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5b8d2e556.mp4?token=guGz5XZmwq4Zl8tjTHXc-7v-oEc78BE_ouwIb1q7DPdGa1lczwKSySVFjLE4fWZHK06nR-w9TsC_gL9--jSJv_MpkJ1wsPSco85Oc2PSgnCh8BeTHa0pZ9aUOGAuXvTH7jGqJrqYVIYGKz0QK7YvI8QMXiysFhSJi9EDih3dBC82Br1cV8Dka1KKO7N57NhKSTXv5w6meYv70Kx9PvPA2qKT29iWebrz6zQNYYEq2E7G2hbNYJNOANt3n01VfucHMNGKyt9dWVKe18QV6yWmhJB8xGQc2mPWrJKctKR0-_IpAedEUPo6bCO67jRXzWgAH6w_34aLY9faBFMZX6TOTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شادی خاص نکونام با بیرانوند پس از گل دوم تراکتور مقابل سپاهان
😂
❌
پ.ن هفته سوم قیافتون دیدن داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/138531" target="_blank">📅 22:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138530">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMyj6jche2fxYc7Tvk4YNrPIZYaG6rpf68lrS4h5mq6s2h_uF06SXPRf7xyMdAFjnYdpMQjq5S2HkaTAS15MYnEv2vLL7rCWuUlYtc5lGfad8HXMjqgz-Czut3Hgr4LZpUZUesieZOh_0cew_G6lZHln1hO9fViGKJvRqYqAXQZCzO9HxsAbUnp1ENf8UJduFQeswadOCMMiHPB4Bv6BgO_Jys5V2EHPGet1M9u-TmLGisxbUKtmbgS_ubMMnv4OKqM_Q0WFOumtyh8c5eD4UuWXra4sT8yYobEyNgEOOplnW6s8U_vs4EUj_-yERJ7COs7k6HWDnlyGNbc0FFaF8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تصاویری از تمرین امروز تیم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/138530" target="_blank">📅 22:37 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138529">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MF36Aueljs-f8zjVod3U0vfRHPrCPEu20BJ_T0y20IXP71Hv0dqmLww_IJmCY3uUtcZ4gCtmmRn4lfdjqo2l_ibIBg46AZfVyltN-E8Wp9qfK_gTaXLjTA_gK1oSR1186uLeQan6CTEHGt0_Ya1K3Ws3rZrRuF__b77o6dUJ9HZi5rUAUoBvkOm1YdnnbfyLjEbQpqeFG7ZOxxDkpdoPqbPHWE0m3gPRN46aewWihMgEzVag8xhhhUlnsJSrXhvnwDgSHDxxPVYj16jg7YqzFJlI3jABecCXr4h3jOZTJR-ZFRmegWp9u-47UtaRlKpsodZRno6T5raeBuLl7vScUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
جدول لیگ برتر بعد از پایان روز اول از هفته دوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/138529" target="_blank">📅 22:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138528">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✔️
✔️
✔️
هفته سوم هفته مرگ و زندگی
✅
استقلال و سپاهان یکشنبه ساعت 19/30
✔️
پرسپولیس و تراکتور دوشنبه ساعت 18/30
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/138528" target="_blank">📅 22:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138527">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
کیسه و ترتر شش امتیازی شدن و کلین شیت و حفظ کردن امیدوارم فردا بازی و ببریم و پیام هم کلین شیت شو حفظ کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/138527" target="_blank">📅 22:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138526">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
❌
دومی هم زد ...و جواد چکش دومین بردشم آورد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/138526" target="_blank">📅 22:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138525">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b05abe66c.mp4?token=TtTkjUklU9nWp6oG8XEQELBkls50kBFPdPoM-FMNm-q3XyyLkFUNZe_p0T-3RgOydd3KeO4_e0ekinN82HxyXHlr2vjwNNoL3XxI5huK2AEIWbX3i8-4geLOm3dNAmBRDDIUnMrkcWs1D6UAJOUHFOk-E0OqYaOHK2HA-QcbI0_9G4pedkqddCGjKlk2GKgKBnBNa8zLx2-WhyTuCKtZQD9T1biVegud95WZlkW1HsUoctA9OYJYovbu_WNble9-vhOvVeji8iO8hoA_ynTS_qV7v53d9RCJeL-K07ejuA-XuUiXlCBLQZHeAGT1jczR8AcmKD0ezGuhjMLB1KJV2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b05abe66c.mp4?token=TtTkjUklU9nWp6oG8XEQELBkls50kBFPdPoM-FMNm-q3XyyLkFUNZe_p0T-3RgOydd3KeO4_e0ekinN82HxyXHlr2vjwNNoL3XxI5huK2AEIWbX3i8-4geLOm3dNAmBRDDIUnMrkcWs1D6UAJOUHFOk-E0OqYaOHK2HA-QcbI0_9G4pedkqddCGjKlk2GKgKBnBNa8zLx2-WhyTuCKtZQD9T1biVegud95WZlkW1HsUoctA9OYJYovbu_WNble9-vhOvVeji8iO8hoA_ynTS_qV7v53d9RCJeL-K07ejuA-XuUiXlCBLQZHeAGT1jczR8AcmKD0ezGuhjMLB1KJV2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔄
🔄
فوووووووووری :
❌
حق میزبانی استقلال با گوه کاری تاجرنیا گرفته شد و ای اف سی هر خراب شده که ای به عنوان میزبان انتخاب کنه استقلال حق اعتراض نداره
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/138525" target="_blank">📅 22:00 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138524">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❤️
گل اول تراکتور به سپاهان توسط امیرحسین حسین زاده 83
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/138524" target="_blank">📅 21:58 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138523">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✔️
✔️
برنامه هفته دوم لیگ برتر  سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/138523" target="_blank">📅 21:57 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138522">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❤️
گل اول تراکتور به سپاهان توسط امیرحسین حسین زاده 83
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/138522" target="_blank">📅 21:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138519">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d2cc7d25d.mp4?token=fB3hwg-3mvn3UPMLlOftZXGOxV33GhuRihjw1NmsgSR_gFtYNGDq8u9ryAsS8AKJ4Xt3kaT-hMCdSLAkgrs13eBojMnCqJJPrxxfyUrMjxB-_XWGaayOS0UtxeNxOnxEz8f4-O6jhKqU7xKOCtH9TfkEvl1_F0RzSBPdK_wEFhkXeDdlAJ9LgJ8cQvji0kFOS1gFLZRL3YxaSF52lnFM_clhw70_tWqYViUyvFrnTemqzdaOupsmOZzs3TuBeJnggLShpC_B6KBS8mWGWRjnMgpK-_rN_a8KnXUIKBEHAbkhRv-NzTTNBwfglGE_ImR11zstZAIY3F-b23wihGny-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d2cc7d25d.mp4?token=fB3hwg-3mvn3UPMLlOftZXGOxV33GhuRihjw1NmsgSR_gFtYNGDq8u9ryAsS8AKJ4Xt3kaT-hMCdSLAkgrs13eBojMnCqJJPrxxfyUrMjxB-_XWGaayOS0UtxeNxOnxEz8f4-O6jhKqU7xKOCtH9TfkEvl1_F0RzSBPdK_wEFhkXeDdlAJ9LgJ8cQvji0kFOS1gFLZRL3YxaSF52lnFM_clhw70_tWqYViUyvFrnTemqzdaOupsmOZzs3TuBeJnggLShpC_B6KBS8mWGWRjnMgpK-_rN_a8KnXUIKBEHAbkhRv-NzTTNBwfglGE_ImR11zstZAIY3F-b23wihGny-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
گل اول تراکتور به سپاهان توسط امیرحسین حسین زاده 83
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/138519" target="_blank">📅 21:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138517">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✔️
✔️
✔️
شهاب زندی مدیرعامل نساجی: به مدیران ارشد استقلال هم تاکید‌ کردم مستنداتی دارم که آسانی‌ بازیکن غیرمجاز است و اگر مقابل ما امروز حتی یک دقیقه هم به میدان برود از آنها شکایت خواهیم کرد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/138517" target="_blank">📅 21:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138515">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✔️
#ارسالی | #تکمیلی
🆕
⚽
هوادار مقیم امارات به نقل از محمد قربانی: میگه به باشگاه گفتم اگه قراره رضایتنامم رو صادر کنین برای باشگاه پرسپولیس صادر کنین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/138515" target="_blank">📅 21:37 · 27 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
