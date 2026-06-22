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
<img src="https://cdn4.telesco.pe/file/my-KxriZJMXFVhT6rCa8SYVNuzSrFEIjoU0oDsRvyH1Dx4tLCNJa61i8z6tTEeWXabaz-U3igWCi2eG6McHUm1s9xOzWGiq5ptVfN7_eBUFyIB_YAa1aqcZQ7Fct7CqxoodiUXeXqUGWMnVLxK6wXtcKkxjH0YVynGXkhsJdgMFFQC_-JDs8L0xdeiC3RnVsoTywhpiO9fnVRp7w-i8VXEtbnjyETSgl0H9uoB2OqNPptgof47kxUv6f8HuQeVSHt3lsr5UCJhwtTwnJBfXFY_YJaX8okzVxFx1WxsM4-2DMuGXrBuFdc_axnpOjwqoAQYz9LZTsp8HBs015esmLMA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 10:42:50</div>
<hr>

<div class="tg-post" id="msg-17892">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">انفجار در کارخانه گاز طبیعی مایع قطر؛ ۵۴ مجروح و ۱۸ مفقود  وقوع یک انفجار داخلی در مجتمع صنعتی راس‌لفان قطر که تأمین‌کننده یک‌پنجم گاز مایع (LNG) جهان است، ۵۴ مجروح برجای گذاشت و عملیات نجات برای یافتن ۱۸ مفقود همچنان ادامه دارد.</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/SBoxxx/17892" target="_blank">📅 08:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17891">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">انفجار قطر بحدی شدید بوده که در بحرین دیده و شنیده شده</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/SBoxxx/17891" target="_blank">📅 08:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17890">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بیانیه قطر و پاکستان در مورد آتش‌بس در لبنان چه می‌گوید؟
طرفین (ایران و ایالات متحده) توافق کردند که یک «واحد کنترل درگیری» را بین خود و جمهوری لبنان با میانجی‌گری تسهیل‌گران تأسیس کنند تا از پایبندی به توقف عملیات نظامی در لبنان طبق مفاد تفاهم‌نامه اطمینان حاصل شود.</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/SBoxxx/17890" target="_blank">📅 07:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17889">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
بیانیه مشترک قطر و پاکستان در مورد پایان اجلاس بورگن اشتوک
بیانیه مشترک قطر و پاکستان:
🔹
اولین جلسه مذاکرات سطح بالا تحت چارچوب تفاهم‌نامه اسلام آباد در بورگن اشتوک سوئیس با حضور نمایندگانی از جمهوری اسلامی ایران، ایالات متحده آمریکا و دو طرف میانجی، دولت قطر و جمهوری اسلامی پاکستان، به پایان رسید.
🔹
اجلاس دریاچه لوسرن در فضایی مثبت و سازنده برگزار شد. پیشرفت‌های دلگرم‌کننده‌ای از جمله ایجاد سازوکاری برای مذاکرات فنی بیشتر حاصل شده است.
🔹
بر اساس این تفاهم‌نامه، طرفین با ایجاد یک کمیته عالی رتبه موافقت کرده‌اند که نظارت سیاسی بر میانجیگری را بر عهده خواهد داشت.
🔹
مذاکره‌کنندگان ارشد به طور منظم به کمیته عالی رتبه گزارش می‌دهند و گروه‌های کاری متمرکز بر هسته‌ای، تحریم‌ها و یک گروه نظارت و حل اختلاف را برای اطمینان از اجرای مؤثر تفاهم‌نامه و سایر موارد رهبری می‌کنند.
🔹
کمیته عالی رتبه بر سر نقشه راهی برای دستیابی به توافق نهایی ظرف ۶۰ روز توافق کرده است که زمینه را برای آغاز فوری مذاکرات فنی بیشتر فراهم می‌کند.
🔹
علاوه بر این، یک خط ارتباطی بین طرفین برای مدت ذکر شده در بند ۵ تفاهم‌نامه ایجاد شده است تا از حوادث و سوءتفاهم‌ها با هدف عبور ایمن کشتی‌های تجاری از تنگه هرمز جلوگیری شود.</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SBoxxx/17889" target="_blank">📅 06:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17888">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
عراقچی
:
🔸
میانجی‌گری خستگی‌ناپذیر پاکستان و قطر باعث پیشرفت‌های بزرگی برای پایان دادن به جنگ در لبنان شد.
🔸
همچنین تحریم صادرات نفت و پتروشیمی تعلیق شد، محاصره دریایی برداشته شد، برخی از دارایی‌های مسدودشده آزاد شدند و طرح بزرگ بازسازی و توسعه اقتصادی ایران اجرایی شد.
🔸
اولین آزمون واقعی: واحد رفع درگیری‌ها در لبنان</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SBoxxx/17888" target="_blank">📅 06:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17887">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">گوستاوو پترو، رئیس‌جمهور کلمبیا، نتایج انتخابات این کشور را به رسمیت نمی‌شناسد و اسرائیل را به دستکاری در نرم‌افزار انتخاباتی کلمبیا متهم کرد</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/SBoxxx/17887" target="_blank">📅 04:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17886">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">رییس جمهور چپگرا و معتاد کلمبیا امشب شکست خورد و جایش را به یک راست گرا داد.  قاره آمریکا در حال یک دست شدن است.</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/SBoxxx/17886" target="_blank">📅 04:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17885">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دونالد ترامپ، پس از ونزوئلا، اکنون کلمبیا را تهدید می‌کند و گوستاوو پترو، رئیس‌جمهور کلمبیا، را «قاچاقچی غیرقانونی مواد مخدر» خواند.</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SBoxxx/17885" target="_blank">📅 02:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17884">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromورزش سه</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6be0b658c6.mp4?token=A23pD_nBBHednAjzwkak7N1csYpHGowg5HublH1ZTXGaAzldHk2V_yyaKr7IywgsBWngKxIoJ8yUh69hdKm2pV35K04ujFPOnrsuFQF2tvYvN7z7x5WkNvQV0gTUdoi3xqYg-wuKAk6VXNSC84Qxjwz4GJSjGC7EUMkSYu4noZnln4jaNPJ2ASbja1IGSrpK52KHbq2uMSKmTFrOdd9Oyx_7C28OnyxaGrPsVX1vAYCtY9u68ocqvlioHvGvZ5c6L_AcUnuaOI28DnYV4ZP2GybCxEqUWmQDJhQ8CpcBQunIJiejXftACxFdSi9xMt2R8pyZz177mIm8jDg86soKzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6be0b658c6.mp4?token=A23pD_nBBHednAjzwkak7N1csYpHGowg5HublH1ZTXGaAzldHk2V_yyaKr7IywgsBWngKxIoJ8yUh69hdKm2pV35K04ujFPOnrsuFQF2tvYvN7z7x5WkNvQV0gTUdoi3xqYg-wuKAk6VXNSC84Qxjwz4GJSjGC7EUMkSYu4noZnln4jaNPJ2ASbja1IGSrpK52KHbq2uMSKmTFrOdd9Oyx_7C28OnyxaGrPsVX1vAYCtY9u68ocqvlioHvGvZ5c6L_AcUnuaOI28DnYV4ZP2GybCxEqUWmQDJhQ8CpcBQunIJiejXftACxFdSi9xMt2R8pyZz177mIm8jDg86soKzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سهراب سپهری به جای طارمی؛
😂
راه حل خیابانی برای گل مردود ایران به بلژیک
🏆
در قسمت دوازدهم برجام رونمایی شد
🆔
@varzesh3</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/SBoxxx/17884" target="_blank">📅 02:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17883">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">به نظرم تنگه هرمز را بدهیم بیرو ببندد و خودمان برویم تنگه مالاکا را ببندیم!  آبش را هم بدهیم آقای میثاقی بخورد!</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SBoxxx/17883" target="_blank">📅 00:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17882">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">خارجی ها مخ شان سوت کشیده و فکر می‌کنند بیرانوند راننده یک تراکتور است!  سبحان الله!</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SBoxxx/17882" target="_blank">📅 00:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17881">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RiSRuuHgZFUfmFBGa6mYrV7bZX2f0GP3up8nu9A7dgKxsCuG6rsXkHnUmvTX1R0h3r39zISzLJ0a0oGonu-AqwTSCVhMXZRXLIlJwjTle7D2oQAN4_6GhRnlu9AjDVcWsfCcJjF4GJPK5T9wqndIEZYap4hyGhdbxgxhKMqJ_f4NJrp8SmZ6M6vvIInofdnWhfK8aPUroZi7haYU8K2wNZhiIAE7IJJoNXCGHcsN2ZeCR1wVcaZl_CICOfkR24PH3Pg1VWg7mDhPD27IF1zctXptYqI1TIe0PdHwimyLbYHLYpwHuoo-N1E5elrQaYJGpBGhTZTkQjk3nsfV6J9Apw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب تاکتیک های ناشناخته ای رو کردیم که سبحان الله!  انصافا بیرو عالی بود و ثابت کرد یک گلر خوب می‌تواند یک تیم نابود را نجات بدهد!</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/17881" target="_blank">📅 00:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17880">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORnALTFrwk_OLYqA4I2zW5fyF2vadwZrGjjsxSZlXL7hUbLvHClEecCUI-A4PyxMU4ggB3HmjAVRyi3xuEeeFu0t9W24vwzsagF7T02ZmHB2BAy16mn8UpCFOxr3iIFfys9jooVr0tmidWQT1QOkKx9GEkDFI7ZGrvovWa_pmBd5y_65ta3ScwlEk-RoF35ixKRDW7ouXZGaz9kId9NuczpHz37ZmsVxeutE29-e5zzQvoB9WfO4p66Ky0-mud9ZoLkxoktnKJASJihwuYOWqu1KfWSwJGh6D6uyCY15psy6fge-3uHjDIK5h6jNQoQ-UPdakKpln4JzvqFMcwM2iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب تاکتیک های ناشناخته ای رو کردیم که سبحان الله!
انصافا بیرو عالی بود و ثابت کرد یک گلر خوب می‌تواند یک تیم نابود را نجات بدهد!</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SBoxxx/17880" target="_blank">📅 00:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17879">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9e2be94a.mp4?token=Mc89SbE34pXMzHUMz8adfIF7mF2adOZ4PPR9AXZYZPKoQDnQNjNAa_dUUZhPsj-FJ39LvCNh86jw9_Y6RpPPoR-3ak8aTbkUK98R8dcb0azv8Nj4ooFpj9R4uO9gPlVoo0aMvq5Yoq2PSgNpWyUN2t4FbIOvy2i5C_d11Vs_p2QO71QCIDUvryVL785udH6oC9Nlow6v5m4KEmfA4NQUqR2vvPFA06uCKQ9qKnO6YcYrmrXbncH_YU-_U3YgNC7B_zTwqz21jp35-F7Iu-9HGaNlC23DBCxgbFOyjUpjLbpBi60ZaDit6ww0MHGdss3bg3umU5kgZw9anW-epVoyUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9e2be94a.mp4?token=Mc89SbE34pXMzHUMz8adfIF7mF2adOZ4PPR9AXZYZPKoQDnQNjNAa_dUUZhPsj-FJ39LvCNh86jw9_Y6RpPPoR-3ak8aTbkUK98R8dcb0azv8Nj4ooFpj9R4uO9gPlVoo0aMvq5Yoq2PSgNpWyUN2t4FbIOvy2i5C_d11Vs_p2QO71QCIDUvryVL785udH6oC9Nlow6v5m4KEmfA4NQUqR2vvPFA06uCKQ9qKnO6YcYrmrXbncH_YU-_U3YgNC7B_zTwqz21jp35-F7Iu-9HGaNlC23DBCxgbFOyjUpjLbpBi60ZaDit6ww0MHGdss3bg3umU5kgZw9anW-epVoyUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دلال های محبت فاکستانی را ببینید!
شهباز شریف از عراقچی التماس می‌کند تا با ونس ترنس دست بدهد اما عراقچی پشت کرده و می‌رود و بعد شهباز شریف و عاصم منیر شروع به ماله کشی برای آمریکایی‌ها می‌کنند!</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SBoxxx/17879" target="_blank">📅 00:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17878">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">راس الفان همان منطقه ای است که ایران تاسیسات گازی قطری ها را در مارس به آتش کشیده بود</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/17878" target="_blank">📅 23:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17877">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">خبرنگار صداوسیما:
هنوز نمی‌توان گفت که مذاکرات به پایان رسیده است یا خیر اما از شواهد به نظر می‌رسد هیئت ایرانی در آستانه بازگشت به کشور است</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/17877" target="_blank">📅 23:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17876">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">وزارت کشور قطر:   انفجار داخلی در یکی از کارخانه‌ های منطقه صنعتی راس لفان رخ داد و تیم‌های دفاع مدنی به محل حادثه اعزام شدند و هیچ گونه آسیب جانی یا نشتی ثبت نشده است.</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/17876" target="_blank">📅 23:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17875">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇶🇦
🇧🇭
— گزارش‌هایی از انفجار در قطر و بحرین.</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/17875" target="_blank">📅 23:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17874">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇶🇦
🇧🇭
— گزارش‌هایی از انفجار در قطر و بحرین.</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/17874" target="_blank">📅 23:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17873">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L53J2LGE808SCVtJGk72D_Y_wtmuPiXSm4bKwa_3lxDI4mrN74SSa-F8vBrXzMeLTZiQjERXta5EBAlA6vPyGw8Tmty9AMVB_7-HOxJsrgKKdGCBtsQWP0R0PH_WBrmlriMjI_Sso86kfmUURiQMUnmp_YQsjfQ3c8SjDxy_hJKOp8UhrFQxAlx13ie98mSTW9ms6z2Fpidmpx40lwntXKIpmoKdj9j6edmHDDSfJ4kUr1z6NJ2YI85JKy5w18nFjUo80exvL6LoE8LNu5917-mumesm1YRF8jH736VhR49-SeAlH9cqsv9wTcZh8WRJ-FZkecGVqp9oZO9xDWGvnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه به جای طارمی، سهراب سپهری رو میذاشتن نوک خط حمله ایران، الان ۱-۰ از بلژیک جلو بودیم  》Keyvan《  @OfficialPersiaTwiter</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/17873" target="_blank">📅 23:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17872">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتوییتر فارسی</strong></div>
<div class="tg-text">اگه به جای طارمی،
سهراب سپهری
رو میذاشتن نوک خط حمله ایران، الان ۱-۰ از بلژیک جلو بودیم
》Keyvan《
@OfficialPersiaTwiter</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/17872" target="_blank">📅 23:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17871">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">به اندازه قهرمانی پرسپولیس در آسیا از بلژیک جلو بودیم…
لعنت بر پرچم کمک داور !</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/17871" target="_blank">📅 23:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17870">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تیکی تاکای عالی از بچه ها !
منتهی در محوطه جریمه خودمان</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SBoxxx/17870" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17869">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتوییتر فارسی</strong></div>
<div class="tg-text">از نادر محمدخانی به اینور هر چی مدافع تیم ملی داشته امشب فیکسه.
》Footfun《
@OfficialPersiaTwiter</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SBoxxx/17869" target="_blank">📅 22:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17868">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">با نتایج درخشانی که همسایگان بیابانگردمان در عراق و عربستان و قطر گرفتند، فشار روحی از روی بچه ها اندکی برداشته شده و امشب با خیالی آسوده تر می توانند برینند.</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/17868" target="_blank">📅 22:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17867">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">مذاکرات آمریکا و ایران در سوئیس به دلیل پست ها و تهدید های امروز ترامپ، زودتر از موعد با خروج ایران پایان یافت</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/17867" target="_blank">📅 22:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17866">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">خواننده Secret Box مدتهاست که از این طرح آگاه است.</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/17866" target="_blank">📅 21:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17865">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اسرائیل در حال بررسی عقب‌نشینی محدود نیروها در جنوب لبنان است.
— کانال ۱۲ اسراییل</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/17865" target="_blank">📅 21:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17864">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مذاکرات آمریکا و ایران در سوئیس به دلیل پست ها و تهدید های امروز ترامپ، زودتر از موعد با خروج ایران پایان یافت</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/17864" target="_blank">📅 21:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17863">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">مذاکرات آمریکا و ایران در سوئیس به دلیل پست ها و تهدید های امروز ترامپ، زودتر از موعد با خروج ایران پایان یافت</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/17863" target="_blank">📅 20:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17862">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">💢
لیندسی گراهام: به مسئولین ایران می گویم؛ اگر گوش می‌دهید: وقتی از حزب‌ الله برای حمله به اسرائیل استفاده می‌کنید، سیاست جدید این خواهد بود که ما به ایران حمله خواهیم کرد.   @StrategicNews_ir</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/17862" target="_blank">📅 19:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17861">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار استراتژیک</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d0bcc2190.mp4?token=g_DxbTViR-fhQjiPBFDnJ5K5bb5d_eNHUhgcuK6mzyUobbq5SFyfK5x_jkxociveBYafw-oVCkDoRO-ytjuJY1itKYXKTNXyPgNnpV-0ZyS50Op3GK0JcR9LsJbPfu2oTvY2tk7skt_vKLUEZDzXvgUPXs81_3AtCwDjXCLTGHmcMxDpSEaQYIbqJrMtqyderCV0XOrUBYoN0Y-730hkYV1JNoKrMI3wG3ya9vLscOURVHvTamxK80V6EuTpL8YldLlfYmzEGX-1eWqyn9tT-f7fJoyMuJEGvTqYP0hwC0ewFoNJidPdg0MNEIPFK8nCWFFJtdmQhqNPeP-D40sz0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d0bcc2190.mp4?token=g_DxbTViR-fhQjiPBFDnJ5K5bb5d_eNHUhgcuK6mzyUobbq5SFyfK5x_jkxociveBYafw-oVCkDoRO-ytjuJY1itKYXKTNXyPgNnpV-0ZyS50Op3GK0JcR9LsJbPfu2oTvY2tk7skt_vKLUEZDzXvgUPXs81_3AtCwDjXCLTGHmcMxDpSEaQYIbqJrMtqyderCV0XOrUBYoN0Y-730hkYV1JNoKrMI3wG3ya9vLscOURVHvTamxK80V6EuTpL8YldLlfYmzEGX-1eWqyn9tT-f7fJoyMuJEGvTqYP0hwC0ewFoNJidPdg0MNEIPFK8nCWFFJtdmQhqNPeP-D40sz0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
لیندسی گراهام: به مسئولین ایران می گویم؛ اگر گوش می‌دهید: وقتی از حزب‌ الله برای حمله به اسرائیل استفاده می‌کنید، سیاست جدید این خواهد بود که ما به ایران حمله خواهیم کرد.
@StrategicNews_ir</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/17861" target="_blank">📅 19:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17859">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترامپ درباره لبنان:  من ناامیدم که اسرائیل نمی‌تواند حزب‌الله را از بین ببرد. آنها بدون خراب کردن ساختمان‌ها نمی‌توانند کاری انجام دهند.  من نزدیکم که این کار را به سوریه بسپارم چون او کار دقیق‌تری انجام می‌دهد</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SBoxxx/17859" target="_blank">📅 18:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17858">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">به گزارش الاخبار، جولانی در جلسه‌ای محرمانه وعده داده که از حزب الله انتقام خواهد گرفت. وی گفته :  «حالا نوبت حزب‌الله است و ما انتقام خود را فراموش نخواهیم کرد»  به نظر می‌رسد  که در صورت حملات آمریکا به ایران، جولانی از وضعیت برای باز کردن جبهه‌ای علیه لبنان…</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/17858" target="_blank">📅 18:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17857">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">من دقیقا نمیفهمم روی چه چیزی به جز پایان موقت ۶۰ روزه جنگ توافق شده؟!  لبنان؟! تنگه هرمز؟! موشکی؟! نیابتی؟!</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/17857" target="_blank">📅 17:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17856">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ:  اگر ایران تنگه هرمز را ببندد، مذاکره‌کنندگان ایرانی به کشورشان باز نخواهند گشت.</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/17856" target="_blank">📅 17:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17855">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">قراردادهای میان کشورها تحت فشار (Under Duress)  در حقوق بین‌الملل، قراردادها و معاهدات میان کشورها باید بر پایه رضایت آزادانه (free consent) منعقد شوند. مفهوم Under Duress یا تحت اکراه زمانی اعمال میشود که یک طرف با تهدید غیرقانونی، نیروی نظامی، فشار اقتصادی…</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/17855" target="_blank">📅 17:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17854">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">مدیر Secret Box از اعضای تیم دیپلماتیک کشورمان ممنون است و به شرافتشان درود میفرستد!</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SBoxxx/17854" target="_blank">📅 17:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17853">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLHotg-hm2XvbAgwKlqeZ-Q8rfACCa765lo_QzCxoLnfa7FSEmRkfFyIaZaut8JXse4hTP6m5SbhUtI3vJr5miePSl9jxkdsr518nb6PhSP0CfsL8JqswsDjoxc7VUmh_IPV4ehdZgtvxxNXLXceik45-qnrOsEUf_DMF1MtxBAJAobx7i2m3xPI88M-YSJsIUZCOzUuiMagVOS0vW2iDl_334Yix7Fzi0ihfa_7m7RFwseLmKI4XkK6FmYUIpCysbFcV_QcaSqPjuSG15CsNBxlc1zXFOa2syvM6kAfsEmlX7tQ0vcK30AYwhYmBtUz_zm5uhixwDy1NMcvU9X3IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثل اینکه یمنی ها در باب المندب فعال شده اند.</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/17853" target="_blank">📅 17:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17852">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ:  اگر ایران تنگه هرمز را ببندد، مذاکره‌کنندگان ایرانی به کشورشان باز نخواهند گشت.</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SBoxxx/17852" target="_blank">📅 17:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17851">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترامپ:
اگر ایران تنگه هرمز را ببندد، مذاکره‌کنندگان ایرانی به کشورشان باز نخواهند گشت.</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/17851" target="_blank">📅 17:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17850">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">— وزیر دفاع اسرائیل، کاتز:
"هیچ محدودیتی برای سربازان ارتش اسرائیل در لبنان برای اقدام به حذف تهدیدها وجود نداشته و وجود ندارد.
آتش‌بس دیروز اعلام شده، ارتش اسرائیل را در تمام مواضع خود در منطقه امنیتی که جوامع شمال اسرائیل را محافظت می‌کند، باقی می‌گذارد.
همانطور که نتانیاهو و من روشن کرده‌ایم: اسرائیل از منطقه امنیتی در لبنان عقب‌نشینی نخواهد کرد".</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/17850" target="_blank">📅 14:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17849">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSxHThSJfFH_uF2Nb2lTmS5EnvDgv5CUyJhyrDZEyNETH3Spkb_7BwN59pZf8pccK8YKQcWE6L7STy6_fRM2Q1l9YV9BrPtPUGMNcQkUmwjvyhf5P-Y8OXjuh3QrCeImcRAZMrlVpThk3JXlzVhhlaqbqpForoVOeKvlQxtQb6L6wnlOb4hFXXRBw2XGj3ekrEWG_5ZrFIUHpENZ7oFzIhOs73z6FNosyCbjYINwLGhEaIVPTJmv7NULbe7kceEyyUG2kZx9dnoxw4NvnxNHtM646wtGENFXnjRxXW34WDhdGmScvtBcvLF8IIQtsxA7gHiCoqMVrJ-Ol3VD3kHPFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
فدرال رزرو و پیام Hawkish به بازارها
در نشست فدرال رزرو آمریکا در ۱۸ ژوئن ۲۰۲۶، نرخ بهره بدون تغییر باقی ماند، اما لحن سیاست‌گذاران به‌وضوح
Hawkish
بود.
✔️
اعضای کمیته
FOMC
تأکید کردند که ریسک تداوم و حتی تشدید تورم همچنان بالاست. همچنین داده‌های
Dot Plot
نشان داد که بسیاری از اعضا احتمال یک مرحله افزایش نرخ بهره در ماه‌های آینده را منتفی نمی‌دانند.
اگرچه در داخل
FOMC
اختلاف‌نظرهایی وجود داشت، اما دیدگاه غالب این بود که
Rate Cut
در شرایط فعلی چندان مناسب نیست و در صورت لزوم حتی گزینه
Rate Hike
نیز می‌تواند مطرح شود.
🔽
واکنش بازار سریع و قابل‌توجه بود؛ پس از انتشار بیانیه،
USD
تقویت شد و انتظارات معامله‌گران نسبت به سیاست‌های انبساطی کاهش یافت.
نکته مهم اینجاست که بازار انتظار یک
Full Hold
(ثبات نرخ بهره بدون هیچ‌گونه سوگیری مشخص) را داشت، اما فدرال رزرو با اتخاذ یک
Hawkish Hold
نشان داد که همچنان نسبت به تورم نگران است و برای حفظ سیاست‌های پولی انقباضی آمادگی دارد.
🕯
جمع‌بندی:
فدرال رزرو برخلاف انتظارات بخش قابل‌توجهی از بازار، سیگنالی انقباضی ارسال کرد. این موضوع باعث افزایش تقاضا برای
USD
شد و تا زمانی که فشارهای تورمی به‌طور محسوسی کاهش پیدا نکنند، می‌تواند از دلار حمایت کند.
💬
برای کسب اطلاعات بیشتر، با آیدی آموزش (
@CWedu
) و یا شماره تماس 09908006002 در ارتباط باشید.
@CyclicalWaves</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/17849" target="_blank">📅 12:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17848">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⭕️
رئیس سازمان بازرسی کل کشور
:
سرویس اینترنت پرو متوقف شد و مبالغ کاربران باید عودت داده شود</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/17848" target="_blank">📅 12:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17847">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🗯
دونالد ترامپ ؛ رئیس دولت آمریکا
:
آنتروپیک دیگر تهدیدی برای امنیت ملی آمریکا نیست
وی در مصاحبه جدیدی اعلام کرد که پس از اقدامات اخیر شرکت آنتروپیک، دیگر این مجموعه و مدیرعامل آن را تهدیدی برای امنیت ملی آمریکا نمی‌داند. این موضوع پس از آن مطرح شد که آنتروپیک در پاسخ به دستور دولت، دسترسی کاربران خارجی به مدل‌های پیشرفته Fable 5 و Mythos 5 را مسدود کرد
اگرچه ترامپ از سرعت عمل و رفتار مسئولانه مدیرعامل آنتروپیک تمجید کرد اما همچنان احتمال استفاده از اختیارات اضطراری قانون تولید دفاعی را برای خود پابرجا نگه داشت. در‌همین‌حال، شرکت آنتروپیک نیز بر تعهد خود برای همکاری با دولت آمریکا جهت حفظ امنیت زیرساخت‌ها و پیشتازی در این فناوری تأکید کرده است</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/17847" target="_blank">📅 12:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17846">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhT2bt7ZDB6uY1m8DvhtYKKlQIYdFvYlv25UZ-mk9Tmm7XYcT7hMrD4gN8XH3mG9hmulZ6Rz_WVyuCFebUt5S142x7SbjVdSBemeEwbiGKrz7LsE_rJHW7avpAkiRMq2-cQ4susiR0LSMVOjr38aO_v4KSLj5nJh2xjXV6nOtA7HazNWEpBSFkPL0EjoBsdmq-_tJxeQvLd-r4-O9zfnWWf2VrFuE-wpTJfpPWCt_x5cJVuKhvC2w4qgJ2f9sJeUM0Oibx3SBCplNu_x8D-3L0BntHA-Wb6-XyffbBdh3eYsUW2ybT7p6Iqyq3gtZPBt5qxDpjoYITecmypDvZEZjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمیدانم ولی اگر بیعت کرده قطعاً مصعب سرش کلاه گذاشته بعداً</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/17846" target="_blank">📅 11:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17845">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پزشکیان:  تنها نکته آمریکا این است که ما بمب اتم نداشته باشیم؛ این موردی است که رهبر شهید هم بارها فرمودند ما بمب اتم نمی‌خواهیم. آمریکا گفت همین را بنویس و امضا کن، ما هم امضا کردیم.</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/17845" target="_blank">📅 11:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17844">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پزشکیان:
تنها نکته آمریکا این است که ما بمب اتم نداشته باشیم؛ این موردی است که رهبر شهید هم بارها فرمودند ما بمب اتم نمی‌خواهیم. آمریکا گفت همین را بنویس و امضا کن، ما هم امضا کردیم.</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/17844" target="_blank">📅 11:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17843">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">حسین شریعتمداری: مسئولان نظام برای بازگرداندن  بحرین به سرزمین اصلی ایران اقدام کنند  حسین شریعتمداری نوشت: «هموطنان بحرینی‌مان بارها اعلام کرده‌اند که خواستار پیوستن به ایران یعنی وطن اصلی خود هستند و انتظار آن است که مسئولان دست‌اندر‌کار نظام این خواسته…</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SBoxxx/17843" target="_blank">📅 11:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17842">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نبرد دریای سرخ: اسرائیل نمایندگی دیپلماتیک خود را در سومالیلند افتتاح کرد  اسرائیل چند ماه پس از به رسمیت شناختن استقلال سومالیلند، یک سفیر برای این منطقه منصوب کرد. دیپلمات مایکل لوتِم پیش از این سفیر اسرائیل در کنیا، آذربایجان و قزاقستان بود.  در ماه ژانویه،…</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/17842" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17841">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">شریعتمداری:   مسیر دفع محاصره دریایی آمریکا؛ شلیک موشک‌های ۲۵۰۰ کیلومتری با کلاهک سنگین به سمت باب المندب است</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/17841" target="_blank">📅 10:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17840">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">روزنامه وال استریت ژورنال:  آمریکا پیشنهاد داده ایران فقط برای خرید دارو، غذا و کالاهای بشردوستانه به ۶ میلیارد دلار دارایی مسدودشده‌اش در قطر دسترسی داشته باشد؛ ایران هنوز این طرح را نپذیرفته است.</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/17840" target="_blank">📅 10:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17839">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">روزنامه وال استریت ژورنال:
آمریکا پیشنهاد داده ایران فقط برای خرید دارو، غذا و کالاهای بشردوستانه به ۶ میلیارد دلار دارایی مسدودشده‌اش در قطر دسترسی داشته باشد؛ ایران هنوز این طرح را نپذیرفته است.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/17839" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17838">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">آقایان عراقچی و تیم همراه علیرغم ادامه و تشدید حملات اسرائیل به جنوب لبنان عازم ژنو شدند!</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/17838" target="_blank">📅 09:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17837">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ:   «در طول دوره آتش‌بس، به مدت ۶۰ روز هیچ عوارضی در تنگه هرمز دریافت نخواهد شد و پس از انقضای این دوره ۶۰ روزه نیز هیچ عوارضی دریافت نخواهد شد، مگر اینکه توسط و برای ایالات متحده آمریکا وضع شود، در صورتی که توافق به پایان نرسد، به عنوان جبران هزینه‌های…</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/17837" target="_blank">📅 08:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17836">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ:
«در طول دوره آتش‌بس، به مدت ۶۰ روز هیچ عوارضی در تنگه هرمز دریافت نخواهد شد و پس از انقضای این دوره ۶۰ روزه نیز هیچ عوارضی دریافت نخواهد شد، مگر اینکه توسط و برای ایالات متحده آمریکا وضع شود، در صورتی که توافق به پایان نرسد، به عنوان جبران هزینه‌های گذشته، حال و آینده برای خدماتی که به عنوان فرشته نگهبان برای کشورهای خاورمیانه ارائه شده است».</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17836" target="_blank">📅 08:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17835">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">هشدار فوری مجدد نیروی دریایی سپاه روی سیگنال رادیویی برای گشودن آتش روی هر شناوری که به تنگه هرمز نزدیک شود.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/17835" target="_blank">📅 01:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17834">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">کمرنگ شدن اهرم هرمز؛ چگونه امارات در حال خنثی‌سازی یکی از مهم‌ترین ابزارهای فشار ایران است؟  برای بیش از چهار دهه، تنگه هرمز یکی از مهم‌ترین اهرم‌های ژئوپلیتیکی ایران محسوب می‌شد. حدود یک‌پنجم تجارت دریایی نفت جهان از این گذرگاه عبور می‌کند و هرگونه تهدید…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/17834" target="_blank">📅 01:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17833">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/raX_lRjtbLju2W-UL0P3KQ3vrc8OT1eXwgCoLY2PfrTcbmMVFJ2Te9S-ZNchVBE6ZXFRMFpG5MQNkr6-j7xBQo9CMOwjAI6YbULXpY0sEqtG9-5f5zsEIbo1IAhKKCf8VzFEdEnUGvcnN1y8Guk9jRY7Jcz70e8S7nQHyJ517nBIfQvdSwjQ6rEE1wfokrcqQcjGW3oOcWshdjNNt5Ja_gLwCB_lrDXxaGqqdjm-44aHB0xNjZ4sS7sBNwvsdUDPSABe8Ij-EkKovBk2bZj_THzTzOblunQ0affC1tdjBe-OyeobaqVpu3Rm1Zvdjr9sATvaPfory025VrWr9nj6Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادداشت ترجمه شده: جنگ آینده، جنگ سیستم‌عامل‌ها  دانیلو تسوک، رئیس مرکز هوش مصنوعی وزارت دفاع اوکراین، پیش‌بینی می‌کند که جنگ در سال‌های آینده با یک پارادایم جدید مواجه خواهد شد: جنگ سیستم‌عامل‌ها. او معتقد است که هوش مصنوعی در حال تغییر بنیادی شیوه جنگ است…</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/17833" target="_blank">📅 00:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17832">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e185e8d16.mp4?token=ZVvkCGvHkyPh4bIuK_r_z9R9b-xvSoxUtzlIhJG1Z7rOcD97VDG2RY5XRokYl3GAO15VX7RhHG8PF-Pq3MtxLT9hKU_8y6NjIN2sXGjS0Pg0lQoO9w4Dfcjtgjb4bY47rcPbaeetkjylROTlhdfSHlsPQQUbrnY6e-zpvHY7lDbu3VVkug_6htrnQEsq1RD88I4GJiGybue9_kksVOq9bjjA2mtKKS7-N0eMGEy5RHM2t8u6ANgw8Yv18EHT_DHemj3FDD3N4AB3VKmFgJ83jL4XQLjDQy_LDv-2QZ-uBTX_fSXzEW8vwmkG4uvSYDC6blmgnK54EVBvRGsLNANMTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e185e8d16.mp4?token=ZVvkCGvHkyPh4bIuK_r_z9R9b-xvSoxUtzlIhJG1Z7rOcD97VDG2RY5XRokYl3GAO15VX7RhHG8PF-Pq3MtxLT9hKU_8y6NjIN2sXGjS0Pg0lQoO9w4Dfcjtgjb4bY47rcPbaeetkjylROTlhdfSHlsPQQUbrnY6e-zpvHY7lDbu3VVkug_6htrnQEsq1RD88I4GJiGybue9_kksVOq9bjjA2mtKKS7-N0eMGEy5RHM2t8u6ANgw8Yv18EHT_DHemj3FDD3N4AB3VKmFgJ83jL4XQLjDQy_LDv-2QZ-uBTX_fSXzEW8vwmkG4uvSYDC6blmgnK54EVBvRGsLNANMTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حالی که سنتکام میگوید تنگه هرمز باز است، اژدهای بندر نظر دیگری دارد!</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/17832" target="_blank">📅 23:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17831">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رسانه های اسرائیل:   عملیات ها در لبنان متوقف شد اما نیروهای ارتش اسرائیل هیچ عقب نشینی در لبنان نخواهند داشت.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/17831" target="_blank">📅 20:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17830">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اوکراین در حال جایگزینی مردان از دست رفته با وارد کردن  مردهای بیگانه است!  در هند، بنرهای دولتی اوکراین نصب شده‌اند که هندی‌ها را تشویق می‌کنند به اوکراین مهاجرت کنند تا «خانواده‌ای تشکیل دهند» و «شغلی پیدا کنند». این بنرها زنان اوکراینی جذاب و مجرد را نشان…</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/17830" target="_blank">📅 19:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17829">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6lw-7--MLxN-yBHKgaboNjSFMzizUrmzrQ6OwndNIELlicrEjqzzPpbsZJ_Ipt-DPN6dQmsVLAt5kXiwqWoEx7_rMPjxp32bXScOXxE0UNgmWUXyCOyE2UQQIPIu-mjqwHK1R0ElU7H_NnfdjAw4q1MC5UikzEqrM1rW6YLER11Q7h6f5yCFFlYiscpZikzqmQVWD52YmYPfoZR4jVMaGO03snX5fAIo31E_vySQAZ_2KqVwyIwwyaxvhVucCmsXH__g3bKzvHiof8A_JaOsjfujapPU70NaeW1nIzCCxfbbXWMvChD7sBTDKPGiZ2iFpMKBjKfPI4wRRuyL54TMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوکراین در حال جایگزینی مردان از دست رفته با وارد کردن  مردهای بیگانه است!
در هند، بنرهای دولتی اوکراین نصب شده‌اند که هندی‌ها را تشویق می‌کنند به اوکراین مهاجرت کنند تا «خانواده‌ای تشکیل دهند» و «شغلی پیدا کنند». این بنرها زنان اوکراینی جذاب و مجرد را نشان می‌دهند. در هند به دلیل فرهنگ پسرپرستی، کمبود زنان وجود دارد و زنان اغلب در صورت اطلاع از دختر بودن جنین، سقط جنین می‌کنند.
در مرحله اول، برنامه‌ریزی شده است که ۳۰۰٬۰۰۰ مهاجر وارد شود.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/17829" target="_blank">📅 19:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17828">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">رسانه های اسرائیل:   عملیات ها در لبنان متوقف شد اما نیروهای ارتش اسرائیل هیچ عقب نشینی در لبنان نخواهند داشت.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/17828" target="_blank">📅 19:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17827">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcocST6ZQNsajc6j_dPIqEUHH67f1LhJwb5qlWDPGffe5jn6iCk9hUn_LIFaV-ZzuqFki6JQVrMQWntnDpLgEEAySVZ2Y2OgFHkiSu8hxiVYu8qGDIuWsg01FmdrkASfBW3QsWVL9wYpl0bG627mG8YL-Lgr3dckB-ZY5TnrMNfA4_8EGDn5Hj5ri6hCFTqBhGXagooqoo7v-kFUQrpVJSX2HNnEZA0Tt0jXYSpwD0B_mdtd8N41KZlu_xtsEM8JJjO2r8h9SYyjg45V7CoAJuTFgZqyyphLglW8CdUYK3PXtm96tsY5b1XOl6_OosG-ImR5Z1M3vGTOHPra7klFIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عثمانی ها جوری مهمتچیکلر فوتبالی شان را بدرقه کردند که انگار دیگر نیمه نهایی در جیب شان است!  اکنون با 2 باخت 0 امتیاز دارند و بازی بعدیشان هم با آمریکای جنایتکار بی رحم است!  ُسبحان الله!</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/17827" target="_blank">📅 18:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17826">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">رسانه های اسرائیل:
عملیات ها در لبنان متوقف شد اما نیروهای ارتش اسرائیل هیچ عقب نشینی در لبنان نخواهند داشت.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/17826" target="_blank">📅 18:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17825">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">قرارگاه مرکزی خاتم‌الانبیا اعلام کرد نظر به بدعهدی و پیمان‌شکنی آشکار آمریکا نسبت به‌عدم اجرای بند اول تفاهم‌نامه پایان جنگ، و در واکنش به نقض بی‌وقفه و مستمر آتش‌بس از سوی اسرائیل در جنوب لبنان و همچنین با توجه به‌عدم عقب‌نشینی ارتش این کشور از لبنان، تنگه…</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/17825" target="_blank">📅 17:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17824">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">قرارگاه مرکزی خاتم‌الانبیا اعلام کرد نظر به بدعهدی و پیمان‌شکنی آشکار آمریکا نسبت به‌عدم اجرای بند اول تفاهم‌نامه پایان جنگ، و در واکنش به نقض بی‌وقفه و مستمر آتش‌بس از سوی اسرائیل در جنوب لبنان و همچنین با توجه به‌عدم عقب‌نشینی ارتش این کشور از لبنان، تنگه…</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/17824" target="_blank">📅 17:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17823">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">قرارگاه مرکزی خاتم‌الانبیا اعلام کرد نظر به بدعهدی و پیمان‌شکنی آشکار آمریکا نسبت به‌عدم اجرای بند اول تفاهم‌نامه پایان جنگ، و در واکنش به نقض بی‌وقفه و مستمر آتش‌بس از سوی اسرائیل در جنوب لبنان و همچنین با توجه به‌عدم عقب‌نشینی ارتش این کشور از لبنان، تنگه هرمز مجددا بسته خواهد شد.
قرارگاه مرکزی خاتم‌الانبیا اضافه کرد این گام اول «پاسخ به عهدشکنی دشمن» است و در صورت ادامه این وضعیت، گام‌های بعدی برای «پایبند کردن دشمن به اجرای تعهدات»، برنامه‌ریزی و اقدام خواهد شد.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/17823" target="_blank">📅 17:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17822">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">یارانۀ 2 دلاری خرداد به حساب سرپرستان خانوار دهک‌های ۴ تا ۹ واریز شد</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/17822" target="_blank">📅 16:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17821">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEGto9zL6qskNNMgfjHTYn-rJ4fZgJEFhZdQvGGhgDBE_nRbv1W1LrcyamNiDgk90-beNpp3EptaOYiNaM9iABMBMWXygAH9QA-Vq8aRg5UoXTatgjneEuoNeOPOwZSSq_vbW1drH9ZNUd3UbS29XOWQgea0rvv9mFY_EC8Po5PFEKX9bQ8NRIynVi2k2uhEpAw4IOaOVKiZYo8ZSK6gWp7eu8U_63Svg2Y8wOCdXqPm_WrD6-5Z664A-q68bqd0d-y-4mHfUMJMIKkYCycRmdwh6SRYzBoCMh3_LZnRMwg0zaCmN-ZRH7RIJiyjJhm9ICufk0bARKGcaRPbn9qg1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لابد چون نظامیان می دانند درگیر شدن با ارتش اول دنیا و یک قدرت هسته ای با فنآوری بالا با توییت ریدن زیر کولر متفاوت است؟!
یک بار از بچه های پدافند و لانچر و ... بپرسید شرایط چطور بود؟!</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/17821" target="_blank">📅 16:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17820">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">همه ایران و انیران خواستار ابطال این پیمان هستند جز باقر!</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/17820" target="_blank">📅 16:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17819">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">همه ایران و انیران خواستار ابطال این پیمان هستند جز باقر!</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/17819" target="_blank">📅 16:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17818">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بخدا سوگند که ما هم خواستار ابطال این تفاهم نامه هستیم!</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17818" target="_blank">📅 15:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17817">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAcMhrssP_nMDcVRGgsFVt5B2lmJ6D7dJ4wnR8G4b8VotHio-cM_WMg2yqZj66uWhg-ANmIvl56eh77ZYQrNFKTArnnpLoHRj140kHgebBUO68xDotJq1k-8UmNi1ovxsJL-yNi9u_SM-xBeGWYNPa4NGnSj6VHieeuufVO_w56ckFXrkgD7CgmJelFqkHTv4N1Wz69VZdVss4ijZaE-AnIz8T3kD5Fdf6xrLxno9kMln_f1NhfPhBAR1gMwFi6VgImmTTPr9VopnUWuWIVtEF8L6QE5ET2eP2rM7j7-BiP6dB_eLnKomWrk3YWTQzXXlb2on9e1ggj0GQ91t0vbjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/17817" target="_blank">📅 15:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17816">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">آقایان عراقچی و تیم همراه علیرغم ادامه و تشدید حملات اسرائیل به جنوب لبنان عازم ژنو شدند!</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/17816" target="_blank">📅 15:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17815">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">آقایان عراقچی و تیم همراه علیرغم ادامه و تشدید حملات اسرائیل به جنوب لبنان عازم ژنو شدند!</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/17815" target="_blank">📅 15:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17814">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhqXORyz2NgT3VX1yM0u1Ra89MkNiDFlJW5aZDNLmlOQ85ENHjlpLnC494BEsHtO18HmhQfDwogivsxxrQFLniWvkzcvozVdYicppWojfT2w4kI8ZBedZJMYMPX_Itr59NrHkL16FufhY8uBYbWORTIAxUkDJnlliXN-3C96I0L-pOuIhuZfPYV74KqbeOn1gWDBAVKjpWrrCVwptz96OxBKjBP3AExAkjChLZhull4i6BK1TXRJcy6HNGgVy_btPxgC2UWollSfi26Hdsz90SPeMyNloXmDW-CtDyLehtOrX49_6_v150uSEeuSGSlMuEqxufNqvPmqAmzvKOgkMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادداشت ترجمه شده: جنگ آینده، جنگ سیستم‌عامل‌ها
دانیلو تسوک، رئیس مرکز هوش مصنوعی وزارت دفاع اوکراین، پیش‌بینی می‌کند که جنگ در سال‌های آینده با یک پارادایم جدید مواجه خواهد شد: جنگ سیستم‌عامل‌ها. او معتقد است که هوش مصنوعی در حال تغییر بنیادی شیوه جنگ است و در سه تا پنج سال آینده، اگر درگیری با روسیه ادامه یابد، جنگ به رقابت بین سیستم‌های هوشمند تبدیل خواهد شد.
اوکراین، که پیش از تهاجم روسیه در سال ۲۰۲۲ سرمایه‌گذاری چندانی در پهپادها نداشت، اکنون به پیشتاز جنگ پهپادی تبدیل شده است. این کشور از هوش مصنوعی برای برنامه‌ریزی عملیات رزمی، تحلیل حملات موشکی روسیه و هدایت پهپادها استفاده می‌کند. تسوک می‌گوید: سیستمی که داده‌های بیشتری دارد و بهتر آنها را درک می‌کند، راه‌حل‌های بهتری پیشنهاد می‌دهد و برتری خواهد داشت.
مرکز هوش مصنوعی اوکراین، که در مارس ۲۰۲۶ تأسیس شد، در حال توسعه یک سیستم عامل واحد است که تمام داده‌های میدان جنگ را تحلیل کرده و تصمیمات را از سطح یگان‌های جلویی تا فرماندهی استراتژیک تسریع می‌بخشد. هدف، ادغام سلاح‌ها و سیستم‌های داده‌ای در یک ارگانیسم زنده واحد است که به صورت هماهنگ عمل کند.
جنگ اوکراین به یک مسابقه تسلیحاتی فناوری تبدیل شده است. شرکت‌های خارجی مانند Palantir سیستم‌های خود را در اختیار اوکراین قرار داده‌اند و پروژه Brave1 Dataroom  برای اشتراک‌گذاری داده‌های میدان جنگ با متحدان ایجاد شده است. روسیه نیز در حال توسعه قابلیت‌های هوش مصنوعی خود است و از آن برای برنامه‌ریزی حملات پهپادی و موشکی استفاده می‌کند.
تسوک می‌گوید: سوال این است که چقدر سریع می‌توانیم راه‌حل‌های خود را بسازیم و چقدر عملی آنها را پیاده‌سازی کنیم تا تأثیر اصلی را در میدان جنگ بگذاریم.  اوکراین در حال حاضر بر اصل حضور انسان در حلقه تصمیم‌گیری تأکید دارد، اما تسوک هشدار می‌دهد که ممکن است روزی برسد که سیستم‌های خودمختار آنقدر سریع عمل کنند که حضور انسان، تصمیم‌گیری را کند کند. در آن صورت، سوال این خواهد بود: چگونه می‌توانیم با تصمیماتی که سیستم‌های خودمختار پیشنهاد می‌دهند، همگام شویم؟</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/17814" target="_blank">📅 15:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17813">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqjAsGkJP01gSsWD-lfVjZV9JH313zYM7jggRjR_M9syFWZll5yU98UigvVptjKWuK9PZMiHRVTnNnr1ZZ2DRIhp_cvyUaw9dhDpSjl86vPEFuB9dcWVudyr3XuG5r5PiprUdFP_o50qYL9aaHeYMB3gib8IA41N9n8gjUw1Wl1x2HDYnkRIiNf8JIKcdwlAzkSVQQw6PnO033steysHVdlvKwaxQBDS8gG_nk4Wqz12MCHWinwvuBNUjr0PEDPqu-s75cuGb7FVhJjalUvgVjqWoauuSuidf6zK-bL3S0ps5KiG6YAtxb0eRZyAm4TPjfd1AKb4RS6sJnlk_62_RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عثمانی ها جوری مهمتچیکلر فوتبالی شان را بدرقه کردند که انگار دیگر نیمه نهایی در جیب شان است!
اکنون با 2 باخت 0 امتیاز دارند و بازی بعدیشان هم با آمریکای جنایتکار بی رحم است!
ُسبحان الله!</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17813" target="_blank">📅 13:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17812">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">وزیرخارجه فاکستان هنگام استقبال از مهمانان نشست اسلام آباد زمین خورد!</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/17812" target="_blank">📅 13:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17811">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e024f4add.mp4?token=NIuIytu3QgGQYJhOL1T6KTvZiwvR4jPhPXCB2lNaQ4CRGXsBawiMber-CzZQa23cwv2S451i-kC1C9MvZPHFP8wvCLfVWj-WRwRbACuFBGyQM_xkd3Hu1SNq0GZ1dYyYpDbYKyQwaxRhD9_veQFQcyAzzCazltVsKYaIOl_JBBK5GfloPHU5WMnrv9vL5IpLRrqHFrOeqZbLLURB8y6-l_wyRoAA9QxRbYfZnX0KYVLbPL6GaJGIrzRhVrUR44pDkRyDk1BfQbVQAn6tuhlBuwhOgYH3WhweT1-r-MTyGxFppci22mgtURkPB99zOC9GnopGpZhOzhNe2jCbrz3LRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e024f4add.mp4?token=NIuIytu3QgGQYJhOL1T6KTvZiwvR4jPhPXCB2lNaQ4CRGXsBawiMber-CzZQa23cwv2S451i-kC1C9MvZPHFP8wvCLfVWj-WRwRbACuFBGyQM_xkd3Hu1SNq0GZ1dYyYpDbYKyQwaxRhD9_veQFQcyAzzCazltVsKYaIOl_JBBK5GfloPHU5WMnrv9vL5IpLRrqHFrOeqZbLLURB8y6-l_wyRoAA9QxRbYfZnX0KYVLbPL6GaJGIrzRhVrUR44pDkRyDk1BfQbVQAn6tuhlBuwhOgYH3WhweT1-r-MTyGxFppci22mgtURkPB99zOC9GnopGpZhOzhNe2jCbrz3LRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیرخارجه فاکستان هنگام استقبال از مهمانان نشست اسلام آباد زمین خورد!</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/17811" target="_blank">📅 13:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17810">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">➡️
استارلینک با مجوز دولت عراق ، بطور رسمی در این کشور فعالیت خودرا آغاز کرد</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/17810" target="_blank">📅 11:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17809">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">📡
طالبان با دستور مستقيم ملا هبت الله آخندزاده رهبر این گروه در افغانستان ،  استفاده از گوشی های هوشمند را برای تمامی کارکنان نظامی و غیر نظامی خود ، ممنوع کرد</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/17809" target="_blank">📅 10:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17808">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3euOtJqtYm-dnzl73-wb5VN8ju44EargHOBORnWCV7OF9l-HwgvrxniVt6SvNScOdjZLKTH3XHbrm4Gke4qdAd5Tw8MrcTB4c8SEmgzpd7KSA9XYTzul7EU-h__zrQU9x0DMuLuxJAdolD9H9oRa7RO0BAmX46q6904PRC6b7mDGLJGXgpNFbiTbbhpM_EzxxevoxJLjEpRakrPtgKkhTxQqD6vYf05G41TleP3-Dwfb4JrkWcNUb35UhZEZyVAd96Er7knzxaV7GXX02feGxyc-E3gB4xfiTnO4u3erHixZ5jn0WNsYoa8uPytYH-kGqjVo2IaWFmttSNK6hwyIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ این مردک مجاهد خلق را رهبر اپوزیسیون ایران معرفی کرده!
این همان گهی است که 24 سال پیش برنامه هسته ای ایران را لو داد</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/17808" target="_blank">📅 10:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17807">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بلومبرگ: اتحادیه اروپا برنامه‌ریزی برای شراکت استراتژیک در زمینه مواد خام با ایالات متحده علیه چین کرده است  اتحادیه اروپا در نظر دارد با ایالات متحده بر سر نقشه راهی برای شراکت استراتژیک و توافقی درباره مواد معدنی حیاتی به توافق برسد. هدف کاهش قابل توجه نفوذ…</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/17807" target="_blank">📅 09:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17806">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epwaIwJwHuS9XaQzNfJAvH5HWEaplmNPEIrjeYpiTdPNEn1cpGCZW9y9HartXcYP1nkdbLty-fYyn_DXcR1o5RnEKSAYgqKdLH6Hwct-IVJaC1rO-9dCu-XBelhrgEkLkqwWxrwbM5DrKQRdHS6khcax-HTgjkX_XT_aEDE6Ul42TFSk8BROYQGbwi133PdrfcsGcdhWxHBBAJDz73w2Qx7cG_hYSqWF3Q3dzaMnGKeKjgICAWtW3tFi8xrmN7lT9ZbgW79xuh2X7RZWQSev1KZFmM-6a9WhjEhtjv8bkMuRstSFlo54yePhK8lbb46ol8-X81mTMea4eQhSeZZPpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شورای شهر نبطیه اعلام کرد با توجه به خطر احتمال بالای اشغال شهر و شدت درگیری مراسم تاسوعا و عاشورا لغو از شهروندان می‌خواهیم از شهر خارج شوند.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/17806" target="_blank">📅 01:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17805">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D11ROiCbj38Q7Txyjivllp6M8miVW7C3IO5F6aR_-G-SrLbM49eFl-4EOaCVmvuxaMwQYmx6KixmgTqsyyn0qgZ085MYUpU1kLX7jQKSQR5vUfSbJj-Nwtvu4QmGbz_vRvIRj2eF8ovdTk40R7-YEPqU16AoghQ_Bz9U0FSSi5y58nQjUVhoNTNAb9yfsMQYYUdZD6O4n1qYdmQ639mwrqgOk930oUpprkrp8_WtJcd2_qCeEN6z_Vs2_2ux-UHpXOJRIjLU9q3pgVJiEjlZ2ecJXiNBVElwKPxiNy6uGiG4kFHxI0sqO4hH46BMY4XTFrZX4ayDu8a8vH533JygZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقایقی قبل ترامپ در توییتی اعلام کرد که ایرانی ها مسئول سقوط بالگرد آپاچی آمریکایی در تنگه هرمز بوده اند.  او اعلام کرد که ایالات متحده باید به این حمله پاسخ دهد.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/17805" target="_blank">📅 00:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17804">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">محسن رضایی:
به خطای دشمن شدیدتر از آنچه بوده پاسخ می دهیم.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/17804" target="_blank">📅 00:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17803">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">جی‌دی ونس درباره پیشنهاد آمریکا به ایران:  «گزینه اول این است که همچنان مانند یک حکومت تروریستی رفتار کنید؛ در این صورت، به‌معنای واقعی کلمه هیچ چیزی به دست نخواهید آورد.  گزینه دوم این است که مانند یک حکومت عادی رفتار کنید؛ در آن صورت، ایالات متحده واقعاً…</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/17803" target="_blank">📅 22:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17802">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">چقدر این ونس ترنس گه می خورد آخر هفته ای....خفه شو دیگر</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/17802" target="_blank">📅 22:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17801">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">— رئیس‌جمهور آمریکا ترامپ:
"ایرانی‌ها، مردم بسیار باهوشی هستند. آن‌ها نوعی نابغه‌ی بدوی هستند، اما باهوش‌اند.
آن‌ها اسرائیل را منفجر می‌کردند.
اگر من نبودم، اسرائیل امروز وجود نداشت."</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/17801" target="_blank">📅 22:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17800">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">چقدر این ونس ترنس گه می خورد آخر هفته ای....خفه شو دیگر</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/17800" target="_blank">📅 21:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17799">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">خود عربها هم گفته بودند
که قرار نیست سرمایه گذاری بکنند</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/17799" target="_blank">📅 21:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17798">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">متن توافقنامه به روایت فارین پالیسی:     تفاهم اسلام‌آباد بین ایالات متحده آمریکا و جمهوری اسلامی ایران   ایالات متحده آمریکا و جمهوری اسلامی ایران و متحدان‌شان در جنگ فعلی، با امضای این تفاهم‌نامه، خاتمهٔ فوری و دائمی عملیات نظامی در همه جبهه‌ها، از جمله…</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/17798" target="_blank">📅 21:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17797">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">این هم‌ در همین راستا است:  — مقامات اسرائیلی از انتقاد تند معاون رئیس‌جمهور ایالات متحده، جی‌دی وانس، از وزرای کابینه اسرائیل و هشدار ظاهری او مبنی بر اینکه حمایت نظامی ایالات متحده از اسرائیل بی‌قید و شرط نیست، شوکه شدند.  رهبران اسرائیلی عمدتاً از پاسخگویی…</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/17797" target="_blank">📅 21:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17796">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پس بند 1 توافقنامه که رفت روی هوا.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/17796" target="_blank">📅 20:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17795">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">حزب الله عملاً دارد سیگنال ادامه حملات به شهرک های شمال اسرائیل را می دهد؛ یعنی اقدامی که پس از آغاز جنگ آغاز کرد.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/17795" target="_blank">📅 20:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17794">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‌  بیانیه کامل  اتاق عملیات حزب‌الله
🔹
رد ادعاهای دشمن اسرائیلی درباره نقض آتش‌بس توسط حزب‌الله، مقاومت اسلامی تأکید می‌کند که دشمن هرگز از ۲۷-۱۱-۲۰۲۴ تا ۱۶-۰۴-۲۰۲۶ و همچنین نتایج تفاهم اخیر ایران و آمریکا که در بند اول آن پایان جنگ در همه جبهه‌ها از جمله…</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/17794" target="_blank">📅 20:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17793">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‌
بیانیه کامل  اتاق عملیات حزب‌الله
🔹
رد ادعاهای دشمن اسرائیلی درباره نقض آتش‌بس توسط حزب‌الله، مقاومت اسلامی تأکید می‌کند که دشمن هرگز از ۲۷-۱۱-۲۰۲۴ تا ۱۶-۰۴-۲۰۲۶ و همچنین نتایج تفاهم اخیر ایران و آمریکا که در بند اول آن پایان جنگ در همه جبهه‌ها از جمله لبنان تأکید شده است، به هیچ توافق آتش‌بس پایبند نبوده است.
🔹
بلکه دشمن اسرائیلی در نقض‌های مکرر آتش‌بس افراط کرده و کشتارها و تخریب ساختمان‌های مسکونی و زیرساخت‌های غیرنظامی را مرتکب شده است، و به حملات زمینی خود از طریق تلاش برای نفوذ و کنترل روستاها و مناطقی که پیش از توافق نتوانسته بود به آنها دست یابد، ادامه داده است. تحقیر اسرائیل نسبت به آتش‌بس به حدی رسیده است که رئیس ستاد ارتش دشمن، جنایتکار آیال زامیر، دو هفته پیش اعلام کرد «در لبنان آتش‌بسی وجود ندارد»، و سخنگوی ارتش او دیروز مجدداً بر ادامه فعالیت نیروهای اشغالگر در جنوب لبنان تأکید کرد.
🔹
و طبق عادت خود، دشمن برای جبران ناتوانی در مقابله با مجاهدان مقاومت و پوشاندن شکست‌ها و خساراتش در میدان نبرد، به ارتکاب کشتار علیه غیرنظامیان و هدف قرار دادن روستاهای امن روی می‌آورد، همانطور که امروز پس از مقابله مجاهد دلیر با تلاش پیشروی به سمت تپه علی الطاهر در شب گذشته رخ داد.
🔹
مقاومت اسلامی همیشه آماده مقابله با هر تجاوزی است، مجاهدان آن با شجاعت و روحیه حسینی کربلایی از خاک و مردم خود دفاع می‌کنند و با تیرهای خود ارتش دشمن را به سختی می‌زنند، ده‌ها افسر و سرباز آن را کشته و زخمی می‌کنند و در تجهیزات آن آسیب‌های ویرانگری وارد می‌آورند، و میان ما و آنها روزها و شب‌ها و میدان نبرد ادامه دارد.
-جمعه ۱۹-۰۶-۲۰۲۶‌
-۰۴ محرم ۱۴۴۸ هـ</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17793" target="_blank">📅 20:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17792">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">شیخ نعیم قاسم: ما نقشه‌ای بلندمدت طراحی کرده‌ایم و به راه خود ادامه می‌دهیم.  ما تصمیمی حسینی و کربلایی گرفتیم؛ تصمیمی بدون حد و این تصمیم همچنان پابرجاست و هیچ بازگشتی به وضعیت پیش از ۲ مارس وجود ندارد.</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/17792" target="_blank">📅 20:13 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
