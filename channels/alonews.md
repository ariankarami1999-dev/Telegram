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
<img src="https://cdn4.telesco.pe/file/Y_jSktuvsFhV0Kx2gy3l4stVQEtXuc8U1nJmK_n39L0iiCM6OkECDfhbjd8duQfzEutHONwagdvlGRaIVy6Kyb7PZcARhiQuPTUoIgc8ntH3_Sc9xA6f_zhlkZk0ginDi8HgcccLT595iRDylLUbQpuhUh9GNHF_hpNmRK6JOkpryD91GH6-OdgvxXh2iAcg5gSrPOfe-7zoG1Ku70mapjApS84Z6VmjI49rgtvVClX_AUvAYTiVL0GNPwKDI5JZ-8A9lRIgvpJWuigcuOlgZOmL4Hh1JnT9Ue9N-oM0aUq60uH5d6XLlXh8tTYxVa8x0vcnlV1jNutsYPOkaEk6vQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 970K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 23:34:57</div>
<hr>

<div class="tg-post" id="msg-125647">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YwJikTgkXQhz78VJk3zguuGd-8-wBVNYTL-XzSJwfD7eblso7b1NG6-nx4IBYG62_ufT2fVPafyGnH6yLCUzepNFbMDj4TevSkQLyypcLpBN855_rFJuAHwspMH3RI0Sovt5mRwUNyL1Sfw88KyCYJlqkXYaSszMAZnt8wwCbf5ZzfeI8Z4eTlqPpiiRBGKCj6KYwqB0LQYYdG2FDnXWeqvufya3Y80suaZyi8H9ET8TQUVDU_PVSPoLUC-lCLTGnmophQ7Ims47ETFxlRNRx3dlDEH3PZa2xI3QRDVbNEzmGOjjB5npXL6spZ1eoVwsHa0Cub8CscwBuemluhiJyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز تعدادی قایق تندرو نیروی دریایی سپاه در مناطق مختلف تنگه هرمز درحال گشت زنی بوده اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3 · <a href="https://t.me/alonews/125647" target="_blank">📅 23:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125646">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
وزیر کشور پاکستان: پیام‌ مهمی از سوی ژنرال عاصم منیر به تهران آورده‌ام
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/alonews/125646" target="_blank">📅 23:28 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125645">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTYWyG_86LF-9elYA4wWjjk2WQeuEjNSBazQrUeuaOuyr9CuMhA8GJca8K2MLtPwYZwoJGB2d17RZlj37n836yF4YN48l4GKGwcBk4p-OOkDujSWVdChQPYG34Vi-f4zHya5KBP0otmrfRbSZA-vv0NVIHdTRDcs5QSAhmAh1gDj-mfzXO7vcaVJyFeUNDoKrROfPfSSOiGFVc0RmZRdBm_aZsfAQJCOe7g0aXl6EKsTKhecajIwHrGZILc7D9HAI0yZTiBhJE2Zr0fkNbfcbtjmtUmTmGPlRrHr7-2t63Z3jO12hyYMYLXyD2ZsVmyP3hD3Au1-ZGvfWoTGfRBcsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صدف طاهریان مدعی شد بهمن ۱۴۰۳ به ایران بازگشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/125645" target="_blank">📅 23:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125644">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل کاتس: سربازان ارتش اسرائیل همچنان با شجاعت در لبنان علیه سازمان تروریستی حزب‌الله برای حذف تهدیدها، محافظت از جوامع شمالی و تضمین امنیت شهروندان اسرائیلی عمل می‌کنند.
🔴
هزینه سنگین و دردناک است، اما در کنار این، عزم و شجاعت سربازان ما برای تکمیل مأموریت قوی‌تر از هر چیزی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/125644" target="_blank">📅 23:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125643">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
رئیس شورای شهر تهران: رایگان شدن حمل‌ونقل عمومی بدون تأمین منابع مالی به توسعه آن آسیب می‌زند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/125643" target="_blank">📅 23:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125642">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
با سابقه ۵ سال فعالیت مداوم
🛡
حتی بدون قطعی تو دوران جنگ
🔥
آتیش زدم به مالم به خاطر عیالم  بقیه هنوز VPN حجمی میفروشن اونم با قیمتای نجومی
🚀
ما چی؟
💯
💥
VPN نامحدود واقعی فقط 190 تومن
🏷️
💥
بدون محدودیت حجم  @NetAazaadBot @NetAazaadBot</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/alonews/125642" target="_blank">📅 23:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125641">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NesGfoXKaPtEHTaIaUM__lQEdZ9aTZ6nc3k9LUTXJp4mjcgflCn50kOLDeNKQXJaSTk4tD4X2pmHNV8eUpVh23s8rIhhf2PBh8f18TU8HzceXn1sctv32nKcCPuUTx74UwjJGTFfs7StXPBURWO97hl1tWEULN6IhRHL10XiJ5QgqwhZzhvq8k-3n3FnV5i7HX6qhLUWW5iatRn29TChaEZLCS-P-QfoW6QD6Kj_Ft6YxSphZNl3rDHxz2UXDPw0QuVEAhZFLD46tIxe6lMcrsFlWxzK-6JBwLUxJkddTiKEXHrceNoL4Nati5A0tuIcMZYOd3fxGctwCB_VvIsapg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با سابقه ۵ سال فعالیت مداوم
🛡
حتی بدون قطعی تو دوران جنگ
🔥
آتیش زدم به مالم به خاطر عیالم
بقیه هنوز VPN حجمی میفروشن
اونم با قیمتای نجومی
🚀
ما چی؟
💯
💥
VPN نامحدود واقعی فقط 190 تومن
🏷️
💥
بدون محدودیت حجم
@NetAazaadBot
@NetAazaadBot</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/alonews/125641" target="_blank">📅 23:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125640">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ماجرا و محتوای این پست بسیار دردناک و ناراحت کننده‌اس، اگه بیماری قلبی دارین به هیچ وجه نخونین.  توی سنندج یه زن و شوهر از هم طلاق میگیرن، بعدش مَرده حضانت بچه هارو به عهده میگیره و میره یه زن دیگه میگیره. دیشب همسایه‌ها بعد از شنیدن صدای جیغ وارد این خونه…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/125640" target="_blank">📅 23:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125639">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
نیویورک تایمز: ترامپ از اینکه حزب الله و اسرائیل حاظر به قبول آتش بس ترامپ نیست و به نبرد با همدیگر ادامه میدهند ناراحت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/125639" target="_blank">📅 23:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125638">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQ_O4w707sAaOtCzKwnTR9CfENsnoaAaAJre_YqrbTpk7V4MyiApArRE_Gk5JH8ZDIwfUoUkQhUZxoQA55jrgGyyU3hPhwUphL2kOGL7meCKMq7mZpM-JZWlqdEHqp4_H1-fnhOUBpWVFxh_l3TQzFEP5Y1np2Bz-1KSUZhyOAGwGgqnml8jO9xqo8J8p2sKihNJQekyZyNYPHowL1O73jLWFOEJ8haQ_BbUx0TJsL9YKLUvgFDp7aXOb_innlxH6pHTcTJ8qOLu9jDXMWZ3n5fRHGB8AedkNk9wNeugqkJEiOvRhMEVsJh6RHu_6iqC5pbGOadqAuuf8AlcErm_lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مونا آذر، بازیگر ایرانی و مشهور هالیوود اعلام کرد که بزودی وارد ایران میشود تا از خاک ایران حمایت کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/125638" target="_blank">📅 22:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125637">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
کانال ۱۲ عبری:  افزایش تعداد سربازان و افسران اسرائیلی کشته شده از زمان آتش‌بس در لبنان به ۱۶ نفر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/125637" target="_blank">📅 22:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125636">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LL7iwEMLbl2HMCkIcFfp0xp5N73pYtDj1MOB2Pl_lz7KXghYXNSU5nfPVPPsHkbKUlDCXifGzvhGOL_-F93KbYHccd-LGbAS8dSVuSfrsFHWMi95Ku4bRPyizTubrWY1cClrfxlKDYPl4bfifVGf59r0S5Gjrbr-1RJcfe-XPP3aSe5aE5w0sESh5Bg1nQuZssYYDyrivzg-WSa0gM8GgaW66wmEG3Hh7Yt7EcEwA6EomfRc6Oz4UhAAzFXsDlxXIUkwywMu7sT91YvtJ78cr7pxBJsF9SPvEZ0YacbJYuXMIw3tjVJd4PIPispHrzOoVhB_03_WwbpBBeLVdFLh2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش صدا و سیمای جمهوری اسلامی، معاون سیاسی، امنیتی و اجتماعی استاندار هرمزگان اعلام کرد که عملیات خنثی‌سازی و انفجار کنترل‌شده مهمات منفجر نشده باقی‌مانده از جنگ اخیر امروز، ششم ژوئن، در بندرعباس آغاز شد.
🔴
عملیات پاکسازی تا سه‌شنبه، دهم ژوئن ادامه خواهد داشت و در این مدت صدای انفجار در سراسر شهر شنیده خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/125636" target="_blank">📅 22:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125635">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
شاه چارلز سوم به همراه جمعی از اعضای ارشد خانواده سلطنتی بریتانیا، روز شنبه ۱۶ خردادماه در مراسم ازدواج شاهزاده پیتر فیلیپس، نوه ارشد ملکه الیزابت دوم، در جنوب غربی انگلستان شرکت کردند.
این مراسم خصوصی در کلیسای «All Saints» در منطقه کمبل برگزار شد و در آن، شاهدخت آن، مادر داماد، به همراه همسرش تیموتی لارنس حضور داشتند. همچنین  ویلیام وهسرش کیت شاهزاده و شاهزاده خانم ولز، ملکه کامیلا و دیگر اعضای خانواده سلطنتی از جمله شاهدان این مراسم بودند.
شاهزاده پیتر فیلیپس، که در حال حاضر در رتبه نوزدهم خط جانشینی تاج‌وتخت بریتانیا قرار دارد، در حوزه مدیریت ورزشی فعالیت می‌کند و نقشی رسمی در ساختار سلطنتی ندارد. همسر او، هریت اسپرلینگ، پرستار کودکان است. این ازدواج پس از پایان ازدواج قبلی فیلیپس در سال ۲۰۲۱ صورت گرفته است.
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/125635" target="_blank">📅 22:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125634">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
نیویورک‌تایمز: اسرائیل مکالمات مربوط به مذاکرات آمریکا با جمهوری اسلامی رو شنود کرده.
🔴
اسرائیل تلاش‌های خود برای شنود مقام‌های ارشد آمریکایی از جمله استیو ویتکاف و البریج کولبی، معاون وزیر جنگ آمریکا، رو افزایش داده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/125634" target="_blank">📅 22:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125633">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2f81d5cd9.mp4?token=U3LPG0UHcv_T5bZZC4XHRJRUz-VXBDwrZ_N9v12RywYPjU5VAOALaqclGvF3L78UZutxgIZj33uKVizfj2XPGNPYmoUUz-grOBzA-QXdkJn9o6b18XRIVqtj7qcsPNKNhQ6RU_GI82Fq0Y3x4ftW1uFq-Obb61M9ATg-eUim91bbHGVfMkedx9j_FoE96TY0uYH8qB5aRmNmGkGc2JkDrdeNy2m7giiBwB_bbIpPSxoZGmroomEI6qgVwvEnQJPoymqhcykgiTow9r4dmpG_GQucges-78dea1G6MqW4gd7UgynA0jETLtnhN4oaY8Vs3VDiDFFlJwg8f_bBtLtLKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2f81d5cd9.mp4?token=U3LPG0UHcv_T5bZZC4XHRJRUz-VXBDwrZ_N9v12RywYPjU5VAOALaqclGvF3L78UZutxgIZj33uKVizfj2XPGNPYmoUUz-grOBzA-QXdkJn9o6b18XRIVqtj7qcsPNKNhQ6RU_GI82Fq0Y3x4ftW1uFq-Obb61M9ATg-eUim91bbHGVfMkedx9j_FoE96TY0uYH8qB5aRmNmGkGc2JkDrdeNy2m7giiBwB_bbIpPSxoZGmroomEI6qgVwvEnQJPoymqhcykgiTow9r4dmpG_GQucges-78dea1G6MqW4gd7UgynA0jETLtnhN4oaY8Vs3VDiDFFlJwg8f_bBtLtLKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پویان مختاری شروع کرد به قرآن خوندن!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/125633" target="_blank">📅 22:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125632">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Co30uDJsCLKncsakHPX0crNa5hszDE9l-8sj_wSLPmEvA2W-haSaP8K4s6mqcV4GOLIkGvF03ACFbeuFHkAjAZEW75hZ4XUIscU-vboJNH-lzmc8O1mkpg6xnykL8TzLa3mh4ufPNTO1ApEKutzIrI6gpE0-3p5u0-PZD9tF_CoRKFLjm0hWAGawcz0FYi2DDjJBJh69f-1MKXgX6EBgfWVVCuV_P_drekGb_-NOcjEmftEGdY0KrFCSu5cYeiErxe3uszhX6WLqS_tNXQ_OyIm-tlUpZ4gV-816O3R3snfPSTKs4ZmAhwl4PBL0OaONk8OXoeLGP6NkxU0fBzKNZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه زوج اندونزیایی اسم بچه تازه متولد شده‌شون رو "علی خامنه‌ای" گذاشتن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/125632" target="_blank">📅 22:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125631">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFa9rcKiWbO48ML0pgkMvdOhimh81UT65FTiTHgpwB9hGsn4u-LUIwoPl9L7CxxZJV6L9ODMUXLx2c0gHqkm5H3B8jSHFTqc4ty9ZADNHP4M13psOST9m9uiJxZBNOkTekOmi2DhsD0A9wZ9L4kzxlCn7xrgiGVV8KMM_djIli2lpXmqUkkBIq1kfsu-8EZWctSrj2OB8zKeuB-eNBHGYdemKcb0JS6RzSDzQi5La0iH-p0pTuQiRCp4h4zhRU4vq6rhZhnOr_NpPgyt4iqYdrmH8ktTDPDNjSYFLotWiOsojErqYhPvF2md1Di9Wcxf6U4Hby3wHomZe0ErdyuCcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇨🇱
تو بازی دوستانه پرتغال و شیلی لیائو اینطوری بازیکن شیلی رو زد و اخراج شد
😂
😂
@AloSport</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/125631" target="_blank">📅 22:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125630">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjkJ0kVPhS8-NZ8A7VGALAUxDYUBAkco3d3qM8T8QnN4EQMKubR5VZrhO4unWyX8qUtmHyiN44ZAnZSJ6KJrm0ylCxqqbL2cLsRa_wVeEx_MotNTZdb2Yziu2q2aCCFFZg1HI18ziWa6VLxleB_OEcHKRjG1pX3GfqNzsi47Q_uFw5D0m6NMZAnE_EVgk4LmiE-wFd0MNnfdBZXlviqGUEXNLOrKgQUFIsIACT6anIL7jLVMGjXY39rz4v_PPMEUJLTfUyey5OGhTrwYbUIMYOysedWrABoX-BD5lU1NEBB0IGLqJo4DHpz9EGRjjXCM-RgmwNh1hh1NuhfvdyUn1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خان‌یونس ، لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/125630" target="_blank">📅 22:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125629">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/199e947d8b.mp4?token=K19jg-N3zJmHtiuhkHHHw59Ck-jX-0a8hVB4yVr1vMMqG0R2MySTYSKZbYDhqNITMWJb0PuXogip051DXCh5gHuKU-tQQ-r1AhaxJIFUb1HpxwgH5Bm_24FSZFqdOXqKCdJrLoZByuyvEpgNIH-CWTAhtSGKmEB-ePhgiMCPbWe9sv9NhuSMqFEuKqTmOVVZxNfOoZ7Yo_MLrUhvbbOCC8g1ucyrwgWECr0n-RaxWFRBqXJM_Jvh40ibpXY6Ocsu5fwUzsHDU7_CSyHdnZSuZWg4lMRgEDFmWhO6iWZX11nUcFu75wD0aHRZ_NSx9YrY8GvEn6jVN3In2YBGD0AEUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/199e947d8b.mp4?token=K19jg-N3zJmHtiuhkHHHw59Ck-jX-0a8hVB4yVr1vMMqG0R2MySTYSKZbYDhqNITMWJb0PuXogip051DXCh5gHuKU-tQQ-r1AhaxJIFUb1HpxwgH5Bm_24FSZFqdOXqKCdJrLoZByuyvEpgNIH-CWTAhtSGKmEB-ePhgiMCPbWe9sv9NhuSMqFEuKqTmOVVZxNfOoZ7Yo_MLrUhvbbOCC8g1ucyrwgWECr0n-RaxWFRBqXJM_Jvh40ibpXY6Ocsu5fwUzsHDU7_CSyHdnZSuZWg4lMRgEDFmWhO6iWZX11nUcFu75wD0aHRZ_NSx9YrY8GvEn6jVN3In2YBGD0AEUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
جاویدنام مجیدرضا رهنورد ، وقتی جلوی دوربین ازش پرسيدند وصیتی داری ، گفت سر مزارم قرآن نخونید ، شادی کنید و آهنگ شاد پخش‌ کنید ؛ او یک آدم عادی نبود ، یک قهرمان و اسطوره بود...
🤔
عرزشی حرام زاده بعد تو سمت مردمت اسلحه گرفتی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/125629" target="_blank">📅 22:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125628">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRm4K_9D7g1mp_ZkU32NbO15PA1aU-a2usBho0rJfdCx1BTQbIw60S7cwk6otILen4lQz1KaFS3M0lQPVV_-g2_lOiuwk3ahee-gilwPhuNlF1nA-eq2ZKTgAHUSvuHK9iWkfuZ1wVurlC88ZWzt72TrRhmLXzUN_ROcxLzNMFb1DBYCgdopaO4cffHgCVWfoBvDGnsv1ZCRmjb2b7PGXjSz0MMcDZYUbn8xAknd47chk4br0Y-Sx1HIUFI1CPKMVjllyc9JJWDrW5XoxSbdSDUcwESwNQsR4XNx77-iiE-8wXf0fd7cY38nfqWcl1wuwSnPXNiy9qpUy4ZeZlwGtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/125628" target="_blank">📅 22:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125627">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
ادعای ایسنا: وزیر کشور پاکستان در جریان سفر به تهران حامل پیام ویژه‌ای از فیلد مارشال ژنرال عاصم منیر به سید مجتبی خامنه‌ای است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/125627" target="_blank">📅 22:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125626">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
روابط عمومی نیروی دریایی سپاه: صدای انفجار شنیده شده از اطراف جزیره خارک مربوط به خنثی‌سازی مهمات باقی‌مانده از جنگ تحمیلی سوم در منطقه بهرگان است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/125626" target="_blank">📅 22:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125625">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
محمد جمالیان، عضو کمیسیون بهداشت و درمان:
🔴
بعد از اون پیامکی که برای مردم فرستاده شد کشت خشخاش تو کشور زیادتر شده!
🔴
کشت خشخاش تو یه سال 246 درصد افزایش پیدا کرده و مردم فهمیدن فروش تریاک سود آورتره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/125625" target="_blank">📅 22:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125624">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf1fba69e.mp4?token=UdL4oPL-79AhOx3MzreaoFN5jGcE3I7UOA0WDPyvtqiw1f9ZBqZsxTmO6GU9AysRE6HIc83RLCeUdJz03MaV9_vVpFcg-VvVwINh6dpmDVQE3NLoygpmuJlA2dAYLHg2CZJluMky116YEkOpAtd1SCUZcFWiBUISLQRnUpsCfM9_6YUZH7ABmi_ctRoH89LXk8fDhzX5aN7utrxP8tSGdNitG-aq1bG7fmGbV-s-Yk0xR4dbHhv35JbieAlog4ykF2zm7UlRJMBr5r4P4AJt_8FeOp8atH_2sVielCPPxOPFNIhn6FsW9XLLup0sCTUGY3-B3MBUNZYb1yC7EKewBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf1fba69e.mp4?token=UdL4oPL-79AhOx3MzreaoFN5jGcE3I7UOA0WDPyvtqiw1f9ZBqZsxTmO6GU9AysRE6HIc83RLCeUdJz03MaV9_vVpFcg-VvVwINh6dpmDVQE3NLoygpmuJlA2dAYLHg2CZJluMky116YEkOpAtd1SCUZcFWiBUISLQRnUpsCfM9_6YUZH7ABmi_ctRoH89LXk8fDhzX5aN7utrxP8tSGdNitG-aq1bG7fmGbV-s-Yk0xR4dbHhv35JbieAlog4ykF2zm7UlRJMBr5r4P4AJt_8FeOp8atH_2sVielCPPxOPFNIhn6FsW9XLLup0sCTUGY3-B3MBUNZYb1yC7EKewBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیکزاد، نایب رییس مجلس: تنگه هرمز طبق قانون مجلس به حالت قبل برنخواهد گشت/ تنگه هرمز برای ما از بمب اتم مهم‌تر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/125624" target="_blank">📅 22:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125623">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
یک سرباز اسرائیلی، بر اثر جراحات وارده در نبرد در لبنان کشته شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/125623" target="_blank">📅 22:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125622">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
احتمال شنیده شدن صداهای شدید انفجار به مدت ۵ روز در بندرعباس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/125622" target="_blank">📅 21:55 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125621">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
تسنیم: لحظاتی پیش صدای انفجار در جزیره خارگ شنیده شد. این صداها مربوط به خنثی سازی مهمات در منطقه نفتی بهرگان است که در جزیره شنیده شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/125621" target="_blank">📅 21:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125620">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
کرملین: نتیجه عملیات نظامی در اوکراین برای واشنگتن روشن شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/125620" target="_blank">📅 21:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125619">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxLjK2iZQ4h_pax3YP2k33xeTc-zz21gskzRosbDZ3kAKUzbytZ4NFKCYomvGD5gtYOvwNzezoJl-Au32PPXpzj0mWhQTm0Wb10HtjrmUZMXRVCdpPKJWgmd9ZdFJhixWkAMZfo6ed3yEaPk48IAplf3pDL3gc9JyG03w-zUs77JohyjicyF7wJkpaTzQEpNbr-Zda4Vznyo3Ozhrvj_7AJAJOtywFof6nLGRjxBfqHSQmOPppTBtNsgglTd8WKnLvDySy5fE51zeiYBTnfO-9vt0DcM7SgSGn4M27nv_ERO7Lipik1z8OEuWJWtTjfy16LhkuZbCBD7RNvYkPhT0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث‌سوشال: کتابخانه باراک حسین اوباما، در ۱۰ سال، وقتی کاملاً به بلوغ رسید!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/125619" target="_blank">📅 21:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125618">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dzche1ynIcG9dznA0cwXFYl-ieegCnhCU_S6-MfmME76oCmmmWPTjNXmas71ky4lVRKcg1HaxsJUGou0hO6A1Oo9eTx9tEbziL3Cay0K5SCN0LV5LquNB3GG_gxay-1x2XJgH8m7fzP1QsHxmCrQRSqeyqN1k6C-9KcfIMS8Soeoix2ppimFLbdzq-EK9_sarFWW6Jilu2GZ-tEjsK0xBWhQm3bGG_-aDmFK7oDun0UR-Jicp614GDeoWW2KGQd-1Iz-Kf4Wi9Q1PnuXIy4EZOwPrhs_Z38I6glpMIrBuU82lws0uYNgMzJ2OW7iCTvqaFoEWQoypc9RV_p3QpTqng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حکم بازی کردن دانش آموزان معترض به مصوبه کنکور در محل تجمع
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/125618" target="_blank">📅 21:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125617">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_LAZOJM2SZqw3On8U0GOgKrloibxEAZZaBFMVamo5djQxFm05Sizwj1EsrLIRatVSw8BsNLEudbKEDxy0XkdyTNP1CIQLQCvvvfI0_sBEzCBmeCYKiqcMzCwVfVF9GyNpXd2f0UWEOFf8VN4ozuiT29_FL9ILjDBI4aBbuRpHupqehH8YUqkGq7jCmPalq-P-VJB6etN7UqKUyrl1dOZcNHNUOw1YpBPlJn2NDAYJxjJSS-tg3vd20GDxvKvT1ZEnw1t1MsACT4-0TJJhprspOw6g1EGtx0vXgiUzc78tzqZXyZBjq90tu-OFZA_tOfaNRKjDx3nXQox0gdxiHLnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارزیابی‌های اخیر اطلاعاتی ایالات متحده نگرانی‌هایی را برانگیخته است که سازمان‌های اطلاعاتی اسرائیل تلاش‌های خود را برای نظارت بر مقامات آمریکایی دخیل در مذاکرات با ایران افزایش داده‌اند، که این موضوع باعث شده مقامات آمریکایی درجه تهدید ضدجاسوسی اسرائیل را از «بالا» به «بحرانی» ارتقا دهند، گزارش نیویورک تایمز.
🔴
اطلاعات اسرائیل به دنبال درک استراتژی مذاکره دولت ترامپ است، از جمله مواضع مقامات ارشد مانند استیو ویتکاف، البریج کولبی و مایکل پی. دی‌مینو چهارم.
🔴
مقامات سطح اخیر جمع‌آوری اطلاعات اسرائیل را به‌طور غیرمعمولی تهاجمی توصیف کردند.
🔴
پرسنل نظامی و اطلاعاتی آمریکایی همچنان هنگام فعالیت در یا در کنار اسرائیل از تدابیر امنیتی تقویت‌شده برای کاهش خطرات جاسوسی استفاده می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/125617" target="_blank">📅 21:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125616">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
مهر: صدای انفجار در خارگ مربوط به خنثی سازی مهمات است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/125616" target="_blank">📅 21:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125615">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
مقامات ارمنستان امروز شش نامزد از حزب مخالف ارمنستان قوی را یک روز قبل از انتخابات پارلمانی دستگیر کردند.
🔴
رسانه‌های دولتی دلیلی برای دستگیری این شش نامزد ارائه نکردند.
🔴
این حزب توسط سامول کاراپتیان، میلیاردر ارمنی-روسی رهبری می‌شود که در حال حاضر به اتهام دعوت به سرنگونی دولت تحت بازداشت خانگی قرار دارد. کاراپتیان این اتهامات را رد کرده و آن‌ها را با انگیزه‌های سیاسی توصیف می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/125615" target="_blank">📅 21:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125614">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fa8198822.mp4?token=D2FQmn9HfU86370W-HJ8bEMpW1M1dVcszTb0B0CNAg282U1pMwJerjMV3gfJ8M310PXh5vxl_hMThQqSqr5nrT_UCxSz2F957gD0Vfly2hGqBr9FJTD4w9PBfGPcAhILPiTowH8VB32_aPasO0zztCVn_24E5a0zcAxKYEda-yejgP7wBloJfjZ7Sw8H5chNYLDqe72h2Abu8390mUT2MAO9y1z2MaMPfRfd0oI-onBTXIck9R2SARBM4tyRgyjdBesMhAljdE9hld6UM1ONHb68dMsRllI9BMicWsduoK9uu8hoBbY0SXsG7gFLLynLS0Uq3nN4JL5dYekI2gO3HDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fa8198822.mp4?token=D2FQmn9HfU86370W-HJ8bEMpW1M1dVcszTb0B0CNAg282U1pMwJerjMV3gfJ8M310PXh5vxl_hMThQqSqr5nrT_UCxSz2F957gD0Vfly2hGqBr9FJTD4w9PBfGPcAhILPiTowH8VB32_aPasO0zztCVn_24E5a0zcAxKYEda-yejgP7wBloJfjZ7Sw8H5chNYLDqe72h2Abu8390mUT2MAO9y1z2MaMPfRfd0oI-onBTXIck9R2SARBM4tyRgyjdBesMhAljdE9hld6UM1ONHb68dMsRllI9BMicWsduoK9uu8hoBbY0SXsG7gFLLynLS0Uq3nN4JL5dYekI2gO3HDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مردم فیروزآباد قرآن هایشان را در آب ریختند!
🤔
عرزشی حرام زاده وقتی دین رو بازیچه قرار میدید و دروغ تحویل مردم میدید نتیجش میشه همین.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/125614" target="_blank">📅 21:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125613">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJuSwTK7kvhGi7N9PgICW0jkvdnxBsEkmCI_CSq47wlQ8KqCfwepOES97xAh6AffkVC1LxRt69aDZBAXdpQ-hEfARI1g6tRQ9tdKQleioxHjdxkQThF9DVQ8DNRTXvccI1dsxzichmo7Kniceu5KOWKD9LiYR5CXhLiBrsl0TDz2DvB5Bs9XGpQPDDHfpwfD2lnXP06omwxzkOuyMp9_ahhVR13U3j8caJXo2pmAF2GKPpEJiNt3kVTFg7hIMa2aLDJlIsLath23CfHBxYVaNIBIwtNOwFVLP7O6CfV4XPsK5nznL4sqa3pe-lQDKhSDu5QgCQgCyDByELpRN5uUKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واشنگتن پست: سریرام کریشنان به مقامات دولت ایالات متحده اطلاع داده که قصد دارد سمت خود را به عنوان مشاور ارشد سیاست‌گذاری هوش مصنوعی کاخ سفید ترک کند تا یک نهاد خارجی که بر سیاست‌های فناوری تاثیر خواهد گذاشت، تأسیس کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/125613" target="_blank">📅 21:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125612">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uz4h8OlUz9uH5yzShHhs0gZZoAy6DmxEkd3Lp5HgHtla4K2kbJFCqkXuIvdphgkfDHJhsKydW0UuOmm8498fRRD9EleomtUvJKyl262--Yp-gBKSJPyoEui5QGBg0Qm1iCoQnMdJoFNUDvpf3S8OBT3MdI2Yb7zyYLHb41kSlDC4EkX6e1whRok6Rr-MzlsrQQVoUSMEaVV8GearzRi1TUO74fGYeUULxsHFwvtX-Rw9BALCb5pFNESWCoLaNoanFRPDY6sE8PLqxhWCq6-uAYCd8CwWHxj1F_QRvm3GRUdvSFhdF4zhd2u_I-sfgcqYXsaOT6ARI-cVke5tTbEw6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار وزرای کشور ایران و پاکستان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/125612" target="_blank">📅 21:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125611">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e82f3909.mp4?token=iwCzCDPCWmh-L-l8tYk8I4iO_F8rRExIeYqFX6rEMwe7nv2jlL0gOtnKpXttOzR9gxMTY4RStWdoGk6-wmmaewCwjHcmGKqVBucqLgOd4nQ_PyAAK8I3ZsjIXN4U2SPVsmAY5E45rkipnP_rfYGuAKRzkuxSByQeW2a_Gj7ppotUtM9CEXWGz5xWd3WVr2I_5JMiqwy-wTOxO5F-gR6fRMP-veljwkQZwF8u23__Vvd85BD33vwlX6jc-OSUqVIQ4KjzhToNM9xihitjh513LcPAbipLIMdJsUDJmbDFipUTevfhvk-yH7fTmwRW12fCc5ur7z0dbD8gCqortMISiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e82f3909.mp4?token=iwCzCDPCWmh-L-l8tYk8I4iO_F8rRExIeYqFX6rEMwe7nv2jlL0gOtnKpXttOzR9gxMTY4RStWdoGk6-wmmaewCwjHcmGKqVBucqLgOd4nQ_PyAAK8I3ZsjIXN4U2SPVsmAY5E45rkipnP_rfYGuAKRzkuxSByQeW2a_Gj7ppotUtM9CEXWGz5xWd3WVr2I_5JMiqwy-wTOxO5F-gR6fRMP-veljwkQZwF8u23__Vvd85BD33vwlX6jc-OSUqVIQ4KjzhToNM9xihitjh513LcPAbipLIMdJsUDJmbDFipUTevfhvk-yH7fTmwRW12fCc5ur7z0dbD8gCqortMISiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بمباران سنگین منطقه وادی برغاز در جنوب لبنان توسط جنگنده‌های اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/125611" target="_blank">📅 21:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125610">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
نیویورک‌تایمز: نگرانی آمریکا از جاسوسی اسرائیل از مذاکرات تهران و واشنگتن
🔴
گزارش‌های اخیر اطلاعاتی آمریکا نگرانی‌هایی را درباره جاسوسی سازمان‌های جاسوسی اسرائیل از مذاکره‌کنندگان آمریکایی که روی توافق صلح با ایران کار می‌کنند، ایجاد کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/125610" target="_blank">📅 21:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125609">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
نیکزاد؛ نایب رئیس مجلس: همه آرزو داریم هرچه زودتر دست مجتبی خامنه ای رو ببوسیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125609" target="_blank">📅 20:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125608">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
نیویورک‌تایمز: نگرانی آمریکا از جاسوسی اسرائیل از مذاکرات تهران و واشنگتن
🔴
گزارش‌های اخیر اطلاعاتی آمریکا نگرانی‌هایی را درباره جاسوسی سازمان‌های جاسوسی اسرائیل از مذاکره‌کنندگان آمریکایی که روی توافق صلح با ایران کار می‌کنند، ایجاد کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/125608" target="_blank">📅 20:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125607">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRI-ID9_O7clmjBDmmQUa2DhmEOeduDBxfvFjxTcjYuTI3eGCjNbgdf__x4Bk7vgSAtLP406TRbB6ss3tSahlxhvvBvP06GtqGeTCD5S-5lCmTmSNAT9WuzFobPReaUC0MXv_X0sUqzUMaVvmDpRhixo8bmZniNdEf4lPjhosp1jfjrdYTepa4YmbrSgS7LmaLavazeoH4p9yefmCF2A5p9JacF4IrJogGqVaK1wveypll8DoF0ZYwiwAfUcEKr7oWCmBsm1q9xQUlKtmfXWLFtvi-aYFHovAh5pkT47Nl1eYoEsmmR7T_7kew6kzxjtNsxUipkF09maZDRcBUTIBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اختلال شدید GPS روی قطر
🇶🇦
، بحرین
🇧🇭
و عمان
🇴🇲
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/125607" target="_blank">📅 20:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125606">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vW3D6YnKe9smVgW_POgn9fvvZFzhmgoTf4PIZ6RyROfJ54UfCejEw7Wi3kU-zI1_P0rtxn2cHQSL7AmmG3sDGxRezKkUDVOpeSFFjUT6YoEzozYhnaYnF9E61v7LRsuARdOyrF34vRorDBixtK_lJD3G3zxsXh7IEIoQUSMar9Uxw1-d82RfcqQfhE9eZw7yDdXqJcobsGqwpvsw1pdLwn7WKoB9UbHq1Kz4n9Q-XuNqz0QaNXRcb84yj12lzIXCag6bhCHi_1epkkYuZ2cwvUuR0s2-CezWEtPW2Fz-oDMSNCy5eBYDHw1iV1UyUwu1Cjct0m26Y7u2C7rlWy3YBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / یه مقام کاخ سفید/پنتاگون، از تل‌آویوِ اسرائیل رفت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/125606" target="_blank">📅 20:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125605">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
هم اکنون ایجاد اختلال شدید GPS در سراسر خلیج فارس‌ و تنگه هرمز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/125605" target="_blank">📅 20:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125604">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
هاآرتص: یک منبع در نیروهای یونیفیل گفت که ارتش اسرائیل پس از اعلام آتش‌بس دو روز پیش، عملیات تخریب روستاها در جنوب لبنان را متوقف کرده است.
🔴
به گفته این منبع، آخرین باری که نیروهای اسرائیلی در حال تخریب روستاها در جنوب لبنان مشاهده شدند، روز چهارشنبه و پیش از بیانیه مشترک ایالات متحده، اسرائیل و لبنان بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/125604" target="_blank">📅 20:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125603">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6ab06f5a.mp4?token=T5AoG0jYCE7M1aXwjsIDNBdglzGSqlN7TjSJdNXkoN1IIj7D6nhFaFHbwFnz2mxAAoeNe3hc6D_tK5l4nRMWXWWjE3T9nS_HLg1tKJGloOR0rXSTazRJtd-_yr7cP_ULdS3ZkdD0fwTyXF0mevo85LLu6O490vvcKXnsC4YXFu0oNzvLU0yGAxBZTWUgqQHGqboasAkI2VD4IwJoy9qWeY5CNGl667VCvAEYyYIvpSsTJB6L8cWY6lAQDXQFqGptamQlc_IsSV_vFw8FLE5y2NRSjbnEMsmW4soMQRiWUqgm90E3uyhA9-LPQyde40440zHIsHjylV4NKBGgziSJlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6ab06f5a.mp4?token=T5AoG0jYCE7M1aXwjsIDNBdglzGSqlN7TjSJdNXkoN1IIj7D6nhFaFHbwFnz2mxAAoeNe3hc6D_tK5l4nRMWXWWjE3T9nS_HLg1tKJGloOR0rXSTazRJtd-_yr7cP_ULdS3ZkdD0fwTyXF0mevo85LLu6O490vvcKXnsC4YXFu0oNzvLU0yGAxBZTWUgqQHGqboasAkI2VD4IwJoy9qWeY5CNGl667VCvAEYyYIvpSsTJB6L8cWY6lAQDXQFqGptamQlc_IsSV_vFw8FLE5y2NRSjbnEMsmW4soMQRiWUqgm90E3uyhA9-LPQyde40440zHIsHjylV4NKBGgziSJlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات هوایی به اطراف القطرانی، جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125603" target="_blank">📅 20:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125602">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
وزیر کشور پاکستان لحظاتی قبل وارد تهران شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/125602" target="_blank">📅 20:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125601">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7716cec2d0.mp4?token=LOWii1Mmri5iSl6JUeZ6m0MXC6fcSlhGB4-PIAQNeV4Y2-KbcSiOyP49oETA_6rNZtRAnylJA8ReA3-QEm1GPL4kSUbSG9sjFxFIcE_NpgteacoY5zKHYmXrf8k5gl8m-C9E74ZfEyZbh7K2ce3mF9JR2WWhAGHAGkTOOXi--ILlBly5sf9wAQ-zvvgwcTsEEL35FwFdCwB7z9aO9stpHDKfpmpMNwyroQOJkff2F45C2euNyi516HTyWBvtmD2a20hCbCh74BO83mmui_puShc0ryCSg6hRoHM_k2QtTyU6QwMtd9KW2OvLlMFnU2CwsHIM6Fq9SwtLHcqZVpEIUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7716cec2d0.mp4?token=LOWii1Mmri5iSl6JUeZ6m0MXC6fcSlhGB4-PIAQNeV4Y2-KbcSiOyP49oETA_6rNZtRAnylJA8ReA3-QEm1GPL4kSUbSG9sjFxFIcE_NpgteacoY5zKHYmXrf8k5gl8m-C9E74ZfEyZbh7K2ce3mF9JR2WWhAGHAGkTOOXi--ILlBly5sf9wAQ-zvvgwcTsEEL35FwFdCwB7z9aO9stpHDKfpmpMNwyroQOJkff2F45C2euNyi516HTyWBvtmD2a20hCbCh74BO83mmui_puShc0ryCSg6hRoHM_k2QtTyU6QwMtd9KW2OvLlMFnU2CwsHIM6Fq9SwtLHcqZVpEIUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرواز شئ
ناشناس
، جنگنده یا پهپاد تو بندرعباس، استان هرمزگان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/125601" target="_blank">📅 20:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125600">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
پاپ لئو : جنگ آمریکا و اسرائیل علیه ایران نامردی بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/125600" target="_blank">📅 20:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125598">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-wWo1x7GDurrzgFKb-MmX7WQQO545vTYeMAjQyyAbc21sZ9W7M6XWfD2R8nzWoVQRBLjlGNOchPtQgtny0o1dpfZVeOb6Xu6Jxub5urB6FN9XYjT56GqBOPFtOUGEyfUsVXsFPcdv2JeUpuyYahDP72iYQ4wqIAYImM3fqdVoGqOJK94wcxj2_V9rgFrM84uoMk9HmK7iEbao_n97oUNPcAQrNddqgWmT3MhOsOSSDw0Lxkk9n57tASuti06Ig15-pp-0EySOsYkwYPuMHYiM96A0rnakGrIqZEKkUYvcsQQD0NMUz3m20uajz8yq8MQ8Aj-ZyQZqrXVmWZK1rxrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d11315989.mp4?token=tOXFshizCv2rDTJYsQIotTelcYOsJV21spv8zmh8pv6L0Ta9HXGZKtrLux35vLJ2z9VJ5oWVrkAsv7nAJVE7KQJ1VA26Kt7pY3TDJjM8h6yajUngOR7f9lox7Op8lDn_bziTHJgPxIa1O5jqPkF_BRhpeENAx5xmKGH61iSeIbzXCnL674JxfdMCd5sza6tNjg97UZawWraEugvIU_Sh_E6H6SXH_nuidFfr4lkttmokYdB6NYmODgVS58yiIqxbdqjQAQ8TvpANSbK-UAF_K7ZWQ313170BiDf2ThfbmEgKt-jmHMLh07rkRr-oAqMkyXZ7ownI9XkZd3xX_qVNhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d11315989.mp4?token=tOXFshizCv2rDTJYsQIotTelcYOsJV21spv8zmh8pv6L0Ta9HXGZKtrLux35vLJ2z9VJ5oWVrkAsv7nAJVE7KQJ1VA26Kt7pY3TDJjM8h6yajUngOR7f9lox7Op8lDn_bziTHJgPxIa1O5jqPkF_BRhpeENAx5xmKGH61iSeIbzXCnL674JxfdMCd5sza6tNjg97UZawWraEugvIU_Sh_E6H6SXH_nuidFfr4lkttmokYdB6NYmODgVS58yiIqxbdqjQAQ8TvpANSbK-UAF_K7ZWQ313170BiDf2ThfbmEgKt-jmHMLh07rkRr-oAqMkyXZ7ownI9XkZd3xX_qVNhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پاپ لئو
چهاردهم
: من طرفدار تیم رئال مادرید هستم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/125598" target="_blank">📅 19:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125597">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: ترامپ ممکن است به مسیر‌های غیرمستقیم، مانند برداشتن محدودیت‌های دارایی‌های ایران در قطر، عمان و عراق یا اعطای معافیت‌های تحریمی برای فروش نفت ایران به چین، روی آورد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/125597" target="_blank">📅 19:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125596">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
نیویورک تایمز: عملیات ارتش اسرائیل برای گرفتن قلعه شقیف، بالای شهر نبطیه از مهمات فسفر سفید استفاده شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/125596" target="_blank">📅 19:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125595">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4rz9RRt3pK4cPUWKYqCtz7AQrneVLzjCF31YOWG7cStpfswYIuk74pB5TpNoUHBOxlQA8PcFk0XWDFFBbLYgx7OAIZi-VHNijb7XEvCJ3fT86_GIwkF4xpVr0oiW6V-7EFMtDhq_sAtQNp8YSdmHcX3-lrZwFiKjTly_3jDvY2RURS0ToUmTIeJ2Jz0Kb0IVCHilNvQZ_8yZO2u1RL_wWR_EW7rwBy3jTdxDqE1UEoELIjcX1J-r8wT4eEORcGCe5y4h8iRCuNeWpKD1oNFybg0jnR4ns9P3MrWdd7Xx5AwDvW6i-iKYgf6Xy6kcCe6qCtwldeLbYecN2DY4PqCyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اولین فروند از شش فروند هواپیمای هواپیمای سوخترسان KC-46 که اسرئیل سفارش داده بود، آزمایش اولیه خود را با موفقیت در آمریکا انجام داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/125595" target="_blank">📅 19:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125594">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ادعای کامران یوسف خبرنگار پاکستانی:
فرمول خلاقانه پاکستان برای توافق ایران و آمریکا
🔴
توافق بالقوه ایران و آمریکا اکنون به رفع توقف دارایی‌های ایران گره خورده است.
🔴
این موضوع تعجب‌آور نیست. در دور نخست مذاکرات در اسلام‌آباد، برداشت عوامل دخیل در روند گفتگوها این بود که در نهایت، طرف ایرانی به دنبال کسب منافع مالی دقیقی است که از نظر آزادسازی دارایی‌ها، رفع تحریم‌های اقتصادی و هر اقدام دیگری در صورت امضای توافق به دست خواهد آورد.
🔴
تقریباً دو ماه بعد، این مسئله همچنان نقطه بن‌بست باقی مانده است.
🔴
ترامپ حاضر نیست بدون دریافت امتیازی که ارزش بیشتری نسبت به امتیاز مالی و اقتصادی او به ایران دارد، هیچ وجهی را در اختیار ایران قرار دهد.
🔴
اینجا همان نقطه بن‌بست است.
سفر محسن نقوی وزیر کشور پاکستان با هدف شکستن این بن‌بست انجام می‌شود.
🔴
گفته می‌شود که محسن نقوی «پیام ویژه‌ای» از سوی فرمانده ارتش پاکستان برای ایران حمل می‌کند.
🔴
در کنار سایر عناصر، پاکستان ممکن است یک راه میانه برای بن‌بست بر سر دارایی‌ها ارائه دهد. یک گزینه این است که بخشی از دارایی‌های مسدودشده ایران در کشور سومی قرار داده شود که هم مورد اعتماد آمریکا باشد و هم مورد اعتماد ایران.
🔴
سپس آزادسازی وجوه به پیشرفت در مسائل مورد مناقشه مشروط خواهد بود.
🔴
آیا این فرمول جدید می‌تواند بن‌بست را بشکند؟ باید تحولات سفر وزیر کشور پاکستان به تهران را به دقت دنبال کنیم.
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/125594" target="_blank">📅 19:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125593">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqMp_ees65R_E6sYtwqlDuqmkl1mmlkNfFYHnhaht7FQU9Y_tMr2ZLT8pttcs8PG6uZjAMFWnr66592p54buCYFKNKptq9RWOvY23Vucn57F64UYed4rdSoRlxFEHgUVJxMqCSv8a2rz2YB6P4KjoJzdcHgHbQ7IpLqDEpIcvxHnRvJLaGCXjBEDMKXj1-8_o0gy5rdHiEwepX27a7Yk2o6i5xJP0eTje5i2aEtgeta-cOVuGXlJzkZXW_HGuGHFJkhQoAVGIrZ8kmvPCwyWPi90BAtnsBSbZJ6pVMb9-_wGPM1eoPc43sIVTN-kncknkoqwhiUPA1JViZ784TzVLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل همچنان درحال بمباران مناطق مختلف جنوب لبنان است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/125593" target="_blank">📅 19:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125592">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owGB279abAVAqHLXnAHdgWXfring-QwfWf4W7RPjFLN4jVPg9Oahg9pIVl6d0MFw4woLjFUK1L66b5UoanMoi7yN9qMCULFDeqay4u0Ym7CDg5FAuAzn8Qu7cjPQLBQGG5EEpcLQymeiQxBr2XaQV1w7O1PfKdo_IZ6mjfLSdNVjc9_FUXTzNuhWwDjgkith2aZ7kx172ytXWohrz6CUq8H0GnLFa3jDVctqL6tP1ZjY8m8AjEonh6uIAv59mv1Uz76zBhqcPne9kGx53tREJungaRuJ9baMJMTSevU0_e_Ffd0SYlEJbdbkM8PL1cH04Z3oGZMGB7gVWuxirNP_lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
از سال ۱۴۰۰ به بعد سکه بازدهی ۱۵۸۷ درصدی داشته و قیمت آن از ۱۰ میلیون ۷۶۰ هزار تومان به ۱۸۱ میلیون ۵۰۰ هزار تومان افزایش پیدا کرده در همین بازه قیمت بین کوین رشدی ۵۷۹ درصدی داشته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/125592" target="_blank">📅 19:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125591">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
الحدث:ارتش لبنان اعلام کرد که فرمانده آن به دعوت همتای پاکستانی خود، عازم پاکستان شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/125591" target="_blank">📅 19:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125590">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJJRYiSyfFTB0ROhwsQ1Hk2EJWyQU13MsErg2lTR2p2Cq8kYpQ1u-H31AIJoRdhFv-vAzKYsS_LxKYl375Z_vQpCXMLMrVL6xFqG2_1L5e9heqqWeWAVYNOFWD8wPhtmBG7oynFFcJzhaNCJP3It_3Nq6O-ShA7btis-bo51WwLplLJQUMv5Fw1NI544m3aLSJIgpgXPi_5mBgy2c6SKSrIZGn_RzhiOAzpvVilLS1-zfKIpH-nq_NpXuI8lE990Fid8JKw4LP_Tapg8t5QrBaR9h9K1RsorfJfGkVA4m3SKQ7uejz-y7pNDTOoVxS_wOWeieln67F-4WuajH-MlIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت: اینترنت را وصل کردیم
اینترنتی که وصل کردن:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/125590" target="_blank">📅 19:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125589">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
الحدث: ایران خواستار مذاکرات سه‌ماهه درباره جزئیات پرونده هسته‌ای است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125589" target="_blank">📅 19:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125588">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbrPO74WHvEpV6hyDADRwjmrzxu4NQq5Xz6yCzQGYa8hI1D8pUT-x60jT5VtixMO_GQ1xk6bO9I-8n9Z8LDvxYb9gH_Dkio1jUbFBY3xKC9ovrKvQhWL8D2gF03mYvyPdG-qLhP8ZHTXI4aaEEZfVdCbUKMW3bfyT2XqtSbok3FOX6QwU3V0isbdS1CK9qFFdpJOJ7MRDc_U833Lx7HBkAXVC94jR_0Cin03iaHlcsScyPbs7JwcPo-A-aJn4elwCq6mtiFJKDc8Tzt-noJ76VbpmIt3NDEeKSWibV699AVeU05Eh0_bDBvuyxvNWd-hHd-H_wFWbGmIUw5TZmI_YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انفجار قیمت مواد غذایی در یک سال:
🔴
روغن ۴۳۱ درصد گرون شد؛ مرغ و تخم مرغ ۳۴۲ درصد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/125588" target="_blank">📅 19:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125587">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✅
با سابقه ۵ سال فعالیت مداوم
🛡
حتی بدون قطعی تو دوران جنگ
🔥
آتیش زدم به مالم به خاطر عیالم
😐
بقیه هنوز VPN حجمی میفروشن اونم با قیمتای نجومی
🚀
ما چی؟
💯
💥
VPN نامحدود واقعی فقط 190 تومن
🏷️
💥
بدون محدودیت حجم  @NetAazaadBot @NetAazaadBot</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/alonews/125587" target="_blank">📅 19:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125586">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rBFZshkGRi9wRpRFAC5NLi0BhPKlY2J4pBJp9i_oma8a5bsv19MwtRO_IekhC1TmXlOEBP9JxLE70fhjBPKT8ICost6wkomRGjoFJiP5MyB3tRIdSzgnm-WmCbcODAV6l7XjX1mSrlyQirFdX_jbG5AFhF5cDM7foP4luV4njgs_gD4XoNQ8Uk1SN_U2v65MNqIl5lsYQ0IZXnZ-XIK8cDkP9Y-DjqZpIvsejiz6qmJYiDXNm0YlCAmtud-cEiPTXzWXG9fqzmM-41iCFtwkJG_1rOn5DY15mq0nCobfmXajtPFt0gV9Mmjsus6nnAmlL-G2RRk1Nra417VJGFF-6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با سابقه ۵ سال فعالیت مداوم
🛡
حتی بدون قطعی تو دوران جنگ
🔥
آتیش زدم به مالم به خاطر عیالم
😐
بقیه هنوز VPN حجمی میفروشن
اونم با قیمتای نجومی
🚀
ما چی؟
💯
💥
VPN نامحدود واقعی فقط 190 تومن
🏷️
💥
بدون محدودیت حجم
@NetAazaadBot
@NetAazaadBot</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/125586" target="_blank">📅 19:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125585">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsepzILsJEsg-2oL1gZOW3tWD7faUmxfaD9CoX_ILSWZRGqJSTgoK0wlsKz89xBDqVmfgS1DtAq4PWR7pSRsa8VsGhqvIDfcTBW80-0UsbTgfl7nI50E7jVgX1P-7Ab9SCYJWFYMI0PAO_3UngChOBNBJR9pmEEQclDR2q-VCrClPrc-33ymZMRer5YUQQFhn5RoZ0BHmwh33RKdF89b6pFwZ7EAVzkK846Yswa3mPRiS7On9Xf-b_pok5PKXDpev0LjnDO48PpCwyI1cFOGFPDWLTzC2i0fMCvEtRuriVh8pdoOk6eVhwZbZdPBswylIez8xjemb-9GrDVsg6o1_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات اسرائیل به لبنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/125585" target="_blank">📅 18:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125584">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
سخنگوی دولت: اعتبار ۲ میلیون تومانی کارت امید مادر به حساب مادران واریز شد
😍
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125584" target="_blank">📅 18:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125583">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d72c112b3f.mp4?token=pQc_lxoLmKApgecIZx2c3YKtv4aZ9bgmnnQ8qYaIugDN_CSQuJukUo0DKuQFsgiX5A5bsf35MrvlksvsSM0Uzx4EUezrFtTCPg0nPKEHAld1gFO0x_1T8qMvZcDQRxnOnEYrjtOREPZtjgdaWTowSd8G_7tEq4F8hjHqU2sYJ_5PVNDCF69cTHwe6mrPZbqYObVo66Q7iso89wONgXPXunRp8W9pL8hlveV3z4t5LhwKWRhvotvC9ajVUy0jIEW80qs1e4n2suxfXgWDTsNOfo11HN0F09X8y3tTvUOxDyVZo-ikE5h0h9fwcI5Kxo1xuUfcr3A11zktZJpqrVuIfEPERuQ_Dy-zyC6r2Ll1xIop35pf7xktntImDCughng1DUhCFfpiPodILO0nI0Vv0Wac---gkMs92tOoKusuVV40FiLdTlzDjhtRX8cfG91uI0wFCt1s2HF76IQwAdn8FiZJOvyJUxdhhfBLAbkM_6-gVE1hA9MbaO8aKWVs9I6Pt1ot1eptd8oCHVGF25ErSVk5wGvU_gS4eURH_L7xVPrxXve15oyhH5YnT9Ej6ORGHufSf6PbyZqbeNZyzV40KKruvLGcr5croL4Kks6ctaROIlfRV5BsrvZawfjTBLvnIxmCcYlv4S5aGbXZzhRCIsumQOq9GSU5xP5P9mJ5UPs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d72c112b3f.mp4?token=pQc_lxoLmKApgecIZx2c3YKtv4aZ9bgmnnQ8qYaIugDN_CSQuJukUo0DKuQFsgiX5A5bsf35MrvlksvsSM0Uzx4EUezrFtTCPg0nPKEHAld1gFO0x_1T8qMvZcDQRxnOnEYrjtOREPZtjgdaWTowSd8G_7tEq4F8hjHqU2sYJ_5PVNDCF69cTHwe6mrPZbqYObVo66Q7iso89wONgXPXunRp8W9pL8hlveV3z4t5LhwKWRhvotvC9ajVUy0jIEW80qs1e4n2suxfXgWDTsNOfo11HN0F09X8y3tTvUOxDyVZo-ikE5h0h9fwcI5Kxo1xuUfcr3A11zktZJpqrVuIfEPERuQ_Dy-zyC6r2Ll1xIop35pf7xktntImDCughng1DUhCFfpiPodILO0nI0Vv0Wac---gkMs92tOoKusuVV40FiLdTlzDjhtRX8cfG91uI0wFCt1s2HF76IQwAdn8FiZJOvyJUxdhhfBLAbkM_6-gVE1hA9MbaO8aKWVs9I6Pt1ot1eptd8oCHVGF25ErSVk5wGvU_gS4eURH_L7xVPrxXve15oyhH5YnT9Ej6ORGHufSf6PbyZqbeNZyzV40KKruvLGcr5croL4Kks6ctaROIlfRV5BsrvZawfjTBLvnIxmCcYlv4S5aGbXZzhRCIsumQOq9GSU5xP5P9mJ5UPs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک روحانی:
مذاکرات
کصشره
و آمریکا قصد داره سنگین حمله کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/125583" target="_blank">📅 18:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125582">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-4cLTon10A3-C889mijt9dXtz5PIgvdMAAbsG-TWyDqERnrZlUWsarG8NV8L0WHthL4r-5Q_8x6VwJ4zj8U62vwr1xiS3FFhUAyb1Cv1la9NPOaH25PEnzvI8wA_GfgUx0q1tJPuA-fFQBJWRcDm2z9rE-q1HPOMqdrqGo68EhX-H_jJll0pBHOWJabQhUgif9gGmojllTt9Yebv4U5hBmQ72Nz7NnmYShIO4-kIDFhLBWfi4gq3wiyvvDISAGAwYDQ5SyTczLM4MsKxhJmoosAfVzuRhqbvBZjWZ9364I-EX_hCOooeiDgUJquhZJ6p02Ln5uGjSNL8je5EgKuEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیکزاد، نایب‌رئیس مجلس: همه آرزو دارند بروند دست رهبری را ببوسند ولی چون ممکن است دشمن در این حین بخواهد اقدامی بکند، نباید این کار را بکنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125582" target="_blank">📅 18:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125581">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
العربیه:
ترامپ به میانجی‌ها اطلاع داد که مذاکرات با ایران بیش از 60 روز ادامه نخواهد داشت که این مهلت در روز های آینده به پایان می‌رسد و ایران باید به‌سرعت پاسخ دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/125581" target="_blank">📅 18:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125580">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره در تهران:
درگیری‌های ایران و آمریکا در خلیج فارس بیانگر وضعیت «نه جنگ و نه صلح» است که تهران و واشنگتن در آن قرار دارند.
🔴
طرفین آمریکایی و ایرانی در حال مذاکره برای یافتن راه‌حلی جهت پایان دادن به جنگ بین خود هستند، اما آیا می‌توان گفت که این وضعیت به همین منوال ادامه خواهد داشت؟ قطعاً خیر.
🔴
هرگونه نقص یا اختلال در مذاکرات می‌تواند این درگیری‌ها را به جنگی تمام‌عیار بین تهران و ایالات متحده تبدیل کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/125580" target="_blank">📅 18:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125579">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPaSVAKEJJPVhX3GqaxakYxemrzQ7aCs8U9BilDPcummMa77Lq4s8H65FhTTuiq09Om02yrthdCS1Fb8eN_DRTiy-RtxO82-wAFA9gbQzm7B1OBqfXt9o-dJoqDb63ys2C___NYhu83KbUcLlhdR66icLR4E0qDXiffOvayIs9sZqTUZqjC2n46GrsofEwvfguPYLOR-hdPt7gFAWN72lhO3NrYvguc-mHk7EpqzV-el6BfZl588mBwyDkF_h1v8rplIz9JHCrqOFMbgfkw0kpFjN1JdqaFSw-GFcoNXNRDQ_B9CPseTBDbb8jOgeL5EInXIjPJy86wbG0d2_OsloQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت برنت: ۹۳ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/125579" target="_blank">📅 18:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125578">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
سایت آدم و حوا که دختر و پسرا مشخصاتشون رو توش ثبت میکردن تا پارتنر پیدا کنن، اعلام کرده بزودی قراره زیر نظر وزارت فرهنگ یه قسمت راه بندازه تا داخلش به صورت ویدیویی پوزیشن های جنسی رو آموزش بدن!
🔴
مدیر سایت اعلام کرده که پوزیشن های اسلامی و مورد تایید رو…</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/125578" target="_blank">📅 17:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125576">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nj-xv3u6pTju7sxulnu4DklEtru_jz9bduEeCVlDrHPHSI5zjB65ZPaFKOf5v0ZY3pi9n0R9biS9WVct1UAanQ3Ufut-yfRYG2Z07jobjvBJcJGNb4oRoU5NGOBCIZEUKvJvWGAY93eyBrbvHjcwp1iL_Gc1ukRyZjjPBOKKMJkTDSgjORnL3dlo9T4UenAmAmOCockXeP7D5vEJBB68xkpmH_FJPBUgw6eczfzrK3L-gr5jOMzZvE4Fs_aJm6qNGGSQlqRaBV81ViodYHS4wVU47K-Uo06e2R-n4yf8KKX-FPSzKU9BiNATBWTXQQf6U7XAK7W9KStGS30hQUeYkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PBAugxUOBSMZ1Yede0_Fzqu-mGGVKyX0Sc60erel-56GY959nrEagV45oyKAtYdtF1MkQMvX0Tqnp1lNrS89qOYDjafKvn-c45USxvDz56dqg8FOb6oW9n_I9oZk47J_OTuVy9gtFEEPgbtnBiGG5BoAast4aT1V6SQkpU8Swr4hyeWX88iSGqAcy_sVOF4HPB24LkUfgIdb7XG3AdV6mE2fC7AlKPVfNLY1z2PikbO9iyk0hWwI9XTF7a1DZ8beArqfRjfQLnlWsXRDE-nriqqUJp1N8_4KWOVibpik9x9rrPPOjJkIHf4X_GrNazOaO059X7Jfw1uDZrcjqCxMxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
سایت آدم و حوا که دختر و پسرا مشخصاتشون رو توش ثبت میکردن تا پارتنر پیدا کنن، اعلام کرده بزودی قراره زیر نظر وزارت فرهنگ یه قسمت راه بندازه تا داخلش به صورت ویدیویی پوزیشن های جنسی رو آموزش بدن!
🔴
مدیر سایت اعلام کرده که پوزیشن های اسلامی و مورد تایید رو آموزش میدن و چون سکس افتضاح ایرانیا باعث طلاق شده قراره اینکارو کنن.
🔴
گفته میشه این سایت زیر نظر دایی حسین یکتا است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/125576" target="_blank">📅 17:55 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125575">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78c3ae38d3.mp4?token=VbizpjOqa9Sh4YKgGiSyuZAfFaf_QH-tLUgH9lrbiAqbkCwQXRQwY911dWa0PihnF4VnFbp615n4eRknTWUbWhGUJgImRnaNYRZtOw-P_cclnq3lcMhpz0onP420RshLzWdYnJTuLtRzxbH-ss7lpK2jS-W8Nx7mNC2hEQDEuwbeBva65lk60hkQLxaIBeAkGDrww1abf69bns6yrAE31kzLznHMyoCt0dNG6GHuJM7qJmzxhxSAhb3UZr9E2b2QzwzcTYFFlRAtb_elcdPDtZP1y9nNcoymkBsyVTi4MQarxAmQ2wf7sfVp2Ud9dvqRHIhacEHOlNAf9DLJVvWFwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78c3ae38d3.mp4?token=VbizpjOqa9Sh4YKgGiSyuZAfFaf_QH-tLUgH9lrbiAqbkCwQXRQwY911dWa0PihnF4VnFbp615n4eRknTWUbWhGUJgImRnaNYRZtOw-P_cclnq3lcMhpz0onP420RshLzWdYnJTuLtRzxbH-ss7lpK2jS-W8Nx7mNC2hEQDEuwbeBva65lk60hkQLxaIBeAkGDrww1abf69bns6yrAE31kzLznHMyoCt0dNG6GHuJM7qJmzxhxSAhb3UZr9E2b2QzwzcTYFFlRAtb_elcdPDtZP1y9nNcoymkBsyVTi4MQarxAmQ2wf7sfVp2Ud9dvqRHIhacEHOlNAf9DLJVvWFwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
استفاده از جرثقیل برای تکان دادن پرچم در تجمعات شبانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/125575" target="_blank">📅 17:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125574">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vj1jrNtuZG3r0p3lSLSgUwxYM9jEgZezcPuwV63FbqOclnzkC2PI87yX_tKVoy4ZwK6jm_dEHJO-On7SPpWRhg--vayYJBtuNZJfmVNW8ub1i5CxMl5us2jBQCiTTbzMbMV_AGQQWkMDLrVHX6kmjtG5vKh11hHpWkLzmhUuhD4gH-osm6Z5jtivB-Sg-UJsh5HIXHpDE4zK5cyPGPedxa2jlQynLTdJY1y795_0JfZO5FU-QUjiHIiryzcPgpzV4DgiKr_tEjEfqMz0TWR9qh5iBmMu_ZtlfYMqvBlaAqPlesxV3rF7-8jo9JIp1P193KLxWVETCtOzmlMhks4vMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیصر، خواننده انقلابی: نظام ما یک تنه جلوی امپریالیسم ایستاده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/125574" target="_blank">📅 17:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125573">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVnsT6JxGDis2HrU0r2UcQvkFJNtAQGTkj_3FPpenFmjWt5OUcMz9dlgnmoM_xbe-UjXVF1PmCHiCBFQN8YvXcQQHISAWMuRk8TYbPrH17YzLp95LYL8h6SRwczQBu0zukCAV9hDIhkiZdaVkjb_DILI31At79A4PZWhm_Iufbt6t5mZIJeAJG3oMBiTKUNuBS7bPXFnPQB-Ge3HPenGnKx1A80fWDo9tHJGrdDJUv5exN-2zpds7dbR1rA7clUezJIwbnozaXpHEn21Qo2RwALfTTLw7OWJ5AENPhqsf5An2_cJjDoXEg4ea1aUTwVFuXKKYyMKCog1RwHxky6nGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خسروپناه، دبیر شورای عالی انقلاب فرهنگی تو شبکه خبر رسما اعلام کرد که تاثیر معدل یازدهم تو کنکور قطعی می‌مونه و قرار نیست مثبت بشه
🔴
پ.ن: دانش آموزا یه جمله به خسروپناه بگید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125573" target="_blank">📅 17:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125572">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcc2ba7680.mp4?token=fxXZ4igpyQWRCPzxV4fbH4T7eVs4RUHEpo4pOLZcNgbz88dlA6eQmGZiYoPGfqorNuIbUkIePerAtVMa5TECTb2FKc1NsKP6RvDYj6Gm-RDUSpPxajDH2CCYx3mtKd6J4zVTYfZOweq3I7SoLEQSKKNNqzP3ciT-xRs9Joz5veZO79Xko-KfDstXUFZ7Tnji6gqNP2zNNTP5Ven6d37VQVdaP48qYCyMPHWXYi8qYcSfdOBiNxMM3mPl_378AtW6rkzdUhM7TquDtlTdu4n8CEkbWMyUes4TbKnEmQct4GU1-zTp56xJkVJ4t4znPS2ezJPJi_-5kyN9QITQdb91SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcc2ba7680.mp4?token=fxXZ4igpyQWRCPzxV4fbH4T7eVs4RUHEpo4pOLZcNgbz88dlA6eQmGZiYoPGfqorNuIbUkIePerAtVMa5TECTb2FKc1NsKP6RvDYj6Gm-RDUSpPxajDH2CCYx3mtKd6J4zVTYfZOweq3I7SoLEQSKKNNqzP3ciT-xRs9Joz5veZO79Xko-KfDstXUFZ7Tnji6gqNP2zNNTP5Ven6d37VQVdaP48qYCyMPHWXYi8qYcSfdOBiNxMM3mPl_378AtW6rkzdUhM7TquDtlTdu4n8CEkbWMyUes4TbKnEmQct4GU1-zTp56xJkVJ4t4znPS2ezJPJi_-5kyN9QITQdb91SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یادی کنیم از روزی که تو صدا و سیما گفتن ناو آبراهام لینکلن رو زدیم
🔴
فقط اونجایی که آخونده رو جو میگیره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125572" target="_blank">📅 17:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125571">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d397f35c8.mp4?token=eTGI3XvnUwSF02g5kO3PlOloEnrScknEqzUwpftbvUxOIn88N76oyV6pwyh9VutgAzGYT-cCfOBY9xCgKqs1A8Ij28e0mPBkaXGv_Ikjf_pdtIcDc17NuZiqiOKvR1UGAd7X3GJRPO9CrSnemae6sSm5lb3ew6gOEgW9K2G8iLUDR_104i6aSl7wTC3F7BZTFCi_C3mZq5gx7Ud-f5cCLWZqw_JaPnM0HGE0aMX-y24xwkHYTeVkYoGmIUcGvGSM7EIFTCFmDwPYz1QXw3roqgd-8zFIdGZFRfXMpdQCKFGc8dh7AJCepsGqZSr53TaSpcfhleiu3lJSsAIS9dw7Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d397f35c8.mp4?token=eTGI3XvnUwSF02g5kO3PlOloEnrScknEqzUwpftbvUxOIn88N76oyV6pwyh9VutgAzGYT-cCfOBY9xCgKqs1A8Ij28e0mPBkaXGv_Ikjf_pdtIcDc17NuZiqiOKvR1UGAd7X3GJRPO9CrSnemae6sSm5lb3ew6gOEgW9K2G8iLUDR_104i6aSl7wTC3F7BZTFCi_C3mZq5gx7Ud-f5cCLWZqw_JaPnM0HGE0aMX-y24xwkHYTeVkYoGmIUcGvGSM7EIFTCFmDwPYz1QXw3roqgd-8zFIdGZFRfXMpdQCKFGc8dh7AJCepsGqZSr53TaSpcfhleiu3lJSsAIS9dw7Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ
از خواب بیدار شد و تصمیم گرفت یک "موزیک ویدئو" تولید شده توسط هوش مصنوعی منتشر کند که نشان می دهد همه عاشق ترامپ هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125571" target="_blank">📅 17:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125569">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OmaXeF1KxkN0pKmmR5JW8hfo9xyxdz4HyeBG6cafrM2L8WiUNRIuZ3Q3xnBCiJmUav4DoIBMx1pTTXSN3ZvQjm7lMpcqRuDmcCGV3bFgIdVAQQ-AtqanyAIcWfpmaUHZaJ6J7QX72DaNMda3l5VUZIvb36Z3rZ7diPZCoqJEYVx8K502KJsrp7KuZ3DERwV1PEPPR2LqDS-i1nyzPB38zvjTNDdt8ub6FYUhUWotAqTUaZ3ZgId9tQ6ZvwdCSqwjOJPYpA3XunUP41o1PZr5LFkzRmF6aNebCO3ljv9Li1WKreum5xLFfAhMuVH1TpizPnHV7ZGTWxr0yNV0eSWpww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HbYX08rcNf53YpKhtJVzKPKmo8-VmHFMcG0k6o7mNSwmqq3W1fvPpKnCwz_wPOI5UXTaTyOHSTUbK-xbYve3a64lok-2X08cQsA8W8xYHPvSEG8hcmdCN5MQ_8TQ-W7Mp577FxQbQ42-GHD5UmlIgiloMGvgV-brMva4nMiLzUAielrK5IyivRUvH8axjGYoTu2QGicNAtdkcsyXdNK8K3zu8GwlCLQRTpVSBGvDA8UsERerU8fPqegZiRENe3O4pIV2O1OmHNYjJyVRPc1L3ubrGCy8-BBnL6pzKwUYAUp5gKcfLuEIHcXDRf3SxSI-IRut16MNLQRYtSFMP3cRlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تئوفیلوس سوم از اورشلیم، رئیس برادری صلیب مقدس، در دفتر بیضی با پرزیدنت ترامپ و در کنار مشاور ارشد مسعد بولوس دیدار کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/125569" target="_blank">📅 17:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125568">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuo0BoicIyOp-KWdu6Kb5vSphjXk3TDG__szZDyecu4PEVwx3aH9SIc5S-LdBWjIj_S2pnlfAOFjc_oWE7IB32XVIV0CfqYqLjX418efdxVzA4ELiWxgXupaLPdp-hLKxEGwK-ksW4KtkaQpzdXVwgtBA-M9UJJCtXPYDwibdl8PuKEYWDQ2rPqPUz-vChBhhdHsHjVxhH4OX1l1N1QItgkRViK7h-xLaCnLADZCcjKxlTsrlHQS3kQN73pW6ExJL7hL3t6h5QDkTupujLlCE-Y3QdiEjlK5iQqgju0mSRonWO8oMWXNda8VmCLse0pHXU45qpe0wiNs91iu0Y6ksA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/125568" target="_blank">📅 17:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125567">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
ترکیه در حال توسعه یک شبکه دفاع هوایی چندلایه موسوم به «گنبد فولادی» است که در آن رادار، جنگ الکترونیک و سلاح لیزری به‌صورت هماهنگ برای مقابله با پهپادها عمل می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/125567" target="_blank">📅 17:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125566">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfMeQ9sUrEhuIrL6i-J3VUUxdw2RVs_w2McpKU-RagOpm82MbM-pBHBUSKGEdbRkGSrs_XJc5wIJx2taMltTk0sZyAWD7L0_dkwjT4OTSvW6wfR4N8m3ZMk3D9zEMTfpIDP2yCYUQI7KXmG93FDcJpJGDcTT6jdcAgiAe8D0g0Axot7LF8aJNj5OaRWw5cBQHKvUljFdscKkGqXrjtvmszSU_oM45XXeII1TTsQukWVcHvTn9v6230KzvpBUMqhugfITHaUG4IgqqOuZ894AnYfDyCJwgYTYuem3mpU_CYvM-AHWVS5ylF1oCHjjreBoR955oQg0TY_ij-t8Bhs0MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جهانبخش: آنطور که من شنیده‌ام کارتل‌های مواد مخدر مکزیک، ایرانی‌ها رو دوست دارند و گفته اند مشکلی با آنها نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/125566" target="_blank">📅 16:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125565">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
وزارت امورخارجه برای بار هزارم، نقض آتش بس توسط آمریکا را به شدت محکوم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125565" target="_blank">📅 16:55 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125564">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AD-zTx42vO1MhcWJKkBVYrA_EyufOWDLQ9nDgGAUV2r3mjH4OZHzXgwvEYHwsN5vf3dnMBjbGhPkcsG8-bGBsr-GG9Roxs6N2iAQCr0u1Ezj3W11CRxNjgyt41dlzr1Tm4rPiD5gzRLU_vMBSjDyOBb3PwEtNWrjdOqEFcLCz50iD3RsC-qp_8gFsR6XCviFFoH2E8SkXeo0WVG7gpj1rVRVQpGehhNd42tHu-vU88sApCLV59PK7eok2OuJYiGcT1Gc8K-Ixd4BmS35uyZRz7pSDDEybPDAqH56YCEbbEAVlWbQw6WTZypR0prLDLH24QbMmk7F5jFj6vDUfcRaqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفع بزرگ اقتصادی چین از جنگ ایران
🔴
جنگ ایران و بستن تنگه هرمز، به صادرات تکنولوژی‌های پاک چین مانند باتری، خودروی برقی و ... منجر شده و به ماهی ۲۰ میلیارد دلار رسیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/125564" target="_blank">📅 16:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125563">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkFwQ4iCK-FQgq-AusIJrUp6p8qnfgrJGG6Qf6v2X1j6odwDDpQZuqy94644eW0tSPxHel_IaTPHf-bfVtFSMgcFKvQrOC6v345TclHw6BUjnhYE_OURQTeAPziK3UQoPm1YMRNAaMSQvIO5IhnyfibfBS3Gyt9EkZSMN8HUfdavyv-etJuIIYnAHlRWzgOAIJaA_GRIrMlC-6SZKb6bv_fSdqmfogEU3UXeOnKhTY7KU_vKO9EG1Y372grGVIAqym28NeOvhS1Y4QsLfv3vvKATtjg6bPUKFzwyKGHNzmD_z7ZKGoEpGS0F7ci2pFjvltu_udjFfETxTgbhXbhPiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار وزیر کشور پاکستان با شهباز شریف پیش از عزیمت به ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/125563" target="_blank">📅 16:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125562">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
پست ترامپ با عکس‌های خودش و آهنگ : ترامپ ترامپ ترامپ، هی دونالد ترامپ...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/125562" target="_blank">📅 16:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125561">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
مسیر غرب به شرق تونل نیایش و پل صدر امشب (۱۶ خرداد) از ساعت ۲۴ تا ۵ صبح مسدود است و مسیرهای جایگزین، بزرگراه‌های حکیم و همت به سمت شرق می‌باشند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125561" target="_blank">📅 16:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125560">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
خضریان در نامه به عراقچی: صدور ویزای ۱۳ کادر تیم ملی در بالاترین سطح دیپلماتیک پیگیری شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125560" target="_blank">📅 16:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125559">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
وزارت خارجه کویت در پی حمله صبح امروز به پایگاه نظامی آمریکایی علی السالم، بیانیه ای صادر و این اقدام را محکوم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125559" target="_blank">📅 16:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125558">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
وزیر کشور پاکستان، لاهور را به مقصد تهران ترک کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125558" target="_blank">📅 16:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125557">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
وزارت خارجه ایران: وزارت امور خارجه موکداً کشورهای منطقه را به رعایت اصل حسن هم‌جواری و پایبندی به اصل بنیادین حقوق بین‌الملل مبنی بر خودداری از اجازه‌دادن به طرف‌های متجاوز برای استفاده از قلمرو و امکانات آنها جهت طراحی و انجام اقدامات تجاوزکارانه علیه جمهوری اسلامی ایران فرا می‌خواند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/125557" target="_blank">📅 16:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125556">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
وزارت خارجه ایران: نقض مکرر آتش‌بس از سوی آمریکا بار دیگر اثبات می‌کند که
این کشور نه‌تنها اراده‌ای برای کاهش تنش و بازگشت به مسیر ثبات ندارد،
بلکه با اقدامات ماجراجویانه خود امنیت منطقه را با مخاطرات جدی مواجه می‌کند و
مسئولیت کلیه آثار و تبعات ناشی از این اقدامات غیرقانونی و نیز هرگونه تشدید تنش احتمالی، بر عهده دولت آمریکا خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125556" target="_blank">📅 16:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125555">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
وزارت خارجه ایران: نیروهای مسلح مقتدر جمهوری اسلامی ایران در چارچوب حق ذاتی دفاع مشروع و با هوشیاری، قاطعیت و اقتدار کامل،
پاسخ متناسب و مؤثری به این اقدام تجاوزکارانه داده و اجازه ندادند که اهداف شرورانه طراحان این تجاوز محقق شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/125555" target="_blank">📅 16:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125554">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
وزارت خارجه قطر: ایران نباید مدام با حملات بی توجیه خود، امنیت و آسایش منطقه را برهم بزند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125554" target="_blank">📅 16:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125553">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce4f1fac45.mp4?token=AVrxzw63V8MGpzro5jTG5AqQTTrrwTU5QxYDTrqy0Yl-8LhK9rZDJhWkEb-Av6WOSiKBnL0iORaIoORPscIKKf_IdX8e9rHHXcva62DTsBvhyKg2BAtFcy5MEncmLlmF4IRKoOU_sgc6vbwQvQEjfvSKfW_9wyCvG7ey4_nntEyGCM2g66v9jxG29NUMQuG1OGa8Wy-812nc8YNhfd1CTpTGjOxpYuzCyKTFnlICTp5dME6bvpzYKtoODkse4AkMv1ZggsWYceA-tUMvUUq_tMyqBx0ZblMQ1OT-70MtgxK7dsDRDMzktcE7LX0vb6ekvOp3t10LobzHmClfR82EGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce4f1fac45.mp4?token=AVrxzw63V8MGpzro5jTG5AqQTTrrwTU5QxYDTrqy0Yl-8LhK9rZDJhWkEb-Av6WOSiKBnL0iORaIoORPscIKKf_IdX8e9rHHXcva62DTsBvhyKg2BAtFcy5MEncmLlmF4IRKoOU_sgc6vbwQvQEjfvSKfW_9wyCvG7ey4_nntEyGCM2g66v9jxG29NUMQuG1OGa8Wy-812nc8YNhfd1CTpTGjOxpYuzCyKTFnlICTp5dME6bvpzYKtoODkse4AkMv1ZggsWYceA-tUMvUUq_tMyqBx0ZblMQ1OT-70MtgxK7dsDRDMzktcE7LX0vb6ekvOp3t10LobzHmClfR82EGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فیلمی از ۱۸دی خیابان سهرودی تهران
🔴
از سری جنایاتی که جمهوری اسلامی با قطعی اینترنت در صدد مخفی کردنش بود.
🤔
عرزشی حرام زاده این مردم تروریست بودن که بهشون شلیک میکردین؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125553" target="_blank">📅 16:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125552">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
شبکه ۱۴ اسرائیل: همه امیدوار بودن که آتش‌بس دووم بیاره اما ظاهرآ قواعد بازی داره کاملا عوض می‌شه. خودتون رو برای  آخر هفته‌ای داغ تو خاورمیانه  آماده کنید، زیرا ایران و آمریکا درحال گذار از حملات پراکنده و شبانه به رویارویی‌های گسترده در روشنایی روز هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125552" target="_blank">📅 16:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125551">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9995675c84.mp4?token=E-9vJt_GIpQOoaiR8GnJgqFsPiOTSwFMc-yxB648a_XDeEckhWpUnl76gYljW9JZQHWQelMKDw-XaoOhjSfleyZzXheLD_EuPe_FnuGs-gJfpMu1b4nUUBBiVKPKEct1i8RdIPC70GRxccebOP0RikbaStHo96P_UurS-WKREsXezWL2-oD4G2LIstxJakGpv6vF6PV8nzji8W4psRiLdTS35O0q2TUaFwdxnIA-VRqAOMqUSAoZDsHgjl3LrPFa-ZTmO5x92Mc7BoNeH_HwmSeXatO3qNkRFkhAKdFN0piykoi5jsFwrScPhHr0pUZZcy2sv7H5l0p1CtIRG41M8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9995675c84.mp4?token=E-9vJt_GIpQOoaiR8GnJgqFsPiOTSwFMc-yxB648a_XDeEckhWpUnl76gYljW9JZQHWQelMKDw-XaoOhjSfleyZzXheLD_EuPe_FnuGs-gJfpMu1b4nUUBBiVKPKEct1i8RdIPC70GRxccebOP0RikbaStHo96P_UurS-WKREsXezWL2-oD4G2LIstxJakGpv6vF6PV8nzji8W4psRiLdTS35O0q2TUaFwdxnIA-VRqAOMqUSAoZDsHgjl3LrPFa-ZTmO5x92Mc7BoNeH_HwmSeXatO3qNkRFkhAKdFN0piykoi5jsFwrScPhHr0pUZZcy2sv7H5l0p1CtIRG41M8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سپاه فیلمی منتشر کرده که نشان می‌دهد  آن‌ها بامداد امروز موشک‌های بالستیک به سمت کویت و بحرین پرتاب کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125551" target="_blank">📅 16:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125550">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e63a2b05.mp4?token=UfP6-A9sEoUgHp7GQbZ3Nw9R7tS4TTqie7v0PCfqKzMpbbgMbIya5Gd1LNoDCNtxi8FDLrTn05Ua1FO8Tlwo7MhBcnNdrc-IK7xtpNAbw4ZI4uKojfDZk4lF0LGc_9sHvTAd5ENsIUsxYtoBSNh-p0Gks1IV42pnoC7oLhV1F0iQF8YosKDb0r1CWs6oVDPV_DMv-jdYWD9nwJ2xLcGtIiadusxGrPTdV7xUdZctTy3qM4kQnVtNg3SxvUca9jePcqBjm2WWyy3b1tSb5NcFopMvUM_uZgPtTd6lMe8N9kEv763JyaCoTu_f5OC5goN6olz3jcwl66drbQOrFXNhbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e63a2b05.mp4?token=UfP6-A9sEoUgHp7GQbZ3Nw9R7tS4TTqie7v0PCfqKzMpbbgMbIya5Gd1LNoDCNtxi8FDLrTn05Ua1FO8Tlwo7MhBcnNdrc-IK7xtpNAbw4ZI4uKojfDZk4lF0LGc_9sHvTAd5ENsIUsxYtoBSNh-p0Gks1IV42pnoC7oLhV1F0iQF8YosKDb0r1CWs6oVDPV_DMv-jdYWD9nwJ2xLcGtIiadusxGrPTdV7xUdZctTy3qM4kQnVtNg3SxvUca9jePcqBjm2WWyy3b1tSb5NcFopMvUM_uZgPtTd6lMe8N9kEv763JyaCoTu_f5OC5goN6olz3jcwl66drbQOrFXNhbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روسیه در حال استقرار سامانه‌های پدافند هوایی Pantsir-SMD بر روی پشت‌بام ساختمان‌های بلند در مسکو با استفاده از هلیکوپترهای Mi-26 است، به عنوان بخشی از تلاش‌ها برای تقویت شبکه پدافند هوایی پایتخت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125550" target="_blank">📅 16:17 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125549">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
وزارت امور خارجه آمریکا: تحریم‌هایی علیه شبکه‌های دخیل در قاچاق سوخت ایرانی. ما سیاست فشار حداکثری بر نظام ایران را ادامه خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/125549" target="_blank">📅 16:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125545">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/memx82rr5OPojS9isYXAGRio_7mGGjh5jbgEpht6pXWNVU6anQhCrbeJFtPJXhWewaxDorh6BCIk1MOf1cPSdcyqDWdI6S8_4HnGnk7KFl8pQlVzyhRXAPnUDAnTa_UBeY-l29P6YmImMT8HFuzsWeKa8uz8KqiakcoTDxaT4v2ejjGS0WfHnr_DeLcNbVoe81cvG7aGQzheuceqFoaDOLf99YBt-dQzFg3Ct6wYjW285eYdxR-DnAJFY7Nxw4f02jfPMwm1yWqn3hAoJgCds7lfAbS0JexfEBsjqDOz-uH7i4Vw83lyhR1f1dkbSWBOnSbxS1DSKorHsJO-8ottkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rBLwcbmYWpqFJt1x7XHoINMT47_0re_IRWcoy8E55D__TbHNjd_L83ci7m3rhahaIwD6teiIZvB-jlTiG6QGX3nV16InnXn_gayJMXO7QbVq2tflGUZ-BYLkdsq9_l6QrXwfl-jgBKyea2PZY50aYF33zSd5e0k0oFPOWapqriBWTs1f3Mwv-4YnAtx6v259UBvLdhZdTrqVemOBYIcU0K6IVQHDGiFwfLdDuD1256bDT5KmOOnetFhu_n-G5MCuyQTVQkWwliaOxqON4-ccSKFJpJlJ69zEvpzx3rqJuNySiT2Z0aanNsuozLfXRIWhp2i5EmZdBXbAahs30hk4xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q5e0eD72DL9wiwtAbH-AmOy7lqIOD_TCF7HYxaTPKYTrOW3vJf6pRlH-oFHJyDxNfJj5ABDF1aRiInapAi7kpjIxd3l0zG4Tj8FT56_QGqYdrDj0Nr0t5Z-eak6hEhzBFDdrKMZkuRZNQIAMJAhfI8kEyXk9ZSIwDuQcvNWwHLCKe0CwZE4dXIAcbprqIPRt_XRrUqkzL2f2XRubf_ff7yUnngEFGmZi1CV01-QZzHWh_nXsni4S63jjYwOTTFjKcl1Zj1GVW6WFJu_v-q5SRIWWctf9rsBNk0zuAcDf4VxG3H76RGQwdHPwwgj0Gz_aKNyAt76iaeFOYA4L0zPlYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QM3UPENWNGiePwjIMP_xaTRaFgWcCOZw9N110q7xzXXYl1s4gIXlad_tZ85lZAnn27zxbTONBqCbFLar5Cnsm1rGl3WZeZ80QVYZR5ohvuXb7CYWK2iZLmlFKsrKAwoDVhJCpajHM6xzQjBDXxLLZ7_x4nnnPYJYj0ozcqTvrHB1b99J_MAUY1UnFIVmRWN4K9O-76QoL4eymydFcthBGKjJJytJLyi8wClJo9vnsEVcWQA87XAENEKv_zqW47USfLydKwWjDXykYrHMOFDeOabrTFXI_9Z36JdkhBU5CIawmDRY6hCY7ThCSQzrHVZWy7wEs57rr-jW6lAz24dcww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی در چند ساعت گذشته حملات هوایی را در سراسر جنوب لبنان انجام داده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125545" target="_blank">📅 16:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125540">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U1kRU7POyMOC788zjX6A-eBs6BWE5lMmkkmz2zihNjv2DqHdEYC4KDKyNBeYTuS8KtBpDRERqfg1XatGtTX22TyE9wFnGibE1SYiORZDtq2LcnSnn7H2qVKawK8UQOkOQso4MXUqjL4NSlSUjrFKNETu474lGXVTeyMAp3ajDC_YrlrhmSJjH8iIk6H2Y8RrGX01dmfwTBydBxoow0nAOFo3t2WvyX89B-4m2RZauTf6_cjyvAT3vdkb5E1bWPXUvpXog471ADo4MWjQzAQyAM4ZitMWv-tmZyHxltC1RpoPbR_VZ4D_lWi_X7PgnsNZFWb2BmpmS4hi2WCW_p_Szw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lx99npjWWinTfu4Dt-DMY3FfMLkb3atAd7vfc8TvnGpekqHJkTbg2jfhFey0U9CRoYUcdECbqXf3MY--2mpL6Nbgx74dFKSd2Pkvwj76TF7deu1gEXzfWnd3lmh6jS6EDSax9M-ZGZS0KMU9VGy2pjWDeVqmtYqEJ732I-P5Gjlzi32jL-uRVZt35Y5NJpUvEvnVvFSB32cUR-zzFqioC2XDcdecweIi7PMm5ioaNpdjizAXi_UxOFzKr3WpLbnx7mAeKAdOwP7zwNtXC4X-ORsGBrr2tLLLc-pcNXuQj5-2gxHzPrxWtUgB_hxYVao0__9jeSHrM08km26kPcGVfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rc65Rs7zNSXAw3jcFhn0sag8bVu329zoxqi1bBo2Sw48ASevB-EjfQAs2ia5a40rpVfhZak3WV-E1VNvfOs5gXFlGa6uBLWvEJZjspkk-gu0M-QfY-oNR2l7dZdqA3Is52fBb5_oxeQZjAeXS4WkGPxH6Dd30V1yE7u4EvfQoz2D-3ap2aLMTj7G-a3idd5dHiiliKK9EmWckXgRlhTrzfRaPx3Q_X0akH8CwBYyO3pP_1adGu9urdHaP7_vpGbS8kIDFV_9QYdJFA5hnAIOtlyXcqwAISz6nKzSjEUd9acUB7SCpb3Nl7LWxOhNfgMg4RqprNgCKE0PxJG8nNilyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uU8h4iUHOWVqZbwKJzVf2S-HjZ37EMf3wXSEsAH9N5nQf-eQyiFAk1eub9nbJ2wa9cXnHTdONcaEEZZjpWF4g8B2u3PLGEqhGB21deYG3UzGaPeWHUk2BZru-hIZHMSfaMXM-sb40HywaOkpj-fugiKfzBEdrSbcVshgWl9zzeBLqZHA7y2oyfGlBEX4a-VCAhfq-0kjOFtjdIv4Yn7U6Lkr_YckRHMbUEAx7C6wRbSSJFn7fKXL1T543JtWXy-vSyThI5aqyFUxYl9BfgF5pRrrcwaqY2q1p5o9FlNCtbxFK_gFMHbmU8pG-JXmaFrsyVePD5ZcpPNVNeLZm33npQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mgwjnUStobXhGK_2spNVBVWAzPGhIL0zg1vikNn8NH4xMKBLoC-YrFot79tUtSmyCQ_nYwvAEJovPbVs4L5PNbIKHjb6XI89an7HwJD1UZ4R0_3e9Clcqva0f5mi9_XPGV3jxojfVom90EDIpzXaCZ8zvKI0vxbmUSqUqQdgW0_FGKN3CiRdvtY1TQejg6MWU9zOL8q5WPG9nlvLbbjmGX3j8qEsa_d2-msg5hXmzRKWyWMK12I3IhZYmdMfetIiUsF0fYXzZeeDUzoCOtswIG3tMGRKtZAvFK29uQNH-UJDOd-8TMQ50cy4zoRN1icpxg_ro9M8Q8WbbPHcfS1cbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
کاخ‌ها و دروازه‌های تخت جمشید
۵۰۰ سال قبل از میلاد مسیح vs امروز...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125540" target="_blank">📅 16:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125539">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKAv-5cQJPZCnegN-20MB-CyPTo6Wd-seypPS0C_PT7ekuU0PoXPVv9i30Z4R3fkdGAR9eZg-4CzohgXd8zbh_mH2umWnEbaH64eqTVnfghrSXbMGeUwTqDnEYa0BC2cymo8VZjoY6Kdu_uNzm_smrMTYK8by2xKH8AUNRu6oV39SPnmRFSSKtget6QNPHUqISLT_REr6GYTgwjEZAQVQjUfoSQszyYEiyYUZ62qj6tL-HSBDpgygtH0thL2ZgnQ_1-OfHNNv0cUWnTU4b4XvkxsJr3H55GaodgeGJcUt75BlGwCxlQWBxSLoBQGpYxy_Mn73E8pavegsdeidZgmlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ : پیش‌تر هشدار داده می‌شد که بسته شدن تنگه هرمز یک فاجعه تمام‌عیار برای اقتصاد جهانی خواهد بود؛ اما اکنون مجموعه‌ای از راهکارهای جایگزین توانسته اثرات این بحران را خنثی کرده و مانع از عبور قیمت نفت خام از مرز ۱۰۰ دلار در هر بشکه شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125539" target="_blank">📅 15:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125538">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1Rx2WVPM1d3MJi4lLFz70rKY0h5J6hE2-XxKRweIZjcaPb6QpTV5wdj0wYySDabnJK88iy1URJA7tju9wjetlCkWPtlzPJipwK6C4Z7gp7i2RK7PJlC6YYnGmBkuSp7XeYz0yOeUvqz9kkzPsrCXpY4Lzp053-ZA9zHTQVyhj6jWKqpTeZHhg1-C_ZpZmr9VF3AKOm9bxN6MiDz3xxNieZ2NHKYCy80ysuUwbBr7aw7icaFGa5n66PoOtUgAW6xUWPcZp0Biap2J3mkzGfWEXKMsS--4MFT3_8cKGhp01tJ0FJGpdfYYfVu43LWPXsFaF0oQxmh5jZZk9AwN2zmWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ستاد کل ارتش کویت در بیانیه‌ای مدعی شد سامانه‌های دفاعی این کشور امروز موفق به رهگیری و مقابله با ۷ موشک بالستیک شلیک‌شده از سوی ایران شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125538" target="_blank">📅 15:54 · 16 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
