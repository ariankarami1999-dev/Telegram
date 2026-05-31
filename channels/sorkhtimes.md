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
<img src="https://cdn4.telesco.pe/file/Nm_OFAgh_sqvnJty80Nof3DOPXPhQK8O7xnsfjnWkf4HRdQfSs5jpdNjo_JJRbaPcsh1wjqSkfg6BSkQiJnx882f4d22jCKz95wnLU9fbJeagZ6ANWJONJygdjmy4yIcmWWP6Njq9EatnsgRQZ9-S_lMl4_v2xB4xor322gf_Lyfqo0uu5kUL3NV71RBN89xiDvELhrPEfDxbupftZPHesiUHkFv4l6_Q_qPxFUbhENGw5e4aSE86PZ3we0c5GUyknRzHIcQw8rFLNaBAjikrxQe_sD-RJAWfDJoetxRiubdofG2T1xJmAMuvJxqznRN2LQZTOoaerNp0V6VMiKC3A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.7K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 19:30:02</div>
<hr>

<div class="tg-post" id="msg-132542">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">فوری
⛔️
‼️
با مخالفت Afc, سپاهان مجوز نگرفت و از آسیا حذف شد
◻️
کنفدراسیون فوتبال آسیا به دلیل اینکه پنجره بارگذاری مدارک  باشگاه سپاهان بسته شده است، مدارک مجوز حرفه ای این تیم را نپذیرفت تا به این ترتیب این تیم از  حضور در لیگ قهرمانان آسیای فصل آینده حرف شود.
◻️
به این ترتیب حالا  یکی از تیم های گل گهر، چادرملو و  پرسپولیس طبق مدارکی که به ای افرسی ارسال کردند شانس حضور به جای سپاهان را دارند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/132542" target="_blank">📅 18:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132541">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGbQ1dCw7xb6knWD5hqkz0B-l6bFk-QAV_XlqSKrgsDMrZ2JtDmulhRDzPs93ydmBJmoJ1C3g3rZRvUMM381fWQ2qsCMhlG8AUg_BBzRQW014JtKJHGsEF4iSb0L5IuA4VFknWqw5TCma0aPcOxEl9XGP-QMGDAXS47NmEnMd9irDUYIC3BaoQw2zDqcCqmcioAtX-xWqvMrg3kB-DDp54lPs9PgpmUO-G4MCR66h4QhJ0rM0cE2LWVaWNDQnnp-_RheDG4FPmUDPE90O3cBqj7GFJVSFwRJcgtyoirNonXb58QfEPNnQic84wuALAF1GslMB-VTVKi263dNGzScFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سهیل صحرایی، مدافع جوان و آینده دار پرسپولیس، دیروز ۲۳ ساله شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/SorkhTimes/132541" target="_blank">📅 18:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132540">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔰
آف ویژه سرویس VIP
🔰
5 گیگ 150T
🔥
10 گیگ 300T
🔥
20 گیگ 400T
🔥
30 گیگ 500T
🔥
40 گیگ 600T
🔥
70 گیگ 900T
🔥
100 گیگ 1T
🔥
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال و مدت زمان نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/SorkhTimes/132540" target="_blank">📅 17:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132539">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
خبرگزاری تسنیم:
◻️
باشگاه پرسپولیس به دنبال جذب چند بازیکن جوان و ملی است تا میانگین سنی این تیم را برای فصل آینده به طور چشم‌گیری کاهش دهد.
◻️
بازیکنانی مانند سروش رفیعی، مرتضی پورعلی‌گنجی، میلاد سرلک، تیوی بیفوما و دنیل گرا از جمله بازیکنانی هستند که به احتمال زیاد فصل آینده در جمع سرخپوشان حضور نخواهند داشت.
◻️
مدیریت پرسپولیس از طریق چند واسطه پیام‌هایی را نیز به چند بازیکن جوان و لژیونر ارسال کرده تا شرایط آن‌ها را برای جذب بررسی کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/SorkhTimes/132539" target="_blank">📅 17:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132538">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❗️
🗣
حمید درخشان:
🔺
در حق پرسپولیس اجحاف شد؛ در ۸ بازی باقی مانده هر اتفاقی ممکن است رخ دهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/SorkhTimes/132538" target="_blank">📅 17:23 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132537">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0omLcDVIQnvnBH8Z6TvHyh71BKlostVcotOIOvbC9J3RjFjyXesELMrevSB4ei1fpzBnYUzvDaIxbmwtrxEjGunCgP4vCVltAKc2gZ3HHFArHN2sBHzQCcqEQlgxMquUBuzyMtpikSeBmXO3GlUy9-Eb-yFj_lNAUqrEzGp_IRRU8KfPC7uPINkjxmi2tjyv5OXPnawQccnFConEmyLsUsFvCqhrTGzQwMilenRGJi6kAq9sSCkZpWePcypFyedJrzLprQ9t2UrcqPSz0n-GF6GKyCAJWZVmhlWVGzntpUYnbteVIm559wNgUNhyHeNTwUHOvmcKqw70lVbX8FXOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قول بزرگ وکیل علیرضا بیرانوند به تاجرنیا رئیس هیات مدیره باشگاه استقلال: پنجره باشگاه‌ تون باز شود بیرو بعد از جام‌جهانی با تیم استقلال سه ساله خواهد بست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/SorkhTimes/132537" target="_blank">📅 17:11 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132536">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
خوردبین: تیمی که در ایران مجوز نگرفته چرا به آسیا معرفی می شود؟
🔻
آرزو به دل ماندیم متولیان فوتبال یک بار تصمیمی درست بگیرند. آقایان بگویند این تصمیم را با چه معیاری گرفتند. یک مثال بزنند در کجای دنیا با لیگی که ۹ هفته از آن مانده تیمی را برای حضور در سطح…</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/SorkhTimes/132536" target="_blank">📅 16:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132535">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✅
ترامپ: بهتر بود اصلاً وارد ماجرای ایران نمی شدیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/SorkhTimes/132535" target="_blank">📅 16:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132534">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
فوری؛ با اعلام دبیر سازمان لیگ، ادامه مسابقات لیگ برتر برگزار نخواهد شد و نمایندگان آسیایی ایران بر اساس جدول فعلی تعیین می‌شوند. به این ترتیب پرسپولیس سهمیه آسیایی نخواهد گرفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/SorkhTimes/132534" target="_blank">📅 16:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132533">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Da_Y_ZtlzferF8T9kTMgSItxGZgpmvF5Gl2MvA_tA9Doro6NQyPe-vVaLnzqHHjG3qZZJSqDRPNIH9SABW_JVHykUIzYCvkTTqZ0mE-YMhFfvKyowCpw-s4yLkjRUbGu7Zgiac-AjIkQ6AqEwM7j6jGGhtq3x40Z7qICJL3T5vAllL9o4kGvFTPc2NV-E9pppr5mNTkyPdokTaAzJyTKsRm2Wq2GPVh4fjEmE8stCiTkaSWglIB99O4EOQ_8TaJnEZmiLtFY2NpZ5ni0ePgPLrIyTib0cxljTZthzqIReOxYkjvLjgH8da9e0g0hLaRSKw52IvrpbxCC32I2zV6JwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
مایل به تمایل…!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/SorkhTimes/132533" target="_blank">📅 16:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132531">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CeuTCu70wlPqDc4SgB3JfFIsBnEgshkgteBm5S-nE6UwQByBFE03TSVU1WfLJpWEohkxJIXFkt8p6AB0gytHEBFIUWlqzSwngQoOHuqdNHAxS0gzdU6lHdvwKXlJPlah7KUHSdgOjVY_MWZZ_QzxrKpSKuCDsFHXnKrV-wlxlgRHwrzl38iM1JaAeV1KTCTJpRBgIAae-JVRVzsc-yqUXyyLKpEWVorXYDARu9QY4fg-a_eekfooRYOYIqhhZJ5KwfwDJdYDKBk2LRj8wwwNMwj8_udjut__8NGhVvjrwVnoqjYJTFSBOpfrxUp5VOAszPZRftb7KxjNw_X5-Hyqlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دسترسی دیتاسنتر همراه اول به اینترنت برقرار شد
🔴
اولین نشانه بازگشت اینترنت به دیتاسنتر ها  باید منتظر باشیم و وضعیت بقیه دیتاسنتر ها رو هم ببینیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/SorkhTimes/132531" target="_blank">📅 15:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132530">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
اوسمار به باشگاه پرسپولیس گفته واسه فصل بعد بازیکن خارجی می‌خواد و از باشگاه خواسته اگه جذب خارجی ممکن نیست، زودتر بهش بگن تا گزینه لژیونر معرفی کنه
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SorkhTimes/132530" target="_blank">📅 15:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132529">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e786c6b741.mp4?token=YwdhpSaXz3icEPmc9QSJJmvxSJzQoxaMDeagrFe3wCexvtuox6IF89gGQHegQKdb0g-CZT6dbKDsqoeu9en8Z6mkjay0SWOzS4gN9Bi8UkGT0PhA0pv6tWwHHk54pa2qldvMcdLCAa1bpDlZ_EH98uoJgEb9D31DL7fZPrbG-TdXcIMvRYvuzMZPWopuxKdGMCkvFtY7EBZpX-XDvBUmoqGBrYEy6MPl82-_UgqZZVMz8g7ePGVGndGRyL-50rWOt6xeyyLN0wog1h27PEswtXqfmK5C2AC71HrsnATyVt25qpNZaRsyfYfGLeM-WoZlaCj3bPQq9m_DjIQV_IdfzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e786c6b741.mp4?token=YwdhpSaXz3icEPmc9QSJJmvxSJzQoxaMDeagrFe3wCexvtuox6IF89gGQHegQKdb0g-CZT6dbKDsqoeu9en8Z6mkjay0SWOzS4gN9Bi8UkGT0PhA0pv6tWwHHk54pa2qldvMcdLCAa1bpDlZ_EH98uoJgEb9D31DL7fZPrbG-TdXcIMvRYvuzMZPWopuxKdGMCkvFtY7EBZpX-XDvBUmoqGBrYEy6MPl82-_UgqZZVMz8g7ePGVGndGRyL-50rWOt6xeyyLN0wog1h27PEswtXqfmK5C2AC71HrsnATyVt25qpNZaRsyfYfGLeM-WoZlaCj3bPQq9m_DjIQV_IdfzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▪
︎ اگه این روزا سایتا سخت لود میشن، ربات تلگرام وینکوبت خیلی کارو راحت کرده:
👇
🤖
@Wincobet_bot
بدون اینکه از تلگرام خارج شی میتونی مستقیم وارد بخش بازی‌ها و کازینو بشی، پیش‌بینی ثبت کنی و حتی واریز و برداشت انجام بدی.
▪
︎حالت Mini App داخل تلگرامه و خیلی سبک‌تر و سریع‌تر باز میشه:
👇
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SorkhTimes/132529" target="_blank">📅 14:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132528">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
مدیرعامل آروان کلاد: از نظر فنی همینطوری که میشه توی یه لحظه اینترنت رو قطع کرد؛ همینطوری میشه تو یه لحظه هم وصلش کرد. زمانبر بودن بهبود وضعیت اینترنت از نظر فنی فقط بهانه ست. وضعیت اینترنت در حال حاضر بسیار ناپایدار و ضعیفه و اصلا به شرایط قبل از جنگ برنگشته.…</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/SorkhTimes/132528" target="_blank">📅 13:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132527">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
قـلعـه نـویی امروز لیست اسامی ۵ نفری که قراره خط بخورن رو میده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SorkhTimes/132527" target="_blank">📅 12:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132526">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❗️
امیر قلعه‌نویی:
👍
دو سه شبه که از بس به فکر چیدن لیست تیم ملی هستم، نخوابیدم. راستش رو بخواهید، هر چه تا امروز خواستم نشده، ولی خداروشکر. من به این تیم ملی امیدوارم، هرچند مشکلاتمان خیلی خیلی زیاد است.
👍
این روزها برای انتخاب نفرات واقعاً روزهای سختی است.…</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/SorkhTimes/132526" target="_blank">📅 12:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132525">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">#اختصاصی_سرخ_تایمز
🔴
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس شایعات منتشر شده در صفحات مجازی صحت ندارد و مارکو باکیچ فصل آینده در پرسپولیس توپ خواهد زد؛ و بند مشروط قرارداد باکیچ فعال شده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SorkhTimes/132525" target="_blank">📅 12:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132520">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
ترامپ: ایران باید قبول کنه هیچ‌وقت سلاح هسته‌ای نخواهد داشت
🔴
تنگه هرمز باید فوری باز بشه و عبور کشتی‌ها بدون هیچ محدودیتی انجام بشه. هر نوع مین دریایی هم باید کامل جمع‌آوری یا نابود بشه
🔴
کشتی‌هایی که به خاطر محاصره متوقف شدن می‌تونن برگردن به مسیرشون و…</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SorkhTimes/132520" target="_blank">📅 10:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132519">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✅
سپاهان به بازیکناش اعلام کرده فصل آینده با کمبود بودجه روبه‌روئه و احتمال فروش چند ستاره این تیم بالاست؛
🔴
پرسپولیس و استقلال هم می‌خوان از این فرصت استفاده کنن و برای جذب بازیکنای کلیدی سپاهان وارد عمل بشن...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/132519" target="_blank">📅 10:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132518">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✅
زمزمه هایی شنیده می‌شود که امیر قلعه‌نویی پس از جام جهانی از تیم ملی جدا خواهد شد و یحیی گل‌محمدی گزینه اصلی جانشینی او است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SorkhTimes/132518" target="_blank">📅 10:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132516">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✅
سهراب بختیاری‌زاده از وقتی فهمیده استقلال بدنبال سرمربی جدیده شاکی شده و میخواد استعفا بده !
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SorkhTimes/132516" target="_blank">📅 10:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132515">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
عضو هیئت رئیسه فدراسیون فوتبال: تصمیم فدراسیون بر ادامه لیگ است/ منتظر رای استیناف درباره سپاهان هستیم
◻️
رحمان سالاری عضو هیات رئیسه فدراسیون فوتبال، در خصوص تصمیم اعلام شده توسط سازمان لیگ:
◻️
اینکه لیگ تمام شده اشتباه محض است.
فدراسیون فوتبال به دنبال این است که لیگ را ادامه دهد حتی اگر لیگ هم تمام شود ما قطعا قهرمان را اعلام نمی‌کنیم.
◻️
براساس مصوبه سازمان لیگ و با موافقت فدراسیون فوتبال
ما ۶ تیم اول را به آسیا معرفی می‌کنیم و براساس دریافت مجوز بهترین تصمیم را می‌گیریم
اما با این حال اگر تیمی موفق به دریافت این مجوز نشود، تیم بعدی جدول که شرایط لازم برای حضور در آسیا را داشته باشد، می‌تواند جایگزین شود.
◻️
ما به دنبال این هستیم که بهترین تصمیمات را بگیریم که حق تیمی ضایع نشود.
در خصوص تیم سپاهان منتظر نتیجه کمیته استیناف هستیم و بعد از نتیجه این کمیته باید منتظر نتیجه AFC بمانیم که ببینم این موضوع قرار است چطور پیش برود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SorkhTimes/132515" target="_blank">📅 10:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132513">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UszNyaEFYJ6KV0tsd4Dx96xaLg1UEiju1WwbeX64E0KwNI8hMozcMv3Hc2uDtoh1JtM9EFBfqCZ47sh9e9yGBcUoMBLgyTK_Lbmx05gSpmfc-99h7sQgZUCPhLVk9BZaVle4Okl0AQvkCTq0f_zWHs7IZlKvbrSAT_dfpMdF89oSINDC67y1j1AyJvSrWB6eRelzHfINnAPlzfU-g3a19RmKUVbSzZGaywiB-HrR_iSv65jOfvc1k-siDwZjpmQwqW22BZnaY4-92sa5WsRpjlnOjQpOgUNfReqiPOAeOvjxI7pIwNfxAiw2AYQhTtdrTSKmffqvtR77f7RxcqjQug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⛔️
ورزش سه: حرکت غیر ورزشی تاج
‼️
🔴
در جلسه کمیته استیناف برای بررسی مجوز حرفه ای باشگاه سپاهان، اعضا دو بار (صبح و بعدازظهر) به این نتیجه رسیدن که اعتراض این باشگاه رد شده و مجوز حرفه ای صادر نمیشه
◻️
اما مهدی تاج، رئیس فدراسیون فوتبال، با اصرار و فشار شخصی خواستار صدور مجوز شده
دلیل اصرار تاج، قول دریافت 250 میلیارد تومانی از کارخانه فولاد مبارکه اصفهان برای تیم ملی هست در نهایت، کمیته استیناف همچنان مخالفه و پرونده معلق مونده
👀
‼️
🔥
رئیس کمیته صدور مجوز تهدید به استعفا کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SorkhTimes/132513" target="_blank">📅 09:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132512">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
قهرمانی دراماتیک پرسپولیس تو فصل ۸۱-۸۰ رو ببینید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SorkhTimes/132512" target="_blank">📅 09:41 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132511">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">#اختصاصی_سرخ_تایمز
🔴
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس هنوز باشگاه وارد نقل و انتقالات نشده و منتظر اوسمار هستند!
♦️
لیموچی و هر اسمی که به گوشتون خورده در حال حاضر هیچکدوم شون صحت ندارن و تا این لحظه باشگاه هیچ مذاکره ای با گزینه…</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SorkhTimes/132511" target="_blank">📅 09:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132510">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
محسن خلیلی: باشگاه پرسپولیس حق دارد از حق و حقوق خود به هر طریقی دفاع کند
◻️
متأسفانه در روزهای اخیر شاهد آن هستیم که برخی افراد از طریق مصاحبه‌های رسانه‌ای و به صورت غیررسمی درباره نمایندگان ایران در مسابقات آسیایی اظهارنظر می‌کنند. این درحالی است که طبق بخشنامه AFC، فدراسیون فوتبال ایران برای معرفی نماینده های ایران به آسیا تا روز 9 تیر فرصت دارد و باشگاه پرسپولیس حق قانونی خود می داند که فدراسیون تا آن زمان برای انتخاب و معرفی نماینده های ایران صبر کند. چنین رویه‌ای و اقدامات این چنینی به هیچ وجه حرفه‌ای نیست و می‌تواند باعث ایجاد ابهام و سوءبرداشت در افکار عمومی و میان باشگاه‌ها شود.
◻️
اعلام رسمی نمایندگان فوتبال ایران در رقابت‌های آسیایی، باید از مجاری رسمی و مکتوب انجام شود. طرح این موضوعات در قالب مصاحبه‌های شخصی، نه تنها کمکی به شفافیت نمی‌کند، بلکه می‌تواند موجب بروز حواشی غیرضروری شود. باشگاه پرسپولیس حق خود می‌داند که موضوع مطرح‌شده را از مسیرهای قانونی و حقوقی پیگیری کند تا از حقوق و منافع این باشگاه به طور کامل صیانت شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SorkhTimes/132510" target="_blank">📅 09:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132508">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YxgAzmB1ctCCxpHmj8vALuYV8WBA_qrdXbuPZ-zLJxaapvOjAkJnz7p-RHuhWu2fYl7LIsIx0I0Q3zOYhwsCiJ7Rbiu92VecQUsRK52dQYK1nMfy3CioWlrP55LGBX7EPTCgzAkD01RDS3RNjpKAhd8aLBbOxYVWTxIKrX4_bcuhDJgkMs6QOgrporlEib_jw7Ava3Maw9AzZaNQ69Szs-5SVnkYzkCsD0YbWiGfyUxrclsshUcRkdJsb3RhGv7A_PjJ80-AmC1y3ZvmaluFR7oYVQzrLtnfoLfKcQ9yK9iFvTdIL1N6JZiXveXqD_5abForP2CXpEmGNfS9vekC8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
گردونه شانس رایگان وینکوبت فعال شد!
🎰
هر ۱۲ ساعت یک‌بار شانس خودتان را امتحان کنید و جوایز نقدی متنوع دریافت کنید.
🎁
تا سقف ۱ میلیون تومان جایزه روزانه
✅
فعال برای تمامی کاربران
📌
برای شرکت در گردونه شانس، وارد ربات وینکوبت شوید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/132508" target="_blank">📅 00:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132507">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
در پی فشارهای تاج بر کمیته حرفه‌ای سازی برای تایید مجوز سپاهان، مصطفی زارعی مسؤول این کمیته تهدید به استعفا کرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/132507" target="_blank">📅 00:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132506">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
کمالوند سرمربی خیبر شد!  پ.ن و. احتمالا پنگوین (مهدی رحمتی )سرمربی کیسه میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/132506" target="_blank">📅 00:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132505">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00937b1a6d.mp4?token=h8q3rl3XA0TLpSFMkvYnbZZpYNW1bX0h0PPZHJ_0NGdQoiF855FvAqAb3Vz9Al30Zus0cHmb1YK55KceYc8I23ca9t6PklnX9CXGIXU5ueDkIbKMrKHHrd1RkQWZ-hjVrTICnNmxIZSOs3o410FUYLMXD7wFOgUXkXQTsFerQiUsulhnicXqQiw7rzWluNCulaW2puhWf2Er4-nRKc_p3lYE984AJxDXnFEf-PhWhsL-BjDbwTr3YUVct4Eag05MqHKDVD-rJ5MenRIknHsKjRx5zs2J4O8v0_hs7J4SbbiBPvJqMgFC1S6UtZt9fRHw7t2C1r-3oigtXmcocTMrkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00937b1a6d.mp4?token=h8q3rl3XA0TLpSFMkvYnbZZpYNW1bX0h0PPZHJ_0NGdQoiF855FvAqAb3Vz9Al30Zus0cHmb1YK55KceYc8I23ca9t6PklnX9CXGIXU5ueDkIbKMrKHHrd1RkQWZ-hjVrTICnNmxIZSOs3o410FUYLMXD7wFOgUXkXQTsFerQiUsulhnicXqQiw7rzWluNCulaW2puhWf2Er4-nRKc_p3lYE984AJxDXnFEf-PhWhsL-BjDbwTr3YUVct4Eag05MqHKDVD-rJ5MenRIknHsKjRx5zs2J4O8v0_hs7J4SbbiBPvJqMgFC1S6UtZt9fRHw7t2C1r-3oigtXmcocTMrkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های امشب عادل فردوسی‌پور در آپارات اسپورت بعد از مدت ها برای گزارش بازی فینال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/132505" target="_blank">📅 00:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132504">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
فوووووری
🚨
مدیران باشگاه پرسپولیس در مذاکرات با چند بازیکن جوان شکست خورده اند و موفق به‌ توافق با بازیکنان و باشگاه های اونا نشدن/ فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/132504" target="_blank">📅 00:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132503">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
سپاهانی‌ ها از بهمن‌ماه سال گذشته دیگه دریافتی نداشتن، از طرفی مدارک مالی هم بارگذاری نکردن و گفته شده استیناف رای به عدم اخذ مجوز حرفه‌ای این تیم داده اما تاج همچنان داره براشون زور میزنه
✔️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/132503" target="_blank">📅 23:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132502">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bc9aa4117.mp4?token=oUEUOOnOjYSDsMvUXIx8-8ltC7f12JY04ZWhD9RDy_5O3TuVUdNfYLm071AMwWzXpLnM87FsYEuU_wGj2ffcD0bOTDa0-0tx4qxlKgBnIrgBtYPiV2kdOqz7PWhdL5fC4dlXKLNJ9F9MoU8MFP-eMiyQ2DETb33gP88yFtUiMtc_XKVtVgvPLrp5jdPcmzOvrHPWLGc1D_smzqgayxTdIOtAFU-zZ-RcNAJ6hM6l7fnGNRx_hKZ_h65gnC9EQMz29XDJvUFa0B8XX1AaeSuqV1NZeg8zrEywqt5Axoc4DcJMWUzktDHMoic74Jkwd0sSmNI4ogcHDN8aTkog1v8qCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bc9aa4117.mp4?token=oUEUOOnOjYSDsMvUXIx8-8ltC7f12JY04ZWhD9RDy_5O3TuVUdNfYLm071AMwWzXpLnM87FsYEuU_wGj2ffcD0bOTDa0-0tx4qxlKgBnIrgBtYPiV2kdOqz7PWhdL5fC4dlXKLNJ9F9MoU8MFP-eMiyQ2DETb33gP88yFtUiMtc_XKVtVgvPLrp5jdPcmzOvrHPWLGc1D_smzqgayxTdIOtAFU-zZ-RcNAJ6hM6l7fnGNRx_hKZ_h65gnC9EQMz29XDJvUFa0B8XX1AaeSuqV1NZeg8zrEywqt5Axoc4DcJMWUzktDHMoic74Jkwd0sSmNI4ogcHDN8aTkog1v8qCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗼
لحظه قهرمانی پاری‌سن‌ژرمن در لیگ قهرمانان اروپا با خراب شدن پنالتی گابریل
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/132502" target="_blank">📅 23:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132501">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
🏆
فینال لیگ قهرمانان اروپا| انریکه جام را از آرتتا ربود؛ پاریسی‌ها در ضربات پنالتی برای دومین بار متوالی قهرمان اروپا شدند
🇫🇷
🔴
آرسنال یک (٣)- پاری‌سن‌ژرمن یک (۴)
⚽️
گل آرسنال: هاورتز
⚽️
گل پاری‌سن‌ژرمن: دمبله  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SorkhTimes/132501" target="_blank">📅 22:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132500">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✅
بازی رفت به وقت های اضافه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/132500" target="_blank">📅 22:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132499">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🛜
سرویس نامحدود Open VPN
یک ماهه تک کاربره 1T
🛜
سرویس نامحدود وایرگارد
یک ماهه تک کاربره 1.1T
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/132499" target="_blank">📅 22:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132497">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
گلللللل اووول آرسنال به پاریس توووسط هاورتزز دقیقه 6  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/132497" target="_blank">📅 21:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132496">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
گلللللل اووول آرسنال به پاریس توووسط هاورتزز دقیقه 6  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/132496" target="_blank">📅 21:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132495">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
به تیم ملی جمهوری اسلامی واسه جام جهانی قراره ویزای ساعتی بدن یعنی واسه هر بازی چند ساعت ویزا میدن بیان بازی کنن بعد سریع باید برگردن مکزیک تازه این ویزا فقط برای بازیکنان و کادر فنی صادر میشه نه افراد دیگه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/132495" target="_blank">📅 21:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132494">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">⚪️
باشگاه پرسپولیس سازمان لیگ را به مناظره دعوت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/132494" target="_blank">📅 21:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132493">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1sontpTcNIhV3BAZg2IUq0FkuHv8YLgQPcvsLTUlbsNG9NyPehmApEVnnDFeutJbIqbcCilWcn0tck9WOtJKfaTJKUS98ohTl4AXTpzsaab_6shS9D1W07xzjTm7vzkNovpoYZObEZVMixo8ykhW5hN98hpc6B0-61gYgoEIcN99nv5vuALM1QUZPbc2OxsRAeEHsItWRFNiZREPZqv3N1ndDFQ_yjs_jgPLcz0J-NagjE7Sp8Ehdv48VucbgNRs6oOQZuR-sfTycgDxsIWvLaoDa7a5LNj2go6TXMJBLBWz5sS3a-kKaY1cCXWx7TUBcLUYZp48NEItavDrU3_OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
Champions League - Final
🔵
PSG -
🔴
Arsenal
⏰
Tonight 19:30
🏟
Puskás Aréna
ربات تلگرام وینکوبت تو این شرایط که اینترنت زیاد قوی نیست خیلی خوبه، چون کل سایت داخل خود تلگرام اجرا میشه و دیگه لازم نیست هی بین سایت و VPN درگیرشی:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
به کاربرانی که تا قبل از نیمه دوم بازی در وینکوبت ثبت‌نام کنند بونوس ۱۰ چرخش رایگان کازینو با جوایز نقدی و شانس بالا تعلق میگیرد.
📌
کانال رسمی وینکوبت:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SorkhTimes/132493" target="_blank">📅 20:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132492">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a6f96dc5.mp4?token=E0FHsUDnG8R0MWcoXF6ojv4kxgWBXs5--p25NiIsd88S_TuWGeRUb6X3QLBUH-nx-7HIiO4G3FNEWOZaSPg6t66xZ4UVOsx_F3CVaRjqDih3gO1fG0NOAzkwWckR8eyAcZnZMjzZjbWDaSMjvZqsz7gHB8NiPQqMWTCR10DgyX-5BJZtlvBbE3fgqOy3vDfQ4m0pEhL4nMs2mZhU7W7Bbq77KbLHPtfR7q5YoYZMovjeN39G4URA-2SMCfJBqEAK9wH94DocAP5vSUp1_SKm6BRr5-P5rqz3612D29a-IESEh9zxkrg9qP8V3jgz5u4LDzL9hkicfmun9u0ZSyyQAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a6f96dc5.mp4?token=E0FHsUDnG8R0MWcoXF6ojv4kxgWBXs5--p25NiIsd88S_TuWGeRUb6X3QLBUH-nx-7HIiO4G3FNEWOZaSPg6t66xZ4UVOsx_F3CVaRjqDih3gO1fG0NOAzkwWckR8eyAcZnZMjzZjbWDaSMjvZqsz7gHB8NiPQqMWTCR10DgyX-5BJZtlvBbE3fgqOy3vDfQ4m0pEhL4nMs2mZhU7W7Bbq77KbLHPtfR7q5YoYZMovjeN39G4URA-2SMCfJBqEAK9wH94DocAP5vSUp1_SKm6BRr5-P5rqz3612D29a-IESEh9zxkrg9qP8V3jgz5u4LDzL9hkicfmun9u0ZSyyQAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گلللللل اووول آرسنال به پاریس توووسط هاورتزز دقیقه 6
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SorkhTimes/132492" target="_blank">📅 20:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132491">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
شایعه حضور تارتار روی نیمکت پرسپولیس از کجا آب می‌خورد؟
💸
یک دلال با سوءاستفاده از شرایط جنگی و شایعات درباره بازنگشتن خارجی‌ها ، پیشنهاد داد در صورت نیامدن اوسمار ، تارتار سرمربی پرسپولیس شود.
⛔️
این پیشنهاد جدی گرفته نشد و مدیران پرسپولیس قصد دارند همکاری…</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/132491" target="_blank">📅 20:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132489">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❗️
ساعت 19/30 فینال جام باشگاه های اروپا بین پاریس و آرسنال انجام میشه ...پیش بینی شما از این بازی چیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SorkhTimes/132489" target="_blank">📅 19:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132488">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gpk-mqVsUXzdbaL9jGFx8LybZ5kjlerEXkJC3RW1V43NuKnRNXm9WNiS2OLugxMco4v8RmRjFlFlwLJ0-xA5PyPnuXcm_tAajHm0WH5dYpj3kvhSQspMPRKZVXfgkTw0RfUcsTrqLM6ci4TWnK-NFW6BM2jEP796b8bCU0MLesOQDqLOqpuzYIfyr_CbDFpzEGHMg6lHNCSam4Yb0yxe3aQayuC4MvrpA46ZFCBgQJEA8PRm5g7QaxJDE_br5Rnc5lF5OC578dfW6k1gpRJ5plYORhqJyRZuJAJanaA3985Vak7ynHT5ldhk92cl9_UtNjhqmx83-CiSO6e4BOFaPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
باشگاه پرسپولیس سازمان لیگ را به مناظره دعوت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/132488" target="_blank">📅 19:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132487">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EE6E1nARKpcfBsaO9uu9xGgK0wfLZlp4-Zo6qM12x7RpJ0cxPFOE0c5vvar4BfiHPwwvpnF3yfKW_KMDgxaWdCOhIJpvDnVvJtI82tG9zVFty0AhR2a02eun_oS9gfUgkzbApzwYvPGj1k3bxjOiO1jgWbZgmSAE0H6BAaqTkYfYh7zaxsrl_5xBaY2ISpllW1uW19QQ17c-Kz7bNJdJILWt0PPn5D-oOwFrEnqegt1BmhxDW9SSxOMkkYdE9Iu7GPWJx2YdSbYEXD06qq5LLITphj2U_i27fxiWvDceL0k296w4iQPFE0J4MoRKnOCZeMUXZp8H8RBAqPskdz7ZHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری؛ با اعلام دبیر سازمان لیگ، ادامه مسابقات لیگ برتر برگزار نخواهد شد و نمایندگان آسیایی ایران بر اساس جدول فعلی تعیین می‌شوند. به این ترتیب پرسپولیس سهمیه آسیایی نخواهد گرفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SorkhTimes/132487" target="_blank">📅 18:54 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132486">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
مهدی لیموچی با مدیران پرسپولیس به توافق رسیده و به زودی با اتمام قراردادش به جمع سرخپوشان پایتخت اضافه خواهد شد/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/132486" target="_blank">📅 18:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132485">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❗️
ساعت 19/30 فینال جام باشگاه های اروپا بین پاریس و آرسنال انجام میشه ...پیش بینی شما از این بازی چیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/132485" target="_blank">📅 18:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132484">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
اولین بمب تابستانی پرسپولیس؟
🔴
ادعای سایت هفت ورزشی؛ اگر اتفاق خاصی نیفتد آریا یوسفی را باید اولین بمب تابستانی باشگاه پرسپولیس برای فصل آینده لقب داد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/132484" target="_blank">📅 18:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132481">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
امیر عابدینی: فدراسیون هر کاری می کند تا سپاهان به آسیا برود؛ لیگ باید ادامه پیدا کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SorkhTimes/132481" target="_blank">📅 16:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132480">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
اوسمار کراش زده رو آریا و لیموچی و حزباوی و باشگاه در تلاشه برای جذب شون راهی پیدا کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SorkhTimes/132480" target="_blank">📅 16:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132479">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">⁉️
⁉️
نت بلاکس: سه ماه پیش در چنین روزی Iran دسترسی به اینترنت جهانی را قطع کرد. در حالی که اتصال اکنون تا حد زیادی بازگشته است، شاخص‌ها نشان می‌دهند که کاربران هنوز با فیلترینگ شدید مواجه‌اند، مشابه دوره موقت بین اعتراضات ژانویه و آغاز جنگ.
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SorkhTimes/132479" target="_blank">📅 16:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132478">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8ec1381c4.mp4?token=OhS2jUvOWs6T4EK5yLdLdIUQ-F-ct4QF3BVVLUGa_wzKEUWVH_q8ltLa15y_vjXfMdNSQyA2gAtI0N6eEHrPeHL6acLq7D9cPsvfTx1mXDQJDOl4l06AT8d-H7JXl-DfIE_WTQh3jz47aya7ixXjFvajBx1yXi_DSroZh4glxgH3c6A0xkC6d4QeQ-XCfsfphDHRTs1eFMI569lGSv9IWLWv0mwYEieeV6TSvh_9DGKG4bQBtXnieeEOJI69znJIyY4kJqjCCqXMb4Mfj6eukik48k39Y871psbslOu6qI715ZC6rBHlqxdW_ZZEqA02do4-VOU24Yx4guQJd2R1Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8ec1381c4.mp4?token=OhS2jUvOWs6T4EK5yLdLdIUQ-F-ct4QF3BVVLUGa_wzKEUWVH_q8ltLa15y_vjXfMdNSQyA2gAtI0N6eEHrPeHL6acLq7D9cPsvfTx1mXDQJDOl4l06AT8d-H7JXl-DfIE_WTQh3jz47aya7ixXjFvajBx1yXi_DSroZh4glxgH3c6A0xkC6d4QeQ-XCfsfphDHRTs1eFMI569lGSv9IWLWv0mwYEieeV6TSvh_9DGKG4bQBtXnieeEOJI69znJIyY4kJqjCCqXMb4Mfj6eukik48k39Y871psbslOu6qI715ZC6rBHlqxdW_ZZEqA02do4-VOU24Yx4guQJd2R1Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
محسن خلیلی، سرپرست پرسپولیس: وقتی پیراهن تیم ملی را میپوشی، سرود ملی را هم با افتخار بخوان!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/132478" target="_blank">📅 16:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132476">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❗️
🔴
وقتی قرمزآنلاین فاش کرد محمودی از سوی ایجنت ها محاصره شده و برای تمدید قرارداد هر هفته یک ایجنت را به باشگاه فرستاده متهم شدیم به حاشیه سازی اما انچه گفتیم حقیقتت بود.از او خواستیم مراقب باشد.محمودی از برترین استعدادهای فوتبال اسیاست.
🔺
احسان خرسندی، سرمربی…</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SorkhTimes/132476" target="_blank">📅 15:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132475">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✅
باوجودی که فدراسیون فوتبال رسما اعلام کرده بود موافق برگزاری مسابقات شش جانبه است اما در تصمیمی ناگهانی و عجولانه، بر اساس جدول نصفه نیمه و ناقص، نمایندگان آسیا رو معرفی کرده!!!
🔴
سپاهان که قطعا مجوز حرفه‌ای نمیگیره ولی جدی میخوایین گل‌گهر یا چادرملو رو بفرستین…</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SorkhTimes/132475" target="_blank">📅 15:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132474">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
مجوز حرفه ای سپاهان صادر نشد و ممکنه یه تیم از بین پرسپولیس و گلگهر بره اسیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/132474" target="_blank">📅 15:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132473">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
فرهیختگان: علیپور از پرسپولیس خواسته رقم قراردادش از همه ایرانیای لیگ بالاتر باشه و اگه موافقت کنن بعد جام جهانی تمدید میکنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/132473" target="_blank">📅 15:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132472">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCc-_EygrQ_r9-mXXmkROggWfdpqGcIR8IdLX09cXxsdGEfb_kllknCcG-PSe-iBeAng11KPJTbzkSDX0sXQoV87vXqsqA8GuR9G6HCb7ufbq-I32IkfJideqenyF_PwH6QedHBeBTes5cnTJ3kVxGQApxsHB7hGE0s83ll2TZPLRvLHN-19iwFa5WOHKm_sEqZVugTgtz6TeiDW3is2hf6jpbFaEZqYQZMYNQcXo-j29kbfbPjiZIKAzWoo2zoXRRj853cPVaNYyOVgfg1WCIGP01KdZU9CpG2FCqW8ycwgTCCIjPvJpkeaXqX6UH_VHT27YhAPl5tf3rX_ualNRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🇪🇺
فینال لیگ قهرمانان اروپا
[
پاری‌سن‌ژرمن
⚽️
-
⚽️
آرسنال
]
⏰
امشب ساعت ۱۹:۳۰
🏟
استادیوم پوشکاش‌آرنا
🔗
فینال جذاب و هیجان‌انگیز امشب رو در سایت اسپورت نود با بالاترین ضرایب و بیشترین آپشن ممکن پیش‌‌بینی کنید.
🎁
بونوس ویژه ثبت‌نام برای کاربران جدید، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
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
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SorkhTimes/132472" target="_blank">📅 15:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132471">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
فراز کمالوند سرمربی صنعت نفت: سوال مردم آبادان این است که دو سوم شهر بوی گاز پیچیده اما چرا پولش در تهران برای استقلال خرج شود؟ بوی گاز برای آبادانی‌هاست اما پولش برای یک تیم تهرانی!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚩
⭐
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SorkhTimes/132471" target="_blank">📅 14:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132469">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc298e01b9.mp4?token=uvocipktsBAOz9X7u7tPR69HldJXDVrBY6qKbnqLo2muoU9EecK-TyVhUYHSRNbpBIT8mkwlBhM0gtaKnmpaZa5Y7etlYI32WdegHva2_Ru6TrFW-X8ld86NVwsG5YVrdk0W3wG1iDIM3xnKxksxyZGcHL104xLOA-Najoza0vl1n1I0W6qSf1gMlgb_UX6338hoowaE1YSLtcmq0kz9UlOd6_uNcteH1fGUvZxiIYDbIAvNPSHQr9xZgvHtWT7Vf2PS6KzvX2_3ly37OGZR2anDmUPUs-OlBBxKHpjVYstUqFydW6kOXM-MsVbtrRRgtoWXPln7nPx4Cd4oqsVQzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc298e01b9.mp4?token=uvocipktsBAOz9X7u7tPR69HldJXDVrBY6qKbnqLo2muoU9EecK-TyVhUYHSRNbpBIT8mkwlBhM0gtaKnmpaZa5Y7etlYI32WdegHva2_Ru6TrFW-X8ld86NVwsG5YVrdk0W3wG1iDIM3xnKxksxyZGcHL104xLOA-Najoza0vl1n1I0W6qSf1gMlgb_UX6338hoowaE1YSLtcmq0kz9UlOd6_uNcteH1fGUvZxiIYDbIAvNPSHQr9xZgvHtWT7Vf2PS6KzvX2_3ly37OGZR2anDmUPUs-OlBBxKHpjVYstUqFydW6kOXM-MsVbtrRRgtoWXPln7nPx4Cd4oqsVQzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
آشتیانی پیشکسوت پرسپولیس: از سهراب بختیاری‌زاده انتظار نداشتم برای بدست آوردن دل هواداران استقلال به همه پرسپولیسی‌‌ها بگویید شما فاسد هستید!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/132469" target="_blank">📅 14:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132467">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‼️
وقتی هوادار اسیر دست جو رسانه ای میشه و ارکان باشگاه و بانک شهر رو تحت فشار قرار میده ثمرش میشه مربی ۴۰۰ هزار دلاری با باشگاه برای ۶ ماه ببنده ۱.۲ برای فصل بعدش هم ۱.۷ این ک.ص.کش خان همین الان بشینه تو خونش تا ۳۰ سال دیگم ۳ میلیون دلارو تموم نمیکنه… ایرانیه…</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/132467" target="_blank">📅 13:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132466">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
قرارداد اوسمار برای فصل آینده ۱.۷ میلیون دلار هست دقیقا مشابه دستمزد پابلو وانولی سرمربی فیورنتینا در سری آ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SorkhTimes/132466" target="_blank">📅 13:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132465">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlJlSUw8uOcxNiMVrzD8C0jZ6MwCHFimwLL884emTO6jCDnaAGkEK4Yw1AoBCaGn1Ung4t5E-4gDXxV-5LUo3vAEhoHwlbJkUPQ9jbXlHwhO5DIYOTmb-lnrXR5IN-vUnhHL-sKfRCkvjWryYY__IeXQx5gKVwoHE7oui35J1N4J7qbJeYeCAtXX29QEKdEkajfB2xycz9_512wCGtn4gzwpztrqmrStM4PzDih03u3CkAkw7LfCkKoXeitXhvixPBGYiS5RxdaXpp8N6OPsWs6GBAcQBf2YHuCy1Zn57BPEy7ch2UJMwL60AZ5dJUVb24CcFETq9LF4x-jXhdNIPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قرارداد اوسمار برای فصل آینده ۱.۷ میلیون دلار هست دقیقا مشابه دستمزد پابلو وانولی سرمربی فیورنتینا در سری آ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/132465" target="_blank">📅 13:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132464">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اصرار بی مورد برای بازگشت؛
🔴
«اوسمار» استخوان در گلوی پرسپولیس/ ۳۰۰ میلیارد برای مربی شکست خورده!
❌
خبرگزاری مهر: متحمل شدن چهار شکست در پنج بازی آخر پرسپولیس باعث شد سرخپوشان تهرانی فاصله قابل توجهی با صدر جدول بگیرند و با ۷ امتیاز اختلاف نسبت به رقیب سنتی…</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SorkhTimes/132464" target="_blank">📅 13:14 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132463">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اصرار بی مورد برای بازگشت؛
🔴
«اوسمار» استخوان در گلوی پرسپولیس/ ۳۰۰ میلیارد برای مربی شکست خورده!
❌
خبرگزاری مهر:
متحمل شدن چهار شکست در پنج بازی آخر پرسپولیس باعث شد سرخپوشان تهرانی فاصله قابل توجهی با صدر جدول بگیرند و با ۷ امتیاز اختلاف نسبت به رقیب سنتی خود در رده ششم بایستند. اتفاقی که انتقادات زیادی را متوجه «اوسمار ویه را» سرمربی برزیلی سرخپوشان کرد.
❌
در این میان هم کمتر کسی به این نکته توجه می کند که مربی گرانقیمت برزیلی یکی از مقصران اصلی وضعیت کنونی پرسپولیس است. ویه را که به خاطر دریافت دلارهای بیشتر در دوره گذشته پرسپولیس را ترک کرد و به تایلند رفت، پس از آن که سرخپوشان نتوانستند با وحید هاشمیان نتایج مدنظرشان را کسب کنند، دوباره گزینه شد و پس از قهرمان کردن بوریرام تایلند با چهره ای مدعی به ایران برگشت.
❌
اوسمار در حالی به پرسپولیس برگشت که رقم های پیشنهادی اش چند برابر گذشته بود و جالب این که مدیران باشگاه هم با این درخواست موافق کردند به گونه ای که گفته می شود او برای نیم فصل یک میلیون و ۲۰۰ هزار دلار دریافت کرده است و برای فصل آینده این رقم ها سرسام آورتر می شود.
❌
به گفته یکی از نزدیکان باشگاه پرسپولیس رقم قرارداد او برای یک فصل و نیم بیشتر از ۳ میلیون دلار است که با وضعیت اقتصادی کنونی باشگاه وحشتناک و غیرقابل تصور است. این در حالی است که چنین رقمی در لیگ های مطرح برای مربیان طراز اول پرداخت می شود/مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/132463" target="_blank">📅 13:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132460">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
محسن خلیلی، معاون پرسپولیس:
‼️
شانس داشتیم که اگر بازی‌ها برگزار می‌شد، سهمیه بگیریم. باید تیمی به آسیا برود که سابقه خوبی داشته باشد و اصلح باشد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/132460" target="_blank">📅 12:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132459">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✅
بهادر عبدی، مربی تیم امید پرسپولیس: امیرحسین محمودی آینده درخشانی دارد. او می‌تواند در همه پست‌های هجومی بازی کند. می‌تواند حتی به بارسلونا برود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/132459" target="_blank">📅 11:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132458">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
المـاس ارتش سـرخ فقط ۴ دقیقه زمان برای درخشیدن نیاز داشت.
🔴
امیر حسین محمودی در جریان بازی دیشب تیم ملی مقابل گامبیا بعنوان بازیکن تعویضی در دقیقه ۸۶ وارد زمین شد که اون تنها در ۴ دقیقه زمان تونست با دو پاس عمقی فوق العاده علیپور و بار دیگر ترابی رو در موقعیت…</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/132458" target="_blank">📅 11:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132457">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❗️
باشگاه پرسپولیس تصمیم‌گرفته است بزودی؛ قرارداد امیرحسین محمودی را از لحاظ مالی افزایش دهد
🔴
به احتمال فراوان قرارداد وی 4 ساله می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/132457" target="_blank">📅 11:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132456">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qS_p3o13zNtAuwSISIN4_0g6OM8EncJ99mJ8F_hUvLzNAbxDC901ub6ghpledAizN2Au7X1PUbZSDkM4qoMlMzLGNeRa_-U6UxNmfs5mg1o2PqzeM_LkzEhggiMkF_tBLVnTHLVU48bh_nl2rWIFAujo5Noy20j0XN10V-5T7kVKnALRCVdHpsxaOhDyd1ffcTrpiFI4x-JeFAtVB2edEb8N9SudQGNW0UQD3RbCQQ8ZOGHNEf7qgzBrgI1k4ru9aCLeYvgl5Q9HldNdtx2BcWaeeEXBhNSrwsMHGGl1yShj2sctyYgMri7ImXQjAjIYu0-rXbTMjTnuPlX1ThZh_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🇫🇷
مسابقات گرنداسلم رولان‌گاروس رو با بالاترین ضرایب در اسپورت نود پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
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
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/132456" target="_blank">📅 01:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132455">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❗️
فرهیختگان: AFC مجددا با درخواست فدراسیون جمهوری اسلامی مبنی بر دیر اعلام کردن 3 نماینده برای حضور در آسیا مخالفت کرده و اعلام کرده ۱۳ روز وقت دارید که 3 نماینده خود را معرفی کنید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/132455" target="_blank">📅 00:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132454">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❗️
فرهیختگان: AFC مجددا با درخواست فدراسیون جمهوری اسلامی مبنی بر دیر اعلام کردن 3 نماینده برای حضور در آسیا مخالفت کرده و اعلام کرده ۱۳ روز وقت دارید که 3 نماینده خود را معرفی کنید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SorkhTimes/132454" target="_blank">📅 00:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132453">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🎙
پیمان حدادی:
🔴
ما هم می‌گوییم استقلال نباید معرفی شود؛ در حالی که نماینده پلی‌آف در آسیا نداریم؛ بعد از جام جهانی در کنار لیگ حتی می‌شود جام حذفی هم برگزار کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/132453" target="_blank">📅 00:16 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132452">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
مرتضی فنونی زاده پیشکسوت پرسپولیس:
❌
آقای تاجرنیا از اسمش معلومه پولدار، بابای منم تاجر بود، ولی آخراش، تاش رفته بود جرش مونده بود
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/132452" target="_blank">📅 00:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132451">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">⚡️
⚡️
⚡️
برکناری با چند هفته تاخیر
❌
قطع همکاری محترمانه پرسپولیس با کرمانشاهی
⚡️
⚡️
فرهیختگان: یکی از انتصاب‌های عجیب رضا درویش در دوران مدیریتش در باشگاه پرسپولیس صدور حکم مدیر اجرایی برای رضا کرمانشاهی با رقم قرارداد قابل توجه بود. جالب اینکه کرمانشاهی فقط…</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/132451" target="_blank">📅 23:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132449">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa86d2930.mp4?token=DAEtD7nlTYKhyLiRuJE--SvYsz6_0Q22RnOC6OIu_DtWHCL1FKV5kLfH4t376lArn8YrbWJpDCT-j2nfwrC49ZUsOsp149lijYcvWelioyyIAuBs92BKIkcETgYjYLoiUfy6rmDauDft3H-Q4uL4bQFwxHv_tydsqQyE1CqvvdaB5Of9o1O_eAzqD9NJR5wKmSwDiAvVyHt4h9i8v-JjMGQ2QpZ8Z3xHgPsXLg3Hi1JiwfgdvGh_GPjroVdblDmo3uf-lyOpkSFsmQK_RBHWhQ37BzIidD6CaV4jlWn0E_M_lmZVBss1EkWo7q85FZ8rztCS9pVAKTOjSrsa5PN22A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa86d2930.mp4?token=DAEtD7nlTYKhyLiRuJE--SvYsz6_0Q22RnOC6OIu_DtWHCL1FKV5kLfH4t376lArn8YrbWJpDCT-j2nfwrC49ZUsOsp149lijYcvWelioyyIAuBs92BKIkcETgYjYLoiUfy6rmDauDft3H-Q4uL4bQFwxHv_tydsqQyE1CqvvdaB5Of9o1O_eAzqD9NJR5wKmSwDiAvVyHt4h9i8v-JjMGQ2QpZ8Z3xHgPsXLg3Hi1JiwfgdvGh_GPjroVdblDmo3uf-lyOpkSFsmQK_RBHWhQ37BzIidD6CaV4jlWn0E_M_lmZVBss1EkWo7q85FZ8rztCS9pVAKTOjSrsa5PN22A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤍
ریکاوری ملی پوشان پس از پایان دیدار با گامبیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/132449" target="_blank">📅 21:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132448">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVBS1qq1lDOkjU_4nGtfod6Zn1KwJqE8T4p_SISuK-SKBsAiZfNkFO1BQ2l-UONIe55SDkjaIf16_LTV2UnOY41xmi1PzkuHYyNePUv8Lxa-IaDBfjcd4PQ6kcJHU-YWscqn9vnpxs-e7Vc3Q6ZuaW09wjdKfv_A7yHeSpbTWy1XZTWxhYB2t3IxC4GVUPg0TdIw_ElxiZO7XsFBmqIKFKSDtfzGkQ-SpTs19u1SGDbC_xhN_SOBqcQVDhnbqZYPB67V7_3X7B2Vxx3gTMe2GVgAb_NQoa5wwqEhk5mfDHoi-LJJJX2nxA_QWOkvQSxssxY_FB-Nhza8bb8iYcR3ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚡️
هر مسابقه یک فرصت، هر انتخاب یک هیجان!
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
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
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/132448" target="_blank">📅 21:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132447">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e547127cf5.mp4?token=poJczfp87naClicpeyA7ZJ5n9p2ARYkybf2BcWM89TLFglpe_h_R_cqtLWFgd7hUfHQ7UPQLqmG-BOrzFzYkOVJHvr-WN1Tica3JRxy5EPY1LoiKESLUmjXj5-uqsvVv8PVpzQyuKNBI9YodZAAJvACA3snhBKlscFIQyVWx4iwgEY4sX6Tg-rsz8PGxccT3Tnf72gVGvaRQLzuxNV_rk8spfb0Va9hfJSsdsQ09vqOtKTX3Nj_-z3kU-diPsvrH1UQmGp1KiOalmoBLSqWKmefphLvxGXwcAisKCN7vEtD7L-erS2Zf963_hBCIihinYvBPM2-ALd8TNPvey2AtdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e547127cf5.mp4?token=poJczfp87naClicpeyA7ZJ5n9p2ARYkybf2BcWM89TLFglpe_h_R_cqtLWFgd7hUfHQ7UPQLqmG-BOrzFzYkOVJHvr-WN1Tica3JRxy5EPY1LoiKESLUmjXj5-uqsvVv8PVpzQyuKNBI9YodZAAJvACA3snhBKlscFIQyVWx4iwgEY4sX6Tg-rsz8PGxccT3Tnf72gVGvaRQLzuxNV_rk8spfb0Va9hfJSsdsQ09vqOtKTX3Nj_-z3kU-diPsvrH1UQmGp1KiOalmoBLSqWKmefphLvxGXwcAisKCN7vEtD7L-erS2Zf963_hBCIihinYvBPM2-ALd8TNPvey2AtdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
#فوری
| رسانه اسرائیلی:
🔻
ایالات متحده و ایران در آستانه امضای توافق هستند
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/132447" target="_blank">📅 21:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132446">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
تیمه گروهبان از گامبیا گل خورده و عقبه.گامبیا با ۱۵ بازیکن اومده
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/132446" target="_blank">📅 21:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132445">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
علی علیپور پس از پاس گلی که به مهدی طارمی داد به سمت قلعه نویی رفت و او را در آغوش گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/132445" target="_blank">📅 21:03 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132442">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be1699b581.mp4?token=IOkr9iWrFCNf8f7sSuMYYYAnUwC1XmPe2XRVirFDmpZhsTXwG_O-0tTxhsvgNHwAfYS3pGBR8qqiJVAHmMAdjbXOVp4KirT9linI2uZ-UI019z4X3-a96l4j6wXpxhfd0kMX5vqFjACUv7rtnKSluQwXqXFDJgCuB3SEl_Wb5Bw3_KLwmq892W8djHvRxKPKbEKrIrSl3_CBduB5-tT7Xr1sILwU3w6xHpp2tBhant_QEESNfnI8x79N5yeZb4NxJTdaa-tD8uEfMR43Xu3s0fEtvEBcYYIHZGgLk0ErjwSSrGrFRfYswdt77Nxu4ZMwInYH2dGK6yMRtJ7bZAkugw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be1699b581.mp4?token=IOkr9iWrFCNf8f7sSuMYYYAnUwC1XmPe2XRVirFDmpZhsTXwG_O-0tTxhsvgNHwAfYS3pGBR8qqiJVAHmMAdjbXOVp4KirT9linI2uZ-UI019z4X3-a96l4j6wXpxhfd0kMX5vqFjACUv7rtnKSluQwXqXFDJgCuB3SEl_Wb5Bw3_KLwmq892W8djHvRxKPKbEKrIrSl3_CBduB5-tT7Xr1sILwU3w6xHpp2tBhant_QEESNfnI8x79N5yeZb4NxJTdaa-tD8uEfMR43Xu3s0fEtvEBcYYIHZGgLk0ErjwSSrGrFRfYswdt77Nxu4ZMwInYH2dGK6yMRtJ7bZAkugw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
مصدومیت شدید کنعانی در جریان بازی با گامبیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/132442" target="_blank">📅 19:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132441">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‼️
🎙
سامان آقازمانی، بازیکن پیشین پرسپولیس:
‼️
اصلا دوست نداشتم جای بازیکنان تیم ملی باشم. راست بری، با دولت درگیری. چپ بری با مردم درگیری. بی‌طرف هم بخوای باشی بهت تخم‌مرغ میزنن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/132441" target="_blank">📅 19:49 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132440">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
گامبیا حریف ایران فقط با ۱۵ بازیکن به آنتالیا آمده است!  در بازی دوستانه هم به ما توهین میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/132440" target="_blank">📅 19:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132439">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
ترامپ: دستور دادم از این لحظه محاصره دریایی ایران پایان یابد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/132439" target="_blank">📅 19:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132438">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
ترامپ: دستور دادم از این لحظه محاصره دریایی ایران پایان یابد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/132438" target="_blank">📅 19:27 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132437">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
ترامپ: ایران باید قبول کنه هیچ‌وقت سلاح هسته‌ای نخواهد داشت
🔴
تنگه هرمز باید فوری باز بشه و عبور کشتی‌ها بدون هیچ محدودیتی انجام بشه. هر نوع مین دریایی هم باید کامل جمع‌آوری یا نابود بشه
🔴
کشتی‌هایی که به خاطر محاصره متوقف شدن می‌تونن برگردن به مسیرشون و…</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/132437" target="_blank">📅 19:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132435">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
ترامپ: دستور دادم از این لحظه محاصره دریایی ایران پایان یابد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/132435" target="_blank">📅 18:47 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132434">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❗️
شبکه ۱۵ اسرائیل : به نظر می رسه ترامپ با یادداشت تفاهم با ایران موافقت کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/132434" target="_blank">📅 18:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132433">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❗️
ترامپ: محاصره دریایی ایران از همین حالا برداشته خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/132433" target="_blank">📅 18:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132431">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
ترکیب بهترین تیم جام‌جهانی برای دیدار دوستانه با یه تیم ناشناخته اعلام شد.   علیرضا بیرانوند، علی نعمتی، حسین کنعانی‌زادگان، احسان حاج صفی، آریا یوسفی، سعید عزت‌اللهی، امیرمحمد رزاقی‌نیا، امیرحسین حسین‌زاده، محمد محبی، مهدی طارمی و کسری طاهری
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/132431" target="_blank">📅 18:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132430">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
ورزش سه: باشگاه پرسپولیس تو نقل و انتقالات تابستانی دو هدف داره: یکی پوست‌اندازی و جوان‌سازی ترکیب پرسپولیس و دیگری اضافه شدن چند ستاره مهم و تاثیرگذار برای بستن تیمی در حد کسب قهرمانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/132430" target="_blank">📅 18:30 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132429">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
🔴
🔴
و تمام
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SorkhTimes/132429" target="_blank">📅 18:29 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132428">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
آکسیوس: ایران و آمریکا در حال حاضر به توافق رسیدن و فقط تأیید نهایی ترامپ باقی مونده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/132428" target="_blank">📅 18:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132427">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
ورزش سه: باشگاه پرسپولیس تو نقل و انتقالات تابستانی دو هدف داره: یکی پوست‌اندازی و جوان‌سازی ترکیب پرسپولیس و دیگری اضافه شدن چند ستاره مهم و تاثیرگذار برای بستن تیمی در حد کسب قهرمانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SorkhTimes/132427" target="_blank">📅 18:10 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132426">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
فارس: مدیرای پرسپولیس منتظر تعیین تکلیف رقابتای لیگ هستن و هیچ فعالیتی در نقل و انتقالات انجام نمیدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/132426" target="_blank">📅 18:03 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132425">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
ترکیب بهترین تیم جام‌جهانی برای دیدار دوستانه با یه تیم ناشناخته اعلام شد.   علیرضا بیرانوند، علی نعمتی، حسین کنعانی‌زادگان، احسان حاج صفی، آریا یوسفی، سعید عزت‌اللهی، امیرمحمد رزاقی‌نیا، امیرحسین حسین‌زاده، محمد محبی، مهدی طارمی و کسری طاهری
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/132425" target="_blank">📅 17:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132424">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
تیم ملی قراره امروز ساعت 19 با یکی از تیم های قَدَر فوتبال جهان بازی دوستانه برگزار کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SorkhTimes/132424" target="_blank">📅 17:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132423">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🎙
🔴
محسن بنگر: وقتی که نمی‌تونیم حتی تیم های اماراتی رو ببریم چه اصراری به حضور تیم های ایرانی تو آسیا داریم؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/132423" target="_blank">📅 17:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132421">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
🚨
🚨
🚨
فووووووووووووری
🚨
سی‌ان‌ان: در این هفته خبر رسید که ایران با آخرین پیش‌نویس پیشنهادی موافق است؛ دونالد ترامپ به مشاوران خود گفت که برای تصمیم‌گیری درباره امضای این توافق احتمالی، چند روز وقت می‌خواهد.
‼️
به گفته یکی از مقامات، به نظر بعید می‌رسد که ترامپ…</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/132421" target="_blank">📅 16:03 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132420">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
شبکه العربیه از منابع مطلع:
🔴
جمهوری اسلامی میخواد اورانیوم غنی‌شده‌ش رو به چین بفرسته، به شرطی که چین تضمین کنه این مواد رو به آمریکا تحویل نمیده.
🔴
به گفته این منابع، خیلی از نکات مربوط به برنامه هسته‌ای جمهوری اسلامی تو مذاکرات الان حل و فصل شده.
🔴
بر…</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/132420" target="_blank">📅 15:59 · 08 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
