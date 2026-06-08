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
<img src="https://cdn4.telesco.pe/file/SnJb7UlggJViluTN9Vr-LAUnH7tKgyqnXSSsyEJxKlWbLfo4UvSxevUFfunxaIzm1_K2WpPqxk2BshIy8rQj4RH1PpPmuuUKLXR-jY8jvSPQ2Qhzov6ZJv48zxZDHvA8x-C2-m-Nuq5z3B84AyKtxM-1rBMyRtncM1RpQVTppH3YlQQb9rjCbHa5Pvm6CilDfqlSbU98FOE3i0ZNhUfVMzD6K7iBWOx2M-1EUjM-Le2YoW5JSqhpL5PFISh8oBUWLjHN_GHS7MDBQcdHFcELk8IzY9UpqT9PZqXu2Qt5czM5OFZkpG8Anv2MN45N2Yn-P-Syge9KnnADGeHTUBnw7A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.25M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 05:08:07</div>
<hr>

<div class="tg-post" id="msg-657119">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">رسانه‌های اسرائیلی: اسرائیل در حال آماده شدن برای حمله موشکی فوری از سوی ایران است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/657119" target="_blank">📅 05:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657118">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">تسنیم: صدای انفجار در سمت کرج نیز شنیده شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/akhbarefori/657118" target="_blank">📅 05:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657117">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">لحظاتی پیش صدای انفجار در مناطقی از تهران، اصفهان و تبریز شنیده شد
اخبار تکمیلی متعاقباً ارسال خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/akhbarefori/657117" target="_blank">📅 05:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657116">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ادعای کانال ۱۴ اسرائیل: هواپیماهای ما در حال حاضر در حال حمله به اهدافی در داخل خاک ایران هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/akhbarefori/657116" target="_blank">📅 05:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657115">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ارتش تروریستی اسراییل با هدایت سرویس اطلاعات نظامی به اهدافی در تهران و غرب ایران حمله کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/akhbarefori/657115" target="_blank">📅 05:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657114">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">زیرنویس شبکه خبر: رسانه‌های اسرائیلی حمله رژیم متجاوز را تأیید کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/akhbarefori/657114" target="_blank">📅 04:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657113">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">زیر نویس شبکه خبر: شنیده شدن صدای چند انفجار در تهران تبریز و اصفهان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/akhbarefori/657113" target="_blank">📅 04:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657112">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ادعای کانال ۱۴ اسرائیل: هواپیماهای ما در حال حاضر در حال حمله به اهدافی در داخل خاک ایران هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/657112" target="_blank">📅 04:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657111">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">شنیده شدن صدای چند انفجار در تهران، تبریز و اصفهان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/657111" target="_blank">📅 04:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657110">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
مهر: هم اکنون چند صدای مهیب در تهران
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/657110" target="_blank">📅 04:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657109">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
خبرنگار المیادین در بغداد: صدای انفجاری با منشأ نامعلوم در سراسر پایتخت عراق شنیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/657109" target="_blank">📅 04:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657108">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
الجزیره از شنیده شدن صدای انفجار در بیروت خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/657108" target="_blank">📅 04:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657107">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار مهیب در جنوب لبنان
🔹
برخی منابع از جمله اسپوتنیک روسیه از شنیده صدای انفجار در بیشتر مناطق جنوبی لبنان خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/akhbarefori/657107" target="_blank">📅 04:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657106">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
۲۹ عملیات علیه مواضع صهیونیست‌ها در یک شبانه‌روز
مقاومت اسلامی لبنان:
🔹
رزمندگان مقاومت طی ۲۴ ساعت گذشته ۲۹ عملیات دقیق علیه مراکز نظامی و مواضع ارتش رژیم صهیونیستی انجام داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/657106" target="_blank">📅 03:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657105">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
زلزله ۸.۲ ریشتری فیلیپین را لرزاند
🔹
سامانه هشدار سونامی ایالات متحده، تهدید سونامی را برای این زلزله اعلام کرده بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/657105" target="_blank">📅 03:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657104">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
هشدار امنیتی سفارت آمریکا در اردن
🔹
سفارت آمریکا در اردن از شهروندان خود در این کشور خواست به دلیل نگرانی از تهدیدات هوایی در منطقه، به پناهگاه بروند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/657104" target="_blank">📅 03:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657102">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szgAZskrmVERRnaNZHoNoHVmr2Y8u2v4_WgJqnqAEAyEVR91wOBN_F8PMU5qlh8I8I0f4QXNZ-1reRds-9DRTtavQwoST8sSXknFdJpRQvqVWkYKXFMEGzEUyCmkZ-1lGZpV0lrxAHY7t1gQqFKN8Ra3CkIjBzvNz9ErUbLZVLhaICWZwOFtmM3twxDWeSfEW-7I34EvNx7EZLCRrGhZ7jbUvrN3d5uzB0Wm07n7kK1hORaCGWBrHUF85EZeDvg0ZwW7BY3tAaVYLJafJokxT1RocY79ST4_I5JnOTxkQ5sfGQC6LUrEJS7sD0UJx1ATyOxyYqi__kz0AbAhwqyUJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15170a1aea.mp4?token=ipXB9tI78OlLwo8Owx-sfbR2v_paXpi6T0sv1UPYOXEJ-Mgu8xxjNPqnhJXlrkDisZiK-vbHgEjy0tYZifonBfQjwhooFRw0-ewwu801SizpK8BemrzJs8maAVh0CgaO9RzZzam019ROM6PRBCtTDwzlh2jUy2N0VIPcCRQzrOlT10kTnjSXxmhkPri8wn98wyBslzuKuSnmT9P8L4GWJaA2ejWLeYKbSkZxL9YnK2c8DyY-jskR-otWUll2EafFRhcN9kWxqSPeQJc9fiKgnj-Ott3aJSEacRP-ApmUDiAhWeDx-xmmIXsZB5h3gr3S7MU2hTb92n_GlucpEYGZEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15170a1aea.mp4?token=ipXB9tI78OlLwo8Owx-sfbR2v_paXpi6T0sv1UPYOXEJ-Mgu8xxjNPqnhJXlrkDisZiK-vbHgEjy0tYZifonBfQjwhooFRw0-ewwu801SizpK8BemrzJs8maAVh0CgaO9RzZzam019ROM6PRBCtTDwzlh2jUy2N0VIPcCRQzrOlT10kTnjSXxmhkPri8wn98wyBslzuKuSnmT9P8L4GWJaA2ejWLeYKbSkZxL9YnK2c8DyY-jskR-otWUll2EafFRhcN9kWxqSPeQJc9fiKgnj-Ott3aJSEacRP-ApmUDiAhWeDx-xmmIXsZB5h3gr3S7MU2hTb92n_GlucpEYGZEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کنایه کنسولگری ایران در حیدرآباد هند به رژیم صهیونیستی: پیام‌های عملیات امشب: بوم بوم تل‌آویو؛ اگر درس عبرت نگیرند و هشدار عملیات را نادیده بگیرند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/657102" target="_blank">📅 03:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657101">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
ادعای اکسیوس به نقل از یک مقام آمریکایی: مذاکرات با ایران به مرحله پایانی رسیده است و به خطر انداختن توافق احتمالی در این زمان حساس، کار عاقلانه‌ای نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/657101" target="_blank">📅 03:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657100">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
تداوم حملات رژيم اسرائیل به لبنان؛ منزل مسکونی هدف قرار گرفت
🔹
جنگنده‌های رژيم صهیونیستی لحظاتی پیش به شهرک "الحلوسیه"در  جنوب لبنان حمله کرده و یک منزل مسکونی را هدف قرار دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/657100" target="_blank">📅 03:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657099">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
ادعای آکسیوس: ترامپ از نتانیاهو خواست که به ایران پاسخ ندهد!
آکسیوس به نقل از یک مقام آمریکایی و یک منبع اسرائیلی:
🔹
ترامپ در تماس تلفنی به نتانیاهو اعلام کرد که به ایران پاسخ ندهد تا فرصت برای دیپلماسی فراهم شود. باید صبر کند، زیرا ایالات متحده به دستیابی به یک توافق خوب با ایران نزدیک شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/657099" target="_blank">📅 03:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657097">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lk08wEUbyo5VnMe_5Oay5JbiXjDo3QRBFuuGIG2mICJ74UqlbmNImAAOqsI6D2USc-AYFkzfjMEFkZME-jHYn1F3ELkzi20A84qGtuXLSFytvOsQ5uHrViBl19UjkG2zhdAthOWSEVvJUtyAikQJRcAWtIOt0eMo5R1Mm5lgTQdyxShsEA2EY5fWeItBBRs7Shb14K3Q4WpSNnduZXuH6gtZjJNQphVda6JYGSWETYX_r-3MXeoHAAEX6kPhMYvUAxkMOA7TMSQFtmSxcUXVYG0sKEcNanYXU6sgzKc3b2wfdEJWlmhF7b7NQSuQO03TSZSgglCN7DjqMwb46lLEwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفارت ایران در غنا: این شما و این هم تبعات حمله به بیروت
🔹
به شما اخطار داده شد. بیروت خط قرمز (ایران) بود. این شما و این هم تبعات حمله به بیروت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/657097" target="_blank">📅 03:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657096">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
شبکه ۱۲ اسرائیل به نقل از یک مقام آمریکایی: ترامپ زمان بیشتری به دست آورده است، زیرا معتقد است که ما به دستیابی به یک توافق نزدیک شده‌ایم.»/الجزیره عربی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/657096" target="_blank">📅 02:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657095">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
سپاه‌نیوز: جمهوری اسلامی ایران از پیش بارها اعلام کرده بود که یکی از شرط‌های توقف جنگ منطقه‌ای، توقف آتش و پایان جنگ در تمام جبهه‌ها، از جمله جبهه لبنان است
🔹
ایران پس از جنگ دیگر معادلۀ امنیتی را فقط ناظر به تمامیت ارضی خود تعریف نمی‌کند. همه نظم مقاومت حالا بخشی از منافع ملی ایران محسوب می‌شوند.
🔹
از این جهت، همان‌طور که پاسداری از ایران بخشی از مأموریت مقدس گروه‌های مقاومت بود، پاسداری از حریم اضلاع مقاومت و محور مقاومت هم بخشی از مأموریت مقدس ایران بوده است. مأموریتی که حالا ایران به آن به مانند دوران پیش از جنگ نگاه نمی‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/657095" target="_blank">📅 02:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657094">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
خبرنگار اکونومیست: اسرائیل از زمان آغاز آتش‌بس با ایران (دو ماه پیش) تلاش می‌کرد جبهه ایران و لبنان را از یکدیگر جدا کند/ این تلاش اکنون شکست خورده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/657094" target="_blank">📅 02:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657093">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
ادعای مقام آمریکایی: ایالات متحده هیچ نقشی در حمله  اسرائیل به بیروت نداشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/657093" target="_blank">📅 02:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657092">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
شنیده شدن صدای دو انفجار در سلیمانیه عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/657092" target="_blank">📅 02:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657089">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/raS26-CrilJYC3QAaEcaeneHmL4hBfgQBMdhjk8U_rM4w-A6ONJHQc08KtJ1bfe00FMH1Hu0ByQcN09WVhgq69GSw1QU9VhttPoQHXdftxEwqll5qRl3dzvrt3J7axmWiPGvHrSu6OIpSAchSt8DZ_19FnF4GYfGM7O3rezSqSNu6BYpBF9DaGiD--IPHtClsQQWdeAkKRqiae3xOVrJsfr2EUCTjxP7H3HNO4I9squVUrhyiet9rG1m6RJlU_5KKv2O8qpahfjjwZfQtpl4cJ3diyqSm6fbyrYlOH7p3x4OHAgl8KGcyboUCaswPIqYszq5dCvf-z-lIfAIQ49LVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UuKlMyGPm_skO22A3Lo06ak9xXwybGrQJ2QEtWAFtLaO_1cNWp47H75PUi02dPD_O6e0R1RXfg6NGloA31PoFJTpS-boxHR_7RFjHI57ss9YzlUkwmcczd4SiRrmlVZUnlOyHJcrToaVLBtWFNeZ5TPwJB_iDDZlH38x-xnbE0ZyHbsd5oK2XZgUpm-1knXNgPELydaKgJaef7J1pTlCHBJL-pC81a5l5s8LwVEHTIgLoJ0-YCHDa0dgeZu-nAI_vhwChPJS8C4Xmiy-WawgHdhC0qsE2nQ_gLR3-RfGWEG22rLgul67ok9dx2_f-Qg9WgHpGBdoLV5mED5od65tVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ui0egfqLuUobTcuCAqh8SM5uvZTG6DzvUJbEgpMwlt4rNqONn3Rt6-DDC-5tUHsGmAf7u8X3VBqhEJNchnOPYUHkvep3czjoHZjyIuZIahXUmDGR6FCMU7fXBuG269L6B5z5foHLixO0TcK6X9lUH8pcbBalhhZ9Qmgw0z5MfFCqaGU64rPAYrnMuV2qi5mZpyI-owiBWOHfIpmKddGfWR9852paX8uP7GwtQNuyIUYWxtEJwgRelp5fQfxESebJUwlXun0ldH6-V2P_EXy7tZAUmCVe9HeGqQiTJOI7MAXFOEN47gDNeMr8lanlqKRje-rBCtyc3uZS9UEA7hz0kA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
علت ترس ترامپ و مصاحبه فوری او به علت این وضعیت بازارها در روز جمعه است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/657089" target="_blank">📅 02:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657088">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVv-0o-T9ZwIUB3YTbk3L2KCFdiExaPJNWM783I_mEwLkREgsmzbUYfY3lAj44_xal4vLMHZIdOM3UDeIY7ETjvuxyvYv3olnrqVTVU1ms4mF89maxCqWVWAQ0pepzxl67GYlFp45m5qvZsxAtSdQ-HyesIe68q9ByCTXU4nCJeEUd4yFto780hALuHySx0JiIeZrUd_5zOH7CTqQWgffZgAgHdKgkJGTDsuot6SHYbUxc3lkrNkudDlR4_wkJ-NKww5hQTDwZIozJt5OefrOVlW-c7yKoMgPoHP_Iel8aiZ-H982sMK1_4emTJ579yN1kziAjWoBYBKYEqgGqN-hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش فعال سیاسی آمریکایی در پی حملات ایران علیه رژیم اسرائیل: زنده باد ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/657088" target="_blank">📅 02:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657087">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a360d4711.mp4?token=iMmngejvHYRYbO5u_OI_gExfme6EN1rUa83j3zexfaNUsF8A7iFXlJQ7Tq_FR4WlD8G9427m-8NqCVBI6OX--1YBP4nd7Ag4xS-ECrA2r_7WgqMAqwfLOaCOToLUkrEXhipbXve_aM_jiXql4-uVolwaxSoolKOjNU5LrNb78bjYrWKiwKr8TvKa7MOxdR-KFbSstSWvWvDeQziMiRiXfpMHRjmWwwxX3iXSjY9LteueKz2kPP8sOwcZ7S9YjE-VnPp9JrcV9w407BNlVh8DHY68wSCD0PMboJIBM2gc8adh6rdEXpqCVcJn2kQJX4aBOo-OuAcK6AOWHTfq7E7dPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a360d4711.mp4?token=iMmngejvHYRYbO5u_OI_gExfme6EN1rUa83j3zexfaNUsF8A7iFXlJQ7Tq_FR4WlD8G9427m-8NqCVBI6OX--1YBP4nd7Ag4xS-ECrA2r_7WgqMAqwfLOaCOToLUkrEXhipbXve_aM_jiXql4-uVolwaxSoolKOjNU5LrNb78bjYrWKiwKr8TvKa7MOxdR-KFbSstSWvWvDeQziMiRiXfpMHRjmWwwxX3iXSjY9LteueKz2kPP8sOwcZ7S9YjE-VnPp9JrcV9w407BNlVh8DHY68wSCD0PMboJIBM2gc8adh6rdEXpqCVcJn2kQJX4aBOo-OuAcK6AOWHTfq7E7dPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مردم جنوب لبنان خطاب به ایران: ممنون بعد از اینکه حتی دولت خودمان ما را تنها گذاشت، کنار ما ایستادی
🔹
مردم جنوب لبنان حین عبور موشک‌های ایران از آسمان اراضی اشغالی فریاد زدند؛ «ممنون که بعد از اینکه حتی دولت خودمان ما را تنها گذاشت، کنار ما ایستادی»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/657087" target="_blank">📅 02:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657086">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
ادعای یک مقام آمریکایی به کانال ۱۲ رژیم: نتانیاهو «به نحوی» با به تأخیر انداختن پاسخ به حمله ایران موافقت کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/akhbarefori/657086" target="_blank">📅 02:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657085">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
ترامپ: نتانیاهو چاره‌ای جز پذیرش توافق با ایران نخواهد داشت
🔹
من تصمیم گیرنده هستم. من همه تصمیمات را می‌گیرم. نتانیاهو تصمیم گیرنده نیست.
🔹
حملات ایران هیچ تاثیری بر توافق نخواهد داشت. / فایننشال‌تایمز #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/657085" target="_blank">📅 02:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657084">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnVJHmCIjT1KQnFs8_qJrlVk48Of3Wa3dPTBATgsc7AYo-eeHeBChxBOy203-hdy_4fxsl23oa7vtMLq3PWC1pZpORs8DwzPg_oAjWxAcduKkxFC8c5d4NmOWnYwFyWF8MK0wHxERKXskOO8UZqzkIwxqT4JMrMcaB2ZS_0p0vVnUXuWXXRrub2Y1EY_9twHhDsVaVVMgwGxz7swB6BwtOMtimpAT6Q7eoaPrfHkK1u5eMea0iEJBylX7fflwhL7vrOLRCG3wcS3_N9ex8Ln9xoPJIeHATTfAKuO-sHqgNQEk0tW_dfLJac4nCkChYBcDS9pRSAi_NBTDAahOfiRxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یحیی ابوزکریا، متفکر سرشناس الجزایری: دروغ‌گویان و اهل باطل کجا هستند؟
🔹
در لبنان و جهان عرب، کسانی که گفتند ایران مقاومت را فروخته است!
🔹
خدا لعنت‌تان کند ای بردگان دلار و ریال
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/657084" target="_blank">📅 02:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657083">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
اعلام وضعیت اضطراری در بیمارستان‌های رژیم صهیونیستی
وزارت بهداشت اسرائیل:
🔹
تصمیم گرفته شد که بیمارستان‌ها بر اساس طرح اضطراری، فعالیت خود را به پناهگاه‌ها و مکان‌های ایمن‌سازی شده منتقل کنند.
🔹
دستور فراخوان نیروهای انسانی به بیمارستان‌ها برای انتقال سریع به وضعیت اضطراری صادر شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/657083" target="_blank">📅 02:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657082">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
تسنیم: ایران از یک‌ پهپاد ناشناخته جدید در حملات اخیر علیه اسرائیل استفاده کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/657082" target="_blank">📅 02:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657081">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
یک مقام پاکستانی به العربیه: «ما به توافق موقت سریع بین ایران و آمریکا نزدیک می‌شویم. این یا یک توافق فوری است یا شکست مذاکرات»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/657081" target="_blank">📅 02:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657080">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7ukLyeUZFfZbd5aCljHBIffe5qcaFTaR1SLwABb0y66nqtNrWyEBgmGYfGKvajlRw8smcHHi8meQl7hYCpk8fsAw33kWI3o4yITdki_NEmPysslGehEbRNbN8apPKMlLxlyqfiECep42YCTuS84R9RoClhpoaT9pfoOVi7aHopQy4kptK2JvR_Iysf5l-ezQGdMjXg1OYNBMkms3ofwa7XaVdtPx4YtGtbg0fUduVFS2MPyQJc-0EEIef9rkAiJqdVpZ765fvXWLje4Z2Iy_K9tzOmOq-OZFEEbs-uVSbWz0uE2MMaKzX9eZRaKuJByCXFBmfWfaYB39-kW5VBdWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کارشناس یهودی غرب آسیا و فعال رسانه‌ای: بشریت مدیون ایران است
آلون میزراهی:
🔹
امشب، در غرب آسیا، «آزادی عمل»(بخوانید: کشتار) اسرائیل در لبنان به پایان رسید. ایران با موشک‌هایش به آن پایان داد و به وعده خود عمل کرد. بشریت مدیون ایران است، سپاسگزاری و تحسین فراوان.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/657080" target="_blank">📅 02:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657079">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
کانال کان رژیم اسرائیل: در حال بررسی تصمیم به عدم پاسخ‌ در امشب، و موکول کردن پاسخ به چند روز دیگر هستیم؛ در حال حاضر تصمیم نهایی گرفته نشده و بحث‌ها ادامه دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/657079" target="_blank">📅 01:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657077">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
نفت صعود کرد و به ۹۵ دلار رسید.
🔹
واکنش اردن به تنش های منطقه: اجازه نخواهیم داد کشورمان به میدان جنگ تبدیل شود.
🔹
حماس: پاسخ موشکی ایران تجلی همبستگی واقعی میان امت اسلامی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/657077" target="_blank">📅 01:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657076">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6Q47LZx-eTrMd7WdavKlW8veBAghrWyrONfeG70_FeUs6vKOxNJkGO4Zbvt7HWcd_EHD7C7bRyRQrtnyfcJLM0Bd1bRgSi6yOW8RiBp31h8TWhbTOalMg5KAt7r_FOcZcHXRYqTsRCdS_8vZ-ymwU9y-1D52Su6ld3DFJ2ovC9MmuONqd0AASkO9mmfiVUUcyJiPof2m-zT1qlanmIuxLTF9SfPn8ova57NE2Fq0BCDxfMFe7C-6SoySNTr3xKR3Fc1jX1UMqryUeXhCs9Rxoo0uxNWG2GOZr0LaSYf3sYmgkxlFnzsJii-XjWJKIOVusu9Nfxu6ncK97gxFTx4Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران به‌خاطر انسانیت در مقابل صهیونیست‌ها ایستاده است
کریگ موری، دیپلمات سابق بریتانیایی:
🔹
خوشحالم که ایران بالاخره به اسرائیل پاسخ داد.
🔹
عدم مجازات اسرائیل که مدام آتش‌بس‌ها در لبنان و غزه را نقض می‌کند، باید تمام شود.
🔹
ایران در برابر افراطی‌های صهیونیست، به‌خاطر تمام بشریت ایستاده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/657076" target="_blank">📅 01:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657075">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
ترامپ: نتانیاهو چاره‌ای جز پذیرش توافق با ایران نخواهد داشت
🔹
من تصمیم گیرنده هستم. من همه تصمیمات را می‌گیرم. نتانیاهو تصمیم گیرنده نیست.
🔹
حملات ایران هیچ تاثیری بر توافق نخواهد داشت. / فایننشال‌تایمز
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/657075" target="_blank">📅 01:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657074">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
انگلیس خواستار کاهش تنش در منطقه شد
وزیر خارجه انگلیس:
🔹
از سرگیری درگیری‌ها میان ایران و اسرائیل به نفع هیچ‌کس نیست؛ دو طرف باید خویشتنداری پیشه کنند و فوری برای کاهش تنش اقدام نمایند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/657074" target="_blank">📅 01:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657073">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_YXGTlO5EzyuEWY2Ami0N21YP4T1DqnJ6sPlzVe_CB5nDatZ1Whr6wAymfJxogCCXGfPijm78Y0jNFhxpQuPu9i_kP0BNm2AgLvBcQx6G982ur87fPZq_I29pr6WxC3WMC8x70dUQWfeqHb7hQoCnPUnkP1t2E42SWF2NsXSbIIucks2v0XmHiCnVE2SVbC5wqTgyOPyMaRd-zf1oZowKsxxpYcd5CT4zsekJ6WJH2VPUERGg6GKNhq5twI6_0LLRdyNeju7D3oBQVURusri_Sb_E0Igkzy0KIizXsoi9KxbGvqCo50LlJoCHl-p9P4bAMjHo-irVRSrp2YYJib7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش کاربر آمریکایی به تصویری که وزیر امور خارجه از پرچم ایران در کنار پرچم لبنان منتشر کرد:
برای خودت دوستی مثل ایران پیدا کن
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/657073" target="_blank">📅 01:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657072">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
ولایتی خطاب به دشمن: انتخاب با شماست توقف حماقت یا ورود به موازنه ضابطه مند شدن دو تنگه!
مشاور رهبر انقلاب:
🔹
پیش بینی چند روز قبل محقق شد؛پاسخ موشکی از جنس «ذات السلاسل».
🔹
حماقت امروز رژیم در بیروت و نقض صریح آتش بس،حلقه اول پاسخ زنجیره‌ای ما را فعال کرد.
🔹
امنیتِ امروزِ باب‌المندب،نباید دشمن را دچار خطای محاسباتی کند. حلقه‌های مقاومت توان قفل کردن هر دو آبراه را دارندانتخاب با شماست توقف حماقت یا ورود به موازنه ضابطه مند شدن دو تنگه!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/657072" target="_blank">📅 01:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657071">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
گفتگوی تلفنی وزرای امور خارجه ایران و عربستان
🔹
عباس عراقچی و فیصل بن فرحان، وزرای امور خارجه ایران و عربستان، بامداد دوشنبه در یک تماس تلفنی درباره پاسخ نیروهای مسلح ایران به نقض آتش مورخ ۱۹ فروردین و تداوم اقدامات تجاوزکارانه رژیم صهیونیستی علیه لبنان و منطقه گفت‌وگو و رایزنی کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/657071" target="_blank">📅 01:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657070">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
رایزنی های امنیتی نتانیاهو بعد از گفت‌وگوی تلفنی با ترامپ
🔹
رسانه های صهیونیستی از رایزنی های امنیتی بنیامین نتانیاهو نخست وزیر رژيم صهیونیستی بعد از گفت‌‌وگوی تلفنی با  دونالد ترامپ خبر دادند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/657070" target="_blank">📅 01:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657069">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
تماس رئیس ستاد ارتش اسرائیل با فرمانده تروریست‌های سنتکام
🔹
یک رسانه صهیونیستی از تماس تلفنی «ایال زامیر» رئیس ستاد مشترک ارتش رژیم صهیونیستی و «برد کوپر» فرمانده ستاد فرماندهی مرکزی آمریکا در خاورمیانه (سنتکام) خبر داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/657069" target="_blank">📅 01:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657068">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
اسرائیل هیوم به نقل از یک مقام امنیتی: اسرائیل احتمالا حمله ایران را فوری پاسخ نمی‌دهد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/657068" target="_blank">📅 01:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657067">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmdcbpgna3sizeURQ_m7gc_VfMILsIkvOoc08daziw1n3I4JPXL-iBxbDyrFUp0ZtxztGFGZG5Bq3xI-JMSfdufd7wBdJmGTK2FPFpkC3ZCrGmE_uTZ6nfSaxCNq6ovM4pD-sMeuHvpwCg5VXvdEOkBbqa8d9k28M_hARZHchFf6HO-4K1xNviEXaaFjkyUvSJaXLbcTE_ZeiEK0ypcGs0dqp_dFSHMgzqhQ_fMIPEJZJyfvRCpYHUhMr0Hw-ZwWhxZCCrQ-Y7lnA1TZ9qLk8dXrxvxn9fkHE3gindGEOZiJ97yKNkFDEy5dj50AVBv5WrYkXlACwgdcyJTLtmRDkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه:
‏«وَ لَیَنْصُرَنَّ اللَّهُ مَنْ یَنْصُرُهُ إِنَّ اللَّهَ لَقَوِیٌّ عَزیزٌ.»
🔹
قطعا خدا کسانى را که او را یارى مى‌دهند یارى خواهد کرد، چرا که خداوند نیرومند و شکست‌ناپذیر است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/657067" target="_blank">📅 01:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657066">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
مقام ایرانی: توافق با ترامپ در شرایط فعلی عملاً ممکن نیست/ حمله دوباره به بیروت، پاسخ فوری موشکی در پی دارد
/ انتخاب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/657066" target="_blank">📅 01:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657065">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
پست عراقچی در شبکه ایکس با تصویر پرچم‌های ایران و لبنان
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/657065" target="_blank">📅 01:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657064">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
منابع عبری: پایان تماس ترامپ و نتانیاهو
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/657064" target="_blank">📅 01:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657063">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxiJocgQHzLPSvGsPzO9Q4EwHeAWhhBf01hddU2jcJTrRB81XqWIPxF08MvMGa3bC_FM36zHMOIElXa5qMZBbI7GEbhocNQN1NxIxxdt9fPar1fcKFlUGoJdsi6vymXNYDdHMOt2MGd2DbEqCDfuSGIADEkvKq0IaxA9yo6baV4kbMdC-h9TFkL69IdZ2bm007Om7htZKwdr0ad0jCwtTcKRvVDzzF2ToE_wekm0dBsJpbYe4PcmEoWkL5vibFax3Fwqln0jdComJ8f_1zaHymOroaJxf6siTvsxNF_Sr-fWYEvz9-6wE6-huffbwwLr7SdWBZBKPvJ3F3XVnvgSvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی مجلس: شلیک‌ها از آن جایی انجام شد که ترامپ می‌گفت نابودشان کرده است
#WillPayThePrice
#هزینه_خواهید_داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/657063" target="_blank">📅 01:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657062">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
قدیری‌ابیانه: باید صهیونیست‌ها را موشک باران کنیم
قدیری‌ابیانه، فعال اصول‌گرا در
#گفتگو
با خبرفوری:
🔹
لبنانی‌ها برای کمک به ایران وارد جنگ شدند و بیش از ۳۰۰۰ شهید دادند؛ بنابراین باید به حزب‌الله کمک کرد و حتی اگر شده، صهیونیست‌ها را موشک‌باران کنیم.
🔹
وی افزود با توجه به ادامه حملات اسرائیل، پاسخ ایران نباید به تأخیر بیفتد و حمله ایران پیش‌دستانه محسوب نمی‌شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/657062" target="_blank">📅 01:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657061">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
شنیده‌شدن صدای رعدوبرق در آسمان تهران
🔹
براساس هشدار سطح زرد هواشناسی، از عصر یکشنبه تا صبح دوشنبه در برخی ساعات در تهران بارش باران، رگبار و رعدوبرق پیش‌بینی شده است.  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/657061" target="_blank">📅 01:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657060">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
سازمان حج و زیارت: هیچ‌گونه نگرانی در خصوص وضعیت زائران ایرانی در سرزمین وحی وجودندارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/657060" target="_blank">📅 01:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657059">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93d0986b0c.mp4?token=BBi15bIs844XKG5_DvjjrIvCe_UclzhGvKPwBdRcmVy1Ib0RLRr28TRw_HaZN8_LTVb5MA0hkNjCWbKD57PwsgHnxsFOUsO07aq-MN1QlPyyzJ-NwnMydlI6frl6TznoZJxJuLx2B2kyOap21JfrxD8RTAVWWDvoi9RxCH6QEosflT7qKK2j_OgMet9TMc51ZhqW7jzajvdYIaQeAyPlP8t3QtbiIwqwlRLnhSUxQtNtYPFmNbQH5rQ6uXQgPt1EBsTJskGvecE7_0ExEPKU6ztN3w-KJeeQBgfaC92z2Tqx2rQJVlV2zotHiQpqMypvBLZZkSpZuKm3HdviX77Tow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93d0986b0c.mp4?token=BBi15bIs844XKG5_DvjjrIvCe_UclzhGvKPwBdRcmVy1Ib0RLRr28TRw_HaZN8_LTVb5MA0hkNjCWbKD57PwsgHnxsFOUsO07aq-MN1QlPyyzJ-NwnMydlI6frl6TznoZJxJuLx2B2kyOap21JfrxD8RTAVWWDvoi9RxCH6QEosflT7qKK2j_OgMet9TMc51ZhqW7jzajvdYIaQeAyPlP8t3QtbiIwqwlRLnhSUxQtNtYPFmNbQH5rQ6uXQgPt1EBsTJskGvecE7_0ExEPKU6ztN3w-KJeeQBgfaC92z2Tqx2rQJVlV2zotHiQpqMypvBLZZkSpZuKm3HdviX77Tow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شنیده‌شدن صدای رعدوبرق در آسمان تهران
🔹
براساس هشدار سطح زرد هواشناسی، از عصر یکشنبه تا صبح دوشنبه در برخی ساعات در تهران بارش باران، رگبار و رعدوبرق پیش‌بینی شده است.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/657059" target="_blank">📅 01:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657058">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
کانال ۱۴ عبری به نقل از یک منبع سیاسی صهیونیست: نتانیاهو باید به بمباران ایران پاسخ دهد، حتی به قیمت رویارویی با ترامپ
🔹
متأسفانه، به نظر می‌رسد احتمال حمله قوی و مشترک امشب اسرائیل و آمریکا تقریباً وجود ندارد./ میزان
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/657058" target="_blank">📅 01:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657057">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
مقر گروهک های تروریستی در سلیمانیه عراق هدف حمله قرار گرفت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/657057" target="_blank">📅 01:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657056">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1PWLOH8rbwMe1quezcPw8MkOdYVlCfT8gZuaP7Htg-BlhTujOAXx2HB_8HIyhgMKDlVkeZQlmONs6JWkhxMxIt79a2x-7sawsgwOurN1ENOpwDOm5ochMTcXckAPuzYbesHqp6IAMPb2m4p5htThsxuZI736PTUWJ3oCR_La7AC7mnfnyq1-yFzBKuIbVRHzhTEEoDyjde6NAC2lAT3RmtYmAK5ZvkIlIriAUsX2Gc9YIFxEd6GHcGSi84IJj_I0fE7kJq_nHh06343vq7Az6KmkkTgmJ0zy3GznS2ScmzdNz135j8S68WU4HQJVIbtBSqas6rFLQad52T4Jh330Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز عملیات موشکی ایران؛ ارتش اسرائیل تایید کرد
🔹
ساعتی پیش ارتش رژیم صهیونیستی در بیانیه‌ای رسمی تأیید کرد که شلیک موشک‌ها از خاک ایران به سمت سرزمین‌های اشغالی آغاز شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/657056" target="_blank">📅 01:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657055">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
ادعای کانال ۱۲ اسرائیل: تاکنون آمریکا برای اجرای حمله علیه ایران موافقت نکرده است/ انتخاب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/657055" target="_blank">📅 01:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657054">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
عراقچی در تماس با وزرای خارجه انگلیس و ترکیه و فرمانده ارتش پاکستان، درباره تحولات منطقه پس از پاسخ ایران به اقدامات رژیم صهیونیستی گفت‌وگو کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/657054" target="_blank">📅 00:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657053">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
مقر گروهک های تروریستی در سلیمانیه عراق هدف حمله قرار گرفت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/657053" target="_blank">📅 00:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657052">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
صنعا با استقبال از پاسخ موشکی ایران: دوران عربده‌کشی رژیم صهیونیستی پایان یافته است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/657052" target="_blank">📅 00:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657051">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
کانال ۱۵ رژیم: پس از پایان گفتگوی نتانیاهو و ترامپ، نخست‌وزیر جلسه گسترده‌ای درباره موضوع ایران برگزار خواهد کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/657051" target="_blank">📅 00:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657050">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
القادر کربلایی، معاون نظامی گروه مقاوت نجبا عراق: آمریکا باید عراق را ترک کند/ سلاح‌مان را فقط امام مهدی تحویل می‌دهیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/657050" target="_blank">📅 00:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657049">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-text">🚀
تو را تنبیه کردیم حیدرانه
✨
انا علی العهدی
#امت_منتقم_و_منصور
مرجع محتوای حماسی در این کانال
👇🏻
👇🏻
@Heyate_gharar</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/657049" target="_blank">📅 00:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657048">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
یدیعوت آحرونوت: ایالات متحده پیامی به اسرائیل منتقل کرد مبنی بر اینکه بهتر است چند روز صبر کنند تا ببینند آیا امکان رسیدن به توافق وجود دارد یا خیر
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/657048" target="_blank">📅 00:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657047">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
پروازهای فرودگاه امام (ره) تا اطلاع ثانوی متوقف شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/657047" target="_blank">📅 00:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657046">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
دفتر نخست وزیری اسرائیل: نتانیاهو به زودی با ترامپ صحبت خواهد کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/657046" target="_blank">📅 00:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657045">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/684792f89c.mp4?token=FFUDTYR1wNtNzgAP6xbgTDqLQj_nt-CA59XpWFRVF0gaN6RdTO4fGio-2Rr8jq8Nf6W2Z2NhoxWa7D0TM5-D_mPda3OS6Gt7mzMqwrHsbDOatcgHNqIcnBCPsF_ZcDHPDFocy7_0jEp4dHEvcP4_OWFziYaf_1EFg1dSE6xvi2dsWFgAgAOlsho8wWMtQPnzmEBfiOHEBRmXostNBSaAvg1XnNROSZ3QRzj1YwsFkNSwlVuWfnqjAmHUot1RP7zlQ-t72Y3bhzJJan6HaFXuhcp_HVD3i8yjL2fGG-tGnFUVIXu2QxYTEecSo4_oBwtH15oDmrHIDcX4r9xvSVSm7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/684792f89c.mp4?token=FFUDTYR1wNtNzgAP6xbgTDqLQj_nt-CA59XpWFRVF0gaN6RdTO4fGio-2Rr8jq8Nf6W2Z2NhoxWa7D0TM5-D_mPda3OS6Gt7mzMqwrHsbDOatcgHNqIcnBCPsF_ZcDHPDFocy7_0jEp4dHEvcP4_OWFziYaf_1EFg1dSE6xvi2dsWFgAgAOlsho8wWMtQPnzmEBfiOHEBRmXostNBSaAvg1XnNROSZ3QRzj1YwsFkNSwlVuWfnqjAmHUot1RP7zlQ-t72Y3bhzJJan6HaFXuhcp_HVD3i8yjL2fGG-tGnFUVIXu2QxYTEecSo4_oBwtH15oDmrHIDcX4r9xvSVSm7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شادی مردم بعلبک لبنان از پاسخ ایران به تجاوز رژیم‌ صهیونیستی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/657045" target="_blank">📅 00:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657044">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVxp-fI6uvcvn1p2X1X5DeSoxCE-pIOJeye-lINpCkLAZ8ZWzsvuYxSFDYMfs9HoVz4Q6RKgMs_iq7W6bYHkY1HYfJmHw-XHcEql9bwU4EwNFn2A3Bt4EMzOExZS_OG67xqDQ8TvRiRUERnfsFVDfHiyBT-vhGZLwALtPYVMJrnT9EQ7br4U69QZx-Wcjjopxc7uoU8O5R2Yh35_e0l6fxJ6WX3aQ6WevUN2SMQDH30CLK6uuhA8M2v6SckIMqTWUVGuXaiYt5n1oS3yMjEv0QkPAxKGaBEbeopAANZAjV9Aj5sWE0TJPD4YcJ7ito-2M1k4Af1ds4nl2hIvMDdqcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیه وزارت امور خارجه درباره ضربات دفاعی ایران علیه اهداف رژیم صهیونیستی
🔹
وزارت خارجه اعلام کرد حمله نیروهای مسلح ایران به اهداف نظامی در شمال فلسطین اشغالی، در پاسخ به نقض‌های مکرر آتش‌بس و اقدامات تجاوزکارانه رژیم صهیونیستی و در چارچوب حق دفاع مشروع انجام شد.
🔹
هرگونه ماجراجویی جدید علیه ایران یا لبنان با پاسخ کوبنده و همه‌جانبه مواجه خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/657044" target="_blank">📅 00:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657043">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
سفارت آمریکا در اسرائیل به همه کارمندان دولت ایالات متحده و اعضای خانواده آنها در اسرائیل دستور داده است تا اطلاع ثانوی در محل‌های امن بمانند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/657043" target="_blank">📅 00:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657042">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
القادر کربلایی، معاون نظامی گروه مقاوت نجبا عراق: آمریکا باید عراق را ترک کند/ سلاح‌مان را فقط امام مهدی تحویل می‌دهیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/657042" target="_blank">📅 00:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657039">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2c94c65b6.mp4?token=g9tjUV7Rl-wkpbL2XHJuNhQg1WuzhPV5EvcbyX2AyTJkTqcUIM0rxXq9rb-ROejz6KeNyrdyV0llnrKHXFwvuQCN-k2RdznbGGc0hBnFT-LF39NmgZRfYA3Uclwcl1CByQGHqz4bGhpIuRLrfh19Os6X3xcP8h7__TyjWU2JcOE9kVE3AL8oVD4bXtSSDzOi7tng-xImemi6R48SbQ9G7Ke3aNowimnTgm7nZvKee9MZWc-SjXjn1jf5mARNjck3-IthTfDHrMiW1eO53x4aQcfqeYYjWUFg6p4kb6gyiAHCcrcF4wJ30jUyvHLidaC7mSIFgDENmA3cMs_dwkaC-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2c94c65b6.mp4?token=g9tjUV7Rl-wkpbL2XHJuNhQg1WuzhPV5EvcbyX2AyTJkTqcUIM0rxXq9rb-ROejz6KeNyrdyV0llnrKHXFwvuQCN-k2RdznbGGc0hBnFT-LF39NmgZRfYA3Uclwcl1CByQGHqz4bGhpIuRLrfh19Os6X3xcP8h7__TyjWU2JcOE9kVE3AL8oVD4bXtSSDzOi7tng-xImemi6R48SbQ9G7Ke3aNowimnTgm7nZvKee9MZWc-SjXjn1jf5mARNjck3-IthTfDHrMiW1eO53x4aQcfqeYYjWUFg6p4kb6gyiAHCcrcF4wJ30jUyvHLidaC7mSIFgDENmA3cMs_dwkaC-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امشب پهپادها با شعار «لبنان را رها نمی‌کنیم» راهی اراضی اشغالی شدند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/657039" target="_blank">📅 00:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657038">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1df242f4b0.mp4?token=Y1t2X65f2ZC7gn_ZXP7ofZglaZ-ZabjkFqkXEkjlyeAEIhFJJTZewrn3Llh1g-ZpbxlfPZi7TOOEfmxGCwC6ORIL_EPPkx7xs4qw7B_V5Dm2efMhZH8IEB-8KvJc_QR-1w1B_-f9xNjc-pgbrZSqm5bfPw5xz-OK6sEVdpvzteRxIH1gCc4d5i9iHSBTjf6Z6fJLGUZGQwS0ZANQ2sMpfAwHSorGoUdxtk5eGtHPXc-3UJbCjmDZRGMN9dK0pYJ9wh8oOA2xYY0wcvzQuty59BApx-BAN_LMo6BJ91FvvT10jSFs5O42K8mKaOmBwZ45jnpT5-wH4yHeGOIY7P_cxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1df242f4b0.mp4?token=Y1t2X65f2ZC7gn_ZXP7ofZglaZ-ZabjkFqkXEkjlyeAEIhFJJTZewrn3Llh1g-ZpbxlfPZi7TOOEfmxGCwC6ORIL_EPPkx7xs4qw7B_V5Dm2efMhZH8IEB-8KvJc_QR-1w1B_-f9xNjc-pgbrZSqm5bfPw5xz-OK6sEVdpvzteRxIH1gCc4d5i9iHSBTjf6Z6fJLGUZGQwS0ZANQ2sMpfAwHSorGoUdxtk5eGtHPXc-3UJbCjmDZRGMN9dK0pYJ9wh8oOA2xYY0wcvzQuty59BApx-BAN_LMo6BJ91FvvT10jSFs5O42K8mKaOmBwZ45jnpT5-wH4yHeGOIY7P_cxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
در روزهایی که خبرها دل‌ها را نگران می‌کند و چشم‌ها پیگیر حوادث است، خداوند در سوره‌ی محمد(ص) سخنی دارد که برای چنین روزهایی نازل شده است:
▫️
«وَلَا تَهِنُوا وَلَا تَدْعُوا إِلَى السَّلْمِ وَأَنْتُمُ الْأَعْلَوْنَ وَاللَّهُ مَعَكُمْ»
▫️
سست نشوید، خود را نبازید و بدانید که اگر در مسیر حق بایستید، خدا با شماست.
▫️
سوره‌ی محمد، سوره‌ی استقامت است؛
سوره‌ی آرامش در میانه‌ی اضطراب،
سوره‌ی امید در هنگامه‌ی تهدید،
و سوره‌ی یادآوری این حقیقت که پیروزی پیش از آنکه در میدان‌ها رقم بخورد، در دل‌ها آغاز می‌شود.
▫️
امشب برای قوت قلب، برای آرامش خانواده‌ها، برای رزمندگان اسلام و برای پیروزی جبهه‌ی حق، سوره‌ی محمد(ص) را با تدبر بخوانیم.
📖
سوره‌ی محمد؛ سوره‌ی ایستادگی مؤمن
مرجع محتوای حماسی در این کانال
👇🏻
👇🏻
@Heyate_gharar
@Heyate_gharar</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/657038" target="_blank">📅 00:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657037">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
ادعای آمیکای اشتاین خبرنگار آی ۲۴ رژیم صهیونیستی: «در طول یک ساعت آینده، یک بحث گسترده با حضور بنیامین نتانیاهو، وزیر جنگ، و فرماندهی عالی امنیتی درباره ایران آغاز خواهد شد.»/انتخاب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/657037" target="_blank">📅 00:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657036">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adf12cfa85.mp4?token=eDB7jZ30vijKSrqQpaFh8lD0UGcqPl992vZ6_B0Naf4WrPPURE-ZZBlrKVWV6e6cy1K1KV0lv1oIQ-nmLxAghncueZsSWrwX0CyP5Tuz4X24se1PEN-x-tVsZ4tW_AtKG6w6tjZFE64jgHPeFi-P4yNUUo4tlkWnDbbusLqwAkk9muiftUtFsB3oXIDIJLn2wfubTS26n9RwwLVjY7R_Au_b_psdu4D0kmIBvI5RsjiKaz0vzHpkEFVgOfTqNkAeIwQoucS0ja4iqINHKxmsaQ3J1sMlnqt_lbJdSYW5K_JUokiWw9bt2oqV2da4t3huDdUVsZJneeyTegUDZIq-sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adf12cfa85.mp4?token=eDB7jZ30vijKSrqQpaFh8lD0UGcqPl992vZ6_B0Naf4WrPPURE-ZZBlrKVWV6e6cy1K1KV0lv1oIQ-nmLxAghncueZsSWrwX0CyP5Tuz4X24se1PEN-x-tVsZ4tW_AtKG6w6tjZFE64jgHPeFi-P4yNUUo4tlkWnDbbusLqwAkk9muiftUtFsB3oXIDIJLn2wfubTS26n9RwwLVjY7R_Au_b_psdu4D0kmIBvI5RsjiKaz0vzHpkEFVgOfTqNkAeIwQoucS0ja4iqINHKxmsaQ3J1sMlnqt_lbJdSYW5K_JUokiWw9bt2oqV2da4t3huDdUVsZJneeyTegUDZIq-sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شبکه تی آر تی ترکیه با توقف برنامه های خود به خبر حمله موشکی ایران به سرزمین های اشغالی پرداخت
فَإِنْ قاتَلُوكُمْ فَاقْتُلُوهُمْ كَذلِكَ جَزاءُ الْكافِرِينَ
🔹
پس اگر با شما جنگیدند، آنان را بکُشید؛ که سزای کافران همین است.
🔹
بقره ـ ۱۹۱
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/657036" target="_blank">📅 00:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657035">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
تکذیب حمله به فرودگاه تبریز ‌
🔹
براساس پیگیری‌ها، صدای شنیده شده در‌فرودگاه تبریز تست پدافند بوده و هیچ‌گونه حمله‌ای به این فرودگاه اتفاق نیفتاده است. ‌
🔹
دقایقی پیش اخباری در برخی کانال‌های تلگرامی مبنی بر شنیده شدن صدای انفجار در فرودگاه تبریز منتشر شده…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/657035" target="_blank">📅 00:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657034">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
حمله هوایی اسرائیل به شهر زیفتا در شهرستان نبطیه در جنوب لبنان
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/657034" target="_blank">📅 00:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657033">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">و ما النصر</div>
  <div class="tg-doc-extra">حاج محسن طاهرى،كربلايى محمد مهدى طاهرى</div>
</div>
<a href="https://t.me/akhbarefori/657033" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/657033" target="_blank">📅 00:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657032">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
وزارت خارجه یمن: پاسخ ایران معادله وحدت میادین را تحکیم می‌کند. محور جهاد و مقاومت برای مقابله با هر تحولی در هماهنگی مستمر هستند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/657032" target="_blank">📅 00:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657031">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7a7d5f654.mp4?token=M3KIcA4Z_LZHEsXocKlZ6qhV-lWXCNyIOkbH9Y0BQblQKNzngKAb-Cuqo6VNJNrEhXnegW9mvl4sqF5u6mAJSFIaYRPYRDyXDUniLyt_Bl6n0BB6Z0tYDUvBeJMaoDX6tJxILrZSd8wWPc2FgezL1RQoCxyxsLUUBJRFZ35zeZvVF45xizXVrWWVTEw4Yh-NzTJDC2nM34Jcgreg3eethJyoOK-6meHsd-QssfuOrUCn0SENHbWaH_H7ZvbSwhZssrAbmZY2vU0c9YmQyJwjhcfrmIsEmYTqyP5Easz7X84InkiSbxQmkCTqTd3Xk3zUcq82XY-K4Q772Mf3fTQXKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7a7d5f654.mp4?token=M3KIcA4Z_LZHEsXocKlZ6qhV-lWXCNyIOkbH9Y0BQblQKNzngKAb-Cuqo6VNJNrEhXnegW9mvl4sqF5u6mAJSFIaYRPYRDyXDUniLyt_Bl6n0BB6Z0tYDUvBeJMaoDX6tJxILrZSd8wWPc2FgezL1RQoCxyxsLUUBJRFZ35zeZvVF45xizXVrWWVTEw4Yh-NzTJDC2nM34Jcgreg3eethJyoOK-6meHsd-QssfuOrUCn0SENHbWaH_H7ZvbSwhZssrAbmZY2vU0c9YmQyJwjhcfrmIsEmYTqyP5Easz7X84InkiSbxQmkCTqTd3Xk3zUcq82XY-K4Q772Mf3fTQXKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چهره وحشت‌زده خبرنگار صهیونیست اینترنشنال در پی حملات موشکی ایران؛ اسرائیل فکرش را هم نمی‌کرد که ایران پاسخ بدهد!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/657031" target="_blank">📅 00:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657029">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
سخنگوی قوه قضاییه: دشمن با میلیون‌ها جانفدا روبه‌رو شده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/657029" target="_blank">📅 00:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657028">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vuw7V7PUYD7tIVp54SMh7XBQ4Mr6RCkMGv5LapJ_GB1Oy8gEGSEqMS0N-FrC0xqDhXkoNHzbEazDO0hIrzEvH710X0daqHsxD75Hwkim55Q9EuF9S-v7u83h2CtpjJ2aVyElkO0_79cEKgzKDz7C1T4NBI1iDYEAC-PLbrkYk2BUUsSbXczRxLglB4rdRNLtvBFaHETz7Day79xuTIl10BfjFgpCf3de8FimT_2IHzOmkDb_kDr4BmaFpGpaK7f1ziLjFfCZIuTmicjsSqB0A_QinCUyNHga8vRSwcrdGs-_6v2ByuGHCT2XVh-qz3Hh382pXs5L-ltK0dgbDuN3Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفارت ایران در بیروت: همیشه در کنار شماهستیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/657028" target="_blank">📅 00:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657027">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
یک منبع نظامی: موشک‌های ایران آماده‌اند در صورت پاسخ اسرائیل فوراً شلیک شوند
🔹
اگر اسراییل پاسخ دهد، نوبت بعدی شلیک‌های ایران، پرحجم‌تر خواهد بود.
🔹
این منبع نظامی خاطرنشان کرد: ایران برای آغاز نبرد گسترده در صورت پاسخ صهیونیستها آماده است و صهیونیستها باید این هشدار را به گوش بسپارند. / تسنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/657027" target="_blank">📅 00:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657026">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
کمیته‌های مقاومت فلسطین ضمن قدردانی از پاسخ ایران به رژیم صهیونیستی، اعلام کردند این اقدام معادلات جدیدی ایجاد کرده و بار دیگر معادله جبهه‌های متحد را تثبیت کرده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/657026" target="_blank">📅 00:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657025">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
نامه ویژه پاکستان به رهبر انقلاب تحویل عراقچی شد /تسنیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/657025" target="_blank">📅 00:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657024">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40efaad5ad.mp4?token=Is3jxN_QZQw8JgmGFi3fOrAR8WDyFWzESzgxeTgkDROU9pVZpxzwun717aNuClMNOv-yeOSN1tKGBsp694uIFI630rknwhRoXMM8vGFuRopckYTwJbv8-1SPaD6zZ1-PnBE6XB0rdNcabnwSKqkPX8t1TXMGhLAqRH7kLmL0sR9LDxnV2wVlJUVL4vmxc446SllAu7ZN5PTSl0cw7bMzmID9AxZ2Y1cMFcI2gxsMIszWYMGO_6fCe_xsa4vpgVyTQwnW4uOoXTARpvwG2xiGooTGYOVjCleVPOGE5NISh3Kwk_5i1yD5zdRXyrGQOGK6VM1JA-TF-RLdjn2y75jfeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40efaad5ad.mp4?token=Is3jxN_QZQw8JgmGFi3fOrAR8WDyFWzESzgxeTgkDROU9pVZpxzwun717aNuClMNOv-yeOSN1tKGBsp694uIFI630rknwhRoXMM8vGFuRopckYTwJbv8-1SPaD6zZ1-PnBE6XB0rdNcabnwSKqkPX8t1TXMGhLAqRH7kLmL0sR9LDxnV2wVlJUVL4vmxc446SllAu7ZN5PTSl0cw7bMzmID9AxZ2Y1cMFcI2gxsMIszWYMGO_6fCe_xsa4vpgVyTQwnW4uOoXTARpvwG2xiGooTGYOVjCleVPOGE5NISh3Kwk_5i1yD5zdRXyrGQOGK6VM1JA-TF-RLdjn2y75jfeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استاندار کربلا: جسم ساقط شده در صحرای کربلا پهپاد است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/657024" target="_blank">📅 00:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657023">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
تکذیب حمله به فرودگاه تبریز
‌
🔹
براساس پیگیری‌ها، صدای شنیده شده در‌فرودگاه تبریز تست پدافند بوده و هیچ‌گونه حمله‌ای به این فرودگاه اتفاق نیفتاده است.
‌
🔹
دقایقی پیش اخباری در برخی کانال‌های تلگرامی مبنی بر شنیده شدن صدای انفجار در فرودگاه تبریز منتشر شده بود./ تسنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/657023" target="_blank">📅 00:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657022">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMbDnwun9E2SFJ13943BbSRA6t1oDBvvhYYO6gTkYy4-jxqnC23jQbxZYSKqfaBTzAWdxx_STCE1RecAJ_5LsnIsuI6katpBMzXyAeZKGxTbQ82TfH41jQaYWHyi6RmSpE-pRqzm9dT_XFRan_oadPhNZqiAci_UZTdDhqYxcWOHh0YBK6Vti49pmCFo2aPq5Ae0dFXXmjcUZBT7H8IKQFpskBoCgUZxvKJmWoEuL6C_jKNzw7rxjmk6e40425XcaghQHfuFrY3K4BarcEpJVwkKxOtpiI70eyMwAjq79h7fvh0NO5OaoyjQRsZzZ1VBbvzYHy1EqVZmVoAcX2QZRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
در این زمان که امیدی به سازوکار جهان نیست
پناه کشور ایران به جز امام زمان(عج) نیست
✨
دوباره بازی‌شان را به‌هم زدیم بفهمند
که شیعه‌خانهٔ مهدی، زمین بازی‌شان نیست
مرجع محتوای حماسی در این کانال
👇🏻
👇🏻
@Heyate_gharar</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/657022" target="_blank">📅 00:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657021">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vh7f4MATNV3AclPakwePhOC4UgTYHeyAOc75Cvj4-5yq9pDYBn_9nr4CACiB7ILAcYbV-dAzHLbMRw3X-BT2BZk6F437knCTJjEgdOM1ehN5UMSclhvM-umzXeKebj9j8L200_NZZBhbDd7rX9WOrA-k6QOJqh5CK6BcY_3Df4NW0wWMD6gLfR5mzKrZGgyf8UvtjLfhVN3T2eXJet0fxYu8kxFfTAcIrn2Ae3PGqEotKJtNGMfCNfoJ62Yqf_-L0gpvXLACBI9tdqlOGp-cM1SF5073rQyKEU_pfWdLwewXvwxvqCQVZV2wFggYAvsETfsoy2BAEXoVZl1ENzR36A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نماینده رهبر انقلاب در شورای دفاع: صدای خروش ملت ایران را در آسمان تل‌آویو بشنوید/‏ادامه مسیر فشار و تهدید، پاسخی قاطع‌تر و کوبنده‌تر در پی خواهد داشت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/657021" target="_blank">📅 00:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657020">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
یک منبع ایرانی: هشدارها درباره نقض آتش‌بس را عملی کردیم
🔹
ایران بارها تأکید کرده است که دوستان خود در لبنان را تنها نخواهد گذاشت؛ این تعهدی است که از آن عقب‌نشینی نخواهیم کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/657020" target="_blank">📅 00:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657019">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cd77c7956.mp4?token=A47tDTt5Wz-Yzpqi2Ff_EtGH9wQzXlJzsml0ZF9nx-vY3haqPZOza6joVQyOtNyaCl0WLDJki9JSoLELaO1Rc1rt2bStn9EC85VqKWCJ9mqcFEdNuxfKvB22B9f0hg59nTUUeGTZ5krfRwgYvaTjj7STmCmB_sn6ZSpo5Dc90cUwonZ9su-aW6VKK4f935EisxhRv8NsknirDpDoUGbWqIoKwGrSk3IyAlJiRFQj8NYrexw15QT7-iTJ6oEPyi_vJbExBW7fvSLbvbj7WDMn4Vj159ZsZ4dDHeTFPhfIdMjFErF4X2U24_JfxN63Di1RIsuf3BoI9cdykTRoSzQwBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cd77c7956.mp4?token=A47tDTt5Wz-Yzpqi2Ff_EtGH9wQzXlJzsml0ZF9nx-vY3haqPZOza6joVQyOtNyaCl0WLDJki9JSoLELaO1Rc1rt2bStn9EC85VqKWCJ9mqcFEdNuxfKvB22B9f0hg59nTUUeGTZ5krfRwgYvaTjj7STmCmB_sn6ZSpo5Dc90cUwonZ9su-aW6VKK4f935EisxhRv8NsknirDpDoUGbWqIoKwGrSk3IyAlJiRFQj8NYrexw15QT7-iTJ6oEPyi_vJbExBW7fvSLbvbj7WDMn4Vj159ZsZ4dDHeTFPhfIdMjFErF4X2U24_JfxN63Di1RIsuf3BoI9cdykTRoSzQwBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جزئیات و اهداف حملات امشب ایران به سرزمین‌های اشغالی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/657019" target="_blank">📅 00:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657018">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
ترامپ افسار نتانیاهو را کشید
🔹
با نتانیاهو تماس خواهم گرفت و به او خواهم گفت که به ایران پاسخ ندهد #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/657018" target="_blank">📅 00:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657017">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/162802ccab.mp4?token=ZuSW95r3dtfCT3gBUkWtVS_EnC0365ofHWI1gPQxeKX-MBy5TA9aegvZB0zsoBrzwOqpokiUVCdV6pD9avmz1X_ZyFXViUkdj_N2ZY8lp3USwNZ_o71Q1ZxM8Xg51I20aQX5sqU6xTddk_FxX79qVPA_d4dDjRDnYrXfKZWf14zT11YqoFtY_CtfliSYYpVM-gyzeMMMu8e39yW3YnwItYGA5fn1-KjndqCsddQzFkPfG_THTcQoyRxJWEmZus_U3SHdZyA67gl-8r8gtQujB0RpxbwDv3lS5-M8uo0F-gC--DEJ1R-sIa4VndbjAYkJQKVe2n7RipZ8ERw2Dij48w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/162802ccab.mp4?token=ZuSW95r3dtfCT3gBUkWtVS_EnC0365ofHWI1gPQxeKX-MBy5TA9aegvZB0zsoBrzwOqpokiUVCdV6pD9avmz1X_ZyFXViUkdj_N2ZY8lp3USwNZ_o71Q1ZxM8Xg51I20aQX5sqU6xTddk_FxX79qVPA_d4dDjRDnYrXfKZWf14zT11YqoFtY_CtfliSYYpVM-gyzeMMMu8e39yW3YnwItYGA5fn1-KjndqCsddQzFkPfG_THTcQoyRxJWEmZus_U3SHdZyA67gl-8r8gtQujB0RpxbwDv3lS5-M8uo0F-gC--DEJ1R-sIa4VndbjAYkJQKVe2n7RipZ8ERw2Dij48w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر واضحی از لحظه اصابت موشک ایران به هدف خود در فلسطین اشغالی  وَلَا تَهِنُوا وَلَا تَحْزَنُوا وَأَنتُمُ الْأَعْلَوْنَ إِن كُنتُم مُّؤْمِنِينَ
🔹
سست نشوید و اندوهگین نباشید؛ شما برترید اگر ایمان داشته باشید.
🔹
سوره آل عمران، آیه ۱۳۹
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/657017" target="_blank">📅 00:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657016">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKKgl3WLHlunI_60jlnCn9VUzxONO7lO7jnANKlN9qxsRd74CIsBcIuOxfQgSnXOQ4W7GB4VoN92xxqF7Qo8UCeixjFAT9bVdgXi3BfHSMu-Ntz6ft1QRqnTgTfhFGlL96RsdF3AcaZJbmuKXXBVlpSeDPrTRPZiUg5OpisV-MXMtnBRH8JHS7TpxjlJKy1exvoMpiexvYQSBU9Sq2N4SinOvnx8POR5fwl7tpzVNilczhXfwEe3K0UfpO3u1Fkhuuc5z1u5xEenbc16KVMlAPy3vBldHUqnc6AjvvXDtJ4-wchyP6gAew4vHS6eUY-jRfu12FlBwKZEjGM2MjS62Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
עוקבים אחריך, אל תטעו.
تحت نظری، اشتباه نکن
#WillPayThePrice
#هزینه_خواهید_داد
توییتر خبرفوری را دنبال کنید
👇🏻
https://x.com/Akhbare_Fori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/657016" target="_blank">📅 00:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657015">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نماهنگ ایران خداقوت</div>
  <div class="tg-doc-extra">مهدی رسولی و محمد اسداللهی قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/657015" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✨
خیابان خدا قوت
میدان خدا قوت
جمهوری اسلامی ایران خدا قوت
ایران خدا قوت ایران خدا قوت
اینجا فقط ما به خدا میگیم ابرقدرت
🎙
#مهدی_رسولی
🎙
#محمد_اسداللهی
مرجع رسمی مداحی
👇🏻
👇🏻
@gharar_madahi</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/657015" target="_blank">📅 00:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657014">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
ترامپ به شبکه کان:ما می‌توانیم پس از ۳۰۰۰ سال به صلح دست یابیم
🔹
«فکر می‌کنم اسرائیل به اندازه کافی پاسخ داده است. دیگر نیازی به هیچ اقدامی نیست. #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/657014" target="_blank">📅 00:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657013">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
منابع عراقی: نیروهای امنیتی در عراق هشدار جدیدی در نزدیکی منطقه سبز و فرودگاه بغداد اعلام کردند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/657013" target="_blank">📅 00:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657012">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
پدافند در بخش محدودی از غرب تهران فعال شد. این اقدام به منظور افزایش امنیت و آمادگی در برابر تهدیدات احتمالی انجام شده است
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/657012" target="_blank">📅 00:08 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
