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
<img src="https://cdn4.telesco.pe/file/WxuZ89O-BXjMGhPSv_jIizBAMEBMDCekDM6dAfj_P1priK4yAnSlpXfo9kiAAudCTXabTFDHvbVxJ7FAUkWkUCfXyTYGUTh7MjguOHXi1oV7Tvcvn0MKQEd79QdG552M7zcrFnVpatSJJ5HonNRmDGG0pTH3gdSAoZ4uNS-qmITl7bioNIMIJ2UVTyIPWAM-SJCIKjzgigH1AO6lMUkC21vVoug8a97ubkeBr71e5OGrZP2nZjX0anjmVXabZwbMAo--40rPtT_Fu4Qv3VCtRL55cHJ0nazlq043FWwBpupDd7pwLrEkwO4zMpPl_43ysyeStvRmVAEs-sojncV56g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-14 10:30:28</div>
<hr>

<div class="tg-post" id="msg-139572">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇷
احتمالا در بازی با ذوب آهن بیفوما زوج علیپور خواهد بود و وینگر چپ پرسپولیس تغییر خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 887 · <a href="https://t.me/SorkhTimes/139572" target="_blank">📅 10:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139571">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🚨
فوووووووری
‼️
🔵
🔹
رسمی، با اعلام فدراسیون فوتبال موعود بنیادی فر داور دربی پایتخت شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 974 · <a href="https://t.me/SorkhTimes/139571" target="_blank">📅 10:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139570">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
✅
خبرگزاری تسنیم در واکنش به صحبتهای قلعه نوعی که گفته از خودگذشتگی کردم اومدم تیم ملی تیتر زده که آقای قلعه نوعی میتونه دیگه ایثار نکنه و از تیم ملی بره و برگرده لیگ برتر همونجایی که تو ۱۰ سال گذشته هیچ افتخاری کسب نکرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/SorkhTimes/139570" target="_blank">📅 10:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139569">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⚽️
تمجید ویژه پیوس از وینگر جوان پرسپولیس!
◀️
امیرحسین محمودی در دیدار مقابل مس رفسنجان آنقدر درخشان ظاهر شد که فرشاد پیوس، سرمربی مس، از کیفیت بالای او تمجید کرد و حتی از بازی نکردن این بازیکن جوان در پرسپولیس تعجب کرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/SorkhTimes/139569" target="_blank">📅 09:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139568">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guzjj4ZNeUWyPFQlFLyhpVR_V9Fl22_TwasDFpKLttx-zA4VGc0KkfWy7Pu6LszgNsEDthf-zUMloieMgNiobq4xo_zlwstO_5ZiviYMxAqZYYzMDt8TIUK422maYq9n19l0fwX6muIzTe6BDX_F9eLoMtosVWoKkZdBjFcuOHkysvtP9nYammP19kq5ZMPCxal_EZeDA9OOMh6U9RY2qhiZfv7CdfIiIjEYwteayO-APIlqQZAo2Uo7i4IguxkUD33CrGxN2WGfvETAHSCMQ_W7umSoZ7pcDgFDhXdbkJZKZE9HlfmkVn61d7cnBI7IUfwfyvpQvjjcTjEoEBwKKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/SorkhTimes/139568" target="_blank">📅 08:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139567">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORHlvyVi7_uIpL3Gziuj_xbjgXbNwsP7LX50fln9Iz5c3jKfGXHOg8hqdt_dE3y_TM7yBmQjARtkrlExUOB6DILeIi0SngNJexeE_CR-AHeigQ80RsAd0Vf7fNwELpXGVtXg2Opsyz2gM_wAVDXe5ztGq5vluvjB05s5wOYGcsYMG2rIKExO6xKxrpcIn-9BSZ2yLi0_OXk-bK_lqgHK8a62lxX-I9L5WQtXSPkDYNOkD9twjgxCqsMf7Ju15J-ZrU4ET6Pr-hjabT53-Rdb1_JnwoX-cenxaFeqadrH71iLvsRMIES6rVbH7oJOrr5j6V9W1DAcZ_m5HUXX-VeTHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
نبردی تماشایی در یواس اوپن
واچروت و تیافو؛ جدال قدرت و سرعت
شلتون و شاپووالوف؛ دوئلی برای صعود
🎾
ولنتین واچروت
🆚
فرانسیس تیافو
🎾
بن شلتون
🆚
دنیس شاپووالوف
🟡
کدوم ستاره‌ها از این نبردهای هیجان‌انگیز موفق بیرون میان؟
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی دیدارهای یواس اوپن همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
مینی‌اپ رسمی اسپورت نود:
👇
🔵
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SorkhTimes/139567" target="_blank">📅 02:14 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139566">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✔️
✔️
✔️
شنیده میشه عباس کهریزی ستاره جدید فوتبال ایران پیشنهاد اولیه استقلال رو رد کرده و گفته تمایل داره پرسپولیسی بشه /ورزش3
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/139566" target="_blank">📅 00:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139565">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
❌
✅
پایان دیدار تدارکاتی:
🔴
پرسپولیس 1
🔴
آلومینیوم اراک 1
✔️
گلزنان: علی علیپور برای پرسپولیس و عباس کهریزی برای آلومینیوم اراک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/139565" target="_blank">📅 00:29 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139564">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✔️
✔️
تارتار در بازی با ذوب باید به بازیکنانی که بازی نکردن یا دقایق خیلی کمی بازی کردن بیشتر میدون بده تا بازیکنان اصلی هم کمی استراحت داشته باشن
💬
خدایی نکرده دچار مصدومیت هم نشن
💬
🗣
🗣
مثل ایری، محمودی، سلمانی باکیچ
💬
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/139564" target="_blank">📅 00:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139563">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d308caf8de.mp4?token=RAOEEwgAFwU0Q_NBTJuXsqhUapWxi7QbcOdYoPgA11PmBJnfRtbB2YutgtlI5Ng46MP-Uh-y48D-F0TQAr4n6c-bGCuRhm2tDJbNmAsybLJok_dKnvXFVuJ2KnFWMueHQQyOYqkoThJALa3fTlLRMGRwSXC2SsLETyLQNWcr3x4yS1pzjKopbr0YG4-BIX41D0fGA0lTw9qgdx_-TrhrTT4cOrjh9DXWKGNkjC4i7tiybGb63fbDJSKSL78l30nhoUq4PxhOJ9zfGDQKmquEZS7UYTcBxg-site5ZxnMTjpUxMktNWkvUMWy_O2wTznJriEWMcB-ILBvbKkKG7pkyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d308caf8de.mp4?token=RAOEEwgAFwU0Q_NBTJuXsqhUapWxi7QbcOdYoPgA11PmBJnfRtbB2YutgtlI5Ng46MP-Uh-y48D-F0TQAr4n6c-bGCuRhm2tDJbNmAsybLJok_dKnvXFVuJ2KnFWMueHQQyOYqkoThJALa3fTlLRMGRwSXC2SsLETyLQNWcr3x4yS1pzjKopbr0YG4-BIX41D0fGA0lTw9qgdx_-TrhrTT4cOrjh9DXWKGNkjC4i7tiybGb63fbDJSKSL78l30nhoUq4PxhOJ9zfGDQKmquEZS7UYTcBxg-site5ZxnMTjpUxMktNWkvUMWy_O2wTznJriEWMcB-ILBvbKkKG7pkyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
محمد تقوی، در برنامه هت‌تریک در آنالیز دربی ۱۰۷ استقلال و پرسپولیس گفت:
✔️
✔️
«از معدود دربی‌هایی بود که همه راضی بودند؛ تماشاگر راضی، مربی‌ راضی، بازیکن راضی. یکی از دلایل موقعیت‌های زیاد گل، دفاع نامنظم دو تیم بود، هر دو تیم به سرعت به فاز حمله می‌رفتند.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/139563" target="_blank">📅 00:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139562">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a36a4cce3e.mp4?token=OURgLc6SnfepXZerYhrfV-4KWw_lW6-0U0ljY7FAIJe-0Dl77uvmeNSJQrvpdYZI30jRj6sy0vBVji57hdLd1SXsdTJTXWQThDCWcZhqE1JrEUcTQCFk2bAZBj0JqUc_DnFlNnu8Nzx1wJ_GK0OVKd7Bu34zB7KrKgs-VZ2ZN7fZW0IFvXJvWWXWw0VS9MsPYI0GDy3nmC9ogqbt0ozERqkAFjZ3-4XYxHbHVF1_yjCmIMx700kfaYCmgXtBCZx2vetnFYU0CBTv9FVd-AjVMbg9Ny5vIr6vwsyyQ8nubWvxXhZbxrk7FPGPu0IVI2LOBhL9A6jWbeTMEI_IRJrQvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a36a4cce3e.mp4?token=OURgLc6SnfepXZerYhrfV-4KWw_lW6-0U0ljY7FAIJe-0Dl77uvmeNSJQrvpdYZI30jRj6sy0vBVji57hdLd1SXsdTJTXWQThDCWcZhqE1JrEUcTQCFk2bAZBj0JqUc_DnFlNnu8Nzx1wJ_GK0OVKd7Bu34zB7KrKgs-VZ2ZN7fZW0IFvXJvWWXWw0VS9MsPYI0GDy3nmC9ogqbt0ozERqkAFjZ3-4XYxHbHVF1_yjCmIMx700kfaYCmgXtBCZx2vetnFYU0CBTv9FVd-AjVMbg9Ny5vIr6vwsyyQ8nubWvxXhZbxrk7FPGPu0IVI2LOBhL9A6jWbeTMEI_IRJrQvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
درخشان: بازیکنان پرسپولیس هنوز به هماهنگی کامل نرسیده اند. قطعا پرسپولیس در ادامه لیگ بهتر می شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/139562" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139561">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdba32ee42.mp4?token=ByEXXJHYqp9jBCm1QCOYchYzJ6EfLaGR2_65mNjWHl4WaJMF1_g72wEwMyCSfq-3qhN7rBM74S4G9810K_GAPdVmnHkVwmezw2d3Ju01POoXyJP1GDW-ss4hsNUJhDhlYEJACzLQzkt8zM9fg39CmomOZAs6KBuHH2QIDdcu4Lk-Id0zHj6JjqdIit31XSWUM3QuhRt9cS9jij-TRlYm4u84lpRkFE2VN34i7ZOkm8305TdfsPkBlhBTwfUXJoUA3trl15gH-DJ03TMY9hJGPAambRRwKJIdnw0r2d0ITfTuoJ79tD8kjgBYJqteNuZdReQynWKAGEeKRUDX2JPKCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdba32ee42.mp4?token=ByEXXJHYqp9jBCm1QCOYchYzJ6EfLaGR2_65mNjWHl4WaJMF1_g72wEwMyCSfq-3qhN7rBM74S4G9810K_GAPdVmnHkVwmezw2d3Ju01POoXyJP1GDW-ss4hsNUJhDhlYEJACzLQzkt8zM9fg39CmomOZAs6KBuHH2QIDdcu4Lk-Id0zHj6JjqdIit31XSWUM3QuhRt9cS9jij-TRlYm4u84lpRkFE2VN34i7ZOkm8305TdfsPkBlhBTwfUXJoUA3trl15gH-DJ03TMY9hJGPAambRRwKJIdnw0r2d0ITfTuoJ79tD8kjgBYJqteNuZdReQynWKAGEeKRUDX2JPKCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
واکنش حسین عبدی به عدم دعوت از امیرحسین محمودی
🗣
حسین عبدی: امیرحسین محمودی بازیکن فوق العاده ای است ولی وقتی من او را حتی ندیده ام چگونه دعوتش کنم؟
🗣
‌‌پ.ن: ما که از خدامون هست دعوت نکنی ولی این حرف عبدی توجیه قابل قبولی نیست
⚪️
بازیکن کیفیتش مشخص هست
🔄
همین دقایق اندکی هم که بازی کرده برای تارتار نشون داده قابلیت هاش رو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/139561" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139560">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🎤
⚽️
وحید فاضلی مربی پرسپولیس: میتواستیم بعد از گل عقب بکشیم و به راحتی برنده مسابقه شویم اما فلسفه تیم ما این بود که برای گل دوم و سوم تلاش کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/139560" target="_blank">📅 22:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139559">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f9d5f0dd.mp4?token=FmGvTytu-HMQx8AIyLwxu6P_kXSjjYlwfeaQlz0ufbutO5ygGdloU1cRWf-xaABoajGQdNvk0pq7ttiQeUxZI9baHJq8IUUMcLv5jAh51abpn-uZlEQT_Ne8O_Ib7P07wyrsKDJLL9cB2sWa4g27RtpwQeWCPhMTVO7ayQuQPy1gbeFKru4WWatAvWOcXJncyypdo6HwsUQZ9Zk6s3-y86j3HWwITYoXpFzxGUZ7VU5tSMaaV4lIMV5_2DPjJND6HDTNRs7hxyff6JjEjrJs_Uc12-nmvipP4Bl1YHsVJDYLnNloe68Mq_8snUOmok0mF5y2W2_ZPmUYT4mDLMiKCn-9a70meO-Z6hyizMDBKh3i1FwCY4-3R1RuHQxfM5MLJbesFLhTQmz3JX64RbaxejHCVbIlS2ycHk5uvprLux-a1fIpU3FEalY705Ky4AsTu_hBzL9Y82h6_1yEff1MlqxGELzJ4FaQaxQlP7KLIwqo48bxLE09Rir_mbkdLBr0rUbwAnnRHH9E1s_P-W9ajSsy33kT145NJ2vr9U6rmHb8IQcHu4iMVb0SS0HQrtahD5dpxe8DZrMh0Mb6v0iEeY1gePU9jDeGjvLyH13on9lk95DshCxTGfsknxEJZKD9G7RX3RbGkawEqZGPOsUmbLLXaVpr_TNrZBq9PFeRhTk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f9d5f0dd.mp4?token=FmGvTytu-HMQx8AIyLwxu6P_kXSjjYlwfeaQlz0ufbutO5ygGdloU1cRWf-xaABoajGQdNvk0pq7ttiQeUxZI9baHJq8IUUMcLv5jAh51abpn-uZlEQT_Ne8O_Ib7P07wyrsKDJLL9cB2sWa4g27RtpwQeWCPhMTVO7ayQuQPy1gbeFKru4WWatAvWOcXJncyypdo6HwsUQZ9Zk6s3-y86j3HWwITYoXpFzxGUZ7VU5tSMaaV4lIMV5_2DPjJND6HDTNRs7hxyff6JjEjrJs_Uc12-nmvipP4Bl1YHsVJDYLnNloe68Mq_8snUOmok0mF5y2W2_ZPmUYT4mDLMiKCn-9a70meO-Z6hyizMDBKh3i1FwCY4-3R1RuHQxfM5MLJbesFLhTQmz3JX64RbaxejHCVbIlS2ycHk5uvprLux-a1fIpU3FEalY705Ky4AsTu_hBzL9Y82h6_1yEff1MlqxGELzJ4FaQaxQlP7KLIwqo48bxLE09Rir_mbkdLBr0rUbwAnnRHH9E1s_P-W9ajSsy33kT145NJ2vr9U6rmHb8IQcHu4iMVb0SS0HQrtahD5dpxe8DZrMh0Mb6v0iEeY1gePU9jDeGjvLyH13on9lk95DshCxTGfsknxEJZKD9G7RX3RbGkawEqZGPOsUmbLLXaVpr_TNrZBq9PFeRhTk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎤
⚽️
وحید فاضلی مربی پرسپولیس: میتواستیم بعد از گل عقب بکشیم و به راحتی برنده مسابقه شویم اما فلسفه تیم ما این بود که برای گل دوم و سوم تلاش کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/139559" target="_blank">📅 22:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139558">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
❌
برخلاف شایعات هفته هفتم لیگ برتر کنسل نشده و قبل از فیفادی برگزار می‌شود.
✍️
فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/139558" target="_blank">📅 22:54 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139557">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✔️
✔️
وحید فاضلی:
✔️
کم بازی کردن اورونوف بخاطر ترس از مصدومیتش هست و داریم دنبال راهی میگردیم که نهایت بهره رو از این ستاره بگیریم!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/139557" target="_blank">📅 22:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139556">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✔️
✔️
وحید فاضلی:
✔️
کم بازی کردن اورونوف بخاطر ترس از مصدومیتش هست و داریم دنبال راهی میگردیم که نهایت بهره رو از این ستاره بگیریم!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/139556" target="_blank">📅 22:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139555">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✔️
✔️
جباری: سبک بازی ارونوف و نوع بازی تیم با توجه به تغییرات در حال هماهنگی است و به مرور زمان بیشتری برای بازی پیدا می‌کند   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/139555" target="_blank">📅 22:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139554">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✅
معاون وزارت ارتباطات : با اشاره به تجربه قطع اینترنت در جریان جنگ اخیر کشور به سطحی از بلوغ رسیده که حتی در شرایط بحرانی و التهاب شدید نیز میتواند بدون قطع اینترنت مدیریت شود و دیگر شاهد قطع اینترنت نخواهیم بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/139554" target="_blank">📅 22:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139553">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf52d5a19e.mp4?token=PAGPIZ0j_Ur40aKZk-9f3IGeqlCXtm5gWKwKEiJuUPB3z9Mdj7EXVQ7tUr3DvudTqel4VffSkvK5JHcqwWv_vX9sZ_-wJXHkRm6aYwFSsvZFFyFTowA6z9ADaZB1r6mB9jDF_KIZzJZBjbXHVKI3R38lajIv6ENNShVKKIgdCMPxESJixB-oHnIhp3rm9bu0BQ3vjkdZtp_bbU2UyBfbqIkmQcKVa-pJmfKLsdm-9ibGd_hj8mTvNp39izTxxcQH9Z77RXVlhSGB5z-IYL4TSR4G1BMahmpzpBPwRnGd-RlG1dd2H6zQ3qIEuMo9gqqxj89zv9lMlSCSWqarw9FRcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf52d5a19e.mp4?token=PAGPIZ0j_Ur40aKZk-9f3IGeqlCXtm5gWKwKEiJuUPB3z9Mdj7EXVQ7tUr3DvudTqel4VffSkvK5JHcqwWv_vX9sZ_-wJXHkRm6aYwFSsvZFFyFTowA6z9ADaZB1r6mB9jDF_KIZzJZBjbXHVKI3R38lajIv6ENNShVKKIgdCMPxESJixB-oHnIhp3rm9bu0BQ3vjkdZtp_bbU2UyBfbqIkmQcKVa-pJmfKLsdm-9ibGd_hj8mTvNp39izTxxcQH9Z77RXVlhSGB5z-IYL4TSR4G1BMahmpzpBPwRnGd-RlG1dd2H6zQ3qIEuMo9gqqxj89zv9lMlSCSWqarw9FRcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
#منهای_پرسپولیس
👾
عبدالکریم حسن دفاع چپ سابق پرسپولیس، به این شکل با پیراهن الشمال در لیگ قطر گلزنی کرد
🚀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/139553" target="_blank">📅 22:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139552">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEvzTfHht1OOF-CN5c4PnJu2J0tqc52w9ZnaS0LTDN1AqAkA8b_Ndj-p11hwXcAfcsSgjcl0WGHd-CUpJOQmhhJmTAx4oL56i0X5UuKDzYfRdaXVvqZpnvnEnEM_EU_qyuWMOdRgv-uVLzmQfD2sB52moY_yN-G4DMp5SbmDpKfsd6oaDiRnq3D03Nv5XZz7w7WgsherimiunAQAX93Eb-tk4lDZzTSW0o5fZEBd03xQZy0Gor7WVWVegB22ax2kaiLiGoOtAk_2DjVuIEuYAL-qV2G7gnQO10L0yZU5ayyFwutbLkUK2MRiduAYBNq6fDcVRRl5M7syqZy0fKMapw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
لیورپول آماده‌ی شروعی قدرتمند
ایپسویچ سد راه قرمزهای مرسی‌ساید
نبردی برای فتح سه امتیاز
🔥
[
ایپسویچ
🔵
🆚
🔴
لیورپول
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
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/139552" target="_blank">📅 21:53 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139551">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✅
✅
سه بازی مهم هفته بعدی
✔️
شنبه :گل گهر و تراکتور
✔️
یکشنبه : آلمینیوم اراک و کیسه در اراک
✔️
دوشنبه : پرسپولیس و ذوب آهن شهر قدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/139551" target="_blank">📅 21:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139550">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqgXj2YVZqsd3YZaQknB3LmZn1BswI6zNLwzYiu__EdkGgpiOHcp5lnQbsNrijPdSAcQWQro3H3SMNXD4BXAVkP6AWwF1SJxjLLawb27VcRcvj87zAWADOGnMvr_1wSTiVOGJV2R1Bfa_rGt3Ca6FMyX4LoXuO1bVCAC3mZAlJQr5kNiWPgZLg3AgJQEJCJOlo1WDkIOkTVeMlXNb-3aJ-VgE8Jieyhq5k1nChwrijc979eruR0i8lMStdgRgghaXXJ3B4U-L1ejFUCGxaISiN3d7SlnTLhoi2ly8Sd_mprM9TVrUm-PCJ_CyjB1JjfOfqBa4EhL7Z9aUv-Xop0boQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تمجید ویژه پیوس از وینگر جوان پرسپولیس!
◀️
امیرحسین محمودی در دیدار مقابل مس رفسنجان آنقدر درخشان ظاهر شد که فرشاد پیوس، سرمربی مس، از کیفیت بالای او تمجید کرد و حتی از بازی نکردن این بازیکن جوان در پرسپولیس تعجب کرد
!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/139550" target="_blank">📅 21:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139549">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxwIcbSYi9eSoksFalkXQMMB4DL21s6hmiJRb7AjUUTQHY-1FHKzUPV-LDijC8MgGfscjoLcapmSL2--7OlgxP61CcxRQhNNvoUqNuUF5KzM0zMVgjkJnNrHIz3dNVZ_oe_HHG9eCGxlb5kJNTGD2qkJ80tMQcWa4VjtQtzOdbs5ci2o-mKiOdwKVrQMnUI_PKdbyd_uc7oEuO4CMgPoH84FtIi0aHF5L1IAa6WkS-FAxc6uT5GT381NMVYDcTNEWOYZbEvJXe4w9La3YhAPHrQ9Pr4mFQUr23NLDH6CdfopTrqito9lgrTgxzvBUvPeD45jfbFeogEOtdbu25RaMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◀️
🔴
از دیروز که باشگاه گفت پرونده ، آسانی رو به CAS می‌بریم به هـــول‌‌ُووَلا افتادن‌... دیروز تاجرنیا و امروز این هوشنگ اصرار میکنن که نکنید بی فایده‌ست‌!
⭕
اصلاً ما دلمون میخواد شکایتِ بی‌فایده کنیم چرا آنقدر میترسید فشار میارید مانعِ ما بشید‌؟
✅
اگر فایده نداره پس سکوت کنید بزارید خود (CAS) معلوم کنه شکایت به‌حق هستش یا نه‌...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/139549" target="_blank">📅 20:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139548">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✅
✅
سه بازی مهم هفته بعدی
✔️
شنبه :گل گهر و تراکتور
✔️
یکشنبه : آلمینیوم اراک و کیسه در اراک
✔️
دوشنبه : پرسپولیس و ذوب آهن شهر قدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/139548" target="_blank">📅 20:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139547">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👀
❓
محمودی ۱۵ دقیقه هم بازی نکرده امسال… اقا تو پستش ترافیکه درست ولی نمیتونی هر بازی بهش ۲۰ دقیقه بازی بدی بازیکن روحیش از دست نره ؟! محمودی چند ساله دیگه عصای دست پرسپولیس میشه اگر آقایون نسوزونن بازیکن رو…فقط بازیکن هایی که از گل گهر آورده رو بازی میده اقا…</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/139547" target="_blank">📅 20:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139546">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
❌
با اعلام باشگاه پرسپولیس، آکو باتری اسپانسر جدید این تیم خواهد بود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/139546" target="_blank">📅 19:37 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139544">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LK12z-eOBVzBMzN5YxNm41Xd7uagnXcgWrqKTU5MaJhqZFAsb8ivoCI_YfkBrKlWH5dv3FGrdg3IzQ7pQbA-r49C6F6wWf5BRlTyN7Ky0Aibw3Tx7c8R0YsZLi7aXcetwFtPmSXabNyGIlsaRo7uUPNwn-wQ_bVDf6D_0fkgtqpSUpuGZ1t_4TSKm8FU_jlejVDB2VhuucmaM2Hk5EaVmgIkiQpr9DHVD8qQo1TL2JQ6F-2xFsqE7I480pjIDTpfCnOyHdsZHYp1jJyB0GFVxopJkBtisJ_wluWyZnvrVucgiBI6G6cGDpLy-k5kw0A2_cSX5WFR5RSftt4e505pgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
♨️
🆔
| ورزش‌سه:
🔴
❤️
با ادامه‌ی روند فعلی مارکو باکیچ از پرسپولیس جدا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/139544" target="_blank">📅 18:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139543">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❤️
❤️
باز هم بزرگی و عظمت پرسپولیس در این سال‌ها به بهترین شکل خودش را نشان داد
🔻
🔻
در سال‌های اخیر، بازیکنان زیادی با آرزوی رسیدن به پیراهن تیم ملی، راهی پرسپولیس شدند و پس از درخشش در این تیم به هدف خود رسیدند؛ گولسیانی و گندوز نمونه‌هایی از این اتفاق هستند…</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/139543" target="_blank">📅 18:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139542">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✔️
✔️
محسن خلیلی: ما پیگیر شکایت از یاسر آسانی هستیم و برای اینکه پرونده را به دادگاه CAS ببریم ابتدا باید در کمیته انضباطی شکایت کنیم و جواب بگیریم بعد به CAS ببریم
✔️
بعضی ها می گفتند ما اورونوف را بازی نمی دهیم که او را  بفروشیم/ واقعا خنده دار است چرا باید…</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139542" target="_blank">📅 18:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139541">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✔️
✔️
جنجال و حاشیه در اردوی کیسه؛ با اعلام سهراب بختیاری‌زاده، صالح‌حردانی بدلیل رفتار ناپسند و درگیری با سرمربی و یاسر‌آسانی در بازی دربی، تا اطلاع ثانوی از حضور در تمرینات کیسه منع شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139541" target="_blank">📅 18:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139540">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">⚪️
⚪️
⚪️
فوتبالی: سهراب بختیاری‌زاده به حردانی، مهار اورونوف و بیفوما رو سپرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/139540" target="_blank">📅 17:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139539">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✔️
✔️
نصیرزاده: شکایت از آسانی، دنبال نخود سیاه رفتن است!
✔️
تیم‌ها با شکایت از آسانی دنبال نخود سیاه هستند؛ فقط استقلال می‌تواند از این بازیکن شکایت کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/139539" target="_blank">📅 17:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139538">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4b00df71c.mp4?token=pG9EDanaOTO0onofSgjdZoRaqTLz36Ig7NUADH9KG0f52s91VZF6NWBrU6IZRxjdHjza9yBggXiBSd8b0BN_QIuPDS3HgTI148-9005b14Qf11oNwskONVc83sKt4bTpB7zU5uaM2NPlfi4UFUUeCAwByqvYftaAebWgeKf_DZEb5IZR3vpwCRr7gTY_QLLFGlV10TqH2ItJAJUQQLTm5G3i-F5zHgZRqWalcV4R5a9NIJH1yd-rbUjQ5G2amadKX65btyQCHmc3gce7tsmtysm9TIEhtaXoCh806GrWyVB2ajmdWgEfu0_B1awIPvR9-DfJ5v2ELTQu6IsxBiRNkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4b00df71c.mp4?token=pG9EDanaOTO0onofSgjdZoRaqTLz36Ig7NUADH9KG0f52s91VZF6NWBrU6IZRxjdHjza9yBggXiBSd8b0BN_QIuPDS3HgTI148-9005b14Qf11oNwskONVc83sKt4bTpB7zU5uaM2NPlfi4UFUUeCAwByqvYftaAebWgeKf_DZEb5IZR3vpwCRr7gTY_QLLFGlV10TqH2ItJAJUQQLTm5G3i-F5zHgZRqWalcV4R5a9NIJH1yd-rbUjQ5G2amadKX65btyQCHmc3gce7tsmtysm9TIEhtaXoCh806GrWyVB2ajmdWgEfu0_B1awIPvR9-DfJ5v2ELTQu6IsxBiRNkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
نصیرزاده: شکایت از آسانی، دنبال نخود سیاه رفتن است!
✔️
تیم‌ها با شکایت از آسانی دنبال نخود سیاه هستند؛ فقط استقلال می‌تواند از این بازیکن شکایت کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139538" target="_blank">📅 15:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139537">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✔️
✔️
رضا جباری:
✔️
این نسل پرسپولیس از لحاظ اخلاقی و فنی بهترین‌های حال حاضر فوتبال ایرانند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/139537" target="_blank">📅 14:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139536">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
کیسه و ترتر شش امتیازی شدن و کلین شیت و حفظ کردن امیدوارم فردا بازی و ببریم و پیام هم کلین شیت شو حفظ کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/139536" target="_blank">📅 13:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139535">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🎥
🔹
تمامی گل‌های هفته پنجم لیگ برتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/139535" target="_blank">📅 13:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139534">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87b97822e9.mp4?token=CLLeZ1swBMQspCNtGTHWXfMwCZgTgufTf1W9suIOd4SyBtCUBjh3ducdjiP9bDWJowdLcx1pQZqU9YqRwuDeD6KLz0JuUoR_0ItmGCxPRxLWeiB_aMFqs5jFXUSRux3xWkTy-3QPJgHmTuQdq7tkzK6Z9XyAy7hFTec_LTnkerui3seCZJm6g0MRn5_UoOhPvBwhDjc9VlzBp1DxLorF9ffzt3oCtDBtHIVsx1wLyLXeaz_2OKt4GQk2udHmG3ZTJXJiFyA1ksjT0bD96H8I5fdrWoeDVzAmxBo83-RzNXWaGk91qCIUXzvITZebrJnEpiZPVxNeVEJjCt89BAmQDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87b97822e9.mp4?token=CLLeZ1swBMQspCNtGTHWXfMwCZgTgufTf1W9suIOd4SyBtCUBjh3ducdjiP9bDWJowdLcx1pQZqU9YqRwuDeD6KLz0JuUoR_0ItmGCxPRxLWeiB_aMFqs5jFXUSRux3xWkTy-3QPJgHmTuQdq7tkzK6Z9XyAy7hFTec_LTnkerui3seCZJm6g0MRn5_UoOhPvBwhDjc9VlzBp1DxLorF9ffzt3oCtDBtHIVsx1wLyLXeaz_2OKt4GQk2udHmG3ZTJXJiFyA1ksjT0bD96H8I5fdrWoeDVzAmxBo83-RzNXWaGk91qCIUXzvITZebrJnEpiZPVxNeVEJjCt89BAmQDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▫️
گل محمدمهدی محبی از زاویه‌ای متفاوت
▫️
▫️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/139534" target="_blank">📅 13:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139533">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
❌
فنونی زاده : به حدادی گفتم حواست به خلیلی باشه میخواد مدیرعامل بشه و زیر پای تو رو خالی می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/139533" target="_blank">📅 12:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139532">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚫
عادل فردوسی پور: با دیدن فوتبال ایران میتونیم غم و رنج خودمون رو فراموش کنیم و به قیمت دلار فکر نکنیم و شاد باشیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/139532" target="_blank">📅 12:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139531">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00fbdf9821.mp4?token=Syr6CvwrwVjdKpUC8W8h-gUk5Kz3yvQE0_-RfxA_YjyOXTd0EeBE_e7-rU75hYGOjOe5TBl43nZByvglBWrZDOuVNrs1rYs-DAGUbzXNpCVmFqqOoYiNyy7_P-pP50TVewYWD2wUJNtKeGvFx1Nt3xnhLZeKqQPfX4-aPrhvHnce-cBiFGxGaSr8tBLjSJrWS0taMpYv3sqHhr5NhDn22ch19b8gpGek5Cjern8sigMgOZ9PaYFtDIQyYRlFWpYN0oEk6HexJ_190UbtAvsdDlPNqIebCZKXpbkx9QePkaw2cParqPfRb_VVMDvRXqxF5Uwc5lVn-kGwWmUYR2GRCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00fbdf9821.mp4?token=Syr6CvwrwVjdKpUC8W8h-gUk5Kz3yvQE0_-RfxA_YjyOXTd0EeBE_e7-rU75hYGOjOe5TBl43nZByvglBWrZDOuVNrs1rYs-DAGUbzXNpCVmFqqOoYiNyy7_P-pP50TVewYWD2wUJNtKeGvFx1Nt3xnhLZeKqQPfX4-aPrhvHnce-cBiFGxGaSr8tBLjSJrWS0taMpYv3sqHhr5NhDn22ch19b8gpGek5Cjern8sigMgOZ9PaYFtDIQyYRlFWpYN0oEk6HexJ_190UbtAvsdDlPNqIebCZKXpbkx9QePkaw2cParqPfRb_VVMDvRXqxF5Uwc5lVn-kGwWmUYR2GRCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
اتفاق عجیب؛ نیمه دوم بازی شمس آذر و تراکتور ۱۶ دقیقه وقت تلف شده داشت اما داور دو دقیقه اعلام کرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139531" target="_blank">📅 12:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139530">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
🔴
پرسپولیس موفق شد امتیاز تیم دسته اولی فولاد نوین رو بخره و تبدیل به پرسپولیس ب خواهد کرد و سید جلال حسینی هدایت این تیمدرا برعهده خواهد گرفت/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/139530" target="_blank">📅 12:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139529">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
✔️
شنیده میشه که همکاری یحیی گل محمدی با باشگاه دهوک عراق به زودی به پایان خواهد رسید و این مربی به زودی به لیگ ایران باز خواهد گشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/139529" target="_blank">📅 12:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139528">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✔️
✔️
فرصت به ستاره خاموش سرخپوشان نیز خواهد رسید؟!
✔️
✔️
مهدی تارتار قصد دارد بصورت چرخشی از بازیکنان جوان خود در ترکیب تیمش استفاده کند و در هفته‌های اخیر شاهد بازی کردن بازیکنانی همچو سلمانی و لطیفی‌فر در پست خط هافبک سرخپوشان بودیم.
✔️
✔️
حالا بنظر میرسد…</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/139528" target="_blank">📅 12:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139527">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
❌
پافوس قبرس با هدایت ریکاردو ساپینتو از پلی‌آف لیگ اروپا حذف شد و راهی پلی‌آف لیگ کنفرانس اروپا شد. تیم ویتبسک بلاروس هم که میلاد محمدی را در اختیار دارد، از لیگ کنفرانس حذف شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139527" target="_blank">📅 12:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139526">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✔️
✔️
محسن خلیلی: هوادارا فقط میگن چرا اورونوف بازی نمیکنه؟ خب وقتی بیفوما در آماده ترین ورژن ممکن هست چرا اوستون بازی کنه؟ بیفوما خیلی خوب بازی کرده و حق دارد فیکس باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/139526" target="_blank">📅 11:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139525">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✔️
✔️
✔️
محسن خلیلی مدیر پرسپولیس: بیفوما الان شرایط خیلی خوبی دارد و دارد خوب بازی می کند ولی دارند حواشی درست می کنند که چرا ارونوف بازی نمی کند. هواداران ما  باید صبور باشند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/139525" target="_blank">📅 10:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139524">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQlqf4As_ZVwlmGRXp0gTY7gIGk0BJqrABpY8oVeIwKAO5qTAVkYfa1y4F4ztyAL0Bpowg172ikngZ-hybdxqTAFNwOpzWXqNwP_IDvS2_kPjHFzylH8yuBkISF-GPWU_MLvVls1aB2cAqr2eLuTNjaz_lHx-olpa-F2IhB-qtMt6qh4P9IBSOGcS656_78L4I8av8GSGb1LEUOQLM0d42NVVkjaWsm10yil1MS1QESKgIU8zMnETsV731H4f0PYnmoOzcTqLdnC5R460utR3rljYvKGCfAZZvWbV1IdjgYeZ_tLWqaTQ55uarinvk4LVa9QOwsPkdnhOPOYIhhjDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌬
پایان دیدار
🇮🇷
ایران
3⃣
_
0⃣
نیوزیلند
🇳🇿
👀
✔️
ایران گام اول را محکم برداشت، شروع مقتدرانه شاگردان پیاتزا در مسابقات قهرمانی آسیا
🇮🇷
۲۵ | ۲۵ | ۲۵
🇳🇿
۱۵ |  ۱۲  | ۲۲
🏐
#قهرمانی_مردان_آسیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/139524" target="_blank">📅 10:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139523">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❤️
محمدمهدی محبی زننده ۲۰۰ مین گل تاریخ دربی بود
👌
❤️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/139523" target="_blank">📅 10:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139522">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❤️
صبح آدینه تون بخیر و شادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/139522" target="_blank">📅 10:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139521">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zx_rNFR8erZKu5OSYy7WP8dXWW_nDB1GNCd0EMJzDdHkeeqUWtNmjWoSZJRTVZ1jtyynUk3GES7j5u8hWrJwEj7z08jBrY-luT0Yb-8BfbvymSLOKH8ZJCQJHVgfLuwtox9tmR60j8Cgbl7CSaxiiUSJyZfkKlgep2VSquumIoDGbCtbj_Jz25fFfAkHiA57kLkWp1LT8JF-gvuMCzjvbgXb6ZX3t9JVrqNHzD_7zkJ__FMNhqYCDVBPHJYp5jEBtyYQzQ7ME2q7CsT9d4rvyZmB6BXfuLh4d1MxTcYttLXdZ9IIflji1qXLdNNh80kHAYhz7-rbmkFUY0ycPDouJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
دوئل ستاره‌ها و مدعیان در نیویورک
جوانی، تجربه و انگیزه در یک شب هیجان‌انگیز
زورف و تین به‌دنبال عبور از سد فرانسوی‌ها
🎾
گائل مونفیس
🆚
لرنر تین
🎾
الکساندر زورف
🆚
کوئنتین هالیس
🟡
کدوم ستاره‌ها از این نبردهای هیجان‌انگیز موفق بیرون میان؟
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی دیدارهای یواس اوپن همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
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
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/139521" target="_blank">📅 02:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139520">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccY3hDbc8sd49Q7Lw4GpcmouygDXRQW3aFCCf32TU8IT9ZpGeKF5vHy4mmMKMZVhD6owWae-Y_kHyujOdtyizwScqTMGlRIYFi_L-793xLmv56GtmcY8BAvUbfru_a0B41rGYjtdvQ6WKZhxvc5XaZCypmntlqSDubaWvaEQykkrQyNJcE0iVvz-ZpahtJ7OfJnpf5ExkOdXA8V3kKk-Jt7L3FoLrFcqFcsBuGJPjcAZj2OkhQxGLmV-bQVmlyNntxfg2F9ql6O8tHg5L0p28HglPHac5t_xfqlIc_g0VpL_LnNSGVdICvkOgQSj5SGlGWi7AcdrPUSwCm40ZcAKAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
🇮🇷
تصویری از ناخن‌ بلند کنعانی زادگان در صحنه درگیری با آقاسی که در برنامه فوتبال برتر نشان داده شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/139520" target="_blank">📅 01:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139519">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✔️
✔️
فوری ترامپ: آماده حمله دیگری به ایران هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/139519" target="_blank">📅 01:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139518">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7cfe803aa.mp4?token=D2-jpzmu8NvaZ6xDP4MyKDUC-2F_XtsgRJtyskCfzxQl7rcjJcLtIEE8yV-xTFzK_6cM5veIUg8w9PcQdZOorGlFZT3vHwAouOkD7adghg8EPpXOoJOL2qEFwBrfAVimkimhrMStzbbhl-Cov06fh0HVY49XCR7aAOHeZiAw4dhY1jtZfVBw7pYCtBLzOJXuvHJXBQ6SpTcgeKYbAHyluyyxyt_7P6z55yKl9Rd1ec88E7o4zwlUErlujliir9fCZacPr11GzSUJ4M-40GwfI1ZSyagDTxlaBo3le6cXFBhCV7CyVt-J2phCNYmx4SR0AxyhEvomHXeaA08xZp1WDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7cfe803aa.mp4?token=D2-jpzmu8NvaZ6xDP4MyKDUC-2F_XtsgRJtyskCfzxQl7rcjJcLtIEE8yV-xTFzK_6cM5veIUg8w9PcQdZOorGlFZT3vHwAouOkD7adghg8EPpXOoJOL2qEFwBrfAVimkimhrMStzbbhl-Cov06fh0HVY49XCR7aAOHeZiAw4dhY1jtZfVBw7pYCtBLzOJXuvHJXBQ6SpTcgeKYbAHyluyyxyt_7P6z55yKl9Rd1ec88E7o4zwlUErlujliir9fCZacPr11GzSUJ4M-40GwfI1ZSyagDTxlaBo3le6cXFBhCV7CyVt-J2phCNYmx4SR0AxyhEvomHXeaA08xZp1WDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇮🇷
تصویری از ناخن‌ بلند کنعانی زادگان در صحنه درگیری با آقاسی که در برنامه فوتبال برتر نشان داده شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139518" target="_blank">📅 01:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139517">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✔️
✔️
محسن خلیلی مدیر پرسپولیس: شما تعویض های تارتار در دربی را ببنید که تماما هجومی و در خط حمله انجام شد
❤️
محسن خلیلی: اینجا پرسپولیس است شما نمی توانید ناگهانی 80 درصد تیم را جوان کنید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/139517" target="_blank">📅 00:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139516">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✔️
✔️
محسن خلیلی مدیر پرسپولیس: شما تعویض های تارتار در دربی را ببنید که تماما هجومی و در خط حمله انجام شد
❤️
محسن خلیلی: اینجا پرسپولیس است شما نمی توانید ناگهانی 80 درصد تیم را جوان کنید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/139516" target="_blank">📅 00:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139515">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">⚽
🎙
رضا جباری:پوریا شهرآبادی جزو 3 مهاجم برتر لیگ است؛بازی در پرسپولیس پرمهره از بازی در تیم ملی سخت‌تر است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/139515" target="_blank">📅 00:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139514">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✔️
✔️
خلیلی: بهترین نقل و انتقالات چند سال اخیر را امسال داشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/139514" target="_blank">📅 00:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139513">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✔️
✔️
دعوت بیفوما به تیم ملی کنگو بعد از درخشش در پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/139513" target="_blank">📅 00:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139512">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✔️
✔️
✔️
باشگاه استقلال:
✔️
سرعت بیفوما خیلی عجیب غریب بود و مشکوک به دوپینگه! ازش شکایت میکنیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/139512" target="_blank">📅 00:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139511">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9jQ9FMNRRoQmyDqwzMUhF4LIHjSafCD2RqDnNl4WniNUtGILD2hSgxE8vB6kVOJQYz3TUCDBGHoz-aH4S4-7RsABaX6YQl6OvMQuBoqOqWCIL5Eag0Nen3UwqmPmaANaosfHU3dyA9uymAzwRhLZ9g6ESD8mvpomOyg8oP_3lnVd7uIMeI0W_TW9JLAe-ac_brIrnv5aLolP5Kj1k04aSFiDEXXaI7hQSDw0otJQ1_SnvP4u2dpggVuowtewVYn4ZhUmzFhXbA-I4NGxO72heLUWn4kgXbTb8rgARxicH18gFSt4RFq_BHOfVcq4yE3QoXCZbiJy-pF6uL3roMLfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🟠
جدول لیگ برتر در پایان هفته پنجم
👑
تراکتور با فاصله ۲ امتیازی همچنان صدرنشین است
👀
فاصله منطقه سقوط تا رده پنجم؛ تنها ۳ امتیاز!
❌
چادرملو و استقلال خوزستان؛ تنها تیم‌های بدون برد
🔼
تراکتور، استقلال، آلومینیوم و فجر؛ ۴ تیم بدون شکست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/139511" target="_blank">📅 00:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139510">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✔️
✔️
محسن خلیلی مدیر پرسپولیس: برای دربی 5 بازیکن جدید در پرسپولیس بازی کردند اما استقلال تیم پارسالش در دربی به میدان رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/139510" target="_blank">📅 00:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139509">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✔️
✔️
محسن خلیلی مدیر پرسپولیس: من شاهد هستم که تارتار واقعا دارد در پرسپولیس زحمت می کشد اما یک سری هجمه ها روی این مربی وجود دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/139509" target="_blank">📅 00:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139508">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👤
محسن خلیلی:
✔️
با کفش‌های بیژن طاهری هتریک کردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/139508" target="_blank">📅 00:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139507">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✔️
✔️
جباری: سبک بازی ارونوف و نوع بازی تیم با توجه به تغییرات در حال هماهنگی است و به مرور زمان بیشتری برای بازی پیدا می‌کند   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/139507" target="_blank">📅 00:06 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139506">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00e2475d08.mp4?token=ss5D8GAvUIgTjI5YUQiWFe-cAPVWZLyxh2o0kcUCPGiD8wxyOBvqaE6WAM6pNaGJE7QKXTbBM8hxdZrBI4anoZy6yNShsQP1HUXl0BDL9X1yvAZeWw5dcLBlWaIJiiNi5OO5WbtVY6cZPcQT13fl2DUU-_aQF5XgOd--nce1IQtdtiTZ22C_tqkhKKBrE6c-WXe-7S330KhYJt72h66bol5HLN0Amk7gk8oUQ2UXswuELZy6bqq4iJdi_QlzpRTOSyKq5U9nZL5bmIKCVw9aOonwU_T8NoiU7J1FQSUx7cf11WG4pdO0DJRgiK8s6x9s902cfvbNDA2olc0-ADyL4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00e2475d08.mp4?token=ss5D8GAvUIgTjI5YUQiWFe-cAPVWZLyxh2o0kcUCPGiD8wxyOBvqaE6WAM6pNaGJE7QKXTbBM8hxdZrBI4anoZy6yNShsQP1HUXl0BDL9X1yvAZeWw5dcLBlWaIJiiNi5OO5WbtVY6cZPcQT13fl2DUU-_aQF5XgOd--nce1IQtdtiTZ22C_tqkhKKBrE6c-WXe-7S330KhYJt72h66bol5HLN0Amk7gk8oUQ2UXswuELZy6bqq4iJdi_QlzpRTOSyKq5U9nZL5bmIKCVw9aOonwU_T8NoiU7J1FQSUx7cf11WG4pdO0DJRgiK8s6x9s902cfvbNDA2olc0-ADyL4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
محسن خلیلی:
✔️
با کفش‌های بیژن طاهری هتریک کردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/139506" target="_blank">📅 00:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139505">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇷
🇮🇷
نظر محسن خلیلی و بیژن طاهری درباره برگزاری دربی در اصفهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/139505" target="_blank">📅 00:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139504">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a595378b0.mp4?token=gXkr886SpbuxJ25rOh6Fq6-fVwr27_S7JplwCIZV0JvSWpqxerk3hXIA9toQy7VywCV2OEtV2ue8ZZJ49Jpcq4OnefipFh317DkN4xkeDumj8Dq2WM9opEDU2_7fFO1EI8Y-N733n0rLf77bgI3W2eeuGTz0V2tezo4KrzBzLo2j56BLhv-0px3cszx2eUY1TRjQ2nzT5NSluXtQI6nZT0knaxQmgbP_uNoQYXaQd7LLdg3PJl-R2zvCfMbuD_EQt9NhNfZ9qR9JSWP_HliZsfpgIug6Plw6UZ8lnJZ2NlYjHi1g52bWsQtx57qThnMNh0D5BnZ4NmZopCOfXs0zmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a595378b0.mp4?token=gXkr886SpbuxJ25rOh6Fq6-fVwr27_S7JplwCIZV0JvSWpqxerk3hXIA9toQy7VywCV2OEtV2ue8ZZJ49Jpcq4OnefipFh317DkN4xkeDumj8Dq2WM9opEDU2_7fFO1EI8Y-N733n0rLf77bgI3W2eeuGTz0V2tezo4KrzBzLo2j56BLhv-0px3cszx2eUY1TRjQ2nzT5NSluXtQI6nZT0knaxQmgbP_uNoQYXaQd7LLdg3PJl-R2zvCfMbuD_EQt9NhNfZ9qR9JSWP_HliZsfpgIug6Plw6UZ8lnJZ2NlYjHi1g52bWsQtx57qThnMNh0D5BnZ4NmZopCOfXs0zmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
محسن خلیلی مدیر پرسپولیس: ۸۰۰ میلیارد بودجه لازم تا ورزشگاه آزادی تا چند ماه آینده آماه شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/139504" target="_blank">📅 00:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139503">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">⚽
🎙
رضا جباری:پوریا شهرآبادی جزو 3 مهاجم برتر لیگ است؛بازی در پرسپولیس پرمهره از بازی در تیم ملی سخت‌تر است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/139503" target="_blank">📅 00:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139502">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">⚽
🎙
رضا جباری: کنعانی و علیپور با رهبری‌ خود نقش کلیدی در ایجاد همدلی و ساختار کلیدی تیم دارند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/139502" target="_blank">📅 23:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139501">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✔️
✔️
جباری، مربی پرسپولیس:  یکی از جذاب‌ترین داربی‌هایی بود که در این سال‌ها دیدیم. تیم پرسپولیس همیشه بالاتر از همه‌ی نام‌ها است. دنبال ۳ امتیاز بازی بودیم که به آن نرسیدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/139501" target="_blank">📅 22:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139500">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AlIMG8X3UkAgFXpd5XF2px95t7ezPfkYfZ5mHDZ6dVvoZA1tIem3e1VZHDprd_1MqaCa4-lXQdaOqckN5Wkse2ZUeXSmftoLiwPnYDgMOsTvgpzRyV92qTKyQla6a1quKlPlI75bNUZvoDdjq52n6ehLR3wh3hlY3N9GgQ2avG3ok2cUvhWVpL_4q8T2GZVtI9uUJ7vuBHRUPl8GXIvNRpcqf6YK_KsLbEQRTW9UhcehStD416LPxdenhBzlsZbhUgeYxP6sfM7Fs-SyUOyCLGNWJAd9T6XmyU-JlVGGmZzabiMHIFa-8BzYD9bevZxO1CmRyIlF3A8ktpcTBjnqoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
تست های پزشکی تیم بانوان
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/139500" target="_blank">📅 22:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139499">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iG8oLYvL8k_MB6XHisDII1AS0BJJ-b8Y8xxJUpyHff7VtrS9Qmd2Ir4uNZw1-Bg6AU1xMkEDFWi5UOAKDIxNNYV441g0C6Z5yPR3_WZepcbG1tI0z1zXFCXtI__dqx_SmztauzVu-cy1sFr6JplMF9w27-i75ho-E2eTLyPQglSWm7VX_Hdrd_-zusbV8SU_OXzAeA4oedXnNar3-VytvoIHFxZuJVV4ZkMirWsmdafplvF7ynOxruninf156TShquYBwK6vQf26nE-ib5NJgOcP6By8Bd-kfLZsXwIFmqIbnJof0Zq0L3JNhWVJDvSVF_K1-7q4HJwUypku_LTANQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کمپانی دیشب یازدهمین بازی بدون شکستش مقابل استقلال رو انجام داد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/139499" target="_blank">📅 22:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139498">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrPkwsmKttXPnV21VUhUt2WiUA3MOA_9LT6KMjIjeNvBHYgeBbk4ZUfNmLpYYljW2YLAr90GoOD4NCiVaPyTGW_X2TJ0JfFMqVpefCRU-IxUmGE02u_3SJLdDT_fDolpjtvYXhQKoU8uAZthG93Up8xShi9F68zNBZj8oKNrJvjS2I_2KWtcJihE_48s8HGpVS4o6H_1koYjH9dL_FWZi0DbTLyrfYjg_b6lolKt1s2DrECqf5nLIfDYD9cQY5nhOKTCsDokP27X60lFD2BT6Ng0Oi_d6Yj3ifzfteFw-pPyCK_GzmrfyvTQlV_Z_4ozjlGlyY_HGgiamqgwXW6ENQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دیدار برگشت شهرآورد لیگ برتر بین دو تیم پرسپولیس
🆚
استقلال به‌احتمال‌زیاد 20 اسفند ماه در ورزشگاه صدهزار نفری آزادی برگزار خواهد شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/139498" target="_blank">📅 22:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139497">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✔️
✔️
تارتار ضعف پرسپولیس را پیدا کرد!
✔️
تارتار به این نتیجه رسیده که پرسپولیس نیاز به یک رهبر در خط هافبک داره و نیم فصل قطعا در این پست تقویت خواهیم شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139497" target="_blank">📅 20:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139496">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezi7taey5-XTxl-RL4N_Xt6xdqQXV9uDqCevTA_oD-2kHUHsGjMwtClN1D0nFWTjaj_Ly_gwFXEI--zzZucKL0zF3TatBpFyoJS6yWKfUZBpbZ962-a9w17anuHwFE2GDOJR_mxFXOc8hOGIi6reKtPokO2ovJuxbpZqMxgQ7NE8Ngk9ZvrNxs6KTyMKBDW_vEVCH4fNuPzk2cJ8pmDRUiEoLq7PI3GJmpgukw0QX9B_2mUupeCrPtAh2UBF-ZppTBfe3vZWb7-PbMn_Fk5lQFe40o_MZ4SQ76evfDWAeMpeAK9QkRZX_OllTxJr7zD_GkG-_TSSFc8rXuDObqylmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🎙
خلیلی سرپرست پرسپولیس:
❌
مصدومیت گرا از ناحیه آشیل است. تارتار گفت اول باید او را ببینم و در مورد ماندن و رفتن وی نظر بدهم. هیچ اختلافی بین اورونوف و کادر فنی نیست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/139496" target="_blank">📅 20:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139494">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNZM0t8LJYnmCnTiOvhl1nNJfq8l204I9TqByjpB3civ-9LAJDc2-TvQfqysmdMlDVAXEFA9nqCwy4Lyo6jUhmV1c35fLC5byw5F_e_OJiHasDEaHARIWwlRV9NjIQpuzX7l18cssjE_78K-bXSbzvgFUl9cCltBCqYfP5xjC0QQ6_Ng5pDRzu3veojKKWZRwT0NYPU20icDUiTMnu78RRrrJt5vPK14yAdXcdGgbcfs4i12cHT1gJoHAoyRj2OfMzfDZep58yebImwSsKVhjllGVbLip7FvO6nHWfLypRGbs57ax48gunAueJAAy_Y94QK_cp8a7lBHdOTXH8NpRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
نبرد سرویس و قدرت در نیویورک
فریتز به‌دنبال عبور از سد بلوچی
شانس بیشتر با ستاره آمریکایی!
[
تیلور فریتز
🎾
🆚
🇮🇹
متئو بلوچی
]
🟡
تنیس یواس اوپن
⏰
امشب ساعت ۲۰:۳۰
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
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139494" target="_blank">📅 20:14 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139493">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBqBSpEX-bZ4gdMBPD75WtToNF1mbOefPVY1qWE2Qggk_ZzjR9De5FN5KxwTMGhCXV5GjwcHbjluRG7u8JTo5QpXcTg-8xEqN6-UAwR8xfXj2_D7-mluC8Iw6ZmBreMqQSfesq77rnZCq9VIFf1XL7virriYTdD8cedsAbeS26pvQKEH9baRunY0xOCz8FOJXf7Op_MUyPOACeTLrmDPvl87bn9VnQnrIY8-q-d9j0YQ1YnCVD4yNylO4YaxnwqUy0cmKXIj8gVAZVa50jNITp_0EinZJfYTJ7Bmx4YZfEdqgrLGZi73e-rDb3ZESSuVMMgXVomuJy5VpslhgP74fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
حضور ابوالفضل جلالی در بازی امروز
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/139493" target="_blank">📅 19:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139492">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZW3SvNR1TIQlcVNHCyO11FI5U-NtazqFtJvfHLMaXK4zKtKKwZpSkl0P2u1UfmuZ-dSALbwLbP-DUpD62ziDqG-hsEr2MpVZxDMWKR6tnCIPIb8Zjb7BAZzg930JOFp5Z42r1VuA01efcX5VUZl7ExPM5JHpVIa2cJLYJ9tAXBPtsJRkakOLTJTMhfZhlHpSZz6sKpoeJk20nvmH9ASREE9Vjoo6l4Ff5a3joGixxYKFHFw7PMeRtH1TlxUVFi7L1zhqiMRtJleA7qcwu2Dwd-Y1RYblIONYUDQvCoz7S9Y8G_Oej52SvTKoCKLeXsFAoD9sExwqdid4OlUJi5qYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
محمدمهدی محبی زننده ۲۰۰ مین گل تاریخ دربی بود
👌
❤️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/139492" target="_blank">📅 19:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139491">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">#بماند_به_یادگار
🔗
💯
تا روزی که اردوبادی و اینانلو داخل هئیت مدیره هستن این تیم رنگ آرامش نخواهد دید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139491" target="_blank">📅 19:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139490">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyjuhsrL7Mb8zOxZkx3IyCGRu_0G0B9Qu1un1zhZJ0Kvf1P4EtiA2mEoQ5k4aqNZGa5-XugmRIJ6t0VH70tWuTULTpoG1_m13JcPzQgHmblejlM9m6qRTZBaSW-zBIPeh7oaaxGqUb5famaNmXrX6Aq3hthGEyolCMYFJjFn1Yh9ysEZ678cO0FaVs4Ds0bchDH3LAvhEOaAwUUctddmTU3IpRbzb8Rup9rOey4bk-bftRfIj0t77ta_8k8_Iv929BkcajajdqXClnirVZPL23Icf2kNdHWC61mkqMtM8LhvmBX74Y0ko2LQo8Si6JiyGaRUKez8USe0IzPQ2nTuAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
پرسپولیس امروز در دیداری تدارکاتی به مصاف مس رفسنجان رفت و با تک گل پوریا لطیفی‌فر به پیروزی رسید.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/139490" target="_blank">📅 19:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139489">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWRNaQ5_ugYVMYuhZMpqGQJYV7jjnoc0kA0R4mKBGVXx8tjl8Fq_ljBfEvdOH0xE2MNywOzcKy4zhks9IPRyA5-ymOYFenIkRj_l2IrFE8wagwHwW50DYRzaePgTDopGbqPPrAiXEsFCuk9ZJloYqpZQUMx-NhRruwqAjKS2B56MnuUdrKlejwGtf8U-lH0zl8TE90xa_CQVDp7H1ako3r9zelONamLO1-oLMRUkNYXnmNSc08BulwGw0a7pFoe5bbrT3Y3-lpfz_0NYHUGAq4Ut4-QAd9Z-so2B6fPdmRBxrz2yvvWG35DvXmBgto28fiib4MexTFNEGqymDG3SCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
🗣
محمد عمری از فصل قبل تا الان توی ۱۷ تا بازی برای پرسپولیس فقط ۲ تا گل زده!
⬅
⬅
با اینکه آمار همه‌چیز نیست و کارایی بازیکن روی بازیِ تیم هم مهمه، اما هوادارها اصلاً ازش راضی نیستن و انتظارات رو برآورده نکرده. امیدوارم بازی دیشب براش درس عبرت شده باشه، تصمیم‌های درست‌تری بگیره و بیشتر به درد تیم بخوره
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139489" target="_blank">📅 18:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139488">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🏅
باشگاه استقلال قصد دارد به دلیل حرکت حسین کنعانی‌زادگان در دربی ۱۰۷ مقابل عارف آقاسی علیه این بازیکن شکایتی را به کمیته انضباطی فدراسیون فوتبال ببرد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/139488" target="_blank">📅 18:00 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139487">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFaC9aXpiXJu6LKG-XQZ5hwHi6_3TawB1hvk8DTgi7esybs1OR7NCWIDNFJMMpsgv3eYAyUlKL1lj_kN4RUjZML9It4m_op74qSu775ohmsdxQArmLfeTii9DzI8MHtehQesbYUFkp-k102FIKIPRMNv1rL3rB9jbLfI7dV-XKi5qQZfP6HZl8uedv4BBDmn4QnsHC8RZNt5mY0z6JvELWXyogywoIbwIjZHtzbPPIORJMMB1MMIyI4-OD9xhGNEptvBJv7GRKAtU1gAYWE4W4j4SPRV8i7DwCXB8ta6yE0pK4ENlbjHNvRGcTGq8f9CiIZ9_Fbqr-TCk-n2kIzWUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
باشگاه استقلال قصد دارد به دلیل حرکت حسین کنعانی‌زادگان در دربی ۱۰۷ مقابل عارف آقاسی علیه این بازیکن شکایتی را به کمیته انضباطی فدراسیون فوتبال ببرد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/139487" target="_blank">📅 17:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139486">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✔️
✔️
دانیال گرا مدافع مجارستانی تیم پرسپولیس برای هفته پنجم از لیست بازی خط خورد تا یک سهمیه خارجی سرخپوشان برای فصل آینده به خطر بیوفته.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139486" target="_blank">📅 16:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139485">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✔️
✔️
خبرگزاری مهر:
🔴
پرسپولیس پیشاپیش شکایت خودشو برای حضور یاسر آسانی تو دربی آماده کرده. پرسپولیس اعتقاد داره کمیته انضباطی و سازمان لیگ صلاحیت لازم رو برای پرونده درباره یاسر آسانی رو ندارن و استعلام فیفا باید منتشر بشه
🔴
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/139485" target="_blank">📅 16:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139484">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
❌
❌
❌
طولانی‌ترین روند شکست‌ناپذیری در تاریخ دربی؛ پرسپولیس با 20 دربی بدون باخت
✔️
✔️
کیسه کش حسرت برد دربی رو به گور می‌بری
😂
🫵
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/139484" target="_blank">📅 15:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139483">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9bc0b70b2.mp4?token=QF6JHTOmovc27WDHv63yO66xFvQrDY6uYDUTW3P0-t1g2EbBV2o7d8fOd1WWJpS2_id4t9FNQyJCCdQyYF0auyiJiUvaH51Q6KYGyZBRlYzGfSisVbzv7ejFGCUYss9rQLFdHVkUN5XMrSLhdyb3xBO3LMr1lmqvH57hFZ86fAJFD90vrBCYl20vaj-6QzFaCel_BPZn_5WcNCwU0QV8rytfrHrnm3nIQRand-zYEj2TyCQySvnnfqw81HE6GdlCPWuHSseW5JkzRoKnG7xrBTMLwer1lovHijMxgC0bIpx6Pap3eduKr5_tI4XhXmqVqPaQbGW9n8mZ7wojgz10S72aIeCK2OkLaUXOVD-2t-ndzpnB7619hvnRbRilfCLv9ebkT7GYhkM5LBFVHZvb92OcTLj7wgOHFi2WIVx5Aos75XJrim6PE5fOu4AXmiojCCOqsjYeo4j8vjum1sr9J6IFff80DmGXHG_o8RsEjGeF2F85_2wbltBymHLh_cp2LkFUqPztR3tYH61PAjDe2Fp6lR7GUEtbyilN8tzrun7HkPaqNSJ1NyPDqy0EF7_zQdDEPpBZrwYhKlb9JlBclmDHKRhdEVwygfsQ-UG4dcI1V1QK2D2DMBULsjPKpJhN0t4oFtnl57Il9iq2nFM1IvVXS7cumw9SmuMuSqLk88Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9bc0b70b2.mp4?token=QF6JHTOmovc27WDHv63yO66xFvQrDY6uYDUTW3P0-t1g2EbBV2o7d8fOd1WWJpS2_id4t9FNQyJCCdQyYF0auyiJiUvaH51Q6KYGyZBRlYzGfSisVbzv7ejFGCUYss9rQLFdHVkUN5XMrSLhdyb3xBO3LMr1lmqvH57hFZ86fAJFD90vrBCYl20vaj-6QzFaCel_BPZn_5WcNCwU0QV8rytfrHrnm3nIQRand-zYEj2TyCQySvnnfqw81HE6GdlCPWuHSseW5JkzRoKnG7xrBTMLwer1lovHijMxgC0bIpx6Pap3eduKr5_tI4XhXmqVqPaQbGW9n8mZ7wojgz10S72aIeCK2OkLaUXOVD-2t-ndzpnB7619hvnRbRilfCLv9ebkT7GYhkM5LBFVHZvb92OcTLj7wgOHFi2WIVx5Aos75XJrim6PE5fOu4AXmiojCCOqsjYeo4j8vjum1sr9J6IFff80DmGXHG_o8RsEjGeF2F85_2wbltBymHLh_cp2LkFUqPztR3tYH61PAjDe2Fp6lR7GUEtbyilN8tzrun7HkPaqNSJ1NyPDqy0EF7_zQdDEPpBZrwYhKlb9JlBclmDHKRhdEVwygfsQ-UG4dcI1V1QK2D2DMBULsjPKpJhN0t4oFtnl57Il9iq2nFM1IvVXS7cumw9SmuMuSqLk88Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
❤️
👀
✔️
تو این صحنه کسی متوجه نشد ولی وقتی از دوربین نزدیک تر صحنه پخش شد مشخص شد نوک انگشتای نیازمند بود که باعث شده توپ به تیرک بخوره وگرنه گلو خورده بودیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/139483" target="_blank">📅 15:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139482">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
❌
20 بازی بدون شکست
🔥
✔️
حسرت کیسه در آستانه ده سالگی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/139482" target="_blank">📅 15:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139481">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❤️
خدا بنده لو، بازیکن پرسپولیس:
⚪️
بیش از اندازه در مورد ارونوف حرف زده می شود. چیز خاصی اصلا وجود ندارد و هنوز خیلی از بازی ها باقی مانده است. او اصلا افت نکرده است و اصلا زیاد بازی نکرده که بخواهد افت کند. همه از کیفیت اورنوف خبر دارند و هر تصمیمی سرمربی…</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/139481" target="_blank">📅 13:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139480">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">⭕️
⭕️
⭕️
با اعلام یاسر همرنگ
🚨
کوپال ناظمی داور دربی شد
📺
موعود بنيادی فر داور var شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/139480" target="_blank">📅 13:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139479">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✔️
✔️
باشگاه استقلال نسبت به عملکرد و سرعت بالای تیوی بیفوما مشکوک شده و احتمال می‌رود درخواست تست دوپینگ از این بازیکن پرسپولیس را مطرح کند.//هفت صبح
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/139479" target="_blank">📅 13:37 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139478">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vmr0kVoY3e6qaChp2Zf-2DQHsmjPaC4D48TNzjxhT-51ObUV8SuB6j-LZVIzMiDZ8dHMFJLvus18dp4XAs0sg1TeFEEv1qe1YVnTTDid2wv8pQDlmglpRSbmOxdFYBFdFOYzfiwvOhX7_kGR9W0YxjAcquDAkqr1GCu7JPTmtE5Vg8w4jByYrZuoomg7nxJze4xzdis1gIeRjfOuDwcBGxL30DoXXzwSdmD_hXoXGwoNEG3a_TnhrwLHkwCdhkbPp8ygOKAFuc-GoYpR4tQIHI7VbaEoCWIDW-7K_Wp-oA41lgbxM4MreGK398JDvb1YDRBr5Vs6sZEE5oyP6zSdPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سوسیداد و سلتا؛ جدالی برای سه امتیاز
دو تیم آماده برای یک نبرد نزدیک و تماشایی
کدام‌یک دست بالاتر را خواهد داشت؟
[
رئال‌سوسیداد
🔵
🆚
🔴
سلتاویگو
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
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/139478" target="_blank">📅 13:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139477">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔄
🔄
🔄
با حضور یاسین سلمانی در بازی دیشب حالا مهدی تارتار به تمام بازیکنان پرسپولیس بجز محمدحسین صادقی که تا حالا در لیست قرار نگرفته بازی داده و تمامی بازیکنان با ذهنیت آماده به سراغ ادامه‌ی لیگ میرن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139477" target="_blank">📅 13:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139476">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🤩
| فارس:
🔴
❤️
🔄
تارتار امید چندانی به دنیل گرا ندارد و حتی درصورت بهبود مصدومیت هم نیمکت نشین خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/139476" target="_blank">📅 10:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139475">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✔️
✔️
باشگاه استقلال نسبت به عملکرد و سرعت بالای تیوی بیفوما مشکوک شده و احتمال می‌رود درخواست تست دوپینگ از این بازیکن پرسپولیس را مطرح کند.//هفت صبح
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/139475" target="_blank">📅 09:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139474">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
♨️
🗞
| #فوووری از تسنیم:
🔴
🔵
👤
پرسپولیس بخاطر استفاده از آسانی مستقیم به فیفا شکایت می‌خواد بکنه نه کمیته انضباطی
⚠️
❌
کمیته انضباطی فدراسیون شکایت های گذشته در مورد آسانی رو رد کرده بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/139474" target="_blank">📅 09:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139473">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✔️
✔️
عادل فردوسی‌پور: ترابی قطعاً ادامه فصل رو از دست میده، با خودش صحبت کردم و گفت دو پزشک بهش گفتن رباطش پاره شده و باید عمل کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/139473" target="_blank">📅 09:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139472">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✖️
✖️
هافبک و کلا استقلال برداشته و خیلی خالی هست هافبک ما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/139472" target="_blank">📅 09:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139471">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❤️
❤️
❤️
❤️
🔴
صبحی که دربی و مساوی کردیم و هنوز داریم حسرت تک به تک نزدن علیپور میکشیم بخیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/139471" target="_blank">📅 08:59 · 12 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
