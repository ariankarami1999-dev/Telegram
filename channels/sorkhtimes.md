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
<img src="https://cdn4.telesco.pe/file/izXnxO6cpWykXVvVtxuwIxj-tBQAkqLZJXDlv8sh2wBjXgNld5Umv6PokunRY53q5PfXJQKd_TWwTYxPC7j4QBzmwrgpBFhdtMM8NZ84gk5NDvsMh-8kEUxqRSU55kIwCP-zQArptO9cToN8NyOizkSc1ymvTqPAgkmJ6KoIZHWHwejemC-vdbOZB6ardK28KpmFvzxUWRemPeoqrmh26SSKCBpUDerPbatp9IspSqhXHoETH4a663k9GT5Re_joer_VTa9ww0RMGh9tcZXvF1sE8dEAw-DatIHSuru9JT1cLDdHJLbXvbzQsnEIZoapRJNO5wnHQFbd1oTecYfOjw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-18 14:29:34</div>
<hr>

<div class="tg-post" id="msg-137626">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
💣
⚽️
🤍
فوووووری از فوتبالی: درحالی که فولاد به شدت دنبال رامین رضاییانه و به توافقاتی هم رسیده، ایجنت و فرستندگان این بازیکن به شدت دارن با پرسپولیس مذاکره می‌کنن و احتمال بازگشت رامین به پرسپولیس وجود داره و تنها مشکل مدیران پرسپولیس رقم درخواستیه این بازیکنه…</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/SorkhTimes/137626" target="_blank">📅 14:16 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137625">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
فووووووووووووری از فرهیختگان
❌
❌
پرسپولیس برای رضایت نامه دانیال ایری کلا 120 میلیارد تومن پیشنهاد داده درحالی که برای جذب زارع ، لطیفی فر و شهرآبادی مبالغ خیلی بالاتری پرداخت کرده
😳
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/SorkhTimes/137625" target="_blank">📅 13:59 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137624">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔄
🔄
🔄
گفته میشه باند شجاع خلیل زاده و علیرضا بیرانوند از محمد ربیعی در تمرینات تراکتور راضی نبودن و شبونه رفتن دفتر زنوزی و محمد ربیعی رو برکنار کردن...!
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/SorkhTimes/137624" target="_blank">📅 13:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137623">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PuFwpMEfeGUKQuSR8c8O9ROaVZh_x7yS9sg4jbBvGlAPdzVr04l7SdZO9Xn0TV43r4iSGSrXIvCNYRkNn2O69Y42SMNc3kDti-58PvUMZlOy4IGCBUyqZRj4rZZVWnYVq22JcW9eThMUKV7WByRaZdGda7r3HQv3-6OVijUhKQ5ipUJ4LkmJa03t0IawcOCJp6Vy0hCo63xwA_N9YNfg275INaKFSGRP0Nndnoh2Ommif-5n14NgoIDSTG5zsrV7YBUcxHvas8n5BtcN2KysBcw7BM-JydZT54jWLKELL3OSaazeNLVbOwcG-GmzBbUYz-J0__Ds2a85F_jnfppX9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
چهار دوئل جذاب، اما این‌بار بدون فشار امتیاز و جدول؛ فرصتی برای آزمون ترکیب‌ها، بازیکنان جدید و تاکتیک‌های متفاوت.
چرخش‌های زیاد و تعویض‌های متعدد می‌تواند معادلات را برهم بزند؛ اینجا کیفیت نمایش مهم‌تر از نتیجه است.
⚡️
دیدارهای دوستانه جذاب امروز رو با آپشن‌های مختلف و بدون خارج شدن از تلگرام همراه با
ربات اسپورت‌نود
پیش‌بینی کنید.
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/SorkhTimes/137623" target="_blank">📅 12:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137622">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eca828cb00.mp4?token=R6nujIZrOJ0w-mvFv6G9j672GRxAR57-xgOM-3bD356dlN9_ozJDvsXYORcHnTBdARnW7Yu4PJhyM8t3RCbakFsc0eKBjTvpy7bPqSq6sReDp2jVa-o70R6U-vYettVrYKahnyXaRROsZdI314fMTTYyAdVm6YFfuEYCR7VA0k8QUg6WQnbHAiUN5VLa7AU57fYsLvjkNVvAre8L6gq-P9Yu-QNOoWtoiOGZyxKVqf1kTeAs1RzQjpr8DxylMrlN5X3A0GaC3rkcSUpLF3FtaxH5QO8Eks9c74GJHUuHyVK6ccK5nbXEcwLeVZIn8d5tlzlPBGjLiJd_NTOYetBaqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eca828cb00.mp4?token=R6nujIZrOJ0w-mvFv6G9j672GRxAR57-xgOM-3bD356dlN9_ozJDvsXYORcHnTBdARnW7Yu4PJhyM8t3RCbakFsc0eKBjTvpy7bPqSq6sReDp2jVa-o70R6U-vYettVrYKahnyXaRROsZdI314fMTTYyAdVm6YFfuEYCR7VA0k8QUg6WQnbHAiUN5VLa7AU57fYsLvjkNVvAre8L6gq-P9Yu-QNOoWtoiOGZyxKVqf1kTeAs1RzQjpr8DxylMrlN5X3A0GaC3rkcSUpLF3FtaxH5QO8Eks9c74GJHUuHyVK6ccK5nbXEcwLeVZIn8d5tlzlPBGjLiJd_NTOYetBaqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نادر محمدی تو لیگ دو روسیه‌ با پرتاب اوت پاس گل داد و پشمای گزارشگر به این شکل ریخت
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SorkhTimes/137622" target="_blank">📅 12:42 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137621">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری
❌
❌
ورزش سه : محمد ربیعی در فاصله شش روز مانده به شروع لیگ از هدایت تراکتور برکنار شد و جواد نکونام بعنوان سرمربی جدید این تیم انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/137621" target="_blank">📅 11:27 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137620">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
فووووووووووووری از فرهیختگان
❌
❌
پرسپولیس برای رضایت نامه دانیال ایری کلا 120 میلیارد تومن پیشنهاد داده درحالی که برای جذب زارع ، لطیفی فر و شهرآبادی مبالغ خیلی بالاتری پرداخت کرده
😳
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/137620" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137619">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
❌
❌
فوووووووووووووری
🚨
رامین رضاییان تا دوشنبه مهلت داده به تیم های خواهانش و اگه تیمی سراغش نره با فولاد خوزستان امضا میکنه/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/137619" target="_blank">📅 10:31 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137618">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
بعد از دوسال هنوزم آوارگی ادامه داره
🔽
دربی در اراک برگزار میشه/ایران‌ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/137618" target="_blank">📅 10:21 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137617">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
❌
میگن دیروز تو بازی دوستانه تراکتور و شمس آذر شجاع خلیل زاده بعد از پایان بازی با محمد ربیعی سرمربی این تیم درگیر میشه و همراه بیرانوند شبانه میرن سراغ زنوزی و خواستار برکناری ربیعی میشن و ربیعی هم همون دیشب حکم اخراجش میخوره و برمیگرده تهران و بجای اون نکونام…</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/137617" target="_blank">📅 10:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137616">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✔️
✔️
✔️
ورزش سه: حجت کریمی مدیرعامل تراکتورسازی هم اکنون در جلسه با نکونام هست و تا ظهر نکونام معارفه میشه
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/137616" target="_blank">📅 10:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137615">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
فووووووووووووری از فرهیختگان
❌
❌
پرسپولیس برای رضایت نامه دانیال ایری کلا 120 میلیارد تومن پیشنهاد داده درحالی که برای جذب زارع ، لطیفی فر و شهرآبادی مبالغ خیلی بالاتری پرداخت کرده
😳
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/137615" target="_blank">📅 10:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137614">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری
❌
❌
ورزش سه : محمد ربیعی در فاصله شش روز مانده به شروع لیگ از هدایت تراکتور برکنار شد و جواد نکونام بعنوان سرمربی جدید این تیم انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/137614" target="_blank">📅 09:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137613">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری
❌
❌
ورزش سه : محمد ربیعی در فاصله شش روز مانده به شروع لیگ از هدایت تراکتور برکنار شد و جواد نکونام بعنوان سرمربی جدید این تیم انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/137613" target="_blank">📅 09:21 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137612">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری
❌
❌
ورزش سه : محمد ربیعی در فاصله شش روز مانده به شروع لیگ از هدایت تراکتور برکنار شد و جواد نکونام بعنوان سرمربی جدید این تیم انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/137612" target="_blank">📅 09:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137611">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
محمد ربیعی هم  در تراکتور ابقا شد.و خبری از اوسمار نیست
🔴
قرارداد ربیعی بند تمدید داشته که در پی توافق با باشگاه تراکتور فعال شد.
🔴
تراکتور نیم نگاهی به اوسمار و طغرل ساغلام داشت و شرایط و وضعیت انها را بررسی کرده بود اما پیشنهاد ارائه شده جدی نبود.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/137611" target="_blank">📅 09:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137610">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
فرهیختگان: مهدی تارتار جاسوس پرسپولیس رو پیدا کرده که یکی از بازیکنان جوان تیم بوده و امروز برای دومین بار به تمام بازیکنان هشدار داد که در صورت درز اخبار اون فرد رو اخراج می‌کنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/137610" target="_blank">📅 09:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137609">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBG9G4JnF9P1Iy8QmEC4nLMPWtWcHYR6uG5lh1AkURlIYelPq7W10_cacCdX-qaqPJcbbkSqFa6TsVGMUQqyZ2X6Q1NOovDDNmCDE8OqMZK0UDc1cB1PfUsl8dQ4URwch5XrNcgZW6JTDblG6AzW3JRrNA8G4laY5ScMOhdJgaoDrWyckkUbc18C8anqL12p3j3Z9fRP3jeHjzxMDGRrcAn441f_Aj5-0OC19fJQiGiexQq3nvAUAp-E2k1wQ-CKSwz__lWR55rcSOb2rjMhym0veKvXfO5boNUsAa-iC_YCByJB-U1N0SXT78NhQAoDoTIVExYIB7Csswa9683h-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/137609" target="_blank">📅 08:43 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137608">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYPn8qpYZvUabof663KmfmuoTjyEt85KjWRsmZ28QY2aYcfhA76h5pmmWKHBjLeKS_gxlwmr4FRq-Ti-0Q8CsDufx8FMEnMx5B_0TmqlrmNSo11Vyq6YyoXIkAHTODAhoBs6ckrBWwTBfgOvGlwrc8zdQiOPOhjabQNnev6aWv0f1xaXf6b03gymZeCiWrTO8_ic04ZfwVsIe1sTg4H4pP2_MvELZILS4ubUbfGZhW27zMVDEYNg6e70k_d5CouqO5wzKVyX2jakvq53XogF0asdUy9S0op4Y0ENA43yctJblwIFf6owMZMwDpXUj8JOBB9YwniXi5UH8CkmEZB_eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
👋
گل رو پیدا کن و جایزه ببر!
🧐
وقتش رسیده تا دقت و شانس خودت رو به چالش بکشی!
⚡️
همین حالا وارد سایت شو و حدس بزن گل زیر کدام لیوان هست و شانس خودت را امتحان کن!
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
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/137608" target="_blank">📅 01:47 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137607">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
❌
❌
محمد جواد حسین نژاد دقایقی قبل ضمن تشکر از باشگاه پرسپولیس آفر این تیم رو ردکرد و به‌پیمان‌حدادی مدیرعامل‌سرخپوشان اعلام کرده که فعلا قصد نداره به لیگ برتر ایران برگرده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/137607" target="_blank">📅 01:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137606">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
💣
⚽️
🤍
فوووووری از فوتبالی: درحالی که فولاد به شدت دنبال رامین رضاییانه و به توافقاتی هم رسیده، ایجنت و فرستندگان این بازیکن به شدت دارن با پرسپولیس مذاکره می‌کنن و احتمال بازگشت رامین به پرسپولیس وجود داره و تنها مشکل مدیران پرسپولیس رقم درخواستیه این بازیکنه…</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/137606" target="_blank">📅 01:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137605">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">⚪️
⚪️
⚪️
پرسپولیس برای تکمیل لیست نفرات خود در پست‌های دفاع وسط، دفاع چپ و هافبک، به دنبال جذب سه بازیکن جدید است. با توجه به محدودیت‌های سهمیه لیگ برتری، سرخپوشان برای دور زدن این چالش قانونی، استراتژی جذب بازیکنان آزاد را در دستور کار دارند؛ بازیکنانی که تا…</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/137605" target="_blank">📅 01:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137604">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
🚨
خبرچین رختکن پیدا شد / فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/137604" target="_blank">📅 23:52 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137603">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZOklSOxII_GVo1AvJwF3NAioPj9RCsZynxKry7AwL1zUO3C7GSNfaW1VqPbKXzCa5f_IQ8QCUwWEjDzZbteco3M2yBaU83nuDH4olldS4mgvAOEgTZe3sOESEmBwiwQ10YzQjsHB6e2Y3aNijpoMZWXidSVhmtvHUuaQbohfdSVY_xiME77aDalVJrPn9xLw9R-Kw-RVaTsquaFMsJewq5CooNp0diPKiffFWCGGGY6TNwI_ymEwM_tpNthqhDw8_xpras2Exti11rhXcFItjnbjfJic7LmoNP3ehoQDJl2jgOrS_heTImAjlalmDuLvxSKGCy2-JmPBkf7DGEUuaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
باشگاه سپاهان اصفهان امروز برای چهارمین بار برای جذب حسین ابرقویی نژاد به باشگاه پرسپولیس نامه زد ///قرمز آنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/137603" target="_blank">📅 23:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137602">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
💣
⚽️
🤍
فوووووری از فوتبالی: درحالی که فولاد به شدت دنبال رامین رضاییانه و به توافقاتی هم رسیده، ایجنت و فرستندگان این بازیکن به شدت دارن با پرسپولیس مذاکره می‌کنن و احتمال بازگشت رامین به پرسپولیس وجود داره و تنها مشکل مدیران پرسپولیس رقم درخواستیه این بازیکنه…</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/137602" target="_blank">📅 23:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137601">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
❌
پرسپولیس امروز برای اولین بار در دیدارهای تدارکاتی گل خورد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/137601" target="_blank">📅 23:09 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137600">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
رسانه های تبریزی از نزدیک شدن پرسپولیس به عقد قرارداد به محمد قربانی نسبت به تراکتور خبر میدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/137600" target="_blank">📅 23:06 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137599">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2af588d022.mp4?token=qRPsu7X-D5A_119FLBS8UBlsq8TYr1iCy5-wbMBRzlIt916D8qG89AHPYOXOEEVDhmzcHNRHNX0sioDxVwAJNpa2RP3IJI5wG6XJRhcwJ1Kc8smlP_lU2nL45zdb2F5WJluQsoMSx7oQ4Y-tQVappanwN_VesP-KGa_8I4uGZv8g96kD2tRY3Dv1O6ax1nAsqZ9pSkUJCA64Dr-S6Yitmw3SIgrIGJ6Xvp2EF1Sc_UOUbZyI4LzRZbd2fUTItJYdj3zOmsZuAWcRMMw2gle5z2Kqvl_4YmNR6CshJlwQDdYnwLqs1X66qPjKEWmzhmO73z_vSLk1zz9ItWnn3_lcIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2af588d022.mp4?token=qRPsu7X-D5A_119FLBS8UBlsq8TYr1iCy5-wbMBRzlIt916D8qG89AHPYOXOEEVDhmzcHNRHNX0sioDxVwAJNpa2RP3IJI5wG6XJRhcwJ1Kc8smlP_lU2nL45zdb2F5WJluQsoMSx7oQ4Y-tQVappanwN_VesP-KGa_8I4uGZv8g96kD2tRY3Dv1O6ax1nAsqZ9pSkUJCA64Dr-S6Yitmw3SIgrIGJ6Xvp2EF1Sc_UOUbZyI4LzRZbd2fUTItJYdj3zOmsZuAWcRMMw2gle5z2Kqvl_4YmNR6CshJlwQDdYnwLqs1X66qPjKEWmzhmO73z_vSLk1zz9ItWnn3_lcIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شایعاتی مبنی بر مذاکرات پرسپولیس با رامین رضاییان وجود دارد اما مدیران پرسپولیس به خوبی می‌دانند اگر رقم درخواستی رضاییان را به او بدهند، ممکن است جو به نفع رضاییان نباشد. قرارداد کنعانی‌زادگان، علیپور و پیام نیازمند در لیگ بیست‌وششم به اتمام می‌رسد و قاعدتا این بازیکنان با رقمی کمتر از قرارداد رامین رضاییان حاضر به تمدید نمی‌شوند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/137599" target="_blank">📅 22:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137598">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
#فوری
❌
مدیران باشگاه نساجی تصمیم گرفتند حداقل تا نیم فصل دانیال ایری و کسری طاهری را نگه دارند، بدین ترتيب حضور این دو بازیکن فعلا در پرسپولیس منتفی شد.
✍️
آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/137598" target="_blank">📅 22:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137597">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✔️
✔️
برای چهارمین بار متوالی ترکیب پرسپولیس لو نرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/SorkhTimes/137597" target="_blank">📅 22:33 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137596">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
❌
دقت کردید ترکیب لو نمیره؟!
👍
❌
پ.ن امروز بازی داشتیم هیچ ترکیبی نیومد بیرون
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/SorkhTimes/137596" target="_blank">📅 22:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137595">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NikZ_47UvSj3LrZwPLh9aX1fWvLcucNGcN_imWxr-T7rSkZB2_YPZ9gOe78p-8PDPnQOdjhfiVB9EbwHAz4RI3ZUhpo43YFGYjbRhXDu3-w_U3e32T0UtD3iILgjiJVHsCahA6H8cVQLdaaXX2f1kfymqdGQgH5RhwqVf3t-1yjP11QbuNnzxgk-5oMy4rPCSI4JRwbl905icjiOgKWbRWAhOFKDcy3mcu1cNwrsTGRNBMPgUCEQORmb41ExlHh1-jwICFUfPHKs1jj8ZT-amjS1c-G3RyUJ6VJFP71goxvZV_8nLyLRh184PLQFnORv-75iahT5f7gc_q0bHvP7pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
⚽️
🤍
فوووووری از فوتبالی: درحالی که فولاد به شدت دنبال رامین رضاییانه و به توافقاتی هم رسیده، ایجنت و فرستندگان این بازیکن به شدت دارن با پرسپولیس مذاکره می‌کنن و احتمال بازگشت رامین به پرسپولیس وجود داره و تنها مشکل مدیران پرسپولیس رقم درخواستیه این بازیکنه و اگه رامین تخفیف بده به پرسپولیس برمی‌گرده
🚨
🚨
🚨
🚨
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/SorkhTimes/137595" target="_blank">📅 22:27 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137594">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
❌
❌
طبق استعلام از فیفا، از نظر قانونی مشکلی برای جذب ایری وجود نداره.قبلاً به‌خاطر گرون بودن رضایتنامه توافق نکرده بودن، ولی الان پرسپولیس امیدوارِ بتونه نساجی رو راضی کنه.
🔴
فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/137594" target="_blank">📅 22:26 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137593">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
تارتار جاسوس را پیدا کرد؟
👍
شنیده میشود تارتار تعمدا چند ترکیب را در بازی های دوستانه در اختیار چند نفر میگذارد و مشخص میشود چه کسی ترکیب را به برخی کانال ها میدهد. باید دید در شروع لیگ باز هم ترکیب پرسپولیس به کانال ها میرسد یا تارتار بعد از هشت سال مانع…</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/137593" target="_blank">📅 21:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137592">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
❌
فرشید حقیری: محسن خلیلی رفته به یه بازیکن ایرانی سوئدی که تو لیگ 2 اتریش توپ میزنه پیشنهاد داده
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/SorkhTimes/137592" target="_blank">📅 21:37 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137591">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🗣
فارس : دانیال ایری هیچ مشکل قانونی نداره و استعلامش اومده مشکلی نداشته و مذاکرات پرسپولیس با نساجی آغاز شده
💬
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/137591" target="_blank">📅 21:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137590">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فوووری از خبرگزاری مهر
❌
❌
نساجی در انتظار دریافت مبلغ تا رضایت نامه ایری صادر کنه ؛ دانیال ایری در آستانه سرخ پوش شدن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/137590" target="_blank">📅 21:29 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137589">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/haCTK9o-hfOkIHsJAPRyBqPokwb3eYFXPbzKBqlVMZtbVJf7gPWHvwNJLyNa3hFc2MaDL_HOUEPT7A9htVBrd3MbVS4JIscWZBFScpW3p4w5PiCiZjljuDH7jSHWIVpxH28qJMEVLByxmdicaS2rtdykgcgNQs4eUTzvUx1IGV5-iMYhysaVMaBt--xH3_nLZYpSRwk9WmJswKBHOBUHg4PlSzqAOS2YITS2arYhwrd3ql8x9d90x4bAc910B-ELR5RlpBw5N42jOncneyOU3jLoM0wF9me12ebSk_zs2aXsnEEsbWlTfgOfvpNwATWfWY-RpmxQQZDTq2gOOvpWLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
✔️
#رسمی
؛ کوروش اژدهاکش هافبک19 ساله آلمینیوم با قراردادی پنج‌ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/137589" target="_blank">📅 21:18 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137588">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sz3TEhSzYuxJn6MNqmOC1bQQMDB9e93Wygg9eHteQoOECS4YJS-2_RoDhlnTGGPzHW0ZDEvilJMCs3ZjYCC3F6UF8BT7qtFCBRxiz1392SJrHo0b6apCZoyvQ8ZB3cXc2Sh374FW_enekiow_LHR_36Cd3q0cZXYT2MVPTK3y6e48-5tgwOIjPwFW9z5zW9Xd1aJMlzsGcx3hI_hzZO6yJuEvUy-_erpLQDtlyahm7cTlcwGykQQK640PG-ZW6BHRtMnnCp6wf1-DplXgXx98N0YAUmhtuquOiHDbohoZfYDH2RK9esDkbiGVfaueOPHX4AwtwTRac2lIGLM1gvFMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
✔️
#
رسمی
؛
امیرحسین طاهری مدافع22 ساله نیروی زمینی با قراردادی 5 ‌ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/137588" target="_blank">📅 21:17 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137587">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRBk75EI4vPJNYgUR_jEh-zmdpqwdil6apwuQxG2hZLzRyrpDP_6u57uWy5vKMT7vem7qTrOPf_7UByjBjKG8ORFvXeln4Y1ArlGIYDJLam1BGzL_TohFLhXmf7MgHjEfksMYfZbYjCZUPyxNkjDdmOFN7HMQ7VNz6SMAUYmJEnJ1Qz0kYGKe3ybv9Uo1uawGdWJOXeXsvtDsA5mbJ8xcuac0l8NcaTuHkifV-yDPT9eGAiivcvFkRh127k2fH4F_5Qxb7SPyqzxVcYbSmggIGKJudhdK9I7ljOPU5DdaH9klMOKmanP6MQBkuV343NmAUCykybvu-se9m87s59gOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
فقط تا پایان امشب برای بونوس ویژه Egypt Power x1000 فرصت دارید!
💰
با حداقل ۱ میلیون تومان واریز، فرصت دریافت ۱۵ فری اسپین رایگان بازی Egypt Power x1000 رو دارید.
📌
نحوه دریافت بونوس:
👇
1️⃣
واریز حساب حداقل ۱ میلیون تومان.
2️⃣
نوتیفیکیشن بونوس داخل حساب کاربری نمایش داده می‌شود.
3️⃣
از همان نوتیفیکیشن وارد بازی شوید و اسپین‌های رایگان را استفاده کنید.
🔗
آدرس ورود به سایت اسپورت‌نود:
👇
🔵
sportn5b2.com
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/137587" target="_blank">📅 20:39 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137586">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
❌
❌
دستیار خارجی فعلاً منتفی شد
🔴
مهدی تارتار خواستار اضافه شدن یک مربی خارجی به کادر فنی پرسپولیس شده بود، اما مدیران باشگاه با گزینه‌های مدنظر به توافق نرسیدند.
🔴
در نتیجه، جذب دستیار خارجی در مقطع فعلی منتفی شده و تارتار فعلاً با همین کادر به کارش ادامه…</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/137586" target="_blank">📅 20:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137585">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
ایری خیلی به پرسپولیس نزدیک شده؛ تارتار اصرار به جذبش داره و پرسپولیس هم در حال مذاکره با نساجیه. اگه توافق مالی نهایی بشه، ایری سرخپوش می‌شه.
❌
مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/137585" target="_blank">📅 20:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137584">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/137584" target="_blank">📅 19:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137583">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qH5_9evfZjLnKtnX64jt4VlxVTSCZgIqQ6XSwjSvFRKfaaPf814uFDLtQ4_9eRIRaSCNZ6GytZycPOlrjTBxFTDPN-rDRsUjL1XFfLRaUg7rG6vbbwwCoqsXBNnmGd8TcW-c6EwIxcuFS_He1ZCVdk-khE9Vd0hT34n5iTSPEamCDqne-Ynz6R_vlpMTpraj_EmQ94V-FTcL_L7ID88aUqgfUpiKy9VIIvHFkNNPHMV4ibLjQ7dwinrPRqLFnbbHoDGlCCVocd4Kno9z5piaS05RymaLLeXmj46BTFfkrLdRRRYO6B50C5kuEFCwo41lkZBkJRg4AVj0WJ1PTgafng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رسمی؛ رضا شکاری به پیکان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/137583" target="_blank">📅 19:37 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137582">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
🔴
شنبه بازی دوستانه داریم،پرسپولیس و آلومینیوم  قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/137582" target="_blank">📅 19:29 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137581">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7NcfwZA_U8rM9hk1EYzF6C9w74bMvQ4ZHchAQ8ZxTxY10ZLlUQ2pVANN1kpdhuc1sq_rjcLHrYl40pShDrRAhutlNB2FxawD4066pPAmViY-Yh2oxkZQh37MHM3wMfpBnChzfFKVzA81YyeNcKvEvsEhNQTgVVMr_-vkR2Y4lfnok3QjASfHjKyAzOjeC8KEJz16IK6YpmuVh5Y-aLea6bp2I_yiTx74TeQx0k74-173xM5W3Kw4JwFrVf7Kn3vPBB_055PdmUxIo3yZvIPABYuGJN4TQ6QG7A6NqBolXuo9Y-9mPkbEHnXBJhQQbbJbGh32FzlCJLxkee6zuQBuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
افشاگری‌عجیب فرهیختگان: موسی جنپو فصل‌گذشته به ازای هرماه حدود ۱۴۰ هزار یورو از  کیسه دستمزد می‌گرفته که در تیم جدیدش در یونان این رقم به ۲۰ هزار یورو در ماه میرسه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/137581" target="_blank">📅 16:41 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137580">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
فووووووووری / قدوسی
❌
قربانی به تیم های خواهانش اعلام کرده همان پولی که تو امارات میگیره باید بهش پرداخت شه  ( یک میلیون دلار + پول رضایت نامه! )
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/137580" target="_blank">📅 16:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137579">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
فووووووووری / قدوسی
❌
قربانی به تیم های خواهانش اعلام کرده همان پولی که تو امارات میگیره باید بهش پرداخت شه  ( یک میلیون دلار + پول رضایت نامه! )
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/137579" target="_blank">📅 16:13 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137578">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">⚡️
⚡️
⚡️
محمد برزگر:
⚡️
⚡️
یکی از الگوهای خوب اوسمار، پذیرش انتقادات است. او خودش هم قبول دارد که پرسپولیس زیبا بازی نمی‌کند. این یک واقعیت است و در کوتاه‌مدت هم نمی‌توان انتظار فوتبال چشم‌نواز داشت. مهم این است که سرمربی این موضوع را می‌داند و پنهانش نمی‌کند…</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/137578" target="_blank">📅 15:35 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137577">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPulseGate</strong></div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
یک ماهه
25 گیگ 220T کاربر نامحدود
30 گیگ 280T کاربر نامحدود
35 گیگ 320T کاربر نامحدود
55 گیگ 420T کاربر نامحدود
100 گیگ 600T کاربر نامحدود
دوماهه
50 گیگ
380T تومن کاربر نامحدود
70 گیگ 450T تومن کاربر نامحدود
150 گیگ 700T تومن کاربر نامحدود
200 گیگ 750T تومن کاربر نامحدود
سه ماهه:
120 گیگ 680T تومن کاربر نامحدود
160 گیگ 730T تومن کاربر نامحدود
230 گیگ 800T تومن کاربر نامحدود
320 گیگ 950T تومن کاربر نامحدود
400 گیگ 1.1T تومن کاربر نامحدود
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/137577" target="_blank">📅 15:27 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137576">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
❌
با اعلام رسمی سازمان لیگ، پرسپولیس و استقلال در ورزشگاه شهر قدس از حریفان میزبانی می‌کنند.
❌
می گویند بازی ها با تماشاگر برگزار می شود اما نمی دانیم چرا خوش بین نیستیم///قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/137576" target="_blank">📅 15:26 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137575">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🏟
برگزاری دیدارهای پرسپولیس و استقلال در ورزشگاه شهدای شهر قدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/137575" target="_blank">📅 15:21 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137574">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rg0IXuBH22uxDyT4mDnpKuMZyH-zHeZbKpSh7e3e_cqR_nRV2IFKpgqyCq5iC3L_98gIYGdc8QdJfvdAJ8bymhfSCevwo1wp2eggKxFMQVD62CA1bNwVdQlvmr1l7Ia7AbmLOy0YgImSX_GHUsx1Rj3Nnn14kfbKARmYnTfJARaHeyik_weIiPKpUvV7PjOGIkA3pF8S7z_Rfg8RLXB4-DiZ_xUMao3VCo8orAnPBXwHWcEuuzo4vOPTP2ldzf3xdl__RCloLyYlaXgK3Rf5lGYDEfgOBvZhmopLp5zQuU14Q7TEmbyjcYUamfFq-DTSeDZcO-jk0VAxagN_yt2bcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏟
برگزاری دیدارهای پرسپولیس و استقلال در ورزشگاه شهدای شهر قدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/137574" target="_blank">📅 15:13 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137573">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
فووووووووری / قدوسی
❌
قربانی به تیم های خواهانش اعلام کرده همان پولی که تو امارات میگیره باید بهش پرداخت شه  ( یک میلیون دلار + پول رضایت نامه! )
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/137573" target="_blank">📅 15:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137572">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇦🇷
💀
گریه‌های مسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/137572" target="_blank">📅 15:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137571">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a058da26.mp4?token=Dyi8y1BsSixeOBZsgbWxFkieoM7XSc3lTO4u5t3qIHef7rZWMpxV09VHbsvUoDW5toxnoKi583s1fw_4LKbYxWpht0LGIRYNTc-yk6feOqG8NfNWsEg_28BNGiZOvWO5uPwXmQ-olyJwRurwDBHNZo_nRKLjOdcIFWYTHiD4SU-f0r4-EuFiTVW5fnTwMtXchNRN4_kb9kdh8EUx1ZVcjAWrZMLyYbXu1477-MUHYHLvnIJBgsErqQAAq35n7qrLnneCaMqyZwkykLDEfBB1qTpY-RqCTAgfmFVKVaYwu2OK3k7SmWztMVrg8ozESyo5DvTRw7VtHPKMuudQg6re3CpevRgAgNGXKicF511tCXAJ61mgfD1jLrbNNcRw7HJXSUfSqpN_zcEG6mMsd2casnHHnl3_jDFbyqpLIlZxkiZpfj_Hx7yDL0iA2tRABbbABNa_ZZLQjOnuqgrsGP-o4AOQpxoTBGRWu0yWUo4XIwMEUlTUM1JXYiZydNsrpUDn0PLWJokE-OVj06g2mx3DKnqCXRxZDelCExN8q68Lrh6uVmD1dai0CUv98njbPZXLwbqNG94itMFL9oD_wiCltRuCbreaIfQmZ6m0WIvNN6xmN1Dwrp1IZAOsNiynzXSSx67161ZwIJRuSmfS8a_GFSp3oRhTfsjZgJaywpv3jWs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a058da26.mp4?token=Dyi8y1BsSixeOBZsgbWxFkieoM7XSc3lTO4u5t3qIHef7rZWMpxV09VHbsvUoDW5toxnoKi583s1fw_4LKbYxWpht0LGIRYNTc-yk6feOqG8NfNWsEg_28BNGiZOvWO5uPwXmQ-olyJwRurwDBHNZo_nRKLjOdcIFWYTHiD4SU-f0r4-EuFiTVW5fnTwMtXchNRN4_kb9kdh8EUx1ZVcjAWrZMLyYbXu1477-MUHYHLvnIJBgsErqQAAq35n7qrLnneCaMqyZwkykLDEfBB1qTpY-RqCTAgfmFVKVaYwu2OK3k7SmWztMVrg8ozESyo5DvTRw7VtHPKMuudQg6re3CpevRgAgNGXKicF511tCXAJ61mgfD1jLrbNNcRw7HJXSUfSqpN_zcEG6mMsd2casnHHnl3_jDFbyqpLIlZxkiZpfj_Hx7yDL0iA2tRABbbABNa_ZZLQjOnuqgrsGP-o4AOQpxoTBGRWu0yWUo4XIwMEUlTUM1JXYiZydNsrpUDn0PLWJokE-OVj06g2mx3DKnqCXRxZDelCExN8q68Lrh6uVmD1dai0CUv98njbPZXLwbqNG94itMFL9oD_wiCltRuCbreaIfQmZ6m0WIvNN6xmN1Dwrp1IZAOsNiynzXSSx67161ZwIJRuSmfS8a_GFSp3oRhTfsjZgJaywpv3jWs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
@Wincobet_bot</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/SorkhTimes/137571" target="_blank">📅 14:13 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137570">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
رسانه های تبریزی از نزدیک شدن پرسپولیس به عقد قرارداد به محمد قربانی نسبت به تراکتور خبر میدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/SorkhTimes/137570" target="_blank">📅 13:19 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137569">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">⚫️
⚫️
فرهیختگان :تارتار هیچ نظری روی دنیل گرا نداره و گفته باید جدا بشه ولی محسن خلیلی مانع جدایی دنیل گرا هستش تا این لحظه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/SorkhTimes/137569" target="_blank">📅 13:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137568">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری
🚨
قدوسی: حضور دانیال ایری، ابوالفضل رزاق پور و کسری طاهری و حسین نژاد در پرسپولیس منتفی شد
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/SorkhTimes/137568" target="_blank">📅 13:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137567">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔄
🔄
🔄
علیرضا بیرانوند:
🔴
🔴
فوتبال بدون تماشاگر عددی نیست. آقایون تصمیم‌ساز خودی نشون بدید! فقط فوتبال می‌تونه نشاط به جامعه اضافه کنه. بازی‌ها رو با تماشاگر کنید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/SorkhTimes/137567" target="_blank">📅 13:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137566">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
پرسپولیس و نساجی برای انتقال ایری به توافق اولیه رسیدند / مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/SorkhTimes/137566" target="_blank">📅 10:46 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137565">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🗣
🗣
🗣
باشگاه پرسپولیس بعد از پاسخ منفی باشگاه ملوان بابت رضایت نامه افسرده بار دیگر جذب ایری را پیگیری کرده است.اینکه بعد از سه هفته طلسم جذب ایری می شکند یا نه فعلا مشخص نیست
✍
قرمزانلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/SorkhTimes/137565" target="_blank">📅 10:44 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137564">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🔹
🔹
استعلام فیفا مثبت شد؛ مشکل قانونی وجود ندارد!
🚨
🚨
طبق آخرین پیگیری‌ها، استعلام فیفا به باشگاه پرسپولیس رسیده و انتقال بازیکن موردنظر مشکلی از نظر قانونی ندارد.
❌
تنها مانع باقی‌مانده، رضایت باشگاه نساجی برای جدایی او بدون حضور بازیکن دیگر در این انتقال…</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/SorkhTimes/137564" target="_blank">📅 10:43 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137563">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
شرط جدایی الکسیس گندوز از پرسپولیس پاداش جام جهانی بود که با خط خوردنش از لیست نهایی تیم ملی الجزایر اون پولم ظاهرا سرش گرده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/SorkhTimes/137563" target="_blank">📅 10:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137562">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❌
❌
شهاب زندی مدیرعامل نساجی:  با استقلال درحال مذاکره‌ایم، با توجه به بسته بودن پنجره شون اگه بر سر مباحث مالی به توافق برسیم این دو بازیکن آینده‌دار نیم‌فصل راهی استقلال میشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/SorkhTimes/137562" target="_blank">📅 09:44 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137561">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
از بین پرسپولیس و تراکتور هرکدوم زودتر با الوحده به توافق برسن قربانی میره اونجا/ورزش‌سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/SorkhTimes/137561" target="_blank">📅 08:48 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137560">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPqdIF7_hFx0Ywq5xkkohDhcJnf5t-J0BFWeJ_LOMPiBMHfi1LUX2Vf0_7EQxrOhFb3rWGLeyWf7AttjfD2u8FuTIvHcZ-rwCAUiT1G3PU0PKsRiMiIjKnbuJN0yIiccqSuWuaBs4nlm2ke08NZt7Xxzg-fhgp9Dt0aKdfi3KUfT-du7IlQuodpuyvQPXCY5Q4bo1Js8Qgfhky2ovXBMgbWtQzhBWsNLYN62TIpnpZnGM96E_vyoOn1vPfHjPAMwoARLGwMRRS4YtX7jQgnZDei6y6eIvA_E3jCy2WIhRsfVdXQo3fNqkHe7nbKOgYmGijq2c6KgGzaIePXvQQRyzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/SorkhTimes/137560" target="_blank">📅 08:37 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137559">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4988f1ce4f.mp4?token=XFF-BrQ_eZ1d3-7WKp-HNlVlESv3s41tTGRKi2lQSDvSZuw4Gmhr_Zzgj_3AUp293xX1J7GHh1ryZGqom2WgxwHJzVcsXLAp63Zg2nlsb4L-arspYYgJuTCni46m_VElfnBYM_UBr-zZqd7pbp55goLpvDxUYngfbtNe1lMohbdNXJfWI7Up_5qs6I7KcT4Nko4dkKd_DYS9d2MzcCjT97StINjeaOCYNytfUSBhw1uiWOzGl8rh_6McWGBEtsougYLq7jB7M6LtPXcs3fVehPXTPZChJLYtRMb3qw9dKn9-WyePAC9QI1toICDdUtZJc-sI10_-WNbol64EqkVa0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4988f1ce4f.mp4?token=XFF-BrQ_eZ1d3-7WKp-HNlVlESv3s41tTGRKi2lQSDvSZuw4Gmhr_Zzgj_3AUp293xX1J7GHh1ryZGqom2WgxwHJzVcsXLAp63Zg2nlsb4L-arspYYgJuTCni46m_VElfnBYM_UBr-zZqd7pbp55goLpvDxUYngfbtNe1lMohbdNXJfWI7Up_5qs6I7KcT4Nko4dkKd_DYS9d2MzcCjT97StINjeaOCYNytfUSBhw1uiWOzGl8rh_6McWGBEtsougYLq7jB7M6LtPXcs3fVehPXTPZChJLYtRMb3qw9dKn9-WyePAC9QI1toICDdUtZJc-sI10_-WNbol64EqkVa0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎁
فقط تا پایان فردا برای بونوس ویژه Egypt Power x1000 فرصت دارید!
💰
تا پایان ۱۷ مرداد با هربار واریز حداقل ۱ میلیون تومان، ۱۵ گردش کازینو به ارزش ۱,۵۰۰،۰۰۰ تومان به صورت رایگان دریافت کنید.
🔹
پس از واریز، بونوس از طریق نوتیفیکیشن داخل حساب کاربری نمایش داده می‌شود و از همان بخش می‌توانید وارد بازی شوید؛ نیازی به جستجوی نام بازی نیست.
🔗
آدرس ورود به سایتاسپورت‌نود:
👇
🔵
sportn5b2.com
🔵
sportn5b2.com
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/SorkhTimes/137559" target="_blank">📅 01:21 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137558">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0556971c1.mp4?token=CPjD5KiTPFouHbIMvqbEFG_yJ9VhHy2QWGB59yuATDpb3GapX9hgQHUfQrvYPcVPIpt8t6nYITtC2FDtVjhS0w_PGIjsjB54aQrHCn5a1Zqg56PwG5fqjI9zTgbfwgE8kkz4EoTY-UTYCvJYrxE1GOEISqwvpLJGcKPvqRLaEhrYWbrhP0XAnCLTio5Eo7fIkvaAWnslg3sTDF1Xn86xLUOK8C642EG21RkcwFnAZUxSyfBUFeA1QLjHADTznAO_1Erv72QO3eihJ7SzlWMGfG3wzM4JI_hwP_DvVPDP5cWfIs-0GFdAWnn96aDxqtS3ovasToitsCrRhKf-Vi0DKBs04tnaeZkzOu1IjX3Wg7YiikWH4CvbtNw82mhpFiw7W-vBqpY8jsePTbHD4iQb9hae3b1NBqDwPGIq5c0xNz2KX1yXrWcSeAHxLILMjgMM_Qys3LvdSv6F_3YOTa7DYmo4B2PE2R1m_Bn3AB594X9oFqMuOi1y-TupXYYrvS_7cKPxtVNr6HEqDINtiLPdjIAZnBDYt4UbN0G2VQkmd8c1v9gZ8ZPZvwowBng83SXyrNew4HqvfJGFVwPA3rRzmtbbdE9LPMY_WG08lOOvCm8e9bBJqDAEpDJYa4MzFAhIwu4om6qx4W7wQO3xJpG0GS6-Jj41euvOgcv2pboSX7U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0556971c1.mp4?token=CPjD5KiTPFouHbIMvqbEFG_yJ9VhHy2QWGB59yuATDpb3GapX9hgQHUfQrvYPcVPIpt8t6nYITtC2FDtVjhS0w_PGIjsjB54aQrHCn5a1Zqg56PwG5fqjI9zTgbfwgE8kkz4EoTY-UTYCvJYrxE1GOEISqwvpLJGcKPvqRLaEhrYWbrhP0XAnCLTio5Eo7fIkvaAWnslg3sTDF1Xn86xLUOK8C642EG21RkcwFnAZUxSyfBUFeA1QLjHADTznAO_1Erv72QO3eihJ7SzlWMGfG3wzM4JI_hwP_DvVPDP5cWfIs-0GFdAWnn96aDxqtS3ovasToitsCrRhKf-Vi0DKBs04tnaeZkzOu1IjX3Wg7YiikWH4CvbtNw82mhpFiw7W-vBqpY8jsePTbHD4iQb9hae3b1NBqDwPGIq5c0xNz2KX1yXrWcSeAHxLILMjgMM_Qys3LvdSv6F_3YOTa7DYmo4B2PE2R1m_Bn3AB594X9oFqMuOi1y-TupXYYrvS_7cKPxtVNr6HEqDINtiLPdjIAZnBDYt4UbN0G2VQkmd8c1v9gZ8ZPZvwowBng83SXyrNew4HqvfJGFVwPA3rRzmtbbdE9LPMY_WG08lOOvCm8e9bBJqDAEpDJYa4MzFAhIwu4om6qx4W7wQO3xJpG0GS6-Jj41euvOgcv2pboSX7U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هایلایت طاهری مدافع و بازیکن جدید تیم با قد و هیکل مناسب
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/SorkhTimes/137558" target="_blank">📅 00:46 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137557">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🔹
🔹
استعلام فیفا مثبت شد؛ مشکل قانونی وجود ندارد!
🚨
🚨
طبق آخرین پیگیری‌ها، استعلام فیفا به باشگاه پرسپولیس رسیده و انتقال بازیکن موردنظر مشکلی از نظر قانونی ندارد.
❌
تنها مانع باقی‌مانده، رضایت باشگاه نساجی برای جدایی او بدون حضور بازیکن دیگر در این انتقال…</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/SorkhTimes/137557" target="_blank">📅 00:39 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137556">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_ST8GaVUKt4QdxiUBsuKZeZrTpmMFncj4xJFey2sZVQrGnbjDPnzQQh7Z3aG8Ne9Nrs2_l8TbLC3OW3d6nl3EzSFEjyhSueg4tqtnTSeZKiNSEsNqcC10a_sdIHwCT7DLZAYLslD871motzHQB-CrpuucgwJpp4dz-by4gK0mEnLOWTwbnTYdLdbo569zfhnMkmO5OXW13k7QiV_m64Jx2VbpBRImLCIew2He-wANUtMNTmUee8FdZbQhfgSp6tw1PkO8oYrEo-ucsk8twYDX1gR41FbrSGXvMR4pkaPupiukPThq_s6Hzb2kOT7raa-oZks_C1bP2mgwQWyzckPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔹
🔹
استعلام فیفا مثبت شد؛ مشکل قانونی وجود ندارد!
🚨
🚨
طبق آخرین پیگیری‌ها، استعلام فیفا به باشگاه پرسپولیس رسیده و انتقال بازیکن موردنظر مشکلی از نظر قانونی ندارد.
❌
تنها مانع باقی‌مانده، رضایت باشگاه نساجی برای جدایی او بدون حضور بازیکن دیگر در این انتقال است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/SorkhTimes/137556" target="_blank">📅 00:33 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137555">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔜
🤩
سکوت حدادی معنای خاصی دارد!
منتظر خبر خاص یکشنبه باشید
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/SorkhTimes/137555" target="_blank">📅 00:28 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137554">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری
🚨
قدوسی: حضور دانیال ایری، ابوالفضل رزاق پور و کسری طاهری و حسین نژاد در پرسپولیس منتفی شد
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/SorkhTimes/137554" target="_blank">📅 00:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137553">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
قدوسی: پرسپولیس بجز خرید های اصلیش قراره دو سه تا بازیکن جوون هم جذب کنه که یکیش اژدها کشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/SorkhTimes/137553" target="_blank">📅 23:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137552">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
قدوسی: پرسپولیس بجز خرید های اصلیش قراره دو سه تا بازیکن جوون هم جذب کنه که یکیش اژدها کشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/SorkhTimes/137552" target="_blank">📅 23:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137551">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
ورزش سه: اژدهاکش فردا با حضور در باشگاه پرسپولیس قرارداد پنج ساله خودش را امضا خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/SorkhTimes/137551" target="_blank">📅 23:46 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137550">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1051799a08.mp4?token=WlfWQQAvMyUCDUovdk0H7vadhczAhTqp3Hy97Jr0JbXCSzefxkjy0oWi3zh5l-Q-F-eRZt11BHtXt1XCwfBMoQO82XLzK626953nOA7pwcNHC7t05UN5bBflrgxhgJzItHvxlAs__73uN59SquXTHe1_xgylpt5Zxp5EDvdkf1ucNX5c9W8bcKZx0a-Y4vCFKZmRjeipV2kmUSqFjoPCzTk0F3gUc8j4NV5tE1kO17yNNZ-uaTsHBu4gtRu1pUNMVcimJP4SNCsQbgzwhrNXYTkvHDonB661B_EccAClybb5J6osrsiwuNjVwtXIT5buzDi7Ask4WjttaCxi-zLfQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1051799a08.mp4?token=WlfWQQAvMyUCDUovdk0H7vadhczAhTqp3Hy97Jr0JbXCSzefxkjy0oWi3zh5l-Q-F-eRZt11BHtXt1XCwfBMoQO82XLzK626953nOA7pwcNHC7t05UN5bBflrgxhgJzItHvxlAs__73uN59SquXTHe1_xgylpt5Zxp5EDvdkf1ucNX5c9W8bcKZx0a-Y4vCFKZmRjeipV2kmUSqFjoPCzTk0F3gUc8j4NV5tE1kO17yNNZ-uaTsHBu4gtRu1pUNMVcimJP4SNCsQbgzwhrNXYTkvHDonB661B_EccAClybb5J6osrsiwuNjVwtXIT5buzDi7Ask4WjttaCxi-zLfQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
تنها گلش سال گذشته به این شکل مقابل استقلال خوزستان به ثمر رسیده .
❌
پ.ن امیدوارم این جوونا که سهمیه لیگ برتری هم حساب نمیشن حداقل جواب بدن و بدرخشن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/SorkhTimes/137550" target="_blank">📅 23:41 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137549">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
کوروش اژدهاکش مهاجم 18 ساله آلومینیوم با قراردادی ۵ ساله به پرسپولیس پیوست./ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/137549" target="_blank">📅 23:39 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137548">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
❌
تسنیم:
😀
✔️
تیوی بیفوما پس از عملکرد درخشان در تمرینات پرسپولیس در این تیم ماندنی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/137548" target="_blank">📅 23:37 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137547">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇷
🇮🇷
عکس یادگاری یحیی گل‌محمدی و علیرضا منصوریان در حاشیه دیدار دوستانه دهوک و الطلبه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/137547" target="_blank">📅 23:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137546">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNtxT18XACAqoXRAmWEFA0q6JpkomTW-pw4cwVk0hnOqiDmLd3mhBl25IN4nesFN10UMVLnMwUdIoY2SAl8GbK7Qxucouz0e_h-RX5NVc8EZmsl95QFUtn6-9_Zop7Jp7Jn_isL9Cy2Ir5KV2uGXLsSPUTtyonYHmTbUAptFuVFKd_uwQo7VPs5FQtiwiFapJ22_aHqGpl6or78TX4fLkCUab2gFov86bwwMp39sk9Gtjh-Rhjw7Tu4q0i8bF9QctxbbgbjQyafTzRNkSq-B6Wai9-7g6ZfFOTObSw00VvwjBpMVO-xmfW1HOXND8qISGhjXkMvocwSoBDn7as57VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇷
عکس یادگاری یحیی گل‌محمدی و علیرضا منصوریان در حاشیه دیدار دوستانه دهوک و الطلبه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/137546" target="_blank">📅 23:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137545">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
اضافه شدن بازیکنان امید پرسپولیس به تمرینات بزرگسالان
🔻
🔻
با اعلام باشگاه پرسپولیس، در ادامه سیاست‌های باشگاه پرسپولیس در مسیر جوان‌گرایی و توجه ویژه به استعدادهای تیم‌های پایه، با درخواست پیمان حدادی، بازیکنان تیم‌های پایه که دارای قرارداد حرفه‌ای با باشگاه…</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/137545" target="_blank">📅 23:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137544">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🏅
فرهیختگان: ماجرای محمد قربانی داره شبیه پرونده محبی می‌شه، تراکتور منتظره قربانی بازیکن آزاد بشه و رایگان جذبش کنه، اما پرسپولیس می‌خواد با پرداخت رضایت‌نامه به الوحده، این انتقال رو نهایی و دوباره هایجک کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/137544" target="_blank">📅 22:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137543">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
تارتار قراره بخاطر کمبود بازیکن از ابرقویی در هافبک دفاعی و از پورعلی در دفاع میانی هم استفاده کنه و اونا رو تو این پستا تست کنه /فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/137543" target="_blank">📅 22:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137542">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔄
🔄
🔄
وزیر خزانه داری آمریکا: فکر میکنم امروز یا فردا، شاهد توافق باشیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/137542" target="_blank">📅 22:12 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137541">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgCZ5-u2rPpZE6YBdxPLLTHR_FIrLIWJDOgsqLbtmbqIeYgUjeuyOsh_FNoTPuaRxumu8gyAf8qIdPKADXWOtVBJDqY4a-Y1rx4VRVVpnoLKHL67GAhnlDyVRGDqSxIE_5-0lJCVeHnYP7YuvwjO5Dtn-YUpzRaQfL9Amx_2muKWiUE8X94Zw7l1reLgNDoJKrUNRZ9Fo-fb52mFFjUgLgSXUuAjptgN8dzhNNIQe5tYXUD6Q2R1YoRUoIZ61H1fl84nj3ukgMLJKCYjQSCWppRvsWIXpOenIVaz12oM44UUSzBDbmlBxfJnwGLAss1su0sjG3ftdrFa53cMFcgZvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
⚽
تصاویری از تمرین امروز تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/137541" target="_blank">📅 22:09 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137540">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
❌
❌
ادموند اختر از پیشکسوت های کیسه: اگه رامین رضاییان برگرده پرسپولیس، بی شعوری خودشو نشون داده !!!
😅
😅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/137540" target="_blank">📅 21:36 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137539">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❗️
❗️
قلی زاده: فکر نمیکنم تو ایران برای تیمی جز پرسپولیس بازی کنم ؛ چون قلبا پرسپولیسیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/137539" target="_blank">📅 21:28 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137538">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری
🚨
قدوسی: حضور دانیال ایری، ابوالفضل رزاق پور و کسری طاهری و حسین نژاد در پرسپولیس منتفی شد
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/137538" target="_blank">📅 21:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137537">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
❌
❌
❌
🚨
مازیار زارع با حضور امیررضا افسرده در پرسپولیس مخالفت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/137537" target="_blank">📅 21:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137536">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‼️
‼️
نمودار ترسناک و فوق العاده غم انگیز... کمترین میزان ازدواج در ۳۰سال اخیر  و کمترین میزان زاد و ولد در ۷۰سال اخیر! سلامی تلخ به پیری جمعیت باید کرد... از هرایرانی بپرسید علت این فاجعه را چشم بسته عاملش را "اقتصاد فاجعه بار" خواهند نامید.
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/SorkhTimes/137536" target="_blank">📅 20:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137535">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y28YsKzUni6l4KtBlvesewIqwUAT-LCfq8WuETzUyd-PIKs-WG2BWyn1Zx1oyMaOVtl0cyS5X48CM2h50f3aPPEFcnp62reP7zKijY37jxfOrpxbeOvzPbzcNaYs7p2dg7SSVQU2PJTjaA32zeXcpYdv-hKozIaiFuMMr4fWDfjamU-pE9ztl_wiGPlu1pA3z-0JsgBw_sfCdSOEODVIR_3rxevyp0SRgHt48PXKZZO8insmO5ACLN2kutaz9Vfuek84G-P1KOJ_8Ad82T64hfCrzLS32GBa09vToTmJdbGOiyWGn5NPq-8G7koXlbSzO3f2MW0Utmsx4g149Ufpfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
صلاح : کاش زبون ترکی بلد بودم. طرفدارای ترابزون خوش‌آمدگویی ویژه ای به من نشون دادن، من اومدم که براتون جام ببرم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/137535" target="_blank">📅 20:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137534">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehjGylmnzqwjQZKPCd4JxVOc07baePwB4kaSrZZYKrYPSyQwb3e1gK3vU9a7YUxYGfGLz70wfR-sTcIag5BXIxO2n-81OQSqzjt-cxQqElzPOsRyiqhaLUMFf--QZfXDQs_IH7vKaf8QczWTRjX4RoqwW6vu-jftMBki7wcszzkfA7OmmLcWuhEc3hJPHJNKm9K1DBymq833FJ4xZpK9dzEcQ0f98oZ-IC7cdQgtOaIYWPgH_sSR7H0wQ0N5Eq4tHPL5cikIxStDAyo6U6m1TwwIsuwZHvY0yzJTYO0RroED06mqlsOdzMQeLoq-_ormz3XDWGyvfVnE88Q2JCcmuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
فقط تا پایان فردا برای بونوس ویژه Egypt Power x1000 فرصت دارید!
💰
تا پایان ۱۷ مرداد با هربار واریز حداقل ۱ میلیون تومان، ۱۵ گردش کازینو به ارزش ۱,۵۰۰،۰۰۰ تومان به صورت رایگان دریافت کنید.
📌
نکات مهم این بونوس:
👇
▪
︎ ۱۵ اسپین رایگان ۱۰۰ هزار تومانی
▪
︎ ارزش اسمی بونوس: ۱,۵۰۰,۰۰۰ تومان
▪
︎ مبلغ فوق تضمین‌شده نیست و میزان برد به نتیجه چرخش اسپین‌ها بستگی دارد.
▪
︎ پس از پایان اسپین‌ها، برد نهایی بی‌قید و شرط به موجودی حساب شما اضافه می‌شود.
🔗
آدرس ورود به سایت
اسپورت‌نود:
👇
🔵
sportn5b2.com
🔵
sportn5b2.com
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/137534" target="_blank">📅 20:20 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137533">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
❌
امیر رضا افسرده: به پیشنهاد پرسپولیس جواب مثبت داده بودم ولی به خاطر روی گل ماه مازیار زارع در ملوان موندنی شدم و به پرسپولیس نمیرم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/137533" target="_blank">📅 19:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137532">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری
🚨
قدوسی: حضور دانیال ایری، ابوالفضل رزاق پور و کسری طاهری و حسین نژاد در پرسپولیس منتفی شد
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/137532" target="_blank">📅 19:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137531">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
❌
❌
ورزش سه: مهدی تارتار از روند نقل و انتقالات پرسپولیس راضی نیست و مدیران باشگاه پرسپولیس دارن لیست خرید شو روز به روز کوچیک تر میکنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/137531" target="_blank">📅 19:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137530">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
❌
❌
ورزش سه: مهدی تارتار از روند نقل و انتقالات پرسپولیس راضی نیست و مدیران باشگاه پرسپولیس دارن لیست خرید شو روز به روز کوچیک تر میکنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/137530" target="_blank">📅 19:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137529">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
🚨
تا این لحظه تارتار مخالف بازگشت رامین رضاییان به پرسپولیس است اما همچنان رایزنی و مشورت ها ادامه دارد.
📰
سپهر خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/137529" target="_blank">📅 19:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137528">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
❌
فارس: نساجی با جدایی و انتقال دانیال ایری مخالفت کرد و پرونده حضور ایری به پرسپولیس بسته شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/SorkhTimes/137528" target="_blank">📅 19:38 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137527">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">⁉️
⁉️
⁉️
فوووووری
⚠️
با اعلام رسول باختر کارشناس حقوقی مطابق قانون پوریا شهرآبادی خرید جدید‌ پرسپولیس سهیمه لیگ برتری محسوب نخواهد شد
⚠️
رسول باختر: بر اساس قوانین بازیکنان سهمیه جوانان (زیر 21 سال) جزو سهمیه لیگ برتر محاسبه نمی‌شوند. این سهمیه شامل متولدین…</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/SorkhTimes/137527" target="_blank">📅 17:55 · 16 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
