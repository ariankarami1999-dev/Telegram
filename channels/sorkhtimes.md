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
<img src="https://cdn4.telesco.pe/file/GI7TGwWfZbo2pOKp_iVLOFpUaNXsNWKSU-B6fNE8IIP7PKdKzxcRhvndyYVZw5k6JJoBN9XIbk8-CDN2pyiMuvQ7Dinu7Nbk1m2WYF1JUwOY6DeyJVe4yMORlY6w7zbnrziWW1HwvfBKn05zOXqv8IB7zMsXbuKAF2MxIyUPTqOJlEmD8wG0iWognD_Jg1MsQNlMX4qoRet8RGKA5mBPPCqVao9jb31I3E7eo6TDYnHuR2cxNZmjEQrdwqOMwTWv_kv6ZgFCDyYYSa7Cklwpo9iVm4R3MuZ_PNEP3_73vOXuFuUKI75N_o8AEOHCf51F28Q6dVM8VfF-qC34m7BjPg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 13:10:54</div>
<hr>

<div class="tg-post" id="msg-134772">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/us_Ry5Xh7MLgZZaNYXMf7SuYGGYWbdOZbKNM7M1PKyDTH6IUoV6WvXPnP4JwYzDFCVPMOFJorI0Mqa02uFgwjDvgANizE8klNjjYBsr7BUyxGlNIh8uRI2b0hLCiVld0c1X_XQMlOFDCa4I0PtZSdZX3GCSCVD-lML9Aiy4pNfGJlN1kswggfpnWP68uwkmtp9qQ7Y619E7WARld3sd_4r5a6XI1pRwkUPzgXfN1MrNfUJJ13IK5y5owujHscohzUOkjQ9eo7HBgYoFVaY5vWU9TxYxd7OF-aJbQfd1uoIIgaUGD6lrMM-d-JWuw-fS6tgHbrKVXP4ZvdHtEU8730g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ماجرا وقتی عجیب میشه که بدونیم سانل کونیویچ دستیار اول اسکوچیچ در تراکتور دیروز با یک تیم اسلوونیایی قرارداد بست !
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 879 · <a href="https://t.me/SorkhTimes/134772" target="_blank">📅 12:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134771">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">⛔️
⚠️
گوساله! گوساله هایی که نیم فصل با هرچی اوسمار بگه، اوسمار نیارید تجمع میکنیم کیر زدید به تیم مادر تیم رو گاییدید
◀️
اینقدر گاب نباشید آدم پرستا،هدف باید موفقیت پرسپولیس باشه فرد مهم نیست
◀️
یه مشت رسانه تخمی دارن تیمو به گوه میکشن باشگاه باید همه شونو تخته کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/134771" target="_blank">📅 12:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134770">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
◀️
باشگاه پرسپولیس درآمد و سود امسال از برند و لوگوی خود (منهای پول اسپانسر و‌ مالک) را 771 میلیارد تومان اعلام کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/SorkhTimes/134770" target="_blank">📅 12:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134769">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">#نظر_شخصی
📌
دوستان من نظر شخصیم میگم ممکنه خیلی ها موافق یا مخالف صحبت های من باشن که عقیده همه برام محترمه
📌
از دید من اقای اسکوچیچ مربی بسیار خوبیه و بنظرم باهاش میتونیم نتیجه بگیریم، اما چنتا نکته هست که منو نگران میکنه
📌
مورد اول:اسکوچیچ نشون داده قدرت…</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/SorkhTimes/134769" target="_blank">📅 12:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134768">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">⭕️
🔴
افشاگری تازه؛ ایجنت اسکوچیچ و درخواست جنجالی ۱.۸ میلیون دلاری
🔴
شنیده‌ها حاکی از آن است که ایجنت دراگان اسکوچیچ به دنبال عقد قراردادی ۱.۸ میلیون دلاری برای این سرمربی است؛ رقمی که فاصله قابل‌توجهی با قراردادهای قبلی او در تراکتور دارد.
❗️
اسکوچیچ در فصل…</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/SorkhTimes/134768" target="_blank">📅 12:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134766">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» حدادی شخصا میخاد با امید عالیشا،میلاد سراک،رضا شکاری،مرتضی پورعلی گنجی،دنیل گرا و تیوی بیفوما فسخ کنه.
❌
حالا باید ببینیم بانک شهر برای فسخ و آوردن بازیکن جایگزین بودجه میده یا نه
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/SorkhTimes/134766" target="_blank">📅 11:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134765">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78b91b0d6.mp4?token=OmYfvNqo8eIreixM8jzvjYrL5zapUhKrrp82xNyAkzK9LmFzB1czQdg9MvcM5JzVve3tsSOJ83JHeIic80Nxkhnr8o1vKJO79kCTpOcz8cqWJiGw2e4R7EJzp7Xo9Tb5tr8GN1XHeTc2DJgJXodvPaj-IBcYKtRgOO143NFKKlx0STbWSFdO3vouSQPIKwCRqZCMBsvgfPYvqGyrRU1Ha1uXNe1wh54gOX8mlpDOpapfpWZ-V2_uv398yQb7TqMz4dojdBv24Tlays7SJWxmAWa8A_6tguGhlfNgdfpPsPznxHR_W_cTZOEDR3pxEk7uNqFpnI3D163A6Fs1zsKOt3yrDzF0ne51s40T13hxs6EIyTc7lWeCYtJZjF93zLsJMzBiEalEAJXM0dNMWcthEJjvv1OjBXGem5HBtCIE8xy1GbeOdM7x_2MmGWrZ8by0BHv8yjnfUE2QRZJd251ZevColTG8Dr9eeeYcgk5GNJkkgIDV8PjlMubJATc3zGqzPoDfwKHhKdiltvkwwmiVZn73oGRkMewTn9s9NFUX9shmrvcByMKAaLpswWTmipQLPk8ZVzDIh3jXPpj5HWVn109lJE8z2aYyEogP3RjCIBtOhOW2D0GM6zUpUbpC51wanWasJf1vZsZbNJX2Vy8ufcJRtjO6Kv_p5sgRNWdvSMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78b91b0d6.mp4?token=OmYfvNqo8eIreixM8jzvjYrL5zapUhKrrp82xNyAkzK9LmFzB1czQdg9MvcM5JzVve3tsSOJ83JHeIic80Nxkhnr8o1vKJO79kCTpOcz8cqWJiGw2e4R7EJzp7Xo9Tb5tr8GN1XHeTc2DJgJXodvPaj-IBcYKtRgOO143NFKKlx0STbWSFdO3vouSQPIKwCRqZCMBsvgfPYvqGyrRU1Ha1uXNe1wh54gOX8mlpDOpapfpWZ-V2_uv398yQb7TqMz4dojdBv24Tlays7SJWxmAWa8A_6tguGhlfNgdfpPsPznxHR_W_cTZOEDR3pxEk7uNqFpnI3D163A6Fs1zsKOt3yrDzF0ne51s40T13hxs6EIyTc7lWeCYtJZjF93zLsJMzBiEalEAJXM0dNMWcthEJjvv1OjBXGem5HBtCIE8xy1GbeOdM7x_2MmGWrZ8by0BHv8yjnfUE2QRZJd251ZevColTG8Dr9eeeYcgk5GNJkkgIDV8PjlMubJATc3zGqzPoDfwKHhKdiltvkwwmiVZn73oGRkMewTn9s9NFUX9shmrvcByMKAaLpswWTmipQLPk8ZVzDIh3jXPpj5HWVn109lJE8z2aYyEogP3RjCIBtOhOW2D0GM6zUpUbpC51wanWasJf1vZsZbNJX2Vy8ufcJRtjO6Kv_p5sgRNWdvSMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
درخواست عجیییییییب هواداران پرسپولیس از علیرضا بیرانوند
🔴
«برگرد پرسپولیس»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SorkhTimes/134765" target="_blank">📅 11:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134764">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SorkhTimes/134764" target="_blank">📅 11:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134763">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
🚨
محمدحسین میثاقی: دراگان اسکوچیچ با عقد قراردادی دوساله سرمربی پرسپولیس شد. اسکوچیچ هم اکنون ترکیه است و به زودی میاد ایران!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SorkhTimes/134763" target="_blank">📅 11:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134762">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">⭕️
🔴
افشاگری تازه؛ ایجنت اسکوچیچ و درخواست جنجالی ۱.۸ میلیون دلاری
🔴
شنیده‌ها حاکی از آن است که ایجنت دراگان اسکوچیچ به دنبال عقد قراردادی
۱.۸ میلیون دلاری
برای این سرمربی است؛ رقمی که فاصله قابل‌توجهی با قراردادهای قبلی او در تراکتور دارد.
❗️
اسکوچیچ در فصل قهرمانی با تراکتور قراردادی
۷۰۰ هزار دلار
داشت،همچین قرارداد فصل  قبل او حدود
۱.۳ میلیون دلار
عنوان شده است.
❗️
از سوی دیگر، در حالی که هنوز توافق نهایی حاصل نشده، گفته می‌شود اتاق فکر آقای سردبیر از همین حالا مشغول برنامه‌ریزی و بستن تیم برای فصل آینده است.
❗️
همچنین مراجع ذی ربط به دلیل مسائل امنیتی به باشگاه توصیه کردن از جذب اسکوچیچ صرف نظر کنند
❗️
اگر این ادعاها صحت داشته باشد، روزهای پرحاشیه‌ای در انتظار باشگاه خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SorkhTimes/134762" target="_blank">📅 10:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134761">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SorkhTimes/134761" target="_blank">📅 10:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134760">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✅
✅
فوووووووووووووووووری
🔴
🔴
فرهیختگان: در صورت پیوستن اسکوچیچ به پرسپولیس هلیلویچ و دروژدک دو بازیکن خارجی پرسپولیسی خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/134760" target="_blank">📅 10:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134759">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
🔴
واکنش یوسفی هوادار پرسپولیس به شایعات پخش شده در خصوص کمک برای خرید بازیکن یا سرمربی:
❌
با هیچ ارتباطی با مدیرای تیم ندارم
❌
نه بازیکن میخرم نه دخالت میکنم
⛔️
به دروغ نویسان هم باج نمی‌دهم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SorkhTimes/134759" target="_blank">📅 09:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134758">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❗️
رسمی؛ باشگاه های اماراتی از جذب بازیکن و سرمربی ایرانی در فصل آینده لیگ ادنوک منع شدند و تمامی بازیکنان ایرانی این لیگ ها باید به ایران بازگردند/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/134758" target="_blank">📅 09:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134757">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfJPpUfQmI3GUS6f-ej_xDOF49c-j4AA8Bsa2W-qv2Fj_jmbMnd1hLj5lrlyBggn6o_lDT2hXbWypsHHMcKOmSENwNO20k5qiev0QnOLRnlQMXi31UaLdQ7kTZOYM5EQIonZIFE9-En9Y2QLxHAraNwcjCjj7Uisq-sqcybUWHJYRiy082u0m3ET0HyzIoSFwD-fvUAEIp69otvrXB66C3Yxnr-_jWhU8vxBVufZt_WW-XLjJx1MMuZN4XX-kt2U0VusBDMPulzMIv0JKaY6bJ4Xntmpqh9ddM0QvCaLp2IjBbxZaX4LIBdF1wBhBdMrFsyyGCtcRtBgXDkqmi62qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
صبحتون بخیر ارتش سرخ
🚩
✨
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/134757" target="_blank">📅 09:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134756">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">فوتبال فقط دویدن ۲۲ نفر دنبال توپ نیست؛ جنگ افکار مربی‌هاست! اگر می‌خوای بدونی پشت پرده تصمیمات پپ گواردیولا یا کارلو آنچلوتی تو دقایق حساس چیه، جای درستی اومدی.
در [لایو تیپ]، ما بازی‌ها رو در لحظه آنالیز می‌کنیم:
📊
بررسی فرمیشن‌ها و تغییرات سیستم در جریان بازی
🎯
آنالیز تعویض‌های طلایی و تاثیر اون‌ها
🔥
بررسی نقاط کور دفاعی و فضاسازی مهاجمان
⚡️
آمار زنده و تاثیرگذار که هیچ گزارشگری به شما نمی‌گه!
اگر فوتبال رو با مغزت تماشا می‌کنی نه فقط با چشمت، جای شما اینجاست:
👇
ورود به جمع تحلیل‌گران و فوتبال‌فهم‌ها:
🔗
https://t.me/+hhwRu0jTAzswN2Nk
🔗
https://t.me/+hhwRu0jTAzswN2Nk</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/134756" target="_blank">📅 00:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134755">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
سنگال گل اول و به بلژیک زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/134755" target="_blank">📅 00:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134754">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/134754" target="_blank">📅 00:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134752">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
🚨
محمدحسین میثاقی: دراگان اسکوچیچ با عقد قراردادی دوساله سرمربی پرسپولیس شد. اسکوچیچ هم اکنون ترکیه است و به زودی میاد ایران!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/134752" target="_blank">📅 00:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134751">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اسکوچیچ امضا کرده و الان رسما سرمربی پرسپولیسه/طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/134751" target="_blank">📅 00:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134750">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
هوادار متمول پرسپولیس به مدیریت گفته 3 تا بازیکن شاخص براتون میگیرم و پیگیر اینم هست افشین پیروانی به تیم برگرده / فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/134750" target="_blank">📅 00:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134749">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❗️
انگلیس از کنگو گل خورد
😐
🔴
چه جام جهانی سمی ایه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/134749" target="_blank">📅 00:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134747">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
بدرود کاپیتان دوست داشتنی ..کاپیشاه هر جا هستی موافق باشی
🤝
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/134747" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134746">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9366cf9e2.mp4?token=GVdbIJzzzGdM_CHX937sgsQhi6z5i5U9TIQqex2K0kI7-k1hRWbvm4Jbg4Hr3V8zyu_7eIzhCVhF5bMkzee9mAuDLKKx1GhzQ3v-7DrZqr5ZVr9-tLcxq9P12I8sA8aY2Z-20CXzWuSY4QvUwCgCMCFPxZm811YtrDAT6luCUGw5c7vRDRwVRVaCABsokmodBEG8_VvUkwujB4HQVxRBBnWnFwEZJAmhfeZeRK_REW8iVJoH6UDfgpJ9Z1oo85ztkZndQWHJ19-xn_4Bw86FnfCu6DrEzgonQCWJCLVuJIEYP_jmJdAfoM48ETj6VUJTjbJ8x8CjIon_jTOlEB4Dn5husdvFCVhuuBi_ntTgdkfXGE2ze5xf2jk-jBdWxsT93LDUWZtnPMXGwJV2wKVu9brELa9-gcKpyTQ3VEyxcS_pQtYb4BGL_d_OgWx--3_-XONHhbYFcY5tCmZVmTpO9_m1lbbqRiURldS0zeK2XiIn9WqFktg600QjSfG-NqHAatQCawROs6x_EcKRHgdDRu61apTtbXYPRuy0BawA_fKzVI7Ta5fXwpvV6W2iixRWbXVYtEzWKkiVb1PNHwBPdWexO2JkgoX4dRwxa8fAmmP9YaFJ29r1UU7D1-uJKo-J7nbzZI59gPsozRiK1a1FGq_SYQhBRnWsHpizuWIlVRU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9366cf9e2.mp4?token=GVdbIJzzzGdM_CHX937sgsQhi6z5i5U9TIQqex2K0kI7-k1hRWbvm4Jbg4Hr3V8zyu_7eIzhCVhF5bMkzee9mAuDLKKx1GhzQ3v-7DrZqr5ZVr9-tLcxq9P12I8sA8aY2Z-20CXzWuSY4QvUwCgCMCFPxZm811YtrDAT6luCUGw5c7vRDRwVRVaCABsokmodBEG8_VvUkwujB4HQVxRBBnWnFwEZJAmhfeZeRK_REW8iVJoH6UDfgpJ9Z1oo85ztkZndQWHJ19-xn_4Bw86FnfCu6DrEzgonQCWJCLVuJIEYP_jmJdAfoM48ETj6VUJTjbJ8x8CjIon_jTOlEB4Dn5husdvFCVhuuBi_ntTgdkfXGE2ze5xf2jk-jBdWxsT93LDUWZtnPMXGwJV2wKVu9brELa9-gcKpyTQ3VEyxcS_pQtYb4BGL_d_OgWx--3_-XONHhbYFcY5tCmZVmTpO9_m1lbbqRiURldS0zeK2XiIn9WqFktg600QjSfG-NqHAatQCawROs6x_EcKRHgdDRu61apTtbXYPRuy0BawA_fKzVI7Ta5fXwpvV6W2iixRWbXVYtEzWKkiVb1PNHwBPdWexO2JkgoX4dRwxa8fAmmP9YaFJ29r1UU7D1-uJKo-J7nbzZI59gPsozRiK1a1FGq_SYQhBRnWsHpizuWIlVRU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بدرود کاپیتان دوست داشتنی ..کاپیشاه هر جا هستی موافق باشی
🤝
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/134746" target="_blank">📅 23:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134745">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✅
✅
🚨
🚨
ایلنا: قرارداد شکاری و عالیشاه فسخ شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/134745" target="_blank">📅 23:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134744">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» حدادی شخصا میخاد با امید عالیشا،میلاد سراک،رضا شکاری،مرتضی پورعلی گنجی،دنیل گرا و تیوی بیفوما فسخ کنه.
❌
حالا باید ببینیم بانک شهر برای فسخ و آوردن بازیکن جایگزین بودجه میده یا نه
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/134744" target="_blank">📅 23:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134743">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔖
عادل فردوسی‌پور : نکنه پس‌فردا صبح با سوییس بازی داریم ما خبر نداریم اینا خبر دارن که مراسم استقبال گذاشتن
🖥
این همه تعریف از استقبال و دستاوردسازی برای چیست؟داستان تغییری نمی‌کند، ما از مرحله گروهی جام جهانی ۴۸ تیمی حذف شدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/134743" target="_blank">📅 23:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134742">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❗️
❗️
🔴
شنیده ها:اسکو تا اخر شب رونمایی میشه بعدشم تیکدری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/134742" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134741">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3n0S-MhUiKumCNx-x0-Maq4ZZ9BGF8mxaAwwDwV-HU0PfGv-H0eF-1SyAMLFat_tlR-myAKW4fFj1d26F40Qu6qb6JdjZ4fQyaNWOjXFbM2pFyak_dGxr5SqrMmEY5pjj0xoDi2n7ViX0y2tBFUxz9dv5lMW62zW8L2AwH54QIwEQBSCjx1Y0o3pzEN5JWl1fStvEeP3TtDprYe1TRb2ofFbYeGwfWZPqQ44zc-nrmdO0TAWQoDvPfCh6_RmI9038JmIM6hbDqHI57n4Oj2hcSxMEgdZ8rkjZfWE8WzNNObWDSSIYonvRBuv0EwKIa39Fn94Ur8Mms7feizjNZY3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
تمرینات پرسپولیس احتمالا از روز ۱۵ تیر در ورزشگاه شهید کاظمی برگزار می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/134741" target="_blank">📅 22:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134740">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">💬
ادعای عجیب دبیرکل فدراسیون فوتبال؛ ممبینی:
🎙
چادرملو برنده شد اما ممکن است گل‌گهر به آسیا برود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/134740" target="_blank">📅 22:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134739">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
فرهیختگان: در اردوی نیم فصل پرسپولیس  اوسمار ویرا جلسات شبانه ای در قطر  در یکی از هتل های دوحه  با هوادار متمول با هماهنگی سروش رفیعی انجام داده که این  اتفاق باعث بی اعتمادی مسئولان باشگاه شده ؛ که خبر این جلسات به گوش بازیکنان هم رسیده و حواشی در رختکن…</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/134739" target="_blank">📅 22:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134738">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TF7oZPthupCoIQYR7DIS9Uj2b_RIc2WFqfRCifqlobniliRhPpGc9VH86Yx87WMCgog2BblOjBKtQSv6FUtSKkY2LG_a6gwON-rECwftOqV-gyn628s-K3b0y97ZSJQhLwJ3qvzjbaTpQz8oJAotenOs38OLQpUhU8u_tFpHdAydUDvGVt1nLPgpRmVrVpApwPHlAKlIlMvWIN9QOjt7-55IM-XvxgfMKjteX12NrrOZW9XyeVhKRlzGxQNdMrbKpwFJiqwk_Ad1ZHUCtwZb9eau0mTDagMpsQt9pL16vOauEEUe2RxPv1XXRRiKJU1ciaaPPOMbhSKuOOJbpEMu8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با اعلام ترانسفر مارکت؛
مجتبی فخریان به پر‌سپولیس بازگشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/134738" target="_blank">📅 21:57 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134737">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
🚨
🚨
🚨
فووووووووووووری
🚨
محمد مهدی نبی مدیر تیم ملی، هدایت ممبینی دبیرکل فدراسیون ، مهدی خراطی مدیر اجرایی تیم ملی، سیامک قلیچ خانی مدیر رسانه ای ، محسن معتمدی‌کیا مدیر روابط عمومی و یکی از آنالیزور های کادرفنی به همراه افسران أمنیتی تیم ملی موفق به دریافت ویزای…</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/134737" target="_blank">📅 21:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134736">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❗️
اوه اوه ...بیست دقیقه تا حذف انگلیس توسط کنگو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/134736" target="_blank">📅 21:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134735">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❗️
انگلیس از کنگو گل خورد
😐
🔴
چه جام جهانی سمی ایه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/134735" target="_blank">📅 21:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134734">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‼️
دانیال مرادی، رئیس دپارتمان داوری: ۱۳ کمک داور و ۱۲ داور موفق نشدند آزمون هارا پاس کنند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/134734" target="_blank">📅 20:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134733">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9ed04d87.mp4?token=kIGFcFCcS9lw1QTLn3AxqPMCsjBuXsmLtePeMs98GuuAI-B8qcJ829gdRxjvHGrc-zrjrL1f1IwvWOVFD2emhxDU5AxxnCW2fAR03AA9wzO_AJk5IM9Jf0vs6OG_4Fjv-j6FIbiwEbb0JDHtIn1I4uBXxb0ZrrTx0EkybzygLKw1r-me3wXpoIhL9nr_kTemnekDMbixoReV3SYRzSSH9WSzQU5Fi9mHhdPFPbU16jhgQnQNG7E-QOpi1bN_a5-Eu-T3Q7ycGQmkL2cOUCTLjrsnaMNCvrTn9iSsU8iolIkQqAlPOJAogM_3EZBjMDA6hYO77S4cLgPnUKebJ4lzZzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9ed04d87.mp4?token=kIGFcFCcS9lw1QTLn3AxqPMCsjBuXsmLtePeMs98GuuAI-B8qcJ829gdRxjvHGrc-zrjrL1f1IwvWOVFD2emhxDU5AxxnCW2fAR03AA9wzO_AJk5IM9Jf0vs6OG_4Fjv-j6FIbiwEbb0JDHtIn1I4uBXxb0ZrrTx0EkybzygLKw1r-me3wXpoIhL9nr_kTemnekDMbixoReV3SYRzSSH9WSzQU5Fi9mHhdPFPbU16jhgQnQNG7E-QOpi1bN_a5-Eu-T3Q7ycGQmkL2cOUCTLjrsnaMNCvrTn9iSsU8iolIkQqAlPOJAogM_3EZBjMDA6hYO77S4cLgPnUKebJ4lzZzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💬
ادعای عجیب دبیرکل فدراسیون فوتبال؛ ممبینی:
🎙
چادرملو برنده شد اما ممکن است گل‌گهر به آسیا برود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/134733" target="_blank">📅 20:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134732">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/80f7520ba9.mp4?token=KV0waImsm54ggHK-_UoJlMd_tnkQRW40aLyWynLG107Qhy4T-aQiETp3MNjzmh6uv_SmbBKlOyo_ki05tvuEnHZAOJ38LRGTPfBqVjcxU_LX11QpMD-_zcPzfz3m-FVhqkFXuY8IxChiFL-EM1VV-ck7xfByxlXd3wv7NCaDgAIZbkSFVphIl1lrOxSrGUv1OxozIbjOY7h8-gtgFumnQan9xveJwyTZm-9_djP1O0F-LSrQbSPZM6BDjnpv_iNYEQ-cIH_SVPVeDjOYzTEzJSosQkrbk7sywPhXCoxWpvS4wwFmidahD0PsUP58_Ov1c_wXsISNg88Wo9tkwZAT1w" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/80f7520ba9.mp4?token=KV0waImsm54ggHK-_UoJlMd_tnkQRW40aLyWynLG107Qhy4T-aQiETp3MNjzmh6uv_SmbBKlOyo_ki05tvuEnHZAOJ38LRGTPfBqVjcxU_LX11QpMD-_zcPzfz3m-FVhqkFXuY8IxChiFL-EM1VV-ck7xfByxlXd3wv7NCaDgAIZbkSFVphIl1lrOxSrGUv1OxozIbjOY7h8-gtgFumnQan9xveJwyTZm-9_djP1O0F-LSrQbSPZM6BDjnpv_iNYEQ-cIH_SVPVeDjOYzTEzJSosQkrbk7sywPhXCoxWpvS4wwFmidahD0PsUP58_Ov1c_wXsISNg88Wo9tkwZAT1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
شاهکاری دیگر از فیروز کریمی: قلعه نویی 5 سانت رو تحمل کرد 10 سانت رو تحمل کرد ولی دیگه 30 سانت رو کجاش بذاره؟؟
😐
😆
😆
😆
😆
😆
😆
😆
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/134732" target="_blank">📅 20:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134731">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» حدادی شخصا میخاد با امید عالیشا،میلاد سراک،رضا شکاری،مرتضی پورعلی گنجی،دنیل گرا و تیوی بیفوما فسخ کنه.
❌
حالا باید ببینیم بانک شهر برای فسخ و آوردن بازیکن جایگزین بودجه میده یا نه
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/134731" target="_blank">📅 20:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134730">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🔥
💵
اگه دوست دارین از بازی های
جام جهانی
یه سود تپل و درست حسابی به جیب بزنید حتما داخل چنل بت زیر عضوشید خفنه واقعا
☑️
🖥
JOIN
JOIN
JOIN
JOIN
JOIN
JOIN</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/134730" target="_blank">📅 20:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134729">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tm6rz7HvKryzzHgHD2kAOp-SfTzWuSxdJS12asgHyXxAv7trBw-aiApOEGueJX54kuR17APWTJ8Hxf06FzNU9dxupsIxQjto2dC9ovljq3fmp6C-UeYXikFuUnSr3mfsLndJne4gbV2zXcCLl1x0Q2J4UQ9rTjUJKYjm0-MY0GVdrHUhLLOqPLo_gEa6Ozw8hSQOpnkPzfFAeMNPilbUfiYv7ImfhLR5jjGRSfUC7qS0YeqXToIsHFHD_iQDj-uIfApUcfMfYca72ZqPu7pjH6QT1nDyw80AmWmZTXrM86unT2_E327qCmNDBVENYBLjdAJw7zwZdoculG3dl-V_zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هردو تیم گل میزنند_بله
Odd: 1.80
🛫
200میلیون
بستیم روی همین بازی اگه توم میخوای کلی از این آپشن های خفن ببندی (بدون ریسک) حتما عضو کانال VIPزیر شو
🛡
https://t.me/+6L9plEThEMk5YTJk
آمار روزانه 90 درصد برد
🔥
✅
با آنالیز حرفه‌ای و تخصصی که روی ، فرم ها انجام میدیم میتونید به سود میلیونی برسید
💵
💯
🆔
@ARON_TIP
@ARON_TIP
🆔
@ARON_TIP
@ARON_TIP</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/134729" target="_blank">📅 20:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134728">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/134728" target="_blank">📅 19:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134727">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✅
✅
🎙
امیر قلعه‌نویی:
🔴
از جام جهانی حذف شدیم ولی خدا بهمون عزت داد!
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/134727" target="_blank">📅 19:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134726">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
دلتون براش تنگ میشه؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/134726" target="_blank">📅 19:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134725">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
تشویق وایکینگی هوادارای تیم ملی تو فرودگاه
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/134725" target="_blank">📅 19:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134724">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
خطر بروز جنگ از جمله مسائلی بود که تردیدهایی را در جذب اسکوچیچ ایجاد کرده بود‌.برخی مدیران این نگرانی را داشته اند که همچون اتفاقات دی ماه که دراگان ایران را ترک کرد او در صورت بروز جنگ قرارداد را فسخ کند اما ظاهرا دغدغه ها و موانع برطرف شده بویژه ابنکه…</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/134724" target="_blank">📅 19:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134723">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
❌
پرسپولیس قرارداد را برای اسکوچیچ ارسال کرد
🔴
با رسمی شدن جدایی اوسمار ویرا، باشگاه پرسپولیس امروز قرارداد خود را برای دراگان اسکوچیچ ارسال کرد تا این مربی کروات در صورت امضا به طور رسمی به عنوان سرمربی جدید سرخپوشان معرفی شود.
🔴
قرارداد باشگاه پرسپولیس با…</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/134723" target="_blank">📅 18:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134722">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
🏟
پرسپولیس از ۱۵ تیر، بعد از آماده شدن چمن شهید کاظمی، دوباره تمریناتش رو همون‌جا برگزار می‌کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/134722" target="_blank">📅 18:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134721">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
❌
قرارداد دوساله برای اسکوچیچ ارسال شد تا امضا کنه! #ورزش3
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/134721" target="_blank">📅 18:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134720">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❗️
قلعه نویی: استعفا نمیدم و آماده میشیم برای جام‌ملت‌ها
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/134720" target="_blank">📅 18:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134719">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-Sl6gBailCWIGtKYi_3vzuTsro7uu29mD7eDmm2FUDpXNr8h-6eCOpiLUSl3TjNk6ArhzWSgSUkIWmEdVkEkBSUpiuL2dAtVesy9E9_4uTlaOxovvARoqCPl_AuC79VfCqZJj1fdYnYf1WOs-T86z6qvT-s3On3g0yKYcgPDNwRCAaEakQROuRkEgBmUZPRURknt3aH0k-jPZPZS0N2LJzI8CdnYzA3JkO7RFwTzk_LBS6W32zhxIPirVA1SBBjIhxhiOgyNBTzk79pV_CS67g5MVBOuRbRK-Ab4IsT0jwbyG5p6Rr9fTEySh9xo_L3NiY2Z0vCZnjvOiw_Wu90aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
شهاب زاهدی، مهاجم سابق آویسپا فوکوکا به تیم جوهور دارلتعظیم مالزی پیوست
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/134719" target="_blank">📅 17:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134718">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
تشویق وایکینگی هوادارای تیم ملی تو فرودگاه
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/134718" target="_blank">📅 17:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134717">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd1a0c4bd.mp4?token=MWBfGOssnriFZOBnUsLqurC68WUeJwuOyWfuDsRLdIG567ZCGyFXek9U2xcLOayPt3kdfbNWxTarLNFSozwX1F5I7zV9zykXYsrp9Lnv5fU-RxR5HSFp87akM7fme39nLNrWKqBBqCLND8RRzzGLkdp93-kVaeuoaSYm4kl2FnaErYYn5ndbBQJpfDCb8EAfJ6Nd5qD_mTJfJCeS63IfFm4OZzeLBh1EmS7q14UX_LhZxZjmv5fOBabxZ17gsgM3RNrKPBdicU5ZAMa8xkr9O5qAXDI_lGHltJjRPUkRaTbPofFj0BNkxILK8R74PLieET9QlllH0FBIa_HA_BthjX22rdEMLOjfWU9BN35TZga0pKd0cdyFXS8fzEkEBrAghLse-LecN47TjRPE00EKalNwYe3-sk1-Ol9BWY0ZrbvefC7Rd2xBaggec8Pm6RBEAJ9l_S-C3O4ZIwjOZ2j4Bb66VF4ZBObfCXQTk8kNAtxQkl4e_Z-37RLeF26t94-OstKvN14UKYL6eQBg2U257m1XfysYYMCdvvQzYk4ITBaIS5w2paHzX8gobTVLiGBgaE2Y8Z5tt8eHoQua3Xi8r7_NWpEGZc7wNtlDOOoVdbamuPh-CT_Qag3Oa3mXjT2IjvH_pjdNPVq8uAI5zAePeoE-uAKFPAjEMnyKghlgwj4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd1a0c4bd.mp4?token=MWBfGOssnriFZOBnUsLqurC68WUeJwuOyWfuDsRLdIG567ZCGyFXek9U2xcLOayPt3kdfbNWxTarLNFSozwX1F5I7zV9zykXYsrp9Lnv5fU-RxR5HSFp87akM7fme39nLNrWKqBBqCLND8RRzzGLkdp93-kVaeuoaSYm4kl2FnaErYYn5ndbBQJpfDCb8EAfJ6Nd5qD_mTJfJCeS63IfFm4OZzeLBh1EmS7q14UX_LhZxZjmv5fOBabxZ17gsgM3RNrKPBdicU5ZAMa8xkr9O5qAXDI_lGHltJjRPUkRaTbPofFj0BNkxILK8R74PLieET9QlllH0FBIa_HA_BthjX22rdEMLOjfWU9BN35TZga0pKd0cdyFXS8fzEkEBrAghLse-LecN47TjRPE00EKalNwYe3-sk1-Ol9BWY0ZrbvefC7Rd2xBaggec8Pm6RBEAJ9l_S-C3O4ZIwjOZ2j4Bb66VF4ZBObfCXQTk8kNAtxQkl4e_Z-37RLeF26t94-OstKvN14UKYL6eQBg2U257m1XfysYYMCdvvQzYk4ITBaIS5w2paHzX8gobTVLiGBgaE2Y8Z5tt8eHoQua3Xi8r7_NWpEGZc7wNtlDOOoVdbamuPh-CT_Qag3Oa3mXjT2IjvH_pjdNPVq8uAI5zAePeoE-uAKFPAjEMnyKghlgwj4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تشویق وایکینگی هوادارای تیم ملی تو فرودگاه
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/134717" target="_blank">📅 17:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134716">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✔️
#تایید_خبراختصاصی
⚽️
🤩
رسمی؛اوسمار ویرا از پرسپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/134716" target="_blank">📅 17:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134714">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUBATs-1sJVccUaGYZWp1D-NP2_jxIFteHG3ngSZ2b3U1FvW0W4nfsxkqzsqVkwdjGR4vA66n58bDrz2fetbnbWmSyQFTu4fkJCBLRoTPy6XpWwCzC1ihF3NG_CZrHjLvrNIMsyECp0L4AJmgaTKZ2mr6nmdpaaEzPF1EckZqWPFr9_UZ5xf-Zt_91E27iD-E-YataBlL6RfotllzEKV4GNaJc7yjtxQuZ8N58lFKdL0_2efn9TBQ-Dr9CDL48OeQcS7LFp-adV7x-6-syuSdcCoL7ePMzTw4SXDiuWzPMSJ1DQZi_9vfNmCLdXmPEkr1vCYN_wa_jriwTz3wwPSXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» حدادی شخصا میخاد با امید عالیشا،میلاد سراک،رضا شکاری،مرتضی پورعلی گنجی،دنیل گرا و تیوی بیفوما فسخ کنه.
❌
حالا باید ببینیم بانک شهر برای فسخ و آوردن بازیکن جایگزین بودجه میده یا نه
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/134714" target="_blank">📅 17:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134711">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✅
✅
شنیده ها :پرسپولیس تا ساعتی دیگه آفر رسمی رو برای اسکوچیچ ارسال میکنه تا با توافق کامل روی جزئیات امضا بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/134711" target="_blank">📅 16:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134709">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
🔴
مهدی طاهرخانی
🔴
یکی از مسئولان باشگاه بهم اطمینان داده که صد درصد و بدون شک اسکوچیچ سرمربی فصل بعد پرسپولیس خواهد بود
✅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/134709" target="_blank">📅 16:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134707">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQfn3c2vemZujcz7m_2z_aYGLXUXeTub7F3jfvOAzHVcqMaY5gJMCxKSUvDrWb_yCWTxzkOWe5QrR_dhq01K-sA7EZS0Nrz6O7Ja_66MO3UnPTN3gMGyKzpUI-utwKNa04gMymVgMHKsDjtqf6zJ4jh8h4PNEhXraPqi_KeLIoc47Km__-NZj2UPUmrtzIgh1qkFMG6ujiaTY4S3k6m_UTonP8HaWNiyyGO8RoMDaf-7bX4QRrYSKb02eg0FMtcrtoiypuPjgiwG_3AixjWCaIls3WqxKWsvzo6UAvyG43Y3-B6dwB_RVhZJoHTlcpLiiSsqDQt1ykXhR6fslAwrEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
دلتون براش تنگ میشه؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/134707" target="_blank">📅 15:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134706">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوررری
🚨
اوسمار ویرا ظهر امروز ایران را ترک خواهد کرد و جدایی این مربی از پرسپولیس رسمی شد…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/134706" target="_blank">📅 15:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134705">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7158fe0fc1.mp4?token=AyJPucSWVLOT4a2TvjyfFqLspGw7MrHKzLBdOJABAjR3B5_BPXBAjuj9N3fCIfBXvW2at-nZQXOoHiWmEoyCO-XIB5iRB9KDLa8Lenml4_QoLd1MmifXXUNTtvYRuBgKOzHl2L24QuYEnrghSYPTKCadprdFMaxY57xFoRR-b7doI6JchBSrgeaegyTCVI17kiFjc4ElPotw4KsEhl0S6s4Jl6FF_kAw7SnBz-jZcLCmhVV2R0bsbe_QTJId2uGKL-3Z_u2521XKasLtO8So8xxNRZtJFKeboTV6JZ80sn0axRA0I2xlqkKNTeuG1UorpbA7vl77ZfOjGBZE14uQyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7158fe0fc1.mp4?token=AyJPucSWVLOT4a2TvjyfFqLspGw7MrHKzLBdOJABAjR3B5_BPXBAjuj9N3fCIfBXvW2at-nZQXOoHiWmEoyCO-XIB5iRB9KDLa8Lenml4_QoLd1MmifXXUNTtvYRuBgKOzHl2L24QuYEnrghSYPTKCadprdFMaxY57xFoRR-b7doI6JchBSrgeaegyTCVI17kiFjc4ElPotw4KsEhl0S6s4Jl6FF_kAw7SnBz-jZcLCmhVV2R0bsbe_QTJId2uGKL-3Z_u2521XKasLtO8So8xxNRZtJFKeboTV6JZ80sn0axRA0I2xlqkKNTeuG1UorpbA7vl77ZfOjGBZE14uQyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
افشاگری جنجالی کاپیتان نساجی علیه استقلال
🚨
کاپیتان نساجی مدعی شده آرش رضاوند بین دو نیمه بازی استقلال و نساجی گفته «شل بازی کنید چون پرسپولیس عقب است» و استقلال عمداً جدی بازی نکرده و همزمان پرسپولیس کامبک زده قهرمان لیگ شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/134705" target="_blank">📅 14:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134704">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✅
✅
✅
تسنیم: علیرضا بیرانوند شهریور ماه سرباز میشه و باید بره فجرسپاسی
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/134704" target="_blank">📅 13:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134703">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🤩
🤩
🤩
باکیچ : کریم باقری هنوز هم می تواند در پرسپولیس بازی کند
💬
من گذشته کریم را ندیده ام اما می توانم قول و تضمین بدهم همین حالا هم او شوت های قوی و قدرتمندی دارد و اگر خودش بخواهد می تواند الان هم برای پرسپولیس بازی کند. او هر روز در تمرین شوت می زند و قدرتش…</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/134703" target="_blank">📅 13:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134702">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✅
✅
علیرضا بیرانوند ملقب به تنگه در آستانه عقد قرارداد با بشیکتاش ترکیه قرار دارد/ فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/134702" target="_blank">📅 13:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134700">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‼️
محسن مسلمان: سال 96 زن گرفتم و همون سال هم طلاق دادم. دو تا خونه و 114 تا سکه دادم واسه مهریه. الآنم دیگه پول مهریه ندارم که زن بگیرم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/134700" target="_blank">📅 13:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134699">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/134699" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/134699" target="_blank">📅 13:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134698">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lAytcoPzO_hndEr7cdFPMgeDb81a0rs8kjXTJMT_pUmTfk1sxbRS1GNX6EkSRw2c6RzDp4uQ-SCxiUcG7ZS9OEwWBxTORoJm347Fv8nJVnncXzqL_ZxQExokill-PTbTvXrZUxDDUOsfOevj1KT59P9GSVco3InwyfFa_tsicAuQ2vMXzjILVWK8OkG-Dxlunz_X1_Yz_En_KMdvIIo7frljbFBTQgWbRniEUgkx8cr41RbPx58gcIsvTstCl11oI_RCpqp5Vp-ck0q1untw6uhQws0rPaEzT1R7sMl5ZRV6Vzy_tr2nNMsKGcRKuoARLL2dMXiKt7548ymUO13ckA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
بازی فوووق جذااااب
انگلیس
و
کنگو
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
⚽️
🔥
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
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/134698" target="_blank">📅 13:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134697">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
🔴
پرسپولیس با طاهری تموم کرده و فقط بخاطر اینکه مشخص نیست قطعی باشه یا قرضی هنوز رونمایی نشده
/آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/134697" target="_blank">📅 12:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134696">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
🔴
مهدی رحمتی :از امیر قلعه‌نویی تعجب میکنم، اولین چیزی که او به من گفت، این بود که به هیچ‌کس هیچ قولی نده، اما خود او قول صعود داد.
🔴
🔴
اولین هدف آن ها صعود از گروه بود اما اتفاق نیوفتاد، پس بیایید عذرخواهی کنید، تاج و قلعه نویی باید حداقل از مردم عذرخواهی…</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/134696" target="_blank">📅 12:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134694">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✅
اوستون اورونوف و ایگور سرگیف اولین خارجی‌های تاریخ پرسپولیس هستند که در حین عضویت در این تیم در جام‌جهانی بازی کردند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/134694" target="_blank">📅 12:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134693">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
🔴
#تکمیلی؛ شماره 10 پرسپولیس در فصل جدید رقابت‌ها به مهدی تیکدری ستاره‌جدید سرخ‌ها رسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/134693" target="_blank">📅 12:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134692">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✅
✅
مهدی رحمتی: این حرف ها چیه که ما نباختیم. خودمون رو که گول نمیتونیم بزنیم. آره نباختیم ولی حذف شدیم اونم تو یکی از ساده ترین گروه های این دوره جام‌جهانی. تاج و قلعه‌نویی باید جوابگو باشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/134692" target="_blank">📅 10:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134691">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
کمالوند سرمربی خیبر شد!  پ.ن و. احتمالا پنگوین (مهدی رحمتی )سرمربی کیسه میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/134691" target="_blank">📅 10:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134690">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❗️
❗️
❗️
فوتبالی : شنیده می‌شود کریم باقری نقش بسیار مهمی در لیست مازاد پرسپولیس دارد و نفرات این لیست با نظر او و البته اسکوچیچ (که به احتمال زیاد سرمربی بعدی پرسپولیس است) مشخص خواهند شد.
❌
❌
قرار است اسکوچیچ بعد از سفر به تهران، جلسه‌ای را با کریم باقری برگزار…</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/134690" target="_blank">📅 10:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134689">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوررری
🚨
اوسمار ویرا ظهر امروز ایران را ترک خواهد کرد و جدایی این مربی از پرسپولیس رسمی شد…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/134689" target="_blank">📅 10:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134688">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
❌
سردار حسن‌زاده، رئیس ستاد وداع و تشییع رهبر شهید:
🔻
روزهای ۱۳، ۱۴ و ۱۵ تیرماه تهران تعطیل است.
🔻
روز ۱۵ تیر کل کشور تعطیل است و در قم ۱۵ تیر و روز ۱۶ تیرماه تعطیل است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/134688" target="_blank">📅 09:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134687">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
🔴
مهدی طاهرخانی
🔴
یکی از مسئولان باشگاه بهم اطمینان داده که صد درصد و بدون شک اسکوچیچ سرمربی فصل بعد پرسپولیس خواهد بود
✅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/134687" target="_blank">📅 09:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134686">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❗️
عملکرد اوسمار ویرا در دوره دوم مربیگری در پرسپولیس:
🔴
۷ برد - ۲ تساوی - ۶ باخت
🔴
۱۷ گل زده - ۱۶ گل خورده
🔴
میانگین ۲.۴ امتیاز در هر بازی
🔴
عدم کسب سهمیه آسیا
🔴
حذف از جام حذفی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/134686" target="_blank">📅 09:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134685">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✅
✅
عملکرد اوسمار ویرا در دوره اول مربیگری در پرسپولیس:
🔴
۱۳ برد - ۴ تساوی - ۱ باخت
🔴
۳۳ گل زده - ۱۷ گل خورده
🔴
میانگین ۲.۴ امتیاز در هر بازی
🔴
کسب قهرمانی لیگ ۲۳
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/134685" target="_blank">📅 08:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134684">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
🤝
🤝
اوسمار ویرا دقایقی قبل رسما قراردادش رو با باشگاه پرسپولیس فسخ کرد و از جمع سرخپوشان پایتخت جدا شد‌. بزودی بخش رسانه ای باشگاه پوستر او رو منتشر خواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/134684" target="_blank">📅 08:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134683">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/134683" target="_blank">📅 08:57 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134682">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اخرین فرصت برای عضو شدن بعدش میخوان  کانال رو خصوصی کنن</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/134682" target="_blank">📅 01:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134681">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gY9611JkMkh5YWAnOnaI6ikqkI84DCeErGJ1mLSdOtb76ge2gPNFUREPsHj2XzyclRPLzdk4_KXiWMjmEnUvOEzICcmzM2nWDNhPLRGzJkUTQ6QA2AMtjiHvVMiEpGRk3sK8fkaZt5NE_FBWLjy1qdg7puH6EduwQvYLnq0a2J7pkk6UAHdeEZibMLTnbH435JUqGTUuDocYeOqU5TnJKjEbsHR4bS8xFYrkAnDDggXzVjQ_8QOKY380a9hwcA9Suzf1MJUnw-wU4w9vPwyfcj9AfWjbbRsATdlWf4ARphcL4O1yn4Ke46-EOUdOWpl0Cp-Uk4VOVwLqLtahXV2poA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
55 درصد از علاقه‌مندان به فوتبال، فقط 4 سال یکبار شرط میبندن!
حالا چرا جام جهانی
❓
خیلی از نتایج تابلو و قابل حدسه
💯
مافیا که کارش دستکاری کردن نتایجه، زورش به جام‌جهانی نمیرسه و نتایج واقعیه
👀
به دلیل تعداد زیاد بازی ها، دستت بازه و کنترل ریسک و سرمایه آسونه!
🔽
?
💡
کافیه یه کانال معتبر پیدا کنی که کارش تحلیل فوتبال باشه و دارای چند سال سابقه کاری باشه کانال پیشبینی تیپستر پرشین همونیه که دنبالشی چکش کن
👇
https://t.me/+iIi9FxzzcYBjNDg8
https://t.me/+iIi9FxzzcYBjNDg8</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/134681" target="_blank">📅 01:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134680">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
🔴
مهدی طاهرخانی
🔴
یکی از مسئولان باشگاه بهم اطمینان داده که صد درصد و بدون شک اسکوچیچ سرمربی فصل بعد پرسپولیس خواهد بود
✅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/134680" target="_blank">📅 00:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134679">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
ایجنت دراگان اسکوچیچ: اگه اتفاق خاصی رخ ندهد اسکوچیچ سرمربی پرسپولیس خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/134679" target="_blank">📅 00:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134678">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✅
✅
تایید شد
🔴
تیکدری به پرسپولیس پیوست.//خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/134678" target="_blank">📅 00:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134677">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
🚨
آخرین جزئیات از توافق پرسپولیس با اسکوچیچ
🚨
🚨
پس از مذاکرات فشرده مدیران باشگاه پرسپولیس با دراگان اسکوچیچ، سرمربی اسبق تیم ملی فوتبال ایران و تراکتور، توافقات نهایی میان طرفین حاصل شده و این مربی کروات در آستانه حضور روی نیمکت سرخ‌پوشان قرار دارد.
🚨
🚨
بر…</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/134677" target="_blank">📅 23:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134676">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❗️
❗️
با توجه به برخورد و واکنش هوادارن پرسپولیس، عملا بانک شهر بی خیال جذب عزیزی شد!
✅
البته با توجه به حضور پیروانی در آمریکا، بعید است، محبوب ترین سرپرست تاریخ باشگاه پرسپولیس به شغل سابقش بازگردد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/134676" target="_blank">📅 23:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134675">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
🔴
پشمااااااااااام
🔴
صدا و سیما: مراسم استقبال از قهرمانان تیم ملی فوتبال فردا ساعت ۱۳.۳۰ برگزار میشه
😐
😐
🤣
✅
بخاطر حذف بین ۶۴ تیم اونم تو مرحله گروهی!؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/134675" target="_blank">📅 23:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134674">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
خبرورزشی: امیر قلعه نویی قبل از شروع جام جهانی از فدراسیون فوتبال ۱ میلیون دلار (معادل ۱۷۰ میلیارد تومن) پاداش گرفت. ۱ میلیون دلارهم بازیکنا و سایر اعضا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/SorkhTimes/134674" target="_blank">📅 21:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134673">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
خداداد عزیزی: حضورم تو پرسپولیس منتفی شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/134673" target="_blank">📅 21:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134672">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✅
خداداد عزیزی: حضورم در پرسپولیس منتفی شد و در تراکتور می‌مانم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/134672" target="_blank">📅 21:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134671">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
❌
فووووووووووری
🗣
فرشید حقیری: خداداد عزیزی به دلیل مشکلات مالی باشگاه، خونه و ماشینی که بانک شهر داده بود رو پس داده و گفته با پرسپولیس فسخ کردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/134671" target="_blank">📅 21:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134670">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
خداداد عزیزی: حضورم تو پرسپولیس منتفی شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/134670" target="_blank">📅 21:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134669">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❗️
❗️
با توجه به برخورد و واکنش هوادارن پرسپولیس، عملا بانک شهر بی خیال جذب عزیزی شد!
✅
البته با توجه به حضور پیروانی در آمریکا، بعید است، محبوب ترین سرپرست تاریخ باشگاه پرسپولیس به شغل سابقش بازگردد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/134669" target="_blank">📅 21:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134668">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✅
✅
حدادی  : خداداد عزیزی و خلیلی گزینه های سرپرستی تیمن  / هیچ فشاری از بانک شهر برای اومدن خداداد نیست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/134668" target="_blank">📅 21:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134667">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">✅
رفقا این فرمو میتونید سنگین بزنید
🔥
🔥
تخصصی ترین چنل شرطبندی تلگرام
‼️
#VIP
#رایگان</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/134667" target="_blank">📅 20:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134666">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOBJJYmgs1ubyCXY5ZqzlXf5RN1vmdJF433a_9PasD_bGJrs2-hfPBy4NKrcFNq8et36f9FqBDwiZalRu4TECQCH-DrWxUAafAyjEYDRcmnp9zeHihSY1bbB4VrCiM-OEH6FGrIbqrSWphnUy-10djssTrdJsqkJL8qXCojEmoERCJIux3e7raW16v0yRkLasgVCLMGJn9L6aRfmnjLIXtbhpKTsrwHHaG0bny379n2eaFsIkM7BOmDsVursmSQZp1duq1MGuJ3XBMlEn0VFeCuCWDJx2qjOiaqR3O1o5lsNjibHWJHWH5WcFvQsorxgmtHjzR0DkZhIhro6vWNJag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
فرم VIP از جام جهانی
🏆
🇫🇷
فرانسه
🆚
سوئد
🇸🇪
باضریب
⬅️
3.42
📊
گذاشتم
اینجا
حتما استفاده کنید
💎
شروع فرم ساعت
🔢
🔢
⬇️
👇
⬇️
⚽️
برای دریافت کلیک کنید
🤩
🤩
🤩
🤩
رفقااینجا عضو بشین تا شما هم سود کردنو یاد بگیرین
👇
https://t.me/+Bt80HN28Ils5YWE0
◀️
https://t.me/+Bt80HN28Ils5YWE0
◀️
💎
💯
100درصد وینه
💯
💎</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/134666" target="_blank">📅 20:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134665">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✅
اوسمار به باشگاه اعلام کرده به رغم دلخوری ها بابت قرارداد سال بعد، شکایتی از پرسپولیس ندارد.
📊
به گزارش خبرنگار قرمزآنلاین، اوسمار ویرا امروز در باشگاه پرسپولیس حضور یافت و جلسه ای را با مدیریت در ساختمان باشگاه برگزار کرد. علت حضور این مربی برزیلی، ظاهراً…</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/134665" target="_blank">📅 19:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134664">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
خبرورزشی: امیر قلعه نویی قبل از شروع جام جهانی از فدراسیون فوتبال ۱ میلیون دلار (معادل ۱۷۰ میلیارد تومن) پاداش گرفت. ۱ میلیون دلارهم بازیکنا و سایر اعضا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/134664" target="_blank">📅 19:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134663">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✅
شایعات؛ چکی که زنوزی به دانیال داده برگشت خورده و شرایط فسخ کردن داره و خودش بدش نمیاد دوباره با اسکوچیچ کار کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/134663" target="_blank">📅 18:42 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
