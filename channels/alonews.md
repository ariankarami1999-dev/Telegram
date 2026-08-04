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
<img src="https://cdn4.telesco.pe/file/NRcG1nHmLvSRZ06H0EvY-TIVHVVxUU0Pozw3pu5oYSiQsfevKNE2OBVNSUyMy2mi2A870O77_Z8_tWL6QlzRlxdmvZe4YqPR0OLQdKW3GyzwF9wbYTpgYtCcFQIrlXycgscYqRvu9KiJx0kp9R_sUoDr9MDNRiNTx13-veqMito807GYQUAxc4TfaOXpb1tkEgP5ungTV5g34jnJp6DjHaSc_JvMAsuruHUcrWY9V9-6i8wE8-KoLSGdiUx9CUJMzeHW-njyWbnjjIZa-0SbN7fS8L-_tQNRvlhQdBXW6ZPaokZblfYsSptyJwPyG2ibPUpNiuIsapyuGvrYxHWuFA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 986K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 23:36:34</div>
<hr>

<div class="tg-post" id="msg-139901">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
قیمت نفت خام برنت با ۵.۲۶ درصد کاهش به ۷۹.۳۶ دلار در هر بشکه رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 3 · <a href="https://t.me/alonews/139901" target="_blank">📅 23:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139900">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
اسرائیل شهر حدثه در جنوب لبنان را بمباران کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/139900" target="_blank">📅 23:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139899">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
تلگراف: ایران در حال بررسی ایجاد یک «صندوق داوطلبانه» توسط کشورهای خلیج فارس و برخی از اعضای اروپایی برای پوشش ناوبری، حفاظت از محیط زیست، جستجو و نجات و سایر خدمات در تنگه هرمز است.
🔴
این طرح که مورد حمایت عمان است، از چارچوب تنگه مالاکا مبنی بر درخواست از کشتی‌ها برای پرداخت سهم داوطلبانه الگوبرداری خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/alonews/139899" target="_blank">📅 23:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139898">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7805dff906.mp4?token=LIe6ty5C3FYQlav0yIA3Ky5g6GtYjfLLNwlHeZsh5AZaLt4aUeRtZzzee08Vvu7mfHJ_Fqt9xI3ZP16VlmbBFWbXWaS4UrxnMDq1FnPQbpjLU1IlzP6RggZGe1uVasOdBBIQe9Gtg1yTglZCxAMwblTp1DFhuQOnF8EdmEqORQtOQugbHelMj__1vdMPsQ6w4Mnii-Z-K1-CqUFWpkMcSdDWFREATi8N4gB7QC5vKOi0yICL1eYuA9_X46C1RxEtBIo96CqWmQfoYeRC3H1V-kMX1ETATgSpDscujxs0ltQzWwKhm3tz4vzKsii-Wjd3Q70kjpZEVONnpozL8PC-LrfpERWCYJ0ozdL1oROEctI6_4aQWfVY71oK01OOfV0b7ZWzeMVNTqBcQWd-TP-V3slPUN4udio3CdvQYJPsM2yOUqmQWUm5w7RoRpwf8r4HLJKDY0UHYjTZIIW8jV5Kwv_1ukqvdvvF9oO-8kyui1a7Iks6uLo6ayYEuJidGP9i_AMmAKnV31WbV6t5EmNN3iWnoHdTiU8gZvCa5zp9gLe9sQPZt6UnOW-oTyWh7ObhzBTZQu0T8Ya4QY1iSGkd-t1gfl02BdNEC0i3xgfimf71doRjdDy6pE5AZqLyUibRxwR7NIfbU-NtlDsaFBRCnK5u3mgis9ceq08mlyOlWBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7805dff906.mp4?token=LIe6ty5C3FYQlav0yIA3Ky5g6GtYjfLLNwlHeZsh5AZaLt4aUeRtZzzee08Vvu7mfHJ_Fqt9xI3ZP16VlmbBFWbXWaS4UrxnMDq1FnPQbpjLU1IlzP6RggZGe1uVasOdBBIQe9Gtg1yTglZCxAMwblTp1DFhuQOnF8EdmEqORQtOQugbHelMj__1vdMPsQ6w4Mnii-Z-K1-CqUFWpkMcSdDWFREATi8N4gB7QC5vKOi0yICL1eYuA9_X46C1RxEtBIo96CqWmQfoYeRC3H1V-kMX1ETATgSpDscujxs0ltQzWwKhm3tz4vzKsii-Wjd3Q70kjpZEVONnpozL8PC-LrfpERWCYJ0ozdL1oROEctI6_4aQWfVY71oK01OOfV0b7ZWzeMVNTqBcQWd-TP-V3slPUN4udio3CdvQYJPsM2yOUqmQWUm5w7RoRpwf8r4HLJKDY0UHYjTZIIW8jV5Kwv_1ukqvdvvF9oO-8kyui1a7Iks6uLo6ayYEuJidGP9i_AMmAKnV31WbV6t5EmNN3iWnoHdTiU8gZvCa5zp9gLe9sQPZt6UnOW-oTyWh7ObhzBTZQu0T8Ya4QY1iSGkd-t1gfl02BdNEC0i3xgfimf71doRjdDy6pE5AZqLyUibRxwR7NIfbU-NtlDsaFBRCnK5u3mgis9ceq08mlyOlWBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ چندی پیش، به سمت لس‌آنجلس رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/139898" target="_blank">📅 23:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139897">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7PijcCGQ41LLwk5k9rAnmKYs8gH9B8astoKWzl1H_kvAxXOhBIDWB7lcfVDGplrTd8r-TqlO4pAYNZQkeB-6_2XdzR9vNLgbxnBLkqA3SNZ-M49m_AXlntv0t2Oos7fyfqn4MmOcMNrBL8T5a3O8oNCk5qL1xK_f0WMz1PiCz2cbFjcXrktF3KpzZDbmO9BP2IUI9ygxmO14J2Crsq6GP2Y-ikMg7HFzCgjoItJYnXT0aL1TNh7ATLNVSiQ72W6pJsiz6rO5HprLggTLwy0dfFNxT9YKcNo3nJ1rXaZFpZuGqnQJ71RrQTTYc6MpjDYgdqzDNedVUR89UUCM1QMFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طی یه حرکت غافلگیرانه اپلیکیشن بله وارد اپ استور شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/139897" target="_blank">📅 22:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139896">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
یک مقام آمریکایی در گفت‌وگو با شبکه الجزیره ادعا کرد:
🔴
ترامپ همه ابزارهای قدرت را در اختیار دارد.
🔴
هرگونه مسیر موقت در تنگه هرمز بدون مانع، مجوز، تأییدیه یا دریافت هزینه خواهد بود.
🔴
تنگه هرمز یک آبراه بین‌المللی است و هیچ طرفی بر مسیرهای آن یا توانایی عبور از این گذرگاه کنترل ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/139896" target="_blank">📅 22:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139895">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
نتانیاهو: ترامپ معتقد است که می‌شود غزه را عاری از سلاح کرد. تا خلع سلاح شدن حماس از خطوط استقرار در نوار غزه خارج نخواهیم شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/139895" target="_blank">📅 22:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139894">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
فرماندهی مرکزی ارتش آمریکا (سنتکام)  با انتشار بیانیه‌ای اعلام کرد ناو آبی‌خاکی باکسر(Boxer LHD 4) در چارچوب حمایت از محاصره دریایی علیه ایران در منطقه فعالیت می‌کند.
🔴
سنتکام همچنین اعلام کرد تا تاریخ ۱۳ مردادماه ، نیروهای آمریکایی ۴۵ کشتی تجاری را که قصد عبور از این مسیر را داشتند دستور تغییر مسیر داده است، دو کشتی را از کار انداخته و دو مورد دیگر را نیز مورد بازرسی قرار داده‌اند.
🔴
این اقدامات در راستای اجرای سیاست‌های ایالات متحده برای کنترل تردد دریایی و افزایش فشار بر ایران در منطقه صورت گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/139894" target="_blank">📅 22:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139893">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
المیادین به نقل از رسانه‌های پاکستانی: محمد باقر قالیباف، در دهم آگوست [۱۹ مرداد]  به پاکستان سفر می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/139893" target="_blank">📅 22:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139892">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvZJgcUGT4C3fnutglwKPo_d4FNW_3_6a1CqzTW-FbJ44B2QlwphG4vw3m7QAWdUgrgs1e9ugyKmlCT2ccpBgiZ_P7ifNjT1j57ZzZYQFeZkhISVslaeCU7X-lbZ0Ie76h8UAnPI3T_Qo9YmpGZMohtF-Efu_hsdgv2mt954RKFEFCRqA7fXOJ6B8-86hzyw6yrl-8dDab556LPUeK418E-mCtirsNOemk8M3gQ03s7ttrRe_nNvSh4eICMH4Lw2U7MPSgtR5Fuev-43O4TSv4HuBK5lBIqIUmxfewGh0cj52iQaapowPQ6jpswzsl4xx88R0fieBYBYpF0qZzpy2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تناقض رفتاری بسیجیان
‼️
🔴
بسیجیان دانشگاه شریف که قبلاً به دلیل اختلاط در سلف دانشگاه اعتراض داشتند، اکنون در مراسم اربعین با خوابیدن مردان و زنان در کنار هم مشکلی ندارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/139892" target="_blank">📅 22:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139891">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
الجزیره : گزارش‌ها مبنی بر اینکه ایران به عنوان بخشی از یک توافق احتمالی، ترافیک تنگه هرمز را کنترل می‌کند، نادرست است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/139891" target="_blank">📅 22:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139890">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
خبرگزاری فارس به نقل از یک منبع نزدیک به تیم مذاکره کننده ایرانی: تهران تنها در مورد ترتیبات آتی برای مدیریت تنگه هرمز با سلطان نشین عمان مذاکره می کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/139890" target="_blank">📅 22:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139889">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
یک مقام آمریکایی در گفت و گو با الجزیره : گزارش‌ها مبنی بر اینکه ایران به عنوان بخشی از یک توافق احتمالی، ترافیک تنگه هرمز را کنترل می‌کند، نادرست است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/139889" target="_blank">📅 22:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139888">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59e43f241f.mp4?token=m5J-bkBZcrqzz53m7NKesOkm1VV0VSfJ1J-aVaZODu9YRJjKh-vPPgN5MqXqxsziCAi7dCy6jMYogF35u41QvTWAZQ3vEVScZmO2XOHbd5x4_GIi4jbJ5ki5N9RCKbjIJdHICoHQnLnpZ2PWEL6XiFwx2DY_Md7uHyGk7bDqHP3c3ek4JHwB9gbXcysdY6dlRg0xWeioGZcBYw4_Vx2JaRdhx4I5Pe4KjUhm5Nt77vmUnv8zjl5XhjspK8rNpB6yt_Kxzv9uhDN45uWzopZ1lPbjNiLzWy-b4TLc-wjv3XBB6ziVnIiJ_oijq_eHN6xIDz35wP1cXkTdpz1sOP4Ukw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59e43f241f.mp4?token=m5J-bkBZcrqzz53m7NKesOkm1VV0VSfJ1J-aVaZODu9YRJjKh-vPPgN5MqXqxsziCAi7dCy6jMYogF35u41QvTWAZQ3vEVScZmO2XOHbd5x4_GIi4jbJ5ki5N9RCKbjIJdHICoHQnLnpZ2PWEL6XiFwx2DY_Md7uHyGk7bDqHP3c3ek4JHwB9gbXcysdY6dlRg0xWeioGZcBYw4_Vx2JaRdhx4I5Pe4KjUhm5Nt77vmUnv8zjl5XhjspK8rNpB6yt_Kxzv9uhDN45uWzopZ1lPbjNiLzWy-b4TLc-wjv3XBB6ziVnIiJ_oijq_eHN6xIDz35wP1cXkTdpz1sOP4Ukw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ناصر هادیان، استاد برجسته روابط بین‌الملل: اگر از این مرحله عبور کنیم، ایران در شرایطی قرار خواهد گرفت که شاید در  سال قبل تا حالا سابقه نداشته
🔴
نسل ما نتایجش را نخواهد دید ولی نسل شما این نتایج را خواهند، دید یعنی کشوری پر رونق، توسعه یافته و قدرتمند
🔴
این محقق می شود اما به دو شرط؛ یک توافق انجام شود و دوم شعور متعارف به خرج دهیم، یعنی عقل زیاد هم نه
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/139888" target="_blank">📅 21:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139887">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
دیوان امیری قطر: امیر قطر در تماس تلفنی که از سوی رئیس‌جمهور آمریکا دریافت کرد، درباره تلاش‌ها برای کاهش تنش میان واشنگتن و تهران گفت‌وگو و رایزنی کرد.
🔴
امیر قطر در گفت‌وگو با ترامپ، تلاش‌ها برای نزدیک کردن دیدگاه‌های واشنگتن و تهران با هدف تقویت روند دستیابی به یک راه‌حل و توافق را بررسی کرد.
🔴
امیر قطر بر اهمیت گفت‌وگو، بهره‌گیری از راهکارهای دیپلماتیک و پایبندی همه طرف‌ها به مفاد یادداشت تفاهم تأکید کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/139887" target="_blank">📅 21:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139886">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
سپاه هرمزگان: از فردا به مدت ۷۲ ساعت، انفجارهای کنترل‌شده برای امحای مهمات عمل‌نکرده در اطراف بندرعباس انجام می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/139886" target="_blank">📅 21:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139885">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73386ecd9d.mp4?token=XklO8gEiarSlsmHWA-6HqaInlUohlDetAbZ46gcefnwnqxkzrIMqlttWSJnBYbUxbCM7BMA4YP7r2CLkPYwqamK--dKW-sNucwL_bPlXf9n7tiulF5MdWTyuC0GforOXlHitu2rmkFjO5t_1pw8h0-x4mmhfgVVSE9y-m-dzuma8ZOI1yveJx0VaC6ZjYxNHgkevkGSjfVweEYJ_x-9gY1viJvqW2H2bILsWJDPlJcx7wyb8alS1qH-BFQx2PovuH8rfYaB1xzuvTdZ8bkZtIa7at4RUutxszn_hmd9z3yfptcUcLjU3xWPZE63cQ1r-gsy1eqTBlQ2lsojXmootpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73386ecd9d.mp4?token=XklO8gEiarSlsmHWA-6HqaInlUohlDetAbZ46gcefnwnqxkzrIMqlttWSJnBYbUxbCM7BMA4YP7r2CLkPYwqamK--dKW-sNucwL_bPlXf9n7tiulF5MdWTyuC0GforOXlHitu2rmkFjO5t_1pw8h0-x4mmhfgVVSE9y-m-dzuma8ZOI1yveJx0VaC6ZjYxNHgkevkGSjfVweEYJ_x-9gY1viJvqW2H2bILsWJDPlJcx7wyb8alS1qH-BFQx2PovuH8rfYaB1xzuvTdZ8bkZtIa7at4RUutxszn_hmd9z3yfptcUcLjU3xWPZE63cQ1r-gsy1eqTBlQ2lsojXmootpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه سرباز روس توی دونتسک لخت خوابیده بود و داشت افتاب میگرفت که ......
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/139885" target="_blank">📅 21:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139884">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ipJvIYXm6KqDK0ZwPbZn90UY0lIsc9f0_j1KvdfN6bCtUXI57pr4P6VGdzZEQOqqsnaCiA4rW-C4xPHHKwLj5Gr2-kIJq5FrKTDNhthadZfp8ct6qg2Gyg13jC6lh9SG0OO2XWUZm26UUd_JFbz4pz7ZuBz0rSq8WHYjGUsKStOXvouRr0aRZCC8O4prRsVnzxOklba_AYQ1FEKjwsonqR-XvpGwVsk7jm7TWQVyNkf_2bBobruLxbBeW3Os4fs5-wuRzET_D5IVg-GyNLkl_K2f7asX9ngb2Ep5v7phg5rZGPoOMYThh5ro5uoLLxG4Jp0PfjZXkbOowBomdrixOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بهای نفت برنت با افت ۴.۷ درصدی به ۷۹.۸۷ دلار در هر بشکه رسید. همزمان بازده اوراق خزانه‌داری ۱۰ ساله آمریکا نیز از ۴.۷۰ درصد در روز دوشنبه به ۴.۶۴ درصد کاهش یافت.
🔴
به گفته تحلیلگران، در حال حاضر اخبار و گمانه‌زنی‌ها درباره احتمال توافق با جمهوری اسلامی مهم‌ترین عامل تأثیرگذار بر بازارهاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/139884" target="_blank">📅 21:29 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139883">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
۱۸ نفر بر اثر انفجار در شهرک شمس آباد مصدوم شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/139883" target="_blank">📅 21:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139882">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
وال استریت ژورنال: به گفته یک مقام ارشد، ایالات متحده و دولت‌های منطقه درخواست ایران برای دریافت هزینه را رد کردند و در عوض خواستار تضمین‌هایی شدند مبنی بر اینکه نیروهای نیابتی ایران به قلمرو آن‌ها حمله نکرده یا آن را تهدید نکنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/139882" target="_blank">📅 21:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139881">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
رویترز
:
منابع آگاه می‌گویند دولت ترامپ در حال تدوین طرحی برای ممنوعیت استفاده از تجهیزات چینی در مراکز داده (دیتاسنترها) است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/139881" target="_blank">📅 21:00 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139880">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره در تهران: ساعات حساسی در پیش است که ممکن است چندان طولانی نشود (شاید حداکثر برآورد، فردا باشد) تا وضعیت تنگه هرمز و هرگونه توافق احتمالی مشخص شود.
🔴
این موضوع مستلزم آن است که واشنگتن در محاصره دریایی و تحریم‌های نفتی تجدیدنظر کند؛ اقدامی که ممکن است انجام شود.
🔴
این مسیر راه را برای بازگشت به تفاهم‌نامه و مذاکرات هموار می‌کند؛ و شاید به برگزاری یک نشست در آینده نزدیک یا تمدید اجرای تفاهم‌نامه منجر شود، زیرا این تفاهم‌نامه در ۱۷ اوت منقضی خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/139880" target="_blank">📅 20:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139879">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
وزارت امور خارجه آمریکا: مذاکرات بین اسرائیل و لبنان در رم تا ۶ آگوست ادامه خواهد یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/139879" target="_blank">📅 20:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139878">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: اسرائیل مستقیماً از دولت آمریکا درباره روند دیپلماتیک با ایران به‌روزرسانی دریافت نمی‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/139878" target="_blank">📅 20:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139877">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
فاکس نیوز: یک مقام ارشد دولت آمریکا فاش کرد که لغو جنگ توسط پرزیدنت ترامپ در واقع بخاطر لو رفتن زمان جنگ در رسانه ها بوده و ترامپ این جنگ را فقط به عقب انداخته و مشاورانش به او گفته اند می تواند در این بین و برای آخرین بار به جمهوری اسلامی فرصت مذاکره و توافق دهد و در غیر این صورت در تاریخی که از قبل معلوم کرده و این دفعه امیدوار است لو نرود، حمله بسیار گسترده به ایران را انجام دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/139877" target="_blank">📅 20:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139876">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
وزیر حمل و نقل هند:  کشتی باری هندی به نام "فایزه نورع لییا" در نزدیکی آب‌های یمن مورد اصابت یک پرتابه قرار گرفته است که منجر به واژگونی و غرق شدن این کشتی شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/139876" target="_blank">📅 20:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139875">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
رویترز: ایالات متحده در جریان جنگ با ایران تقریباً از تمام موشک‌های تهاجمی دقیق خود استفاده کرده است. ذخایر موشک‌های ضدتانک و موشک‌های تهاجمی هدایت‌شونده و دقیق این کشور تقریباً به سطحی بسیار پایین رسیده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/139875" target="_blank">📅 20:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139874">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
فوری / سخنگوی وزارت خارجه : مذاکرات تا الان تو سطح فنی و سیاسی مثبت ارزیابی شده
🔴
ایران با عمان در حال کار برای تنظیم سازوکارهای مدیریت تردد کشتی‌ها تو این آبراه مهم هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/139874" target="_blank">📅 20:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139873">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a445c24fe6.mov?token=GbZuWXnYjBaBx9C4npR-jkyBZgSYn6Jbq7NZzMrRkk5o8_ElvDvY5oi1yLyDFryyP9F1GQZsjU4tUK0RqZcunLxwbrHwH33KYXrIjyxlPz1hADAq6H8-DQpB0sToqjDMXL7DaBN814h2qiYxng0457gujm822RDaACjDwaWxpVduJ7L-uS90PqRUh-BsGTcNtynKD26GcY0d1_UpxSqF2S8ktRDswJbULGOdRCB7ZvmSYTyGH9H5AHM6JwGxWN5tbo1v7P3gOs3Z2L3zgiRI5w0rgV0QyBkb56d9FNGfcsxu7NZp2-6Zd0v_ZZ4akLG5jJrOsE4pmS-89X8yOpXAdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a445c24fe6.mov?token=GbZuWXnYjBaBx9C4npR-jkyBZgSYn6Jbq7NZzMrRkk5o8_ElvDvY5oi1yLyDFryyP9F1GQZsjU4tUK0RqZcunLxwbrHwH33KYXrIjyxlPz1hADAq6H8-DQpB0sToqjDMXL7DaBN814h2qiYxng0457gujm822RDaACjDwaWxpVduJ7L-uS90PqRUh-BsGTcNtynKD26GcY0d1_UpxSqF2S8ktRDswJbULGOdRCB7ZvmSYTyGH9H5AHM6JwGxWN5tbo1v7P3gOs3Z2L3zgiRI5w0rgV0QyBkb56d9FNGfcsxu7NZp2-6Zd0v_ZZ4akLG5jJrOsE4pmS-89X8yOpXAdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک سرباز چترباز روس در جریان جشن روز نیروهای چترباز در نزدیکی مسکو جان خود را از دست داد، زیرا چترش باز نشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/139873" target="_blank">📅 20:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139872">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c2f667a2.mp4?token=k12cr7rbleiMpa1hSlaX0C2aaZzcBs5BSYkQIg4on5YFVPqWucXtJuyIGbmllfSxBg_3uecyshwAcO9bFkTkammejetFDOOMShUXohNdAaUuAuUOrx0_fVFbDnAdhtPCF32GjDKF0v7SRqkJs9rrPAj4KGEmZUftnA2cV39fqmJ18YribfZoGdP6q0Ct-QdNuYz5_KIdUR8-WasWemtooOBPTVUyT2f1Q50IeExSl6UzQkyQ4H9GIsGF6wczQlaUdMqTcAFVERT_iYsR5d0bnIhqCp28osHg5tsbEJ-kOpk3EjW-vuMPTtF1NqcVIpRlFkKC0V_rkdPhgCoMlI2d8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c2f667a2.mp4?token=k12cr7rbleiMpa1hSlaX0C2aaZzcBs5BSYkQIg4on5YFVPqWucXtJuyIGbmllfSxBg_3uecyshwAcO9bFkTkammejetFDOOMShUXohNdAaUuAuUOrx0_fVFbDnAdhtPCF32GjDKF0v7SRqkJs9rrPAj4KGEmZUftnA2cV39fqmJ18YribfZoGdP6q0Ct-QdNuYz5_KIdUR8-WasWemtooOBPTVUyT2f1Q50IeExSl6UzQkyQ4H9GIsGF6wczQlaUdMqTcAFVERT_iYsR5d0bnIhqCp28osHg5tsbEJ-kOpk3EjW-vuMPTtF1NqcVIpRlFkKC0V_rkdPhgCoMlI2d8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو وایرال شده از یه خانم که ازش مصاحبه میگیرن: هوش مصنوعی ایرانی بهتر از امریکاییه، اصلا مگه آمریکاییا سواد دارن که بخوان هوش مصنوعی درست کنن؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/139872" target="_blank">📅 19:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139871">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
فوری / سخنگوی وزارت خارجه :
مذاکرات تا الان تو سطح فنی و سیاسی مثبت ارزیابی شده
🔴
ایران با عمان در حال کار برای تنظیم سازوکارهای مدیریت تردد کشتی‌ها تو این آبراه مهم هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/139871" target="_blank">📅 19:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139870">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
فارس: از زمان اعلام آتش بس در غزه، اسرائیل ۴۰۰۰ بار آتش بس رو نقض کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/139870" target="_blank">📅 19:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139869">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
بلومبرگ: ایران بارها به طور علنی اعلام کرده است که اجازه نخواهد داد کشورهای خارجی در عملیات پاکسازی مین در این منطقه حیاتی که مرکز حمل و نقل نفت و گاز مایع است، شرکت کنند.
🔴
با این حال، در جلسات خصوصی در هفته‌های اخیر، تهران موضع خود را تعدیل کرده است. این موضوع توسط دیپلمات‌هایی که با شرایط این گفتگوها آشنا هستند و به شرط ناشناس ماندن صحبت کرده‌اند، فاش شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/139869" target="_blank">📅 19:29 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139868">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
دو زمین‌لرزه ۳.۹ و ۳.۵ ریشتری هرمزگان را لرزاند
🔴
نخستین زمین‌لرزه ساعت ۱۶:۱۰:۱۴ امروز حوالی سردشت و دومین زمین‌لرزه نیز ساعت ۱۶:۲۲:۱۶ در مرز جزیره قشم، خلیج فارس و جنگل‌های حرا، حوالی لافت در استان هرمزگان رخ داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/139868" target="_blank">📅 19:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139867">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
فرماندار ری: آتش‌سوزی در شهرک صنعتی شمس‌آباد اطفا شده و آتش‌نشانان در حال لکه‌گیری هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/139867" target="_blank">📅 19:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139866">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
یک مقام ارشد ایرانی:
رسیدن به توافقی با عمان در مورد تنگه هرمز، در صورت توقف دخالت‌های آمریکا، امکان‌پذیر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/139866" target="_blank">📅 19:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139865">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
انتشار گفت‌وگوی مهم پزشکیان با مردم عقب افتاد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/139865" target="_blank">📅 19:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139864">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
یک نفتکش هندی در جنوب یمن هدف شهپاد قرار گرفت و در اثر انفجار غرق شد.
خدمه کشتی توسط گشت دریایی یمن ( مخالف حوثی ها ) بدون جراحت نجات یافتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/139864" target="_blank">📅 19:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139863">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6wWO974Pry9q7BszH10DrGqNJT3aaxtf9pVFHwowYPS4IKjCfy50yAMqIEv2DCPd__de2EGA7-DkyslreQoYp-hmhmLvg6Igj5IpA-EpplltFOU_0a6eylbYrqyBWv25o8Zwu9DcYZbyehzJHHKFO036MDI_JwfzhqdonWI3b93QDqkmMODYT4c7WIqjxeDnMV0RI3HUm5XDvYO19_Ndeo3F6RGfC4MgLXwDvj_y9r57ufV-gklbbDS_6mP4NncL7euSkVsAUZymiE77BUJnz5Hf3E5tZOe2NBYCIRBRbJN1DX21WyVw2_-83EfASGynBc4wMHZ-U6yA-FqK2tkuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاتریک وینتور، دبیر دیپلماسی گاردین:
‏ به نظر می‌رسد عمان، تحت فشار آمریکا، اروپا و عربستان سعودی، در حال پذیرش مسیری برای بازگشایی تنگه هرمز است که تا حد زیادی با ابتکار ایران طراحی شده است.
🔴
‏ بر اساس این پیشنهاد، مسیر عبور کشتی‌ها به گونه‌ای خواهد بود که ایران همچنان کنترل غالب را بر آن داشته باشد و کشتی‌ها هنگام ورود به تنگه از آب‌های تحت کنترل ایران عبور کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/139863" target="_blank">📅 19:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139862">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLgZypHaugXaEG6xUKi0V2C64kvXDSd5hmsSX8VmYk_211YF8U-g7arpzAEiFBUp6tVqTvTZs9WculUxOgsqXaSHI6RXdapW5-mZMKhJU2WEOmTZN9y0ERYkduyLz25SR5qP4QiH6Bm0f55fY8rFMcw4rVk6CWsYAhldcCq9A2LeG8F1m-MtElpF55YQBV0lvTJ2KpVmKSdCQcD8U9O-F0AEQL6eUdDUhpXKetqHMgzGdS721z8UqZp_X__zJfnzUj9LTwXg9lrrQYgEnk3RkewB0pARbZHAvzecFqOaZq5wEvbPnq8fLljyt5N7ByqIXQdlk1ynp5g6LLb-vTfb_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کشور رو هواست همزمان عباس تو کربلا:
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/139862" target="_blank">📅 18:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139861">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
ارتش عربی سوریه دستور تجهیز کامل تمام نیروها با مهمات جنگی و افزایش آمادگی رزمی به بالاترین سطح را صادر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/139861" target="_blank">📅 18:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139860">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D54dOlYS6hMLlWK-KjYTUCXFGVC_uADCWcVY2GBdoNgFdoXIIeJVaghdJHGwa_aqrPbfJHisjm0WGBDbc6f10L94FJt2dG30xzaScyB23WbQiSGL9saxtdCYOJPlEEiG4NVVokCIlMsve2wGfZpqMPU557v1aQozHd1cSsSSyl829_BuyTRfW88Rt33J0rdG1U8wm1EiPpy7SeB1Ehlyt3Tu_AC1C977mUVl9yAypXiYNSNx75c-sKdozx96PTuh0yzOIho3mG2ZSf-hQaIi9CmhfilPqXIDFzWdT_7nRsQEx1Zo3hf2wQn7W6MUr8Y4DVoMP2SLnfpzJtvaZ3mMPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: "توافق قریب الوقوع است" با از سرگیری مذاکرات با ایران در مورد خلع سلاح هسته‌ای و تنگه هرمز.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/139860" target="_blank">📅 18:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139859">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
ترامپ: افتخار من بود که از سناتور دارلین گراهام نوردونه (خواهر لیندزی گراهام بزرگ و فقید!)، از ایالت فوق‌العاده کارولینای جنوبی، در دفتر بیضی شکل استقبال کنم.
🔴
ما مدت‌هاست که یکدیگر را می‌شناسیم - او فردی فوق‌العاده و یک وطن‌پرست واقعی آمریکایی است. لیندزی یکی از بزرگترین انسان‌ها و سناتورهایی بود که من تا به حال شناخته‌ام، و خواهرش عشق عمیق او به کشورمان و ایالت کارولینای جنوبی را به ارث برده است.
🔴
در جریان دیدارش، از دارلین خواستم، به خاطر کشورمان، در انتخابات مقدماتی ویژه جمهوری‌خواهان در روز سه‌شنبه، ۱۱ اوت ۲۰۲۶ نامزد شود. او پذیرفت، چرا که هیچ‌کس بهتر از او برای گرامیداشت میراث برادر عزیزش، لیندزی، وجود ندارد.
🔴
دارلین، که از خانواده‌ای کاملاً فوق‌العاده می‌آید، در تمام زندگی‌اش یک برنده بوده است، و از حمایت کامل و تمام من در انتخابات ویژه سنای آمریکا در کارولینای جنوبی برخوردار است - او هرگز شما را ناامید نخواهد کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/139859" target="_blank">📅 18:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139858">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
بسنت: همین حالا تعداد زیادی کشتی درحال عبور از تنگه هرمز هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/139858" target="_blank">📅 18:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139857">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqTCrNhvkd9-exFaUdrHT_svDpS-HiJUfFx9NMFA_ccPZYqGnzU1jytnN1FLFni_9tvyf_dNdwHgbhONl8_jrnUA8pyBAYfObKVdmpn-36PqXDq8Uj-3oVxKB4OUsidaQwvdkGuQ5BHgZ6CPO0pUf8ybHGY5gjLoD5864oEj__KoTfwd5mYy3mzkihhZzi6GQEC1AgJaqZ3UScogzZicdYqMvIqtsHePUS4wD0msTCRFBTf7JW-dx-j7KMFBK9sXxKEvgLQ003sNBsfpcgeuXumNJE8ZqmF4u9UTxG5EbtwN6WQG2nFVTAGFvuTHVep37OunH0BA-B9LyXTzq4cmcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فووووووووووووری
/
بهرام یوسفی فعال اقتصادی نزدیک به دولت مدعی شد توافق ایران و عمان برای  بازگشایی  تنگه هرمز حاصل شده و احتمالا ساعات آتی خبر بازگشایی تنگه هرمز از سمت مقامات  ای عمانی اعلام شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/139857" target="_blank">📅 18:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139856">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
رادیو ارتش اسرائیل: فرماندهی ارتش طی ۴۸ ساعت گذشته سیاست حمله به غزه را به شدت تشدید کرده و اکنون هر عملیات هدف‌گیری نیازمند تأیید شخص رئیس ستاد، زمیر، است.
🔴
سخنگوی ارتش اسرائیل هنوز در این باره اظهارنظری نکرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/139856" target="_blank">📅 18:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139853">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KMjspa2OZkILfe0dqIKCmT9JTL6Zh0M4fss9qTtAEALa-qj6XIQYzMV3KWnB0Uv8RSuirGZfcbRMby2Tj5Y5RVIWRS7Z-0ankvB_QEtz1hTZ72lH0PDMMbP50xNZQlvMIopPKWvZf2hww4oX9f0WLVLXvFHNl5ejH9AYvNaw8oJ5jknbOeDezzhYMiUQ_fzoefoXUZuysA112Kl74LqZEufv1D-KY43QxaFqK3qt9-qUSqFzsF6ALQAoOUF0gb2zJIk7hJr_3UJ42f0JqgpilgE3sFD0DcpnSlJQDfnnfM6YwXQE7l2uS8RtIefCKsYh-CUYKsDUMOXRJ7JcyDMbiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/K1vNuK547ohzTmXJWRNK2wzFi_yNHHZrPheZcSShxKjlOjYmdSiPKOEWr98zNpWhO8dZRkQp8A1WzstR9eBE0SREtumhG5UtWizrr7ewb-kTkLnuVAAURvGOY8RmyUauCVx52Xpmly_4jIAK52HxWKJQn4i_HRVndtxbzZSXx7exogBDVfUHuvArasFWLrSDpKl5ewKo9h6upZpZCdzJ0sxXdB14fJYHtifgrZZUNLgvHuOmmWeoik1xohxeCANzcILaebqroZZXmt_CZ74gszTk0ejiuCjR6LlGzgrPORy1CvXGA1_U3QQVURFT4YcheNP5eDjiUWIZJOc6OWq4dg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4b73abb732.mp4?token=UjZoQ68veQwhzPSdRTPb7EtA1R2ieh7Kyvlc6ZZhTCPj677OcAaMg_i1H4o3shr9kwYUg0TXm-mS-T5Ng2Zo31-QGP9VkI8y1j2hKcRbxU-XIj-vfHHfsT1wN02Mpsb4YS_nbRw2xblLtE_7VhIddDOMnO-tKBIQ1REGsSEwai5bC4pD6UHy2XMbpuzfB3gNfuB7UB9eBxZL80IxpbniCXGsOjaHRVCBMDTaXSh65ElYoo4XgnvuOGa6UIJ-rXtC4SAqOgHYQuQrwc5Vma1JivAwWKRWC4tT5ob4g36aHjTbrsSU99PhtnixB4kATGdDsIlgz0jHep3ltA7hU6VsYg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4b73abb732.mp4?token=UjZoQ68veQwhzPSdRTPb7EtA1R2ieh7Kyvlc6ZZhTCPj677OcAaMg_i1H4o3shr9kwYUg0TXm-mS-T5Ng2Zo31-QGP9VkI8y1j2hKcRbxU-XIj-vfHHfsT1wN02Mpsb4YS_nbRw2xblLtE_7VhIddDOMnO-tKBIQ1REGsSEwai5bC4pD6UHy2XMbpuzfB3gNfuB7UB9eBxZL80IxpbniCXGsOjaHRVCBMDTaXSh65ElYoo4XgnvuOGa6UIJ-rXtC4SAqOgHYQuQrwc5Vma1JivAwWKRWC4tT5ob4g36aHjTbrsSU99PhtnixB4kATGdDsIlgz0jHep3ltA7hU6VsYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز 13 ام مرداد، تولد جهان پهلوان، جاویدنام مسعود ذات پروره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/139853" target="_blank">📅 18:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139852">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
نشریه بلومبرگ گزارش داد عربستان سعودی از طریق میانجی‌های عمانی در حال گفتگو با انصارالله یمن درباره برقراری آتش‌بس و کاهش تنش‌ها است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/139852" target="_blank">📅 18:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139851">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptQKZ_82uXNaxHRVTW5L6qw_I9GgrgcAYxvQ5yce9n-uWXWeao8uqlkb7PcZWzPCi3QJQ82ZQG3GIAU7_Q4AZFiGw60F-e5rUIZVC-EGTecy6Hu63YSQui4x1b9b85MvP6EKMuUqr-_4kbL2P_DUvTuWPegrgbpYjGodspmR41esSa5bJtA8TV0S5JP3K1aDHI4pG77iXWXyMLQxgI0XQEISMZOfFZWYsmjrvm2E90hL0-8lPxY4biFxg9Vo8RMaCRi-iwb_BoFOhC6Ida2UsubmIdFuFRrTaTnYa5ueGQUX9L08wcRgSIRgYdf1iYcust3xbLl7EYTkHHsqKcycJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
توییت ضرغامی درباره جنتی
🔴
خودت استعفا بده و به نظام خدمت کن
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/139851" target="_blank">📅 17:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139850">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
به گزارش فارن پالیسی، گسترش سریع تولیدات صنایع دفاعی در روسیه باعث شده است شمار زیادی از نیروهای کار از بخش‌های غیرنظامی به صنایع نظامی منتقل شوند.
🔴
این روند رقابت برای جذب نیروی کار را در شرایطی که روسیه از پیش نیز با کمبود نیروی انسانی مواجه بود، تشدید کرده و فشار بیشتری بر بخش‌های غیرنظامی اقتصاد وارد آورده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/139850" target="_blank">📅 17:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139849">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
روبیو : روابط آمریکا و پاراگوئه هر روز قوی‌تر می‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/139849" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139848">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
روبیو : تو مذاکرات برای بازگشایی تنگه پیشرفت‌هایی داشتیم، اما هنوز به توافق نهایی نرسیدیم
🔴
امیدواریم خیلی زود به توافق برسیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/139848" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139847">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
روبیو: اعلام توافق با ایران در مورد تنگه هرمز می‌تواند خیلی زود انجام شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/139847" target="_blank">📅 17:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139846">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
العربیه: بیانیه مشترک عمان و ایران درباره هرمز، طی چند ساعت آینده اعلام می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/139846" target="_blank">📅 17:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139844">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f3aBfOEISWOO4CncoEDWEHEdrDzViXwD1X8ntXMUhr17JipbE3HEBcLfzb6DIlPHZdaIfT4Mtd1QQcUBq6UUST1cPzzkKc-lxfBJdMtHcVYSp4-dleo-k-HqoeRIOiP2zryggxJm2bQad20yXhpfl_xMqPJ-YklmNej9fziaW2fEjXSPvma6i2jtO3EoYSFr-7JrWnDuD_J_fEj9cO3INcefPXmBdcEhwGDzRw9jeC7Yhl3Tpo6FW13kSyJsAZuLM6sPooUMd6PW-MhOgm8x8mPHvBA2iRdDha4dC_7Nalabm7IA4zv4XkGv3wf-P6M5KBzXwoQPqyryKZjHYpaVzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QFxzx5MKGLaHX468am9pHm6_8Lye_RQJKis90o_sPvYahRnCh0-H7QNsHasZJnN2JJY6I7-XsCBau8lJqJ8dKU5ywj9U-DaSpk8504__cdve1D-vWy5KDRLVIM1KxOy58a7c22x9vPJm42SzkGQy9VY9uZQKyWAH9-nlbChYU3aHGcQ57by1zk9fngW3WZppei50D3oorQ2bLF2GrWZXwTnSpgsoj_3yE8eKm8jsCKjWOGY-YjCgzNdRiaEuUlrI_w3BrhoDnNtaGR3VEjaMZHh40WKVs_Nm-t5WrFDEhyZ48F3hpy4Og2LaNusZrKntIw_JzcIbUfFjHLun8O2mPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک هواپیمای آمریکایی امروز از پایگاه هوایی اوسان در کره جنوبی به سمت پایگاه هوایی عیسی در بحرین به پرواز درآمد که احتمالاً به دلیل کمبود موشک‌های پدافند هوایی در بحرین، محموله‌ای از این موشک‌ها را حمل می‌کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/139844" target="_blank">📅 17:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139843">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
الجزیره : اعلام توافق برای بازگشایی کامل تنگه، ممکنه تا چند ساعت دیگه یا نهایتاً فردا انجام بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/139843" target="_blank">📅 17:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139842">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
یک منبع مطلع به العربیه: احتمالاً طی ساعات آینده یا فردا، جزئیات مربوط به بازگشایی کامل تنگه هرمز اعلام خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/139842" target="_blank">📅 17:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139841">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
شرکت تسلیحاتی «فایر پوینت» اوکراین با بیش از ۱۲ شرکت دفاعی اروپایی برای تأمین رادار، سامانه‌های هدایت و دیگر تجهیزات مورد نیاز پروژه دفاع موشکی «فریا» توافق‌نامه امضا کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/139841" target="_blank">📅 17:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139840">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_exWetlnRXFBDs7HIPkWQymQsCnYXrPcuWN9idWlPUx94wfN9Xi8uT1AelS-rBUilzzFzONCQP89nq3H1AxfuyKB2WsLPFX-huwXqQcsVTm1XYUW63uRgQbeVSu57ey7PBoF7LtikOmpzmD9t-w_5I9Yslm1PUOd7OmagitrReFGfcSp-5neiE2T0Pe8ET8L5R3oOdN3146et6UaEBwyjPzTBBUy_E33OFCiUCTNDBU8BQRn6fULq7LM07IvOhHtVjuPf2bOA2V8u_uIVWw8IeFH8ug0-HvGnJOC8b5An3RWIhFlMa3m-F0GTZpSf9L6cQ-8bbQ9CC7Qgou374wuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تایوان: همکاری نظامی با آمریکا فراتر از تصور است!
🔴
مقام‌های تایوانی از گسترش همکاری‌های دفاعی با ایالات متحده خبر داده‌اند؛ همکاری‌هایی که علاوه بر فروش تسلیحات، آموزش‌ها و تبادلات نظامی گسترده‌ای را نیز در بر می‌گیرد و بخش زیادی از آن تاکنون به‌صورت علنی مطرح نشده بود. این موضع‌گیری در عین حال پیامی به چین تلقی می‌شود که نشان می‌دهد روابط نظامی میان واشنگتن و تایپه همچنان در حال تقویت است.
🔴
به نوشته وال‌استریت ژورنال، «ولینگتون کو» وزیر دفاع تایوان تأکید کرده است که سطح همکاری با آمریکا «بسیار نزدیک‌تر از آن چیزی است که تصور می‌کنید». به گفته او، این همکاری‌ها تنها به تأمین تجهیزات نظامی محدود نیست و نیروهای تایوانی از طریق تعامل با ارتش آمریکا، تجربیات عملیاتی و رزمی ارزشمندی نیز کسب می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/139840" target="_blank">📅 16:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139839">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUX2S9Y9qnAylkEeVcwTz9KQF5P1GeAVUYNt7dmY9lXsy_4ROCF4qiFaycf73E8wKrfIguNb3E34PsVIDv4clC6LlV7aG5aitxdi5R7W0my6jk00ymihz4bnx8Kji3udyT0kQz1OWD3EPut_kHXo5YzMyaeIbQEqNlMvRPy3zqEfPQQSytHVD3n0kppnzk24l_sdyjlGJg0RL2GvJ2ifUufyjRcIygCbem4GFKbWcld_3bOMm0qNJbvjsI9DFuB630ZVtFLXmgsMFUI0gi6iezZaOuuUplkbtaVfKIn0VDpEad9R5aY4FxEnmh_LYQPWkbi8vBOOyLusITWEQ_7KQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سقوط نفت برنت به ۸۰ دلار پس از مصاحبه تلویزیونی وزیر خزانه‌داری آمریکا و اعلام احتمال دستیابی به توافقی جدید برای بازگشایی تنگه هرمز تا فردا
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/139839" target="_blank">📅 16:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139837">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
شش نفتکش غول‌پیکر سعودی، خالی از محموله، مسیر باب‌المندب را تغییر داده و از جنوب اقیانوس هند به سمت آفریقا حرکت می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/139837" target="_blank">📅 16:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139836">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
رسانه‌های انگلیس: آتش گرفتن قایق حامل ۱۶۰ مهاجر در کانال «مانش»
🔴
رسانه‌های انگلیس امروز (سه‌شنبه) اعلام کردند یک قایق حامل ۱۶۰ مهاجر هنگام تلاش برای عبور از کانال مانش دچار آتش‌سوزی شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/139836" target="_blank">📅 16:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139835">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ویدئویی از عملیات جنگنده F-22 همراه سوخت‌رسان آمریکایی
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/139835" target="_blank">📅 16:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139834">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
روزنامه Izvestia: آمریکا داره با سردر‌گم کردن تهران زمینه رو برای یک حمله غافلگیرانه فراهم میکنه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/139834" target="_blank">📅 16:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139833">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
امارات متحده عربی ورود همه شناورهای ایرانی، از جمله کشتی‌ها و لنج‌ها، را به بنادر خود ممنوع کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/139833" target="_blank">📅 16:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139832">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sA8wYEzk3EQGA4dM0iXUqhhvd8UC67UulAqD09KAXxJUb3h-2EN1M39rWMHjRLFO5SN2XtfRli-0hz3alHqjGvpgQXcKpgxB03hCu_kyXQKJjU_lST6IPJu3bJ5FW838Yh3Mkozzr_BmoUAZBCm3JqH0PzqG-07qypmDHLBl81uGd1Ib3HyDKUjDKatB1b-_orXs_fc9nVP2Ry6lhGQdZugMq8vEEJpY8hS9UpIi9hOV-dvLa8UhqX_7FRCa2yUP7s8LTE3HhGrZDnYJl6xAzKanvujw2OFm3konuKTFyZTbUWqtNSqVkuyPIMxP_H4FsLtC5qqpXZ-d2reDSPluIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حسن عباسی:
سال 73 با امکانات متروی تهران، در جزایر و سواحل جنوب تونل زدیم
🔴
زیرِ جزایر و سواحل، تونل‌های موشکی متعددی با امکانات متروسازی شهرداری تهران ساخته شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/139832" target="_blank">📅 16:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139831">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EguU5f4xO3oA2CR96wrFjprjK8inu5HWMTHW3vO4w0Tbs13tDqg19geZ-tElnho0S_mD5DqpBuz3jduU1HfEzYYUgTvEI5-lpdXI4D5RgWhX8PSrZE9Ue8AImHQCUWl7q04m9i_oQBuGAvqiGz4NDi90Fkepe_l8VXohEbw2z0jY4UuMrjVpDMnJc6YVGpvYzGpvDw7LBrlpJPfvUj4-K9PZ2mWtXy6fmQu7-ZjX5Kq3Gw_3XWeUm0uj99et80noH62JYLNGHkISksqyBP8nKHn-Q1DXyRwgcDfEBOJBdqn9RN_1Iz5eBFuVJbXgG1kbdgs_EXwKiAvVOE4xG47Isw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز : وقتی با رضا پهلوی حرف میزنی، میفهمی بیشتر از سیاست به فوتبال، غذا و عکاسی علاقه داره
کاملاً مشخصه که او ویژگی‌ های لازم برای رهبری را ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/139831" target="_blank">📅 16:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139830">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvnTrOJMFXIEvIX1IeJZXD4l4j0WgmZV36N42RlVAhEl_drd4XNmgJoDCfoEhE_BC_rMZUcbP8dfLfzPS0pcDLMnaxwhRtvH0Do3eKGxujVXVW50lpXBMgzMjT1Xe3hK3yp9p-REi5xMsm4yyUdlxNLCub4hCRUe1RdQLJh-LnOGGz2SjjNjTMt0yANhsCe7loMgynKSzlh5ILWbgMixlYdO-hVGr7M9B0Msf5kdIN15CP1dO3DvNR_x3FNuGTznPiigCDZC1_m1DGoGPQw7CEmgFOF_RAYrYJS_tNRodUhWVluAUmnJ6eGExrX-v4sF5AfLeczoOCZhowhDDUT3kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۱۸ نفر بر اثر انفجار در شهرک شمس آباد مصدوم شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/139830" target="_blank">📅 16:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139828">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7df5d5b7fb.mp4?token=d7J44QaOG2dubPBKteDNEG-k03ZkK9CVkMf47ITIx7PjG9cfHD1AcSRg0kC_1Hn1JDpJgvqHyjcDPKnfinaqwlliHjtTQGY_XY88_NC-c3LpZ3Rg_jW_7uKLmPYP4ADEnRtasYeq3iTV8tzX6WXmALuqxBv7Y_7dmKWWS2dfECEHD3PfSywyPB0gRTZKz6XGMEXcrbC63CP8Ae-XvUw-GUvgmWOQ1rj-dBZ6iOyqnmnd6a_1rQc6BxvYO19DgZsAh91LF5cGbFlhsLqlfzd2XOs8QxBHD6y9svz_mACIcwJIMb5TlLO1ZgiTbWV2ExMecw6Dkydew5JavieDcKLAjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7df5d5b7fb.mp4?token=d7J44QaOG2dubPBKteDNEG-k03ZkK9CVkMf47ITIx7PjG9cfHD1AcSRg0kC_1Hn1JDpJgvqHyjcDPKnfinaqwlliHjtTQGY_XY88_NC-c3LpZ3Rg_jW_7uKLmPYP4ADEnRtasYeq3iTV8tzX6WXmALuqxBv7Y_7dmKWWS2dfECEHD3PfSywyPB0gRTZKz6XGMEXcrbC63CP8Ae-XvUw-GUvgmWOQ1rj-dBZ6iOyqnmnd6a_1rQc6BxvYO19DgZsAh91LF5cGbFlhsLqlfzd2XOs8QxBHD6y9svz_mACIcwJIMb5TlLO1ZgiTbWV2ExMecw6Dkydew5JavieDcKLAjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
توریست ایرانی پاشده رفته کوبا و زیبایی های کمونیسم رو به عینه تجربه کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/139828" target="_blank">📅 15:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139827">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
کاهش نفت و افزایش اونس طلا بعد از مصاحبه وزیر خزانه داری آمریکا
🔴
ریزش 5 درصدی نفت برنت به زیر 80 دلار.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/139827" target="_blank">📅 15:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139826">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
وزیر خزانه داری آمریکا، در مصاحبه با شبکه CNBC، گفت: ممکن است فردا با ایران برای بازگشایی تنگه هرمز به توافق برسیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/139826" target="_blank">📅 15:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139825">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
یک مقام ارشد پاکستان به گاردین:
مذاکرات میان جمهوری اسلامی و امریکا،
به بن بست رسیده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/139825" target="_blank">📅 15:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139824">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-C1o7NS2DGod1JnlyMuX2Zl2pTvIIqh0fdcVB5CornlIFSNrrPKofL7v5iHD86XZK44sZ1MVT11qw1YcoPhsPCOIC-CHG1BSC8OPvpCfSWW-WrDE7Zs0sbuZFpJ82HC6F8x3LhXRH9D7WiaL9VigKqOFaZzZ0T2s35fucrmMit7TUJEZ-1H1ZEzUbvRYRywMQk-gP6o4gnQm48e9JaTMNFzXuER3SbX9KImmHraqsHEAHNLHaw63XP5oSGr07px_N-8KcxsTyEbKkvEN2-0wlLF8vEyy2W6kfS5R11D3pfluMuHAe32P3gdudON9x-x49LGekUNNAUwQ3VTCaOhbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
العربیه تصویری از کشتی هدف قرار گرفته در تنگه هرمز منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/139824" target="_blank">📅 15:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139823">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNj5ge0yXZHZHXjn-HheMJ7rDQhxmlH1p6uiSDIFkZWanKV2W5WaP9vQR-l0eDWQV7S6scxzun5Bmod3X-dvfsGNE3u14gAXMs-I5l5ShcHXs8bgQIXOEOpYrZcw_wRkShhtDFxG7_Ja-wa5hXpzR1VTMFO60Vz8tYs0y9h3vWlY9ALu18zXOoIq0IR3vmdeYapEnDHpsJmNKJTN7KMbqjgvoPnOWpxBe8n27HdwaFcfARugmILtz0TaNhw_JTOoY9WDAHEL8UHb52qj6kx9KRmA5Yg-8AwvNuoW5_1MwWIuHR-QqtsCklbgHB1gR8ByBcR71WNpcrb4TeTQQuh7Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ: ترامپ تا سه شنبه به جمهوری اسلامی فرصت مذاکره داده و باید تنگه هرمز رو باز بکنن
در صورت باز نشدن تنگه هرمز ایران با حملاتی ویرانگر مواجه خواهد شد
✅
‎
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/139823" target="_blank">📅 15:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139822">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vY8lJu-cXq2Szsk1f0w4zvll1fjuUSr4Al4EII6cUVEdZCN-MmIMQIauZVYqvKMdg6q4Mvirf7Ty0xyfyp5_zbhedpFho2gqFZuzHFp4hBySlgak0D9w8Hv3uZbRP2CyNUcqroQzaZiM-NyD64ylk9j8JoAdKCwHtMmY5X_0UsUkAKf-iWgHGLJ6uM0VFr1qN5GLOY9785Buj-882nspeRjJ8DlgpcLRJv5kfEJp2jM5fsCKsoSB3s4etg7MLoYjEdGATHRUqDIXfUZb52sfBeoyebzef1C8usLmNQghN13NGXCqTjggdsvjoY6V_Id23IDw8LpHwCXRU58Vb6KdXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پراید در سال ۱۳۸۵: ۶ میلیون تومن.
Vs
چرخ فرغون در سال ۱۴۰۵: ۶ میلیون تومن.
همین برای توصیف اقتصاد ایران کفایت میکنه.
فقط طی ۲۰ سال.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/139822" target="_blank">📅 14:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139821">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
قطر: متن اولیه برای یک توافق  آمریکا–ایران تدوین شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/139821" target="_blank">📅 14:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139820">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
قطر: متن اولیه برای یک توافق  آمریکا–ایران تدوین شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/139820" target="_blank">📅 14:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139819">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
امام جمعه ساری: بی حجابی سبک زندگی یزیده، سرباز یزید نباشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/alonews/139819" target="_blank">📅 14:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139818">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
جمهوری‌خواهان کنگره آمریکا برای ایجاد اجماع میان اکثریت شکننده خود بر سر «قانون SAVE»، بودجه دفاعی و چندین طرح مهم دیگر با چالش روبه‌رو هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/139818" target="_blank">📅 14:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139817">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
زمین‎لرزه‌ای به بزرگی ۴.۱ ریشتر در عمق ۲۶ کیلومتری زمین، کهنوج در استان کرمان را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/139817" target="_blank">📅 14:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139815">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8Z2uoukuWwUT4AC4nyM1vc2zlTU2URFFmhK71CMo5M-s0CwZHo_xxn8_fYvVnwe8EUS0Y8uS6b5cBgAtJp8oVqWHcaw_V2WPBaB5s_Y7XG9BbxvPMo-ShSdPmdzuCj9EFj0TE8y13OgTFzm6XBEhmJ_dn4lhb5OQucnWnaQ1aR9VVeYHyMUgd4V8E8_ZSjvpmo_xhiEso7_6wxS-I1MBGqH_oD4r21AnAg9VG8akQy0hnqzSSiN0Q2nmBviV7yHjcyEiV22ZL7JH6lHrQbKvU-OJri0J4aoS2L1Fb1G8ReHdXKZxCBbhHSUrObnL37xrPSfnxpCuY_jHuft_df_jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری دیگر منتسب به انفجار
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/139815" target="_blank">📅 14:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139814">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
گویا یه مخزن گاز ترکیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/139814" target="_blank">📅 13:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139813">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
رویترز:ایالات متحده تقریباً تمام مهمات پرای‌اس‌ام (PrSM) و اِتِی‌سی‌اِم (ATACMS) را در طول جنگ با ایران مصرف کرد. همچنین، کمی کمتر از نیمی از ذخایر جهانی موشک‌های تام‌هاوک (Tomahawk) نیز به کار رفت. برخی از مقامات نگران هستند که کاهش ذخایر، آمادگی ایالات متحده را در صورت بروز درگیری‌های بعدی تحت تأثیر قرار دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/139813" target="_blank">📅 13:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139812">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
حوثی‌های یمن : با پهپاد، یه حمله دقیق به یک «هدف حساس» تو فرودگاه نجران عربستان انجام دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/139812" target="_blank">📅 13:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139811">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
گویا یه مخزن گاز ترکیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/139811" target="_blank">📅 13:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139810">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
فوری / صدای انفجار در شهرک صنعتی شمس آباد تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/139810" target="_blank">📅 13:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139809">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
حوثی‌های یمن: یک هدف حساس از عربستان سعودی را در فرودگاه نجران با پهپاد هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/139809" target="_blank">📅 13:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139807">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iWRuJKenN5ZAbn03gCraX7f72FQlfaXAM_CB3nOWMS54Mq3KGdV1ZafEB_Iw-5dJakI49-vNNMTQz6mxwPd1UhwXYMGSWscd9PhzV-icaq-nHKmOQjdeCtq_Q1KjZLNfyZaD4hNftnlJ05XzhuQS2qyW2FurtGO2VYdHfZjUP1pVSlTHWUx0deIOelYrVeKI4BS5TrXsaq_mBidOFmQqsXQqhjps86MvR0-9BNywXLFRYY8CODPnZy3G42rKMx5a5mzQF4d_hOH04fNIZAFfugk0XVhpYDdLuKhLPdiTum8seVAJa3fFuFoLawKQMXPCrgbJsRntLUBJJgoqLX5bhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vi-zL51ViEt8IyB1KTfWB9vv9JIrt4pqQy1kHBp-O0D1JUoYifJCz6mrjNOlFOMf6sPp9DU6ZfTSjeSXprzcfAoMr71vJN5R6U1Ex88NlOs59UTC8y3n6K_OvTfgLy-CyYxqgxNlCYyLk3YaMKSXNV-gnY1cqeTRVza-ucozrrb4_xYXhOUmfKTurBz9pJsHn0Rp2d_qBNcyUIhbdZUN0agz6NhSfqZlH8QkqDiTHye8ND6DuK204B8RBw543OA4QAPnzdjNuZ4v_UKSPmHBk21kymXCrPI05VnlsQj0khOrPHKA9E8IQ4jisEpaKhDR-TjYbd3i8QpCFOgtCKmdKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
کشتی یونانی که مورد هدف قرار گرفت، در حال حرکت در نزدیکی عمان بود و سیستم شناسایی خودکار آن فعال نبود. این کشتی پیش از این، در تاریخ ۲۹ جولای، با خیال راحت از مسیری عبور کرده بود که توسط ایران تعیین شده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/139807" target="_blank">📅 13:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139806">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRaZ4PmU6-YCi47Wzcu0ceaJPSUL6qwXM7EntDt3wrJXCilhJtrtfYh3TTpKhkKq44wlAbNVJJbhu_vU_SQJEudd8aOJan6ihhE0S6mu78IsnDxEyMY1QeyL3aEZFmJyi95S7v74po_L6LPzq7PRcYX9VIK7YTE6hfd3PX4wYzdaWrGwgg9h9iqUE4jx0K6Gcun4V1byaFLapu2OOlzGhmrsRSONrmMvr4lkPAHCFTL9V4tBdD1NK9BSsV0yi-3TFN4s4f-X1bPCyKxpKVwzkZ-4wC9CifRPT9gIXipieTbMjIigLyVMqHPAhR2fxcRLUs7BnrGSsmsAiKmBEv8a0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شعار علیه اسرائیل می داد اما جاسوس بود.
🔴
این مرد ‎إیلی‌ کوهین بود. مردی ‎تندرو و مخالف اسرائیل!
🔴
اما در اصل مأمور مخفی ‎اسرائیل که تا یک قدمی نخست وزیری سوریه رفت. در مجلس ملی سوریه فریاد می‌زد و اسرائیل را به هزار کار کرده و نکرده متهم می‌کرد، اما شب‌ها، برای اسرائیل اطلاعات ارسال می‌کرد.
🔴
شباهت نداره به بعضیا؟
#الی_کوهن
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/139806" target="_blank">📅 13:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139805">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBOR69aNULRJxrKsrb_UHoGqDTzMVJcTOAR669pRLjP47Nue7DfyDv-KQtX7tsdn7223FJy5NIUl_GpxzmQyPGhgTgLQmAs3YlJ9w6ZWDROrY_KzeSRkvfU9V6DI5hpz-rfPpr8AYGRMm0N4N7l8Y1_9cgoaPhSm3NVobZPpZ25wWpP0qkiL0sVhfROeIvpRfCsMX-q4S8wXXAjwBibqfJFcEQ9qWKW_YbBDxqPDfieZCeoYK-C1zjpYxV3XxRTUs7k6nGKJYUWHeujMXWqOoKUnj_eJ5zZ22-wDRnCS6RxV6Eyq4GzR8aESXGlDrwaYNwfbiFZPXEnCTBfp755ndA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اظهارات عجیب محمد باقر خرازی: تنها راه نجات ایران ساختن بمب اتم و زدن بمب اتم تو دریای اطلس و اقیانوس آرامه طوری که تو آمریکا سونامی بیاد، هرکس با ساخت بمب اتم مخالفه با اطلاع بهتون میگم اون دنیا باید جواب پس بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/139805" target="_blank">📅 13:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139804">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
دونالد ترامپ از ایران خواسته است حداکثر تا روز سه‌شنبه بر سر تنگه هرمز با میانجی‌گری عمان به توافق برسد.
🔴
بر اساس گزارش بلومبرگ، ترامپ هشدار داده است که در صورت عدم دستیابی به توافق، ایران با حملات هوایی ویرانگر مواجه خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/139804" target="_blank">📅 13:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139803">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqRjaKQNjlPBMcbZx66G1SsSFeJZkz9M375s7b2jqWa1pkbIeHOEDcs-8pWCI_ihpIgfH-z2iLmSdMDBIJyXk1k6OAVyqIB6ohQlBzXEZnQ2dUWpZVENx_Ri-I1i_P-eOxUjAQd_ysQ0uX94yiJP6wrz-wjYDe-EBe0mB5Fc0MRydMUXNYONSOEWDkuLQjnz13d_e_Vro-GiSBU8D2tkpNdn8udbRq2CrAHBoJw3miAcJBMuTbjYYY4VAJQdHyIrxk9v_JIXx7_f98s9pRP5oy3Q15t8OhgnovSxJw3Zd8lFr9Dx3qRKxACh5sVhLfSQ0-NetxlTThmks6p1rCvGkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / صدای انفجار در شهرک صنعتی شمس آباد تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/139803" target="_blank">📅 13:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139802">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
رویترز به نقل از منابع امنیتی دریایی:
یک کشتی باری در نزدیکی تنگه هرمز مورد اصابت موشک قرار گرفت؛ خدمه آن کشتی را ترک کردند و یک ملوان نیز مفقود شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/139802" target="_blank">📅 13:00 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139801">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
نعیم قاسم: رهبری آقای جدید(مجتبی خامنه‌ای) یعنی پیروزی‌های بیشتر
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/139801" target="_blank">📅 12:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139800">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
نعیم قاسم، رهبر حزب الله لبنان:
دیدار بین حزب الله و دولت سوریه هیچ مانعی ندارد و این دیدار در زمان درستش بر اساس روابط دو طرفه انجام خواهد شد.
🔴
یک سوریه پایدار منبع حمایت برای لبنان است و یک لبنان پایدار هم می تواند به ستپن استراتژیک سوریه تبدیل شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/139800" target="_blank">📅 12:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139799">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oK7XlHHRCsmM14kIImNvMxV8PwV9vbvwPqxoAf2GwPSbN9KUfl1cQMkYRjhIa0YL7Zcjbsi3UAzq00vCODV7lCcE5mNn-9FZCwZ-ZyU2YfLFjofN4-ca2hTH65hHdGk-FmsX-naWrvoTwJDg77q8Ony0EFk1AEBoU2hAB7wMlGdaRSqsQO1MYzVNfw9wuI2CewuCMnO1l1IKbPceTpFb3xZgdBcyBkp8zgCY-7f3Ateo0KM82-K93Z7a4yfcjo2nWU_T2VMNuDrOIKe57dy9u4GXjzNN8QcICIbmauLFqd1BTmnZC1J8kV9J-enRCx_PH-AJG8dctKWQdZ5g-Thv4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اگه‌ توی گوگل سرچ کنید «پدر استعفای ایران»؛ با همچین شاهکاری مواجه میشید.
✅
@AloSport</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/139799" target="_blank">📅 12:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139798">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/499a783e28.mp4?token=KBbv_0DDCv-9wNTVM8UXhPTWzzZy35dOpnK05nDzjEXORPQMI1r5OMkZ-oBejvLgkfxdRERCsZRnwLhacDOQrUiNgyJndSr3kmi5XENoA3UDFoM9BUBGpoBQ7Rey7YefzR2iGj_9Sw7GVtFIlVHyK5pbna2eIzD67SWnY1QVWChmRATwg1gPHiel1TjVBUNCchNjohPdq2DQ1woduH10rdpah-gHcZwGZAZqGjDfiZ2C5cFal9SL4rL8wDT0GP9EW47kdUfrd_-xukamSlRw74lYWULFuIaFWeUokTu_ekxDuEJF1hKEYbdwSoy3w4uZ6sxwN7q87LpOeYpnBZVzhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/499a783e28.mp4?token=KBbv_0DDCv-9wNTVM8UXhPTWzzZy35dOpnK05nDzjEXORPQMI1r5OMkZ-oBejvLgkfxdRERCsZRnwLhacDOQrUiNgyJndSr3kmi5XENoA3UDFoM9BUBGpoBQ7Rey7YefzR2iGj_9Sw7GVtFIlVHyK5pbna2eIzD67SWnY1QVWChmRATwg1gPHiel1TjVBUNCchNjohPdq2DQ1woduH10rdpah-gHcZwGZAZqGjDfiZ2C5cFal9SL4rL8wDT0GP9EW47kdUfrd_-xukamSlRw74lYWULFuIaFWeUokTu_ekxDuEJF1hKEYbdwSoy3w4uZ6sxwN7q87LpOeYpnBZVzhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
به گزارش رسانه‌های ترکیه یک کشتی باری این کشور در حمله‌ای که ظاهراً با پهپادهای اوکراینی انجام شده، در نزدیکی بندر نووروسیسک روسیه در دریای سیاه هدف قرار گرفت و دچار آتش‌سوزی شد.
🔴
بر اساس اعلام اداره کل امور دریایی ترکیه، ۲۲ خدمه سرنشین کشتی بودند که ۱۳ نفر آن‌ها شهروند ترکیه هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/139798" target="_blank">📅 12:29 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139797">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
جروزالم پست به نقل از یک منبع آگاه مدعی شد امروز سپاه پاسداران ایران به یک پایگاه نظامی آمریکا در کویت حمله کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/139797" target="_blank">📅 12:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139796">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
دور جدید مذاکرات لبنان و اسرائیل در رم آغاز شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/139796" target="_blank">📅 12:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139795">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
حاجی دلیگانی، نایب رئیس کمیسیون اصل نود: هر نوع توافق با عمان درباره تنگه هرمز باید به تصویب مجلس برسد
🔴
افکار تیم وزارت امورخارجه در دوران قاجار گیر کرده و از روی ترس و وادادگی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/139795" target="_blank">📅 12:16 · 13 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
