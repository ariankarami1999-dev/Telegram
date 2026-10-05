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
<img src="https://cdn4.telesco.pe/file/rfZxNaZRzCnRMW6V8KuJ2HXJ4OsmCl2Lph3gLhzhzUCurgXYYTKBlj2c08bxWTOOzuIupNWTqTF6xW7fQyv8lR8ZQUO-Z9bNS7lUyYk59tlMBJ7-ZvPzKNFYMBTeH7BnbG18ZObbhWDBDX97g0thnC4hNQdZpe4KA9NU81EtAVH85-TDkh3eOK4AtVxuF1kil0-cES4g_IouISKP6N3qlXs7IkexQvKQ9dj84oNzBKTorIDK7o8vzajmvG7WSqSUAYzRSBRt7rPfz7hNCcXg2ETipvXeJ5mSW_XsJ59lcc8VGzadVlMpwikdwx34-8FNJKZoU0g6DOoYlAL5Pp8-5w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-13 05:41:06</div>
<hr>

<div class="tg-post" id="msg-140962">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8U7ICYLjiJuGXMHjfTfTfQM05HjVHDjpbdNy-mIGidK-DaJXiJPCYp-DlrTy3PeoTN7NYbXGbFFzlycOzyUaDzVk7J5acgJ8BvYa6qj2hDDkHnDkSVFaA5Cp_Kzb0ek5OP8SYrVj-E02an3BFWWfbJkEf-NtISF11W25DaACamIrAWEjiYF4i7vkkLmQezWY69PfxRed0k2jf13MqS3Z6J-5iq3NVgygL9isd6Rcb8OwckFysEOUxVxq4MO75El5joRsYun5wvwBj42FU13ms4kwMyeb-tAM0_CCZY9IotG61-4r52xtF1F_tKmzHM7MPyA4KhYEbqe_VVHPfaQDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
France
🆚
❤️
Belgium
⏰
Monday 22:15
🏟
Stade de France
🇪🇺
فرانسه از نظر کیفیت هجومی و میانگین موقعیت‌های خلق‌شده برتری محسوسی دارد و احتمالاً حجم بیشتری از حملات را در اختیار خواهد داشت. بلژیک در انتقال‌های سریع خطرناک است، اما مقابل فشار و مالکیت بالای فرانسه احتمالاً فرصت‌های کمتری برای تهدید دروازه پیدا می‌کند.
✅
برآورد آماری: برد فرانسه ۵۸٪ | مساوی ۲۴٪ | برد بلژیک ۱۸٪ | بالای ۲.۵ گل ۵۷٪
همچنین در غیاب دی‌بروینه و تیلمانس احتمال می‌رود خروس‌ها پیروز میدان باشند.
🟢
با درگاه بانکی اختصاصی و امن وینکوبت، حساب کاربری خودت رو به‌صورت مستقیم شارژ کن و مثل هزاران کاربر دیگه، بدون دردسر از امکانات وینکوبت استفاده کن.
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
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SorkhTimes/140962" target="_blank">📅 01:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140961">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">💢
💢
مدیران پرسپولیس به تاج اعلام کردن اگه استقلال قهرمان لیگ اعلام بشه از لیگ برتر انصراف میدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/SorkhTimes/140961" target="_blank">📅 00:58 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140960">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✔️
✔️
حدادی : نمیتونم قرارداد محمودی رو اضافه کنم چون باید به سازمان بازرسی جواب بدم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/SorkhTimes/140960" target="_blank">📅 00:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140959">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
❌
فوووووری
🔄
🔄
حدادی: تا آخر همین ماه یه جلسه مهم برای بیرانوند تو فیفا به صورت ویدیو کنفرانس انجام میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/SorkhTimes/140959" target="_blank">📅 23:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140958">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TH_kn5w57zw3ivNkIHgLefcDyCC4UrOSJjdRRsWi6iGtMAR2X-ou29iEWrspvtYqUCqtigb0DhSZ0W-Jb3aAuFO0GaOiFAz9PUrWMm-CpB1COWH0EsBad0unjS4bYG5v7-bP0cMuTEaayZavZ2cneDIVVnO-ffRRIOFgWerQh4eob2-t7-xMkFhZD5pMJ2JeNz0ZS_Y3SAXZ__3zaCuQY-btpJN5tDm0QvX2b4r6NWMC9Oj7gOL53DqoP-MT1dfB6AELnglBr_atWl9elU7eR9N7fuutoXoxBStwvUNXlW9Uf6p8Kbbk-rVsk6qxh6WFCXD6gD_aKQKYUVOLv9hgmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
⚪️
برترین بازیکنان لیگ برتر تا این لحظه از نظر متریکا
1⃣
⚽️
🔻
علی علیپور 7.7
2⃣
⚽️
🔻
سعادت حردانی 7.49
3⃣
⚽️
🔻
اسماعیل قلی‌زاده 7.49
4⃣
⚽️
🔻
تیبور هلیوبویچ 7.48
5⃣
⚽️
🔻
یاسر آسانی 7.46
6⃣
⚽️
🔻
محمدمهدی محبی 7.45
7⃣
⚽️
🔻
عباس کبیریزی 7.44
8⃣
⚽️
🔻
امیرحسین حسین‌زاده 7.39
9⃣
⚽️
🔻
مجید عیدی 7.37
0⃣
1⃣
⚽️
🔻
امیرمحمد رزاق‌نیا 7.37
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/SorkhTimes/140958" target="_blank">📅 23:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140957">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
حدادی : در یک بازی رسمی از عالیشاه تقدیر میکنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SorkhTimes/140957" target="_blank">📅 22:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140956">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
❌
❌
خبرنگار الجزیره در تهران: به نظر می‌رسد که همه طرف‌ها در حالت آماده‌باش کامل هستند و منتظر هرگونه تحول نظامی هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SorkhTimes/140956" target="_blank">📅 22:23 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140955">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
❌
قرارگاه خاتم‌الانبیا: براساس اطلاعاتی که دریافت کردیم، آمریکا قصد دارد دوباره به ایران حمله کند. اگر حمله کند، پاسخ دردناکی می‌دهیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SorkhTimes/140955" target="_blank">📅 22:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140954">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✅
✅
حدادی: قرارداد علی علیپور با پرسپولیس تمدید شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SorkhTimes/140954" target="_blank">📅 22:07 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140953">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
❌
غیبت عالیشاه برابر پرسپولیس/ ستاره سابق سرخ‌ها کجا بود؟
❌
امید عالیشاه در دیدار دوستانه گل‌گهر و پرسپولیس نه در ترکیب تیمش قرار گرفت و نه روی نیمکت نشست.
❌
❌
گویا عالیشاه در ورزشگاه حضور داشته و به دلیل مصدومیت جزئی در رختکن در حال گرفتن ماساژ بوده است. این…</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SorkhTimes/140953" target="_blank">📅 22:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140952">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✔️
حدادی : قرارداد همایی فر ۱/۶۰۰ دو سال دیگه هم قرارداد داره فردا قرارداد هرکسو زیاد کنیم باید بریم صدتا نهاد جواب بدیم ، اضافه هم نکنیم بازیکن انگیزه ش از بین میره و راحت می‌تونه فسخ کنه
☹️
☹️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس …</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SorkhTimes/140952" target="_blank">📅 22:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140951">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🎙
🤩
پیمان حدادی: به درستی قهرمان لیگ سال پیش اعلام نشد؛  امسال ۲ همت درآمد خواهیم داشت. خیلی از باشگاه‌ها پول نداشتند. پارسال ۵۶۰ میلیارد درآمد داشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/140951" target="_blank">📅 21:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140950">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👀
❓
چرا خداداد عزیزی منتفی شد؟
🤩
پیمان حدادی: سیاست پرسپولیس و تراکتور فرق دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/140950" target="_blank">📅 21:24 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140949">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🤩
🎙
با اعلام حدادی ساخت ورزشگاه به خاطر نبود ثبات اقتصادی و امنیتی فعلا قابل ساخت نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SorkhTimes/140949" target="_blank">📅 21:23 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140948">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🎙
🤩
حدادی: یا فوتبال یا یه کار دیگه! بازیکنای پرسپولیس باید حواسشون به فوتبال باشه. شکاری ۹۰ میلیارد از پولش گذشت و آقاسی با استقلال ۶۰٪ بیشتر گرفت. جام حذفی رو هم با تیم‌های حاضر برگزار کنید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SorkhTimes/140948" target="_blank">📅 21:21 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140947">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✅
قرار داد 27 بازیکنان ایرانی تیم 1همت هستش.
🔘
اسکوچیچ برای پرسپولیس بالای یک همت هزینه داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SorkhTimes/140947" target="_blank">📅 21:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140946">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🤩
حدادی : حتی من لیست تابستونی فصل آینده رو هم دارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SorkhTimes/140946" target="_blank">📅 21:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140944">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🤩
حدادی: با همه مدیران باشگاها رفیقم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SorkhTimes/140944" target="_blank">📅 21:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140943">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🤩
حدادی: برای آسانی مدارکی داریم که هیچ باشگاهی نداره؛ فدراسیون هم باید استعلام فیفا رو منتشر کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SorkhTimes/140943" target="_blank">📅 21:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140942">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">▫️
🤩
حدادی: قرارداد علی علیپور با پرسپولیس تمدید شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SorkhTimes/140942" target="_blank">📅 21:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140941">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🤩
حدادی : هرکس نمیتونه توی  جام حذفی شرکت کنه انصراف بده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SorkhTimes/140941" target="_blank">📅 21:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140940">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🤩
حدادی : اون ۱۰۰ هزار دلار که بخاطر آقاسی دادیم بخاطر پیش پرداخت یک بازیکن بود که می‌خواستیم حسن نیت خودمون رو نشون بدیم و با اخذ رسید اون پولو دادیم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/SorkhTimes/140940" target="_blank">📅 21:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140939">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cH1qMGSP6v2smaDs8sBFQ2B2KWpk6KxjfPuajILnhD6OoGulTYmATSMJuUerllmmc3xQnGowu734pJeugRykospq2qJzvDtv9Y1e7IT0OsvcrWhLkptaVymkQtL6QUy3Duj2tOHdbEjxvoYl0PPl2uXwfCVTln56z7yQvPLPx7Y0K5qgtOyxy5xUU27rnt1VlYunvk2QK_QUWGzkG9L-821nK1xGiYskDosTaIHYjCxcFV7FQNHJ5cFFOpNr779VVAva2yWVUvBdeSpXDxzDprcaeH7leetpcy2KVY-hIWxcPNu2pi72YGfntlzcWktnRxmGE3EB5qMEKeeQsQpXPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
Portugal -
❤️
Norway
⏰
Tonight 22:15
🏟
Estádio Do Dragão
🇪🇺
پرتغال در ۳ بازی این گروه ۷ گل زده و با ۹ امتیاز صدرنشینه؛ نروژ ۵ گل زده و ۶ گل هم دریافت کرده، ضمن اینکه پرتغال بازی رفت را ۲-۱ برده است. از نظر xG، نروژ با وجود کیفیت هجومی هالند خطرناکه؛ اما مدل‌های آماری همچنان پرتغال را شانس اول می‌دانند: برد پرتغال ۵۵.۹٪، مساوی ۲۰.۷٪، برد نروژ ۲۳.۵٪. می‌باشد. احتمال بازی گل‌دار و نزدیک زیاد هست و همچنین احتمال ‌می‌رود هردوتیم به گل برسند.
🟢
با درگاه بانکی اختصاصی و امن وینکوبت، حساب کاربری خودت رو به‌صورت مستقیم شارژ کن و مثل هزاران کاربر دیگه، بدون دردسر از امکانات وینکوبت استفاده کن.
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
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SorkhTimes/140939" target="_blank">📅 20:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140938">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✔️
✔️
فووووووووری از حدادی : قرارداد امیر حسین محمودی 3 میلیارد و 200 میلیونه
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SorkhTimes/140938" target="_blank">📅 20:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140937">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✔️
✔️
حدادی : نمیتونم قرارداد محمودی رو اضافه کنم چون باید به سازمان بازرسی جواب بدم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/140937" target="_blank">📅 20:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140936">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
❌
فووووووووری از حدادی : تصمیم گرفته بودیم اورونوف و تمدید کنیم و بعد جام جهانی بفروشیم ولی نشد
🙁
🙁
🙁
🙁
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SorkhTimes/140936" target="_blank">📅 20:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140935">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
❌
فوووووری
🔄
🔄
حدادی: تا آخر همین ماه یه جلسه مهم برای بیرانوند تو فیفا به صورت ویدیو کنفرانس انجام میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/140935" target="_blank">📅 20:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140934">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
❌
فووووووووری از حدادی : تصمیم گرفته بودیم اورونوف و تمدید کنیم و بعد جام جهانی بفروشیم ولی نشد
🙁
🙁
🙁
🙁
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/140934" target="_blank">📅 20:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140933">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
⭕️
⭕️</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/140933" target="_blank">📅 20:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140932">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
⭕️
⭕️</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SorkhTimes/140932" target="_blank">📅 20:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140931">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✅
قرار داد 27 بازیکنان ایرانی تیم 1همت هستش.
🔘
اسکوچیچ برای پرسپولیس بالای یک همت هزینه داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/140931" target="_blank">📅 20:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140930">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
حدادی : اجاره شهرقدس هر بازی ۱/۲۰۰
🫪
🫪
🫪
✅
بازی های میزبان ۴ میلیارد هزینه میکنیم مهمان ۵ میلیارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SorkhTimes/140930" target="_blank">📅 20:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140929">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔻
🎙
⚽
حدادی، مدیرعامل باشگاه پرسپولیس: قرارداد 5 بازیکن خارجی ما 4 میلیون و 80 هزار دلار است
⚪️
در نیم فصل و تابستان بعدی بازیکن خارجی نخواهیم گرفت، ابتدای فصل بخاطر همین کادر ایرانی گرفتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/140929" target="_blank">📅 20:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140928">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50712b5d4b.mp4?token=ftR3xYjDiYU9kVvN95yHKUid7sqRFOx3F5R-nnGDps_K9-ksFRjQi2EokVZNYnFAlalEkXNBd1dBucjiZzFJt0rTIl8dy0jZ3leMhoSO47pSAWBHz7gVtYZdLJY9dy_kKgRt0fnKCkpu9-e8gbP2WzQ2ub08EIsygJmNWbFVJzGdFuT6d63ibEZWKDQyKf0-uk7uM6wYGThn0iXACkwwwbCzty39eSBncnbBC0oZSp5a42ZEaK8Qz8rOd00BA2Ai8Umx_9w5XJHLHnfnHozbIOeVb_1UoGReS3JnXkGSEdpx6SRqN26pcGiKGJyZumiuahB6b01E-OIZdsxAwyC-zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50712b5d4b.mp4?token=ftR3xYjDiYU9kVvN95yHKUid7sqRFOx3F5R-nnGDps_K9-ksFRjQi2EokVZNYnFAlalEkXNBd1dBucjiZzFJt0rTIl8dy0jZ3leMhoSO47pSAWBHz7gVtYZdLJY9dy_kKgRt0fnKCkpu9-e8gbP2WzQ2ub08EIsygJmNWbFVJzGdFuT6d63ibEZWKDQyKf0-uk7uM6wYGThn0iXACkwwwbCzty39eSBncnbBC0oZSp5a42ZEaK8Qz8rOd00BA2Ai8Umx_9w5XJHLHnfnHozbIOeVb_1UoGReS3JnXkGSEdpx6SRqN26pcGiKGJyZumiuahB6b01E-OIZdsxAwyC-zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
🎙
⚽
حدادی، مدیرعامل باشگاه پرسپولیس: قرارداد 5 بازیکن خارجی ما 4 میلیون و 80 هزار دلار است
⚪️
در نیم فصل و تابستان بعدی بازیکن خارجی نخواهیم گرفت، ابتدای فصل بخاطر همین کادر ایرانی گرفتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/140928" target="_blank">📅 20:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140927">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
❌
❌
پیمان حدادی: ما شفاف هستیم و هیچ مشکلی نداریم نگرانی بابت لو رفتن قرارداد های پرسپولیس هم ندارم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/140927" target="_blank">📅 20:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140926">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">⭕️
⭕️
باشگاه پرسپولیس با خرید امتیاز باشگاه پادیاب خلخال صاحب تیم «ب» شد.
🆕
🆕
🆕
عصر امروز با حضور مدیرعامل و مالک باشگاه پادیاب خلخال در باشگاه پرسپولیس، امتیاز این تیم که امسال در لیگ دسته دوم حضور داشته به باشگاه پرسپولیس واگذار شد.
🔜
🔜
راه‌اندازی تیم «ب» یکی…</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/140926" target="_blank">📅 20:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140925">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
❌
❌
امشب پیمان حدادی مدیرعامل پرسپولیس ساعت ۲۰:۰۰ در لایو ورزش سه حاضر خواهد شد و به سوالات هواداران پاسخ خواهد داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/140925" target="_blank">📅 20:11 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140924">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✖️
✖️
شنیده میشود که رای کمیته استیناف نیز در پرونده آسانی تایید رای کمیته انضباطی بوده و پرسپولیس موفق به محکوم شدن این بازیکن نبوده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes ﻿</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/140924" target="_blank">📅 19:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140923">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
❌
❌
امشب پیمان حدادی مدیرعامل پرسپولیس ساعت ۲۰:۰۰ در لایو ورزش سه حاضر خواهد شد و به سوالات هواداران پاسخ خواهد داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/140923" target="_blank">📅 19:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140922">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
❌
اوستون اورونوف در ادامه‌ی رقابت‌ها نقش موثرتری در ترکیب پرسپولیس خواهد داشت/ورزش‌سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SorkhTimes/140922" target="_blank">📅 18:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140921">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">⭕️
⭕️
۶ بازی آینده پرسپولیس در لیگ برتر فرصت مناسبیه برای اوج گرفتن و صدرنشینی در لیگ برتر
✅
✅
✅
ما ۳ بازی خانگی مقابل صنعت نفت ، فولاد و فجرسپاسی داریم و سه بازی خارج از خونه مقابل خیبر و مس شهربابک و نساجی و با توجه به آمادگی و اسکواد خوبی که داریم باید به…</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/140921" target="_blank">📅 18:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140920">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
❌
پیمان حدادی: خدا را شاکریم که سومین برد متوالی تیم بانوان را شاهد بودیم. سه پیروزی ارزشمند که باعث شد در صدر جدول قرار بگیریم و در هر سه مسابقه نیز کلین‌شیت داشته باشیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/140920" target="_blank">📅 18:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140919">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✖️
تارتار به دنبال امتحان کردن امیرحسین محمودی در پست شماره ۱۰ است.
❌
با مصدومیت علیپور، احتمال داره محمودی از وینگر به پشت مهاجم منتقل بشه تا خلاقیت بیشتری به خط حمله پرسپولیس بده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/140919" target="_blank">📅 18:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140918">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‼️
⁉️
‼️
یحیی گل محمدی به دلیل اینکه باشگاه دهوک یکماه در پرداخت دستمزد خودش و بازیکنانش تاخیر داشته اعتصاب کرده و تمرینات تیم شو تعطیل کرده:))))
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/140918" target="_blank">📅 18:21 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140917">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
مهدی تاج: سهمیه ما برای سال آینده 3+1 است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/140917" target="_blank">📅 15:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140916">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
#شایعات
✔️
هیئت مدیره پرسپولیس به سازمان لیگ اعلام کرده که در صورت اینکه نتیجه دربی 3-0 به سود پرسپولیس اعلام شود از بردن پرونده آسانی به دادگاه CAS صرف نظر می‌کند، در غیر این صورت این پرونده‌ به صورت رسمی با تمام مدارک به cas برده خواهد شد
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/140916" target="_blank">📅 15:24 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140915">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b62ce8f42.mp4?token=NQPrCC5It4CnvgO6WabqMuq0INZCh0_sPqRW-Keh2AW4z3GE8nsFtykbdwx7WD9xp7CmFETWgWyJUN1RULP0LniloSPB7Yl1zKCA8HY6Wkd05VZojx2Oi1cxszEG3yn_d6ETIYjm8prwvNEulkAfwXpFTYjY26x6BxwkUukmuI3L5Tf08YB4mnct09Qj9P9Wnsn1Y2jqlH8EjCZI0XfdNLBVkD0bH8EgLRdlIR21k1ER2pl5_5LuA5UoVKBrqGlspXsikM94-sNUc3I3S2fFfTptCf7GnYyugAHaj2xpNUHhRIxX1ppOMuAQJlxevZphEnK5L4SGUJJDNN9IeljnQRzQSc9BOZL-cpQABWqYsGp0SvbA_Qr2ko2ygVG5UcYE8qk2PBkJsbps6SyQ05B36GW7tILg6Tc_M_SNAVeAeduJEFe3yU4XWfAytQb_DI8muLEryqFSLmMXdXTzelqvFiQSZebK1bLyePn4S3GHTNf5yapzmpCwmUKY2yEmmFMmdMMgeIxSkxw9PCzul9ljiCglmylyceZNHFMXHraYRY0KEBJp_peIZ7KmJXqKpzoWxdxVy8jhiLLK65csoT8YWO0GlVneB17swDcPWgfiuB-UuFCmUv_2QeYQ_iC6dvXOGO0DikS0Sw6SvidSE9HWRfuqZznvClSPes-ZXn2jMH0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b62ce8f42.mp4?token=NQPrCC5It4CnvgO6WabqMuq0INZCh0_sPqRW-Keh2AW4z3GE8nsFtykbdwx7WD9xp7CmFETWgWyJUN1RULP0LniloSPB7Yl1zKCA8HY6Wkd05VZojx2Oi1cxszEG3yn_d6ETIYjm8prwvNEulkAfwXpFTYjY26x6BxwkUukmuI3L5Tf08YB4mnct09Qj9P9Wnsn1Y2jqlH8EjCZI0XfdNLBVkD0bH8EgLRdlIR21k1ER2pl5_5LuA5UoVKBrqGlspXsikM94-sNUc3I3S2fFfTptCf7GnYyugAHaj2xpNUHhRIxX1ppOMuAQJlxevZphEnK5L4SGUJJDNN9IeljnQRzQSc9BOZL-cpQABWqYsGp0SvbA_Qr2ko2ygVG5UcYE8qk2PBkJsbps6SyQ05B36GW7tILg6Tc_M_SNAVeAeduJEFe3yU4XWfAytQb_DI8muLEryqFSLmMXdXTzelqvFiQSZebK1bLyePn4S3GHTNf5yapzmpCwmUKY2yEmmFMmdMMgeIxSkxw9PCzul9ljiCglmylyceZNHFMXHraYRY0KEBJp_peIZ7KmJXqKpzoWxdxVy8jhiLLK65csoT8YWO0GlVneB17swDcPWgfiuB-UuFCmUv_2QeYQ_iC6dvXOGO0DikS0Sw6SvidSE9HWRfuqZznvClSPes-ZXn2jMH0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
مهدی تاج: سهمیه ما برای سال آینده 3+1 است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/140915" target="_blank">📅 15:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140914">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇵🇹
نشریه رکورد پرتغال : محمدجواد حسین نژاد در آستانه انتقال به ریو آوه قرار دارد
💵
مبلغ انتقال : 1/4 میلیون یورو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/140914" target="_blank">📅 15:11 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140913">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
❌
تاج: آزادی باید مسقف بشه؛ شرط AFC!
❌
❌
حالا سؤال اینه؛ سقف‌زدن آزادی چند سال زمان می‌بره؟ ۲، ۳ یا ۴ سال؟ وعده آذرماه هم که ظاهراً منتفی شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/140913" target="_blank">📅 13:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140912">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‼️
دهقانی ناظر AFC در امور استانداردسازی استادیوم‌ها
✅
باید ورزشگاه آزادی را همانند نیوکمپ بارسلون مسقف کنیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/140912" target="_blank">📅 13:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140911">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9db93cfbe3.mp4?token=H6vqkxJ4CrUvCfE7RJFiWLz-qRU3l-NBc5rt4FZAJCp_eDf4nQiYJatKR0NimdwY7Kdv1QzjXTqm42ByTIiI9RqMgLTo5mEUij_VCutLWzhPw_yBg80wf2J0D-P5O-J1mVq7gTxMBsC-PQ5YdUAy4X_-yY0J5-OXQh_vFd1PFG_KlEvtPTOZrXMv9Gv-11LN071cxRvxL7kKJBmy-IvNdFx8u3_4r08CI8HZdTxWyHUzSRZoF7fI0ZCDkQwGxUuqK6ZaPvVSor-Fb80m9qCEW6jnvW8mRx6CcOUpR1fanmGyeBWzHriY1nGtbYSNsrTFyjYj8W7nhw2EIh4M6BXKtEZ2HdBPVKSyJ5s-5Kyb4Uqs5qwaL0LpJg9_dUo_X3hjvSmw_8aJ-ngS6nxokQHWhcIaDPI22f29BmsfwwtgsbE_tPmcgzlDU5UvketdpwjnCNQpSFyR3S7TmcqCVtX3Jns4X_jwYmAyGb8iLKerp2oM5ChGxL7fVfzQv6Fjj7YqJ5ukrWQRxfTPhMUd6d3_aapdM5zgSWb0kMYDZN3yJlngiBcThGOJM-N8y2Nzx2nh7fMlLb40RiTOrOr6oSaf2_8JP2RjWGB05746wyXHDeXR2kYwCTFA7sg4ESAPDLxkG2MzILnn2qtqNjGLow4CD2GBNPYMquo3FDxzhB-a35E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9db93cfbe3.mp4?token=H6vqkxJ4CrUvCfE7RJFiWLz-qRU3l-NBc5rt4FZAJCp_eDf4nQiYJatKR0NimdwY7Kdv1QzjXTqm42ByTIiI9RqMgLTo5mEUij_VCutLWzhPw_yBg80wf2J0D-P5O-J1mVq7gTxMBsC-PQ5YdUAy4X_-yY0J5-OXQh_vFd1PFG_KlEvtPTOZrXMv9Gv-11LN071cxRvxL7kKJBmy-IvNdFx8u3_4r08CI8HZdTxWyHUzSRZoF7fI0ZCDkQwGxUuqK6ZaPvVSor-Fb80m9qCEW6jnvW8mRx6CcOUpR1fanmGyeBWzHriY1nGtbYSNsrTFyjYj8W7nhw2EIh4M6BXKtEZ2HdBPVKSyJ5s-5Kyb4Uqs5qwaL0LpJg9_dUo_X3hjvSmw_8aJ-ngS6nxokQHWhcIaDPI22f29BmsfwwtgsbE_tPmcgzlDU5UvketdpwjnCNQpSFyR3S7TmcqCVtX3Jns4X_jwYmAyGb8iLKerp2oM5ChGxL7fVfzQv6Fjj7YqJ5ukrWQRxfTPhMUd6d3_aapdM5zgSWb0kMYDZN3yJlngiBcThGOJM-N8y2Nzx2nh7fMlLb40RiTOrOr6oSaf2_8JP2RjWGB05746wyXHDeXR2kYwCTFA7sg4ESAPDLxkG2MzILnn2qtqNjGLow4CD2GBNPYMquo3FDxzhB-a35E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دهقانی ناظر AFC در امور استانداردسازی استادیوم‌ها
✅
باید ورزشگاه آزادی را همانند نیوکمپ بارسلون مسقف کنیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/140911" target="_blank">📅 13:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140910">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETrUCwrRPRDGSLiVXrQGhb43DFtOD91KqvH8dgVIYnoH6GPOeL1O5zV4HXgxTCQ6dhWk-VNZrGXP7xMhvf5HVx-Ml9kIkLWRb6o0KIcz8Hxm0jMrB10cVRqvkkEcB5-kGg85JbxkAtOyh4hax-FCYjfi6kbtKPCPzyFpIccQX7tTezz06XR4tufb4KekNFeuQw-Oqb1BGqxwy30wjQTsavKONmDFEGMJsWGXQ-mm7PrKCdGNdBfAffl14IjpBiw8vbO7jExyh6Mhuh7LWmUNEjuv_MPV39tJk0mKbbGp7qPBnkkHWDpMsvknZ3txtE21LCxTGTtqRAZutUK556dcHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نبرد سلسائو با وایکینگ‌ها؛ پرتغال در برابر نروژ، یک شب پر از هیجان!
🔥
⚡️
[
پرتغال
🇵🇹
🆚
🇳🇴
نروژ
]
⚽️
پرتغال با تکیه بر مالکیت توپ و کیفیت بالای خط حمله، معمولاً مقابل تیم‌های فیزیکی هم موقعیت‌های زیادی خلق می‌کند. نروژ اما با قدرت درگیری، انتقال سریع و تهدید دائمی در یک‌سوم هجومی می‌تواند بازی را برای سلسائو سخت کند. سناریوی محتمل، بازی نزدیک در نیمه اول و افزایش موقعیت‌ها در ادامه است؛ گل در هر دو نیمه سناریوی جذابی به نظر می‌رسد.
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
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/140910" target="_blank">📅 13:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140909">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
تارتار هنوز به یاسین سلمانی امیدواره
🔻
مهدی تارتار این روزها تمرینات ویژه‌ای برای یاسین سلمانی در نظر گرفته و قصد دارد این بازیکن را دوباره به روزهای خوبش برگرداند
🔻
گفته می‌شود تارتار به اطرافیانش گفته اگر تا پایان نیم‌فصل اول نتواند سلمانی را به شرایط…</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/140909" target="_blank">📅 13:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140908">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpKTR8z34S2GMNxPVh9VZaMS9ZGy5pNwSU5Vis9sDKkt4uAdD8Pj3Lzj2H-DMw7nP__fB5FbvrWJGR6adnbuWR1rslyfOGTBSccZjm33mXEGuoCNZ4dHMVZHOXeQTpba4F1_ebGe7cpn6l-7VYRubWvBzG2mYbqp5aANfrZj5V1KzvSrGG5Dni0OkvM6qCPIInBn1ApJJI6v5pvGDT1eYc69Qw4ARudSJe4oWhMBhfEtEo1M5VYe_oiq6wo3P1fMNhJJYcl8uEHb7C4QVS0c0l5RXSrs02LePgmyzmEezSry27z4Qrn7ZUh3WPPKO9i62QrrvbpBG0T7E2FUOI-Z1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
باشگاه پرسپولیس طی روزهای اخیر درگیر تمدید قرارداد سه بازیکن مهم خود یعنی نیازمند، اورونوف و کنعانی‌زادگان است که تاکنون موفق به توافق با دو نفر از آنها شده است که اون نفر باقی مانده اورونوفه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/140908" target="_blank">📅 13:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140907">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">⭕️
❌
❌
❌
❌
ادعای برگ ریزون یه خبرنگار ورزشی: یه زن اعتراف کرده که باهمخوابی باچند داور برخی اتفاقات فوتبال ایران را باآنها هماهنگ کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140907" target="_blank">📅 10:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140906">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
حمید ابراهیمی خبرنگار ورزش سه: یه معاوضه دیگه بین پرسپولیس و گل گهر شکل گرفته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140906" target="_blank">📅 10:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140905">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvsRSo8ord7u9475VA4A4l_yRQ86m0LQsp7nf4VPqPYnMprVrCckSaiC58oeLkAnH_M_zT9d7zu55TS04smnzejYF0crZIz0KpVSZqBv-P4bNJGMWeZIa6fatfLxuqTvnkPNN8Ub6vCD5o4wZIU65xWm-ijkVKESZp8u9r8si7r-c0cj_WQux78ZSxh6PorqflmlTzfb64v6nP2sUq_wyIQ6hsQubN4z6aFObmNGJJju-UsAP68EQlu-V-XMfb62BMtll2xLCd23n0wF8inay_UOsxsZPYqY80QwlnmDsgu5_zgTfYG_6SJE1rzZtpqvZzT9kTtZmKFgZBDFtDu7tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇮🇷
بازی دوستانه تیم ملی که قرار بود در مقابل تیم‌های گینه استوایی یا گینه بیسائو برگزار شود به دلیل محدودیت پروازی و غیبت بازیکنان حریف لغو شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/140905" target="_blank">📅 10:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140904">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✖️
✖️
پرسپولیس امروز استراحت داره  و از دوشنبه تمریناتش شروع میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/140904" target="_blank">📅 10:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140903">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pAzhteIX_E-5ljSn_cmQnUmaBcwFy-fpaEgZHE_lQBwncSgleDIsUHKUYyYaIfYhdRVNETAESwbj5E2BLNWHyAzBh0XXVnT0tGtpaaGTHO0wd4dLRk7wuEXgl4ZGVuzVFqZV_mI5GVisouAKzuux247KPTGdPCAhITjI11kk22YyUkTtAWki0DgEoulVMFhDZKVpIAYhkms91vZ1cg_-oJ7wkYrWziOBhAdHcyc5SxMstLtkHz6Y0Syljtvrk30ZTJ6rcgGLOFqN6iLtqU5TlD7myG3o5ehoYh3x0GzCbbgVGFR7Atr0Gf5QNG-Usml7GJRQGqZ0VCiLm5IblVmiCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
✖️
پرسپولیس امروز استراحت داره
و از دوشنبه تمریناتش شروع میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/140903" target="_blank">📅 09:11 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140902">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">⭕️
بهترین لحظات پرسپولیس در لیگ قهرمانان آسیا در سال های اخیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/140902" target="_blank">📅 09:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140901">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQSfGN3_i5V0PhiQcRaJ2EwcXuFhwHDkN8tu2Tkn8XXBRjUehNCVQCH8T8SQ417mEpz5ZftyAbKnzJOBfAoSodEoVEatg9JMQj5svFb05M95GscWFGB1nn6qWVZFdaJCr4IrzYaNokAuC4XTziVgcJHFWxRjvpqbCVys7mYSrHZPbtRT9ExFtjrsud3w7Aotx_2X6gXmiBBUNJE9tICnm09YiVNtXAgQ0Ku3v7y4Z9wcXRgYuEn2aW5pvKJ6P0oHNMDbUoLUBvB7NB5SbSMMiSjYeDzycuqZ1iOozUsAt-6WGrVqht0h38XC7S-Q112gbcjKwsEX1eQt0zRqaJAa1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/140901" target="_blank">📅 09:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140900">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">■ دیگه دنبال لینک سایت برای ورود نگرد!
🔵
اسپورت‌نود کار رو از طریق ربات مینی‌اپ ساده و راحت کرده، به‌راحتی میتونید پیش‌بینی مسابقات ورزشی و بازی‌های کازینو رو انجام بدید!
🔗
فرآیند ورود به سایت به شکلی طراحی شده که کاربران بدون درگیر شدن با لینک‌های متعدد یا مسیرهای غیرضروری، مستقیماً وارد محیط اصلی سایت شوند.
📌
این دسترسی از طریق ربات رسمی اسپورت‌نود انجام می‌شود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
به جای روش‌های قدیمی ورود، این ساختار یک مسیر واحد و ثابت ارائه می‌دهد که همیشه قابل استفاده است.
📌
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/140900" target="_blank">📅 01:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140899">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
❌
دیدار تیم‌های زنان پرسپولیس و استقلال در ورزشگاه کاظمی با استفاده از سیستم VAR برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/140899" target="_blank">📅 00:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140898">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✅
از این پس امیرحسین محمودی در پست پشت مهاجم بازی خواهد کرد/ورزش‌سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/140898" target="_blank">📅 00:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140897">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❌
❌
دیدار تیم‌های زنان پرسپولیس و استقلال در ورزشگاه کاظمی با استفاده از سیستم VAR برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/140897" target="_blank">📅 00:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140896">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qN-csmevJaCX1sjEepOE-0Z8DGBSFH_gPy4F0zC_XCQS1YJpFwR2kMG6V56gD2GB318OwIdYA-5-xlhvv0h_hDN8qaosiA3oWDT_HdKg7_JDwSwk01vt-iHEz1JtDbwItTNiwaGapItqezrdwvT2jUxiofV4KHVtG0ArweoFZceCAnu6XKelQF3Xo6s4i5o6YaF6O0uYOIP3Dx-Je6ccXhF_eYMMQQm2kSpk0MlBbtWAj729Bc3VUwdz60xBFDRZRRNEIMu21D3kN7Wjf_3Q5VVjlS51UcvJTVX40BJGW45WAcyggrjRBc9EHzxVHqtsB0h5OoP_p-veoXrwJaxH2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⁉️
‼️
یحیی گل محمدی به دلیل اینکه باشگاه دهوک یکماه در پرداخت دستمزد خودش و بازیکنانش تاخیر داشته اعتصاب کرده و تمرینات تیم شو تعطیل کرده:))))
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140896" target="_blank">📅 23:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140895">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✅
✅
✅
احمد دنیا مالی وزیر ورزش:
✅
✅
فدراسیون های ناموفق رو حتی شده تعلیق کنم میکنم. این همه هزینه کردن که هیچ افتخاری کسب نکنن؟
✅
✅
گفته می شود حکم اخراج قلعه نویی توسط وزیر ورزش صادر شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/140895" target="_blank">📅 22:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140894">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🏆
🏆
اشک شوق قهرمانی و معافیت از سربازی
❌
❌
بازیکنان تیم امید کره جنوبی چهارمین قهرمانی متوالی این کشور در بازی‌های آسیایی را رقم زدند و این قهرمانی برای بازیکنان کره به معنای معافیت از خدمت سربازی ۲ ساله بود تا این گونه اشک از چشمانشان جاری شود
❌
❌
البته لازم به ذکر است که همه بازیکنان این تیم همچنان ملزم به گذراندن دوره آموزشی هستند، مسیری که سون هیونگ مین هم قبلا طی کرده بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/140894" target="_blank">📅 22:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140893">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
گفته میشه که یحیی گل محمدی هم یکی از گزینه های جایگزینی امیر قلعه نویی هستش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/140893" target="_blank">📅 22:08 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140892">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eG9jbwfat6uDMca3cz0BLpPjBQ4AG8wKHwM5F3j09IeNT8L7NbgRNHO0iTr3IsjJ0k1A5JhVJo4VThYqt6yuy6kl2Qk3f2cPPeMEc6cAuOyJ6gXhf1pjejKJR03O3Ci_J1Nia9gDeJ7M8nuFzb-gCt3eDD1stbftgtejmtQK8ez5rIxWeeSZ4zm_m46XkFVRunSARIZ0CNlZDr8_iEvE3Tcx_5YiQLv6Mca4qqAQ3IBF_m950wd3JnfpLEH9ifTiUFGsGCMLSSYJbnYsh4zkGrFVrzrGJzGRJyhGuyIJMzRVpozWnm2ALUS9a6P7I1gbNcYEllJon6QannNup0g96A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
محمدرضا مجیدی، مدیر ورزشگاه تختی: چمن طبیعی برای ورزشگاه تختی کاشته می‌‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140892" target="_blank">📅 22:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140891">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_LxP_DrAaZdW_0RHwKrLxI-N5OmQj7HBM74z0dKRskAc9oi5MXQr0dYEP3eMu2fJA8bneOJ8VN-V6e_F3O3tM-WNOz-zw8VjsaXxzsHvMIuM5hN2wnkpm92KwxA28o2UhLvzkmDzE2UGSTlYX87GNcr6y_FirdP1YnMrpM-KVsBkn-8P2oHn2RF_sel7LKIlzs7j0iqpVTInIdXYRnac3iezOcW0DQuuG5147VyXi9Qnf6ihOEIJnHAI28LNe4bP8PAUkutm2Tvitah5oBATl2HjVHe_519pB7_A75sLIaR8yz-ifHELA4ZEqh0vQAQGVU6tnSVHoUQigY8CtPFDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
یک قدم تا سومین برد؛ لاروخا آماده‌ی شکار!
[
اسپانیا
🇪🇸
🆚
🇨🇿
جمهوری‌چک
]
⚽️
اسپانیا با ۶ امتیاز و ۷ گل در دو بازی، شروعی کاملاً هجومی داشته؛ چک اما فقط یک گل زده و هر دو دیدار را واگذار کرده است. میانگین مالکیت اسپانیا حدود ۶۳٪ است و در ۲۰ بازی اخیرش به‌طور میانگین ۲.۶ گل زده؛ در مقابل میانگین ۱.۶ گل برای چک ثبت شده. اسپانیا در دو بازی اخیر خود پیروز بوده و لامین یامال در هر دو مسابقه گل زده است. با توجه به حجم موقعیت‌سازی و اختلاف آماری دو تیم، سناریوی بازی می‌تواند برتری اسپانیا همراه با حداقل ۲ گل باشد.
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
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/140891" target="_blank">📅 21:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140890">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">⚽️
🔻
علی علیپور بعد از سپری کردن دوران مصدومیت به تمرینات گروهی پرسپولیس بازگشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/140890" target="_blank">📅 21:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140889">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
❌
۲ گزینه پرسپولیس برای لیگ دو
✅
✅
پرسپولیس بعد از ناکامی در راه‌اندازی تیم «ب»، حالا دنبال خرید امتیاز یک تیم لیگ دوییه. پادیاب خلخال یا شایان دیزل شیراز در صورت توافق، امتیاز تیم به تهران منتقل میشه و زیر نظر پرسپولیس فعالیت می‌کنه.
✅
فارس
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/140889" target="_blank">📅 20:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140888">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwBgtU9NKbq659OTY21liDseJ_avEbQkotNEs1lV-LThZFsuh11AcdbENwfHiEQDcWw3f8YS9SHfD11L5LZJ1fVNaW6a_3toTM8ihGvTVuHVYadWQNbQWu8ElF7U001EBJnTjrE0d15JEFof1YXd_0RQoZatkm8oGWIYNpHUeUvm8LJVb8whQxDwf4wfMPPkVehg8EQfaQCms3QM3XVd-S--KydJqPIx-Eq9wvp48TNv5v_RvcSvw_Fo5__z2emgcxivma_CyBW23lh6yecgIuTJDWAsZgfswY-Ak_86xJc3k-tgHFkRi4qVn-6Zu3jvc7F6A6jFhP1v8C3pSvf2mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🔻
علی علیپور بعد از سپری کردن دوران مصدومیت به تمرینات گروهی پرسپولیس بازگشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/140888" target="_blank">📅 20:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140887">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✖️
✖️
محمودی و صادقی کماکان از آماده ترین بازیکنان تمرینات پرسپولیس هستند
✅
✅
هر دو به همراه زارع در دفاع از بهترین های بازی دیروز مقابل گل گهر بودند.
✅
✅
باتوجه به مصدومیت ها به احتمال زیاد این دو بازیکن در بازی های آتی برای سرخپوشان به میدان خواهند رفت.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/140887" target="_blank">📅 20:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140886">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">⭕️
⭕️
بخاطر کمبود گاز ، از اول آبان به مدیران ابلاغ کردن کلاس ها و مدارس غیر حضوری و مجازیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140886" target="_blank">📅 18:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140885">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">⭕️
⭕️
بخاطر کمبود گاز ، از اول آبان به مدیران ابلاغ کردن کلاس ها و مدارس غیر حضوری و مجازیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/140885" target="_blank">📅 18:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140884">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/140884" target="_blank">📅 18:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140883">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✖️
✖️
شنیده میشود که رای کمیته استیناف نیز در پرونده آسانی تایید رای کمیته انضباطی بوده و پرسپولیس موفق به محکوم شدن این بازیکن نبوده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes ﻿</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/140883" target="_blank">📅 18:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140882">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
⚽
طرفداری: پرسپولیس در آستانه‌ی تیمداری در لیگ دو و شهر مشهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/140882" target="_blank">📅 18:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140881">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔹
بغض محمد عمری درباره شروع دوران فوتبالش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/140881" target="_blank">📅 18:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140880">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UItDD2PRfe-m4-QDd63G2BHR49qGmqTGgdv1z4wilJFhxvFIEG3Si-ck4-pzfoVI9ea1Nvr6Hv0NAb1sdIyNmQ9LJWJpFAGf901URZQjn7KpQtBPMgZo56WfatkVcnTFkmvIljv3BlFAUbHdAlSJygT_SEGTL9Kknns5sDGrmrDwfwuntxELJrPnvD4gxHvCZPnpjZUjgY56ukrMtgtRPFo5Sxj-x1pstPjcMwpz09W8RW7Jk4-pcJAtIl0tDWxVxis2hyyRStPMgvQkP0QMiWSonrGskaFdfGD3zscRDQBg5X47gWzpQrdROwcgq0CIMltwcGFkvJN1GrPlnXhO0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
کاروان ایران با 19 طلا، 18 نقره و 15 برنز و کسب مقام‌ششم مسابقات آسیایی ناگویا رو تموم کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140880" target="_blank">📅 16:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140879">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✅
رامین رضاییان 2 ماه به دلیل مصدومیت از میادین دور خواهد بود.و پنج بازی آینده فولاد و از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/140879" target="_blank">📅 16:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140878">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
اورونوف با بهره‌گیری از تعطیلات فیفادی به اوج آمادگی رسیده و اکنون با بالاترین کیفیت در اختیار مهدی تارتار است.
😀
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/140878" target="_blank">📅 16:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140877">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wzq1yYE5hTv9KnkVnXYxbEooJBC4gHsuYCvrcvChTxx1oqyQXF4h1Jh68dGJdH8wIs8TJVzmanvx3C0029SsSzdY_vyKxbuK384wM8PlUvGA87wcCurbbetXqC-baSIEJVMBVFCC2G4tz-W45PmsE6va8DwrwKvnDahVZm42TGLZoxy3Jsp7uEKee-Z20IBMqBMn9B4TL5Z2Bdkk2SJKPZE63xs7biIN_O5_XyHn58a6XAaqSgV5HHFg7-dEVHGil3b8iPBk-NVjkO2t6oU0JFt8rW1M-lUkromFw6L-zXxfVtAp6S57veGJlJgc0EEx1I-xaXXneJT4X_sD4wNFaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
SPAIN -
❤️
CZECHIA
⏰
Tonight 22:15
🏟
Municipal Carlos Tartiere
🇪🇺
اسپانیا با ۹ برد متوالی و پیروزی ۴-۱ مقابل کرواسی وارد این دیدار شده؛ یامال هم با دبل اخیرش همچنان مهم‌ترین تهدید خط حمله است. چک بعد از شکست ۲-۰ برابر انگلیس و اخراج پاول شولتس، از نظر نتیجه و اعتمادبه‌نفس شرایط متفاوتی دارد و مقابل مالکیت و پرس اسپانیا احتمالاً عقب‌تر بازی می‌کند. احتمال می‌رود اسپانیا کنترل و فشار تدریجی روی دفاع چک بگذارد؛ اگر گل اول زود برسد، بازی می‌تواند به سمت برد با اختلاف و کلین‌شیت اسپانیا برود.
🟢
با درگاه بانکی اختصاصی و امن وینکوبت، حساب کاربری خودت رو به‌صورت مستقیم شارژ کن و مثل هزاران کاربر دیگه، بدون دردسر از امکانات وینکوبت استفاده کن.
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
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/140877" target="_blank">📅 16:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140876">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/L-T1XLcFVGVlIrcEKuoeTdhdMV4A9yF4fSDR39ckFDjVQKgtpIjRawN0_KP3ZF1MkGwxfMKpCqlhpHiBS0OEXOSIexm8RXhHx-gUzxOcrQ7rXJr9ut8x3br7g6yLXSOT3IUiruhOkJ4C72WLO9XcsSDOhKzSNV1Mw8ywPhxS4BjPz-h4SlpHZEC8dp-kMyB2F-86Z8MjTqYH4X0TkZM-IOHEpvjqzB4Yr6pkTvfhRlno5Sgh-UbCPxStYhORniNta9LldSEIYA4xbA5TH0RSymB7n8MjBMr0K4FSzXNQGjCiGLahSRx1xbBsiCuHMVpGxctlINtIhpnDzwP0pY2YJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
تیم ملی والیبال ایران با غلبه بر تیم ملی ژاپن مدال طلای بازی‌های آسیایی ناگویا رو به دست آورد
ایران ۳ - ۱ ژاپن
🇮🇷
۲۸ | ۱۹ | ۲۵| ۲۶
🇯🇵
۲۶ | ۲۵| ۲۱| ۲۴
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/140876" target="_blank">📅 15:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140875">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
خلاصه بازی پرسپولیس و گل گهر سیرجان
✅
پ.ن چه کاشته ای زد یاسین
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/140875" target="_blank">📅 15:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140874">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
❌
والیبالیست‌های ایران به فینال ناگویا رسیدند
🏐
تیم ملی والیبال ایران در نیمه‌نهایی بازی‌های آسیایی ناگویا با نتیجه 3-0 پاکستان را شکست داد و فینالیست شد.
🇮🇷
25 | 25 | 25
🇵🇰
13 | 15 | 11  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/140874" target="_blank">📅 15:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140873">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
❌
غیبت عالیشاه برابر پرسپولیس/ ستاره سابق سرخ‌ها کجا بود؟
❌
امید عالیشاه در دیدار دوستانه گل‌گهر و پرسپولیس نه در ترکیب تیمش قرار گرفت و نه روی نیمکت نشست.
❌
❌
گویا عالیشاه در ورزشگاه حضور داشته و به دلیل مصدومیت جزئی در رختکن در حال گرفتن ماساژ بوده است. این…</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/140873" target="_blank">📅 14:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140872">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✅
عالیشاه امروز اصلا نزدیک نیمکت‌ تیم نشده! و هیچ سلام و احوال پرسی با هیچکدام از بازیکنان و کادرفنی پرسپولیس نداشته!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/140872" target="_blank">📅 13:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140871">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
خدابنده لو: ارونوف به من گفت در ایران فقط دوست دارم برای پرسپولیس بازی کنم.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/140871" target="_blank">📅 13:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140870">
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/140870" target="_blank">📅 13:28 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140869">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZfvWymNbJzPFmEeSfeLbqUvJpY9BukyITgnY9oq5ukBQHmQ7hGOez3P2kflD3ao2CswYWT9Saa2j4tdGrypMemGqMngogW_rHLi11B5co4eY312o0xOzMvtTnktUhbjYBtBb4tNboVNnGhAB_5XyFXmludOtGoym-cZEKUdBJOnpk3DrIFdjsfVD79R6xc2aJwaB2_AbSQ53X9SaIYTeZ_am_GqyNuUyLRfuoMpV64Ab8UQfwgL8gkUYP9cwsIInNNjcoI9Mq9MqK8TrdEXH-1aSPnoAhn45yQrFP_WtDbKCWNp6PcQeBTDEvgD7SKLb_MLv4JJ1iqQdpNzxskVFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇱
زمان بازگشت قلی‌زاده به میادین
◽️
بر اساس پیش‌بینی کادر پزشکی باشگاه لخ پوزنان، قلی‌زاده می‌تواند پیش از پایان سال ۲۰۲۶ و در اواسط آذرماه دوباره به میادین برگردد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
﻿</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/140869" target="_blank">📅 11:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140868">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBKR9fS9gUWT6rZuqNsDZ6ma3SX-o1vUaDHElsHPToI93MFokWayMcZCQ8i88-fb1H2l6GRSF9T-Q_sQJAB60xfQRHltX92l8hKCo85xxtMIvZwLFEHQdGZrRpYYu4IoM98dMaN31OD6-IWp5zsqkhaNzyirQ8dnktU3IDKfZqtN9ihpMHkfw7ftjV8TzTxtBQ0sk4iwcPrO7yiZJSOl15o5obq_q_BM1TU1LVLHDBRijDB_pNjyS7jxuZCATUlhTQO-x5xfLjDqViR2vGqCnN_whyF2IE-7CFHuEdkn7et0VaeX-Qv4AQ7chhEnNH13j2CsewnH2nN2ucS6I0EoVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری از ورزش سه
🚨
زوج خط حمله پرسپولیس مقابل صنعت نفت آبادان رو ایگور سرگیف و پوریا شهر آبادی تشکیل خواهند داد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
﻿</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/140868" target="_blank">📅 11:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140867">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">⚪️
⚪️
محمدحسین صادقی امروز علاوه بر گلی که زد، عملکرد درخشانی در ترکیب پرسپولیس داشت و ممکن است در بازی‌های بعدی لیگ به او بازی بیشتری برسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/140867" target="_blank">📅 09:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140866">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
#شایعات
✔️
هیئت مدیره پرسپولیس به سازمان لیگ اعلام کرده که در صورت اینکه نتیجه دربی 3-0 به سود پرسپولیس اعلام شود از بردن پرونده آسانی به دادگاه CAS صرف نظر می‌کند، در غیر این صورت این پرونده‌ به صورت رسمی با تمام مدارک به cas برده خواهد شد
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/140866" target="_blank">📅 09:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140865">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✅
✅
✅
گرا: از پرسپولیس نمی‌روم؛ از زندگی در تهران راضی‌ام
‼️
✅
✅
گرا در در گفت‌وگو با «Nemzeti Sport» درباره مصدومیتش گفت پس از مشکل کف پا و انجام MRI و تصویربرداری، شرایطش بهتر شده است. او درباره شایعه جدایی از پرسپولیس هم تأکید کرد یک سال دیگر قرارداد دارد و…</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140865" target="_blank">📅 09:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140864">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fl8f0kJ7bt2NTLxjWk8jSY299cjhAWpqtjh_3jWTVrht0ADFJYyOPc12LAKgQfOwTXVJGo20uGkqexIIcJEsGmhvZh5yNhMw4Rb3iBf6peZPisPEnmnAu5jbZ_8X2fyk_WuwbfoLF4joEKe70xvoRzHJxROjUZQsgCViaQUH9r5lBLpyCqFSz1L8JsxF3M28m8OyRToav2-D5xPt9yeOEEssKL5KvOLpN6LDbSDmiq6a7Dk_mhtRQZLU-QkzeXfC0BrIclwh6nX420qGwlXuqN1UNtZrMRRGBfEuBZx0IAqaJjckMM15Fs12xIam2g8PuTrFhnMLX7Wr1tNyhwVWyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140864" target="_blank">📅 09:01 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140863">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQDQzE4CwJ99KoWAvbJWhPrs7GoEIqRa9_yM3a3YmcHlqAM8fLdCrpGbGEUilX0kkewnKyX3aPQ8gTLNqP1Y5ZECmmDuSQEJcJovBXKOh3ZcdYqzKwckl8OOmvpX0WzdKruxTkvhlz9t2ZFKPjs37gHrfgFxq1nIff3N_udQ2JMlehXnnmqIFNM7CB5qaxMZJzMDoiNf2aJzc5AHwFpryZ2__5CLkBlGFOXmQIBVBYLHx12WbT563B7ppWJcGB2S_z11WKa_XmheZ5ApRtWWJdLi7T8Z3sxnwfUvtjRIdqDdQPGSY3Fh3c8Wtu_GVM2iVQIFT68AGLyaZgkr4QJOJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
CROATIA -
❤️
ENGLAND
⏰
Saturday 19:30
🏟
Stadion HNK Rijeka
🇪🇺
کرواسی برای کنترل بازی روی مالکیت و گردش توپ در میانه زمین حساب می‌کند، اما انگلیس با سرعت بالای انتقال و کیفیت نفرات هجومی می‌تواند در ضدحملات خطرناک باشد. تجربه و کنترل کرواسی در کنار قدرت هجومی انگلیس، این مسابقه را به یک نبرد نزدیک تبدیل می‌کند؛ احتمال موقعیت‌سازی برای هر دو تیم بالاست و گلزنی دو طرف سناریوی جذابی به نظر می‌رسد.
🟢
با درگاه بانکی اختصاصی و امن وینکوبت، حساب کاربری خودت رو به‌صورت مستقیم شارژ کن و مثل هزاران کاربر دیگه، بدون دردسر از امکانات وینکوبت استفاده کن.
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
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/140863" target="_blank">📅 01:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140862">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
❌
مجتبی فخریان بصورت قرضی راهی گلگهر شد تا پوریا پورعلی بصورت رایگان به پرسپولیس بپیوندد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/140862" target="_blank">📅 01:02 · 11 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
