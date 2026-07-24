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
<img src="https://cdn4.telesco.pe/file/FHadioX0GrbajPg9EV7dJdGyH5-KIOqcUbiMhmHC9gRh-FTSQVeZpppE9G0ADWLYXehZKjpSzvcPxbKfmc3XtOCnSlFXsXfymYTJ9dE8Vw2B-x133CPALaBhHEZbuWXHUY4QMsAqDXPZ7EZrAgZMnmPotxeutskqHbQGtfORB7JQznGB9ny1NP2raqffJBLquzvqgFjt0WSN95jqPZm02TeGSQFvKv3vxPaPYHRoVxV26OT72x2qVakmigMh5tQHvbH2hLIvH_4-hGT2Cot9xAczd7v6_jJMi6tWyJ1jyvb-0dvXH8BNOo76MtUsNwEf4pj855Vg--OTEpVaqAn0gw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.34M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 03:26:29</div>
<hr>

<div class="tg-post" id="msg-675008">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
اکبر عبدی درگذشت
🔹
اکبر عبدی، بازیگر سینما و تلویزیون در سن ۶۶ سالگی درگذشت.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/akhbarefori/675008" target="_blank">📅 03:11 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675007">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: ترامپ از جنگ با ایران کلافه و خشمگین است
وال‌استریت ژورنال:
🔹
دونالد ترامپ با ورود جنگ ایران به پنجمین ماه خود، از طولانی شدن نبردی فرسایشی که می‌پنداشت ظرف چند هفته پایان می‌یابد، کلافه و خشمگین شده است.
🔹
ترامپ که پنج ماه پیش با اطمینان از «پیروزی سریع» سخن می‌گفت، اکنون در باتلاقی گرفتار شده که نه راه خروج روشنی دارد و نه افقی برای پایان.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/675007" target="_blank">📅 02:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675006">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a95efd45d9.mov?token=pl9hn9S-HjWChifo2Kx-oMrwwvHQHvDnTKV5mHBsKG4HeF4yqWENYB7qBjwAZq80aUspOrzTHHWI6ufpfQsDrdZMUNhWDOsTk2O43F83VVKPEKKraL5gri6Qv9GDW3W27_rzPU9eYKJmyVGHW2due2EbMzX_8_8HqTY7fGL3iLO8GmQlhS6EZyHzYv_uPwLuV22Dwmeqp4d_Iu5Y8p_h7JRq5gqCWw16SUMs3Ha-6hYHhilAL2t5o-ZH3x4UxJfF4TT2Gx7sD8GmjWSPwIARSBtXAVZeiA2ijZQVstctMgKV4eZ92zg9X-AobkMW35jXNHh0jarBek2xbtYF_F2tfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a95efd45d9.mov?token=pl9hn9S-HjWChifo2Kx-oMrwwvHQHvDnTKV5mHBsKG4HeF4yqWENYB7qBjwAZq80aUspOrzTHHWI6ufpfQsDrdZMUNhWDOsTk2O43F83VVKPEKKraL5gri6Qv9GDW3W27_rzPU9eYKJmyVGHW2due2EbMzX_8_8HqTY7fGL3iLO8GmQlhS6EZyHzYv_uPwLuV22Dwmeqp4d_Iu5Y8p_h7JRq5gqCWw16SUMs3Ha-6hYHhilAL2t5o-ZH3x4UxJfF4TT2Gx7sD8GmjWSPwIARSBtXAVZeiA2ijZQVstctMgKV4eZ92zg9X-AobkMW35jXNHh0jarBek2xbtYF_F2tfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عبور روان زائران اربعین حسینی از مرز شلمچه دقایقی قبل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/675006" target="_blank">📅 01:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675005">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
نامه‌ ایران به دبیرکل سازمان ملل و شورای امنیت:  هدف قراردادن عامدانه دو شناور ایرانی از سوی آمریکا جنایت جنگی است
🔹
«غلامحسین درزی» سفیر و معاون نمایندگی ایران در سازمان ملل در نامه‌ای به شورای امنیت، درباره حمله آمریکا به شناورهای «ناجی-۱۵» و «ناجی-۱۶» گفت که هدف قراردادن عمدی این دو شناور که در زمان حمله در هیچ گونه فعالیت نظامی مشارکت نداشتند، «نقض جدی و آشکار حقوق بین‌الملل بشردوستانه و مصداق جنایت جنگی است.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/675005" target="_blank">📅 01:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675004">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
حملۀ ارتش تروریست آمریکا به یک کشتی
🔹
ارتش تروریستی ایالات متحده اعلام کرد یک کشتی تجاری دیگر را که مکرراً برای شکستن محاصرهٔ بنادر ایران تلاش می‌کرد، زمین‌گیر و از کار انداخته است.
🔹
طبق اعلام سازمان تروریستی سنتکام این دومین شناور تجاری است که از زمان برقراری مجدد این محاصره متوقف می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/675004" target="_blank">📅 01:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675003">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d15c04c185.mp4?token=YI0hwVeTCHI4uX_4OM5zkNSxwUvySUgI5rB7KHfQle7ML7evPEI6lwamWbmeSfCqvecn2pBCHLBmktOikIeIzcgtblCYfQM5q0dAhlZiv1Vo625X4kbbEztvMQHhbmGX8ehvDTWtorIrLW3LGIIIIMGrjNuYqQ45oEPvWUS9OF_Muzd3UAdd7eO6y4WpRpQJ6JRQ0cOSv8HMPUJmNTH68e5oH7ZBntROhvWIbIWbCg795ZwBxrTSaLCutYBhoRF7xCTcwYx016fJtLn4FtYCljssYms3OpyjnLZH7JA9v1Fq3qxQ8KZxilrLvvst6PglOtj4WrIEWl5UblZ5790z9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d15c04c185.mp4?token=YI0hwVeTCHI4uX_4OM5zkNSxwUvySUgI5rB7KHfQle7ML7evPEI6lwamWbmeSfCqvecn2pBCHLBmktOikIeIzcgtblCYfQM5q0dAhlZiv1Vo625X4kbbEztvMQHhbmGX8ehvDTWtorIrLW3LGIIIIMGrjNuYqQ45oEPvWUS9OF_Muzd3UAdd7eO6y4WpRpQJ6JRQ0cOSv8HMPUJmNTH68e5oH7ZBntROhvWIbIWbCg795ZwBxrTSaLCutYBhoRF7xCTcwYx016fJtLn4FtYCljssYms3OpyjnLZH7JA9v1Fq3qxQ8KZxilrLvvst6PglOtj4WrIEWl5UblZ5790z9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع عربی: در پی اصابت مستقیم موشک به پایگاهی در بحرین، ستون‌های دود به آسمان برخاست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/675003" target="_blank">📅 01:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675002">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
منابع عربی: در پی اصابت مستقیم موشک به پایگاهی در بحرین، ستون‌های دود به آسمان برخاست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/675002" target="_blank">📅 01:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675001">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
المسیره: تاسیسات بندر الحدیده هدف تجاوز سعودی قرار گرفت
خبرنگار المسیره در الحدیده:
🔹
عربستان سعودی در تعدادی از حملات تجاوزکارانه خود، یکی از تأسیسات بندر الحدیده را هدف قرار داده است.
🔹
رژيم سعودی مدعی شد که مراکز نظامی انصارالله یمن در استان  الحدیده را هدف قرار داده اما بندر حدیده هدف قرار نگرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/675001" target="_blank">📅 01:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674999">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9ROAezXp5m2G8qAuZVi_Gsw5YjMgeYDcTKdgdqHEGjSOvVa1VfONFe2seW7WS7cn9gv-e4korA9sNjXYa_nofuJweFbCShZ2u2iSNfE44at6lVn-iuYQQCA4kw1hGJjwky56FCBcNs_Wahp1MObcBCRDkoYgxtjRXQfVV0VwRfKCAnNtZCzU0eULLG9takpyB8bHuyRIXkQ5M4n3i5jnBaCBzI3fewMtbN0Nq6tyEaj68ceqGv44cCZAlO9dAz07fVTX_Al6LKZTwNNfPFLfpaKhTNL56Zwu0flie_alY1PDeQ6mo_RMw_bgpHV0dmJPjpB-Lo9hq59rTpvYNinVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اثر جدید کمال شرف، کاریکاتوریست یمنی در کنایه به عربستان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/674999" target="_blank">📅 01:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674998">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBNVbBq3-hhbYBik2_PbWSRWabi-IlLrAxwScSRsoGi02tNmH8ACr2THR1suriT4LNjdUVigktLTMh-eV7YD6F4n8WvE22DURJ_ZAgpctmY_CrUCqfcpNwy6te1WjsEq6s1enonS2DpY_kMrr2JlZE9RvcaIgsHV5BNx7VqU-j3yBG2JOUto_EbEXP6bVU8aGqpwyN4I7F3pdf1wlxJH2KYOl9uVjp6hoYQiGbpDS9U5nGUzjJoLVwMRfYJStVpUqRqTV-nHR_gBKY5lFmEhXfKePkUp6m5XYMo6Pe0mnrQ_8Uv2aj_-Jlo8Ha7Aoqe2monsaUUlnkNWuR_sERcbjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تکذیب پیام منتسب به فرمانده نیروی هوافضای سپاه
🔹
در روزهای اخیر پیام هایی به نقل از سردار سید مجید موسوی، فرمانده نیروی هوافضای سپاه پاسداران انقلاب اسلامی در فضای مجازی انتشار می‌یابند که منابع و منتشر کنندگان این پیام‌ها فاقد اعتبار و جعلی می‌باشند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/674998" target="_blank">📅 01:11 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674996">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tD5IUOOClO4OsRI-AdVwOHjrXKaD0GbncaFA8BJiT6ZfgCLTklIw1DAX8bF5nNHEckLKO_3rNIE20eKa-lRhjII5zGFc5yMSCVykLb1qsJ1MLw1lQggYqb80hyTA0SdeoL_mQtE8zFTNrbJcGxdlxb418oHFIrODQKlvVPnLAe4iilu99QiKRmir8V_wBDNQAUlDftBOINIYmTa7zAq6LxSNzwbSEcIMJpOF0_cKvj99lZsJmSU6qQLwcXBsOtgUJeqrl8UPvqHDYlyfQPoceo5lQJ6ePR2jbKSbvRuX6AY-5nvD-2XMlbLw_P2qdJjybq9mQeCBKMdIFjKKrCLxAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بلند شدن دود از مقر ناوگان پنجم آمریکا در بحرین
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/674996" target="_blank">📅 01:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674995">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
عملیات شکارِ شیطان خونخوار و نتانیاهو کودک‌کش
🔹
انیمهٔ جدید از عملیات انتقام علیه وزیر جنگ آمریکا، نتانیاهو و ترامپ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/674995" target="_blank">📅 01:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674993">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e200a8d21.mp4?token=q_igR1YDCP2y6KyUD5WKYL6LA8iGoSQR9Wpmh9LioXveNl_0UzYt3QlzzK1j_dn44uoMT3PumZPMOgyvVDBZHRMKbyqa34r13z_KzwcStkC-eiGiY84C4DLsprQR7D3yq7Z0W1KXYtWJ0HjHthkyoBQMUJa8C1TP285Ko2RjIu4cNeBjwUF7w2ff1NvjSNY7FqU2zieO_Jfk9ApmckpvmnmZuyOfIfaRKQyq6NRXycF9LPRgy6FfeSPP3pZvmFaH9nwIV6JZAYraDR7wmGFsgFXRljVLsEk39s7yGfqwEli_S5KEyfz2e1dslAEe0xqFqG2XzV6Rho1mfe0cAa-OBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e200a8d21.mp4?token=q_igR1YDCP2y6KyUD5WKYL6LA8iGoSQR9Wpmh9LioXveNl_0UzYt3QlzzK1j_dn44uoMT3PumZPMOgyvVDBZHRMKbyqa34r13z_KzwcStkC-eiGiY84C4DLsprQR7D3yq7Z0W1KXYtWJ0HjHthkyoBQMUJa8C1TP285Ko2RjIu4cNeBjwUF7w2ff1NvjSNY7FqU2zieO_Jfk9ApmckpvmnmZuyOfIfaRKQyq6NRXycF9LPRgy6FfeSPP3pZvmFaH9nwIV6JZAYraDR7wmGFsgFXRljVLsEk39s7yGfqwEli_S5KEyfz2e1dslAEe0xqFqG2XzV6Rho1mfe0cAa-OBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سامانه پدافند هوایی بحرین در رهگیری موشک‌ها و پهپادهای ایرانی ناکام ماند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/674993" target="_blank">📅 01:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674992">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e7eda22c1.mp4?token=qrYrcf61BS44nyJcTMKjA6yfQ6dGF1GoKFKHWE1XHSsZ7A4JS7F83bG_tPBPOYXfgAO5mohF9T-Ti8byo552uVrDjw5NnBc92ZauOGonJrZw8FlLgxEilfTkWjch9zz0xTYRBH56d0lU_k8pAunJnGElVmCtqj-0HaFxsUOkUE_DnwK9D05Leom8l_0kL1ccujngALiRznmpuBj4QC366wAMPJXxiPzJPKIBhQrqIevKDLZL9SzCdpe8JsIatToXow6arGtqCY3Y4lryJFfHmiXBsrqtSJ6qR87vXtUWnrI4LvzqD10GgtO1xb88Q69i6wVr-01v0unm5ONXXZayWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e7eda22c1.mp4?token=qrYrcf61BS44nyJcTMKjA6yfQ6dGF1GoKFKHWE1XHSsZ7A4JS7F83bG_tPBPOYXfgAO5mohF9T-Ti8byo552uVrDjw5NnBc92ZauOGonJrZw8FlLgxEilfTkWjch9zz0xTYRBH56d0lU_k8pAunJnGElVmCtqj-0HaFxsUOkUE_DnwK9D05Leom8l_0kL1ccujngALiRznmpuBj4QC366wAMPJXxiPzJPKIBhQrqIevKDLZL9SzCdpe8JsIatToXow6arGtqCY3Y4lryJFfHmiXBsrqtSJ6qR87vXtUWnrI4LvzqD10GgtO1xb88Q69i6wVr-01v0unm5ONXXZayWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه انصارالله یمن خطاب به دشمن سعودی ویدیویی به نمایش گذاشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/674992" target="_blank">📅 01:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674980">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t03o8JrbEhQ3uryOFlmlI_RQLWI0rD-6PePEplDtIGo3NybLoQs8vQr5-FLVdmgbqNuRkZqKQvEEhyrJgOT4EWT8nlJgmnyppG8mSJWRlPgh3gwQCDwEtoMhPzP5n0IETJNNSbKMV8gweKTDXTFrV8LmItDGcuzzgl8Aoj375wisyQpXt5g36UtKYkH9yN1ePf8BVdFRa9JozYUb6Rpf2JIBRzwQOG7c3xmx3KvW5sm137d89f2JHEW3eJ5t8KlGv5KW8Um_6Cy4W4AZdO-lVMoefexBSEcqg6xN5tV63NNxXL9Bjnj9xGHa8z-Rfrl2EdvsneqXtVFe2HCJVQHlIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RXDrn1CttrsfpldFpcGAZbEaljulnwm6S5AoovXrcIedH2uAcdbIvYYfQSo3HZgmyfCubaDcBGdltYDJqjVrULzy_zynZ1_6MEWta1xfIC4AfhY8FPG4EeN5NBPJuOKsul3gTtYUKwz6DbxOvhda98SvIqnrqbOnJz6YWB1lc26e_qc81I_hEcQ5S1qNqsy27j-Hfx_tU1lfTy8KxYX4qVm9ZcUL6ELof5B9fs4d_sOjleR_t3Ey1AcNgaZB-VqayEHQSayBnFI1VUOHdzjrOFqowTF-pePVEOBgVoBHgGMc_Rjyv33sev2Dke-e_yGI1YSCY9muK2MeGBXuKCRcIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fjxU9o_DddLDiuIk5E8fgjBiUWcxkkjF6IOFLFdcAiVEdPNTl1FCiZ4hTeLgUrE7fvCGhB9l20eofdmRPGJBf_3V1u_cY6w1OjaSEoIiK4yg3SU3IKZBQB14gZBUJoWHSiZWqY11qic0UMs1trjqeny5HaCPFzQe493FWWo8I0pJm974WDPLW4vtsZ4m5mqP6bjvwHKknsQCBwc7SkmVTvGwt9_InVdGH-yNAMsATy-WWnlvHfOJhpmK4ful_bxstvvw3bllHriZn5SfDKe0qNx4Uc1WlVTwoDy3pXHnQ3AifOZAR5Pf9kUjqiKUHJ2sukQEwl1DJrULsQbcHw9WFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rTw2Bm7-8d1fFVuVzzdHeq4OWrtx5rnmE4UUwjweBelS3Hl3f8sufMZ7jP8WmwIzLbKLqSjVrDwGLUpRjdsgg1ixNv-YElIDbPc8JOpgNhCvBgUvbWdAohSZF5d8Lip1NPCpSg9cSeS-W-L4HW8hAkrfGrBZrquYUYD8hDkTvoHHx2TlXpEqX9BjUyk7hSJWtaiSqeXzM2EJMsYW0w3ilxBE3-VjVm9YhTvgtmnLjJAxZb-uRlv3-dnufpg8257YEw5DawFdGkJPfD5Rii-okwElPsxXNTZDVYCQpso9EeNmupALx1AWvQrgUAgGxX9K4sS4Rc3onYXo365bSb4mlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FEEx56NYmDGxHvxdmy1ru9JJXtieY7QQD5n-rDBFe_-kZNqy8rP6IyOnJBpClsKFsN2AwFYU1L2yGunj0YJXNk394Ipm5lOlLOedQjyARX9wUL0vzvS-bpq_aXaLOrFe3eCdDxd-7psIROA1P6C0rpfddM8YfE9zG6VpiS10C83OEpwj_WMNS9MNL1eu6jsbnM0cKQD4M7-AodiZr0c6wzsCZITqVWocYoMbOK5jOfOqvW_va3clGOzVGtbW1HIEHRivyBrbEy-wWA7Ze-AYOQldSJ2iOBlLn9phquPZHafMVfAWa9-eGQ3W3CtAHRFSVWa-n0l9LH2NyNEJ-LUiDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lONhsDHbCq_RtkYho00NVb7AMS3Y_oVC4yjjvjUaAbn0s2XeNMZPonHz6FQFsX_-X2hNr6TvYjRakXM0_UbgGZOtWHkWCmiBuacTW4z_xKHLoJZLH9MzToNK7EUTzdhrfYpPDtQ-I8ExZlUwfAPWSO1xU0jJXQC_ltFdUFjjAwEV4rA6X3aM_kx-NWqFbewXjU5RNtnYIOF-chXYBwNvWR-57SAWBjw0FX8vhVykeRZC04XnV7oS28rEmhlMMJ-bslqilYQ4EZvTtFdc4v1MhwCEPwDbm6kavMFb7-CN9vdl4CgNKbEiVN9SqK6s7wp9MYp3VUS1gZMGHAc0duCh_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M3UK59O4fwg_YRdf6Hns1RQeCtHo_lirsgkg6AorNnsgCkkpxTFtZitCwgIFj_qcStClEfXroW7j4W0nIXco0ILOi12GzcBUwi3wjHHcKhp012S4OKaODsWz8M4CqxIgYiJqX2-bRImKcCU0cNre8j7bCIWoZzIXTQXW3OyejXve5v9OGx1KPnmrMkitg7tYA6O1VP5pytb_5uzqbUlrAh1SRl5v841GJZFEyIc6nrl8GmU7CMeSUopp5HL-NOdK8jFXk_YslL8qrHSvwsCCk1xKrkJgCsPQQFcOIAMNxgLUbbPlpJjLsF-UaE9En53ZfTUbqvzFjv8UqQvNhvdIBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AtR-q3e_UPQG_zB7GL7yj3GqPbxbwtA5CJ0ZjlxR-O6JJIQHeTXC6f8n7byGhkX5Iu5DkjTks8ihagpa0ROUxXrchsjdJhMH3ucvAxZGtUS8hBPzU_zeoXeOvkzB1FAgBb1l3hsm51usQAMz4TyRA7XiLLYuK9QzemuuNGT_rYbDFaGoFUPu8n2i9Ue1DaUgwhTcY-XfoD1TgihLI32WiHIWR_5tLW8Mphm6mRxIBxwIEzsIcRiqAq00udSIUOXJ4uXKgs9fesuCANqKfIihc38PNn1dk4DOtKw-8zYcpMSISfs6Pwvzhq6OACCW-xvcwUfm57Y4yT1Lo4B2dvvmmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ep68DufjcHXdN0AoOH7QZncQVzPD2VhnSiymvtvmiJq3BxZpns5H6OgJeVMmy83xvJgWBzHvzgafyzxHRujnpIndmsugvqwob5q5jHNTNdhjhD63Aobzo04UySOscQbrTvce-2h_z5DREy6SUkBKdehzTOiR77AoFX5QOudkEMb4CYBNPPO_rghTbKFYWtDELnNYMMhKIqFdZOxC1a8rUCQnaUBw54EgZVKyY57dYKiCH-ZwCktk6IGFJb43nlHO8vf61ctl3RfzuhkDB-kMCj-dnxTRqAB5OOx3qNPcexXS58X9h91tDhHsGglNOgOiFfcNGuNeqsecvj3eFzPS2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nni0DTEUWAfgEmazToZgNLoFBs73aZ16z3Z9dPLVypciDYbFRbo5eGT6279kqziMkLSS6L6KF2KMhTYe-zMuDvhzJHVukF4JXbL9b_ohGsvixYI8t2Dj3u_wYee72ttSMcr8GldLg6XexZhp8oId9zHFxY2nkQGfRlRZqDnATlvYE88QZ2AjOT5i7pg-Uwxc2KyX_43MQTQMqnDpes-OCDcxOkjKKmsJZa7ZZpjsx6Tojz3sf7s36CBnQ70tmCaCllXiDHt2-Qi-fqlbC7C5Y_J8D2sLe-seep5zHCeJDnsXFzj9bIbCQHNToTi5S3bQi2-EKhZu90y6CoEE1jnTuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
لامرد؛ شهری که قربانی یک حمله شد اما روایتش جهانی نشد
🔹
پشت آمارها، انسان‌هایی هستند که زندگی‌شان برای همیشه تغییر کرد؛ کودکانی که دیگر به خانه برنگشتند و خانواده‌هایی که داغدار شدند. لامرد یکی از روایت‌های تلخ از آسیب دیدن غیرنظامیان در جنگ است.
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/674980" target="_blank">📅 00:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674978">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c1bf73fab.mp4?token=ezWZMHQI9PENIht5rkp85WDamQWiswymvUCPZroBkezpSBnGpg7QV3lrk0jRGuh5v3uXvmCeWPyPKPdjnFwmE2Guxi_Ma69Eq3f9BLl0_iSUSab74b2mvYcY5hwXcB08qSkY2wCy1ovPgzjoWY60HxRWR5v6HjHOWXHsdTclSgJZPAncUeYMc7tT3-yhK6J6TzilNQsmZoYt2qiBw4kLzUqYjW768rFhZt-Q8qh2qypuV-uTCLPXsWq9ltCYwRFSKcJERt90DYpW1TckVOWluuGZUXX94fG4GooUgawNSKbm1Suw4MoI-sOTszwm6X1a4S1CaNrYFmeOQ_H7EKqwMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c1bf73fab.mp4?token=ezWZMHQI9PENIht5rkp85WDamQWiswymvUCPZroBkezpSBnGpg7QV3lrk0jRGuh5v3uXvmCeWPyPKPdjnFwmE2Guxi_Ma69Eq3f9BLl0_iSUSab74b2mvYcY5hwXcB08qSkY2wCy1ovPgzjoWY60HxRWR5v6HjHOWXHsdTclSgJZPAncUeYMc7tT3-yhK6J6TzilNQsmZoYt2qiBw4kLzUqYjW768rFhZt-Q8qh2qypuV-uTCLPXsWq9ltCYwRFSKcJERt90DYpW1TckVOWluuGZUXX94fG4GooUgawNSKbm1Suw4MoI-sOTszwm6X1a4S1CaNrYFmeOQ_H7EKqwMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایلان ماسک: روزی می‌رسد که پول دیگر ارزشی ندارد!
🔹
با رشد هوش مصنوعی و ربات‌ها، زمانی می‌رسد که تولید کالا و خدمات از نیاز انسان‌ها بیشتر خواهد شد؛ در چنین شرایطی، به باور او نقش پول کم‌رنگ یا حتی بی‌معنا می‌شود، چون هدف اصلی پول یعنی دسترسی به غذا، مسکن، حمل‌ونقل و خدمات، توسط ماشین‌ها تأمین خواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/674978" target="_blank">📅 00:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674974">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3245f5ecd8.mp4?token=aXOUMNlZvPEtAoXLa_PDm0wPOADJQobGF89MPef28-nWJzSbOV748IAsOdMVNlhAS_MTzqKbJUc0pYKoj7EC242IdPXcVAcTe3x7R2x12nk9Dw2ntS3xrHmJmr3l1hEzPwtjMoGJ705ZIgUqQKr_SJ60sqaOtIMZ4Ez6C_0I9B61k45HqlVatGFOFPtrm34Rncaj3XfxEDUsOdAlSRM9RcLYMVKYLmp3pYjxt_aicWIo88ze0-tAuA83xEzDG2He8i3USGYBI5KxPlaTJG9-gfEfCSKO6XwrqWPzPqT6FsoiPoDLQDpZD928DXimpfWHY5HQNd5p9cl_y8TO2ccyng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3245f5ecd8.mp4?token=aXOUMNlZvPEtAoXLa_PDm0wPOADJQobGF89MPef28-nWJzSbOV748IAsOdMVNlhAS_MTzqKbJUc0pYKoj7EC242IdPXcVAcTe3x7R2x12nk9Dw2ntS3xrHmJmr3l1hEzPwtjMoGJ705ZIgUqQKr_SJ60sqaOtIMZ4Ez6C_0I9B61k45HqlVatGFOFPtrm34Rncaj3XfxEDUsOdAlSRM9RcLYMVKYLmp3pYjxt_aicWIo88ze0-tAuA83xEzDG2He8i3USGYBI5KxPlaTJG9-gfEfCSKO6XwrqWPzPqT6FsoiPoDLQDpZD928DXimpfWHY5HQNd5p9cl_y8TO2ccyng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای خوک زرد: ایران برای بازسازی خود به ۲۵ سال زمان نیاز دارد
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/674974" target="_blank">📅 00:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674973">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1da21f30e2.mp4?token=QRz3PZO70lkDfnnw7BkQ34-H8ZxePho_bjhugQOK9w-EJDFr7nP4Uh6OVedxFfhFGkzZdPdrxh7PPNDOLqSZlQCH1Z8w5VVi4FTBw9vqGhwfF9Z_hTDkYWLL84d_rsgx0nGbVqr_AfOBAQIwOlKAer4fpNLb2OataJlJOE63eNeCC9Dcirqul-I47ys-W70fVaNq0Und4rkFm4WK-yfiDgrpZNCBQUCeLK_yzGuvyRiTT9Ir-4FFr9gi5OfIdGxYnj7wZOfz2X9QXxWBaB1nvGIgU0OXuuk8GiOFgcr9LFB2J7Fo6aDlRUwzyxemc_wxnq-gFIoLxLwYyqpO1FKPZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1da21f30e2.mp4?token=QRz3PZO70lkDfnnw7BkQ34-H8ZxePho_bjhugQOK9w-EJDFr7nP4Uh6OVedxFfhFGkzZdPdrxh7PPNDOLqSZlQCH1Z8w5VVi4FTBw9vqGhwfF9Z_hTDkYWLL84d_rsgx0nGbVqr_AfOBAQIwOlKAer4fpNLb2OataJlJOE63eNeCC9Dcirqul-I47ys-W70fVaNq0Und4rkFm4WK-yfiDgrpZNCBQUCeLK_yzGuvyRiTT9Ir-4FFr9gi5OfIdGxYnj7wZOfz2X9QXxWBaB1nvGIgU0OXuuk8GiOFgcr9LFB2J7Fo6aDlRUwzyxemc_wxnq-gFIoLxLwYyqpO1FKPZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت کادر درمان هلال احمر از دق کردنِ کودک سه‌ساله‌ای که با چشمان خود شهادت مادر و برادرانش را در جنگ رمضان دیده بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/674973" target="_blank">📅 00:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674972">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c795d247e.mp4?token=bVBHXjQpLoZgxSEBsIO9U7qOnHEqxNm6qKs04C0gVMXDUo5nry3n_jkGgyDANsHVZrAkGII8gIr3ehprNINi94fKVLThjsJF5oZlgjX9WGOtXt47Xd1StVZwTOYNpJmWq2bd95-xMhFEIwjEL6_y2TGRAMmOB6ERmRnFhE4YoGAQDKHsvMjLTo0A-8956IvzrK3UTbhCGATmpH3YuT-UnnZE2q5vBwiHQKlKi65eocfJ48fQ6mnTH0-9j2DBZeMDrHCwMtuHxblgdYybQKGD04gnC6_LyENaF81mznjhEFFvkuUsC1g2ry-Wxd2btWAkDScSG7bT1e-R3U4NcgaK_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c795d247e.mp4?token=bVBHXjQpLoZgxSEBsIO9U7qOnHEqxNm6qKs04C0gVMXDUo5nry3n_jkGgyDANsHVZrAkGII8gIr3ehprNINi94fKVLThjsJF5oZlgjX9WGOtXt47Xd1StVZwTOYNpJmWq2bd95-xMhFEIwjEL6_y2TGRAMmOB6ERmRnFhE4YoGAQDKHsvMjLTo0A-8956IvzrK3UTbhCGATmpH3YuT-UnnZE2q5vBwiHQKlKi65eocfJ48fQ6mnTH0-9j2DBZeMDrHCwMtuHxblgdYybQKGD04gnC6_LyENaF81mznjhEFFvkuUsC1g2ry-Wxd2btWAkDScSG7bT1e-R3U4NcgaK_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اکبر عبدی درگذشت
🔹
اکبر عبدی، بازیگر سینما و تلویزیون در سن ۶۶ سالگی درگذشت.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/674972" target="_blank">📅 00:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674971">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
فشار آمریکا به کردستان عراق برای ورود به جنگ با ایران
🔹
رسانه‌ها از فشار واشنگتن بر مقام‌های اقلیم کردستان برای تقابل با ایران خبر داده‌اند.
🔹
بر اساس این گزارش، آمریکا تهدید کرده در صورت همکاری نکردن، وضعیت خودمختاری اقلیم را تغییر می‌دهد؛ همزمان برخی گروهک‌های تجزیه‌طلب خواستار حمایت تسلیحاتی شده‌اند./ فارس
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/674971" target="_blank">📅 00:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674969">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
اولین واکنش انصارالله به تجاوز سعودی به بندر الحدیده یمن  حزام الاسد، عضو جنبش  انصارالله در واکنش به تجاوزات عربستان به بندر الحدیده یمن تاکید کرد:
🔹
بندر در برابر بندر، فرودگاه در برابر فرودگاه، هر تشدید تنش با تشدید تنش بیشتر روبرو خواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/674969" target="_blank">📅 00:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674967">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1oGL_K4j_M9RDUopAJ1BJNbR0RiPtZQRAQ05g8MMtPuWA4_hsQlK65QzFVIJEWUCU2ZrNwSOK0q25jAYvOm8xBDPrxOadNtwasOYEc33F20FyWcOtWa1wURn23uWKmLoVOYQ7ZXD3RHErTHJWs0as_0zgxR2xxr7rWIBsBOzFfcZClKV6AYnoE0kX5qjfGx8XOeJis1kCDVrLO9r8UOcWJ6axGjH7m3ubq0ssOerg_YZ_qy_sAVyQV2FcDaExlY5RYVYAVYOWOQ_o2mijoGDFxIkgG6r2-fQ2Y3U9c7QN2j4Fqlbt0WjIp6z14VG4V07lE2WYxVMTdNc-cGNNV9SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولین واکنش انصارالله به تجاوز سعودی به بندر الحدیده یمن
حزام الاسد، عضو جنبش  انصارالله در واکنش به تجاوزات عربستان به بندر الحدیده یمن تاکید کرد:
🔹
بندر در برابر بندر، فرودگاه در برابر فرودگاه، هر تشدید تنش با تشدید تنش بیشتر روبرو خواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/674967" target="_blank">📅 00:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674965">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShbaacsekBTJSn7OgrCWfZO1wfOmyyz55_1txvhFw3HzWWm4uma0zMHT9bSKF_V9I18NAkGsLWEx_ITfLTMD927OuvrkKbshz3EjDId1eQjrABP9rD1IBhNXk6lAjAy4pVKDF3F9b-_d59NOGY1XCvCxUXmzb0vpNvSyX8xeiQU3ywc2GfMQ-Gs2XMp97tOT7oiDnKpY1mcIdUxqnrqTvyKecAXkWjBBdYdyyw1UYXL2v41JwNMc5bU1o7oFEHBoNbloX6zCI_6I-FBYyAzQJwMMVjdcU5nFPcLwLk_J8OYpbPJEMJL4V7vkIsUP7cEVy7UJm6YD3Q_Cr2LVtkoKJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛑
اثرگذاری در کمپین های سازمان ها  معمولا مهمترین عامل برای موفق بودن کمپین حساب میشود
ایا هر تبلیغاتی و  یا اطلاع رسانی ، تاثیر گذار خواهد بود ؟
استفاده هدفمند و هوشمندانه از ابزار هایی که در اختیار دارید و یا میتوانید استفاده کنید مهم ترین عامل اثر گذاری خواهد بود
مشاوره تخصصی و طراحی کمپین های تبلیغاتی و خبری با ما در ارتباط باشید
👇
@marketing_mn
برای رسید به اثر گذاری ، ما در کنارتون هستیم در اژانس دیجیتال کست:
https://t.me/+fZbPfI0dd-41ZWNk</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/674965" target="_blank">📅 00:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674964">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKV_BEI2CKY73ZEnU_kVQjrRiRgJn0XA06bMBTzbIqYQXwRH6VocbTldvRpjXiZE0YaNnOGjSfXkT8Xuq5rKokkgvd0dpoW5Jx-KAA3zgF5mHDhP4J1YTcahzlaOg2qdsfcmu_6xQNAEo0qy2LG_-xwEC7xzbPMasjZf-L0ykRtTr-6MM-0iVCqIahal8ROd1wvBKULpPG_d6JrVVI-780E1vZMehSloLxOnlTCQVRgO1P3QmP4OX8zr4frh_mMlckwxJItmRyQ3EtedyFyTLyW2AapwVlPEAIGf-658PU3_qYY4t60Qid4GYBq5QBcNj2onNKBPBlMbhGXyVXwLUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/674964" target="_blank">📅 00:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674962">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔹
داغ‌ترین خبرها را هر لحظه در وبسایت خبرفوری دنبال کنید
🔹
🔹
راز آخرین‌جلسه شمخانی فاش شد
👇
khabarfoori.com/fa/tiny/news-3232741
🔹
امروز کدام شهرهای ایران هدف حمله قرار گرفت؟ + جزئیات کامل
👇
khabarfoori.com/fa/tiny/news-3232597
🔹
جنجال بازیگر فیلم‌های مستهجن پس از فینال جام جهانی
👇
khabarfoori.com/fa/tiny/news-3232778
🔹
رایزنی‌های فشرده برای آتش‌بس ۱۰ روزه | ایران چراغ سبز نشان داد؟
👇
khabarfoori.com/fa/tiny/news-3232805
🔹
اختلاف پزشکیان و جبلی بالا گرفت | ماجرای توبیخ رییس صداوسیما چه بود؟
👇
khabarfoori.com/fa/tiny/news-3232771
🔹
برای اطلاع از تازه‌ترین خبرها، اپلیکیشن خبرفوری را نصب کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/674962" target="_blank">📅 23:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674960">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0tRzTHH_ZdTOnvqPcIz-UkzNUqaK82POG-uD9pbZu7xKKshUay-KOUTBiMavA42h5kWQY4ahzwhD3M95AIK4keojjq_Vkf2ONiMHdTfPZ9wx4xYUbiPhXq-4vsnMW7pWS5K4s7apxITgrDs0aodVrUDdvYEAjIlCl4Qn4nFMaWQAyISeEOuAHMyhB4nheS8PgvE40CPZ_JtlTZCoh321As2BkV9RT81iS9fDa1pT_DvqSoCOcVN2dp8gmFkbWYExsDMlvJnBE7Ipx1oab3ALjx7rX4N4Kt13vUf0f9EtPFGlhwA8SRnBC_mpr65uxveqhsaYrvuQgLC6qjA32-0cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایندیپندنت: کارشناسان هشدار می‌دهند که فشار اقتصادی واقعی ناشی از جنگ ایران در شرف وقوع است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/674960" target="_blank">📅 23:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674958">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20f63abf7f.mp4?token=WV3ANhLnbcZ9YOrsdnBCbifsEjKjVEn4ZD8ZaoJB4nnP0SIU1oRmw2Lk0Ivah3xJ0RJDmLIYJbrLO1xbjePYM3XrpSWJL0UtkAAKFJRWQubbx3um6xsaEs08qrw3UgNHfxzwwEYkzYpWjNpThn_giqVCx79foMiIzy44Y7a-A4O_ENuosJOdbpxUk8vxkcJPa6YmknLfXtxtaLGqar1e7OD84B_vUACLCwXz5EnhDGIpZ61Nl29QUzzNqglvXAJALMQzao6djwscPBkQ_tZCK5g-fMbrpY6idJb05QqTw9zqllqsKZx0fbaHA5V6DWccjSqeYxJM7Pu1jGBkc3Kb9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20f63abf7f.mp4?token=WV3ANhLnbcZ9YOrsdnBCbifsEjKjVEn4ZD8ZaoJB4nnP0SIU1oRmw2Lk0Ivah3xJ0RJDmLIYJbrLO1xbjePYM3XrpSWJL0UtkAAKFJRWQubbx3um6xsaEs08qrw3UgNHfxzwwEYkzYpWjNpThn_giqVCx79foMiIzy44Y7a-A4O_ENuosJOdbpxUk8vxkcJPa6YmknLfXtxtaLGqar1e7OD84B_vUACLCwXz5EnhDGIpZ61Nl29QUzzNqglvXAJALMQzao6djwscPBkQ_tZCK5g-fMbrpY6idJb05QqTw9zqllqsKZx0fbaHA5V6DWccjSqeYxJM7Pu1jGBkc3Kb9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هـــــــر جا کـه هســــتی</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/674958" target="_blank">📅 23:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674956">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03a642cea0.mp4?token=R9CSuqUUhOUdofK_jXO1RaA49F4o9Y9Ly8weUKg_Q15FZQoUpqK4Nxm73N3byfV6P8oO5N2DbQHnjiH-vfKzQGJ0cqOL4bElkEEDDT81my1dia8hlqUmIr4wk5JcbKHba37nBoOhGYmR4nnF5daQQrh37SJFmvGcijoWEgzm5RSqwpw6fW5LBhPfVm5_ESBR8mXFBMApO_ZZqOsXvLcZ66JEOHPV2I2SpduBqyV_jPpTFuBe3SM9RGcINoKzCg35SYRwmMSrOcCargjzzyNg-t3BRDNWhEWB-nnMic2K2UY-8oqIZ4fL79LAYsQ9kGZql9bEHTGZHeH5SauMKTzPIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03a642cea0.mp4?token=R9CSuqUUhOUdofK_jXO1RaA49F4o9Y9Ly8weUKg_Q15FZQoUpqK4Nxm73N3byfV6P8oO5N2DbQHnjiH-vfKzQGJ0cqOL4bElkEEDDT81my1dia8hlqUmIr4wk5JcbKHba37nBoOhGYmR4nnF5daQQrh37SJFmvGcijoWEgzm5RSqwpw6fW5LBhPfVm5_ESBR8mXFBMApO_ZZqOsXvLcZ66JEOHPV2I2SpduBqyV_jPpTFuBe3SM9RGcINoKzCg35SYRwmMSrOcCargjzzyNg-t3BRDNWhEWB-nnMic2K2UY-8oqIZ4fL79LAYsQ9kGZql9bEHTGZHeH5SauMKTzPIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش بینی تقابل ایران و آمریکا در روزهای آخر عمر آیت الله حائری شیرازی رحمة الله..</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/674956" target="_blank">📅 23:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674954">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URmsXRXN2cmFGO-5QX44q6BsjhjE-2XsDJyxVP_bqac_3IiZiyGWNFKCIAO9FaucQYn46lsfS-d37iOSqDd5vc-1fVLXQM_AqIGvcP_cKfdKwWSwdX0SU3U34G53dFRyca8Vk57PjgOkEugG2E_J7Wzr84ioEYLoQbVJ_tATs21ilNaJ7qEIYZ1-8TVcT1Xcrk82r8D727h3hsiPD1V6tZCieValrk9y5NhhdjqR63igKtMwpVrvmPZeR8Y3Hpuh6tNKA1iR0Lm0OTfsecu4YS9L42sBj_QNgomD82_Bog6TWFfFDWp96L_90UDwRu7EaxqVLPztNQQ2gG6_OEtxDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f4d128eee.mp4?token=h2Tv0N_jx3mDE-XFEvCPSBRLZF5cA5veSNKUiruCrqf8E9nK0DV4xNvhRhGISae2NzEfkuViPipb4xF4-iVGUFoVk2noiwEFPnRnnFoexAQNd_NSLmPHEqQLEtc8yhS88CjuYoVo_968ZxqQlpz3yea7hmVGn2DfWPlYD9syVJR84xAkeF-odOZhf0nI3SKcYAamO72okQyQUsMwD5SkNrqcRA6WccKfNTppE_uDh2-RIa6BaEzTAFSABF23z_l649NDimpRDSxcvXRTimE8oeP7A73l8Tyw7xVkdpj4DD-4pra36JJQdPvMeMu7-hrXy2XBY_bJQMFf2mtZU_IUtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f4d128eee.mp4?token=h2Tv0N_jx3mDE-XFEvCPSBRLZF5cA5veSNKUiruCrqf8E9nK0DV4xNvhRhGISae2NzEfkuViPipb4xF4-iVGUFoVk2noiwEFPnRnnFoexAQNd_NSLmPHEqQLEtc8yhS88CjuYoVo_968ZxqQlpz3yea7hmVGn2DfWPlYD9syVJR84xAkeF-odOZhf0nI3SKcYAamO72okQyQUsMwD5SkNrqcRA6WccKfNTppE_uDh2-RIa6BaEzTAFSABF23z_l649NDimpRDSxcvXRTimE8oeP7A73l8Tyw7xVkdpj4DD-4pra36JJQdPvMeMu7-hrXy2XBY_bJQMFf2mtZU_IUtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر منتشرشده از بندر حدیده در غرب یمن، زبانه کشیدن شعله‌های آتش را در این بندر پس از حمله عربستان نشان می‌دهد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/674954" target="_blank">📅 23:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674953">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSoMgPU6CStF_axzhbcmhiN80hRFMG4ctnSj9vqGaEj58mFYrIgM2T3MCMvVyJu1gQT4uJYiYuAJX4sw1Y3XMMc28Ql2vpDW4WVm_pF97cOrxaTjPQWyohBuHYaMpMGwhXpYQyImRZieaKb4rF6kxb_pZ67bUMQAx2zPEEvDrM5fmwEgRMpqPUvxN2lxsiY7kT4UO2HdlMHMhecB7KCmsQhWW9uj7_8SdSoE4sIstIgoGPjb6Sv0VPzeYEErEwdDRIoPbytrSb2tV5hBDvYniXgqJo-DBSlthLZE6dWsHDUhNeP4ffGNfMpw14vX1Q_Yo_mHW6YSoQWiBpeV0HcNoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خنده یتیم شد
🔹
هشتصدوهجدهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/674953" target="_blank">📅 23:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674952">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2oozt6LJvSXI0MearO5HKB_HzG4PT-fPStXxoKsvIDzfIXJWLX9yQ38mspy9qAlZENjPnT1INOtyJEkY1JTuQwTsBfESfuQvKwqyQi2rSkNfORorZtSK8Qv-XiB8wkjnzWuMG4o1yEiOwLP_KeqbVMrDCx05s7wjPekqAknh5jOssaBjlqWSqb-Yg7pc6AYFf4CqdfI3Sx4Tbzuz6mzDrjlIXOZCAI2XAhGvG3rLYsq-gJx8tSi0k9bj8Ow_60Fuo3iWk7rdXkDAZE3jChL4hGcrEMrjh4K5cPi8korbENgQZweyhImMmU5TCcIcqcvDGWMbRs7jagr262V8svCuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منابع عربی از حملۀ هوایی عربستان سعودی به بندر الحدیده یمن خبر می‌دهند/ فارس
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/674952" target="_blank">📅 23:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674950">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7460a8d557.mp4?token=AlCKGT_cteERrE52SrOhg8TEUK6B5wx4ortAGPiyNe2H9pyvGIZOl0tZEN6reS5IscL1nlm8V6HiSpv7s2agN3YNl82IcAN2EnFau2frquwbnG7EmgZTcDjhdc4-UkQkjVkvl01q1C2fTx1kB_WmSKE3jU3utIOsfFTogyI6O3kulc4m6uUB-F-J-kPbIlJEoT5SSlthJ2GKitovZeB_g2WhaeCScEruosFAhGUIoVSH6IAp9wvYRvnhw_s2ad2u8TkeVU0Jv-_eEBl_4TpC_x_1C9in94waDaIyN-ppsmZVqysiMuJLLseY_HkVMUjyiQn34FS6jNuyTOsljFoWrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7460a8d557.mp4?token=AlCKGT_cteERrE52SrOhg8TEUK6B5wx4ortAGPiyNe2H9pyvGIZOl0tZEN6reS5IscL1nlm8V6HiSpv7s2agN3YNl82IcAN2EnFau2frquwbnG7EmgZTcDjhdc4-UkQkjVkvl01q1C2fTx1kB_WmSKE3jU3utIOsfFTogyI6O3kulc4m6uUB-F-J-kPbIlJEoT5SSlthJ2GKitovZeB_g2WhaeCScEruosFAhGUIoVSH6IAp9wvYRvnhw_s2ad2u8TkeVU0Jv-_eEBl_4TpC_x_1C9in94waDaIyN-ppsmZVqysiMuJLLseY_HkVMUjyiQn34FS6jNuyTOsljFoWrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک زرد مدعی شد: ما در حال حاضر در حال مذاکره با ایران هستیم و ممکن است به نقطه‌ای نرسیم که حمله‌ای بزرگ ضروری باشد
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/674950" target="_blank">📅 23:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674948">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNfzxx8Eksfp3REUTJoADiAPYoRXTuTLRsw_sM8trfm9sMD9MJaAgl3emmlqeHHfJQ_MAiqcnfMStskF4pCYOYE8dHpPfu9aDxeqiidzNMRS2mPHkvH6afD0me8NcOJRbgk5C3uagv08gJn4EQ6cXEcSsJU6LlqqKWVyWxPBGkP83x9dBQ0lOniCzOcJjDeDmypfHbeLz1ohd9H4DoOxg64H6J_qPpxE986XyioOasiFHIBp6_431SE2s7AZiYD90h8yRgz2JBJutA6B4qVxsI4UlKZnOa-fwxeCxsO483YEcD4ykewdqK5G8NI7RfwwkMQ-oUjCnMgQ-mAgJCCyaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اکبر عبدی درگذشت
🔹
اکبر عبدی، بازیگر سینما و تلویزیون در سن ۶۶ سالگی درگذشت.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/674948" target="_blank">📅 23:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674947">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
منابع عربی از حملۀ هوایی عربستان سعودی به بندر الحدیده یمن خبر می‌دهند
/ فارس
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/674947" target="_blank">📅 23:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674946">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRhYXR1pM1Qbh-qJGG5MKe2A_gFOIikXlqdnyY2MNGqCPtJnqoI2E7q2gDyjWccRDEvkvaxOlV2SPZmOUcly4V_lNi_HcPONJVP3BNG1TdO3WWmCf_LxxnL3x3z6tSK4dsUK6hH5ZmAjKio2mgP22RykLokd3ap-oJTEigvE9h1nVZYaFnb8bKTzNgIo9mffsaIFWS1dqaUsMzQJUB5syo9Y8MXkc6Teh_2L1G_bN2LnLYhAFlegAG860x_85xXQheslUzXFyYfSeHPUMR_0GwZnJXkstrfweJ8LTYRlvAVl4WkI349s-tKhPJ3ThNAbUcrxpnnGGjP3lh_GbZFGfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نشریه تایم: پایگاه‌های نظامی آمریکا در نتیجه جنگ ایران بین ۴ تا ۹ میلیارد دلار خسارت دیده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/674946" target="_blank">📅 23:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674945">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
خوک زرد: هنوز درباره حمله به ایران تصمیم نهایی نگرفته‌ام؛ مذاکره در جریان است
🔹
شی و پوتین به من گفتند مشارکت نمی‌کنند و به آنها اعتماد دارم.
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/674945" target="_blank">📅 23:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674942">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b4507e042.mp4?token=EabzO5CrYp7T2sv10T9fqvMNWMTgQgIDTetvzOZprJkOSBf-T3C8dpnTPVjDN081U5S791_bl1PWUszl1HDNP8RuMKwJz0rkKJNQxIpwz1IGSJc3U8rECTgTu-uJ8VVaBJ3wJW-2cYsC_rXcJOnJHX9lThIjJfsd9XoJhI6nGIR-Km1kV_T56H4azYQOjWL6rUIRmqMNDfqHF4FdX09x0WLgOGQYtuaCh4S0D06YmlyhMsw4QOvoDJM-MjysrkjNRZORf7jNH_21WCSgPsyU08fEc9tS7153fRRHnhabD3pVUc4c17UHMX2GBol0J3ZBhgCPZBFigFPWjl-NAYd1JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b4507e042.mp4?token=EabzO5CrYp7T2sv10T9fqvMNWMTgQgIDTetvzOZprJkOSBf-T3C8dpnTPVjDN081U5S791_bl1PWUszl1HDNP8RuMKwJz0rkKJNQxIpwz1IGSJc3U8rECTgTu-uJ8VVaBJ3wJW-2cYsC_rXcJOnJHX9lThIjJfsd9XoJhI6nGIR-Km1kV_T56H4azYQOjWL6rUIRmqMNDfqHF4FdX09x0WLgOGQYtuaCh4S0D06YmlyhMsw4QOvoDJM-MjysrkjNRZORf7jNH_21WCSgPsyU08fEc9tS7153fRRHnhabD3pVUc4c17UHMX2GBol0J3ZBhgCPZBFigFPWjl-NAYd1JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طفره خوک زرد از پاسخ دادن به پرسش خبرنگار نیویورک تایمز درباره ایران
خبرنگار به ترامپ:
🔹
شما از بمباران نیروگاه‌های غیرنظامی و پل‌ها صحبت می‌کنید. بسیاری در جهان متمدن آن را جنایت جنگی محسوب می‌کنند. شما هم همین نظر را دارید؟
🔹
ترامپ: به آن سؤال پاسخ نمی‌دهم. شما از کدام رسانه هستید؟
🔹
خبرنگار پاسخ داد: نیویورک تایمز.
🔹
ترامپ: حدس زدم. نیویورک تایمز شکست‌خورده.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/674942" target="_blank">📅 23:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674941">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3427ceff0.mp4?token=ohtsKInPhrHhGXcQLwjd9vcgmky-vP3hl-2A0ySfbql9ScBNn7bn-LB5liCxtq9fmd5RtA5x98_w8GxrSHW67eB1gAsM3i2ricQgjyktr2EoEkRSYPPThFrfk1C-JpF9ogIdSkkaGlRnSr081YlQCF8jJUwk-siy1hfKy_QaodFLFw8j5hAwj5l3ZbK8pK58TJRU6T5SZV200TlYELHcmkaRlWgSUo9Ur8BIeoNLtGGdPNCyoLWnUerw8IhdPSkzNaqmuwhw_OuX06VK_ZSBzJeey4JaBGZh4xvT_Z5RphhSW0yRPLl4XOXZhY8Ix0VRS5GKbYf_8DD0VfoOYnyypg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3427ceff0.mp4?token=ohtsKInPhrHhGXcQLwjd9vcgmky-vP3hl-2A0ySfbql9ScBNn7bn-LB5liCxtq9fmd5RtA5x98_w8GxrSHW67eB1gAsM3i2ricQgjyktr2EoEkRSYPPThFrfk1C-JpF9ogIdSkkaGlRnSr081YlQCF8jJUwk-siy1hfKy_QaodFLFw8j5hAwj5l3ZbK8pK58TJRU6T5SZV200TlYELHcmkaRlWgSUo9Ur8BIeoNLtGGdPNCyoLWnUerw8IhdPSkzNaqmuwhw_OuX06VK_ZSBzJeey4JaBGZh4xvT_Z5RphhSW0yRPLl4XOXZhY8Ix0VRS5GKbYf_8DD0VfoOYnyypg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سی‌ان‌ان: کمتر از ۲۴ ساعت پس از امضای توافق همکاری هسته‌ای غیرنظامی میان آمریکا و عربستان سعودی، دونالد ترامپ،  عملاً این توافق را با اعلام این شرط به حالت تعلیق درآورد که تنها در صورتی پیش خواهد رفت که عربستان به پیمان ابراهیم بپیوندد و با اسرائیل روابط…</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/674941" target="_blank">📅 23:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674940">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghreR_N5pXJl9dmw_bN4YBKWnrwImIuOuJldAV3CXkL_m0Kwp5xce2O5IBlW-dsNxjzCKc7t3FPQvwo0B19_3pGzk81mzaUrlfim7I2Kl6wPzuBJhO6Z2vm8aqouI-Ykd5O7K6NP3XxkaYk_mRMFNqt9XIGE3fhhj39bDFQVWuKcEvBfqVOAxTgxgRIuMaZukxZUJCnUUCY75WzAmZGXzPhZ9xxhqOL2BXU867LKtJhL6g6KcgQp_csizUxDuRdmZRaOExxkFulZ0sc6uPCt7B5LSFp_dH22aS8KfuZ270OVtWNGN0ZjvSWw_6WbQErB8JyMAa8HX_9dwqqsX1rxgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برسد به دست زائران اربعین
🏴
🔹
امسال هم با بسته‌های ویژه رومینگ اربعین همراه شماییم؛ از بسته ۱ گیگی ۳۰۰ هزار تومانی تا بسته ۵ گیگابایتی ۱۴ روزه و بسته‌های ترکیبی شامل اینترنت، مکالمه و پیامک، تا در طول سفر با خیال راحت متصل بمانید.
🔹
همچنین می‌توانید در آخرین نسخه اپلیکیشن «همراه من» به خدمات جامع دیجیتال اربعین دسترسی داشته باشید؛ از خرید ارز سفر و استعلام گذرنامه گرفته تا مشاوره آنلاین پزشکی، چک‌لیست وسایل و راهنمای سفر.
📲
روش خرید بسته‌های رومینگ ویژه اربعین:
🔹
کد دستوری: ستاره ۱ ستاره ۴۰ مربع
🔹
اپلیکیشن همراه من
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/674940" target="_blank">📅 23:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674938">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0cd13bbff.mp4?token=SufpvLLdYU0WhyrwOXU1Cu6p0Ng5ZPUhZwUdpuC1gqSsfUAV7JC0FIvaeufUd7LL2RfqZPK333GGdKRqT3SUSG_XAyUJs5QWVXB2ONDbjRBgSizCfuvnH-a4cJODNdXeIVyLcPta7PUuU54vznHrnjHlIeSgFCGfI72UpMOsqTQ8yKAV0KeXa0sYN_AvoB3Z3WVdprNLrptnefNQVS4gXgGSP4RlPzuZa0ZhrTLI54iWXZEkImiBaW6wT1XT4z2mYjdzD8FipyIuFJVFhXL7ARnsB3jA8rF8SdNcsgAjrEeH1w-rD0wYrR1ikgZcT8j_pqQSyXLD4reO3kwVIQ1xZ4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0cd13bbff.mp4?token=SufpvLLdYU0WhyrwOXU1Cu6p0Ng5ZPUhZwUdpuC1gqSsfUAV7JC0FIvaeufUd7LL2RfqZPK333GGdKRqT3SUSG_XAyUJs5QWVXB2ONDbjRBgSizCfuvnH-a4cJODNdXeIVyLcPta7PUuU54vznHrnjHlIeSgFCGfI72UpMOsqTQ8yKAV0KeXa0sYN_AvoB3Z3WVdprNLrptnefNQVS4gXgGSP4RlPzuZa0ZhrTLI54iWXZEkImiBaW6wT1XT4z2mYjdzD8FipyIuFJVFhXL7ARnsB3jA8rF8SdNcsgAjrEeH1w-rD0wYrR1ikgZcT8j_pqQSyXLD4reO3kwVIQ1xZ4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حاج قاسم سلیمانی: اگر آمریکا جنگی علیه ما شروع کنه نه تنها تنگه هرمز ارث پدری ماست بلکه حتی ما در راستای دفاع از ملت و کشورمون به دریای سرخ و مدیترانه و آتلانتیک و... هم فکر کردیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/674938" target="_blank">📅 22:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674937">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
جهش تاریخی صندوق ذخیره فرهنگیان در ۲۰ ماه گذشته
🔹
تسنیم: حد فاصل آبان ۱۴۰۳ تا تیرماه ۱۴۰۵ اقدامات ویژه‌ای در مدیریت «علی صادقی» در صندوق ذخیره فرهنگیان رخ داد.
🔹
تشکیل و فعال‌سازی کمیته‌های تخصصی مانند کمیته سرمایه‌گذاری، کمیته ریسک، کمیته حسابرسی، کمیته انتصابات و جبران خدمات، کمیته عالی ارزش مالکانه، کمیته رفاه و منزلت فرهنگیان، کمیته مسئولیت اجتماعی، کمیته بحران و سلامت کار و راه‌اندازی یا توسعه سامانه‌هایی چون، سامانه جامع اعضا، سامانه برنامه و بودجه، سامانه ارزیابی عملکرد، سامانه قراردادها، سامانه دعاوی، سامانه املاک، سامانه حسابداری، سامانه معاملات.
🔹
بر اساس صورت‌های مالی منتهی به ۳۱ شهریور ۱۴۰۴ دارایی تلفیقی صندوق ذخیره فرهنگیان به ۱۴۴ هزار میلیارد تومان رسیده و درآمد تلفیقی به ۵۵,۴۶۰ میلیارد تومان رسیده است؛ پیش بینی می‌شود دارایی درآمد تلفیقی صندوق در صورت‌های مالی شهریور ۱۴۰۵، رشدی بیش از ۷۰٪ را تجربه کند.
🔹
سود ایجاد شده برای اعضا معادل ۱۹۵ درصد آورده گزارش شده که رکوردی بی نظیر در تاریخ صندوق است.
🔹
حدود ۶۰ درصد درآمد صندوق ذخیره، ارزی اعلام شده که با توجه به نوسانات ارز در کشور، کاملا به نفع فرهنگیان است. میزان تعیین تکلیف و پیشرفت پروژه‌های نیمه‌تمام در ۲۰ ماه گذشته خیره کننده بوده به عنوان مثال پروژه سبلان۲ (بزرگترین مجموعه متانول‌سازی کشور) ۵۰٪ در یکسال اخیر پیشرفت داشته است.
🔹
هتل جنت اصفهان در این مدت افتتاح شده، پروژه هتل قطب مجددا به راه افتاده، پروژه پل سد گلورد افتتاح گردید و همچنین نیروگاه ۱۰ مگاواتی نیز به اتمام رسید.
🔹
یکی از نقاط مثبت ۲۰ ماه گذشته، بازگشت ۱۵ هزار میلیارد تومان به صندوق ذخیره فرهنگیان بابت پیگیری پرونده‌های حقوقی بوده است که در سابقه صندوق و همچنین بنگاه‌های بزرگ کشور، بی‌نظیر است‌.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/674937" target="_blank">📅 22:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674933">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4498bf9a7a.mp4?token=mXfIunJPiYLkvSgtOW3N5mhfrsF7JdcUBrH9ktUFc42aDlx-AwwFOfjZgrZyw7fvm-EXlcsLQAM-iWu18_GahW1ikqBhn05tClUL2w9THvkLsL0rU6hdSGiKIown20EzjAmgeqKkEhNCfNgxymLeoi3jIrqxmMj7TzAVeID4Aqelh2b1cOMlD9pF4Nw9gBPDe8P8VLkqy7XhKr-v3NcmzUnUChnV9gI1Rlf_7rwKZHDSC-zRHgt74vR4gmZNde5vpN2q0AnCE6SePBBmZrZfxZoT2ACgzqdwBFNfYNskCwwK_Qp1BkOxPGKMzIhQXE7a88KB0dQIm68WmfMTTkMieQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4498bf9a7a.mp4?token=mXfIunJPiYLkvSgtOW3N5mhfrsF7JdcUBrH9ktUFc42aDlx-AwwFOfjZgrZyw7fvm-EXlcsLQAM-iWu18_GahW1ikqBhn05tClUL2w9THvkLsL0rU6hdSGiKIown20EzjAmgeqKkEhNCfNgxymLeoi3jIrqxmMj7TzAVeID4Aqelh2b1cOMlD9pF4Nw9gBPDe8P8VLkqy7XhKr-v3NcmzUnUChnV9gI1Rlf_7rwKZHDSC-zRHgt74vR4gmZNde5vpN2q0AnCE6SePBBmZrZfxZoT2ACgzqdwBFNfYNskCwwK_Qp1BkOxPGKMzIhQXE7a88KB0dQIm68WmfMTTkMieQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار عظیم در یک واحد صنعتی بزرگ در رتندون در انگلیس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/674933" target="_blank">📅 22:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674929">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S2SAUr_59v9VDoxUeOZ80g2i4nR8_fa-lxv1nvxWdKNmlRbW3aHXK1_4ANY51B6iWh5QsyCMnivOnCIB2sAw7y3xGFUdJtjvEkAXA6gP9UEYKEkv5t0ufzA9yWsgF7TJbgkuSeAUDw0uUvKtie2DfTmc-q53MP6eBy4a1wDHPztDsUbFqrQ1qF0-3fdzZcy3Sv0oZsAW5S8aghmQOeqazG6OsL3FRPBUYoGpOD_5NMv-vwj20wu6FZ6dTPnMiRkHcWR4fAjAPx4asdDZyA4mzgTLIvD21fs9SmTdMm3iE9qyRreOrvHAcQPwK5lCGPskYtaoxj6e6DM9HVXk1ampzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YZw7qgXkl3Occhh2hvnBsUGx8V1B0o3Th96wMsJo878a8CUqz3ZPvHrsG9ssjb3kjFeqiU5p7lA6gQnItIN_n_QxjLYbV03urnFoX9OZ2D3w9ExX8X3jmv1PT1kqwxjijUXWUJorksCs4kCTmCU-tFfc2wwsBQUZiFQWpdD1kqu6gXTfcNHmCjZywaZgiUbosfHgPwr849eLGCKEQezVisL6saxhx-7UUkJBKqrOhTPXL5poYwBM326OWwcl8Mr3gIC5eAdO6H1DMacjO2JV4zvGmu3YQI_-Jj59ebLjNPTT8Wx4A1JZ4WouKERXcnq8Uvo5VaaGTDkKAM9Y_Wa_Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NEcvTgCb6fY-GZ5Ab1lRnXjKXtR4bg19Hwn9Lp9bY6XC-rSbI7JhZR_3obfaCZuqMsFPzZQqjslCO_M2DVQEfNeAbxAyTLJZOCuiKYBTWLV1h5zdIj5eDovicIniVVwnj0blxYOHgSqJE-3z7-f-mMed_DpKcZySqrk6bw6Lm7vJULG4505agQNXmOXqDbHV1a7e8GAhxFs6tuE-QnFckWEZpPjHQaUMHqS1GqjntW7fKIdLX6GLnqGrmwpTvQyOgDH4_2OibNXS1P0JLfvji3B9dfhuupEHF1qOFQu20K8-mxqpf9f56Zib0EYmrQYNcsRFW2-N7nE16x5q9X1NdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اکبر عبدی درگذشت
🔹
اکبر عبدی، بازیگر سینما و تلویزیون در سن ۶۶ سالگی درگذشت.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/akhbarefori/674929" target="_blank">📅 22:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674928">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
صداوسیما: ارتش آمریکا با شلیک دو موشک به یک تانکر LPG در دریای عمان، آن را هدف قرار داده و دو نفر از خدمه کشته شده‌اند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/akhbarefori/674928" target="_blank">📅 22:13 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674926">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/370fbc2f00.mp4?token=AzpM6FSSTaPDpvPTk1PpByMcsrVETFwmRBVuyEL5FocINsIljcqUPNXS9YzV6JZ3JonBZuOqyxJrAkD8jUuf3WSYqB_2sJ6YCJflzCQjfitCVwmrKaDhCazzoa3qOtLXbHzFpp93LS32Cr6HpfkYzoS1HwuySbyg2SUHqh3zmvHiKKTKz2fyn-trIFZb6RUMTZljpYQRhKNNLKdrOABlFBiMo7NEmqptNHPxhpzjnZMg_is02QCi8attrH9p9dcw6AocBOQaf5cjnv-g6as95EJz03L1g2ajEujkQSBKAHGLCa3aQhH2ZP4M6B274KVUb7V2G3Fm20Ym0dqIpeB_CEiBBLIcCmGrD_s0zNKjdwEZcuj9c_ZmM7u34VJlX6N1zpD6dL_3RXXzLJFt5MgRWcYtg3MpTrTE1KOEIE74p5c4CfBzpjcmH_6Bide6Rt3GIRL2ErTBWL569OOvJSS9RrC_CQ2FigaF7pvEyrHDPzv4LTx47owvfsTxBWuhBFOz3fw4KAyOPoxdbMyh_K7q8_gmiQ8JvLTNnzOV2-6pdoSuamJmGiPJXPDS6Kns2l9Fx6bLMVfjP1Z8rETvQU74TNshpgEKAyV_l_ohvzbhdDWr2d48xmk7KV_DRzs18FTfc196ds3Nn9nJsJ7IuVwINarp68U08dL9Flmp2Y4nBR0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/370fbc2f00.mp4?token=AzpM6FSSTaPDpvPTk1PpByMcsrVETFwmRBVuyEL5FocINsIljcqUPNXS9YzV6JZ3JonBZuOqyxJrAkD8jUuf3WSYqB_2sJ6YCJflzCQjfitCVwmrKaDhCazzoa3qOtLXbHzFpp93LS32Cr6HpfkYzoS1HwuySbyg2SUHqh3zmvHiKKTKz2fyn-trIFZb6RUMTZljpYQRhKNNLKdrOABlFBiMo7NEmqptNHPxhpzjnZMg_is02QCi8attrH9p9dcw6AocBOQaf5cjnv-g6as95EJz03L1g2ajEujkQSBKAHGLCa3aQhH2ZP4M6B274KVUb7V2G3Fm20Ym0dqIpeB_CEiBBLIcCmGrD_s0zNKjdwEZcuj9c_ZmM7u34VJlX6N1zpD6dL_3RXXzLJFt5MgRWcYtg3MpTrTE1KOEIE74p5c4CfBzpjcmH_6Bide6Rt3GIRL2ErTBWL569OOvJSS9RrC_CQ2FigaF7pvEyrHDPzv4LTx47owvfsTxBWuhBFOz3fw4KAyOPoxdbMyh_K7q8_gmiQ8JvLTNnzOV2-6pdoSuamJmGiPJXPDS6Kns2l9Fx6bLMVfjP1Z8rETvQU74TNshpgEKAyV_l_ohvzbhdDWr2d48xmk7KV_DRzs18FTfc196ds3Nn9nJsJ7IuVwINarp68U08dL9Flmp2Y4nBR0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صلاح یکتا به دلیل دخالت در امور پزشکی بازداشت شد
🔹
صلاح یکتا با کلیپ‌های شکستن قولنج در ایران و امارات در اینستاگرام مشهور شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/akhbarefori/674926" target="_blank">📅 22:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674925">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34dd09164e.mp4?token=rjOVuQajLlNV2VkCLUlEYlDFLhC8cHgOerpeGHrdfV4_6odyY_bSev0-em5UV2R7hNMILWq5zsuarD8kA3oP_huNuWs48dXUF3bF0KV8XOdk5Zr-R2p0eTrcDPgC_RDbAf1xg1-jdYBw9Y0zcXghdq-2yx4_pHn7DpD4Invy5LOahYm8J24SzJUNN3G9hGUKdKyaPK7rlqMD-1uMSxyRQzmgoYr67WUQsRQtlTk8MUKI1nGJsXQ-S9pUqnlYPXw9BUzj6mYJtpouFOLR7ZaWI0kZRz7UcgmDQm9jZo7rCKkW_belubOzF7aJmxD_g0PLqaJGfXXInDtC4KAqJWdNZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34dd09164e.mp4?token=rjOVuQajLlNV2VkCLUlEYlDFLhC8cHgOerpeGHrdfV4_6odyY_bSev0-em5UV2R7hNMILWq5zsuarD8kA3oP_huNuWs48dXUF3bF0KV8XOdk5Zr-R2p0eTrcDPgC_RDbAf1xg1-jdYBw9Y0zcXghdq-2yx4_pHn7DpD4Invy5LOahYm8J24SzJUNN3G9hGUKdKyaPK7rlqMD-1uMSxyRQzmgoYr67WUQsRQtlTk8MUKI1nGJsXQ-S9pUqnlYPXw9BUzj6mYJtpouFOLR7ZaWI0kZRz7UcgmDQm9jZo7rCKkW_belubOzF7aJmxD_g0PLqaJGfXXInDtC4KAqJWdNZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش ده‌نمکی به درگذشت اکبر عبدی: خداحافظ رفیق
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/akhbarefori/674925" target="_blank">📅 21:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674923">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
المیادین: فشار آمریکا بر کردستان عراق برای ورود به جنگ با ایران
🔹
واشنگتن از رهبران کردستان عراق خواسته در جنگ علیه ایران وارد شوند و ایران هم به اربیل درباره پیامدهای هرگونه همراهی با این جنگ هشدار داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/akhbarefori/674923" target="_blank">📅 21:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674922">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYhW0opZnRm72uAKUWaXILAkQ2VccDaXpgDjl3xQ6qwpwCTN0UXMu5DpSWyuL3IRR_RyWVAh-fuV4j1zdjjIU95qvBYlhUBTW6oydEoo5dCrSZLxKWA38h6NGWNiPo8eatYv4B0Kjm5hPRu3C7MvwwRo_28MSKrurb9lDe2GR3aqFf_aM5PcEv6LA_fWdF8ohn0lcqvNzqYsSdA4Y1FvCshcXb1XZSmDJTFH3Dpl-GkoxO-mS9f9DIA31xEsVFLJ4inl1H0BMegNd1HjTpORugwiAdRiO9EWD5mOetcp25KzFZwtsusia-Ei3Lvh_NpBK8rWO-YC6x8Z9U2PRgzsYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اکبر عبدی درگذشت
🔹
اکبر عبدی، بازیگر سینما و تلویزیون در سن ۶۶ سالگی درگذشت.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/akhbarefori/674922" target="_blank">📅 21:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674920">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2c96e0588.mp4?token=uWrOYyoyExoAVf2gXE8pJImHtlTIku8kiqOItnBhGDDaS9e654pXvmy4iVCa4SqKG77nWQenlrHAP9RFr4PTwe4iO85KKEauekT3fpv3GZ-AQ44ocTHP4u1rbmHeo11TniRpHmdHGseNW-NDzEYilLy6EkeplP0ykw4EziuvivNT3ahaZzWgVsR192DoMKC3_rjLp7LIbGmbpOMpkQHskhzf1M_q0wQpyMeV0gISiKCzuXTIz-ABmQn9FfNlYES2AmwW0hSBG1q_ojueK8AevCTNK0K0zu5FE736IfgHLsIIm-lOw82MLbOw9CGxthzpY7C6D_OpPFN5eOulBxKRgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2c96e0588.mp4?token=uWrOYyoyExoAVf2gXE8pJImHtlTIku8kiqOItnBhGDDaS9e654pXvmy4iVCa4SqKG77nWQenlrHAP9RFr4PTwe4iO85KKEauekT3fpv3GZ-AQ44ocTHP4u1rbmHeo11TniRpHmdHGseNW-NDzEYilLy6EkeplP0ykw4EziuvivNT3ahaZzWgVsR192DoMKC3_rjLp7LIbGmbpOMpkQHskhzf1M_q0wQpyMeV0gISiKCzuXTIz-ABmQn9FfNlYES2AmwW0hSBG1q_ojueK8AevCTNK0K0zu5FE736IfgHLsIIm-lOw82MLbOw9CGxthzpY7C6D_OpPFN5eOulBxKRgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اکبر عبدی درگذشت
🔹
اکبر عبدی، بازیگر سینما و تلویزیون در سن ۶۶ سالگی درگذشت.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/akhbarefori/674920" target="_blank">📅 21:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674919">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82bdf2a764.mp4?token=quCySdjQfbrADX1-xUKU0N2ACGnVAvKbs4GfVNPjdoPf3wJ9lp-84_-DZ8EZgx7eYanWrpfEUVFB8Aiconu2NDvQuaicFKxhW2qbUA1YfUEQQNVKkatf1zTsHGYjrc-McQ-ouC0vUe1GzynuMLotFyI8IUK1fjEEo6ScuVZHIt-UJLqT2j2KMvFf24gP5vZY_tZO21oOr8Edll8quBfI4DbsTHIdMg_A-h0GvLLpiOBGghAj3lWC25gssVK0B_GTuA6jk9599pDhyux0LswzjmmHxgfYt2_OAt89F09uKd96fSLI5e3HdpAF9nxL4HRdt7p5l5_kxFCeZwVyrYVFaHPgSKSHhkUrTDT6fH02LsR78k68B9GQBzA2u8P5G6Pz5Yvwunx_xwh4m3C93fNsrVyHlbwAk-Hl2v19bT2KjNyDNbD1CjAvsuC8B8LBLJZRoteaMVtpzeGURppPI-5i5bnkKE7anCM9v9Qlnd1GVKZnwlLSzLJO74U56MxWzhdnFw_zsaKg0vGrewWGgDM2i00Wqj5NBvsz9hVbWuw9JReH_6x_TeQ7DTL6Y65pT38tX_w7clgS4Fqs5uMwpnCKmrgyR4-Qci_6zZ0byIipNCeoVKm6TvUS6ut_8FTvE-TDosN0CNxKd4jKODUg5OELSL9BWDOuYLwY_3QhBCwyEOU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82bdf2a764.mp4?token=quCySdjQfbrADX1-xUKU0N2ACGnVAvKbs4GfVNPjdoPf3wJ9lp-84_-DZ8EZgx7eYanWrpfEUVFB8Aiconu2NDvQuaicFKxhW2qbUA1YfUEQQNVKkatf1zTsHGYjrc-McQ-ouC0vUe1GzynuMLotFyI8IUK1fjEEo6ScuVZHIt-UJLqT2j2KMvFf24gP5vZY_tZO21oOr8Edll8quBfI4DbsTHIdMg_A-h0GvLLpiOBGghAj3lWC25gssVK0B_GTuA6jk9599pDhyux0LswzjmmHxgfYt2_OAt89F09uKd96fSLI5e3HdpAF9nxL4HRdt7p5l5_kxFCeZwVyrYVFaHPgSKSHhkUrTDT6fH02LsR78k68B9GQBzA2u8P5G6Pz5Yvwunx_xwh4m3C93fNsrVyHlbwAk-Hl2v19bT2KjNyDNbD1CjAvsuC8B8LBLJZRoteaMVtpzeGURppPI-5i5bnkKE7anCM9v9Qlnd1GVKZnwlLSzLJO74U56MxWzhdnFw_zsaKg0vGrewWGgDM2i00Wqj5NBvsz9hVbWuw9JReH_6x_TeQ7DTL6Y65pT38tX_w7clgS4Fqs5uMwpnCKmrgyR4-Qci_6zZ0byIipNCeoVKm6TvUS6ut_8FTvE-TDosN0CNxKd4jKODUg5OELSL9BWDOuYLwY_3QhBCwyEOU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رونمایی از نماد رواق دارالذکر در «محرم شهر»/ درد و دل های مردم با رهبر شهید انقلاب در حاشیه رویداد آیینی محرم شهر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/akhbarefori/674919" target="_blank">📅 21:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674918">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
محاصره دریایی یمن علیه عربستان؛ صنعا معادله «محاصره در برابر محاصره» را اجرایی کرد
🔹
نیروهای مسلح یمن با صدور بیانیه‌ای رسمی در پاسخ به محاصره ۱۲ ساله این کشور، از آغاز تحریم و محاصره کامل ناوبری دریایی علیه عربستان سعودی خبر دادند.
🔹
صنعا با تأکید بر آمادگی…</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/akhbarefori/674918" target="_blank">📅 21:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674916">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e693b50351.mp4?token=NdLNGcWTvW4iqHxmFZ9Gi2CV54-UFXh9zd7rNN8xGXWFS-GomelVsk7OzAVonBFxNZWDUpQOSvlUdZQ4hs60CReveb621gGH7jHJb-O2vimeVp5WcXb-PhKopDPQJRPJgJooXkFQv9zvCpnFgAzEVgy1hiBFW6uGX4YFQ57ll1kRqwiZYXlIbdWSGV0o38SYU1LwsIROQpZQW0JDqg_9C1lJrwlxNiK1vFst8ONSPN6cSAI_SOHny1lBr4RIF5ShRGZsjV0JCwQS4byvq7gxHxubYoGVHiekV3M461BA_DDA9GtHFVbRkSDRk3GYNnPEEyDW6cUA_uUPF7I6JvTrow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e693b50351.mp4?token=NdLNGcWTvW4iqHxmFZ9Gi2CV54-UFXh9zd7rNN8xGXWFS-GomelVsk7OzAVonBFxNZWDUpQOSvlUdZQ4hs60CReveb621gGH7jHJb-O2vimeVp5WcXb-PhKopDPQJRPJgJooXkFQv9zvCpnFgAzEVgy1hiBFW6uGX4YFQ57ll1kRqwiZYXlIbdWSGV0o38SYU1LwsIROQpZQW0JDqg_9C1lJrwlxNiK1vFst8ONSPN6cSAI_SOHny1lBr4RIF5ShRGZsjV0JCwQS4byvq7gxHxubYoGVHiekV3M461BA_DDA9GtHFVbRkSDRk3GYNnPEEyDW6cUA_uUPF7I6JvTrow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دردسر دهه هفتادی‌ها؛ نحوه باز کردن گوگل ۲۵ سال قبل!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/akhbarefori/674916" target="_blank">📅 21:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674915">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79fd05ea96.mp4?token=nRm9GZQhS_fO3F0oB_54YmLQGIdN6q9C2Hp91oAcS__hI5NiplY9j_UnJ3g3T-JSMc56PQK35REgOmdi4w_owoPRi6hbGKg_zwNZ04DM672_URnEIvqyTyFr5myW6dVXrBNuSAlcC1WkgDHJTog3_zautdXmWqGvyZiIhGoJSH-przBp3sxPylHZb7wRxCIxailvlTAZKYd-zdiaBKg1cj4JMmF38qrjCEKzb7VVsZA6Bn0cVBtkeHozWLxRTkIVHx76RSk8KvISEaNRgP9WakWdOdGJlgjLMiNeTHmqCI82qqviTjswCe5hKusMsYoatdb0PLbmqOvpxc7qfpfywA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79fd05ea96.mp4?token=nRm9GZQhS_fO3F0oB_54YmLQGIdN6q9C2Hp91oAcS__hI5NiplY9j_UnJ3g3T-JSMc56PQK35REgOmdi4w_owoPRi6hbGKg_zwNZ04DM672_URnEIvqyTyFr5myW6dVXrBNuSAlcC1WkgDHJTog3_zautdXmWqGvyZiIhGoJSH-przBp3sxPylHZb7wRxCIxailvlTAZKYd-zdiaBKg1cj4JMmF38qrjCEKzb7VVsZA6Bn0cVBtkeHozWLxRTkIVHx76RSk8KvISEaNRgP9WakWdOdGJlgjLMiNeTHmqCI82qqviTjswCe5hKusMsYoatdb0PLbmqOvpxc7qfpfywA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای احوالپرسی امام شهید از مرحوم اکبر عبدی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/akhbarefori/674915" target="_blank">📅 21:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674912">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1961e3844c.mp4?token=AqM17h_UU2V-CDoEdv2Tl7H3ctUAoSLz_dWRBWShR-ljCzkoWkupTCvmSb2s5XFnwzY9QEaoHbNAIXOJIs8UPWeYHFCz6_k1Bq5bGKc--VhtH6TTJtfee6_YiVJbSwLymZaq89oLPDflqDBDMPjBtLHeQBhvhNwxOkdkRzKiV98k553qL-Y3ZxUgcT907xhg1oqdU9hqRu7MvE-FmIrPMLn_lQlXkkzuU-HpBUs2iVXyAjetnIzkk91zbXb0uSWK_xfTdJANMxGhF-Zk5tkGDeIwp4oR2S7jm_HHpCmlARYNOYPd8Kz-_6EoOOhWmTOJIIHs9emmxZjxswF9LWc_lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1961e3844c.mp4?token=AqM17h_UU2V-CDoEdv2Tl7H3ctUAoSLz_dWRBWShR-ljCzkoWkupTCvmSb2s5XFnwzY9QEaoHbNAIXOJIs8UPWeYHFCz6_k1Bq5bGKc--VhtH6TTJtfee6_YiVJbSwLymZaq89oLPDflqDBDMPjBtLHeQBhvhNwxOkdkRzKiV98k553qL-Y3ZxUgcT907xhg1oqdU9hqRu7MvE-FmIrPMLn_lQlXkkzuU-HpBUs2iVXyAjetnIzkk91zbXb0uSWK_xfTdJANMxGhF-Zk5tkGDeIwp4oR2S7jm_HHpCmlARYNOYPd8Kz-_6EoOOhWmTOJIIHs9emmxZjxswF9LWc_lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظاتی از هنرآفرینی آقای هنرپـیشه!
🔹
اکبر عبدی بی‌شک لقب سلطان کمدی سینمای ایران را می‌گیرد و  در حدود ۴ دهه فعالیت در بازیگری، در بیش از ۸۰ فیلم سینمایی و در متنوع‌ترین ژانرها از فیلم‌های جنگی و تاریخی گرفته تا ملودرام و کمدی و هنر و تجربه و کودکان و نوجوان و همچنین متنوع‌ترین نقش‌ها هنرنمایی کرده بود، روحش شاد
@AkhbareFori</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/akhbarefori/674912" target="_blank">📅 21:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674910">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_sc5Qssq787o40p6UIKZ-nnOt22XDPQ9TGpteV_3UbIG4_Uk8ae-cmWhmOvoO1PxYU7yD_5-IvBnuyLgN16OaBK--WvIPUMtccsDwWRwCVUTEKhD_pjieQ6_hUKUNE7dQveLIZ5USrs4keMP8xOtA2Bd6yeRBY9GqJ2KVthMEobkowZAXy5kPx1bK_nKBNC4GL5PqfpaZSlqxrTXyU3Jjb4vuEyhW4W3oV2tOJ0CyLqUdmb8_L2evwP005pQHtSPBMjCjm3OG6NeGWT7gNhtSt19q5bRjgMQpeYnV2acMd7BqPpCl5YdBuDgUc1izLKYzaJYX4KFW480n3K_J0uKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اکبر عبدی درگذشت
🔹
اکبر عبدی، بازیگر سینما و تلویزیون در سن ۶۶ سالگی درگذشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/akhbarefori/674910" target="_blank">📅 20:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674909">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kpi3PAdezxlzcTl3baah45AtI3GqF5_jBnQkJGEXuU7a4Eo_bDLvO3YAdqdLDp-nLVMFCgKP8mwvnD5RlCo3ioy_-OlioEpspKIC_cTynJKFxxJpg1eVoNPxvnDR8H_jrt4HUlTa8O94cvNgvYR7KxQrh94K7MEpl05n6ZdTJkk8zMy1Bvn8zoT9wP1rvXhFZV01xzEQxvcNFE3IA-6_SXs7BSKcwcyByzfZUTLxnu8C5ygKHlsJONpRqH2IloH4wHJYvT2Zd35zpCX4bo5kNgX3hGwzNblPYUV0b8_QFbmM2xCukeQd0sbCvH1s2BAqOyNNP2MSg0QmexoQBHpyaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تخلیه کامل هواپیماهای نظامی آمریکا از پایگاه العدید قطر
🔹
تصاویر ماهواره‌ای و داده‌های منابع باز نشان می‌دهد آمریکا همه هواپیماهای نظامی خود را از پایگاه العدید خارج کرده؛ اقدامی که برخی آن را ناشی از نگرانی امنیتی و نشانه احتمال تشدید تنش‌ها در منطقه می‌دانند.…</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/akhbarefori/674909" target="_blank">📅 20:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674908">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgkqO6GXYcTDae_w5fXEtX16UmM6iYmkZNDe4HNI7TIZ5e2EiEpnqED2XCz07S7YtO3qXT_6ows8vjd8iEglH0g8kXe8fFCkdFEZYOHyePg2FOsP-vlr5vnEBUk32h5-HMbaY5z5Z3dJnhy67gaTQh-bvjTNRc6n5fFQXTVLlZlUc-XKqhap2dNMWym6c97PDe8lR3pr3OIkrgTEl_XbjrtFGKfBNViEQ1otJVaLll58B1bOKBIZ4BKKhvFYx7q1PDSJ1Laj1OqeTkAgjaxeFsvH_SUT6oHihyyo89iM-C0ePKtOx264oyi8C90pEn-3-dJvBf0QXJs9yVLWaN8MTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بلغارستان در جنگ ایران رسما به آمریکا پیوست  خبرگزاری دولتی BTA:
🔹
کمیته دفاع پارلمان بلغارستان به تصویب پیش‌نویسی رأی داد که به هواپیماهای سوخت‌رسان آمریکایی اجازه می‌دهد از پایگاه هوایی در خاک این کشور، از عملیات نظامی علیه ایران پشتیبانی کنند.
🔹
واشنگتن…</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/akhbarefori/674908" target="_blank">📅 20:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674907">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpQQd6CB0WxHVhxtgUKhFumyU3m7aQ25goFLvYpE7WQVTvP5daJ1_Ee8Q9WJSPZ_6mLccJW6cEaQR6F6UCUz6NBIcI-WugHnJ_N8bVOsjmuIroCuNpC7hTz22RuUvJzAQqj-JWnBwTZ9MCh4AW2FTcTzVXF0_TG8TAFuGyVeHwzIWTYOaSC97NsEsjQG38DnY_3721Vx-jXk7HmpPm0d-Tf7nDbPAGeDVFP-Lph3m3YbK74D5Hu4BXMddWMywIDy8471cBr7gZ9WAVG6MHuXl72-HnmCM3GxZkCKzI27cJtLjhThalgHIWiKjU6gzabcOdTRBXQHVFMb08lAGFkm1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ما ایران را شکست خواهیم داد!
🔹
کارتون: الا بیکر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/akhbarefori/674907" target="_blank">📅 20:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674906">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWbEKO94VA8LQrGUe3BUzFQ4pTjEEoEi3V2_TpMDny1qAg7rz9DYpQFPvOSYX7jOZRmEpFd3SDhZoi3koC-ofiOljKiCKyHjOPVbijTI0yr9d-tAuHcdJMQKFD5fQI9hI8lEGKAH2rIFHsyC4mc8cPl1ftZR8RkSe8PAlE04VJjA67FWwR3GShKumBy8WF6b4uRVutM7LgM9dhopd35BanZk5-s1Noq4w17CFgCriX3osT839DIUNzIicIdnwkfc1614qtXjCG7DaMS6vH_BRpQbj_a5fnfvviFA9VvABpmThdKELbCEpvU3hc0g8cjLdMnrO7DtD71ODtgajb-llg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیزده صفر شاید بهترین بهانه برای یک شروع ارزشمند باشد
💎
طلای اقتصادی با اجرت از ۳٪
🏦
خرید مرحله‌ای از ۵ میلیون تومان
🔄
تعویض طلای سالم با عیار ۷۵۰
👰
سرویس عروس از ۵ تا ۶۰ گرم
کانال رسمی ما :
https://t.me/haghgo_gold
ادمین :
@haghgogold
_
__
آدرس شعبه ۱: ستارخان بین فلکه اول و دوم صادقیه پاساژ زرناب طبقه همکف پلاک ۳۲
شعبه ۲: فلکه اول صادقیه زیما مال طبقه B1 واحد۴
برای اطلاع از موجودی تماس بگیرید :
09924100036  ---  09924100039</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/akhbarefori/674906" target="_blank">📅 20:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674905">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
روایت مردی که پس از تصادف شدید و ۲ ماه کما، تجربه‌ای متفاوت را بازگو می‌کند
🔹
00:10:00 عاداتی که در هنگام جدایی روح از جسم به همراه برده خواهد شد
🔹
00:21:00 رؤیت عذاب شدن چوپان دزد و حیله‌گر در برزخ
🔹
00:34:40 برقراری ارتباط بیمار در کما با پرستار
🔹
00:49:40 متوسل شدن همسرم به اهل‌ بیت در زیر باران شدید
🔹
00:53:20 شدت وابستگی به جسم، دوری از آن را سخت می‌کرد
🔹
01:00:20 نام‌گذاری فرزندم توسط حضرت ابالفضل
🔹
01:03:30 آب روان با طعم بی‌نظیر که با نظاره کردن رفع تشنگی می‌کند
🔹
01:08:45 خودزنی در برزخ، عذاب کتک زدن همسر در دنیا
🔹
قسمت یازدهم (به خواب شیرین)، فصل پنجم
🔹
#تجربه‌گر
: سید مجید غضنفری
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/akhbarefori/674905" target="_blank">📅 20:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674903">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
ادعای اکسیوس: آمریکا و انگلیس دنبال ائتلاف دریایی در هرمز
🔹
واشنگتن و لندن برای تشکیل ائتلاف حفاظت از کشتیرانی در تنگه هرمز برنامه‌ریزی می‌کنند و شرط بسیاری از کشورها، پایان درگیری‌ها در این منطقه است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/akhbarefori/674903" target="_blank">📅 20:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674902">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/189ca34d45.mp4?token=QWki0Lan3WfUeRkZF_ClTaKYeZHciG0lNvo4D3NCFuTw4YbnBpkPsVSsdqBLYQCvG5-7zfKunGfhezsjL8voCdJM0iS8EXKc_9GxniaX3OzoF-YX6BpH0nGhSFp145QbNRNTI6F-VHw-LKGu0f6GE8VTSOvmPvglWNlJDydocCDgndC3FD6XOBRe3Q2e5klHr1rWFm4LP8rrNwAKfujmD_v0CXKQS2GXO3Apx13lWV9oTU33TxCF-0YoePesYx7B_dyoLwG6-XIMDxZxNgf7-gbyFBpdetnguAuXhN2q76Tw1or7HPH1n0QHJzdkVFJKFY0na4cWUUITK4zqHH1YEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/189ca34d45.mp4?token=QWki0Lan3WfUeRkZF_ClTaKYeZHciG0lNvo4D3NCFuTw4YbnBpkPsVSsdqBLYQCvG5-7zfKunGfhezsjL8voCdJM0iS8EXKc_9GxniaX3OzoF-YX6BpH0nGhSFp145QbNRNTI6F-VHw-LKGu0f6GE8VTSOvmPvglWNlJDydocCDgndC3FD6XOBRe3Q2e5klHr1rWFm4LP8rrNwAKfujmD_v0CXKQS2GXO3Apx13lWV9oTU33TxCF-0YoePesYx7B_dyoLwG6-XIMDxZxNgf7-gbyFBpdetnguAuXhN2q76Tw1or7HPH1n0QHJzdkVFJKFY0na4cWUUITK4zqHH1YEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اطلاعیه شماره ۵۱: اقامتگاه نظامیان آمریکایی و چند جنگنده در اردن، سامانه پدافند هوایی پاتریوت، یک بالن جاسوسی و اقامتگاه تروریست‌های امریکایی در اربیل منهدم شدند  روابط عمومی سپاه پاسداران انقلاب اسلامی:
🔹
مردم عظیم الشان و فداکار ایران اسلامی؛ ایستادگی…</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/akhbarefori/674902" target="_blank">📅 20:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674901">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
ادعای روزنامه آمریکایی درباره مشارکت بحرین و کویت در حمله به ایران
وال‌استریت‌ژورنال:
🔹
بحرین و کویت در حملاتی محرمانه برخی اهداف نظامی داخل ایران را هدف قرار داده‌اند و امارات نیز پشتیبانی اطلاعاتی و دفاعی داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/akhbarefori/674901" target="_blank">📅 20:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674900">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qb1w_MpdObvkRycp90Qnq5ZeYLdV2PBBD4Vckxd7gK2lJjW2D0Op6waEwSLagmWaxSp6MBGeDvZOFOvmg4nSBePto54R4m__ut7MIAUPb7i79DjO7seBvjivOMTZnUwsvySmJFw1JzHaVs3A7dCS17wGLyzQ-sHwvogCLzFjLcl_-vXIbli88zRpy43OUUhP5iCuhqdAiPwjGHsHhTmMdgXgIBUTQlYDQck-xF8D8rOZrn9leOJ5y7PmSQ1UzmZ0Fjuo5Rt7VA0nXNmz_KL7wvIA7UZgzBcYa5fv03KgQmZuJsaKYRkDMN0NEcw-_apjSnvOYMNQOi-h_iVl5eP3ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/674900" target="_blank">📅 20:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674897">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
نرخ کرایه مسیرهای اربعین از مرزهای ایران تا عراق
🔹
مرز مهران تا نجف: سواری بین ۲۰ تا ۳۰ هزار دینار، ون ۱۵ تا ۱۸ هزار دینار و اتوبوس ۱۰ تا ۱۳ هزار دینار
🔹
مرز مهران تا کربلا: سواری ۲۵ تا ۳۰ هزار دینار، ون ۱۳ تا ۱۵ هزار دینار و اتوبوس ۸ تا ۱۲ هزار دینار
🔹
مرز شلمچه تا نجف: سواری ۲۵ تا ۳۰ هزار دینار، ون ۱۵ تا ۱۷ هزار دینار و اتوبوس ۱۰ تا ۱۳ هزار دینار
🔹
مرز شلمچه تا کربلا: سواری ۲۵ تا ۳۵ هزار دینار، ون ۲۲ تا ۲۵ هزار دینار و اتوبوس ۱۸ تا ۲۰ هزار دینار
🔹
مرز خسروی تا نجف: سواری ۲۵ تا ۳۰ هزار دینار، ون ۱۵ تا ۲۰ هزار دینار و اتوبوس ۱۲ تا ۱۶ هزار دینار
🔹
مرز خسروی تا کربلا: سواری ۲۲ تا ۲۸ هزار دینار، ون ۱۵ تا ۱۸ هزار دینار و اتوبوس ۱۰ تا ۱۵ هزار دینار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/akhbarefori/674897" target="_blank">📅 20:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674895">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRmmDGh6RknaoP5QjM9QlU0l0zNtaMI85-fENxc_HbMnJ_AcqEe01OSIQ58eMaW5XVmPWI-hZOcrdLnm7nHC6xwwsTLFVusilP21DHvdzqYODcCTcgzbYBOSBrBYLOYahN7kgoLNi8fRPWY7xtQai31LBob4XetqwICPIQLVGMSiBZ_ARoKAs4a8SfXPyXkeSdbzzMNvFXPzsn9Ysi5VZwM25gjXFCyUG5ICEU-vxDXa0y1TrRCr34-VmkKQRdJSuaAQx-UH780JHOTGeTxBPlMwhI9VBoavJInyr4OgiM_2k_Fh-RUj7F1RWXNXzzrJYMmhW3e-OmkHNLKRcwHmxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۲ غذای که در زمان نامناسب میخورید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/674895" target="_blank">📅 19:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674892">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IL5YOSItqZMPkV-lrLdOURb45ev9hLNzjPHHawUQz91Gympa_69kKT9WItxpAfQ5X7IOv64wTY0HtMh_Kar4vSgqpASXES36nuE8rLW9aunALotXcREjqKyLE3UIu4g6u1dsg4_OhIorR4Cw2IV6of4vPxyu4qdN94RY1ydSWJ-HbUvaM4rMDnTMlyIaQi00I4Nv7taNJPfEleyjuBKimEyNdd3mM2Ds29Es16hOrEU-ecVGC2n2qwLYT_SZoQsxOu9PWlyWhUjtU0ZuXC7eTgzNn9XkuuZpmcjpdX--8fz1U3-yKrlXZK2U0bY3Kt8JQAR17av0cUU6Q9CHgQCfJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرمانده قرارگاه مرکزی خاتم الانبیاء: در ازای شهادت رساندن هر یک از شهروندان ایران یک نیروی آمریکایی به درک واصل خواهد شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/akhbarefori/674892" target="_blank">📅 19:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674889">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ah4FGg71k9LPyDyFsMxNKtck9cmP23xu_vlzax6wruN7Ga4WoNpF5XVQ4JmkcQ-bqPKJQGv5aFgEHt5u_lPUHDA7cLJqAplrWoAZYnLgILNAT2KeA4oIFZhSuWx6wqt0FriFTBq5oCKAN_-xXOiYRR0d6WKXxjT9EeEtviALB9tc53eg8T3gKjDhv3D8DGIGRTGRJBN4ihwlDhBv00gpMTiJQ3E6kyKaXYGLjFVx-Smrx0fqbMwHUE48j1u46k0i3b_7a_OpXmIdbxMD0s5N1diUydMLFE9TV58Ktn-uhg0Tp1K85l4Gl9ohfvFzrFpaUGYW7fNgug-R_rWMPDkqCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاداش قهرمانان؛ فیفا مبالغ جوایز جام جهانی ۲۰۲۶ را اعلام کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/akhbarefori/674889" target="_blank">📅 19:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674888">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb1ec3628c.mp4?token=RSiApTmg4M9GwtLvnrzYbcfG4orhRjQ0xXgSQ4BAMIDEyg77ceGajwGud44vVQCjMi98apBUc-c_4alwyhYGWF4YyHWUaIUBaOxkAU9sps0YZlIdsbGeDdbRKHAGzSaJtBlwzqg3fRZR9f9ogXplbHXy13zfD5YHYQ2PnRNKGwI30I7JQG38BooS8vyUQrCiDRFQ1ht_haXG-DTa47PjwnpKxqJ6tII2odXcP1qs-3M1ltsLO2Z7rhLWTHrWE_XmUtE9CTN0E8j3rvSAb4MUzto--nC6BSZWJYE6EtnzzbhkedFmzRcLVz0Lb1sor3TAcb95sGysXN9LeZPqJl6evA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb1ec3628c.mp4?token=RSiApTmg4M9GwtLvnrzYbcfG4orhRjQ0xXgSQ4BAMIDEyg77ceGajwGud44vVQCjMi98apBUc-c_4alwyhYGWF4YyHWUaIUBaOxkAU9sps0YZlIdsbGeDdbRKHAGzSaJtBlwzqg3fRZR9f9ogXplbHXy13zfD5YHYQ2PnRNKGwI30I7JQG38BooS8vyUQrCiDRFQ1ht_haXG-DTa47PjwnpKxqJ6tII2odXcP1qs-3M1ltsLO2Z7rhLWTHrWE_XmUtE9CTN0E8j3rvSAb4MUzto--nC6BSZWJYE6EtnzzbhkedFmzRcLVz0Lb1sor3TAcb95sGysXN9LeZPqJl6evA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آمریکا گمان نکند که ملت به پا خاسته ما را می‌تواند در برابر جنایاتش مهار کند؛ یک ایران به قیمت جان در برابرش ایستاده است #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/674888" target="_blank">📅 19:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674887">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRv35uMqTm11q1RrDMI33k6XlE3xoJV0AoGzwnqN5MwCwljmziG3Ep8eabCvyLRen3mtwsXMULsexbaWWJvhWIh13CYLf-S38b8xQyh7FCBDbaHlw_tVUIX5ecE861Kp6ZbawQ-nKItnrjm689YrOweV_DkiN5prmzHokM7ktOGjHJdV7yN2a-7eX8qTjGxfYd_G0qZjVfjqKeC-EuqCMt4pYrsK2cG7XhUvMYYgPuCXK1UnnE4gtXVIYOG1LlHWuCyDdQf8nvD6pDsj6WUSyphOt2KH_UbIRfBCYd6A3sIHIDXnn9OoO6rk48cVD5sOw7f-W-JDJO83h5TIKAnZ1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت درمورد ادعای رویترز برای از سرگیری احیای مذاکرات، بیش از ۴.۵ درصد کاهش یافت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/akhbarefori/674887" target="_blank">📅 19:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674886">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
ادعای رویترز: چین به دنبال احیای مذاکرات است
🔹
پاکستان با میانجی‌گری چین، راه‌هایی برای ازسرگیری مذاکرات متوقف‌شده ایران و آمریکا بررسی می‌کند؛ هرچند موانع این گفت‌وگوها همچنان زیاد است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/674886" target="_blank">📅 19:13 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674885">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBfj6a9HaKqNOivEpDBECUYbCrGAMdb_cHdZ9bKs_KkSssHRJtW8F3RzZfzfaGWWlBvIfdsS5t5f-jJrJ9DEElTXCxOnIlpAeOijpGakozbkg2DKEZx8yYWJoD0kRis5G-q9v57VwGGtTWPJ0N_dvfyKcQVSstkfptOy83wdVMQpwZM8ogShaabg0R5owVbCOoS0534WZy2NVYH7sWcoHaMM_SbfLCJnY2Tywoq9wcR-HGka98N1K-g6JwOYeRFC1jWrwpHBcu9Lq0T3j19uGg-vxtPlRmSag37ZLSSPmXvOSgcsemuExqiMkzeFzTREJG_WECkuPMpKgBUKKbJ8Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سی‌بی‌اس: ذخایر موشک‌های پیشرفتهٔ آمریکا در جنگ با ایران رو به اتمام است
🔹
مصرف بالای موشک‌های پیشرفته در تقابل با ایران، ذخایر تسلیحاتی آمریکا را تحت فشار قرار داده و پنتاگون را به محدود سازی استفاده برخی از موشک ها و انتقال بخشی از ذخایر پدافند‌ی از اقیانوس آرام را به خاورمیانه واداشته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/674885" target="_blank">📅 19:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674884">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7n2JIoSKDscbFOQulyW27qxGQJELhhvz39DUSvhE1powO7fwUqYWCh-0z7zM1esnkndHQP9CfDMsOESJr7Zgukrmlp1yK8tKrUADzoH0-pBnlc8pl6PCL6H4AsYjAEi8-FTo0Z-3pAK1aFdI7NpejKn3me12OWgDQmDuQ4TUYX5efFzFWiQcqRr6BoRFxgIibKq2eBH-_b70evdUq9e6A_CCiVR6Ja1r4uCo236UpkzX6N9qdodxVLr5DuQ8ANGSFe8-Kk_HmnP6qsyw0vkZhh0THqBHF6VFlltJkNwDSowoc55d9kVUrXumzOtmsnvjYeRNYZ9iZzmm2SXZz2B_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در جمع ۱۰ کشور برتر در ذخایر سنگ‌آهن جهان
🔹
بر اساس داده‌های ۲۰۲۴، استرالیا با ۵۸ میلیارد تن بزرگ‌ترین ذخایر سنگ‌آهن جهان را دارد و پس از آن روسیه و برزیل قرار گرفته‌اند.
🔹
ایران
با حدود ۳.۸ میلیارد تن ذخیره سنگ‌آهن در رتبه هشتم جهان قرار دارد و بالاتر از کشورهایی مانند آمریکا و پرو ایستاده است.
🔹
سنگ‌آهن یکی از مواد اولیه اصلی تولید فولاد است و میزان ذخایر آن نقش مهمی در ظرفیت بالقوه کشورها برای توسعه صنایع معدنی و فولادی دارد.
آمارفکت مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/674884" target="_blank">📅 19:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674883">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYHe--MgoDfmsqbLfFUAz4IUHvPdheGLEBsc8E-_BpnVXTFTkISVNUYAUg57rAzxLjUIyiICOscrc4GRQoZjs6iHrjKEg2Dz-CESpH-rxb9m4mLLYtXJbHNW-B2VhaNFOMJVthXAOAPRApH6plh-17r9KRFd7TJVvPKe_wB-iKVTAHFyD4My3JuEqBbHcclbCU_T94L8npTJf8K8hi-Pd4UmcD0FRxOXZvw8GkYvF43oxmi0zMp8e8lexVxgeV7TNlwS-gEk3X9Fvy-M1v4XjtkUSfKsukeDyqlAxtOjVpfv1aON0U8-7dn_Exggvtnl3V_POMa2fHz7bBRecH3ojQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قبل از امضای هر قرارداد، حواست به حقت باشه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/674883" target="_blank">📅 18:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674882">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQq_7a7ph_hSTfizJ81i6aetCcT6HLfVr5Tuh_1gg_Jc_s496RRbLIzyZq6VKOKhyyl72hZ4fB3xex3LYHksBOjkB2br4y0Z1sUH9uySjEYof2WYh-olZD8qgeGDctiE3EUT7qk-998d258MZSJAjujs3lDMg9bdd83C4pwsoVnEDYpW4poMwKSB2AV7ccaLZE44fzcisfDdeAsjyRC7YTi1ds4xScMYgSfZBJMjTayypL5dEeyk0Uuuy4R4os1kmJ-gI_E5g4rQXocLIHIWuxBKESKl6voikvS_4TIyiHNSSiAttVm5zbcjuuZPzMH9uqo5XExVMnuoH0KaaMys-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای خوک نجس: رؤسای جمهور چین و روسیه به او اطمینان دادند که تحت هیچ شرایطی به ایران سلاح نخواهند فروخت و این تعهد شامل شرکت‌های چینی می‌شود
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/674882" target="_blank">📅 18:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674877">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OhzjiFsGuWkg_lg1HrogtznIgxHfLRSDlR7fmOVLcOOt4wJ5ASOuwUZjs6lR4Q47mU6IuY4DmXwbihc1OzOsqsPTom23tiRhRWQUshxk_56PkiPTazhaCPr9Lj56JWw-foPqVX1CPm-P3z4GKf65KyzgooTqC2f4VCNvnKTRAsHGej-ckbhcz4QHFiEEKspzmvOBQ0TvzVALp42_rQmIdeG0sIyi8eOWSxkATNrNgm1EgCz7uxSDIqUre5LGvMFUsP-zGEd9iG_xX_MHaoja3Nx-bYko0z_Q1GQzSboKiNNjaRtUe3hBNXmxnu-Z1EbBr7oAtbsadMccxvTlBZN8nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UF5kQDvowoUcH0L7oVwyeXW8OVTce0IYRgs4-aqDVIze-2kyB1BEOLRToiS4M_-HrVT4K9GUOx9g-GiQaJYyzui01GhwjuEU38EDRBxfvsYWuyl4ugk8SBQWo6yLbWqai6Jt7NBdTxoXeFiiask0X0o7UldoN9MqBFmSLi2TN6Yki4Q0va4tssfKbEKC6gFXHsWcMGBwyNzopUEcS207vomLrZgRIim2Fq3nz44N_zG69h9Myu5Ewx34Ii2xoR9ElHCEtMC0buCSrWUfpT-g7qMnD9lgNXoRGLvkL8jk51XXPxgiqf_F5JkFw5xp-YqSxsX_bA6gaMjUuHYBio_1pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l7clOa-XmLGi876mALnHxdN-U6C0BfysGTUyjM2goahAx6YnZJ5LfPvl3jXMmQlY0Z7AGTqvihY0pXAB0V2lW3Dosnrgsse_D-Dd2utgU6R7tVlQquz4ZfHeEcDlNNhaRO5jVTXiANR7KpiMvBEVOTMUceqOA_UILHwEItA0QZKseOTNdDbndlNsXydPOe_s4tHF55ch0x2oQb7Zhf_WM48SZDjj5KBKTZS7DekD8-JSx-jeUfXIDSHleTxfqDAGUUHV93aVXD0Ehf6-tM77CKEIC5tx5h28ZCsfcVzSxCVVmYVmAae8X_4R_2XBE4AdiLg2ndPhSCdNHv-gvTsHHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iZg3t8EDKKoUga2HFBDkXG9YEyk7BtgH2n4h0F2RdRk3EXXrlS1g3gBmFNeLiF5WjWBjMGg3ELFK_TiSCApEHoqCJiIwWT46lQjT9BKhTvHDtP9S2JN8-GrmBT8QLe1bx6mGcLGdeFvSZmzEteIFX6tIpKEgkAw7YkbyCsx5CTjYCp-w_9_AMbLN93lLkKc8u9cEOT0cJlMoHfjSYw927Em_uCBXRZLvuqF8vk6VV3VVMmt3-OyPGkU4IchLI3bQvhO-1lU8nsKd3evZYDpmJ1sP5_eWe5JTMQyrO8b1zGAaG3LTeC7UCYwGknE9dvyKJhkFnAF7dzFrjNcydWojuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DfQT2Mhv8EEPATSzvBuoMoxB3Tt0ACvJ0hDdtU6gTroYdfEWL4KY6iiOebxNkBVQ-eUeGHLx_DakrZV6BENjcVDFIzWbNAzOVOrsEvlUjDDIV1SWNGzHOMpaGI1MaZrF84kSQJBTg7RqUK7hdQoFv9OnJ0UhKUkjhYZkyz8R8xb6Vd-rgHWPjKf8JvS2_Oh7HYc3izR1084Ifb9oHjx3V8ekwAtj6OPnvsbBASW7VSofUdSiUlttXBnMD6-IxC3J9Hn9wdJ-MUeRQfW-6OaJjGIurrqR5LvbC9qveNMKjeeYl7xyfiGgEPjrt9VwFESJQf2a4-S0OlhAWU3qeG7TOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۵ ماسک خانگی ساده که پوستت رو شاداب وشفاف میکنه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/akhbarefori/674877" target="_blank">📅 18:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674875">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXUWlx3cSzwZWuYHCVrHLkHIHWZNxwu60uZQoKEIhD1Iz8KjRqNX0wxM3Bhk5RXX-H-tup2t5hjXUjw4_ewKXx1kAeIba5JbxrDsLwV2x8h5qzt8lik8-d9v_gByrySMiQd7QsWWEbtUNia-EW7ixbEj9m909cEjQTqlWxOf_sVI_JRjeRucQALLgFvl35eAwQiL2URaoUGsOf-gC9EmYL7Is2nnZmBV-ldph1iGuLSFCP_sfi3UOoeVrnUWQArE2cbHP-YT-_5W-Y-bwIUscPw1M1YbAjCwymDIu21UZOVzjaXLOAKG4OYeBDEys3RabYqrnEusDETCZP9nKTmNtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
♦️
پس از فراخوان بزرگمهر حسین پور صورت گرفت
استقبال بی‌نظیر از طرح خودکار بیک برای طراحی چهره فرشتگان شهدای میناب در نمایشگاه شهر آفتاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/akhbarefori/674875" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674871">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9699dec59.mp4?token=Dj3S8kKv_3kyi8shuvtnCPSFw-yGGan5vvD0m6yiti18qfwZld2YKz1y4biNKz4UWt6NURIBtZetJduhuTqpBGrPmszdeVYX7792-mI43-TjeW8GLlLoXDXqzIaHKUY6LSxh8GC1D8qR-CtCVBv2IeJQUo-b3V0RGL99ag9ZeYsmesnxC1EGtwCWFCOMyZUV-Y8SJVZwV2mYA5_DQB3ReOFForrsJG50AwbTy1WI41xlArQC_DIui6K9fp2rXfzUnz-J7H5WboFs6Xf-9p51FB5G5OyzkpUqgOWNT1IhAkZBya5j-JcGoqFj9VfSFInqp0vRmnYc2o_G_P0A5CNsug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9699dec59.mp4?token=Dj3S8kKv_3kyi8shuvtnCPSFw-yGGan5vvD0m6yiti18qfwZld2YKz1y4biNKz4UWt6NURIBtZetJduhuTqpBGrPmszdeVYX7792-mI43-TjeW8GLlLoXDXqzIaHKUY6LSxh8GC1D8qR-CtCVBv2IeJQUo-b3V0RGL99ag9ZeYsmesnxC1EGtwCWFCOMyZUV-Y8SJVZwV2mYA5_DQB3ReOFForrsJG50AwbTy1WI41xlArQC_DIui6K9fp2rXfzUnz-J7H5WboFs6Xf-9p51FB5G5OyzkpUqgOWNT1IhAkZBya5j-JcGoqFj9VfSFInqp0vRmnYc2o_G_P0A5CNsug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شاهکار طراحی خودرو دهه ۶۰؛ نگاهی به کابین افسانه‌ای تورونادو
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/akhbarefori/674871" target="_blank">📅 18:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674870">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
سی‌ان‌ان: کمتر از ۲۴ ساعت پس از امضای توافق همکاری هسته‌ای غیرنظامی میان آمریکا و عربستان سعودی، دونالد ترامپ،  عملاً این توافق را با اعلام این شرط به حالت تعلیق درآورد که تنها در صورتی پیش خواهد رفت که عربستان به پیمان ابراهیم بپیوندد و با اسرائیل روابط عادی‌سازی کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/akhbarefori/674870" target="_blank">📅 18:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674867">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
دفتر نتانیاهو: نخست وزیر رژیم صهیونیستی روز دوشنبه به دعوت ترامپ عازم واشنگتن خواهد شد
🔹
او روز سه‌شنبه در کاخ سفید با دونالد ترامپ، رئیس‌جمهور آمریکا دیدار و در مراسم تشییع لیندسی گراهام شرکت خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/akhbarefori/674867" target="_blank">📅 17:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674866">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_iHtleuvUSvzEacX994KEhgkAEITHD8B69-WWjclxQrzG_8HSwAFDVm_oCHC5-oz-3WI_LtNSLgC-9D3BBlaW72I8JI3M32h09B8tWUVquPbVxLSdOUJYO0ieIDp6psOPjuODV9975SOpLAbK688Ic3BWjLNfYawcAS_VDu5Fk6difdaam-UCJbFhvveHSLNx3hDHj28T2rIwQIzKHMeR2t9VN1wDI7K8vY72vfXC0iwoihf6OnqP0BBu8RM0Z0Z7B5BISe-pmfpOx4brogq9Bv0YGSnM7amjDVCiaYqlfVpkeZFvu-JRRbYrlh3nhA2LdkzUWKRx9NV8Alm6NSKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اقلام ضروری در کیف کمک‌های اولیه در پیاده روی اربعین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/akhbarefori/674866" target="_blank">📅 17:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674865">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دعای خاص امام زمان علیه‌السلام در عصر جمعه
✨
گفته شده هرکس صلوات ابوالحسن ضراب اصفهانی را بفرستد، حضرت حجت ارواحنافداه برای او دعا می‌کند.
✨
بیایید در این جمعه‌ نورانی، با فرستادن این صلوات، دل‌های‌مان را به عطر یاد امام زمان ارواحنافداه معطر کنیم و مشمول دعای حضرت شویم.
#گنج_پنهان
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/akhbarefori/674865" target="_blank">📅 17:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674864">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDyDsnYO0xaNbmRx_2G84zJy664qbOeiK6KLcpaCvClcmzsEYSk3K4wKXSZFdg6XB1jJUMqCxGHL5lDe4_z-3cXwNBll2zIQpXVy5haXrMrL-33WbySf5Z1p-SfmfXHEu24AHRnSSPyKXvT2ZIhGMQvvW40lKx58BYPBO458MaCLkzpNgqwsF3hjc_wo2AIDeYBk0bYp0guoodZ4nBFPp5d6pOtlSLzDo-Z_3qrHlYZ9BztVXVx5ojVlElIvsQF2_6aElZ010soUL6MX3csrzyElwktLUvvyOjg09MW_lk1ztuHtvAedgjhIP_jbmAZrScVGvkZ8M4m3Q7fytlzFGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیدار معشوقه پنهان ترامپ با زلنسکی | از نازی‌های اوکراینی تا توهم ترور پوتین
🔹
ولادیمیر زلنسکی، رئیس‌جمهور اوکراین، در گفت‌وگویی با لورا لومر، فعال رسانه‌ای و چهره نزدیک به جریان راست‌گرای آمریکا که رسانه‌های این کشور از او با عنوان معشوقه پنهان ترامپ یاد می‌کنند، اعلام کرد که روابط او با دونالد ترامپ پس از تنش شدید در کاخ سفید، به شکل چشمگیری بهبود یافته است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3232773</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/674864" target="_blank">📅 17:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674863">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ee7fb6622.mp4?token=JdQohwzGrefOd3TbtO2JKv5nF9946wE90rlfmuQqMzQRfVY6MlFfJ6wP0pmjrIEjqD_6zKLntDpduo865kXcrWy8oUgVorSMa5mdhIwGnFrVul5km5J6bsRBFqpPH8XVBplBC4sXz8oUcansJt7FAaI5SOdXkAGvPH7h41cQ7_rIzqeEhh_12bC3vrheZyno5FcqYI_EkR90yrhjxjReBnFcz3yNRYWI5KWhYM3DgSVuNAvZb8UZTp7Jo2yr6UJbpgdBUlFMzOMEZaKsFEDvAWqn_i4zDy6fvlefMmnRfjmUpWCOpZhAiGpyF4x7qvFW-LYEL9aBZdjLWYFLq7DxEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ee7fb6622.mp4?token=JdQohwzGrefOd3TbtO2JKv5nF9946wE90rlfmuQqMzQRfVY6MlFfJ6wP0pmjrIEjqD_6zKLntDpduo865kXcrWy8oUgVorSMa5mdhIwGnFrVul5km5J6bsRBFqpPH8XVBplBC4sXz8oUcansJt7FAaI5SOdXkAGvPH7h41cQ7_rIzqeEhh_12bC3vrheZyno5FcqYI_EkR90yrhjxjReBnFcz3yNRYWI5KWhYM3DgSVuNAvZb8UZTp7Jo2yr6UJbpgdBUlFMzOMEZaKsFEDvAWqn_i4zDy6fvlefMmnRfjmUpWCOpZhAiGpyF4x7qvFW-LYEL9aBZdjLWYFLq7DxEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سعدالله زارعی، کارشناس مسائل منطقه: مطالبه خوان‌خواهی و انتقام به‌اندازه تسلط ایران بر تنگه هرمز اثرگذار بود و بارها واکنش ترامپ را به‌دنبال داشته‌ است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/674863" target="_blank">📅 17:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674861">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/045a827bf5.mp4?token=Xvb_98Kfq1-1DGVNVHBR-2-T4LItSNU816mnKWWvJK5DvktBR0ssjXkfZJsOJPgfrt7pl7TllqRSuHM1AKj5plieeP07GOJMbU9wQMIjCMbggQ7UvSeXY5Pk3K8WgmZ9SYT58IB9mf25o1v_SEJG3zI-6URnBnqds1K0DcT5UzR5VfzbcH-Fc89kglQmgjh7q_stFVskh7wGw3uuemkrWd_HVlYMISAsBlk9fSGkAsbuTUw48Umrnu-FboQ6cVKeyoUXxdCYrAmpuF7a_f2EPRod4D4TVdAjq9uCrW6bbwGuPwVCUSyHLUfaJaE3foMbZv-qpgZDkYkeku5rrvw82A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/045a827bf5.mp4?token=Xvb_98Kfq1-1DGVNVHBR-2-T4LItSNU816mnKWWvJK5DvktBR0ssjXkfZJsOJPgfrt7pl7TllqRSuHM1AKj5plieeP07GOJMbU9wQMIjCMbggQ7UvSeXY5Pk3K8WgmZ9SYT58IB9mf25o1v_SEJG3zI-6URnBnqds1K0DcT5UzR5VfzbcH-Fc89kglQmgjh7q_stFVskh7wGw3uuemkrWd_HVlYMISAsBlk9fSGkAsbuTUw48Umrnu-FboQ6cVKeyoUXxdCYrAmpuF7a_f2EPRod4D4TVdAjq9uCrW6bbwGuPwVCUSyHLUfaJaE3foMbZv-qpgZDkYkeku5rrvw82A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر لحظۀ شلیک موشک‌های فاتح ۱۱۰، ذوالفقار، کروز و پاوه در موج ۲۷ عملیات نصر۲ علیه اهداف مختلف در کویت، اردن، بحرین و اربیل عراق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/674861" target="_blank">📅 17:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674853">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n-qTq2iryrb0cWmTPeVg-dICIwEfUdjcWxdzU6l2j-rDeNYIpl5LaWE83ToQYeOxGJCBI_e7mH1V4sAPavE9Gu-IlJEF1Lny9gD51zFfSQ-cq3FPAjbehNxrcv9C_TTmUumG0-TjACsGIp5oGhvEgOMeqddKtdowkOR8NN_wUwtcib3pUCB1fgiE4kD-ciZnmZ8KOX3dWA3potMaTelbPATX0DKhm_riLcNcKG_H6je4K0mmMw39nNyP758njJrzpZEBQo6AgHvYFNDbGXuTk1pD6g5xSOTo07IYKB1EnLMRMosUrXIBMmu4X2oo0Mw4mBG-Jeswfz55aIB-9EWrmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UDSgZBUwC-F0GkeesNeqzn56NEOvCwMfeKK0LPma7KzCtJwI9ivEc5PvxCDCgf6g2aGYutlAERw_fBxQPNvO_HSH36A5NNt43T3j9sDua4NXnCt5ZHEuQR7MebOUum6964t03UB1c4c4a2kIBXyrnhEpyVKNzyCVPHMKQClhfcGPrAvRF99tS-8P65L3O4AQNuPZItv300R3d18fIqUSdk1JF9X93QKtwQUrEoG8oX3iA42ssKLuXSIjeGXsYaKcAl8zCsLCUwguhjJSL6rU8-wqxzVN526nTBCHqqwZ-ag1z0xlGe5rdZuWtDFOICXZCS0n51yBFt04aD0sX5H2cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B8cFp2oX1H_9s5i0153TGkhz2uuWNu9dfTYI00p8hGle62-mjNQMwU9Fca8PzcuP5MAHbLw0qVuECDge7BG1PHWQcqaO4YFbnq2Xo9Big3uad9X_oP2QniQ6WjvSfCzVcOYc07BgMy8oNDIfDlLFLv6LQEgSUC14e1z4oXl68Ge-KfladbTenuPHHfN03OsYsY9YkTgBAFXDi23k1fHEAEWAqIcS2NT0nSGNn8zZuKDEMKJiBofSXCNLTPZMCWVmossfq2ejx_0YoHkgMT53EDz87rKVRVXQqdMYD8-j8R9k17LaQ62J6XjzFb4bqI7hwMWoaul4AnCQFzkYaeM69A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mLqr0-4nG1Uy46iK6NE7CM1mcy9hXD2Tn95Na-lzUbumbSoxUjgpgqqcc9v5i2Hl2Jy-l39cvTBrumItR_WiieDE8GZ9RjhJHcXMpuVWpHSyOTRfYKfPlmlbwZ-Vy8AzTmGdJLeSLn6fGrvgOy-liKBAfwsQtQ5qDAp3PAgXwFcIvf7bl4jQJttWsRTHUfsMdNa1lCmtjOUnNfe7ez294vUYevYYjBGqt--QSsuxb9OwDkEl-KOjblbBh3r_kAg25-caXkLyA-cEr1UjDODPTnX45e0Ql5TzXnDCw5IcRAfWb44VsES7aZ5r0e7s2p5sQ5TcF7XOWR2LuHFiKyvRLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hfFO7qR_5tf2H2W1laq0C00Ieg8U8iNrE9EC5pIeHnAIv7lW2DzzCTKcAIDg8YCJJSKs_mt9eUfhncU05RQ7mDpHGYT9J7Du3ybnqY_hlk2mF74eNXgC9suaSp_kr-LqjxO8rf03GiRwmgbKZjTYd8HuhuYRjtqqF8QU3FKehcRFrC9Bs6hifvbrJvdPGgoMNMeK7rAngyK1tczAeQFc_0wl94y37DcXTy8xZlT6bzzR8H4RpWhqaP9Wy-Y51IeafAfhiH-in9AB73BAq33J7fT8ipeRhVw_d4iAzyedX7lwzlOlEbRU3NGhQ-cd03v3pPKx-REANYCGDsyy2JOs2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gzISni1cGg58bd5g7qBwzVY7FxChJD8BiZDnMfqv2sk9_whbtdMMzNkLNFXFMVSMY3uCk_yez2Q7P-IalGpdLcVZpkBlQpDG-XzPncFGBL5TVeXw5gsmO4S9NpETn-PDj2QzUHzAVtifCaFepvtKHWJSq5H9fDM9EoXfkhO-FFW6dG1F9-Yi8uH2D_a2bes3drVlRJ4bHG5DxokkQ3dCpRG8Q6B-cgRhf5nR0TJfHXYb-j9V3EQY9D-vJ6dYiVdPI0185HW2pAsR8XLcMoqOzjwrJzWZaQUvSIKDpasfRaxLe0xogSxm6XMf_oDaKofw3lK2hXxfLKywmRSeCnDvdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QS6av2DvTwRfa0bF0M87pEYGnFpZsM7vDp2XHvWmK939NBHQlsRDGUH7Wp_1ROrdWSOGuTAP5yU-LvOg19FuDFF632461q72IifS0fL76zNDZ5JR6x2agyfyKneXs9YA4wcFCS4cEU6EFKV2y7da8dmoelfFpx7mFZUF86_mj4o7HIsU8YYlBv1SVGerS9bYzSougjwd79oxTDAtdQ6VqVYykdBsKvMlpGD5j2PQLvDQ9H7rihZj4S0_U3wXq7aSZR7HChpYmjEPYDHatK30XT3dkdOkKzHJ1GGFYNVsVgGT4GL-8YiCy40ggFLDHqhiXkf0FzbHM6c84aeG7YFNnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oHuv5m8AInStrwDGstJANo7vlxbznokzKCvniLs6QXYehNEtQLclhYlZgRd_2-m7QgDIlGDLV2pB5hoKeKAzEIVcdX1DFZcJqoYcKz4N4hQSJDZdmNcovT5iTIOsrmPAT_Z_Nvmx0LVOeq-P1t84paUz3J4FDIhPw-UzSXiYEOeTFJNYpSAXX9dnG9uc65T50cOy-8bhkeZrFRTf_oZO3eGwO6FMY7uKYphpXZXg8W7dBdTcncP60sRgqattI5dcuE0Y4HHKwHvo8xbduPcr9FU0gSF6UOzTwr-36Fm4aUIPljDSO8__IkHTXpXsbt6MjM1im3J33c-XG2G10JL-bA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
واکنش گسترده کاربران فضای مجازی نسبت به محدودسازی کانال خبرفوری در برخی از پلتفرم‌ها
🔹
تا این لحظه بیش از ۵۰ هزار نفر با ارسال پیام به درگاه‌های ارتباطی خبرفوری، پیگیر آخرین وضعیت دسترسی به کانال خبرفوری بوده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/akhbarefori/674853" target="_blank">📅 17:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674850">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u0UuYi7XEdLUfYb28SxK7DUtXSe1mDcAElNZKVw0MqjYkiNg8JFw_EpMjGPrVuI9xyGcCO_pODceJ4GucSfz6_f6yEYMdUSZlC2xYfEaDjyhY1Reiv71mOMgNrTkoYaRScPLfi6kSSAu1bJPr4Lh1jPG3xORNjO7f5oWVSD-7Hz43k8_eRd56xdCC_5--oZQMxSb0soAN5_WI8_yDwBP4qihh_vkWpFIvka72AUaSMUq85rdHbotZ_er3dCoX3NHTtpm3CbEG3LYbTUcH7M9NhHTEGNmkZp2Nrbe6DEbJmw6EyYyPYIXCrtc1fczzLbuzjnG0t_gY-9J_JLzQ52jpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D1UKrct6rGqYFdlX8LD8rYADPLwPqjscUe0OvaVZPMHPKoelqgC6x0cuozqWY3f-vZ6y0tju_7YxDZk9Vxa-2uOIWIrjfY5jypmJTWfTaiAbhg4YRIUTqpVnQ5sGiPcShn5AOFQrGaeGtr7jGalMcQaEjHEH4YIQCsVJEeXejuXkpfAAjcwGoHGyITDqgl7AWnmiNgMkgxKXyrDKFY7B0vY6S250rMYb7tpYvRkbcVaVHcWgdewpQD8dM78rfQeYbPFldMjbG-2HsaGJRAdYT2L1sYnuxE_HD7X22OYejJByIXMbtVkEWWhczeIOCl8rV2DVBHTWWPArGiZZnFVlHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pSzNmOmicyfHcaAZYuiSG70j6kz6jZDTuvcCq-YjCtyR-41zuBtdXZDEHFgSAHerF8zZK2PbQe6rhl2_Q2Qxa-IFPDz4mx-3XtlVuBQs-ZiisgOzPp38cUwDg0E7kr6PxhnioPSC1Ntu8Ehd1WwzISse12HG1wKAGTZ10DKSXZNF4EqMZAqZcp0vIIYWSVSJ1-Ct3LSrkEry-seQnIhu6MP3Kovvjq0okwwi5pUJr5RL9FUvbIDLgn6TOPWqtxpvJFIhrIfrsI8xQcd6MS_rKU85fYD73AxHHeBI9gDXUFz-xXnCQ4wl5-1YnFgsRzZKFyEp3-mHkNFjFzosHHBhUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۳ نوع سس جادویی برای چربی سوزی در غذا‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/674850" target="_blank">📅 17:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674849">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79956eb4be.mp4?token=APrx4eMgRU0ku-Hy9T59EvSF5tMwj1-GMzz2PSb2sEGw8QhS--UGuiBom2cQ-vdhpR4kmUCowNZnC9YcLm031ppHAsbic3tx1UfvSjXpMRay5o4orlaGVoJeP-DGaqx-U6DUbRfSuq7ViTS3PRRFixaUnZ-bM9v_e24GaOqSs4FZ9F2DCt4_rm83IZQ3RB2sXlu2abtHlMhYMfWV3TuCcgMTvI8vP2P1HwUeT94QD-4g5ovTonGfmI7FWrYMHrQ6Pr5qdM9M9p_ISO44fXRLbyNMP-Ia1bITfwpnaa7Ja5-cgg5UxATxAO2-MD6lVKcZyiLucMHa8Wyh6i5MlTngwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79956eb4be.mp4?token=APrx4eMgRU0ku-Hy9T59EvSF5tMwj1-GMzz2PSb2sEGw8QhS--UGuiBom2cQ-vdhpR4kmUCowNZnC9YcLm031ppHAsbic3tx1UfvSjXpMRay5o4orlaGVoJeP-DGaqx-U6DUbRfSuq7ViTS3PRRFixaUnZ-bM9v_e24GaOqSs4FZ9F2DCt4_rm83IZQ3RB2sXlu2abtHlMhYMfWV3TuCcgMTvI8vP2P1HwUeT94QD-4g5ovTonGfmI7FWrYMHrQ6Pr5qdM9M9p_ISO44fXRLbyNMP-Ia1bITfwpnaa7Ja5-cgg5UxATxAO2-MD6lVKcZyiLucMHa8Wyh6i5MlTngwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خاطره جالب مهدی قایدی از خساست بیرانوند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/akhbarefori/674849" target="_blank">📅 17:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674847">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99e3dc7e56.mp4?token=ZWOk3cV0xU2H-U21KWHCduZJVyuYssT8efmKFWwND86wKL_myAULhNsuJ9I96AM7PzkqleR60oYdLvoUwm-stg-L7nP_svNQStNXG983dYL3hoeuyIJx8yoFpozXfs4__AeXxE4FlQkXZTMOcmuHQi5RFAu7LkVzOLL4gyUtbQFBecB5e1QLekSnyWVGo1-QhYYmoZK71A7rEM1eJp3E5wwgBHX5oXECoNnvj3wSi-Tm-CLWRrCV_oqoXqlKf7D2h8H8LW56Ro0dVZUI3HtuI8v15M4cqaQaPUiPCb_ozjJbYUYFTYpu-Zno6vPteKv4N-iQFtUnc3QOWx1TeD_rTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99e3dc7e56.mp4?token=ZWOk3cV0xU2H-U21KWHCduZJVyuYssT8efmKFWwND86wKL_myAULhNsuJ9I96AM7PzkqleR60oYdLvoUwm-stg-L7nP_svNQStNXG983dYL3hoeuyIJx8yoFpozXfs4__AeXxE4FlQkXZTMOcmuHQi5RFAu7LkVzOLL4gyUtbQFBecB5e1QLekSnyWVGo1-QhYYmoZK71A7rEM1eJp3E5wwgBHX5oXECoNnvj3wSi-Tm-CLWRrCV_oqoXqlKf7D2h8H8LW56Ro0dVZUI3HtuI8v15M4cqaQaPUiPCb_ozjJbYUYFTYpu-Zno6vPteKv4N-iQFtUnc3QOWx1TeD_rTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سعدالله زارعی، کارشناس مسائل منطقه: ایران با حمله به مراکز تمرکز و دپوی دشمن، از یک برگ جدید نظامی رونمایی کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/akhbarefori/674847" target="_blank">📅 16:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674840">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oapr1fS1844St_uLoVR7aNqKnJYBQGqgRSEyKN72ncHjapZ0UrZjtrx0ekbK2uOXhV7LBK6his73terLF6b81tAzsgrl71Gcx6D_gXq5VxfWRMwV1z-o5Kc6p1GM4i_U51x3I_5FB29l1x_SrNzMb_jTqZth9lT3VjSwMjriIJ3abkIX8zTc_PrTamYwTGd5jud16D0QprCaUFkQjt2c9XG82Io48CaY7k6UyQ-mOFpzwjoDjLmrWYuBnSzrmL2NmnleTbyXSQKscGFX9GAoPRf_Is3YfhKMvHTMZlLpa8hgeYXh3Fw6HvQ5a6oe1J0iBMNOofT_jngcCMweMzm-Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y0JuAqMLhGNvVgEOX-Nb7Lm0ZzqsTDVlZr15W8n5QEG_33RpaGdts4c6b_n0PV-Zo48rCdmC-vbeSc41admLBFLStoSiuKJIpl7g-I65bElfh_lYOq-r_giDf4gDWXLN8oJiGOf1omx86mCWXsjinOfsDyevPxCvzsIa7lf4x5rNaZ3cxkF21n5YEiEkuUKBiNwInY3WaR8vTTsnNj_hCCRBzSHxWgOnKNhuqGdHeRkYI-paAuT0CsKXdYa1zT4YpT3bNdR4vwH4EbEqcqgbgDHt4fIDjDOffMltj5syuraUSnzbfpCJN5pnOeo7UfZr_U9lfBzwpLYiHqF2Vc18rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e2BQl98PYwTeOl2Js_uaQwkpCMwM1Ztg4rbtpRBOc_BVMA2av0qJema7qlpHzAf3Ps7hc1hzc1ab5HyQPk2kJwHSJcWmag7PIe_yoP9MQQHdKV9Y7uncljTI28AFKfIE3hJwdhQjLK2vbFyymSIJ8X6Rg-o3SN7TBLxLk4sF9ZAIY_kS4XKYevXQSSGF6Kvxof_8HZVLDwDiToNj2ljXik2ASkgh0JsXPL8ajaspWCGRdIVixHkThYnNZcUUgs-iSsabu8pQZam3tahQH1PHgw6O9XV72Az1jBY6j9WvGVInAHvIwugw2orm-IqI1xGFbXUVo7aGxC2e8NmUQ457DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HFypLs457c0KHi_X0M6LAu6NwFIW4W5WElAcqa-_yoAZHmUAwQCZaaHzr72wsJERnSsRP9Cty4i4rgcbfIi8NeaHE-Z18zRDeV7Ad6YO82NByESwaSXySRhqxfCYBJYySC6j8J3Wu9tGb7gG0cNB3oY4kctla-1JpJD39JoOFlcStlSfstMiLSaOiqkQ8wacbs4GtIwTrY0F4m-aVVC7yEbzouzaaYhre8w46-baQv2_QqmzfmIwfxSnR9LbTjBatOy3HF6CJrY7TEdTTq5rTxOAfuxLQLxw2ek5CZGCa5LOloVEqAFNloA_jZHHdopVUoWDQGJf_-5n1rnJcc9EJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بازار داغ بازی‌های دیجتیال
🔹
گردش مالی مستقیم بازار بازی‌های رایانه‌ای ایران در سال ۱۴۰۴ به حدود ۷۰ هزار میلیارد تومان رسید؛ این رقم بیانگر هزینه‌کرد خانواده‌ها برای بازی‌هاست و هزینه‌های زیرساختی را شامل نمی‌شود.
🔹
بازار جهانی گیم در سال ۲۰۲۵ بیش از 180 میلیارد دلار ارزش داشته است؛ آمریکا و چین با بیشترین درآمد، بزرگ‌ترین بازارهای این صنعت هستند.
🔹
بازی‌های موبایلی با سهم ۵۵ درصدی، بزرگ‌ترین بخش درآمد صنعت گیم جهان را تشکیل می‌دهند؛ پس از آن کنسول و رایانه شخصی قرار دارند.
🔹
۹۴.۵ درصد بازیکنان ایرانی از گوشی هوشمند برای بازی استفاده می‌کنند و بیش از نیمی از بازیکنان، بازی‌های آنلاین انجام می‌دهند.
آمارفکت مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/akhbarefori/674840" target="_blank">📅 16:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674839">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d3d111df1.mp4?token=SNOFT0xCBvvjA_IVjC1nLYQQYqRaN5RWs8yngQMUCSpCN4i5qos9r_m1UKWSvyfdoeOMOaOQbdYo-6TXhJSpnpMQWIm-MbkdHwvrlKY-5Irkq07NWiqCu62lNBu77tCzY11w9RVXnwDcrgzB_0lmQ2ALTIq2hWRNtUHQ-8D2BR-pqGrRDDCYWySVVdsXU_Mk9GdkJM7U8MTQslcN0i1-JhO4pgBwO1YI-wvALKeuZZadl0PFOX8KuIYpLd_12fY66B71pwdRyEh9LEcrr9KhnLOnJId6l-2ihi5wV3f97Ml5wtJuyPI9EuAf58dMICXtA1Gt_FRzK4ZM_zkI-sSoCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d3d111df1.mp4?token=SNOFT0xCBvvjA_IVjC1nLYQQYqRaN5RWs8yngQMUCSpCN4i5qos9r_m1UKWSvyfdoeOMOaOQbdYo-6TXhJSpnpMQWIm-MbkdHwvrlKY-5Irkq07NWiqCu62lNBu77tCzY11w9RVXnwDcrgzB_0lmQ2ALTIq2hWRNtUHQ-8D2BR-pqGrRDDCYWySVVdsXU_Mk9GdkJM7U8MTQslcN0i1-JhO4pgBwO1YI-wvALKeuZZadl0PFOX8KuIYpLd_12fY66B71pwdRyEh9LEcrr9KhnLOnJId6l-2ihi5wV3f97Ml5wtJuyPI9EuAf58dMICXtA1Gt_FRzK4ZM_zkI-sSoCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جواد تاجیک، راوی جنگ در تجمع محرم شهر: فقط در شهر تهران در دو جنگ با دشمن آمریکایی و اسرائیلی، بیش از ۲ هزار نفر به شهادت رسیده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/akhbarefori/674839" target="_blank">📅 16:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674838">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbFM2ctKJ7o8lV0ne7mUxhsJdJLOtt1VYh-MmUo0B3f9de0heSzSuPodRI_5EXjh-zs9DXHVJuimNne5Sv2C_Yt-teVTroSm6x0B7y4QsxLvjV9eK5rh3lg_HZVknXFK6bZj6oKj3o-whEAowe3KniXGV-aGJEznkZcvozQTW1Ma-lWD4IoSHpLVcYLFnNf4NG7RPK0RYud1Nd52o90EJqLce3gf51j2VIjbNur8GUx-ENSBwjXGo57H-FO9F18p_NYSusb8lqnM6cCyaeNXrJ31GqaKJgrGDuXO9ueCQXzxbrs2ZJ94J6VXPhEhGzwk3E3aNZdozWTNkHOcDzVIOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تخلیه کامل هواپیماهای نظامی آمریکا از پایگاه العدید قطر
🔹
تصاویر ماهواره‌ای و داده‌های منابع باز نشان می‌دهد آمریکا همه هواپیماهای نظامی خود را از پایگاه العدید خارج کرده؛ اقدامی که برخی آن را ناشی از نگرانی امنیتی و نشانه احتمال تشدید تنش‌ها در منطقه می‌دانند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/akhbarefori/674838" target="_blank">📅 16:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674833">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dbaf83b8e.mp4?token=PxZGKYR8j5_bhEhftGi-CsC7oNyQ5aULCq7wl2WJ5PMxdgv3T8l0ZXIaCP1_nUB615q-s88hkOWbilFxCr2sNoVr_MwpQcRTv8eZfWHN_70jr8OOAmwfpDy7-7bWSTwyhEHzY5zFs0I4l5GEwAdj7lqbJ3J2KX44ZtVatrmVOwETwDgzjkIh1xVsHapbQwiVqA3Mx6sWMW7SpNHHluThnYZG-8OptCOzgwcYlDaZWqOAk1V78-p3yYqukxwOg05_lWa55MU4jxXgwNYUc5Z0-PI2wCCx_zXXzk1cFsFX7_qPhkUAU6oAPhT6_8L4QgkXQdU33T1aHYyoTgVkjcsglw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dbaf83b8e.mp4?token=PxZGKYR8j5_bhEhftGi-CsC7oNyQ5aULCq7wl2WJ5PMxdgv3T8l0ZXIaCP1_nUB615q-s88hkOWbilFxCr2sNoVr_MwpQcRTv8eZfWHN_70jr8OOAmwfpDy7-7bWSTwyhEHzY5zFs0I4l5GEwAdj7lqbJ3J2KX44ZtVatrmVOwETwDgzjkIh1xVsHapbQwiVqA3Mx6sWMW7SpNHHluThnYZG-8OptCOzgwcYlDaZWqOAk1V78-p3yYqukxwOg05_lWa55MU4jxXgwNYUc5Z0-PI2wCCx_zXXzk1cFsFX7_qPhkUAU6oAPhT6_8L4QgkXQdU33T1aHYyoTgVkjcsglw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خداحافظی تلخ داریوش فرضیایی با پیکر مادرش
💔
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/akhbarefori/674833" target="_blank">📅 16:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674832">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
امید ملایی سردبیر ارشد خبرفوری: تضعیف رسانه‌های مؤثر، خواسته دشمنان ایران است. خبرفوری همواره خود را متعهد به قانون دانسته‌، اما انتظار داریم تمرکز اصلی بر مقابله با جریان‌هایی باشد که شبانه‌روز برای ناامید کردن مردم و تضعیف کشور تلاش می‌کنند. در جنگ رسانه‌ای،…</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/akhbarefori/674832" target="_blank">📅 15:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674830">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/310f040801.mp4?token=RmwVx81qFt2stioIQ-Xk35JBV28v-DlG0tqryvnwi_1vWLGaF-vU2wmGIV-c7xHKpn7gt8ULuhhDnhmvsPoxmq7EqEhN4VWvLyiwTw6-zc7yOsdO6iYRuUaExePhzJhXAPbwXJB2bXgjLpVxOLCVM7fx_SwZHgwyuTyaMiMjfR7zdDhG7JyzTX98LA0b3hrof3T1ZxgXyG_ySrMA5Sk1S0t1WJ4jXA2BkiMtiKv8akopnYQTYbwiEg5_GJDk0QVKsxvXuFO1CZBAKEdBiU-4E3JlsJTGOFTvgTPssrX8LaR5I9H4dB0NqkaHIuDbWIMLiA1Y4sXOg7GkoN0s0A5BoE7_kNtEhFH5WFVRU8evL6Umg2jDIdXPjsbEDJBut6Jl2l59zanp0YsXrvJOV5TAj73tQn9py5dUlLnZ2iAaiuLhj0Yk_YzZfQQnl_x8ABq0T-kDhhIcFY0d6PU-8kxFvems7UD0p_uGkAI8s9xj9XEAw94AmEXH44P6w3EirXjSUwxDXIrfd44pqdRnz-WO4eSaWvIR3-_SFEQqMixSAaEzFvFvo0KVuu7VGrOm_WOVPMffkHBlp0J-PNerINRBYBUck63A1J6tVr0I4wnae5l0_uYWJNzBHzpQL5D8Q9Bx_r9SFo_w77u1d41ho0KmKZem566_i1vp2Mrh6q8jS10" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/310f040801.mp4?token=RmwVx81qFt2stioIQ-Xk35JBV28v-DlG0tqryvnwi_1vWLGaF-vU2wmGIV-c7xHKpn7gt8ULuhhDnhmvsPoxmq7EqEhN4VWvLyiwTw6-zc7yOsdO6iYRuUaExePhzJhXAPbwXJB2bXgjLpVxOLCVM7fx_SwZHgwyuTyaMiMjfR7zdDhG7JyzTX98LA0b3hrof3T1ZxgXyG_ySrMA5Sk1S0t1WJ4jXA2BkiMtiKv8akopnYQTYbwiEg5_GJDk0QVKsxvXuFO1CZBAKEdBiU-4E3JlsJTGOFTvgTPssrX8LaR5I9H4dB0NqkaHIuDbWIMLiA1Y4sXOg7GkoN0s0A5BoE7_kNtEhFH5WFVRU8evL6Umg2jDIdXPjsbEDJBut6Jl2l59zanp0YsXrvJOV5TAj73tQn9py5dUlLnZ2iAaiuLhj0Yk_YzZfQQnl_x8ABq0T-kDhhIcFY0d6PU-8kxFvems7UD0p_uGkAI8s9xj9XEAw94AmEXH44P6w3EirXjSUwxDXIrfd44pqdRnz-WO4eSaWvIR3-_SFEQqMixSAaEzFvFvo0KVuu7VGrOm_WOVPMffkHBlp0J-PNerINRBYBUck63A1J6tVr0I4wnae5l0_uYWJNzBHzpQL5D8Q9Bx_r9SFo_w77u1d41ho0KmKZem566_i1vp2Mrh6q8jS10" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اطلاعیه شماره ۵۱: اقامتگاه نظامیان آمریکایی و چند جنگنده در اردن، سامانه پدافند هوایی پاتریوت، یک بالن جاسوسی و اقامتگاه تروریست‌های امریکایی در اربیل منهدم شدند
روابط عمومی سپاه پاسداران انقلاب اسلامی:
🔹
مردم عظیم الشان و فداکار ایران اسلامی؛ ایستادگی مثال‌زدنی شما هر روز حقیقت را در عالم پرفروغ‌تر و ظلم و استکبار را منزوی تر می‌کند. رزمندگان به پیروزی نهایی امیدوارتر و دشمنان بشریت را مایوس‌تر می‌نماید.
🔹
فرزندان غیرتمند شما در نیروی هوافضای سپاه در ادامه عملیات تنبیهی خود، در موج ۲۷ عملیات نصر۲ با رمز مبارک «یا اباصالح المهدی ادرکنی» با یک حمله کوبنده دیگر به پایگاه آمریکا در الازرق اردن، به چند جنگنده خسارات اساسی وارد آوردند و با در هم کوبیدن یک اقامتگاه نظامیان آمریکایی تعدادی از آنها را کشته و مجروح کردند.
🔹
رژیم آمریکای کودک‌کش، به ملت خود و دیگران در مورد تعداد کشته‌ها به وضوح دروغ می‌گوید، مراکز تحقیقاتی و رسانه‌ها را به تحقیق میدانی در این مورد دعوت می‌کنیم.
🔹
در عملیات غافلگیر کننده دیگر، رزمندگان اسلام یک سامانه پدافند هوایی پاتریوت و یک بالن جاسوسی رژیم کودک‌کش آمریکا در اربیل را منهدم و اقامتگاه تروریست‌های امریکایی را مورد هدف قرار دادند.
🔹
رژیم زورگو و غیرقانونی آمریکا در صورت ادامه شرارت با پاسخ های متفاوتی مواجه خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/akhbarefori/674830" target="_blank">📅 15:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674829">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxG89tApktt5GWVCPsdhZkwMBecUICa3yOJZXccQtkzw_A7KJDUj3-lUzNWs3u_kKqvfCaiDb5m2hH6488IfHfHVBOtI1jSUPqaUQweIn7gFiL749pkKewZsjCGbwqmOGun6PJw0FNTRSzvlTTF-r2vU1WRJpp6X-A6MJ8kM4s9cjtiP05MjqVabD4be-Xv0IMBloMbZ5LD8EFw8pavFgPh87ewfKO9odf7sn3m5KqBX4iQqqm3r9yS1yyjmfKod975D8OM6srZmRKYg9dxEQR_Efb5FPdkhszoVa-XDd5VeOCetv_Nu8x3nU9EfdICowsntLfbneEjRKbW_Yy_mwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وضعیت عجیب بازار استخدام سرایداران؛ اتباع افغان در اولویت استخدام مالکین!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/akhbarefori/674829" target="_blank">📅 15:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674828">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fddf870ff2.mp4?token=uF3PSSfQHBGao2pRZSwzbqX1Cd0CDNcE3klXx2tS5yF6mVfDUEWPxVCsSyXUunJXWUWYa-64qQBLs9BgupnbV9re33Rs2JoaH0a78OElrMwO8G0z7PlAOhemEEC4v4pISv8zzlCTDpTZgd2JtiC6N90YJmFDJWq2swKOIj-iy5XoaR_FkVyiRoJRya32eMG88-EXVA-VCrd_P-wCLtho6KXftRawVTuDAdWwNQarYFDYAMvkQXIrDLmhd53jVYW1y4Au9KarBU6Am8x5sT95rrdh-Fsvg5pr_3Ji8znzSc4BWeUJlB2bS3qTKjULFpGqTezmJYdqsNoDIO-CRGPtVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fddf870ff2.mp4?token=uF3PSSfQHBGao2pRZSwzbqX1Cd0CDNcE3klXx2tS5yF6mVfDUEWPxVCsSyXUunJXWUWYa-64qQBLs9BgupnbV9re33Rs2JoaH0a78OElrMwO8G0z7PlAOhemEEC4v4pISv8zzlCTDpTZgd2JtiC6N90YJmFDJWq2swKOIj-iy5XoaR_FkVyiRoJRya32eMG88-EXVA-VCrd_P-wCLtho6KXftRawVTuDAdWwNQarYFDYAMvkQXIrDLmhd53jVYW1y4Au9KarBU6Am8x5sT95rrdh-Fsvg5pr_3Ji8znzSc4BWeUJlB2bS3qTKjULFpGqTezmJYdqsNoDIO-CRGPtVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دستگاه میخ کوب دستی مدل (دارای باکس)-BPZ ویژه
با دستگاه میخ‌کوب دستی BPZ، چالش‌های نصب را پشت سر بگذارید!
دیگر نیازی به ابزارهای سنگین و پرهزینه نیست. دستگاه میخ‌کوب دستی BPZ به شما امکان می‌دهد تا میخ‌ها را به سرعت و با دقت روی سخت‌ترین سطوح مانند بتن، سیمان و حتی فولاد بکوبید.
ویژگی‌های کلیدی:
فولاد مقاوم سری و پلاستیک نشکن دسته
عملکرد عالی با میخ‌های تا 5 سانتی‌متر
طراحی ارگونومیک و ضد ضربه
باکس حمل برای نظم و جابجایی آسان
هر بسته شامل 5 تا 10 عدد میخ است.
🔴
قیمت 1,798,000 تومان
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/brief/41267/180124/</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/akhbarefori/674828" target="_blank">📅 15:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674827">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
تیزر قسمت یازدهم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای سید مجید غضنفری که در اثر تصادف شدید، ۲ ماه در کما به سر برده و با جدایی روح از جسم، مواردی از جمله حضور چهارده معصوم، عذاب چوپان دزد و حیله‌گر، فرزندان سقط شده‌اش که در عالم معنا زنده هستند و آبی که با نگاه سیراب می‌کند را در برزخ درک کرده و در نهایت با دستی که حضرت ابالفضل بر سرش نوازش می‌کند به دنیا بازمی‌گردد را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: سید مجید غضنفری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/akhbarefori/674827" target="_blank">📅 15:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674826">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
حادثه دلخراش برای شرکت‌کننده مردان آهنین
🔹
در جریان رقابت‌های برنامه مردان آهنین یکی از شرکت‌کنندگان هنگام تلاش برای رکوردزنی دچار پارگی شدید عضله پا شد؛ اتفاقی که باعث شد ورزشکار با شدت به عقب پرتاب شود و فضای مسابقه را در بهت فرو ببرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/akhbarefori/674826" target="_blank">📅 15:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674823">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
ثبت تصویر پرتاب استارشیپ از خاک مکزیک
🔹
پرتاب دوم استارشیپ، بزرگ‌ترین موشک شرکت اسپیس‌ایکس (۱۲۱ متری) متعلق به ایلان ماسک، از زاویه دید ناظران در خاک مکزیک به ثبت رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/akhbarefori/674823" target="_blank">📅 15:29 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
