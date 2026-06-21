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
<img src="https://cdn4.telesco.pe/file/t0KcSQto0wd6VIETfBSci394CBkk6nabhXGRqwlh9amFdrLD1RNalRlLL8avjZzsxftQ7_m7_InDfoyTLThxc7EyTDMFy5HM8z_vASGN5iKyh6pVAcr4IEMaIt0p_lBnrbIRTrMThNB4l_4l-pddgBAV7-imVOCMpxGZh-RaBugwynhA7nMPDLAFbSMq6y0av9IAiQ5oGpwZFz48nMkpd5KDBU_4bVqPW14x6TR_CN4xB-PQwC5LQa2ccCXpHhxap1Vto5JeUImlYY5yhIj_9Jl15nDFGNJQxvqRFNj2ARlD0K0FEqKB-r7DuUnwsKWiImXQUjXsX2UmueUAyACOog.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 10:56:56</div>
<hr>

<div class="tg-post" id="msg-133992">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❌
دانیال اسماعیلی فر ۱ ساله با تراکتور تمدید کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 561 · <a href="https://t.me/SorkhTimes/133992" target="_blank">📅 10:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133991">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
با وجود توافق اولیه بر سر مبلغ قرارداد، طبق پیگیری خبرنگار تسنیم مذاکرات بر سر دو بند همچنان ادامه دارد و توافق در مورد آنها تا این لحظه حاصل نشده است. طرفین امروز بر سر این دو بند که مربوط به مسائل مالی نیست؛ مذاکره می‌کنند تا در صورت توافق، قرارداد رسمی…</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/SorkhTimes/133991" target="_blank">📅 10:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133990">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❗️
ادامه مذاکره پرسپولیس با اسکوچیچ بر سر دو بند؛ امروز؛ صحبت نهایی
🔴
مدیران باشگاه پرسپولیس پس از انجام صحبت‌های اولیه با دراگان اسکوچیچ، بامداد روز گذشته (شنبه) برای مذاکره حضوری با این مربی راهی ترکیه شدند. روز گذشته  مذاکراتی جدی بین پیمان حدادی مدیرعامل…</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/SorkhTimes/133990" target="_blank">📅 10:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133989">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❗️
مذاکرات میان اسکوچیچ و حدادی مدیر عامل پرسپولیس روند مثبتی داشته و اگر اتفاق غیرمنتظره‌ای رخ ندهد، اسکوچیچ به‌احتمال فراوان در روزهای آینده به‌عنوان سرمربی جدید معرفی خواهد شد./فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/SorkhTimes/133989" target="_blank">📅 10:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133988">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
هواپیمایی حامل هیئت ایرانی به سوئیس رسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/SorkhTimes/133988" target="_blank">📅 10:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133987">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
✅
تاجرنیا: باید استقلال رو قهرمان لیگ معرفی کنند، ما حاضر بودیم لیگ برگزار بشه ...!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/SorkhTimes/133987" target="_blank">📅 10:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133986">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
✅
ورزش سه :  طبق تصمیم فدراسیون و سازمان لیگ، لیگ برتر فصل آینده با حضور 18 تیم برگزار می‌شود و از لیگ ناتمام امسال، هیچ تیمی سقوط نخواهد کرد و قهرمانی مشخص نخواهد شد .
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/SorkhTimes/133986" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133985">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
🔻
پرسپولیس با اسکوچیچ تموم کرد / قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/SorkhTimes/133985" target="_blank">📅 09:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133984">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqqH6NRVntloq1w9bEgIW7l3n9vFM2_w0URqv-YlFgtKdHgb8jZ5NaZ7VVzeAZGzpmt4TKY4VfHE-LZyYR1O9dboTqbCgl7JGeSBtNABPvDq83uVv7yUwg6GMEHJSGj1QI6_9PhR5pEjYYvhdflajMXjdPY7k8GQhmSZBvRKKqSlqY0-I2TvcstWw8kJa1KPtbcJHLEJG8jqYop3IfPkPYqzxuzYaM6mwxbAv1TnkBSx6zSt8J6_AsB4pLZZZ0NtYfJXETQ91mQbPYEuhFNKcluFuYpXqy61s4BX3cmoNgd6SZ6d3ulRYBbh3Lys2hisTLt3FxU-lIgo9WDSguTmYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
امروز 21 June، روزِ جهانی دلتنگ شدنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/SorkhTimes/133984" target="_blank">📅 09:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133983">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVJg76Ith26XAxUgQ47SCl6iosv_VE_zqHdaKWeEzKurLfkfkErNNVlXyFZieecDGOzW9ag0nAdE_YRKmmclZaeOSSLrgUxz4fFf333i2qp8mBhp8oM0-OTyhFpqskRBIq-MWl_uhOSXu94ZRPjIK2ZF0Q2_ASlihUk1YlhLOwizbX8eAWyVeG0LSFe6ZWhRDJWTIE4vlX2c-CZSbCQ56jOiZzDZra1mQtiAMJ6NOwQheFrwrlAhjSQjVGD-BxveHigS-Qy7s1Af5DWxHSOXtyXLm2L2VUvgme8Mne-qxPaFE8exUxZJ_FNo1tD2-aWlpGMb4jE9hy8j9AR8TR9oJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس ویژه جام‌جهانی
6⃣
2⃣
0⃣
2⃣
همراه با وینکوبت ادامه دارد!
🔴
Tunisia -
🔵
Japan
⚫️
جام‌جهانی گروه F
⏰
بامداد یکشنبه ساعت ۰۷:۳
۰
🏟
استادیوم بی‌بی‌وی‌ای
🎁
🔣
5⃣
1⃣
بونوس ویژه به مدت محدود روی تمامی واریزها فقط با یک گردش روی حداقل ضریب ۱.۸ به موجودی خودت اضافه کن.
⏰
این بونوس ویژه وینکوبت فقط تا دوشنبه ۱ تیرماه ساعت ۲۱:۳۰ فعال است.
📌
همین حالا وارد ربات وینکوبت شو و ازین بونوس ویژه استفاده کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/SorkhTimes/133983" target="_blank">📅 02:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133982">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lAqVsVh-tDvD6wqHGbNl4O6dQAb1usnmKfy94xG_K0Gcs8GQAIKu9f1KRpZZRbTnMRQaDjENYKULtvPFuiE-VjoiWALUqhtCH4GJRyt28IWg_eR-Dg2BCsGF8Tt6vvDPj8IOnIKxyozZaLgpe64RJyQIhDSCdzZg_bsQLyyXzPXKEgzJh4pY8gD5GvwIbIMVXjUHbRBF2qSD12xCleIsHWH7yIkxKCrXZxTEHkXuC6SlF2DXeXZMx4zivbQZ8aIoPcMDYtauEI2dKdA2iUctNVWYJAkal4yiRUQ8OA6gb4H8BRxE75MC8204-DOccbNjLUkHct1owRI0GMoxO0LY_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پیش‌بینی اپتا از نتیجه بازی ایران و بلژیک
🔴
سایت اپتا براساس ۱۰۰۰۰ شبیه‌سازی نتیجه بازی ایران و بلژیک را پیش‌بینی کرده که در آن شانس برد تیم ملی ۱۵.۱ درصد است. در این پیش‌بینی شانس برد بلژیک ۶۶ درصد و تساوی ۱۸.۹ درصد است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SorkhTimes/133982" target="_blank">📅 01:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133981">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">⚡️
چه زجه ای میزنن ایجنت های اوسمار، بستون نبود هرچی نیم فصل خوردید؟!
🧐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/133981" target="_blank">📅 00:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133980">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
|
#فوری
⁉️
🏅
به گزارش رسانه «سرخ تایمز» تاکنون قراردادی بین باشگاه پرسپولیس و دراگان اسکوچیچ امضاء نشده؛اما مذاکرات بین دو طرف در حال انجامه و اینکه آیا اسکوچیچ فصل آینده سرمربی پرسپولیس خواهد بود یا نه نهایتا روز دوشنبه مشخص میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/133980" target="_blank">📅 00:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133979">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⚡️
علیرضا نورمحمدی حماسه سازی کرده
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/133979" target="_blank">📅 00:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133978">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b80ddf04f1.webm?token=fXd1Jp157oNBnlk_aGAkxORXCMO0A1TQUwOIQzzde4Yn5ZiAumHnTcpZ25amlg-czbGO3I5-wEgz3_AweQXu4CWS_TXsEZGKJgH1CBrLUkXm7WLxQav4kZVMVAfNoUufZyvwW2u8cikZqRvA-ox1vuBMP1g1MSjWRGV3pciRefrcgNNTTfRpV3VSC2WjLYgrr_-VjHlhQ9ZGqBCEubon7knLp-NvTCxfx8ihjoM4LMIS-G_21my4GBoShKsRHJOvRuP8GziHdZ_F0TAhRd7mze5t90rKgmgmyX9khyLTCayHzvdUvcO7TslYrm0PYFrmR-JIGjicwW0m2Kq1wJ74DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b80ddf04f1.webm?token=fXd1Jp157oNBnlk_aGAkxORXCMO0A1TQUwOIQzzde4Yn5ZiAumHnTcpZ25amlg-czbGO3I5-wEgz3_AweQXu4CWS_TXsEZGKJgH1CBrLUkXm7WLxQav4kZVMVAfNoUufZyvwW2u8cikZqRvA-ox1vuBMP1g1MSjWRGV3pciRefrcgNNTTfRpV3VSC2WjLYgrr_-VjHlhQ9ZGqBCEubon7knLp-NvTCxfx8ihjoM4LMIS-G_21my4GBoShKsRHJOvRuP8GziHdZ_F0TAhRd7mze5t90rKgmgmyX9khyLTCayHzvdUvcO7TslYrm0PYFrmR-JIGjicwW0m2Kq1wJ74DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🆗
واکنش من به اخبار نقل و انتقالات این روز های باشگاه:
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/133978" target="_blank">📅 00:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133977">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🆗
واکنش من به اخبار نقل و انتقالات این روز های باشگاه:
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/133977" target="_blank">📅 00:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133976">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✅
بقایی سخنگوی وزارت خارجه
🔴
مردم مطمئن باشند که ما با آمریکا تعهدی را امضا نکردیم که‌اجرا نشود/از همین‌رو هیئت‌میناب 168 تیم مذاکره‌کننده‌ی ما به ریاست آقایان قالیباف و عراقچی و همتی راهی سوئیس برای ادامه مذاکره با آمریکا شد
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/133976" target="_blank">📅 00:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133975">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❗️
جرمی‌ دوکو ستاره تیم‌ ملی بلژیک دیدار مقابل ایران را از دست داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/133975" target="_blank">📅 00:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133974">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✅
بقایی سخنگوی وزارت خارجه
🔴
مردم مطمئن باشند که ما با آمریکا تعهدی را امضا نکردیم که‌اجرا نشود/از همین‌رو هیئت‌میناب 168 تیم مذاکره‌کننده‌ی ما به ریاست آقایان قالیباف و عراقچی و همتی راهی سوئیس برای ادامه مذاکره با آمریکا شد
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SorkhTimes/133974" target="_blank">📅 00:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133972">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oce-2yy6Feg10c9cHr83_YU-nwA3KNxguEUm7sAJ-tf0SsBMoRvsSI4nfoqjYou-OnVOGEBltXua0FVSxEVsw6Pnq5WSbmzbSJz6UXHkJssomHxWn94YIbi3LNxNzXifuIPozYHgJ8-FZkRSV0M1X6LpEcWAlBo1RNTVZWJblRBHCn2Qdg_DHpZI4Q3d7f91aW26LnYjOIZvsuXzd_fVuTu9YcjlLooUdTWn9XOp26pugpB0TG3g7fxzg_V99k1SGFqlxcRI0Lr312XecCov49w2vAHcBkO2_MGNODjCVHgX2fPY_fSXjhGMz3hqWsa4t9-m_XhCrRHJpxALlfTA1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/133972" target="_blank">📅 23:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133971">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✅
تارتار: گل گهر سه ماه و نیم است تمرین نکرده، 4 بازیکن تاثیر گذار تیم هم بازیکن آزاد هستند، چطور من برای مسابقه آماده شوم؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/133971" target="_blank">📅 23:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133970">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✅
تارتار: گل گهر سه ماه و نیم است تمرین نکرده، 4 بازیکن تاثیر گذار تیم هم بازیکن آزاد هستند، چطور من برای مسابقه آماده شوم؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/133970" target="_blank">📅 23:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133969">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
فوووووووری
🚨
مهدی گودرزی هافبک 22 ساله خیبر خرم آباد در لیست خرید تیم پرسپولیس قرار گرفته و مدیران باشگاه پرسپولیس قصد دارند این بازیکن را با پرداخت رضایت نامه جذب کنند/ فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/133969" target="_blank">📅 23:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133968">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
🔻
پرسپولیس با اسکوچیچ تموم کرد / قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/133968" target="_blank">📅 23:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133966">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فرشید حقیری :
⛔️
اسکوچیچ سرمربی پرسپولیس شد تمام
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/133966" target="_blank">📅 23:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133965">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
فوووووووری
🚨
مهدی گودرزی هافبک 22 ساله خیبر خرم آباد در لیست خرید تیم پرسپولیس قرار گرفته و مدیران باشگاه پرسپولیس قصد دارند این بازیکن را با پرداخت رضایت نامه جذب کنند/ فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/133965" target="_blank">📅 23:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133964">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
🚨
🚨
🚨
کسری طاهری، تیکدری و گودرزی خریدای پرسپولیسن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/133964" target="_blank">📅 23:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133963">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✅
هلند انتقام تونس رو از سوئد گرفت!
🇳🇱
5️⃣
➖
1️⃣
🇸🇪
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/133963" target="_blank">📅 22:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133962">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❗️
جرمی‌ دوکو ستاره تیم‌ ملی بلژیک دیدار مقابل ایران را از دست داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/133962" target="_blank">📅 22:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133961">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🟨
🟨
دوکو بخاطر زایمان همسرش اردو بلژیک رو ترک کرده و احتمالا بازی فردا شب مقابل تیم قلعه‌نویی رو از دست میده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/133961" target="_blank">📅 22:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133960">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anivyEZuLks4evTRenYA-AM7pzf75nHPUhst0UpyY-I_xEUA8iM08aLQghHwLGLkG2FO2RSm9eIfIrPEA1L-HJ95E3nCrjTcEBuvTOUbS1bI4Mmewxmp5UqHAxdB7eq5t765IIysX3Rwu14czNbyPEhlei1VU8TTgxz44moFMFx70JThiC0obXFAYJ5Jc_L62mpf06ShUFEEODY5S8Z0NNJHa_-bBK8CtMLRLTiHhcMVNPmwS9nkMXCNtobfkP1d4pa0fVhPJMa0IsUUOzbks1fuHPMoPlXHj-bigmsfcojbgnTv1lbZJhCD7rv6h5fDKJxn1SYM8pGUddZgPxnXAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
حضور مرتضی پورعلی گنجی با دست گچ گرفته در تمرین پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/133960" target="_blank">📅 22:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133959">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGB59ZbQDYcvYOPW_81mQ_j08SvrA8wo-b-xXY3lA-hYMAXjr4o3XgUPP8ZlNduYQbrE26VjUDEXgqpLyVfDlkTtdSEphJjLXvp-EbCWqsZgV0T93XuMjVf-IARTe1Bvl6K914Q1WkYtiPOwc-PplrIYcY6C36SC6VRDxoB5PAu89vkrpnBzL1qzsYz8aV6YB1-OR51LgsgId544jFzLSxoH4VIjsfjsdQNif1slJd7YIOclaFbigTzfrSdXM9nUHMV_jMazIPjrpsEmzYuKUlbomkRHQwzScS3u-VzQy2F-k5EZiAFH1dbAG8IAi5FWtZyOP7ruvo5qAABoFdkM-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
⚽️
گروه F جام‌جهانی ۲۰۲۶
[
آلمان
🇩🇪
🆚
🇨🇮
ساحل‌عاج
]
⏰
شنبه ساعت ۲۳:۳۰
🏟
استادیوم
بی‌ام‌و
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
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/133959" target="_blank">📅 22:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133958">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✅
بعد از جام جهانی قرارداد امیرحسین محمودی هم از لحاظ مدت و هم از مبلغ افزایش خواهد یافت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/133958" target="_blank">📅 21:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133957">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
شنیده می‌شود قرارداد دو ساله اسکوچیچ با پرسپولیس امضا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/133957" target="_blank">📅 20:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133956">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96b9555f3f.mp4?token=aPYpxbhixVf2_VnY1bsvOEYeT8iTPTTJY0db9MxVVZ-8GCZA06AprULKfZkR7IOYPoli9Aq-AaxsnkyJiBcmKvE16wGe4DMl0vDPIDrA_3d6KTsS8wPLX_9Gkv8jABqzibnrQ9rrdhEHKmIuwaFkHVhHY4eYAygcPbMpPs3tbyIkidApUAyro5Ty85cLjAF-qNCvllAriMavzVU1QfKqhqG9uya9zHcY5eqqPd4h7eYaaEjkOy6GmMY57DX5KeBkaV_x05_RCzs6tMw7vpL6-kZEFKuzF0A0wgqVBE_l_tNuqyD-9eHda_Qzoq0Z8kQ-faLwPaLTZGC56JLlsbJF_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96b9555f3f.mp4?token=aPYpxbhixVf2_VnY1bsvOEYeT8iTPTTJY0db9MxVVZ-8GCZA06AprULKfZkR7IOYPoli9Aq-AaxsnkyJiBcmKvE16wGe4DMl0vDPIDrA_3d6KTsS8wPLX_9Gkv8jABqzibnrQ9rrdhEHKmIuwaFkHVhHY4eYAygcPbMpPs3tbyIkidApUAyro5Ty85cLjAF-qNCvllAriMavzVU1QfKqhqG9uya9zHcY5eqqPd4h7eYaaEjkOy6GmMY57DX5KeBkaV_x05_RCzs6tMw7vpL6-kZEFKuzF0A0wgqVBE_l_tNuqyD-9eHda_Qzoq0Z8kQ-faLwPaLTZGC56JLlsbJF_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
دکتر عزیزی دست به کار شد
🔴
خداداد : میخوایم حسین نژاد رو بیاریم ایران!
پ.ن مبلغ فسخ و شنیدن شاخ درآوردن
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/133956" target="_blank">📅 20:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133955">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
مخالفت آمریکا با سفر ایران ۲ روز قبل بازی با بلژیک
🔴
🔴
در شرایطی که کادر فنی تیم ملی برنامه آماده‌سازی خود برای مسابقات را به فیفا اعلام کرده بود، محدودیت‌های اعمال‌شده از سوی برگزارکنندگان، روند اجرای این برنامه را با مشکلاتی مواجه کرده است. قرار بود تیم…</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/133955" target="_blank">📅 19:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133954">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
⚠️
⚠️
تنگه هرمز مجدد درش تخته شد
🔥
قرارگاه خاتم الانبیا:‌ تنگه هرمز به دلیل نقض مکرر اتش بس توسط اسرائیل تو جنوب لبنان و کشتار بی رحمانه‌ی مردم بسته شد
🚨
اگر عهدشکنی‌های آمریکا ادامه پیدا کنه پاسخ سنگین‌تری میدیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/133954" target="_blank">📅 19:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133953">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فرشید حقیری :
⛔️
اسکوچیچ سرمربی پرسپولیس شد تمام
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/133953" target="_blank">📅 19:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133952">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❗️
پاکستان: مذاکرات فنی ایران و آمریکا فردا در سوئیس برگزار میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/133952" target="_blank">📅 18:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133951">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‼️
فووووووووووووری
🚨
قرارداد اسکوچیچ دوساله خواهد بود
‼️
سه دستیار نیز به همراه اسکوچیچ به تهران خواهند آمد. همچنین گفته میشود مربی دروازه‌بان‌های اسپانیایی پرسپولیس در کادرفنی اسکوچیچ باقی خواهد ماند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/133951" target="_blank">📅 18:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133950">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
پیمان حدادی برای بستن قرارداد به ترکیه رفته و اگر اتفاق خاصی نیفتد، تا ۲۴ ساعت آینده اسکوچیچ رسماً معرفی می‌شود.
🔸
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/133950" target="_blank">📅 18:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133949">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇵🇰
🇵🇰
🇵🇰
#فووووری شریف، نخست‌وزیر پاکستان:
🔸
خوشحالم که اعلام کنم توافق صلحی بین ایالات متحده آمریکا و جمهوری اسلامی ایران حاصل شد. جنگ در تمام جبهه ها پایان یافت. مراسم رسمی امضا روز جمعه، ۱۹ ژوئن، در سوئیس برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/133949" target="_blank">📅 18:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133948">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">💢
💢
#فوری؛ ادعای #فرهیختگان:
▪
پیمان حدادی برای عقد قرارداد نهایی با اسکوچیچ به ترکیه رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/133948" target="_blank">📅 18:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133947">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
🚨
❌
#فووووووووری از فرشید حقیری: حدادی صبح برای بستن قرارداد با اسکوچیچ به ترکیه رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/133947" target="_blank">📅 18:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133946">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i3jn2AJlUT5b-4sEVAeW35nm2pzOnSrqHFx7NTlQdOkaF5FycIiKOpwgYXNgeFGeLyoyZaxVhVdC5CHA14jycVvOoXBTryEG15B-rwX2xw54FwD9AW36JgQaKmE-wOnS3OtRtu0IIuvFzGkk5Jq_hyxj2rFVtYifDyCvXpYQxXWho1L5Vc5DB9h8MAStKB448-F8uAg6Ag9Tq43KOJWZ5zW0vS8we9NQQhDpxXDrucTkEFqhyikGDFv_60agHE3oo3BvRAoJe9CrZAbWER8XK9DmItveLIPMoixxHx6MGoiFhjSqvhnBPVo40xueNXstjf734teiqC8dRFKIsst8pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
عجب بازی‌های آسونی دارن تیما آسیایی تو این هفته
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/133946" target="_blank">📅 17:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133945">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✅
قرمز آنلاین مدعی است دو تیم خواهان سروش رفیعی شده اند اما او دلش با پرسپولیس است اما به حدی از برخی واکنش ها و رویکردها ناراحت است که ترجیح داده سکوت کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/133945" target="_blank">📅 17:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133944">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❗️
❗️
فرشید حقیری: اسکوچیچ‌ ترکیه ست و به‌ زودی با امضا قرارداد میاد پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/133944" target="_blank">📅 16:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133943">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✅
سروش اگه پیشنهادی نداشته باشه خداحافظی میکنه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/133943" target="_blank">📅 16:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133942">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
⚠️
⚠️
تنگه هرمز مجدد درش تخته شد
🔥
قرارگاه خاتم الانبیا:‌ تنگه هرمز به دلیل نقض مکرر اتش بس توسط اسرائیل تو جنوب لبنان و کشتار بی رحمانه‌ی مردم بسته شد
🚨
اگر عهدشکنی‌های آمریکا ادامه پیدا کنه پاسخ سنگین‌تری میدیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/133942" target="_blank">📅 16:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133941">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
متن کامل پیام رهبر انقلاب اسلامی خطاب به ملت ایران درباره تفاهم‌نامه رئیس‌جمهوران ایران و امریکا :
🔸
بنده علی الاصول نظر دیگری داشتم ولی از باب تعهدی رئیس جمهور محترم به عنوان رئیس شورای عالی امنیت ملی به حقوق ملت ایران و محور مقاومت جلو اجازه آن را صادر…</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/133941" target="_blank">📅 15:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133940">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❗️
تیبو کورتوا:
✅
ایرانی‌ها یک مدافع راست به نام رامین رضاییان دارند که در حملات بسیار فعال است و ارسال‌های دقیقی دارد. باید مراقب او باشیم، او می‌تواند خطرناک باشد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/133940" target="_blank">📅 15:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133939">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇧🇪
تیبو کورتوا دروازه‌بان بلژیک: در بازی فرداشب آماده گلباران ایران هستیم چون برای صدرنشینی و صعود باید برنده شویم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/133939" target="_blank">📅 15:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133938">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">⚡️
⚡️
⚡️
گئورگی گولسیانی در لیست مازاد باشگاه سپاهان قرار گرفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/133938" target="_blank">📅 14:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133937">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1K2fUzBovWylGxoViliyZiD7YeNdmX7PRV-UAW7hBmFTOPEdXPkqtBFBgGod-6RTNLtjppdYqcH4hEvo8RvRKAbkZIawFPEuoO18qJaeT9BXzoqxHrHfU3cPs8DTpp6bc8R5DILiTjJeK7YTyjULHJWYYBcmktr3EI04qWGj43uG5iwFWVecS6scL6ZK5B6BKZd-h14lb5jIJAyNIRD_A6PqSYUfIgPfqraqyBaf9yEDUIsH-9jpz4w_LA75Yy86i2NEu2c-do41VtC-8oQuweukk91OIIchdeduzRW9nRhrS6tuJ_HBbBqYDsX1-aWkoK3XPYaFqJ4BgbExRzVqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
روزبه چشمی، سوگولی گروهبان قلعه‌نوعی که رفاقتی رفت جام‌جهانی بازی بلژیک رو هم به دلیل مصدومیت از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/133937" target="_blank">📅 14:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133936">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❗️
تصمیم نهایی با بانک شهره و انتخاب اونا هم اسکوچیچه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/133936" target="_blank">📅 14:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133935">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❗️
برگزاری لیگ بیست‌وششم در اواخر مرداد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/133935" target="_blank">📅 14:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133934">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❗️
برگزاری لیگ بیست‌وششم در اواخر مرداد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/133934" target="_blank">📅 13:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133933">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8eRQbF4ATPCX-DW8CWTYvrg7utwKx5o9y-2udh5SVrGbaB3zR46BScodJyhM7tvv1OkB-6quM66ZxrznynHzECYoh9NGxfStsiBj7wxUjcpfk2T23jZS42IZ4rPJpfci1ij_Demx6s8NRYjClJoSNnDbduXP2_3AvRvJ4BIbfzw6TmWZvolppAQql0JskOc07nZqdN3Md4FTIAKCGRCDK6wWQWM8XKYRtK-7FCNniXwQ8YOS4iui13c7pOTBMDyoG08C0JiSzNZqHh8lwLZqnuwuKqOwgjd-1TeK4sq6s-F7xfhbLLxBIev_SDqDDPyMmfYr8rmThqyQElntkCQ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نقل و انتقالات تابستانی لیگ برتر فصل 1405-1406 از 31 خرداد آغاز می شود و تا روز 4 شهریور ادامه خواهد داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/133933" target="_blank">📅 13:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133932">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✅
از دیگر نکات، این است که پیش‌تر باید حتما یک بازیکن آسیایی در بین نفرات خارجی می‌بود (1+7) اما در مصوبه جدید الزامی به آسیایی بودن یک بازیکن وجود ندارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/133932" target="_blank">📅 13:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133931">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
این مصوبه البته یک استثنا دارد؛ اگر باشگاهی در فصل گذشته بیش از چهار بازیکن خارجی در اختیار داشته و این بازیکنان برای فصل آینده خود قرار دارند، استفاده از آنها بلامانع خواهد بود. در غیر اینصورت اگر قرارداد بازیکن خارجی تمام شده باشد، برای تمدید قرارداد تابع…</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/133931" target="_blank">📅 13:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133930">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BiowML8DDRlPS-uB5_JzvHEmsDM8HpLzN3KMgJoqEktD65fmPH5Af4NJ8WhFf2lNKm_gXTTKgHm6MC5hX4LzEqrs3YGVMfuY2z7GMDhPWVrWcEYU0Dv7Wkjig0RkfTPc7g5bLkNtxE3UJbdA1YjFANrmugqdFLwoeK8GqTxHfdYXG_WrQBdNyRNmKMk4g18UXr2RRb_KPaIdi7vHlouWZc6rRAnae7-Ub-szIkDMrG5L6b6nPSZ2mt3H-WDMJ_zTJv90x8TuS2lz_BruQ8rzzdbSi8sjnteVLH5X6qFF9Sgb1bzdc5aNoNPlmt1tuFkWe6UhSkck1SMT7pOH3QS9Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
⚽️
گروه F جام‌جهانی ۲۰۲۶
[
هلند
🇳🇱
🆚
🇸🇪
سوئد
]
⏰
شنبه ساعت ۲۰:۳
۰
🏟
استادیوم
ان‌آرجی
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
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/133930" target="_blank">📅 13:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133929">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❗️
یکی از مصوبات دیگر و مهم جلسه امروز هیئت رئیسه فدراسیون فوتبال مربوط به بازیکنان خارجی بود. طبق پیگیری خبرنگار تسنیم بر این اساس سهمیه بازیکنان خارجی برای باشگاه‌ها که در فصل گذشته 1+7 بود، به 4 بازیکن کاهش یافت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/133929" target="_blank">📅 13:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133928">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✅
✅
ورزش سه :  طبق تصمیم فدراسیون و سازمان لیگ، لیگ برتر فصل آینده با حضور 18 تیم برگزار می‌شود و از لیگ ناتمام امسال، هیچ تیمی سقوط نخواهد کرد و قهرمانی مشخص نخواهد شد .
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/133928" target="_blank">📅 13:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133927">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🖍
فارس طی خبری مدعی شد باشگاه پرسپولیس با ارسال نامه ای به الوحده خواهان به خدمت گیری مبین دهقان شد
🔴
این بازیکن از الشارجه نیز پیشنهاد دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/133927" target="_blank">📅 13:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133926">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❗️
جدایی اوسمار از پرسپولیس قطعی هست/مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/133926" target="_blank">📅 12:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133925">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❗️
فووووووووری از ورزش 3: اعلام رای استیناف کنسل شده و تورنمنت قطعا برگزار میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/133925" target="_blank">📅 12:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133924">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❗️
فووووووووری؛ تکلیف نیمکت پرسپولیس تا هفته آینده مشخص میشه. باشگاه از اوسمار تخفیف خواسته اونم موافقت کرده ولی میزان تخفیف رو اعلام نکرده/ فارس   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/133924" target="_blank">📅 11:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133923">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❗️
اوسمار : امروز من سرمربی پرسپولیس هستم تا روزی که باشگاه تصمیم بگیره و بخواد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/133923" target="_blank">📅 11:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133922">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❗️
فووووووووری از ورزش 3: اعلام رای استیناف کنسل شده و تورنمنت قطعا برگزار میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/133922" target="_blank">📅 11:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133921">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❌
از باشگاه پرسپولیس خبر میرسد که با توجه به حضور مرتضی پور علی گنجی و حسین کنعانی زادگان در دفاع و همچنین احتمال جذب یک یا دو بازیکن جوان دیگر اگر اتفاق خاصی رخ ندهد مسئولان باشگاه قصد دارند نام ابرقویی رو در لیست مازاد قرار دهند
❌
البته مبلغ بالای دو مدافع…</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/133921" target="_blank">📅 11:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133920">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❗️
فووووووووری از ورزش 3: اعلام رای استیناف کنسل شده و تورنمنت قطعا برگزار میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/133920" target="_blank">📅 10:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133919">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇧🇪
تیبو کورتوا دروازه‌بان بلژیک: در بازی فرداشب آماده گلباران ایران هستیم چون برای صدرنشینی و صعود باید برنده شویم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/133919" target="_blank">📅 10:39 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133918">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🎥
خبر میثاقی برای تصمیم درباره نماینده سوم آسیا: تورنمنت سه جانبه بین گل گهر، چادرملو و پرسپولیس برگزار می شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/133918" target="_blank">📅 10:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133917">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❗️
🇱🇷
#رسمی؛ آمریکا با برتری مقابل استرالیا به دومین تیم حاضر در مرحله حذفی جام جهانی ۲۰۲۶ تبدیل شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/133917" target="_blank">📅 08:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133916">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔸
🔸
🔸
🔸
ایران ورزشی طی یه خبری مدعی که شد مهدی ترابی و مهدی هاشم نژاد در استانه پیوستن به پرسپولیس قرار دارن
☝️
☝️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/133916" target="_blank">📅 08:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133915">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❌
کسری طاهری اعلام کرد با پرسپولیس به توافق نهایی رسیده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/133915" target="_blank">📅 08:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133914">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtcM60tf4Kf0sNjB5lnqOMpJTy-RZhovHcNCQENuxv7Y2YWKTSQ3lAr_Z7jETiL-IEAfWzVi9R064onRLpIvLHGFkDGsd18jXiyxH99N45uOZMgdWGsCjMDN6vMJKkHq4sKSsRX1Ve1rxhGdGSr2bfNlOLREYxXRQp82xXEb9zTSo02RgppCf-X5vbxteisazdqiVxhkm1wz3iHa8AzKQu90CMgubdYlHZi3HHPRwyYhN9O_jvyU4NvO9Ffefj3Rn4g873lGAB_qtmShQjnChy0bsIphR1Uru6_6yilNnn4srDLa-T5Oy5JlUCNcfbyWWtCMH93jCYG7XP--Chdscw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
⚽️
گروه C جام‌جهانی ۲۰۲۶
[
برزیل
🇧🇷
🆚
🇭🇹
هائیتی
]
⏰
بامداد شنبه ساعت ۰۴:۰۰
🏟
استادیوم
لینکُلن فایننشیال فیلد
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
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/133914" target="_blank">📅 01:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133913">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/740f6c6148.mp4?token=V2ff05DC-y1LcexrAT5tBdGXaPauTenAb3d0i48zP1kiGTrlcpP0HaS0ev-1jg7kY7xUjhaEItzIDaK7Kzl4RSkgZMvjjMkv_Rr7z5c-YNofTuXnDxLG4jNQBRB_KjmHK8qMpKPG_YfQZ9SoDmxu225m-G6A8FeTbQdR1Vpq62bsVsya9ZgR9Ar36GDaFpA7N4uZL66MS8QG-pPGgp97y2FAtalyY0gUDOFdmkRUjUt4CgJPo1GwTTenTv4E30mPzN6XDU6WEahsnEs9rHK2Fp9UG-hu3VX3qdsc29zRp4QyX2ATD3z7y5s1jFUEENUAwZ_sIk5zw8u8eLRNjmnP8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/740f6c6148.mp4?token=V2ff05DC-y1LcexrAT5tBdGXaPauTenAb3d0i48zP1kiGTrlcpP0HaS0ev-1jg7kY7xUjhaEItzIDaK7Kzl4RSkgZMvjjMkv_Rr7z5c-YNofTuXnDxLG4jNQBRB_KjmHK8qMpKPG_YfQZ9SoDmxu225m-G6A8FeTbQdR1Vpq62bsVsya9ZgR9Ar36GDaFpA7N4uZL66MS8QG-pPGgp97y2FAtalyY0gUDOFdmkRUjUt4CgJPo1GwTTenTv4E30mPzN6XDU6WEahsnEs9rHK2Fp9UG-hu3VX3qdsc29zRp4QyX2ATD3z7y5s1jFUEENUAwZ_sIk5zw8u8eLRNjmnP8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
تا 37-38 بازی می‌کنم؛
پورعلی‌گنجی: در ایران فقط پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/133913" target="_blank">📅 01:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133912">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
رونالدینهو: مسی، فرانسه را نابود خواهد کرد
▫️
کوچکترین شکی ندارم. مسی فرانسه را نابود خواهد کرد. نتیجه بازی به نفع آرژانتینی‌ها خواهد بود، آن‌ها قهرمان جام جهانی خواهند شد. مسی فراتر از یک فوتبالیست است. من می‌خواهم بعد از فینال به سمت او بروم و به او تبریک…</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/133912" target="_blank">📅 01:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133911">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATQJk2cIQhRRzvAytCXBKEQnm3kkT9XgzFW6qRdun973S7Fk46CMktBIas_dVSbcXfxuWuQSPOt94nd6B-NmDUFR8LEPHPoDE-ZZeNCcmr7g0glieOrmzOxwWcbZg3Vp-Bd83oj4EJ2LUMNepgrPyXg-DPLt1Yzft0ttb0O0AHUDEArt8UGLAqRPcF5S2mY76-dPMaqiVfJf4f2LUuauyiymcdbpl30V4NMZmHqSqk-CPUMFtHadIyhyfUonRAUdec7gHKG0jo4xSFFHW1gTrvKlJyZ18w0dktOFjDmS689QlL9l84XwOEAq-C0dsdEJay2zgu-Mad6JNqeH1jE9kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه روز دهم مسابقات جام‌جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/133911" target="_blank">📅 01:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133910">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
🇲🇽
تیم‌ملی مکزیک به عنوان اولین تیم راهی مرحله یک شانزدهم نهایی جام‌جهانی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/133910" target="_blank">📅 01:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133909">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
فرشید حقیری : اینانلو همه تصمیمات رو داره تو باشگاه میگیره
🔺
پ.ن: باشگاهی که سگ صاحبشو نمیشناسه همینه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/133909" target="_blank">📅 23:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133908">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❗️
خیلی دلم برای تیم ملی تنگ شده؛
🔴
پورعلی‌گنجی: انتظار داشتم قلعه‌نویی فراموشم نکند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/133908" target="_blank">📅 23:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133907">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❗️
#فووری؛ ادعای #فرهیختگان: اگر اوسمار با پرسپولیس به توافق نرسه تراکتورسازی به صورت جدی میره سراغش و برای فصل بعد اوسمار رو جایگزین محمد ربیعی میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/133907" target="_blank">📅 23:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133906">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❗️
#مهم | لحظه امضای نسخه فارسی یادداشت تفاهم ایران و آمریکا توسط دونالد ترامپ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/133906" target="_blank">📅 23:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133905">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❗️
بازگشا: ما فعلا با اوسمار ادامه میدهیم و توافق برای فصل بعد با او به آینده موکول شده است یعنی با توافق دو طرف تمدید یا قطع همکاری خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/133905" target="_blank">📅 23:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133904">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73a7d67143.mp4?token=Gzx_BvAmDPrevbJxbsiSv_qbQfW44b3EvdhgD2QxQFCRiOdx_3LcdioXjTv2JBgJYdGhK0s26WjdSVQqcfhj736asa0i85e6pWylvEESeZ40cwSt5lqIJhrlAtp2Ax49ZMeskS9859V9j2iqKKBZRbJvI_XfqNP8v6lqBdZVBDtTp3l3zbrlkiC7_mlbtlGd3RO9sbiIpWVboEuF759Mg4GXYvroNpsDRLsgyacI7NmuA9rnaDgFsf1JIuCT5NCSs69GsYi623kHZdNFsrmmmuTNTYclrpumUzAoKArWm1OWMdnvnOt95aFkgqwNUQmqOLsytetiyz3Cf5UI3skhLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73a7d67143.mp4?token=Gzx_BvAmDPrevbJxbsiSv_qbQfW44b3EvdhgD2QxQFCRiOdx_3LcdioXjTv2JBgJYdGhK0s26WjdSVQqcfhj736asa0i85e6pWylvEESeZ40cwSt5lqIJhrlAtp2Ax49ZMeskS9859V9j2iqKKBZRbJvI_XfqNP8v6lqBdZVBDtTp3l3zbrlkiC7_mlbtlGd3RO9sbiIpWVboEuF759Mg4GXYvroNpsDRLsgyacI7NmuA9rnaDgFsf1JIuCT5NCSs69GsYi623kHZdNFsrmmmuTNTYclrpumUzAoKArWm1OWMdnvnOt95aFkgqwNUQmqOLsytetiyz3Cf5UI3skhLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
اوسمار: اگر بودجه کافی باشد شاید ۴۰ ۵۰ درصد پرسپولیس تغییر کند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/133904" target="_blank">📅 23:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133903">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
🔴
نظراوسمار در مور اینکه اگه باشگاه با یه سرمربی دیگه قرارداد بنده :
🔴
من یه مربی برزیلی هستم و تو برزیل ممکنه با ۳، ۴ باخت یه مربی عوض بشه
🔴
درسته ناراحت میشم چون دوست داشتم اینجا بمونم و کارم رو ادامه بدم اما شاید باشگاه فکر میکنه بودن یه مربی دیگه میتونه…</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/133903" target="_blank">📅 23:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133902">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
صحبت‌های علی بازگشا، سخنگوی باشگاه پرسپولیس درباره تورنمنت ۳ جانبه و آینده همکاری با اوسمار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/133902" target="_blank">📅 23:07 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133901">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcfd460d83.mp4?token=ZJ8TvwqBiQkBG-h_7KvJQX7Jz9i65yNy5SbST4onQFyE1mqzIBvvkUQ6ZkBjcqfVeIZ5EzjkzwcoZ7qSa_pDA5G2k8w2cUIkWaYt5wSQ0GOc8J81WbyApbwjF7ZaGhdGR5K0hkSgZVl5MQIogClmNrZW2iRdGq_M4WGSp3Fq648V8qRay6xHBjGF6uPhqyej9zJHy07I1PijIxzAFcpKChKbldlACRjAmkPHMPft68vI850mw3LBpWfQwaSCb4-5URoWJlqoYzmJ4eREYHjx1RBHW-0bkcO6IZcnT5WQ1Rj9CTcY-bLF13_Yf-73KCra9hBROAI2RuzF5WXjnZLYgoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcfd460d83.mp4?token=ZJ8TvwqBiQkBG-h_7KvJQX7Jz9i65yNy5SbST4onQFyE1mqzIBvvkUQ6ZkBjcqfVeIZ5EzjkzwcoZ7qSa_pDA5G2k8w2cUIkWaYt5wSQ0GOc8J81WbyApbwjF7ZaGhdGR5K0hkSgZVl5MQIogClmNrZW2iRdGq_M4WGSp3Fq648V8qRay6xHBjGF6uPhqyej9zJHy07I1PijIxzAFcpKChKbldlACRjAmkPHMPft68vI850mw3LBpWfQwaSCb4-5URoWJlqoYzmJ4eREYHjx1RBHW-0bkcO6IZcnT5WQ1Rj9CTcY-bLF13_Yf-73KCra9hBROAI2RuzF5WXjnZLYgoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
مهدی تارتار سرمربی گل گهر سیرجان:
🔴
برای برگزاری تورنمنت سه جانبه اگر باشگاه و فدراسیون فوتبال تصمیم به برگزاری بگیرند ما هم تمکین می کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/133901" target="_blank">📅 23:07 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133900">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac325be43e.mp4?token=ELeqKj2Kz8TdX_n4y8QpKpuVW0zCyz419LcSv2a5zLXWrGcCN3ANbkAQ5JNyZzrr8jHOxf5MU31npZ7wbktSxLpnIEA2s5PRTk-7ik1v44qtPWM60NdQ-1QlS7b_v2Do-pzHkS06xezO0zm4QMh9GKKSBf4OVm0s40umN0DOz8jtkMRI7nts6lKxFINoFETL1CU1GPv2qXBH548UF5-D9c22h80ODF-TRxI1_rFqIQQwSm3yM8Vn2K94YvOCX48LkaiXMdD5trinjKE9NrKujnpiN3FkDj59PPELAxJKUm0DIsZxmheq67npDuoaLxJa95gTEarXUFYnrbGhL44_jYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac325be43e.mp4?token=ELeqKj2Kz8TdX_n4y8QpKpuVW0zCyz419LcSv2a5zLXWrGcCN3ANbkAQ5JNyZzrr8jHOxf5MU31npZ7wbktSxLpnIEA2s5PRTk-7ik1v44qtPWM60NdQ-1QlS7b_v2Do-pzHkS06xezO0zm4QMh9GKKSBf4OVm0s40umN0DOz8jtkMRI7nts6lKxFINoFETL1CU1GPv2qXBH548UF5-D9c22h80ODF-TRxI1_rFqIQQwSm3yM8Vn2K94YvOCX48LkaiXMdD5trinjKE9NrKujnpiN3FkDj59PPELAxJKUm0DIsZxmheq67npDuoaLxJa95gTEarXUFYnrbGhL44_jYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اخباری سرمربی چادرملو اردکان: ما از فردا تمرین می کنیم که پنجم با پرسپولیس بازی کنیم
🔴
چیزی به ما برای بازی با پرسپولیس ابلاغ نشده است اما مدیرعامل از ما خواسته است که از فردا تمرینات خودمان را شروع کنیم/ مجبور هستیم که رای را تمکین کنیم و بازی کنیم/ به بازیکنان گفته ایم از فردا تمرینات آغاز می شود تا پنجم تیر مقابل پرسپولیس بازی کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/133900" target="_blank">📅 23:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133899">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c26a7662b.mp4?token=otiin03dq2FiVYfNtHBlXoAZnaW49O1VbLSlOG1i87sTCImSm8a4ZsDPe3zOuqCN9Xe-SvDwar-bWrCwGVPbod8M5o_waoBx7iXQn5dMa1oivojvBANb01ke6kjKnsDcuX6gvTtoaQbiB5csUgtOF3ZP8PIuJ57omW7KwxnY3sRFluNJjnK4NKLrVoAmiq7b81n17HVMN7eoK4C0a2G8fD999KAU9mpLKWAcMzgyWBFaCYyWsnG6ft9GDQtFQZoMqVN8CbBSQJ4mtPKzNuTd6tHE10uvVhiOZVu5nFx4grounimlf7Hh92Q4dgBwakkE6KYD2EvqOlAqgjJZucCtKWPqMSs6c1wi4suWluNuFILw8yC6LZNXI6F6qWCUWq1S_KrNxZvy41LJl9emThE-vHxNLKnWr9_d_VesWD6V22U-eg636G3vOZekc080Q1KCw5-WQz2rGnfYlKpl0BGl32CxUP_tfyLJqtZkDLf5mOwp8_NxZhKrWCHK2mcRUxGM4BOSjuTPc5QewqT22VhDhfn_ksfhSgYOOKZ8emOkaaMCbU16lOOPnMc35n3opPW2R-nJSQUx5alyFCzLbne4X5uhDUx5jGKlq5yOaQH78XjsxjmwotLYfTL78MeT64KAi8MZTYF5ixRMsc0iOdgpQpLT6YGQ5WlYFwDmzEYgudc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c26a7662b.mp4?token=otiin03dq2FiVYfNtHBlXoAZnaW49O1VbLSlOG1i87sTCImSm8a4ZsDPe3zOuqCN9Xe-SvDwar-bWrCwGVPbod8M5o_waoBx7iXQn5dMa1oivojvBANb01ke6kjKnsDcuX6gvTtoaQbiB5csUgtOF3ZP8PIuJ57omW7KwxnY3sRFluNJjnK4NKLrVoAmiq7b81n17HVMN7eoK4C0a2G8fD999KAU9mpLKWAcMzgyWBFaCYyWsnG6ft9GDQtFQZoMqVN8CbBSQJ4mtPKzNuTd6tHE10uvVhiOZVu5nFx4grounimlf7Hh92Q4dgBwakkE6KYD2EvqOlAqgjJZucCtKWPqMSs6c1wi4suWluNuFILw8yC6LZNXI6F6qWCUWq1S_KrNxZvy41LJl9emThE-vHxNLKnWr9_d_VesWD6V22U-eg636G3vOZekc080Q1KCw5-WQz2rGnfYlKpl0BGl32CxUP_tfyLJqtZkDLf5mOwp8_NxZhKrWCHK2mcRUxGM4BOSjuTPc5QewqT22VhDhfn_ksfhSgYOOKZ8emOkaaMCbU16lOOPnMc35n3opPW2R-nJSQUx5alyFCzLbne4X5uhDUx5jGKlq5yOaQH78XjsxjmwotLYfTL78MeT64KAi8MZTYF5ixRMsc0iOdgpQpLT6YGQ5WlYFwDmzEYgudc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت‌های علی بازگشا، سخنگوی باشگاه پرسپولیس درباره تورنمنت ۳ جانبه و آینده همکاری با اوسمار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/133899" target="_blank">📅 23:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133898">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🎥
خبر میثاقی برای تصمیم درباره نماینده سوم آسیا: تورنمنت سه جانبه بین گل گهر، چادرملو و پرسپولیس برگزار می شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/133898" target="_blank">📅 22:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133897">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❗️
بابایی مدیرعامل چادرملو: پرسپولیس با گل‌گهر بازی کند، نه با ما
🔴
اگر رأی کمیته استیناف به سود ما صادر نشود، باید حکم دستور موقت بگیریم و پرونده را در دادگاه حکمیت ورزش (CAS) دنبال کنیم.
🔴
به این مدل تورنمنت‌ها اعتراض داریم، اما راه آسیایی شدن همین است…</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/133897" target="_blank">📅 22:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133896">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
این فهم و شعور رو میشه تو امثال آدم های عین اوسمار میشه پیدا کرد .بی ادعا و با درک بالا صحبت میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/133896" target="_blank">📅 22:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133895">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
این فهم و شعور رو میشه تو امثال آدم های عین اوسمار میشه پیدا کرد .بی ادعا و با درک بالا صحبت میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/133895" target="_blank">📅 22:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133894">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
🔴
نظراوسمار در مور اینکه اگه باشگاه با یه سرمربی دیگه قرارداد بنده :
🔴
من یه مربی برزیلی هستم و تو برزیل ممکنه با ۳، ۴ باخت یه مربی عوض بشه
🔴
درسته ناراحت میشم چون دوست داشتم اینجا بمونم و کارم رو ادامه بدم اما شاید باشگاه فکر میکنه بودن یه مربی دیگه میتونه…</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/133894" target="_blank">📅 22:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133893">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✅
✅
تایید شد
🚨
میثاقی: پرسپولیس 5 تیر به مصاف چادرملو خواهد رفت و برنده این بازی 9 تیر با گل گهر مسابقه خواهد داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/133893" target="_blank">📅 21:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133892">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✅
در صورت برگزاری مسابقه، این دو دیدار در تاریخ 5 و 9 تیر برگزار خواهد شد.و بدون تماشاگر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/133892" target="_blank">📅 21:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133891">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">#اختصاصی_سرخ_تایمز | #افشاگری
⚠️
🔴
به گزارش رسانه «سرخ تایمز» امروز پس از شایعات و هویاهو های روز های اخیر ایجنت اوسمار ویرا در اقدامی غیر قانونی نامه باشگاه پرسپولیس به اوسمار رو در اختیار خبرگزاری فرهیختگان قرار دادن که موجب بروز برخی شایعات بی اساس و نادرست…</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/133891" target="_blank">📅 21:55 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
