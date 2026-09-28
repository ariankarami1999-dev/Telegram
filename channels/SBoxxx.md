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
<img src="https://cdn4.telesco.pe/file/DhHaoOHkm94pSi4JZpxTdEsHbhDCbMPwRShJIq2_0U1MoZzSUtMoC250DbaXyyZA0tYgd8Bfox_4qglyZ33TDhJ3p4tW6TfOZ2RUcYQWFOuAJJlTbK_sRx3SSa1wKFpzL4lDl1lo5yPIZnb_BqmsoD9giXDZMvIBqL_dKkYYT9cUpQDjYmNXQ8lCvXl3o8peTYU66WihsbodYB_-HxP19WmrPGxOY7SQzhDF4gS6jWn8gMSGKqL0KB8NP4rKgmWu9Ex8zGeQN4KP7MsupLDIxhJcIka_Csacz6DL2hIrzLkaBjV9dayQ2n7P1PpPdd3cpmgHXNrtwe4vckz4U1rdVw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.9K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-06 21:14:38</div>
<hr>

<div class="tg-post" id="msg-21296">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">احتمالا امروز ترامپ خواهدگفت مذاکرات خوب پیش می رود</div>
<div class="tg-footer">👁️ 683 · <a href="https://t.me/SBoxxx/21296" target="_blank">📅 21:09 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21295">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بخدای کعبه سوگند که دروغ و فریبی بیش نیست! همه اش فریب و نیرنگ ترامپ است تا زمان بخرد و نیروهای بیشتری به منطقه بیاورد!
خواهیم دید چه خواهدشد!
عجالتاً طلایمان برگردد حالا خوب است</div>
<div class="tg-footer">👁️ 900 · <a href="https://t.me/SBoxxx/21295" target="_blank">📅 21:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21294">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ایران با توقف غنی سازی موافقت کرد!</div>
<div class="tg-footer">👁️ 993 · <a href="https://t.me/SBoxxx/21294" target="_blank">📅 21:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21293">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWAxy4gGpvu5S5-fxRdMsb42VEQuPELkToHKkRH-FJubcxORMrNvpg_cVsTQqfmBbh5MWfx9i2I0xduxEYv1Im4tdoQcF0loXROVaQMrGBUHqFEy_Ep0CSevAc3sTXLmn0jyYWp95oXGrnItO3pJvER1-wEuQ6_XxD0ULORzHZIP2mWWGZLFW7kqsYXURTF6zFzscQKoSmtihaIt0ZrzCi2Nq-ewdYzgSHOMz4THavnFh9xKHcfINL_hH7bA7sMUQ1NkYbMvWoh2yzAhpKHtg5xdAlDeLHC7Cos7bgEV1ZVnjDKExiwIBeahAjlENdv6KPXDpMKorWjlNEfHjXn_EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادران ارزشی تازه دارند می فهمند چرا دکتر پزشکیان آن روز در سازمان ملل از ماتریکس خارج شده بود!
یا ذی الجلال و الاکرام!</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/SBoxxx/21293" target="_blank">📅 20:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21292">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">در ۲۴ ساعت گذشته، دو اسکادران جنگنده آمریکایی به پایگاه هوایی اوودا نیروی هوایی اسرائیل در جنوب این کشور رسیدند و به نیروهای آمریکایی دیگری که از قبل در این کشور مستقر بودند، پیوستند.
مقامات امنیتی اسرائیل اعلام کردند که این استقرار بخشی از تحرکات گسترده‌تر نیروهای هوایی آمریکا در سراسر خاورمیانه است و نشان‌دهنده آمادگی بیشتر یا تشدید تنش با ایران نیست.
یک منبع امنیتی گفت که حضور نظامی فعلی آمریکا همچنان بسیار کمتر از سطح نیروهایی است که قبل از عملیات «خشم حماسی» (Operation Epic Fury) در این منطقه مستقر شده بودند.
— کانال ۱۲ اسرائیل</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/SBoxxx/21292" target="_blank">📅 20:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21291">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❗
عربستان سعودی پس از تعمیرات، صادرات نفت خود را از طریق خط لوله شرقی-غربی از سر گرفته است</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/SBoxxx/21291" target="_blank">📅 20:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21290">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دیدید؟! این کله زرد حرامزاده را من بهتر از پدرانش میشناسم!</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/SBoxxx/21290" target="_blank">📅 20:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21289">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">گزارش‌ رسانه‌های عربی از شلیک موشک‌ از خاک ایران</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SBoxxx/21289" target="_blank">📅 19:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21288">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترکیه یک هواپیمای ایرانی را به دلیل تحریم های آمریکا توقیف کرد.</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/SBoxxx/21288" target="_blank">📅 19:08 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21287">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کار طلافروش آنلاین به شورای عالی امنیت ملی رسید  پلتفرم فروش آنلاین طلای میلی‌گلد در نامه‌ای به محسن رضایی، دبیر شورای عالی امنیت ملی، خواستار صدور دستور فوری برای رفع محدودیت دسترسی به طلای کاربران در خزانه‌های بانکی شده است.   این پلتفرم می‌گوید محدودیت‌های…</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SBoxxx/21287" target="_blank">📅 18:06 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21286">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط انرژی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlLFL29gSmm0itHLNUWOUVD5zZGaXdbluy-kXLkQMPudslHf82KP0sf4TuUD_GD-0UW7yNJ-HqMaonUzUfjMFGJz6Qqk2uCOIKYYTaPSawSz_l8bjfWJQu1P5bw4yffzrAfK5wWzs-61UTWHh1awuZE5eGTkaDYyKHOmSLq8uVKqy2YUI9I3tcXXqDncPvmJm33TbhtPH19Rprddp1ggsRnFCXpohdIwr8BTMtksOKK6WwJMje7-bB47If050Zyisks7fE_ABNJljBQXIMpgl5pR-hZFBCdcPAeFtEIQVQP4kfhbt8IPwFSH7yGg7yqqfLCqZYQSE06quBWCbNsXBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
صادرات نفت خلیج فارس به ۸۰ درصد سطح پیش از جنگ رسید
🔹
خاویر بلاس مدعی شد: صادرات نفت خام عربستان، عراق، کویت، امارات، بحرین و قطر با کمک نیروی دریایی آمریکا، به ۸۰ درصد سطح پیش از جنگ بازگشته.
@khate_energy</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SBoxxx/21286" target="_blank">📅 17:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21285">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SBoxxx/21285" target="_blank">📅 17:23 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21284">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">فوری | فرماندهی مرکزی آمریکا:   ایران کنترل تنگه هرمز را در دست ندارد؛ شواهدی مبنی بر عبور بیش از یک میلیارد بشکه نفت در طول چند ماه وجود دارد.</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/21284" target="_blank">📅 17:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21283">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">فوری | فرماندهی مرکزی آمریکا:   ایران کنترل تنگه هرمز را در دست ندارد؛ شواهدی مبنی بر عبور بیش از یک میلیارد بشکه نفت در طول چند ماه وجود دارد.</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/21283" target="_blank">📅 15:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21282">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">پیام تند آیت الله خامنه‌ای:   دشمنان جرأت ورود به خلیج فارس را ندارند  رهبر جمهوری اسلامی ایران، در بیانیه‌ای اعلام کرد نیروهای دشمن جرأت ورود به خلیج فارس را ندارند.  او همچنین گفت دریای عرب به‌زودی از حضور «دشمنان» پاک خواهد شد.</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/21282" target="_blank">📅 15:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21281">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">هیچ کس را امین تُِن های ماهی تان قرار ندهید.</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/21281" target="_blank">📅 15:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21280">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/21280" target="_blank">📅 15:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21279">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">طلا تارگت روز جمعه را زد (ما زودتر کلوز کرده بودیم)  امروز اما اندک اندک وقت خرید است و کل این مسیر ریزش را برخواهدگشت.  بازار جنگ را کامل دارد پیشخور می‌کند اما ناوهای هواپیمابر آمریکا هنوز نرسیده اند و آرایش جنگی تکمیل نشده و عباس آقا سعد اکبر هم هنوز برنگشته!…</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/21279" target="_blank">📅 15:37 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21278">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">— تًن ماهی — گوشگیر سیلیکونی — آب معدنی — چسب شیشه — یدید پتاسیم — پنبه — روغن بنفشه</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/21278" target="_blank">📅 14:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21277">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">— تًن ماهی — گوشگیر سیلیکونی — آب معدنی — چسب شیشه — یدید پتاسیم</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/21277" target="_blank">📅 14:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21276">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">— تًن ماهی — گوشگیر سیلیکونی — آب معدنی — چسب شیشه — یدید پتاسیم</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/21276" target="_blank">📅 14:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21275">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">— تًن ماهی — گوشگیر سیلیکونی — آب معدنی — چسب زدن شیشه ها</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/21275" target="_blank">📅 14:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21274">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پیام تند آیت الله خامنه‌ای:   دشمنان جرأت ورود به خلیج فارس را ندارند  رهبر جمهوری اسلامی ایران، در بیانیه‌ای اعلام کرد نیروهای دشمن جرأت ورود به خلیج فارس را ندارند.  او همچنین گفت دریای عرب به‌زودی از حضور «دشمنان» پاک خواهد شد.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/21274" target="_blank">📅 14:55 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21273">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پیام تند آیت الله خامنه‌ای:
دشمنان جرأت ورود به خلیج فارس را ندارند
رهبر جمهوری اسلامی ایران، در بیانیه‌ای اعلام کرد نیروهای دشمن جرأت ورود به خلیج فارس را ندارند.
او همچنین گفت دریای عرب به‌زودی از حضور «دشمنان» پاک خواهد شد.</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/21273" target="_blank">📅 14:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21272">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ایران شکایتی را علیه ایالات متحده به سازمان هواپیمایی ملل متحد (ایکائو) ارائه کرده است، به این دلیل که آمریکا محدودیت‌هایی را علیه شرکت‌های هواپیمایی این کشور اعمال کرده است.</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/21272" target="_blank">📅 14:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21271">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">عملاً همه دارند نفت صادر می کنند جز خودمان!</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/21271" target="_blank">📅 11:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21270">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔥
جریان ۱۲ میلیون بشکه‌ای نفت در کریدور عمانی
🔹
موسسه HFI: افزایش صادرات نفت عربستان از مسیر شرق می‌تواند جریان نفت در کریدور عمان را به ۱۲ میلیون بشکه در روز برساند که در نگاه اول می‌تواند نشانه عادی‌شدن تردد نفت در منطقه تلقی شود.
🔹
بخش قابل‌توجهی از نفت…</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/21270" target="_blank">📅 11:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21269">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط انرژی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYmwoyPK1ffpdKgypyCFZ67bgRS65Oi3Hv-j-KvF7vwDp7fMjvzNo3n5AxWrsHvvqU_SHONJTirVOgYzUYbsKJd3fyUEcLCz0p2tcjlD89O2W6j-W89oUtFL1rsYV01QygV_sq0rHv7tIBzsrJEQD0LPYVK0Q7O3Cp_9nG_DO0YqDH7pYLjmr8Str4G-5FkXha2FIM9Zqtsp1uLV6dtNiES8dfQoajPAxV9uRHVnejHgICIvbZFcBLg5CjzRm-uAHhMp5_kbjh72FTt39yeRrGU0DGnhffpU2R0wfrkxx8II5OtFgMpOs9IcH9K4CEL2kaz86FsUcal3kLMHi1Pstw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
جریان ۱۲ میلیون بشکه‌ای نفت در کریدور عمانی
🔹
موسسه HFI: افزایش صادرات نفت عربستان از مسیر شرق می‌تواند جریان نفت در کریدور عمان را به ۱۲ میلیون بشکه در روز برساند که در نگاه اول می‌تواند نشانه عادی‌شدن تردد نفت در منطقه تلقی شود.
🔹
بخش قابل‌توجهی از نفت عربستان در این جریان راهی چین می‌شود.
@khate_energy</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/21269" target="_blank">📅 11:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21268">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سراج، نماینده مجلس: حرف‌های عراقچی و پزشکیان درباره هسته ای و کوتاه آمدن از قصاص قاتلان رهبری بی‌اساس است و ربطی به سیاست جمهوری اسلامی ندارد
آمریکا می‌داند پزشکیان و عراقچی تصمیم‌گیر نیستند و محلی از اعراب ندارند
سخنان عراقچی صرفا اظهارنظرات خود اوست و هیچ اعتباری ندارد
اجرای انتقام و قصاص ربطی به دولت ندارد که نظر مثبت داشته باشد یا منفی
محمد سراج، نماینده تهران با اشاره به موضع گیری های مکرر پزشکیان و عراقچی درباره شرط ۷ روزه و باز کردن تنگه هرمز و رقیق سازی اورانیوم به دیده بان ایران گفت: « صحبت های آقایان عراقچی و پزشکیان در خصوص کوتاه آمدن از سیاست های نظام نظر شخصی بوده و نظر جمهوری اسلامی نیست. نظر جمهوری اسلامی ساز و کار خود را دارد و در سیاست کلان خارجی رهبری تعیین‌کننده هستند و در سایر موارد نیز مجلس و قانون مجلس مبنا قرار دارد. در حال حاضر محسن رضایی، دبیر شورای عالی‌ امنیت ملی سیاست کلان خارجی جمهوری اسلامی را بیان کرده است.»</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/21268" target="_blank">📅 11:36 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21267">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">طلا تارگت روز جمعه را زد (ما زودتر کلوز کرده بودیم)  امروز اما اندک اندک وقت خرید است و کل این مسیر ریزش را برخواهدگشت.  بازار جنگ را کامل دارد پیشخور می‌کند اما ناوهای هواپیمابر آمریکا هنوز نرسیده اند و آرایش جنگی تکمیل نشده و عباس آقا سعد اکبر هم هنوز برنگشته!…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/21267" target="_blank">📅 10:11 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21266">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kizhm3pkW_MNB8iilvrMjYNNhJkYJqSHBM6ySw2SFv_tFJ1f5IjDVe52xQ3m5rIBKqLMRtp2Zd7eLVCujPfLqUKp-ns4CBm0b082Iq96rfC3VpTiTgEIeygheDE4iys9xi1nXUlNzzRhzCIkt_Y0dSB8uOzcAZ5y9_lsV13Hza9iOyvfMDfzzPg1e7xBYtIh2ezf39rSf11ynPYTbLq1MYExH9JDm1tRXyw_cHlT3156XK5NuecABviJMAOJG1CoDNpuy3uuseADWq1qntuHncINMcMC4w4YgRd_JcSqB-_VSOyE34GXbl1fgfMMiDiFRyXE2zHU-IzZZuqJwpB01A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#WHEAT — D  به نظر می رسد گندم هم دارد همان مسیری را می رود که نقره 3 سال پیش در آغاز آن بود...</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/21266" target="_blank">📅 09:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21265">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVw5sHF1gFFqOKy4_0-szWSB22FeuFReLvny6x8hDw6lE16wmqQzeWXfJvlV9hNwv958YNYFHv130ij90BCXSWs91hcZaKKStzrWfNWsZJqwyAn09F5W7iugG7s43qX1yc0pCt86R8YDgAt6XzxTyfHNSmOztC_SbdSQenLphbJm6T6GSYiuuZcumvCouo9UW5mI9LaXUBgqFkNg1o185Y_b9aB6ClJ-tvx3cgGPXJgWQJNNdXaI0jKeW7XvIb7urLCfoGlxuyZWWO4PHKJ18c6st5acAkqsAsW_U5zmFOccoVUnPlUGyhM3PKJKGK7bsCfnPs6kP7E0xj7DuRejsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC نیز به کف محدوده بیش—فروش رسیده و خرید توصیه می کند.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/21265" target="_blank">📅 09:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21264">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdRDRcQxsh-d19c1dsWW0sVVP5uO4dKt2yi-g2ZZrV7_NX7tB8sqhlaLoUEe-IfT9QpKGWwhBWCp7wBdCaASzhY5TWwatmPaclrWQpfZn6dWbbtld7YgY8Md0j-xsAZbAuhsbYo6kMltJMB1n_maJTeVjRb9mOO1qIOWlpWosOj_3ZIZcek8Y8Obiu3jNBBR5F4ha-pIw8y-cO77z0N-6SovaOkF7UAHrEmesdcGhV04jmvA8J0ET0KkAIuocQresIqY0pEoGz5l3QnrquFSdok0cGB9Y2Ug9skWnG3Ffi0SJKzaC2EehfssuU9WbSHo0eUokSjCZam7-wmwUeQY9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح پایینی است و از دید این شاخص، واکنش بازار به تنشهای هرمز مقداری افراطی بوده است.</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/21264" target="_blank">📅 09:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21263">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3PI4_RSX40-u5zsF4vq4GK3UMUXS05ISw5ax6ixuUR6aJlSCUIOqL3XjmJ9uIKIEbqL993YgsNEKk74sED4paQvc2Mou0vZVTeDNx4CovO_rCcVaO21uhHkB_UMGF7GRxaq0ZsPrD528scKs2Mzn8aafIQ4xmHdqt_6pdw238JcSQYwk_e7EIypviaCHVs1ZUALTOmmDOuttGTJGX3bHS_k50mCg8_tdFKgG10FTiJCeXhqfaH4z07fVzwg3WsPi0rBv7wgVlNCMNhGws0DZcwTO75mZBHNzCBE8uUKLe6dJ_hpqTWNP-MRl6nyjd8wOJvlAk_xTkxiRcyi5UPnHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ژاپن بزودی بدجور موی دماغ چین خواهدشد.</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/21263" target="_blank">📅 08:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21262">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">جنگ ایران و بن‌بست فزاینده آمریکا؛ از بحران انرژی تا تغییر موازنه خلیج فارس
بر اساس دیدگاه‌های مطرح‌شده توسط جان مرشایمر نویسنده پرآوازه کتابها و مقالات ژئوپولیتیک، جنگ ایران و آمریکا وارد مرحله‌ای از بن‌بست شده است. از نگاه او، آمریکا تاکنون به اهداف اولیه خود دست نیافته و در عین حال ایران نیز حاضر نیست بدون دریافت امتیازات قابل‌توجه از جنگ خارج شود. تهران به‌جای تلاش برای شکست نظامی آمریکا، به دنبال افزایش هزینه‌های جنگ و فرسایش توان اقتصادی و سیاسی واشنگتن است؛ به بیان ساده‌تر، راهبرد ایران «دوام آوردن تا فرسوده شدن طرف مقابل» است.
یکی از مهم‌ترین اهرم‌های ایران، موقعیت آن در تنگه هرمز و پیوند آن با تحولات دریای سرخ و باب‌المندب است. اختلال در مسیرهای اصلی انرژی باعث افزایش قیمت نفت، سوخت، حمل‌ونقل و مواد غذایی شده و فشار تورمی را به اقتصاد جهانی منتقل کرده است. هم‌زمان، جنگ میان حوثی‌ها و عربستان نیز جریان صادرات نفت عربستان از مسیر دریای سرخ را با اختلال مواجه کرده است. مرشایمر می‌گوید ظرفیت عملی خط لوله عربستان به دریای سرخ پیش از حملات حدود ۴ میلیون بشکه در روز بود، اما پس از آسیب به ایستگاه‌های پمپاژ، جریان آن به حدود ۱.۶ میلیون بشکه در روز کاهش یافته است.
این وضعیت برای اروپا اهمیت ویژه‌ای دارد، زیرا هم‌زمان با کاهش عرضه نفت، بازار جهانی گازوییل نیز تحت فشار قرار گرفته است. روسیه صادرات گازوییل خود را محدود کرده و آمریکا نیز درباره محدود کردن صادرات گازوییل بحث می‌کند. از دید مرشایمر، تداوم این روند می‌تواند فشار قابل‌توجهی بر اقتصاد اروپا و اقتصاد جهانی وارد کند.
محدودیت گزینه‌های نظامی آمریکا
مرشایمر معتقد است آمریکا گزینه نظامی مؤثری برای دستیابی به پیروزی در ایران در اختیار ندارد. به گفته او، جنگ هوایی اولیه که از ۲۸ فوریه تا ۸ آوریل ادامه داشت نتوانست اهداف آمریکا را محقق کند و یکی از محدودیت‌های مهم واشنگتن، کاهش ذخایر تسلیحات پیشرفته و گران‌قیمت است. بنابراین، تهدید به حمله گسترده پس از انتخابات میان‌دوره‌ای لزوماً به معنای وجود یک راهبرد جدید برای پیروزی نیست.
همین محدودیت درباره حوثی‌ها نیز مطرح است. عربستان چند بار از ترامپ درخواست کمک کرده، اما آمریکا از ورود مجدد به جنگ با حوثی‌ها خودداری کرده است. استدلال اصلی این است که چنین جنگی می‌تواند منابع تسلیحاتی محدود آمریکا را مصرف کند، بدون آنکه تضمینی برای دستیابی به یک پیروزی پایدار وجود داشته باشد.
فشار اقتصادی و راهبرد تحریم‌ها
راهبرد اقتصادی آمریکا برای تحت فشار قرار دادن ایران نیز، از نگاه مرشایمر، با محدودیت روبه‌رو شده است. طرح وزیر خزانه‌داری آمریکا، اسکات بسنت، بر تشدید فشار اقتصادی و اعمال تحریم‌های ثانویه علیه کشورهایی استوار است که با ایران تجارت می‌کنند. اما چین، روسیه، ترکیه و امارات حاضر نیستند به‌طور کامل از تجارت با ایران خارج شوند. بنابراین، ایجاد یک محاصره اقتصادی کامل بسیار دشوار است.
چین در این میان نقش کلیدی دارد. طبق ادعاهای مطرح‌شده در مصاحبه مرشمایر، چین بخش بزرگی از نفت ایران را خریداری می‌کند و از طریق شبکه‌های تجاری و مالی به تهران کمک می‌کند فشار تحریم‌ها را دور بزند. همچنین ادعا شده است که چین در زمینه تجهیزات نظامی و ارتقای توان پهپادی و موشکی ایران نیز کمک‌هایی ارائه کرده است.
در نتیجه، فشار آمریکا علیه ایران صرفاً یک رویارویی دوجانبه نیست و به رقابت گسترده‌تری میان آمریکا، از یک سو، و ایران، چین و روسیه از سوی دیگر تبدیل شده است.
نفت و خطر تشدید بحران جهانی
یکی از نگرانی‌های اصلی، کاهش توان اقتصاد جهانی برای جذب شوک نفتی است. ذخایر استراتژیک نفت آمریکا در این مصاحبه حدود ۲۸۵ میلیون بشکه عنوان شده و کاهش بیشتر آن می‌تواند توان واشنگتن برای مقابله با شوک‌های بعدی را محدود کند. چین نیز که در آغاز جنگ واردات نفت خود را به‌شدت کاهش داده بود، اکنون دوباره واردات خود را افزایش داده است؛ بنابراین یکی از مکانیسم‌های اولیه برای کاهش فشار بازار نفت در حال ضعیف شدن است.
اگر صادرات عربستان نیز همچنان مختل شود، فشار بر بازار جهانی نفت می‌تواند بیشتر شود. در چنین شرایطی، اثرات جنگ دیگر محدود به ایران و آمریکا نخواهد بود و می‌تواند از طریق انرژی، تورم، زنجیره تأمین و هزینه حمل‌ونقل به اقتصادهای مختلف منتقل شود.
مرشایمر هشدار می‌دهد که در صورت ادامه جنگ، خطر رکود شدید جهانی افزایش می‌یابد؛ هرچند خودش تأکید می‌کند که نمی‌تواند با قطعیت پیش‌بینی کند بحران تا چه اندازه عمیق خواهد شد یا آیا به یک رکود جهانی بسیار طولانی منجر خواهد شد.
تغییر محاسبات کشورهای خلیج فارس
یکی از پیامدهای مهم جنگ می‌تواند تغییر محاسبات امنیتی کشورهای عربی خلیج فارس باشد. اگر این کشورها به این نتیجه برسند که آمریکا در شرایط بحرانی حاضر نیست مستقیماً از آنها دفاع کند، ممکن است به دنبال ترتیبات امنیتی مستقل‌تر بروند.
مرشایمر معتقد است عربستان و سایر کشورهای خلیج فارس ممکن است به سمت نوعی تفاهم با ایران حرکت کنند، زیرا اتکا به آمریکا، پاکستان یا ترکیه الزاماً نمی‌تواند یک چتر امنیتی پایدار ایجاد کند. در این چارچوب، کاهش تنش مستقیم میان ایران و کشورهای عربی می‌تواند به یکی از گزینه‌های مهم آینده تبدیل شود.
خطر مسابقه هسته‌ای منطقه‌ای
یکی از مهم‌ترین پیامدهای بلندمدت جنگ، از دید مرشایمر، افزایش انگیزه کشورهای منطقه برای دستیابی به بازدارندگی هسته‌ای است.
در این تحلیل، اگر ایران به این نتیجه برسد که سلاح هسته‌ای تنها راه تضمین بقای حکومت و جلوگیری از حملات آینده است، فشار برای حرکت در این مسیر افزایش می‌یابد. همین منطق می‌تواند عربستان را نیز به دنبال کردن یک گزینه هسته‌ای سوق دهد و در مرحله بعد کشورهای دیگری مانند ترکیه، مصر و عراق را نیز تحت تأثیر قرار دهد.
این مسئله یک تناقض مهم ایجاد می‌کند: جنگی که هدف یکی از طرف‌های آن جلوگیری از دستیابی ایران به توانمندی هسته‌ای بوده، ممکن است در صورت شکست مذاکرات، انگیزه ایران و حتی سایر کشورهای منطقه برای دستیابی به بازدارندگی هسته‌ای را افزایش دهد.
پیامدها برای اسرائیل
در این روایت، جنگ الزاماً به تحقق اهداف اسرائیل نیز منجر نشده است. یکی از نگرانی‌های اصلی اسرائیل، جلوگیری از دستیابی ایران به سلاح هسته‌ای بوده است؛ اما ادامه جنگ و فروپاشی مسیر مذاکرات هسته‌ای می‌تواند احتمال دستیابی ایران به چنین ظرفیتی را افزایش دهد.
هم‌زمان، توان موشکی و پهپادی ایران به‌عنوان یک تهدید مهم برای اسرائیل و کشورهای خلیج فارس مطرح شده است. همچنین جنگ نتوانسته پیوند ایران با گروه‌های متحد منطقه‌ای خود را از بین ببرد و حتی از دید مرشایمر ممکن است این پیوندها را تقویت کرده باشد.
جمع‌بندی
تصویر کلی ارائه‌شده در این مصاحبه، جنگ ایران را نبردی می‌داند که در آن مسئله اصلی دیگر صرفاً توان نظامی نیست؛ بلکه زمان، انرژی، اقتصاد، ذخایر تسلیحاتی، انسجام ائتلاف‌ها و تحمل سیاسی به عناصر اصلی قدرت تبدیل شده‌اند.
در این چارچوب، آمریکا با سه مشکل هم‌زمان مواجه است: دشواری دستیابی به پیروزی نظامی، محدودیت در ایجاد محاصره اقتصادی مؤثر و افزایش هزینه‌های جهانی جنگ. در مقابل، ایران می‌تواند از موقعیت جغرافیایی خود، به‌ویژه در ارتباط با هرمز، و از حمایت یا همکاری چین و روسیه برای افزایش قدرت چانه‌زنی خود استفاده کند.
اگر جنگ ادامه پیدا کند، مسئله فقط آینده ایران و آمریکا نخواهد بود. بازار جهانی انرژی، اقتصاد اروپا و آسیا، امنیت کشورهای خلیج فارس، روابط آمریکا با متحدانش و حتی آینده رژیم منع اشاعه هسته‌ای در خاورمیانه می‌تواند تحت تأثیر قرار گیرد.</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/21262" target="_blank">📅 08:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21261">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتجارت کشاورزی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfKnk4VhF0IjHsAqDlDDiPG8ZeHDxvL0LykwbDd_yr85xZmEWj-Fps22rRk2kDPRM09dbORfTiT_1Y-Hyk9goClJEvTIouYavoMFgWk4QcDaE4jP74aUB-tQR6tIJL6p4VcVWuoaqVAc4MRL20rzo_Dq_dmpx8tFGVd2UeYW4QBhAV9WJQwebWP-kCZCLCc1ffywt2EZcdPz7to38EbU6nMDvcqJZZwxlA6yIg8BVHfVTIVmK4yB3LGrGzQyd7Usa-55H6mWFABy0IXHDvF2C5z0sNW_DNjBAqvAXc2U7lV-BMJRWZl73diAETVn5LFnkhCL22YN382posqllOB5zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابلاغیه دولتی
به اطلاع کلیه بازرگانان محترم می رساند
دولت الزیدی تا پایان هفته آینده مهلت داده است تا کالاهای وارداتی جمهوری اسلامی ایران به بازار عراق انتقال یابند.
پس از انقضای این مهلت صرفاً دو گزینه در دسترس خواهد بود ۱-پرداخت مالیات مضاعف بر کالاهای مذکور
۲- منع كامل ورود کالاهای ایرانی به خاک عراق
⚠️
این تصمیم در راستای اجرای مفاد مشارکت جمهوری عراق در تحریمهای ایالات متحده آمریکا علیه جمهوری اسلامی ایران اتخاذ گردیده است.</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/21261" target="_blank">📅 08:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21260">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">#FairValueCurve  نمایه FVC در حال نزدیک شدن به کف محدوده بیش—فروش است.  در این شرایط پرتناقض، بهترین استراتژی فروش در مقاومتهای نزدیک (4292 و 4308) با تارگت 4235 می باشد.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/21260" target="_blank">📅 07:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21259">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پنتاگون مصدوم شدن ۸ تفنگدار دریایی آمریکا در حمله موشکی ایران را پنهان کرد
به گزارش NBC News به نقل از ۳ مقام آمریکایی، ۲ هفته پیش زمانی که یک موشک کروز ایرانی به شناوری که تفنگداران دریایی آمریکا در تنگه هرمز در آن مشغول به کار بودند اصابت کرد، ۸ تفنگدار دریایی مجروح شدند.
وزارت دفاع هیچ حمله‌ای در تاریخ ۱۴ سپتامبر علیه نیروهای آمریکایی در منطقه را فاش نکرده بود.
موشک کروز ضدکشتی ایران به شناور دریایی که تفنگداران دریایی در آن مستقر بودند اصابت کرد
🔴
تفنگداران دریایی — ۷ سرباز و ۱ افسر — دچار استنشاق دود و احتمالاً آسیب‌های تروماتیک مغزی شدند که علائم ضربه مغزی از جمله سردرد را شامل می‌شد. آن‌ها بخشی از یک تیم پیاده‌سازی گردانی بودند
مقامات از تعریف نوع کشتی خودداری کرده و آن را تنها یک «شناور دریایی» نامیدند
در حالی که ایالات متحده در حال خارج کردن دارایی‌های خود است و ذخایرش بیشتر تخلیه می‌شود، گزارش‌های مربوط به تلفات آمریکایی‌ها همچنان ظاهر می‌شوند — و همچنان کمتر از مقدار واقعی گزارش می‌گردند.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/21259" target="_blank">📅 07:18 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21258">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دلار دوباره نزدیک ۲۴۰</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/21258" target="_blank">📅 00:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21257">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">خبرنگار CBS:   مذاکرات روز دوشنبه بین ایران و آمریکا لغو شد  مارگارت برنان، خبرنگار سی‌بی‌اس نوشت: یک دیپلمات که در جریان مذاکرات قرار دارد به من گفت آمریکا روز پنجشنبه پیش‌نویس ایران را بررسی و آن را همراه با بازخورد و ملاحظات خود بازگردانده است.</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/21257" target="_blank">📅 00:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21256">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">خبرنگار CBS:
مذاکرات روز دوشنبه بین ایران و آمریکا لغو شد
مارگارت برنان، خبرنگار سی‌بی‌اس نوشت: یک دیپلمات که در جریان مذاکرات قرار دارد به من گفت آمریکا روز پنجشنبه پیش‌نویس ایران را بررسی و آن را همراه با بازخورد و ملاحظات خود بازگردانده است.</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SBoxxx/21256" target="_blank">📅 22:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21255">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">بنیامین نتانیاهو دستور داده است که یک تیم بین‌وزارتی و مقامات حقوقی پرونده‌ای علیه رجب طیب اردوغان، رئیس‌جمهور ترکیه، در دادگاه کیفری بین‌المللی (ICC) آماده کنند.
پرونده پیشنهادی عمدتاً بر «رفتار ترکیه با جمعیت کرد خود» و ادعاها مبنی بر اینکه دولت اردوغان حماس را تأمین مالی کرده، تمرکز خواهد داشت.</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/21255" target="_blank">📅 21:51 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21254">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">به نظر من جمهوری اسلامی بزودی گزینه آخرالزمانی حمله به چاههای نفت و تاسیسات انرژی منطقه را فعال خواهدکرد که در پی آن نفت به بالای ۱۳۰ دلار و طلا به زیر ۴۰۰۰ دلار خواهندرفت.</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/21254" target="_blank">📅 20:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21253">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">عراقچی:  ما برای جنگ آخرالزمانی آماده هستیم</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/21253" target="_blank">📅 20:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21252">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">عراقچی:
ما برای جنگ آخرالزمانی آماده هستیم</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/21252" target="_blank">📅 20:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21251">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پلیس ضدتروریسم بریتانیا در حال بررسی این موضوع است که آیا ایران با طرح ناکام‌مانده حمله به پایگاه هوایی در پایگاه نیروی هوایی سلطنتی فیرفورد (RAF Fairford) ارتباط دارد یا نه.</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/21251" target="_blank">📅 19:41 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21250">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/904c5f3c14.mp4?token=slLXL4x70IzLVH4-uxVWxSdJe1Dnz9z3DaB4WNwibTvYkr9H48oHnt8gf6H94PE_CZcM45GrrW4sp8mF3gnC9Ec8_KGNzIxDNPLA7Vg73sbuA3CE7FvGQFU5hAmdYDYy_NpeqSMtJ-ddkqAetWfF26XFL2sBPEfivv_c-wN50TkjVPg7yl4FjrRrnBD2WeKD_E3PhnkdbMDb_RWgbpxWJ8LkIkWExnpBMl2VhAcaLMwtpPT3qSGfG7FO6GlMLFs-ywNMAkDLSPeOPBczzrzelepMk4wEI-_SwcGLjfnux34hlVDI38xvKq_0b_r8iTX8EoYQ5JrY1oWC_kQfWv7z4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/904c5f3c14.mp4?token=slLXL4x70IzLVH4-uxVWxSdJe1Dnz9z3DaB4WNwibTvYkr9H48oHnt8gf6H94PE_CZcM45GrrW4sp8mF3gnC9Ec8_KGNzIxDNPLA7Vg73sbuA3CE7FvGQFU5hAmdYDYy_NpeqSMtJ-ddkqAetWfF26XFL2sBPEfivv_c-wN50TkjVPg7yl4FjrRrnBD2WeKD_E3PhnkdbMDb_RWgbpxWJ8LkIkWExnpBMl2VhAcaLMwtpPT3qSGfG7FO6GlMLFs-ywNMAkDLSPeOPBczzrzelepMk4wEI-_SwcGLjfnux34hlVDI38xvKq_0b_r8iTX8EoYQ5JrY1oWC_kQfWv7z4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/21250" target="_blank">📅 19:36 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21249">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GRwq7wzpVhLFoCBb0V4XDC70Ypq56imUzIvBtbtBVbm4T3i1irY7sPDzx6ef2GnaD6v0eR72aPlY0Dh-KMcVRsisZxh21uHOqFg6x0K6em_H6hgkpTpp_JZHTWZkh0Z5Zcsp5E9BDCxoTMt1WyJzRnYCcTVY8guavnp6wntNkNFLAxG1RG6EKo0dFVOmADVNPV7bZUwmqVj2zTB268QeuWyR6_JJYKvqooTTyP7yqn336IQMphJ3m-mvJeJ3-s3UEsUDgPhDEMk4_gblm1vATBrBLaEfiy74juwffSlML3axH6E4uEH5Iw7jSGIf5a-JbP2u_1-uviWeLGhjHdr-rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/21249" target="_blank">📅 19:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21248">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا:
به احتمال زیاد، اقتصاد ایران در دو هفته آینده فرو خواهد پاشید
انزوای اقتصادی ایران به صورت مرحله‌ای اجرا می‌شود و ارزهای دیجیتال، هوانوردی و حمل‌ونقل دریایی را در بر می‌گیرد.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/21248" target="_blank">📅 19:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21247">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">حرف درستی است. به این پفیوزها گاز و برق ندهید دستکم خودمان اینقدر قطعی نداشته باشیم.
زیبنده ابرقدرت چهارم دنیا نیست.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/21247" target="_blank">📅 19:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21246">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-qMtmeQZCVpzNaR97uva5ANC_8q7re1motTw_B8YL4-xcCfELZW__gpMi0HMYBXRUiNc4ZqhCwnfRjbM5jgRT4ROy7jsTN22AzWGUnwhsMW1eA4KwZYBunhC0Wap01yzWVcP4oIDpbqUWxVMt4v5bzMVFObE6L9ZnOi0XvClAedp0bO1CJYvsX-irRbPr093gX_rHX3fGl3XuB04_-uKY4zDT8QiFtbf5QxjCQ5PQ8yNLU6LFXbNZTEJYt5xQrPx2_UB9NT6--c_JMy4iNuFPA66jsUaYP0rsEBz-y8cHzDx3a1wpwiTmbXDE3zxIy3ZZCni6K5LUN3lQxlBSb8Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران انقلاب اسلامی ایران امروز مدعی شد که یک پهپاد زیرآبی خودکار ساخت آمریکا به نام Remus 600 را در نزدیکی تنگه هرمز به دست آورده است. نام‌گذاری نظامی این وسیله توسط ارتش آمریکا، Mk 18 Mod 2 Kingfish است.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/21246" target="_blank">📅 19:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21245">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">رابرت کیوساکی (Robert Kiyosaki)، نویسنده کتاب «پدر پولدار، پدر بی‌پول»، به دارندگان حساب‌های بازنشستگی هشدار داد که ممکن است فروپاشی‌ای در مقیاس سال ۱۹۲۹ در راه باشد، و بیش از یک سال بعد، این فروپاشی رخ نداده است.
کیوساکی در ژوئیه ۲۰۲۵ در ایکس نوشت: «آیا حساب 401(k) یا IRA دارید که پر از سهام است؟» او به وارن بافت (Warren Buffett)، رئیس برکشایر هاتاوی (Berkshire Hathaway)، و جیم راجرز (Jim Rogers)، هم‌بنیان‌گذار صندوق کوانتوم (Quantum Fund)، اشاره کرد و مدعی شد آن‌ها بیشتر یا همه سهام و اوراق قرضه خود را فروخته‌اند و پول نقد یا نقره نگه می‌دارند. او افزود: «اگر نمی‌دانید چرا بافت و راجرز سهام و اوراق قرضه‌شان را فروخته‌اند، ممکن است بخواهید علتش را بفهمید.»
او جایگاه خود را متفاوت توصیف کرد. کیوساکی نوشت: «من محکم روی طلا، نقره و بیت‌کوین می‌نشینم» و سپس افزود: «ممکن است در آستانه فروپاشی دیگری مانند ۱۹۲۹ و رکود بزرگ دیگری باشیم.» او همچنین هشدار داد که بدهی آمریکا از کنترل خارج شده است و این کشور فقط «تا مدت محدودی» می‌تواند به چاپ پول ادامه دهد.
البته این پیش‌بینی محقق نشده است. شاخص S&P 500 به صعود خود ادامه داده و در سال ۲۰۲۶ به بالاترین سطح تاریخی رسیده است، نه اینکه فرو بپاشد.
کیوساکی همچنان درباره سهام، صندوق‌های قابل معامله در بورس (ETF)، صندوق‌های سرمایه‌گذاری مشترک، حساب‌های 401(k) و IRA هشدار می‌دهد و در همان حال طلا، نقره و بیت‌کوین را تبلیغ می‌کند. استدلال اصلی او ثابت مانده است: سرمایه‌گذاران نباید صرفاً به این دلیل که دارایی‌های سنتی آشنا هستند، فرض کنند که امن‌اند.
تمایز مهم، میان آماده شدن برای یک رکود و تلاش برای زمان‌بندی دقیق وقوع آن است.</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/21245" target="_blank">📅 19:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21244">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVaWj7fDWEYsiOxsoaFXdLv3SNOh7UaqIFal75-3qQIdy_eOYlo5IP5Y8J7EmQZkVWxc7wB17AIDwI15TZTL8P3D9IQeG3pJ5epD1537cLLy167sP811OqkwkzVsbGrygle_iGWcBasmvSF_sWWtPy88xlld3TYkamqCf7_ZGBmyCjkQkpjsjvHcV3B79ppGttHNLE-dWzQrRxgLuiFxKibNlSKN1UiEeE5YndGCHnY71KU_OpFEbLbL770BQT_s3dHObdBuWLKxW81-cWY_urAGHw0um6lrweVGSs_I5dyX5qp5eaDGqeQk_nmwlPQfPaSCnCRWKOAlHs7ZgZbVxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SBoxxx/21244" target="_blank">📅 17:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21243">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">حاجی‌بابایی، نماینده مجلس:  ایران باید با قدرت [مسیر] انرژی را بر روی همه ببندد؛ یا همه یا هیچکس  نایب رییس مجلس با بیان اینکه امروز مقاومت با محوریت ملت بزرگ ایران تازیانه الهی بر فرق ترامپ جنایتکار است، گفت: تنگه هرمز همان دریا و همان رودی است که فرعون در…</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/21243" target="_blank">📅 13:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21242">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">حاجی‌بابایی، نماینده مجلس:
ایران باید با قدرت [مسیر] انرژی را بر روی همه ببندد؛ یا همه یا هیچکس
نایب رییس مجلس با بیان اینکه امروز مقاومت با محوریت ملت بزرگ ایران تازیانه الهی بر فرق ترامپ جنایتکار است، گفت: تنگه هرمز همان دریا و همان رودی است که فرعون در آن غرق شد؟ آیا آمریکا در منطقه و در تنگه هرمز در نبرد با ملتی که خدایی فکر می‌کند و توحیدی فکر می‌کند غرق نخواهد شد؟ دیپلماسی با قدرت امکان‌پذیر است و ما باید حرفمان را از قدرت و اقتدار و جایگاه قدرت اقتدار بزنیم.</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/21242" target="_blank">📅 13:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21241">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">باز هم تاکید میکنم خواهرمیانه جای مبتدی ها نیست :
حکم ۱۰ ماه زندان حمید رسایی اجرا می‌شود</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/21241" target="_blank">📅 12:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21240">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LG1oa5FgC3znl3iaR3rMGKRxFmah8shghCC79bK1LGzz9K2R7skmHc56qzLhchiVlKL9_7Jj_OaiYxv7Qnjl7dgMMxSHt3BWjrnjn065d2b-6urghGCh0lFxE1Z3v74HZiASzIyVeNGN3cKgW4lAsEpQkFp4FagzkRV38RwSFDSnQm8dDP92Zt7qR2O-ca-01B5N8rvTR9HamqR984MeFZ1E3iqIcIb8d5N81Rs5mY0YCS0mIAvc-EjGJOk32f7oE6wEAJbKhnBo_k_eLk0KQH6lw0dJ4as4zwwq8561HMLVjUP8PQwluDopMfvydXPGTvuF0KyjhOVBRjKp80nNUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواهرمیانه برای مبتدی ها نیست!</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/21240" target="_blank">📅 12:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21239">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">وقتی برخی سرمایه گذاران به امانتداری بانک انگلستان با ۴۰۰ سال سابقه برای طلایشان شک می‌کنند؛ در عجبم از ملتی که در پلتفرم های آنلاین ایرانی طلا میخرند!  راستی میدانستید آلمان چند سال است از آمریکا درخواست انتقال طلاهایش از فدرال رزرو به انبار بوندس بانک در…</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/21239" target="_blank">📅 10:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21238">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سپاه
پاسداران:
در یکی از بزرگترین عملیات‌ها  دقایقی پیش 7 نفتکش اماراتی در تنگه هرمز مورد هدف قرار گرفتند</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SBoxxx/21238" target="_blank">📅 09:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21237">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">یک نفر دایرکت داده خب استاد ما که به قله رسیده و سرش نشسته ایم، حالا اگر پنبه نایاب شد بیاییم خود قله را آغشته به روغن بنفشه کنیم!</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/21237" target="_blank">📅 09:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21236">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترسم این است که پنبه هم نایاب شود؛ آن وقت با چی روغن بنفشه را داخل آنجایمان قرار بدهیم؟!  اصلاً آدم یک جوری می شود!</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/21236" target="_blank">📅 09:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21235">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">شیوه درست استفاده از روغن بنفشه</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/21235" target="_blank">📅 09:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21234">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/134b1ed686.mp4?token=tJlI4wxnOwsk1gHaVI31HPRPJ3ytsJcp2VskJPWZ1xJiViNNSE2Tarw6V2itDYyrl8cqj9eUidmv6dK9YhwvK90V7GA1IwHG-hv6Mv0P_1lyL84EUypi_-2bGsiUT_et2v845M_k1wScdxrZhqeAzaUJqNdIFWCj48_5RpnTlc1MQdW2um6wqmLE0OOEN2cPYqzjIs4iqj_3iQsu2ABpiwlY55ZbwhPSqLZC72JcnH07jN8pnTMPFTWjRgXy_gniL4RpZpWiXhqtd_kdLHhPH5tTCDydXgkuDG26sy_FHxCYUGJeJpxTsTmpBEMEB3r2cr6DKgQ1E2nlmBZHds-AXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/134b1ed686.mp4?token=tJlI4wxnOwsk1gHaVI31HPRPJ3ytsJcp2VskJPWZ1xJiViNNSE2Tarw6V2itDYyrl8cqj9eUidmv6dK9YhwvK90V7GA1IwHG-hv6Mv0P_1lyL84EUypi_-2bGsiUT_et2v845M_k1wScdxrZhqeAzaUJqNdIFWCj48_5RpnTlc1MQdW2um6wqmLE0OOEN2cPYqzjIs4iqj_3iQsu2ABpiwlY55ZbwhPSqLZC72JcnH07jN8pnTMPFTWjRgXy_gniL4RpZpWiXhqtd_kdLHhPH5tTCDydXgkuDG26sy_FHxCYUGJeJpxTsTmpBEMEB3r2cr6DKgQ1E2nlmBZHds-AXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عزیزان پنبه و روغن بنفشه به همراه داشته باشید که داروهای مدرن نایاب می شود.  در ضمن انجام سرویس تعویض روغن به صورت رایگان انجام می شود.</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/21234" target="_blank">📅 08:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21233">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqGOxGdR29DC03CA8lRUJwMhS7xtlr8bE-IwSBoX7HNNXyJlYZftAxNSEdzeO0T7Tp0hPNMrMMzgwcpyfrl0tiOJFoAz2g_Qf_RGllHR-_z1tVUEoS0l2sn7Kstjvyl4-P96uywNkpyUQyHu4d7cxqsOa8CyQty-J5udnfsY9yyYwTLV47GzzZS5rpIe9xtUN1RIMqRZfzPmJmYB9b_zQ9BiFSBKYYqZfGQzIyjghCd7svR04L7QlWNk9AsjQdPFL2deDaNJbDw5Xax_iD_Q4fiC8JK_Jz87cKc3zcHNtwYl6Sws_xzUmYdN_XsU46RMvROYBgS5aQN-1YeLWEhgxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزیزان پنبه و روغن بنفشه به همراه داشته باشید که داروهای مدرن نایاب می شود.
در ضمن انجام سرویس تعویض روغن به صورت رایگان انجام می شود.</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/21233" target="_blank">📅 08:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21232">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بوی محاصره زمینی می آید…</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SBoxxx/21232" target="_blank">📅 08:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21231">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">حملات موشکی گسترده سپاه در تنگه هرمز</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/21231" target="_blank">📅 07:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21230">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vjSpe7XeAfSiJ-WrCPXVEGQW6ApzPVwVSrDhXs6-GXSfPCZyHM_JZrKoBU6rnYQUeajGL5n2ij2r0DSe3dcyBFbNnqpsKQHjyUW_Qw2yhIMq5r_gDjPT4R1WW3MIetEmhe7HSRzJzZxQaeKqfgTn4zJc9EQ-d1PtFwtx2yAImro78dJDUUjPwKXT3EYHtp9joZ2BX62BOYMoHWIAHr8R-pMTbZZ9Upk9grWDuJOLyjJkFrjCGUVIMWPjxuPGB6vlCPWb0n2TDI8GAcNqePGnu8jO_XZiwA9zVhvNcunFsTVxKcrnkYan6IjCJct_52CMeD8Kp-6GYMbdItouNjXlIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید براتون جالب باشه
فرودگاه نجف عراق که اجازه پرواز به هواپیماهای ایرانی رو نمیده ،
توسط جمهوری اسلامی ساخته شده
😄
شب خوش!
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/21230" target="_blank">📅 01:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21229">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">واشنگتن و پکن؛ پیام مشترک درباره ایران و تنگه هرمز
در یکی از قابل‌توجه‌ترین بخش‌های دیدار اخیر دونالد ترامپ و شی جین‌پینگ، موضوع ایران نیز در گفت‌وگوهای دو رهبر مطرح شد؛ موضوعی که می‌تواند برای تهران و به‌ویژه آینده تنگه هرمز اهمیت ژئوپلیتیکی قابل‌توجهی داشته باشد.
بر اساس فکت‌شیت منتشرشده از سوی کاخ سفید، ترامپ و شی درباره نگرانی‌های جهانی از جمله ایران گفت‌وگو کردند و بر دو اصل تأکید داشتند: ایران نباید به سلاح هسته‌ای دست پیدا کند و هیچ کشور یا نهادی نباید برای عبور از آبراه‌های بین‌المللی عوارض تعیین کند.
اگرچه در متن جدید نام «تنگه هرمز» به‌طور مستقیم ذکر نشده، اما این بند در شرایط کنونی به‌وضوح با مناقشه هرمز ارتباط پیدا می‌کند. اهمیت موضوع زمانی بیشتر می‌شود که بدانیم در مواضع قبلی واشنگتن و پکن، مسئله بازگشایی هرمز و مخالفت با دریافت عوارض برای عبور کشتی‌ها صراحتاً مطرح شده بود.
از منظر تهران، نکته مهم صرفاً محتوای این دو موضع نیست؛ بلکه هم‌زمانی مواضع واشنگتن و پکن اهمیت بیشتری دارد. چین بزرگ‌ترین خریدار نفت ایران و یکی از مهم‌ترین شرکای اقتصادی تهران است و در بسیاری از پرونده‌های ژئوپلیتیکی در برابر فشارهای آمریکا موضع متفاوتی داشته است. بنابراین هم‌صدایی آمریکا و چین درباره اصول مرتبط با هرمز می‌تواند فضای مانور دیپلماتیک ایران را محدودتر کند.</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SBoxxx/21229" target="_blank">📅 20:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21228">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M30sz3YEKPH9g3BNRnvfwYBfx29hIb34qYceRtW2AYZje0YPnNX7Z7Wd3dolJqvuILswbHNMY8isN6StTEc1QYt1patVCMsuxSJ0I_bTJ9A0I0HlXcjAdQa2GT1QeRJEE5pd8nJJhd2dCUXm64n9oIw5xj5ngxB8QeNFHFgWYKELTF2BUE4pkSiing2yT73VW_tejqx1he8pIqgjR5ygO1r4hgidXrlBhIMstn6QQLLpkIHBckaTJrQydQRKrb-Mk1qgAbazGd-njoUnGKmnYrfVUmVXY_PDtAsSCA7AAyBot7BT2NnstLRHypm91ay0y_ELdLNcTmnGEa3v98me3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجم عملیات انتقال کشتی‌به‌کشتی (STS) در دریای عمان نسبت به سطح ماه فوریه، ده برابر شده است.
تولیدکنندگان نفت را بارگیری کرده و با عبور از تنگه هرمز از طریق مسیری جایگزین که امنیت آن توسط ارتش آمریکا در نزدیکی سواحل عمان تأمین می‌شود، محموله‌ها را برای تحویل به خریداران نهایی به کشتی‌های بزرگ‌تر منتقل می‌کنند.</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SBoxxx/21228" target="_blank">📅 19:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21227">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">شورای عالی امنیت ملی:  «ادعاهایی مبنی بر اینکه ایران به محدودیت‌های اخیر هوایی با اقدام نظامی پاسخ خواهد داد، نادرست است.  مذاکرات با کشورهای ذی‌ربط برای لغو ممنوعیت‌های غیرقانونی پرواز به‌طور فعال در جریان است.  در صورت لزوم، اقدامات متقابل غیرنظامی برای…</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/21227" target="_blank">📅 18:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21226">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">مخبر، مشاور رهبر انقلاب:  پرواز در منطقه یا برای همه آزاد است یا برای هیچ‌کس  اگر ایران امکان پرواز و دریافت خدمات فرودگاهی نداشته باشد هیچ کشوری در منطقه هم این امکان را نخواهد داشت.</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SBoxxx/21226" target="_blank">📅 17:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21225">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پسری ۹ ساله ارمنی‌تبار مسیحی در اورشلیم، پس از آنکه به دلیل دوچرخه‌سواری و استفاده از هدفون در روز عید یوم کیپور مورد اعتراض قرار گرفت، توسط شهرک نشینان یهودی با اسپری فلفل مورد حمله قرار گرفت.
تصاویری که از
کانال ۱۳
اسرائیل پخش شد، نشان می‌داد که این کودک که نامش ویلیام است، پس از این حمله در حال دریافت درمان پزشکی از سوی تکنسین‌های اورژانس در یک آمبولانس است. این درگیری در نزدیکی شهر قدیم رخ داد، زمانی که ویلیام در حال دوچرخه‌سواری و گوش دادن به موسیقی بود.
گزارش‌ها حاکی است که مهاجمان از پسر خواستند هدفون خود را در بیاورد. پس از آنکه او این کار را انجام داد و به زبان انگلیسی صحبت کرد، فریاد زدند: «انگلیسی نه، یهودی‌ها» و سپس مستقیماً اسپری فلفل را به سمت او پاشیدند.</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SBoxxx/21225" target="_blank">📅 15:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21224">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">وزیر امور خارجه آذربایجان، بایراموف:
اگرچه دهه‌ها درگیری با ارمنستان تراژدی عظیمی بر مردم ما تحمیل کرد و زخم‌های عمیقی بر سرزمین ما باقی گذاشت، آذربایجان انتخاب کرده است که به آینده نگاه کند و صفحه دشمنی را ورق بزند.
ما صلح را به ارمنستان پیشنهاد دادیم که کاملاً مطابق با هنجارها و اصول حقوق بین‌الملل و مبتنی بر شناخت متقابل و احترام به حاکمیت و یکپارچگی قلمرو یکدیگر است.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/21224" target="_blank">📅 14:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21223">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">حقیقتا خواهرمیانه جای مبتدی ها نیست!  از ۶ ماه پیش بلایی نبوده که جمهوری اسلامی و نیروهای نیابتی اش سر این سعودی های فلک زده نیاورده باشند؛ بعد این هفته جشن باشکوهی به مناسب ۹۶-امین سالگرد تاسیس کشور سعودی در قلب تهران برگزار شده!  سبحان الله!</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/21223" target="_blank">📅 14:11 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21222">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzpBX77umvZ8WnvByfcsVFD2-077mrrw5wgAAyO0enAaeArK2QwtZQ820m6xnyA4jTsdpe8G-bCwk7XsArrZ3FmQ9fNcZlSf50ytLyIGy163X5TWUhSvff_RntNMqJcPzsYnaq0CkZlH5fCBG7Pj74g8GH0snn7BiWxLcgVpdBVkmPkW9AH8MeclvsEGIpKDjTch8gk9dpIZAOf-cnme2CNIZhjb4h-iC66NZlrIQ_64p0kVgPj2F1294Flx495iev7tQtHmTUBpNt6N1ApKDtc0qWBcB5H8YCMdFdNs7HMyeZEOFDsKZSBriUHrrpQveaMEAzm9PTVPNetpImr4UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برآورد درصد مسلمانان نسبت به جمعیت هر کشور در اروپا در سال ۲۰۵۰</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SBoxxx/21222" target="_blank">📅 13:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21221">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpnRvaXwLslOOZ6eAiow3OJi1A7QYPdzF-dw79VqGE0HA1fECmtYBjI84jw7jIbLHWopStfOEvHU4fTGhBJPGIEn5QAGtjYTZnIz8LHyY7eNVf0WAbiDnqvBoOm0oLt8fs2o-iVdogo56_YstsnXVl4iTzoaret7M7SM5KWboanp0TH1UFjLcWH2n0kqXS-DMzw47pLGsoAZhTpRgJgbCXXoep-AN42w6Z0nLrOerzBolGX2TPW3bVBSCY0n4etY-rhzmiLjJqpJ9981FPWF3zbrRVeSwJbZacqOBKRrWtLxXuS5MScZeQ6l5WT-3vekziXXd7GdTDbFLsgeCmxUDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشاره دوباره ترامپ به تنگه هرمز به عنوان تنگه ترامپ !</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/21221" target="_blank">📅 13:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21220">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ، رئیس‌جمهور ایالات متحده، پیشنهاد ایران برای آتش‌بس هفت‌روزه را رد کرد و به دستیاران خود گفته است که انتظار دارد بمباران‌های آمریکا علیه ایران پس از انتخابات میان‌دوره‌ای نوامبر از سر گرفته شود.  طبق پیشنهاد ایران قرار بود تنگه هرمز بازگشایی و مذاکرات…</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/21220" target="_blank">📅 08:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21219">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07644aa8e4.mp4?token=Us9EITD468rWRXEWySSaOnW6gFKCB6wPn1O68n2yvVKepOpMygHszVbHPhhKklnKuW3PWjA8Zy8UBrDf_OwmLEtWkAxdOWzG1JnlBe4BC_NpQG9U4CypaGSWf453bmEcWLhDdoi2zt7tTmolthsEH3ZBoDfSCaToTNXx2hlgcUriGLdBS_OCusM2o28Gzco3Ku2t-Lr31zgRjrS0xcIYNjS7Ovb-AHa0io5VFfP9HEfPiB9mxsODGLgIoop4xlSQ_Q8IEUCt3pu2sWlMZq5UHznikDFMeTAy5GfvhXniHjkvCJqvEdOGjIJnpx-nhtMOkL2fK7uU5o_Cjrk7LbRm9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07644aa8e4.mp4?token=Us9EITD468rWRXEWySSaOnW6gFKCB6wPn1O68n2yvVKepOpMygHszVbHPhhKklnKuW3PWjA8Zy8UBrDf_OwmLEtWkAxdOWzG1JnlBe4BC_NpQG9U4CypaGSWf453bmEcWLhDdoi2zt7tTmolthsEH3ZBoDfSCaToTNXx2hlgcUriGLdBS_OCusM2o28Gzco3Ku2t-Lr31zgRjrS0xcIYNjS7Ovb-AHa0io5VFfP9HEfPiB9mxsODGLgIoop4xlSQ_Q8IEUCt3pu2sWlMZq5UHznikDFMeTAy5GfvhXniHjkvCJqvEdOGjIJnpx-nhtMOkL2fK7uU5o_Cjrk7LbRm9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی عبدی برنامه آمریکا و اسرائیل برای جنگ بعدی علیه ایران را نفوذ آبی و خاکی و هلی برن از سمت خلیج فارس، غرب(عراق)، جمهوری باکو، آسیای مرکزی و جنوب شرق (پاکستان) دانست و تصریح کرد حملات هوایی، تلاش برای شکار شاه مهره و استفاده از بمب اتمی تاکتیکال نیز رخ خواهد…</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/21219" target="_blank">📅 08:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21218">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ، رئیس‌جمهور ایالات متحده، پیشنهاد ایران برای آتش‌بس هفت‌روزه را رد کرد و به دستیاران خود گفته است که انتظار دارد بمباران‌های آمریکا علیه ایران پس از انتخابات میان‌دوره‌ای نوامبر از سر گرفته شود.
طبق پیشنهاد ایران قرار بود تنگه هرمز بازگشایی و مذاکرات هسته‌ای در ازای رفع محاصره بنادر ایران توسط ایالات متحده و کاهش فشارهای اقتصادی بر تهران، از سر گرفته شود.
— وال استریت ژورنال</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SBoxxx/21218" target="_blank">📅 07:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21217">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سفیر ایالات متحده در چین، گفت که رئیس‌جمهور ترامپ در مذاکرات خود در کاخ سفید، از رئیس‌جمهور چین، شی جین‌پینگ، خواسته است تا هرگونه کمک چین به ایران را متوقف کند.
او اظهار داشت که واشنگتن به وضوح اعلام کرده است که «هرگونه کمکی که چین به ایران ارائه می‌دهد، کاملاً غیرقابل قبول است».
او افزود: «ما از قبل حرکتی در این زمینه مشاهده کرده‌ایم. این همان تعهدی است که داده شده است. آن‌ها به ما اطمینان دادند که چنین کاری انجام نمی‌دهند.»</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/21217" target="_blank">📅 02:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21216">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">فیلم کامل مستند BBC درباره نسل کشی ترکیه ضد کردها در عراق</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/21216" target="_blank">📅 00:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21215">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ada5e22fc.mp4?token=tESFK8KCyZA6Or2lUCzl28KMBr34bCSRNlHa4pdmKO1si7xBFuwHFR6_2TJpcyxVM7kaBrWa8YU9vAk6apnUyKgvJC-JCLYaxK8iOyw1mvkAidaGBOnb6l4PHtPBOUsQK4sCesRBlDeLCglyjQEa6PrloxDMZ4T3nfc_GombGno8pyxU2quOO35heckSIPhhsVi5FIvAi3Qc5DbMRDxi3RvSwCszT8UoDplUPpPzwo9CszZhNTE-PYzTq65lVLv6RdEQTiNZaZBkdcv-XH2FuES6nzRLb5U2SlPq_4LlbzLp9f0jsHvflmn6UDVSarVaTEW0HzGhqoSygO7jiwX5Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ada5e22fc.mp4?token=tESFK8KCyZA6Or2lUCzl28KMBr34bCSRNlHa4pdmKO1si7xBFuwHFR6_2TJpcyxVM7kaBrWa8YU9vAk6apnUyKgvJC-JCLYaxK8iOyw1mvkAidaGBOnb6l4PHtPBOUsQK4sCesRBlDeLCglyjQEa6PrloxDMZ4T3nfc_GombGno8pyxU2quOO35heckSIPhhsVi5FIvAi3Qc5DbMRDxi3RvSwCszT8UoDplUPpPzwo9CszZhNTE-PYzTq65lVLv6RdEQTiNZaZBkdcv-XH2FuES6nzRLb5U2SlPq_4LlbzLp9f0jsHvflmn6UDVSarVaTEW0HzGhqoSygO7jiwX5Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اثرات خانمانسوز جهش دلار روی مغز مردان سرزمینم!
گفته می شود ایشان قبلاً پرایس اکشن کار بوده که بعد از 36 بار کال کردن اکنون وارد مباحث تشکیل سبد و تخمگذاری در آن شده است و گرنه این حجم از آشنایی و تسلط بر مفاهیم بازاری نمیتواند از دهان یک اسکل معمولی بیرون بیاید!</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/21215" target="_blank">📅 23:23 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21214">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">علی عبدی برنامه آمریکا و اسرائیل برای جنگ بعدی علیه ایران را نفوذ آبی و خاکی و هلی برن از سمت خلیج فارس، غرب(عراق)، جمهوری باکو، آسیای مرکزی و جنوب شرق (پاکستان) دانست و تصریح کرد حملات هوایی، تلاش برای شکار شاه مهره و استفاده از بمب اتمی تاکتیکال نیز رخ خواهد…</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/21214" target="_blank">📅 23:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21213">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">— تًن ماهی — گوشگیر سیلیکونی — آب معدنی — چسب زدن شیشه ها</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/21213" target="_blank">📅 23:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21212">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">علی عبدی برنامه آمریکا و اسرائیل برای جنگ بعدی علیه ایران را نفوذ آبی و خاکی و هلی برن از سمت خلیج فارس، غرب(عراق)، جمهوری باکو، آسیای مرکزی و جنوب شرق (پاکستان) دانست و تصریح کرد حملات هوایی، تلاش برای شکار شاه مهره و استفاده از بمب اتمی تاکتیکال نیز رخ خواهد داد، ولی پیروزی از آن ملت ایران خواهد بود.</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/21212" target="_blank">📅 23:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21211">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">به پزشکیان رای دادیم که جنگ نشود، هر هفته 15 بار جنگ می شود!</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/21211" target="_blank">📅 23:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21210">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">به پزشکیان رای دادیم که جنگ نشود، هر هفته 15 بار جنگ می شود!</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/21210" target="_blank">📅 23:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21209">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">خداوکیلی راست می گوید ؛ این بار دیگر غافلگیر نشویم!</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/21209" target="_blank">📅 23:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21208">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CY-EpRMAvCOOMv-GfUUqy6qIBRfEubGrdSgqCyt34UMvL8Rps7aSN_8zeEnHmAd3GCv9s-pZyV80KoogwzDH_fjQBUDs-aIFbifFVBjPifTJblcI5WM7OAZC4oTT1FSvDMRS6cK0xdKPeN2d0ZCCSb8POrkeaYrwatLqYZ4N7LliKpLhCC90YqfpI7qS_YvyZuKx6XZe0GEzLUNQv39n0wi3fBCJbqMiBwmGMD8Gg8ny4wdKqi7KxsjVXQDYoGCMspqgWrjwSDYjZ9qrVoHabP8Hp7VWTyutptQrVlsTu8pUmk3mlPM8vkU9N0X2UFhUy7SKIN5AMtLPDUmBcWTcPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من شخصاً هیچ وقت به نزدیک بودن توافق ایران و آمریکا توجه نمی کنم ولی اعتقاد دارم نزدیکی ایران و آمریکا نزدیک است.</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/21208" target="_blank">📅 23:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21207">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">چرا می خند؟!</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/21207" target="_blank">📅 22:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21206">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eX6S8NwYCO_AIszQJ0WKmSzQumUCa9XknklV--h27YA4DMb4ZUy2XFrJi975wGbR9537ZrdCGOfzjMzYA24XyxZUtvMKRcIL1toIvX4ys2Cjdg11J0SPG8WUbHoRcnMIS0cn4dwrE0XwCBdeLPmTi1pAzguN1wo9q_loB1a74XXasTC37nZ3a6htXpVMEgRVjlEySS2SOXBM2czemLhUN0EO4QxwNAcVlcM8MHIqQE-nIkLUolsKtzeJ0VCrne_OqTcNQK1gYVBEoXfSbd9S9aIfs_jLlLdNQ8osykqmfRQ-B1zwswV9PGE8Bh3STnMN-uqnHBRjHwIk_TT8uQSASg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">First Time ?</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/21206" target="_blank">📅 22:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21205">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مرندی ذوالاکتاف:
هیچ پیشرفتی در مذاکرات غیرمستقیم با رژیم ترامپ حاصل نشده است. منطقه به سوی تشدید تنش پیش می‌رود، چرا که دیکتاتوری‌های حوزه خلیج فارس که در جنگ علیه ایران همدست بوده‌اند، به توطئه ترامپ و بسنت علیه ملت ایران می‌پیوندند.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/21205" target="_blank">📅 22:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21204">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMjIUQwYWshuPhPfMpiRpr7OCfInFTWC54wDN9B1tZw1fqhhR_OzQ1RPq5AYrLpPbSrbUnjYLqkOf1wiYWXI0KeyInWSnizxFzl5qvNmLHTEP5041akfHm5YCVhmbTYYsc0c5yXHKrotYgYZeNFjC5ecgMeeGWqITT25_YwP1Yo1hPqeBD0PanB2sWI8ZMEZXYet4reF-VuRZv3wAmAMAKUaMCcxG_cUfUDI0D32GiLVYJl-SGe7SpQZ2DaZjf4fXPgxcsFYhanHygkrjfkE067tsGDD1BPOspiT75y3gc7WdcAKLhXZmOBjhs4bO2b8FETC6mE4qbQrTeLDbD7IPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محدوده 4255 بسیار مهم است.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/21204" target="_blank">📅 22:41 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21203">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrpt7Bhx9rBkL7UnuK6lptTH4S4DQEwxLZnhcSmX1uWUga8dfNM20jg51g3mF7tbIf2saqmYL5kTTzj-BuXnACZAJYBFhao7shAXFFrcK7PbvXu21XjRF9Z_QEQ-lV3Q45fAFg8NrbT1SBPoeh5UCpVAWfIDyP-4U4YGXuR8rSXYgw0VBx_5-4rsLghdgJM6f021-XQg9YlaKC1dXdbIKIpmMA6oOj4P5IVQAtMgodVa4g8-oTGPl7A4CDSD6o3h2DWz-BRVSWQmvSTf9-04l5vWqZNCYSWpMB4IGCAi-4JnPmj5jKtjhANsYff4JSc8k7E6CUreFQoaaqtqT9ptrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حقیقتا خواهرمیانه جای مبتدی ها نیست!
از ۶ ماه پیش بلایی نبوده که جمهوری اسلامی و نیروهای نیابتی اش سر این سعودی های فلک زده نیاورده باشند؛ بعد این هفته جشن باشکوهی به مناسب ۹۶-امین سالگرد تاسیس کشور سعودی در قلب تهران برگزار شده!
سبحان الله!</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/21203" target="_blank">📅 21:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21202">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">Ali SharifAzadeh – انتخابات اسرائیل</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/21202" target="_blank">📅 21:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21201">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ
:
در نوامبر در چین دوباره با شی ملاقات خواهیم کرد</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/21201" target="_blank">📅 20:49 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21200">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">First Time ?</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/21200" target="_blank">📅 20:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21199">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‏ قائم‌پناه:
به عربستانی‌ها گفتم انشاءالله برد موشک‌های ما به آمریکا برسد تا دیگر به پایگاه‌ آمریکا در کشور شما حمله نکنیم بلکه به خود کاخ سفید موشک بزنیم.</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SBoxxx/21199" target="_blank">📅 20:17 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21198">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سفیر آمریکا در چین:
پکن در پی هشدار ترامپ، بخشی از حمایت‌ها از تهران را متوقف کرده است</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/21198" target="_blank">📅 19:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21197">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">میانگین 200 پیپ</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/21197" target="_blank">📅 18:08 · 03 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
