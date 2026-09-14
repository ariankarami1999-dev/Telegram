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
<img src="https://cdn4.telesco.pe/file/FMfvbt8os8L0QgRgY3r1RJZqUjhGSrWgSJIFxwunHPHgHwT4GhS5eZeBCUuSJT8ZITdXW6o6K5dvNVcIVaxJFvMgvBYRuO2ZF1MLjTSVikVKfaMsReDPEO4GZyMfMTaXU6f40t3eZbqMn8Vvboax_KscTAcKq8Gq16pS9MwMBIwi64xlpjX81dlz58Jpm0qSKBaXHYTWDisQN0WI8u8Qgwgvi0owv1DRDPeIBsgrkFXh7sEeJmRdWvwTqysolLkOk2NLKgZ20-iXpex03qudmuS_NrD4fi2UHHX5LmU-vKV6mhONBL9CEQyeLc1rnJnABfCMpnNMxpFQyIuhJKBSgg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-23 18:37:23</div>
<hr>

<div class="tg-post" id="msg-140047">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVqRT0c_orjIinmZ2xcHf58T1C5zcMQ6blXewY8H9CRCFlYGg-JLiHP8ebqFS6m8E4g-zPN8xqYsrtrGPTEgl_NsIvAePcJnepr5oL_-jQcDmFh48ttVT4clbbmgWUKQVIEj2uE5oRnA9arC58QWNsN1YZ6r01qUIaMXF-c8gGd4GsMZp6iBN7Lfcy0U8lFoNyjE4ajuej4EyCPP_H2zP09m5FiH9nNeBuKq68L8xshCUkvv5MiWBT_6XAoE4AzmnHCguhi4zRFikmCj7yAre9fpVB6Nr4HXTyNWdL2Qlon1xKz8krRsTU1AXTrAKJtxSykIj5Ea7KwZz3NZD1GJ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
علی علیپور با وجود اینکه پرسپولیس یک بازی کمتر انجام داده، همچنان صدر جدول موثرترین بازیکنان لیگ رو در اختیار داره.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 494 · <a href="https://t.me/SorkhTimes/140047" target="_blank">📅 18:29 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140046">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✔️
✔️
✔️
علیرضا بیرانوند دروازبان تیم تراکتور، دو دیدار آغازین مقابل شباب الاهلی امارات و الغرافه قطر را به دلیل محرومیت غایب خواهد بود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 578 · <a href="https://t.me/SorkhTimes/140046" target="_blank">📅 18:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140045">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
بازگشا سخنگوی پرسپولیس: دنیل گرا در هر تیمی که قبل از آمدن به پرسپولیس بوده است کاپیتان آن تیم بوده و بازیکن بسیار پخته و باشخصیتی است!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/SorkhTimes/140045" target="_blank">📅 17:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140044">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
پایان زودهنگام حضور گل‌محمدی در عراق
❌
ادعای مجری شبکه الرابعه عراق: یک خبر اختصاصی داریم که با توجه به باخت شب گذشته باشگاه دهوک تصمیم به قطع همکاری با یحیی گل‌محمدی گرفته است.   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/SorkhTimes/140044" target="_blank">📅 16:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140042">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔻
🔻
دهوک عراق با هدایت آقا یحیی گل‌محمدی در هفته هفتم لیگ این کشور متحمل شکست شد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/SorkhTimes/140042" target="_blank">📅 16:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140041">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✔️
✔️
✔️
✔️
شایعات: حسین کنعانی، حسین ابرقویی، امیرحسین محمودی و ابوالفضل جلالی در دیدار دوستانه امروز پرسپولیس از ناحیه زانو مصدوم شد.
❌
ظاهراً کیفیت بد چمن باعث این مصدومیت‌های عجیب شده است…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SorkhTimes/140041" target="_blank">📅 15:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140040">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
❌
علیرضا بیرانوند: هراسی از رفتن به سربازی ندارم. دنبال رانت و پارتی هم نیستم. وقتی گلر تیم ملی هستم، اونجا هم سرباز کشورم. دنبال فرار از سربازی نیستم. همیشه کنار مردم هستم. الآنم سرباز وطن میشم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SorkhTimes/140040" target="_blank">📅 15:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140039">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🔴
❤️
ورزش سه: دلیل بانداژ دست امیرحسین محمودی تکل او مقابل ذوب‌آهن است که باعث آسیب جزئی این ستاره‌ی جوان شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/140039" target="_blank">📅 14:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140038">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJqyZk3iEBDVb2A6PIZtXLu9KB8Bjl_QF0ARotQrR-2K5h6F7bEeqkPkq41Yl10r60M0dE8yhBGnDOH6we6SNbpueXgdWyQc17usbuhE_haGDh5SM7_DVIPccBYaF-XgMY1aMj5lTz_OSGRO7-2XGc6Crf9mQyZjIAt2c6o8DW3uELbo57xP2x0LgLqKdMTmAgO_MHTmhPVQdQP9JeZLc0YtDUmvj3yKpJ1uIDhYKO9DErnl7CgzcI1nvbqMqrmF9bCg-evSh7clTqUqd_1-gceOH5QcgbI3GaS5RsFhgsxNq-vaooxk6DJ4JJGVS5B0QL8XTwNjriNqU-H1AfWMSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
استقلال در آزمون بزرگ آسیایی؛ سدِ السد مقابل آبی‌ها!
[
استقلال
🔵
🆚
⚪️
السد
]
⚽️
استقلال برای گرفتن امتیاز مقابل السد باید اول بازی را کنترل کند و در انتقال‌ها کم‌اشتباه باشد. السد با مالکیت و کیفیت فنی بالایش می‌تواند خطرناک باشد، اما استقلال هم در ضدحملات فرصت‌های خوبی خواهد داشت. در مجموع، بازی نزدیک و تاکتیکی به نظر می‌رسد و جزئیات می‌تواند سرنوشت مسابقه را تعیین کند.
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه تا سقف ۵ میلیون تومان دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/140038" target="_blank">📅 14:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140037">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
🔴
مهدی تیکدری (۲۷)، یاسین سلمانی (۵۹ پنالتی)، ابوالفضل زارعی (۷۰) و مجید عیدی (۸۵)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SorkhTimes/140037" target="_blank">📅 13:18 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140036">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✔️
✔️
پویش مردمی با عنوان فرستادن صفر بیرانوند بعنوان #سرباز_نخبه به جزیره سیریک در جنوب ایران راه افتاده
✔️
✔️
این بازیکن به دلیل پرتاپ های بلندش می تونه نقش پدافند سیار ایفا کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/140036" target="_blank">📅 13:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140035">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
فووووووووووووری از ورزش سه
🎙
🎙
علیرضا بیرانوند از اول آبان به طور قطعی و صد در صدی سرباز محسوب میشه و دیگه نمیتونه برای تراکتورسازی تبریز بازی کنه
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
〰️</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SorkhTimes/140035" target="_blank">📅 11:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140034">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✔️
✔️
تیکدری‌ جای جلالی را گرفت!
🗣
🗣
مصدومیت ابوالفضل جلالی می‌توانست برای تارتار دردسرساز شود، اما مهدی تیکدری‌نژاد با عملکرد خوب در پست دفاع چپ حسابی جایش را پر کرده.
🗣
🗣
تیکدری در ۴ بازی اخیر فیکس بوده و پرسپولیس در ۲ بازی اخیر کلین‌شیت کرده. حالا با این عملکرد،…</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/140034" target="_blank">📅 11:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140033">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✔️
✔️
علیرضا بیرانوند: به عنوان یک سرباز جان بر کف ایران و اسلام، آماده رفتن به خط مقدم و خدمت مقدس سربازی هستم و از اول مهر به هر تیمی که معرفی شوم حضور پیدا خواهم کرد و در زیر این پرچم مقدس به انجام وظیفه خواهم پرداخت!
😁
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/140033" target="_blank">📅 11:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140032">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
❌
❌
❌
حریفان پرسپولیس در نیم فصل اول:
✔️
هفته اول: شمس‌آذر
✔️
هفته دوم: اس‌خوزستان
✔️
هفته سوم: تراکتور
✔️
هفته چهارم: ملوان
✔️
هفته پنجم: استقلال(میهمانیم)
✔️
هفته ششم: ذوب‌آهن
✔️
هفته هفتم: خیبر
✔️
هفته هشتم: صنعت نفت
✔️
هفته نهم: مس شهر بابک
✔️
هفته دهم: فولاد…</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/140032" target="_blank">📅 11:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140030">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✔️
✔️
علیرضا بیرانوند: به عنوان یک سرباز جان بر کف ایران و اسلام، آماده رفتن به خط مقدم و خدمت مقدس سربازی هستم و از اول مهر به هر تیمی که معرفی شوم حضور پیدا خواهم کرد و در زیر این پرچم مقدس به انجام وظیفه خواهم پرداخت!
😁
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/140030" target="_blank">📅 11:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140029">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_bwC0Ky2a1nNLE7Ctv4C5VRfWZiqpgY10EqkjYKdnvYz7m94_rpRH0MV0r_DTQGIHP4a8UaS-dQbtPkKVs7QWUx8Byg48CnjADKqfGvlP4mK6yKlPFGyljVp9icJ2bFvzSKLWTvpbSr3bqlKCu250_Y4dXLH3dpIXuJJdvfKsLbyuRrFUWYpH9WHc_vEO5Szy-yvV7DajOg9j34m1bB5thdKHbdw9iHifLn1GoIpQzgIIuQFd5DxUoxtKyNPQfE32O8C_r54csnahJPTnVnPn0_rvR1wsK3OcQkO9MFZomrrDZ4sSJIZXzaEBWFvDrzQ1K-XkBmdMwBnd12QALfpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔄
دیدار استقلال و تراکتور در هفته هشتم لیگ‌برتر روز پنجشنبه ۱۶ مهرماه در ورزشگاه تبریز برگزار می‌شود. بزودی برنامه هفته‌های آینده لیگ‌برتر اعلام خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/140029" target="_blank">📅 11:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140028">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✔️
✔️
پرسپولیس برای خرید امتیاز و راه‌اندازی تیم «ب» با بعثت کرمانشاه و فرد البرز مذاکره کرده؛ قیمت پیشنهادی این دو تیم هم به‌ترتیب 120 و 125 میلیارد تومان اعلام شده. احتمالاً تا امروز یا فردا تکلیف نهایی خرید امتیاز مشخص میشه
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/140028" target="_blank">📅 09:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140027">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✔️
✔️
پویش مردمی با عنوان فرستادن صفر بیرانوند بعنوان #سرباز_نخبه به جزیره سیریک در جنوب ایران راه افتاده
✔️
✔️
این بازیکن به دلیل پرتاپ های بلندش می تونه نقش پدافند سیار ایفا کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/140027" target="_blank">📅 09:18 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140026">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPhc76d0jZIH7eJz5EMHtOqCqexU1M_JbRzZh_GKfNWiHt9dT-elJCnDIPNpRN3vC23YeWIqaHlUzG09rVxNTR9r84e17OFn1QMxz5rB1UTLZG__HOsu6Qt0WV6bpcVFEO91xJ-VGdl1O25ZJRqQSpsXsaocP2ncAnpYahPepoPSTkJHH0LLxmOEtIy2gRSSb3AmkjOD6IE5gJXEM8OGMG9F8jb5VoH__dfk7gjjiUITjtySMnQDJPeqMJ89TuRtBX6SfgjFMsN24gH-v_EoaMV1rELJ6F0nlziNKOzzXTSHbN7KmKmm4asuArqjzfZmjDcPbx6pCPWFev0wzEhTLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
صبحتون بخیر ارتش سرخ
🚩
✨
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/140026" target="_blank">📅 09:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140025">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dgqDGsvTzT8pNQ0gapAffQTbYEE5aZbEX4ZQVbrwX-fTKj6Zj3j9J5gCI_YrNN-7LjMmmqc-LeBqhJgjtGZEx1CIz9tl6JnI7L2Vh_Z7kTrUfBllrL_MNdRArcAJuJnWz6d959vo2UicBZn6Vmtj6XTHK1i6hO1qDbhIUwZi8sfFgBh-rQx8jiSuRKI5r3biOHIfXPYoLLj2ZReOQNKuQ48OuTzIY78c1wwTj490O4W2DhLsVa63sbp0CGfJn4Y3ro-rdDB_IEqsGz4nVp9C3r1ysDZem-nDGXdLsxyx_YWdYKOcZH7Ck6-dcstwY123M3vCTrp7q4dnKNUxH43pCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بونوس ویژه اسپورت‌نود
🔵
با هر واریز بین ۵ تا ۱۰۰ میلیون تومان ۱۰٪ بونوس ورزشی تا سقف ۵ میلیون تومان دریافت کنید.
🔗
آزادسازی بونوس خیلی ساده‌ست؛ فقط کافیه یکی از این دو روش رو انجام بدی:
👇
📌
شرط تکی با ضریب حداقل ۱.۹
📌
شرط میکس با ضریب حداقل ۴
🟢
مدت استفاده از بونوس ۲ روز می‌باشد.
🔗
همین حالا واریز کن، بونوس بگیر و شانس بردتو بیشتر کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
مینی‌اپ رسمی اسپورت‌نود:
🔵
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140025" target="_blank">📅 01:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140024">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
خدابنده لو: ارونوف به من گفت در ایران فقط دوست دارم برای پرسپولیس بازی کنم.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140024" target="_blank">📅 00:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140023">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✔️
✔️
✔️
تیم دهوک عراق با مربیگری یحیی گل‌محمدی سرانجام بعد از ۵ هفته به اولین برد خودش دست یافت.
🇮🇶
در این مسابقه، دهوک که میزبان هم بود تا دقیقه ۷۳ یک بر صفر از نیرو هوایی عقب بود اما با دو گل ایگور برزیلی در دقیقه ۷۴ و ۹۰ به برتری جذابی رسید.
🇰🇬
دهوک با ۷…</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/140023" target="_blank">📅 00:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140022">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
🗞
علیرضا بیرانوند ۶ روز پیش دفترچه سربازی شو پست کرده.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/140022" target="_blank">📅 00:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140021">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✔️
✔️
فارس :
⚪️
اگه بیرانوند مهرماه دفترچه اعزام بگیره شاید بتونه با تمدید تو دو یا سه بازه تا نیم فصلو تراکتور بمونه
🗣
ولی اگه امکان تمدید تاریخ اعزام نباشه یا باید تا نیم فصل بدون تیم بمونه یا بره دسته یک و برای نیروی زمینی بازی کنه تا نقل و انتقالات زمستانی…</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/140021" target="_blank">📅 00:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140020">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✔️
✔️
پویش مردمی با عنوان فرستادن صفر بیرانوند بعنوان #سرباز_نخبه به جزیره سیریک در جنوب ایران راه افتاده
✔️
✔️
این بازیکن به دلیل پرتاپ های بلندش می تونه نقش پدافند سیار ایفا کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/140020" target="_blank">📅 23:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140019">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a30d045eab.mp4?token=nT-M4suiOP9TyLN-7IZloQwpRvB3Ppdu8vuAHga-UajAZcwyDxQSeRcPgGZrEPk7e19FI2cUONaOGbSNR7FN3NpJS7K4AHuE6krB_ZiKCGc7qd0d5Q-soItQODx8whAiZBB1cjELa2pAvNsHMdhSepYbnRAYreRp_FezyCrDgGMBTRdb5GydGi-cf3UZ9wSslqwpih0NT4hoO4KKx5aAV0Tk4KGNpJE4HkM1Zy3ZuVDv45Eci0gCpWoZYohb2k0hFW4PfS50J95EEV-oBhX4jbm2IHj-RD1r1pZgPudRdpqHGpBaRD4LiaZj8bBdu2-5GAwY0GWh-D7rvw3CMi3rrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a30d045eab.mp4?token=nT-M4suiOP9TyLN-7IZloQwpRvB3Ppdu8vuAHga-UajAZcwyDxQSeRcPgGZrEPk7e19FI2cUONaOGbSNR7FN3NpJS7K4AHuE6krB_ZiKCGc7qd0d5Q-soItQODx8whAiZBB1cjELa2pAvNsHMdhSepYbnRAYreRp_FezyCrDgGMBTRdb5GydGi-cf3UZ9wSslqwpih0NT4hoO4KKx5aAV0Tk4KGNpJE4HkM1Zy3ZuVDv45Eci0gCpWoZYohb2k0hFW4PfS50J95EEV-oBhX4jbm2IHj-RD1r1pZgPudRdpqHGpBaRD4LiaZj8bBdu2-5GAwY0GWh-D7rvw3CMi3rrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تیکدری بازیکن پرسپولیس: مهدی تارتار یک مربی بی نظیر است
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/140019" target="_blank">📅 22:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140018">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08e82ae3f4.mp4?token=XQ-YruOVzUVp5irwvmmvt97OBDdTRNB7kh3KU3-E3ZYiDoPuhp1YmGZvP1jpFWZih2vKDVRy7sh0Nub6fqXH55KSqZRLmlVuXi4lRmlVi-Gnwnp2fQIlHASVQVbz6v2eP2beoDr-S-FevPD9lkhT1o7zd4_r-aUQgp1gGVJTYPXKimkgq2DxE_GlUJn4kZYCfD9F32_LUetthMgxT0DHWaXKg2sGSFY0QywBkq_9qigBd9neo1Yg0jOHRQ7v2WS2IY0uhyDwiiD8PAnks8Yjjpg2vow6mNW1PqjCyunMjLwPrHDaOmoUyn1yZN07mlLZH4mRDo9f-GqahoknDzME2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08e82ae3f4.mp4?token=XQ-YruOVzUVp5irwvmmvt97OBDdTRNB7kh3KU3-E3ZYiDoPuhp1YmGZvP1jpFWZih2vKDVRy7sh0Nub6fqXH55KSqZRLmlVuXi4lRmlVi-Gnwnp2fQIlHASVQVbz6v2eP2beoDr-S-FevPD9lkhT1o7zd4_r-aUQgp1gGVJTYPXKimkgq2DxE_GlUJn4kZYCfD9F32_LUetthMgxT0DHWaXKg2sGSFY0QywBkq_9qigBd9neo1Yg0jOHRQ7v2WS2IY0uhyDwiiD8PAnks8Yjjpg2vow6mNW1PqjCyunMjLwPrHDaOmoUyn1yZN07mlLZH4mRDo9f-GqahoknDzME2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خدابنده لو: ارونوف به من گفت در ایران فقط دوست دارم برای پرسپولیس بازی کنم.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/140018" target="_blank">📅 22:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140017">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e23b00c48.mp4?token=eUefW1R2DFUVTf7tM7gWxyoun6G2XIt64BMVFtbwlMJUOOMwFzBxluMxbs5fTewx_gdbKmcv7GiY8SIJzE8JOFbbc9ezQ5_Q3-Gbohmva-ozdkivuJu15Hc04LZopL5ogKv0uZ1T9plmXo50FrXGCm7AmpswFI3yE9PzAAs_pva7UhlUisO63moZFytaDLFMvN983SM4UdOBYoRccv2AUysQhB7wFlW3CPFowaFKtvuMybCGhBbtLSoU--CHwTxRlk5Ka0iA4CKccvH4TbZ9vvQWcgTBu_XfV8VyqK6qVyuJ2MQnjJwHfZ1XxnQHyUaVu1X73Vuo9v1NsbRgt8wGgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e23b00c48.mp4?token=eUefW1R2DFUVTf7tM7gWxyoun6G2XIt64BMVFtbwlMJUOOMwFzBxluMxbs5fTewx_gdbKmcv7GiY8SIJzE8JOFbbc9ezQ5_Q3-Gbohmva-ozdkivuJu15Hc04LZopL5ogKv0uZ1T9plmXo50FrXGCm7AmpswFI3yE9PzAAs_pva7UhlUisO63moZFytaDLFMvN983SM4UdOBYoRccv2AUysQhB7wFlW3CPFowaFKtvuMybCGhBbtLSoU--CHwTxRlk5Ka0iA4CKccvH4TbZ9vvQWcgTBu_XfV8VyqK6qVyuJ2MQnjJwHfZ1XxnQHyUaVu1X73Vuo9v1NsbRgt8wGgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
کنایه تیکدری هافبک پرسپولیس به شرایط ورزشگاه آزادی: قول داده اند آزادی را تا 10،15 سال بعد آماده کنند!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/140017" target="_blank">📅 22:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140016">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f06355658.mp4?token=YAHvn9YedH02joKOzUXtilm6Qa-5-cmGGjDNiq8Yco9h6rDz-EorVBxBb0M9tDeEPASZE1-EtqJtUcmjgS-kmHu9ywmj-ge0pfPL9P2FrwBdfEAMgkpRsylCL2zoqfuxgNiuWVDgRSYq0SYy86Of43Jq_hH_CJckbWhbytz3VeusyuGkxOc_9W1Qrvmm7K-PWzW5PtGe4WTLd0DeVPKT30hvH4hXnvyLUpRBRci-wJr0fwSDQvVLUNlEom9WJIz9a924FlukBnb74L4UX2E4PdKgG0TYtM2ElnZ4ZcpMGT6X2ZYeMKj0yFb9AArq8hQGF4SxMrJr-lweLbk5ILcSXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f06355658.mp4?token=YAHvn9YedH02joKOzUXtilm6Qa-5-cmGGjDNiq8Yco9h6rDz-EorVBxBb0M9tDeEPASZE1-EtqJtUcmjgS-kmHu9ywmj-ge0pfPL9P2FrwBdfEAMgkpRsylCL2zoqfuxgNiuWVDgRSYq0SYy86Of43Jq_hH_CJckbWhbytz3VeusyuGkxOc_9W1Qrvmm7K-PWzW5PtGe4WTLd0DeVPKT30hvH4hXnvyLUpRBRci-wJr0fwSDQvVLUNlEom9WJIz9a924FlukBnb74L4UX2E4PdKgG0TYtM2ElnZ4ZcpMGT6X2ZYeMKj0yFb9AArq8hQGF4SxMrJr-lweLbk5ILcSXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
خدابنده لو هافبک پرسپولیس: امسال متحد شده ایم که هم در لیگ برتر و هم جام حذفی نتیجه بگیریم و هواداران را شاد کنیم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/140016" target="_blank">📅 22:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140015">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12ff628214.mp4?token=UspKMdfzWLUmUhJaTofmjUiyB2WTL9nwz8nhGCm0yCKXkIjukYhcmc4gkgcLiyb0353FQf8HFIIB6HbWAqMSMowsGiInymKK7PTPnbR7WMFrk9FMENSRjZoc7vGwJVxeA-QBH1T_uNB11ZQm2wbSEUI4f-aFJ2J84OeO0oa9a9D-o9DMvlcrVTLKtZA5EnzW28xxbZrB47LVD2Ec5RW7KJ-3LLb1uVFPuoN7Ti52stsnxYzLnF4zZSb7dlaZI0Xa-8jPEsfk9WUF442RY-yfky7_QmlN9gbXLyQT3MdlaRvEjH6FAxRvNuIUN9nmWbbKWXqMn5LTPOsWCzL1k0ganA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12ff628214.mp4?token=UspKMdfzWLUmUhJaTofmjUiyB2WTL9nwz8nhGCm0yCKXkIjukYhcmc4gkgcLiyb0353FQf8HFIIB6HbWAqMSMowsGiInymKK7PTPnbR7WMFrk9FMENSRjZoc7vGwJVxeA-QBH1T_uNB11ZQm2wbSEUI4f-aFJ2J84OeO0oa9a9D-o9DMvlcrVTLKtZA5EnzW28xxbZrB47LVD2Ec5RW7KJ-3LLb1uVFPuoN7Ti52stsnxYzLnF4zZSb7dlaZI0Xa-8jPEsfk9WUF442RY-yfky7_QmlN9gbXLyQT3MdlaRvEjH6FAxRvNuIUN9nmWbbKWXqMn5LTPOsWCzL1k0ganA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
خدابنده لو هافبک پرسپولیس: از اردوی ترکیه به بعد ترجیح دادیم بیشتر کار کنیم و عملکردمان را نشان دهیم تا اینکه در فضای مجازی باشیم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/140015" target="_blank">📅 22:26 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140014">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e456b94978.mp4?token=ACdSC4vSmxZMedWJ9YHUzmAjPWvLSVWnUSgDQuo-60eDpj9gGPkNdec7lRkjT5U-bTuNNgQj04S_cp5vEmvpsf3II8kNcLrSGfV8SnqvS4zViKMaw_KjTSlvYpeiFNS3wdcHXE0W3HOl-VeQBR7uIBwa9ZtahpB9II-HOCa-zduza4AthMvOtyr6AuDfiWD7tbov_Pfl4X8zjEHMYk9DL4bPYw-5kB7hJe4MYZq4oHaDZR-1EwSrfTyhnyAnAA9FI08nWtgy12bVjRj0Oi8Bd3ara-h5cZVlapV4pbJonydkXqFL2SHE9EGTx5thi52mLv1bWRcrIe1YddZFVSJhXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e456b94978.mp4?token=ACdSC4vSmxZMedWJ9YHUzmAjPWvLSVWnUSgDQuo-60eDpj9gGPkNdec7lRkjT5U-bTuNNgQj04S_cp5vEmvpsf3II8kNcLrSGfV8SnqvS4zViKMaw_KjTSlvYpeiFNS3wdcHXE0W3HOl-VeQBR7uIBwa9ZtahpB9II-HOCa-zduza4AthMvOtyr6AuDfiWD7tbov_Pfl4X8zjEHMYk9DL4bPYw-5kB7hJe4MYZq4oHaDZR-1EwSrfTyhnyAnAA9FI08nWtgy12bVjRj0Oi8Bd3ara-h5cZVlapV4pbJonydkXqFL2SHE9EGTx5thi52mLv1bWRcrIe1YddZFVSJhXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
خدابنده لو هافبک پرسپولیس:
🔄
🔄
تا روزی که هواداران و باشگاه مرا بخواهد در پرسپولیس می مانم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/140014" target="_blank">📅 22:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140013">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98087f79b6.mp4?token=cKwh2v2atE-QssUhdiejdARr3DQppJ7puItirX2MF02w5AahRIeDhCz2FVf7BApki2Cym3Cmj3JtMI_8TKBDQn99sFFlb7XW7Y9UiIxIGUUYAPF4RrmoAvzNJAEko9iIJgFvfZGXWX7Tgu8ERF0TTR21XfbMJq9FMtNDkZa86geKcAOmmaZOU24yA390wvDOT8m-NLFg4ZrXmB-M_CdYUHULj5zRMTZ0AG0Bu6JiJCUKo8ugAw3p-PS1HiGhOKzcmcA6jeFgmaXQxbaDlfySpBMes_EhmysYSlYegO7sBnX4OytaL2CnEqnuLwgpnERNRRxgbgZJ4glKc48k8H3MxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98087f79b6.mp4?token=cKwh2v2atE-QssUhdiejdARr3DQppJ7puItirX2MF02w5AahRIeDhCz2FVf7BApki2Cym3Cmj3JtMI_8TKBDQn99sFFlb7XW7Y9UiIxIGUUYAPF4RrmoAvzNJAEko9iIJgFvfZGXWX7Tgu8ERF0TTR21XfbMJq9FMtNDkZa86geKcAOmmaZOU24yA390wvDOT8m-NLFg4ZrXmB-M_CdYUHULj5zRMTZ0AG0Bu6JiJCUKo8ugAw3p-PS1HiGhOKzcmcA6jeFgmaXQxbaDlfySpBMes_EhmysYSlYegO7sBnX4OytaL2CnEqnuLwgpnERNRRxgbgZJ4glKc48k8H3MxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
مهدی تیکدری بازیکن پرسپولیس:
✔️
امسال یک تیم گردن کلفت داریم و نظر همه  هم همین است که امسال حقمان قهرمانی در لیگ است
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/140013" target="_blank">📅 22:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140012">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9eb4ad0d3.mp4?token=rsLGMu3FcK4J5-qQppd3Lu1CnAuGUmgHXhRI90Rd6glpc7i3DEIKL_D50C74cxbmylFLolldyHaFD0tjHchz48z3LiXbRc67FmVptyNEzejsg_cDKkevCQ2P6fN_yPSTvUW1uHEyTy2f1fqGTERdsNQFzCX6Cv3s6Juls1gQSiNOl4UKTAePmEEQV-vH6xxw7KzGPUentmMfVFcdAvT3r-3zpaSm3r_0OTUam5VcijtFuuVRXHRmQ-SNfhMmnUZuXFp_KOBPidMvfrYXHf2XzsJEi5lKV2pVbHOp156Ny50wcW9lm4M7l8qJpRD9aP5mGzknq2erbnj2sxbu7H_2lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9eb4ad0d3.mp4?token=rsLGMu3FcK4J5-qQppd3Lu1CnAuGUmgHXhRI90Rd6glpc7i3DEIKL_D50C74cxbmylFLolldyHaFD0tjHchz48z3LiXbRc67FmVptyNEzejsg_cDKkevCQ2P6fN_yPSTvUW1uHEyTy2f1fqGTERdsNQFzCX6Cv3s6Juls1gQSiNOl4UKTAePmEEQV-vH6xxw7KzGPUentmMfVFcdAvT3r-3zpaSm3r_0OTUam5VcijtFuuVRXHRmQ-SNfhMmnUZuXFp_KOBPidMvfrYXHf2XzsJEi5lKV2pVbHOp156Ny50wcW9lm4M7l8qJpRD9aP5mGzknq2erbnj2sxbu7H_2lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بازگشا سخنگوی پرسپولیس: دنیل گرا در هر تیمی که قبل از آمدن به پرسپولیس بوده است کاپیتان آن تیم بوده و بازیکن بسیار پخته و باشخصیتی است!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/140012" target="_blank">📅 22:22 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140011">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e5221c79f.mp4?token=XYJXojXDpMwafgWx5Cill3wgRE5Hc2wgipPuQy-sWwkH-IL4Cc5ofxl70RBv1JavvmBGYfs8g_QAZWjmcmjTnbnvGstiHELKfSMynhLjmcBBLPSggRro3ip4On5V_G8_qPgWnkmv7ElnbfvYz_7p9nCG3_GgA-ArRTOH3IYmszAtRwU7niK_WQTIh8lUiM5_qKoK-1rb20xhi4bUjunMAElx5GCQ4oD1pWMODXobId9Pc4sukcNZytcJ98DVMO9ly3_39pSXNLatzjjxNptpLdLt6fZwusCRvuDCB4lpouDZrKVVqo6zgFyEqd3lsFBqVfVG9STCHhwyGcXmmMDojQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e5221c79f.mp4?token=XYJXojXDpMwafgWx5Cill3wgRE5Hc2wgipPuQy-sWwkH-IL4Cc5ofxl70RBv1JavvmBGYfs8g_QAZWjmcmjTnbnvGstiHELKfSMynhLjmcBBLPSggRro3ip4On5V_G8_qPgWnkmv7ElnbfvYz_7p9nCG3_GgA-ArRTOH3IYmszAtRwU7niK_WQTIh8lUiM5_qKoK-1rb20xhi4bUjunMAElx5GCQ4oD1pWMODXobId9Pc4sukcNZytcJ98DVMO9ly3_39pSXNLatzjjxNptpLdLt6fZwusCRvuDCB4lpouDZrKVVqo6zgFyEqd3lsFBqVfVG9STCHhwyGcXmmMDojQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
بازگشا سخنگوی پرسپولیس: ما باید تعطیلات فیفادی را با صدرنشینی لیگ شروع می کردیم اما نخواستند که به این شکل شود
💢
پاسخ سازمان لیگ را ندادیم و به جای آن رفتیم به فکر آماده سازی تیم خودمان شدیم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/140011" target="_blank">📅 22:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140010">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b66e5d4924.mp4?token=FqtN3nu3OyF3E4rgaNgqzHUlHjfZYY11NrVC-j_mB74kM1RVxn3axISNy4ub8L5lY88ixrXYb5WPQPgc0HvdwyHEahPLdGZ7X76sTwNBaDHD68TICTyhcOvOW9olykp2ph0OaGWnAbfwyL1IoR-F1ADvGchutGOgpY9yRFWh3TugEeH82I3HT85rUXUFu0KxYyS0Y8eM27aK7hGGfFELj159PRcsAn6XW_6LJQWwAvz_gV5QagY3FW70hEIXDQdUC68LoO76DfyeNiSKytB3hn6VwVYZ3UfL54fImIXipZOGbPVT4BPwszCNnNsNGr91Kmwp3decVaih0MqTUIEHdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b66e5d4924.mp4?token=FqtN3nu3OyF3E4rgaNgqzHUlHjfZYY11NrVC-j_mB74kM1RVxn3axISNy4ub8L5lY88ixrXYb5WPQPgc0HvdwyHEahPLdGZ7X76sTwNBaDHD68TICTyhcOvOW9olykp2ph0OaGWnAbfwyL1IoR-F1ADvGchutGOgpY9yRFWh3TugEeH82I3HT85rUXUFu0KxYyS0Y8eM27aK7hGGfFELj159PRcsAn6XW_6LJQWwAvz_gV5QagY3FW70hEIXDQdUC68LoO76DfyeNiSKytB3hn6VwVYZ3UfL54fImIXipZOGbPVT4BPwszCNnNsNGr91Kmwp3decVaih0MqTUIEHdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
بازگشا سخنگوی پرسپولیس: با احترام به وحید هاشمیان، تعداد مصاحبه های او از تعداد دفعاتی که روی نیمکت پرسپولیس نشسته است بیشتر شده است
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/140010" target="_blank">📅 22:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140009">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✔️
✔️
نماینده محمد عمری ستاره 25 ساله‌تیم‌پرسپولیس این بازیکن رو الشارجه امارات و لخ‌پوزنان پیشنهاد داده تا درصورت موافقت کادرفنی هرکدوم‌ از این دو تیم با عمری قرارداد امضا کنند. عمری علاقمند به لژیونرشدن در نیم‌فصله.  «سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/140009" target="_blank">📅 21:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140008">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
🔴
مهدی تیکدری (۲۷)، یاسین سلمانی (۵۹ پنالتی)، ابوالفضل زارعی (۷۰) و مجید عیدی (۸۵)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/140008" target="_blank">📅 21:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140007">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✔️
✔️
اورونوف در دیدار امروز نمایش قابل قبولی داشت، در این بازی یک پاس گل ارسال کرد و یک بار نیز تیرک دروازه حریف را به لرزه درآورد.
✔️
✔️
این بازیکن در طول دقایق حضور در میدان چند بار با حرکات تکنیکی و نفوذ از جناحین برای پرسپولیس موقعیت خلق کرد و از استاندارد…</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140007" target="_blank">📅 21:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140006">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvC0oXSvDw0mLLx_0MVwQKxHk4s-SyTPh_uqg_O0GJ_YnoBfNA3367WteOKkPDVnvonsW6hTn8GqdZLrCrxv4j4hiCupnSeRS18rvisO-XFNEyALuANYGHyHqJ_AlOmU3c0LOS8a5yA5KZsBhpWUVOD-TouwoyuOHENMeV3NpRD_oebCjL80pHiPDBzgrWA2wA2y97JyTZCnHoeVTkXsfWyyhW4u_3xjGL4zhAQbHasyDOY-Rz3tpFI-D58XsNWtd3La-k76xxWp_dzBXoyBKj5PGYUMvHOMtnjeA79mX6tA4GAl75VPGkQlgCRKb63hodyZzhporJbP_VujdAljlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
برانکو ایوانکوویچ، مربی کروات که اکنون به عنوان مدیر فنی تیم ملی امارات فعالیت می‌کند، با حضور در اردوی تراکتور در دبی، با سید حجت کریمی، مدیرعامل باشگاه، جواد نکونام، سرمربی تیم، و جمعی از بازیکنان دیدار و گفت‌وگو کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/140006" target="_blank">📅 20:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140005">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✔️
✔️
✔️
اطلاعیه رسمی قرارگاه جانفدای کشور:
✔️
از سه شنبه 24 شهریور ماه قراره هزار گردان مقاومت ملی تشکیل بدیم که شامل کسایی هست که جانفدا ثبت‌نام کردن.
✔️
قراره به این افراد آموزش نظامی و امدادی بدن تا اگه جنگ شد، فورا اعزام بشن.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/140005" target="_blank">📅 20:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140004">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✅
✅
اورونوف نمیخواد جدا بشه/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/140004" target="_blank">📅 20:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140003">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🏅
❤️
فووری از رسانه داریو ازبکستان: باشگاه تراکتور به دنبال جذب اوستون ارونوف وینگر ازبک تیم پرسپولیس در نقل انتقالات نیم فصل است
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/140003" target="_blank">📅 20:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140002">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihoCzbCI4SQk9LRjuvodI8AIW3gEo83yGKX0W-JYuUPS9XLbliLz6ixIVJCK40B1VczzcULPUT8cjg3sBqaAkm79wyOC2UerlhdjHx-uZcJCh58O_-9a0tVzPlymNEWAczuq82S4qNH4ZgcKNqk6IALdCvaKMgFlrrR-WXXK90m-Az_IbVQFjXY95ZJB5T08mm1Sty7E9UiAK3f08ATba9WPK67lGP_ml3csMMxtkzXGm9R2imc2YakzriniuJasNzL33UEg1s1vPdfDbUlLpHMFCJ2Q3c_jV5945g96sKAlxaPqqs8ZF6vMAenvUsrihnXAb--ARj5XNzW1iuYZBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
جدال نزدیک و نفس‌گیر؛ برست و پاریس برای یک برد ارزشمند امشب به میدان می‌روند!
[
برست
🔴
🆚
🔵
پاری‌سن‌ژرمن
]
⚽️
بازی برای هر دو تیم از نظر امتیازی مهم است و انتظار می‌رود محتاطانه شروع شود. پاریس روی مالکیت و کیفیت هجومی حساب می‌کند، اما برست در انتقال‌ها می‌تواند خطرناک باشد. با توجه به سبک دو تیم، تقابل نزدیک و کم‌فاصله‌ای می‌تواند شکل بگیرد.
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه تا سقف ۵ میلیون تومان دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140002" target="_blank">📅 19:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140001">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">⚽️
باشگاه پرسپولیس در دیداری دوستانه با نتیجه 4-0 تیم شهید قندی یزد رو شکست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/140001" target="_blank">📅 19:20 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140000">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EL5kvzbqcntYRnDvQ8rO8sOm70WTzHUuGWTXjbAhfdoMml0v-FjeDJ-uJF6h75OGKDNRoKStIW1vNpNxnbZB8QEVe9iosOFNvlsYl5cbWSFX2ijbC9XN39-BiU48gEsh5lh9UZZtvmlheXWWBa-_elo79R96OFRj4QqQdq7Q7TtKgsJqsHS4AL44lMId8zRgohUMeE8hbtP3mYHB11NCgG5y8hCN8LwOffj13mDbl0z_YWXlLVAnbjEOBtCBOFBd5LWJsWZkjbPRBX0LATL_ZB4KCmXs6h5k6G8e_mCywIbUvT1VjxBoqIt7VBX9HAVeITMSlDZ-oLHLkRT4SVP9GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
⭕️
⭕️
بیرانوند سرباز شد
😂
😂
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/140000" target="_blank">📅 18:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139999">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
سردار رادان: بیرانوند شامل قانون سرباز قهرمان نمیشود و از اول مهر سرباز است و باید یکی از تیم‌های ملوان یا فجرسپاسی را برای بازی انتخاب کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/139999" target="_blank">📅 18:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139998">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af9bbd8729.mp4?token=ZNEnxnCzk4KUI4m5044BKmE8mi5LvUZjQaP41ddgu2yd7t0NlVO--UZnMuEWNjzxTrp5DZwBf281cH_tERqZkNcikdu4-SVE7v6tVc3cixUT521E_wiD__MBLenpNPtgXUt-LWdARVif3cKG2wrvLpt9J4UA6qtk7k49JSIFRMO8o9Sa_-CLxEGEGevr9rPOK_AqnGpiz3OUKMJB1Nk0GZJE1wjaM0zwhY8yMM1kJeZLyxi0IS5MUlmUuMiBeTibda4Lo_nUB5l9UORqsxd9KgSlUS2gilg7JpvvjITGpc_qbb4L1TZE-D8p8QpvQ4w1yE4DKeJfOkQ67yfEEItgdjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af9bbd8729.mp4?token=ZNEnxnCzk4KUI4m5044BKmE8mi5LvUZjQaP41ddgu2yd7t0NlVO--UZnMuEWNjzxTrp5DZwBf281cH_tERqZkNcikdu4-SVE7v6tVc3cixUT521E_wiD__MBLenpNPtgXUt-LWdARVif3cKG2wrvLpt9J4UA6qtk7k49JSIFRMO8o9Sa_-CLxEGEGevr9rPOK_AqnGpiz3OUKMJB1Nk0GZJE1wjaM0zwhY8yMM1kJeZLyxi0IS5MUlmUuMiBeTibda4Lo_nUB5l9UORqsxd9KgSlUS2gilg7JpvvjITGpc_qbb4L1TZE-D8p8QpvQ4w1yE4DKeJfOkQ67yfEEItgdjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
سردار رادان: بیرانوند شامل قانون سرباز قهرمان نمیشود و از اول مهر سرباز است و باید یکی از تیم‌های ملوان یا فجرسپاسی را برای بازی انتخاب کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/139998" target="_blank">📅 18:37 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139997">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">⚽️
باشگاه پرسپولیس در دیداری دوستانه با نتیجه 4-0 تیم شهید قندی یزد رو شکست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/139997" target="_blank">📅 18:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139996">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✔️
✔️
✔️
اطلاعیه رسمی قرارگاه جانفدای کشور:
✔️
از سه شنبه 24 شهریور ماه قراره هزار گردان مقاومت ملی تشکیل بدیم که شامل کسایی هست که جانفدا ثبت‌نام کردن.
✔️
قراره به این افراد آموزش نظامی و امدادی بدن تا اگه جنگ شد، فورا اعزام بشن.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/139996" target="_blank">📅 18:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139995">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
تو 24 ساعت اخیر سرچ «لغو عضویت جانفدا» بیش از 5 هزار درصد افزایش داشته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/139995" target="_blank">📅 18:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139994">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9B2-DnDuzcmumUg8kDqRk17LcF1S2fDkmjE4mJMfV6g1SBr5KM0zo0lmJ2O3x1Q_Nb268khR7HN_VPqKvJyAyXoe17k0hYh_yQuzDd2xApcQFwJxk4ixqwHgc9Dvnfn-HNIfAlA5R6MWHDsci2L1swGurQ17-aG_GB6flQxGqbAoYImgevrDDuyWFSNQaH5YqhAS8BTmyawYv957CgZKEeQTo8pD70mZfz93M7CEEjk0ntqoUlWDjKQoEOVPhuBauuTlGbuH4vVQXaTosGaU2Hy-fWcQVWuHZZMYQ9eKwrt9jQoN5k0je74iKeZTnB4XPC7oRCyxWl3WaTX-3PTfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
باشگاه پرسپولیس در دیداری دوستانه با نتیجه 4-0 تیم شهید قندی یزد رو شکست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/139994" target="_blank">📅 18:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139993">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🗣
#یادآوری
✔️
✔️
هتریک بیفوما مقابل بارسا‌، گل‌هاش یکی‌از یکی قشنگ‌تره و خلاقیتش رو به‌رخ میکشه
✔️
✔️
وقتی تو سن ٣۴ سالگی جلو ملوان استارت شصت‌متری میزنه یا اون پاس‌گل جلو اس‌خوزستان میده از سر فوتبال‌ بلدیشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/139993" target="_blank">📅 16:57 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139992">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
حضور هانی نوروزی پسر زنده یاد هادی نوروزی، کاپیتان فقید پرسپولیس در تمرین تیم دهه شصت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/139992" target="_blank">📅 16:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139991">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
فارس: محسن نامجو با هماهنگی به ایران برگشت، احتمالا شادمهر عقیلی هم به کشور برمیگرده و حتی کنسرت هم میذاره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/139991" target="_blank">📅 16:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139990">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
از داخل ایران مدارکی به باشگاه السد ارسال شده که در صورت بازی کردن یاسر آسانی، ازش شکایت بشه
🤣
🤣
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/139990" target="_blank">📅 16:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139989">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✔️
✔️
دو ست و فعلا باختیم و واقعا زورمون به ژاپن نمی‌رسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/139989" target="_blank">📅 15:37 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139988">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✔️
✔️
میثاقی:
✔️
مهرداد محمدی یه چیزی گفت شش ماه محروم شد اما خداداد چهار ماه؛ ساکت الهامی هم شش ماه محروم شد!
✔️
یکی از دوستان حقوقی گفت شکایت قضایی این موضوع چهار ماه زندان دارد!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/139988" target="_blank">📅 15:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139987">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRmdRYGgAP3lA6R_qb8MR0lkI7OtbIJB7tnqMpZWLe2ejmK7SEtL28f50_bsYDqmPmOXBIhvZI6mOvwFvchFyluokPnGSQnNUasol_RheiNh--JKWLiCdVy01N8rZcJQ64lAQLJiFV1Gq4jOmKUCELUrwbL28GgtjvzzkfnR5HLpBfciluytgIBBbiIEe_xCf8zUxjuJ3ADGvwr2gYOpahGu4uDlSrXWn2Wg9lzVqGDiW6ftFGYuBUlO6DjRicNV3fgZ4efyx4YK36-Tg02s8bi5t32smSgnEL_P16uRsrpejee_mNWsDaKnMkDOEYk77Afl-7ODGTiZYLNbgwJOqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
پس از آنکه محسن خلیلی در ابتدا اعلام کرد: «جام حذفی برگزار نشود بهتر است»، حالا پیمان حدادی برای چندمین بار خواهان برگزاری این مسابقات شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/139987" target="_blank">📅 15:20 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139986">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✔️
ژاپن 3-0 کره جنوبی
❌
ایران و ژاپن فردا ساعت 14 برای کسب عنوان قهرمانی و سهمیه المپیک به مصاف هم میرن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/139986" target="_blank">📅 15:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139985">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/139985" target="_blank">📅 14:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139984">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
❌
❌
تیکدری: روز اولی که به پرسپولیس اومدم گفتم با تمام توان در هر پستی بازی میکنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/139984" target="_blank">📅 14:37 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139983">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ru4W3dk94fkKPYYIbLrBNXjiNVd_ZYeR2e6bqandzDKnGfbnm6uSkaa4tPDD5rf9a5gxntzO40EWuRM0KUPbd9P8BFvQaoArzYeVECJOIplsB4V9c0Q1a1TiBc3CXFxgZCmslL8xZ__-uKeOWgJxABb275pRp1rrFVQ05qzGNeOaQFcdT1YaBtwlFwRNXOFmXNA97RlNiIET_zdRQtuH46djx6eBQ4ngwxdO4b9j26DvTsNq5BDd9gVbQfmGh2PeYFQH8Ay89E_bc0m9sWUMHl3yiaY4ve82B2pV1ea2qwOwViJA925G-2JCSz2nnD77IxjiOkp2qWf37CPD0gxJqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
Man United -
🔵
Man City
⏰
Tonight 19:00
🏟
Old Trafford
🟣
منچستریونایتد در اولدترافورد با تکیه بر انرژی هواداران و ضدحملات می‌تواند سیتی را به دردسر بیندازد، اما ضعف دفاعی‌اش نگرانی اصلی است.
سیتی با شروع قدرتمند فصل و خط حمله آماده، کنترل میانه میدان و فشار روی دفاع یونایتد را هدف می‌گیرد؛ دیداری که پتانسیل گل‌دار شدن دارد.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
آدرس دائمی سایت:
👇
🟣
Wincobet.com
🤖
ربات رسمی مینی‌اپ وینکوبت برای ورود سریعتر به سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/139983" target="_blank">📅 12:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139982">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔥
⚽️
رکورد جالب پوریا شهرآبادی؛ شروعی درخشان در پرسپولیس!
🔴
پوریا شهرآبادی در حالی که تنها ۲۰ سال سن داره، تبدیل شده به دومین گلزن جوان تاریخ باشگاه که در کمترین زمان ممکن به ۲ گل می‌رسد.یعنی شهرآبادی برای زدن ۲ گل، حتی به اندازه‌ی دو بازی کامل هم در زمین نبوده…</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/139982" target="_blank">📅 12:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139981">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">💢
💢
بشار رسن هافبک عراقی پاختاکور که‌اواخر آذر قراردادش با این تیم به پایان میرسه از طریق دوستانی نزدیک خود به باشگاه پرسپولیس اعلام کرده حاضرست نیم فصل به پرسپولیس برگردد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/139981" target="_blank">📅 11:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139980">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✔️
ساپینتو : من و کلارنسس سیدورف مخالف ۱۰۰ درصدی جذب جنپو بودیم ، ولی تاجرنیا اصرار به جذبش داشت بعدا متوجه شدیم بازیکن و ایجنتش ارتباط نزدیکی با تاجرنیا دارن...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/139980" target="_blank">📅 11:01 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139979">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb6f48f178.mp4?token=E-AIcY0HEiITjO-mjzPn85no-RVqxTLLAZCmp3ONKHTE5_KOtBbOr29Hpg3zevPHogILRwW42HlvZFZ3dx4v68J_f-ZL9uDNdNtJjD9kx8T637geRj5YtcNW40gnf2fRcznQsmRIFvespekaQTR1e3st55Nqs2xhCvbmepf1id0HoFetlPGuL4ULxk3CNFQa3hTxtxfgnpT7G6QthF8yExSBGE-yObl3r-ZpUMZV-hv_Tj36Nyipgx2vdwFS_kRjNCoOzLwy4d7gBOm5at-SZnepICHKbJFufnlgfKFC8rH3RBGKia4UB8iLwjnsKyq2uQbo4ZywaMc5qOP08ChGig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb6f48f178.mp4?token=E-AIcY0HEiITjO-mjzPn85no-RVqxTLLAZCmp3ONKHTE5_KOtBbOr29Hpg3zevPHogILRwW42HlvZFZ3dx4v68J_f-ZL9uDNdNtJjD9kx8T637geRj5YtcNW40gnf2fRcznQsmRIFvespekaQTR1e3st55Nqs2xhCvbmepf1id0HoFetlPGuL4ULxk3CNFQa3hTxtxfgnpT7G6QthF8yExSBGE-yObl3r-ZpUMZV-hv_Tj36Nyipgx2vdwFS_kRjNCoOzLwy4d7gBOm5at-SZnepICHKbJFufnlgfKFC8rH3RBGKia4UB8iLwjnsKyq2uQbo4ZywaMc5qOP08ChGig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗣
#یادآوری
✔️
✔️
هتریک بیفوما مقابل بارسا‌، گل‌هاش یکی‌از یکی قشنگ‌تره و خلاقیتش رو به‌رخ میکشه
✔️
✔️
وقتی تو سن ٣۴ سالگی جلو ملوان استارت شصت‌متری میزنه یا اون پاس‌گل جلو اس‌خوزستان میده از سر فوتبال‌ بلدیشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/139979" target="_blank">📅 10:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139978">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ol11Y_HcwX155lbhMWYHseuqlzK87KCdVXQvl2qJeQFZHF32eG_jmoVRw0ZyaLttJANjPgAsCUe_Grrs68rG9B79-Er6w1BQRxhw4ZngfqshcQ1JQZ6ykCMognX-hZTtwknvWJnAvr-whYcWTx3aIAqdABNjGXT_RPZjwiDzd6wUQkSLNAVQThCHyGdKmfAZOxA0lqPz9mNCgxrJI9qyx3D8MzaWSLHRtHEuuUpughb-UUfRfqsf-zk6xo76anB415wgVT61n0fhfAZfe9kzJnOWg-yk2YoQ7GZWtNf65EKAra48-XoBPSGABKneFbu0iDiS1kCVXV2R7hABbmVSqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
کاروان تیم فوتبال گل گهر امروز برای اولین بازی خود در لیگ قهرمانان آسیا مقابل الجزیره امارات راهی تاجیکستان شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/139978" target="_blank">📅 10:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139977">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nX1s36o2W5PqqvbDP7Iglk45dzWeKTohqnlE29OA7vgQXStBK0Sxg-JepPyeVUp7tQwZazULbgz5tKaKzUCoK1vtz1OM6saU0AH5zUkGslMHJPspNEJY98F2mtXYcu94XKT6lf0ye-q7qro_aBvaPqu-ET1TJGDmGv4roJ7sJ0P-TG8u4i3LcSswcFuVHuqEF2dbZP9qMcZI2zsr94xGNKrW2PuU6xHYQybTVOg14E7IxevoEZctcC79DWmC60JHcOk-eosZrUuY5xsZEe5yKVB0RNcx9UAxTEFH_W3BOJ4l-BYJ8viGwdc4YFqJoMgLpD_20gtWtjZJTOM7U2diIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
پرسپولیس امروز عصر در دیداری تدارکاتی به مصاف تیم شهید قندی یزد می‌رود. این دیدار در زمین شماره ۳ آزادی و پشت درهای بسته برگزار می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/139977" target="_blank">📅 10:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139976">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🗣
🗣
🗣
🗣
🗣
🗣
حمید درخشان: هیچ‌کس در باشگاه پرسپولیس دوست نداشت موفقیت من را ببیند. همین‌جا در خبرورزشی با صراحت می‌گویم چند بازیکن آن زمان پرسپولیس کم‌فروشی کردند تا تیم نتیجه نگیرد و با حمید درخشان موفق نشود.
✔️
✔️
امیدوارم این بازیکنان حالا پس از گذشت ۱۲ سال جواب…</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/139976" target="_blank">📅 10:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139975">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">💢
درخشان: بازیکنان پرسپولیس هنوز به هماهنگی کامل نرسیده اند. قطعا پرسپولیس در ادامه لیگ بهتر می شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/139975" target="_blank">📅 10:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139974">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vi9DTrtHGkc-4kPbsBNEjwo5bZVgTnsVAzi3O6a9LORh9BIwKxNzGMkEZdL9tKqgPNSzASQAE14H_SNPMbG4TT3dtaiB0HYiqKM8i3n6j-Dl8LtStLADHmvrWsXwjJHytdUOpTPC53-RiAagjbYJDqg7Xestef5G2PTQ42I55Qxs5WAD_mGqQ1T6azPaT5iqS0HcMmk8srYSOfyDxtRhwLD__A0Hdk4Uv3fRYlcWfYsfOtkhvfdP-zBIprmt9Qfe5SchGM0ptyTGKdXPB8OZpDbtKIkdguwNq0a0Rpihc00Z5XdspsVxOkxekF_xWrJN6t0rlJonna9u5RVlPdrKqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗣
🔴
❤️
پیمان حدادی:
🔻
بازی با خیبر را لغو کردند تا یک‌ماه دیگر به صدر نرسیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/139974" target="_blank">📅 08:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139973">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTYOmLM0wFMit1JDhXXMXaN6S42Em8noA3N-v7petHJsKeUVR8nOejp9x-sjEzCmeUVhoC_yv5S4zNfMfTz8Zq7tR7FH_jvtc5rmby12Zihbiajwhkg0zCNjElzpHV6UWxNPnLOVXz78OMF9LLZklOgralh2QxYqMDXxth-J8hmfxrXKc0j8GjaVUeleo6UOcvcslQc6YVwnW89WZ53NGavwAa0H8XLWhHbSX7q8pf8wIU25BdjbSO-Mv_Z7Rnh19BKdkbvia1kvBcUowd_vuddbnfEtU1UgfwzDdNVpx2m3GWSypIXBfryzDBqXZIoDQ72c7Bxtqt4o2v98URuoWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/139973" target="_blank">📅 08:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139972">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✅
می‌خوای پیش‌بینی کنی، ولی نمی‌دونی چطور حسابت رو شارژ کنی؟
وینکوبت کار رو برات ساده کرده!
با درگاه بانکی اختصاصی و امن وینکوبت، حساب کاربری خودت رو به‌صورت مستقیم شارژ کن و مثل هزاران کاربر دیگه، بدون دردسر از امکانات وینکوبت استفاده کن.
🎁
بونوس ویژه اولین شارژ:
فقط با یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و به موجودی اصلی حسابت اضافه کنی.
🟣
آدرس سایت وینکوبت:
wincobet.com
🔗
همین حالا وارد مینی‌اپ وینکوبت شو و اولین شارژت رو انجام بده:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/139972" target="_blank">📅 01:22 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139971">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13b9033e7e.mp4?token=L_xv03iRTUY6QSu0xDz0eoTm15hSQl7i6W3Qcgnrc98YvmVqBQakj06usgDaA6tK49DI-zO_oMW5lq5PlrK_Das_OYy40lbb4Kv4rZYhMGpiyOlvQaQKg6Nol1HMlfyhjkqjzX5dxCjKaOdaGWX4Yums4UP_RU-VfhWuf7KY0p22cfrJy2zxjWktawhXCfI0P9NGeZWM8Nrdnz0STlOoRTHZcFfNe9THH5p24QMb9ZqDl7YKUQsQXwHQEiMpqHZzBuYz5YgvE9PFUoo1TC2nr-DeLTSkAaJNqTPE6syMd09K10Krs10-hUQ5SJcDg3de5FjC727cyvNtKxnXjsHhhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13b9033e7e.mp4?token=L_xv03iRTUY6QSu0xDz0eoTm15hSQl7i6W3Qcgnrc98YvmVqBQakj06usgDaA6tK49DI-zO_oMW5lq5PlrK_Das_OYy40lbb4Kv4rZYhMGpiyOlvQaQKg6Nol1HMlfyhjkqjzX5dxCjKaOdaGWX4Yums4UP_RU-VfhWuf7KY0p22cfrJy2zxjWktawhXCfI0P9NGeZWM8Nrdnz0STlOoRTHZcFfNe9THH5p24QMb9ZqDl7YKUQsQXwHQEiMpqHZzBuYz5YgvE9PFUoo1TC2nr-DeLTSkAaJNqTPE6syMd09K10Krs10-hUQ5SJcDg3de5FjC727cyvNtKxnXjsHhhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔴
آرش فرزین: پرسپولیس خسته را پدرم به عشق پروین خواند  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/139971" target="_blank">📅 00:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139970">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✔️
✔️
‌ ۵-۶ بازیکن از پرسپولیس در فیفادی جاری به تیم ملی دعوت میشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/139970" target="_blank">📅 00:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139969">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✔️
✔️
تعطیلی ۲۵ روزۀ لیگ برتر
🗣
🗣
لیگ برتر حدود ۲۵ روز تعطیل خواهد بود. بخشی از این تعطیلی نسبتاً طولانی به دلیل همکاری باشگاه‌ها با تیم ملی امید است و بخش دیگر نیز مربوط به روزهای فیفاست که از ۳۰ شهریور تا ۱۴ مهر است.  «سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139969" target="_blank">📅 00:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139968">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
🔴
پرسپولیس موفق شد امتیاز تیم دسته اولی فولاد نوین رو بخره و تبدیل به پرسپولیس ب خواهد کرد و سید جلال حسینی هدایت این تیمدرا برعهده خواهد گرفت/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/139968" target="_blank">📅 00:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139967">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✔️
✔️
✔️
درخشش بشار رسن در ازبکستان ادامه دارد؛ هتریک پاس گل این بازیکن در دیدار روز گذشته تیمش که با برتری 3 بر صفر پاختاکور همراه شد
✅
✅
آمار او در این فصل : 25 بازی، 4 گل، 9 پاس گل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/139967" target="_blank">📅 23:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139966">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✔️
ساپینتو : من و کلارنسس سیدورف مخالف ۱۰۰ درصدی جذب جنپو بودیم ، ولی تاجرنیا اصرار به جذبش داشت بعدا متوجه شدیم بازیکن و ایجنتش ارتباط نزدیکی با تاجرنیا دارن...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/139966" target="_blank">📅 23:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139965">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❤️
پیمان حدادی: وقتی لیگ تموم شد و به همه جا اعلام کردن نیمه تمام هست، هیچ جای دنیا پس به تیمی جام نمیدن و خیلی غیر منطقی هست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/139965" target="_blank">📅 23:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139964">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✔️
✔️
ریکاردو ساپینتو؛سرمربی سابق استقلال:
🔻
من با مدیران زیادی کار کرده‌ام اما تابه‌حال مدیری به شهرت‌طلبی و دروغ‌گویی علی تاجرنیا ندیده‌ام.
✔️
✔️
از روز اول تاجرنیا به رابطه من و مدیرعامل وقت آقای نظری جویباری حسادت می‌کرد و انتظار داشت من مسائل تیم را با او…</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/139964" target="_blank">📅 23:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139963">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/139963" target="_blank">📅 23:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139962">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✔️
✔️
ساپینتو: پیشنهاد عجیب تاجرنیا برای استقلال!
✔️
✔️
ساپینتو مدعی شد تاجرنیا به او گفته قرار است سعید فتاحی به استقلال اضافه شود تا با توجه به ارتباطاتش با داوران، مدیران سازمان لیگ و فدراسیون، مشکلات داوری و برنامه‌ریزی مسابقات را به نفع استقلال حل کند و…</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/139962" target="_blank">📅 23:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139961">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❤️
پیمان حدادی: خیلی ها آرزوی قهرمانی دارن اما پرسپولیس در ۸-۹ سال اخیر ۶-۷ جام گرفته. بازی ما رو لغو کردن تا صدرنشینی ما یک ماه عقب بیفته.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/139961" target="_blank">📅 23:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139960">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❤️
حدادی: هاشمیان قبل و بعد از پرسپولیس کجا مربیگری کرده است؟ دوستان در یک سال، سه بار او را دعوت کرده‌اند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/139960" target="_blank">📅 23:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139959">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✔️
✔️
دکتر حقیقت: محمد عمری تا ۳ هفته‌ی دیگر به تمرینات برمی‌گردد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/139959" target="_blank">📅 23:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139958">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
از داخل ایران مدارکی به باشگاه السد ارسال شده که در صورت بازی کردن یاسر آسانی، ازش شکایت بشه
🤣
🤣
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/139958" target="_blank">📅 22:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139956">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✔️
ژاپن 3-0 کره جنوبی
❌
ایران و ژاپن فردا ساعت 14 برای کسب عنوان قهرمانی و سهمیه المپیک به مصاف هم میرن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/139956" target="_blank">📅 21:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139955">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEnJJAnmkLaEVnKBlZo5f4DKj3hAVs4hkAgYP1BSss06WZGxAHxvYiUfuoCRdKTuCmQP9wSKGsvHZcp8QFN-WPJQTVqZ2YOKcUl327rB_IA9w7jzoQd2lL1VOE0HDQRt8aK2VW2jrh5ceMLCNazj7lvSBsClUOYecO7q32bdX-AA4mjRN74OKbE6S-dGi2wSPVdhAglF6adYz_1KMFC8rpOU3ct5RduxfF9D8HogPCk-qsS0cIHyMo8F_MiKIA9KEAmfmQJ0h8dQD6dI4rJVi94GvDXT1l7m8827n5kjeaLD6Qg7mBS6Q9AIPqLCqQ1jT6A9JTVAe0ujLE_SPazfzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تصاویری از تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/139955" target="_blank">📅 21:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139954">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6060af132f.mp4?token=fZvbGBe6VAU7EVB6KS4k1maBRVCa7YxTH_tIOIvmZdICTrzO83cxmTTwystmsj-Syz-X7IQZUw7h3LS29N9OBHTn-dwPCA7uo8JJ6KydJXSK6eUfm3gSnV9SuzCm2u41okTj9-ydr--2R0rcIW45wdN6yT2GjUkr8bJRiSyc7wOQqojGicJrAurxXaAAGuJyu5vl4SiikYXIhVVVl0Ydrv1THRx4obpBdrwtxw6Fz8DxVBPaKwzbkqouoKZuLFdZEIqk4_KX3O95Pgk2zujxqqbTq1zj2JBVm79YVA6BIDWgBmB1CAhYlUiugUfDexsMSgrWp7act23Ja4ALtIN6OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6060af132f.mp4?token=fZvbGBe6VAU7EVB6KS4k1maBRVCa7YxTH_tIOIvmZdICTrzO83cxmTTwystmsj-Syz-X7IQZUw7h3LS29N9OBHTn-dwPCA7uo8JJ6KydJXSK6eUfm3gSnV9SuzCm2u41okTj9-ydr--2R0rcIW45wdN6yT2GjUkr8bJRiSyc7wOQqojGicJrAurxXaAAGuJyu5vl4SiikYXIhVVVl0Ydrv1THRx4obpBdrwtxw6Fz8DxVBPaKwzbkqouoKZuLFdZEIqk4_KX3O95Pgk2zujxqqbTq1zj2JBVm79YVA6BIDWgBmB1CAhYlUiugUfDexsMSgrWp7act23Ja4ALtIN6OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
صحبت های وحید هاشمیان علیه پیمان حدادی:  حداقل درویش از مدیریت الان مرام بیشتری داشت و به نظرم برکنار شد چون من را برکنار نکرد. چطور برای اوسمار این چنین مراسم بدرقه ای انجام دادید ولی با من این گونه برخورد شد؟  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/139954" target="_blank">📅 21:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139953">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✔️
✔️
السد در 4 بازی اخیرش 19 گل زده
🔥
پ.ن یعنی دوباره قراره عروس بشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/139953" target="_blank">📅 21:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139952">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ee53113a6.mp4?token=NVzDvAJxAQjh3YPMoC1Cqliwp0iItQu8AuOfd4Ow_gLMn952tjL-j03A_tGx0EK9BU38KTXhzoVd3BETsgiZqhD5JNR6wtn5RJ4asNo5JJHxl4JRojH9ITRO58dOMjVgNVIfnLhndqIT8J1B4UvTrhBYmXVqUz8pLDNFCEtH1QYe6MbdO3QMztpHNFCOY6cSn41M27Nyym22uqyUMNQlmUa10EtG9tItARptERmxyPdeKfpO2y2yhd5phheau5J5e9fXBmDhn1YHZf7RJ-3y55JZq9h1Rqdbyfl3RM0FuC0N7VOtSJssP8a4xne7vowZqy_YUn4tFmiU0rS-Qc6MXRYzySx0LXRmf6eq77e8AUpVdFz6d9qQ56P3Ai9NXYMybaG8RkN--UM9CSfl7-O5TI2ih4ZDQAkr6MP60vDr5Y5vu6ycxr3gajDncPrIzDXQoVBNK3ndaV_JfePWe9f2hqhMePL18wvZrKnSdmF4YZCMWQyrR6nVC2wjGwHK_e8bN9azG04GzuUDEJKeWqVLfqTmYoagsooAri7-WdmI42f0QpKtPK69g3Kk77LrgJ-3VF0aLDQdtB-iXvJEoQJUuYJfBjxOdqjWjbnoF5z6KGZ3a-1MMaywWxc3cSGev1J_sTUAQwwhTNfcXs_ZiOetPZh5ZxIDV_O4VNiDUBP13aU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ee53113a6.mp4?token=NVzDvAJxAQjh3YPMoC1Cqliwp0iItQu8AuOfd4Ow_gLMn952tjL-j03A_tGx0EK9BU38KTXhzoVd3BETsgiZqhD5JNR6wtn5RJ4asNo5JJHxl4JRojH9ITRO58dOMjVgNVIfnLhndqIT8J1B4UvTrhBYmXVqUz8pLDNFCEtH1QYe6MbdO3QMztpHNFCOY6cSn41M27Nyym22uqyUMNQlmUa10EtG9tItARptERmxyPdeKfpO2y2yhd5phheau5J5e9fXBmDhn1YHZf7RJ-3y55JZq9h1Rqdbyfl3RM0FuC0N7VOtSJssP8a4xne7vowZqy_YUn4tFmiU0rS-Qc6MXRYzySx0LXRmf6eq77e8AUpVdFz6d9qQ56P3Ai9NXYMybaG8RkN--UM9CSfl7-O5TI2ih4ZDQAkr6MP60vDr5Y5vu6ycxr3gajDncPrIzDXQoVBNK3ndaV_JfePWe9f2hqhMePL18wvZrKnSdmF4YZCMWQyrR6nVC2wjGwHK_e8bN9azG04GzuUDEJKeWqVLfqTmYoagsooAri7-WdmI42f0QpKtPK69g3Kk77LrgJ-3VF0aLDQdtB-iXvJEoQJUuYJfBjxOdqjWjbnoF5z6KGZ3a-1MMaywWxc3cSGev1J_sTUAQwwhTNfcXs_ZiOetPZh5ZxIDV_O4VNiDUBP13aU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حدادی: بازی خیبر را عمدا به تعویق انداختند تا روند پرسپولیس را متوقف کنند!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/139952" target="_blank">📅 21:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139951">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❤️
❤️
حدادی در بین هواداران، بعد از بازی با ذوب آهن.
✔️
هوادار:
❌
دمت گرم با این تیمی که بستی، تا آخرش همینجوری وایسا.نیم فصل دو تا ضعف رو برطرف کن، بخدا تا آخر فصل ازت حمایت میکنیم.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/139951" target="_blank">📅 21:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139950">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
از داخل ایران مدارکی به باشگاه السد ارسال شده که در صورت بازی کردن یاسر آسانی، ازش شکایت بشه
🤣
🤣
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/139950" target="_blank">📅 20:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139949">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
پرسپولیس فردا به حای بازی لغو شده با خیبر احتمالا تو یه دیدار دوستانه به مصاف تیم شهید قندی یزد میره و بعد از اون تمرینات مدتی کنسل و بازیکنان به استراحت میرن  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/139949" target="_blank">📅 20:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139948">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FY-c_dws0UVKLfUxh9qZa8vEp2bbIpeNiDCtEcey5V8MjPP5StSrABU7l7I26w8hR1OK4u3WAVcqfziL7U4V7NxIOTKD-5nHFUaBydUCs31gFF_NoMlSpaAbvc-5yRI10SYzGjDuwS5S-CqpqdFim6--_9xTvN79bnEp5wMp5Ed5LEYA2p35WOyz9yGBqUjZ3lMXmJDwnbcLox0MN0LVA6VSM77SPy4-eOufqqhz61TfQv1KM7wpRVV87gcQJi5bYdwZgQFe7eZsfTCmcrtYqLNFWEvLVWtZ-ccM91ni49AvUO_UM2uPvxVBfueH1l5Oo8bpdOi2SCnrew0GdYPZhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پرسپولیس فردا به حای بازی لغو شده با خیبر احتمالا تو یه دیدار دوستانه به مصاف تیم شهید قندی یزد میره و بعد از اون تمرینات مدتی کنسل و بازیکنان به استراحت میرن
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/139948" target="_blank">📅 20:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139947">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s96q17FnDlajp3ZHcfY8QvwgHJUKT2-4s0XbkLm5zTcTxCTUB9ifnWS65jHUQOqvN-ch1Sa2GEnuqRpCiDBLsIfmAFsOxu0O3X21vC3UHRxEncj6CZiWaEm0pU8_JNtdC4UWgy9LQypiF4-6S3R_2SWLoKM508tSrlHgRcny3IxaeOQp_dE_nfEyt79ztsva-Jg9ZMKVM58jeGYU96ZOfkSRtwjXiALFc-wmBap3JQ-x8fvGRhdDzSVR1HC1qTUpz3JiRN1bXX1JbJZ3JAmN2xX7ZmXlqgXlaAXZyr5ZcHPVmTVf_mO2PlvigTfsAy2B_tY2kexxCggHn8cSD9yBXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
Real Madrid -
⚪️
Rayo Vallecano
⏰
Tonight 22:30
🏟
Estadio Bernabèu
🟠
رئال با برتری کیفیت فردی و مالکیت توپ، از همان ابتدا برای کنترل بازی جلو می‌آید.
رایو وایکانو احتمالاً با دفاع فشرده و ضدحملات سریع، سعی می‌کند ریتم رئال را برهم بزند.
کلید بازی برای رئال، باز کردن لایه‌های دفاعی رایو و استفاده از فضاهای کناری خواهد بود.
با توجه به اختلاف کیفیت دو تیم، کفه ترازو به سود رئال مادرید است و شانس بردش بالاتر به نظر می‌رسد.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
آدرس دائمی سایت:
👇
🟣
Wincobet.com
🤖
ربات رسمی مینی‌اپ وینکوبت برای ورود سریعتر به سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/139947" target="_blank">📅 20:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139946">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✔️
✔️
فوری؛ در آستانه بازی استقلال و السد در بصره عراق، به دستور نخست‌وزیر عراق، تمام مرزهای عراق با ایران بسته شد و پروازها نیز به حالت تعلیق درآمد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/139946" target="_blank">📅 18:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139945">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a080739df.mp4?token=jEGZNBVhpQXP3SRiNDv8MnYXR_keloPt4ZlN6gmFF0VzJsk4Xb8wUMlGmEu3B6t4xGDfcggvCakHZ5p21-FJLENHFeCMT3pJzzuOhdHfiwRnq5UMok-ZfigOtihR9-9Tlxwa6MOTfmJCyVIsHmt2hjof8NfgatheONAYTcduDMhFyQHLfQbP29D2RPuznocKE6g6jK8An6vMN3qNAiot7Uss-jjT9di33EP4-MH5TAdULUPstczHxsusUOlSRenD5pnS52WvvEaLlV55rKtZS89EIO7tq3N3nAocnBaX_pO45hSI4tO3j3bjfT1xiCHP4cgDGu5n-eIZt1RoPigZZalL4mP7BtLls1RTgxgvLhmhsp04n9NedPt_dGq2pvFM0Bb7vWoiXW0mxFqa0PeNEDKecXEZlNJgr1mW_b7Qb__acBeQ_vsTcS4P0c25VREOZSiDPSMzWIVNKzTxz9-q3vOSZ8cnF1LN0ARM-nonn5eh6V4DUiz8RKbs3HIgsz5UTaVM2WkVI3nkejKigdxyemDHvLuSUURDUS1cWu8BWa1MPefzRzNmD9YxL7xVfP1xDvPFdDDHnlZGdbGejHJYdw5IulrqBeRUiMqXQ00Ns_pmkKJneIExFz41CGGGYjjn8AblfEhogbWmrSyHVbQUHQr25NcGrj5ixgpGI0TiX18" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a080739df.mp4?token=jEGZNBVhpQXP3SRiNDv8MnYXR_keloPt4ZlN6gmFF0VzJsk4Xb8wUMlGmEu3B6t4xGDfcggvCakHZ5p21-FJLENHFeCMT3pJzzuOhdHfiwRnq5UMok-ZfigOtihR9-9Tlxwa6MOTfmJCyVIsHmt2hjof8NfgatheONAYTcduDMhFyQHLfQbP29D2RPuznocKE6g6jK8An6vMN3qNAiot7Uss-jjT9di33EP4-MH5TAdULUPstczHxsusUOlSRenD5pnS52WvvEaLlV55rKtZS89EIO7tq3N3nAocnBaX_pO45hSI4tO3j3bjfT1xiCHP4cgDGu5n-eIZt1RoPigZZalL4mP7BtLls1RTgxgvLhmhsp04n9NedPt_dGq2pvFM0Bb7vWoiXW0mxFqa0PeNEDKecXEZlNJgr1mW_b7Qb__acBeQ_vsTcS4P0c25VREOZSiDPSMzWIVNKzTxz9-q3vOSZ8cnF1LN0ARM-nonn5eh6V4DUiz8RKbs3HIgsz5UTaVM2WkVI3nkejKigdxyemDHvLuSUURDUS1cWu8BWa1MPefzRzNmD9YxL7xVfP1xDvPFdDDHnlZGdbGejHJYdw5IulrqBeRUiMqXQ00Ns_pmkKJneIExFz41CGGGYjjn8AblfEhogbWmrSyHVbQUHQr25NcGrj5ixgpGI0TiX18" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔴
آرش فرزین: پرسپولیس خسته را پدرم به عشق پروین خواند
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139945" target="_blank">📅 18:03 · 21 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
