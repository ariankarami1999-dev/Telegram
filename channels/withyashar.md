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
<img src="https://cdn4.telesco.pe/file/m6FbA8ifwlRRa5Zx9CVjJsLbwE8CKWrQvkRHjOzAct5NTYKwVKqpje030MpqtmxgmibQP7x7pyeCaHhnQBEnjXIU1gOvSaAtd5y3vqrEAAonw5vg6YfvyxZ7pA2UOfmYvpk0GwodTQvBiJKwmlwNGbLBRcZjI0wlYlIh3HoJsJ3_sGvh3k76MmZvE4A8vRknE647BFi6djNdtyHs7cn_SRbN9BOSV5QprlZnPxMDmOZ0XZ-9r2VnqTB5DyNb1igRCE_3oPiOD5lYhrTbX60FvSTA7_KAEXUO2MapvIGYcqCAIDlmHAcQbah2D5O3MUXR03ZXQA2FlB_ImRjCrJroYg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 269K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-01 19:15:28</div>
<hr>

<div class="tg-post" id="msg-11959">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/withyashar/11959" target="_blank">📅 17:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11958">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/609141a267.mp4?token=p9P4xJo2HQMgxWeSf9SOeR_PvETKzSbaJe5itV3wKNvgimah25i-KNIfO8L-W8iYA-iWOyXkQVBCDrUmq33O5qCa3KHWVfsMEospxrRjN1NezcU3Jj96zgPB53_3NGFXoyvlu3WDUv9g1CmRfV9IYcV6O5QqUn7yw0o0B7EFKZgiNwifHkKq-J98uxIZLLVu-uBxcOhohK3LzLPMogDZ5osFQqH4r8G31EXylPU3yffVUvYcWjqu28dFBXioc3iTEcA0-UNi2WeZ45kKfmofH2nwbt_d5SBbYJlmz5HMhlZmkxAWSXEaTRkOsRSQLiGoSjJhGNQor50nW-qZRiyXDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/609141a267.mp4?token=p9P4xJo2HQMgxWeSf9SOeR_PvETKzSbaJe5itV3wKNvgimah25i-KNIfO8L-W8iYA-iWOyXkQVBCDrUmq33O5qCa3KHWVfsMEospxrRjN1NezcU3Jj96zgPB53_3NGFXoyvlu3WDUv9g1CmRfV9IYcV6O5QqUn7yw0o0B7EFKZgiNwifHkKq-J98uxIZLLVu-uBxcOhohK3LzLPMogDZ5osFQqH4r8G31EXylPU3yffVUvYcWjqu28dFBXioc3iTEcA0-UNi2WeZ45kKfmofH2nwbt_d5SBbYJlmz5HMhlZmkxAWSXEaTRkOsRSQLiGoSjJhGNQor50nW-qZRiyXDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/withyashar/11958" target="_blank">📅 17:01 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11957">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">امشب مراسم دعای سرخپوستی در اتاق جنگ برگزار میکنیم
💨
😬
😂
🙌🏾</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/withyashar/11957" target="_blank">📅 16:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11956">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">الجزیره: شهباز شریف، نخست‌وزیر پاکستان، قصد دارد فردا به چین سفر کند. برداشت این است که او پیام‌هایی را از تهران به پکن می‌برد.
پاکستان در حال تعامل با بازیگران متعددی است: آمریکا، ایران، کشورهای منطقه و البته چین.
@withyashar</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/withyashar/11956" target="_blank">📅 16:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11955">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">رویترز به نقل از منابع آگاه:
قطر با هماهنگی آمریکا تیم مذاکره کننده‌ای رو برای کمک به دستیابی به توافق برای پایان جنگ با ایران به تهران اعزام کرده.
@withyashar
این هیئت دقایقی پیش به تهران رسید</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/withyashar/11955" target="_blank">📅 16:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11954">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مارک لوین تحلیلگر و از نزدیکان ترامپ :
"زمان نابودی رژیم ایران فرا رسیده است. بیایید کار را تمام کنیم.
بگذارید کار را به انجام رسانیم.
تیک‌تاک ساعت را می‌شنوید."
@withyashar</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/withyashar/11954" target="_blank">📅 16:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11953">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/withyashar/11953" target="_blank">📅 16:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11952">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">وال استریت ژورنال: ترامپ درحال بررسی امکان تکیه بر گروه‌های مخالف مسلح ایرانی، از جمله جناح‌های کرد، در صورت اقدام مسلحانه اونا برعلیه دولت تهرانه.
@withyashar</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/withyashar/11952" target="_blank">📅 16:40 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11951">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/withyashar/11951" target="_blank">📅 16:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11950">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">یجور دایرکت میدید که انگار من این چند ماه قصه حسین کرد شبستری تعریف میکدم !!!
🤬
بد میگین عصبی‌نشو</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/withyashar/11950" target="_blank">📅 16:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11949">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ادعای الحدث: عاصم منیر، فرمانده ارتش پاکستان در راه تهران است. @withyashar</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/withyashar/11949" target="_blank">📅 16:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11948">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">خضریان، عضو کمیسیون امنیت ملی مجلس: جمهوری اسلامی در خصوص خروج اورانیوم از ایران هیچ مصالحه‌ای انجام نخواهد داد
@withyashar</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/withyashar/11948" target="_blank">📅 15:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11947">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ادعای الحدث: عاصم منیر، فرمانده ارتش پاکستان در راه تهران است.
@withyashar</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/withyashar/11947" target="_blank">📅 15:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11946">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تلویزیون منو‌تو : به اطلاع مخاطبان گرامی می‌رسانیم که پس از مدت‌ها تامل و ارزیابی، سرانجام به این تصمیم دشوار رسیده‌ایم که به پخش برنامه‌های منوتو پایان دهیم. آخرین پخش ما از ماهواره و یوتیوب، شامگاه ۲۴ مه ۲۰۲۶ (۳ خرداد ۱۴۰۵) خواهد بود.
@withyashar
🥲</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/withyashar/11946" target="_blank">📅 15:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11945">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بقائی: مرحله بعدی جنگ، قابل کنترل نیست / آمریکایی‌ها در حال ارسال سلاح به منطقه هستند
@withyashar</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/withyashar/11945" target="_blank">📅 15:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11944">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Sonnat Shekan (t.me/withyashar)</div>
  <div class="tg-doc-extra">Pishro (instagram.com/yashar)</div>
</div>
<a href="https://t.me/withyashar/11944" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
@withyashar
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/withyashar/11944" target="_blank">📅 15:25 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11943">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmirAli</strong></div>
<div class="tg-text">یاشار میدونی
تو همیشه خط شکن بودی
اون زمان که کسی رپ رو نمیشناخت و همه اش ریسک بود
تو رپفا رو اوردی، که خود من سالها ازش استفاده میکردم
الانم کانالت، نحوه جدید و درست برخورد با اخبار و تحلیل های سیاسی رو داره میده که برای امروز خوبه و مخاطب بدون ترس و تردید میتونه دنبالت کنه
واقعا کار درست، خوش فکر و درجه یکی
و این یکی برای تو فقط زحمت هست ولی مثل همیشه پای کار هستی</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/withyashar/11943" target="_blank">📅 15:24 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11942">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">فاکس نیوز: مذاکرات بین ایالات متحده و ایران همچنان در جریان است، با نشانه‌هایی از خوش‌بینی محتاطانه که هر دو طرف ممکن است در نهایت به توافق برسند
@withyashar</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/withyashar/11942" target="_blank">📅 15:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11941">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">poshte-pardehaye-enghelab (@withyashar).pdf</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/withyashar/11941" target="_blank">📅 15:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11940">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">عمو ترامپ در‌ تروث : رکورد جدید بازار سهام!
@withyashar
یاشار : عمو باز ببین اگه کمه ما گلریزون میکنیم بقیشو ولی ‌زودتر بزن
😂</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/withyashar/11940" target="_blank">📅 15:01 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11939">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">طبق روال هر روز حمله هوایی اسرائیل به جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/withyashar/11939" target="_blank">📅 14:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11938">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">@withyashar
روشن فکران</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/withyashar/11938" target="_blank">📅 14:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11937">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اتحادیه اروپا: به دلیل بسته ماندن تنگه هرمز، تحریم‌های جدیدی علیه ایران وضع کرديم.
@withyashar</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/withyashar/11937" target="_blank">📅 14:01 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11936">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">العربیه: بر اساس ارزیابی ایالات متحده، حدود ۱۰۰ افسر از نیروهای سپاه پاسداران انقلاب اسلامی در ماه‌های اخیر به لبنان رسیده‌اند و در حال تسلیح و آموزش فعال نیروهای حزب‌الله هستند.
@withyashar</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/withyashar/11936" target="_blank">📅 14:00 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11935">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">طبق گزارش العربیه با استناد به یک منبع پاکستانی :   اسلام‌آباد به شدت رو چین برای کمک به پیشبرد یک توافق احتمالی بین ایالات متحده و ایران حساب می‌کنه و انتظار میره شهباز شریف، نخست‌وزیر پاکستان، تو مرحله‌‌ی بعدی به چین سفر کنه
@withyashar</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/withyashar/11935" target="_blank">📅 13:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11934">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EDMCRuoiCUr-KmPT9Rod4ZTIiiGXB-mmWnQkxp1qo8U8XvP1E7mGn9uK35jXnPHso04qwrRFFEdF1QMskNTnSOZ12y8S_ZJClBZxDuDlv359EdObK7Hs2ADUkLiH6ZYVBYaxTAUm4sIBE_NWZOBLd-hHceeNJpuPkAQaEMayhWPwJfEnhdaVLXvRUw2ov2KQmBMF8GaJU6_F83Aqp4BzqEmWoIJGkZ8210yZv1J44rntzVVSc-9lJq3QjS6cCKtGFHrMSaWiKNIdouexAFkKErlh_RybMGhVmMhacgCWVmeb-VSM8lMPfNVdmzHSIP96VcrY2UU1fM2qcOhyKlHjhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ماهواره‌ای که امروز ثبت شده‌اند، آنچه به نظر می‌رسد بیش از یک دوجین هواپیمای سوخت‌رسان در محوطهٔ پایگاه هوایی شاهزاده سلطان را نشان می‌دهد، همچنین چندین هواپیمای شناسایی E-3 سنتری و دست‌کم ۲۰ جنگنده، به‌همراه چندین هواپیمای سوخت‌رسان که در وضعیت آمادهٔ برخاست هستند.
واشنگتن در حالی که دیپلمات‌ها در حال مذاکره هستند، ماشین جنگی خود را در وضعیت آماده شلیک نگه داشته است.
@withyashar</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/withyashar/11934" target="_blank">📅 13:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11933">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">کانال ۱۲ اسرائیل : بر اساس گزارش، پیش‌نویس توافق‌نامه در مجموع شامل ۹ ماده است
از جمله توقف عملیات نظامی و جنگ رسانه‌ای بین کشورها، احترام به حاکمیت و خودداری از دخالت در امور داخلی و همچنین رعایت قوانین بین‌المللی و منشور سازمان ملل.
@withyashar</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/withyashar/11933" target="_blank">📅 13:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11932">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">امروز ۲۲ می (۱ خرداد) روز جهانی پیتزای بیت‌کوین است . این روز به یادبود اولین تراکنش واقعی برای خرید یک کالای فیزیکی با بیت‌کوین در سال ۲۰۱۰ نام‌گذاری شده است که در آن کاربری به نام لازلو هانیچ (Laszlo Hanyecz) دو پیتزا را در ازای ۱۰,۰۰۰ بیت‌کوین خریداری کرد.
@withyashar</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/withyashar/11932" target="_blank">📅 12:28 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11931">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">وزیر امور خارجه آلمان: ما در حال آماده شدن برای مشارکت در تأمین امنیت تنگه هرمز تحت رهبری بریتانیا هستیم، اما انتظار ماموریتی مشابه ناتو را ندارم
@withyashar</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/withyashar/11931" target="_blank">📅 12:07 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11930">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">وال استریت ژورنال:  میلیاردها دلار از طریق پلتفرم بایننس به شبکه‌هایی که نظام ایران را تامین مالی می‌کنند، جریان یافته است بابک زنجانی شخص مسئول ایرانی در معاملات از طریق پلتفرم بایننس است @withyashar</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/withyashar/11930" target="_blank">📅 11:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11929">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">رسانه‌های داخلی ایران تصاویری منتشر کرده‌اند که نشان می‌دهد نیروهای سپاه به غیرنظامیان و کودکان آموزش باز و بسته کردن سلاح می‌دهند. خبرگزاری «آسوشیتدپرس» نیز گزارش داده نیروهای سپاه به‌طور منظم نحوه استفاده از تفنگ‌های تهاجمی مانند کلاشینکف به غیرنظامیان آموزش می‌دهند. پایتخت ایران همچنین شاهد رژه خودروهای نظامی مجهز به مسلسل‌های قدیمی ساخت شوروی است.
@withyashar</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/withyashar/11929" target="_blank">📅 11:38 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11928">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بلومبرگ : پوتین می‌خواهد جنگ اوکراین را تا پایان امسال به پایان برساند، اما فقط با شرایطی که روسیه بتواند آن‌ها را به عنوان پیروزی معرفی کند.
این شرایط شامل کنترل کامل منطقه دونباس و تضمین‌های امنیتی گسترده‌تر از اروپا است که به طور موثر کسب‌های ارضی روسیه در اوکراین را به رسمیت می‌شناسد.
@withyashar</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/withyashar/11928" target="_blank">📅 11:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11927">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سنتکام:
ناو هواپیمابر آبراهام لینکلن در بالاترین سطح آمادگی عملیاتی قرار دارد
@withyashar</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/withyashar/11927" target="_blank">📅 11:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11926">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سخنگوی کمیسیون امنیت ملی: موشک‌ها را برای مذاکره با شیطان بفرستید.
@withyashar</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/withyashar/11926" target="_blank">📅 11:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11925">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامپ فروش ۱۴ میلیارد دلار سلاح به تایوان را متوقف کرده تا مهمات آمریکا برای جنگ با ایران حفظ شود؛ به‌گفتهِ هانگ کائو، سرپرست وزارت نیروی دریایی آمریکا.
او به سناتورها گفت: “در حال حاضر ما این فروش را متوقف کرده‌ایم تا مطمئن شویم مهماتی که برای عملیات اِپیک فیوری لازم داریم در اختیارمان باشد.” کائو اضافه کرد که آمریکا همچنان “به‌قدرِ کافی” سلاح در اختیار دارد.
@withyashar</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/withyashar/11925" target="_blank">📅 11:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11924">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">وال استریت ژورنال:
میلیاردها دلار از طریق پلتفرم بایننس به شبکه‌هایی که نظام ایران را تامین مالی می‌کنند، جریان یافته است
بابک زنجانی شخص مسئول ایرانی در معاملات از طریق پلتفرم بایننس است
@withyashar</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/withyashar/11924" target="_blank">📅 11:07 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11923">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">رویترز به نقل از یک منبع پاکستانی:
نگرانی‌هایی وجود دارد که صبر ترامپ رو به پایان باشد، اما ما در حال تلاش برای تسریع روند انتقال پیام‌ها میان دو طرف هستیم
@withyashar</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/withyashar/11923" target="_blank">📅 10:38 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11922">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">جروزالم پست: مقامات اطلاعاتی اسرائیل هشدار دادند که ایران ممکن است در حال برنامه‌ریزی برای حمله موشکی و پهپادی غافلگیرکننده علیه اسرائیل و کشورهای خلیج فارس باشد
@withyashar</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/withyashar/11922" target="_blank">📅 10:32 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11921">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سفارت پاکستان در تهران اعلام کرد، وزیر کشور پاکستان بار دیگر با عباس عراقچی وزیر خارجه ایران دیدار کرد تا پیشنهادات برای حل اختلافات در مذاکرات با آمریکا را بررسی کنند.
@withyashar</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/withyashar/11921" target="_blank">📅 09:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11920">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">رأی‌گیری درباره اختیارات جنگی ترامپ، به دست جمهوری‌خواهان به تعویق افتاد.
@withyashar</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/withyashar/11920" target="_blank">📅 09:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11919">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/withyashar/11919" target="_blank">📅 06:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11918">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/withyashar/11918" target="_blank">📅 05:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11916">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA</strong></div>
<div class="tg-text">تو خواب نداری یاشار؟!
😂</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/withyashar/11916" target="_blank">📅 05:58 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11915">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">زمانی بدتر میشه که پاسخ با پارازیت میاد و بعد با پارازیت جواب داده میشه ، کلا دو دکل اصلی میرن کنار پارازیت ها میوفتن به جون هم و تصویر کاملا از دست میره و برفکی میشه !
@withyashar</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/withyashar/11915" target="_blank">📅 05:46 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11913">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خیلی ساده است یکی یه سیگنالی میده برای یک جوابی بعد تمام پارازیت ها میان رو موج!   خوب بزارید پیغامش درست برسه و جواب بگیره !</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/withyashar/11913" target="_blank">📅 05:42 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11912">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خدا نکنه یکی یه انتقادی کنه همه مافیا ها میان تو بازی خودشونو سفید کنند
🤣
به هر حال ما وارد موج نمیشیم و فقط خبر ، تحلیل و فرهنگ سازی رو ادامه میدیم</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/withyashar/11912" target="_blank">📅 05:38 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11911">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSiamak Mosaferi</strong></div>
<div class="tg-text">یاشار چرا همه به جون هم افتادن
کی درست میگه
چیکار میشه کرد</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/withyashar/11911" target="_blank">📅 05:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11910">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">وبسایت خبری «ددلاین» گزارش داد شرکت فیلمسازی «یونیورسال پیکچرز» با همراهی مایکل بی، کارگردان آمریکایی، در حال تهیه یک فیلم سینمایی درباره نجات دو خلبان آمریکایی است که پس از سرنگونی جنگنده «اف۱۵-ای» در عملیات «خشم حماسی» در داخل خاک ایران گرفتار شده بودند.
بر اساس این گزارش، این فیلم بر پایه کتابی در دست انتشار از «میچل زوکاف» ساخته می‌شود که انتشارات «هارپرکالینز» قرار است آن را در سال ۲۰۲۷ منتشر کند.
@withyashar</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/withyashar/11910" target="_blank">📅 04:01 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11909">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/withyashar/11909" target="_blank">📅 03:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11908">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اتاق جنگ با یاشار : آمریکا حتماً داره آخرین اولتیماتوم رو میده….
@withyashar</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/withyashar/11908" target="_blank">📅 03:34 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11907">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اتاق جنگ با شما : سیریک جنگنده اومد ارتفاع پاین تو شهر مانور داد الان
@withyashar</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/withyashar/11907" target="_blank">📅 03:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11906">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from-</strong></div>
<div class="tg-text">درود ياشار جان
سيريك الان نزديك صبحه و يهو صدا جنگنده اومد،رسما ا بالا سرمون رد شد،و چند ديقه بعد پنجره ها لرزيد</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/withyashar/11906" target="_blank">📅 03:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11905">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d5cbcf6a.mp4?token=MPUNkeD_gbqCNbDR6FEBVS7izqGVgQqsAOoIiU9eCkA4GmhcgNABbqggQf2Di2DwLSNlL9Po1i5aVl8AR7ghQBvZIeVnbEb1Jt6vHl-zfnCr3DkxG-vPTuajFAuN2s83skpSvovWfsrHGmjo6FLY3XQp4NKOOoo7iHATasmJ3ULhNRsp2d7AL6y5FPREVxEzoMmWvwa-cMUkHZ_m7ShLlSryPGHX_jI9iYUOC2ernAUgcCY0G8nnG_eZf0g1IhcfJN3UEOchYw64ZHi5VjayYlrZ7NUXE_uDuxo-Z0WBVFInL8ko2Kqre4ZaHHm9iD-fUO76v0gU-ceNvamU1CFZZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d5cbcf6a.mp4?token=MPUNkeD_gbqCNbDR6FEBVS7izqGVgQqsAOoIiU9eCkA4GmhcgNABbqggQf2Di2DwLSNlL9Po1i5aVl8AR7ghQBvZIeVnbEb1Jt6vHl-zfnCr3DkxG-vPTuajFAuN2s83skpSvovWfsrHGmjo6FLY3XQp4NKOOoo7iHATasmJ3ULhNRsp2d7AL6y5FPREVxEzoMmWvwa-cMUkHZ_m7ShLlSryPGHX_jI9iYUOC2ernAUgcCY0G8nnG_eZf0g1IhcfJN3UEOchYw64ZHi5VjayYlrZ7NUXE_uDuxo-Z0WBVFInL8ko2Kqre4ZaHHm9iD-fUO76v0gU-ceNvamU1CFZZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : یه خبرایی هست …
@withyashar</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/withyashar/11905" target="_blank">📅 03:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11903">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">Martik (t.me/withyashar) – Parandeh (IG @yashar)</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/withyashar/11903" target="_blank">📅 03:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11902">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Parandeh (IG @yashar)</div>
  <div class="tg-doc-extra">Martik (t.me/withyashar)</div>
</div>
<a href="https://t.me/withyashar/11902" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
@withyashar
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/withyashar/11902" target="_blank">📅 03:07 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11901">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/withyashar/11901" target="_blank">📅 02:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11900">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐏ـٍٍٍٍٍٍٍٍؔؑؒـٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍِِِِِِِِِِِِِِِِِِِِِِِِؔؑؐد</strong></div>
<div class="tg-text">عروسیه ولی بزا بگو درگیری بین نیرو های سپاه و اسراییل
🤣
🤣</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/withyashar/11900" target="_blank">📅 02:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11899">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐏ـٍٍٍٍٍٍٍٍؔؑؒـٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍِِِِِِِِِِِِِِِِِِِِِِِِؔؑؐد</strong></div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/withyashar/11899" target="_blank">📅 02:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11898">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">رسانه‌های ایرانی: تبادل پیام‌های میان آمریکا و ایران از طریق پاکستان ادامه دارد. وزیر کشور پاکستان با ادامه مذاکرات روز جمعه در ایران خواهد ماند. عاصم منیر، فرمانده ارتش پاکستان در صورت دست‌یابی به «چارچوب توافق» به تهران سفر خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/withyashar/11898" target="_blank">📅 01:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11897">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">النصر با کریستیانو رونالدو قهرمان لیگ عربستان شد.
@withyashar</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/withyashar/11897" target="_blank">📅 01:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11896">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">صدای پدافند در تهران
@withyashar</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/withyashar/11896" target="_blank">📅 01:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11895">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اتاق جنگ با شما : سلام همچنان صدای پدافند میاد اصفهان.
@withyashar</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/withyashar/11895" target="_blank">📅 01:42 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11894">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اتاق جنگ با شما : درود خسته نباشی برادر به نظرم درگیری هست بین بندرعباس و سیریک تو دریا داخل تنگه مدام صدای بمب میاد
@withyashar</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/withyashar/11894" target="_blank">📅 01:40 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11893">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">صدای انفجار یا پدافند شدید در قشم
@withyashar</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/withyashar/11893" target="_blank">📅 01:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11892">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">لیندزی گراهام: ترامپ تاکید کرده است بدون توانایی غنی‌سازی، مسیری برای دستیابی به سلاح هسته‌ای وجود ندارد و به دلیل سابقه «تقلب» جمهوری اسلامی، تهران نباید اجازه ادامه غنی‌سازی را داشته باشد.
این موضوع، همراه با هدف اعلام‌شده برای اطمینان از اینکه ایران نتواند از گروه‌های نیابتی تروریستی حمایت کند، از نظر من خطوط قرمز مذاکرات هستند و دلایل محکمی هم دارند.
زمان مشخص خواهد کرد
@withyashar</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/withyashar/11892" target="_blank">📅 01:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11891">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل به جنوب لبنان
منابع لبنانی از آغاز دور دیگر حملات جنوبی لبنان خبر دادند.
تا این لحظه شهرک‌های زوطر، کفرا و شوکین هدف این حملات قرار گرفته‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/withyashar/11891" target="_blank">📅 01:12 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11890">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">۸ سوخت رسان در آسمان منطقه !!!!
@withyashar</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/withyashar/11890" target="_blank">📅 01:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11889">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/withyashar/11889" target="_blank">📅 01:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11888">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پدافند اصفهان فعال شده</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/withyashar/11888" target="_blank">📅 01:00 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11887">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">درود به اقا یاشار گل  داداش من با این حرفت که میگی پادشاهی خوبه چون مردم میترسن حساب میبرن مخالفم  چون بلاخره راه در رو برای دور زدن اون موضوع رو پیدا میکنن ولی اگه قبولش داشته باشن و بهش اعتماد داشته باشن بدون نیاز به ترسوندن دستور رو اجرا میکنن</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/withyashar/11887" target="_blank">📅 00:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11886">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromKarvan Ghvami</strong></div>
<div class="tg-text">درود به اقا یاشار گل
داداش من با این حرفت که میگی پادشاهی خوبه چون مردم میترسن حساب میبرن مخالفم
چون بلاخره راه در رو برای دور زدن اون موضوع رو پیدا میکنن
ولی اگه قبولش داشته باشن و بهش اعتماد داشته باشن بدون نیاز به ترسوندن دستور رو اجرا میکنن</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/withyashar/11886" target="_blank">📅 00:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11885">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">@withyashar
eXtrime weekend</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/withyashar/11885" target="_blank">📅 00:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11883">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMehryar</strong></div>
<div class="tg-text">درود به شرفت مرد
حرف دلمونو زدی
❤️
🔥</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/withyashar/11883" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11882">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">خیلی حال کردم با دایرکتها ، حال اتاق جنگ ندارم ولی اینجا ویس میدم  تحلیل رو</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/withyashar/11882" target="_blank">📅 00:19 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11881">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">خصوصیات پادشاه مورد قبول ایرانیان
@withyashar</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/withyashar/11881" target="_blank">📅 00:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11880">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ما یکی لازم داریم همه مثل سگ ازش بترسند ! و اول از همه مثل سنگاپور و چین باید فساد رو ریشه‌کن کنه و فتیله پیچ کنه، چون اگه نکنه، اولیگارکهای مافیایی شکل می‌گیرن دوباره!!!</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/withyashar/11880" target="_blank">📅 00:07 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11879">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">فرهنگ سازی این مملکت فقط یه رضا شاه کبیر میخواد ! حتی محمد رضاشاه هم کارش نیست ! جدی‌میگیم … دموکراسی رو فراموش کنید که در انتها بد تر از اخوندا میشه
😂
🙌🏾
مینویسم امضا میکنم من اینجا رو یه کلونی کوچیک تمام تست های روانپزشکی رو انجام دادم فقط دیکتاتوری ولی مدرن بدون محدود کردن تفریح و استعداد ها !</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/withyashar/11879" target="_blank">📅 00:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11878">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/withyashar/11878" target="_blank">📅 23:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11877">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">العربیه: پیش‌نویس نهایی توافق‌نامه ایالات متحده و ایران با میانجیگری پاکستان دست یافته است که قرار است ظرف چند ساعت آینده اعلام شود.  ۱. این پیش‌نویس شامل آتش‌بس فوری و جامع در تمامی جبهه‌ها است. ۲. طرفین متعهد می‌شوند به‌صورت متقابل از هدف قرار دادن زیرساخت‌ها…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/withyashar/11877" target="_blank">📅 23:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11876">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/withyashar/11876" target="_blank">📅 23:36 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11875">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/withyashar/11875" target="_blank">📅 23:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11874">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مخبر: هیچ‌وقت باور نکردم که حادثهٔ سقوط بالگرد شهید رئیسی یک اتفاق عادی باشد.
@withyashar
😃</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/withyashar/11874" target="_blank">📅 23:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11873">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یک مقام کاخ سفید گفت : فردا کوین وارش به عنوان رئیس جدید فدرال رزرو سوگند یاد خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/withyashar/11873" target="_blank">📅 23:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11872">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca046287c.mp4?token=CLAzUKQVkwUjlyjRZlr3u0gFR31vioSsgUtdWiTHyILLB6U5W-zXWaWVlk84OCKrO5yQc06rKX748cXcwaQ3ZiNEc3Q9cbB9pwEcX-GI8MZ9-gf_kXW2WuAb-cexcrzI4NOKT8yvMQ8PlgVZRQ2jvWzGYH9n4weqDTF-yHaHoJTuuCTVevue9L-ZckJZbL4h2vH2qQti0XqvITwsdQwfkU_8HEoUedRSSVysFfUGNyt6kWrEUlCESeQlRXKZlwAhUQo0t0XWFvnLFuCiTPYofGIyHMGQbPnnRGWYImnPYknc7AULXzmKHY5DpHnX-qCSEGSjN-DQG1bT7NCdY3s9WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca046287c.mp4?token=CLAzUKQVkwUjlyjRZlr3u0gFR31vioSsgUtdWiTHyILLB6U5W-zXWaWVlk84OCKrO5yQc06rKX748cXcwaQ3ZiNEc3Q9cbB9pwEcX-GI8MZ9-gf_kXW2WuAb-cexcrzI4NOKT8yvMQ8PlgVZRQ2jvWzGYH9n4weqDTF-yHaHoJTuuCTVevue9L-ZckJZbL4h2vH2qQti0XqvITwsdQwfkU_8HEoUedRSSVysFfUGNyt6kWrEUlCESeQlRXKZlwAhUQo0t0XWFvnLFuCiTPYofGIyHMGQbPnnRGWYImnPYknc7AULXzmKHY5DpHnX-qCSEGSjN-DQG1bT7NCdY3s9WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه های رژیم :
ابراز آمادگی احمدی‌نژاد برای مذاکره با ترامپ مقابل دوربین‌ها
@withyashar</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/withyashar/11872" target="_blank">📅 23:10 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11871">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">الحدث به نقل از یک منبع دیپلماتیک بلندپایه پاکستانی: فرمانده ارتش پاکستان امشب به تهران سفر نخواهد کرد
@withyashar</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/withyashar/11871" target="_blank">📅 22:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11870">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/withyashar/11870" target="_blank">📅 22:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11869">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وال‌استریت ژورنال: کویت بر اثر جنگ ایران منزوی شده؛ با بسته شدن تنگه هرمز، صادرات ۲ میلیون بشکه نفتی روزانه این کشور متوقف شده و واردات مایحتاج از مسیر زمینی عربستان، ۶ برابر هزینه حمل دریایی تمام می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/withyashar/11869" target="_blank">📅 22:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11868">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
منبع ایرانی نزدیک به تیم مذاکره‌کننده:
اصرار آمریکا بر مذاکرات هسته‌ای باعث بن‌بست در گفتگوها شده است،
تهران تمایل کمی به ادامه مذاکرات نشان می‌دهد،
احتمال شروع درگیری در هر لحظه وجود دارد.
@withyashar</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/withyashar/11868" target="_blank">📅 21:56 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11867">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‏شاهزاده رضا پهلوی:
ما برای مطالبه آزادی‌مان عذرخواهی نمی‌کنیم. جهان باید بابت نادیده گرفتن مردم ایران از آنها عذرخواهی کند که ۴۷ سال با این رژیم مماشات کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/withyashar/11867" target="_blank">📅 21:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11866">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وزارت امور خارجه آمریکا : ‏استیون میلر، معاون رئیس دفتر در امور سیاستگذاری کاخ سفید:
‏«ایران دو انتخاب پیش رو دارد: یا با سندی که مورد رضایت ایالات متحده باشد موافقت می‌کند، یا با مجازاتی از سوی ارتش ما روبه‌رو خواهد شد که مشابه آن در تاریخ معاصر دیده نشده است. این انتخابی است که پیش روی آنها قرار دارد.»
@withyashar</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/withyashar/11866" target="_blank">📅 21:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11865">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">علی کریمی : ‏اگر نتوانیم بگوييم اشتباه ،اشتباه است؛
‏يعنى به پايين‌ترين مرحله بردگى رسيديم!!!
‏فعلا يكسرى هاتون جولان بدهید  تا اينترنت مردم داخل ايران  وصل بشه!!
‏آنوقت مردم داخل ايران قضاوت  خواهند كرد
@withyashar</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/withyashar/11865" target="_blank">📅 21:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11864">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">دولت فرانسه معتقد است بحران خاورمیانه طولانی‌تر از آنچه سایر کشورها تصور می‌کنند، ادامه خواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/withyashar/11864" target="_blank">📅 21:36 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11863">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پیام اطلاعات سپاه به آمریکا: زمان به نفع شما نیست
@withyashar</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/withyashar/11863" target="_blank">📅 21:36 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11862">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">العربیه: پیش‌نویس نهایی توافق‌نامه ایالات متحده و ایران با میانجیگری پاکستان دست یافته است که قرار است ظرف چند ساعت آینده اعلام شود.
۱. این پیش‌نویس شامل آتش‌بس فوری و جامع در تمامی جبهه‌ها است.
۲. طرفین متعهد می‌شوند به‌صورت متقابل از هدف قرار دادن زیرساخت‌ها خودداری کنند.
۳. آزادی کشتیرانی در خلیج فارس و تنگه هرمز تحت یک سازوکار نظارتی مشترک تضمین می‌شود.
۴. تحریم‌ها در برابر پایبندی ایران به مفاد توافق، به‌تدریج لغو خواهد شد.
۵. مذاکرات درباره مسائل معوقه حداکثر ظرف هفت روز آغاز می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/withyashar/11862" target="_blank">📅 21:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11861">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اتاق جنگ با یاشار : آرامش قبل از طوفان
🌪️
@withyashar</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/withyashar/11861" target="_blank">📅 21:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11860">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44e3625918.mp4?token=B7itqbtprFYWt0eZ36Wfi6sedBorfLIHHQNL9iMoDXt4ASgnD6W9qx0sWbULYLbnCE8LOKPbf_fyKF_YTS35RuwwT0Zm5zr-66fBNzAL3m-6-jbxRx4d3XhR3tgH8CdKTBo3ZLE6-9v4Fh5UFvCI8VPmvU2woW58_dNg5jFHTA6YW92mIwm4zSIuMkDynkFH3rHuhT9mQz-HkHV5SZDqm56WZqKPHvpjUZGoXXDYGRWMfvtwmzp_SFzXaRZ4yngTYK_FYtRZX6GD0wxS16OOA2KbDmRmX_D1f3H6VQID1OXK0_ta5_o___zbofVqr2gbb0CGXv6zp7uuIXsPs3JQjbO_hAeRajeuUzIFvFzWfaKe4etaUpEfYoi8QIn9eD1D04fVW6nWKi5VPWeFFdolus8ckKyEf3721eIKZTqrd9NX2dXkGu4vwgV5x9GquU6xArRRhJ0PuvUYoNLFbcOQiXXksAL9CKNu5S6lIaSGD7QuKSm2QI_SXMVrlAmaIiI3avaGtWZLxm3GYSn-5J0s5KXdAmWtJEZER2nL5uiKfvZ3Hcc-zcHq9RjvcwV5EG1mBmVAB7J-TXExEZ03r6jac4pHebX9hGplgyQAS3ONop4CzYKkbJVG78FP_ld4lcGSTD-rW89eGX5R5F7gpaFQcuFoBr5AR22J6Ipqizi2xLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44e3625918.mp4?token=B7itqbtprFYWt0eZ36Wfi6sedBorfLIHHQNL9iMoDXt4ASgnD6W9qx0sWbULYLbnCE8LOKPbf_fyKF_YTS35RuwwT0Zm5zr-66fBNzAL3m-6-jbxRx4d3XhR3tgH8CdKTBo3ZLE6-9v4Fh5UFvCI8VPmvU2woW58_dNg5jFHTA6YW92mIwm4zSIuMkDynkFH3rHuhT9mQz-HkHV5SZDqm56WZqKPHvpjUZGoXXDYGRWMfvtwmzp_SFzXaRZ4yngTYK_FYtRZX6GD0wxS16OOA2KbDmRmX_D1f3H6VQID1OXK0_ta5_o___zbofVqr2gbb0CGXv6zp7uuIXsPs3JQjbO_hAeRajeuUzIFvFzWfaKe4etaUpEfYoi8QIn9eD1D04fVW6nWKi5VPWeFFdolus8ckKyEf3721eIKZTqrd9NX2dXkGu4vwgV5x9GquU6xArRRhJ0PuvUYoNLFbcOQiXXksAL9CKNu5S6lIaSGD7QuKSm2QI_SXMVrlAmaIiI3avaGtWZLxm3GYSn-5J0s5KXdAmWtJEZER2nL5uiKfvZ3Hcc-zcHq9RjvcwV5EG1mBmVAB7J-TXExEZ03r6jac4pHebX9hGplgyQAS3ONop4CzYKkbJVG78FP_ld4lcGSTD-rW89eGX5R5F7gpaFQcuFoBr5AR22J6Ipqizi2xLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سکانس هایی از فیلم کمدی تهران۵۷ و باز سازی عکس معروف ترامپ در تهران…
😂
@withyashar</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/withyashar/11860" target="_blank">📅 20:50 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11859">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامپ : پس از پایان جنگ با ایران، قیمت بنزین در آمریکا به سطح ۱.۸۵ دلار سقوط خواهد کرد
«این وضعیت خیلی زود، خیلی زود تمام خواهد شد. و وقتی تمام شود، قیمت بنزین شما پایین‌تر از قبل خواهد آمد. می‌دانید، چند ماه پیش از آیووا رفتم و قیمت بنزین ۱.۸۵ دلار در هر گالن بود.»
«و ما دوباره به چنین ارقامی خواهیم رسید. اما به‌هرحال به شکلی بسیار بهتر به آن خواهیم رسید. ما به آن اعداد برمی‌گردیم و در عین حال کشوری خواهیم داشت که سلاح هسته‌ای نخواهد داشت!
@withyashar</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/withyashar/11859" target="_blank">📅 20:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11858">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/456925e365.mp4?token=QYF2oE3MINCmzT_lDbN-XFL4S2VhJH9bTkWHsKZAwJY8zDPatemVi8iAlzmQMrIU2zjdVAykEV3lZiN_hGx07tI3Sz4rXWWGBaxx0AadIkA3AYRs2CJWylBgUDx0LnhfYKqDlKH_muQ4K9usCkBCpNNIuSU928b5_Q3HEBjJb3OLxYla8Dxp2q-gu2l78W20IYffzLkPU5WL94uEijr9unmK5c3_vJV8JvenpCwQzcRxvb3Iz5zCPjungofY59gihLZZH3QzpIWiCmrt3Qn-yqXiDpimPj_4z3yXhKhQguiv-avhOJzSksC9aM-1xrepeLOu5er9TK9vwXw4vIHvKI3_Ena-ufdR6YpQWcAoG020WsDaFEDa0vosi8aWLwuZzK-CS5srQvv__dv_vVDU9HCnLWlZn7kgpXg25oPJxmv0grhRCJ_72U4bLxqaN4ITU6lFITdceixtdgv2A7sqRNEjuG-0-XbNcCfxZdAXtBEmvt1CL4kWxQkZoPe8GlHZBUDs7s7a_zWbB5FHoov6Dt9Gy_AXCbU5NlpjXOKhnYrRyJDk9lhflscvm0fJa8UEYq8GwnnAFbzdvQI1m8sYLbhp6rh34t0INEsTURhJ72x_CxUuPvV5aci-uOXi9z-H74SaFh1o_I0zEVxY82I65AfEh0um1_VOnE9dn2YwreE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/456925e365.mp4?token=QYF2oE3MINCmzT_lDbN-XFL4S2VhJH9bTkWHsKZAwJY8zDPatemVi8iAlzmQMrIU2zjdVAykEV3lZiN_hGx07tI3Sz4rXWWGBaxx0AadIkA3AYRs2CJWylBgUDx0LnhfYKqDlKH_muQ4K9usCkBCpNNIuSU928b5_Q3HEBjJb3OLxYla8Dxp2q-gu2l78W20IYffzLkPU5WL94uEijr9unmK5c3_vJV8JvenpCwQzcRxvb3Iz5zCPjungofY59gihLZZH3QzpIWiCmrt3Qn-yqXiDpimPj_4z3yXhKhQguiv-avhOJzSksC9aM-1xrepeLOu5er9TK9vwXw4vIHvKI3_Ena-ufdR6YpQWcAoG020WsDaFEDa0vosi8aWLwuZzK-CS5srQvv__dv_vVDU9HCnLWlZn7kgpXg25oPJxmv0grhRCJ_72U4bLxqaN4ITU6lFITdceixtdgv2A7sqRNEjuG-0-XbNcCfxZdAXtBEmvt1CL4kWxQkZoPe8GlHZBUDs7s7a_zWbB5FHoov6Dt9Gy_AXCbU5NlpjXOKhnYrRyJDk9lhflscvm0fJa8UEYq8GwnnAFbzdvQI1m8sYLbhp6rh34t0INEsTURhJ72x_CxUuPvV5aci-uOXi9z-H74SaFh1o_I0zEVxY82I65AfEh0um1_VOnE9dn2YwreE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس‌نیوز: «رگ حیاتی تهران»
ژنرال جک کین هشدار می‌دهد که یک توافق جدید ممکن است ایران را زخمی اما همچنان پابرجا باقی بگذارد و این تصور را در ذهن حکومت ایجاد کند که آمریکا را وادار به عقب‌نشینی کرده است.
او می‌گوید:
«مشکل من با این توافق این است که ما ایران را زخمی اما همچنان سرپا باقی می‌گذاریم، و آن‌ها از اینجا خارج می‌شوند و خودشان را قانع می‌کنند که آمریکا را مجبور به عقب‌نشینی کرده‌اند.»
@withyashar</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/withyashar/11858" target="_blank">📅 20:30 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11857">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6961194543.mp4?token=v9WsrqFgkXpxng8EWPaIEHJXQrxNeyuSMwop8l04bZ8jegvFjBD3MFzncivWp6cXrImuWjy_6xovmiRiEQxNQyQ7SHJath32UG67pctooejwH2XBjEKOpWjl2Qwa28SoVX-1pRl5XHXuHBY83PYwXLKNUfBFsl1IJUI8fmgEsXS0OoxQWMOcrwZ4COJ6MYupJ_btb11IoELT6FMT0Pjt3lJG8nvoGVfdg1MdWdjf0iBeEGxYniPs-VolzMG39CF-xCuB0Zt2jpBUOtHCa3t5s2p2o-K7BHuH_XEkkjTvFFMd3LtpeovgpQXaytm957XBJE86pzS47d5QedT9lXfg4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6961194543.mp4?token=v9WsrqFgkXpxng8EWPaIEHJXQrxNeyuSMwop8l04bZ8jegvFjBD3MFzncivWp6cXrImuWjy_6xovmiRiEQxNQyQ7SHJath32UG67pctooejwH2XBjEKOpWjl2Qwa28SoVX-1pRl5XHXuHBY83PYwXLKNUfBFsl1IJUI8fmgEsXS0OoxQWMOcrwZ4COJ6MYupJ_btb11IoELT6FMT0Pjt3lJG8nvoGVfdg1MdWdjf0iBeEGxYniPs-VolzMG39CF-xCuB0Zt2jpBUOtHCa3t5s2p2o-K7BHuH_XEkkjTvFFMd3LtpeovgpQXaytm957XBJE86pzS47d5QedT9lXfg4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس نیوز : تیم رئیس‌جمهور ترامپ شروط ایران برای دسترسی و کنترل تنگهٔ هرمز را رد کرده است.
خوب است! فقط شرایط «اول آمریکا» پذیرفته می‌شود.
«ایران نقشه‌ای منتشر کرده که آن را “منطقهٔ دریایی تحت کنترل” می‌نامد. تهران می‌گوید متعهد است تنگه را برای کشورهایی که با شروط آن موافقت کنند دوباره باز کند؛ شروطی که به‌احتمال زیاد شامل دریافت هزینه برای عبور از این تنگه خواهد بود.»
و واشنگتن، در واکنش به این موضوع، اعلام کرده که این اقدام کاملاً غیرقابل قبول است
@withyashar</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/withyashar/11857" target="_blank">📅 20:24 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11856">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">خبرنگار: آیا دارید کنترل سنا رو از دست می‌دهید؟
ترامپ: نمیدونم، واقعاً نمیدونم، من فقط کاری رو میکنم که درسته.
@withyashar</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/withyashar/11856" target="_blank">📅 19:54 · 31 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
