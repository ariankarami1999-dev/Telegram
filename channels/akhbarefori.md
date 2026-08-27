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
<img src="https://cdn4.telesco.pe/file/lZuoBlfAi2vicrpRTgTukgYGZWN1UyDdqGYZ1xkX7d5h5mdmTkA_fpeCI_J01zEMk-EshWclVeeB5RK-Xmleaf_izgLoC7wEMKLEvB_FLPjvh07UpFtkMECYn0MssdmLZ23Ag7wCNc5LtHBNxlOBNK-kw9HBiQedxwiqnJaxylMsAXx0mKBjLkTu8SnbYh2nWZjpn3sIwoWFFz0MeN5iOSbpLNjpBGO9_54AkQHY6NIF3emsu0fiBgKVqpxWsDF50X3h3lJ7npEGMLem74yNco8Nu_-WC4J4YSWKrMMD80QMP-DvvbwHr7GZkHHvABNngl20FC3rWEwpp4Mtlax_iA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.37M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-05 20:40:41</div>
<hr>

<div class="tg-post" id="msg-684805">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fo6rKswkdZT1EMWzYqx5X9UXq6YDdFAFs8E00NPK8QAxDxAjRK-sbs_vDU3_q5_atqOUx1-aLJ2wEql6xVl08DjYcy-wxGjDTJK72MLoQecSYcj9YiHRA4nWKObfpmyWK8oSU_QfcCM52bU60leLLsFevfjDZabWOH5L6Zprzfq6-YcBLZTvhHN67VxkC3xP-0UceBzU6pV5ddjXBv_k1zUROPZaE3M9V8Qnmu0_LmAYQtoDclRXWpjiX_78iqcQL6BCJpT7o1jBC_b4TxwMyQXKkMnoH528kguMOAdEiOf0EgaDJwS3aUUwP3t2ZvKkcRPmyqFDdKMmSvFeFAkogw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فارین‌افرز: زمان آن رسیده که ارتش آمریکا خاورمیانه را ترک کند
فارین افرز:
🔹
دهه‌ها جنگ و درگیریِ نسنجیده، جان بسیاری را گرفته و ثروت زیادی را به خطر انداخته، در حالی که چیز زیادی به امنیت امریکا اضافه نکرده است. حضور نظامی واشنگتن به جای خدمت به منافع استراتژیک امریکا، باعث ویرانی و بی‌ثباتی شده است.
🔹
هیچ کجا این موضوع به اندازه کارزار علیه ایران آشکار نیست؛ این جنگ همان خطراتی را ایجاد کرده است که قرار بود از آنها جلوگیری کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10 · <a href="https://t.me/akhbarefori/684805" target="_blank">📅 20:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684804">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tr4kr3IXcZgE9ITFt4VDMtHoeK-ga6oh7UUt5Kg3d7dpwCJ4HP09eujclThRi2nXievCnot4jRFf4UPfrN5q29H0KdOoh7cW7gAWWfq9QwPRZDsTzHm8H3xJ4R5TswUI7ci91vMaZKyOfTVCxlp4EflnqkxA1RLAT2wu5WwDuxfJYl3Pzvbb2z1jimLcAN3dwXi9DPa0QiMB-8Op0IxB0rUMUzea85WT0fFCV5IwuGniIhSN6uKOTPn7ZxFcjMNKAKUJ31nWXFeaLI_CPxNlsVhYqT4SNoEXNMWm6Bd3rs6LKm9VgBe1S_YtenklyJsnD5Qzf8qd3ORAVr9BrYc9uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش قالیباف به گزافهٔ جدید وزیر خزانه‌داری آمریکا: تمام اعتبارت در معرض خطر است و امپراتوری آمریکا روبه‌زوال قرار گرفته است
قالیباف در پاسخ به گزافه‌گویی امروز اسکات بسنت با به‌اشتراک‌ گذاشتن مقاله‌ای از نیویورک‌تایمز که در آن به ناتوانی بسنت در کنترل شاخص‌های مهم اقتصادی اشاره شده، نوشت:
🔹
این امپراتوری روبه‌زوال به‌جای اینکه میلیاردها دلار را به تروریست نیابتی خود یعنی اسرائیل و ۷۵۰ پایگاه نظامی در دنیا سرازیر کند، می‌توانست آن پول را صرف مردم آمریکا کند؛ اما نه، این کار برای رژیم آمریکا زیادی منطقی است.
🔹
هی اسکات! مَرد[؟]! اعتبارت در خطر است. کاری بکن!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/akhbarefori/684804" target="_blank">📅 20:37 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684803">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
یک نفتکش کویتی در تنگه هرمز هدف حمله قرار گرفت
🔹
سازمان حمل و نقل دریایی بریتانیا (UKMTO) تأیید کرد که نفتکش کویتی السلام ۲ دیروز هنگام عبور از تنگه هرمز مورد حمله قرار گرفته است.
🔹
این سازمان مدعی شد که حمله توسط نیروی دریایی سپاه انجام شده است. این کشتی متعاقباً در جزیره توکل عمان لنگر انداخته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/akhbarefori/684803" target="_blank">📅 20:34 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684802">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d99d17b82e.mp4?token=YAyDXMXjxOr3XKc3AJ0jZ_tH7hN2f5To2ooXHBjnL91UgL2HNHswwj6YRooWaN_aLi545KWP9cpjfDoPNu1QqS58A9GMAGG-rqfWkykYoPbQtPIHQyasLIulkaQhVR3SprHjnLo29DGqU9p2nfUrjxYR8-JruWb0ZTysLi4ceI3OV6l2FyTAT1AasWsYryy1ffhRKVzwYhOXRTQt_b8kxNRP_ovaqwYYvXH_dvyIS-CH2B7-AVrKtU8b94JUWYgKDcdo17vMMC5fEVWWHnwTUeHqB0kcQkWPPWu38Xy6Fw9-gnLYhViCjLxCWIkHJPLWZLL_SAFDygRvI2hZ515VJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d99d17b82e.mp4?token=YAyDXMXjxOr3XKc3AJ0jZ_tH7hN2f5To2ooXHBjnL91UgL2HNHswwj6YRooWaN_aLi545KWP9cpjfDoPNu1QqS58A9GMAGG-rqfWkykYoPbQtPIHQyasLIulkaQhVR3SprHjnLo29DGqU9p2nfUrjxYR8-JruWb0ZTysLi4ceI3OV6l2FyTAT1AasWsYryy1ffhRKVzwYhOXRTQt_b8kxNRP_ovaqwYYvXH_dvyIS-CH2B7-AVrKtU8b94JUWYgKDcdo17vMMC5fEVWWHnwTUeHqB0kcQkWPPWu38Xy6Fw9-gnLYhViCjLxCWIkHJPLWZLL_SAFDygRvI2hZ515VJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سلاح ضد پهپاد جدید اوکراین برای مقابله با کوادهای FPV
🔹
این گجت جیبی یک پرتابگر تور است که تا ۲۵ متر برد دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/akhbarefori/684802" target="_blank">📅 20:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684801">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
حمله تروریستی به خودروی مرزبانی در محور مواصلاتی میرجاوه - زاهدان
پلیس سیستان و بلوچستان:
🔹
در پی اقدام بزدلانه و تروریستی اشرار مسلح به خودروی گشت مرزبانی در محور مواصلاتی میرجاوه به زاهدان، یکی از مرزبانان جان‌برکف، به‌نام استواردوم «علی حیدری» به درجه رفیع شهادت نائل آمد و یکی دیگر از همرزمان وی مجروح شد که بلافاصله توسط عوامل امدادی به مراکز درمانی منتقل و تحت مداوا قرار گرفت.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/akhbarefori/684801" target="_blank">📅 20:24 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684800">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
وب‌سایت عبری‌زبان «واللا» به نقل از یک منبع امنیتی گزارش داد که اسرائیل رسمیت شکست طرح خود برای ایجاد مناطق آزمایشی در جنوب لبنان را پذیرفته است
🔹
اسرائیل از طریق کانال‌های امنیتی به آمریکا اعلام کرد که طرح ایجاد «مناطق آزمایشی» در جنوب لبنان با شکست مواجه شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/akhbarefori/684800" target="_blank">📅 20:21 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684799">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b193111727.mp4?token=vtT-lQ9Zbbtad2y4xADcNrOcxgDK9zDOm3Zvj8_LlwWcMfELBnFw9u0UvhzH8qKHr_HL8UY5jEVhnR74G4N4Qo58EbGPZEj3ZDb6Uu_w8EhnR5xkwvEedOUGHc4EF2LeaSjFh40SGst0mBlC7fnZPcgLgz_-J4Zh006gElAk5SrqQD4saxGxjkfkOKJsVWmhMp07y9Xc5qnjuqm2mnQh8osY7epeIdjDzGZT5Hz96OGeGUZ94iJCT4p-oMJDwJd2K1zGhT5qLAUXGgYGzzRFAWkdbqvzs4HWL8HaNrAQJWXDMcNBvhjc2801y9lpXuB-VQR7Ug8vRQ7piezjQ1WqKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b193111727.mp4?token=vtT-lQ9Zbbtad2y4xADcNrOcxgDK9zDOm3Zvj8_LlwWcMfELBnFw9u0UvhzH8qKHr_HL8UY5jEVhnR74G4N4Qo58EbGPZEj3ZDb6Uu_w8EhnR5xkwvEedOUGHc4EF2LeaSjFh40SGst0mBlC7fnZPcgLgz_-J4Zh006gElAk5SrqQD4saxGxjkfkOKJsVWmhMp07y9Xc5qnjuqm2mnQh8osY7epeIdjDzGZT5Hz96OGeGUZ94iJCT4p-oMJDwJd2K1zGhT5qLAUXGgYGzzRFAWkdbqvzs4HWL8HaNrAQJWXDMcNBvhjc2801y9lpXuB-VQR7Ug8vRQ7piezjQ1WqKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جشنواره تخفیف‌های ۷۰ درصدی برج میلاد را از دست ندهید
🔹
از ۳ تا ۱۳ شهریور همزمان با ولادت رسول اکرم (ص) و امام صادق (ع) و آغاز هفته دولت
بلیت های بازدید از طبقات برج میلاد: ۷۰ درصد
مجموعه فرهنگی و صنایع دستی هفتا: ۱۰ درصد
زیپ لاین: ۵۰ درصد
کارواش: ۲۵ درصد
سینما گیم: ۵۰ درصد
سرزمین افسانه: ۵۰ درصد
شهربازی (چرخ و فلک، ترن و کشتی): ۵۰ درصد
کاربازیا:۲۰ درصد
رستوران ها و کافه ها: ۲۰ تا ۳۰ درصد
بازی‌های هیجانی : ۳۰ درصد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/akhbarefori/684799" target="_blank">📅 20:19 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684798">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
هشدار جمعیتی؛ تا دو دهه آینده ۳۰ درصد جمعیت کشور سالمند می‌شود
🔹
در ۶۰ سال گذشته، جمعیت سالمندان ایران تقریباً دو برابر سریع‌تر از رشد کل جمعیت کشور افزایش یافته است؛ روندی نگران‌کننده که زنگ خطر آینده جمعیتی ایران را به صدا درآورده است.
🔹
پیش‌بینی‌ها نشان می‌دهد تا سال ۱۴۳۰، شمار سالمندان کشور به حدود ۲۸ میلیون نفر، معادل ۳۰ درصد جمعیت ایران خواهد رسید؛ یعنی از هر سه ایرانی، یک نفر سالمند خواهد بود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/akhbarefori/684798" target="_blank">📅 20:17 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684797">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
صدای انفجار در اربیل عراق
🔹
منابع عراقی از حملات پهپادی به مواضع گروهک های تجزیه‌طلب در منطقه سوران در اربیل خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/akhbarefori/684797" target="_blank">📅 20:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684796">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">06 Ane Manaee (1403-08-17) Marghade Sheikh Sadoogh</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/684796" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه ششم
حجت‌الاسلام امینی‌خواه:
🔹
عمل در آیینه هستی؛ تأملی بر جایگاه و معنای آن [8:33]
🔹
در جستجوی قواعد غیب؛ تدبر در آیات قرآن چگونه ساختار هستی و انسان را آشکار می‌کند؟ [12:53]
🔹
اعتباریات و اراده؛ پرده‌برداری از بایدهای پنهان در رفتارهای ساده [24:28]
🔹
ضرورت و کنش؛ چرا هر اقدامی ریشه در ضرورتی ذهنی دارد؟ [31:23]
🔹
دینِ بی‌دینان؛ همه باوری دارند، حتی آنان که دین را نفی می‌کنند [34:10]
🔹
زیارت یا سیاحت؟ وقتی نیتِ دوگانه، خلوص عمل را مخدوش می‌کند [42:40]
🔹
خدای ناپیدا، خدای واقعی؛ آنچه به تو انگیزه حرکت می‌دهد، خدای حقیقی توست [44:03]
🔹
داستان حیرت‌انگیز کاظم؛ از شکنجه حاج آقا ابوترابی تا شهادت در حرم حضرت زینب (سلام‌الله‌علیها) [57:51]
🔹
آن‌ هنگام که کنیزان یزید ملعون در پرده بودند اما حرم رسول‌الله در میان خارهای نگاه‌ حرامیان [1:09:06]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/akhbarefori/684796" target="_blank">📅 20:08 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684795">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
سرلشکر محسن رضایی: آمریکا شرارت کند بلایی سرشان می‌آوریم که در تاریخ ثبت شود
دبیر شورای عالی امنیت ملی در دیدار با وزیر امور خارجه دولت قطر:
🔹
ایران به قطر در روزها و شرایط سخت کمک کرده است و بر دوستی و برادری بین ۲ کشور تاکید دارد.
🔹
ما به آمریکا بی‌اعتمادیم و آن‌ها بارها به دیپلماسی و مذاکره خیانت کرده‌اند.
🔹
آمریکا باید ابتدا اقدامات عملی در جهت انجام شروط ایران انجام دهد و پس از آن ایران اقدام به بازگشایی تنگه هرمز خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/akhbarefori/684795" target="_blank">📅 20:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684794">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f9cc60ceb.mp4?token=uQBwS8DbEYcZvs74wCPK4YlEYWHmcuup2AMuFdCdi6QOydVU806jV_7gkKvlxOG9JG8AAWkCjn8qTWaqlbr7ZDoMbVgdgzOLj0riEg9xyvTFYT2iXWG8Jmb2IZ4A9YgPdICm2oc3ZGXsgWP5OfEb_kAySWWCEQAfpSd92mckI6OyjnlS6xPh5YUwLa3c7j89dJw4ZGmNDqRfu50ADNPZTfxtyxdVAnqGtybudfAUmYCtwEQ0tQJxL-GnCzupL7UNzArReur3Q7CHxh1I7wJT_Xqpz51wcSTDMVmSpnoDlU_aiXoFRhm7quaEq3rq2i09favVDd2tPWssXMxcjeuBrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f9cc60ceb.mp4?token=uQBwS8DbEYcZvs74wCPK4YlEYWHmcuup2AMuFdCdi6QOydVU806jV_7gkKvlxOG9JG8AAWkCjn8qTWaqlbr7ZDoMbVgdgzOLj0riEg9xyvTFYT2iXWG8Jmb2IZ4A9YgPdICm2oc3ZGXsgWP5OfEb_kAySWWCEQAfpSd92mckI6OyjnlS6xPh5YUwLa3c7j89dJw4ZGmNDqRfu50ADNPZTfxtyxdVAnqGtybudfAUmYCtwEQ0tQJxL-GnCzupL7UNzArReur3Q7CHxh1I7wJT_Xqpz51wcSTDMVmSpnoDlU_aiXoFRhm7quaEq3rq2i09favVDd2tPWssXMxcjeuBrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با چند ترفند ساده، بوی بد کفش‌هاتو سریع از بین ببر!
👟
✨
#ترفند_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/akhbarefori/684794" target="_blank">📅 20:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684793">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPKfVEqXkIPpmj6LT3e6tYDIJuyeYj7aBl9QLFgfYM6zCo3FzkWUknDvbJ7xOiC5TUAM9OlGyDAKcluerAYSR9GiHKZDf3C6xopuddKWylmpVee1WT9x3TOvmvtSklmur4hzqsgdioeEhuqDs9NaQ2Hp5nmFTf976-yqjumYbm6M0KHMFrTf0h-U7oNCiqAMEw_y6YMB6UxRuDacbD5xRmZQgIqQh6Fue6ahHn7WIl_7vQ9y8aStnu71sCta9SPzl0Up1CDFenE8tvBUZOWTQc5REQ1UwCVene9UlXt_jf-FLVJeBwRCXgquDOCIkKylmsVp2ahEtvx4NE_5fDwpIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تازه‌ترین قسمت از کمدیِ اپوزیسیون | چهل سال جنگ قدرت در توهم | از بنی‌صدر و رجوی تا پهلوی و کریمی؛ تاریخچه دعواهای بی‌پایان اپوزیسیون
🔹
تاریخ چهار دهه‌ گذشته‌ اپوزیسیون خارج‌نشین ایران، بیش از آنکه روایتی از یک مبارزه‌ سیاسی مستمر باشد، به یک کمدی ـ تراژدی مبتذل و کشدار شبیه است.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3240777</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/akhbarefori/684793" target="_blank">📅 20:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684792">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a44675bacc.mp4?token=vtTFwUOxg7NS43nH5XbR-n_TlWvwUQgl6dnXhNgh1EHRscq0Y9n27sy-mW_jI38WuiaeLjE0f8YtyWnDwp-UFZq8-mOYB7eVMan_RP3uV0wOSoEJvJjvHwYUdkTz-FIfWXQ2SG135h32W5_KyH6IBIdIoxxj18_YDFS8-4P5zIvgNUkcNRi89atu7zmjPFZUY63g_T3bFRPBC1fGqXcqTfjeWr1lefj7QYCbJOZ90II0U0vDpffL86vzcidRLbyreF6d2QXmBDdivKjCocHjHOKUJlHDsBnvQTkss11dtotkAV9ewSg38KR1H76O7ijuRq2fT-RWNYlaBMkZ4VyEaZGV0-mVIvZR8coG-sHznEDAqIYwebFuDsMalvTI21pZ15iim4_baihLYN10Vnj41Nsyui8wnIELOLMeRqyuIX2OumxVanNLo2Cml3mCbxS3E-mVsAOqQu7BYnFNf6_9-9bFe9WAGhXZ02gkth88hAb-8PHOe8dAgbcqtFsSp45KDjfiO7Gm_QWJGJ0ynwP6jkut3GcBPuTOEKoLZywnVQ1FWspERrwXsBoKgE7bJTvexNyGaKydAXD2vKfTmQg2dtBW-6bWS0BhD_fZpCOFQmIhFgPWfiZ9WQhZhWZ_Nor4BmTUIx9czLfu0U1yMsEexITd1mapCWwXlWlMrdYzMvo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a44675bacc.mp4?token=vtTFwUOxg7NS43nH5XbR-n_TlWvwUQgl6dnXhNgh1EHRscq0Y9n27sy-mW_jI38WuiaeLjE0f8YtyWnDwp-UFZq8-mOYB7eVMan_RP3uV0wOSoEJvJjvHwYUdkTz-FIfWXQ2SG135h32W5_KyH6IBIdIoxxj18_YDFS8-4P5zIvgNUkcNRi89atu7zmjPFZUY63g_T3bFRPBC1fGqXcqTfjeWr1lefj7QYCbJOZ90II0U0vDpffL86vzcidRLbyreF6d2QXmBDdivKjCocHjHOKUJlHDsBnvQTkss11dtotkAV9ewSg38KR1H76O7ijuRq2fT-RWNYlaBMkZ4VyEaZGV0-mVIvZR8coG-sHznEDAqIYwebFuDsMalvTI21pZ15iim4_baihLYN10Vnj41Nsyui8wnIELOLMeRqyuIX2OumxVanNLo2Cml3mCbxS3E-mVsAOqQu7BYnFNf6_9-9bFe9WAGhXZ02gkth88hAb-8PHOe8dAgbcqtFsSp45KDjfiO7Gm_QWJGJ0ynwP6jkut3GcBPuTOEKoLZywnVQ1FWspERrwXsBoKgE7bJTvexNyGaKydAXD2vKfTmQg2dtBW-6bWS0BhD_fZpCOFQmIhFgPWfiZ9WQhZhWZ_Nor4BmTUIx9czLfu0U1yMsEexITd1mapCWwXlWlMrdYzMvo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غلتیدن غول‌های سنگی در سیلاب مرگبار نپال
🔹
سی ان ان به نقل از منابع محلی اعلام کرد که تعداد قربانیان سیل ویرانگر در مرز نپال و چین به بیش از ۱۶۰ نفر افزایش پیدا کرده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/akhbarefori/684792" target="_blank">📅 20:01 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684791">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
سخنگوی ارتش: قطر از سرنوشت خلبانان سوخو اظهار بی‌اطلاعی کرده است  سخنگوی ارتش:
🔹
پیگیری‌ها از طریق وزارت خارجه، ریاست‌جمهوری و دولت و ارتش قطر انجام شده، اما طرف قطری تاکنون از سرنوشت خلبانان اظهار بی‌اطلاعی کرده است.
🔹
وی خواستار پیگیری جدی‌تر و ارائه پاسخ…</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/akhbarefori/684791" target="_blank">📅 19:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684783">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BSNMeXMhNtP8rMjeUs9gxIwJxyJZxTgUiiv4Yl-OHBf26i_yTXemzagl-psd25K8si4cwipSreLMyYm5Uly0wg_HVjvwfgf-JpsxNlxAcNadfz-hdvaa7-_CzMavN_8-QtfMU9wFpDdeerLKyhFWlX3gzUhiy3qVF9PFOzwpxkSE87BN3Y9GlqaGLoFBzBshNIsbnBx9OOPSN3B4yZzIjM_dgStXV05X3GI8IzXFtICGrPWkvuH4HTpX2O2LWOwooixs5uRmsvUja7s6kph4duXENeFqdlS23jtUtOTXdXXatNrITkaYPFF1xzrbiUxwcgxEVte94CkV4ncdfDMslg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G7J9IqWp_hgyC5oC13JOiELmq9jihEf0yzgjJfB-w8oXLStPn6k-muR8V2sLWcirPlKP4jB6_ejgflcqsaby1bQ84v8iyaPomevcmYu0aQgV7ynb4CRqyL3lx1cQxiE8BgQ9exsUWoBOJUcqxJDFdtSfQ7vvETcm1JCTt6XNrTRr3drvY4Inz5SVxjJcfIIUtYkBO5U9VdyNpUyQkfgHAvd1TLpYxOdlMaSIR2Gt6R0_gvaw4ATT2wIw678uWwGztoaykMlWzK0RBpM5BCHPpnr86pLjhLs3zzxA7gDjggMM1XHUiHSWx3jyqACJeazVJDfqVGGUERDgTp3OlOKTGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CWJMqV2-zNggLno46PU6GuIBfhkfr138pPvI45badTLoTCAW1-8LwRpNbI90HeS7XTgvInXBJhxfsSA30H4-dfnZ89PqfL_pYIei2hqj5dHI8s53sS8rqHme7qACOG6qjirTDM2VAZKXUqM2g17Az0L72CDc3bcJrw5phI8ZHY2xfp4HpLF42yceH6ObBGn0Sc9dznJ0O3ZnqnXBXnLQYjEiLPZAvdmsLOshW-vKj3zawkp4UxqYTEK6umQR2CFgpj4AVFqU-D1Ey3zzXc00jAHuxxL1ndJSoXgYf2euucyGardgapDWZwoNM1pZXpb0Jf8QUD6WVInEQ5TiM07_8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NRwK1iPZhPumN2ywARxVlOUcBjZVTgCqrvWoHzlsqFWwPmRGvgXVfUJsUT2Ol8nAcj4vziMGUfS7A2AwNymMzRhrH8r--o9FChNtFD0YJZzPt2iz5i3q39EbG4KjxSQmGYdyor9TfKqQtVXi8OOcSuR4qh7BRfT79VYmz7xySdrv5WGKPnh_F8PUBtbkKvyiUNlJbDHYnd7h_gtabs4nYvBck7EuGuCboqImT7t_BNW6FRmPpREIIQEvIQMbLBi4ogLRVYyehxRaIGIVpPH4erANTZkBgcSeXXNdtGM39kUW9677i8-xv-VvTYAnhYukUOmLdmf-b9BLoyENVcqJ3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WlRFAf0d5wBC6iu6Y3SsMYu-MjcYCLoCCm78ORFdq9DzMKwKpcLVcnaWb_Ehfvogz8z7eUJwnBvLLuQWgN07xZiOGyQjPaVreqxbXsRjmpSR9iZpPodym-utLNwFrMm8dc6bnGBl60CAGqVd86RSUbYCClQ9Fy8dztFF4y56nmTUS_hXefPz8ois6cuSVFcpWI8kuUAPNDFAKLa4ex1VrudbMYjPe75bbmS29vYdqPq-bWkHm0XSPP8ryqa6pv632-HKDX_HF44CSsULKxW7UwGGSCmP1jJ1rtApEmNvJd1mappG3gfNEP5KBOhPOnTA2ilaKsIiUBZ4PfapwJG_gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q7MnyTHt8ExWJo2mbdowb0sGzZvivwQljQKls0ZvdggIo-j5eZsQ8WJcMEzJOXKm1GnnUyIpv1d0Mke0IwvOB22zIA1dZT7XvW8CU8MdpvBihqWjAkFPqk7Ql6VvVl_aCSYoBqMjbaSFUhYO4UKpayrFQQMnDCsSA5I7eSHPJ45WicWnDHnneoa4RzNaS-4VxSbztqzUXsLK4U6kPOj6PSYKuDS1iqQEBUVAgrr9DmBrAYLXdEtPt8YzYglWU-5PHF9FDvVcBxR05JvLwgPjHNxikGlZs8kGgNOGGqX_Nu5fGaFVlEURvO7akg0RHI6mGWVXKFgG3uY7_hYnqkpz8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uZq0jCUIZt8uvJDaYFunTNqgyNTokLuB3n0v2hIk3XWupoAHXzgwTxV1cqwf6rXdsnUuuCGfd-HG7dSdqJPXQT1lefc9epN2isS8TKmeiMKSQ4feUdh3xmsOIGnu6h5JWB6-snqlCtYssOoJMa3IJn2hD5JO7gDupnC1CX9jD-ftaBVsw4V7TYp6zij04wu8DmlAc55EHKcRfymXL8821jnBpANtu3h1FTjPCJ2qcRXsAxPHjr8M31lCHHmcvuj7Lkhl8-rt5Hpo6WLePPfWfeqm70bRrY8Dj70laPevX6uJoNgMIZMIWdXUIyd4d4eFvovGTpSuNIdUpP4WA7ZbCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aBcpM317nB6NmdqEW2xR-eYi8_1qTZdcTFAow8EGzoZ90E-g8t7EwyVB_zHu9FhAP81HcCVzAAAtzBLrZ_6iFeY5-tVW40cpt0xScqFa367g8lW_RCRObmd9xntaybaNkFu07JKGdecuFtOBURM1XtD-TbgXYjCjdIkMVbQ-UEI6HRMeUliyLIGJwwffBGWeDN56lPOIeNynKqB0TbgBhB2R5Wl7LSXFYPFGukrPN_BGFjI7MbV93UBoijtFagyk3TLWoB9NOglzV0of8Ll7uY9s7mu13R3KyqT4_50haOAIule831XfuzlCTHUOl9BmasBscP91yTAnUMz32In3hQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت برکتِ حضور
💫
✨
برکتِ هر نذر، به حضور دل‌هایی‌ست که بی‌منت کنار هم می‌ایستند.
🌱
#هیات_قرار
با همراهی شما مردم عزیز، هر روز با نذر و قربانی و توزیع گوشت قربانی، در مسیر حمایت از خانواده‌های کم برخوردار این همراهی را معنا می‌بخشد.
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇🏻
@Heyate_ghararr
شما نیز میتوانید در این کار خیر سهیم باشید
👇🏻
5029087002135690</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/akhbarefori/684783" target="_blank">📅 19:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684782">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
هشدار بیل‌ گیتس: هوش مصنوعی خطرناک‌تر از آن چیزی است که غول‌های فناوری اعتراف می‌کنند
🔹
از خطر بیکاری گسترده تا بیوتروریسم؛ از رهبران جهان می‌خواهم بیشتر به موضوع هوش مصنوعی فکر کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/akhbarefori/684782" target="_blank">📅 19:52 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684781">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3ZiI3TGyLtML2Aft6-R98ifxrP76WLcMczqvu-Xp0bPoIOIK1269FAuTRY6at6I-Fb2M_o50lhVuefkgWALuc7XPyJpsBYbAbwEyyR6bMF0kmTRKe1-luMfG7P_MqvqanbrQR4lE2U5tWMboKiQxvFHiHNrltrnsEENeXHgIgOwqtJjubDh5WWjPDv5IbcHL5Myc8O4k3Zg08BlHAUfQGgYW-Jg2tsr2_NNFeGphuqzUx2kqFcmxudZlq3B51AbR2dikXdWmMyHofLcekn5pLjaoxjiwHcXtXPMZAPEJEazhNgWaj__aeq3BjXwMTh7KlGekCc1kMmUQwRqRpZHDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار ابن‌الرضا سرپرست وزارت دفاع: معادلات قدرت منطقه را تغییر دادیم؛ با احترام با ملت ایران سخن بگویید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/684781" target="_blank">📅 19:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684780">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
قالیباف در دیدار با وزیر خارجهٔ قطر: ترامپ با محاسبات غلطش ناامنی دامنه‌دار در منطقه ایجاد کرده
🔹
ادعای سنتکام: از زمان تقویت محاصره بنادر ایران ۷۵ کشتی را به مسیرهای دیگر هدایت کردیم.
🔹
روسیه: ۱۰۰ میلیون دلار بسته حمایتی برای تقویت اقتصاد و ثبات سوریه اختصاص دادیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/akhbarefori/684780" target="_blank">📅 19:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684779">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔹
نخست‌وزیر و وزیر خارجه قطر با پزشکیان دیدار و گفت‌وگو کرد.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/684779" target="_blank">📅 19:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684778">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e01e91473d.mp4?token=MHdXdX_mH5tgH4BDhlQlqLSErl9J4SrZz2vDOIpZvqWU6RGA0Xs3zhTMZ7JhaYEJakOMzOagYhXg6Yt9Ms6epI8vOq8ZTlyWYjHwOF3iVDMNnId8m2xdpehAxCj0UeQyl703tZXom-0W6NpIzxabRTKz_oJDhehO9e5ZTXueU45-MElEUoJ_2wYJ3MBCxUfGPa1PS7IVCh8AumodEvBNB6_SyXDY8G1L9Hpm8vw_wHdFqgXIHOKnt5cSwB3cezgf0mlEy7olfqnrmZQZyIX0obtWLJ-D02xhrYHtsn-59czJ24WFAP42bG1LO2gotzdT6AnP2RatYefq_p4T084DFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e01e91473d.mp4?token=MHdXdX_mH5tgH4BDhlQlqLSErl9J4SrZz2vDOIpZvqWU6RGA0Xs3zhTMZ7JhaYEJakOMzOagYhXg6Yt9Ms6epI8vOq8ZTlyWYjHwOF3iVDMNnId8m2xdpehAxCj0UeQyl703tZXom-0W6NpIzxabRTKz_oJDhehO9e5ZTXueU45-MElEUoJ_2wYJ3MBCxUfGPa1PS7IVCh8AumodEvBNB6_SyXDY8G1L9Hpm8vw_wHdFqgXIHOKnt5cSwB3cezgf0mlEy7olfqnrmZQZyIX0obtWLJ-D02xhrYHtsn-59czJ24WFAP42bG1LO2gotzdT6AnP2RatYefq_p4T084DFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مینی‌برگرهای جذاب؛ یک ایده خوشمزه برای شروع یک کسب‌وکار کوچک
🔹
در #چرخ_زندگی سراغ ایده‌هایی می‌رویم که با سرمایه اولیه قابل‌مدیریت می‌توانند به یک کسب‌وکار خانگی یا کوچک تبدیل شوند.
🔹
این بار نوبت به مینی‌برگرهای خوشمزه و پرطرفدار رسیده؛ محصولی که می‌توان…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/684778" target="_blank">📅 19:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684777">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
از جلب اعتماد تا غیب شدن ۳۰ سکه؛ شگرد کثیف متهم سابقه‌دار برای سرقت طلا و اقلام با ارزش
🔹
پلیس آگاهی موفق به بازداشت کلاهبردار سابقه‌داری شد که با پرستیژ خریدار طلا به سراغ فروشندگان می‌رفت و با جلب کامل اعتماد آن‌ها، در فرصتی مناسب طلاها و اموال باارزش‌شان را به سرقت می‌برد.
🔹
طبق گزارش‌ها پرونده برای شناسایی سایر مالباختگان احتمالی همچنان باز است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/684777" target="_blank">📅 19:06 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684776">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🏡متراژ مسكن🏡</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PH53eIgLWPLSQRrhG9MuaN1O5_Lia8ru9EmGm8ucC-8nF6Alp6uuM3AndJiKnmIqmOKIcTPp1bQoDzvvfbE9pVj8uKKsnFfrjoztms5c0NuwW7cWLcR1Eys_NNSqVIX6V__8lbWQSynTnyKunKQMaFAg9CO639GjCORafF_gQZaERS-Txp0_XLh1cjL_yPj7xcw-xvhWl2te0zqo3t3OWBnkpuzhRHHaHq67h5uJ8ijhyW6LZ9wYRjhrnFz0c2SmP_sVX7e9_KW4UgfOuhlSLkR4XQMokSmFVWJB9EcxmHEc2NIjBFKJGfmFsKgQkktiwCvpWIlt4nQHN7wSgwSsKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کد ۱۶۰، آهودشت، ویلا تریبلکس زیرقیمت، ۳۷۰ متر زمین
۲۶۰ متر بنا،۳خواب مستر، استخر چهار فصل
( پروانه ساخت و..)
انشعابات ۳کنتور اختصاصی، روف گاردن، آلاچیق، شهرکی با نگهبانی ۲۴ ساعته
قیمت : قیمت کارشناسی۲۸م
قیمت الان۱۸/۵
#تهاتر
با ماشین انجام پذیر است
قیمت ویلا ها از ۴ میلیارد  با اقساط بدون بهره و زمین اقساط بلند مدت بدون بهره
https://t.me/Metrazh_maskan
خانم شایگان : 09194879515
خانم مطلق : 09199661658
https://www.instagram.com/vilamaskan_?igsh=MXM1cm1ycDU0cmNuZg%3D%3D&utm_source=qr
ادرس سایت :
http://www.metrazhvila.ir</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/684776" target="_blank">📅 19:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684774">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمشاور سرمایه‌گذاری ترنج</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gyy7pZQ1Ag6Cm3c6VZDnacj7H_aSaFOHbH0potGOWEuzfQRNyAoNIdmQcrsHQc_AHIWRh_qPBgbPfQAhkKftTo9_gooUqvaetFUNqgmDmoRzVlwML0jJf7D2fmWNjRrC0Zwp9r0uQbSclRCfOH6vzeQ-FSgZA9JSV6iD1wWhH6P4M9qoHiMavIhGmO8bFUDxe1009IK-6WkjnRduW5uAXB8gD60RYlB6eT2RtXWHGZXAnHlOS8A36TfG0GY-qi9waih93F_pgCd2ms1VKbpJQKDyrt2w1VeoiNQ7mISMTwKjLkgDGaxfgiW5P4CYg6ODVkg2nP7DglhiOFirjQ2RmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت تمکن مالی با خرید ETF طلای «رز ترنج»
🟢
یکی از مزایای جانبی خرید صندوق طلای «رز ترنج»، امکان دریافت گواهی تمکن‌مالی از شرکت سپرده‌گذاری مرکزی اوراق بهادار است.
🟢
با خرید صندوق طلای «رز ترنج» هم ارزش پولتان را حفظ می‌کنید و هم می‌توانید تمکن مالی با اعتبار بالا و به زبان انگلیسی دریافت کنید.
▫️
خرید رز ترنج از ساعت ۱۲:۰۰ تا ۱۸:۰۰ و با جست‌وجوی نماد «رز ترنج» در تمام کارگزاری‌ها امکان‌پذیر است.
🖥
برای آشنایی با نحوه دریافت تمکن مالی اینجا کلیک کنید.
▫️
@ToranjCapital</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/684774" target="_blank">📅 19:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684773">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATlpw8Ue4MLLDx98HDSXaCY8tcm9PAf_ZVbgUig0_1rn1GVLrW9KCyt52YaOTI0pywRCVusCFlIWaMDUQZo1y-z3KAdn5RyYfD4ZqExaiLBC6k-SeoP8A6IUTMSwsPcqM9m1ND4kK91viSGE4uV8ac2zr9u8I2Dz-iklO0U__ZOB98jWazL44bELfVxpqLFqBs0VfMQT2UMBDtW97n4qEHsNwly-qG94wwBrSY2CSc6lQ-A6vc34lKtvvyAMuxPaHNqF1wHx-RnLfAE5pKuMcbujuPzVG3Q7JMFczFqI78f8_QTGgK0mjruBJYumKuYlqRSLnpEFhcvkE4slxj7jGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماجرای دعوای علی کریمی و رضا پهلوی چیست؟ + تصاویر همه استوری‌ها
🔹
استوری‌های «علی کریمی » و درگیری او با تیم «رضا پهلوی» طی ساعات اخیر در فضای مجازی خبرساز شده است.  بیشتر بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3240618</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/684773" target="_blank">📅 18:49 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684772">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
بلومبرگ: آمریکا به‌دنبال احیای دادگاه دوران جنگ داخلی برای توقیف نفت ایران
ادعای بلومبرگ:
🔹
وزارت دادگستری آمریکا در حال احیای دادگاه‌های دریایی موسوم به «Prize Courts» است تا در صورت توقیف نفتکش‌های ایرانی، امکان مصادره محموله‌ها و انتقال درآمد حاصل از فروش آنها به خزانه آمریکا فراهم شود.
🔹
این طرح هنوز نهایی نشده و با چالش‌های حقوقی مواجه خواهد بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/684772" target="_blank">📅 18:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684767">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qM96Zmv68WElPWdeHkIFuZhP_PaCje2INCUZnoAVN8K_4cn46VOjv957_MhVhT7OV3kKVD-b1-sR2ilOX-WFbjnAk2tEhZ0-tsyiTmfEuucZN5uU3c8ctAqaA6vDheZhBiDdiWT_nwjkWmy45aZzOmQvijeo5rA9Z_rj1T96X50ZiMuNt54RjhOt055NXVPIk4Qy6Q471hLJNc4LXWy_ajebcjwTaiiV59Lxo4_wzIHIhYA8Lfe_W0qqZRYF4elL7ZMc-4zXXvmxvfztGE1oFGHgt_nQ_636-1U5V2o2cgl1BfSrnaJXculvah2c9mI_Rjngl3WeC7ME0IK2Gy3Qlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BJFb3V7Km1uhpFMvO5N4oLYj8_F9nT55kruO3vGVEOBEpTuBXjKmo07ueU8psLkWFSpA68HdmWFDUMbznqmrbaTfKIP_7yOlfCD7CFt4kwIL_gAorVjHlIcTtUP8xjENMAqwPUaidvKtxE2RbnyzrosD02q_EWTatHYdWsklEnr3e2vkSDUjQr1ED6WPtI_13adtqL8BIUZ3pQWfqeJy2odEHr7yQfC2uEwHzOvt0LaQt2A7Qoid6W1pQxWwvDSqZQMH9_885Mzy482p2dKiLKYOogbV9VPj6VYxdYFPsxH5bpZxxBP58zHU9ZTLxe6kvAsuXBCkkbqZb5gVrzPnDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TSbLJ19l8jxt55uB3FfKRXZscAvLXuD238ZjUqqCVdSxMvBB0CAMt9VsMRDqs4OuHCM6-PKw1h9HsmBP9xaaAwy6KNM24sybEu16cxcauHn1R60NgnKQf0n8GSMmlDxpEgl_NKUhiq0q3spQFvGjk9eMhvfebOYjxOwNkQb8cVXVGziSm9MIhq17uo5cSYtcN4cHekySaLaxheQZwEdb2-5_WdpHXQVuFvet7_oMRv_uQXpf-jcW2q9sTC33a6vc_E7-DlRb27QLTUO3Jcuji6WztFBcyDIKYUW01ab0sppHCSy27BlJFE5EuFkP1RoI1uwe4zA8z3Af4gFr2Ci1nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SxuNb3vaIDH3l_tW8QLJn-tHY3njpIWBCV0CxsUMhdVxuqBvOmiwpPBbgP4PCmOjkSPHdsimXptym-B-UGN3StGv1aoaHQPl_levRiA0iNIghYWp4T9rDew4hgdllc6eBMDJH0DWApUYIDYkzJM0bv9zLny-__EFxjpGD4Ci2Na2icDWBBw4B92UhF7OZPVANYRJhbAxBeDa2maD-3Ca3vwR6-tsMSrpin68sjAnqwvWgyWep2vJaAO_66PViYecS1s2SmGwhTrcTyhqDxfxwM-isLyEM3WHnT728aScqK0sHfqeCSNKxoybOOIyvmp9wWCAfoKwVjZYGlTnqGSuuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H_BJXt3lhNnRwXGKCZblJI-b-xIFmXCcE-NKQux49lx22Kl50Wed2O4dfMu-FuoYO4zQaChyABCtrNK6tLvIEfvP4lr7rnaOjHc5dEr-z4aLx5U1PA3oFu5hnkaKmehK4UE4cZYfstC3GVNxwlYGs98x7a0HZZabh24cIKJ1djGwHGU_6wHjhxLpiAoWs4QpJDUqsn6o9dWuBBECDX0DL9DUj9bO4TA3OxE5VxLCVUXkSKS0xEARXsCZdojm7kF2bCqZ8u-3lik7zamXnjhgP5lrM8q-OmHKffADDFtUHPbwcPUup0LSNOfx6ao_hBRkwGzhH8Ro9vpwF4ZlOvBxxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بیانیه سازمان اطلاعات سپاه در خصوص ترسیم صحنه سرنوشت ساز مبارزه با دشمن شرور خطاب به ملت شریف ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/684767" target="_blank">📅 18:42 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684766">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf0ec4e373.mp4?token=hR6nLv--esW3sBSBvd4wgsk6-yJzHOcxlE0QH3ihnen--x_GZwpS8d0ZQMRa8COqpMKguNe4MsT2En9qe-fIy_HqzRSZGVEs7E9SlIzDHn7VqW3_bxTnJl0a6KLaEpqafpATeNYNJmI5LYtypejxqBADWB8UOGOo-IbEITK_wvYc88wO-Zfq8vfhqeK_Z3f280YUIIaT9bJfS-NMyq4-7dpTdMx0VjPko8YRk2HyNvv79csVVvWYwm8oL7PCqVi5jYXgPJACHyL6oygVTNtQX6CqUeGwvPn6_BM3R2OXWjQZOJcus9e5njyEQutxEsHT8hecM6l5YtghvOk3Lp9-HVRR9SvmvRQij36mo0I_neaovhG9tpflim_PgbSbRbf1IZMqR2ZyhNBR5RaIl0LM2fBRW44oCwD96B4-yYsDYUTsgIul2A-7FFoNZ-WDTNibPeG1E-c04aMKClHCVTvoIsqJoGPCM7-u95dJ7cXTktqx3zYB5Adh8R_VCD4h1yg_hQLKEjeb6FEMi6HSOgn7XgFm_tWc26N3e76zlqbI0vtKtwIz8EoPUZvH69oelz-oq6jx6mxw_0qQP4_ktUspxwJKCf70yoX0DxeGrjdC5O5fA2lit9Qso5fRW2jnt0qXcO8K37R6sumQKTAFTz2Hlxzr_HW3xewlWUHyV3PZpNc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf0ec4e373.mp4?token=hR6nLv--esW3sBSBvd4wgsk6-yJzHOcxlE0QH3ihnen--x_GZwpS8d0ZQMRa8COqpMKguNe4MsT2En9qe-fIy_HqzRSZGVEs7E9SlIzDHn7VqW3_bxTnJl0a6KLaEpqafpATeNYNJmI5LYtypejxqBADWB8UOGOo-IbEITK_wvYc88wO-Zfq8vfhqeK_Z3f280YUIIaT9bJfS-NMyq4-7dpTdMx0VjPko8YRk2HyNvv79csVVvWYwm8oL7PCqVi5jYXgPJACHyL6oygVTNtQX6CqUeGwvPn6_BM3R2OXWjQZOJcus9e5njyEQutxEsHT8hecM6l5YtghvOk3Lp9-HVRR9SvmvRQij36mo0I_neaovhG9tpflim_PgbSbRbf1IZMqR2ZyhNBR5RaIl0LM2fBRW44oCwD96B4-yYsDYUTsgIul2A-7FFoNZ-WDTNibPeG1E-c04aMKClHCVTvoIsqJoGPCM7-u95dJ7cXTktqx3zYB5Adh8R_VCD4h1yg_hQLKEjeb6FEMi6HSOgn7XgFm_tWc26N3e76zlqbI0vtKtwIz8EoPUZvH69oelz-oq6jx6mxw_0qQP4_ktUspxwJKCf70yoX0DxeGrjdC5O5fA2lit9Qso5fRW2jnt0qXcO8K37R6sumQKTAFTz2Hlxzr_HW3xewlWUHyV3PZpNc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن نامجو: کنسرت‌های تورنتو، نیویورک و واشنگتن‌دی‌سی لغو شده/بعد از تعیین تکلیف زندگی در ایران و خارج از ایران به روی صحنه بازمی‌گردم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/684766" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684765">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعای عضو کمیسیون بهداشت: برخی اقلام دارویی تا ۲۰ برابر گران شدند
احمد آریایی‌نژاد، عضو کمیسیون بهداشت و درمان مجلس در
#گفتگو
با خبرفوری:
🔹
برخی اقلام دارویی به‌ویژه داروهای تک‌قلمی وارداتی، گاهی با افزایش قیمت ۳ تا ۴ برابر و حتی ۱۰ تا ۲۰ برابر مواجه شده و در مواردی سر از بازار آزاد و ناصرخسرو درمی‌آورند.
🔹
بخشی از این گرانی ناشی از تحریم‌ها و مشکلات واردات مواد اولیه است و از سمتی محاصره دریایی، هزینه حمل‌ونقل را افزایش داده و در تأمین ظروف و مواد پتروشیمی مورد نیاز تولید دارو و همچنین تخصیص ارز نیز با مشکل مواجهیم.
🔹
برای بیمارانی که توان مالی ندارند باید با تقویت پوشش بیمه‌ای و تسهیلات حمایتی، دسترسی به دارو تضمین شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/684765" target="_blank">📅 18:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684764">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
نخست‌وزیر و وزیر خارجه قطر با پزشکیان دیدار و گفت‌وگو کرد
.
🔹
سازمان ملل: جولان اشغالی متعلق به سوریه است.
🔹
کویت و پاکستان توافقنامه همکاری دفاعی و نظامی امضا کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/684764" target="_blank">📅 18:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684763">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
دخالت آشکار ترامپ تروریست در مسائل مربوط به فیفا و خط  و نشان برای مخالفان اینفانتینو  رئیس دولت تروریست آمریکا:
🔹
اگر فدراسیون جهانی فوتبال (فیفا) به هر دلیلی به فکر برکناری و جایگزینی جیانی اینفانتینو بیفتد، مرتکب اشتباهی بزرگ خواهد شد.
🔹
او فوق‌العاده…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/684763" target="_blank">📅 18:18 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684762">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLheJ9LPE9AtpbLGepVd-iWzmzoLjlbVBVOIPuVTn_2XCduPp7k2OdxFU6JXAtvMIYAeUiFI2xSrY4y2FbRqz-5FCtVF1oU_M8jON-CB4rP8RzFWFETnMmfeC2be5JTAidqPkM_fRb2U4y3pZYXCQ818mGkfPFMlggXxquKqowppsx-VHAVZK9WNXZDG7CA5rth7K8HIukh9mOPih7tazU1FVx8g2N1Ats-dKUr5kg7GnkGpUgFZLVnUFMS1lCH5vC_kZIbxrkAv0235gB5IqY96m3GrLqLdytNhcg98fozUnWmiF4zzqx5VV0cj3VKAVSva598cIj6-AmnNjb3Izg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بسنت: هیچ‌کس از تحریم‌های آمریکا علیه ایران در امان نیست  وزیر خزانه‌داری آمریکا، درباره چین و ایران:
🔹
می‌خواهیم امروز به‌صراحت اعلام کنیم که هیچ‌کس خارج از دسترس تحریم‌های آمریکا نیست. هر فرد یا نهادی که معاملات را تسهیل کند و بخشی از شبکه‌ای باشد که نفت…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/684762" target="_blank">📅 18:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684761">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28d83ea631.mp4?token=NLZPd-RJr_y5_xIWR8TeZpHgbFDGyAlu_m-WTPSsAEidCU4CXGvcOc6tzhSfekYZRBYpKeC2AgASt9q9zLBvGKdKXKTL_zJAR4fuQU9khUyDYLob-FJDSV4DL9PFACbyqdLwi2O-2MQnrzViWlkVW-PR0vcu2ddb1KTIjzkGQMDPG1SxsslYW0sUemGB3i53TM2YJY9Yv290b11vaDUQUqkVv1mROYrJbuSrb2TkglItkyoKvnDaVw58MWwhSdjqZ5SvV91S6FqJqK11oSMjRxpCHgB5atVss0TBehlH7kf18IvYhEpYyru8M_oKpSKfh8Z37vr7f9jElt2rqP5jVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28d83ea631.mp4?token=NLZPd-RJr_y5_xIWR8TeZpHgbFDGyAlu_m-WTPSsAEidCU4CXGvcOc6tzhSfekYZRBYpKeC2AgASt9q9zLBvGKdKXKTL_zJAR4fuQU9khUyDYLob-FJDSV4DL9PFACbyqdLwi2O-2MQnrzViWlkVW-PR0vcu2ddb1KTIjzkGQMDPG1SxsslYW0sUemGB3i53TM2YJY9Yv290b11vaDUQUqkVv1mROYrJbuSrb2TkglItkyoKvnDaVw58MWwhSdjqZ5SvV91S6FqJqK11oSMjRxpCHgB5atVss0TBehlH7kf18IvYhEpYyru8M_oKpSKfh8Z37vr7f9jElt2rqP5jVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا حالا به این فکر کردی که مایکروویو چگونه کار می‌کند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/684761" target="_blank">📅 18:13 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684760">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/394056e459.mp4?token=rjupEp1pwm7CYZcd5W0dRx3ZqWFZSU1QzMoyDmfgRKWlMKqK5li8fR71-gU-DufIy60MjnduMrrUf4aKJAXcXZ7WGN9ZVmKZzlp3ha9rFQIOLiSnR9eKVbw1rqsbHguvc6Tp64WbXLETqrcJZiXFfg3mbMdjW2AHCMB2pmzy__y9xY21C4rK4a-4XgF0pZk1Dk7LWTtECLm_Jl15NdOMElxFTXdsEvzOSvvceBB7Bdf_5gdGbnl00dbsBPrQW1ryfgii-jbGFY05wpQHptcXcSNaR6-IcQS2bPwzG1mDdxLR0DRwUoiI-HWHRx3o5LTchIJO5T7fy4zyOIaNN_Smjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/394056e459.mp4?token=rjupEp1pwm7CYZcd5W0dRx3ZqWFZSU1QzMoyDmfgRKWlMKqK5li8fR71-gU-DufIy60MjnduMrrUf4aKJAXcXZ7WGN9ZVmKZzlp3ha9rFQIOLiSnR9eKVbw1rqsbHguvc6Tp64WbXLETqrcJZiXFfg3mbMdjW2AHCMB2pmzy__y9xY21C4rK4a-4XgF0pZk1Dk7LWTtECLm_Jl15NdOMElxFTXdsEvzOSvvceBB7Bdf_5gdGbnl00dbsBPrQW1ryfgii-jbGFY05wpQHptcXcSNaR6-IcQS2bPwzG1mDdxLR0DRwUoiI-HWHRx3o5LTchIJO5T7fy4zyOIaNN_Smjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فقط در یک دقیقه تمام افعال و گرامر زبان رو یاد بگیر #زبان_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/684760" target="_blank">📅 18:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684759">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43a9400350.mp4?token=Lhoj32rs0yGikiDjpnfzz_SubpLOReli3EmeIQb_fobea83jZ6RHqm8ntqtSaIW8qFshu26uvb_203Olstz34GNl4TTqcZzq5r5IAgVt2UZ0LEK-KI4TbHz6QhbIv4ENmHoPg1MPqUFYehbV4KWfb1GYDT-U5hR27rkfl3-RkGhVYUTkqyoavx2PI72VbUPXDsBLBx9ChtcN4s1DbwfwiB4YMLuD9oqHtmSYs6gLUHZvODAegGTfYYJ_dltaX5_8a3DVsj6UeVpBdBc-_3EKh9c4pIVrYoV5t53mJGf6_koMtGViXOTICpYtbKREW4PWU9B-kVZeaE_qV2M9pCMYNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43a9400350.mp4?token=Lhoj32rs0yGikiDjpnfzz_SubpLOReli3EmeIQb_fobea83jZ6RHqm8ntqtSaIW8qFshu26uvb_203Olstz34GNl4TTqcZzq5r5IAgVt2UZ0LEK-KI4TbHz6QhbIv4ENmHoPg1MPqUFYehbV4KWfb1GYDT-U5hR27rkfl3-RkGhVYUTkqyoavx2PI72VbUPXDsBLBx9ChtcN4s1DbwfwiB4YMLuD9oqHtmSYs6gLUHZvODAegGTfYYJ_dltaX5_8a3DVsj6UeVpBdBc-_3EKh9c4pIVrYoV5t53mJGf6_koMtGViXOTICpYtbKREW4PWU9B-kVZeaE_qV2M9pCMYNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با خرید از "چرم مَنطِـ" BMW ببر
❗️
از %𝟲𝟬 تا %𝟴𝟬 تخفیف «تمامی‌کالاها»
در جشنواره پایان تابستان مَنطِـ
🔥
➕
𝟮 میلیون تومان تخفیف اسنپ‌پی
حضوری و آنلاین با کد: PAYCWGZ5
🌐
manteofficial.com</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/684759" target="_blank">📅 18:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684758">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVXTNRPN_UuOWE_zKwOl0huCwWfsDU0He5z8VRwP16Thr1mtagUrok31Rloss3fJIqwGyARJ3hiiGFgjOJTiav4XnRKuPkfvj2hRfUh31Hb64OI6r379dnbNIJll3NX3YuZPMjFw0lK05M8nATr4FRcwyPE-UXBzK2MTFiue2tfrsreqKOcsuPAJXmXESZVmOSL5tImMOEvz1ZQDeTymJNlr1g9Io3kAdoDMBe5JAy0HmwJ8SmOLJYYVXKyJOF7iQcY6oC2vAX3TwjcblLNyLTIr10iME46bOeXirKmWZwojqbAv34Dh6SKeL2yeFrvWj5guONHqPRbsujv0s5P4OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تقدیر پزشکیان از عملکرد وزارت راه در ایام جنگ
🔹
در اختتامیه بیست‌ویکمین جشنواره شهید رجایی با عنوان «روایت نصر»، وزارت راه و شهرسازی به‌عنوان دستگاه اجرایی برتر در بخش «یاور فتح» انتخاب شد.
🔹
این عنوان به دستگاه‌هایی اختصاص دارد که در روزهای جنگ، با وجود شرایط ویژه و محدودیت‌های ایجادشده، فرآیند خدمت‌رسانی به مردم را متوقف نکردند.
🔹
در این مراسم، فرزانه صادق، وزیر راه و شهرسازی، به نمایندگی از مدیران، متخصصان و کارکنان این وزارتخانه مورد تقدیر قرار گرفت.
🔹
وزارت راه و شهرسازی در جریان جنگ، مسئولیت تداوم فعالیت بخش‌هایی از زیرساخت‌های حیاتی کشور از جمله حمل‌ونقل جاده‌ای، ریلی، هوایی و دریایی را بر عهده داشت؛ بخش‌هایی که توقف آنها می‌توانست مستقیماً بر زندگی روزمره مردم و جریان جابه‌جایی کالا و مسافر اثر بگذارد.
🔹
حالا انتخاب این وزارتخانه به‌عنوان «یاور فتح»، یک پیام روشن دارد: در روزهای جنگ هم، زیرساخت کشور نباید از حرکت بایستد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/684758" target="_blank">📅 17:56 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684757">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/434b9312db.mp4?token=q7ET_pZVQWL--ySVrhz19CRlYS8SnS8nig1wn2RezK4HcteXCleJFioOsm_1I-d7aR0BrlpaJM6zm2AiEwAJCzSq0h0YAKIzy-XiPLx-XaEs8o7yjumROlEZCPaOCij09GSUvPvaBl_LsYLfs5W31ehMWRTmJkPK3zHCvO5AYhgZDYvf3hLzoO8fp-gTTsw3hD_JuMzfeAUQeyw5CNmbHWL3vTrtwS9QiXCVUY0DVTL2cUaWd1WU5NY6RMX2xJWyYxYex37gj6Wz0sO9IP4h64M2QyWUxcxVhkPr5SeArnwZE1KU4Lxu8BuXfrzeX0uGmqiu5IMzwqW8VaiAIE_hOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/434b9312db.mp4?token=q7ET_pZVQWL--ySVrhz19CRlYS8SnS8nig1wn2RezK4HcteXCleJFioOsm_1I-d7aR0BrlpaJM6zm2AiEwAJCzSq0h0YAKIzy-XiPLx-XaEs8o7yjumROlEZCPaOCij09GSUvPvaBl_LsYLfs5W31ehMWRTmJkPK3zHCvO5AYhgZDYvf3hLzoO8fp-gTTsw3hD_JuMzfeAUQeyw5CNmbHWL3vTrtwS9QiXCVUY0DVTL2cUaWd1WU5NY6RMX2xJWyYxYex37gj6Wz0sO9IP4h64M2QyWUxcxVhkPr5SeArnwZE1KU4Lxu8BuXfrzeX0uGmqiu5IMzwqW8VaiAIE_hOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه برخورد صاعقه به هلال برج ساعت در مکه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/684757" target="_blank">📅 17:51 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684756">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
ترامپ جنایتکار وضعیت وخیم در ناو آمریکا را رد کرد
🔹
خبرنگار: اعضای خانواده سربازان نگران شرایط ناو یو اس اس لینکلن هستند.
🔹
ترامپ: نه، نگران نیستند.
🔹
خبرنگار: آیا استقرار نیروها خیلی طولانی شده است؟
🔹
ترامپ: نه. نه. نه. به اندازه کافی طولانی نیست. #Devil…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/684756" target="_blank">📅 17:49 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684753">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gb07k8nu6b8Oq_EhTr7toKQdf5W8h8PiFqYsC0_AwBadBu4VevuOZmosHLj6c91ULYtMn9u07BAcvqB-1z8P7Jnv1sappgCS_tqqHoGW7061A8wXyf7fyTqbIwd8r-0kKcZIy7bBxqp66R43DAys95XQNyQlYNRwGadKulUwryIA3sFlyS4GHkV4poQLuW8tmF-pmy-Tc2CYdGVhCvi2oXv9kznuc-lD5Ci2YKNoNeG3M8fPHXHyqLwKHgUA0BQnQpTZsYnkDIRSSGBuRk2QHbU7RVHvjiEe4LsDJJukIcRNH3zUMdjhga8Seh_4xKqWFkxbugkLSgJx4kd-W6H8zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشت مدال و یک مقام نخست جهانی ایران در المپیاد جهانی علوم زمین
🔹
تیم ملی المپیاد علوم زمین ایران در نوزدهمین دوره المپیاد جهانی علوم زمین ۲۰۲۶ در ایتالیا، با کسب ۲ مدال نقره، ۶ مدال برنز و یک رتبه نخست جهانی به کار خود در این رقابت‌ها پایان داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/684753" target="_blank">📅 17:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684752">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUNQ6VI7Nfoi0jU26PhMy4-Qbc5-18qjE9-cUce6G1TkbZuN8s-RXeZpuq_iMvT6znghxsjq5MLMZU4QlPD-e2SZvtmfLEQtA_uEmsIX6sdgvW1bz3HakUPK9Y9070tHRB4jA2RJsLch6b8h47GCT71iuTyIzt4it5syELtW0igUjM1uOms2DfCUBxENPsQr-LSpnU6kFcCPbaWP_bt7JGg7h125NNtx8xXqsRtKSCbMknflZmtu8Qd9Ic1NVBoHaXrvzCZLfqmrn_1mXPi8zUz_e_-W3uCZaO5R9t8ESG_ObHLb5lgUD7YUg7LSefjIis9SXwYo-L67zvqnMo8QcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری ؛ درد دارو
🔹
اگر برای تهیه داروی مورد نیاز خود یا خانواده‌تان با کمبود، گرانی، نبود پوشش بیمه، نایاب‌شدن دارو یا سرگردانی بین داروخانه‌ها مواجه شده‌اید، تجربه‌تان را برای ما ارسال کنید.
🔸
در چند خط یا در قالب ویس حداکثر ۳۰ ثانیه‌ای، روایت خود را همراه با نام، شهر و نام دارو برای ما بفرستید
👇
#درد_دارو
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/684752" target="_blank">📅 17:26 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684750">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8c16c92d3.mp4?token=D53XYnoOhcQYdxtx61du9OopNdETHdLvluJxcRZlhxU1uknG_oCf7-aOus9sldVY4I04T42yQwwBbrHaJnBkO5i82Bk34IXZEEDtZijnplhLtso4vWiwiZArPXAv3lZ_p4ZMFhzcN04SvY0c7ys0QaRCLffDtz4xU351j5heLENGadj87GvD8Vf48btuj_oaoxxq_aPfCfjrcUlNR0Bjn7rChH5Ii9JlsJtEQ7tXbl6w3c_njS-WZG523XwUkTUQMHmg3uqU1RaCAd8wRc0NL4903qDdoHwQ3R-Yi42JB8jux510XdfsMXLTs6UrhiB6hfNJDpE78EKlzqz46p6ffw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8c16c92d3.mp4?token=D53XYnoOhcQYdxtx61du9OopNdETHdLvluJxcRZlhxU1uknG_oCf7-aOus9sldVY4I04T42yQwwBbrHaJnBkO5i82Bk34IXZEEDtZijnplhLtso4vWiwiZArPXAv3lZ_p4ZMFhzcN04SvY0c7ys0QaRCLffDtz4xU351j5heLENGadj87GvD8Vf48btuj_oaoxxq_aPfCfjrcUlNR0Bjn7rChH5Ii9JlsJtEQ7tXbl6w3c_njS-WZG523XwUkTUQMHmg3uqU1RaCAd8wRc0NL4903qDdoHwQ3R-Yi42JB8jux510XdfsMXLTs6UrhiB6hfNJDpE78EKlzqz46p6ffw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۱۵ ارتش بزرگ جهان در ۱۲۶ سال گذشته (۱۹۰۰–۲۰۲۶)
🪖
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/684750" target="_blank">📅 17:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684749">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
پزشکیان: رویکرد ایران در عرصه بین‌الملل همواره صلح‌طلبانه بوده است
رئیس جمهور:
🔹
رویکرد جمهوری اسلامی ایران در عرصه بین‌الملل همواره صلح‌طلبانه و تعامل‌گرایانه بوده است و سفرای کشور باید این رویکرد را به‌درستی برای مردم دنیا تبیین کنند
🔹
منافع هیچ کشوری با زیاده‌خواهی تامین نخواهد شد، بلکه باید شرایطی ایجاد شود تا در یک تعامل هر دو کشور از منافع مشترک بهره‌مند شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/684749" target="_blank">📅 17:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684748">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
بسنت: هیچ‌کس از تحریم‌های آمریکا علیه ایران در امان نیست  وزیر خزانه‌داری آمریکا، درباره چین و ایران:
🔹
می‌خواهیم امروز به‌صراحت اعلام کنیم که هیچ‌کس خارج از دسترس تحریم‌های آمریکا نیست. هر فرد یا نهادی که معاملات را تسهیل کند و بخشی از شبکه‌ای باشد که نفت…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/684748" target="_blank">📅 17:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684747">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
سرانه ریلی ایران یک چهارم کشورهای توسعه یافته جهان
🔹
سرانه زیرساخت ریلی در کشورهای توسعه‌یافته به ۵۰۰ تا ۷۰۰ متر برای هر نفر می‌رسد، اما در ایران این رقم فقط حدود ۱۶۰ متر است!
🔹
فاصله فقط به طول شبکه ختم نمی‌شود؛ در کشورهای صنعتی، حمل بار ریلی ۷ تا ۱۵ برابر ایران است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/684747" target="_blank">📅 16:50 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684746">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0dd7d1c56.mp4?token=PGALouvVOrcFAq8wyfycBctyFiGyZFJ9cLf7uD3Esa-FFBaoES7UQbGzNzLEK7H50JAZpoO40tmccOVHGz0gFCIIU03Du2HgUnmRgmSgDPLBFh7FPcsxJB3CtdYtf4Qj-XVHg6-jXkPQzzY_1KlFap3s4qmqHi_NcFIhXxpiqv6KhTQ3eyTGm2-4USk-7ERYt8qg9IUUEe1Gkq6ozcTc3bLwRM_33IepziZe-_KqA9CRfyU8JgpXgcIPOXv4La8I5my-_scJ2CQmq4ITC1WZfdFRZ99GBoaiWxukqoiTo_rGQLNup9r1_d8-dUMSnEQi4ANltzR5iFmDH8Tc3Raszw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0dd7d1c56.mp4?token=PGALouvVOrcFAq8wyfycBctyFiGyZFJ9cLf7uD3Esa-FFBaoES7UQbGzNzLEK7H50JAZpoO40tmccOVHGz0gFCIIU03Du2HgUnmRgmSgDPLBFh7FPcsxJB3CtdYtf4Qj-XVHg6-jXkPQzzY_1KlFap3s4qmqHi_NcFIhXxpiqv6KhTQ3eyTGm2-4USk-7ERYt8qg9IUUEe1Gkq6ozcTc3bLwRM_33IepziZe-_KqA9CRfyU8JgpXgcIPOXv4La8I5my-_scJ2CQmq4ITC1WZfdFRZ99GBoaiWxukqoiTo_rGQLNup9r1_d8-dUMSnEQi4ANltzR5iFmDH8Tc3Raszw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زیبایی خیره‌کننده قرقاول طاووسی، ساکن جزایر پالاوان فیلیپین
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/684746" target="_blank">📅 16:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684745">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee4cc817dd.mp4?token=au66zd5VTRRITfuu91fgWPbTHt7lGXDgSnA09YA3uDH30L7qtziE4FLAWOarPPFsV4aNWUc7slXAyrLt37EMsRMIzgNb_hRNAjdqfNCe-bAy6p3a6tQR2B7haONnDS-dsyV6JxuMqTw7t5gbsT7kHUKTho-BRSmKBBr-PuhE7ORW4Bus6wU7dG7sPdxqIoPJ-G3IZcg1Z81yezlzNpUcHG-00GW-3QNEi9MvOd7vHtd06eUsDrSboMmRrCbVLfgyeKNgeVi78D-yZVZ0m7FvrNGkPvdedaloJip_rSdNWIcXR7WuAUwGvSm3QtMkfyNtYGZAFRb-02r2OZBLYu5xXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee4cc817dd.mp4?token=au66zd5VTRRITfuu91fgWPbTHt7lGXDgSnA09YA3uDH30L7qtziE4FLAWOarPPFsV4aNWUc7slXAyrLt37EMsRMIzgNb_hRNAjdqfNCe-bAy6p3a6tQR2B7haONnDS-dsyV6JxuMqTw7t5gbsT7kHUKTho-BRSmKBBr-PuhE7ORW4Bus6wU7dG7sPdxqIoPJ-G3IZcg1Z81yezlzNpUcHG-00GW-3QNEi9MvOd7vHtd06eUsDrSboMmRrCbVLfgyeKNgeVi78D-yZVZ0m7FvrNGkPvdedaloJip_rSdNWIcXR7WuAUwGvSm3QtMkfyNtYGZAFRb-02r2OZBLYu5xXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کاخ سفید: در حال حاضر هیچ مذاکره‌ای با ایران در جریان نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/684745" target="_blank">📅 16:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684744">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
وزیر نفت: فروش نفت متوقف نشده است
🔹
فروش نفت متوقف نشده و با وجود کاهش، فرآیند تحویل نفت به مشتریان در آب‌های دور همچنان ادامه دارد.
🔹
وارد جزئیات نمی‌شوم، زیرا اگر اطلاعات مطرح شود، این اطلاعات مورد سوءاستفاده دشمن قرار می‌گیرد./ باشگاه خبرنگاران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/684744" target="_blank">📅 16:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684743">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سگ‌گردانی در بوستان‌های مشهد ممنوع شد.
🔹
گرما جان ۱۵۸۰۰ آلمانی را گرفت.
🔹
حمله موشکی نیروهای مسلح‌ یمن به مواضع مزدوران سعودی در منطقه المخا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/684743" target="_blank">📅 16:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684742">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2111b7992.mp4?token=qoI_YMzJZoGcm7nBe0KiJRoc6zp4ulTyxxY0_METIGeJDco6TTSq8NeN2eT3vxgZSl0FGIVx4nPKtBsEgPpWAiUVwCPRhwaooFed0W6rvNqlt2o_Vy2dCGQb_HI1qy_uY9Z2ez5F_q5h_P6GcdVAPeql3IWfAWhHGql0WunpHQgYDg7anLzIbu_zCvkn3Vxf0MJPcWA_6lDY7VBxdfCp5dvulmrg-QLJyHDX9gjB6Q278Q1xolbBO2yJ0MMcTeFR3W44e2KStE5xHVtQt_CH-DN7tM0JsfSXGIWNVizp9B5ERNErC4W7Lb9wHj3PcaTigAg3NwZj3UdSLUvSbcfSzTjhmZKYVJfy-Wbvqce2sEmbVPVhpyOazyCUv3jrbuoDRQZJgzkH_gvyDENI-h4nmqPQBzUg7xvNuq8n857Nrb07vCjTi0EQowtSJ3ZS50BuSQUkjsPVjWEBcLSybCt3s5N3r3TJHPb94jPEDYxPFmWoyFDYiW_HRjqVS0QMCkSldyWNyH4Uo3DXmiOx2KM68x0adGZTrZ8EloNa7aDEcVfNBvT_PtEmkba3lp4xbWeQTwPmcj8LH1n2nis_0MCG9xQ9IJ6H977oBEQH5RFijeqzXnlgjwVD-tbCCGHHVZXc4I2bPcn2rwNh1xsAZ8kxF0CExeFtetkDuMG0ooJ2YXk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2111b7992.mp4?token=qoI_YMzJZoGcm7nBe0KiJRoc6zp4ulTyxxY0_METIGeJDco6TTSq8NeN2eT3vxgZSl0FGIVx4nPKtBsEgPpWAiUVwCPRhwaooFed0W6rvNqlt2o_Vy2dCGQb_HI1qy_uY9Z2ez5F_q5h_P6GcdVAPeql3IWfAWhHGql0WunpHQgYDg7anLzIbu_zCvkn3Vxf0MJPcWA_6lDY7VBxdfCp5dvulmrg-QLJyHDX9gjB6Q278Q1xolbBO2yJ0MMcTeFR3W44e2KStE5xHVtQt_CH-DN7tM0JsfSXGIWNVizp9B5ERNErC4W7Lb9wHj3PcaTigAg3NwZj3UdSLUvSbcfSzTjhmZKYVJfy-Wbvqce2sEmbVPVhpyOazyCUv3jrbuoDRQZJgzkH_gvyDENI-h4nmqPQBzUg7xvNuq8n857Nrb07vCjTi0EQowtSJ3ZS50BuSQUkjsPVjWEBcLSybCt3s5N3r3TJHPb94jPEDYxPFmWoyFDYiW_HRjqVS0QMCkSldyWNyH4Uo3DXmiOx2KM68x0adGZTrZ8EloNa7aDEcVfNBvT_PtEmkba3lp4xbWeQTwPmcj8LH1n2nis_0MCG9xQ9IJ6H977oBEQH5RFijeqzXnlgjwVD-tbCCGHHVZXc4I2bPcn2rwNh1xsAZ8kxF0CExeFtetkDuMG0ooJ2YXk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حیرت تلویزیون موساد از فاش شدن ضرر ۵ میلیارد دلاری ایران به تأسیسات جاسوسی آمریکا در عربستان!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/684742" target="_blank">📅 16:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684741">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
بحران تنگه هرمز؛ آغاز رقابت کریدورهای نوظهور
🔹
بحران هرمز، رقابت بر سر مسیرهای جایگزین را جدی‌ تر کرده است؛ از عربستان و عراق تا ترکیه و پاکستان. کریدورهایی که می‌توانند نقشه تجارت و انرژی منطقه را تغییر دهند.
🔹
در این گزارش ببینید رقابت بر سر این مسیرها چگونه می‌تواند آینده هرمز و جایگاه ایران را تحت تأثیر قرار دهد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/684741" target="_blank">📅 16:20 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684740">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f1449f3c.mp4?token=YcMmdwb0kcm3X4zOEOFP9vADCfK3HUB4fba1he8NCEZe1pGX8-7mJu4HpleYzg2UhCu-anNWoqnn7DjgGhOz9IqyXRrpUwGeRBoixxmjmHRjQwpUusLEY0cqI-V_stHT5dvnuNkdZlq9COB1Hq47Dmngb9EwZyE8S0KDh1eSG5APfsqwx6sOXGhOed3CEAveZVI29NgnkKgy6fGc38XGh4tCU8nRObGawMS5MOxTRn-fVilE6SvXNemw2wg71pZ1LErxPQUreBDiwd8tieLPCBBPBs14onOdBldruxckva72o4K8FZVhSxus4_XDT16Jpcz3iXMaoignRIQNDlCsFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f1449f3c.mp4?token=YcMmdwb0kcm3X4zOEOFP9vADCfK3HUB4fba1he8NCEZe1pGX8-7mJu4HpleYzg2UhCu-anNWoqnn7DjgGhOz9IqyXRrpUwGeRBoixxmjmHRjQwpUusLEY0cqI-V_stHT5dvnuNkdZlq9COB1Hq47Dmngb9EwZyE8S0KDh1eSG5APfsqwx6sOXGhOed3CEAveZVI29NgnkKgy6fGc38XGh4tCU8nRObGawMS5MOxTRn-fVilE6SvXNemw2wg71pZ1LErxPQUreBDiwd8tieLPCBBPBs14onOdBldruxckva72o4K8FZVhSxus4_XDT16Jpcz3iXMaoignRIQNDlCsFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این همان چیزی است که هنگام سیگار کشیدن داخل سیستم بدن شما اتفاق می‌افتد!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/684740" target="_blank">📅 16:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684739">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e0285b88f.mp4?token=PfpOH8Wf-Y-1E712JR1cvBoyBOqh6kKjLSQBXxVxDqa003wVF_LeaGvTSLMOScQwqZBLHnstYvpgIEMBO36SAielY3PLmwjOXsdlVLDDn_TyG6vGu3Kch80OkB1euSwPoPl3mD3gXJ4gtsoQf-Y7b-5cWYOVxiv9ZTj7FK7DWCBaJ_86DBu0IAMHM5kfJUfSE1VhNVSqTJUyZ4PSk0oybN7WkgUy2fflVgw2BKnrcAbU3aeMVAmIDvoEfPNmfJALRPOTEQAPcvUnLNQRxG6LGvUBHHNVpXxSaZHzGlndLhsdO1gci5qqm5IbVXym5tVLUf34STsA7VwPs7MmS9uK4DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e0285b88f.mp4?token=PfpOH8Wf-Y-1E712JR1cvBoyBOqh6kKjLSQBXxVxDqa003wVF_LeaGvTSLMOScQwqZBLHnstYvpgIEMBO36SAielY3PLmwjOXsdlVLDDn_TyG6vGu3Kch80OkB1euSwPoPl3mD3gXJ4gtsoQf-Y7b-5cWYOVxiv9ZTj7FK7DWCBaJ_86DBu0IAMHM5kfJUfSE1VhNVSqTJUyZ4PSk0oybN7WkgUy2fflVgw2BKnrcAbU3aeMVAmIDvoEfPNmfJALRPOTEQAPcvUnLNQRxG6LGvUBHHNVpXxSaZHzGlndLhsdO1gci5qqm5IbVXym5tVLUf34STsA7VwPs7MmS9uK4DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن نامجو، خواننده و آهنگساز، با انتشار ویدیویی از بازگشت خود به ایران پس از حدود ۲۰ سال خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/684739" target="_blank">📅 16:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684738">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43f1d60821.mp4?token=eJnSZ0JSufj67jrMxzcQWWeAh3ZuCA4twu2ku-LE886euw9_MCHPXV5TC9tZ2THm3xKs77MTh13JLF0YiN68rnU8wX8uMw-gQOw1joYxv3UMGbiK59R2svP-AjNfiScovsOmh5UVGXIp_6j0D00by649Mg32TPfPwRmShVsy8ZtQ770tjEROaOn4BQTljwyg0kSKpGqlpuJQq1Bd6SEiBGSZeBDnockS_IMa9yzoIDbFqUfPiOKy4UlGwzotI9l5M3AGQfexv4DYJ9WVvyrevlVueiN2Sb6s6rrQvvTBEVTuNs4jJdOvy8zB9h8bCPi6DE4ZknavxPudls2QjNZXGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43f1d60821.mp4?token=eJnSZ0JSufj67jrMxzcQWWeAh3ZuCA4twu2ku-LE886euw9_MCHPXV5TC9tZ2THm3xKs77MTh13JLF0YiN68rnU8wX8uMw-gQOw1joYxv3UMGbiK59R2svP-AjNfiScovsOmh5UVGXIp_6j0D00by649Mg32TPfPwRmShVsy8ZtQ770tjEROaOn4BQTljwyg0kSKpGqlpuJQq1Bd6SEiBGSZeBDnockS_IMa9yzoIDbFqUfPiOKy4UlGwzotI9l5M3AGQfexv4DYJ9WVvyrevlVueiN2Sb6s6rrQvvTBEVTuNs4jJdOvy8zB9h8bCPi6DE4ZknavxPudls2QjNZXGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرمایه‌گذاری در بازار طلا یک راه هوشمندانه برای حفظ ارزش دارایی‌هاست، اما به شرطی که این نکات رو‌‌ در نظر بگیری #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/684738" target="_blank">📅 16:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684737">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W75zdj2itzIaZF3KBxuxXlfiotdd4J4gqzWWNqtugHQfzIH635vRYZZY6Wsg48vL5zWLgJpze4m6Bw2NLVEWBSa-B2NhQNlVBHUTXx9qukIlDA9msJZ_a39iEEG03XU4VDs4Ai_YCUUT1JDijquLZFjmiNIRSptN16abOOhJxkeZHap_f1nOWZyxI7DqpvXeDqoESkwp1vZCnh_XHP5c3BOV6U63liQKM7UTKBOUmwPMUZSd-3Kv748VU0OktQlDqUFXmUBaVpuos5YLR9naWrhpMRGUxBhUkbDa_Jf-V4o-fjukRZi_Mv8P_6VocGlR7Nz9diNNIYSx1Gi_aDHwxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهان برق خود را از چه منابعی تامین می‌کند؟
🔹
با وجود توسعه انرژی‌های نو، سوخت‌های فسیلی همچنان سهم اصلی را در تامین انرژی الکتریکی دارا هستند.
🔹
بر اساس این آمار، زغال‌سنگ با ۳۲.۹۷٪ و گاز طبیعی با ۲۱.۷۷٪ بیشترین سهم را در تولید برق جهان دارند؛ در حالی که سهم مجموع انرژی‌های خورشیدی و بادی روی هم تنها به ۱۷.۲٪ می‌رسد.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/684737" target="_blank">📅 15:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684736">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1a395b6a6.mp4?token=fYT1sdCLLQ5DD7Teoe0pIyBSuKjQwwVKT9v5iw4mpFXm7d1lCYubW396c4MOdl7zEqWuNrulLBseADQX77WLkGec2EwfBEsM2qA7O7ZN6ZVMAkRLlqu6zAMMWE8ya0NOvG2mwCOzjJTeNa50aEQJq8oTrAf18ZeIOokYexa5NYMEaNKjNozlP49hJyRDuMVwVV09uMPpP2ItajsFosTOrizSRJjUB_p5VrMuscwdGAG-iuJYclgLco3_kPkDG2X-ezZsM7Cxiq2Sf8RnWxGub8Rsh4ShPzLMHaLWwD6oygiHx64PjmEDe6HYl0RirmVU9db994WlJMmM6XP8RQzabA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1a395b6a6.mp4?token=fYT1sdCLLQ5DD7Teoe0pIyBSuKjQwwVKT9v5iw4mpFXm7d1lCYubW396c4MOdl7zEqWuNrulLBseADQX77WLkGec2EwfBEsM2qA7O7ZN6ZVMAkRLlqu6zAMMWE8ya0NOvG2mwCOzjJTeNa50aEQJq8oTrAf18ZeIOokYexa5NYMEaNKjNozlP49hJyRDuMVwVV09uMPpP2ItajsFosTOrizSRJjUB_p5VrMuscwdGAG-iuJYclgLco3_kPkDG2X-ezZsM7Cxiq2Sf8RnWxGub8Rsh4ShPzLMHaLWwD6oygiHx64PjmEDe6HYl0RirmVU9db994WlJMmM6XP8RQzabA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ارتش رژیم صهیونیستی از آغاز دور جدید حملات به جنوب لبنان خبر داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/684736" target="_blank">📅 15:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684733">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pt31nBWd88mAryiujEvBuUJZlgPF5w01CT19ltuL1PXbVYs0CarmehFsXXdjvEunPdljvRlIm0wB2kBJGPJMsVX6h-faRcVrwusi2_7be7M6VmFz5epEhKzpC2DtEfUTuzKFvZRrcJgpiuoDni7WBYTO1POYsdzevEWXSXHIHOb68pp85UEmpAWz70ndUtotPf0QNGYraX4tIFAYM8QSYIHI_5j6PW5nuKObR0k1vMw3Z4bBgkpZJdEsFpaCZFWMFrhmDfngWzF02p6Z2O-_nPFtcNb-UrlM4J0ybPeqvVywUcUbSe9IbWxc7QkZld8PHZ8zYI1oJwTNs5T9aO3iMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bl6SEG16YNC4NFj_mUA08DPr1LgnStysvVySo1Z8tnjYWbQlCn2uyAJ4bAOPgtD3bPRx5MmM4jhax26lqYF7cPxQ3ooWsirZAffw3mHCeulMqyKd0O9RuJUQIX0QuvHhtaZ3mDHeFc7Equ9HXJkwuUamq9ytLyUO9NMU39P2wjRcNH04HSk2qXAtYsRYOzZGiJ2JzQIEhHFkDXozNcUL8WuCCJMOYGaFq07fYrz7G9xJj2VZikx4TbYCIoTJS6tfQMlGkDDbdTCfMev7mf3lp9e3G0ISbUteBj3lLJRqqmx0OIPuJhF_svfCZx9EH7_mcvlHTpZPW-dRIQKgtTt0BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MTjDKq9YuFyMkAYTOCXlf6R-1PdgydJMkhWxtQSvHdc7R-rV-G16Dqy6tZIICVXebScDKaqq0kOHE5C1-b1BpuoULTfnRF7J8UJc3yYraKEO9kj1JQLEyfbWS2Qjv9Pz9ZJWL9W-xwPA5Cty450fDrBWtZidAO5TzGeo5_zSuN8Ki0BcWuSLvCElTAb44oHZKy8qtCM7VfVBKpa6IWBdDZJUppgZdGni0yN9UkLe9G9xuX_kLwTSZOGua6x93ux_l0T4oAEG1sCStIQuw656ATcBjzPtM3ab-hhTLRMfofOMn6wYZurOElRbli2c8ePplcS4RNVY0VGblRVcR1B7xg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ماه‌گرفتگی تقریبا کامل ۶ شهریور ۱۴۰۵ از راه رسید؛ آیا می‌توانیم از ایران مشاهده کنیم؟
🔹
ماه گرفتگی عمیق ۶ شهریور ماه را تقریبا به‌طور کامل در سایه‌ی زمین فرو می‌برد. حدود ۹۶ درصد از سطح ماه در تاریک‌ترین بخش سایه‌ی زمین قرار می‌گیرد.
🔹
بخش تماشایی و رنگ مسی ماه در ایران دیده نمی‌شود. ماه در زمان اوج گرفت، زیر افق قرار دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/684733" target="_blank">📅 15:52 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684732">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b226e0f0f0.mp4?token=vw6m8sgJgGCw7Tw-frG6XqcKzGC-eIhbdg_ZDRcKF-jBWlPVvEMmIjRc7tehrUz4Sm3AgDjwjE4xEZMZPTOW3SVZBvOCkhprWRuX5_4iLkWjw6MVk8EXEZY5YtyLay_yyJzpi_NivKIST1HbSwmqrSZLgtoIAVnthiAaw7N0-nL0Yhfwm-Ryqo34CEsTLLEZt5Gyd9CCZk0vOlvRJjTKk4sztURVA2XQzwoWkrOqOP74iiQIhLTjnemEjBk06SDO6ovXvYR-UORlTkF_FjX8FQUSXW6eiIvkUjz9p6pP4ZPoF7rljHwJhDQItQKnLSp3_yEREHJOKkxrhD3BE-ktMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b226e0f0f0.mp4?token=vw6m8sgJgGCw7Tw-frG6XqcKzGC-eIhbdg_ZDRcKF-jBWlPVvEMmIjRc7tehrUz4Sm3AgDjwjE4xEZMZPTOW3SVZBvOCkhprWRuX5_4iLkWjw6MVk8EXEZY5YtyLay_yyJzpi_NivKIST1HbSwmqrSZLgtoIAVnthiAaw7N0-nL0Yhfwm-Ryqo34CEsTLLEZt5Gyd9CCZk0vOlvRJjTKk4sztURVA2XQzwoWkrOqOP74iiQIhLTjnemEjBk06SDO6ovXvYR-UORlTkF_FjX8FQUSXW6eiIvkUjz9p6pP4ZPoF7rljHwJhDQItQKnLSp3_yEREHJOKkxrhD3BE-ktMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نحوه
کارکرد
داخل دستگاه خودپرداز؛ پول نقد واقعاً چگونه از دستگاه خارج می‌شود
؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/684732" target="_blank">📅 15:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684731">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vs2peiv32f0ULQNZgqFMG7tdqebATitlc2e9R4Sbc8r0B7sTOf1zObzPbr39GN1X5lTf8KSTelJj9Jh7fOshcvLo7zezMmtHUOVhuNZ6iTj_A-vwrDs3Grk3tRYDhmwDzcWndBMqsXiRZJ3IasKhXix1mzA4aFG4buiRz1vdvCVDGSMx6BZdnHG7FbPKvjrha7NpSG3yA5gD6qWPwHgTjd6kUZlZY8QbCni7228ZIEmgS2-pe6yXXPfZMGIH6AC3evmaKRyLg2hbcQgUTx-rcsApsIQl1IavQNtQcU-VS35LAXaPp4xP5ywhXq49fc0oWdKG-HKgXcQ40uDnw0WGSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برت اریکسون: بودجه پیشنهادی دفاعی آمریکا برای سال ۲۰۲۷ حدود ۱.۵ تریلیون دلار است
🔹
تصمیم ساده است: برای فقط یک سال، این بودجه را به یک تریلیون دلار کاهش دهید، ۵۰۰ میلیارد دلار باقی‌مانده را به ایران بپردازید و تمام؛ بروید سراغ کارتان
🔹
این مبلغ برای آمریکا چیزی نیست؛ اما می‌تواند بهترین بازده سرمایه‌گذاری ممکن را برای این پول به همراه داشته باشد.
🔹
این جنگ احمقانه را تمام کنید و بگذارید همه‌چیز به مسیر عادی برگردد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/684731" target="_blank">📅 15:42 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684730">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56161c5a11.mp4?token=NGJWvjs0y09S9zSYdQEqInEbIyxisFuDeJV6xCTm50D9g-C732uidY48JYXSeg-RJbYBcDkhhX2n9UtqNhkcqeQtAQQeYbtJf0PRFTu4V5B1hDWVGuSP1SklkNl332g1HtVkMqcrKrFLa7m8nVzXfEq0jsdhf59kr_ZFMH0EKYM_4zk6_4jY3-VK6pDa2Vc_pqp_wZh1Wm8GwnaqlLUtvm3JA74Qg9ZBmV6XqOdcybLuUIFKF5K8lSsnPyYIXbJyRfGc1vsr-BiLi5I-H0IDSPRnk1HKyGQo5T1mOKHXU2LLtLi6tysHiCr2lDP9EnaU6n4KlLzoalddRom6OwfeEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56161c5a11.mp4?token=NGJWvjs0y09S9zSYdQEqInEbIyxisFuDeJV6xCTm50D9g-C732uidY48JYXSeg-RJbYBcDkhhX2n9UtqNhkcqeQtAQQeYbtJf0PRFTu4V5B1hDWVGuSP1SklkNl332g1HtVkMqcrKrFLa7m8nVzXfEq0jsdhf59kr_ZFMH0EKYM_4zk6_4jY3-VK6pDa2Vc_pqp_wZh1Wm8GwnaqlLUtvm3JA74Qg9ZBmV6XqOdcybLuUIFKF5K8lSsnPyYIXbJyRfGc1vsr-BiLi5I-H0IDSPRnk1HKyGQo5T1mOKHXU2LLtLi6tysHiCr2lDP9EnaU6n4KlLzoalddRom6OwfeEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا شهروندان ما در زندان‌های ایران در امان هستند؟
🔹
عراقچی: اگر امریکا و اسرائیل بمبارانشان نکنند اره در امنیت هستند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/684730" target="_blank">📅 15:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684729">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
قطر: وزیر امور خارجه به منظور فراهم کردن زمینه‌های گفتگو با عراقچی رایزنی کرد.
🔹
فایننشال تایمز: جنگ ایران در حال نزدیک شدن به بن‌بستی شبیه به جنگ اوکراین است.
🔹
ارتش صهیونیستی مدعی ترور ۲ عضو گردان‌های القسام شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/684729" target="_blank">📅 15:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684728">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نقشه آمریکا برای خفه کردن اقتصاد ایران جواب می‌دهد؟
🔹
واشنگتن از «ضربات ویرانگر» به اقتصاد ایران می‌گوید، اما این ادعا تا چه اندازه با واقعیت مطابقت دارد؟
🔹
در این گزارش تصویری، ۵ اهرم فشار آمریکا و پیامدهای آن برای هر دو طرف بررسی شده است.
🔹
این اهرم‌ها چقدر به کار آمریکا می‌آید؟ در این ویدئو تماشا کنید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/684728" target="_blank">📅 15:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684726">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2332da0a8d.mp4?token=GW3EU4Kqwf-TxV2b8niH0BQbGU425O3Jqp_LupmwfKIY_DLwv211RgVoNrVFZUKkjAoffM4BPMx8r-KwYLj3DDyi8k4DXHtZ0MUyYM46w9QPS9xkGMg0fsOhWiS4lX32Qr-sn1c38NOeABXXDQ5ZmzBdgd9K2QNIVHh_rOUrTyyTJiEd6cSooQgozIwhx3cjZr4lyDwpsbhTxivoTnXwiY7KLYw5YkFaqx76CkP_obSdmQtWHL1ruyDFkjjJuEDaooUqCIdU61PXTqgQY1ZcW_iXYcWj_N0k47DJRToi87RvuZx55A1JZ-j7zoZEWfsoPKJJN4GG7lf0xU-DpTRqTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2332da0a8d.mp4?token=GW3EU4Kqwf-TxV2b8niH0BQbGU425O3Jqp_LupmwfKIY_DLwv211RgVoNrVFZUKkjAoffM4BPMx8r-KwYLj3DDyi8k4DXHtZ0MUyYM46w9QPS9xkGMg0fsOhWiS4lX32Qr-sn1c38NOeABXXDQ5ZmzBdgd9K2QNIVHh_rOUrTyyTJiEd6cSooQgozIwhx3cjZr4lyDwpsbhTxivoTnXwiY7KLYw5YkFaqx76CkP_obSdmQtWHL1ruyDFkjjJuEDaooUqCIdU61PXTqgQY1ZcW_iXYcWj_N0k47DJRToi87RvuZx55A1JZ-j7zoZEWfsoPKJJN4GG7lf0xU-DpTRqTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طوفان شدید در مکه
🔹
طوفان شدید در مکه مکرمه، همزمان با حضور زائران در مسجدالحرام و اماکن زیارتی، حال‌وهوای متفاوتی رقم زد.
🔹
زائران در میان وزش شدید باد در جبل‌الرحمه برای حفظ تعادل و جلوگیری از سقوط، نشستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/684726" target="_blank">📅 15:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684725">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3342f01244.mp4?token=jhieJFw5gvx-U8o6sZQ2-P-VasC1pqmBYa6lvKZCPU9R7QHYHeHNFczi0pUqyRkXWksVGPYqTnnjac_PJPPLKDQP-CxcvJXw3W6V5N8tVbZNY96Xd2DFgJDihAgFDzm1NfZIOipJOe9Qb2RMlEkO6eSHNHRnbYSZyoA-RCNxnFbvY4OZAhAId7x60lSaXXl4poYGPNG3RrnUVaRd3VHiPWXtpJwEwvxFfv6rOhoGBLlMjGVeRXsq62vLr1mvWLgF4EowxmKBJ2tXNmp11Y0AEgwvYBGFICLCIKrIa6qHhup0HYLSSsadlSsHGehO-wrYlP3L2eNVCoiuon2koZcxPqeEq3SokEiv9lL4B40fN1ofOyb9UFqUZLe1jZboce7LAnX7PcwiPicWPhQS4qXxqVQhXDvkLj9EdQKbeawvEAQrNuuuh9gzH6emKascaccAxGRWk3Lq16Wl8Xyb2iZ0mM4K9-nng06NKiP6sqGdyA0N76XuFRs9etDcA5KlBUQtgeBsm99K2TS1fhN1T3t2CV2npdG0Vbhv73585uRef254hgDtUfosKSH8YWTVTfbYay8Fl3PhCzMFmWcjOSb4U6UvVIbpvlevuV9uGzDVU4V1J2WhqG5xTC3yjy_p9l9Z2olRcQclSJzcaP4zGsptxltcBcpeaLRmspk_LOTJ1y8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3342f01244.mp4?token=jhieJFw5gvx-U8o6sZQ2-P-VasC1pqmBYa6lvKZCPU9R7QHYHeHNFczi0pUqyRkXWksVGPYqTnnjac_PJPPLKDQP-CxcvJXw3W6V5N8tVbZNY96Xd2DFgJDihAgFDzm1NfZIOipJOe9Qb2RMlEkO6eSHNHRnbYSZyoA-RCNxnFbvY4OZAhAId7x60lSaXXl4poYGPNG3RrnUVaRd3VHiPWXtpJwEwvxFfv6rOhoGBLlMjGVeRXsq62vLr1mvWLgF4EowxmKBJ2tXNmp11Y0AEgwvYBGFICLCIKrIa6qHhup0HYLSSsadlSsHGehO-wrYlP3L2eNVCoiuon2koZcxPqeEq3SokEiv9lL4B40fN1ofOyb9UFqUZLe1jZboce7LAnX7PcwiPicWPhQS4qXxqVQhXDvkLj9EdQKbeawvEAQrNuuuh9gzH6emKascaccAxGRWk3Lq16Wl8Xyb2iZ0mM4K9-nng06NKiP6sqGdyA0N76XuFRs9etDcA5KlBUQtgeBsm99K2TS1fhN1T3t2CV2npdG0Vbhv73585uRef254hgDtUfosKSH8YWTVTfbYay8Fl3PhCzMFmWcjOSb4U6UvVIbpvlevuV9uGzDVU4V1J2WhqG5xTC3yjy_p9l9Z2olRcQclSJzcaP4zGsptxltcBcpeaLRmspk_LOTJ1y8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن نامجو، خواننده و آهنگساز، با انتشار ویدیویی از بازگشت خود به ایران پس از حدود ۲۰ سال خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/684725" target="_blank">📅 15:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684723">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزیر خارجه قطر و عراقچی در تهران دیدار کردند.
🔹
شرکت ملی پالایش و پخش فرآورده‌های نفتی: میانگین مصرف بنزین به ۱۳۲ میلیون لیتر در روز رسید.
🔹
روسیه: همراه با ایران برای حذف فشارهای تحریمی تلاش خواهیم کرد.
🔹
ترکیه از تل‌آویو خواست فورا به حملات علیه سوریه پایان دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/684723" target="_blank">📅 15:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684722">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e1139a9e.mp4?token=Is0wwzHfLI8_aXZstMnNbNfJgUkBHcgDNfnOtvG-132fJidLRh9FTbKSZrJaydi9vJUZrOHjesYgELN9VVDZq9NT8Xx2FPWJ5xtb01bapNtV5WwHlq80P_OhKaRCry0pm5GnGlGnb4mFazMddbS_xOqFI7VfJmSnolwEPM6qgTfY38_chS1X3CcW676puPN--clFnRN6AuvLX85zNkYcxZ-dSRAEbYy74o4c7h5fZh7xIS1g1m2u_8BBlPH1EpPznXuaGW46AG3SMCn_itUAeyfyhcXRSv7K5zco-OkPz0gk3FJYsNprm_q4W11zrAppXRFAyboe5qTi100xH1DALw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e1139a9e.mp4?token=Is0wwzHfLI8_aXZstMnNbNfJgUkBHcgDNfnOtvG-132fJidLRh9FTbKSZrJaydi9vJUZrOHjesYgELN9VVDZq9NT8Xx2FPWJ5xtb01bapNtV5WwHlq80P_OhKaRCry0pm5GnGlGnb4mFazMddbS_xOqFI7VfJmSnolwEPM6qgTfY38_chS1X3CcW676puPN--clFnRN6AuvLX85zNkYcxZ-dSRAEbYy74o4c7h5fZh7xIS1g1m2u_8BBlPH1EpPznXuaGW46AG3SMCn_itUAeyfyhcXRSv7K5zco-OkPz0gk3FJYsNprm_q4W11zrAppXRFAyboe5qTi100xH1DALw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیایید سیم کشی کولر گازی اسپیلت رو ببینیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/684722" target="_blank">📅 14:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684721">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d45f1db5f4.mp4?token=KiVh9K7h2SwYl4lMYqUrL7GHmgANYxqI3WkFUlnwDVbiPZL6q1PYtJhq1A7eVN_9RZlW-FrMliZi7D7Dc1AWel_Q6XnnGQdRS5y1r3pEcueTynXZ8cYtTSjTgY5CzFzAr1S80AZLvg6q6U0xLAht9i-N_CqRal1JPPxLn1P6ynoNCY_HUCDLXEeJzjywTFPM868GY8Q3ahZ778UPR-UC-biRuAlsELG47KHo29r9gX6XjHqNynLqO6IyndTPAFcADAikhYrX-I7VYGHiSMJPR3b2L-jM2uoVKa_XAJYBvgsf8CIbsJISbf45FimFeVaTIBaO3cbwpluUmZAOB-kiNw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d45f1db5f4.mp4?token=KiVh9K7h2SwYl4lMYqUrL7GHmgANYxqI3WkFUlnwDVbiPZL6q1PYtJhq1A7eVN_9RZlW-FrMliZi7D7Dc1AWel_Q6XnnGQdRS5y1r3pEcueTynXZ8cYtTSjTgY5CzFzAr1S80AZLvg6q6U0xLAht9i-N_CqRal1JPPxLn1P6ynoNCY_HUCDLXEeJzjywTFPM868GY8Q3ahZ778UPR-UC-biRuAlsELG47KHo29r9gX6XjHqNynLqO6IyndTPAFcADAikhYrX-I7VYGHiSMJPR3b2L-jM2uoVKa_XAJYBvgsf8CIbsJISbf45FimFeVaTIBaO3cbwpluUmZAOB-kiNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، خبرنگار جبهه مقاومت: برخی شهرهای جنوب لبنان به دلیل حملات رژیم صهیونیستی و نابودی زیرساخت‌ها خالی از سکنه شده‌اند/ اقدام برای متوقف کردن رژیم صهیونیستی و کمک به مقاومت، امروز بسیار مهم است/ وزیر جنگ رژیم صهیونیستی با ورود غیرقانونی به خاک سوریه، رئیس‌جمهور خودخوانده این کشور را تهدید کرد/ این اقدامات در آستانه انتخابات سرنوشت‌ساز نتانیاهو، پیوست سیاسی دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/684721" target="_blank">📅 14:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684720">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1450be839.mp4?token=G7egWwrH_jX94GAw1vhz3XwadwDovBH42fmx-665AKhVvJLyWq5xvKGHHLwEPP6UuZRWvIghKB4S0ZrPBxO-_5JOV1ZldPaorentMIM1Jlh5CKEF8F4loUScMl9P2RfzwTPe91cg3XPxiZ_HzmxYLFg31XKanYPjdoIzGeIylVeCzS3n0Vl8pWN4f0dCAsHbAC--ZeELcZlHb76DJeuWLg7_CwM73s5m113dgMvAkETZH2tktB6iVt8zhhTpNMHozPxpPEUxAmiBIeyMrBo9XIMuGal2azjQMMAuRcjCGcbmrJkiAbUYCzfJLYNjT8NhqJEkOikmymPigT7oYWYDELqIIMHQu2XuSAl1p4ItYZWu30xGZuxNqnYJtGpYljZaFiMCIlSeYUxvILo3x1cKhlxDDO95H-WjHU_XNON4aF1yQxlw3OItFEdFK_Fwmh8S63qtZo15T-ohLcoBmSdHBXkZ-rrNOnQkQcbTuIGd-A400YJPSqf656Sa_OkW3YeP-d1JYFxf0hvu6MbehA8tAlCIRVaqSTu72k408UC8OEymg1mQmuoQ2UUnkqV0nTETulfDkFOTir2hBBw8haCtR3FvKd_f_0bxNQBK460iW7knmruzvhCF4YYU-VCAnfmzxZplmLpfrLhtqgkfI2-EIXq2Ce5lIqqKQ5Jz12EmB28" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1450be839.mp4?token=G7egWwrH_jX94GAw1vhz3XwadwDovBH42fmx-665AKhVvJLyWq5xvKGHHLwEPP6UuZRWvIghKB4S0ZrPBxO-_5JOV1ZldPaorentMIM1Jlh5CKEF8F4loUScMl9P2RfzwTPe91cg3XPxiZ_HzmxYLFg31XKanYPjdoIzGeIylVeCzS3n0Vl8pWN4f0dCAsHbAC--ZeELcZlHb76DJeuWLg7_CwM73s5m113dgMvAkETZH2tktB6iVt8zhhTpNMHozPxpPEUxAmiBIeyMrBo9XIMuGal2azjQMMAuRcjCGcbmrJkiAbUYCzfJLYNjT8NhqJEkOikmymPigT7oYWYDELqIIMHQu2XuSAl1p4ItYZWu30xGZuxNqnYJtGpYljZaFiMCIlSeYUxvILo3x1cKhlxDDO95H-WjHU_XNON4aF1yQxlw3OItFEdFK_Fwmh8S63qtZo15T-ohLcoBmSdHBXkZ-rrNOnQkQcbTuIGd-A400YJPSqf656Sa_OkW3YeP-d1JYFxf0hvu6MbehA8tAlCIRVaqSTu72k408UC8OEymg1mQmuoQ2UUnkqV0nTETulfDkFOTir2hBBw8haCtR3FvKd_f_0bxNQBK460iW7knmruzvhCF4YYU-VCAnfmzxZplmLpfrLhtqgkfI2-EIXq2Ce5lIqqKQ5Jz12EmB28" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله تند مجری آمریکایی به ترامپ: احمق‌ترین، تنبل‌ترین و بی‌برنامه‌ترین رئیس‌جمهور تاریخ
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/684720" target="_blank">📅 14:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684719">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd78c1c30d.mp4?token=WNGTTWz8kENoUtDIgpg1z7iahwGoBiRQdqgBiNtOlXvphddJV0O5TK07y-tWQnF7m-P7-hM5xVVAlzz8gM4R5lTflEhY1CRCiUXu0NwPl_TeYW5rB5JhfPiB3RGXxtce7IhltGEieELxSE0FjacOgfzkeQXcyh4TbQ6oS09K0TdEi610OE-NfAxNi1a0GzIQ-QokMEayfOBwJqEDAfE8Gg7-3EXu3FP48GOXgr5j6WqON3tepVMrtjEE87YFu6kGkols_noYAsKpUjQ6cUhgSbqTimuiTI2x1UjM1B1pEU3QfgrSfIr1S3ehF5Pv9z15q7Plfe65KFrSdrSXk_d9Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd78c1c30d.mp4?token=WNGTTWz8kENoUtDIgpg1z7iahwGoBiRQdqgBiNtOlXvphddJV0O5TK07y-tWQnF7m-P7-hM5xVVAlzz8gM4R5lTflEhY1CRCiUXu0NwPl_TeYW5rB5JhfPiB3RGXxtce7IhltGEieELxSE0FjacOgfzkeQXcyh4TbQ6oS09K0TdEi610OE-NfAxNi1a0GzIQ-QokMEayfOBwJqEDAfE8Gg7-3EXu3FP48GOXgr5j6WqON3tepVMrtjEE87YFu6kGkols_noYAsKpUjQ6cUhgSbqTimuiTI2x1UjM1B1pEU3QfgrSfIr1S3ehF5Pv9z15q7Plfe65KFrSdrSXk_d9Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کروکودیل هم اگر زنده بود، احتمالاً قیمت کفشش را باور نمی‌کرد!
🐊
🔹
یک جفت کفش از پوست کروکودیل با قیمت ۱۰ میلیارد تومان؛ نمونه‌ای عجیب از فاصله قیمت‌ها در بازار کالاهای لوکس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/684719" target="_blank">📅 14:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684718">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
از مدیریت پول تا کسب درآمد؛ راه‌های ساده برای بهتر چرخاندن زندگی
🔹
#چرخ_زندگی
، کمپینی است که مسیر راه‌اندازی کسب‌وکارهای خانگی را از سرمایه اولیه و بسیار کم را تا تولید و توزیع و اولین درآمد را، ساده و کاربردی بررسی می‌کند. مطالب منتشر شده در راستای درآمدزایی ساده در منزل را ببینید و از امروز دست به کار شوید
🤩
🔹
یک قدم تا درآمد
▪️
با یک میلیون، میشه شروع کرد؟
🔹
اگر آخر ماه نمی‌دانید پولتان کجا خرج شده، این محتوا مخصوص شماست
▪️
آموزش میوه خشک کردن به روش سنتی
🔹
روش ساده دیگر برای تهیه میوه خشک د خانه
▪️
۳ قانون مهم مدیریت پول
🔹
جدول زمان‌بندی خشک کردن میوه‌ها با سرخ‌کن
▪️
دو تله مالی پنهان که هر روز تو رو فقیرتر میکنه
🔹
چرا بعضی میوه‌های خشک مثل نمونه‌های بازار نمی‌شوند؟
▪️
تکنیک ساده کم کردن مخارج
🔹
آموزش شمع‌سازی و کسب درآمد
▪️
قانون مدیریت پول
🔹
ساخت قند تزئینی و کسب درآمد
▪️
از یک پارچه ساده تا یک کسب‌وکار خانگی
🔹
چطوری با حقوق ۳۰ میلیون پس‌انداز کنیم؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/684718" target="_blank">📅 14:37 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684717">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
ضربه سنگین قوه قضائیه به زمین‌خواران/ انهدام شبکه بزرگ جعل اسناد با ۴۸ بازداشتی
🔹
مرکز حفاظت و اطلاعات قوه قضائیه در اقدامی قاطع، یک شبکه حرفه‌ای جعل اسناد و زمین‌خواری را متلاشی کرد.
🔹
اعضای این باند با سندسازی غیرقانونی، ده‌ها هکتار از اراضی شهری به ارزش هزاران میلیارد تومان را تصاحب کرده بودند که سرانجام در چنگال قانون گرفتار شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/684717" target="_blank">📅 14:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684716">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnappBimeh | اسنپ‌بیمه</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LoM4NO7c4nUu4N_nCUz6y7QVw4yPJWMtjxkq_ECdL4LtsjCUF5iA9570RySHox_zYe3QDms0aREyllbb9CBw43bW5H-RwKC8CUG3pvJIFdoWqd3cda_39XMQiU4A6-VUxyiEnt4d2Rafj3BgyoipoWF0v0nPp8Ka4rUjlSRfZeeqlRvP5w3UNNWYFzB_pFa7G9Py3q-M_esbe-0y_5GAWcB91Hg0WiF11RdhTJNikgMBPDRTOfRrZcLiodpqOCK3RhSxxBCmaZw58Go2YYtI9dJQ6rbnNOee_Ilx5pZX7Wjw-pBYyLNs8cTs_Pe2EzWwJIbW4mjX8TXnSwz5rQH48A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شانس برنده شدن باهاته!
🎁
تا ۲۰ شهریور
با خرید هر بیمه‌ای از اسنپ‌بیمه در
قرعه‌کشی موتور یاماها، آیفون 17 و PS5
شرکت می‌کنی
🤩
چرا با اسنپ‌بیمه بیمه بگیرم؟
✅
با پرداخت قسطی هم می‌تونی تخفیف بگیری
✅
برای هر سوال یا مشکلی، پشتیبانی ۲۴ساعته داری
✅
و در قرعه‌کشی
موتور یاماها، iphone 17 و PS5
شرکت می‌کنی
این فرصت رو از دست نده؛ چون با اسنپ‌بیمه شانس باهاته
💙
وارد لینک زیر شو و جایزه ببر:
👇
👇
👇
https://l.snpy.ir/ixsth
https://l.snpy.ir/ixsth
https://l.snpy.ir/ixsth</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/684716" target="_blank">📅 14:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684715">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f683783704.mp4?token=oqwlWdTz10Q-jtwSgXO0EpKhfuQlT-i7-WoYQLVIpI_P-RyhQ30h3HnWxDSNkkUm6zb9eUY5YU3TFYPylC3fKDCe-OcTBOX_A3pBFR9GbcEvewz979szs3XFDHYpNtK4elJPbSzmaDVN_XBdePfebllgcB20_bSeTamotXLzO0pZUByi5393TGd_M48Q9sc07MJ2GYop3mEU5gabNf_r5uCbXsCJig81jGysVyYmYWekwqm3w63r6HT1tXnlcKKBx0qhfpPWK_PdhM_4rwaIOWHoEyX1up4VUmkxEnDyNIPS-8lvgYgY5wqkCGSDJIRDMncD5CeOFpdhmWGNYpxW8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f683783704.mp4?token=oqwlWdTz10Q-jtwSgXO0EpKhfuQlT-i7-WoYQLVIpI_P-RyhQ30h3HnWxDSNkkUm6zb9eUY5YU3TFYPylC3fKDCe-OcTBOX_A3pBFR9GbcEvewz979szs3XFDHYpNtK4elJPbSzmaDVN_XBdePfebllgcB20_bSeTamotXLzO0pZUByi5393TGd_M48Q9sc07MJ2GYop3mEU5gabNf_r5uCbXsCJig81jGysVyYmYWekwqm3w63r6HT1tXnlcKKBx0qhfpPWK_PdhM_4rwaIOWHoEyX1up4VUmkxEnDyNIPS-8lvgYgY5wqkCGSDJIRDMncD5CeOFpdhmWGNYpxW8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر مستقیم به سمت ماه حرکت کنیم، چند وقت طول می‌کشد به آن برسیم؟
🌕
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/684715" target="_blank">📅 14:24 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684711">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
با اعلام باشگاه استقلال، شهر بصره عراق میزبان مسابقات این تیم در فصل جدید لیگ نخبگان آسیا شد.
🔹
ارتش رژیم صهیونیستی: بودجه ما در وضعیت بحرانی قرار دارد.
🔹
روسیه: پیشروی نیروها در تمام جبهه‌ها با سرعت ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/684711" target="_blank">📅 14:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684709">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pj46ZQRgXShUyzL0tyQkchm7VPCjJTOGYXXfZNJmndd1pruFuwYEaWUd3zsfRLCtJHoc-gGMHe0sMazQx7v302CjPQI9Ieope3P5dw0h_CVagDyAvfy6U7TiG107Ax2GCFQ0Hgn-XNcycuqO5vn1QnM2d3EwoAKt6xIJZZJPP0u89dC-WTnF5WUflIifK-uFIxocF9iNaHCqpw0poEfMAiL8T-wAMC6NElkbSwLKW24k_6ywluPxdPRUJJ_sdhH2bdds8D6D1zzgyEBV4TZvTPo2AT8vIlYgekYKD39lWngEQ6LOOo5sik7aCftInUdpCWFajw9j2CBBcl-k4sh0ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۵ شهریور ۱۴۰۵؛ ساعت ۱۳:۵۰
🔹
دلار آزاد، امروز به ۲۰۱ هزار و ۱۰۰ تومان رسید.
🔹
با وجود این توقف رشد موقت، دلار در طول یک هفته گذشته رشد ۵.۲ درصدی «معادل ۱۰ هزار تومان افزایش» را ثبت کرده است./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/684709" target="_blank">📅 14:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684708">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tw-qNFd0_aEbTd25b7Qih0_Mw8UUUy00DjstiNL1gmO6nSUlbEbWYY2G0u43tRMd-dttCV1OH36xJJTQyEUtThUJuLUtMoEQz1wlQLsLXfGm6XvSyYNuIcz_v8UrpRT6qlOPfPrZHHhTmdGLA0SyiGYmKwaE9-dYhscnHV_JW0RIbl99PJa26UDBOqRHSl7s0WXRvD3QBMpbJDnTBKVx0cKME6UZU1PEc_zYyJM3hmeGi4KpvxDsd3sxE4kMzPLvKP1LqPHZDH8RWOZ6D-jo6nZERRjMTROVWWBqA-RssiDngeuO7IPf-h0TO-lCqVSCzqflsKweZheh55axE1FC3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با یک سوزن، لباس‌های ایراددارتون رو با یک زرافه خوشگل تزئین کنین و لذت ببرین  #فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/684708" target="_blank">📅 14:01 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684707">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
کالابرگ سرپرستان خانوار دارای رقم انتهایی کدملی ۷، ۸ و ۹ شارژ شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/684707" target="_blank">📅 13:51 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684706">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a204beb43.mp4?token=YoF6xafpN8Wlr3xSlDamXJ-dfw9XjnhrtgK_qLokEOq7g6pSlv73Aj9RRqP6RZ_vEMHzeArZKdwnjE6D04RpV_6_n9HE7QPSmgL5U-cEGxKrHH7kkIaVXnY-00jg48_QBboJq8eQdryndfkWPyfaxIIyrNixQHJBn9lVlp2PbOCG51SnNYsTAM0ReyE5pqcyrl8wjm5GMoawD3KaPis7BIVc55vpGxynXV-THO81gN9sqKWLIdqQaELWn6y_oN2EwueRpg9vI3KviXRKoyKCpMjzypMVhDSbeVbeX2e5Fk_WhSMWTS7TLbjhu5salqSk79U6OzRHq4YYp7vNQCt-jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a204beb43.mp4?token=YoF6xafpN8Wlr3xSlDamXJ-dfw9XjnhrtgK_qLokEOq7g6pSlv73Aj9RRqP6RZ_vEMHzeArZKdwnjE6D04RpV_6_n9HE7QPSmgL5U-cEGxKrHH7kkIaVXnY-00jg48_QBboJq8eQdryndfkWPyfaxIIyrNixQHJBn9lVlp2PbOCG51SnNYsTAM0ReyE5pqcyrl8wjm5GMoawD3KaPis7BIVc55vpGxynXV-THO81gN9sqKWLIdqQaELWn6y_oN2EwueRpg9vI3KviXRKoyKCpMjzypMVhDSbeVbeX2e5Fk_WhSMWTS7TLbjhu5salqSk79U6OzRHq4YYp7vNQCt-jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کلیپی را که می‌بینید، در ابتدا فکر می‌کنید افتتاح پالایشگاه است، اما آخرش معلوم می‌شود افتتاح یک پمپ‌ بنزین ۴ نازله در یاسوج با حضور استاندار و سایر مسئولان استان
است
#اخبار_کهگیلویه_و_بویراحمد
در فضای مجازی
👇
@akhbar_kohgiluyevaboyerahmad</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/684706" target="_blank">📅 13:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684704">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/djOHrVbma5mAsvPkosLeY6vwQ0zQ3LDgT1eymXxG4Z-ha_cgf0kJewLnajQc5GBPLCczKJOpMAOkVTL_Ym0VmVJv378v5RszOWw5QxKHLguMitDV2zg_DYmHP1sW0F_k6B5qbZjCatGELsA8baTjvIxRF49CF6NOZZEc1vA144LAqGf0-IaH1NgqFkX745f-AQjnR8ox5Qjo2LavH7WvrLRkIFTSFcFFuR_TOtw6PbY_XgLNUJUwJvrSB2Prcvtgjr2MPiGAZtYhBLVKta_FfuPv68uY6OwsELXZV7ji7XnDIYaadcJO5UWaoON7G2BnTMpUq_4Jpwsj1cG5aZDdrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/2918231a66.mp4?token=gfVIkeAVQSGlvnJ8ck9WoUNjTugKtZx0Ewp9U6ibC_e-3l0YMNZw5CmVbe3-QWoVOqTSzUFu6kGYnRlDHLsQZ4MLgZpyK1IyQc-E0YxftdIShFAYnaTGk8Q835_1dflkuMvbN9t_oLHtloLAFsKnFPsL0J63x-3tuISPjgCfyHP9rHkfVLAhLkcldK-s09wH-UbefD-fvRJsLdWvbw1XVfpp8iNWBe9a5HOeIV_fDkkr3T7mDXpX6juKNu8_mf3V8B_H1G3apcIrozY1Vkg9lB71MHFfxSvsjAH-XJwztYWcwvEvPNdvt3zS2s3m_YPHbBywsiqOwkahV4hXy_Hq2w" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/2918231a66.mp4?token=gfVIkeAVQSGlvnJ8ck9WoUNjTugKtZx0Ewp9U6ibC_e-3l0YMNZw5CmVbe3-QWoVOqTSzUFu6kGYnRlDHLsQZ4MLgZpyK1IyQc-E0YxftdIShFAYnaTGk8Q835_1dflkuMvbN9t_oLHtloLAFsKnFPsL0J63x-3tuISPjgCfyHP9rHkfVLAhLkcldK-s09wH-UbefD-fvRJsLdWvbw1XVfpp8iNWBe9a5HOeIV_fDkkr3T7mDXpX6juKNu8_mf3V8B_H1G3apcIrozY1Vkg9lB71MHFfxSvsjAH-XJwztYWcwvEvPNdvt3zS2s3m_YPHbBywsiqOwkahV4hXy_Hq2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رکورد تاریخی طولانی‌ترین ست والیبال شکسته شد
🔹
در دیدار اخیر تیم‌های ملی آلمان و ایتالیا، رکورد پیشین آرژانتین و لهستان (۵۰-۴۸) جابه‌جا شد. ست نخست این بازی ۸۹ دقیقه به طول انجامید و با نتیجه ۶۶ بر ۶۴ به سود آلمان پایان یافت؛ رکوردی بی‌سابقه با رد و بدل شدن ۱۳۰ امتیاز در یک ست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/684704" target="_blank">📅 13:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684703">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82bd1ef61d.mp4?token=bhocYrWD4QACqWnHCWEQyBHwpc3IyroNi9Mkex7CWEQR4XWg_VP1lAZSETw-kFmN4Wo2XkcqFL1T7zghIw9mK5KFsOiKqF2tvv-kc07LMJYe9aUV4Q6Nh-Wzm5aK394UG8mHEXIZm5ZHTfBnCAWCv3iB0JRdzuOTYfOYR1UUZ0ebDGVVr2muZnA3Pn_UQrxBJQ8qJ0lAwD8ppPHS_dti7nxia7_vGq7vC8LzDPJ1Q2lgnUo6nyLiy5o8E816NZSfPFw3M4Qwxu11kCtSzuqU8Bv6H-2iRMszxOr_2QeyXY21xXotlRVj40cVLS48K0HLw5STHty0o3LObjRyh1UUSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82bd1ef61d.mp4?token=bhocYrWD4QACqWnHCWEQyBHwpc3IyroNi9Mkex7CWEQR4XWg_VP1lAZSETw-kFmN4Wo2XkcqFL1T7zghIw9mK5KFsOiKqF2tvv-kc07LMJYe9aUV4Q6Nh-Wzm5aK394UG8mHEXIZm5ZHTfBnCAWCv3iB0JRdzuOTYfOYR1UUZ0ebDGVVr2muZnA3Pn_UQrxBJQ8qJ0lAwD8ppPHS_dti7nxia7_vGq7vC8LzDPJ1Q2lgnUo6nyLiy5o8E816NZSfPFw3M4Qwxu11kCtSzuqU8Bv6H-2iRMszxOr_2QeyXY21xXotlRVj40cVLS48K0HLw5STHty0o3LObjRyh1UUSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گاهی یک دست، یک قلم و یک جمله کافی‌ست؛ برای اینکه سکوت، دیگر سکوت نماند
🇮🇷
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/684703" target="_blank">📅 13:38 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684702">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5db8181f96.mp4?token=MwaAC0vFnq86jpmQ3L-VOEPEpRiQ8bZtwXVzLGYxSdU_wNoun_LlUbikkqMUEY_KXYS1MeHSDTRY0jLPCfXPynEYxUzlipG-B2ZnmGnEo0Osf-bLePgyKCKrGNpvqy0W7TetbS0D8CLp_CW9xf-_dmkKqXUNn1eD-CO8Ot6CxXyff4-RDqIle10d-vLYUHh_lsPY_b5H4K45fLbj5o6wOuyypKX1mjQ4YL-KWpun6iokdH0khKG_bdqNdMb4lpDYqdfCbXVWYqALX6EeBsPdAsaZP-ep5Pc_R2TPrmklpA24DMVUx8bN6vivDjo1GaWXjCkmUqb6SEdyRogTj_7Obw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5db8181f96.mp4?token=MwaAC0vFnq86jpmQ3L-VOEPEpRiQ8bZtwXVzLGYxSdU_wNoun_LlUbikkqMUEY_KXYS1MeHSDTRY0jLPCfXPynEYxUzlipG-B2ZnmGnEo0Osf-bLePgyKCKrGNpvqy0W7TetbS0D8CLp_CW9xf-_dmkKqXUNn1eD-CO8Ot6CxXyff4-RDqIle10d-vLYUHh_lsPY_b5H4K45fLbj5o6wOuyypKX1mjQ4YL-KWpun6iokdH0khKG_bdqNdMb4lpDYqdfCbXVWYqALX6EeBsPdAsaZP-ep5Pc_R2TPrmklpA24DMVUx8bN6vivDjo1GaWXjCkmUqb6SEdyRogTj_7Obw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درگیری شدید میان گندوزی و بازیکنان لیون در تونل ورزشگاه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/684702" target="_blank">📅 13:21 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684701">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08cb3a2286.mp4?token=fNAfZrwg1HaVz1tUB_ZaoQ0ZNrvYnj88DmuzhuGd3esesRka5jAln5rG9-45elFCw-VbxS7jGRsBFiGpgHqWm-KLJ81SQxsviiS7dxKuiDnrPTLjXBpcWSIhOX2o26sR_t0bqG4hvL2CiPAP3r0UCo4swydqbbYVeuM9PCYwfrhrJNHUiRuy4HtW8YZ2uRHQ6MkhKfBYylI98nZy1ma5Ufi55fiKyf2JOdm6qtohOTOM2qTJylZ5rH6nLps_LXNJ3qkFGSgtEF5iTKV45bFee6_rF334tiD7aYCR1qSsFJToNGL2pGdb4shGGOOVJFfBULeYk2R8GLQsHD5nFQESRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08cb3a2286.mp4?token=fNAfZrwg1HaVz1tUB_ZaoQ0ZNrvYnj88DmuzhuGd3esesRka5jAln5rG9-45elFCw-VbxS7jGRsBFiGpgHqWm-KLJ81SQxsviiS7dxKuiDnrPTLjXBpcWSIhOX2o26sR_t0bqG4hvL2CiPAP3r0UCo4swydqbbYVeuM9PCYwfrhrJNHUiRuy4HtW8YZ2uRHQ6MkhKfBYylI98nZy1ma5Ufi55fiKyf2JOdm6qtohOTOM2qTJylZ5rH6nLps_LXNJ3qkFGSgtEF5iTKV45bFee6_rF334tiD7aYCR1qSsFJToNGL2pGdb4shGGOOVJFfBULeYk2R8GLQsHD5nFQESRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غلتیدن غول‌های سنگی در سیلاب مرگبار نپال
🔹
سی ان ان به نقل از منابع محلی اعلام کرد که تعداد قربانیان سیل ویرانگر در مرز نپال و چین به بیش از ۱۶۰ نفر افزایش پیدا کرده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/684701" target="_blank">📅 13:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684700">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
قالیباف: با تلاش دولت و ایستادگی مردم در جنگ اقتصادی، پشت دشمن‌ به خاک مالیده خواهد شد
رئیس‌مجلس:
🔹
در شرایطی که جنگ پیامدهایی بر اقتصاد کشور ایجاد کرده است و دشمن همه ظرفیت‌های خود را برای فشار بر ملت ایران به میدان آورده در چنین شرایطی گوش فرا دادن به توصیه‌های موکد رهبری معظم انقلاب مبنی بر وحدت، انسجام ملی و اعتماد به مسئولین مهم‌ترین پشتوانه کارگزاران کشور برای عبور از چالش ها و اعتلای نام ایران اسلامی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/684700" target="_blank">📅 13:08 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684699">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gvc_PrbwwsKNkKOvGfwUnpLWPODMu8Vl65KMHmJQM4kalBHwYx3Qw6SOqU70FPXk-p6ovHxgWcm6Q7c0U-YmoEzMw0gyNvMjyPs1wOVtRKRR9sZTf9d6PYzW9CGtA73ItemDHWb877bNncJcierV-8zBuTAWruzsukRvqC943yRwBnzS-slqhdRsQsewpTM2plbrmHkKIcKNQAenYOWHpV53IMi72pwbtsVSga4sw0TjpUWJ_9Qpnb-CiaLpJ-H8wohOCZuivc4HeswaIYNEDHJ-dNvoqGbInAQyFQorpW4DVb_tq_h7wUdS4L_RgC11qOqs1eZHHShPZOLaRms6pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برت اریکسون، کارشناس آمریکایی جرایم مالی و ژئوپلیتیک: ایران کوبا نیست. ایران می‌تواند و در حال حاضر هم کمپین جنگ اقتصادی خودش را به راه انداخته. در نهایت، ما باز هم شکست خواهیم خورد؛ فقط این بار با رنج و آسیب بی‌دلیل بیشتر به غیرنظامیان.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/684699" target="_blank">📅 13:06 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684698">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0fe4e5305.mp4?token=R966JjL2RGCc1rouNQvCk0X-nU9d_DHqozzFDnTykYWHddmIS3nWRewhHcWPUFHc3fFGMKkRnkpAFwoutcWF8ZC0cPTh3fSxSf05PSdXwfYaNa6dFcwoVsMgj5B8W60FVh5cG-eToniIH7mkNG-jD97RDY1Lnd2jYUUY-mgaLH2iocNs_N0rqIHP3-l18XpWM9FtTZ_4iluU_0GB8eG0wCUATe2rO-Ujo2QOXVn5EptyGLyz9uxgWyTQnufZ_b3qPmm3QHJQ1uOwproYwT8728heJiM83DB9Q19nUKjLPwN_YqxDvgv_H2TSkFLMIs6iwUv9unQVFc7UYRXdLhAdaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0fe4e5305.mp4?token=R966JjL2RGCc1rouNQvCk0X-nU9d_DHqozzFDnTykYWHddmIS3nWRewhHcWPUFHc3fFGMKkRnkpAFwoutcWF8ZC0cPTh3fSxSf05PSdXwfYaNa6dFcwoVsMgj5B8W60FVh5cG-eToniIH7mkNG-jD97RDY1Lnd2jYUUY-mgaLH2iocNs_N0rqIHP3-l18XpWM9FtTZ_4iluU_0GB8eG0wCUATe2rO-Ujo2QOXVn5EptyGLyz9uxgWyTQnufZ_b3qPmm3QHJQ1uOwproYwT8728heJiM83DB9Q19nUKjLPwN_YqxDvgv_H2TSkFLMIs6iwUv9unQVFc7UYRXdLhAdaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلمی از آتش‌سوزی در انبار کارخانه فرآورده‌های پلاستیکی در آق‌قلا
#اخبار_گلستان
در فضای مجازی
👇
@AkhbareGolestan</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/684698" target="_blank">📅 13:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684697">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPrupbQ1NF6kLwAT3vGu2I_tx4W_h7VMWlAk1T4NVbdxXPulcUZsyNLgaEK24naI9Zl-NFEgkDNyLSxhILI1ZRzMEYmy4DjFA221SaJmYFtIil7bhu1xl0He39c4VxD1M79B8ZW9LwICqMVR-S1LQEhjn18VVxIBU1qlBVFA0rMzyfvcRO6KwJASL_RdIcIScJyGZw_gy_-fEZexOODAxuqjA-Mz8xFoKOvD0EJ7r_sxPddX-Ltq_BkbdvgG29JE1GUQSZNg2drOPI3UfTgRxsCuYxOM-HlslOMAjVYCi9XX7s2_yam0RNxWMfOWz8-RMmwj9IFBRjVSXabFAqhCaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
علیرضا کاظمی مدیرعامل شرکت «توسعه نیشکر و صنایع جانبی آن» شد
🔹
علیرضا کاظمی پس از چند ماه فعالیت به‌عنوان سرپرست شرکت «توسعه نیشکر و صنایع جانبی آن» با اتفاق نظر اعضای هیئت‌مدیره به عنوان مدیرعامل و نایب‌رئیس هیات‌مدیره این مجموعه انتخاب شد. این انتخاب پس از طی فرآیندهای قانونی و نظارتی، صورت گرفته و تأیید صلاحیت وی از سوی سازمان بورس و اوراق بهادار، در کنار نظر مثبت نهادهای نظارتی، پشتوانه حرفه‌ای و قانونی این انتصاب محسوب می‌شود.
🔹
مدیرعاملی دکتر علیرضا کاظمی همچنین از اعتماد بانک صادرات ایران به عنوان سهامدار عمده شرکت برخوردار است. انتظار می‌رود با تثبیت مدیریت در شرکت «توسعه نیشکر و صنایع جانبی آن» برنامه‌های این مجموعه بزرگ اقتصادی با تمرکز بر افزایش تولید، ارتقای بهره‌وری، توسعه صنایع جانبی و تقویت سودآوری با شتاب بیشتری دنبال شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/684697" target="_blank">📅 13:01 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684696">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
پاکستان: فرمانده ارتش به عنوان فرستاده ترامپ به تهران نرفت
سخنگوی وزارت امور خارجه پاکستان:
🔹
ادعای سفر فرمانده ارتش به عنوان نماینده ترامپ نادرست است؛ سفر او در چارچوب میانجی‌گری پاکستان بوده.
🔹
تحریم‌های یکجانبه علیه ایران مغایر قوانین بین‌المللی است و پیامدهای منفی دارد.
🔹
جنگ اقتصادی با ایران باید از طریق دیپلماسی و گفت‌وگو حل شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/684696" target="_blank">📅 12:58 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684695">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ba4f2959b.mp4?token=d_BrCIOoKq54lpHCON1OVXbRT4ABeDsjnG_nIKN1NZE1P3fQM-bmXfD3C-orolcg3ys1e1KIiApqVNuBR68WL-dTOy9UVxo9CY5NlcWUNuGt_4EFdyvt1ybdqgckgSeMIxmHLJnQCagGh_FYv15XBkmckAp4pIULa50FRjmoMfKKY1nK1jO39-MyXKwaZJ55nd9Kw7dcpz7JX-PmwnYQFdeIjljzVMXn1R2wKar_dsIPBZDL--ZJv7yUQ2iFaRoaiyS4s_Oo3GASjHErMCu8GH1t92sfUwY7I9oKDgZvyR_jW1SZaUcsHVeTB3W7mLXxkfofpI5h4u6jAJAGE_gbWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ba4f2959b.mp4?token=d_BrCIOoKq54lpHCON1OVXbRT4ABeDsjnG_nIKN1NZE1P3fQM-bmXfD3C-orolcg3ys1e1KIiApqVNuBR68WL-dTOy9UVxo9CY5NlcWUNuGt_4EFdyvt1ybdqgckgSeMIxmHLJnQCagGh_FYv15XBkmckAp4pIULa50FRjmoMfKKY1nK1jO39-MyXKwaZJ55nd9Kw7dcpz7JX-PmwnYQFdeIjljzVMXn1R2wKar_dsIPBZDL--ZJv7yUQ2iFaRoaiyS4s_Oo3GASjHErMCu8GH1t92sfUwY7I9oKDgZvyR_jW1SZaUcsHVeTB3W7mLXxkfofpI5h4u6jAJAGE_gbWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شبیه‌ساز واقعی قلب که یک قلب را خارج از بدن در حال تپش نگه می‌دارد برای تحقیقات و آزمایش‌های پزشکی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/684695" target="_blank">📅 12:52 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684694">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60a272e55b.mp4?token=Ec86S_eZnLM35lRjsXmFCiRcdlVKqd4wtL0wgxWUxIFkIflLfoz-tSAUIjTkKAkS5SgrW8VHAgRXiMi2Zymn0UApz2POy7Ofxhb7efmOFa9lxM4a9lzF4nHJw2s5_ltGDbPp4jn86RIa9JK5N70wz7VsTdVhuIoTfjTspgV9m3XcsYDbfiDNMkhWPCSjyVkxzCXppNPPfFa2bAj-yyqsXIOKJudHMscRCd-VUjJ6dCfvrexnlwNki29UPrDW-mVn6c5U31d1yczeAE3KNc4FLonsPsn0F993jFDCLPBnzzKMLAGNNnGZ6vCtw3sPpMplOXPQv1ZGLJGKKTkPSxsAGHRwewaUYXFrCfhsJSJmEb3VQHY8IcIoL9NXf28tbnWWwWdixklk3cv3-5JVten6NztBV0EEV-EqX0fcyWNnj-WYc4uZbSeGnuTXjXHfMBD4jzNi_tbZfWhEJbCm5qmY8LmJpPXtFnAJtlqTbPWdgyli987mr-YqxImCLIFBzhjCwggv2P6p9B7gJlL93tqRQOWau1018q36dWvCbtTl-lYFFAZRZERsOKg9K9aIq6zpTBF__d0uAd3FoqXRVUaSwNYzoaQYxhmY1O280jt5MIw-PBWe9sJF5zXZ_JqKWY1iD8h0NzJoUTYNcBgrIhjpTIahQ8buYpZ-v1Di6DJBn1M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60a272e55b.mp4?token=Ec86S_eZnLM35lRjsXmFCiRcdlVKqd4wtL0wgxWUxIFkIflLfoz-tSAUIjTkKAkS5SgrW8VHAgRXiMi2Zymn0UApz2POy7Ofxhb7efmOFa9lxM4a9lzF4nHJw2s5_ltGDbPp4jn86RIa9JK5N70wz7VsTdVhuIoTfjTspgV9m3XcsYDbfiDNMkhWPCSjyVkxzCXppNPPfFa2bAj-yyqsXIOKJudHMscRCd-VUjJ6dCfvrexnlwNki29UPrDW-mVn6c5U31d1yczeAE3KNc4FLonsPsn0F993jFDCLPBnzzKMLAGNNnGZ6vCtw3sPpMplOXPQv1ZGLJGKKTkPSxsAGHRwewaUYXFrCfhsJSJmEb3VQHY8IcIoL9NXf28tbnWWwWdixklk3cv3-5JVten6NztBV0EEV-EqX0fcyWNnj-WYc4uZbSeGnuTXjXHfMBD4jzNi_tbZfWhEJbCm5qmY8LmJpPXtFnAJtlqTbPWdgyli987mr-YqxImCLIFBzhjCwggv2P6p9B7gJlL93tqRQOWau1018q36dWvCbtTl-lYFFAZRZERsOKg9K9aIq6zpTBF__d0uAd3FoqXRVUaSwNYzoaQYxhmY1O280jt5MIw-PBWe9sJF5zXZ_JqKWY1iD8h0NzJoUTYNcBgrIhjpTIahQ8buYpZ-v1Di6DJBn1M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیل در طائف عربستان خودروها را با خود برد
🔹
بارش شدید باران موجب جاری شدن سیل و آب‌گرفتگی مناطقی در طائف عربستان شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/684694" target="_blank">📅 12:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684693">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rud0l7Llpl5T0Rlf_4enQX9Alr4Vd0fnSzDtdoyVO4_S-TggWS-HBv3L4uBb2MdB1PC8GaYWfap-2RGwAlizYRBm0z7rScXU5uJ1GtfZGfnl5FGtmhFaqNQDGZ5qpSUU2FDLAheOSPEG-1yfrC61EN1pLcnuXuUFiqhJ_luYdEGdZo68It12Pyui1L4YA5bXfr1Q_MKppKxbnPNVREnqsWqpfc1pJfpaDRLZSfM38iBsooAKkOQbixZULP7n3yzBckWcEklIS37L9_Z_Vx4SA_lDup4ITpQ0CydSxRJ_Hr6vX1_Br-ll3ixEUUNMLcwrHdLkodD9ruUbd5G6-byRyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«یاور فتح»؛ روایتی از خدمت بی‌وقفه در روزهای جنگ
🔹
در اختتامیه بیست‌ویکمین جشنواره شهید رجایی با عنوان «روایت نصر»، وزارت راه و شهرسازی به پاس تداوم خدمت‌رسانی به مردم و نقش‌آفرینی مؤثر در روزهای جنگ، به‌عنوان دستگاه اجرایی برتر در بخش «یاور فتح» معرفی شد.
🔹
در این مراسم، از فرزانه صادق، وزیر راه و شهرسازی، به نمایندگی از مجموعه مدیران، متخصصان و کارکنانی که در روزهای دشوار، چرخه خدمت را متوقف نکردند، تجلیل به عمل آمد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/684693" target="_blank">📅 12:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684692">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1c9092ad.mp4?token=Thn7v7lok0sRAzoReu2abewQ5mo2aBx0YJuJk_Nv6FBTGJn7eRs4e3Id__UTHnf3Nc1uvFZZAHuuR526x1pw0KaTn09GQfBP1secvzcT5e5P913O2-bT-WLtiqC7MvLvnFIHKBdObkXs0GxPKgNQo0R392rS71S_Vb0NX3keOQoM16AKItiuvjCCjZcijiacQQ353rqYelzlgqRjyUvaCSGfCAZ0LmA-h3Ry2eL__uqUTkmcI0qfCywkjg3fCqtKjztGzmArZpi8H050RxANLkpR4MTu7dWlq1fEXrBLTphHX69uiQHyja8NYpPKZepSwo8J8Oc78wvOyHc0DyMPEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1c9092ad.mp4?token=Thn7v7lok0sRAzoReu2abewQ5mo2aBx0YJuJk_Nv6FBTGJn7eRs4e3Id__UTHnf3Nc1uvFZZAHuuR526x1pw0KaTn09GQfBP1secvzcT5e5P913O2-bT-WLtiqC7MvLvnFIHKBdObkXs0GxPKgNQo0R392rS71S_Vb0NX3keOQoM16AKItiuvjCCjZcijiacQQ353rqYelzlgqRjyUvaCSGfCAZ0LmA-h3Ry2eL__uqUTkmcI0qfCywkjg3fCqtKjztGzmArZpi8H050RxANLkpR4MTu7dWlq1fEXrBLTphHX69uiQHyja8NYpPKZepSwo8J8Oc78wvOyHc0DyMPEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سبدبافی؛ شروع یک درآمد خانگی با سرمایه کم
🔹
در کمپین #چرخ_زندگی تلاش می‌کنیم کسب‌وکارهایی را معرفی کنیم که با سرمایه کم، امکان شروع دارند و می‌توانند به تقویت اقتصاد خانواده‌ها، به‌خصوص برای بانوان، کمک کنند.
🔹
این بار  رفتیم سراغ یک کار ساده و جذاب خانگی:…</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/684692" target="_blank">📅 12:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684689">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45342c1858.mp4?token=H2p1FB77I5MxXW18raLyIlFMhiWYDtNZjLujM99-W2ligImOO8H-iLNkI7A7jJb3feVMQHhj05JFE8eCJ1bzPTlDaiyJjPkWMiFH8Aqks0uALEWZ4cmZ2FZWtPqcFO_AiZ_OWv00BHm5Biwpbx8FybncHXC9ap9yCfcc3x7g3Q4G1uoNxOle54wMYysPYMb43wkxrmVtVFkvffAaWgPiC9qbLapMVfGiu0gOt6gm2GZiFAIWeI25_7i3c6c_OG3WgfMecxRCry7qmox0SZQ3wrzG81cqQOQaowRHhNQitDtIIS95QqzoLwKPXC16fTw34ze6v1raD3uWXoV1jwuBKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45342c1858.mp4?token=H2p1FB77I5MxXW18raLyIlFMhiWYDtNZjLujM99-W2ligImOO8H-iLNkI7A7jJb3feVMQHhj05JFE8eCJ1bzPTlDaiyJjPkWMiFH8Aqks0uALEWZ4cmZ2FZWtPqcFO_AiZ_OWv00BHm5Biwpbx8FybncHXC9ap9yCfcc3x7g3Q4G1uoNxOle54wMYysPYMb43wkxrmVtVFkvffAaWgPiC9qbLapMVfGiu0gOt6gm2GZiFAIWeI25_7i3c6c_OG3WgfMecxRCry7qmox0SZQ3wrzG81cqQOQaowRHhNQitDtIIS95QqzoLwKPXC16fTw34ze6v1raD3uWXoV1jwuBKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از خارج کردن نفت به روش کشتی به کشتی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/684689" target="_blank">📅 12:20 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684688">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ffec3ed91.mp4?token=oCT_OXtOoRiYo28zMtqbc_cDX5fQsiTRWXArC1I1aPbPSCuv6yNhanmRxmJDpTz4GEauvfJq_aaolTHMTk7WvcoWhqUlV2sK_RF_CKXHJ21lGqISWoYscp02O74Z9lfBLwEBsr5uO1G1rcxd78UjXwb8_m15dj3HGn07T-r_ho6rcMGYsEK8a9yDSA2jciaFGkFs78ClZ2Iv5vB7bT6e1Q3WdyqRo1_pl2OvBF_c5JACCAJUq_kyb2Y21X7VVIrJd_cGvRsfj9YPf8l0rzyN6-UUuXsAhfbrjvTQ4bf4_xg39z04XJKhARTpgOhD-dBMWY5q1VyPIY5ruUPyWGzhWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ffec3ed91.mp4?token=oCT_OXtOoRiYo28zMtqbc_cDX5fQsiTRWXArC1I1aPbPSCuv6yNhanmRxmJDpTz4GEauvfJq_aaolTHMTk7WvcoWhqUlV2sK_RF_CKXHJ21lGqISWoYscp02O74Z9lfBLwEBsr5uO1G1rcxd78UjXwb8_m15dj3HGn07T-r_ho6rcMGYsEK8a9yDSA2jciaFGkFs78ClZ2Iv5vB7bT6e1Q3WdyqRo1_pl2OvBF_c5JACCAJUq_kyb2Y21X7VVIrJd_cGvRsfj9YPf8l0rzyN6-UUuXsAhfbrjvTQ4bf4_xg39z04XJKhARTpgOhD-dBMWY5q1VyPIY5ruUPyWGzhWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه آغاز سیل در مرز نپال و تبت؛ یخچال‌های هیمالیا فرو ریختند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/684688" target="_blank">📅 12:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684687">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/892a622da5.mp4?token=jGgOHRVc2Yf7an-vivYTluN3FBBzC6JfF0-ntwz7YEb5Mezknp_1iaw_wXxJJRSCj-6BzFvt3XSWFa-tOH_VN15T-tESfoO86K06-v_Aq6MwmEvW2hsMBd1lqnjLdyj_KiYt8QST6HfV05wb6kDnUL5iHjdaZjSta28Nis3yaPjrVDIxYTM33jvUgpzunk2cPJy8xwlgn5YEtH5Ez6mSb2xQ8u2SIN-_zl1D1lphdHVz4I4eLShJgDnTn24tR02BZyfdTtKtuzfFCvlqU5w0b6rz2AAzIhtvMZqfAvBTJojZ9oLBDqwTh4dHMr0Y6nFwhS_2OKhHZueJiLmptt4q_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/892a622da5.mp4?token=jGgOHRVc2Yf7an-vivYTluN3FBBzC6JfF0-ntwz7YEb5Mezknp_1iaw_wXxJJRSCj-6BzFvt3XSWFa-tOH_VN15T-tESfoO86K06-v_Aq6MwmEvW2hsMBd1lqnjLdyj_KiYt8QST6HfV05wb6kDnUL5iHjdaZjSta28Nis3yaPjrVDIxYTM33jvUgpzunk2cPJy8xwlgn5YEtH5Ez6mSb2xQ8u2SIN-_zl1D1lphdHVz4I4eLShJgDnTn24tR02BZyfdTtKtuzfFCvlqU5w0b6rz2AAzIhtvMZqfAvBTJojZ9oLBDqwTh4dHMr0Y6nFwhS_2OKhHZueJiLmptt4q_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این روش بسته‌بندی ۲ برابر بیشتر لباس را به‌طور کامل جا می‌دهد
🧳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/684687" target="_blank">📅 12:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684686">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bab0d9657e.mp4?token=IXkHaZk_FbVvGh3YeshSKvBMbDV3pAoBJVrXgWYJ2wjTR-czCJ9yYnorgZ4HvhdI5n7whgUyvLNe8ifHno7ByqY2fV-XK3zdwkJFU_lGsRudcw1U2Yp6YEjlAtExJaBKPxCBUN8Nex0kde2yrmLh5j98cZPwyaTcZ5Br4e9wFj_oYZ9KTzQSPvQ-5LBhmzzcWvMSioSIguCkMhpq0QNmqXi4_clQcOpl_qX3gS5JmJCfmJ-k1R8K_vRgJezCZQ1TGAysInaO5e7onO39v6oKbn6UpTZuDsee1Uu2N3HetUnsJA_o0BYUmlKC599hx4aORhfGl2oL5v8NXeKwGat-Zl38Q6FI_1ezOFsHmg2-at4X2S0K1L6DMAMlfqo6y0PX0BC4dW-Uuu5TwBLfSLsLz6YyyvsPhyq_fytO_VnqGM08fEgcOJKqnYce7NhSTvl5aXXEl_ey3VkGFT2TDIv5BYYHfeCa9VPNT-_ry8X6hm5c-PK8HvL_rr1O90t7VHwWkbvj-oMX_4Y3Vf_mENzSGdgjZ8Op0xWhq5FW5ZKUnHpa8rWSWS9MRBsnHJhhCYXNGlIHrFDIFNJlMMbmJeGvn82CwD4DOp2asERowmsFtwVvwJl-kOTN8mS6uzofdxQgxctqPADfLoxfMEB45D4InIGll4R6p4LhsHIRcdYE2Vo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bab0d9657e.mp4?token=IXkHaZk_FbVvGh3YeshSKvBMbDV3pAoBJVrXgWYJ2wjTR-czCJ9yYnorgZ4HvhdI5n7whgUyvLNe8ifHno7ByqY2fV-XK3zdwkJFU_lGsRudcw1U2Yp6YEjlAtExJaBKPxCBUN8Nex0kde2yrmLh5j98cZPwyaTcZ5Br4e9wFj_oYZ9KTzQSPvQ-5LBhmzzcWvMSioSIguCkMhpq0QNmqXi4_clQcOpl_qX3gS5JmJCfmJ-k1R8K_vRgJezCZQ1TGAysInaO5e7onO39v6oKbn6UpTZuDsee1Uu2N3HetUnsJA_o0BYUmlKC599hx4aORhfGl2oL5v8NXeKwGat-Zl38Q6FI_1ezOFsHmg2-at4X2S0K1L6DMAMlfqo6y0PX0BC4dW-Uuu5TwBLfSLsLz6YyyvsPhyq_fytO_VnqGM08fEgcOJKqnYce7NhSTvl5aXXEl_ey3VkGFT2TDIv5BYYHfeCa9VPNT-_ry8X6hm5c-PK8HvL_rr1O90t7VHwWkbvj-oMX_4Y3Vf_mENzSGdgjZ8Op0xWhq5FW5ZKUnHpa8rWSWS9MRBsnHJhhCYXNGlIHrFDIFNJlMMbmJeGvn82CwD4DOp2asERowmsFtwVvwJl-kOTN8mS6uzofdxQgxctqPADfLoxfMEB45D4InIGll4R6p4LhsHIRcdYE2Vo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تلاش کودکان فلسطینی برای بقا
🔹
دو کودک فلسطینی پس از اینکه آب را در میان صف طولانی و ساعت‌ها انتظار طاقت‌فرسا به دست می‌آورند، سعی می‌کنند راهی برای جا به جایی آن پیدا کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/684686" target="_blank">📅 12:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684684">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20c706cd49.mp4?token=gdEEN5xGxG-6CsOJ0Ndx3OxQAwM7iDiJG7-c5V146ZBM1bd61Syf8kDeTIQ0XBXPof5ws7JYEslJaGaN-Xn15RHZT-q1O8REhhrIM7ip-IgHQskIxDm0M973ChVIEPLolwmK5YKTbpl4-TE907qzuZinwwSeW4T11ayiBwhXtntO1p_Wx1NGcd4PQ7GH6arfC4_8HbeNL8LAwYJ8auGmNX_Y8ZON5b3H2SCcCmQuZHrVriqkaYX_JoIlpzGjzYdVEATb1ATfgz_cP-aBe3mpn5fl2AMPM6khDCdCk9j6tYzdgqQJM5rYSQvRh_KRAQ_mFR4cgQHFthV2N5lqzpn9ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20c706cd49.mp4?token=gdEEN5xGxG-6CsOJ0Ndx3OxQAwM7iDiJG7-c5V146ZBM1bd61Syf8kDeTIQ0XBXPof5ws7JYEslJaGaN-Xn15RHZT-q1O8REhhrIM7ip-IgHQskIxDm0M973ChVIEPLolwmK5YKTbpl4-TE907qzuZinwwSeW4T11ayiBwhXtntO1p_Wx1NGcd4PQ7GH6arfC4_8HbeNL8LAwYJ8auGmNX_Y8ZON5b3H2SCcCmQuZHrVriqkaYX_JoIlpzGjzYdVEATb1ATfgz_cP-aBe3mpn5fl2AMPM6khDCdCk9j6tYzdgqQJM5rYSQvRh_KRAQ_mFR4cgQHFthV2N5lqzpn9ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با رعایت این سه مرحله روانشناختی دیگه به راحتی از دست حرف هرکسی آشفته نمی‌شید
#سلامت_روان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/684684" target="_blank">📅 12:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684683">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pu8dmuWqz54kJ3w0m-jWCOwny_fpx_FLqLWW9GwHKMopN3XACKUY5iKqasyvXUhOt-4onEooVf7apIzdSg0YUjnfO1pefQrZF6Q4Vb9QPQewdR_KOT8gBj4_Q7O5HBf420FzCj8AsuKdWHUT61tsYZtIVpkx_pwPUCczixxhzh7gpJq5p2JmX90MyeOFGkqBrvtlvCMC40GsXvUuGMPTZUOZolLQcDQFPAX8iPZOeWOZy1qSN9FTFYvqlF4iMBEMXWFwei3dFj_FpKsvswU4NU5CY-NNOCeajPP1xI_kBh5QBboC56FXw8-LO2xIp5iXyIy4F_nQkB3mU-M7-m7IWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دکتر قاسمی، سرپرست بانک توسعه صادرات ایران در هفته دولت خبر داد
🔹
تمامی تسهیلات تکلیفی، از جمله تسهیلات ازدواج، جوانی جمعیت به صورت ۱۰۰ درصدی محقق شده است
🔹
بانک توسعه صادرات ایران خود را برای ایفای نقش مؤثر در دوران بازسازی پس از جنگ تحمیلی سوم آماده کرده است.
🔹
بانک توسعه صادرات ایران در ۴ ماهه نخست سال جاری نسبت به تأمین مالی شرکت‌های تولیدی از طریق گشایش اعتبار اسنادی و همچنین صدور انواع ضمانت نامه­‌های ریالی بالغ بر ۱۰ همت اقدام نموده است./
مشروح خبر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/684683" target="_blank">📅 12:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684681">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMVDRhBk_LiNSdWJLnnB8oWfj-1qe44nzPYBcJzQ7SswrNSOOKLvBz-lms_L2FM-YCqB0rz0AG4D6CRBCge1aZh3uSQroZtI3_NaQa5BIN2KeoBl6ZH3FcYc-E0fEwbJAfkO9mxG_bKUA1mLAgkpXjqSsG37-X05LpefgOHdnCdNI9pjwGgtWoPa2rrJHc_we-v8G7n6vzKl2RJfHHYJcrcI0OOoacc37l1LrrSMPOvaB5mY2F0BFTnE0rXwMF68mKNlYWu7__Vdu_yx42t0szYQ8Bbuu1zNY9GNjRnDg-_EDCaNK2JAhWJEhsEc1UlwIaGIAO0Ler90P5Z_roanmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
با این روش، درست از هوش مصنوعی استفاده کنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/684681" target="_blank">📅 11:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684680">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
باران‌های سیل‌آسا در راه شمال/ گرمای ۵۰ درجه در راه خوزستان
هواشناسی:
🔹
شمال کشور امروز با رگبارهای شدید، بارندگی و لغزندگی جاده‌ها روبه‌روست و از فردا کاهش دما در سواحل خزر آغاز می‌شود.
🔹
خوزستان از شنبه با گرمای ۴۹ تا ۵۰ درجه مواجه خواهد شد.
🔹
همچنین گردوخاک و توفان شن در شرق کشور پیش‌بینی شده و دریای خزر تا یکشنبه برای شنا مناسب نیست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/684680" target="_blank">📅 11:38 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684678">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
چین خواستار رفع موانع در روابط دو جانبه با آمریکا شد.
🔹
اسلام‌آباد: تابع تحریم‌های یکجانبه علیه ایران نیستیم.
🔹
صادرات سیب‌زمینی تا پایان سال ممنوع ماند.
🔹
کندوان یک‌طرفه شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/684678" target="_blank">📅 11:21 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684677">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
ادعای وال‌استریت‌ژورنال: پهپاد شاهد ایرانی با کمک چین جنگ را متحول کرد
وال‌استریت‌ژورنال:
🔹
افزایش سریع پهپادهای تهاجمی یک طرفه ارزان قیمت توسط یک زنجیره تامین جهانی پیچیده که همچنان به چین منتهی می‌شود، امکان‌پذیر شد.
🔹
پهپاد شاهد ایرانی با کمک چین جنگ را متحول کرد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/684677" target="_blank">📅 11:14 · 05 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
