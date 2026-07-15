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
<img src="https://cdn4.telesco.pe/file/pvyes6oSLmGvL7kjfqwqMLgJN8gYNEWZYj60VWT53UzW-qTYwXOkXH4tYxo6VzauMe4kDlde2zfW55iCdwweFWQT8vUI7-gNInwkXGXmA2hTCwVJ_AFZFTzyTIAh-4PbhGo8qHTVg7Pqd0eo770Pa-UrjMnktVfwm9rngEJkNBkxDAzjDOICTLxoEx7_wHEd-_LrdNZozOUSo0t1Gm4cwwkSKun7vI6Uq9cwqRrMRT0r76sr7yU7MH6S2jnRULgKn_R_9vP5xqpvrFH467fldhKLj2usYvqItxAtI2GAdzAu-X7TgRz_i0SV-V77ick3lvUzzsrf1ncUzFH4WgQILQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 21:13:29</div>
<hr>

<div class="tg-post" id="msg-450230">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‌
🔴
قالیباف: مردم جنوب کشورم، شما عزیز جان ایران هستید، جان ما هزار بار فدای شما
🔹
به مردم جنوب کشورم که این روزها در خط مقدم جبهه قرار دارند، می‌گویم که از ابتدای جوانی دوشادوش شما خواهران و برادران عزیزم اسلحه به دوش گرفتم و جنگیدم، شما عزیز جان ایران هستید،…</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/farsna/450230" target="_blank">📅 21:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450229">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‌
🔴
قالیباف: بنده هم در میدان دفاعی و هم در مقابل طراحی دشمن در جنگ رسانه‌ای بودم، بعد از آن هم با علم به تمامی مشکلات و تخریب‌ها در سنگر دیپلماسی حضور پیدا کردم و هیچ‌گاه از زیر بار مسئولیت شانه خالی نکرده‌ام
🔹
هدفم اعتلای ایران عزیزتر از جان، تحت هدایت‌های…</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/farsna/450229" target="_blank">📅 21:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450227">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‌
🔴
قالیباف: حمایت و اعتماد شما به سربازان عرصه دفاعی، دیپلماسی و خدمت، دست آنان را مقابل دشمن برتر می‌کند
🔹
مطمئن باشید آن‌ها جان خود را ضمانت امنیت شما و منافع ملی ایران گذاشته‌اند و با تدابیر رهبر معظم انقلاب و مسیری که طراحی شده، نتیجه این اعتماد و حمایت…</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/farsna/450227" target="_blank">📅 21:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450226">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‌
🔴
قالیباف: برای ما مسجل است که انتقام خون آقای شهیدمان را به ثمر خواهیم نشاند. @Farsna</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/farsna/450226" target="_blank">📅 21:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450225">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‌
🔴
قالیباف: همه می‌دانیم که مسیر دشواری پیش رو داریم. آن‌ها قبلا هم ما را با ناو و حمله هوایی و زمینی و ... تهدید کرده‌اند، نتیجه‌اش را هم دیده‌اند پس نباید از تهدیدهای دشمن ترسید. @Farsna</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/farsna/450225" target="_blank">📅 21:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450224">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‌
🔴
قالیباف:  از همه ملت ایران با هر نگاه و سلیقه‌ای می‌خواهم در تبعیت از اوامر رهبر معظم انقلاب وحدت را حفظ کنند، در میدان باشند و این حضور و وحدت را به رخ دشمنان بکشند. @Farsna</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/farsna/450224" target="_blank">📅 21:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450223">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‌
🔴
قالیباف: مرز بین جنگ یا مذاکره با دشمن، براساس امنیت و منافع ملی مشخص می‌شود و تشخیص استفاده از هرکدام از این ابزارها، متناسب با اقتضای زمان و شرایط، با ولی امر و فرمانده کل قواست
🔹
همه ما وظیفه داریم متناسب با تکلیفی که نایب ولی عصر (عج) معلوم می‌کنند،…</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/farsna/450223" target="_blank">📅 21:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450222">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‌
🔴
قالیباف: باید بتوانیم بین دو روش نظامی و دیپلماسی، هماهنگی ایجاد کنیم و نباید از جنگ یا مذاکره هراسی داشته باشیم
🔹
جنگ و مذاکره دو روش حفظ منافع ملی است. مذاکره در این مقطع همان‌گونه که بارها اعلام کرده‌ام معادل سازش نیست، بلکه در کنار جنگ، بخشی از راهبرد…</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/farsna/450222" target="_blank">📅 21:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450221">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‌
🔴
قالیباف: آمریکا که به لحاظ حقوقی و دیپلماسی دستش خالی است، می‌خواهد با زور ترتیبات ایرانی تنگۀ هرمز را کم ‌اثر کند، ولی ما بر پایه دستاوردی که در تفاهم‌نامه به دست آوردیم، باید بایستیم تا حقوق ملت محقق شود. @Farsna</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/farsna/450221" target="_blank">📅 21:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450220">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‌
🔴
قالیباف: امروز امنیت ملی ما در حفظ «ترتیبات ایرانی» بر تنگه هرمز و عبور و مرور حداکثری ایمن و بی‌ضرر کشتی‌های تجاری از این آبراهه است تا برای ایران امنیت‌ساز شود. @Farsna</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/farsna/450220" target="_blank">📅 21:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450219">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‌
🔴
قالیباف:  نیروهای مسلح ما مثل همیشه برای مقابله با تهاجم دشمن آزادی عمل کامل دارند. @Farsna</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/farsna/450219" target="_blank">📅 21:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450218">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‌
🔴
قالیباف: تفاهم‌نامه زمانی معنا دارد که بندهای آن معتبر و درحال اجرا باشد
🔹
اگر قرار باشد ایران از تفاهم‌نمامه انتفاع نبرد، دلیلی برای پایبندی به چنین تفاهمی نداریم. @Farsna</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/farsna/450218" target="_blank">📅 21:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450217">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‌
🔴
قالیباف: باید همواره آماده نبرد باشیم و در کنار این باید از ابزار دیپلماسی و مذاکره هم استفاده کنیم تا منافع ملی را محقق و تثبیت کنیم. @Farsna</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/farsna/450217" target="_blank">📅 21:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450216">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‌
🔴
قالیباف: آمریکا در هر زمان که بتواند به‌دنبال ضربه زدن به ایران و پیش‌برد منافع خود است و این محدود به جنگ،  مذاکره یا فقط این رئیس جمهور فعلی آمریکا نیست.  @Farsna</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/farsna/450216" target="_blank">📅 21:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450215">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‌
🔴
قالیباف: باید بدانیم ما در یک جنگ جوهری و وجودی با آمریکا قرار گرفته‌ایم
🔹
هدف جنگ ساقط کردن نظام مقدس جمهوری اسلامی ایران به‌عنوان نهاد اصلی جبهه حق و چندپاره کردن کشور عزیزمان ایران است. این راهبرد دشمن تغییر نکرده است. @Farsna</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/farsna/450215" target="_blank">📅 20:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450214">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
قالیباف: باید همواره آماده نبرد باشیم و برای حفظ امنیت و منافع  ملی خود تا پای جان بایستیم
🔹
ما هیچ‌گاه از جنگ استقبال نکرده و نمی‌کنیم اما باید همواره آماده نبرد باشیم و برای حفظ امنیت و منافع  ملی خود تا پای جان بایستیم. @Farsna</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/farsna/450214" target="_blank">📅 20:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450213">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
قالیباف: باید همواره آماده نبرد باشیم و برای حفظ امنیت و منافع  ملی خود تا پای جان بایستیم
🔹
ما هیچ‌گاه از جنگ استقبال نکرده و نمی‌کنیم اما باید همواره آماده نبرد باشیم و برای حفظ امنیت و منافع  ملی خود تا پای جان بایستیم.
@Farsna</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/farsna/450213" target="_blank">📅 20:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450212">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82172044b9.mp4?token=cWltS9Gur_Pgdel9LDfSfIVujp8SQpJsghWa1COlDIVzsLnYV6rvz7r_EKywWDo3KBCho6EJwYHoFLUSN7IEfb5_Kf5e4B0sBBuNuXXgehtTR3VMf7MxtCHT3WD3QSY7CGwP_44jYzuVotP99fmRORi-T26YJOLPK1dxpWx_wyb7KQPoARmbdRLLs1mBF-hCAe4mMQtAE1Lo_u0tJE_g6y6KbtNlIGq7VZ-bBlT1zT70IEf9t2Y89a6-jRSe_UMyTzfV3lmGA6JVbrBExoSjJMyuS9jZ6rwqGOTZRFBDiUUQLJSpkm-mYGfK7fwp81nHAwb5zwu9K2DpSy0xF8Fljw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82172044b9.mp4?token=cWltS9Gur_Pgdel9LDfSfIVujp8SQpJsghWa1COlDIVzsLnYV6rvz7r_EKywWDo3KBCho6EJwYHoFLUSN7IEfb5_Kf5e4B0sBBuNuXXgehtTR3VMf7MxtCHT3WD3QSY7CGwP_44jYzuVotP99fmRORi-T26YJOLPK1dxpWx_wyb7KQPoARmbdRLLs1mBF-hCAe4mMQtAE1Lo_u0tJE_g6y6KbtNlIGq7VZ-bBlT1zT70IEf9t2Y89a6-jRSe_UMyTzfV3lmGA6JVbrBExoSjJMyuS9jZ6rwqGOTZRFBDiUUQLJSpkm-mYGfK7fwp81nHAwb5zwu9K2DpSy0xF8Fljw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکا تاوان تجاوزات اخیر را پس داد
@Farsna</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/farsna/450212" target="_blank">📅 20:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450211">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6de1acb88a.mp4?token=Un1xEuPTfbzTgi71mQImKpeyO3A3Jpxc9t66NXjmEbBhGy7XdwvNemgw-aKt9QqC3NjXxWg9_TEmKw3K1gHqfqNiTZUqdgVIheSVsTiZ2LuBgxXrNdnzQsRvD7lYkzEEVC1sSr64jonc_j3Y2o8HCaWuYVeDv7laY79it5BIXJhbA47xs1Rwo_ZS2A9tWxP9vRzGlDac0wYVCQVE2lHtl-vlLnXG-jx3IqxYCtkcWMz05IuLAcLyELA_Eyrm_n5CNJSizmwcOV_X4pPjnAR-Frmwj4otpGT3VQzFEiiIHrP9sEpOlR8dKJ2uaj6IjAx26aXgCi0fQiu2nWY7HmvDPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6de1acb88a.mp4?token=Un1xEuPTfbzTgi71mQImKpeyO3A3Jpxc9t66NXjmEbBhGy7XdwvNemgw-aKt9QqC3NjXxWg9_TEmKw3K1gHqfqNiTZUqdgVIheSVsTiZ2LuBgxXrNdnzQsRvD7lYkzEEVC1sSr64jonc_j3Y2o8HCaWuYVeDv7laY79it5BIXJhbA47xs1Rwo_ZS2A9tWxP9vRzGlDac0wYVCQVE2lHtl-vlLnXG-jx3IqxYCtkcWMz05IuLAcLyELA_Eyrm_n5CNJSizmwcOV_X4pPjnAR-Frmwj4otpGT3VQzFEiiIHrP9sEpOlR8dKJ2uaj6IjAx26aXgCi0fQiu2nWY7HmvDPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک ایرانی مقیم خارج از کشور: ایرانیان مقیم خارج جنگ‌طلب نیستند، ما نمی‌خواهیم کشورمان بمب بخورد.
@Farsna</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/450211" target="_blank">📅 20:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450206">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XXxcvfWquXSb-pA8phE6UmIqap2DJufpvok6HDBKEtwQ0_k0w6rvSJdlt_lsnVdgQ1ssfo2zrsnmHL-Eo_nXcg24aaxpCVTzcGhw7wyS7PxnxwNbD3QdiJOsP7reRe76XjpHOCMrGW3mLwj5YWy8X5Neh9Te9CJyGV72ivFrQWNxIJouy9R7LJqJzaWVBx0L5x15XLxBYHA5MTg7DLjO3mPE0bdMI4NKNiV5rzhHnV07YI62PCDNy9aFSCU-Yg-ebk9_FZOLSTDqhOneZJgzuQ5keXOzlrDHLsxqVtu5G46qMtGtYwrbnDjzCtuouy0CpLKS-VV5kVLPDaWol8TFfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lZBKLQoDg6cLHZHJn4lWZzipBI6CSVXgGfMsfHtUP40rbgrYUAzrKE5YAb3WeinyWaoydMkfcpqxjzIP0DzCZOvl506ZN_DRauYJWC4z9dCr9pvEOyuFFeLWG-9sbIzmVnHrhosCVn1dtYyo1HKXLz5vxRE0BjvI9-n11QstzdW1w3qKhp1iylO678OpqfkynbibloOONVrw5NWqK6y5To4UrO3Zw0J2xJT4nLBkmrtFIuwZvDrLztIsZu6CgbdOOtd2ji9ipz3-3iw0RXh1BFZrwG9iJ7jJE5BDfdlBdVV8DC4PQynoQEWPbg7XYNyehDub5nc94-5_1h497Eb76g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/edo4VDRzOp5k6YBAEiORk9EMeVWqvfILb1H9rJhHHO1flKZ3XnLeCwgyUIZQlcXDUNgOGdmwhjPrv82gyiyIN6gKaL7u1B1ahisHoN1HPZ4j1BnsXCxQSRr4_YOUVRdeq-EZE9q1Bkw3LSDu792640gCiNAAWzkX7fIZohj1p8JaLOEScVBSbEhTCdxqHPDnFVgDY9KoyB8P6miaZAvsanwGEdRkfj3Xm6WpzjbbdBnjSAuQN03vdeNAYjC4fqxp2CvIyBF522QF-mlWoVs1v4MUAj4-QvuZJmSP_2TkTrKImpEwYe7XNaNFwFWIDEoVGQYBoV9mH7ldDZ6FK4cQYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t1kBsYnEUzZK2hkW0-GFOHSmRfo_HvWkKCJis6ylt1PwP7MM2Nkh4zX7qPMMj3Z2peDUtfRtj4ZgjwJslKb7jA19aOyCRUn1RATCq9124mcU-dh1Ve1sf1CwQ15s3WxLseEii2jvn8svcy6PvqsNMePbPaghhTtWVky5vVy_CdLzmBZ1wE-rWoTGmOzSqN4nXbCcs-Hpadl99L8Y5OYGCjHpBydUM0oPDwLe4cbFBKzQm4SRbsB7gUkiyT1pyA0ff42ka7_rxtFKbZz2Vs164FN8SIcczn7y6uUucO17hA_QheVw3eTaZZU_EEONHI35ZG2UbnEzwhAv5j_s5u-17g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YvxGlYwKObEex528iWhUnXj66c_40VwzfhU4cJmK2brDwvNeS3zCmGKKQhlDUROo-0IMBa7dpjE8HZiAUkTP84AxFPS_Qt0cF_XVtWFjhrUiTuTwlI5GQ3xEKr65L2OPJwr03imWVo-rv6sfHXDJDzKvrIbM7pVbEYZ-wMHqIPIYxTv4NI1XUbapUEOl2tQsDZzk5YC3k5eMQD1KLRrgb4fS-ZR8FUBNRqRJWz13klplPmPSBg1JikuoCUqxVBtXYLGlK-XHu2Q8Yfkp5Z1ZFt1DYHQkGpTJyIsa1MpcVEnOAS81vLGSs-wOd_O4viDFlAjB-r8d6ktUYETAAuBIDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سالروز بازدید تاریخی رهبر شهید انقلاب از پژوهشگاه رویان
🔹
پژوهشگاه رویان به‌مناسبت سالگرد بازدید تاریخی رهبر شهید انقلاب از این پژوهشگاه، امروز مراسم یادبودی برگزار کرد.
عکس:
زینب خدابخشیان
@Farsna</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/450206" target="_blank">📅 20:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450203">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YDe0YVCjadVJ3z9arcw-WiiaMx0tDSvVJVVfcubVmSU6Hs3hUzLHQlZLkmDDqe-_8paLBVuE18egGDVth2Pj1i6O_7ArjRVXwkrU0VixHwjrV0ocWH6CejClYMBmBxnUeDC69ZMAR2sFNxJ-Gv26SKuKheck_IhcQR9lRe1QwDQNDLmY3yM6-qzemXGgqmBVAcVWmD-CoPAbO55-EkdD8dorhOytvNZslxYkmTNz08ZaS7VIBrsFx5IM0vQUdQHgY5mvaWRiGICQVMCiEUDZkhJvcEWlu2fxzSqPYKg3nXJgLywsmDd-fXDKEXVXHwrvyX5ni37TzDlkh0WWXkF9JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TjeDiX-tl0ZMVIWaHMw8tOWn7suhcmEx-zCaGdbK5kRgQAjlXcf4kAridNjGhXL6ZIf_JNahduxBz1A1qt5L6esgK2vc21KVKkGo0VNA13ww8VT49f0WRnQUozE73LC5VYEdp5PQgoxUp1v7xKB82fGSVemZJCOYSnNa8HoOWaKX44YTdbJAmRfvRCk4x_NOuJxZec3x64iG9xq0OCA2lQFIYy_h6Q8FMcu1eziYcc5VDH-bl5kUMJ0_YsWs6KfzUnGI2ao9jNxRIDyaJmiVkHxwAk42lytAoD1R1Nr7jfrWBaMI3o1S6H2IEWi1gyZn1gSPBndwO-4KEX7gGTzftQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k00BEcsbFp9H99kweYg6_iwwqV4JhInvN2IQZyaanra5xJa8Mv9__LbhfPa4BxhRBrXaTG9ANO8ZX3JOI01t6eOy6tjLjBtSeyZNacqvdQeuzHoJT3EeOiys0liEKLPdjCKxYhh1_oIXuy7cd4E2PR23jl0tNJ0WtyZE6M0KTuObYt-LT_4T90T9cL0oIiElYeorDY7VNMvCQCubeY4GbU8uP-M5G8PlEEzZvSIIM0NdXc-K7cy3NnK2BDcBj16vtXwTXg1bpPbLmSxso4vzGub51uDwXCQOQyp5LAWbeYL_FjYaWBiFNVPu3kFivkyf_Hp8Ec9qvlM_dlCXQ9dOMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
انهدام پهپاد آمریکایی لوکاس در بندرعباس توسط رزمندگان سپاه
🔹
این پهپاد متجاوز ساعتی قبل با رهگیری و شلیک موفق سامانۀ پدافندی رزمندگان سپاه در بندرعباس منهدم شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/farsna/450203" target="_blank">📅 20:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450202">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4e887824b.mp4?token=Y75g2GxfYGKXDImkrYwdOfKR0KJ9zLNDmX1cS0YZmHw75IBJezfcE6MmczqEgmrfYAsHEQ5x77fKJawgFu4OKVcaH9hX0eXYEaSLVUaVj-K2S5DWuFQ2ErcSCHeHcohtprKlf2z6VDVWZf4ep_R1y-7qiZ_mIfAhskgL4WWM9pOY2kI6ODbSanmAp9ZrzaKo6bx-2rz8PDZDMWD48cobPfQjPCATXsDQL--3ZK8SAlvRghWO_Xu4Go4MyH6KKyo2k2lE5OYxHuKc4ymmm671BcsvNnxjU1gQed3FBkB-VDufu6LkE8MubnvKlaKJkls_2GLIYh9hS46LqrwpsunZkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4e887824b.mp4?token=Y75g2GxfYGKXDImkrYwdOfKR0KJ9zLNDmX1cS0YZmHw75IBJezfcE6MmczqEgmrfYAsHEQ5x77fKJawgFu4OKVcaH9hX0eXYEaSLVUaVj-K2S5DWuFQ2ErcSCHeHcohtprKlf2z6VDVWZf4ep_R1y-7qiZ_mIfAhskgL4WWM9pOY2kI6ODbSanmAp9ZrzaKo6bx-2rz8PDZDMWD48cobPfQjPCATXsDQL--3ZK8SAlvRghWO_Xu4Go4MyH6KKyo2k2lE5OYxHuKc4ymmm671BcsvNnxjU1gQed3FBkB-VDufu6LkE8MubnvKlaKJkls_2GLIYh9hS46LqrwpsunZkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">والیبال ایران حریف اوکراین نشد
🏐
اوکراین ۳ - ۱ ایران
🇮🇷
۲۲| ۲۱ |۳۱ | ۲۵
🇺🇦
۲۵| ۲۵ |۲۹ | ۱۹
@Farsna</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/450202" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450201">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sj_muH1sl1YADCT7wyiqd8Fh9nkXZRO77yW_X5UOnHKa30ZDPnTAh_7za8Emxc_z9bHYMF-nwSKrceuXj4qWtUfi6D8Y-If9SX4GFPRY0Ab59gl67RzCwUdJX15oMPkLU32TIyN17fDawwlnTOVPs9S7Stb1kOmvspIh8hATPvyulHvhy7-8zjJl-oSvP2WOblTYznQ3e3HBCUWIKP9t_A__h43aMWGdzFIXPIpPedYVi-GL2cnWcZfUyWW2k6uk-JpFLl3DoSMGxo6KnPeFvwnLvDTIc2gPjP_vbiV5Ilpt0kSRY9oJzGMp4TOGJAADxn2aUvHowPgBzTUmUVKjvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بمب نقل‌وانتقالاتی منفجر نمی‌شود
🔹
پس از فسخ قرارداد یاسر آسانی با استقلال شایعاتی درباره احتمال پیوستن این بازیکن به پرسپولیس مطرح شده است.
🔹
بااین‌حال یکی از مسئولان باشگاه پرسپولیس امروز در گفت‌وگو با فارس گفت سرخ‌پوشان هیچ مذاکره‌ای با آسانی نداشته‌اند و اخبار مطرح‌شده درحد شایعه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/450201" target="_blank">📅 20:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450200">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f67045d3b3.mp4?token=hijq1cQO3ORyrRY4n_QHniwboaiG2MUrozYb6PUSkcxaTTe5NpnJ1l3yEM679p2mNcAbtkQpU4lMrOOBKhwg3zCDn5tHib6cbKu_ZvHVh61pcw-5pQhlor-_Pa4T9k3fLGk3h0gsYO7UnCXQ8fcAElh_c4FS26L5QWzeA8HVByzcwIfgFxSROQhBQB7N-3ibGO5zLZnoKfZ6SlrKExv8lvyBU2V3NLyexRYG6nvomwXMGz-0KXvP8WMWzBlTXEtWdjARXGcwUPruhmLmcwm3YxZFn8EMvaLGKGVmYzAOECUXrt42laXwm5hLKJRl1lD7XB00QadKXG32bd0jm0W-Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f67045d3b3.mp4?token=hijq1cQO3ORyrRY4n_QHniwboaiG2MUrozYb6PUSkcxaTTe5NpnJ1l3yEM679p2mNcAbtkQpU4lMrOOBKhwg3zCDn5tHib6cbKu_ZvHVh61pcw-5pQhlor-_Pa4T9k3fLGk3h0gsYO7UnCXQ8fcAElh_c4FS26L5QWzeA8HVByzcwIfgFxSROQhBQB7N-3ibGO5zLZnoKfZ6SlrKExv8lvyBU2V3NLyexRYG6nvomwXMGz-0KXvP8WMWzBlTXEtWdjARXGcwUPruhmLmcwm3YxZFn8EMvaLGKGVmYzAOECUXrt42laXwm5hLKJRl1lD7XB00QadKXG32bd0jm0W-Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اخاذی با عکس پروفایل در همدان و لرستان!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/450200" target="_blank">📅 20:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450199">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">شاهکار دولت لبنان در کسب مجوز برای ورود به روستای غیراشغالی!
🔹
دولت لبنان پس‌از چندین دور مذاکرات مستقیم با اسرائیل اعلام کرد که  بر سر ورود ارتش لبنان به ۲ روستای زوطر غربی و فرون با صهیونیست‌ها به توافق رسیده.
🔹
این درحالی است ‌که یکی از این روستاها یعنی…</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/450199" target="_blank">📅 19:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450198">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3eDG5cDalsdZEkxCo9sFhYyweWuUfEOAxL6USEYSZX7m8ljHdFcdCA0f-nVKpuOD9qtl0mwnSbqB25TS6C9BWSOVtRiUfHJRtbVoxP3VFsnj4Agn18HoBWersnZroMH8nS4vXT8lqZxJzrPHW9RPD52Bwi9fJZTK7sID0bTYE2cwQPjb4qV41HKVMaC_Rz5_bLKBk8NdnzkS9HlD8k3AboaVLwSJb6rphdutY5kYSCaWQD40wbLOMw9ny8JEm3igEUYXp_IP0lUUapP1aJcn4T8xZRvw6sEZc7RCiCW_lTcYIwAoCb5zxJnOxf5_yGx4FgGk6TLqjAhblEYzv5btA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار
نفت در آستانه تهی‌شدن با بسته شدن مجدد هرمز
🔹
درحالی‌که در جنگ ۴۰ روزه، آزادسازی ۴۰۰ میلیون بشکه ذخایر استراتژیک مانع از بروز فاجعه اقتصادی شد، با بسته شدن مجدد تنگۀ هرمز، این ذخایر در شرف پایان است و  فایننشال تایمز هشدار داد که بازار جهانی در آستانه تهی شدن از نفت قرار گرفته است.
🔹
یک تاجر بین‌المللی به فایننشال تایمز گفت: «همۀ ضربه‌گیرهایی که داشتیم را مصرف کردیم. همه‌چیز تمام شده است.»
🔹
حالا تجار نفت می‌گویند که اگر بسته‌شدن مجدد تنگه هرمز ماه‌ها ادامه یابد، مشخص نیست این‌بار نفت از کجا تأمین خواهد شد؟
🔗
پاسخ را از
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/450198" target="_blank">📅 19:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450197">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
برخی از منابع عراقی از وقوع چند انفجار در اربیل عراق خبر می‌دهند
@Farsna</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/450197" target="_blank">📅 19:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450196">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
منابع عربی: دقایقی پیش ۲ انفجار، پایگاه آمریکا در کویت را به لرزه درآورد.  @Farsna</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/450196" target="_blank">📅 19:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450195">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcC8YIVVDeZBoddJ22ZomwL_c23ir9Se_9ag-GI6kFicuD3_8abLvP7cPij74iWp8X3rBppDwPj8uS-BvYMDqjuH8ZaF_X2a3eRpVAWwDdusKfKZt3UOEtbkORgbeZJZqz4OFQyrNUQ95jpJECbMEtk4u7cXk9ovssl5gGi8EzeNiKQ-Z16S3U2eWzSVylXXOzPnQidJM9yfppFwumYvX9YlHTh-EOas_e8HI4TeYCetS0iZXuhbp8iwEO6CASzVdlmLKkF8bjPvo7-QizFNR0a_ruGlBcyPYiTE19w9r-Rxu84-nx-2YqRTODFE2YswghnsB2Ob4C3Ikqa9f6mnZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
لحظۀ بمباران فرودگاه صنعا توسط جنگنده‌های سعودی  @Farsna</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/450195" target="_blank">📅 19:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450194">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
منابع عربی: دقایقی پیش ۲ انفجار، پایگاه آمریکا در کویت را به لرزه درآورد.
@Farsna</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/450194" target="_blank">📅 19:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450193">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otxci66Hx3aFRHHrmVYEX30l3BG2nSCQxwsk7rQajrca0oQpNlUd4JtN0KDL47uSxA8oVdERdtdBa9I8bkfv7o7jr7LFgbEEnWITKLo0wM17Mt71p6hNmEBKiNWmVpUmwAySyiQm2kqJk7lXXtOOXME77bJdUZyELuDQeGKD1bs4Xz7ytiLcnsv1RIm-nb6sDLgd-5TFTYHUlFoPeUdwlIlud-4FS6eN5AX314B0Vrp7zTNBqjY3VcedkXdMlrKqpeLn1jIsBPnOgTvE0ng82h-ZwudvpYsgWGsJNuIxaaH0B1tVBrnj0V9Si1B2cOhikFcILumxW-WPZj21Q3kClA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقایی: نیروهای مسلح ما نشان داده‌اند هرگونه تعرض به خاک ایران، قطعاً با پاسخ متقابل مواجه خواهد شد
🔹
سخنگوی وزارت خارجه: تعهد در برابر تعهد به این معناست که ما تعهدات خود را تا زمانی اجرایی می‌دانیم که طرف مقابل به آنها پایبند باشد؛ در صورت نقض از سوی طرف مقابل، ما نیز متقابلاً هرجا که لازم بوده از اجرای تعهدات خود خودداری کرده‌ایم.
🔹
بقایی درخصوص ادامۀ روند مذاکرات گفت: فعلا روی دفاع متمرکزیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/450193" target="_blank">📅 19:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450192">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iySYdbPOuxRLfbknDSasYmF7bd7OObjO5n6Vvwpy-ahk_-P2tsYGATla-HvSqZIsqDz1tPNOG4F9Zxdz1STEZW0ntn8QTDj5WiIdTMLwAb0cpOvdtZXUc0aapcV2Q1cUQc2TrpoYU9ofDb-sZYZdzCdjWxs9ASH-6oi75ifskwkT1h7C31K-oGW1fjpo9FpdT3Zdzxp5QTapCX8uF1RGvFhj1vssLa8jBlVx0KD909RZItxuspra9mgWTFb7ScozCxwI6u3APk7H5-1dk2X7cAE40s1HtybcVq0Q-rnA3X3qP28Csg6XcKOEC8RKtGF1aqlfUkMGg8lU-L-D4WbLCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسایشگاه و محل اسکان یکی از پادگان‌های نیروی زمینی ارتش در بمپور</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/450192" target="_blank">📅 19:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450191">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/focONh-tuF48Bd-1-7C0B1ysfha9nA56ut36WJO7xeaWTU1gXe28by11AYjXgMhV2NBrSBb2w97P2gQwpr5XI3GM3p0Sx6K0jJ3lOWGQpSVU6Vs1wM0LFacWbNldG7hXB13pWibccNKxoAqnCdIJkM_pXQ5Va1ErKcOCxN_gZpdaLNbP4SHFllwoI3UqHoVcpEJMz-luBGr44uvvcQ61OfrjNeAd5i2vOxzMl3nmdlGP76-CGR024O5GH1ln7HhOpwAHtYxj1FrG2RrJ_HVCScuXC71EK4zncz4PrRd5ostbZVEVILTUkRLxTCQhAxqEq4o1AYOk1azW-m0fWHoX-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۱۱۶ دستگاه استخراج غیرمجاز رمزارز در هرمزگان
🔹
در دو عملیات مشترک پلیس امنیت اقتصادی، دستگاه قضایی و شرکت توزیع برق در بستک و قشم، ۱۱۶ دستگاه استخراج غیرمجاز رمزارز کشف و ضبط شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/450191" target="_blank">📅 19:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450190">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a04aff34e3.mp4?token=RmErsVa8CUAzznxv8jTo5dKx0X4kZ_Sl3RqCZAeobkWcD89e55I6-KB98IrUsh0iQRv7mUMBBpBHr1VM0dVkI_9irpR_R-_dVwfUarCTKSXt7hPAi9toUIwcXvSo8jfPuQMDI4CBwgFwpMRkqQL4jOR8OW_Oe2DKvJje0U5eHn2waLGa5OQU9-ksDImbYF19ZYoXbuhnBlL6RMTeEM7fcGB9njroaZMTrZyGsvdMAWAkIdjeHOAMjH7MnVWT40c5f2FFEkAW0PSpHVuC4z2ksfQ3gzPU0YUYiRIld_jtT1DPVIb1BWdPh8dKlfefXZqtnsulFcqoQg7j8dfssR3Jhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a04aff34e3.mp4?token=RmErsVa8CUAzznxv8jTo5dKx0X4kZ_Sl3RqCZAeobkWcD89e55I6-KB98IrUsh0iQRv7mUMBBpBHr1VM0dVkI_9irpR_R-_dVwfUarCTKSXt7hPAi9toUIwcXvSo8jfPuQMDI4CBwgFwpMRkqQL4jOR8OW_Oe2DKvJje0U5eHn2waLGa5OQU9-ksDImbYF19ZYoXbuhnBlL6RMTeEM7fcGB9njroaZMTrZyGsvdMAWAkIdjeHOAMjH7MnVWT40c5f2FFEkAW0PSpHVuC4z2ksfQ3gzPU0YUYiRIld_jtT1DPVIb1BWdPh8dKlfefXZqtnsulFcqoQg7j8dfssR3Jhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شوک تنگۀ هرمز این‌بار سریع‌تر عمل کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farsna/450190" target="_blank">📅 19:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450189">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92b9bce1e6.mp4?token=d5fg_b8WO6d-pcImt1PomYB0jrLNZMps5IR8AyMwRmp0885CvYG8IEEftkoxLOgqKo_dgKk8EVeH80tFX06S1g5CEhv-f7Tm2Z0pvuHhP12YE21v2fQwRB0jHCTebCzpRf9qjYqoUH4GmKXhhNOlv3ih95kxd4nCopRJBqxeYFZNus1R7kHX4mjQO2yE9esIZjDt0rAQTn0QbDqnE850bdPfd9DmCB5RIxF5ErLv9TpCe66JiAHFWhYdYjt4U7FJz8x1U1s1e39g4yLMKHBpnnaKTR-bvCr_e2iw9ksRCB1fePLCy9djgoCE13CwP9pI24Hk5GshAAjoSbpOXaVtPRm9hUllcqRCb8pLo6KmX2ZnMpJ9eNHPbLQjJOS88TdwufNkmq6Uxs-YYAsXuTUk3KW_GCV7-KAej4lY5lQgRPVycLIB80Wr1QfNMUanIDAzAh2Xn-6CK_vWpsydiulIu5921WTwlOY-n0SEWg8DdKOLK5pbBMQc5PMXktiO4a_anWKMjvmjytc1N2QK3cIQznH6ZcZf10mH4Cm5DavYoAQ3BlgU37hHFxbHJpOzkbs_49w9HrGYCUlWUF6t4m71KgdeD2MQd5olZXhSjrqWr-zOKm6Soql5PQaJLVWemOHITgu5RldHhpo235bvo9_yS_OSYSowVjHF_z_5ylvRQ_c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92b9bce1e6.mp4?token=d5fg_b8WO6d-pcImt1PomYB0jrLNZMps5IR8AyMwRmp0885CvYG8IEEftkoxLOgqKo_dgKk8EVeH80tFX06S1g5CEhv-f7Tm2Z0pvuHhP12YE21v2fQwRB0jHCTebCzpRf9qjYqoUH4GmKXhhNOlv3ih95kxd4nCopRJBqxeYFZNus1R7kHX4mjQO2yE9esIZjDt0rAQTn0QbDqnE850bdPfd9DmCB5RIxF5ErLv9TpCe66JiAHFWhYdYjt4U7FJz8x1U1s1e39g4yLMKHBpnnaKTR-bvCr_e2iw9ksRCB1fePLCy9djgoCE13CwP9pI24Hk5GshAAjoSbpOXaVtPRm9hUllcqRCb8pLo6KmX2ZnMpJ9eNHPbLQjJOS88TdwufNkmq6Uxs-YYAsXuTUk3KW_GCV7-KAej4lY5lQgRPVycLIB80Wr1QfNMUanIDAzAh2Xn-6CK_vWpsydiulIu5921WTwlOY-n0SEWg8DdKOLK5pbBMQc5PMXktiO4a_anWKMjvmjytc1N2QK3cIQznH6ZcZf10mH4Cm5DavYoAQ3BlgU37hHFxbHJpOzkbs_49w9HrGYCUlWUF6t4m71KgdeD2MQd5olZXhSjrqWr-zOKm6Soql5PQaJLVWemOHITgu5RldHhpo235bvo9_yS_OSYSowVjHF_z_5ylvRQ_c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیین بزرگداشت شهادت شهید صادق دروگر در رودان هرمزگان برگزار شد
🔸
شهید دروگر، بازیکن فوتبال هرمزگان، که در حملهٔ اخیر آمریکا و اسرائیل به شهادت رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/450189" target="_blank">📅 19:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450188">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
تحریم مجدد ایران توسط آمریکا
🔹
وزارت خزانه‌داری آمریکا  از اعمال تحریم‌های جدید علیه یک فرد و یک نهاد ایرانی دیگر خبر داد.
🔹
افراد و نهادهایی از روسیه، ایتالیا و نیجریه نیز در این فهرست قرار گرفتند.
🔹
این تحریم به بهانه ممانعت از گسترش سلاح‌های هسته‌ای و مبارزه با تروریسم وضع شده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/450188" target="_blank">📅 19:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450187">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/280a9857f2.mp4?token=YJIzvBUfDwv5HLYoCVAC43yTZ2Zd6w5mwYFkZ-EqWGROHyZrR0Q0DnxrlfV8ZJWIms2tKceBWHOAUz4fPxx6P1wHF7hUZ_iUVpzJDC-MNr8XclcCVZARin5dfDcgtLUN_V3dAZbpNJxAFXqUkFCzrMDtFyQiO3IZMdH0rBQefhKe5h-cVOz6Yd7L5fixJvSiUQaSSqlBIjqK6vaoOMWWH8pbU7PVpZ-esixLLaaRCOvrJ4Lvn6kiE0V6jvmqLCQK67b-ccFDXX5xMHj9zG-8pXI7O45fNuqTCXkl9KMWlFj-BO-lzCcUFKYKsIfjKzC1H3fKJSO4ZDLahpBBDYpt_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/280a9857f2.mp4?token=YJIzvBUfDwv5HLYoCVAC43yTZ2Zd6w5mwYFkZ-EqWGROHyZrR0Q0DnxrlfV8ZJWIms2tKceBWHOAUz4fPxx6P1wHF7hUZ_iUVpzJDC-MNr8XclcCVZARin5dfDcgtLUN_V3dAZbpNJxAFXqUkFCzrMDtFyQiO3IZMdH0rBQefhKe5h-cVOz6Yd7L5fixJvSiUQaSSqlBIjqK6vaoOMWWH8pbU7PVpZ-esixLLaaRCOvrJ4Lvn6kiE0V6jvmqLCQK67b-ccFDXX5xMHj9zG-8pXI7O45fNuqTCXkl9KMWlFj-BO-lzCcUFKYKsIfjKzC1H3fKJSO4ZDLahpBBDYpt_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرویس عجیب والیبالیست جوان تیم ملی در دیدار با اوکراین
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/450187" target="_blank">📅 19:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450186">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">وزارت خارجه یمن: اقدام انگلیس علیه سپاه پاسداران محکوم است
🔹
غربی‌ها خواهان کشورهای ضعیفی هستند که صرفاً ابزارهایی برای اجرای دستور کار شیطانی آن‌ها در منطقه باشند.
🔹
از سپاه پاسداران در دفاع از حاکمیت ایران و به شکست کشاندن توطئه‌های دشمنان قدردانی می‌کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/450186" target="_blank">📅 19:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450184">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">حملۀ دشمن آمریکایی به جزیرۀ هنگام
🔹
ساعت ۱۸ امروز نقطه‌ای در جزیرۀ هنگام هدف حملۀ دشمن آمریکایی قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/450184" target="_blank">📅 18:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450177">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GDSh1OySHh2lJtJC1K5pkKAOdpEykPwkbuPYvBKFsSMaqrCPHfarNOzeULNQyNGD4mLbEnN_aW9_HDZTgf_3L1WCFKUbH-iLZ9c1eeCTsHe7cPPC0avnkxMxhNexVF02kbzNlZvpllXCGglyyl8-TX7n5arnX0RaxIaM3e7-617h4RlA2vgTbU6kpRxFAMXAkyHC33tkzNSUocvTvHybmIwradYsTLHZBBT28dilSGgPKqtiUNAH4KXAXmHKI9MBgxcZxfCwcV2ApV92Ifj7aRQm8Qo9uCIwv3wVzKeabjl-Fithzgp2yrN7I1Vfr3NzAHDSF6Crlxc7AJaYbIXDRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uBRzUCRRxCAXD3Bj11cmKj8bTVAoYHwxSBQhWwwdxbFz4P-JhqqxHtdw0DIpnKDbKYyj-fPDRDSYc2ejq3WoRNKH3gPoYJSC81ht1jk3YB4MsaOOAKo9iPHHphk4jpns8xH8dZYzrJDrazh6vs26UGn-uBTe4fgs1Jpmp5d8a-4mhfRC4SKQKT0NFx3CgBnhhkDa5ihXUIfzF2bKXV7UfeQOvF6FdfEQhlas9e08bw7sFfFPGgG_jpmzdvqKixV4Mohb-vBPSiLxsZ9VItTH8EjgkBoRtLmyZFcI-9XnZ95zAexa2DQFDf1qmKAPutGeT6QJh-XnwFAbiuUC_KSsrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gunWHJSGoRLjTGpNJaGHNOurur0puvYw8xVO8798AOVLDX4BlZBm1DJKF37sRLXYN1Rln16usVgqad0EHqrpJ9p4uoqHRdQnaZkCLfAuWdYVlsNxzt51IciVH5LdjmQSjbmFWZm6k_IfGFjroEHXL2usOdHE20ITuifyFtS7W2gF9nKXjadJQqAizbVqCCLv_sRMtbAxgA2T-F0LpOKw0pjxvM8Qtc2Q1XDja-DciURdI7gAGcMJnw6rjpYH3ujf0raNkdZHg2jD6Ohw-dlXt1yd-M4z7YoZK7mlov9hdufiqzEm_F-hYA9ELL8U7UNlT_YdT6i18EthvNNl7jDwFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qwtHPffmkWoeuUPOvfjuiZL3MRrRx2rhJU1HR-cyNG60qEGYYG1dZCSgP7lJvcFmX2KuRKgkBW23etQcrFfRcWru3ixctqRL2SbxW-8s89TV-Hz11r2Qh__hgX33VZvfjpZlX0fL7KA4Cdwg1KG5QzbqEgHxASdV8-g3NSArwBekH7l5iL6XhL8K7Qh2X2mgfDud0-mQr6UTf73YhQFVf5hbrMbIXQ_GeEhCiylBhqwiD6fkOEiwwzjBq79hYsjcvZtcjYmbW2COo93e_ZLbRT-69eh6z8xp7Ec2YdCRjXvVSxI-lmshdRE-cKo49ylM357T8FKk7B98n6IqLH2MMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rnHx8O9Cmm2bMVxhH438pR-AeGTAAdq0SAvPDsU19nhR8-EMLZHmKwHEoT0hEaOUzWLbhA7vgr36QX4fdNhiBr3G5rYBsPEq5PLAwtxxcm8Vis2Qy9kuPr-7n80647gWwl8R9s_jJ1uitMC__ciM955cFqpqUNNPmBbWSnAMx1uS4OFeOGY3Ct7Mq7sO6uKEbXfXK8sySnZ_TrpLagLlWIw-6_1N8tZOOsJwH7Y5FM7o8A3ANk2I9Pfl9YK_uARds-VZVKP-WwQLjb2k7gQSXfGAwP9zl3D2UBRDSKfQ29FhtWhsTIcsR1M4ny49jRZiUc5boKHTug-K-pHxSp7UBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LVnHCzxnTR7RoueIMCfDNBUGv-HlaPOcf5Y69ZjSj1mdSjofbOb8nkVbRlKfLOpbxazgbV7QDsAobtlFfrynxv_uS0VPCSjTxdlDKAjB6sHuSHWpJMpt760Oy0V1D6zww3AYirvm9w-zzqvZw_thmoZNKaL8IVRfJ4JMzDi-7NwnuBjo9rPwVrJ0i9eEIE1cmeHtXE-ccHVlYuh5QLchxsM-YRgcpzPnnzNpR_Lj7XFp1OU-gMp1eGJH44daQeU6fxpkQCGurHOIxsLFsjEigtf4pcUsrFbtN19EeDflLEdq3UgLtb64SbnLPp7BRRq7Ax6RT1RYQyOPvUM_ZVHsYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AinRZid6fB3ya1ggtJoBPq2OiV5dlrlEv6AIxRftCflTtqwTiZJdBvxdzS-ChMbgFgyPtqBGwNmO8COs5FQP7V7ESM1WQH7DXNE0wlnDhSScdqvAMOCoyah5kHomNjx5ZqhTEKJjNmy__4F7ZX7AsSWm8vVzr1dAPMZK0qlKezNQ__GAoQ_6F3Da3Z80WC6Smcl_arCfsyQBXaXwcjAZmU6qwJUFf1OfST8SPErO_Mh-zsh2UuK0kOi9ER8xQtH2QmbfVdnN85nCzY975ycKmTvOIFFFQWZTzMiTsb900C6my7zE6P05IesrE_Bal_I9JITR37dVS-njnpZAT56VCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
خاکسپاری مادر داریوش فرضیایی
عکس:
الهه آسیابی
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/450177" target="_blank">📅 18:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450176">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVFqcAL45hXXxRIKLsrzVnfgkK30wmv3wWjHsIZebZThP151P1dv5DIEUC4jyzBDLTGkjSsoUxE_dJgMAou8fADHMJvkotq7SRaoFt3_tjJT-MNeUim1Psx6JLEQIQBd229n_NJdhfbkd2gsOWT81rhYoqHHfMzJq7CLvZh62miJkX-9e4ZP-h9hQmIITjI4sJFRXF0n76n52bSJtVTlmAElg8UKKYgImui5neWs4KJ6R5y5BNY1z6uYgr6kQU55L1-dQZwS8zwvZH5vQIjSskgReIqrjiGJShztolJzWrNqnhEdB4grnGgF14KPLIVcvW1aOyD-BIDHy5V3nkrhpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
توصیۀ پزشکی برای این روزها: از ساعت ۱۱ تا ۱۷ از خانه بیرون نروید.  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/450176" target="_blank">📅 18:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450175">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMqIiOX3t2B5qwhj4EGe2MXWbMLvsTenZr2B8pOdFs7An8c1WdXQrLxFsdX186SKYQ_0C7M0q9K3ukOMpBUHGYfkhFd4BYi-gbg_qrTRxS4pQ3IcK4kmC0LHWM8ZGv7Hkeqsv5CfafVBUNDDcdloz_tM5qZGDpTVRszaozcjHmEsSRujpZ6S7DV2vQ7tDKOobhNPqqL_6r_S3JV0QMvbqpHcm4g9Zev1D6d_8baiFyIk1-JExIO-_KlOhS_pRT9_S596WC4BogA-GNIQbVfp6jyKL62h3GS4z8U9HLXEcZGHrnCyNmXcvGh1z0jZL9eVQtMp0UJhyA0bLwj7XVEsUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلیلی: خون‌خواهی امروز ملت ایران یک مطالبه جهانی است
🔹
خون‌خواهی‌ که امروز ملت ایران آن را فریاد می‌زند، صرفاً یک مطالبه ملی نیست، بلکه مسئله‌ای جهانی است.
🔹
این مطالبه، دفاع از حق همه ملت‌ها در برابر کسانی است که به خود اجازه می‌دهند با نهایت گستاخی، حاکمیت ملت‌ها و عزیزان آن‌ها را هدف قرار دهند و به آن‌ها جسارت کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/450175" target="_blank">📅 18:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450174">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a64bc46239.mp4?token=ss4JIGNAuKL8hbCljSGklZQDbe6Z39wHN2wrCpvKX8DucF-hkAlmoYMSMn1SS8JNsQZrvftt1PUxr99RfkNxqJ2gZPuIKx2HK8HmSUby6nFIbv52OjFLQ0Bc4AJ7j_Fz2MKrEda0eDleO21Y8pKVgR3Jcf8LrQtX7O9qCSgqxKo_HYJuEzhldc6ILEWhKvpcE03Vgq76vSCZU0f1Da-cJ9nSJ58etUlykPsTK_jocKwEt8X_VCeR7sjjkzmuPmZApp1ql8ZkVyA6JIDBqZ4Kn2-qdrkYOc9-LueloXl2xs_p9b-drZOiR3dyhFes6epWB8LdiTpRFnHzzyj0_6oqkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a64bc46239.mp4?token=ss4JIGNAuKL8hbCljSGklZQDbe6Z39wHN2wrCpvKX8DucF-hkAlmoYMSMn1SS8JNsQZrvftt1PUxr99RfkNxqJ2gZPuIKx2HK8HmSUby6nFIbv52OjFLQ0Bc4AJ7j_Fz2MKrEda0eDleO21Y8pKVgR3Jcf8LrQtX7O9qCSgqxKo_HYJuEzhldc6ILEWhKvpcE03Vgq76vSCZU0f1Da-cJ9nSJ58etUlykPsTK_jocKwEt8X_VCeR7sjjkzmuPmZApp1ql8ZkVyA6JIDBqZ4Kn2-qdrkYOc9-LueloXl2xs_p9b-drZOiR3dyhFes6epWB8LdiTpRFnHzzyj0_6oqkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: شاید تصاویر حملهٔ آمریکا به مدرسهٔ میناب با هوش مصنوعی تولید شده باشد!
🔹
فکر نمی‌کنم کسی بتواند با قطعیت بگوید که آنجا چه اتفاقی افتاده است. @Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/450174" target="_blank">📅 18:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450173">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZsTH3Vim7RG8U0E3IJmxhjk9itBgsI2eRfcB1j-IVXwVgfFsXEpPDsy2-3nVNLRt6Ym4GRmwCpP1Qh_Q08zKj28S3ulfC6BO5oUJt1_RSDsF9iXUC44GVT5eTRq2VZk3_rhTMkRN-O0fqep_QVbAuTWmIZiTe6obkECaEbenUngtPNmnwBC2RvANw2xP-LCCcI81dLO3jGfx79kln-tlFRuJuFbG-GFER_v_40HiDpNQQcO1yMjC5NJ_ukzmJttGr6jaa1dVFc_6HfyvRQqcgawqnhk7xf7J-SfvqHpVMkXvLYZhNOYhqARLe94gPoJuf6YQQFSBBy3f1-WQaxe_SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهکار دولت لبنان در کسب مجوز برای ورود به روستای غیراشغالی!
🔹
دولت لبنان پس‌از چندین دور مذاکرات مستقیم با اسرائیل اعلام کرد که  بر سر ورود ارتش لبنان به ۲ روستای زوطر غربی و فرون با صهیونیست‌ها به توافق رسیده.
🔹
این درحالی است ‌که یکی از این روستاها یعنی فرون اساسا تحت اشغال قرار ندارد!
🔸
ارتش اشغالگر طی مدت مذاکرات مستقیم با دولت لبنان همچنان در حال تخریب منازل مسکونی مردم لبنان در مناطق اشغالی جنوب است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/450173" target="_blank">📅 18:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450172">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkLdJOit-L_jEBIsqz5Jr3jk5q68CPagi5BvAfKgpZ_Ki2w3Fi6nDsMovhcut4qFYN01eNVR2kMpn-JDj3Muak160gWKc4rumLmYotM2uvQanhPYa0X8ma5D34Ji61zfL-EtCqj4Tb0rQUcevTwQOs7d0WEHd8nVl_cLWDk6ELP1tP4siGNyVeifT4elZO-FypSe42FzjXeseRHuoz8D1VsdtDvIoCOZv5y2ecmqsgkCmbE0KuXmd4_TfDhXf2_WyNMBL2VnepvHLdQn-GkpkGIl3YTeNGYTXV6T8XS7FmvEg-FFfWy4M9xCPg_iBy7fjR1NtDzs-MBxQDEqDiPoQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصباحی‌مقدم: خون‌خواهی امام شهید حق ملت ایران است
🔹
مطابق قرآن، کسی که مظلومانه به شهادت می‌رسد، خداوند برای ولی او حق قصاص قرار داده است؛ این یک حق الهی و کاملاً طبیعی است و البته چون ایشان ولی جامعه بوده‌اند، خون‌خواه ایشان ملت ایران است.
🔹
این مسئله باید هم از نظر حقوقی و هم از نظر حقیقی دنبال شود و نباید چنین افراد خون‌آشامی به‌راحتی زندگی خود را به پایان برسانند.
عکس: مرضیه سلیمانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/450172" target="_blank">📅 18:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450170">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETHzo9R2dRJYj13-ibS4sENEZgnTNiZnFyVF5puxmETZv9ttTI4urPEmsD4nxj8w2n13JglwMWDdCaKxO3f3kyfjL-wUAOqB_iiaXMJw8rGSKUtYJn6S-PRl4rYDFJE33CvpddFVIBN2ReDLPrCPBEtFWKNbY-7m2QDXhxfTER633f557Q5GynP2WjCMLAlHWRcY4qgjxchtNSTZFaft86Ic0IELV22JU3-2zdPlLDl8uS5xUL40iBMt81BP6DwEQpAA4Cfn6kllWOorkB7yli7KlX_-YhuYp5DjLqFYB9frvFVMAinRz6FQ0XaetDZzO20GAAos6yhSe4hZCBU5Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنرمندان کنار ایران ایستادند
🔹
با ادامه حملات آمریکا به مناطق جنوبی ایران در روزهای اخیر، موج تازه‌ای از واکنش‌های هنرمندان در فضای مجازی شکل گرفت؛ واکنش‌هایی که عمدتاً با محوریت همدردی با مردم جنوب، تأکید بر وحدت ملی و محکومیت رنجی که بر مردم این مناطق تحمیل شده، منتشر شد.
🔹
واکنش هنرمندان را
اینجا
ببینید.
@Farsnart</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/450170" target="_blank">📅 18:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450168">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fb2295736.mp4?token=RyJUqF2W3vedy76h-iltnu5R0TC2BPrhAbZdpxn8vayOPtbWweMzgx8pIVMqJ0yfzwZSPvijSIbY6i4YHuW8zXbRYroYh2euRRZF0aOdotWnU77J_tTeC9kSkdDqAW9PW9CDYUs1oUv8VX4Bu1szMpfHKU3ZmYYuxxrgaWGkQ9VyOz4htLXMPrZtykQ-kg8UNDGfKLu3RdqE98TsoeEvxy-A-InN5gC0p-W5hF7_40yqRSmHQY3g1QxJ9CdeGxXWc3IeD8dCUwQEk5qD-bS6Ls0K11A3VDgDiX3QtHXbXD2X6flss4St8RKEI8iyGqu2bK5zc98jmo1iDKiXeBTBIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fb2295736.mp4?token=RyJUqF2W3vedy76h-iltnu5R0TC2BPrhAbZdpxn8vayOPtbWweMzgx8pIVMqJ0yfzwZSPvijSIbY6i4YHuW8zXbRYroYh2euRRZF0aOdotWnU77J_tTeC9kSkdDqAW9PW9CDYUs1oUv8VX4Bu1szMpfHKU3ZmYYuxxrgaWGkQ9VyOz4htLXMPrZtykQ-kg8UNDGfKLu3RdqE98TsoeEvxy-A-InN5gC0p-W5hF7_40yqRSmHQY3g1QxJ9CdeGxXWc3IeD8dCUwQEk5qD-bS6Ls0K11A3VDgDiX3QtHXbXD2X6flss4St8RKEI8iyGqu2bK5zc98jmo1iDKiXeBTBIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: شاید تصاویر حملهٔ آمریکا به مدرسهٔ میناب با هوش مصنوعی تولید شده باشد!
🔹
فکر نمی‌کنم کسی بتواند با قطعیت بگوید که آنجا چه اتفاقی افتاده است.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/450168" target="_blank">📅 17:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450167">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd12106af.mp4?token=NTedZOU1-KeYMMJ24X8OzFyEJ4PMuT8OQWzWGNXdKY2UozP-h8Xxc3VPBclQVPvxpIKJzMWB_6FvHsSp76tzkzn_kJAzpDLV5RqV_mon_klRm7GerAmgh1CwqLqu9rJWQd6rOUVekIZWdyjggNHw8W-8dnvs37ixgsKLZHJfbANTTPAncmobsmVYSF6l-HiPiaxpqzOvL74Rb5eiZUYamUPPd3mDx0i_DVGHKp59SaJXyMSP7yTPw5gfuI6qf1uuntDvzr5h85O3McpBxLbwSAJVYUU08Fp2oxGUDfVjXSFJ3ivG428hjo7d8eF_KC9IMv78OTPbonEYM9K6b3fEWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd12106af.mp4?token=NTedZOU1-KeYMMJ24X8OzFyEJ4PMuT8OQWzWGNXdKY2UozP-h8Xxc3VPBclQVPvxpIKJzMWB_6FvHsSp76tzkzn_kJAzpDLV5RqV_mon_klRm7GerAmgh1CwqLqu9rJWQd6rOUVekIZWdyjggNHw8W-8dnvs37ixgsKLZHJfbANTTPAncmobsmVYSF6l-HiPiaxpqzOvL74Rb5eiZUYamUPPd3mDx0i_DVGHKp59SaJXyMSP7yTPw5gfuI6qf1uuntDvzr5h85O3McpBxLbwSAJVYUU08Fp2oxGUDfVjXSFJ3ivG428hjo7d8eF_KC9IMv78OTPbonEYM9K6b3fEWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شیطان از شجاعان سخت در وحشت است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/450167" target="_blank">📅 17:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450166">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">زلزله گرگان را لرزاند
🔹
دقایقی پیش زمین‌لرزه‌ای به بزرگی  ۳.۹ ریشتر با مرکزیت انبارالوم آق‌قلا، گرگان را لرزاند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/450166" target="_blank">📅 17:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450165">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YU47fdffGQ-e6BTKMpn4BqhPyPmGvSY_TexfD0JHSAspdsAfBZ157nwQse9Zf-Mbum59VZhgvvQol-F6xe28RVbsPPyKstFKr0SAGNhFnDiYk4T0fF-OoFGQBhNa8Q-rW_pIuR8sakVAqVqSKwjVY6PLEUu4CrAj8tanS02UJNwWyJaYt2iSydJpSXNyM6QXu-E28szQeTZhQI-TCZogbLfqPy_vCm--xEAlKQLS8vtaWrXgC4tVuKYqImKFBJaTvRv5glxpmQ5NygWTSROduuREItEvchO1n57LgVw0VGrc6B81oRTGuUboLCzYuAXg9FpJ-z4NSm35L1WJQrUz5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیخ عیسی قاسم: مذهب شیعه در بحرین با تهدیدی وجودی روبه‌روست
🔹
مذهب شیعه در بحرین، به‌همراه علما، خطیبان، نویسندگان، معلمان و مبلغان دینی با تهدیدی شدید و وجودی روبرو است.
🔹
حقوق سیاسی شهروندان شیعه در بحرین و به‌طور کلی حقوق شهروندی آنان، به‌شدت دچار فرسایش شده و روند انکار این حقوق به شکلی گسترده و نگران‌کننده ادامه یافته است.
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/450165" target="_blank">📅 17:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450164">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4MJExQnZJAdo_R0E4bQnJPJfso2mZemRAQVf31-qIkuix43ud_WFnsnTwUkBce7Q06o9t9v-syhooYATrNwG5ulldfTOrUxsoQpISw5HdrLZcDSM3OeZXAZrHKxldt5tHcV6f25KSn7uVr3x6ECssDzn-uGZ5fNGxu2lUmxJJNF5zh0y0re5RfHkcu2L3K0yK1TSgxy4GN4hs14ScaPMyQWnnw7xI6JfCytdp3Ge3p56jN2JfgK6tUps658dcMRZpHNB2BxzVHrdZubpAqGGGKAgY0pnE5SazeTf7u1IyMl30DtoRy0O5GN9_Fnak8Mr7yDdk3193JDOStNColaaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مواظب میزان این ماده در بدن‌تان باشید
🔹
منیزیم یکی از مهم‌ترین مواد معدنی بدن است که در بیش‌از ۳۰۰ واکنش حیاتی از جمله تنظیم عملکرد عضلات، کنترل قند خون، فشار خون و ترشح انسولین تاثیر دارد.
🔹
بین ۲۵ تا ۳۸ درصد بیماران دیابتی با کمبود منیزیم مواجه هستند؛ مشکلی که می‌تواند باعث افزایش مقاومت به انسولین، اختلال در کنترل قند خون و افزایش خطر ابتلا یا پیشرفت دیابت نوع ۲ شود.
علائم کمبود منیزیم:
🔸
اضطراب، سردرد و بی‌اشتهایی
🔸
گرفتگی و اسپاسم عضلات
🔸
افزایش فشار خون و نامنظمی ضربان قلب
🔸
اختلال در عملکرد انسولین و متابولیسم قند
مهم‌ترین منابع غذایی غنی از منیزیم:
🔸
اسفناج و سبزیجات برگ‌سبز
🔸
آجیل و دانه‌ها
🔸
حبوبات
🔸
غلات کامل(جو دوسر، برنج قهوه‌ای)
🔹
متخصصان همچنین رژیم مدیترانه‌ای و رژیم DASH را برای حفظ سطح مناسب منیزیم توصیه می‌کنند.
🔹
نیاز روزانه بزرگسالان به منیزیم حدود ۴۰۰ تا ۴۲۰ میلی‌گرم برای مردان و ۳۱۰ تا ۳۲۰ میلی‌گرم برای زنان است.
🔹
در صورت تشخیص کمبود، مصرف ۳۰۰ تا ۵۰۰ میلی‌گرم مکمل منیزیم فقط با نظر پزشک و در دوره‌ای ۹۰ تا ۱۲۰ روزه توصیه می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/450164" target="_blank">📅 17:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450163">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مصوبهٔ جدید مجلس برای تشکیل جلسات در مواقع اضطرار
🔹
نمایندگان مجلس در جلسه علنی شامگاه دوشنبه، طرح اصلاح آیین‌نامه داخلی مجلس را تصویب کردند.
🔹
براساس این مصوبه، در شرایط اضطراری و خاص کشور که به تشخیص هیئت‌رئیسه امکان تشکیل جلسه در ساختمان مجلس وجود نداشته…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/450163" target="_blank">📅 17:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450162">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDmUTt5BAW0bI26H45RH21RcnaQX8iPa81hRaeSsAd-v7uPGEixVdNNYXcMfR5WtV9ef3ytor_lvfplQ_jWT4aaQDwLOD2KufCAzpwOH6qyhaHS_u0dJVBMbz3hJHXMVPU3VCt6zWUZhM2dFKzb90pkKsAFUsMj2vcLg7o8GgjbJrpme3KBThpqCAwQNBX0O3VRmYa02UinJk_TLQ2P1yPoKTOQPEzdluk0nGuLJaHMGG1SL1AEpRmILy_o14_BuztAyTIU-_y0jm8rdLjxeC7-GP_JY7eG3Ec1TaqRJ1ocx6bRxN5gWnnHP2964v5LCIStL_ZvZwZgB4R4W9Rckag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فینال جام جهانی کش می‌آید
🔹
فیفا اعلام کرده بین دونیمه فینال جام جهانی به‌جای ۱۵ دقیقه ۳۰ دقیقه خواهد بود. هدف فدراسیون جهانی فوتبال از این کار فرصتی برای اجرای خوانندگان و برنامه‌های سرگرمی است.
🔹
فیفا این ایده را از مسابقات سوپرباول (فینال فوتبال آمریکایی) گرفته. اقدامی که پیش‌تر با انتقاد برخی فوتبالی‌ها روبه‌رو شده بود. آن‌ها عنوان کرده بودند که برای دیدن فینال جام جهانی این مسابقه را دنبال می‌کنند و نه دیدن اجرای گروهی از خوانندگان.
🔹
در فینال جام جهانی باشگاه‌ها نیز که از قضا در همین آمریکا بود رویۀ مشابهی پیش گرفته شده بود اما در جام جهانی تیم‌های ملی این اولین بار خواهد بود.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/450162" target="_blank">📅 17:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450161">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-owNSIK58XAVfIDCncpX6Lyeu90jLlDNF6vRxIQr7w-ab2yiPRI-WHkv0J5pAQZaOE49PWRnMHpVejhssNp_utaNLATBkU85g4ovk3IsENlnXplCvO6oYvqNi-SpcSaKhHyRT69vdj9mUtPphx4RWT02ffnnsSek5cnoPSCfOu_Q0xu_Db5KH2cq1oMqbMiut2AoScv307ZdIuQS1jNvNglprKbVeCxIVQUeVc2Syb2RQqm9Yv1zkPqhkiJ7R5JwPHM3EKvb9eheBXlbXgn3mOxvK1YTtYBt5wIvC1oQ0p3yhXPyVa-vPcz-Y6ytQRNCqSpQlJLUsN852qHvbZ5DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۱۸۷ دستگاه ماینر غیرمجاز در استان تهران
🔹
شرکت توزیع نیروی برق استان تهران: ۱۸۷ دستگاه استخراج غیرمجاز رمزارز در دو واحد صنعتی خاوران و شهریار کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/450161" target="_blank">📅 17:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450160">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f32bc93599.mp4?token=ZcqR4dYzn4OcKa25E1stxr_gOMajt63MYVH6fvw3r3ONEGA132OCUTjqrRwRRjdv3rPo4sKXWax0SD3nLnURHh88OXvY3LCPkB7VdgdQn7P6Cn0jafEZwBWso_y1kcU8zrNi1NVHGv2piX5iDQ2P99G5EYW2Zu7SPWDfOQWN9vpUebWE_-ZJ6SjaClTpBqlgOjJzyQ_dY6974-0Gg1ncp2nDr6q6O6WtLZg799CzTK_hTCNMJ2eQMw1iir5A5G10rTrzsFaKLnOZlcBqFGCU-86XE_T4VUinC6EgsB54qSotCqbMUqkSIkvqGlpUfwxBtI4kgaglXYNA0GGKWumdyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f32bc93599.mp4?token=ZcqR4dYzn4OcKa25E1stxr_gOMajt63MYVH6fvw3r3ONEGA132OCUTjqrRwRRjdv3rPo4sKXWax0SD3nLnURHh88OXvY3LCPkB7VdgdQn7P6Cn0jafEZwBWso_y1kcU8zrNi1NVHGv2piX5iDQ2P99G5EYW2Zu7SPWDfOQWN9vpUebWE_-ZJ6SjaClTpBqlgOjJzyQ_dY6974-0Gg1ncp2nDr6q6O6WtLZg799CzTK_hTCNMJ2eQMw1iir5A5G10rTrzsFaKLnOZlcBqFGCU-86XE_T4VUinC6EgsB54qSotCqbMUqkSIkvqGlpUfwxBtI4kgaglXYNA0GGKWumdyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ریک سانچز، خبرنگار آمریکایی: جنگ ایران باعث سقوط ترامپ و حزبش خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/450160" target="_blank">📅 17:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450159">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENZ_BXPpx06VZetRgA67Q24T0srmPi40u3JBq5unIOCc54Dvzoe7X2znDli43ezqCUP6SLmX1SzgjNKOtzvGtqwlMRD9bEDeCrs_GVKtC20EGw7VZmVXma0CaIDYk9dAAyWdND1vVd-N2t9yVfKpTacD5nNQ9Fb-fC19vwu_iA_xDZN1S0RbhWUN7IBp4B_60vTxgp_-BlZnCiNiuH6omkfiPROk0pRpbJ4shhcJVE15OMTPSslpL0USmqeQ6RdHFgRenwrbfVGggJkrKPmfoG3wEQAuNN8cgN3-0srOzdnaktXCzfwSwmkc8zH9KKvZNaYtwA4kGZJX7lt7OvxSzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کارت
رفاهی متصل به اوراق گام؛
👈
خدمت جدید  بانک شهر برای تقویت قدرت خرید خانوارها و کمک به تولیدکنندگان داخلی
⬅️
بانک شهر در راستای توسعه خدمات نوین مالی و حمایت از تولید و مصرف، از ارائه «کارت رفاهی متصل به اوراق گام» خبر داد؛ ابزاری که با هدف افزایش قدرت خرید خانوارها، تسهیل تأمین مالی بنگاه‌های اقتصادی و تقویت گردش منابع در زنجیره تولید و مصرف طراحی شده است.
⬅️
به گزارش روابط عمومی بانک شهر، با هدف توسعه خدمات اعتباری و بهره‌گیری از ابزارهای نوین تأمین مالی،
بانک شهر
«کارت رفاهی متصل به اوراق گام» را به عنوان یکی از خدمات جدید خود به مشتریان ارائه می‌کند.
⬅️
کارت رفاهی متصل به اوراق گام با ایجاد پیوند میان تأمین مالی بنگاه‌های اقتصادی و افزایش قدرت خرید خانوارها، امکان خرید اعتباری کالا و خدمات را فراهم کرده و می‌تواند نقش مؤثری در فعال‌سازی تقاضا، تسهیل مبادلات و گردش
منابع در زنجیره تولید و مصرف ایفا کند.
🔗
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/450159" target="_blank">📅 17:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450158">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس‌ پرس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKkXiWGbSY5ZZZ6imqMgXDHpF4etg2T99yD-BskV6JKvmLISvqh9Y9Tl2Nvrx2Mod-AM8D5WuA2nE8aJ2wYXtUSF5_hbnlIbX-d35ISoyAYBcEnbA-OdFNqbDQYBlpnImEJHsu5AgftieCfk6iNvrmnPg_8T5cKv01Lwtu33uy68E329AxJOd_Cwl___sR2mLBZKL7QkdIDw-qVG-eup9a2a-cC_BYNj7xvfOBOyeoafFwZlOEG-QC3rI-T7LkXa4fT7OWl7VNkl0bf_h36KGwlgnL9lmHZV0aQmIbYvdMpLQ56lTGYWS9W25B-drMbYpI3wE_4yrtxjSICWlHk35g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
بررسی عملکرد سه‌ماهه نخست شرکت ملی صنایع مس ایران؛
🔰
تولید مس محتوی از ۹۲هزار تن گذشت/ تحقق برنامه تولید با رشد ۶درصدی کنسانتره
🔻
شرکت ملی صنایع مس ایران در سه‌ماهه نخست سال ۱۴۰۵ با ثبت عملکردی فراتر از برنامه در مهم‌ترین شاخص‌های تولید، موفق شد تولید مس محتوی معدنی را به بیش از ۹۲هزار تن و تولید کنسانتره را به بیش از ۴۳۰هزار تن برساند؛ عملکردی که از تداوم روند رو به رشد تولید در این شرکت حکایت دارد.
🔹
شرکت ملی صنایع مس ایران در پایان خردادماه ۱۴۰۵، با تحقق اهداف تولیدی و ثبت عملکردی فراتر از برنامه در اغلب شاخص‌های کلیدی، سه‌ماهه نخست سال را با دستاوردهای چشمگیری پشت سر گذاشت.
🔹
براساس آمار عملکرد، تولید مس محتوی معدنی به‌عنوان یکی از مهم‌ترین شاخص‌های راهبردی شرکت، در پایان سه‌ماهه نخست سال به ۹۲هزار و ۶۶۹ تن رسید که ۶درصد بیش از برنامه مصوب است.
ادامه خبر در مس‌پرس:
https://mespress.ir/x6RK
@mespress_ir</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/450158" target="_blank">📅 16:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450157">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/450157" target="_blank">📅 16:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450156">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0qm-ZISMxeT_x7reSDNIaf_OuMDpKhwzSQ1aHDaYSh3Ltogc9bYx5vH7NawGREsXdnVwdsXbACTRFZectmp5U-QWbgB8pWVJ4b2XUZDrx4cXagufUnI8DEE0udmpOY5YI0tIHrPg6GmUY78kVvzxcMOiwoUOkreW4C57T94hxmiLmcXYKb4FYY3JC5YViiDUJe3AYlnnDFRCWWHqC6MvSilsFNBJpMkIJaeQAMjnj9AyEldngSNle_RBCtn5Fwbt443PmHUE0v7L1z8TWuBWk04ThtmZjy8iZj6pUx8E38iqaJnodAfJxrqCNg_0aAmuJs_3wkCOX1K8URzZBuPrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعری که آقا برای اولین نوزاد رویان خواندند
🔹
رئیس پژوهشگاه رویان: زمانی‌که نخستین فرزند حاصل از درمان ناباروری در رویان به دنیا آمد، خبر این موفقیت را به رهبر شهید اعلام کردیم. مرحوم دکتر سعید کاظمی آشتیانی نیز ماجرای تفأل پیشین خود به قرآن را برای آقا تعریف کرد و گفت در آن تفأل، بشارت حضرت یحیی(ع) آمده بود، اما تنها تفاوتش این بود که نخستین فرزند رویان، به‌جای پسر، دختر بود.
🔹
رهبر شهید از اینکه این موفقیت به دست جوانان، بانوان محجبه و نیروهای جهادی رقم خورده بود، ابراز خوشحالی کردند و این بیت را خواندند: «باش تا صبح دولتت بدمد/ کاین هنوز از نتایج سحرست.»
🔹
لبخند و خوشحالی رهبر شهید برای مجموعه رویان انرژی‌بخش بود و همین حمایت‌های معنوی، انگیزه‌ای برای آغاز فعالیت‌های جدید و برداشتن گام‌های بعدی در مسیر پیشرفت این پژوهشگاه شد.
ماجرای بازدید رهبر شهید از رویان را
اینجا
بخوانید
@FarsnaTech</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/450156" target="_blank">📅 16:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450155">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7151964478.mp4?token=SxnhelY5stG26tnNoykzZOQZRljUh1jKIj05e7ma9IqupP-jj4L98SBZLKjsTa_PzkE5hpsM2B_CwdR4oDXFE3BnisrkUwybrdJk4CsYlfg8R4YIvSHCmuOkwtkCN6rtI7Bxkt_TfRwr9Yc97xMpra6MleJybdFIjsruS4FOlDfJwLjvOmcQWX5bTaA_DdUxWV1TD-AOcAx5IVWKYx4uzJN7NRRliMNscBkHJnVsjgWSgoygxNVUlErh9kE-6mNrNrZLaJ4JC2qDG01cGSU6Tl9dg5bobf4gtjTmk_1F6OOkqTQ9c_7Mj2eKh5AFRG1VzF7mexlNYRsNxkQ6mjIUTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7151964478.mp4?token=SxnhelY5stG26tnNoykzZOQZRljUh1jKIj05e7ma9IqupP-jj4L98SBZLKjsTa_PzkE5hpsM2B_CwdR4oDXFE3BnisrkUwybrdJk4CsYlfg8R4YIvSHCmuOkwtkCN6rtI7Bxkt_TfRwr9Yc97xMpra6MleJybdFIjsruS4FOlDfJwLjvOmcQWX5bTaA_DdUxWV1TD-AOcAx5IVWKYx4uzJN7NRRliMNscBkHJnVsjgWSgoygxNVUlErh9kE-6mNrNrZLaJ4JC2qDG01cGSU6Tl9dg5bobf4gtjTmk_1F6OOkqTQ9c_7Mj2eKh5AFRG1VzF7mexlNYRsNxkQ6mjIUTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کابوسی که هیچ سلاح آمریکایی قادر به حل آن نیست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/450155" target="_blank">📅 16:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450154">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">زمین‌لرزه‌ای به بزرگی ۳.۲ ریشتر خرمشهر را لرزاند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/450154" target="_blank">📅 16:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450153">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4ba0aae8c.mp4?token=ocOtl-Ih0m2Q_LHaYYHSVHv23rqQM9uZPIPbcAQ5NPuv8lp6nuoXr6TztOnZaimOAZHbvSZA2sLuLJn3s5YKNd0WT3KEWkCIJcHIEKwPRgueg3fnrZQZGzDkz8pHxdF7nkzLBv0BDQrrjph0vgPPPVq7Eq5xAK-yAaUCvlBh5jBEGCOWxmzNU1kx33L3oOYYw8hxQsOfxvkhV_melKPJByxjOFSpvfOT1X3x6fif5D3tDBXBZLNh6RskUmgNbSnGE-6cj6yH0g2tMzhfSrU6NNEzKZ-BDK3Nl6PshIGazW4OAzSYukz5EluwF-t7h-M9l-Td8q5n8I45q2CJtq1qWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4ba0aae8c.mp4?token=ocOtl-Ih0m2Q_LHaYYHSVHv23rqQM9uZPIPbcAQ5NPuv8lp6nuoXr6TztOnZaimOAZHbvSZA2sLuLJn3s5YKNd0WT3KEWkCIJcHIEKwPRgueg3fnrZQZGzDkz8pHxdF7nkzLBv0BDQrrjph0vgPPPVq7Eq5xAK-yAaUCvlBh5jBEGCOWxmzNU1kx33L3oOYYw8hxQsOfxvkhV_melKPJByxjOFSpvfOT1X3x6fif5D3tDBXBZLNh6RskUmgNbSnGE-6cj6yH0g2tMzhfSrU6NNEzKZ-BDK3Nl6PshIGazW4OAzSYukz5EluwF-t7h-M9l-Td8q5n8I45q2CJtq1qWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نانواهایی که هم‌چنان گران‌فروشی می‌کنند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/450153" target="_blank">📅 16:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450152">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNbKczON9TaiMhYek7IW1rBTYptvtf__-tidbtfHNwRc-GdwaemBD8IROj-sj0sqYuza5IuklpUFVHkEfSzjgPW3P2IrFfV9Z6J6M0Iy9mIvYbujsoLePzX1ZnwIZcE1MM9QgZoe0RXTGYLv0CcRIYr5gByJ4rxKXztyUxvzHj72sLL8qSG8-iVk8_dj2-kzi_1-kYw_OuhOZO77RGzNSIj4LbyyuoPCAWTpvQPdGbgDLR1dHGqm9pmc83IMTEeVLvC-rfMWTjb5pyDh6S5M4GmPK8_CeZyu33dZxFqfcRKilg3lngGt4glUagbKsxKjiDBqbrv1jMZRzAQfK0Pf5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برد قاطع والیبال نشسته ایران مقابل آمریکا
✔️
🔥
در ششمین روز از چهاردهمین دوره رقابت‌های والیبال نشسته قهرمانی جهان در هانگژو، تیم ملی مردان ایران در مرحله یک‌چهارم نهایی به مصاف آمریکا رفت و این حریف را با نتیجه قاطع ۳ بر صفر شکست داد و با کسب پنجمین برد پیاپی، گام به نیمه‌نهایی گذاشت.
📊
ملی‌پوشان کشورمان در با نتایج ۲۵ بر ۲۱، ۲۵ بر ۱۵ و ۲۵ بر ۱۶ آمریکا را شکست دادند.
📆
ملی‌پوشان کشورمان در مرحله نیمه‌نهایی باید به مصاف قزاقستان بروند.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/450152" target="_blank">📅 16:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450151">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2-1313A68JFXsPx_j5IpqZ2ji1FKxiLWfS3PD2fzrYkYlZo62NzK2lB1fneSPW-YBnG_XwuZr59Pl1hbWV0J4J_4yi6J3rFQwMIAtMAK88Y2AI5KixWtWtgGIDM92FsPK4a7MPCLgYH2OiQQb05KOLLGfx0w9cJt_xSQORRYEGOzVeSkt5uMl6UIG7EZ_mL7oKoV18DW4TL8mK0rsBIGqQczFSjTAlxbOU6GBdMa81JrAt5IuCFg0FYKDZGN-Wq5fWcY0sKuQWCYIrM1I1KrGy1ZgB3ZG84B9mMpcJQyO-_I9Yjzq0Pz_qgo6VmNy1W3P8zG-bK3hB9GmRE424Jqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بن‌گوریون دوباره پادگان نظامی آمریکا شد
🔹
با وجود اینکه سازمان هواپیمایی اسرائیل روز گذشته با صدور دستوری فوری، فرود سوخت‌رسان‌های نظامی آمریکا در فرودگاه بن‌گوریون را ممنوع اعلام کرد، اما فشار تروریست‌های سنتکام تل‌آویو را مجبور به عقب‌نشینی کامل و بازگشت به وضعیت پیشین کرد.
🔹
سازمان هواپیمایی رژیم صهیونیستی صبح امروز با صدور دستوری فوری به واحدهای کنترل ترافیک هوایی، اجازه فرود مجدد سوخت‌رسان‌های آمریکایی در فرودگاه بن‌گوریون را صادر کرد.
🔹
بر اساس گزارش رسانه‌های عبری، فرماندهی مرکزی آمریکا (سنتکام) اعتراض رسمی خود را به ارتش اسرائیل ابلاغ و مقامات آمریکایی با سران امنیتی اسرائیل تماس گرفته و خشم خود را از این تصمیم ابراز کرده‌اند.
🔸
خسارت‌های فرودگاه بن‌گوریون تا پایان ماه گذشته به ۷۰۰ میلیون شکل (واحد پول اسرائیل) رسیده و پیش‌بینی‌ها می‌گوید اگر سوخت‌رسان‌های آمریکایی از فرودگاه خارج نشوند، این خسارت تا پایان سال به مرز ۲ میلیارد شکل خواهد رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/450151" target="_blank">📅 16:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450150">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecd9bc8b00.mp4?token=dnFn2AB3GLMHS0OqA-410lXy_45dX3ylF9w4ZZavSuZ51_dSYgraERboP5odsU9kTKkNfB6UzrN8uG0A8A7PXurmhdLBlaVzG0lBC6bS6KFVxVT5KGyP3psWCHNUPmZ0Ap79uQTENHQhluhWxgahqace942hLSksGk_7emyWqyKgo4G1GN1ILQtM_KpXi6gy3NS50DPecthK6Dn_OPm266DKo8shDRo89PgD_WXurTIxbzsv6nLVWDmyMMm4pW5tDpwlhTV7Yb4P6Mps8kUwGPYmk15YZjxa00XKCeDgSKfc2fgI1v5uh8nop1FPQECOguJC6qIj7O3bRB-mV9-OGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecd9bc8b00.mp4?token=dnFn2AB3GLMHS0OqA-410lXy_45dX3ylF9w4ZZavSuZ51_dSYgraERboP5odsU9kTKkNfB6UzrN8uG0A8A7PXurmhdLBlaVzG0lBC6bS6KFVxVT5KGyP3psWCHNUPmZ0Ap79uQTENHQhluhWxgahqace942hLSksGk_7emyWqyKgo4G1GN1ILQtM_KpXi6gy3NS50DPecthK6Dn_OPm266DKo8shDRo89PgD_WXurTIxbzsv6nLVWDmyMMm4pW5tDpwlhTV7Yb4P6Mps8kUwGPYmk15YZjxa00XKCeDgSKfc2fgI1v5uh8nop1FPQECOguJC6qIj7O3bRB-mV9-OGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توصیۀ پزشکی برای این روزها: از ساعت ۱۱ تا ۱۷ از خانه بیرون نروید
.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/450150" target="_blank">📅 16:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450149">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5ecd15c19.mp4?token=lt0xkytTOIoSRU2nTKoPnPWUqBpgGi3rQJUW58M0lYWHPxZpECoOyEwF5lixwUQkO20ZvwpMiNLTPOsMqaPj9TfuCSqsQqmPhP--5UgZthHEUplU7L8gtB-QIN-Xqk0F3CvDrfjavcPTeQHv8fOGnXDYPwfXPna0NVh3_CnSNhh5Cz_wxrYU-JZ5Dsv1Xck41IuMFjw9FE0xPdp1vFILBFV8qH_MhYMgTjYeOcB5hWwFfaqcviXDlV5VCqsW-49CzJcO--qZsOqzpMS7c3wMTm6AK99HBPY79a4APlyEWdw1pRF6c9vctZEnTzmIPD1ny81RITr4rbJrVBMu8bAo4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5ecd15c19.mp4?token=lt0xkytTOIoSRU2nTKoPnPWUqBpgGi3rQJUW58M0lYWHPxZpECoOyEwF5lixwUQkO20ZvwpMiNLTPOsMqaPj9TfuCSqsQqmPhP--5UgZthHEUplU7L8gtB-QIN-Xqk0F3CvDrfjavcPTeQHv8fOGnXDYPwfXPna0NVh3_CnSNhh5Cz_wxrYU-JZ5Dsv1Xck41IuMFjw9FE0xPdp1vFILBFV8qH_MhYMgTjYeOcB5hWwFfaqcviXDlV5VCqsW-49CzJcO--qZsOqzpMS7c3wMTm6AK99HBPY79a4APlyEWdw1pRF6c9vctZEnTzmIPD1ny81RITr4rbJrVBMu8bAo4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
بدرقهٔ طولانی‌ترین کاروان پیادهٔ کربلا از مشهدالرضا
🔹
کاروان پیادهٔ انصارالحسین(ع) امروز حرکت معنوی خود را برای بیست‌وپنجمین سال متوالی از مشهد مقدس به‌سوی کربلای معلی آغاز کردند.   عکس:حدیث فقیری @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/450149" target="_blank">📅 16:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450148">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZyYc5ZvXoLI1L07P3mQzIwC3C1zGV0EpAt5JeghF6pPLCHdz42774PDvilrzkHOVq-6ZzexD_3BzmxWoZH_Blr6W3T67yzFZLzkejvOiCBfgu1l2zB1YQyV09-JqltmXZVgPmFnTKHOnKCLdW1oNSP3y8pjhBaD5wsGdpn51dALZVyCoxXy0yTAzM3XWUm5mOuDsfQBm8dldvz8Vf45ZadUZQ_isT6m8CSnP1OZPpTssXo2Hu2GJ9dcAkekjS0-hj-15L8zX47MwmeTnCqBOEo7DGqRY9jI5ScMygVW_ZA2roo7-SnXRbB2yOhlmOq8boJ5LRvZiLfTkBjEoBFQkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در پیامی درگذشت امیر پیشین قطر را تسلیت گفت  @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/450148" target="_blank">📅 16:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450147">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSwbM8N6Q-mwPZAzWPSfxSDyfFAPbYQ4f38i-EufUsdNs-EaK8OFy20FLvpWwF0BDVHjkln8biaiq6aM1KmCwuNOEMcEAjf2pL69k75xJlA1_Yba8P6G9l7ZJ_xPCB3TKPOnrZJCr5Swhb74du1n-nVh13ahLx_0VgOlPSFRn_AJis31K2svOetyyh2L2fWObpNndeQ1gVWqoDoD45AoLNWv1Yie0BuOto8tcYbNufPpa0sedpechArlBBcOnGs2WIYI2GWrL1fUBilM3AIvYvtyMkNhk4zIJRjaRXnDMXmtOrH0KOSTu15MciTcJAlVx0fAO0QV4bC1f-IoDtPGeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگلیس به‌دنبال ممنوعیت اینترنت شبانه برای نوجوانان
🔹
دولت انگلیس درحال بررسی طرحی است که بر اساس آن، دسترسی کاربران ۱۶ و ۱۷ ساله به شبکه‌های اجتماعی به‌صورت پیش‌فرض از ساعت ۱۲ شب تا ۶ صبح محدود می‌شود.
🔹
دولت انگلیس هدف از این اقدام را بهبود کیفیت خواب، افزایش تمرکز در مدرسه و کاهش وابستگی نوجوانان به شبکه‌های اجتماعی عنوان کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/450147" target="_blank">📅 16:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450146">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-gybX3Qs_ZDbYkja3YXlRZgF14HzoNXzYy2ZrvcxJXcZKIcP2jHMUrOaL1MYz4IjALnJ6H9O1-_FczG5O4kEwESfrlVIZ_CNW5wFu4fPxXq3kkIT0TUJbSdNuEUc05xvnb4Rma1XjX2zCgpHD0UwrbcaIIP2woGQQEkn01Q1KJT2Z7U-vXb5YaIRc16mA4jpN4wSI6OkTc789D2cHEZCHJCP5dz6ZNTnhD8G-P7pLTTzBGR2GGATLjQSwqzF3W_lcgHa-nrEUMJ6lPbiPZubYxb_htwdqDKk-_3NNZK9oDQZCughSVJYhRXFRxTj7IaH1D940jd4xb4N2YwLRIbMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کپلر: عبور از مسیر جنوبی تنگهٔ هرمز به صفر رسیده است
🔹
جدیدترین پایش ماهواره‌ای کپلر نشان می‌دهد که روز گذشته ۲۱ کشتی از تنگهٔ هرمز عبور کرده‌اند که از این تعداد هیچ کشتی از مسیر تحت حمایت آمریکا موسوم به کریدور عمانی عبور نکرده است.
🔹
بر اساس داده‌های این شرکت، مجموع حوادث تاییدشده در دریای عمان هم به ۵۶ حادثه و شمار جان‌باختگان دریانورد به ۱۷ نفر رسیده است.
🔸
این درحالی‌ست که ترامپ پیوسته می‌گوید، تنگه باز است؛ او دیشب در پاسخ به خبرنگار فاکس نیوز گفت: «منظورم این است که اگر مردم بخواهند از آن عبور کنند، باز است.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/450146" target="_blank">📅 15:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450145">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c33f0c42a0.mp4?token=azJndL-ugTjEq7imPvoLnE1z_6Qn4IjtMPssMcOf5Hm0cwn8eqG0HYK2gpD7hEX7waHVTEyfCdG5Vgk6oPqrWURL40mzrT94wA4kkhn-Uai6Yf4AYMQjLrTDq9ShAYiAb6hgGX3b7aLiv2OZctpg_2C0clracdR5nhLYUX5Hv5Cl0Nv9Wy0xT6dLUTeBdXTVXXqdwsLhribn70oApmNpCQtVuqJbF7BoH0qthIOCmUSTkGDDskMOJashcIDaYDEpsMCNUa-1VqnpXwi1b-zRPtskDGjtVwVXfkjxNYlxGryjxXITPAhITWkhXtDKBSsLeqpLLWQxjNh2RO4lOxYVcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c33f0c42a0.mp4?token=azJndL-ugTjEq7imPvoLnE1z_6Qn4IjtMPssMcOf5Hm0cwn8eqG0HYK2gpD7hEX7waHVTEyfCdG5Vgk6oPqrWURL40mzrT94wA4kkhn-Uai6Yf4AYMQjLrTDq9ShAYiAb6hgGX3b7aLiv2OZctpg_2C0clracdR5nhLYUX5Hv5Cl0Nv9Wy0xT6dLUTeBdXTVXXqdwsLhribn70oApmNpCQtVuqJbF7BoH0qthIOCmUSTkGDDskMOJashcIDaYDEpsMCNUa-1VqnpXwi1b-zRPtskDGjtVwVXfkjxNYlxGryjxXITPAhITWkhXtDKBSsLeqpLLWQxjNh2RO4lOxYVcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روزنامه‌نگار لبنانی: سعودی‌ها به ایران پیشنهاد کرده‌اند که در خصوص لبنان و یمن گفت‌وگو کنند ولی هنوز هیچ گفت‌وگویی انجام نشده است.  @Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/450145" target="_blank">📅 15:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450144">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWKaEkWtZlP-_RF-JBamSMyPyR6xoy1Q0sLfpSAg2zxN-p3MZ3jKj0VmQAlU4miMbNdreNqFy7YBUWh5ztirUR9QDkpsjTr2CZ76UefhGoELGfPL4iTfyQU0lD80U5Sxm5qXcam98qp7It_qOfaCV4BWa3R_SFn82UtX1D68j6YNhY2A0Ye49ANJ0LzhOFWZhTku7l8HQ6YBOu-edZCxmT3SJcNZegSKZu7Tmp0FCiRUT_ONsxddlDG6x9IA9FDTvyu5RLC1CBcqtEZOP_bSNPsqd3ryNI0hrDYkZRFJlOeuiYyuiQ0hDv17twnbtXPsWbYv-oEaqVFYGHm33JwwbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله اعرافی: قاتلان امام شهید دیگر احساس امنیت نخواهند کرد
🔹
براساس پیام اخیر رهبر معظم انقلاب، مطالبه انتقام و خون‌خواهی امام شهید و سایر شهدای دو جنگ اخیر، امری است حتمی و قطعی و به آمدوشد دولت‌ها و اشخاص مرتبط نیست و درهرصورت محقق می‌شود.
🔹
جنایت‌کاران و عاملان این جنایت‌ها، از این به بعد هرگز احساس امنیت نخواهند کرد و مسلماً آرزوی مرگی آرام و در بستر را با خود به گور خواهند برد و این انتقام در ساحت بین‌المللی و فراگیر و باهمت آزادی‌خواهان جهان دنبال خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/450144" target="_blank">📅 15:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450143">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1237345d28.mp4?token=GRmBoCVfHfIrFjssDWSFybXk2DMLugjfOUqtNlRWvs76mBMTS3aAQuQh8o8_g4jeb6bidBDKWAi6Q8oaT6y7GC0mAznQYqXtNfa1vtJBEHae3nbTeO_y0tsmjoILR4tcu_LOInNuKTaYshu2IMQ7Rx5gPpB_zXgAlTXrme_QjGJLjfKYJMW3gYa4VGmqc1GcaupyjyR6x3ZEsS0TNvCIqxAgjSCc3rY65LTPPDLjZAJ3EDQ29_a5FoiI85wTdhitCLmMU4QOXfK3OWDrKIqbi-X4iJXFXrjQuepqLMbvM8oHjELuGln7R6gowiCS-N92-tPPFpHapaO14E8l1m1E2RM366PDIHOHlejnuLODXq1_64JJ3hpbcO-8byXp-PB9nFeq_1Hwp6ArRUPRmHUKhBZSFKVV1yXoziaCuuwZTLQo2Z07KBNXrKubhYGZXLoGtXvNKTlcduzaDgaAYzlPWL1q84mr9kBTQ5bthc4X0oDl6XxHRk_lVpCy2oTYmrnFzL3-K65mc767pw52idRh3CnXdhkpLCVPc7D_lHf_fAT9KSBTvoH-ntrH13FNgeBfZM1bLp6EcpOTan3VGqetvxVkyqNLuet0S-enW2k3zzehQjVwmd4Du4q9hCSd3Lp56JxjCWVHnETlGjVYlstudqYjSxC50cLwABuuKMj-100" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1237345d28.mp4?token=GRmBoCVfHfIrFjssDWSFybXk2DMLugjfOUqtNlRWvs76mBMTS3aAQuQh8o8_g4jeb6bidBDKWAi6Q8oaT6y7GC0mAznQYqXtNfa1vtJBEHae3nbTeO_y0tsmjoILR4tcu_LOInNuKTaYshu2IMQ7Rx5gPpB_zXgAlTXrme_QjGJLjfKYJMW3gYa4VGmqc1GcaupyjyR6x3ZEsS0TNvCIqxAgjSCc3rY65LTPPDLjZAJ3EDQ29_a5FoiI85wTdhitCLmMU4QOXfK3OWDrKIqbi-X4iJXFXrjQuepqLMbvM8oHjELuGln7R6gowiCS-N92-tPPFpHapaO14E8l1m1E2RM366PDIHOHlejnuLODXq1_64JJ3hpbcO-8byXp-PB9nFeq_1Hwp6ArRUPRmHUKhBZSFKVV1yXoziaCuuwZTLQo2Z07KBNXrKubhYGZXLoGtXvNKTlcduzaDgaAYzlPWL1q84mr9kBTQ5bthc4X0oDl6XxHRk_lVpCy2oTYmrnFzL3-K65mc767pw52idRh3CnXdhkpLCVPc7D_lHf_fAT9KSBTvoH-ntrH13FNgeBfZM1bLp6EcpOTan3VGqetvxVkyqNLuet0S-enW2k3zzehQjVwmd4Du4q9hCSd3Lp56JxjCWVHnETlGjVYlstudqYjSxC50cLwABuuKMj-100" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاخ یزید وسط میدان شهر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/450143" target="_blank">📅 15:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450142">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQpUnuE0fb1FGUYhOXkzP4y_i3hVw_5mPleNJtF3TdSRt226YmO1gVbMUDCZWOjr1FLAlgq4WmORCkLoMxidBylsNVPW74oVO6a_V_IdpNDhNIROf_eYAEMbqcCO2B0XpcbgDyrdKqtKU-zfH2uMvheDh4uJDD3gNyl5ZISpFxXeyS8aJ19mr2mfZGyaWMQJACGVNhZ7E_34Kv1BvNdtEJTB6yN2HnvLuseNDhQ9U-42yJO_jvd17YHk9UjkkkYcoQmNiYBYe-fmL3fjwYdvXDX6FKW8KHY9aK7flH48mxsrp_YEv77a0iPgaNoVykUs4xrvygsx0xLOsUZpgcoBCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان فضایی: نخستین ماهوارۀ راداری ایران به‌زودی رونمایی می‌شود
🔹
توسعۀ ماهواره‌های سنجشی و مخابراتی همچنان یکی از ضروری‌ترین نیازهای کشور است و این پروژه‌ها با قدرت درحال پیگیری هستند.
در ماه‌های آینده مراکز جدید کنترل ماهواره، آزمایشگاه‌های تخصصی و بخش‌هایی از پایگاه پرتاب چابهار افتتاح و رونمایی خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/450142" target="_blank">📅 15:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450141">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aa3cf2ab2.mp4?token=YguZ_0_FnO1l5bosOnZ7VtiYVr354SaFltUWb7gyENrJLIsfhP_GsZKTX4ybQ9VEq9rQ5QnCdDlYf1JyaCQoZ2PW66JdJDAwCywD6zo8Un8WMGMziF4vrfF7Vb2x6tKAvANEKBdQn-QT8pLZeXjgQqBdsHFPrfyNiOMtVGJIG4E33W-vKHYgegBU8MN8q_-_b9bkoKVSNtaIzotAwOyTo_tzOxxECO8meLv4Ba59HgeJUcuz9hsmjHTSxIi5K7Qs3ln2utdcjLeeLkqDG42sAMk15pKn13nq2mSwPECthiI6szjA_Ra8CLa2A_JxjZ8ZHW0Qfnevm92Y2HrGgxSRJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aa3cf2ab2.mp4?token=YguZ_0_FnO1l5bosOnZ7VtiYVr354SaFltUWb7gyENrJLIsfhP_GsZKTX4ybQ9VEq9rQ5QnCdDlYf1JyaCQoZ2PW66JdJDAwCywD6zo8Un8WMGMziF4vrfF7Vb2x6tKAvANEKBdQn-QT8pLZeXjgQqBdsHFPrfyNiOMtVGJIG4E33W-vKHYgegBU8MN8q_-_b9bkoKVSNtaIzotAwOyTo_tzOxxECO8meLv4Ba59HgeJUcuz9hsmjHTSxIi5K7Qs3ln2utdcjLeeLkqDG42sAMk15pKn13nq2mSwPECthiI6szjA_Ra8CLa2A_JxjZ8ZHW0Qfnevm92Y2HrGgxSRJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توطئه ضدایرانی‌ها علیه عراقی‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/450141" target="_blank">📅 15:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450140">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/565655934e.mp4?token=DBrQolnrUTUP4KewGpRU_CDaBas0NkSjRmk-ddbFg9Sx8TInqVAv-BJgJYjWRiAvNEadT_LchSzYN8yr9VlV597698dGCCMGFAdiGi7Knu0HebERFiCYdTZ-4aRMfci6RReRH8y8os8b7-Rai0Q28RtIeBGU1ncWqraQeN2YwxXRmeftiO3rkN1kioEOcN42JL3UvBX7mz8WnuzX9uEB8vAfb-PAHH2ZOBejPb5gTmn1rJd0gppCtPOOrthWz1ksewcVEtvUS3V3AqSWbpH7Ee042YQO6IIA6sl6vJmv_AIVpjtea-4T2cfH397oZuIKFBgL9Gyxu1OExSabhp1iJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/565655934e.mp4?token=DBrQolnrUTUP4KewGpRU_CDaBas0NkSjRmk-ddbFg9Sx8TInqVAv-BJgJYjWRiAvNEadT_LchSzYN8yr9VlV597698dGCCMGFAdiGi7Knu0HebERFiCYdTZ-4aRMfci6RReRH8y8os8b7-Rai0Q28RtIeBGU1ncWqraQeN2YwxXRmeftiO3rkN1kioEOcN42JL3UvBX7mz8WnuzX9uEB8vAfb-PAHH2ZOBejPb5gTmn1rJd0gppCtPOOrthWz1ksewcVEtvUS3V3AqSWbpH7Ee042YQO6IIA6sl6vJmv_AIVpjtea-4T2cfH397oZuIKFBgL9Gyxu1OExSabhp1iJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روزنامه‌نگار لبنانی: سعودی‌ها به ایران پیشنهاد کرده‌اند که در خصوص لبنان و یمن گفت‌وگو کنند ولی هنوز هیچ گفت‌وگویی انجام نشده است.
@Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/450140" target="_blank">📅 15:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450139">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">مجروحیت بیش از ۲۶۰ ایرانی در حملات جدید دشمن
🔹
وزارت بهداشت: در موج جنگ‌افروزی جدید علیه کشورمان ایران، تاکنون بیش از ۲۶۰ نفر مجروح شدند که ۳ نفر زن و ۶ نفر هم زیر ۱۸ سال هستند. متأسفانه در میان شهدا ۲ نفر از خانم هستند. ۲۲۲  نفر از مجروحین، درمان و ترخیص شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/450139" target="_blank">📅 14:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450138">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbbf027082.mp4?token=ApYGKL3QlQb5yn_zwmuFRIdSz6R0zFWu0bjB6pMjEq3yhoSRVvMDbO8tb3bz4-4jhedB-rH1lYUQGQCq_CBrX96utl4G08bBwWY-jwnNTB4n9U-y9Bcna_ffpb0CoMCPEOfeRCNfjiJiLB7960GCVtsmbI_5dq6UGbueVNUgGEq-uq-GJxoicSEIoA7HyRPeB4EzuaLuP5rJR36q-ZVIH3Lq6ta_jrpd4jTlOK4KpN8-n4kSiGytTr75vbuBxz3IzVWqy-FFASSBT6cNkDQOAvCW5EtbB2Qz4nJ5gcZ2wdb9RkXmtXw-Aa_rXgre3hsIC82aT4KNHxyuvOd2G-r7Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbbf027082.mp4?token=ApYGKL3QlQb5yn_zwmuFRIdSz6R0zFWu0bjB6pMjEq3yhoSRVvMDbO8tb3bz4-4jhedB-rH1lYUQGQCq_CBrX96utl4G08bBwWY-jwnNTB4n9U-y9Bcna_ffpb0CoMCPEOfeRCNfjiJiLB7960GCVtsmbI_5dq6UGbueVNUgGEq-uq-GJxoicSEIoA7HyRPeB4EzuaLuP5rJR36q-ZVIH3Lq6ta_jrpd4jTlOK4KpN8-n4kSiGytTr75vbuBxz3IzVWqy-FFASSBT6cNkDQOAvCW5EtbB2Qz4nJ5gcZ2wdb9RkXmtXw-Aa_rXgre3hsIC82aT4KNHxyuvOd2G-r7Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تنگۀ هرمز همچنان بسته است؛ عبور غیرقانونی کشتی‌ها با مجازات روبه‌رو می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/450138" target="_blank">📅 14:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450136">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNP0T1qP8B5-Vzw2ntMtRNU2gaPZY-x0Ph0fuvXVxmvlZSnnpkzN83FsaZymevDeoRMnYVNPHaedyJM2Hlvvs6Yvn5juIuNYRKBfmpzVdFotMQt5X2MnuTlZlKzZUAtci2cdATISYcGfOTXDw362oSRXGlNqC2lQwLTvfvJWAZfgQIApVW_66h3z1xJcM-7dWT9YWADkxYKhzNvu6Uc2ZMbthioVUGIHCwl4ajh3ehkRFr68Ost2DlEM0XNHhK0rY1xHpaBxBrJOkLcmNqUc39j7uKBEdokYjvQlLpa9oJz6Y3P5RPzyIZo_SThTIuzIIaUcMxct-zZFASz07FaN0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمان اعلام قیمت بلیت پروازهای اربعین مشخص شد
🔹
سازمان هواپیمایی اعلام کرد قیمت نهایی بلیت پروازهای اربعین اوایل هفته آینده اعلام خواهد شد.
🔸
درحالی‌که برخی گمانه‌زنی‌ها از تعیین نرخ ۲۳ تا ۲۵ میلیون تومانی برای بلیت رفت‌وبرگشت پروازهای اربعین امسال حکایت دارد، دبیر ستاد مرکزی اربعین تأکید کرد قیمت‌ها هنوز نهایی نشده و جلسات تعیین نرخ همچنان درحال برگزاری است.
عکس: خدیجه نادری
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/450136" target="_blank">📅 14:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450135">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دامنهٔ t.me تلگرام از دسترس خارج شد
🔹
دامنهٔ t.me تلگرام که برای لینک‌های دعوت، کانال‌ها و اشتراک‌گذاری پیام‌ها استفاده می‌شود، با قرارگرفتن در وضعیت Server Hold از دسترس خارج شده و تمامی این لینک‌ها در سطح جهانی غیرفعال شده‌اند.
🔹
تاکنون تلگرام و رجیستری…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/450135" target="_blank">📅 14:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450134">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7263ff6e2.mp4?token=tTRznTlZ_DjPH-EGOSO2C5furSppki8G22x2aL8fK-d9UE02gHm-seL8mFymi_GisyAF9tRHZAwyHE4xQttS0-HAqW4w_QBZTw2LdltKON-oBy0GuRgNfQ2n8FF6t--fvvj9Ymv9kIGH2HplXA9P8hGMmJk-w3h2DLbB_s8jfjD5rQxIF_m3Sa1mAz_6Cr1ZwFEiwapRqVvS8vopE-rEIAzRV9raM4L9P5-vY4nxT8yTP8R_b0hFv0-bvVdS-Ct0ZOJhzHND0Nesbi4wUt60H1ncww7Si4ck3syZyLtNo6d06uMCwHRh1_4-Pts_XCGKjdtKBvQ6iJh3SaOC3381zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7263ff6e2.mp4?token=tTRznTlZ_DjPH-EGOSO2C5furSppki8G22x2aL8fK-d9UE02gHm-seL8mFymi_GisyAF9tRHZAwyHE4xQttS0-HAqW4w_QBZTw2LdltKON-oBy0GuRgNfQ2n8FF6t--fvvj9Ymv9kIGH2HplXA9P8hGMmJk-w3h2DLbB_s8jfjD5rQxIF_m3Sa1mAz_6Cr1ZwFEiwapRqVvS8vopE-rEIAzRV9raM4L9P5-vY4nxT8yTP8R_b0hFv0-bvVdS-Ct0ZOJhzHND0Nesbi4wUt60H1ncww7Si4ck3syZyLtNo6d06uMCwHRh1_4-Pts_XCGKjdtKBvQ6iJh3SaOC3381zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ابلاغیه‌های لینک‌دار کلاهبرداری است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/450134" target="_blank">📅 14:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450133">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37d02ed93f.mp4?token=XXo_7RlUkYXl7CsnB9VaqSSyB7g3lwQy92RUHQ1am3kxZ4eNAnYnCkGVxqG9alc1rlnc2qUkFaTKEm3c3O1LUZCMOSxqmVynXoLjnspRp-dGzMeOZLx5Gg5i1qT-n08tllG09ZfQ6u34dvR2oB02MWP6qnSbDAL_OS-0ZuwLxpkO-xdnmznxF5PyuVZ9oJkn1Czui5y3MHdYBLEfr2CoBeOqdUxxeTJ1Ct1yXIxRWxwwOi4wVpQvW04bHfMZxgc8kSZGhKHMt_WN5rhQ1zwKfFAeJIg5UIuqAG3eT5GzdqMI3N9OK1rBaw9kMxoD8ULsR3qinvxc-m6zaWAa47uaLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37d02ed93f.mp4?token=XXo_7RlUkYXl7CsnB9VaqSSyB7g3lwQy92RUHQ1am3kxZ4eNAnYnCkGVxqG9alc1rlnc2qUkFaTKEm3c3O1LUZCMOSxqmVynXoLjnspRp-dGzMeOZLx5Gg5i1qT-n08tllG09ZfQ6u34dvR2oB02MWP6qnSbDAL_OS-0ZuwLxpkO-xdnmznxF5PyuVZ9oJkn1Czui5y3MHdYBLEfr2CoBeOqdUxxeTJ1Ct1yXIxRWxwwOi4wVpQvW04bHfMZxgc8kSZGhKHMt_WN5rhQ1zwKfFAeJIg5UIuqAG3eT5GzdqMI3N9OK1rBaw9kMxoD8ULsR3qinvxc-m6zaWAa47uaLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آمریکا به آهوهای ایرانی هم رحم نکرد
🔹
درپی حملات آمریکا به جزیرهٔ خارگ، تاکنون تلف‌شدن ۲۵ آهو تأیید شده است.
🔹
معاون دفتر حفاظت حیات‌وحش سازمان حفاظت محیط‌زیست می‌گوید که آمار تلفات حیات وحش مربوط به مناطق خارج از محدوده‌های نظامی است و تلفات واقعی بیشتر…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/450133" target="_blank">📅 14:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450130">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qVixGJ1xVGrhTAtbazi9xSrY-1LPWHlckJCRfUEmrYNkVfoU0FSXZ-CIGMVv8X57QE_Uc3cJlSB50cmfVj-5zHSGwNTKp1u2nKpk0IRZ7kANOitG6JDgWTDyRsYijXRrR4YOr5abo_7RVBpoXx1MeNzYV85X0Jl0Bw3zehge0fEokF27vcGFWmJozTpkStVahLyEtmReRFRYcdr5g9bp1KAh3zxx2rQGj3DOAA1iDMivUO7hWk4h9EbKs07diPMzxhXJ-ZpaufqKtK30PNQfdQlErtXdUiswGox8Vk8uanOfdH7CPszha58YW0wh8W1PKXkqarEleOuaA2qV9UW2wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lFGmk6L5MGjdOWVtyFRdH9OtMUv0drIrZO8TaUiZHkWNXeexVg7UIyKfyxBTxdvw-rBsXgaEmN6CwuilQvP3E9DKewlTP0QT7CCH0LZKJbLnBNps17EYKQFwvhBEsLTCkEd3oTlNzbwTAbn75DbtRlVrKc22FwwUxdJu4jt3PoSX7KfprPyKD6aA4sVwtjQYMstyK5l9ObwjUsMMbe_AUtlihTnedQhhDfuuI1kh728B4qFVWUVniI7uLFIcor-1apR_iPo2YUyrEdPSkkIK9eAmappz9FyGz0v02mexOAuTiohwTT32HRHn9vTNaTvfuS0IGi2Nh-JyAK38uPUu0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GdCF9RrsJocjIZAIeUqg1aC5JoEw4hWJnivVWhRAXXoYRNhEfHQlsoVchAKXUpaDDWOgSM-4_CPiIgQ53N0CDwBp6O-HdRAxVuuZBcHHPut4qIDtEp9QPD94CZ6IOz6vHsEW17c6PJhXMgJMv-q1OGSba-ay1_OcDV3I0_1akL1uu8n--1mJz80dhNMmfzeac-Li6gZr0RjZ-8ss5Gvotg7OFjo-UImX6BI_LgGghoihFASuDmvHfIb7idj7nII46vDkQUBKHQvAXVqo1geq_c9r95_lXk7YszkVrIze27VvtuT0KWVJqKdM31ID56hP36Ayv7QFMhHSch8nTCRaAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌
🔴
آشیانۀ جنگنده‌های اف ۱۵، ۱۶ و ۳۵ و تعدادی از پهپادهای راهبردی MQ9 آمریکا در پایگاه الازرق اردن در هم کوبیده شدند
🔹
مردم شریف اردن، سحرگاه امروز که شرارت های ارتش کودک‌کش آمریکا علیه ملت ما مجددا از سر گرفته شد، در پاسخ به جنایت های شیطان بزرگ که بخش عمده…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/450130" target="_blank">📅 14:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450129">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae6e6af36b.mp4?token=KgAXWWc6Gmb0xFXYSwgGSPUfiBrnyWuJINDle3d0Gi8HlKGW064BgnNAKZEti9edM_HZWXtFs6d6rNRWVVpFtLts4zXGh23cccE9PBSQglDQ5aN7FrCp8KmUMPo0NHkcyesA3KZPxPT_dFOE2vWRmIzeGrwQYCroAgdCKr3w-K7f8Tu0rXv2N7CrLZmR0wHN4afxvAFDw1TcMuIixgqj8BSg7GihkKY9Onv_I3j5cUgYwURX4mVNRa8PLElNw1qKKQlTFSjYtkPHz4dlNmJ6yzzUONbBVmq0r80IDEwLGYTtNhJk6t-iLeKFKUMYw3fwnFkRi3frruTo0GVG2O2jgZUTQBH6X8EioYSTKNVzbI21dcAC7-A9h9xCBXPor5gaSFm1E61AXA25YQbJjlgYLYFgyxzYPPHzS7xHeBQD1Qmpvycl-1kP8cLEqskn_zyEeIM4RTGjrew5u3NElJZz2BMFD09AcFxei36v2QJhok6E_Slrc4w8n_tupV97PcKbgS7fLjfEZmFwWQeOk6dbD6S3lYcELfCRHUlG4bsu4ugt-dJogae-3Hsffdl0Dg2K6Oggku-qk1jssIjxI5cC5BYxxsPNmeuljOfw9Qnnivj_FoehPPNHjP1lxtNrHRtWQUHGh-QzVIVUH9FwXe5zVh_3cG_s1jm-A3lGk4eDXmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae6e6af36b.mp4?token=KgAXWWc6Gmb0xFXYSwgGSPUfiBrnyWuJINDle3d0Gi8HlKGW064BgnNAKZEti9edM_HZWXtFs6d6rNRWVVpFtLts4zXGh23cccE9PBSQglDQ5aN7FrCp8KmUMPo0NHkcyesA3KZPxPT_dFOE2vWRmIzeGrwQYCroAgdCKr3w-K7f8Tu0rXv2N7CrLZmR0wHN4afxvAFDw1TcMuIixgqj8BSg7GihkKY9Onv_I3j5cUgYwURX4mVNRa8PLElNw1qKKQlTFSjYtkPHz4dlNmJ6yzzUONbBVmq0r80IDEwLGYTtNhJk6t-iLeKFKUMYw3fwnFkRi3frruTo0GVG2O2jgZUTQBH6X8EioYSTKNVzbI21dcAC7-A9h9xCBXPor5gaSFm1E61AXA25YQbJjlgYLYFgyxzYPPHzS7xHeBQD1Qmpvycl-1kP8cLEqskn_zyEeIM4RTGjrew5u3NElJZz2BMFD09AcFxei36v2QJhok6E_Slrc4w8n_tupV97PcKbgS7fLjfEZmFwWQeOk6dbD6S3lYcELfCRHUlG4bsu4ugt-dJogae-3Hsffdl0Dg2K6Oggku-qk1jssIjxI5cC5BYxxsPNmeuljOfw9Qnnivj_FoehPPNHjP1lxtNrHRtWQUHGh-QzVIVUH9FwXe5zVh_3cG_s1jm-A3lGk4eDXmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عامل آتش‌زدن فرمانداری و کلانتری دهاقان اعدام شد
🔹
محمد امینی دهاقانی فرزند حسین از عناصر همکار دشمن که در روز ۱۹ دی ماه سال ۱۴۰۴ اقدام به آتش‌زدن فرمانداری و تخریب اموال عمومی در میدان امام حسین (ع) و کلانتری شهرستان دهاقان کرده بود، بامداد امروز پس از تایید…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/450129" target="_blank">📅 14:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450128">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">انفجار معدنی علت شنیده‌شدن صدا در شیراز بود
🔹
معاون امنیتی استاندار فارس: امروز هیچگونه حملهٔ نظامی یا امنیتی در استان و شیراز رخ نداده و صدای شنیده‌شده ناشی از انفجار کنترل‌شده در پروژه‌های معدنی بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/450128" target="_blank">📅 14:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450127">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‌ ارتش: پاسخ تجاوز آمریکا به ایرانشهر را خواهیم داد
🔹
نیروی زمینی ارتش: ارتش تروریستی آمریکا بامداد امروز، با شلیک ۱۳ فروند موشک،  آسایشگاه و محل اسکان یکی از پادگان‌های نیروی زمینی ارتش در بمپور را هدف قرار داد.
🔹
بنابر این گزارش، دشمن متجاوز در اوج خباثت،…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/450127" target="_blank">📅 14:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450126">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">تعویق یک امتحان نهایی پایۀ یازدهم و دوازدهم در ۴ استان
🔹
وزارت آموزش‌وپرورش اعلام کرد امتحان نهایی پایه دوازدهم در روز پنجشنبه ۲۵ تیر و امتحان نهایی پایه یازدهم در روز شنبه ۲۷ تیر در استان‌های هرمزگان، بوشهر، خوزستان و سیستان‌وبلوچستان برگزار نخواهد شد.
🔹
زمان جدید برگزاری این آزمون‌ها در این ۴ استان متعاقباً اطلاع‌رسانی خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farsna/450126" target="_blank">📅 14:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450125">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTtarQpuZBNjvxGRdh0dJe_AJKhc_ijjWU9pjh_y7ZalGT_LjhI2CfB3EgIntg5ff-3EhyWIEQ41dTDQUcdZgzgxQF_m5mxnC9qy0T57jOu0iXmuuO9YyRpasDhKQVoFS89dzrU-_4NbtUe29DaslbBYIJi-Qkr5x8ORA6kaTRLFbJY1KkGyjONv05YyWwB76CFqAJkKW6eqqbMpoSfuimBdksMjsjky-XLNPslGtCf5tD_qA2FUffguP_WrHtC--WtT09-CDwtvzFVXjZFLNM0_kmpToBpFSO8R8oR1s8lc0SZ9xeRHeQaQAi4pN2pMGJc3yKY1y-dChIVMg1iGhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیلات هرمزگان: ناوگان صیادی در تمامی بنادر استان طبق روال درحال فعالیت است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/450125" target="_blank">📅 14:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450124">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MIoq0u7Sm7B-kXiKIfBbePJPPZYs6PNkfB4KibpR0g-TiG9pRRFu18hlv6yD--c0tskFr-Y3l-UhKV1MjPsbLGp4pj2GuHGznq1ujU1vxh1l-38uiQvpXX1VnhX0oL66kdN52kOWyESzzpvSRZTzR2S2hDRZ-kuJomUcpT8kDAg21T9VvWYVUJnTD8UIIbz0qN-KmXsDvsI3SjeKA92BHX-QoDgnHN0zAvW-BCkEU6Ud0d1-E47D6ELgm6B8DbUhppWpdsUWis7c5VmfB2k-k3iE02o7cg04GwCDkAkllalG3-6ZQVA87-Zrd_Hm5ShudaAcleE_GITLfOlpEQZ_xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قدردانی واشنگتن از همکاری امنیتی اردن در برابر ایران
🔹
وزارت امور خارجه آمریکا اعلام کرد مارکو روبیو، وزیر خارجه این کشور، روز گذشته در واشنگتن با ایمن الصفدی، معاون نخست‌وزیر و وزیر خارجه اردن، درباره روابط دوجانبه و تحولات منطقه از جمله آنچه «حملات مداوم ایران به کشتیرانی و کشورهای منطقه» خوانده شد، تبادل نظر کردند.
🔹
براساس بیانیه وزارت خارجه آمریکا، روبیو با اشاره به این موضوع، از نقش اردن در پیشبرد امنیت منطقه قدردانی کرده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/450124" target="_blank">📅 13:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450123">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9PUtNI0PEv_cvDFZ3XCQYUEsKX_cwXxQ5vbkp1DGvY-4YTEG2J_Niz4oJ1pxzzPB1zc9SrFfQhaj5VKQz19EFeQiK2Z2LF3kEMr91WBDJN_W5InTx_IT894SCKPyaHcOLOow74zPXPn74Gy77tNjokEmWy9TsWX29RcOaAQ4Udh4JO4zbi5q4hkCAmmmYIcsiYscqaQH5uee_rNW8SKgotyVfI_a1MrGe-N4vjBroSdYfMpAPlmjaUrEsnzX0L3E5bjXAOo_cDHWBCpkyDQw1SgNeVBO7D86L6ojqLead8XrpfKjSIk7oNIApEGKAvndZl3LKbbumpv4ZoyODrRiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکایت بیرانوند از پرسپولیس به دادگاه CAS
🔹
دروازه‌بان محروم تراکتور، شکایت خود از پرسپولیس و فدراسیون فوتبال را به دادگاه عالی ورزش فرستاد.
🔹
او داوری سه‌نفره خواسته چون همزمان از پرسپولیس به‌عنوان شاکی و از فدراسیون به‌عنوان صادرکنندۀ رأی شکایت دارد. @Farsna…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/450123" target="_blank">📅 13:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450122">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLZMLqMF8B8PDAVS6gWZwRtJnWwkc8u10Z9HGjtwjEVnkuBuop0tJC7dGaSzBJRjozO3LwpKNbvHt9o7zPbU02l4Kus7SuWv7vBVno8fdLJmob17YLV6SCrvV7rMHQRb_oYUPpF_RNwqvoL8mqeDjGLDmw5BnZl1gR_rZHHcCoBML8NqksF2FA54ladqhOitaIGtL8EhYn5nKLNya1x3l16ZRqz-4VxmZA6vqxmFOqYxl25AWKIVwM8fLB4BKSpH5a3X4pLdaCkKceByqnK9RfT4bRDDacN2jgrV0z1WF2qPbzzZA00JnQeqfvpXmjS7zGFkBh57J-mMeldxccEIVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلی‌آف لیگ برتر با VAR شد
🔹
در جلسهٔ رئیس و دبیر سازمان لیگ فوتبال ایران با رئیس دپارتمان داوری فدراسیون فوتبال مقرر شد که دیدار پلی‌آف لیگ یک برای صعود به لیگ برتر، با تجهیزات تکنولوژی VAR (کمک‌داور ویدئویی) برگزار شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/450122" target="_blank">📅 13:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450121">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/136fc8d572.mp4?token=HYubTdadZ0hNQb4PqWcc65pGh3hmXyyHDINBraXWE-xMItxwuCQGo1pGzCxUzWbpF0_nGUgVaXFeo1-SFoYJbIca7Yk87wmlB1R3-YZh1i3gIksnxQgss_zp2ezj1lQJzMCoDV4Jc7XcX7Z5mKNlvql9zkscc-GhbLhKv1YdTsV_J9Eq23c3AMb_gfQ1ikO003FSlf3RWVjDL9aj5rSiFESnQZ_-v432qa6lLrxY2u7K_pCJfMw-eer_KNCSl_yLc9w7moKEywT5vnRWnuIYJI9RybXdCWSa_T7dXDp-ohNBnxaAl_TYp3JIG-mV45268Hoa3ML_362c8HRko6yYMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/136fc8d572.mp4?token=HYubTdadZ0hNQb4PqWcc65pGh3hmXyyHDINBraXWE-xMItxwuCQGo1pGzCxUzWbpF0_nGUgVaXFeo1-SFoYJbIca7Yk87wmlB1R3-YZh1i3gIksnxQgss_zp2ezj1lQJzMCoDV4Jc7XcX7Z5mKNlvql9zkscc-GhbLhKv1YdTsV_J9Eq23c3AMb_gfQ1ikO003FSlf3RWVjDL9aj5rSiFESnQZ_-v432qa6lLrxY2u7K_pCJfMw-eer_KNCSl_yLc9w7moKEywT5vnRWnuIYJI9RybXdCWSa_T7dXDp-ohNBnxaAl_TYp3JIG-mV45268Hoa3ML_362c8HRko6yYMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر لحظهٔ شلیک موشک‌های خیبرشکن، ذوالفقار و فاتح ۱۱۰ در موج‌های سوم تا هفتم عملیات نصر۲
@Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/450121" target="_blank">📅 13:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450120">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfT6bsj_VMlMwrUzmeoO47S22y51O8_bXTEWmHLk_ecCneBeh4_4VpC6SQiaNt6u0vYhCz7zDsDcTOuf6eSYipM-uY_8Y2n2yENyAbbcHIv8keAz8TVviqsyIYigeQGVDrpaASTe1OsKRwl-aCYQuwDxjyQTX_EBDNIw9KvQBdEUkY5kGStFdeDyrrZBBVJQdD0t0uCtpuRc4kMkAkpMBuumlppxxPoILPMfDSiySkJLS5WQ0UcOEJzSbXkstpuUkv7yWwzUOzLntBWrH3ay-UJEaa6Cw_p1AprIkRvabdoLSCtN4YDLIAkYDJCT59sOnuqQ1v75U1lGuf9O0GCcYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسم بزرگداشت حضرت آیت الله شهیدسیدعلی خامنه ای
و داماد ایشان شهید مصباح الهدی باقری کنی
و دیگر شهدای خانواده امام مجاهد شهید
🔻
مکان:مسجد دانشگاه امام صادق(ع)
🔶
زمان: چهارشنبه ۲۴تیر ساعت ۱۷</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/450120" target="_blank">📅 13:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450119">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3Q74izq7f8JMMteEsIUuYmFBFa_lMKkizNrcZ54WUS02F3hMalSoKMiXq246koFcrsc77yrTzU3l7R-bGwvzG6gHXfWhBoq7z4htk48qvn8i8h5kVVgiPiJsAyxu0L8TmqHa6zMkcEK00j3OW5iBtafdfMlwbbiPcDwny3GpCv6Jzc2h10DjLCtsQq1iwnFMaPaWq6aiFiSQtbB0GrX2Cg6NfYfQNNA1eSBqA71DOXiRCqcK6Up6k60ZgStsiUGlCMKksRiVFqKK7nd7ct6O0Z0PH6SK5NvwcecQqMlzMMLu-5Vw4nDnPylGppF-noxnIK79K5s5EvCyRt_4_G3Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
پیام تبریک دکتر اسماعیل للـه‌گانی مدیرعامل بانک رفاه کارگران به مناسبت هفته تامین اجتماعی
🔹️
در این پیام آمده است: تأمین اجتماعی، صرفاً یک نهاد ارائه‌دهنده خدمات بیمه‌ای و حمایتی نیست، بلکه یکی از ارکان اساسی تحقق عدالت اجتماعی، حفظ کرامت انسانی، ارتقای سرمایه اجتماعی و تقویت امنیت و آرامش جامعه به شمار می‌آید.
🔹️
بی‌تردید، حمایت مؤثر از جامعه کار و تولید، صیانت از معیشت و سلامت بیمه‌شدگان، مستمری‌بگیران و اقشار تحت پوشش و گسترش خدمات مبتنی بر عدالت، از مهم‌ترین مؤلفه‌های توسعه پایدار و پیشرفت کشور است.
🔹️
بانک رفاه کارگران به عنوان بازوی مالی و بانکی خانواده بزرگ تأمین اجتماعی، همواره افتخار داشته است با توسعه خدمات نوین مالی، حمایت از تولید، تسهیل دسترسی ذی‌نفعان به خدمات بانکی و پشتیبانی از برنامه‌های رفاهی و اقتصادی، در کنار سازمان، در مسیر خدمت به مردم و اعتلای نظام رفاه و تأمین اجتماعی کشور ایفای نقش کند و این همکاری ارزشمند را سرمایه‌ای گران‌بها برای تحقق اهداف مشترک بداند.
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/450119" target="_blank">📅 13:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450118">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/450118" target="_blank">📅 12:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450117">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
اقدام ضد ایرانی انگلیس این بار علیه سپاه
🔹
در ادامه دشمنی‌های انگلیس علیه ایران، لندن نام سپاه پاسداران انقلاب اسلامی را در فهرست ادعایی تروریستی قرار داد.
🔹
شبکه اسکای نیوز گزارش داد که «بریتانیا سپاه پاسداران انقلاب اسلامی ایران را در فهرست سازمان‌های…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/450117" target="_blank">📅 12:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450116">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aElTJtf6sC9emjjLtz2NQQLrmK35qWUGNSytHZOc-UNao-3GQfBYOeKZW71nvNrQ6SRtBZfGXYvfvZ_Vr01UceyfrjX8jKijL7bIvMLLXqENMgQWzdGqXpQgPSLMuD6bxZ2xUyGqF72U0BY8ykUJGHupEQi1T2hx-Mmdi6gRRYEBAfA0SK7mkZQyeIVaxYz37lfltJPRare622P-FoCZ7IoUAeNTCE0nH5aeFQaNjlS1JfvzigUbLzL2tTKNZiGYH2dTfZIs20fVYX009ehH1L09BoVj86oYmj3ImgZdBGQ_7i1CRROdIMWJGOUFAOHgz_o50VTjD0Eqi2RjBBj9Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس از ۴ میلیون و ۹۰۰ هزار هم پایین‌تر رفت
🔹
شاخص کل بورس در پایان معاملات امروز با کاهش ۳۱ هزار واحدی به ۴ میلیون و ۸۹۴ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/450116" target="_blank">📅 12:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450115">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">راهکار خروج از بازی دوگانهٔ ترامپ؛ «پاسخ صریح» جایگزین «واکنش به پیام‌های پشت پرده»
🔹
برآورد اندیشکده‌های مرتبط با حوزهٔ انرژی نشان می‌دهد، ضربه به تأسیسات نفتی منطقه، می‌تواند توسعهٔ کشورهای غربی را تا چند دهه متوقف کند.
🔹
به‌گزارش فارس، در تازه‌ترین اظهارات شب‌گذشته، دونالد ترامپ، رئیس‌جمهور آمریکا، بار دیگر تهدید کرد که «پل‌های ایران را می‌زنیم و هفته بعد زیرساخت‌های نفتی را هدف قرار می‌دهیم» و بلافاصله افزود: «مگر اینکه ایرانی‌ها پای میز مذاکره بیایند.» این الگوی تکراری در ماه‌های اخیر، نشان‌دهندهٔ استراتژی همزمان «تهدید علنی» و «ارسال پیام‌های فریبنده از پشت پرده» است که هدف آن، القای تصویر «تسلیم‌شدن ایران» به افکار عمومی جهان است.
🖼
اما پرسش کلیدی این است: راهکار هوشمندانه برای مقابله با این شانتاژ رسانه‌ای و سیاسی چیست؟
۱. الگوی تکراری؛ تهدید در ملأعام، وعده در خفا
🔹
بررسی تحرکات رسانه‌ای و دیپلماتیک آمریکا در ماه‌های گذشته نشان می‌دهد که کاخ سفید همزمان با مطرح‌کردن تهدیدهای نظامی، از طریق واسطه‌هایی نظیر عمان، قطر و پاکستان، پیام‌هایی مبنی‌بر «امتیازهای غیررسمی» به تهران ارسال می‌کند. این پیام‌ها که اغلب وعده‌های  فریبنده و غیرقابل اعتماد هستند، پس از مدتی در رسانه‌های غربی به‌عنوان «نشانه تمایل ایران به مذاکره» تفسیر می‌شوند و روایت رسانه‌ای آمریکا را تقویت می‌کنند.
۲. چرا پاسخ به پیام‌های پشت پرده اشتباه است؟
🔹
کارشناسان راهبردی معتقدند که هرگونه واکنش به این پیام‌های غیررسمی، بدون لغو تهدید نظامی و رفع تحریم‌های قابل راستی‌آزمایی، عملاً در دام بازی رسانه‌ای ترامپ افتادن است. آمریکا به‌دنبال آن است که با القای «فشار حداکثریِ مؤثر»، ایران را در موضع انفعال قرار دهد و سپس هزینه‌های جدیدی را تحمیل کند.
۳. برآورد اندیشکده‌ها؛ ضربه‌ای که توسعهٔ غرب را دهه‌ها متوقف می‌کند
🔹
پژوهشگران حوزهٔ دفاعی، انرژی و توسعه در اندیشکده‌های مرتبط، برآورد کرده‌اند که اگر ایران به تأسیسات نفتی منطقه‌ای که به‌صورت مستقیم و غیرمستقیم از آمریکا حمایت می‌کنند، ضربه‌ای حیاتی و کلیدی وارد کند به‌گونه‌ای که صدور نفت از منطقه برای چندین سال متوقف شود، پیامدهای آن فراتر از یک بحران موقت خواهد بود.
🔹
براساس این برآوردها، چنین اقدامی می‌تواند روند توسعه در کشورهای غربی و به‌ویژه اروپایی را بسته به‌شدت عملیات ایران تا چند دهه متوقف کرده و حتی به عقب بازگرداند.
🔹
وابستگی شدید این کشورها به نفت و فرآورده‌های منطقهٔ خلیج‌فارس، به‌گونه‌ای است که هرگونه اختلال بلندمدت در عرضه، زنجیرهٔ تولید، حمل‌ونقل، صنایع پتروشیمی و حتی بخش کشاورزی و خدمات آنها را با شوکی جبران‌ناپذیر مواجه خواهد ساخت؛ این هشدار، نشان‌دهندهٔ اهرم بی‌بدیلی است که در اختیار ایران قرار دارد.
۴. راهکار کارشناسان؛ «پاسخ صریح» جایگزین «واکنش پنهان»
🔹
تحلیلگران حوزهٔ دفاعی و سیاست خارجی بر این باورند که هوشمندانه‌ترین واکنش در شرایط کنونی، «خروج از ابهام و اعلام صریح پاسخ متقارن» است؛ به این معنا که ایران باید از طریق کانال‌های رسمی و معتبر (سخنگوی وزارت خارجه، فرماندهان نظامی و یا بیانیهٔ شورای‌عالی امنیت ملی)، به‌صورت شفاف اعلام کند که:
🔸
هرگونه ضربه به تأسیسات نفتی ایران، به منزلهٔ بازشدن پای تمامی زیرساخت‌های انرژی آمریکا و متحدانش در منطقه به‌عنوان هدف مشروع خواهد بود.
🔸
در صورت هرگونه تعرض، تأسیسات نفتی عربستان، امارات و قطر که نقش جایگزین برای تولید نفت آمریکا را دارند، هدف قرار خواهند گرفت.
🔸
باب‌المندب بسته خواهد شد و تنگهٔ هرمز به‌طور کامل به‌روی نفت‌کش‌های متحدان آمریکا بسته خواهد ماند.
🔸
همزمان ایران باید در فکر کشته‌گیری گسترده از نظامیان آمریکایی در منطقه باشد.
۵. هم‌زمان، قطع تعامل با پیام‌های فریبنده
🔹
کارشناسان تأکید دارند که ایران باید صریحاً اعلام کند: «تا زمانی که تهدید نظامی لغو نشود و تحریم‌ها به‌صورت قابل راستی‌آزمایی برداشته نشوند، هیچ پیام غیررسمی پاسخ داده نخواهد شد.» این اقدام، ارزش پیام‌های پشت پرده را برای آمریکا به صفر می‌رساند و مانع از سوءاستفاده رسانه‌ای از آنها می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/450115" target="_blank">📅 12:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450110">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZwyYtJrHFT8NRkHhb56NjAb_k2RvNY5ribAJrocfYkrOBOU_j18AyI08dE3CbX_ZXTmTdEIUSo9vhtMo8-yW_Q4wO-kfKIDUtprxkWglu6l1NOvtH5K3i1fIeyTrMmJ3DYmtW53l1hkuGGWi39dlG6hA2RmxLNgAldqUOYIYNLTwoMOJMRAoopv18Ln2ozX6-M65WxgXcV-YbA6WifXB7DcCD7eDs-9XXZfmNJzFPNkT-kNi_pFKYxhgi0N9q4-rFcl4_ClybuqJJSBgqMXky-2U9DRa6qp0VfqCW5etH3OhIkkUSBxxuhCa0CfBwiAQs1eD7L0CyUHZC4HEaY9vig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c5v7cTJh_LJIbIMo_7jN0A_OUdC1tHVYrNQkDkmgNDjfeqbIix70679EVdxgdNMupNbqiks5hBeRgEMYOvWtvlX2O53cK888TCDyJLOO6CApGij1DH8vTt4Rl5OhR7MPSXNgsfY5akOy-VweMmfk37sDAJnbwsSe44rDqMylrZYGTV-qV8L4uGS1jYReaLs46-FZAyOGG_x_aij19wTeQ-aTYuGpU0PDfNu6WdagO-JmwXHCawA6b6gQbSXaupIRnbkAJmSEBtS5dhm_GdnbmMgStN60O7ZN_vRED6ClBkskZmbZ2Bazw0vlI8srf5W-E_0TB0eBaWmQjgI2FML8aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ppr1L9umqBigkGi8aH5R5ECbUiOQI3IM1Oqv_TyspNY7Ia7_2ypIBnl6maV8J1dMu5wQRfnVFE51XqbU2BhymjxHOJNjq-AjgPsrU8WRWqRc2KvP7yCRGcErPUM4oA4XpJbhqyPYxNF-UrINvWw4oUWDGR7mefFbiCNhK5VDEbPyhQej3ogkGlosiEwv9y1iLfKg99E_Uh1MYuVFjbdHnRYzzYPmXHoVLW8UfIoAz8d2YvbfS-GlgaW1VsNYQ5h7V5lsMG_ptGkoLLjqgaPtdnkfJLDo8nWY5JRfswQD-IMzOxEGVVpHaaAlZUOaKVYHdjvxyppDOb8JRiH0WYMy7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c04J9H3hEusB5bF3Ki0HlVR9xe7fsEQybAXY2-IjPSd8jR46Xo4r8alHTH_rMKw-wXTgwVPqxz-0RDG2_-VKBfab0ZH0ZGj2dwPoK2XWe8YFXNnAJ1MlCpF41F8NLNjLrGF_cizzoIIQrsAc1HE-ztVh8SPUx98Ea7HaHwTMc_NsJfQBgrM8gygcm-f-KimJvYa2Tiu784I_61pU6_Jz5qR8kHEuOVub6GIlCXlYd023NbnRb4LB6fT2YiBY3_aE0wbr32TcG2Sq1ZHR2rcVLvRtZ2kPqjoeXjWaSUQa2NTC-3H5yXvEZIrCUi20ryB0ujFbnjxSip_dGODQayysYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pXUz0KV_43HI8yJoeuYbzqkDy5ecsAgeZ7PLfFaGrWRj5YMXCEoiC4U8N-c6iE1amvD6xQgKw3V6MLzU4cGC_mgFg2-pS8S6ACXFXVv3MxhrQ5brdsJ2z0KmhHvN5b96lV_Uk6eOm0fOp0dwdz_CPcHqqKCNU_6vHibJyIPXRBGct_PX9Fp5AGtZ2Ixno4YfZ-40PJsB_g5YzVL8UQH1LB3QGQQAOAvdSTypRgPuXvHwemz4H5hldK4SCLVTMCyx0UtxxxlyMnguFaIUTSkistMCv7jmu4WIMsDhBrbeCm8xoPyF7oxKQwnwHRuiUhZSjaQYYDajTS73VEyqZdIPUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تشییع پیکر شهید نیروی دریایی سپاه در حرم حضرت شاهچراغ(ع)
🔹
آیین تشییع پیکر مطهر سرهنگ پاسدار «شهید محمدناصر دلیرور» از شهدای نیروی دریایی سپاه که‌ ۲۱ تیر در جزیرهٔ فارور خلیج‌فارس توسط دشمن آمریکایی به فیض عظیم شهادت نائل آمده بود، در حرم مطهر حضرت شاهچراغ(ع) برگزار شد.
عکس:
احمدرضا مداح
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/450110" target="_blank">📅 12:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450107">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفالس نیوز</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QPiwq6JJZNuqLfUEYUReUjMgJE62pTa0Xa0OrCEzcFCNVNuTwz1rxI9iIIE8LnookurMlEjYw3awW63bNNzz3tH64pnc8Sy5tYg8EfMz0YABMcMgIJGmvwsaoHkygykWSYXRA4gO9d28x3ut42lmToMkjlwHIWTs95Js9BgfEH5joxVzLqwocv3tOjPxiJOCUEYpQaH9QUU-culmWOkS1XFl4KUHJkRCGCOGwOKNHECRu-0s2rgmq0xLon7X-7-zBleCHaKa_gVSWQUKfqPAKa92kSKsPVlJ_Z_YhVn0HJFhEnNQ6abunAkLTWLM7Vv1Ld2nH4JC7DWZBft9m-c9Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lt9lesbRzvmrqRd-9DhVCaeEIJWnHjrGsP3LEg2F8AUKI3U-xoACQBYTMfmP6fXZ0XFoayDPKrACNYw7dJR8ZHg_12EUuKFvzUVxJcF7bKffJTSzKwCNpxTZA4rK958o_D3xatTjbmx0uyJEfHcEmpaKnEkfc0ht7v869HwLvMm5Qpt_3raz02Mi1nK0VplLxha4wbgDmlRg0MC_JzmuUnAmdH7C6Ox-szWAxh2UrY6PL1LXBsbG8SJPSPh8oUeXvrXAaXbAQlLg57dZ1m6F_armSEqHDCavWprX6GkrqDNV3Bgg7jbUvw8gdDKNlsXVHySTrOA8KOfv0Xk_pblrAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BsPIHq9flEWywuwZWnkJRqlH7tqCPDBfCaIpdGXUApoS5t5zKpqU8P4_SxX2xxYUtCe9r5meWg6A8V2bIW8wMtPMCspH-HAnrefKzUjFUxwq7ZgDMoXv775SjBGqp-K2BOobuVoybMskhnOxZ4wKw-gnw_67rOGOEdnSZVyViKMOsoBNp4Zj2hkfXYU8oM1m1mSEr-iGj6w4UjQptPV9Hexd2Cy5mC5q33WcSBjy6O2IeKaRwj8FCGbF0IrIEBTje4erMZ97vCMNuYkFVmiZwNU8J0KA4sFJU5BKezkdxW_XdWrd7GsQJbhiiv3jZ5L2weDm5IwM3jn1Nj-y09YqRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نقل قول جعلی منسوب به مدیر روابط عمومی صداوسیما
❌
به‌تازگی پس از حملات آمریکا به بنادر ایران، تصویری با ادعایی منتسب به «افخمی، مدیر روابط عمومی صداوسیما» منتشر شده که در آن گفته می‌شود: «شهرهای حاشیه‌ای ایران اهمیت کمتری دارند و باید تلاش کنیم جنگ به تهران نرسد.»
✅
این درحالی است مدیر روابط‌عمومی صداوسیما «حسین قرایی» است، نه افخمی. همچنین تصویر منتشرشده در این شایعه نیز مربوط به آیت‌الله مظاهری است و ارتباطی با فرد ادعاشده ندارد.
⚠️
به‌نظر می‌رسد هدف از انتشار این ادعا، تحریک احساسات عمومی، به‌ویژه در میان مردم جنوب ایران و ایجاد شکاف میان مناطق مختلف کشور باشد.
@Fals_News</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/450107" target="_blank">📅 12:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450106">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctXS0cNtpl83PJJXAd7kfAgSTDNUitk2JuQpsG6B36G7CTWgqYC5uZxYE6lrzqLR5UkKmbH1veq3YmEMHvR9CjWGotLzcEQaUwXGdson-vZPTzMUx1DrSa817qXNxu9wx4gr7eBEBYQSSqqQnRnO4bP8_nJa4GMWUJwy04CMXgXzFD6Umf-wNuXi1cZiqaDaZKJLLlqL64mJDJGHXWgx1b80wlD3_H53cApU2UCG0wmhlAf6GF-BNF5oLOWL8VhcPkD-lWiTjMd-bO4ZtUihA7COhtALXdSEEODZ7-O9wOmlBLkmUgbQuEj7CjAhFOoB_PQcjnNgInMiaD66hdZvQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وام ارزی ۲۰ ساله برای یک شرکت سیمانی
🔹
وام ارزی شرکت سیمان بیارجمند که در سال ۱۳۹۱ از محل حساب ذخیرهٔ ارزی دریافت‌شده بود، با پیشنهاد بانک مرکزی و تصویب هیئت امنای حساب ذخیرهٔ ارزی و هیئت وزیران، تا سال ۱۴۱۱ تمدید شد.
🔹
براساس این مصوبه، دورهٔ بازپرداخت وام ۴ سال و ۶ ماه افزایش یافته و مجموع مدت آن به ۲۰ سال و یک ماه رسیده است.
🔹
اگر شرکت در مهلت جدید اقساط خود را پرداخت نکند، جریمهٔ دیرکرد از پایان دورهٔ استفادهٔ قبلی محاسبه خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/450106" target="_blank">📅 11:47 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
