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
<img src="https://cdn4.telesco.pe/file/Y1vCteMF11s8z2NFCHn0gQ6IRjZ51z3SDapg3xHYOuTO-QhwOdnIHSEtwOuULCNvNSXxIptThSDBaWRG5f718dJp1B_D7aD0f4qBZJNKCqFltonVNWeBuNJ1Rov3Ki0gNAi2KF768mZw1zBVE6hQaFcKN63_JQCaEdd-l2ItDpNg_lVXOc2P2JxIDsy4LJ0_wbegnxacjz-T6qD6EAlSSV0NAMjbxTSeo99yGg8Kgrb5IoiIJYj9hXCuaUSDDhT3hdXEB1gmTIBsRGXSAD9kuz78GB-3LpEN_3rFcUQNrxO8h2o8Z9EJg6sStfLdPeF2qL7ZYaWiD60jUzvoBN4h_w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.8K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-05 21:10:54</div>
<hr>

<div class="tg-post" id="msg-132267">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
💢
🇮🇷
🤝
🇺🇸
📰
الجزیره به نقل از یک منبع آگاه: میانجیگری قطر به توافق آمریکا و ایران بر سر دارایی‌های مسدودشده تهران منجر شد!
🚫
به لطف توافق بر سر این موضوع که برای ایرانیان از اهمیت بالایی برخوردار بود، احتمال قوی وجود دارد که توافق میان آمریکا و ایران فردا اعلام…</div>
<div class="tg-footer">👁️ 531 · <a href="https://t.me/SorkhTimes/132267" target="_blank">📅 20:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132266">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
وزارت ارتباطات:
🖍
اینترنت گوشی های همراه هم تا ساعاتی دیگه وصل میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 564 · <a href="https://t.me/SorkhTimes/132266" target="_blank">📅 20:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132265">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‼️
‼️
وضعیت اتصال اینترنت بین‌الملل کشور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 815 · <a href="https://t.me/SorkhTimes/132265" target="_blank">📅 19:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132264">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZYoAZmSDXTRvju4smjyZVri3RFgNw7dZhAIxOFdiTv8DjiHmU0axuiodJ0acRu_y9_mtnxEGXvdkgcrKPw3ajXTX4T7erFQCi5_KvnWKGJbCz-g2Vis9iYm_xL4K_UVgAA4Ok3uoK6THtzueUFqveoRa7W4qT5daZABqH7AXhNUOZ0MIwnjG40fYbbzPG5yNxCmGwd6xL77HkM90-RwlYilF2TQ_PVHwaNxkcEQnlZlZHiedA22Ype7AeXu75xYr-uJ6S2szn1utiLkdVSfPaUYiCWLrzgX_TO_joMlO8nbhwh3ocza-1XyLtneIMOPgvOrTJI4NDCRCepJWjCG4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‼️
وضعیت اتصال اینترنت بین‌الملل کشور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 864 · <a href="https://t.me/SorkhTimes/132264" target="_blank">📅 19:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132263">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔽
وزارت قطع ارتباطات:اینترنت همراه، امروز (سه‌شنبه ۵ خرداد) وصل می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 872 · <a href="https://t.me/SorkhTimes/132263" target="_blank">📅 19:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132262">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❗️
تسنیم : یحیی گل‌محمدی به جز باشگاهای عراقی یه پیشنهاد مالی خوب هم از تراکتور داره و ممکنه بره تبریز!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 893 · <a href="https://t.me/SorkhTimes/132262" target="_blank">📅 19:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132261">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EzM_glBF7r-rjWvQgmF1L2z-yse1H7XVkoFg0t38q4PGyF-VDxUzzaG0kSVhzTSdvAM3qjwCLANWyhPGWXY3pxrwvK1mJaFWVrv75QzPlXyHaprdDABU54U6fRHWr9yfuEh0numC9DzHsm-GyV_z0fqyhTkT4gE3KxLoziZPcIH8PUgdFnfrEePzMm77PgoKUcdRZVWFExARI0MQ7HvwUT_hzGMGhY7D7yLytfR9k8xgdNRXDnH7eZcaHPDUab9RnPlIBFCwEsykDV5ooBAI2EwSDJzRw_PImR9QS82OmEfeEX2blBk5rg5hCDnhjYk_qobl7ov9lcMf5EOaYnqwQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شایعات
🔴
مدیران باشگاه پرسپولیس با درخواست ویژه اوسمار با مهدی هاشم نژاد ستاره تراکتور وارد مذاکره شدند
‼️
قرارداد این بازیکن با تراکتور به پایان رسیده و هم اکنون بازیکن آزاد است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/SorkhTimes/132261" target="_blank">📅 17:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132260">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e786c6b741.mp4?token=dLP5SperzBiJ-Y2kU4jyrK4rpBLUbFgtJpF2WWj3KXv4PTmIZVAICikZk8ZqS-rt5lJ3jrKnfRFeE9uO8qGcUZnrtirtkoCkfUORw_7Ef2kCUZBYw-Wr1qhSd-fUFCaR6orwnioOevWT-EpmK_HjGoTjtayyHykEu8ioBNkqy3hlRK6K5epN6ImozR_bFtZFEp2KgIvhvM9OCm0FMxvKD2vUH4YAwp1EC7zu9O1J7gaNvNoA2WutUMyEsCFOua0-8mPp5BiVaAq9z0YOQ3VLvKGNqeGPLI3iBndHumpZx-g7_EnQT50qGaVCXRb3uPDo9eRt-9bzmZaZM4XkYLYXWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e786c6b741.mp4?token=dLP5SperzBiJ-Y2kU4jyrK4rpBLUbFgtJpF2WWj3KXv4PTmIZVAICikZk8ZqS-rt5lJ3jrKnfRFeE9uO8qGcUZnrtirtkoCkfUORw_7Ef2kCUZBYw-Wr1qhSd-fUFCaR6orwnioOevWT-EpmK_HjGoTjtayyHykEu8ioBNkqy3hlRK6K5epN6ImozR_bFtZFEp2KgIvhvM9OCm0FMxvKD2vUH4YAwp1EC7zu9O1J7gaNvNoA2WutUMyEsCFOua0-8mPp5BiVaAq9z0YOQ3VLvKGNqeGPLI3iBndHumpZx-g7_EnQT50qGaVCXRb3uPDo9eRt-9bzmZaZM4XkYLYXWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▪
︎با این وضعیت اینترنت،
ربات تلگرام وینکوبت
خیلی کاربردیه چون براحتی وارد سایت میشی.
▪
︎هم ثبت‌نامش سریع انجام میشه، هم کازینو رو داخل خود تلگرام میتونی بازی کنی و عملاً کل سایتو داخل ربات داری.
▪
︎پیش‌بینی، بازی، واریز، برداشت و همه‌چی همونجا انجام میشه و خیلی روون‌تره:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/SorkhTimes/132260" target="_blank">📅 17:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132258">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
پس از ۸۸ روز قطعی و ثبت رکورد تاریخی ۲۰۹۳ ساعت انزوای دیجیتال، نت‌بلاکس لحظاتی پیش تایید کرد که اتصال اینترنت در ایران در حال بازگشت است.  وضعیت فعلی در یک نگاه:
🔹
اینترنت خانگی و ADSL: اکثر شرکت‌ها وصل هستند.
🔹
اینترنت TD-LTE: ایرانسل و مبین‌نت وصل شدند.…</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/SorkhTimes/132258" target="_blank">📅 17:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132257">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
تیم فوتبال دهوک عراق به یحیی گل محمدی پیشنهاد داده اما یحیی میخواد تو ایران مربیگری کنه!/فارس
🚮
امپرور جان لطفا هر گورستونی میری طرف های خیابون شیخ بهایی آفتابی نشو…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/132257" target="_blank">📅 17:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132256">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
دوستان از برخط به online شدنتون مبارک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/SorkhTimes/132256" target="_blank">📅 17:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132255">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
دوستان از برخط به online شدنتون مبارک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/132255" target="_blank">📅 16:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132254">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❗️
خوشحالیم که دوباره آنلاین شدید
❤️
🔴
خوش برگشتید؛  امیدواریم تا شب دیتاسنتر ها هم متصل شوند تا کسایی که وایفای خانگی هم ندارند به اینترنت متصل شوند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/132254" target="_blank">📅 16:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132253">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
نت بلاکس:
🔻
نمودار زنده نشان‌دهنده بازگشت نسبی اتصال اینترنت بین‌الملل در ایران است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/132253" target="_blank">📅 16:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132252">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QAvmKOMUi5gtTOEwti97bg1QXFkU9xgoPjcBBJdkFpxk4OubldzCrgMH-Icb1NiP5jT5jz4KoRDqCOe9bIK2nq_4a_TQiVy771SvuVbRehz_b407noTzj6byHe2nHDTukYB4OgTOHLPw1vqjh3FRhxXV44dhVz00IhCJqU0xPJb9lvV3OlSzX_3Pfl4k69MK5OVEMq-g9GMg2PFRyxiuTbS6I739T-q0pD7YAKxoMPjnftHVeiqcsaBwXZYAtgkW9cchAa8TXEJSZv_KuSazzmg1ChJAUAGeGfzTPPO2nJWcJ7mJ7ieLp9OeXaMp9-PkTDRbTCj0Mn5L56y31ELeJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نت بلاکس:
🔻
نمودار زنده نشان‌دهنده بازگشت نسبی اتصال اینترنت بین‌الملل در ایران است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/132252" target="_blank">📅 16:36 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132251">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❗️
خوشحالیم که دوباره آنلاین شدید
❤️
🔴
خوش برگشتید؛  امیدواریم تا شب دیتاسنتر ها هم متصل شوند تا کسایی که وایفای خانگی هم ندارند به اینترنت متصل شوند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SorkhTimes/132251" target="_blank">📅 16:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132250">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‼️
خبرنگار «انتخاب» دقایقی پیش کسب اطلاع کرد که ۴ نفر شاکی حقیقیِ «توقف اتصال اینترنت بین‌الملل» هستند. این ۴ نفر که گرایش سیاسی آن‌ها کاملاً مشخص است و تحت راهبری یک مقام ابقا شده‌ی دولت رییسی، دست به شکایت زده‌اند، عبارتند از کامیار ثقفی، رضا تقی پور، رسول جلیلی و محمد حسن انتظاری!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/132250" target="_blank">📅 16:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132249">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIbpjCwre3tAz3Q5jV_Nu9JCHXfI4N_mekaT3UMCSjf2BDFfki-A07UjziA1tLT2YQmuquJG0PKQURRm6fVGV-MHpKM7jBOJxXoEoiyH43JQgZ3vuk_ETgqboo65elC2AEAHzU1qvBFpxbAw8nFHbNdigvi8fgiqTSNDMvLTeqQi_AUMR_gUqIzuN9tyfJICWtk5aDmMZ3ob8hxdo3aAQP_gSzZT5sjMDK-KTKKm1_ws_8IwNSWVSQ39m87jZUiD3_St-D93nsP0vkQdDZ1LO3Ul7HSSxPzX6dsRUGZPRWBUfn1mRUxJfPFIGRYxDjSTbBsL6_dZ1NJDMYpxAgoaxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
بازگشایی اینترنت به دیتاسنترها رسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/132249" target="_blank">📅 16:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132248">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
نت خونگی وصل شده .تست بگیرید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 996 · <a href="https://t.me/SorkhTimes/132248" target="_blank">📅 15:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132247">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
دستور وزیر ارتباطات برای اتصال اینترنت صادر شد؛ اتصال جهانی ایران از همین دقایق احیا می‌شود؛ اتصال کامل مردم تا ۲۴ ساعت آینده
🔺
معاون سیاست گذاری و برنامه‌ریزی توسعه فاوا و اقتصاد دیجیتال وزارت ارتباطات، در پی دستور رییس جمهور از بازگشایی تدریجی اینترنت…</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/132247" target="_blank">📅 15:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132245">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlNSEXBSWmg4gZQKEdP7ApEbiU4YJuk4Ed23ALo4fvPDPtH6SMjexZpMcVtcGUiuPAcokMaWXVkFbalEKMHiRvtvj3lH3o5joRxiBEqj43aEJB_WAsGVD6Zax4naeoDjzYzB4jb4Rl4-Mrvhqp2St6NkNjS7alJpu2FXp_Zz46hYYL_9PpMFQw1fA8D412yKKbpwgxp6Fujp7ALHs0R8-nTijC3y-2YUbYUr9SxtYr4LmZSZGBMxqI9W444r56fy0yp4o7-sH3fe74yQoy-s1hFcRbBZZZ_TSAFTHMGpf3Q2qv72Xm0R-9M1sL-_VRyfDIi7iu5lPJiUB_d-rU2eVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
فسخ لیموچی با سپاهان؟
▫️
به احتمال فراوان مهدی لیموچی به دلیل عدم گرفتن دستمزد خود در سپاهان با این تیم فسخ خواهد کرد و مقصد احتمالی وی پرسپولیس خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/SorkhTimes/132245" target="_blank">📅 13:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132244">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
دستور وزیر ارتباطات برای اتصال اینترنت صادر شد؛ اتصال جهانی ایران از همین دقایق احیا می‌شود؛ اتصال کامل مردم تا ۲۴ ساعت آینده
🔺
معاون سیاست گذاری و برنامه‌ریزی توسعه فاوا و اقتصاد دیجیتال وزارت ارتباطات، در پی دستور رییس جمهور از بازگشایی تدریجی اینترنت تا دقایقی دیگر خبر داد و گفت:
🔺
دسترسی کامل مردم به اینترنت تا ۲۴ ساعت آینده میسر می شود. بر اساس اعلام یک منبع مطلع، برخی سرویس‌ها و پیام‌رسان‌های بین‌المللی نیز به‌تدریج و در چارچوب فازهای بعدی بازگشایی شبکه، در دسترس کاربران قرار خواهند گرفت و در فاز اول بازگشایی قرار ندارند.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/SorkhTimes/132244" target="_blank">📅 13:29 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132242">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c57ee64b0.mp4?token=dOmEarbhqNlWXvTnscBLD9OLgWZi6I1NonxLDxcchmBs4DQLgdbHS1NFCDcZPYMHpOp_O3BE6tqneAL8jNpYoWHd34GvAEp1xow-xm_zA2u-dVfIfZ4pUPDTfbNWV5oDYHw3Xguxx4ek-SELJOAKcJgyHDUL1mYYFoJpwNgsHxhxHNma56DQr4WqFO-RbD7WPyufze11nz6hLk5s6s3zCyel06Y3ACjkOZaGyDJsV7PdJHPTkHBo3VYGHKJLft0TkLXkEEnPl9mwExfqwlRa9ai4vUaS6kPjgTL3uapDH9POSrD5DDDquMEwqvbaq4EEq3TNTlRUCVp2avTE4uX-QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c57ee64b0.mp4?token=dOmEarbhqNlWXvTnscBLD9OLgWZi6I1NonxLDxcchmBs4DQLgdbHS1NFCDcZPYMHpOp_O3BE6tqneAL8jNpYoWHd34GvAEp1xow-xm_zA2u-dVfIfZ4pUPDTfbNWV5oDYHw3Xguxx4ek-SELJOAKcJgyHDUL1mYYFoJpwNgsHxhxHNma56DQr4WqFO-RbD7WPyufze11nz6hLk5s6s3zCyel06Y3ACjkOZaGyDJsV7PdJHPTkHBo3VYGHKJLft0TkLXkEEnPl9mwExfqwlRa9ai4vUaS6kPjgTL3uapDH9POSrD5DDDquMEwqvbaq4EEq3TNTlRUCVp2avTE4uX-QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
کانفیگ فروشا وقتی از خواب پا میشن و تلگرامو باز میکنن که خبر هارو بخونن:
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SorkhTimes/132242" target="_blank">📅 12:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132241">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
وزیر ارتباطات: با دستور رئیس‌جمهوری و پس از برگزاری ۳ جلسه فشرده کارشناسی، فرایند بازگرداندن اینترنت کشور به وضعیت قبل از دی‌ماه ۱۴۰۴ آغاز شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/132241" target="_blank">📅 11:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132240">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
وزیر ارتباطات: با دستور رئیس‌جمهوری و پس از برگزاری ۳ جلسه فشرده کارشناسی، فرایند بازگرداندن اینترنت کشور به وضعیت قبل از دی‌ماه ۱۴۰۴ آغاز شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/SorkhTimes/132240" target="_blank">📅 11:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132239">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OY5vFtZs0VTeohX8w68gPyg-F2yyYmDm4-bUsvQQgABZSou8fZdMAwL3GR4-a0ixoQLkTkV7fDBksWC3hmJ5_8NZxzCSO4TutHxCNaOTVqHNJ4WXI08EudojFbrhqHHiQ8m1ZTP54cHsqZHBXLSlo9ERy0YSmpC18asEDlCW46Qc6lzvHmmhNVIYBmpRcNvID9MrTfEQ4pJTNm-s-RdzYtPKFJpOmimUO5_nd86GYaTS_SoGNqdkNqfTbLlYiuIK9skQVFMGDw6hyRBUQiiNlrWexDwiKU8Liyz7xaDEne3fSs6pBTKmGqLcpV0waQ3iMMzRC5guchqZzkt2I3RsVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسبت به دیروز وضعیت اینترنت بهتر شده و از ۲ درصد به ۳ درصد رسیده
😂
خوب نتیجه میگیرم در آستانه بازگشت نت هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/132239" target="_blank">📅 11:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132238">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❗️
ایسنا:   دستور باز شدن اینترنت از فردا اجرا میشه
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SorkhTimes/132238" target="_blank">📅 10:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132237">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
شهاب زاهدی قرارداش را با باشگاه آویسپا فوکوئوکا ژاپن تمدید کرد و خبر از بیخ گوشمون گذشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/132237" target="_blank">📅 10:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132236">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VwsxEyo4tkmvrb1Obqc6UKXoJ4ln_GaEaD2neeMzU9yp_FFB0A7TXgcVO037EP46QuK_Dtprmu4QO_Ia0agqxq_OJNlfjF5btFd2PiyFV90I7QmO8pXp8rmyZaffdBGkVBJfs1R5CixQvgFIlX-hBChkxa-S-jDpqRVcAcJZelp4ak6UX7kt-nGS7bCH3LbvTQVMiKk_hB9rxgpZKS5BXFwrEIffzS3uEKOPS_1JHyw3Wol9j7Sg046VdnwCDd7XvoFel2JS0kRrVYQPHKrB6R7XhiYNv9GHgFZHLMePLzTMaIBDod5e7s_yUJKPydoU7OMw_lNGJzQAHK_U6lc24w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا ساعاتی است جیمیل در دسترس کاربران ایران قرار گرفته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/132236" target="_blank">📅 10:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132235">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWoChoVm-IxyaS0dEl1d9Hn_1ajmQqUPZAcNOkHXR-NOMwOzlNFOy_c63D85kWB9dtgCXQVLxDMlkqaNFTHQ7S4s3oNPlOwmPSS79JNiEplvg9nu2kyRd1cnfB2-4pqaquXtfBrfJZa2yZ14M6Xf_nrR8C5tQW-XNiawlVEa7AIzOZfGLIkL4Fq5EnmRsEpxcwsmzHlD8ecQ3dZAw6OBJxOKHd9sgUyt2Dw0lQDrlCWIqO36v-yAvYi3tLRT0tc87iw0q0091QkE1qGSyip1t9J7qZOt708hZzsUcShibHrj4aC9DZAsbz0r7ySsQWU0ICA1g18XOAjQ6jcsY-At5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
صفحه اینترنت پرو از سایت همراه اول حذف شد
✅
شکست رسمی اینترنت پرو
همراه اول صفحه ویژه اینترنت پرو رو حذف کرد
✅
روسیاهی موند به اونا که خریدن
🖕🏾
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/132235" target="_blank">📅 10:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132233">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYGIXtfVztE9iosOWc9N21y_ezqoB6UfgsPnSV3gnmyuq6LPfWOhQE9ZBBF0nNlC5DOyaexVQU_U1UnKXfuAskc91_U2ony1gOqd2LCFvgw53IkZ6sCXh_SiP-dQ_FbAR0JCj2n6WnyuuL9Z79bZLKLyWwKhdvwttg2ggwO8jzqra1yjmGF4Ycq43-x-9GfYrcY2sl4uIOONzSDTvl29JAEuN-aYhMEmqSXdV9sBw6TGBfUsaFyZfqa3TeFERWYvTkaaO7kuDFr_DdNt3s0q89cbBSZY4snyniGJMAJSMtGrVCAJfRWNqI_sRUOlxZWrHu3hIYPRfS6fMGFG8nA-Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
از بین شهریار مغانلو و علی علیپور؛ یکنفر از لیست نهایی تیم ملی برای جام جهانی 2026 خط خواهد خورد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/SorkhTimes/132233" target="_blank">📅 10:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132232">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❗️
ایسنا:   دستور باز شدن اینترنت از فردا اجرا میشه
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/SorkhTimes/132232" target="_blank">📅 10:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132231">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBoM0Ujj88IHblLuDPekA7bt1DILRx3qCaagKxbIR9M5i0gjva1uEKdDmJ9k-i9saF37T9n1sQeRXt-i3mPdpRfO5utcL2INlcSozlSZ2Ik2D2_N2uG48vjaW8070jkY32BAIdEckOlqDJmueOWbcbyDd0rpj3bnDhrPumupeNUZeSNIx759-WcRmgbQpvEhXfKjzRmdQdz5NT6qrOW0_mGWTaD5aZc5PYr_Aqie3w2_MVoSoD-Au9LsUaqh-oG5SY_lj8y6UbpGqnmFW3jfpV4j4pHTlFj5LGfzf3sBAkJsW1_9nCYThY1ZZl8PZ97A2BDe058xkO2p-zylV_D-bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ارزش امیرحسین محمودی ستاره ملی پوش پرسپولیس به 500 هزار دلار رسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/SorkhTimes/132231" target="_blank">📅 09:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132230">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rn_O8cdA6HbfauQT-JKJpZKu0JMDYaDUynRgvxN-EnHAdl_VlVmybB57fXRLzJfMn1detDaycq6dDOIGG8bsGUWmUgrorumNVk_QJh7ZTkdlw32UDqXtq4-HKxsS1OCRsMYQieqcVnTjAUko38Wy72Bbk6kbrk82XNrPqvd5Ff4souUniVFtMkdg5_Ec9cl_9t3rKdqfn5ixXqmbmnMQ7YqBiOGU4TjdoS92JB5KsJzizrKlk8JALbZooxgyeqFx8CpHvGMZ0oOM-fx-G363chPdRXVOLq32k7kZ5IHiSt5SdHiLW9vTJXIQ0Ro9JYWXNPz1x0GB_sIVmfZ1u11bhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
شایعات حاکی از این داره که سردار آزمون به زودی به تیم ملی برمیگرده....!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/132230" target="_blank">📅 09:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132229">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">▪
︎با این وضعیت اینترنت،
ربات تلگرام وینکوبت
خیلی کاربردیه چون براحتی وارد سایت میشی.
▪
︎هم ثبت‌نامش سریع انجام میشه، هم کازینو رو داخل خود تلگرام میتونی بازی کنی و عملاً کل سایتو داخل ربات داری.
▪
︎پیش‌بینی، بازی، واریز، برداشت و همه‌چی همونجا انجام میشه و خیلی روون‌تره:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/SorkhTimes/132229" target="_blank">📅 01:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132228">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a864573491.mp4?token=Z9ThaZi9AyHZXN3ZYnbgG8wJLQcY0Z2ouqGfxO3V9ORPBkP4FqkG9o78cqeVS8S8LEtpLIpX-Ud4U6yFqq2rC9fJkadSpYeFNZwNX3dAEIJJVVco4hs8p8Im-4v_lbMPvA4rbzT0XdJQoHjiUUBT9MViuxzHD3_4Wa-dgO6BFKDJDAZq9pdIbrsSY-UC66n0THngC_6IUlu6KcW6N3fRgjXz4-Bide_Nk_wrOrYfSg8H4gGIYtoPSON8-n6hdthzhaXVyC4rwtrnEpaCddSGAXiIXyfJk7bT7GnJKhNkqAOZ-IscPjBBOrPMh3FL_F2audwSIwL9-6xNoE1uV5GCTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a864573491.mp4?token=Z9ThaZi9AyHZXN3ZYnbgG8wJLQcY0Z2ouqGfxO3V9ORPBkP4FqkG9o78cqeVS8S8LEtpLIpX-Ud4U6yFqq2rC9fJkadSpYeFNZwNX3dAEIJJVVco4hs8p8Im-4v_lbMPvA4rbzT0XdJQoHjiUUBT9MViuxzHD3_4Wa-dgO6BFKDJDAZq9pdIbrsSY-UC66n0THngC_6IUlu6KcW6N3fRgjXz4-Bide_Nk_wrOrYfSg8H4gGIYtoPSON8-n6hdthzhaXVyC4rwtrnEpaCddSGAXiIXyfJk7bT7GnJKhNkqAOZ-IscPjBBOrPMh3FL_F2audwSIwL9-6xNoE1uV5GCTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوری
| ترامپ:
🔻
«اورانیوم غنی‌شده (غبار هسته‌ای!) یا فوراً به ایالات متحده تحویل داده خواهد شد تا به خاک آمریکا برده شده و منهدم گردد، یا ترجیحاً با هماهنگی و همکاری جمهوری اسلامی ایران، در همان مکان منهدم شود،
🔻
یا در مکانی دیگر که مورد قبول باشد، با نظارت کمیسیون انرژی اتمی یا نهاد معادل آن بر این فرآیند و رویداد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/SorkhTimes/132228" target="_blank">📅 01:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132227">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔹
کالدرون: کاش می‌شد کارم را در پرسپولیس تمام کنم
🔴
اگر می‌ماندید پرسپولیس قهرمان می‌شد؟
فکر می‌کنم تیم در آن زمان شرایط بسیار خوبی داشت و ای‌ کاش می‌توانستم کاری را که شروع کرده بودم را به پایان برسانم، اما متأسفانه این اتفاق نیفتاد. به نظرم ما تیم را در مسیر درستی قرار دادیم و یحیی گل‌محمدی هم پس از حضورش کار خوبی بر پایه‌هایی که گذاشته بودیم انجام داد.
🔴
پس به خوبی پیگیر اوضاع پرسپولیس هستید!
در این سال‌ها تغییرات زیادی در سطح مربیان و مدیران باشگاه رخ داده و پرسپولیس همیشه باشگاهی پرتحرک بوده است. بازیکنان زیادی هم تغییر کردند؛ بعضی از بازیکنان مهم زمان من مثل شجاع خلیل‌زاده، مهدی ترابی، احمد نوراللهی و علیرضا بیرانوند از تیم جدا شدند و برخی مثل حسین کنعانی، علی علیپور رفتند و دوباره برگشتند؛ بعضی دیگر مثل محمد انصاری امروز مسئولیت مهمی در باشگاه دارند.
🔴
خبرهای بود مبنی براینکه باشگاه پرسپولیس در پائیز سال گذشته قصد داشت شما را دوباره بازگرداند؛ مذاکراتی صورت گرفت؟
همیشه شایعاتی وجود دارد، اما شایعه فقط سر و صداست. تنها واقعیت این است که در حال حاضر من سرمربی پرسپولیس نیستم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/SorkhTimes/132227" target="_blank">📅 01:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132226">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23f501face.mp4?token=iDnc-694lSnH_1GjyLRiLnsbe_kcsRt0hgpSLch8Gl8xgtpUuLIKnFkWay2xO0CySo0pqKPoy4TgU2cO1NQKwZUTSvcRhOTnaTLRfbxhSOiqxhfkysucidGmtBVWlVLJt6mcbdnBWrPwuJTG1GPAhSdyVeJguPwKtpGRfnhylhYciqKR4OomVfsFXrb9EgbJgmHEDE8YD4MwBtBI9gKpPUCyUnWPqtdUC5_u73q7riB4D2PSUy0buO893WTblux4asS0zf_YtrNiVZ7ASubkE_SK3Yr_hawK4G_jsDwfTesXNjl-U6bhzKdnVH-nDhwQKoq5rCL2kWeL6duX9KMxTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23f501face.mp4?token=iDnc-694lSnH_1GjyLRiLnsbe_kcsRt0hgpSLch8Gl8xgtpUuLIKnFkWay2xO0CySo0pqKPoy4TgU2cO1NQKwZUTSvcRhOTnaTLRfbxhSOiqxhfkysucidGmtBVWlVLJt6mcbdnBWrPwuJTG1GPAhSdyVeJguPwKtpGRfnhylhYciqKR4OomVfsFXrb9EgbJgmHEDE8YD4MwBtBI9gKpPUCyUnWPqtdUC5_u73q7riB4D2PSUy0buO893WTblux4asS0zf_YtrNiVZ7ASubkE_SK3Yr_hawK4G_jsDwfTesXNjl-U6bhzKdnVH-nDhwQKoq5rCL2kWeL6duX9KMxTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
بازگشا سخنگوی باشگاه پرسپولیس: پرسپولیس برای برگزاری مسابقات اعلام آمادگی کرده است هم زیر ساخت داریم هم پشتوانه مالی
🔸
این نمی شود که بعضی تیم‌ها بیایند نامه بزنند که ما نمی توانیم در لیگ بازی کنیم و بعد همین تیم‌ها هم توسط فدراسیون برای آسیا انتخاب شوند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/SorkhTimes/132226" target="_blank">📅 00:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132225">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMdXmY51gZGnwBUu_BlCBRQo_-gxMDt-yrzdKcvCJih-WgS69uOGFNjlx3xOwkIYkhbBvHvXPpbU2Diw5oAUT09UAcYUJFDVnqNhGIKp3QEX5Ph_L2nhRBbD55JsED2VmjAkInWWnX1QraEAp86oWFQyGMp8G_QmFk80IYgfGUFobzYtLhXJ1AK4VLTWUD462CIDa9-jKPpfz8n51QOX2IOftNlemZfvqdPEqxMraPJDv3sgMd6uhQxUDtjdaAEUhBLXDc2JfatLEgKVMH_egcfFn_-nP69DX7-ulaWujn-X-oJ34vit7M_ZhM8licakL2tMYLMx9VdG-Osd_TMdpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق آخرین آپدیت ترانسفر مارکت امیرحسین حسین زاده جای ارونوف رو در صدر با ارزش ترین بازیکن لیگ برتر گرفت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/SorkhTimes/132225" target="_blank">📅 00:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132223">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔰
آف ویژه
سرویس VIP
🔰
1 گیگ 200T
2 گیگ 400T
3 گیگ 600T
5 گیگ 870T
10 گیگ 1.5T
به مدت ۴۸ ساعت
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال و مدت زمان نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SorkhTimes/132223" target="_blank">📅 00:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132222">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">تو بندر عباس صدا توافق میاد</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/SorkhTimes/132222" target="_blank">📅 00:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132221">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
الجزیره:  احتمالا توافق بین آمریکا و ایران، فردا (سه‌شنبه) رسما اعلام میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/SorkhTimes/132221" target="_blank">📅 00:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132220">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">تو بندر عباس صدا توافق میاد</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/SorkhTimes/132220" target="_blank">📅 23:57 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132219">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
سه نمایندهٔ ایران در آسیا مشخص شدند
✅
استقلال، تراکتور و سپاهان ۳ نماینده فوتبال ایران در آسیا خواهند بود. این تصمیم را هیئت‌رئیسه فدراسیون با توجه به جدول کنونی لیگ برتر اتخاذ کرده.
❌
اگر سپاهان موفق به اخذ مجوز حرفه‌ای نشود در آن‌صورت تیم‌های رتبه‌های بعدی…</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/SorkhTimes/132219" target="_blank">📅 23:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132217">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOVix4NULxQoQd4jbhKwQOkVMzrQDqzgZfUFPlqubH3430gYfK2Qu5F9sKB9aNznv85CJ7Pbd8J9AcekSnL9QM-Vg3Is4vB20Yx2Kf_jGzrHYPD-CNnr9B0mEq_sWBI5ZXB8FBkZdQ8oVWT3pmGNYeYQENXYXX88YC27TFKJCUII8yYGbTXxOM_mtE9ysTffhGZ5hBp2TXq8wf3ilsfxt7ZgjcSZrNhZHj9Xnr4WuRUv07fve-cwQSFZ9YAna1LwEsFKxdqm3F-WNC_-j35jLpUnObPpXfTZMCzFB8BQX2f5z76inGcQkFSDGrGmmRrNAOujFjJN4mNp1aq-hKgywQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
پیام‌ نیازمند در جدیدترین آپدیت سایت ترانسفرمارکت با ارزش ترین گلر ایران شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/SorkhTimes/132217" target="_blank">📅 23:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132215">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
👈
نورالدین الدغیر خبرنگار الجزیره: احتمال دارد اسرائیل پیش از هر توافق ایران و آمریکا، دست به یک عملیات نظامی بزرگ در لبنان بزند
🔴
با هدف استفاده از فرصت زمانی باقی‌مانده تا توافق ایران و آمریکا.
🔴
یا برای به شکست کشاندن توافقی که بر توقف جنگ در جبهه لبنان…</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/SorkhTimes/132215" target="_blank">📅 22:56 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132214">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
واکنش باشگاه پرسپولیس به معرفی سه تیم اول جدول به عنوان نمایندگان ایران در آسیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/SorkhTimes/132214" target="_blank">📅 22:34 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132213">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✅
و بلاخره بعد از نود روز وصل شدن نت بین الملل و شاهد خواهیم بود ...حال الان کانفینگ فروش و خریدارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/132213" target="_blank">📅 22:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132212">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1XbCX5XVIxrR06qiLQ6OVCY8XSgHXErEEN0_XRRYDhS0y1I9ZuTU9rwKC7qeAdAcZjwlLRPQb1670yobhVQvdZv1ogRKrxPd2eb6_96pnJFBSJ1G0TKAaG7vvPcG5JGLCqA1lAXI8Wz7n1vsCOngwc1u4qXAS0f0uBZEQK03WfjWas8BWCSxOXN_nwkoBcEKZt5sWRxXH1QlsJkRxlFBo2sKUyMsfk3ZlPfgwQHyHb7OQ9l7aPLng23V8rzz_fMcFXFzYMpeYlkSfrK_NGUejbwtkSqG_J0MctSBY5u_Bf5K1O3hI7fD1ZYY43dt7SBo3nWNLYEXCETGYX5Aqnrxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
واکنش باشگاه پرسپولیس به معرفی سه تیم اول جدول به عنوان نمایندگان ایران در آسیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SorkhTimes/132212" target="_blank">📅 22:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132211">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
🚨
خبرگزاری های داخلی خبر دادند که اینترنت بین‌الملل از فردا به تدریج در سراسر کشور وصل می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/SorkhTimes/132211" target="_blank">📅 22:27 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132210">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
فووووری/ مدیر روابط‌عمومی وزارت قطع ارتباطات خبر داد: رئیس‌جمهور دستور بازگشایی اینترنت بین‌الملل را ابلاغ کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/SorkhTimes/132210" target="_blank">📅 22:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132208">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">▪
︎ اگه این روزا بخاطر ضعیف بودن اینترنت سایتا سخت لود میشن، ربات تلگرام وینکوبت خیلی کارو راحت کرده:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
بدون اینکه از تلگرام خارج شی میتونی مستقیم وارد بخش بازی‌ها و کازینو بشی، پیش‌بینی ثبت کنی و حتی واریز و برداشت انجام بدی.
▪
︎حالت Mini App داخل تلگرامه و خیلی سبک‌تر و سریع‌تر باز میشه:
👇
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SorkhTimes/132208" target="_blank">📅 22:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132207">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
ادعای عاصم منیر:
🟢
توافق ایران و آمریکا در آستانه نهایی شدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SorkhTimes/132207" target="_blank">📅 22:11 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132206">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
فووووری/ مدیر روابط‌عمومی وزارت قطع ارتباطات خبر داد: رئیس‌جمهور دستور بازگشایی اینترنت بین‌الملل را ابلاغ کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/SorkhTimes/132206" target="_blank">📅 21:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132205">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
ورزش سه: پرسپولیس از رقابت های آسیایی کنار گذاشته شد و استقلال، تراکتور و سپاهان (درصورت تایید مجوز حرفه ای) آسیایی خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/SorkhTimes/132205" target="_blank">📅 21:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132204">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
خبرگزاری فارس: مسعود پزشکیان فردا سه‌شنبه مصوبه بازگشت اینترنت به وضعیت قبل از دی‌ماه را امضا و به وزارت ارتباطات ابلاغ می‌کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/SorkhTimes/132204" target="_blank">📅 21:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132203">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
تغییر نظر عجیب فدراسیون فوتبال با پیشنهاد سازمان لیگ
❌
در حالی که طبق ادعای مسئولان ارشد فدراسیون فوتبال قرار بود فردا (سه شنبه) جلسه وبیناری بین مهدی تاج و معاون کمیته اجرایی AFC  برای گرفتن فرصت مجدد برای معرفی تیم های آسیایی برگزار شود، هیئت رئیسه فدراسیون…</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/SorkhTimes/132203" target="_blank">📅 21:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132200">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
باشگاه پرسپولیس برخی نفرات سپاهان  را مدنظر دارد چرا که این باشگاه به بازیکنان گفته نمی توانیم مبالغ قراردادها را پرداخت کنیم ک نهایت پرداختی ما ده تا ۲۵ میلیارد خواهد بود و سقف پرداختی هم برای چند نفر است.
🔴
از  مهدی لیموچی،امین حزباوی و  آریا یوسفی به…</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/SorkhTimes/132200" target="_blank">📅 20:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132199">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
خبرگزاری تسنیم :
🔴
دستور رفع محدودیت های اینترنت بین الملل تایید شده و فقط به تایید نهایی پزشکیان نیاز داره ، در صورت تایید اینترنت بین الملل تا هفته ی آینده به حالت قبل جنگ برمیگرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SorkhTimes/132199" target="_blank">📅 20:24 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132198">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
سه نمایندهٔ ایران در آسیا مشخص شدند
✅
استقلال، تراکتور و سپاهان ۳ نماینده فوتبال ایران در آسیا خواهند بود. این تصمیم را هیئت‌رئیسه فدراسیون با توجه به جدول کنونی لیگ برتر اتخاذ کرده.
❌
اگر سپاهان موفق به اخذ مجوز حرفه‌ای نشود در آن‌صورت تیم‌های رتبه‌های بعدی…</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SorkhTimes/132198" target="_blank">📅 19:49 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132197">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
تغییر نظر عجیب فدراسیون فوتبال با پیشنهاد سازمان لیگ
❌
در حالی که طبق ادعای مسئولان ارشد فدراسیون فوتبال قرار بود فردا (سه شنبه) جلسه وبیناری بین مهدی تاج و معاون کمیته اجرایی AFC  برای گرفتن فرصت مجدد برای معرفی تیم های آسیایی برگزار شود، هیئت رئیسه فدراسیون فوتبال امروز تشکیل جلسه داده و ظاهرا با معرفی سه تیم اول لیگ برای مسابقات آسیایی فصل بعد موافقت کرده است.
❌
این در شرایطی است که هنوز جلسه فدراسیون فوتبال با AFC برگزار نشده و سپاهان به عنوان تیم سوم جدول فعلی مجوز حرفه ای کسب نکرده و پرونده این باشگاه در کمیته استیناف بررسی خواهد شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/132197" target="_blank">📅 19:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132195">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇷
میزبانی مکزیک از ایران
⚪️
«کلودیا شین‌بام» رئیس‌جمهور مکزیک، رسماً اعلام کرد که تیم ملی فوتبال ایران به دلیل محدودیت‌های حضور در خاک آمریکا، در ایالت «باخا کالیفرنیا» مستقر خواهد شد.
⚪️
با تایید دولت مکزیک، تیم ملی ایران شهر «تیخوانا» را به عنوان مقر اصلی و محل تمرینات خود در طول مسابقات جام جهانی ۲۰۲۶ انتخاب کرده است.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/132195" target="_blank">📅 19:08 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132194">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
سه نمایندهٔ ایران در آسیا مشخص شدند
✅
استقلال، تراکتور و سپاهان ۳ نماینده فوتبال ایران در آسیا خواهند بود. این تصمیم را هیئت‌رئیسه فدراسیون با توجه به جدول کنونی لیگ برتر اتخاذ کرده.
❌
اگر سپاهان موفق به اخذ مجوز حرفه‌ای نشود در آن‌صورت تیم‌های رتبه‌های بعدی جدول به آسیا معرفی خواهند شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/132194" target="_blank">📅 19:05 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132192">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
در حالی که فوتبال ایران تلاش می‌کند استانداردهای سخت‌گیرانه کنفدراسیون فوتبال آسیا (AFC) را برای دریافت مجوز حرفه‌ای پیاده‌سازی کند، اخبار واصله از باشگاه سپاهان اصفهان نشان می‌دهد که این باشگاه با چالش‌های جدی در مسیر دریافت این مجوز مواجه است. عدم بارگذاری به‌موقع مدارک و وجود بدهی‌های انباشته، اکنون باشگاه طلایی‌پوش اصفهان را در موقعیت دشواری قرار داده که اعتراض به کمیته استیناف آخرین تلاش آن‌ها برای خروج از این بن‌بست است.
🔺
سپاهانی‌ها اما در حالی به کمیته استیناف صدور مجوز حرفه‌ای پناه برده‌اند که عدم بارگذاری به موقع مدارک توسط آن‌ها کار را بسیار دشوار کرده است. سپاهان که حالا چشم امید به کمیته استیناف دارد، بسیار بعید است با قصوری که انجام داده بتواند مجوز حرفه‌ای خود را از کمیته استیناف دریافت کند؛ زیرا این باشگاه در بازه زمانی مقرر اقدام به بارگذاری مدارک نکرده و حالا کمیته استیناف هم همین موضوع را مدنظر قرار خواهد داد.
🔺
سپاهان که در جایگاه سوم جدول رده‌بندی لیگ برتر قرار دارد، با توجه به اتفاقات رخ داده در جنگ سوم، اکنون با مشکلات مالی نیز مواجه است و باید دید چه سرنوشتی در انتظار این تیم خواهد بود.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/SorkhTimes/132192" target="_blank">📅 17:24 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132191">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❗️
پرشیانا اسپورت : لیموچی دومین بازیکن سپاهان که از پرسپولیس آفر دریافت کرده و اگر شرایط خوب پیش بره ، لیموچی به پر‌سپولیس میرود   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/132191" target="_blank">📅 17:20 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132190">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
نماینده محمد امین حزباوی امروز پیشنهاد مالی‌ مدنظر مدافع میانی سپاهان رو به مدیران باشگاه پرسپولیس ارائه کرده است. درصورت موافق با این پیشنهاد به احتمال فراوان حزباوی راهی پرسپولیس خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/SorkhTimes/132190" target="_blank">📅 16:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132188">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYhda_xqneapcwYC74Y_LCBeRtg7X5Qs2cFQF9-rLGT1pMaU0Y78h83iOKTw86rn0vv8uQw4iP73KK6HGcapCVP404cj4BWEpcLyDOzeatI0DvHkhPUqfKW4MNEscSPRmbd-Ud_wweQcdCuT3z3OYMEVHTU4WP3Z1b-5HANoooEleSBlwM0aUiB1Uy3J8yU38S1lRyE6LMARFJjLhnCCcr3xZonwhOZZKSIc-yEanaDptP-4uRHJd1T7Tx-NAJGGrj4APUyD-3rHbZtI0XZo4Mu5w_DN_3truHnk2EJCESAfHXyJKIc5GZp_FI8eUbI9LCThqEXg1t5sHigXHCnq5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔽
فهرست ابتدایی ازبکستان برای جام‌جهانی با حضور اورونوف و سرگیف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/SorkhTimes/132188" target="_blank">📅 16:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132187">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⭕️
#فوری | خبرگزاری رویترز: مذاکرات در دوحه عمدتاً بر تنگه هرمز و اورانیوم غنی‌شده با غنای بالا متمرکز است
‼️
🔻
رئیس کل بانک مرکزی ایران بخشی از هیئت اعزامی به دوحه برای گفتگو در مورد احتمال آزادسازی دارایی‌های مسدود شده به عنوان بخشی از توافق نهایی است.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/SorkhTimes/132187" target="_blank">📅 16:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132186">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
فاکس نیوز: امروز پزشکیان ، قالیباف و عراقچی رفتن قطر تا درمورد پایان جنگ و توافق گفتگو کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/SorkhTimes/132186" target="_blank">📅 16:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132185">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
فاکس‌ نیوز :   ترامپ برای رسیدن به توافق نهایی ۷ روز‌ دیگر به ایران زمان داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/SorkhTimes/132185" target="_blank">📅 16:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132179">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TyC-yQ6iSzUwmC-luN7Grk12xgg0Mpq0e0Z-meIYYn1SlknaBj3YDK3LkwoXryouahE-DLJxmLN8Jepzw7rC3TCFzbnhlsVaBf1icf6yzTJZZ_fEanJRo9NBreskkRIwv1uwFO1heluS4TKI730QDahmumq-vqp8uGdCCzcWqTI7zw8p9d6Qout1ba05bp9ADCWkmHklJZf0suZy7JJX3fhQIruT0cPwkFd8P-93MrzAHdLg6FKzchV_IjJsHG51IbN54wRkHyHcGK4fHe4S7OQJ3hdj082ns_33iE3e1nOtuT8P1hzMubtr0ebMEnDZiVvSCO5z-OOw7T61RbRzIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پرزیدنت ترامپ : یا توافقات من با رژیم ایران بزرگ و بسیار مهم خواهد بود و یا اصلا این توافقات انجام نخواهد شد و به جنگ باز خواهیم گشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/SorkhTimes/132179" target="_blank">📅 14:25 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132178">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kt7sQx78RWGFEN3sRsdf3-i8GTkznrtNqOVsuzwrYK7FQlcc7W1YGEmKEVM-wuVGJspTcfrIyAqsSQb91-f-Lb8G_tji27fsz1OXgKTiko0jZIdzFQtFNDQRRz2mI88ZhuLGm7O9H9LJP45kAgOYCT9QMgbeM03aptbQI6cY_Blis73j0CBvlyxk-S3IGQxXi4R7IWxubgovRjwVqbD3wI8eav0v9xI-F1ghO4SwUqU_bnOYGiC-FkLdgMVlQredXnYceka_fH4qhqqT62v00-100LbpywpZ7kQrNxVvgMORjTIYNh6pRPBpgpBaKRbbYOG8xwGbCnzY-IGNd7zfTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهدی هاشم نژاد یکی از بهترین بازیکنان چندفصل اخیر فوتبال ایران که توسط قلعه نویی خط زده شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/132178" target="_blank">📅 14:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132177">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8twmTcnIxrRx_yNeeJERezIWTZn3xgqFgCumFuKagnzAo1Tn4J_wyavsxO9W0-Rbeg4AI1KlajAOpiivdYWtF_mWFblkDwSUwJ0ujiRkMb5Dvdd2Kz_bbP2EUe8xY6jK48GRrknVeMdqZQgQw8-0uIgw1vZ0FyEjdl_JERfhrLe9fmycS_aqf1rFMA75IfDMIFS1gQwS5srYCXG62FcUM5LPI_lNcA_JUMKm_K_o0inPPrbFFnjLsqV8aGKOH72qW5SiiPT-6XH5EbaLYWvDOh22ve_7hVTfdd2Kif6ByhopsyIdqrKtQdjANlJMdSfAAaTbv4CWBO6gpGoPlp3iQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/132177" target="_blank">📅 14:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132176">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
یک منبع به فارس: در این جلسه برقراری اتصال اینترنت بین‌الملل با ۹ رای موافق و ۳ رای مخالف تصویب و برای تأیید به دفتر رئیس‌جمهور ارسال شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/132176" target="_blank">📅 14:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132175">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
فوری؛ علی علیپور قبل از اینکه بره همراه تیم ملی ترکیه با مدیران تراکتور جلسه ای برگزار کرده و به توافقاتی رسید اما امیدواره بره جام جهانی و با قیمت بالاتر لژیونر بشه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/SorkhTimes/132175" target="_blank">📅 13:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132174">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
یک منبع به فارس: در این جلسه برقراری اتصال اینترنت بین‌الملل با ۹ رای موافق و ۳ رای مخالف
تصویب و برای تأیید به دفتر رئیس‌جمهور ارسال شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/132174" target="_blank">📅 13:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132172">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
فوری/ بازگشایی اینترنت بین الملل مصوب شد
🔹
سیتنا خبر داد: ستاد راهبری و ساماندهی فضای مجازی صبح امروز دوشنبه (چهارم خردادماه) به ریاست دکتر عارف معاون اول رئیس جمهور تشکیل جلسه داد و بازگشت اینترنت به وضعیت قبل از دی ماه 1404 مصوب شد.
🔹
این مصوبه برای رییس جمهور ارسال شد و در صورت تایید رئیس جمهور جهت اجرا برای وزارت ارتباطات ارسال خواهدشد.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/132172" target="_blank">📅 12:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132170">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✅
اینترنت بین‌المللی تا یک هفته آینده در دسترس قرار می‌گیرد
🔴
مشاور وزیر و رئیس پارک فناوری اطلاعات و ارتباطات کشور از احتمال دسترسی و اتصال به اینترنت بین‌المللی در هفته آینده خبر داد و گفت شرکت‌های فناور با دریافت IP ویژه، اکنون از اینترنت بین‌المللی بهره‌مند…</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/132170" target="_blank">📅 11:56 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132168">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Co1ycqHRb77PCDcEGzP91HF0HG15KfA9lQ9yjHWq0MZ4yOyr_zHu38bfKQm2_zHIq9hMKypzbmNtP_UsgmfnV08G9j8XZa5dZhDxoRa3t-jw8yqEIU3YZOG5cZk3UqBLzX8P8KjAN7GKjTiWad8KxJppc7UCU8eKuRtuu4uBQzwE9jBi2d-qATo4u2YR5PNYlgkloJQX-z2JQAsDX_q1FGSi1TXGVzaET7fKY_8GcOMVCFeJ-4s_Xk3Y_2TsdgysfGD4X--X08iPiovNYMH0zKoVulfRVppiy0FFQ0nnMB0ri9TuxqI9adnVIWTpnudvy5MIBxiEJbmrjYEmFQLTBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فاکس‌ نیوز :
ترامپ برای رسیدن به توافق نهایی ۷ روز‌ دیگر به ایران زمان داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/132168" target="_blank">📅 11:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132167">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✅
سردار آزمون به زودی با انتشار یک پیام عذرخواهی به تیم ملی بازخواهد گشت.  #خبرنگار_فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/132167" target="_blank">📅 11:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132166">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
رشیدی کوچی نماینده سابق مجلس:   معتقدم این هفته اینترنت به حالت قبلی باز خواهد گشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/SorkhTimes/132166" target="_blank">📅 11:09 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132164">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
به نقل از منابع فوتبال 360 مدیران باشگاه پرسپولیس
از همین حالا تماس های خودشو با مهدی لیموچی و آریا یوسفی برای جذبشون در تابستان آغاز کرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/SorkhTimes/132164" target="_blank">📅 10:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132163">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4LRLFXYpLcSEpNXGMK_r3k5Fmjlf06ejIUuQHSO-wGhWOkvn9dAFyjL7FSgH8QnhpNnlDf0Z7Kk4BpdA24IROmTASMc3i9iHFnrjZbQpOLRFTWqFuW-t-A1p614TyQIjTf6D3Bduu0RyaEVLQgTJPiQ6BrXW39UYswK-uE9qVvcL2kNVbX5F2cUZgKF9qDAGv0-CPC68_8-ek0iaLDVQzYZf3zC-PPUX_gastoo2PeoCI4mSWPgcBH9Hbku9o2SUQr1VINP162c-S5ybRKkboTc72XYmWqxoSuVdCD8ICNb__ie2GUDwAAAe-sZbGFy_qP5n50GjBeSxNMRbNh8KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مدیران باشگاه‌ تراکتور تا‌به اکنون مجوز جدایی مهدی ترابی ستاره خود را صادر نکرده‌اند و بعید بنظر میرسد این بازیکن در پنجره نقل و انتقالاتی بازهم به پرسپولیس بازگردد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/SorkhTimes/132163" target="_blank">📅 10:27 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132162">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
فوووووری/ خبرنگار فارس حاضر در اردوی تیم ملی: امیرحسین محمودی در لیست نهایی تیم ملی برای جام جهانی قرار گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/SorkhTimes/132162" target="_blank">📅 10:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132160">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e786c6b741.mp4?token=WhwgQiJHdvVwdNC-V-_OITkjJECdIB_bcInKLAfPwe2oog6XcYhOCwn_9c8NXOOLHWye4T5qIovrudw28hDgU3Ac1kWq6bwVg7vInMrw8l6dKKICPBSzgZa-3CXi74C_CO-QncPB4v6eE_Pspx1Fod5oQfElxf0WC7Vxg9dBOq9ayJjJXzW4NuFskSuRLXOBqhftaRU4W9lkfhLK2aO8TzNPRmbTLAP-tcddwHwtIM2LOWspoOpRV0DZU45vHJGONVSIsf-CxscNK5YcLi3lXC91Ho861b-dpSf-otmazyledYOHavsytF_UpGTT26wTki01EhJDADdpEdqihGSj-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e786c6b741.mp4?token=WhwgQiJHdvVwdNC-V-_OITkjJECdIB_bcInKLAfPwe2oog6XcYhOCwn_9c8NXOOLHWye4T5qIovrudw28hDgU3Ac1kWq6bwVg7vInMrw8l6dKKICPBSzgZa-3CXi74C_CO-QncPB4v6eE_Pspx1Fod5oQfElxf0WC7Vxg9dBOq9ayJjJXzW4NuFskSuRLXOBqhftaRU4W9lkfhLK2aO8TzNPRmbTLAP-tcddwHwtIM2LOWspoOpRV0DZU45vHJGONVSIsf-CxscNK5YcLi3lXC91Ho861b-dpSf-otmazyledYOHavsytF_UpGTT26wTki01EhJDADdpEdqihGSj-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- همه اون لحظه‌ای که سایت نصفه لود میشه و VPN قاطی میکنه رو تجربه کردیم، مخصوصاً وقتی وسط بازی یا ثبت پیش‌بینی باشی.
😑
- ربات رسمی تلگرام وینکوبت کارو راحت و ورود به سایت رو آسون کرده:
👇
-
🤖
@Wincobet_bot
-
🤖
@Wincobet_bot
- برای کسایی که بیشتر وقتشون توی تلگرامه، خیلی کاربردیه.</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/SorkhTimes/132160" target="_blank">📅 01:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132158">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABhoARoFx_yPn2JysrqINGsT2wN3J3UQfV9MPcL-qqDU6yFuGSMZHN2HCxkpOgAAqjf4EQynyJp_cYepYNhYNxIi8cMlBfCtOttjP5eMWj0qvGI1ouMVNaK7dctVQ-F15UcDFEmyUSYiqhChz5dd5BVs6zfhGtcb1BrqGpHBrBILEyQdJ9Yk943WMvK3k1rxI9yziVtcaRwc8D79yAg3P-62AtxKfWeU8DMxEOyEim6SdpC6u7txxmbzKm8qb84rEbK0sgfnCh7nqjutnl-Vhd2WBB-vApWSTLY_9PiCc9LBPpuql3kN9DYRzMt8SczGJmPnkXXg02oX360hAqNMCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇺🇸
کانال 12 عبری: نتانیاهو در تلاشه تا توافق رو بهم بزنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/SorkhTimes/132158" target="_blank">📅 00:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132157">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❗️
رسانه‌های داخلی: آمریکا مانع آزادسازی پول‌های مسدود شدست، احتمال لغو کلی توافق وجود داره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/SorkhTimes/132157" target="_blank">📅 00:38 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132156">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
علیرضا جهانبخش و مهدی طارمی در اردوی تیم‌ملی از امیر قلعه‌نویی درخواست کرده اند سردار آزمون را ببخشد و او را به تیم ملی دعوت کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/SorkhTimes/132156" target="_blank">📅 23:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132155">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
نماینده محمد امین حزباوی امروز پیشنهاد مالی‌ مدنظر مدافع میانی سپاهان رو به مدیران باشگاه پرسپولیس ارائه کرده است. درصورت موافق با این پیشنهاد به احتمال فراوان حزباوی راهی پرسپولیس خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/SorkhTimes/132155" target="_blank">📅 23:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132154">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">📣
#شنیده‌ها
🗣
🇮🇷
محمدامین حزباوی از باشگاه پرسپولیس پیشنهاد رسمی دریافت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/SorkhTimes/132154" target="_blank">📅 23:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132153">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RM4t_iMM6kquN33-Dfy_U-BfRWOO6Vxegp53QSS0LAvagyPuRzuR7DZAOpArPYgsrwcnu6HNsHRxSEqfAZMaG4OZwoSQYxAab97F-fe_SHqVQGfDS9m5IZGQnDoWrecYYRRPIdIiA2FP620iXMoetgJsJhywGU68PIlo8DmXzhgbAQ-6o8_AQbQ2BrTlT6wOregepnspYOlu8F-LzQ7VNYjuIIbi2Hk-xFRPFY_vGc_snqX6WKRLOreFe-KasrmzLrrpM1SaD5pRjO04UAdAowukGFysRHdlDUDdye6zkLxZr7hLPTtBdSyHJks639GDl3g2hhw6-mfupS57CcEr7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مدیران باشگاه پرسپولیس قصد دارند درصورت افزایش بودجه؛ قرارداد ابرقویی نژاد را از لحاظ مالی افزایش دهند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/SorkhTimes/132153" target="_blank">📅 23:22 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132151">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
جوزالم پست: ایران در اصل با یک توافق آتش‌بس با ایالات متحده موافقت کرده است که بر اساس آن، اورانیوم بسیار غنی‌شده خود را از بین خواهد برد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/SorkhTimes/132151" target="_blank">📅 22:27 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132150">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VburWRH_-1Ldphct9b-rAdtAuYpRGKrgyB1HMVl47mzfBD8vGZ4NP169ePzKyfC4oqO2dneZuX-n8zyt3X1jP3Mqxe9vCY_uKTcXv29EhLhwBF3vbvm1XnNbHu1kngtNjOMVyA37CGXZmDmnfK1wBM1eL_kjZh8Z8jmNtzhMzoL2nihoKiDULm4Xf1IRuCOQdvuaWhayKF70oaCoUojMqjELzxKYd6juZKMpz9fzQk9jkzQFcMnG_1gk4WMXEvOuych9HGB422_SR0VV7ZnD62w23fNRkA5MQE71cTkl-J0Q3InMMx-NYS1ZaHOGdmv8XecMD9pwTuzRQCOGq33N2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علیرضا جهانبخش و مهدی طارمی در اردوی تیم‌ملی از امیر قلعه‌نویی درخواست کرده اند سردار آزمون را ببخشد و او را به تیم ملی دعوت کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/SorkhTimes/132150" target="_blank">📅 22:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132149">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/um6ThO5EBBDFUSm9kBF1Fc_Nxbg4EJwqriz8pphImM5f0UwjEoVOwAGklgY6prjpH2uSBz8evWwKTyETOWBQhCbanrytVGH41PiKSlKzrZLY_l2DhhwxicFue6DvZ2dOfIUSDRTyHeHFCAjK993XmbV_K86qxQ-Ik0nPF8_V7pxzDhMrXgCdNbGBwXA6JER_2kYttYPH4YIkupmhw2u2NFQu87X7PvSVUSXf38lBstEsUgUP_wv4LkBRn5pEehh4jv-Tfe1OOK-6YfOqCqm7n29QlanU2foFbQi_TReENNxaWoFdbMQTQGMqF37gvet0uUFImZgZiQnzeicfvFBqfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/SorkhTimes/132149" target="_blank">📅 22:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132148">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✅
فووووووووووووری
🚨
علی علیپور در آستانه عقد قرارداد با باشگاه تراکتور سازی تبریز قرار دارد/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/SorkhTimes/132148" target="_blank">📅 22:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132147">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
فرهیختگان: علیپور از پرسپولیس خواسته رقم قراردادش از همه ایرانیای لیگ بالاتر باشه و اگه موافقت کنن بعد جام جهانی تمدید میکنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/SorkhTimes/132147" target="_blank">📅 22:02 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132145">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hINo8uYsGaFDNMKSrzXkVyjsE-Bnz5wzYnkt_nOIs83w6TjdPU9BzIhw-s5gxUt11RhY3INsKyX2xTxNpBYhhlgVL6_ZkS5dJhpCXJlnvm11kieDCQ8ROMwBGzjKqXWcMXgMAn5h9tydDmUWf6KzTBW8-UYVAQI59kJ-5pHlrNo61qmqkLK3dfQCkFcmlqXVhEY7SiX2qNkhJacDEhFj-cB1pKEppHpE9-SNHEsLfMbujMM5TluCCRbFs3AqQuigLzYm527VOf3F4wNQSZ9wadP3GzE93KRB92WKKntHw5CyzllLTLFNEcttz2ZXr9da_5wOzkf2DDhKmXw-r5SLMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖍
سایت فوتی رنکینگ ، چادرملو رو به عنوان نماینده ایران در لیگ دو آسیا معرفی کرد
😐
😟
😟
😟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/SorkhTimes/132145" target="_blank">📅 21:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132144">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffe4f5232d.mp4?token=TwxhhqNqJn4qmpxmIa-BITtrXo1dPiUUfSbEqB9KFkWUa-fU5-ONawu5VH0UV5oMY3FgTIkHttNJxQyKqfoHGx11qxkefSsRcCVCsukDch8hUt6sJWa4kLkeSWZ4PFaoUumeXCsENNAek8J3Q54TvAeKTKcpks6T3CxUZQtMp6HFXCKveV_fnsdM7Gj3EBGOG_L5mpznsUSbau3XsXRwnUGd4THVUPfenspzlPbhlcYGyiX3GwM1p1AjcANk6dOebt-1mgoIMyQq1nlxUWy0UGX-QvbHdHx4Dw1-Yy4byG-kNsR03QedcjLnod8uezMoR2AUqFymwHqQ8cbb2OVpOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffe4f5232d.mp4?token=TwxhhqNqJn4qmpxmIa-BITtrXo1dPiUUfSbEqB9KFkWUa-fU5-ONawu5VH0UV5oMY3FgTIkHttNJxQyKqfoHGx11qxkefSsRcCVCsukDch8hUt6sJWa4kLkeSWZ4PFaoUumeXCsENNAek8J3Q54TvAeKTKcpks6T3CxUZQtMp6HFXCKveV_fnsdM7Gj3EBGOG_L5mpznsUSbau3XsXRwnUGd4THVUPfenspzlPbhlcYGyiX3GwM1p1AjcANk6dOebt-1mgoIMyQq1nlxUWy0UGX-QvbHdHx4Dw1-Yy4byG-kNsR03QedcjLnod8uezMoR2AUqFymwHqQ8cbb2OVpOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی علیپور امروز تو بازی دوستانه درون تیم ملی به این شکل پنالتی خراب کرد تا شایعه خط خوردنش از لیست تیم ملی تقویت بشه!!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/SorkhTimes/132144" target="_blank">📅 21:18 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132143">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
فارس: باشگاه پرسپولیس قصد تمدید قرارداد میلاد محمدی را ندارد و به احتمال زیاد از جمع سرخپوشان جدا شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/SorkhTimes/132143" target="_blank">📅 20:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132142">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a133b9505.mp4?token=G7KF6Q5TVLCAzTy8Waj0d8f3eXNayQGqe3TFqUa3fKRwzg73DmA8dR1EwFko4VTQ-nEmC1HcSLkdQZlMA6AmldAm4oVPubGNGr4pW9ExVLtsbOyMZNcrzPch7FJtMa5OSTNsssw1G1pg_yGIyaDMU7G3r6fAF1ZMT50ENp0BQ17zLpfO8OZiiUfg5AfFG2WSnD7MnKeXzriZM-Vk5gmrfLAZ-Eu42e7g_szPIFhUNZ6HqVw7nf0h43se_yDN6KnMaD77fLceU8hcvpPamJ0yISVUYoWcY3_ictAXxHqup8GEln9fz5qJqTurizZB0aap7qVV-rEft_PZshCVguMsWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a133b9505.mp4?token=G7KF6Q5TVLCAzTy8Waj0d8f3eXNayQGqe3TFqUa3fKRwzg73DmA8dR1EwFko4VTQ-nEmC1HcSLkdQZlMA6AmldAm4oVPubGNGr4pW9ExVLtsbOyMZNcrzPch7FJtMa5OSTNsssw1G1pg_yGIyaDMU7G3r6fAF1ZMT50ENp0BQ17zLpfO8OZiiUfg5AfFG2WSnD7MnKeXzriZM-Vk5gmrfLAZ-Eu42e7g_szPIFhUNZ6HqVw7nf0h43se_yDN6KnMaD77fLceU8hcvpPamJ0yISVUYoWcY3_ictAXxHqup8GEln9fz5qJqTurizZB0aap7qVV-rEft_PZshCVguMsWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پاس گل امیرحسین محمودی تو بازی دوستانه درون تیمی امروز تیم ملی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/SorkhTimes/132142" target="_blank">📅 20:41 · 03 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
