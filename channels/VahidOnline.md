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
<img src="https://cdn1.telesco.pe/file/vETZkRvhaljqdV_xjRWVsJlrfMv91GKAdqmg7EiEc3Mc8HhNvhByc0qYT2NTnV0J0cFm_kX6jEdA1xmnIQZSsFtFEdmZX9X6x52UbMqZNELjmKqebTJQFYjyA_FZvchCGcm3BMX3I7kPAbLQTz_WT2pXdG9A3AtYk4uunVMvZv_L755lxLcmRSyoUMDL6mc3zNM-l15a2k7qvGAD2VXNfkxlfkfqqN3BYoq8qYS_lzJO4Ctl0RjP7UF--cbzfM-sBGWJr9ux-VX8lxsRNLuKDvRoS42d7B7E26_t35LKTYouF3tAg9P4DtcshE9Sqz1GEH9ahb6ZCEKcsMObGsDMVQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.33M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-07 05:44:51</div>
<hr>

<div class="tg-post" id="msg-75761">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BvnzZcQrm4EAd-MdgTbROjDijAg-mTsv8Kzqf7JuHhbSCy8S4YNExhgAfpmSjzOXPxCq2iOIBiHzGSV5p_mHIel_wBQbbXW8rzU53nH1OJx4PvDGhJvLydyP0wBGJYbFGqZkgIwmJyGG-W-9dRM1k8EvCsxk6U1A0RO5uP5NGWwOGhCfVYagfNSDAtNN99bVLfz-qhGfyEeFIyNhPw7rQswQAqLoqH_SA3ObKgScfbWL3WsbfyXsQa03KoBZtiAbpALkFwHVOnwDO47Mu5jbO7qrjg3u6lI5O1Oj-Qt5-CjzsZ8HHjQbydTeo5KcLMHn6y0lXX-mKTe5d-tg2Z3rnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
یک مقام آمریکایی به سی‌بی‌اس گفت ایالات متحده حملات جدیدی را علیه یک سایت نظامی ایران انجام داده ولی آتش‌بس همچنان برقرار است.
cbsnews
یک مقام آمریکایی در گفت‌وگو با رویترز از حملات جدید آمریکا به یک سایت نظامی در ایران خبر داد و گفت ارتش آمریکا همچنین چندین پهپاد ایرانی را رهگیری و سرنگون کرده است. هنوز به جزییات این سایت نظامی و تعداد پهپادها اشاره‌ای نشده است.
ساعتی پیش در پی شنیده شدن صدای ۳ انفجار در شرق بندرعباس، پدافند هوایی این شهر فعال شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/VahidOnline/75761" target="_blank">📅 03:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75760">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">#بندرعباس
پیام‌های دریافتی:
چهار تا صدای انفجار پشت سر هم اومد الان
ساعت ۱:۳۳ بندرعباس
درود آقا وحید همین الان سه تا صدای انفجار اومد تو بندرعباس ساعت ۱:۳۳ دقیقه
حاجی صدای انفجار دوباره شرق بندرعباس همین حالا  سه تا پشت سر هم ساعت1/43 دقیقه
سلام وحید
۰۱:۳۳ شب
همین الان بندرعباس صدای ۳ تا انفجار اومد
سمت بهشت بندر
احتمالا باز مثل سری قبل باند فرودگاهه
بندرعباس ساعت ۱:۳۰ هفتم خرداد صدای جنگنده بعدش سه تا صدا انفجار اومد
سه تا انفجار بندرعباس
ساعت 1 و 33 دقیقه بامداد پنجشنبه 7 خرداد صدای سه تا انفجار رو از بندر عباس کس دیگه ای هم گزارش کرده ؟
شبیه صدای موشک زمین به هوا بود
بندرعباس صدا اومد
سه بار
درود. ساعت ۱:۳۲ دقیقه صدای سه انفجار شدید در بندرعباس اومد و خونه شدید لرزید.
ساعت ۱:۴۷ باز هم صدای دو انفجار دیگه اومد
صدای سه انفجار بندرعباس همین الان
سلام وحید جان بندرعباس چند انفجار وحشتناک پنجره خونه لرزید 1.38
دباره زدن بندرعباس ساعت 1.49
۳تا صدای انفجار بعد صدای پدافند
سه انفجار پشت سر هم و یکی هم ده دقیقه بعدش بندرعباس رخ داده
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/VahidOnline/75760" target="_blank">📅 01:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75758">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RJuPJYsq1FXjm4ojuLk38981rfRJQCbktBZhZ449-spfa5ZO1LCwlER2ndgQENdh9uSkAiQW_BYY5eKnlb38JpOniM-89yFG6OuCPF4GSu9-tIsd-BOMLWVhon3ZHtuTasBnhDW0U6mI6itjwyUSdre65kslvBzunQvwQqwHoNYzGjYq2gWVi1HfThuC2ia-9Nc3iLhahZDJGH_7qML4TD_9OqlwszL0lK_SwxDZHhkyyolWq7tG-Cf2QHbBSlT03mmNiwzNdFcG5nmV8CEgWpcoCtJdTqqI34XaHKzER1-1klgbrMBGKwFXd79LpKaPhhsW289yBkOuJGLSc8OF-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b2c97c6720.mp4?token=uTvowm2SDjo45dlilNR3dh9nb716TNjCWa43bbG8xvNUi0ep5UnVp4fVW-vVzYHn9rYH_CLGQbhCzFM3aHZOxVo1xyzCa3fdcmFNy4-j8-n1uOrKivBEErN_ilfr5S22d4En3sZWUt6EAeW8DBJhS5nkuYt2M1QUzigIXWU2fUQB3gKfSs0z1ENEC_fczI0fbCJMWXkswTGIfmGF5XHOaGzsRk48SBioBQizHZLw-zdemM6joSHFif-jAHDq0KRhixzVPSTGApp4jcP7GdZNb8agj0taq7_xS-kYmWayJEYD9j5kcfyAUW7qIWKRT1bFQItsSQlTIUHC3brgfEhplA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b2c97c6720.mp4?token=uTvowm2SDjo45dlilNR3dh9nb716TNjCWa43bbG8xvNUi0ep5UnVp4fVW-vVzYHn9rYH_CLGQbhCzFM3aHZOxVo1xyzCa3fdcmFNy4-j8-n1uOrKivBEErN_ilfr5S22d4En3sZWUt6EAeW8DBJhS5nkuYt2M1QUzigIXWU2fUQB3gKfSs0z1ENEC_fczI0fbCJMWXkswTGIfmGF5XHOaGzsRk48SBioBQizHZLw-zdemM6joSHFif-jAHDq0KRhixzVPSTGApp4jcP7GdZNb8agj0taq7_xS-kYmWayJEYD9j5kcfyAUW7qIWKRT1bFQItsSQlTIUHC3brgfEhplA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ درباره لغو یا کاهش تحریم‌های جمهوری اسلامی گفت واشینگتن «درباره هیچ‌گونه کاهش تحریم‌ها یا دادن پول» صحبت نمی‌کند و تاکید کرد: «هیچ تحریمی، هیچ پولی، هیچ چیزی.»
او افزود آمریکا کنترل پولی را که جمهوری اسلامی ادعا می‌کند متعلق به خود است در اختیار دارد و این کنترل را حفظ خواهد کرد. ترامپ گفت زمانی که جمهوری اسلامی «رفتار درستی» داشته باشد و «کار درست را انجام دهد»، اجازه دسترسی به این پول داده خواهد شد، اما «در حال حاضر چنین کاری انجام نمی‌دهیم» و «این دو موضوع به هم وابسته نیستند.»
ترامپ همچنین درباره انتقال اورانیوم غنی‌شده گفت با انتقال ذخایر اورانیوم غنی‌شده ایران به روسیه یا چین موافق نیست.
@
VahidOOnLine
دونالد ترامپ در پاسخ به سوالی درباره کنترل تنگه هرمز توسط تهران و عمان گفت این تنگه برای همه باز خواهد بود و آب‌های بین‌المللی محسوب می‌شود. او تاکید کرد هیچ‌کس آن را کنترل نخواهد کرد و آمریکا بر آن نظارت خواهد داشت.
ترامپ افزود کنترل تنگه بخشی از مذاکرات است و ایران تمایل دارد آن را در اختیار بگیرد، اما چنین اتفاقی نخواهد افتاد. او درباره عمان نیز گفت این کشور مانند دیگران رفتار خواهد کرد و در غیر این صورت آمریکا مجبور خواهد شد آن‌ها را منفجر کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/75758" target="_blank">📅 21:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75757">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kh3vl7smseZbasRLJQwwhMiP_9Cpsx9ShUehqFSkGL9oqLzqS9h_kMQk3CwPuNR4-EgrqhLoKid1sz7SF9IACWJqGi_g7bqeiZ3yjDfDR38LYwzqQDmXG77s0Ya5MeMb0qAlq3xNqwKc1ILk_tjDT_cDLsb-XYoKYb3GEp2wc2Z-lyk1prYye684dU7WDJInpCfru7QvO0y8DqvDEU-blVDiTaDlbO7vzJS8OMseI5-lyT9DAHI9pqy4WHGkitshj6AElcaisaja6PsbHseVSx1BsO4TDJgB30RkCj2nmEDF3ljG19_eLfJ8MtjOPg3maEmDEwKBfvwEzhjNTmdELg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز چهارشنبه گفت که ایران در ازای کنار گذاشتن اورانیوم با غنای بالای خود، از لغو تحریم‌ها توسط واشینگتن برخوردار نخواهد شد و از پیشنهادات ایران برای توافق پایان جنگ ابراز نارضایتی کرد.
ترامپ پیش از برگزاری جلسه کابینه خود در یک تماس تلفنی کوتاه با شبکه پی‌بی‌اس نیوز، در پاسخ به این سوال که آیا توافق فعلی به این معناست که ایران در ازای لغو تحریم‌ها، اورانیوم با غنای بالای خود را واگذار خواهد کرد، گفت: «نه، نه، اصلاً. خبری از لغو تحریم‌ها نیست، نه.»
او اضافه کرد: «آن‌ها قرار است اورانیوم با غنای بالای خود را کنار بگذارند، نه در ازای لغو تحریم‌ها. نه، نه، اصلاً.»
ایران بیش از ۴۰۰ کیلو اورانیوم غنی شده تا حد ۶۰ درصد دارد که در تأسیسات زیرزمینی هدف قرار گرفته در جنگ ۱۲ روزه سال گذشته مدفون است.
رئیس‌جمهور ایالات متحده ساعتی بعد در ابتدای نشست کابینه خود در کاخ سفید گفت که ایران بسیار مایل است به توافق برسد، اما آمریکا هنوز از توافق پیشنهادی رضایت ندارد.
ترامپ در این نشست در حضور خبرنگاران گفت: «ایران خیلی مصمم است، آن‌ها خیلی می‌خواهند که به توافق برسند. تا اینجا هنوز موفق نشده‌اند... ما از آن راضی نیستیم، اما خواهیم شد.»
او سپس بار دیگر ایران را به ازسرگیری حملات نظامی تهدید کرد: «یا به آن نقطه می‌رسیم، یا اینکه مجبور می‌شویم کار را یکسره کنیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/75757" target="_blank">📅 20:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75756">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aKxayZbpLu9kqjvkqF2MgjnTMKYERVKnghH1KIKptnT7t36AdI2hLPTiQMTzsAbYnOLxhiCqwd4BXhYbES-_JZRjXlnyMkB7zS8ZVSR4gh22d20-j_Z_UIL8NiPe_lFt9R6U3vdjk0eGBWVJ7timvFsvZzO0Md5XPHeQPol_p845sppl0QL9idnCNTDEwyUXrmzJ-vz9y6n-u430JMqQVqTVCwfVl3Y12eC_mCQnxDzOX43MRnuvzBZqXZoBkELUTcRakFJyzOAUB7Dq5bOrRfFtHNY4va4P1o0Snmz4o5wddsYUymLh5bmwssKUPABtrPoeH4fRfkx1FGTzsuKY7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
تصاویر دلخراش از اجساد مردم کشته‌شده در بیمارستان تهرانپارس تهران
⚠️
دو روز پیش ویدیوی دوم رو با تردید منتشر کرده بودم و نوشته بودم نمی‌دونم درسته یا نه. حالا عکس‌هایی از بیمارستان تهرانپارس با شرح جان‌باختگان ۱۸ و ۱۹ دی دریافت کردم که نشون میدن اون ویدیو…</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/75756" target="_blank">📅 20:01 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75755">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/43dd15a53a.mp4?token=B9KuobKmckLHEPzFOVn3UBfUo1mX14-ZO-EbR4kuki15L_37YRHGYjl3_M_Ti3rUcMziwYp-wTFmasoDOl4L5cRgM9RSSXoqVR2Gf1oMrTWruFE291HbEjGpQv_uN7KWBuJAchaeDQM0cDvI5w1xAk6K9IAK80zpKa3T4FVUHYamSnKKoQKrWvpcsMRhWVBMKXsroLOS4piT7l6CNG4CwXHxbkaz4yNJ788DM_obr8ivS1cP3xNPqvZC8LmcZSoMjRKJC8dB6Yidg2RnV25BqPpjQREC6eA6WEe8kRnrLFpNJKbZpI005OZD60H1fKIvYdhqgRAGqvaiLWYXUFuavw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/43dd15a53a.mp4?token=B9KuobKmckLHEPzFOVn3UBfUo1mX14-ZO-EbR4kuki15L_37YRHGYjl3_M_Ti3rUcMziwYp-wTFmasoDOl4L5cRgM9RSSXoqVR2Gf1oMrTWruFE291HbEjGpQv_uN7KWBuJAchaeDQM0cDvI5w1xAk6K9IAK80zpKa3T4FVUHYamSnKKoQKrWvpcsMRhWVBMKXsroLOS4piT7l6CNG4CwXHxbkaz4yNJ788DM_obr8ivS1cP3xNPqvZC8LmcZSoMjRKJC8dB6Yidg2RnV25BqPpjQREC6eA6WEe8kRnrLFpNJKbZpI005OZD60H1fKIvYdhqgRAGqvaiLWYXUFuavw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد‌ ترامپ، رئیس‌جمهوری آمریکا، چهارشنبه ششم خرداد، در نشست کابینه در کاخ سفید درباره مذاکرات با جمهوری اسلامی گفت تهران «بسیار مشتاق» توافق است، اما مذاکرات هنوز به نتیجه نهایی نرسیده است.
ترامپ گفت: ما از وضعیت فعلی راضی نیستیم ولی خواهیم شد.
رئیس‌جمهوری آمریکا همچنین جمهوری اسلامی را تحت فشار شدید توصیف کرد و گفت: «نیروی دریایی‌شان نابود شده، نیروی هوایی از بین رفته و همه‌چیزشان از دست رفته است.»
ترامپ افزود جمهوری اسلامی «در حالی مذاکره می‌کند که چیزی برایش باقی نمانده» و هشدار داد اگر توافق حاصل نشود، آمریکا ممکن است «برگردد و کار را تمام کند.»
ترامپ گفت: «آنها تازه دوباره به اینترنت برگشته‌اند، چون به‌شدت تحت فشار قرار گرفته‌اند.»
او همچنین گفت اقتصاد ایران «در حال سقوط آزاد» است و تهران به‌دلیل فشارهای سنگین، گزینه دیگری جز حرکت به‌سوی توافق ندارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 216K · <a href="https://t.me/VahidOnline/75755" target="_blank">📅 19:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75753">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">خبرگزاری فارس به نقل از «منابع آگاه» گزارش داد که دونالد ترامپ، رئیس‌جمهوری آمریکا، ممکن است در ساعات آینده به‌صورت یک‌طرفه اعلام کند که توافق میان ایران و آمریکا نهایی شده است؛ اقدامی که به گفته این منابع می‌تواند با هدف اعمال فشار سیاسی و اثرگذاری بر افکار عمومی انجام شود، پیش از آنکه اختلافات باقی‌مانده به‌طور کامل برطرف شود.
بر اساس این گزارش، این سناریو در حالی مطرح شده که هنوز برخی موضوعات میان دو طرف حل‌نشده باقی مانده و روند مذاکرات به مرحله نهایی نرسیده است.
در همین زمینه، یک عضو تیم مذاکره‌کننده ایرانی در گفتگو با فارس تاکید کرده است که تا زمانی که همه موارد مورد نظر ایران حل و فصل نشود، هیچ توافقی قابل اعلام نخواهد بود.
به گفته این منبع، جمهوری اسلامی ایران تنها در صورتی که اختلافات به‌طور کامل برطرف شود، نتیجه مذاکرات را به‌صورت رسمی اعلام خواهد کرد و هیچ توافقی پیش از رسیدن به جمع‌بندی نهایی، مورد تایید تهران نخواهد بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 206K · <a href="https://t.me/VahidOnline/75753" target="_blank">📅 19:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75749">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tMFHNkYCnZ9iYqVnuD5sOVcqnde92AR9bQF0Spk_mqHr9KrkQ1WHF4m6WOW_9QSy2akqMiJxDG438AkutMZF21paP8yZLYnfNeHnJd9BDYYJxhcT4k98nFFQvSRLEvjDvfIfUWmk21-c57MbN9p8KLMqi3GYdtFbZEeDO0dRvf1C1w2zEoCXMhVM0d-rR61wS-qmSs241-xNZnnrc23xHiqTq-5worOzYBZU-6Mq1c6N0N5VY9TkhyzYhtjamNkgT7fWV0Lc9USVK6MDMWeq5JceK6J2QxUE5o9m9Yqth3SdVw90upGWJsIVt8ra0vjnOe5VomdPv9An27d4yJNSMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a77ea28679.mp4?token=oKQR2WSTBiTD4n-9oI7BsxPRhKSJthNSH8qy-PIC6WjIHIN6We8D5bYH461n_Oq7W5BwYdpZtZvZqSPA8qn1L1Sa5bHSCuYa6g6pYGKDjoRnNSA06VAcVpwIPskINelqN5NHF3badap8qj4b6_ESEJkFp7hY2Zvj7uQJnpVEDxw2rFdOPP1Om1ZsGh77SjHBXi5QhJUVQ0GIFLu2SfCnVjhDMiFg3fyN4PYL76g1B5zMxoRVQJiDyMiYNrTfDdHPuni6H4-_gxtszLgpRJpJC8QIt2SLidcqLE6Ff5Gln3mRdiCZ4AGSn2hpJjlfNk0YYfcr90S4PIC_06eoyVUDfA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a77ea28679.mp4?token=oKQR2WSTBiTD4n-9oI7BsxPRhKSJthNSH8qy-PIC6WjIHIN6We8D5bYH461n_Oq7W5BwYdpZtZvZqSPA8qn1L1Sa5bHSCuYa6g6pYGKDjoRnNSA06VAcVpwIPskINelqN5NHF3badap8qj4b6_ESEJkFp7hY2Zvj7uQJnpVEDxw2rFdOPP1Om1ZsGh77SjHBXi5QhJUVQ0GIFLu2SfCnVjhDMiFg3fyN4PYL76g1B5zMxoRVQJiDyMiYNrTfDdHPuni6H4-_gxtszLgpRJpJC8QIt2SLidcqLE6Ff5Gln3mRdiCZ4AGSn2hpJjlfNk0YYfcr90S4PIC_06eoyVUDfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#آتش‌سوزی
در یکی از برج‌های مجتمع مسکونی پامچال در چیتگر
#تهران
تصاویر دریافتی + منتشرشده، چهارشنبه ۶ خرداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 196K · <a href="https://t.me/VahidOnline/75749" target="_blank">📅 19:44 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75748">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlvahMzgDi02YRSU9gwfrq1gBF_hfk1RwSsK1gDJp3jr6hjs-gxGO7PcQXS375-lXh4VTLBtZXYj0gJpB4Q1jTz9CI0fcE6i_SL0SIj7B9XV1MjjRi5JTz2kA7h3PkXV521Y4F7LEdnlD5lZaBdtY6dTh4H0shNLkWria-jWAyuYMkKEryBJBaLAtb_XlWu_Ou1-hFSY7Kcme6QDe1i3raboI4sjk99-efRqIjvdI4EoPN-Ojqvu7quFrNqyul5mLWvla3sFbrZ7V4chnEA-8HYIFyz-xxh7P-wlrTtf2GaukWITZgjUyTQkWGml3Ass5xRWdSMUGNeVU7DCbC4VUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاخ سفید روز چهارشنبه اعلام کرد گزارشی که از سوی صداوسیمای جمهوری اسلامی منتشر شده و به پیش‌نویس یک چارچوب اولیه و غیررسمی برای تفاهم‌نامه میان ایران و ایالات متحده اشاره داشت، «صحیح نیست» و تفاهم‌نامه مورد اشاره «کاملاً ساختگی» است.
تلویزیون حکومتی ایران ساعتی قبل گزارش داده بود که پیش‌نویس یک توافق چارچوبی با ایالات متحده شامل تعهد به لغو محاصره دریایی ایران، بازگرداندن رفت‌وآمد در تنگه هرمز و خروج نیروهای آمریکایی از منطقه خلیج فارس است.
کاخ سفید در بیانیه‌ای اعلام کرد: «این گزارش رسانه‌های تحت کنترل ایران حقیقت ندارد و تفاهم‌نامه‌ای که آنها منتشر کرده‌اند کاملاً ساختگی است. هیچ‌کس نباید آنچه رسانه‌های دولتی ایران منتشر می‌کنند را باور کند. واقعیت‌ها اهمیت دارند.»
گزارش صداوسیما
مدعی شده بود که آمریکا متعهد به رفع محاصره دریایی ایران شده و در مقابل، ایران تعهد داده تعداد کشتی‌های عبوری تجاری را طی یک ماه به سطح پیش از تنش‌ها بازگرداند.
تلویزیون جمهوری اسلامی همچنین گفته بود بر اساس این پیش‌نویس، «مدیریت و مسیر عبور و مرور» کشتی‌ها با ایران و همکاری عمان انجام خواهد شد و آمریکا تعهد داده نیروهای نظامی این کشور از «محیط پیرامونی ایران خارج شوند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 223K · <a href="https://t.me/VahidOnline/75748" target="_blank">📅 18:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75747">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T66X8JzDCXM3E4GgPLlgygUjw-9C058iZYqT8vbY9-kuss1_oiKmxuzd7TeqptM50ur7iYnbOQi3jx6-dQXG82ePshsgfGdra3G5uOrAc3aQ7kMSiE43VnQMimU7T2O88qxPHThWxeKztHn-pseNPPEPh-_-z6MXxQ3ZX3VL4cBYTny9Gm46yN_5LsE5cNUFN1oQ_cbvDpZtkmfbk0PasiCCelf0IknxYfgd7753GZFmPTbW_p_tdfcYU52LDCz455y_kvedsRTt7T_w54JUDl6cIWdzVZs5mfq2nxg5gtAizYiHedaLXbc-Xp80RIVQqOIixyMw75h6RtaXx16jWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد‌ ترامپ، رئیس‌جمهوری آمریکا، چهارشنبه ششم خرداد در شبکه اجتماعی تروث سوشال با انتشار تصویری ساخته‌شده با هوش مصنوعی، از شبکه سی‌ان‌ان انتقاد کرد و نوشت این رسانه نیروی دریایی جمهوری اسلامی را قدرتمند نشان می‌دهد، در حالی که شناورهای ایران در اقیانوس غرق شده‌اند.
در این تصویر، جمله «سی‌ان‌ان: نیروی دریایی ایران قدرتمند است» در کنار تصویری از شناورهای غرق‌شده جمهوری اسلامی در کف اقیانوس دیده می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 219K · <a href="https://t.me/VahidOnline/75747" target="_blank">📅 18:44 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75746">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iFoUVLCJ08ecp6Z4OhgCFOdxmAXNdQnv_1gOOUnF4txwlvLjjDlrVCF3owhUbrcs92T5Ck5OOYms9SrPX1Cuyv5rDdzX_rtJ38h5MFNJCt4um2xP9dWeVUjT6XB02-2XwvRwON3wiVd4xrpbfHV-3GptN9BOFWMWgh-1_dlOSz8XzFkXNE2xsi26eJgFnBGXUEKfqjhxDQCrJOfMspXjEnuJd_M7I-XqM3cxtoWp9Hn5F3IV9eScsCX2WPTXEKZUpl0-6lqJODAyK-Mqlvw99DhiVSzY5XtodWOHq0hLU-XFafaeBjQxnWtpwVJ9uGyY6RCGiYMXYN74aM-4y1fFNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏گروهی از کاربران در شبکه اجتماعی ایکس (توییتر سابق) پست‌های انتقادی گزارش‌گونه از تحولات و رویدادهای سیاسی خارج از ایران منتشر می‌کنند، خطاب به شهروندانی که پس از حدود سه ماه به‌طور تدریجی با فیلترشکن موفق می‌‌شوند به اینترنت وصل شوند.
‏این پست‌ها که با عبارت‌هایی مانند «
وقتی شما نبودید
» یا «بچه‌های ایران که تازه وصل شده‌اید» آغاز می‌شود، همزمان با کاهش تدریجی اختلال در دسترسی به اینترنت، به محلی برای مستندسازی و بازاندیشی انتقادی نسبت به تحولات سیاسی‌ ۸۸ روز گذشته تبدیل شده است.
@
VahidHeadline
دوستانی که تازه وصل شدن یدونه «
سلام وحید جان
» سرچ کنید آرشیو کامل از اندر احوالات ایرانی جماعت در زمان قطعی نت رو براتون میاره
iamroyaz
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 226K · <a href="https://t.me/VahidOnline/75746" target="_blank">📅 18:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75745">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d05e2caab7.mp4?token=g9Dj47lnyHR3foygbYWTQlpVPjtkOBVr6fBEAWDKwdLy6V6cPSUClmbcGkCCbDb6BN1Ceac6A4XKJqadaoRw76be3HZQlYHrLT43jBFZlBqU2QaQSqcLpZUNonUtednq6OBPdVDUp_3Z_gs3_OtHqcib6DaApBs_wnGHD4p02vRMtsc3ZDFMWGetbj9upe0maOCmGu-JNVSnihxRm-tEsfw3v4pCqp2PthbE0tDHZ5DRfEOfbqam0DT_8a_3oJSjHTMBlbfEX_IHs7NphyccHKJaHR76GjajDRVJMblmK4tC0-2xyJR7FqvI0oz0Y8TTCpCU5S47WpxTExoo1xfdoTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d05e2caab7.mp4?token=g9Dj47lnyHR3foygbYWTQlpVPjtkOBVr6fBEAWDKwdLy6V6cPSUClmbcGkCCbDb6BN1Ceac6A4XKJqadaoRw76be3HZQlYHrLT43jBFZlBqU2QaQSqcLpZUNonUtednq6OBPdVDUp_3Z_gs3_OtHqcib6DaApBs_wnGHD4p02vRMtsc3ZDFMWGetbj9upe0maOCmGu-JNVSnihxRm-tEsfw3v4pCqp2PthbE0tDHZ5DRfEOfbqam0DT_8a_3oJSjHTMBlbfEX_IHs7NphyccHKJaHR76GjajDRVJMblmK4tC0-2xyJR7FqvI0oz0Y8TTCpCU5S47WpxTExoo1xfdoTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری صداوسیما اعلام کرد به یک سند غیررسمی اولیه از چارچوب ۱۴ بندی تفاهم احتمالی میان ایران و آمریکا دسترسی پیدا کرده، سندی که به گفته رسانه‌های ایرانی، هنوز نهایی نشده اما حاوی جزئیاتی درباره وضعیت تنگه هرمز و حضور نظامی آمریکا در منطقه است.
بر اساس این گزارش، در پیش‌نویس منتشرشده آمده است که آمریکا متعهد می‌شود نیروهای نظامی خود را از اطراف ایران خارج کرده و محاصره دریایی را متوقف کند. در مقابل، تهران نیز تعهد می‌دهد ظرف مدت یک ماه، عبور کشتی‌های تجاری از تنگه هرمز را به سطح پیش از جنگ بازگرداند.
طبق مفاد این سند، کشتی‌های نظامی مشمول توافق نخواهند بود و مدیریت مسیر حرکت کشتی‌های تجاری در تنگه هرمز با همکاری ایران و سلطنت عمان انجام می‌شود.
صداوسیما همچنین گزارش داد که هنوز چارچوب نهایی تفاهم تدوین نشده و ایران تاکید کرده بدون وجود «سازوکار راستی‌آزمایی» یا همان مکانیزم اطمینان، هیچ اقدام عملی انجام نخواهد داد.
در بخش دیگری از این گزارش آمده است که اگر دو طرف طی ۶۰ روز آینده به توافق نهایی برسند، این تفاهم می‌تواند در قالب یک قطعنامه الزام‌آور در شورای امنیت سازمان ملل تصویب شود.
@
VahidOOnLine
🔄
آپدیت:
کاخ سفید: گزارش رسانه‌های جمهوری اسلامی درباره تفاهم‌نامه تهران و واشینگتن کاملا ساختگی است
کاخ سفید گزارش رسانه‌های جمهوری اسلامی درباره بندهای تفاهم‌نامه احتمالی را «کاملا ساختگی» خواند و گفت نباید به روایت رسانه‌های جمهوری اسلامی اعتماد کرد
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/75745" target="_blank">📅 17:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75744">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qf145ARdzftX3bXxlj5UTuaLo2lg_n5OWeTWVccd_RojGWxPgAb4OArCrMfHLv61xIBidA4L6wLWrNy05WzlD1wXBOwQh6OqBFcjnBcaOZdQjSjGJvvc6-udFOFBaPteULUQkpKBXx3j5XPctW2U6TrpNC8AxgrjNCJ3EEHrYwqsIdvvJb9K2bLU8W6ZgeimQScXj6xgdsyzfAgdhV0SL-Kodm89HuwcZu5j_RSG7zcEH10svguymVjDHJe-i4Ks0WFW2DlIW5LS3a84VRjSeKnMjR7OQWoXvF7TA7mpixtjyyqOJ0ax_kZf3KsWO06x8N7cJLUjsY62ixjZaTUJDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در تروث‌سوشال گزارشی از جروزالم‌پست را بازنشر کرد که بر اساس اطلاعات اختصاصی «مدیا لاین» نوشته است موارد آزار و تعرض جنسی به زنان بازداشت‌شده، به‌ویژه زنان جوان، در زندان‌ها و بازداشتگاه‌های جمهوری اسلامی در دوران آتش‌بس افزایش یافته است.
در این گزارش، زنی جوان به نام کاملیا گفته پس از بازداشت خشونت‌آمیز در خانه‌اش، دو هفته همراه هشت زن دیگر، از جمله دختری ۱۶ ساله که با ساچمه از ناحیه صورت زخمی شده بود، در اتاقی ۲۰ متری نگهداری شد.
به گفته کاملیا، او پس از انتقال به سلول انفرادی و خودداری از اعتراف اجباری، در اتاق بازجویی هدف خشونت قرار گرفت، لباس‌هایش پاره شد، با باتوم مورد تجاوز قرار گرفت، به‌شدت کتک خورد و به تجاوز گروهی تهدید شد.
جروزالم‌پست همچنین با اشاره به قطع گسترده اینترنت، بازداشت‌ها، ناپدیدسازی قهری، آدم‌ربایی، تهدید روزنامه‌نگاران و مخالفان در خارج از کشور و افزایش ناگهانی اعدام مخالفان نوشت سرکوب در ایران تشدید شده است.
دونالد ترامپ پیش‌تر نیز با انتشار پستی در تروث سوشال خواستار آزادی هشت زندانی سیاسی زن در ایران شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 230K · <a href="https://t.me/VahidOnline/75744" target="_blank">📅 17:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75742">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/N2JTZb0Y0brTZCKRsM0WTQw0PVGXP5yftQoLYOf_VP3T580j-ksMmhBuNSDrc64S7X7qBaSE4lKgF2YbTC9dzl8umxWpW3Dg2C7loAk266SZ2b6Py6QpPAYthMNq2xsRzKXK-1S-Ol_F37vlfc7maaqwfRx2JLzCFPEt3dVdkYvqx35Fnr7-FE-N8bHP_7dSjWdQrORbvawfytJdGSewiIN9a4tBIeaj_H08U4MtCqWOGw90SSMB5OQLuBHtvM9P4cXSO7YTLvf9LNsGxO7BVr_5QLOdMZmpSDc5x5xquoIh8wwjQEowpvtMBcqHWo-FVk_U9wkDeNulq7BGwCsB7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/G43KEfEWxAA7FYEEaXZ8bk3s0S-Ziqgg0ZL8K2Cq6_Chx6cUKegac6o30PhQoNIaooh2S4w9esTz6TDdqyKR2cGUd1DSfQfgoi-4os0qUwDFcxZ6sk5xML2DmZaeNYR7bOvKXSOQrtr3ouHgRosFbKVVvLtrf8jr1xscsHf3lHUqIUOpMTc2w6jvs1Bwp4ACBtlJDX9SweWuoC2iiuwWf4ZfEwOlkr1NWAl0wJUo_aOR2F6j97dh4kFYjwG1QJB8qZBHMBxK7oF7z0gbUO4-Ng9ZOHvv_usnH8U_btHYgmN9ZsA8trRvIC82bzrw30dqbjf1g11148w8anoQmy4K5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزارت اطلاعات جمهوری اسلامی روز چهارشنبه ششم خرداد هشدار داد که بعد از جنگ اخیر، «برخی کمبودها و گرانی‌ها» در پی فشارهای اقتصادی آمریکا می‌تواند باعث بروز ناآرامی‌های تازه در ایران شود.
این وزارتخانه در بیانیه‌ای مدعی شد که «تشدید فشارهای اقتصادی و متعاقب آن، انجام تحریکات گوناگون اجتماعی توسط عوامل دشمن و رسانه‌های مزدور فارسی‌زبان بیگانه، با سوء استفاده از برخی کمبودها و گرانی‌ها» یکی از محورهای مورد توجه آمریکا و اسرائیل است.
هشدار درباره احتمال ناآرامی همزمان با افزایش شدید نرخ تورم و و گرانی کالاها و همچنین انتشار گزارش‌هایی درباره کاهش شدید درآمدهای دولت جمهوری اسلامی در پی هفته‌ها محاصره دریایی آمریکا و سقوط شدید صادرات نفت ایران مطرح شده است.
این در حالی است که اعتراضات دی‌ماه سال گذشته نیز بعد از افزایش مداوم نرخ ارز در بازار و مناطق تجاری ایران آغاز و بعد از چند روز با افزایش تعداد معترضان، با خشونت شدید نیروهای امنیتی و کشتار هزاران نفر مواجه شد.
وزارت اطلاعات همچنین درباره «عملیات تروریستی و تجاوزات مرزی بویژه در شمال غرب و جنوب شرق ایران» و انواع عملیات «ترور و خرابکاری» هشدار داده و مدعی شده که آمریکا و اسرائیل به دنبال وارد کردن «انواع سلاح، مهمات و ابزار ارتباطی غیرقانونی، بویژه استارلینک» به ایران هستند.
ابراز نگرانی از رواج اینترنت ماهواره‌ای استارلینک در حالی است که بعد از ۸۸ روز قطع سراسری اینترنت در ایران، از روز سه‌شنبه شهروندان توانسته‌اند به شکل تدریجی و محدود به برخی سرویس‌های اینترنت جهانی دسترسی پیدا کنند.
@
VahidHeadline
این بیانیه که با عنوان «سخنی با ولی‌نعمتان و هشداری به دشمنان» در رسانه‌های داخلی ایران منتشر شده، ادعا می‌کند که «دشمن شکست خورده در جنگ نظامی، بدنبال تولید دستآورد برای خویش، گرچه از طریق جنگ نرم، می‌باشد.»
این بیانیه در حالی صادر می‌شود که اسماعیل خطیب، وزیر اطلاعات جمهوری اسلامی در سومین هفته جنگ در حمله اسرائیل کشته شد و دولت هنوز جانشینی برای او معرفی نکرده است.
وزارت اطلاعات در این بیانیه علاوه بر اسرائیل و آمریکا، بریتانیا و اروپا را به همراهی با این دو قدرت متهم و کشورهای عرب حاشیه خلیج فارس را به‌عنوان «غلامان متمول» مسئول تامین مالی «جنگ ترکیبی تمام عیار» علیه «مردم قهرمان ایران» معرفی کرده است.
وزارت اطلاعات در این بیانیه معترضان و مخالفان جمهوری اسلامی در خارج از ایران را تهدید کرد و نوشت: «مزدوران ضد انقلاب و تروریست‌های مقیم خارج کشور و حامیان آن‌ها نیز از آتشی که می‌افروزند در امان نخواهند بود.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/75742" target="_blank">📅 17:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75741">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ubJAWsFkW0gHLJkx32tckJZRKBFNB5-rMmUntnT1hjlSSkRflNNWGUJS835QPdTE1lFlggzJgT4pI31xU1Ipo4cEqe8E0Xc4vJWTwTk-lA8krCZjZxNsYS1iWhwPEBbCAE827eGMiuFPphj_F6mIWiiPjhjgfzE77BzIM3WecJ4Nu_pkFznI_0n5sHcHmtrxnJ4mPTRDaRn_hPJSoagHDC61FSVcnutKl38tjdu47iQMG3E5Wb_gtEsfKD6uHIVBE3JLKtuZd4hfSD4v6c-cK1ROfWItAiLmD7zyLFEGttZrnNaKl2tv8WihpS2jPGq1hRsv--CZvLeNXFo_JXNSZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز به نقل از دو مقام آمریکایی در روز سه‌شنبه ۵ خرداد گزارش داد که حملات دوشنبه شب نظامی ایالات متحده به اهدافی در جنوب ایران پس از آن صورت گرفت که تحلیلگران اطلاعاتی، مجموعه‌ای از اقدامات نظامی بالقوه تهدیدآمیز جمهوری اسلامی را در ۲۴ ساعت منتهی به این حملات شناسایی کردند.
هواپیماهای جنگی آمریکا دو قایق تندرو سپاه پاسداران انقلاب اسلامی را که سعی در مین‌گذاری در تنگه هرمز داشتند، غرق کردند.
این مقامات که نخواستند نامشان فاش شود، همچنین گفتند که جمهوری اسلامی پهپادهای تهاجمی یک‌طرفه را به سمت حدود دوازده کشتی جنگی نیروی دریایی ایالات متحده که در خلیج عمان و دریای عرب یا اطراف آن هستند شلیک کرد. این کشتی‌ها در حال اعمال محاصره دریایی آمریکا علیه جمهوری اسلامی هستند.
طبق این گزارش تحلیلگران نظامی آمریکا همچنین فعالیت‌هایی را در برخی از سایت‌های موشکی زمین به هوای جمهوری اسلامی در نزدیکی تنگه هرمز شناسایی کردند؛ فعالیت‌هایی که امنیت هواپیماهای جنگی آمریکایی مستقر بر روی زمین و آن‌هایی که روی ناو هواپیمابر آمریکا در منطقه به عنوان بخشی از نیروی اعمال‌کننده محاصره دریایی حضور دارند، تهدید می‌کرد.
تیم هاوکینز، سخنگوی فرماندهی مرکزی ایالات متحده، روز دوشنبه در بیانیه‌ای گفت که ایالات متحده «برای محافظت از نیروهای خود در برابر تهدیدات نیروهای» جمهوری اسلامی حملاتی را به اهدافی در جنوب ایران انجام داد.
سایر مقامات پنتاگون گزارش‌های رسانه‌های داخلی در ایران را که در روز سه‌شنبه مدعی شدند یک پهپاد آمریکایی «ام-کیو۹ ریپر» توسط جمهوری اسلامی سرنگون شد، رد کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/75741" target="_blank">📅 04:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75740">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JRDxHab5601My7gJNFCi7Zo48rBVhWBH9ULSjItj0_xd7eay1jml103xI0bjBnyKXDCejlRBN4uCrbBFA3p7NGCS8PASPnKykac0HtQsWk2BSIEXmGXWDVFoobrKF71ahM_5SStk55HGMqD1L9RMm-4yK5E77rjhiB0zgIRDf7YNUlSvBp44eL3tpPLYNmt_-fUXfdpLCTMJkfemmGdKPWVQyJ6V6oINomQj8oeUiKwoLzc4HZb2Rs3lijgOyyiGPEEf5CEk7Wex4XoD1TafE32J_tkPENfGb721XLOMJGE6qxxiKaT4LpCFEKVnEDb9nRBmBrpzuMlEcuatdQtcyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
با توجه به احتمال نامساعد بودن شرایط جوی در روز آینده، جلسه کابینه را در کاخ سفید برگزار خواهیم کرد و سفر کابینه به کمپ دیوید را به تعویق می‌اندازیم.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 394K · <a href="https://t.me/VahidOnline/75740" target="_blank">📅 00:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75739">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rmY5gIMWwztMVWoHFiP1wEvceZ_c8HvMlkL_3VgmXA2kRsMA0lUtLJTz_15vMGsNittak_hpeuqYIJoWpKmtXvBJh57qPqJZONTGcDsrRzttBzvl2CJ2sbk-ePGeOBkkLSg8vzq26rE6FDoZOadTDij5JmBKGqTS9ShuBtZV9l-5c3ls0hxh33OrvXn_Ovlu-ZjfgB96YZXXRZjDcrBO3suXaADf56uu_HR1VzAZ_krwFM66gRjGoCED3Lb2PZ9YWwjlC7u_v13yqjrj1zwlvz4NM8TPVo5Yc6hw0f5NYtwyu7trRBYvfCXW9pbO4nYIZ69Il1xi4sspLfiVLR9YrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ متنی که
۸ روز پیش
منتشر کرده بود رو دوباره پست کرد.
ترجمه ماشین:
اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در کف دریا آرمیده، و نیروی هوایی‌اش دیگر در میان ما نیست؛ و اگر کل ارتشش از تهران بیرون بیاید، سلاح‌ها را زمین بگذارد و دست‌ها را بالا ببرد، در حالی که هر کدام فریاد می‌زنند «تسلیمم، تسلیمم» و با هیجان پرچم سفیدِ نمادین را تکان می‌دهند؛ و اگر تمام رهبران باقی‌مانده‌اش همه «اسناد تسلیم» لازم را امضا کنند و شکست خود را در برابر قدرت و نیروی عظیم ایالات متحده باشکوه آمریکا بپذیرند، نیویورک تایمز شکست‌خورده، چاینا استریت ژورنال، همان وال‌استریت ژورنال، سی‌ان‌ان فاسد و حالا بی‌اهمیت، و همه دیگر اعضای رسانه‌های جعلی، تیتر خواهند زد که ایران یک پیروزی استادانه و درخشان بر ایالات متحده آمریکا به دست آورد و اصلاً هم رقابت نزدیک نبود.
دموکرات‌ها و رسانه‌ها کاملاً راه خود را گم کرده‌اند. آن‌ها به‌کلی دیوانه شده‌اند!!!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/75739" target="_blank">📅 23:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75738">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8vBMIL205Pu-NRWBtk6z4ZfOaTmYW6ZcJUeBxW0VIthRGJu_qePPaqyQs6d3iarfu5QYgJyvbQxreXnlgRHkfx2tjJ0oGjNXxYvewYJoUyUKUYWwyyp0NBUsDtg_eOGZrcVpM3uHx1z-g2-xuSxlbUATE4ivgG1hQEvEcEQxroDTI0vgaPxpQzFT56mNMYRC6ONpTZFYzOmW4y96hU6nBuUS_WWdX3JZoQW808u-fNLSgAtu8Qwvt_LiEIYiC90edfuLf_Jz7_ECgof5ndG83Opr6rg70EKhWO98p7TANquFngZ5rEeqlv3t-vMEawpW4DC-ShEjBM-YslVxhQzMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، قرار است روز چهارشنبه نشستی کم‌سابقه با اعضای کابینه خود در اقامتگاه ریاست‌جمهوری کمپ دیوید برگزار کند؛ نشستی که به گفته یک مقام کاخ سفید، همزمان با نزدیک شدن مذاکرات مربوط به ایران به مرحله‌ای حساس برگزار می‌شود.
خبرگزاری فرانسه با انتشار این خبر نوشت که انتخاب کمپ دیوید، اقامتگاهی دورافتاده در کوهستان‌های مریلند که ترامپ برخلاف بسیاری از رؤسای‌جمهور پیشین کمتر به آن رفت‌وآمد داشته، نشان‌دهنده حساسیت گفت‌وگوهای پیش رو ارزیابی شده است.
روزنامه نیویورک‌پست گزارش داده که موضوع ایران محور اصلی این نشست خواهد بود و همه اعضای کابینه  [
از جمله
تولسی گابارد، مدیر مستعفی اطلاعات ملی] در آن حضور خواهند داشت. بر اساس این گزارش، مسائل اقتصادی نیز در دستور کار قرار دارد.
کمپ دیوید در گذشته صحنه چند تحول مهم دیپلماتیک به رهبری آمریکا بوده، از جمله توافق‌های سال ۱۹۷۸ میان اسرائیل و مصر در دوره جیمی کارتر و نشست ناکام اسرائیلی‌ـفلسطینی در سال ۲۰۰۰ در دوره بیل کلینتون.
این دومین سفر ترامپ به کمپ دیوید در دوره دوم ریاست‌جمهوری او خواهد بود؛ نخستین بار چند روز پیش از حملات آمریکا به برنامه هسته‌ای ایران در خرداد ۱۴۰۴ بود.
@
VahidHeadline
🔄
آپدیت:
محل جلسه فردا عوض شد به کاخ سفید
چند پست پایین‌تر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 398K · <a href="https://t.me/VahidOnline/75738" target="_blank">📅 18:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75737">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M6_2z83uc-Ube27l9Pi5Hhx0YsLxdZqPZlW5memD3N8ElfMJYJgnm-1S_GtDYvMrE3Rbn4u1XnLPUTxzEzsGRxN599p4sfqMASlqdx281w5NGUr3k0dG47LStrKEE0wfk2hK6FuQm_7xiq0oKmV2sb6hxXQbD9e7GlIGrlZ1ePXywH3v8cx4j0FcVWZPlgrO0aoVsnzAB_psKJtJ_INewsBn9Hg8nPP-39k-_bXlsK_fsTyskHXEN2RZ9nemWCpg2bQqqUavxNJjf-yK6CYeODIgaQd4eOqaHcyM9qSea5QZq-q4KvlhxaDdLN5ajrvP2s3jAwQ5jTzu0W5SsZltGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به گزارش فارس، خبرگزاری وابسته به سپاه، محمدباقر قالیباف، رئیس هیات مذاکره‌کننده جمهوری اسلامی ایران که روز دوشنبه در راس هیاتی با همراهی عباس عراقچی، وزیر امور خارجه و عبدالناصر همتی، رئیس بانک مرکزی، برای رایزنی با مقامات قطری به دوحه سفر کرده بود، عصر سه‌شنبه، پنجم خردادماه، به ایران بازگشت. بر اساس این گزارش، محور اصلی گفتگوهای میان مقامات عالی تهران و دوحه در این سفر، رایزنی درباره بازگشت پول‌های مسدودشده ایران بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/75737" target="_blank">📅 18:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75736">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Li-Srprkd4o9mejGViGJ_VTvQEYDo_GnE7vEUIzM3ImAdZnkN_-MXkpnx3VOUOsU9dNhHkGdr6LppLsNKIf_IN7YyRmd_uMjMoCuS9BknbkbyI78ol_hYvwYxRLjfmdpz0fAAzpLm3ArbSk_ZOVfr2OKlA5Yc-5IAnAIDF4al7XXn4tWkq6vjl0hYl5Gdgbc3fGhYEy-SNWgK_UxQEBCsx95kO8fwrLKwBNYt1bRZNOomzupp5KZs494iKrNzjMNC-21rAgDGfbIKfohzHRg66sypWgofHuzY8wWdGfpaSeneP2WpP5SCHniMSVgIO90Chs97-jyibYX2D4ybTj6AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، روز سه‌شنبه، به نقل از منابع خود مدعی شد که طبق متن ۱۴ ماده‌ای یادداشت تفاهم بین ایران و آمریکا، منابع بلوکه‌شده ایران، به میزان ۲۴ میلیارد دلار باید در طول مذاکرات آزاد شود.
آنطور که این رسانه نزدیک به سپاه پاسداران از قول « یک منبع آگاه نزدیک به تیم مذاکره‌کننده» گزارش داده، ایران تأکید دارد که نصف این مبلغ باید با شروع مذاکرات، در دسترس قرار گیرد، و بقیه در طول ۶۰ روز منتقل شود.
این گزارش می‌گوید که سفر اخیر عباس عراقچی و محمدباقر قالیباف به قطر هم برای تفاهم دربارهٔ اجرایی‌سازی این مطالبه، و نحوه دسترسی به ۱۲ میلیارد دلار در گام اول و رفع موانع بوده است.
همزمان، احمد بخشایش اردستانی، عضو کمیسیون امنیت ملی مجلس، مدعی شد که چند روز پیش، قرار بود ۱۲ میلیارد دلار از منابع مسدودشده ایران، از طریق روسیه وارد شود، ولی آمریکایی‌ها مانع این انتقال شدند.
هنوز هیچ مقام رسمی در دولت آمریکا، این ادعاها را تأیید نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/75736" target="_blank">📅 18:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75732">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Y5oxD33asBGZaPaSvnABpnPWldxACEJ-pP831LGOgH9auPpsZcMBsc21XH2ICapEZ6-Rjc0BKlknnxyQC6F4nRtI8i8xU3TYvEMoPQ3IhcbMfyuB22VNZvFmBTdL-zq9e1N_MpZzqaLNs93vwA5hlYnmSfGjeht_W1S1iqerUoTjfBx7rd0puTdZng2Af1UVMh5XoHd-A-bvXuqB0i5ytq5cNdXwRUL8jLtvJ1A-7Mwef43mKuMbq-dElGPVFerFBLeBk35wHQc3IctzVejFXujaE_8Zd29a9nWsBVkTuGEqVDZsK76PW00qYGEDq3nkYIYz9GoyTEwR8oqHhTvPxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IC8LK21a5uQjErk3VE2Q4j1HK03at77pl6sRszg1NWHV7pNFeNiWV6aVkmV15P9TojjdgaFPqTqt3Eh0fsnEJIlmtKudtaYUEBs41olqqFLyBCeA06Q8RAvHvKfYRSJ66NyzqeZTuL5C_2UwofAwPqv8gumoQ-nSIrxjXK-9XX9gO91j5AzLUz5Q3bACmPWcSa311uF1GjnS4dn3MHS09yK83fTtOm3ZfmUwrluVDIzruTTAE4DvW98wQ5mzs92zwMUTPZaeSwXDK3QxndkCwNDHzhxPein6ckrpEojRhx2SrBtgSIXHS13dSZ6MP7HLHl81FlGSQGWtc8uzkamp-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lPU3Hj6lwwaefU6RSakTvsmKfC5VnSzS40TLlasyJ-1BrdVRWZupVIuE9trPKW5YbgM0DLXsOX1RKJJ-csJ5xJOL0O-M242JjhW2MsS08TO89-Wy5o5ltDLErZPqGw4_glrajOM8mpjrE9buJfNmp-c7x3P-ubimvL15cYSQvefCgFMiIrPDwxh3epYiv9BMGuJSfj_CThCuabQvYEA_JTXV5_P_ddtre5Nl1Jmi4IoolU7wCpJUzkaF9sfkBiGYcm6C0P9lObUb8V3iXL1ZV8fDdhuOD7F5it6ymOpOVhQnwtNfXaL2hghk83B8U_44IDML6gbGCwcWNLRz_0-_lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ApyZ4uspqlzZBm_G3xPiApjGtYlbTSn3uIzxEVRRYyeOowkj9hbrkkV4Y1LJYYUIMoohA12GuFjX4h_43AVSLZa3E8F77cA58HZzyRxgO6ZlatSIZUF95XPsuIBt1ZSQ9qzCV-0IpNfARj28AqWyC-CRVn3fHC_quE9LRiBxTtwfxe7VCymYT3i9dGwA9ajy6St37JJ64_5pd0hQE5gTSn_7-Ig9Vppd5mIWFTugsIGyY0LftBmEstxpObM8-rkG5qon-QoIRk-1C1Nr5nnIEkKX07aTibOtz_UCwBA7iXZj4s_Ng8-TfmbV7nz5Dg5bmy9g-PXK6fwMmjm3VUuZ-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نت‌بلاکس، نهاد پایش وضعیت اینترنت در جهان، اعلام کرد داده‌های زنده این مجموعه نشان می‌دهد اتصال اینترنت در ایران در هشتاد و هشتمین روز قطعی گسترده، به صورت نسبی در حال بازگشت است؛ هرچند هنوز مشخص نیست این وضعیت پایدار خواهد ماند یا نه.
@
VahidHeadline
ساعاتی پیش از این واقعه اخبار دیگری منتشر شده بود:
در حالی که مقام‌های دولت مسعود پزشکیان از آغاز روند اتصال کامل به اینترنت تا ۲۴ ساعت آینده خبر می‌دادند، دیوان عدالت اداری اعلام کرد دستور توقف اجرای مصوبه تشکیل «ستاد ویژه ساماندهی و راهبری فضای مجازی کشور» را صادر کرده است.
این دیوان ظهر سه‌شنبه پنجم خرداد اعلام کرد «به‌دنبال طرح شکایاتی، دستور به توقف مصوبهٔ ایجاد «ستاد ویژهٔ ساماندهی و راهبری فضای مجازی کشور» داده است» و افزود: «تا زمان رسیدگی نهایی به شکایات مطروحه، مصوبات و تصمیمات این ستاد قابل ترتیب اثر نخواهد بود.»
مرکز رسانه قوه قضاییه نیز اعلام کرد دستورات و مصوبات ستاد ویژه «به دلیل بررسی غیرقانونی بودن ساختار ستاد، تا زمان رسیدگی قانونی قابل اجرا نیست».
@
VahidHeadline
بعدش:
همزمان با اعلام دیوان عدالت اداری مبنی بر صدور دستور توقف بازگشت اینترنت، ایسنا به نقل از «یک منبع مطلع»، روز سه‌شنبه، پنجم خردادماه، گزارش داد که با صدور دستور اتصال اینترنت از وزیر ارتباطات و فناوری اطلاعات فرآیند اتصال در حال انجام است و طی ۲۴ ساعت این امکان برای همه فراهم خواهد شد.
این درحالی اتفاق افتاد که تنها یک روز پس از مصوبه «ستاد ویژه ساماندهی فضای مجازی» برای «بازگشت اینترنت به وضعیت پیش از دی‌ماه ۱۴۰۴»، دیوان عدالت اداری با صدور دستور موقت، «اجرای مصوبه ایجاد ستاد ویژه ساماندهی فضای مجاری» را متوقف و مصوبات این ستاد را تا زمان رسیدگی نهایی، غیرقابل اجرا اعلام کرد.
همزمان، انتخاب نوشت که کامیار ثقفی، رضا تقی پور، رسول جلیلی و محمد حسن انتظاری تحت راهبری یک مقام ابقا شده دولت ابراهیم رئیسی، «شاکی قضایی» اتصال اینترنت بین‌الملل هستند.
ایران از زمان آغاز جنگ در نهم اسفند، به مدت ۸۸ روز، در خاموشی دیجیتال به سر می‌برد.
@
VahidOOnLine
محمدرضا عارف، معاون اول پزشکیان، در شبکه ایکس نوشت پیرو دستور پزشکیان «گام نخست دسترسی آزاد و ضابطه‌مند به فضای مجازی برداشته شد.»
او افزود: «با بازگشایی اینترنت، خدمات هوشمند هموار و مطالبات مردمی که این‌چنین پای کار نظام و ایران ایستادند محقق و موانع توسعه دانش‌بنیان و مرجعیت علمی برداشته می‌شود.»
عارف در متن خود درباره «گام نخست» و وصل شدن اینترنت برای شهروندان توضیحی ارائه نداد.
این در حالی است که پیش‌تر فارس، رسانه وابسته به سپاه نوشت دیوان عدالت اداری اعلام کرد که در پی طرح شکایاتی درباره ابطال «سند ایجاد ستاد ویژه ساماندهی و راهبری فضای مجازی کشور»، هیات تخصصی صنایع و بازرگانی این دیوان، با احراز ضرورت و فوریت موضوع، دستور توقف اجرای این مصوبه را تا زمان رسیدگی به شکایت صادر کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/75732" target="_blank">📅 17:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75731">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S1Pq-rGXTXOZ8CJ1A7oSxg0yHgs3gkRhRnC0dswv0OtTz57dCYqtY8N4jW21Wu6mbawONMInU4Std5Lgit7pRHX8DBXVJ7q5ZskOqlP5U1vuFvwI4_3WvddE0m5E896D7LabNRA7huBdtTFAG2qe-puuQr4e8zuUBYgKRYjZwO1nFMe5_eHiDY7pK6cehtxyi51XHVrDxJ9JManx75xtwP2imZ_vDWPa27QQka3-POz4uYHEy7VXPjvISdXy9u0DUtFp_6bYwJRj9oGCfXu4c4c7yI5uO-gMTcMuEM09XysyfucZD_NwttVRmBN1Z4i3a7CKF4nM-96Ww-bgZ8P9lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Gerduo
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/75731" target="_blank">📅 17:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75729">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BLgCxtsYAFvzF_agdEyfbl3GRr-TwZaWtwpsywo-qhbKYOdM5-g0TanaWTqjTZ2enkFMoBzAE3CpjdJJ18IclMrLwUkant-slPX21XAA1oo8wnl8WGubfDx3oI4TD7SaYw5CQsKIGAIpwABss1Qw0JtBy7Ug1e26DuxtIJJI0QlKHXUnnYKslmYkzDLxjheUbxHGaDkU4D1NmB0VBmJugwk8xjVa4b5TemgmaRv9B-Maeg6Xd_u5_RelV2__RcAnWNGJpspxuzn89Ay57IYwoHPxTmOMoaOESzq-igfOVYrMfXQhnAP0wQEoq5FzFW-zwCh2FkZICVDuB1Lg6WKdNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MV3iHXsAL1cziNVAgAY5Xc6-EM4BydeSId6JUDEeEBU8g4BYX5WBPv5vXvygd9MCg49iuvVfPA00nhTp-PsX18ESBm_X-jQZ_0lTFXEEiCTchyrGYlwiLH9V4veFnk0eU1rYMEpOXjsVQt-nSZVagE3BlrY3L_zpKTGj_gc8aXPCGvTn3xk9Xy68OCd0-plc0kug99ESaUZbAoCaR5m25tKwmVwyW3-y0W9ihwTCzO4UP-n1hlHTDGFxjlNTY05LQV81wa4okHd5tViSxRav7YCCH2AvPethWE1fMvGv0nx0JoLq08_sNDRPuJsW7nkAtJrUGkS5EXn-b7yfck0viQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسانه‌های ایران روز سه‌شنبه پنجم خرداد پیامی منسوب به مجتبی خامنه‌ای، رهبر جمهوری اسلامی، را به‌مناسبت برگزاری مراسم حج منتشر کردند که در آن می‌گوید آمریکا از این پس «نقطه امنی برای استقرار پایگاه نظامی در منطقه نخواهد داشت».
او در این پیام توضیحی دربارهٔ پایگاه‌های آمریکایی مستقر در کشورهای خلیج فارس نکرد اما هشدار داد که «سرزمین‌های منطقه دیگر سپر پایگاه‌های آمریکایی نخواهد بود».
مجتبی خامنه‌ای همچنین با یادآوری ادعای ۱۰ سال پیش پدرش علی خامنه‌ای درباره اسرائیل، مدعی شد این کشور نیز «به مراحل پایانی عمر» خود نزدیک شده و «۲۵ سال بعد از آن تاریخ را نخواهد دید».
از زمان اعلام نام مجتبی خامنه‌ای، به عنوان سومین رهبر جمهوری اسلامی، تصویر یا صدایی از او منتشر نشده و رسانه‌های ایران فقط پیام‌های کتبی را از او منتشر می‌کنند.
@
VahidHeadline
در پیام منتسب به مجتبی خامنه‌ای با اشاره به گفته‌های ۱۰ سال پیش علی خامنه‌ای، رهبر کشته شده جمهوری اسلامی، اسرائیل «رژیم متزلزل صهیونی و غده سرطانی» توصیف شده و آمده است: «اسرائیل به مراحل پایانی عمر منحوس خود نزدیک شده و به فضل الهی و مطابق با سخن قاطع و آینده‌نگرِ ده سال قبل رهبر عظیم‌الشأن شهید قدس‌الله‌نفسه‌الزکیه، ۲۵ سال بعد از آن تاریخ را نخواهد دید، ان‌شاءالله.»
این سخنان در حالی عنوان می‌شود که اسرائیل و آمریکا در یک سال گذشته در جریان دو جنگ، مقام‌های عالی‌رتبه  سیاسی و نظامی حکومت ازجمله علی خامنه‌ای، رهبر پیشین جمهوری اسلامی، را کشتند، بخش بزرگی از برنامه هسته‌ای جمهوری اسلامی را نابود و تاسیسات و زیرساخت‌های نظامی و اقتصادی ایران را به‌شدت تضعیف کرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/75729" target="_blank">📅 17:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75728">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxklfF1p0qlLzc23Dn6mSoYYog5t5UBgCHJJDOMFDTpbc4xOJGye8MVlScSfU4DeaetQNbLLzrcssUmQnEsiQ9FSbKtm4VW58E1-u5qm7B_Ti0pt7UNKQjxzojSvfW_fT-KP5vB3MzzXZ2-Vrk3dKRgqyp9BHxjOJcP7DB3sBkmCR8Vl8-8LpcjXBryCJq0fm8XCSlbnqnov2QnOAAaS0Pm7NepCajmy8sXjaqh4NSh3FEA32ThUKqtXO9aUC6qB04FGp-BIUuXqvR98gd-MPDNRW2afchTxiSxvbq-CHpnkemuBcbSegGjW0Gz7cclvHMS49QT3JXr2DOTKUjSJbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه قطر می‌گوید گزارش‌هایی که ادعا می‌کنند دولت این کشور برای تضمین نهایی‌شدن توافق با ایران، ۱۲ میلیارد دلار به جمهوری اسلامی «پیشنهاد» داده، «کاملاً بی‌اساس» است.
ماجد الانصاری سه‌شنبه پنجم خرداد در شبکه ایکس نوشته که این گزارش‌ها «توسط طرف‌هایی منتشر می‌شوند که به دنبال برهم زدن توافق و تضعیف تلاش‌های دیپلماتیک با هدف کاهش تنش‌ها و تقویت ثبات در منطقه‌اند.»
او افزوده که تلاش‌های دیپلماتیک قطر که با «هماهنگی» شرکای منطقه‌ای انجام می‌شود، «شناخته‌شده و شفاف است».
ماجد الانصاری انتشار این دست روایت‌ها را «تلاش‌های مذبوحانه برای خدشه‌دار کردن اعتبار» دولت قطر نامیده که به گفته او به‌عنوان «یک بازیگر بین‌المللی قابل اعتماد در مسیر دستیابی به صلح» است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/75728" target="_blank">📅 17:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75723">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ezg-JJvuNSxi1bf6M_ObRltUSAlNMANV0bHcDi9SaknUvTJYTrtDmj2740IIUixHPGmm_UT6Gl9_F0TMRIyVPwJybyKIjbNeEeU0vg9kZOz9YrlhwoRbkJRBNMFdYzeo7WWOFGgQuKQSjfOly2X5WzhUYbV5gxPmijCDENvyclX7pqHZg3jQ3j2Gsa7GEv6bmnG3GHfcEGk7Djknr1-Z6TP-_XIcXIr-Ae5kGg0R7jpIE7Zg964aqUMJgowm4pAx3_jnJ0v8UXSRKAbXhaU1Eh5SQUeNk_1-0t3krnDtEMCVKYyZ3NcwDVTqO13No5dy5HVwFYlzjSeYrzIUHxpC8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QM6CVns1lJLgb8gh5o0G0R2zSgUoK_YyKr8sQ_nTPFmXGKr72Rdull1Zp4qm9mOJmS_D4tCSFgq6NIU2_HRFADlMNkhhZPYdCn-BG-UC3GYt7aLDkR9WYStyDHuNO2x1t8hWwGnPMdcvVvIJehYmqw5LdIP_dOX746o4byRKjjx_B5DmtpCRK7Ige_e94HxwXhKoY7fq-B0LCUmkvq9_Jbb-3GLZ7CsjP3z_em3c54E35DXdCbz8lLiMPGrgSaFUnJSGxJzre18BY8MOUwGSfWUjtSchf4qFjd5GAwTFZkv0aBHLXDT-exDZOoSlwoqN6by-7Dn_EJVPMq1dAwOdng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NmOQgSjqtfs9qCB4D2PUqhRkYF2eV18LlLff-nibI23fQsOGFpIByGRjD1Eo6XuFgm4iaR-DqcCLFbhvBYQ58sODlpyNgEsDWLHa9HX4KVhlH1Xfp8B1hxRskQpGu8jVOKWblLlC3681m49Q5oa8JJgEN8yM92G6N1wPMxzbXlufKeYsseSP_icUoGYcHVcuELXWLcAiJhUUZV5cA3FuV51fQN9maifgRF_y2O5wq0EvsLHbNzoJ6h_sBCcC_5QuSVVElO6UWzZqzkd_9Da2hJN26Qj46YymzjKCPMwFGZ5vqJa3Kw4HsWRKs3SCsTBYq-NVTE_unqWdJOzW47I0Gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری میزان، وابسته به قوه قضائیه، اعلام کرد غلامرضا خانی‌شکرآب به اتهام «همکاری اطلاعاتی و جاسوسی به نفع اسرائیل» اعدام شده است.
میزان مدعی شده او «سرشبکه عملیاتی موساد» بوده و پس از تأیید حکم در دیوان عالی کشور اعدام شده است.
در روایت قوه‌قضائیه، اتهام‌های سنگینی به او نسبت داده شده است؛ از جمله جذب افراد برای عملیات خرابکارانه، دریافت پول نقد و ارز دیجیتال، تعرض و اسیدپاشی به خودروهای افراد مورد نظر موساد، آتش‌زدن اموال عمومی، تهیه بمب و ارسال آن به تهران، تصویربرداری از نقاط هدف و حتی مأموریت برای فراهم‌کردن مقدمات ترور یک خاخام یهودی در یکی از کشورهای منطقه.
ابهام اصلی پرونده، نحوه انتقال خانی‌شکرآب به ایران است. میزان نوشته او در خارج از کشور شناسایی و با «فریب اطلاعاتی» به داخل کشور هدایت و بازداشت شد.
@
VahidHeadline
میزان نوشته است: بر اساس اعترافات متهم، یکی از مهم‌ترین مأموریت‌هایی که سرویس موساد برای وی طراحی کرده بود، اعزام او به یکی از کشورهای منطقه با هدف شناسایی و فراهم‌سازی مقدمات ترور یک خاخام یهودی بوده است.
@
VahidHeadline
گزارش دستگاه قضایی اشاره‌ای به تاریخ بازداشت و محاکمهٔ متهم نکرده و در عین حال وی را «از اراذل و اوباش یکی از استان‌های کشور و دارای سوابق نزاع و شرارت» خوانده و ادعا کرده است که او «به دنبال جذب افراد و به‌کارگیری آن‌ها در داخل کشور برای اجرای اقدامات ضد امنیتی بوده است».
از روند محاکمه این متهم گزارشی منتشر نشده و گزارش قوه قضاییه نیز مدارک و مستنداتی از اتهامات ارائه نداده است.
دستگاه قضایی جمهوری اسلامی در ماه‌های اخیر به شکل تقریباً روزانه اقدام به اجرای احکام اعدام معترضان و یا افرادی می‌کند که آن‌ها را به همکاری با آمریکا و اسرائیل متهم می‌کند. برخی نهادهای حقوق‌بشری می‌گویند جمهوری اسلامی از اعدام برای ایجاد فضای ترس و به‌عنوان عامل سرکوب استفاده می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/75723" target="_blank">📅 17:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75721">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UCijj8lHiUliyqwERseppH7A6uSLfEqZSEoYUN5XttCgXGx99P7Bj-14UW3OXs5CWMKHbeH0in4SMlq__FOMOEONSb3mkkj630JVtxwvpN2BvlA5nrQMu2D9Ve4YMy120wiu0V2gaVnDFTyifxvgDAIUgU1tqOvocEQq7jQ3WTJ6ck6NBi_i5oHLiyRwqATyf70BFt-8KVYNwjTzAyo4UzhHlYMktRVD90Z5fYd5yN3o2zOAmXUVZ4_ik1Nyzu1L31GXl2uqJEdGxHFu36A5swtK-Zfc22P29oc5R7splKEygp-VTvvwoWQ7XjTj6miI3W3ahe7qSvfL7rFw3uL5IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lJScIeHcJ0gpewJVSK7DTrDVuK_mNt4i_BgsVK3ghvav6PvPTe6WuVvKXpNgwulUNH_nOdjr63m6J0sGp5H2HExYSglYVuMGNixmRRhHX7qKrLEn9cBcNcj9kZanrtRRi-SOq4nZ18rcySxktdhT27jMq66JdcolAjZFYt17h-W5f5TgCovuhyRsov5opUfMyQgJKzyDnUt8S6t6y1nlw9xnE-E_AZhrPuXpbU0aZTRnRXGRdUk2lYSKvzdk3RGhrtU1UcsA_Mk39Mjxgj4GYy2wWYG-GSJxS__j3P23dKHnr6elaT_q5h4A8ceu0G1jJZcKX7vqYopqcyTHbL-MWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با وجود حملات اخیر آمریکا به سامانه‌های موشکی و قایق‌های ایران در خلیج فارس که وضعیت آتش‌بس شکننده را متزلزل‌تر کرده است،‌ مارکو روبیو، وزیر خارجه آمریکا روز سه‌شنبه گفت که توافق با ایران «همچنان امکان‌پذیر است.»
او در هند به خبرنگاران گفت: «امروز مذاکراتی در قطر در جریان بود،‌ و باید دید آیا می‌توانیم شاهد پیشرفتی باشیم یا خیر. فکر می‌کنم بخش زیادی از زمان صرف دقت در کلمات و واژه‌های به کار گرفته در متن اسناد می‌شود، بنابراین چند روز طول خواهد کشید.»
آقای روبیو افزود: «رئیس‌جمهور تمایل خود را برای انجام این کار ابراز کرده است. او یا به یک توافق خوب دست خواهد یافت یا هیچ توافقی نخواهد کرد.»
آقای روبیو به خبرنگاران گفت که تنگه هرمز باید باز باشد.
او گفت که آنها به هر حال این مسیر را باز خواهند کرد و افزود: «آنچه در آنجا اتفاق میافتد،‌ غیرقانونی است و باعث بی‌ثباتی برای جهان و غیرقابل قبول است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/75721" target="_blank">📅 07:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75720">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CfWsRnRMMKUmYfF-juaqLORrU6eJK2l1dV2iwsmqxEKCDwKlglyy86G84YfW4SrSygOrpyEcyjM04_X_nYdn-G2vx0JHZr032flCbwtxxAUbvHasB7gJpz5whZFxH5m9SGFueu7RciEe7ESqoTtSRYMz6Of92aWWJgdSanKQ6w6WmqIjK7kVIeAtp5qOCCiy-p8eLrlTGEKImpfvcVqnGGMtvDaYpVL9nFEzoogQEI0VanVn98S7QqfiU3emNkwuUA6EE0VZMfgR1X6351yhL-nVIyuu9ScSggLnN4McHqCAPXCvs8KNnzyKX3BSswAtihlVihLS0yhPG3MnxS1onQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا اواخر دوشنبه به وقت واشنگتن گفت مارکو روبیو وزیر امور خارجه، به در خواست همتای روس خود سرگئی لاوروف، با او صحبت کرد. در این تماس تلفنی، دو وزیر درباره جنگ روسیه و اوکراین، روابط دوجانبه و اوضاع ایران صحبت کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/75720" target="_blank">📅 06:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75719">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mecK_v36HhfpDLybJPievVA6blkq-lXFf3DzgqA3OrAHBqgWs7YKJMigU7DLIe0CKOcrMmmywdMOGKLDvfXrA67Uae8_sGtn7KHGl3E8ZvVUQ0vCFyYRn0MuPTIN9W0Wlacslt1vf2-KePg92aNZCQ3G12oNUCr8AwG0ybXbOOsdmHHDAFfslAnF_ZrBn2TS8I27524OUNkZTWojF5E8Z49ybtNfxiRJhTvxucYPjYPcTFBFKT90Q2OVvFpmW1MQDL1b9-ZHfst0HuQ4In4mvi3CcWTTyRIgNoKMvSQEXYCpDzSJlOOrNTpd32wrZopPE9R4pd-VtpL4zAl582kiIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/75719" target="_blank">📅 05:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75718">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VXP71XlAzjnpKKGLfgfgLTKwj0Pzw4L9TDyrX_xXTUWXxfahVAZkmijVfh6MysZuoAgY52HUAe-je9uVyenck6764OX-NyxxJAK1Db3i7rkFXaUVJ7v3uGSevk9BtxY3BL-YV_W6DuTj92yYOkZTsSzN50OmPgbuSGSdGlMJGh2Ufes98gZWnRZswX5SsYdhYz6uIyVls4amD3M51BATz0S83GEsW2JxEZKCkS5fQfXv13slxqaAZ3-OUUlRYs1NvkMvY60RIHXzA2wW8c0xVAmDeQZP2ihHZcIUWmBRVEeRphNQ3elTLnfXFgWX8oirwMlJoNaYsHXHHT_51bjrNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رماندهی مرکزی نیروهای آمریکا - سنتکام - در بیانیه‌ای اعلام کرده است: «نیروهای آمریکا امروز (دوشنبه) در جنوب ایران حملات دفاعی از خود انجام دادند تا از نیروهای ما در برابر تهدیدهای ناشی از نیروهای ایرانی محافظت شود»
در بیانیه سنتکام آمده: «اهداف این حملات شامل سایت های پرتاب موشک و قایق های ایرانی بود که تلاش می‌کردند مین‌گذاری کنند. فرماندهی مرکزی آمریکا ضمن خویشتن‌داری در طول آتش بس جاری، همچنان به دفاع از نیروهای خود ادامه می‌دهد.»
ایران هنوز واکنشی رسمی به این گزارش نشان نداده است، اما برخی از سایت‌های ایرانی از هدف قرار گرفتن دو قایق تندرو سپاه در نزدیکی سواحل خلیج فارس و کشته شدن چند نفر از سرنشینان این قایق‌ها خبر دادند.
نیمه شب دوشنبه به وقت ایران،‌ برخی از ساکنان بندرعباس و شهرهای حاشیه خلیج فارس، از شنیده شدن چند انفجار و فعالیت پدافند ضدهوایی خبر داده بودند.
رسانه‌های رسمی هم این گزارش‌ها را تایید کردند اما اعلام کرده بودند که علت این انفجارها مشخص نیست.
@
VahidHeadline
درباره همون وقایع ۲۴ ساعت پیشه که اخبارش تازه داره منتشر میشه ولی بسیاری از منابع جوری جلوه میدن انگار مربوط به ساعت‌های الانه.
احتمالا
اون پست ترامپ
هم که تصویری از قایق‌های مهندم شده با پرچم جمهوری اسلامی گذاشته بود و نوشته بود «خداحافظ»، در اشاره به همین واقعه همون موقع بوده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/75718" target="_blank">📅 02:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75716">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qAI1kiCwDREhd6UpBiTbQwFqCKnnWIAUVh3judqAis7pBEKYJM6ud4ZGtJh32We67dTyFGn_GQ6aweqvQGXq8gdfnq8R30LJRf8IM7j6da9StJqhZXIPdcvVPvTJSfTLYoNZQvh8QIHelaFRUB6-Ya02Ec8XF77IR_ZEqHZDBV9_2y4V_q1UMyojDdN3aaGehuSRSzmPieIDEyPZDx-_L347hXCsBIs5LuJH9idUk1VyYywT62kYBvHW4aELDQyUjQN5u1eSnvL6lbbev1FTOvsvr82xNd-vLS4WkyrOVVG4XTomavLUuL220MAD0ETvb6T0nQH3_3JoQMSTTVgnIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YW5cfynJlzTpYjLX0cMTeY57hRVU0V0ZL47iubKotc1jJV9mYYMZ8fs1z2TZcyxjka97qSMoO82v2BUJ49Lx2MX018W2qSCytKKWKqOPJRPaVGhlNGcsrv9mclB8EBadQuOPCp1rIM_mWjmP0j6mqTBP4dY0mIkHk3SHNI3Bfe8cnQmS1P5_nRyOrkbySOYGxAPGI5kS40qPyiAcVxe5llvz-8VI044qLDMlY3jtyDXFtuYoRNLbUA1m-PL0Z5_vPYPkQRFrIBxfOALrobcif3wEih8V-_nrCWFtj2WEVB5K9KsJMq9A707bI4036iD7Zh8PTLOxKFVuYb918aOriQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری دانشجو گزارش داد که در ["حمله سحرگاه شب گذشته ۴ خرداد"] در جنوب جزیره لارکآمریکا و اسرائیل به جنوب جزیره لارک، عباس اسلامی، قدرت زرنگاری و عبدالرضا گلزاری، نیروهای سپاه پاسداران کشته شدند.
براساس این گزارش «تعداد دقیق کشته‌شدگان هنوز مشخص نشده است».
@
VahidOOnLine
گویا این واقعه مربوط به اولین ساعت‌های دوشنبه است. یعنی حدود ۲۴ ساعت قبل
ولی به نظر می‌رسه اون دسته از منابع جمهوری اسلامی که این خبر رو پخش کردند عمدا طوری گمراه‌کننده نوشتند که مربوط به صداهای شنیده شده الان به نظر بیاد.
ولی این توییت مربوط به ساعت ۷ شب دوشنبه است که درباره همین خبر به نظر می‌رسه:
دیشب یه قایق سپاه در حال مین ریزی در تنگه هرمز مورد اصابت یک جنگده که از خاک امارات بلند شده بود قرار میگیره و چهار نفر از نیروهای سپاه کشته میشن
YourAnon_Zeus
حالا این خبر درسته یا نه نمی‌دونم ولی مربوط به
صداهای شنیده شده ساعتی پیش
نیست. من هم ساعت سه چهار صبح دوشنبه پیام‌هایی داشتم از شنیده شدن صدا در قشم و بندرعباس
آپدیت:
پست بعدی: آمریکا اعلام کرد که ما بودیم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/75716" target="_blank">📅 01:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75715">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QRQ2uo1RtLspt8tpNWhu8hRLlSAO9wOAsuyaEnKlcveJnBrr5ofxBAiK4PFxTJdbo5dTkcQSjnR3hgw2rHbwCUBdS3XireOxGQVJg0uf8cjA6u_n-uiTQHTiOyuw1VyuwIbBobRPtlCj53ma_L0QArDOMgtzN19Uruap04mZ3tXw0NmvIR5GLUBRX-EVvmP-zv1l1R2j1LtnlbpmJL8rYo8Muu6mEh50z_2g9g9IoiCPWJkLm3mNX0EUst7NT83w4jp4aUO58nBFgQMGqQNSE4BN3KnH6A3L7mlgpdNN1gUjyLS5-kPmFti9px72gSFVuUmKf75RyJQKDdZrhXXv8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اورانیوم می‌تواند در همان محل یا جای دیگری نابود شود
ترجمه ماشین:
غبار هسته‌ای، یعنی اورانیوم غنی‌شده، یا باید فوراً به ایالات متحده تحویل داده شود تا به کشورمان منتقل و نابود شود، یا ترجیحاً، در همکاری و هماهنگی با جمهوری اسلامی ایران، در همان محل یا در مکان قابل قبول دیگری نابود شود؛ در حالی که کمیسیون انرژی اتمی، یا نهاد معادل آن، شاهد این روند و رویداد باشد.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/75715" target="_blank">📅 01:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75714">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">#بندرعباس
پیام‌های دریافتی درباره صدای شنیده شدن صدای انفجار:
بندرعباس سه بار صدای شدید اومد الان
صدای بمب میاد.
بندرعباس ساعت ۲۳:۴۰
همین الان ساعت ۲۳:۴۰ صدای سه تا انفجار شدید توو بندرعباس اومد. نزدیک پایگاه شکاری یا همون فرودگاه بود به نظرم
سلام وحید جان
بندر عباس صدای آزاد سازی پول های بلوکه شده میاد
بندرعباس ۲۳:۴۰ سه تا انفجار شدید
حاجی۲۳/۴۰ سه تا انفجار شدید شرق بندرعباس
دقیقا صدای انفجار ۴۰روز جنگ بود
سلام همین الان بندرعباس صدای دوتا انفجار اومد
بندرعباس حدود ۲۳:۴۰ دقیقه سمت فرودگاه صدای سه انفجار اومد.
درود وحید جان
بندر عباس ۱۱:۴۲ سه تا صدای زدن اومد
بندرعباس، ساعت 11.40
صدای شدید انفجار و لرزش
سه تا صدای انفجار پشت هم شنیدیم بندرعباس
بندرعباس 11:40  شب 4 خرداد صدای انفجار
بندرعباس ۵ بار صدای انفجار
ما سمت پایگاه هوایی هستیم نسبتا شدید بود
پدافند سمت فرودگاه بندرعباس فعال شده ساعت ۲۳:۴۵
آپدیت:
رسانه‌های ایران شامگاه دوشنبه از شنیده‌شدن صداهای انفجار در بندرعباس و همزمان در خلیج فارس حوالی سیریک و جاسک خبر دادند.
معاون استاندار هرمزگان اعلام کرد منشا صدای انفجار در حال بررسی است.
@
VahidOOnLine
آپدیت:
کانال‌هایی غیررسمی نوشتند که به فرودگاه بندرعباس و اسکله باهنر حمله شده. منابعی مطرح هم با تاکید روی غیرقابل تایید بودنش نقل کردند ولی منابع رسمی چیزی ننوشتند که لابد مذاکره و توافق به خطر نیفته. تکذیب هم نکردند. حتی منابعی هم مدعی شدند حملاتی از سمت اسرائیل یا امارات بوده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/75714" target="_blank">📅 23:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75713">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e6990989c0.mp4?token=cRuX_CUNbwBIpokjnKdUmltHLYXtowWi_Xzxix6bjzocYsN8PP64TEpzwWX0FDX1dqSHumfo4HY0F8aIkWClU5jRlqEq85ncGNwO7exUg9w2er2iS8ntUw8QwNRI52PMLtKgOmR4iR7dFKaa2qf7xWOEDJ1cks57I6lBkHLq-87CKBFn-T0VbFdVLR1kXaeLmCiNFAPY6M9SbZCWmVg9aTuWD8bDPD07i9c65E0y1ivTRqU29E-Xg1qZtL-GHYwZUG-wZlcUopNXvDICY2UbZ8nB_9Wi6vRA8P42SL5cWgHrAIaJDZOoQe7FztJWimLIw6tIAM0gs_6EmhrTtlTVsg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e6990989c0.mp4?token=cRuX_CUNbwBIpokjnKdUmltHLYXtowWi_Xzxix6bjzocYsN8PP64TEpzwWX0FDX1dqSHumfo4HY0F8aIkWClU5jRlqEq85ncGNwO7exUg9w2er2iS8ntUw8QwNRI52PMLtKgOmR4iR7dFKaa2qf7xWOEDJ1cks57I6lBkHLq-87CKBFn-T0VbFdVLR1kXaeLmCiNFAPY6M9SbZCWmVg9aTuWD8bDPD07i9c65E0y1ivTRqU29E-Xg1qZtL-GHYwZUG-wZlcUopNXvDICY2UbZ8nB_9Wi6vRA8P42SL5cWgHrAIaJDZOoQe7FztJWimLIw6tIAM0gs_6EmhrTtlTVsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست وزیر اسرائیل، روز دوشنبه خبر داد که دستور حملات تازه به جنوب لبنان در تلاش برای «خرد کردن» گروه حزب‌الله را صادر کرده است.
ساعتی بعد خبرگزاری‌ها از چند حمله شدید اسرائیل به این منطقه خبر دادند.
نتانیاهو در ویدئویی که در شبکه تلگرام منتشر شد خبر داد که خواستار «سرعت بیشتر دادن» به حملات ارتش اسرائیل شده است.
او همچنین حزب‌الله را متهم کرد که با پهپاد نیروهای اسرائیلی را هدف گرفته است.
صدور دستور حمله بیشتر به لبنان، همزمان است با خواسته دو وزیر افراطی در کابینه اسرائیل که در همین روز خواستار تشدید حملات به جنوب لبنان و همین طور پایتخت، بیروت، شده بودند.
حمله اسرائیل به این منطقه در حالی رخ می‌دهد که در سوی دیگر تهران و واشینگتن از جمله درباره پایان جنگ در لبنان مذاکره می‌کنند.
حکومت ایران در هر دور از مذاکرات اخیر خود با آمریکا، پایان جنگ در لبنان را نیز خواستار شده است.
حملات متقابل اسرائیل و حزب‌الله در حالی رخ می‌دهد که دو طرف بیش از یک ماه است که به طور اسمی در آتش‌بس به سر می‌برند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/75713" target="_blank">📅 23:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75712">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H4Lcc12KyGmkj_7YZLfDz1M9UsCp-ZsUEIxLOJXKqA4rDEG-x0pB_xAM4YIH3GZoVDP5z1Rccbk5QTI8uNAjCNW3b0hAXRWUPLdbxouWMWMZ7u8yxdOvLRJrXcJlsJj4QAjcraFpiXKTLI-a59akt-GPPqmgeRrEhtSGTcqXttie-YXVr4kXiIGkIwoj3bsbkjKeAGuNZKrY1M-BLe8r6cLHAgeGiDipeL3DFXDVP4LDL7kSTW69eKfYl6yOuRKAVpeWme6a8rb_XQ-SFLGOu3oY1OQsraiJNpMa4URjip_d5zsZJ5ikvgGXf42IUf-aEzsYQtBSTyJe97ZodgQwTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره به نقل از یک منبع آگاه
گزارش
داد میانجی‌گری قطر به دستیابی به تفاهمی میان آمریکا و جمهوری اسلامی درباره دارایی‌های مسدودشده ایران منجر شده است.
این منبع افزود با توجه به اهمیت بالای این موضوع برای ایران، احتمال زیادی وجود دارد توافق میان آمریکا و جمهوری اسلامی فردا اعلام شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/75712" target="_blank">📅 23:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75710">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6zraI_zoVY_YN9CAM7guWdsMFDAV7gAuARuX1pFcwB6rdSLJSZiQ4dJUDX4eiJN2BFMGhYXzrk_9bce3uw3g-U9hL3cgQ4gvKMjY3e7eM3dn4PUEeVdivBiBTy41GrK53T67pgyjsHLumePeEqA-RYCFL8tHuCfkQvwkTcZyJTtMKa5psZjCBU-CMnkMW3Tw-VhqaXTXxxCma0jsOUgb2OR_SedTAq2W3X3YFyG62k5bH52kfAkbnINCZY_BKlPcIERxAkscTnloBJYVvc6ajHTZLkVnVrbuhDEyLAmYolvWvhC_BaxFs2OVe66tIqSYGGfxeZQrw7yuXeWnfBiJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعاتی پس از انتشار خبر تصویب تصمیم بازگشت اینترنت به خانه‌های مردم، چند رسانه در داخل کشور می‌گویند که مسعود پزشکیان، رئیس جمهور، این مصوبه را به طور رسمی ابلاغ کرده است.
رسانه‌ها در ایران روز دوشنبه از تصویب مصوبه‌ای «جدید و مهم» دربارهٔ اتصال دوباره اینترنت کشور به اینترنت بین‌الملل در «ستاد ویژه ساماندهی فضای مجازی» خبر داده‌ بودند، مصوبه‌ای که برای اجرا نیازمند تأیید نهایی مسعود پزشکیان، رئیس‌جمهور ایران، بود.
به گزارش سیتنا، پایگاه خبری فناوری اطلاعات، بر اساس این مصوبه، اینترنت عمومی باید «به وضعیت قبل از دی‌ماه ۱۴۰۴» بازگردد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/75710" target="_blank">📅 21:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75709">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SL31AxMm6ZDFYXM5ReVDc_5cT-Sfscmg4CePf_khNjbgh97-cpRggyRBxmaBPVwuOuuAY4Fxx4WqMBM5XNcsfaq8rT45ShD52SnzyU9rElx78ziFMUHzN2HXi8PSWzWOAms59wzZ-D0XKubuRopCwsKQlKUZ9L39cTPsYHnxD4-Bjn6tj8ZDVz9o_JA9Hd0sVSoK2_jOC6Br3JInhnpHPfl2JNQ5vj8uRZAymIX7RPZzMS5ZAYNYa2BHCpUMQ8VU2fNANDg5ofc_1WkEpOjWLMx_L6yQjZAbXRkiIv6D0r_IryhA49LrDtHLuyTZmEvO4q9TJLEucw5Z8ZwAMXPjeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العربیه به نقل از منابع آگاه گزارش داد پیش‌نویس یک یادداشت تفاهم اولیه و نهایی میان آمریکا و جمهوری اسلامی در حال بررسی است؛ تفاهمی که شامل بازگشایی تنگه هرمز، تمدید آتش‌بس و کاهش برخی محدودیت‌ها علیه ایران می‌شود.
بر اساس گزارش العربیه، در پیش‌نویس این تفاهم‌نامه آمده است تنگه هرمز بدون دریافت هزینه از کشتی‌ها بازگشایی خواهد شد و عملیات پاکسازی مین‌ها نیز انجام می‌شود.
این گزارش همچنین می‌گوید در چارچوب این تفاهم، به جمهوری اسلامی اجازه فروش و صادرات نفت داده خواهد شد.
العربیه افزود پیش‌نویس توافق شامل تمدید ۶۰ روزه آتش‌بس است و امکان تمدید دوباره آن نیز وجود دارد.
بر اساس این گزارش، آمریکا همچنین متعهد شده محدودیت‌ها علیه بنادر جنوب ایران را کاهش دهد.
منابع العربیه گفته‌اند بخشی از دارایی‌های مسدودشده ایران نیز بر اساس سازوکاری مشخص آزاد خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/75709" target="_blank">📅 20:17 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75707">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FYD7mv72cZs73Ursgv3Q5Ldg2QnE_5j1mpu3aG0ZcdBeEedAdkdFirKJc7izqABcs_WGF_OsG-_mdXC683ukeq3RaZRi4tCLoOx-42NRBHj5TdSmPIBn_v2p9CYG1RfyGdA8jVXzQmd4Bq0Frzu0A1LyIM_PSFOJLP1wnG3jZMUOKk8a6Bcl5wMOzyXfaYDHbJIBagz753Y0v5du5oEO7lRP5XRFpMuffPzGb0l1lvB3VhFc3lLLStChYXhoNR7lOZOHtIGYJME3kGs8lazu4hTDzca0RbhTTQHlNolSrwhI1VF4jtUWlYhq1KdYY576go-j21KldRUzf1IzYVxLfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bD-0ZQY-LmP3LsGGRr3spRzE7zrYuQr9_HV_e0kQJJKuD9lvdxeDCj66N0LMOSRBOpKIWY2VkQ6vzmJ5AAMZlJ-XjVhZmy1pzlhPub1FVawVsBqVvs78I7HfAn2KP1JXIkm-BPLLcgLaWuT5cuEgPmkhAq8DwqlbqVaeGdTTb3mIOmhfpmyuVAAyO6oMqK7KNZ-XGaBi_uKXhtKAJXvn71nKFC1rmXVksC-zRbJnn65l0s07JUZN3kcqckKVEM7iA2O6844nEWvxftFuxS6jjL5nx1LZHm4KjqlUKzHCKZhhUrNeyUJjBBZLOx4r68114zolJI9IPbJuWttG_fFt_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی، در پیامی با اشاره به «میدان نظامی، میدان دیپلماسی و مردم مبعوث‌شده حاضر در خیابان» نوشت: عقب‌نشینی در کار نخواهد بود.
او تاکید کرد: بیش از هر زمان دیگری به وحدت و انسجام نیاز داریم تا آمریکایی‌ها و اسرائیلی‌ها مایوس شوند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/75707" target="_blank">📅 19:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75705">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KE-_rVuAvMhcdxW1NaiVii0ILQxWK7NpBGMWaGLEMjW90MfAQ0mpk6j6YjX4evsTddoLv_CI7JvaIq6HaHD46O_kyPvZnRD_aAr3C8Ayn1ERVcE8tTdMr4DYh6xctYzXBgCWRg4OU8wEl5JH1_ubBQpukc1urtQEGgTcVUI4GEEic6TKKXm3zviOwkcu3YkMyyCZw_RFIoztRKkB2MoFeO5Ryvbso9eqXfoV9OdLyT7c_25PUz8s-PifY6g0iybfs2TF1zjdttqNTCU2vhONZu8ED0V91QWf6lY_TSLX1ftI8AxVrt3J8ebOpHPYy7-Cvz3__hITIvISc-RLZpx2lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FcAIKj_197I8_ZKITxOftAe3_dmSKpE9rvMwScrzXT4nI6KWjw3lF9nNqr0p7thNLSF71VP9kq77EimeFKMSQlLXwr01VcCXpLwnW288lRNiDhdisHO343ONpdXhIjGKz5wcsj2y3t0a7tQVfrZNGWr_a1GXjej2NJWu4yb0plM0ZVAvuq0ILs_nu4Orz-LISK2XBbkirLfeGjRAdAGDsLjpZ9meQWyPr8lW-UJNISLgC56fWnVvKAWyP24SUCLn--BqA21_zxgx4z-hrF4ZRDhF-u9dtpWRUurIcRMnxOHR0nwGZ56OHllvrsKKci3pgJbztq2XI4w1CK954ijg4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری که ترامپ از اکانت بقیه بازنشر کرده.
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/75705" target="_blank">📅 19:17 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75703">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hQeCbSNaBJOmZLXfSy6evJz90hv1rVhaq_zE0B502lE31nJM-WrTkNzc6xNhdZiDMdxMpkT-_N7FzbdyV8dh9356G6XBjBVnfh3ONyIfgjKDpy3aLAlzg8lHYRUkNJ1TvWIr3VybfbrHkEODELkWrqHnal9_sibg6FX8y_VMA2NyWvCsk5UeJ6aojj3LRn8XabnLBf_TJ0fF2z3FhNGCD7NdQAy-4Hl9YnZe4UhiV2Lxvn7PkP89hJa9yoJQdKCDCo2eOZu8S_a-pYZtsZlr7HRtGA6eBTTzx53mYyH10S843drjxhw08_hv1ybmdBgWETzxtWQ16R6pyw1IjMG0-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kiKLLTHo5akTI0bNVvxA_qxAgJ-gdDOIwTvjPbcBdCNtvClZ8GootQ0Nf4xJSyGimfcatbu7xf4TbQT53aETo5Gv-_Arg6jMx7GZ5t_1VSS5rXgpjJdFfSAU3sdCG98tnZJmN8makMAiJyPpkiWdqVGUCwRzRFg-i-rRTh0XI4IZ-iaoaGFnI6tT4VxDNx5bd-H6nK808pPhmfO_Dbq9Dtz_GzaKRMDDmGihBOu3q8QxuKJIXAi2s6cY9_GzXHl9O7-4v5BNIJ3nLvU5hyiYNaj-OB3Q-dsvuypfWrM6Q2CkgOcL6bXfukB7bv9GgxrwdBkxTd7NvdZrrRUa1PPKbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهور آمریکا، روز دوشنبه در تازه‌ترین پیام خود در شبکه اجتماعی‌اش ضمن خبر دادن از پیشرفت «خوب» در مذاکره با ایران، از تمام کشورهای دخیل در این مذاکرات خواست پس از حصول توافق با ایران، بلافاصله به پیمان‌های ابراهیم بپیوندند.
پیمان یا پیمان‌های ابراهیم طرحی بود که دونالد ترامپ در دوره اول خود برای تلاش در راه عادی‌سازی روابط میان اعراب و اسرائیل آغاز کرد و موفق شد تا چندین کشور از جمله بحرین و امارات متحده عربی را هم به این کار ترغیب کند.
حال رئیس جمهور آمریکا روند توافق با جمهوری اسلامی را به این طرح پیوند زده و به گفته خود این «خواسته اجباری» را با دیگر کشورهای عرب خلیج فارس و همین طور ترکیه مطرح کرده که به‌فوریت و همزمان به پیمان ابراهیم بپیوندند.
@
VahidHeadline
دونالد ترامپ در شبکه تروث سوشال نوشت که پیوستن جمهوری اسلامی به پیمان ابراهیم، می‌تواند به «اتفاقی تاریخی» تبدیل شود.
او افزود که در گفت‌وگو با سران عربستان سعودی، امارات متحده عربی، قطر، ترکیه، مصر، اردن و بحرین، تاکید کرده لازم است همه این کشورها به‌طور هم‌زمان پیمان ابراهیم را برای عادی‌سازی روابط با اسرائیل امضا کنند.
ترامپ نوشت: ««کشورهایی که درباره آن‌ها صحبت شد عبارت‌اند از عربستان سعودی، امارات متحده عربی (که هم‌اکنون عضو است)، قطر، پاکستان، ترکیه، مصر، اردن و بحرین (که هم‌اکنون عضو است). ممکن است یکی دو کشور دلیلی برای انجام ندادن این کار داشته باشند و این پذیرفته خواهد شد، اما بیشتر آن‌ها باید آماده، مایل و قادر باشند که این توافق با ایران را به رویدادی بسیار تاریخی‌تر از آنچه در غیر این صورت می‌بود تبدیل کنند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/75703" target="_blank">📅 18:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75701">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/J-CRXPVMXF8Cj3QLNTiyzGVQmPvvkcXYJw_hgHCcxGMRaw31ya-CZ4vwveyG7qT5Ii1KoYebLvHm5HhBz9Gu4d54nKrXp7kVY5mSfTiBcqyIGTBaLV1ieCnXE_LP_HJ5q9eBc3JU6iflCT3Gx5hJ5iCsH9kMZDKBW4i35DowGuo5-nQOnTkF-u-0ghZksNQwGwTsGUuXmYOQRaUtBOIwnsKhWB1vORYk4GFjUQfm_e7i_TdZNbWhJjwxmX0dMaKv5ypHSSHTjogbI-YM9PqG41WCGCDKwXiPyXqCyqYweYBoCliNNs9I7X_qcOTYAccEJxOlpipwmRJiUyfVzc3TkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Y2afIHdV7q5hMIiCoUKiIDDOqwCFZZ3dQICJrmPuDxS0hyuM5VHBZoH-XVODddhnc7w6yEjjrfWeQdyjdh6lhEth5jx2IHkPkNOn7AzttkA7aZFUdBhNKdnugMXxqzeP9ZxoP-XNIKxAmfQckWu4c4Cn-jyjiZaMhozdObOop0Ue7HlDwRclKQJ1REuqswqzu4ZAM9ZmZVo2euvfEmVbyXvpvGGJcHii7t00J89M22ZHioO4Z9tzt6PtE1kQZbJ1AGiAXVQ1qFKXFUSAw1HBlMqGvt8fF6DbOIctubhoyEOl0DqAildfIDjEaxFCa9OTdR5WQBC0Rl8CPhahx5HZ4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری‌های رویترز و فرانسه به نقل از یک مقام آگاه، از سفر غیر‌منتظره محمد باقر قالیباف و عباس عراقچی، مذاکره‌کنندگان ارشد ایران، به دوحه خبر داده‌اند.
بر اساس این گزارش‌ها، رئیس مجلس و وزیر خارجه ایران برای گفت‌وگو با نخست‌وزیر قطر به دوحه سفر کرده‌اند.
رویترز نوشت که این گفت‌و‌گوها عمدتا درباره «تنگه هرمز و ذخایر اورانیوم غنی‌شده» ایران است.
رسانه‌های ایران گزارش داده بودند که عبدالناصر همتی، رئیس کل بانک مرکزی ایران، برای «بررسی آزادسازی اموال بلوکه‌شده و در راستای کمیسیون اقتصادی مذاکرات» به قطر سفر کرده است.
هیئتی از قطر هفته پیش به ایران سفر کرده بود.
یکی از خواسته‌های ایران در مذاکره با آمریکا آزاد شدن منابع مالی مسدودشده‌اش است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 234K · <a href="https://t.me/VahidOnline/75701" target="_blank">📅 18:49 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75700">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBlZPsWDpRa1sil7-vJQBiul5dZtsyfpKLBjMgHcGz0it6TbZkLpK_TtV5fDcaoQeJk996sXmzscm0zKG2kYSkd04gp0Bgxf9Ox0QevARBofcosoi9i7ihvIp6NMuJoOGgWrzNxc0x1p4HLIdNwRkzYzAxv4Mo-E7iYjEGliipTEMqp7ZpfjuM8tH6ujxvi31ioIjv1-vYYlnlvlm7fUkn8vrD0xOTz96-iCMqSavsjBLmU3EPfJwkBd0Zj2R82Cg2kr8OKduqqyEyWcBedV4VCNaIk7HgzS8IlEnxEBT4CwtDDXKDYX2j2G0Hz82u0DhARrey0TOSKHp6AZnNXPeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در پیامی در شبکه اجتماعی تروث سوشال گفت توافق احتمالی با ایران یا «عالی و معنادار» خواهد بود یا اساساً توافقی در کار نخواهد بود.
آقای ترامپ در این پیام، منتقدان خود در میان دموکرات‌ها و برخی جمهوری‌خواهان را به باد انتقاد گرفت و گفت آنان «هیچ چیز» دربارهٔ توافق احتمالی او با ایران نمی‌دانند و حتی دربارهٔ موضوعاتی اظهار نظر می‌کنند که به گفتهٔ او «هنوز مذاکره نشده‌اند».
ترامپ تأکید کرد توافق مورد نظر او با ایران «دقیقاً نقطهٔ مقابل» توافق هسته‌ای برجام خواهد بود؛ توافقی که او بار دیگر آن را «فاجعه» خواند و دولت باراک اوباما را به گشودن «مسیر مستقیم و آشکار» ایران به سوی جنگ‌افزار هسته‌ای متهم کرد.
او در پایان پیام خود نوشت: «من چنین توافق‌هایی نمی‌کنم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 202K · <a href="https://t.me/VahidOnline/75700" target="_blank">📅 18:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75699">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nafRKokUQ7BOJrk-MvNYkA-VbqgT3gI6OXwLrzeCKcrEU6R2sMWG8Q-LN_JpF3qA0gTiw9keZkpZqNqGxfpHxlKMmMuORPPtIMmmTa-6lVg9zLMfQfoMIzcj6K_xv3RSxdmKTRX_aRIXcyq6fixw6jpvyc2NdfhX-igqHgYWyOnkzrdtui_p_f6u6dBB6NwCEzn_gqOeUnQiUjwhUrG7kBV3ikAOaGO9tTO8J88FGGMGlsiG4R1bpsSARFxxyO2_1iBX6vCioNWfoW2ROnTdVx0Bmr3Z0NAoKPEEnozWoyystZ3FtTUiLxh12MqwuRDVlgLj_qw_6MclKjbuWvtPKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران از تصویب مصوبه‌ای «جدید و مهم» دربارهٔ اتصال دوباره اینترنت کشور به اینترنت بین‌الملل در «ستاد ویژه ساماندهی فضای مجازی» خبر داده‌اند؛ مصوبه‌ای که هنوز برای اجرا نیازمند تأیید نهایی مسعود پزشکیان، رئیس‌جمهور ایران، است.
خبرگزاری فارس روز دوشنبه چهارم خرداد گزارش داد چهارمین جلسه این ستاد به ریاست محمدرضا عارف، معاون اول رئیس‌جمهور، برگزار شد و در آن «مصوبات مهمی» دربارهٔ اتصال به اینترنت بین‌الملل به تصویب رسید.
فارس به نقل از یک منبع نوشت که «برقراری اتصال اینترنت بین‌الملل» با ۹ رأی موافق و سه رأی مخالف تصویب شده و برای تأیید به دفتر رئیس‌جمهور ارسال شده است.
خبرگزاری تسنیم نیز با انتشار گزارشی مشابه نوشت مصوبات این جلسه پس از تأیید نهایی رئیس‌جمهور، برای اجرا به وزارت ارتباطات و فناوری اطلاعات ابلاغ خواهد شد.
در همین حال، سیتنا، رسانه تخصصی حوزه ارتباطات و فناوری اطلاعات، به نقل از «یک منبع آگاه» گزارش داد که در جلسه صبح دوشنبه «بازگشت اینترنت به وضعیت قبل از دی‌ماه ۱۴۰۴» مصوب شده و در صورت تأیید مسعود پزشکیان، جهت اجرا به وزارت ارتباطات ابلاغ خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 195K · <a href="https://t.me/VahidOnline/75699" target="_blank">📅 18:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75698">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMH8WzUoP9yjvYl3bNbYQIRJlcPYVEtE7loSQrko2tF3NvluOGV7LMHPkwCIYYQIeav9azb04ECbntTJ5xH2eKRzn1jWHxORtSYkETp6zpAvwKCe74MRbre2BQTU1S7ZOfuRAdaTwGXznoniY5M2W0Qv0uUt9zQFkZ5r3fJU25bwikwwKxqVwQNId0b1ujVLPE_nWZQjYfsU_avM3qhtnIJW-R8o0ZZT6XlH-RCG6tsAN1_La2xvdU7Jv77nAIdstWNC1WCW_NoRlDedwCrPs76VnfGLSCMJGEPJ1l8QZYfHpU6TS4Bca-NrPGwF_L3x4hADQSwSlhBDNns-2dcTIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران به نقل از «حسین کرمانپور»، رییس مرکز روابط عمومی وزارت بهداشت، گزارش دادند که جراحت‌های وارد شده به «مجتبی خامنه‌ای»، رهبر جمهوری اسلامی، در جریان حملات اخیر «سطحی» بوده و مشکل جدی برای او ایجاد نکرده است.
کرمانپور گفت رهبر جمهوری اسلامی تنها از ناحیه صورت، سر و پاها دچار جراحت شده و این آسیب‌ها «منجر به قطع عضو یا ناراحتی خاصی نشده است.»او همچنین مدعی شد که هنگام انتقال خامنه‌ای به بیمارستان، پزشکان از او خواسته‌اند روزه خود را بشکند، اما او تا زمان افطار روزه‌اش را ادامه داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 185K · <a href="https://t.me/VahidOnline/75698" target="_blank">📅 18:44 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75697">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/due79Cqc-51lbLMeo6mOvT-ydIO9ilu25nXM3qUcXu9BUPQpfHZgzrpDk96Ceu5-Qj4PVb5JukNnmxzKsT1kZUQyb0ozjq9svo0q8-rF2xBNNs04Ppx2qIrWOBVL_E3peS2wvUdDDU872hWnnnhQ4CEt5dj2GQuA8KV94o7wxj_7ufRZd_n8n41-176F1IgzoJCN39UeTCXWC0yzdQYnlisUIveWh4759a1a4NhrvvI46ma-cfuNGV6mkj_i_Uz0exqc4fZQJwELLcHjVN3rs4jhkLISQG9hGQZnMfQocq1xENa5UNQKc5miZ_5AohwQkCZ7doMYKoF7DJnhUVBKoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران می‌گوید که سفر وزیر خارجه به نیویورک برای شرکت در نشست شورای امنیت «منتفی» شده است.
اسماعیل بقایی، سخنگوی وزارت خارجه ایران، دلیل انجام نشدن سفر عباس عراقچی را «مشکل روادید» عنوان کرد.
آقای بقایی چهارشنبه هفته پیش درمورد حضور آقای عراقچی در این نشست گفته بود: «این سفر به نیویورک احتمال دارد انجام شود و البته ممکن هم هست انجام نشود، چون هنوز قطعی نیست. دلیلش هم این است که هم باید روادید صادر شود و هم ممکن است اولویت‌های دیگری داشته باشیم.»
چین به‌عنوان رئیس دوره‌ای شورای امنیت، سه‌شنبه ۲۶ مه یک بحث آزاد در سطح بالا با موضوع «حفظ اهداف و اصول منشور سازمان ملل و تقویت نظام بین‌المللی متمرکز بر سازمان ملل» برگزار خواهد کرد.
این جلسه به ریاست وانگ یی، عضو دفتر سیاسی کمیته مرکزی حزب کمونیست و وزیر امور خارجه چین، برگزار می‌شود.
چین این نشست را «فرصتی» برای همبستگی و اجماع کشورهای عضو توصیف کرد تا «تعهد راسخ خود را به حفظ اهداف و اصول منشور سازمان ملل متحد مجددا تصریح و نقش محوری این سازمان را در نظام بین‌المللی احیا کنند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 207K · <a href="https://t.me/VahidOnline/75697" target="_blank">📅 18:44 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75696">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1hE8VM-JdqkZV_ESOT14UHYqzJIPRiDCVSGO32nut41G5JUYx2KXR8QwNKP0QKuQZP40UCzjEXKrZnfDvxw6GrrR-Pl-vS4RLT6Mu7Non3RPfkbY3UyzfOp_QLoYGHQNpeAGLOaF-nn3VIcabBl-it6N5CXyIwufG9Y4fJBGA28dRNrPtoAvaON83vz-LMw2KkDW3N3MpO9eGkpg_POpwDb80Bioslfi8e-QSlpRCGpIPK-5yBAf7dY5nVYXlKJhT9261HoMreL86v2fD-EdFcTlhVFSiqaqs3rz9bxqy0vyQ_e4WNT4u5pIyq2HYahM25vfNvuLdYzhE3iPlWDgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز سه‌شنبه ۲۶ اردیبهشت‌ماه ۱۴۰۵، «جانا سعدوئی»، زن ۱۹ ساله، مادر دو کودک و اهل روستای تاریمیش از توابع بخش قطور شهرستان خوی، به دست همسر خود به قتل رسیده است.
به گفته منابع آگاه، همسر این زن پس از وارد کردن ضربات مرگبار، تلاش کرده است ماجرا را به‌عنوان «خودکشی» جلوه دهد.
با این حال، نتایج بررسی‌های پزشکی قانونی و تناقض‌های موجود در روایت‌ها و اظهارات مطرح‌شده، ابعاد این قتل و تلاش برای صحنه‌سازی را آشکار کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/75696" target="_blank">📅 18:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75695">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZgsMMceApRJxBMwwdFVUv-GXNz0Cq6twRM1a4lKe9F7fUJRQfMW78DBVYCVgnx6C_tFH9cCvDbxm2sDCaZIrrLu1pU_vigPDD5-TXWbiZH_G-JYYQB_XQdKgcnGBBHBf0yysCIkePI13Xb1GRtoe56M2NSVdcTweAtNLLJjqRYolXvqKEl1JzIYygqZHce8dLbOOjb2vJ9o72n-XrkmsZLvI-F-XDnopu4RZzf6ZIIAdHRh7-i6yOJdc3IpZDWGXsFfaYejYJZi00vrCNxo4b3zvf37TuuBrc2La8uN6nNzISDemKSU0M6M56jO3d_oGbY95Jq76FwjkCrZFFjb8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه ایالات متحده، روز دوشنبه چهارم خرداد گفت که واشینگتن در مذاکرات جاری خود با ایران، «هر فرصتی برای موفقیت» به دیپلماسی خواهد داد.
مارکو روبیو که اکنون در هند به‌سر می‌برد در جمع خبرنگاران گفت که مذاکرات با ایران همچنان «در حال پیشرفت» است و خوش‌بینی محتاطانه‌ای نسبت به توافق احتمالی برای بازگشایی مسیرهای کلیدی کشتیرانی و از سرگیری مذاکرات هسته‌ای ابراز کرد.
او که روز گذشته از احتمال توافق با ایران تا پایان روز یک‌شنبه خبر داده بود، گفت: «همه ما باید مطمئن باشیم که یا به یک توافق خوب خواهیم رسید، یا مجبور می‌شویم به شکل دیگری با این مسئله برخورد کنیم. ترجیح ما این است که یک توافق خوب داشته باشیم.»
دونالد ترامپ، رئیس‌جمهور آمریکا نیز شامگاه یک‌شنبه در دومین پیام خود درباره روند مذاکرات با ایران اطمینان داد که توافق احتمالی با ایران «خوب و درست» خواهد بود اما هیچ کس درباره محتوای آن اطلاع ندارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/75695" target="_blank">📅 09:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75694">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGFytVMtQ7dTGH4ABFWIf-TBd5D7XTkggSeQTcRm-IX7IR79yEmCG54aUuFulHCDgcvPmeYvTn4U5mDCyh_u7UiRDGvMIzJQdytS5M2AcYkJC00oYEcEV8rwX_D7fNzBQYrje2JIyrS6w2bjT8CjMfPE1NxfnBDwXD_BcbDcpGtEucKMVnEO45uZkwHchqfevsLRnFWLAfAotBGBie0wOhFW8lQwVkIKogpi92LeHwXEb5RWdRsgPVbYcMlcdq4dJW1caCnAYRG5OSrckalVwEAI3ipvGIPxLP4IyQQJRZDhr-70fmvga232OsaVarXDpp4piZb_lQhezQsuhHaiSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری «میزان» رسانه قوه قضاییه جمهوری اسلامی اعلام کرد حکم اعدام «عباس اکبری فیض‌آبادی»، از متهمان پرونده اعتراضات دی‌۱۴۰۴ در شهرستان «نایین» اصفهان، صبح روز دوشنبه ۴خرداد۱۴۰۵ اجرا شده است.
«میزان» مدعی شده که عباس اکبری از «لیدرهای مسلح» اعتراضات در نایین بوده و در جریان حمله به فرمانداری این شهر و برخی مراکز حکومتی، به سوی ماموران امنیتی تیراندازی کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/75694" target="_blank">📅 09:25 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75693">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X8kob5olqDSZeZMSXPrnY6Ypn_BOfguFP0PKHZnBfsMnNVO-Ubo3HcPadN2VB0MD-b8A9KBveS5A7El6QbmNuYO8dPdF2VT5zp7e4nUwC6OOMAIxVmwRMbIwAgddeUvkenCr174alwyL7lkciqOKycidoLrAuGLsIHzDUVDq_0I0BKZQfMxiZy7zsrJrDEYrXjJbvh1-VMhDYVPHjZWJw8JM75Q8Hz4JRTFF74XxpO1T3CoQiSOcpty2dQ3jEMUBnABxZanuh1tNHbFGCxSV_GPdjTxQ0Z2hX3HHRS_PG8KBDjDBNajw5uKxPXuMg_bzV9o_QJ587Y-AwVs22HO_qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌بی‌اس: مجتبی خامنه‌ای در مکانی نامعلوم با دسترسی کم به دنیای خارج پنهان شده است.
ترجمه ماشین:
اطلاعات نهادهای امنیتی آمریکا نشان می‌دهد که رهبر عالی ایران عملاً در مکانی نامعلوم پنهان شده، دسترسی محدودی به جهان خارج دارد و ارتباط با او تنها از طریق شبکه‌ای پیچیده از پیک‌ها امکان‌پذیر است؛ این را مقام‌های آمریکایی آگاه از موضوع گفته‌اند.
به گفته این منابع، مقام‌های ایرانی که مجوز همکاری با دولت ترامپ را دارند، برای برقراری ارتباط در داخل ساختار حکومتی خودشان با دشواری روبه‌رو بوده‌اند؛ مسئله‌ای که یکی از دلایل اصلی تأخیر در روشن شدن جزئیات توافق احتمالی با ایران و توافق‌های قبلی بوده است.
دو مقام آمریکایی گفتند وقتی آمریکا جزئیات پیشنهادی را ارسال می‌کند، دشواری دسترسی به رهبر عالی باعث می‌شود گاهی پیش از دریافت پاسخ از سوی آمریکا، تأخیری طولانی رخ دهد.
سخنگوی کاخ سفید از اظهارنظر درباره اطلاعات مربوط به محل حضور رهبر عالی یا روش‌های ارتباطی ایران خودداری کرد.
یک مقام ارشد دولت روز یکشنبه گفت رهبر عالی با چارچوب کلی پیش‌نویس توافق فعلی موافقت کرده و دونالد ترامپ، رئیس‌جمهوری آمریکا، در تروث‌سوشال نوشت که انتظار دارد ظرف چند روز آینده پاسخ نهایی اعلام شود.
مجتبی خامنه‌ای، رهبر عالی ایران، که در حملات آمریکا و اسرائیل در عملیات «خشم حماسی» زخمی شده بود، برای جلوگیری از حملاتی مشابه حملاتی که به کشته شدن پدرش، آیت‌الله علی خامنه‌ای، منجر شد، تدابیر بسیار شدیدی اتخاذ کرده است. علی خامنه‌ای از سال ۱۹۸۹ تا ۲۸ فوریه بر ایران حکومت می‌کرد. مجتبی خامنه‌ای از پیش از آغاز جنگ تاکنون به‌طور رسمی در انظار عمومی دیده یا شنیده نشده است.
یکی از مقام‌ها گفت اطلاعات به‌دست‌آمده توسط نهادهای اطلاعاتی آمریکا و اسرائیل از داخل حکومت ایران، امکان شناسایی و حذف بخش بزرگی از رهبری ارشد ایران در جریان جنگ را فراهم کرده است.
منابع گفتند در حال حاضر بیشتر رهبران ایران نور روز را نمی‌بینند، هفته‌ها در پناهگاه‌های به‌شدت مستحکم می‌مانند و جز در موارد کاملاً ضروری از صحبت با یکدیگر خودداری می‌کنند.
یکی از مقام‌ها گفت: «تماشای تلاش آن‌ها برای فهمیدن این‌که چطور با هم حرف بزنند، تقریباً مثل تماشای یک سیتکام است. آن‌ها کاملاً به ستوه آمده‌اند.»
شدیدترین تدابیر احتیاطی از سوی رهبر عالی اتخاذ شده است.
بر اساس طراحی این سازوکار، حتی مقام‌های عالی‌رتبه حکومت ایران هم نمی‌دانند او کجاست و هیچ راهی برای تماس مستقیم با او ندارند.
در عوض، پیام‌ها از طریق شبکه‌ای از پیک‌ها منتقل می‌شود که با هدف پنهان نگه داشتن محل حضور رهبر عالی ایجاد شده است.
یکی از مقام‌ها گفت: «به همین دلیل است که می‌بینید برخی می‌گویند: "رهبر عالی با چارچوب موافقت کرده" یا "منتظر پاسخ درباره نکات نهایی توافق هستیم." هر اطلاعاتی که به او می‌رسد، از پیش قدیمی شده و پاسخ‌های او با تأخیر زیادی همراه است.»
رهبر عالی در قالب کلیات با زیردستان خود ارتباط برقرار کرده و به آن‌ها جهت داده است که درباره چه موضوعاتی می‌توانند مذاکره کنند و چه موضوعاتی نباید مطرح شود.
cbsnews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/75693" target="_blank">📅 03:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75691">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vzJ0_rfyTYZjVDEzp1ocv1tV5DrEuhq8ceCqSg1mk3lQhDPl6qIZTmff7SeziJHl_R89AaX5cPVOt_7uDsKnQOtg_xQS_8S6yRdKzqnvGBe5JXFb5jCVFEetAr0v_RxHkyZumlKnJBTb-xMZSUPAIh_TW11zEyfKhYBIOpQT-NGwXIKmFYUhkxIzrYgpxQ1drznLM1bfipSk6I4q8cfsIlgWqG7Afy1QSiIN9yQ_RwM0zaUTQK6Jfg68YMfK9bQci8628eUBkdQzrmM7GKd5f_78n4VCeVjOzsYD2W0E8lPfLA-RwmbKFyme2mlD4dd5IjSdaU-_frEaBNO0NshdSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Zvhd687PWr0Br8A16ixOozoLP1xolpnvY-AHoHvHB7zFj6OGpXG1T6jmHP9gtWUiOIuh-CXuSXBqcUx0UYJDhoXhNBuZx210S2I64p1p4CHSmWhBT5oyktGhZjKvXSc4rq91qJ3xjVo9QnVFBrB6J4o9FSz-PLYfy_f7Uf8cmCe8a2Nrz0pqhuAMKIvjE1d63iyGjfBN88CtB64QSwOYriuujOOOxa6mBX-5qJzbldLaKZzsOfCssieLHiZXCpwEojYCrBxtSOi3fhg15UgLrml4i49UykQtIdKW395451s58kA4T8Awq_bJp-rbxkAZBzqLKikUk-GsDmdEQRVG8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یک مقام رسمی ایالات متحده در گفتگو با شبکه «فاکس‌نیوز» اعلام کرد که واشنگتن هنوز به توافق نهایی با تهران دست نیافته است و هیچ توافقی امروز یا فردا امضا نخواهد شد؛ این مقام مسئول با تاکید بر این‌که آمریکا تسلیم خواسته‌های طرف مقابل نخواهد شد، افزود که تمایل و تصمیم دونالد ترامپ، رئیس‌جمهوری آمریکا، این است که یک فرصت ۵ تا ۷ روزه دیگر به مذاکره‌کنندگان بدهد تا توافق را به مرحله نهایی برسانند.
بر اساس این گزارش، یک توافق چارچوبی با ایران تا روز یکشنبه تا ۹۵ درصد پیشرفت داشته است و اگرچه دو طرف بر سر کلیات مربوط به ذخایر هسته‌ای تهران و بازگشایی تنگه هرمز به توافق رسیده‌اند، اما چانه‌زنی مذاکره‌کنندگان بر سر جزئیات و «ادبیات دقیق» متن این تفاهم‌نامه همچنان ادامه دارد.
@
VahidOOnLine
تسنیم، خبرگزاری وابسته به سپاه پاسداران، روز یکشنبه به نقل از «یک مقام مطلع» گزارش داد: «هیچگونه خوش‌بینی به آمریکا ندارد و رد و بدل پیامها از طریق میانجی پاکستانی نیز دائماً با در نظر گرفتن بدبینی به دولت آمریکا صورت می‌گیرد».
تسنیم به نقل از این منبع در ادامه نوشت: «تا این لحظه تفاهم نهایی حاصل نشده و چالش در بعضی بندها ادامه دارد، اما حتی اگر تفاهم اولیه‌ای نیز صورت بگیرد، به معنای تغییر نگاه ایران به آمریکا و اطمینان از اجرای تعهدات این دولت نیست. آمریکایی‌ها سابقه بسیار بدی در مذاکرات دارند که بدبینی ها را تقویت و تثبیت می‌کند. پس حتی اگر تفاهمی نیز صورت بگیرد ایران در طول روند پس از اعلام تفاهم، اقدامات آمریکا را زیر نظر خواهد گرفت و در صورتی که آمریکا در آن مرحله نقض عهد کند، ایران اهرم‌های خود برای مواجهه با آن را حفظ خواهد کرد».
تسنیم پیش از این نیز از «کارشکنی‌های آمریکا» در بندهای تفاهم از جمله در آزادسازی اموال بلوکه شده ایران گزارش داده و نوشته بود: «همچنان امکان منتفی شدن تفاهم وجود دارد».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/75691" target="_blank">📅 00:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75690">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H_BvyH-hnp6-smd1vfBkxgldBcQkkeGQvXbbpLAdBR0M7hjOeaTQeJWh4kYSpDrwdjuwCQ-IVVpTDk2rgiRw_zS8cb_dh34uyuHS6fseTaKizwJVQ_01wb_g_BTaHKnT7nX1DIBJ63X6m0QHn27op3Lle25MFR6qZhdvfngQnlGfQyAD6P00nR45SSXD3FUfhLGUk6cc1c2voSkEgis61xo1v566AHB4hAB1kb6hzv6k7eOO_z_uTAzVLVRPsDHNSmMKk3zIrKdqgaBgMD0uP4KEJN_GqxWfthmxmUqpqS8UNDd2saDrEtKcxpDIGnweMI7Zgl_d302NSFlxOogfNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری حکومتی تسنیم، شامگاه یکشنبه سوم خرداد ماه، به نقل از دادگاه انقلاب تهران اعلام کرد، رای اولیه پرونده موسوم به «بچه‌های اکباتان» صادر شده و طی آن چهار نفر از «متهمان اصلی» به اتهام «افساد فی‌الارض» به اعدام محکوم شده‌اند.
به گزارش تسنیم،  اتهامات ۹ نفر از متهمان این پرونده که به دلیل کشته شدن «آرمان علی‌وردی» بسیجی حامی حکومت زندانی شده‌اند مواردی چون  «وارد کردن ضربات چاقو،اخلال در نظم عمومی، اخلال گسترده در امنیت کشور، اجتماع و تبانی برای ارتکاب جرم علیه امنیت داخلی کشور، توزیع کوکتل مولوتف، وارد کردن ضربات سنگ به آرمان علی وردی، ضرب و شتم آرمان علی‌وردی و فعالیت تبلیغی علیه نظام» عنوان شده است.
بر اساس این گزارش، دادگاه انقلاب تهران متهمان ردیف اول تا چهارم پرونده را به اتهام «افساد فی‌الارض» به اعدام محکوم کرد و متهمان ردیف پنجم تا نهم نیز به حبس از یک تا پنج سال و مجازات‌های تکمیلی محکوم شدند.
@
VahidOOnLine
شعبه ۱۵ دادگاه انقلاب تهران به ریاست قاضی ابوالقاسم صلواتی چهار تن از متهمان پرونده «شهرک اکباتان» را به اتهام «افسادفی‌الارض» به اعدام محکوم کرد؛ این در حالی است که دادگاه کیفری پیش‌تر اعلام کرده بود انتساب قتل به متهمان به‌صورت قطعی ثابت نشده و امکان صدور حکم قصاص وجود ندارد.
خبرگزاری میزان، وابسته به قوه قضاییه جمهوری اسلامی، روز یکشنبه در گزارشی تلاش کرد صدور این حکم را توجیه کند.
بر اساس این گزارش، رسیدگی به پرونده در دو مرجع موازی انجام شده؛ دادگاه کیفری به اتهام قتل رسیدگی کرد و دادگاه انقلاب به اتهامات امنیتی از جمله افساد فی‌الارض.
میزان مدعی شد که پس از آن‌که کمیسیون پزشکی قانونی و اداره آگاهی هر دو اعلام کردند تعیین فرد وارد کننده ضربه مرگبار به آرمان علی‌وردی ممکن نیست، دادگاه کیفری سه تن از متهمان را از اتهام مشارکت در قتل تبرئه و سه تن دیگر را به پرداخت دیه و حبس محکوم کرد. اما در مسیر موازی، دادگاه انقلاب همان متهمان را به اتهام افساد فی‌الارض به اعدام محکوم کرد.
به گزارش خبرگزاری هرانا، میلاد آرمون، نوید نجاران، مهدی ایمانی و سید محمدمهدی حسینی چهار نفری هستند که حکم اعدام برای آن‌ها صادر شده است.
چهار متهم دیگر این پرونده یعنی امیرمحمد خوش‌اقبال، علیرضا برمرزپورناک، علیرضا کفایی و حسین نعمتی نیز هر کدام به پنج سال زندان، دو سال حبس به اتهام تبلیغ علیه نظام، دو سال منع فعالیت در فضای مجازی و دو سال منع اسکان در تهران و البرز محکوم شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/75690" target="_blank">📅 00:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75689">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E1BrHbDJhL98S4eBEUsr6BuW5S5Z0IlebPLEjYLBrYfIpiRr8AkrnMKP2BH7zN7f7QTs5dLXJaBnZ0dcDIpGcH6LCj6JPscERjYt5IAv92_2UlV7lKAhzB9pXaoFb4-Z-KusjUmUHM5dVXm_SRFQBzimrf6lqFMoY3kfVb3d4foBuey0g-1uy5D3t92-tVXZu39KkUojy_MY42YDdC614pHa1n-7SNavLbeYWGchUZDWQlYKIXI5uJDAus-zPCihOlrOTbBaSU7tw7NJqLsDZW__iMhpSYi6DT5gkRPMjHXErpiG9cm0kqJxgA68DRAfd1OW5Epb_nUZM8eGHX5Ocg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ
روی تصویر بمب نوشته: از توجه شما به این موضوع سپاسگزارم.
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/75689" target="_blank">📅 23:16 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75688">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIVJqsTlyJJMDO6m_Z_CFmtNOpv6eXskA7Np_DIHTIQRheI_gdDjsVYaMODWvidLHNDFMnjKp1QRxFQEuc0eLJjo0vOVsq-me5oAfNYJq4eSlrScmV7MysRbhPc2VtUuIXtHDse81JrjZz40-QN4QyWavt7T3DAz_vq3tS8KZm_eL72xvoRw8Oq7-JiwrRxpy9-xJLWj8b326M0urqvcOorshZaA6lBXCC-u4Vx63ebADU67lpB64qT_CQ7ww9aJpXgwQnIRUKA_Zp1PMMs2PmGztzd5ILR7TwKLBPL1JolATNlAe1TvmzW-VY55wE2tEGpIMs-yEy2G-eAgW0xEQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، در گفت‌وگویی کوتاه با نیویورک تایمز گفت: «ما موضوع را به بعد موکول نمی‌کنیم. مذاکرات هسته‌ای مسائل بسیار فنی هستند. شما نمی‌توانید یک موضوع هسته‌ای را در ۷۲ ساعت و روی یک دستمال کاغذی حل کنید.»
او افزود: «در حال حاضر، هفت یا هشت کشور منطقه از این رویکرد حمایت می‌کنند و ما آماده‌ایم این مسیر را ادامه دهیم.»
این در حالی است که آقای روبیو ساعاتی پیش گفته بود که ممکن است تا شامگاه یک‌شنبه خبری دربارهٔ توافقی با ایران اعلام شود که می‌تواند به‌طور رسمی به جنگ خاورمیانه پایان دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/75688" target="_blank">📅 22:42 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75687">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dMbEVmaU2quLakRcqkQxHd3Y4cKLDieQBwtlibVfQ2kNFrMX3ki6Fb0DbTUZWpSTbinV6xwv4MP6VcYnI81mzrQqKQl8C4wEEzhLTIflCo1p0iLg1T1Jkagn1HKwWwzhqGV7BYETyNHgtGXs6-B3VqAINnYDt2Pdo-D7pu94Q0j5_dGuQ03130U6mm-TY974f4cmcrsZdafes_qDN93t7ZHBp4SpgRLqol88YKTPj0GtS_IFV0_BwQvbhQPqY6t_HoqKU7U-SgiNPBcD_E9xyCRFc20Y4tidj5Q_M7ngsgKDPULPNReUFp3b28SIsaLMtjnjN9Hni5u2P1qJOVtahA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اگر توافق کنم توافقی خوب خواهد بود
ترجمه ماشین:
اگر با ایران توافقی انجام بدهم، توافقی خوب و درست خواهد بود؛ نه مثل توافقی که اوباما انجام داد و مبالغ عظیمی پول نقد به ایران داد و مسیری روشن و باز به سوی سلاح هسته‌ای پیش پای ایران گذاشت.
توافق ما دقیقا برعکس آن است، اما هیچ‌کس آن را ندیده و نمی‌داند چیست.
حتی هنوز به‌طور کامل هم مذاکره و نهایی نشده است.
بنابراین به بازنده‌هایی که درباره چیزی انتقاد می‌کنند که هیچ اطلاعی از آن ندارند گوش نکنید.
برخلاف کسانی که پیش از من بودند و باید سال‌ها پیش این مشکل را حل می‌کردند، من توافق‌های بد انجام نمی‌دهم!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/75687" target="_blank">📅 22:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75686">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCfAO34r0ndj9KG2Yj5gasi9S5JyO_Zy-tS8-IhOwQi3J7iXwLn6S-b1xqZhL9kM9DDuevAAZlgmtIsYm0KwXjWecaX_daBct2CzP8hUAIPTnbozso15fnNzP9TyQuJvwao-PNL6Ri5YSGWOWvM1lNUqObUsDv8SOJmOB1_qa97ipqyg2b9u0LiOvOFeSVttZKvBhdvAuvnLSEv3w0z7NPIlapUp6bR73x-dFq2buW77rXDC7Vm_1gP23ERvT8EpfaiNJq0acgLdXZgUXWSW7BcfuxScT6kxMonwvvlFbZl8cySeXl-DtVBfv6y2KqYLkuIJL0diDVOeWYdbHqukcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه آکسیوس، روز یکشنبه سوم خرداد ماه، به نقل از یک مقام ارشد دولت دونالد ترامپ گزارش داد، «چند مورد جزئیات حل‌نشده» میان تهران و واشنگتن باقی‌مانده است و به همین دلیل توافق میان ایران و آمریکا احتمالا امروز امضا نخواهد شد.
این مقام آمریکایی به آکسیوس گفت هنوز بر سر برخی بخش‌های توافق «رفت‌وبرگشت» وجود دارد و اختلاف‌ها بیشتر بر سر عباراتی است که برای هر یک از دو طرف اهمیت دارد: «برخی کلمات برای ما مهم هستند و برخی کلمات برای آن‌ها.»
آکسیوس به نقل از این مقام ارشد کاخ سفید نوشت، ساختار تصمیم‌گیری در جمهوری اسلامی «سریع عمل نمی‌کند» و روند دریافت همه تاییدیه‌های لازم چند روز زمان خواهد برد.
به گفته این مقام، ارزیابی واشنگتن این است که «مجتبی خامنه‌ای»، رهبر جمهوری اسلامی، چارچوب کلی توافق را تایید کرده، اما اینکه این روند به توافق نهایی منجر شود، «همچنان یک سوال باز» است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/75686" target="_blank">📅 18:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75685">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_VN6xMwQ3xKJ3ZXkYLcJ8X11A-M27xeOODrBbfqqJ_yHhZqRDY9OgbPJMxWVc6UlF5xEZ2tytBiBq9Kr-gI5lpZ2eY1zG1USReGc95QARB3gcsFQtMD0f2KPhl-bdjONxMPCREXuRdV894l5MnFRDzLBt9ZHiaqCtINXeuiYuc2IFhP2vOpN7kEXaLLh48aXHalE4djvVa3IU5xkxjRsEumOGQ7pL27v0slZs9aALfti4KN1dHt4SuItP4SZCt0T1f0tF_yvfhjznVTA-disaixwXc4C3H7k4PiTW_XQoweyUHOMyq5B4n-aIygcmvNlBOiERumGA-yk6iY-5ORMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، اعلام کرد او و دونالد ترامپ توافق دارند هرگونه توافق نهایی با جمهوری اسلامی باید به‌طور کامل تهدید هسته‌ای را برطرف کند.
او گفت این به معنای برچیدن تاسیسات غنی‌سازی ایران و خارج کردن مواد هسته‌ای غنی‌شده از خاک این کشور است.
نتانیاهو افزود ترامپ بار دیگر بر حق اسرائیل برای دفاع از خود در برابر تهدیدها در همه جبهه‌ها، از جمله لبنان، تاکید کرده است.
او همچنین گفت سیاست او، همانند سیاست ترامپ، همچنان ثابت است؛ ایران نباید به سلاح هسته‌ای دست یابد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 243K · <a href="https://t.me/VahidOnline/75685" target="_blank">📅 18:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75684">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rd_OPV2XQH0dyRQ9RzwsbsrnBE3E9fYzwLk4NZLYQSX0R_i-RrW2Xt45vxXV6uVu-dLB8lPeYcAYdxnF79Rt15YZfL8N-55eWyWT5j0xxHxTeMkSGmfy6Bng-xzOtnJ8ad8nGafxEpiOyMzeJt47yecQj2F5-OJ_SIICWN5oiIMmT7IopfdYAkF487unnFrC78z4_2vsR3SMzbDyx8pej3zJyxuihiNRgjJz56b37SwoK94umqWG8RIzdN7eTn02ETXAGUMzjfqP0kRA1cXIrSSWll05NzRS8CvlOnkFDAGh41bZ3rdfYMC5W86SMqtM7YdAxramVi2hSMSUnb3D7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ سخنان پزشکیان را نشان داد: آماده‌ایم به جهان اطمینان بدهیم
ترامپ اسکرین‌شاتی از
توییت
خبرنگار فاکس‌نیوز رو پست کرده که نوشته بود:
مسعود پزشکیان، رئیس‌جمهور ایران: ما آماده‌ایم به جهان اطمینان بدهیم که به‌دنبال سلاح هسته‌ای نیستیم. ما به‌دنبال بی‌ثباتی در منطقه نیستیم.
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 235K · <a href="https://t.me/VahidOnline/75684" target="_blank">📅 18:56 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75683">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ANL56GYsd9u-74yeKrgCIYKRt5fJVsXcXV7ZhicHcCDaErgbp4LDFEAdIdZ3wqAilW5boh3HoprxJFV22cIHLP7zSHWlUQsIZ1886JStwtveo6uvvlEWHFzMVEQOGM9gI1hROcS24Wx_ljeVKa0rfmTEyGjt2EAiWuEKVYPsXXNsSwW5vj7M_R4NvD1GnVvbUn8ip2ff-QpGnmusQRBy5WTSGMBeTCN2oV_zF56hN_MqMBTAxyOkn0R4O_pnG_nEuHX0E8Wv16TVKrLlkwrH43Y-r00VCe0EU8cuYNI_RWVOWHKeDRmekMpHsiVk1IYC8w_ZJ45l6NCLaFSlFFPHig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
یکی از بدترین توافق‌هایی که کشور ما تاکنون انجام داده، توافق هسته‌ای ایران بود؛ توافقی که باراک حسین اوباما و افراد کاملاً ناشیِ دولت اوباما آن را مطرح کردند و به امضا رساندند. این توافق، مسیری مستقیم برای دستیابی ایران به سلاح هسته‌ای بود. اما درباره معامله‌ای که اکنون دولت ترامپ با ایران در حال مذاکره بر سر آن است، چنین نیست؛ در واقع کاملاً برعکس است!
مذاکرات به شکلی منظم و سازنده در حال پیشرفت است و من به نمایندگانم اطلاع داده‌ام که برای رسیدن به توافق عجله نکنند، زیرا زمان به سود ماست. محاصره تا زمانی که توافقی حاصل، تأیید و امضا شود، با تمام قدرت برقرار خواهد ماند. هر دو طرف باید وقت بگذارند و کار را درست انجام دهند. هیچ اشتباهی نباید رخ دهد!
رابطه ما با ایران در حال تبدیل شدن به رابطه‌ای بسیار حرفه‌ای‌تر و ثمربخش‌تر است. با این حال، آنها باید درک کنند که نمی‌توانند سلاح یا بمب هسته‌ای تولید یا تهیه کنند. مایلم تا این مرحله از همه کشورهای خاورمیانه بابت حمایت و همکاری‌شان تشکر کنم؛ حمایتی که با پیوستن آنها به کشورهای عضو توافق‌های تاریخی ابراهیم، بیش از پیش تقویت و گسترش خواهد یافت و چه کسی می‌داند، شاید جمهوری اسلامی ایران هم بخواهد به آن بپیوندد!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 227K · <a href="https://t.me/VahidOnline/75683" target="_blank">📅 18:17 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75682">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p6EdcNU3-A0XZzGrbFGx4OzyPyRGrt-Sgi1DBPKmivt8FlAQbcHm21fbuIsI0JJjlHz9lHVlBtY6nyMp9TkqGJX3SiM3B3YkHvcMMUA9jcs2IySET-Tp-h09e9lFKZEztkLCifvfNWTHhiLfrgLOyjqYNYBvUU5A8PEltdX_jTQvBGcg2qTfOwvvZ8FUzwTvs5ko6tDmxvxTaKQtpLEvpX1qCQKr-7b-hTXCNnjtSW_l_uvR4icftMjadUOwOIwIklBUTqJ-VMcKHBVg9oC-IvA05pKr-YVxfjOyPINWhWQeXnbWKKaGIn8Q7d8sNAxfZJgwv1kzSTObl8Gr7Tx7hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ تصویری ساخته با هوش مصنوعی را در شبکه اجتماعی تروث سوشال
منتشر کرد
که انهدام یک قایق سپاه پاسداران  به دست پهپاد آمریکایی را نشان می‌دهد.
بر این تصویر، واژه «حداحافظ» به زبان اسپانیایی نوشته شده است.
این تصویر در حالی توسط رئیس جمهوری آمریکا منتشر می‌شود که رسانه‌ها در انتظار نهایی شدن توافق احتمالی تهران و واشنگتن برای پایان جنگ هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 209K · <a href="https://t.me/VahidOnline/75682" target="_blank">📅 18:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75681">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMfMB9qTZWWw72ZhfOQAx36WMdQHlnkS-ZX85zQD5ZH_Ydtrt-xtHcmgLSKhGEge5fPK1PRHyj7WJeAjdj8z-EuOTQjbvdBhf-Hv43WS-pb-KXGm_Wgpdvzz3G6vS_uECk3opDloyNF-N_sYvuvM3zNOzNpFqJgZhaWuki17l2R7nSVKAJN1IQ6roNlNrOMq5_yxX468mgEWToyB4qmgOGTqTr8VKr4Aze9LaeYmem6lj6i4DY93-HpRq3m9ITV7N_v5wqeClx_mW30ODD9zb16gbTqY8mtE8TVhYExFkjzC_lgDpFJZl75aUid65oza5YoPDcQFZj-GqhC22_SclA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا عارف، معاون اول پزشکیان گفت: «مدیران دولت تا زمانی که مباحث کارشناسی درباره مدیریت مصرف بنزین نهایی نشده است، حق اظهارنظر شخصی ندارند.»
او افزود: «اگر کسی از این دستور تخطی کند با او برخورد می‌شود، زیرا ابتدا باید نظرات کارشناسی بررسی و سپس جمع‌بندی نهایی حاصل شود.»
او ادامه داد: «مسئولان تا پیش از آن حق ندارند اظهارنظر شخصی کنند، چرا که نباید در جامعه التهاب یا نگرانی ایجاد شود.»
@
VahidOOnLine
این دستور در شرایطی صادر شده که شایعات درباره افزایش قیمت بنزین، تغییر سهمیه‌ها و تشدید سیاست‌های مدیریت مصرف بالا گرفته است.
همزمان، ناترازی بنزین و فاصله میان مصرف داخلی و توان تأمین سوخت، نگرانی‌ها درباره کمبود احتمالی یا فشار بیشتر بر شبکه توزیع را افزایش داده است.
عارف گفت دولت تلاش می‌کند تصمیم‌ها به‌گونه‌ای اتخاذ شود که معیشت مردم آسیب نبیند، اما واقعیات اقتصادی کشور و تحولات اخیر نیز باید در نظر گرفته شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 193K · <a href="https://t.me/VahidOnline/75681" target="_blank">📅 18:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75679">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mmAKnj0KwnTZWR_GuBnhl13h0t-_SHor0iVvH5tqQZ0BeE8pGQ7yL77nW4OCBsNohcGC0QxarnqovZdlZrqx_IO07fH8atcQC5ZAi2SUB3PCc1jqs_QK0J0ZwIiQWhE59K5pi8_VQIDMYmRFdnfZgs-PaE62ac0rUUFrv7jihQumARjex-qMZeKv_Q9K1cva3oXTbhKSeiT-Db7Z5qq6TK6bq7-KkrY78Jh2ULhuv1DknlxMq_jWDOFCWy_CZTxArIj_EdeFOLruhawY0Emd4SRf57oh9qGHB8qxiVaoCUFPaVw0s-I5Z8GFzV2lmhxcXjQIoi6uYobEConzSHVS9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SDLCeO-cNAFMVRRlO0NZW06rHSFfdj4cdItKO8x1Owg9lnlVL5enF0iWJ3IeqWUaLwBhAg7k4Sy6DBTu80mGw9FPLQZZs_f4Hgxka9mpUfqzTKb7LHnu7qR5NjT94hLqZH3_5x1WMTJ1yFsAVTzRYBe8VFFDgaU7s4hSGIhZpWk0lQquh8lLa3-q0rGjdVFGLy3aYhXHd6SbV3YYTbHWVErDXIvXbbjYk6BH0GTanCMEA_ZoUTAEtz-d40rcbZwPHJ6CU8go6H0g4KwOxNCxIutN7rwFlTDxcvASBOededdRhUamYyWf8nfT9DUe3aYPO-3bk1EQHPPzhMWSeh8azQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری فارس، نزدیک به سپاه پاسداران روز یکشنبه سوم خرداد با اشاره به توافق احتمالی میان جمهوری اسلامی و آمریکا، نوشت:  در پیش‌نویس توافق احتمالی ایران و آمریکا هیچ بندی درباره «تعهدات هسته‌ای ایران گنجانده نشده و تمام مسائل مرتبط با برنامه هسته‌ای به مذاکرات ۶۰ روزه پس‌از امضای توافق موکول شده است.»
فارس در ادامه تاکید کرده است که «ایران در این توافق هیچ تعهدی برای واگذاری ذخایر هسته‌ای، خروج تجهیزات، تعطیلی تأسیسات یا حتی تعهد به نساختن بمب هسته‌ای وجود ندارد.»
این در حالیست که نیویورک تایمز به نقل از دو مقام آمریکایی گزارش داد، یکی از عناصر کلیدی توافق پیشنهادی میان واشنگتن و تهران، تعهد آشکار ایران به واگذاری ذخایر اورانیوم با غنی‌سازی بالای خود است.
@
VahidOOnLine
خبرگزاری تسنیم، وابسته به سپاه پاسداران، نوشت که شنیده‌ها از جزییات تفاهم اولیه «احتمالی»، حاکی است که واشینگتن متعهد خواهد شد در طول دوره مذاکرات، تحریم‌های نفتی ایران را به حالت اسقاط درآورد و جمهوری اسلامی در مقطع کنونی هیچ اقدامی را در حوزه هسته‌ای نپذیرفته است.
این گزارش افزود در صورتی که این تفاهم‌نامه مورد توافق قرار گیرد، بخشی از دارایی‌های بلوکه شده حکومت ایران باید در گام اول آزاد شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 185K · <a href="https://t.me/VahidOnline/75679" target="_blank">📅 18:11 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75676">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/arpQlgW2rVUuBR_MFPWeAdkyeJ3FpqphvUToYGjgATSb9Ddqao5RulVBhHwW7L9n78cZmDwb1pTdU4KfNkQSr7cz888wFMb_gxgA7HMDYytNahXij4MdQwHTNI8yx2VM-zp6YBOYFoI7QGjNbSo4aoj4YSzhxLyPLNq7qaQMtZsTeBxSsggBpZCdAEjCidX8fmsXT0W1UHXeCTqRpZ8wY_ehkQy5BbSuhvR-cix7tIfbKEJnoI6AReQlVxyu7PN4aPaqupfPyIgb7Mv9j5hawP8CG4B0PKU7RHrqJVXc5ndvo75jGDtcBw_AMtf9jO51xHRSmFd5QRDAE-XexlL-zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/af3f5ad4b2.mp4?token=BgQJqTOq19j9gh6e8-IVvTU6jL3nLIHDki-6giOxlSv2T386WX32ik35jDFB1ZzBlokDppzZn7pZzop2-40ADWid2bqn52fOvli9iBpdCyYFejDYVVMXYykkMDNGxSQ97Wn3rd0RMVK47XQzTOl8W78cZcnrBiPdSB17FKssnFug7r5tM7F5mh1yxaSB4hHAToKNJf84kEzGhWRAd_hngtK2Mz3ydE_pF9X6LRXjKgX9qbClQ4j05BXnYXqr3PoiT1Df5c00QoN4B0zN2dveH8-Y2vImN7JtGk7Z-WuhH655HDAkj12uY--cklDh2hASXS8m4hJ3Q8SJ6cnNChHeJA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/af3f5ad4b2.mp4?token=BgQJqTOq19j9gh6e8-IVvTU6jL3nLIHDki-6giOxlSv2T386WX32ik35jDFB1ZzBlokDppzZn7pZzop2-40ADWid2bqn52fOvli9iBpdCyYFejDYVVMXYykkMDNGxSQ97Wn3rd0RMVK47XQzTOl8W78cZcnrBiPdSB17FKssnFug7r5tM7F5mh1yxaSB4hHAToKNJf84kEzGhWRAd_hngtK2Mz3ydE_pF9X6LRXjKgX9qbClQ4j05BXnYXqr3PoiT1Df5c00QoN4B0zN2dveH8-Y2vImN7JtGk7Z-WuhH655HDAkj12uY--cklDh2hASXS8m4hJ3Q8SJ6cnNChHeJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، روز یکشنبه در جریان نشست خبری مشترک با سابرامانیام جایشانکار، وزیر خارجه هند، در دهلی‌نو اعلام کرد که طی ۴۸ ساعت گذشته «پیشرفت قابل‌توجهی» در مذاکرات و رایزنی‌های مرتبط با بحران تنگه هرمز و پرونده ایران حاصل شده و احتمال دارد تا ساعاتی دیگر اخبار مهم‌تری در این زمینه منتشر شود.
او بدون ارائه جزئیات کامل، گفت هنوز توافق نهایی شکل نگرفته اما مسیر مذاکرات نسبت به روزهای گذشته امیدوارکننده‌تر شده است.
روبیو با تاکید بر اینکه دولت آمریکا همچنان راه‌حل دیپلماتیک را ترجیح می‌دهد، اظهار داشت دونالد ترامپ تمایل دارد بحران ایران از طریق وزارت خارجه و مذاکره حل شود، نه از مسیر درگیری نظامی.
با این حال او هشدار داد که واشنگتن در هر شرایطی مانع دستیابی ایران به سلاح هسته‌ای خواهد شد و این موضوع «خط قرمز» دولت آمریکاست.
به گفته او، رئیس‌جمهوری آمریکا بارها تاکید کرده که ایران هرگز نباید به توانایی ساخت سلاح هسته‌ای برسد و دولت ترامپ در این زمینه از همه دولت‌های پیشین آمریکا سخت‌گیرتر عمل کرده است.
وزیر خارجه آمریکا در بخش دیگری از سخنانش به وضعیت تنگه هرمز پرداخت و گفت این آبراه، یک مسیر بین‌المللی است و هیچ کشوری حق ندارد عبور و مرور آزاد کشتی‌های تجاری را تهدید کند. او اقدامات اخیر ایران در قبال کشتی‌های عبوری را مغایر قوانین بین‌المللی دانست و هشدار داد اگر جامعه جهانی در برابر چنین اقداماتی سکوت کند، یک «وضعیت خطرناک و غیرقابل‌قبول» به رویه‌ای عادی در جهان تبدیل خواهد شد، موضوعی که می‌تواند در مناطق دیگر دنیا نیز تکرار شود.
روبیو همچنین اعلام کرد آمریکا طی دو روز گذشته همراه با شرکای خود در منطقه خلیج فارس روی چارچوبی کار کرده که هدف آن باز نگه داشتن کامل تنگه هرمز، جلوگیری از اخذ عوارض یا محدودیت برای عبور کشتی‌ها و همچنین رسیدگی به نگرانی‌های مرتبط با برنامه هسته‌ای ایران است.
او توضیح داد که در صورت موفقیت این روند، نه‌تنها امنیت کشتیرانی و تجارت جهانی حفظ خواهد شد، بلکه نگرانی‌ها درباره برنامه هسته‌ای ایران نیز تا حد زیادی کاهش پیدا می‌کند.
روبیو در ادامه گفت هرگونه توافق احتمالی نیازمند پذیرش کامل ایران و اجرای عملی تعهدات خواهد بود و مذاکرات درباره جزئیات فنی برنامه هسته‌ای، روندی پیچیده و زمان‌بر دارد.
او افزود هنوز نمی‌توان درباره موفقیت نهایی مذاکرات با قطعیت صحبت کرد، اما «نشانه‌هایی از پیشرفت واقعی» دیده می‌شود و ممکن است جهان در ساعات آینده خبرهای مثبتی درباره تنگه هرمز و روند مذاکرات دریافت کند.
@
VahidOOnLine
روبیو گفت: «هدف نهایی این است که ایران هرگز نتواند به سلاح هسته‌ای دست یابد. ایران هرگز نباید مالک سلاح هسته‌ای شود.»
او تاکید کرد دونالد ترامپ، رئیس‌جمهوری آمریکا، در این زمینه موضعی «کاملا روشن» داشته و گفته است ایران هرگز به سلاح هسته‌ای دست نخواهد یافت.
وزیر خارجه آمریکا افزود: «قطعا تا زمانی که دونالد ترامپ رئیس‌جمهور است، این اتفاق نخواهد افتاد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 187K · <a href="https://t.me/VahidOnline/75676" target="_blank">📅 18:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75675">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iMDWbW9T5p3JopoqjhOdTvWBs450Kc9DQ9Tm0ZvbNHBpJ5quttnZxzbqFYhqx66B5BUplHhAD62URp5oApmwhTt-l0kMP-MSf9R457Bh-VfpNPiMi89uw__F7UhMukvkwo46ujUUZCWBGbn46uVnZ2dKvhQKrW2gqXHVPFuhvjDa1ILk8XTpIRsp1v1GEAK0tHwxpUzWRmkrAfMYhW7d2UViRwpSHnKR06pNg3jWOvaSL8-GYSbyKImnDolUyFXij3oKePEoOkNKLG5xzI6_AFyZ80wwGQLms4Z-NB95RMTbRElBNnf92GIMy4AqNglKs9AnZMCyxh19Q4ScvLSQwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد سرافراز، رئیس پیشین سازمان صداوسیما و عضو کنونی شورای عالی فضای مجازی، می‌گوید بخشی از حاکمیت ایران با الهام از الگوی چین به‌دنبال محدود کردن اینترنت جهانی برای عموم مردم و ارائهٔ آن فقط به گروهی خاص و کنترل‌شده است.
او روز یک‌شنبه سوم خرداد در گفت‌وگو با روزنامه اینترنتی فراز گفت جمهوری اسلامی تجهیزات لازم برای «قطع دائمی اینترنت» را از چین خریداری و وارد کرده است.
محمد سرافراز توضیح داد که در چین اینترنت جهانی برای عموم مردم قطع است و فقط به‌صورت محدود در اختیار گروه‌هایی خاص قرار می‌گیرد. سرافراز با اشاره به الگویی که آن را «سامانه نیکان» در چین خواند، گفت هدف چنین سازوکاری این است که «روایت حکومت» بر کشور حاکم باشد.
او همچنین اپراتورهای عضو شورای عالی فضای مجازی را از عوامل پشت پردهٔ تصویب طرح موسوم به «اینترنت پرو» دانست و گفت ذی‌نفعان قطع اینترنت «یک روز فیلترشکن می‌فروشند و یک روز اینترنت پرو».
@
VahidHeadline
پس از ۲۰۴۰ ساعت قطعی اینترنت در ایران، نت‌بلاکس نوشت در حالی که دسترسی به اینترنت جهانی در طول مذاکرات صلح تا حد زیادی قطع است، کاربران منتخب در لیست سفید، تصویری مصنوعی از زندگی ایرانیان را به جهان خارج ارائه می‌دهند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 200K · <a href="https://t.me/VahidOnline/75675" target="_blank">📅 17:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75674">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9232e36d77.mp4?token=sjOp7Rpza9ZlTyEcDA3szizi46CP4ufFgqPsOB-d8w7w2yAm8tXtZeAnYYV61LEXAlX0H1bNlSseRpptlzKjBUzv71zceigGAIW4FZCFtl76gd_l5xo_ouwkb7wYH-IwZzD1DiFOnekqgOaUniskMLmRUW8Yq3UdZOjNOm9GEC7Kt-RDvFxAp726MCkHLq0nsIRbovv7Ec6tVhlNHqU6QwI-n41u3f-vUcXni5gyB4HXdPFOddij_DJb1kv2cHKB1NscYzwIn8ZvrSOZEFJ5OkJV5vWxQM3evZkIBxdfbabTaXT0slI6XyimMiUkmBUE0qcJbS51_T2MFTPa_VRcYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9232e36d77.mp4?token=sjOp7Rpza9ZlTyEcDA3szizi46CP4ufFgqPsOB-d8w7w2yAm8tXtZeAnYYV61LEXAlX0H1bNlSseRpptlzKjBUzv71zceigGAIW4FZCFtl76gd_l5xo_ouwkb7wYH-IwZzD1DiFOnekqgOaUniskMLmRUW8Yq3UdZOjNOm9GEC7Kt-RDvFxAp726MCkHLq0nsIRbovv7Ec6tVhlNHqU6QwI-n41u3f-vUcXni5gyB4HXdPFOddij_DJb1kv2cHKB1NscYzwIn8ZvrSOZEFJ5OkJV5vWxQM3evZkIBxdfbabTaXT0slI6XyimMiUkmBUE0qcJbS51_T2MFTPa_VRcYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجاری بزرگ در نزدیکی یک قطار که از گذرگاه چمن در شهر کویته در ایالت بلوچستان پاکستان عبور می‌کرد، تعداد زیادی کشته و ده‌ها نفر زخمی برجا گذاشت.
یک مقام ارشد پلیس بلوچستان و یکی از مسئولان این ایالت به محمد کاظم، خبرنگار بی‌بی‌سی اردو، گفت تاکنون کشته شدن ۲۰ نفر در این انفجار تأیید شده و دست‌کم ۷۰ نفر زخمی شده‌اند.
تصاویر منتشرشده پس از حادثه نشان می‌دهد که چندین خودرو در نزدیکی خط آهن آتش‌ گرفته‌اند و واگن‌های قطار نیز روی ریل واژگون شده‌اند.
گروه جدایی‌طلب «ارتش آزادیبخش بلوچ» مسئولیت این حمله را به عهده گرفته‌ است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/VahidOnline/75674" target="_blank">📅 17:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75673">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rbOM62YzjKrHcSKHe0ID63h0reK3j-1WeA8QvgZWVTuN3bTlQft80ShtZyiud3AhCWMo0DFFhiai5krnwbPU2PzPJ4jhJ2fqY9Dt9mRFgC9wmoHNecuMJnNkP8vq_eweKwwSQNgVBGgNnZHFeyMZV6XOftNRqmy3cMrdI_43bT-C3FQ9OuVqSYk9kQniG7ctdWkbGsIHDMVqboxjWpRw80Nd49dFFifC-3QKlGnG9EcqjRbyvYpng63c5KlYaSBS9KYmtMW2bUdjeullWCNg1Qtc1Yw2u38Rfwn5hTkW3Bvaw78ndRQJZifGodyAAsthwMuU7hLDL7KcZRVUPS1Pvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان، وابسته به قوه قضائیه جمهوری اسلامی، اعلام کرد مجتبی کیان به اتهام ارسال اطلاعات مراکز تولید صنایع دفاعی به «دشمن آمریکایی ـ صهیونیستی» اعدام شده است.
قوه قضائیه مدعی شده کیان در جریان آنچه مقام‌های جمهوری اسلامی «جنگ رمضان» می‌نامند، اطلاعات و مختصات واحدهای مرتبط با تولید قطعات صنایع دفاعی را از طریق پیام به شبکه‌های وابسته به اسرائیل و آمریکا ارسال کرده بود.
میزان مدعی شده بررسی‌های فنی نشان داده سه روز پس از ارسال این اطلاعات، محل مورد اشاره هدف حمله قرار گرفته و به‌طور کامل تخریب شده است. قوه قضائیه گفته پرونده این متهم در دادگستری استان البرز رسیدگی شد و حکم او پس از تأیید دیوان عالی کشور اجرا شد.
بر اساس رأی دادگاه، مجتبی کیان به اعدام و مصادره کلیه اموال محکوم شده بود. میزان همچنین نوشت از زمان بازداشت تا اجرای حکم کمتر از ۵۰ روز زمان گذشته است؛ موضوعی که پرسش‌های جدی درباره سرعت رسیدگی، امکان دفاع مؤثر و فرصت اعتراض در پرونده‌ای با مجازات اعدام ایجاد می‌کند.
قوه قضائیه گفته دادگاه با حضور وکیل برگزار شده، اما روشن نیست این وکیل منتخب متهم بوده یا تسخیری، از چه زمانی به پرونده دسترسی داشته، آیا امکان ملاقات محرمانه و آماده‌سازی دفاع فراهم بوده و آیا متهم فرصت کافی برای اعتراض به ادله فنی، درخواست کارشناسی مستقل و پیگیری مؤثر در دیوان عالی کشور داشته است یا نه.
این پرونده در بستر موج گسترده‌تری از اعدام‌ها، احکام امنیتی، مصادره اموال و رسیدگی‌های شتاب‌زده پس از جنگ قرار می‌گیرد؛ روندی که منتقدان و سازمان‌های حقوق بشری آن را نشانه استفاده فزاینده جمهوری اسلامی از مجازات اعدام برای ایجاد بازدارندگی سیاسی و امنیتی می‌دانند.
@
VahidHeadline
خبرگزاری میزان هیچ اطلاعاتی درباره حرفه این فرد نداده و مشخص نیست که مجتبی کیان چگونه به «اطلاعات صنایع دفاعی» دسترسی داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/75673" target="_blank">📅 17:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75672">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OMylofEs-_iCy034P1Kb353T_N-sb-0u9pOEFbI9KpDOnjURFa0e54vzIr9NGdGID-Pq-8Gr4UQ_MOMCHwleVRgLSzu9rYXj32lAJ-rGOJa-6NYKty29e6Z-O1dTfbeNfnqQAMoyehn99Q_aDtCtWShEOmNEBA1HVk9mJbvzbMhIuWLKGoKaIPw7mIiCjtnIwKDHinIcz45txHQhAuJHz4qh7EbTB6mjfRZc4Rkpl3WoB4RSNFtgiQou7cUC-dpvt4mfu5UbxA0VZQSBZBPUkIGnsnkKFNfLJtuYZGrx7jjq7POpM2daWupKdWXdLKmHwFX-MtgIevJVHMyrfVUk9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آکسیوس: جزئیات توافقی که ترامپ در آستانه امضای آن با ایران است
ترجمه ماشین:
توافقی که آمریکا و ایران در آستانه امضای آن هستند، شامل تمدید ۶۰ روزه آتش‌بس است؛ دوره‌ای که طی آن تنگه هرمز دوباره باز خواهد شد، ایران می‌تواند نفت خود را آزادانه بفروشد و مذاکراتی برای محدود کردن برنامه هسته‌ای ایران برگزار خواهد شد؛ این را یک مقام آمریکایی گفته است.
🔻
چرا مهم است: این توافق از تشدید جنگ جلوگیری می‌کند و فشار بر عرضه جهانی نفت را کاهش می‌دهد. با این حال روشن نیست که آیا به یک توافق صلح پایدار منجر خواهد شد یا نه؛ توافقی که هم‌زمان خواسته‌های هسته‌ای رئیس‌جمهور ترامپ را نیز پوشش دهد.
▪️
وضعیت فعلی: هم ترامپ و هم میانجی‌ها گفته‌اند ممکن است این توافق روز یکشنبه اعلام شود، هرچند هنوز نهایی نشده و همچنان ممکن است از هم بپاشد.
▪️
این مقام آمریکایی طرح کلی مفصلی از پیش‌نویس فعلی ارائه کرده که بخش عمده آن را منابع دیگر نزدیک به مذاکرات نیز تأیید کرده‌اند.
🔻
چه چیزهایی در توافق آمده است؟
دو طرف یک یادداشت تفاهم امضا خواهند کرد که ۶۰ روز اعتبار دارد و با رضایت متقابل قابل تمدید است.
▪️
در این دوره ۶۰ روزه، تنگه هرمز بدون عوارض باز خواهد بود و ایران موافقت می‌کند مین‌هایی را که در این تنگه کار گذاشته پاکسازی کند تا کشتی‌ها آزادانه عبور کنند.
▪️
در مقابل، آمریکا محاصره بنادر ایران را لغو می‌کند و برخی معافیت‌های تحریمی صادر خواهد کرد تا ایران بتواند نفت خود را آزادانه بفروشد.
▪️
این مقام آمریکایی اذعان کرد که این موضوع به سود اقتصاد ایران خواهد بود اما گفت در عین حال کمک قابل توجهی برای بازار جهانی نفت خواهد بود.
🔻
این مقام آمریکایی گفت هرچه ایرانی‌ها سریع‌تر مین‌ها را پاکسازی کنند و اجازه دهند کشتیرانی از سر گرفته شود، محاصره هم سریع‌تر لغو خواهد شد.
▪️
اصل کلیدی ترامپ در این توافق «امتیازدهی در برابر عملکرد» است.
▪️
طبق گفته این مقام، ایران خواستار آزادسازی فوری منابع مالی مسدودشده و لغو دائمی تحریم‌ها بود، اما طرف آمریکایی گفت این موارد فقط پس از ارائه امتیازهای ملموس اجرا خواهد شد.
🔻
مسائل هسته‌ای هنوز باید مذاکره شوند
▪️
به گفته مقام آمریکایی، پیش‌نویس یادداشت تفاهم شامل تعهد ایران به این است که هرگز به دنبال سلاح هسته‌ای نرود و درباره تعلیق برنامه غنی‌سازی اورانیوم و خارج کردن ذخایر اورانیوم با غنای بالای خود مذاکره کند.
▪️
به گفته دو منبع مطلع، ایران از طریق میانجی‌ها تعهدات شفاهی درباره دامنه امتیازهایی که حاضر است در زمینه تعلیق غنی‌سازی و واگذاری مواد هسته‌ای بدهد، به آمریکا ارائه کرده است.
▪️
آمریکا موافقت خواهد کرد که در دوره ۶۰ روزه درباره لغو تحریم‌ها و آزادسازی منابع مالی ایران مذاکره کند؛ هرچند این اقدامات فقط در چارچوب توافق نهایی و پس از اجرای قابل راستی‌آزمایی آن عملی خواهند شد.
▪️
نیروهای آمریکایی که در ماه‌های اخیر در منطقه مستقر شده‌اند، در دوره ۶۰ روزه در منطقه باقی خواهند ماند و فقط در صورتی خارج می‌شوند که توافق نهایی حاصل شود.
🔻
نکته قابل توجه: پیش‌نویس یادداشت تفاهم همچنین تصریح می‌کند که جنگ میان اسرائیل و حزب‌الله در لبنان پایان خواهد یافت.
▪️
یک مقام اسرائیلی گفت بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در تماس تلفنی روز شنبه با ترامپ درباره این شرط ابراز نگرانی کرد. او همچنین درباره جنبه‌های دیگر توافق نیز نگرانی‌هایی مطرح کرد، اما به گفته یک مقام آمریکایی، دیدگاه خود را با احترام و لحنی محتاطانه بیان کرد.
▪️
مقام آمریکایی گفت این یک «آتش‌بس یک‌طرفه» نخواهد بود و اگر حزب‌الله برای مسلح شدن دوباره یا تحریک حملات تلاش کند، اسرائیل اجازه خواهد داشت برای جلوگیری از آن اقدام کند.
...
🔻
چه باید دید: به گفته مقام آمریکایی، کاخ سفید امیدوار است اختلافات نهایی در ساعات آینده حل‌وفصل شود و توافق روز یکشنبه اعلام شود.
▪️
این مقام گفت ممکن است توافق حتی کل ۶۰ روز هم دوام نیاورد، اگر آمریکا به این نتیجه برسد که ایران درباره مذاکرات هسته‌ای جدی نیست. از سوی دیگر، آمریکا معتقد است فشار اقتصادی بر ایران انگیزه‌ای برای رسیدن به توافق کامل به‌منظور رفع تحریم‌ها و آزادسازی منابع مالی این کشور ایجاد می‌کند.
▪️
این مقام آمریکایی گفت: «دیدنی خواهد بود که ایران واقعا تا کجا حاضر است پیش برود؛ اما اگر آن‌ها توانایی و تمایل تغییر مسیر خود را داشته باشند، این مرحله بعدی آن‌ها را وادار خواهد کرد تصمیم‌های حیاتی درباره این بگیرند که می‌خواهند چه نوع کشوری باشند.»
▪️
مشاوران ترامپ می‌گویند اگر خواسته‌های او درباره برنامه هسته‌ای ایران برآورده شود، رئیس‌جمهور آماده است برای بازتنظیم روابط با ایران و دادن فرصت به این کشور برای دنبال کردن ظرفیت کامل اقتصادی‌اش، که به نظر ترامپ «عظیم» است، اقدامات بسیار گسترده‌ای انجام دهد.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/75672" target="_blank">📅 07:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75670">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t-namSS3CYuSx8Iv185H6hEMH2y654bSIhlHodgTrFhhuxvI2hJ6dT_R7wYPqlUxKeh19AssysH3zvmknabMIi4nVLbUq-tI0Tkdb9vbiWTUjqR9M_nGvJV4tL9AzKC6GoGz3AKpMQN7QQPAq41UzBPz07G8dO3GFRILwGxWnsacWaIEle-ew7QJcjTjbFQMUpYcQFpJdWyjZgizlxZsTL3LpDZPX0d7pPQSo_Uu4tAbfrS3AZUgiX2okDdL6lDaXC7RmqoYb1SBoTbS8GEhe92aj30RYV-eFmiaok3qUqOB8bWmGzzQ3gCKcxp6DezdKklYYd98OqdyXoUVsHtjuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H6KlhZtW1rs6JiRPe90WreoKyiqvPbN7SoscmqKpxFqqPRLDTJvHTiT8x-LBo3bC_twnxDA9OOr4gXfNnSo_XVDtEeSQeu9d6CCQmBuIXxJnXQTPWUzJ4PmcttqlJUMCF25qjO-IWGJ1bMv1xyw66Q2l52wJSBPvLHbhnunKKx4VtM7kz3qbEqB1HEByoJ3VLeW0XZvw7Khie-rmcOdXBQAPc3WvJWQUycGxpFt3zhcdv0w53tCQljvf_K2Lnrs9TUXjwwRBbtjEDCDQHMhREIKXFIA7u58yO1vpr64nzcD6WPaHr6PewFJ79vXjlUudCAMHhg88SEWTyMcHrFqr8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسماعیل بقائی، سخنگوی وزارت امور خارجه، در پیامی در شبکه اجتماعی ایکس با درج تصویر سنگ‌نگاره پیروزی شاپور اول ساسانی بر امپراتور روم، نوشت: «وقتی ایرانیان مهاجمان متوهم را ناکام گذاشتند.»
او در این پیام که کنایه‌ای است به محاصره دریایی بنادر ایران توسط آمریکا نوشت: «رومیان تصور می‌کردند که رم مرکز عالم است؛ اما ایرانیان این توهم را در هم شکستند.»
پیام آقای بقایی که به نحو گسترده‌ای در کانال‌های تلگرامی رسانه‌های حکومتی ایران بازنشر شده است به نظر می‌رسد که با استفاده از سنگ‌نگاره پیروزی شاپور بر امپراتوران روم در نقش رستم استان فارس بازنقش شده است.
آقای بقایی که اخیرا با حکم محمدباقر قالیباف به عنوان سخنگوی هیئت مذاکره‌کننده ایران هم منصوب شده است با اشاره به لشگرکشی مارکوس یولیوس فیلیپوس معروف به فیلیپ عرب، امپراتور روم، علیه امپراتوری ساسانیان، نوشت که لشگرکشی او «منجر به پیروزی رومیان نشد بلکه به صلحی با شروط شاپور اول ختم شد؛ امپراتور ناچار شد با واقعیت کنار بیاید.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/75670" target="_blank">📅 06:22 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75669">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UF3z5SMXV7IZr_FB8AA2ZaGW4fllp3Lz4NFuJ4D_hK9-EoyHAgFs8nLSwiCO6os1oOI4KMaN9Pr9YHze7hUclUhMz--5jcDHOArgRZGSurz7U6T0LhF9GlLHql0tpeHOp-SfUIyEMRY_0WCIU0HwWyM6LV5YPPajaZR1JlwU4ziwQkA0_C2pAZajrr-9aFqcy81MY-9pHeWOZzVkPmgZi52G6hCi93KRnRQdcMP9piiHNNMJY3vpksZWZq0Yqd24SjbReQ4pd7qAFRezEIBtJ-v2TKEGPUrlG5QgWdNNmFEbfwxoKjHX263JBqr6H5fbHJTst-1RJGpG4TmtIQ_-mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز به نقل از دو مقام آمریکایی گزارش داد، یکی از عناصر کلیدی توافق پیشنهادی میان واشنگتن و تهران، تعهد آشکار ایران به واگذاری ذخایر اورانیوم با غنی‌سازی بالای خود است؛
مقامات آمریکایی تصریح کردند که این پیشنهاد هنوز جزئیات دقیق نحوه واگذاری این ذخایر را تعیین نکرده و حل این مسئله را به دور بعدی گفتگوها درباره برنامه هسته‌ای ایران موکول کرده است، اما یک بیانیه کلی که ایران را متعهد به این کار کند، که هدف دیرینه ایالات متحده بوده، برای توافق بسیار حیاتی است، به‌ویژه اگر این توافق کلی با بدبینی جمهوری‌خواهان در کنگره مواجه شود. تا این لحظه، ایران هیچ بیانیه‌ عمومی درباره توافقی که ترامپ اعلام کرده، صادر نکرده است.
تهران در ابتدا با گنجاندن هرگونه توافقی درباره ذخایر اورانیوم غنی‌شده خود در این مرحله اولیه مخالفت کرده و خواستار موکول شدن آن به مرحله دوم گفتگوها بود، اما مذاکره‌کنندگان آمریکایی از طریق واسطه‌ها به صراحت اعلام کردند که بدون دستیابی به توافقی بر سر این ذخایر در فاز اولیه، میز مذاکره را ترک کرده و کارزار نظامی خود را از سر خواهند گرفت.
براساس این گزارش، بخش دیگری از این توافق محتمل شامل آزادسازی میلیاردها دلار از دارایی‌های بلوکه‌شده ایران در خارج از کشور است؛ اما به گفته مقامات آمریکایی، ایران تنها زمانی به بخش عمده این دارایی‌ها که قرار است توسط ایالات متحده و متحدانش در یک صندوق بازسازی قرار گیرد دسترسی پیدا خواهد کرد که با یک توافق هسته‌ای نهایی موافقت کند؛ امری که انگیزه‌ای برای تهران ایجاد می‌کند تا پای میز مذاکره بماند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 253K · <a href="https://t.me/VahidOnline/75669" target="_blank">📅 05:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75668">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tGzmT33m1nGreUyHvw6QhtFljFAIaot3TTc52CyfjmZaIJPQBE2yMVN4do3uAe8tbMtoiJ5xsHpuxetgSQY30c6AtLHE-Vmun-XNTwLTK7Tcz-i8POXrPp6GVE1Tk43RgVxrlUpjqeJDq5yhnyWvfEaVR2T1t7VstNFEtGxyqgV4AxHaxRKOyKmwj9fmRaQyEqWeyA3LVFYqnwlUsRcYPe5Rik1dJuKNXRIuN7KBkE8ig8kxJgmbXfyHBmSOKqtH_0OXDtt9MQx0EVBE-fbp-BT0UOScNwJP-k3OjWRgTSjqgzeAEIDov9WCFD85uXF_ivbMOwvFjZgW3909AXv_sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهباز شریف، نخست‌وزیر پاکستان، ابراز امیدواری کرد پاکستان به‌زودی میزبان دور بعدی گفت‌وگوهای تهران و واشینگتن باشد.
CMShehbaz
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 226K · <a href="https://t.me/VahidOnline/75668" target="_blank">📅 05:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75666">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PyG3ZR831CK7Jooj6zB7zb5hTwcdvVSlHzJqy6fh7HDnIKFxTuP2JUZPlt_4kv6NcN_AEKrMnP_zMcMtID1diYz26d1PDMXnpxq5ll2P36guJJQqs7YsKqk0YSEOkPjbxrMEiF9dIW-R4E9UG1_SaBmcyscCdtDOPEHm9pO5Ok5IQ0QWYP5UvaAqgYsKmsJf44R69o09-5AqkMABLPqX3VAI6UJftoa9muMkHsQiaHlWIE0uWSK_fp4RYyh7sAftHMYOI-T_t3jh8s9PdKsaV3rX4JysGNzwG7jbybycavFPWNBTk3ihTpUCeyh3ob0-NrMTgMY2Gv9PLxrQSUV-CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/U2ABSrxqsg1Dqov68myaN8dDS5gXuFtZMbyW5qo5QaXiRYxmUsKtICuYqjn3N1_vf1joh7NDAKCDgLow_KejFEvBHWXTc_D67eeV41qXSi9eyNnmcJWTIlE8nu8fqGw95seXwRvpfzDil5tuGgPB1jhbKKuE8jJzqka1IJptwxHXWwCGi145boYZHxs83mMyeMs0jK-BRK0I_6dmR0hpxgozv65UNeEPEwgQ0OQ9t1izO1A3RRZV7TGI8ylsfHS-K36NZpbe5qfdBHl27-ZiQRRiZy-nhOurzdjtgCLphJ6Ji-4txCxMGx-ow8ZwZ_jEZQ84T_wgscwsiYWKmh4TLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">توییت‌های تد کروز و لیندسی گراهام در واکنش به اخبار منتشر شده درباره توافق احتمالی
tedcruz
,
LindseyGrahamSC
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 219K · <a href="https://t.me/VahidOnline/75666" target="_blank">📅 04:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75665">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7119557db8.mp4?token=pcv3Gwh-VCG6nVOmLlI7liMbRpS9bnak2SDuU06pjmKRNo7yBRliUXnlqpiVZaFGPdL2Mg0KJQYInRFmc54sI6x0mp8i73rrsiLCprDZA5YVgNZJaeVkIexbWwiVPwwnIjm7RKP8-caDvgcWtNkLLsp3KLzNY3aF7alKICAI82wPvOFXV2emFvIr0UGTmbG6MMcjWHcS_j4467Hjc_YDeNaHDOcY_XBhq52Q_glzbsii5ZqKLr6SxYiSXHJlEDeUoWa04xYywhbRySanUGD3Vm8TT9jyDU7GIGUTcvYruY2nw1ZbywNSeU_DIX7sY59w_vsDgzN79K7flotAS3cPqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7119557db8.mp4?token=pcv3Gwh-VCG6nVOmLlI7liMbRpS9bnak2SDuU06pjmKRNo7yBRliUXnlqpiVZaFGPdL2Mg0KJQYInRFmc54sI6x0mp8i73rrsiLCprDZA5YVgNZJaeVkIexbWwiVPwwnIjm7RKP8-caDvgcWtNkLLsp3KLzNY3aF7alKICAI82wPvOFXV2emFvIr0UGTmbG6MMcjWHcS_j4467Hjc_YDeNaHDOcY_XBhq52Q_glzbsii5ZqKLr6SxYiSXHJlEDeUoWa04xYywhbRySanUGD3Vm8TT9jyDU7GIGUTcvYruY2nw1ZbywNSeU_DIX7sY59w_vsDgzN79K7flotAS3cPqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شنبه عصر، یک تیراندازی در حوالی کاخ سفید خبر روی داد که طی آن دو نفر از جمله یک عابر و فرد مظنون تیر خوردند.
سرویس مخفی ایالات متحده، در گزارشی اعلام کرد که اندکی پس از ساعت ۶ عصر روز شنبه، فردی در محدوده خیابان ۱۷ و خیابان پنسیلوانیا، (شمال غربی) سلاحی را از کیف خود خارج کرد و شروع به تیراندازی کرد.
سرویس مخفی ایالات متحده افزود پلیس سرویس مخفی به تیرانازی او پاسخ داد و به مظنون شلیک کرد.
به گفته سرویس مخفی،‌مظنون به یک بیمارستان محلی منتقل شد، اما در آنجا اعلام شد که جان باخته است.
به گفته این نهاد امنیی، در جریان این تیراندازی، یک عابر نیز مورد اصابت گلوله قرار گرفت و هیچ‌یک از مأموران آسیب ندیدند.
سرویس مخفی که وظیفه حفاظت از رئیس‌جمهوری آمریکا را دارد افزود دونالد ترامپ، رئیس‌جمهوری آمریکا، در زمان حادثه در کاخ سفید حضور داشت.
@
VahidHeadline
آپدیت:
رسانه‌های آمریکایی هویت عامل تیراندازی عصر شنبه در مجاورت کاخ سفید را «نصیر بست»، جوان ۲۱ ساله اهل مریلند، معرفی کردند که به عنوان فردی با اختلالات روانی و عاطفی شدید برای ماموران امنیتی شناخته‌شده بوده است.
بر اساس گزارش‌ها، این فرد که پیش از این در ژوئن ۲۰۲۵ با ادعای این‌که «خدا» است یک مسیر ورودی کاخ سفید را مسدود کرده و پس از آن به یک مرکز روان‌پزشکی منتقل شده بود، به دلیل تلاش مجدد برای ورود به حریم کاخ سفید در ژوئیه همان سال، حکم دادگاه مبنی بر «ممنوعیت ورود و نزدیکی به این عمارت» را داشته است.
گزارش‌های تکمیلی نشان می‌دهد که «نصیر بست» دست‌کم در یک پست رسانه‌های اجتماعی تمایل خود را برای آسیب رساندن به دونالد ترامپ ابراز کرده بود؛ او سرانجام پس از نقض حکم دادگاه، نزدیک شدن به ایست بازرسی خیابان هفدهم و پنسیلوانیا و گشودن آتش به سمت ماموران، در تبادل آتش متقابل با نیروهای سرویس مخفی هدف قرار گرفت و در بیمارستان جان باخت.
📷
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/75665" target="_blank">📅 04:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75664">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwyI480BN4PDFSLI7HwXVSKdG8sotDOFl7-Ayg58XiksfrqvkPh2FLHxzrLLwRqgt-GKOID_nPlo6aSX9nW7FEAyYhFsyJl6VEgIdMI-EUDWNzSpLy9m15vn3GjoVCwX6XveMWjw4U0X1oIxLA1wogtgV1nRdXKsiftmUg0gQiof43-Yl87tHru-rotweJRXSnLCK2m-XjQNPDR_OB16ZxCfsIXR8eybQ_m2XL1zuBIsZ6cW6h_0CyxQ_Fne9nxnFm7FigDV2W6chKmO94WcCemMqTgUxpmmCQvX25nib4gGKF1tnBAmVeAf2n9YgRRoPg9bcYhP-T6fIyIFby0j_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس، خبرگزاری وابسته به سپاه، در واکنش به پیام دونالد ترامپ، رئیس‌جمهوری آمریکا مبنی بر نزدیک شدن به توافق با ایران و بازگشایی تنگه هرمز نوشت: «این ادعا نیز با واقعیت‌ها فاصله دارد».
فارس در ادامه نوشت: «برخلاف ادعای لحظات قبل دونالد ترامپ در شبکه اجتماعی تروث سوشال مبنی بر بازگشت تنگه هرمز به وضعیت پیشین و آماده‌سازی برای امضای توافق‌نامه، پیگیری‌های خبرنگار فارس نشان می‌دهد که این ادعا نیز با واقعیت‌ها فاصله دارد؛ چرا که بر اساس آخرین متن ردوبدل‌شده، در صورت توافق احتمالی، تنگه هرمز کماکان تحت مدیریت ایران خواهد بود و اگرچه ایران موافقت کرده اجازه دهد تعداد کشتی‌های عبوری به میزان قبل از جنگ بازگردد، اما این به‌هیچ‌عنوان به معنای تردد آزاد به وضعیت قبل از جنگ نیست و مدیریت تنگه، تعیین مسیر، زمان، نحوه عبور و صدور مجوز، کماکان در انحصار و با تدبیر جمهوری اسلامی ایران خواهد بود.»
خبرگزاری سپاه در ادامه مدعی شد که برخلاف شروط پیشین ترامپ مبنی بر گنجاندن برنامه هسته‌ای در توافق، «هیچ تعهدی از سوی ایران داده نشده و پرونده هسته‌ای اساسا در این مرحله مورد بحث قرار نگرفته است.»
فارس همچنین ادعا کرد که «مقامات آمریکایی در پیغام‌های متعدد به ایران اذعان داشته‌اند که توییت‌های ترامپ عمدتا جنبه تبلیغاتی و مصرف رسانه‌ای در داخل آمریکا دارد و توصیه کرده‌اند که به این اظهارات توجهی نشود».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/75664" target="_blank">📅 01:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75663">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZrJVhjW0PaC6SKJLNY52JtNK0LPJbq8I94Ar5dQBwhpqfM_hnnLtKJriMsunqvCbip1Hy4WQaZFwkBgjWuoRcdYru-O7uc84cH5d8DTrsOaf01nMJD0cwkIlFqnXgu4n8V8QC5m5Z2DEgCXmzqOxc36HY3kTPiCfvM5DW7mdFgonU5XzUwWyhTYIdq0EAheOuo3IGzw8hSadeDSPLlTh7c6h2ixee8tsl4Dyjwc1QQET6ZDuAkE0RLyVphb_A41dwdB_n3ved-3IF-7K6hwM5h0gB_2XFKaKIl0zGgU4KaV2hz0wY-6_meR2141SIiwzqJsP7WL1tESuUxNOymfj7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار الجزیره به نقل از «منابع خود»، مفاد کلیدی پیش‌نویس توافقی را که قرار است میان واشنگتن و تهران نهایی شود را اعلام کرد.
خبرنگار الجزیره مدعی شد، توافق پیشنهادی شامل «پایان جنگ در تمامی جبهه‌ها از جمله لبنان»، «آزادسازی چندین میلیارد دلار از دارایی‌های مسدودشده ایران»، «رفع محاصره دریایی آمریکا و بازگشایی تنگه هرمز» و همچنین «عقب‌نشینی نیروهای آمریکایی از مجاورت مرزهای ایران» است.
پس از اجرای این گام‌ها، طرفین یک مهلت ۳۰ روزه، که با توافق دوطرفه قابل تمدید است، خواهند داشت تا درباره مسئله هسته‌ای به توافق برسند که در طول این مدت نیز تردد از تنگه هرمز تسهیل خواهد شد.
به گفته این خبرنگار، از نظر ایران، مدیریت تنگه هرمز یک موضوع دوجانبه میان تهران و مسقط تلقی می‌شود و گفتگوها در این زمینه با عمان در جریان است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/75663" target="_blank">📅 01:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75662">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nC883TZGxgGg67CYGSkz9U6RwmLmajIRiWED0dDY4PcrF9Vf_qirugQNVqQbFZR0lMJHDClmHWY21IzHSAXUZZ5dMjKdPpLPxcMBGx_JGnXEh2zfBXQiBF0xnJ4EU1KTE2EmztgMwfdwYb8coWaxST8_LSgZBiIA1J81OfcGAzdWxWqMyu8_HniujTaHN8S4XqtqkezCgCmYMDD0E_rmsYhEmN-7owcTKVVSPOb4Qw1qkmzAgMgK2W_ujMqMHgM7RKha0L3jdwlrd5JYNLjJ1oIQ9vxiUV6uC6gmavrznRZ4SX-PEt9FNDaQdWWwZsQcdNLv9nRusrthjt-VDjlVvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«یک منبع ارشد منطقه‌ای» از جزییات گفتگوی رهبران کشورهای عربی و مسلمان با دونالد ترامپ خبر داد.
خبرنگار آکسیوس نوشت: «یک منبع ارشد منطقه‌ای به من گفت که تمامی رهبران عرب و مسلمان حاضر در گفتگوی روز شنبه با ترامپ، از او خواسته‌اند تا برای پایان دادن به جنگ و مهار تنش‌ها در منطقه، توافق را پیش ببرد.»
این منبع تاکید کرده است که «پیام همه این بود: لطفا به خاطر کل منطقه، جنگ را متوقف کنید.»
به گفته این منبع، مذاکرات به خوبی در حال پیشرفت است و میانجی‌ها امیدوارند روز یکشنبه یک توافق چارچوب یک‌صفحه‌ای را منعقد و بلافاصله آن را اعلام کنند و پس از آن، قصد دارند ظرف چند روز مذاکرات را برای دستیابی به یک توافق دقیق و پرجزئیات آغاز کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/75662" target="_blank">📅 00:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75660">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hFvbasmgfTPq1Wb4zm3bhePKXdvVP3DpFSob3XenknzK3ro4w_WO8lXNrJrE8n1urlsHDI1XhZlhR-Sj6sAFW-A8cuUA-Mgkhm89KmcW1lAvW8wTC8-FyuWuqOKs-TeCJB_7kiqfdJQ3ekTnxsVWCytmJDc8V7rK9smctjsVa4ewzGiYayR50QQRdxkuQhTbpg4rH2FueJPQvXS3XdsjLhTYI0-uB4iEEM36kxNdYv4oeVqelRixlIVSBHmLAnJHQBcbx8UoOqhE5GTwrlwvk-kz46oyOCwzHuYJo4vxVtTmVlA6hWrSb8wVnb0T5MmjdmPQZZoW5_dkCtmUfjneBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ: یک توافق تنظیم شده و اکنون در انتظار نهایی شدن است
پست ترامپ، ترجمه ماشین:
من در دفتر بیضیِ کاخ سفید هستم؛ جایی که همین حالا تماس بسیار خوبی با
▪️
پرزیدنت محمد بن سلمان آل سعود از عربستان سعودی،
▪️
محمد بن زاید آل نهیان از امارات متحده عربی،
▪️
امیر تمیم بن حمد بن خلیفه آل ثانی،
نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جبر آل ثانی و وزیر علی الثوادی از قطر،
▪️
فیلد مارشال سید عاصم منیر احمد شاه از پاکستان،
▪️
رجب طیب اردوغان رئیس‌جمهور ترکیه،
▪️
عبدالفتاح السیسی رئیس‌جمهور مصر،
▪️
عبدالله دوم پادشاه اردن،
▪️
و حمد بن عیسی آل خلیفه پادشاه بحرین،
درباره جمهوری اسلامی ایران و همه مسائل مربوط به یادداشت تفاهمی در ارتباط با صلح داشتیم.
یک توافق تا حد زیادی مذاکره شده و نهایی شدن آن منوط به جمع‌بندی میان ایالات متحده آمریکا، جمهوری اسلامی ایران و کشورهای مختلف دیگری است که نامشان ذکر شد.
▪️
جداگانه، با نخست‌وزیر بی‌بی نتانیاهو از اسرائیل نیز تماسی داشتم که آن هم بسیار خوب پیش رفت.
جنبه‌ها و جزئیات نهایی توافق در حال حاضر در حال بررسی است و به‌زودی اعلام خواهد شد. علاوه بر بسیاری دیگر از عناصر این توافق، تنگه هرمز باز خواهد شد.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/75660" target="_blank">📅 00:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75659">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m9hckOBtBNYwUyfAy5UeZQfiKooXZZpkGJl183GWHMWNV6OOryGNeEJtLNUnYUtAJkkYz3efzPW3AbODkiyqpgMiyctw13HNZ1Yx16KrlLkiX0W4QUvvU69guCZLTRIfIW8x8Hz3qGsJwEXjUntwfE9DlMiYofba7tuddWQPs3NG9sfnztvq3M-z2ZFibyJ64f2WzqlbeU66J2EPS4JSXvz7WwfMKezfioY_0MdunVnfGJi8L0zdVfup5rBJx1jbP0V7JUeC9DmjQawPMVSkNf27dihXfKRByavhdKB0MyIoWsYYz47lLX6dnkFGosRh_bKKkeeeKq-KrAsQcD_JTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز شنبه دوم خرداد ۱۴۰۵ در تماس‌هایی جداگانه با رهبران عربستان سعودی، امارات، قطر، مصر، ترکیه، پاکستان و فرانسه درباره توافق احتمالی برای پایان جنگ با جمهوری اسلامی گفت‌وگو کرد. همزمان یک مقام آمریکایی آگاه از روند مذاکرات گفت واشنگتن و تهران به دستیابی به توافق نزدیک شده‌اند و اختلاف‌های باقی‌مانده عمدتا بر سر نحوه نگارش برخی بندهای توافق است.
به گزارش اکسیوس، چند تن از رهبران حاضر در تماس با ترامپ از او خواسته‌اند مسیر دستیابی به توافق را دنبال کند. با این حال، این مقام آمریکایی تاکید کرده است که هنوز تصمیم نهایی از سوی رییس‌جمهوری آمریکا اتخاذ نشده و او همچنان می‌تواند توافق را رد کرده و دستور حملات جدید علیه ایران را صادر کند.
همزمان، جی‌دی ونس، معاون رییس‌جمهوری آمریکا، و پیت هگست، وزیر دفاع این کشور، برای شرکت در نشست ویژه بررسی توافق احتمالی به واشینگتن فراخوانده شدند. ترامپ پیش‌تر گفته بود پس از بررسی آخرین پیشنهاد ایران با تیم مذاکره‌کننده خود، احتمالا تا روز یکشنبه درباره ادامه مذاکرات یا ازسرگیری جنگ تصمیم خواهد گرفت.
به گفته منابع آگاه، پیش‌نویس جدیدی که قرار است ترامپ آن را بررسی کند، حاصل مذاکرات اخیر میان ایران و پاکستان است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/75659" target="_blank">📅 23:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75658">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhQ0OPR3cqHg_A2Vwj216Txgxv904M6QMgl8jhnC6gju_hj3jLodAnVGsBLnXBUoGEaNe5IplXKNI4TbzqyBHDDSkJlVeDKIIp8cUbXm7JGfHw1poFzZqQhKLT_D57W-nhmF84iO3rDAgD8arvvs2A1GMaCjhlElNDjMc1Jke6qWvCaaHxolK9apBqw0ZEXND8GtDo_sOsPM76N_Moz3N-IsI3FD-C9KRr6Ee5vnKcCLF80uWfvEWZYvuf8SRXdRmefnCml9oUVSVMvuaWapKcdq3VYZli9RlKnFRan--9Gp8FqCeJpjseKR9bxSUpKdhmKn-LcQkcvHbb5UQ4u6RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه ۱۳ اسرائیل در گزارشی از روند گفت‌وگوهای ایران و آمریکا گفت مقام‌های اسرائیلی معتقدند ایالات متحده و ایران به دستیابی به توافق احتمالی نزدیک‌تر شده‌اند و گزارش‌های اخیر و اطلاعاتی که دریافت می‌شود، «در اورشلیم به‌طور فزاینده‌ای معتبر تلقی می‌شود».
بر اساس گزارش این شبکه، مقام‌های ارشد اسرائیلی گفته‌اند پیشرفت در مذاکرات برای بخشی از نهاد امنیتی اسرائیل «بسیار ناامیدکننده» است، به‌ویژه در شرایطی که به نظر می‌رسد تلاش واشینگتن برای رسیدن به توافق در حال تشدید شدن است.
این مقام‌ها همچنین معتقدند فشار برخی مشاوران رئیس‌جمهور ترامپ در روزهای اخیر افزایش یافته و انتظار می‌رود بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در پی این تحولات، نشست‌هایی مشورتی با وزیران ارشد و مقام‌های امنیتی برگزار کند.
نهادها و مقامات رسمی اسرائیل هنوز این گزارش را رد یا تأیید نکرده‌اند.
ارزیابی اسرائیل در دو هفتهٔ گذشته این بود که ترامپ خواهان توافق است، اما در نهایت به دلیل اختلاف بر سر مسائل کلیدی، موفق به دستیابی به آن نخواهد شد. با این حال، مقام‌های اسرائیلی اکنون معتقدند روند کنونی ظاهراً برخلاف چیزی است که اسرائیل در هفته‌های اخیر برای آن تلاش کرده بود.
این گزارش همچنین می‌گوید چارچوبی که دربارهٔ آن گفت‌وگو می‌شود، شامل یک توافق موقت ۶۰ روزه خواهد بود که ممکن است بعداً در حالی که مذاکرات درباره توافقی گسترده‌تر ادامه دارد، تمدید شود.
روز شنبه مقامات ایران و آمریکا و همچنین پاکستان که نقش میانجی را بین دو طرف بر عهده دارد، اعلام کردند که در مذاکرات برای پایان دادن به جنگ پیشرفت حاصل شده است.
روز شنبه، روزنامه اسرائیل هیوم نیز در گزارشی ادعا کرد پیش‌نویس توافقی که روی میز قرار دارد، شامل تعهد اولیه ایران به خودداری از توسعه سلاح هسته‌ای و تعلیق بلندمدت غنی‌سازی اورانیوم است و سایر مسائل، از جمله سرنوشت ذخایر کنونی اورانیوم غنی‌شده ایران، در مذاکرات بعدی در دورهٔ آتش‌بس بررسی خواهد شد.
این روزنامه همچنین به‌نقل از منابع آگاه که نام‌شان را نیاورده، ادعا کرد «رهبری سیاسی ایران پیش‌تر با تحویل اورانیوم غنی‌شده موافقت کرده بود، اما فرماندهان سپاه پاسداران با این اقدام مخالفت کردند و تصمیم‌گیری دربارهٔ این موضوع اکنون به تأیید رهبر جمهوری اسلامی بستگی دارد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/75658" target="_blank">📅 21:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75657">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lHG_PWA8hXoXxmVQFaFno2t2rdE2wEXyAOGfEYTX5sBeusK9bdpKRmbo-3_Xt4ZfyLfpo34yLUGdW1nJLaPOmhuO3D60Yuz2SQZvwUGyfEa87isPzdfUt9_YdSSWHHKXXiyRupnGDTXuWqn2Bo4fPXM5zYUjp7BPzJqR1pD9z7tH2N1GYZJ-ctqp15g2M9E1ju3uqyWrl5vqV9qNqKH8a-HJVyoHdrFkJ1GW87uLBA-bH5jFKZj9ZfBXTi0jCQAGA7JqWeTYZ6qPK5rzhc195F7EjJi1unPT4_QBnxT65Up5L0ma-kgBA4h_5Li_UVHApV-5UR2g4y9nls2FOB6fQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک منبع آگاه و نزدیک به تیم مذاکره‌کننده، با تاکید بر اینکه اگر آمریکا انعطاف نشان ندهد، مذاکره شکست می‌خورد نوشت که موضوع هسته‌ای، پول‌های بلوکه‌شده و کنترل جمهوری اسلامی بر تنگه هرمز، سه موضوع اختلاف جدی در مذاکرات است.
فارس نوشت که تهران اعلام کرده که در این دوره وارد مذاکره درباره موضوع هسته‌ای نمی‌شود. تنها در صورتی که طرف مقابل شرایط اعتمادساز را اجرا کند، در دور بعد درباره مسائل هسته‌ای صحبت خواهد شد.
رسانه سپاه به نقل از این منبع نوشت: «پول‌‌های بلوکه‌شده باید واریز شود؛ شرط دوم و اساسی برای ورود تهران به مذاکره این است که پول‌های بلوکه‌شده ابتدا واریز و آزاد شوند. بدون این اتفاق، اساسا وارد مذاکره نمی‌شویم.»
در ادامه آمده است: «اختلاف دیگر بر سر نحوه عبور کشتی‌ها در تنگه هرمز است. آمریکا تاکید دارد که تنگه باید کاملا به شرایط پیشین بازگردد، اما تهران می‌گوید فقط خود را متعهد می‌کند که تعداد کشتی‌ها به وضعیت قبل بازگردد. معنای این حرف آن است که حکومت ایران با مدل خود، تعداد کشتی‌های مجاز برای عبور را تعیین می‌کند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 246K · <a href="https://t.me/VahidOnline/75657" target="_blank">📅 19:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75656">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZHSY47fmOHy3g7mXAhwU9elJFmT0Sr5XNaBeui2SWSfilznv63yWNm2FyWgmX08xKn561wt-yGY84T7BeeUgIb2U5tGR7APJCzEJR2LtkXA8j1Ltwy54SmzNcNLiUqcc5PH6LiEnDXEXz8hfxNvRU4DWFQ5LR_ZXkXpQU5VY3ZrEJC0eWN3B2C9NvrpFiK5N6dm3m1iLfkyL-t76u_aQRhVqquaX8ZCJLvwcaKZCjLdIWkPW1ae73riMm9O3WchpWcRWbSVdR-peCY4fAVV4xzyFtCVreCA7w8AhMW25gWiwiD9gfg_LWKFu2M2Lst7vS9vMwjhQIZRNH_2zLepCog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: به توافق بسیار نزدیک‌تر شده‌ایم
ترجمه ماشین:
پرزیدنت ترامپ به شبکه سی‌بی‌اس نیوز گفت مذاکره‌کنندگان ایالات متحده و ایران برای نهایی کردن توافقی که به جنگ میان دو کشور پایان دهد، «بسیار به هم نزدیک‌تر شده‌اند».
منابع آگاه از مذاکرات به سی‌بی‌اس نیوز گفتند تازه‌ترین پیشنهاد شامل روندی برای بازگشایی تنگه هرمز، آزادسازی بخشی از دارایی‌های ایران که در بانک‌های خارجی نگهداری می‌شود، و ادامه مذاکرات است.
آقای ترامپ از ارائه جزئیات درباره این توافق خودداری کرد، اما گفت که «هر روز بهتر و بهتر می‌شود.»
آقای ترامپ در یک مصاحبه تلفنی به سی‌بی‌اس نیوز گفت: «نمی‌توانم قبل از اینکه به خودشان بگویم، به شما بگویم، درست است؟»
👈
آقای ترامپ گفت معتقد است توافق نهایی مانع دستیابی ایران به سلاح هسته‌ای خواهد شد و افزود که در غیر این صورت «اصلاً درباره آن صحبت هم نمی‌کرد».
👈
او همچنین گفت این توافق باعث خواهد شد اورانیوم غنی‌شده ایران «به شکل رضایت‌بخشی مدیریت شود.»
👈
او گفت: «من فقط توافقی را امضا می‌کنم که در آن به هر چیزی که می‌خواهیم برسیم.»
منابع به سی‌بی‌اس نیوز گفتند آقای ترامپ هنوز در حال بررسی پیشنهادهاست و هنوز تصمیم نهایی خود را نگرفته است. این منابع گفتند او با مشاوران خود رایزنی می‌کند و با رهبران خارجی، از جمله رهبران عربستان سعودی و دیگر کشورهای حوزه خلیج فارس، گفت‌وگو دارد.
آقای ترامپ گفت اگر آمریکا و ایران به توافق نرسند، «با وضعیتی روبه‌رو خواهیم شد که هیچ کشوری هرگز به اندازه ضربه‌ای که آن‌ها در آستانه دریافتش هستند، ضربه نخورده باشد.»
آقای ترامپ پیش‌تر ایران را تهدید کرده بود؛ او پیش از آغاز آتش‌بسی که در ماه آوریل آغاز شد، گفته بود بدون توافق «یک تمدن کامل نابود خواهد شد» و اخیراً نیز به این کشور هشدار داده بود که «ساعت در حال تیک‌تاک است.»
مارکو روبیو، وزیر خارجه آمریکا، نیز روز شنبه گفت ممکن است «بعداً امروز خبری» درباره وضعیت مذاکرات میان ایران و آمریکا منتشر شود.
روبیو پیش از یک شام رسمی در سفارت آمریکا در دهلی‌نو، هند، گفت: «پیشرفت‌هایی حاصل شده، همین حالا هم که با شما صحبت می‌کنم، کارهایی در حال انجام است. این احتمال وجود دارد که چه بعداً امروز، چه فردا، چه ظرف چند روز آینده، چیزی برای گفتن داشته باشیم؛ اما همان‌طور که رئیس‌جمهور گفت، این موضوع باید به یک شکل یا شکل دیگر حل شود.»
CBSNews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 232K · <a href="https://t.me/VahidOnline/75656" target="_blank">📅 19:37 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75655">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ldxojK0BzYoQ2hR4NwP-GMsI5GMmW2p8qrXWGa4yB0yabAmS-zjBO7POsrvIg3LQ8RdCjoYSxFZ74qzXEQoZmANJ4thqzBbk7N5zxGH77BWrj8c0vyGAzcrDsohMUQ7u-DsBqHEHggiYLf92JD8stSueAmeOFCw9JblwX171tUIBh0V0lFI_oxq7H2kzUVM8eK7rQqI4-b6J1izJB4OJjkwyPcRcjiaTiqk3WE9yHbYYNe3EuhspAKAhUjBTm5Tx_NRBwNE7dYG_D05QOc9f4lcAWQSw1uGq7NGJ8RemkYi8yXoAtcgbSzasE3iRavzm-11cbieb2oCqmyWVZ_kBbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز شنبه دوم خرداد در گفتگو با آکسیوس اعلام کرد که اواخر امروز با تیم مذاکره‌کننده خود دیدار می‌کند تا آخرین پیشنهاد ایران را بررسی کند. او افزود که احتمالا تا روز یکشنبه درباره پذیرش توافق یا از سرگیری جنگ تصمیم‌گیری خواهد کرد.
ترامپ شانس دستیابی به یک توافق «خوب» یا در غیر این صورت، «نابود کردن کامل آن‌ها» را یک «۵۰-۵۰ محکم» توصیف کرد. به گفته او، قرار است اواخر روز شنبه نشستی با حضور استیو ویتکاف، جرد کوشنر و جی‌دی ونس، معاون رئیس‌جمهور، برای بررسی پاسخ اخیر جمهوری اسلامی برگزار شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 212K · <a href="https://t.me/VahidOnline/75655" target="_blank">📅 19:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75654">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uq0d9FblzHDMcs5sE2QiszulpHPZZ621vW7I4RlYHwzF0Xna12_19seueCeF4EgzLBoOepJ6xsmbcDpKP7mQjWgTKIWrflj-bJSe0v4Exre5zI_n19vzSiMstYhc-XZpv08LASJSHly3MbVFOhLpcy-skD-eWHgv713JET4vsVWHl_UksAEdTTK2_iWikoVtyKWwNrrvLP5NN5ukgrkCRE68Iz4gDLtVhNtYk4UY2i-Od9Lnd6BvxDqo8m4R9DFXDWvbz29Cm5_iuj-fUmiO6_Q9DmTXwuhoWhCk4iElcBLIQKzt0SvbXPfAuYRXTaA-yrhvC7yyBbuf5NKfV3FAXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، رسانه وابسته به سپاه، درباره روند مذاکرات تهران و واشینگتن، با اشاره به اینکه هنوز اختلافات جدی در بعضی از حوزه‌ها مانند تعهد واقعی آمریکا به آزادسازی اموال و موضوع تنگه هرمز وجود دارد، نوشت: «با توجه به زیاده‌خواهی‌های آمریکا، احتمال عدم حل موضوعات بالاست.»
در این گزارش آمده که در صورت حل موارد اختلاف، احتمالا در گام اول یک تفاهم اولیه اعلام شود و سپس مهلت ۳۰ یا ۶۰ روزه برای گفتگو درباره موضوع هسته‌ای (بدون تعهد اولیه جمهوری اسلامی) اعلام شود.
تسنیم نوشت که آمریکایی‌ها در متون پیشین خود تاکید داشتند که تهران در همان گام نخست باید امتیازاتی در بحث هسته‌ای بدهد و موضوع تعطیلی تاسیسات هسته‌ای و تحویل مواد غنی‌شده به آمریکایی‌ها از جمله مباحثی است که مدام در متن‌های آمریکایی‌ها مورد درخواست قرار می‌گرفت اما حکومت ایران اساسا بحث درباره جزئیات هسته‌ای را در این مرحله رد می‌کند.
بر اساس این گزارش تهران بر ضرورت پایان جنگ و تهدید در همه جبهه‌ها از جمله لبنان تاکید دارد. و این موضوع باید مورد پذیرش طرف آمریکایی قرار گیرد اما آمریکایی‌ها در برخی از متن‌های پیشین خود با این موضوعات مخالفت کرده‌اند.
@
VahidOOnLine
خبرگزاری تسنیم، وابسته به سپاه، به نقل از یک منبع مطلع نوشت که خبر العربیه درباره اینکه تهران پیشنهاد تعلیق ۱۰ ساله غنی‌سازی اورانیوم بالای ۳.۶ درصد را مطرح کرده، «از اساس کذب است».
تسنیم به نقل از این منبع با تاکید بر «ساختگی» بودن خبر العربیه، نوشت: «اساسا تمرکز پیام‌ها و گفتگوها در وضعیت فعلی صرفا بر روی مساله پایان جنگ است و هیچ جزئیاتی درباره موضوع هسته‌ای مورد بحث قرار نمی‌گیرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/VahidOnline/75654" target="_blank">📅 19:07 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75653">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUrqo1rh_M6p11VXw6f0V7tFV2x-5iN5yXNMqTJSChe-vBabv8zxAv_vIWFsLrSzw1djQXEbccqKj15AoDDbrcjZBw9jS2rK3vJhze7dX3YsaMLX_0ATPpgDZzT380RTB3QY3ZZmVKDRXaF1pyRg4Rt-t-RTvBr9BU6pUkXFUFyJVW1iE6eOI7fBpit4X3lVfwmbb_z0-pNyrSI48bYBQ5lMWWH4PMFP1sW1JnTDvD5rMEX5EJ-eCbr849BzQ-yoApsKIiEcYjksgt8FOd2dkZqwB8BQwWDd0iB7zGEESopWCIg0m5H236qPqtIoghKSNms6xpgnwMGHR6wLZuK_Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخش رسانه‌ای ارتش پاکستان (ISPR) آخرین دور گفتگوها میان میانجی‌های قطری-پاکستانی و مقامات بلندپایه جمهوری اسلامی را «کوتاه اما بسیار پربار» توصیف کرد.
بر اساس بیانیه منتشر شده، این رایزنی‌های فشرده در ۲۴ ساعت گذشته در فضایی مثبت و سازنده برگزار شده و پیشرفت‌های دلگرم‌کننده‌ای را برای دستیابی به یک تفاهم نهایی جهت پایان دادن به جنگ ایجاد کرده است.
ارتش پاکستان جزئیات بیشتری از مفاد دقیق این مذاکرات ارائه نکرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/VahidOnline/75653" target="_blank">📅 19:06 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75652">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GypaVhYZC-7XZdg6AdbvoZUKKdepZbKHiUPyXz50ou6me0mB-y17g-jClyBVSZTGS8fdpQWYZAFWuisI6ATKzlOcoE4q0x6k06AnpQD6LZUX3k0rMkgE93s7_5qs4jI7txO8jPiShRXRDJ6Uck_UAOKQbGCm23MJSGLsHStkYaDbXLgCN-YBhwDE1zqPRKjFV7th3NEtqcO0HRnLHjI5IThSSaelfydZgsNcBJWB4_2Iq3zHfINfyY67V9OfSBPKVTKUJ9sCB7BqSWz7tBRNTODZJ1jDg68iXrbHeHv_NaESSxDy3Xr-DZpDXRyvFleaLZBhn9TFxpUeI8iaCweG9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فایننشال تایمز گزارش داد که میانجی‌های جنگ ایران معتقدند در حال نزدیک شدن به توافقی هستند که آتش‌بس میان واشینگتن و تهران را به مدت ۶۰ روز تمدید و چارچوبی برای مذاکرات درباره برنامه هسته‌ای جمهوری اسلامی ایجاد کند.
بنا بر این گزارش، افرادی که در جریان این مذاکرات قرار دارند به این رسانه گفتند این توافق شامل بازگشایی تدریجی تنگه هرمز و همچنین تعهد به بررسی رقیق‌سازی یا واگذاری ذخایر اورانیوم با غنای بالا خواهد بود.
فایننشال تایمز افزود که آمریکا همچنین محاصره دریایی بنادر جنوب ایران را کاهش می‌دهد و با کاهش تحریم‌ها و همچنین آزادسازی مرحله‌ای دارایی‌های مسدودشده تهران در خارج از کشور موافقت خواهد کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 174K · <a href="https://t.me/VahidOnline/75652" target="_blank">📅 19:06 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75651">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98d608f8c4.mp4?token=uXokbaN6iAD4PYyE5ne4_Cya6sf0qfAnYWH70N74BgaNw5pVC1KqAT_Ay7W_ANWFq_MgHVoPmxJQeWqLCLf5r3a7oJ-KvkDk8s9XXJFDFAwvXWntbBYYKccEnDOEtmQ8o77JaNvnj2OwMYfa8yEuuOe7gOrDod7ZwQ6ZQyYn-NmyFRX4Eh_cufEIoLs2pThkPwDzdURGSiuB1eCv1bU5kv-pbdmg6VvtoLNLcv_tIQhPi1UllPtGn5KIVgns4sPBxOxEqu9ROLfKhulNm_LQNCGbwhvqDMYkpPCgoRqsSm7LhUB-bBSll-pM58hmy7Jv5b6BrMD9LMUYbSA60Uyuaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98d608f8c4.mp4?token=uXokbaN6iAD4PYyE5ne4_Cya6sf0qfAnYWH70N74BgaNw5pVC1KqAT_Ay7W_ANWFq_MgHVoPmxJQeWqLCLf5r3a7oJ-KvkDk8s9XXJFDFAwvXWntbBYYKccEnDOEtmQ8o77JaNvnj2OwMYfa8yEuuOe7gOrDod7ZwQ6ZQyYn-NmyFRX4Eh_cufEIoLs2pThkPwDzdURGSiuB1eCv1bU5kv-pbdmg6VvtoLNLcv_tIQhPi1UllPtGn5KIVgns4sPBxOxEqu9ROLfKhulNm_LQNCGbwhvqDMYkpPCgoRqsSm7LhUB-bBSll-pM58hmy7Jv5b6BrMD9LMUYbSA60Uyuaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
‌ویدیوهایی از اعتراض دانش‌آموزان در شهرهای مختلف منتشر شده است. این دانش‌آموزان به حضوری شدن امتحاناتشان اعتراض دارند.
دانش‌آموزان در شهرهای خرم‌آباد، یاسوج و دورود مقابل ساختمان‌های آموزش و پرورش این شهرها تجمع کردند و با شعارهای مختلف اعتراض خودشان را نشان دادند.
در جریان اعتراضات سراسری در دی ماه ۱۴۰۴ که به کشتار بی‌سابقه معترضان انجامید در بعضی استان‌ها مدارس غیرحضوری شد.
با شروع جنگ آمریکا و اسرائیل با ایران، مدارس در ایران تعطیل شد و بعد از تعطیلات نوروز کلیه کلاس‌ها غیرحضوری برگزار شد.
چند روز پیش عبدالرضا فولادوند، سرپرست مرکز ارزشیابی آموزش و پرورش در یک مصاحبه تلویزیونی از احتمال برگزاری امتحانات به صورت حضوری خبر داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 194K · <a href="https://t.me/VahidOnline/75651" target="_blank">📅 19:05 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75650">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U_QndJSQGKsLYBkBTy2BTQzE3WQTW_YZiUvvqVxeOYsofljwNerl-ZCh0CjdYxJjY2RG4Bzxp4yvowPNPDHjIebJI53VYNekYSotHEhCs3JUui-_Fqs5nID0Ur-zIFvgkJ48FoNGn9im4ATCejl6QXx19AffUm6EaJIXQdo9htDfhXvXPgo1mInmf0Bm8Gn0HIfuUIi4H9F07Ui5ygJmy9IJm60sk9wi1LAQlCcebIlThaX85Z-8S9Jqq3Y0x9skwpZ9b01o8XDkAskH6Z6NOdRYzd4E33vcX3UXF0eNJQgja-JAwQiE-DVJScvNONlv9kYa3iu4aSGE3UaqxYod9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام جمهوری اسلامی روز شنبه دوم خرداد، در گفتگو با شبکه الجزیره اعلام کرد که تهران با میانجی‌گری پاکستان با یک تفاهم‌نامه موافقت کرده و اکنون در انتظار پاسخ ایالات متحده است.
به گفته این مقام، مفاد این تفاهم‌نامه شامل پایان دادن به جنگ، رفع کامل محاصره دریایی، بازگشایی تنگه هرمز و خروج نیروهای آمریکایی از منطقه جنگی است.
او تصریح کرد که به دلیل پیچیدگی موضوع هسته‌ای و نیاز به زمان بیشتر، این تفاهم‌نامه شامل مسائل هسته‌ای نمی‌شود؛ با این حال، پس از گذشت ۳۰ روز از اجرای این توافق، درب‌های مذاکرات هسته‌ای باز خواهد شد.
این منبع آگاه همچنین اشاره کرد که قرار بود فرمانده ارتش پاکستان این تفاهم‌نامه را در تهران اعلام کند، اما او جهت هماهنگی با واشنگتن، ایران را ترک کرده است.
او با تاکید بر نقش اساسی دولت قطر در تدوین این پیش‌نویس افزود که ایران هیچ امتیازی فراتر از آنچه در این تفاهم‌نامه قید شده، واگذار نخواهد کرد.
@
VahidOOnLine
همچنین بر اساس این گزارش، تهران پیشنهاد داده غنی‌سازی اورانیوم بالاتر از ۳.۶ درصد را به مدت ۱۰ سال به حالت تعلیق درآورد.
@
VahidOOnLine
🔄
آپدیت:
خبرگزاری تسنیم، وابسته به سپاه، به نقل از یک منبع مطلع نوشت که خبر العربیه درباره اینکه تهران پیشنهاد تعلیق ۱۰ ساله غنی‌سازی اورانیوم بالای ۳.۶ درصد را مطرح کرده، «از اساس کذب است».
تسنیم به نقل از این منبع با تاکید بر «ساختگی» بودن خبر العربیه، نوشت: «اساسا تمرکز پیام‌ها و گفتگوها در وضعیت فعلی صرفا بر روی مساله پایان جنگ است و هیچ جزئیاتی درباره موضوع هسته‌ای مورد بحث قرار نمی‌گیرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 191K · <a href="https://t.me/VahidOnline/75650" target="_blank">📅 17:58 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75649">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VTrvgKlfE4WrJ_tbVYDZ-DTt8A2RCd0cCHgPiteltsv-4Voywn2ZMDydt3qPimHKXzUc3swi4EmPDLbWn3qv1DSXTvnyML26hOE7ZJFYPM0s2NQXkbYeiczqNjkUDU1vyvE7uxV0JjhOOMine-DVxjzQXxK6No3x8ZlS7CQUmxwAtt_Vjg8u9t4Hx52sXpxS2IYmUmXcC8I5xafHKmPE058bfWtZGFQ2fuWvDeS8Ff-je7lE2KsVU-dCapgDneen2Yc0eHHyZlRHZ5nv8jwiZQZ7lgCeQ4bd-r0G3azQ5FxSCRLHj9MHU_tO-WgtYYOw8rHdOfHbdlLX8zHnX448AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العربیه گزارش داد جمهوری اسلامی دو پیشنهاد به میانجی پاکستانی ارائه کرده که بر اساس آن، در ازای پرداخت غرامت از سوی آمریکا، تنگه هرمز را باز کند و پیش از امضای هرگونه توافقی، پرونده تحریم‌ها و دارایی‌های مسدود شده مورد بحث قرار گیرد.
دونالد ترامپ، رییس‌جمهوری آمریکا، پیش‌تر گفته بود که حاضر به پرداخت غرامت به تهران نیست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 184K · <a href="https://t.me/VahidOnline/75649" target="_blank">📅 17:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75648">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HeFfECusJDeLRIpOfi0ddEosWjoEO1oT_aLrXYPLHOtemM46hHkpd0kzDp7aZdw5vt-LU6gC9Fp2BnNlywBXqxukQQBOPM_X148YNoCNBn3y-iR0rLXdPWHImxieI6clDG6BD9rXcHbDCVS9NeX81mXw0MWwOwbOMbk5yAZ78LUobUK-STTtIXYXFuBJDqPSUaa5dJMq6Vjn1xTnb3a6DEjCREEK4HDl4HpIju2RURl3-r_DaAr6Eo8Xm9DtoF3GUSNu7lx1m90SgwwVHH1HmgADgw4Txe2SUmoXQQJSsbtBESJIvfAvaeGyhXWWWdT7-3gvsD3pLZkGhZn9QtE5pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ تصویری از نقشه ایران را که با پرچم آمریکا پوشانده شده، در شبکه اجتماعی تروث سوشال
منتشر کرد
. روی این نقشه نوشته شده است: «ایالات متحده خاورمیانه؟»
ترامپ توضیح بیشتری در این‌باره ارائه نکرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 183K · <a href="https://t.me/VahidOnline/75648" target="_blank">📅 17:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75647">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/028369f0dd.mp4?token=jOZIuVlqvzcbg-GJuE7MUqBdc5_c2eV4v6EQ9wR8B6N-u4Z3iczLndq71NVkQug-5Ts59O9DjJgXBu5W1Z3RnO34071PVYCioBfbSWvnpxfYSfLgwSvKJaZehKXGI6mNDvYHSm9RHrDnsB4Ixn7zq7KJU6hxhBIKRtVb-GVnry5P5NJ3Jj3oIqhgpQu7mbM1T_7J0E_WZsvoHHsiFdGN_kTJ7nKKez16CNvIxhECJxnOjK-l1gzV4ILG7HbRPXHUDuVqJKlsz-AQmMXbOXDmp_m7ly9FHVBA5LPxk1vzlWYuQbniuuBFuIIrf9rv0A2az76ma7ewQvsyPm-ujw0ciQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/028369f0dd.mp4?token=jOZIuVlqvzcbg-GJuE7MUqBdc5_c2eV4v6EQ9wR8B6N-u4Z3iczLndq71NVkQug-5Ts59O9DjJgXBu5W1Z3RnO34071PVYCioBfbSWvnpxfYSfLgwSvKJaZehKXGI6mNDvYHSm9RHrDnsB4Ixn7zq7KJU6hxhBIKRtVb-GVnry5P5NJ3Jj3oIqhgpQu7mbM1T_7J0E_WZsvoHHsiFdGN_kTJ7nKKez16CNvIxhECJxnOjK-l1gzV4ILG7HbRPXHUDuVqJKlsz-AQmMXbOXDmp_m7ly9FHVBA5LPxk1vzlWYuQbniuuBFuIIrf9rv0A2az76ma7ewQvsyPm-ujw0ciQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنان مارکو روبیو در سفر هند در پاسخ به سوالی درباره مذاکرات با ایران
ترجمه ماشین:
ممکن است امروز کمی دیرتر خبری باشد. در همین لحظه خبری برای شما ندارم، اما ممکن است کمی دیرتر امروز خبری باشد. ممکن است هم نباشد. امیدوارم باشد، اما هنوز مطمئن نیستم.
سؤال در مورد موضوع ایران است و همان‌طور که گفتم، پیشرفت‌هایی صورت گرفته، پیشرفت‌هایی حاصل شده. حتی در حالی که الان با شما صحبت می‌کنم، کارهایی در حال انجام است.
امکان دارد که چه امروز کمی دیرتر، چه فردا یا چند روز آینده، چیزی برای گفتن داشته باشیم. اما این مسئله باید حل شود، همان‌طور که رئیس‌جمهور گفته، به یک شکل یا شکل دیگر.
ایران هرگز نباید سلاح هسته‌ای داشته باشد. تنگه‌ها باید بدون عوارض باز بمانند. آنها باید اورانیوم غنی‌شده خود را تحویل دهند، اورانیوم غنی‌شده با غنای بالا.
ما باید به آن مسئله رسیدگی کنیم. ما باید به مسئله غنی‌سازی رسیدگی کنیم.
این‌ها نقاط مورد نظر رئیس‌جمهور به طور مداوم است. و ترجیح او همیشه این است که آن را از راه دیپلماتیک حل کند. ترجیح او همیشه این است که مشکلاتی از این دست را از طریق راه‌حل دیپلماتیک مذاکره‌شده حل کند.
این چیزی است که الان روی آن کار می‌کنیم. اما این مشکل حل خواهد شد، همان‌طور که رئیس‌جمهور به وضوح گفته، به یک شکل یا شکل دیگر. امیدواریم از طریق مسیر دیپلماتیک انجام شود. این چیزی است که روی آن کار می‌کنیم. و شاید چیزی برای صحبت در مورد آن موضوع در حالی که اینجا هستم، در طی این بازدید در زمانی داشته باشیم.
EricLDaugh
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 191K · <a href="https://t.me/VahidOnline/75647" target="_blank">📅 17:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75646">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQUu9KMvqCKl_Y_QmOEai-o3oOxTOTN0E0n30ZarX150jwl7OdSzMbGJx8WSYqaNqkZ1yynxmLvhqAqhHCW8v56_2VuQp-lmm9ao_w6Xlum1n6m2bPrn3UMU4NK3zko6CqDe_zlNCAjwXLowK3-Ez9nckH7JPI-WFjw3ilC7AnloWZHF1HpaL7sDLC7U-xjO88bfQcMMasWvLT8_vfLpwGSeSm1Htqcd2zWOVOWvgtKrrClz0qJisVAl8FcZxbRgnvA7FiNyiPQY4IFznS5nOzkETazq8_1mfWzKC9jzIOSNUmQSqWkqqm_XXVeANd3dbDDEo5JVs1DRtR_s0VZgeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی، وزیر خارجه جمهوری اسلامی، در پیامی به شیخ نعیم قاسم، دبیرکل حزب‌الله لبنان، گفت: «جمهوری اسلامی دست از حمایت حزب‌الله نخواهد کشید و همچنان از جنبش‌های مطالبه‌گر حق و آزادی پشتیبانی می‌کند. تهران پیوند آتش‌بس لبنان با هر توافق احتمالی را به‌عنوان شرط مطرح کرده است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 184K · <a href="https://t.me/VahidOnline/75646" target="_blank">📅 17:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75645">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UaNW5QcZRQIArz3gEtn6kIrC1vA0c0nbFQhanhfzemA7IhZqQ2Gkci_GaUEjM1Z9oVV0ob9fF6QWfBS5zelTosOqc8wUwYIFRQQJ6u-uJ3faSCAE0qBj97VHJIDOufCA2ZPIcyG5G_UbDgBSL0jLSBlu7DBT9uJRUIb0wLrhHFDSIlKS_gYyo9Vv-bIVq5br2ck2kxkim5KtRTrcSbareTGukk-Y5XwK36XzckxspbRucNV7P2LeuzUFJzTKFBepZ4y41H8tL05Sj1wbGcXr6DIHfPhFlsC38vxobsxVK4PJC1deFgqTkguhMYYm2IcD2r59DcoYuwxY1lqqolO20A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرویز قلیچ‌خانی، کاپیتان پیشین تیم ملی فوتبال ایران و فعال سیاسی چپگرا در ۸۱ سالگی درگذشت. او به آلزایمرمبتلا بود.
نجمه موسوی-پیمبری، «یار و همراه» پرویز قلیچ‌خانی به بی‌بی‌سی فارسی گفت: «قهرمان ملی و چهره همیشه زنده ایران در تاریخ بیست و سوم ماه مه ٢٠٢٦ مصادف با  دوم خرداد ١٤٠٥ در بیمارستانی در حومه پاریس درگذشت.»
آقای قلیچ‌خانی، پیش از انقلاب، علاوه بر تیم ملی، در باشگاه‌های تاج، پرسپولیس و پاس هم بازی کرد. او تنها بازیکنی است که با تیم ایران سه بار قهرمان جام ملت‌های آسیا شده است. پرویز قلیچ‌خانی بعد از انقلاب هم در خارج از کشور، مجله آرش را با گرایش سیاسی چپ اداره می‌کرد.
او فوتبال را از کوچه‌های محله صابون پزخانه میدان شوش تهران شروع کرد و بعد از مدتی کوتاه فوتبالیستی ماهر و بالاخره کاپیتان تیم ملی ایران شد.
ولی هنوز طعم قهرمانی فوتبال را درست نچشیده بود که توجهش به سیاست جلب شد و از پشت میله های زندان سر درآورد.
پس از انقلاب از فوتبالیست حرفه‌ای به فعال سیاسی و روزنامه‌نگار خارج‌نشین تبدیل شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/VahidOnline/75645" target="_blank">📅 17:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75635">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NLjkwxrAvHXsWQPJ2Wqwa2gQIsMpj7qlWyp3neN_jSaaZ1sXN9fJGND7NkfDIBYYblpRtqLy2SNgcYUf0SljlOZvSOyEBcZHRDRg6cWh-6bTc56Zge9AM2M_xxadvQucN3Sp0WUCHmX_3Zl8gx6544zPaz5Bx02mlIkO7OuLMzo-MXGG30UtRw8tQkYZLCf0m_56_NFnktPHG4NQIvM4PSaUjKaLxHP0Zd0gHN6BOagfThlMczHijII3TO3zkamBBnfGLGOlFa0Zu7ZB57IW9ZDYcIfRB-7-gq-jkZPjCLOz5t_igvFa3p0fxNpUEnlcEWHzwbbHYB7Z3SUu7y2oWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LKNzG-P_F6oExknRfmWM5kica4T63zB2OOkXER8pei62QRkiXSm4aBuQufVvEJE79Ltc4MMQS9scJpcCO4UnEbKF9nbAhYPvUR1d5O38yXUHGIO0HH-KO1WbYdy8E340SlLdrJFpAVomLKqJhGLG0HxI7KLtTzQoUHkI2xq5bXaTOxu6ZFUOiaWLKBGX9i7grwX0g4ZmqqHs6Ajjs2truaLYazf8Pu8rXfnNjNb_IP6LWGulghUdWf4IBKoB2fyV81sFcRpJwOeggeyPBXV7O70hTsNReOIQZ4va38UseNBfZQOHLs82ErG8kzNsFbNdykVtR2hkAWl5EsvI6bN_ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h8gEpS-KBb-3QhFThePSZYnv3BXSbI0PNqYm9sMEbYV0XfsrII2f7FPbX7PfgFyM8m6QDBaDyTtKtBWqcdZp1EEe67ZcsvLblFCrjVRjdTVXsl6g8_mT7Wi55SFK1J9AvJWYrTtgD5hpQlYWWBmsv9luPAfDC6q5buXchuh3Mc87qUwBnvPTpGvnx1nR7V6nG8_KAd1ZJvE524Yf1rGXoHUxOmtasg-1-w4xvLOM3B5YCczFKcXCeHhKgrRWFNA0qgYxs4qot_4RsKy1-LNRxvf4M3_HHasaFs2NM2nLtDgkI4wSdRswiYoGHx-CxsPBCJOfA7EpgrAuhvPbS54N3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Z7fQU7mPcksKrKSRt7g_c7bBYnBe3XoUTGWME2GpcOUk465lfYb6ohO5Y14ipq-m_5I86biN3K4wyYFS0WiQa4efv7WojK8oMaWsjzClHZppcopsYq9w7KnWCsh-AuIwdrxIIj7qulSFh1V75cW2zfKjmZeQomBQIlhUl7FTf4nMLU8foO3yasB46fPSz1g35uHGsNOwz1Cx_XUoOT6A_J1Gt8jl8jtKCzqLRuPxhYP5wl89HbrXXlgo4a6frdWSEZmphXbgsaM32YxmiL27VCvMm88plKvACcqSt-xBKFHp97nxPxM_gyxCMgVVO4VABbi3lh640TwzUUyii1yRjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QdkpJAFVpOJhabd8ALJZU4b_C2W27Lw4a4vjuGjxFjB4H8WnypLwjVuX3zE7tWwWn5IikVq_DH9lQ04jQXdDIosQ8yZqSBw_9Pd3uBjrrfILc_D4IluQ9iQZF6rTy6T4-wZpdj_E03YzQmzi9CnEbf3sNK1__rduS2WTcaf60Me2SYPRHkyxomg1Wtf7-drvN2b5c9gJclZkr76pKlPnKF46R6_kjh1B3YhRVq3SlBc-n9j1F_lMPzjcjkBV1guKkqrUxVqHK6qCds7StPpWzu_xR0MV_QdvGIebry-gbwNKeYBp8EWmf3rsmmSJ8k8-2Jk7ZvHmxL0D7COGO2tsDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jWWcgL6Yp_p0Y1lJsxV7FSxpaHnBcrl2TMpN6MZ_Q08UUS6rmntc9Zlv7aKjuGH4-zG_0ejLvoPjqlXkwpiTt6prhsu7-cmtSo89wmZFd9FzXFhl3wFI5CcDXNG4p0SyWdYFvw9FDKx1XSRg99GPoucNE8_WxBxo4GFr9R5vhu78pg0lIoTBEhwbbqy_Z_quRyltyPJfCWcvM4sv-fzZaRmWdgmoSPkWvq9xmUqTCFzWGej0EqfOlVMvpgkyI4arhRXcqQLTJsuwVLRwkk7w-H13CklJARLCcyPBjPbD0K250OxE7l8TM1-YE-WM3nADX2m0oI6wtBp-f1g9bY4MvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DJuXXyL5C3HWNAw0zOBuV76sSqGdc3PFQxYFcdHQYY2u9mTHtloiFsbD_kKTJ3FkJ-rycNjzSVjm7uHoITfqDVC-kA7EgFUttJTBkguXlNhAtAchBVzTYVjB2oTeHEMDB13W8daBUJifJIMHwds5jpZv1pHKmeRLKMohYVY0GejHfBiiunbQBZo9rOrccfkTGvA8ATJsYENsUmkc2FuZJKNFYgqCQxQQG8mLXyqwX6N-uA7Kas7GXBIIzj-mFuaZuPxOwe_TYXLvf8L9qS-8C7wz7I6EwIAOcTIUoTHUiBD6ZE9wITfpi-Y7qWOLnVFMJAMHXtQ5qmGW1pPEK_XdGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AnxjCByUlZvgVBgIoZS1dS8w9Vbr6qdibbczuPXHwh93xw_ZlcMBwwyaKoO-5eC4P9_ca4kxXk3lTKbRBiQ4M55jeLezaznXSXRz0d-XbhYD8k2nVZnpG615TcW6tjt5Iwc5qyQlThy8tbYmyHg8Ec2jsGEFyEywi7wmMS6EbbWE2cmVeNTPedMGH9Z9pwRKQXL2yaesOnJjfOvGiqr-oq2HKe3PGh3-moeKv9D1DcsxNJ2PIUNn_jkMvouCxhXb_VIgCQn8mLS9ddx8uX0--y0OJLNktGXDOx88cP4DIDBU2lXRQrfsLVkG39BMczJduMo5p7UfvrK_CNcYxdvwyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hRhtknJndZsAOAmAlXTghd_nwm9slh-Gl2bR2YQVkAJEL0WDHtFC77SppgazFqMC-exM1D--sp2KWNXsUyQpwHuJNuFr1VheFXfNbubf3G5ziokKeNJL_J_ztcWs_tO97XVwCFBNrAzuHHm4fvTG01OGY_ANlIqPMkF2FtCG17YDrv_qKKXozSrQOuNBmBmJwnhInE1ON71rug9RcaZq3EhTH977WqiPKMGwD6r4w3v5PLP4RxViPdRpabJVfeHYJaGlEE9ekkCK1RdBF5dvEX7dznZ2X7vA-fda0sMuElLcbpUqYBw-ySme9dukMAJ9WeeMeXk-a1E021cpH9M2hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GvzcVD8fJYtAY62bPgkND63vgBaZpCDze4PUXneehGn8sGQt60YrySUQ7zg45juWCkc61ss6MMLNUcoojtSBSYJbbzdGT9JOOn6uMVPiVgyn5z_iB3OjG-l4w3ROT-6Hg1NGbNKYv9corhaQGElDXaSxVeR2aRYdflC8Bz7TXCSjhYhb_6XkB5o0I-jsp07wtOEfy-1Lsn-WSCdWFmudPR1LdlRsPPpncE4YG6SVKP9WXbK1mJfGsP0seEGI7Oa5rg7CPxEjFu2_BLsz6X9QYUU01mmVCZJz0AtkB41xt6sKJbAvUC7mtitI3o1SmjdmBMbmex-CKqUa6fjbFcWgqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شبکه العربیه به نقل از منابع آگاه گزارش داد عاصم منیر، رییس ستاد کل ارتش پاکستان، پیام‌های آمریکا را به تهران منتقل کرده است و بخشی از این پیام حاوی تهدید به ازسرگیری جنگ بوده است.
در این پیام‌ها همچنین تاکید شده در صورت موافقت جمهوری اسلامی با توافق، حل مسائل اختلافی در مرحله بعدی انجام خواهد شد.
به گفته این منابع، آمریکا در پیام‌های خود تصریح کرده است تهران باید اکنون با توافق موافقت کند یا با پیامدهای منفی روبه‌رو شود.
@
VahidOOnLine
شبکه العربیه،  روز شنبه دوم خرداد ماه، به نقل از «یک منبع بلندپایه ایرانی» گزارش داد پیشنهاد ارائه‌شده از سوی تهران تاکنون نتوانسته رضایت آمریکا را جلب کند و همچنان از دید واشنگتن «غیرقابل قبول» تلقی می‌شود.
@
VahidOOnLine
عاصم منیر، رییس ستاد کل ارتش پاکستان، پس از سفری یک روزه به تهران، ایران را ترک کرد.
به گزارش ایرنا، او به همراه محسن نقوی، وزیر کشور پاکستان که از هفته گذشته در تهران به سر می‌برد، پایتخت ایران را ترک کرده است.
عاصم منیر در جریان این سفر با محمدباقر قالیباف، رییس مجلس، مسعود پزشکیان، رییس‌جمهوری ایران و عباس عراقچی، وزیر امور خارجه دیدار و گفت‌وگو کرد.
@
VahidHeadline
محمدباقر قالیباف در دیدار با عاصم منیر گفت نیروهای مسلح جمهوری اسلامی در دوران آتش‌بس بازسازی شده‌اند و در صورت آغاز دوباره جنگ، واکنش ایران شدیدتر خواهد بود.
او گفت: «نیروهای مسلح ما در دوران آتش‌بس به نحوی خود را بازسازی کرده‌اند که در صورت حماقت ترامپ و آغاز مجدد جنگ، حتما برای آمریکا کوبنده‌تر و تلخ‌تر از روز اول جنگ خواهند بود.»
قالیباف با اشاره به نقش پاکستان در میانجی‌گری افزود: «در آتش‌بسی بودیم که شما واسطه‌اش بودید و آمریکا با نقص عهد، محاصره دریایی کرد و حالا به‌دنبال برداشتن آن است.»
@
VahidOOnLine
شیخ تمیم بن حمد آل ثانی، امیر قطر، روز شنبه دوم خرداد ماه در تماس تلفنی با دونالد ترامپ، رئیس‌جمهوری آمریکا، آخرین تحولات و رویدادهای فوری منطقه را بررسی کرد.
بر اساس بیانیه رسمی دیوان امیری قطر، این گفتگو بر «تلاش‌های منطقه‌ای و بین‌المللی برای حفظ آرامش کنونی و کاهش تنش‌ها» متمرکز بوده است.
«امنیت دریانوردی، حفظ ایمنی آبراه‌های راهبردی و تضمین تداوم روان زنجیره‌های تامین جهانی و انتقال انرژی» از دیگر محورهای این گفتگو توصیف شده است.
به گزارش رسانه‌های قطری، امیر قطر در این تماس بر موضع ثابت دوحه در اولویت دادن به راه‌حل‌های مسالمت‌آمیز برای بحران‌ها تاکید و اعلام کرد قطر از همه ابتکارهایی که با هدف مهار بحران‌ها از طریق گفتگو و دیپلماسی انجام می‌شود، حمایت می‌کند.
این خبر در حالی منتشر می‌شود که رسانه‌ها از گفتگوی تلفنی وزیرامورخارجه قطر با عباس عراقچی خبر داده‌اند.
همزمان گزارش‌ها از رایزنی‌های گسترده کشورهای منطقه برای جلوگیری از حملات احتمالی آمریکا به ایران خبر می‌دهد.
این در حالیست که شبکه خبری العربیه پیشتر از هشدار واشنگتن به تهران مبنی بر از سرگیری حملات به ایران خبر داده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/VahidOnline/75635" target="_blank">📅 17:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75634">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nt36DX9Z3DSzYtIjzh35R--t_rU5pxd7a_lJyKP94GDgX0kRfagc-5TMDikHzSwYrhTVdqENhGp1BJVWxSExIRhzzuh6LB_mqNHlb9_8ty2aK0etUKF7-TfNZkpO0vOMgpkz51au-FwjqDjfWw7zWdYUyJLPxdxLXAsCIvtHZDZYjY1vNloZt2zmr2Q9KxfmgSSsf5pAmizGVIwOfyQEB7aofRT6l0qLNQ21dLNgHk-7whQXp4CmXlxr5qHGZzyobCMVL0suI2miEFz346-vwnNjdPxoH9-CwVf6A0_gO8KwrOw4_O38bYEd8mQP0b02XuzMR7esdGI6s8cCmD9fNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سازمان هواپیمایی ایران اعلام کرد این سازمان هیچ اطلاعیه رسمی هوانوردی جدیدی درباره اعمال محدودیت در آسمان کشور صادر نکرده است و شرایط پروازی عادی است.
او با تاکید بر تداوم وضعیت عادی پروازها گفت: «شرایط آسمان کشور همچنان مانند روال گذشته است و پروازها طبق برنامه انجام می‌شود.»
سخنگوی سازمان هواپیمایی بدون اشاره به جزئیات اطلاعیه هوانوردی (نوتام)، افزود: «نوتامی که اخیرا در فضای مجازی منتشر شده، تکذیب می‌شود.»
سازمان هواپیمایی کشوری ایران روز جمعه یکم خرداد در اطلاعیه‌ای اعلام کرده بود فعالیت فرودگاه‌های واقع در بخش غربی محدوده پروازی ایران، موسوم به «FIR تهران»، تا دوشنبه متوقف شده و تنها شمار محدودی از فرودگاه‌ها مجاز به فعالیت هستند.
بر اساس آن اطلاعیه، فرودگاه‌های ارومیه، کرمان، آبادان، شیراز، یزد، کرمانشاه، رشت و اهواز از این محدودیت مستثنی شده‌اند و فعالیت آنها نیز فقط از طلوع تا غروب آفتاب مجاز اعلام شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 234K · <a href="https://t.me/VahidOnline/75634" target="_blank">📅 17:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75633">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYAXi2dsMWxzZ7Zs2W6-C1_Zo5_kbgaWImis4O5neZ5zpaIrMrgp8388Oc8Ll9VcWyRl3mLRamoq3u5sICEbA_mfTuQALbVTw6S7VkXqbwH-TNyrx7gfR6D9hmlZYOulaqYYG30fRhl3Tdyd0K3VblW-hwp9f3lt1Rx3vUybwKNh3sD8NG_ecmhHf0LNyJyrg0iuf6PR0RXuV9s-nybuin3wkUgkrgNaXiTr4BOHNmtTZWciV0IyKd_jWR35W3yyGv6LYTa-rho5H-aMx3GaH1L4Q8rNq-m4jYjYAtXBV-3qk8B9Kw8AVS5QFiOk3m03weoSxpBffTx7ZKrT7D-Ldg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌ها در ایران از دیدار فیلد مارشال عاصم منیر، فرمانده ارتش پاکستان با عباس عراقچی، وزیر امور خارجه ایران در شامگاه جمعه یکم خرداد خبر دادند.
بر اساس این خبر، دیدار این دو مقام تا پاسی از شب ادامه یافته و محور گفت‌وگوها «تلاش‌ها برای جلوگیری از تشدید تنش و خاتمه جنگ» و «راهکارهای تقویت صلح، ثبات و امنیت در منطقه غرب آسیا» بوده است.
جزئیات بیشتری از این دیدار منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/75633" target="_blank">📅 08:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75632">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9LyB58HnxX-8IM7Ecxh0-JruH4gYBKvMHtsD8ry5rvBhaaoN3tZhVbT5JlcwXbzvv-Yr1ncMtETv5MjVJqBJYLu4nr-0mM9S0P1sp5zuoaAIfl__-ia6zqkao82u9MQSjg0ykKP13gGjkUo-e_PKSmVzYGnHVCjboiRIHip1l-AUACFm2xOCE1xQHvdUBJsl5NvfgWUskLe941fKkwwWF2IjMBYmXUvhxXV3DPM2qG5RYYSRk61MDUKYjel_g6XizCt9dcCBeibxpGa9JNkVnh_e43RaXbzwXsBe2rc1vvClCvu10_MDFktEKar_Q5znewlj-05iEHPpZOlxitNvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت دونالد ترامپ اعلام کرد که سیاست‌های مهاجرت به آمریکا تغییر می‌کند.
در یک تغییر اساسی در سیاست‌های مهاجرتی آمریکا، دولت این کشور اعلام کرد خارجی‌هایی که قصد دریافت اقامت دائم یا همان گرین کارت را دارند، باید خاک ایالات متحده را ترک و از طریق کنسولگری یا سفارت آمریکا اقدام نمایند.
زک کالر، سخنگوی دفتر مهاجرت دولت آمریکا، گفت که این سیاست «نیاز به یافتن و اخراج» کسانی را کاهش می‌دهد که درخواست اقامتشان رد شده است.
از سوی دیگر وکلای مهاجرت و گروه‌های امدادی می‌گویند که این تغییر احتمالا به «جدایی بیش‌ازپیش خانواده‌ها» منجر خواهد شد و قربانیان قاچاق انسان هم مجبور خواهند شد «به کشورهای خطرناکی بازگردند که از آن گریخته‌اند.»
این تغییر سیاست تازه‌ترین اقدام آقای ترامپ در محدود کرد مهاجرت به آمریکا است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/75632" target="_blank">📅 08:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75631">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3vh99kH2bgJubScXqGVII4RM6k9jjc82yWsLfM7W_ajXrpr0UOxX-_4RvUdGlcI1__s66tLloBWxEXVG1Hi1MlsUvpJdYTyA3sKPRnKg-Pbed2FFRobiwk8J0I56K1eYYCLUu7I9qZSO6N0fvW94EOMv7AhQGtRXea1IGMgke8A6G-7VaXlJkPkTJuBZyfa5btb5Xyq8XZTA0JSS5F6gsu9dmzMOUoVDBH0uSFO7Ogks3fuwGF0ud5Rd9M8cYnkKckrB_7jX525xQ07gDnlpV7TZpC9s3W4hDPCFeowPjF4Hyiq9O4iHRSOWRpawhCmVdEJIxAWADWyVQRe4F5unw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه «نیویورک‌پست» به نقل از منابع آگاه افشا کرد که ایوانکا ترامپ، دختر ۴۴ ساله دونالد ترامپ، هدف یک طرح ترور پیچیده از سوی یک تروریست تحت آموزش سپاه پاسداران انقلاب اسلامی قرار گرفته که با انگیزه انتقام‌جویی از کشته شدن قاسم سلیمانی طراحی شده بود.
بر اساس این گزارش، متهم که یک تبعه عراقی ۳۲ ساله به نام «محمد باقر سعد داوود الساعدی» است و به تازگی دستگیر شده، عهد کرده بود برای «به آتش کشیدن خانه ترامپ»، دختر رئیس‌جمهوری آمریکا را به قتل برساند.
منابع اطلاعاتی اعلام کرده‌اند که الساعدی حتی نقشه و جزئیات معماری عمارت ۲۴ میلیون دلاری ایوانکا ترامپ و همسرش جارد کوشنر در فلوریدا را در اختیار داشته و پیش از این با انتشار تصویری از موقعیت این خانه در شبکه اجتماعی اکس (توییتر سابق)، به زبان عربی تهدید کرده بود که «نه کاخ‌ها و نه سرویس مخفی آمریکا» نمی‌توانند از آن‌ها محافظت کنند و انتقام تنها مسئله زمان است.
وزارت دادگستری ایالات متحده اعلام کرده است که الساعدی از مهره‌های بلندپایه در حلقه‌های تروریستی وابسته به ایران و کتائب حزب‌الله عراق به شمار می‌رود که در تاریخ ۱۵ مه در ترکیه بازداشت و به آمریکا مسترد شد. او در ایالات متحده با اتهاماتی سنگین پیرامون هدایت و اجرای ۱۸ حمله و تلاش برای ترور در سراسر اروپا و آمریکا مواجه است؛ پرونده‌ای که شامل بمب‌گذاری در یک بانک در آمستردام، حمله با چاقو به دو شهروند یهودی در لندن، تیراندازی به ساختمان کنسولگری آمریکا در تورنتو و آتش‌سوزی عمدی در معابد یهودیان در بلژیک و هلند می‌شود.
این متهم که به دلیل وابستگی به قاسم سلیمانی او را مانند پدر خود می‌دانست، پس از کشته شدن سلیمانی در حمله پهپادی شش سال پیش آمریکا در بغداد، تحت آموزش‌های نظامی و اطلاعاتی ویژه سپاه پاسداران در تهران قرار گرفت و ارتباط نزدیکی نیز با جانشین او، سردار اسماعیل قاانی، برای تامین مالی شبکه‌های تروریستی خود داشته است.
اطلاعات فاش‌شده نشان می‌دهد الساعدی با وجود نقش برجسته‌اش در شبکه‌های تروریستی، حضور بسیار فعالی در شبکه‌های اجتماعی نظیر «اسنپ‌چت» و «اکس» داشته و تصاویری از رایزنی‌های نظامی خود با قاسم سلیمانی را نیز به اشتراک گذاشته بود.
او با تاسیس یک آژانس مسافرتی مذهبی و با سوءاستفاده از یک «گذرنامه خدمت عراقی» که سفر بدون تشریفات امنیتی و اخذ آسان ویزا را برای او ممکن می‌ساخت، به راحتی به کشورهای مختلف سفر کرده و با گروه‌های تروریستی ارتباط می‌گرفت.
الیزابت تسورکوف، پژوهشگر انستیتو «نیولینز» که خود ۹۰۳ روز در اسارت کتائب حزب‌الله بود، تایید کرده که روابط الساعدی با سلیمانی و قاانی فرصت بزرگی برای گروه‌های شبه‌نظامی عراقی ایجاد کرده بود. الساعدی که در زمان دستگیری در ترکیه در حال سفر به روسیه بود، هم‌اکنون در سلول انفرادی بازداشتگاه متروپولیتن بروکلین، در کنار دیگر زندانیان سرشناس نگهداری می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/75631" target="_blank">📅 04:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75630">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJF8dumrJlozDSn0HZ2ci4TmLU3jOs86yC0c3ZIzCvyDkf97Dj0VJZ8AfIqC93w2iuFHCkz4s2RAqVZxRmMPfLRrZDiW0_avXCIXBO5docnQBa9p9sJZoAVVGxshUto4KIcjmN0_oJTvZwo-1AC2Eg_Fq00pmc3wsQfGn5Ha5O-I2xDvA-8uH7LrrEJpxf2Z_sQBhqSoL6YecOVZFGTmnkzqDHi5rYNiMiMg_NguyWfKZogRIHEmx219ftBxzn26ZaFPR6vfH4whGJfZGNQyvzc_7bZQZ8Aj0n6OqgyUYA6AoDyP1y6KAkWrJHQSteUzkycq3rFqIYK2lBQa3-z5rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌بی‌اس گزارش داد که آمریکا در حالی خود را برای دور تازه‌ای از حملات نظامی علیه ایران آماده می‌کند که تلاش‌های دیپلماتیک همچنان ادامه دارد.
به گزارش سی‌بی‌اس نیوز، منابعی که مستقیم در جریان برنامه‌ریزی‌ها قرار دارند می‌گویند که دولت ترامپ روز جمعه در حال آماده‌سازی برای حملات تازه بود هرچند تا عصر جمعه تصمیم نهایی گرفته نشد.
آقای ترامپ در پیامی در شبکه‌های اجتماعی اعلام کرد که «مسائل مربوط به دولت» مانع از حضور او در مراسم ازدواج پسرش، دونالد ترامپ جونیور در روز شنبه خواهد شد.
او قرار بود تعطیلات آخر هفته را در مجموعه گلف خود در ایالت نیوجرسی بگذراند، اما اکنون به کاخ سفید بازمی‌گردد.
چند منبع نیز گفته‌اند که برخی اعضای ارتش و جامعه اطلاعاتی آمریکا برنامه‌های تعطیلات خود را لغو کرده‌اند؛ اقدامی که در انتظار احتمال حملات تازه انجام شده است.
به گفته این منابع، مقام‌های دفاعی و اطلاعاتی آمریکا در حال به‌روزرسانی فهرست نیروهای آماده‌باش در پایگاه‌های خارج از کشور هستند؛ همزمان با خروج بخشی از نیروهای مستقر در خاورمیانه، در چارچوب تلاش برای کاهش حضور نظامی آمریکا در منطقه و نگرانی از واکنش احتمالی ایران.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/75630" target="_blank">📅 04:06 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75629">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n76HkwNVYRrOg6PngL0WwZJhYYvjQMRBdnp5kAjske5-sBr2PXOg1w1K-RjCxVuqKbB2QCP9FJxLjBEBdqBxyprWq4At5jbbUnVAyJrbsRfdy2HcNe_l8CLwyx6fPOPVu7ELehUs3LuyZgzhQ3RmFCOWuYas9x53o7XS_Z6GbGdDplhjGrKaooL5UVscMXsu7sQqQHXNmCzdx8T6y4LY8c1Vq801eHc1nMKY8z6LxI-1JkZw-jdcTljYxIpalSRg7geWuEyVPmki9GT4CZM_-sBe-7onsfPBbL43BNm--12z25ywlBA8sbOxnzBOXzmr8vqXju_uPaeRgunPnRO8Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا، روز جمعه با تیم ارشد امنیت ملی خود در کاخ سفید دیدار کرد تا سناریوهای مختلف در صورت شکست مذاکرات و احتمال آغاز حملات جدید علیه ایران را بررسی کند.
در این نشست حساس که با حضور مقامات کلیدی از جمله جِی‌دی ونس، معاون رئیس‌جمهوری، پیت هگست، وزیر جنگ و جان راتکلیف، رئیس سی‌آی‌ای، برگزار شد، ترامپ در جریان آخرین وضعیت دیپلماسی قرار گرفت.
نشانه‌های جدی از تغییر برنامه آخر هفته رئیس‌جمهوری، از جمله لغو سفر به باشگاه گلف بدمینستر، بازگشت به واشنگتن و حتی عدم شرکت در مراسم عروسی پسرش، دونالد ترامپ جوان، نشان‌دهنده وضعیت اضطراری در کاخ سفید است.
منابع نزدیک به ترامپ می‌گویند او از روند کند مذاکرات ناامید شده و به سمت گزینه نظامی متمایل شده است، هرچند هنوز تصمیم قطعی برای از سرگیری جنگ اتخاذ نشده است.
در همین حال، تهران به کانون تلاش‌های دیپلماتیک «لحظه آخری» برای جلوگیری از شعله‌ور شدن دوباره جنگ تبدیل شده است.
عاصم منیر، فرمانده کل ارتش پاکستان، به عنوان میانجی اصلی، در سفری حساس وارد تهران شده و قرار است با احمد وحیدی، از فرماندهان کلیدی سپاه پاسداران دیدار کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/75629" target="_blank">📅 00:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75628">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3SP0ZCThJD70fT3qYIX4bV2fLpdaUQv0Shh2Jrz563KLpOAmLQAwvODFMGTAdsn6KK-GJZ0NDLyFfBDFJf6Eg1mpuqoFk7a55jnXpRFfDRs-V8cUp1sSmJzJlj0mC1naYNbanHuRhnIziI9BNIQ9QMW4tztm7VCgRNGSbrvfdlm8YNoGgddKbDC22CT02eCoVEWSd-KeIOzICYkiOAzSfd2jaJ05fFMHR92tszmNUIsxKVBskU9qG_Nzep9VitH7Mc0yhJZCDclc0Y_om_m_Ct8pTI1jMLtCRTuI2iuDN93YDuDok45CzuTWJMLaK9ERWdAsLwNfsKaSEn4c3j_xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از یک منبع نزدیک به ترامپ نوشت که رییس‌جمهوری آمریکا در روزهای اخیر به‌طور فزاینده‌ای کلافه شده و احتمال انجام یک عملیات نظامی نهایی و گسترده را مطرح کرده است؛ عملیاتی که پس از آن بتواند اعلام پیروزی کرده و به جنگ پایان دهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/75628" target="_blank">📅 22:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75627">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ho79Dcloh8Qle8UD0QmYPgqb3_XMqYaGakJamIKnYQ5XOL1KWLTBse4DuaFMtJCYTF0LikU3rNbNqV5wekQFtoqUSWm1ZdX18LQ2sAKs2i8FF4pQIiz1Y6eukd9xuGj-GxZIqQrXyjuTsIBsi3efue5jSsaya1YccU4dYFONvTA2-WO8fZXsIvsgqzzsxLJCW1dWUdG0GbhoIXKR7yfJgg7j-T5DSO8GKpMcco7p2_PsfeeKP5NqQdgv48hEnedynbxcYOMQrG836CLtsOK2uafs74tuGGgyRSeiEC8nEZzilTzMx9Fci-W34sXLO0nHq9n4mKWKKM27_HPPpomwyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی هیئت مذاکره‌کننده ایران با آمریکا روز جمعه گفت که موضوع پرونده هسته‌ای ایران در این مرحله مورد مذاکره نیست و از اختلاف نظر عمیق با آمریکا خبر داد.
اسماعیل بقائی گفت: «اختلاف‌نظرها بین ایران و آمریکا آن‌قدر عمیق و زیاد است که نمی‌شود گفت با چندبار رفت‌وآمد یا مذاکرات ظرف چند هفته ما باید حتماً به نتیجه برسیم.»
او گزارش‌ها درباره قریب‌الوقوع بودن توافق با آمریکا را رد کرد و اعلام کرد: «نمی‌توانیم بگوییم ضرورتاً به جایی رسیده‌ایم که توافق نزدیک است.»
بقائی بار دیگر موضع جمهوری اسلامی درباره برنامه هسته‌ای و اورانیوم غنی‌شده را تکرار کرد و گفت مواضع ایران قبلاً اعلام شده است.
@
VahidHeadline
سخنگوی وزارت خارجه ایران حضور هیئتی از قطر را در تهران تایید کرد
اسماعیل بقایی،‌ سخنگوی وزارت خارجه ایران تایید کرد که یک هیئت از قطر روز جمعه در تهران بودند و با عباس عراقچی وزیر خارجه ایران گفت‌وگو کردند.
او بدون ارائه جزئیات گفت که کشورهای مختلفی طی روزهای اخیر با وزیر خارجه گفتوگو کردند اما تاکید کرد که میانجی اصلی میان ایران و آمریکا همان کشور پاکستان است.
پیشتر رویترز به نقل از یک منبع آگاه گزارش داد که هیئتی از قطر در هماهنگی با آمریکا وارد تهران شده است.
قطر و امارات و عربستان سعودی سه کشوری بودند که آقای ترامپ روز دوشنبه گفت که به درخواست آنها فعلا حمله مجدد به ایران را متوقف کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/75627" target="_blank">📅 22:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75626">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioXkEgy9vlKO-dk_Va_Fwsh0Mc9S3QnLmdVxRsGknweAHIrgdp4_cPBVvAJkMaYLl-GI-uH6D6BhZBol_eiYH8fV0dHOyQFB5UjUkbfWI-vQqvJIBI0hCOQqzeHrMyTZJCkWGbT4yVhoNm9lkG84d1jqW29kFG1ZDHIbSNZRdY1ACnkA1acfpaL06toxoxltpHAT1rGp3Mbc92Y8IoZWuHg94tEnyizHzj3ptMRYxqqWC87MrHK1Tb5UMLdh20g4wMSHvpBYRjGVlj66sVyeS_5ZcAc0tzunTPKKT9Y_j7dl7MuPOamZjivRPSEx-SpiBU8NoxILFaP03NDWaZhcow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از عاصم منیر، فرمانده ارتش پاکستان که امروز جمعه یکم خرداد۱۴۰۵ وارد تهران شد و مورد استقبال اسکندر مومنی وزیر کشور قرار گرفت. خبرگزاری آسوشیتدپرس پاکستان نیز به نقل از منابع امنیتی اعلام کرده‌اند که عاصم منیر در طول این سفر رسمی، درباره «مذاکرات جاری ایران و آمریکا و صلح و ثبات منطقه‌ و منافع دوجانبه دیگر» با مقام‌های ایران گفت‌و‌گو خواهد کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 229K · <a href="https://t.me/VahidOnline/75626" target="_blank">📅 22:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75625">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Tj6-_Wt2oFQrasv3-VFQlm__SAcLzbd_QzoUMarkAOUnTr0CwOqv7vbuHr-PlY53wGPbfqiNhTRdQA1Pd_2BAefA-8RFvN3FGrGV-nTVdmfP4cW9hhgvcvQPsOvItg1fYOyWod10E5ohM3hMvKcfElUXaFf49MkeliFlJopj7Yn9YHEgnvH8LGJ3UjoO4rh00asfFHQAYBFS5r6C8Ed0SdLoSphY_KkMU0d7X5QEkFbGmGgTtT2Xz3B-Sf9K4T0cUNw0xYsxsoPPfZaTh4EfbrXi5JRzq-Eoy00YruZfWuwXBE6noomUbPcvbjv2dOXaVqxH4evV9rWxITZU9f4eqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«فاکس نیوز»: تولسی گابارد از پست خود به عنوان مدیر اطلاعات ملی آمریکا استعفا کرد.
AlArabiya_Fa
پست ترامپ، ترجمه ماشین:
متأسفانه تولسی گبرد، پس از آنکه عملکردی بسیار خوب داشت، روز ۳۰ ژوئن دولت را ترک خواهد کرد. همسر فوق‌العاده او، آبراهام، به‌تازگی به نوعی نادر از سرطان استخوان مبتلا شده و او، به‌درستی، می‌خواهد در کنار همسرش باشد و در حالی که این نبرد دشوار را با هم پشت سر می‌گذارند، به بازگشت او به سلامتی کمک کند. تردیدی ندارم که او به‌زودی بهتر از همیشه خواهد شد.
تولسی کار فوق‌العاده‌ای انجام داده و دلمان برای او تنگ خواهد شد. معاون اصلی و بسیار محترم او در دفتر مدیر اطلاعات ملی، آرون لوکاس، به‌عنوان سرپرست مدیر اطلاعات ملی خدمت خواهد کرد.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
از سوی دیگر رویترز به نقل از یک منبع آگاه از موضوع، نوشته که او ادعا کرده کاخ سفید خانم گابارد را برای کناره‌گیری «تحت فشار» قرار داده بود.
پیشتر اختلاف دیدگاه‌هایی بین رئیس‌جمهور ایالات متحده و مدیر امنیت ملی‌اش، بخصوص در قبال ایران بروز کرده بود. دونالد ترامپ در فروردین‌ماه هم اشاره کرده بود که از نظر او، تولسی گابارد در قبال برچیده‌شدن بلندپروازی‌های هسته‌ای ایران، «موضع نرم‌تری» دارد.
خانم گابارد بیش از یک سال پیش، پنجم فروردین‌ماه ۱۴۰۴ به کنگره گفته بود که ایران در حال ساخت سلاح هسته‌ای نیست.
مدیر اطلاعات ملی آمریکا که برای ارائۀ گزارش سالانۀ نهادهای اطلاعاتی ایالات متحده به همراه رئیس سی‌آی‌ای و مدیر اف‌بی‌آی در جلسه استماع سنا حاضر شده بود، تأکید کرد که بر اساس ارزیابی نهادهای اطلاعاتی، علی خامنه‌ای رهبر وقت جمهوری اسلامی، درباره تعلیق برنامهٔ تسلیحات هسته‌ای ایران، که در سال ۱۳۸۲ فرمان آن‌را صادر کرده بود، تجدیدنظر نکرده است.
با این حال خانم گابارد بعد از مدتی، موضع‌گیری خود در این زمینه را تغییر داد.
تولسی گابارد که مسیر سیاسی پرفراز و نشیبی داشته، پیش از پیوستن به حزب جمهوری‌خواه و ورود به دولت دوم دونالد ترامپ، عضو حزب دموکرات و نمایندۀ هاوایی در مجلس نمایندگان بود.
او هفت سال پیش، زمانی که خود را برای رقابت به‌عنوان نامزد حزب دموکرات در انتخابات رباست جمهوری آماده می‌کرد، گفت که در صورت پیروزی در این انتخابات، ایالات متحده را به توافق هسته‌ای با ایران باز خواهد گرداند.
خانم گابارد در آن زمان در گفت‌وگو با شبکه تلویزیونی فاکس‌نیوز هشدار داده بود که ایالات متحده در آستانه جنگ با ایران قرار دارد.
تولسی گابارد نخستین و تنها مقام ارشد امنیتی یا نظامی دولت دونالد ترامپ نیست که کناره‌گیری کرده یا وادار به کناره‌گیری شده است.
در آخرین روزهای سال ۱۴۰۴، جوزف کنت مدیر وقت مرکز ضد تروریسم آژانس امنیت ملی آمریکا، که مستقیماً از سوی دونالد ترامپ منصوب شده بود و زیر نظر تولسی گابارد انجام وظیفه می‌کرد، در مخالفت آشکار با جنگ ایران، کناره‌گیری کرد.
@
VahidHeadline
خبر یک ماه و نیم پیش:
ترامپ قصد داشت گابارد را اخراج کند
به گزارش وب‌سایت آکسیوس، دونالد ترامپ تا آستانه اخراج تولسی گابارد، مدیر اطلاعات ملی آمریکا، پیش رفته بود، اما مداخله لحظه آخری راجر استون، مشاور قدیمی و نزدیک او، مانع از این اتفاق شد.
دلیل خشم ترامپ به شهادت اخیر گابارد در کنگره بازمی‌گردد؛ جایی که او برخلاف انتظار، از جنگ با ایران حمایت تمام‌عیار نکرد.
طبق گفته منابع آگاه، ترامپ از اینکه گابارد در اظهاراتش اعلام کرده بود برنامه هسته‌ای ایران پیش از آغاز جنگ «منهدم» شده بود (موضعی که توجیهات ترامپ برای حمله را تضعیف می‌کرد)، به شدت ناراضی بود.
همچنین استعفای اعتراضی جو کنت، دستیار گابارد که جنگ را غیرضروری خوانده بود، بر آتش خشم ترامپ افزود.
در حالی که ترامپ در حال نظرسنجی از مشاورانش برای جایگزینی گابارد بود و وفاداری او را زیر سؤال می‌برد، راجر استون در تماسی تلفنی از او دفاع کرد. یک منبع نزدیک به آکسیوس گفت: «راجر معامله را جوش داد و تولسی را نجات داد.»
استون نیز بعدا در شبکه اجتماعی ایکس تایید کرد: «خوشبختانه به موقع اقدام کردم.» با این میانجی‌گری، گبرد فعلا در سمت خود ابقا شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 232K · <a href="https://t.me/VahidOnline/75625" target="_blank">📅 21:12 · 01 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
