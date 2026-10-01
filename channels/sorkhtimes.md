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
<img src="https://cdn4.telesco.pe/file/UtH2I92lfk5ugLHHd0UGRuJHNly02HUwNOlICNEIazy0WmodVyW1N0ZVPKzL5IiRh6T-85wQzjZ3_GmE78mU8hLn-ZRn_lF9OIpM2l6p2gCjiiEzsWmyBtP5_nlYH4ZtbknYMkt82dhCIXDpYVUZKSdOogMJyJt8tctnkRbESVdqdRx4LxT3NcT2afzZk4nSnpABycr20ZQrE6ZXYFd6MZDK5YgwCsOaEIf1wPe-sajipBzk2EE9ZB29nf4LBeekBG_n77ZzZksHzmrOoDb5TAGaY16qV28Y3XXae3V9pNNdUDzmYqDc8fjPPB3m-NZLAtDbIzwBtaaA0Go6yfzMng.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.4K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 02:47:57</div>
<hr>

<div class="tg-post" id="msg-140816">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g33l_jPqNtkf4MxXYmDygMv4T9TOa7E8fJLis52jns6FPl0Zzh2yGT-uYeLuT4hcIh56uzoL8-1AWu6fPI_AHDLRngu1uyQ0gG-kDJzEStzKweVEUUAHnTGjTRAipL03cRIjOiyNX45RLL3b4cM3JFAtWB4hEXA9MqVu200ArQVjhaizqzxGN7Kjlq8eO_BU9F-O6_mv1H0wZHHBtREfymtmmf5OX7nWVtYKRNAez5KKbIOO4uuMkI-APvd9MPInB-y3gOOo_vouQXp_fZ1mLhZ0iW5ABPtnRIZvhMN69FzYXMbqYhL9IFpGaYz5w3xihCpCR_d6HhL9U2LixXK9aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
یک شب پر از بازی‌های سنگین و دوئل‌های نزدیک؛ جایی که چند دیدار می‌تونن تا آخرین دقایق غیرقابل پیش‌بینی بمونن.
🔥
⚽️
از تقابل‌های پرریسک فرانسه با ایتالیا و بلژیک با ترکیه تا بازی‌های متعادل بوسنی با سوئد و مجارستان با گرجستان؛ کنداکتور فرداشب ترکیبی از مدعی‌های واضح و نبردهای کاملاً قابل پیش‌بینی‌ نبودن است. در سمت دیگر، اوکراین و لهستان روی کاغذ دست بالاتری دارند، اما فاصله‌ها آن‌قدر نیست که بازی را از قبل تمام‌شده بدانیم. ۶ بازی، یک ساعت مشترک؛ از اولین سوت تا آخرین دقیقه، شب فوتبال ادامه دارد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی بازیای فرداشب همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 978 · <a href="https://t.me/SorkhTimes/140816" target="_blank">📅 01:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140815">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9phN6VeVMtnberXPNa0YvZY2EUpKUVyW9UdAFR2PBLyWu8NwGFxn152rs4Q5qA3INgn65i_i_mdS6CAyuGjAv6x_zeLsKVPYdNQtc7g1ZTcM7Hf_rU67vzDir241T-ucTZKfCJPdk-tODL0J6pYolHgP-QDBYmyoAsgR8m9DeV1c2qWIGC7BmCCwjpBtJh8Us6PWpLUOE7ayid-a44vaZX48SNkk9QFql4vcRHApLkQmwk3cP3UQNOuTRpmEPnlleCS9wi-X8Bn5mjowo3Ca1tgutTQEuZnHmvPkaDYfPsnw0HlIBdL2Q5rvX53IZ9V4kr_RqEYJnC-qPMMBa3OpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
گفته میشه که پویا اسمی ۱۶ساله یکی از استعداد های جدید و درخشان پرسپولیس هستش و تارتار میخواد بهش بازی بده و مثل زارع تو گل‌گهر بهش بها بده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/SorkhTimes/140815" target="_blank">📅 01:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140814">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDBIlFnAVZXMhDLxYsVzz12hQj2Z6colSCtqdustbtZDP9rZ2T3zBhw6knDAACWvcG1VjbiyYn2pEUiEpKUiTeGEefmqD3Q4nza4UFPKtHEzbJZ8Su1JwoVmMW4kFOt2xZF3-Z-KU6xQ4ea7JvaNQwfrfycfGy4oE1OeRNc03xahu883jkDVv9nsVKW8RIW0diwp6RqGAYEVdhUHAwF6y71uJ3nf8s-S7HZgX170QZE1Jwclr0_Ssosh3vj91D_HGXceTPfPCrhx4g06UeXYu-LKUPqKkSK7taxwhpP3gsHyx3i-eA8C3zcON-kH2obd6prVclgcJnJ4ej93p1UFTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
پرسپولیس فردا به مصاف گل‌گهر می‌رود
🗣
تیم فوتبال پرسپولیس در آخرین دیدار تدارکاتی خود پیش از آغاز دوباره رقابت‌های لیگ، فردا (جمعه) پشت درهای بسته به مصاف گل‌گهر سیرجان خواهد رفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/SorkhTimes/140814" target="_blank">📅 01:01 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140813">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
رامین رضاییان 2 ماه به دلیل مصدومیت از میادین دور خواهد بود.و پنج بازی آینده فولاد و از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/SorkhTimes/140813" target="_blank">📅 00:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140812">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEeQdR06QIDKOvI634J25miKSlNjdb_mfi2T4R9g6Iz0ZQUVS1ujl0xzZmO5-jTWNihKEqsWbdErNiq6t-glRDe9upGrJZ_aL0DvAN50nVXqCABvltzQbzjHG_05zSta2-DGZhpMPnsBozUphikfqazJZr6gtFY2kHNUaS7ShgV5VqM_Z5FDnkSAHiaIn2Uskf67AF-3CKbQdiqQEzNAmxUCKacrLCsg3zyN98A7MhEb7FuHsg3DFOYxe66yEAX4IwuzF-udHIQZC80MaxiRHx_M6wM5eXqcAWzaMtfcNj72PwYImEtmA8eU2T4AZv9gXF1LhSBuHoDd3gxDumYszQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بازگشت ملی پوشان پرسپولیس به تمرینات
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/SorkhTimes/140812" target="_blank">📅 23:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140811">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
✅
✅
فشار شدید امریکا علیه ایران
✔️
✔️
امارات، ترکمنستان و تاجیکستان ۳ کشور جدیدی هستند که حریم هوایی خودشون رو به روی هواپیماهای ایرانی تحریم کردند !
❌
مکزیک برزیل و بقیه کشور ها هم رسما تحریم کردند   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/SorkhTimes/140811" target="_blank">📅 23:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140810">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
❌
جنجال قرارداد گرا در رسانه‌های مجارستانی
🔺
رسانه‌های مجارستانی با اشاره به غیبت گرا در ۶ بازی اول پرسپولیس، دلیلش رو مصدومیت پاشنه عنوان کردن و درباره قرارداد و دستمزدش هم نوشتن. همچنین مدعی شدن پرسپولیس دنبال پایان همکاری با این بازیکنه و اختلافی هم بر…</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SorkhTimes/140810" target="_blank">📅 22:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140809">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">⭕️
⭕️
ترامپ:
🟢
اکنون باید تصمیمی بگیرم: یا ایران توافق را امضا می‌کند، یا دیگر وجود نخواهد داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/140809" target="_blank">📅 21:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140808">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
❌
❌
❌
ادعای جنجالی حسن روشن درباره ساپینتو
⬇
حسن روشن، پیشکسوت استقلال، مدعی شد در دوران حضور ساپینتو در استقلال، اتفاقاتی در اردوهای تیم(دختر بازی) و محل اقامت او رخ داده که حاشیه‌های زیادی ایجاد کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SorkhTimes/140808" target="_blank">📅 21:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140807">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
❌
❌
خبرنگار: شما ایرانی‌هایی که آمریکا باهاشون در ارتباطه رو «دیوانه» خطاب می‌کنید؛ چطور میشه با آدم‌های دیوانه به توافق رسید؟
❌
❌
🇺🇸
ترامپ: شاید منفجرشون کنیم. باید بین این دو تصمیم بگیریم؛ یا منفجرشون می‌کنیم یا به توافق می‌رسیم. زمانش که برسه، تصمیم می‌گیریم.…</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SorkhTimes/140807" target="_blank">📅 21:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140806">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
🟡
🔴
حسن روشن:
🤔
🤔
ساپینتو اکنون بهانه دیگری پیدا نکرده و روی داوری تمرکز کرده است. ساپینتو یک مربی درجه سه است. صریح می‌گویم روی آدان در دربی نمی‌توان حساب کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/140806" target="_blank">📅 21:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140805">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
یاسر آسانی: رامین رضاییان کسی بود یک دقیقه بعد تمرین تمام اتفاقات رو لو میداد و همه میفهمیدن و ساپینتو برای همین لج کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SorkhTimes/140805" target="_blank">📅 21:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140804">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🤩
✅
هفته‌هشتم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
صنعت نفت آبادان
🇮🇷
🗓
تاریخ جمعه ۱۷ مهر
⏰
ساعت ۱۷
🏟
میزبان شهرقدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/140804" target="_blank">📅 21:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140803">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
هاشم نژاد به تمرینات تراکتور برگشت و برای بازی مقابل استقلال اماده هست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SorkhTimes/140803" target="_blank">📅 21:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140802">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXqelgtsIGPVR5qt1eF7xwJ8NIQ5RcsUxdyepnPykuafJ9ZLsMRIOJ3AM2sYZ72fHxNlhxlvEDJHAZRQys-PKkAPxA-rkJmgZTb-q4lnXvzXZCgivpM1ipCcFKrgn3TkhEtZX-FlXH_0x8rzahJP6XJ3fC1ORNs-SdAmu35MoMWFM7z6fJtJoBcVQVJcDwccabmrnHyjmW_1ZMiKy3iS3AvX0vIsb5x1cAB4jQWsRD91NiBvUBbP9MgixZdPN4xwAulXuhBwNg7m2FbEaTJHgWu0PedXu6eRVuI-0MG9nkKqK3-LBfLDGpscw_6ycxTI2I5zcmCDGkz8YGz6R9p4qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نبرد شمال و جنوب اروپا در یک جدال سنگین امشب در پارکن!
🔥
⚡️
[
دانمارک
🇩🇰
🆚
🇵🇹
پرتغال
]
⚽️
دانمارک بعد از برد ۲-۰ مقابل ولز با اعتمادبه‌نفس بیشتری وارد بازی می‌شود و در پارکن هم معمولاً تیم سختی برای حریف است؛ پرتغال اما با ۶ امتیاز صدرنشین گروه است و دو برد متوالی داشته. نکته مهم امشب غیبت کریس رونالدو است؛ او اردوی پرتغال را ترک کرده و برونو فرناندز هم با مشکل جسمانی روبه‌روست. در مقابل، دانمارک روی هویلوند، دامسگارد حساب می‌کند.
سناریوی محتمل: بازی نزدیک و پرموقعیت، با شانس گلزنی دو طرف.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
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
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SorkhTimes/140802" target="_blank">📅 21:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140801">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
نایب رئیس فدراسیون فوتبال پرتغال: رونالدو دیگه به تیم ملی برنمیگرده  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/140801" target="_blank">📅 18:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140800">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2Y1j0OJbvgeqdNqhV0taUXPNjzo3Pg81srVHz1Tjp5g841mg1akQUqoxsXBX_tzo5-yhD--b8ePiehyE0jLQc_txZBjyXxhMUaVohIRYBwMhASDWOnzFIY71_w6yAcUWU35XadX872zruhrBh43p9PkVjWjtbKf_OGZeCtpq7aAuuAfUCtkl1BdBW-L-ggBz5MJ__WZuUaHAZHLv0m-I5wgtN7lTDWjWJAU0MEPVq1eHbHqppgy2o5CeXtL-8AdYdYkVhnd8LRPD-QANPtcvYiYbRnAJYdpJIP41obwJF0fjKesVrGrTG5DedEd-kiJllJraxqqClqquN72nbuLoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علی علیپور دویدن را آغاز کرده و احتمال حضورش مقابل صنعت نفت وجود داره/ورزش‌سه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/140800" target="_blank">📅 18:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140799">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lChtiS53vtJChmNQCON8durcNFYeSkxvmd2vrWO2xvraUPW-aucDzQRZEAVrnYZy9afqrc5h48JaYtiSUJFeK67L7Y-GcZ4HZkro5yNkRqE8SSY9hvF2B0A0XpGSRp3rTde3vyJiaKUdu-wIbyfYxa75JjtQEtmJZJrJroqgPjrvy2HJTPolamLsNPAlKTVyAuFa6usxhX503K62DTfBr7YYf_16pYqGA8-JpFxW-11etzT6BgARUCxEei7WJyvvkckRZdWeFuoOnfP4-z21B6__G_UYY9PkAGw5ePNmhyNsGVFDj3efFf-EzVVC4Xa4YrDnqO2BHj2v9C9rCKK4Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
گویا بازی دوستانه سلحشوران تیم ملی برابر گینه بیسائو به دلیل محدودیت‌های پروازی لغو شده است. به این ترتیب سوژه خنده سوم این فیفادی از دست رفت!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/140799" target="_blank">📅 18:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140798">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔄
🔄
هوشنگ نصیرزاده: پرسپولیس با شکایت از آسانی به CAS وقت خود را تلف می‌کند هیچ سندی علیه آسانی وجود ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/140798" target="_blank">📅 18:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140797">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4PtnYaYnsaV9g71OpMmlHZAUdkjO6j5JMcKi1lWy-2qrzxhjTLvoKJ8ilT5bxuycCwCHNTSPWfxXCmQg-ZceMOiC2_y7mm6Z1HiBu1yWmejw4wf2dXWlX_TPPP3ol4PZ75ikxiVk8SOpHSEyJxi7ED-a6azX-0AkssVx9sPlCo40VfljB5lnBc5wWkP-B0fdhUmJ9cSlrihEch8gc91GowvjExb_IvSvxlkX-S-OFhpbQTKuhFQCbLCSAEQUMmwnWjr-SyjwdeIJczjPMT2xLQO2Wu2X6VdrNzQ6Q4_Jjp-_czoWeMdB1DiD1H5FLFBTCDHORz7MpS_XobFD1VvGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
ایجنت دنیس اکرت در تلاشه که این بازیکن رو فرو کنه به یکی از تیم‌های ایرانی
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/140797" target="_blank">📅 18:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140796">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfgWwQLICTcjQmmXO9fmcNh-6NSA9-p1Jm9Z8eP6F-rbvyq_NmXaO3R1VZJV2cqtzMd7gNitMOCiPurdY3-qh8QpBMS8KmB7mNlQY50m7GwProOa2tTfmScwHMlf9BcppuicStq0d3R77-7z1nD2RVjrIjL3vk9CyOiyrXDE7LrfwPjA0wQMJnR_77AIllCWxNi_nbXzxcl6GwyWcuAtXGkustNwm0BR0dopIgbRmcpOW0_Lyg57hIs2uPMQQIejr6ck6YQuTMdQGDLN-3vk9SNMAYOsjJfEsfs4wUvrqu-JrYkXShgXQyYiyajSI9hFniOtjDy2CIl5mUyAwlKXCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نایب رئیس فدراسیون فوتبال پرتغال: رونالدو دیگه به تیم ملی برنمیگرده
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/140796" target="_blank">📅 16:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140795">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jD2VbV6R-8Lak9X4tLiZfRa1gSm--GT1kk-9933uLJGCM1lIC5W2tIrNQsI_0l2QMIv0D_79vcAOfafjaB0uBmvgXgNLCxArZMGxmDS-ZSGbpA87HZR55qRU9XkBAzJOCmiIxYURi3pqMsPHxNJMI-DrgY4xobd9eBakANkviAIaHzVBF6mNhW9jXQRyC9oPiZCkpiAYzOT2pNDHlPByp8VyCf7d_wkQeT8rNhYNqMSktOIwYO011QRe3C7o4P3QZUHM6wFeCC6rUgl9pu0cK1JVn04tnmPdS78Q9qkizK1eNBTOTnlzBL95lMG4MzjFGBdfblbhi-0hlZm9Wl7i3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
دیشب در بازی دوستانه بین کونیا اسپور و تیم ملی فلسطین بازی رو دقیقه 89:59 متوقف کردند و گفتن بقیه بازی رو وقتی انجام میدیم که فلسطین آزاد بشه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/140795" target="_blank">📅 16:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140794">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🤩
✅
هفته‌هشتم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
صنعت نفت آبادان
🇮🇷
🗓
تاریخ جمعه ۱۷ مهر
⏰
ساعت ۱۷
🏟
میزبان شهرقدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SorkhTimes/140794" target="_blank">📅 16:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140793">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KO4elTNkFyB6HE9Xoj4P3ezYMY3SU6XkaySk7YdQGQpklcau9kpr8Vcao2PqpOHEFvl27xD8tDgaylh8Vwq_bpkYK8J-d2PPJUTt2DeeNTvHhRBIBCpMgUAY09K-dgD3onMoeTVr1SYMDw6jPIER1KpkwfiAGF3zkN9c0ct3rTCVr2WXbbjr8SkJwEaooO8qRi8XZzHPQTYezC2dRv333wLO65w229v_0kaM_MQWHUjWjAX45-jDZnu9xe81c4PI9aL7Ns7xe01HcJMfNKbXiST1hKVEC1cJsQj3bfnUmQ_83N3z8Lg4nvRNbUaty28PJFcF1K_n-TIFXkUXfXB6kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🔴
در یازدهمین سالگرد درگذشت هادی نوروزی کاپیتان فقید پرسپولیس، یاد و خاطر این بازیکن در دیدار امید پرسپولیس و سیاه جامگان زنده نگه داشته شد.
🔺
پیراهن شماره ۲۴ هادی نوروزی در دستان هانی نوروزی فرزند هادی و بازیکن تیم امید پرسپولیس در عکس تیمی پیش از بازی.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SorkhTimes/140793" target="_blank">📅 16:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140792">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g03-1NLnHx-OR2UQQ5BDMMNkvNJllatVUUgpsSQfgffsg6ysTAR5yDfNSHtYE8a8oFIGDv1jiZDEid3OXRSIxOP6-noxuIrnMk8D_Az0t9p4A0XjJ5M0YFkMmCF8yCQkYWjB62m-0igYGvqb4dqlu2wcn0SG_Pl1WCgELO6dWX_SjILCQ52eNGYTreCcK4J3r9z4Tgplsl01cz8gnwpbPDI7GUjGDbWt3whmBldA_Vlg5eGZ4JC5BJAslEWXQZMzfkZC3BibU6LoxbF2DjNOb3rmjtq60g4F20brtYpyRWgILdsVi2q8WpmXW-jKz5E1MA3HvNbA8f7d-sUGLZPrwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
Germany -
❤️
Serbia
⏰
Tonight 22:15
🏟
Allianz Arena
🇪🇺
آلمان بعد از ۱-۱ مقابل هلند و شکست ۰-۱ برابر یونان هنوز زیر نظر کلوپ به برد نرسیده و مهم‌ترین مشکلش تبدیل مالکیت و برتری میدانی به موقعیت‌های باکیفیت است. صربستان هم شرایط خوبی ندارد؛ در دو بازی ابتدایی لیگ ملت‌ها مقابل یونان و هلند شکست خورده و با صفر امتیاز قعرنشین گروه است. از نظر تاکتیکی، انتظار می‌رود صربستان عقب‌تر بازی کند و فضای کمی بین خطوط بدهد؛ خود کلوپ هم روی همین موضوع تأکید کرده و گفته شکستن دفاع فشرده برای آلمان چالش اصلی خواهد بود.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/140792" target="_blank">📅 15:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140791">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">⭕️
⭕️
⭕️
خبرورزشی: مرغ حدادی یه پا داره بردن شکایت آسانی به Cas همین و تمام
⭕️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/140791" target="_blank">📅 14:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140790">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✅
✅
✅
تیوی بیفوما که بدلیل مسائل سیاسی دعوت تیم ملی کنگو را رد کرده بود دقایقی پیش برای حضور در تمرینات پرسپولیس وارد ایران شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/140790" target="_blank">📅 14:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140789">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
🇬🇭
کارلوس کی روش بعد از باخت خانگی ۴-۲ غنا جلو گامبیا سیکش از تیم ملی غنا زده شد و باید دنبال تیم ملی جدید بگرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/140789" target="_blank">📅 13:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140788">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
❌
❌
❌
دراگان اسکوچیچ از طریق واسطه‌های نزدیک به فدراسیون فوتبال، برای بازگشت به نیمکت تیم ملی و هدایت مجدد ملی‌پوشان اعلام آمادگی کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/140788" target="_blank">📅 13:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140787">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🗣
سرگیف و بیفوما هردو در تمرینات تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/140787" target="_blank">📅 13:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140786">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
❌
قطبی یک قدم تا بازگشت به فوتبال ایران؛ مذاکره ادامه دارد  •
✔️
✔️
مدیر برنامه افشین قطبی اعلام کرد مذاکرات با فدراسیون فوتبال ادامه دارد و دو طرف در حال توافق بر سر شروط همکاری هستند. طبق مذاکرات انجام‌شده، قطبی قرار است مدیر فنی تیم‌های پایه و سرمربی تیم امید…</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/140786" target="_blank">📅 13:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140785">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✅
محمد نصرتی درباره حضور دنیس اکرت در جام جهانی: آقای قلعه‌نویی، با دعوت از اکرت در حق یکسری بازیکن جوان اجحاف کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/140785" target="_blank">📅 13:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140784">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
❌
❌
هفته هشتم لیگ برتر در آستانه تعویق!
✔️
✔️
در صورت قطعی شدن برگزاری سومین دیدار دوستانه تیم ملی در فیفادی پیش‌رو و انجام این بازی در ترکیه، احتمال تعویق برخی مسابقات هفته هشتم لیگ برتر وجود دارد.
✔️
✔️
در این صورت، دیدار حساس استقلال و تراکتور نیز ممکن است…</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/140784" target="_blank">📅 12:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140783">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">⭕️
فووووووووووووووری
❌
محمد مهدی محبی مصدوم نشده و اصلا مصدوم نیست. امیر قلعه نویی دیشب با هماهنگی قبلی برای توجیه شکست های پیاپی به محبی ستاره تیمش اعلام کرده باید تا دقیقه ۳۰ مصدوم بشه و تعویض بشه تا فشار رسانه ها کمتر بشه و این یک حربه از سوی قلعه نویی…</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/140783" target="_blank">📅 12:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140782">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
❌
میلاد سورگی: از باشگاه بزرگ پرسپولیس ممنونم که باعث شد من به فوتبال معرفی شوم و به تیم ملی برسم. امیدوارم روزی به عنوان ستاره به پرسپولیس برگردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/140782" target="_blank">📅 11:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140781">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🗞
لیست بازیکنانی که قلعه‌نویی ازشون ناراضیه و شاید دیگه دعوت نکنه:
❌
محمدمهدی محبی
❌
صالح حردانی
❌
سامان فلاح
❌
احسان حاج‌صفی
❌
حسین حسینی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/140781" target="_blank">📅 09:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140780">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
❌
خط خوردگان بزرگ لیست
😀
محمدحسین کنعانی‌زاگان
😀
روزبه چشمی
😀
شهریار مغانلو
😀
هادی حبیبی‌نژاد
😀
علی علیپور   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140780" target="_blank">📅 09:26 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140779">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
❌
پیگیری‌ها از مسئولان باشگاه پرسپولیس نشان می‌دهد که هیچ پیشنهاد رسمی از سوی باشگاه‌های خارجی، چه از قطر و چه از سایر کشورها، برای جذب محمد عمری به باشگاه پرسپولیس ارائه نشده است و بحث جدایی این بازیکن صحت ندارد. / فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/140779" target="_blank">📅 09:12 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140778">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
یازده سال گذشت
❌
روحت شاد؛ هادی جان 24 ابدی  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/140778" target="_blank">📅 09:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140777">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
❌
❌
❌
دراگان اسکوچیچ از طریق واسطه‌های نزدیک به فدراسیون فوتبال، برای بازگشت به نیمکت تیم ملی و هدایت مجدد ملی‌پوشان اعلام آمادگی کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/140777" target="_blank">📅 09:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140776">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
یه سری شایعات از بازگشت اسکوچیچ به تیم ملی در حال انتشاره که نه تایید می‌کنیم و نه رد می‌کنیم./فوتبال برتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/140776" target="_blank">📅 09:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140775">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AT37vy77d6MaUrIwBEWpOHwf2Z1Xe1uZ2BI-rkfFA1RA3Q-BRoUbNy-7tFry03G31lLX-MSU9Ki1Z3z3LkAAfUtBV7YbN0vYXcMPidF0oJlAj5IFpD2kfsCeF-Eq_KqrBGAiWf8UydjZEeD4bFmbGtS8irFZKdghVGHnoxVBO_SgfYA6dm4ekWA63PVJ1Y9nGKpGV1Kg0qA4F6nxTN7-v7pJ3LkEULBlT--EXLSB0lFds7Nt6o5zMgZd18Uf8Hv_4Oj0O5bt5Trs-dP4FqwWNS90JiZ_3Z9TBil29TeFIpA6sXHIf1GVGUYzeKHFcrDuMqXmaCOeKknXq_6UNeRoUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/140775" target="_blank">📅 08:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140774">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4m6dYDFOcTYTi0euCQUmFFvRfT3dSojg21Ptq8Fp4w4XEbXbmT36FES6jLDg3szQ5q3408ZEzfgyVpPXZR6TSbo-N8zz4V03f7haQnLdtD7fI8mfkUrnAMweFGvip1Biv-EiarWxgl5ZboeLPf1sXJAq3jxkWt8kVs8DkYPGeR5Y0n_ZsoeJBoHBZ2C3hLsvU9Oy9qzygyVMAos9bRhiddHLP2kIKwUYe_6wJtGzs2Ge_sfFXIU4ioVlTVgQriuOIjZO3QpXiNBPZutdEhfyydfpNGFzfNFBZKnPGp8IOna1Ko8wlhHv4I66X4xr6s3nfYSTdoCS-Su5mGfdUZB2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
شبِ سنگین فوتبال؛ چند تقابل با پتانسیل غافلگیری
🔥
⚡️
⚽️
ژاپن و اکوادور شروع‌کننده بازی‌های فردا؛ کنداکتور فرداشب پر از تضادِ ضریب و احتماله؛ جایی که بعضی انتخاب‌ها از همان ابتدا جهت مشخصی دارند و بعضی‌ها تا دقیقه آخر قابل پیش‌بینی نیستند. آلمان و نروژ روی کاغذ دست بالاتر را دارند؛ پرتغال، هلند و اتریش اما وارد بازی‌هایی می‌شوند که یک اتفاق می‌تواند همه‌چیز را جابه‌جا کند. فرداشب، عددها حرف می‌زنند؛ زمین تصمیم می‌گیرد.
📌
مسابقات را فقط تماشا نکن؛ همین حالا وارد مینی‌اپ وینکوبت شو و با اولین شارژ خود و دریافت ۱۰٪ بونوس ویژه این دیدار‌هارو رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/140774" target="_blank">📅 01:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140773">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
❌
🚨
فوری/ ترامپ : به زودی اتفاقات مهمی درمورد ایران خواهد افتاد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/140773" target="_blank">📅 01:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140772">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✔️
✔️
فرهیختگان : دقیقه ۲۷ قلعه‌نویی خواسته حاج صفی بیاد تو بازی تا رکورددار تیم ملی بشه و به محبی گفته یجوری بیوفت زمین که انگار مصدوم شدی وگرنه مصدوم نیست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140772" target="_blank">📅 00:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140771">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
تعویض زودهنگام محبی، به دلیل مصدومیت که احسان حاج صفی جای او را می‌گیرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140771" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140770">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPG0EQ30enhmpOYVKX2loIUYeHHmF2Xf5EJMo77XQiqslkfmxuwEPvrf4r7P4b8usGMXnwS_Zks-5M7d2WIpKP_G4YsSLUWR99Xdduu4zECjPJdBC_twKWhv6sibBu7srVZDe0EMJisdVbyIzJyFxb2HeZDP2PdTz7-5-acRaXIv8eQ8mh4Sddf8znhKxSfdFALQuftzdXrrd7L6KMXU-5WM7TCkrLnING-lCG0t4SL6UpEpQbypKrXXX1Uquxft2VQlvr2amouR5dID8f1MQfIKrpPnDGocP3J4O5bFZ-mDK7qBCl0UYW0ECfqv3WmeoL9ncduvgm_M77pKbpDX9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
عالیشاه در خانه
❌
دیدار تدارکاتی روز جمعه میان پرسپولیس و گل‌گهر در ورزشگاه شهید کاظمی فرصت خوبی برای قدردانی از کاپیتان سابق پرسپولیس است
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140770" target="_blank">📅 23:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140769">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
لحظه گل ثانیه پایانی جوانان پرسپولیس مقابل پارسیان توسط محمدامین قرنجیک
👍
👍
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/140769" target="_blank">📅 23:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140768">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c458bfa09b.mp4?token=jYQmZbehCFduTS_Voxc1pmMnw1HWtd0fMAB9BHwuO-KZiskp1oqjP-BsMZkh6gZEYRdGpy1_5d4hikvkLhd03wnfhEX2Qxalt5dVs-JGFnssYYzEVpp0bqJXldxrjF2TrNVojhSta1GpU9xOdArk2IEdG_3_qp8yjN6lN0kHkrAhM7WRg1-a3sJOyBCOI6M08CRC-ghj-43CAvjv0-ewMz42Z4h7ajO2Qih1QpP7tSP0EkH33SA4Ll05wUBy0j_DvVmp5W8PvDtPPABvSy0nSpJ2YGF9GGe3enVmeSObn1i4QIOBD1eIDmDZJ9PEE3TpAaKVYUDHla46nwqD7szdpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c458bfa09b.mp4?token=jYQmZbehCFduTS_Voxc1pmMnw1HWtd0fMAB9BHwuO-KZiskp1oqjP-BsMZkh6gZEYRdGpy1_5d4hikvkLhd03wnfhEX2Qxalt5dVs-JGFnssYYzEVpp0bqJXldxrjF2TrNVojhSta1GpU9xOdArk2IEdG_3_qp8yjN6lN0kHkrAhM7WRg1-a3sJOyBCOI6M08CRC-ghj-43CAvjv0-ewMz42Z4h7ajO2Qih1QpP7tSP0EkH33SA4Ll05wUBy0j_DvVmp5W8PvDtPPABvSy0nSpJ2YGF9GGe3enVmeSObn1i4QIOBD1eIDmDZJ9PEE3TpAaKVYUDHla46nwqD7szdpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بالاخره گداوند رو‌ بردن سربازی
😂
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/140768" target="_blank">📅 23:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140767">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ca8ba9d21.mp4?token=ZH_4fr99KSD0Td0GshJ1eybqbuSaeleFVflxqDj1j87yM49N4xxVSPRxC-bMjDUOXu0ntfLISJyC2Se_KI0EqfbMtu8KpnZvhhlU-nwNZFT44WN2wMR1Kixdk0bWSrG2ve0auiraFslLH_V2GlTDH-g7x5yxu6GCkh3bnf0gqL0BJf2MK_7CY2OLKkXSjmowXk49qAxiPDyPlER3ctRh7vwebNshQp7G2UpNOw4yimzDMOiqVXn3UTsRO_d0s2iwo2sBcM2WBHCiKuM8kM9O4qxMOor9tQL4l6pkHkhVIVuium3I8eSir0cuw1UaaAeW-7-ogQALgLRua4CsN3lVPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ca8ba9d21.mp4?token=ZH_4fr99KSD0Td0GshJ1eybqbuSaeleFVflxqDj1j87yM49N4xxVSPRxC-bMjDUOXu0ntfLISJyC2Se_KI0EqfbMtu8KpnZvhhlU-nwNZFT44WN2wMR1Kixdk0bWSrG2ve0auiraFslLH_V2GlTDH-g7x5yxu6GCkh3bnf0gqL0BJf2MK_7CY2OLKkXSjmowXk49qAxiPDyPlER3ctRh7vwebNshQp7G2UpNOw4yimzDMOiqVXn3UTsRO_d0s2iwo2sBcM2WBHCiKuM8kM9O4qxMOor9tQL4l6pkHkhVIVuium3I8eSir0cuw1UaaAeW-7-ogQALgLRua4CsN3lVPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
دلداری خیابانی به بیرانوند قبل خدمت رفتن
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/140767" target="_blank">📅 23:30 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140766">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ux4IzdCdbZbeP_Ocvy3vNCUxRpaGqSXkaI5xPERrOn5M9HuH811HCrYmPasOYYgyVSIQ0YZRpHSzBs5dt2qhv7tyKZJaRDCoscim6lJ_jeEz-VCocZtZnRcqDq3QhlzYDSgJ1FlQf69eZ2TgxA47CZN_UOLXy760t_BcThu3v-Q8_P0QO56BD3XUMg33MvtdHRUajxTnTxYQDNzqOpadMAwmmftL2toSNEUTZtOlUI63XdFCr8iP__QNXhP0RnXx3ITqXYLq9EEpBM_yT6CGyubYjSWvSJdS4emqDCGt8XB91mW11Eg3EphOPO9oo8AsCE8k0mtswFl3TmG1nK-inA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🤍
قلعه‌نویی: اشتباهات و نتایج اخیر رو می‌پذیرم و مسئولیت فنی تیم با من است. برنامه تیم رو دوباره بررسی می‌کنیم و در انتخاب بازیکنان، تاکتیک و آماده‌‌‌سازی تغییراتی میدیم.
⚪
می‌خواهم تیم ملی رو حتی بهتر از قبل بسازم و از مردم می‌خواهم فرصت بدن انتقادها رو می‌پذیرم اما تسلیم نمیشم!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/140766" target="_blank">📅 23:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140765">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqbP5ShzVNtJJsW0_6NFcevyZFrmgl02iHSz6l90Y669PNqitdUepYjfJETPpQEzeN4Y-xF3ZNVusg2wqnrp39ch4QX8sAtuMRFka6q9efAo6O9piIShzj7TBea9pjhaKNZfGSTNtOTA8s91KQfnpcpbmMxyh1qCU4-1mthdSdQar4vxvNpSc47lCpC5jbB5TyncZX7R7-Q-4mHJQj0HDvnTK-hKZf-hFxhELGnfeUIZUh1fs3RqIO0xpTVibIkcxF8T-VanRAn8qXcuQDfcHuoBB7gTPJ6vueqNeah_nDm2ZDp12xwABc5jbDaLVYI-8GEHv2hliU1bFS2EUNrFfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
یازده سال گذشت
❌
روحت شاد؛ هادی جان 24 ابدی
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/140765" target="_blank">📅 23:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140764">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✔️
✔️
کریستیانو رونالدو امروز برای سومین روز متوالی در تمرین تیم ملی پرتغال حاضر نشد و طبق گزارش رسانه‌های پرتغالی و اسپانیایی، اردوی تیم را ترک کرده است. این اتفاق پس از اظهارات ژسوس درباره غیبت رونالدو مقابل دانمارک رخ داده و برخی رسانه‌ها احتمال بازگشت او…</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140764" target="_blank">📅 22:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140763">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
❌
🚨
فوری/ ترامپ : به زودی اتفاقات مهمی درمورد ایران خواهد افتاد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/140763" target="_blank">📅 21:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140762">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامپ: جمهوری اسلامی‌ هیچ پولی براش نمونده؛ برای همین فشار آورده که توافق کنه و رفع محاصره بشه. وگرنه چه نیازی به توافق دارن که پیشنهاد میفرستن؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/140762" target="_blank">📅 21:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140761">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
🇵🇹
👤
رونالدو اردوی پرتغال را ترک کرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/140761" target="_blank">📅 21:39 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140760">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJCoq42rF3Rk9QsBKEAeevpdWAAVLBXrItADSyf-Y188qF2NUaBGNTVUAf4iHDjdFVWGkRpRwKWB7_ptarvJrs8XQymJR9zZ-GSomCy7CESF6N5wqflzQPm3ZC0aiekRhFlqV3tAwt9J9q1ilTZy52SavcyHP349Yknf9L4_w19wGqOpqfSA3X1feGULR1trvIg2gOtPCEaLx6VaNJGam_ofhlp_D0xl6cqOk8OvbHex2pNK_Myxr3bplqroDtynChngWm94CgCi7QcTn_iLZh1zwPuEau767swtxbaYWzI5Nk_niEbTUhPCT-UDX7LwefTrdsapMaQKzbeXdc3c-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇵🇹
👤
رونالدو اردوی پرتغال را ترک کرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTime
s</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/140760" target="_blank">📅 21:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140759">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SloJelunsXZyyAIrZ6KaQJopOVlFpmI1np7vAhtRFmNNipRulntk5hGLS5UgeBx1n6poakWsiCqii56zy90umN1V0fdMNfsSZTDuCAHzm0Fdrb88Kc4rxvYgjgNLwJ8Huyde-T9f5uotqnCMan1SSiwzQ3jUVjkMDZG_TFrgZdcDCUzEA5zh-eFmJBwBTrjusjKyzQbbNxqu24qzTD_uOJHvA-5gHsza_5kLh5a1udcU7jVYJifS5933kxztv-IO853hM9s0NvgdFsBD4UoOT-zN1lbSG4irtFMZ5h7_1RQFiVqz_aIFZQ3DW0lMAScWsDj_pkoPkJS4XavbLCiYUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نزول فوتبال ایران به رده ۲۳ جهان
▫️
تیم ملی فوتبال ایران با شکست مقابل ازبکستان و روسیه، در جدیدترین رده‌بندی فیفا یک پله سقوط کرد و به رتبه بیست‌وسوم جهان رسید؛ جایگاهی که در سه سال اخیر بی‌سابقه بوده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140759" target="_blank">📅 21:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140758">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJCkXSEJUdNqU7ZQamyP80118jox-WPOc45ROkFVentyUgJPXxo_Q6Zp3Ok74NY6Sl0gOLhGA2VTTzowqx-to-MG8WwxFBTHDDDiI_NVzks-pcLo7sT835uWLUcKaIuwyKSLkvRTn870PG2kXcQ6xxPy5CCtFELK6oBqvTf4U-ggwV8scqDh4V-UWwcSMxEEu16fWf430kiI0uhO-KRCsD1VlTY1KHpI2SnvTf3YsX6P-CRPMRepwARDaZWVG5NZCVwaGiR7BchQP6J1UD2uo-QYqnuqAMpyU5zFOj5156G1prOq4zWnEb0OxqftB8BMzoKglIn51JZ_V42lPg0HMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🩸
لیست مصدومان باشگاه
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/140758" target="_blank">📅 21:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140757">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
❌
مذاکرات مدیران باشگاه پرسپولیس برای جذب فرهان جعفری ستاره ملوان ادامه دارد و اتفاق خاصی رخ ندهد این ستاره به زودی راهی پرسپولیس خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/140757" target="_blank">📅 21:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140756">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKK0HvL4SFWvKKUSveDagqVfQ2FsbDbGsrWShD4jgobkBFQE1aoEZjfvjo2zIQXJrscTZj6CSCGqCvImnmxfZlZRu80bDwJSKyzLQLbf2Bm5KNAODqgSIVMNZ8BAvkKUgZ3M_GeWUPAqsvqDS9sKQNZR6N3fIw32HVR24at4P4TkMurV41hsOMIQBkibyHsUz3Nmvsu83wXZgeRWBZM5zXs67Vtf63CFoYP2wS4ianp7jWnH0GMy3ekRmKyuWsIG7D4bAcvueM9F6EdTpxjwRblGH101e12usxajLmsUK6nCMIAdc8ETeE5IkMCPXIQAOg8N35gkT7h5WBTCkVs-cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
وقتشه پوکرو حرفه‌ای بازی کنی!
🎰
اگر به دنبال تجربه‌ای متفاوت و پر از هیجان هستید، بخش کازینوی وینکوبت بهترین انتخاب برای شماست. از بازی‌های کلاسیک مانند بلک‌جک، رولت و باکارات گرفته تا صدها اسلات جذاب با جوایز بزرگ، همه چیز برای یک سرگرمی حرفه‌ای فراهم شده است.
🕹
همین حالا وارد دنیای کازینوی وینکوبت شوید و هیجان واقعی را تجربه کنید. شاید برنده بزرگ بعدی شما باشید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/140756" target="_blank">📅 20:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140755">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwFD9xiWdQORbeA1B5IpfCOrcYEVmUSpac2d4yjXKfSGIPkZuNnqXDyRM_ymDJQXHOf9OZamI9VzEaKVQGRA650wrZVifu7UAdTa7szeGYEfm0yGtBo8C8zmjGHkbn3TEY1RigsoRGC21UmBOFogOe7CYBCfmiTlluBlXnrDdMkLj_Syqta-rGzIBiPzGQjYa7tN_qsSj-67gfaKrihbdrpt9Iq4oU1fT7tbQ3mg30ehukmnRuoz9hGG7D0AypJd_u-E3xVCvmQaowV_UHmeX5gnsh6dmAnxxhORL6wiIO5T7DRMRL2xRzkZiuk7Ok-whqqOb143IbQFk8i9DEu7dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
والیبال به میرزایی رسید!
🔴
با حکم احد میرزایی؛ رضا صفایی سرمربی تیم والیبال پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/140755" target="_blank">📅 19:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140754">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
❌
تیمداری مجدد پرسپولیس در والیبال پس از سال ها
❌
❌
تیم والیبال پرسپولیس تهران در گروه چهارم رقابت های دسته یک کشور با تیم‌های طلایی‌پوشان ورامین، نیروی زمینی تهران، بوعلی قم، مقاومت شهرداری تبریز، سروقامتان ارومیه، بنیس شبستر تبریز و روژمیوه زریبار مریوان…</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/140754" target="_blank">📅 19:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140753">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔄
🔄
هوشنگ نصیرزاده: پرسپولیس با شکایت از آسانی به CAS وقت خود را تلف می‌کند هیچ سندی علیه آسانی وجود ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140753" target="_blank">📅 16:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140752">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⭕️
⭕️
⭕️
خبرورزشی: مرغ حدادی یه پا داره بردن شکایت آسانی به Cas همین و تمام
⭕️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/140752" target="_blank">📅 16:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140751">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
تعویض زودهنگام محبی، به دلیل مصدومیت که احسان حاج صفی جای او را می‌گیرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140751" target="_blank">📅 16:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140750">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
❌
❌
هفته هشتم لیگ برتر در آستانه تعویق!
✔️
✔️
در صورت قطعی شدن برگزاری سومین دیدار دوستانه تیم ملی در فیفادی پیش‌رو و انجام این بازی در ترکیه، احتمال تعویق برخی مسابقات هفته هشتم لیگ برتر وجود دارد.
✔️
✔️
در این صورت، دیدار حساس استقلال و تراکتور نیز ممکن است…</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/140750" target="_blank">📅 16:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140749">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⚽️
گل های بازی بانوان پرسپولیس چهار - صفر ملوان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/140749" target="_blank">📅 16:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140748">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d02c1a357e.mp4?token=jTRLdTpXIOewQHjXiuK6psHYi5QEW6eUEnyWRWKNWUXO7dfmXAQ_VyLCRUcQoRMfH01rPG-Si6lkiDJF1fGSfVn-U24CJYDtj5qvrl661Jhjf4aXWKg0Hh2kumf0Vd7eKLheA5dv88w8bLl6FLfk31v3ZHTusVL5UgIfZuTKEnFskpUJltj8djGMnmI36_SAggjqi0ftkakYtUr0lAgEsZpimXslZAzsFlOUM5Sg1w6KYOHPZ0QMxEKSjeVxyNu-rMuakGpFIyuyKySTrc3LM2vAO-e-ek0bi17EEAk7Ma4cxzsbOWRPpVcL0INzpUXixp65JIdq5K-0pezgVYmHmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d02c1a357e.mp4?token=jTRLdTpXIOewQHjXiuK6psHYi5QEW6eUEnyWRWKNWUXO7dfmXAQ_VyLCRUcQoRMfH01rPG-Si6lkiDJF1fGSfVn-U24CJYDtj5qvrl661Jhjf4aXWKg0Hh2kumf0Vd7eKLheA5dv88w8bLl6FLfk31v3ZHTusVL5UgIfZuTKEnFskpUJltj8djGMnmI36_SAggjqi0ftkakYtUr0lAgEsZpimXslZAzsFlOUM5Sg1w6KYOHPZ0QMxEKSjeVxyNu-rMuakGpFIyuyKySTrc3LM2vAO-e-ek0bi17EEAk7Ma4cxzsbOWRPpVcL0INzpUXixp65JIdq5K-0pezgVYmHmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ملی‌پوشان فوتبال ایران پس از برگزاری دیدار تدارکاتی برابر روسیه وارد ایران شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/140748" target="_blank">📅 16:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140747">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/140747" target="_blank">📅 15:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140746">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/In4dC0zXuB_aP7eMMYwEnzXFETvOCMtoQidTzE3AnQzoXCQSoIJAYhNgbkrqYWbr5w35shdc6JidBv2QUXRk1GgKjGTuNNZkcnMkwsY2ECcGTPorw2aG6FTwG1B5IQyYPL00w-5z5YbHOYmMyN0wJbjAhcWc2YykKjVeHVIi_PH1mRR04k9ch5lm3HRQozkk7IgMWCUsz5J-44-58uHwvTDWK7dM_gqXua6NCDdaN-7dJ5dAEm_B7ZY8TSy9HfSLYZ4OEm0chebZAS0MbLtxIoeeRvmdj1tbbaCU-0gDs5B8rFiYIHVydRzSammlccC9nERDdNczwdgxZh7YHyGLNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
⭕️
⭕️
اگه درآینده جنگ رخ بده و بیش از 90 روز طول بکشه بازیکن میتونه یه اخطاره 30 روزه به مدیریت باشگاه‌بده و بعدش‌هم توافقی قراردادش رو فسخ کنه اما اگه جنگ کمتر از 90 روز باشه بازیکنان خارجی باشگاه‌ها حق هییییچگونه فسخی ندارند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/140746" target="_blank">📅 14:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140745">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🤩
✅
هفته‌هشتم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
صنعت نفت آبادان
🇮🇷
🗓
تاریخ جمعه ۱۷ مهر
⏰
ساعت ۱۷
🏟
میزبان شهرقدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/140745" target="_blank">📅 14:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140744">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">⭕️
⭕️
ابوالفضل رزاق پور مدافع چپ تیم فولاد: از پرسپولیس آفر دریافت‌کرده‌ام‌اگه دو باشگاه به توافق کامل برسن درنیم‌فصل راهی این باشگاه خواهم شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/140744" target="_blank">📅 14:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140743">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔄
🔄
عملکرد یاسین سلمانی در دیدار های تدارکاتی  امسال پرسپولیس: ۸ بازی - ۴ گل - ۵ پاس‌گل :  پ.ن تارتار به شدت راضیه از یاسین   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/140743" target="_blank">📅 14:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140742">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
بازگشت دنیل گرا به تمرینات پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/140742" target="_blank">📅 14:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140741">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OujZITNOfKRmxso8N9SkO0i1HVhQZRtfTE2augFJK3ud5aVU2czBBgG6paXvLF2mmO1gWlz34Q9PSwKlIJoktC0scBXaPq-42atXEwfRVQVFY0KIcFugCJnhMYTpZCO7V9VKDRRZzolFCl6ISvUdWsuXi7Hs3Q3W1JTCbfszfcA3Tq6-J383Hqtf1CuSnLYYCwLKS4nv7_4PPZeZfS-NNyNknzm5sacE0JDYwC8nwIsCuMF-74wy_UkIN4kO-05FfUf-jOnQ5anWEAM5gZUKOOJQPbNfP4Pm8_rkLnCkN1hRjpaVEMsMC-rIVMJPgYsqasX-vcJmYkLvBP6ntWXo0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🎲
هیجان واقعی همراه با کازینو
اسپورت نود
🔵
کازینو آنلاین
اسپورت‌نود
، هیجان واقعی با بردهای بزرگ همراه با انواع
بازی‌های کازینویی،
🎮
انفجار،
💣
رولت، بلک‌جک،
🃏
اسلات و بازی‌های زنده
همراه با پشتیبانی ۲۴ ساعته همین حالا شانس خودت رو امتحان کن!
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
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
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/140741" target="_blank">📅 13:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140740">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‼️
آخرین وضعیت پرونده جادوگر فوتبال؛ تمام اموال نامشروع مصادره شد
🔄
🔄
رئیس کل دادگستری استان البرز:
❌
❌
در پی دستگیری و محاکمه شخصی که در محافل ورزشی به نام «جادوگر فوتبال» معروف بوده است؛ وی به اتهام «فعالیت تبلیغی انحرافی مغایر یا مخل به شرع از طریق ادعای واهی و کذب» به تحمل ۵ سال حبس و ضبط اموال نامشروع حاصل از جرم محکوم شد.
❌
❌
حدود ۶۶۰۰ دلار، بیش از ۲ هزار یورو، ۸۰ سکه تمام بهار آزادی، ۳ شمش طلا و مقادیری طلا و ۲ دستگاه خودرو تویوتا لندکروز و مرسدس بنز از متهم کشف شد.
✔️
✔️
متهم هم اکنون در حال تحمل پنج سال محکومیت حبس صادره است و کلیه آلات و ادوات مختلف مربوط به سحر و جادو که از متهم کشف شده بود هم معدوم شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/140740" target="_blank">📅 13:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140739">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
🏟
بازسازی زیرساخت‌های پرسپولیس
✔️
✔️
رختکن‌ها، چمن، نیمکت‌ها و سکوهای ورزشگاه شهید کاظمی بازسازی و بهسازی شدن. بازسازی کامل استخر درفشی‌فر هم تقریباً تمومه و قراره نیمه دوم مهرماه به بهره‌برداری برسه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/140739" target="_blank">📅 13:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140738">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🤩
⚽
شاهکار پیمان حدادی در پرسپولیس؛ درآمدزایی ۱۳۶۵ میلیارد تومانی از پیراهن سرخ‌ها
❌
پیمان حدادی، مدیرعامل پرسپولیس، پس از پشت سر گذاشتن نقل‌وانتقالاتی موفق و پیروزی در پرونده‌های حقوقی باشگاه، حالا با یک دستاورد اقتصادی قابل‌توجه مورد توجه قرار گرفته است. بر…</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140738" target="_blank">📅 11:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140737">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkkunU3lqgFljhnu-ynCMc9imXLtzDOtj5Wx4QYcQ-nCvu8WxvOiDOVaWE2wI0tdP8s0Lm1hILMxA3jblJ4Lokly8DZbTGCXJfwh1DmrkYjlbFW2S8UO8HSo3m__hZTHLyfJ96m4oSMlc7gxBGfObqqdmjg4JSE2DsoA5q0pBkV3M9_kQ4telMHuniyHteEONMqxpWXQ_PqP45RNl2kCefQoC_YZ7sLl0kGGg2RsXBxkZke4J5gtmnAtwCshlUZkgLwPubsThhQi4aAqrNSk1EbL7ayz0wskevQHkSeUT8y6EMXCmLJhfT545DKvq1OIw7UF2bwHOjuz54kx5wvFeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
✅
هفته‌هشتم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
صنعت نفت آبادان
🇮🇷
🗓
تاریخ جمعه ۱۷ مهر
⏰
ساعت ۱۷
🏟
میزبان شهرقدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140737" target="_blank">📅 11:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140736">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3297ba87bf.mp4?token=eX0asDSwbFfQNDnrjwT1d2kdS54kdVvgy1OC6L-g7BUqI5TzsTZ_IyduX0IMeTPBMH68_hkVVStJnl6hlw7mmAmVYlAZD02jOgDIqRFhclMaujKNzbjr6ootkK5pi67wrlelRRImrqyuoDwN77cA0xbOLtqmnUh5lh99aDKLCoJ9hUTn-V5-T0xu95PvCVNNc5-_-4d6dnKvxpwIPUPYa7oz6q3ZHGWp6xJrEAYa2OcSaS8tcbUDGGXM9B6z4tdjhnbxKbCoMLaHPh6aoYbu_GxlPit_VlmGMhRAW8j1XvV-t-UiIRSd_S2DMRqiRg2YFm4AcOVo94u_7gz4miYyMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3297ba87bf.mp4?token=eX0asDSwbFfQNDnrjwT1d2kdS54kdVvgy1OC6L-g7BUqI5TzsTZ_IyduX0IMeTPBMH68_hkVVStJnl6hlw7mmAmVYlAZD02jOgDIqRFhclMaujKNzbjr6ootkK5pi67wrlelRRImrqyuoDwN77cA0xbOLtqmnUh5lh99aDKLCoJ9hUTn-V5-T0xu95PvCVNNc5-_-4d6dnKvxpwIPUPYa7oz6q3ZHGWp6xJrEAYa2OcSaS8tcbUDGGXM9B6z4tdjhnbxKbCoMLaHPh6aoYbu_GxlPit_VlmGMhRAW8j1XvV-t-UiIRSd_S2DMRqiRg2YFm4AcOVo94u_7gz4miYyMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
۶ سال گذشت...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/140736" target="_blank">📅 10:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140735">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✔️
✔️
مصدومیت دانیال ایری از ناحیه کشاله ران پا بوده و مداوا روش شروع شده تا بزودی به تمرینات برگرده؛ اما بعیده به بازی صنعت نفت برسه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/140735" target="_blank">📅 10:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140734">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
🏥
دانیال ایری در بازی آخر تیم امید مصدوم شد؛ MRI کشیدگی عضلات لگن و بالای کشاله ران رو نشون داد. کادر پزشکی پرسپولیس هم درمان و فیزیوتراپی رو شروع کرده تا هرچه زودتر برگرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/140734" target="_blank">📅 10:30 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140733">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
❌
❌
گروهبان قندلی: از بازیکنانی که به آنها فضا دادیم اما نتونستن چیزی که مدنظر ما هست رو انجام بدن در اردوهای بعدی استفاده نخواهیم کرد
😁
✔️
✔️
این بازی ما رو یاد جام جهانی انداخت و سطحش در حد این رقابت‌ها بود. برای ما بسیار مفید بود هرچند از نتیجه ناراحت هستیم…</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/140733" target="_blank">📅 10:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140732">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
❌
❌
گروهبان قندلی: از بازیکنانی که به آنها فضا دادیم اما نتونستن چیزی که مدنظر ما هست رو انجام بدن در اردوهای بعدی استفاده نخواهیم کرد
😁
✔️
✔️
این بازی ما رو یاد جام جهانی انداخت و سطحش در حد این رقابت‌ها بود. برای ما بسیار مفید بود هرچند از نتیجه ناراحت هستیم…</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/140732" target="_blank">📅 10:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140731">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7PZYGzIXfdiEV0VExtW1jkQcYClpPlAZIVM_kPShaW6rBGRR1YJ7XnfBG50pTvgoCnnq3kuYAjlI9IDsrrmRTVJUxxQKeMrQkLbGJcFjA18JdDUiVxzQl0QwJkZaSOg9yeTp8RWIybGFefYbdPrNnWPChmV2yVCkqx-rGSw5BUSS8Rqe1ABshMKB5OdRkgb1AUtD-M3wjKwDch3LbcrgCSc742hORnHtplmAmz6wcK2Zro8S1t-qf7cUw0uUyFK62fS2NWbDJsYMlSt9yn7XIMH3dmlOueOHLCXMDXC1yEG2eJUFbXyDse5I9aRDy-N02xveDndnvUtUkhu_iAJgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
حمله تند روزنامه‌های ورزشی به قلعه‌‌نویی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/140731" target="_blank">📅 09:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140730">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1PWBuUQmWZjYJz0PjVwGs050ZhHFolIWusBHA2a6RxugoxNRhou-Dg0Jidc6f-ve4O4M4lSGpTZ58I5Bu_NPZHhc5WRIS5mUNSV6ue9p8ppu5rwhMQQS9vd3fdQBesn1pDKExCakbK8-MVnXCT5o0qen-qW68toOu1Z59wIw1PpogaSGe5-3qaWs0SabI9ItVDTXlY2Jn4bKiTpUy9x1cDhVpnRHC13nF15vwA304SK-qBtms_4iQ0DsIYUaeTTKolQKiz_yBS0VBNcvgRCdXUw4lMGIsVuy3QkUxYQq_xHY-DlcVI-jLt4zVyPXNfxeSrxqpj7Vnb_vqT2Kuu9zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
صبحتون بخیر ارتش سرخ
🚩
✨
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/140730" target="_blank">📅 09:00 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140729">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rytX49pPg0V3IolxFRSBWcWx3cQ4J3tCbc0s3LqgubyvFD1JquFZOhHADlINFpNEd7z-va8WBMVIQA_lHp2efxII5C_M0-7iRuGquOFJoZ-v7FvMAR9p8b6IGqQ-lUjysw7hA_nGlBJv0rO4lbtyBX2WrZvGNF4NkxWUwlyKALXAxOkbj-am_R88bngblj9tCzjH0zAlmVDppDv0H2TQ6XC22aC0MQp3QkVXZWQqOLvB9IbKXGby_J-uf_Xx4iFVzmX2fwmL_zkTsDutK0kOmv3LEn3ddEft93zWumg1uNfB6l1zhW-vdQ-r215oWUjqNOpaQ5IS4yCYGdxfGSctqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ورود به اسپورت‌نود؛ ساده‌تر از همیشه!
🔗
دنبال یه راه سریع و بدون دردسر برای ورود به اسپورت‌نود هستی؟
🔵
با مینی‌اپ ربات رسمی اسپورت‌نود، مسیر دسترسی ساده و یکپارچه شده؛ بدون لینک‌های متعدد و مراحل اضافی، مستقیماً وارد محیط کاربری شو و از امکانات سایت استفاده کن.
🔗
ربات رسمی اسپورت‌نود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت‌نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/140729" target="_blank">📅 01:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140728">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IcFCMx_7Z88M6eKzruA11VOy3oFIX5jRsA2n_e0wACZrgqyztpcfYTlPbRhbRcPbaHjGDLwiox6hhTI4qymB4Lhh2_fkUhLLB5ImDgs2iJWXwIkOeGb6fSrquRE6pNaetAmnbn-NAWYb_25Naemo5Ok47R3QJppPuUlW8-Kv2eLwBjf6-uZTHvuQRzmOJC_NYTD-0eRFAEqwOnNBJy_caxyimEBsyoASPUVWvHO8Re5NpHtcXbbxGJ2vd9F7eg3OZDJa2mo1-s312iT1jYERnPEpg7XON5tkS_kOkELkZ9Dbo7ko2KrL4TVaOG9xb3NGRIj-MPE9w2LMrbm2Cj-ZHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
در تاریخ بنوسید تو فوتبال‌‌فاسد ایران قرار بوده استقلال جام رو بگیره بجاش ٧۵٠ هزاردلار طلبش از مهدی‌تاج رو بلاعوض کنن‌‌. پشت‌پرده درحال انجام بوده اما مخالفت شدید باشگاه‌ها این معامله کثیف پول با جام بهم میخوره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/140728" target="_blank">📅 00:27 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140727">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
❌
#فوووووری
🖍
دانیال ایری به دلیل مصدومیت در تمرین امروز  سرخپوشان غایب بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/140727" target="_blank">📅 00:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140726">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🏆
🏆
نتایج بازی های امشب:
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140726" target="_blank">📅 00:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140725">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVXNqZLYkQomEk33dmbtaewoj9C4Szg05RWg8Fb5dSuwp5_NgLK50zUtGSlxOagzD88iI27muImp6k5EdonyqA0MM7N8vXasgPb4ke1ObiDemyqH9WS-UYXAmNpjmkSbKbCUO4m9gROGhBMu2b4GpieoxnVSIhsiHZwWEmSoNLPLk_8UptWi77K48dOmOrBAhjZsO1mNGSI1ozEvfL7ZWZR82xrg8-REfQZNjySYZfnjkum5drPx8f2XGu7EH_VXZ4KTE9-OAlgp8U6gJlTvc_ERVhPmlmDoF1fdYyKmxP6tADk6EPle2VasAJdFP_GV_g9JnoTRl6MtC147gpt09A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏆
نتایج بازی های امشب:
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140725" target="_blank">📅 00:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140724">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♨️
🤩
🤩
افشاگری باورنکردنی میثاقی از یک ایجنت، عارف آقاسی، پرسپولیس و پیش قرارداد برای یاسر آسانی!
🔄
🔄
محمدحسین‌میثاقی: پرسپولیس به یک ایجنت ۱۰۰ هزار دلار پول داده بود که عارف آقاسی را به پرسپولیس ببرد ولی این بازیکن را به استقلال برد و الان باشگاه از این ایجنت…</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/140724" target="_blank">📅 00:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140723">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofb2SQ4Dtyjj4DT23NRzIVFMRb578A6bRgFJZUnaDlG5blb8w5cnLarWORIS6YHvlGpnSoImefbRuMYrPtAbg2QdQSHpKIQs4RdS-WvVJTymPte6afkOivjlsXboVrAqQhnpqhuGvVI7Iv0_gE_z2qCqMAdiOWjDhraE025c4X0sVa2LpA_zPBLeJXfrgNMZsYYzlhlJTYhzzlIMU5FpRfJ9tpqdAQ9M-26-0yaHL29_8CISrO_hPOMGb5Uy3jUHaNpR9mIBAc8rASQETvMhn2EaJ7eXckY3u8lB5rNYcrUkg8Jtd0PIzwIjd6Pd-RRln7tOsaCIDcFndsmJMxrFyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
🔻
مدت قرارداد احتمالی جدید نیازمند با پرسپولیس مشخص شد
⚪️
⚪️
پیام نیازمند گلر پرسپولیس که اخیرا مذاکراتش را با این باشگاه برای تمدید قرارداد آغاز کرده طبق شنیده ها به توافقات نسبی دست یافته. طبق شنیده‌ها قرارداد جدید نیازمند با پرسپولیس 2 ساله خواهد بود و گلر فعلی سرخپوشان قرار است دو فصل دیگر نیز در جمع پرسپولیسی‌ها باقی بماند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/140723" target="_blank">📅 23:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140722">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">📘
📘
در 14 بازی آخر تیم ملی با هدایت امیرخان فقط سه برد داشته که اونم مقابل گامبیا، تانزانیا و کره‌شمالی بوده
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140722" target="_blank">📅 23:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140721">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_Lrn7PS1SMvxFs6P0-2H2itRlrqmgKuFKGwFHAdXGydkk4BtK4ExK9g5dcJ3hSxdB4BOWIuCq9ySDJeYdL_w4JpgTPD5ovfLiQpFpKlKMajz0iVrVH0hDgHIrN6_4GKb8hNkBFDXmXObgL5sksTUHd7KvE9yRIXd9gLWlvn4Lm2pn3ullW3D4np04z-92IhJH-oK0znZVMS2KQEV7EkAiOQvbYqTiRt1B_Uu2A2Z5cZfPj_ePv67OBCexbqthBOMPNjme0WhCUw2zhCBoMgP9fXr4t5raxOwdTHiMmA5A7kJupm1ROwcJ1lwd_E8vvjIrgT9YUSmVhv-RXnN7IRdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
قرارداد ۱۳۶۵ میلیاردی پرسپولیس برای تبلیغات البسه
✔️
✔️
باشگاه پرسپولیس قراردادی به مبلغ ۱۳۶۵ میلیارد تومان برای تبلیغات بر روی البسه تیم‌های خود شامل بزرگسالان، رده‌های پایه و بانوان منعقد کرد.
✔️
✔️
این قرارداد برای فصل جاری جهت اطلاع عموم بر روی سایت کدال…</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/140721" target="_blank">📅 22:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140720">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CoYy-jkkzd2fZFxP_T5XR2wSP9-l8Hh4h6ZJww5QcRHbG8BGoSe9iiabtpYz5C6tAWvLGZPK-xf26iE0QMPWBbBuTLMOk_h0qmkSZWkCXINx47EK2VtI5ZCN0kOdW2eKvvRBcna_OHqBnDesjNOVnw0buHx5GMTRao4ynwzmynfIpibD_1mZdwXaRMw2yC3skurDeTy4MpResbjkl2I7E9PfhYJ1KPWnqH0SGd6X-Zu_UVK7mS0l1sQj1yzvc-xmhzMt0E7d5UhcrMkLjlstBsibhnNm1_sYX8_SsS6_vu3Pp3qjr6TnIulwmPzBQGzUzbCNqyhcgsjc_e9CjRPyng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
امشب اگه پیام نیازمند نبود، فاجعه بازی انگلیس تکرار میشد؛ تفاوت دروازبان درجه یک با دروازبان معمولی اینجور جاها معلوم میشه
❤️
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140720" target="_blank">📅 22:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140719">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
لباس پرسپولیس عوض می‌شود
⚡️
⚡️
باشگاه پرسپولیس برای فصل جدید رقابت‌های فوتبال، در آستانه تغییر برند تولیدکننده البسه خود قرار دارد.
⚡️
⚡️
⚡️
برند «یوسف جامه» در فرایند مربوط به انتخاب تولیدکننده البسه باشگاه پرسپولیس، توانسته نظر کمیسیون معاملات باشگاه را جلب…</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/140719" target="_blank">📅 22:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140718">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1880075a0d.mp4?token=vUutd2rsNNZQBOYAhr0UEaxEBVYXTAyEF9g2IqLa07ERmtuSC8F0UV4CQvX3N6U4rOYPiSGKXj-8Sy2F8tR2xLOMx-6q11qF3GeRLNx2EWOF5phR6563ZP4YBCOO8ZsRuCerrGOE5t6-PbfEhavZmltw71QOghKKo8HuZMuh9EaVFwWN5mHFYXo_mF17gJtFBFVx2s_7cIL6-kYDVCbNFG8DQGKPKC4vi01QxwVYTa_jsPsLyTsZOgsIKPbPempx3tYiHCsjv5QikryovWh7hZBDOncqL3XGQek8f4MBMj8CCTr0TG6II-Ii9VtZyDByDRNjMTmdQ6P0U_X11oSJ_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1880075a0d.mp4?token=vUutd2rsNNZQBOYAhr0UEaxEBVYXTAyEF9g2IqLa07ERmtuSC8F0UV4CQvX3N6U4rOYPiSGKXj-8Sy2F8tR2xLOMx-6q11qF3GeRLNx2EWOF5phR6563ZP4YBCOO8ZsRuCerrGOE5t6-PbfEhavZmltw71QOghKKo8HuZMuh9EaVFwWN5mHFYXo_mF17gJtFBFVx2s_7cIL6-kYDVCbNFG8DQGKPKC4vi01QxwVYTa_jsPsLyTsZOgsIKPbPempx3tYiHCsjv5QikryovWh7hZBDOncqL3XGQek8f4MBMj8CCTr0TG6II-Ii9VtZyDByDRNjMTmdQ6P0U_X11oSJ_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
درگیری شدید در بازی رده نوجوانان لیگ تهران میان تیم‌های کیسه و شاهین!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/140718" target="_blank">📅 22:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140717">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✔️
پرسپولیس هنوز هیچ توافق یا مذاکره‌ای با اندونگ انجام نداده/طرفداری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/140717" target="_blank">📅 22:06 · 07 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
