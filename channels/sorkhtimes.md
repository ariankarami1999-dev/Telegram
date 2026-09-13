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
<img src="https://cdn4.telesco.pe/file/V24zRRy_nu3pBRd49U4QZH8Oz-Vp9wCah1PzJn1pJUW2xG7BlbFSicpN9LKGXaT7UpNSIIPJL-UChM1gNaAzfMDcjziCQxoMPa5QBNhkL6LBZ9Uc0fb227m3BW2ZEi4Tt_T6cOl3TEEaRGnfOuMGrbxkOojZfT6bLMOurlDX18pAMBDyoiJ5rpEQ_36IK16fquxBj47qIpkq2Ajue39rVDqZTpj0FUhYqlnwbwv__RLTbzP0FTgp0NiC87CQhUznbIyzU-KMI7B0bA7YC2E31yJPyd3blRCJVWLhTKfVvrT2vQNRja-IT1cK6UZQZG8XVxxHDYjiT2tmCWq2stuQzA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 05:45:24</div>
<hr>

<div class="tg-post" id="msg-139972">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/SorkhTimes/139972" target="_blank">📅 01:22 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139971">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13b9033e7e.mp4?token=taIA5HTGHLbRc0YjCCkDT5J0adLiQVuLcTnvGH_7CtBRTBP6PRYnZqgX5ILVujP4ga1TNpJsIJJruaXX0pa-_3pfEXXjyyXBiNGLWEmruYBpdmdVrUM5YbkeZlNnjxsRjaLR8tZpnYa7d55FB5ITH5Lm9Zak9XQjPZHXfhKq4MQfeiikQf7o6K2bLBdw49rwLGU6AUaETvYUYO0A2rr998efEvk0h3HJzTyesXV1MJT5ISziZFOkTXeRcm-f5K3wLn2gd57YkPR0nNvIzlbqdWjtEXYyOIQoipr-CDD0EBm7iKHg-t28lRngOeRfe1Lgbad7DuCqgtNtSZOZSbIJvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13b9033e7e.mp4?token=taIA5HTGHLbRc0YjCCkDT5J0adLiQVuLcTnvGH_7CtBRTBP6PRYnZqgX5ILVujP4ga1TNpJsIJJruaXX0pa-_3pfEXXjyyXBiNGLWEmruYBpdmdVrUM5YbkeZlNnjxsRjaLR8tZpnYa7d55FB5ITH5Lm9Zak9XQjPZHXfhKq4MQfeiikQf7o6K2bLBdw49rwLGU6AUaETvYUYO0A2rr998efEvk0h3HJzTyesXV1MJT5ISziZFOkTXeRcm-f5K3wLn2gd57YkPR0nNvIzlbqdWjtEXYyOIQoipr-CDD0EBm7iKHg-t28lRngOeRfe1Lgbad7DuCqgtNtSZOZSbIJvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔴
آرش فرزین: پرسپولیس خسته را پدرم به عشق پروین خواند  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/SorkhTimes/139971" target="_blank">📅 00:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139970">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✔️
✔️
‌ ۵-۶ بازیکن از پرسپولیس در فیفادی جاری به تیم ملی دعوت میشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/SorkhTimes/139970" target="_blank">📅 00:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139969">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✔️
✔️
تعطیلی ۲۵ روزۀ لیگ برتر
🗣
🗣
لیگ برتر حدود ۲۵ روز تعطیل خواهد بود. بخشی از این تعطیلی نسبتاً طولانی به دلیل همکاری باشگاه‌ها با تیم ملی امید است و بخش دیگر نیز مربوط به روزهای فیفاست که از ۳۰ شهریور تا ۱۴ مهر است.  «سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SorkhTimes/139969" target="_blank">📅 00:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139968">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
🔴
پرسپولیس موفق شد امتیاز تیم دسته اولی فولاد نوین رو بخره و تبدیل به پرسپولیس ب خواهد کرد و سید جلال حسینی هدایت این تیمدرا برعهده خواهد گرفت/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/SorkhTimes/139968" target="_blank">📅 00:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139967">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/139967" target="_blank">📅 23:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139966">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✔️
ساپینتو : من و کلارنسس سیدورف مخالف ۱۰۰ درصدی جذب جنپو بودیم ، ولی تاجرنیا اصرار به جذبش داشت بعدا متوجه شدیم بازیکن و ایجنتش ارتباط نزدیکی با تاجرنیا دارن...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SorkhTimes/139966" target="_blank">📅 23:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139965">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❤️
پیمان حدادی: وقتی لیگ تموم شد و به همه جا اعلام کردن نیمه تمام هست، هیچ جای دنیا پس به تیمی جام نمیدن و خیلی غیر منطقی هست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/139965" target="_blank">📅 23:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139964">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✔️
✔️
ریکاردو ساپینتو؛سرمربی سابق استقلال:
🔻
من با مدیران زیادی کار کرده‌ام اما تابه‌حال مدیری به شهرت‌طلبی و دروغ‌گویی علی تاجرنیا ندیده‌ام.
✔️
✔️
از روز اول تاجرنیا به رابطه من و مدیرعامل وقت آقای نظری جویباری حسادت می‌کرد و انتظار داشت من مسائل تیم را با او…</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SorkhTimes/139964" target="_blank">📅 23:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139963">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SorkhTimes/139963" target="_blank">📅 23:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139962">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✔️
✔️
ساپینتو: پیشنهاد عجیب تاجرنیا برای استقلال!
✔️
✔️
ساپینتو مدعی شد تاجرنیا به او گفته قرار است سعید فتاحی به استقلال اضافه شود تا با توجه به ارتباطاتش با داوران، مدیران سازمان لیگ و فدراسیون، مشکلات داوری و برنامه‌ریزی مسابقات را به نفع استقلال حل کند و…</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/139962" target="_blank">📅 23:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139961">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❤️
پیمان حدادی: خیلی ها آرزوی قهرمانی دارن اما پرسپولیس در ۸-۹ سال اخیر ۶-۷ جام گرفته. بازی ما رو لغو کردن تا صدرنشینی ما یک ماه عقب بیفته.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SorkhTimes/139961" target="_blank">📅 23:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139960">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❤️
حدادی: هاشمیان قبل و بعد از پرسپولیس کجا مربیگری کرده است؟ دوستان در یک سال، سه بار او را دعوت کرده‌اند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SorkhTimes/139960" target="_blank">📅 23:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139959">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✔️
✔️
دکتر حقیقت: محمد عمری تا ۳ هفته‌ی دیگر به تمرینات برمی‌گردد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SorkhTimes/139959" target="_blank">📅 23:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139958">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SorkhTimes/139958" target="_blank">📅 22:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139956">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✔️
ژاپن 3-0 کره جنوبی
❌
ایران و ژاپن فردا ساعت 14 برای کسب عنوان قهرمانی و سهمیه المپیک به مصاف هم میرن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/139956" target="_blank">📅 21:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139955">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqaHyo8o79NeAm0cS3SQi_nPNyvone_ebFjV0UHtoOgy_A6lUpbd3uObydWgy7PjWjY51paSKBGQjdST6UV2jy9IZ9PbL3nwofs3AQqLyye6NGvKjG5_3qm0odfhW2I_FcdNToH6isuhHQutReLfDSxBf0idbjDRAG1YUbf3yf3SRO8hdMOyI20w6meuLOQZO4lRjnGL_AJ5OEGr2I7fS5dX1WJD9vcwdf1OnptA2-DQAKZ-T_7WYhwfvB-IKjvckykxffbj0vCXtGght6Q966lrnwLA5LnXxhsIJOhUQP1Pjn8yYivnnq6BXez9qDW0tUBZkBA6B2R0eW2kBCdk7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تصاویری از تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/139955" target="_blank">📅 21:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139954">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6060af132f.mp4?token=DS6x3rw-Z0icq25Et3pS2ENYVOF7fVWeVKG36TAsMWpAf1galU-RG7VSyP8YClsDuPTxmXcBRTGxBkF6ed5sAZyInF7ARipWCD9Ab07cpS4Q237-WTc3EeBP9bLXVeTvLD3XgrtQxla8UZ5xTiJezljm5KfJYVbBW7jfncTvNltPz2M9ydJxIpasCMfY2LSjkfT9cX5YkQyAg0omSaRJ3KCgG9rqlfwBNXSZtFkVs9A__7O2UFZvuTj967u_BTtsTR1vRyXr9adN7EnamXetECOqbh05UXwVr_EQgD88ehlPcXOatLK-G1ltWxSZzkGiO0-DnC0YcXFUCnorSSxfeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6060af132f.mp4?token=DS6x3rw-Z0icq25Et3pS2ENYVOF7fVWeVKG36TAsMWpAf1galU-RG7VSyP8YClsDuPTxmXcBRTGxBkF6ed5sAZyInF7ARipWCD9Ab07cpS4Q237-WTc3EeBP9bLXVeTvLD3XgrtQxla8UZ5xTiJezljm5KfJYVbBW7jfncTvNltPz2M9ydJxIpasCMfY2LSjkfT9cX5YkQyAg0omSaRJ3KCgG9rqlfwBNXSZtFkVs9A__7O2UFZvuTj967u_BTtsTR1vRyXr9adN7EnamXetECOqbh05UXwVr_EQgD88ehlPcXOatLK-G1ltWxSZzkGiO0-DnC0YcXFUCnorSSxfeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
صحبت های وحید هاشمیان علیه پیمان حدادی:  حداقل درویش از مدیریت الان مرام بیشتری داشت و به نظرم برکنار شد چون من را برکنار نکرد. چطور برای اوسمار این چنین مراسم بدرقه ای انجام دادید ولی با من این گونه برخورد شد؟  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/139954" target="_blank">📅 21:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139953">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✔️
✔️
السد در 4 بازی اخیرش 19 گل زده
🔥
پ.ن یعنی دوباره قراره عروس بشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/139953" target="_blank">📅 21:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139952">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ee53113a6.mp4?token=exOmkYuJvarQnaX9zIqYJu6KM3UgAO8RKt5x2bwOwO7_Lv8GKj7MrEM90_yc7zPm1fIp2bedPQkJp73RbPe7FOBpTKzJF3ZRbUIry3VupDDQI9F6ZSMsfi_nc3hUI5_kn7XD8YuN_7ZGanTs2mS4WFpPD48_1bFSwHG_A29KTkuYx5hG467m-0QSYS16tNJ8V03gtzOkljCKGLO1fw4STL8LuteEgqddcFAbF9cqPCQqQ8Iof7maMa3SjhViUtxPe23-pyl6aV1508vfj4HDI9t_wV1eDMt3D15mApg8Z5p25HnAbqSazPwcL_S-zGF2lPMZ5NkVL-1yJdd1iroL4aj9TtM2mI3JQVp9iBvjiVp8Cu6yzIASO_UJGuP9ayKXeeDltJ5TxgbSWUZuWGLa--YZ7VUCxdcXaednEzRRuMlINp5OeO4pJsPMimD0rXbocsRmIlRA65iAgQv9Ixlw10doRmAGzcSekZTz3xblYxiPzwr4PROJy_tmuJDi3Qsf9XdCgSoE-mEjWlWzjKXyav7duko5VSJ_U5cfgzSQtShZACPeh1but8XkYXsTwdktCcjz8FwnPeZIrDHnzokPKyf7tSBzjCiMttV96TwNaq1hXyTYafWl_halhEAS8rEicVd8KaK-XsWIAVH11hP5fpizWxysq4OASrcVM0flrBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ee53113a6.mp4?token=exOmkYuJvarQnaX9zIqYJu6KM3UgAO8RKt5x2bwOwO7_Lv8GKj7MrEM90_yc7zPm1fIp2bedPQkJp73RbPe7FOBpTKzJF3ZRbUIry3VupDDQI9F6ZSMsfi_nc3hUI5_kn7XD8YuN_7ZGanTs2mS4WFpPD48_1bFSwHG_A29KTkuYx5hG467m-0QSYS16tNJ8V03gtzOkljCKGLO1fw4STL8LuteEgqddcFAbF9cqPCQqQ8Iof7maMa3SjhViUtxPe23-pyl6aV1508vfj4HDI9t_wV1eDMt3D15mApg8Z5p25HnAbqSazPwcL_S-zGF2lPMZ5NkVL-1yJdd1iroL4aj9TtM2mI3JQVp9iBvjiVp8Cu6yzIASO_UJGuP9ayKXeeDltJ5TxgbSWUZuWGLa--YZ7VUCxdcXaednEzRRuMlINp5OeO4pJsPMimD0rXbocsRmIlRA65iAgQv9Ixlw10doRmAGzcSekZTz3xblYxiPzwr4PROJy_tmuJDi3Qsf9XdCgSoE-mEjWlWzjKXyav7duko5VSJ_U5cfgzSQtShZACPeh1but8XkYXsTwdktCcjz8FwnPeZIrDHnzokPKyf7tSBzjCiMttV96TwNaq1hXyTYafWl_halhEAS8rEicVd8KaK-XsWIAVH11hP5fpizWxysq4OASrcVM0flrBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حدادی: بازی خیبر را عمدا به تعویق انداختند تا روند پرسپولیس را متوقف کنند!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/139952" target="_blank">📅 21:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139951">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❤️
❤️
حدادی در بین هواداران، بعد از بازی با ذوب آهن.
✔️
هوادار:
❌
دمت گرم با این تیمی که بستی، تا آخرش همینجوری وایسا.نیم فصل دو تا ضعف رو برطرف کن، بخدا تا آخر فصل ازت حمایت میکنیم.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/139951" target="_blank">📅 21:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139950">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/139950" target="_blank">📅 20:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139949">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
پرسپولیس فردا به حای بازی لغو شده با خیبر احتمالا تو یه دیدار دوستانه به مصاف تیم شهید قندی یزد میره و بعد از اون تمرینات مدتی کنسل و بازیکنان به استراحت میرن  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/139949" target="_blank">📅 20:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139948">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYqukD--X8yNJUkzMCcXGB3-xJdD28_JAh4uG2BPqVnoEwEJL_a5LaaamDD2G4Sn1rNwYneS3-pZ6tiY-8J8vIbaRckA1oZD07ju8jS45OdU6EKFe47QZj9DdE7ICWXOkobCnF9cW2siJd-ddO5EOuhH6x-qCddkCMhC9TeHUFXBVK6avpyP5BlpsCVLOxq1-v8c1-Cq6lKYdcyE_zH-Yca4VOToznat0fJ8ZAt5Z3aeOSIbvoGsop4-tIqlxPyT3_Tp6u6KCjLKzf_0IoVp1qaVmiSa1Dhds1qxmyAuvSl_1_mnAZ8G80cAq4aijpJdI3asKTuDvVP3YSGSwyRgIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پرسپولیس فردا به حای بازی لغو شده با خیبر احتمالا تو یه دیدار دوستانه به مصاف تیم شهید قندی یزد میره و بعد از اون تمرینات مدتی کنسل و بازیکنان به استراحت میرن
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/139948" target="_blank">📅 20:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139947">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fABzdIMJbvcdqX9dJO2YbkzDRaRgvJXQ9degmTtgHH9CojmnuxFGAgSiujxdc9Cwe66IStcBhrDCQ9_Bz5LIYihxVoPPzdrEaGXY8lrgzkTK9eQQxSAp3mHK4-CrvLUf_2GjgqU1MSOBrYWb-8uUFq1POK8nz5Yjc2TCXaT8SZCZqx3Wq0YO-1btg_9qXt054EDMmRaGOQX5S0344OUDn9uZ_e97cUMTSVd7Bncxd6asX2tyhbczdlpg9XqFBol2QDVWV3rvGYZb7WFusVQkI8IblNy5mmk45vwN-NWN0b3ymbLHfaIdojzTRehE2fUrTwgO9l8ZgHAdunRad03VVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/139947" target="_blank">📅 20:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139946">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✔️
✔️
فوری؛ در آستانه بازی استقلال و السد در بصره عراق، به دستور نخست‌وزیر عراق، تمام مرزهای عراق با ایران بسته شد و پروازها نیز به حالت تعلیق درآمد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/139946" target="_blank">📅 18:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139945">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a080739df.mp4?token=jEGZNBVhpQXP3SRiNDv8MnYXR_keloPt4ZlN6gmFF0VzJsk4Xb8wUMlGmEu3B6t4xGDfcggvCakHZ5p21-FJLENHFeCMT3pJzzuOhdHfiwRnq5UMok-ZfigOtihR9-9Tlxwa6MOTfmJCyVIsHmt2hjof8NfgatheONAYTcduDMhFyQHLfQbP29D2RPuznocKE6g6jK8An6vMN3qNAiot7Uss-jjT9di33EP4-MH5TAdULUPstczHxsusUOlSRenD5pnS52WvvEaLlV55rKtZS89EIO7tq3N3nAocnBaX_pO45hSI4tO3j3bjfT1xiCHP4cgDGu5n-eIZt1RoPigZZX1C2d9oQfeN9MnxR63jKpm-10uN-4aZu52aZLIzA0fyl_6Z71ge7bSujNoyjUAcFbUDHaLQy7kfD_Qx0jMhzjzfcJtMH60MMpSWqkQO2GZYqQIr9LizVgB_XtsuFi5YQUNiiKnrigmyOT_V9v4BgXKdTmFEdT79bD2tw2rfifHAFbTtLVHuUOIGUQaUr7c7_ViAo3z-3Xa_RwxUlhnAJeDu_yGPHIACvAeCABpM3XfjhhWpVU6z18Thq4sDtBehR8IeAj4SonsLD4RUfw8a12wzYtUJf4lAKF9Fjp8CkOL7eSvQuF2I1O3sY4vgGbxKq4IBAoRRb8S1wSbjnDwKP6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a080739df.mp4?token=jEGZNBVhpQXP3SRiNDv8MnYXR_keloPt4ZlN6gmFF0VzJsk4Xb8wUMlGmEu3B6t4xGDfcggvCakHZ5p21-FJLENHFeCMT3pJzzuOhdHfiwRnq5UMok-ZfigOtihR9-9Tlxwa6MOTfmJCyVIsHmt2hjof8NfgatheONAYTcduDMhFyQHLfQbP29D2RPuznocKE6g6jK8An6vMN3qNAiot7Uss-jjT9di33EP4-MH5TAdULUPstczHxsusUOlSRenD5pnS52WvvEaLlV55rKtZS89EIO7tq3N3nAocnBaX_pO45hSI4tO3j3bjfT1xiCHP4cgDGu5n-eIZt1RoPigZZX1C2d9oQfeN9MnxR63jKpm-10uN-4aZu52aZLIzA0fyl_6Z71ge7bSujNoyjUAcFbUDHaLQy7kfD_Qx0jMhzjzfcJtMH60MMpSWqkQO2GZYqQIr9LizVgB_XtsuFi5YQUNiiKnrigmyOT_V9v4BgXKdTmFEdT79bD2tw2rfifHAFbTtLVHuUOIGUQaUr7c7_ViAo3z-3Xa_RwxUlhnAJeDu_yGPHIACvAeCABpM3XfjhhWpVU6z18Thq4sDtBehR8IeAj4SonsLD4RUfw8a12wzYtUJf4lAKF9Fjp8CkOL7eSvQuF2I1O3sY4vgGbxKq4IBAoRRb8S1wSbjnDwKP6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔴
آرش فرزین: پرسپولیس خسته را پدرم به عشق پروین خواند
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/139945" target="_blank">📅 18:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139944">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
✔️
با توجه به لغو بازی با خیبر، پرسپولیس فردا در دیداری دوستانه به مصاف تیم شهید قندی یزد خواهد رفت.   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/139944" target="_blank">📅 17:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139943">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✔️
✔️
✅
تصمیم تارتار درباره تمرینات پرسپولیس
⏺
با وجود لغو مسابقه پرسپولیس و خیبر، تمرینات پرسپولیس طبق برنامه امروز برگزار خواهد شد و سرخپوشان پایتخت یک جلسه تمرینی دیگر را پشت سر می‌گذارند.
⏺
مهدی تارتار، سرمربی پرسپولیس، قصد دارد از فرصت به‌وجود آمده برای…</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/139943" target="_blank">📅 17:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139942">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🆔
| ورزش‌سه:
🔴
🔄
پرسپولیس امروز هم تمرین می‌کند و روز یکشنبه نیز در دیداری تدارکاتی حاضر خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/139942" target="_blank">📅 17:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139941">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✔️
✔️
✔️
علیرضا بیرانوند دروازبان تیم تراکتور، دو دیدار آغازین مقابل شباب الاهلی امارات و الغرافه قطر را به دلیل محرومیت غایب خواهد بود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/139941" target="_blank">📅 17:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139940">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARPHUc4uGDsZ6TGocWB7jkYiwkIvSKbbHngW1g458Xmo8OjigLWFkiLyknMAu7_E14Jbf3TBCv9GudWOuC32GXi9kY2X6p9s3P-52kHtNud-nRHwgCATOp46O9DGpIQJpqfqeHHXw27DJuRQxGey7MziB8sYhLW05d2QMUl3DrdgcVi64Vq6yCpJOrD0Qz2fjIV9rUNQSY-sAVpuIxYUiMtykM4FoRtwkXzWgq63zUACkH0X5H0YQSMvxxOYfXz_T1eSL6QAX_KWdg8ImWjDytVDYV4B42kSz8gNddeS664WT4LsJ7bsn8w4EyG132erE7PWGM7tpwGss42g-M07Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
میلان در آزمون لاتزیو؛ جدالی نزدیک و تماشایی
⚽️
میلان با تکیه بر کیفیت هجومی و امتیاز میزبانی، دست بالاتری روی کاغذ دارد. لاتزیو اما با ساختار دفاعی و ضدحملاتش می‌تواند بازی را برای روسونری سخت کند. انتظار دیداری نزدیک می‌رود؛ جایی که جزئیات می‌تواند سرنوشت بازی را تعیین کند.
[
آث‌میلان
🔴
🆚
⚪️
لاتزیو
]
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه دریافت کنید.
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
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/139940" target="_blank">📅 16:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139939">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✔️
✔️
فوری؛ در آستانه بازی استقلال و السد در بصره عراق، به دستور نخست‌وزیر عراق، تمام مرزهای عراق با ایران بسته شد و پروازها نیز به حالت تعلیق درآمد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/139939" target="_blank">📅 16:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139938">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">💢
ویدئو باشگاه پرسپولیس برای گئورگی گولسیانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/139938" target="_blank">📅 16:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139937">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ls3FzT4Mffp_nxafyTud28gICNGCM-APN2S-_to_2vn4fVxXHNxhPnx3Ktkl9A_7sLZJbqxWPOKBBm4Vx9FDrJyUH0MIlUCDAASafkGH64M90qKhNGfGpxLr5oDkStgDNBw_p_CjpmXZL6TFfP05I8aesjIIpAbwgSk1oSNop0cyy5pxBqdd7U4ejwgj5zoSfwcCGRa3LyZroOIaDWaV6RS3hCIDGhv1Bhf8l94C_VBcM0SMl_WKnMWiTCK1wOvnjLw_G5HAFMROV3vmv07WoUKfbQubZyzGse3fVsfmAj--6M3E0h9QqSUQMQRjrEdYJYfwW8Dpy_CviMLIfWkyHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
⚽️
رکورد جالب پوریا شهرآبادی؛ شروعی درخشان در پرسپولیس!
🔴
پوریا شهرآبادی در حالی که تنها ۲۰ سال سن داره، تبدیل شده به دومین گلزن جوان تاریخ باشگاه که در کمترین زمان ممکن به ۲ گل می‌رسد.یعنی شهرآبادی برای زدن ۲ گل، حتی به اندازه‌ی دو بازی کامل هم در زمین نبوده است.
📊
۶ بازی | ۱۳۰ دقیقه
⚽️
۲ گل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/139937" target="_blank">📅 14:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139936">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✔️
✔️
باشگاه آلومینیوم اراک هم از بازی کردن آسانی شکایت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/139936" target="_blank">📅 14:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139935">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">💢
ویدئو باشگاه پرسپولیس برای گئورگی گولسیانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/139935" target="_blank">📅 13:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139934">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✔️
✔️
عادل فردوسی‌پور: ترابی قطعاً ادامه فصل رو از دست میده، با خودش صحبت کردم و گفت دو پزشک بهش گفتن رباطش پاره شده و باید عمل کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/139934" target="_blank">📅 13:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139933">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJaxKAVvfCGEW4_RB03l9pPrpiiLwCpabP83xDPa_A609yuuTI7Fi8mq8StqWFc5gkcrLIuYC9JBU7OnILwsU-aAtj8j8A_gNkh2CUwqWxbSuBCfAODjdP6d66FQG6FUf49UFfwI4Yq3DLPVgKOXz9yCQRrX6M0HErnWpjtLHVv9kIFqD75mwIAZYjYhrniB6Azus7J6tpRMO_FvL-U8ZdnYvYuEqtKkfQ9L-T-nlU-Xqo-9U_tk0r6UUGyF4iqjzEu77jqWtektsLDyaJPitmdzD3ceRLSZ91g-F04Wa_l6dYN4N8C9oyueXsCvEpNb0XeM1A_BeXD_ObLIADUrEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🆔
| ورزش‌سه:
🔴
🔄
پرسپولیس امروز هم تمرین می‌کند و روز یکشنبه نیز در دیداری تدارکاتی حاضر خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/139933" target="_blank">📅 11:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139932">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6OHF94IeJLcbNksq5aD50dK_0B0FXPIEBH9hyUjkl65_U-cR891cGnAHsytjH7KCk7MQANGf63ZVq9650vq12Qn7hgVNugvmEO5WqIJd0BHxfIUxpGxNRl932wO_Qliley3fZIc7Ao3ZJaSH5eZyCh0XTxKnsKGMAJI2-UUzTUhkPsclR9g4s6CWEfqTIboL089yHbm4xV1EISiRAIvmud9JKoNOrnHaIHYmKJ5HUqE4-KSnZd7Kki3wnPfLXmNFLkuLsBjeOW___rQUoG5rMC_Uy_wW41RMW9s9n-e6qlVJaNzwr0s9x35rBu_DjK8lRbxfbZtdlrkOhUB7aQhYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اسپانسر دو باشگاه لیگ برتری نساجی (وارش) و تراکتور (آتا) توسط وزارت خزانه داری آمریکا تحریم شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/139932" target="_blank">📅 11:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139931">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🏅
❤️
فووری از رسانه داریو ازبکستان: باشگاه تراکتور به دنبال جذب اوستون ارونوف وینگر ازبک تیم پرسپولیس در نقل انتقالات نیم فصل است
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/139931" target="_blank">📅 11:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139930">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
❌
حمایت از خداداد عزیزی به رغم فحاشی های زشت و حمله بی اساس به فدراسیون فوتبال درباره var
✔️
✔️
سخنگوی فدراسیون فوتبال: قطعا و حتما امید عالیشاه هم زمانی که خداداد به استرالیا گل زد از آن گل خوشحال شده. هم عالیشاه و هم خداداد عزیزی برای این فوتبال عزیز هستند!…</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/139930" target="_blank">📅 11:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139929">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
پروازهای ایران–بصره تعلیق شد؛ سفر استقلال در هاله‌ای از ابهام
❌
❌
درحالی‌که مدیر سازمان فوتبال استقلال دیشب گفته بود که اعضای این تیم امروز ساعت ۱۴ تهران را به‌مقصد بصره ترک می‌کنند، فرودگاه بین‌المللی این شهر تمام پروازهای با مبدأ و به‌مقصد ایران را تا اطلاع…</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/139929" target="_blank">📅 10:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139928">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✔️
پزشک‌باشگاه استقلال: یاسر آسانی هیچ مشکلی برای همراهی استقلال در بازی برابر السد قطر نداره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/139928" target="_blank">📅 09:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139927">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pny4ERFvk2VTeCZB5OJQUlfI7VQhjgJt-vHQgwIxu8id9d97oxuit6URmkiB25pAgXyDQGnXJUD7ZokDDJaK2tQZMp1L-3xLURsA-8zCBzI3JHVViyxR8HbPsNGMRje_qUfMnI0XyDtn6Zx5RoPBIbfnpnVKy6AorbQJg8x5tPnGbA4jnJGLrW2y3JCM13cvAmKimeBpQxwbmhLTb6e-BJ4DcBo0wuTXqq7W9qF9OiF6i1VH4DYM20B3Gq1cEVqDuXp6_ENuYlwd8RBZR8JkOU9N7dPSDEJWAlscETVpNORA19wB3cMUfkd3pLl2OYCNmIY844XHaTayu847089x6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
❤️
ورزش سه: دلیل بانداژ دست امیرحسین محمودی تکل او مقابل ذوب‌آهن است که باعث آسیب جزئی این ستاره‌ی جوان شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/139927" target="_blank">📅 09:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139926">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyzkiBI3LRQ3k8GqRzyBb4Eqs5EBe0lRQ2cLNpGE7jZx1Zl-av4kbtqOWrcIyVml5VwG9rwW-pdL9UP-_jGRhboVcz1pySa24qVWB3hzKtvfwtyx33ttQ1JUMk8UoJ3ICPoqx0J1S7lANnXNK3yWFrKFE_U6y6YjTWDTT6C5fI6Py7cXP2cSP6DETh5VAeCGWX0TIrNbc9KfifQPQq0uBaIoMTGH7KRoKu9In5vClrDDouVs2ydlyURb53Q22izpIJnXyq9BkwxICJSrb8bIVs_BVmBR1h_V_8R0ZVIptFtS12q3689HaBzg52ocpFhDiZ0KzRL_eD-OarQBcPINgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/139926" target="_blank">📅 09:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139925">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTy_7MpNXFh1WSxjkdM5VELmfZ5CGeuvuvzQcAHCSECXcKraJPZ8q62eawivoWe3VS1hzOYb3iRKJVdNZ4uVEWRAbf1mBHe0u7h8Jw2fEhrJQHUROGAS0IRc0EC3qnruh78Wj7AdjM-sls5g_V2-mQqIjeNY6PMqx4ScGnaC-m6jlCimCpjtRWq1jMVehuCBybZMwDnSMn79WDrSLg4FEDii8E6T4SVYaOLfuMgMDRv_soSkMmrVU0rtt29y1f4BBQ0NCfAHZDLKGTztTKwtlDRoxNxbX9a0ow2WGOsTvrenay9O6UsHIkMALGPpC_BgCxNpyaYz8mLLfUs9NmVBlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
شلتون و تیافو؛ نبرد قدرت و جسارت برای صعود در نیویورک
[
فرانسیس تیافو
🆚
بن شلتون
]
⏰
بامداد شنبه ساعت ۰۲:۳۰
🎾
شلتون با سرویس‌های قدرتمند و بازی تهاجمی می‌تواند ریتم مسابقه را در دست بگیرد. تیافو اما در رالی‌ها و تغییر سرعت، توانایی بالایی برای به‌هم‌زدن برنامه حریف دارد. اگر شلتون روی سرویس اول و ضربات فورهندش مسلط باشد، شانس برتری‌اش بیشتر می‌شود. با این حال، تجربه و تنوع تیافو می‌تواند این نبرد را به یک بازی نزدیک و جذاب تبدیل کند.
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
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
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/139925" target="_blank">📅 01:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139924">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✔️
✔️
محسن خلیلی مدیر پرسپولیس: چرا می خواهند ترمز پرسپولیس را بکشند؟ چرا می خواهند حق پرسپولیس را بخورند واقعا این شائبه برانگیز هست  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/139924" target="_blank">📅 00:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139923">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✔️
✔️
تارتار قصد داره که به اورونوف تایم بیشتری بازی بده تا اعتماد به نفس رفته این بازیکن برگرده و این بازیکن رو دوباره احیا کنه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/139923" target="_blank">📅 00:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139922">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🎦
تحلیل مدعیان اصلی قهرمانی در لیگ از نگاه وحید هاشمیان؛ شانس اول قهرمانی به نظرم پرسپولیس است
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/139922" target="_blank">📅 23:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139921">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✅
✅
براساس گزارش منابع خبری، مسعود پزشکیان با درخواست زنوزی بدنبال حل مشکل سربازی علیرضا بیرانوند تا پایان جام ملت‌های آسیا است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/139921" target="_blank">📅 23:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139920">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63b0b11397.mp4?token=UX9TINYQLXWsDhrbERil4OwrqnWpbh8UOtGxvtQYHZ3UWJEk22s5Rugc2xSVkXTwQzHDu59skX1BC2VWM6OaViinvlwZRGquDJW-adCLvRZqN5QTWNJY-EFyYM1-s_clgOo_5AyyDLZoiuJpyVKaA-WBavg0Zt7y5YjOH2f6aSVKzljoGWi_S3KAos-J0WTn5Mwa_xrJnU94RRuIqPBX9c5LdoIE8MyMNCB_ufZEY619pAmquJss0KbMrb8EugmKhb70iGMGqxLy8-yCcN8Tu_v1NSsYrGud8Uhx3sdw-mqCrw3KcAUtWmmMJisnoqH9D9BINGK4kCLjdJjDdPPmtlt99nqPS3t32hAdcVT1zb9etqyFUKI6bkDnsQUTkuH13M0Nmy2-6XEpdcdg6Jqu5yR57lOXxqY5BbOP7Gq5bwKpmrvji2ohpIATv4ncrHstaFjW2usSNAtwZ1Ahq0ylS-d4TcPySZaY3et2lMi4GjPy7y-m7oMvRgfeJmzodZ2DV3dLptlWJ4mFJEQoRIXohxD1q9vrg3xIMWXEQHzzrpSRtpJ_ka0-A-y92NNw95xlteNOKUx4ki26vLBvFw0WC_QO5PgcMb9V_GolCnNzxwVktKBqreKIDupb1OqB9cO8HMn_tsMgE17nRstTbcQoVL8BrO8x9dy3GDBCAAubzqk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63b0b11397.mp4?token=UX9TINYQLXWsDhrbERil4OwrqnWpbh8UOtGxvtQYHZ3UWJEk22s5Rugc2xSVkXTwQzHDu59skX1BC2VWM6OaViinvlwZRGquDJW-adCLvRZqN5QTWNJY-EFyYM1-s_clgOo_5AyyDLZoiuJpyVKaA-WBavg0Zt7y5YjOH2f6aSVKzljoGWi_S3KAos-J0WTn5Mwa_xrJnU94RRuIqPBX9c5LdoIE8MyMNCB_ufZEY619pAmquJss0KbMrb8EugmKhb70iGMGqxLy8-yCcN8Tu_v1NSsYrGud8Uhx3sdw-mqCrw3KcAUtWmmMJisnoqH9D9BINGK4kCLjdJjDdPPmtlt99nqPS3t32hAdcVT1zb9etqyFUKI6bkDnsQUTkuH13M0Nmy2-6XEpdcdg6Jqu5yR57lOXxqY5BbOP7Gq5bwKpmrvji2ohpIATv4ncrHstaFjW2usSNAtwZ1Ahq0ylS-d4TcPySZaY3et2lMi4GjPy7y-m7oMvRgfeJmzodZ2DV3dLptlWJ4mFJEQoRIXohxD1q9vrg3xIMWXEQHzzrpSRtpJ_ka0-A-y92NNw95xlteNOKUx4ki26vLBvFw0WC_QO5PgcMb9V_GolCnNzxwVktKBqreKIDupb1OqB9cO8HMn_tsMgE17nRstTbcQoVL8BrO8x9dy3GDBCAAubzqk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
صحبت های وحید هاشمیان علیه پیمان حدادی:
حداقل درویش از مدیریت الان مرام بیشتری داشت و به نظرم برکنار شد چون من را برکنار نکرد. چطور برای اوسمار این چنین مراسم بدرقه ای انجام دادید ولی با من این گونه برخورد شد؟
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139920" target="_blank">📅 23:38 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139918">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b780a05a54.mp4?token=Elv-paQaS8c2JJzm96IhlQxya0VaZax60_5tUEEqTXWq6ZHJYiy4IgtMohTWL1D8GHhkyaa0JsElnLd2hwR6Mnl4m88ss4mtYj22eNP3Ra0Od4i7j0eg2EkVfPzPkUYn8_DjzPyn-W80oUtbVca0QY809MgU3zXbf_NZYjYkZrhEbXvVbd9n3UE8v1_c-T1NH0MbrRYrk8tTV618egZD9GOcnjsBbOHcYlKk_MBK45Bh66EbDlrD7u8Nm5SCJsXF8UsbdX38gzHpqSa9M7jwbdby-KrPOnRPK8zTBLVqNze8jKJBj6OnQhswr6ioXTkm-GK1qVMGqp1DcvWnGE1bcIfQ71npUpYCZUl6_dj72_J_W-dyYnq_zQ7Vb2CuPJP0KS3YHSVlX-LKwhgDTQP9o-DNxxYVnVpvWa400T3FVkI3C8zrhBg5d539IXF2p6NQkHEEhCNNIPHdQzYI7TvZmFpshdvdMia25IFHbIJP3gC9O0Fb8nv9hBNy-9iMoeio6iGfzr9m9tj1_R8V9XYE5Pyn9Qfg-9sX2c2UYemxRuJDDPE8S775-1U0yFJ8RxH6LguE9bTH5Xp8tG8-9re0YFwH9uhrROiygcZ_Owz8q_DLxpB07effftepnVDHrrD9qfoUi-ZAPUu2uVzguQfxullPHZwJKLRhaRP7zXn8YT8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b780a05a54.mp4?token=Elv-paQaS8c2JJzm96IhlQxya0VaZax60_5tUEEqTXWq6ZHJYiy4IgtMohTWL1D8GHhkyaa0JsElnLd2hwR6Mnl4m88ss4mtYj22eNP3Ra0Od4i7j0eg2EkVfPzPkUYn8_DjzPyn-W80oUtbVca0QY809MgU3zXbf_NZYjYkZrhEbXvVbd9n3UE8v1_c-T1NH0MbrRYrk8tTV618egZD9GOcnjsBbOHcYlKk_MBK45Bh66EbDlrD7u8Nm5SCJsXF8UsbdX38gzHpqSa9M7jwbdby-KrPOnRPK8zTBLVqNze8jKJBj6OnQhswr6ioXTkm-GK1qVMGqp1DcvWnGE1bcIfQ71npUpYCZUl6_dj72_J_W-dyYnq_zQ7Vb2CuPJP0KS3YHSVlX-LKwhgDTQP9o-DNxxYVnVpvWa400T3FVkI3C8zrhBg5d539IXF2p6NQkHEEhCNNIPHdQzYI7TvZmFpshdvdMia25IFHbIJP3gC9O0Fb8nv9hBNy-9iMoeio6iGfzr9m9tj1_R8V9XYE5Pyn9Qfg-9sX2c2UYemxRuJDDPE8S775-1U0yFJ8RxH6LguE9bTH5Xp8tG8-9re0YFwH9uhrROiygcZ_Owz8q_DLxpB07effftepnVDHrrD9qfoUi-ZAPUu2uVzguQfxullPHZwJKLRhaRP7zXn8YT8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚽️
❤️
🎙
انتقادهای تند وحید هاشمیان از مدیریت پرسپولیس: وقتی سرمربی دارید چرا به او احترام نمی‌گذارید و رسما اعلام می کنید که دنبال سرمربی دیگری هستید؟ همین می شود که بازیکن هم به سرمربی احترام نمی‌گذارد
🔴
همین جریان و اتفاق را هم برای اوسمار ایجاد کردند و این رفتار اصلا حرفه ای نیست
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/139918" target="_blank">📅 23:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139917">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c45fdbb36.mp4?token=W2GCVVDA-dkhbP3WhJ8FMLpdmoOc2n1tiWsdmdqp07yVY6J_AU2u-8pikSABZUrRim_AbS2Y03QZaRSBmccw98BTejPrhjWTD7qpzFwmu6BJDQCb5A8HH-CZsFb5kYd9G6nhte8-wo3ChVNWy7yXUU0-PM0FHWwu0hgzStqxRslIZ5kzIWW6_Yf_PCiaHaHXSAWjCk6CbtCl8sqB0HvKJRtuAa87jNxXm0kp4VUB5rzwdejX5Sg-B5YiX-6L0wtxSJdtac5Da0eTwjvk1WvWOHDDT1Ay4dg_FkFSOif3Q_L4Aoeh95L01XdfqpBUA1ir4b8yY_c3lNfQ8zjqCKT20YF9r0S8O6UcFpx1EaWjfd5zJWJxcN93S0_OvVdCV8ZmQj33lCj7yvwaWW1_ShbkXngnVm4ythjePYNktbGJIIbB3rVkUY73iNbFwBy1q7QCogmuvAelS7ltQSKeFh__wWnquFhiLfhvd1i_BvOT9IgNnrkD3xkSwxG-XFEq9kChAtfkBU2pZxoEQsZLp0OuidRu5fpaPfJr17QG0MXnFx_Ri3wMV9C7OgIJ3zkgBpFckm3dWPyvc_0GgmH4LZYXkOPyKwB7V-i09LJrNt2XBn9_Rz_3RNxxrYmB-hT4AyqIpzJEusDMrFdWkbXQJJ6cQAulJ1O9E1wCvkkuppNec5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c45fdbb36.mp4?token=W2GCVVDA-dkhbP3WhJ8FMLpdmoOc2n1tiWsdmdqp07yVY6J_AU2u-8pikSABZUrRim_AbS2Y03QZaRSBmccw98BTejPrhjWTD7qpzFwmu6BJDQCb5A8HH-CZsFb5kYd9G6nhte8-wo3ChVNWy7yXUU0-PM0FHWwu0hgzStqxRslIZ5kzIWW6_Yf_PCiaHaHXSAWjCk6CbtCl8sqB0HvKJRtuAa87jNxXm0kp4VUB5rzwdejX5Sg-B5YiX-6L0wtxSJdtac5Da0eTwjvk1WvWOHDDT1Ay4dg_FkFSOif3Q_L4Aoeh95L01XdfqpBUA1ir4b8yY_c3lNfQ8zjqCKT20YF9r0S8O6UcFpx1EaWjfd5zJWJxcN93S0_OvVdCV8ZmQj33lCj7yvwaWW1_ShbkXngnVm4ythjePYNktbGJIIbB3rVkUY73iNbFwBy1q7QCogmuvAelS7ltQSKeFh__wWnquFhiLfhvd1i_BvOT9IgNnrkD3xkSwxG-XFEq9kChAtfkBU2pZxoEQsZLp0OuidRu5fpaPfJr17QG0MXnFx_Ri3wMV9C7OgIJ3zkgBpFckm3dWPyvc_0GgmH4LZYXkOPyKwB7V-i09LJrNt2XBn9_Rz_3RNxxrYmB-hT4AyqIpzJEusDMrFdWkbXQJJ6cQAulJ1O9E1wCvkkuppNec5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
❤️
❌
گلایه وحید هاشمیان از احمدی و مدیریت اسپانسر اصلی پرسپولیس؛ صحبتهای او حرفه ای نبود
🔻
احمدی گفت که هاشمیان نبود دورسون و امیری را رد می کرد و این حرف در رسانه حرفه ای نبود و میتوانست شخصا با خودم صحبت کند/ صحبتهای او فرار از مسئولیت بود و در شان یک مدیر نبود
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/139917" target="_blank">📅 23:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139916">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✔️
فراز کمالوند، سرمربی تیم خیبر: الان که پرسپولیسی مخالف لغو که سه ماه پیش اصرار داشت تورنمنت 3 جانبه برگزار شود، در حالی که همه مخالف بودند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/139916" target="_blank">📅 22:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139915">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
روشنک :
✔️
✔️
باشگاه‌هایی مثل سپاهان، آلومینیوم و.. به ما اعلام کردند که اگر هفته هفتم را برگزار کنیم نمی‌توانند بازیکن در اختیار تیم امید قرار دهند.
✔️
✔️
فقط پرسپولیس درخواستی برای لغو بازی‌اش در هفته هشتم نداشت.
✔️
✔️
نمی دانم سازمان لیگ چه گناهی مرتکب…</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139915" target="_blank">📅 22:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139914">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wver5GJVLoW4G2bv3MeONJiLInzCozYTlJDtR4NsNcMiyZWyFPizDd_Do-FzHI4fH0CR9IJtR_BRoll06eFZd1U8WWoNNMGRpFvDKXtlD8fNxq9VIzH0xm6Clbr0WfrPUHqwt_t1EvstlTAapFVtWad4HDPFEphPK8QqeG9UQJiqLpx4DRmuFIdxBaDNEah7gjrnvHypDKq9yauUcrqFXQJIi2p7XYBafvh6JBiSNodFLjwAsrm0mbWiySCkpAWnM7lTIvXaZYpd3pm_LRibqfY8F_skKvj0ITeihDkNKhPdNPapb4XNwaxLKtDU5szkY93AxDRvVNyCbN7xXd4vTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
با وجود لغو دیدار برابر خیبر خرم‌آباد، پرسپولیس امروز هم طبق برنامه تمرین کرد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/139914" target="_blank">📅 22:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139913">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b227fb7993.mp4?token=Yp7Avy7yqdr_TvBDxAdhRECVU5_3x25MNb-lGsRGFyHVT3cDDDaCAQA_cG9TIeyLKpNYYKopRzQH4ROW2858Rcra947OLKJQyxcC8v73j0-DP1hGgsGunfx5qSyYb8t4RGksD0vtlroxCBKgM62RAgCDw-cWUloYMJFA9dvReTBXfDALEOGDNAWp3MowQnUgK2gvYDmeyd_D-isR1GdB9ceYhAKkvwt-BQTf-urAALLp-qb_BV3bTgZmBvKwOM-LL-eQ2CUNPGr9UTUdXzqONIYBQXVUqtWjfE4oifBhLs9XIj0kUt4YJQuZIp_gW397fKefEkUX5P0v9Sbz0Jw6-ZvkHdpYHnoA-4dP5aAWb4KdSgsX1NsQVdx8Il9B5ogYFXJk8neYggj60u2ErZQtSl1UrK8qswg_oHaHFJxmAkVe7C6ttFgdUs9WQmzS4bBrQA4iDNVuNx4jzqjFPkaIUUuy3uuFG5Ey6j5HGorvwGZ-g1KWrBQUQ3xqCt2WpntYkveIw2gdXsoTB4VychVPQpLE1q8_sBzJMO8vUWfl2wSyxOtuU4dV29E1ynChyBYLgil38iUQWInaf6MpStu3pGcGV9F-Gimj4ShCGM2S_psZzRITO_2yxj97kmNrAPwhRmzWcsMDB6UHlpgTmqRDJJzGt2ODp0vYpAB7PX72zDI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b227fb7993.mp4?token=Yp7Avy7yqdr_TvBDxAdhRECVU5_3x25MNb-lGsRGFyHVT3cDDDaCAQA_cG9TIeyLKpNYYKopRzQH4ROW2858Rcra947OLKJQyxcC8v73j0-DP1hGgsGunfx5qSyYb8t4RGksD0vtlroxCBKgM62RAgCDw-cWUloYMJFA9dvReTBXfDALEOGDNAWp3MowQnUgK2gvYDmeyd_D-isR1GdB9ceYhAKkvwt-BQTf-urAALLp-qb_BV3bTgZmBvKwOM-LL-eQ2CUNPGr9UTUdXzqONIYBQXVUqtWjfE4oifBhLs9XIj0kUt4YJQuZIp_gW397fKefEkUX5P0v9Sbz0Jw6-ZvkHdpYHnoA-4dP5aAWb4KdSgsX1NsQVdx8Il9B5ogYFXJk8neYggj60u2ErZQtSl1UrK8qswg_oHaHFJxmAkVe7C6ttFgdUs9WQmzS4bBrQA4iDNVuNx4jzqjFPkaIUUuy3uuFG5Ey6j5HGorvwGZ-g1KWrBQUQ3xqCt2WpntYkveIw2gdXsoTB4VychVPQpLE1q8_sBzJMO8vUWfl2wSyxOtuU4dV29E1ynChyBYLgil38iUQWInaf6MpStu3pGcGV9F-Gimj4ShCGM2S_psZzRITO_2yxj97kmNrAPwhRmzWcsMDB6UHlpgTmqRDJJzGt2ODp0vYpAB7PX72zDI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
به مناسبت خداحافظی گولسیانی، یادی کنیم از گلش به مس تو دقایق پایانی که باعث قهرمانی پرسپولیس شد و باسن خیلی از کیسه کشارو سوزوند
❤️
🔥
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/139913" target="_blank">📅 21:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139912">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✔️
فراز کمالوند، سرمربی تیم خیبر: الان که پرسپولیسی مخالف لغو که سه ماه پیش اصرار داشت تورنمنت 3 جانبه برگزار شود، در حالی که همه مخالف بودند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/139912" target="_blank">📅 20:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139911">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🤩
🤩
🤩
🤩
🤩
🤩
💬
گولسیانی:
⭐️
من تو تیمهای زیادی بازی کردم ولی یه تیم هست که وقتی یه بار داخلش بازی کنی و بدرخشی، دیگه از قلبت بیرون نمیره. نمیدونم چرا ولی وقتی یه بار تو پرسپولیس بدرخشی دیگه پرسپولیس میشه عضوی از خونوادت. من رو نخواستن ولی من تا ابد عاشق پرسپولیس…</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/139911" target="_blank">📅 20:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139910">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dz3QHKC2Ew4-NnbAA7PDz8Oi8JcJkf2MfyNp-MxuMqLXTpr4V5ouJ51yucCMwPlglt5ei32uB3HhMvuN9XBZ9qn0-nF984SXOS3W46XtAZWn4PmEOgK-nJ3Jq3TPRlKJWAQKk33gvTXDVRQX7O7WHNX4zh8n6yr9EHLp3eKWPVmAzEu695WN0adEKnTC7CM0_xT3OCSvLpkCMxyEI3wZUrDzI7s5HUWbDA4zdbfAynSXCadrjK9SkIMnQXXPPaA52BNTUzte2VISZEJVY4s4qmJ4rOm9hyi1ruJKWuhP1NeWNbdO59907j-lec_dpin7JxG3LBeE7YncwNOD37IAJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
⚽
سالاری از پست مشاوره مدیرعامل پرسپولیس استعفا داد.
🔻
محمد رحمان سالاری عضو هیات رئیسه فدراسیون فوتبال که چندی قبل به عنوان مشاور پیمان حدادی مدیرعامل پرسپولیس انتخاب شده بود از این سمت استعفا کرده است.
🔻
سالاری به توصیه مهدی تاج رئیس فدراسیون فوتبال برای توسعه رده های پایه و کمک به فوتبال از تاریخ اول شهریور در پیامی به حدادی اعلام کرده که دیگر به عنوان مشاور او فعالیت نخواهد کرد و از این سمت استعفا داده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/139910" target="_blank">📅 20:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139909">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✔️
✔️
✔️
فراز کمالوند سرمربی خیبر: سازمان لیگ تصمیم بسیار درستی گرفته است که بازی‌ ما با پرسپولیس را لغو کرده است/ من نمی دانم سر و صدای دوستان برای چیست؟
☹️
☹️
☹️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/139909" target="_blank">📅 20:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139908">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✔️
✔️
فراز کمالوند سرمربی خیبر در گفتگو با ورزش سه:
🗣
باشگاه پرسپولیس ابوذر صفرزاده را از ما خواسته و ما گفتیم در شرایطی این بازیکن را می‌دهیم که حسین ابرقویی را بگیریم. همچنان هم در حال مذاکره هستیم و به نتیجه نرسیده‌ایم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/139908" target="_blank">📅 20:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139907">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-0tAZdbrY2B56Ul95s97GwvC-r2M5Zt_GtWYQ96ZSrCkgNpeDAasDpoLa1byBR7xBqhxMWfcrkfwiO4LHOCKeqCfEvCYR4KXwzfJtm2IBzN8GFpksTDNfN0AiX8vzpI_-pdCNoBe_ZW6ZYIdP6EJY8f6r2XI-OxHxbkIQV5k1Dp433LSPrr6gLXOjoyPkct4b-oCUIA6k2z1Qxc4Ks6hfmfsfeiEbryq5fIP5SZL64gEpigtOE7C8WZBlgVFyKDS9Fq4Jh4yTcragzjaowcOEQlVX7zKl3YLJXLcmVpd_3ykNwr-udvTu8l3avCNnT2BdCdS1-LkvYKlex4nJV8hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نبردی نزدیک و تاکتیکی؛ والنسیا با تکیه بر امتیاز میزبانی به‌دنبال فشار بیشتر است و سویا امیدوار به استفاده از فضاهای دفاعی حریف و ضربه در ضدحملات؛ دیداری که می‌تواند تا دقایق پایانی کاملاً پایاپای دنبال شود.
[
سویا
🔴
🆚
⚪️
والنسیا
]
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه دریافت کنید.
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
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139907" target="_blank">📅 19:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139906">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❌
❌
❌
تیکدری: روز اولی که به پرسپولیس اومدم گفتم با تمام توان در هر پستی بازی میکنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/139906" target="_blank">📅 18:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139905">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hU-qbXCD0hvXM3A7fUR-vnTcEwhrk-5zF3HVQuvxZKRS-Grd5pqtOMeYOFjJXMslLbus0ekeyvf3ltTR1AdVgjiWM1JC92stFtiZ3hYk-aeeruZ6xoc2ltPp2Qga5T4rUL1JLqhMM1UyxVsbnWwsb666tcsG8u4PIOxcjzvbHIu5cJnHny8cGZTj-GT5lpFeDmrZlJH9RB3igB--9WCQ9aIx71EzZarHrd__yw3xYwZjbC0W5sN4MUiF8j76ah6xvT2Op2gTbKpr5nRP4Zzmeg182UPwIJ-HYjffHKZQddFTgQCl0mtjOleVBBCvjU70ruoNB_Ke1fGretkyKZngRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
ورزش سه:
🔄
🔄
علیپور و خدابنده لو به خاطر عملکرد خوبی که تو 6 هفته ابتدایی داشتن، در لیست قلعه نویی برای جام ملت های آسیا قرار دارن
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/139905" target="_blank">📅 18:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139904">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✔️
✔️
عباس کهریزی، آلترناتیو محمد عمری در پرسپولیس!
✔️
✔️
طبق شنیده‌ها مهدی تارتار سرمربی پرسپولیس اعلام کرده درصورت جدایی محمد عمری از پرسپولیس، مدیران این تیم تمام تلاش خود را برای جذب عباس کهریزی وینگر 21 ساله آلومینیوم اراک بگذراند. کهریزی از استقلال و سپاهان…</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/139904" target="_blank">📅 18:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139903">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
❌
مهدی تارتار بزودی و بعد از بازگشت دنیل گرا به تمرینات درباره‌ی ادامه‌ی همکاری با او نظر میده/فارس  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/139903" target="_blank">📅 17:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139902">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✔️
✔️
پرسپولیس برای خرید امتیاز و راه‌اندازی تیم «ب» با بعثت کرمانشاه و فرد البرز مذاکره کرده؛ قیمت پیشنهادی این دو تیم هم به‌ترتیب 120 و 125 میلیارد تومان اعلام شده. احتمالاً تا امروز یا فردا تکلیف نهایی خرید امتیاز مشخص میشه
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/139902" target="_blank">📅 16:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139901">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6l5XzU546mge7fK59Yufxt9tFpjxvPFxlsGuqeYSIsDSMTH80KFOpP4Nn9xRm2-g6nhdmbvCiJ9h7-gz302YC00yYBbhVmBZjZ_kTRdsazkV8kEFgoDPrikxYPmViJMXiG5Lm7HEM-n3QqerXYn77e9JffstQUtK7Xujv6kInTbp0hLFbkTT88tOPisIellN8PZ0547RmddTVEnuW5duKcYYlr09Xn-99PNpDq2cykyd3qK7j2KhJJ5D0aqfyCrCCNLXr863ivpme6kJA_N7I28VYptgrlmQp9kOgg11wYGqOrhgaEXjOdLI2en9fnCI_lU3TLdUKoWznyLZ3mPyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
⭕️
پوریا شهرآبادی ۱۵۵ دقیقه ۲ گل
✔️
شهریار مغانلو ۶ بازی فیکس ۴۶۰ دقیقه ؛ ۲ گل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/139901" target="_blank">📅 16:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139900">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✔️
✔️
✔️
مصدومیت یاسر آسانی از ناحیه فسخ غیرقانونی قرارداد و غیرقانونی بازی کردن وی برای این تیم هستش و بعد از بازی با السد خوب میشه
🔄
🔄
این مصدومیت در لیگ مملکت با کمک فدراسیون برطرف شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139900" target="_blank">📅 16:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139899">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/139899" target="_blank">📅 16:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139898">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✔️
✔️
✔️
🧤
علیرضا بیرانوند نتوانست کلین شیت های خود را ادامه دهد تا رکورد هشت کلین‌شیت متوالی پیام نیازمند در لیگ نوزدهم، دست‌نخورده باقی بماند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/139898" target="_blank">📅 16:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139897">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
❌
فووووووووووووری
✔️
اسماعیل کارتال سرمربی فنرباغچه پس از مساوی مقابل رم در هفته لیگ قهرمانان اروپا از سمت خود استعفا داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/139897" target="_blank">📅 16:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139896">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✔️
✔️
✔️
مصدومیت یاسر آسانی از ناحیه فسخ غیرقانونی قرارداد و غیرقانونی بازی کردن وی برای این تیم هستش و بعد از بازی با السد خوب میشه
🔄
🔄
این مصدومیت در لیگ مملکت با کمک فدراسیون برطرف شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/139896" target="_blank">📅 15:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139895">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🏅
❤️
فووری از رسانه داریو ازبکستان: باشگاه تراکتور به دنبال جذب اوستون ارونوف وینگر ازبک تیم پرسپولیس در نقل انتقالات نیم فصل است
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/139895" target="_blank">📅 15:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139894">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7h-NcOtPHsbzPdLk08yeZeHpJFqGyBO7D57NtuZAl6s7O-adGxZok9scTwvzONp5pNI_zUC7z2L0Vlgicz6HMOJosm7ogUf7rFgAG05OnL_kCqQAjsA4Q1YMYEd45MZIW6ZpovyL6tU5CkWw2L4VlhcazBMoQHtjS021S6n538AI8BNN7tz-QNfzxCW_riJVhDLNchhqWXv3MbmnVcXbF1mpYtqaOsmhNmRmd2oW8KBzdxBBR2OUN4QMcQhLz2FVpP9kMzaQ6aC1fSZr1UW5glsGo3J_TF3ofEkeu79gBPGSwkd3VBtNS-tH_Cjcz--t91t9GxiFka_tdczpeoWVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏅
❤️
فووری از رسانه داریو ازبکستان: باشگاه تراکتور به دنبال جذب اوستون ارونوف وینگر ازبک تیم پرسپولیس در نقل انتقالات نیم فصل است
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/139894" target="_blank">📅 15:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139893">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEwyCE9a-q-glXNFqVZiTim8xCnNXlGRzl89D71GIMEgje6edxV4WZequuNw2dXW-AG5cd5R4w2WY6WAjow-lx9O7m1J8ilU_w0ztykx2mi8U4E3qW80ARE6CT_lJ_09UW4dv-D4i5w50pJVaKMRE05I8Li5U-WldIZbiRymxSaRe530mDRwSux5tgFyT6YFJihbCfBHfKBH-qeBdI5qt4kaoYV0HFGuy_Ji0C4NBlrCH7aPiLoOoBps4gmDFC40mawzClVjSIfrbo34xmps_QpRDw4MYG8zUv6CvrEIhS2Zdn7ApaOWejlvrGryrBSTRSFXAe3-EOrn4wGiG_qH3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
عباس کهریزی، آلترناتیو محمد عمری در پرسپولیس!
✔️
✔️
طبق شنیده‌ها مهدی تارتار سرمربی پرسپولیس اعلام کرده درصورت جدایی محمد عمری از پرسپولیس، مدیران این تیم تمام تلاش خود را برای جذب عباس کهریزی وینگر 21 ساله آلومینیوم اراک بگذراند. کهریزی از استقلال و سپاهان نیز پیشنهاداتی دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/139893" target="_blank">📅 13:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139892">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✔️
✔️
جباری: اورونوف قطعا مورد اعتماد ماست نیاز به زمان داشت تا با تفکرات تارتار هماهنگ بشه ما هم وقتی دیدیم پیشرفت کرده برای تشویق فیکسش کردیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/139892" target="_blank">📅 11:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139891">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">⬇
علوی سخنگوی فدراسیون فوتبال: پرسپولیس دوست داشت بازی‌اش لغو نشود؟ باید بگویم از آن طرف خیبر درخواست داشت که بازی‌‌اش لغو شود
✔️
✔️
خیبر فقط یک ملی‌پوش داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/139891" target="_blank">📅 11:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139890">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QaXcSWEPnMDH_OpLVVLN3AIS1-islqplEqdvvw8CMPcl58P5jfjuleodpLj6la9lsKdQ273c8_yUoHiDTjzCrsCPzhzqtGQoAo-cUq5QRfLPM29F35RQayCRsQFF6o6R_T-EJ51dHY0j4oUt0ue46Go-0vqq_0DCrLaNzp3uYERwmKOhTmQOIGSnqODcPWnEWupuwTggz0siCl3xn-8u8V0OH7tUVEWW-3yv_-KusL5q0XEB4qrBZHX0OcqwlXU_3JnnZ6EGwp9RZGhlLo5T5fOSVX0WrpG4m3TM9Drg2Rb3shiKTjFpOOlA1xxp75Ut7u7di7MBHmwzJC4jbE3tzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
از دیروز و با آغاز دور جدید تمرینات پویا اسمی مدافع وسط 17 ساله که همراه تیم ملی جوانان در ویتنام حضور داشت در تمرینات پرسپولیس حاضر شد و اکنون پرسپولیس سه مدافع آماده برای جانشینی محمدمهدی زارع در بازی با خیبر ( در صورت برگزاری ) در اختیار دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/139890" target="_blank">📅 11:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139889">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✔️
✔️
این بازی لغو نشه خیلی به نفع پرسپولیسه.
✔️
✔️
تیم به هماهنگی نسبی قابل قبولی رسیده و دلیلی نداره الکی وقفه بیوفته.‌ خیبر هم توو اوج نیست!
✔️
✔️
ضمن اینکه سه بازیکن ملحق شده به تیم امید جزو بازیکنان فیکس ما نیستن که جای نگرانی داشته باشه.
✔️
✔️
تقویم رو بی‌دلیل…</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/139889" target="_blank">📅 11:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139888">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✔️
✔️
آسانی مصدوم شده یا از ترس شکایت جلوی السد نمی‌خوایید بازی کنه؟ ///اعظمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/139888" target="_blank">📅 11:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139887">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❤️
❤️
❤️
خداداد در طول این ۴ ماه حق ورود به هیچ کدوم از ورزشگاه‌های کشور رو نداره
🤣
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/139887" target="_blank">📅 11:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139886">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✔️
✔️
۵۷۲ دقیقه مقاومت بیرانوند برابر رقبا
✔️
✔️
علیرضا بیرانوند از آغاز فصل در ۵ بازی، ۵ کلین‌شیت پیاپی را توانسته است به‌ثبت برساند؛ اتفاق ویژه آن‌که بیرو در آخرین بازی فصل گذشته تراکتور در لیگ‌برتر مقابل گل‌گهر هم توانست دروازه‌اش را بسته نگه دارد تا ۶ کلین‌شیت…</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139886" target="_blank">📅 11:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139885">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✔️
✔️
رضا جباری مربی پرسپولیس :
✔️
من با علیپور صحبت کردم و قول گرفتم که بتواند امسال آقای گلی لیگ برتر را به دست بیاورد و این مقام را تقدیم به خانواده‌اش و هواداران پرسپولیس کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/139885" target="_blank">📅 11:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139884">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❤️
❤️
❤️
علی علیپور با گل امشب رکورد علی پروین را شکست و دومین گلزن برتر تاریخ پرسپولیس  شد
😀
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/139884" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139883">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b893ef9367.mp4?token=ipe2jUc5Es2Mn8Oj8rngIBjUqxnw6LkxPH7MuLIGDv37VtT-4DrfZy5ZMf18B_ipYJtUYWPkYno81rn0LXH3L_ZY9UwbPRacB5AQqCWeN68cJApDAOobBkPpIm1rPgV9YGuRV_SdUwbGbh7V2G75jbqolAVN9G-kgLdEnpL0mTMTsmSd1kbpn_N-qsy0mVo4zYT8Cu-FACZ-N6xUnJ7RxvinMQJ1ilr6wFQW0bd3ITEgt9KXQ3Zl_Z9PCAPjiiyAxzIVUdD4ww666jbAN0UhVhDpxPpXGecf-3Tnr8ATFRPvn0QL5a8Bahp3h69zA89WJpOy4dzfTkJTE4ILkNz1pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b893ef9367.mp4?token=ipe2jUc5Es2Mn8Oj8rngIBjUqxnw6LkxPH7MuLIGDv37VtT-4DrfZy5ZMf18B_ipYJtUYWPkYno81rn0LXH3L_ZY9UwbPRacB5AQqCWeN68cJApDAOobBkPpIm1rPgV9YGuRV_SdUwbGbh7V2G75jbqolAVN9G-kgLdEnpL0mTMTsmSd1kbpn_N-qsy0mVo4zYT8Cu-FACZ-N6xUnJ7RxvinMQJ1ilr6wFQW0bd3ITEgt9KXQ3Zl_Z9PCAPjiiyAxzIVUdD4ww666jbAN0UhVhDpxPpXGecf-3Tnr8ATFRPvn0QL5a8Bahp3h69zA89WJpOy4dzfTkJTE4ILkNz1pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حردانی: آقا سهراب جواب تماس هامو نمی‌ده
🤣
🤣
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139883" target="_blank">📅 10:37 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139882">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❤️
❤️
❤️
علی علیپور با گل امشب رکورد علی پروین را شکست و دومین گلزن برتر تاریخ پرسپولیس  شد
😀
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/139882" target="_blank">📅 10:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139881">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✔️
صبح آدینه تون بخیر و شادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/139881" target="_blank">📅 09:18 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139880">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0DCaaj8rTutg20nD_-mRGCcl3t_pEc8lKR_VJAUnI1ed6FUme8iawP6kG4iATYLPR7PFwJoNwWCAyMzqyWt_7ty723SOB9-0GX0t3pH50WVgsPa3kbPrpizKDdFUsHq4Q7weL3EtugwFza8-FctNUYzwjEa_3Tbw9sxdknZaTyw3VRCVTvpJUi-BWnD-I79OEkk2r488aQpH6EAdis1QE9gK2vn0VF7mxCmkC8I3QK89xVvGfZ7RGKZh_IpvKHI_7mUfef54GXZRrsAzVlxavjtKIVKBbsb8lA-i9ABW-kVnFXBu-7g3Jb-0_KC6XGgavR_a50HhucP1rP4f1qYPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
سابالانکا مقابل پگولا؛ قدرت سابالانکا برابر بازی حساب‌شده پگولا. ریباکینا در تقابل با گاف؛ نبرد سرویس‌های سنگین با سرعت و دفاع. دوئل‌هایی نزدیک که تمرکز در امتیازهای حساس تعیین‌کننده است.
🎾
Sabalenka -
🎾
Pegula
🎾
Coco Gauff -
🎾
Rybakina
با درگاه بانکی اختصاصی و امن وینکوبت، حساب کاربری خودت رو به‌صورت مستقیم شارژ کن و مثل هزاران کاربر دیگه، بدون دردسر از امکانات وینکوبت استفاده کن.
📌
مسابقات را فقط تماشا نکن؛ همین حالا وارد مینی‌اپ وینکوبت شو و اولین شارژ خودتو انجام بده و پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/139880" target="_blank">📅 01:22 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139879">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
روحیه بازیکنا که عالیه امیدوارم در نهایت بازی با خیبر برگزار بشه بهترین فرصت برای گرفتن سه امتیاز و رفتن به صدر جدول
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/139879" target="_blank">📅 00:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139878">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa7d8a9c3c.mp4?token=YnIOenQX8-FOyyDtTg7-4MisO9BXMK5qL8JLAO95bFECSR3oIfDCYJl0LX6Z_E4XmfsAwhBS5uUDCGMUgGPRtHDJGSw6cU6XYRr3g7JbwM-g7bxFxtySNPVgy9sSmLEqO2zIkz8lC2DeTHIPL3ZWAgJHx_OR8q7gdzo24LNP2ZhqZYPpbY5I0LSHDvux4v_wX-7PcRTSJa6NsctPdWzJfs9z12oGI4B1niz-sMWbm52hdGUvQF7werujkwdr2hui__e29O5CPSb1FKdFpiZ2wuWllBkCYCUJzFVy2Tnu9xPye4xl7HkywdMS1NX9pMhstAM7CYkSzrY4OAoDWXhguDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa7d8a9c3c.mp4?token=YnIOenQX8-FOyyDtTg7-4MisO9BXMK5qL8JLAO95bFECSR3oIfDCYJl0LX6Z_E4XmfsAwhBS5uUDCGMUgGPRtHDJGSw6cU6XYRr3g7JbwM-g7bxFxtySNPVgy9sSmLEqO2zIkz8lC2DeTHIPL3ZWAgJHx_OR8q7gdzo24LNP2ZhqZYPpbY5I0LSHDvux4v_wX-7PcRTSJa6NsctPdWzJfs9z12oGI4B1niz-sMWbm52hdGUvQF7werujkwdr2hui__e29O5CPSb1FKdFpiZ2wuWllBkCYCUJzFVy2Tnu9xPye4xl7HkywdMS1NX9pMhstAM7CYkSzrY4OAoDWXhguDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
دقیقه 95 بازی استقلال و پیکان، یاسر آسانی به یکباره بعد از سوت پایان بازی مصدوم شد تا شایعاتی مبنی بر مصدومیت تعمدی برای عدم بازی در لیگ نخبگان به اوج خود برسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/139878" target="_blank">📅 00:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139877">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✔️
✔️
✔️
اتهام بزرگ خداداد: فدراسیون پول آپدیت VARهای لیگ را نداده و اصلاً خط آفساید کار نمی‌کند و نمی‌توانند سر صحنه‌های آفساید خط‌کشی کنند و تنها با عکس تشخیص می‌دهند  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/139877" target="_blank">📅 00:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139876">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWqSDyeYupFLl3JP5RIGRn_2TnU-TH6mE1hBMDlC1YMehrgf6OVR1ag-KZPSXni2KvGaVNCsrRLe-U6Z5M1ri27kFhN253uhAQEsTqA-1q-K0K79hMrB2TzM8mkYP5hUWnCqxv6OrOVm2waZdvS9izotaMjwxb5mykAhAWxvbj0KOD5I_SfhbSah48IBG752A0FGwlmdRyQ7DssAQfHV4uMdgO80AWBhwp8ThOOXEIjCwp6R1nmBNbPqtMlqokrb9Av_ElSWFNduGSYz9wGbz6M_FKf2xAlwaauY5mFp4ul-HgjY913H6mI3HFDZoCK_3UHuiyIWcysb_2abPgxiBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
جدول لیگ بعد از بازیهای امروز
پرسپولیس با برد خیبر می‌تونست به صدر بره ولی آقایان رنگی تصمیم گرفتن خودسر بازیها رو به تعویق بندازن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/139876" target="_blank">📅 00:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139875">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🗣
🗣
ورزش سه: یاسر آسانی به علت مصدومیت دیدار برابر السد قطر رو از دست داد
‼️
السد قبلا اعلام کرده بود آسانی بازی کنه می‌ره شکایت می‌کنه
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/139875" target="_blank">📅 23:43 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139874">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
پرسپولیس با مدارک جدید دوباره پرونده آسانی رو پیگیری کرده و معتقده حضور این بازیکن در استقلال غیرقانونیه. سرخ‌ها میگن مدارک جدیدشون کامل‌تر از شکایت‌های قبلیه و امیدوارن این بار نتیجه پرونده تغییر کنه.
🚨
فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/139874" target="_blank">📅 23:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139873">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✔️
✔️
#منهای_پرسپولیس
✔️
✔️
استقلال ۴ روز دیگه با السد بازی داره و السد تو پنج بازی اخیرش دو بار حریفش رو شیش تایی کرده به بار چهارتایی و یه بار سه تایی فقط خدا به دادت برسه استقلال :)
✔️
✔️
شما فقط مراقب باش دوباره خاطرات العین و الوصل رو تکرار نکنی قهرمانی…</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/139873" target="_blank">📅 23:38 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139872">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
یا الله بسم الله اسماعیل کارتال ...
🔥
❌
پ.ن چه تیمی داره حاج اسماعیل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/139872" target="_blank">📅 23:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139871">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6DKOB1JF5Zx2e5MOP3Sam-8Of2LCJp6-Vkl6ggVLNMlDrEoc-WssNJOujNHDEwwpMMyRAwjHlk53E2oZWwBBpuyQInUA1fckV92ymKxkszG80GKnAe5UwQu2WldIM9P8IyVQePJxvNoQ2VzNZkc_-tvxRkwL1TC3Yc-xazsFAwN4hFkb7xOnGVQcAQ4TY5AIeiObyAi2AOHd2OLOi7PauRJz_zgT9HKkVKwtFHx_hCgt-0yqIcXHPBqFYkRpKJInxJmRRsWC1te3GRmlYNOeA2C2wuswzOiJAGkBjgW2EaBrF_kKBUCGiZ6AC7F5XThfuLaXlGufLO3eNWsB2QXGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
پس میگفتید که استقلال خوزستان ضعیف بود که ما چهارتا زدیم؟
😁
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/139871" target="_blank">📅 23:32 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
